# Curriculum: Spiral with Research Enrichment

## Structural Rules
1. **Define starts every morning** — always human, at best AI-informed, never AI-driven
2. **Afternoon = the new step** (1st pass)
3. **Morning = returning steps** accelerating with AI
4. **Day 1 exception:** 3 new steps across morning and afternoon
5. **AI tiers are cumulative.** If cap = assistant, that includes Q&A and docs. The table shows the **cap**.
6. **AI as docs is constant** — every step, every day, all the time

### AI Usage Cap Levels
| Level | Meaning |
|-------|---------|
| **docs** | Students actively build a personal library of tutorials, prompts, and reusable AI skills. Strategic, not passive. Always on. |
| **Q&A** | Query AI for help with planning, information gathering, and problem-solving. Exercises are more challenging than 1st pass (theory + hands-on intro already done). Includes docs. |
| **assistant** | AI-driven approach: structured exploration of how AI does this step. Includes Q&A + docs. |
| **fast** | AI-driven, light difficulty. The step is now routine — students execute quickly and move on. |

### Interactive Conventions
- **Morning quiz** every day (Slido-style MCQ, ~5 min) to wake up the room. Day 1: baseline knowledge. Days 2-5: recall from previous days.
- **End-of-day quiz** on Day 1 only ("Guess the Scale") to introduce industry context.
- **Define is interactive** with collaborative whiteboard, at least Days 1-2.
- **Daily Critical Question** (~1 min) — one reflexive prompt per day, posed during Define or wrap-up:

| Day | Critical Question |
|-----|------------------|
| 1 | "What can't this table capture? Who is invisible?" |
| 2 | "Who counted this, and how?" |
| 3 | "What would it take to build this dataset from scratch?" |
| 4 | "What does this algorithm assume?" |
| 5 | "Who is the audience, and what do they need?" |

---

## Iteration Map

| Step | Day 1 | Day 2 | Day 3 | Day 4 | Day 5 |
|------|-------|-------|-------|-------|-------|
| **Define** | 1st (docs) | 2nd (Q&A) | 3rd (Q&A) | 4th (Q&A) | 5th (Q&A) |
| **Find** | 1st (docs) | 2nd (Q&A) | **3rd (assistant)** | 4th (fast) | 5th (fast) |
| **Get** | 1st (docs) | 2nd (Q&A) | **3rd (assistant)** | 4th (fast) | 5th (fast) |
| **Verify** | n/a | 1st (docs) | 2nd (Q&A) | **3rd (assistant)** | 4th (fast) |
| **Clean** | n/a | n/a | 1st (docs) | 2nd (Q&A) | **3rd (assistant)** |
| **Analyze** | n/a | n/a | n/a | 1st (docs) | 2nd (Q&A) |
| **Present** | n/a | n/a | n/a | n/a | 1st (docs) |

**Bold = AI-driven pass (assistant cap) = the day the step is "unlocked" with AI.**

---

## Day 1 — Define → Find → Get (all new)

| Section | Morning | Afternoon |
|---------|---------|-----------|
| **Steps** | Define (1st) | Find (1st), Get (1st) |
| **AI usage cap** | docs | docs |
| **Theory** | What is DDJ — definition, history (Nightingale 1855 → Minard 1869 → Mayer 1967 → Jones 1968 → Burnham 1977 → Morin/Tasker 1985 → Dedman 1988 → Rogers 2008). Each era assumed something different about what data *proves*: Progressive era believed transparent facts → enlightenment; Precision Journalism professionalized social science; computational era risks "facts speak for themselves" (Anderson, *Apostles of Certainty*). The current era's risk = overclaiming certainty. 3 objectives (compile, analyze, make available). 4 applications (illustration, investigation, personalized info, decryption). Non-journalist actors (institutions, activists, researchers). Local scale examples. Tabular Thinking. What is a Horizon Table — and what it *can't* capture (D'Ignazio: what gets counted is a political decision; feminicides undercounted in Mexico, police killings in the US, maternal mortality globally). Why Define comes first. | What is a data source. Démarche — two starting points (from dataset OR from question). Data locations (open data portals, admin systems, physical archives, APIs, web, "nowhere" — but "nowhere" has strategies: (a) FOI/CADA requests, e.g. UK knife crime data from 43 police forces; (b) media monitoring + scraping, e.g. Turkish worker deaths; (c) crowdsourcing, e.g. La Nación Vozdata — 25K senate declarations verified by readers; (d) collaborative assembly networks, e.g. Land Conflict Watch India — 35+ researchers). Formats (xls/csv/shp/pdf/ods/json/xml/sqlite). Format transformation needs (when and why). Web tables as structured data. Open Data revolution (CADA 1978 → PSI 2003 → Etalab 2011 → Loi République Numérique 2016). Data & OSINT (Bellingcat). Google Sheets as tool environment (IMPORTHTML for web import). |
| **Project** | Deconstruct published charts. Manually type 20 rows of class demographics into a Horizon Table. | Locate Wikipedia table (e.g. French Presidents). Use `IMPORTHTML` in Google Sheets. |
| **Research grounding** | **"Why Before How"** — most repeated principle across 42 Newsroom Robots episodes. The Horizon Table *is* the "Why." Define your question before you pick your tool. | This manual web import is where most newsrooms still are. The maturity spectrum runs from here to integrated AI pipelines. Briefly mention **Whisper** as "the single undisputed AI productivity win" — audio → text → structured data, same pipeline logic. |
| **Interactive** | **Morning quiz (5 min):** General data journalism knowledge (baseline). Collaborative whiteboard: students co-design the Horizon Table columns for the demographics exercise. **Critical Question:** "What can't this table capture? Who is invisible?" (2 min, during whiteboard). | **End-of-day quiz (5 min):** "Guess the Scale" — How many AI tools at Aftonbladet? (25-30). What % of newsrooms actively use AI? (~20%). How long did iTromsoe's daily review take pre-AI? (60-90 min). How many models did Ippen evaluate? (200+). Introduces the **80/20 literacy divide** — students are joining the 20%. |
| **Artifact** | Horizon Table Skill doc | Web-Import Skill doc |

---

## Day 2 — Define → Find → Get → **Verify** (new)

| Section | Morning (returning steps) | Afternoon (new step) |
|---------|--------------------------|----------------------|
| **Steps** | Define (2nd), Find (2nd), Get (2nd) | **Verify (1st)** |
| **AI usage cap** | Define: Q&A. Find: Q&A. Get: Q&A | docs |
| **Theory** | n/a (steps seen yesterday, now more hands-on with AI for Q&A) | Data as "structured representations" — not raw reality, not just numbers or information. Reframing that introduces skepticism: data is a representation that can be incomplete, biased, or wrong. Lombion quality schema (structuration × representativity → 4 quadrants: hallucination/bad encoding/erroneous/good data). Ground with handbook examples: Reinhart-Rogoff Excel error = "bad encoding" quadrant (wrong cell range in austerity spreadsheet influenced EU policy — structurally sound data, but a processing error); COMPAS recidivism scores = "the data itself encodes bias" (ProPublica's Machine Bias: algorithm scored Black defendants as higher risk at twice the rate of white defendants with same profile). What verification means. 3 enjeux (fiabilité, exhaustivité, qualité). Reproducibility as a verification principle: "If you can't re-run the analysis and get the same result, you haven't verified it." (Global Witness reused Papua New Guinea scraping code years later for follow-up investigation.) This concept later justifies the Skill Library. Why it matters before any analysis. |
| **Project** | "Maternity Ward Medicalization" hypothesis. Design Horizon Table (whiteboard). Use NotebookLM to scout C-section data in PDFs — first time AI assists Find/Get. | Manual verification: audit findings, identify ambiguous nulls, missing codes, contradictions between sources. |
| **Research grounding** | NotebookLM is industry-standard: Der Spiegel, BBC, Economist, Philadelphia Inquirer. Students use a real newsroom tool at the right pipeline stage (scouting before extraction). | **Pure verification lesson — no AI architecture concepts.** Why verification matters in journalism. WBEZ Chicago: published AI-generated book list with fabricated titles. Went viral. CEO apology. The failure was a *verification* failure, regardless of what generated the list. |
| **Interactive** | **Morning quiz (5 min):** Recall from Day 1 (pipeline, Define, data sources). Collaborative whiteboard for Define (Maternity Ward hypothesis → what columns do we need?). **Critical Question:** "Who counted this, and how?" (1 min, during whiteboard). | n/a |
| **Artifact** | n/a | Verification Skill doc |

---

## Day 3 — Define → Find → Get → Verify → **Clean** (new)

| Section | Morning (returning steps) | Afternoon (new step) |
|---------|--------------------------|----------------------|
| **Steps** | Define (3rd), **Find (3rd, assistant), Get (3rd, assistant)**, Verify (2nd) | **Clean (1st)** — "The Wall" |
| **AI usage cap** | Define: Q&A. Find: **assistant**. Get: **assistant**. Verify: Q&A | docs |
| **Theory** | Find/Get reach assistant cap: structured exploration of how AI changes data acquisition. Before the parsing palette: AI is one assembly strategy. Others: FOI campaigns, crowdsourcing platforms, researcher networks, cross-border collaborations (El Diario/El Faro traced 68M trade records across colonialism's legacy; Postdata.club Cuba reassembled fragmented government data through university partnership). The parsing palette handles *documents you already have* — getting documents is often the harder problem. The document parsing palette — 4 approaches, each answering a different question. The choice depends on the question (connects to "Why Before How"). | What cleaning means. Types of dirty data (inconsistent formats, duplicates, encoding). Google Sheets functions for cleaning (SPLIT, SUBSTITUTE, IF). OpenRefine as what newsrooms actually use for cleaning at scale before they reach code — free, visual, bridges the gap between spreadsheets and CLI (Philippines crash mapping: normalized inconsistent location data with OpenRefine). Why cleaning is the bottleneck. |
| **Project** | "Digital Divide in Rural Areas." Design Horizon Table (Define, quick by now). Then explore AI-driven Find/Get with the day's data sources. | Attempt manual cleaning of 1,000 rows of inconsistent addresses. Experience the bottleneck. |
| **Research grounding** | **Document Parsing Palette.** Four approaches, each for a different question: | **The Wall has industry backing.** Delfi: 8 years of data infrastructure before AI paid off. Times of India: "banking-grade" pipelines. Cross-analysis finding: "Data infrastructure, not AI models, is the binding constraint." The boring work matters most. |
| | | |
| | **1. Naive AI search** — "What does this say about X?" Chat with documents. Quick but model decides relevance. NotebookLM at Der Spiegel, BBC. | |
| | **2. Summarize individually, read summaries** — "What's in each document?" NYT manosphere project. Preserves document-level granularity. | |
| | **3. Entity extraction as search anchors** — "Who/what/when/where?" Pull names/orgs/amounts, use as structured search keys. iTromsoe fisheries: 5M transactions, entities as investigation anchors. | |
| | **4. Embeddings / semantic search** — "What's similar to what?" NYT Echo (2,000 journalists). Found euphemisms keyword search would miss. | |
| | **Pedagogical point:** these aren't interchangeable. The choice depends on the question. Connects back to Define ("Why Before How"). | |
| **Interactive** | **Morning quiz (5 min):** Recall from Days 1-2 (verification, quality schema, data locations). **Critical Question:** "What would it take to build this dataset from scratch?" (1 min). | n/a |
| **Artifact** | Document Parsing Skill doc | Cleaning Skill doc |

---

## Day 4 — Define → ... → Verify → Clean → **Analyze** (new)

| Section | Morning (returning steps) | Afternoon (new step) |
|---------|--------------------------|----------------------|
| **Steps** | Define (4th), Find (4th), Get (4th), **Verify (3rd, assistant)**, Clean (2nd) | **Analyze (1st)** |
| **AI usage cap** | Define: Q&A. Find/Get: fast. Verify: **assistant**. Clean: Q&A | docs |
| **Theory** | Verify reaches assistant cap: how newsrooms build AI verification systems at scale. Clean (Q&A): rapprocher les données — merging/consolidating datasets from multiple sources (why and when). | 3 types of analysis (descriptive: moyenne/médiane/écart-type/max; inferential: corrélation/sondage; predictive: modélisation/ML — scope for this course = descriptive). Before calculating, interrogate your numbers: Where did this number come from? Who counted? What was excluded? A mean or median inherits the biases of its source data. "700,000 Rohingya displaced" — what does this number include? Who counted? What methodology? A number without provenance is not an analysis. Analysis method (theme → hypotheses → analysis questions → reformulated with data columns). What pivot tables do — verification + analysis + presentation tool combined with conditional formatting. |
| **Project** | Earlier steps are fast (Define/Find/Get by 4th pass). Teaching weight on Verify assistant: explore AI-driven verification approaches with the day's data. Clean (Q&A): AI assists cleaning, previewing tomorrow's full automation. | Google Sheets Pivot Tables. Calculate digital center distribution by region. |
| **Research grounding** | **AI-Driven Verify.** **RAG (Retrieval-Augmented Generation)** — the consensus architecture for any AI touching published content. Introduce here, when students are ready. | **Multi-model is standard** — no serious newsroom uses one LLM. Ippen evaluated 200+. Different tools for different pipeline steps = professional practice. |
| | | |
| | **Aftonbladet election chatbot:** 150K questions, zero hallucinations. RAG with ~100 curated sources. | |
| | **Particle news:** Multi-source requirement (3 articles, 2 publishers min) + bias meter. | |
| | **SZ expert-in-the-loop:** Article *authors* verify AI summaries, not generic reviewers. | |
| | Key distinction: **"human in-the-loop" vs "human on-the-loop"** — how much oversight is enough? | |
| | **"Hallucination is a feature, not a bug"** — inherent to LLM generation. Not being fixed. This is *why* verification systems matter. |
| | **Algorithmic accountability as verification skill.** Verification doesn't just apply to data — it applies to AI tools themselves. Diakopoulos framework: 4 audit angles — discrimination/unfairness, errors/mistakes, legal/social norm violations, human misuse. ProPublica COMPAS audit (revisited from Day 2): auditing AI *is* a journalism skill. AlgorithmWatch: 6M Google searches from 4K+ users. Auditing AI = the same verification instinct applied to systems, not just datasets. | |
| **Interactive** | **Morning quiz (5 min):** Recall from Days 1-3 (cleaning, parsing palette, "Why Before How"). **Critical Question:** "What does this algorithm assume?" (1 min). | **"Guess the Process" (15 min):** Show 2-3 published investigations. Students reverse-engineer: What was the starting question? Which parsing approach? Where was AI, where human? Examples: iTromsoe fisheries, Der Spiegel gender audit, NYT recordings investigation. |
| **Artifact** | Verification Automation Skill doc | Pivot Table Skill doc |

---

## Day 5 — Define → ... → Clean → Analyze → **Present** (new)

| Section | Morning (returning steps) | Afternoon (new step) |
|---------|--------------------------|----------------------|
| **Steps** | Define (5th), Find (5th), Get (5th), Verify (4th), **Clean (3rd, assistant)**, Analyze (2nd) | **Present (1st)** |
| **AI usage cap** | Define: Q&A. Find/Get/Verify: fast. Clean: **assistant**. Analyze: Q&A | docs |
| **Theory** | Clean reaches assistant cap: AI-driven automation of the step that was "The Wall" on Day 3. | Why "presentation" not "visualization" — message > strict representation; data viz relevant for limited angles only; data may be just one step of investigation, not an end in itself. Presentation ≠ chart: in Bogotá, journalists used WhatsApp voice notes from residents about neighborhood trees — the "data" was cultural memory, the "visualization" was an interactive map with audio (Leaflet + SoundCloud + StoryMapJS). In the Philippines, crash data led to a community forum that got pedestrian lanes painted. In India, Land Conflict Watch built a searchable database as civic infrastructure. The output is whatever serves the story and its audience. The Triad: les données (simple visualizations), la mise en forme (attract attention, mark minds), le message (storytelling > details, infographics). Cartography as a presentation form. Analysis blind spots (fétichisation, sur-interprétation, non-interprétation). |
| **Project** | CLI agents (Terminal + `uv`) automate Day 3's cleaning task. What took an afternoon is now 20-30 minutes. Analyze (Q&A): cross-analysis — merge digital divide data with population density to test rural service hypothesis. | Datawrapper for final visualization. Portfolio assembly. |
| **Research grounding** | **Prototype-to-production gap** — "the industry's central operational challenge." What students built = prototype. iTromsoe's GIN took sustained engineering to scale from 1 to 36 newspapers. Honest framing for the Skill Library. | "The article will die, should die" (Schibsted CTO) — but the *story* persists. Students build stories, not articles. |
| | | Contrasting formats from newsrooms: Aftonbladet chatbot (conversational), SZ easy-language slider (adaptive complexity), Times of India Signals (recommendation-driven, 85% CTR increase from old articles). |
| | | Good Tape: internal tool → $3M business → exit. The Skill Library is a reusable asset, same kind of thing. |
| **Interactive** | **Morning quiz (5 min):** "Final Showdown" — recall from Days 1-4 (RAG, analysis method, pivot tables, human-in/on-the-loop). **Critical Question:** "Who is the audience, and what do they need?" (1 min). | **"Where's the Human?" spectrum (5 min, optional):** Tasks read aloud ("writing a headline," "choosing what to cover," "cleaning 10K addresses," "verifying a source's identity"). Students position from "fully automatable" to "irreducibly human." |
| **Artifact** | CLI Automation Skill doc | **Final Portfolio:** Story (Datawrapper) + Horizon Table (final dataset) + Skill Library (all skill docs) |

---

## Week Arc

```
Day 1: Foundation — pipeline exists, Google Sheets as tool environment, docs cap only
Day 2: First AI contact — NotebookLM assists Find/Get, verification as journalism practice
Day 3: Find/Get unlocked (parsing palette) → then The Wall (manual Clean)
Day 4: Verify unlocked (RAG, verification systems) → then first Analyze
Day 5: Clean unlocked (CLI automation) → then the story (Present + portfolio)
```

Days 3-5: each morning has one "unlock" (assistant cap) moment. Every afternoon introduces the next step fresh (docs cap).

---

## Prevalence-Driven Concepts (Must-Name)

| Concept | When | Why |
|---------|------|-----|
| **"Why Before How"** | Day 1 (Horizon Table), reinforce Day 3 | Most repeated principle, 42 episodes |
| **80/20 literacy divide** | Day 1 quiz | Students joining the 20% |
| **Whisper** | Day 1 or 2, brief mention | "The single undisputed AI productivity win" |
| **RAG** | Day 4 morning (Verify assistant) | Consensus architecture |
| **"Hallucination is a feature"** | Day 4 morning | Reframes verification as structural |
| **Multi-model approach** | Day 4 afternoon | No org uses single LLM |
| **Prototype-to-production gap** | Day 5 morning | Honest framing for portfolio |

---

## Conspicuous Absences Worth Naming (Day 5 wrap-up, 2 min)

The industry isn't talking about:
- Environmental cost of AI — near-total silence across 42 episodes
- Freelance/independent journalists — invisible in discourse
- Non-English language challenges — acknowledged but unsolved; Cuba chapter shows Spanish-language data journalism faces fragmented/unavailable government data as a structural barrier, not just a language model issue
- Revenue model innovation — more anxiety than solutions
- Indigenous data sovereignty — Te Mana Raraunga (Maori) and FNIGC (First Nations) have formal protocols (OCAP principles) for data governance, entirely absent from Western DDJ discourse. Directly relevant: France has overseas territories, former colonies, and unresolved data governance questions
- Resource asymmetry — the best data journalism happens at well-resourced outlets (NYT, ProPublica, Guardian) while the need is greatest at local/community level. The handbook's recurring finding, and a structural challenge for French regional press

---

## The Skill and the Task

The curriculum introduces a distinction between the **artifact** and the **process** that underpins all AI-assisted work:

**The Skill (Artifact):** A standardized document (SKILL.md format) that packages journalistic expertise into a reusable file. Contains instructions, constraints, and metadata that allow an AI to perform a specific category of work. Students build their Skill Library across the week — each afternoon's new step produces a new Skill doc.

**The Task (Process):** The journalistic workflow documented *within* a skill. A Task is a single, bounded unit of work belonging to one pipeline stage. It documents:
- **Objective & Context:** The specific goal and source material boundaries.
- **Output Shape:** The exact Horizon Table schema — the minimum dataset required.
- **Verifiability Rules:** Mandatory "anchors" (direct quotes, page numbers, source URLs) that force falsifiable results.
- **Process Checklist:** The "chain of thought" steps the AI must follow to prevent shortcuts.

The Skill/Task distinction teaches students that AI assistance is engineering, not magic: you design the constraints, specify the output, and build in verification.

---

## Sources

### From 2024-2025 IJBA Course (Slides & Exercises)
The following frameworks are inherited from previous years of teaching:
- 7-step data pipeline (Define → Find → Get → Verify → Clean → Analyze → Present) — School of Data / Open Knowledge Foundation
- Tabular Thinking and the Horizon Table (introduced 2024-2025)
- Lombion quality schema (structuration × representativity → 4 quadrants) — Cédric Lombion / Open Knowledge Foundation
- History timeline: Nightingale 1855, Minard 1869, Mayer 1967, Jones 1968, Burnham 1977, Morin/Tasker 1985, Dedman 1988, Rogers 2008
- 3 objectives (compile, analyze, make available), 4 applications (illustration, investigation, personalized info, decryption)
- Open Data revolution timeline (CADA 1978 → PSI 2003 → Etalab 2011 → Loi République Numérique 2016)
- The Triad: les données, la mise en forme, le message
- 3 types of analysis (descriptive, inferential, predictive)
- Verification 3 enjeux (fiabilité, exhaustivité, qualité)
- Analysis blind spots (fétichisation, sur-interprétation, non-interprétation)
- Analysis method (theme → hypotheses → questions → reformulated with data columns)
- Démarche — two starting points (from dataset OR from question)
- Data as "structured representations"
- Tool stack: Google Sheets, IMPORTHTML, Tabula, OpenRefine, Datawrapper, Pivot Tables
- Project examples: class demographics, French Presidents table, maternity ward medicalization

### From Newsroom Robots Podcast Analysis (42 episodes, Jan 2024 – Jan 2026)
All Research Grounding rows draw from this corpus unless otherwise noted:
- "Why Before How" — most repeated principle (cross_analysis §4 Scale, §3 Synthesis)
- 80/20 literacy divide — Daudens split (cross_analysis §5 Maturity Model, codebook T05.2)
- Whisper as productivity win (codebook T01.5 Automation Paradox)
- RAG as consensus architecture (cross_analysis §5, codebook T04.2)
- "Hallucination is a feature, not a bug" (codebook T04.4)
- Multi-model approach — Ippen 200+ models (codebook T04.1)
- Prototype-to-production gap (cross_analysis §1-2, codebook T11.2)
- Document Parsing Palette — curriculum synthesis from: NYT Echo semantic search, iTromsoe entity extraction, Der Spiegel/BBC summarization (codebook T04.2)
- NotebookLM industry usage (codebook T08.3)
- Data infrastructure as binding constraint — Delfi 8 years, Times of India "banking-grade" (cross_analysis §2)
- Human-in-the-loop vs human-on-the-loop (cross_analysis §7, codebook T03.4)
- Expert-in-the-loop / SZ model (codebook T03.4)
- Good Tape: Whisper prototype → $3M → exit (codebook T09.1, T11)
- Aftonbladet chatbot: 150K questions, zero hallucinations (codebook T04.2)
- iTromsoe GIN: fisheries investigation, scale to 36 newspapers (codebook T11)
- Schibsted CTO: "the article will die, should die" (codebook T08)
- Times of India Signals: 85% CTR increase from old articles (codebook T08)
- SZ easy-language slider (codebook T08)
- Conspicuous absences: environmental silence, freelance invisibility, revenue anxiety (cross_analysis §6)

### From Data Journalism Handbook 2 (Amsterdam University Press, 2021)
Added to enrich theory sections with critical frameworks and Global South perspectives:
- Critical Data Practice framing — Anderson, "Genealogies of Data Journalism" (ch. 07-situating): epistemological eras, overclaiming certainty
- "Who is missing from the data?" — D'Ignazio, "Data Journalism: What's Feminism Got to Do With I.T.?" (ch. 01-doing-issues): feminicides, police killings, maternal mortality undercounting
- Indigenous data sovereignty — Kukutai & Taylor (ch. 01-doing-issues): Te Mana Raraunga, FNIGC, OCAP principles
- "Building your own dataset" typology — UK knife crime FOI (ch. 02-assembling), Turkish worker deaths (ch. 02-assembling), Land Conflict Watch India (ch. 02-assembling), La Nación Vozdata crowdsourcing (ch. 02-assembling), Postdata.club Cuba (ch. 02-assembling)
- Reinhart-Rogoff Excel error — "Accounting for Methods" (ch. 03-working-with-data)
- COMPAS / ProPublica Machine Bias — Diakopoulos, "The Algorithms Beat" (ch. 04-investigating)
- Algorithmic accountability: 4 audit angles — Diakopoulos (ch. 04-investigating)
- Reproducibility via Jupyter Notebooks — Global Witness Papua New Guinea (ch. 03-working-with-data)
- OpenRefine for cleaning — Philippines crash mapping (ch. 03-working-with-data)
- Collaborative assembly models — El Diario/El Faro 68M trade records (ch. 02-assembling)
- "Narrating a Number" — interrogating quantification (ch. 01-doing-issues)
- Bogotá "Multiplying Memories" — Leaflet + SoundCloud + WhatsApp voice notes (ch. 01-doing-issues)
- Philippines crash mapping → community forum → pedestrian lanes (ch. 01-doing-issues)
- Land Conflict Watch searchable database as civic infrastructure (ch. 01-doing-issues)
- Teaching Data Journalism — Phillips (ch. 06-learning): fundamentals first, project-based, flipped classroom
- Resource asymmetry finding (recurring across handbook chapters)
