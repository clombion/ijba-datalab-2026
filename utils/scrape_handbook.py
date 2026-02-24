#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "typer>=0.9.0",
#     "rich>=13.0.0",
#     "requests>=2.31.0",
#     "beautifulsoup4>=4.12.0",
#     "markdownify>=0.13.0",
# ]
# ///
"""Scrape the Data Journalism Handbook 2 to local markdown files.

Assumptions:
- Network access to https://datajournalism.com
- Site structure: TOC at /read/handbook/two with section headers (h5)
  and article links in ul/li elements
- Each article page has a main content area with title, byline, and body

Exit codes:
  0  All articles scraped successfully
  1  Some articles failed (skipped, logged at end)
  64 No articles found on TOC page (site structure changed?)
"""

from __future__ import annotations

import re
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Annotated

import requests
import typer
from bs4 import BeautifulSoup, Tag
from markdownify import markdownify as md
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

BASE_URL = "https://datajournalism.com"
TOC_URL = f"{BASE_URL}/read/handbook/two"

STRIP_SELECTORS = [
    "nav",
    "footer",
    "header",
    "script",
    "style",
    "noscript",
    ".newsletter",
    ".sidebar",
    ".menu",
    ".breadcrumb",
    ".cookie",
    ".social",
    "[class*='nav']",
    "[class*='footer']",
    "[class*='header']",
    "[class*='menu']",
    "[class*='share']",
    "[class*='related']",
    "[class*='comment']",
]

console = Console()
err_console = Console(stderr=True)

# ---------------------------------------------------------------------------
# Types
# ---------------------------------------------------------------------------


@dataclass
class Article:
    title: str
    authors: list[str]
    section_name: str
    section_slug: str
    section_index: int
    slug: str
    url: str
    markdown: str = ""


# ---------------------------------------------------------------------------
# Pure functions
# ---------------------------------------------------------------------------


def slugify(text: str) -> str:
    """Convert text to a filesystem-safe slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[-\s]+", "-", text)
    return text.strip("-")


def section_dir_name(index: int, slug: str) -> str:
    """Generate numbered section directory name."""
    return f"{index:02d}-{slug}"


def make_frontmatter(article: Article) -> str:
    """Generate YAML frontmatter for an article."""
    authors_str = ", ".join(f'"{a}"' for a in article.authors)
    return (
        "---\n"
        f"title: \"{article.title.replace('"', '\\'+'\"')}\"\n"
        f"authors: [{authors_str}]\n"
        f"section: \"{article.section_name}\"\n"
        f"source_url: \"{article.url}\"\n"
        "---\n\n"
    )


def clean_markdown(raw_md: str) -> str:
    """Clean up converted markdown."""
    # Remove excessive blank lines
    cleaned = re.sub(r"\n{4,}", "\n\n\n", raw_md)
    # Remove trailing whitespace on lines
    cleaned = re.sub(r" +\n", "\n", cleaned)
    # Strip leading/trailing whitespace
    cleaned = cleaned.strip()
    return cleaned


# ---------------------------------------------------------------------------
# Parsing functions
# ---------------------------------------------------------------------------


def parse_toc(html: str) -> list[Article]:
    """Parse the TOC page using handbook-overview__section containers."""
    soup = BeautifulSoup(html, "html.parser")
    articles: list[Article] = []
    seen_urls: set[str] = set()

    sections = soup.find_all("div", class_="handbook-overview__section")

    for section_index, section_div in enumerate(sections):
        # Section name from the header
        head = section_div.find("div", class_="handbook-group__head")
        section_name = head.get_text(strip=True) if head else f"Section {section_index}"
        section_slug = slugify(section_name)

        # All article links within this section
        for a in section_div.find_all("a", href=True):
            href = a["href"]
            if "/read/handbook/two/" not in href:
                continue
            if not href.startswith("http"):
                href = BASE_URL + href

            title = a.get_text(strip=True)
            if not title:
                continue
            if href in seen_urls:
                continue
            seen_urls.add(href)

            article_slug = href.rstrip("/").split("/")[-1]

            articles.append(
                Article(
                    title=title,
                    authors=[],
                    section_name=section_name,
                    section_slug=section_slug,
                    section_index=section_index,
                    slug=article_slug,
                    url=href,
                )
            )

    return articles


def extract_article_content(html: str, article: Article) -> Article:
    """Extract article content from an article page and update the Article."""
    soup = BeautifulSoup(html, "html.parser")

    # Title from h2.article__title
    title_el = soup.find("h2", class_="article__title")
    if title_el:
        article.title = title_el.get_text(strip=True)

    # Content from div.article__entry
    entry = soup.find("div", class_="article__entry")

    # Fallback: largest div with paragraphs
    if not entry:
        candidates = []
        for div in soup.find_all("div"):
            p_count = len(div.find_all("p", recursive=False))
            if p_count >= 2:
                candidates.append((p_count, div))
        if candidates:
            candidates.sort(key=lambda x: x[0], reverse=True)
            entry = candidates[0][1]

    if not entry:
        entry = soup.find("body") or soup

    # Extract authors from "Written by" paragraph before converting
    authors: list[str] = []
    for p in entry.find_all("p"):
        text = p.get_text(strip=True)
        if text.lower().startswith("written by"):
            # Authors may be in <strong>, <a>, or plain text
            for strong in p.find_all("strong"):
                name = strong.get_text(strip=True)
                if name:
                    authors.append(name)
            if not authors:
                for a in p.find_all("a"):
                    name = a.get_text(strip=True)
                    if name and len(name) > 1:
                        authors.append(name)
            if not authors:
                text_after = re.sub(r"(?i)written\s+by:?\s*", "", text)
                if text_after:
                    authors = [
                        n.strip()
                        for n in re.split(r",|&| and ", text_after)
                        if n.strip()
                    ]
            # Remove the "Written by" paragraph from content
            p.decompose()
            break

    # Strip unwanted elements from the entry
    for selector in STRIP_SELECTORS:
        for el in entry.select(selector):
            el.decompose()

    # Convert to markdown
    raw_md = md(str(entry), heading_style="ATX", strip=["img"])
    article.markdown = clean_markdown(raw_md)
    article.authors = authors or article.authors

    return article


# ---------------------------------------------------------------------------
# I/O functions
# ---------------------------------------------------------------------------


def fetch_page(url: str) -> str:
    """Fetch a page and return its HTML content."""
    resp = requests.get(url, timeout=30, headers={"User-Agent": "DataJHandbook-Scraper/1.0"})
    resp.raise_for_status()
    return resp.text


def write_article(article: Article, output_dir: Path) -> Path:
    """Write an article to a markdown file. Returns the file path."""
    section_dir = output_dir / section_dir_name(article.section_index, article.section_slug)
    section_dir.mkdir(parents=True, exist_ok=True)

    filename = f"{article.slug}.md"
    filepath = section_dir / filename

    content = make_frontmatter(article) + article.markdown
    filepath.write_text(content, encoding="utf-8")
    return filepath


def write_index(articles: list[Article], output_dir: Path) -> Path:
    """Generate an index.md with TOC grouped by section."""
    output_dir.mkdir(parents=True, exist_ok=True)
    filepath = output_dir / "index.md"

    lines = ["# Data Journalism Handbook 2\n"]
    lines.append(f"Source: {TOC_URL}\n\n")
    lines.append(f"**{len(articles)} articles** across {len(set(a.section_index for a in articles))} sections.\n\n")

    current_section = -1
    for article in sorted(articles, key=lambda a: (a.section_index, a.slug)):
        if article.section_index != current_section:
            current_section = article.section_index
            section_dir = section_dir_name(article.section_index, article.section_slug)
            lines.append(f"\n## {article.section_name}\n\n")
        rel_path = f"{section_dir}/{article.slug}.md"
        authors = f" — {', '.join(article.authors)}" if article.authors else ""
        lines.append(f"- [{article.title}]({rel_path}){authors}\n")

    filepath.write_text("".join(lines), encoding="utf-8")
    return filepath


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

app = typer.Typer(add_completion=False)


@app.command()
def main(
    output_dir: Annotated[
        Path, typer.Option(help="Output directory for markdown files")
    ] = Path("research/ddj-handbook-2"),
    dry_run: Annotated[
        bool, typer.Option("--dry-run", "-n", help="List articles without downloading")
    ] = False,
    delay: Annotated[
        float, typer.Option(help="Seconds between requests")
    ] = 1.5,
    verbose: Annotated[
        bool, typer.Option("--verbose", "-v", help="Show detailed progress")
    ] = False,
) -> None:
    """Scrape the Data Journalism Handbook 2 to local markdown files."""
    # Step 1: Fetch and parse TOC
    console.print(f"Fetching TOC from {TOC_URL}...")
    try:
        toc_html = fetch_page(TOC_URL)
    except requests.RequestException as e:
        err_console.print(f"[red]Failed to fetch TOC: {e}[/red]")
        raise typer.Exit(69)

    articles = parse_toc(toc_html)

    if not articles:
        err_console.print("[red]No articles found on TOC page. Site structure may have changed.[/red]")
        raise typer.Exit(64)

    console.print(f"Found [bold]{len(articles)}[/bold] articles across "
                  f"{len(set(a.section_index for a in articles))} sections.\n")

    # Show article list
    if dry_run or verbose:
        current_section = -1
        for article in sorted(articles, key=lambda a: (a.section_index, a.slug)):
            if article.section_index != current_section:
                current_section = article.section_index
                console.print(f"\n[bold cyan]{article.section_name}[/bold cyan]")
            console.print(f"  {article.title}")
            if verbose:
                console.print(f"    [dim]{article.url}[/dim]")

    if dry_run:
        console.print(f"\n[yellow]Dry run:[/yellow] Would download {len(articles)} articles to {output_dir}/")
        raise typer.Exit(0)

    # Step 2: Fetch each article
    failed: list[tuple[Article, str]] = []
    succeeded: list[Article] = []

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        TextColumn("[progress.percentage]{task.completed}/{task.total}"),
        console=console,
    ) as progress:
        task = progress.add_task("Scraping articles...", total=len(articles))

        for i, article in enumerate(articles):
            progress.update(task, description=f"[cyan]{article.title[:50]}...[/cyan]" if len(article.title) > 50 else f"[cyan]{article.title}[/cyan]")

            try:
                html = fetch_page(article.url)
                extract_article_content(html, article)

                if not article.markdown:
                    failed.append((article, "Empty content after extraction"))
                    continue

                filepath = write_article(article, output_dir)
                succeeded.append(article)

                if verbose:
                    console.print(f"  [green]✓[/green] {filepath}")

            except requests.RequestException as e:
                failed.append((article, str(e)))
                err_console.print(f"  [red]✗[/red] {article.title}: {e}")

            progress.advance(task)

            # Rate limit (skip delay on last item)
            if i < len(articles) - 1:
                time.sleep(delay)

    # Step 3: Write index
    index_path = write_index(succeeded, output_dir)

    # Step 4: Report
    console.print(f"\n[bold green]Done![/bold green] {len(succeeded)}/{len(articles)} articles saved to {output_dir}/")
    console.print(f"Index: {index_path}")

    if failed:
        console.print(f"\n[bold yellow]Failed ({len(failed)}):[/bold yellow]")
        for article, reason in failed:
            console.print(f"  [red]✗[/red] {article.title}: {reason}")
            console.print(f"    {article.url}")
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
