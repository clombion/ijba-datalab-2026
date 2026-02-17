# Glossary: AI in Journalism

Key terms and concepts as defined and used by practitioners in the Newsroom Robots podcast (2024-2026). These are working definitions from the field, not textbook entries.

---

### Agentic AI / AI Agents
Software systems that can independently perform multi-step tasks -- browsing the web, gathering data, making decisions -- rather than just responding to single prompts. Giske at iTromsoe uses agents to scrape government databases overnight. Marconi warns many "agents" are just GPT wrappers. Franz predicts "your next reader is an agent." Still largely not production-ready for newsrooms as of January 2026.

### AI Buffet
Aftonbladet's term for its collection of 25-30 simple prompt-wrapper tools available to all journalists. Each tool does one specific thing (translate, generate TikTok scripts, proofread, suggest follow-up stories). The concept: lower the threshold for adoption by offering many small, easy-to-use tools rather than one complex platform.

### AI Design Language
A consistent visual system for marking AI-generated or AI-assisted content. SZ developed branded colors, frames, and labels applied uniformly across all AI products. The purpose is to make AI involvement immediately visible to audiences without requiring them to read fine print.

### AI Hub
A dedicated editorial team focused on AI experimentation and deployment, typically led by editorial staff rather than engineers. Aftonbladet created one because central product teams deprioritized newsroom AI ideas. Distinguished from an innovation lab by its editorial leadership and proximity to daily news production.

### Augmentation (vs. Replacement)
The dominant framing across the corpus for AI's role: AI should enhance journalists' capabilities rather than replace their jobs. Practitioners describe AI as "co-pilot," "force multiplier," and "grunt-work augmentation." The framing is contested -- Alviani provides firsthand testimony of real job losses at Microsoft News.

### Build vs. Buy
The strategic decision of whether to develop AI tools in-house or purchase from vendors. Lindskow's framework: build core editorial functions (where competitive advantage lies), buy generic ones (where vendors already solve the problem). Chicago Public Media pivoted from building to buying a recommendation engine. Small newsrooms generally cannot build.

### Change Management
The organizational process of integrating new AI tools and workflows. Lindskow's key insight: "Even if the technology develops exponentially, rolling it out and adapting it is change management -- a very linear process." Budget 12-18 months for meaningful organizational adoption.

### CMS Integration
Embedding AI tools directly within the Content Management System journalists already use. Schori found that tools outside the CMS see minimal adoption regardless of quality. Seward at the NYT deliberately avoided it, prioritizing long-term architecture. One of the strongest predictors of sustained tool usage.

### Concept Drift
When an AI model's performance degrades over time because the real-world data it encounters has shifted away from its training data. Parrikh at Times of India flagged this as a persistent maintenance challenge: business features change, data definitions shift, and models need continuous updating.

### Content Multiplication
Using AI to transform a single piece of journalism into multiple formats: text article, bullet-point summary, audio version, video recap, easy-language adaptation, push notification. Enables newsrooms to reach different audiences from the same underlying reporting. Central to the "experience over content" thesis.

### Custom GPT
A tailored version of ChatGPT configured with specific instructions, data, and constraints for a particular task. Tordecilla built a Philippine government audit processor; Aftonbladet built 25-30 for various newsroom functions. Distinguished from general ChatGPT use by their domain specificity and reusability.

### Data Infrastructure
The foundational layer of structured data, pipelines, metadata, and storage that must exist before AI tools can be effective. Krustok at Delfi invested eight years in data foundations. Parrikh calls it the equivalent of energy for a country. Multiple practitioners insist: without clean, structured data, AI produces unreliable results.

### Data Minimization
Deliberately using the fewest data points possible to achieve a goal. Parrikh at Times of India describes using "the least amount of information that can give us the highest return" for personalization. Contrasts with Big Tech's data-maximalist approach. Both a privacy principle and an engineering philosophy.

### Deep Research
An emerging AI capability where models conduct extended, multi-step research on a topic. Phillips references it for source curation. Krustok used a Chinese deep research model for extended analysis. Distinguished from simple prompting by its multi-step, iterative nature.

### Disintermediation
The process by which AI platforms (ChatGPT, Google AI Overviews, Perplexity) insert themselves between publishers and audiences, extracting information without driving traffic back to the source. The Lenfest episode quantifies a 20-30% decline in Google-referred traffic. The central economic threat.

### Echo
The New York Times' internal AI platform for summarizing and transforming content. Supports multiple LLMs, preset and custom prompts, URL-based content fetching. Used by over half of the 2,000-person newsroom. Built as a general-purpose tool that desks adapt to their own needs.

### Essential AI Toolkit
A curated collection of AI tools, models, and resources for journalists maintained by Daudens. Designed as a structured starting point for newsroom practitioners who are overwhelmed by the pace of AI development. Includes open-source models, prompt templates, and workflow guides. Represents the shift from one-off training sessions to ongoing, self-serve AI literacy resources.

### Expert-in-the-Loop
SZ's refinement of the human-in-the-loop concept: requiring that the article's author -- not a generic reviewer -- verify AI-generated summaries. The distinction matters because domain expertise catches errors that general review misses.

### Fine-Tuning
Customizing a pre-trained AI model on a specific dataset to align with a newsroom's editorial voice, style, or language. Ippen fine-tuned on millions of regional articles. BBC's Style Assist was trained on paired datasets of submitted and edited articles. Works for surface features (tone, format) but fails on editorial nuance (political impartiality).

### Floor-Scale-Ceiling Framework
A strategic framework for categorizing AI opportunities: floor (minimum viable use), scale (broad deployment), and ceiling (aspirational/transformational). Used for prioritizing which AI projects to pursue first.

### GIN (Governmental Information Network)
iTromsoe's AI system that ingests municipal planning documents, ranks them by newsworthiness using a model trained on senior journalists' editorial judgment, and delivers a prioritized daily briefing. Covers 130 municipalities across 36 newspapers.

### Guidelines-to-Practice Gap
The persistent disconnect between stated AI ethics policies and actual behavior. Helberger found nearly 20% of newsrooms adopt non-use as their ethics strategy. Zetland discovered unauthorized voice cloning. The gap is the field's defining failure according to the corpus.

### Hallucination
When an AI system generates plausible-sounding but factually incorrect output. The Chicago book list incident (7 of 10 hallucinated books) is the corpus's most-cited example. Multiple practitioners describe it as "an inherent feature, not a bug to be fixed." Mitigation strategies include RAG grounding, multi-LLM verification, and human review.

### HeyGen
An AI video dubbing platform that translates video content into other languages with lip-sync adaptation. Siegele at The Economist describes the results as "startlingly convincing" -- speakers appear to speak the target language natively. Used by The Economist to expand the reach of video content across language barriers. Represents the frontier of AI translation moving beyond text into multimedia.

### Human-in-the-Loop / Human-on-the-Loop
Two models of human oversight. Human-in-the-loop: a person reviews every AI output before it reaches audiences. Human-on-the-loop: humans monitor and audit AI systems without reviewing every individual output. Franz describes a spectrum from coordinator (active) to consultant (reactive) to observer (passive). The evolution from in-the-loop to on-the-loop is the corpus's sharpest ethical fault line.

### Jagged Frontier
The uneven capability landscape of AI: brilliant on some tasks, failing unpredictably on others. Coined in the research literature and widely adopted in the podcast. Siegele found style-guide checking at 80% accuracy -- impressive for some uses, unacceptable for publication. Newsrooms must map which tasks fall on which side.

### JournaPilot
An AI tool built specifically for journalism workflows, cited by Dhar at the McGovern Foundation as an example of innovation emerging from within journalism rather than from Big Tech. Represents the thesis that the journalism market is too small for commercial AI companies to build bespoke solutions, so the field must develop its own tools. Part of a growing ecosystem alongside MuckRock and other journalism-native AI projects.

### Langdog
SZ's internal AI literacy platform that provides journalists with access to AI tools and training. Achieved nearly 50% newsroom adoption. Named playfully; serves as both a tool access point and a learning environment.

### Licensing Paradox
The contradictory incentive structure facing publishers: licensing content to AI companies provides short-term revenue but may accelerate the disintermediation that threatens long-term survival. Eeman described it as "digging your own grave."

### Local Inference
Running AI models on local hardware rather than sending data to cloud servers. Critical for source protection in investigative journalism. Tools: Whisper/WhisperX for transcription, Ollama for LLM inference. Daudens: "Run open-source AI models locally for sensitive or confidential journalism work."

### LoRA (Low-Rank Adaptation)
A cost-efficient method for fine-tuning large language models that updates only a small number of parameters. Ippen Digital used LoRA-based fine-tuning to adapt models for regional editorial style. Mentioned as making fine-tuning accessible to newsrooms without massive compute budgets.

### MCP (Model Context Protocol)
An emerging standard (from Anthropic/OpenAI) for connecting AI models to external data and tools. Marconi described it as "the USB-C for AI context." Chivers at Lenfest called it "transformational for modular AI integration work." Still early-stage as of January 2026.

### Multi-Agent Error Checking
Using multiple AI models to verify each other's outputs rather than relying solely on human review. Particle's LLM-as-judge step, where one model evaluates another's summary, is the most concrete example. Proposed by Steiro as a structural alternative to human-in-the-loop at scale.

### No-Code / Vibe Coding
Building functional applications without traditional programming, using AI tools to generate code from natural-language descriptions. Tordecilla built a government audit tool in minutes. Franz describes journalists building "full-stack products." Shifts journalists from consumers to creators of AI tools.

### Person-and-a-Half Effect
Lenfest Collaborative's observation that shared knowledge among embedded AI fellows multiplied individual capacity. When fellows shared solutions through a biweekly working group, each became approximately 1.5 times as effective. Demonstrates the value of collaborative learning networks.

### Prompt Queen
Aftonbladet's organization-wide prompting masterclass, taken by every employee. Named to be memorable and approachable. Represents the peer-learning, hands-on approach to AI literacy that the corpus consistently identifies as more effective than formal training.

### Prototype-to-Production Gap
The persistent difficulty of moving from a working AI demo to a robust, scalable production system. Siegele: "Moving from AI prototype to production is much harder than building the prototype." Caused by CMS integration barriers, engineering bottlenecks, and organizational friction. The industry's central operational challenge.

### RAG (Retrieval-Augmented Generation)
An architectural pattern that grounds AI outputs in curated, authoritative source material rather than relying on the model's training data alone. The consensus approach for any system touching published content. Aftonbladet's election chatbot (zero hallucinations from ~100 sources) is the benchmark example.

### Responsible Procurement
Evaluating AI vendors' data practices, liability terms, and training data provenance before adopting their tools. Helberger found it to be the least popular but potentially most consequential ethical practice. Key questions: What data trained this? Who is liable for errors? What happens to our data?

### Scraping War
The ongoing technical and legal battle between publishers trying to prevent AI companies from using their content for training, and AI companies whose core competence is information retrieval. Siegele: content appears in ChatGPT despite active blocking. Franz: Google's Gemini solves Google's own CAPTCHAs. The consensus: the technical war is already lost.

### Signals
Times of India's in-house recommendation system. Achieved 85% CTR increase. Recirculates 50% of page views from archival content. Self-learning: adjusts automatically when story supply fluctuates. Operates with minimal data points per story and per user.

### Style Assist
BBC's bespoke fine-tuned LLM that rewrites articles from local democracy reporters to align with BBC editorial standards. Trained on paired datasets of submitted and published articles. Performs well on formatting and tone but struggles with political impartiality -- the "undertext" in local political reporting.

### Think Big, Start Small, Move Fast, Learn Fast
Markus Franz's mantra for AI product development at Ippen Digital. Emphasizes prototyping the smallest possible version of a big vision and getting feedback quickly. Paired with a 95% expected failure rate and a "ship fast, murder darlings" discipline.

### Tolbit
A content marketplace designed to compensate publishers when AI systems use their content for inference (not just training). Cited by both Beykpour (Particle) and Siegele (The Economist) as an emerging model for fair publisher compensation. Alongside Cloudflare and ProRata, represents one of the first attempts to create a transactional layer between AI platforms and news publishers, addressing the disintermediation threat.

### Two-Tier Adoption Divide
The split between AI-engaged and AI-disengaged staff within newsrooms. Daudens estimates 80/20. Marconi found 38% of early-career journalists had never used ChatGPT. The divide reflects time pressure, cultural resistance, fear, and inadequate organizational support rather than technology access.

### Vector Database
A specialized database that stores content as mathematical representations (embeddings), enabling semantic search -- finding content by meaning rather than keywords. Foundation for RAG systems. Der Spiegel identified it as their most important infrastructure project. Delfi indexed 25 years of multilingual content.

### Why Before How
The consensus strategic principle: ask what editorial problem needs solving before evaluating which AI tool to use. Peretti: "I wish there was more time spent on a step before thinking, what are we trying to do?" Reissmann: "Maybe the most obvious use cases of generative AI are not the ones we should go after." Functions as the practical ethical checkpoint that survives across organizational contexts.
