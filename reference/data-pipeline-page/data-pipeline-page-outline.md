# Data Pipeline Page — Structural Outline

This document records the rationale behind the structure of `data-pipeline-page.md`. It is preserved as a companion reference so that future editors understand why the page is organized the way it is.

---

## Purpose

A single, authoritative description of the School of Data's 7-step data pipeline methodology — suitable for team members, students, collaborators, and partners. The page is generic (not tied to any one project) and self-contained. It is an overview, not a teaching resource — detailed examples, exercises, tables, and tool walkthroughs belong in curriculum slides.

## Source material

- `reference/pipeline-reference.md` — exhaustive compilation across 14 sources (~1500 lines)
- `reference/Data pipeline views.png` — original diagram (split into two SVGs for the page)

---

## Three-part structure

### Section 1 — Introduction

**Purpose**: Frame the methodology before presenting the steps.

**Content**: Two flowing paragraphs, no subsections or bullet points.

1. **Data definition + two risks** — "Data is a structured representation of the world." Flawed structure (encoding) or gaps in representation. The pipeline addresses both.

2. **History + AI** — Iterations since 2012, Define step added in 2016, AI models emerging ten years later. AI brings potential but also a greater need for structure and control.

**Why here**: These principles apply to the whole pipeline. Placing them before the steps prevents repetition.

### Section 2 — Definition: The 7 Steps

**Purpose**: The core of the page. Define what each step is and why it matters.

**Per-step structure — two layers**:

| Layer | Visibility | Content |
|---|---|---|
| Summary + description | Always visible | One-sentence summary, then one to two paragraphs of conceptual explanation. |
| "More on this step" | Collapsed `<details>` block | Brief illustration, AI role (one to two sentences), typical outputs (short list). Flows as a single readable section, not three separate blocks. |

**The boundary rule**: If removing a sentence would make the step harder to *understand*, it belongs in the description. If it would only make it harder to *apply*, it either goes in the collapsed block or stays in curriculum materials.

**What stays out**: Detailed tables, tool walkthroughs, exercises, checklists, case studies. Those belong in teaching materials.

#### Step-by-step notes

**1. Define** — Key concepts: research question, hypothesis, tabular thinking, horizon table. The horizon table is introduced here (designed during Define, populated during Clean, queried during Analyze).

**2. Find** — Key concepts: data locations, proxy indicators, effort scoping. The range from open data portal to "nowhere" (data must be constructed).

**3. Get** — Key concepts: format/retrieval matrix, complexity range. The matrix is mentioned conceptually, not reproduced as a full table.

**4. Verify** — Key concepts: structuration × representativity, three pillars (trustworthiness, completeness, quality), four methods, data dictionary, metadata.

**5. Clean** — Key concepts: three cleaning types (tidying, editing, consolidation), horizon table as target output. The connection to Define is explicit.

**6. Analyze** — Key concepts: three analysis types, the analysis chain (theme → hypothesis → column-level query), reproducibility via the analysis plan.

**7. Present** — Key concepts: three emphases (data, design, message), visualization task vocabulary, "present not visualize."

### Section 3 — Execution: From Steps to Tasks

**Purpose**: Explain how the 7 steps translate into real project work. The steps are a conceptual framework; tasks are where work gets done.

**Key concepts**:

- **Task** — A discrete unit of work that belongs to exactly one step and produces a concrete deliverable. Should not cross step boundaries.
- **Tasks per step** — A simple project may have one task per step; a complex one may have many.
- **Dependency graph** — Tasks don't flow in a straight line. They run in sequence, fork into parallel tracks, converge, and loop back to earlier steps.
- **Non-linearity** — Returning to an earlier step is part of the process. The Define–Find–Get loop and the Verify–Clean cycle are normal.
- **Scaling** — The seven steps are constant; what changes is the number and depth of tasks per step.

**Visuals**: Two SVG diagrams placed inline to illustrate what the text describes — the pipeline SVG after the paragraph about steps containing tasks, the task SVG after the paragraph about dependency graphs and looping.

**Why a separate section**: The steps are conceptual categories; execution is about workflow and project management. Mixing them blurs the distinction between methodology and practice.

---

## Format decisions

- Summaries and descriptions are plain sections (always visible).
- Each step has a single `<details>` block ("More on this step") combining illustration, AI role, and typical outputs in one readable flow.
- Diagrams are inline SVGs referenced as relative image links, placed where they illustrate the surrounding text.
- Attribution: "Created by School of Data, refined by CLI" in the header.

## Files

| File | Purpose |
|---|---|
| `data-pipeline-page-outline.md` | This document — structural rationale |
| `data-pipeline-page.md` | The full page with complete prose |
| `data_pipeline_views_pipeline.svg` | Steps-contain-tasks diagram |
| `data_pipeline_views_tasks.svg` | Task dependency graph diagram |
