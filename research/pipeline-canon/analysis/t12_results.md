# T12 Analysis Results

_Generated 2026-02-25 by `t12_1_analyse_horizon.py`_

Deterministic cross-tabulations of `horizon-table.csv`. Raw numbers only — interpretation in `t13_report.md`.

## Corpus

- **Total extracts**: 4,351
- **Sources**: 71 (unique source IDs)
- **Unique themes**: 6,452

## Output CSVs

| File | Rows | Contents |
|------|------|----------|
| `step_distribution.csv` | 7 | Primary/secondary/combined counts per step |
| `type_x_relevance.csv` | 4 | Extract type x relevance cross-tab with row % |
| `step_x_relevance.csv` | 7 | Pipeline step x relevance cross-tab + redefinition % |
| `themes_by_step.csv` | 70 | Top 10 themes per step |
| `displaced_extracts.csv` | 46 | All displaced rows with full context |
| `source_coverage.csv` | 7 | Source count per step |

## Step Distribution (H1)

| Step | Primary | % | Secondary | Combined |
|------|---------|---|-----------|----------|
| Define | 483 | 11.1% | 62 | 545 |
| Find | 467 | 10.7% | 128 | 595 |
| Get | 634 | 14.6% | 138 | 772 |
| Verify | 698 | 16.0% | 375 | 1,073 |
| Clean | 243 | 5.6% | 112 | 355 |
| Analyse | 1,174 | 27.0% | 265 | 1,439 |
| Present | 652 | 15.0% | 224 | 876 |

Ratio max/min: 4.8:1 (Analyse/Clean)

## Extract Type Distribution

| Type | Count | % |
|------|-------|---|
| Procedural | 2,016 | 46.3% |
| Epistemological | 1,522 | 35.0% |
| Tool-specific | 416 | 9.6% |
| Organizational | 397 | 9.1% |

## Overall Relevance

| Relevance | Count | % |
|-----------|-------|---|
| Endures | 3,023 | 69.5% |
| Needs update | 1,282 | 29.5% |
| Displaced | 46 | 1.1% |

## Extract Type x Relevance (H2)

| Type | Total | Endures | Endures % | Needs update | Needs update % | Displaced | Displaced % |
|------|-------|---------|-----------|--------------|----------------|-----------|-------------|
| Epistemological | 1,522 | 1,360 | 89.4% | 161 | 10.6% | 1 | 0.1% |
| Procedural | 2,016 | 1,329 | 65.9% | 672 | 33.3% | 15 | 0.7% |
| Organizational | 397 | 290 | 73.0% | 107 | 27.0% | 0 | 0.0% |
| Tool-specific | 416 | 44 | 10.6% | 342 | 82.2% | 30 | 7.2% |

## Step x Relevance — Redefinition Candidates (H3)

| Step | Total | Redef count | Redef % | Flag |
|------|-------|-------------|---------|------|
| Define | 483 | 73 | 15.1% | |
| Find | 467 | 135 | 28.9% | |
| Get | 634 | 311 | 49.1% | REDEFINE |
| Verify | 698 | 114 | 16.3% | |
| Clean | 243 | 195 | 80.2% | REDEFINE |
| Analyse | 1,174 | 418 | 35.6% | REDEFINE |
| Present | 652 | 82 | 12.6% | |

Threshold: >30% needs_update + displaced

## Source Coverage per Step

| Step | Sources |
|------|---------|
| Define | 59 |
| Find | 48 |
| Get | 55 |
| Verify | 57 |
| Clean | 37 |
| Analyse | 66 |
| Present | 55 |

## Displaced Extracts by Category

| Category | Count | Examples |
|----------|-------|----------|
| Defunct tools | 18 | Google Fusion Tables, Kimono Labs, ScraperWiki, TileMill |
| Manual text preprocessing | 12 | Tokenization, stop-words, stemming, encoding fixes |
| Search operator syntax | 10 | Google AROUND(), site:, filetype:, min_retweets |
| Obsolete workflows | 6 | Selective transcription, manual PDF extraction |

Source concentration: Verification Handbook series = 16/46 (35%), NICAR tipsheets = 7/46 (15%)
