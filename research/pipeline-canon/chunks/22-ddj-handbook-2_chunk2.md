<!-- chunk: 2/4 | source: 22-ddj-handbook-2.md | words: 35553 -->
<!-- headings: **18. Coding With Data in the Newsroom**; **19. Accounting for Methods: Spreadsheets,** **Scripts and Programming Notebooks**; **20. Working Openly in Data Journalism**; **21. Making Algorithms Work for** **Reporting**; **22. Journalism With Machines?** **From Computational Thinking to** **Distributed Cognition**; Experiencing Data; **23. Ways of Doing Data Journalism**; **24. Data Visualizations: Newsroom Trends** **and Everyday Engagements**; **25. Sketching With Data**; **26. The Web as Medium for Data** **Visualization**; **27. Four Recent Developments in News** **Graphics**; **28. Searchable Databases as a Journalistic** **Product**; **29. Narrating Water Conflict With Data** **and Interactive Comics**; **30. Data Journalism Should Focus on** **People and Stories**; Investigating Data, Platforms and Algorithms; **31. The Algorithms Beat: Angles and** **Methods for Investigation**; **32. Telling Stories With the Social Web**; **33. Digital Forensics: Repurposing Google** **Analytics IDs** -->

##### **18. Coding With Data in the Newsroom**

_Basile Simon_


**Abstract**
Newsrooms present unique challenges to coders and technically minded
journalists.


**Keywords:** computational journalism, programming, data cleaning,
databases, data visualization


Inevitably, there is a point where data and code become companions. Perhaps
when Google Sheets slows down because of the size of a data set; when Excel
formulas become too arcane; or when it becomes impossible to make sense
of data spanning hundreds of rows. Coding can make working with data
simpler, more elegant, less repetitive and more repeatable. This does not
mean that spreadsheets will be abandoned, but rather that they will become
one of a number of different tools available. Data journalists often jump
between techniques as they need: Scraping data with Python notebooks,
throwing the result into a spreadsheet, copying it for cleaning in Refine
before pasting it back again.
Different people learn different programming languages and techniques;
different newsrooms produce their work in different languages, too. This
partly comes from an organization’s choice of “stack,” the set of technologies
used internally (for example, most of the data, visual and development
work at _The Times_ (of London) is done in R, JavaScript and React; across
the pond _ProPublica_ uses Ruby for many of their web apps). While it is
often individuals who choose their tools, the practices and cultures of
news organizations can heavily influence these choices. For example, the
BBC is progressively moving its data visualization workflow to R (BBC
Data Journalism team, n.d.); _The Economist_ shifted their world-famous Big
Mac Index from Excel-based calculations to R and a React/d3.js dashboard
(González et al., 2018). There are many options and no single right answer.


Bounegru, L. and J. Gray (eds.), _The Data Journalism Handbook:_ _Towards a Critical Data Practice_ .
Amsterdam: Amsterdam University Press, 2021
doi 10.5117/9789462989511_ch18


The good news for those getting started is that many core concepts apply
to all programming languages. Once you understand how to store data
points in a list (as you would in a spreadsheet row or column) and how to
do various operations in Python, doing the same thing in JavaScript, R or
Ruby is a matter of learning the syntax.
For the purpose of this chapter, we can think of data journalism’s coding
as being subdivided into three core areas: Data work—including scraping,
cleaning, statistics (work you could do in a spreadsheet); back-end work—the
esoteric world of databases, servers and APIs; and front-end work—most of
what happens in a web browser, including interactive data visualizations.
This chapter explores how these different areas of work are shaped by
several constraints that data journalists routinely face in working with
code in newsrooms, including (a) time to learn, (b) working with deadlines
and (c) reviewing code.


**Time to Learn**


One of the wonderful traits uniting the data journalism community is the
appetite to learn. Whether you are a reporter keen on learning the ropes,
a student looking to get a job in this field or an accomplished practitioner,
there is plenty to learn. As technology evolves very quickly, and as some
tools fall out of fashion while others are created by talented and generous
people, there are always new things that can be done and learned. There
are often successive iterations and versions of tools for a given task (e.g.,
libraries for obtaining data from Twitter’s API). Tools often build and expand
on previous ones (e.g., extensions and add-ons for the D3 data visualization
library). Coding in data journalism is thus an ongoing learning process
which takes time and energy, on top of an initial investment of time to learn.
One issue that comes with learning programming is the initial reduction
of speed and efficiency that comes with grappling with unfamiliar concepts.
Programming boot camps can get you up to speed in a matter of weeks,
although they can be expensive. Workshops at conferences are shorter
and cheaper, and for beginners as well as advanced users. Having time to
learn on the clock, as part of your job, is a necessity. There you will face
real, practical problems, and if you are lucky you will have colleagues to
help you. There’s a knack to finding solutions to your problems: Querying
for issues over and over again and developing a certain “nose” for what is
causing an issue.


This investment in time and resources can pay off: Coding opens many
new possibilities and provides many rewards. One issue that remains at all
stages of experience is that it is hard to estimate how long a task will take.
This is challenging, because newsroom work is made of deadlines.


**Working With Deadlines**


Delivering on time is an essential part of the job in journalism. Coding,
as reporting, can be unpredictable. Regardless of your level of experience,
delays can—and invariably will—happen.
One challenge for beginners is slowdown caused by learning a new way to
work. When setting off to do something new, particularly in the beginning
of your learning, make sure you leave yourself enough time to be able to
complete your task with a tool you know (e.g., spreadsheet). If you are just
starting to learn and strapped for time, you may want to use a familiar tool
and wait until you have more time to experiment.
When working on larger projects, tech companies use various methods
to break projects down into tasks and sub-tasks (until the tasks are small
and self-contained enough to estimate how long they will take) as well as
to list and prioritize tasks by importance.
Data journalists can draw on such methods. For example, in one _The_
_Sunday Times_ project on the proportion of reported crimes that UK police
forces are able to solve, we prioritized displaying numbers for the reader’s
local area. Once this was done and there was a bit of extra time, we did
the next item on the list: A visualization comparing the reader’s local area
to other areas, and the national average. The project could have gone to
publication at any point thanks to how we worked. This iterative workflow
helps you focus and manage expectations at the same time.


**Reviewing Code**


Newsrooms often have systems in place to maintain standards for many of
their products. A reporter doesn’t simply file their story and it gets printed:
It is scrutinized by both editors and sub-editors.
Software developers have their own systems to ensure quality and to
avoid introducing bugs to collaborative projects. This includes “code reviews,”
where one programmer submits their work and others test and review it,
as well as automated code tests.


According to the 2017 Global Data Journalism Survey, 40% of responding
data teams were three to five members and 30% of them counted only
one or two members (Heravi, 2017). These small numbers pose a challenge
to internal code reviewing practices. Data journalists thus often work on
their own, either because they don’t have colleagues, because there are no
peer-review systems in place or because there is no one with the right skills
to review their code.
Internal quality control mechanisms can therefore become a luxury that
only a few data journalism teams can afford (there are no sub-editors for
coding!). The cost of not having such control is potential bugs left unattended,
sub-optimal performance or, worst of all, errors left unseen. These resource
constraints are perhaps partly why it is important for many journalists to
look for input on and collaboration around their work outside their organizations, for example from online coding communities. [1]


**Works Cited**


BBC Data Journalism team. (n.d.). What software do the BBC use? [Interview].
https://warwick.ac.uk/fac/cross_fac/cim/news/bbc-r-interview/
González, M., Hensleigh, E., McLean, M., Segger, M., & Selby-Boothroyd, A. (2018,
August 6). How we made the new Big Mac Index interactive. _Source_ . https://
source.opennews.org/articles/how-we-made-new-big-mac-index-interactive/
Heravi, B. (2017, August 1). State of data journalism globally: First insights into
the global data journalism survey. _Medium_ . https://medium.com/ucd-ischool/
state-of-data-journalism-globally-cb2f4696ad3d


**About the Author**


**Basile Simon** is graphics editor at Reuters Graphics and a Visiting Lecturer
in Interactive Journalism at City, University of London.


1 More on data journalism code transparency and reviewing practices can be found in chapters
in this volume by Leon and Mazotte.


##### **19. Accounting for Methods: Spreadsheets,** **Scripts and Programming Notebooks**

_Sam Leon_


**Abstract**
This chapter explores the ways in which literate programming environments such as Jupyter Notebooks can help make data journalism
reproducible, less error prone and more collaborative.


**Keywords:** Jupyter Notebooks, reproducibility, programming, Python,
literate programming environments, data journalism


With the rise of data journalism, ideas around what can be considered a
journalistic source are changing. Sources come in many forms now: Public
data sets, leaked troves of emails, scanned documents, satellite imagery
and sensor data. In tandem with this, new methods for finding stories in
these sources are emerging. Machine learning, text analysis and some of
the other techniques explored elsewhere in this book are increasingly being
deployed in the service of the scoop.
But data, despite its aura of hard objective truth, can be distorted and
misrepresented. There are many ways in which data journalists can introduce error into their interpretation of a data set and publish a misleading
story. There could be issues at the point of data collection which prevent
general inferences being made to a broader population. This could, for
instance, be a result of a self-selection bias in the way a sample was chosen,
something that has become a common problem in the age of Internet polls
and surveys. Errors can also be introduced at the data-processing stage.
Data processing or cleaning can involve geocoding, correcting misspelled
names, harmonizing categories or excluding certain data points altogether
if, for instance, they are considered statistical outliers. A good example of
this kind of error at work is the inaccurate geocoding of IP addresses in a


Bounegru, L. and J. Gray (eds.), _The Data Journalism Handbook:_ _Towards a Critical Data Practice_ .
Amsterdam: Amsterdam University Press, 2021
doi 10.5117/9789462989511_ch19


widely reported study that purported to show a correlation between political
persuasion and consumption of porn (Harris, 2014). Then, of course, we have
the meat of the data journalist’s work, analysis. Any number of statistical
fallacies may affect this portion of the work, such as mistaking correlation
with causation or choosing an inappropriate statistic to summarize the
data set in question.
Given the ways in which collection, treatment and analysis of data can
change a narrative—how does the data journalist reassure the reader that
the sources they have used are reliable and that the work done to derive
their conclusions is sound?
In the case that the data journalist is simply reporting the data or research
findings of a third party, they need not deviate from traditional editorial
standards adopted by many major news outlets. A reference to the institution
that collected and analyzed the data is generally sufficient. For example, a
recent _Financial Times_ chart on life expectancy in the United Kingdom is
accompanied by a note which says: “Source: Club Vita calculations based
on Eurostat data.” In principle, the reader can then make an assessment of
the credibility of the institution quoted. While a responsible journalist will
only report studies they believe to be reliable, the third-party institution is
largely responsible for accounting for the methods through which it arrived
at its conclusions. In an academic context, this will likely include processes
of peer review and in the case of scientific publishing it will invariably
include some level of methodological transparency.
In the increasingly common case where the journalistic organization
produces the data-driven research, then they themselves are accountable
to the reader for the reliability of the results they are reporting. Journalists
have responded to the challenge of accounting for their methods in different
ways. One common approach is to give a description of the general methodology used to arrive at the conclusions within a story. These descriptions
should be framed as far as possible in plain, non-technical language so as to
be comprehensible to the widest possible audience. A good example of this
approach was taken by _The Guardian_ and Global Witness in explaining how
they counted deaths of environmental activists for their “Environmental
Defenders” series (Leather, 2017; Leather & Kyte, 2017).
But—as with all ways of accounting for social life—written accounts have
their limits. The most significant issue with them is that they generally do
not specify the exact procedures used to produce the analysis or prepare
the data. This makes it difficult, or in some cases impossible, to exactly
reproduce steps taken by the reporters to reach their conclusions. In other
words, a written account is generally not a reproducible one. In the example


above, where the data acquisition, processing and analysis steps are relatively
straightforward, there may be no additional value in going beyond a general
written description. However, when more complicated techniques are
employed there may be a strong case for employing reproducible approaches.


**Reproducible Data Journalism**


Reproducibility is widely regarded as a pillar of the modern scientific
method. It aids in the process of corroborating results and identifying and
addressing problematic findings or questionable theories. In principle, the
same mechanisms can help to weed out erroneous or misleading uses of
data in the journalistic context.
A look at one of the most well-publicized methodological errors in recent
academic history can be instructive. In a 2010 paper, Harvard’s Carmen
Reinhart and Kenneth Rogoff purposed to have shown that average real
economic growth slows to -0.1% when a country’s public debt rises to more
than 90% of gross domestic product (Reinhart & Rogoff, 2010). This figure
was then used as ammunition by politicians endorsing austerity measures.
As it turned out, the analysis was based on an Excel error. Rather than
taking the mean of a whole row of countries, Reinhart and Rogoff had made
an error in their formula which meant only 15 out of the 20 countries they
looked at were incorporated. Once the all the countries were considered
the 0.1% “decline” became a 2.2% average increase in economic growth.
The mistake was only picked up when PhD candidate Thomas Herndon and
professors Michael Ash and Robert Pollin looked at the original spreadsheet
that Reinhard and Rogoff had worked off. This demonstrates the importance of having not just the method written out in plain language—but
also having the data and technology used for the analysis itself. But the
Reinhart–Rogoff error perhaps points to something else as well—Microsoft
Excel, and spreadsheet software in general, may not be the best technology
for creating reproducible analysis.
Excel hides much of the process of working with data by design. Formulas—which do most of the analytical work in a spreadsheet—are only
visible when clicking on a cell. This means that it is harder to review the
actual steps taken to reaching a given conclusion. While we will never know
for sure, one may imagine that had Reinhart and Rogoff’s analytical work
been done in a language in which the steps had to be declared explicitly
(e.g., a programming language) the error could have been spotted prior to
publication.


Excel-based workflows generally encourage the removal of the steps taken
to arrive at a conclusion. Values rather than formulas are often copied across
to other sheets or columns, leaving the “undo” key as the only route back
to how a given number was actually generated. “Undo” histories, of course,
are generally erased when an application is closed, and are therefore not a
good place for storing important methodological information.


**The Rise of the Literate Programming Environment: Jupyter**
**Notebooks in the Newsroom**


An emerging approach to methodological transparency is to use so-called
“literate programming” environments. Organizations like _Buzzfeed_, _The_
_New York Times_ and Correctiv are using them to provide human-readable
documents that can also be executed by a machine in order to reproduce
exactly the steps taken in a given analysis. [1]

First articulated by Donald Knuth in the 1980s, literate programming
is an approach to writing computer code where the author intersperses
code with ordinary human language explaining the steps taken (Knuth,
1992). The two main literate programming environments in use today are
Jupyter Notebooks and R Markdown. [2] Both produce human-readable documents that mix plain English, visualizations and code in a single document
that can be rendered in HTML and published on the web. Original data
can be linked to explicitly, and any other technical dependencies such as
third-party libraries will be clearly identified.
Not only is there an emphasis on human-readable explanation, the code
is ordered so as to reflect human logic. Documents written in this paradigm
can therefore read like a set of steps in an argument or a series of answers
to a set of research questions.


The practitioner of literate programming can be regarded as an essayist,
whose main concern is with exposition and excellence of style. Such an
author, with thesaurus in hand, chooses the names of variables carefully
and explains what each variable means. He or she strives for a program
that is comprehensible because its concepts have been introduced in an
order that is best for human understanding, using a mixture of formal
and informal methods that reinforce each other. (Knuth, 1984)


1 https://github.com/TheUpshot
2 http://jupyter.org/, https://rmarkdown.rstudio.com/


A good example of the form is found in _Buzzfeed News_ ’ Jupyter Notebook
detailing how they analyzed trends in California’s wildfires. [3] Whilst the
notebook contains all the code and links to source data required to reproduce
the analysis, the thrust of the document is a narrative or conversation with
the source data. Explanations are set out under headings that follow a logical
line of enquiry. Visualizations and charts are used to bring out key themes.
One aspect of the “literate” approach to programming is that the documents produced (as Jupyter Notebook or R Markdown files) may be capable
of reassuring even those readers who cannot read the code itself that the
steps taken to produce the conclusions are sound. The idea is similar to
Steven Shapin and Simon Schaffer’s account of “virtual witnessing” as a
means of establishing matters of fact in early modern science. Using Robert
Boyle’s experimental program as an example, Shapin and Schaffer set out
the role that “virtual witnessing” had:


The technology of virtual witnessing involves the production in a reader’s
mind of such an image of an experimental scene as obviates the necessity for either direct witness or replication. Through virtual witnessing
the multiplication of witnesses could be, in principle, unlimited. It was
therefore the most powerful technology for constituting matters of fact.
The validation of experiments, and the crediting of their outcomes as
matters of fact, necessarily entailed their realization in the laboratory
of the mind and the mind’s eye. What was required was a technology of
trust and assurance that the things had been done and done in the way
claimed. (Shapin & Schaffer, 1985)


Documents produced by literate programming environments such as Jupyter
Notebooks—when published alongside articles—may have a similar effect
in that they enable the non-programming reader to visualize the steps taken
to produce the findings in a particular story. While the non-programming
reader may not be able to understand or run the code itself, comments
and explanations in the document may be capable of reassuring them that
appropriate steps were taken to mitigate error.
Take, for instance, a recent _Buzzfeed News_ story on children’s home inspections in the United Kingdom. [4] The Jupyter Notebook has specific steps to
check that data has been correctly filtered (Figure 19.1), providing a backstop
against the types of simple but serious mistakes that caught Reinhart and


3 https://buzzfeednews.github.io/2018-07-wildfire-trends/
4 https://www.buzzfeed.com/richholmes/care-price


Figure 19.1. A cell from the _Buzzfeed_ Jupyter notebook with a human readable explanation or
comment explaining that its purpose is to check that the filtering of the raw data was performed
correctly. Source: Jeremy Singer-Vine, _Buzzfeed_ .


Rogoff out. [5] While the exact content of the code may not be comprehensible
to the non-technical reader, the presence of these tests and backstops against
error with appropriately plain English explanations may go some way to
showing that the steps taken to produce the journalist’s findings were sound.


**More Than Just Reproducibility**


Using literate programming environments for data stories does not just
help make them more reproducible.
Publishing code can aid collaboration between organizations. In 2016,
Global Witness published a web scraper that extracted details on companies
and their shareholders from the Papua New Guinea company register. [6]
The initial piece of research aimed to identify the key beneficiaries of the
corruption-prone trade in tropical timber, which is having a devastating
impact on local communities. While Global Witness had no immediate
plans to reuse the scraper it developed, the underlying code was published
on GitHub—the popular code-sharing website.
Not long after, a community advocacy organization, ACT NOW!, downloaded the code from the scraper, improved it and incorporated it into their
iPNG project that lets members of the public cross-check names of company
shareholders and directors against other public interest sources. [7] The scraper
is now part of the core data infrastructure of the site, retrieving data from
the Papua New Guinea company registry twice a year.
Writing code within a literate programming environment can also help to
streamline certain internal processes where others within an organization


5 https://github.com/BuzzFeedNews/2018-07-ofsted-inspections/blob/master/notebooks/00analyze-ofsted-data.ipynb
6 https://github.com/Global-Witness/papua-new-guinea-ipa
7 https://pngiportal.org/


need to understand and check an analysis prior to publication. At Global
Witness, Jupyter Notebooks have been used to streamline the legal review
process. As notebooks set out the steps taken to get a certain finding in a
logical order, lawyers can then make a more accurate assessment of the
legal risks associated with a particular allegation.
In the context of investigative journalism, one area where this can be
particularly important is where assumptions are made around the identity
of specific individuals referenced in a data set. As part of our recent work
on the state of corporate transparency in the United Kingdom, we wanted
to establish which individuals controlled a very large number of companies.
This is indicative (although not proof) of them being a so-called “nominee”
which in certain contexts—such as when the individual is listed as a Person
of Significant Control (PSC)—is illegal. When publishing the list of names of
those individuals who controlled the most companies, the legal team wanted
to know how we knew a specific individual, let’s say John Barry Smith, was
the same as another individual named John B. Smith. [8] A Jupyter Notebook
was able to clearly capture how we had performed this type of deduplication
by presenting a table at the relevant step that set out the fields that were
used to assert the identity of individuals. [9] These same processes have been
used at Global Witness for fact-checking purposes as well.
Jupyter Notebooks have also proven particularly useful at Global Witness
when there is need to monitor a specific data set over time. For instance,
in 2018 Global Witness wanted to establish how the corruption risk in
the London property market had changed over a two-year period. [10] We
acquired a new snapshot from the land registry of properties owned by
foreign companies and reused and published a notebook we had developed
for the same purpose two years previously. [11] This yielded comparable results
with minimal overheads. The notebook has an additional advantage in
this context, too: It allowed Global Witness to show its methodology in the
absence of being able to republish the underlying source data which, at the
time of analysis, had certain licensing restrictions. This is something very
difficult to do in a spreadsheet-based workflow. Of course, the most effective


8 https://www.globalwitness.org/en/campaigns/corruption-and-money-laundering/
anonymous-company-owners/companies-we-keep/
9 https://github.com/Global-Witness/the-companies-we-keep/blob/master/companies_we_
keep_analysis.ipynb
10 https://www.globalwitness.org/en/blog/two-years-still-dark-about-86000-anonymouslyowned-uk-homes/
11 https://github.com/Global-Witness/overseas-companies-land-ownership/blob/master/
overseas_companies_land_ownership_analysis.ipynb


way of accounting for your method will always be to publish the raw data
used. However, journalists often use data that cannot be republished for
reasons of copyright, privacy or source protection.
While literate programming environments can clearly enhance the
accountability and reproducibility of a journalist’s data work, alongside
other benefits, there are some important limitations.
One such limitation is that to reproduce (rather than just follow or “virtually witness”) an approach set out in a Jupyter Notebook or R Markdown
document you need to know how to write, or at least run, code. The relatively
nascent state of data journalism means that there is still a fairly small group
of journalists, let alone general consumers of journalism, who can code. This
means that it is unlikely that the GitHub repositories of newspapers will
receive the same level of scrutiny as, say, peer-reviewed code referenced
in an academic journal where larger portions of the community can actually interrogate the code itself. Data journalism may, therefore, be more
prone to hidden errors in code itself when compared to research with a
more technically literate audience. As Jeff Harris (2013) points out, it might
not be long before we see programming corrections published alongside
traditional reporting corrections. It is worth noting in this context that
tools like Workbench (which is also mentioned in Stray’s chapter in this
book) are starting to be developed for journalists, which promise to deliver
some of the functionality of literate programming environments without
the need to write or understand any code. [12]

At this point it is also worth considering whether the new mechanisms
for accountability in journalism may not just be new means through which
a pre-existing “public” can scrutinize methods, but indeed play a role in the
formation of new types of “publics.” This is a point made by Andrew Barry
in his essay “Transparency as a Political Device”:


Transparency implies not just the publication of specific information; it
also implies the formation of a society that is in a position to recognize and
assess the value of—and if necessary to modify—the information that is
made public. The operation of transparency is addressed to local witnesses,
yet these witnesses are expected to be properly assembled, and their presence validated. There is thus a circular relation between the constitution of
political assemblies and accounts of the oil economy—one brings the other
into being. Transparency is not just intended to make information public,
but to form a public which is interested in being informed. (Barry, 2010)


12 http://workbenchdata.com/


The methods elaborated on above for accounting for data journalistic work in
themselves may play a role in the emergence of new groups of more technically aware publics that wish to scrutinize and hold reporters to account
in ways not previously possible before the advent and use of technologies
like literate programming environments.
This idea speaks to some of Global Witness’ work on data literacy in order
to enhance the accountability of the extractives sector. Landmark legislation in the European Union that forces extractives companies to publish
project-level payments to governments for oil, gas and mining projects,
an area highly vulnerable to corruption, has opened the possibility for far
greater scrutiny of where these revenues actually accumulate. However,
Global Witness and other advocacy groups within the Publish What You
Pay coalition have long observed that there is no pre-existing “public” which
could immediately play this role. As a result, Global Witness and others
have developed resources and training programmes to assemble journalists
and civil society groups in resource-rich countries who can be supported
in developing the skills to use this data to more readily hold companies
to account. One component of this effort has been the development and
publication of specific methodologies for red-flagging suspicious payment
reports that could be corrupt. [13]

Literate programming environments are currently a promising means
through which data journalists are making their methodologies more
transparent and accountable. While data will always remain open to
multiple interpretations, technologies that make a reporter’s assumptions
explicit and their methods reproducible are valuable. They aid collaboration
and open up an increasingly technical discipline to scrutiny from various
publics. Given the current crisis of trust in journalism, a wider embrace of
reproducible approaches may be one important way in which data teams
can maintain their credibility.


**Works Cited**


Barry, A. (2010). Transparency as a political device. In M. Akrich, Y. Barthe, F.
Muniesa, & P. Mustar (Eds.), _Débordements: Mélanges offerts à Michel Callon_
(pp. 21–39). Presses des Mines. http://books.openedition.org/pressesmines/721
Harris, J. (2013, September 19). _The Times_ regrets the programmer error. _Source_ .
https://source.opennews.org/articles/times-regrets-programmer-error/


13 https://www.globalwitness.org/en/campaigns/oil-gas-and-mining/finding-missing-millions/


Harris, J. (2014, May 22). Distrust your data. _Source_ . https://source.opennews.org/
articles/distrust-your-data/
Knuth, D. E. (1984). Literate programming. _The Computer Journal_, _27_ (2), pp. 97–111.
Knuth, D. E. (1992). _Literate programming_ . Center for the Study of Language and
Information.
Leather, B. (2017, July 13). Environmental defenders: Who are they and how do we
decide if they have died in defence of their environment? _The Guardian_ . https://
www.theguardian.com/environment/2017/jul/13/environmental-defenderswho-are-they-and-how-do-we-decide-if-they-have-died-in-defence-of-theirenvironment
Leather, B., & Kyte, B. (2017, July 13). Defenders: Methodology. Global Witness.
https://www.globalwitness.org/en/campaigns/environmental-activists/
defendersmethodology/
Reinhart, C. M., & Rogoff, K. S. (2010). _Growth in a time of debt_ (Working Paper
No. 15639). National Bureau of Economic Research. https://doi.org/10.3386/w15639
Shapin, S., & Schaffer, S. (1985). _Leviathan and the air-pump: Hobbes, Boyle, and the_
_experimental life_ . Princeton University Press.


**About the Author**


**Sam Leon** is Data Investigations Lead at Global Witness, where he researches
and campaigns against corruption and environmental destruction.



##### **20. Working Openly in Data Journalism**

_Natalia Mazotte_


**Abstract**
This chapter examines some examples and benefits of data journalists
working more openly, as well as some ways to get started.


**Keywords:** data journalism, open source, free software, transparency,
trust, programming


Many prominent software and web projects—such as Linux, Android,
Wikipedia, WordPress and TensorFlow—have been developed collaboratively based on a free flow of knowledge. [1] Stallman (2002), a noted hacker
who founded the GNU Project and the Free Software Foundation, says that
when he started working at MIT in 1971, sharing software source code was
as common as exchanging recipes.
For years such an open approach was unthinkable in journalism. Early
in my career as a journalist, I worked with open-source communities in
Brazil and began to see openness as the only viable path for journalism.
But transparency hasn’t been a priority or core value for journalists and
media organizations. For much of its modern history, journalism has been
undertaken in a paradigm of competition over scarce information.
When access to information is the privilege of a few and when an important finding is only available to eyewitnesses or insiders, ways of ensuring
accountability are limited. Citing a document or mentioning an interview
source may not require such elaborate transparency mechanisms. In some
cases, preserving the secrecy means ensuring the security of the source,
and is even desirable. But when information is abundant, not sharing the
_how-we-got-there_ may deprive the reader of the means to understand and
make sense of a story.


1 This chapter was written by Natalia Mazotte with contributions from Marco Túlio Pires.


Bounegru, L. and J. Gray (eds.), _The Data Journalism Handbook:_ _Towards a Critical Data Practice_ .
Amsterdam: Amsterdam University Press, 2021
doi 10.5117/9789462989511_ch20


As journalists both report on and rely on data and algorithms, might they
adopt an ethos which is similar to that of open-source communities? What
are the advantages of journalists who adopt emerging digital practices and
values associated with these communities? This chapter examines some
examples and benefits of data journalists working more openly, as well as
some ways to get started. [2]


**Examples and Benefits of Openness**


_The Washington Post_ provided an unprecedented look at the prescription
opioid epidemic in the United States by digging into a database on the sales
of millions of painkillers. [3] They also made the data set and its methodology
publicly accessible. This enabled local reporters from over 30 states to publish
more than 90 articles about the impact of this crisis in their communities
(Sánchez Díez, 2019). [4]

Two computational journalists analyzed Uber’s surge pricing algorithm
and revealed that the company seems to offer better service in areas with
more White people (Stark & Diakopoulos, 2016). The story was published by
_The Washington Post_, and the data collection and analysis code used were
made freely available on GitHub, an online platform that helps developers
store and manage their code. [5] This meant that a reader who was looking at
the database and encountered an error was able to report this to the authors
of the article, who were in turn able to fix the bug and correct the story.
_Gênero e Número_ (Gender and number), a Brazilian digital magazine I
co-founded, ran a project to classify more than 800,000 street names to
understand the lack of female representation in Brazilian public spaces. We
did this by running a Python script to cross-reference street names with a
database of names from the Brazilian National Statistical office (Mazotte
& Justen, 2017). The same script was subsequently used by other initiatives
to classify data sets that did not contain gender information—such as lists
of electoral candidates and magistrates (Justen, 2019).
Working openly and making various data sets, tools, code, methods and
processes transparent and available can potentially help data journalists in a


2 For more on data journalism and open-source, see also chapters by Leon, Baack, and Pitts
and Muscato in this book.
3 https://www.washingtonpost.com/national/2019/07/20/opioid-files/
4 https://www.washingtonpost.com/national/2019/08/12/post-released-deas-data-pain-pillsheres-what-local-journalists-are-using-it/
5 https://github.com/comp-journalism/2016-03-wapo-uber


number of ways. Firstly, it can help them to improve the quality of their work.
Documenting processes can encourage journalists to be more organized,
more accurate and less likely to miss errors. It can also lighten the burden
of editing and reviewing complex stories, enabling readers to report issues.
Secondly, it can broaden reach and impact. A story that can be built upon
can gain different perspectives and serve different communities. Projects
can take on a life of their own, no longer limited by the initial scope and
constraints of their creators. And thirdly, it can foster data literacy amongst
journalists and broader publics. Step-by-step accounts of your work mean
that others can follow and learn—which can enrich and diversify data
ecosystems, practices and communities.
In the so-called “post-truth” era there is also potential to increase public
trust in the media, which has reached a new low according to the 2018
Edelman Trust Barometer. [6] Working openly could help decelerate or even
reverse this trend. This can include journalists talking more openly about
how they reach their conclusions and providing more detailed “how tos,” in
order to be honest about their biases and uncertainties, as well as to enable
conversations with their audiences. [7]

As a caveat, practices and cultures of working openly and transparently in
data journalism are an ongoing process of exploration and experimentation.
Even as we advance our understanding of potential benefits, consideration
is needed to understand when transparency is valuable, or might be less of
a priority, or might even be harmful. For example, sometimes it’s important
to keep data and techniques confidential in order to protect the integrity
of the investigation itself, as happened in the case of the Panama Papers.


**Ways of Working Openly**


If there are no impediments (and this should be analyzed on a case-bycase basis) then one common approach to transparency is through the
methodology section, also known as the “nerd box.” This can come in a
variety of formats and lengths, depending on the complexity of the process
and the intended audience.


6 https://www.edelman.com/research/2018-edelman-trust-barometer; https://www.edelman.
com/sites/g/files/aatuss191/files/2018-10/2018_Edelman_Trust_Barometer_Global_Report_FEB.
pdf
7 For more on issues around uncertainty in data journalism, see Anderson’s chapter in this
volume.


If your intention is to reach a wider audience, a box inside the article
or even a footnote with a succinct explanation of your methods may be
sufficient. Some publications opt to publish stand-alone articles explaining how they reported the story. In either case, it is important to avoid
jargon, explain how data was obtained and used, ensure readers don’t miss
important caveats, and explain in the most clear and direct way how you
reached your conclusion.
Many media outlets renowned for their work on data journalism—such
as _FiveThirtyEight_, _ProPublica_, _The_ _New York Times_ and the _Los Angeles_
_Times—_ have repositories on code-sharing platforms such as GitHub. The
_Buzzfeed News_ team even has an index of all its open-source data, analysis,
libraries, tools and guides. [8] They release not only the methodology behind
their reporting, but also the scripts used to extract, clean, analyze and
present data. This practice makes their work reproducible (as discussed
further in Leon’s chapter in this volume) as well as enabling interested readers to explore the data for themselves. As scientists have done for centuries,
these journalists are inviting their peers to check their work and see if they
can arrive at the same conclusions by following the documented steps.
It is not simple for many newsrooms to incorporate these levels of
documentation and collaboration into their work. In the face of dwindling
resources and shrinking teams, journalists who are keen to document
their investigations can be discouraged by their organizations. This brings
us to the constraints that journalists face: Many news organizations are
fighting for their lives, as their role in the world and their business models
are changing. In spite of these challenges, embracing some of the practices of
free and open-source communities can be a way to stand out, as a marker of
innovation and as a way of building trust and relationships with audiences
in an increasingly complex and fast-changing world.


**Works Cited**


Justen, A. (2019, May 31). Classificando nomes por gênero usando dados públicos | Brasil.IO—Blog. _Brasil.IO_ . https://blog.brasil.io/2019/05/31/
classificando-nomes-por-genero-usando-dados-publicos/
Mazotte, N., & Justen, A. (2017, April 5). Como classificamos mais de 800 mil logradouros brasileiros por gênero. _Gênero e Número_ . http://www.generonumero.
media/como-classificamos-mais-de-800-mil-logradouros-brasileiros-por-genero/


8 https://github.com/BuzzFeedNews/everything#guides


Sánchez Díez, M. (2019, November 26). _The Post_ released the DEA’s data on pain
pills. Here’s what local journalists are using it for. _The Washington Post_ . https://
www.washingtonpost.com/national/2019/08/12/post-released-deas-data-painpills-heres-what-local-journalists-are-using-it/
Stallman, R. M. (2002). _Free software, free society: Selected essays of Richard M._
_Stallman_ (J. Gay, Ed.). GNU Press.
Stark, J., & Diakopoulos, N. (2016, March 10). Uber seems to offer better service in
areas with more White people. That raises some tough questions. _The Wash-_
_ington Post_ . https://www.washingtonpost.com/news/wonk/wp/2016/03/10/
uber-seems-to-offer-better-service-in-areas-with-more-white-people-thatraises-some-tough-questions/


**About the Author**


**Natalia Mazotte** is a Brazilian data journalist and entrepreneur. She cofounded the news start-up _Gênero e Número_ and the School of Data Brazil.


##### **21. Making Algorithms Work for** **Reporting**

_Jonathan Stray_


**Abstract**
Sophisticated data analysis algorithms can greatly benefit investigative
reporting, but most of the work is getting and cleaning data.


**Keywords:** algorithms, machine learning, computational journalism,
data journalism, investigative journalism, data cleaning


The dirty secret of computational journalism is that the “algorithmic” part
of a story is not the part that takes all of the time and effort.
Don’t misunderstand me: Sophisticated algorithms can be extraordinarily
useful in reporting, especially investigative reporting. Machine learning
(training computers to find patterns) has been used to find key documents
in huge volumes of data. Natural language processing (training computers to
understand language) can extract the names of people and companies from
documents, giving reporters a shortcut to understanding who’s involved in
a story. And journalists have used a variety of statistical analyses to detect
wrongdoing or bias.
But actually running an algorithm is the easy part. Getting the data,
cleaning it and following up algorithmic leads is the hard part.
To illustrate this, let’s take a success for machine learning in investigative
journalism, _The Atlanta Journal-Constitution_ ’s remarkable story on sex
abuse by doctors, “License to Betray” (Teegardin et al., 2016). Reporters
analyzed over 100,000 doctor disciplinary records from every US state, and
found 2,400 cases where doctors who had sexually abused patients were
allowed to continue to practice. Rather than reading every report, they first
drastically reduced this pile by applying machine learning to find reports
that were likely to concern sexual abuse. They were able to cut down their


Bounegru, L. and J. Gray (eds.), _The Data Journalism Handbook:_ _Towards a Critical Data Practice_ .
Amsterdam: Amsterdam University Press, 2021
doi 10.5117/9789462989511_ch21


pile more than 10 times, to just 6,000 documents, which they then read and
reviewed manually.
This could not have been a national story without machine learning,
according to reporter Jeff Ernsthausen. “Maybe there’s a chance we would
have made it a regional story,” he said later (Diakopoulos, 2019).
This is as good a win for algorithms in journalism as we’ve yet seen, and
this technique could be used far more widely. But the machine learning
itself is not the hard part. The method that Ernsthausen used, “logistic
regression,” is a standard statistical approach to classifying documents
based on which words they contain. It can be implemented in scarcely a
dozen lines of Python, and there are many good tutorials online.
For most stories, most of the work is in setting things up and then
exploiting the results. Data must be scraped, cleaned, formatted, loaded,
checked, and corrected—endlessly prepared. And the results of algorithmic
analysis are often only leads or hints, which only become a story after large
amounts of very manual reporting, often by teams of reporters who need
collaboration tools rather than analysis tools. This is the unglamorous
part of data work, so we don’t teach it very well or talk about it much. Yet
it’s this preparation and follow-up that takes most of the time and effort
on a data-driven story.
For “License to Betray,” just getting the data was a huge challenge. There is
no national database of doctor disciplinary reports, just a series of state-level
databases. Many of these databases do not contain a field indicating why
a doctor was disciplined. Where there is a field, it often doesn’t reliably
code for sexual abuse. At first, the team tried to get the reports through
freedom of information requests. This proved to be prohibitively expensive,
with some states asking for thousands of dollars to provide the data. So,
the team turned to scraping documents from state medical board websites
(Ernsthausen, 2017). These documents had to be OCR’d (turned into text)
and loaded into a custom web-based application for collaborative tagging
and review.
Then the reporters had to manually tag several hundred documents
to produce training data. After machine learning ranked the remaining
100,000, it took several more months to manually read the 6,000 documents that were predicted to be about sex abuse, plus thousands of other
documents containing manually picked key words. And then, of course,
there was the rest of the reporting, such as the investigation of hundreds
of specific cases to flesh out the story. This relied on other sources, such
as previous news stories and, of course, personal interviews with the
people involved.


The use of an algorithm—machine learning—was a key, critical part
of the investigation. But it was only a tiny amount of the time and effort
spent. Surveys of data scientists consistently show that most of their work
is data “wrangling” and cleaning—often up to 80%—and journalism is no
different (Lohr, 2014).
Algorithms are often seen as a sort of magic ingredient. They may seem
complex or opaque, yet they are unarguably powerful. This magic is a lot
more fun to talk about than the mundane work of preparing data or following up a long list of leads. Technologists like to hype their technology,
not the equally essential work that happens around it, and this bias for
new and sophisticated tools sometimes carries over into journalism. We
should teach and exploit technological advances, certainly, but our primary
responsibility is to get journalism done, and that means grappling with the
rest of the data pipeline, too.
In general, we underappreciate the tools used for data preparation.
OpenRefine is a long-standing hero for all sorts of cleaning tasks. Dedupe.
io is machine learning applied to the problem of merging near-duplicate
names in a database. Classic text-wrangling methods like regular expressions
should be a part of every data journalist’s education. In this vein, my current
project, Workbench, is focused on the time-consuming but mostly invisible
work of preparing data for reporting—everything that happens before the
“algorithm.” It thus aims to make the whole process more collaborative,
so reporters can work together on large data projects and learn from each
other’s work, including with machines.
Algorithms are important to reporting, but to make them work, we have to
talk about all of the other parts of data-driven journalism. We need to enable
the whole workflow, not just the especially glamorous, high-tech parts.


**Works Cited**
Diakopoulos, N. (2019). _Automating the news: How algorithms are rewriting the_
_media_ . Harvard University Press.
Ernsthausen, J. (2017). Doctors and sex abuse. NICAR 2017, Jacksonville. https://
docs.google.com/presentation/d/1keGeDk_wpBPQgUOOhbRarPPFbyCculTObGLeAhOMmEM/edit?usp=embed_facebook
Lohr, S. (2014, August 17). For big-data scientists, “janitor work” is key hurdle to
insights. _The New York Times_ . https://www.nytimes.com/2014/08/18/technology/
for-big-data-scientists-hurdle-to-insights-is-janitor-work.html
Teegardin, C., Robbins, D., Ernsthausen, J., & Hart, A. (2016, July 5). License to betray.
_The Atlanta Journal-Constitution_, Doctors & Sex Abuse. http://doctors.ajc.com/
doctors_sex_abuse/?ecmp=doctorssexabuse_microsite_nav


**About the Author**


**Jonathan Stray**, a Research Fellow at Partnership on AI, previously taught
the dual masters degree in Computer Science and Journalism at Columbia
University and built software for investigative journalism.



##### **22. Journalism With Machines?** **From Computational Thinking to** **Distributed Cognition**

_Eddy Borges-Rey_


**Abstract**
This chapter reflects on the ways news automation increasingly distributes
journalistic knowledge and thought processes.


**Keywords:** automated journalism, distributed cognition, computational
thinking, extended mind, databases, machine learning


Imagine you are a journalist in the not so distant future. You are working
on a story, and in order to get the insight you are looking for, you ask your
conversational agent (who you affectionately call Twiki) to stitch together
over 15 anonymized databases. Given the magnitude and complexity of
the fused data sets, visualization software is too rudimentary to isolate the
anomalies you are searching for. So, using your brain implant, you plug into
the system and easily navigate the abstraction of the data sets. Although,
individually, each redacted data set is effective in protecting the identity
and the personal data of the people listed, when combined, you are able
to infer the identity of some top-profile individuals and put into context
their personal data. Realizing the potential legal implications of revealing
the names and the data attached to them, you ask Twiki to run a neural
network to determine whether disclosing this information has ethical or
legal implications. The network runs a “n+” number of simulations of virtual
journalists making decisions based on a number of codes of ethics and
regulatory frameworks. Whilst this runs in the background, you manage to
isolate a few outliers and identify a couple of interesting trends. Since you
want to make sure the anomalies have something to add to the story, and are


Bounegru, L. and J. Gray (eds.), _The Data Journalism Handbook:_ _Towards a Critical Data Practice_ .
Amsterdam: Amsterdam University Press, 2021
doi 10.5117/9789462989511_ch22


not simply errors, you ask Twiki to check through archival historic records
to see if the outliers coincide with any major historical event. In addition,
you ask Twiki to run a predictive model to calculate the likelihood that
the identified trends will persist for the foreseeable future, thus triggering
worrying implications.
This brief, fictional introduction is based on a fascinating conversation
I had with former _Times_ data journalist Nicola Hughes a few years ago.
Although the scene it describes could well have come out of Philip K. Dick’s
“The Minority Report,” it actually refers to a range of tools and techniques
that are either already available and widely used, or in rapid development.
More importantly, it also refers to a kind of journalistic workflow and professional mindset emerging in newsrooms, in a world where journalists are
increasingly engaging with data and computation is becoming indispensable.
These recent changes reflect how historically, every time a major technological innovation has been introduced into the news production workflow,
news reporting itself has not only been disrupted and consequently transformed, but journalists’ thought processes and working professional ideals
have invariably been modified.
Today, as we move beyond the era of big data to the era of artificial
intelligence (AI) and automation, principles and working practices that hail
from computing and data science become ever more pervasive in journalism.
As Emily Bell, Founding Director of the Tow Center for Digital Journalism
at Columbia University, puts it:


Every company in every field, and every organization, whether they are
corporate or public sector, will have to think about how they reorient
themselves around AI in exactly the same way that 20 years ago they had to
think about the way they reoriented themselves around web technologies.
(Bell, personal communication, September 7, 2017)


In this context, this chapter reflects on the ways journalists who work
closely with data and automated processes internalize a range of computing
principles, that on the one hand augment their journalistic abilities, and on
the other have begun to modify the very cornerstone of their journalistic
approaches and ideals.
The chapter, thus, explores a range of theoretical concepts that could
serve as a framework to envision journalistic cognition in an environment
of pervasive computation. I adopt the notion of extended cognition to
stimulate further discussion on the ways in which journalistic cognition
is nowadays dependent on (and therefore distributed across) the machines


used to report the news. Through this discussion I hope to encourage future
work to investigate the role of computation in journalistic situations, including empirical work to test and further specify the concept of distributed
journalistic cognition. This line of inquiry could be particularly useful for
professional journalists who want to be aware of, and engage with, the
changes journalism is likely to experience if datafication and automation
become ubiquitous in news production.


**Computational Thinking**


In an attempt to trace the historical meaning of the concept of computation,
Denning and Martell (2015) suggest that “[c]omputation was taken to be
the mechanical steps followed to evaluate mathematical functions [and]
computers were people who did computations.” In the 1980s, however, the
concept was more frequently associated with a new way of doing science,
thus shifting its emphasis from machines to information processes (Denning
& Martell, 2015).
This shift in emphasis is critical for my argument, as it aligns the ultimate
goals of news reporting and computation: Journalism is also about managing
information processes—in very general terms, the journalist’s job consists of
streamlining the flow of information, curating it and packaging it in a format
that is palatable to an audience. Here, I would argue that the pervasiveness of
a computational mindset in news reporting is partially due to the similarities
that exist between both professional practices.
Both computing and journalism are formulaic, about solving problems
and require syntactical mastery. Wing (2008) remarks that “[o]perationally,
computing is concerned with answering ‘How would I get a computer to
solve this problem?’” (p. 3719), and this requires a relatively high level of
computational thinking. As computation becomes a norm in newsrooms,
computational thinking is employed by an increasing number of journalists
to approach data stories. Bradshaw, for instance, argues that computational
thinking “is at the heart of a data journalist’s work,” enabling them “to solve the
problems that make up so much of modern journalism, and to be able to do so
with the speed and accuracy that news processes demand” (Bradshaw, 2017).
Computational thinking is the reflexive process through which a set of
programmatic steps are taken to solve a problem (Bradshaw, 2017; Wing,
2006, 2008). Wing contends that “the essence of computational thinking is
abstraction” and that “in computing, we abstract notions beyond the physical
dimensions of time and space” (Wing, 2008, p. 3717) to solve problems,


design systems and understand human behaviour (Wing, 2006). The author
argues that in order to answer the question “How would I get a computer to
solve this problem?” computing professionals have to identify appropriate
abstractions (Wing, 2008, p. 3717) which are suitable for designing and
implementing a programmatic plan to solve the problem at hand.
Since the introduction of automation technologies in newsrooms, journalists working with computing professionals have faced a similar question:
“How would I get a computer to investigate or write a news story to human
standards?” Gynnild proposes that the infusion of computational thinking
into professional journalism challenges the “fundamental thought system in
journalism from descriptive storytelling to abstract reasoning, autonomous
research and visualization of quantitative facts” that equips journalists
with “complementary, logical and algorithmic skills, attitudes, and values”
(Gynnild, 2014).
Of course, this is not to say that the idea of “computational” abstraction is a new one to journalists. In fact, journalists working on beats like
finance, business, real estate or education exert abstraction on a daily basis
to understand complex dynamics such as market performance, stock returns,
household net worth, etc. And interestingly, as Myles (2019) remarks, contrary
to expectations that automation would free up journalists from onerous tasks,
it has introduced a range of new editorial activities not previously performed
by journalists. For instance, he explains that the introduction of image
recognition into the workflow of the Associated Press has seen journalists
and photographers having to engage with tasks traditionally associated with
machine learning, like labelling of training data, evaluation of test results,
correcting metadata or generating definitions for concepts (Myles, 2019).


**Cognitive Projection and Extended Creativity**


So far, I have argued that journalists who, as part of their job, have to engage
with the computational problems introduced by news automation, see their
workflows and editorial responsibilities transformed. _The Wall Street Journal_, for
instance, recently advertised for positions such as Machine Learning Journalist,
Automation Editor and Emerging Processes Editor, all associated with the
expansion of AI and automation. As a result of these kinds of infrastructural
expansions, and the subsequent diversification of editorial responsibilities
prompted by them, journalists often find themselves asking questions that
project them into the shoes of a machine that has to think and perform like a
journalist. An interesting paradox, which brings equally interesting challenges.


This idea of projection, I believe, is becoming prevalent in news automation. Take, for instance, the quintessential journalistic endeavour: Writing a
news story. If we deconstruct the process, in general terms, journalists have
to use their creativity to put together an account of events that engages and/
or informs the public. The question, then, is: How do I get a machine to write
news that reads as if it were written by a human reporter? Journalists and
technologists have collaborated over the last five years to project themselves,
in an attempt to solve this question. A good example, on this front, is the
implementation of natural language generation (NLG) technologies to
automate the production of news stories. But counter to what we could
expect, the process still involves human reporters writing templates of
news stories, which contain blank spaces that are subsequently filled in
by automation software using a database. This process, which has been
quite successful in news organizations such as the Associated Press, and
in RADAR, a collaboration between the Press Association and Urbs Media,
seeks to augment the speed and scale of the news production operation in
areas such as sports, company earnings and local news.
Creativity within this realm takes a new form, in which coder-journos
have had to rethink storytelling as a machine that decodes and recodes
the news-writing process. Instead of discerning which interview would
better substantiate an argument or what words would make for a stronger
headline, the goal has shifted to choosing which configuration of conditional
statements would be more efficient in making the automated system decide
which headline would appeal more effectively to the audience of the news
organization where it functions. Following the principles of human–computer interaction (HCI) and user experience (UX) design, coder-journos have
to anticipate the ways users want to engage with automated informational
experiences, the potential ways in which they will navigate the different
layers of information and the confines of the news piece. Wheeler (2018),
conceptualizing the notion of extended creativity, explains that there are
cases of intellectual creation in which “the material vehicles that realize
the thinking and thoughts concerned are spatially distributed over brain,
body and world.” The concept of extended creativity then works well as
a framework to explicate the idea that the mind of a journalist working
with data and automation now functions in close connection with a series
of automations, spanning into a series of Python libraries, Jupyter Notebooks, data sets, data analytics tools and online platforms. This dynamic
consequently brings a series of additional challenges worthy of attention.
For example, Mevan Babakar, head of automated fact-checking at Full
Fact, explains that one of the challenges they face with their automated


fact-checker is context. She uses as an example the claim of former UK
prime minister Theresa May that her government allocated more resources
to the National Health Service (NHS) than the opposition Labour Party
promised in their manifesto. And although the claim was fact-checked as
accurate, for it to be meaningful and useful to the public, it needs to be
understood within a wider context: The allocation was not enough for the
NHS to perform efficiently (Babakar, personal communication, August 16,
2018). Therefore, as automated systems are not yet capable of making such
contextual connections between sources of information, Babakar and her
team have to resort to questions like “How do I get an automated fact-checker
to understand the nuances of context?”


**Journalistic Distributed Cognition**


To conclude, I would like to further explore the idea of a journalistic
distributed cognition and the questions it raises. Anderson, Wheeler and
Sprevak (2018) argue that as computers become pervasive in human activity,
cognition “spread[s] out over the brain, the non-neural body and . . . an
environment consisting of objects, tools, other artefacts, texts, individuals,
groups and/or social/institutional structures.” In journalism, this means that,
at present, as journalists use networked software and hardware to augment
their capacity to produce news at scale and speed, their cognition becomes
distributed across the range of platforms and tools they use. This of course,
provides them with unlimited access to most of human knowledge online.
However, this idea of portable knowledge and distributed cognition begs
the question of who owns and manages journalists’ access to that wealth of
knowledge and “free” analytical power. Who enables journalistic distributed
cognition? This issue, worthy of deeper discussion, is a thorny one, as we
experienced when Google shut down its online data visualization tool Google
Fusion Tables. After the closure of the platform, dozens of data journalism
projects that had been developed with the tool became unavailable as they
were no longer supported by the company.
In this context, as journalists engage with computational dynamics
on a daily basis, their computational thinking becomes normalized and
facilitates the projection of their cognition into the machines they employ
for their daily journalistic routines. As journalistic knowledge becomes
distributed, does the same happen to journalistic authority and control?
Inexorably, distribution shifts the boundaries that provide journalists with
control over their routines and professional cultures, thus impacting on


their epistemological authority. Looking ahead, as we did in this chapter’s
fictional introduction, distribution could also create an array of associated
risks, once journalists begin to delegate important ethical considerations
and decisions to machines. It is important then, that the infrastructure they
use to distribute their cognition is open, and available for public scrutiny, if
the cornerstone ideals of journalism are to be preserved in the age of data
and automation.


**Works Cited**


Anderson, M., Wheeler, M., & Sprevak, M. (2018). Distributed cognition and the
humanities. In M. Anderson, D. Cairns, & M. Sprevak (Eds.), _Distributed cognition_
_in classical antiquity_ (pp. 1–17). Edinburgh University Press.
Bradshaw, P. (2017). Computational thinking and the next wave of data journalism. _Online Journalism Blog_ . https://onlinejournalismblog.com/2017/08/03/
computational-thinking-data-journalism/
Denning, P. J., & Martell, C. H. (2015). _Great principles of computing_ . The MIT Press.
Gynnild, A. (2014). Journalism innovation leads to innovation journalism: The
impact of computational exploration on changing mindsets. _Journalism_, _15_ (6),
713–730. https://doi.org/10.1177/1464884913486393
Myles, S. (2019, February 1). _Photomation or fauxtomation? Automation in the news-_
_room and the impact on editorial labour: A case study._ [Technology]. Computation
+ Journalism Symposium 2019, University of Miami.
Wheeler, M. (2018). Talking about more than heads: The embodied, embedded and
extended creative mind. In B. Gaut & M. Kieran (Eds.), _Creativity and philosophy_
(pp. 230–250). Routledge. http://dspace.stir.ac.uk/handle/1893/26296
Wing, J. M. (2006). Computational thinking. _Communications of the ACM_, _49_, 33–35.
Wing, J. M. (2008). Computational thinking and thinking about computing.
_Philosophical Transactions of the Royal Society A: Mathematical, Physical and_
_Engineering Sciences_, _366_ (1881), 3717–3725. https://doi.org/10.1098/rsta.2008.0118


**About the Author**


**Eddy Borges-Rey** is an Associate Professor in Digital Journalism and Emerging Media at Northwestern University in Qatar, and a former broadcast
journalist.


###### Experiencing Data


##### **23. Ways of Doing Data Journalism**

_Sarah Cohen_


**Abstract**
This chapter explores the various ways that data journalism has evolved
and the different forms it takes, from traditional investigative reporting
to news apps and visualizations.


**Keywords:** investigative journalism, news applications, data visualization,
explanatory journalism, precision journalism


**data** ( _**dey-**_ _tah)_ **:** a body of facts or information; individual facts, statistics
or items of information (“Data,” n.d.)
**journalism:** the occupation of reporting, writing, editing, photographing,
or broadcasting news or of conducting any news organization as a business
(“Journalism,” n.d.)


If you’re reading this handbook, you’ve decided that you want to learn a little
about the trade that’s become known as data journalism. But what, exactly,
does that mean in an age of open data portals, dazzling visualizations and
freedom of information battles around the world?
A dictionary definition of the two words doesn’t help much—put together,
it suggests that data journalism is an occupation of producing news made
up of facts or information. Data journalism has come to mean virtually any
act of journalism that touches electronically held records and statistics—in
other words, virtually all of journalism.
That’s why a lot of the people in the field don’t think of themselves as data
journalists—they’re more likely to consider themselves explanatory writers,
graphic or visual journalists, reporters, audience analysts, or news application
developers—all more precise names for the many tribes of this growing field.
That’s not enough, so add in anything in a newsroom that requires the use


Bounegru, L. and J. Gray (eds.), _The Data Journalism Handbook:_ _Towards a Critical Data Practice_ .
Amsterdam: Amsterdam University Press, 2021
doi 10.5117/9789462989511_ch23


of numbers, or anything that requires computer programming. What was
once a garage band has now grown big enough to make up an orchestra.
Data journalism is not very new. In fact, if you think of “data” as some sort
of systematic collection, then some of the earliest data journalism in the
United States dates back to the mid-1800s, when Frank Leslie, publisher of
_Frank Leslie’s Illustrated Newspaper_, hired detectives to follow dairy carts
around New York City to document mislabelled and contaminated milk.
Scott Klein (2016), a managing editor for the non-profit investigative site
_ProPublica_, has documented a fascinating history of data journalism also
dating to the 1800s, in which newspapers taught readers how to understand
a bar chart. Chris Anderson also explores different genealogies of data
journalism in the 1910s, 1960s and 2010s in his chapter in this volume.
With these histories, taxonomies of different branches of data journalism
can help students and practitioners clarify their career preferences and
the skills needed to make them successful. These different ways of doing
data journalism are presented here in an approximate chronology of the
development of the field.


**Empirical Journalism, or Data in Service of Stories**


Maurice Tamman of Reuters coined the term “empirical journalism” as a way
to combine two data journalism traditions. Precision journalism, developed
in the 1960s by Philip Meyer, sought to use social science methods in stories.
His work ranged from conducting a survey of rioters in Detroit to directing the
data collection and analysis of an investigation into racial bias in Philadelphia
courts. He laid the groundwork for investigations for a generation. Empirical
journalism can also encompass what became known as computer-assisted
reporting in the 1990s, a genre led by Eliot Jaspin in Providence, Rhode Island. In this branch, reporters seek out documentary evidence in electronic
form—or create it when they must—to investigate a tip or a story idea.
More recently, these reporters have begun using artificial intelligence
and machine learning to assist in finding or simplifying story development.
They can be used to help answer simple questions, such as the sex of a patient
harmed by medical devices when the government tried to hide that detail. Or
they can be used to identify difficult patterns, such Peter Aldhous’ analysis
of spy planes for _Buzzfeed_ (Aldhous, 2017; Woodman, 2019).
These reporters are almost pure newsgatherers—their goal is not to
produce a visualization nor to tell stories with data. Instead, they use records
to explore a potential story. Their work is integral to the reporting project,


often driving the development of an investigation. They are usually less
involved in the presentation aspects of a story.
Arguably the newest entry into this world of “data journalism” could be
the growing impact of visual and open-source investigations worldwide. This
genre, which derives from intelligence and human rights research, expands
our notion of “data” into videos, crowdsourced social media and other digital
artefacts. While it’s less dependent on coding, it fits solidly in the tradition
of data journalism by uncovering—through original research—what others
would like to hold secret.
One of the most famous examples, _Anatomy of a Killing_ from BBC’s Africa
Eye documentary strand, uncovers where, precisely, the assassination of a
family occurred in Cameroon, when it happened, and helps identify who
was involved—after the Cameroonian government denied it as “fake news”
(BBC News, 2018). The team used tools ranging from Google Earth to identify
the outline of a mountain ridge to Facebook for documenting the clothing
worn by the killers.


**Data Visualization**


Looking at the winners of the international Data Journalism Awards would
lead a reader to think that visualization is the key to any data journalism. [1]
If statistics are currency, visualization is the price of admission to the club.
Visualizations can be an important part of a data journalist’s toolbox. But
they require a toolkit that comes from the design and art world as much as the
data, statistics and reporting worlds. Alberto Cairo, one of the most famous
visual journalists working in academia today, came from the infographics
world of magazines and newspapers. His work focuses on telling stories
through visualization—a storytelling role as much as a newsgathering one.


**News Applications**


At _ProPublica_, most major investigations start or end with a news application—a site or feature that provides access to local or individual data through
an engaging and insightful interface. _ProPublica_ has become known for its
news apps, and engineers who began their careers in coding have evolved
into journalists who use code, rather than words, to tell stories.


1 See Loosen’s chapter in this volume.


_ProPublica_ ’s Ken Schwenke, a developer by training who has worked in
newsrooms including the _Los Angeles Times_ and _The New York Times_, became
one of the nation’s leading journalists covering hate crimes in the United
States as part of the site’s Documenting Hate project, which revolved around
stories crowdsourced through _ProPublica_ ’s news application.


**Data Stories**


The term “data journalism” came of age as reporters, statisticians and other
experts began writing about data as a form of journalism in itself. Simon
Rogers, the creator of _The Guardian_ ’s Datablog, popularized the genre.
_FiveThirtyEight_, _Vox_ and, later, _The New York Times_ ’ Upshot became this
branch’s standard bearers. Each viewed their role a little differently, but
they converged on the idea that statistics and analysis are newsworthy on
their own.
Some became best known for their political forecasts, placing odds on US
presidential races. Others became known for finding quirky data sets that
provide a glimpse into the public’s psyche. One example of this is the 2014
map of baseball preferences derived from Facebook preferences in the US
Table stakes. The entry point for this genre is a data set, and expertise in a
subject matter is the way these practitioners distinguish themselves from
the rest of the field. In fact, Nate Silver and others who defined this genre
came not from a journalism background, but from the worlds of statistics
and political science.
Amanda Cox, the editor of _The New York Times_ ’ Upshot, has said she
sees the site’s role as occupying the space between known hard facts and
the unknowable—journalism that provides insight from expert analysis
of available data that rides the border between pure fact and pure opinion
(Cox, personal communication, n.d.).


**Investigating Algorithms**


An emerging field of data journalism is really journalism about technology—the “algorithmic accountability” field, a term coined by Nicholas
Diakopoulos at Northwestern University. [2] Reporters Julia Angwin and Jeff
Larson left _ProPublica_ to pursue this specialty by founding The Markup, a


2 For more on this field, see Diakopoulos’ and Elmer’s chapters in this book.


site that Angwin says will hold technology companies accountable for the
results that their machine learning and artificial intelligence algorithms
create in our society, from decisions on jail sentences to the prices charged
based on a consumer’s zip code.
This reporting has already prompted YouTube to review its recommendation engines to reduce its tendency to move viewers into increasingly violent
videos. It has held Facebook to account for its potentially discriminatory
housing ads, and has identified price discrimination in online stores based
on a user’s location (Dwoskin, 2019).


**Works Cited**


Aldhous, P. (2017, August 8). We trained a computer to search for hidden spy planes.
This is what it found. _BuzzFeed News_ . https://www.buzzfeednews.com/article/
peteraldhous/hidden-spy-planes
BBC News. (2018, September 23). _Anatomy of a killing_ . BBC Africa Eye. https://www.
youtube.com/watch?v=4G9S-eoLgX4
Data. (n.d.). In _Dictionary.com_ . Retrieved May 20, 2020, from https://www.dictionary.
com/browse/data
Dwoskin, E. (2019, January 25). YouTube is changing its algorithms to stop recommending conspiracies. _The Washington Post_ . https://www.washingtonpost.com/
technology/2019/01/25/youtube-is-changing-its-algorithms-stop-recommendingconspiracies/
Journalism. (n.d.). In _Dictionary.com_ . Retrieved May 20, 2020, from https://www.
dictionary.com/browse/journalism
Klein, S. (2016, March 16). Infographics in the time of cholera. _ProPublica_ . https://
www.propublica.org/nerds/infographics-in-the-time-of-cholera
Woodman, S. (2019, October 22). Using the power of machines to complete
impossible reporting tasks. ICIJ. https://www.icij.org/blog/2019/10/
using-the-power-of-machines-to-complete-impossible-reporting-tasks/


**About the Author**


**Sarah Cohen** is the Knight Chair in Journalism at the Walter Cronkite School
of Journalism and previously worked as the editor of a data journalism team
at _The New York Times_ .



##### **24. Data Visualizations: Newsroom Trends** **and Everyday Engagements**

_Helen Kennedy, William Allen, Martin Engebretsen,_
_Rosemary Lucy Hill, Andy Kirk and Wibke Weber_


**Abstract**
This chapter looks at the production of data visualizations (dataviz) in
newsrooms and audiences’ everyday engagements with them.


**Keywords:** data visualization, audience engagement, newsrooms, dataviz,
storytelling, data publics


This chapter looks at both the production of data visualizations (henceforth
“dataviz”) in newsrooms and audiences’ everyday engagements with dataviz,
drawing on two separate research projects. The first is Seeing Data, which
explored how people make sense of data visualizations, and the second is
INDVIL, which explored dataviz as a semiotic, aesthetic and discursive
resource in society. [1] The chapter starts by summarizing the main findings
of an INDVIL sub-project focusing on dataviz in the news, in which we
found that dataviz are perceived in diverse ways and deployed for diverse
purposes. It then summarizes our main findings from Seeing Data, [2] where
we also found great diversity, this time in how audiences make sense of
dataviz. This diversity is important for the future work of both dataviz
researchers and practitioners.


1 http://seeingdata.org/, https://indvil.org/
2 The second half of the chapter summarizes a longer article available online: Kennedy, H.,
Hill, R. L., Allen, W., & Kirk, A. (2016). Engaging with (big) data visualizations: Factors that
affect engagement and resulting new definitions of effectiveness. _First Monday_, _21_ (11). https://


Bounegru, L. and J. Gray (eds.), _The Data Journalism Handbook:_ _Towards a Critical Data Practice_ .
Amsterdam: Amsterdam University Press, 2021
doi 10.5117/9789462989511_ch24


**Data Visualization in Newsrooms: Trends and Challenges**


How is data visualization being embedded into newsroom practice? What
trends are emerging, and what challenges are arising? To answer these
questions, in 2016 and 2017 we undertook 60 interviews in 26 newsrooms
across six European countries: Norway (NO), Sweden (SE), Denmark (DK),
Germany (DE), Switzerland (CH) and the United Kingdom (UK). Interviewees
in mainstream, online news media organizations included editorial leaders, leaders of specialist data visualization teams, data journalists, visual
journalists, graphic/data visualization designers and developers (although
some didn’t have job titles, a sign in itself that this is a rapidly emerging
field). We present some highlights from our research here.


**Changing Journalistic Storytelling**


The growing use of data visualization within journalism means that there
is a shift from writing as the main semiotic mode to data and visualization
as central elements in journalistic storytelling. Many interviewees stated
that data visualization is the driving force of a story, even when it is a simple
graphic or diagram.


The reader stats tell us that when we insert a simple data visualization
in a story, readers stay on the page a little longer. (SE)


Dataviz are used with a broad range of communicative intentions, including:
“to offer insight” (UK), “to explain more easily” (SE), “to communicate clearly,
more clearly than words can” (UK), “to tell several facets in detail, which
in text is only possible in an aggregated form” (DE), to make stories “more
accessible” (DK), “to reveal deplorable states of affairs” (CH), “to help people
understand the world” (UK). Data visualization is used to emphasize a point,
to add empirical evidence, to enable users to explore data sets, as aesthetic
attraction to stimulate interest and to offer entry into unseen stories.
These changes are accompanied by the emergence of multiskilled specialist groups within newsrooms, with data and dataviz skills prioritized in new
recruits. But there are no patterns in the organization of dataviz production
within newsrooms—in some, it happens in data teams, in others, in visual
teams (one of our dataviz designer interviewees was also working on a virtual
reality project at the time of the interview) and elsewhere, in different teams
still. And just as new structures are emerging to accommodate this newly


4,,,,


proliferating visual form, so too newsroom staff need to adapt to learn new
tools, in-house and commercial, develop new skills, and understand how
to communicate across teams and areas of expertise in order to produce
effective data stories.


**The “Mobile First” Mantra and Its Consequences**


Widespread recognition that audiences increasingly consume news on small,
mobile screens has led to equally widespread adoption of a “mobile first”
mantra when it comes to producing dataviz in newsrooms. This means a turn
away from the elaborate and interactive visualizations that characterized
the early days of dataviz in the news, to greater simplicity and linearity,
or simple visual forms with low levels of interactivity. This has led to a
predominance of certain chart types, such as bar charts and line charts,
and to the advent of _scrollytelling_, or stories that unfold as users scroll down
the page, with the visualizations that are embedded in the article appearing
at the appropriate time. Scrolling also triggers changes in visualizations
themselves, such as zooming out.


Often in our stories we use the scrolling technique. It is not necessary
to click but to scroll, if you scroll down, something will happen in the
story. (DE)


Tools to automate dataviz production and make it possible for journalists
who are not dataviz experts to produce them also result in the spread of
simplified chart forms. Nonetheless, some interviewees are keen to educate
readers by presenting less common chart types (a scatterplot, for example)
accompanied with information about how to make sense of them. Some
believe that pictures can also present data effectively—a Scandinavian
national tabloid represented the size of a freight plane by filling it with
427,000 pizzas. Others recognize the value of animation, for example, to show
change over time, or of experimenting with zoomability in visualizations.


**The Social Role of Journalism**


Linking a dataviz to a data source, providing access to the raw data and
explaining methodologies are seen by some participants as ethical practices
which create transparency and counterbalance the subjectivity of selection


and interpretation which, for some, is an inevitable aspect of visualizing data.
Yet for others, linking to data sources means giving audiences “all of the data”
and conflicts with the journalistic norm of identifying and then telling a story.
For some, this conflict is addressed by complex processes of sharing different
elements of data and process on different platforms (Twitter, Pinterest, GitHub).
This leads data journalists and visualization designers to reflect on how
much data to share, their roles as fact providers and their social role more
generally. Data journalist Paul Bradshaw sums this up on his blog:


How much responsibility do we have for the stories that people tell with
our information? And how much responsibility do we have for delivering
as much information as someone needs? (Bradshaw, 2017)


Former _Guardian_ editor Alan Rusbridger (2010) raised a similar question
about the social role of journalism when he pointed to the range of actors
who do what journalism has historically done—that is, act as a gatekeeper
of data and official information (e.g., FixMyStreet and TheyWorkForYou in
the United Kingdom). He concluded: “I don’t know if that is journalism or
not. I don’t know if that matters” (Baack, 2018). Some of our interviewees
work on large-scale projects similar to those discussed by Rusbridger—for
example, one project collated all available data relating to schools in the
United Kingdom and made this explorable by postcode to inform decision
making about school preference. So the question of what counts as journalism in the context of widespread data and dataviz is not easy to answer.
What’s more, sharing data sets assumes that audiences will interact with
them, yet studies indicate that online interactivity is as much a myth as a
reality, with the idealized image of an active and motivated explorer of a
visualized data set contrasting with the more common quick and scrolling
reader of news (e.g., Burmester et al., 2010). Similarly, a study of data journalism projects submitted to the Nordic Data Journalism Awards concludes
that interactive elements often offer merely an _illusion_ of interactivity, as
most choices already are made or predefined by the journalists (Appelgren,
2017). This again calls into question the practice of sharing “all of the data”
and raises questions about the changing social role of journalism.


**Trust, Truth and Visualizations “in the Wild”**


Other elements of the process of visualizing data raise issues of trust
and truth and also relate to how journalists think about the social role


,,,,


of journalism. One aspect of dataviz work that points to these issues is
how journalists working with data visualization think about data and
their visual representation. Some see it as a form of truth-telling, others
as a process of selection and interpretation, and others still believe that
shaping data visualizations through choices is a way of revealing a story and
so is precisely what journalists should do. These reflections highlight the
relationship between (dis)trust and presentation, and between perspective
and (un)truthfulness.
In our current, so-called “post-truth” context, in which audiences are
said to have had enough of facts, data and experts and in which “fake news”
circulates quickly and widely, our participants were alert to the potential
ways in which audiences might respond to their data visualizations, which
might include accepting naively, refuting sceptically, decontextualizing
through social sharing, or even changing and falsifying. They felt that
journalists increasingly need “soft knowledge of Internet culture” (UK), as
one participant put it. This includes an understanding of how online content
might be more open to interrogation than its offline equivalent, and of how
data visualizations may be more likely to circulate online than text, floating
free of their original contexts as combinations of numbers and pictures “in
the wild” (Espeland & Sauder, 2007). This in turn requires understanding of
strategies that might address these dangers, such as embedding explanatory
text into a visualization file so that the image cannot be circulated without
the explanation. These issues, alongside concern about audiences’ data
and visualization literacy, inform and reshape journalists’ thinking about
their audiences.


**How Do People Engage With Data Visualizations?**


In this section, we look at dataviz in the news from the perspective of the
audience. How do audiences engage with and make sense of the visualizations that they encounter in news media? Data journalists are often too
busy to attend to this question. Data visualization researchers don’t have
this excuse, but nevertheless rarely focus their attention on what end users
think of the visualizations that they see.
Enter Seeing Data, a research project which explored how people engage
with the data visualizations that they encounter in their everyday lives,
often in the media. It explored the factors that affect engagement and what
this means for how we think about what makes a visualization effective. On
Seeing Data we used focus groups and interviews to explore these questions,


to enable us to get at the attitudes, feelings and beliefs that underlie people’s
engagements with dataviz. Forty-six people participated in the research,
including a mix of participants who might be assumed to be interested
in data, the visual or migration (which was the subject of a number of the
visualizations that we showed them) and so “already engaged” in one of the
issues at the heart of our project, and participants about whom we could
not make these assumptions.
In the focus groups, we asked participants to evaluate eight visualizations,
which we chose (after much discussion) because they represented a diversity
of subject matters, chart types, original media sources and formats, and
aimed either to explain or to invite exploration. Half of the visualizations
were taken from journalism (BBC; _The New York Times_ ; _The Metro_, a freely
distributed UK newspaper; and _Scientific American_ magazine). Others came
from organizations which visualize and share data as part of their work:
The Migration Observatory at the University of Oxford; the UK Office for
National Statistics (ONS); and the Organisation for Economic Co-operation
and Development (OECD).
After the focus groups, seven participants kept diaries for a month, to
provide us with further information about encounters with visualizations
“in the wild” and not chosen by us.


**Factors Which Affect Dataviz Engagement**


**Subject matter.** Visualizations don’t exist in isolation from the subject matter
that they represent. When subject matter spoke to participants’ interest, they
were engaged—for example, civil society professionals who were interested
in issues relating to migration and therefore in migration visualizations. In
contrast, one participant (who was male, 38, White, British, an agricultural
worker) was not interested in any of the visualizations we showed him in the
focus group or confident to spend time looking. However, his lack of interest
and confidence and his mistrust of the media (he said he felt they try “to
confuse you”) did not stop him from looking at visualizations completely:
He told us that when he came across visualizations in _The Farmer’s Guide_,
a publication he read regularly because it speaks to his interests, he would
take the time to look at them.
**Source or media location.** The source of visualizations is important: It
has implications for whether users trust them. Concerns about the media
setting out to confuse were shared by many participants and led some to
view visualizations encountered within certain media as suspect. In contrast,


,,,,


Figure 24.1. Non-UK born census populations 1951–2011.
Source: Office for National Statistics.


Figure 24.2: Migration in the census. Source: The Migration Observatory, University of Oxford.
http://www.compas.ox.ac.uk/migrationinthecensus/, http://migrationobservatory.ox.ac.uk/


some participants trusted migration visualizations which carried the logo of
the University of Oxford, because they felt that the “brand” of this university
invokes quality and authority. But during the diary-keeping period, a different
picture emerged. Participants tended to see visualizations in their favoured
media, which they trusted, so they were likely to trust the visualizations
they saw there, too. One participant (male, 24, White, British, agricultural
worker), who reads _The Daily Mail_, demonstrated this when he remarked in
his interview that “you see more things wrong or printed wrong in _The Sun_, I
think.” Given the ideological similarities between these two publications, this
comment points to the importance of media location in dataviz engagement.
**Beliefs and opinions.** Participants trusted the newspapers they regularly
read and therefore trusted the visualizations in these newspapers, because
both the newspapers and the visualizations often fitted with their views of
the world. This points to the importance of beliefs and opinions in influencing how and whether people take time to engage with particular visualizations. Some participants said they liked visualizations that confirmed their
beliefs and opinions. But it is not just when visualizations confirm existing
beliefs that beliefs matter. One participant (male, 34, White, British, IT
worker) was surprised by the migration data in an ONS visualization in
Figure 24.1. He said that he had not realized how many people in the United
Kingdom were born in Ireland. This data questioned what he believed and
he enjoyed that experience. Some people like, or are interested in, data in


7,,,,


visualizations that call into question existing beliefs, because they provoke
and challenge horizons. So beliefs and opinions matter in this way, too.
**Time.** Engaging with visualizations is seen as work by people for whom
doing so does not come easily. Having time available is crucial in determining
whether people are willing to do this “work.” Most participants who said
they lacked time to look at visualizations were women, and they put their
lack of time down to work, family and home commitments. One working
mother talked about how her combined paid and domestic labour were so
tiring that when she finished her day, she didn’t want to look at news, and
that included looking at visualizations. Such activities felt like “work” to
her, and she was too tired to undertake them at the end of her busy day.
An agricultural worker told us in an email that his working hours were
very long and this impacted on his ability to keep his month-long diary of
engagement with visualizations after the focus group research.
**Confidence and skills.** Audiences need to feel that they have the necessary skills to decode visualizations, and many participants indicated a
lack of confidence in this regard. A part-time careers advisor said of one
visualization: “It was all these circles and colours and I thought, that looks
like a bit of hard work; don’t know if I understand.” Many of our participants
expressed concern about their lack of skills, or they demonstrated that they
did not have the required skills, whether these were visual literacy skills,
language skills, mathematical and statistical skills (like knowing how to
read particular chart types), or critical thinking skills.
**Emotions.** Although last in our list, a major finding from our research
was the important role that emotions play in people’s engagements with
data visualizations. [3] A broad range of emotions emerged in relation to
engagements with dataviz, including pleasure, anger, sadness, guilt,
shame, relief, worry, love, empathy, excitement, offence. Participants
reported emotional responses to visualizations in general; represented
data; visual style; the subject matter of data visualizations; the source or
original location of visualizations; their own skill levels for making sense
of visualizations.
For example, two civil society professionals used strong language to
describe their feelings when they looked at the visualizations of migration in
the United Kingdom shown in Figure 24.2. The data caused them to reflect
on how it must feel to be a migrant who comes to the United Kingdom and


3 For more on the role of emotions in engagements with data visualization, see Kennedy, H.,
& Hill, R. L. (2018). The feeling of numbers: Emotions in everyday engagements with data and
their visualisation. _Sociology_, _52_ (4), 830–848. https://doi.org/10.1177/0038038516674675


encounters the anti-immigration headlines of the media. They described
themselves as feeling “guilty” and “ashamed” to be British.
Other participants had strong emotional responses to the visual style of
some visualizations. A visualization of film box office receipts by _The New_
_York Times_ divided participants, with some drawn to its aesthetic and some
put off by it (Bloch et al., 2008):


It was a pleasure to look at this visual presentation because of the coordination between the image and the message it carries.
Frustrated. It was an ugly representation to start with, difficult to see
clearly, no information, just a mess.


**What This Means for Making Effective Visualizations**


A broad range of understandings of what makes a visualization effective
emerged from our research. Visualizations in the media that are targeted at
non-specialists might aim to persuade, for example. They all need to attract
in order to draw people in, if they are to commit time to finding out about
the data on which the visualization is based. Visualizations might stimulate
particular emotions, which inspire people to look longer, deeper or further.
They might provoke interest, or the opposite. An effective visualization
could: Provoke questions/desire to engage in discussions with others; create
empathy for other humans in the data; generate enough curiosity to draw
the user in; reinforce or back up existing knowledge; provoke surprise;
persuade or change minds; present something new; lead to new confidence
in making sense of dataviz; present data useful for one’s own purposes;
enable an informed or critical engagement with a topic; be a pleasurable
experience; provoke a strong emotional response.
What makes a visualization effective is fluid—no single definition applies across all dataviz. For example, being entertained by a visualization
is relevant in some contexts, but not others. Visualizations have various
objectives: to communicate new data; to inform a general audience; to
influence decision making; to enable exploration and analysis of data; to
surprise and affect behaviour. The factors that affect engagement which
we identified in our research should be seen as _dimensions_ of effectiveness, which carry different weight in relation to different visualizations,
contexts and purposes. Many of these factors lie outside of the control of
data visualizers, as they relate to consuming, not producing, visualizations.
In other words, whether a visualization is effective depends in large part on


7,,,,


how, by whom, when and where it is accessed. Sadly, our research doesn’t
suggest a simple checklist which guarantees the production of universally
effective visualizations. However, if we want accessible and effective data
visualizations, it’s important that journalists working with data visualization
engage with these findings.


**Works Cited**


Appelgren, E. (2017). An illusion of interactivity: The paternalistic side of data
journalism. _Journalism Practice_, _12_ (3). https://doi.org/10.1080/17512786.2017.12
99032
Baack, S. (2018). _Knowing what counts: How journalists and civic technologists use_
_and imagine data_ [Doctoral dissertation], University of Groningen. https://www.
rug.nl/research/portal/files/56718534/Complete_thesis.pdf
Bloch, M., Byron, L., Carter, S., & Cox, A. (2008, February 23). Ebb and flow of movies:
Box office receipts 1986–2008. _The New York Times_ . http://archive.nytimes.
com/www.nytimes.com/interactive/2008/02/23/movies/20080223_REVENUE
_GRAPHIC.html?_r=1
Bradshaw, P. (2017, September 14). No, I’m not abandoning the term “storytelling,”
Alberto—Just the opposite (and here’s why). _Online Journalism Blog_ . https://
onlinejournalismblog.com/2017/09/14/narrative-storytelling-data-journalismalberto-cairo/
Burmester, M., Mast, M., Tille, R., & Weber, W. (2010). How users perceive and use
interactive information graphics: An exploratory study. In E. Banissi (Ed.),
_Proceedings of the 14th International Conference Information Visualisation_
(pp. 361–368). https://doi.org/10.1109/IV.2010.57
Espeland, W. N., & Sauder, M. (2007). Rankings and reactivity: How public measures
recreate social worlds. _American Journal of Sociology_, _113_ (1), 1–40. https://doi.
org/10.1086/517897
Rusbridger, A. (2010, July). _Why journalism matters_ . Media Standards Trust Series,
British Academy.


**About the Authors**


**Helen Kennedy’s** research has traversed digital media landscapes; her
current focus is on lived and visualized experiences of datafication and
related phenomena (algorithms, AI, machine learning), inequalities, and
everyday perspectives on “fair” data practices.


**William Allen** is a researcher based at Oxford’s Centre on Migration, Policy,
and Society (COMPAS), where his research examines the intersections of
political communication and public attitudes using the lenses of migration
and mobility.


**Martin Engebretsen** is Professor of Language and Communication at the
University of Agder, with special expertise in the fields of multimodal
discourse analysis and journalism studies.


**Rosemary Lucy Hill** researches gender, popular music and the politics of
data visualizations and is author of _Gender, Metal and the Media: Women_
_Fans and the Gendered Experience of Music_ (Palgrave, 2016).


**Andy Kirk** is a data visualization specialist.


**Wibke Weber** is Professor of Media Linguistics at ZHAW (Zurich University
of Applied Sciences) studying data visualization, information graphics,
visual semiotics, comics journalism, VR and multimodality.


##### **25. Sketching With Data**

_Mona Chalabi and Jonathan Gray_


**Abstract**
An interview with celebrated data journalist Mona Chalabi exploring the
development and reception of her practice of sketching as a way of making
data relatable, including discussion of data as a means of providing context,
visual practices of making things comparable, the role of humour and analogy in her work, data journalism as social commentary, and the importance
of communicating the uncertainty of data and the provisionality of analysis.


**Keywords:** data sketching, data visualization, uncertainty, data publics,
data journalism, visual practices


**Jonathan Gray (JG): How did you start sketching with data?**
Mona Chalabi (MC): When I was working at _FiveThirtyEight_ I felt that they
weren’t catering to readers like me. They were catering to a slightly different
kind of reader with their complex interactives. During this time I began
sketching with data, which I could do while sitting at my desk. As I started
to do them I had this realization that they could be quite an effective way to
communicate the uncertainty of data projects. They could remind people
that a human was responsible for making all of these design decisions. They
could be quite democratizing, communicating with data in a way that anyone
can do. I used to write this DIY column at _The Guardian_ which took people
through every single step of my process. It was fun that as a journalist you
could talk people through not only where you found your data, exactly how you
processed it and what you did to it, but you could also enable them to replicate
it, breaking down the wall between them and you, and hopefully creating
new kinds of accessibility, participation and relationships with readers.


**JG: In the book we explore how data journalists do not just have to mir-**
**ror and reinforce established forms of expertise (e.g., data science and**


Bounegru, L. and J. Gray (eds.), _The Data Journalism Handbook:_ _Towards a Critical Data Practice_ .
Amsterdam: Amsterdam University Press, 2021
doi 10.5117/9789462989511_ch25


Figure 25.1. Mona Chalabi illustration “Average Sentences”. Source: _The Guardian_ . https://www.theguardian.com/news/datablog/2019/jan/12/intimate-partner-violence-gender-gap-cyntoia-brown


**advanced statistical methods), but how they can also promote other**
**kinds of data practices and data cultures. Do you consider your work to**
**be partly about finding other ways of working with and relating to data?**
MC: I don’t have really advanced statistical skills. The way that I often start
analyzing data is through relatively simple calculations that other people can
replicate. In a way this makes the data that I’m using much more reliable.
At a certain point with other more advanced statistical approaches you
present readers with an ultimatum: Either you trust the journalist’s analysis
or you don’t. This is different to the proposition of trusting government
statistics and basic multiplication or not trusting them. There is a certain
benefit to doing things with simple calculations. This is a big part of what
I do and my approach.
Data can be used as an opportunity to do two different things: To “zoom
in” or “zoom out.” On the one hand, my responsibility as a data journalist is
to zoom out from that one specific incident and give readers context using


Figure 25.2. Mona Chalabi illustration “There are approximately 40 Burmese roofed turtles left in
the world”. Souce: _The Guardian_ . https://www.theguardian.com/environment/gallery/2018/sep/17/
endangered-species-on-a-train


data. For example, say there is an incident or an attack, we might show them
how these attacks happen, where they happen, whether their prevalence
increases over time and whether there are people who are more targeted
than others. That is an opportunity for readers to understand broader trends,
which can be really informative for them. Maybe it helps them to not freak
out, or to duly freak out in response to the news.
On the other hand, we can do the complete opposite and zoom in. Let’s
say that the BLS [US Bureau of Labor Statistics] publishes unemployment
data and that most other news outlets just publish the unemployment rate.
We as data journalists are able to zoom in: We can say to readers, here is
the national employment rate but also this is what it looks like for women,
this is what it looks like for men, this is what it looks like for different age
groups, here is what it looks like for different racial and ethnic groups. So
it allows readers to explore the data more closely.
My work alternates between these two modes. I think one of my biggest
critiques of outlets like _FiveThirtyEight_ is that the work can sometimes be
about intellectual bravado: “Here’s what we can do.” I’m not into that. My
purpose is to serve readers and in particular the broadest community of


readers, not just White men who identify as geeks. _FiveThirtyEight_ readers
call themselves geeks and _FiveThirtyEight_ journalists call themselves that.
But that is not why I got into journalism.


**JG: To take one recent example of your work, could you tell us a bit more**
**about the “Endangered Species on a Train” piece published in** _**The Guardian**_
**(Figure 25.2)?** **How did you get into this topic, how did the project arise**
**and how did you approach it?**
MC: It was actually quite strange. It was not really inspired by the news;
it was more about my personal practice of doing these illustrations and
wanting to do something a bit more ambitious. Part of the reason why
I started doing these illustrations is they are also really efficient: They
can have such a fast turnaround, and can be made in a matter of hours if
need be. I wanted to create something bigger that would take a bit more
time. I started with a much bigger topic that people already feel familiar
with—endangered species—but for which the existing visual language
is perhaps a bit uninspiring. I took data from the International Union for
Conservation of Nature (IUCN) “Red List.” [1] For a lot of those numbers on
endangered species they gave a range, and I chose a midpoint for each of
them.
Stepping back, you could look at my illustrations as charts. The only thing
that makes them charts is scale. Every illustration that I post has a sense
of scale and that is what every single chart does. One of the problems with
scale is that different countries and places use different scales, for example,
millimetres in the United Kingdom and inches in the United States. Scales
mean different things to different people. A lot of data journalists lose
sight of this. What does “1 million” mean to someone? What does “1” mean
to someone? All of this depends on context. When numbers are low it can
be easier to get your head around this: You know what 27 means. But what
does that mean?
Part of the beauty of data visualization is that it can make things feel more
visceral. Another illustration that I was pretty proud of and that did really
well was one where I compared the average parking space to the average
solitary confinement cell (Figure 25.3). This is like a common practice for
dealing with numbers in journalism: You don’t say “bankers in London
earn this much,” you say “bankers in London earn 7,000 times what a social
worker earns.” All of those analogies really help people.


1 https://www.iucnredlist.org/


Figure 25.3. “Space in America” illustration. Source: Mona Chalabi. https://www.instagram.com/p/
BEi-v3tKvBZ/


**JG: It seems that part of your practice is also to do with juxtaposition of**
**different elements (e.g., the familiar and the disturbing). Is there also a**
**curatorial element here?**
MC: Humour also plays an important role in my work. Not that the pieces
are funny, but there is often something wry in the style. The best comedy
is basically saying “this is fucked up.” There is always some kind of social
commentary. If you can inject data journalism with a little bit of that it can
be really powerful.


**JG: Returning to the “Endangered Species” example as a case of making**
**numbers relatable through humour and the use of different visual spaces**
**of comparison, did you start with the carriage (as opposed to the chart)?**
MC: First I drew the carriage, and then I drew about seven or eight of
each animal. I used Photoshop to separate out the layers, to colour them


and to count them. To make sure I got it correct each animal is a different
layer. My first idea was to draw endangered species in different things
which are all universally relatable. The New York Subway is not perfect
(is it bigger or smaller than the London Tube?), but it is enough to give
you a sense of scale. I started with a spreadsheet of different possibilities
combining endangered species and relatable spaces. I was thinking of
showing a shark in a swimming pool. But with all of the different spaces it
felt a bit difficult to get your head around and once I started drawing them
I realized it was going to be a really lengthy process. Rather than drawing
them all in different places I would show them all in the same one, which
also works better.
It is not really perfect: To fit all of the rhinos in the scale is a little bit
questionable I would say (a lot of them would need to be babies rather
than adults!). But it makes you feel something about the numbers. And it
is also transparent about its shortcomings. When you look at a chart that
_FiveThirtyEight_ created, how are you, especially as a non-expert, supposed
to remotely understand to what extent it is accurate? Readers are just given
an ultimatum: Trust us or don’t. When readers look at the illustrations of
the endangered species they can look at the rhinos and think, “It is a little
bit off but I get it.” They have access to that critique in a way that they don’t
with computer generated graphics.


**JG: Earlier you mentioned that you hoped your work could democratize**
**how people engage with data. Could you say a bit more about this?**
MC: Without this ability for readers to participate in making sense with
data and forming their own judgements, how are journalists any better than
politicians? You have right-wing papers and left-wing papers just saying:
“You either trust us or you don’t.” But we’re supposed to be empowering
people to make informed decisions in their everyday lives. Empowering
people is not just about saying, “These are the facts, now clearly you’re
supposed to go and do this.” It is saying, “These are the facts; here is how
we got here.” It is not just journalism: I think there is a lot of work to be
done in medicine as well. I’d like to do more work around how to change
medical packaging. Rather than boxes saying, “Here’s what you need to
do,” if you’re going to be a really good doctor you should be able to say to
the patient, “These are the risks for this medicine. These are the risks of
not taking it. These are the risks of this other course of medicine. These
are the risks of not taking it,” so people can make decisions for themselves
as no two people are alike.


I think good data visualizations should communicate uncertainty. [2]
Uncertainty is part of that whole story of making an informed decision in
your life. So few data journalists take the time to communicate uncertainty.
So few data journalists take the time to reach out to communities that aren’t
geeks. Just because you don’t have these particular vocabularies of statistical
or computational skills does that mean that you are not smart, that you are
not entitled to understand this information? Of course not. And yet some
data journalists refer to so many of these terms in this off-hand way, like,
“I’m not going to bother explaining this every time. You either get it or you
don’t.” It is stupid. My approach to data journalism is based on the idea that
you don’t necessarily need specific vocabularies or expertise to be smart.


**JG: Is there also an element of people participating in deciding what**
**matters?**
MC: Part of the reason I started the “Dear Mona” advice column was so
that people could send me questions. People are constantly sending DMs on
Instagram about things which matter to them, and there are many things
that I wouldn’t necessarily have thought of at all. There are some routes that
I don’t want to go down, like looking at the relation between mental health
and gun control, which can stigmatize people with mental health issues and
open a whole can of worms. But if I get many DMs from people who want to
know about this then you wonder whether you should not just sidestep the
nuance because it is complicated but should instead try to tackle it head
on. So I’m constantly looking to readers to tell me what matters to them.
I don’t think that this is an abdication of journalistic responsibility. It is
part of the democratic role of journalism and people seeing that they have
a stake in the final product in every single way: In the process of creating
it, in understanding it, and it is not this thing which is just given to them
in a “take it or leave it” kind of way.


**JG: Could you tell us a bit about the responses to your work? Have there**
**been any unexpected or notable responses?**
MC: I get all kinds of different responses to my work. Some people focus on
the subject matter. So any time I do something on wage gaps, for example, I
get lots of White men that are, like, “No, Black women only earn less because
they work less,” and you have to engage with them about how the illustrations
are based on “like for like” comparisons between full-time workers, and if


2 Editors: See also Anderson’s chapter in this book, as well as his _Apostles of Certainty: Data_
_Journalism and the Politics of Doubt_ (Oxford University Press, 2018) _._


there are differences in the levels they are at (e.g., senior management), that
is also part of the problem. I’m always keen to focus on the critique first.
But overall I get much more support than criticism. Sometimes people
respond to critiques in comments even before I get to them. People whose
lives are represented in the illustrations sometimes intervene to say, “No,
my personal experience bears this out.” People sometimes want to see
extra data. Lots of students write to say that they really want to do this
(interestingly I get more female students writing to me than men). A lot of
NGOs and charities write to me as they want to feel something about their
data rather than thinking something about their data, and sometimes my
work manages to do that. One of my pieces was cited in a US bill.
My work has been viewed and shared by a lot of people on social media
who are not necessarily into data journalism per se, which is getting it in
front of a new audience. Bernie Sanders shared my gun violence illustration,
Miley Cyrus shared one, as did Iman, the model, and Shaun King, the civil
rights activist. These are not people I know and not necessarily people who
follow my work, but they see other people sharing it and it somehow ends up
on their radar. It is amazing to see people engaging with it. Once someone
prominent shares it, it can take on a life of its own sometimes.
Examples of the works referred to in this chapter can be found on the
web at monachalabi.com and on Instagram at @monachalabi.


**About the Authors**


**Mona Chalabi** is trying to take the “numb” out of numbers and is left with
lots of “ers.”


**Jonathan Gray** is Lecturer in Critical Infrastructure Studies at the Department of Digital Humanities, King’s College London, co-founder of the Public
Data Lab and Research Associate at the Digital Methods Initiative, University
of Amsterdam.



##### **26. The Web as Medium for Data** **Visualization**

_Elliot Bentley_


**Abstract**
Exploring the types of graphics made possible by the web, including
interactive dataviz, games and virtual reality (VR).


**Keywords:** interactive graphics, data visualization, web development,
JavaScript, infographics, newsgames


Not all media are created equal. A 20-episode television series is able to tell
a story differently than a two-hour film, for example. In the same way, the
humble web page can provide its own possibilities for data visualization.
The web was originally designed for simple, hyperlinked documents
consisting of mostly text and static images. The addition of JavaScript and
a slow drip of new features and tools has expanded the palette available
to work with. [1]

Although traditional data visualization theory and techniques (e.g.,
Edward Tufte, Jacques Bertin) are still mostly applicable to graphics on the
web, the unique features of the web provide vast potential for new forms
of data journalism. These works are often referred to as “interactives,” an
awkward word that obscures some of the web’s unique strengths.
Below is a list illustrating some of the ways in which graphics on the web
can take advantage of their host medium.


1 Other “multimedia” platforms, especially Flash, provided a wealth of options long before
the open web did. However, for better or worse these have since been phased out. And while
all of these features—more in fact—are available in native applications, the web is far easier
to work with and distribution is practically free.


Bounegru, L. and J. Gray (eds.), _The Data Journalism Handbook:_ _Towards a Critical Data Practice_ .
Amsterdam: Amsterdam University Press, 2021
doi 10.5117/9789462989511_ch26


**Huge, Explorable Data Sets**


A classic use of interactivity is to present the reader with a huge data set and
allow them to “dive in” and explore in as much depth as they like. Sometimes
this takes the shape of a giant table; other times, a big interactive map.
This format is often looked down upon nowadays, since it expects the
reader to find the interesting bits themselves; but it can still be valuable
if the data is juicy enough. I find that the most successful versions accept
the fact they are simply tools (as opposed to being articles), such as the
extremely popular _Wall Street Journal_ College Rankings or _ProPublica_ ’s
public-service news apps. [2]


**Guide the Reader Through Complex Charts**


A now-common format begins with a single chart and then proceeds to
manipulate it—zooming in and out, travelling through time, switching out
data—in order to fully explore the data set. This pairs exceptionally well
with scrollytelling and is especially valuable on mobile, where there may
not be enough space to show all elements of a chart at once. [3]

In the now-classic piece “A Visual Introduction to Machine Learning”
(Figure 26.1), the same data points transition between multiple chart formats, helping readers keep track of how the machine learning algorithms
are sorting them. [4] Another good example is “100 years of tax brackets, in
one chart,” a _Vox_ piece that zooms in and out of a data set that might be
overwhelming if presented otherwise. [5]


**Up-to-the-Second Live Data**


Why settle for a static data set when you can use the latest numbers of
whatever you’re charting? Elections, sport coverage, weather events and
financial data are obvious sources of live data interesting enough to display
in real time. Even more cool is providing context for these live figures in


2 https://www.wsj.com/articles/explore-the-full-wsj-the-college-rankings-11567638555,
https://www.propublica.org/newsapps/
3 https://pudding.cool/process/how-to-implement-scrollytelling/
4 http://www.r2d3.us/visual-intro-to-machine-learning-part-1/
5 https://www.vox.com/2015/10/26/9469793/tax-brackets


Figure 26.1. A visual introduction to machine learning. Source: R2D3. http://www.r2d3.us/
visual-intro-to-machine-learning-part-1/


interesting ways—for example, showing which countries benefit from the
current price of oil (Figure 26.2).
Ampp3d, a short-lived experimental pop-data journalism outlet, used live
counters to bring numbers to life in interesting ways, such as the number of
immigrants entering the United Kingdom, and footballer Wayne Rooney’s
earnings. [6] Sadly, these have since been taken offline.


**Placing the Reader Within a Data Set**


Another twist on the “huge data sets” idea—and one that I’ve found to be
incredibly compelling to readers—is to show the reader where they fall in
a data set, usually by asking for a couple of personal details. _The New York_


6 https://onlinejournalismblog.com/2015/05/13/the-legacy-of-ampp3d-usvsth3m-and-row-zed/


Figure 26.2. Countries that benefit from the current price of oil. Source: _Wall Street Journal_ . http://
graphics.wsj.com/oil-producers-break-even-prices/


_Times_ ’ 2013 dialect quiz map (Figure 26.3) famously became the publication’s most popular article of the year—despite only being published on
December 20th.
The BBC seem to do these pretty frequently, often as a public service tool,
with things like “UK fat scale calculator.” [7] I like this _Quartz_ piece on how people
in different cultures draw circles, which opens by asking the reader to draw a
circle, a compelling introduction to an otherwise (potentially) dull feature. [8]


**Collecting Original Data Sets**


A step beyond the previous category are projects that not only use readers’
submitted data to give an immediate response, but also to compile a new
data set for further analysis.
The Australian Broadcasting Corporation collaborated with political
scientists on a “Vote Compass” to help readers understand their place


7 https://www.bbc.com/news/health-43697948
8 https://qz.com/994486/the-way-you-draw-circles-says-a-lot-about-you/


Figure 26.3: _The New York Times_ ’ 2013 dialect quiz map. Source: _The New York Times_ . https://www.
nytimes.com/interactive/2014/upshot/dialect-quiz-map.html


in the political landscape—and then wrote a series of articles based on
the data. [9]

More recently, _The New York Times_ used the same idea on a softer subject,
asking readers to rate _Game of Thrones_ characters and plotting the results
on live charts (Figure 26.4).


**The Infinite Canvas**


The web is infinite in its scope and capacity, but more specifically web
pages can be as wide or tall as they like—an “infinite canvas” on which
to work. I borrowed this term from artist Scott McCloud, who argues that


9 https://www.abc.net.au/news/nsw-election-2015/vote-compass/, https://www.abc.net.au/
news/nsw-election-2015/vote-compass/results/


Figure 26.4: A plot chart rating _Game of Thrones_ characters. Source: _The Upshot_ . https://www.
nytimes.com/interactive/2017/08/09/upshot/game-of-thrones-chart.html


there is “no reason that longform comics have to be split into pages when
moving online.” [10] And indeed, why should our graphics be constrained to
the limits of paper either?
In _The Washington Post_ ’s “The Depth of the Problem,” a 16K-pixel-tall
graphic is used to show the depth of the ocean area being searched for
missing flight MH370 (Figure 26.5). [11] Sure, this information could have been
squeezed into a single screen, but it would have lacked the level of detail
and emotional impact of this extremely tall graphic.
In _The Guardian_ ’s “How the List Tallies Europe’s Migrant Bodycount,”
tens of thousands of migrant deaths are powerfully rendered as individual
dots that appear one by one as the reader scrolls down the page. [12]


10 http://scottmccloud.com/4-inventions/canvas/index.html
11 https://www.washingtonpost.com/apps/g/page/world/the-depth-of-the-problem/931/
12 https://www.theguardian.com/world/2018/jun/20/the-list-europe-migrant-bodycount


Figure 26.5. Graphic that shows the depth
of the ocean area being searched for the missing
flight MH370. Source: _The Washington Post_ .
http://apps.washingtonpost.com/g/page/
world/the-depth-of-the-problem/931/


**Data-Driven Games**


“Newsgames,” interactive experiences that borrow mechanics from video games
to explore news subjects, have existed for a while, with varying levels of success.
The Upshot’s “You Draw It” series (Figure 26.6) challenges readers’ assumptions by asking them to fill in a blank chart, before revealing the
answer and exploring the subject in greater depth.
Some games are more involved, perhaps asking the reader to solve a
simplified version of a real-world problem—such as how to fund the BBC—to
prove just how difficult it is. [13]


13 https://ig.ft.com/sites/2015/bbc/


Figure 26.6. A chart from _The Upshot’s_ “You Draw It” series.
Source: _The Upshot_ . https://www.nytimes.com/interactive/2015/05/28/upshot/you-draw-it-howfamily-income-affects-childrens-college-chances.html


These could be considered toys that only present the reader with surfacelevel information, but done right they can provide a fresh perspective on
played-out subjects. _FiveThirtyEight_ ’s “How to Win a Trade War,” in which
the reader chooses a trading strategy and competes against a previous
visitor to the page, brings to life the otherwise potentially dry economic
theory. [14]


**Live, Randomized Experiments**


A related format is to allow the reader to run a live simulation in their
browser. More than just an animated explainer, this introduces a degree
of randomness that leads to a unique result each time and is a great way to
bring abstract statistical probabilities to life.
The _Guardian_ piece in Figure 26.7 simulates a measles outbreak across
ten populations with varying rates of vaccination. The web graphics make
the results starkly clear in a way that percentages alone could not convey.
In Nathan Yau’s “Years You Have Left to Live, Probably,” a simple line chart


14 https://fivethirtyeight.com/features/how-to-win-a-trade-war/


Figure 26.7: A simulation of a measles outbreak across ten populations with varying rates of
vaccination. Source: _The Guardian_, https://www.theguardian.com/society/ng-interactive/2015/
feb/05/-sp-watch-how-measles-outbreak-spreads-when-kids-get-vaccinated


(“probability of living to next year”) is made more poignant with “lives” that
die at random and then pile up. [15]

These simulations don’t have to use imaginary data. “The Birthday
Paradox” tests the probability of shared birthdays using data from previous
visitors to the page. [16]


**3D, VR and AR**


3D graphics and virtual reality are difficult to harness in service of data
journalism, outside of maps of terrain.
Two notable experiments, both from 2015 and on the subject of financial
data (“Is the Nasdaq in Another Bubble?” and “A 3-D View of a Chart That
Predicts the Economic Future: The Yield Curve”), are clever novelties but
failed to spark an explosion of three-dimension charts. [17] Perhaps for the best.


15 https://flowingdata.com/2015/09/23/years-you-have-left-to-live-probably/
16 https://pudding.cool/2018/04/birthday-paradox/
17 http://graphics.wsj.com/3d-nasdaq/, https://www.nytimes.com/interactive/2015/03/19/
upshot/3d-yield-curve-economic-growth.html


The potential of augmented reality, in which a camera feed of the real
world is overlaid with graphics, has yet to be proven.


**Conclusion: How New Formats Arise**


Some of the web graphics listed above are new formats that have only
emerged over the past few years; some have stuck around, such as the
guide through a complex chart (typically using a scrollytelling interaction
pattern). Others, like three-dimensional charts, were mere flashes in the
pan.
Yet it’s not just taste that determines which types of graphics are in
vogue on the web: Available technology and readers’ consumption habits
shape trends, too.
Take, for example, the widely used interactive map. In addition to
being a visually attractive and easily grasped form, the proliferation and
familiarity of this format was doubtless helped by tools that make them
easy to create and manipulate—Google Maps and Leaflet being two of
the most common.
Without any hard data to hand, it at least feels as though fewer interactive
maps are being published nowadays. While it would be easy to attribute
this trend to a growing realization among journalists that such interactivity
(or even the map itself) can often be superfluous, new technologies likely
also contributed to this drop.
A high proportion of readers now access the web using mobile phones, and
interactive maps are a particularly poor experience on small touchscreens.
In addition, there is a new technological solution that in many ways is
superior: ai2html, a script open-sourced by _The New York Times_ that generates
a responsive html snippet from Adobe Illustrator files. [18] Maps built with
ai2html can leverage a traditional cartographer’s skill set and still have
sharp, machine-readable text. The lack of interactivity in such maps is often
a blessing, even if it is in many ways limiting.
This is just one example of how data journalists should be thoughtful in
their use of the web’s unique features. With so many possibilities to hand,
it’s important to carefully evaluate those and use them only when truly
necessary.


18 https://github.com/newsdev/ai2html


**About the Author**


**Elliot Bentley** has worked in _The Wall Street Journal_ ’s graphics department since 2014 and is also the creator of open-source transcription app
oTranscribe.


##### **27. Four Recent Developments in News** **Graphics**

_Gregor Aisch and Lisa Charlotte Rost_


**Abstract**
This chapter explores four developments we have recently seen in news
graphics: “Mobile first” becomes more important, the importance of
interactivity shifts, more (in-house) charting tools get developed, and
data-centric online publications are on the rise.


**Keywords:** news graphics, mobile, charting tools, interactivity, data
visualization, data journalism


The news graphics field is still young and tries to answer questions like: How
do we show the bias and uncertainty in (polls) data? (Cairo & Schlossberg,
2019). How do we work together with reporters? How do we communicate
complex data on fast-paced social media? (Segger, 2018). Here, we try to
cover four key developments that we think are relevant for the coming years.


**“Mobile First” Starts to Be Taken Seriously**


“Mobile first” is a widely used buzzword, but in the fast-paced world of news
graphics, mobile experiences have often remained an afterthought. Now
we finally see them climb up the priority list. That has two consequences.
First, there is more thought being put in making graphics work on mobile.
A note telling mobile users that “this experience works best on a desktop”
becomes a faux pas. A chart needs to be responsive, to not make more than
half of the users leave. But thinking inside the few pixels of a mobile box can
be frustrating for graphics reporters, many of whom are used to the “luxury”
of filling entire pages in print newspapers and designing full-screen desktop


Bounegru, L. and J. Gray (eds.), _The Data Journalism Handbook:_ _Towards a Critical Data Practice_ .
Amsterdam: Amsterdam University Press, 2021
doi 10.5117/9789462989511_ch27


experiences. In the best case, the limits of the small screen motivate graphics
reporters to think outside of the box and become creative. We already see
this happening: For example, the _Financial Times_ turned their parliament
seat chart 90 degrees, essentially creating a new chart type. [1]

The second consequence of mobile-first data visualization is that news
developers and reporters will see “mobile” not just as a tiny screen anymore,
but also as a device that is packed with sensors. This can lead to new data
experiences. _The Guardian_ created an app with which you can take a virtual
audio tour of Rio de Janeiro, covering the same length as the marathon that
took place there in 2016. [2] “Our challenge for you: Complete all 26.2 miles—or
42.2 km—of the route over the next three weeks,” they write. AR and VR make
similar use of our smartphones, and we see them arriving in news as well.


**Interactivity Is Dead, Except When It’s Not**


We’ve seen interactivity being used less and less for simple charts in the past few
years. It’s now reserved for the biggest projects a newsroom will publish each
year. But interactivity is not necessary for success anymore. Newsrooms like
the _Financial Times_, _FiveThirtyEight_ and _National Geographic_ have repeatedly
published charts that went viral without letting users interact with them.
We see two main reasons for a decline in interactive graphics. First, fewer
people interact with charts than previously assumed. [3] Curious, Internet-savvy
people—like graphics reporters—will always try to hover over a visualization. And reporters want their articles to feel more alive. But we’re creating
for an audience that prefers passive consumption; especially on mobile. Most
people will miss content if it’s hidden behind interactivity, which led many
graphic reporters to decide not to hide anything in the first place.
Second, graphics arrived in the breaking news cycle. Graphics reporters
have gotten faster and faster at creating visualizations, and a breaking
news story will quickly have, for instance, a locator map of where an event
happened. However, well-made interactivity still takes time. Often, it is left
out for the sake of publishing the article faster.
We still see interactive news graphics, but their importance has shifted.
Instead of adding to a story, interactivity becomes the story. We’ve seen great


1 https://ig.ft.com/italy-poll-tracker/
2 https://www.theguardian.com/sport/2016/aug/06/rio-running-app-marathon-course-riorun
3 https://vimeo.com/182590214, https://medium.com/@dominikus/the-end-of-interactivevisualizations-52c585dcafcb


examples of explorable explanations where readers can enter their personal
data, such as location, income, or opinion, to then see how they fit into the
greater scheme. Examples are “You Draw It: How Family Income Predicts
Children’s College Chances” and “Is It Better to Rent or Buy?” from _The New_
_York Times_ . [4] Both pieces are of no value for readers if they don’t enter data:
The value comes _through_ the interaction.


**Newsrooms Use More (in-House) Charting Tools**


More than ever, reporters are pressured to make their articles stand out.
Adding a chart is one solution, but graphics teams struggle to handle the
increasingly large numbers of incoming requests. That’s why we see more
and more newsrooms deciding to use charting tools that make it easy to
create charts, maps and tables with a few clicks. A newsroom has two
options when it comes to charting tools: Use an external charting tool such
as Datawrapper or Infogram, or build an in-house charting tool adjusted to
internal requirements and integrated into the content management system.
Although the second option sounds like a great idea, many newsrooms
will find that it uses more resources than expected. External charting
tools are built by dedicated teams that will maintain the tool and offer
training. Within a newsroom, all of this will often be done by the graphics
or interactive team, leaving them less time for actual news projects. An
in-house charting tool can become a success only if it is made a priority.
The _Neue Zürcher Zeitung_, for example, has three developers that dedicate
their time exclusively to developing and maintaining their charting tool Q.


**Data-Centric Publications Drive Innovation and Visual Literacy**


While a data-driven approach was only considered useful for individual
stories a few years back, we now see entire (successful!) publications build
on this idea. Often, these sites use data as a means to communicate about
publication-specific topics, for example, _FiveThirtyEight_ about politics and
sport, _The Pudding_ about pop culture and _Our World in Data_ about the
long-term development of humanity. Maybe the biggest difference between


4 https://www.nytimes.com/interactive/2015/05/28/upshot/you-draw-it-how-family-incomeaffects-childrens-college-chances.html, https://www.nytimes.com/interactive/2014/upshot/
buy-rent-calculator.html


these publications and others about the same topics is the audience: It’s a
curious and data-orientated one, one that is not afraid of seeing a chart.
As a consequence, data-centric publications can show their readership
harder-to-decipher chart types such as connected scatterplots. If used
well, they give a more complex, less aggregated view of the world and make
comparisons visible in a way that a bar chart wouldn’t be able to do.
A chapter reviewing recent developments can quickly become outdated.
However, the four developments we covered have dominated debates for a
few years now, and we expect them to remain relevant. This is because they
are underpinned by questions with no single right answer in day-to-day
news work: “Do we design a project mobile-first or go with a more complex
solution that only works on desktop?”, “Do we invest effort into making this
visualization interactive and possibly more interesting to readers (even if
only an estimated 10–20% of them will use the interactive features)?”, “Do
we build the visualization from scratch or use a charting tool?”, “Do we
create a visualization for a broader audience or for a data-savvy audience?”
The answers may differ across newsrooms, graphics teams and projects.
But, increasingly, we think, the answers will converge on mobile-first and
non-interactive charts and visualizations built with charting tools and for
an increasingly data-literate audience.


**Works Cited**


Cairo, A., & Schlossberg, T. (2019, August 29). Those hurricane maps don’t mean
what you think they mean. _The New York Times_ . https://www.nytimes.com/
interactive/2019/08/29/opinion/hurricane-dorian-forecast-map.html
Segger, M. (2018, June 28). Lessons for showcasing data journalism on social media.
_Medium_ . https://medium.com/severe-contest/lessons-for-showcasing-datajournalism-on-social-media-17e6ed03a868


**About the Authors**


**Gregor Aisch** is a data journalist, software engineer and former graphics
editor at _The New York Times_ who now works as CTO of the data visualization
tool Datawrapper.


**Lisa Charlotte Rost** is a designer who visualized data for several newsrooms
( _Der Spiegel_, NPR, Bloomberg, _ZEIT Online_ ) before joining Datawrapper.



##### **28. Searchable Databases as a Journalistic** **Product**

_Zara Rahman and Stefan Wehrmeyer_


**Abstract**
Exploring the responsible data challenges and transparency opportunities
of using public-facing searchable databases within a data journalism
investigation.


**Keywords:** databases, responsible data, crowdsourcing, engagement, data
journalism, transparency


A still emerging journalistic format is the searchable online database—a
web interface that gives access to a data set, by newsrooms. This format
is not new, but its use in data journalism projects is still relatively scarce
(Holovaty, 2006).
In this chapter, we review a range of types of databases, from ones which
cover topics which directly affect a reader’s life, to interfaces which are
created in service of further investigative work. Our work is informed by one
of the co-author’s work on Correctiv’s Euros für Ärzte (Euros for Doctors)
investigation, outlined below as an illustrative case study. [1] It is worth
noting, too, that although it has become good practice to make raw data
available after a data-driven investigation, the step of building a searchable
interface for that data is considerably less common.
We consider the particular affordances of creating databases in journalism,
but also note that they open up a number of privacy-related and ethical issues
on how data is used, accessed, modified and understood. We then examine
what responsible data considerations arise as a consequence of using data
in this way, considering the power dynamics inherent within, as well as the


1 https://correctiv.org/recherchen/euros-fuer-aerzte/ (German language)


Bounegru, L. and J. Gray (eds.), _The Data Journalism Handbook:_ _Towards a Critical Data Practice_ .
Amsterdam: Amsterdam University Press, 2021
doi 10.5117/9789462989511_ch28


consequences of putting this kind of information online. We conclude by
offering a set of best practices, which will likely evolve in the future.


**Examples of Journalistic Databases**


Databases can form part of the public-facing aspect of investigative journalism in a number of different ways.
One type of database which has a strong personalization element is
_ProPublica_ ’s Dollars for Docs. It compiled data on payments to doctors and
teaching hospitals that were made by pharmaceutical and medical device
companies. [2] This topic and approach was mirrored by Correctiv and _Der_
_Spiegel_ to create Euros für Ärzte, a searchable database of recipients of payments from pharmaceutical companies, as explained in further detail below.
Both of these approaches involved compiling data from already-available
sources. The goal was to increase the accessibility of said data so that readers
would be able to search it for themselves to, for instance, see if their own
doctor had been the recipient of payments. Both were accompanied by
reporting and ongoing investigations.
Along similar lines, the _Berliner Morgenpost_ built the Schul Finder to
assist parents in finding schools in their area. In this case, the database
interface itself is the main product. [3]

In contrast to the type of database where the data is gathered and prepared
by the newsroom, another style is where the readers can contribute to the
data, sometimes known as “citizen-generated” data, or simply crowdsourcing.
This is particularly effective when the data required is not gathered through
official sources, such as _The Guardian_ ’s crowdsourced database The Counted,
which gathered information on people killed by police in the United States,
in 2015–2016. [4] Their database used online reporting as well as reader input.
Another type of database involves taking an existing set of data and
creating an interface that allows the reader to generate a report based
on criteria they set. For example, the Nauru Files allows readers to view
a summary of incident reports that were written by staff in Australia’s
detention centre on Nauru between 2013 and 2015. [5] The UK-based Bureau


2 https://projects.propublica.org/docdollars/
3 https://interaktiv.morgenpost.de/schul-finder-berlin/#/
4 https://www.theguardian.com/us-news/ng-interactive/2015/jun/01/the-counted-policekillings-us-database
5 https://www.theguardian.com/australia-news/ng-interactive/2016/aug/10/the-nauru-filesthe-lives-of-asylum-seekers-in-detention-detailed-in-a-unique-database-interactive


of Investigative Journalism compiles data from various sources gathered
through their investigations, within a database called Drone Warfare. [6] The
database allows readers to select particular countries covered and the time
frame, in order to create a report with visualizations summarizing the data.
Finally, databases can also be created in service of further journalism, as a
tool to assist research. The International Consortium of Investigative Journalists created and maintain the Offshore Leaks Database, which pulls in data
from the Panama Papers, the Paradise Papers, and other investigations. [7]
Similarly, Organized Crime and Corruption Reporting Project (OCCRP)
maintains and updates OCCRP Data, which allows viewers to search over 19
million public records. [8] In both cases, the primary user of the tools is not
envisioned to be the average reader, but instead journalists and researchers
envisioned to carry out further research on whatever information is found
using these tools.
The list below summarizes the different considerations in making
databases as a news product:

- **Audience:** aimed at readers directly, or as a research database for other
journalists

- **Timeliness:** updated on an ongoing basis, or as a one-off publication

- **Context:** forming part of an investigation or story, or the database itself
as the main product

- **Interactivity:** readers encouraged to give active input to improve the
database, or readers considered primarily as viewers of the data

- **Sources:** using already-public data, or making new information public
via the database


**Case Study: Euros für Ärzte (Euros for Doctors)**


The European Federation of Pharmaceutical Industries and Associations
(EFPIA) is a trade association which counts 33 national associations and
40 pharmaceutical companies among its members. In 2013, the federation
decided that, starting in July 2016, member companies must publish payments to healthcare professionals and organizations in the countries they
operate (EFPIA, 2013). Inspired by _ProPublica_ ’s Dollars for Docs project, the
non-profit German investigative newsroom Correctiv decided to collect


6 https://www.thebureauinvestigates.com/projects/drone-war/
7 https://offshoreleaks.icij.org/
8 https://data.occrp.org/


these publications from the websites of German pharmaceutical companies
and create a central, searchable database of recipients of payments from
pharmaceutical companies for public viewing. They named the investigation
Euros für Ärzte (Euros for Doctors).
In collaboration with the German national news outlet _Der Spiegel_, documents and data were gathered from around 50 websites and converted from
different formats to consistent tabular data. This data was further cleaned
and recipients of payments from multiple companies were matched. The total
time for data cleaning was around ten days and involved up to five people.
A custom database search interface with individual URLs per recipient was
designed and published by Correctiv. [9] The database was updated in 2017
with a similar process. Correctiv also used the same methodology and web
interface to publish data from Austria, in cooperation with derStandard.at
and ORF, and data from Switzerland with Beobachter.ch.
The journalistic objective was to highlight the systemic influence of the
pharmaceutical industry on healthcare professionals through events and
organizations, and the associated conflicts of interest. The searchable database
was intended to encourage readers to start a conversation with their doctor
about the topic, and to draw attention to the very fact that this was happening.
On a different level, the initiative also highlighted the inadequacy of voluntary disclosure rules. Because the publication requirement was an industry
initiative rather than a legal requirement, the database was incomplete—and
it’s unlikely that this will change without legally mandated disclosure.
As described above, the database was incomplete, meaning that a number
of people who had received payments from pharmaceutical companies
were missing from the database. Consequently, when users search for their
doctor, an empty result can either mean the doctor received no payment
or that they denied publication—two vastly different conclusions. Critics
have noted that this puts the spotlight on the cooperative and transparent
individuals, leaving possibly more egregious money flows in the dark. To
counter that, Correctiv provided an opt-in feature for doctors who had not
received payments to also appear in the database, which provides important
context to the narrative, but still leaves uncertainty in the search result.
After publication, both Correctiv and _Der Spiegel_ received dozens of
complaints and legal threats from doctors who appeared in the database.
As the data came from public, albeit difficult to find, sources, the legal team
of _Der Spiegel_ decided to defer most complaints to the pharma companies
and only adjust the database in case of changes at the source.


9 https://correctiv.org/thema/aktuelles/euros-fuer-aerzte/


**Technical Considerations of Building Databases**


For a newsroom considering how to make a data set available and accessible
to readers, there are various criteria to consider, such as size and complexity
of the data set, internal technical capacity of the newsroom, and how readers
should be able to interact with the data.
When a newsroom decides that a database could be an appropriate
product of an investigation, building one requires bespoke development
and deployment—a not insignificant amount of resources. Making that
data accessible via a third-party service is usually simpler and requires
fewer resources.
For example, in the case of Correctiv, the need to search and list around
20,000 recipients and their financial connections to pharma companies
required a custom software solution. Correctiv developed the software
for the database in a separate repository from its main website but in
a way it could be hooked into the content management system. This
decision was made to allow visual and conceptual integration into the
main website and investigation section. To separate concerns, the data
was stored in a relational database separate from the content database.
In this case, having a process and interface for adjusting entries in the
live database was crucial as dozens of upstream data corrections came
in after publication.
However, smaller data sets with simple structures can be made accessible without expensive software development projects. Some third-party
spreadsheet tools (e.g., Google Sheets) allow tables to be embedded. There
are also numerous front-end JavaScript libraries to enhance HTML tables
with searching, filtering and sorting functionalities which can often be
enough to make a few hundred rows accessible to readers.
An attractive middle ground for making larger data sets accessible are
JavaScript-based web applications with access to the data set via API. This
setup lends itself well to running iframe-embeddable search interfaces
without committing to a full-fledged web application. The API can then be
run via third party services while still having full control over the styling
of the front end.


**Affordances Offered by Databases**


Databases within, or alongside, a story, provide a number of affordances
for both readers and newsrooms.


On the reader side, providing an online database allows readers to search
for their own city, politician or doctor and connects the story to their own
life. It provides a different channel for engagement with a story on a more
personal level. Provided there are analytics running on these search queries,
this also gives the newsroom more data on what their readers are interested
in—potentially providing more leads for future work.
On the side of the newsroom, if the database is considered as a long-term
investigative investment, it can be used to automatically cross-reference
entities with other databases or sets of documents for lead generation.
Similarly, if or when other newsrooms decide to make similar databases
available, collaboration and increased coverage becomes much easier while
reusing existing infrastructure and methodologies.
Databases also potentially offer increased optimization for search engines,
thus driving more traffic to the news outlet website. When the database
provides individual URLs for entities within, search engines will pick up
these pages and rank them highly in their results for infrequent keyword
searches related to these numerous entities—the so-called “long tail” of
web searches, thus driving more traffic to the publisher’s site.
Optimizing for search engines can be seen as an unsavoury practice
within journalism; however, providing readers with journalistic information
while they are searching for particular issues can also be viewed as a part
of successful audience engagement. While the goal of the public database
should not be to compete on search keywords, it will likely be a welcome
benefit that drives organic traffic, and can in turn attract new readership.


**Responsible Data Considerations**


Drawing upon the approach of the responsible members of the data community, who work on developing best practices which take into account
the ethical and privacy-related challenges faced by using data in new and
different ways, we can consider the potential risks in a number of ways. [10]

First is the question of the way in which power is distributed in this
situation, where a newsroom decides to publish a database containing
data about people. Usually, those people have no agency or ability to veto
or correct that data prior to publication. The power held by these people
depends very much upon who they are—for example, a politically exposed
person (PEP) included in such a database would presumably have both the


10 https://responsibledata.io/what-is-responsible-data/


expectation of such a development and adequate resources to take action,
whereas a healthcare professional would probably not be expecting to be
involved in an investigation. Once a database is published, visibility of the
people within that database might change rapidly—for example, doctors in
the Euros für Ärzte database gave feedback that one of the top web search
results for their name was now their page in this database.
Power dynamics on the side of the reader or viewer are also worth considering. For whom could the database be most useful? Do they have the
tools and capacity required to be able to make use of the database, or will
this information be used by the already-powerful to further their interests?
This might mean widening the scope of user testing prior to publication
to ensure that enough context is given to properly explain the database to
the desired audience, or including certain features that would make the
database interface more accessible to that group.
The assumption that more data leads to decisions that are better for
society has been questioned on multiple levels in recent years. Education
scholar Clare Fontaine (2017) expands upon this, noting that in the United
States, schools are becoming more segregated despite (or perhaps because
of) an increase in data available about “school performance.” She notes that
“a causal relationship between school choice and rampant segregation hasn’t
yet been established,” but she and others are working more to understand
that relationship, interrogating the perhaps overly simplified relationship
that more information leads to better decisions, and questioning what
“better” might mean (Fontaine, 2017).
Second is the question of the database itself. A database on its own
contains many human decisions; what was collected and what was left
out, and how it was categorized, sorted or analyzed, for example. No piece
of data is objective, although literacy and understanding of the limitations
of data are relatively low, meaning that readers could well misunderstand
the conclusions that are being drawn.
For example, the absence of an organization from a database of political
organizations involved in organized crime may not mean that the organization does not take part in organized crime itself; it simply means that there
was no data available about their actions. Michael Golebiewski and Danah
Boyd (2018) refer to this absence of data as a “data void,” noting that in some
cases a data void may “passively reflect bias or prejudice in society.” This
type of absence of data in an otherwise data-saturated space also maps
closely to what Brooklyn-based artist and researcher Mimi Onuoha (2016)
refers to as a “missing data set,” and highlights the societal choices that go
into collecting and gathering data.


Third is the direction of attention. Databases can change the focus of
public interest from a broader systemic issue to the actions of individuals,
and vice versa. Financial flows between pharmaceutical companies and
healthcare professionals are, clearly, an issue of public interest—but, on
an individual level, doctors might not think of themselves as a person of
public interest. The fact remains, though, that in order to demonstrate an
issue as broader and systemic (as a pattern, rather than a one-off), data
from multiple individuals is necessary. Some databases, such as the Euros
für Ärzte case study mentioned above, also change boundaries of what, or
who, is in the public interest.
Even when individuals agree to the publication of their data, journalists
have to decide how long this data is of public interest and if and when it
should be taken down. The General Data Protection Regulation (GDPR)
will likely affect the way in which journalists should manage this kind of
personal data, and what kinds of mechanisms are available for individuals
to rescind consent to their data being included.
With all of these challenges, our approach is to consider how people’s
rights are affected by both the process and the end result of the investigation
or product. At the heart is understanding that responsible data practices
are ongoing approaches rather than checklists to be considered at specific
points. We suggest that approaches which prioritize the rights of people
reflected in the data throughout the entire investigation, from data gathering
to publication, are a core part of optimizing (data) journalism for trust
(Rosen, 2018).


**Best Practices**


For journalists thinking of building a database to share their investigation
with the public, here are some best practices and recommendations. We
envision these will evolve with time, and we welcome suggestions.
First, ahead of publication, develop a process for how to fix mistakes in
the database. Good data provenance practices can help to find sources of
errors. Second, build in a feedback channel. Particularly when individuals
are unexpectedly mentioned in an investigation, there is likely to be feedback
(or complaints). Providing a good user experience for them to make that
complaint might help the experience. Third, either keep the database up to
date, or clearly mark that it is no longer maintained. Within the journalistic
context, publishing a database demands a higher level of maintenance
than publishing an article. The level of interactivity that a database affords


means that there is a different expectation of how up to date it is compared
to an article. Fourth, allocate enough resources for maintenance over time.
Keeping the data and database software up to date involves significant
resources. For example, adding data from the following year to a database
requires merging newer data with older data, and adding an extra time
dimension to the user interface. Fifth, observe how readers are using the
database. Trends in searches or use might provide leads for future stories
and investigations. Finally, be transparent: It’s rare that a database will be
100% “complete,” and every database will have certain choices built into it.
Rather than glossing over these choices, make them visible so that readers
know what they’re looking at.


**Works Cited**


EFPIA. (2013). About the EFPIA Disclosure Code. European Federation of Pharmaceutical Industries and Associations. https://efpia.eu/media/25046/efpia_
about_disclosure_code_march-2016.pdf
Fontaine, C. (2017, April 20). Driving school choice. _Medium_ . https://points.datasociety.net/driving-school-choice-16f014d8d4df
Golebiewski, M., & Boyd, D. (2018, May). Data voids: Where missing data can be easily
exploited. _Data & Society_ . https://datasociety.net/wp-content/uploads/2018/05/
Data_ Society_Data_Voids_Final_3.pdf
Holovaty, A. (2006, September 6). A fundamental way newspaper sites need to change.
Adrian Holovaty. http://www.holovaty.com/writing/fundamental-change/
Onuoha, M. (2016, February 3). On missing data sets. https://github.com/
MimiOnuoha/missing-datasets
Rosen, J. (2018, May 14). Optimizing journalism for trust. _Medium_ . https://medium.
com/de-correspondent/optimizing-journalism-for-trust-1c67e81c123


**About the Authors**


**Zara Rahman** is deputy director at the Engine Room and a fellow at the
Digital Civil Society Lab at Stanford University’s Centre for Philanthropy
and Civil Society.


**Stefan Wehrmeyer** is the founder of FragDenStaat.de, Germany’s Freedom
of Information Portal, and works as a data journalist and developer.


##### **29. Narrating Water Conflict With Data** **and Interactive Comics**

_Nelly Luna Amancio_


**Abstract**
How we developed an interactive comic to narrate the findings of a
journalistic investigation into the water war in Peru against a big mining
company.


**Keywords:** water conflicts, data journalism, environment, comic, interactivity, Peru


Everything in the comic _La guerra por el agua_ (The war over water) is real
(Figure 29.1). The main characters—Mauro Apaza and Melchora Tacure—
exist, along with their fears and uncertainties. We found them on a hot
September day of 2016. It was noon and there were no shadows, no wind.
She was weeding the soil with her hands, he was making furrows on the
rough ground. For over 70 years they’ve grown food on a small plot of land
in the Tambo Valley, an agricultural area in southern Peru where there
are proposals for a mining project. The history of this couple, like that of
thousands of farmers and Indigenous communities, tells of disputes between
farmers and the powerful industries working to extract one of the world’s
most strategic resources: Water.
How to narrate this confrontation in a country like Peru where there are
more than 200 environmental conflicts and the national budget depends
heavily on income from this sector? How to approach a story about tensions
between precarious farmers, the interests of multinational companies
and those of a government that needs to increase its tax collection? What
narrative can help us to understand this? How is it possible to mobilize
people around this urgent issue? These questions prompted _The War Over_
_Water_ —the first interactive comic in Peru, developed by OjoPúblico.


Bounegru, L. and J. Gray (eds.), _The Data Journalism Handbook:_ _Towards a Critical Data Practice_ .
Amsterdam: Amsterdam University Press, 2021
doi 10.5117/9789462989511_ch29


Figure 29.1. Home screen of the interactive comic The War over Water. Source: _OjoPúblico_ .


The piece integrates data and visualizations into a narrative about this
conflict. [1]


**Why an Interactive Comic?**


The project began in July 2016. We set out to narrate the conflict from an
economic perspective, but to approach the reader from the perspective of
two farmers, through a route that mimics an intimate trip to one of the most
emblematic areas of the conflict. The interactivity of the format allows the
audience to discover the sounds and dialogues of the conflict, across and
beyond the strips.
We chose the story of the Tía María mining project of the Southern Copper
Corporation—one of the biggest mining companies in the world, owned by
one of the richest individuals in Mexico and in the world, Germán Larrea.
Local opposition to this project led to violent police repression that killed
six citizens.
The team that produced this comic was composed of a journalist (myself),
cartoonist Jesús Cossio and web developer Jason Martínez. The three of
us travelled to the Tambo Valley in Arequipa, the heart of the conflict, to
interview leaders, farmers and authorities, and document the process. We
took notes, photos and drawings that would later become the first sketches
of the comic. Upon returning to Lima, we structured what would become the


1 https://laguerraporelagua.ojo-publico.com/en/


Figure 29.2. Data visualisation showing the decrease in tax collection since 2008 in Peru, as a result
of the mining conflict over water. Source: _OjoPúblico_ .


first prototype. Based on the prototype, we wrote the final script, worked
out the interactive features, and started developing the project.


**Honesty With Comics**


We chose the medium of the comic because we believe that journalists should
not—as cartoonist Joe Sacco (2012) puts it—“neuter the truth in the name
of equal time.” Sacco joined us for a presentation of the first chapter of the
project and it was one of his works that inspired us: _Srebrenica_, a webcomic
about the massacre in which more than 8,000 Bosnian Muslims died in 1995.
_The War Over Water_ took eight months to develop. It is based on real events
and has a narrative structure that allows the audience to experience the
daily life of the characters and to surface one of the biggest dilemmas in the
economy of Peru: Agriculture or mining? Is there enough water to do both?
We told the story of this conflict through the eyes and memories of Mauro
and Melchora. The story is accompanied by data visualizations showing
the economic dependency of the region as well as the tax privileges that
mining companies have. All the scenes and the dialogue in the comic are


Figure 29.3. This is how the journalists and the illustrator of _OjoPúblico_ developed the interactive
script of the comic “The War over Water.” Source: _OjoPúblico_ .


real, products of our reporting in the area, interviews with the authorities
and local people, and investigations into the finances of Southern Copper.
We aimed to compose scenes from dialogues, figures, interviews and settings
with honesty and precision.


**From Paper to the Web**


For the cartoonist Jesús Cossio, the challenge was to rethink how to work
with time in an interactive comic: “While in a printed cartoon or static
digital strip the idea is to make the reader stop at the impact of the images,
in an interactive comic the composition and images had to be adapted to
the more agile and dynamic flow of reading.”
From a technological perspective, the project was a challenge for the
OjoPúblico team as we had never developed an interactive comic before.
We used the GreenSock Animation Platform (GSAP), a library that allowed
us to make animations and transitions, as well as to standardize the scenes
and timeline. This was complemented with JavaScript, CSS and HTML5.
The comic has 42 scenes and more than 120 drawings. Jesús Cossio drew
each of the characters, scenes and landscapes in the script with pencil and


ink. These images were then digitized and separated by layers: Backgrounds,
environments, characters and elements of the drawing that had to interact
with each other.


**From the Web Back to Paper**


_The War Over Water_ is a transmedia experience. We have also published
a print edition. With its two platforms, the comic seeks to approach different audiences. One of the greatest interests in the OjoPúblico team is
the exploration of narratives and formats to tell (often complex) stories of
public interest. We have previously won awards for our data investigations.
In other projects we have also used the comic format to narrate the
topic of violence. In _Proyecto Memoria_ (Memory project), the images tell
the horror of the domestic conflict that Peru faced between 1980 and 2000.
Comics provide a powerful language for telling stories with data. This is our
proposal: That investigative journalists should test all possible languages
to tell stories for different audiences. But above all, we want to denounce
imbalances of power—in this case the management of natural resources
in Peru.


**Works Cited**


Sacco, J. (2012). _Journalism_ . Henry Holt and Co.


**About the Author**


**Nelly Luna Amancio** is an investigative journalist, editor and founder of
OjoPúblico, a Peruvian media outlet that investigates power and conducts
cross-border investigations in Latin America.



##### **30. Data Journalism Should Focus on** **People and Stories**

_Winny de Jong_


**Abstract**
The story and the people the story is about should be the sun around
which journalism, including data journalism, revolve.


**Keywords:** storytelling, data journalism, radio, television, data publics,
data visualization


As is the case with people, data journalism and journalism share more
commonalities than differences. [1] Although data-driven reporting builds
on different types of sources which require other skills to interrogate, the
thought process is much the same. Actually, if you zoom out enough, you’ll
find that the processes are almost indistinguishable.


**Known Unknowns**


At its core, journalism is the business of making known unknowns into
known knowns. The concept of knowns and unknowns was popularized
by the US Secretary of Defense Donald Rumsfeld in 2002. At the time there
was a lack of evidence that the Iraqi government had supplied weapons
of mass destruction to terrorist groups. During a press briefing over the
matter, Rumsfeld said:


1 Since ideas are new combinations of old elements, this essay draws on Winny’s 2019 Nieman
Lab prediction, a talk at the Smart News Design Conference in Amsterdam and alshetongeveermaarklopt.nl, a Dutch website that teaches math to journalists.


Bounegru, L. and J. Gray (eds.), _The Data Journalism Handbook:_ _Towards a Critical Data Practice_ .
Amsterdam: Amsterdam University Press, 2021
doi 10.5117/9789462989511_ch30


Reports that say that something hasn’t happened are always interesting
to me, because as we know, there are known knowns; there are things
we know we know. We also know there are known unknowns; that is to
say we know there are some things we do not know. But there are also
unknown unknowns—the ones we don’t know we don’t know. And if one
looks throughout the history of our country and other free countries, it
is the latter category that tend to be the difficult ones. (US Department
of Defense, 2002)


Every journalistic process comes down to moving pawns over the matrix of
knowns and unknowns. All journalism starts with a question—or, to follow
the said matrix, with a known unknown. (You know there is something
you don’t know, hence the question.) When bootstrapping to move from
question or hunch to publication-ready story, the ideal route is to “simply”
move all pawns from known unknowns to known knowns. But as every
journalist will tell you, reality tends to differ. While researching—either by
interviewing people or examining documents or data sets—you are likely to
find things you were not aware that you didn’t know (unknown unknowns),
that require answers, too. If you’re lucky, you might stumble upon some
things you didn’t know you were familiar with (unknown knowns). Working
towards your deadline, you’re transforming three categories of knowledge
into known knowns: Known unknowns (i.e., the questions that got you
started), unknown unknowns (i.e., the questions you didn’t know you should
have asked), and unknown knowns (answers you didn’t know you had).
Unlike our governments, journalists can only proceed to action with, or
publish, known knowns.


**Solid Journalism**


With data-driven reporting and classic bootstrapping being so indistinguishable, surely the two should meet the same standards. Like journalism, data
journalism should always be truthful, independent and free of bias. Like
all other facts, data needs to be verified. So before trying to create known
knowns, ask yourself: Is the data true? What does each number actually
mean? What is the source? Why was the data collected? Who made the data
set? How was the data table created? Are there outliers in the data? Do they
make sense? And, often forgotten but, as with every interview, of significant
importance: What does the source not say? While the requirements and
therefore the questions are the same, the actions they result in slightly differ.


Figure 30.1. Matrix of knowns and unknowns. This matrix differs slightly from the Johari Window,
which is sometimes used in cognitive psychology to help people better understand their relationship with themselves and others. Source: Lars Boogaard.


Figure 30.2. Navigating the knowns and unknowns matrix for journalism. Source: Lars Boogaard.


As Bill Kovach and Tom Rosenstiel (2007) describe in _The Elements of Journal-_
_ism_, the first task of the news journalist is “to verify what information is reliable
and then order it so people can grasp it efficiently.” For data journalists—especially those working in television or radio—this means that the numbers
they came to love do not necessarily have a place in the final production.


Figure 30.3. Still from an NOS video on how thin you need to be to become a fashion model.
Source: _NOS_ .


**Limited Nerdery**


Obviously you should be precise while doing data analysis. But in order to keep
your story “efficiently graspable,” there needs to be a limit on precision—for
example, the number of decimals used—in the final publication. Using “4
out of 10 people” is probably better than “41.8612%.” In my experience the
right amount of precision is pretty close to the precision you would use when
talking about your story to non-data-nerd friends on a Saturday afternoon.
Unless your audience needs to know about the methods and tools used
to be able to grasp the story, you should probably save the nerd goodies
for the methodology. Because when your audience is reading, listening
or watching your data-driven production they should be thinking about
the story, not the data, analysis or technology that keep the story afloat.
This means that the best data journalism might hardly be recognizable as
such—making data journalism an invisible craft. As long as this invisibility
facilitates the story, making your journalism more “efficient to grasp,” it’s
all for the better. After all, journalism creates different maps for citizens
to navigate society with, so we should make sure our maps are readable for
all and read by many.


**Radio and Television**


When publishing data journalism stories for radio or television, less is more.
In the newsroom of NOS, the largest news organization in the Netherlands,


reporters talk about the number of seconds they have to tell their stories.
This means that there is no time to dwell on how a story was made or
why we decided to use the one data source and not the other, if that does
not contribute to the story or the public’s understanding of said story. In
an online video on how thin you need to be to be able to become a high
fashion model, we spent 20 seconds explaining our methods. [2] When you
have 90 seconds to tell a story on national television, 20 seconds is a lot. In
this case, less is more means no time left to explain how we went about the
investigation. When time and space are limited, the story prevails above
everything else.


**Modest Visuals**


Of course, the “less is more” adage goes for data visualizations, too. Data
journalism is much like teenage sex: Everybody talks about it, yet almost
nobody actually does it. When newsrooms finally add data to their toolkit,
some have a tendency to kiss and tell by making data visuals for everything.
Sure, I love visuals, too, especially the innovative, high-end ones—but only if
they add to the story. Visualizations can add value to journalism in multiple
ways. Among others they can do so by deepening the public’s understanding
of the story at hand and by widening the public’s understanding by giving
extra insight at, for example, a regional level. So act like a gentleman and
don’t kiss and tell. Limit yourself to value-adding data visualizations that
help to get the story across. Nowadays most people combine listening to
the radio and watching television with another activity. This limits their
information intake: When driving, listening to news is secondary; the same
goes for watching TV while cooking. So be careful not to ask too much
from your audience. Again, this might make our craft an invisible one; but
we’re here to break news and tell stories—not to flex our dataviz (data
visualization) muscles.


**About People**


All of this is to say that everything that truly matters—in your story, in
journalism and in life at large—does not fit in a data set. It never has, and it
never will. In the end it’s always about people; so whatever you do, wherever


2 https://www.youtube.com/watch?v=DWRGqmywNY


you publish, talk people not data. And when you find yourself tempted
to use more data, technology or news nerdery than necessary, remember
that you’re one of too few craftspeople in this field. That in and of itself
is awesome: There is no need to underline the obvious. So simply stick to
the pecking order found in the best data journalism: Form facilitates data,
facilitates story. Everything and everybody needs to revolve around the
story—it is our sun. Story is king.


**Works Cited**


Kovach, B., & Rosenstiel, T. (2007). _The elements of journalism: What newspeople_
_should know and the public should expect_ . Three Rivers Press.
US Department of Defense. (2002, February 12). DoD News Briefing—Secretary
Rumsfeld and Gen. Myers [Interview transcript]. https://archive.defense.gov/
Transcripts/Transcript.aspx?TranscriptID=2636


**About the Author**


**Winny de Jong** works as a data journalist at the Dutch national news
broadcaster NOS and publishes the weekly _Data Journalism Newsletter_ at
ddj.news.


###### Investigating Data, Platforms and Algorithms


##### **31. The Algorithms Beat: Angles and** **Methods for Investigation**

_Nicholas Diakopoulos_


**Abstract**
A beat on algorithms is coalescing as journalistic skills come together
with technical skills to provide the scrutiny that algorithms deserve.


**Keywords:** algorithms, algorithmic accountability, computational journalism, investigative journalism, algorithm studies, freedom of information
(FOI)


The “Machine Bias” series from _ProPublica_ began in May 2016 as an effort
to investigate algorithms in society. [1] Perhaps most striking in the series
was an investigation and analysis exposing the racial bias of recidivism risk
assessment algorithms used in criminal justice decisions (Angwin et al.,
2016). These algorithms score individuals based on whether they are a low
or high risk of reoffending. States and other municipalities variously use the
scores for managing pretrial detention, probation, parole and sometimes
even sentencing. Reporters at _ProPublica_ filed a public records request
for the scores from Broward County in Florida and then matched those
scores to actual criminal histories to see whether an individual had actually
recidivated (i.e., reoffended) within two years. Analysis of the data showed
that Black defendants tended to be assigned higher risk scores than White
defendants, and were more likely to be incorrectly labelled as high risk
when in fact after two years they hadn’t actually been rearrested (Larson
et al., 2016).
Scoring in the criminal justice system is, of course, just one domain where
algorithms are being deployed in society. The “Machine Bias” series has since


1 https://www.propublica.org/series/machine-bias


Bounegru, L. and J. Gray (eds.), _The Data Journalism Handbook:_ _Towards a Critical Data Practice_ .
Amsterdam: Amsterdam University Press, 2021
doi 10.5117/9789462989511_ch31


covered everything from Facebook’s ad-targeting system, to geographically
discriminatory auto insurance rates, and unfair pricing practices on Amazon.
com. Algorithmic decision making is increasingly pervasive throughout both
the public and private sectors. We see it in domains like credit and insurance
risk scoring, employment systems, welfare management, educational and
teacher rankings, and online media curation, among many others (Eubanks,
2018; O’Neil, 2016; Pasquale, 2015). Operating at scale and often impacting
large swaths of people, algorithms can make consequential and sometimes
contestable calculation, ranking, classification, association and filtering
decisions. Algorithms, animated by piles of data, are a potent new way of
wielding power in society.
As _ProPublica_ ’s “Machine Bias” series attests, a new strand of computational and data journalism is emerging to investigate and hold accountable
how power is exerted through algorithms. I call this _algorithmic account-_
_ability reporting_, a re-orientation of the traditional watchdog function of
journalism towards the power wielded through algorithms (Diakopoulos,
2015). [2] Despite their ostensible objectivity, algorithms can and do make
mistakes and embed biases that warrant closer scrutiny. Slowly, a beat on
algorithms is coalescing as journalistic skills come together with technical
skills to provide the scrutiny that algorithms deserve.
There are, of course, a variety of forms of algorithmic accountability
that may take place in diverse forums beyond journalism, such as in political, legal, academic, activist or artistic contexts (Brain & Mattu, n.d.;
Bucher, 2018). [3] But my focus is this chapter is squarely on algorithmic
accountability reporting as an independent journalistic endeavour that
contributes to accountability by mobilizing public pressure. This can be
seen as complementary to other avenues that may ultimately also contribute
to accountability, such as by developing regulations and legal standards,
creating audit institutions in civil society, elaborating effective transparency
policies, exhibiting reflexive art shows, and publishing academic critiques.


2 The term _algorithmic accountability_ was originally coined in: Diakopoulos, N. (2013,
August 2). Sex, violence, and autocomplete algorithms. _Slate Magazine_ . https://slate.com/
technology/2013/08/words-banned-from-bing-and-googles-autocomplete-algorithms.html;
and elaborated in: Diakopoulos, N. (2013, October 3). Rage against the algorithms. _The Atlantic_ .
https://www.theatlantic.com/technology/archive/2013/10/rage-against-the-algorithms/280255/
3 For an activist/artistic frame, see: Brain, T., & Mattu, S. (n.d.). _Algorithmic disobedience_ .
https://samatt.github.io/algorithmic-disobedience/#/. For an academic treatment examining
algorithmic power, see: Bucher, T. (2018). _If . . . then: Algorithmic power and politics_ . Oxford
University Press. A broader selection of the academic scholarship on critical algorithm studies
can be found here: https://socialmediacollective.org/reading-lists/critical-algorithm-studies/


In deciding what constitutes the beat in journalism, it is first helpful
to define what is newsworthy about algorithms. Technically speaking,
an algorithm is a sequence of steps followed in order to solve a particular
problem or to accomplish a defined outcome. In terms of information
processes, the outcomes of algorithms are typically decisions. The crux of
algorithmic power often boils down to computers’ ability to make such decisions very quickly and at scale, potentially affecting large numbers of people.
In practice, algorithmic accountability is not just about the technical side
of algorithms, however—algorithms should be understood as composites
of technology woven together with people such as designers, operators,
owners and maintainers in complex sociotechnical systems (Ananny, 2015;
Seaver, 2017). Algorithmic accountability is about understanding how those
people exercise power within and through the system, and are ultimately
responsible for the system’s decisions. Oftentimes what makes an algorithm
newsworthy is when it somehow makes a “bad” decision. This might involve
an algorithm doing something it was not supposed to do, or perhaps not doing
something it was supposed to do. For journalism, the public significance
and consequences of a bad decision are key factors. What is the potential
harm for an individual, or for society? Bad decisions might impact individuals directly, or in aggregate may reinforce issues like structural bias. Bad
decisions can also be costly. Let’s look at how various bad decisions can
lead to news stories.


**Angles on Algorithms**


In observing the algorithms beat developed over the last several years
in journalism, as well as through my own investigations of algorithms, I
have identified at least four driving forces that appear to underlie many
algorithmic accountability stories: (a) discrimination and unfairness, (b)
errors or mistakes in predictions or classifications, (c) legal or social norm
violations, and (d) misuse of algorithms by people either intentionally
or inadvertently. I provide illustrative examples of each of these in the
following subsections.
**Discrimination and Unfairness.** Uncovering discrimination and unfairness is a common theme in algorithmic accountability reporting. The
story from _ProPublica_ that opened this chapter is a striking example of
how an algorithm can lead to systematic disparities in the treatment of
different groups of people. Northpointe, the company that designed the
risk assessment scores (since renamed Equivant), argued the scores were


equally accurate across races and were therefore fair. But their definition of
fairness failed to take into account the disproportionate volume of mistakes
that affected Black people. Stories of discrimination and unfairness hinge
on the definition of fairness applied, which may reflect different political
suppositions (Lepri et al., 2018).
I have also worked on stories that uncover unfairness due to algorithmic
systems—in particular looking at how Uber pricing dynamics may differentially affect neighbourhoods in Washington, DC (Stark & Diakopoulos,
2016). Based on initial observations of different waiting times and how
those waiting times shifted based on Uber’s surge pricing algorithm, we
hypothesized that different neighbourhoods would have different levels of
service quality (i.e., waiting time). By systematically sampling the waiting
times in different census tracts over time, we showed that census tracts
with more people of colour tend to have longer wait times for a car, even
when controlling for other factors like income, poverty rate and population
density in the neighbourhood. It is difficult to pin the unfair outcome directly
to Uber’s technical algorithm because other human factors also drive the
system, such as the behaviour and potential biases of Uber drivers. But the
results do suggest that when considered as a whole, the system exhibits
disparity associated with demographics.
**Errors and Mistakes.** Algorithms can also be newsworthy when they
make specific errors or mistakes in their classification, prediction or filtering
decisions. Consider the case of platforms like Facebook and Google which
use algorithmic filters to reduce exposure to harmful content like hate
speech, violence and pornography. This can be important for the protection
of specific vulnerable populations, like children, especially in products (such
as Google’s YouTube Kids) which are explicitly marketed as safe for children.
Errors in the filtering algorithm for the app are newsworthy because they
mean that sometimes children encounter inappropriate or violent content
(Maheshwari, 2017). Classically, algorithms make two types of mistakes: False
positives and false negatives. In the YouTube Kids scenario, a false positive
would be a video mistakenly classified as inappropriate when actually it’s
totally fine for kids. A false negative is a video classified as appropriate
when it is really not something you want kids watching.
Classification decisions impact individuals when they either increase or
decrease the positive or negative treatment an individual receives. When
an algorithm mistakenly selects an individual to receive free ice cream
(increased positive treatment), you won’t hear that individual complain
(although when others find out, they might say it’s unfair). Errors are
generally newsworthy when they lead to increased negative treatment for


a person, such as by exposing a child to an inappropriate video. Errors are
also newsworthy when they lead to a decrease in positive treatment for
an individual, such as when a person misses an opportunity. Just imagine
a qualified buyer who never gets a special offer because an algorithm
mistakenly excludes them. Finally, errors can be newsworthy when they
cause a decrease in warranted negative attention. Consider a criminal
risk assessment algorithm mistakenly labelling a high-risk individual as
low-risk—a false negative. While that’s great for the individual, this creates
a greater risk to public safety by setting free an individual who might go on
to commit a crime again.
**Legal and Social Norm Violations.** Predictive algorithms can sometimes
test the boundaries of established legal or social norms, leading to other
opportunities and angles for coverage. Consider for a moment the possibility
of algorithmic defamation (Diakopoulos, 2013; Lewis et al., 2019). Defamation
is defined as “a false statement of fact that exposes a person to hatred,
ridicule or contempt, lowers him in the esteem of his peers, causes him to
be shunned, or injures him in his business or trade.” [4] Over the last several
years there have been numerous stories, and legal battles, over individuals
who feel they have been defamed by Google’s autocomplete algorithm. An
autocompletion can link an individual’s or a company’s name to everything
from crime and fraud to bankruptcy or sexual conduct, which can then
have consequences for reputation. Algorithms can also be newsworthy
when they encroach on social norms like privacy. For instance, _Gizmodo_
has extensively covered the “People You May Know” (PYMK) algorithm
on Facebook, which suggests potential “friends” on the platform that are
sometimes inappropriate or undesired (Hill, 2017b). In one story, reporters
identified a case where PYMK outed the real identity of a sex worker to her
clients (Hill, 2017a). This is problematic not only because of the potential
stigma attached to sex work, but also out of fear of clients who could become
stalkers.
Defamation and privacy violations are only two possible story angles
here. Journalists should be on the lookout for a range of other legal or social
norm violations that algorithms may create in various social contexts.
Since algorithms necessarily rely on a quantified version of reality that
only incorporates what is measurable as data they can miss a lot of the
social and legal context that would otherwise be essential in rendering an
accurate decision. By understanding what a particular algorithm actually
quantifies about the world—how it “sees” things—journalists can inform


4 http://www.dmlp.org/legal-guide/defamation


critique by illuminating the missing bits that would support a decision in
the richness of its full context.
**Human Misuse.** Algorithmic decisions are often embedded in larger
decision-making processes that involve a constellation of people and algorithms woven together in a sociotechnical system. Despite the inaccessibility
of some of their sensitive technical components, the sociotechnical nature
of algorithms opens up new opportunities for investigating the relationships
that users, designers, owners and other stakeholders may have to the overall
system (Trielli & Diakopoulos, 2017). If algorithms are misused by the people
in the sociotechnical ensemble, this may also be newsworthy. The designers
of algorithms can sometimes anticipate and articulate guidelines for a
reasonable set of use contexts for a system, and so if people ignore these in
practice it can lead to a story of negligence or misuse. The risk assessment
story from _ProPublica_ provides a salient example. Northpointe had in fact
created two versions and calibrations of the tool, one for men and one for
women. Statistical models need to be trained on data reflective of the
population where they will be used and gender is an important factor in
recidivism prediction. But Broward County was misusing the risk score
designed and calibrated for men by using it for women as well (Larson, 2016).


**How to Investigate an Algorithm**


There are various routes to the investigation of algorithmic power and no
single approach will always be appropriate. But there is a growing stable of
methods to choose from, including everything from highly technical reverse
engineering and code-inspection techniques, to auditing using automated
or crowdsourced data collection, or even low-tech approaches to prod and
critique based on algorithmic reactions (Diakopoulos, 2017, 2019). [5] Each
story may require a different approach depending on the angle and the specific context, including what degree of access to the algorithm, its data and
its code is available. For instance, an exposé on systematic discrimination
may lean heavily on an audit method using data collected online, whereas
a code review may be necessary to verify the correct implementation of


5 For more a more complete treatment of methodological options, see: Diakopoulos, N. (2019).
_Automating the news: How algorithms are rewriting the media_ . Harvard University Press; see
also: Diakopoulos, N. (2017). Enabling accountability of algorithmic media: Transparency as a
constructive and critical lens. In T. Cerquitelli, D. Quercia, & F. Pasquale (Eds.), _Transparent_
_data mining for big and small data_ (pp. 25–43). Springer International Publishing. https://doi.
org/10.1007/978-3-319-54024-5_2


an intended policy (Lecher, 2018). Traditional journalistic sourcing to talk
to company insiders such as designers, developers and data scientists, as
well as to file public records requests and find impacted individuals, are as
important as ever. I can’t go into depth on all of these methods in this short
chapter, but here I want to at least elaborate a bit more on how journalists
can investigate algorithms using auditing.
Auditing techniques have been used for decades to study social bias in
systems like housing markets and have recently been adapted for studying
algorithms (Gaddis, 2017; Sandvig et al., 2014). The basic idea is that if the
inputs to algorithms are varied in enough different ways, and the outputs
are monitored, then inputs and outputs can be correlated to build a theory
for how the algorithm may be functioning (Diakopoulos, 2015). If we have
some expected outcome that the algorithm violates for a given input this
can help tabulate errors and see if errors are biased in systematic ways.
When algorithms can be accessed via APIs or online web pages output
data can be collected automatically (Valentino-DeVries et al., 2012). For
personalized algorithms, auditing techniques have also been married to
crowdsourcing in order to gather data from a range of people who may
each have a unique “view” of the algorithm. AlgorithmWatch in Germany
has used this technique effectively to study the personalization of Google
Search results, collecting almost 6 million search results from more than
4,000 users who shared data via a browser plug-in (as discussed further by
Christina Elmer in her chapter in this book). [6] _Gizmodo_ has used a variant
of this technique to help investigate Facebook’s PYMK. Users download a
piece of software to their computer that periodically tracks PYMK results
locally to the user’s computer, maintaining their privacy. Reporters can then
solicit tips from users who think their results are worrisome or surprising
(Hill & Mattu, 2018).
Auditing algorithms is not for the faint of heart. Information deficits
limit an auditor’s ability to sometimes even know where to start, what to
ask for, how to interpret results and how to explain the patterns they are
seeing in an algorithm’s behaviour. There is also the challenge of knowing
and defining what is expected of an algorithm, and how those expectations
may vary across contexts and according to different global moral, social,
cultural and legal standards and norms. For instance, different expectations
for fairness may come into play for a criminal risk assessment algorithm
in comparison to an algorithm that charges people different prices for an


6 https://algorithmwatch.org/filterblase-geplatzt-kaum-raum-fuer-personalisierung-beigoogle-suchen-zur-bundestagswahl-2017/ (German language)


airline seat. In order to identify a newsworthy mistake or bias you must first
define what normal or unbiased should look like. Sometimes that definition
comes from a data-driven baseline, such as in our audits of news sources in
Google search results during the 2016 US elections (Diakopoulos et al., 2018).
The issue of legal access to information about algorithms also crops up and
is, of course, heavily contingent on the jurisdiction (Bhandari & Goodman,
2017). In the United States, freedom of information (FOI) laws govern the
public’s access to government documents, but the response from different
agencies for documents relating to algorithms is uneven at best (see Brauneis
& Goodman, 2018; Diakopoulos, 2016; Fink, 2017). Legal reforms may be in
order so that public access to information about algorithms is more easily
facilitated. And if information deficits, difficult-to-articulate expectations
and uncertain legal access are not challenging enough, just remember that
algorithms can also be quite capricious. Today’s version of the algorithm
may already be different than yesterday’s: As one example, Google typically
changes its search algorithm 500–600 times a year. Depending on the stakes
of the potential changes, algorithms may need to be monitored over time
in order to understand how they are changing and evolving.


**Recommendations Moving Forward**


To get started and make the most of algorithmic accountability reporting,
I would recommend three things. Firstly, we have developed a resource
called Algorithm Tips, which curates relevant methods, examples and
educational resources, and hosts a database of algorithms for potential
investigation (first covering algorithms in the US federal government
and then expanded to cover more jurisdictions globally). [7] If you are looking for resources to learn more and help to get a project off the ground,
that could be one starting point (Trielli et al., 2017). Secondly, focus on
the outcomes and impacts of algorithms rather than trying to explain
the exact mechanism of their decision making. Identifying algorithmic
discrimination (i.e., an output) oftentimes has more value to society as
an initial step than explaining exactly how that discrimination came
about. By focusing on outcomes, journalists can provide a first-order
diagnostic and signal an alarm which other stakeholders can then dig into
in other accountability forums. Finally, much of the published algorithmic
accountability reporting I have cited here is done in teams, and with


7 http://algorithmtips.org/


good reason. Effective algorithmic accountability reporting demands all
of the traditional skills journalists need in reporting and interviewing,
domain knowledge of a beat, public records requests and analysis of the
returned documents, and writing results clearly and compellingly, while
often also relying on a host of new capabilities like scraping and cleaning
data, designing audit studies, and using advanced statistical techniques.
Expertise in these different areas can be distributed among a team, or
with external collaborators, as long as there is clear communication,
awareness and leadership. In this way, methods specialists can partner
with different domain experts to understand algorithmic power across a
larger variety of social domains.


**Works Cited**


Ananny, M. (2015). Toward an ethics of algorithms. _Science, Technology & Human_
_Values_, _41_ (1), 93–117.
Angwin, J., Larson, J., Mattu, S., & Kirchner, L. (2016, May 23). Machine bias.
_ProPublica_ . https://www.propublica.org/article/machine-bias-risk-assessmentsin-criminal-sentencing
Bhandari, E., & Goodman, R. (2017). Data journalism and the computer
fraud and abuse act: Tips for moving forward in an uncertain landscape.
Computation+Journalism Symposium. https://www.aclu.org/other/datajournalism-and-computer-fraud-and-abuse-act-tips-moving-forward-uncertainlandscape
Brain, T., & Mattu, S. (n.d.). Algorithmic disobedience. https://samatt.github.io/
algorithmic-disobedience/
Brauneis, R., & Goodman, E. P. (2018). Algorithmic transparency for the smart city.
_Yale Journal of Law & Technology_, _20_, 103–176.
Bucher, T. (2018). _If . . . then: Algorithmic power and politics_ . Oxford University Press.
Diakopoulos, N. (2013, August 6). Algorithmic defamation: The case of the
shameless autocomplete. Tow Center for Journalism. https://towcenter.org/
algorithmic-defamation-the-case-of-the-shameless-autocomplete
Diakopoulos, N. (2015). Algorithmic accountability: Journalistic investigation of
computational power structures. _Digital Journalism_, _3_ (3), 398–415. https://doi.
org/10.1080/21670811.2014.976411
Diakopoulos, N. (2016, May 24). We need to know the algorithms the government uses to make important decisions about us. _The Conversation_ . http://
theconversation.com/we-need-to-know-the-algorithms-the-government-usesto-make-important-decisions-about-us-57869


Diakopoulos, N. (2017) Enabling Accountability of Algorithmic Media: Transparency
as a Constructive and Critical Lens. In T. Cerquitelli, D. Quercia, & F. Pasquale
(Eds.), _Transparent data mining for Big and Small Data_ (pp. 25–44). Springer.
Diakopoulos, N. (2019). _Automating the News: How Algorithms are Rewriting the_
_Media_ . Harvard University Press.
Diakopoulos, N., Trielli, D., Stark, J., & Mussenden, S. (2018). I vote for—How search
informs our choice of candidate. In M. Moore & D. Tambini (Eds.), _Digital Domi-_
_nance: The power of Google, Amazon, Facebook, and Apple_ (pp. 320–341). Oxford
University Press. https://www.academia.edu/37432634/I_Vote_For_How_Search_
Informs_Our_Choice_of_Candidate
Eubanks, V. (2018). _Automating inequality: How high-tech tools profile, police, and_
_punish the poor_ . St. Martin’s Press.
Fink, K. (2017). Opening the government’s black boxes: Freedom of information
and algorithmic accountability. _Digital Journalism_, _17_ (1). https://doi.org/10.108
0/1369118X.2017.1330418
Gaddis, S. M. (2017). An introduction to audit studies in the social sciences. In M.
Gaddis (Ed.), _Audit studies: Behind the scenes with theory, method, and nuance_
(pp. 3–44). Springer International Publishing.
Gillespie, T., & Seaver, N. (2015, November 5). Critical algorithm studies: A reading
list. _Social Media Collective_ . https://socialmediacollective.org/reading-lists/
critical-algorithm-studies/
Hill, K. (2017a, October). How Facebook outs sex workers. _Gizmodo_ . https://gizmodo.
com/how-facebook-outs-sex-workers-1818861596
Hill, K. (2017b, November). How Facebook figures out everyone you’ve ever met.
_Gizmodo_ . https://gizmodo.com/how-facebook-figures-out-everyone-youveever-met-1819822691
Hill, K., & Mattu, S. (2018, January 10). Keep track of who Facebook thinks you
know with this nifty tool. _Gizmodo_ . https://gizmodo.com/keep-track-of-whofacebook-thinks-you-know-with-this-ni-1819422352
Larson, J. (2016, October 20). Machine bias with Jeff Larson [Data Stories podcast].
https://datastori.es/85-machine-bias-with-jeff-larson/
Larson, J., Mattu, S., Kirchner, L., & Angwin, J. (2016, May 23). How we analyzed
the COMPAS recidivism algorithm. _ProPublica_ . https://www.propublica.org/
article/how-we-analyzed-the-compas-recidivism-algorithm
Lecher, C. (2018, March 21). What happens when an algorithm cuts your
health care. _The Verge_ . https://www.theverge.com/2018/3/21/17144260/
healthcare-medicaid-algorithm-arkansas-cerebral-palsy
Lepri, B., Oliver, N., Letouzé, E., Pentland, A., & Vinck, P. (2018). Fair, transparent, and
accountable algorithmic decision-making processes. _Philosophy & Technology_,
_31_ (4), 611–627. https://doi.org/10.1007/s13347-017-0279-x


Lewis, S. C., Sanders, A. K., & Carmody, C. (2019). Libel by algorithm? Automated
journalism and the threat of legal liability. _Journalism and Mass Communication_
_Quarterly_, _96_ (1), 60–81. https://doi.org/10.1177/1077699018755983
Maheshwari, S. (2017, November 4). On Youtube Kids, startling videos slip past
filters. _The New York Times_ . https://www.nytimes.com/2017/11/04/business/
media/youtube-kids-paw-patrol.html?_r=0
O’Neil, C. (2016). _Weapons of math destruction: How big data increases inequality_
_and threatens democracy_ . Broadway Books.
Pasquale, F. (2015). _The black box society: The secret algorithms that control money_
_and information_ . Harvard University Press.
Sandvig, C., Hamilton, K., Karahalios, K., & Langbort, C. (2014, May 22). Auditing algorithms: Research methods for detecting discrimination on Internet
platforms. International Communication Association preconference on Data
and Discrimination Converting Critical Concerns into Productive Inquiry,
Seattle, WA.
Seaver, N. (2017). Algorithms as culture: Some tactics for the ethnography of algorithmic systems. _Big Data & Society_, _4_ (2). https://doi.org/10.1177/2053951717738104
Stark, J., & Diakopoulos, N. (2016, March 10). Uber seems to offer better service in
areas with more White people. That raises some tough questions. _The Wash-_
_ington Post_ . https://www.washingtonpost.com/news/wonk/wp/2016/03/10/
uber-seems-to-offer-better-service-in-areas-with-more-white-people-thatraises-some-tough-questions/
Trielli, D., & Diakopoulos, N. (2017, May 30). How to report on algorithms even
if you’re not a data whiz. _Columbia Journalism Review_ . https://www.cjr.org/
tow_center/algorithms-reporting-algorithmtips.php
Trielli, D., Stark, J., & Diakopoulos, N. (2017). _Algorithm tips: A resource for algorithmic_
_accountability in Government_ . Computation + Journalism Symposium.
Valentino-DeVries, J., Singer-Vine, J., & Soltani, A. (2012, December 24). Websites
vary prices, deals based on users’ information. _The Wall Street Journal_ . https://
www.wsj.com/articles/SB10001424127887323777204578189391813881534


**About the Author**


**Nicholas Diakopoulos** is an Assistant Professor at Northwestern University
School of Communication, where he directs the Computational Journalism
Lab. He is the author of _Automating the News: How Algorithms are Rewriting_
_the Media_ (Harvard University Press, 2019).



##### **32. Telling Stories With the Social Web**

_Lam Thuy Vo_


**Abstract**
This chapter is a primer into investigating the social web.


**Keywords:** social media, misinformation, data journalism, data analysis,
data visualization, bots


We have become the largest producers of data in history. [1] Almost every click
online, each swipe on our tablets and each tap on our smartphone produces
a data point in a virtual repository. Facebook generates data on the lives of
more than 2 billion people. Twitter records the activities of more than 330
million monthly users. One MIT study found that the average American
office worker was producing 5GB of data each day (Tucker, 2013). That was in
2013 and we haven’t slowed down. As more and more people conduct their
lives online, and as smartphones are penetrating previously unconnected
regions around the world, this trove of stories is only becoming larger.
A lot of researchers tend to treat each social media user like they would
treat an individual subject—as anecdotes and single points of contact. But
to do so with a handful of users and their individual posts is to ignore the
potential of hundreds of millions of others and their interactions with one
another. There are many stories that could be told from the vast amounts of
data produced by social media users and platforms because researchers and
journalists are still only starting to acquire the large-scale data-wrangling
expertise and analytical techniques needed to tap them.
Recent events have also shown that it is becoming crucial for reporters to
gain a better grasp of the social web. The Russian interference with the 2016


1 Earlier versions of this chapter have been published at: https://source.opennews.org/articles/
what-buzzfeed-news-learned-after-year-mining-data-/, http://www.niemanlab.org/2016/12/
the-primary-source-in-the-age-of-mechanical-multiplication/


Bounegru, L. and J. Gray (eds.), _The Data Journalism Handbook:_ _Towards a Critical Data Practice_ .
Amsterdam: Amsterdam University Press, 2021
doi 10.5117/9789462989511_ch32


US presidential elections and Brexit; the dangerous spread of anti-Muslim
hate speech on Facebook in countries in Europe and in Myanmar; and the
heavy-handed use of Twitter by global leaders—all these developments
show that there’s an ever-growing need to gain a competent level of literacy
around the usefulness and pitfalls of social media data in aggregate.


**How Can Journalists Use Social Media Data?**


While there are many different ways in which social media can be helpful
in reporting, it may be useful to examine the data we can harvest from
social media platforms through two lenses.
First, social media can be used as a proxy to better understand individuals
and their actions. Be it public proclamations or private exchanges between
individuals—a lot of people’s actions, as mediated and disseminated through
technology nowadays, leave traces online that can be mined for insights.
This is particularly helpful when looking at politicians and other important
figures, whose public opinions could be indicative of their policies or have
real-life consequences like the plummeting of stock prices or the firing of
important people.
Second, the web can be seen as an ecosystem in its own right in which
stories take place on social platforms (albeit still driven by human and
automated actions). Misinformation campaigns, algorithmically skewed
information universes and trolling attacks are all phenomena that are
unique to the social web.


**Case Studies**


Instead of discussing these kinds of stories in the abstract, it may be more
helpful to understand social media data in the context of how it can be
used to tell particular stories. The following sections discuss a number of
journalistic projects that made use of social media data.


**Understanding Public Figures: Social Media Data for**
**Accountability Reporting**


For public figures and everyday people alike, social media has become a way
to address the public in a direct manner. Status updates, tweets and posts


Figure 32.1. A snapshot of the media links that Trump tweeted during his presidential campaign.
Source: _BuzzFeed News_ .


can serve as ways to bypass older projection mechanisms like interviews
with the news media, press releases or press conferences.
For politicians, however, these public announcements—these projections
of their selves—may become binding statements and in the case of powerful
political figures may become harbingers for policies that have yet to be put
in place.
Because a politician’s job is partially to be public-facing, researching
a politician’s social media accounts can help us better understand their
ideological mindset. For one story, my colleague Charlie Warzel and I collected and analyzed more than 20,000 of Donald Trump’s tweets to answer
the following question: What kind of information does he disseminate and
how can this information serve as a proxy for the kind of information he
may consume?
Social data points are not a full image of who we actually are, in part due to
their performative nature and in part because these data sets are incomplete
and so open to individual interpretation. But they can help as complements:
President Trump’s affiliation with _Breitbart_ online, as shown in Figure 32.1,
was an early indicator for his strong ties to Steve Bannon in real life. His
retweeting of smaller conservative blogs like the Conservative Tree House
and News Ninja 2012 perhaps hinted at his distrust of “mainstream media.”


**Tracing Back Human Actions**


While public and semi-public communications like tweets and open
Facebook posts can give insights into how people portray themselves to
others, there’s also the kind of data that lives on social platforms behind
closed walls like private messages, Google searches or geolocation data.
Christian Rudder (2014), co-founder of OKCupid and author of the book
_Dataclysm_, had a rather apt description of this kind of data: These are
statistics that are recorded of our behaviour when we “think that no one
is watching.”
By virtue of using a social platform, a person ends up producing longitudinal data of their own behaviour. And while it’s hard to extrapolate
much from these personal data troves beyond the scope of the person who
produced them, this kind of data can be extremely powerful when trying
to tell the story of one person. I often like to refer this kind of approach as
a “quantified selfie,” a term Maureen O’Connor coined for me when she
described some of my work.
Take the story of Jeffrey Ngo, for instance. When pro-democracy protests
began in his hometown, Hong Kong, in early September 2014, Ngo, a New
York University student originally from Hong Kong, felt compelled to act.
Ngo started to talk to other expatriate Hong Kongers in New York and in
Washington, DC. He ended up organizing protests in 86 cities across the
globe and his story is emblematic of many movements that originate on
global outrage about an issue.
For this _Al Jazeera America_ story, Ngo allowed us to mine his personal
Facebook history—an archive that each Facebook user can download from
the platform (Vo, 2015). We scraped the messages he exchanged with another
core organizer in Hong Kong and found 10 different chat rooms in which the
two and other organizers exchanged thoughts about their political activities.
The chart below (Figure 32.2) documents the ebbs and flows of their
communications. First there’s a spike of communications when a news
event brought about public outrage—Hong Kong police throwing tear gas
at peaceful demonstrators. Then there’s the emergence of one chat room,
the one in beige, which became the chat room in which the core organizers
planned political activities well beyond the initial news events.
Since most of their planning took place inside these chat rooms, we were
also able to recount the moment when Ngo first met his co-organizer, Angel
Yau. Ngo himself wasn’t able to recall their first exchanges but thanks to the
Facebook archive we were able to reconstruct the very first conversation
Ngo had with Yau.


Figure 32.2. United for Democracy: Global Solidarity with Hong Kong Facebook group.
Facebook data courtesy of Jeffrey Ngo. Source: _BuzzFeed News_ .


While it is clear that Ngo’s evolution as a political organizer is that of an
individual and by no means representative of every person who participated
in his movement, it is, however, emblematic of the _kind_ of path a political
organizer may take in the digital age.


**Phenomena Specific to Online Ecosystems**


Many of our interactions are moving exclusively to online platforms. While
much of our social behaviour online and offline is intermingled, our online
environments are still quite particular because online human beings are
assisted by powerful tools.
There’s bullying for one. Bullying has arguably existed as long as
humankind. But now bullies are assisted by thousands of other bullies
who can be called upon within the blink of an eye. Bullies have access
to search engines and digital traces of a person’s life, sometimes going as
far back as that person’s online personas go. And they have the means of
amplification—one bully shouting from across the hallway is not nearly as
deafening as thousands of them coming at you all at the same time. Such
is the nature of trolling.


Figure 32.3 - A chart of Doris Truong’s Twitter mentions starting the day of the ­attack. Source:
BuzzFeed News. https://www.buzzfeednews.com/article/lamvo/heres-what-it-feels-like-to-betrolled-in-trumps-america


_Washington Post_ editor Doris Truong, for instance, found herself at
the heart of a political controversy online. Over the course of a few days,
trolls (and a good amount of people defending her) directed 24,731 Twitter
mentions at her. Being pummelled with vitriol on the Internet can only be
ignored for so long before it takes some kind of emotional toll.
Trolling, not unlike many other online attacks, have become problems
that can afflict any person now—famous or not. From Yelp reviews of businesses that go viral—like the cake shop that refused to prepare a wedding
cake for a gay couple—to the ways in which virality brought about the
firing and public shaming of Justine Sacco—a PR person who made an
unfortunate joke about HIV and South Africans right before she took off
on an intercontinental flight—many stories that affect our day-to-day life
take place online these days.


**Information Wars**


The emergence and the ubiquitous use of social media have brought about
a new phenomenon in our lives: Virality.


Figure 32.4. _BuzzFeed News_ compared one of its own human editors’ Twitter data, @tomnamako,
and the data of several accounts that displayed bot-like activity to highlight their differences in
personas and behavior. The first chart above shows that the _BuzzFeed News_ editor’s last 2,955
tweets are evenly distributed throughout several months. His daily tweet count barely ever
surpassed the mark of 72 tweets per day, which the Digital Forensics Research Lab designated as
a suspicious level of activity. The second chart shows the bot’s last 2,955 tweets. It was routinely
blasting out a suspicious number of tweets, hitting 584 in one day. Then, it seems to have stopped
abruptly. Source: _BuzzFeed News_ .


Social sharing has made it possible for any kind of content to potentially be
seen not just by a few hundred but by millions of people without expensive
marketing campaigns or TV air time purchases.
But what that means is that many people have also found ways to game
algorithms with fake or purchased followers as well as (semi-)automated
accounts like bots and cyborgs (Vo, 2017a).


Bots are not evil from the get-go: There are plenty of bots that may delight
us with their whimsical haikus or self-care tips. But as Atlantic Council
fellow Ben Nimmo, who has researched bot armies for years, told me for a
_BuzzFeed_ story: “[Bots] have the potential to seriously distort any debate. .
. . They can make a group of six people look like a group of 46,000 people.”
The social media platforms themselves are at a pivotal point in their
existence where they have to recognize their responsibility in defining
and clamping down on what they may deem a “problematic bot.” In the
meantime, journalists should recognize the ever-growing presence of nonhumans and their power online.
For one explanatory piece about automated accounts we wanted to
compare tweets from a human to those from a bot (Vo, 2017b). While there’s
no sure-fire way to really determine whether an account is operated through
a coding script and thus is not a human, there are ways to look at different
traits of a user to see whether their behaviour may be suspicious. One of
the characteristics we decided to look at is that of an account’s activity.
For this we compared the activity of a real person with that of a bot.
During its busiest hour on its busiest day the bot we examined tweeted
more than 200 times. Its human counterpart only tweeted 21 times.


**How to Harvest Social Data**


There are broadly three different ways to harvest data from the social web:
APIs, personal archives and scraping.
The kind of data that official channels like API data streams provide
is very limited. Despite harbouring warehouses of data on consumers’
behaviour, social media companies only provide a sliver of it through
their APIs. For Facebook, researchers were once able to get data for public
pages and groups but are no longer able to mine that kind of data after
the company implemented restrictions on the availability of this data in
response to the Cambridge Analytica scandal. For Twitter, this access is
often restricted to a set number of tweets from a user’s timeline or to a set
time frame for search.
Then there are limitations on the kind of data users can request of their
own online persona and behaviour. Some services like Facebook or Twitter
will allow users to download a history of the data that constitutes their
online selves—their posts, their messaging, or their profile photos—but that
data archive won’t always include everything each social media company
has on them either.


For instance, users can only see what ads they’ve clicked on going three
months back, making it really hard for them to see whether they may or
may not have clicked on a Russia-sponsored post.
Last but not least, extracting social media data from the platforms
through scraping is often against the terms of service. Scraping a social
media platform can get users booted from a service and potentially even
result in a lawsuit ( _Facebook, Inc. v. Power Ventures, Inc._, 2016).
For social media platforms, suing scrapers may make financial sense. A
lot of the information that social media platforms gather about their users
is for sale—not directly, but companies and advertisers can profit from it
through ads and marketing. Competitors could scrape information from
Facebook to build a comparable platform, for instance. But lawsuits may
inadvertently deter not just economically motivated data scrapers but also
academics and journalists who want to gather information from social
media platforms for research purposes.
This means that journalists may need to be more creative in how they
report and tell these stories. Journalists may want to buy bots to better
understand how they act online, or reporters may want to purchase Facebook
ads to get a better understanding of how Facebook works (Angwin et al.,
2017).
Whatever the means, operating within and outside of the confines set
by social media companies will be a major challenge for journalists as they
are navigating this ever-changing cyber environment.


**What Social Media Data Is** _**Not**_ **Good For**


It seems imperative to better understand the universe of social data also
from a standpoint of its caveats.


**Understanding Who** _**Is**_ **and Who** _**Is Not**_ **Using Social Media**


One of the biggest issues with social media data is that we cannot assume
that the people we hear on Twitter or Facebook are representative samples
of broader populations offline.
While there are a large number of people who have a Facebook or Twitter
account, journalists should be wary of thinking that the opinions expressed
online are those of the general population. As a Pew study from 2018 illustrates, usage of social media varies from platform to platform (Smith


& Anderson, 2018). While more than two thirds of US adults online use
YouTube and Facebook, less than a quarter use Twitter. This kind of data
can be much more powerful for a concrete and specific story, whether it
is examining the hate speech spread by specific politicians in Myanmar
or examining the type of coverage published by conspiracy publication
_Infowars_ over time.


**Not Every User Represents One Real Human Being**


In addition to that, not every user necessarily represents a person. There
are automated accounts (bots) and accounts that are semi-automated and
semi-human controlled (cyborgs). And there are also users who operate
multiple accounts.
Again, understanding that there’s a multitude of actors out there manipulating the flow of information for economic or political gain is an important
aspect to keep in mind when looking at social media data in bulk (although
this subject in itself—media and information manipulation—has become
a major story in its own right that journalists have been trying to tell in
ever more sophisticated ways).


**The Tyranny of the Loudest**


Last but not least it’s important to recognize that not everything or
everyone’s behaviour is measured. A vast amount of people often choose
to remain silent. And as more moderate voices are recorded less, it is only
the extreme reactions that are recorded and fed back into algorithms
that disproportionately amplify the already existing prominence of the
loudest.
What this means is that the content that Facebook, Twitter and other
platforms algorithmically surface on our social feeds is often based on
the likes, retweets and comments of those who chose to chime in. Those
who did not speak up are disproportionately drowned out in this process.
Therefore, we need to be as mindful of what is not measured as we are of
what is measured and how information is ranked and surfaced as a result
of these measured and unmeasured data points.


**Works Cited**


Angwin, J., Varner, M., & Tobin, A. (2017, September 14). Facebook enabled advertisers to reach “Jew haters.” _ProPublica_ . https://www.propublica.org/article/
facebook-enabled-advertisers-to-reach-jew-haters
_Facebook, Inc. v. Power Ventures, Inc._, No. 13-17102 (United States Ninth Circuit
July 12, 2016). https://caselaw.findlaw.com/summary/opinion/us-9thcircuit/2016/07/12/276979.html
Rudder, C. (2014). _Dataclysm: Who we are (When we think no one’s looking)_ . Fourth
Estate.
Smith, A., & Anderson, M. (2018, March 1). _Social media use 2018: Demograph-_
_ics and statistics_ . Pew Research Center. https://www.pewresearch.org/
internet/2018/03/01/social-media-use-in-2018/
Tucker, P. (2013, May 7). Has big data made anonymity impossible? _MIT Tech-_
_nology Review_ . https://www.technologyreview.com/2013/05/07/178542/
has-big-data-made-anonymity-impossible/
Vo, L. T. (2015, June 3). The umbrella network. _Al Jazeera America_ . http://projects.
aljazeera.com/2015/04/loving-long-distance/hong-kong-umbrella-protest.html
Vo, L. T. (2016). The primary source in the age of mechanical multiplication. _Nieman_
_Lab_ . https://www.niemanlab.org/2016/12/the-primary-source-in-the-age-ofmechanical-multiplication/
Vo, L. T. (2017a, October 11). Twitter bots are trying to influence you. These six
charts show you how to spot one. _BuzzFeed News_ . https://www.buzzfeednews.
com/article/lamvo/twitter-bots-v-human
Vo, L. T. (2017b, October 20). Here’s what we learned from staring at social
media data for a year. _BuzzFeed_ . https://www.buzzfeed.com/lamvo/
heres-what-we-learned-from-staring-at-social-media-data-for
Vo, L. T. (2017c, October 20). What we learned from staring at social media data
for a year. _Source_ . https://source.opennews.org/articles/what-buzzfeed-newslearned-after-year-mining-data-/


**About the Author**


**Lam Thuy Vo** is a senior data reporter at _BuzzFeed News_ and author of
_Mining Social Media: Finding Stories in Internet Data_ (No Starch Press, 2019),
a Python book.


##### **33. Digital Forensics: Repurposing Google** **Analytics IDs**

_Richard Rogers_


**Abstract**
This chapter describes a network discovery technique on the basis of
websites sharing the same Google Analytics and/or AdSense IDs.


**Keywords:** digital methods, digital forensics, anonymous sources, network
mapping, Google Analytics, data journalism


When an investigative journalist uncovered a covert network of Russian
websites in July 2015 furnishing disinformation about Ukraine, not only
did this revelation portend the state-sponsored influence campaigning
prior to the 2016 US presidential elections, [1] it also popularized a network
discovery technique for data journalists and social researchers (Alexander,
2015). Which websites share the same Google Analytics ID (see Figure 33.1)?
If the websites share the same ID, it follows that they are operated by the
same registrant, be it an individual, organization or media group. The
journalist, Lawrence Alexander, was prompted in his work by the lack of a
source behind emaidan.com.ua, a website that appears to give information
about the Euromaidan protests in 2013–2014 in Ukraine that ultimately
upended the pro-Russian Ukrainian president in favour of a pro-Western
one. In search of the source, and “intrigued by its anonymity,” Alexander
(2015) dug into the website code.


1 A longer version of this chapter is available in Rogers, R. (2019). _Doing digital methods_ .
SAGE. The author would like to acknowledge the groundwork by Mischa Szpirt. For more on
this approach, see Rogers, R. (2019). _Doing digital methods_ . SAGE (Chapter 11), and Bounegru,
L., Gray, J., Venturini, T., & Mauri, M. (Comp.) (2017). _A field guide to “fake news”: A collection of_
_recipes for those who love to cook with digital methods_ . Public Data Lab (Chapter 3).


Bounegru, L. and J. Gray (eds.), _The Data Journalism Handbook:_ _Towards a Critical Data Practice_ .
Amsterdam: Amsterdam University Press, 2021
doi 10.5117/9789462989511_ch33


Figure 33.1. Website network discovered through (shared) Google Analytics IDs. Source: Alexander,
L. (2015, July 13). Open-source information reveals pro-Kremlin web campaign. Global Voices. https://globalvoices.org/2015/07/13/open-source-information-reveals-pro-kremlin-web-campaign/


Viewing the source code of the web page, he found a Google Analytics
ID, which he inserted into reverse lookup software that furnishes a list of
other websites using the same ID. [2] He found a (star-shaped) network of a
Google Analytics ID linked to eight other websites (in Figure 33.1 at the
top of the diagram), sharing a similar anti-Ukraine narrative. One of those
websites also used an additional Google Analytics ID, which led to another
cluster of related websites (in Figure 33.1 at the bottom to the right), also of
similar political persuasion. Examining the WHOIS records of several of


2 The lookup may also yield each website’s IP address, Google AdSense ID, WHOIS domain
record and other telling information.


Figure 33.2. Google Analytics ID. Source: Baio, A. (2011, November 15). Think you can hide,
anonymous blogger? Two words: Google analytics. Wired. https://www.wired.com/2011/11/
goog-analytics-anony-bloggers/


these domains, he found an associated email address, and subsequently a
person’s profile and photo on VKontakte, the Russian social networking site.
The name of this person he then found on a leaked list of employees from
the Internet Research Agency in St Petersburg, known as the workplace of
the Russian government-sponsored “troll army” (Chen, 2015; Toler, 2015).
Drawing links between data points, Alexander put a name and face on a
so-called Russian troll. He also humanized the troll, somewhat, by pointing
to his Pinterest hobby page, where there is posted a picture of Russian space
achievements. The troll is a Cosmonaut space fan, too.
Employing so-called “open-source intelligence” (OSINT) tools as discovery
techniques (and also digital methods in the sense of repurposing Google
Analytics and reverse lookup software), Alexander and other journalists
make and follow links in code, public records, databases and leaks, piecing it
all together for an account of “who’s behind” particular operations (Bazzell,
2016). “Discovery” is an investigative or even digital forensics approach for
journalistic mining and exposure, where one would identify and subsequently
strive to contact the individual, organization or media group to interview
them, and grant them an opportunity to account for their work. [3] The dual
accountings—the journalist’s discovery and the discovered’s explanation—constitute the story to be told. The purpose is to make things public,
to wring out of the hairy code of websites the covert political work being
undertaken, and have this particular proof be acknowledged (Latour, 2005).
Google Analytics ID detective work has a lineage in the practice of unmasking anonymous online actors through exploits, or entry points to personally


3 Digital forensics has its roots in the investigation of corporate fraud through techniques
such as “data carving,” which enable the retrieval of deleted files.


Figure 33.3. Embedded digital objects on websites, depicted as network diagram. Source:
Alexander, L. (2015, July 13). Open-source information reveals pro-Kremlin web campaign. Global
Voices. https://globalvoices.org/2015/07/13/open-source-information-reveals-pro-kremlin-webcampaign/.


identifiable data that have not been foreseen by its creators. Mining Google
Analytics IDs for network discovery and mapping is also a repurposing
exercise, using the software in unintended fashion for social research. The
originator of the technique, Andy Baio, a journalist at _Wired_ magazine, tells
the story of an anonymous blogger posting highly offensive material, who had
covered his tracks in the “usual ways”: “hiding personal info in the domain
record, using a different IP address from his other sites, and scrubbing any
shared resources from his WordPress install” (Baio, 2011). Baio ID’d him
because the blogger shared a Google Analytics ID with other websites he
operated in full view. The cautionary tale about this discovery and unmasking
technique concludes with Baio providing a safety guide for other anonymous
bloggers _with a just cause_, such as those monitoring Mexican drug cartels,
whose discovery could lead to danger or even loss of life. Here one also could
test the robustness of the anonymity, and inform the journalists working
undercover online of any vulnerabilities or potential exploits.
By way of conclusion, I offer a research protocol for network discovery
using Google Analytics IDs, summarized in the list below:


Curate a list of websites that do not provide their sources.
Locate Google Analytics and AdSense IDs.


Insert URL list into reverse lookup software such as dnslytics.com.
Seek websites that share the same IDs.
Thematically group and characterize the websites sharing IDs.
Consider network visualization using Gephi.


**Works Cited**


Alexander, L. (2015, July 13). Open-source information reveals pro-Kremlin
web campaign. _Global Voices_ . https://globalvoices.org/2015/07/13/
open-source-information-reveals-pro-kremlin-web-campaign/
Baio, A. (2011, November 15). Think you can hide, anonymous blogger?
Two words: Google analytics. _Wired_ . https://www.wired.com/2011/11/
goog-analytics-anony-bloggers/
Bazzell, M. (2016). _Open source intelligence techniques: Resources for searching and_
_analyzing online information_ (5th ed.). CreateSpace Independent Publishing
Platform.
Chen, A. (2015, June 2). The agency. _The New York Times Magazine_ . https://www.
nytimes.com/2015/06/07/magazine/the-agency.html
Latour, B. (2005). From realpolitik to dingpolitik—An introduction to making
things public. In B. Latour & P. Weibel (Eds.), _Making things public: Atmospheres_
_of democracy_ (pp. 14–41). MIT Press. http://www.bruno-latour.fr/node/208.html
Toler, A. (2015, March 14). Inside the Kremlin troll army machine: Templates,
guidelines, and paid posts. _Global Voices_ . https://globalvoices.org/2015/03/14/
russia-kremlin-troll-army-examples/


**About the Author**


**Richard Rogers** is Professor of New Media and Digital Culture in Media
Studies at the University of Amsterdam and director of the Digital Methods
Initiative as well as the Netherlands Research School for Media Studies.


