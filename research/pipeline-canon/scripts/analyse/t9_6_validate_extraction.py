# /// script
# requires-python = ">=3.12"
# dependencies = ["typer>=0.9.0", "rich>=13.0.0"]
# ///
"""T9 Validation — check extraction completeness and quality.

Usage:
    uv run research/pipeline-canon/scripts/analyse/t9_6_validate_extraction.py              # validate all
    uv run research/pipeline-canon/scripts/analyse/t9_6_validate_extraction.py --only 07    # one source
"""

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console

__version__ = "1.0.0"

PIPELINE_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PIPELINE_ROOT / "scripts"))
from log_action import log_action  # noqa: E402

EXTRACTIONS_DIR = PIPELINE_ROOT / "extractions"

console = Console()

VALID_STEPS = {"Define", "Find", "Get", "Verify", "Clean", "Analyse", "Present"}
VALID_TYPES = {"procedural", "epistemological", "organizational", "tool-specific"}
MIN_WORDS_FOR_EXTRACTS = 2000
MIN_EXTRACT_LEN = 20
MAX_EXTRACT_LEN = 2000
MAX_THEMES = 5

app = typer.Typer(help=__doc__, add_completion=False, no_args_is_help=False)


def version_callback(value: bool) -> None:
    if value:
        Console().print(f"t9_6_validate_extraction {__version__}")
        raise typer.Exit()


def validate_file(path: Path) -> tuple[list[str], list[str]]:
    """Validate one extraction JSON. Returns (errors, warnings)."""
    errors = []
    warnings = []

    data = json.loads(path.read_text())
    extracts = data.get("extracts", [])
    chunk_words = data.get("chunk_words", 0)

    # Error: no extracts on substantial chunk
    if not extracts and chunk_words > MIN_WORDS_FOR_EXTRACTS:
        errors.append(f"0 extracts on {chunk_words:,}w chunk")

    step_counts = Counter()
    for i, ext in enumerate(extracts):
        prefix = f"extract #{i+1}"

        # Required fields
        if not ext.get("extract"):
            errors.append(f"{prefix}: missing extract text")
        if not ext.get("chapter"):
            errors.append(f"{prefix}: missing chapter")
        if not ext.get("pipeline_step"):
            errors.append(f"{prefix}: missing pipeline_step")
        elif ext["pipeline_step"] not in VALID_STEPS:
            errors.append(f"{prefix}: invalid step '{ext['pipeline_step']}'")
        if not ext.get("extract_type"):
            errors.append(f"{prefix}: missing extract_type")
        elif ext["extract_type"] not in VALID_TYPES:
            errors.append(f"{prefix}: invalid type '{ext['extract_type']}'")

        # Warnings
        text_len = len(ext.get("extract", ""))
        if text_len < MIN_EXTRACT_LEN:
            warnings.append(f"{prefix}: extract too short ({text_len} chars)")
        if text_len > MAX_EXTRACT_LEN:
            warnings.append(f"{prefix}: extract too long ({text_len} chars)")

        themes = ext.get("themes", [])
        if len(themes) > MAX_THEMES:
            warnings.append(f"{prefix}: {len(themes)} themes (max {MAX_THEMES})")

        if ext.get("pipeline_step"):
            step_counts[ext["pipeline_step"]] += 1

    # Warning: >80% same step
    if extracts and step_counts:
        max_step, max_count = step_counts.most_common(1)[0]
        if max_count / len(extracts) > 0.8 and len(extracts) >= 5:
            warnings.append(f"{max_count}/{len(extracts)} extracts are {max_step} (>80%)")

    return errors, warnings


@app.command()
def main(
    only: Annotated[str | None, typer.Option("--only", help="Validate only this source ID.")] = None,
    version: Annotated[bool | None, typer.Option("--version", callback=version_callback, is_eager=True, help="Show version.")] = None,
) -> None:
    """Check extraction completeness and quality."""
    files = sorted(EXTRACTIONS_DIR.glob("*_chunk*.json"))
    if only:
        files = [f for f in files if f.name.startswith(f"{only}-")]

    if not files:
        console.print("[yellow]No extraction files found.")
        return

    total_errors = 0
    total_warnings = 0
    total_extracts = 0
    files_with_errors = []

    console.rule(f"[bold]VALIDATE EXTRACTIONS — {len(files)} files")

    for f in files:
        data = json.loads(f.read_text())
        n_extracts = len(data.get("extracts", []))
        total_extracts += n_extracts

        errors, warnings = validate_file(f)

        if errors:
            total_errors += len(errors)
            files_with_errors.append(f.name)
            for e in errors:
                console.print(f"  [red]ERROR[/] {f.name}: {e}")
        for w in warnings:
            total_warnings += 1
            console.print(f"  [yellow]WARN[/]  {f.name}: {w}")

    console.rule("[bold]Summary")
    console.print(f"  Files: {len(files)}")
    console.print(f"  Total extracts: {total_extracts}")
    console.print(f"  Errors: {total_errors}")
    console.print(f"  Warnings: {total_warnings}")

    log_action(Path(__file__).name, f"Validated {len(files)} files, {total_extracts} extracts, {total_errors} errors, {total_warnings} warnings")

    if total_errors:
        console.print(f"  [red]FAIL[/] — {len(files_with_errors)} files with errors")
        raise typer.Exit(1)
    else:
        console.print("  [green]PASS[/]")


if __name__ == "__main__":
    app()
