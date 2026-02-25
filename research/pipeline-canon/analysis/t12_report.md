# Horizon Table Analysis Report

_Generated 2026-02-25 by `t12_1_analyse_horizon.py` + LLM narrative synthesis_

## Overview

This report analyses the horizon table produced in T11: **4,351 extracts** drawn from **81 sources** (71 unique source IDs after deduplication) spanning 2012-2025. Each extract is a passage of practitioner or educator advice mapped to one of seven School of Data pipeline steps, classified by extract type (epistemological, procedural, organizational, tool-specific), and scored for LLM-era relevance (endures, needs_update, displaced).

The corpus includes textbooks, handbooks, NICAR tipsheets, academic articles, and curriculum guides across four languages (EN/FR/ES/PT, all translated to English for analysis). The horizon table schema was designed to answer two research questions and test three hypotheses about what endures in the data journalism pipeline when LLMs arrive.

**Methodology note**: Extraction (T9) and relevance scoring (T10) were performed by LLM agents against a structured schema, then validated deterministically. The analysis below is purely deterministic cross-tabulation of the scored data.

---

## RQ1: What do practitioners recommend at each stage?

### Step coverage distribution (H1 test)

Coverage across the seven pipeline steps is markedly uneven:

| Step | Extracts | % | Sources |
|------|----------|---|---------|
| Define | 483 | 11.1% | 59 |
| Find | 467 | 10.7% | 48 |
| Get | 634 | 14.6% | 55 |
| Verify | 698 | 16.0% | 57 |
| Clean | 243 | 5.6% | 37 |
| Analyse | 1,174 | 27.0% | 66 |
| Present | 652 | 15.0% | 55 |

**Analyse dominates** with 27.0% of all extracts (1,174) — nearly five times the share of Clean (5.6%, 243). The literature overwhelmingly focuses on what to do with data once you have it, while the preparatory work of cleaning receives the least attention.

When secondary step assignments are included (extracts tagged with a secondary pipeline step), the picture sharpens further: Verify rises to 1,073 combined mentions and Analyse to 1,439 — many extracts about other steps also touch on verification and analysis concerns.

**H1 verdict**: Coverage is uneven. **Confirmed.**

### Extract type mix per step

The corpus contains four extract types:

| Type | Count | % |
|------|-------|---|
| Procedural | 2,016 | 46.3% |
| Epistemological | 1,522 | 35.0% |
| Tool-specific | 416 | 9.6% |
| Organizational | 397 | 9.1% |

Nearly half of all practitioner advice is procedural (how-to), and over a third is epistemological (why it matters). Tool-specific advice and organizational guidance each comprise roughly a tenth of the corpus.

### Theme clusters per step

Each pipeline step has a distinctive thematic signature (top 3 themes shown):

- **Define**: collaboration (38), project management (22), hypothesis (18) — emphasising team coordination and research design
- **Find**: public records (29), data discovery (18), FOI (17) — the civic infrastructure of data acquisition
- **Get**: FOI (66), web scraping (46), data acquisition (43) — legal and technical mechanisms for obtaining data
- **Verify**: verification (189), data quality (77), fact-checking (41) — overwhelmingly dominated by verification itself
- **Clean**: data cleaning (68), OpenRefine (23), data quality (15) — tool-oriented and quality-focused
- **Analyse**: reproducibility (56), VisiData (44), collaboration (39) — emphasis on repeatable methods
- **Present**: transparency (96), visualization (38), storytelling (37) — communicating findings responsibly

Notable: **Verification** (189 mentions) is the single most common theme in any step, reflecting the literature's deep concern with trust and accuracy. **FOI** dominates both Find and Get, underlining the legal backbone of data journalism. **Transparency** leads Present, suggesting the field views presentation as an accountability act, not just storytelling.

### Source diversity

All seven steps draw from at least 37 sources, with Analyse (66 sources) and Define (59) having the broadest coverage. Clean has the narrowest source base (37 sources), consistent with its low extract count — fewer authors write about data cleaning in depth.

---

## RQ2: Which recommendations endure vs are displaced?

### Overall relevance distribution

| Relevance | Count | % |
|-----------|-------|---|
| Endures | 3,023 | 69.5% |
| Needs update | 1,282 | 29.5% |
| Displaced | 46 | 1.1% |

Nearly 70% of the canonical advice endures — the core of data journalism methodology survives the LLM transition. About 30% needs updating (the advice is still directionally valid but the methods or tools need revision). Only 1.1% is genuinely displaced — advice that is no longer useful because LLMs have made the underlying task trivial or the referenced tools defunct.

### H2 test: extract type x relevance

| Type | Endures | Needs update | Displaced |
|------|---------|--------------|-----------|
| Epistemological | 89.4% | 10.6% | 0.1% |
| Organizational | 73.0% | 27.0% | 0.0% |
| Procedural | 65.9% | 33.3% | 0.7% |
| Tool-specific | 10.6% | 82.2% | 7.2% |

The gradient is steep and clean:

- **Epistemological advice** is nearly indestructible: 89.4% endures, and only 1 extract out of 1,522 is displaced. Principles about why data matters, how to think critically, and what journalism owes its audience are independent of tooling.
- **Organizational advice** also persists strongly (73.0% endures) — how to structure teams, manage projects, and build data culture in newsrooms remains relevant.
- **Procedural advice** shows significant update needs: a third (33.3%) requires revision. The how-to steps still point in the right direction, but the specific methods often need rewriting for LLM-era workflows.
- **Tool-specific advice** is overwhelmingly outdated: 82.2% needs updating and 7.2% is outright displaced. Only 10.6% of tool-specific advice endures — the small fraction that references tools still in active use (e.g., Python, SQL).

**H2 verdict**: Procedural advice is more likely to be displaced than epistemological advice. **Confirmed** — and the effect is stronger than hypothesised. Tool-specific advice, a subcategory not in the original hypothesis, is the most vulnerable of all.

### H3 test: redefinition candidates

Steps where >30% of extracts are needs_update or displaced qualify as "redefinition candidates" — steps where the field needs not just new tools but reconceptualization of the work.

| Step | Total | Redef % | Flag |
|------|-------|---------|------|
| Clean | 243 | 80.2% | REDEFINE |
| Get | 634 | 49.1% | REDEFINE |
| Analyse | 1,174 | 35.6% | REDEFINE |
| Find | 467 | 28.9% | |
| Verify | 698 | 16.3% | |
| Define | 483 | 15.1% | |
| Present | 652 | 12.6% | |

Three steps cross the 30% threshold:

1. **Clean (80.2%)** — The most disrupted step. Four out of five cleaning extracts need revision. Manual text preprocessing (tokenization, stop-word removal, encoding fixes, regex-based cleaning) is the single most displaced category of advice in the entire corpus. LLMs handle raw, messy text natively, making much of the traditional clean-before-analyse pipeline unnecessary.

2. **Get (49.1%)** — Nearly half of data acquisition advice needs updating. Specific scraping tools (Kimono Labs, ScraperWiki), manual transcription techniques, and environment configuration barriers are all displaced or dated. FOI and legal access principles endure, but the technical mechanisms of obtaining data are transforming.

3. **Analyse (35.6%)** — The largest step by volume also has significant update needs. Traditional NLP pipelines (TFIDF, word vectors, manual clustering), specific tool stacks (Google Fusion Tables, CartoDB), and formula-driven approaches need revision. The analytical principles endure but the methods are shifting.

**H3 verdict**: Clean, Get, and Analyse are redefinition candidates. **Confirmed** — with Clean showing far more disruption than initially expected (80.2% vs the hypothesised >30% threshold).

### The 46 displaced extracts: what was lost

The 46 displaced extracts cluster into clear categories:

1. **Defunct tools** (18 extracts): Google Fusion Tables, Kimono Labs, ScraperWiki, TileMill, namechk — tools that no longer exist or function. These are historically interesting but practically useless.

2. **Manual text preprocessing** (12 extracts): Tokenization, stop-word removal, stemming, sentence segmentation, encoding fixes, whitespace normalization. LLMs process raw text directly, making this preprocessing layer largely unnecessary.

3. **Search operator syntax** (10 extracts): Google AROUND(), site:, filetype:, OR operators, min_retweets filters. LLM-powered search agents handle these queries conversationally without requiring syntax knowledge.

4. **Obsolete workflows** (6 extracts): Selective interview transcription (LLMs transcribe full interviews cheaply), manual data entry templates (LLM-assisted validation), and manual PDF extraction (LLMs handle natively).

**Source concentration**: The Verification Handbook series (sources #138, #142, #143) accounts for 16 of 46 displaced extracts (35%), largely due to their detailed Google search operator tutorials. The NICAR tipsheets (#97) contribute 7 displaced extracts, mostly NLP preprocessing recipes.

### Needs_update patterns: what needs rewriting

The 1,282 needs_update extracts (29.5% of corpus) are not displaced — the underlying advice is still directionally correct — but the specific methods require revision. Common patterns:

- **Tool substitution**: Advice referencing Excel, OpenRefine, or Tableau that could now be augmented or replaced by LLM-assisted workflows
- **Procedural simplification**: Multi-step manual processes (e.g., data profiling, format conversion, basic analysis) that LLMs can now perform in a single prompt
- **Skill reframing**: Advice about learning specific programming syntax or tool interfaces that shifts toward learning how to prompt and validate LLM outputs

The key insight: needs_update advice is still *teaching the right thing* — you still need to clean data, verify sources, and analyse patterns — but the *how* has changed.

---

## Hypothesis Verdicts

### H1: Coverage is uneven across pipeline steps
**CONFIRMED.** Analyse commands 27.0% of extracts while Clean receives only 5.6% — a 4.8:1 ratio. The literature's emphasis on analysis over data preparation reflects a longstanding bias in data journalism education that predates LLMs.

### H2: Procedural advice displaced most; epistemological advice endures
**CONFIRMED.** Epistemological advice endures at 89.4% vs procedural at 65.9% (displaced+needs_update: 10.6% vs 34.0%). The effect is even stronger for the tool-specific subcategory (89.4% needs_update or displaced). The abstract principles of data journalism — skepticism, transparency, verification, evidence-based reasoning — are technology-independent. The specific methods are not.

### H3: Some steps need redefinition, not just new tools
**CONFIRMED.** Three steps exceed the 30% redefinition threshold: Clean (80.2%), Get (49.1%), Analyse (35.6%). Clean in particular requires fundamental reconceptualization — the entire preprocessing-before-analysis paradigm is disrupted when LLMs can work with raw, messy data directly. Get and Analyse need significant methodological updates but retain their core logic.

---

## Limitations

1. **LLM-scored relevance**: The endures/needs_update/displaced labels were assigned by LLM agents (T10), not human coders. While validated against deterministic checks and human-reviewed samples, systematic bias toward "endures" is possible — LLMs may underestimate their own disruptive potential.

2. **English-language bias**: While 15 non-English sources were translated, the corpus is 85%+ originally English, weighted toward US/UK data journalism traditions. Practices specific to non-English-language contexts may be underrepresented.

3. **Temporal snapshot**: Relevance was scored in February 2026. The LLM landscape is evolving rapidly; advice scored as "endures" today may shift as capabilities expand.

4. **Source selection**: The corpus of 81 sources, while systematic, is not exhaustive. Practitioner knowledge shared informally (Slack communities, conference hallways, newsroom mentoring) is absent.

5. **Extract granularity**: The unit of analysis is a passage, not a complete argument. Some nuanced positions may be split across multiple extracts or lose context when isolated from surrounding text.

6. **Clean step underrepresentation**: Clean's low extract count (243, 5.6%) means its high redefinition rate (80.2%) is based on a smaller sample than other steps. However, the pattern is consistent and the displaced extracts are qualitatively coherent.
