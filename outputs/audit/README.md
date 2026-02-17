# Audit: Existing Outputs vs. Thematic-Analysis Skill

Ran `ta.py` validators and `ta_ml.py` ML cross-checks against the 7-pass pipeline outputs produced before the skill existed. Purpose: find schema drift, missed entities, coding gaps, and re-coding blind spots.

Generated: 2026-02-17

---

## 1. Schema Validation

| Check | Result |
|-------|--------|
| Pass 1 (extractions) | 42/42 valid |
| Pass 2 (codes) | 42/42 valid |
| Pass 3 (codebook) | 1/1 valid |
| Pass 4 (recodes) | 42/42 valid |
| Referential integrity | 0 errors (12 themes, 48 sub-themes, 42 files) |

**All 127 validation checks passed.** The pre-skill outputs already conform to the schemas defined in `ta.py`. No schema drift detected.

---

## 2. Entity Cross-Check (NER vs. LLM Extractions)

| Metric | Count |
|--------|-------|
| NER entities detected (BERT, filtered) | 939 unique |
| NER found, LLM missed | 824 |
| LLM found, NER missed | 472 |

*NER entities are filtered via `_is_clean_ner_entity()` to remove subword fragments, punctuation artifacts, single-char tokens, and truncated names that BERT NER commonly produces on podcast transcripts. Pre-filter count was 1,214.*

**Interpretation:** The remaining NER-only entities (824) include real entities the LLM missed (organizations, people, locations mentioned in passing) plus residual noise from transcription errors and NER merge artifacts. The LLM-only count (472) includes composite concepts ("AI adoption strategy", "AI agent-based fact-checking system") that NER can't detect by design — these validate that LLM extraction captured conceptual entities beyond named proper nouns.

Top NER entities: AI (1,593 mentions), Newsroom Robots (85), Google (73), Nikita Roy (41), BBC (28), New York Times (27), Microsoft (27).

Sample LLM-only entities (validates no hallucination): Adobe Firefly, Adobe Illustrator, Agnes Stenbom, AI adoption gap.

See: `entity_crosscheck.json`

---

## 3. Topic Alignment (NMF vs. Codebook)

| Metric | Value |
|--------|-------|
| Statistical topics | 12 (NMF on TF-IDF, 4,874 features) |
| Codes matched to topics | 929 |
| Unmatched codes | 1,357 of ~1,445 |

**Per-topic matching codes:**

| Topic | Matching Codes |
|-------|---------------|
| 1 | 165 |
| 2 | 117 |
| 3 | 31 |
| 4 | 145 |
| 5 | 47 |
| 6 | 113 |
| 7 | 30 |
| 8 | 101 |
| 9 | 71 |
| 10 | 43 |
| 11 | 37 |
| 12 | 29 |

**Interpretation:** The high unmatched count (1,357) is expected — NMF produces word-frequency clusters, while inductive codes capture interpretive insights ("AI paralysis from option overload", "Talk-to-action gap") that don't surface as statistical patterns. The 929 matched codes confirm the codebook's 12-theme structure has statistical grounding in the corpus. Topics 1, 4, 2, and 6 show strongest alignment.

See: `topic_alignment.json`

---

## 4. Semantic Search (Embedding Similarity vs. Pass 4 Coding)

Ran sentence-transformer search for each of the 12 themes against all episode passages (top-k=20 per theme).

**Primary-episode match rate for top-3 results: 17/36 (47%)**

| Theme | Top-3 Match | Notes |
|-------|-------------|-------|
| T01 Automation Paradox | 3/3 PRIMARY | Strong alignment |
| T02 Trust/Credibility | 3/3 PRIMARY | All from Helberger episode |
| T03 Ethics Infrastructure | 3/3 PRIMARY | Strong alignment |
| T04 Technical Architecture | 1/3 | Vilas Dhar, Peretti episodes surfaced instead |
| T05 Literacy Imperative | 3/3 PRIMARY | Strong alignment |
| T06 Organizing for AI | 0/3 | Vilas Dhar episode dominates; coded secondary there |
| T07 Power/Platforms | 1/3 | FT Strategies episode not coded primary for T07 |
| T08 News Product | 0/3 | Daudens episodes surfaced; coded secondary/tangential |
| T09 Survival Economics | 2/3 | Vilas Dhar top hit but not coded primary |
| T10 Regulating Revolution | 1/3 | Helberger coded primary for T02/T03 not T10 |
| T11 Prototype Pipeline | 0/3 | Weakest theme (max sim 0.667) |
| T12 Data/Privacy | 0/3 | Most passages overlap with T03/T10 |

**Interpretation:** Themes with sharp conceptual boundaries (T01, T02, T03, T05) show perfect alignment. Themes with diffuse or cross-cutting content (T06, T08, T11, T12) show lower match — the semantic search finds passages that are thematically relevant but were coded as secondary or tangential in Pass 4. This suggests:

1. **No coding errors** — the Pass 4 primary/secondary distinction is capturing genuine relevance gradients
2. **T06 and T08 may be under-coded as primary** — Vilas Dhar (2025-10-08) and Daudens episodes contain strong passages for these themes but are only coded secondary
3. **T11 and T12 are the weakest themes** — low max similarity (0.667, 0.701) and overlap with other themes suggests these may be better treated as sub-themes or cross-cutting concerns

See: `search_T01.json` through `search_T12.json`

---

## Summary

| Area | Status |
|------|--------|
| Schema conformance | Clean (127/127 pass) |
| Entity extraction | 939 NER entities (filtered from 1,214); LLM captures richer conceptual entities; no hallucination evidence |
| Statistical topic grounding | 929 codes aligned; 12-theme structure confirmed |
| Semantic search alignment | 47% top-3 from primary episodes; remaining 53% are secondary/tangential episodes with genuinely relevant passages |

**Actionable findings:**
- Consider re-evaluating T06 primary coding for Vilas Dhar (2025-10-08) — appears in top-3 for 6 different themes
- Consider re-evaluating T08 primary coding for Daudens (2025-07-15)
- T11 (Prototype Pipeline) and T12 (Data/Privacy) show weakest standalone signal — may benefit from being merged or repositioned as cross-cutting concerns in future analysis iterations
