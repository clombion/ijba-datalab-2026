# Action Log — Pipeline Canon

> Append-only record of pipeline actions. Entries marked [reconstructed] were inferred from git history, plan files, and artifacts. Entries marked [live] are written by scripts during execution.

## 2026-02-17 — T1 DEFINE [reconstructed]
- Established research questions (RQ1: practitioner recommendations per pipeline step; RQ2: LLM-era displacement vs endurance)
- Confirmed hypotheses H1 (uneven coverage), H2 (procedural displaced, epistemological endures), H3 (some steps need redefinition)
- Defined scope: data journalism methodology, not OSINT/pure data science/tool manuals
- Set languages: EN, FR, ES, PT; temporal range: 2012+
- Designed horizon table schema (12 columns, unit = one advice extract)
- Built task map: T1–T13 with dependency flow
- Corpus selection protocol: systematic review (wide search → metadata screen → structure skim → document exclusions)
- Created master plan: `.claude/plans/dazzling-moseying-liskov.md`
- Key decision: all source types included (books, articles, guides, curricula, MOOCs, tipsheets)
- Key decision: academic articles included even SLRs/meta-research
- Git: `Initial commit: IJBA Datalab 2026 project` (2026-02-17 18:41)

## 2026-02-17 — Repo setup [reconstructed]
- Initial repo structure created
- Git: `Reorganize repo: nest research, add content folder, remove audit` (2026-02-17 19:03)

## 2026-02-18 — T2/T3 FIND: initial source registry [reconstructed]
- Built source registry with candidates from GIJN, NICAR, university syllabi, academic databases, publisher catalogues
- Applied inclusion/exclusion checklist to metadata
- Registry columns: title, author, year, language, type, access, found_via, status, included, exclusion_reason
- Output: `research/pipeline-canon/source-registry.md`
- Git: `Add full IJBA Data J archive (2017-2025), content outline, remove flat 2023-2024 refs` (2026-02-18 20:52)

## 2026-02-23 — T4/T5 GET + CONVERT: batch conversion [reconstructed]
- Batch source-to-markdown converter built and run
- Converted PDFs, EPUBs to markdown using markitdown/LibreOffice
- Stored converted files in `research/pipeline-canon/sources/{en,fr,es,pt}/`
- Git: `Add batch source-to-markdown converter, update registry to T4 CONVERT` (2026-02-23 22:18)

## 2026-02-24 — T2/T3 FIND: expansion search (v7) [reconstructed]
- Expansion search executed across three directions; 9 new candidates added (#142–#150) covering verification, investigative methods, data ethics
- Maybe items resolved: #133→excluded, #134→excluded, #137→excluded, #139→included
- User-discovered books resolved: Apostles of Certainty→excluded (theory), Nerd Journalism→excluded (viz history)
- Sources folder reorganized: root files → `en/`, NICAR stragglers → `en/nicar/`, excluded → `_rejected/`
- NICAR tipsheet IDs renumbered to 97a–97n to avoid conflicts
- Registry reached 160 entries (v7)
- Plan: `.claude/plans/zippy-stirring-hamster.md` (acquire 9 expansion candidates)
- Output: `research/pipeline-canon/search-results-raw.md`

## 2026-02-24 — T4 GET: expansion candidates acquired [reconstructed]
- Downloaded 9 new open-access sources (#142–#150): Verification Handbook 2+3, Exposing the Invisible, Al Jazeera Handbook, Responsible Data Handbook, UNESCO Reporting on AI, Algorithmic Accountability, Amnesty toolkit
- PDF downloads for 7 items, web-to-markdown for 2 items
- Registry updated: status changed from `screened` to `acquired`
- Git: `Add IJBA Data J exercise screenshots/slides, IRI curriculum, pipeline and SCoDA references` (2026-02-24 14:49)
- Git: `Add DDJ Handbook 2 scrape, pipeline-canon status/search docs, handbook scraper script` (2026-02-24 14:49)

## 2026-02-24 — T6 VERIFY: corpus profile [reconstructed]
- Ran `utils/corpus_profile.py` to assess corpus representativeness
- 71 deduplicated sources, 5.31M words, median 16.7K words/source
- Language: 92.5% EN, 8.5% FR/ES/PT (8 sources)
- Format: 34 PDFs, 9 EPUBs, 14 md-native; NICAR consolidated files = 39.8% of words
- Type: guides 41.6%, books 20.7%, handbooks 8.6%
- Decade: 2020s 59.1%, 2010s 15.4%, 25.5% unknown year
- Flagged: 8 thin sources (<1K words), 2 PDF word-count warnings, 15 included-but-not-converted gaps
- 35 new papers screened during verification
- Output: `research/pipeline-canon/corpus-profile.md`
- Git: `T6 VERIFY: corpus profile, registry updates, 35 new papers screened` (2026-02-24 17:59)

## 2026-02-25 — T8 CLEAN: corpus cleaning [reconstructed]
- Built `utils/clean_corpus.py` — deterministic regex-based cleaning
- Plan: `.claude/plans/velvety-frolicking-clock.md`
- Cleaning passes: page numbers, ISSN/DOI/copyright blocks, pandoc anchors/divs/spans, HTML tags, orphaned images, encoding artifacts
- Copied from `sources/{lang}/` to `corpus/`, originals untouched
- 7 sources excluded: #105 (portal stub), #106 (MOOC stub), #116 (course stub), #58 (TOC only), #45/#55/#57 (DDJ Handbook 1 FR/ES/PT — duplicates of #7 EN)
- Output: 81 cleaned .md files in `research/pipeline-canon/corpus/`

## 2026-02-25 — T8 CLEAN: translation [reconstructed]
- Built `utils/translate_corpus.py` (API-based, idempotent via `<!-- translated -->` marker)
- 15 non-EN sources translated to English (7 ES, 7 PT, 1 FR)
- Translations done directly via LLM, not via the script (script created but unused)
- Original 20 non-EN reduced to 15 after excluding 3 DDJ Handbook 1 translations + 2 stubs

## 2026-02-25 — T8 CLEAN: final corpus registry [reconstructed]
- Generated `corpus/corpus-registry.csv` via `clean_corpus.py --registry-only`
- 81 final sources, 5.14M words total (down from 5.54M pre-cleaning)
- CSV = single source of truth for T9+ (columns: id, file, title, author, year, lang, type, words, translated)
- Artifact: `research/pipeline-canon/corpus/corpus-registry.csv` (11KB, dated 2026-02-25 11:38)

## 2026-02-25 — T9/T10 EXTRACT planning [reconstructed]
- Designed harnessed multi-pass extraction pipeline (T9 Extract + T10 Relevance)
- Plan: `.claude/plans/keen-roaming-lollipop.md`
- Core design: LLM never produces JSON; outputs plain text values; CLI handles all schema enforcement
- Process: chunk → classify → annotate (context) → scaffold → Pass A (identify) → Pass B (classify) → validate → merge → Pass C (relevance) → merge horizon table
- 13 new scripts planned for `utils/`
- Action log format specified for [live] entries going forward
- Scaffolded empty directories: `extractions/`, `relevance/`

## 2026-02-25T13:29 — chunk_corpus.py [live]
- Chunked 81 sources into 124 chunks
- Strategy breakdown: 1 heading_h1, 7 heading_h2, 1 heading_h5, 3 nicar_filter, 58 single, 11 word_boundary

## 2026-02-25T13:29 — classify_chunks.py [live]
- 98 chunks context_ok, 26 chunks context_needed
- context_needed: 07-ddj-handbook-1_chunk1.md, 07-ddj-handbook-1_chunk2.md, 11-data-literacy_chunk1.md, 11-data-literacy_chunk2.md, 21-digital-investigative-journalism_chunk1.md, 21-digital-investigative-journalism_chunk2.md, 21-digital-investigative-journalism_chunk3.md, 23-data-storytelling-workbook_chunk1.md, 23-data-storytelling-workbook_chunk2.md, 37-art-science-data-driven-journalism_chunk1.md, 37-art-science-data-driven-journalism_chunk2.md, 52-big-data-periodismo_chunk1.md, 52-big-data-periodismo_chunk2.md, 61-elementos-transparencia_chunk1.md, 61-elementos-transparencia_chunk2.md, 82-periodismo-datos-big-data-thesis_chunk1.md, 82-periodismo-datos-big-data-thesis_chunk2.md, 82-periodismo-datos-big-data-thesis_chunk3.md, 127-modern-investigative-journalism-arij_chunk1.md, 127-modern-investigative-journalism-arij_chunk2.md, 132-digging-deeper_chunk1.md, 132-digging-deeper_chunk2.md, 132-digging-deeper_chunk3.md, 132-digging-deeper_chunk4.md, 149-unesco-reporting-on-ai_chunk1.md, 149-unesco-reporting-on-ai_chunk2.md

## 2026-02-25T13:29 — scaffold_extraction.py [live]
- Created 124 extraction scaffolds, skipped 0 existing

## 2026-02-25T13:34 — LLM Pass 0 (context annotation) [live]
- Annotated 26 context_needed chunks across 11 sources
- Sources: 07, 11, 21, 23, 37, 52, 61, 82, 127, 132, 149
- 4 parallel agents, all completed successfully

## 2026-02-25T14:18 — t9_5_add_extract.py [T9]
- Batches 1-2: 10/124 chunks extracted, 586 total extracts. 0 validation errors.

## 2026-02-25T14:32 — t9_5_add_extract.py [T9]
- Batch 3: 8 more chunks extracted (440 new), 18/124 total, 1026 extracts. 0 validation errors.

## 2026-02-25T14:41 — t9_5_add_extract.py [T9]
- Batch 4: 5 more chunks (152 new), 23/124 total, 1178 extracts. Sources complete: 10,11,13,21,23. 0 errors.

## 2026-02-25T14:48 — t9_5_add_extract.py [T9]
- Batch 5: 8 chunks (203 new), 31/124 total, 1381 extracts. New sources: 37,38,41,42,50,51,54,56. 0 errors.

## 2026-02-25T14:55 — t9_5_add_extract.py [T9]
- Batch 6: 15 chunks (215 new), 46/124 total, 1596 extracts. Sources complete: 22,37,38,42,50,51,54,56,63,66,67,69,71,72,73,74,76. 0 errors.

## 2026-02-25T15:58 — merge_chunks.py [live]
- Merged 81 sources, skipped 0 incomplete + 0 existing

## 2026-02-25T15:58 — scaffold_relevance.py [live]
- Created 81 relevance scaffolds, skipped 0 existing

## 2026-02-25T16:02 — t9_5_add_extract.py [live]
- NOTE: Future pipeline improvement — add code-block stripping pass to cleaning scripts (utils/clean/), not the chunker. Fenced code blocks and console output lines should be replaced with semantic placeholders before chunking. Would have prevented the 830K Wells chunk2 anomaly.

## 2026-02-25T17:37 — t10_2_score_extract.py [live]
- Scored all 90 extracts for 140-data-for-journalism-tong.json: 58 endures, 32 needs_update, 0 displaced

## 2026-02-25T17:37 — t10_2_score_extract.py [live]
- T10 scoring complete for 4 sources (43 extracts): 149-unesco-reporting-on-ai (13), 21-digital-investigative-journalism (12), 97g-nicar-2022 (10), 148-algorithmic-accountability-diakopoulos (8). All 4 files now fully scored. Zero nulls remain.

## 2026-02-25T17:38 — t10_2_score_extract.py [live]
- T10 COMPLETE: 146-aljazeera-investigative-handbook.json — 74/74 extracts scored (53 endures, 21 needs_update, 0 displaced)

## 2026-02-25T17:39 — merge_horizon.py [live]
- Merged 4351 extracts from 81 sources into horizon-table.csv

## 2026-02-25T17:40 — t10_2_score_extract.py [live]
- T10 COMPLETE: 22-ddj-handbook-2.json — 165/165 extracts scored (127 endures, 38 needs_update, 0 displaced)

## 2026-02-25T17:41 — t10_2_score_extract.py [live]
- Scored 260 extracts across 3 sources: 24-data-plus-journalism (106), 97i-nicar-2024 (80), 82-periodismo-datos-big-data-thesis (74). All 3 files now 100% scored. Distribution: file1=95e/29u/1d, file2=54e/55u/1d, file3=90e/24u/0d.

## 2026-02-25T17:47 — t10_2_score_extract [live]
- T10 COMPLETE: 4,351/4,351 extracts scored. Distribution: endures 3,023 (69.5%), needs_update 1,282 (29.5%), displaced 46 (1.1%). Validation PASS (0 errors, 5 warnings). Scoring via LLM agents + deterministic batch for stubborn sources.

## 2026-02-25T17:47 — t11_1_merge_horizon [live]
- T11 COMPLETE: horizon-table.csv produced with 4,351 rows, 14 columns. All 81 sources merged from extractions + relevance JSONs.

## 2026-02-25T17:47 — t8_clean_corpus [live]
- Added pass4_strip_code_blocks to cleaning pipeline. Strips fenced code blocks and long indented code blocks, replaces with [CODE BLOCK REMOVED] placeholder. Ready for future re-cleans.
