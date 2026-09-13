"""
Pre-flight check for the ElevenLabs AM coach.

Verifies the prompt and knowledge base are intact and the environment is
configured, before spending an API call on provisioning.

  .venv/Scripts/python.exe scripts/smoke_check.py
"""

import os
import sys
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]

# Documents under this size cannot be RAG-indexed and silently fall back to
# being stuffed into the prompt — which defeats the point of the split.
RAG_MIN_BYTES = 500


def main() -> None:
    load_dotenv(ROOT / ".env")
    problems: list[str] = []

    if not os.getenv("ELEVENLABS_API_KEY"):
        problems.append("ELEVENLABS_API_KEY is not set (copy .env.example to .env)")

    instructions = ROOT / "coach" / "instructions.md"
    if not instructions.exists():
        problems.append("coach/instructions.md is missing")
    elif len(instructions.read_text(encoding="utf-8")) < 1000:
        problems.append("coach/instructions.md looks truncated")

    kb_dir = ROOT / "coach" / "kb"
    docs = sorted(kb_dir.glob("*.md")) if kb_dir.exists() else []
    if not docs:
        problems.append("no knowledge base documents found in coach/kb/")

    # Sourced methodology corpus: every source doc must stay attributable.
    corpus = sorted((ROOT / "knowledge").rglob("*.md"))
    required = ("framework", "topic", "source_url", "source_title", "source_org", "retrieved_date")
    for doc in corpus:
        if doc.name == "INDEX.md":
            continue
        head = doc.read_text(encoding="utf-8")[:1500]
        missing = [k for k in required if f"\n{k}:" not in head]
        if missing:
            problems.append(f"{doc.relative_to(ROOT)} missing metadata: {', '.join(missing)}")
    docs += corpus

    for doc in docs:
        size = doc.stat().st_size
        if size < RAG_MIN_BYTES:
            problems.append(f"{doc.name} is {size}B, under the {RAG_MIN_BYTES}B RAG floor")

    if not (ROOT / "index.html").exists():
        problems.append("index.html is missing")

    if problems:
        print("Smoke check failed:\n")
        for problem in problems:
            print(f"  - {problem}")
        sys.exit(1)

    prompt_tokens = len(instructions.read_text(encoding="utf-8")) // 4
    kb_tokens = sum(d.stat().st_size for d in docs) // 4

    print("Smoke check passed.\n")
    print(f"  Prompt:         ~{prompt_tokens:,} tokens  (sent every turn)")
    print(f"  Knowledge base: ~{kb_tokens:,} tokens across {len(docs)} docs (retrieved on demand)")

    if not os.getenv("ELEVENLABS_AGENT_ID"):
        print("\n  No ELEVENLABS_AGENT_ID yet — run provision.py next.")


if __name__ == "__main__":
    main()
