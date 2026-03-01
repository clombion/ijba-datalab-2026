# /// script
# requires-python = ">=3.12"
# dependencies = ["typer>=0.9.0", "rich>=13.0.0"]
# ///
"""Build self-contained contextual recode review HTML.

Reads matched_passages/ + transcripts + codebook.json.
Assembles a single blob, gzips, base64-encodes, and injects into template.html.

Usage:
    uv run research/newsroom-robots/scripts/review/build.py [--output PATH] [--dry-run]
"""

from __future__ import annotations

import base64
import gzip
import json
from pathlib import Path

import typer

app = typer.Typer(add_completion=False)

NEWSROOM_ROOT = Path(__file__).resolve().parent.parent.parent
HERE = Path(__file__).resolve().parent

MATCHED_DIR = NEWSROOM_ROOT / "outputs" / "matched_passages"
CODEBOOK_PATH = NEWSROOM_ROOT / "outputs" / "codebook.json"
EPISODES_DIR = NEWSROOM_ROOT / "episodes"

# fflate 0.8.2 UMD — vendored at build time
FFLATE_PATH = Path("/tmp/fflate-0.8.2.umd.js")
FFLATE_CDN = "https://cdn.jsdelivr.net/npm/fflate@0.8.2/umd/index.js"


def _ensure_fflate() -> str:
    """Return fflate UMD source, downloading if needed."""
    if FFLATE_PATH.exists():
        return FFLATE_PATH.read_text()
    import urllib.request

    typer.echo("Downloading fflate 0.8.2 from CDN...")
    urllib.request.urlretrieve(FFLATE_CDN, FFLATE_PATH)
    return FFLATE_PATH.read_text()


def _build_data() -> dict:
    """Assemble episodes + codebook + transcripts into a single dict."""
    codebook_raw = json.loads(CODEBOOK_PATH.read_text())

    # Build codebook lookup: { "T01": { "name": ..., "sub_themes": { "T01.1": "..." } } }
    codebook = {}
    for theme in codebook_raw["themes"]:
        subs = {}
        for st in theme.get("sub_themes", []):
            subs[st["id"]] = st["name"]
        codebook[theme["id"]] = {"name": theme["name"], "sub_themes": subs}

    # Build episodes sorted by date
    episodes = []
    matched_files = sorted(MATCHED_DIR.glob("*.json"))

    for mp_path in matched_files:
        mp = json.loads(mp_path.read_text())

        # Load transcript
        transcript_file = mp.get("transcript_file", "")
        transcript = ""
        if transcript_file:
            transcript_path = EPISODES_DIR / transcript_file
            if transcript_path.exists():
                transcript = transcript_path.read_text(encoding="utf-8")

        # Classify themes by relevance
        primary = []
        secondary = []
        tangential = []
        for m in mp.get("matches", []):
            rel = m.get("relevance", "tangential")
            tid = m["theme_id"]
            if rel == "primary":
                primary.append(tid)
            elif rel == "secondary":
                secondary.append(tid)
            else:
                tangential.append(tid)

        episodes.append({
            "date": mp.get("episode_date", ""),
            "title": mp.get("episode_title", ""),
            "guests": mp.get("guests", []),
            "host": mp.get("host", "Nikita Roy"),
            "summary_claims": mp.get("summary_claims", []),
            "transcript": transcript,
            "matches": mp.get("matches", []),
            "primary_themes": primary,
            "secondary_themes": secondary,
            "tangential_themes": tangential,
        })

    return {"episodes": episodes, "codebook": codebook}


@app.command()
def build(
    output: Path = typer.Option(
        HERE / "index.html",
        "--output",
        help="Output HTML path",
    ),
    dry_run: bool = typer.Option(False, "--dry-run", help="Show sizes without writing"),
) -> None:
    """Build the self-contained contextual recode review tool HTML."""
    # 1. Build data blob → gzip → base64
    data = _build_data()
    json_str = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    json_bytes = json_str.encode("utf-8")
    compressed = gzip.compress(json_bytes, compresslevel=9)
    b64 = base64.b64encode(compressed).decode("ascii")

    total_codings = sum(len(ep["matches"]) for ep in data["episodes"])
    transcript_bytes = sum(len(ep["transcript"].encode()) for ep in data["episodes"])
    typer.echo(f"Episodes: {len(data['episodes'])}")
    typer.echo(f"Total codings: {total_codings}")
    typer.echo(f"Transcript text: {transcript_bytes:,} bytes")
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
