# /// script
# requires-python = ">=3.12"
# dependencies = ["typer>=0.9.0", "rich>=13.0.0"]
# ///
"""Build self-contained taxonomy review HTML.

Reads taxonomy.csv, converts to JSON, gzips, base64-encodes,
and injects into template.html along with inlined CSS, JS, and fflate.

Usage:
    uv run research/pipeline-canon-2/scripts/review/taxonomy/build.py
    uv run research/pipeline-canon-2/scripts/review/taxonomy/build.py --csv taxonomy.csv --output index.html
    uv run research/pipeline-canon-2/scripts/review/taxonomy/build.py --dry-run
"""

from __future__ import annotations

import base64
import csv
import gzip
import json
from pathlib import Path

import typer

app = typer.Typer(add_completion=False)

PIPELINE_ROOT = Path(__file__).resolve().parent.parent.parent.parent
HERE = Path(__file__).resolve().parent

FFLATE_PATH = Path("/tmp/fflate-0.8.2.umd.js")
FFLATE_CDN = "https://cdn.jsdelivr.net/npm/fflate@0.8.2/umd/index.js"


def _ensure_fflate() -> str:
    if FFLATE_PATH.exists():
        return FFLATE_PATH.read_text()
    import urllib.request
    typer.echo("Downloading fflate 0.8.2 from CDN...")
    urllib.request.urlretrieve(FFLATE_CDN, FFLATE_PATH)
    return FFLATE_PATH.read_text()


def _csv_to_json(csv_path: Path) -> str:
    with open(csv_path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return json.dumps(rows, ensure_ascii=False, separators=(",", ":"))


@app.command()
def build(
    csv_path: Path = typer.Option(
        PIPELINE_ROOT / "taxonomy.csv",
        "--csv",
        help="Path to taxonomy.csv",
    ),
    output: Path = typer.Option(
        HERE / "index.html",
        "--output",
        help="Output HTML path",
    ),
    dry_run: bool = typer.Option(False, "--dry-run", help="Show sizes without writing"),
) -> None:
    """Build the self-contained taxonomy review tool HTML."""
    if not csv_path.exists():
        typer.echo(f"Error: CSV not found: {csv_path}", err=True)
        raise typer.Exit(1)

    json_str = _csv_to_json(csv_path)
    json_bytes = json_str.encode("utf-8")
    compressed = gzip.compress(json_bytes, compresslevel=9)
    b64 = base64.b64encode(compressed).decode("ascii")

    typer.echo(f"CSV rows: {json_str.count('{')}")
    typer.echo(f"JSON: {len(json_bytes):,} bytes")
    typer.echo(f"Gzipped: {len(compressed):,} bytes")
    typer.echo(f"Base64: {len(b64):,} bytes")

    template = (HERE / "template.html").read_text()
    style = (HERE / "style.css").read_text()
    app_js = (HERE / "app.js").read_text()
    fflate_js = _ensure_fflate()

    html = template
    html = html.replace("/* {{STYLE}} */", style)
    html = html.replace("/* {{FFLATE}} */", fflate_js)
    html = html.replace("/* {{SCRIPT}} */", app_js)
    html = html.replace("{{DATA}}", b64)

    typer.echo(f"Output: {len(html):,} bytes")

    if dry_run:
        typer.echo("Dry run — no file written.")
        raise typer.Exit(0)

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(html)
    typer.echo(f"Written: {output}")


if __name__ == "__main__":
    app()
