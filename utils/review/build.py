# /// script
# requires-python = ">=3.12"
# dependencies = ["typer>=0.9.0", "rich>=13.0.0"]
# ///
"""Build self-contained horizon-table review HTML.

Reads horizon-table.csv, converts to JSON, gzips, base64-encodes,
and injects into template.html along with inlined CSS, JS, and fflate.

Usage:
    uv run utils/review/build.py [--csv PATH] [--output PATH] [--dry-run]
"""

from __future__ import annotations

import base64
import csv
import gzip
import json
from pathlib import Path

import typer

app = typer.Typer(add_completion=False)

ROOT = Path(__file__).resolve().parent.parent.parent
HERE = Path(__file__).resolve().parent

# fflate 0.8.2 UMD — vendored at build time
FFLATE_PATH = Path("/tmp/fflate-0.8.2.umd.js")
FFLATE_CDN = "https://cdn.jsdelivr.net/npm/fflate@0.8.2/umd/index.js"


def _ensure_fflate() -> str:
    """Return fflate UMD source, downloading if needed."""
    if FFLATE_PATH.exists():
        return FFLATE_PATH.read_text()
    import urllib.request

    typer.echo(f"Downloading fflate 0.8.2 from CDN...")
    urllib.request.urlretrieve(FFLATE_CDN, FFLATE_PATH)
    return FFLATE_PATH.read_text()


def _csv_to_json(csv_path: Path) -> str:
    """Read CSV and return JSON array string."""
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    return json.dumps(rows, ensure_ascii=False, separators=(",", ":"))


@app.command()
def build(
    csv_path: Path = typer.Option(
        ROOT / "research" / "pipeline-canon" / "horizon-table.csv",
        "--csv",
        help="Path to horizon-table.csv",
    ),
    output: Path = typer.Option(
        HERE / "index.html",
        "--output",
        help="Output HTML path",
    ),
    dry_run: bool = typer.Option(False, "--dry-run", help="Show sizes without writing"),
):
    """Build the self-contained review tool HTML."""
    if not csv_path.exists():
        typer.echo(f"Error: CSV not found: {csv_path}", err=True)
        raise typer.Exit(1)

    # 1. CSV → JSON → gzip → base64
    json_str = _csv_to_json(csv_path)
    json_bytes = json_str.encode("utf-8")
    compressed = gzip.compress(json_bytes, compresslevel=9)
    b64 = base64.b64encode(compressed).decode("ascii")

    typer.echo(f"CSV rows: {json_str.count('{')}")
    typer.echo(f"JSON: {len(json_bytes):,} bytes")
    typer.echo(f"Gzipped: {len(compressed):,} bytes")
    typer.echo(f"Base64: {len(b64):,} bytes")

    # 2. Read template, CSS, JS
    template = (HERE / "template.html").read_text()
    style = (HERE / "style.css").read_text()
    app_js = (HERE / "app.js").read_text()
    fflate_js = _ensure_fflate()

    # 3. Assemble
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
