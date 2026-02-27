# IJBA Datalab 2026

Curriculum, research, and tooling for the 2026 edition of the IJBA data journalism module and Datalab — 5 days of classes followed by a 5-day investigation week for graduate journalism students at the Institut de Journalisme Bordeaux Aquitaine.

A substantial amount of research has been done to prepare this edition. Large language models are now integrated in the curriculum, and that meant rethinking the place existing frameworks (data pipeline), methodologies (horizon table), and tools (google sheets, openrefine, tabula...) had in the program. 

So what did change? The broad answer is: workflows change, but frameworks remain. The structure that has been refined over the years has emerged from my research as the greatest asset to harness LLMs in a way that centers journalism instead of displace or degrade it. Consequently, the pace of the course (which was already quite fast due to time constraints) doesn't evolve much, and even the central tool, Google Sheets, preserves its place. Instead, two things evolve:

1. AI tools are introduced as a way to document, research, and speed up some of the tasks
1. The core frameworks and methodologies are refined and strenghtened

Just like for any other tool, we plan to introduce AI a tool in service of journalism, and not the other way around.

## Structure

```
content/            Curriculum design documents
  theory.md           Design principles, evidence, rationale
  draft_curriculum.md Day-by-day spiral curriculum (5 days)
  curriculum-todo.md  Outstanding development tasks
  handouts-todo.md    Skill document checklist
  handouts/           Student-facing artifacts

research/           Research inputs to curriculum design
  newsroom-robots/    Podcast thematic analysis (42 episodes)
  pipeline-canon/     Data journalism methodology review (81 sources)

reference/          External reference materials
  pipeline-reference.md        SCoDA pipeline notes
  iri_data_literacy_curriculum_final.md

research/
  pipeline-canon/
    scripts/          Python scripts (PEP 723, run via uv)
      log_action.py     Action logging utility
      analyse/          T9–T12 extraction and analysis pipeline
      clean/            T8 corpus cleaning and translation
      verify/           T6 corpus profiling
      get/              T4–T5 source acquisition and conversion
      review/           Horizon-table review tool
```

## Curriculum

The curriculum uses the **School of Data 7-step pipeline** (Define, Find, Get, Verify, Clean, Analyse, Present) as its spine. Each step is introduced once, then revisited across the week at increasing complexity and AI autonomy — a spiral structure.

Key design elements:

- **Scaffold fading**: Four cumulative AI cap levels control when and how students use AI at each step. Define never exceeds Q&A — the editorial question is always human-driven.
- **Skill/Task framework**: Students build a portable library of reusable AI skill documents, learning to engineer AI workflows rather than just prompt chatbots.
- **Horizon Table**: The empty spreadsheet students design before finding any data. Forces Define-before-Find and creates the output schema that constrains AI extraction.
- **Critical data practice**: A daily reflexive question drawn from the DDJ Handbook 2 framework — who counted this, what's invisible, what does the algorithm assume.

See `content/theory.md` for full rationale and `content/draft_curriculum.md` for the day-by-day plan.

## Research

Two research projects inform the curriculum design. Both are complete; their findings are integrated into `content/theory.md`.

### Newsroom Robots — Podcast Thematic Analysis

A 7-pass thematic analysis of 42 episodes of the *Newsroom Robots* podcast (Jan 2024 – Jan 2026), covering real AI adoption at newsrooms including Aftonbladet, iTromsoe, Der Spiegel, NYT, Times of India, Ippen, and Delfi.

- **Corpus**: ~339K words across 42 transcripts
- **Output**: 12 themes, 48 sub-themes, 1,445 inductive codes
- **Teaching resources**: 350 AI tools identified, 428 use cases, 252 curated quotes, case studies, glossary, discussion prompts
- **Curriculum role**: Grounds every "Research Grounding" row in the curriculum in documented newsroom practice. Supplies the quizzes, case studies, and industry context that make abstract pipeline steps concrete.

Located in `research/newsroom-robots/`. See `outputs/codebook.md` for the thematic codebook and `outputs/resources/` for teaching materials.

### Pipeline Canon — What Endures in the LLM Era

A systematic literature review of 81 canonical data journalism sources (2012–2025) — textbooks, handbooks, NICAR tipsheets, academic articles, and curriculum guides across EN/FR/ES/PT — asking what practitioners recommend at each pipeline stage and which recommendations survive the arrival of LLMs.

- **Corpus**: 81 sources, 5.14M words, 4 languages
- **Output**: 4,351 coded extracts mapped to the 7 pipeline steps, classified by knowledge type, scored for LLM-era relevance
- **Key findings**:
  - 70% of canonical advice endures as-is
  - Epistemological advice (principles, reasoning) is nearly indestructible: 89.4% endures
  - Tool-specific advice is the most fragile: only 10.6% endures
  - Three steps flagged for redefinition: Clean (80.2%), Get (49.1%), Analyse (35.6%)
  - Only 46 extracts (1.1%) are genuinely displaced — defunct tools, manual preprocessing, obsolete search syntax
- **Curriculum role**: Validates the pipeline as a teaching structure, confirms the scaffold fading approach (teach principles before tools), and identifies where the curriculum must go beyond the published literature — especially for Clean, where 80% of existing advice needs revision but only 6% of the literature covers the topic.

Located in `research/pipeline-canon/`. See `analysis/t13_report.md` for the full literature review and `analysis/t12_results.md` for raw cross-tabulation results.

## Scripts

All scripts are standalone PEP 723 Python files, run via `uv run`, and live alongside their data in `research/pipeline-canon/scripts/`. They are designed to be called by LLM agents during the research pipeline — structured stdout for parsing, errors to stderr, `--help` on every script.

The pipeline sequence: T8 (clean) → T9 (chunk, extract) → T10 (score relevance) → T11 (merge) → T12 (analyse). See `research/pipeline-canon/scripts/analyse/pipeline_status.py` for progress tracking.

## Requirements

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) (dependency management and script runner)
- Dependencies are declared per-script in PEP 723 inline metadata
