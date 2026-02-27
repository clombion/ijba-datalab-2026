# /// script
# requires-python = ">=3.12"
# dependencies = ["rich", "typer>=0.9.0"]
# ///
"""T10 Validation — check relevance scoring completeness.

Usage:
    uv run utils/analyse/t10_3_validate_relevance.py              # validate all
    uv run utils/analyse/t10_3_validate_relevance.py --only 07
"""

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console
from rich.table import Table

__version__ = "1.0.0"

ROOT = Path(__file__).resolve().parent.parent.parent
RELEVANCE_DIR = ROOT / "research" / "pipeline-canon" / "relevance"

console = Console()

VALID_RELEVANCE = {"endures", "displaced", "needs_update"}
RELEVANCE_LABELS = ["endures", "needs_update", "displaced"]

app = typer.Typer(help=__doc__, add_completion=False, no_args_is_help=False)


def version_callback(value: bool) -> None:
    if value:
        console.print(f"t10_3_validate_relevance {__version__}")
        raise typer.Exit()


@app.command()
def main(
    only: Annotated[str | None, typer.Option("--only", help="Validate only sources matching this ID prefix.")] = None,
    version: Annotated[bool | None, typer.Option("--version", callback=version_callback, is_eager=True, help="Show version.")] = None,
) -> None:
    files = sorted(RELEVANCE_DIR.glob("*.json"))
    if only:
        files = [f for f in files if f.name.startswith(f"{only}-")]

    if not files:
        console.print("[yellow]No relevance files found.")
        return

    console.rule(f"[bold]VALIDATE RELEVANCE — {len(files)} files")
    total_errors = 0
    total_warnings = 0
    total_extracts = 0
    dist = Counter()

    for f in files:
        data = json.loads(f.read_text())
        extracts = data.get("extracts", [])
        total_extracts += len(extracts)

        unscored = [i for i, e in enumerate(extracts) if not e.get("llm_relevance")]
        if unscored:
            total_errors += 1
            console.print(f"  [red]ERROR[/] {f.name}: {len(unscored)} unscored extracts (indices: {unscored[:5]})")

        no_rationale = [
            i for i, e in enumerate(extracts)
            if e.get("llm_relevance") and not e.get("relevance_rationale")
        ]
        if no_rationale:
            total_errors += 1
            console.print(f"  [red]ERROR[/] {f.name}: {len(no_rationale)} missing rationales")

        for e in extracts:
            rel = e.get("llm_relevance")
            if rel:
                if rel not in VALID_RELEVANCE:
                    total_errors += 1
                    console.print(f"  [red]ERROR[/] {f.name}: invalid relevance '{rel}'")
                else:
                    dist[rel] += 1

        # Warning: >90% endures
        file_scored = [e for e in extracts if e.get("llm_relevance")]
        if len(file_scored) >= 5:
            endures_count = sum(1 for e in file_scored if e["llm_relevance"] == "endures")
            if endures_count / len(file_scored) > 0.9:
                total_warnings += 1
                console.print(f"  [yellow]WARN[/]  {f.name}: {endures_count}/{len(file_scored)} endures (>90%)")

    console.rule("[bold]Summary")
    console.print(f"  Files: {len(files)}")
    console.print(f"  Total extracts: {total_extracts}")
    dist_table = Table(show_header=True)
    dist_table.add_column("Relevance")
    dist_table.add_column("Count", justify="right")
    dist_table.add_column("%", justify="right")
    for label in RELEVANCE_LABELS:
        n = dist.get(label, 0)
        pct = 100 * n / total_extracts if total_extracts else 0
        dist_table.add_row(label, str(n), f"{pct:.1f}%")
    console.print(dist_table)
    console.print(f"  Errors: {total_errors}")
    console.print(f"  Warnings: {total_warnings}")

    if total_errors:
        console.print(f"  [red]FAIL[/]")
        raise typer.Exit(1)
    else:
        console.print("  [green]PASS[/]")


if __name__ == "__main__":
    app()
