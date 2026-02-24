# Project Status: Data Pipeline Canon — What Endures in the LLM Era
_Last updated: 2026-02-23 (v8)_

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
| Get | 🔄 In progress | ~50 sources acquired; 8 expansion candidates acquired (#142–#144, #146–#150); #145 needs manual download; ~6 still being procured; sources folder reorganized |
| Verify | ⬜ Not started | |
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

## Current Step: GET

### Acquisition status (see source-registry.md for the authoritative per-item detail)

**The registry is the single source of truth.** Every entry's last column shows: file location if acquired, "PROCUREMENT IN PROGRESS" if being obtained, "NOT ACQUIRED" + reason if unavailable.

**Summary counts (as of 2026-02-23, v8):**
- **Acquired**: ~50 sources (PDFs, EPUBs, markdown, cloned repos). All organized in `sources/{lang}/` with standard naming.
- **Expansion search acquired**: #142–#144, #146–#150 (8 of 9 sources). #145 (Follow the Money) needs manual download from archive.org.
- **Procurement in progress**: #23 Data Storytelling Workbook
- **Not acquired — digital exists, can still procure**: #16 (Houston, Kindle ~$40), #25 (Tong, SAGE ebook)
- **Not acquired — paperback/physical only**: #17 (Vallance-Jones, OUP Canada), #43 (Felle, Abramis), #44 (LaFleur, IRE spiral-bound)
- **Excluded — wrong language**: #26 (Elmer/Matzat, German only)
- **Paywalled articles**: ~7 still need institutional access
- **Excluded (acquired but not in corpus)**: Apostles of Certainty, Nerd Journalism → `sources/_rejected/`

**Maybe items resolved (v7):**
- #133 Digital Technology and Journalism → **excluded** (theory/case studies)
- #134 Journalism in an Era of Big Data → **excluded** (theory-heavy)
- #137 The Watchdog Still Barks → **excluded** (impact analysis, no methods)
- #139 Best Practices for Data Journalism → **included** (practitioner workflow guide)

**New acquisitions since v6:**
- #24 Data + Journalism (Reilley/Sunne) — acquired
- #141 Nerd Journalism (Cairo) — acquired, excluded (viz history)

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
1. User manually downloads #145 (Follow the Money) from archive.org: https://web.archive.org/web/20200706122418/http://test.irrp.org.ua/wp-content/uploads/2017/11/Follow-The-Money.pdf → save as `sources/en/145-follow-the-money-occrp.pdf`
2. User finishes procuring #23 (Data Storytelling Workbook)
3. Optionally procure #16 (Houston, ~$40) and #25 (Tong, SAGE ebook)
4. User downloads remaining browser-blocked PDFs and paywalled articles
5. Once corpus sufficiently populated → T5 (convert to text) → T6 (verify representativeness)

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
