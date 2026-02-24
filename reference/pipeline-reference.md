# Data Pipeline Step Reference

## How to Use This Document

This document compiles all available content about the 7-step data pipeline (Define, Find, Get, Verify, Clean, Analyze, Present) from across the project's source materials. It is organized by pipeline step, with subsections per source. Content is extracted verbatim or lightly edited for readability — not summarized. The goal is to have everything in one place for curriculum design.

**Sources compiled:**

| # | Source | Shorthand |
|---|--------|-----------|
| 1 | `reference/scoda-pipeline-compiled-notes.md` | Scoda notes |
| 2 | `reference/iri_data_literacy_curriculum_final.md` | IRI curriculum |
| 3-6 | `reference/IJBA Data J/Data J 2023-2024/slides/` (4 decks) | 2023-2024 slides |
| 7-12 | `reference/IJBA Data J/Data J 2024-2025/slides/` (6 decks) | 2024-2025 slides |
| 13 | `reference/IJBA Data J/Data J 2024-2025/2024-2025-overview.md` | 2024-2025 overview |
| 14 | `reference/IJBA Data J/Data J 2024-2025/2024-2025-changelog.md` | 2024-2025 changelog |

---

## 0. Pipeline Overview

### From: Scoda notes

**The data pipeline handbook** (`pages/The data pipeline handbook.md`):
> The Data Pipeline is School of Data's approach to working with data from beginning to end. Once you understand your action cycle and the stakeholders, it will be time to work with the data and we have broken down this process in steps. The Data Pipeline is a work in progress, we started out suggesting five steps, but our community is constantly experimenting and tweaking it to reflect the core steps that are present in every kind of data-driven projects.

**Designing strong LLM harnesses and evaluation for LLM pipelines** (`journals/2026_02_18.md`):
> The concept of the school of data pipeline (Define, Find, Get, Verify, Clean, Analyze, Present) in the age of AI: it would have helped me identify that the find part (listing documents to be analyzed) is different from the get part (sending a document for processing)

**Curriculum ideas for IJBA** (`journals/2026_02_14.md`):
> Tasks should ideally align with the steps of a data pipeline (e.g., get, verify, clean, analyze) and not attempt to combine multiple steps into one, allowing for iterative verification.

**2024-2025 IJBA curriculum -- Cours 1: Introduction** (`pages/2024-2025 IJBA curriculum.md`):
> **Presenter la demarche projet** : Introduire le concept de "data pipeline" comme un cadre methodologique pour les projets de datajournalisme.

**Cours 3: Verification et nettoyage -- Slides** (`pages/Cours 3%3A Verification et nettoyage.md`):
> **Slides 4-7 : Rappel Data Pipeline**
> - Slide 5: Schema des 7 etapes (Definir a Presenter), mention du caractere non lineaire.
> - Slide 6: Schema mettant en evidence les etapes deja vues (Definir, Trouver, Recuperer).

**Initial ideas and vision for lectures and crash course (Turin 2025-26)** (`journals/2025_09_11.md`):
> I put a bit less emphasis on the overall data pipeline, because that's too much information in a limited time.

**EITI companies database next step report** (`pages/EITI companies database next step report.md`):
> use the data pipeline steps to do a mapping of the actions that are mission aligned vs ones that are processing. The use it to show potential for improvements in the pipeline. There's a potential image to explain / visualise showing the different pieces that make an ideal data pipeline in terms of products, tools, processes, the components of that ideal, and the level/path of progress that each scenario enables.

**IJBA Quiz -- Which stages are not always necessary?** (`journals/2025_04_14.md`):
> Quelle(s) etape(s) de la data pipeline ne sont pas toujours necessaires?
> - Nettoyer et Presenter
> - Definir et Verifier
> - Analyser
> - Nettoyer

**Fellows and Data Experts -- Sheena Carmel Opulencia-Calub** (`journals/2025_08_03.md`):
> Her Fellowship was consequently focused on similar work, where she used the data pipeline as a basis for training CSOs and civil servants around the Philippines.

**Fellows and Data Experts -- Ali Rebaie** (`journals/2024_09_16.md`):
> Ali went on to become a prominent consultant on the impact of data [...] spreading data skills and educating on the use of the data pipeline methodology to ordinary citizens and journalists.

### From: IRI curriculum

**Curriculum framing** (lines 1-5):
> This curriculum, developed by the Open Knowledge Foundation with the support of the International Republican Institute, aims to present the fundamentals of data literacy in a way that is approachable for civic actors in general, and democracy activists in particular. The curriculum's structure is based on the Data Pipeline, a methodology developed by School of Data, an Open Knowledge Foundation program.

**Module 1, Section 4 -- Data Pipeline definition** (lines 744-812):
> The Data Pipeline is School of Data's approach to working with data from beginning to end. Once you understand your action cycle and your stakeholders, it will be time to work with the data. We have broken down this process in steps. The Data Pipeline is a work in progress. We started out by suggesting five steps, but our community is constantly experimenting and tweaking it to reflect the core steps that are present in every kind of data-driven project. The steps are:
>
> Define [...] Find [...] Get [...] Verify [...] Clean [...] Analyze [...] Present [...]

**Module 1, Introduction** (lines 188-197):
> What is data? Many use the word but asking this question to ten people will probably give you ten answers. And that's because we all have an instinctive sense of what data is, although not having a clear definition inhibits us from properly making use of it. But in a context where most civic organizations are still far from being data savvy, the confusion about data leads to many missed opportunities for social change.
>
> This module will cover the basic concepts needed to navigate the world of data and start your own data-driven projects.

**Module 1, Section 4 -- Pipeline walkthrough recap** (lines 727-739):
> And we're done! With this module completed, you now have the fundamentals needed to be able to work with data. With the dataset you were given, you were able to:
> - Get the data, by accessing the spreadsheet and making a copy of it
> - Verify it by checking if the budget items matched the total
> - Clean it by reshaping it to facilitate your analysis
> - Analyze it by calculating the percentages
> - Visualize it with a pie chart
>
> Those steps are part of what we call the Data Pipeline.

### From: 2024-2025 SESSION 1 slides

**Data Pipeline (School of Data / Open Knowledge Foundation)**

> Définir — Récupérer — Nettoyer — Représenter
> 1 — 3 — 5 — 7
> 2 — 4 — 6
> Trouver — Vérifier — Analyser

- Matrice conçue par School of Data, la branche "formation" de l'ONG Open Knowledge Foundation

**Journalisme & data : De quoi parle-t-on ?**

- Objectifs : Informer le public en exploitant de larges volumes de données structurées
- Approches : Rendre lisibles des données complexes, enrichir des contenus, construire des enquêtes guidées par des données ou livrer une information personnalisée grâce à des visualisations interactives de données.

**3 objectifs**

Compiler des données — Analyser des données — Disponibiliser des données

Pour favoriser une approche granulaire — Pour produire des articles journalistiques — Pour un usage journalistique et/ou citoyen

**Que permet le datajournalisme ?**

Informer le public en exploitant de larges volumes de données structurées

- Rendre lisibles des données complexes
- Enrichir des contenus
- Construire des enquêtes guidées par des données
- Livrer des informations personnalisées grâce à des visualisations interactives de données

**Filiation historique**

- Charles Joseph Minard : Carte des pertes de l'armée napoléonienne en Russie (1812-1813), Tableau chronologique de l'entretien des pavés de Paris (1825)
- Florence Nightingale : Diagram of the causes of mortality in the army in the East (1855)
- Philippe Mayer : Couverture des émeutes de Detroit dans le Detroit Free Press (1967)
- David Burnham : Enquête du New York Times sur les départements de police à New York (1968)
- Clarence Jones : Enquête du Miami Herald sur la corruption dans le système judiciaire dans le comté de Dade (1977)
- Bill Dedman : Enquête du Atlanta Journal sur les biais racistes liés à l'octroi de prêts immobiliers à Atlanta (1978/1985/1988)
- Eliott Jaspin : Enquête du Providence Journal sur les prêts hypothécaires
- Simon Rogers : Enquête du Guardian sur le chômage (données granulaires) (2008)

CAR : JOURNALISME ASSISTE PAR L'ORDINATEUR → DATAJOURNALISME

**La « révolution » Open Data**

- 1978 : Loi "Cada". Création du droit d'accès aux documents administratifs
- 2005 : Ordonnance sur la réutilisation de l'information publique
- 2011 : Création d'une mission « Etalab » chargée de mettre en place un portail unique interministériel des données publiques
- 2003 : Directive européenne « PSI » : ensemble de règles concernant la réutilisation des données et documents détenus par les organismes des Etats membres de l'Union européenne
- 2016 : Promulgation de la loi République Numérique consacrant le principe de l'Open Data par défaut

**Les nouveaux terrains : Data & OSINT**

Combiner l'analyse des données aux enquêtes en sources ouvertes

"We used social media to track a single IDF combat engineering battalion, 8219 Commando, as they moved across Gaza, demolishing tunnels, houses, and mosques."

We geolocated each video or image of a demolition, verifying exactly where it took place. We then used satellite imagery from Planet Labs to determine when the demolition had occurred.

We used all these sources to build up a picture of where 8219 went, what it demolished and why.

— "We've Become Addicted to Explosions" The IDF Unit Responsible for Demolishing Homes Across Gaza, Bellingcat, 29 avril 2024

### From: 2024-2025 Verification alt deck (slides 4-5)

**Rappels sur la Data Pipeline**

- 7 GRANDES ETAPES : valable pour tout type de projet, de la brève sur le vote du budget municipal à l'enquête internationale sur l'évasion fiscale
- TRAVAIL SOUVENT NON LINEAIRE : aller-retour entre étapes, répétition des étapes pour plusieurs jeux de données

### From: 2024-2025-overview.md

**Strategic & Pedagogical Introduction**

The Strategic Approach: "Tabular Thinking" & The Horizon Table

The 2025 curriculum builds on the standard Data Pipeline but introduces two critical strategic shifts early in the process:
- **"Tabular Thinking" (La pensée tabulaire):** From Session 1, students are trained to reverse-engineer existing visualizations. By looking at a complex chart (e.g., car accidents by engine power), they must mentally reconstruct the spreadsheet (rows/variables) that generated it. This trains the "data eye" before they even touch a dataset.
- **The Horizon Table (Tableau d'horizon):** The course explicitly moves away from "finding data and seeing what's inside." Instead, it enforces a Design-First approach. Students must formulate a hypothesis and design the empty table (the "Horizon Table") with the specific columns they need *before* they start searching for data.

**The Pedagogical Strategy**
- **Deconstruction:** The course uses "reverse engineering" exercises (turning charts back into data tables) to demystify data structures.
- **Structured Skepticism:** It frames data not as facts, but as "structured representations of the world" that can be prone to hallucinations or poor encoding.
- **Tooling:** The stack remains accessible, centered on Google Sheets for logic, Tabula for unlocking PDFs, and Pivot Tables for analysis.

**Course Outline (5 Sessions)**

- Session 1: Introduction & Data Logic (Defining data journalism, "Tabular Thinking," and formulating hypotheses)
- Session 2: Finding & Acquiring Data (Sourcing strategies, scraping, and understanding data nature)
- Session 3: Verification & Cleaning (Reliability, PDF extraction, and structural hygiene)
- Session 4: Consolidation & Analysis (Merging datasets and executing the analysis)
- Session 5: Presentation (Storytelling and the limits of visualization)

### From: 2024-2025-changelog.md

**Major Evolutions from 2023-2024 to 2024-2025**

**1. Strategic Shift: From "Exploration" to "Design-First"**

- 2023-2024 (The "Search" Approach): The curriculum moved quickly from defining a project to Finding and Getting data. The focus was on *locating* existing files (Open Data, APIs) and then figuring out what was inside.
- 2024-2025 (The "Horizon" Approach): New Concept: The Horizon Table (*Tableau d'horizon*). Before searching for data, students must now design the empty dataset they *want* to find, specifying exactly which rows (observations) and columns (variables) are needed to answer their hypothesis. This prevents "data drift" by forcing students to define their destination before they start driving.

**2. Pedagogical Shift: "Tabular Thinking"**

- 2023-2024: Started with definitions of Open Data and the history of the field.
- 2024-2025: Introduces "Tabular Thinking" (*La pensée tabulaire*). Students are given complex published visualizations and must mentally "reverse-engineer" them back into a spreadsheet format. Goal: trains students to understand data structure abstractly before they ever open a spreadsheet.

**3. Data Literacy: "Hallucinations" & Representation**

- 2023-2024: Focused on technical verification -- checking reliability, exhaustiveness, and quality using statistics and expert interviews.
- 2024-2025: Reframes data ontologically. Data is explicitly defined as a "Structured representation of the world". New Risk: The curriculum now lists "Hallucination" alongside "Error" and "Falsification" as a core data risk, to account for AI-generated or synthetic data risks.

**4. Case Study Evolution**

- 2023-2024: Focused heavily on the 2022 Legislative Elections (gender parity among candidates).
- 2024-2025: "Rurbanization" & Digital Divide: a new complex case study. Maternity Wards: a case study on medicalization rates.

**5. The Role of AI**

- 2023-2024: AI (ChatGPT) was introduced at the very end as a "Helper" to write formulas or scripts.
- 2024-2025: AI is integrated more deeply. It is treated as a subject of scrutiny (checking for hallucinations). A dedicated section "Les IA et le journalisme de données" is now explicitly part of the analysis phase.

**Summary Comparison**

| Feature | 2023-2024 Session | 2024-2025 Session |
| :--- | :--- | :--- |
| **Starting Point** | Finding Sources & Open Data Definitions | "Tabular Thinking" (Reverse Engineering Charts) |
| **Design Methodology** | Define Project -> Find Data | Horizon Table (Design the empty table first) |
| **Data Definition** | Facts to be verified | "Structured Representation" susceptible to Hallucination |
| **Key Case Study** | 2022 Elections (Political) | Digital Fracture & Maternities (Sociological/Health) |
| **AI Role** | A tool for writing formulas (Assistant) | A subject of scrutiny and analysis (Component) |

### From: 2023-2024 Récupération slides (slides 4-7)

> 7 GRANDES ETAPES
> valable pour tout type de projet, de la brève sur le vote du budget municipal à l'enquête internationale sur l'évasion fiscale
>
> TRAVAIL SOUVENT NON LINEAIRE
> aller-retour entre étapes, répétition des étapes pour plusieurs jeux de données…)

CE QUE VOUS CONNAISSEZ:
Problématique & hypothèses, demande d'accès aux documents publics, portails open data, filetype:xls…

CE QUE L'ON VA VOIR AUJOURD'HUI:
scraping, collecte manuelle, extraction...

### From: 2023-2024 Verification & Nettoyage slides (slides 4-8)

> 7 GRANDES ETAPES
> valable pour tout type de projet, de la brève sur le vote du budget municipal à l'enquête internationale sur l'évasion fiscale
>
> TRAVAIL SOUVENT NON LINEAIRE
> aller-retour entre étapes, répétition des étapes pour plusieurs jeux de données…)

CE QUE VOUS AVEZ DEJA VU:
- Qu'est-ce que l'open data ?
- Définir son projet d'enquête
- Trouver les sources de données
- Récupérer les données

CE QUE L'ON VA VOIR AUJOURD'HUI:
- Méthodes de vérification
- Nettoyage de données tabulaires

EXEMPLE: DOSSIER MATERNITES DU MONDE
> Problématique: Sur quel critère choisir une maternité lorsque l'on est enceinte ? Y a-t-il des profils type d'établissements ?
> Hypothèse supposée : certains établissements se distinguent par un taux de médicalisation de l'acte plus fort (césarienne…)
> Recherche de données : enquête nationale périnatale, base statistique annuelle des établissements de santé (SAE), l'Agence technique de l'information hospitalière (ATIH) et la Fédération française de recherche en santé périnatale (FFRSP)
> Problèmes avec les données : fiabilité: données aberrantes, encodage non standardisé ; exhaustivité: actes non encodés

### From: 2023-2024 Consolidation & Analyse slides (slides 2-3)

CE QUE VOUS AVEZ DEJA VU:
- Qu'est-ce que l'open data ?
- Définir son projet d'enquête
- Trouver les sources de données
- Récupérer les données
- Vérifier les données
- Nettoyer les données
- Analyser les données
- Présenter les données

### From: 2023-2024 Presentation & Cartographie slides (slides 3-5)

CE QUE VOUS AVEZ DEJA VU:
- Qu'est-ce que l'open data ?
- Définir son projet d'enquête
- Trouver les sources de données
- Récupérer les données
- Vérifier les données
- Nettoyer les données
- Analyser les données
- Présenter les données

---

## 1. Define

### From: Scoda notes

**The data pipeline handbook** (`pages/The data pipeline handbook.md`):
> **Action**: Define:
> **Explanation**: Data-driven projects always have a "define the problem you're trying to solve" component. It's in this stage you start asking questions and come around the issues that will matter in the end. Defining your problem means going from a theme (e.g. air pollution) to one or multiple specific questions (has bikesharing reduced air pollution?). Being specific forces you to formulate your question in a way that hints at what kind of data will be needed. Which in turns helps you scope your project: is the data needed easily available? Or does it sound like some key datasets will probably be hard to get?

**Personal note on Tim Davies' article -- Define** (`pages/Linking Data and AI Literacy at Each Stage of the Data Pipeline.md`):
> This relates to the Chris Anderson's 2008 proclamation of the death of the traditional hypothesis-driven scientific enquiry, which should be replaced by Big Data pattern analysis as a first step for scientific investigations.
>
> More than 10 years later, this prediction fell flat, and as Sam Briddle mentioned it in his Book "New Dark Age: Technology and the End of the Future", this kind of thinking is typical of the solutionism of embedded in "computational thinking" where solving a problem is as simple as breaking it down into smaller parts that can be analysed separately.

**ICT 4 development - 2023-24 crash course syllabus -- Day 2 Objectives** (`pages/ICT 4 development - 2023-24 crash course syllabus.md`):
> Define step of the data pipeline: Practice the process of defining the main research questions and hypotheses of the proposal, including the development of a horizon table

**Personal note on Tim Davies' article -- Define + Get + Verify interplay**:
> it shows that the balanced that need to be reached in creating more structured data with AI is embedded in the natural back-and-forth between GET and VERIFY. DEFINE to some extent can be included, because in a context of a project, the "world" that we're looking at is specific.

*[Cross-reference: this Define/Get/Verify interplay also appears under Verify and Get]*

### From: IRI curriculum

**Module 1, Section 4 -- Data Pipeline: Define** (lines 756-765):
> Define: Data-driven projects always have a "define the problem you're trying to solve" component. It's in this stage you start asking questions and focus on the issues that will matter in the end. Defining your problem means going from a theme (e.g., air pollution) to one or multiple specific questions (has bike sharing reduced air pollution?). Being specific forces you to formulate your question in a way that hints at what kind of data will be needed. This, in turn, helps you scope your project: is the data needed easily available? Or does it sound like some key datasets will probably be hard to get?

**Module 1, Section 1 -- What is Data?** (lines 252-345):

Key definition used throughout: _Data is a structured representation of the world._ Data is:
- A representation of the world because data always tries to capture a part of reality.
- Structured, because to call it data, the result of that act of representing the world needs to follow a logical ordering.

Data types covered: Categorical (ordered/unordered), Discrete, Continuous, Qualitative vs Quantitative.

**Module 6, Section 1 -- From research question to hypothesis** (lines 2734-2831):

> Any data project starts with the DEFINE step of the Data Pipeline, during which you define a research question (also called a problem statement). The goal of the research question is to give your project a focus. Without it, you only have a theme, and you take the risk of wasting a lot of time analyzing the data in ways that do not help your initial aim.

Research question examples:

| Theme | Research question |
|---|---|
| Air pollution | Are air pollution levels around primary schools in Paris higher than the city average? |
| Gender parity in legislative elections | Do legislative election candidate lists include 50 percent of candidates from each gender? |

Good vs. bad research questions:

| Bad | Good |
|---|---|
| Are children affected by air pollution? | Are there higher levels of air pollution around primary schools in Paris? |

> The second thing to consider are the constraints on your project: how much time do you have? Who do you want to present the project's results to? What is realistic to do, given your level of skill/knowledge? [...] It is indeed very common to go back and forth between DEFINE, FIND and GET, as you refine your research question.

**Defining hypotheses** (lines 2787-2831):
> A hypothesis is a proposed explanation for some phenomenon. A good hypothesis should be simple, concise, and most importantly, testable -- you should be able to prove it wrong. Hypotheses are there for two reasons:
> - They further refine your project by defining the specific observations that you expect to highlight in the data.
> - They structure the narrative that you are trying to evidence with data.

*[Cross-reference: hypothesis formation also appears under Analyze as part of the analysis plan]*

### From: 2024-2025 SESSION 1 slides

**Qu'est ce qu'une donnée ?**

Une donnée n'est pas :
- Forcément un chiffre. Elle est souvent transformée en chiffre pour être traitée de manière statistique
- Types de données : Textuelles, Visuelles, Sonores, Olfactives, Gustatives, Tactiles

Une donnée n'est pas :
- Une information

Mais un moyen pour produire :
- Une information
- Des connaissances
- Un éclairage précis
- Une analyse exceptionnelle
- Et parfois : des théories farfelues

**Où se trouvent les données ?**

DONNEES DES ADMINISTRATIONS PUBLIQUES
- Portail Open Data
- Derrière une API
- Archives numériques ou physiques des administrations

DONNEES DES ENTREPRISES PRIVEES
- Sur internet (site web et réseaux sociaux)
- Derrière une API
- Archives numériques ou physiques des entreprises

NULLE PART...

LES PORTAILS OPEN DATA : Data.gouv.fr, Datara.gouv.fr, opendata.bordeauxmetropole

**La pensée tabulaire**

Exercice : Transformez ce diagramme en tableau de données
- Qu'est ce qu'on observe ?
- Selon quelles variables ?
- Quelle serait la forme la plus granulaire de ce tableau ?

Exercices basés sur :
- https://www.liberation.fr/societe/securite-routiere-plus-une-voiture-est-puissante-plus-elle-risque-davoir-un-accident-20241018
- https://www.lemonde.fr/les-decodeurs/article/2024/09/04/au-moins-20-644-traversees-de-migrants-dans-la-manche-depuis-janvier-2024
- https://www.lefigaro.fr/elections/legislatives/carte-les-resultats-des-elections-legislatives-2024
- https://www.liberation.fr/france/2019/05/08/elections-europeennes-faites-entrer-les-sortants

**L'enquête par hypothèses**

Démarche :
- Point de départ : Un jeu de données constitué OU Un questionnement
- Produire, grâce à un travail de documentation, des réponses provisoires à une question
- S'assurer que les réponses provisoires comportent des variables mesurables
- Créer un tableau d'horizon
- Exemple : diversité dans les écoles de journalisme

**Tableau d'horizon**
- Quelles lignes ? observations
- Quelles colonnes ? variables

**Mise en pratique**
- Sujet : L'aide à la presse
- Données : le recensement des jeux de données liés aux aides à la presse
- Hypothèses ?
- Tableau d'horizon ?

### From: 2024-2025 SESSION 2 slides (rappel)

**Ce qu'elles ne sont pas**

Des informations. Des chiffres et rien que des chiffres.

Les données peuvent prendre différentes formes. Elles sont souvent transformées en chiffres pour être traitées de manière statistique.

Les données sont une des briques utiles à la création d'information, ainsi que des connaissances.

**Schéma de Cédric Lombion (Open Knowledge Foundation)**

Axes : Forte/Faible représentativité x Forte/Faible structuration
Quadrants : Bonnes données, Données mal encodées, Hallucination, Données erronées

**Attention : les angles morts de l'analyse**

1. Accorder une importance capitale à la donnée au détriment des idées, des opinions, des vécus, des sens, etc → **Fétichisation**
2. Essentialiser un phénomène en partant de faits non représentatifs → **(Sur)interprétation**
3. Passer le relais interprétatif aux récepteurs → **(Non)interprétation**

### From: 2024-2025 Verification alt deck (slides 9-19)

**Qu'est-ce qu'une donnée ? (développement étendu par Cédric Lombion, 2018)**

- Une représentation structurée du monde
- Axes : structuration x représentativité
- Quadrants : bonnes données / données mal encodées (qualité) / hallucinations / données falsifiées ou erronées (fiabilité / exhaustivité)

**Exemple de données mal encodées :**

| Mois | Type | Nombre 2017 | Nombre 2018 |
| --- | --- | --- | --- |
| Juillet | Neufs | 793 | 993 |
| | Usagés | 4482 | 4682 |
| Août | Neufs | 609 | 809 |
| | Usagés | 1477 | 1677 |

Probleme : lecture humaine possible, mais lecture machine mal engagée.

**Bonnes données (version corrigée) :**

| Mois | Type | Nombre | Année |
| --- | --- | --- | --- |
| Juillet | Neufs | 793 | 2017 |
| Juillet | Neufs | 993 | 2018 |
| Juillet | Usagés | 4482 | 2018 |
| ...etc... |

**Données falsifiées ou erronées :** Que signifie "Neufs" ? (ambiguité sémantique)

**Hallucinations :** Valeurs impossibles (-5, 110.5, -20 pour des importations de véhicules)

### From: 2023-2024 Verification & Nettoyage slides (slide 22)

> ETAPES DEFINIR, TROUVER
> Compléter ces étapes sur le thème: lutte contre la fracture numérique dans la métropole bordelaise

_Note: The Define step is referenced but not deeply covered in the 2023-2024 decks. It appears only as a recap item ("Définir son projet d'enquête") and in a combined exercise._

---

## 2. Find

### From: Scoda notes

**The data pipeline handbook** (`pages/The data pipeline handbook.md`):
> **Action**: Find:
> **Explanation**: While the problem definition phase hints at what data is needed, finding the data is another step, of varying difficulty. There are a lot of tools and techniques to do that, ranging from a simple question on your social network, to using the tools provided by a search engine (such as Google search operators), open data portals or a Freedom of Information request querying about what data is available in that branch of government. This phase can make or break your project, as you can't do much if you can't find the data! But this is also where creativity can make a difference: using proxy indicators, searching in non-obvious locations... don't give up too soon!

**2024-2025 IJBA curriculum -- Cours 2: Recherche et recuperation** (`pages/2024-2025 IJBA curriculum.md`):
> Ce cours a pour but d'approfondir les etapes "Trouver" et "Recuperer" de la *data pipeline*. Cela inclut doter les participants des connaissances et techniques necessaires pour identifier des sources de donnees pertinentes, evaluer leur format et leur qualite initiale, et choisir/appliquer les methodes de recuperation appropriees, y compris les bases du web scraping.
>
> **Contextualiser la recherche de donnees :** Reviser la place des etapes "Trouver" et "Recuperer" dans la demarche globale ("Data Pipeline").

**Designing strong LLM harnesses** (`journals/2026_02_18.md`):
> it would have helped me identify that the find part (listing documents to be analyzed) is different from the get part (sending a document for processing)

### From: IRI curriculum

**Module 2, Introduction** (lines 821-831):
> Now that we know what data is and the questions we're interested in, we're ready to go out and hunt for it online. In this tutorial, you will learn where to start looking for data. In this module, we will look at different ways of getting data before setting you loose to find data yourselves!
>
> We will also consider what types of data you create and/or work with, and what format those datasets use. Your data stewardship practices will be dictated by the types of data that you work with, and what format they are in.

**Module 2, Section 1 -- Understanding data formats** (lines 879-998):

Key data formats: `.txt`, `.csv`/`.tsv`, `.xls`/`.xlsx`, `.ods`, `.doc`/`.docx`, `.json`/`.geojson`, `.xml`, `.pdf` (digital vs. scanned), `.html`, `.shp`

Tabular vs. Tree Structure distinction: CSV for tabular, JSON for tree-like data with variable branches per node.

**Module 2, Section 2 -- Where can I find data?** (lines 1001-1076):

Three main questions: (1) Where is the data? (2) Which format? (3) Do I need to transform it?

Data locations:
- On an open data portal
- In the digital system of a public or private organization
- In the physical archives of a public or private organization
- Behind an API
- Freely accessible on the web
- Nowhere (you must collect it yourself)

Localization/Format/Retrieval table:

| Localization | Possible formats | Retrieval |
|---|---|---|
| On an Open Data Portal | xls, csv, shp, pdf, ods, json, xml, sqlite... | Download |
| In a non-public digital system | xls, csv, shp, pdf, ods, json, xml, sqlite... | Access request |
| In a physical archive | Paper, photos, microfilm | Access request |
| Behind an API | CSV, JSON, XML | With a little bit of programming |
| On a web page | HTML, PDF | Varies based on the format |
| Nowhere | Depends on the data collection process | Data collection |

**Module 2, Section 3 -- Searching for data** (lines 1148-1183):

Walkthrough on Google search operators (e.g., `site:usa.gov filetype:pdf covid-19 unemployment`).

External resources:
- [Overview of data files](http://opendatahandbook.org/guide/en/appendices/file-formats/)
- [Google search operators](https://support.google.com/websearch/answer/2466433?hl=en)

### From: 2024-2025 SESSION 2 slides

**Où se trouvent les données ?**

| LOCALISATION | RECUPERATION | FORMATS |
|---|---|---|
| Portail open data | Téléchargement | xls, csv, shp, pdf, ods, json, xml, sqlite |
| Dans le système informatique d'une administration ou d'une entité privée (non publiées en ligne) | Demande d'accès | xls, csv, shp, pdf, ods, json, xml, sqlite (et bien pire...) |
| Dans les archives physiques d'une administration ou d'une entité privée | Demande d'accès | papier, photos (!), microfilm (!?!) |
| Derrière une interface de programmation applicative (API) | En bidouillant un peu de code informatique | csv, json, xml |
| En libre accès sur le web | en fonction du format | html, pdf (ou tout autre format en existence) |
| Nulle part | collecte de données | lié au mode de collecte |

**Dois-je transformer les données ?**

| FORMAT | RECUPERATION |
|---|---|
| XLS, CSV, SHP, ODS, JSON, XML, SQLITE | Pas d'étapes supplémentaires |
| PDF créé numériquement | Extraction des données (via Tabula par exemple, ou manuellement) |
| PDF scanné | Reconnaissance optique de caractère (OCR) ou manuellement |
| Papier, Photographie, Microfilm | Scanner + OCR ou manuellement |
| HTML | Collecte automatisée (scraping) ou manuellement |

### From: 2024-2025 SESSION 1 slides (cross-ref: sourcing also introduced here)

DONNEES DES ADMINISTRATIONS PUBLIQUES : Portail Open Data, Derrière une API, Archives numériques ou physiques des administrations

DONNEES DES ENTREPRISES PRIVEES : Sur internet (site web et réseaux sociaux), Derrière une API, Archives numériques ou physiques des entreprises

NULLE PART...

LES PORTAILS OPEN DATA : Data.gouv.fr, Datara.gouv.fr, opendata.bordeauxmetropole

### From: 2024-2025 Verification alt deck (slide 22)

ETAPES DEFINIR, TROUVER

Compléter ces étapes sur le thème: lutte contre la fracture numérique dans la métropole bordelaise

Exercice (slide 30) :
1. Retrouver le jeu de données «Lieux d'inclusion numérique» sur le portail open data de Bordeaux métropole
2. Quelles questions de vérification poser à ce jeu de données ?

### From: 2023-2024 Récupération slides (slides 11-15)

**"Où sont mes données?"**

3 GRANDES QUESTIONS:
1. Où sont mes données ?
2. Sous quel format sont-elles conservées ?
3. Dois-je les transformer ?

OU SONT MES DONNEES ?

| LOCALISATION | RECUPERATION | FORMATS |
| --- | --- | --- |
| Portail open data | Téléchargement | xls, csv, shp, pdf, ods, json, xml, sqlite |
| Dans le système informatique d'une administration ou d'une entitée privée (non publiées en ligne) | Demande d'accès | xls, csv, shp, pdf, ods, json, xml, sqlite (et bien pire…) |
| Dans les archives physiques d'une administration ou d'une entitée privée | Demande d'accès | papier, photos (!), microfilm (!?!) |
| Derrière une interface de programmation applicative (API) | En bidouillant un peu de code informatique | csv, json, xml |
| En libre accès sur le web | en fonction du format | html, pdf (ou tout autre format en existence) |
| Nulle part | collecte de données | lié au mode de collecte |

DOIS-JE LES TRANSFORMER ?

| FORMAT | RECUPERATION |
| --- | --- |
| XLS, CSV, SHP, ODS, JSON, XML, SQLITE | Pas d'étapes supplémentaires |
| PDF créé numériquement | Extraction des données via Tabula, ou manuellement |
| PDF scanné | Reconnaissance optique de caractère (OCR) ou manuellement |
| Papier, Photographie, Microfilm | Scanner + OCR ou manuellement |
| HTML | collecte automatisée (scraping) ou manuellement |

_Note: "manuellement ne veut pas dire tout seul: le travail d'équipe peut être important ici, et le crowdsourcing peut jouer. Exemple des déclarations des députés à la Haute Autorité pour la Transparence de la Vie Publique" (speaker notes, slide 15)_

### From: 2023-2024 Récupération slides (slides 30-32) — La collecte manuelle

ET SI... LES DONNEES N'EXISTENT PAS?

> ALORS IL FAUT LES CREER!
> - CROWDSOURCING
> - COLLECTE DE DONNEES SUR LE TERRAIN

COLLECTER SES PROPRES DONNEES N'EST PAS SIMPLE:
> - Quelle méthodologie ?
> - Quelle structuration de mes données (colonnes) ?
> - Quel degré de précision ?
> - Quel niveau d'exhaustivité ?
>
> Il vaut mieux prendre contact avec des spécialistes qui pourront vous aider à penser votre collecte (spécialistes de la statistique, de l'urbanisme…)

_Cross-reference: Find and Get are both covered in the Récupération deck. The above content is more Find-oriented (sourcing strategies, data locations). See Get for the technical extraction methods._

---

## 3. Get

### From: Scoda notes

**The data pipeline handbook** (`pages/The data pipeline handbook.md`):
> **Action**: Get
> **Explanation**: To get the data from its inital location to your computer can be short and easy or long and painful. Luckily, there's plenty of ways of doing that. You can crowdsource using online forms, you can perform offline data collection, you can use some crazy web scraping skills, or you could simply download the datasets from government sites, using their data portals or through a Freedom of Information request.

**Personal note on Tim Davies' article -- Get** (`pages/Linking Data and AI Literacy at Each Stage of the Data Pipeline.md`):
> Really important concept, as it relates to the very definition of data: Structure representation of the world. AI can be a powerful agent to create more data by producing more structures. The catch is the balance with the representativity of the AI system, which may create a lot of false positive, or erroneous information.

**Designing strong LLM harnesses** (`journals/2026_02_18.md`):
> the find part (listing documents to be analyzed) is different from the get part (sending a document for processing)

*[Cross-reference: the Define/Get/Verify interplay appears under Define and Verify]*

### From: IRI curriculum

**Module 3, Introduction** (lines 1186-1209):
> Even after confirming that a dataset is available, getting it on your computer can be an arduous process or a test of patience. Getting data in a readable format is a specific step that requires dedicated planning, including the time needed to research and locate the appropriate tools for the task. Very rarely will data just be magically available to analyze. One of the most common roadblocks faced by journalists and civic organizations is the lack of disclosure of the data owned by a public administration. Your first step should always be to ask nicely, but that is often not enough. This is where FOI (Freedom of Information) requests become necessary.
>
> While FOI requests leave you at the mercy of public administrations, there are many ways to take matters in your own hands when it comes to getting data. We'll cover three of them: PDF extraction, web scraping, and field data collection.

**Module 3 -- concepts and skills covered:**
- Concepts: Web scraping, PDF extraction, Field data collection
- Skills: Using Tabula to extract data from PDFs, Using Google Sheets to scrape data from the web (`IMPORTHTML`), Using Kobo Toolbox for field surveys

**Module 3, Section 1 -- Extracting data from digital PDFs** (lines 1253-1403):

Methods for PDF extraction:
- PDF to Word/Excel converters
- OCR (Optical Character Recognition)
- Programming (PDFMiner for Python, Tika/PDFBox for Java, pdftotext/pdftohtml for CLI)
- Crowdsourcing
- Tabula (free, open-source, MIT license, offline, works in Java environment)

Tabula key features: Autodetect Tables, manual selection, Stream vs. Lattice extraction algorithms, export to CSV/JSON/zip of CSVs.

Format/retrieval summary:

| Format | Retrieval |
|---|---|
| XLS, CSV, SHP, ODS, JSON, XML, SQL | No additional step |
| Digital PDF | Manual extraction or with Tabula |
| Scanned PDF | Manual extraction or with OCR |
| Paper, photograph, microfilm | Manual or OCR-equipped scan |
| HTML | Manual or automated (scraping) collection |

**Module 3, Section 2 -- Web scraping** (lines 1406-1463):

Google Sheets `IMPORTHTML` function for extracting HTML tables/lists. Also mentions the Web Scraper Chrome extension (https://webscraper.io).

**Module 3, Section 3 -- Collecting data** (lines 1465-1812):

Mobile data collection with ODK (Open Data Kit) and Kobo Toolbox. Covers XLSForm creation (Survey/Settings/Choices sheets), question types, constraints, uploading forms, testing on Android via Kobo Collect app.

### From: 2024-2025 SESSION 2 slides

**STRUCTURE D'UNE PAGE WEB** — Avec "X-Ray Goggles"

**Scraping (facile) : Importer des données dans un tableau depuis un site web**

- OPTION 1 : Copier/coller
- OPTION 2 : ImportHtml (Google Spreadsheet <-- Wikipedia)

**Scraping (plus complexe)**

Via des outils comme :
- import.io
- octoparse
- crawly
- Scraper (Google)

### From: 2024-2025 SESSION 2 slides (exercice Aides à la presse)

Exercice avec un jeu de données constitué : Aides à la presse (Ministère de la Culture)

1. Retrouvez les données
2. Récupérez les données
3. Familiarisez vous avec le tableau de données

Répondez aux questions suivantes :
- Quelles sont les entreprises qui n'ont reçu de l'aide qu'une seule fois ?
- Quelles sont les entreprises qui n'ont reçu de l'aide qu'en 2018 ?
- Quelles sont les 10 entreprises qui ont reçu le plus d'aide en 2016 ?

### From: 2024-2025 Verification alt deck (slide 38)

Ce que l'on va faire ensemble:
- Récupérer le fichier PDF marqué 'EXO'
- Télécharger le logiciel Tabula https://tabula.technology/
- Extraire les données
- Vérifier & Nettoyer les données

### From: 2023-2024 Récupération slides (slides 16-22) — Le scraping

Comment un site web est-il structuré ?
> https://x-ray-goggles.mouse.org/

RECUPERER DES DONNEES HTML SUR INTERNET = SCRAPER:
> C'est parce que c'est structuré qu'on peut facilement automatiser l'extraction.
> Démonstration par la preuve: scrapons Wikipedia avec Google Sheets

On utilise la formule IMPORTHTML.

Le niveau de difficulté est très variable, mais les outils sont nombreux:
- Wikipedia? IMPORTHTML
- IKEA? webscraper.io
- Mais aussi avec des programmes payants, ou en codant soi-même etc.

Un autre scraper: webscraper.io
> Gratuit et puissant
> un peu difficile à prendre en main au début
> ne fonctionne que sur Chrome/Chromium

### From: 2023-2024 Récupération slides (slides 23-24) — Les API

Récupérer des données via une API: genderize.io
_(Démonstration de l'utilisation de l'API via le navigateur)_

### From: 2023-2024 Récupération slides (slides 25-28) — L'extraction de PDF

LES TABLEAUX DE DONNEES EN PDF:

- LE PDF EST NUMERIQUE? **Tabula**
- SI LE PDF EST SCANNE? **Amazon Textract** (https://aws.amazon.com/fr/textract/)
- RECHERCHER DES DONNEES A TRAVERS PLUSIEURS PDF: **Google Pinpoint** (https://journaliststudio.google.com/pinpoint)
  - _"ça fonctionne avec pleins de formats"_ (speaker notes)

### From: 2023-2024 Récupération slides (slides 33-35) — ChatGPT

UN ASSISTANT UTILE A LA COLLECTE DE DONNEES

Peut être utile pour:
- se rappeler des formules: "rappelle moi la formule de Google Sheets qui permet d'extraire du contenu HTML"
- trouver pourquoi la formule ne fonctionne pas: "voici ma formule, mais j'ai le mauvais tableau en retour."
- faciliter l'écriture de petits scripts, si on a appris les bases: "voici les urls des délibérés de Bordeaux Métropole, aide moi à écrire un script curl pour télécharger les PDFs"
- "voici la documentation de l'API de météo France, aide moi a construire une requête pour récupérer la température"

Mais attention:
> ChatGPT se trompe souvent, donc il faut vérifier les résultats systématiquement
> ne jamais compter sur ChatGPT pour extraire sans erreurs de données d'un PDF

---

## 4. Verify

### From: Scoda notes

**The data pipeline handbook** (`pages/The data pipeline handbook.md`):
> **Action**: Verify
> **Explanation**: We got our hands in the data, but that doesn't mean it's the data we need. We have to check out if details are valid, such as the meta-data, the methodology of collection, if we know who organised the dataset and it's a credible source. We've heard a joke once, but it's only funny because it's true: all data is bad, we just need to find out how bad it is!

**Personal note on Tim Davies' article -- Get/Verify interplay**:
> it shows that the balanced that need to be reached in creating more structured data with AI is embedded in the natural back-and-forth between GET and VERIFY. DEFINE to some extent can be included, because in a context of a project, the "world" that we're looking at is specific.

**2024-2025 IJBA curriculum -- Cours 3: Verification et nettoyage** (`pages/2024-2025 IJBA curriculum.md`):
> **Diagnostiquer la qualite des donnees :** Approfondir l'analyse des problemes potentiels via le cadre structuration/representativite (donnees mal encodees, erronees/falsifiees, hallucinations)
>
> **Maitriser les concepts de la verification :** Definir et savoir evaluer les trois dimensions cles : Fiabilite (representation de la realite), Exhaustivite (completude) et Qualite (structure, documentation)
>
> **Appliquer des methodes de verification :** Mettre en oeuvre differentes strategies pour verifier les donnees (interroger la source, consulter des experts, effectuer des controles statistiques de base, utiliser le bon sens)

**Cours 3 -- Session outline** (`pages/Cours 3%3A Verification et nettoyage.md`):
> **11h15 - 11h40 (25 min) : La Verification : Theorie et Methodes**
> - Les 3 piliers (Fiabilite, Exhaustivite, Qualite).
> - Les 4 methodes (Source, Experts, Stats, Bon sens).

**Cours 3 -- Slides on verification**:
> **Slides 9-19 : Qu'est-ce qu'une donnee ? Concepts Qualite**
> - Slide 14: Axe Structuration vs Representativite.
> - Slide 15: Schema 2x2 mappant les problemes : 'donnees mal encodees' (qualite/structure), 'bonnes donnees', 'hallucinations', 'donnees falsifiees ou erronees' (fiabilite/exhaustivite).
>
> **Slides 24-28 : Theorie Verification**
> Les 3 enjeux (Fiabilite, Exhaustivite, Qualite) avec definitions et exemples courts. Les 4 methodes (Source, Experts, Stats, Bon sens).

### From: IRI curriculum

**Module 4, Introduction** (lines 1815-1827):
> Verifying is a step that is often skipped in the process of working with data. Especially if the data was difficult to get, we are all the more eager to start on the analysis. Not including at least some basic verification will mean that, on many projects, you will end up wasting time on bad data or worse -- you could publish incorrect results.

**Module 4, Section 1 -- What is good data? (3 criteria)** (lines 1880-1928):

1. **Trustworthiness**: how well the data represent reality. Assessing trustworthiness requires understanding the methodology and choices behind the creation of the dataset.

2. **Completeness**: how well the data covers the reality it tries to represent. Can be incomplete due to inconsistent collection practices or key elements being absent.

3. **Quality**: how well the dataset is structured and documented. Includes tidy data principles + documentation (data dictionary, metadata, methodology).

Sidebar on Metadata, Data Dictionary, Data Inventory (lines 1931-1952):
> A data inventory (or registry) is a document listing all the datasets owned by an organization. A data dictionary or codebook is a document describing the meaning of all columns and values in a dataset. The metadata is most simply described as 'data about the data.'

**Module 4, Section 2 -- Four verification methods** (lines 1954-2028):

1. **Asking the source**: those who produced or published the data are most likely the best experts on it.

2. **Asking experts**: data practitioners from the civic sector often get to work on datasets that pertain to many different topics. But on each of those topics there is probably an expert you can reach.

3. **Statistical checks**: create a statistical summary -- calculating the mean, median, maximum and minimum values and standard deviation for key columns. The Statistical Summary box covers: mean, median, max, min, standard deviation.

4. **Common sense check**: the ability to identify weird patterns in the data, or a number which shouldn't be this high, or a value which shouldn't have been part of this dataset. Relies on background knowledge about the topic.

**Module 4, Section 3 -- Common data issues** (lines 2207-2239):
- Missing values (blank, 0, NA)
- Missing values replaced with fallback dates (1900, 1904, 1969, 1970)
- Duplicated rows or values
- Inconsistent date formats
- Unspecified units
- Ambiguous column names
- Undocumented provenance
- Suspicious values
- Data too coarse
- Totals differ from published aggregates
- Spreadsheet has 65536 rows (old Excel max) or 255 columns (old Numbers max)

> It is very common for data projects to circle between verification and cleaning a few times until every suspicion has been rooted out.

### From: 2024-2025 SESSION 3 slides

**Schéma de Cédric Lombion (rappel dans Session 3)**

Données = des représentations structurées du monde.
Axes : Forte/Faible représentativité x Forte/Faible structuration.
Quadrants : Bonnes données, Données mal encodées, Hallucination, Données erronées.
Schéma conçu par Cédric Lombion (Civic Literacy Initiative)

**Un réflexe essentiel**

Vérifier est nécessaire même avec des données officielles

**Vérification: 3 enjeux**

1. Les données représentent-elles la réalité ? --> **Fiabilité**
2. Les données sont-elles complètes ? --> **Exhaustivité**
3. Les données sont-elles structurées et documentées correctement ? --> **Qualité**

**4 méthodes (à employer en fonction des données)**

- **Demander à la source**
- **Demander aux experts**
- **Vérifications statistiques** (moyenne, médiane, maximum, minimum, écart-type)
- **Bon sens** (est-ce que les hypothèses de bases sont réalistes?)

**Problèmes courants**

- Valeurs manquantes
- Valeurs manquantes remplacées par des valeurs ambiguës comme 0 ou des dates par défaut (1900, 1904, 1969, 1970 sont des défauts courants)
- Lignes ou valeurs en double
- Formats de dates qui varient au sein du même jeu de données
- Unités de mesure non spécifiées
- Noms de colonnes ambigus
- Pas de documentation de la provenance ou méthodologie du jeu de données
- Des valeurs suspectes sont présentes
- Les données ne sont pas assez fines
- Les totaux diffèrent des agrégats inclus
- La feuille de calcul a exactement 65536 lignes (valeur max dans les anciennes versions d'Excel) ou 255 colonnes (valeur max dans les anciennes versions de Numbers)

**Exemple: dossier des maternités du Monde**

Problématique: Sur quel critère choisir une maternité lorsque l'on est enceinte ? Y a-t-il des profils type d'établissements ?

Recherche de données : enquête nationale périnatale, base statistique annuelle des établissements de santé (SAE), l'Agence technique de l'information hospitalière (ATIH) et la Fédération française de recherche en santé périnatale (FFRSP)

Hypothèse: certains établissements se distinguent par un taux de médicalisation de l'acte plus fort (césarienne...)

Problèmes avec les données :
- fiabilité: données aberrantes, encodage non standardisé
- exhaustivité: actes non encodés

### From: 2024-2025 Verification alt deck (slides 24-28)

**VERIFICATION: 3 ENJEUX**

- **FIABILITE:** les données représentent-elles la réalité ?
  - « par exemple, un taux d'épisiotomie plus élevé chez les multipares que chez les primipares, des taux d'épisiotomie à moins de 1 % ou à plus de 60 % » (source: Le Monde)

- **EXHAUSTIVITE:** les données sont-elles complètes ?
  - « tous les actes ne disposent pas d'un code spécifique, et même parmi ceux qui en ont, certains, non « tarifés », ne sont pas systématiquement saisis par les soignants, à l'image de l'épisiotomie. » (source: Le Monde)

- **QUALITE:** Les données sont-elles structurées et documentées correctement ?

**VERIFICATION: 4 méthodes** (slide 28)

- Demander à la source: ce sont les meilleurs experts sur les données qu'ils produisent
- Demander aux experts: de bons interlocuteurs quand la source ne coopère pas ou quand il faut choisir entre plusieurs sources
- Vérifications statistiques: moyenne, médiane, maximum, minimum, écart-type
- Bon sens: est-ce que les hypothèses de bases sont vraies?

**Problèmes courants rencontrés lors de la vérification** (slide 31)

- Valeurs manquantes
- Valeurs manquantes remplacées par des valeurs ambiguës comme 0 ou des dates par défaut (1900, 1904, 1969, 1970 sont des défauts courants)
- Lignes ou valeurs en double
- Formats de dates qui varient au sein du même jeu de données
- Unités de mesure non spécifiées
- Noms de colonnes ambigus
- Pas de documentation de la provenance ou méthodologie du jeu de données
- Des valeurs suspectes sont présentes
- Les données ne sont pas assez fines
- Les totaux diffèrent des agrégats inclus
- La feuille de calcul a exactement 65536 lignes (valeur max dans les anciennes versions d'Excel) ou 255 colonnes (valeur max dans les anciennes versions de Numbers)

### From: 2023-2024 Verification & Nettoyage slides (slides 9-19) — Qu'est-ce qu'une donnée

Une donnée = une représentation structurée du monde

Deux axes de qualité:
- **structuration**
- **représentativité**

Quatre problèmes types:
- **données mal encodées** (qualité)
- **bonnes données**
- **hallucinations** (données aberrantes)
- **données falsifiées ou erronées** (fiabilité / exhaustivité)

Exemple illustratif — Importations de véhicules en Côte d'Ivoire:
- Slide 16: données mal encodées (tableau croisé avec années en colonnes, pas tidy)
- Slide 17: bonnes données (format tidy: une ligne par observation, colonnes Mois/Type/Nombre/Année)
- Slide 18: données falsifiées ou erronées — "Que signifie 'Neufs' ?" (définitions ambiguës)
- Slide 19: hallucinations — valeurs impossibles (0, -5, 110.5, -20 pour des nombres de véhicules)

### From: 2023-2024 Verification & Nettoyage slides (slides 24-28) — 3 enjeux de vérification

VERIFICATION: 3 ENJEUX

1. **FIABILITE**: les données représentent-elles la réalité ?
   > par exemple, un taux d'épisiotomie plus élevé chez les multipares que chez les primipares, des taux d'épisiotomie à moins de 1 % ou à plus de 60 % (source: Le Monde)

2. **EXHAUSTIVITE**: les données sont-elles complètes ?
   > tous les actes ne disposent pas d'un code spécifique, et même parmi ceux qui en ont, certains, non "tarifés", ne sont pas systématiquement saisis par les soignants, à l'image de l'épisiotomie. (source: Le Monde)

3. **QUALITE**: Les données sont-elles structurées et documentées correctement ?

### From: 2023-2024 Verification & Nettoyage slides (slide 28) — 4 méthodes de vérification

VERIFICATION: 4 méthodes

1. **Demander à la source**: ce sont les meilleurs experts sur les données qu'ils produisent
2. **Demander aux experts**: de bons interlocuteurs quand la source ne coopère pas ou quand il faut choisir entre plusieurs sources
3. **Vérifications statistiques**: moyenne, médiane, maximum, minimum, écart-type
4. **Bon sens**: est-ce que les hypothèses de bases sont vraies?

### From: 2023-2024 Verification & Nettoyage slides (slide 31) — Problèmes courants

Problèmes courants rencontrés lors de la vérification:

- Valeurs manquantes
- Valeurs manquantes remplacées par des valeurs ambigues comme 0 ou des dates par défaut (1900, 1904, 1969, 1970 sont des défauts courants)
- Lignes ou valeurs en double
- Formats de dates qui varient au sein du même jeu de données
- Unités de mesure non spécifiées
- Noms de colonnes ambigus
- Pas de documentation de la provenance ou méthodologie du jeu de donnée
- Des valeurs suspectes sont présentes
- Les données ne sont pas assez fines
- Les totaux diffèrent des agrégats inclus
- La feuille de calcul a exactement 65536 lignes (valeur max dans les anciennes versions d'Excel) ou 255 colonnes (valeur max dans les anciennes versions de Numbers)

---

## 5. Clean

### From: Scoda notes

**The data pipeline handbook** (`pages/The data pipeline handbook.md`):
> **Action**: Clean
> **Explanation**: It's often the case the data we get and validate is messy. Duplicated rows, column names that don't match the records, values that contain characters which will make it difficult for a computer to process and so on. In this step, we need skills and tools that will help us get the data into a machine-readable format, so that we can analyse it. We're talking about tools like OpenRefine or LibreOffice Calc and concepts like relational databases.

**2024-2025 IJBA curriculum -- Cours 3** (`pages/2024-2025 IJBA curriculum.md`):
> **Identifier les problemes courants :** Reconnaitre les erreurs et incoherences frequentes dans les jeux de donnees brutes (valeurs manquantes, doublons, formats heterogenes, unites absentes, manque de documentation, etc.
>
> **Comprendre les types de nettoyage :** Differencier les trois principales categories d'operations de nettoyage : le Toilettage (mise en forme structurelle sans alterer le contenu), l'Edition (correction et modification du contenu) et le Rapprochement (fusion avec d'autres donnees)
>
> **Appliquer des techniques de "Toilettage" :** Utiliser des fonctions de tableur pour nettoyer la structure des donnees (ex: supprimer les artefacts, scinder/recombiner des colonnes, standardiser des formats simples)
>
> **Appliquer des techniques d'"Edition" :** Utiliser des fonctions de tableur pour corriger ou enrichir le contenu (ex: traiter les valeurs manquantes, identifier/supprimer les doublons, creer des colonnes calculees ou de categorisation)
>
> **Comprendre le principe du "Rapprochement" :** Saisir la logique de fusion de differents jeux de donnees grace a une cle commune

**Cours 3 -- Afternoon session on cleaning** (`pages/Cours 3%3A Verification et nettoyage.md`):
> **14h00 - 14h20 : Transition vers le Nettoyage & Role des LLMs**
> - Introduction 3 types de Nettoyage (Toilettage, Edition, Rapprochement).
> - **Discussion specifique : "Place des LLMs dans le Nettoyage"** (Principes 2 & 3, cas d'usage, importance verification).

> **14h20 - 15h50 : Exercice Pratique 1 : Extraction (Tabula) & Nettoyage Guide (Google Spreadsheet)**
> - Nettoyage Guide : Toilettage (forme) et Edition (fond) avec fonctions Sheets (`TRIM`, `SPLIT`, `IF`, `UNIQUE`...).
> - Mini-demo/Essai LLM : Sur une tache precise (ex: standardiser `type lieu`), montrer prompt, analyser sortie LLM, comparer avec methode Sheets.

**Cours 3 -- Slides on cleaning**:
> **Slides 33-36 : Types de Nettoyage** -- Toilettage (structure), Edition (contenu), Rapprochement (fusion/contexte).
>
> **[NOUVELLE SLIDE 3] : Discussion LLMs et Nettoyage** -- Cas d'Usage (Standardisation texte, Parsing, Suggestion formule/code), Limites (VERIFICATION HUMAINE, prompt, hallucinations).
>
> **Slides 39-42 : "Boite a Outils" Google Spreadsheet** -- Toilettage (`SUBSTITUTE`, `SPLIT`...), Edition (`UNIQUE`, `DATEDIF`, `IF`...), Rapprochement (`FILTER()`, `INDEX(MATCH())`).

**ICT 4 development - 2023-24 crash course syllabus -- Day 3** (`pages/ICT 4 development - 2023-24 crash course syllabus.md`):
> On Day 3, the course shifts focus towards the critical process of data cleaning and consolidation, preparing students to handle the diversity and complexity of combining datasets of varying quality and formats. Leveraging GUI tools such as Google Spreadsheets, OpenRefine, and Tabula, students will refine their collected data, merging it into a coherent dataset ready for analysis.
>
> - Introduction to Data Cleaning Tools: Learn the functionalities and applications of Google Spreadsheets, OpenRefine, and Tabula for data cleaning and preparation tasks.
> - Practical Data Cleaning: Apply these tools to clean the data collected on Day 2, focusing on removing duplicates, correcting errors, and standardizing formats.
> - Data Consolidation: Practice combining data from various sources, including academic databases and APIs, to create a unified dataset.

### From: IRI curriculum

**Module 5, Introduction** (lines 2248-2278):
> There is a common saying among people who work regularly with data that "80 percent of the time spent working with data is spent cleaning it." And indeed, it is often an arduous task that is not only time consuming but can also be error prone. The CLEAN step of the Data Pipeline works as a group with the VERIFY and ANALYZE steps. While simple datasets will have you go through VERIFY, CLEAN and ANALYZE linearly, more complex ones will see you go back and forth between the three.

Three activities:
1. **Data tidying**: cleaning the structure of the data, without touching its content.
2. **Data editing**: modifying the data content to prepare it for analysis.
3. **Data consolidation**: adding complementary data to your main dataset(s).

**Module 5, Section 1 -- Data tidying** (lines 2323-2452):

Two main types of problems:
- **Formatting problems**: multi-line/merged headers, single info stored in multiple columns, multiple data points in single cells.
- **Content problems**: mistakes in case, spelling, or actual values.

Key operations covered:
- Combining columns with `CONCATENATE()`
- Splitting columns with Data -> Split text to columns
- Fixing multi-line/merged headers

Data types sidebar: Numeric, Boolean, Date, String.

**Module 5, Section 2 -- Data editing** (lines 2455-2606):

Key operations:
- Removing extra white spaces with `TRIM()`
- Standardizing case with `UPPER()`, `LOWER()`, `PROPER()`
- Fixing spelling mistakes with Find and Replace (CTRL+H)
- Handling blank/incorrect values using verification methods and source consultation
- Removing duplicates with Data -> Remove Duplicates

**Module 5, Section 3 -- Data consolidation** (lines 2608-2652):

- For small datasets: copy/paste
- For larger datasets: `FILTER()` function to pull matching data from complementary dataset

Best practices:
- Always back up your data
- When using spreadsheets, make a tab for every step of the cleaning process
- Avoid overwriting or deleting data
- Documentation: add notes on what you were doing and how

### From: 2024-2025 SESSION 3 slides

**Récapitulatif: nettoyage -- Toilettage**

Lors du toilettage, vous serez souvent amenés à:
- Enlever les artefacts de mise en forme (e.g. \*NOM\*) --> en utilisant SUBSTITUTE()
- Séparer les données en deux colonnes, par exemple pour séparer une valeur et son unité (e.g. 5 milliards) --> en utilisant SPLIT()
- Aligner les colonnes qui étaient décalées (par exemple après un export Tabula)
- Scindre les données sur plusieurs lignes quand elles sont dans une seule cellule --> par exemple avec SPLIT() et char(10)
- Corriger les problèmes basiques d'orthographe qui affectent les filtres comme les formats de dates et les variations dans l'écriture des noms propres (New York, N.Y.) --> en utilisant: IF() or IFS()

**Récapitulatif: nettoyage -- Edition**

- Valeurs manquantes ou incorrectes: corriger ou supprimer ?
- La seule solution peut être d'abandonner le jeu de données et aller en chercher un autre
- Identifier et enlever les éléments en double --> formule utile: UNIQUE() / fonctionnalité utile: Filters
- Ajouter des colonnes de clarification (e.g. unités de valeur)
- Ajouter des colonnes calculées (e.g. âge des individus quand vous n'avez que leurs date de naissance --> formule utile: DATEDIF()
- Ajouter des colonnes de catégorisation (e.g. tranches d'âges) --> formules utiles: IF() or IFS()
- Enlever des portions de données qui ne sont pas pertinentes pour votre analyse

**Récapitulatif: nettoyage -- Rapprochement**

- Fusion de deux jeux de données (ou plus) en utilisant une colonne commune --> formule utile: FILTER() et INDEX(MATCH())

### From: 2024-2025 SESSION 4 slides (cross-ref: cleaning functions revisited)

**Nos amies les fonctions**

Les plus utiles au nettoyage:
- SPLIT()
- SUBSTITUTE()
- IF()

### From: 2024-2025 Verification alt deck (slides 33-42)

**3 TYPES DE NETTOYAGE**

1. **TOILETTAGE** -- Préparer les données à la vérification ou l'analyse, sans toucher au contenu : nettoyage de la structure des données.
2. **EDITION** -- Préparer les données à l'analyse, en corrigeant les problèmes et/ou en enlevant le superflu: nettoyage du contenu des données.
3. **RAPPROCHEMENT** -- Préparer les données à l'analyse, en les fusionnant avec des données additionnelles qui rajoutent du contexte ou de la précision.

**Astuces à retenir pour l'étape de Nettoyage -- Toilettage** (slide 39)

Lors du toilettage vous serez souvent amené à:
- Enlever les artefacts de mise en forme (e.g. \*NOM\*) --> en utilisant SUBSTITUTE()
- Séparer les données en deux colonnes, par exemple pour séparer une valeur et son unité (e.g. 5 milliards) --> en utilisant SPLIT()
- Aligner les colonnes qui étaient décalées (par exemple après un export Tabula)
- Scinder les données sur plusieurs lignes quand elles sont dans une seule cellule --> par exemple avec SPLIT() et char(10)
- Corriger les problèmes basiques d'orthographe qui affectent les filtres comme les formats de dates et les variations dans l'écriture des noms propres (New York, N.Y.) --> en utilisant: IF() or IFS()

**Astuces à retenir pour l'étape de Nettoyage -- Edition** (slides 40-41)

Lors de l'Édition vous serez amené à faire:
- Valeurs manquantes ou incorrectes: corriger ou supprimer ? La seule solution peut être d'abandonner le jeu de données et aller en chercher un autre
- Identifier et enlever les éléments en double --> formule utile: UNIQUE() / fonctionnalité utile: Filters
- Ajouter des colonnes de clarification (e.g. unités de valeur)
- Ajouter des colonnes calculées (e.g. âge des individus quand vous n'avez que leurs date de naissance --> formule utile: DATEDIF()
- Ajouter des colonnes de catégorisation (e.g. tranches d'âges) --> formules utiles: IF() or IFS()
- Enlever des portions de données qui ne sont pas pertinentes pour votre analyse

**Astuces à retenir pour l'étape de Nettoyage -- Rapprochement** (slide 42)

Lors du Rapprochement vous serez amenés à faire:
- Fusion de deux jeux de données (ou plus) en utilisant une colonne commune --> formule utile: FILTER() et INDEX(MATCH())

### From: 2023-2024 Verification & Nettoyage slides (slides 33-42)

3 TYPES DE NETTOYAGE:

**1. TOILETTAGE**
Préparer les données à la vérification ou l'analyse, sans toucher au contenu : **nettoyage de la structure des données**.

Astuces — Lors du toilettage vous serez souvent amené à:
- Enlever les artefacts de mise en forme (e.g. \*NOM\*) — en utilisant `SUBSTITUTE()`
- Séparer les données en deux colonnes, par exemple pour séparer une valeur et son unité (e.g. 5 milliards) — en utilisant `SPLIT()`
- Aligner les colonnes qui étaient décalées (par exemple après un export Tabula)
- Scinder les données sur plusieurs lignes quand elles sont dans une seule cellule — par exemple avec `SPLIT()` et `char(10)`
- Corriger les problèmes basiques d'orthographe qui affectent les filtres comme les formats de dates et les variations dans l'écriture des noms propres (New York, N.Y.) — en utilisant: `IF()` or `IFS()`

**2. EDITION**
Préparer les données à l'analyse, en corrigeant les problèmes et/ou en enlevant le superflu: **nettoyage du contenu des données**.

Astuces — Lors de l'Edition vous serez amené à faire:
- Valeurs manquantes ou incorrectes: corriger ou supprimer ?
  - La seule solution peut être d'abandonner le jeu de donnée et aller en chercher un autre
- Identifier et enlever les éléments en double — formule utile: `UNIQUE()` ; fonctionnalité utile: Filters
- Ajouter des colonnes de clarification (e.g. unités de valeur)
- Ajouter des colonnes calculées (e.g. âge des individus quand vous n'avez que leur date de naissance) — formule utile: `DATEDIF()`
- Ajouter des colonnes de catégorisation (e.g. tranches d'âges) — formules utiles: `IF()` or `IFS()`
- Enlever des portions de données qui ne sont pas pertinentes pour votre analyse

**3. RAPPROCHEMENT**
Préparer les données à l'analyse, en les fusionnant avec des données additionnelles qui rajoutent du contexte ou de la précision.

Astuces — Lors du Rapprochement vous serez amenés à faire:
- Fusion de deux jeux de données (ou plus) en utilisant une colonne commune — formules utiles: `FILTER()` et `INDEX(MATCH())`

### From: 2023-2024 Verification & Nettoyage slides (slide 38) — Exercice pratique

Exercice:
1. Récupérer le fichier PDF marqué 'EXO'
2. Télécharger le logiciel Tabula (https://tabula.technology/)
3. Extraire les données
4. Vérifier & Nettoyer les données

---

## 6. Analyze

### From: Scoda notes

**The data pipeline handbook** (`pages/The data pipeline handbook.md`):
> **Action**: Analyse
> **Explanation**: This is it! It's here where we get insights about the problem we defined in the beginning. We're gonna use our mad mathematical and statistical skills to interview a dataset like any good journalist. But we won't be using a recorder and a notebook. We can analyse datasets using many, many skills and tools. We can use visualisations to get insights of different variables, we can use programming languages packages, such as Pandas (Python) or simply R, we can use spreadsheet processors, such as LibreOffice Calc or even statistical suites like PSPP.

**ICT 4 development - 2023-24 crash course syllabus -- Day 4** (`pages/ICT 4 development - 2023-24 crash course syllabus.md`):
> Day 4 is dedicated to transforming the cleaned and consolidated data into compelling, data-informed arguments that will enrich the project proposal. Through the use of tools like Google Spreadsheets for analysis and Datawrapper and Flourish for visualization, students will extract meaningful insights and present them in an engaging manner.
>
> - Data Analysis Techniques: Learn the principles of data analysis and basic statistical best practices using Google Spreadsheets.

### From: IRI curriculum

**Module 6, Introduction -- Three types of data analysis** (lines 2655-2687):
> We can distinguish three types of data analysis:
> - **Descriptive analysis** which focuses on describing the basic features of the data, such as the mean, the median, the maximum and so on.
> - **Inferential analysis** which allows you to answer more complex questions about how the phenomena described by the data behave and extrapolate those answers to similar phenomena.
> - **Predictive analysis** which is a more advanced type of inferential analysis, and which aims to make predictions about future events based on past data about these events.
>
> In this module we will explore the methodology for data analysis by coming back to the DEFINE step, which is crucial for your analysis.

**Module 6, Section 1 -- From research question to hypothesis** (lines 2734-2831):

*[Cross-reference: full content under Define -- research questions and hypothesis formation]*

> It is indeed very common to go back and forth between DEFINE, FIND and GET, as you refine your research question.

Hypothesis example (air pollution near schools): (1) Primary schools close to city roads have higher levels of air pollution. (2) The levels of fine particulate matter are twice as large around primary schools right before school starts.

> A hypothesis is interesting only if it is grounded in something concrete -- it could be an assumption shared by many people; or an observation you made in the field.

**Module 6, Section 2 -- Creating your analysis plan** (lines 2832-2875):

> The ANALYZE step starts with the definition of your analysis plan, which is simply the series of transformations that you intend to apply to your data in order to generate the insights that you're looking for. Because the analysis plan comes after you have cleaned the data, each step can be worded in a way that includes the actual column names of your dataset.
>
> Your goal should be that anyone should be able to reproduce your analysis step by step, given that they are provided with your cleaned data and your analysis plan.

Example analysis plan for "primary schools close to city roads have higher levels of air pollution":
1. Calculate distance between PRIMARY_SCHOOL and CITY_ROAD
2. Create DISTANCE_TO_ROAD column and include results
3. For DISTANCE_TO_ROAD < 100M, calculate average of NOx and FPM50 levels
4. For DISTANCE_TO_ROAD > 100M, calculate average of NOx and FPM50 levels
5. Compare the two averages

**Module 6, Section 3 -- Common techniques for data analysis** (lines 2877-3089):

**Pivot tables**: Rows (main variable), Columns (secondary/cross-variable), Values (numerical amounts or counts), Filter (slice the data).

| Analysis step | Rows | Columns | Value |
|---|---|---|---|
| For each state, see number of candidates | State | | Candidate (COUNTA) |
| For each state, see candidates per mode of vote | State | Mode | Candidate (COUNTA) |
| For each party, see number of votes | Party | | Total votes (SUM) |
| For each party, see votes in each state | Party | State | Total votes (SUM) |

**Data visualizations for analysis**: heatmaps via conditional formatting on pivot tables. Reference: [Dataviz catalogue heatmap](https://datavizcatalogue.com/methods/heatmap.html).

### From: 2024-2025 SESSION 4 slides

**Contexte: 3 types d'analyse**

1. **Descriptive** -- Moyenne, médiane, écart-type, maximum...
2. **Inférentielle** -- Corrélation, sondage
3. **Prédictive** -- Modélisation, machine learning

**La méthodo d'analyse**

Un thème:
1. Décomposé en plusieurs hypothèses
2. Qui deviennent des questions d'étapes / d'analyse
3. Reformulées selon les données.

**Exemple appliqué:**

Un thème: Quel impact la rurbanisation a-t-elle sur la fracture numérique ?

1. Décomposé en plusieurs hypothèses: les lieux urbains ont une plus forte densité d'espaces d'accompagnement au numérique.
2. Qui deviennent des questions d'étapes / d'analyse: Il y a-t-il plus de lieux d'inclusion numérique dans les zones urbaines de Bordeaux Métropole ?
3. Reformulées selon les données: si je fais le compte des lieux d'inclusion numérique (colonne "nom") pour chaque zone (colonne adresse_code_insee), je trouverai un compte supérieur dans les zones à forte densité (données à rajouter).

**Exercice: fusionner deux jeux de données (rapprochement, cross-ref avec Clean)**

- On va reprendre le jeu de données nettoyé d'hier
- On va importer dans la même feuille le jeu de données "subventions-metropole-de-bordeaux.csv"
- On va fusionner les données pour pouvoir faire d'autres analyses

**Exercice: analyser des données électorales**

- On va explorer un nouveau jeu de données (élections législatives 2024)
- On se va poser la question: Quelles nuances politiques sont les plus paritaires ?
- Et on va tenter d'y répondre par du nettoyage, rapprochement et de l'analyse

**Exemple de solution:**

Problème: Quelles nuances politiques sont les plus paritaires ?

Hypothèse: les nuances politiques écologiques et de gauche sont plus proches de la parité au niveau des têtes de liste

Étape(s) d'analyse :
- DVG/NUP ont 40-60% de sexe F
- les nuances non-DVG/NUP ont-elles moins de 40% de sexe F

**Les IA et le journalisme de données** (section dédiée, contenu non détaillé dans les slides)

### From: 2024-2025 SESSION 5 slides (cross-ref)

**Le tableau croisé dynamique**

Un outil de vérification, d'analyse, et, combiné avec la mise en forme conditionnelle, de présentation.

**Rappel: Analyse (reprise de l'exercice élections)**

Problème: Quelles nuances politiques sont les plus paritaires ?
Hypothèse: les nuances politiques écologiques et de gauche sont plus proches de la parité au niveau des têtes de liste.
Étape(s) d'analyse :
- DVG/NUP ont 40-60% de sexe F
- les nuances non-DVG/NUP ont-elles moins de 40% de sexe F

### From: 2023-2024 Consolidation & Analyse slides (slides 5-9)

3 CATEGORIES D'ANALYSE:

1. **ANALYSE DESCRIPTIVE**: MOYENNE, MEDIANE, ECART TYPE, MAXIMUM...
2. **ANALYSE INFERENTIELLE**: CORRELATION, SONDAGE
3. **ANALYSE PREDICTIVE**: MODELISATION, MACHINE LEARNING

### From: 2023-2024 Consolidation & Analyse slides (slide 9) — Méthodologie d'analyse

LA METHODOLOGIE D'ANALYSE:
> un thème...
> décomposé en plusieurs hypothèses...
> qui deviennent des question(s)/étape(s) d'analyse…
> reformulées selon les données.

### From: 2023-2024 Consolidation & Analyse slides (slides 11-12) — Exercice législatives

Exemple d'analyse descriptive — Analyse des résultats du 2e tour des législatives 2022:

> Concentrons nous sur l'analyse descriptive
> Pour chaque question, il nous faudra formuler nos hypothèse(s) et étape(s) d'analyse

Problème: Quelles nuances politiques sont les plus paritaires ?
Hypothèse: les nuances politiques écologiques et de gauche sont plus proches de la parité au niveau des têtes de liste
Etape(s) d'analyse:
- DVG/NUP ont 40-60% de sexe F
- les nuances non-DVG/NUP ont-elles moins de 40% de sexe F

_Speaker notes (slide 12): Grandes étapes: Importer la colonne sexe dans l'onglet résultats via FILTER. Faire un tableau croisé dynamique avec les nuances politiques en ligne et en valeur, et le sexe en colonnes. Afficher les valeurs en % de lignes pour comparer F et M. Utiliser la mise en forme conditionnelle pour afficher les lignes de F entre 40 et 60._

---

## 7. Present

### From: Scoda notes

**The data pipeline handbook** (`pages/The data pipeline handbook.md`):
> **Action**: Present
> **Explanation**: And, of course, you will need to present your data. Presenting it is all about thinking of your audience, the questions you set out to answer and the medium you select to convey your message or start your conversation. You don't have to do all by yourself, it's good practice to get support from professional designers and storytellers, who are experts at understanding what are the best ways to present data visually and with words.

**ICT 4 development - 2023-24 crash course syllabus -- Day 4** (`pages/ICT 4 development - 2023-24 crash course syllabus.md`):
> - Data Visualization: Learn about data visualization best practices, and explore useful online tools for refining your visuals such as Datawrapper and Flourish.
> - Data communication strategy: define a strategy to produce and include data-informed arguments and visuals in a proposal for improving the clarity, storytelling and legitimacy of your idea.

### From: IRI curriculum

**Module 7, Introduction** (lines 3092-3117):
> The first question that you must ask yourself at this stage of the Data Pipeline is not 'how do I visualize the data?' but rather, 'what do I want my audience to get out of my project?' Said differently, the key parameters of data presentation are your audience and your message.
>
> All too often, people default to the idea that a data analysis should be presented with a graph of some sort, which is not always the case. After all, how would you present your results on the radio? To people with a visual impairment? To remote communities with no data visualization literacy?
>
> All of this to say that the use of the title 'Presenting Data' instead of 'Visualizing Data' is deliberate. There's also one more reason [...] data visualizations are used throughout the Data Pipeline! They are frequently used for data verification and analysis, which make them not exclusive to the presentation step.

**Module 7, Section 1 -- Choosing your emphasis** (lines 3164-3227):

Three key elements to emphasize:
1. **Emphasizing the data**: simple visualizations, interactivity for precise exploration.
2. **Emphasizing the design**: requires design chops, goal is to make content memorable.
3. **Emphasizing the message**: storytelling at the forefront, interactive formats, infographics.

Data Visualization vs. Infographics sidebar:
> Data visualizations are tightly linked to their underlying data [...] Infographics are information graphics. They are used to present fact-based stories in a visual way. They frequently include data visualizations but are not constrained by any underlying data.

Audience-based presentation choices:
- Within a report: table + simple graph
- Specialist audience: interactive data visualization
- General audience: infographic

**Module 7, Section 2 -- Choosing your visualization** (lines 3229-3425):

Two main considerations: type of data and visualization task.

**Categorical vs. Continuous data** in visualization context:
- Categorical: split across groups (gender, colors, age groups). Bar charts, pie charts.
- Continuous: countable, any value on a scale. Scatterplots, histograms.
- Most charts require a mix of both. Continuous can be displayed as categorical (time -> weeks/months/years).

**Visualization tasks** (from Dataviz catalogue):
Comparisons, Proportions, Relationships, Hierarchy, Location, Part-to-a-whole, Distribution, Flow, Patterns, Range, Data over time.

"I want to show..." task identification table:

| I want to show... | Task |
|---|---|
| The number of adults and children who exercise regularly | Comparison |
| The proportion of adults and children who exercise regularly | Comparison, part-to-a-whole |
| The evolution over time of the number of adults and children exercising regularly | Comparison, pattern, data over time |
| The share of adults and children exercising regularly across men and women | Part-to-a-whole, comparison, hierarchy |

Chart chooser resources:
- [Depict Data Studio](https://depictdatastudio.com/charts/)
- [Juice Analytics](http://labs.juiceanalytics.com/chartchooser/index.html)
- [Dataviz Catalogue](https://datavizcatalogue.com/search.html)

**Module 7, Section 3 -- Tools for data presentation** (lines 3426-3457):

Four categories of tools:
1. **Data wrangling applications**: spreadsheets, BI software (Tableau, Google Data Studio), data analysis software (R, SPSS, Workbench) -- include some visualization.
2. **Data visualization applications**: Datawrapper, Flourish, Raw Graphs, Khartis; libraries (D3.js, Plot.ly).
3. **Information graphics applications**: Piktochart, Canva, Illustrator.
4. **Storytelling applications**: Timeline.Js, Storymap, Tableau dashboards, Flourish multi-step, scrollytelling libraries.

**Module 8 -- Using geographical data** (lines 3460-3707):

> A GIS is a computer-based system that provides four sets of capabilities: Data capture and preparation, Data management, Data manipulation and analysis, Data presentation.

GIS data types: Vector (points, lines, polygons) and Raster (pixelated/gridded).

Key concepts: layers, base layers (Google Maps, OpenStreetMap), foundational layers (geodatabases), external layers (WMS, TMS).

Tools covered: QGIS (free, open-source desktop GIS) and Datawrapper (online choropleth map creation). Walkthrough covers creating a choropleth map of US election data with Datawrapper, from CSV import to embed/share.

**Module 9 -- Going further with spreadsheets** (lines 3710-3796):

> A dashboard is a format of data presentation which aims to:
> - Surface multiple insights on the same interface
> - Make it easy to monitor trends
> - Be easily shareable and printable
>
> Dashboards are meant to be dynamic (i.e., they receive new data regularly). If not, a dashboard is just an infographic.

Covers: conditional formatting, data validation, Google App Scripts for custom functions, interactive dashboard creation in Google Sheets.

### From: 2024-2025 SESSION 5 slides

**Pourquoi parler de présentation et pas de visualisation?**

1. Parce que parfois, le message à tirer des données est plus important que leur représentation stricte.

2. Parce que souvent, visualiser des données n'est intéressant que pour un nombre d'angles limité de votre sujet d'enquête.
   - Sur 8 articles du dossier « conflits d'intérêts dans l'hôpital public » de Sud Ouest, seuls 3 incluent des visualisations de données.

3. Parce que les données peuvent parfois ne représenter qu'une simple étape de votre travail d'enquête: elles ne sont pas une fin en soi.
   - De la même façon que vous n'essayez pas de retranscrire toutes les interviews de témoins dans l'article final, les données n'ont pas nécessairement à être mises en avant.

**3 éléments clés**

Les trois sont à prendre en compte à chaque fois que vous voulez présenter des données, mais une emphase peut être mise sur un aspect plutôt que les autres.

1. **Les données** -- Visualisations simples
2. **La mise en forme** -- Attirer le regard et marquer l'esprit
3. **Le message** -- Domaine des infographies. Storytelling > détails

**La cartographie** (section dédiée)

**Les ressources (outils)**

- Le dataviz catalogue -- datavizcatalogue.com
- Google Sheets
- Rawgraph
- Flourish
- Datawrapper
- Google Data Studio

### From: 2023-2024 Presentation & Cartographie slides (slides 6-9) — Pourquoi "présentation" et pas "visualisation"

> Parce que parfois, le message à tirer des données est plus important que leur représentation stricte

> Parce que souvent, visualiser des données n'est intéressant que pour un nombre d'angles limité de votre sujet d'enquête.
> Sur 8 articles du dossier "conflits d'intérêts dans l'hôpital public" de Sud Ouest, seuls 3 incluent des visualisations de données

> Parce que les données peuvent parfois ne représenter qu'une simple étape de votre travail d'enquête: elles ne sont pas une fin en soi.
> De la même façon que vous n'essayez pas de retranscrire toutes les interviews de témoins dans l'article final, les données n'ont pas nécessairement à être mises en avant.

### From: 2023-2024 Presentation & Cartographie slides (slides 10-13) — La Triade (3 éléments clés)

3 ELEMENTS CLES:
1. **Les données**
2. **La mise en forme**
3. **Le message**

> Les trois sont à prendre en compte à chaque fois que vous voulez présenter des données, mais une emphase peut-être mise sur un aspect plutôt que les autres.

Si emphase sur **LES DONNEES**:
> visualisations simples mais qui détaillent les chiffres ou visualisations qui permettent l'exploration par le lecteur via l'interactivité

Si emphase sur **LA MISE EN FORME**:
> visualisations qui ont pour but d'attirer le regard et de marquer l'esprit

Si emphase sur **LE MESSAGE**:
> infographies qui respectent les données mais ne cherchent pas à les représenter strictement
> storytelling de données

### From: 2023-2024 Presentation & Cartographie slides (slides 14-17) — Outils de visualisation

Outils démontrés:
- **Google Sheets**: visualisation directe (ex: niveau de participation par département)
- **RawGraphs** (https://app.rawgraphs.io/): ex: évolution du nombre de blancs entre 2017 et 2022
- Google Data Studio (https://datastudio.google.com)
- **Flourish**
- **Datawrapper**
- **Infogram**

Emphase sur le message:
> dépend beaucoup plus de l'angle journalistique choisi.
> Exemple: une storymap qui part du nombre de têtes de listes femmes par couleur politique avant de zoomer sur des candidats individuels
> https://storymap.knightlab.com

Liste récapitulative d'outils (slide 17):
- Dataviz: Spreadsheet, Data Studio, Datawrapper, Flourish, Raw Graphs, Plotly Studio, Tableau
- Infographies: Infogram, PiktoCharts
- Storytelling: TimelineJS, StorymapJS

### From: 2023-2024 Presentation & Cartographie slides (slides 18-23) — Cartographie

Outils de cartographie:
- Très simple: **Umap**, **Khartis**
- Plus complexe: **QGIS**, outils très spécialisés (e.g. éditeur de tuiles)

Notions générales:
> Qui dit cartographie dit données géographiques:
> - niveau 0: latitude et longitude
> - niveau 1: point, lignes, polygons (géométries)
> - niveau 2: noms communs (adresses, noms administratifs…)

> Qui dit cartographie dit projection:
> - La projection Web Mercator est la plus connue, mais elle déforme les pôles
> - d'autres projections existent, et ont d'autres usages
> - L'équilibre est généralement entre la préservation des angles vs les distances

> Qui dit cartographie dit fichiers géographiques:
> - shapefiles
> - kml
> - geojson
> - csv avec colonnes lat/lon

Exercice: Khartis (http://www.sciencespo.fr/cartographie/khartis)
> Quelles proportions de têtes de listes hommes ou femmes dans chaque région ?
> Khartis a les délimitations administratives les plus à jour
