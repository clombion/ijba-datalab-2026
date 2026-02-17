# The Prototype Pipeline: From Experiment to Shipped Product

## Overview

Theme T11 addresses the practical journey of moving AI projects from idea to prototype to production in newsrooms -- prototyping speed, the persistent production gap, deployment strategies, scaling challenges, user testing, and the infrastructure needed to ship. Unlike themes concerned with what AI can do (T01) or how organizations should be structured (T06), T11 focuses on the mechanical, operational question of how AI tools actually get built, validated, and deployed at scale. The theme encompasses two sub-themes: rapid prototyping and MVP discipline (T11.1), and the production gap and scaling realities (T11.2). Across the corpus, this theme reveals a fundamental tension: generative AI has compressed prototyping timelines from months to hours, yet the gap between a working demo and a production system remains stubbornly wide.

## Prevalence

T11 appears as a primary theme in approximately 5 episodes: Martin Schori's Aftonbladet AI hub, Rune Ytreberg and Lars Adrian Giske's iTromsoe investigative tools, Upasna Gautam's product management framework, Ivar Krustok's Estonia Delfi infrastructure, and one Ippen Digital episode on fine-tuning. It surfaces as a secondary theme in roughly 15 additional episodes and is tangential or absent in the remaining 22. The theme's prevalence increases across the corpus's timeline, reflecting an industry shift from theoretical discussion toward operational deployment. Earlier episodes (2024) tend to address prototyping as a possibility; later episodes (2025-2026) grapple with production realities.

## Key Findings

**1. GenAI has radically compressed prototyping timelines.** Ivar Krustok described building a Google Trends prototype with live data in three hours using Manus AI, Stitch, and V0.dev. Nikita Roy noted that "right now the biggest power is with coding... if you're trying to build out prototypes, quick prototyping, that's where I feel like the power of AI agents is right now." Custom GPTs reduced what previously required "thousands of hours of ML training" to minutes of configuration (Jaemark Tordecilla). This speed compression is consistently cited as transformational.

**2. The prototype-to-production gap remains the industry's central operational challenge.** Ludwig Siegele named it explicitly: "Moving from AI prototype to production is much harder than building the prototype due to IT bureaucracy, scaling, robustness requirements, and competing priorities." Across the corpus, the gap manifests as CMS integration barriers (Schori: tools outside the CMS see low usage), engineering bottlenecks (Lenfest fellows building first-ever AI engineering capacity), and organizational friction (Zacharison: the media industry pattern of launching MVPs then jumping to the next project without iterating).

**3. The MVP abandonment pattern plagues the industry.** Zacharison criticized the "media industry pattern of launching MVPs then jumping to the next project without iterating." Particle's Sara Beykpour referenced Artifact and SmartNews as cautionary precedents of abandoned AI news products. Neil Brown warned against the 3-6 month evaluation window that discards tools before they can demonstrate value. The industry's project-based rather than product-based culture is the root cause.

**4. User testing discipline separates successful deployments from failed ones.** Gard Steiro offered the sharpest insight: "When testing new AI-powered products for new audiences, recruit users you don't currently have rather than testing on loyal super users, who will always prefer the status quo." Alviani at Ippen Digital practiced deep product discovery -- embedding with editors, understanding workflows before building. Gautam advocated "involving editorial teams early in the process" as "the ultimate product management hack in news."

**5. Workflow integration is the primary adoption gate.** Siegele observed that "the barrier to entry or the investment you have to make as an individual to kind of integrate [AI tools] into your personal workflow is largely underestimated." Schori found that tools not integrated into the CMS saw minimal adoption despite being technically functional. The NYT's Zach Seward deliberately deprioritized CMS integration in favor of general-purpose tools that desks could self-serve -- a contrarian strategy reflecting the NYT's unique scale.

**6. Scaling from prototype to multi-site deployment introduces distinct challenges.** Ippen Digital's deployment across 60 portals and 250 editors required standardization as a scaling principle. iTromsoe's GIN system scaled to 36 newspapers covering 130 municipalities, but 40% of municipalities lacked open data. Cheryl Phillips's Agenda Watch aimed to scale from hundreds to 3,000 government agencies in six months. Each case reveals that scaling is not merely technical but depends on data availability, organizational readiness, and funding.

**7. Small wins build the organizational trust needed for larger deployments.** Ytreberg started with "low hanging fruits... very easy to get our hands on" to demonstrate value to editors before scaling. Chonofsky at Chicago Public Media built trust through a simple Slack weather/traffic integration before pursuing larger projects. The Dewey archive tool at Lenfest expanded from editorial to ad sales after demonstrating value in one domain. This pattern -- prove value small, then scale -- recurs across nearly every successful deployment story.

## Evolution Over Time

The corpus tracks a clear maturation arc. In early 2024, prototyping discussions are aspirational: the FT Strategies sprint emphasizes validating user needs and running small proofs of concept. By mid-2024, concrete production deployments emerge: Ippen Digital's fine-tuned models across 60 portals, Aftonbladet's election chatbot reaching 150,000 questions. Through 2025, the conversation shifts from "can we build this?" to "how do we sustain and scale this?" -- Kasper Lindskow frames the transition from building for AI front-runners to building for the average journalist as a change management challenge. By late 2025 and early 2026, the focus sharpens further: Alviani declares "there is no done column when we build AI products" and Marconi describes the industry's progression from shock (2023) to experimentation (2024) to "operational reckoning" (2025). The production gap has not disappeared; it has been reframed from a technical problem to a change management and organizational culture problem.

## Consensus vs. Debate

Strong consensus exists around two points: prototyping speed has been transformatively accelerated by GenAI, and the production gap is real and persistent. The primary debate concerns strategy for closing the gap. One camp (Seward at NYT, Siegele at The Economist) advocates building general-purpose infrastructure that empowers individual teams to self-serve rather than building bespoke tools for each use case. The opposing camp (Alviani at Ippen/SZ, Schori at Aftonbladet) argues for deep CMS integration and purpose-built tools that require minimal journalist effort. A secondary debate concerns pacing: Franz advocates "think big, start small, move fast, learn fast" with a 95% failure rate as normal, while Brown warns against evaluating experiments over too-short timeframes. Both positions have merit; the right approach likely depends on organizational scale and culture.

## Concrete Examples

- **Good Tape (Zetland)**: From internal Whisper prototype to $3M revenue product to successful divestiture -- the most complete prototype-to-production-to-exit story in the corpus.
- **GIN (iTromsoe)**: Compressed daily document review from 60-90 minutes to 5 minutes, scaled to 36 newspapers covering 130 municipalities, with two summer interns producing five cover stories in their first week.
- **Dewey (Lenfest/Philadelphia Inquirer)**: From a two-week hackathon to broad newsroom deployment in four months (versus an expected 24 months), then expanded from editorial to ad sales and marketing.
- **Aftonbladet election chatbot**: RAG architecture with nearly 100 sources, zero detected hallucinations, 150,000+ user questions, tenfold login conversion -- a prototype that reached production scale under election-deadline pressure.
- **Ivar Krustok's 3-hour prototype**: Used Manus AI, Stitch, and V0.dev to build a working prototype with live API data and send a test link to stakeholders the same day, replacing the traditional slide-deck approach.

## Actionable Insights

- **Adopt "prove small, then scale" as a deployment principle.** Start with low-friction, high-visibility tools (transcription, document search) that build organizational trust before attempting complex deployments. Every successful case study in the corpus follows this pattern.
- **Invest in CMS integration as infrastructure, not afterthought.** Schori's finding that tools outside the CMS see minimal adoption is consistently validated. Workflow integration is the single strongest predictor of sustained usage.
- **Treat the production gap as a change management problem, not a technical one.** Lindskow's observation that "even if the technology develops exponentially, rolling it out and adapting it is change management -- a very linear process" reframes where investment should be directed.
- **Build working prototypes instead of presentations.** Krustok's approach of sending test links with live data to stakeholders replaces slide decks with tangible artifacts. Franz's "demos not memos" principle accelerates stakeholder alignment.
- **Plan for continuous iteration, not project completion.** Alviani's "no done column" insight means AI products require ongoing monitoring, concept drift management, and model updates -- budget and staff accordingly.

## Best Quotes

**Ludwig Siegele (The Economist, September 2025):** "Moving from AI prototype to production is much harder than building the prototype due to IT bureaucracy, scaling, robustness requirements, and competing priorities."

**Ivar Krustok (Delfi Estonia, September 2025):** "I can already send them a test link. Like, okay, we talked about it a while ago that something like this would help. Like is this something you're envisioning and it would already have some sort of mock data already, live data from the API."

**Rune Ytreberg (iTromsoe, February 2025):** "We started with low hanging fruits. That was very easy to get our hands on and that we could very efficiently get the product out and show our editor that this is actually working and it's going to have an impact."

**Olle Zacharison (BBC, November 2025):** "We've been in fifteen, twenty years of digital transformation, we've been obsessed with building things... Whereas now some of the stuff that we can do with Gen AI is like basically you can go in and in three hours customize the GPT that can perform a task that you had to build a tool for and using in six months."

**Markus Franz (Ippen Digital, November 2025):** "My mantra is think big, start small, move fast, learn fast. Building the tiniest possible product out of your vision and get as soon as possible feedback from the editors, from the customers. It's just normal product development."
