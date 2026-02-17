#!/usr/bin/env python3
"""Build manifest.csv from episode CSV metadata + transcript word counts."""

import csv
import re
from pathlib import Path

CSV_PATH = Path(__file__).parent / "newsroom_robots_episodes_since_2024.csv"
EPISODES_DIR = Path(__file__).parent.parent / "episodes"
OUTPUT_PATH = Path(__file__).parent.parent / "outputs" / "manifest.csv"


def parse_guests_and_org(title: str) -> tuple[str, str]:
    """Extract guest name(s) and infer organization from episode title."""
    # Title format: "Guest Name: Topic description" or "Guest Name Topic description"
    # Try colon split first
    if ":" in title:
        guest_part = title.split(":")[0].strip()
    else:
        # No colon — the guest name is harder to parse; return full title
        guest_part = title.split("  ")[0].strip() if "  " in title else ""

    return guest_part, ""


def sanitize_filename(name: str) -> str:
    name = re.sub(r'[<>:"/\\|?*]', "", name)
    name = name.strip(". ")
    return name[:180]


def make_slug(date: str, title: str) -> str:
    """Create a short slug from date and title for output filenames."""
    # Take first ~40 chars of sanitized title, lowercase, replace spaces with hyphens
    clean = re.sub(r'[^a-z0-9\s-]', '', title.lower())
    clean = re.sub(r'\s+', '-', clean.strip())[:60]
    return f"{date}-{clean}"


def main():
    rows = []
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            title = row["Title"].strip()
            date = row["Release Date"].strip()
            link = row["Link"].strip()

            guest, org = parse_guests_and_org(title)

            # Find matching transcript
            safe_title = sanitize_filename(title)
            transcript_name = f"{date} - {safe_title}.txt"
            transcript_path = EPISODES_DIR / transcript_name

            word_count = 0
            has_transcript = False
            if transcript_path.exists():
                text = transcript_path.read_text(encoding="utf-8")
                word_count = len(text.split())
                has_transcript = True

            slug = make_slug(date, title)

            rows.append({
                "date": date,
                "title": title,
                "guest": guest,
                "link": link,
                "transcript_file": transcript_name if has_transcript else "",
                "word_count": word_count,
                "slug": slug,
                "has_transcript": has_transcript,
            })

    # Sort by date
    rows.sort(key=lambda r: r["date"])

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "date", "title", "guest", "link",
            "transcript_file", "word_count", "slug", "has_transcript"
        ])
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} episodes to {OUTPUT_PATH}")
    total_words = sum(r["word_count"] for r in rows)
    transcribed = sum(1 for r in rows if r["has_transcript"])
    print(f"Transcripts found: {transcribed}/{len(rows)}, Total words: {total_words:,}")


if __name__ == "__main__":
    main()
