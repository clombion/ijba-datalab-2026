# /// script
# requires-python = ">=3.12"
# dependencies = ["rich"]
# ///
"""T10 Scaffold — create relevance JSONs from merged T9 extractions.

Reads merged extractions/{stem}.json (chunk=null), creates
relevance/{stem}.json with each extract's text + classification
but llm_relevance: null.

Usage:
    uv run utils/scaffold_relevance.py              # scaffold all
    uv run utils/scaffold_relevance.py --only 07
"""

import json
import sys
from pathlib import Path

from rich.console import Console

ROOT = Path(__file__).resolve().parent.parent.parent
EXTRACTIONS_DIR = ROOT / "research" / "pipeline-canon" / "extractions"
RELEVANCE_DIR = ROOT / "research" / "pipeline-canon" / "relevance"

console = Console()


def main():
    only_id = None
    args = sys.argv[1:]
    for i, arg in enumerate(args):
        if arg == "--only" and i + 1 < len(args):
            only_id = args[i + 1]

    RELEVANCE_DIR.mkdir(parents=True, exist_ok=True)

    # Find merged extraction files (chunk: null)
    files = sorted(EXTRACTIONS_DIR.glob("*.json"))
    # Filter to merged files only (no _chunk in name)
    merged = [f for f in files if "_chunk" not in f.name]

    if only_id:
        merged = [f for f in merged if f.name.startswith(f"{only_id}-")]

    console.rule(f"[bold]T10 SCAFFOLD RELEVANCE — {len(merged)} sources")
    created = 0
    skipped = 0

    for f in merged:
        out_path = RELEVANCE_DIR / f.name
        if out_path.exists():
            skipped += 1
            continue

        data = json.loads(f.read_text())
        extracts = data.get("extracts", [])

        rel_extracts = []
        for ext in extracts:
            rel_extracts.append({
                "extract": ext["extract"],
                "chapter": ext.get("chapter", ""),
                "pipeline_step": ext["pipeline_step"],
                "secondary_step": ext.get("secondary_step"),
                "extract_type": ext["extract_type"],
                "themes": ext.get("themes", []),
                "notes": ext.get("notes", ""),
                "llm_relevance": None,
                "relevance_rationale": None,
            })

        rel_data = {
            "source_id": data["source_id"],
            "source_file": data["source_file"],
            "source_title": data["source_title"],
            "author": data["author"],
            "year": data["year"],
            "extracts": rel_extracts,
        }

        out_path.write_text(json.dumps(rel_data, indent=2, ensure_ascii=False) + "\n")
        created += 1

    console.print(f"  Created: {created}")
    console.print(f"  Skipped (exist): {skipped}")

    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent.parent)); from log_action import log_action
        if created:
            log_action("scaffold_relevance.py", f"Created {created} relevance scaffolds, skipped {skipped} existing")
    except ImportError:
        pass


if __name__ == "__main__":
    main()
