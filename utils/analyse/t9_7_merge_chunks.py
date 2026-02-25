# /// script
# requires-python = ">=3.12"
# dependencies = ["rich"]
# ///
"""Count-gated merge of chunk extractions into per-source extraction JSONs.

Won't merge a source unless ALL its chunks have extraction files.

Usage:
    uv run utils/analyse/t9_7_merge_chunks.py                  # merge all complete
    uv run utils/analyse/t9_7_merge_chunks.py --only 07        # one source
"""

import csv
import json
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

from rich.console import Console

ROOT = Path(__file__).resolve().parent.parent.parent
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
        console.print("[red]chunks-manifest.csv not found.")
        sys.exit(1)

    # Group manifest by source
    sources: dict[str, list[dict]] = defaultdict(list)
    with open(MANIFEST_CSV, newline="") as f:
        for row in csv.DictReader(f):
            sources[row["source_file"]].append(row)

    if only_id:
        sources = {k: v for k, v in sources.items() if v[0]["source_id"] == only_id or k.startswith(f"{only_id}-")}

    console.rule(f"[bold]MERGE CHUNKS — {len(sources)} sources")
    merged = 0
    skipped_incomplete = 0
    skipped_exists = 0

    for source_file, chunks in sorted(sources.items()):
        stem = source_file.replace(".md", "")
        out_path = EXTRACTIONS_DIR / f"{stem}.json"

        # Skip if merged file already exists
        if out_path.exists():
            skipped_exists += 1
            continue

        # Count-gate: check all chunks have extraction files
        total = int(chunks[0]["total_chunks"])
        chunk_files = []
        complete = True
        for c in sorted(chunks, key=lambda x: int(x["chunk_num"])):
            chunk_stem = c["chunk_file"].replace(".md", "")
            extraction_path = EXTRACTIONS_DIR / f"{chunk_stem}.json"
            if not extraction_path.exists():
                complete = False
                break
            chunk_files.append(extraction_path)

        if not complete or len(chunk_files) != total:
            skipped_incomplete += 1
            console.print(f"  [yellow]SKIP[/] {stem} ({len(chunk_files)}/{total} chunks)")
            continue

        # Merge: combine extracts from all chunks
        all_extracts = []
        first_data = None
        total_words = 0
        for cf in chunk_files:
            data = json.loads(cf.read_text())
            if first_data is None:
                first_data = data
            all_extracts.extend(data.get("extracts", []))
            total_words += data.get("chunk_words", 0)

        merged_data = {
            "source_id": first_data["source_id"],
            "source_file": first_data["source_file"],
            "source_title": first_data["source_title"],
            "author": first_data["author"],
            "year": first_data["year"],
            "chunk": None,
            "chunk_words": total_words,
            "extracts": all_extracts,
        }

        out_path.write_text(json.dumps(merged_data, indent=2, ensure_ascii=False) + "\n")
        merged += 1
        console.print(f"  [green]OK[/] {stem} — {len(all_extracts)} extracts from {total} chunks")

    console.rule("[bold]Summary")
    console.print(f"  Merged: {merged}")
    console.print(f"  Incomplete (skipped): {skipped_incomplete}")
    console.print(f"  Already merged (skipped): {skipped_exists}")

    if merged:
        subprocess.run(
            ["uv", "run", str(ROOT / "utils" / "log_action.py"),
             "--script", Path(__file__).name,
             "--message", f"Merged {merged} sources, skipped {skipped_incomplete} incomplete + {skipped_exists} existing"],
            check=False, capture_output=True,
        )


if __name__ == "__main__":
    main()
