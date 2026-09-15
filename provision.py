"""
Provision the AM coach on ElevenLabs Agents.

Uploads every markdown file in coach/kb/ and the sourced methodology corpus in
knowledge/ as knowledge base documents, then creates (or updates) an agent whose
instructions come from coach/instructions.md and whose framework detail is
retrieved from the knowledge base via RAG.

This is the architectural point of the branch: behavioral rules live in the
prompt, reference material lives in retrieval. The prompt stays small and flat
regardless of how much methodology we add.

Usage:
  .venv/Scripts/python.exe provision.py            # create or update
  .venv/Scripts/python.exe provision.py --recreate # force a brand new agent

Requires ELEVENLABS_API_KEY in .env. Writes ELEVENLABS_AGENT_ID back to .env.
"""

import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path

import requests
from dotenv import load_dotenv, set_key

load_dotenv()

API_BASE = "https://api.elevenlabs.io/v1"
API_KEY = os.getenv("ELEVENLABS_API_KEY")

ROOT = Path(__file__).parent
ENV_PATH = ROOT / ".env"
INSTRUCTIONS_PATH = ROOT / "coach" / "instructions.md"
KB_DIR = ROOT / "coach" / "kb"
KNOWLEDGE_DIR = ROOT / "knowledge"

# Maps a hash of each uploaded document to its ElevenLabs id, so a retry after a
# failed agent create reuses documents instead of uploading duplicates.
UPLOAD_CACHE = ROOT / ".kb_upload_cache.json"

AGENT_NAME = "Account Management Coach"

# Default is a stock ElevenLabs voice; override with ELEVENLABS_VOICE_ID in .env.
VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID", "cjVigY5qzO86Huf0OWal")
# English agents must use a turbo or flash v2 model; the v2.5 models are rejected.
TTS_MODEL = os.getenv("ELEVENLABS_TTS_MODEL", "eleven_flash_v2")
LLM_MODEL = os.getenv("ELEVENLABS_LLM", "claude-sonnet-4-5")

FIRST_MESSAGE = "Hey — what are you working on?"


def _headers() -> dict:
    return {"xi-api-key": API_KEY, "Content-Type": "application/json"}


def _post(path: str, payload: dict) -> dict:
    resp = requests.post(f"{API_BASE}{path}", headers=_headers(), json=payload, timeout=60)
    if not resp.ok:
        # Surface the full body — ElevenLabs returns field-level validation detail
        # here, which is the fastest way to spot a wrong config path.
        print(f"\n  ERROR {resp.status_code} on POST {path}", file=sys.stderr)
        print(f"  {resp.text}\n", file=sys.stderr)
        resp.raise_for_status()
    return resp.json()


def kb_documents() -> list[Path]:
    """Coach playbook docs plus the sourced methodology corpus."""
    return sorted(KB_DIR.glob("*.md")) + sorted(KNOWLEDGE_DIR.rglob("*.md"))


FRAMEWORK_LABELS = {
    "meddpicc": "MEDDPICC",
    "spiced": "SPICED",
    "successcoaching": "SuccessCOACHING",
    "account-management": "Account management",
    "expansion": "Expansion",
    "account-planning": "Account planning",
    "cross-framework": "Cross-framework",
}

# Sections marked "(model note)" are project inference inside a sourced
# document, so they must not inherit the document's first-party authority.
MODEL_NOTE_TAG = "[model note · secondary · P5]"


def _frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        return {}
    meta = {}
    for line in match.group(1).splitlines():
        field = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if field:
            meta[field.group(1)] = field.group(2).strip().strip('"')
    return meta


def _provenance_tag(meta: dict[str, str]) -> str:
    parts = [
        FRAMEWORK_LABELS.get(meta.get("framework", ""), meta.get("framework", "")),
        meta.get("source_org", ""),
        meta.get("source_type", ""),
        f"P{meta['priority']}" if meta.get("priority") else "",
    ]
    return "[" + " · ".join(p for p in parts if p) + "]"


def _tag_headings(text: str, tag: str) -> str:
    """Append the provenance tag to every heading.

    Retrieval returns chunks, not whole documents, and the frontmatter only
    lands in the first chunk. Tagging headings keeps framework, source and
    authority attached to each section wherever the chunker splits.
    """
    lines, in_code = [], False
    for line in text.split("\n"):
        if line.startswith("```"):
            in_code = not in_code
        elif not in_code and re.match(r"^#{1,3} ", line):
            line = f"{line} {MODEL_NOTE_TAG if '(model note)' in line else tag}"
        lines.append(line)
    return "\n".join(lines)


def _doc_name(path: Path, meta: dict[str, str]) -> str:
    if meta.get("source_title") and meta.get("source_org"):
        return f"P{meta.get('priority', '?')} {meta.get('source_type', '')} | {meta['source_org']}: {meta['source_title']}"
    # "04-renewals.md" -> "Renewals"
    return path.stem.split("-", 1)[-1].replace("-", " ").title()


def upload_knowledge_base() -> list[dict]:
    """Upload every knowledge document as text. Returns knowledge_base entries."""
    docs = kb_documents()
    if not docs:
        sys.exit(f"No markdown files found in {KB_DIR} or {KNOWLEDGE_DIR}")

    entries = []
    cache = json.loads(UPLOAD_CACHE.read_text(encoding="utf-8")) if UPLOAD_CACHE.exists() else {}
    print(f"Uploading {len(docs)} knowledge base documents...")

    for path in docs:
        text = path.read_text(encoding="utf-8").replace("\r\n", "\n")

        # Documents under 500 bytes cannot be RAG-indexed and silently fall back
        # to being stuffed into the prompt — exactly what this design avoids.
        if len(text.encode("utf-8")) < 500:
            print(f"  ! {path.name} is under 500 bytes and will not be indexed")

        meta = _frontmatter(text)
        name = _doc_name(path, meta)
        text = _tag_headings(text, _provenance_tag(meta))

        key = hashlib.sha256(f"{name}\n{text}".encode("utf-8")).hexdigest()
        doc_id = cache.get(key)
        if doc_id:
            print(f"  = {name}  ({doc_id}, already uploaded)")
        else:
            doc_id = _post("/convai/knowledge-base/text", {"text": text, "name": name})["id"]
            cache[key] = doc_id
            UPLOAD_CACHE.write_text(json.dumps(cache, indent=2), encoding="utf-8")
            print(f"  + {name}  ({doc_id})")
        entries.append({"type": "text", "name": name, "id": doc_id})

    return entries


def build_config(knowledge_base: list[dict]) -> dict:
    instructions = INSTRUCTIONS_PATH.read_text(encoding="utf-8")

    return {
        "name": AGENT_NAME,
        "conversation_config": {
            "agent": {
                "first_message": FIRST_MESSAGE,
                "language": "en",
                "prompt": {
                    "prompt": instructions,
                    "llm": LLM_MODEL,
                    "knowledge_base": knowledge_base,
                    # RAG must be explicitly enabled or the documents are ignored.
                    "rag": {
                        "enabled": True,
                        "embedding_model": "e5_mistral_7b_instruct",
                        "max_vector_distance": 0.6,
                        "max_documents_length": 50000,
                        "max_retrieved_rag_chunks_count": 20,
                    },
                },
            },
            "tts": {
                "voice_id": VOICE_ID,
                "model_id": TTS_MODEL,
            },
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--recreate",
        action="store_true",
        help="create a new agent even if ELEVENLABS_AGENT_ID is already set",
    )
    args = parser.parse_args()

    if not API_KEY:
        sys.exit("ELEVENLABS_API_KEY is not set. Add it to .env and re-run.")

    existing = os.getenv("ELEVENLABS_AGENT_ID")
    if existing and not args.recreate:
        print(f"ELEVENLABS_AGENT_ID already set ({existing}).")
        print("Re-run with --recreate to provision a fresh agent.")
        return

    knowledge_base = upload_knowledge_base()

    print(f"\nCreating agent '{AGENT_NAME}'...")
    print(f"  LLM:   {LLM_MODEL}")
    print(f"  Voice: {VOICE_ID} ({TTS_MODEL})")

    config = build_config(knowledge_base)
    agent = _post("/convai/agents/create", config)
    agent_id = agent.get("agent_id") or agent.get("id")

    if not agent_id:
        print(json.dumps(agent, indent=2))
        sys.exit("Could not find an agent id in the response.")

    set_key(str(ENV_PATH), "ELEVENLABS_AGENT_ID", agent_id)

    instructions_tokens = len(INSTRUCTIONS_PATH.read_text(encoding="utf-8")) // 4
    kb_chars = sum(p.stat().st_size for p in kb_documents())

    print(f"\nAgent created: {agent_id}")
    print("Saved ELEVENLABS_AGENT_ID to .env\n")
    print(f"  Prompt:         ~{instructions_tokens:,} tokens (sent every turn)")
    print(f"  Knowledge base: ~{kb_chars // 4:,} tokens (retrieved on demand)")
    print("\nNext:  .venv/Scripts/python.exe server.py")


if __name__ == "__main__":
    main()
