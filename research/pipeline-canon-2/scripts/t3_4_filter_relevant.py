# /// script
# requires-python = ">=3.12"
# dependencies = ["typer>=0.9.0", "rich>=13.0.0"]
# ///
"""Filter podcast use cases to relevant practitioner-level entries.

Reads the mapped podcast file and filters to relevant == true AND
granularity == "practitioner". Outputs with null practice fields for filling.

Input: practices/podcast_mapped.json
Prerequisites: t3_1_scaffold_podcast_mapping in manifest
Output: practices/podcast_filtered.json

Usage:
    uv run research/pipeline-canon-2/scripts/t3_4_filter_relevant.py
    uv run research/pipeline-canon-2/scripts/t3_4_filter_relevant.py --dry-run

Exit codes:
    0  Success
    1  General error
    5  Output already exists (use --force)
    66 Input not found
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console

__version__ = "1.0.0"

PIPELINE_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = PIPELINE_ROOT / "practices" / "podcast_mapped.json"
OUTPUT_FILE = PIPELINE_ROOT / "practices" / "podcast_filtered.json"
REQUIRES_STEPS = ["t3_1_scaffold_podcast_mapping"]

console = Console(stderr=True)
app = typer.Typer(help=__doc__, add_completion=False)


def version_callback(value: bool) -> None:
    if value:
        print(f"t3-4-filter-relevant {__version__}")
        raise typer.Exit()


@app.command()
def main(
    dry_run: Annotated[bool, typer.Option("--dry-run", help="Show counts without writing.")] = False,
    force: Annotated[bool, typer.Option("--force", help="Overwrite existing output.")] = False,
    version: Annotated[bool | None, typer.Option("--version", callback=version_callback, is_eager=True, help="Show version.")] = None,
) -> None:
    """Filter podcast use cases to practitioner-relevant entries."""
    from manifest import check_manifest_prerequisites
    check_manifest_prerequisites(REQUIRES_STEPS)

    if not INPUT_FILE.exists():
        console.print(f"[red]Input not found: {INPUT_FILE}[/red]")
        raise typer.Exit(66)

    if OUTPUT_FILE.exists() and not force:
        console.print(f"[yellow]Output already exists: {OUTPUT_FILE}[/yellow]")
        raise typer.Exit(5)

    with open(INPUT_FILE, encoding="utf-8") as f:
        data = json.load(f)

    # Filter: relevant AND practitioner granularity
    filtered = []
    for uc in data:
        if uc.get("relevant") is True and uc.get("granularity") == "practitioner":
            entry = dict(uc)
            entry["practices"] = []
            entry["filter_index"] = len(filtered)
            filtered.append(entry)

    console.print(f"Total use cases: {len(data)}")
    console.print(f"Relevant + practitioner: {len(filtered)}")

    if dry_run:
        console.print("[yellow]Dry run — no file written.[/yellow]")
        print(json.dumps({"total": len(data), "filtered": len(filtered)}))
        raise typer.Exit(0)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(filtered, f, indent=2, ensure_ascii=False)

    console.print(f"[green]Written: {OUTPUT_FILE}[/green]")

    from log_action import log_action
    from manifest import append_manifest

    append_manifest("t3_4_filter_relevant", "practices/podcast_filtered.json", ["practices/podcast_mapped.json"])
    log_action("t3_4_filter_relevant.py", f"Filtered {len(filtered)} relevant practitioner use cases from {len(data)} total")

    print(json.dumps({"total": len(data), "filtered": len(filtered)}))


if __name__ == "__main__":
    app()
