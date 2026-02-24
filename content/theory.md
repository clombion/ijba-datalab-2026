# Curriculum Design: Theory & Rationale

## 1. Design Principles

### Spiral Format
The curriculum uses a **spiral structure**: each pipeline step (Define, Find, Get, Verify, Clean, Analyze, Present) is introduced once, then revisited with increasing complexity and AI autonomy. Students encounter the same step multiple times across the week, each time at a higher level of sophistication. This produces durable learning — students don't just *learn* a step, they *internalize* it through repetition at escalating difficulty.

The spiral is not metaphorical. The Iteration Map is the literal schedule: Day 1 introduces Define/Find/Get at the simplest level; by Day 5, students execute those same steps rapidly while tackling new challenges in Clean/Analyze/Present.

### Scaffold Fading
AI usage follows a strict **scaffold fading** progression through four cumulative cap levels:

| Level | Role | Fading Logic |
|-------|------|-------------|
| **docs** | Students build a personal library of tutorials, prompts, and reusable AI skills. Strategic, not passive. Always on. | The baseline. Never removed. |
| **Q&A** | Query AI for planning, information gathering, problem-solving. | Introduced on second encounter with a step. Students already have theory + hands-on from the first pass. |
| **assistant** | AI-driven approach: structured exploration of how AI performs this step. | Introduced on third encounter. Students understand the step well enough to evaluate AI output critically. |
| **fast** | AI-driven, light difficulty. The step is now routine. | Fourth encounter onward. Execution speed, not learning. |

The key constraint: **Define never exceeds Q&A.** The editorial question — what are we investigating and why — is always human-driven. AI can inform it, never drive it.

### Interactivity Mix
Each day combines four modes:

1. **Morning quiz** (5 min, Slido-style MCQ) — retrieval practice. Day 1 = baseline; Days 2-5 = recall from previous days.
2. **Collaborative whiteboard** — students co-design Horizon Tables during Define. Most active Days 1-2, lighter thereafter.
3. **Critical Question** (~1 min) — one reflexive prompt per day, drawn from the DDJ Handbook 2's critical data practice framework. Forces students to question data provenance, absence, and audience.
4. **End-of-session activities** — Day 1 "Guess the Scale" quiz, Day 4 "Guess the Process" reverse-engineering exercise, Day 5 "Where's the Human?" spectrum.

### Theory → Hands-On Balance
Each new step follows the same pattern:
- **Afternoon (1st pass):** Theory + guided hands-on exercise at docs cap. The step is new; students need conceptual grounding before touching tools.
- **Morning (2nd pass):** Theory is minimal or absent. Students repeat the step with more challenge and AI assistance (Q&A cap). Learning by doing.
- **Morning (3rd pass, assistant):** The "unlock" moment. Structured exploration of how AI changes this step. Theory returns, but now it's *AI architecture* theory (parsing palette, RAG, automation), not pipeline fundamentals.

## 2. The Skill and the Task

The curriculum introduces a distinction between the **artifact** and the **process** that underpins all AI-assisted work:

### The Skill (Artifact)
A standardized document (the SKILL.md format) that packages journalistic expertise into a reusable file. It contains the instructions, constraints, and metadata that allow an AI to perform a specific category of work. Students build their Skill Library across the week — each afternoon's new step produces a new Skill doc.

The Skill is what survives the course. Students leave with a portable library they can apply in internships, jobs, and personal projects. The analogy is Good Tape: an internal Whisper prototype became a $3M business because it was packaged as a reusable asset.

### The Task (Process)
The conceptual journalistic workflow documented *within* a skill. A Task is a single, bounded unit of work that belongs to one stage of the Data Pipeline (Find, Get, Verify, Analyze). It explicitly documents:

- **Objective & Context:** The specific goal and source material boundaries.
- **Output Shape:** The exact schema for the Horizon Table — the minimum dataset required.
- **Verifiability Rules:** Mandatory "anchors" (direct quotes, page numbers, source URLs) that force the AI to produce falsifiable results.
- **Process Checklist:** The internal "chain of thought" steps the AI must follow. This prevents shortcuts and "eyeballing."

The Skill/Task distinction teaches students that AI assistance is not magic — it's **engineering.** You design the constraints, specify the output, and build in verification. The AI executes within those boundaries.

### The Horizon Table as Control Surface
The Horizon Table — the empty spreadsheet students design before finding any data — is the course's central pedagogical device. It serves three functions:

1. **Forces Define before Find.** Students must articulate what they need before searching. ("Why Before How.")
2. **Creates the Output Shape for Tasks.** The Horizon Table columns *are* the schema the AI must fill. No schema = no constraint = hallucination.
3. **Makes absence visible.** When students ask "What can't this table capture?" they practice the critical data literacy that separates journalism from data processing.

## 3. The Data Pipeline in the Age of AI

### What AI Changes
AI reshapes each pipeline step differently:

| Step | Pre-AI | With AI | What Doesn't Change |
|------|--------|---------|-------------------|
| **Define** | Human question | Human question (AI can inform, not drive) | Editorial judgment |
| **Find** | Manual search, portals, FOI | AI-assisted scouting (NotebookLM), semantic search | Source evaluation |
| **Get** | Manual download, scraping, IMPORTHTML | Document parsing palette (4 approaches, each for a different question) | Format understanding |
| **Verify** | Manual audit, cross-checking | RAG-grounded systems, algorithmic accountability audits | Skepticism, provenance |
| **Clean** | Spreadsheet formulas, OpenRefine | CLI automation, AI-assisted normalization | Understanding *why* data is dirty |
| **Analyze** | Pivot tables, descriptive stats | Multi-model approaches, pattern detection at scale | Hypothesis formation, critical interpretation |
| **Present** | Datawrapper, static charts | Conversational formats, adaptive complexity, searchable databases | Story > tool, message > visualization |

### What AI Doesn't Change
The pipeline's order matters. Define before Find. Verify before Analyze. Clean before everything else works. AI accelerates steps but doesn't reorder them. The curriculum enforces this: students experience every step manually before AI is introduced.

The "Why Before How" principle — the most repeated insight across 42 episodes of industry interviews — applies at every level: choose the pipeline step before the tool, choose the question before the method, choose the editorial goal before the AI capability.

## 4. What Changed from 2024-2025

### Preserved
- **The 7-step pipeline** (Define → Find → Get → Verify → Clean → Analyze → Present) — credited to School of Data / Open Knowledge Foundation. Proven over 8 years of teaching.
- **Tabular Thinking and the Horizon Table** — introduced 2024-2025, now central to the course.
- **Lombion quality schema** — the 4-quadrant framework for data quality assessment.
- **Core theory frameworks** — history timeline, 3 objectives, 4 applications, Open Data revolution, analysis types, The Triad, analysis blind spots.
- **Data journalism first** — this is not an AI class. The pipeline, the editorial judgment, the verification instinct come first. AI is a capability layer, not the subject.

### Changed

**1. AI integration via scaffold fading.** Previous years had no structured AI progression. 2026 introduces the 4-level cap system (docs → Q&A → assistant → fast) so students encounter AI at the right moment for each step — after they understand it manually.

**2. Tool tutorials reduced to a strict minimum.** AI is proficient at explaining how to use Google Sheets, Datawrapper, or any GUI tool. Class time previously spent on step-by-step tool walkthroughs is redirected to: (a) understanding *what task is possible*, (b) knowing *which tools work well* for which pipeline steps, (c) learning to go *beyond GUI tools* — scripts, command-line tools, CLI agents. The Skill Library replaces the tutorial: students build reusable AI-readable docs instead of following instructor-led demos.

**3. Grounding in documented newsroom practice.** Previous years relied on general data journalism examples. 2026 draws on systematic analysis of 42 podcast episodes (Newsroom Robots, Jan 2024 – Jan 2026) covering real AI adoption at Aftonbladet, iTromsoe, Der Spiegel, NYT, Times of India, Ippen, Delfi, and others. Every Research Grounding row cites real practice, not hypotheticals.

**4. Critical data practice framework.** New for 2026: a daily Critical Question drawn from the DDJ Handbook 2, plus the "Conspicuous Absences" closing. Students learn to question data provenance, absence, power dynamics, and audience — not just technical quality.

**5. The Skill/Task framework.** New conceptual layer that makes AI assistance *designable* — students learn to engineer AI workflows, not just prompt chatbots.

**6. Beyond-GUI progression.** Day 5 introduces CLI agents (Terminal + `uv`) that automate Day 3's manual cleaning. Students experience the full spectrum: manual spreadsheet → OpenRefine → scripted automation. This prepares them for professional environments where code-level tools are standard.
