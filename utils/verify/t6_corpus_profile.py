# /// script
# requires-python = ">=3.12"
# dependencies = ["rich"]
# ///
"""T6 VERIFY — Corpus profile from metadata.

Reads convert-manifest.csv and source-registry.md to produce a
sanity-check report before LLM extraction begins.
"""

import csv
import re
import statistics
import sys
from collections import defaultdict
from pathlib import Path

from rich.console import Console
from rich.table import Table

ROOT = Path(__file__).resolve().parent.parent.parent
MANIFEST = ROOT / "research" / "pipeline-canon" / "sources" / "convert-manifest.csv"
REGISTRY = ROOT / "research" / "pipeline-canon" / "source-registry.md"
OUTPUT = ROOT / "research" / "pipeline-canon" / "corpus-profile.md"

console = Console()


# ── Parse manifest ──────────────────────────────────────────────────

def parse_manifest() -> list[dict]:
    """Read manifest, deduplicate by output_path. Merge format/warnings from all rows."""
    rows = []
    with open(MANIFEST, newline="") as f:
        for row in csv.DictReader(f):
            rows.append(row)

    # Group by output_path, collect original format and any warnings
    by_output: dict[str, dict] = {}
    for row in rows:
        key = row["output_path"]
        if key not in by_output:
            by_output[key] = {
                **row,
                "orig_formats": set(),
                "all_warnings": [],
            }
        entry = by_output[key]
        fmt = row["format"]
        entry["orig_formats"].add(fmt)
        if row.get("warnings"):
            entry["all_warnings"].append(row["warnings"])

    # Pick the most descriptive original format (prefer non-md)
    for entry in by_output.values():
        fmts = entry["orig_formats"]
        non_md = fmts - {"md"}
        if non_md:
            entry["orig_format"] = sorted(non_md)[0]  # e.g. epub, pdf, jekyll-concat
        else:
            entry["orig_format"] = "md"
        entry["warnings"] = "; ".join(entry["all_warnings"]) if entry["all_warnings"] else ""

    return list(by_output.values())


# ── Parse registry ──────────────────────────────────────────────────

def parse_registry() -> list[dict]:
    """Extract table rows from the markdown registry."""
    text = REGISTRY.read_text()
    entries = []
    # Match markdown table rows: | # | title | ... |
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.split("|")[1:-1]]
        if len(cells) < 10:
            continue
        num = cells[0]
        if num in ("---", "#", ""):
            continue
        # Skip header-separator rows
        if all(c.startswith("-") for c in cells):
            continue
        entry = {
            "num": num,
            "title": cells[1],
            "author": cells[2],
            "year": cells[3],
            "lang": cells[4].upper().strip(),
            "type": cells[5].lower().strip(),
            "status": cells[8].strip(),
            "included": cells[9].strip(),
        }
        entries.append(entry)
    return entries


# ── Helpers ─────────────────────────────────────────────────────────

def lang_from_path(p: str) -> str:
    return p.split("/")[0].upper()


def format_from_row(row: dict) -> str:
    fmt = row.get("orig_format", row["format"])
    if fmt in ("epub", "pdf", "txt"):
        return fmt
    if "concat" in fmt:
        return "dir-concat"
    if "nicar" in fmt:
        return "NICAR"
    if fmt == "md":
        return "md-native"
    return fmt


def decade_from_year(year_str: str) -> str:
    m = re.search(r"((?:19|20)\d{2})", year_str)
    if not m:
        return "unknown"
    y = int(m.group(1))
    if y < 2010:
        return "pre-2010"
    elif y < 2020:
        return "2010s"
    else:
        return "2020s"


def fmt_words(n: int) -> str:
    if n >= 1_000_000:
        return f"{n / 1_000_000:.2f}M"
    if n >= 1_000:
        return f"{n / 1_000:.1f}K"
    return str(n)


# ── Report sections ─────────────────────────────────────────────────

def section_corpus_size(sources: list[dict], md_lines: list[str]):
    words = [s["words"] for s in sources]
    total = sum(words)
    med = int(statistics.median(words))
    console.rule("[bold]1. Corpus Size")
    console.print(f"  Sources: {len(sources)}")
    console.print(f"  Total words: {fmt_words(total)}")
    console.print(f"  Median: {fmt_words(med)}  Min: {fmt_words(min(words))}  Max: {fmt_words(max(words))}")

    md_lines.append("## 1. Corpus Size\n")
    md_lines.append(f"- **Sources**: {len(sources)}")
    md_lines.append(f"- **Total words**: {fmt_words(total)}")
    md_lines.append(f"- **Median**: {fmt_words(med)} | **Min**: {fmt_words(min(words))} | **Max**: {fmt_words(max(words))}")
    md_lines.append("")


def section_by_key(sources: list[dict], key: str, label: str, section_num: int, md_lines: list[str]):
    groups: dict[str, list[int]] = defaultdict(list)
    for s in sources:
        groups[s[key]].append(s["words"])

    table = Table(title=f"{section_num}. By {label}")
    table.add_column(label, style="cyan")
    table.add_column("Sources", justify="right")
    table.add_column("Words", justify="right")
    table.add_column("% Words", justify="right")

    total_words = sum(s["words"] for s in sources)
    for k in sorted(groups, key=lambda x: -sum(groups[x])):
        w = sum(groups[k])
        pct = w / total_words * 100 if total_words else 0
        table.add_row(k, str(len(groups[k])), fmt_words(w), f"{pct:.1f}%")

    console.rule(f"[bold]{section_num}. By {label}")
    console.print(table)

    md_lines.append(f"## {section_num}. By {label}\n")
    md_lines.append(f"| {label} | Sources | Words | % Words |")
    md_lines.append("|---|---:|---:|---:|")
    for k in sorted(groups, key=lambda x: -sum(groups[x])):
        w = sum(groups[k])
        pct = w / total_words * 100 if total_words else 0
        md_lines.append(f"| {k} | {len(groups[k])} | {fmt_words(w)} | {pct:.1f}% |")
    md_lines.append("")


def section_thin(sources: list[dict], md_lines: list[str]):
    thin = [s for s in sources if s["words"] < 1000]
    console.rule("[bold]6. Thin Sources (< 1,000 words)")
    if not thin:
        console.print("  None")
        md_lines.append("## 6. Thin Sources (< 1,000 words)\n\nNone.\n")
        return

    table = Table(title="Thin Sources")
    table.add_column("Output", style="cyan")
    table.add_column("Words", justify="right")
    table.add_column("Format")
    for s in sorted(thin, key=lambda x: x["words"]):
        table.add_row(s["output_path"], str(s["words"]), s["format"])
    console.print(table)

    md_lines.append("## 6. Thin Sources (< 1,000 words)\n")
    md_lines.append("| Output | Words | Format |")
    md_lines.append("|---|---:|---|")
    for s in sorted(thin, key=lambda x: x["words"]):
        md_lines.append(f"| `{s['output_path']}` | {s['words']} | {s['format']} |")
    md_lines.append("")


def section_gaps(sources: list[dict], registry: list[dict], md_lines: list[str]):
    """Sources marked included=yes in registry but not in manifest."""
    converted_nums = set()
    converted_parents = set()
    for s in sources:
        m = re.match(r"(?:\w+/)?([\d]+)([a-z]?)", s["output_path"])
        if m:
            base = m.group(1).lstrip("0") or "0"
            letter = m.group(2)
            converted_nums.add(base + letter)
            converted_parents.add(base)  # mark parent as having children

    gaps = []
    for entry in registry:
        if entry["included"] != "yes":
            continue
        raw = entry["num"].strip()
        # Normalize: extract digits and optional trailing letter
        m2 = re.match(r"(\d+)([a-z]?)", raw)
        if not m2:
            continue
        base = m2.group(1).lstrip("0") or "0"
        letter = m2.group(2)
        norm_num = base + letter
        # Match if exact num is in manifest, OR if this is a parent/child of a converted group
        if norm_num in converted_nums or base in converted_parents:
            continue
        gaps.append(entry)

    console.rule("[bold]7. Known Gaps (included but not converted)")
    if not gaps:
        console.print("  None")
        md_lines.append("## 7. Known Gaps\n\nNone — all included sources are converted.\n")
        return

    table = Table(title="Gaps")
    table.add_column("#")
    table.add_column("Title", max_width=50)
    table.add_column("Status")
    table.add_column("Lang")
    for g in gaps:
        table.add_row(g["num"], g["title"], g["status"], g["lang"])
    console.print(table)

    md_lines.append("## 7. Known Gaps (included but not converted)\n")
    md_lines.append("| # | Title | Status | Lang |")
    md_lines.append("|---|---|---|---|")
    for g in gaps:
        md_lines.append(f"| {g['num']} | {g['title']} | {g['status']} | {g['lang']} |")
    md_lines.append("")


def section_warnings(sources: list[dict], md_lines: list[str]):
    warned = [s for s in sources if s.get("warnings")]
    console.rule("[bold]8. Conversion Warnings")
    if not warned:
        console.print("  None")
        md_lines.append("## 8. Conversion Warnings\n\nNone.\n")
        return

    table = Table(title="Warnings")
    table.add_column("Output", style="cyan")
    table.add_column("Warning", max_width=80)
    for s in warned:
        table.add_row(s["output_path"], s["warnings"])
    console.print(table)

    md_lines.append("## 8. Conversion Warnings\n")
    md_lines.append("| Output | Warning |")
    md_lines.append("|---|---|")
    for s in warned:
        md_lines.append(f"| `{s['output_path']}` | {s['warnings']} |")
    md_lines.append("")


# ── Main ────────────────────────────────────────────────────────────

def main():
    if not MANIFEST.exists():
        console.print(f"[red]Manifest not found: {MANIFEST}")
        sys.exit(1)
    if not REGISTRY.exists():
        console.print(f"[red]Registry not found: {REGISTRY}")
        sys.exit(1)

    manifest_rows = parse_manifest()
    registry = parse_registry()

    # Build registry lookup: num → entry
    reg_by_num = {e["num"]: e for e in registry}

    # Build enriched source list
    sources = []
    for row in manifest_rows:
        m = re.match(r"(?:\w+/)?(\d+)", row["output_path"])
        num = m.group(1) if m else None
        reg_entry = reg_by_num.get(num, {})

        year_str = reg_entry.get("year", "")
        decade = decade_from_year(year_str)
        if decade == "unknown":
            # Fallback: try extracting year from filename
            decade = decade_from_year(row["output_path"])

        sources.append({
            "output_path": row["output_path"],
            "words": int(row["word_count"]),
            "format": format_from_row(row),
            "lang": lang_from_path(row["output_path"]),
            "type": reg_entry.get("type", "unknown"),
            "year": year_str or "unknown",
            "decade": decade,
            "warnings": row.get("warnings", ""),
            "status": row.get("status", ""),
        })

    md_lines: list[str] = [
        "# Corpus Profile — Data Pipeline Canon",
        f"_Generated: {__import__('datetime').date.today()}_\n",
    ]

    section_corpus_size(sources, md_lines)
    section_by_key(sources, "lang", "Language", 2, md_lines)
    section_by_key(sources, "format", "Format", 3, md_lines)
    section_by_key(sources, "type", "Type", 4, md_lines)
    section_by_key(sources, "decade", "Decade", 5, md_lines)
    section_thin(sources, md_lines)
    section_gaps(sources, registry, md_lines)
    section_warnings(sources, md_lines)

    # Write markdown
    OUTPUT.write_text("\n".join(md_lines) + "\n")
    console.rule("[bold green]Done")
    console.print(f"  Written to {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
