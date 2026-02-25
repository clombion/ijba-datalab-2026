<!-- chunk: 1/1 | source: 77-ai-automation-investigative-journalism.md | words: 7158 -->
<!-- headings: **“This could save us months of work” - Use Cases of AI and** **Automation Support in Investigative Journalism** -->

## **“This could save us months of work” - Use Cases of AI and** **Automation Support in Investigative Journalism**


[Besjon Cifliku](https://orcid.org/0009-0007-5081-9531)
besjon.cifliku@cais-research.de
Center For Advanced Internet Studies
Bochum, Germany


**ABSTRACT**


As the capabilities of Large Language Models (LLMs) expand, more
researchers are studying their adoption in newsrooms. However,
much of the research focus remains broad and does not address
the specific technical needs of investigative journalists. Therefore,
this paper presents several applied use cases where automation
and AI intersect with investigative journalism. We conducted a
within-subjects user study with eight investigative journalists. In
interviews, we elicited practical use cases using a speculative design
approach by having journalists react to a prototype of a system
that combines LLMs and Programming-by-Demonstration (PbD)
to simplify data collection on numerous websites. Based on user
reports, we classified the journalistic processes into data collecting and reporting. Participants indicated they utilize automation
to handle repetitive tasks like content monitoring, web scraping,
summarization, and preliminary data exploration. Following these
insights, we provide guidelines on how investigative journalism
can benefit from AI and automation.


**CCS CONCEPTS**


- **Human-centered computing** → **Empirical studies in collab-**
**orative and social computing** ; **Empirical studies in HCI** .


**KEYWORDS**


Computational Journalism,Automated Journalism,Automation,AI,Large
Language Models (LLMs),Programming-by-Demonstration


**1** **INTRODUCTION**


Investigative journalism uncovers truths and shapes public opinion [26, 45, 51] by collecting, analyzing, and fact-checking vast
amounts of data. Nevertheless, the exponential growth in available
data poses significant challenges in promoting transparency and
justice in the digital age. Broader technical expertise and significant
efforts are required to process and acquire online information. Automation assists investigative reporting by analyzing large datasets,
finding correlations, and recognizing hidden patterns in documents
that might be overlooked otherwise [14]. Accordingly, this allows
journalists to automate repetitive tasks, focus on framing better
insights, and create newsworthy stories.
Diakopoulos et al. [17] report the widespread use of generative
AI for content creation, editing, and translation, as well as for
researching, coding, and sensemaking. In addition, integrating AI
agents with web surfing opens new doors to access digital resources.
According to Cools [9], Cools and Diakopoulos [10], automation is


[Hendrik Heuer](https://orcid.org/0000-0003-1919-9016)
hendrik.heuer@cais-research.de
Center For Advanced Internet Studies
Bochum, Germany
Bergische Universität Wuppertal
Wuppertal, Germany


already incorporated in news collection, production, verification,
and news-sharing processes.
This study examines how investigative journalists integrate automation and AI into their daily workflows, focusing on automation tasks, practical use cases, and the limitations of the tools they
already employ. In this work, we do not constrain AI to generative models, but we consider AI as any system capable of doing
autonomous work. Our approach aims to identify end-user requirements and features to guide the design and development of an
automation framework for investigative journalism. To the best of
our knowledge, this paper is among the first to involve investigative
journalists deeply in a tool-based co-creation process through user
studies interviews.
We used an elicitation [8] prototype during the interviews to
introduce journalists to the PbD paradigm using LLMs. Our study
employs a speculative discursive design methodology [1, 19, 35]
combined with user elicitation [54], encouraging interviewees to
reflect on the potential benefits when applying a similar artifact in
their daily context. The elicitation prototype facilitates user interactions on the web utilizing LLMs by allowing users to intuitively
demonstrate how they want to collect web data. The system then
replicates these actions and suggests methods for retrieving similar
hierarchical data. The goal is to empower users, regardless of background, to automate web-based tasks easily. We used a video of
the prototype during interviews to illustrate web automation use
cases, to showcase the prototype’s features, and to elicit responses.
We explored how this novel interaction with generative AI could
be integrated into journalists’ workflows and evaluated their need
for such an automation system. We further asked participants to
suggest practical and relevant software features applicable to their
work.
We applied the Human-in-the-Loop (HITL) paradigm, similar to

[44], involving investigative journalists as end-users in the design
process to tailor the technical solutions to their needs. This approach guided our investigation of the following research question.


  - **RQ: In what use cases is automation or generative AI**
**used in investigative journalism workflow?**

To answer this research question, we conducted eight qualitative within-subject semi-structured interviews with investigative
journalists in Germany.
Briefly, our work contributes to (1) a qualitative analysis of investigative journalists perspectives on AI and automation, focusing on
a novel approach to automating repetitive tasks through a combination of PbD and generative LLMs and (2) a taxonomy of potential
automation use cases and solutions that researchers can use as


a foundation for developing new tools. Lastly, we briefly discuss
some insights on challenges when using automation in journalistic
settings.


**2** **BACKGROUND & RELATED WORK**


Computational journalism combines data science, algorithms, and
social science to support journalists in shaping stories when working with the continuously growing volume of data [6, 27]. Diakopoulos [14] identified various newsroom applications of computational
algorithms, such as social media monitoring, fact-checking, document analysis, and automated reporting. Previous studies have
agreed on four key processes in news automation: verification,
production, gathering, and distribution [9, 10]. In this study, investigative journalism’s [53, 56] scope mainly focuses on information
gathering and analyzing and not much on reporting.
Scholars like Stray [51] and Fridman et al. [22] explored the
hurdles of integrating AI in newsrooms. They identified data access
and availability as significant obstacles in investigative research due
to inconsistency, lack of open-source data, and transparency issues.
Stray [51] described automated data preparation as a prospective
future application. It is important to note that this study predates
the release of OpenAI’s ChatGPT [46].
Web automation has long been a valuable tool for data collection

[2]. As the web evolves and transforms, the automation ecosystem adapts in response. However, this introduces new layers of
complexities as the data retrieval process requires more technical
expertise [5]. Practitioners must understand how to navigate increasingly tangled web structures to retrieve data [5]. Automation
reduces technical knowledge needs, enabling users to collect data
without a deep understanding of web architectures [2, 5]. PbD enables users to automate tasks through demonstrations, eliminating
the need for manual coding [12]. In another direction, a large body
of researchers is studying how LLMs allow users to query data or
automate web interaction using natural language [25, 38, 52] with
a few open-source initiatives [13, 39, 50].
Emerging computational methods are increasingly supporting
journalistic processes. For example, Diakopoulos et al. [18] support
political reporters in identifying newsworthy voter locations during
elections using data mining algorithms. Broussard [4] developed an
AI system to analyze data and identify opportunities or newsworthy
investigative ideas related to public affairs, while Park et al. [47]
automated news articles’ comments moderation and provided analytics for better storytelling. Similarly, Petridis et al. [48] worked on
co-designing and prototyping a tool to explore different reporting
angles using LLMs. Jamil and Rubaiat [32] enabled journalists to
query data and extract insights from multiple online sources.
Kasica et al. [34] thoroughly interviewed 36 data journalists to
explore how they work and process dirty data (i.e., incomplete,
inaccurate, or inconsistent information [7]). Their study provides a
taxonomy of data processing from data collection to data dissemination in the context of data journalism [34]. We follow a similar
approach but prioritize revealing practical use cases rather than
comprehensively analyzing the data workflow chain.
Rather than simply exploring automation trends in investigative
journalism, we aim to create a framework to develop AI-powered
tools specifically for journalists. This paper explicitly explores the


Cifliku and Heuer


journalists’ perception of automation using PbD and LLMs. Fridman
et al. [22] argue that a practice-focused approach, as proposed by
Barroca et al. [3], enables a deeper understanding of how technology
shapes the investigative newsroom environment.
Fridman et al. [22] bridged the gap between researchers and
industry practitioners by collaborating with journalists, data scientists, and IT experts in a transdisciplinary workshop. Journalists
defined research topics, scoped projects, and planned the work.
Our study shares this collaborative approach with a stronger usercentered focus by deeply involving journalists in the problem formulation. Similarly, Missaoui et al. [44] highlighted the need for
more interactive collaboration with journalists and identified opportunities and challenges while co-creating human-centered AI
tools with journalists. They co-designed the "DMINR AI" [41] to
automate claim verification and exploratory analysis.


**3** **METHOD**


This paper aims to place journalists at the core of the research
process, actively involving them in identifying areas where we
can integrate automation into their tasks and engaging journalists
with an elicitation prototype. The following section presents an
overview of the participants, the prototype, and the procedure.


**3.1** **Participants**


We conducted within-subject user studies using semi-structured
interviews. To recruit participants, we applied purposive [49] and
snowball [21] sampling similar to [34]. For our sampling strategy,
we decided to recruit journalists with significant experience, particularly those with expertise in working with data. We contacted
journalists through one of Germany’s largest investigative journalism research networks, _[Netzwerk Recherche](https://netzwerkrecherche.org/ueber-uns/kurzportrait/)_ . We initially recruited
four participants from this channel. After each interview, we asked
participants to recommend colleagues interested in joining the
study. We contacted these referrals via email and continued reaching out until all recommendations were exhausted. Additionally,
we recruited one more through university newsletters. The final
sample comprised eight participants from major newspapers of
record and news agencies across Germany. We did not provide
monetary compensation for the participation.
The participants are listed in Table 2. The sample included five
male and three female participants: three OSINT specialists, three
data journalists, one state-funded cyber intelligence specialist, and
one editor-investigative reporter. Participants ranged in age from
34 to 40, with a mean of 37 _._ 5 (SD≈2 _._ 26). Educational backgrounds
included two doctorates, five master’s degrees, and one college
degree. All participants had over five years of experience and were
familiar with generative AI and automation. All participants, except
for P07, had programming background.


**3.2** **Elicitation Prototype: JournalXRecorder**


We designed an elicitation prototype around three main objectives.
First, it should feature a **record and replay** functionality [5], enabling journalists to capture and replay the web activity chronologically. Second, users must be able to automate and customize their
workflows using LLMs **without requiring technical expertise** .
Finally, users should be able to extract **structured data** from any


“This could save us months of work” - Use Cases of AI and Automation Support in Investigative Journalism


**Figure 1: JournalXRecorder, prototype user interface. A) Main page where user can see their workflow, track events, and ask**
**LLMs to automate. B) Running automation and generating scripts. C) Chat with and analyze the collected data.**


website. For instance, journalists could use the tool to monitor how
content on various sites evolves. They would only need to visit
a site once, select the elements they wish to track, and the tool
would then perform the checks repeatedly. Like Chasins [5], the
motivation is to **do it once and repeat it anytime, anywhere** .
The tool lets users collect data online by recording their browser
interactions, such as clicking, typing, and scrolling. To engage journalists with this automation framework, we employed speculative
design [1, 19] using a video of the prototype as our key method.


**3.3** **Procedure**


We instructed participants to prepare a use case that AI could automate. We began the interviews by obtaining participants’ informed
consent to use their data in compliance with GDPR and requesting
permission to record the sessions.
We divided the semi-structured interviews into two phases. In
the first part (approximately 20 minutes), we asked participants
about their familiarity with automation and AI. They responded to
questionnaires regarding the impact of automation on their work,
data management practices, and the challenges they face. Further,
we questioned participants about the limitations of their current automation tools and their desired improvements to their workflows.
Finally, we tasked participants to **imagine** an ideal tool tailored to
their needs, considering both computational and human resources
available for its creation. In a storytelling setting, we aimed to explore practical journalistic use cases and point out any potential
limitations.
In the second part, we presented the elicitation prototype. We
listed its main features, explained a few details for the use case as
illustrated in Appendix A.2, and presented an eight-minute demo in
the form of a video. Afterward, we requested participants to suggest
potential scenarios for its application during investigations.
Interviews lasted, on average, 62:39 minutes (SD≈9:10) and were
conducted virtually via Webex. To transcribe the audio, we used
an automatic caption generator provided by Webex. In addition,
the first author noted down key points during the interviews. We
applied qualitative content analysis to identify key themes through
inductive coding following [42, 43]. We reviewed the interviews
iteratively, grouping codes into a set of overarching themes similar
to [28]. The first author assigned the preliminary codes. Following


the interviews, we identified potential concepts related to news
processes. We then mapped these categories to the participants’
statements and engaged in an iterative process, repeatedly revisiting
the participant’s statements to draw new codes [11] related to news
automation. The codes were subsequently merged and refined into
themes and sub-themes. The first author did the coding, while the
second author reviewed the codes in weekly sessions to ensure the
themes’ relevance to the participants’ statements. The interview
questionnaires can be found in Appendix A.2


**4** **RESULTS**


The following presents a taxonomy of automation scenarios and
investigative journalism tasks based on systematically reviewed
use cases. Interviews revealed that automation facilitates news
**collection** and **reporting**, as listed in Table 1.


**4.1** **Collecting**


_4.1.1_ _Monitoring._ **Continuous Analytics and Alerting:** Participants emphasized using automation for continuous data collection
and generating comprehensible responses, often through web scraping ( _𝑃_ 01 _, 𝑃_ 02 _, 𝑃_ 03 _, 𝑃_ 06 _, 𝑃_ 07 _, 𝑃_ 08). For instance, _𝑃_ 02 analyzed hotel
prices during the European soccer championship and tracked climate change trends by comparing historical temperature records
across cities. Moreover, _𝑃_ 03 and _𝑃_ 08 reported on downloading and
summarizing data from Telegram groups. In addition, _𝑃_ 08 recounted
collecting metadata from GitHub to verify content and visualize
repository activities. Furthermore, _𝑃_ 06 suggested using the prototype for notifying the public about topic monitoring on local
democracy. _𝑃_ 08 proposed an automatic analysis of how influencers
on YouTube shift their language over time to study radicalization
patterns. Additionally, _𝑃_ 06 described how combining and reporting
data from local air sensors can alert the public about air pollution.
**Tracking:** Participants also reported on tracing leaked information and tracking suspicious user fingerprints across online
platforms, social media, public databases, and geospatial locations
( _𝑃_ 01 _, 𝑃_ 04 _, 𝑃_ 05 _, 𝑃_ 08). For instance, _𝑃_ 01 described tracking “personas
of interest” on foreign-language websites or leaked documents, noting the process complexity and the lack of a centralized data storage.
He suggested that an AI assistant capable of understanding initial
hints and automating research could _“save months of work”_ and


Cifliku and Heuer


**Table 1: This table depicts the investigative journalism processes grouped into two categories: collecting and reporting data.**


|Process|Theme|Description|
|---|---|---|
|**Collecting**|Monitoring|Auditing, gathering, and tracking content information from multiple sources.|
|**Collecting**|Filtering|Reducing redundancy and only targeting relevant information.|
|**Collecting**|Documenting|Recording of the investigation process and keeping track of each action.|
|**Collecting**|Storing|Preserving the collected data into usable format, converting it into searchable entities, and indexinginto databases.|
|**Collecting**|Augmenting|Assisting in scaling up scraping tasks, providing analytical support and investigation leads.|
|**Reporting**|Analysing|Simplifying and comprehending the results. Structuring and processing of data to draw insights.|
|**Reporting**|Labeling|Categorizing, clustering, and linking data into themes and subtopics.|
|**Reporting**|Writing|Inspiration or assistance starting or clarifying tasks. AI news production and dissemination.|


_“make more interesting stories possible.”_ Similarly, _𝑃_ 05 recognized
the potential of automation to process and extract key details from
large document sets, providing an example of comparing websites’
hidden Google tags to trace their origins. Likewise, _𝑃_ 08 discussed
comparing and tracking IP addresses to verify if sites are related.
In another case, _𝑃_ 04 pondered on having precise tools that provide
greater control when geolocating images. She clarified that _“If you_
_got a picture in Gaza and if you try to find one house, it takes hours”_ .
**Content Audit Trail:** Some participants noted that automation
could be used to compare and track historical changes in online
content to verify if it was maliciously altered ( _𝑃_ 05 _, 𝑃_ 08). _𝑃_ 05 described downloading complete website archives using Wayback
Machine [31] and matching their content against search phrases.
Similarly, _𝑃_ 08 highlighted the potential of using the prototype to
monitor social media content for periodic changes. Furthermore,
he expressed the idea of _“taking snapshots of”_ news websites and
analyzing their content every hour to check how different outlets
report particular news events.
**Universal Data Scrapers:** Participants envisioned a universal
scraper capable of retrieving data using natural language ( _𝑃_ 01 _, 𝑃_ 06 _,_
_𝑃_ 07 _, 𝑃_ 08), particularly useful when journalist coverage is limited
( _𝑃_ 07). For instance, _𝑃_ 06 and _𝑃_ 07 highlighted the challenge of retrieving unstructured, non-standardized regulations from local state
governments across Germany, where documents are inconsistently
formatted and lack systematic accessibility. _𝑃_ 06 emphasized the
importance of city council proceedings for local democracy, noting the absence of a coherent publishing system. Similarly, _𝑃_ 07
remarked, _“I have to check around 18 different websites regularly, and_
_it would be great to have a tool to collect that data”_ . Additionally, _𝑃_ 07
suggested using such a tool to monitor the social media accounts of
radical political party members. In addition, _𝑃_ 01 noted its potential
for retrieving data from opaque social media platforms, which he
referred to as _“black boxes”_ . Both _𝑃_ 01 and _𝑃_ 08 endorsed the idea
of multi-modal scrapers capable of transcribing, analyzing, and
summarizing speech, audio, or video content.
**LLMs Web Search Engines:** Participants ( _𝑃_ 01 _, 𝑃_ 03) suggested
AI agents functioning as advanced search engines. _𝑃_ 03 noted that
posing a question to a _chatbot_ is far easier than manually searching
for answers online. Similarly, _𝑃_ 01 explained that much of their work
involves _“googling_ _and_ _finding_ _relevant_ _details”_ and argued that


generative AI agents simplify the retrieving process and utilizing
information.


_4.1.2_ _Filtering._ Participants also recognized the value of LLMs in
reducing redundant information ( _𝑃_ 01 _, 𝑃_ 02 _, 𝑃_ 03, _𝑃_ 05 _, 𝑃_ 07). For example, _𝑃_ 03 shared how she used ChatGPT to clean web markups,
spotlight elements, and generate automation scripts. Furthermore,
_𝑃_ 02 and _𝑃_ 07 highlighted its application in searching documents and
automated findings reporting. Additionally, _𝑃_ 01 primarily relied
on automation for fact-checking and document analysis. However,
automated fact-checking using machine learning is still limited, as
agents struggle to distinguish between complex and trivial facts.
_𝑃_ 04 explained how automation could help when investigating economic topics such as white-collar crime (i.e., corruption) by looking
into big data registries and quickly filtering and categorizing information.


_4.1.3_ _Documenting._ Participants also discussed the importance of
documenting and maintaining a clear record of the investigative
process. _𝑃_ 05 and _𝑃_ 08 reported that they usually do not work with
much data but rather with small snippets of leaked information.
Their job involves researching multiple websites to gather information and integrating it with government databases. As noted
by _𝑃_ 05, documenting this process could be challenging and timeconsuming, and recalling the origin of the data may be difficult.
_𝑃_ 05 described a tool, which he referred to as _“a time machine”_, that
records users’ digital activities during investigations and allows
them to retrace their steps back to the source.


_4.1.4_ _Storing._ During the interviews, participants highlighted challenges associated with data storage and cloud architecture ( _𝑃_ 03, _𝑃_ 05,
_𝑃_ 07, and _𝑃_ 08). _𝑃_ 03 and _𝑃_ 07 reported issues related to saving data in
databases, which they attributed to a lack of software knowledge.
_𝑃_ 05 claimed that journalists often waste significant time copying
data from multiple files. He reflected, _“it takes your time to do great_
_research”_, and speculated that an automated solution could solve
this issue. Additionally, he suggested implementing an automated
system to convert investigation reports into Excel files. Furthermore, _𝑃_ 08 proposed an automated process for saving data to the
cloud using LLMs. Interestingly, _𝑃_ 03 proposed sharing automation
workflows among outlets without exchanging the collected data
to prevent sensitive data leakage while calling a plugin that could


“This could save us months of work” - Use Cases of AI and Automation Support in Investigative Journalism


automatically collect **any (un)structured** online content and store
it in the cloud as _“a superpower”_ .


_4.1.5_ _Augmenting._ Participants believed that AI and automation
assist in augmenting information discovery and boosting their productivity. _𝑃_ 08 illustrated an automated process by expanding the
scraping scripts, automatically executing in the cloud, storing collected data, and reporting the progress to the user. Interestingly,
_𝑃_ 07 considered the automatic email folder organization as an automation tool. All participants used generative AI to program and
write scripts. _𝑃_ 04 stated using LLMs to get initial investigation leads
by analyzing small snippets during the investigation.


**4.2** **Reporting**


_4.2.1_ _Analyzing._ Themes on the role of data exploration using
LLMs emerged repeatedly during interviews ( _𝑃_ 01 _, 𝑃_ 02 _, 𝑃_ 07 _, 𝑃_ 08).
Participants _𝑃_ 02 _, 𝑃_ 03, and _𝑃_ 08 warned about hallucinations [30]
when using LLMs. Despite these concerns, their ability to quickly
identify patterns overlooked during research makes them useful
data visualizers ( _𝑃_ 02, _𝑃_ 07, and _𝑃_ 08). For example, _𝑃_ 03 _, 𝑃_ 04, and _𝑃_ 05
underlined the idea of representing data in knowledge graphs. _𝑃_ 05
stated that an AI-assisted KG could potentially optimize the query
results. Furthermore, _𝑃_ 01 elaborated on generating info-graphics
metrics. In addition, _𝑃_ 01 briefly explained a concept of a large RAG

[40] using several LLMs to securely chat with 150 million various
formatted articles from their archive. _𝑃_ 04 mentioned using LLMs
to generate initial leads when verifying leaks before beginning the
investigation. _𝑃_ 03 also argued using LLMs to generate relevant
queries for further investigation. In contrast, _𝑃_ 03 was doubtful
about the benefit of LLMs in data analysis and raised concerns
about deterring data literacy. Analogously, _𝑃_ 06 stated, _“I am just_
_not sure if it [LLMs] can interpret data in the way that humans do”_ .


_4.2.2_ _Labeling._ Participants also mentioned clustering content and
discovering relations ( _𝑃_ 01 _, 𝑃_ 06). _𝑃_ 01 was already working on automatic data annotating and labeling articles using generative AI
technologies. Interestingly, _𝑃_ 06 explains the process of creating a
crime map network based on police reports.


_4.2.3_ _Writing._ Participants also used LLMs to summarize text from
documents or transcribed interviews. _𝑃_ 06 reported using LLMs to
rewrite hundreds of parents’ reports on dangerous children’s school
routes and generate news headlines. _𝑃_ 07 considered using LLMs for
_“brainstorming inspiring ideas”_ while writing reports but refrained
from using them for rephrasing or copy editing, as he valued the
originality of his work. Additionally, _𝑃_ 06 mentioned that LLMs are
helpful for text editing, such as citing interview question outlines,
and noted that automation can also be applied to storytelling. He
touched on using an AI illustrator and discussed integrating a print
layout automation system.


**5** **DISCUSSION**


The following section outlines the study outcomes, discussing how
automation and AI impact digital investigation. We find that investigative journalists must work with vast data sources while ensuring
the reported information is still valid, accurate, and reliable. They
often use automation as a means to build custom workflows for


data extraction from public databases, social media platforms, or
proprietary document archives.
We provide a set of journalistic use cases that can act as a basis for
developing new automation tools. Our findings showed that the reported use cases are mainly related to information gathering rather
than reporting. These results may be influenced by participants’
OSINT-based profiling and the focus of the elicitation prototype
on data scraping and analysis. Further studies on understanding
reporting scenarios could help to complete the entire automation
pipeline.


**5.1** **Automation Helps When Done Right**


With the growing scope of automation and adoption of LLMs in
journalism, more tangled stories can be investigated. Our interviews indicate that many tools are already available to journalists,
and new ones will continue to emerge. However, we find that many
existing research solutions do not adequately address user needs.
Therefore, we emphasize the importance of involving experts, affected stakeholders, and developers in a co-creation process to
enhance the transparency of such systems.
Our study reveals that a demonstration-based LLM system could
simplify information extraction by automating repetitive tasks, significantly speeding up research. Participants noted the need for
multi-modal agents to facilitate source monitoring. To this end,
stacking agents with different capabilities could reduce the workload, broaden automation scope, and accelerate investigation outcomes, especially when dealing with unstructured information. We
reported that journalists without sufficient technical training might
struggle with cloud storage. LLMs can streamline structuring data,
converting files on multiple formats, and simplifying data ingestion.
In addition, our findings underscore the importance of an automated systematic documentation process to maintain investigation
records, as it allows journalists to trace back investigation leads,
enabling more transparency. Furthermore, researchers can explore
alternative methods to share automation workflows as described
by _𝑃_ 03, which can encourage collaboration among news outlets
and enhance privacy. Another positive aspect of this approach is
that it improves the reproducibility of online research, provided
that the data is accessible.
To summarize, we can identify a few design recommendations
based on study results for future research. Users should be able
to (1) get (un) structured data quickly using multi-modal agents
running periodically; (2) automatically convert and store collected
data in multiple formats with the support of LLMs; (3) document,
record, and track the actions during investigations; and (4) securely
share automation flows without sharing sensitive data.


**5.2** **Ironies When Automating Investigations**


On another level, while automation boosts efficiency, it introduces
new risks related to reliability, accountability, and transparency

[36]. Journalists value accurate and credible story reporting.
The **bias** embedded in the training data used to power the AI
systems [33] can diminish journalistic values [36] as it can generate inaccurate stories that can mislead or radically influence the
audiences. Additionally, **LLMs hallucinations** [30] can produce
inaccurate facts, undermining the trustworthiness of such systems


and the reliability of their output. This way, automation could
harm the reputation of the publishers [24] and also threaten consumers’ trust. For example, when doing web automation, LLMs may
generate code with outdated dependencies, introducing vulnerabilities and security issues ( _𝑃_ 08). Raising awareness, _“AI literacy”_,
and establishing clear guidelines for using AI in the newsroom
are essential for building trust in autonomous systems. This could
be achieved by organizing workshops within investigative teams
or developing simple prototypes to demonstrate and test system
capabilities.
We identified several use cases affected by automation, in particular, related to information retrieval and source monitoring. Retrieving data from complex digital systems is complicated and requires
knowledge and expertise. Consequently, the overlap between data
science and investigative reporting continues to expand [15]. Even
if outlets automate fact-checking [55] through automatic claim verification, human intervention would still be necessary to validate
and ensure the relevance and accuracy of results. While automation helps in information retrieval and could bridge knowledge
gaps, journalism involves more than just collecting data. The ability of journalists to structure and fact-check sources and evaluate
automation outcomes utilizing computational and data thinking

[15] is crucial in preserving the integrity of automated reporting.
Additionally, journalists need statistical knowledge and a deep understanding of how information flows on the internet to identify
suitable data, interpret it, and create the right stories ( _𝑃_ 03) . KoutsKlemm [37] argues that the information loses value unless news
workers properly interpret it. Due to the shift in today’s data-driven
digital world, there is an ongoing recalibration of responsibilities
related to journalistic roles in the newsroom [16, 24]. Journalists
must acquire new skills to uphold technology updates [15] and
embrace the idea of **data and internet literacy**, which refers to
the ability to structure, analyze, understand, and report insights
from data [23].
Another topic is **budget constraints**, particularly faced by local
news agencies [20, 36], when implementing large-scale automation
( _𝑃_ 06). Running scrapers on the cloud or paying third-party services
to host automation systems can be costly. A local outlet may lack
the resources to support such tools for finding newsworthy stories
( _𝑃_ 06). Furthermore, an investigation topic might not be **relevant**
for a long time to be automated, and specific topics might show up
only once [51] ( _𝑃_ 05).


**5.3** **Limitations**


The study’s limitations include a small number of participants
based in Germany, with an average age of 37 _._ 5, as we focused on recruiting experienced practitioners. We leveraged the practitioners’
technical backgrounds and expertise to inform our future goal of
transforming their workflows into tools targeting less technically
trained news workers. A larger participant pool, including more
non-technically skilled journalists, could reveal additional automation use cases. In addition, we did not let users interact with the
prototype, which could have yielded more insights.


Cifliku and Heuer


**6** **CONCLUSION**


This paper serves as a starting point for exploring how generative
AI and PbD can assist journalists in data collection and automation processes. We provide actionable insights on **collection** and
**reporting** .
Our findings highlight the potential for journalists to adopt automation technologies that simplify data retrieval from multiple
sources without the need for programming skills. We encourage
future work to examine the potential of PbD in the context of
automating journalistic workflows.


**REFERENCES**


[1] James Auger. 2013. Speculative design: crafting the speculation. _Digital Creativity_
24, 1 (2013), 11–35. [https://doi.org/10.1080/14626268.2013.767276](https://doi.org/10.1080/14626268.2013.767276)

[2] Shaon Barman, Sarah Chasins, Rastislav Bodik, and Sumit Gulwani. 2016. Ringer:
web automation by demonstration. In _Proceedings of the 2016 ACM SIGPLAN_
_International Conference on Object-Oriented Programming, Systems, Languages,_
_and_ _Applications_ (Amsterdam, Netherlands) _(OOPSLA_ _2016)_ . Association for
Computing Machinery, New York, NY, USA, 748–764. [https://doi.org/10.1145/](https://doi.org/10.1145/2983990.2984020)
[2983990.2984020](https://doi.org/10.1145/2983990.2984020)

[3] Leonor Barroca, Helen Sharp, Dina Salah, Katie Taylor, and Peggy Gregory. 2018.
Bridging the gap between research and agile practice: an evolutionary model.
_International_ _Journal_ _of_ _System_ _Assurance_ _Engineering_ _and_ _Management_ 9, 2
(2018), 323–334. [https://doi.org/10.1007/s13198-015-0355-5](https://doi.org/10.1007/s13198-015-0355-5)

[4] Meredith Broussard. 2015. Artificial Intelligence for Investigative Reporting.
_Digital Journalism_ 3, 6 (2015), 814–831. [https://doi.org/10.1080/21670811.2014.](https://doi.org/10.1080/21670811.2014.985497)
[985497](https://doi.org/10.1080/21670811.2014.985497)

[5] Sarah Elizabeth Chasins. 2019. _Democratizing Web Automation: Programming_
_for Social Scientists and Other Domain Experts_ . Ph. D. Dissertation. University of
California, Berkeley. [https://escholarship.org/uc/item/332664jd](https://escholarship.org/uc/item/332664jd) ProQuest ID:
Chasins_berkeley_0028E_19245, Merritt ID: ark:/13030/m5zh20g8.

[6] Sarah Cohen, James T. Hamilton, and Fred Turner. 2011. Computational journalism. _Commun. ACM_ 54, 10 (2011), 66–71. [https://doi.org/10.1145/2001269.](https://doi.org/10.1145/2001269.2001288)
[2001288](https://doi.org/10.1145/2001269.2001288)

[7] Wikipedia Contributors. 2025. Dirty data. [https://en.wikipedia.org/wiki/Dirty_](https://en.wikipedia.org/wiki/Dirty_data)
[data](https://en.wikipedia.org/wiki/Dirty_data) Accessed: 2025-03-03.

[8] [Wikipedia contributors. 2025. Requirements elicitation. https://en.wikipedia.org/](https://en.wikipedia.org/wiki/Requirements_elicitation)
[wiki/Requirements_elicitation.](https://en.wikipedia.org/wiki/Requirements_elicitation) [https://en.wikipedia.org/wiki/Requirements_](https://en.wikipedia.org/wiki/Requirements_elicitation)
[elicitation](https://en.wikipedia.org/wiki/Requirements_elicitation) Accessed: 2025-01-23.

[9] Hannes Cools. 2022. _How algorithms are augmenting the journalistic institution:_
_In search of evidence from newsrooms and its innovation labs_ . Ph. D. Dissertation.
KU Leuven, Faculty of Social Sciences. [https://research.kuleuven.be/portal/en/](https://research.kuleuven.be/portal/en/project/3H190286)
[project/3H190286](https://research.kuleuven.be/portal/en/project/3H190286)

[10] Hannes Cools and Nicholas Diakopoulos. 2024. Uses of Generative AI in the
Newsroom: Mapping Journalists’ Perceptions of Perils and Possibilities. _Journal-_
_ism Practice_ 0, 0 (2024), 1–19. [https://doi.org/10.1080/17512786.2024.2394558](https://doi.org/10.1080/17512786.2024.2394558)

[11] Juliet Corbin and Anselm Strauss. 2014. _Basics of Qualitative Research: Techniques_
_and Procedures for Developing Grounded Theory_ (4th ed.). SAGE Publications, Inc,
Thousand Oaks, CA. 456 pages.

[12] Allen Cypher, Daniel C. Halbert, David Kurlander, Henry Lieberman, David
Maulsby, Brad A. Myers, and Alan Turransky (Eds.). 1993. _Watch_ _what_ _I_ _do:_
_programming by demonstration_ . MIT Press, Cambridge, MA, USA.

[13] Miessler Daniel. 2025. Fabric: open-source framework for augmenting humans
using AI. [https://github.com/danielmiessler/fabric.](https://github.com/danielmiessler/fabric) Accessed: 2025-01-08.

[14] Nicholas Diakopoulos. 2019. _Automating the News: How Algorithms Are Rewriting_
_the Media_ . Harvard University Press. [http://www.jstor.org/stable/j.ctv24w634d](http://www.jstor.org/stable/j.ctv24w634d)

[15] Nicholas Diakopoulos. 2024. Data journalism: The emergence of computational
journalism at Georgia Tech, 2006-2008. In _Milestones in Digital Journalism_ . Taylor
and Francis, 30–48. [https://doi.org/10.4324/9781003316152-3](https://doi.org/10.4324/9781003316152-3)

[16] Nick Diakopoulos. 2024. The Impact of Generative AI on Journalistic Labor. [https://generative-ai-newsroom.com/the-impact-of-generative-ai-on-](https://generative-ai-newsroom.com/the-impact-of-generative-ai-on-journalistic-labor-e87a6c333245)
[journalistic-labor-e87a6c333245](https://generative-ai-newsroom.com/the-impact-of-generative-ai-on-journalistic-labor-e87a6c333245) Accessed: 2025-01-15.

[17] Nicholas Diakopoulos, Hannes Cools, Charlotte Li, Natali Helberger, Ernest Kung,
Aimee Rinehart, and Lisa Gibbs. 2024. _Generative AI in Journalism: The Evolution_
_of Newswork and Ethics in a Generative Information Ecosystem_ . Technical Report.
Associated Press. [https://doi.org/10.13140/RG.2.2.31540.05765](https://doi.org/10.13140/RG.2.2.31540.05765)

[18] Nicholas Diakopoulos, Madison Dong, and Leonard Bronner. 2020. Generating
Location-Based News Leads for National Politics Reporting. _Proc Computational_
_+ Journalism Symposium_ (2020). [https://par.nsf.gov/biblio/10206645](https://par.nsf.gov/biblio/10206645)

[19] Anthony Dunne and Fiona Raby. 2013. _Speculative Everything: Design, Fiction,_
_and Social Dreaming_ . The MIT Press. 240 pages.

[20] Paul Farhi. 2024. _Is American Journalism Headed Toward an ‘Extinction-Level_
_Event’?_ [https://www.theatlantic.com/ideas/archive/2024/01/media-layoffs-la-](https://www.theatlantic.com/ideas/archive/2024/01/media-layoffs-la-times/677285/)


“This could save us months of work” - Use Cases of AI and Automation Support in Investigative Journalism


[times/677285/](https://www.theatlantic.com/ideas/archive/2024/01/media-layoffs-la-times/677285/)

[21] Bruce B. Frey. 2018. _The SAGE Encyclopedia of Educational Research, Measurement,_
_and_ _Evaluation_ . Vol. 4. SAGE Publications, Inc., Thousand Oaks, California.
[https://doi.org/10.4135/9781506326139](https://doi.org/10.4135/9781506326139)

[22] Marina Fridman, Roy Krøvel, and Fabrizio Palumbo. 2023. How (not to) Run
an AI Project in Investigative Journalism. _Journalism_ _Practice_ (2023), 1–18.
[https://doi.org/10.1080/17512786.2023.2253797](https://doi.org/10.1080/17512786.2023.2253797)

[23] Friedrich-Schiller-Universitat Jena. 2024. What is Data Literacy? - Information
on the topics data and data competencies. [https://www.dataliteracy.uni-jena.](https://www.dataliteracy.uni-jena.de/en/26/what-is-data-literacy)
[de/en/26/what-is-data-literacy](https://www.dataliteracy.uni-jena.de/en/26/what-is-data-literacy) Accessed: 2025-03-04.

[24] Andreas Graefe. 2016. Guide to automated journalism. _Columbia Journalism_
_Review_ (2016). [https://www.cjr.org/tow_center_reports/guide_to_automated_](https://www.cjr.org/tow_center_reports/guide_to_automated_journalism.php)
[journalism.php](https://www.cjr.org/tow_center_reports/guide_to_automated_journalism.php)

[25] Izzeddin Gur, Hiroki Furuta, Austin Huang, Mustafa Safdari, Yutaka Matsuo,
Douglas Eck, and Aleksandra Faust. 2024. A Real-World WebAgent with Planning,
Long Context Understanding, and Program Synthesis. [arXiv:2307.12856 [cs.LG]](https://arxiv.org/abs/2307.12856)
[https://arxiv.org/abs/2307.12856](https://arxiv.org/abs/2307.12856)

[26] James T. Hamilton. 2018. _Democracy’s Detectives: The Economics of Investigative_
_Journalism_ . Harvard University Press.

[27] James T. Hamilton and Fred Turnern. 2009. _Accountability Through Algorithm:_
_Developing the Field of Computational Journalism_ . Technical Report. Developing
the Field of Computational Journalism, a Center For Advanced Study in the
Behavioral Sciences Summer Workshop. [https://web.stanford.edu/~fturner/](https://web.stanford.edu/~fturner/Hamilton%20Turner%20Acc%20by%20Alg%20Final.pdf)
[Hamilton%20Turner%20Acc%20by%20Alg%20Final.pdf](https://web.stanford.edu/~fturner/Hamilton%20Turner%20Acc%20by%20Alg%20Final.pdf)

[28] Hendrik Heuer and Elena Leah Glassman. 2023. Accessible Text Tools: Where
They Are Needed & What They Should Look Like. In _Extended_ _Abstracts_ _of_
_the_ _2023_ _CHI_ _Conference_ _on_ _Human_ _Factors_ _in_ _Computing_ _Systems_ (Hamburg,
Germany) _(CHI EA ’23)_ . Association for Computing Machinery, New York, NY,
USA, Article 20, 7 pages. [https://doi.org/10.1145/3544549.3585749](https://doi.org/10.1145/3544549.3585749)

[29] Hendrik Heuer, Hendrik Hoch, Andreas Breiter, and Yannis Theocharis. 2021.
Auditing the Biases Enacted by YouTube for Political Topics in Germany. In
_Proceedings_ _of_ _Mensch_ _Und_ _Computer_ _2021_ (Ingolstadt, Germany) _(MuC_ _’21)_ .
Association for Computing Machinery, New York, NY, USA, 456–468. [https:](https://doi.org/10.1145/3473856.3473864)
[//doi.org/10.1145/3473856.3473864](https://doi.org/10.1145/3473856.3473864)

[30] Lei Huang, Weijiang Yu, Weitao Ma, Weihong Zhong, Zhangyin Feng, Haotian
Wang, Qianglong Chen, Weihua Peng, Xiaocheng Feng, Bing Qin, and Ting
Liu. 2024. A Survey on Hallucination in Large Language Models: Principles,
Taxonomy, Challenges, and Open Questions. _ACM Trans. Inf. Syst._ (2024). [https:](https://doi.org/10.1145/3703155)
[//doi.org/10.1145/3703155](https://doi.org/10.1145/3703155)

[31] Internet Archive. 2025. Wayback Machine. [http://web.archive.org.](http://web.archive.org) [http://web.](http://web.archive.org)
[archive.org](http://web.archive.org) Accessed: 2025-01-23.

[32] Hasan M. Jamil and Sajratul Y. Rubaiat. 2024. Online Digital Investigative Journalism Using SociaLens. In _Information Integration and Web Intelligence: 26th_
_International Conference, IiWAS 2024, Bratislava, Slovak Republic, December 2–4,_
_2024, Proceedings, Part II_ (Bratislava, Slovakia). Springer-Verlag, Berlin, Heidelberg, 103–117. [https://doi.org/10.1007/978-3-031-78093-6_9](https://doi.org/10.1007/978-3-031-78093-6_9)

[33] Juliane Jarke and Hendrik Heuer. 2024. Reassembling the Black Box of Machine
Learning: Of Monsters and the Reversibility of Foldings. In _Algorithmic Regimes:_
_Methods,_ _Interactions,_ _and_ _Politics_, Juliane Jarke, Bianca Prietl, Simon Egbert,
Yana Boeva, Hendrik Heuer, and Maike Arnold (Eds.). Amsterdam University
Press, Amsterdam, 103–125.

[34] Stephen Kasica, Charles Berret, and Tamara Munzner. 2023. Dirty Data in the
Newsroom: Comparing Data Preparation in Journalism and Data Science. In
_Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems_
(Hamburg, Germany) _(CHI_ _’23)_ . Association for Computing Machinery, New
York, NY, USA, Article 865, 18 pages. [https://doi.org/10.1145/3544548.3581271](https://doi.org/10.1145/3544548.3581271)

[35] Samantha Kolovson, Samuel So, and Sean A. Munson. 2024. Using Speculative
Design to Understand Preferred Futures for the Design and Use of Tracking
Data in U.S. College Sport Teams. _Proc. ACM Hum.-Comput. Interact._ 8, CSCW1,
Article 189 (April 2024), 35 pages. [https://doi.org/10.1145/3641028](https://doi.org/10.1145/3641028)

[36] Tomoko Komatsu, Marisela Gutierrez Lopez, Stephann Makri, Colin Porlezza,
Glenda Cooper, Andrew MacFarlane, and Sondess Missaoui. 2020. AI should
embody our values: Investigating journalistic values to inform AI technology
design. In _Proceedings of the 11th Nordic Conference on Human-Computer Inter-_
_action: Shaping Experiences, Shaping Society_ (Tallinn, Estonia) _(NordiCHI ’20)_ .
Association for Computing Machinery, New York, NY, USA, Article 11, 13 pages.
[https://doi.org/10.1145/3419249.3420105](https://doi.org/10.1145/3419249.3420105)

[37] Ragne Kouts-Klemm. 2019. Data literacy among journalists: A skills-assessment
based approach. _Central European Journal of Communication_ 12, 3 (2019). [https:](https://doi.org/10.19195/1899-5101.12.3(24).2)
[//doi.org/10.19195/1899-5101.12.3(24).2](https://doi.org/10.19195/1899-5101.12.3(24).2)

[38] Hanyu Lai, Xiao Liu, Iat Long Iong, Shuntian Yao, Yuxuan Chen, Pengbo Shen,
Hao Yu, Hanchen Zhang, Xiaohan Zhang, Yuxiao Dong, and Jie Tang. 2024.
AutoWebGLM: A Large Language Model-based Web Navigating Agent. In _Pro-_
_ceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data_
_Mining_ (Barcelona, Spain) _(KDD_ _’24)_ . Association for Computing Machinery,
New York, NY, USA, 5295–5306. [https://doi.org/10.1145/3637528.3671620](https://doi.org/10.1145/3637528.3671620)

[39] LaVague. 2025. LaVague - Large Action Model framework to develop AI Web
Agents. [https://github.com/lavague-ai/LaVague.](https://github.com/lavague-ai/LaVague) Accessed: 2025-01-08.


[40] Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir
Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim
Rocktäschel, Sebastian Riedel, and Douwe Kiela. 2020. Retrieval-augmented
generation for knowledge-intensive NLP tasks. In _Proceedings of the 34th Inter-_
_national Conference on Neural Information Processing Systems_ (Vancouver, BC,
Canada) _(NIPS_ _’20)_ . Curran Associates Inc., Red Hook, NY, USA, Article 793,
16 pages.

[41] Andrew MacFarlane, Marisela Gutierrez-Lopez, Stephann Makri, Tim Atwell,
Sondess Missaoui, Colin Porlezza, and Cooper Glenda. 2022. DMINR:
A Tool to Support Journalists Information Verification and Exploration.
[arXiv:2204.13546 [cs.HC]](https://arxiv.org/abs/2204.13546) [https://arxiv.org/abs/2204.13546](https://arxiv.org/abs/2204.13546)

[42] Philipp Mayring. 1991. Qualitative Inhaltsanalyse. In _Handbuch_ _qualitative_
_Forschung : Grundlagen, Konzepte, Methoden und Anwendungen_ . Beltz - Psychologie Verl. Union, München, 209–213.

[43] Philipp Mayring. 2000. Qualitative Content Analysis. _Forum Qualitative Sozial-_
_forschung_ _/_ _Forum:_ _Qualitative_ _Social_ _Research_ 1, 2 (2000). [https://doi.org/10.](https://doi.org/10.17169/fqs-1.2.1089)
[17169/fqs-1.2.1089](https://doi.org/10.17169/fqs-1.2.1089)

[44] Sondess Missaoui, Marisela Gutierrez-Lopez, Andrew MacFarlane, Stephann
Makri, Colin Porlezza, and Glenda Cooper. 2019. How to Blend Journalistic
Expertise with Artificial Intelligence for Research and Verifying News Stories.
In _CHI 2019 ACM Conference on Human Factors in Computing Systems_ . [https:](https://openaccess.city.ac.uk/id/eprint/22996/1/AI-CHI19.pdf)
[//openaccess.city.ac.uk/id/eprint/22996/1/AI-CHI19.pdf](https://openaccess.city.ac.uk/id/eprint/22996/1/AI-CHI19.pdf)

[45] Adam Nugent. 2022. The Role of Investigative Journalism to Uncover Fraud and
Corruption in Europe. [https://www.europarl.europa.eu/RegData/etudes/BRIE/](https://www.europarl.europa.eu/RegData/etudes/BRIE/2023/747083/IPOL_BRI(2023)747083_EN.pdf)
[2023/747083/IPOL_BRI(2023)747083_EN.pdf](https://www.europarl.europa.eu/RegData/etudes/BRIE/2023/747083/IPOL_BRI(2023)747083_EN.pdf) Accessed: January 22, 2025.

[46] OpenAI. 2025. ChatGPT. [https://openai.com/index/chatgpt/.](https://openai.com/index/chatgpt/) [https://openai.](https://openai.com/index/chatgpt/)
[com/index/chatgpt/](https://openai.com/index/chatgpt/) Accessed: 2025-01-23.

[47] Deokgun Park, Simranjit Sachar, Nicholas Diakopoulos, and Niklas Elmqvist.
2016. Supporting Comment Moderators in Identifying High Quality Online
News Comments. In _Proceedings of the 2016 CHI Conference on Human Factors_
_in_ _Computing_ _Systems_ (San Jose, California, USA) _(CHI_ _’16)_ . Association for
Computing Machinery, New York, NY, USA, 1114–1125. [https://doi.org/10.1145/](https://doi.org/10.1145/2858036.2858389)
[2858036.2858389](https://doi.org/10.1145/2858036.2858389)

[48] Savvas Petridis, Nicholas Diakopoulos, Kevin Crowston, Mark Hansen, Keren
Henderson, Stan Jastrzebski, Jeffrey V Nickerson, and Lydia B Chilton. 2023.
AngleKindling: Supporting Journalistic Angle Ideation with Large Language
Models. In _Proceedings of the 2023 CHI Conference on Human Factors in Computing_
_Systems_ (Hamburg, Germany) _(CHI ’23)_ . Association for Computing Machinery,
New York, NY, USA, Article 225, 16 pages. [https://doi.org/10.1145/3544548.](https://doi.org/10.1145/3544548.3580907)
[3580907](https://doi.org/10.1145/3544548.3580907)

[49] Rebecca S." "Robinson. 2014. _Purposive Sampling_ . Springer Netherlands, Dordrecht, 5243–5245. [https://doi.org/10.1007/978-94-007-0753-5_2337](https://doi.org/10.1007/978-94-007-0753-5_2337)

[50] Skyvern. 2025. Skyvern - Automate Browser-Based Workflows with AI. [https:](https://www.skyvern.com)
[//www.skyvern.com.](https://www.skyvern.com) Accessed: 2025-01-08.

[51] Jonathan Stray. 2019. Making Artificial Intelligence Work for Investigative
Journalism. _Digital Journalism_ 7, 8 (2019), 1076–1097. [https://doi.org/10.1080/](https://doi.org/10.1080/21670811.2019.1630289)
[21670811.2019.1630289](https://doi.org/10.1080/21670811.2019.1630289)

[52] Brian Tang and Kang Shin. 2024. Steward: Natural Language Web Automation.
_arXiv preprint arXiv:1905.10900_ (2024).

[53] Dick van Eijk. 2005. _Investigative Journalism in Europe_ . Vereniging van Onderzoeksjournalisten (VVOJ). [https://books.google.de/books?id=Yie2AAAACAAJ](https://books.google.de/books?id=Yie2AAAACAAJ)
[Online Report: https://www.vvoj.org/tag/vvoj-in-english/page/4/.](https://www.vvoj.org/tag/vvoj-in-english/page/4/)

[54] Radu-Daniel Vatavu and Jacob O. Wobbrock. 2016. Between-Subjects Elicitation
Studies: Formalization and Tool Support. In _Proceedings of the 2016 CHI Conference_
_on Human Factors in Computing Systems_ (San Jose, California, USA) _(CHI ’16)_ .
Association for Computing Machinery, New York, NY, USA, 3390–3402. [https:](https://doi.org/10.1145/2858036.2858228)
[//doi.org/10.1145/2858036.2858228](https://doi.org/10.1145/2858036.2858228)

[55] Robert Wolfe and Tanushree Mitra. 2024. The Impact and Opportunities of
Generative AI in Fact-Checking. In _Proceedings_ _of_ _the_ _2024_ _ACM_ _Conference_
_on_ _Fairness,_ _Accountability,_ _and_ _Transparency_ (Rio de Janeiro, Brazil) _(FAccT_
_’24)_ . Association for Computing Machinery, New York, NY, USA, 1531–1543.
[https://doi.org/10.1145/3630106.3658987](https://doi.org/10.1145/3630106.3658987)

[56] Lena Wuergler, Pauline Cancela, David Gerber, and Annik Dubied. 2023. Identifying Investigative Pieces. _Journalism Studies_ 24, 14 (2023), 1754–1774. [https:](https://doi.org/10.1080/1461670X.2023.2209814)
[//doi.org/10.1080/1461670X.2023.2209814](https://doi.org/10.1080/1461670X.2023.2209814)


**A** **APPENDIX**

**A.1** **Participants**

**A.2** **Automation Use-Case Video Prototyping**


Illustration of a use case scenario to audit data from YouTube similar
to Heuer et al. [29] using the elicitation prototype explained in
Section 3.2 .


**Table 2: Distribution of participants according to their role**
**at** **the** **newsroom,** **their** **age,** **gender,** **and** **their** **educational**
**background**

|Col1|Role|Age|Gender|Education|
|---|---|---|---|---|
|P1|OSINT (Fact Checking)|39|m|PhD|
|P2|Data Journalist|34|f|Master|
|P3|OSINT (Fact-checking)|37|f|Master|
|P4|Data Journalist|34|f|Master|
|P5|OSINT (Digital Forensic)|37|m|Master|
|P6|Data Journalist|40|m|PhD|
|P7|Reporter & Editor|39|m|Master|
|P8|Cyber-intelligence|40|m|College Degree|


The user starts inputting a URL in the prototype,
which triggers a local browser to pop up. The user
navigates to YouTube and searches for “Journalism”.
Upon clicking the first search result, the user is redirected to the corresponding video page. The user
can then select elements to scrape, such as the video
title, description, or the number of comments. The
user can also click on a second video recommendation. Throughout the process, JournalXRecorder
tracks all interactions. While the user only needs
to demonstrate the scraping process once, the tool
can automatically collect all video results. Once the
scraping is complete, the user uploads and analyze
the collected using the chat.


**A.3** **Interview Questions**


(1) Can we record the video?
(2) We would like to know a bit more about you. Could you
please introduce yourself, explain what you do, and why
you are interested in this workshop? What news outlets
have you worked for in the past?
(3) Could you share your gender, age, and highest education
level?
(4) What kind of journalism are you working on?
(5) For which tasks do you use Chat GPT or other similar AI
based tools for?
(6) How do these AI tools affect your work?
(7) Have you ever collected and analyzed large amounts of
data? If so, for which tasks?

    - Did you find it challenging to do?

    - If yes, could you please elaborate on the challenges or
limitations?
(8) Have you used any automation (tools) for your work?

    - YES: What kind of automation do you use?

    - YES: Why did you use automation?

    - YES: How did automation affect your work?

    - YES: What challenges did you face when automating?

    - NO: Why did you not use any automation?


Cifliku and Heuer


(9) What challenges or limitations do you face when you want
to use automation tools?
(10) Imagine having all the necessary computational and human
resources available; what kind of tool (with or without AI)
do you wish for that could support you on your job?


After the participants had seen the prototype, we further asked:


(1) What similar tools have you seen or used before?
(2) What are your thoughts on our prototype?
(3) What did you like about the tool?
(4) What did you dislike about the tool?
(5) How could this tool assist you in your work?
(6) Could you think for a few minutes about use cases where
you could use such a tool in your work? If not, why would
you not use it?
(7) From your perspective, we would love to know what we
can do to improve our tool. What new features would you
like to have?
(8) Open discussion
