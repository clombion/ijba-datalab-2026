# /// script
# requires-python = ">=3.12"
# dependencies = ["rich"]
# ///
"""Classify chunks as context_ok or context_needed based on heading quality.

Reads each chunk file, inspects its headings, and updates chunks-manifest.csv
with a context_status column.

Usage:
    uv run utils/classify_chunks.py                # classify all
    uv run utils/classify_chunks.py --only 07      # one source
"""

import csv
import re
import sys
from pathlib import Path

from rich.console import Console

ROOT = Path(__file__).resolve().parent.parent.parent
CHUNKS_DIR = ROOT / "research" / "pipeline-canon" / "chunks"
MANIFEST_CSV = CHUNKS_DIR / "chunks-manifest.csv"

console = Console()

# NICAR filename heading: ## 2024-ai-101.md
RE_NICAR_FILENAME = re.compile(r"^\d{4}-.+")
# Backtick-wrapped headings (OCR garbage)
RE_BACKTICK_HEADING = re.compile(r"`[^`]+`")


def classify_chunk(chunk_path: Path) -> str:
    """Classify a chunk as context_ok or context_needed."""
    text = chunk_path.read_text()

    # Extract headings from chunk body (skip metadata header)
    headings = []
    for line in text.splitlines():
        if line.startswith("<!--"):
            continue
        m = re.match(r"^#{1,6}\s+(.+)", line)
        if m:
            headings.append(m.group(1).strip())

    if not headings:
        return "context_needed"

    # All headings are NICAR filename patterns
    nicar_count = sum(1 for h in headings if RE_NICAR_FILENAME.match(h))
    if nicar_count == len(headings):
        return "context_needed"

    # All headings contain backticks (OCR garbage)
    backtick_count = sum(1 for h in headings if RE_BACKTICK_HEADING.search(h))
    if backtick_count == len(headings):
        return "context_needed"

    # Check if chunk came from word_boundary strategy (read from manifest later)
    # For now, headings exist and look reasonable
    return "context_ok"


def main():
    only_id = None
    args = sys.argv[1:]
    for i, arg in enumerate(args):
        if arg == "--only" and i + 1 < len(args):
            only_id = args[i + 1]

    if not MANIFEST_CSV.exists():
        console.print("[red]chunks-manifest.csv not found. Run chunk_corpus.py first.")
        sys.exit(1)

    # Read manifest
    with open(MANIFEST_CSV, newline="") as f:
        rows = list(csv.DictReader(f))

    if only_id:
        rows = [r for r in rows if r["source_id"] == only_id or r["source_file"].startswith(f"{only_id}-")]

    ok_count = 0
    needed_count = 0
    needed_files = []

    console.rule(f"[bold]CLASSIFY CHUNKS — {len(rows)} chunks")

    for row in rows:
        chunk_path = CHUNKS_DIR / row["chunk_file"]
        if not chunk_path.exists():
            console.print(f"  [red]MISSING[/] {row['chunk_file']}")
            continue

        # word_boundary strategy → always context_needed
        if row.get("strategy") == "word_boundary":
            status = "context_needed"
        else:
            status = classify_chunk(chunk_path)

        row["context_status"] = status

        if status == "context_needed":
            needed_count += 1
            needed_files.append(row["chunk_file"])
            console.print(f"  [yellow]NEEDED[/] {row['chunk_file']}")
        else:
            ok_count += 1

    # Write updated manifest
    fields = list(rows[0].keys()) if rows else []
    with open(MANIFEST_CSV, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    console.rule("[bold]Summary")
    console.print(f"  context_ok: {ok_count}")
    console.print(f"  context_needed: {needed_count}")
    if needed_files:
        console.print(f"  Needed: {', '.join(needed_files)}")

    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent.parent)); from log_action import log_action
        log_action("classify_chunks.py", f"{ok_count} chunks context_ok, {needed_count} chunks context_needed\ncontext_needed: {', '.join(needed_files)}")
    except ImportError:
        pass


if __name__ == "__main__":
    main()
