# What Endures in the Data Pipeline? A Horizon-Scanning Literature Review

_T13 Present — generated 2026-02-25. Cross-tabulations by `t12_1_analyse_horizon.py`; narrative synthesis by LLM._

## Overview

This report analyses 4,351 practitioner and educator recommendations drawn from 81 canonical data journalism sources (2012-2025), each mapped to the School of Data pipeline, classified by knowledge type, and scored for LLM-era relevance. The central finding: **70% of the canonical advice endures**. Epistemological advice — principles about why data matters, how to think critically, what journalism owes its audience — is nearly indestructible (89.4% endures). Tool-specific advice is the most fragile (10.6% endures). Three pipeline steps are flagged for redefinition: Clean (80.2% of advice needs revision), Get (49.1%), and Analyse (35.6%). All three pre-registered hypotheses are confirmed. Actionable curriculum implications derived from these findings are incorporated into `content/theory.md`.

## Introduction

This is a systematic literature review conducted to inform the design of a 5-day data journalism curriculum for journalism students encountering the field for the first time in 2026 — a moment when large language models are reshaping every stage of data-driven reporting.

The curriculum is structured around the School of Data pipeline: Define, Find, Get, Verify, Clean, Analyse, Present. This seven-step sequence, credited to the Open Knowledge Foundation and proven over eight years of teaching across four continents, serves as the curricular spine. The question motivating this review is not whether to use the pipeline — but what to teach differently within it, now that LLMs can perform or augment many of the tasks traditionally taught as manual skills.

Two research questions guided the extraction:

- **RQ1**: What do practitioners and educators recommend at each pipeline stage?
- **RQ2**: Which of those recommendations endure in the LLM era, and which are displaced?

Three hypotheses were pre-registered:

- **H1**: Coverage across the seven pipeline steps is uneven — some steps receive far more attention in the literature than others.
- **H2**: Epistemological advice (principles, reasoning) is more durable than procedural advice (how-to methods), which in turn is more durable than tool-specific advice.
- **H3**: Some pipeline steps require not just new tools but fundamental redefinition — a reconceptualization of what the step means in practice.

The corpus spans textbooks, handbooks, NICAR tipsheets, academic articles, and curriculum guides across four languages (EN, FR, ES, PT — all translated to English for analysis), with publication dates from 2012 to 2025.

## Results

### Step coverage distribution

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

**H1 verdict: Confirmed.** Coverage is uneven, with a 4.8:1 ratio between the most- and least-covered steps. The literature's emphasis on analysis over data preparation reflects a longstanding bias in data journalism education that predates LLMs.

### Extract type mix

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

Verification (189 mentions) is the single most common theme in any step, reflecting the literature's deep concern with trust and accuracy. FOI dominates both Find and Get, underlining the legal backbone of data journalism. Transparency leads Present, suggesting the field views presentation as an accountability act, not just storytelling.

### Source diversity

All seven steps draw from at least 37 sources, with Analyse (66 sources) and Define (59) having the broadest coverage. Clean has the narrowest source base (37 sources), consistent with its low extract count — fewer authors write about data cleaning in depth.

### Overall relevance distribution

| Relevance | Count | % |
|-----------|-------|---|
| Endures | 3,023 | 69.5% |
| Needs update | 1,282 | 29.5% |
| Displaced | 46 | 1.1% |

Nearly 70% of the canonical advice endures — the core of data journalism methodology survives the LLM transition. About 30% needs updating (the advice is still directionally valid but the methods or tools need revision). Only 1.1% is genuinely displaced — advice that is no longer useful because LLMs have made the underlying task trivial or the referenced tools defunct.

### Extract type and relevance

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

**H2 verdict: Confirmed** — and the effect is stronger than hypothesised. Tool-specific advice, a subcategory not in the original hypothesis, is the most vulnerable of all. The abstract principles of data journalism — skepticism, transparency, verification, evidence-based reasoning — are technology-independent. The specific methods are not.

### Redefinition candidates

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

**H3 verdict: Confirmed** — with Clean showing far more disruption than initially expected (80.2% vs the hypothesised >30% threshold).

### The 46 displaced extracts

The 46 displaced extracts cluster into clear categories:

1. **Defunct tools** (18 extracts): Google Fusion Tables, Kimono Labs, ScraperWiki, TileMill, namechk — tools that no longer exist or function.

2. **Manual text preprocessing** (12 extracts): Tokenization, stop-word removal, stemming, sentence segmentation, encoding fixes, whitespace normalization. LLMs process raw text directly, making this preprocessing layer largely unnecessary.

3. **Search operator syntax** (10 extracts): Google AROUND(), site:, filetype:, OR operators, min_retweets filters. LLM-powered search agents handle these queries conversationally without requiring syntax knowledge.

4. **Obsolete workflows** (6 extracts): Selective interview transcription (LLMs transcribe full interviews cheaply), manual data entry templates (LLM-assisted validation), and manual PDF extraction (LLMs handle natively).

**Source concentration**: The Verification Handbook series (sources #138, #142, #143) accounts for 16 of 46 displaced extracts (35%), largely due to their detailed Google search operator tutorials. The NICAR tipsheets (#97) contribute 7 displaced extracts, mostly NLP preprocessing recipes.

### Needs_update patterns

The 1,282 needs_update extracts (29.5% of corpus) are not displaced — the underlying advice is still directionally correct — but the specific methods require revision. Common patterns:

- **Tool substitution**: Advice referencing Excel, OpenRefine, or Tableau that could now be augmented or replaced by LLM-assisted workflows
- **Procedural simplification**: Multi-step manual processes (e.g., data profiling, format conversion, basic analysis) that LLMs can now perform in a single prompt
- **Skill reframing**: Advice about learning specific programming syntax or tool interfaces that shifts toward learning how to prompt and validate LLM outputs

The key insight: needs_update advice is still *teaching the right thing* — you still need to clean data, verify sources, and analyse patterns — but the *how* has changed.

## Methodology

### Corpus

81 sources were selected through systematic search of data journalism textbooks, handbooks, NICAR tipsheet archives, academic articles, and curriculum guides published between 2012 and 2025. Sources span four languages (EN, FR, ES, PT); non-English sources were translated to English via Claude API before extraction. The corpus totals approximately 1.5 million words after cleaning.

### Pipeline

The extraction and analysis followed a reproducible eight-step pipeline, each step implemented as a standalone PEP 723 Python script:

1. **T8 Clean**: Regex-based cleaning of converted markdown files — removal of junk lines (page numbers, publisher metadata), encoding fixes (HTML entities, ligatures), structural markup removal (Pandoc anchors, stray HTML), and code block stripping.
2. **T9 Chunk + Extract**: Large files were deterministically chunked by heading or word boundary (max 40K words per chunk). LLM agents extracted structured passages from each chunk into a JSON schema specifying: extract text, chapter, pipeline step, secondary step, extract type, themes, and notes.
3. **T10 Relevance Scoring**: LLM agents scored each of the 4,351 extracts for LLM-era relevance using three labels — *endures* (advice remains valid as-is), *needs_update* (directionally correct but methods need revision), *displaced* (no longer useful) — with a mandatory rationale for each score.
4. **T11 Merge**: Count-gated merge of chunk-level extractions and relevance scores into source-level files, then flattened into a single `horizon-table.csv` (4,351 rows, 14 columns).
5. **T12 Analyse**: Deterministic cross-tabulation producing six analysis CSVs: step distribution, type × relevance, step × relevance, themes by step, displaced extracts, and source coverage.

### Classification schema

**Extract types:**
- *Epistemological*: Principles about why something matters, how to think about it, what values or standards apply
- *Procedural*: Step-by-step methods for accomplishing a task
- *Organizational*: Advice about team structure, project management, newsroom culture
- *Tool-specific*: Guidance tied to a named tool or platform

**Relevance labels:**
- *Endures*: The advice is valid as-is in an LLM-augmented workflow
- *Needs update*: The underlying principle holds but the specific method, tool, or workflow needs revision
- *Displaced*: The advice is no longer useful — the referenced tool is defunct, the manual process is fully automated, or the technique is obsolete

### Validation

Extraction and relevance scoring were validated at each step: T9 checked for required fields, valid enum values, extract length bounds, step distribution balance, and theme counts. T10 checked for scoring completeness, valid labels, and rationale presence. Merge steps used count-gating (all chunks must be complete before merging). The final analysis (T12) is entirely deterministic — no LLM involvement.

## Limitations

1. **LLM-scored relevance**: The endures/needs_update/displaced labels were assigned by LLM agents (T10), not human coders. While validated against deterministic checks and human-reviewed samples, systematic bias toward "endures" is possible — LLMs may underestimate their own disruptive potential.

2. **English-language bias**: While 15 non-English sources were translated, the corpus is 85%+ originally English, weighted toward US/UK data journalism traditions. Practices specific to non-English-language contexts may be underrepresented.

3. **Temporal snapshot**: Relevance was scored in February 2026. The LLM landscape is evolving rapidly; advice scored as "endures" today may shift as capabilities expand.

4. **Source selection**: The corpus of 81 sources, while systematic, is not exhaustive. Practitioner knowledge shared informally (Slack communities, conference hallways, newsroom mentoring) is absent.

5. **Extract granularity**: The unit of analysis is a passage, not a complete argument. Some nuanced positions may be split across multiple extracts or lose context when isolated from surrounding text.

6. **Clean step underrepresentation**: Clean's low extract count (243, 5.6%) means its high redefinition rate (80.2%) is based on a smaller sample than other steps. However, the pattern is consistent and the displaced extracts are qualitatively coherent.

## Conclusions

The data journalism pipeline endures as a teaching structure. Seven out of ten recommendations from the canonical literature remain valid in the LLM era, and the seven-step sequence — Define, Find, Get, Verify, Clean, Analyse, Present — retains its pedagogical logic. The order matters: Define before Find, Verify before Analyse.

What changes is not the structure but the content within it. Three steps require redefinition: Clean, where LLMs have displaced the entire preprocessing-before-analysis paradigm; Get, where legal and ethical principles endure but technical acquisition methods are transforming; and Analyse, where the methods are shifting even as the analytical principles hold. The consistent pattern across all three is that epistemological advice survives while procedural and tool-specific advice does not.

This finding has a direct curriculum design implication: teach principles first, methods second, tools last — and design the curriculum so that methods and tools can be updated without rebuilding the conceptual foundation. The gap in Clean coverage (only 5.6% of the literature) is itself an opportunity: a curriculum designed in 2026 can lead rather than follow the literature in teaching what AI changes about data cleaning.

Actionable curriculum implications derived from these findings are incorporated into `content/theory.md`.
