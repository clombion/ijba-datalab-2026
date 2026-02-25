<!-- chunk: 1/4 | source: 33-data-journalism-wells.md | words: 10406 -->
<!-- headings: Introduction {number="1"}; 1.1 Modern data journalism {number="1.1"}; 1.2 Installations {number="1.2"}; 1.3 About this book {number="1.3"}; 1.4 What we'll cover {number="1.4"}; Public records {number="2"}; 2.1 Federal law {number="2.1"}; 2.2 State law {number="2.2"}; R basics {number="3"}; 3.1 About libraries {number="3.1"}; Data journalism in the age of replication {number="4"}; 4.1 The stylebook {number="4.1"}; 4.2 Replication {number="4.2"}; 4.3 Goodbye Excel? {number="4.3"}; 4.4 "Receptivity ... is high" {number="4.4"}; 4.5 Replication in notebooks {number="4.5"}; Data, structures and types {number="5"}; 5.1 A Mental Picture {number="5.1"}; 5.2 Types {number="5.2"}; Aggregates {number="6"} -->

#  Introduction {number="1"}

If you were at all paying attention in pre-college science classes, you have probably seen this equation:

    d = rt or distance = rate*time

In English, that says we can know how far something has traveled if we know how fast it's going and for how long. If we multiply the rate by the time, we'll get the distance.

If you remember just a bit about algebra, you know we can move these things around. If we know two of them, we can figure out the third. So, for instance, if we know the distance and we know the time, we can use algebra to divide the distance by the time to get the rate.

    d/t = r or distance/time = rate

In 2012, the South Florida Sun Sentinel found a story in this formula.

People were dying on South Florida tollways in terrible car accidents. What made these different from other car fatal car accidents that happen every day in the US? Police officers driving way too fast were causing them.

But do police regularly speed on tollways or were there just a few random and fatal exceptions?

Thanks to Florida's public records laws, the Sun Sentinel got records from the toll transponders in police cars in south Florida. The transponders recorded when a car went through a given place. And then it would do it again. And again.

Given that those places are fixed -- they're toll plazas -- and they had the time it took to go from one toll plaza to another, they had the distance and the time.

[It took high school algebra to find how fast police officers were driving. And the results were shocking.](http://www.sun-sentinel.com/news/local/speeding-cops/fl-speeding-cops-20120211,0,3706919.story)

Twenty percent of police officers had exceeded 90 miles per hour on toll roads. In a 13-month period, officers drove between 90 and 110 mph more than 5,000 times. And these were just instances found on toll roads. Not all roads have tolls.

The story was a stunning find, and the newspaper documented case after case of police officers violating the law and escaping punishment. And, in 2013, they won the Pulitzer Prize for Public Service.

All with simple high school algebra.

## 1.1 Modern data journalism {number="1.1"}

It's a single word in a single job description, but a Buzzfeed job posting in 2017 is another indicator in what could be a profound shift in how data journalism is both practiced and taught.

"We're looking for someone with a passion for news and a commitment to using data to find amazing, important stories --- both quick hits and deeper analyses that drive conversations," the posting seeking a data journalist says. It goes on to list five things BuzzFeed is looking for: Excellent collaborator, clear writer, deep statistical understanding, knowledge of obtaining and restructuring data.

And then there's this:

**"You should have a strong command of at least one toolset that (a) allows for filtering, joining, pivoting, and aggregating tabular data, and (b) enables reproducible workflows."**

This is not the data journalism of 20 years ago. When it started, it was a small group of people in newsrooms using spreadsheets and databases. Data journalism now encompases programming for all kinds of purposes, product development, user interface design, data visualization and graphics on top of more traditional skills like analyzing data and writing stories.

In this book, you'll get a taste of modern data journalism through programming in R, a statistics language. You'll be challenged to think programmatically while thinking about a story you can tell to readers in a way that they'll want to read. They might seem like two different sides of the brain -- mutually exclusive skills. They aren't. I'm confident you'll see programming is a creative endeavor and storytelling can be analytical.

Combining them together has the power to change policy, expose injustice and deeply inform.

## 1.2 Installations {number="1.2"}

This book is all in the R statistical language. To follow along, you'll do the following:

1.  Install the R language on your computer. Go to the [R Project website](https://www.r-project.org/), click download R and select a mirror closest to your location. Then download the version for your computer.

2.  Install [R Studio Desktop](https://www.rstudio.com/products/rstudio/#Desktop). The free version is great.

Going forward, you'll see passages like this:

``` 
install.packages("tidyverse")
```

That is code that you'll need to run in your R Studio. When you see that, you'll know what to do.

## 1.3 About this book {number="1.3"}

This book is the collection of class materials originally written for Matt Waite's Data Journalism class at the University of Nebraska-Lincoln's College of Journalism and Mass Communications. It has been substantially updated by Derek Willis and Sean Mussenden for data journalism classes at the University of Maryland Philip Merrill College of Journalism.

There's some things you should know about it:

- It is free for students.
- The topics will remain the same but the text is going to be constantly tinkered with.
- What is the work of the author is copyright Matt Waite 2020.
- The text is [Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/) Creative Commons licensed. That means you can share it and change it, but only if you share your changes with the same license and it cannot be used for commercial purposes. I'm not making money on this so you can't either.\
- As such, the whole book -- authored in Bookdown -- in its original form is [open sourced on Github](https://github.com/mattwaite/datajournalismbook). Pull requests welcomed!

## 1.4 What we'll cover {number="1.4"}

- Public records and open data
- R Basics
- Replication
- Data basics and structures
- Aggregates
- Mutating
- Working with dates
- Filters
- Cleaning I: Data smells
- Cleaning II: Janitor
- Cleaning III: Open Refine
- Cleaning IV: Pulling Data from PDFs
- Joins
- Basic data scraping
- Intermediate data scraping
- Getting data from APIs: Census
- Visualizing for reporting: Basics
- Visualizing for reporting: Publishing
- Geographic data basics
- Geographic queries
- Geographic visualization
- Text analysis basics
- Text analysis
- Advanced analysis: Correlations and regressions
- Advanced analysis: Logistic regression
- Writing with and about data
- Data journalism ethics

`<!--chapter:end:index.Rmd-->`{=html}


#  Public records {number="2"}

Public records are the lifeblood of investigative reporting. They carry their own philosophical framework, in a manner of speaking.

- Sunlight is the best disinfectant. Corruption hides in the shadows.
- You paid for it with your taxes. It should be yours (with exceptions).
- Journalism with a capital J is about holding the powerful accountable for their actions.

Keeping those things in mind as you navigate public records is helpful.

## 2.1 Federal law {number="2.1"}

Your access to public records and public meetings is a matter of the law. As a journalist, it is your job to know this law better than most lawyers. Which law applies depends on which branch of government you are asking. In addition to documents and other kinds of information, FOIA also provides access to structured datasets of the kind we'll use in this class.

The Federal Government is covered by the Freedom of Information Act, or FOIA. FOIA is not a universal term. Do not use it if you are not talking to a federal agency. FOIA is a beacon of openness to the world. FOIA is deeply flawed and frustrating.

Why?

- There is no real timetable with FOIA. Requests can take months, even years.
- As a journalist, you can ask that your request be expedited.
- Guess what? That requires review. More delays.
- Exemptions are broad. National security, personal privacy, often overused.
- Denied? You can appeal. More delays.

The law was enacted in 1966, but it's still poorly understood by most federal employees, if not outright flouted by political appointees. Lawsuits are common.

Post 9/11, the Bush administration rolled back many agency rules. Obama ordered a "presumption of openness" but followed it with some of the most restrictive policies ever seen. The Trump Administration, similar to the Obama administration, claims to be the most transparent administration, but has steadily removed records from open access and broadly denied access to records.

Result? FOIA is in trouble.

[SPJ is a good resource](https://www.spj.org/foi-guide-pros.asp).

## 2.2 State law {number="2.2"}

States are -- generally -- more open than the federal government. The distance between the government and the governed is smaller. Some states, like Florida and Texas, are very open. Others, like Virginia and Pennsylvania, are not. Maryland is somewhere in the middle.

These laws generally give you license to view -- and obtain a copy of -- a record held by a state or local government agency.

What is a public record? Generally speaking, public records are information stored on paper or in an electronic format held by a state or local government agency, but each state has its own list of types of records -- called "exemptions" -- that are not subject to disclosure.

If a record has both exempt and non-exempt information mixed in, most states require an agency to disclose it after removing the exempt information, a process called "redaction." Agencies aren't required to create a record in order to fill your request.

In some states but not all -- the public information law (or related case law) explicitly dictates that extracting a slice of a database doesn't constitute creation of a record. Most states can charge you a reasonable fee for time spent retrieving or copying records, though many have provisions to waive those fees for journalists. Every state law operates on a different timeline. Some only require agencies respond in a "reasonable" time, but others spell out exactly how fast an agency must respond to you, and how fast they must turn over the record.

[The Reporters Committee For Freedom of the Press](https://www.rcfp.org/open-government-guide/) has a good resource for learning the law in your state.

Please and thank you will get you more records than any lawyer or well-written request. Be nice. Be polite. And be persistent. Following up regularly to check on status of a request lets an agency know they can't ignore you (and some will try). Hunting for records is like any other kind of reporting -- you have to do research. You have to ask questions. Ask them: What records do you keep? For how long?

When requesting data, you are going to scare the press office and you are going to confuse the agency lawyer. Request to have their data person on the phone.

A good source of info? Records retention schedules, often required by law or administrative rule at an agency. Here's an example from [Nebraska](http://www.sos.ne.gov/records-management/retention_schedules.html).

`<!--chapter:end:01-publicrecords.Rmd-->`{=html}



#  R basics {number="3"}

[R](https://www.r-project.org/about.html) is a programming language, one specifically geared toward data analysis.

Like all programming languages, it has certain built-in functions.

There are many ways you can write and execute R code. The first, and most basic, is the console, shown here as part of a software tool called [RStudio (Desktop Open Source Edition)](https://www.rstudio.com/products/rstudio/) that we'll be using all semester.


Think of the console like talking directly to the R language engine that's busy working inside your computer. You use it send R commands, making sure to use the only language it understands, which is R. The R language engine processes those commands, and sends information back to you.

Using the console is direct, but it has some drawbacks and some quirks we'll get into later. Let's examine a basic example of how the console works.

If you load up R Studio, type 2+2 into the console and hit enter it will spit out the number 4, as displayed below.

``` 
2+2
```

    ## [1] 4

It's not very complex, and you knew the answer before hand, but you get the idea. With R, we can compute things.

We can also store things for later use under a specific name. In programming languages, these are called **variables**. We can assign things to variables using this left-facing arrow: `<-`. The `<-` is a called an **assignment operator**.

If you load up R studio and type this code in the console...

``` 
number <- 2
```

...and then type this code, it will spit out the number 4, as show below.

``` 
number * number
```

    ## [1] 4

We can have as many variables as we can name. We can even reuse them (but be careful you know you're doing that or you'll introduce errors).

If you load up R studio and type this code in the console...

``` 
firstnumber <- 1
secondnumber <- 2 
```

...and then type this, it will split out the number 6, as shown below.

``` 
(firstnumber + secondnumber) * secondnumber
```

    ## [1] 6

We can store anything in a variable. A whole table. A list of numbers. A single word. A whole book. All the books of the 18th century. Variables are really powerful. We'll explore them at length.

A quick note about the console: After this brief introduction, we won't spend much time in R Studio actually writing code directly into the console. Instead, we'll write code in fancied-up text files -- interchangably called R Markdown or R Notebooks -- as will be explained in the next chapter. But that code we write in those text files will still *execute* in the console, so it's good to know how it works.

## 3.1 About libraries {number="3.1"}

The real strength of any programming language is the external libraries (often called "packages") that power it. The base language can do a lot, but it's the external libraries that solve many specific problems -- even making the base language easier to use.

With R, there are hundreds of free, useful libraries that make it easier to do data journalism, created by a community of thousands of R users in multiple fields who contribute to open-source coding projects.

For this class, we'll make use of several external libraries.

Most of them are part of a collection of libraries bundled into one "metapackage" called the [Tidyverse](https://www.tidyverse.org/packages/) that streamlines tasks like:

- Loading data into R. (We'll use the [readr](https://readr.tidyverse.org/) Tidyverse library)
- Cleaning and reshaping the data before analysis. (We'll use the the [tidyr](https://tidyr.tidyverse.org/index.html) and [dplyr](https://dplyr.tidyverse.org/) Tidyverse libraries)
- Data analysis. (We'll use the [dplyr](https://dplyr.tidyverse.org/) Tidyverse library)
- Data visualization (We'll use the [ggplot2](https://ggplot2.tidyverse.org/) Tidyverse library)

To install packages, we use the function `install.packages()`.

You only need to install a library once, the first time you set up a new computer to do data journalism work. You never need to install it again, unless you want to update to a newer version of the package.

To install all of the Tidyverse libraries at once, the function is `install.packages('tidyverse')`. You can type it directly in the console.

To use the R Markdown files mentioned earlier, we also need to install a Tidyverse-related library that doesn't load as part of the core Tidyverse package. The package is called, conveniently, [rmarkdown](https://rmarkdown.rstudio.com/docs/). The code to install that is `install.packages('rmarkdown')`

`<!--chapter:end:02-basics.Rmd-->`{=html}


#  Data journalism in the age of replication {number="4"}

A single word in a single job ad for [Buzzfeed News](https://www.buzzfeednews.com/) posted in 2017 offered an indication of a profound shift in how data journalism is both practiced and taught.

"We're looking for someone with a passion for news and a commitment to using data to find amazing, important stories --- both quick hits and deeper analyses that drive conversations," the posting seeking a data journalist says. It goes on to list five things BuzzFeed is looking for: Excellent collaborator, clear writer, deep statistical understanding, knowledge of obtaining and restructuring data.

And then there's this:

**"You should have a strong command of at least one toolset that (a) allows for filtering, joining, pivoting, and aggregating tabular data, and (b) enables reproducible workflows."**

The word you're seeing more and more of? Reproducible. And it started in earnest in 2017 when data journalism crossed a major threshold in American journalism: It got it's own section in the [Associated Press Stylebook](https://www.apstylebook.com/).

"Data journalism has become a staple of reporting across beats and platforms," the Data Journalism section of the Stylebook opens. "The ability to analyze quantitative information and present conclusions in an engaging and accurate way is no longer the domain of specialists alone."

The AP's Data Journalism section discusses how to request data and in what format, guidelines for scraping data from websites with automation, the ethics of using leaked or hacked data and other topics long part of data journalism conference talks.

But the third page of the section contains perhaps the most profound commandment: **"As a general rule, all assertions in a story based on data analysis should be reproducible. The methodology description in the story or accompanying materials should provide a road map to replicate the analysis."**

Reproducible research -- replication -- is a cornerstone of scientific inquiry. Researchers across a range of academic disciplines use methods to find new knowledge and publish it in peer reviewed journals. And, when it works, other researchers take that knowledge and try it with their own samples in their own locations. Replication studies exist to take something from an "interesting finding" to a "theory" and beyond.

It doesn't always work.

Replication studies aren't funded at nearly the level as new research. And, to the alarm of many, scores of studies can't be replicated by others. Researchers across disciplines are finding that when their original studies are replicated, flaws are found, or the effects found aren't as strong as the original. Because of this, academics across a number of disciplines have written about a replication crisis in their respective fields, particularly psychology, social science and medical research.

In Chapter 1 of the [New Precision Journalism](https://www.amazon.com/New-Precision-Journalism-Midland-Book/dp/0253206642), Phil Meyer wrote that "we journalists would be wrong less often if we adapted to our own use some of the research tools of the social scientists."

Meyer would go on to write about how computers pouring over datasets too large to crunch by hand had changed social science from a discipline with "a few data and a lot of interpretation" into a much more meaningful and powerful area of study. If journalists could become comfortable with data and some basic statistics, they too could harness this power.

"It used to be said that journalism is history in a hurry," Meyer wrote. "The argument of this book is that to cope with the acceleration of social change in today's world, journalism must become social science in a hurry."

He wrote that in 1971. It might as well have been yesterday.

Journalism doesn't have a history of replication, but the concerns about credibility are substantially greater. Trust in media is at an all time low and shows no signs of improving. While the politics of the day have quite a bit to do with this mistrust of media, being more transparent about what journalists do can't hurt.

The AP's commandment that "Thou must replicate your findings" could, if taken seriously by the news business, have substantial impacts on how data journalism gets done in newsrooms and how data journalism gets taught, both at professional conferences and universities.

How? Two ways.

- The predominant way that data journalism gets done in a newsroom is through simple tools like Microsoft Excel or Google Sheets. Those simple tools, on their own, lack significant logging functions that automatically keep track of steps a data journalist took to reach a given conclusion. That means journalists using those tools have to maintain separate, detailed logs of what they did so any analysis can be replicated.
- The predominant way that data journalism gets taught -- both in professional settings and at most universities -- doesn't deal with replication at all. The tools and the training stress "getting things done" -- an entirely logical focus for a deadline driven business. The choices of tools -- like spreadsheet programs -- are made to get from data to story as quick as possible, without frightening away math and tech phobic students.

If the AP's replication rules are to be followed, journalism needs to become much more serious about the tools and techniques used to do data journalism. The days of "point and click" tools to do "quick and dirty" analysis that get published are dying. The days of formal methods using documented steps are here.

## 4.1 The stylebook {number="4.1"}

Troy Thibodeaux, the editor of the AP's data journalism team, said the stylebook entry started when the data team found themselves answering the same questions over and over. With a grant from the Knight Foundation, the team began to document their own standards and turn that into a stylebook section.

From the beginning, they had a fairly clear idea of what they wanted to do -- think through a project and ask what the frequently asked questions are that came up. It was not going to be a soup-to-nuts guide to how to do a data project.

When the section came out, eyebrows went up on the replication parts, surprising Thibodeaux.

"From our perspective, this is a core value for us," he said. "Just for our own benefit, we need to be able to have someone give us a second set of eyes. We benefit from that every day. We catch things for each other."

Thibodeaux said the AP data team has two audiences when it comes to replication -- they have the readers of the work, and members of the collective who may want to do their own work with the data.

"This is something that's essential to the way we work," he said. "And it's important in terms of transparency and credibility going forward. We thought it would be kind of unexceptionable."

## 4.2 Replication {number="4.2"}

Meyer, now 86, said he's delighted to see replication up for discussion now, but warned that we shouldn't take it too far.

"Making the analysis replicable was something I worried about from the very beginning," he wrote in an email. So much so that in 1967, after publishing stories from his landmark survey after the Detroit riots, he shipped the data and backup materials about it to a social science data repository at the University of North Carolina.

And, in doing so, he opened the door to others replicating his results. One scholar attempted to find fault with Meyer's analysis by slicing the data ever thinner until the differences weren't significant -- gaming the analysis to criticize the stories.

Meyer believes replication is vitally important, but doesn't believe it should take on the trappings of science replication, where newsrooms take their own samples or re-survey a community. That would be prohibitively expensive.

But journalists should be sharing their data and analysis steps. And it doesn't need to be complicated, he said.

"Replication is a theoretical standard, not a requirement that every investigator duplicate his or her own work for every project," he said. "Giving enough information in the report to enable another investigator to follow in your footsteps is enough. Just telling enough to make replication possible will build confidence."

But as simple as that sounds, it's not so simple. Ask social scientists.

Andrew Gelman, a professor of statistics and political science and director of the Applied Statistics Center at Columbia University, wrote in the journal CHANCE that difficulties with replication in empirical research are pervasive.

"When an outsider requests data from a published paper, the authors will typically not post or send their data files and code, but instead will point to their sources, so replicators have to figure out exactly what to do from there," Gelman wrote. "End-to-end replicability is not the norm, even among scholars who actively advocate for the principles of open science."

So goes science, so goes journalism.

Until a recent set of exceptions, journalists rarely shared data. The "nerd box" -- a sidebar story that explains how a news organization did what they did -- is a term that first appeared on NICAR-L, a email listserv of data journalists, in the 1990s.

It was a form born in print.

As newsrooms adapted to the internet, some news organizations began linking to their data sources if they were online. Often, the data used in stories were obtained through records requests. Sometimes, reporters created the data themselves.

Journalism, more explicitly than science, is a competitive business. There have been arguments that nerd boxes and downloadable links give too much away to competitors.

Enter the AP Stylebook.

The AP Stylebook argues explicitly for both internal and external replication. Externally, they argue that the **"methodology description in the story or accompanying materials should provide a road map to replicate the analysis"**, meaning someone else could do the replication post publication.

Internally, the AP Stylebook says: **"If at all possible, an editor or another reporter should attempt to reproduce the results of the analysis and confirm all findings before publication."**

There are two problems here.

First is that journalism, unlike science, has no history of replication. There is no "scientific method" for stories. There is no standard "research methods" class taught at every journalism school, at least not where it comes to writing stories. And, beyond that, journalism school isn't a requirement to get into the news business. In other words, journalism lacks the standards other disciplines have.

The second problem is, in many ways, worse: Except for the largest newsrooms, most news organizations lack editors who could replicate the analysis. Many don't have a second person who would know what to do.

Not having a second set of eyes in a newsroom is a problem, Thibodeaux acknowledges. Having a data journalism team "is an incredible luxury" at the AP, he said, and their rule is nothing goes on the wire without a second set of eyes.

Thibodeaux, for his part, wants to see fewer "lone nerds in the corner" -- it's too much pressure. That person gets too much credibility from people who don't understand what they do, and they get too much blame when a mistake is made.

So what would replication look like in a newsroom? What does this mean for how newsrooms do data journalism on deadline?

## 4.3 Goodbye Excel? {number="4.3"}

For decades, Excel has been the gateway drug for data journalists, the Swiss Army knife of data tools, the "One Tool You Can't Live Without." Investigative Reporters and Editors, an organization that trains investigative journalists, have built large amounts of their curricula around Excel. Of the journalism schools that teach data journalism, most of them begin and end with spreadsheets.

The Stylebook says at a minimum, today's data journalists should keep a log that details:

- The source of the data, making sure to work on a copy of the data and not the original file.
- Data dictionaries or any other supporting documentation of the data.
- **"Description of all steps required to transform the data and perform the analysis."**

The trouble with Excel (or Google Sheets) is, unless you are keeping meticulous notes on what steps you are taking, there's no way to keep track. Many data journalists will copy and paste the values of a formula over the formula itself to prevent Excel from fouling up cell references when moving data around -- a practical step that also cuts off another path to being able to replicate the results.

An increasing number of data journalists are switching to tools like analysis notebooks, which use languages like Python and R, to document their work. The notebooks, generally speaking, allow a data journalist to mix code and explanation in the same document.

Combined with online sharing tools like GitHub, analysis notebooks seem to solve the problem of replication. But the number using them is small compared to those using spreadsheets. Recent examples of news organizations using analysis notebooks include the [Los Angeles Times](https://github.com/datadesk), the [New York Times](https://github.com/TheUpshot), [FiveThirtyEight](https://github.com/fivethirtyeight/data), and [Buzzfeed](https://github.com/BuzzFeedNews).

Peter Aldous, a data journalist at Buzzfeed recently published a story about how the online news site used machine learning to [find airplanes being used to spy on people in American cities](https://www.buzzfeednews.com/article/peteraldhous/us-marshals-spy-plane-over-mexico#.qqYnVj0B). Published with the story is the [code Aldous used to build his case](https://github.com/BuzzFeedNews/2017-08-spy-plane-finder).

"I think of it this way: As a journalist, I don't like to simply trust what people tell me. Sometimes sources lie. Sometimes they're just mistaken. So I like to verify what I'm told," he wrote in an email. "By the same token, why should someone reading one of my articles believe my conclusions, if I don't provide the evidence that explains how I reached them?"

The methodology document, associated code and source data took Aldous a few hours to create. The story, from the initial data work through the reporting required to make sense of it all, took a year. Aldous said there wasn't a discussion about if the methodology would be published because it was assumed -- "it's written into our DNA at BuzzFeed News."

"My background is in science journalism, and before that (way back in the 1980s) in science," Aldous said. "In science, there's been a shift from descriptive methods sections to publishing data and analysis code for reproducible research. And I think we're seeing a similar shift in data journalism. Simply saying what you've done is not as powerful as providing the means for others to repeat and build on your work."

Thibodeaux said that what Buzzfeed and others do with analysis notebooks and code repositories that include their data is "lovely."

"That to me is the shining city on the hill," Thibodeaux said. "We're not going to get there, and I don't think we have to for every story and every use case, and I don't think it's necessarily practical for every person working with data to get to that point."

There's a wide spectrum of approaches that still gets journalists to the essence of what the stylebook is trying to do, Thibodeaux said. There are many tools, many strategies, and the AP isn't going to advocate for any single one of them, he said. They're just arguing for transparency and replicability, even if that means doing more work.

"There's a certain burden that comes with transparency," he said. "And I think we have to accept that burden."

The question, Thibodeaux said, is what is sufficient? What's enough transparency? What does someone need for replicability?

"Maybe we do have to set a higher standard -- the more critical the analysis is to the story, and the more complex that analysis is, that's going to push the bar on what is a sufficient methodology statement," he said. "And it could end up being a whole code repo in order to just say, this isn't black magic, here's how we got it if you're so interested."

## 4.4 "Receptivity ... is high" {number="4.4"}

Though written almost half a century ago, Meyer foresaw how data journalism was going to arrive in the newsroom.

"For the new methods to gain currency in journalism, two things must happen," he wrote. "Editors must feel the need strongly enough to develop the in-house capacity for systematic research ... The second need, of course, is for the editors to be able to find the talent to fill this need."

Meyer optimistically wrote that journalism schools were prepared to provide that talent -- they were not then, and only small handful are now -- but students were unlikely to be drawn to these new skills if they didn't see a chance to use those skills in their careers.

It's taken 45 years, but we are now at this point.

"The potential for receptivity, especially among the younger generation of newspaper managers, is high," Meyer wrote.

## 4.5 Replication in notebooks {number="4.5"}

For our purposes in this book, replication requires two things from you, the student: What and why. What is this piece of code doing, and why are you doing that here and now? What lead you to this place? That you can copy and paste code from this book or the internet is not impressive. What is necessary for learning is that you know what a piece of code is doing a thing and why you want to do that thing here.

How will we replicate? We'll make use of special text files -- R Markdown, also known as R Notebooks -- that combine contextual text; the code we use to load, clean, analyze and visualize data; and the output of that code that allowed us to draw certain conclusions to use in stories.

In an R Notebook, there are two blocks: A block that uses markdown, which has no special notation, and a code block. The code blocks can run mulitple languages inside R Studio. There's R, of course, but we could also run Python, a general purpose scripting language; and SQL, or Structured Query Language, the language of databases.

For the rest of the class, we're going to be working in notebooks.

In notebooks, you will both run your code and explain each step, much as I am doing here in this online book. This entire book was produced with R markdown files

To start a notebook in R Studio, you click on the green plus in the top left corner and go down to R Notebook.


In our first lab, we'll go through the process of editing a markdown notebook.

`<!--chapter:end:03-replication.Rmd-->`{=html}



#  Data, structures and types {number="5"}

Data is everywhere. It surrounds you. Every time you use your phone or buy something online, you are creating data that is stored in cloud-computing centers. Modernity is drowning in data, and more comes along all the time. As journalists, it's critical that we learn to work with it.\
In this class we'll deal largely with two kinds of data: **unaggregated data** and **aggregated data**.

Unaggregated data, oversimplifying it a bit, is organized information that represents something tangible that exists in the real world. Aggregated data takes that raw, unaggregated information and summarizes it in some way.

In this class, we'll generally start with unaggregated ["tidy data"](https://tidyr.tidyverse.org/articles/tidy-data.html#defining-tidy-data), that is organized into a grid of rows and columns in tables.

Rows -- which run horizontally and are sometimes called observations or records -- each represent one individual element in a group. Columns -- which run vertically and are also sometimes called variables or fields -- represent features of that group.

To illustrate this, think about how the Metropolitan Police Department collects information about crime incidents in Washington, D.C. in 2021.

Below is an image of an **unaggrgated** information about crime incidents taken from [Washington, D.C.'s open data repository](https://opendata.dc.gov/datasets/crime-incidents-in-2021/explore?location=38.893745%2C-77.019147%2C11.78&showTable=true).


Each row (blue box) represents a single reported crime incident that -- if this data is accurate -- actually happened. Each column (green box), represents some feature of that incident: the date on which occured, the type of crime, where it occurred. The highlighted row in blue represents incident number 21075574 (CCN), an auto theft (OFFENSE) that was reported on June, 7 2021 at 12:02 p.m. (REPORT_DATE) during the day shift (SHIFT) that occured in the 400 Block of M Street (BLOCK). By looking where a given row intersects a given column, we can tell a little story about each incident.

This is unaggregated data. Aggregated data -- also called summary data -- will take raw data and summarize it in some way. For example, a table that counts up all of the assaults, thefts, and homicides would represent aggregated data.

## 5.1 A Mental Picture {number="5.1"}

One of the critical components of data analysis, especially for beginners, is having a mental picture of your data. What does each row represent? What does each column in each row signify? How many rows do you have? How many columns?

All semester, we'll work with a dataset of loans made under the Paycheck Protection Act, a government program that loaned money to businesses during the Covid-19 pandemic with the goal of keeping people employed. In the raw, unaggregated data set we'll work with, each row represents a single loan made to a single company. Each column describes a different feature of that loan: the company's name, the company's location, the industry the company operates in, the lender name, the amount of the loan, and so on.

## 5.2 Types {number="5.2"}

There are scores of data types in the world, and R has them. In this class, we're primarily going to be dealing with data frames, and each element of our data frames will have a data type.

Typically, they'll be one of four types of data:

- Numeric: a number, like the number of car accidents in a year or the number of journalism majors.
- Character: Text, like a name, a county, a state.
- Date: Fully formed dates -- 2019-01-01 -- have a special date type. Elements of a date, like a year (ex. 2019) are not technically dates, so they'll appear as numeric data types.
- Logical: Rare(ish), but every now and then we'll have a data type that's Yes or No, True or False, etc.

Is a zip code a number? Is a jersey number a number?

Trick question, because the answer is no. When we think of data types, numbers are things we do math on. If the thing you want is not something you're going to do math on -- can you add two phone numbers together? -- then make it a character type. If you don't, most every software system on the planet will drop leading zeros. For example, every zip code in Boston starts with 0. If you record that as a number, your zip code will become a four digit number, which isn't a zip code anymore.

When we load data into R, the library we'll use will try to guess the correct data type for each column. Sometimes it gets it right, sometimes it gets it wrong. As we'll see, we change data types during and after loading.

`<!--chapter:end:04-databasics.Rmd-->`{=html}


#  Aggregates {number="6"}

## 6.1 Libraries {number="6.1"}

R is a statistical programming language that is purpose built for data analysis.

Base R does a lot, but there are a mountain of external libraries that do things to make R better/easier/more fully featured. We already installed the tidyverse -- or you should have if you followed the instructions for the last assignment -- which isn't exactly a library, but a collection of libraries. Together, they make up the Tidyverse. Individually, they are extraordinarily useful for what they do. We can load them all at once using the tidyverse name, or we can load them individually. Let's start with individually.

The two libraries we are going to need for this assignment are `readr` and `dplyr`. The library `readr` reads different types of data in. For this assignment, we're going to read in csv data or Comma Separated Values data. That's data that has a comma between each column of data.

Then we're going to use `dplyr` to analyze it.

To use a library, you need to import it. Good practice -- one I'm going to insist on -- is that you put all your library steps at the top of your notebooks.

That code looks like this:

``` 
library(readr)
```

To load them both, you need to do this:

``` 
library(readr)
library(dplyr)
```

    ## 
    ## Attaching package: 'dplyr'

    ## The following objects are masked from 'package:stats':
    ## 
    ##     filter, lag

    ## The following objects are masked from 'package:base':
    ## 
    ##     intersect, setdiff, setequal, union

But, because those two libraries -- and several others that we're going to use over the course of this class -- are so commonly used, there's a shortcut to loading all of the libraries we'll need:

``` 
library(tidyverse)
```

    ## ── Attaching packages ─────────────────────────────────────── tidyverse 1.3.1 ──

    ## ✓ ggplot2 3.3.4     ✓ purrr   0.3.4
    ## ✓ tibble  3.1.2     ✓ stringr 1.4.0
    ## ✓ tidyr   1.1.3     ✓ forcats 0.5.1

    ## ── Conflicts ────────────────────────────────────────── tidyverse_conflicts() ──
    ## x dplyr::filter() masks stats::filter()
    ## x dplyr::lag()    masks stats::lag()

You can keep doing that for as many libraries as you need.

## 6.2 Importing data {number="6.2"}

The first thing we need to do is get some data to work with. We do that by reading it in. In our case, we're going to read a datatable from an "rds" file, which is a format for storing data with R. Later in the course, we'll more frequently work with a format called a CSV. A CSV is a stripped down version of a spreadsheet you might open in a program like Excel, in which each column is separated by a comma. RDS files are less common when getting data from other people. But reading in CSVs is less foolproof than reading in rds files, so for now we'll work with rds.

The rds file we're going to read in is from the \[Small Business Administration's Paycheck Protection Program(<https://www.sba.gov/funding-programs/loans/covid-19-relief-options/paycheck-protection-program>)\]. The program gave loans to businesses to keep people employed during the Covid-19 pandemic. We'll be working with a slice of the data that documents loans to Maryland businesses.

So step 1 is to import the data. The code to import the data looks like this:

`ppp_maryland_loans <- read_rds("ppp_maryland.rds")`

Let's unpack that.

The first part -- **ppp_maryland_loans** -- is the name of a variable.

A **variable** is just a name that we'll use to refer to some more complex thing. In this case, the more complex thing is the data we're importing into R that will be stored as a **dataframe**, which is one way R stores data.

We can call this variable whatever we want. The variable name doesn't matter, technically. We could use any word. You could use your first name, if you like. Generally, though, we want to give variables names that are descriptive of the thing they refer to. Which is why we're calling this one **ppp_maryland_loans**. Variable names, by convention are one word all lower case (or two or more words connected by an underscore). You can end a variable with a number, but you can't start one with a number.

The `<-` bit, you'll recall from the basics, is the **variable assignment operator**. It's how we know we're assigning something to a word. Think of the arrow as saying "Take everything on the right of this arrow and stuff it into the thing on the left." So we're creating an empty vessel called **ppp_maryland_loans** and stuffing all this data into it.

**read_rds()** is a function, one that only works when we've loaded the tidyverse. A **function** is a little bit of computer code that takes in information and follows a series of pre-determined steps and spits it back out. A recipe to make pizza is a kind of function. We might call it **make_pizza()**.

The function does one thing. It takes a preset collection of ingredients -- flour, water, oil, cheese, tomato, salt -- and passes them through each step outlined in a recipe, in order. Things like: mix flour and water and oil, knead, let it sit, roll it out, put tomato sauce and cheese on it, bake it in an oven, then take it out.

The output of our **make pizza()** function is a finished pie.

We'll make use of a lot of pre-written functions from the tidyverse and other packages, and even write some of our own. Back to this line of code:

`ppp_maryland_loans <- read_rds("ppp_maryland.rds")`

Inside of the **read_rds()** function, we've put the name of the file we want to load. Things we put inside of function, to customize what the function does, are called **arguments**.

The easiest thing to do, if you are confused about how to find your data, is to put your data in the same folder as as your notebook (you'll have to save that notebook first). If you do that, then you just need to put the name of the file in there (ppp_maryland.rds). If you put your data in a folder called "data" that sits next to your data notebook, your function would instead look like this:

``` 
ppp_maryland_loans <- read_rds("data/ppp_maryland.rds")
```

In this data set, each row represents a loan application, and each column represents a feature of that loan: who it went to, how much it was for, whether the loan was forgiven.

After loading the data, it's a good idea to get a sense of its shape. What does it look like? There are several ways we can examine it.

By looking in the R Studio environment window, we can see the number of rows (called "obs." which is short for observations), and the number of columns(called variables). We can double click on the dataframe name in the environment window, and explore it like a spreadsheet.

There are several useful functions for getting a sense of the dataset right in our markdown document.

If we run `glimpse(ppp_maryland_loans)`, it will give us a list of the columns, the data type for each column and and the first few values for each column.

``` 
glimpse(ppp_maryland_loans)
```

    ## Rows: 195,856
    ## Columns: 63
    ## $ id                             <dbl> 99443772, 99444241, 99445051, 99445208,…
    ## $ name                           <chr> "TARBIYAH ACADEMY INC", "J &AMP; M DRYW…
    ## $ slug                           <chr> "tarbiyah-academy-inc-8387378410", "j-a…
    ## $ amount                         <dbl> 149000.0, 146000.0, 140400.0, 139527.0,…
    ## $ state                          <chr> "MD", "MD", "MD", "MD", "MD", "MD", "MD…
    ## $ address                        <chr> "6785 Business Pkwy Ste 108", "10413 Fo…
    ## $ city                           <chr> "Elkridge", "Union Bridge", "PHOENIX", …
    ## $ zip                            <chr> "21075-6353", "21791", "21131-2229", "2…
    ## $ naics_code                     <dbl> 611110, 238310, 623110, 311920, 561730,…
    ## $ business_type                  <chr> "Corporation", "Subchapter S Corporatio…
    ## $ race                           <chr> "Asian", "Unanswered", "Unanswered", "U…
    ## $ gender                         <chr> "Male Owned", "Unanswered", "Unanswered…
    ## $ veteran                        <chr> "Non-Veteran", "Unanswered", "Unanswere…
    ## $ non_profit                     <lgl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA,…
    ## $ jobs_retained                  <dbl> 25, 6, 18, 23, 15, 25, 14, 11, 24, 5, 1…
    ## $ date_approved                  <date> 2021-02-13, 2020-05-01, 2020-04-28, 20…
    ## $ lender                         <chr> "Bank of America, National Association"…
    ## $ congressional_district         <chr> "MD-02", "MD-08", "MD-01", "MD-08", "MD…
    ## $ loan_range_sort_key            <lgl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA,…
    ## $ previous_loan_range            <lgl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA,…
    ## $ previous_name                  <lgl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA,…
    ## $ loan_number                    <dbl> 8387378410, 7763877705, 1414477305, 806…
    ## $ sba_office_code                <dbl> 373, 373, 373, 353, 373, 373, 373, 373,…
    ## $ processing_method              <chr> "PPS", "PPP", "PPP", "PPP", "PPS", "PPP…
    ## $ loan_status                    <chr> "Exemption 4", "Exemption 4", "Paid in …
    ## $ term                           <dbl> 60, 24, 24, 24, 24, 24, 60, 60, 24, 60,…
    ## $ sba_guaranty_percentage        <dbl> 100, 100, 100, 100, 100, 100, 100, 100,…
    ## $ initial_approval_amount        <dbl> 149000.0, 146000.0, 140400.0, 139527.0,…
    ## $ current_approval_amount        <dbl> 149000.0, 146000.0, 140400.0, 139527.0,…
    ## $ undisbursed_amount             <dbl> 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, …
    ## $ franchise_name                 <chr> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA,…
    ## $ servicing_lender_location_id   <dbl> 9551, 44449, 124055, 46391, 434059, 304…
    ## $ servicing_lender_name          <chr> "Bank of America, National Association"…
    ## $ servicing_lender_address       <chr> "100 N Tryon St, Ste 170", "222 Delawar…
    ## $ servicing_lender_city          <chr> "CHARLOTTE", "WILMINGTON", "ROCKVILLE",…
    ## $ servicing_lender_state         <chr> "NC", "DE", "MD", "NY", "VA", "MD", "NY…
    ## $ servicing_lender_zip           <chr> "28202-4024", "19801-1621", "20850-6238…
    ## $ rural_urban_indicator          <chr> "U", "U", "U", "U", "R", "R", "R", "U",…
    ## $ hubzone_indicator              <chr> "N", "N", "N", "N", "N", "Y", "Y", "N",…
    ## $ business_age_description       <chr> "Existing or more than 2 years old", "U…
    ## $ project_city                   <chr> "Elkridge", "Union Bridge", "PHOENIX", …
    ## $ project_county_name            <chr> "HOWARD", "CARROLL", "BALTIMORE", "MONT…
    ## $ project_state                  <chr> "MD", "MD", "MD", "MD", "MD", "MD", "MD…
    ## $ project_zip                    <chr> "21075-6353", "21791-0001", "21131-2229…
    ## $ utilities_proceed              <dbl> 1, NA, NA, 3926, 1, NA, 1, NA, NA, NA, …
    ## $ payroll_proceed                <dbl> 148997.0, 146000.0, 140400.0, 88000.0, …
    ## $ mortgage_interest_proceed      <dbl> NA, NA, NA, 0, NA, NA, NA, NA, NA, NA, …
    ## $ rent_proceed                   <dbl> NA, NA, NA, 42062, NA, NA, NA, NA, NA, …
    ## $ refinance_eidl_proceed         <dbl> NA, NA, NA, 0, NA, NA, NA, NA, NA, NA, …
    ## $ health_care_proceed            <dbl> NA, NA, NA, 5539, NA, NA, NA, NA, NA, N…
    ## $ debt_interest_proceed          <dbl> NA, NA, NA, 0, NA, NA, NA, NA, NA, NA, …
    ## $ originating_lender_city        <chr> "CHARLOTTE", "WILMINGTON", "ROCKVILLE",…
    ## $ originating_lender_state       <chr> "NC", "DE", "MD", "NY", "VA", "MD", "VA…
    ## $ loan_status_date               <date> NA, NA, 2021-05-12, 2021-01-22, NA, 20…
    ## $ originating_lender_location_id <dbl> 9551, 44449, 124055, 46391, 434059, 304…
    ## $ old_slug                       <lgl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA,…
    ## $ lmi_indicator                  <chr> "N", "Y", "N", "Y", "N", "Y", "N", "N",…
    ## $ unmatched_original             <lgl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA,…
    ## $ unmatched_updated              <lgl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA,…
    ## $ previous_jobs_reported         <lgl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA,…
    ## $ ethnicity                      <chr> "Not Hispanic or Latino", "Unknown/NotS…
    ## $ forgiveness_amount             <dbl> NA, NA, 141554.40, 140486.49, NA, 13427…
    ## $ forgiveness_date               <date> NA, NA, 2021-02-25, 2020-12-30, NA, 20…

If we type `head(ppp_maryland_loans)`, it will print out the columns and the first six rows of data.

``` 
head(ppp_maryland_loans)
```

    ## # A tibble: 6 x 63
    ##        id name   slug  amount state address city  zip   naics_code business_type
    ##     <dbl> <chr>  <chr>  <dbl> <chr> <chr>   <chr> <chr>      <dbl> <chr>        
    ## 1  9.94e7 TARBI… tarb… 149000 MD    6785 B… Elkr… 2107…     611110 Corporation  
    ## 2  9.94e7 J &AM… j-am… 146000 MD    10413 … Unio… 21791     238310 Subchapter S…
    ## 3  9.94e7 DULAN… dula… 140400 MD    4 Wind… PHOE… 2113…     623110 Corporation  
    ## 4  9.94e7 QUART… quar… 139527 MD    4972 W… Rock… 20852     311920 Corporation  
    ## 5  9.94e7 ORCHA… orch… 133400 MD    1855 W… Owin… 2073…     561730 Subchapter S…
    ## 6  9.94e7 FRUIT… frui… 133000 MD    402 MA… EAST… 2160…     531120 Limited  Lia…
    ## # … with 53 more variables: race <chr>, gender <chr>, veteran <chr>,
    ## #   non_profit <lgl>, jobs_retained <dbl>, date_approved <date>, lender <chr>,
    ## #   congressional_district <chr>, loan_range_sort_key <lgl>,
    ## #   previous_loan_range <lgl>, previous_name <lgl>, loan_number <dbl>,
    ## #   sba_office_code <dbl>, processing_method <chr>, loan_status <chr>,
    ## #   term <dbl>, sba_guaranty_percentage <dbl>, initial_approval_amount <dbl>,
    ## #   current_approval_amount <dbl>, undisbursed_amount <dbl>,
    ## #   franchise_name <chr>, servicing_lender_location_id <dbl>,
    ## #   servicing_lender_name <chr>, servicing_lender_address <chr>,
    ## #   servicing_lender_city <chr>, servicing_lender_state <chr>,
    ## #   servicing_lender_zip <chr>, rural_urban_indicator <chr>,
    ## #   hubzone_indicator <chr>, business_age_description <chr>,
    ## #   project_city <chr>, project_county_name <chr>, project_state <chr>,
    ## #   project_zip <chr>, utilities_proceed <dbl>, payroll_proceed <dbl>,
    ## #   mortgage_interest_proceed <dbl>, rent_proceed <dbl>,
    ## #   refinance_eidl_proceed <dbl>, health_care_proceed <dbl>,
    ## #   debt_interest_proceed <dbl>, originating_lender_city <chr>,
    ## #   originating_lender_state <chr>, loan_status_date <date>,
    ## #   originating_lender_location_id <dbl>, old_slug <lgl>, lmi_indicator <chr>,
    ## #   unmatched_original <lgl>, unmatched_updated <lgl>,
    ## #   previous_jobs_reported <lgl>, ethnicity <chr>, forgiveness_amount <dbl>,
    ## #   forgiveness_date <date>

We can also click on the data name in the R Studio environment window to explore it interactively.

## 6.3 Group by and count {number="6.3"}

So what if we wanted to know how many loans were made in each Maryland county?

To do that by hand, we'd have to take each of the 195,856 individual rows (or observations or records) and sort them into a pile. We'd put them in groups -- one for each county -- and then count them.

`dplyr` has a group by function in it that does just this. A massive amount of data analysis involves grouping like things together and then doing simple things like counting them, or averaging them together. So it's a good place to start.

So to do this, we'll take our dataset and we'll introduce a new operator: `%>%`. The best way to read that operator, in my opinion, is to interpret that as "and then do this."

We're going to establish a pattern that will come up again and again throughout this book: `data %>% function`. In English: take your data set and then do this specific action to it.

The first step of every analysis starts with the data being used. Then we apply functions to the data.

In our case, the pattern that you'll use many, many times is: `data %>% group_by(COLUMN NAME) %>% summarize(VARIABLE NAME = AGGREGATE FUNCTION(COLUMN NAME))`

In our dataset, the column with county information is called "project_county_name"

Here's the code to count the number of loans in each county:

``` 
ppp_maryland_loans %>%
  group_by(project_county_name) %>%
  summarise(
    count_loans = n()
  )
```

    ## # A tibble: 24 x 2
    ##    project_county_name count_loans
    ##    <chr>                     <int>
    ##  1 ALLEGANY                   1293
    ##  2 ANNE ARUNDEL              17336
    ##  3 BALTIMORE                 28789
    ##  4 BALTIMORE CITY            20004
    ##  5 CALVERT                    1870
    ##  6 CAROLINE                    828
    ##  7 CARROLL                    4040
    ##  8 CECIL                      1686
    ##  9 CHARLES                    4398
    ## 10 DORCHESTER                 1082
    ## # … with 14 more rows

So let's walk through that.

We start with our dataset -- `ppp_maryland_loans` -- and then we tell it to group the data by a given field in the data. In this case, we wanted to group together all the counties, signified by the field name `project_county_name`, which you could get from using the glimpse() function. After we group the data, we need to count them up.

In dplyr, we use the `summarize()` function, [which can do alot more than just count things](http://dplyr.tidyverse.org/reference/summarise.html).

Inside the parentheses in summarize, we set up the summaries we want. In this case, we just want a count of the number of loans for each county grouping. The line of code `count_loans = n(),` says create a new field, called `total_loans` and set it equal to `n()`. `n()` is a function that counts the number of rows or records in each group. Why the letter n? The letter n is a common symbol used to denote a count of something. The number of things (or rows or observations or records) in a dataset? Statisticians call it n. There are n number of loans in this dataset.

When we run that, we get a list of counties with a count next to them. But it's not in any order.

So we'll add another "and then do this" symbol -- %\>% -- and use a new function called `arrange()`. Arrange does what you think it does -- it arranges data in order. By default, it's in ascending order -- smallest to largest. But if we want to know the county with the most loans, we need to sort it in descending order. That looks like this:

``` 
ppp_maryland_loans %>%
  group_by(project_county_name) %>%
  summarise(
    count_loans = n()
  ) %>% 
  arrange(desc(count_loans))
```

    ## # A tibble: 24 x 2
    ##    project_county_name count_loans
    ##    <chr>                     <int>
    ##  1 MONTGOMERY                38781
    ##  2 PRINCE GEORGES            34408
    ##  3 BALTIMORE                 28789
    ##  4 BALTIMORE CITY            20004
    ##  5 ANNE ARUNDEL              17336
    ##  6 HOWARD                    12011
    ##  7 FREDERICK                  6666
    ##  8 HARFORD                    6300
    ##  9 CHARLES                    4398
    ## 10 CARROLL                    4040
    ## # … with 14 more rows

Montgomery County has 38,781 loans, more than any other Maryland county.

We can, if we want, group by more than one thing.

The ppp loan data contains a column detailing the race of the business owner: "race." It has six possible values:

- American Indian or Alaska Native
- Asian
- Black or African American
- Native Hawaiian or Other Pacific Islander
- White
- Unanswered

We can group by "project_county_name" and "race" to see how many loans fell in each category in each county. We'll sort alphabetically by county and then race.

``` 
ppp_maryland_loans %>%
  group_by(project_county_name,race) %>%
  summarise(
    count_loans = n()
  ) %>% 
  arrange(project_county_name,race)
```

    ## `summarise()` has grouped output by 'project_county_name'. You can override using the `.groups` argument.

    ## # A tibble: 126 x 3
    ## # Groups:   project_county_name [24]
    ##    project_county_name race                                      count_loans
    ##    <chr>               <chr>                                           <int>
    ##  1 ALLEGANY            American Indian or Alaska Native                    1
    ##  2 ALLEGANY            Asian                                              14
    ##  3 ALLEGANY            Black or African American                          11
    ##  4 ALLEGANY            Unanswered                                       1035
    ##  5 ALLEGANY            White                                             232
    ##  6 ANNE ARUNDEL        American Indian or Alaska Native                   21
    ##  7 ANNE ARUNDEL        Asian                                             544
    ##  8 ANNE ARUNDEL        Black or African American                        1013
    ##  9 ANNE ARUNDEL        Native Hawaiian or Other Pacific Islander          10
    ## 10 ANNE ARUNDEL        Unanswered                                      13894
    ## # … with 116 more rows

As you can see here, it's not clear that we'll be able to make use of the race data going forward. By far the most common category in every county is "Unanswered." We'll avoid grouping by race in the rest of the examples in this chapter.

## 6.4 Other summarization methods: summing, mean, median, min and max {number="6.4"}

In the last example, we grouped like records together and counted them, but there's so much more we can to summarize each group.

Let's say we wanted to know the total dollar amount of loans to each county? For that, we could use the `sum()` function to add up all of the loan values in the column "amount." We put the column we want to total -- "amount" -- inside the sum() function `sum(amount)`. Note that we can simply add a new summarize function here, keeping our count_loans field in our output table.

``` 
ppp_maryland_loans %>%
  group_by(project_county_name) %>%
  summarise(
    count_loans = n(),
    total_loans_amount = sum(amount)
  ) %>% 
  arrange(desc(total_loans_amount))
```

    ## # A tibble: 24 x 3
    ##    project_county_name count_loans total_loans_amount
    ##    <chr>                     <int>              <dbl>
    ##  1 MONTGOMERY                38781        3191350613.
    ##  2 BALTIMORE                 28789        2241954213.
    ##  3 PRINCE GEORGES            34408        1993351125.
    ##  4 ANNE ARUNDEL              17336        1533274782.
    ##  5 BALTIMORE CITY            20004        1454393232.
    ##  6 HOWARD                    12011        1287751670.
    ##  7 FREDERICK                  6666         611545614.
    ##  8 HARFORD                    6300         458507678.
    ##  9 CARROLL                    4040         326178266.
    ## 10 WASHINGTON                 3338         284712867.
    ## # … with 14 more rows

We can also calculate the average size loan in each county -- the mean -- and the loan amount that sits at the midpoint of our data -- the median.

``` 
ppp_maryland_loans %>%
  group_by(project_county_name) %>%
  summarise(
    count_loans = n(),
    total_loans_amount = sum(amount),
    mean_loan_amount = mean(amount),
    median_loan_amount = median(amount)
  ) %>% 
  arrange(desc(mean_loan_amount))
```

    ## # A tibble: 24 x 5
    ##    project_county_name count_loans total_loans_amount mean_loan_amount
    ##    <chr>                     <int>              <dbl>            <dbl>
    ##  1 HOWARD                    12011        1287751670.          107214.
    ##  2 FREDERICK                  6666         611545614.           91741.
    ##  3 ANNE ARUNDEL              17336        1533274782.           88445.
    ##  4 SAINT MARYS                1809         154853058.           85601.
    ##  5 WASHINGTON                 3338         284712867.           85294.
    ##  6 WICOMICO                   2718         228878462.           84208.
    ##  7 ALLEGANY                   1293         107943361.           83483.
    ##  8 MONTGOMERY                38781        3191350613.           82292.
    ##  9 CARROLL                    4040         326178266.           80737.
    ## 10 BALTIMORE                 28789        2241954213.           77875.
    ## # … with 14 more rows, and 1 more variable: median_loan_amount <dbl>

We see something interesting here. The mean loan amount is much higher than the median loan amount in every county. Why? There are some very large loans -- millions of dollars -- skewing the mean higher. Examining both the median -- which is less sensitive to extreme values -- and the mean -- which is more sensitive to extreme values -- gives you a clearer picture of the composition of the data.

Howard County has the highest average loan amount (107,217), while Carroll County has the highest median (\$25,111.00)

What about the highest and lowest loan values in each county? For that, we can use the `min()` and `max()` functions.

``` 
ppp_maryland_loans %>%
  group_by(project_county_name) %>%
  summarise(
    count_loans = n(),
    total_loans_amount = sum(amount),
    mean_loan_amount = mean(amount),
    median_loan_amount = median(amount),
    min_loan_amount = min(amount),
    max_loan_amount = max(amount)
  ) %>% 
  arrange(desc(max_loan_amount))
```

    ## # A tibble: 24 x 7
    ##    project_county_name count_loans total_loans_amount mean_loan_amount
    ##    <chr>                     <int>              <dbl>            <dbl>
    ##  1 ANNE ARUNDEL              17336        1533274782.           88445.
    ##  2 BALTIMORE                 28789        2241954213.           77875.
    ##  3 CARROLL                    4040         326178266.           80737.
    ##  4 GARRETT                    1196          84889005.           70977.
    ##  5 HOWARD                    12011        1287751670.          107214.
    ##  6 MONTGOMERY                38781        3191350613.           82292.
    ##  7 PRINCE GEORGES            34408        1993351125.           57933.
    ##  8 FREDERICK                  6666         611545614.           91741.
    ##  9 BALTIMORE CITY            20004        1454393232.           72705.
    ## 10 CHARLES                    4398         238654940.           54264.
    ## # … with 14 more rows, and 3 more variables: median_loan_amount <dbl>,
    ## #   min_loan_amount <dbl>, max_loan_amount <dbl>

From this, we can see that the largest loan amounts in Anne Arundel County, Baltimore County, Carroll County, Garrett County and Howard County were \$10 million, the maximum loan value authorized under the program.

It would be interesting to see what these companies are that got the maximum of \$10 million. To do that, we could simply take our original data set and sort it from highest to lowest on the loan amount.

``` 
ppp_maryland_loans %>%
  arrange(desc(amount))
```

    ## # A tibble: 195,856 x 63
    ##         id name  slug  amount state address city  zip   naics_code business_type
    ##      <dbl> <chr> <chr>  <dbl> <chr> <chr>   <chr> <chr>      <dbl> <chr>        
    ##  1  9.38e7 GSE … gse-… 1   e7 MD    1332 L… Syke… 21784     333318 Corporation  
    ##  2  9.38e7 GMS … gms-… 1   e7 MD    PO Box… OAKL… 21550     212112 Corporation  
    ##  3  9.38e7 LEME… leme… 1   e7 MD    8184 L… ELKR… 2107…     722513 Subchapter S…
    ##  4  9.38e7 MISS… miss… 1   e7 MD    7750 G… Glen… 21061     722511 Limited  Lia…
    ##  5  9.38e7 PT N… pt-n… 1   e7 MD    501 Fa… Tows… 21286     621340 Limited  Lia…
    ##  6  9.38e7 SMAR… smar… 9.51e6 MD    1997 A… ANNA… 2140…     541611 Limited  Lia…
    ##  7  9.38e7 SILV… silv… 9.50e6 MD    12276 … ROCK… 2085…     722511 Limited  Lia…
    ##  8  9.38e7 D.A.… d-a-… 9.22e6 MD    1330 M… LAUR… 20708     238220 Limited  Lia…
    ##  9  9.38e7 VISI… visi… 9.14e6 MD    530 Mc… Glen… 21061     517311 Subchapter S…
    ## 10  9.38e7 YOUN… youn… 9.11e6 MD    303 W … Balt… 2120…     813410 501(c)3 – No…
    ## # … with 195,846 more rows, and 53 more variables: race <chr>, gender <chr>,
    ## #   veteran <chr>, non_profit <lgl>, jobs_retained <dbl>, date_approved <date>,
    ## #   lender <chr>, congressional_district <chr>, loan_range_sort_key <lgl>,
    ## #   previous_loan_range <lgl>, previous_name <lgl>, loan_number <dbl>,
    ## #   sba_office_code <dbl>, processing_method <chr>, loan_status <chr>,
    ## #   term <dbl>, sba_guaranty_percentage <dbl>, initial_approval_amount <dbl>,
    ## #   current_approval_amount <dbl>, undisbursed_amount <dbl>,
    ## #   franchise_name <chr>, servicing_lender_location_id <dbl>,
    ## #   servicing_lender_name <chr>, servicing_lender_address <chr>,
    ## #   servicing_lender_city <chr>, servicing_lender_state <chr>,
    ## #   servicing_lender_zip <chr>, rural_urban_indicator <chr>,
    ## #   hubzone_indicator <chr>, business_age_description <chr>,
    ## #   project_city <chr>, project_county_name <chr>, project_state <chr>,
    ## #   project_zip <chr>, utilities_proceed <dbl>, payroll_proceed <dbl>,
    ## #   mortgage_interest_proceed <dbl>, rent_proceed <dbl>,
    ## #   refinance_eidl_proceed <dbl>, health_care_proceed <dbl>,
    ## #   debt_interest_proceed <dbl>, originating_lender_city <chr>,
    ## #   originating_lender_state <chr>, loan_status_date <date>,
    ## #   originating_lender_location_id <dbl>, old_slug <lgl>, lmi_indicator <chr>,
    ## #   unmatched_original <lgl>, unmatched_updated <lgl>,
    ## #   previous_jobs_reported <lgl>, ethnicity <chr>, forgiveness_amount <dbl>,
    ## #   forgiveness_date <date>

The first five rows here all represent companies that got \$10 million loans. Who are they? What industries are they in? The answers to these questions could provide a lead for further reporting.

`<!--chapter:end:05-aggregates.Rmd-->`{=html}


