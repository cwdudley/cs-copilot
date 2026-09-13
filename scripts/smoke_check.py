"""
Pre-flight check for the ElevenLabs AM coach.

Verifies the prompt and knowledge base are intact, every knowledge document
carries complete provenance metadata, and the environment is configured —
before spending an API call on provisioning.

  .venv/Scripts/python.exe scripts/smoke_check.py
"""

import os
import re
import sys
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]

# Documents under this size cannot be RAG-indexed and silently fall back to
# being stuffed into the prompt — which defeats the point of the split.
RAG_MIN_BYTES = 500

REQUIRED_METADATA = (
    "framework",
    "topic",
    "source_title",
    "source_org",
    "source_authority",
    "source_type",
    "framework_version",
    "priority",
    "public_url",
    "source_url",
    "published_date",
    "retrieved_date",
    "license",
    "reproduction_status",
)

# Authority ranking, highest first. "secondary" covers project-authored
# synthesis, which ranks below every first-party source.
SOURCE_TYPES = {
    "canonical": 1,
    "practitioner_article": 2,
    "research": 3,
    "historical": 4,
    "secondary": 5,
}


def frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"\A---\n(.*?)\n---\n", text.replace("\r\n", "\n"), re.DOTALL)
    if not match:
        return {}
    meta = {}
    for line in match.group(1).splitlines():
        field = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if field:
            meta[field.group(1)] = field.group(2).strip().strip('"')
    return meta


def check_metadata(doc: Path) -> list[str]:
    rel = doc.relative_to(ROOT)
    meta = frontmatter(doc.read_text(encoding="utf-8"))
    if not meta:
        return [f"{rel} has no frontmatter"]

    problems = []
    missing = [k for k in REQUIRED_METADATA if not meta.get(k)]
    if missing:
        problems.append(f"{rel} missing metadata: {', '.join(missing)}")

    source_type = meta.get("source_type")
    if source_type and source_type not in SOURCE_TYPES:
        problems.append(f"{rel} has unknown source_type '{source_type}'")

    priority = meta.get("priority", "")
    if priority and (not priority.isdigit() or not 1 <= int(priority) <= 5):
        problems.append(f"{rel} priority must be 1-5, got '{priority}'")
    elif priority and source_type in SOURCE_TYPES and int(priority) != SOURCE_TYPES[source_type]:
        problems.append(f"{rel} priority {priority} does not match source_type '{source_type}'")

    return problems


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

    docs = sorted((ROOT / "coach" / "kb").glob("*.md")) + sorted((ROOT / "knowledge").rglob("*.md"))
    if not docs:
        problems.append("no knowledge base documents found")

    for doc in docs:
        problems += check_metadata(doc)
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
