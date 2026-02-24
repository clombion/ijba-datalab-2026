# School of Data Pipeline — Compiled Notes Index

## Context
This document compiles, verbatim, every reference to the School of Data data pipeline found across the Logseq vault, organized by pipeline step. Each subsection includes the source file path and title.

---

## The Pipeline as a Whole

### The data pipeline handbook
`pages/The data pipeline handbook.md`

> The Data Pipeline is School of Data's approach to working with data from beginning to end. Once you understand your action cycle and the stakeholders, it will be time to work with the data and we have broken down this process in steps. The Data Pipeline is a work in progress, we started out suggesting five steps, but our community is constantly experimenting and tweaking it to reflect the core steps that are present in every kind of data-driven projects.

### Designing strong LLM harnesses and evaluation for LLM pipelines
`journals/2026_02_18.md`

> The concept of the school of data pipeline (Define, Find, Get, Verify, Clean, Analyze, Present) in the age of AI: it would have helped me identify that the find part (listing documents to be analyzed) is different from the get part (sending a document for processing)

### Curriculum ideas for IJBA
`journals/2026_02_14.md`

> Tasks should ideally align with the steps of a data pipeline (e.g., get, verify, clean, analyze) and not attempt to combine multiple steps into one, allowing for iterative verification.

### 2024-2025 IJBA curriculum — Cours 1: Introduction
`pages/2024-2025 IJBA curriculum.md`

> **Présenter la démarche projet** : Introduire le concept de "data pipeline" comme un cadre méthodologique pour les projets de datajournalisme.

### Cours 3: Vérification et nettoyage — Slides
`pages/Cours 3%3A Vérification et nettoyage.md`

> **Slides 4-7 : Rappel Data Pipeline**
> - Slide 4: Titre de section.
> - Slide 5: Schéma des 7 étapes (Définir à Présenter), mention du caractère non linéaire.
> - Slide 6: Schéma mettant en évidence les étapes déjà vues (Définir, Trouver, Récupérer).
> - Slide 7: Exemple "Maternités Le Monde" illustrant les problèmes rencontrés *après* la récupération (fiabilité, encodage, exhaustivité) et motivant les étapes suivantes.

> **Slide 8 : Focus du Jour**
> Schéma du pipeline mettant en évidence "VÉRIFIER" et "NETTOYER". Texte : "Méthodes de vérification", "Nettoyage de données tabulaires".

### Cours 3: Vérification et nettoyage — Morning schedule
`pages/Cours 3%3A Vérification et nettoyage.md`

> Positionnement dans le "Data Pipeline".

### ICT 4 development - 2023-24 lectures syllabus — Lecture 1
`pages/ICT 4 development - 2023-24 lectures syllabus.md`

> data pipeline across different projects
> - data pipeline steps
> - case study
> - why focus on data collection?

### ICT 4 development - 2023-24 lectures syllabus — Lecture 3
`pages/ICT 4 development - 2023-24 lectures syllabus.md`

> Reminder of where we are in the data pipeline

### Initial ideas and vision for lectures and crash course (Turin 2025-26)
`journals/2025_09_11.md`

> I put a bit less emphasis on the overall data pipeline, because that's too much information in a limited time.

### EITI companies database next step report
`pages/EITI companies database next step report.md`

> use the data pipeline steps to do a mapping of the actions that are mission aligned vs ones that are processing. The use it to show potential for improvements in the pipeline. There's a potential image to explain / visualise showing the different pieces that make an ideal data pipeline in terms of products, tools, processes, the components of that ideal, and the level/path of progress that each scenario enables. Could be a good overall visual for the document, as a red thread to anchor the explanations.

> those strategic objectives are distilled from the ideal view of EITI data pipeline, a sort data-focused theory of change.

### IJBA Quiz — Which stages are not always necessary?
`journals/2025_04_14.md`

> Quelle(s) étape(s) de la data pipeline ne sont pas toujours nécessaires?
> - Nettoyer et Présenter
> - Définir et Vérifier
> - Analyser
> - Nettoyer

### Brainstorming — Asking AI about each step
`journals/2026_02_20.md`

> Ask Gemini about the scoda data pipeline in the Journalism context

> Maybe to see what they have to say about each step of the data pipeline?

### Fellows and Data Experts — Sheena Carmel Opulencia-Calub (Class of 2015)
`journals/2025_08_03.md`

> Her Fellowship was consequently focused on similar work, where she used the data pipeline as a basis for training CSOs and civil servants around the Philippines.

### Fellows and Data Experts — Ali Rebaie (Class of 2013)
`journals/2024_09_16.md`

> Ali went on to become a prominent consultant on the impact of data [...] spreading data skills and educating on the use of the data pipeline methodology to ordinary citizens and journalists.

---

## 1. Define

### The data pipeline handbook
`pages/The data pipeline handbook.md`

> **Action**: Define:
> **Explanation**: Data-driven projects always have a "define the problem you're trying to solve" component. It's in this stage you start asking questions and come around the issues that will matter in the end. Defining your problem means going from a theme (e.g. air pollution) to one or multiple specific questions (has bikesharing reduced air pollution?). Being specific forces you to formulate your question in a way that hints at what kind of data will be needed. Which in turns helps you scope your project: is the data needed easily available? Or does it sound like some key datasets will probably be hard to get?

### Personal note on Tim Davies' article — Define
`pages/Linking Data and AI Literacy at Each Stage of the Data Pipeline – Tim's Blog (highlights).md`

> This relates to the Chris Anderson's 2008 proclamation of the death of the traditional hypothesis-driven scientific enquiry, which should be replaced by BIg Data pattern analysis as a first step for scientific investigations.
>
> More than 10 years later, this prediction fell flat, and as Sam Briddle mentioned it in his Book "New Dark Age: Technology and the End of the Future", this kind of thinking is typical of the solutionism of embedded in "computational thinking" where solving a problem is as simple as breaking it down into smaller parts that can be analysed separately.

### ICT 4 development - 2023-24 crash course syllabus — Day 2 Objectives
`pages/ICT 4 development - 2023-24 crash course syllabus.md`

> Define step of the data pipeline: Practice the process of defining the main research questions and hypotheses of the proposal, including the development of a horizon table

### Day 2: Data Collection and Initial Assessment via Command Line Tools
`pages/Day 2%3A Data Collection and Initial Assessment via Command Line Tools.md`

> Define step of the data pipeline: Practice the process of defining the main research questions and hypotheses [...]

### Designing strong LLM harnesses — What to make static
`journals/2026_02_18.md`

> Statically: [...] define the pipeline

### Personal note on Tim Davies' article — Define + Get + Verify interplay
`pages/Linking Data and AI Literacy at Each Stage of the Data Pipeline – Tim's Blog (highlights).md`

> it shows that the balanced that need to be reached in creating more structured data with AI is embedded in the natural back-and-forth between GET and VERIFY. DEFINE to some extent can be included, because in a context of a project, the "world" that we're looking at is specific.

---

## 2. Find

### The data pipeline handbook
`pages/The data pipeline handbook.md`

> **Action**: Find:
> **Explanation**: While the problem definition phase hints at what data is needed, finding the data is another step, of varying difficulty. There are a lot of tools and techniques to do that, ranging from a simple question on your social network, to using the tools provided by a search engine (such as Google search operators), open data portals or a Freedom of Information request querying about what data is available in that branch of government. This phase can make or break your project, as you can't do much if you can't find the data! But this is also where creativity can make a difference: using proxy indicators, searching in non-obvious locations… don't give up too soon!

### 2024-2025 IJBA curriculum — Cours 2: Recherche et récupération
`pages/2024-2025 IJBA curriculum.md`

> Ce cours a pour but d'approfondir les étapes "Trouver" et "Récupérer" de la *data pipeline*. Cela inclut doter les participants des connaissances et techniques nécessaires pour identifier des sources de données pertinentes, évaluer leur format et leur qualité initiale, et choisir/appliquer les méthodes de récupération appropriées, y compris les bases du web scraping.

> **Contextualiser la recherche de données :** Réviser la place des étapes "Trouver" et "Récupérer" dans la démarche globale ("Data Pipeline").

### Designing strong LLM harnesses
`journals/2026_02_18.md`

> it would have helped me identify that the find part (listing documents to be analyzed) is different from the get part (sending a document for processing)

---

## 3. Get

### The data pipeline handbook
`pages/The data pipeline handbook.md`

> **Action**: Get
> **Explanation**: To get the data from its inital location to your computer can be short and easy or long and painful. Luckily, there's plenty of ways of doing that. You can crowdsource using online forms, you can perform offline data collection, you can use some crazy web scraping skills, or you could simply download the datasets from government sites, using their data portals or through a Freedom of Information request.

### Personal note on Tim Davies' article — Get
`pages/Linking Data and AI Literacy at Each Stage of the Data Pipeline – Tim's Blog (highlights).md`

> Really important concept, as it relates to the very definition of data: Structure representaton of the world. AI can be a powerful agent to create more data by producing more structures. The catch is the balance with the representativity of the AI system, which may create a lot of false positive, or erroneous information.

### 2024-2025 IJBA curriculum — Cours 2
`pages/2024-2025 IJBA curriculum.md`

> approfondir les étapes "Trouver" et "Récupérer" de la data pipeline

### Designing strong LLM harnesses
`journals/2026_02_18.md`

> the find part (listing documents to be analyzed) is different from the get part (sending a document for processing)

---

## 4. Verify

### The data pipeline handbook
`pages/The data pipeline handbook.md`

> **Action**: Verify
> **Explanation**: We got our hands in the data, but that doesn't mean it's the data we need. We have to check out if details are valid, such as the meta-data, the methodology of collection, if we know who organised the dataset and it's a credible source. We've heard a joke once, but it's only funny because it's true: all data is bad, we just need to find out how bad it is!

### Personal note on Tim Davies' article — Verify (Get/Verify interplay)
`pages/Linking Data and AI Literacy at Each Stage of the Data Pipeline – Tim's Blog (highlights).md`

> it shows that the balanced that need to be reached in creating more structured data with AI is embedded in the natural back-and-forth between GET and VERIFY. DEFINE to some extent can be included, because in a context of a project, the "world" that we're looking at is specific.

### 2024-2025 IJBA curriculum — Cours 3: Vérification et nettoyage
`pages/2024-2025 IJBA curriculum.md`

> Ce cours a pour objectif de découvrir les étapes fondamentales de "Vérification" et "Nettoyage" du pipeline de données. Permettre aux participants d'évaluer de manière critique la qualité et la fiabilité des données collectées, d'identifier les problèmes courants, et d'appliquer des techniques de nettoyage et de structuration (principalement via tableur) pour rendre les données exploitables pour l'analyse journalistique.

> **Contextualiser la vérification et le nettoyage :** Réaffirmer la place de ces étapes dans la démarche globale ("Data Pipeline") et leur caractère itératif

> **Diagnostiquer la qualité des données :** Approfondir l'analyse des problèmes potentiels via le cadre structuration/représentativité (données mal encodées, erronées/falsifiées, hallucinations)

> **Maîtriser les concepts de la vérification :** Définir et savoir évaluer les trois dimensions clés : Fiabilité (représentation de la réalité), Exhaustivité (complétude) et Qualité (structure, documentation)

> **Appliquer des méthodes de vérification :** Mettre en œuvre différentes stratégies pour vérifier les données (interroger la source, consulter des experts, effectuer des contrôles statistiques de base, utiliser le bon sens)

### Cours 3: Vérification et nettoyage — Session outline
`pages/Cours 3%3A Vérification et nettoyage.md`

> **9h45 - 10h05 (20 min) : Pourquoi Vérifier et Nettoyer ? Concepts de Qualité**
> - Révision rapide : donnée = représentation structurée.
> - Cadre Qualité (Structure/Représentativité) : mal encodées, erronées, hallucinations. Exemples.

> **11h15 - 11h40 (25 min) : La Vérification : Théorie et Méthodes**
> - Les 3 piliers (Fiabilité, Exhaustivité, Qualité).
> - Les 4 méthodes (Source, Experts, Stats, Bon sens).

> **11h40 - 12h00 (20 min) : Application Vérification "Lieux d'inclusion numérique"**
> - Présentation / Description / Observation collective du jeu de données `met_lieux_inclusion_numerique_EXO.pdf`.
> - **Intégration LLM (5 min) :** Démo/Discussion rapide : Que dit un LLM sur les biais/erreurs potentiels dans ce *type* de données ?
> - Formulation collective des questions de vérification prioritaires pour *ce* jeu.

### Cours 3 — Slides on verification
`pages/Cours 3%3A Vérification et nettoyage.md`

> **Slides 9-19 : Qu'est-ce qu'une donnée ? Concepts Qualité**
> - Slides 10-13: Répétition visuelle "Qu'est-ce qu'une donnée ?" menant à "Une représentation structurée du monde".
> - Slide 14: Axe Structuration vs Représentativité.
> - Slide 15: Schéma 2x2 mappant les problèmes : 'données mal encodées' (qualité/structure), 'bonnes données', 'hallucinations', 'données falsifiées ou erronées' (fiabilité/exhaustivité).

> **Slides 24-28 : Théorie Vérification**
> Les 3 enjeux (Fiabilité, Exhaustivité, Qualité) avec définitions et exemples courts. Les 4 méthodes (Source, Experts, Stats, Bon sens).

---

## 5. Clean

### The data pipeline handbook
`pages/The data pipeline handbook.md`

> **Action**: Clean
> **Explanation**: It's often the case the data we get and validate is messy. Duplicated rows, column names that don't match the records, values that contain characters which will make it difficult for a computer to process and so on. In this step, we need skills and tools that will help us get the data into a machine-readable format, so that we can analyse it. We're talking about tools like OpenRefine or LibreOffice Calc and concepts like relational databases.

### 2024-2025 IJBA curriculum — Cours 3
`pages/2024-2025 IJBA curriculum.md`

> **Identifier les problèmes courants :** Reconnaître les erreurs et incohérences fréquentes dans les jeux de données brutes (valeurs manquantes, doublons, formats hétérogènes, unités absentes, manque de documentation, etc.

> **Comprendre les types de nettoyage :** Différencier les trois principales catégories d'opérations de nettoyage : le Toilettage (mise en forme structurelle sans altérer le contenu), l'Édition (correction et modification du contenu) et le Rapprochement (fusion avec d'autres données)

> **Appliquer des techniques de "Toilettage" :** Utiliser des fonctions de tableur pour nettoyer la structure des données (ex: supprimer les artefacts, scinder/recombiner des colonnes, standardiser des formats simples)

> **Appliquer des techniques d'"Édition" :** Utiliser des fonctions de tableur pour corriger ou enrichir le contenu (ex: traiter les valeurs manquantes, identifier/supprimer les doublons, créer des colonnes calculées ou de catégorisation)

> **Comprendre le principe du "Rapprochement" :** Saisir la logique de fusion de différents jeux de données grâce à une clé commune

### Cours 3: Vérification et nettoyage — Afternoon session
`pages/Cours 3%3A Vérification et nettoyage.md`

> **14h00 - 14h20 (20 min) : Transition vers le Nettoyage & Rôle des LLMs**
> - Synthèse Vérification & Cibles pour le nettoyage.
> - Introduction 3 types de Nettoyage (Toilettage, Édition, Rapprochement).
> - **Discussion spécifique : "Place des LLMs dans le Nettoyage"** (Principes 2 & 3, cas d'usage, importance vérification).

> **14h20 - 15h50 (90 min) : Exercice Pratique 1 : Extraction (Tabula) & Nettoyage Guidé (Google Spreadsheet)**
> - **Extraction (15 min) :** Avec Tabula sur `met_lieux_inclusion_numerique_EXO.pdf`. Export CSV.
> - **Nettoyage Guidé (75 min) :** Import dans Google Spreadsheet. Toilettage (forme) et Édition (fond) avec fonctions Sheets (`TRIM`, `SPLIT`, `IF`, `UNIQUE`...).
> - **Mini-démo/Essai LLM (intégré) :** Sur une tâche précise (ex: standardiser `type lieu`), montrer prompt, analyser sortie LLM, comparer avec méthode Sheets.

### Cours 3 — Slides on cleaning
`pages/Cours 3%3A Vérification et nettoyage.md`

> **Slides 33-36 : Types de Nettoyage**
> Introduction, puis définition et objectif de chaque type : Toilettage (structure), Édition (contenu), Rapprochement (fusion/contexte).

> **[NOUVELLE SLIDE 3] : Discussion LLMs et Nettoyage**
> Titre : "Les LLMs peuvent-ils aider au Nettoyage ?". Bullet points : Principes 2 & 3 (Tâches complexes/vérif facile; Utile si maîtrise), Cas d'Usage (Standardisation texte, Parsing, Suggestion formule/code), Limites (VÉRIFICATION HUMAINE, prompt, hallucinations).

> **Slides 39-42 : "Boîte à Outils" Google Spreadsheet**
> Listes de fonctions et techniques utiles pour Toilettage (`SUBSTITUTE`, `SPLIT`...), Édition (`UNIQUE`, `DATEDIF`, `IF`...), Rapprochement (`FILTER()`, `INDEX(MATCH())`).

### ICT 4 development - 2023-24 crash course syllabus — Day 3
`pages/ICT 4 development - 2023-24 crash course syllabus.md`

> On Day 3, the course shifts focus towards the critical process of data cleaning and consolidation, preparing students to handle the diversity and complexity of combining datasets of varying quality and formats. Leveraging GUI tools such as Google Spreadsheets, OpenRefine, and Tabula, students will refine their collected data, merging it into a coherent dataset ready for analysis.

> - Introduction to Data Cleaning Tools: Learn the functionalities and applications of Google Spreadsheets, OpenRefine, and Tabula for data cleaning and preparation tasks.
> - Practical Data Cleaning: Apply these tools to clean the data collected on Day 2, focusing on removing duplicates, correcting errors, and standardizing formats.
> - Data Consolidation: Practice combining data from various sources, including academic databases and APIs, to create a unified dataset that aligns with the project's objectives and horizon table requirements.

---

## 6. Analyse

### The data pipeline handbook
`pages/The data pipeline handbook.md`

> **Action**: Analyse
> **Explanation**: This is it! It's here where we get insights about the problem we defined in the beginning. We're gonna use our mad mathematical and statistical skills to interview a dataset like any good journalist. But we won't be using a recorder and a notebook. We can analyse datasets using many, many skills and tools. We can use visualisations to get insights of different variables, we can use programming languages packages, such as Pandas (Python) or simply R, we can use spreadsheet processors, such as LibreOffice Calc or even statistical suites like PSPP.

### ICT 4 development - 2023-24 crash course syllabus — Day 4
`pages/ICT 4 development - 2023-24 crash course syllabus.md`

> Day 4 is dedicated to transforming the cleaned and consolidated data into compelling, data-informed arguments that will enrich the project proposal. Through the use of tools like Google Spreadsheets for analysis and Datawrapper and Flourish for visualization, students will extract meaningful insights and present them in an engaging manner.

> - Data Analysis Techniques: Learn the principles of data analysis and basic statistical best practices using Google Spreadsheets.

---

## 7. Present

### The data pipeline handbook
`pages/The data pipeline handbook.md`

> **Action**: Present
> **Explanation**: And, of course, you will need to present your data. Presenting it is all about thinking of your audience, the questions you set out to answer and the medium you select to convey your message or start your conversation. You don't have to do all by yourself, it's good practice to get support from professional designers and storytellers, who are experts at understanding what are the best ways to present data visually and with words.

### ICT 4 development - 2023-24 crash course syllabus — Day 4
`pages/ICT 4 development - 2023-24 crash course syllabus.md`

> - Data Visualization: Learn about data visualization best practices, and explore useful online tools for refining your visuals such as Datawrapper and Flourish.
> - Data communication strategy: define a strategy to produce and include data-informed arguments and visuals in a proposal for improving the clarity, storytelling and legitimacy of your idea.
