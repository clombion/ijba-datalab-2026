#!/usr/bin/env python3
"""Download Newsroom Robots podcast episodes listed in the CSV."""

import csv
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from pathlib import Path

FEED_URL = "https://feeds.acast.com/public/shows/64c86a5585617f0011a4a263"
CSV_PATH = Path(__file__).parent / "newsroom_robots_episodes_since_2024.csv"
OUTPUT_DIR = Path(__file__).parent / "episodes"


def fetch_feed():
    """Parse RSS feed and return {(title, date_str): audio_url} mapping."""
    print("Fetching RSS feed...")
    with urllib.request.urlopen(FEED_URL) as resp:
        tree = ET.parse(resp)
    episodes = {}
    for item in tree.getroot().findall(".//item"):
        title_el = item.find("title")
        pub_el = item.find("pubDate")
        enc_el = item.find("enclosure")
        if title_el is not None and pub_el is not None and enc_el is not None:
            dt = parsedate_to_datetime(pub_el.text.strip())
            date_str = dt.strftime("%Y-%m-%d")
            episodes[(title_el.text.strip(), date_str)] = enc_el.get("url")
    return episodes


def sanitize_filename(name):
    """Remove characters that are unsafe for filenames."""
    name = re.sub(r'[<>:"/\\|?*]', "", name)
    name = name.strip(". ")
    return name[:180]


def main():
    feed_episodes = fetch_feed()

    # Read CSV to get the target episodes
    targets = []
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            title = row["Title"].strip()
            date = row["Release Date"].strip()
            targets.append((title, date))

    OUTPUT_DIR.mkdir(exist_ok=True)

    total = len(targets)
    downloaded = 0
    skipped = 0

    for i, (title, date) in enumerate(targets, 1):
        audio_url = feed_episodes.get((title, date))
        if not audio_url:
            print(f"[{i}/{total}] SKIP (no audio URL): {title[:60]}")
            skipped += 1
            continue

        filename = f"{date} - {sanitize_filename(title)}.mp3"
        filepath = OUTPUT_DIR / filename

        if filepath.exists():
            print(f"[{i}/{total}] EXISTS: {filename[:70]}")
            skipped += 1
            continue

        print(f"[{i}/{total}] Downloading: {filename[:70]}...")
        try:
            urllib.request.urlretrieve(audio_url, filepath)
            downloaded += 1
        except Exception as e:
            print(f"  ERROR: {e}")
            skipped += 1

    print(f"\nDone. Downloaded: {downloaded}, Skipped: {skipped}, Total: {total}")


if __name__ == "__main__":
    main()
