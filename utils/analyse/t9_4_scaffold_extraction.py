# /// script
# requires-python = ">=3.12"
# dependencies = ["rich"]
# ///
"""Create empty extraction JSON scaffolds for each chunk.

Reads chunks-manifest.csv and corpus-registry.csv, creates
extractions/{stem}_chunk{N}.json with source metadata and empty extracts[].

Usage:
    uv run utils/analyse/t9_4_scaffold_extraction.py              # scaffold all
    uv run utils/analyse/t9_4_scaffold_extraction.py --only 07    # one source
"""

import csv
import json
import subprocess
import sys
from pathlib import Path

from rich.console import Console

ROOT = Path(__file__).resolve().parent.parent.parent
CORPUS = ROOT / "research" / "pipeline-canon" / "corpus"
REGISTRY_CSV = CORPUS / "corpus-registry.csv"
CHUNKS_DIR = ROOT / "research" / "pipeline-canon" / "chunks"
MANIFEST_CSV = CHUNKS_DIR / "chunks-manifest.csv"
EXTRACTIONS_DIR = ROOT / "research" / "pipeline-canon" / "extractions"

console = Console()


def main():
    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__)
        sys.exit(0)

    only_id = None
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == "--only" and i + 1 < len(args):
            only_id = args[i + 1]; i += 2
        else:
            print(f"Unknown argument: {args[i]}", file=sys.stderr)
            sys.exit(1)

    if not MANIFEST_CSV.exists():
        console.print("[red]chunks-manifest.csv not found. Run chunk_corpus.py first.")
        sys.exit(1)

    # Read registry into dict keyed by file
    reg = {}
    with open(REGISTRY_CSV, newline="") as f:
        for row in csv.DictReader(f):
            reg[row["file"]] = row

    # Read manifest
    with open(MANIFEST_CSV, newline="") as f:
        manifest = list(csv.DictReader(f))

    if only_id:
        manifest = [r for r in manifest if r["source_id"] == only_id or r["source_file"].startswith(f"{only_id}-")]

    EXTRACTIONS_DIR.mkdir(parents=True, exist_ok=True)
    created = 0
    skipped = 0

    console.rule(f"[bold]SCAFFOLD EXTRACTIONS — {len(manifest)} chunks")

    for row in manifest:
        chunk_stem = row["chunk_file"].replace(".md", "")
        out_path = EXTRACTIONS_DIR / f"{chunk_stem}.json"

        if out_path.exists():
            skipped += 1
            continue

        source_meta = reg.get(row["source_file"], {})
        scaffold = {
            "source_id": row["source_id"],
            "source_file": row["source_file"],
            "source_title": source_meta.get("title", ""),
            "author": source_meta.get("author", ""),
            "year": source_meta.get("year", ""),
            "chunk": f"{row['chunk_num']}/{row['total_chunks']}",
            "chunk_file": row["chunk_file"],
            "chunk_words": int(row["words"]),
            "extracts": [],
        }

        out_path.write_text(json.dumps(scaffold, indent=2, ensure_ascii=False) + "\n")
        created += 1

    console.print(f"  Created: {created}")
    console.print(f"  Skipped (exist): {skipped}")

    subprocess.run(
        ["uv", "run", str(ROOT / "utils" / "log_action.py"),
         "--script", Path(__file__).name,
         "--message", f"Created {created} extraction scaffolds, skipped {skipped} existing"],
        check=False, capture_output=True,
    )


if __name__ == "__main__":
    main()
