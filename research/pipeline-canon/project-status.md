# Project Status: Data Pipeline Canon — What Endures in the LLM Era
_Last updated: 2026-02-24 (v9)_

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
| Clean | ⬜ Not started | Includes translation task for FR/ES/PT sources |
| Analyse | ⬜ Not started | |
| Present | ⬜ Not started | |

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

## Current Step: VERIFY (T6) → CLEAN (T8)

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
1. **Decision**: proceed to T8/T9 with current corpus, or go back to GET for remaining gaps?
2. If proceeding: T8 (Clean + translate FR/ES/PT) → T9 (LLM extraction)
3. Optional: procure remaining gaps (#16 Houston ~$40, #25 Tong, paywalled articles)

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
- DDJ Handbook 2 (already in repo): `research/ddj-handbook-2/`
