# Source Registry — Data Pipeline Canon Project

_Last updated: 2026-02-24 (v11 — improved legend documentation)_
_Status: T6 — VERIFY phase: COMPLETE_

## Screening Protocol

**Inclusion criteria** (must meet ALL):
1. About journalism, news, or civic data practice
2. Contains methodological content (not just case studies or theory)
3. Published work (book, article, guide, curriculum)
4. Published 2012 or later — applies to the **edition acquired**, not first edition
5. Available in digital format (PDF, EPUB, or web). Paperback-only titles are noted but excluded from analysis.

**Expanded criteria (v6)** — sources in these adjacent domains are included when they contain transferable methodology applicable to the data journalism pipeline:
- Verification and fact-checking methodology (pipeline stage: Verify)
- Investigative research methods (pipeline stages: Define, Find, Get)
- Data ethics and production methodology
- Digital journalism workflow methodology (broader than data-only)

**Exclusion criteria** (any one disqualifies):
- Purely about OSINT/intelligence
- Purely about data visualization with no upstream methodology
- Tool-specific manual with no transferable methodology
- Purely theoretical / critical studies with no practitioner methodology

**Screening fields**: title, TOC/chapter list, abstract/description, author background

---

## Registry

Legend:

**included** — screening decision (does this source belong in the corpus?):
- `yes` = passes all inclusion criteria → should be acquired and processed
- `no` = excluded → last column explains why
- `maybe` = borderline, needs user review (all resolved as of v10)
- `meta` = meta-resource (reading list, syllabus, portal — useful for finding sources, not a source itself)

**status** — how far this source has progressed through the pipeline:
- `identified` → found but not yet screened against criteria
- `screened` → inclusion decision made. If `included=yes` but still `screened`, the source was **not acquired** (purchase barrier, paywall, or unavailable)
- `acquired` → file obtained and saved to `sources/`. If `included=no`, file is in `sources/_rejected/`
- `converted` → text extracted to `.md` output, listed in `convert-manifest.csv`
- `extracted` → LLM extraction complete (T9)

**Common combinations:**
| included | status | meaning |
|----------|--------|---------|
| yes | converted | in corpus, ready for analysis |
| yes | screened | passed screening but **not acquired** — gap in corpus |
| no | screened | excluded during screening, never obtained |
| no | acquired | obtained then excluded after deeper review — file in `_rejected/` |
| meta | screened | reference resource, not a corpus source |

**last column** (`exclusion_reason`): overloaded field. Contains:
- For `included=no`: reason for exclusion
- For `included=yes` + `status=converted`: file path in `sources/`
- For `included=yes` + `status=screened`: why not acquired (e.g. "NOT ACQUIRED — Kindle available")

### File locations
- All files: `sources/{lang}/{number}-{slug}.{ext}` (e.g., `en/07-ddj-handbook-1.pdf`)
- Git-cloned repos: `sources/{lang}/{number}-{slug}/` directory
- NICAR tipsheets: `sources/en/nicar/`
- Excluded-but-acquired: `sources/_rejected/`
- Cross-references: `.md` file with pointers to actual content elsewhere

### Books — English

| # | title | author | year | lang | type | access | found_via | status | included | exclusion_reason |
|---|-------|--------|------|------|------|--------|-----------|--------|----------|------------------|
| 1 | Precision Journalism: A Reporter's Introduction to Social Science Methods | Philip Meyer | 1973 | EN | book | purchase | DDJ reading lists | screened | no | pre-2012 |
| 2 | Computer-Assisted Reporting: A Practical Guide | Brant Houston | 1996 | EN | book | purchase | NICAR/IRE | screened | no | pre-2012 |
| 3 | Numbers in the Newsroom: Using Math and Statistics in News | Sarah Cohen | 2001 | EN | guide | purchase (~$10) | IRE | screened | no | pre-2012 |
| 4 | Computer-Assisted Research: Information Strategies and Tools for Journalists | Nora Paul, Kathleen Hansen | 2005 | EN | book | purchase | DDJ syllabi | screened | no | pre-2012 |
| 5 | Computer-Assisted Reporting: A Comprehensive Primer | Fred Vallance-Jones, David McKie | 2009 | EN | book | purchase | DDJ syllabi | screened | no | pre-2012 |
| 6 | The Functional Art | Alberto Cairo | 2012 | EN | book | purchase | DDJ reading lists | screened | no | visualization only, no upstream methodology |
| 7 | The Data Journalism Handbook 1 | Jonathan Gray, Liliana Bounegru, Lucy Chambers (eds.) | 2012 | EN | handbook | open access (CC) | canonical | converted | yes | `en/07-ddj-handbook-1.pdf` |
| 8 | Facts Are Sacred | Simon Rogers | 2013 | EN | book | purchase | DDJ reading lists | converted | yes | `en/08-facts-are-sacred.epub` |
| 9 | Scraping for Journalists | Paul Bradshaw | 2013 | EN | ebook | purchase | DDJ reading lists | screened | no | Old edition (2013), not worth purchasing; superseded by newer tools coverage |
| 10 | Finding Stories in Spreadsheets | Paul Bradshaw | 2015 | EN | ebook | purchase | DDJ reading lists | converted | yes | `en/10-finding-stories-spreadsheets.epub` |
| 11 | Data Literacy: A User's Guide | David Herzog | 2015 | EN | book | purchase | DDJ syllabi | converted | yes | `en/11-data-literacy.pdf` |
| 12 | The Truthful Art | Alberto Cairo | 2016 | EN | book | purchase | DDJ reading lists | screened | no | visualization methodology only |
| 13 | The Curious Journalist's Guide to Data | Jonathan Stray | 2016 | EN | book | open access (CJR/Tow) | DDJ reading lists | converted | yes | `en/13-curious-journalists-guide-to-data.pdf` |
| 14 | The WSJ Guide to Information Graphics | Dona Wong | 2010 | EN | book | purchase | DDJ reading lists | screened | no | visualization/presentation standards only |
| 15 | Investigative Reporter's Handbook (6th ed.) | Brant Houston, Mark Horvit, IRE | 2020 | EN | book | purchase | IRE | converted | yes | `en/15-investigative-reporters-handbook-6e.epub` |
| 16 | Data for Journalists (5th ed.) | Brant Houston | 2018 | EN | book | purchase (Routledge) | IRE | screened | no | No digital edition found; purchase barrier (fails criterion #5 in practice) |
| 17 | The Data Journalist: Getting the Story | Fred Vallance-Jones, David McKie | 2017 | EN | book | purchase (Oxford UP) | DDJ syllabi | screened | no | paperback only, no digital edition (fails criterion #5) |
| 18 | Data Journalism in the Global South | Bruce Mutsvairo et al. (eds.) | 2019 | EN | book | purchase | academic search | screened | no | case study collection, not methodology |
| 19 | Artificial Unintelligence | Meredith Broussard | 2018 | EN | book | purchase (MIT Press) | DDJ reading lists | screened | no | critical theory, not methodology |
| 20 | More Than a Glitch | Meredith Broussard | 2023 | EN | book | purchase (MIT Press) | DDJ reading lists | screened | no | algorithmic bias theory, not DJ methodology |
| 21 | Digital Investigative Journalism | Oliver Hahn, Florian Stalph (eds.) | 2018 | EN | book | purchase (Palgrave) | academic search | converted | yes | `en/21-digital-investigative-journalism.pdf` |
| 22 | The Data Journalism Handbook 2 | Liliana Bounegru, Jonathan Gray (eds.) | 2021 | EN | handbook | open access (Amsterdam UP, CC) | canonical | converted | yes | `en/22-ddj-handbook-2.pdf` + full text in `research/ddj-handbook-2/` |
| 23 | The Data Storytelling Workbook | Anna Feigenbaum, Aria Alamalhodaei | 2020 | EN | book | purchase | DDJ reading lists | converted | yes | `en/23-data-storytelling-workbook.pdf` |
| 24 | Data + Journalism: A Story-Driven Approach | Mike Reilley, Samantha Sunne | 2022 | EN | textbook | purchase (Routledge) | DDJ syllabi | converted | yes | `en/24-data-plus-journalism.epub` |
| 25 | Journalism in the Data Age | Jingrong Tong | 2022 | EN | book | purchase (SAGE) | academic search | screened | no | Theoretical; not relevant to practitioner methodology |
| 26 | Handbuch Daten und KI im Journalismus | Christina Elmer, Lorenz Matzat (eds.) | 2024 | DE | book | purchase (Herbert von Halem) | recent publications | screened | no | GERMAN ONLY — no English edition. PDF ebook exists in DE. Outside corpus languages (EN/FR/ES/PT). |
| 27 | CHART: Designing Creative Data Visualizations | Nadieh Bremer | 2024 | EN | book | purchase | DDJ reading lists | screened | no | creative visualization, no upstream methodology |
| 28 | Learning to See Data | Ben Jones | 2020 | EN | book | purchase | DDJ reading lists | screened | no | visual literacy only |
| 29 | Presenting Data Effectively | Stephanie Evergreen | 2017 | EN | book | purchase | DDJ reading lists | screened | no | presentation only |
| 30 | Data Visualisation: A Handbook for Data Driven Design | Andy Kirk | 2016 | EN | book | purchase | DDJ reading lists | screened | no | visualization only |
| 31 | The Art of Insight | Alberto Cairo | 2023 | EN | book | purchase | DDJ reading lists | screened | no | visualization thinking only |
| 32 | I Am a Book. I Am a Portal to the Universe | Stefanie Posavec, Miriam Quick | 2021 | EN | book | purchase | DDJ reading lists | screened | no | data physicalisation art, not journalism methodology |
| 33 | Data Journalism: A Quick & Practical Guide | Rob Wells | ongoing | EN | online book | open access (bookdown.org) | DDJ syllabi | converted | yes | GitHub repo cloned (profrobwells/datajournalismbook) |
| 34 | Data Journalism with R and the Tidyverse | Matt Waite | ongoing | EN | online book | open access (GitHub) | DDJ syllabi | screened | no | tool-specific R tutorial |
| 35 | Effective Data Visualization | Stephanie Evergreen | 2019 | EN | book | purchase | DDJ reading lists | screened | no | chart selection only |
| 36 | Data at Work | Jorge Camões | 2016 | EN | book | purchase | DDJ reading lists | screened | no | Excel charting manual |
| 37 | The Art and Science of Data-Driven Journalism | Alexander Howard | 2014 | EN | report | open access (Tow Center) | Tow Center | converted | yes | `en/37-art-science-data-driven-journalism.pdf` |
| 38 | Teaching Data and Computational Journalism | Charles Berret, Cheryl Phillips | 2016 | EN | report | open access (Columbia) | Columbia/DDJ syllabi | converted | yes | `en/38-teaching-data-computational-journalism.pdf` |
| 39 | Web Scraping with Python | Ryan Mitchell | 2015 | EN | book | purchase (O'Reilly) | DDJ reading lists | screened | no | tool-specific manual (Python scraping) |
| 40 | Interactive Data Visualization for the Web | Scott Murray | 2013 | EN | book | purchase (O'Reilly) | DDJ reading lists | screened | no | D3.js manual |
| 41 | The Journalist's Toolbox Handbook | Mike Reilley | 2024 | EN | book | purchase (Routledge) | recent publications | converted | yes | `en/41-journalists-toolbox-handbook.epub` |
| 42 | Data Journalism Heist | Paul Bradshaw | 2013 | EN | ebook | purchase | DDJ reading lists | converted | yes | `en/42-data-journalism-heist.epub` |
| 43 | Data Journalism: Inside the Global Future | Tom Felle, John Mair (eds.) | 2015 | EN | book | purchase (Abramis) | DDJ reading lists | screened | no | paperback only, no digital edition (fails criterion #5) |
| 44 | Mapping for Stories | Jennifer LaFleur, David Herzog, Charles Minshew | 2017 | EN | guide | IRE/NICAR | IRE | screened | no | spiral-bound only, no digital edition (fails criterion #5) |
| 127 | Modern Investigative Journalism: A Comprehensive Curriculum Based on the ARIJ Method | Mark Lee Hunter, Luuk Sengers, Marcus Lindemann | 2019 | EN | curriculum | open access (storybasedinquiry.com) | user reference | converted | yes | `en/127-modern-investigative-journalism-arij.pdf` |
| 128 | A Model for the 21st Century Newsroom | Paul Bradshaw | 2007 (ebook 2012) | EN | ebook/blog | open access (onlinejournalismblog.com) | user reference | converted | yes | `en/128-model-21st-century-newsroom.txt` |
| 129 | Statistics for Journalists | Connie St Louis (CIJ) | 2011 | EN | guide | open access (PDF) | statistics+journalism search | screened | no | pre-2012 |
| 130 | Math Tools for Journalists (3rd ed.) | Kathleen Woodruff Wickham | 2003 | EN | book | purchase | statistics+journalism search | screened | no | pre-2012 |
| 131 | Making Sense of Statistics | Sense about Science + RSS | n.d. | EN | guide | open access (PDF, fullfact.org) | statistics+journalism search | converted | yes | `en/131-making-sense-of-statistics.pdf` |
| 132 | Digging Deeper: A Canadian Reporter's Research Guide | Robert Cribb, Dean Jobb, David McKie, Fred Vallance-Jones | 3rd ed. | EN | book | purchase | user discovery | converted | yes | `en/132-digging-deeper.pdf` |
| 133 | Digital Technology and Journalism: An International Comparative Perspective | Jingrong Tong, Shih-Hung Lo (eds.) | 2017 | EN | book | purchase (Springer) | user discovery | acquired | no | Academic/theoretical edited volume; sociological case studies, no transferable methodology. `_rejected/133-digital-technology-journalism.epub` |
| 134 | Journalism in an Era of Big Data: Cases, Concepts, and Critiques | Seth C. Lewis (ed.) | 2019 | EN | book | purchase (Routledge) | user discovery | acquired | no | Academic essay collection; theory-heavy, no practitioner workflows. `_rejected/134-journalism-era-big-data.epub` |
| 135 | The Online Journalism Handbook: Skills to Survive and Thrive in the Digital Age | Paul Bradshaw | 3rd ed., 2023 | EN | book | purchase (Routledge) | user discovery | converted | yes | `en/135-online-journalism-handbook.epub` |
| 136 | The Power of Data: Data Journalism Production and Ethics | Zhang Chao | 2023 | EN | book | purchase (Routledge) | user discovery | converted | yes | `en/136-power-of-data.epub` |
| 137 | The Watchdog Still Barks: How Accountability Reporting Evolved for the Digital Age | Beth Knobel | 2018 | EN | book | purchase (Fordham UP) | user discovery | acquired | no | Content analysis of accountability reporting quantity; no investigative methods or workflows described. `_rejected/137-watchdog-still-barks.pdf` |
| 138 | Verification Handbook for Investigative Reporting | Craig Silverman (ed.), EJC | 2014 | EN | handbook | open access (CC) | user discovery | converted | yes | `en/138-verification-handbook.pdf` |
| 139 | Best Practices for Data Journalism | Kuang Keng Kuek Ser (MDIF) | n.d. | EN | guide | open access (PDF) | user discovery | converted | yes | `en/139-best-practices-data-journalism.pdf`. Practitioner guide covering full DJ workflow: team setup, acquisition, cleaning, bulletproofing, visualization. |
| 140 | Data for Journalism: Between Transparency and Accountability | Jingrong Tong | 2022 | EN | book | purchase (Routledge) | user discovery | converted | yes | `en/140-data-for-journalism-tong.pdf` |
| 141 | Apostles of Certainty: Data Journalism and the Politics of Doubt | C.W. Anderson | 2018 | EN | book | purchase (OUP) | user discovery | acquired | no | Historical/epistemological study of data journalism across 4 eras; no practitioner methodology. `_rejected/apostles-of-certainty.pdf` |
| 151 | Nerd Journalism: How Data and Digital Technology Transformed News Graphics | Alberto Cairo | 2017 | EN | dissertation | open access (UOC) | user discovery | acquired | no | PhD dissertation on news graphics history; visualization-focused, no upstream methodology. `_rejected/nerd-journalism-cairo.pdf` |

### Expansion Search — Verification & Fact-Checking

| # | title | author | year | lang | type | access | found_via | status | included | exclusion_reason |
|---|-------|--------|------|------|------|--------|-----------|--------|----------|------------------|
| 142 | Verification Handbook 3: For Disinformation & Media Manipulation | Craig Silverman (ed.), EJC | 2020 | EN | handbook | open access (datajournalism.com) | expansion search A | converted | yes | `en/142-verification-handbook-3.pdf` |
| 143 | Verification Handbook 2: A Definitive Guide to Verifying Digital Content for Emergency Coverage | Craig Silverman (ed.), EJC | 2015 | EN | handbook | open access (PDF) | expansion search A | converted | yes | `en/143-verification-handbook-2.pdf` |
| 144 | Exposing the Invisible: The Kit | Tactical Tech | 2020+ | EN | toolkit | open access (CC) | expansion search A | converted | yes | `en/144-exposing-the-invisible-kit.pdf` |

### Expansion Search — Investigative Research Methods

| # | title | author | year | lang | type | access | found_via | status | included | exclusion_reason |
|---|-------|--------|------|------|------|--------|-----------|--------|----------|------------------|
| 145 | Follow the Money: A Digital Guide for Tracking Corruption | Paul Radu / OCCRP via Tactical Tech | 2019 | EN | handbook | open access | expansion search B | screened | no | Unavailable — archive.org inaccessible, no alternative source found |
| 146 | Al Jazeera Investigative Journalism Handbook | Al Jazeera Media Institute | 2020 | EN | handbook | open access (PDF) | expansion search B | converted | yes | `en/146-aljazeera-investigative-handbook.pdf` |

### Expansion Search — Data Ethics & Algorithmic Accountability

| # | title | author | year | lang | type | access | found_via | status | included | exclusion_reason |
|---|-------|--------|------|------|------|--------|-----------|--------|----------|------------------|
| 147 | Responsible Data Handbook | The Engine Room | 2014 (updated) | EN | handbook | open access (CC) | expansion search C | converted | yes | `en/147-responsible-data-handbook.pdf` |
| 148 | Algorithmic Accountability Reporting | Nicholas Diakopoulos, Tow Center / CJR | 2014 | EN | report | open access | expansion search C | converted | yes | `en/148-algorithmic-accountability-diakopoulos.md` (full text, ~62KB) |
| 149 | UNESCO Reporting on Artificial Intelligence: Handbook for Journalism Educators | Maarit Jaakkola (ed.), UNESCO | 2023 | EN | handbook | open access (PDF) | expansion search C | converted | yes | `en/149-unesco-reporting-on-ai.pdf` |
| 150 | Amnesty International Algorithmic Accountability Toolkit | Amnesty International | 2025 | EN | toolkit | open access | expansion search C | converted | yes | `en/150-amnesty-algorithmic-accountability-toolkit.md` (full text, ~108KB) |

### Books — French

| # | title | author | year | lang | type | access | found_via | status | included | exclusion_reason |
|---|-------|--------|------|------|------|--------|-----------|--------|----------|------------------|
| 45 | Guide du datajournalisme | Jonathan Gray et al.; dir. fr. Nicolas Kayser-Bril | 2013 | FR | book | purchase (Eyrolles) / open access | canonical | converted | yes | GitHub repo cloned (jplusplus/guide-du-datajournalisme) |
| 46 | Imposture à temps complet | Nicolas Kayser-Bril | 2022 | FR | book | purchase | DDJ reading lists | screened | no | not about DDJ methodology |
| 47 | Voracisme | Nicolas Kayser-Bril | 2024 | FR | book | purchase | DDJ reading lists | screened | no | data-driven investigation (case study), not methodology |
| 48 | La Guerre du gras | Nicolas Kayser-Bril | n.d. | FR | book | purchase | DDJ reading lists | screened | no | data-driven investigation (case study), not methodology |

### Books — Spanish

| # | title | author | year | lang | type | access | found_via | status | included | exclusion_reason |
|---|-------|--------|------|------|------|--------|-----------|--------|----------|------------------|
| 49 | Herramientas digitales para periodistas (2a ed.) | Sandra Crucianelli | 2010 | ES | book | open access (Knight Center PDF) | ICFJ/Knight Center | screened | no | pre-2012 |
| 50 | ¿Qué es el periodismo de datos? | Sandra Crucianelli | 2013 | ES | guide | open access (Issuu) | ICFJ | screened | yes | |
| 51 | Manual de Periodismo de Datos Iberoamericano | Felipe Perry, Miguel Paz (eds.) | 2014 | ES | handbook | open access (CC BY-SA) | canonical | converted | yes | Primary site down; intro + first chapters extracted from Scribd (187pp). Full PDF on Scribd |
| 52 | Big Data y periodismo en la sociedad red | Carlos Elías | 2015 | ES | book | purchase | academic search | acquired | yes | `es/52-big-data-periodismo.pdf` |
| 53 | Periodismo de datos: Un golpe rápido | collective | n.d. | ES | ebook | open access (Leanpub) | web search | screened | no | Spanish translation of Bradshaw's Data Journalism Heist (#42), already in corpus |
| 54 | Guía de Buenas Prácticas para Periodistas de Datos | Lorena R. Romero-Domínguez | n.d. | ES | guide | open access | academic search | screened | yes | |
| 55 | Manual de Periodismo de Datos (Spanish DDJ Handbook 1) | La Nación Data | 2013 | ES | handbook | open access | canonical | screened | yes | |
| 56 | Guía de periodismo de datos | David Hidalgo, Fabiola Torres (Ojo Público) | n.d. | ES | guide | open access | GIJN | screened | yes | |

### Books — Portuguese

| # | title | author | year | lang | type | access | found_via | status | included | exclusion_reason |
|---|-------|--------|------|------|------|--------|-----------|--------|----------|------------------|
| 57 | Manual de Jornalismo de Dados (Portuguese DDJ Handbook 1) | Abraji | 2014 | PT | handbook | open access | canonical | screened | yes | |
| 58 | Manual de Jornalismo de Dados 2 (Portuguese DDJ Handbook 2) | Abraji / Escola de Dados | 2021 | PT | handbook | open access | canonical | converted | yes | `pt/58-manual-jornalismo-dados-2.md` (TOC); full EN text in `research/ddj-handbook-2/` |
| 59 | Jornalismo de Dados: Conceitos, Rotas e Estrutura Produtiva | Alexsandro Ribeiro | 2018 | PT | book | purchase | academic search | screened | yes | |
| 60 | Leitura e Interpretação de Dados no Jornalismo | various | n.d. | PT | book | purchase | academic search | screened | yes | |
| 61 | Os Elementos de Transparência no Jornalismo Guiado por Dados | academic | n.d. | PT | book | purchase | academic search | acquired | yes | `pt/61-elementos-transparencia.pdf` |
| 62 | Il potere dei dati | n.d. | n.d. | IT | book | purchase | web search | screened | no | Italian — outside language scope |

### Academic Articles

| # | title | author | year | lang | type | access | found_via | status | included | exclusion_reason |
|---|-------|--------|------|------|------|--------|-----------|--------|----------|------------------|
| 63 | Data Journalism Research: Studying a Maturing Field | Stalph, Hahn et al. | 2019 | EN | article | paywall (T&F) | academic search | acquired | yes | `en/63-dj-research-maturing-field.pdf` |
| 64 | The Datafication of Data Journalism Scholarship | Ausserhofer et al. | 2017 | EN | article | open access | academic search | screened | no | meta-analysis of DJ research, not methodology |
| 65 | Systematic Literature Review on Data Journalism in Viz Research and Journalism Studies | Francesca Morini | 2025 | EN | article | paywall (SAGE) | academic search | screened | no | SLR (meta-research), not methodology |
| 66 | Teaching Data Journalism: A Systematic Review | various | 2022 | EN | article | paywall (T&F) | academic search | acquired | yes | `en/66-teaching-dj-systematic-review.pdf` |
| 67 | Data Journalism: A Systematic Literature Review | Özlem Erkmen | 2023 | EN | article | paywall (T&F) | academic search | acquired | yes | `en/67-dj-systematic-literature-review.pdf` |
| 68 | Data Journalism and Journalism Education: A Scoping Review | Serwornoo et al. | 2024 | EN | article | paywall (SAGE) | academic search | screened | yes | highlights DJ practices |
| 69 | Open Data Journalism: A Domain Mapping Review | various | 2023 | EN | article | open access (ACM) | academic search | screened | yes | highlights DJ practices |
| 70 | Preserving Data Journalism: A Systematic Literature Review | various | 2022 | EN | article | open access | academic search | screened | no | archiving/preservation, not methodology |
| 71 | Data Science, ML and Big Data in Digital Journalism: A Survey | various | 2023 | EN | article | paywall (Elsevier) | academic search | acquired | yes | `en/71-data-science-ml-digital-journalism.pdf` |
| 72 | Data Journalism in Africa: A Systematic Review | various | 2024 | EN | article | open access | academic search | screened | yes | highlights DJ practices |
| 73 | Teaching Data Journalism in a World of Technology Companies | MIT | 2021 | EN | article | open access (MIT) | academic search | screened | yes | highlights DJ practices |
| 74 | Teaching Data Journalism: Insights for Indian Journalism Education | Kashyap, Bhaskaran | 2020 | EN | article | paywall (SAGE) | academic search | acquired | yes | `en/74-teaching-dj-indian-journalism.pdf` |
| 75 | Philip Meyer, the Outsider who Created Precision Journalism | various | 2017 | EN | article | open access | academic search | screened | no | historical analysis, not methodology |
| 76 | Data Journalism, Digital Verification and AI | various | n.d. | EN | article | open access | academic search | converted | yes | PDF downloaded from VIEW Journal |
| 77 | Use Cases of AI and Automation Support in Investigative Journalism | various | 2025 | EN | article | open access (arXiv) | academic search | screened | yes | AI in investigative journalism |
| 78 | Data Journalism and the Law | various | n.d. | EN | article | open access (CJR/Tow) | Tow Center | screened | no | legal issues, not methodology |
| 152 | Data Journalism: Lessons Learned While Designing an Interdisciplinary Service Course | Christopher Plaue, Lindsey R. Cook | 2015 | EN | article | open access (ACM/SIGCSE) | user discovery | acquired | yes | `en/152-dj-lessons-interdisciplinary-course.pdf`. DJ course design: data acquisition, cleaning, programming, visualization. |
| 153 | Interdisciplinary Learning in Journalism: A Hong Kong Study of Data Journalism Education | Lingzi Zhu, Ying Roselyn Du | 2018 | EN | article | paywall (SAGE) | user discovery | acquired | yes | `en/153-interdisciplinary-learning-journalism-hk.pdf`. Survey of DJ training outcomes across disciplines. |
| 154 | A DIY, Project-based Approach to Teaching Data Journalism | Caroline Graham | 2018 | EN | article | paywall (SAGE) | user discovery | acquired | yes | `en/154-diy-project-based-teaching-dj.pdf`. Project-based DJ teaching methodology. |
| 155 | Analyzing Code: What a Critical Code Studies Approach Reveals About the Epistemology of Data Journalism | Aman Abhishek, Lucas Graves | 2024 | EN | article | paywall | user discovery | acquired | yes | `en/155-analyzing-code-critical-code-studies.pdf`. Analysis of 234 GitHub repos — reveals scraping, data processing techniques used in newsrooms. |
| 156 | By the Numbers: Data Journalism Projects as a Means of Teaching Political Investigative Reporting | Caroline Graham | 2015 | EN | article | paywall | user discovery | acquired | yes | `en/156-by-the-numbers-teaching-political-investigative.pdf`. DJ teaching framework with networked journalism workflow. |
| 157 | First Things First: Teaching Data Journalism as a Core Skill | Lynette Sheridan Burns, Benjamin J. Matthews | 2018 | EN | article | paywall (SAGE) | user discovery | acquired | yes | `en/157-first-things-first-teaching-dj.pdf`. Critical reflection model for teaching data literacy to first-year students. |
| 158 | Interrogating Data, Algorithms, and Automatization Through Journalism Ethics (Panama Papers chapter) | Helena Cortés, María Luengo | 2021 | EN | article | paywall | user discovery | acquired | yes | `en/158-interrogating-data-panama-papers-ethics.pdf`. Panama Papers methodology: encrypted sources, cross-border verification of 11.5M files. |
| 159 | Learning to Teach Data Journalism: Innovation, Influence and Constraints | Jonathan Hewett | 2015 | EN | article | paywall | user discovery | acquired | yes | `en/159-learning-to-teach-dj.pdf`. Curriculum design methodology for DJ module in MA programme. |
| 160 | Teaching Data Journalism in New Zealand | Grant Hannis | 2018 | EN | article | paywall (SAGE) | user discovery | acquired | yes | `en/160-teaching-dj-new-zealand.pdf`. Concrete 3-hour DJ teaching module with curriculum structure. |
| 161 | When the Numbers Don't Add Up: Accommodating Data Journalism | Sue Green | 2018 | EN | article | paywall (SAGE) | user discovery | acquired | yes | `en/161-when-numbers-dont-add-up.pdf`. Curriculum design for integrating DJ into compact journalism programme. |
| 162 | An analysis about the curriculum of Data Journalism in China | Xihao Yang | 2022 | EN | article | open access (ACM) | user discovery | acquired | no | Descriptive landscape survey of DJ curriculum in China, no transferable methodology. `_rejected/` |
| 163 | Classifying Data Journalism | Florian Stalph | 2017 | EN | article | paywall (T&F) | user discovery | acquired | no | Content analysis classifying daily DJ stories; descriptive, no practitioner methodology. `_rejected/` |
| 164 | Datafication of Journalism: How Data Elites and Epistemic Infrastructures Change News Organizations | Nadja Schaetz, Juliane Lischka, Laura Laugwitz | 2023 | EN | article | paywall | user discovery | acquired | no | Sociological analysis of data infrastructures in newsrooms via job ads. `_rejected/` |
| 165 | Data Journalism, Impartiality and Statistical Claims | Stephen Cushion, Justin Lewis, Robert Callaghan | 2016 | EN | article | paywall | user discovery | acquired | no | Content analysis of statistics in UK news; critical study, no practitioner methodology. `_rejected/` |
| 166 | Data Journalism and Ethics: A Russian Approach | Alexandra Shilina | 2017 | EN | article | paywall (T&F) | user discovery | acquired | no | Two-page commentary on DJ ethics in Russia; too brief, no methodology. `_rejected/` |
| 167 | Data Journalism and the Challenge of Shoe-Leather Epistemologies | Norman P. Lewis, Stephenson Waters | 2017 | EN | article | paywall | user discovery | acquired | no | Content analysis of how 'data journalism' is defined; epistemological/sociological. `_rejected/` |
| 168 | Data Journalism Classes in Australian Universities: Educators Describe Progress to Date | Kayt Davies, Trevor Cullen | 2016 | EN | article | paywall | user discovery | acquired | no | Survey of DJ teaching landscape in Australia; descriptive, no transferable methodology. `_rejected/` |
| 169 | Data Journalism in the Arab Region: Role Conflict Exposed | Norman P. Lewis, Eisa Al Nashmi | 2019 | EN | article | paywall | user discovery | acquired | no | Qualitative interview study of barriers to DJ in Arab nations; sociological. `_rejected/` |
| 170 | Data Journalism Practices Globally: Skills, Education, Opportunities, and Values | Bahareh R. Heravi, Mirko Lorenz | 2020 | EN | article | paywall | user discovery | acquired | no | Descriptive survey of global DJ practices; no transferable methodology. `_rejected/` |
| 171 | Data Journalism Sustainability: An Outlook on the Future of Data-Driven Reporting | Florian Stalph, Eddy Borges-Rey | 2018 | EN | article | paywall | user discovery | acquired | no | Analysis of DJ sustainability; organizational/economic, not methodology. `_rejected/` |
| 172 | Diving into Data: Pitfalls and Promises of Data Journalism in Semi-Authoritarian Contexts | Allen Munoriyarwa, Sarah Chiumbu | 2023 | EN | article | paywall | user discovery | acquired | no | Sociological analysis of DJ under political constraints (South Africa). `_rejected/` |
| 173 | Exploring the Normative Foundation of Journalism Education: Nordic Journalism Educators' Conceptions | Maarit Jaakkola, Panu Uotila | 2022 | EN | article | paywall | user discovery | acquired | no | Survey of Nordic educators' normative conceptions; not DJ-specific methodology. `_rejected/` |
| 174 | All Forest, No Trees? Data Journalism and the Construction of Abstract Categories | Wilson Lowrey, Jue Hou | 2018 | EN | article | paywall | user discovery | acquired | no | Sociology of quantification; critical/theoretical, no practitioner methodology. `_rejected/` |
| 175 | Probabilistic Storytelling and Temporal Exigencies in Predictive Data Journalism | Christian Pentzold, Denise Fechner | 2021 | EN | article | paywall | user discovery | acquired | no | Epistemological study of predictive analytics in DJ; theoretical. `_rejected/` |
| 176 | Remaining in Control with an Illusion of Interactivity: The Paternalistic Side of Data Journalism | Ester Appelgren | 2019 | EN | article | paywall | user discovery | acquired | no | Short critical essay on paternalism in DJ visualization; theoretical. `_rejected/` |
| 177 | The Data Journalism Workforce: Demographics, Skills, Work Practices, and Challenges | Simona Bisiani et al. | 2023 | EN | article | paywall | user discovery | acquired | no | Descriptive workforce survey; documents practices but no transferable methodology. `_rejected/` |
| 178 | The Evolution of Data Journalism: A Case Study of Australia | Scott Wright, Kim Doyle | 2018 | EN | article | paywall (T&F) | user discovery | acquired | no | Case study of DJ evolution in Australia; historical/sociological. `_rejected/` |
| 179 | The Impact of Public Transparency Infrastructure on Data Journalism | Lindita Camaj, Jason Martin, Gerry Lanosga | 2022 | EN | article | paywall | user discovery | acquired | no | Comparative analysis of transparency infrastructure effects on DJ; sociological. `_rejected/` |
| 180 | The Inapplicability of Objectivity: Understanding the Work of Data Journalism | Jingrong Tong, Landong Zuo | 2019 | EN | article | paywall | user discovery | acquired | no | Epistemological study of objectivity norms in DJ; critical/theoretical. `_rejected/` |
| 181 | Towards an Epistemology of Data Journalism in the Devolved Nations of the UK | Eddy Borges-Rey | 2017 | EN | article | paywall | user discovery | acquired | no | Epistemological framework; purely theoretical. `_rejected/` |
| 182 | Transparency, Interactivity, Diversity, and Information Provenance in Everyday Data Journalism | Rodrigo Zamith | 2019 | EN | article | paywall | user discovery | acquired | no | Content analysis of DJ output characteristics; analytical, not production methodology. `_rejected/` |
| 183 | What Makes for Great Data Journalism? | Mary Lynn Young, Alfred Hermida, Johanna Fulda | 2017 | EN | article | paywall | user discovery | acquired | no | Evaluative analysis of DJ quality criteria; no practitioner methodology. `_rejected/` |
| 184 | Writing With Data: A Study of Coding on a Data-Journalism Team | Chris Aaron Lindgren | 2020 | EN | article | paywall | user discovery | acquired | no | Code studies theorizing coding as 'intermediary writing'; academic analysis, not DJ workflow. `_rejected/` |
| 185 | "API-Based Research" or How Digital Sociology and Journalism Studies Can Learn from the Cambridge Analytica Breach | Tommaso Venturini, Richard Rogers | 2019 | EN | article | paywall | user discovery | acquired | no | Research methodology for studying platforms, not journalism production methodology. `_rejected/` |
| 186 | "In the Beginning Were the Data": Economic Journalism as/and Data Journalism | Angel Arrese | 2022 | EN | article | paywall | user discovery | acquired | no | Historical/conceptual analysis of economic journalism and DJ; theoretical. `_rejected/` |
| 79 | Jornalismo guiado por dados: aproximações entre identidade jornalística e cultura hacker | Marcelo Träsel | n.d. | PT | article | open access | academic search | screened | yes | highlights DJ practices |
| 80 | Jornalismo de Dados: Conceitos e Categorias | academic | n.d. | PT | article | open access (Knight Center) | academic search | screened | yes | concepts and categories |
| 81 | Data Journalism (encyclopedia entry) | Brant Houston | n.d. | EN | article | paywall (Wiley) | academic search | screened | no | encyclopedia entry — definitional, not methodology |
| 82 | Periodismo de datos: el big data como elemento diferenciador | doctoral thesis | n.d. | ES | article | open access (Dialnet) | academic search | screened | yes | highlights DJ practices |
| 83 | Antecedentes y fundamentos del Periodismo de datos | various | n.d. | ES | article | open access | academic search | screened | yes | highlights DJ practices |

### Guides, Curricula & Training

| # | title | author/org | year | lang | type | access | found_via | status | included | exclusion_reason |
|---|-------|------------|------|------|------|--------|-----------|--------|----------|------------------|
| 92 | GIJN Data Journalism Resource Collection | GIJN | ongoing | EN | meta | open access | canonical | screened | meta | meta-resource for finding more sources |
| 93 | GIJN Summer Reading List 2025 | GIJN | 2025 | EN | meta | open access | GIJN | screened | meta | curated list — meta-resource |
| 94 | GIJN Intro to Investigative Journalism: Data Journalism | Purity Mukami, Emilia Díaz-Struck (GIJN) | n.d. | EN | guide | open access | GIJN | converted | yes | Full article text (process, toolbox, case studies) |
| 95 | MaryJo Webster Training Materials | MaryJo Webster | ongoing | EN | guide | open access | NICAR | converted | yes | GitHub repo cloned (mjwebster/DataJ) |
| 96 | ProPublica Collaborative Data Journalism Guide | Rachel Glickhouse (ProPublica) | ~2018 | EN | guide | open access | web search | converted | yes | Full GitHub repo cloned (30 .md files): sources/en/96-propublica-collaborative-dj-guide/ |
| 97 | NICAR Tipsheets Archive (2020–2025) | IRE/NICAR, compiled by Sharon Machlis | ongoing | EN | guide | open access (machlis.com/nicar/) | NICAR | converted | yes | 234 entries screened → 80 included, 154 excluded; 78 fetched (26 repos, 48 markdown, 4 PDFs). See `en/nicar/nicar_screening.md` |
| 98 | Simon Rogers — Intro to Data Journalism (syllabus) | Simon Rogers | ongoing | EN | curriculum | open access | DDJ syllabi | screened | meta | syllabus — meta-resource |
| 99 | Matt Waite JOUR307 (syllabus + materials) | Matt Waite | ongoing | EN | curriculum | open access (GitHub) | DDJ syllabi | screened | meta | syllabus — meta-resource |
| 100 | Dan Nguyen — CAR and DDJ Syllabi Collection | Dan Nguyen | n.d. | EN | meta | open access (GitHub) | DDJ syllabi | screened | meta | meta-collection of syllabi |
| 101 | Journalists Resource — Data Journalism Syllabus | Harvard | n.d. | EN | curriculum | open access | DDJ syllabi | screened | meta | syllabus |
| 102 | UH Libraries Syllabus Bank | UH Libraries | n.d. | EN | meta | open access | web search | screened | meta | aggregated syllabi |
| 103 | DataJourn.com Syllabus | n.d. | n.d. | EN | curriculum | open access | web search | screened | meta | syllabus |
| 104 | The Lede Program | Columbia | ongoing | EN | curriculum | ledeprogram.com | DDJ syllabi | screened | meta | bootcamp program |
| 105 | Columbia Data Journalism Teaching Guides | Columbia | ongoing | EN | guide | open access | Columbia | converted | yes | Portal page; actual PDFs already acquired as #37 and #38 |
| 106 | Doing Journalism with Data (MOOC) | Bradshaw, Cairo, Doig, Rogers, Kayser-Bril | 2014 | EN | curriculum | open access (learno.net) | EJC | converted | yes | Course overview + all 5 modules fetched |
| 107 | DataJournalism.com | EJC | ongoing | EN | guide | open access | canonical | screened | meta | resource portal |
| 108 | jwyg/awesome-data-journalism | Jonathan Gray | ongoing | EN | meta | open access (GitHub) | web search | screened | meta | curated list |
| 109 | Damiano Bacci — Data Journalism Books List | Damiano Bacci | n.d. | EN | meta | open access | web search | screened | meta | book catalog |
| 110 | CFPJ — Formations en datajournalisme | CFPJ | ongoing | FR | curriculum | cfpj.com | web search | screened | meta | training program |
| 111 | EMI — Bases du datajournalisme | EMI | ongoing | FR | curriculum | emi-ecoles.com | web search | screened | meta | training program |
| 112 | Paris Nanterre — Master Journalisme de données | Paris Nanterre | 2025 | FR | curriculum | university site | web search | screened | meta | university course |
| 113 | Comment devenir un bon datajournaliste (MOOC) | Rue89 / Kayser-Bril | 2015 | FR | curriculum | archived | web search | screened | no | MOOC — video/interactive format, not analyzable as text |
| 114 | Jean-Marc Manach — Data et journalisme (MOOC) | Jean-Marc Manach | n.d. | FR | curriculum | open access | web search | screened | no | MOOC — video/interactive format, not analyzable as text |
| 115 | UC3M Data Journalism Course | UC3M Madrid | ongoing | ES | curriculum | open access (syllabus) | web search | screened | meta | syllabus |
| 116 | ICFJ Online Course: Periodismo de datos para investigar la corrupción | ICFJ | 2019 | ES | curriculum | open access | ICFJ | converted | yes | Course page content fetched |
| 117 | Fundación Gabo — 15 recursos para periodismo de investigación y de datos | Fundación Gabo | n.d. | ES | meta | open access | GIJN | screened | meta | curated list |
| 118 | Fundación Gabo — Curso de periodismo de investigación | Fundación Gabo + Columbia | ongoing | ES | curriculum | fundaciongabo.org | GIJN | screened | meta | training program |
| 119 | Sandra Crucianelli — Periodismo de Base de Datos (blog/tutorials) | Sandra Crucianelli | ongoing | ES | guide | open access | ICFJ | converted | yes | Full blog post + 18 Issuu document links + 6 video links extracted |
| 120 | UOC Biblioguía: Periodismo de datos | UOC | ongoing | ES | meta | open access | web search | screened | meta | academic guide with resources |
| 121 | Escola de Dados — Courses and Tutorials | Escola de Dados | ongoing | PT | guide | open access | canonical | converted | yes | Portal + 3 full tutorials (raspagem, busca avançada, limpeza de dados) |
| 122 | Escola de Dados — 10 livros para aprender sobre jornalismo de dados | Escola de Dados | 2020 | PT | meta | open access | Escola de Dados | screened | meta | curated book list |
| 123 | Escola de Dados — Primeiros passos no jornalismo de dados | Escola de Dados | n.d. | PT | guide | open access | Escola de Dados | converted | yes | Full tutorial fetched via browser |
| 124 | Abraji Help Desk — Manual de Jornalismo de Dados | Abraji | ongoing | PT | guide | open access | Abraji | converted | yes | Portal + 3 full chapters from Elections Guide (Intro, Ch1 Tools, Ch3 Investigating Candidates) |
| 125 | Natália Mazotte — Como começar no jornalismo de dados | Natália Mazotte | n.d. | PT | guide | open access (Medium) | web search | converted | yes | Content summarized from Escola de Dados #123 (Medium behind Cloudflare) |
| 126 | A dossier of data journalism teaching strategies | DataJournalism.com | n.d. | EN | guide | open access | EJC | converted | yes | Full article (7 countries, 9 teachers) fetched via browser |

### NICAR Tipsheets — Top Individual Entries

_Entries below are the most methodologically rich tipsheets from NICAR 2020–2025 (source: #97 screening). Status `acquired` = content fetched to `sources/en/nicar/`. Numbered as sub-items of #97 (97a–97j) to avoid ID conflicts._

| # | title | author | year | lang | type | access | found_via | status | included | exclusion_reason |
|---|-------|--------|------|------|------|--------|-----------|--------|----------|------------------|
| 97a | Cutting-Edge Web Scraping Techniques | Simon Willison | 2025 | EN | tipsheet | open access (GitHub) | NICAR | converted | yes | browser automation, data from images, LLM scraping |
| 97b | Using Python to Build Data Pipelines You Can Share | Sean McMinn, Allan James Vestal | 2024 | EN | tipsheet | open access (GitHub) | NICAR | converted | yes | explicit pipeline methodology for newsrooms |
| 97c | First LLM Classifier | Ben Welsh, Derek Willis | 2025 | EN | tipsheet | open access (palewi.re) | NICAR | converted | yes | LLM classification methodology — key for RQ2 |
| 97d | Go Big with GitHub Actions | Ben Welsh, Iris Lee, Dana Chiueh | 2025 | EN | tipsheet | open access (palewi.re) | NICAR | converted | yes | automated data pipeline at scale |
| 97e | The Worst PDFs on the Planet | Derek Willis | 2025 | EN | tipsheet | open access (GitHub) | NICAR | converted | yes | LLM-based PDF extraction replacing OCR |
| 97f | Large-scale scraping projects: Best practices | Leon Yin, Ilica Mahajan, Jeff Kao | 2024 | EN | tipsheet | open access (Google Slides) | NICAR | converted | yes | legal/ethical large-scale scraping methodology |
| 97g | Best practices for quantitative assessments of AI success | Jeremy Merrill, Ence Morse, Caitlin Gilbert | 2025 | EN | tipsheet | open access (Google Docs) | NICAR | converted | yes | AI evaluation methodology for journalism |
| 97h | Editing the data story | Maud Beelman, Jennifer LaFleur | 2020 | EN | tipsheet | open access (Google Slides) | NICAR | converted | yes | bulletproofing/verification methodology |
| 97i | What's New in the World of LLMs | Simon Willison | 2025 | EN | tipsheet | open access (blog) | NICAR | converted | yes | LLM landscape for journalism — key for RQ2 |
| 97j | Data Unit Guide | Clayton Aldern, Tatyana Monnay | 2021 | EN | tipsheet | open access (dug.news) | NICAR | converted | yes | newsroom data unit organization methodology |

### NICAR Session Notes — Brent Jones (2014–2018)

_Detailed session notes from NICAR 2014–2018 by Brent Jones (brentajones on GitHub). Covers sessions predating the Machlis CSV (2020–2025). 69 session notes total across 4 repos._

| # | title | author | year | lang | type | access | found_via | status | included | exclusion_reason |
|---|-------|--------|------|------|------|--------|-----------|--------|----------|------------------|
| 97k | NICAR 2014 Session Notes (20 sessions) | Brent Jones | 2014 | EN | notes | open access (GitHub) | brentajones/nicar14-notes | converted | yes | mixed sessions; includes data acquisition, analysis, workflow |
| 97l | NICAR 2015 Session Notes (10 sessions) | Brent Jones | 2015 | EN | notes | open access (GitHub) | brentajones/nicar15-notes | converted | yes | includes "16 Solutions for Data-Driven Projects" (Groskopf/Overberg) — pipeline methodology goldmine |
| 97m | NICAR 2016 Session Notes (18 sessions) | Brent Jones | 2016 | EN | notes | open access (GitHub) | brentajones/nicar16-notes | converted | yes | includes analysis methodology, stats primer, data project life cycle |
| 97n | NICAR 2018 Session Notes (21 sessions) | Brent Jones | 2018 | EN | notes | open access (GitHub) | brentajones/nicar18-notes | converted | yes | includes reproducible data analysis (ETL/workflows), data-you-already-have |

---

## Screening Summary

| Category | Count |
|----------|-------|
| **yes** (included) | 89 |
| **no** (excluded) | 38 |
| **meta** (resource for finding sources) | 20 |
| **NICAR top tipsheets** (included, sub-items of #97) | 10 |
| **NICAR session notes** (2014–2018, sub-items of #97) | 4 |
| **Total entries** | 161 |

_All maybes resolved. Expansion search (v7) added 9 new candidates; 8 acquired (v8). #145 reclassified as unavailable (v9)._

**GET phase closed 2026-02-23.** Final tally: ~90 acquired, 2 included-not-acquired (purchase barrier: #16, #25), 41 excluded. NICAR: 78/80 tipsheets fetched.

**CONVERT phase completed 2026-02-23.** 75 outputs generated (6.27M words total). 3 PDF warnings (word count delta >10%): #57 (45.7% — likely scanned), #146 (13.4% — Arabic/English), #54 (13.8%). NICAR consolidated into 10 per-year files (97a–97j). See `sources/convert-manifest.csv`.

### Exclusion reasons breakdown
- Visualization/presentation only (no upstream methodology): 9
- Case study / narrative (not methodology): 4
- Critical theory / no practitioner methodology: 5
- Meta-research / historical analysis: 5
- Tool-specific manual: 3
- Outside language scope: 1
- Not about DDJ: 1
- Content analysis / impact study (no transferable methods): 1

---

## Conference Proceedings (separate handling)

Conference proceedings (#84–91) contain individual papers, not a single methodology. These are better handled as **meta-resources** — we can mine them for specific relevant papers rather than including the entire proceedings as sources.

| # | venue | years | access | action |
|---|-------|-------|--------|--------|
| 84–87 | European Data & Computational Journalism Conference | 2017–2025 | open access (UCD) | mine for relevant papers |
| 88 | Computation+Journalism | 2014–2022 | non-archival | mine for relevant papers |
| 89 | NICAR | annual | IRE membership | mine for relevant tipsheets |
| 90 | Coda.Br | 2016+ | escoladedados.org | mine for relevant papers |
| 91 | IAMCR | various | iamcr.org | mine for relevant papers |

---

## Bias Assessment

| Dimension | Observation | Mitigation |
|-----------|-------------|------------|
| **Language** | English-dominant (~70% of sources). FR/ES/PT well represented for available literature. | Acceptable — reflects publication landscape. Non-EN sources adequately covered. |
| **Geography** | US/UK heavy in EN sources. Latin America well covered via ES/PT. Africa, Asia underrepresented. | DDJ in the Global South (#18) and Africa SLR (#72) partially address this. |
| **Temporal** | Range from 1973 to 2025. Cluster around 2013–2024. | Good temporal spread. Pre-2010 works capture foundational thinking. |
| **Practitioner vs. academic** | Mix of both. Practitioner works dominate books; academic works dominate articles. | Balanced for the project's needs. |
