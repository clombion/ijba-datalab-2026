# /// script
# requires-python = ">=3.12"
# dependencies = ["typer>=0.9.0", "rich>=13.0.0"]
# ///
"""Scaffold per-step mapping files for disrupted extracts.

Creates one JSON file per pipeline step in mapping/, each containing
the step's disrupted extracts with null mapping fields. The full taxonomy
is embedded in each file as reference context for cross-step mapping.

Input: disrupted.csv, taxonomy.csv
Prerequisites: t1_1_filter_disrupted, t4_1_merge_taxonomy in manifest
Output: mapping/{Step}.json (7 files)

Usage:
    uv run research/pipeline-canon-2/scripts/t5_1_scaffold_mapping.py
    uv run research/pipeline-canon-2/scripts/t5_1_scaffold_mapping.py --dry-run
    uv run research/pipeline-canon-2/scripts/t5_1_scaffold_mapping.py --status

Exit codes:
    0  Success
    1  General error
    5  Output already exists (use --force)
    66 Input not found
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console

__version__ = "1.0.0"

PIPELINE_ROOT = Path(__file__).resolve().parent.parent
DISRUPTED_CSV = PIPELINE_ROOT / "disrupted.csv"
TAXONOMY_CSV = PIPELINE_ROOT / "taxonomy.csv"
MAPPING_DIR = PIPELINE_ROOT / "mapping"
REQUIRES_STEPS = ["t1_1_filter_disrupted", "t4_1_merge_taxonomy"]
PIPELINE_STEPS = ["Define", "Find", "Get", "Verify", "Clean", "Analyse", "Present"]

console = Console(stderr=True)
app = typer.Typer(help=__doc__, add_completion=False)


def version_callback(value: bool) -> None:
    if value:
        print(f"t5-1-scaffold-mapping {__version__}")
        raise typer.Exit()


@app.command()
def main(
    dry_run: Annotated[bool, typer.Option("--dry-run", help="Show counts without writing.")] = False,
    status: Annotated[bool, typer.Option("--status", help="Report fill progress across all step files.")] = False,
    force: Annotated[bool, typer.Option("--force", help="Overwrite existing output.")] = False,
    version: Annotated[bool | None, typer.Option("--version", callback=version_callback, is_eager=True, help="Show version.")] = None,
) -> None:
    """Scaffold per-step mapping files."""
    if status:
        result = {}
        for step in PIPELINE_STEPS:
            step_file = MAPPING_DIR / f"{step}.json"
            if not step_file.exists():
                result[step] = {"scaffolded": False}
                continue
            with open(step_file, encoding="utf-8") as f:
                data = json.load(f)
            extracts = data.get("extracts", [])
            total = len(extracts)
            filled = sum(1 for e in extracts if e.get("practice_ids") is not None)
            result[step] = {"total": total, "filled": filled, "remaining": total - filled}
        print(json.dumps(result, indent=2))
        raise typer.Exit(0)

    from manifest import check_manifest_prerequisites
    check_manifest_prerequisites(REQUIRES_STEPS)

    for path, label in [(DISRUPTED_CSV, "disrupted.csv"), (TAXONOMY_CSV, "taxonomy.csv")]:
        if not path.exists():
            console.print(f"[red]Input not found ({label}): {path}[/red]")
            raise typer.Exit(66)

    # Check if output exists
    existing = [s for s in PIPELINE_STEPS if (MAPPING_DIR / f"{s}.json").exists()]
    if existing and not force:
        console.print(f"[yellow]Mapping files already exist for: {', '.join(existing)}[/yellow]")
        raise typer.Exit(5)

    # Read taxonomy
    with open(TAXONOMY_CSV, newline="", encoding="utf-8") as f:
        taxonomy = list(csv.DictReader(f))

    # Read disrupted extracts
    with open(DISRUPTED_CSV, newline="", encoding="utf-8") as f:
        disrupted = list(csv.DictReader(f))

    # Group by step
    by_step: dict[str, list[dict]] = {step: [] for step in PIPELINE_STEPS}
    for row in disrupted:
        step = row.get("pipeline_step", "")
        if step in by_step:
            by_step[step].append(row)

    console.print(f"Disrupted extracts: {len(disrupted)}")
    console.print(f"Taxonomy practices: {len(taxonomy)}")
    for step in PIPELINE_STEPS:
        console.print(f"  {step}: {len(by_step[step])}")

    if dry_run:
        console.print("[yellow]Dry run — no files written.[/yellow]")
        print(json.dumps({s: len(rows) for s, rows in by_step.items()}))
        raise typer.Exit(0)

    MAPPING_DIR.mkdir(parents=True, exist_ok=True)
    files_written = 0

    for step in PIPELINE_STEPS:
        rows = by_step[step]
        if not rows:
            continue

        extracts = []
        for i, row in enumerate(rows):
            extracts.append({
                "index": i,
                "source_id": row.get("source_id", ""),
                "pipeline_step": row.get("pipeline_step", ""),
                "extract_type": row.get("extract_type", ""),
                "llm_relevance": row.get("llm_relevance", ""),
                "extract": row.get("extract", ""),
                "relevance_rationale": row.get("relevance_rationale", ""),
                # Null mapping fields for LLM to fill
                "practice_ids": None,
                "mapping_rationale": None,
                "mapping_status": None,
                "disruption_type": None,
                "notes": None,
            })

        step_data = {
            "step": step,
            "extract_count": len(extracts),
            "taxonomy": taxonomy,
            "extracts": extracts,
        }

        step_file = MAPPING_DIR / f"{step}.json"
        with open(step_file, "w", encoding="utf-8") as f:
            json.dump(step_data, f, indent=2, ensure_ascii=False)
        files_written += 1

    console.print(f"[green]Written: {MAPPING_DIR}/ ({files_written} files)[/green]")

    from log_action import log_action
    from manifest import append_manifest

    for step in PIPELINE_STEPS:
        if by_step[step]:
            append_manifest("t5_1_scaffold_mapping", f"mapping/{step}.json", ["disrupted.csv", "taxonomy.csv"])

    log_action("t5_1_scaffold_mapping.py", f"Scaffolded {files_written} mapping files for {len(disrupted)} extracts")

    print(json.dumps({s: len(rows) for s, rows in by_step.items()}))


if __name__ == "__main__":
    app()
