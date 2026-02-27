# /// script
# requires-python = ">=3.12"
# dependencies = ["typer>=0.9.0"]
# ///
"""CLI for LLM to score an extract for LLM-era relevance (T10).

Usage:
    uv run research/pipeline-canon/scripts/analyse/t10_2_score_extract.py \
      --file relevance/07-ddj-handbook-1.json \
      --index 3 \
      --relevance endures \
      --rationale "Verification against original sources is fundamental journalism"
"""

import json
import sys
from pathlib import Path
from typing import Annotated

import typer

__version__ = "1.0.0"

PIPELINE_ROOT = Path(__file__).resolve().parent.parent.parent
RELEVANCE_DIR = PIPELINE_ROOT / "relevance"

VALID_RELEVANCE = {"endures", "displaced", "needs_update"}

app = typer.Typer(help=__doc__, add_completion=False, no_args_is_help=True)


def version_callback(value: bool) -> None:
    if value:
        print(f"t10_2_score_extract {__version__}")
        raise typer.Exit()


@app.command()
def main(
    file: Annotated[str, typer.Option("--file", help="Relevance JSON file path.")],
    index: Annotated[int, typer.Option("--index", help="Extract index to score.")],
    relevance: Annotated[str, typer.Option("--relevance", help="Relevance label: endures, displaced, needs_update.")],
    rationale: Annotated[str, typer.Option("--rationale", help="Rationale for the relevance score.")],
    version: Annotated[bool | None, typer.Option("--version", callback=version_callback, is_eager=True, help="Show version.")] = None,
) -> None:
    # Validate relevance
    if relevance not in VALID_RELEVANCE:
        print(f"Error: --relevance must be one of: {', '.join(sorted(VALID_RELEVANCE))}", file=sys.stderr)
        print(f"  Got: {relevance}", file=sys.stderr)
        raise typer.Exit(code=1)

    # Resolve path
    p = Path(file)
    if not p.is_absolute():
        p = RELEVANCE_DIR / p.name if not p.exists() else p
    if not p.exists():
        p = RELEVANCE_DIR / Path(file).name
    if not p.exists():
        print(f"Error: file not found: {file}", file=sys.stderr)
        raise typer.Exit(code=1)

    data = json.loads(p.read_text())
    extracts = data.get("extracts", [])

    if index < 0 or index >= len(extracts):
        print(f"Error: index {index} out of range (0-{len(extracts) - 1})", file=sys.stderr)
        raise typer.Exit(code=1)

    extracts[index]["llm_relevance"] = relevance
    extracts[index]["relevance_rationale"] = rationale

    p.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Scored extract #{index} in {p.name}: {relevance}")


if __name__ == "__main__":
    app()
