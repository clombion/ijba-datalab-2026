# Building the Machine: Technical Architecture and Engineering Decisions

## Overview

This theme captures the engineering substrate beneath every AI initiative in journalism -- the model selection decisions, retrieval-augmented generation (RAG) pipelines, multi-agent architectures, hallucination mitigation strategies, open-source commitments, and data infrastructure investments that determine whether a newsroom's AI ambitions remain prototypes or become production systems. It matters because the gap between "we used ChatGPT" and "we built a reliable editorial system" is an engineering gap, and the choices newsrooms make here shape what is editorially possible, what remains trustworthy, and what can scale.

## Prevalence

T04 appears as a primary or secondary theme in approximately 35 of 42 episodes. It surfaces as a primary theme in deeply technical episodes featuring practitioners who build systems: Alviani at Ippen Digital (Feb 2024), Reissmann at Der Spiegel (Jun 2024), Schori at Aftonbladet (Sep 2024), Parrikh at Times of India (Oct 2024), Giske and Ytreberg at iTromsoe (Feb-Mar 2025), Lindskow at JP/Politikens (Mar 2025), Phillips at Stanford/Big Local News (May 2025), Seward at NYT (May 2025), Daudens on open-source AI (Jul 2025), Krustok at Delfi (Sep 2025), Beykpour at Particle (Aug 2025), Franz at Ippen (Nov 2025), and Alviani/Heckenberger at SZ (Jan 2026). Guests with engineering backgrounds or AI leadership roles engage most deeply; policy-oriented guests (Eshoo, Helberger) treat it tangentially.

## Key Findings

**1. RAG is the consensus architectural pattern for journalism.** From Ippen's reader chatbot to Aftonbladet's election bot to iTromsoe's document search to Particle's multi-source summarization, retrieval-augmented generation -- grounding LLM outputs in curated, authoritative content -- appears in virtually every production system. Aftonbladet's election chatbot used nearly 100 sources and achieved zero detected hallucinations. Seward at NYT described the core value as "creating structure out of unstructured data sets" rather than generating prose.

**2. The multi-model, multi-method approach has become standard.** Alviani evaluated 200+ candidate models before selecting one. Lindskow at JP/Politikens mixes fine-tuned Danish transformers with commercial LLMs. Giske insists on "combining complementary methods -- gen AI or machine learning or traditional if-and-then coding." Particle uses multi-LLM pipelines with an LLM-as-judge verification step. The single-model era is over; newsrooms assemble architectures from multiple components.

**3. Hallucination remains the defining technical constraint.** The jagged frontier concept -- AI performs brilliantly on some tasks and fails unpredictably on others -- recurs across 20+ episodes. Siegele at The Economist found style-guide checking at only 80% accuracy was unacceptable. Schori at Aftonbladet reported headline generation consistently failing human editors' standards. Alviani built self-evaluation systems with automatic reprompting. The phrase "hallucination as inherent feature" captures a hardening consensus: this is not a bug to be fixed but a characteristic to be engineered around.

**4. Data infrastructure is the prerequisite, not AI itself.** Krustok at Delfi invested eight years in data foundations before AI tools became possible. Parrikh at Times of India built "banking-grade" data pipelines. Marconi declared newsrooms must become "data gathering companies." Multiple guests warned that without structured, clean, well-maintained data, AI tools produce unreliable outputs. The CMS, metadata layer, and archive quality determine what AI can accomplish.

**5. Open source is a strategic commitment, not just a cost decision.** Daudens devoted an entire episode to Hugging Face and the democratization mission. Alviani required open-source models with commercial licenses and native German training data. Giske built Kotemon as an open-source RAG front-end when commercial tools failed at citation accuracy. The Dutch LLM initiative and Estonian multi-model approach reflect a sovereignty argument: open source enables transparency, linguistic independence, and vendor escape.

**6. Agents are the next architectural paradigm, but not yet production-ready.** Franz at Ippen declared "your next reader is an agent." Marconi described MCP (Model Context Protocol) as "the USB-C for AI context." Giske and Phillips both use agent-based architectures for web scraping and document extraction. But Marconi warned many "agents" are just GPT wrappers, and Giske acknowledged agents are not production-ready for newsrooms. The gap between agent hype and agent reality is wide.

**7. Fine-tuning delivers brand voice but not editorial judgment.** Ippen fine-tuned models on millions of regional articles to capture local style. SZ's fine-tuned LLM aligned with BBC-style prose but failed at political impartiality -- the "undertext" in local political reporting proved impossible to encode. Siegele found teaching an American model British English "very, very difficult." Fine-tuning works for surface features but breaks on the editorial nuances that define quality journalism.

## Evolution Over Time

Early 2024 episodes treated technical architecture as a novelty. The FT Strategies sprint (Jan 2024) discussed LLMs versus traditional ML at a conceptual level. By mid-2024, practitioner episodes (Ippen, Spiegel, Aftonbladet) showed increasingly sophisticated production architectures: vector databases, multi-step verification, CMS integration. Through 2025, the conversation shifted toward systemic infrastructure: data platforms (iTromsoe, Delfi), multi-agent workflows (Marconi, Franz), and the MCP interoperability standard. By January 2026, the discourse had matured from "which model should we use?" to "how do we build continuous monitoring systems for AI products that are never done?" (Alviani at SZ). The technical ambition grew from single-tool experiments to integrated editorial platforms.

## Consensus vs. Debate

**Consensus exists on:** RAG as the reliable architectural pattern; human verification as non-negotiable for published output; the multi-model approach; data infrastructure as prerequisite; and hallucination as an engineering constraint rather than a solvable problem.

**Debate persists on:** Whether to build in-house or buy from vendors (Lindskow advocates building core editorial functions, buying generic ones; Chicago Public Media pivoted from building to buying a recommendation engine). Whether CMS integration should be prioritized (Seward at NYT deliberately avoided it; Schori at Aftonbladet found it essential for adoption). Whether agents represent imminent transformation or premature hype. Whether fine-tuning justifies the investment when models improve quarterly.

## Concrete Examples

**Ippen Digital's 200-model funnel:** Alviani evaluated 200+ models, filtering for open-source availability, commercial license, native German training, and task performance. The result was a LoRA-based fine-tuned model for regional editorial style, deployed across 60 news portals.

**Aftonbladet's election chatbot:** Schori built a RAG system with nearly 100 authoritative sources, achieving zero detected hallucinations across 150,000+ user questions, with a tenfold login conversion rate.

**iTromsoe's hybrid architecture:** Giske combined generative AI, classical ML anomaly detection, and traditional if-then coding into a unified platform that compressed daily document review from 60-90 minutes to 5 minutes and detected anomalies across 5 million fisheries transactions.

**Particle's multi-LLM pipeline:** Beykpour described a three-article, two-publisher minimum source threshold, an LLM-as-judge reality check step, and multi-tier filtering architecture to reduce hallucination in automated news summarization.

## Actionable Insights

1. **Invest in data infrastructure before AI tools.** The most successful deployments (Delfi, Times of India, iTromsoe) built years of data foundation first. Clean, structured, well-maintained archives and metadata are the non-negotiable prerequisite.

2. **Design for the jagged frontier.** Map which tasks AI handles reliably (summarization, transcription, translation, entity extraction) and which it does not (headline writing at editorial standards, political nuance, creative voice). Build systems that route tasks accordingly.

3. **Adopt RAG as the default pattern for any system touching published content.** Grounding LLM outputs in authoritative source material dramatically reduces hallucination and provides an audit trail.

4. **Pursue open-source models for editorial-core functions.** This provides transparency, vendor independence, linguistic sovereignty for non-English markets, and the ability to fine-tune on proprietary corpora.

5. **Build continuous monitoring, not one-time deployment.** Alviani's insight that "there is no done column" applies universally. Concept drift, model updates, and evolving editorial standards require ongoing evaluation systems.

## Best Quotes

> "I think it's all about combining complementary methods. Be they gen AI or machine learning or traditional just if-and-then coding. Once you start seeing how they can complement each other and building systems that integrate all of these approaches, that's when you get something really useful."
> -- Lars Adrian Giske, iTromsoe (Feb 2025)

> "I do not trust the LLM and the probability model... I'm gonna put some authoritative sources in there and ask about what did the experts actually say. And I think it gives you a much more interesting, nuanced answer compared to the LLM looks into itself and spills out some hallucinations."
> -- Ole Reissmann, Der Spiegel (Jun 2024)

> "A lot of the most interesting applications have nothing to do with writing articles or writing out creating prose at all, so much as creating structure out of unstructured data sets to help unlock stories that are hidden in massive data sets you probably previously couldn't have considered as possible to report on."
> -- Zach Seward, NYT (May 2025)

> "There is no done column when we build AI products, you know? There's no finish. We basically -- it's continuous learning, it's continuous monitoring."
> -- Alessandro Alviani, Suddeutsche Zeitung (Jan 2026)

> "One of the key missions of Hugging Face is basically fighting the concentration of power. We want people to be able to choose how and what they want to use in AI."
> -- Florent Daudens, Radio Canada/Hugging Face (Jul 2025)
