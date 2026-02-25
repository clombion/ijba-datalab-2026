# /// script
# requires-python = ">=3.12"
# dependencies = ["rich"]
# ///
"""T11 Final merge — count-gated join of extractions + relevance → horizon-table.csv.

All 81 sources must have T9 + T10 complete.

Usage:
    uv run utils/analyse/t11_1_merge_horizon.py                  # merge all
    uv run utils/analyse/t11_1_merge_horizon.py --force          # skip count gate
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
EXTRACTIONS_DIR = ROOT / "research" / "pipeline-canon" / "extractions"
RELEVANCE_DIR = ROOT / "research" / "pipeline-canon" / "relevance"
HORIZON_CSV = ROOT / "research" / "pipeline-canon" / "horizon-table.csv"

console = Console()

CSV_FIELDS = [
    "source_id", "source_file", "source_title", "author", "year",
    "extract", "chapter", "pipeline_step", "secondary_step",
    "extract_type", "themes", "llm_relevance", "relevance_rationale", "notes",
]


def main():
    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__)
        sys.exit(0)

    force = False
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == "--force":
            force = True; i += 1
        else:
            print(f"Unknown argument: {args[i]}", file=sys.stderr)
            sys.exit(1)

    # Read registry
    registry = []
    with open(REGISTRY_CSV, newline="") as f:
        for row in csv.DictReader(f):
            registry.append(row)

    console.rule(f"[bold]T11 MERGE HORIZON — {len(registry)} sources")

    # Count gate
    if not force:
        missing_extract = []
        missing_relevance = []
        for reg in registry:
            stem = reg["file"].replace(".md", "")
            ext_path = EXTRACTIONS_DIR / f"{stem}.json"
            rel_path = RELEVANCE_DIR / f"{stem}.json"
            if not ext_path.exists():
                missing_extract.append(stem)
            if not rel_path.exists():
                missing_relevance.append(stem)

        if missing_extract:
            console.print(f"  [red]Missing extractions ({len(missing_extract)}):[/] {', '.join(missing_extract[:10])}")
        if missing_relevance:
            console.print(f"  [red]Missing relevance ({len(missing_relevance)}):[/] {', '.join(missing_relevance[:10])}")
        if missing_extract or missing_relevance:
            console.print("  [red]Count gate failed.[/] Use --force to override.")
            sys.exit(1)

    # Build horizon table
    rows = []
    for reg in registry:
        stem = reg["file"].replace(".md", "")
        rel_path = RELEVANCE_DIR / f"{stem}.json"

        if not rel_path.exists():
            continue

        data = json.loads(rel_path.read_text())
        for ext in data.get("extracts", []):
            rows.append({
                "source_id": data["source_id"],
                "source_file": data["source_file"],
                "source_title": data["source_title"],
                "author": data["author"],
                "year": data["year"],
                "extract": ext["extract"],
                "chapter": ext.get("chapter", ""),
                "pipeline_step": ext["pipeline_step"],
                "secondary_step": ext.get("secondary_step") or "",
                "extract_type": ext["extract_type"],
                "themes": "; ".join(ext.get("themes", [])),
                "llm_relevance": ext.get("llm_relevance", ""),
                "relevance_rationale": ext.get("relevance_rationale", ""),
                "notes": ext.get("notes", ""),
            })

    with open(HORIZON_CSV, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    console.print(f"  Total rows: {len(rows)}")
    console.print(f"  Written to: {HORIZON_CSV.relative_to(ROOT)}")

    subprocess.run(
        ["uv", "run", str(ROOT / "utils" / "log_action.py"),
         "--script", Path(__file__).name,
         "--message", f"Merged {len(rows)} extracts from {len(registry)} sources into horizon-table.csv"],
        check=False, capture_output=True,
    )


if __name__ == "__main__":
    main()
