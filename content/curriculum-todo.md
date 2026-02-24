# Curriculum TODO

Stubs and underdeveloped sections in `draft_curriculum.md` that need fleshing out.

---

## Quizzes

### Morning Quizzes (Days 2-5)
Currently just "Recall from Day N" — need actual questions.

- [ ] **Day 2 morning quiz** — 5 MCQ on: pipeline order, Define purpose, data source types, what a Horizon Table is, one Open Data history question
- [ ] **Day 3 morning quiz** — 5 MCQ on: Lombion quadrant identification (give scenario → which quadrant?), verification vs. analysis, what reproducibility means, data representation concept, one WBEZ/Reinhart-Rogoff question
- [ ] **Day 4 morning quiz** — 5 MCQ on: cleaning function matching (which Sheets function for X?), document parsing palette (which approach for which question?), "Why Before How" application, OpenRefine purpose, dirty data types
- [ ] **Day 5 morning quiz ("Final Showdown")** — 8-10 MCQ cumulative: RAG definition, human-in vs human-on-the-loop, analysis method steps, pivot table purpose, one algorithmic accountability question, one Lombion question, one parsing palette question

### Day 1 Baseline Quiz
- [ ] **Day 1 morning quiz** — 5 MCQ baseline: what is data journalism (definition), name a famous data viz (Nightingale/Minard), what is a CSV, what does CADA stand for, what is a pivot table. Calibration — expect low scores, that's the point.

### Day 1 End-of-Day Quiz ("Guess the Scale")
- [ ] Flesh out with 8-10 questions beyond the 4 listed. Add: How many journalists use NYT Echo? (2,000). How long did Delfi build data infrastructure before AI paid off? (8 years). What did Good Tape sell for? ($3M). What's the ratio of newsrooms with vs without AI strategy? Frame as multiple choice with surprising wrong options.

### Day 4 "Guess the Process"
- [ ] Select 2-3 published investigations and write the reverse-engineering prompts. For each: show the final output, then ask students to identify (a) starting question, (b) which parsing approach, (c) where AI vs human. Need actual links/screenshots.

---

## Timing

- [ ] **Produce a minute-by-minute schedule for each day.** Current structure is morning/afternoon blocks. Need: theory duration, exercise duration, quiz duration, transition time. Assume 9h00-12h30 morning (with 15 min break), 14h00-17h30 afternoon (with 15 min break). Total ~7h usable per day.
- [ ] **Day 1 is the densest** — 3 new steps. Verify that Define morning (theory + Horizon Table exercise + whiteboard) fits in ~3h. Verify that Find+Get afternoon (theory + IMPORTHTML exercise + end-of-day quiz) fits in ~3h.
- [ ] **Day 3 morning is the most complex** — Define (quick) + Find/Get assistant unlock (parsing palette theory + exploration) + Verify Q&A. Estimate time for parsing palette theory (likely 30-40 min) and ensure hands-on time for AI-assisted Find/Get.
- [ ] **Day 5 afternoon is the lightest** — Present theory + Datawrapper + portfolio assembly. May have slack for wrap-up, Conspicuous Absences (2 min), "Where's the Human?" spectrum (5 min), and buffer.

---

## Artifacts / Skill Docs

Currently listed as one-liners. Each needs a content outline.

- [ ] **Horizon Table Skill doc** (Day 1 AM) — template + instructions for designing a Horizon Table from a question. Include: column naming conventions, critical question prompt ("What can't this capture?"), example filled row.
- [ ] **Web-Import Skill doc** (Day 1 PM) — IMPORTHTML syntax, when to use it, limitations, format awareness (what breaks, what needs cleaning).
- [ ] **Verification Skill doc** (Day 2 PM) — verification checklist (Lombion quadrants as diagnostic), common failure modes, reproducibility principle.
- [ ] **Document Parsing Skill doc** (Day 3 AM) — the 4-approach palette as a decision tree. For each: when to use, example prompt, expected output shape, limitations.
- [ ] **Cleaning Skill doc** (Day 3 PM) — dirty data taxonomy, Sheets functions reference, OpenRefine mention, when to escalate to code.
- [ ] **Verification Automation Skill doc** (Day 4 AM) — RAG concept, human-in/on-the-loop decision framework, algorithmic accountability checklist.
- [ ] **Pivot Table Skill doc** (Day 4 PM) — pivot table construction steps, conditional formatting for patterns, linking analysis questions to pivot table design.
- [ ] **CLI Automation Skill doc** (Day 5 AM) — Terminal basics, `uv` setup, running a cleaning script, interpreting output, when CLI beats GUI.

---

## Theory Gaps in Curriculum Draft

- [ ] **Skill vs Task framework** — currently not in draft_curriculum.md. Needs to be integrated, probably Day 1 morning (after Horizon Table, before exercises) or as a framing section before Day 1. See `theory.md` §2 for the full concept. Students need to understand early that they're building Skills, not just doing exercises.
- [ ] **AI pipeline theory** — the "what AI changes per step" table from theory.md should appear somewhere in the curriculum, possibly as a Day 1 morning overview or as a handout. Students need the big picture before the spiral begins.
- [ ] **Scaffold fading explanation** — students should understand *why* the AI cap changes. A 2-minute framing on Day 1 ("You'll do this manually first, then with AI help, then with AI driving") prevents confusion about why they can't use ChatGPT freely on Day 1.
- [ ] **"Beyond GUI" progression** — Day 5 morning jumps to CLI agents without much setup. Consider adding a brief "tools spectrum" mention on Day 3 (when The Wall hits): "Today you're cleaning in Sheets. Tomorrow AI helps. Day 5, you'll automate this with a script."

---

## Project Continuity

- [ ] **Clarify which datasets persist across days.** The curriculum mentions different projects per day (demographics, French Presidents, maternity wards, digital divide). Are these independent exercises or does one dataset thread through? If independent, the Horizon Table loses its spiral power. Consider: one anchor dataset that grows across the week + daily satellite exercises.
- [ ] **Day 2-3 transition** — Maternity Ward (Day 2) → Digital Divide (Day 3). Is there a connection? If not, the Define step on Day 3 feels disconnected from the verification work on Day 2.
- [ ] **Final portfolio scope** — "Story (Datawrapper) + Horizon Table (final dataset) + Skill Library (all skill docs)" — which dataset is the final story about? Needs to be explicit.

---

## Sources Section

- [ ] **Add sources section to draft_curriculum.md** — see below, ready to integrate.
