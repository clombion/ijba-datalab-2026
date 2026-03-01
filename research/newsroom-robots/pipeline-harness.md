# Newsroom Robots Analysis Pipeline

42 episodes of the Newsroom Robots podcast (Jan 2024 – Jan 2026, ~339K words), analyzed through a 7-pass thematic analysis. 12 themes, 48 sub-themes, 151 output files.

## Pipeline structure

| Pass | Input | Output | Files |
|------|-------|--------|-------|
| 0 | Corpus inspection | Confirmed scope, `manifest.csv` | 1 |
| 1 | Each transcript | `episode_extractions/*.json` | 42 |
| 2 | Each transcript + extraction | `episode_codes/*.json` | 42 |
| 3 | All codes aggregated | `codebook.json` | 1 |
| 4 | Each transcript + codebook | `episode_recodes/*.json` | 42 |
| 5 | Recodes grouped by theme | `theme_reports/*.md` | 12 |
| 6 | All theme reports | `cross_analysis.md` | 1 |
| 7 | Everything | `resources/*.md` | 7 |

Human review gates after Pass 0, 3, and 6.

## How a file moves through Pass 4

Pass 4 is where the harness does the most work. Each of the 42 episodes goes through:

```
manifest.csv + codebook.json
        ↓
   ta.py scaffold --pass 4           → scaffold-4 in manifest
        ↓
   skeleton JSON (deterministic fields filled: episode_date,
   episode_title, theme_id, theme_name for all 12 themes)
        ↓
   ta.py next --pass 4               → shows scaffold + staging paths
        ↓
   LLM writes reduced JSON to staging dir (only interpretive fields)
        ↓
   ta.py fill --pass 4               → fill-4 in manifest
        ↓  merges staging → scaffold
        ↓  validates sub-theme IDs against codebook
        ↓  rejects files with invalid IDs
        ↓
   ta.py validate --pass 4 --fix     → validate-4 in manifest
        ↓  chain enforcement: requires fill-4 with matching hash
        ↓  normalizers (alias correction, summary list rebuild)
        ↓  schema checks (required fields, enum values, no extra keys)
        ↓
   ta.py check-refs (sub-theme IDs exist in codebook?)
        ↓
   done — or banished if schema still fails after fixes
```

**Deterministic fields** (scaffold writes, LLM must not touch): `episode_date`, `episode_title`, `theme_id`, `theme_name`, `primary_themes`, `secondary_themes`, `tangential_themes`.

**LLM fields** (scaffold leaves empty, LLM fills): `relevance`, `sub_themes_present`, `best_quote.text`, `best_quote.speaker`, `summary`.

**Derived fields** (validate --fix rebuilds from LLM output): `primary_themes`, `secondary_themes`, `tangential_themes` — computed from `theme_codings[].relevance`.

## Completion tracking

`ta.py next` checks if `{slug}.json` exists in the output dir. File present = done. Content not inspected. This means a corrupt file blocks re-processing — it exists, so it's "done," but it fails validation.

The banish mechanism breaks the deadlock: `validate --fix` moves files that still fail after all deterministic fixes to `outputs/error_files/episode_recodes/`. The file is gone from the output dir, so `next` treats it as pending again.

## What the manifest tracks

`.pipeline-manifest.jsonl` records every operation with SHA-256 hashes. The enforced chain for Pass 4:

```
scaffold-4  →  fill-4  →  validate-4
```

`validate` requires a `fill-4` entry with matching SHA-256 for each file. Files without `fill-4` are rejected with chain errors — no bypass is possible.

Each entry: `step`, `file`, `sha256`, `parent` (previous hash), `ts`. Detects out-of-band edits and lets you trace any file's full history.

**Migration:** 34 pre-existing files had `fill-4` entries seeded via `scripts/seed_fill4_migration.py` with `"migration": true` for auditability.

## Failures encountered

### Null best_quote (7 files)

LLM left `best_quote` as `{"text": "", "speaker": ""}` for tangential themes — treating "tangential" as "no quote needed." Schema requires non-empty strings for every theme.

- **Caught by:** schema (`'best_quote' is a required property`)
- **Fixed by:** banish → re-scaffold → re-fill → validate clean

### Empty relevance (1 file)

`adrian-gill-ai-image-generation.json` had `relevance: ""` for T12. LLM wasn't sure how to rate it.

- **Caught by:** schema enum (`got '', expected one of ['primary', 'secondary', 'tangential']`)
- **Fixed by:** same banish cycle

### Hallucinated sub-theme IDs (8 files, 24 errors)

Re-fill agents invented T09.4, T10.4, T11.3, T11.4, T12.3. The codebook only has T09.1–T09.3, T10.1–T10.3, T11.1–T11.2, T12.1–T12.2. Agents assumed 4 sub-themes per theme.

- **Caught by:** `check-refs`
- **Fixed by:** script stripped invalid IDs
- **Prevention:** pass actual sub-theme IDs from codebook.json, not a summary

### Scaffold slug mismatch (42 files)

Original recodes used short editorial slugs (`nordic-summit-hard-truths`). `ta.py scaffold` generates manifest slugs (`fabian-heckenberg-naja-nielsen-gard-steiro-the-hard-truths-a`). After banishing 8 short-slug files, scaffold created 42 long-slug files — 34 duplicates plus 8 new skeletons.

- **Not caught by harness:** `_get_pending_documents` uses date-prefix matching, so both slug styles resolve as "done"
- **Fixed by:** manual cleanup (removed 34 duplicates, renamed 8 to match original short slugs)

### Summary list drift (ongoing, self-correcting)

LLM sometimes generates `primary_themes` / `secondary_themes` / `tangential_themes` instead of leaving them for `validate --fix`. The normalizer rebuilds them from `theme_codings[].relevance` every run.

## Recovery playbook

| Situation | What to run |
|-----------|-------------|
| Deterministic drift (titles, summary lists, aliases) | `validate --pass 4 --fix --check-scaffold --manifest outputs/manifest.csv --codebook outputs/codebook.json` |
| LLM content failures (null quotes, empty fields) | Same command banishes automatically, then `scaffold --pass 4` + LLM re-fill + `validate` |
| Bad sub-theme IDs across multiple files | Script to strip invalid refs, then `check-refs` |
| One-off issue in a single file | Edit directly, then `validate` |
| Codebook revision or corpus change | Delete pass output, re-scaffold, re-run all 42 |
