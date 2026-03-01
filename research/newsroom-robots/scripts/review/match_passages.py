# /// script
# requires-python = ">=3.12"
# dependencies = ["typer>=0.9.0", "rich>=13.0.0"]
# ///
"""Match recode quotes to transcript positions.

Reads recode JSONs + extraction JSONs + manifest + transcripts.
Outputs one JSON per episode to outputs/matched_passages/ with
character offsets for each quote in the transcript.

Usage:
    uv run research/newsroom-robots/scripts/review/match_passages.py
"""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer(add_completion=False)
console = Console()

NEWSROOM_ROOT = Path(__file__).resolve().parent.parent.parent
RECODES_DIR = NEWSROOM_ROOT / "outputs" / "episode_recodes"
EXTRACTIONS_DIR = NEWSROOM_ROOT / "outputs" / "episode_extractions"
CODEBOOK_PATH = NEWSROOM_ROOT / "outputs" / "codebook.json"
MANIFEST_PATH = NEWSROOM_ROOT / "outputs" / "manifest.csv"
EPISODES_DIR = NEWSROOM_ROOT / "episodes"
OUTPUT_DIR = NEWSROOM_ROOT / "outputs" / "matched_passages"


def _load_manifest() -> dict[str, list[dict]]:
    """Load manifest as {date: [row_dict, ...]} to handle duplicate dates."""
    rows: dict[str, list[dict]] = {}
    with MANIFEST_PATH.open(newline="") as f:
        for row in csv.DictReader(f):
            rows.setdefault(row["date"], []).append(row)
    return rows


def _best_manifest_row(
    manifest: dict[str, list[dict]], ep_date: str, ep_title: str
) -> dict | None:
    """Find the best manifest row for a given episode date and title."""
    candidates = manifest.get(ep_date, [])
    if not candidates:
        return None
    if len(candidates) == 1:
        return candidates[0]
    # Multiple episodes on same date — match by title overlap
    title_lower = ep_title.lower()
    best = candidates[0]
    best_score = 0
    for row in candidates:
        row_title = row.get("title", "").lower()
        # Count shared words
        title_words = set(title_lower.split())
        row_words = set(row_title.split())
        score = len(title_words & row_words)
        if score > best_score:
            best_score = score
            best = row
    return best


def _normalize(text: str) -> str:
    """Normalize whitespace for matching."""
    return re.sub(r"\s+", " ", text).strip()


def _find_sentence_boundary(transcript: str, pos: int, direction: str) -> int:
    """Find the nearest sentence boundary from pos."""
    if direction == "forward":
        # Look for sentence-ending punctuation followed by space or end
        match = re.search(r"[.!?](?:\s|$)", transcript[pos:])
        if match:
            return pos + match.end()
        return len(transcript)
    else:  # backward
        # Look backwards from pos for sentence-ending punctuation
        chunk = transcript[:pos]
        match = re.search(r"[.!?]\s+", chunk[::-1])
        if match:
            return pos - match.end()
        return 0


def _match_quote(transcript: str, quote_text: str) -> dict:
    """Try cascading match strategies. Returns match info dict."""
    if not quote_text:
        return {"passage_start": None, "passage_end": None,
                "match_method": "none", "matched_text": ""}

    norm_transcript = _normalize(transcript)
    norm_quote = _normalize(quote_text)

    # Strategy 1: Exact substring match (normalized)
    idx = norm_transcript.find(norm_quote)
    if idx >= 0:
        # Map back to original transcript positions
        start = _map_norm_to_orig(transcript, norm_transcript, idx)
        end = _map_norm_to_orig(transcript, norm_transcript, idx + len(norm_quote))
        return {
            "passage_start": start,
            "passage_end": end,
            "match_method": "exact",
            "matched_text": transcript[start:end],
        }

    # Strategy 2: Case-insensitive exact
    lower_transcript = norm_transcript.lower()
    lower_quote = norm_quote.lower()
    idx = lower_transcript.find(lower_quote)
    if idx >= 0:
        start = _map_norm_to_orig(transcript, norm_transcript, idx)
        end = _map_norm_to_orig(transcript, norm_transcript, idx + len(norm_quote))
        return {
            "passage_start": start,
            "passage_end": end,
            "match_method": "exact-ci",
            "matched_text": transcript[start:end],
        }

    # Strategy 3: Anchor-based (first N words)
    words = norm_quote.split()
    for n in (8, 6, 5, 4):
        if len(words) < n:
            continue
        anchor = " ".join(words[:n]).lower()
        anchor_idx = lower_transcript.find(anchor)
        if anchor_idx >= 0:
            return _build_anchor_result(
                transcript, norm_transcript, norm_quote, anchor_idx, f"anchor-{n}"
            )

    # Strategy 4: Strip brackets [editorial insertions] and retry
    stripped = re.sub(r"\[.*?\]", "", norm_quote)
    stripped = _normalize(stripped)
    if stripped != norm_quote:
        stripped_lower = stripped.lower()
        idx = lower_transcript.find(stripped_lower)
        if idx >= 0:
            start = _map_norm_to_orig(transcript, norm_transcript, idx)
            end = _map_norm_to_orig(transcript, norm_transcript, idx + len(stripped))
            return {
                "passage_start": start,
                "passage_end": end,
                "match_method": "bracket-strip",
                "matched_text": transcript[start:end],
            }
        # Also try anchor with stripped version
        stripped_words = stripped.split()
        for n in (8, 6, 5, 4):
            if len(stripped_words) < n:
                continue
            anchor = " ".join(stripped_words[:n]).lower()
            anchor_idx = lower_transcript.find(anchor)
            if anchor_idx >= 0:
                return _build_anchor_result(
                    transcript, norm_transcript, norm_quote, anchor_idx, f"bracket-anchor-{n}"
                )

    # Strategy 5: Sliding window — try distinctive word chunks from middle of quote
    # The LLM sometimes edits the start of quotes, but middle phrases remain
    # Use chunk position as anchor, extend by approximate quote length (capped)
    quote_char_len = min(len(norm_quote), 500)  # cap passage length
    for n in (6, 5, 4):
        if len(words) < n + 2:
            continue
        for start_word in range(1, len(words) - n + 1):
            chunk = " ".join(words[start_word:start_word + n]).lower()
            if len(chunk) < 20:
                continue
            chunk_idx = lower_transcript.find(chunk)
            if chunk_idx >= 0:
                # Use chunk as center, extend outward
                approx_start = max(0, chunk_idx - min(start_word * 7, quote_char_len // 2))
                orig_start = _map_norm_to_orig(transcript, norm_transcript, approx_start)
                orig_start = max(0, _find_sentence_boundary(transcript, orig_start, "backward"))
                approx_end = min(chunk_idx + len(chunk) + quote_char_len // 2, len(norm_transcript))
                orig_end = _map_norm_to_orig(transcript, norm_transcript, approx_end)
                orig_end = min(_find_sentence_boundary(transcript, orig_end, "forward"), len(transcript))
                # Sanity: passage shouldn't exceed ~800 chars
                if orig_end - orig_start > 800:
                    orig_end = orig_start + 800
                    orig_end = min(_find_sentence_boundary(transcript, orig_end, "forward"), len(transcript))
                return {
                    "passage_start": orig_start,
                    "passage_end": orig_end,
                    "match_method": f"window-{n}",
                    "matched_text": transcript[orig_start:orig_end],
                }

    # Strategy 6: Normalize quotes/apostrophes and retry key phrases
    # Transcripts often use straight quotes, recodes use curly
    quote_cleaned = norm_quote.replace("\u2018", "'").replace("\u2019", "'")
    quote_cleaned = quote_cleaned.replace("\u201c", '"').replace("\u201d", '"')
    quote_cleaned = quote_cleaned.replace("\u2014", "-").replace("\u2013", "-")
    if quote_cleaned != norm_quote:
        cleaned_lower = quote_cleaned.lower()
        cleaned_words = cleaned_lower.split()
        for n in (8, 6, 5, 4):
            if len(cleaned_words) < n:
                continue
            anchor = " ".join(cleaned_words[:n])
            anchor_idx = lower_transcript.find(anchor)
            if anchor_idx >= 0:
                return _build_anchor_result(
                    transcript, norm_transcript, norm_quote, anchor_idx, f"cleaned-anchor-{n}"
                )

    return {"passage_start": None, "passage_end": None,
            "match_method": "none", "matched_text": ""}


def _build_anchor_result(
    transcript: str, norm_transcript: str, norm_quote: str,
    anchor_idx: int, method: str
) -> dict:
    """Build match result from an anchor position."""
    orig_start = _map_norm_to_orig(transcript, norm_transcript, anchor_idx)
    approx_end = anchor_idx + len(norm_quote)
    if approx_end > len(norm_transcript):
        approx_end = len(norm_transcript)
    orig_end = _map_norm_to_orig(transcript, norm_transcript, approx_end)
    orig_end = _find_sentence_boundary(transcript, orig_end, "forward")
    return {
        "passage_start": orig_start,
        "passage_end": min(orig_end, len(transcript)),
        "match_method": method,
        "matched_text": transcript[orig_start:min(orig_end, len(transcript))],
    }


def _map_norm_to_orig(original: str, normalized: str, norm_pos: int) -> int:
    """Map a position in normalized text back to original text position."""
    # Walk both strings in parallel
    orig_i = 0
    norm_i = 0
    while norm_i < norm_pos and orig_i < len(original):
        if original[orig_i].isspace():
            # In normalized, consecutive whitespace is collapsed to single space
            if norm_i < len(normalized) and normalized[norm_i] == " ":
                norm_i += 1
            # Skip all whitespace in original
            while orig_i < len(original) and original[orig_i].isspace():
                orig_i += 1
        else:
            norm_i += 1
            orig_i += 1
    return orig_i


def _process_episode(
    recode_path: Path,
    manifest: dict[str, list[dict]],
) -> dict | None:
    """Process one episode, return matched_passages dict or None."""
    recode = json.loads(recode_path.read_text())
    ep_date = recode.get("episode_date") or recode.get("date", "")
    ep_title = recode.get("episode_title", "")

    # Load extraction for metadata
    extraction_path = EXTRACTIONS_DIR / recode_path.name
    guests: list[dict] = []
    host = "Nikita Roy"
    summary_claims: list[str] = []
    if extraction_path.exists():
        extraction = json.loads(extraction_path.read_text())
        meta = extraction.get("episode_meta", {})
        guests = meta.get("guests", [])
        host = meta.get("host", "Nikita Roy")
        for kc in extraction.get("key_claims", []):
            summary_claims.append(kc.get("claim", ""))

    # Find transcript file via manifest (handles duplicate dates)
    manifest_row = _best_manifest_row(manifest, ep_date, ep_title)
    if not manifest_row:
        console.print(f"[yellow]No manifest entry for {ep_date}[/yellow]")
        return None

    transcript_file = manifest_row["transcript_file"]
    transcript_path = EPISODES_DIR / transcript_file
    if not transcript_path.exists():
        console.print(f"[yellow]Transcript not found: {transcript_file}[/yellow]")
        return None

    transcript = transcript_path.read_text(encoding="utf-8")

    # Match each theme coding
    matches = []
    for tc in recode.get("theme_codings", []):
        quote_text = ""
        speaker = ""
        if tc.get("best_quote"):
            quote_text = tc["best_quote"].get("text", "")
            speaker = tc["best_quote"].get("speaker", "")

        match_info = _match_quote(transcript, quote_text)
        matches.append({
            "theme_id": tc["theme_id"],
            "theme_name": tc.get("theme_name", ""),
            "relevance": tc.get("relevance", "tangential"),
            "sub_themes_present": tc.get("sub_themes_present", []),
            "best_quote": {"text": quote_text, "speaker": speaker},
            "summary": tc.get("summary", ""),
            "passage_start": match_info["passage_start"],
            "passage_end": match_info["passage_end"],
            "match_method": match_info["match_method"],
            "matched_text": match_info["matched_text"],
        })

    return {
        "episode_date": ep_date,
        "episode_title": recode.get("episode_title", ""),
        "transcript_file": transcript_file,
        "summary_claims": summary_claims[:4],
        "guests": guests,
        "host": host,
        "matches": matches,
    }


@app.command()
def main(
    output_dir: Path = typer.Option(
        OUTPUT_DIR, "--output-dir", help="Output directory for matched passage JSONs"
    ),
    dry_run: bool = typer.Option(False, "--dry-run", help="Print stats without writing"),
) -> None:
    """Match recode quotes to transcript positions."""
    manifest = _load_manifest()
    recode_files = sorted(RECODES_DIR.glob("*.json"))

    stats: dict[str, int] = {"total": 0, "none": 0}
    episode_stats: list[tuple[str, int, int]] = []

    output_dir.mkdir(parents=True, exist_ok=True)

    for recode_path in recode_files:
        result = _process_episode(recode_path, manifest)
        if not result:
            continue

        ep_matched = 0
        ep_total = len(result["matches"])
        for m in result["matches"]:
            stats["total"] += 1
            method = m["match_method"]
            if method == "none":
                stats["none"] += 1
            else:
                # Group by method family
                family = method.split("-")[0] if "-" in method else method
                stats[family] = stats.get(family, 0) + 1
                ep_matched += 1

        episode_stats.append((result["episode_date"], ep_matched, ep_total))

        if not dry_run:
            out_path = output_dir / recode_path.name
            out_path.write_text(
                json.dumps(result, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )

    # Print summary
    matched = stats["total"] - stats["none"]
    rate = (matched / stats["total"] * 100) if stats["total"] else 0

    console.print()
    table = Table(title="Match Results")
    table.add_column("Method", style="bold")
    table.add_column("Count", justify="right")
    for method, count in sorted(stats.items()):
        if method not in ("total", "none"):
            table.add_row(method, str(count))
    table.add_row("No match", str(stats["none"]))
    table.add_row("Total", str(stats["total"]), style="bold")
    table.add_row("Match rate", f"{rate:.1f}%", style="green" if rate > 80 else "yellow")
    console.print(table)

    # Show unmatched episodes
    unmatched_eps = [(d, m, t) for d, m, t in episode_stats if m < t]
    if unmatched_eps:
        console.print(f"\n[yellow]Episodes with unmatched quotes ({len(unmatched_eps)}):[/yellow]")
        for date, m, t in unmatched_eps:
            console.print(f"  {date}: {m}/{t} matched")

    if dry_run:
        console.print("\n[dim]Dry run — no files written.[/dim]")
    else:
        console.print(f"\n[green]Written {len(episode_stats)} files to {output_dir}[/green]")


if __name__ == "__main__":
    app()
