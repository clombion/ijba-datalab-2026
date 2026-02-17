# Case Studies: AI in Journalism

12 standalone case studies drawn from the Newsroom Robots podcast (2024-2026). Each includes the organization, what they did, tools used, outcome, and discussion questions for classroom use.

---

## 1. iTromsoe: A 25-Person Newsroom Outperforms Its Competitors with AI

**Organization:** iTromsoe / Polaris Media, Tromsoe, Norway
**Episode:** Rune Ytreberg & Lars Adrian Giske, February 2025

**What they did:** iTromsoe, a local newsroom of just 25 journalists, built a suite of AI tools for investigative journalism. Their GIN system ingests municipal planning documents from 130 municipalities, ranks them by newsworthiness using a model trained on senior journalists' editorial judgment (thumbs up/down ratings that outperformed manually curated entity lists), and delivers a prioritized daily briefing. Separately, they built a fisheries database analyzing 5 million fishing transactions across 20 years to detect anomalies in Norway's second-largest industry. They also developed domain-specific RAG-based research assistants for FOIA document analysis, including one that uncovered an X-ray crisis at the University Hospital of Northern Norway where at least five people died due to a freelance doctor spending insufficient time reviewing images.

**Tools:** Custom-built GIN system (combining generative AI, classical ML anomaly detection, and traditional if-then coding), RAG-based research assistants, OpenAI and Anthropic APIs, vector databases, Python scripts for PDF-to-JSON conversion, Slack notification bots, OCR assistant, LAILA research assistant.

**Outcome:** GIN compressed daily document review from 60-90 minutes to 5 minutes. Two summer interns produced five cover stories in their first week. The fisheries database detected a company engaged in non-sustainable practices -- when police raided the facility, iTromsoe was there ten minutes after officers because they already knew the target. The system now serves 36 Polaris newspapers. Four municipalities started publishing data openly after seeing the tool's value. A cross-border collaboration with Sweden's Goteborgs-Posten used batch processing to generate timelines from hundreds of documents after discovering RAG limitations on aggregation tasks.

**Discussion Questions:**
1. How does the codification of senior journalists' editorial judgment into an AI system change the nature of newsroom expertise? What is gained and what is lost?
2. iTromsoe is competing against a newspaper twice its size. Does AI give small newsrooms a structural advantage, or does it simply narrow the gap?
3. The fisheries investigation relied on AI-detected anomalies. What are the risks of investigative journalism becoming dependent on what algorithms flag as unusual?

---

## 2. Aftonbladet: Building an Election Chatbot with Zero Hallucinations

**Organization:** Aftonbladet, Stockholm, Sweden
**Episode:** Martin Schori, September 2024

**What they did:** Scandinavia's largest newspaper (reaching 4 million of Sweden's 10 million people daily) built an AI chatbot for the 2024 EU elections called "Vi kollar" (We check). The chatbot used a RAG architecture with nearly 100 authoritative sources -- party manifestos, official EU documents, and Aftonbladet's own election coverage -- so the AI could only answer from verified material. Users had to log in to use it. The chatbot was part of a broader AI strategy led by an editorially staffed AI Hub that also built an "AI buffet" of 25-30 tools including a follow-up story suggestion tool, a TikTok manuscript generator, a proofreading tool (built by a journalist with no programming experience), and a content diversity audit using MediaCatch that analyzed approximately 100,000 articles.

**Tools:** OpenAI GPT-4o, RAG model with curated source database, Schibsted transcription tool, MediaCatch (content analysis), Custom GPTs, Midjourney.

**Outcome:** The chatbot received 18,000 questions on day one and 150,000-160,000 total over two weeks. 60% were original user questions rather than pre-suggested prompts. Zero hallucinations were detected across the entire election period. Login conversion was nearly tenfold higher than typical initiatives. Users actively tried to trick the bot into expressing political bias -- it refused. The content diversity audit revealed a gender gap larger than expected across coverage. Notably, Schori reported that AI headline generation consistently failed to match the quality of Aftonbladet's human tabloid editors.

**Discussion Questions:**
1. Aftonbladet's management was initially reluctant because the EU elections are low-engagement in Sweden and the chatbot would publish without per-answer editorial review. How should newsrooms evaluate risk for AI-generated audience-facing content?
2. The chatbot required nearly 100 curated sources. What does this reveal about the relationship between AI reliability and editorial preparation?
3. Should a news chatbot refuse to give voting recommendations? Where is the line between informing and advising?

---

## 3. The New York Times: AI Semantic Search for Investigative Journalism

**Organization:** The New York Times, New York, USA
**Episode:** Zach Seward, May 2025

**What they did:** The NYT's five-person AI team used AI to support major investigations. For a story on the Election Integrity Network, reporters obtained 500 hours of leaked Zoom recordings. Traditional keyword search would miss relevant discussions because participants used different language to describe the same topics. The team transcribed all recordings with AI, then used LLM-based semantic search guided by reporters' domain expertise to find discussions about RNC connections, funding sources, and targeting of immigrant communities. For vetting Trump cabinet nominees, the team downloaded voluminous TV and video appearances, transcribed them, and used LLMs to search for specific topics. They also built Echo, an internal summarization platform, after a 100-person pilot program revealed that more than half of identified workflow problems involved summarization.

**Tools:** AI transcription, LLM semantic search, computer vision (for speaker identification in video), Echo (internal summarization/transformation platform wrapping multiple LLMs with both web playground and API access), embedding models for improved website search.

**Outcome:** The LLM identified euphemisms and indirect references that keyword searches missed entirely. For Pete Hegseth, AI found references to drinking habits through phrases like "getting blitzed" and "having a rager" rather than explicit terms. Computer vision was used to distinguish when Tulsi Gabbard was speaking versus being discussed by others on TV. Echo was deployed across over half the 2,000-person newsroom, enabling individual desks to solve their own summarization needs without centralized project management. The NYT deliberately avoided CMS integration, viewing short-term integrations as less important than long-term ambitious plans. Seward's key design lesson: journalist agency over AI prompts -- making prompts transparent and editable -- proved more important than any fancy feature.

**Discussion Questions:**
1. Seward argues AI's value is "creating structure out of unstructured data sets," not generating prose. How does this reframe what journalism students should learn about AI?
2. The NYT deliberately avoided CMS integration, unlike competitors. What are the tradeoffs between embedding AI in workflows and building standalone tools?
3. Seward says AI will not differentiate newsrooms -- access to documents and sources will. Do you agree?

---

## 4. Der Spiegel: Using AI to Audit Your Own Bias

**Organization:** Der Spiegel, Hamburg, Germany
**Episode:** Ole Reissmann, June 2024

**What they did:** Germany's leading news magazine used AI to conduct a gender representation audit of its own coverage. The system automatically extracts names from articles, identifies gender, and produces monthly departmental reports showing the balance of men and women mentioned across all content. The project ran for multiple years, building longitudinal data on representation patterns. Beyond the gender audit, Der Spiegel built an internal AI platform on Microsoft Azure providing secure access to multiple AI models within European data protection guidelines, trained over 870 staff in AI fundamentals, developed an AI-assisted fact-checking tool that extracts factual statements and verifies them against multiple sources, and built a Chrome browser plugin that surfaces contextual information from the Spiegel archive.

**Tools:** GPT (for name extraction and gender identification), internal AI platform (Microsoft Azure, ChatGPT Enterprise, Google models), AI fact-checking tool with confidence scoring, Chrome browser plugin with RAG-based archive search, text-to-speech, Midjourney, DALL-E.

**Outcome:** The audit revealed that significantly more men than women appeared across Spiegel's coverage -- confirming a systemic blind spot. The data was broken down by department, allowing targeted editorial conversations. The fact-checking tool gets journalists 20-40% of the way to verification, allowing the department to focus on more complex tasks. Reissmann described the irony: "There's so much talk about AI LLMs being biased. And now it's actually an LLM that's helping us discover our biases. I think that's quite beautiful." He also noted that Der Spiegel refuses to use photorealistic AI-generated images because they "do not want to make up the truth or trick anybody."

**Discussion Questions:**
1. How does using AI to audit editorial bias differ from traditional diversity audits? What can AI detect that humans overlook?
2. What should a newsroom do with gender imbalance data once they have it? Is measurement enough, or does it require structural changes?
3. The AI's gender identification was "not 100% accurate." How should newsrooms handle the imperfections of AI-driven auditing tools?

---

## 5. Good Tape / Zetland: From Newsroom Tool to $3M Business

**Organization:** Zetland, Copenhagen, Denmark
**Episode:** Tav Klitgaard, December 2025

**What they did:** Zetland, a Danish membership-based digital publication where 45% of paying members are in their twenties or thirties, built an internal transcription tool called Good Tape, based on OpenAI's open-source Whisper model. A developer discovered the Whisper model through a GitHub commit. Danish-language transcription tools had been "totally useless" because no one invested in small languages. When the developer showed the tool to colleagues, journalists called it "magic." CEO Tav Klitgaard told the team: "Stop everything, allocate all resources to this project." Good Tape launched the day before the first version of ChatGPT, giving Zetland early organizational learning about AI concepts like hallucinations.

**Tools:** OpenAI Whisper (open-source), custom wrapper and security layer, AI translation (internal productivity), AI voice cloning (discovered being used by audio producer).

**Outcome:** Good Tape became a subscription product sold globally to journalists, researchers, therapists, lawyers, and consultants. It reached approximately $3 million in revenue -- a significant fraction of Zetland's total revenue -- and was profitable almost immediately. It was later successfully divested as part of a larger transaction with Bonnier News. The brand trust of being "built for journalists" became a selling point: users associated journalism with high-quality data protection. Klitgaard said: "It's not just GDPR -- that's table stakes. It's source protection. It cannot leak." The early adoption also removed newsroom fears that AI was "out for people's jobs" because staff saw it practically solving real problems from day one. An audio producer was discovered using AI voice cloning to correct journalist recordings without editorial knowledge, leading Zetland to update its principles to address this use case.

**Discussion Questions:**
1. Good Tape's market proved much larger than journalism. What other newsroom pain points could become commercial products?
2. Zetland's journalism-grade data protection became a competitive advantage in the broader market. What does this suggest about the commercial value of editorial standards?
3. An audio producer was discovered using AI voice cloning to correct journalist recordings without editorial knowledge, violating guidelines. How should newsrooms handle policy violations when the intent is innocent?

---

## 6. AP Investigations: Journalism as AI Accountability

**Organization:** Associated Press, USA
**Episode:** Garance Burke, July 2024

**What they did:** AP global investigative reporter Garance Burke led a series of investigations into AI systems affecting real people. Her team investigated a child welfare algorithm in Allegheny County, Pennsylvania, that used sensitive family data -- including maternal smoking history, disability status, and family size -- to predict which children were at risk. The algorithm overrepresented communities of color. In a separate investigation conducted in collaboration with Proof News, the team tested the five most popular chatbots with basic questions about U.S. democracy. Burke developed a systematic framework for investigating AI: who built it, how does it work, who benefits, who is harmed, and whether it is regulated. She also investigated government agencies using predictive and surveillance tools post-COVID to monitor marginalized populations, and examined Brad Parscale's AI-powered political campaign platform.

**Tools:** Chatbot testing (five popular chatbots), public records analysis, algorithmic auditing methodology, synthetic datasets for simulated user experience testing, GitHub examination of AI model logs.

**Outcome:** The child welfare algorithm reporting prompted a federal civil rights investigation by the U.S. Department of Justice. Chatbot testing revealed that one told a Philadelphia resident in a predominantly Black neighborhood there was no polling place, and another told California voters they could vote by text message. A sentencing tool trained on historical data was found to reproduce bias where Black offenders typically received longer terms than white offenders for the same crimes. Burke argued that journalism functions as a de facto regulator of AI: "AI systems are really unregulated by and large around the world." She emphasized that journalists don't need to be engineers to interrogate AI systems -- journalistic street smarts are sufficient.

**Discussion Questions:**
1. Burke frames investigative journalism as AI's primary accountability mechanism. Is this a sustainable model, or should formal regulation take over?
2. The chatbot voting errors could have real democratic consequences. How should journalists approach testing AI systems that affect public participation?
3. Burke's framework: who built it, how does it work, who benefits, who is harmed. How does this map to traditional investigative journalism methods?

---

## 7. Times of India: Personalization Without Sacrificing Editorial Judgment

**Organization:** The Times of India, India
**Episode:** Ritvvij Parrikh, October 2024

**What they did:** Senior Director of Product Ritvvij Parrikh built Signals, an in-house recommendation system that personalizes news delivery while preserving editorial guardrails. The system uses minimal data points per story and per user ("the least amount of information that can give us the highest return") and includes an editorial moderation layer allowing human editors to reject inappropriate recommendations. The system is self-learning: it dynamically adjusts when story supply fluctuates (e.g., after the 4-5 AM print dump versus lower midday output) without hard-coded rules. Parrikh also built Growth Rx, a real-time clickstream data pipeline with banking-level accuracy standards, replacing reliance on delayed Google Analytics data.

**Tools:** Signals (in-house recommender), Growth Rx (in-house real-time data pipeline), BigQuery, editorial training data (evergreen vs. non-evergreen tagging).

**Outcome:** Signals achieved a sustained 85% CTR increase on web and 30-40% on app over 1.5 years. 50% of personalized page views came from stories older than two days, proving it could recirculate evergreen archive content. The system self-adjusts when story supply fluctuates. Parrikh drew an analogy: "There is no rich country with low energy. Similarly, there is no rich media company that doesn't have strong data pipelines." He argued that newsrooms should adopt recommender systems before investing in LLMs, noting: "Generative AI is two, three years old. Recommender systems have been around for 15 years. We've not fully adopted those and we are imagining that we can participate in the LLM race. It's not practical."

**Discussion Questions:**
1. Parrikh argues data infrastructure is the prerequisite for AI, not the AI itself. What does this mean for newsrooms that have not invested in data pipelines?
2. The system uses "data minimization" -- the fewest data points possible. How does this contrast with Big Tech's data-maximalist approach, and what are the editorial implications?
3. Two recommender systems with identical engagement metrics can produce radically different editorial effects (per JP/Politikens research). How should newsrooms evaluate recommendation algorithms beyond clicks?

---

## 8. Big Local News: AI-Powered Accountability Journalism at Scale

**Organization:** Big Local News, Stanford University, USA
**Episode:** Cheryl Phillips, May 2025

**What they did:** Cheryl Phillips built a shared infrastructure enabling local reporters -- many covering 20+ cities solo -- to do accountability journalism previously impossible without large teams. Agenda Watch scrapes municipal government meeting agendas from hundreds of agencies by targeting the platform companies they contract with, enabling keyword search and pattern detection across jurisdictions. DataTalk, built with the Stanford Oval Lab using SUQL, provides natural-language querying of FEC campaign finance data with built-in transparency: it shows SQL-like query steps, plain English explanations, caveats, and a shareable dashboard. Autofolio extracts entities from police misconduct records across California's 700+ police agencies. Audit Watch scrapes the federal audit clearinghouse daily for problematic audits of entities receiving $750,000+ in federal funds. A Starling Lab collaboration uses blockchain to authenticate and preserve police body camera footage with immutable provenance trails.

**Tools:** Custom scraping infrastructure, ML anomaly detection, DataTalk (Stanford Oval Lab), SUQL, Autofolio (entity extraction), BillTrack 50, Starling Lab (blockchain provenance), Slack alert bots, Ping Pong (walled-garden RAG for teaching), audio analysis ML for meeting newsworthiness detection.

**Outcome:** The system uncovered that Santa Clara County (Silicon Valley) had the most ICE contracts in California despite being in a sanctuary state, with officials proclaiming non-cooperation with ICE the day after signing new contracts. Student teams published stories in the Honolulu Civil Beat, Bay City News, and Atlanta Journal Constitution. The AJC team analyzed campaign spending in swing counties on abortion issues married with ad spending data. The Baltimore Banner published 3-4 stories from WARN Act layoff data (scraped from 44 states) delivered via Slack alerts. A drug overdose data analysis revealing disproportionate deaths among older Black men in industrial cities was published with the New York Times and Baltimore Banner, with county-level data shared to 11+ additional local newsrooms.

**Discussion Questions:**
1. Phillips's tools enable individual reporters covering 20+ cities. Does this represent empowerment or an acceptance of industry contraction?
2. The ICE contracts story was only possible by cross-referencing datasets. What types of accountability journalism become possible when AI can merge data across jurisdictions?
3. Phillips delays introducing AI tools until three-quarters through her curriculum, building fundamentals first. Do you agree with this pedagogical approach?

---

## 9. BBC: Fine-Tuning an LLM for Editorial Style Across 42 Languages

**Organization:** BBC News, London, UK
**Episode:** Olle Zacharison, November 2025

**What they did:** BBC News, with 5,500 people operating in 42 languages, built a bespoke fine-tuned LLM called Style Assist. It rewrites articles from 150 local democracy reporters to align with BBC editorial standards, trained on paired datasets of incoming articles and their edited/published versions. The BBC also deployed AI translation across the World Service with a side-by-side interface showing original text, AI translation, and human sub-edit, boosting output specifically in BBC Mundo. Additional projects include AI-generated alt text for accessibility (with time savings benchmarked to the second), video reformatting across aspect ratios for social media, newsletter production assistants, and My Club Daily -- a synthetic voice podcast covering five Premier League clubs. Zacharison organized AI strategy around four themes: boost productivity, reformat content, augment journalism, and innovate user experiences.

**Tools:** BBC fine-tuned LLM (Style Assist), AI translation tools, AI transcription, synthetic voice (My Club Daily podcast, article read-aloud), Microsoft Copilot, Google NotebookLM, AI-powered video reformatting, customized GPTs.

**Outcome:** Translation became the BBC's most mature AI project with precise time-savings metrics. Style Assist performed well on formatting and tone but struggled with political impartiality nuances -- the "undertext" in local political reporting proved impossible to encode. Of 60,000 annual article submissions from local democracy reporters, only 12,000-15,000 are currently published; the tool aims to increase that. At Swedish Radio, Zacharison's previous post, a basic AI training course for all 1,400 staff generated 1,224 idea submissions through a free text field -- "some so brilliant that we could never think them up in a strategy team." His guiding principle: "People don't come to the BBC News app to get AI. You go there to get credible news."

**Discussion Questions:**
1. Style Assist can handle formatting but not political impartiality. What does this boundary reveal about what AI can and cannot learn from editorial data?
2. The BBC operates in 42 languages. How does scale change the calculus for AI translation versus human-only translation?
3. Zacharison said current AI investments have "negative ROI." How should public-service broadcasters evaluate AI investment when their mandate is not profit?

---

## 10. Sueddeutsche Zeitung: Building Trust Through Transparent AI Design

**Organization:** Sueddeutsche Zeitung (SZ), Munich, Germany
**Episode:** Alessandro Alviani & Fabian Heckenberger, January 2026

**What they did:** SZ, Germany's largest subscription newspaper, developed a comprehensive approach to trustworthy AI products. They created a consistent AI design language -- branded colors, frames, and clear labels -- across all AI-generated content, publishing a designer deep dive explaining why colors alone are insufficient for transparency labeling. They built an expert-in-the-loop model where article authors (not generic reviewers) verify AI summaries, with a feedback system that compares AI-generated output against the final published version to self-learn over time (e.g., learning that SZ writes "FIFA" in lowercase). They deployed live monitoring with sensitive keyword alerts and Slack notifications during their German general election chatbot, adjusting prompts and guardrails multiple times per day. They built easy-to-understand article versions using a multi-LLM pipeline (one LLM translates, a second LLM-as-judge checks against the original, then the author reviews). And they published a transparency blog explaining their AI use, plus a technical deep dive including prompt excerpts.

**Tools:** Fine-tuned LLMs on proprietary corpus, Langdog (Berlin-based AI literacy platform enabling multi-LLM testing, prompt sharing, and peer-to-peer assistant building), RAG-based election chatbots (EU 2024 and German general election 2025), LLM-as-judge verification, CMS-integrated SEO assistant, Figma-based social media tool, AI-supported WhatsApp channels for eight Munich districts, live monitoring systems.

**Outcome:** SZ achieved nearly 50% newsroom adoption via Langdog, projected to reach 70-75%. One science editor's custom assistant for chatting with 300+ page scientific studies generated 30+ colleague adoption requests in two hours -- demonstrating that bottom-up peer demonstration scales faster than top-down mandates. The easy-language articles deployed during the German election and a multi-party investigation into sheltered workshops received "extremely positive" reader feedback, with users asking for expansion to all articles. AI-supported WhatsApp channels enabled hyper-local content coverage across eight Munich districts that would not have been possible without the AI layer. Alviani articulated the key operational insight: "There is no done column when we build AI products. It's continuous learning, continuous monitoring."

**Discussion Questions:**
1. SZ's expert-in-the-loop requires article authors -- not generic reviewers -- to check AI summaries. Why does this distinction matter for accuracy and accountability?
2. A consistent AI design language (branded colors, labels) represents a product design commitment to transparency. Should this become an industry standard?
3. SZ asks: "Can you reinvest the time savings in new formats?" How does this question prevent efficiency gains from being absorbed by budget cuts?

---

## 11. Lenfest AI Collaborative: Embedding Engineers in Under-Resourced Newsrooms

**Organization:** Lenfest Institute for Journalism (10 newsrooms), USA
**Episode:** Jim Friedlich, David Chivers & Matt Boggie, December 2025

**What they did:** The Lenfest AI Collaborative placed AI fellows -- at $250,000 per year each -- as the first-ever engineers in 10 local newsrooms. Fellows report to newsroom editors, not funders, ensuring editorial independence. The program was funded partly by Microsoft and OpenAI but maintained platform neutrality: newsrooms are not required to use any specific vendor's products. Fellows formed a self-organized biweekly working group within the first month, creating a "person-and-a-half effect" where shared knowledge multiplied individual capacity -- fellows checked each other's code, swapped code, and accelerated each other's work.

**Tools:** Various (platform-agnostic), including Dewey (Philadelphia Inquirer's RAG-based archive search back to 1978), Slack AI integrations, custom advertising prospecting tools, AI transcription and translation, Google NotebookLM, ChatGPT.

**Outcome:** The Philadelphia Inquirer's Dewey archive tool went from a two-week hackathon with Microsoft's MADA team to broad deployment in about four months (versus an expected 24 months), saving reporters up to two days on deep archive research -- a nearly 40% time improvement. Dewey then expanded from editorial to ad sales (researching client coverage history) and marketing (identifying reporter coverage trends). The Seattle Times built an ad prospecting tool in a two-to-three week sprint that sold additional advertising "fairly quickly out of the box," demonstrating self-funding ROI. Chicago Public Media's Slack weather integration produced recording-ready scripts in the voice of WBEZ on-air talent, building trust with newsroom staff. The model addressed a structural problem: AI use in the news field is "dramatically undercapitalized," and these were the first AI engineers at each organization.

**Discussion Questions:**
1. The collaborative is funded by Microsoft and OpenAI but maintains editorial independence. Can philanthropic funding from AI companies create genuine independence?
2. Fellows report to editors, not funders. Why is this structural choice important for maintaining journalistic integrity?
3. The "person-and-a-half effect" suggests knowledge sharing multiplies individual capacity. How can this model be replicated without institutional backing?

---

## 12. Chicago Public Media: When AI Fails in Public

**Organization:** Chicago Public Media (WBEZ + Chicago Sun-Times), USA
**Episode:** Melissa Bell, Aron Pilhofer, Mark Chonofsky & David Chivers, January 2026

**What they did:** In May 2025, the Chicago Sun-Times published a "best books" list in which 7 of 10 titles were AI hallucinations -- imaginary books attributed to real authors. A Hearst freelancer had used AI against policy. The list went viral on Bluesky and was featured on Stephen Colbert's show. CEO Melissa Bell responded with immediate transparency, a public apology, and swift creation of AI guidelines. The incident became the corpus's most-cited example of what happens when guardrails fail. Beyond the crisis response, Chicago Public Media built substantive AI capabilities: transcribing an extensive WBEZ audio archive (so large "they don't actually know how much they have") to make decades of radio journalism searchable; AI translation reducing Spanish-language content turnaround from "yesterday's news tomorrow" to near-real-time; a natural-language-to-SQL interface enabling a journalist to query a complex Chicago schools dataset conversationally; and Slack integrations delivering weather and traffic reports in WBEZ's editorial voice.

**Tools:** Generative AI (used by freelancer without authorization), AI transcription, AI translation (English-to-Spanish), natural-language-to-SQL query tools, Slack AI integrations, Figma Make (rapid prototyping), machine learning content recommendation (third-party vendor, after determining LLM inference was not the right approach).

**Outcome:** Bell's response -- admitting the error publicly, creating policy from it, discussing it openly on a podcast -- generated more trust than pretending to have everything under control. The organization adopted a firm stance: "We are not in the business of generating content at any point, up to and including links." The AI fellow (Mark Chonofsky) noted that newsroom resistance to AI often stems from "people who've come to them with an AI solution to a problem they don't have" -- the key was starting with small, impactful wins like the Slack weather integration that demonstrated AI respecting editorial voice. Pilhofer's approach: "We don't have an AI product roadmap. We have a product roadmap of which AI is a part." Bell argued: "One of the opportunities that AI presents to us is better surfacing our humanity and better surfacing our authenticity."

**Discussion Questions:**
1. Bell turned an AI failure into a trust-building moment through radical transparency. Is this replicable, or does it only work once?
2. The freelancer used AI against policy. How should organizations manage AI use by external contributors who may not follow internal guidelines?
3. Chicago Public Media's response was "guardrails against content generation." Is this the right long-term stance, or does it foreclose legitimate uses of AI-generated content?
