# Handouts TODO

Student-facing documents to prepare before the course. Each handout is a standalone PDF/printout.

---

## Skill Docs (SKILL.md format)

These are the course artifacts — students build them progressively. Each follows the SKILL.md template and is designed to be reusable with AI tools after the course.

### 1. SKILL: Creating a Skill
- **Day introduced:** Day 1 (framing, before first exercise)
- **Content:**
  - What a Skill is (reusable AI-readable document that packages expertise)
  - The SKILL.md template structure: metadata, objective, context, output shape, verifiability rules, process checklist
  - The Skill vs Task distinction: the artifact vs the process
  - Example: a minimal Skill for "Import a web table into a spreadsheet"
  - Why Skills matter: Good Tape analogy (internal tool → reusable asset → business)
  - How to write constraints that prevent AI shortcuts

### 2. SKILL: Building a Query for an AI-Driven Task
- **Day introduced:** Day 2 (when Q&A cap unlocks)
- **Content:**
  - Anatomy of a good query: objective + context + constraints + output format
  - The difference between chatting and querying (conversation vs structured task)
  - "Why Before How" applied to prompting: define what you need before asking how
  - Verifiability anchors: requiring quotes, page numbers, source URLs in AI output
  - Common failure modes: vague objectives, missing constraints, no output shape
  - Example: querying NotebookLM for C-section data in PDFs (Day 2 exercise)
  - Anti-pattern: "summarize this" (no constraints, no shape, no anchors)

### 3. SKILL: Scouting Documents with AI
- **Day introduced:** Day 2 (NotebookLM introduction)
- **Content:**
  - When to scout vs when to extract (scouting = understanding what's in a corpus before committing to a method)
  - NotebookLM as industry-standard scouting tool (Der Spiegel, BBC, Economist, Philadelphia Inquirer)
  - What scouting produces: a map of what's available, not the data itself
  - Connecting scouting results to Horizon Table design (does this corpus have what my table needs?)
  - Limitations: model decides relevance, context window constraints

### 4. SKILL: Scraping the Web
- **Day introduced:** Day 3 (Find/Get assistant unlock)
- **Content:**
  - What scraping is and when it's the right approach (vs APIs, downloads, IMPORTHTML)
  - Legal and ethical considerations (robots.txt, rate limiting, public interest defense)
  - The spectrum: IMPORTHTML (simplest) → browser extensions → Python scripts → dedicated scrapers
  - Connecting scraping output to the Horizon Table (does the scraped data match my schema?)
  - When to ask AI for help writing a scraper vs when to use a pre-built tool
  - Example: scraping a public data table that has no download button

### 5. SKILL: Cleaning Data
- **Day introduced:** Day 3 PM (The Wall)
- **Content:**
  - Dirty data taxonomy: inconsistent formats, duplicates, encoding issues, ambiguous nulls, mixed types
  - Google Sheets functions: SPLIT, SUBSTITUTE, IF, TRIM, CLEAN, PROPER
  - OpenRefine: what it is, when to use it (scale beyond what Sheets handles comfortably)
  - The cleaning spectrum: manual Sheets (Day 3) → OpenRefine → CLI scripts (Day 5)
  - Verification after cleaning: did cleaning change the meaning of the data?

### 6. SKILL: Parsing Documents with AI
- **Day introduced:** Day 3 AM (Document Parsing Palette)
- **Content:**
  - The 4-approach decision tree:
    1. Naive AI search — "What does this say about X?" → quick exploration, model decides relevance
    2. Summarize individually — "What's in each document?" → preserves document-level granularity
    3. Entity extraction — "Who/what/when/where?" → structured search anchors
    4. Embeddings / semantic search — "What's similar to what?" → finds what keyword search misses
  - For each: when to use, example prompt, expected output, limitations
  - "Why Before How": the choice depends on the question, not the tool
  - Connecting to Horizon Table: which approach fills which columns?

### 7. SKILL: Verifying AI Output
- **Day introduced:** Day 4 AM (Verify assistant unlock)
- **Content:**
  - RAG explained simply: AI answers grounded in specific documents, not general knowledge
  - Verifiability rules: anchors (quotes, page numbers, URLs) that make AI output falsifiable
  - The Lombion schema as diagnostic: which quadrant is this failure in?
  - Algorithmic accountability: 4 audit angles (discrimination, errors, legal violations, human misuse)
  - Human-in-the-loop vs human-on-the-loop: when is each appropriate?
  - "Hallucination is a feature, not a bug" — what this means for workflow design
  - Checklist: before publishing any AI-assisted finding, verify X, Y, Z

### 8. SKILL: Automating with CLI Tools
- **Day introduced:** Day 5 AM (Clean assistant unlock)
- **Content:**
  - Why CLI: reproducibility, automation, scale, version control
  - Terminal basics: navigating directories, running scripts, reading output
  - `uv` as Python environment manager: what it does, why it matters
  - Running a cleaning script: input → process → output → verify
  - The prototype-to-production gap: what students build = prototype. Professional versions require engineering.
  - When CLI beats GUI: repetitive tasks, large datasets, reproducibility requirements

---

## Reference Handouts (non-Skill)

### 9. Horizon Table Guide
- **Day introduced:** Day 1 AM (first exercise)
- **Content:**
  - What a Horizon Table is: the empty spreadsheet you design *before* finding data
  - Why it matters: forces "Why Before How," creates the output shape for AI tasks, makes absence visible
  - How to design one:
    1. Start with the question (What are we trying to show/prove/explore?)
    2. Identify the unit of observation (What is one row? A person? A year? An event?)
    3. Define columns (What do we need to know about each unit?)
    4. Add metadata columns (source, date retrieved, confidence level)
    5. Critical Question: "What can't this table capture? Who is invisible?"
  - Column naming conventions: lowercase, no spaces, descriptive (e.g. `commune_name`, `year`, `c_section_rate`)
  - Example: demographics Horizon Table from Day 1 exercise
  - Example: maternity ward Horizon Table from Day 2 exercise
  - Common mistakes: too many columns, vague column names, no unit of observation, forgetting source columns

### 10. Data Pipeline Overview Card
- **Day introduced:** Day 1 AM (before first exercise, kept by students all week)
- **Content:**
  - The 7-step pipeline as a visual diagram: Define → Find → Get → Verify → Clean → Analyze → Present
  - For each step: one-sentence definition, one example, the AI cap progression across days
  - The "What AI Changes" table (from theory.md): what's new, what doesn't change
  - Credit: School of Data / Open Knowledge Foundation
  - Back of card: the week's Critical Questions (one per day)

### 11. Critical Data Questions Card
- **Day introduced:** Day 1 AM (referenced daily)
- **Format:** Small card or bookmark. Could be printed on the back of the Pipeline Overview Card.
- **Content:**

  | Day | Question | What It Challenges |
  |-----|----------|--------------------|
  | 1 | "What can't this table capture? Who is invisible?" | Data as complete representation |
  | 2 | "Who counted this, and how?" | Data as objective truth |
  | 3 | "What would it take to build this dataset from scratch?" | Data as given/found |
  | 4 | "What does this algorithm assume?" | AI as neutral tool |
  | 5 | "Who is the audience, and what do they need?" | Output as self-evident |

  - Sources: D'Ignazio (feminist data), Kukutai/Taylor (Indigenous data sovereignty), Grassi (Argentina femicides), Diakopoulos (algorithmic accountability), DDJ Handbook 2 civic engagement chapters (Bogotá, Philippines)
  - Instruction to students: ask yourself this question at least once during the day's work. There is no right answer — the point is to develop the reflex.

---

## Where Critical Questions Live

The DDJ Handbook 2 critical questions work at three levels:

1. **In the curriculum itself** — embedded in the Interactive row of each day, posed during Define or wrap-up (~1 min).
2. **As a standalone card** (Handout #11) — students keep this on their desk all week. Physical reminder.
3. **Inside relevant Skill docs** — each Skill doc includes the critical question most relevant to its pipeline step:
   - Horizon Table Guide (#9): "What can't this table capture?"
   - Building a Query (#2): "Who counted this, and how?" (applies to evaluating AI-retrieved information)
   - Parsing Documents (#6): "What would it take to build this from scratch?" (before choosing a parsing approach, ask if the documents themselves are trustworthy)
   - Verifying AI Output (#7): "What does this algorithm assume?"
   - Automating with CLI (#8): "Who is the audience?" (automation should serve the story, not just be efficient)

This three-layer approach (curriculum → card → skill doc) means students encounter the questions in different contexts, reinforcing the critical reflex without making it feel like a lecture.

---

## Production Notes

- [ ] Design SKILL.md template (structure all Skill handouts will follow)
- [ ] Decide format: printed A4? Digital PDF? Both?
- [ ] Horizon Table Guide and Pipeline Overview Card should be Day 1 pre-distributed (on desks when students arrive)
- [ ] Skill docs are produced *by students* during exercises, but they need a template/example to follow — Handout #1 (Creating a Skill) serves this purpose
- [ ] Critical Questions Card can be a laminated bookmark — cheap, durable, always visible
