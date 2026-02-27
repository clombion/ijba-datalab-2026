# /// script
# requires-python = ">=3.12"
# dependencies = ["rich", "anthropic", "typer>=0.9.0"]
# ///
"""T8 TRANSLATE — LLM translation of non-EN corpus files to English.

Reads corpus-registry.csv to find non-EN sources, translates each via
Claude API, writes translated text back to corpus/ (in-place), and logs
results to translation-log.csv.

Idempotent: files with a <!-- translated --> marker are skipped.

Usage:
    uv run utils/clean/t8_translate_corpus.py              # translate all non-EN
    uv run utils/clean/t8_translate_corpus.py --dry-run    # show what would be translated
    uv run utils/clean/t8_translate_corpus.py --only 45    # translate only source #45

Requires ANTHROPIC_API_KEY in environment.
"""

from __future__ import annotations

import csv
import os
import re
import sys
import time
from pathlib import Path
from typing import Annotated

import anthropic
import typer
from rich.console import Console

__version__ = "1.0.0"

ROOT = Path(__file__).resolve().parent.parent.parent
CORPUS = ROOT / "research" / "pipeline-canon" / "corpus"
REGISTRY_CSV = CORPUS / "corpus-registry.csv"
TRANSLATION_LOG = CORPUS / "translation-log.csv"

console = Console()

app = typer.Typer(help=__doc__, add_completion=False, no_args_is_help=False)

MODEL = "claude-sonnet-4-20250514"
MAX_CHUNK_WORDS = 40_000  # split files larger than this
TRANSLATED_MARKER = "<!-- translated -->"

SYSTEM_PROMPT = """\
You are a professional translator specializing in journalism and media studies.
Translate the following text faithfully from {lang_name} to English.

Rules:
- Preserve all markdown formatting (headings, bold, italic, links, lists)
- Preserve YAML frontmatter blocks (--- delimited) — translate values but keep keys
- Keep proper nouns, organization names, and publication titles in their original form
  with an English translation in parentheses on first mention if not obvious
- Preserve academic citation formats (Author, Year) as-is
- Translate section headings
- Do not add commentary, notes, or explanations — output only the translation
- Maintain the same paragraph structure and line breaks"""

LANG_NAMES = {
    "ES": "Spanish",
    "PT": "Portuguese",
    "FR": "French",
}


def read_registry() -> list[dict]:
    """Read corpus-registry.csv, return non-EN rows."""
    rows = []
    with open(REGISTRY_CSV, newline="") as f:
        for row in csv.DictReader(f):
            if row["lang"] != "EN":
                rows.append(row)
    return rows


def is_already_translated(text: str) -> bool:
    """Check if file has the translated marker."""
    return TRANSLATED_MARKER in text[:200]


def split_into_chunks(text: str, max_words: int) -> list[str]:
    """Split text on ## headings, keeping chunks under max_words."""
    # Split on level-2 headings
    sections = re.split(r"(?=^## )", text, flags=re.MULTILINE)
    chunks: list[str] = []
    current: list[str] = []
    current_words = 0

    for section in sections:
        section_words = len(section.split())
        if current_words + section_words > max_words and current:
            chunks.append("\n".join(current))
            current = [section]
            current_words = section_words
        else:
            current.append(section)
            current_words += section_words

    if current:
        chunks.append("\n".join(current))
    return chunks


def translate_text(
    client: anthropic.Anthropic,
    text: str,
    lang: str,
) -> str:
    """Translate text via Claude API. Chunks if needed."""
    lang_name = LANG_NAMES.get(lang, lang)
    words = len(text.split())

    if words <= MAX_CHUNK_WORDS:
        return _translate_chunk(client, text, lang_name)

    # Chunk large files
    chunks = split_into_chunks(text, MAX_CHUNK_WORDS)
    console.print(f"    Splitting into {len(chunks)} chunks...")
    translated_chunks = []
    for i, chunk in enumerate(chunks):
        console.print(
            f"    Chunk {i + 1}/{len(chunks)} "
            f"({len(chunk.split()):,}w)...",
            end=" ",
        )
        result = _translate_chunk(client, chunk, lang_name)
        translated_chunks.append(result)
        console.print("[green]done[/]")
        if i < len(chunks) - 1:
            time.sleep(1)  # rate limit courtesy
    return "\n\n".join(translated_chunks)


def _translate_chunk(
    client: anthropic.Anthropic,
    text: str,
    lang_name: str,
) -> str:
    """Translate a single chunk via API."""
    message = client.messages.create(
        model=MODEL,
        max_tokens=16384,
        system=SYSTEM_PROMPT.format(lang_name=lang_name),
        messages=[{"role": "user", "content": text}],
    )
    return message.content[0].text


def version_callback(value: bool) -> None:
    if value:
        from rich.console import Console
        Console().print(f"t8-translate-corpus {__version__}")
        raise typer.Exit()


@app.command()
def main(
    dry_run: Annotated[bool, typer.Option("--dry-run", help="Show what would be translated.")] = False,
    only: Annotated[str | None, typer.Option("--only", help="Translate only source with this ID.")] = None,
    version: Annotated[bool | None, typer.Option("--version", callback=version_callback, is_eager=True, help="Show version.")] = None,
) -> None:
    if not REGISTRY_CSV.exists():
        console.print("[red]Registry not found. Run clean_corpus.py first.")
        raise typer.Exit(1)

    non_en = read_registry()
    if only:
        non_en = [r for r in non_en if r["id"] == only]

    console.rule(f"[bold]T8 TRANSLATE \u2014 {len(non_en)} non-EN sources")

    if not dry_run:
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            console.print("[red]ANTHROPIC_API_KEY not set.")
            raise typer.Exit(1)
        client = anthropic.Anthropic(api_key=api_key)

    log_rows: list[dict] = []

    try:
        for row in non_en:
            corpus_file = CORPUS / row["file"]
            if not corpus_file.exists():
                console.print(f"  [red]MISSING[/] {row['file']}")
                continue

            text = corpus_file.read_text()
            words_before = len(text.split())

            if is_already_translated(text):
                console.print(f"  [dim]SKIP (already translated)[/] {row['file']}")
                continue

            if dry_run:
                console.print(
                    f"  [cyan]WOULD TRANSLATE[/] {row['file']} "
                    f"({row['lang']}, {words_before:,}w)"
                )
                continue

            console.print(
                f"  [yellow]TRANSLATING[/] {row['file']} "
                f"({row['lang']}, {words_before:,}w)..."
            )

            try:
                translated = translate_text(client, text, row["lang"])
                words_after = len(translated.split())

                # Validate word count ratio
                ratio = words_after / words_before if words_before else 0
                if ratio < 0.5 or ratio > 2.0:
                    console.print(
                        f"    [red]WARNING: word ratio {ratio:.2f} "
                        f"({words_before:,} \u2192 {words_after:,})[/]"
                    )

                # Write with marker
                output = f"{TRANSLATED_MARKER}\n\n{translated}\n"
                corpus_file.write_text(output)

                console.print(
                    f"    [green]OK[/] {words_before:,}w \u2192 {words_after:,}w "
                    f"(ratio {ratio:.2f})"
                )

                log_rows.append({
                    "id": row["id"],
                    "file": row["file"],
                    "lang": row["lang"],
                    "words_before": words_before,
                    "words_after": words_after,
                    "ratio": f"{ratio:.2f}",
                    "status": "ok",
                })

            except Exception as e:
                console.print(f"    [red]ERROR: {e}[/]")
                log_rows.append({
                    "id": row["id"],
                    "file": row["file"],
                    "lang": row["lang"],
                    "words_before": words_before,
                    "words_after": 0,
                    "ratio": "0",
                    "status": f"error: {e}",
                })

            time.sleep(2)  # rate limit between files
    except KeyboardInterrupt:
        console.print("\n[yellow]Interrupted. Files processed so far are saved.[/]")

    # Write translation log
    if log_rows and not dry_run:
        fields = ["id", "file", "lang", "words_before", "words_after", "ratio", "status"]
        with open(TRANSLATION_LOG, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows(log_rows)
        console.print(f"\n  Log: {TRANSLATION_LOG.relative_to(ROOT)}")

    console.rule("[bold green]Done")


if __name__ == "__main__":
    app()
