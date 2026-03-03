# /// script
# requires-python = ">=3.12"
# dependencies = ["typer>=0.9.0", "rich>=13.0.0"]
# ///
"""Scaffold case study practice extraction file.

Reads sources/case-studies.md and creates practices/case_studies.json with
one entry per case study, with null fields for practices to be filled by LLM.

Input: sources/case-studies.md (## headings = case studies)
Output: practices/case_studies.json

Usage:
    uv run research/pipeline-canon-2/scripts/t2_1_scaffold_case_studies.py
    uv run research/pipeline-canon-2/scripts/t2_1_scaffold_case_studies.py --dry-run
    uv run research/pipeline-canon-2/scripts/t2_1_scaffold_case_studies.py --status

Exit codes:
    0  Success
    1  General error
    5  Output already exists (use --force)
    66 Input file not found
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console

__version__ = "1.0.0"

PIPELINE_ROOT = Path(__file__).resolve().parent.parent
SOURCES_FILE = PIPELINE_ROOT / "sources" / "case-studies.md"
OUTPUT_FILE = PIPELINE_ROOT / "practices" / "case_studies.json"

console = Console(stderr=True)
app = typer.Typer(help=__doc__, add_completion=False)


def _parse_case_studies(text: str) -> list[dict]:
    """Parse case-studies.md into structured entries."""
    entries = []
    # Split on ## headings (level 2)
    sections = re.split(r"^## ", text, flags=re.MULTILINE)
    for section in sections[1:]:  # skip preamble before first ##
        lines = section.strip().splitlines()
        if not lines:
            continue
        heading = lines[0].strip()
        # Extract number and title from heading like "1. OpenElections"
        match = re.match(r"(\d+)\.\s+(.*)", heading)
        if match:
            idx = int(match.group(1))
            title = match.group(2).strip()
        else:
            idx = len(entries) + 1
            title = heading
        body = "\n".join(lines[1:]).strip()
        entries.append({
            "source_index": idx - 1,  # 0-based
            "source_id": f"cs_{idx:02d}",
            "title": title,
            "raw_description": body,
            "practices": [],
        })
    return entries


def version_callback(value: bool) -> None:
    if value:
        print(f"t2-1-scaffold-case-studies {__version__}")
        raise typer.Exit()


@app.command()
def main(
    dry_run: Annotated[bool, typer.Option("--dry-run", help="Show what would be created without writing.")] = False,
    status: Annotated[bool, typer.Option("--status", help="Report fill progress.")] = False,
    force: Annotated[bool, typer.Option("--force", help="Overwrite existing output.")] = False,
    version: Annotated[bool | None, typer.Option("--version", callback=version_callback, is_eager=True, help="Show version.")] = None,
) -> None:
    """Scaffold case study practice extraction file."""
    if status:
        if not OUTPUT_FILE.exists():
            print(json.dumps({"scaffolded": False, "message": "Output file does not exist"}))
            raise typer.Exit(0)
        with open(OUTPUT_FILE, encoding="utf-8") as f:
            data = json.load(f)
        total = len(data)
        filled = sum(1 for entry in data if entry.get("practices"))
        print(json.dumps({"total": total, "filled": filled, "remaining": total - filled}))
        raise typer.Exit(0)

    if not SOURCES_FILE.exists():
        console.print(f"[red]Input not found: {SOURCES_FILE}[/red]")
        raise typer.Exit(66)

    if OUTPUT_FILE.exists() and not force:
        console.print(f"[yellow]Output already exists: {OUTPUT_FILE}[/yellow]")
        console.print("Use --force to overwrite, or --status to check progress.")
        raise typer.Exit(5)

    text = SOURCES_FILE.read_text(encoding="utf-8")
    entries = _parse_case_studies(text)

    console.print(f"Parsed {len(entries)} case studies from {SOURCES_FILE.name}")
    for e in entries:
        console.print(f"  [{e['source_id']}] {e['title']}")

    if dry_run:
        console.print("[yellow]Dry run — no file written.[/yellow]")
        print(json.dumps({"count": len(entries), "titles": [e["title"] for e in entries]}))
        raise typer.Exit(0)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(entries, f, indent=2, ensure_ascii=False)

    console.print(f"[green]Written: {OUTPUT_FILE}[/green]")

    from log_action import log_action
    from manifest import append_manifest

    append_manifest("t2_1_scaffold_case_studies", "practices/case_studies.json", ["sources/case-studies.md"])
    log_action("t2_1_scaffold_case_studies.py", f"Scaffolded {len(entries)} case study entries")

    print(json.dumps({"count": len(entries)}))


if __name__ == "__main__":
    app()
