#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pymupdf==1.27.1",
#     "pymupdf4llm==0.3.4",
#     "typer>=0.9.0",
#     "rich>=13.0.0",
# ]
# ///
"""Convert a PDF to Markdown via pymupdf4llm with quality verification.

Optionally uses pymupdf-layout for AI-powered page structure detection
(headings, tables, headers/footers). Install it separately to enable:

    uv pip install pymupdf-layout==1.27.1

When installed, layout mode is used by default. Use --no-layout to
force legacy mode with manual --margins.

Prerequisites:
    - uv (https://docs.astral.sh/uv/)
    - No other install needed — deps are inline (PEP 723)

Examples:
    # Convert (uses layout mode if pymupdf-layout is installed):
    ./research/pipeline-canon/scripts/get/t5_pdf2md.py document.pdf

    # Force legacy mode with manual margins:
    ./research/pipeline-canon/scripts/get/t5_pdf2md.py document.pdf --no-layout --margins 40

    # Analyze PDF to find optimal legacy-mode settings:
    ./research/pipeline-canon/scripts/get/t5_pdf2md.py document.pdf --analyze

    # Custom output path:
    ./research/pipeline-canon/scripts/get/t5_pdf2md.py document.pdf -o out.md

Exit codes:
    0  Success
    1  Verification warnings (output written but may have issues)
    66 Input file not found
"""

from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Annotated

import pymupdf
import pymupdf4llm
import re
import sys

import typer
from rich.console import Console
from rich.table import Table

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

__version__ = "0.3.0"

DEFAULT_MARGINS = 50
WORD_COUNT_THRESHOLD_PCT = 10.0
TOC_SCAN_PAGES = 10
HEADING_PATTERN = re.compile(
    r"((?:Module|Section|Chapter|Part) \d+[\s:–—-].+?)(?:\s+\d+\s*$)",
    re.MULTILINE,
)
PROMO_LINE = re.compile(r"^Consider using the pymupdf_layout package.*\n")
MARGIN_CANDIDATES = [0, 20, 30, 40, 50, 60, 72]

console = Console()
err_console = Console(stderr=True)

# ---------------------------------------------------------------------------
# Layout mode detection — deferred to avoid side-effects at import time
# ---------------------------------------------------------------------------


def _check_layout_available() -> bool:
    try:
        import pymupdf.layout  # noqa: F401
        return True
    except ImportError:
        return False


# ---------------------------------------------------------------------------
# Types
# ---------------------------------------------------------------------------


@dataclass(frozen=True, slots=True)
class VerifyStats:
    pdf_words: int
    md_words: int
    delta_pct: float
    toc_headings: int
    missing_headings: int


@dataclass(frozen=True, slots=True)
class AnalysisResult:
    total_pages: int
    repeated_headers: list[str]
    repeated_footers: list[str]
    suggested_margins: int
    has_toc: bool
    toc_heading_count: int
    margin_trials: list[dict[str, float | int]]


# ---------------------------------------------------------------------------
# Pure business logic
# ---------------------------------------------------------------------------


def extract_zone_text(
    page: pymupdf.Page, zone: str, margin_pt: int = 50
) -> str:
    """Extract text from the top or bottom margin zone of a page."""
    rect = page.rect
    if zone == "top":
        clip = pymupdf.Rect(rect.x0, rect.y0, rect.x1, rect.y0 + margin_pt)
    else:
        clip = pymupdf.Rect(rect.x0, rect.y1 - margin_pt, rect.x1, rect.y1)
    return page.get_text(clip=clip).strip()


def find_repeated_text(texts: list[str], min_freq: int = 3) -> list[str]:
    """Return text strings that appear on at least min_freq pages."""
    counts = Counter(t for t in texts if t)
    return [text for text, count in counts.most_common() if count >= min_freq]


def find_toc_headings(doc: pymupdf.Document) -> list[str]:
    """Scan early pages for TOC-style heading lines."""
    toc_text = ""
    for i in range(min(TOC_SCAN_PAGES, len(doc))):
        toc_text += doc[i].get_text()
    return HEADING_PATTERN.findall(toc_text)


def count_words_pdf(doc: pymupdf.Document) -> int:
    words = []
    for page in doc:
        words.extend(page.get_text().split())
    return len(words)


def check_word_parity(pdf_wc: int, md_wc: int) -> str | None:
    if pdf_wc == 0:
        return "PDF has no extractable text"
    delta = abs(pdf_wc - md_wc) / pdf_wc * 100
    if delta > WORD_COUNT_THRESHOLD_PCT:
        return (
            f"Word count delta {delta:.1f}% exceeds {WORD_COUNT_THRESHOLD_PCT}% "
            f"(PDF={pdf_wc:,}, MD={md_wc:,})"
        )
    return None


def check_headings(toc_headings: list[str], md_text: str) -> str | None:
    missing = [h for h in toc_headings if h not in md_text]
    if missing:
        lines = "\n".join(f"  - {h}" for h in missing)
        return f"{len(missing)} TOC heading(s) missing from output:\n{lines}"
    return None


def suggest_margins(doc: pymupdf.Document) -> int:
    """Heuristic: pick the smallest margin that removes repeated headers/footers."""
    page_count = len(doc)
    for margin in [20, 30, 40, 50, 60, 72]:
        headers = [extract_zone_text(doc[i], "top", margin) for i in range(page_count)]
        footers = [extract_zone_text(doc[i], "bottom", margin) for i in range(page_count)]
        rep_h = find_repeated_text(headers)
        rep_f = find_repeated_text(footers)
        if rep_h or rep_f:
            return margin
    return 0


# ---------------------------------------------------------------------------
# I/O
# ---------------------------------------------------------------------------


def convert(pdf_path: str, *, use_layout: bool = False, margins: int = 0) -> str:
    """Convert PDF to Markdown.

    In layout mode, runs in a subprocess with pymupdf-layout injected via
    `uv run --with` for clean dependency isolation.
    In legacy mode, margins are applied to trim page edges.
    """
    if use_layout:
        return _convert_layout_subprocess(pdf_path)

    raw = pymupdf4llm.to_markdown(pdf_path, margins=margins)
    return PROMO_LINE.sub("", raw)


def _convert_layout_subprocess(pdf_path: str) -> str:
    """Run layout-mode conversion in an isolated subprocess."""
    import subprocess
    import textwrap

    script = textwrap.dedent(f"""\
        import pymupdf.layout
        import pymupdf4llm
        print(pymupdf4llm.to_markdown({pdf_path!r}), end='')
    """)
    result = subprocess.run(
        ["uv", "run", "--with", "pymupdf-layout==1.27.1",
         "--with", "pymupdf4llm==0.3.4",
         "python3", "-c", script],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"Layout subprocess failed:\n{result.stderr}")
    return PROMO_LINE.sub("", result.stdout)


def verify(pdf_path: str, md_text: str) -> tuple[list[str], VerifyStats]:
    with pymupdf.open(pdf_path) as doc:
        pdf_wc = count_words_pdf(doc)
        md_wc = len(md_text.split())
        delta_pct = abs(pdf_wc - md_wc) / pdf_wc * 100 if pdf_wc else 0

        toc_headings = find_toc_headings(doc)
        missing = [h for h in toc_headings if h not in md_text]

    warnings = []
    w = check_word_parity(pdf_wc, md_wc)
    if w:
        warnings.append(w)
    w = check_headings(toc_headings, md_text)
    if w:
        warnings.append(w)

    return warnings, VerifyStats(
        pdf_words=pdf_wc,
        md_words=md_wc,
        delta_pct=round(delta_pct, 1),
        toc_headings=len(toc_headings),
        missing_headings=len(missing),
    )


def analyze_pdf(pdf_path: str) -> AnalysisResult:
    with pymupdf.open(pdf_path) as doc:
        page_count = len(doc)

        headers = [extract_zone_text(doc[i], "top", 50) for i in range(page_count)]
        footers = [extract_zone_text(doc[i], "bottom", 50) for i in range(page_count)]
        rep_headers = find_repeated_text(headers)
        rep_footers = find_repeated_text(footers)

        toc_headings = find_toc_headings(doc)
        suggested = suggest_margins(doc)

        trials = []
        pdf_wc = count_words_pdf(doc)
        for m in MARGIN_CANDIDATES:
            md = convert(pdf_path, use_layout=False, margins=m)
            md_wc = len(md.split())
            missing = [h for h in toc_headings if h not in md]
            trials.append({
                "margins": m,
                "md_words": md_wc,
                "delta_pct": round(abs(pdf_wc - md_wc) / pdf_wc * 100, 1) if pdf_wc else 0,
                "missing_headings": len(missing),
            })

    return AnalysisResult(
        total_pages=page_count,
        repeated_headers=rep_headers,
        repeated_footers=rep_footers,
        suggested_margins=suggested,
        has_toc=len(toc_headings) > 0,
        toc_heading_count=len(toc_headings),
        margin_trials=trials,
    )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

app = typer.Typer(
    help=__doc__,
    add_completion=False,
    no_args_is_help=True,
    rich_markup_mode="rich",
)


def version_callback(value: bool) -> None:
    if value:
        console.print(f"pdf2md {__version__}")
        raise typer.Exit()


@app.command()
def main(
    pdf: Annotated[
        Path,
        typer.Argument(help="Path to the input PDF file."),
    ],
    output: Annotated[
        Path | None,
        typer.Option("-o", "--output", help="Output .md path. Default: same name as input."),
    ] = None,
    margins: Annotated[
        int,
        typer.Option(help="Margin in points to trim headers/footers (legacy mode only)."),
    ] = DEFAULT_MARGINS,
    layout: Annotated[
        bool,
        typer.Option("--layout", help="Enable layout mode (requires pymupdf-layout)."),
    ] = False,
    no_layout: Annotated[
        bool,
        typer.Option("--no-layout", help="Force legacy mode even if pymupdf-layout is installed."),
    ] = False,
    analyze: Annotated[
        bool,
        typer.Option("-a", "--analyze", help="Analyze PDF and suggest optimal legacy-mode settings, then exit."),
    ] = False,
    strict: Annotated[
        bool,
        typer.Option("--strict", help="Exit 1 on verification warnings. Default: warn only."),
    ] = False,
    verbose: Annotated[
        bool,
        typer.Option("-v", "--verbose", help="Show detailed output."),
    ] = False,
    version: Annotated[
        bool | None,
        typer.Option("--version", callback=version_callback, is_eager=True, help="Show version."),
    ] = None,
) -> None:
    if not pdf.exists():
        err_console.print(f"[red]Error:[/] {pdf} not found")
        raise typer.Exit(66)

    # Resolve layout mode — layout runs in a subprocess, so we don't need
    # it installed in this script's env. --layout is an explicit opt-in.
    use_layout = layout and not no_layout

    # --- Analyze mode (always uses legacy for margin trials) ---
    if analyze:
        console.print(f"[bold]Analyzing[/] {pdf} ...")
        result = analyze_pdf(str(pdf))

        console.print(f"\n[bold]Pages:[/] {result.total_pages}")
        console.print(f"[bold]TOC detected:[/] {'yes' if result.has_toc else 'no'}"
                       f" ({result.toc_heading_count} headings)")
        layout_installed = _check_layout_available()
        console.print(f"[bold]Layout mode:[/] {'available' if layout_installed else 'not installed (use --layout to run via subprocess)'}")

        if result.repeated_headers:
            console.print(f"\n[bold]Repeated headers[/] (found in 3+ pages):")
            for h in result.repeated_headers:
                console.print(f"  [dim]{h!r}[/]")
        if result.repeated_footers:
            console.print(f"\n[bold]Repeated footers[/] (found in 3+ pages):")
            for f in result.repeated_footers:
                console.print(f"  [dim]{f!r}[/]")

        table = Table(title="\nLegacy-mode margin trials")
        table.add_column("Margins (pt)", justify="right")
        table.add_column("Words", justify="right")
        table.add_column("Delta %", justify="right")
        table.add_column("Missing headings", justify="right")

        for t in result.margin_trials:
            is_suggested = t["margins"] == result.suggested_margins
            style = "bold green" if is_suggested else None
            suffix = " *" if is_suggested else ""
            table.add_row(
                str(t["margins"]) + suffix,
                f"{t['md_words']:,}",
                f"{t['delta_pct']}%",
                str(t["missing_headings"]),
                style=style,
            )

        console.print(table)

        if layout_installed:
            console.print(
                "\n[bold green]Recommended:[/] Use --layout for AI-powered detection. "
                "It auto-detects headers/footers."
            )
        elif result.suggested_margins:
            console.print(
                f"\n[bold green]Suggested:[/] --margins {result.suggested_margins}"
            )
        else:
            console.print(
                "\n[bold]Suggestion:[/] No repeated headers/footers detected. "
                "Try --margins 0 for full extraction."
            )
        raise typer.Exit(0)

    # --- Convert mode ---
    out_path = output or pdf.with_suffix(".md")
    mode_label = "layout" if use_layout else f"legacy (margins={margins}pt)"

    console.print(f"Converting {pdf} → {out_path}  [dim]({mode_label})[/]")
    try:
        md_text = convert(str(pdf), use_layout=use_layout, margins=margins)
    except Exception as exc:
        if use_layout:
            err_console.print(
                f"[yellow]Layout mode failed ({exc}); falling back to legacy.[/]"
            )
            md_text = convert(str(pdf), use_layout=False, margins=margins)
            mode_label = f"legacy fallback (margins={margins}pt)"
        else:
            raise

    out_path.write_text(md_text)
    console.print(
        f"Wrote {len(md_text):,} chars ({len(md_text.splitlines()):,} lines)"
    )

    console.print("\n[bold]Verifying...[/]")
    warnings, stats = verify(str(pdf), md_text)

    console.print(
        f"  Words: PDF={stats.pdf_words:,}  MD={stats.md_words:,}  "
        f"(delta {stats.delta_pct}%)"
    )
    console.print(
        f"  TOC headings: {stats.toc_headings} found, "
        f"{stats.missing_headings} missing"
    )

    if warnings:
        for w in warnings:
            err_console.print(f"  [yellow]{w}[/]")
        if strict:
            err_console.print(f"\n[red]{len(warnings)} warning(s)[/]")
            raise typer.Exit(1)
        else:
            err_console.print(f"\n[yellow]{len(warnings)} warning(s) (use --strict to fail)[/]")

    console.print("\n[green]All checks passed.[/]")


if __name__ == "__main__":
    app()
