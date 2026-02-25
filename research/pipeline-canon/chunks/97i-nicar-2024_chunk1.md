<!-- chunk: 1/2 | source: 97i-nicar-2024.md | words: 37907 -->
<!-- headings: NICAR 2024 Tipsheets & Session Notes; 2024-ai-101-tools-tips.pdf; **AI-driven tools, tips and tricks to empower your data journalism**; 2024-ai-202-cooking-genai.md; **Automated CAPTCHA solving with Anti-Captcha API**; **Table of contents**; **Introduction** `<a id="introduction">`{=html}`</a>`{=html}; **Installation and importing** `<a id="installation">`{=html}`</a>`{=html}; **Getting started** `<a id="getting-started">`{=html}`</a>`{=html}; **What information do we need to send to the API?** `<a id="what-information">`{=html}`</a>`{=html}; **Where do we get the `sitekey`?** `<a id="where-do-we-get-the-sitekey">`{=html}`</a>`{=html}; Await the result of query_selector before evaluating; Use the element handle to evaluate the JavaScript expression; **How do we send this information to the API?** `<a id="how-do-we-send-this-information">`{=html}`</a>`{=html}; **Solving CAPTCHAs** `<a id="solving-captchas">`{=html}`</a>`{=html}; **Inject and submit in Browser** `<a id="inject-and-submit">`{=html}`</a>`{=html}; **Step 1: Inject the solution into the CAPTCHA**; inject the response into the page; **Step 2: Submit the form**; **Skip the browser and submit with an undocumented API** `<a id="skip-the-browser">`{=html}`</a>`{=html} -->

# NICAR 2024 Tipsheets & Session Notes




## 2024-ai-101-tools-tips.pdf

# **AI-driven tools, tips and tricks to empower your data journalism**

_Dozens of new, powerful (and sometimes scary) AI tools have already started transforming_
_society and industries as a whole. What this means for news is an ongoing conversation. But_
_some of these tools can be a boon to newsroom data journalists and coders. We walk_
_through a dozen big and small tools, tips and tricks for utilizing AI in your daily workflows._


Details

  - Thursday, March 7 from 9 to 10 a.m. in room Harbor C

  - [Slide deck](https://docs.google.com/presentation/d/e/2PACX-1vQ5AsqOiHScmxM-H-wwPbyv2dJOCUgKW-Oc9H6MRjgsmdPuEb1OJVilRiu7nko5htHkJOu1gqpI0Rkr/pub?start=false&loop=false&delayms=3000)


Panelists

  - [June Minju Kim, mk4672@columbia.edu](mailto:mk4672@columbia.edu)

    - MIT Technology Review and AI project for The Brown Institute for Media
Innovation

    - Arriving in Baltimore Wednesday evening (5 pm)

  - Mike Reilley, [mikereilley1@gmail.com](mailto:mikereilley1@gmail.com) | @itsmikereilley | @journtoolbox |
MikeReilley.com

    - University of Illinois Chicago and JournalistsToolbox.ai

    - Arriving in Baltimore Wednesday afternoon

  - [Jeff Hargarten, jeff.hargarten@startribune.com](mailto:jeff.hargarten@startribune.com)

    - Star Tribune

    - Arriving in Baltimore Wednesday afternoon

  - [Darla Cameron, dcameron@texastribune.org](mailto:dcameron@texastribune.org)

    - Texas Tribune + IRE board (moderator)

    - Arriving in Baltimore around 6 p.m. Wednesday


Outline

  - 5 minutes: Brief introductions

    - We are the best advocates for our journalistic needs. It’s critical that
newsrooms take a beat and think through what their needs are, instead of
trusting vendors to tell us what our needs are.

    - This panel is designed to help you articulate your needs as a data reporter or
developer. I’m excited about how AI might help us scale and solve some of the
big challenges we face as data journalists.

  - Intro question:

    - Why SHOULD we use AI for journalism?

  - 20 minutes: Each panelist takes 5 minutes to share one or two examples of an AI tool
that they find really helpful

    - Let’s think of these as lightning talk-style demos using screen recordings,
instead of live presentations, and keep them super brief


  - 20 minutes: Discussion using refined versions of the questions below, designed to
prompt conversation — time to riff together on the potentials and pitfalls ahead.

    - What have you learned so far from your experiments using AI tools for data
journalism? Are there any lessons for your organization or the industry more
broadly?

    - What do you wish other journalists knew about how to make their AI
experiments successful?

    - What kind of technical skills do journalists need to cultivate to be proficient at
working with AI vs. developing their own AI tools?

    - How should we consider pitches from companies making plug and play tools
with this tech?

    - How can journalists self-determine to solve real problems we have instead of
the problems that tech company think we have?

    - How do we help people in our newsrooms overcome the fear of it? Tools to
advocate for this in the newsroom?

    - How can journalists make tools for themselves?

  - 15 minutes: audience questions, with specific prompts if we have time:

    - What problem are you facing? Ask the panelists what AI tool might present a
useful solution.

       - What’s something that you wish could be automagically done for you


Async brainstorm:

  - Introduce yourself to the other panelists. What is your official role and what kind of AI
work are you exploring?

    - **Mike Reilley,** I teach data and digital journalism at UIC and run
JournalistsToolbox.ai. I’m a Google News Initiative trainer (8th year), now with
RTDNA. I also do trainings for Gannett and just launched the ONA/Microsoft
AI in Journalism Initiative trainings, which debuts the week before NICAR. I
also do some AI trainings for newsrooms, university faculty and state bar
[associations. Rest in the bio: mikereilley.com](https://mikereilley.com/)

    - **Jeff Hargarten** : I’ve been a data journalist at the Star Tribune in Minneapolis
for a decade. I principally analyze data, help other reporters write stories,
design data visualizations and code internal tools. I’ve been exploring AI
solutions to aid my efficiencies around all of the above.

    - **June Kim** : I’m a data reporter currently covering climate and technology at
MIT Technology Review. But I also work with the Brown Institute of Media
Innovation on a grant project, building an AI-driven tool for investigative
journalists that help analyze public comments on federal regulations.

    - **Darla Cameron:** I’m a managing editor at the Texas Tribune working with our
data, photo and product teams. I’m leading our experiments with AI in the


newsroom, including writing policies to set guardrails for how we will use the
technology and establishing new collaborations.


- What is the best AI tool or workflow you’ve tried?

   - **Reilley:** So many. Vidiofy, many copy editing tools, image-creation tools,
Rolliapp’s Information Tracer, also working on a CustomGPT for the Toolbox
right now.

   - **Hargarten** : The list is ever-growing. GitHub Copilot plugin for VSCode helps
me scaffold whole Svelte app projects on the fly. I designed an entire internal
Minneapolis crime tracking dashboard in R using only GPT4 prompts. Any of
the LLM tools can generate near-flawless FOIA or state data practices
requests in the correct format, and a few times even found and appended my
contact information. GPTExcel has been brilliant for writing super complex
Excel formulas, saving me hours-to-days on complex data analyses. This
[mapbox-adjacent tool has an AI bot that shows me map design solutions I’ve](https://demo.kapa.ai/widget/mapbox)
never encountered in my decade of coding with their JS and API. Just some
examples.

   - **June Kim:** I lean on copilot when I’m building charts or analyzing data,
especially when using libraries I’m unfamiliar with. I’d also like to share a tool
that I’ve built, specifically for investigative and policy journalists. It’s a
lightweight website that compiles all public comments posted on
Regulations.gov and provides downloadable CSV files, as well as extracted
information such as commenters’ names, where they’re from, what they do,
and what they are saying in the comments. It’s meant to be a window into
who’s voicing their opinions on important regulations being made. Also GPT
for google sheet, when doing collaborative work.


- What is the most challenging or disappointing AI tool or workflow you’ve tried?

   - **Reilley:** Again, so many. Probably some of the image creation tools. And some
of the poor data analysis results on some of the LLMs. (I do a fun experiment
with them in my classes that I’ll talk about. Some of the data tools have
worked OK (spreadsheets, plug-ins). Diagram (cq) for making charts has
worked nicely a couple of times. I will demo all o f these in my training session
on Thursday afternoon.

   - **Hargarten** : Some tools just aren’t as good as the manual tools we have in our
newsroom, like ChartGPT has less utility than just even making a chart in
Excel. ChatGPT’s Data Analyst has mostly been a potato, in my experience.
ChatGPT3 seems so promising, but often just circles the solution, and getting
it to land can be frustrating, and sometimes it never produces what you want
and soon you’ve wasted more time fighting with this AI than it would have
taken to StackOverflow the solution yourself – upgrading to GPT4 is so worth


the $20, especially if your newsroom is paying.


- What have you learned so far from your experiments using AI tools for data
journalism? Are there any lessons for your organization or the industry more broadly?

   - **Reilley** : Reliability issues (see data analysis above). I use Claude a lot for it. It’s
accurate for certain things, not for others.

   - **Hargarten** : It’s not in a place where it can automagically just do all your work
for you (yet). It’s very good at coding and solving tech challenges, but
soulless-to-suspect around much else. Our journalistic sensibilities are
necessary to guide these tools. In that sense, it helps shift my thinking away
from the technological nuts-and-bolts I’ve spent years bashing my head
against as a Swiss Army Nerd, and into a space where I’m focusing FAR
MORE on accuracy, creativity, storytelling and other fundamentals that drive
the core of what journalists do. And using these tools really highlights for me
how important it is for news organizations to value that human expertise and
focus on implementing AI merely as an enhancement, not a replacement, for
people-powered journalism.

   - **June Kim:** My perspective is more from building the AI tool for journalists.
Manual checking of data integrity is so, so important and often ignored.
Problems can be very specific to the problem and they arise very
unexpectedly. So always assuming there could be something off about the
tool is a good attitude, I think.


- What do you wish other journalists knew about how to make their AI experiments
successful?

   - **Reilley:** Don’t be AFRAID to experiment and fail. Just don’t publish anything
unless it has human editing/quality control on the back end. (AP’s 80/20 rule)

   - **Hargarten** : Prompting is an art all by itself. Depending upon the tool, there can
be wildly different results between asking for the same thing one way versus
another. More detail is important, but not so much that it crosses and
confuses your asks. So don’t write AI off if a tool initially generates garbage
instead of just automagically spitting out what you wanted. Play with it, be
specific, check everything – chances are you’re still saving time.

   - **June Kim:** Understanding how the tools are built and being diligent about
learning and communicating the limitations of the tool/methodologies. Very
flawed. A lot of work to ask people to do, but there’s just no way around ti


- Where do you see this technology going next?

   - **Reilley:** Nobody knows for sure. Limitless possibilities. LLMs are an unfinished
product. They’re learning and getting smarter.

   - **Hargarten** : This “copilot” notion where everyone has a custom-tuned AI
assistant on their phones or computers that can basically help with anything,


wear any hat and purportedly make everything easier seems to be the next
wave. Also smarter AI integration for search results, e.g. Google Gemini, could
have deep impacts on our industry. The rapid pace of AI development can be
scary. AI image editing on phones has tons of ramifications. Comparing Dall-E
generated images in March 2024 versus March 2023 is a quantum leap in
development in merely a year’s time. Misinformation and disinformation could
proliferate at an alarming rate. The tech is still in its infancy, and so are the
associated challenges and the threat of swan-diving further into dystopia if
these tools are implemented and used recklessly.

- **June Kim:** Many different ways I think, but the way I “hope” to see it go next, in
the journalism context, is more journalists being involved in the creation of
these tools that are tailor-made for journalists and reporting purposes.


## 2024-ai-202-cooking-genai.md

AI 202: Cooking with generative AI
Andrew Ford, Pri Bengani, Jeff Kao and Jonathan Soma

https://bit.ly/nicar2024ai202 

Submit your data reporting problems 
and we'll show you how we’d try to solve them: 
https://bit.ly/nicar_ai

Why are you here
Using LLMs Effectively
Ethics
Anecdotes
APIs and Local LLMs
Validating LLM outputs
Do it live!heessdesssw4wawagdddxftfxf5sa,,,,, 
Agenda
Intro (1 minute each / 4 minutes total)
Effectiveness (Jeff) (11 minutes total)
Ethics (Jeff) (11 minutes total)
One Anecdote (Jeff) (11 minutes total)
More Anecdotes (Andrew) (11 minutes total)
Learning a skill (Pri) (11 minutes total)
APIs and Local LLM (Pri) (11 minutes total)
Validating LLM outputs (Soma) (11 minutes total)
Do it live (All who are interested - 10 minutes total)


AI is coming for your job


AI is coming for your job
Data reporters using
are


Let’s embrace being LAZY

If your good-intentioned, and eager to please friend (that is generally knowledgeable but has poor judgment) told you something that you wanted to hear…
Embrace being lazy but with caution... 
LLMs hallucinate, get things wrong frequently, and are non-deterministic
Generative AI is bad at getting facts exactly right…

Embrace being Lazy
…would you put it in your story without checking it out?


Embrace being LAZY for easy things

You already know what the answer should look like
80% of your time is spent on easy but time-consuming tasks (?)
Save time/energy for the hard problems that require your thinking, judgment and expertise
Tools that help you move up the data reporter stack
Lazy for Easy Things
Fact checks
Write a story
Web scraping
Search primary sources
Interpret and compile data points
Data analysis
Data visualization
Add numbers together
Interview a source
FOIA requests
judgment/complexity
high
low
Write/debug code
old tools
new tools

LLMs can also help with tasks that require basic, commonly known domain knowledge, like...
Template code 
Basic SQL
Boilerplate data viz 
(including identifying common approach)
Regex
Explaining vague errors and exceptions
Simple line editing
(finding headlines or alternative phrasing)
(BUT it can water-down nuanced/complex thoughts)

Embrace being Lazy

Fact checks
Write a story
Web scraping
Search primary sources
Interpret and compile data points
Data analysis
Data visualization
Add numbers together
Interview a source
FOIA requests
judgment/complexity
high
low
Write/debug code
old tools
new tools
When to Embrace being Lazy?
-	available knowledge	+
-	reasoning/creativity	+

Fact checks
Write a story
Web scraping
Search primary sources
Interpret and compile data points
Data analysis
Data visualization
Add numbers together
Interview a source
FOIA requests
judgment/complexity
high
low
Write/debug code
old tools
new tools
When to Embrace being Lazy?
-	available knowledge	+
-	reasoning/creativity	+
Don’t buy into the hype:

Fact checks
Write a story
Web scraping
Search primary sources
Interpret and compile data points
Data analysis
Data visualization
Add numbers together
Interview a source
FOIA requests
judgment/complexity
high
low
Write/debug code
old tools
new tools
When to Embrace being Lazy?
-	available knowledge	+
-	reasoning/creativity	+
Don’t buy into the hype:
They are essentially next-word predictors

Fact checks
Write a story
Web scraping
Search primary sources
Interpret and compile data points
Data analysis
Data visualization
Add numbers together
Interview a source
FOIA requests
judgment/complexity
high
low
Write/debug code
old tools
new tools
When to Embrace being Lazy?
-	available knowledge	+
-	reasoning/creativity	+
But they are constantly getting more sophisticated 😱
Don’t buy into the hype:
They are essentially next-word predictors

Don’t check your brain at the door

LLMs are not people
(start around 20:16)

LLMs are not people
LLMs are generating statistically likely tokens to imitate people based on context.
they have no internal monologue - they need to compute out loud
they can’t go back and edit what they randomly generated, even if it’s wrong
BUT they have perfect working memory (of what’s already written down)

Takeaways:
Be aware where it might have a lot of knowledge/too little
Provide outside knowledge: “I googled _____ and found”
Work iteratively
Let the model talk!
“State the assumptions and then…”
“Work step-by-step”
“Critique your reasoning/conclusions”
Unlock parts of the LLM that might have better abilities
“As an expert…”
How can we use Generative AI more effectively?
-	available knowledge	+
-	reasoning/creativity	+

REMEMBER:
You’re typing at a machine that is designed to trick people into thinking it’s a human
You are good at what the model isn’t, e.g.:
define the goal
break down the task 
logic/creativity/metacognition
How can we use Generative AI more effectively?
-	available knowledge	+
-	reasoning/creativity	+

So use your judgment

Some newsroom guidelines:
https://generative-ai-newsroom.com/towards-guidelines-for-guidelines-on-the-use-of-generative-ai-in-newsrooms-55b0c2c1d960 
https://www.bbc.co.uk/mediacentre/articles/2024/update-generative-ai-and-ai-tools-bbc 
Journalistic Ethics and Generative AI
newsroom guidelines
personal ethics
trained on proprietary or private data w/o permission
bias in models
risk of plagiarism
energy consumption for model training
transparency/passing off LLM content as human work
feeding an LLM proprietary info that becomes training data
use cases that reduce trust
supply chain ethics (RLHF; data sources)

Debug: loading data into a database
Full transcript: https://chat.openai.com/c/6a2b960f-31f5-44dd-adfe-3b465c3682f9
Error while reading data, error message: CSV table references column position 46, but line contains only 38 columns.;
byte_offset_to_start_of_line: 585891075 column_index: 46
While loading a 20GB file into BigQuery….
I had to correct it a few times….

Debug: loading data into a database
Full transcript: https://chat.openai.com/c/6a2b960f-31f5-44dd-adfe-3b465c3682f9

A word from a scrappy newspaper reporter 
Work the cost-benefit, ChatGPT and the like are great, when they work. (See Maximizing Utility at 2:15 today)
Flatten privilege — attending NICAR is awesome, a masters is great, working with ProPublica LRN is an incredible experience. If you can’t have that (yet), AI can help fill (some) gaps in access 
Think about your unique selling point — if ChatGPT can be a decent data analyst and an improving writer, what makes you special? 

Battle ornery records custodians
ChatGPT is said to have passed the bar
Generally, legalistic records requests get better responses
So let it be your pitbull (for informal purposes, and be mindful of security)
Help draft the initial request, battle it out with citations
Treat it like an intern – always check its work

Battle ornery records custodians

Battle ornery records custodians
How’d we do?

✅ “...pursuant to the Arizona Public Records Law, A.R.S. §§ 39-121 through 39-161...” 

✅ “Under A.R.S. § 39-121.01(D), I am entitled to inspect or receive copies of public records…” 

❌ “Please note that A.R.S. § 39-121.01(B) requires that you promptly respond to this request.” (Promptness is established elsewhere)

🤨 “Furthermore, I would like to remind you of the importance of transparency and accountability in public administration, as emphasized in the case of Mathews v. Pyle, 75 Ariz. 76, 251 P.2d 893 (1952), which affirmed the right of citizens to access public records.” (Kind of, not exactly on point)


Matthews v. Pyle – ”It is our view that we may reasonably conclude that the documents received by the Governor in his official capacity were not intended to be classified by the legislature as public records, but they may fall within the classification of "other matters", in section 12-412, supra, and therefore subject to inspection by an interested citizen unless they are confidential or of such a nature that it would be against the best interests of the state to permit a disclosure of their contents.”


Battle ornery records custodians

Battle ornery records custodians
“I understand that Arizona Public Records Law does not specify a strict timeline for the production of records. However, the law does require that access to public records be provided "promptly" (✅ A.R.S. § 39-121.01(D)). The Arizona Supreme Court has interpreted this to mean that a custodian of records must respond to a request within a "reasonable" time frame, considering the nature and volume of the requested documents (Carlson v. Pima County, 141 Ariz. 487, 687 P.2d 1242 (1984))❌.
A hit and a miss. So it gets better with conversation (don’t we all?), and it does represent a time savings.

Write code
ChatGPT can be hit or miss as an attorney, but it can write clean Python (or other languages) faster than you can type
Excellent tutor, build on what you’re starting at NICAR. You still need to be able to read the code. 
Can debug well if the code is relatively short (but you can do a lot with short code)
Introduction to new packages (Streamlit)


ChatGPT to make your own web apps
https://bit.ly/NICARJustTheFacts
Skip hours of querying stack overflow

ChatGPT to make your own web apps

ChatGPT to make your own web apps

https://www.azcentral.com/story/news/local/arizona-investigations/2023/07/10/arizona-doctor-misconduct-search/70375177007/
Help your process, help your colleagues, add something interactive to your reporting, ROI is strong because it can be done fairly quickly and bears fruit for a long time

Machine learning

Machine learning
ChatGPT can write code to deploy a machine learning model 
And it can produce a set of sentences to train on
Flagging keywords is cool 
Flagging ideas is cooler 
Speed up big doc review, or set up alerts
Worked well enough on an upcoming story that I’d recommend it 

Create sample data sets
sentence,label
"The contract guarantees officers a minimum of 10 days' notice before they are required to attend any disciplinary hearing.",0
"Officers are allowed to review all evidence against them before any internal investigation begins.",1
"The contract limits the use of force to situations where it is absolutely necessary for the protection of life.",0
"Any complaints against officers must be filed within 30 days of the incident, or they will not be considered.",1
"Officers are entitled to legal representation at all stages of the disciplinary process.",0
"The contract prohibits the release of an officer's disciplinary records to the public without their consent.",1
"Officers are required to undergo regular training on de-escalation techniques and cultural sensitivity.",0
"The contract allows officers to appeal disciplinary actions through an arbitration process.",1
"Officers must report any use of force incidents within 24 hours to their supervisor.",0
"Any disciplinary action taken against an officer will be removed from their record after five years.",1


Create sample data sets
2021 3rd place Phil Meyer win, which recognizes “The best uses of empirical methods in journalism”
How we did it then: https://www.propublica.org/article/how-we-found-pricey-provisions-in-new-jersey-police-contracts
We might do it faster or better today 
Do a longer training set faster (still need experts to guide which practices are problematic) 

More on LLMs from Jeff

Don’t like the chat interface? Want to do more?
APIs:
Really easy to get started! Costs some $. They promise not to train models with your data.
ChatGPT: https://www.datacamp.com/tutorial/a-beginners-guide-to-chatgpt-api 
Anthropic/Claude: https://docs.anthropic.com/claude/reference/getting-started-with-the-api 
Others: Google, Microsoft Azure, Open source LLaMa APIs, etc.
Local LLMs: 
https://colab.research.google.com/drive/1QbbU9vEfk9FxGO_qOBbGzido0dEK70Iw  

Running LLMs locally

Why local?
Terms and conditions keep changing — don’t know at what point your data, prompts, and responses will be used to improve existing commercial products like ChatGPT
Sensitive documents or datasets — you might not feel comfortable relying on a third-party entity 
Can deploy to an air-gapped computer if needed 
Might be more cost-effective, especially in the long run 
More control over environment 
Why not?
It’s a lot more work! 
Easier access to the state-of-the-art or the latest and greatest 
Up-to-date information means it's more useful in most scenarios
Might be easier to scale depending on the context 
Will be able to do most tasks without a lot of fine-tuning or validation or sanity checks — but always always always sanity check! 

How do you decide which model to use? 


Deploying the model locally


Prompt
The chat interface

Increase this number if you want to work with really large texts... 

...or pass in small chunks of text. 

The server...that you can access programatically
Sample “AI assistant” code
Overflow policies

Things to remember
Test the same thing over and over again to see how varied and inconsistent the results can be
Check the “context overflow” setting and ensure you handle that by 
setting a higher context length 
chunking your documents to ensure there’s no overflow
ensuring third-party libraries haven’t specified different max token lengths
More parameters typically means better models but also far more compute resources
Just because an LLM might be able to do something, it doesn’t mean it’s the right approach

Large language models are awful at everything they do and it’s only by a strange, strange accident that we find them useful

Error resilient tasks	
Problems with tight feedback loops
A large number of tasks where individual errors don’t matter too much
Tasks where low-quality outputs can just be ignored


Errors are going to happen, so anticipate and measure them


take a large handful, evaluate with a human

Out of 4 scored by a human as YES, our AI marked 3 as “YES” and one as “MAYBE”
Out of the 5 scored as YES by the AI, the human only agreed on 3 of them

It probably won’t miss many good story leads, but it will make us read some useless bills


Response validation and repair


Name
Email
Food being written about
Language


Or just stop caring!


Work on the process
1. Don't trust the answers. Measure the errors! (Confusion matrices + error tracking)
2. Don't trust the output. Validate and repair! (Guardrails) 
3. Don’t trust the bot. Provide suggestions that humans can ignore instead of demands!

Submit your data reporting problems 
and we'll show you how we’d try to solve them: 
https://bit.ly/nicar_ai

Questions we got during the session:


Questions we got during the session:

Too much data

Data cleaning 
Questions we got during the session:

Too much data

Data cleaning 
Questions we got during the session:

Too much data
cojxoijcio

Data cleaning 
Questions we got during the session:

Too much data
cojxoijcio
finding sources of data

My colleague is investigating whether there was a coordinated effort across states to [remove objectionable books from schools and public libraries]. She has filed public records requests for emails from officials that contain keywords like [evolution, LGBT, feminism, history of race, climate change], etc. Is there was a way for a LLM to read through these emails and identify if certain individuals or groups were in contact with officials across multiple states?
Audience Question:


Thank you!
Andrew Ford, Pri Bengani, Jeff Kao and Jonathan Soma

BONUS SLIDES

Bonus: Customize ChatGPT

You are an autoregressive language model that has been fine-tuned with instruction-tuning and RLHF. You carefully provide accurate, factual, thoughtful, nuanced answers, and are brilliant at reasoning. If you think there might not be a correct answer, you say so.

Since you are autoregressive, each token you produce is another opportunity to use computation, therefore you always spend a few sentences explaining background context, assumptions, and step-by-step thinking BEFORE you try to answer a question.

Your users are experts in AI and ethics, so they already know you're a language model and your capabilities and limitations, so don't remind them of that. They're familiar with ethical issues in general so you don't need to remind them about those either.

Don't be verbose in your answers, but do provide details and examples where it might help the explanation.

Bonus: Limitations and Pitfalls
Source: https://x.com/FractalEcho/status/1758968904674836979?s=20


Bonus: Limitations and Pitfalls
Source: https://x.com/FractalEcho/status/1758968904674836979?s=20



## **Automated CAPTCHA solving with Anti-Captcha API**

*By Ryan Little, Data Editor at The Baltimore Banner* ``{=html} [GitHub](https://github.com/ryanelittle), [Twitter/X](https://twitter.com/RyanLittleE), [Work Email](mailto:ryan.little@thebaltimorebanner.com), [Personal Email](mailto:ryanerinlittle@gmail.com)

This notebook demonstrates how to use the [ANTI-CAPTCHA API](https://anti-captcha.com/) to solve CAPTCHAs. This API is a paid service that uses human workers to solve CAPTCHAs. In this notebook, we will solve Google\'s reCAPTCHA v2, which is a common type of CAPTCHA used on the web. However, the API can solve many other types of CAPTCHAs as well.

`Note: API KEY` We will use an API key paid for by [The Baltimore Banner](https://www.thebaltimorebanner.com) in today\'s class. This key will be invalid at the end of the class. If you are working with this notebook after the class, you will need to obtain your own API key from the ANTI-CAPTCHA website.


## **Table of contents**

1.  [Introduction](#introduction)
2.  [Installation and importing](#installation)
3.  [Getting started](#getting-started)
    - A. [What information do we need to send to the API?](#what-information)
    - B. [Where do we get the sitekey?](#where-do-we-get-the-sitekey)
    - C. [How do we send this information to the API?](#how-do-we-send-this-information)
4.  [Solving CAPTCHAs](#solving-captchas)
    - A. [Inject and submit in Browser](#inject-and-submit)
    - B. [Skip the browser and submit with an undocumented API](#skip-the-browser)
    - C. [Inject and submit with JavaScript](#inject-and-submit-js)
5.  [Links to other resources](#other-resources)
6.  [Extra credit](#extra-credit)



## **Introduction** `<a id="introduction">`{=html}`</a>`{=html}

CAPTCHAs are a common way to prevent bots from accessing a website. They are used to distinguish between human and bot traffic. They are sometimes used by government entities to make it harder for journalists to access public information. For example, the [Maryland Judiciary Case Search](https://casesearch.courts.state.md.us/casesearch/) website uses CAPTCHAs to prevent web scraping.

There are three primary strategies to overcoming CAPTCHAs:

- Find a way to never have to solve a CAPTCHA.
- Solve the CAPTCHA programatically with some type of Optical Character Recognition.
- Solve the CAPTCHA with a human worker.

For this hands-on class, we will focus on the third strategy. We will use the Anti-Captcha API to solve CAPTCHAs for us. This API uses human workers to solve CAPTCHAs. It is a paid service, but it is relatively inexpensive. The most difficult part is determining how to inject the CAPTCHA solution into the website.

In this notebook, we will demonstrate how to use the Anti-Captcha API to solve CAPTCHAs for our public records web scrapers. We will use the API to solve a sample CAPTCHA and then inject the solution. We will cover three ways to submit the solution once it is obtained: using a \"submit\" button, submitting the response to an undocumented API and calling custom JavaScript functions.

`Note: Automation tool choice` There are multiple automation tools designed for testing web applications. The most popular one is called Selenium. However, we will be using Playwright, a new web automation tool that is similar to Selemium but is easier to use and has more features like device emulation and tracing. The strategies taught in this notebook will work in Selenium, but the code will be slightly different.


## **Installation and importing** `<a id="installation">`{=html}`</a>`{=html}

Everything you need to run this code has already been installed on the lab computers. If you are working on your local machine, you will need to install the packages below. Because we are using Playwright, we will need to install the Playwright package and then invoke the `playwright install` method to install the browsers we will use.

``` python
#This code has been commented out so it is not accidentally run by someone on a lab computer.
#Remove the hastgags from lines 4-8 to install the required packages and playwright.

#!pip install anticaptchaofficial
#!pip install playwright
#!pip install requests
#!pip install bs4
#!playwright install

from anticaptchaofficial.recaptchav2proxyless import * #importing the recaptchav2proxyless class from the anticaptchaofficial module
from IPython.display import Image #importing the Image class from the IP for displaying screenshots
from IPython.display import HTML #importing the HTML class from the IP for displaying HTML
from bs4 import BeautifulSoup
import playwright 
import requests 
```



## **Getting started** `<a id="getting-started">`{=html}`</a>`{=html}

There are many types of CAPTCHAs you are likely to encounter. The most common type is Google\'s reCAPTCHA v2. This is the type of CAPTCHA we will be solving in this notebook.

For these CAPTCHAs, the Anti-Captcha API works by having a human worker on its network visit the exact website you are trying to scrape. There, the worker will solve the CAPTCHA, intercept the unique solution key the CAPTCHA creates and redirect the unique key to your program via the API.

### **What information do we need to send to the API?** `<a id="what-information">`{=html}`</a>`{=html}

The ANTI-CAPTCHA API requires the following information to solve mosts Google recaptcha v2s:

- The website URL
- The `data-sitekey` value from the website.
- The method to use to solve the CAPTCHA (e.g. `recaptchaV2Proxyless()`)
- The API key

Let\'s take our first look at the code we will use to send this information to the API:

``` python
solver = recaptchaV2Proxyless() # creates a task object
solver.set_verbose(1) # 1 to receive more debug data, 0 to receive only result
solver.set_key(api_key) # setting anticaptcha api key
solver.set_website_url(url) # url of the site you are on
solver.set_website_key(sitekey) # unique key of the site

result = solver.solve_and_return_solution() # getting task result
```

### **Where do we get the `sitekey`?** `<a id="where-do-we-get-the-sitekey">`{=html}`</a>`{=html}

The `sitekey` is a value that is used to identify the CAPTCHA. It is usually found in the website\'s HTML. It is a long string of characters that is unique to the website. It is used to generate the CAPTCHA and to validate the solution.

We can find the `sitekey` by inspecting the website\'s HTML by hand. We can do this by right-clicking on the CAPTCHA and selecting \"Inspect\" from the context menu. This will open the browser\'s developer tools, which will show the website\'s HTML. We can then search for the `sitekey` by using the \"Find\" feature in the developer tools.

Sometimes, we can find it by searching for the `data-sitekey` attribute in the HTML. This attribute is used to store the `sitekey`. It is usually found in the `div` tag that contains the CAPTCHA.

For this example, we will use the following website: <https://www.google.com/recaptcha/api2/demo>. This website has a sample CAPTCHA that we can use to test the ANTI-CAPTCHA API.

This code block will load a Playwright-controlled Chrome browser. It will load Google\'s demo recaptcha. We will find the `sitekey` by querying the div that contains the CAPTCHA and then get the attribute `data-sitekey`.

``` python
from playwright.async_api import async_playwright

playwright = await async_playwright().start()
browser = await playwright.chromium.launch(headless=False)
page = await browser.new_page()
await page.goto("https://www.google.com/recaptcha/api2/demo")
# Await the result of query_selector before evaluating
g_recaptcha_element = await page.query_selector('div.g-recaptcha')
# Use the element handle to evaluate the JavaScript expression
sitekey = await g_recaptcha_element.get_attribute("data-sitekey")
print(sitekey)
```

    6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-

You should now see the sitekey printed above and the an open browser window with the Google recaptcha demo. If you don\'t see the browser window, you may need to click on the browser icon in the taskbar to bring it to the front. The browser is typically a different window than a normal Chrome window.

`Note: Sitekey` The `sitekey` is not always this easy to find. Some custom implimentations purposely hide the sitekey to make it more difficult to solve the CAPTCHA. In these cases, you may need to use a more advanced method to find the sitekey. We will cover this in the [Skip the browser and submit with an undocumented API](#skip-the-browser) section.

### **How do we send this information to the API?** `<a id="how-do-we-send-this-information">`{=html}`</a>`{=html}

Now let\'s use the `sitekey` to send the information to the Anti-Captcha API. We will use the code block below to send the information to the API. We will use the Anti-Captcha API to solve the CAPTCHA and then print the result.

First, we set the API key and url. Then we will use the code from above to call for a response from the API. This could take a few seconds or up to a minute. The timing will depend on the number of requests the API is currently processing and number of workers available to solve the CAPTCHA.

``` python
api_key = 'e016f394d73bb866e249d5aed2771139' #this key will no longer work after this class is over
url = page.url #this is the url we are at right now
```

``` python
solver = recaptchaV2Proxyless() # creates a task object
solver.set_verbose(1) # 1 to receive more debug data, 0 to receive only result
solver.set_key(api_key) # setting anticaptcha api key
solver.set_website_url(url) # example url
print(sitekey)
solver.set_website_key(sitekey) # example key

anti_captcha_response = solver.solve_and_return_solution() # getting task result
print(anti_captcha_response) # printing the result
```

    6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-
    making request to createTask
    created task with id 30278439
    making request to getTaskResult
    task is still processing
    making request to getTaskResult
    task is still processing
    making request to getTaskResult
    task is still processing
    making request to getTaskResult
    task solved
    03AFcWeA7LDp89FgzfvKw4Q_mEyuljxE6zJXvS5PatFOahOo3sBNLxOZpPMHQIjHC0ExxLNW7B6UWb_5_oIWElQkkvsiIlO-LByRXguMr-tthGNPsgSTdhNdi3JRfLh3Q5uKM3Ygdb6V1bKptG2xH0LBaukP8oGgRJZGpPIcM1CWrMCDB3PPybmO0leB-d7TmudngC-DvRPZmSaFAe4B-Mfk7zJoLAsdkppvKVsyRwPyJ_JUapj9PGK9_16uEz2goZW3Lxzjtlc8YtF-piaMaeqaSftyflcVp-UnlyLUaQt2qA9be22F67TInfGxr1kF7ZFrA3uD0xbii5ivGfXdmH0du2ioK9tJsnS7HMh-BcsBdgts8idhqpPSUZLzax7adE-1A2ezpxgDq0SmR5xlr7ZY1lWcvtqNWi7_RNSbVsOmx_hMp9ML6X0A0IH_e6EVAIKo1p_Z_CbVSdL-7djmQeZ5H1axVK-9mVinUAcIdgZ1D7gyoQ1T2dg2jq8aPn1xS_FZqUj50E9-mnJliFva-FY-jrIzX7cNCZwzHam0KdyPSvUwF3etH6RdIngusi1vKTYxr1A-hec_6bPCXZF_EoLJvbCbiKOVvevInLC_1rCjLlCb2GmQn_ypG6KihB03RUS-VjJjaQ9y-hLzOXQtGRgIAqwr7C00bL0zh1CzqGseNYW-KcPkHsXpVnVz62BaZBT4fXUbCe__U6kO01KmOvMNR4d57gNUWXuNR0O3pxUL0o4p5H-LW-v_VwpIiIHxXOfGf-L-zJx8XxbGm8TeE_wlFQuFlj6Drg9qeHpC1ylSqOC1JeKrKXI5bMnNVagtd2hHjyxrw0AKRP1K0byIf5K-fZy3e3MD6E-zyDAnlOuGAqr7QwN2cSy6rJEHMHC40nCV0kklYaqmKMEhrkKrYTF6D_IUK6ArMi7A6G33XIL3xSKcMCXLjjoruhNsyVjSvyfB25_EfE-g8tPTzA1Q490RoijcDiw4BanOAQGT0uKeylD8iwENiOxjEqZPGt7qOhDkyl5BBbyHvOOwdl6nGgQ-ykJ4q1Z9taS74mtbCwkqnA6cGbpxHw4e30qUFHFa6ESsOl--GzXAhL8V3tPRP2EIXACSYRQoFCpIBNEHWiDNmDKgwXf3UC1LByos8_HTbJFy5Le2CsxHfaRmPAAZyvTGu8ucpFkftkUFiz5gN_Ip7dhhYd9aeJMLdFrqBLvsFGcN6LJ43RuDucV6bGwvjvY-TVnNX6GXk20TvCc1E1XgrxggsaxFdbRYqNrF5ZmRj2DJ-oo33CDgVn6-AS_NKgkCoXzn4LocQ8_TmkwFXHydxT7G0aLSpWaNcLvgkm35tXzzzjXeThaNYD15GbvjJn1Jou--BF6Cul0gdu-2EyYw4P9DSE3PN4OsuKU3RgnT4mqHNy-hzZ7wZD0JFbxFy4aD6TjkKOm9pE-VbqunAz-vPhDt8PS9VvnBuZoiDBs09eoLbBso_B8JWSiulg3bT8iV2JdVjtXxX-E8ayyKz7M_j6iEtL3gY-LAC62GW93rywqvZ6Kc83IZpl58gtcNVPIEfNvmSNQWIWFTMWkDwvfyfKM94dJrKR8x5qYs-FPCcZLMTEjcxU7c-gcL3NHkFmVZeoUcApkB0hDwGMcpxt7CVPNYaSk46_ZnsL2NZ8RrbRd_EC43aJCaZoC7baS5VrIzfpjlURaIbcfFb-TRZBrr-7mmG55_Glt0F6z-5qVn5nzVfIwFrsBiM3SszRsEsPh3XHaJyuW_8LVWGosgCXGvCX_8MrcohRto9prlUuDRD_VG7FQ3L-GTf9Dr9lzYvoGFNOap4mYMdr4b4gr4e2YoWoEJIjAniivt-o62GovdGsb1jjTJtn5Xs1ATfxwpJeN4AcNStUKcG55dgsyaQI5pfoVF8lhPjVIVwmTW-gPhK0qtQg0iQPXodccJsNYdPXSrSW7-hcWy6Sfp-kwyCwxe95UrFyvEomJpJysKi9RCGeriOhnurg--Svo82MBuiXzIxKJ96xahKPeCOFrmB-Gd3jap2H_L334dUDuKTY6zBQ1KFKhmUXUDDpx0PRw8qo-Lvuo0B9l5HZIpUQlkT6pDOVcw1xERlgrTGNh68CD_lxzBwSqqL6DMoEDybduZIO2Pp9O__V3Wz3ycnIlTQl3zH4D3qX8q3vYHOvSPNIlMfc4Eqb9k0v3FO6BQel60IAs2Mh-RbJzbJ-rh_Din-LRQ8Vq41Z1Rnq-sgbiL8cSOdl0DAlpAUK80Z47F843eiKuy7TJjYyeFoQC0w143tbPxtz-X3RPQFiINW-VctjJyjJ5CNfj8WZiiqxq8jqG-I6iwAMhdnso4c85A

You should see the response printed above. The response will contain the solution to the CAPTCHA. This solution is a string of characters that can be used to solve the CAPTCHA. We will use this solution to inject the CAPTCHA into the website.


## **Solving CAPTCHAs** `<a id="solving-captchas">`{=html}`</a>`{=html}

Now that we have the solution to the CAPTCHA, we need to inject it into the website. There are a few ways to do this. We will cover three ways to submit the solution: using a \"submit\" button, using an undocumented API and using JavaScript.

### **Inject and submit in Browser** `<a id="inject-and-submit">`{=html}`</a>`{=html}

The first way to submit the solution is to use a \"submit\" button. This is the most common way to submit a form on a website. We can use Playwright to inject the solution into the CAPTCHA and then click the submit button.

We will try to use the browser we already have open. If that doesn\'t work, go back up to the code that creates a browser and get\'s the `sitekey` and run it again. Then come back to the code block below.

Before we bust this CAPTCHA, let\'s take a screen shot of the before.

``` python
await page.screenshot(path='screenshots/before-submission.png') #print screenshot of browser
display(Image(filename="screenshots/before-submission.png")) # Display the screenshot
```

#### **Step 1: Inject the solution into the CAPTCHA**

You can watch this happen by finding the \'g-recpatcha-response\' div in the browser inspector before running the code below.

``` python
# inject the response into the page
await page.evaluate(f'document.getElementById("g-recaptcha-response").innerHTML="{anti_captcha_response}"')
```

    '03AFcWeA5xBVtdneD7YNT4BvSvyG46bkN5AEvy4xiT3QP9qUYhLCZcZFwLY6D-fUc5aSoVJkO5TPQAk5g3Y8OwCSzQC12M8d-abWIE0Y5F6srnpjzFFwxMmi9K0z31PEdlMPYaHb-i7rICSLkAn5VznSNY-4TS_XA6I-UpQIkPxnWJX6s7As4OkpVFgxV_PwiUg3Yp7rQ-W-DONvZ_3pZXaQ1kiNAAw0VNbnf0IpI0tJNWBYMi-2VDBpkWaz19bnLbffSmyW_c6QDeOaAsscQuM-8d18RfmdCUrfF8QlVm2mKMFbLJ7PJqbLIH3qqQ3WnJ_ohSMqNqQN11rfh3VBTgcYwhQuXaB_AqjFYnK0XmGgkw6JBsqjY8enHEWBCUCbrRu7KhHLxJsDOFrDRn18OhZk_6B6kMVmZEfpIOKAMiHTQfj5oF-qeWMAU73FELSsto4srxRkdgOl13JMXWhkah6d871HSHotD7SplhmpUzOArHV8p38q_sLHN6y1U_PkALy4lGjUbtoOBeZ6lA_6sBW1kqKE-G70qKIuhr9WCtM1bmW98J3Ajzhh-Qc_KhiREk30zxUfix7SA5Tzi-MylUx50I7_9dTrj0k9-HpATUysKQweHe0XSbz4zt6e-JvExn5IY4Bk52U0LMDLfBZtdzd_Ij1doDxUTT0vXjFMJMj77rIwyd4_uFnfet_2ll_QcEIKkBeVTvr1Z60hoo_vb39712vlxjlL5rt2Xv94mmAMV19oOamEKx9h7Pg5GJuwhi2hySP6fOJHfFXUyX2tLz1Kg3RzKt1dVBdXSonKZsBGsFBoeXFM_d_2FbkcXAWVDI_Ng3y2nHqu3bQmg49NXwBYgf0ySZ2djiGbQK9AZsbw9Hg9FjfepHPY3UgkgJbrR0QtNGQmU62NTQy2So3Rz3qe8z-HeQzHc7WAJk1ITSQlj_RZNrhBPkBgNekbz8v-tkubfVFH6fM6dk2UOwW4cGJHaWxj1fl6oyQoUQ89Uz2KIg0rgFZbrV7uumaSKF3NPrjB6_uJyAhCgIbbvCTnulXaqRMsOZ37oh5xz-J_9nC3sLk0F47Jy9Dsx-_u-mHT67FPXU5xR7Ok6TTt-tnQ-pFPXXwZFCinxmVsmeqezVLhOi9AEB7Ct8t2DTmvfcQbawQ9rxTwN3vS1z7sgwJb0gymb0sFtQlagefBWLCaoASBklS0_ga5woW1K5mkT338evugnnSsqkv8kKDj2Ae3KYbxm3NhzVskzk8iNexPh4M9SyOkgtPaXEu4UwB76oupCLmR3g2C8ho7mUmwclG4JBjETRGowNmgOOepsM5MvGWrOoYwI5VOKItBCgt5dHZWrf56fUZYrs3UlcI8ILyznIR4Jo0qy3bYnGeD1kxf3EL9swjEbYY5iz0RLajRxwWqkPM2YeepFoQkIrRacEvcmqGhzGW4TTwR1X3GirEGjSr19cXUnTbyu_lZwnxXwXrjd71Yvfi6L6ZluowLQMZo05K_UvAgvXr_FJXKiB5iIfc6b1EwSietQb1G8lJ2VI11z0QNdyR9B8HQFRSI9U_sURAIGO7xyDdVvzItNPPbFjRbtL-gGUNDgKx-oQnhzH3PSIHRK8WVFnr9en'

#### **Step 2: Submit the form**

``` python
submit_button = await page.query_selector('//*[@id="recaptcha-demo-submit"]')# creates an object that represents the submit button
await submit_button.click() #clicks the submit button
```

``` python
await page.screenshot(path='screenshots/after-submission.png') #print screenshot of browser
display(Image(filename="screenshots/after-submission.png")) # Display the screenshot
```

Let\'s close that browser so we can open a new one and try the next method.

``` python
await browser.close()
```



## **Skip the browser and submit with an undocumented API** `<a id="skip-the-browser">`{=html}`</a>`{=html}

In some ways, this is the most advanced method. In others, it\'s the simplest. The trick here is using the tools described by Leon Yin\'s [Finding Undocument APIs](https://inspectelement.org/apis) to find an API that has the information we need. It is possible to find an API that appears to be protected by a CAPTCHA but it\'s actually not. Other times, the API requires a CAPTCHA solution to be sent as a parameter.

For this example, we will use the Maryland State Board of Elections Voter Lookup API. It requires a CAPTCHA solution to be sent as a parameter.

`NOTE: This Scraper is not really useful` The underlying data in the API is public and can be accessed by [purchasing voter registration lists](https://elections.maryland.gov/voter_registration/data.html). Typically, the Maryland State Board of Elections will waive fees for journalists.

#### **Step 1: Get the `sitekey`**

Unfortunately, the code we used earlier won\'t work. The `sitekey` is not in the HTML. Instead, I had to find it by searching the JavaScript files. This is a common way to hide the `sitekey` from web scrapers.

Run the code below to see what happens.

``` python
from playwright.async_api import async_playwright

playwright = await async_playwright().start()
browser = await playwright.chromium.launch(headless=False)
page = await browser.new_page()
await page.goto("https://voterservices.elections.maryland.gov/VoterResults")
# Await the result of query_selector before evaluating
g_recaptcha_element = await page.query_selector('div.g-recaptcha')
# Use the element handle to evaluate the JavaScript expression
sitekey = await g_recaptcha_element.get_attribute("data-sitekey")
browser.close()
print(sitekey)
```

Instead, I quickly found the sitekey by searching the JavaScript in the HTML using the browser inspector. This is a common way to hide the sitekey from web scrapers. It\'s possible to write code to pull the sitekey from the JavaScript files, but it\'s often easier ot just find it yourself by inspecting the page in a web browser. ``{=html} ``{=html} ``{=html} ``{=html}

#### **Step 2: Get the solution from Anti-Captcha**

``` python
api_key = 'e016f394d73bb866e249d5aed2771139' #this key will no longer work after this class is over
url = 'https://voterservices.elections.maryland.gov/VoterSearch'
sitekey = '6LfOqoQaAAAAAJumoHDEpR5ybjMoLs0vlckL-wkd'
#sitekey = '6LfOqoQaAAAAAJumoHDEpR5ybjMoLs0vlckL-wkd' #copied and pasted from inspecting the source of the website

solver = recaptchaV2Proxyless() # creates a task object
solver.set_verbose(1) # 1 to receive more debug data, 0 to receive only result
solver.set_key(api_key) # setting anticaptcha api key
solver.set_website_url(url) # example url
print(sitekey)
solver.set_website_key(sitekey) # example key

anti_captcha_response = solver.solve_and_return_solution() # getting task result
print(anti_captcha_response) # printing the result
```

#### **Step 3: Call the API with the CAPTCHA solution**

You can see what would happen without a solution by running the code below without the solution.

``` python
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
viewstate = soup.find(id='__VIEWSTATE')['value']
viewstategenerator = soup.find(id='__VIEWSTATEGENERATOR')['value']
eventvalidation = soup.find(id='__EVENTVALIDATION')['value']
print(viewstate, viewstategenerator, eventvalidation)
```

``` python
import requests

cookies = {
    '_ga_SQ06B8V4SF': 'GS1.1.1684347847.1.0.1684347856.0.0.0',
    '_ga_MDQZL9L6L5': 'GS1.1.1692127755.1.1.1692129115.0.0.0',
    '_ga_FMC7CCN0GD': 'GS1.1.1692127728.1.1.1692129161.0.0.0',
    '__gsas': 'ID=d6ec8b280c7996fe:T=1692211872:RT=1692211872:S=ALNI_MZTeLPF70DSVhNO2nLa2fecE3t1LA',
    '_ga_HFF70SMGZW': 'GS1.2.1692298470.1.1.1692298492.0.0.0',
    '_ga_GFHX73E8E3': 'GS1.1.1697035073.4.0.1697035073.0.0.0',
    '_ga_7J788E15ZL': 'GS1.1.1697125144.3.1.1697125449.60.0.0',
    '_ga_BFWLVL451M': 'GS1.1.1697467984.11.0.1697467989.55.0.0',
    '_ga_6YXDMHRX0X': 'GS1.1.1697488769.2.1.1697489688.0.0.0',
    '_ga_63CV5Y2TQG': 'GS1.1.1699916271.4.0.1699916271.0.0.0',
    '_ga_CBXPK98M4Q': 'GS1.1.1699999182.6.1.1700000849.0.0.0',
    '_ga_0YC16CCD4X': 'GS1.1.1701094680.1.1.1701094694.0.0.0',
    '_ga_366879341': 'GS1.1.1701430571.16.1.1701430571.0.0.0',
    '_ga_CF3KTNF4G6': 'GS1.1.1701430571.2.1.1701430571.0.0.0',
    '_ga_JWSSDNSRC1': 'GS1.1.1701808161.1.1.1701808203.0.0.0',
    '_ga_QKG4LJ7JLD': 'GS1.1.1703777538.1.0.1703777538.0.0.0',
    '_ga_ZP48NY6MR7': 'GS1.1.1703777539.1.0.1703777539.0.0.0',
    '_ga_1ZY55NML4M': 'GS1.1.1704319045.14.0.1704319045.0.0.0',
    '_ga_MTLMMN1WH4': 'GS1.1.1704317413.4.1.1704319047.60.0.0',
    '_ga_8B4ZSK23KY': 'GS1.2.1706040903.2.1.1706040929.0.0.0',
    '_ga_0BZFNFE34F': 'GS1.1.1706208660.11.0.1706208660.0.0.0',
    '_ga_6D4R5G9TNJ': 'GS1.2.1706628384.4.0.1706628384.0.0.0',
    'nmstat': '56197ed4-31c7-1869-cfe0-1195bfd0b8b1',
    '_ga_S1781DM4BJ': 'GS1.1.1706643402.2.0.1706643402.0.0.0',
    '_ga_SLX0CQ3HRM': 'GS1.1.1706713816.3.0.1706713818.58.0.0',
    '_ga_R1LE8KQW1T': 'GS1.2.1706823486.3.1.1706824757.0.0.0',
    '_ga': 'GA1.1.1886365173.1683662029',
    '_ga_KJKE71WK2Y': 'GS1.1.1707084016.1.1.1707084872.0.0.0',
    '_ga_LJCC9XG5J9': 'GS1.1.1707084016.34.1.1707084872.0.0.0',
    'ASP.NET_SessionId': 'av2lpbbcvddfdxwx10uehhbr',
    '_ga_7G2EGZ357T': 'GS1.1.1707089172.14.0.1707089172.0.0.0',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'DNT': '1',
    'Origin': 'https://voterservices.elections.maryland.gov',
    'Referer': 'https://voterservices.elections.maryland.gov/VoterSearch',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    # 'Cookie': '_ga_QKG4LJ7JLD=GS1.1.1707150074.2.0.1707150078.0.0.0; _ga_ZP48NY6MR7=GS1.1.1707150074.2.0.1707150078.0.0.0; _ga_F6GG4ZJNNW=GS1.1.1707253896.1.1.1707254726.0.0.0; _ga_0LFN5749EH=GS1.1.1708383406.5.0.1708383406.0.0.0; _ga_8B4ZSK23KY=GS1.2.1710879032.3.0.1710879032.0.0.0; _ga_5ZJ7TGHP45=GS1.1.1712066756.5.1.1712066756.0.0.0; _ga_FM37HSEP1G=GS1.1.1715873185.1.1.1715874400.0.0.0; _ga_XYSMSP82XG=GS1.1.1718040302.2.0.1718040302.60.0.0; _ga_Q3FWZYW7WL=GS1.2.1721848080.1.1.1721848116.0.0.0; _ga_SQ06B8V4SF=GS1.1.1721848079.1.1.1721848212.0.0.0; _ga_JK2Z55H1X9=GS1.1.1721933644.2.1.1721933654.0.0.0; _ga_9QB6VTY3DZ=GS1.1.1723477512.1.1.1723477994.0.0.0; _ga_1ZY55NML4M=GS1.1.1724680478.16.0.1724680478.0.0.0; _ga_0D6FYT0V7S=GS1.1.1725980278.1.0.1725980280.58.0.0; visid_incap_3015948=XG9NnTCJRgq69GRPbQm9RzQ2CGcAAAAAQUIPAAAAAADWKSlmrccb0xYOPwLBSXnk; _ga_0YC16CCD4X=GS1.1.1728594833.3.1.1728594993.0.0.0; _ga_0BZFNFE34F=GS1.1.1729717324.19.1.1729718613.0.0.0; _ga_J4VBH6CP6T=GS1.1.1729717324.4.1.1729718613.0.0.0; chaport-62603374034dcf77dca873ba=ed5e01ae-1d3c-42a2-b973-67f800debacc%2FtYHoNIB4OkmCPwN7AMQemw3RAZbvxP8f9PJ7UgzpOx; _ga_BFWLVL451M=GS1.1.1730226400.30.1.1730226463.0.0.0; _ga_366879341=GS1.1.1730327404.30.0.1730327614.0.0.0; __gsas=ID=385a45d92be5e3f8:T=1731945019:RT=1731945019:S=ALNI_MZjkAxZU9r5yYOCHHNw6N7vtaWd4Q; _ga_6D4R5G9TNJ=GS1.2.1731950411.8.1.1731950705.0.0.0; _ga_7J788E15ZL=GS1.1.1731949528.7.1.1731950961.60.0.0; _ga_SLX0CQ3HRM=GS1.1.1731952468.5.1.1731953159.60.0.0; _ga_P7HK6CTQ7T=GS1.1.1732034267.1.1.1732034279.0.0.0; _ga_2VJZCX56R2=GS1.1.1734478695.2.0.1734478695.0.0.0; _ga_SE2SMFDBDW=GS1.1.1736905115.5.1.1736905319.60.0.0; _ga_GFHX73E8E3=GS1.1.1738621542.14.0.1738621542.0.0.0; _ga_9STJHEHP96=GS1.1.1738796821.1.0.1738796827.54.0.0; _ga_7G2EGZ357T=GS1.1.1739120675.123.1.1739121402.0.0.0; _ga_R1LE8KQW1T=GS1.2.1739213998.13.1.1739214022.0.0.0; _ga=GA1.1.1886365173.1683662029; _ga_CBXPK98M4Q=GS1.1.1739391341.34.0.1739391341.0.0.0; cf_clearance=g__ybRA4Egg5XLYH1pkOHQv1NRpUbhuyIGvRheQCdmM-1741212575-1.2.1.1-FEAKrxrXtf0Wj4CSane40xEVxdQTaeBDlPh6NeEtYYg1koSBVnZb_qF_VxYIx2lVxON4L8AQm9IP05YvpKuiM2v57nhP0LLQfixxeOHAnMprATxOM2jwODoOIqMTA4bz5s.mBj1hu_RGj5ZeGlwd7Xb6bZOND9lxCkK_TmaqgxW.18qSKqjzEYCcUlqD4ys9_00hFSGLt9n_Dkshth7zQd8TrhQgaGdcXcJTW4ppinKNM8vNVpaNuwys.EV28oNa4c.7WJcJM1mSbovYm5caae8.o9Hy1uhkBXASMb1r62oslsxWRwr_0cPb1ftX33pYRixf2hml5gB4uyRvEFkByeItQVNFlvC_e6nZqWOXom01k.AYMtWWHVT84B61aUpV0v5WHnfhnL0jdyovrz.NYGAcgAsO6tV02DJ49DkJT70; _ga_KJKE71WK2Y=GS1.1.1741218879.7.0.1741218879.0.0.0; _ga_LJCC9XG5J9=GS1.1.1741218879.103.0.1741218879.0.0.0; ASP.NET_SessionId=3wvqcgo1imwfxxvjohaynbsn',
}

data = {   
   '__VIEWSTATE': viewstate,
   '__VIEWSTATEGENERATOR': viewstategenerator,
   '__EVENTTARGET': '',
   '__EVENTARGUMENT': '',
   '__VIEWSTATEENCRYPTED': '',
   '__EVENTVALIDATION': eventvalidation,
   'ctl00$MainContent$listLanguages': 'en',
   'ctl00$MainContent$txtSearchFirstName': 'Ryan',
   'ctl00$MainContent$txtSearchLastName': 'Little',
   'ctl00$MainContent$txtDOBMonth': '06',
   'ctl00$MainContent$txtDOBDay': '29',
   'ctl00$MainContent$txtDOBYear': '1985',
   'ctl00$MainContent$txtSearchZipCode': '20910',
   'ctl00$MainContent$txtSearchHouseNumber': '',
   'ctl00$MainContent$txtSearchMiddleInitial': '',
   'g-recaptcha-response': anti_captcha_response, #injecting the response into the form
   'ctl00$MainContent$btnSearch': 'Search',
}

api_response = requests.post('https://voterservices.elections.maryland.gov/VoterSearch', cookies=cookies, headers=headers, data=data)
display(HTML(api_response.text))
```


## **Inject and submit with JavaScript** `<a id="inject-and-submit-js">`{=html}`</a>`{=html}

But what do you do when there is no submit button? This is what Google calls an [invisible CAPTCHA](https://developers.google.com/recaptcha/docs/invisible). This implimentation requires us to use JavaScript to call a function that will submit the form. This is a line of defense webmasters use to make bypassing a CAPTCHA more difficult. However, it is still possible to bypass the CAPTCHA by injecting the solution into the website using JavaScript.

`Note: NICAR Hands-on` The only times I have encountered this method in the wild is when a CAPTCHA is used to test my robot\'s every `Nth` request. In the interest of time, we will not demonstrate this method today becuase it could be very cumbersome.

Let\'s take a look at Google\'s example for implimenting an invisible CAPTCHA.

``` html
<html>
  <head>
    <title>reCAPTCHA demo: Explicit render after an onload callback</title>
    <script>
        var onSubmit = function(token) {
          console.log('success!');
        };

        var onloadCallback = function() {
          grecaptcha.render('submit', {
            'sitekey' : 'your_site_key',
            'callback' : onSubmit
          });
        };
    </script>
  </head>
  <body>
    <form action="?" method="POST">
      <input id="submit" type="submit" value="Submit">
    </form>
    <script src="https://www.google.com/recaptcha/api.js?onload=onloadCallback&render=explicit"
        async defer>
    </script>
  </body>
</html>
```

You can see that this demo webpage has two functions that are used to render the CAPTCHA and to submit the solution. `grecaptcha` is the function that renders the CAPTCHA. It\'s the same function where we found the sitekey in the previous example.

The `onSubmit()` function is defined as the `callback function` in `grecaptcha`. That means we can need to call `onSubmit()` with the response from the ANTI-CAPTCHA API to bypass this captcha.

This time, we don\'t have to inject the solution into the HTML. We just need to execute the JavaScript function using Playwright with the solution as a parameter.

``` python
await page.evaluate(f'onSubmit({anti_captcha_response})')
```

There are more complicated examples of custom `callback function` that call for a complex set of functions to be executed. In these advanced cases, you may need to spend many hours deciphering a tangled web of JavaScript to find the right functions and parameters to call.



## **Links to other resources** `<a id="other-resources">`{=html}`</a>`{=html}

- [ANTI-CAPTCHA API documentation](https://anti-captcha.com/apidoc)
- [Google\'s reCAPTCHA v2 documentation](https://developers.google.com/recaptcha/docs/display)
- [Google\'s reCAPTCHA v3 documentation](https://developers.google.com/recaptcha/docs/v3)
- [Finding Undocumented APIs](https://inspectelement.org/apis)


## **Extra credit** `<a id="extra-credit">`{=html}`</a>`{=html}

If you are still having trouble finding a `sitekey` or a `callback function` in the HTMLm or inside of `<script></script>` tags, you will need to search in the console for the correct function. I would recommend startingn with searching `grecaptcha` and inspecting each dropdown object.

Sometimes you may find that you need to use a proxy to access a website. This is common when you are scraping a website that blocks your IP address. You can use a proxy to change your IP address and access the website. However, this can make it more difficult to solve CAPTCHAs. This is because the ANTI-CAPTCHA API may not be able to access the website if it is behind a proxy.

In this case, you will need to share the proxy with the ANTI-CAPTCHA API. This can be done by using the `set_proxy()` method. This method allows you to set the proxy that the ANTI-CAPTCHA API will use to access the website. You will need to obtain the proxy from a proxy provider and then use the `set_proxy()` method to share the proxy with the ANTI-CAPTCHA API.

I do not have much experience with this method. In the cases where I have used proxies to scrape website, my proxies have allowed me to employ strategies that avoid CAPTCHAs.

If you want to use this method for proxy and CAPTCHA, [ANTI-CAPTCHA documentation suggests making your own proxy or using Fast VPS](https://anti-captcha.com/apidoc/task-types/RecaptchaV2Task).

If you try to use a proxy with ANTI-CAPTCHA, you will need to add this code to your Anti-Captcha API requests.

``` python
solver.set_proxy_address("PROXY_ADDRESS")
solver.set_proxy_port(1234)
solver.set_proxy_login("proxylogin")
solver.set_proxy_password("proxypassword")
solver.set_user_agent("Mozilla/5.0")
solver.set_cookies("test=true")
```



## A really bad spreadsheet ##

- import by range
- use janitor to help with unwieldy names
- append a prefix for certain columns to name
- convert bad excel numbers to true numbers
- overwrite names if you need to

```{r message=FALSE}
data <- read_excel("UN_population.xlsx", sheet=1, range="A17:BM20613", col_types = "text") %>% 
  clean_names() %>% 
  mutate(across(12:65, parse_number)) %>% 
  rename_at(vars(12:23), ~ str_c("pop_", .)) %>% 
  rename_at(vars(24:30), ~ str_c("fert_",.)) %>% 
  rename_at(vars(31:63), ~ str_c("mort_",.)) %>% 
  rename_at(vars(64:65), ~ str_c("migr_", .))

  summary(data)
```


## Getting Help

- [Datasette on Discord](https://datasette.io/discord)
- The `#proj-datasette` channel in the [News Nerdery Slack](https://newsnerdery.org/)
- The [Github Discussions page on Datasette](https://github.com/simonw/datasette/discussions)



## How to run Datasette on a laptop

This will be a walkthrough of the Datasette open source project! This can be ran either on the conference-provided laptops, as long as you have a working Python environment (ie can `pip install`) packages.

### 1. Installing Datasette and `sqlite-utils`

On the command line, run:

```bash
pip install datasette sqlite-utils
```

To make sure it installed correctly:

```bash
datasette --version

sqlite-utils --version
```

For this workshop, we will use the [`datasette-upload-csvs`](https://github.com/simonw/datasette-upload-csvs) plugin, which can be installed with:

```bash
datasette install datasette-upload-csvs
```

### 2. Uploading a CSV

We will be working with the [San Fransisco Supplier Contracts](https://data.sfgov.org/City-Management-and-Ethics/Supplier-Contracts/cqi5-hm2d/about_data)
dataset. [Download the CSV here](https://gist.githubusercontent.com/asg017/144d059dbad77135a50ef3cd8590aad5/raw/sf_supplier_contracts.csv).

Now startup Datasette with an empty database like so:

```bash
datasette --create nicar24.db --root
```

<details>
<summary>Explanation of flags</summary>
<li>The <code>--create</code> flag will create the <code>nicar24.db</code> database for you. Without it, an <code>nicar24.db file not found</code> error would be raised</li>
<li>The <code>--root</code> flag will print out a signed URL, which grants a view higher privileges, like uploading CSVs.
</details>

Copy+paste the `http://127.0.0.1:8001/-/auth-token?token=...` URL into a web browser. You should see "root" in the top-right corner.

Navigate to the top-right corner menu and select "Upload CSVs". Drag+ drop the `sf_supplier_contracts.csv` file, and name the table `sf_supplier_contracts`.

After importing is complete, you'll have a new `sf_supplier_contracts` table to explore!

### 3. Building a search engine on NICAR24 Sessions

Now we'll focus on a 2nd way to import data, using the `sqlite-utils` CLI. Download the [`nicar-2024-schedule.csv`](https://schedules.ire.org/nicar-2024/nicar-2024-schedule.csv) file to your project folder.

To import the CSV to your SQLite database, we'll use `sqlite-utils` like so:

```bash
sqlite-utils insert nicar24.db sessions nicar-2024-schedule.csv  --csv
```

Start Datasette back up with:

```bash
datasette nicar24.db
```

<details>
<summary>No need for the <code>--create</code> or <code>--root</code> flags!</summary>
Since the <code>nicar24.db</code> database has been created, and we aren't uploading CSVs through the Datasette interface anymore, there's no need for those flags anymore.
</details>

Open `http://127.0.0.1:8001` and checkout the new `sessions` table.

If we want to add a search field to the session_description column, we could run:

```bash
sqlite-utils enable-fts nicar24.db sessions session_description
```


## Introduction to Datasette Cloud

Datasette Cloud is a collaborative space for your newsroom to share and analyze data

It's all built on open source Datasette components: if you want to build your own you are welcome to do so! It will probably cost you more time than having us run it for you though.

Each organization gets a "space" - a private space to collaborate on data.

### 1. Creating a space

Let's create a space now:

- Go to https://www.datasette.cloud/ and create an account - I recommend sign in with Google, that way you don't have to deal with Yet Another Password.
- Enter the invite code we distributed in the session...
- ... and create a space. Datasette Cloud is built on top of [Fly.io](https://fly.io/) which means we can run your space in many different locations around the world. The default in Virginia works just fine though.
- Spaces can take up to a minute to be created the first time.
  - Each space runs on a separate container, for security and to ensure the performance of one space doesn't impact any others
  - We'll start you with 2GB of volume space but this can be increased up to 500GB
  - Your data is continually backed up to a private S3 bucket using Litestream. You can download snapshots of the data directly.
  - Philosophically, avoiding lockin is very important to us. You should be able to extract your data at any time, in an open format


### 2. Importing some data

Once the space is up and running! Let's import some data. There are several ways to load data into Datasette Cloud:
- Uploading CSV files
- Importing CSV files from a URL
- Using the Datasette Cloud API
- ... and a new option using AI, which we'll try out shortly

Let's start with an import from a URL - we'll use the Global Power Plants example on the site.

- Click "The Global Power Point Database" to get started
- Once it has imported, rename that table:
  - Table actions -> Edit table schema -> Enter a new name -> Click "Rename"
- And we get our first visualization! Because it has latitude and longitude columns we can see it on a map.

### 2. Uploading CSV files

Next we'll upload some CSV data.
- Download a copy of the CSV of Baltimore Grocery Stores from https://data.baltimorecity.gov/datasets/baltimore::grocery-stores/explore
- Click "Upload CSV files" on the homepage and drag on the file
- This gets a map too!

Let's try a larger CSV
- Download the CSV of Baltimore City Employee Salaries from https://catalog.data.gov/dataset/baltimore-city-employee-salaries-b820d
- Upload the file
- Edit schema to change the type on `annualSalary` and `grossPay` to float. This means we can sort them.
- Let's start exploring! Find the highest paid employee.
- We can run a custom SQL query to see the department with the highest average:
  ```sql
  select agencyName, avg(grossPay) from Baltimore_City_Employee_Salaries
  group by agencyName
  order by avg(grossPay) desc
  ```

### 3. Running an enrichment

[Enrichments](https://enrichments.datasette.io/) are a powerful new Datasette feature ([introduced here](https://simonwillison.net/2023/Dec/1/datasette-enrichments/)) which allow you to run data modification operations against rows in a table. They are based around plugins, which means new enrichments can be added with [very little code](https://enrichments.datasette.io/en/stable/developing.html).

Now we'll use the regular expression enrichment to add a `hireYear` column:

- Table actions -> Enrich selected data -> Regular expressions
- Source column: `hireDate`
- Capture mode: "Store first match in single column"
- Regular expression: `(\d{4})-.*`
- Output column: `hireYear`


### 4. Building a search engine

We'll repeat the exercise from earlier with the NICAR schedule. This time, upload the `nicar-2024-schedule.csv` file to Datasette Cloud to create a table.

Now we can enable full-text search using the interface:

- Table actions -> Configure full-text-search
- Select `session_title` and `session_description`
- Click the blue button

### 5. Enriching with GPT-4

Let's write a haiku for every NICAR session!

- Table actions -> Enrich selected data -> AI analysis with OpenAI GPT
- Model: `gpt-3.5-turbo` - it's very fast, cheap and writes terrible but entertaining haikus
- Prompt: `{{ session_title }} {{ session_description }}`
- System prompt: `Turn this into a haiku`
- Output column: `haiku`
- Start the enrichment

You can use haiku column -> cog menu -> Show not-blank rows to see the haikus it has written so far.

### 6. Publishing a table

Everything in Datasette Cloud is private, but you can publish individual tables to make them available to anyone with the URL.

Try this on the `nicar-2024-schedule` table:

- Table actions -> Make table public
- Confirm that you want to change the privacy for the table
- The table is now available to anyone at `your-subdomain.datasette.site/data/nicar-2024-schedule`

You can tell if a table is public due to the lack of a padlock icon (we'll be making this more clear soon).

Published tables include the search and filtering interface, and support both `.json` API access and `.csv` exports.

### 7. Extracting data into a table with AI

**[datasette-extract](https://github.com/datasette/datasette-extract)** is a brand new (built just in time for this conference) Datasette plugin that lets you enter unstructured data into a Datasette table using the OpenAI GPT-4 model.

Let's use it to load up a table with data copied from a website.

https://bachddsoc.org/calendar/ is a calendar of upcoming events at the [Bach Dancing & Dynamite Society](https://en.wikipedia.org/wiki/Bach_Dancing_%26_Dynamite_Society) jazz venue in Half Moon Bay (I just created their Wikipedia page!)

We're going to start an events calendar for the city, without any tedious data entry.

Start on your `/data` database  is page. 
- Database actions -> Create table with extracted data

Visit https://bachddsoc.org/calendar/ and copy and paste a chunk of text from the page. Don't worry about the format.

Configure the table as follows:
- Table name: `events`
- Columns:
  - `event_title`
  - `event_date` - Hint: `YYYY-MM-DD`
  - `venue_name`
  - `venue_address`
  - `start_time` - Hint: `HH:MM 24hr`
  - `description`

Now scroll down and click "Extract".

Watch as the extraction process pulls the events out of the unstructured text and writes them to your new `/data/events` table!

### 8. Extracting structured data from an image

I took [a photograph of a flier](https://static.simonwillison.net/static/2024/comedy-luau.jpeg) for an event in Half Moon Bay a while ago. Let's import that event as well.

From the new `events` table click:
- Table actions -> Extract data into this table

Drag the photograph onto the textarea, or select it with the file upload field.

Now wait for a few seconds... and if all goes well the event will be added to the table as well.



## Using the Datasette Cloud (and Datasette) API

Datasette has had a powerful read-only JSON API since it first launched.

One of the signature features of the forthcoming [Datasette 1.0](https://docs.datasette.io/en/latest/changelog.html) is the new [JSON write API](https://docs.datasette.io/en/latest/json_api.html#the-json-write-api), for writing data directly to a Datasette instance.

Let's use the API to import a JSON file directly into Datasette Cloud.

### 1. Create an API key

Use the burger menu at the top right of Datasette Cloud and select "Create API token".

This form allows you to create finely grained API keys. You can create a long-lived key that can do anything your user can do, or you can set an expiration time on it. You can also limit an API key to specific operations, either against everything or against specific databases or tables.

For the moment let's keep things simple: create an API key with the default settings, but set it to expire in an hour.

You'll only see the API key once, so copy and paste it out to your notes.

### 2. Try it out with `curl`

Let's try our new API key. Run the following command in the terminal:
```bash
export DS_KEY='dsatok_...'
```
Now let's make an API call:
```bash
curl 'https://your-subdomain.datasette.cloud/data.json' \
  -H "Authorization: Bearer $DS_KEY"
```
This returns details about every table in your database.

A more interesting thing to do is tag on a SQL query:
```bash
curl 'https://your-subdomain.datasette.cloud/data.json?sql=select+*+from+events' \
  -H "Authorization: Bearer $DS_KEY"
```
This should return the results of that query to your terminal.

### 3. Install and use dclient

[dclient](https://dclient.datasette.io) is a command-line tool for interacting with the Datasette API in a more convenient way. Install it like this:

```bash
pip install dclient
```
To tell it about your key, run `dclient auth set`:

```bash
dclient auth add https://your-subdomain.datasette.cloud/
# Token: paste your token here
```

Now any calls you make to that URL will automatically include the token:
```bash
dclient query https://your-subdomain.datasette.cloud/data 'select * from events'
```
One last convenience: create an alias for that URL like this:
```bash
dclient alias add dc https://your-subdomain.datasette.cloud/data
```
And now you can do this:
```bash
dclient query dc 'select * from events'
```

### 4. Upload JSON using dclient

With all of the above setup, let's import the NICAR JSON schedule.

Grab the file from https://schedules.ire.org/nicar-2024/nicar-2024-schedule.json

Now run the following:
```bash
dclient insert dc nicar_schedule nicar-2024-schedule.json \
  --create --alter --pk session_id
```
This should create a table called `nicar_schedule` in your instance with the `session_id` column set as the primary key.

The `--create` option causes the table to be created if it does not exits yet. The `--alter` option is needed because this JSON file has later objects that have keys that were not present earlier on, so the table needs to be altered to fit them.


## Advanced API usage

Here are some more advanced uses of the Datasette Cloud API:

- https://demos.datasette.site/data/documents is a public searchable database of documents added to the Federal Register. It is populated by [this scheduled GitHub Action](https://github.com/simonw/federal-register-to-datasette/blob/6e46f167de6ff312ef5338121cf2879483aba33b/.github/workflows/main.yml), described in detail in [Getting started with the Datasette Cloud API](https://www.datasette.cloud/blog/2023/datasette-cloud-api/).
- https://simon.datasette.site/data/feed is a feed of content from my blog. It's written to by [this Val Town](https://www.val.town/v/simonw/feedToDatasetteCloud) scheduled JavaScript task, described in [Running a scheduled function on Val Town to import Atom feeds into Datasette Cloud](https://til.simonwillison.net/valtown/scheduled).



## Final demos

- `datasette-comments`
- ChatGPT talking to Datasette - https://gist.github.com/simonw/d6425fd997e61cf517aa196fe988638c
- `datasette-scribe`


## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, religion, or sexual identity
and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.



## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
* Focusing on what is best not just for us as individuals, but for the
  overall community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or
  advances of any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email
  address, without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting


## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate, threatening, offensive,
or harmful.

Community leaders have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, and will communicate reasons for moderation
decisions when appropriate.



## Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official e-mail address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.


## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at
b@palewi.re.
All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the
reporter of any incident.



## Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines in determining
the consequences for any action they deem in violation of this Code of Conduct:

### 1. Correction

**Community Impact**: Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.

**Consequence**: A private, written warning from community leaders, providing
clarity around the nature of the violation and an explanation of why the
behavior was inappropriate. A public apology may be requested.

### 2. Warning

**Community Impact**: A violation through a single incident or series
of actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or
permanent ban.

### 3. Temporary Ban

**Community Impact**: A serious violation of community standards, including
sustained inappropriate behavior.

**Consequence**: A temporary ban from any sort of interaction or public
communication with the community for a specified period of time. No public or
private interaction with the people involved, including unsolicited interaction
with those enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

### 4. Permanent Ban

**Community Impact**: Demonstrating a pattern of violation of community
standards, including sustained inappropriate behavior,  harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within
the community.


## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.0, available at
https://www.contributor-covenant.org/version/2/0/code_of_conduct.html.

Community Impact Guidelines were inspired by [Mozilla's code of conduct
enforcement ladder](https://github.com/mozilla/diversity).

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see the FAQ at
https://www.contributor-covenant.org/faq. Translations are available at
https://www.contributor-covenant.org/translations.



## Installation

Fork the repository and clone it:

```bash
gh repo clone your-name/first-python-notebook
```

Change into the project directory:

```bash
cd first-python-notebook
```

Install the dependencies using pipenv:

```bash
pipenv install
```


## Contributing

To start a test server that previews the site, use the following command:

```bash
make serve
```

Once it starts, visit [localhost:8000](http://localhost:8000) in your browser. Edits made in the `docs/` folder will appear immediately. Commit your changes to a branch and then submit a pull request to the source repository.



## Reporting a Vulnerability

If you have found a vulnerability in this project, please contact maintainer Ben Welsh at [b@palewi.re](mailto:b@palewi.re)


## A command-line interface

Whether you know about it or not, there should be a way to open a window and directly issue commands to your operating system. Different operating systems give this tool slightly different names, but they all have some form of it.

On Windows this is called the “command prompt.” On MacOS it is called the “terminal.” Other people will call this the “command line.”

On Windows, we recommend you install the [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10) and select the Ubuntu distribution from the Windows Store. This will give you access to a generic open-source terminal without all the complications and quirks introduced by Windows. On MacOS, the standard terminal app will work fine.



## Python 3.6 or higher

[Python](https://www.python.org/) is a free and open-source computer programming language. It's one of the most popular in the world and praised by its supporters as clear and easy to read.

That makes it ideal for beginners and is partly why it's been adopted by professionals in many fields, ranging from engineering and web development to journalism and music.

You can check if Python is already installed on your computer by visiting your command line and entering the following:

```bash
python --version
```

You should see something like this after you hit enter:

```bash
Python 3.6.10
```

If not, you'll need to install Python on your system.

If you see a number starting with 2, like say ...

```bash
Python 2.7.12
```

...then you have an outdated version of Python and will need to upgrade to a version starting with a 3. You can probably complete the class without doing so, but the maintainers of Python are gradually phasing out version 2 and officially recommend you upgrade.

Instructions for both new installations and upgrades can be found [here](https://docs.python-guide.org/starting/installation/).


## The `pipenv` environment manager

Our notebook depends on a set of Python tools that we'll need to install before we can run the code. They are the [JupyterLab](https://jupyter.org/) computational notebook, the [requests](https://docs.python-requests.org/en/latest/) library for downloading webpages and [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/), a handy utility for parsing data out of HTML. 

By default, Python's third-party packages are all installed in a shared "global" folder somewhere in the depths of your computer. By default, every Python project on your computer draws from this same set of installed programs.

This approach is fine for your first experiments with Python, but it quickly falls apart when you start to get serious about coding.

For instance, say you develop a web application today with [Flask](https://palletsprojects.com/p/flask/) version 1.1. What if, a year from now, you want to start a new project and use a newer version of Flask? Your old app is still live and requires occasional patches, but you don't have time to re-write all of your old code to make it compatible with the latest version of Flask.

Open-source projects are changing every day and such conflicts are common, especially when you factor in the sub-dependencies of your project’s direct dependencies, as well as the sub-dependencies of those sub-dependencies.

Programmers solve this problem by creating a [virtual environment](https://docs.python.org/3/tutorial/venv.html) for each project that isolates them into discrete, independent containers that do not rely on code in the global environment.

Strictly speaking, working within a virtual environment is not required. At first, it might even feel like a hassle. But in the long run, you will be glad you did it. And you don’t have to take my word for it, you can read discussions on [StackOverflow](https://conda.io/docs/index.html) and [Reddit](https://www.reddit.com/r/Python/comments/2qq1d9/should_i_always_use_virtualenv/).

Good thing [pipenv](https://pipenv.kennethreitz.org/en/latest/) can do this for us.

Pipenv and its prerequisites are installed via your computer's command-line interface. You can verify it’s there by typing the following into your terminal:

```bash
pipenv --version
```

If you have it installed, you should see the terminal respond with the version on your machine.

```bash
pipenv, version 2018.11.26
```

If you get an error, you will need to install it.

If you are on a Mac, Pipenv’s maintainers [recommend](https://pipenv.kennethreitz.org/en/latest/install/#homebrew-installation-of-pipenv) installing via [Homebrew](https://brew.sh/):

```bash
brew install pipenv
```

If you are on Windows and using the [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10), you can install [Linuxbrew](https://docs.brew.sh/Homebrew-on-Linux) and use it to install Pipenv.

If neither option makes sense for you, Pipenv's [docs](https://pipenv.kennethreitz.org/en/latest/install/#pragmatic-installation-of-pipenv) recommend a [user install](https://pip.pypa.io/en/stable/user_guide/#user-installs) via pip:

```bash
pip install --user pipenv
```

Whatever installation route you choose, you can confirm your success by testing for its version again:

```bash
pipenv --version
```

If you see that version number now, you know you're okay.

### Create a code directory

Now let’s create a common folder where all of your projects will be stored starting with this one. This is also where our virtualenv will be configured.

Depending on your operating system and personal preferences, open up a terminal program. It will start you off in your computer’s home directory, just like your file explorer. Enter the [`ls`](https://en.wikipedia.org/wiki/Ls) command and press enter to see all of the folders there now.

```bash
ls
```

Now let’s check where we are in our computer's file system. For this we'll use a command called [pwd](https://en.wikipedia.org/wiki/Pwd), which stands for present working directory. The output is the full path of your location in the file system, something like `/Users/palewire/`.

```bash
pwd
```


Use the [mkdir](https://en.wikipedia.org/wiki/Mkdir) command to create a new directory for your code. In the same style as the Desktop, Documents and Downloads folders included by most operating system, we will name this folder Code.

```bash
mkdir Code
```

To verify that worked, you can open in your file explorer and navigate to your home folder. Now jump into the Code directory, which is the same as double clicking on a folder to enter it in your filesystem navigator.

```bash
cd Code
```

### Create a project directory

Now let's make a folder for your work in this class.

```bash
mkdir first-python-notebook
```

Then, jump into that project directory:

```bash
cd first-python-notebook
```

This is where you'll store a local copy of all the code and files you create for this project.

It isn't necessary to change directories one level at a time. You can also specify the full path of directory you want to change into. For instance, from your home directory you could run the following to move directly into your project directory.

```bash
cd Code/first-python-notebook
```

### Install your first package

Now let's install a simple Python package to see `pipenv` in action. We’ll choose [yolk3k](https://pypi.org/project/yolk3k/), a simple command-line tool that can list all your installed python packages.

We can add it to our project’s private virtual environment by typing its name after Pipenv's install command.

```bash
pipenv install yolk3k
```

When you invoke Pipenv's `install` command, it checks for an existing virtual environment connected to your project’s directory. Finding none, it creates one, then installs your packages into it.

As a result, two files are added to your project directory: `Pipfile` and `Pipfile.lock`. Open these files in a text editor and you'll see how they describe your project’s Python requirements.

In the `Pipfile`, you'll see the name and exact version of any package we directed Pipenv to install. We didn't specify an exact version, so you'll see:

```bash
[packages]
yolk3k = "*"
```

`Pipfile.lock` has a more complicated, nested structure that specifies the exact version of your project's direct dependencies along with all their sub-dependencies.

Now that yolk is installed, we can execute it inside our environment using the `pipenv run` command. Let's use it to see yolk3k’s method for listing all of our currently installed tools.

```bash
pipenv run yolk -l
```

You should see the computer spit out everything you have installed. You’ll notice that yolk3k is on the list.



## Python packages

Next we will install the extra Python packages used during the tutorial.

We will return to pipenv and use it to install JupyterLab, the web-based interactive development environment for Jupyter notebooks, code and data.

```bash
pipenv install jupyterlab
```

We'll install pandas the same way:

```python
pipenv install pandas
```

Install altair too.

```python
pipenv install altair
```

````{note}
You can install more than one package at once. For instance, all three of the packages above could be added like so:

```bash
pipenv install jupyterlab pandas altair
```
````


## Your first notebook

Now we can use pipenv's run command to start JupyterLab from your terminal.

```bash
pipenv run jupyter lab
```

That will open up a new tab in your default web browser that looks something like this:

```{image} /_static/jupyterlabdesktop.png
```

Click the "Python 3" button in the middle panel and create a new Python 3 notebook. You should now be able to pick up in [chapter two](../notebook.md) and start work from there.



## Make a basic bar chart

The first thing we need to do is import Altair. In the tradition of pandas, we'll import it with the alias `alt` to reduce how much we need to type later on. 

```{code-cell}
:tags: [hide-cell]

import warnings
warnings.simplefilter("ignore")
import pandas as pd
accident_list = pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/main/docs/src/_static/ntsb-accidents.csv")
accident_list["latimes_make_and_model"] = accident_list["latimes_make_and_model"].str.upper()
accident_counts = accident_list.groupby(["latimes_make", "latimes_make_and_model"]).size().rename("accidents").reset_index()
survey = pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/main/docs/src/_static/faa-survey.csv")
survey["latimes_make_and_model"] = survey["latimes_make_and_model"].str.upper()
merged_list = pd.merge(accident_counts, survey, on="latimes_make_and_model")
merged_list["per_hour"] = merged_list.accidents / merged_list.total_hours
merged_list["per_100k_hours"] = (merged_list.accidents / merged_list.total_hours) * 100_000
```

```{code-cell}
import altair as alt
```

```{note}
If the import triggers an error that says your notebook doesn't have Altair, you can install it by running `%pip install altair` in a cell. This will download and install the library using the [pip](https://pip.pypa.io/en/stable/) package manager and Jupyter's built-in [magic command](https://ipython.readthedocs.io/en/stable/interactive/magics.html).
```

In a typical analysis, you'd import all of your libraries in one cell at the top of the file. That way, if you need to install or make changes to the packages a notebook uses, you know where to find them and you won't hit errors importing a package midway through running a file.

With Altair imported, we can now feed it our DataFrame to make a simple bar chart. Let's take a look at the basic building block of an Altair chart: the `Chart` object. We'll tell it that we want to create a chart from `merged_list` by passing the DataFrame in, like so:

```{code-cell}
alt.Chart(merged_list)
```

OK! We got an error, but don't panic. The error says that Altair needs a "mark" — that is to say, it needs to know not only what data we want to visualize, but also _how_ to represent that data visually. There are lots of different marks that Altair can use (you can [check them all out here](https://altair-viz.github.io/user_guide/marks.html)). But let's try out the most versatile mark in our visualization toolbox: the bar.

```{code-cell}
alt.Chart(merged_list).mark_bar()
```

That's an improvement, but we've got a new error: Altair doesn't know which columns of our DataFrame to look at! At a minimum, we also need to define the column to use for the x- and y-axes. We can do that by chaining in the `encode` method.

```{code-cell}
alt.Chart(merged_list).mark_bar().encode(
    x="latimes_make_and_model",
    y="per_100k_hours"
)
```

That’s more like it!

Here's an idea — maybe we do horizontal bars instead of vertical. How would you rewrite this chart code to reverse those bars?

```{code-cell}
alt.Chart(merged_list).mark_bar().encode(
    x="per_100k_hours",
    y="latimes_make_and_model"
)
```

This chart is an okay start, but it's sorted alphabetically by y-axis value, which is pretty sloppy and hard to visually parse. Let's fix that.

We want to sort the y-axis values by their corresponding x values. We know how to do that in Pandas, but Altair has its own opinions about how to sort a DataFrame, so it will override any sort order on the DataFrame we pass in.

Until now, we've been using the shorthand syntax to create our axes, but to add more customization to our chart we'll have to switch to the longform way of defining the y-axis.

To do that, we'll use a syntax like this: `alt.Y(column_name)`. Instead of passing a string to `y` and letting Altair do the rest, this lets us create a y-axis object and then give it additional instructions.

```{code-cell}
alt.Chart(merged_list).mark_bar().encode(
    x="per_100k_hours",
    y=alt.Y("latimes_make_and_model")
)
```
This chart should look identical to our previous attempt when we created the y-axis the simpler way, but it opens up new options! Now we can instruct Altair to sort the y-axis by the x-axis values.

```{code-cell}
alt.Chart(merged_list).mark_bar().encode(
    x="per_100k_hours",
    y=alt.Y("latimes_make_and_model").sort("x")
)
```

That's looking a lot neater! By default, the sort order will be small to large. Visually, if we want to feature the highest accident rates, it probably makes sense to reverse that order. We can do that by adding a minus before the axis name.

```{code-cell}
alt.Chart(merged_list).mark_bar().encode(
    x="per_100k_hours",
    y=alt.Y("latimes_make_and_model").sort("-x")
)
```

And we can't have a chart without context. Let's throw in a title for good measure.

```{code-cell}
alt.Chart(merged_list).mark_bar().encode(
    x="per_100k_hours",
    y=alt.Y("latimes_make_and_model").sort("-x")
).properties(
    title="Helicopter accident rates"
)
```

Yay, we made a chart!


## Other marks

What if we wanted to switch it up and show this data in a slightly different form? For example, in the [Los Angeles Times story](https://www.latimes.com/projects/la-me-robinson-helicopters/), the fatal accident rate is shown as a scaled circle.

We can try that out with just a few small tweaks, using Altair's `mark_circle` option. We'll keep the `y` encoding, since we still want to split out our chart by make and model. Instead of an `x` encoding, though, we'll pass in a `size` encoding, which will pin the radius of each circle to that rate calculation. And hey, while we're at it, let's throw in an interactive tooltip that displays the accident rate when users hover over a mark.

```{code-cell}
alt.Chart(merged_list).mark_circle().encode(
    size="per_100k_hours",
    y="latimes_make_and_model",
    tooltip="per_100k_hours"
)
```
A nice little change from all the bar charts! But once again, the default sorting alphabetical by name. Instead, it would be really nice to sort this by rate, as we did with the bar chart. How would we go about that?

```{code-cell}
alt.Chart(merged_list).mark_circle().encode(
    size="per_100k_hours",
    y=alt.Y("latimes_make_and_model").sort("-size"),
    tooltip="per_100k_hours"
)
```



## `datetime` data

One thing you'll almost certainly find yourself grappling with time and time again is date (and time) fields, so let's talk about how to handle them.

Let’s see if we can do that with our original DataFrame, the `accident_list` that contains one record for every helicopter accident. We can remind ourselves what it contains with the `info` command.

```{code-cell}
accident_list.info()
```

When you import a CSV file with `read_csv` it will take a guess at column types — for example, `integer`, `float`, `boolean`, `datetime` or `string` — but it will default to a generic `object` type, which will generally behave like a string, or text, field. You can see the data types that pandas assigned to the accident list on the right hand side of the `info` table.

Take a look above and you'll see that pandas is treating the `date` column as an object. That means we can't chart it using Python's system for working with dates.

But we can fix that. The [`to_datetime`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html) method included with `pandas` can handle the conversion. Here's how to reassign the `date` column after making the change.

```{code-cell}
accident_list["date"] = pd.to_datetime(accident_list["date"])
```

This redefines each object in that column as a date. If your dates are in an unusual or ambiguous format, you may have to [pass in a specific formatter](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html), but in this case pandas should be able to guess correctly.

Run `info` again and you'll notice a change. The data type for `date` has changed.

```{code-cell}
accident_list.info()
```

Now that we've got that out of the way, let’s see if we can chart with it, tracking fatalities over time.

```{code-cell}
alt.Chart(accident_list).mark_bar().encode(
  x="date",
  y="total_fatalities"
)
```

This is great on the x-axis, but it's not quite accurate on the y. To make sure this chart is accurate, we'll need to aggregate the y-axis in some way.


## Aggregate with Altair

We could back out and create a new dataset grouped by date, but Altair actually lets us do some of that grouping on the fly. We want to add everything that happens on the same date, so we'll pop in a `sum` function on our y column.

```{code-cell}
alt.Chart(accident_list).mark_bar().encode(
  x="date",
  y="sum(total_fatalities)"
)
```

This is getting there. But sometimes plotting on a day-by-day basis isn't all that useful — especially over a long period of time like we have here.

Again, we could back out and create a new DataFrame grouping by month, but we don't have to — in addition to standard operations (sum, mean, median, etc.), Altair gives us some handy datetime aggregation options. You can find a list of options in the [library documentation](https://altair-viz.github.io/user_guide/transform/timeunit.html).

```{code-cell}
alt.Chart(accident_list).mark_bar().encode(
  x="yearmonth(date)",
  y="sum(total_fatalities)",
)
```

This is great for showing the pattern of fatalities over time, but it doesn't give us additional information that might be useful. For example, we almost certainly want to investigate the trend for each manufacturer.

What can do is facet, which will create separate charts, one for each helicopter maker.

```{code-cell}
alt.Chart(accident_list).mark_bar().encode(
  x="yearmonth(date)",
  y="sum(total_fatalities)",
  facet="latimes_make"
)
```



## Add a `color`

What important fact in the data is this chart *not* showing? There are _two_ Robinson models in the ranking. It might be nice to emphasize them.

We have that `latimes_make` column in our original DataFrame, but it got lost when we created our ranking because we didn't include it in our `groupby` command. We can fix that by scrolling back up our notebook and adding it to the command. You will need to replace what's there with a list containing both columns we want to keep.

Make note that because we're listing more than one column in the `groupby` call now, we'll need to surround those column names in a pair of square brackets like so:

```{code-cell}
accident_counts = accident_list.groupby(["latimes_make", "latimes_make_and_model"]).size().rename("accidents").reset_index()
```

Rerun __all__ of the cells after that one to update everything you're working with and add the new column.

```{note}
Remember: If we change a variable, future cells that use that variable won't change unless we run them again. When you go back and make these changes, make sure to run all of the cells that come after them as well, otherwise you may not get the results you're expecting.

This is one reason that it can be good to clear cell outputs and rerun your analysis every so often. If you've been going back and forth editing cells and tweaking your analysis, you may have saved variables in memory that are no longer accurate. One way to do that is to clear your "kernel" and rerun the whole notebook to make sure everything still runs as you expect it to (In the Jupyter menu, `Kernel` > `Restart Kernel and Clear All Outputs`, or `Restart Kernel and Run Up to Selected Cell`).
```

Now, when you inspect your `merged_list` variable, you should see the `latimes_make` column included.

```{code-cell}
merged_list.info()
```

Let's put that to use with an Altair option that we haven't toyed with yet: `color`.

```{code-cell}
alt.Chart(merged_list).mark_bar().encode(
    x="per_100k_hours",
    y=alt.Y("latimes_make_and_model").sort("-x"),
    color="latimes_make"
).properties(
    title="Helicopter accident rates"
)
```

Hey now! That wasn't too hard, was it? But now there are too many colors. It would be easier to read this chart and highlight information we want readers to notice if we used one color for the Robinson bars and made everything else a different color.

The simplest way to do this is to hand Altair a DataFrame with a column that has the values we want to color-code on. We already have the `latimes_make` columns, but in this case we don't want that many values; we just want that column to contain one value for the Robinson rows, and another value for all the non-Robinson rows. It doesn't really matter what those two values are! 

How might we go about creating that column? (Hint: We can adapt the technique we learned about in the Filters chapter!)

One way to do this is to create a test for rows with an `latimes_make` value equal to "ROBINSON", like so:

```{code-cell}
merged_list["latimes_make"] == "ROBINSON"
```
That will give us a true/false list. In the Filters chapter, we used that list to filter the DataFrame to only rows that matched this test. But we can also simply define a new column and save that list to it. Let's call the new column `robinson`.

```{code-cell}
merged_list["robinson"] = merged_list["latimes_make"] == "ROBINSON"
```
If you take a look at our `merged_list` DataFrame, you should now see that new column.

```{code-cell}
merged_list.head()
```
Now, we can alter our chart to use that new column.

```{code-cell}
alt.Chart(merged_list).mark_bar().encode(
    x="per_100k_hours",
    y=alt.Y("latimes_make_and_model").sort("-x"),
    color="robinson"
).properties(
    title="Helicopter accident rates"
)
```

_Bonus: This is fine for exploratory use, but we don't really need that legend, since it's adding a highlight to information that's already included in the names of the helicopters. To hide it, we can use that more advanced syntax and instruct Altair to skip creating a legend._

```{code-cell}
alt.Chart(merged_list).mark_bar().encode(
    x="per_100k_hours",
    y=alt.Y("latimes_make_and_model").sort("-x"),
    color=alt.Color("robinson", legend=None)
).properties(
    title="Helicopter accident rates"
)
```


## Polishing your chart

These charts give us plenty of areas where we might want to dig in and ask more questions, but none are polished enough to pop into a news story quite yet. But there *are* lots of additional labeling, formatting and design options that you can dig into in the [Altair docs](https://altair-viz.github.io/index.html) — you can even create Altair themes to specify default color schemes and fonts.

But you may not want to do all that tweaking in Altair, especially if you're just working on a one-off graphic. If you wanted to hand this chart off to a graphics department, all you'd have to do is head to the top right corner of your chart.

See those three dots? Click on that, and you'll see lots of options. Downloading the file as an SVG will let anyone with graphics software like Adobe Illustrator take this file and tweak the design.

To get the raw data out, you'll need to learn one last pandas trick. It's covered in our final chapter.



## Count a column's values

In this case, the column is filled with characters. So we don’t want to calculate statistics like the median and average, as we did before.

There’s another built-in pandas tool that will total up the frequency of values in a column. The method is called [`value_counts`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.value_counts.html) and it’s just as easy to use as `sum`, `min` or `max`. All you need to do it is add a period after the column name and chain it on the tail end of your cell.

```{code-cell}
:tags: [show-input]
accident_list["latimes_make_and_model"].value_counts()
```

Congratulations, you've made your first finding. With that little line of code, you've calculated an important fact: During the period being studied, the Robinson R44 had more fatal accidents than any other helicopter.

But wait. Before we congratulate ourselves, let's take a closer look at the data. Our value counts operation has turned up an imperfection that was buried in the data. Can you see it?


## Cleaning data columns

On closer inspection, we can see that Bell 206 helicopter is listed two different ways, as `BELL 206` and `bell 206`. The variation in capitalization is causing pandas to treat them as two distinct values.

This is a common problem and a simple example of how "dirty" data can trip up a computer program. The solution is to clean up the column prior to analysis.

In this case, we can use the `str` method, which is short for string. In many computer programming languages, string is the technical term used to refer to text. Thus, the pandas `str` method is designed to manipulate a column of text. It can change the casing of text, find and replace different patterns and conduct many other useful operations.

You can access it by chaining `.str` and your desired manipulation method after the column name. In this case, we want to use the `upper` method, which will convert all of the text in the column to uppercase.

```{code-cell}
:tags: [show-input]

accident_list["latimes_make_and_model"].str.upper()
```

While it's not useful in this case, we can try out the companion `lower` method to see it do the opposite.

```{code-cell}
:tags: [show-input]

accident_list["latimes_make_and_model"].str.lower()
```

```{note}
You can find a full list of `str` methods, along with useful examples, in the [pandas documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html#string-methods).
```

To correct the bug, we need to assign the result of the `upper` method to our existing column and overwrite what's there. We can do that with the `=` operator.

```{code-cell}
:tags: [show-input]

accident_list["latimes_make_and_model"] = accident_list["latimes_make_and_model"].str.upper()
```

Now we can run `value_counts` again to see if the problem has been fixed.

```{code-cell}
:tags: [show-input]

accident_list["latimes_make_and_model"].value_counts()
```

Much better! We have a clean list of helicopter models and their frequencies.

In the real world, you will almost always need to clean your data before you can analyze it, though the challenges will typically be more complex than this one. Pandas offers a wide range of tools to help you clean your data, but the basic process is always the same: Identify the problem, fix it, and then check your work. The `value_counts` method is one of the most useful tools in this process.

Before we move on to the next chapter, here's a challenge. See if you can answer a few more questions a journalist might ask about our dataset. All of the questions below can be answered using only tricks we've covered thus far.

1. What was the total number of fatalities?
2. Which helicopter maker had the most fatal accidents?
3. Which year had the most fatal helicopter accidents?
4. How many fatal helicopter accidents occurred in Texas?
5. How many different helicopter makers are in the dataset?

Once you’ve written code that generates the answers, you’re ready to move on to the next chapter.



## The `read_csv` method


    <iframe class="responsive-iframe" src="https://www.youtube.com/embed/XWqRkIx-BzQ?si=tXxS-F_KdzOIbp1F" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


Scroll down to the first open cell. There we will import the first CSV file using the [`read_csv`](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html) function included with pandas.

```{code-cell}
:tags: [show-input]
pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/main/docs/src/_static/ntsb-accidents.csv")
```

```{warning}
You need the exact URL shared in the example to access the file. While you could laboriously type it out, feel free to copy and paste it into your notebook.
```

After you run the cell, you should see a big table output to your notebook. It is a “DataFrame” where pandas has structured the CSV data into rows and columns, just like Excel or other spreadsheet software might. Take a moment to look at the columns and rows in the output, which contain the data we'll use in our analysis.

```{note}
On the left-hand side, you'll see a bolded number incrementing upward from zero that's not present in our source data file. This is what pandas calls the [index](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Index.html). It is a separate column created automatically and used to identify each row. The index is not considered part of the data, but it is used to reference the rows of the DataFrame or Series in advanced operations that are beyond the scope of this class.
```

A major advantage of Jupyter over spreadsheets is that rather than manipulating the data through a haphazard series of clicks and keypunches, we will be gradually grinding it down using a computer programming script that is transparent and reproducible.

To do more with your DataFrame, we need to store it so it can be reused in subsequent cells. We can do this by saving it in a variable, just as we did in with our `number` in Chapter 2.

Go back to your latest cell and change it to this. Rerun it.

```{code-cell}
accident_list = pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/main/docs/src/_static/ntsb-accidents.csv")
```

You shouldn't see anything. That's a good thing. It means our DataFrame has been saved under the name `accident_list`, which we can now begin interacting with in the following cells.

We can do this by calling ["methods"](https://en.wikipedia.org/wiki/Method_(computer_programming)) that pandas makes available to all DataFrames. You may not have known it at the time, but `read_csv` is one of these methods. There are dozens more that can do all sorts of interesting things. Let’s start with some easy ones that analysts use all the time.


## The `head` method

To preview the first few rows of the dataset, try the [`head`](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.head.html) method. Add a new cell, type this in and hit the play button again.

```{code-cell}
:tags: [show-input]
accident_list.head()
```

It serves up the first five rows by default. If you want a different number, submit it as an input.

```{code-cell}
:tags: [show-input]
accident_list.head(1)
```



## The `info` method

To get a look at all of the columns and what type of data they store, add another cell and try the [info](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.info.html) method. Look carefully at the results and you'll see we have 163 fatal accidents to review.

```{code-cell}
:tags: [show-input]
accident_list.info()
```

Now that you've got some data imported, we’re ready to begin our analysis.


## Reset a DataFrame

You may notice that even though the result of a `groupby` has two columns, pandas does not return a clean-looking table the same way other operations like `head` do. In most instances, you can convert ugly tables like the ones above into a pretty DataFrame by tacking the `reset_index` method onto the end of your code.

```{code-cell}
:tags: [show-input]
accident_list.groupby("latimes_make_and_model").size().reset_index()
```

Why doesn't `groupby` return a DataFrame? Why does `reset_index` have such a weird name?

Like so much in computer programming, the answer is simply, “because the people who created the library said so.” It’s important to learn that all open-source programming tools are made by humans, and humans have their quirks. Over time you’ll see pandas has more than a few.

As a beginner, you should just accept the oddities and keep moving. As you get more advanced, if there’s something about the system you think could be improved, you should consider [contributing](https://pandas.pydata.org/pandas-docs/stable/development/contributing.html) to the Python code that operates the library.

You can clean up the `0` column name assigned by pandas with the `rename` method.

```{code-cell}
:tags: [show-input]
accident_list.groupby("latimes_make_and_model").size().rename("accidents").reset_index()
```

Now save that as a variable.

```{code-cell}
:tags: [show-input]
accident_counts = accident_list.groupby("latimes_make_and_model").size().rename("accidents").reset_index()
```

That will return a DataFrame with the accident totals we need to calculate a rate. Inspect it with `head`.

```{code-cell}
:tags: [show-input]
accident_counts.head()
```

Now we‘ve got a ranking we can work with.



## What you will learn

* Just enough of the [Python](https://www.python.org/) computer-programming language to read, filter, join, group, aggregate and rank structured data with [pandas](http://pandas.pydata.org/), a popular tool for statistical analysis

* How to record, remix and republish your work using [Project Jupyter](http://jupyter.org/), the emerging standard for generating reproducible research

* How to explore data using using [Altair](https://altair-viz.github.io/), a Python package that offers a simple, structured grammar for generating charts.


## Who can take it

This course is free. All you need is a good attitude.



## Table of contents

```{toctree}
:maxdepth: 1
:caption: Chapters
:name: mastertoc
:numbered:

jupyter_desktop
notebook
pandas
dataframe
columns
filters
groupby
merge
compute
sorting
concat
charts
export
```

```{toctree}
:maxdepth: 1
:caption: Appendix
:name: appendix
:numbered:

appendix/index
about
```


## Install JupyterLab Desktop


    <iframe class="responsive-iframe" src="https://www.youtube.com/embed/578B63wZ7rI?si=0G3M2pFHt71J8irv" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


The first step is to visit [JupyterLab Desktop’s homepage on GitHub](https://github.com/jupyterlab/jupyterlab-desktop) in your web browser.


Scroll down to the documentation below the code until you reach the [Installation](https://github.com/jupyterlab/jupyterlab-desktop) section.


Then pick the link appropriate for your operating system. The installation file is large, so the download might take a while.

Find the file in your downloads directory and double click it to begin the installation process. Follow the instructions presented by the pop-up windows, sticking to the default options. 

```{warning}
Your computer's operating system might flag the JupyterLab Desktop installer as an unverified or insecure application. Don't worry. The tool has been vetted by Project Jupyter's core developers and it's safe to use.

If your system is blocking you from installing the tool, you'll likely need to work around its barriers. For instance, on MacOS, this might require [visiting your system’s security settings](https://www.wikihow.com/Install-Software-from-Unsigned-Developers-on-a-Mac) to allow the installation. 
```



## Hashes make headings
- Dashes make
- Bulleted lists
```


## Hashes make headings

- Dashes make
- Bulleted lists

Once you've got the hang of making the notebook run, you’re ready to introduce pandas, the powerful Python analysis library that can do a whole lot more than add a few numbers together.



## Import pandas

Create a new cell at the top of your notebook where we will import pandas for our use. Type in the following and hit the play button.

```{code-cell}
:tags: [hide-cell]

my_list = [1, 3, 5, 7, 9, 999]
```

```{code-cell}
import pandas
```

If nothing happens, that's good. It means you have pandas installed and ready to use.

```{note}
Since pandas is created by a third party independent from the core Python developers, it wouldn't be installed by default if you followed our [advanced installation](/appendix/index.md) instructions.

It's available to you because the JupyterLab Desktop developers have pre-selected a curated list of common utilities to include with the package, another reason to love their easy installer.

If your notebook doesn't have pandas, you can install it by running `%pip install pandas` in a cell. This will download and install the library using the [pip](https://pip.pypa.io/en/stable/) package manager and Jupyter's built-in [magic command](https://ipython.readthedocs.io/en/stable/interactive/magics.html).
```

Return to the cell with the import and rewrite it like this.

```{code-cell}
import pandas as pd
```

This will import the pandas library at the shorter variable name of `pd`. This is standard practice in the pandas community. You will frequently see examples of pandas code online using `pd` as shorthand. It's not required, but it's good to get in the habit so that your code is more likely to be quickly understood by other computer programmers.

```{note}
In Python, a variable is a way to store a value in memory for later use. A variable is a named location in the computer's memory where a value can be stored and retrieved. Variables are used to store data values, such as numbers, strings, lists, or objects, and they can be used throughout the program to refer to the stored value.

To create your own variable in Python, you use the assignment operator (`=`) to assign a value to a variable. The variable name is on the left side of the assignment operator and the value is on the right side.
```


## Conduct a simple data analysis

Those two little letters contain dozens of data analysis tools that we'll use in future lessons. They can read in millions of records, compute advanced statistics, filter, sort, rank and do just about anything else you'd want to do with data.

As we saw with the list in the last chapter, Python can do quite a bit on its own. The advantage of pandas is that it saves time by offering even more options. 

We can start to get a look at its powers by converting that plain Python list into what pandas calls a [Series](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.html). Here's how to make it happen in your next cell. Let’s stick with simple variables and name it `my_series`.

```{code-cell}
my_series = pd.Series(my_list)
```

Once the data becomes a Series, you can immediately run a wide range of [descriptive statistics](https://en.wikipedia.org/wiki/Descriptive_statistics). Let's try a few.

How about summing all the numbers? Make a new cell and run this. It should spit out the total, just like the `sum()` function in the last chapter.

```{code-cell}
:tags: [show-input]
my_series.sum()
```

Then find the maximum value in the next.

```{code-cell}
:tags: [show-input]
my_series.max()
```

The minimum value in the next.

```{code-cell}
:tags: [show-input]
my_series.min()
```

How about the average?

```{code-cell}
:tags: [show-input]
my_series.mean()
```

And how about the median, which we didn't have a way to do with just Python?

```{code-cell}
:tags: [show-input]
my_series.median()
```

Let's go further. How about the standard deviation?

```{code-cell}
:tags: [show-input]
my_series.std()
```

Finally, all of the above, plus a little more about the distribution, in one simple command.

```{code-cell}
:tags: [show-input]
my_series.describe()
```

If you substituted in a series of 10 million records, your notebook would calculate all those same statistics without you needing to write any more code. Once your data, however large or complex, is imported into pandas, there's little limit to what you can do to filter, merge, group, aggregate, compute or chart using simple methods like the ones above. In the chapter to come we’ll start doing just using that with data from a real Los Angeles Times investigation.



## 2024-getting-hands-on-ai-tools.md

Hands-on with AI Tools for Journalists

NICAR 2024


Mike Reilley | UIC  | JournalistsToolbox.ai 

 Deck, handout, images and Mike’s schedule/notes: bit.ly/reilley24


Everything on One Freakin’ Slide
Session materials: bit.ly/nicar24aitools


Introduction
Mike Reilley

Let’s have ChatGPT introduce Mike (LOL)

And Happy Sunshine Week everyone!


Introduction
Books

Author of two Routledge textbooks:

“Data + Journalism” with Samantha Sunne 

 “The Journalist’s Toolbox: A Guide to Digital Reportiing and AI” 


Open This Folder
bit.ly/reilley24

JournalistsToolbox.ai
Tools That Are Relevant to Journalists

JournalistsToolbox.ai

Launched in June 2023

Free newsletters and more than 105 short training videos

Thousands of links to AI tools (free and paid): Writing, editing, data, ethics, automation, fact-checking, etc. 

Follow @journtoolbox | @itsmikereilley for updates


Getting Started With AI: The Process

Data Tools: Daigram 
ChatGPT custom GPT (phasing out plug-ins)

Cut/paste header, data and footer into ChatGPT with a detailed prompt on what type of chart you want it to build. 

Produces an interactive chart. Use follow-up prompts to adjust chart type, colors, etc.

Good for quick, basic interactive charts

Not a lot of controls with colors, etc.

Example: https://daigr.am/344e0a13.svg


Data Tools: Chart Maker 
ChatGPT Custom GPT

Creates static charts similar to what you’d get from Excel

Drawback: Won’t include footer information


Data Tools: Data Analyst 
ChatGPT Custom GPT

Built into ChatGPT Plus

Treat it as a co-pilot

Analyzes data (similar to ChartGPT) and creates a static graphic similar to Chart Maker’s GPT tool 

“Kind of a potato”


Data Tools: Rolliapp 
Uses AI to find vetted expert sources on a topic

Includes Information Tracer to detect disinformation spreaders on social platforms (very cool)

Nick Toso, former CNN producer, launched with ICFJ funding

Full disclosure: Rolliapp advertises on JournalistsToolbox.ai

https://rolliapp.com/

Sign up for the “Press Pass” free plan for a year. Use JOURNOAI code to get quicker access

Tools: Geolocating Images

Digital Investigations Substack Newsletter
Craig Silverman’s excellent newsletter on fact-checking tools and techniques.

GeoSpy *
A freemium tool to identify the location of an uploaded photo. 

Picarta
Photo geolocation

Geolocation Estimation
Free tool. Upload a photo to find the location. 
*-Double-check locations in Google Earth Streetview


Track Website Updates: VisualPing 
Track website updates with just a link

Free for journalists with paid upgrades

Adding more AI capabilities

https://visualping.io

Also: Klaxon and Scraper in DocumentCloud.org | Distill.io 

Disclosing AI Use  to Audience


If you disclose, put it in an editor’s note at the start or a footnote at the end of the story

AI images or video should ALWAYS be labeled as illustrations produced with AI (right)

Image credit in Naomi Delkamiller’s LinkedIn post credits software and labels her “art direction”


Mobile Apps

Credits
Joe Amditis, Center for Cooperative Media at  Montclair State University

Ezra Eeman, Strategy Director at NPO

Poynter Institute

Journalist’s Toolbox™ AI

Aimee Rinehart, program manager for the Associated Press Local News AI Initiative

Sil Hamilton, developer, Knight Open Online Course

Ashley Hamer, Descript, blog post: 2023 blog post 

US Copyright Office | CCIJ | Google

NICAR 24 AI and Journalism Panel


Tools: Facial Recognition

Pimeyes
Use it for facial recognition in photos

FaceCheck.id 
Facial recognition tool.

Face++ 
Performs a variety of facial recognition functions.


Introduction
Mike Reilley

UIC Senior Lecturer in Data and Digital Journalism

20+ years full-time teaching: Northwestern (4), ASU (2), DePaul (6) and UIC (8)

Launched JournalistsToolbox.ai in June

Lead trainer: ONA/Microsoft AI in Journalism | RTDNA/GNI Election Fact-Checking Training

More than 14,500 journalists in 42 states trained in 7 years

See Mike and Samantha about Google trainings

Former LA Times, Chicago Tribune, Washington Post staffer

One of 11 founding editors of ChicagoTribune.com

MikeReilley.com | mikereilley1@gmail.com | @journtoolbox | @itsmikereilley


Data Tools: Canva GPT
ChatGPT Custom GPT

Good for Instagram image/text cards, posters, etc.

It can’t do a bar chart … yet.

Reply: My current capabilities are focused on generating designs based on descriptions for creative content such as posters, social media posts, and similar visual materials. I'm unable to directly create data visualizations like bar charts from specific datasets.


Data Tools: GPTExcel 
Can turn even the most complex verbal descriptions into functional Excel formulas.

Can provide straightforward explanations of what the formula is doing.

Can choose Excel, Sheets or Airtable for specific syntax.

Can do SQL, VBA, Regex and Google Scripts too.

Most LLM interfaces are good at these things but this slick tool makes it all a bit easier.

https://gptexcel.uk/dashboard

What Is Fear? 
When Dwight thought the computer was talking to him in “The Office”

Many people in our newsrooms and classrooms fear AI

How can we help them overcome this fear?

APPROACH AI WITH CAUTIOUS CURIOSITY

Data Tools: LLMs 
Can generate near-flawless data practices requests, properly citing state laws, rough template of a FOIA letter and sometimes include PIO and contact info.

Build a data dictionary and design basic interactive templates with cut/paste data or a spreadsheet (ChartGPT, Canva, Daigram, a ChatGPT plug-in)

Generate whole R data dashboards, build a fast webpage, solve complex dataviz solutions, translate between data formats.

Great at technical development and troubleshooting

Charts and graphics using custom GPTs and plug-ins
Source: AI in Journalism Panelists, NICAR 2024

Google Gemini
Help with writing a specific FOIA letter to a government agency

Upload a photo and ask it to check its authenticity and origin (inconsistent; still learning photos of people)

Fact-check Gemini results by clicking on the Google logo at the bottom and you get Google search

Assign it a role: “You are a data journalist and need to …

ChatGPT Custom Instructions
Fill out two fields in the custom instructions pulldown menu when you click on your account name in the lower left corner

Tailor your results the way you want them. 

Helps ChatGPT better understand you, your needs and expectations

Tell it to cite sources, provide links and bulleted list of edits 

Claude.ai 3 Opus
Made by startup Anthropic: $1.5 billion in funding, including $400 million from Google, one if its partners.

Started by Daniela and Dario Amodei, who used to work at OpenAI

Claude can analyze, summarize, translate or answer questions about text – up to 75,000 words, 10x more than ChatGPT

You can upload a PDF or other trusted files to the interface and ask it to summarize or analyze. (double-check all outputs)

Opus 3 version can pull text from handwriting in images. (Pinpoint and others can do this.)

Has hallucinations if you ask it to write a news article


Be Accurate: Edit and Fact-Check
AI is better at creating effective language around information you already have sourced and know to be true.

Facts relayed by AI can be effective leads but should be independently confirmed.

Similar thinking: You wouldn’t quote Wikipedia but you might find the footnote links useful.

Be Accurate: Edit and Fact-Check
How do hallucinations happen with Generative AI?

Writing Prompts
Simplify: Break complex tasks into smaller steps

Use chain-of-thought and step-by-step prompting

Provide training examples to help with new or complex tasks

Add relevant contextual information whenever possible

Repeat the main instructions at the end if need be

Include words or phrases to guide the responses


*-Garbage in, garbage out | *-Better prompts generate better results

Writing Prompts
7. Use clear punctuation, headings and section markers

8. Specify the output structure you want (format, lenses, version of software for image generation)

9. Use tools like Prompt Perfect, a ChatGPT plug-in, to polish a prompt you write

10. Write and rewrite the prompt, and use “Regenerate” buttons until you get a result you want.

11. Be Crystal Clear: Chat with the AI like you're giving directions to a lost tourist or a new intern. The more specific you are, the less likely you'll end up with wacky answers.


Writing Prompts

12. Provide Reference Text: Include reference materials for more reliable answers, especially on less-known topics.

13.  Allow Time for Thinking: Ask the AI to explain its thought process for better answers.

14. ChatGPT custom instructions: Tell it about yourself and how you want it to answer.

15. Test, Test, and Retest: Keep throwing a mix of challenges at the AI. It's like a training montage in a movie, ensuring your AI sidekick gets sharper with each round.

16. Assign it a role: Reporter, doctor, expert in a certain field. 

I’m a medical reporter for a national magazine. Give me five links to good resources for writing about sports concussions

Source on last five tips: OpenAI Prompt Engineering Guide


Base Prompts
Solve complex problems using the First Principles Thinking Framework.

Prompt: "I am having difficulty learning [insert topic]. Help me understand it better by using First Principles Thinking."

Ask ChatGPT, Gemini or Claude

Prompt: "Create a beginner's guide to using ChatGPT. Topics should include prompts, priming, and personas. Include examples. The guide should be no longer than 500 words."

Summarize long texts and documents you upload

Prompt: "Summarize the text below and give me a list of bullet points with  key insights and the most important facts."


Source: @heyshrutimishra on X

Base Prompts
4.  Learn and develop any new skill.

Prompt: "I want to learn / get better at [insert desired skill]. I am a complete beginner. Create a 30 day learning plan that will help a beginner like me learn and improve this skill."

5. Train ChatGPT or other LLM to generate prompts for you. Example below is broad. You can be more specific

Prompt: "I'm new to using ChatGPT and I am a [insert your profession]. Generate a list of the 10 best prompts that will help me be more productive."

6. Have it edit your copy and cite specific things you want it to cover: AP Style, grammar, punctuation, etc. Ask it to list changes.

Prompt:  [paste your writing] "Proofread my writing above and fix grammar, AP Style, punctuation, word usage and spelling mistakes. And make suggestions that will improve the clarity of my writing. List all edits at the end as bullet points.”

Source: @heyshrutimishra on X


## 2024-google-sheets-importing.md

Google Sheets: Importing and data prep
Adrian D. Garcia
@adriandgarcia | garcia.d.adrian@gmail.com
The Financial Times Specialist
bit.ly/3wLFoVh
Prepared for Nicar 2022

Session Outcomes
Practice importing data stored as text, extracting data from PDFs and pulling data live from HTML tables

Use a few key functions and features to reshape and reformat data

Let’s Meet Our Data
bit.ly/ire-sheets-importing

import_contributions.csv – A text file of campaign contributions
warnreport.pdf – A California WARN report
TSA checkpoint travel numbers
https://help.yahoo.com/kb/SLN6796.html

Let’s start with text files
.txt – a generic extension, could be anything


Overview of textual data -- gold standard because most data programs can import/export, not proprietary:

Let’s start with text files
.txt – a generic extension, could be anything
.csv –  most common; each piece of data is separated by a comma


Overview of textual data -- gold standard because most data programs can import/export, not proprietary:

Let’s start with text files
.txt – a generic extension, could be anything
.csv –  most common; each piece of data is separated by a comma
.tsv or .tab – tab-separated values

Overview of textual data -- gold standard because most data programs can import/export, not proprietary:

Let’s start with text files
.txt – a generic extension, could be anything
.csv –  most common; each piece of data is separated by a comma
.tsv or .tab – tab-separated values
You’ll get custom delimiters sometimes: |~;


Overview of textual data -- gold standard because most data programs can import/export, not proprietary:

Import settings
On the Sheets file, add a new tab and name it Contributions. Go to File → Import → Upload.
Find import_contributions.csv
Changing the layout/display of data, make it easier to answer questions and perform analysis

Avoid This Mistake
Not opening a CSV through import can truncate data starting with a zero such as Northeastern zip codes or ID numbers
We do not want to change the data itself.

Pulling in HTML tables
Works well for static tables
https://help.yahoo.com/kb/SLN6796.html

Pulling in HTML tables
=importHTML(“URL”, “table”, 1)
URL = The URL of the webpage you are trying to scrape.
table = This parameter take two options: “table” or “list”.
1 = the number of the table on the page.
https://help.yahoo.com/kb/SLN6796.html

Other resources
table capture for Chrome

Table capture for Firefox 

Pulling data from PDFs

Pulling data from PDFs
native PDFs (text is selectable) 


image PDFs (basically a picture of a piece of paper, requires Optical Character Recognition to extract text)


Pulling data from PDFs

Resources for OCRs
Adobe


Open Source Tools


Data Prep

Data Prep



## 2024-intro-gathering-data-apis.md

Gathering data with 
A guide by Huyen Nguyen, Kansas State University
APIS

https://bit.ly/3wMZ772
For the slides

What is an API?
API stands for Application Programming Interface. It enables two software applications to communicate with each other using a set of definitions and protocols provided in its user guide.
To understand how API functions, you need to know two terms: client, or the application that sends the request, and server, or the application that sends the response. 
There are many types of API, but probably the most popular, flexible, and easy-to-use API is REST API. 
REST stands for Representational State Transfer. Using REST API, you allow the client to send data requests (using REST pre-defined functions such as Get, Put, and Delete) to the server and wait for the server to run internal functions and return output data back to the client.
Data exchange between the client and the server is based on the use of HTTP (Hypertext Transfer Protocol), which allows you to type in your client requests in your own web browser as your regular URLs. The plain data you receive from the server will be stripped of all formatting. By the way, the server won't save client data requests. You must save the data yourself.


How to use a REST API?
1. In many cases, you will need to obtain an API key or an authentication token from the API provider, for security purposes.
2. You need to set up an HTTP API client to customize the client requests using the API key obtained. Or if you don't have an API client, you can create a client request right in your web browser. 

3. Of course, you want to retrieve the base url. This url may be clearly labeled api.something

4. Then, make your queries based on the API documentation. This process can be complicated, but be patient and read the API guides carefully.


What are some popular API clients?
3. Postman: Postman is one of the most popular API development and testing tools. It provides a user-friendly interface for sending HTTP requests, testing APIs, and automating the testing process. It supports various authentication methods and allows you to organize requests into collections.
4. curl: curl is a command-line tool and library for making HTTP requests. It supports a wide range of protocols and is available on various operating systems. While it may not have a graphical interface, it's powerful and scriptable, making it a popular choice for developers who prefer command-line tools.

2. Google Sheets Add-ons: API Connector
1. Your web browser: Chrome, Firefox, Safari

Let’s get started with a web browser!

Exploring FBI Crime Data API 
The FBI Crime Data API is a read-only web service that returns JSON or CSV data. 
It is broadly organized around the data reporting systems the FBI Uniform Crime Reporting (UCR) program uses and their related entities. 
Agencies submit data using one of two reporting formats – the Summary Reporting System (SRS) or the National Incident Based Reporting System (NIBRS).
SRS data is the legacy format that provides aggregated counts of the reported crime offenses known to law enforcement by location. 
NIBRS is a newer format that provides an incident-based view of crime; it includes information about each offense, such as the time of day an incident occurred, the demographics of the offenders/victims, the known relationships between the offenders and victims, and many other details around how and where crime occurs.
https://www.justice.gov/developer

How to interact with the FBI API? 
It’s fairly easy to interact with this API. 
1. It suggests you to obtain an API Key, but you actually do not always need the key.
2. It provides you a client, if you just click on each drop-down menu and hit GET.
3. Here’s the base url: https://api.usa.gov/crime/fbi/cde
4. To make a query, you simply need to select what parameter you want from a drop-down menu and hit Execute. You then can copy/ download the JSON response.
https://www.justice.gov/developer

Import API data into Google Sheet with an add-on
It’s more convenient to import API data into rows and columns for some users. 
1. Login and open a new Google spreadsheet 
2. Select Extensions > Add-ons > Get add-ons > API Connector
3. Install API Connector. Close.
4. Go back to the Extensions > API Connector > Open > Create request
5. Add the Request URL you got from the FBI Crime Data API to the Request URL field. Select a cell for Destination. Click Run.


Collect API data using Postman
It may look more professional to use Postman for API data collection. 
1. Launch and sign up for an account with Postman. 
2. Select Send an API request
3. Add the Request URL you got from the FBI Crime Data API to the GET field. Click Send.

Collect API data from your Terminal
Traditionally, I’d use the Terminal to fetch data. 
1. On Mac, click the Search icon and type Terminal. On Windows, Run > cmd. Launch it. 
2.  Copy and paste the Curl you got from the FBI Crime Data API where the cursor is. Hit Return/Enter.

Exploring Census Bureau APIs
Traditionally, journalists work with Census Bureau APIs to find demographic data and beyond that. You need to sign up for an API key.
Check out the list of available APIs and the Census Data API User Guide. 
Inside the User Guide, you will find the API Discovery Tool to retrieve an API for a specific set of data, for example, American Community Survey: 5-Year Estimates: Detailed Tables 5-Year's (ACS 5) API will be http://api.census.gov/data/2022/acs/acs5. You will also be able to check out all variables for the ACS 5 dataset.
Now, you can start construct the URL to query your desired dataset using the API, the GET function, the variables, and the predicates. 
For example, if you want to query Hispanic data from Table B03002 of the ACS 5, you must write: https://api.census.gov/data/2022/acs/acs5?get=B03002_001E
If you want to add more variables, use a comma. 
https://api.census.gov/data/2022/acs/acs5?get=B03002_001E,B03002_002E
To filter, use &for predicate https://api.census.gov/data/2022/acs/acs5?get=B03002_001E,B03002_002E&for=state
To check for state code, you can use this table.
Users are restricted to sending just 500 queries per day with up to 50 variables in a single query. To bypass the limits, you must append your API key at the end of the URL. https://api.census.gov/data/2022/acs/acs5?get=B03002_001E,B03002_002E&for=state&key=your API key


Getting more advanced with APIs
Most of the time, your need won’t be satisfied if you just rely on an HTTP url to collect small chunks of data. You need to  use some Python/R code to help with authentication and pagination.
 
In the following section, I’ll introduce to you:
• How to collect all video statistics/comments for a YouTube channel
• How to collect a list of all 3D models from Sketchfab

Both tutorials were developed when I conducted my academic research. 
To do so, you need to harness THREE basic tools:

• Google Colab: a coding environment where you execute most of your API requests. 
• ChatGPT: a bot that can teach you some Python code and perhaps help solve errors from running its outdated code.
• Dev Tools: web browser’s developer tools that allow you to inspect websites, track API requests, and analyze API responses.  If you are new, here’s a great guide by Bloomberg journalist Leon Yin.

Of course, you will need to understand the APIs you want to interact with. 

Exploring YouTube Data API v3
Audience metrics are currency for video creators. 

In order to measure audience engagement with 360VR videos, I used YouTube Data API v3 to collect video statistics and comments for all videos from the YouTube VR channel [https://www.youtube.com/channel/UCzuqhhs6NWbgTzMuM09WKDQ]. 

You can try the API Explorer on a side panel for convenience. 
• You need to specify which part(s) of the video properties you want the API response to  include.
• You then need to add a video id(s).
• Click Execute and authenticate the connection to your Google account.
https://www.justice.gov/developer

Google API Console and API keys (1)
First, you need to create a project in the Google Cloud Console and obtain authorization credentials so your application can submit API requests.

https://www.justice.gov/developer

Google API Console and API keys (2)

Next, enable YouTube Data API v3. 


https://www.justice.gov/developer

Google API Console and API keys (3)
Finally, copy the API key
https://www.justice.gov/developer

Make API requests in Google Colab
Collect all video statistics
https://colab.research.google.com/drive/1_vNoZginksvGaKjy25d2deLn0nh59qrE?usp=sharing
Collect all video comments https://colab.research.google.com/drive/1UuWSLjqxXiRsdQblAr5p3f6DOWFF6JO5?usp=sharing
Save every 200 videos
https://colab.research.google.com/drive/1yJmB2AbVMX9479v7WI8QRG1YwLSo9B-F?usp=sharing 
Collect comments from specific videos
https://colab.research.google.com/drive/1ZXea5t2n5D3AS676RMhZ1K-wuDIZpltY?usp=sharing


Theoretically, you can use ChatGPT to generate the Python code to request video statistics/comments from a specific YouTube channel. 

In reality, the process is more complicated. You can open my two Colab notebooks and try collecting YouTube data for the YouTube VR channel with you own API key. 

When you get used to the practice, you can change your YouTube channel ID as well. To find a channel ID, look for the number at the end of the YouTube link.
https://www.justice.gov/developer

Video statistics

Video comments

Exploring hidden Sketchfab API (1)
As a media economist, I care for price and pricing determinants of media assets. 

In order to collect price and characteristics of 3D models from Sketchfab, I explored Sketchfab API. But it seems like Korbel, Siddiq and Zarnekow (2022) suggested that researchers have to use the dev tools from the web browser to analyze the 3D model listing of 24 models each page and cursor referencing. Or, it has a hidden/undocumented API. 

You need to do the following: 
• Open the website on Chrome browser (recommended) and turn on Dev Tools.
• Monitor the Network tab, especially the  fetch/XHR section, where some API requests may show up. 
• On the left, add some features in Category, Date, Downloadable, and Animated. 

https://www.justice.gov/developer

• Find the cURL under the Name column.

If you click on a search request, you will see a list of 3D models under the Preview and Response windows.

You will see that the more you scroll, the Response’s JSON file will change accordingly.

At the top of each response, you will see the cursors value. They’re helpful for pagination.

• Convert cURL to Python code using this.

Copy the code
Use Dev Tools to find Sketchfab API (2)
https://youtu.be/5eeFeWomZEo


Make API requests in Google Colab
Collect list of 3D models 
https://colab.research.google.com/drive/1bJYBo1Qfc_7PKML5WcmXwlzYC35Jckux?usp=sharing


You can modify the Python requests to check if after loading 24 models, there will be the next batch, then output the results as a CSV file. 

You can open my Colab notebook to see how it works. If you need to customize the code to suit your need and don’t know Python very well, try ChatGPT. That’s how I’ve learned Python recently.

When you get used to the practice, you can change the parameters as you please. 
https://www.justice.gov/developer


Thank you for your attention!
I hope these tips are useful for your data-driven/research projects.
If you have any questions, please feel free to contact: huyenme@ksu.edu


## 2024-large-scale-scraping.md

Leon Yin ∙ Bloomberg | Ilica Mahajan ∙ The Marshall Project | Jeff Kao ∙ ProPublica

https://bit.ly/nicar2024scrapepres 
Large-scale scraping projects
2024-03-08, 10:15am

Roadmap
Leon: how to use a big chunky computer to do a large scraping project
Ilica: concepts for parallelizing big chunky computers for a large scraping project
Jeff: how we put these concepts into practice for a large scraping project

Still Loading
https://themarkup.org/still-loading
Leon Yin and Aaron Sankin
The Markup

Findings:
4 Internet Service Providers (ISPs) charge the same price for drastically different speeds based on where you live. 
After collecting +1.1M Internet plans we found that…
In major cities across the U.S., neighborhoods that were:
Historically redlined (22 / 22 = 100% cities)
Lower-income (35 / 38 =  92% cities)
Highest concentration of people of color (21 / 32 = 66% cities)
… were disproportionately asked to overpay for slow speeds.

Used broadband availability tools (BATs) to scrape address-level data that revealed ISPs vastly overstated the availability, speed, and competition of their services to the FCC. 
“No WAN’s Land” - Major, Teixeria, and Mayer 2020
Source: Screen recording of AT&T’s lookup tool.

Trial analysis: AT&T - Green Bay, Wisconsin


Who are the actors?
4 of the nation’s largest providers practice “tier flattening”:
AT&T, Verizon, CenturyLink, EarthLink
They serve 44 states and Washington D.C.

Tier flattening
Disparate outcomes
Many cities

Challenges
IP blocking
Browsers are slow
Where to get addresses?
Categorization?


Data Collection: Where to find addresses?
Simple 💪big😤data 👉 collect the largest city in each state.
Major cities focus on urban areas.
Found open source addresses:
Used OpenAddresses and NYC Open Data to collect 12M addresses from 45 cities.
Incomplete: Census Geocoder to merge incorporated city and block group.
Goal: Collect plans for 10% of addresses in each census block group (stratified sample) to collect representative samples in each city.
Incomplete how?

Data Collection: using Undocumented APIs
Found and reverse-engineered underlying API’s powering each search portal.
Built four scrapers using similar set of sequential requests:
Autocomplete and verify address
Choose apartment number
Check availability and list plans
Only made possible by using a session to keep track of cookies and params.
Scraped ~100x addresses at once by making each scraper asynchronous.
Circumvented IP blocking us a proxy.

Example of a scraper as a Python function
Disclaimer: this is an not a functioning example!
Make note of how the scraper is the smallest unit of work

Example of a scraper as an asynchronous function
Disclaimer: this is an not a functioning example!

Run asynchronously using the asyncio and aiohttp libraries.
The await notations used to make sure actions to finish sequentially.
Can run 100x or more at once with async (forgot to write that down)

Use session to keep track of cookies and state across requests. 
Disclaimer: this is an not a functioning example!

Route requests through IP proxy to prevent rate limiting.
A proxy looks like this: {“http” : “http://example-proxy.com:5321}
Note that all proxies are not the same

Bookkeeping tips
Don’t repeat yourself: Structured naming system for outputs.
Make a todo list: AWS SQS (a queuing service)is useful for keeping tabs on what’s to be done.
Save receipts:  Keep raw data, don’t parse until later.
Circumvent blocking: Use proxies as a last resort. Different levels of proxies.

Resources
Finding undocumented APIs - a tutorial that lives online
https://inspectelement.org/apis

The U.S. Place Sampler - a tool by Big Local News and The Markup to build random samples of street addresses in cities, block groups, tracts, and more.
https://usps.biglocalnews.org


Building and analyzing a novel dataset about the criminal court system
Not easy to access, understand, or make use of
Want it to be queryable to answer questions


Cases
Defendants
Charges
Airtable
GraphQL


Scraping
All credit to Aaron Williams and David Eads for this part
AWS -> elastic container service = break down the problem into bite-sized chunks
Large scale projects are all about breaking things down, and thinking a series of functions/inputs/outputs
Write a scraper to scrape one page at a time, and funnel documents to an s3 bucket
Write a script that takes a start and end case number, scrapes those cases

Scraping
Anti
You may hit anti-scraping tech if you’re hitting the same domain over and over again
Block your IP
Can’t block the entire AWS space
So new containers get new IP’s

Word of the day:
Idempotent

Containerize
Bite-sized jobs
Dockerfiles: a recipe to create containers
Containers can be deployed locally or in the cloud
Separate steps: scrape to s3 bucket, then parse into tables
AWS to store containers
AWS ECS to run the containers in…

DOCKER
FILES
a recipe to create containers

Parallelize
Run thousands containers at once
For scraping against one domain, not too many in parallel
Once scraped files are in an s3 bucket, go wild
Tighten iteration loops 


Iteration
Tighten loops, experiment, re-run, change schemas to suit analysis
Tunable run times to parse >100K documents
Hasura (GraphQL) + Observable (Analysis + Data Memos)
Up-to-date fact checking

Story: Series examining Google’s ad business

GOALS:
Given a list of disinfo websites, figure out which ones are advertising with Google.
Determine a list of all of websites on the internet advertising using Google (deanonymize sellers.json)
TASKS:
Design a system that can determine whether a site is advertising using Google’s ads platform.
Do this quickly (i.e., in parallel) for any arbitrarily long list of websites 
describe the story and how scraping was relevant
-the story was examining google’s ad system
-ads.txt

SCRAPING (multiple websites in parallel)
S3
database of all sites
docker/ecs/ecr/fargate
x 30

dockerize your scraping script
Set up Dockerfile (environment and code)
Create a docker image
upload the docker image on ECR (Elastic Container Registry)
Essentially a repository of docker images
define your container in ECS (Elastic Container Service)
Basically the type of computer you are running in the cloud
kick off N instances
Via AWS console or with a script
MOVING YOUR WORK INTO THE CLOUD
Docker Image
Container

BUILDING AND TESTING YOUR SYSTEM
Build it step by step:
Local computer => Local docker image => One cloud instance => Multiple cloud instances
Separate scraping and analysis
Collect data in as raw a state as possible
Back-of-the-envelope math
Manage time, money and time spent building
MANAGING COSTS/TIME
Look at the cost structure of your tools; design your system to save money
Storage and compute
Compute: Fargate vs EC2 - Fargate is about 20% more expensive, but it shuts down when it finishes the task
Storage: S3 (cost per transaction: directory listing vs retrieving a file; ongoing storage costs)
Turn on cloud resources only when you’re using them!
PRACTICAL TIPS

General Tips
Scheduling: 
Use cron (locally) or configure cloud instances to kick off at set times or intervals
Be discrete: 
Break tasks up into smallest unit or work. 
Use queuing to communicate between tasks.
Keep logs: 
Record what was done to help troubleshoot.
Optimize: 
Use queues and logs to find bottlenecks. Determine infra and N instances needed. 

Don’t always need to be fancy or in the cloud!
Parallelization: bit.ly/nicar2024_scrape 

Thank you! Questions?
Leon Yin ∙ Bloomberg | Ilica Mahajan ∙ The Marshall Project | Jeff Kao ∙ ProPublica

New Story about OpenAI GPT Bias in hiring ->
Leon Yin, Davey Alba, Leonardo Nicoletti
Bloomberg News | March 7, 2024
Plz read here:

Auditing Algorithms and AI for Bias
Leonardo Nicoletti, Victoria Turk, Leon Yin, Meredith Broussard

NICAR Baltimore - Saturday, March 9, 2:15 p.m. in Harborside C
Discussion area



## Introduction

This class seeks to help you solve a common problem in journalism: Data stored in a computer generated PDF or worse an image PDF. We'll first walk through how to extract text from a computer-generated PDF using command line tools. Then we'll step up to Optical Character Recognition, or OCR, to work on image files. 

If we have some extra time at the end of class, we'll show how you can use `pdfplumber` to extract data from one of the searchable PDFs we created. You can find the notebook [here](/notebooks/pdfplumber_example.ipynb).


## Installation

First things first, we need to install the tools we'll be using. (NICAR attendees using lab laptops: IRE has already completed the install).

* [Xpdf](https://www.xpdfreader.com/) is an open source toolkit to work with pdfs. We'll be using its tool, [pdftotext](https://www.xpdfreader.com/pdftotext-man.html).

* [tesseract](https://github.com/tesseract-ocr/tesseract/wiki) is our OCR engine. It was first developed by HP but for the last decade or so it's been maintained by Google.

* [ImageMagick](http://www.imagemagick.org/script/command-line-processing.php) is an open source image processing and conversion power tool.

* [Ghostscript](https://www.ghostscript.com/index.html) is an interpreter for PDFs and Adobe's PostScript language.

This class will be following the Mac install instructions but you can find Windows and Linux in the following documentation.

* Xpdf [documentation](https://www.xpdfreader.com/download.html)
* tesseract [documention](https://github.com/tesseract-ocr/tesseract/wiki).
* ImageMagick [documentation](http://www.imagemagick.org/script/command-line-processing.php)
* Ghostscript [documentation](https://ghostscript.com/doc/9.21/Install.htm)

For Mac, we'll be using the Homebrew package manager. You can install it [here](https://brew.sh/). 

For tesseract, you will use the following command.
```bash
brew install tesseract
```

For Xpdf, you will use this.
```bash
brew install xpdf
```

We will also install libtiff, a dependency for ImageMagick that we will need.
```bash
brew install libtiff
```

Then we'll install ghostscipt
```bash
brew install ghostscript
```

And for ImageMagick you will use this.
```bash
brew install imagemagick
```

To install all of them at once, you can run the following
```bash
brew install xpdf tesseract libtiff ghostscript imagemagick
```



## Some important updates

This class doesn't assume that you're working on a Mac with an OS greater than 13 but if you are, you can take advantage of some built-in OCR features. For example, some of the image PDFs you open up from this repo will be automatically OCR'd and have selectable text when you open them on newer Macs. 

You can also try out [textra](https://github.com/freedmand/textra) an open-source project from The Washington Post's Dylan Freedman that uses those built in Mac OCR tools to extra text from image PDFs. 

All of the tools below are also available to you on Mac OS 13 or higher.

If you're not on a newer Mac, fear not! Hopefully some of the tools below will help you out.



## How to think about this class
Text extraction from PDFs and OCRing image files is much more of an art than a science. The tools below are meant to give you a lot of different options to try to get the text out of an image PDF and into a format that you can work with. Sometimes they will work amazingly well. Sometimes they won't work at all. Oftentimes, it's somewhere in the middle where the data will require some clean up.

If you're comforable in Python, I recommend pairing these tools with other great open-source projects such as Jeremy Singer-Vine's [`pdfplumber`](https://github.com/jsvine/pdfplumber), which we used extensively to build several Python parsers for [the Capital Assets project](https://www.wsj.com/articles/capital-assets-11665673055) and many others at The Wall Street Journal.



## Files

We'll be using a number of files for our examples. You can find them in [here](/files).


## Scenario 1: Analyzing a computer generated pdf with embedded text (searchable pdf)

We want to extract the text from a searchable pdf for analysis of some type. There are many GUI software programs you can use to do this. They all have strengths and weaknesses.

* [Cometdocs](https://www.cometdocs.com/)
* [Tabula](https://tabula.technology/) (free and great for tabular data!)
* [Adobe Acrobat Pro](https://acrobat.adobe.com/us/en/acrobat/pricing.html?mv=search&sdid=J7XBWTSV&ef_id=CjwKCAiA1ZDiBRAXEiwAIWyNC62H_xFn3sW5k3JAETpc_MeS9HOq-7l-qD2cvFXcU-Qkl-v_TPYjSxoC4bsQAvD_BwE:G:s&s_kwcid=AL!3085!3!99546333262!e!!g!!%2Badobe%20%2Bacrobat%20%2Bpro&gclid=CjwKCAiA1ZDiBRAXEiwAIWyNC62H_xFn3sW5k3JAETpc_MeS9HOq-7l-qD2cvFXcU-Qkl-v_TPYjSxoC4bsQAvD_BwE) ($$)
* [Abbyy Finereader](https://www.abbyy.com/en-us/finereader/?redirect-from=old-fr-pro&__c=1) ($$ but also very accurate)
* [PDFElement](https://pdf.wondershare.net/ad/pdf-editor-mac.html?gclid=Cj0KCQiA9YugBhCZARIsAACXxeIuIJnFM5WV8YzhxqnEVl_cP7dwNYTGuzNZ-w0AhQiEn6AWrWZZ9TEaAvuXEALw_wcB) 


For this tutorial, we're going to use an open source powertool from Xpdf called `pdftotext`. The construction of the command is pretty intuitive. You point it at a file and it outputs a text file.

I often use this tool to check for hidden text, particularly in documents that have redactions. 

Our example is from 2019 when lawyers for Paul Manafort accidentally filed a document in court that wasn't properly redacted — even though the document contained blacked out sections, the text was still present in the document. You can read more about it [here](https://www.apnews.com/608b9fcbca5941348e2ac8796e94c8cd).

One way to get to this text is just to copy and paste the sections out. But this can be tedious if there are a lot of sections or you have a large document. A faster and easier method is Xpdf's pdftotext.

Our [document](files/manafort/Manafort_filing.pdf) has several sections like this.


But since we can tell that there's text underneath there, let's run it through `pdftotext` and see what comes out.

#### `pdftotext` command construction

```bash
pdftotext /path/to/my/file.pdf name-of-my-text-file.txt
```
So for our file it would look something like this within the files directory.

```bash
pdftotext Manafort_filing.pdf manafort_filing.txt
```

You can also run it from the repo parent directory.

```bash
pdftotext files/manafort/Manafort_filing.pdf files/manafort/manafort_filing.txt
```

Now, if we look in our newly created text file, we can find full extracted text — including the parts that are blacked out in the PDF. 

Let's take a look at another one of our files involving tabular data, found [here](/files/tabular/07012018-report-final.pdf). This is a salary roster of Trump White House employees. We'll be using a single image page of this file for a later example.


As mentioned before, Tabula is a great tool for getting tabular data out of pdf files, but I wanted to give you another option using pdftotext that works well with fixed-width data files like this White House salaries listing. It also has the added benefit of being easily scriptable.

### pdftotext command for tables

```bash
pdftotext -table /path/to/my/file name-of-my-text-file.txt
```

We'll test it out on the [file](/files/tabular/07012018-report-final.pdf). You can ```cd``` to it in the ```/files/tabular``` directory or just use the path.

```bash
pdftotext -table 07012018-report-final.pdf tabular-test.txt
```

Or use this command from the repo parent directory

```bash
pdftotext -table files/tabular/07012018-report-final.pdf files/tabular/tabular-test.txt```
```

You should get something like this: 


For comparison, try using just pdftotext.

```bash
pdftotext files/tabular/07012018-report-final.pdf files/tabular/raw-test.txt
```

You should get something like this (very bad stuff):


Now that we've walked through one way to extract text from computer generated (nice) pdfs, let's move on to working with image pdfs.



## Scenario 2: Basic text extraction from image files

Extracting text from image files is perhaps one of the most common problems reporters face when they get data from government agencies or are trying to build their own databases from scratch (paper records, the dreaded image pdf of an Excel spreadsheet, etc.) To do this, we use OCR and in this example, `tesseract`.

#### Basics of `tesseract`

`tesseract` has many options. You can see them by typing:

```bash
tesseract -h
```

We're not going to go into detail on many of these options but you can read more [here](https://github.com/tesseract-ocr/tesseract/wiki)

The basic command structure looks like this:

```bash
tesseract imagename outputbase [-l lang] [--oem ocrenginemode] [--psm pagesegmode] [configfiles...]
```

Let's look at a single image file. In this case, that's the wh_salaries.png file in our imgs folder. This is the first page of our White House salaries PDF but notice that it is not searchable.

This is perhaps the most simple use of `tesseract`. We will feed in our image file and have it output a searchable pdf.

In ```/files/single_img``` directory, use the following command.

```bash
tesseract wh_salaries.png out pdf
```

You start with a file like this:


You should get a file name out.pdf and you can see that it's searchable.



## Scenario 3: Combining our skills to make a searchable pdf out of an image pdf.

#### Converting pdfs to images to prepare for OCR using ImageMagick

So far, we've covered extracting text from computer generated files and doing some basic OCR. Now, we'll turn to creating searchable pdfs out of image files. To do this, we'll be adding another command line tool called ImageMagick, an image editing and manipulation software.

We will be using the `convert` tool from ImageMagick.

ImageMagick has some great documentation that explains its many options. You can find it [here](http://www.imagemagick.org/script/command-line-options.php#page)

```bash
convert [options ...] file [ [options ...] file ...] [options ...] file
```

If you're familiar with photography or document scanning, you know that the proper image resolution is essential for electronic imaging. When it comes to OCR, this is even more true. 

The general standard for OCR is 300 dpi, or 300 dots per inch, though [ABBYY recommends](https://knowledgebase.abbyy.com/article/489) using 400-600 for font sizes smaller than 10 point. In ImageMagick, this is specified using the density flag. Below we are telling ImageMagick to take our pdf document and convert it to an image with 300 dpi.

#### Important 

Before we go on from here, let's make sure we have the tiff delegate installed. You can check like this:

```bash
convert -list configure
```

Scroll down to `DELEGATES` and make sure it includes `tiff`

For example:

```bash
DELEGATES      bzlib mpeg freetype jng jpeg lzma png tiff xml zlib
```

#### If you don't have tiff in the list, follow these steps:

First check to make sure that libtiff and ghostscript are installed. You can do this by running

```bash
brew list
```

If ghostscript is not in the list, then install it using brew.
```bash
brew install ghostscript
```

If libtiff is not in the list, then install it using brew.
```bash
brew install libtiff
```

Now check to make sure that imagemagick is recognizing libtiff is installed as a dependency.
```bash
brew info imagemagick
```

If you're good to go, it should look something like this:

```bash
==> Dependencies
Build: pkg-config ✔
Required: freetype ✔, jpeg ✔, libheif ✔, libomp ✔, libpng ✔, libtiff ✔, libtool ✔, little-cms2 ✔, openexr ✔, openjpeg ✔, webp ✔, xz ✔
```
Now that we've installed ghostscript and the tiff delegate, let's continue on with our example.

#### Example with the image file Russia findings document


First, we have to convert it to an image so we can run it through tesseract.

We'll use ImageMagick's `convert` tool.

```
convert russia_findings.pdf russia_findings.tiff
```

On a Mac, an easy way to find the dpi of an image is to use Preview. Open the image in preview, go to `Tools` and click `Show Inspector`.

So let's take a look at our image we just created.

#### Open in Preview


#### Go to `Show Inspector`


#### Inspector pane 1


#### Inspector pane 2


So our dpi is `72`, which likely is fine for this document but let's go ahead and up that using convert. This will increase the file size of the tiff we create (so warning about file bloat) but it's only a temporary file that we're using to get the best text recognition.

Let's do this with our Russia document.

```bash
convert -density 300 russia_findings.pdf -depth 8 -strip -background white -alpha off russia_findings.tiff
```

So let's break this down.

`convert` - invokes ImageMagick's convert tool

`-density` - ups the dpi of our image to 300

`russia_finding.pdf ` - our file that we're converting to an image.

`-depth 8` - "This the number of bits in a color sample within a pixel. Use this option to specify the depth of raw images whose depth is unknown such as GRAY, RGB, or CMYK, or to change the depth of any image after it has been read", according to ImageMagick documentation.

`-strip` - strips off any junk on the file (profiles, comments, etc.)

`-background white` - sets the background to white to help with contrasting our text

`-alpha off` -generally the transparency of the image. A great explanation [here](https://www.quora.com/What-exactly-is-an-alpha-channel-in-an-image)

#### Now we run this tiff through tesseract

```bash
tesseract russia_findings.tiff russia_findings_enh pdf 
```

And you've got a searchable pdf!

Let's take a look at the underlying text now.

```bash
pdftotext russia_findings_enh.pdf russia_text.txt
```



## Where to go from here:

#### Scripting and Batch process

Now that we've walked through how some of these tools work, you can put them all together into bash scripts if you like. I've included an example script in this repo that seeks to hold down file bloat but it may require some tweaking for your specific use case. OCRing is not a perfect science and most of the time, it takes some trial and error to find the right settings for the documents you're working with.

Try it out on `russia_findings.pdf` in the `image_pdfs` folder. (You will likely need to run `chmod u+x im_ocr.sh`)

##### Output a searchable pdf

```bash
./im_ocr.sh /files/image_pdfs/russia_findings.pdf pdf
```

In the IRE mac lab, the terminals by default use zsh, so we'll want to invoke bash manually instead like below.

```bash
bash im_ocr.sh /files/image_pdfs/russia_findings.pdf pdf
```

##### Output a text file
```bash
./im_ocr.sh /files/image_pdfs/russia_findings.pdf txt
```

In the IRE mac lab, the terminals by default use zsh, so we'll want to invoke bash manually instead like below.

```bash
bash im_ocr.sh /files/image_pdfs/russia_findings.pdf txt
```
#### Judicial Public Financial Disclosure Example

Public financial disclosures of federal judges are multi-page documents but they are released as extremely long, single tiff files. You can find a similar test file [here](https://drive.google.com/open?id=11YpC2-0yYyuJL7AJnvG48q9H8hrrDQon)


And you'll notice that the pages need to be split.


The workflow below walks through one example of how to solve the problem using ImageMagick and Tesseract.

This blows up the images, adjusts the image resolution, ups the contrast to help bring out the text. It then outputs a grayscale version, set at 8-bit depth, named `Walker16_enh.tiff`.
```bash
convert -resize 400% -density 450 -brightness-contrast 5x0 Walker16.tiff -set colorspace Gray -separate -average -depth 8 -strip Walker16_enh.tiff
```

Next we use ImageMagick's crop to split it up into a multi-page pdf. 

To find the dimensions, first use Preview's Inspector tool. You 'll see the dimensions of the entire image file. (NOTE: This screenshot is from a different file since I added this later.)


The first value is the width and the second value is the length. To get the pixel length of each page, just divide by the number of pages you should have in the final file.


```bash
convert Walker16_enh.tiff -crop 3172x4200 Walker16_to_ocr.tiff
```

Then we convert that image into a searchable pdf.

```bash
tesseract Walker16_to_ocr.tiff -l eng Walker16 pdf
```

Exploring the various options and fine-tuning your skills with ImageMagick can help prepare you for the next big step: Batch processing of documents. 

As mentioned above, you should definitely check out [`pdfplumber`](https://github.com/jsvine/pdfplumber#extracting-tables) and Jeremy's tutorial on how to get started with it found [here](https://mybinder.org/v2/gh/jsvine/nicar-2023-pdfplumber-workshop/HEAD?labpath=notebooks/00-hello-world.ipynb).


## Sources and references
I originally created this tutorial for [NICAR 2019]('https://www.ire.org/events-and-training/conferences/nicar-2019'). It was update for [NICAR 2022](https://schedules.ire.org/nicar-2022/). It relies on many helpful open source resources that deserve credit. They are listed below. Thanks for sharing your work with the rest of the world.

[Tesseract](https://github.com/tesseract-ocr/tesseract/wiki/Command-Line-Usage) documentation

[ImageMagick](https://www.imagemagick.org/script/command-line-processing.php) documentation

[pdftotext](https://www.xpdfreader.com/pdftotext-man.html) documentation



## Next steps: `pdfplumber` example

This short notebook shows you one way you can wrangle some of the data we extracted using the CLIs in the tutorial.

If you want a more detailed `pdfplumber` tutorial, please refer to Jeremy Singer-Vine\'s great documentation found [here](https://github.com/jsvine/pdfplumber).

#### Import `pdfplumber` and `pandas`

We\'ll use pdfplumber to extract our tabular data into a list of lists. We\'ll then use `pandas` to turn that into a dataframe.

``` python
import pdfplumber
import pandas as pd
from pathlib import Path
```

#### Open our pdf using `pdfplumber`

We\'ll be using the `out.pdf` we created from the image PDF of White House salary data.

``` python
repo_path = Path().parent.resolve().parent

pdf_path = f'{repo_path}/files/single_img/out.pdf'

pdf = pdfplumber.open(pdf_path)
```

#### Example of table extraction

Below are some functions that uses `pdfplumber`\'s `extract_table` and `extract_words`. This example is slightly more complicated because we are using a searchable PDF created by OCR. These types of PDFs don\'t often have the lines, curves and rects that pdfplumber uses to parsed computer-generated text.

Instead, we are using the pixel position of each word and the structure of the PDF to pass in explicit lines where each column should be separated based on our own visual inspection of the document.

There are many ways you can find these pixel values.

A few common ones below:

1.  You can use Preview\'s Inspector and Rectangle Selection tools in the Tools menu. Drawing a rectangle with the left side of the box where you think the line should go will yield the pixel position in the \"Left\" box in the inspector as you draw.

2.  You can use `pdfplumber`\'s built-in visual debugging tools that allow you to view the pdf page in the Jupyter notebook and draw lines where the columns should be separated. Then you record the pixels in the list as we do below.

3.  You can look for the column headers using `pdfplumber`\'s `extract_words`. For example, if the column header words are unique, you could loop through all the words, add some logic to identify them and then assemble the vlines from the `x0` values. (See below with some caveats because the OCR\'d pdf isn\'t perfect).

I strongly suggest you familiarize yourself with `pdfplumber`\'s documention because it has many other tools and suggestions that can help extract much more complicated tables.

``` python
def create_settings(page, header_words):
    '''
    Accepts a pdf page
    Accepts a list of column header words
    Outputs a table settings dict with vlines
    '''
    padding = 3 # Give some extra space on the left because the headers are slightly off center.
    vlines = [77, 810] # Set the first and last value because of some quirks with the OCR
    words = page.extract_words()
    [vlines.append(word['x0'] - padding) for word in words if word['text'].lower() in header_words]
    vlines.sort()
    ts = {
            "vertical_strategy": "explicit", 
            "horizontal_strategy": "text",
            "explicit_vertical_lines": vlines,
    }
    return ts


def extract_salaries(page, ts, cols):
    '''
    Accepts a pdf page with a table of salary data
    Accepts a list of vertical lines that divide the data columns
    Accepts a dictionary of table settings
    Accepts a list of columns to slap on the DataFrame as headers
    Outputs a pandas DataFrame
    '''
    data = []
    table = page.extract_table(table_settings=ts)
    [data.append(row) for row in table if row[0] != '']
    return pd.DataFrame(data, columns=cols)


cols = [
    'name',
    'status',
    'salary',
    'pay',
    'position'
]

page = pdf.pages[0]

ts = create_settings(page, cols)

df = extract_salaries(page, ts, cols)

df
```


<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>status</th>
      <th>salary</th>
      <th>pay</th>
      <th>position</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Amin, Stacy C.</td>
      <td>Employee</td>
      <td>$140,000.00</td>
      <td>Per Annum</td>
      <td>ASSOCIATE COUNSEL TO THE PRESIDENT</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Andersen, Whitney N.</td>
      <td>Employee</td>
      <td>$115,000.00</td>
      <td>Per Annum</td>
      <td>SPECIAL ASSISTANT TO THE PRESIDENT AND DIRECTO...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Anderson, Alexander J.</td>
      <td>Employee</td>
      <td>$78,500.00</td>
      <td>Per Annum</td>
      <td>DIRECTOR OF VIDEO PRODUCTION</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Angelson, Alexander J.</td>
      <td>Employee</td>
      <td>$115,000.00</td>
      <td>Per Annum</td>
      <td>SPECIAL ASSISTANT TO THE PRESIDENT FOR LEGISLA...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Assefi, Camellia N.</td>
      <td>Employee</td>
      <td>$47,900.00</td>
      <td>Per Annum</td>
      <td>WRITER FOR PRESIDENTIAL CORRESPONDENCE</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Assefi, Omeed A.</td>
      <td>Employee</td>
      <td>$78,500.00</td>
      <td>Per Annum</td>
      <td>ASSISTANT SPECIAL COUNSEL</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Baitel, Rachael</td>
      <td>Employee</td>
      <td>$71,300.00</td>
      <td>Per Annum</td>
      <td>EXECUTIVE ASSISTANT</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Baker, Brittany G.</td>
      <td>Employee</td>
      <td>$63,200.00</td>
      <td>Per Annum</td>
      <td>EXECUTIVE ASSISTANT</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Baldwin, Brittany L.</td>
      <td>Employee</td>
      <td>$95,000.00</td>
      <td>Per Annum</td>
      <td>SPECIAL ASSISTANT TO THE PRESIDENT AND SPEECHW...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Beattie, Darren J.</td>
      <td>Employee</td>
      <td>$84,600.00</td>
      <td>Per Annum</td>
      <td>SPEECHWRITER AND POLICY DEVELOPMENT AIDE</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Beatty, Julia-Grace D.</td>
      <td>Employee</td>
      <td>$42,800.00</td>
      <td>Per Annum</td>
      <td>STAFF ASSISTANT</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Bekkering, Michelle A.</td>
      <td>Detailee</td>
      <td>$143,100.00</td>
      <td>Per Annum</td>
      <td>POLICY ADVISOR</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Beley, James P.</td>
      <td>Employee</td>
      <td>$63,200.00</td>
      <td>Per Annum</td>
      <td>DIRECTOR OF WRITERS FOR PRESIDENTIAL CORRESPON...</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Berkowitz, Avrahm J.</td>
      <td>Employee</td>
      <td>$130,000.00</td>
      <td>Per Annum</td>
      <td>SPECIAL ASSISTANT TO THE PRESIDENT AND ASSISTA...</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Biddle, Emily K.</td>
      <td>Employee</td>
      <td>$78,500.00</td>
      <td>Per Annum</td>
      <td>DEPUTY SOCIAL SECRETARY</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Bis, Justin B.</td>
      <td>Employee</td>
      <td>$71,300.00</td>
      <td>Per Annum</td>
      <td>PRINCIPAL DEPUTY ASSOCIATE DIRECTOR FOR PRESID...</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Blair, Patricia A.</td>
      <td>Employee</td>
      <td>$104,200.00</td>
      <td>Per Annum</td>
      <td>CHIEF CALLIGRAPHER</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Blase, Brian C.</td>
      <td>Employee</td>
      <td>$140,000.00</td>
      <td>Per Annum</td>
      <td>SPECIAL ASSISTANT TO THE PRESIDENT FOR ECONOMI...</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Block, Monica J.</td>
      <td>Employee</td>
      <td>$140,000.00</td>
      <td>Per Annum</td>
      <td>SPECIAL ASSISTANT TO THE PRESIDENT AND DEPUTY ...</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Blount, Mallory N.</td>
      <td>Employee</td>
      <td>$52,000.00</td>
      <td>Per Annum</td>
      <td>DIRECTOR OF DIGITAL RESPONSE FOR PRESIDENTIAL ...</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Blount, Patricia H.</td>
      <td>Employee</td>
      <td>$63,000.00</td>
      <td>Per Annum</td>
      <td>RECORDS MANAGEMENT ANALYST</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Bock, Caroline E.</td>
      <td>Employee</td>
      <td>$115,000.00</td>
      <td>Per Annum</td>
      <td>SPECIAL ASSISTANT TO THE PRESIDENT AND ASSOCIA...</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Bolton, John R.</td>
      <td>Employee</td>
      <td>$179,700.00</td>
      <td>Per Annum</td>
      <td>ASSISTANT TO THE PRESIDENT FOR NATIONAL SECURI...</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Boney, Virginia M.</td>
      <td>Employee</td>
      <td>$115,000.00</td>
      <td>Per Annum</td>
      <td>SPECIAL ASSISTANT TO THE PRESIDENT FOR LEGISLA...</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Bonvillian, Marcus D.</td>
      <td>Employee</td>
      <td>$78,500.00</td>
      <td>Per Annum</td>
      <td>ASSOCIATE DIRECTOR,</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Bottari, Joseph U.</td>
      <td>Employee</td>
      <td>$52,000.00</td>
      <td>Per Annum</td>
      <td>STAFF ASSISTANT</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Brady, Lillie J.</td>
      <td>Detailee</td>
      <td>$56,233.00</td>
      <td>Per Annum</td>
      <td>POLICY ASSISTANT</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Braid, Duncan M.</td>
      <td>Employee</td>
      <td>$63,200.00</td>
      <td>Per Annum</td>
      <td>DIRECTOR OF RESEARCH FOR PRESIDENTIAL PERSONNEL</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Bremberg, Andrew P.</td>
      <td>Employee</td>
      <td>$179,700.00</td>
      <td>Per Annum</td>
      <td>ASSISTANT TO THE PRESIDENT FOR DOMESTIC POLICY</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Brooke, Jr., Francis J.</td>
      <td>Employee</td>
      <td>$115,000.00</td>
      <td>Per Annum</td>
      <td>SPECIAL ASSISTANT TO THE PRESIDENT FOR ECONOMI...</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Brooke, Mary J.</td>
      <td>Employee</td>
      <td>$109,900.00</td>
      <td>Per Annum</td>
      <td>SUPERVISOR FOR RECORDS MANAGEMENT</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Brooks, John H.</td>
      <td>Detailee</td>
      <td>$179,700.00</td>
      <td>Per Annum</td>
      <td>POLICY ADVISOR</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Brown, Debra S.</td>
      <td>Employee</td>
      <td>$92,600.00</td>
      <td>Per Annum</td>
      <td>CALLIGRAPHER</td>
    </tr>
  </tbody>
</table>


#### Now that you have a dataframe \...

You can do everything else you would normally do in pandas such as clean up the salary field so you can do some math on it. Below we remove the dollar sign and commas from the salary string and then convert it into a numeric column. Then we sort on that column to put the highest salary on the page at the top of our data and return the top five highest paid on the page.

``` python
df['salary_num'] = df['salary'] \
    .str \
    .replace('$', '', regex=True) \
    .str \
    .replace(',', '', regex=True)

df['salary_num'] = pd.to_numeric(df['salary_num'])

df \
    .sort_values(by=['salary_num'], ascending=False) \
    .head(5)
```


<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>status</th>
      <th>salary</th>
      <th>pay</th>
      <th>position</th>
      <th>salary_num</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>31</th>
      <td>Brooks, John H.</td>
      <td>Detailee</td>
      <td>$179,700.00</td>
      <td>Per Annum</td>
      <td>POLICY ADVISOR</td>
      <td>179700.0</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Bremberg, Andrew P.</td>
      <td>Employee</td>
      <td>$179,700.00</td>
      <td>Per Annum</td>
      <td>ASSISTANT TO THE PRESIDENT FOR DOMESTIC POLICY</td>
      <td>179700.0</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Bolton, John R.</td>
      <td>Employee</td>
      <td>$179,700.00</td>
      <td>Per Annum</td>
      <td>ASSISTANT TO THE PRESIDENT FOR NATIONAL SECURI...</td>
      <td>179700.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Bekkering, Michelle A.</td>
      <td>Detailee</td>
      <td>$143,100.00</td>
      <td>Per Annum</td>
      <td>POLICY ADVISOR</td>
      <td>143100.0</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Amin, Stacy C.</td>
      <td>Employee</td>
      <td>$140,000.00</td>
      <td>Per Annum</td>
      <td>ASSOCIATE COUNSEL TO THE PRESIDENT</td>
      <td>140000.0</td>
    </tr>
  </tbody>
</table>


``` python
```


## Next steps: `pdfplumber` example

This short notebook shows you one way you can wrangle some of the data we extracted using the CLIs in the tutorial.

If you want a more detailed `pdfplumber` tutorial, please refer to Jeremy Singer-Vine\'s great documentation found [here](https://github.com/jsvine/pdfplumber).

#### Import `pdfplumber` and `pandas`

We\'ll use pdfplumber to extract our tabular data into a list of lists. We\'ll then use `pandas` to turn that into a dataframe.

``` python
import pdfplumber
import pandas as pd
from pathlib import Path
```

#### Open our pdf using `pdfplumber`

We\'ll be using the `out.pdf` we created from the image PDF of White House salary data.

``` python
repo_path = Path().parent.resolve().parent

pdf_path = f'{repo_path}/files/single_img/out.pdf'

pdf = pdfplumber.open(pdf_path)
```

#### Example of table extraction

Below are some functions that uses `pdfplumber`\'s `extract_table` and `extract_words`. This example is slightly more complicated because we are using a searchable PDF created by OCR. These types of PDFs don\'t often have the lines, curves and rects that pdfplumber uses to parsed computer-generated text.

Instead, we are using the pixel position of each word and the structure of the PDF to pass in explicit lines where each column should be separated based on our own visual inspection of the document.

There are many ways you can find these pixel values.

A few common ones below:

1.  You can use Preview\'s Inspector and Rectangle Selection tools in the Tools menu. Drawing a rectangle with the left side of the box where you think the line should go will yield the pixel position in the \"Left\" box in the inspector as you draw.

2.  You can use `pdfplumber`\'s built-in visual debugging tools that allow you to view the pdf page in the Jupyter notebook and draw lines where the columns should be separated. Then you record the pixels in the list as we do below.

3.  You can look for the column headers using `pdfplumber`\'s `extract_words`. For example, if the column header words are unique, you could loop through all the words, add some logic to identify them and then assemble the vlines from the `x0` values. (See below with some caveats because the OCR\'d pdf isn\'t perfect).

I strongly suggest you familiarize yourself with `pdfplumber`\'s documention because it has many other tools and suggestions that can help extract much more complicated tables.

``` python
def create_settings(page, header_words):
    '''
    Accepts a pdf page
    Accepts a list of column header words
    Outputs a table settings dict with vlines
    '''
    padding = 3 # Give some extra space on the left because the headers are slightly off center.
    vlines = [77, 810] # Set the first and last value because of some quirks with the OCR
    words = page.extract_words()
    [vlines.append(word['x0'] - padding) for word in words if word['text'].lower() in header_words]
    vlines.sort()
    ts = {
            "vertical_strategy": "explicit", 
            "horizontal_strategy": "text",
            "explicit_vertical_lines": vlines,
    }
    return ts


def extract_salaries(page, ts, cols):
    '''
    Accepts a pdf page with a table of salary data
    Accepts a list of vertical lines that divide the data columns
    Accepts a dictionary of table settings
    Accepts a list of columns to slap on the DataFrame as headers
    Outputs a pandas DataFrame
    '''
    data = []
    table = page.extract_table(table_settings=ts)
    [data.append(row) for row in table if row[0] != '']
    return pd.DataFrame(data, columns=cols)


cols = [
    'name',
    'status',
    'salary',
    'pay',
    'position'
]

page = pdf.pages[0]

ts = create_settings(page, cols)

df = extract_salaries(page, ts, cols)

df
```


<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>status</th>
      <th>salary</th>
      <th>pay</th>
      <th>position</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Amin, Stacy C.</td>
      <td>Employee</td>
      <td>$140,000.00</td>
      <td>Per Annum</td>
      <td>ASSOCIATE COUNSEL TO THE PRESIDENT</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Andersen, Whitney N.</td>
      <td>Employee</td>
      <td>$115,000.00</td>
      <td>Per Annum</td>
      <td>SPECIAL ASSISTANT TO THE PRESIDENT AND DIRECTO...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Anderson, Alexander J.</td>
      <td>Employee</td>
      <td>$78,500.00</td>
      <td>Per Annum</td>
      <td>DIRECTOR OF VIDEO PRODUCTION</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Angelson, Alexander J.</td>
      <td>Employee</td>
      <td>$115,000.00</td>
      <td>Per Annum</td>
      <td>SPECIAL ASSISTANT TO THE PRESIDENT FOR LEGISLA...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Assefi, Camellia N.</td>
      <td>Employee</td>
      <td>$47,900.00</td>
      <td>Per Annum</td>
      <td>WRITER FOR PRESIDENTIAL CORRESPONDENCE</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Assefi, Omeed A.</td>
      <td>Employee</td>
      <td>$78,500.00</td>
      <td>Per Annum</td>
      <td>ASSISTANT SPECIAL COUNSEL</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Baitel, Rachael</td>
      <td>Employee</td>
      <td>$71,300.00</td>
      <td>Per Annum</td>
      <td>EXECUTIVE ASSISTANT</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Baker, Brittany G.</td>
      <td>Employee</td>
      <td>$63,200.00</td>
      <td>Per Annum</td>
      <td>EXECUTIVE ASSISTANT</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Baldwin, Brittany L.</td>
      <td>Employee</td>
      <td>$95,000.00</td>
      <td>Per Annum</td>
      <td>SPECIAL ASSISTANT TO THE PRESIDENT AND SPEECHW...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Beattie, Darren J.</td>
      <td>Employee</td>
      <td>$84,600.00</td>
      <td>Per Annum</td>
      <td>SPEECHWRITER AND POLICY DEVELOPMENT AIDE</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Beatty, Julia-Grace D.</td>
      <td>Employee</td>
      <td>$42,800.00</td>
      <td>Per Annum</td>
      <td>STAFF ASSISTANT</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Bekkering, Michelle A.</td>
      <td>Detailee</td>
      <td>$143,100.00</td>
      <td>Per Annum</td>
      <td>POLICY ADVISOR</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Beley, James P.</td>
      <td>Employee</td>
      <td>$63,200.00</td>
      <td>Per Annum</td>
      <td>DIRECTOR OF WRITERS FOR PRESIDENTIAL CORRESPON...</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Berkowitz, Avrahm J.</td>
      <td>Employee</td>
      <td>$130,000.00</td>
      <td>Per Annum</td>
      <td>SPECIAL ASSISTANT TO THE PRESIDENT AND ASSISTA...</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Biddle, Emily K.</td>
      <td>Employee</td>
      <td>$78,500.00</td>
      <td>Per Annum</td>
      <td>DEPUTY SOCIAL SECRETARY</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Bis, Justin B.</td>
      <td>Employee</td>
      <td>$71,300.00</td>
      <td>Per Annum</td>
      <td>PRINCIPAL DEPUTY ASSOCIATE DIRECTOR FOR PRESID...</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Blair, Patricia A.</td>
      <td>Employee</td>
      <td>$104,200.00</td>
      <td>Per Annum</td>
      <td>CHIEF CALLIGRAPHER</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Blase, Brian C.</td>
      <td>Employee</td>
      <td>$140,000.00</td>
      <td>Per Annum</td>
      <td>SPECIAL ASSISTANT TO THE PRESIDENT FOR ECONOMI...</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Block, Monica J.</td>
      <td>Employee</td>
      <td>$140,000.00</td>
      <td>Per Annum</td>
      <td>SPECIAL ASSISTANT TO THE PRESIDENT AND DEPUTY ...</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Blount, Mallory N.</td>
      <td>Employee</td>
      <td>$52,000.00</td>
      <td>Per Annum</td>
      <td>DIRECTOR OF DIGITAL RESPONSE FOR PRESIDENTIAL ...</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Blount, Patricia H.</td>
      <td>Employee</td>
      <td>$63,000.00</td>
      <td>Per Annum</td>
      <td>RECORDS MANAGEMENT ANALYST</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Bock, Caroline E.</td>
      <td>Employee</td>
      <td>$115,000.00</td>
      <td>Per Annum</td>
      <td>SPECIAL ASSISTANT TO THE PRESIDENT AND ASSOCIA...</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Bolton, John R.</td>
      <td>Employee</td>
      <td>$179,700.00</td>
      <td>Per Annum</td>
      <td>ASSISTANT TO THE PRESIDENT FOR NATIONAL SECURI...</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Boney, Virginia M.</td>
      <td>Employee</td>
      <td>$115,000.00</td>
      <td>Per Annum</td>
      <td>SPECIAL ASSISTANT TO THE PRESIDENT FOR LEGISLA...</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Bonvillian, Marcus D.</td>
      <td>Employee</td>
      <td>$78,500.00</td>
      <td>Per Annum</td>
      <td>ASSOCIATE DIRECTOR,</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Bottari, Joseph U.</td>
      <td>Employee</td>
      <td>$52,000.00</td>
      <td>Per Annum</td>
      <td>STAFF ASSISTANT</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Brady, Lillie J.</td>
      <td>Detailee</td>
      <td>$56,233.00</td>
      <td>Per Annum</td>
      <td>POLICY ASSISTANT</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Braid, Duncan M.</td>
      <td>Employee</td>
      <td>$63,200.00</td>
      <td>Per Annum</td>
      <td>DIRECTOR OF RESEARCH FOR PRESIDENTIAL PERSONNEL</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Bremberg, Andrew P.</td>
      <td>Employee</td>
      <td>$179,700.00</td>
      <td>Per Annum</td>
      <td>ASSISTANT TO THE PRESIDENT FOR DOMESTIC POLICY</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Brooke, Jr., Francis J.</td>
      <td>Employee</td>
      <td>$115,000.00</td>
      <td>Per Annum</td>
      <td>SPECIAL ASSISTANT TO THE PRESIDENT FOR ECONOMI...</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Brooke, Mary J.</td>
      <td>Employee</td>
      <td>$109,900.00</td>
      <td>Per Annum</td>
      <td>SUPERVISOR FOR RECORDS MANAGEMENT</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Brooks, John H.</td>
      <td>Detailee</td>
      <td>$179,700.00</td>
      <td>Per Annum</td>
      <td>POLICY ADVISOR</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Brown, Debra S.</td>
      <td>Employee</td>
      <td>$92,600.00</td>
      <td>Per Annum</td>
      <td>CALLIGRAPHER</td>
    </tr>
  </tbody>
</table>


#### Now that you have a dataframe \...

You can do everything else you would normally do in pandas such as clean up the salary field so you can do some math on it. Below we remove the dollar sign and commas from the salary string and then convert it into a numeric column. Then we sort on that column to put the highest salary on the page at the top of our data and return the top five highest paid on the page.

``` python
df['salary_num'] = df['salary'] \
    .str \
    .replace('$', '', regex=True) \
    .str \
    .replace(',', '', regex=True)

df['salary_num'] = pd.to_numeric(df['salary_num'])

df \
    .sort_values(by=['salary_num'], ascending=False) \
    .head(5)
```


<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>status</th>
      <th>salary</th>
      <th>pay</th>
      <th>position</th>
      <th>salary_num</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>31</th>
      <td>Brooks, John H.</td>
      <td>Detailee</td>
      <td>$179,700.00</td>
      <td>Per Annum</td>
      <td>POLICY ADVISOR</td>
      <td>179700.0</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Bremberg, Andrew P.</td>
      <td>Employee</td>
      <td>$179,700.00</td>
      <td>Per Annum</td>
      <td>ASSISTANT TO THE PRESIDENT FOR DOMESTIC POLICY</td>
      <td>179700.0</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Bolton, John R.</td>
      <td>Employee</td>
      <td>$179,700.00</td>
      <td>Per Annum</td>
      <td>ASSISTANT TO THE PRESIDENT FOR NATIONAL SECURI...</td>
      <td>179700.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Bekkering, Michelle A.</td>
      <td>Detailee</td>
      <td>$143,100.00</td>
      <td>Per Annum</td>
      <td>POLICY ADVISOR</td>
      <td>143100.0</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Amin, Stacy C.</td>
      <td>Employee</td>
      <td>$140,000.00</td>
      <td>Per Annum</td>
      <td>ASSOCIATE COUNSEL TO THE PRESIDENT</td>
      <td>140000.0</td>
    </tr>
  </tbody>
</table>


``` python
```



## Local installation instructions

### Install dependencies

```
make venv
```

### Test that the installation worked

```
make test
```

... should not throw an error.


## Running Jupyter Lab

```
make lab
```



## First things first

#### Load the library

``` python
import pdfplumber
```

#### Open the PDF

``` python
pdf = pdfplumber.open("../pdfs/00-hello-world.pdf")
```

#### How many pages in the PDF?

``` python
len(pdf.pages)
```


#### Select that first/only page

``` python
page = pdf.pages[0]
page
```

    <Page:1>


## Now let\'s extract the text

``` python
page.extract_text()
```

    'Hello, World!'



## Where does that text come from?

The `page.chars` list:

``` python
len(page.chars)
```


``` python
[char["text"] for char in page.chars]
```

    ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']

#### What does an individual character look like?

``` python
page.chars[0]
```

    {'matrix': (1, 0, 0, 1, 50, 260),
     'fontname': 'Times-Roman',
     'adv': 25.991999999999997,
     'upright': True,
     'x0': 50.0,
     'y0': 252.188,
     'x1': 75.99199999999999,
     'y1': 288.188,
     'width': 25.99199999999999,
     'height': 36.0,
     'size': 36.0,
     'mcid': None,
     'tag': None,
     'object_type': 'char',
     'page_number': 1,
     'ncs': 'DeviceRGB',
     'text': 'H',
     'stroking_color': None,
     'stroking_pattern': None,
     'non_stroking_color': (0.2, 0.5, 0.2),
     'non_stroking_pattern': None,
     'top': 31.812000000000012,
     'bottom': 67.81200000000001,
     'doctop': 31.812000000000012}


## Let\'s examine the graphical features

(I.e., lines, rectangles, and \"curves\")

#### Lines

``` python
page.lines
```

    [{'x0': 50,
      'y0': 160,
      'x1': 350,
      'y1': 160,
      'width': 300,
      'height': 0,
      'pts': [(50, 160), (350, 160)],
      'linewidth': 0,
      'stroke': True,
      'fill': False,
      'evenodd': False,
      'stroking_color': None,
      'non_stroking_color': None,
      'mcid': None,
      'tag': None,
      'object_type': 'line',
      'page_number': 1,
      'stroking_pattern': None,
      'non_stroking_pattern': None,
      'top': 160,
      'bottom': 160,
      'doctop': 160},
     {'x0': 50,
      'y0': 140,
      'x1': 350,
      'y1': 140,
      'width': 300,
      'height': 0,
      'pts': [(50, 180), (350, 180)],
      'linewidth': 0,
      'stroke': True,
      'fill': False,
      'evenodd': False,
      'stroking_color': None,
      'non_stroking_color': None,
      'mcid': None,
      'tag': None,
      'object_type': 'line',
      'page_number': 1,
      'stroking_pattern': None,
      'non_stroking_pattern': None,
      'top': 180,
      'bottom': 180,
      'doctop': 180}]

#### Rectangles

``` python
page.rects
```

    [{'x0': 50,
      'y0': 200,
      'x1': 250,
      'y1': 220,
      'width': 200,
      'height': 20,
      'pts': [(50, 120), (250, 120), (250, 100), (50, 100)],
      'linewidth': 0,
      'stroke': True,
      'fill': True,
      'evenodd': False,
      'stroking_color': (0.25, 0.25, 0.25),
      'non_stroking_color': (0.9, 0.9, 0.9),
      'mcid': None,
      'tag': None,
      'object_type': 'rect',
      'page_number': 1,
      'stroking_pattern': None,
      'non_stroking_pattern': None,
      'top': 100,
      'bottom': 120,
      'doctop': 100}]

#### "Curves"

(Curves are paths that `(a)` have more than 1 point, and `(b)` do not form a rectangle.)

``` python
page.curves
```

    [{'x0': 50,
      'y0': 50,
      'x1': 150,
      'y1': 100,
      'width': 100,
      'height': 50,
      'pts': [(50, 220), (70, 270), (90, 220), (110, 270), (130, 220), (150, 270)],
      'linewidth': 2,
      'stroke': True,
      'fill': False,
      'evenodd': False,
      'stroking_color': None,
      'non_stroking_color': None,
      'mcid': None,
      'tag': None,
      'object_type': 'curve',
      'page_number': 1,
      'stroking_pattern': None,
      'non_stroking_pattern': None,
      'top': 220,
      'bottom': 270,
      'doctop': 220}]



## Let\'s use the visual debugging tools

The first step is to create an image of the page:

``` python
im = page.to_image()
im
```


From there, we can use the image object\'s various `.draw_*` methods to see what the PDF parser sees. For example:

#### Flag the `.chars`

``` python
im.draw_rects(page.chars)
```


#### Reset the image

The things we draw on the page accumulate \... until we call the image\'s `.reset()` method:

``` python
im.reset()
```


#### Flag the `.rects`

We can also adjust the stroke color/width and fill color, like so:

``` python
im.reset()
im.draw_rects(
    page.rects,
    stroke="orange",  # Colors can be (standard) names
    fill=(0, 255, 0, 50),  # or RGB(A) tuples, with values 0–255
    stroke_width=3,
)
```


#### Flag the `.curves`

``` python
im.reset()
im.draw_rects(page.curves)
```



## One more key feature: Cropping

When you\'re parsing a PDF, you often want to focus on just one region of the document. The `page.crop(bounding_box)` method lets you do that.

The method expects to receive a bounding box in the format `(x0, top, x1, bottom)`. Here\'s an arbitrary example:

``` python
bbox = (10, 30, 150, 300)

page.crop(bbox).to_image()
```


A more useful technique is to base the bounding box on information you extract from the PDF itself. For instance:

``` python
curve = page.curves[0]

curve_bbox = pdfplumber.utils.obj_to_bbox(curve)

print(curve_bbox)
```

    (50, 220, 150, 270)

``` python
page.crop(curve_bbox).to_image()
```


We\'ll use this technique, and others, in the [next notebook](./01-practice.ipynb).


------------------------------------------------------------------------

------------------------------------------------------------------------

------------------------------------------------------------------------



## First things first

#### Load the library (and a couple of others)

``` python
import re

import pandas as pd
import pdfplumber
```

#### Open the PDF

``` python
pdf = pdfplumber.open("../pdfs/01-practice.pdf")
```

#### How many pages in the PDF?

``` python
len(pdf.pages)
```


#### Select that first/only page

``` python
page = pdf.pages[0]
page
```

    <Page:1>


## What does the page look like?

``` python
im = page.to_image()
im
```




## Let\'s extract the text

#### The \"plain\" way, which we learned in the previous notebook

``` python
print(page.extract_text())
```

    Jungle Health and Safety Inspection Service
    INS-UP70N51NCL41R
    Site: Durham’s Meatpacking Chicago, Ill.
    Date: February 3, 1905
    Violation Count: 7
    Summary: Worst of any, however, were the fertilizer men, and those who served in the cooking rooms.
    These people could not be shown to the visitor - for the odor of a fertilizer man would scare any ordinary
    visitor at a hundred yards, and as for the other men, who worked in tank rooms full of steam, and in
    some of which there were open vats near the level of the floor, their peculiar trouble was that they fell
    into the vats; and when they were fished out, there was never enough of them left to be worth
    exhibiting - sometimes they would be overlooked for days, till all but the bones of them had gone out
    to the world as Durham’s Pure Leaf Lard!
    Violations
    Statute Description Level Repeat?
    4.12.7 Unsanitary Working Conditions. Critical
    5.8.3 Inadequate Protective Equipment. Serious
    6.3.9 Ineffective Injury Prevention. Serious
    7.1.5 Failure to Properly Store Hazardous Materials. Critical
    8.9.2 Lack of Adequate Fire Safety Measures. Serious
    9.6.4 Inadequate Ventilation Systems. Serious
    10.2.7 Insufficient Employee Training for Safe Work Practices. Serious
    Jungle Health and Safety Inspection Service

#### The \"layout\" way

If you set `layout=True`, then `.extract_text(...)` attempts to mimic the layout of the original text. As you\'ll see, it does a *decent* but not perfect job.

``` python
print(page.extract_text(layout=True))
```

                                                                                        
                                                                                        
                                                                                        
                                                         Jungle Health and Safety Inspection Service
                                                         INS-UP70N51NCL41R              
                                                                                        
           Site: Durham’s Meatpacking Chicago, Ill.                                     
                                                                                        
           Date: February 3, 1905                                                       
                                                                                        
           Violation Count: 7                                                           
           Summary: Worst of any, however, were the fertilizer men, and those who served in the cooking rooms.
           These people could not be shown to the visitor - for the odor of a fertilizer man would scare any ordinary
                                                                                        
           visitor at a hundred yards, and as for the other men, who worked in tank rooms full of steam, and in
           some of which there were open vats near the level of the floor, their peculiar trouble was that they fell
           into the vats; and when they were fished out, there was never enough of them left to be worth
           exhibiting - sometimes they would be overlooked for days, till all but the bones of them had gone out
           to the world as Durham’s Pure Leaf Lard!                                     
                                                                                        
                                                                                        
                                                                                        
                                                                                        
                                                                                        
                                                                                        
                                                                                        
                                                                                        
                                                                                        
                                                                                        
           Violations                                                                   
                                                                                        
            Statute Description                                    Level  Repeat?       
            4.12.7 Unsanitary Working Conditions.                  Critical             
                                                                                        
            5.8.3 Inadequate Protective Equipment.                 Serious              
            6.3.9 Ineffective Injury Prevention.                   Serious              
                                                                                        
            7.1.5 Failure to Properly Store Hazardous Materials.   Critical             
            8.9.2 Lack of Adequate Fire Safety Measures.           Serious              
                                                                                        
            9.6.4 Inadequate Ventilation Systems.                  Serious              
            10.2.7 Insufficient Employee Training for Safe Work Practices. Serious      
                                                                                        
                                                                                        
                                                                                        
                                                                                        
                                                                                        
                                                                                        
                                                                                        
                                                                                        
                                                                                        
                                                                                        
                                                                                        
                                                                                        
                                                                                        
                                                                                        
                                                                                        
                                                                                        
                                                                                        
                                    Jungle Health and Safety Inspection Service         


## Let\'s start visual debugging

Visual debugging is typically the first thing I do when I\'m working with a PDF for the first time.

First, let\'s examine the structural parts of the page: Where are the characters, rectangles, and lines?

#### Characters

``` python
im.reset().draw_rects(page.chars)
```


#### Rectangles

``` python
im.reset().draw_rects(page.rects)
```


#### Lines

``` python
im.reset().draw_lines(page.lines, stroke_width=2)
```


#### Here\'s something we haven\'t seen before: `.debug_tablefinder(...)`

`pdfplumber` comes with a set of features for identifying and extracting tables on a given page. `PageImage.debug_tablefinder(...)` shows you what the table-finding method sees:

``` python
im.reset().debug_tablefinder()
```




## Let\'s extract that table!

(Note: Not all tables are so simple and explicit. See `pdfplumber`\'s [table-extraction documentation](https://github.com/jsvine/pdfplumber#extracting-tables) to learn how to extract more difficult tables.)

#### All tables (in this example, there\'s only one)

``` python
page.extract_tables()
```

    [[['Statute', 'Description', 'Level', 'Repeat?'],
      ['4.12.7', 'Unsanitary Working Conditions.', 'Critical', ''],
      ['5.8.3', 'Inadequate Protective Equipment.', 'Serious', ''],
      ['6.3.9', 'Ineffective Injury Prevention.', 'Serious', ''],
      ['7.1.5', 'Failure to Properly Store Hazardous Materials.', 'Critical', ''],
      ['8.9.2', 'Lack of Adequate Fire Safety Measures.', 'Serious', ''],
      ['9.6.4', 'Inadequate Ventilation Systems.', 'Serious', ''],
      ['10.2.7',
       'Insufficient Employee Training for Safe Work Practices.',
       'Serious',
       '']]]

#### Just the largest table (and put it in a `pandas` `DataFrame`)

``` python
rows = page.extract_table()

pd.DataFrame(rows[1:], columns=rows[0])
```


<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Statute</th>
      <th>Description</th>
      <th>Level</th>
      <th>Repeat?</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4.12.7</td>
      <td>Unsanitary Working Conditions.</td>
      <td>Critical</td>
      <td></td>
    </tr>
    <tr>
      <th>1</th>
      <td>5.8.3</td>
      <td>Inadequate Protective Equipment.</td>
      <td>Serious</td>
      <td></td>
    </tr>
    <tr>
      <th>2</th>
      <td>6.3.9</td>
      <td>Ineffective Injury Prevention.</td>
      <td>Serious</td>
      <td></td>
    </tr>
    <tr>
      <th>3</th>
      <td>7.1.5</td>
      <td>Failure to Properly Store Hazardous Materials.</td>
      <td>Critical</td>
      <td></td>
    </tr>
    <tr>
      <th>4</th>
      <td>8.9.2</td>
      <td>Lack of Adequate Fire Safety Measures.</td>
      <td>Serious</td>
      <td></td>
    </tr>
    <tr>
      <th>5</th>
      <td>9.6.4</td>
      <td>Inadequate Ventilation Systems.</td>
      <td>Serious</td>
      <td></td>
    </tr>
    <tr>
      <th>6</th>
      <td>10.2.7</td>
      <td>Insufficient Employee Training for Safe Work P...</td>
      <td>Serious</td>
      <td></td>
    </tr>
  </tbody>
</table>



## Planning the rest of our extraction

What parts of the page do we want to grab? What strategies might we be able to use?

``` python
im.reset()
```




## Inspection ID

Let\'s start with the inspection ID, in the box at the top of the page. How might we get that?

With PDFs, there\'s often more than one option. Let\'s explore a few!

#### **Option 1**: Just extract the text and parse it out of there.

We might feel confident, perhaps, that the text will always look something like this:

    Jungle Health and Safety Inspection Service
    {Inspection ID}
    [...]

If that\'s a safe assumption, then straightforward text extraction should work fine. Here\'s the top part of the text:

``` python
text_simple = page.extract_text()
print(text_simple[:200])  # Printing just the initial chunk
```

    Jungle Health and Safety Inspection Service
    INS-UP70N51NCL41R
    Site: Durham’s Meatpacking Chicago, Ill.
    Date: February 3, 1905
    Violation Count: 7
    Summary: Worst of any, however, were the fertilizer men

\... which you could parse with a [regular expression](https://www.w3schools.com/python/python_regex.asp):

``` python
insp_num_pat = r"Jungle Health and Safety Inspection Service\s+([^\n]+)"

insp_num_match = re.search(insp_num_pat, text_simple)

print(insp_num_match.group(1))
```

    INS-UP70N51NCL41R

Huzzah! Alternatively, you could use `pdfplumber`\'s built-in `Page.search(...)` method:

``` python
search_results = page.search(insp_num_pat)

first_match = search_results[0]

print(first_match["groups"][0])
```

    INS-UP70N51NCL41R

   

#### **Option 2**: Cropping

What if you weren\'t so sure about that textual pattern? Maybe `Jungle Health and Safety Inspection Service` isn\'t the only inspection agency in your pile of PDFs? Or maybe there\'s sometimes a second line of text before the inspection number?

How about the box surrounding it? From the debugging we did above, we know that the box is defined as a rectangle, and perhaps we\'re pretty sure it\'ll always be the first one on the page. So let\'s take these steps, using the `Page.crop(...)` method we learned in the previous notebook:

1.  Select the rectangle
2.  Grab the rectangle\'s bounding box
3.  Pass the bounding box to `page.crop(...)`
4.  Extract the text

``` python
top_rect = page.rects[0]

top_rect_bbox = (top_rect["x0"], top_rect["top"], top_rect["x1"], top_rect["bottom"])

# Alternatively:
# top_rect_bbox = pdfplumber.utils.obj_to_bbox(top_rect)

print(top_rect_bbox)
```

    (375, 27, 555, 62)

``` python
top_rect_cropped = page.crop(top_rect_bbox)
```

Let\'s check that the crop looks like what we intended:

``` python
# Here, we pass an argument that increases the dimensions, for easier viewing
top_rect_cropped.to_image(resolution=150)
```


Great. Now, we can extract:

``` python
top_rect_text = top_rect_cropped.extract_text()

print(top_rect_text)
```

    Jungle Health and Safety Inspection Service
    INS-UP70N51NCL41R

\... and grab the second line:

``` python
print(top_rect_text.split("\n")[-1])
```

    INS-UP70N51NCL41R

   

#### **Option 3**: Filtering on character attributes

What if you weren\'t so sure about that, either? Maybe there\'s not always a box around the text, or maybe the inspection number sometimes comes *before* the agency name.

Perhaps you\'re more confident that, whatever the rest of the pattern, the inspection number will always show up in red? Let\'s try that.

Text and graphical objects can have two types of colors: `stroking_color` (the outline) and `non_stroking_color` (the fill). With text, you\'re almost always looking for the `non_stroking_color`.

Let\'s see what `non_stroking_color`s our text has:

``` python
char_colors = pd.DataFrame(page.chars)["non_stroking_color"].astype(str)

char_colors.value_counts()
```

    non_stroking_color
    (0,)         688
    None         504
    (1, 0, 0)     17
    (0.5,)        13
    Name: count, dtype: int64

As you can see, there are a few ways to specify color in PDFs. Let\'s break these down:

- `None`: The default color, black.
- `0`: A one-number specification refers to a grayscale color, on a continuum running from 0 (black) to 1 (white).
- `0.5`: Ditto. In this case, `0.5` is a gray halfway between white and black.
- `(1, 0, 0)`: A three-number tuple refers to an RGB color, with values for each item ranging from 0 to 1. This one here stands for full-red.

We\'re pretty sure it\'s last one we want, but let\'s make sure by using the visual debugging feature:

``` python
red_chars = [c for c in page.chars if c["non_stroking_color"] == (1, 0, 0)]

im.reset().draw_rects(red_chars)
```


Great! Now let\'s extract that, using a new method we haven\'t seen before: `Page.filter(...)`.

`Page.filter(...)` takes a function that will return `True` for objects we want to keep and `False` for those we want to ditch. So let\'s write that function and try it:

``` python
def is_red(obj):
    return obj.get("non_stroking_color") == (1, 0, 0)


filtered_page = page.filter(is_red)

print(filtered_page.extract_text())
```

    INS-UP70N51NCL41R

It worked!


## Date, site, and violation count

For these fields, which each seem to be single-lined, we can probably safely just search by regular expression:

``` python
print(page.search(r"\nDate:\s+(.+?)\n")[0]["groups"][0])
```

    February 3, 1905

``` python
print(page.search(r"\nSite:\s+(.+?)\n")[0]["groups"][0])
```

    Durham’s Meatpacking Chicago, Ill.

``` python
print(page.search(r"\nViolation Count:\s+(.+?)\n")[0]["groups"][0])
```


Extra credit: How might you separate the site name (`Durham’s Meatpacking`) from its location (`Chicago, Ill.`)?



## Summary text

There\'s basically (other than the extra credit below), just one other part we need to grab: The summary text. Unlike the other chunks of text, it\'s multiline. We *could* use the `.search(...)` method above \... but where would we stop? We could stop at \"Violations\" \... but can we be sure that the summary text itself doesn\'t use that phrase?

Instead, let\'s try combining a few of the techniques we\'ve picked up so far. We\'ll do this:

1.  Identify where the summary begins
2.  Identify the position of the horizontal line that separates the summary text from the violations section
3.  Crop the page based on that information
4.  Extract the text

#### Identify where the summary begins

`.search(...)` results each have positional information (`x0`, `top`, etc.) similar to other objects:

``` python
summary_match = page.search(r"\nSummary:")[0]

summary_match["top"]
```

    144.07000000000005

``` python
summary_bbox = pdfplumber.utils.obj_to_bbox(summary_match)

summary_bbox
```

    (50.0, 144.07000000000005, 98.9, 154.07000000000005)

#### Identify the position of the horizontal line

There are a number of ways to identify a line; in this case, we\'ll take advantage of the fact, that it\'s the only line that\'s 2 units thick:

``` python
pd.Series([x["linewidth"] for x in page.lines]).value_counts()
```

    0.0    14
    0.5     6
    2.0     1
    Name: count, dtype: int64

``` python
dividing_line = [x for x in page.lines if x["linewidth"] == 2][0]
dividing_line
```

    {'x0': 50,
     'y0': 440,
     'x1': 550,
     'y1': 440,
     'width': 500,
     'height': 0,
     'pts': [(50, 352), (550, 352)],
     'linewidth': 2,
     'stroke': True,
     'fill': False,
     'evenodd': False,
     'stroking_color': (0,),
     'non_stroking_color': None,
     'mcid': None,
     'tag': None,
     'object_type': 'line',
     'page_number': 1,
     'stroking_pattern': None,
     'non_stroking_pattern': None,
     'top': 352,
     'bottom': 352,
     'doctop': 352}

#### Let\'s confirm we got what we wanted

``` python
im.reset()

im.draw_rect(summary_bbox)

im.draw_line(dividing_line, stroke_width=3)
```


#### Crop the page based on that information

``` python
summary_crop = page.crop(
    (
        0,  # The left side of the page
        summary_match["top"],  # The top of the "Summary:" match
        page.width,  # The right side of the page
        dividing_line["top"],  # The top of the dividing line
    )
)

summary_crop.to_image()
```


#### Extract the text

``` python
print(summary_crop.extract_text())
```

    Summary: Worst of any, however, were the fertilizer men, and those who served in the cooking rooms.
    These people could not be shown to the visitor - for the odor of a fertilizer man would scare any ordinary
    visitor at a hundred yards, and as for the other men, who worked in tank rooms full of steam, and in
    some of which there were open vats near the level of the floor, their peculiar trouble was that they fell
    into the vats; and when they were fished out, there was never enough of them left to be worth
    exhibiting - sometimes they would be overlooked for days, till all but the bones of them had gone out
    to the world as Durham’s Pure Leaf Lard!


## Extra-extra credit

In the violations table, how might you determine which rows have the `Repeat?` box checked?


------------------------------------------------------------------------

------------------------------------------------------------------------

------------------------------------------------------------------------



## Session description
In this session, you'll learn how to analyze data using the popular Python data analysis library pandas. You'll learn about the benefits of scripting your data projects and enough syntax to load, sort, filter and group a data set.

This class is good for: People who are comfortable working with data in spreadsheets or SQL and want to make the leap to programming.


## Session goals
Attendees should leave with a basic understanding of:
- How to write and run Python code in a Jupyter notebook
- When it makes sense to script your analysis (as opposed to just using Excel, SQL, etc.)
- Loading a CSV into a `pandas` dataframe
- Inspecting the dataframe with `head()`, `describe()` and other methods
- Sorting data with `sort_values()`
- Filtering data
- Grouping data (if time)
- Where to find [instructions for installing Python on their own machines](https://docs.google.com/document/d/1cYmpfZEZ8r-09Q6Go917cKVcQk_d0P61gm0q8DAdIdg/edit#)
- How to find help when they get stuck



## General approach
I Do, We Do, You Do. Demonstrate a concept, go through it together, then give them plenty of time to experiment on their own while you and your coach walk around and answer questions (see sections marked `✍️ Try it yourself`). The pace will be slower than you think, and that's OK! It's not the end of the world if you don't get through everything.

Most people who come to this class will have _zero_ experience with programming, so be empathetic and try to remember how frustrating it is to feel lost.

Having the students open [the included syntax reference notebook](Python%20syntax%20cheat%20sheet.ipynb) can be useful for reinforcing Python basics. 


## Class setup
We'll have the latest version of Python 3 installed. We're using the standard library's `venv` module to manage the virtual environment and project dependencies (`jupyterlab` and `pandas`), which will already have been installed and tested prior to your session. Please refer to the Python setup sheet for the conference and let us know if you have any questions.



## Class outline

### Start up the notebook server
Begin the class by (slowly!) walking everyone through the process of activating their virtual environments and launching Jupyter:
1. Open Terminal (or `cmd` or `Cygwin` if you're on a PC)
2. `cd` into your class directory
3. Activate the virtual environment:
    - Macs: `source env/bin/activate`
    - PCs: `.\env\Scripts\activate`
4. `jupyter lab`

It will take everyone a few minutes to get going. You'll also probably get some questions about what, exactly, you're doing at this step. Try to avoid a lengthy digression into virtual environments -- it's beyond the scope of this hourlong session, so maybe offer to talk to them after class, or send 'em our way: [training@ire.org](mailto:training@ire.org).

Once everyone is good to go, toggle back to the terminal and show them what's going on: A Jupyter server is running in the background, so don't close that terminal window!

Go over some notebook basics: Adding cells, writing code and running cells, etc. A common beginner gotcha: Writing code that other cells depend on but forgetting to first _run_ it to make it available.

### Main course content
Start marching down the notebook: Importing pandas, loading data from file, sorting, filtering, grouping. Pause frequently to ask if anyone has questions.

Any time you see `✍️ Try it yourself`, hit the brakes and give everyone time to play around with whatever concept you're discussing.

### Debugging
If you can, find an opportunity when someone has gotten an error and take 5 minutes to walk through basic debugging strategy: Reading the traceback error from bottom to top, strategic Googling, etc.

### If you have extra time at the end
Unlikely! But if you have extra time, oversee some unstructured lab time -- they can practice syntax or look up additional methods, find their own data to work with, etc.

### Ending the session
1. Have everyone close out of their notebook tabs
2. In terminal, `Ctrl+C` to kill the server process
3. Close the terminal window


## Run the notebook

You'll need Python 3 installed on your computer. [Here's our install guide](https://docs.google.com/document/d/1cYmpfZEZ8r-09Q6Go917cKVcQk_d0P61gm0q8DAdIdg/edit?usp=sharing).

1. Clone or [download/unzip](https://github.com/ireapps/teaching-guide-intro-to-pandas/archive/master.zip) this repo onto your computer
2. In your command-line interface, `cd` into the folder
3. Create a virtual environment:
    - Macs: `python3 -m venv env`
    - PCs: `python -m venv env`
4. Activate the virtual environment:
    - Macs: `source env/bin/activate`
    - PCs: `.\env\Scripts\activate`
5. `pip install -r requirements.txt`
6. `jupyter lab`



## Collections of data

Now we\'re going to talk about two ways you can use Python to group data into a collection: lists and dictionaries.

### Lists

A *list* is a comma-separated list of items inside square brackets: `[]`.

Here\'s a list of ingredients, each one a string, that together makes up a salsa recipe.

``` python
salsa_ingredients = ['tomato', 'onion', 'jalapeño', 'lime', 'cilantro']
```

To get an item out of a list, you\'d refer to its numerical position in the list \-- its *index* (1, 2, 3, etc.) \-- inside square brackets immediately following your reference to that list. In Python, as in many other programming languages, counting starts at 0. That means the first item in a list is item `0`.

``` python
salsa_ingredients[0]
```

``` python
salsa_ingredients[1]
```

You can use *negative indexing* to grab things from the right-hand side of the list \-- and in fact, `[-1]` is a common idiom for getting \"the last item in a list\" when it\'s not clear how many items are in your list.

``` python
salsa_ingredients[-1]
```

If you wanted to get a slice of multiple items out of your list, you\'d use colons (just like in Excel, kind of!).

If you wanted to get the first three items, you\'d do this:

``` python
salsa_ingredients[0:3]
```

You could also have left off the initial 0 \-- when you leave out the first number, Python defaults to \"the first item in the list.\" In the same way, if you leave off the last number, Python defaults to \"the last item in the list.\"

``` python
salsa_ingredients[:3]
```

Note, too, that this slice is giving us items 0, 1 and 2. The `3` in our slice is the first item we *don\'t* want. That can be kind of confusing at first. Let\'s try a few more:

``` python
# everything in the list except the first item
salsa_ingredients[1:]
```

``` python
# the second, third and fourth items
salsa_ingredients[1:4]
```

``` python
# the last two items
salsa_ingredients[-2:]
```

To see how many items are in a list, use the `len()` function:

``` python
len(salsa_ingredients)
```

To add an item to a list, use the [`append()`](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) method:

``` python
salsa_ingredients
```

``` python
salsa_ingredients.append('mayonnaise')
```

``` python
salsa_ingredients
```

Haha *gross*. To remove an item from a list, use the `pop()` method. If you don\'t specify the index number of the item you want to pop out, it will default to \"the last item.\"

``` python
salsa_ingredients.pop()
```

``` python
salsa_ingredients
```

You can use the [`in` and `not in`](https://docs.python.org/3/reference/expressions.html#membership-test-operations) expressions to test membership in a list (will return a boolean):

``` python
'lime' in salsa_ingredients
```

``` python
'cilantro' not in salsa_ingredients
```

### Dictionaries

A *dictionary* is a comma-separated list of key/value pairs inside curly brackets: `{}`. Let\'s make an entire salsa recipe:

``` python
salsa = {
    'ingredients': salsa_ingredients,
    'instructions': 'Chop up all the ingredients and cook them for awhile.',
    'oz_made': 12
}
```

To retrieve a value from a dictionary, you\'d refer to the name of its key inside square brackets `[]` immediately after your reference to the dictionary:

``` python
salsa['oz_made']
```

``` python
salsa['ingredients']
```

To add a new key/value pair to a dictionary, assign a new key to the dictionary inside square brackets and set the value of that key with `=`:

``` python
salsa['tastes_great'] = True
```

``` python
salsa
```

To delete a key/value pair out of a dictionary, use the `del` command and reference the key:

``` python
del salsa['tastes_great']
```

``` python
salsa
```

### Indentation

Whitespace matters in Python. Sometimes you\'ll need to indent bits of code to make things work. This can be confusing! `IndentationError`s are common even for experienced programmers. (FWIW, Jupyter will try to be helpful and insert the correct amount of \"significant whitespace\" for you.)

You can use tabs or spaces, just don\'t mix them. [The Python style guide](https://www.python.org/dev/peps/pep-0008/) recommends indenting your code in groups of four spaces, so that\'s what we\'ll use.

### `for` loops

You would use a `for` loop to iterate over a collection of things. The statement begins with the keyword `for` (lowercase), then a temporary `variable_name` of your choice to represent each item as you loop through the collection, then the Python keyword `in`, then the collection you\'re looping over (or its variable name), then a colon, then the indented block of code with instructions about what to do with each item in the collection.

Let\'s say we have a list of numbers that we assign to the variable `list_of_numbers`.

``` python
list_of_numbers = [1, 2, 3, 4, 5, 6]
```

We could loop over the list and print out each number:

``` python
for number in list_of_numbers:
    print(number)
```

We could print out each number *times 6*:

``` python
for number in list_of_numbers:
    print(number*6)
```

\... whatever you need to do in you loop. Note that the variable name `number` in our loop is totally arbitrary. This also would work:

``` python
for banana in list_of_numbers:
    print(banana)
```

It can be hard, at first, to figure out what\'s a \"Python word\" and what\'s a variable name that you get to define. This comes with practice.

Strings are iterable, too. Let\'s loop over the letters in a sentence:

``` python
sentence = 'Hello, IRE/NICAR!'

for letter in sentence:
    print(letter)
```

To this point: Strings are iterable, like lists, so you can use the same kinds of methods:

``` python
# get the first five characters
sentence[:5]
```

``` python
# get the length of the sentence
len(sentence)
```

``` python
'Hello' in sentence
```

You can iterate over dictionaries, too \-- just remember that dictionaries *don\'t keep track of the order that items were added to it*.

When you\'re looping over a dictionary, the variable name in your `for` loop will refer to the keys. Let\'s loop over our `salsa` dictionary from up above to see what I mean.

``` python
for key in salsa:
    print(key)
```

To get the *value* of a dictionary item in a for loop, you\'d need to use the key to retrieve it from the dictionary:

``` python
for key in salsa:
    print(salsa[key])
```

### `if` statements

Just like in Excel, you can use the \"if\" keyword to handle conditional logic.

These statements begin with the keyword `if` (lowercase), then the condition to evaluate, then a colon, then a new line with a block of indented code to execute if the condition resolves to `True`.

``` python
if 4 < 6:
    print('4 is less than 6')
```

You can also add an `else` statement (and a colon) with an indented block of code you want to run if the condition resolves to `False`.

``` python
if 4 > 6:
    print('4 is greater than 6?!')
else:
    print('4 is not greater than 6.')
```

If you need to, you can add multiple conditions with `elif`.

``` python
HOME_SCORE = 6
AWAY_SCORE = 8

if HOME_SCORE > AWAY_SCORE:
    print('we won!')
elif HOME_SCORE == AWAY_SCORE:
    print('we tied!')
else:
    print('we lost!')
```


## Table of contents

* `pipeline.ipynb` => the working notebook you'll write your code in during the class
* `pipeline-finished.ipynb` => the completed notebook we've prepped ahead of time
* `google sheetes code.ipynb` => \*bonus\* code to publish your csv to a Google Sheet
* `.github/workflows/main.yaml` => Github actions file to run your notebook once every 12 hours
* `requirements.txt` => the Python libraries you need for the notebooks to run (these should be pre-installed on the NICAR computers)



## Intro 

### What We're Doing

In this hourlong session, we're going to show you two things:

**1. The many ways to get data in RStudio!**
* *We'll practice loading data from:* a built in R dataset, an R package, a local csv, an Excel file, and an html table. If the wifi cooperates, we'll also show how to load from a csv on the web and read in a Google Sheet.
* *I'll introduce you to resources that will show you how to:* pull data from an API (like the Census), and pull data from a database. 

**2. Some data cleaning tricks in R!**
* *We'll practice:* cleaning up column names, correcting erroneous values, converting data types, manipulating strings. 

### What You'll Get Out of This

* You won't leave here an expert.  
* You will leave here understanding some basic loading and cleaning data concepts in R, a list of helpful packages, and some resources for further learning. 


## Let's go

### Set your working directory

We'll want to set our working directory inside of the notebooks folder.  I'll show you how to do that in RStudio. 

### Load packages

We'll need to load several packages for this class.  

They are:
* The [babynames](https://cran.r-project.org/web/packages/babynames/index.html) package for loading social security babyname data. 
* The [Tidvyerse](https://www.tidyverse.org/) collection of packages. We'll be making extensive use of the readr, dplyr and stringr packages,which all load as part of the tidyverse core.  
  * [readr](https://readr.tidyverse.org/)
  * [dplyr](https://dplyr.tidyverse.org/)
  * [stringr](https://stringr.tidyverse.org/)
* The [rvest](http://rvest.tidyverse.org/) package for web scraping.
* The [janitor](https://github.com/sfirke/janitor) package for data cleaning. 
* The [readxl](https://readxl.tidyverse.org/) package for loading Excel files. 
* The [googlesheets4](https://googlesheets4.tidyverse.org/) package for reading -- and writing -- data stored in a Google Sheet. 


```{r}


## Install packages if you need them by uncommenting these lines
#install.packages('babynames')
#install.packages('tidyverse')
#install.packages('rvest')
#install.packages('janitor')
#install.packages('readxl')
#install.packages('googlesheets4')
#install.packages('babynames')

# Turn off scientific notation
options(scipen=999)

# Load libraries
library(tidyverse)
library(rvest)
library(janitor)
library(readxl)
library(googlesheets4)
library(babynames)
library(lubridate)


```

### Loading preloaded data from a package

If you've taken earlier classes in this sequence, you'll have loaded Social Security Administration data on names of babies born across the last ~100 years. It comes built in with the 'babynames' package we loaded. 

To refresh, let's load that now and store it as an object called `babynames_package_df`.

We're going to load the same data from different locations, using different methods, to show you how some of the many ways to get data into R.

```{r}

# Load babynames
babynames_package_df <- babynames

# Show first 10 records
babynames_package_df %>%
  head(10)

```

#### Loading data from a local flat file

Loading data from a flat file -- like a csv -- stored on your local machine is a very common data loading task.  For that, we'll use the `read_csv()` function that's part of the `readr` package that loads with the `tidyverse`. 

We're going to read in a sample of the babynames data that contains all of the names that start with "A". 

Store it as an object called "babynames_a_csv" (the name doesn't matter, can be anything). The information inside of `read_csv()` is the filepath to the data, which is stored in the data folder. 

```{r}

babynames_a_csv <- read_csv("data/babynames_a.csv")

```

#### Loading data from a flat file on the internet

We can load that same csv from the internet, instead of doing it locally.  We just need to change the information inside of the `read_csv()` function to pass a URL, instead of a location on our computer. 

The CSV is up on Github.com, here: https://raw.githubusercontent.com/smussenden/nicar_2024_r3_loading_cleaning_data/main/data/babynames_a.csv

Warning: this may not work if the wifi is buggy!

```{r}
babynames_a_csv_web <- read_csv("https://raw.githubusercontent.com/smussenden/nicar_2024_r3_loading_cleaning_data/main/data/babynames_a.csv")
```

#### Loading data from an Excel file

Another data format you'll likely see in the wild: Excel files. They're a little trickier than csvs, because they can contain multiple sheets. 

We can use the `read_xlsx()` function from the `readxl` package to load data from Excel files. 

There's an Excel file in the data folder called babynames_excel.  It has two sheets, one with all of the "A" babynames, followed by one with all of the "B" babynames. 

Let's load the first sheet, the "A" babynames, as a dataframe and store it as an object called babynames_a_excel.

```{r}
babynames_a_excel <- read_xlsx("data/babynames_excel.xlsx")
```

Because the "A" names sheet is the first sheet in the Excel file, the function automatically loads the "A" sheet. 

But if we need to get any other sheet, like the one containing the "B" names, we'll have to get it by adding another argument to the read_xlsx function. 

The sheet is called "babynames_b".

How can we load Sheet B?  Let's take a look at the handy help page for the readxl package.

* You can either type ?read_xlsx in the console and look at what pops up on the right. 
* Or you can visit https://readxl.tidyverse.org/reference/read_excel.html.  

Can you see how to read in a different sheet from the first?  

Let's modify the read_xlsx function below to load the sheet "babynames_b".

```{r}
babynames_b_excel <- read_xlsx("data/babynames_excel.xlsx")

```

#### Loading data from an HTML table

On this page is an HTML table showing the top 2022 baby names. https://www.ssa.gov/oact/babynames/. Because the wifi is often buggy, I've saved an HTML file locally of this page, which we'll work with instead.  It's in the data folder.

We can use the inspector in our web browser to see this.  It's composed of html tags. 

Using the `rvest` package we're going to first read in the entire html page using the `read_html()` function.

```{r}
# If we were going to pull directly from the web, instead of from a local file, this is what it will the function would look 

# top_2022_baby_names <- read_html("https://www.ssa.gov/oact/babynames/") 

# Instead, we're gonna load a local html file to simulate the act of scraping from the web
top_2022_baby_names <- read_html("data/html/ssa_baby_names.html")
```

Open it up in the environment window.  It's the full HTML of the page. 
Next, we'll use `rvest` to extract the html table we want using `html_table()`

```{r}
top_2022_baby_names <- read_html("data/html/ssa_baby_names.html") %>%
  html_table()

```

Open it up in the environment window. We've isolated that one html table and turned it into a dataframe, albeit one that is nested in a list.  Let's extract it from the list. 

```{r}

# Load html and extract table
top_2022_baby_names <- read_html("data/html/ssa_baby_names.html") %>%
  html_table()

# Pluck out the table
top_2022_baby_names <- top_2022_baby_names[[1]]

# display it
top_2022_baby_names

```

Never web scraped before? Now you have! A warning that web scraping does get more challenging from here. 

#### Loading data from google sheets

We can also load data directly from Google Sheets, using the `read_sheet()` function from the `googlesheets4` package.  Google Sheets, like Excel files, can also have multiple workbooks. 

I've loaded up a Google Sheet workbook here with two sheets, one for "A" babynames and one for "B" babynames: https://docs.google.com/spreadsheets/d/1GG_RmYPGCNKbLb4x1dkQv1B9NjDBF0kQRtge9Aea4rs. These samples only have 1,000 records in them.

To read in the sheet, we need to paste in the sheet ID, which is the long sting of numbers and letters at the end of the URL: "1GG_RmYPGCNKbLb4x1dkQv1B9NjDBF0kQRtge9Aea4rs"

Because the "A" sheet comes first, it automatically loads that sheet.

Before we get there, though, we'll need to authenticate with Google.  Look down in the console, select an account or hit 1 to start the process of in-browser authentication.

```{r}
gs4_auth()

```

Now we can read in the sheet.

```{r}

babynames_a_sheet <- read_sheet("1GG_RmYPGCNKbLb4x1dkQv1B9NjDBF0kQRtge9Aea4rs")
```

If we want to load any other sheet, we need to tell it which one to load. 

```{r}
babynames_b_sheet <- read_sheet("1GG_RmYPGCNKbLb4x1dkQv1B9NjDBF0kQRtge9Aea4rs", sheet = "babynames_b")
```

In addition to loading data from Google Sheets, you can also WRITE data from R Studio to Google Sheets.  This is such a great way to share data you've analyzed with other, less tech-savvy members of your team. More on that here: https://googlesheets4.tidyverse.org/index.html.  

### Your Turn Option 1

This page https://www.ssa.gov/oact/babynames/state/top5_2021.html, which I've also stored locally, contains tables of the top 5 birth names for 2021 by state, one for male and one for female.  

Using what you just learned, I'd like you to take a stab at ingesting the html of this page, and saving each of the tables as a separate data frame.   

```{r}

# local path to the data 
# "data/html/baby_names_2021_state.html"

```

### Your Turn Option 2

538 puts a lot of neat data sets on its' GitHub organization page.  Here's the page to a dataset about the Avengers, from Marvel Comics:  

https://github.com/fivethirtyeight/data/blob/master/avengers/avengers.csv

Read this data into your environment and store it as an object called `avengers`. 

```{r}

```

#### Other ways of getting data

There are lots of other ways to bring data into R.  We don't have to delve into all of them today, but you should be aware of them for continued learning. 

* Pull data from an SQL database with the `dbplyr` package. [dbplyr](https://dbplyr.tidyverse.org/)

* Get data from an API endpoint - You can access data available through pretty much any API, or application programming interface, by sending queries and getting back a response, using the excellent [HTTR package](https://httr.r-lib.org/).  An example of an API: [Spotify data](https://developer.spotify.com/documentation/web-api/) 

* Get data from packages the R community has built to load and work with specific kinds of data, including some nice helper functions. If the dataset you want to use is popular, there's a great change someone has built an R package for it! Some great examples:
  *[Tidycensus](https://walkerke.github.io/tidycensus/index.html): for loading and working with all manner of U.S. Census Data.
  *[RTweet](https://rtweet.info/): for working with Twitter data

#### Clear enivronment

Before moving on to the data cleaning section, let's clean up all those dataframes in our environment with this handy bit of code. 

```{r}
rm(list=ls())
```

#### Data Cleaning 

Data cleaning is a critical step in preparing data for analysis.  Everyone wants to jump right to the fun stuff -- me too! -- but failing to account for flaws in the data can lead to errors, which can lead to corrections.  

To start, we're going to load a dataframe with info on year-by-year totals for the most popular female baby names from 2008 to 2017. 

I've intentionally made this very ugly. Keeping with our theme, someone needs to change this dataframe's diaper!

```{r}

babynames_dirty <- read_rds("data/babynames_dirty.rds")

```

#### Identify Issues

Examine the data in the environment window.  

What problems do you see? Don't scroll down until you think you've found one or two of the problems. 


Are you sure you can't find more?


Are you sure? Ok. Here's what I see. 

* EMPTY ROWS - There's a totally empty row of NAs. Let's get rid of it.  It could prevent proper summarizing. 
* EMPTY COLUMN - There's a totally empty column called source. Let's get rid of it, because it's unneeded. 
* INCONSISTENT VALUES - The "sex" column has inconsistent values for Female vs F. This could hurt our ability to group and summarize properly. 
* STYLING INCONSISTENCIES - There are lots of issues in "name_at_birth" column. MADISON is upper. elizabeth is lower. Abigail has "First Name: Abigail" instead of just Abigail. Everything else is title case. This is just...ugly.
* DUPLICATE ROWS - There are two apparently identical rows for Emma and Amelia (or are they?). We should really only have one, and could lead to misleading summarization if we kept both.
* NUMBERS STORED AS CHARACTER STRINGS - The 2015 column has a random underscore appended to the end of the number, unlike every other year column. The fact that it's a mix of characters and numbers means the column is stored as a "character", while all of the other year columns are numbers (integers).  If we want to calculate say, the percent change in a name between 2008 and 2015, we'll get an error. 
* BAD COLUMN NAMES - Less obvious, but still annoying: the fact that the year columns start with a number means they'll be harder to include in our code.

Let's examine each of these, while fixing them. 

Our goal will be one nice long chained function to fix all the problems, so we have a clear record of what we've done.

#### Remove empty rows and columns

First, let's get rid of that totally NA row and column. The `janitor` package has a nice function for getting rid of empty rows and columns

```{r}
babynames_clean <- babynames_dirty %>%
  remove_empty()

# just empty rows? remove_empty(which="rows")
# just empty columns? remove_empty(which="columns")
# both rows and columns? remove_empty()
```

#### Remove duplicates

Right now, we have two identical rows with values for "Amelia" and "Emma".  We can remove those by using the `distinct()` function, which looks for duplicate values and keeps only one.

```{r}

babynames_clean <- babynames_dirty %>%
  remove_empty() %>%
  distinct()

```

That appears to have removed the duplicate "Amelia" rows, but not the duplicate "Emma" rows.  

Why? 

Before scrolling down, see if you can figure it out. 


If we examine the Emma row closely, we'll see that one has extra whitespace on both sides of the name, and the other doesn't. That means the rows aren't EXACTLY equal.

We can fix that with our first of many string functions, from the `stringr` package, which has lots of helpful functions for cleaning character strings. The function we'll use is called `str_trim()` and it's good at trimming extra whitespace. 

```{r}

babynames_clean <- babynames_dirty %>%
  remove_empty() %>%
  mutate(name_at_birth = str_trim(name_at_birth,side="both")) %>%
  distinct() 

```

Now when we run it again, `distinct()` gets rid of the extra Emma row because the difference has been fixed. 

#### Clean up names column

There are still lots of issues with the "name_at_birth" column.

MADISON is UPPERCASE; elizabeth is lowercase; everything else is Title Case.

Let's fix that first with a function called `str_to_title()`, which will convert everything to title case.

```{r}

babynames_clean <- babynames_dirty %>%
  remove_empty() %>%
  mutate(name_at_birth = str_trim(name_at_birth,side="both")) %>%
  distinct() %>%
  mutate(name_at_birth = str_to_title(name_at_birth))

```

### Before we move on from names column
Before we move on, let's suppose we wanted to make all the names lowercase or uppercase instead.  What do we think a function to do that might be called?  If you start typing str_to in the console, you might get a clue. 

### Fixing Abigail
The next issue will be a bit more challenging, fixing Abigail.  Her name has extra stuff -- "First Name: Abigail" -- that the others don't have.  We can remove that extra stuff with `str_remove()`. 

```{r}

babynames_clean <- babynames_dirty %>%
  remove_empty() %>%
  mutate(name_at_birth = str_trim(name_at_birth,side="both")) %>%
  distinct() %>%
  mutate(name_at_birth = str_to_title(name_at_birth)) %>%
  mutate(name_at_birth = str_remove(name_at_birth,"First Name: "))

```

#### Standardize "Sex" Column

We can use one another string function, `str_sub()` to standardize the "sex" column. This function in the block below says, "Starting at the left side of the sex column, keep everything from the first character on the left to...the first character on the left and Get rid of everything else."  

```{r}


# The slightly more complex way, to introduce you to string functions

babynames_clean <- babynames_dirty %>%
  remove_empty() %>%
  mutate(name_at_birth = str_trim(name_at_birth,side="both")) %>%
  distinct() %>%
  mutate(name_at_birth = str_to_title(name_at_birth)) %>%
  mutate(name_at_birth = str_remove(name_at_birth,"First Name: ")) %>%
  mutate(sex = str_sub(sex, start=1L, end=1L))

```

### Before we move on from sex

What happens if you change the start and end numbers?  How does the output change? Try it now.

#### Fix 2015 column

The 2015 column is different from the other columns, with an underscore at the end.  If we want to do math to that column, we'll have to fix it.  Here, again, we can use `str_remove()`.

```{r}
babynames_clean <- babynames_dirty %>%
  remove_empty() %>%
  mutate(name_at_birth = str_trim(name_at_birth,side="both")) %>%
  distinct() %>%
  mutate(name_at_birth = str_to_title(name_at_birth)) %>%
  mutate(name_at_birth = str_remove(name_at_birth,"First Name: ")) %>%
  mutate(sex = str_sub(sex, start=1L, end=1L)) %>%
  mutate(2015 = str_remove(2015,"_"))
```

But we get an error!  Why? Because R hates it when you start column names with numbers.  You could wrap it in tick marks when you use it, like `2015`, but that's pretty annoying.

Instead, we can use the helpful `clean_names()` function from the `janitor` package to standardize it.  If our column names had spaces, or capital letters, it would fix that too. 

```{r}
babynames_clean <- babynames_dirty %>%
  remove_empty() %>%
  mutate(name_at_birth = str_trim(name_at_birth,side="both")) %>%
  distinct() %>%
  mutate(name_at_birth = str_to_title(name_at_birth)) %>%
  mutate(name_at_birth = str_remove(name_at_birth,"First Name: ")) %>%
  mutate(sex = str_sub(sex, start=1L, end=1L)) %>%
  clean_names()
```

It puts an x at the start of the name, so now we can get to cleaning 2015. 

```{r}
babynames_clean <- babynames_dirty %>%
  remove_empty() %>%
  mutate(name_at_birth = str_trim(name_at_birth,side="both")) %>%
  distinct() %>%
  mutate(name_at_birth = str_to_title(name_at_birth)) %>%
  mutate(name_at_birth = str_remove(name_at_birth,"First Name: ")) %>%
  mutate(sex = str_sub(sex, start=1L, end=1L)) %>%
  clean_names() %>%
  mutate(x2015 = str_remove(x2015,"_"))
```

Okay, it looks like a proper number now.  But if we look under the hood, at the data type of each column, we'll see it hasn't been fixed. We can do that with `glimpse()`

```{r}
glimpse(babynames_clean)
```

x2015 is still a "character". If we try to do math to it, it will error.  So let's change the datatype to a number using `as.integer()`. 

```{r}
babynames_clean <- babynames_dirty %>%
  remove_empty() %>%
  mutate(name_at_birth = str_trim(name_at_birth,side="both")) %>%
  distinct() %>%
  mutate(name_at_birth = str_to_title(name_at_birth)) %>%
  mutate(name_at_birth = str_remove(name_at_birth,"First Name: ")) %>%
  mutate(sex = str_sub(sex, start=1L, end=1L)) %>%
  clean_names() %>%
  mutate(x2015 = str_remove(x2015,"_")) %>%
  mutate(x2015 = as.integer(x2015))
```
When we glimpse the data, it's been converted to the correct datatype.
```{r}
glimpse(babynames_clean)
```

Thanks for joining.  If you get stuck in the future and need some help, I'm at smussend@umd.edu.


## Top 5 Baby Names by State for Births in 2021

:::::::: grid
- [Popular Baby Names](https://www.ssa.gov/oact/babynames/index.html)
- [Top 100 names by State](https://www.ssa.gov/oact/babynames/state/index.html)

**Select another year of birth?**\
Year 2021 2020 2019 2018 2017 2016 2015 2014 2013 2012 2011 2010 2009 2008 2007 2006 2005 2004 2003 2002 2001 2000 1999 1998 1997 1996 1995 1994 1993 1992 1991 1990 1989 1988 1987 1986 1985 1984 1983 1982 1981 1980

The following tables show the five most frequent given names, by State, for [male](https://www.ssa.gov/oact/babynames/state/top5_2021.html#Male) and [female](https://www.ssa.gov/oact/babynames/state/top5_2021.html#Female) births in 2021. The number to the right of each name is the number of occurrences in the data. The source is a 100% sample based on Social Security card application data as of March 2022. See the [limitations](https://www.ssa.gov/oact/babynames/background.html) of this data source.


Top Five Female Names for Births in 2021

  ------------------- ----------- ----------- ----------- ----------- -----------
  State               Rank 1      Rank 2      Rank 3      Rank 4      Rank 5
  Alabama             Olivia      Ava         Amelia      Charlotte   Emma
  Alaska              Amelia      Hazel       Olivia      Ava         Charlotte
  Arizona             Olivia      Emma        Sophia      Camila      Isabella
  Arkansas            Olivia      Emma        Amelia      Ava         Charlotte
  California          Olivia      Emma        Camila      Mia         Sophia
  Colorado            Olivia      Emma        Charlotte   Evelyn      Amelia
  Connecticut         Olivia      Charlotte   Emma        Amelia      Sophia
  Delaware            Charlotte   Olivia      Amelia      Emma        Sophia
  Dist. of Columbia   Charlotte   Ava         Maya        Sophia      Emma
  Florida             Olivia      Emma        Isabella    Mia         Sophia
  Georgia             Olivia      Ava         Amelia      Emma        Charlotte
  Hawaii              Olivia      Amelia      Luna        Ava         Isla
  Idaho               Olivia      Amelia      Emma        Evelyn      Harper
  Illinois            Olivia      Emma        Sophia      Charlotte   Amelia
  Indiana             Charlotte   Amelia      Emma        Olivia      Ava
  Iowa                Charlotte   Olivia      Amelia      Ava         Emma
  Kansas              Olivia      Charlotte   Amelia      Emma        Evelyn
  Kentucky            Emma        Olivia      Amelia      Ava         Charlotte
  Louisiana           Olivia      Ava         Amelia      Charlotte   Emma
  Maine               Charlotte   Olivia      Amelia      Emma        Harper
  Maryland            Olivia      Charlotte   Ava         Emma        Sophia
  Massachusetts       Olivia      Charlotte   Emma        Sophia      Amelia
  Michigan            Charlotte   Olivia      Amelia      Ava         Evelyn
  Minnesota           Charlotte   Olivia      Evelyn      Emma        Nora
  Mississippi         Ava         Olivia      Amelia      Paisley     Emma
  Missouri            Olivia      Charlotte   Amelia      Ava         Emma
  Montana             Olivia      Evelyn      Ava         Charlotte   Harper
  Nebraska            Olivia      Charlotte   Evelyn      Amelia      Eleanor
  Nevada              Olivia      Isabella    Emma        Mia         Camila
  New Hampshire       Olivia      Charlotte   Evelyn      Emma        Amelia
  New Jersey          Olivia      Emma        Mia         Ava         Sophia
  New Mexico          Mia         Sophia      Emma        Isabella    Amelia
  New York            Olivia      Emma        Sophia      Mia         Amelia
  North Carolina      Olivia      Ava         Emma        Charlotte   Amelia
  North Dakota        Olivia      Harper      Emma        Evelyn      Amelia
  Ohio                Olivia      Charlotte   Emma        Amelia      Ava
  Oklahoma            Olivia      Amelia      Harper      Charlotte   Ava
  Oregon              Evelyn      Olivia      Charlotte   Amelia      Sophia
  Pennsylvania        Olivia      Charlotte   Emma        Ava         Sophia
  Rhode Island        Olivia      Sophia      Amelia      Charlotte   Emma
  South Carolina      Olivia      Ava         Charlotte   Emma        Amelia
  South Dakota        Evelyn      Emma        Charlotte   Amelia      Ava
  Tennessee           Olivia      Charlotte   Ava         Emma        Amelia
  Texas               Olivia      Emma        Camila      Isabella    Mia
  Utah                Olivia      Charlotte   Emma        Evelyn      Hazel
  Vermont             Charlotte   Emma        Nora        Isla        Olivia
  Virginia            Charlotte   Olivia      Emma        Ava         Sophia
  Washington          Olivia      Amelia      Emma        Charlotte   Sophia
  West Virginia       Amelia      Harper      Paisley     Willow      Emma
  Wisconsin           Charlotte   Olivia      Emma        Evelyn      Amelia
  Wyoming             Olivia      Amelia      Charlotte   Emma        Evelyn
  ------------------- ----------- ----------- ----------- ----------- -----------


Top Five Male Names for Births in 2021

  ------------------- --------- --------- ---------- ----------- -----------
  State               Rank 1    Rank 2    Rank 3     Rank 4      Rank 5
  Alabama             William   John      James      Noah        Elijah
  Alaska              Noah      Oliver    Liam       William     Wyatt
  Arizona             Liam      Noah      Mateo      Oliver      Sebastian
  Arkansas            Liam      Oliver    Elijah     Noah        Asher
  California          Noah      Liam      Mateo      Sebastian   Julian
  Colorado            Liam      Oliver    Noah       Henry       Theodore
  Connecticut         Noah      Liam      James      Lucas       Benjamin
  Delaware            Liam      Noah      Michael    Lucas       James
  Dist. of Columbia   Henry     William   James      Noah        Liam
  Florida             Liam      Noah      Lucas      Elijah      Oliver
  Georgia             Noah      Liam      William    Elijah      James
  Hawaii              Noah      Kai       Liam       Ezekiel     Oliver
  Idaho               Oliver    Liam      Henry      William     Jack
  Illinois            Noah      Liam      Oliver     Henry       Benjamin
  Indiana             Liam      Oliver    Noah       Elijah      Henry
  Iowa                Oliver    Liam      Henry      Noah        Asher
  Kansas              Liam      Oliver    Noah       Theodore    James
  Kentucky            Liam      James     Elijah     William     Noah
  Louisiana           Liam      Noah      Elijah     James       William
  Maine               Oliver    William   Owen       Henry       Jack
  Maryland            Liam      Noah      James      Lucas       Oliver
  Massachusetts       Noah      Liam      Henry      Jack        Benjamin
  Michigan            Noah      Oliver    Liam       Henry       Elijah
  Minnesota           Oliver    Henry     Theodore   Liam        Owen
  Mississippi         William   John      James      Elijah      Noah
  Missouri            Oliver    Henry     Liam       William     Elijah
  Montana             Oliver    Liam      James      Asher       Jackson
  Nebraska            Henry     Oliver    Liam       Theodore    William
  Nevada              Liam      Noah      Mateo      Oliver      Sebastian
  New Hampshire       Oliver    Henry     Liam       Jackson     Benjamin
  New Jersey          Liam      Noah      Lucas      Joseph      Michael
  New Mexico          Noah      Liam      Elijah     Ezekiel     Mateo
  New York            Liam      Noah      Lucas      Joseph      Jacob
  North Carolina      Liam      Noah      William    James       Oliver
  North Dakota        Oliver    Liam      Theodore   Asher       Brooks
  Ohio                Oliver    Liam      Noah       Henry       Lincoln
  Oklahoma            Liam      Oliver    Noah       Elijah      William
  Oregon              Oliver    Liam      Henry      Benjamin    Lucas
  Pennsylvania        Noah      Liam      Benjamin   Oliver      Owen
  Rhode Island        Liam      Noah      Julian     Henry       Oliver
  South Carolina      William   James     Liam       Noah        Elijah
  South Dakota        Henry     Oliver    Theodore   Hudson      Asher
  Tennessee           William   Liam      James      Noah        Elijah
  Texas               Liam      Noah      Elijah     Mateo       Sebastian
  Utah                Oliver    Liam      Jack       William     Henry
  Vermont             Henry     Oliver    Theodore   Noah        Owen
  Virginia            Liam      Noah      James      William     Oliver
  Washington          Liam      Noah      Oliver     Henry       Theodore
  West Virginia       Liam      Waylon    Elijah     Noah        Grayson
  Wisconsin           Oliver    Henry     Theodore   Liam        Levi
  Wyoming             Oliver    Liam      Henry      Lincoln     Owen
  ------------------- --------- --------- ---------- ----------- -----------



## Get Ready for Baby

Social Security is with you from day one, which makes us *the* source for the most popular baby names and more!

[Learn How to Get Baby\'s First Number](https://www.ssa.gov/pubs/EN-05-10023.pdf) [What Every Parent Should Know](https://www.ssa.gov/people/parents/index.html#anchor1)

[Subscribe to Baby Names](https://public.govdelivery.com/accounts/USSSA/subscriber/new?topic_id=USSSA_31 "Subscribe to Baby Names"){rel="noopener noreferrer" target="_blank" style="color: white" auto-tracked="true"}

::::::: section
:::::: grid
::::: row-12
::: column-12
### Top 10 Baby Names of 2021

::: column-6
  Rank   Male name   Female name
  ------ ----------- -------------
  1      Liam        Olivia
  2      Noah        Emma
  3      Oliver      Charlotte
  4      Elijah      Amelia
  5      James       Ava
  6      William     Sophia
  7      Benjamin    Isabella
  8      Lucas       Mia
  9      Henry       Evelyn
  10     Theodore    Harper

::::::: section
:::::: grid
::::: row-12
:::: column-12
### View Popularity of Names By:

::: c-icons
[![](./ssa_baby_names_files/popularity.svg) Change in popularity](https://www.ssa.gov/oact/babynames/rankchange.html) [![](./ssa_baby_names_files/top5.svg) Top 5 names](https://www.ssa.gov/oact/babynames/top5names.html) [![](./ssa_baby_names_files/decade.svg) Decade](https://www.ssa.gov/oact/babynames/decades) [![](./ssa_baby_names_files/state.svg) State](https://www.ssa.gov/oact/babynames/state) [![](./ssa_baby_names_files/territory.svg) U.S. territories](https://www.ssa.gov/oact/babynames/territories.html)

::::::: section
:::::: grid
### Items of Interest

::::: row-12
### Popular Names by Birth Year

Enter the Year and Popularity for a List of the Most Popular Names

Any year after 1879

  Birth Year\

Top 20 Top 50 Top 100 Top 500 Top 1000   Popularity\

Name rankings may include:   Percent of total births\
  Number of births

### Popularity of a Name

See How the Popularity of a Name has Changed Over Time!

 Name\

2000 & later 1980 & later 1960 & later 1940 & later 1920 & later 1900 & later   Years\

Sex associated with name Male   \
Female

::::::: section
:::::: grid
::::: row-12
::: column-6

::: column-6
### Open Your Personal my Social Security Account

Open an account today to view estimates of the retirement, disability, and survivors benefits you and your growing family may be eligible for in the future. Already receiving benefits? Use your account to check and manage your benefits, and much more!

[Create Your Account](https://ssa.gov/myaccount/)

::::::: section
:::::: grid
::::: row-12
::: column-6
### See How Social Security Protects Your Family

We offer a wide range of resources for families with children. When a parent becomes disabled or dies, we have programs and benefits to help secure the family\'s financial future.

[Benefits for Children](https://ssa.gov/pubs/EN-05-10085.pdf) [Parents and Guardians](https://www.ssa.gov/people/parents/)

::: column-6

::::::: section
:::::: grid
::::: row-12
::: column-6
### Related Links

- [Background Information](https://www.ssa.gov/oact/babynames/background.html)
- [Plan Your Family\'s Financial Security](https://ssa.gov/planners/retire/)
- [Calculate Your Retirement Benefits](https://ssa.gov/planners/benefitcalculators.html)
- [Future Financial Status of Social Security](https://www.ssa.gov/oact/TR/)

::: column-6
### Other Sites of Interest

- [Healthy Pregnancy](https://www.nlm.nih.gov/medlineplus/pregnancy.html){rel="noopener noreferrer" target="_blank" auto-tracked="true"}
- [Caring for Your Newborn](https://www.nlm.nih.gov/medlineplus/infantandnewborncare.html){rel="noopener noreferrer" target="_blank" auto-tracked="true"}
- [Childhood Immunizations](https://www.cdc.gov/vaccines/pubs/parents-guide/default.htm){rel="noopener noreferrer" target="_blank" auto-tracked="true"}
- [Food Stamps and WIC](https://www.fns.usda.gov/fns/){rel="noopener noreferrer" target="_blank" auto-tracked="true"}


## Two types of lessons

- The [regex101 version](regex101.qmd) is a lesson that uses regex101.com to learn and practice the learning expressions.
- The [VS Code version](vscode.qmd) is the same lesson, but it is a backup that can be done without the web (providing you have the material)

There is also a Google Docs version: [Wrangling data with Regular Expressions](https://docs.google.com/document/d/1DvAM4lnGJLefo9skD8GgM-_9S1BEhpjJfV86yhJavI0/edit).



## **Key concept: patterns**


et’s say you have a list of phone numbers in 10-digit format – 512-555-1212 – but you want the area code to be in

arentheses: (512) 555-1212. You could do a simple search of the “512” area code followed by a dash “512-” and

eplace it with an area code in parentheses and a space: “(512)”.


But what if there are different area codes in the list?

```
      512-555-1211
      301-333-1212
      410-123-1213

```

With regular expressions, you can search for a pattern of characters. Instead of searching just for 512-, you can look

or “three numbers together at the beginning of a line that are then followed by a dash”.


f you capture that matching pattern as a group, you can then replace that group with parentheses outside it, no

matter what the contents of the group. If that saved group is called `$1` then you can replace it with `($1)` and it

oesn’t matter if `$1` is equal to “512-” or “301-”.


## **Special characters, commands and escape**


et’s touch quickly on the syntax of regular expressions. Don’t get hung up if these sound like gibberish, because it

[will make sense more when we start using it. This Cheatsheet](http://localhost:3824/cheatsheet.html) comes in handy here.


Regular expressions use special characters to do special things, like match the beginning of a line. These

ommands are called tokens. Some examples:


`*` will find “zero or more” of whatever precedes it.


Regular expressions use the backslash (the one above return on a keyboard where the top tips to the left) with

ther characters to create more tokens to do special things:


`\d` will find any number character (or digit).


`\D` will match anything other than a number.


`\t` is a tab character, because hitting the tab on the keyboard will perform the action instead of giving you the

haracter.


But then sometimes, you actually need to find the character ^, and not use it as a command. Regular expressions

se the to give the literal expression of a character that would otherwise be a token:


`\*` will find the asterisk character instead of the token to find “zero or more”.



## **Defining our goal**


We’re going to use regular expressions to split complicated address data into individual parts. The sample we’ll us

s a column from some City of Austin data published on their Socrata open data portal.


t had all the address parts crammed into a single field. Regex can easily explode that into individual columns,

which is more useful to us.


o, our goal is to turn this …

```
      "10111 N LAMAR BLVD
      AUSTIN, TX 78753
      (30.370945933000485, -97.6925542359997)"
      "2620 LAKE AUSTIN BLVD
      AUSTIN, TX 78703
      (30.28190796500047, -97.77587573499966)"

```

… into this, with each address part separated with a tab:

```
      10111 N LAMAR BLVD AUSTIN TX 78753  30.370945933000485 -97.6925542359997
      2620 LAKE AUSTIN BLVD  AUSTIN TX 78703  30.28190796500047  -97.775875734999

```

With this change, we can copy/paste the results into a spreadsheet.


## **The goal in a nutshell**


We are building a pattern in our regular expression field, creating “capture groups” for each part of the address


[ou’ll want to reference your Regex-Cheatsheet.docx](http://localhost:3824/resources/Regex-Cheatsheet.docx) [or Regular-expressions-syntax.pdf](http://localhost:3824/resources/Regular-expressions-syntax.pdf) in the resources folder.


et’s get started:


1. From Visual Studio Code where you are working with this, click on the file

`data/socrata_addresses_copy.txt` to open it.


Note this is just one column from a larger Socrata data set of restaurant inspection scores in Austin, TX. (When I

want to clean a single column of data, I often download the data and will just copy out one column into my text

ditor and work it before pasting back the results into a new Excel column, carefully making sure they still line up.)


et’s look at our data a little closer. This example from the top of the file is just one “cell” of data, even though it

as multiple lines of text

```
      "10111 N LAMAR BLVD
      AUSTIN, TX 78753
      (30.370945933000485, -97.6925542359997)"

```

he address, city, state, zip, latitude and longitude are all in the same “cell” (what is inside the quote marks), but

he content of the cell has returns in it. We want to split these six distinct pieces into their own columns for each

ecord. Why? Many reasons, but one is to use the latitude and longitude for data visualizations.


We will build a Regular Expression pattern to **Find** and capture six groups of text and then **Replace** those groups

with tabs between them so we can put them back into a spreadsheet as columns.



## **Building our Find pattern**


1. In your `data/socrata_addresses_copy.txt` file, do **Command-option-f** to open the Find and Replace

box. (Or menu: Edit > Replace)


The Find/Replace window will open at the top right.


2. Next to Find you’ll find some options. Click on the one that is a period-asterisk: .*


Find and Replace prompt

### **Capturing the address**

We’ll begin entering tokens into the “Find” prompt so we can see how to use tokens to capture patterns. In some

ases, we’ll “capture” the pattern using parentheses, so we can refer back to it later.


You’ll see that the first character of each line is now highlighted.


2. Next we want to **add the double-quote** so we can continue the pattern from the beginning of each address.

Add a double-quote after the first token, like this:

```
 ^"

```

You’ll notice that now only the double-quote marks are selected.


First quote selected


3. Next, we’ll start our first capture group with parentheses:

```
 ^"()

```

You’ll see as you type in the open parentheses that you’ll get an “error” in the Find box because it expects a

closing parentheses. Make sure you add that, then put your cursor back between them.


4. Now, inside those parentheses, we’ll add `.*` so the full line looks like this:

```
 ^"(.*)

```

You’ll see that the rest of the line has been selected.


Inside the parentheses (our first group), we want to capture the whole address, which is everything until the

end of the line. The period token `.` means “any character”, and `*` means “zero or more”, so put these

together and we get everything: `^"(.*)` .


Address line


**New lines differe between Mac and PCs**

Before we can start capturing the second group with the city, we need to add the “return” to the pattern so it can start

recognizing the next line. But here’s the drive-you-crazy thing: Windows and Macs treat these differently. On a Mac, `\n` is a


this lab, you ll need to use `\R` every time you see `\n` in this tutorial.


5. Add `\n` to the end of the string to make:

```
  ^"(.*)\n

```

Address line with return

### **Capturing the city**

As we look through the list, you can see we have some cities with more than one word – like “BEE CAVE” – so we

eed a way to capture both letters and spaces, but not other punctuation. There are MANY ways to do this, but

we’ll use a “character set” to show how to use more than one token at a time:


1. First, create a new group:

```
  ^"(.*)\n()

```

2. Then inside the group, we have to build the “character set” using square brackets. Inside those brackets we’ll

ad a `\w` token to catch any word character, and a space so we can catch those, too. Lastly, we put a `+` token

right after the character set to signify we want “one or more”:

```
  ^"(.*)\n([\w ]+)

```

City captured

### **Capturing the state**

hese addresses are all in TX, so we don’t really have to save it at all, but we will. We’ll use this to remind ourselves

hat you can also just match a string literally.


1. First we put the comma and space outside the second group, since we don’t want to keep it:

```
  ^"(.*)\n(\w+),

```

City with comma and space


You can’t see that trailing space in the image above, but make sure it is there.

2. Then we create our third group with TX inside it:

```
  ^"(.*)\n([\w ]+), (TX)

```

Adding TX


We choose to find the literal text “TX” because there are no other states in this data set. We can’t skip it because we

eed the pattern to continue.

### **Capturing the ZIP**

Again, we don’t want to keep the space between the state and ZIP, so we’ll put it outside the third group.


1. Add the comma, space and new group to start our fourth group:

```
  ^"(.*)\n([\w ]+), (TX) ()

```

2. All of these zip codes are of the 5-digit variety, so this can be less complicated than it might be with 9-digit

ZIPs. Again, there are many ways to do this, but we’ll use `\d` for the numbers and `*` to capture zero or more

of them. Add those inside the capture group:

```
  ^"(.*)\n([\w ]+), (TX) (\d*)

```

3. Complete the pattern for this line with the new line token `\n` . ( **NOTE:** Remember to change the `\n` to `\R` if

we are on PCs):

```
  ^"(.*)\n([\w ]+), (TX) (\d*)\n

```

Zip captured to end of line

### **Capturing latitude**

1. We don’t want to keep the parentheses that starts this last line, so we’ll put it outside any capture group.

However, since parentheses mean something special in regex, we need to escape it with a backslash so it will

find the character and not start the new group:

```
  ^"(.*)\n([\w ]+), (TX) (\d*)\n\(

```

2. Now we can start our new group, so go ahead and add the beginning and end parentheses:

```
  ^"(.*)\n([\w ]+), (TX) (\d*)\n\(()

```

3. Inside our fifth group, we need numbers and the decimal point. We will create a character set using square

brackets and put inside it `\d` for numbers and `\.` for the decimal point, which we have to escape since `.`

means “any character”. We finish it off by using `+` to look for one or more of the characters in the set. Like this

```
  ^"(.*)\n([\w ]+), (TX) (\d*)\n\(([\d\.]+)

```

Latitude captured

### **Capturing longitude**

1. We don’t need the comma and space in our next group, so we put it outside to keep the pattern going:

```
  ^"(.*)\n([\w ]+), (TX) (\d*)\n\(([\d\.]+),

```

2. We can get the longitude like we did latitude, but we have to add the hyphen to the character set. So, create

the group:

```
  ^"(.*)\n([\w ]+), (TX) (\d*)\n\(([\d\.]+), ()

```

3. Add the character set:

```
  ^"(.*)\n([\w ]+), (TX) (\d*)\n\(([\d\.]+), ([])

```

```
  ^"(.*)\n([\w ]+), (TX) (\d*)\n\(([\d\.]+), ([\d\-\.])

```

5. Add our quantifier to get one or more:

```
  ^"(.*)\n([\w ]+), (TX) (\d*)\n\(([\d\.]+), ([\d\-\.]+)

```

6. Because the trailing parentheses and quote are at the end of a line, we could ignore them, but we won’t. We’l

add them to the end of the pattern, escaping the close parentheses just to be sure:

```
  ^"(.*)\n([\w ]+), (TX) (\d*)\n\(([\d\.]+), ([\d\-\.]+)\)"

```

Longitude captured


## **The Replace string**


Now that we have a pattern with our six groups of data, we keep or exclude them in any order we want using the

**Replace** prompt and the replace all icon.


Our goal is to bring back six of our groups, but to put tabs in between each of them. If we can build a search and

eplace like this, then we can paste the result back into Excel, and each group will become its own column.


A quick refresher from our intro: Once we’ve built a group, we can reference it in our substitution string by order in

which we captured it. So, if we want to reference our first group, we use this: `$1` .


1. Add this to the Replace prompt:

```
  $1

```

2. Click the second icon next to the replace string (which is replace all):


I wasn’t trying to scare you there, but you needed to see how replacing with a capture group worked.


4. Update the **Replace** string to add a tab token `\t` between each group.

```
  $1\t$2\t$3\t$4\t$5\t$6

```

5. And then use the **replace all icon** to do the Find/Replace on all rows.


We did it!

### **Add to Excel or Google Sheets**

he way this text is structured, you can copy it all and then paste it into an Excel or Google Sheets spreadsheet and

ou should get six distinct rows.


heets gif



## **More Regex**


our friends. ChatGPT might be helpful, too, if you are good at prompts.


## Key concept: patterns


Let's say you have a list of phone numbers in 10-digit format -- `512-555-1212` -- but you want

space: `(512)` .


But what if there are different area codes in the list?

```
512-555-1211
301-333-1212
404-123-1213

```

With regular expressions, you can search for a pattern of characters. Instead of searching just
for `512-`, you can look for "three numbers together at the beginning of a line that are then
followed by a dash".


If you capture that matching pattern as a group, you can then replace that group with
parenthesis outside it, no matter what the contents of the group. If that saved group is called `$1`
then you can replace it with `($1)` and it doesn't matter if `$1` is equal to `512-` or `301-` .




## Special characters, commands and escape

Let's touch quickly on the syntax of regular expressions. Don't get hung up if these sound like
gibberish, because it will make more sense when we start using it. Your [Regex Cheat Sheet](https://drive.google.com/file/d/0B8ConnGcXrv8MzE3SWtwU2NxQk0/view?usp=sharing) (or
[this alternative) comes in handy here.](https://drive.google.com/open?id=0B8ConnGcXrv8bnJwdEtWVGx4N0E)


Regular expressions use special characters to do special things, like match the beginning of a
line. These commands are called tokens:

  - `^` will find the beginning of a line.

  - `*` will find "zero or more" of whatever precedes it.


Regular expressions use the backslash (the one above return on the keyboard: `\` ) with other
characters to create more tokens to do special things:

  - `\d` will find any number character (or digit).

  - `\D` will match anything other than a number.

  - `\t` is a tab character, because hitting the tab on the keyboard will perform the action
instead of giving you the character.


But then sometimes, you actually need to find the character `^`, and not use it as a command.
Regular expressions use the `\` to give the literal expression of a character that would otherwise
be a token:

  - `\*` will find the asterisk character instead of modifying the query to find "zero or more".


Enough of that. Let's do this, with the help of ...


## Regex101.com


[Regex101 is a great way to not only build regex patterns, but to also learn how they work. Go](https://regex101.com/)
ahead and launch that site in a browser so we can work with it here in a minute.


We're going to use this tool to take split complicated address data into individual parts. Let's talk
about the data first.


