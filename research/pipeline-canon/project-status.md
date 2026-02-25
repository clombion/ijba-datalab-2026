# Project Status: Data Pipeline Canon — What Endures in the LLM Era
_Last updated: 2026-02-25 (v13 — T13 PRESENT complete)_

## Research Questions
- **RQ1**: What do data journalism practitioners and educators recommend at each stage of the data pipeline?
- **RQ2**: Which of those recommendations have been displaced or substantially changed by LLMs, and which endure?

## Hypotheses
- **H1**: Coverage is uneven across pipeline steps
- **H2**: Procedural advice displaced most; epistemological advice endures
- **H3**: Some steps need redefinition, not just new tools

## Pipeline Progress
| Step | Status | Notes |
|------|--------|-------|
| Define | ✅ Complete | RQs, hypotheses, task map, horizon table, scope, corpus selection protocol |
| Find | ✅ Complete | 160 entries (v7); expansion search added 9 new candidates in verification, investigative methods, data ethics |
| Get | ✅ Complete | ~90 acquired; 75 converted outputs; 15 included-not-acquired (purchase barrier or paywalled) |
| Verify | ✅ Complete | T6 corpus profile: 71 sources, 5.31M words, 4 languages. 8 thin sources (<1K words), 2 conversion warnings, 15 gaps. See `corpus-profile.md` |
| Clean | ✅ Complete | T8: 81 sources, 5.14M words. 7 excluded (4 stubs + 3 DDJ Handbook 1 translations). 15 non-EN sources translated to EN. See `corpus/corpus-registry.csv` |
| Analyse | ✅ Complete | T9 extraction (4,351 extracts). T10 relevance. T11 merge. T12 analysis: 6 CSVs + results summary. H1/H2/H3 all confirmed. |
| Present | ✅ Complete | T13 report: research-paper-format literature review. Curriculum conclusions in `content/theory.md`. |

## Scope & Criteria
- **In scope**: Methodological practice of working with data in journalism
- **Out of scope**: OSINT, pure data science, tool-specific manuals
- **Languages**: EN, FR, ES, PT
- **Temporal**: 2012+ (aligned with School of Data pipeline creation)
- **Corpus selection**: Systematic review protocol — wide search → metadata screen (inclusion/exclusion checklist) → structure skim → document exclusions

## Horizon Table Schema
**Unit of analysis**: One extract (passage containing advice mapped to a pipeline step)

| Column | Type | Answers |
|--------|------|---------|
| extract | text | RQ1, RQ2 |
| pipeline_step | enum (7 steps) | RQ1, H1 |
| secondary_step | enum (nullable) | RQ1 |
| source_title | string | RQ1 |
| author | string | RQ1 |
| year | int | RQ1 |
| chapter | string | RQ1 |
| page | string (nullable) | RQ1 |
| extract_type | enum: procedural, epistemological, organizational, tool-specific | H2 |
| themes | list[string] | RQ1, H2 |
| llm_relevance | enum: endures, displaced, needs_update | RQ2, H2, H3 |
| notes | text (nullable) | — |

## Current Step: COMPLETE

### T13 Present (2026-02-25)

Research-paper-format literature review synthesizing all pipeline canon findings. Curriculum conclusions integrated into `content/theory.md` (section 4: "Evidence from the Pipeline Canon").

Outputs:
- `research/pipeline-canon/analysis/t13_report.md` — full report (Overview, Introduction, Results, Methodology, Limitations, Conclusions)
- `content/theory.md` section 4 — actionable curriculum implications

### T12 Analyse (2026-02-25)

Deterministic cross-tabulation of horizon-table.csv. Key findings:

- **H1 confirmed**: Analyse 27.0% vs Clean 5.6% — coverage is uneven (4.8:1 ratio)
- **H2 confirmed**: Epistemological 89.4% endures vs tool-specific 10.6% endures — abstract principles survive, tool advice does not
- **H3 confirmed**: Three redefinition candidates — Clean (80.2%), Get (49.1%), Analyse (35.6%)
- **Overall**: 69.5% endures, 29.5% needs_update, 1.1% displaced (46 extracts)
- **46 displaced extracts**: defunct tools (18), manual text preprocessing (12), search operator syntax (10), obsolete workflows (6)
- **6,452 unique themes** across 4,351 extracts; Verify > Analyse > Present for thematic density

Outputs:
- `research/pipeline-canon/analysis/` — 6 CSVs (step_distribution, type_x_relevance, step_x_relevance, themes_by_step, displaced_extracts, source_coverage)
- `research/pipeline-canon/analysis/t12_results.md` — dry results summary
- Script: `utils/analyse/t12_1_analyse_horizon.py`

### T10 Relevance + T11 Merge (2026-02-25)

T10 relevance scoring and T11 horizon table merge completed.

- **4,351 extracts** scored across 81 sources
- **Distribution**: endures 3,023 (69.5%), needs_update 1,282 (29.5%), displaced 46 (1.1%)
- **Validation**: PASS (0 errors, 5 warnings — all >90% endures on short principled sources)
- **Output**: `research/pipeline-canon/horizon-table.csv` (14 columns, 4,351 rows)
- Scoring via `utils/analyse/t10_2_score_extract.py` + LLM agents + deterministic batch scoring
- Code-block stripping pass added to `utils/clean/t8_clean_corpus.py` (pass4) for future re-cleans

### T9 Extract (2026-02-25)

LLM extraction against horizon table schema. Key outcomes:
- **81 sources** → 124 chunks → 4,347 extracts (merged to 81 per-source JSONs)
- **0 validation errors** via `utils/analyse/t9_6_validate_extraction.py`
- Scripts: chunk → classify → annotate → scaffold → extract → validate → merge

### T8 Clean + Translate (2026-02-25)

Corpus cleaned and translated via `utils/clean_corpus.py` + direct LLM translation. Key outcomes:
- **81 final sources** in `corpus/corpus-registry.csv` (single source of truth for T9+)
- **5.14M words** total (down from 5.54M: cleaning removed ~1-5% artifacts per file)
- **15 non-EN sources** translated to English (10 ES, 4 PT, 1 FR → excluded; remaining: 7 ES, 7 PT, 1 FR translated)
- **7 excluded**: #105 (portal stub), #106 (MOOC stub), #116 (course stub), #58 (TOC only), #45/#55/#57 (DDJ Handbook 1 FR/ES/PT — duplicate of #7 EN)
- **Cleaning passes**: page numbers, ISSN/DOI/copyright blocks, pandoc anchors/divs/spans, HTML tags, orphaned images, encoding artifacts
- **Originals untouched** in `sources/`; cleaned files in `corpus/`

Scripts: `utils/clean_corpus.py` (deterministic), `utils/translate_corpus.py` (API-based, unused — translations done directly)

### T6 Corpus Profile (2026-02-24)

Corpus profile generated via `utils/corpus_profile.py`. Key findings:
- **71 deduplicated sources**, 5.31M words (median 16.7K/source)
- **Language**: EN-dominant (92.5%). FR/ES/PT present but thin (8 sources total, 8.5% of corpus)
- **Format**: NICAR consolidated files dominate (39.8% of words). 34 PDFs, 9 EPUBs, 14 md-native
- **Type**: guides (41.6%), books (20.7%), handbooks (8.6%). 2 "unknown" type sources need registry mapping
- **Decade**: 2020s (59.1%), 2010s (15.4%), 22 sources with unknown year (25.5% of words)
- **Thin sources**: 8 under 1K words (portal pages, stubs, TOC-only entries)
- **Gaps**: 15 included-but-not-converted (purchase barriers + paywalled articles)
- **Warnings**: 2 PDF word-count deltas >10% (#146 Al Jazeera, #54 Guía Buenas Prácticas)

Full report: `research/pipeline-canon/corpus-profile.md`

### Previous: GET phase

See source-registry.md for authoritative per-item detail. ~90 acquired, 75 converted, 15 gaps.

## Key Decisions Made
- RQs: two research questions confirmed (session 1)
- Hypotheses: H1-H3 confirmed (session 1)
- Scope: data journalism methodology, not OSINT/general data science (session 1)
- Languages: EN/FR/ES/PT (session 1)
- Corpus selection: systematic review with inclusion/exclusion checklist, human-driven, no LLM scoring (session 1)
- Temporal: 2012+ only, aligned with ScoDA pipeline creation (session 1)
- Academic articles included: even SLRs/meta-research, because they highlight what DJ practices focus on (session 1)
- All sources included regardless of format (books, articles, guides, curricula, MOOCs, tipsheets) (session 1)

## Task Map
```
T1 (Define) → T2+T3 (Find) → T4 (Get, manual) → T5 (Convert) → T6 (Verify) → T8 (Clean+translate) → T9 (Extract) → T11 (Merge) → T12 (Analyse) → T13 (Present)
                                                                    └→ T7 (Tag) ─┘    └→ T10 (Relevance) ─┘
```

## Next Actions
1. Optional: procure remaining gaps (#16 Houston ~$40, #25 Tong, paywalled articles)

## Completed: Research Expansion (v7)

**Expansion search executed 2026-02-23.** Three directions searched, 9 candidates added to registry (#142–#150). See `search-results-raw.md` for full results including MAYBE candidates.

**Maybe items resolved:** #133→excluded, #134→excluded, #137→excluded, #139→included.

**User-discovered books resolved:** Apostles of Certainty→excluded (theory), Nerd Journalism→excluded (viz history). Both in `_rejected/`.

**Sources folder reorganized:** All root-level files moved to `en/` with standard naming. NICAR stragglers moved to `en/nicar/`. Excluded items in `_rejected/`. NICAR tipsheet IDs renumbered to 97a-97n to avoid conflicts.

### Books still procurable (digital exists)
- #16 Data for Journalists (Houston) — Kindle/ePub, ~$40-50 via Routledge
- #25 Journalism in the Data Age (Tong) — SAGE ebook, Google Play
- #23 Data Storytelling Workbook (Feigenbaum) — Kindle/ePub, ~$37

## Files
- Plan: `.claude/plans/dazzling-moseying-liskov.md`
- Source registry: `research/pipeline-canon/source-registry.md`
- Raw search results: `research/pipeline-canon/search-results-raw.md`
- Downloaded sources: `research/pipeline-canon/sources/{en,fr,es,pt}/`
- Cleaned corpus: `research/pipeline-canon/corpus/` (81 .md files + corpus-registry.csv)
- Extractions: `research/pipeline-canon/extractions/` (81 per-source JSONs, 4,351 extracts)
- Relevance scores: `research/pipeline-canon/relevance/` (81 per-source JSONs with llm_relevance)
- Horizon table: `research/pipeline-canon/horizon-table.csv` (final merged output, 4,351 rows)
- Analysis: `research/pipeline-canon/analysis/` (6 CSVs + t12_results.md + t13_report.md)
- DDJ Handbook 2 (already in repo): `research/ddj-handbook-2/`
