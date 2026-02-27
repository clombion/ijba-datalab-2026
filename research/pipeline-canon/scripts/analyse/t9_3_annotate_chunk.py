# /// script
# requires-python = ">=3.12"
# dependencies = ["typer>=0.9.0"]
# ///
"""CLI for LLM Pass 0 — write section labels into chunk metadata header.

Usage:
    uv run research/pipeline-canon/scripts/analyse/t9_3_annotate_chunk.py \
      --file chunks/82-periodismo-datos_chunk2.md \
      --sections "Research methodology; Survey design and sampling"
"""

import sys
from pathlib import Path
from typing import Annotated

import typer

__version__ = "1.0.0"

PIPELINE_ROOT = Path(__file__).resolve().parent.parent.parent
CHUNKS_DIR = PIPELINE_ROOT / "chunks"

app = typer.Typer(help=__doc__, add_completion=False, no_args_is_help=True)


def version_callback(value: bool) -> None:
    if value:
        typer.echo(f"t9_3_annotate_chunk {__version__}")
        raise typer.Exit()


@app.command()
def main(
    file: Annotated[str, typer.Option("--file", help="Chunk file path (relative or absolute).")],
    sections: Annotated[str, typer.Option("--sections", help="Semicolon-separated section labels.")],
    version: Annotated[bool | None, typer.Option("--version", callback=version_callback, is_eager=True, help="Show version.")] = None,
) -> None:
    """Write section labels into chunk metadata header."""
    # Resolve path (could be relative or absolute)
    p = Path(file)
    if not p.is_absolute():
        p = CHUNKS_DIR / p.name if not p.exists() else p
    if not p.exists():
        p = CHUNKS_DIR / Path(file).name
    if not p.exists():
        typer.echo(f"Error: file not found: {file}", err=True)
        raise typer.Exit(1)

    text = p.read_text()
    sections_line = f"<!-- sections: {sections} -->\n"

    # Insert after existing metadata comments
    lines = text.splitlines(keepends=True)
    insert_idx = 0
    for idx, line in enumerate(lines):
        if line.startswith("<!--") and "-->" in line:
            # Remove existing sections line if present
            if line.startswith("<!-- sections:"):
                lines[idx] = sections_line
                insert_idx = -1  # flag: already replaced
                break
            insert_idx = idx + 1
        else:
            break

    if insert_idx >= 0:
        lines.insert(insert_idx, sections_line)

    p.write_text("".join(lines))
    typer.echo(f"Annotated {p.name}: {sections}")


if __name__ == "__main__":
    app()
