# /// script
# requires-python = ">=3.12"
# dependencies = ["rich", "typer>=0.9.0"]
# ///
"""T10 Scaffold — create relevance JSONs from merged T9 extractions.

Reads merged extractions/{stem}.json (chunk=null), creates
relevance/{stem}.json with each extract's text + classification
but llm_relevance: null.

Usage:
    uv run utils/analyse/t10_1_scaffold_relevance.py              # scaffold all
    uv run utils/analyse/t10_1_scaffold_relevance.py --only 07
"""

import json
import sys
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console

__version__ = "1.0.0"

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "utils"))
from log_action import log_action  # noqa: E402

EXTRACTIONS_DIR = ROOT / "research" / "pipeline-canon" / "extractions"
RELEVANCE_DIR = ROOT / "research" / "pipeline-canon" / "relevance"

console = Console()

app = typer.Typer(help=__doc__, add_completion=False, no_args_is_help=False)


def version_callback(value: bool) -> None:
    if value:
        console.print(f"t10_1_scaffold_relevance {__version__}")
        raise typer.Exit()


@app.command()
def main(
    only: Annotated[str | None, typer.Option("--only", help="Process only sources matching this ID prefix.")] = None,
    dry_run: Annotated[bool, typer.Option("--dry-run", help="Show what would be created without writing files.")] = False,
    version: Annotated[bool | None, typer.Option("--version", callback=version_callback, is_eager=True, help="Show version.")] = None,
) -> None:
    RELEVANCE_DIR.mkdir(parents=True, exist_ok=True)

    # Find merged extraction files (chunk: null)
    files = sorted(EXTRACTIONS_DIR.glob("*.json"))
    # Filter to merged files only (no _chunk in name)
    merged = [f for f in files if "_chunk" not in f.name]

    if only:
        merged = [f for f in merged if f.name.startswith(f"{only}-")]

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

        if not dry_run:
            out_path.write_text(json.dumps(rel_data, indent=2, ensure_ascii=False) + "\n")
        created += 1

    prefix = "[DRY RUN] " if dry_run else ""
    console.print(f"  {prefix}Created: {created}")
    console.print(f"  {prefix}Skipped (exist): {skipped}")

    if created and not dry_run:
        log_action(Path(__file__).name, f"Created {created} relevance scaffolds, skipped {skipped} existing")


if __name__ == "__main__":
    app()
