# /// script
# requires-python = ">=3.12"
# dependencies = ["typer>=0.9.0"]
# ///
"""CLI for LLM to add an extract to an extraction JSON file.

The LLM passes plain text arguments; this script handles all JSON assembly
and enum validation.

Usage:
    uv run utils/analyse/t9_5_add_extract.py \
      --file extractions/07-ddj-handbook-1_chunk2.json \
      --extract "Always verify your data against the original source" \
      --chapter "Getting Data from the Web" \
      --step Verify \
      --secondary-step null \
      --type epistemological \
      --themes "verification, data quality" \
      --notes ""
"""

import json
import sys
from pathlib import Path
from typing import Annotated

import typer

__version__ = "1.0.0"

ROOT = Path(__file__).resolve().parent.parent.parent
EXTRACTIONS_DIR = ROOT / "research" / "pipeline-canon" / "extractions"

VALID_STEPS = {"Define", "Find", "Get", "Verify", "Clean", "Analyse", "Present"}
VALID_TYPES = {"procedural", "epistemological", "organizational", "tool-specific"}

app = typer.Typer(help=__doc__, add_completion=False, no_args_is_help=True)


def version_callback(value: bool) -> None:
    if value:
        typer.echo(f"t9_5_add_extract {__version__}")
        raise typer.Exit()


@app.command()
def main(
    file: Annotated[str, typer.Option("--file", help="Extraction JSON file path.")],
    extract: Annotated[str, typer.Option("--extract", help="Extract text.")],
    chapter: Annotated[str, typer.Option("--chapter", help="Chapter or section title.")],
    step: Annotated[str, typer.Option("--step", help="Pipeline step (Define/Find/Get/Verify/Clean/Analyse/Present).")],
    extract_type: Annotated[str, typer.Option("--type", help="Extract type (procedural/epistemological/organizational/tool-specific).")],
    secondary_step: Annotated[str | None, typer.Option("--secondary-step", help="Secondary pipeline step, or null.")] = None,
    themes: Annotated[str | None, typer.Option("--themes", help="Comma-separated themes.")] = None,
    notes: Annotated[str | None, typer.Option("--notes", help="Additional notes.")] = None,
    version: Annotated[bool | None, typer.Option("--version", callback=version_callback, is_eager=True, help="Show version.")] = None,
) -> None:
    """Add an extract to an extraction JSON file."""
    # Validate enums
    if step not in VALID_STEPS:
        typer.echo(f"Error: --step must be one of: {', '.join(sorted(VALID_STEPS))}", err=True)
        typer.echo(f"  Got: {step}", err=True)
        raise typer.Exit(1)

    if extract_type not in VALID_TYPES:
        typer.echo(f"Error: --type must be one of: {', '.join(sorted(VALID_TYPES))}", err=True)
        typer.echo(f"  Got: {extract_type}", err=True)
        raise typer.Exit(1)

    if secondary_step and secondary_step != "null" and secondary_step not in VALID_STEPS:
        typer.echo(f"Error: --secondary-step must be null or one of: {', '.join(sorted(VALID_STEPS))}", err=True)
        raise typer.Exit(1)

    # Resolve file path
    p = Path(file)
    if not p.is_absolute():
        p = EXTRACTIONS_DIR / p.name if not p.exists() else p
    if not p.exists():
        p = EXTRACTIONS_DIR / Path(file).name
    if not p.exists():
        typer.echo(f"Error: file not found: {file}", err=True)
        raise typer.Exit(1)

    # Parse themes
    theme_list = [t.strip() for t in (themes or "").split(",") if t.strip()]

    # Normalize secondary_step
    sec_step = None if (not secondary_step or secondary_step == "null") else secondary_step

    # Read, append, write
    data = json.loads(p.read_text())
    extract_obj = {
        "extract": extract,
        "chapter": chapter,
        "pipeline_step": step,
        "secondary_step": sec_step,
        "extract_type": extract_type,
        "themes": theme_list,
        "notes": notes or "",
    }
    data["extracts"].append(extract_obj)
    p.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")

    n = len(data["extracts"])
    typer.echo(f"Added extract #{n} to {p.name} (step={step}, type={extract_type})")


if __name__ == "__main__":
    app()
