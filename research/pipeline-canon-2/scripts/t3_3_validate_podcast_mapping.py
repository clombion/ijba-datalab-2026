# /// script
# requires-python = ">=3.12"
# dependencies = ["typer>=0.9.0", "rich>=13.0.0"]
# ///
"""Validate podcast use case mapping completeness and quality.

Checks: all entries mapped, valid enums, rationale present.
Reports distribution by step, granularity, and relevance.

Input: practices/podcast_mapped.json
Prerequisites: t3_1_scaffold_podcast_mapping in manifest

Usage:
    uv run research/pipeline-canon-2/scripts/t3_3_validate_podcast_mapping.py
    uv run research/pipeline-canon-2/scripts/t3_3_validate_podcast_mapping.py --json

Exit codes:
    0  PASS
    1  FAIL
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
REQUIRES_STEPS = ["t3_1_scaffold_podcast_mapping"]

VALID_STEPS = {"Define", "Find", "Get", "Verify", "Clean", "Analyse", "Present"}
VALID_GRANULARITY = {"practitioner", "organizational", "strategic"}

console = Console(stderr=True)
app = typer.Typer(help=__doc__, add_completion=False)


def version_callback(value: bool) -> None:
    if value:
        print(f"t3-3-validate-podcast-mapping {__version__}")
        raise typer.Exit()


@app.command()
def main(
    json_output: Annotated[bool, typer.Option("--json", help="Machine-readable JSON output.")] = False,
    version: Annotated[bool | None, typer.Option("--version", callback=version_callback, is_eager=True, help="Show version.")] = None,
) -> None:
    """Validate podcast mapping completeness and quality."""
    from manifest import check_manifest_prerequisites
    check_manifest_prerequisites(REQUIRES_STEPS)

    if not INPUT_FILE.exists():
        console.print(f"[red]Input not found: {INPUT_FILE}[/red]")
        raise typer.Exit(66)

    with open(INPUT_FILE, encoding="utf-8") as f:
        data = json.load(f)

    errors: list[dict] = []
    warnings: list[dict] = []

    # Check completeness
    unmapped = [i for i, uc in enumerate(data) if uc.get("pipeline_steps") is None]
    if unmapped:
        errors.append({"type": "incomplete", "count": len(unmapped), "indices": unmapped[:10]})

    # Validate enums and rationale
    by_step: dict[str, int] = {}
    by_gran: dict[str, int] = {}
    relevant_count = 0
    practitioner_relevant = 0

    for i, uc in enumerate(data):
        if uc.get("pipeline_steps") is None:
            continue

        steps = uc["pipeline_steps"]
        gran = uc.get("granularity", "")
        rel = uc.get("relevant")
        rat = uc.get("mapping_rationale", "")

        # Validate steps
        for step in steps:
            if step not in VALID_STEPS:
                errors.append({"type": "invalid_step", "index": i, "value": step})
            by_step[step] = by_step.get(step, 0) + 1

        # Validate granularity
        if gran not in VALID_GRANULARITY:
            errors.append({"type": "invalid_granularity", "index": i, "value": gran})
        by_gran[gran] = by_gran.get(gran, 0) + 1

        # Validate relevant
        if rel is None:
            errors.append({"type": "missing_relevant", "index": i})
        elif rel:
            relevant_count += 1
            if gran == "practitioner":
                practitioner_relevant += 1

        # Validate rationale
        if not rat or len(rat.strip()) < 10:
            warnings.append({"type": "short_rationale", "index": i, "length": len(rat.strip())})

    total = len(data)
    filled = total - len(unmapped)

    result = {
        "status": "PASS" if not errors else "FAIL",
        "total": total,
        "filled": filled,
        "unmapped": len(unmapped),
        "by_step": dict(sorted(by_step.items())),
        "by_granularity": dict(sorted(by_gran.items())),
        "relevant": relevant_count,
        "practitioner_relevant": practitioner_relevant,
        "errors": errors,
        "warnings": warnings,
    }

    if json_output:
        print(json.dumps(result, indent=2))
    else:
        console.print(f"Total: {total}, Filled: {filled}, Unmapped: {len(unmapped)}")
        console.print(f"\nBy step:")
        for step in sorted(VALID_STEPS):
            console.print(f"  {step}: {by_step.get(step, 0)}")
        console.print(f"\nBy granularity:")
        for g in sorted(VALID_GRANULARITY):
            console.print(f"  {g}: {by_gran.get(g, 0)}")
        console.print(f"\nRelevant: {relevant_count} ({relevant_count/max(filled,1)*100:.0f}%)")
        console.print(f"Practitioner + relevant: {practitioner_relevant}")

        if errors:
            console.print(f"\n[red]{len(errors)} error(s)[/red]")
            for e in errors[:10]:
                console.print(f"  {e}")
        if warnings:
            console.print(f"\n[yellow]{len(warnings)} warning(s)[/yellow]")
        if not errors:
            console.print("\n[green]PASS[/green]")
        else:
            console.print("\n[red]FAIL[/red]")

    raise typer.Exit(1 if errors else 0)


if __name__ == "__main__":
    app()
