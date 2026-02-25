<!-- translated -->
---
source: "#121 Escola de Dados — Courses and Tutorials"
url: https://escoladedados.org/cursos/
author: "Escola de Dados (Open Knowledge Brasil)"
year: ongoing
lang: PT
type: guide
access: open access (CC BY 4.0)
status: acquired
note: "Portal + 3 full tutorials fetched (raspagem, busca avançada, limpeza de dados)"
---

# Escola de Dados — Courses and Tutorials

Portal of the Brazilian chapter of School of Data (part of Open Knowledge Brasil).

**Tagline**: "Evidência é poder" (Evidence is power)

## Course Categories
- **Gratuitos** (Free online courses)
- **Pagos** (Paid courses)
- **Sob demanda** (On-demand)
- **Presenciais** (In-person)
- **Laboratórios** (Labs)

## Featured Tutorials
Available at escoladedados.org/tutoriais/:
- Primeiros passos no jornalismo de dados (First steps in data journalism)
- Busca avançada na internet (Advanced internet search)
- Compartilhe tabelas no Google Sheets (Share tables in Google Sheets)
- Raspagem e jornalismo de dados (Scraping and data journalism)
- Limpando bases com o Google Sheets (Cleaning data with Google Sheets)
- Ferramentas simples e gratuitas de raspagem (Simple free scraping tools)
- Guia Quartz para limpeza de dados (Quartz guide for data cleaning)

## Additional Resources
- Blog: escoladedados.org/blog/
- Boletins (Newsletters): escoladedados.org/boletins/
- e-Books: escoladedados.org/ebooks/
- Webinars: escoladedados.org/webinars/

## Events
- Coda.Br (Conference on Data Journalism and Digital Methods)
- Cerveja com Dados (in-person meetups)

## Related
- Programa de membros (Membership program)
- GitHub: github.com/escola-de-dados
- License: Creative Commons Attribution 4.0 International

---

# Tutorial 1: Scraping and Data Journalism

**URL**: https://escoladedados.org/tutoriais/raspagem-e-jornalismo-de-dados/

Data scraping is a technique in which a computer program extracts information from an interface designed for human reading. In journalism, this technique has been applied mainly to extract information from web pages and from documents that are not organized in a structured way, such as PDFs. It is undoubtedly one of the most important tools a journalist can have in investigations involving the web and digital systems.

However, far from being part of journalists' toolkits, computer programs for scraping data are normally written by a computing specialist who understands the necessary steps: how to download content from web pages, recognize patterns in their code, program an extraction routine, and export the data to a structured format such as a CSV file. Computing enthusiasts are increasingly taking an interest in journalism and producing important work and tools, but journalists also need to make an effort to close the gap that exists between computing and journalism.

It is not hard to imagine how data scraping can be useful for newsgathering. Vast amounts of information are scattered across websites and PDF documents provided by government agencies, companies, and organizations. Not only investigative journalism, but service journalism, sports journalism, and cultural journalism also benefit from scraping techniques. Extracting and compiling information scattered around the web into a structured format can make it possible to uncover potential irregularities, correlations, raise important questions, and open paths to producing useful services and tools.

## Scrapers in Journalism

A journalist-programmer could, for example, write a computer program that "scrapes" the photos and geographic coordinates from (public) Instagram accounts of public officials and compare the locations with their public schedules and appearances. If the location of official engagements does not match the coordinates of Instagram photos posted at the same time, we have a potential story.

Data scraping can also help journalists monitor the accountability of government agencies that, despite publishing information on the web, still do not do so in a structured way. This is the case with the Public Security Secretariat of the state of Bahia, which publishes updated information on homicides in the state — the tables are published on the secretariat's website but serve only for human consultation.

Web data scraping has already helped, for example, to profile Chinese censorship on Weibo (ProPublica). The journalist-programmers scraped posts from thousands of accounts for months and then revisited those accounts to find out which posts had been deleted or edited by government agents.

## The Journalist-Programmer

Perhaps data scraping is the technique in service of journalism that most justifies launching any journalist into a programming career. Programming "bots" that perform automated data collection from digital systems is a skill that any journalist of this century must develop. If before we needed to do good "social scraping" to conduct our investigations (talking to sources and building lasting interpersonal relationships), today, in addition to that, we need to extend those skills to the digital realm using computing techniques.

Data journalism extends an invitation to the journalist interested in getting to know other fields, reducing the degree of dependency we have on certain subjects. Being able to talk with a programmer about a journalistic idea that takes advantage of technological means will only happen if we allow ourselves to enter, even if only a little, the world of computing.

At Escola de Dados it is possible to learn web and PDF data-scraping techniques without needing to learn to program. However, these techniques allow for medium-complexity scraping — they do not allow data to be scraped from a website with automated frequency nor information to be extracted from sites that require authentication. These limitations are overcome through scrapers built with programming code.

## Learning to Program

Many universities in the US already offer courses that blend journalism and computer science skills (Columbia, Northwestern). In Brazil the subject is starting to enter academic curricula. Resources for learning: Python para Zumbis (PT), Codecademy, edX, Coursera, Exercism.

---

# Tutorial 2: Advanced Internet Search

**URL**: https://escoladedados.org/tutoriais/busca-avancada-na-internet/

Search engines like Google — and there are others, such as Bing, DuckDuckGo, etc. — are the most important documentary information systems of our time. Before explaining how to perform an advanced search on the internet, it is important to understand the anatomy of a search engine, or its search motor.

The search engine is a documentary information system that accepts two types of inputs:
- **Documents**: web pages, PDFs, and spreadsheets
- **Information needs**: the questions asked by internet users

The output of the system is a list of links to sites that presumably contain information capable of satisfying the user's needs.

### Structure of a Search Engine

A search engine consists of two main groups:
1. **Exploration system** (crawler/spider): discovers and copies sites and documents from the web
2. **Information retrieval system**: comprises the indexing system (document analysis) and the query system (user interface)

### Relevance Calculation

Search engines combine criteria to determine relevance:
- **Internal/intrinsic**: keyword frequency, presence in HTML tags, presence in the URL
- **External/popularity**: number of external links pointing to the page

Google uses more than 200 different signals to determine results, including terms on websites, content freshness, user region, and PageRank.

## Query Languages

"Query language" — the role of the query language is to transform an information need into a formula that a robot can interpret.

## Boolean Logic

Originated with Irish mathematician George Boole (19th century). Applied to searches:

| Operator | Example | Meaning |
|----------|---------|---------|
| AND | prevention AND alcoholism | Both words present |
| OR | prevention OR alcoholism | At least one present |
| NOT | prevention NOT alcoholism | First present, second absent |

**Complex Boolean**: combines three or more words with parentheses. E.g.: `(alcohol OR amphetamines) AND (treatment OR prevention)`

Main advantage: expresses the characteristics of the information need with near-precision. Main disadvantage: counter-intuitive for the end user.

## Google Search Operators

- `site:` — search only within a specific site
- `filetype:` — search for specific file types (.pdf, .xls)
- `-` (minus) — exclude results containing certain words
- `+` — require that a word be present
- `""` (quotes) — exact phrase
- `*` (asterisk) — wildcard character
- `..` (two dots) — numeric range. E.g.: camera $50..$100

Combination: `"sustainable development" site:ufrj.br filetype:pdf`

### Searching with Google Images

Reverse image search: upload a file or drag an image into the search box to find information, similar photos, or related publications.

---

# Tutorial 3: Cleaning Data with Google Sheets

**URL**: https://escoladedados.org/tutoriais/limpando-bases-com-o-google-sheets/

Although Google Sheets is a web application designed for spreadsheet processing, it is possible to perform quick clean-ups using a few functions. Practical example: cleaning a table scraped from a PDF from the Rio de Janeiro Public Security Institute using PDFtables.

### Importing the File
From any spreadsheet in Google Sheets: File > Import > Upload. Drag the table file into the browser window.

### Removing the Bulk
Delete unnecessary rows: select rows, right-click > "Delete rows." Standardize font (Arial, size 10). Rename columns.

### New Column
Create a separate "Category" column when categories are mixed in with data. Right-click on the column > "Insert 1 to the right."

### Filling Blank Cells
Click on the value and drag the blue square in the lower-right corner of the cell to fill the cells below.

### Automatic Formatting
Use `=proper(b2)` to standardize capitalization. Then: select column > Copy > Paste Special > "Paste values only" to convert formulas into fixed text.

### Sorting and Grouping to Delete
Add an asterisk in front of category names, sort A-Z to group them at the top, then delete them all at once. Important: freeze the first row before sorting.

### Find and Replace
Edit > Find and replace. Type "-" in the first box, leave the second blank > "Replace all."

### Locale
File > Spreadsheet settings > select the appropriate locale for correct interpretation of numbers and dates.
