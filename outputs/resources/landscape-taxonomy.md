# AI in Journalism: Landscape Taxonomy

A categorization of AI applications in journalism based on 42 episodes of the Newsroom Robots podcast (Jan 2024 -- Jan 2026). Organized by function, with maturity levels and representative adopters.

**Maturity Key:**
- **Proven** = Widely deployed, measurable results, low controversy
- **Emerging** = Multiple deployments, promising results, still evolving
- **Experimental** = Piloted at a few organizations, unclear scalability
- **Nascent** = Discussed conceptually, few or no production deployments

---

## 1. CONTENT CREATION AND EDITORIAL SUPPORT

### 1.1 Transcription and Translation
**Maturity: Proven**

The uncontested winners. Every organization in the corpus uses these.

| Application | Who Uses It | Notes |
|---|---|---|
| Interview transcription | Zetland (Good Tape), BBC, Der Spiegel, Aftonbladet, iTromsoe, Radio Canada, Delfi | Good Tape: $3M revenue, divested. Whisper-based. Delfi: Estonian quality leapt with generative AI. |
| Real-time translation | BBC World Service (42 languages), Delfi (4 Baltic languages), Ippen Digital, The Economist (DeepL + multi-LLM pipeline) | BBC: most mature AI project. Delfi: near-zero cost. Economist: translation identified as most successful AI application. |
| Video translation and dubbing | The Economist (HeyGen) | Lip-sync dubbing of TikTok videos into French, German, Mandarin with voice preservation. |
| Multilingual content adaptation | Ippen Digital (German to easy language), Chicago Public Media (English to Spanish) | SZ easy-language slider for accessibility. CPM: reduced turnaround from "last week's news" to near-real-time. |
| Local/secure transcription | iTromsoe, Radio Canada, Ippen Digital, Hugging Face (Essential AI Toolkit) | Whisper/WhisperX running locally for source protection. Daudens: privacy-first with speaker diarization. |

### 1.2 Summarization and Reformatting
**Maturity: Emerging**

| Application | Who Uses It | Notes |
|---|---|---|
| Article summaries | Aftonbladet, NYT (Echo), SZ, The Economist (Espresso app), Delfi (Breach Media) | Aftonbladet: 40% user expansion rate. Economist: multilingual summaries on Espresso. |
| Newsletter automation | BBC (10 newsletters), Der Spiegel, The Economist (personalized newsletter prototype) | AI for subject lines and instrumental text; humans write leads. Economist: detailed transparency explanation for readers. |
| Content multiplication (article to audio, video, social) | BBC (My Club Daily), Der Spiegel (synthetic podcasts), Aftonbladet (TikTok scripts), BBC (video reformatting) | BBC: synthetic voice podcasts for 5 Premier League clubs. BBC also piloting AI video reformatting across aspect ratios. |
| Multi-source news summarization | Particle (production) | Requires 3+ articles from 2+ publishers per story. Reality check LLM step verifies every claim against sources. |
| Easy-language adaptation | Ippen Digital/SZ | Slider between standard and simplified German. |

### 1.3 Headline and SEO Generation
**Maturity: Experimental (mixed results)**

| Application | Who Uses It | Notes |
|---|---|---|
| SEO headlines | Der Spiegel (~150/day), NYT, Essential AI Toolkit (open-source), YesEo | Spiegel: frees SEO editors. Works for SEO; fails for editorial headlines. Daudens: open-source alternative. |
| Brainstorming headlines | The Economist | Useful as thinking catalyst; proposed headlines rarely used directly. |
| Tabloid headline generation | Aftonbladet (abandoned) | Human editors consistently outperformed AI. |

### 1.4 AI-Generated Visuals and Media Processing
**Maturity: Emerging (with strong constraints)**

| Application | Who Uses It | Notes |
|---|---|---|
| Illustration-style images | Ippen Digital, SZ, Adrian Gill's studio | Universal red line: no photorealism. Illustration only. |
| Alt text for accessibility | BBC | Benchmarked time savings down to the second vs. manual workflow. |
| Campaign imagery | Delfi (national costume selfies) | 20,000 images generated on AWS; no user data stored. Estonian facial expression challenge. |
| AI image editing | Hugging Face (Essential AI Toolkit) | Natural-language object removal for social media thumbnails; replaces Photoshop expertise. |
| Handwriting OCR | Hugging Face (Essential AI Toolkit) | 100% accuracy on difficult handwriting (e.g., US presidential transition letters). |
| Chart-to-data extraction | Hugging Face (Essential AI Toolkit) | Extracts structured data from visual charts into spreadsheets. |
| Video shot listing | Hugging Face (SmallVLM 2) | 250M-parameter model generates complete shot lists locally in minutes; previously took hours. |

### 1.5 Style and Editorial Assistance
**Maturity: Experimental**

| Application | Who Uses It | Notes |
|---|---|---|
| Style guide enforcement | The Economist (custom LLM), BBC (Style Assist) | Economist: 80% accuracy insufficient; "teaching an American to speak British English." BBC: works for style, fails on political nuance. |
| Google Docs style extension | The Economist (in development) | Two-click integration where journalists already work to reduce adoption friction. |
| Custom editorial GPTs | Various newsrooms, BBC ("British Lingo Decoder") | Act as editorial buddies that read stories and give suggestions. |
| Shared prompt libraries | FT (collaborative prompt library), Aftonbladet (25-30 tool "AI buffet"), Radio Canada | FT: treats prompts like code. Lowering threshold through simple prompt wrappers. |

---

## 2. INVESTIGATION AND ACCOUNTABILITY

### 2.1 Document Analysis and Anomaly Detection
**Maturity: Emerging**

| Application | Who Uses It | Notes |
|---|---|---|
| Government document ranking by newsworthiness | iTromsoe (GIN system) | 130 municipalities, 36 newspapers. 60min to 5min daily. |
| Audit report processing | Tordecilla (COA Beat Assistant, Philippines), Phillips (Audit Watch) | Custom GPTs for dense government audit documents. |
| Fisheries anomaly detection | iTromsoe | 5M transactions, 20 years. Led to exclusive police raid coverage. |
| Leaked recording analysis | NYT | 500 hours of Election Integrity Network Zoom recordings. |
| Cross-jurisdictional pattern detection | Phillips (Agenda Watch), iTromsoe | ICE contracts vs. sanctuary city claims; hospital understaffing. |
| Court case monitoring | Delfi | Automated ingestion and summarization of court cases pushed via Teams notifications. 5-6 articles in first month otherwise missed. |
| Open governmental data integration | Delfi | Court cases, tax returns, procurement databases processed at scale for editorial use. |
| Legal filing extraction | Various newsrooms (Marconi) | AI agents extracting data from 200-page filings; 100% accuracy on rote extraction tasks. |
| Public meeting monitoring | Lenfest Collaborative (multiple newsrooms) | AI processing of public records and recordings to restore local coverage capacity abandoned two decades ago. |
| FOIA streamlining | MuckRock, newsrooms (Dhar) | AI to automate bureaucratic processes of filing and tracking records requests. |

### 2.2 AI-Assisted Fact-Checking
**Maturity: Emerging**

| Application | Who Uses It | Notes |
|---|---|---|
| Automated claim extraction and verification | Der Spiegel (full deployment), Symbolic AI, ChatGPT Pro Model | Spiegel: scaled from pilot to full deployment across all content. Symbolic: catches nuanced semantic misrepresentations. Marconi: "AI fact-checking is no longer the flying car of journalism." |
| Multi-step reality checking | Particle (LLM-as-judge) | Additional LLM step double-checks every claim against source material; produces audit log with evidence. |
| Affirmative content verification | Gigafact (McGovern Foundation) | Users submit content for AI-driven assessment of authenticity against surrounding information ecosystem. |
| Bias auditing | Der Spiegel (gender report), Aftonbladet (100K article audit) | AI reveals editorial blind spots rather than just external bias. |
| Bias transparency for audiences | Particle (bias meter), LA Times (Insights) | Human-designated political lean labels mapped to hundreds of sources; displayed alongside AI summaries. |
| Misframing detection | Semafor (Gina Chua) | Identifies what is missing from stories on marginalized communities. |

### 2.3 AI as Investigative Subject
**Maturity: Proven (as journalism practice)**

| Application | Who Uses It | Notes |
|---|---|---|
| Investigating AI systems | AP (Garance Burke), Phillips | Child welfare algorithms, voter chatbot failures, police misconduct. |
| Model testing as journalism | Stanford (Padejski) | Reporting-prompts-regulation pipeline. Co-authoring handbook with Garance Burke on investigating AI. |
| Predictive modeling for journalism | The Economist | Supreme Court decision prediction scoreboard with agent-per-judge architecture. |

---

## 3. DISTRIBUTION AND AUDIENCE ENGAGEMENT

### 3.1 Personalization and Recommendation
**Maturity: Emerging**

| Application | Who Uses It | Notes |
|---|---|---|
| Article recommendation | Times of India (Signals), Ekstra Bladet, JP/Politikens, Chicago Public Media (vendor-based) | TOI: 85% CTR increase. 50% of page views from archival content. CPM: chose ML vendors over LLM-based approach. |
| Push notification personalization | Times of India, Ippen (WhatsApp) | Hyper-local distribution via WhatsApp channels. |
| Personalized news briefings | ChatGPT Pulse, Particle (topic-based ranking) | Pulse: daily briefings from accumulated user data. Particle: personalized without filter bubbles. |
| Format choice (read/listen/summary) | Ippen Digital, SZ | Reader selects preferred format. |
| AI-powered news curation | VG (VGX project), Yle (Finland) | VGX: AI product for younger users tested on non-users. Yle: "first brave steps" in editorial AI curation. |

### 3.2 Conversational Interfaces and Chatbots
**Maturity: Experimental**

| Application | Who Uses It | Notes |
|---|---|---|
| Election chatbot | Aftonbladet (Vi kollar) | 150K questions, zero hallucinations, 10x login conversion. |
| Archive Q&A | Der Spiegel (Chrome plugin), Delfi (25-year archive), Philadelphia Inquirer (Dewey) | RAG-based querying of historical content. Dewey: 40% time savings on archive research, used by newsroom + ad sales + marketing. |
| Audience-facing archive notebooks | The Economist (Google Notebook LM) | Public notebooks for World Ahead 2025/2026 and WWII 1945 content. Partnership with Google. |
| Natural-language data querying | Chicago Public Media (schools data), Phillips (DataTalk/FEC data) | SQL generation from plain English. |
| In-story Q&A | Particle | Users ask questions within stories; AI responds grounded in source material with citations. |
| Conversational news service | Swedish Radio, Aftonbladet | 80% of users press pre-suggested questions rather than typing. |

### 3.3 Voice and Audio Interfaces
**Maturity: Emerging**

| Application | Who Uses It | Notes |
|---|---|---|
| Synthetic voice podcasts | BBC (My Club Daily), Der Spiegel (prototype) | BBC: 2-minute daily football summaries for 5 clubs. |
| Text-to-speech article reading | Der Spiegel, Aftonbladet, BBC (pilot) | Serving immigrant communities in their languages. BBC: read-aloud as UX innovation. |
| On-device TTS in apps | Hugging Face (conceptual) | Small open-source TTS models embedded in news apps for mid-article switching from reading to listening. |
| AI voice cloning / correction | Zetland | Audio producer corrected small mistakes in journalist recordings; prompted updated editorial guidelines. |
| Conversational news service | Swedish Radio | Live beta since March 2025; 80% of users press pre-suggested questions. |
| Voice interaction with archives | NYT (prototyping) | "Talking to the Times" -- early stage. |

---

## 4. OPERATIONS AND INFRASTRUCTURE

### 4.1 Data Infrastructure and CMS Integration
**Maturity: Emerging**

| Application | Who Uses It | Notes |
|---|---|---|
| Vector database / archive indexing | Der Spiegel, Delfi (25-year multilingual), iTromsoe, Philadelphia Inquirer (Dewey), The Economist | Foundation for all downstream AI applications. Inquirer: nightly refresh of new stories. |
| CMS-integrated AI tools | Aftonbladet (one-click summaries), Ippen Digital, The Economist (Google Docs extension) | Tools outside CMS see low adoption. Economist: two-click workflow integration. |
| Internal AI platforms | Der Spiegel (multi-model), Delfi (Azure + Hugging Face), The Economist (AI lab) | Secure access without data leaving infrastructure. Economist: 8-10 person internal startup structure. |
| Data pipelines | Times of India (Growth Rx), iTromsoe (municipal data), Delfi (Microsoft Fabric) | Banking-grade accuracy standards. Delfi: years of foundational data work enabling agile AI deployment. |
| Audio archive transcription | Chicago Public Media (WBEZ) | Unlocking 40+ years of audio journalism for discoverability via AI transcription. |
| Semantic search | The Economist (in-house build) | Replacing Google-powered keyword search for editorial control over rankings and data ownership. |

### 4.2 Training and Literacy Infrastructure
**Maturity: Emerging**

| Application | Who Uses It | Notes |
|---|---|---|
| Organization-wide AI training | Aftonbladet (Prompt Queen), Der Spiegel (870+ trained), Radio Canada (3-tier), Swedish Radio (1,400 staff trained; 1,224 ideas submitted) | Spiegel: sessions book out immediately. SR: bottom-up idea surfacing. |
| AI literacy platforms | SZ (Langdog), NYT (Echo) | Langdog: nearly 50% newsroom adoption. |
| AI literacy in education | Stanford (Padejski), CUNY AI Lab | Padejski: critical thinking first, productivity second. Hands-on comparison of multiple tools. |
| Prompt libraries and AI tool menus | Aftonbladet (25-30 tool "AI buffet"), Radio Canada, FT (shared prompt library) | Lowering threshold through simple prompt wrappers. FT: treats prompts like code. |
| AI competitions and experimentation culture | The Economist (80 entries in internal competition), Delfi (biweekly open discussions) | Economist: open to newsroom and commercial staff. Delfi: pivoted from top-down to peer-driven. |

### 4.3 Business-Side AI
**Maturity: Experimental**

| Application | Who Uses It | Notes |
|---|---|---|
| Ad prospecting | Seattle Times (Lenfest fellow) | Self-funding ROI demonstrated; sold additional advertising quickly out of the box. |
| Churn prediction / subscriber analytics | Times of India, Delfi (Copilot dashboards) | Natural-language querying of business data. Delfi: Microsoft Copilot on Power BI. |
| Ad inventory bot | Delfi (Microsoft Teams bot) | Agentic bot answering questions about ad placements and sales figures. Required significant domain terminology training. |
| Vendor evaluation | Chicago Public Media | AI for comparing vendor feature sets and API robustness. |
| Content repurposing for reach | JournaPilot (McGovern Foundation) | Enables organizations to extend reach and reuse of investigative work. |
| Content licensing marketplace | Particle/Time (Tolbit) | First-of-its-kind online licensed access exchange transaction. |
| Automated weather/traffic reports | Chicago Public Media (WBEZ Slack integration) | AI generates recording-ready scripts in WBEZ editorial voice; replaces 1-2 hours of manual gathering. |

### 4.4 Rapid Prototyping and Development
**Maturity: Emerging**

| Application | Who Uses It | Notes |
|---|---|---|
| AI-assisted prototyping | Delfi (Manus AI + Vercel V0.dev + Google Stitch), Chicago Public Media (Figma Make) | Delfi: working Google Trends prototype with live data in 3 hours. CPM: demos not memos. |
| Vibe coding / LLM code generation | Hugging Face (Daudens), Marconi (Claude Code), various newsrooms | Non-coders building audience-facing apps through conversation. Marconi: sub-agents for parallel research. |
| Screenshot-to-data conversion | Philadelphia Inquirer (ChatGPT) | Converting presentation slide images to data tables; saves ~1 hour per instance. |

---

## 5. MODEL ARCHITECTURE AND TECHNICAL PATTERNS

### 5.1 Retrieval-Augmented Generation (RAG)
**Maturity: Proven (as architectural pattern)**

The consensus approach for any system touching published content. Used by Aftonbladet (election chatbot), Der Spiegel (archive search), iTromsoe (document analysis), Particle (multi-source summaries), Delfi (25-year archive), SZ (reader chatbot), Philadelphia Inquirer (Dewey), and The Economist (Notebook LM archive of 5 years of issues).

### 5.2 Fine-Tuning
**Maturity: Emerging (with caveats)**

| Application | Who Uses It | Notes |
|---|---|---|
| Brand voice adaptation | Ippen Digital (regional style), BBC (Style Assist) | Works for surface features; fails on political nuance. BBC: 60,000 annual submissions, only 12-15K published. |
| Language-specific models | Ippen (German), Delfi (Estonian), Dutch sovereign LLM | Small-language sovereignty argument. Estonian: "Est English" detectable where grammar is correct but sentence structure follows English patterns. |
| Style guide enforcement | The Economist (custom LLM) | 80% accuracy insufficient for Economist standards; struggling with British English rules and Americanisms. |

### 5.3 Multi-Agent Systems
**Maturity: Nascent**

| Application | Who Uses It | Notes |
|---|---|---|
| Multi-agent error checking | VG/Schibsted (production), Particle (LLM-as-judge) | VG: one agent performs task, second agent audits output. Alternative to human-in-the-loop for scale. |
| Agentic web scraping | Delfi, iTromsoe, Phillips, Browser Use (Daudens) | Agents operating browsers to gather public data. Delfi: agents run overnight on governmental databases. |
| Multi-agent research workflows | Marconi (Claude Code) | 10+ sub-agents doing deep research on different topics simultaneously; synthesis agent combines reports. |
| AI-powered analytics agents | Hugging Face (conceptual) | Agents that understand user journeys, suggest editorial improvements, and report on actions; surpasses static dashboards. |
| MCP (Model Context Protocol) | Referenced by Marconi, Chivers, Applied Excel | Marconi: "one of the most underrated disruptions for news." Applied Excel: MCP servers connecting to proprietary data sources. |

### 5.4 Open-Source and Small Models
**Maturity: Emerging**

| Application | Who Uses It | Notes |
|---|---|---|
| Open-source model hosting | Hugging Face (7M users, 1.5M+ models), Delfi (Azure + Hugging Face) | Daudens: switch models in one line of code; avoid vendor lock-in. |
| Distilled/small models for local use | Hugging Face (SmallVLM 2, DeepSeek R1 distilled), Dhar (McGovern Foundation advocacy) | DeepSeek R1 distilled to 7B runs on MacBook with 16GB RAM. Dhar: "we need smaller, more targeted, more power-effective models." |
| Essential AI Toolkit | Hugging Face (Daudens) | Curated set of open-source tools for newsroom tasks: transcription, image editing, OCR, chart extraction, SEO. |

---

## 6. AI NEWS AGGREGATION AND PLATFORM LAYER

### 6.1 AI-Native News Products
**Maturity: Experimental**

| Application | Who Uses It | Notes |
|---|---|---|
| Multi-source AI news aggregation | Particle (Beykpour) | Summaries from 3+ articles/2+ publishers; bias meter; opposite sides; story regeneration; in-story Q&A. |
| AI search as news interface | Perplexity, Google AI Overviews / AI Mode, ChatGPT Pulse | Perplexity: 12 words per query vs. Google's 3. Pulse: personalized daily briefings from accumulated conversation data. |
| AI fact-checking platforms | Symbolic AI (Austin), Gigafact (McGovern Foundation) | Symbolic: auditing feature cross-references every fact against sources and web. Gigafact: public-facing verification tool. |
| Pre-news / anticipatory systems | Applied Excel (Marconi), CNN/CNBC (prediction markets) | Marconi: "age of anticipation" where signals detected before events become news. |

### 6.2 Publisher-Platform Relationships
**Maturity: Nascent**

| Application | Who Uses It | Notes |
|---|---|---|
| Content licensing / access exchanges | Particle/Time (Tolbit), The Economist (Google Notebook LM partnership) | Economist: "give and take" with editorial control over content presentation. |
| OAuth-based LLM content access | Philadelphia Inquirer (proposed), industry-wide discussion | Emerging publisher authentication standard for subscriber content via AI interfaces. |
| Content payment clearinghouses | Multiple competing systems (Lenfest discussion) | Three systems announced: some open-source, some commercial. |
| AI scraper defense | The Economist, publishers broadly | Economist: "losing the war" despite blocking; more AI scrapers than human visitors on some publisher sites. |

---

## 7. CROSS-CUTTING DIMENSIONS

### Scale of Adopter

| Size | Representative Organizations | Characteristics |
|---|---|---|
| **Large** (1000+ journalists) | NYT, BBC, Times of India, The Economist, CNN | Dedicated AI teams (5-10+), custom platforms, enterprise deals. Economist: 8-10 person AI lab as internal startup. |
| **Medium** (100-500) | Der Spiegel, Aftonbladet, JP/Politikens, Delfi, VG | AI hubs or heads of AI, mix of build and buy. Delfi: 400-500 employees with Azure + HF internal platform. |
| **Small** (<100) | iTromsoe (25), Zetland, Chicago Public Media | Resourceful use of open-source tools, shared infrastructure. CPM: 2-person product team + AI fellow. |
| **Collaborative** | Lenfest (10 newsrooms), Big Local News (40+), Polaris (36 newspapers) | Shared engineering, costs, and knowledge. Lenfest: $250K/year per newsroom for first AI engineer. |
| **AI-Native Startups** | Particle, Symbolic AI, Applied Excel, Good Tape | Purpose-built for AI; no legacy constraints. Particle: multi-source aggregation. Symbolic: newsroom fact-checking. |

### Geographic Distribution

| Region | Notable Adopters | Distinctive Pattern |
|---|---|---|
| **Nordics** | Aftonbladet, VG, Zetland, iTromsoe, Delfi, Swedish Radio, SVT | Leading in experimentation culture, public-service AI, and foundation ownership models. |
| **Germany** | Der Spiegel, Ippen Digital, SZ | Strong on ethics infrastructure, fine-tuning, and easy-language accessibility. |
| **US** | NYT, Chicago Public Media, AP, Big Local News, Philadelphia Inquirer, Seattle Times | Investigative applications, collaborative models, and Lenfest AI Collaborative. |
| **UK** | BBC, The Economist | BBC: 42-language translation, fine-tuned editorial models. Economist: translation pipeline, Notebook LM archive, AI lab structure. |
| **Global South** | Times of India, PCIJ (Philippines) | Data infrastructure investment, custom GPT innovation. |
| **Netherlands/Belgium** | NPO (Dutch broadcaster) | Sovereign LLM initiatives, public-service mandate. |
| **Baltics** | Delfi (Estonia, Latvia, Lithuania) | Cross-Baltic real-time translation, world's highest digital subscription penetration (21%), court case monitoring. |
| **Canada** | Radio Canada, Hugging Face (Daudens) | Open-source advocacy, 3-tier training programs, privacy-first transcription. |

### Philanthropy and Institutional Support

| Organization | Role | Notes |
|---|---|---|
| Patrick J. McGovern Foundation (Dhar) | Funder, ethics advocate | Supports Gigafact, MuckRock, JournaPilot. Champions smaller targeted models and journalist-led AI. |
| Lenfest Institute | Collaborative funder | 10 newsrooms, $250K/year each, platform-agnostic. First AI engineers for all 10 organizations. |
| Craig Newmark Philanthropies | Infrastructure funder | Supporting journalism cybersecurity and AI training. |
| Stanford HAI / JSK | Research and education | Padejski: AI literacy curriculum. Storm: LLM + knowledge base research. |
| Harvard Innovation Labs | Incubation support | Supporting Newsroom Robots podcast and emerging AI-journalism research. |
