<!-- chunk: 2/2 | source: 24-data-plus-journalism.md | words: 35854 -->
<!-- headings: Queries; Exercise 9; Footnotes; 7 Writing a Data Story; Summary Paragraphs and Making Numbers Relatable; Human-​Centered Reporting: Putting a Face on a Data Story; Seven Common Angles for Data Stories; Writing Data Stories on a Beat; Declutter Your Data Stories; Reporting and Writing for a Broadcast Audience; Writing Exercise; Writing Exercise Example; Footnotes; 8 SQL; Pro Tip ![](images/Pro_Tip_Icon.jpg); Queries; Importing; Exercise 1 ![](images/Exercise_Icon.jpg); Pro Tip ![](images/Pro_Tip_Icon.jpg); Filtering -->

## Queries

Now let's put our formula skills to use with some analysis queries. One of the most important things to understand from this book is that the same tasks can be done in different programs, to different scales, with much of the same language.

The tidyverse package offers many of the same functions you're used to seeing in other contexts, like Select, Filter and Count. Take this simple R function:


    filter(Big.Ten.Covid.Cases, "Confirmed.Cases">100)

As you may have guessed, thanks to your new data skills, this command is telling RStudio to filter the COVID-​19 dataset for rows where there were more than 100 confirmed cases.

There are many options at your fingertips, but we are going to explore one advantage that R has over spreadsheets: the ability to create an entirely new table from a function. This is done by typing the name of a new table, then typing a reverse arrow (\<-​) and then the conditions for the filter.


    high _ case _ days <-​ filter(Big.Ten.Covid.Cases, "Confirmed.
    Cases">100)

Running that command will give us a whole new table called high_case_days. This table should appear in your Environment pane alongside your original table ([Figure 6.11](#ch06.xhtml_f6_11)).


You can then use your new high_case_days table when writing new functions, like this:


    filter(high _ case _ days, "State"=="Illinois”)

Let's try it using our own COVID-19 table.

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 9 

1.  In the Console pane of RStudio, create a filter query that would limit your data to a useful subset. For instance, COVID-​19 cases at a certain university or low case rate universities in a certain state.
2.  Use the commands learned above to create this filter, and assign it to a new table. Give your table a specific name, but do not use spaces.
3.  Press enter to execute this query in the Console. You should see your new filtered table appear in the Environment pane.

</aside>
<aside class="boxed-text2" epub:type="tip" role="doc-tip">

For more data journalism tips, tricks and exercises, visit the Data + Journalism blog at <http://dataplusjournalism.com>

</aside>

\* \* \*

This method -- ​using queries to create entirely new tables -- ​is just a small taste of what R can do. We will explore the powers of programming languages further in [Chapter 9](#ch09.xhtml_c9).

## Footnotes

- Google Sheets [https://www.google.com/sheets/about/](https://www.google.com/)
- Microsoft Excel [https://www.microsoft.com/en-us/microsoft-365/excel](https://www.microsoft.com/)
- SQLServer [https://www.microsoft.com/en-us/sql-server/sql-server-downloads](https://www.microsoft.com/)
- OpenOffice <https://www.openoffice.org/>
- Big Ten Daily COVID-19 shortlink [http://bit.ly/bigtencovid19](http://bit.ly/)
- R <https://www.r-project.org/>
- RStudio Cloud <https://rstudio.cloud/>
- RStudio <https://www.rstudio.com/>
- Tidyverse <https://www.tidyverse.org/>


# 7 Writing a Data Story

Mike Reilley

DOI: [10.4324/9781003273301-8](https://doi.org/10.4324/9781003273301-8){aria-label="D.O.I. link to this document."}

Lise Olsen has worked on more than 100 data-​driven investigative stories in a career that spans more than 30 years. She said she's most proud of stories that have "helped people in one way or another," and her multipart series over the years have changed laws and inspired reforms in three different states.

At the *Houston Chronicle*, Olsen was part of a team that produced "Abuse of Faith," which identified Southern Baptist preachers, missionaries and other workers who had committed sexual assault or other forms of sex abuse. In many cases, the church moved problematic pastors from one church to another, they found, including a missionary who had abused his own children. The team persuaded many victims who'd never given interviews to talk to them and posted their powerful stories online, along with videos. They also created a national database of convicted offenders. In the aftermath, the Southern Baptist Convention was forced to proceed with reforms.

The team opened the six-​part series with a human-​centered approach to a very sensitive story:

> *Thirty-​five years later, Debbie Vasquez's voice trembled as she described her trauma to a group of Southern Baptist leaders.*
>
> *She was 14, she said, when she was first molested by her pastor in Sanger, a tiny prairie town an hour north of Dallas. It was the first of many assaults that Vasquez said destroyed her teenage years and, at 18, left her pregnant by the Southern Baptist pastor, a married man more than a dozen years older.*
>
> *In June 2008, she paid her way to Indianapolis, where she and others asked leaders of the Southern Baptist Convention and its 47,000 churches to track sexual predators and take action against congregations that harbored or concealed abusers. Vasquez, by then in her 40s, implored them to consider prevention policies like those adopted by faiths that include the Catholic Church.*

In Seattle, Olsen and Lewis Kamb solved cold cases as part of a *Seattle Post-​Intelligencer* series that looked into Washington State's missing and unidentified deaths. They built databases from paper records on missing persons from every county in Washington and also researched every unidentified cold case victim statewide at a time when the Green River serial killings remained unsolved. After posting the series online, several long-​unidentified murder victims were identified almost immediately. More than a year later, Olsen got a phone call from Australia that led to the identification of a mother and child murder victim who'd gone unidentified since 1987.

The story again opened with a human-​centered anecdotal lead:

> *KELSO -- ​Jai Prasad's tears mix with the cold drip of the day as he stares at an anonymous patch of ground near the crest of a hilltop in the misty Columbia River Valley.*
>
> *He has no proof, yet. But he believes that before him lies the unmarked grave of his youngest sister, a shy Fiji Islands village girl who came to the United States as an immigrant bride, saw the birth of her first child and then disappeared from a cheap downtown apartment in Eugene, Ore., nearly 20 years ago.*
>
> *He utters her name. Raj Mati. He promises to take her home to Fiji. He pushes down his glasses and wipes away his tears.*
>
> *"It really breaks my heart to leave you here alone," he says.*

In Texas, a data-​driven series Olsen did in 2020 involved analyzing Superfund sites nationwide and showing which were most vulnerable to climate change. The "Super Threats" series, a collaboration with Inside Climate, NBC and *The Texas Observer*, showed that some particularly dangerous sites, based on the Environmental Protection Agency's (EPA) own data, faced ongoing triple threats from flooding, hurricanes and rising sea levels.

The analysis for this series again spawned multiple investigative stories that often led with a human-​centered angle and then moved into the data:

> *BARRETT, Texas -- ​Fred Barrett thought he'd wait out Hurricane Harvey at his home in this town outside Houston, founded by his great-​grandfather in 1889. He prepared for heavy rain, wind and flooding.*
>
> *But when the murky brown San Jacinto River jumped its banks, flooding Barrett's neighbors and an ominous cluster of four hazardous waste Superfund sites nearby, Barrett worried the catastrophic 2017 storm could fill his community with deadly toxins.*
>
> *The most notorious of the sites, the San Jacinto Waste Pits, was smashed by 16 feet of water that undermined a concrete cap covering the site's toxic contents, washing dioxin downriver. A dive team from the Environmental Protection Agency later found the potent human carcinogen in river sediment at 2,300 times the agency's standard for cleanup.*

All three of Olsen's projects had immediate and long-​term impacts -- ​and also illustrate how posting compelling data on the web can yield leads, sources and spin-​off story ideas. That crowdsourcing approach has only become a more powerful tool over the years with the growth of social media.

<aside class="boxed-text2" epub:type="tip" role="doc-tip">

For more data journalism tips, tricks and exercises, visit the Data + Journalism blog at <http://dataplusjournalism.com>

</aside>

Her stories also shared one other common characteristic -- ​crisp, clear writing, combining numbers with a human-​driven focus to show how the data impacted *people*. She and many other data journalists are the first to tell you: Great data stories don't *read* like data stories. They are stories about how issues impact human beings.

In this chapter, you'll explore how to focus your data stories with a human-​centered narrative approach, how to simplify your writing with just a few numbers per paragraph, how to scale the data to make sense to the reader and how to find key data points that can be buried in reports and databases. Earlier chapters explore how to research, scrape, analyze and draw data points from datasets. Now let's see how to turn it into stories that make a difference.

::: section

## Summary Paragraphs and Making Numbers Relatable

In December 2016, the *Charleston (West Virginia) Gazette-​Mail* reporters wrote a series of stories called "Painkiller Profiteers" on the state's rising number of prescription drugs. In the fifth paragraph of the in-​depth story, the reporter, Eric Eyre, wrote a summary paragraph for the ages.

> *In six years, drug wholesalers showered the state with 780 million hydrocodone and oxycodone pills, while 1,728 West Virginia families fatally overdosed on those two painkillers, a Sunday Gazette-​Mail investigation found.*
>
> *The unfettered shipments amount to 433 pain pills for every man, woman and child in West Virginia.*

In two sentences, Eyre encapsulated the issue using three key data points, the last of which he calculated by dividing the 780 million pills by the state's population. More importantly, the 433 pain pills per resident brought the story into a crystal-​clear focus and scaled the issue in an alarming way.

Eyre's approach is also used in sports infographics. For example, when Kansas City Chiefs quarterback Patrick Mahomes signed a 10-​year, \$503 million contract extension -- ​at the time the largest in the National Football League's (NFL) history -- ​ESPN and CBS Sports built digital graphics to help readers better understand just how much \$503 million is.

CBS Sports' infographic based its analysis on his career averages and 17-​game regular-​season schedule. It focused on five key data points with Mahomes' contract:

- \$49,300 per minute
- \$83,500 per attempt
- \$126,700 per completed pass
- \$1.21 million per touchdown pass
- \$2.96 million per game

ESPN's infographic spread the contract out over time:

- \$50.3 million per year average
- \$137,808 per day
- \$5,742 per hour
- \$96 per minute
- \$1.60 per second

Both sets of data help any sports fan getting by on a livable wage relate to the contract. Mahomes makes \$1.60 for taking a breath, and \$5,742 per hour, more than many people make in a month or two. Mahomes makes more than \$49,000 -- ​an annual salary for some -- ​for every *minute* he's on the field.

Helping the reader better understand the data can be a tricky balancing act for reporters, particularly when writing a summary paragraph. As with Eyre's story, a summary paragraph -- ​also known as a "nut graph" as it tells the story in a nutshell -- ​typically appears between paragraphs three to five, depending on the length of the piece. For magazine stories, it can be lower. It typically follows an anecdotal or straight news lead and contains one to three data points spread over two or three sentences.

:::: section
## Human-​Centered Reporting: Putting a Face on a Data Story

Cognitive psychologist Jerome Bruner, quoted by *Forbes* in 2015, said readers are 22 times more likely to remember a fact when it has been wrapped in a story. Why? Because stories are memorable. People relate to them, and they inspire emotions and reactions from the reader. We tell stories every day. We hear them. So put the data into the context of a story, and the reader can better understand.

Adopting a narrative structure, a data story typically starts with an anecdote on the current issue, uses data and other anecdotal support that builds up to the key findings and usually ends with a "call to action" that gives the readers choices at the end of the story: Read a related story, how to get help, comment, answer a poll, etc.

A great example of this approach came in a June 2018 *Arizona Republic* story by Arizona State University student journalists Nate Fain, Daniel Perle and Veronica Graff. They wrote an in-​depth piece about a group of NFL players' lawsuit against the league over its poor handling of ongoing concussions with current and former players. The story used several data points that weren't presented until the summary paragraphs. Instead, the reporters focused the lead on how the concussions affected former Arizona Cardinals players, using those local anecdotes to set the tone for the story:

> *Mark Maddox is left with fragments of what should be his fondest memories: He's lost the details of a family trip to Disney World, and forgotten most of what happened in the three Super Bowls he played in. Sometimes, he watches video of his own games to help jog a memory impaired by too many hits to the head.*
>
> *Tyronne Stowe once anchored the Cardinals' defense. Nowadays, he often forgets where he's going when he's driving on Arizona highways. He forgets that he's babysitting his grandchild. Stowe recently covered the walls of his office with photos to remind himself of his days as a hard-​hitting NFL linebacker who for years went head-​to-​head with opponents -- ​literally.*
>
> *Derek Kennard wears hearing aids, thanks to his history of concussions. He suffers from anxiety attacks when he's in any crowded room and has to leave. Just two years ago, Kennard lost his last job as a guidance counselor at Grand Canyon University because he couldn't remember his duties.*

Once that issue was established, it was time to introduce the data and show how widespread the issue was. How many other players were impacted? How big is the lawsuit? Following the lead were three paragraphs summarizing the broader issue and scale of the suit:

> *To most Americans, even to most football fans, the 2011 lawsuit against the National Football League for concussion-​related injuries is all about numbers -- ​5,000 former players, a \$1 billion initial settlement, scores of lawyers.*
>
> *But for the nine former Cardinals players interviewed for this article, those numbers are irrelevant. What matters most is whether, or when, or how soon memory loss might become dementia, then a death too early for men once idolized for their physical prowess.*
>
> *All told, there are 157 former Cardinals who played for the team since it moved to Arizona in 1988 who are among the 5,000 men who joined in the lawsuit, according to a database analysis of the lawsuit's plaintiffs and all former Cardinals players. Those 157 represent 21 percent of everyone who's played for the team since 1988. Another 109 players from the franchise's days in St. Louis also joined the suit.*

Their story followed a basic structure common in journalism called "The Hero's Journey" ([Figure 7.1](#ch07.xhtml_f7_1)), where the protagonist(s) faces a challenge, goes to resolve it and then returns to normalcy or at least a satisfying end in most cases.


Olsen's aforementioned articles as well as the *Arizona Republic*'s NFL concussions story follow the "Hero's Journey" narrative. For instance, in the NFL story, the heroes are the players suing the league. Their challenges are the fallout from the concussions. We see atonement as they continue on the journey with the lawsuit (which the NFL later settled with the players), and the story is eventually brought back full circle to end with the players. While this is not a "one-​size-​fits-​all" model for writing data stories, it's a common approach for when reporters are trying to show how the issue impacts people while also weaving the data into the story.

There's a running joke among data journalists not to make the reader "numb" with numbers -- ​don't overwhelm them with data. While data can be an interesting way to tell the story, journalism is most often about those being impacted by the data: People. And who's reading the stories? People.

"We connect with those we can relate to," said Andy Boyle, former director of product engineering at the *Chicago Sun-​Times*. 

"It's harder to relate to an opening paragraph showing that a data analysis found 80% of a certain group of people were impacted by something nefarious. But if you instead open it with a *person* who's been impacted by this nefarious thing, as an example of the larger issue, the reader can now connect with this person's struggle."

Boyle's next step: Explain what the data you found shows. Then show more people from this community. Then you explain the choices that were made that led to this situation. And hopefully, you can explain what some of the potential situations are.

Olsen's approach is to tell "human stories above all." Instead of using a lot of numbers, a good reporter will know exactly how to interpret and describe the data, she said. A reporter can use numbers to describe and bolster investigative findings. It's also important for reporters to provide the context and importance (or limitations) of the numbers in clear and compelling explanatory or declarative sentences.

Usually, the fewer numbers you can use, the better. Choose the numbers that will have the most impact, and then use the others in graphics or charts. Use the numbers to write -- ​and to find people and examples that best illustrate the problem. Humans, and how we deal with one another, are almost always the real part of the story, Boyle said.

"Behind most data analyses are human decisions that led to whatever you found," he said. "That's a policy decision. Or it's a lack of enforcement of something. Or people turning a blind eye. Or just deciding they don't give a damn. They may *say* they give a damn, but if the data shows otherwise, who cares what they say?

"When you're writing about something using data, always find people representative of that data. That'll help make your story not only better, but more relatable."

Olsen uses the interviewing data approach to building stories. Ask questions of the data the same you would a source: Who, what, when, where, how and how much. Then use those queries -- ​or the analysis of a spreadsheet -- ​to gain valuable information. Ask the data good questions. Then, let the "responses" and the numbers you get to your questions guide you to make good decisions about whom to interview or who is typical of the trend you're trying to describe and the additional questions to ask.

For example, when Olsen analyzed deaths in oil fields nationwide for the *Houston Chronicle*, she could say with confidence that Texas workers had the highest death rate of any state at the time she did her research -- ​and that the risks seemed to be rising in the drilling boom. She also could say that nationwide, Nabors Drilling had by far the most overall deaths even compared to other large drillers. And because she had done her homework, she could write stories about workers with that important context. Those conclusions -- ​from the data -- ​shaped the stories that she did in that project, Peril in the Oil Patch.

She picked Texas workers and Texas families to profile in writing the story for Houston and Texas audiences. But that's how a California oil worker's allegations of a cover-​up of a nearly fatal accident by Nabors became part of the series -- ​Olsen had the important context that Nabors was the nation's leader in drilling deaths.

<aside class="boxed-text2" epub:type="tip" role="doc-tip">

::: section
### Seven Common Angles for Data Stories 

Paul Bradshaw's Online Journalism Blog outlines seven common angles for data journalism stories. Consider these when you're starting to research a data-​driven story and when you start writing it.

1.  **Scale:** How big is an issue?
2.  **Change/stasis:** This is going up/down/not improving.
3.  **Outliers/ranking:** The best/worst/where we rank on a list.
4.  **Variation:** Postcode lotteries and distributions.
5.  **Exploration:** Tools, simulators, analysis -- ​and art.
6.  **Relationships/debunking:** How are things connected? Or are they not connected? Track networks and flows of power and money.
7.  **Problems and solutions:** Concerns over data, missing data, etc.

</aside>

::::: section

## Writing Data Stories on a Beat

In 2021, Cherone wrote a story for the web and reported for TV a story about City Council committee spending overseen by Alderman Carrie Austin (34th Ward), who was then under indictment.

Cherone's reporting relied on data from Chicago's annual comprehensive financial report, which is a dense 236-​page document. To begin the process, she looked at the actual spending by each of the City Council's 19 committees in 2020 and compared that to what each committee was authorized to spend by the 2020 city budget. Then she compared the actual spending of each committee with the spending by Austin's committee.

That data showed the disparity clearly, which meant she could start talking to committee chairs and other sources, like Mayor Lori Lightfoot and Austin. Eleven days later, Austin resigned as committee chair. The fact that Austin's committee spent so much more than other committees and did so much less than all of them is newsworthy on its own. But the fact that Austin was also under indictment for bribery is the key.

Cherone opened her story with a hard news lead:

> *The Chicago City Council committee led by indicted Ald. Carrie Austin (34th Ward) spent \$191,500 in 2020, while meeting just three times without advancing a single piece of substantive legislation or pressing officials on how the city can do a better job ensuring lucrative contracts can benefit firms owned by women or Black, Latino or Asian Chicagoans.*
>
> *More than 45 days after Austin was indicted on charges of bribery and lying to federal officials, Mayor Lori Lightfoot, who picked Austin to lead the Committee on Contracting Oversight and Equity, has yet to call for Austin to relinquish her position.*

Note that in the lead, Cherone focused on the money -- ​taxpayer dollars -- ​while reporting that the committee rarely met and didn't accomplish much. By doing so, she followed one of her key rules for writing data-​driven stories: Isolate numbers in short, tight sentences and paragraphs. She typically uses just one statistic per sentence and just one or two sentences per paragraph.

"For example, Chicago's police budget is \$1.9 billion, but at one point was \$1.7 billion, so I'm either going to use those two numbers or I'm simply going to calculate the percentage change and what it changed to," she said. "It's essentially the same statistic, but it's just presented in a way that gives people the right context.

"I think what is problematic is if in that one sentence you're saying the police budget went up 3 percent of the city's total budgeted \$16.7 billion, then you're dividing the reader's attention in a sense."

When writing for the web, specifically mobile, a paragraph should never be longer than three sentences in order to maintain clarity and readability on those devices. Spreading the data throughout the story and balancing it with human-​centered anecdotes, quotes and context help increase reader understanding of the issue, Cherone said.

<aside class="boxed-text2" epub:type="tip" role="doc-tip">

::: section
### Declutter Your Data Stories 

Numbers can be messy and hard to read in small type. Here are some ways to declutter your writing by simplifying numbers and presenting them in a concise way:

- 29,912 can be rounded up: Nearly 30,000.
- Round off percentages, too: 62.2 percent is 62 percent; 79.9 percent is 80 percent; 75 percent is three-​fourths or three in four.
- 80 percent of women and 25 percent of men can be one in eight women and one in four men.
- 12.55 Instead of a 100 percent increase, say it doubled. Instead of a 200 percent increase, say it tripled. It's easier for the reader to understand.
- Break data into bullet-​point lists and pullout boxes like this.
- Could the data be better presented in a chart, infographic or database? Does it *need* to be written?

Source: Working Safely with Statistics, presentation by Jennifer LaFleur and Holly Hacker, NICAR 2022 Conference

</aside>

"Many readers' eyes glaze over at the sight of numbers, and they are very likely to stop reading and head over to TikTok and never return," she said. "Talking about a person rather than a percentage can make an issue come alive for readers, and make it clear what is at stake."

John Walton, data journalism editor at BBC News, said one pitfall of data-​driven stories is that reporters assume that the reader loves the data as much as the "nerdy journalist who's spent hours and hours analyzing, cleaning and visualizing it.

"It is also easy for the data journalist to fall into the habit of assuming that the audience knows the subject being written as well as the data journalist does," Walton said. "It's much more likely that they don't, and they are also likely to have a lower tolerance for reading number after number in a news report too."

Use numbers sparingly if you can, it's not always easy, but remember it's your job to digest and simplify your work for the reader, and to communicate it succinctly.

One way to keep readers' interest from figure fatigue is to make the numbers relevant or, to put a face on them. Make the inhuman figures relevant in human terms and the reader is more likely to stay with you.

One of Walton's tricks of the trade: Boil large budget figures down to figures per person. What does the 3 percent city sales tax increase mean to the taxpayers?

"Even better, if you're able to make the data relevant to people by their age, income, location, gender or ethnicity then this is going to have much more impact and relevance to them than a simple national average figure might," he said.

<aside class="boxed-text2" epub:type="tip" role="doc-tip">

::: section
### Reporting and Writing for a Broadcast Audience 

As she did with the Austin story, Cherone sometimes has to produce broadcast stories for WTTW to complement her online pieces. With only three minutes to work with as opposed to thousands of words, she must shift her approach to a more conversational tone and be more selective in the data she shares and explains on-​air. A short bullet list of key stats may flash on the screen as she discusses the story with the news anchor.

"I know the questions that the anchor is going to ask me so that I can be sure that we're heading in the right direction," she said. "Many times, you can only tell them why it matters and maybe one important supplementary piece of information and then that's it. It's frustrating but it is just the nature of TV."

</aside>

Cherone said she believes data can point journalists to the most compelling and illustrative people to interview for an article, and a data-​infused summary graph can give the story authority and credibility. It's important to know how to integrate data into a story and how to characterize and present numbers and statistics in ways that readers can readily understand. The general rule of thumb: Journalists should use only the most salient numbers in their story and allow readers to drill deeper by posting data online and creating graphics.

Data journalism gives reporters the opportunity to "zoom out" and look at an issue on a larger scale. For instance, you notice more potholes showing up on the roads in your neighborhood -- ​this is a potential story idea. You talk to some people whose cars were damaged by the potholes. You talk to some area tire and auto repair shops and, sure enough, business is booming this year.

That makes for a good *start* to a story, but you need data to give the readers the entire picture. Enter data reporting. Most likely, your city, county or province tracks pothole complaints and repairs. Pull the dataset, clean it and start sorting and filtering. Ask questions of the data: Which ZIP code, neighborhood or area has the most potholes? Which has the least? Are certain areas of the city slow to be repaired? If so, why? Compare this year's pothole data to past years. Is there an increase or decrease?

Cherone used this "zoom out" approach when she wrote a WTTW News story on Illinois' ban on evictions during the COVID-​19 pandemic in November 2021. Her first challenge came with finding the data. She contacted the Chicago Department of Housing, which said it didn't maintain data on evictions. She eventually reached the Office of Cook County Chief Judge Tim Evans, which took seven days to get her the data.

"Then it was a straightforward matter of comparing the number of evictions in October 2021 with the number of evictions in October 2020 and October 2019," she said.

"It was important to have \[two\] years of data to have a point of comparison before the COVID-​19 pandemic; while stay-​at-​home orders and the ban on evictions designed to stop the spread of COVID-​19 were in place; and after the ban and stay-​at-​home orders had been lifted."

The analysis broadened the scope of the story both in scale and time. She wrote:

> *Evictions rebounded significantly in October 2021 as compared with October 2020, when the restrictions were in place as the second wave of COVID-​19 swept Chicago and Illinois. Cook County judges approved only 322 evictions in October 2020, as compared with 1,866 in October 2021, according to the data*
>
> *In Chicago, 1,278 households were evicted from their homes in October 2021, along with 42 businesses, according to the data. In suburban Cook County, an additional 566 households were evicted, along with 22 businesses, according to the data.*

\* \* \*

Alvin Chang, head of data and visuals at *The Guardian US*, said data is "merely a structured collection of stories."

"So that means you can do two things with it: You can look at the dataset as a whole and see the big trends. But you can also zoom into one data point and learn more about it. If it's a dataset of people, you can call them; if it's a dataset of places, you can visit a location."

Beyond the data analysis, you can use the data to visualize the problem. A simple bar chart would track the number of pothole repairs and complaints annually over a five-​year stretch. This approach will be covered in-​depth in [Chapter 10](#ch10.xhtml_c10), but a map of those complaints and repairs, layered over a neighborhood or ZIP code shapefile, helps readers visualize patterns ([Figure 7.2](#ch07.xhtml_f7_2))that would be difficult to see in a written piece.


Chang said there's another dimension that reporters can forget about: The context. When reporters are neck-​deep in a dataset, it's easy to forget that this isn't the only information available. There are other datasets, other articles, other studies that can contribute to our understanding of the story. This is true for writing and visualizing a story, which we'll explore more in [Chapter 10](#ch10.xhtml_c10).

"They can help us explain *why* something is happening in the data," he said.

"A good example is visualizing racial segregation in neighborhoods, which can lead people to assume that there was some kind of natural sorting of racial groups. But understanding the larger context will reveal that residential segregation was an engineered phenomena born out of racist housing policies -- ​and missing that story would be journalistic malpractice."

\* \* \*

::: section
## Writing Exercise

In [Chapter 5](#ch05.xhtml_c5), you analyzed the 2019 Federal Highway Administration National Bridge Inventory database. You figured the percentage of good, fair and fair-​poor graded bridges per state and sorted them to see where various states rank.

Remember the questions you answered in the [Chapter 5](#ch05.xhtml_c5) exercises about states with the most and least in each category. Where does your state rank? Using the data points from that [Chapter 5](#ch05.xhtml_c5) analysis, write a three-​to-​four paragraph story for a local audience. Use a hard news lead focusing on just one key finding from your analysis, and then expand to more detail. Focus your lead there, and then support with a few paragraphs analyzing the high/low totals. There's an example for Illinois at the end of this chapter.

Journalism students at the University of Illinois at Chicago turned this assignment (using the 2017 database) into final project stories examining the conditions of Illinois and, more specifically, Illinois bridges. They compiled the percentages, sorted and filtered to find where Illinois ranked nationally for fair and poor bridges and then analyzed other studies to map where many of the troubled bridges are in the state.

The stories came with an interesting twist: The week after the first story was published on [RedLineProject.org](http://RedLineProject.org) in December 2018, a bridge over Lake Shore Drive at the Chicago River, one of the city's busiest and ranked "structurally deficient," buckled and shut down northbound lanes for two days. This snarled traffic and proved that, to play off a cliche, the numbers don't lie.

\* \* \*

::: section

## Writing Exercise Example

Illinois ranked 34th nationally in the number of bridges rated in fair-​to-​poor condition, according to an analysis of the 2019 Federal Highway Administration National Bridge Inventory database.

The data showed that 51.2 percent of the state's 26,825 bridges were in fair-​poor shape. The study also showed that 9 percent were rated in poor condition.

Rhode Island led all states with 82 percent of its bridges in fair-​poor condition, but the smaller state also had only 779 bridges. The District of Columbia (80 percent) and West Virginia (75.4 percent) weren't far behind.

Florida had the fewest fair-​poor rated bridges with 33.9 percent, followed by Mississippi with 37.2 percent.

\* \* \*

## Footnotes

- Houston Chronicle, Abuse of Faith [https://www.houstonchronicle.com/local/investigations/abuse-of-faith/](https://www.houstonchronicle.com/)
- Seattle Post-Intelligencer, Unmarked Graves May Hold His Sister, Niece [https://www.seattlepi.com/local/article/Unmarked-graves-may-hold-his-sister-niece-1213531.php](https://www.seattlepi.com/)
- Inside Climate News, Superfund, Super Threats [https://insideclimatenews.org/project/super-threats/](https://insideclimatenews.org/)
- Charleston (West Virginia) Gazette-Mail, Painkiller Profiteers [https://www.wvgazettemail.com/news/legal_affairs/drug-firms-poured-780m-painkillers-into-wv-amid-rise-of-overdoses/article_99026dad-8ed5-5075-90fa-adb906a36214.html](https://www.wvgazettemail.com/)
- Working Safely With Statistics, presentation by Jennifer LaFleur and Holly Hacker, NICAR 2022 Conference
- Forbes, A Good Presentation Is about Data and a Story [https://www.forbes.com/sites/kateharrison/2015/01/20/a-good-presentation-is-about-data-and-story/?sh=4360736b450f](https://www.forbes.com/)
- Arizona Republic, [AZCentral.com](http://AZCentral.com), Former Arizona Cardinals Players among Thousands in NFL Concussion Lawsuit [https://www.azcentral.com/story/sports/nfl/cardinals/2018/06/09/former-arizona-cardinals-players-among-thousands-nfl-concussion-suit/592331002/](https://www.azcentral.com/)
- DataCamp, Seven Tricks for Better Data Storytelling [https://www.datacamp.com/blog/seven-tricks-for-better-data-storytelling-part-ii](https://www.datacamp.com/)
- Houston Chronicle, Peril in the Oilpatch [https://www.houstonchronicle.com/local/peril-in-the-oil-patch/](https://www.houstonchronicle.com/)
- Online Journalism Blog <https://onlinejournalismblog.com/>
- WTTW, City Council Committee Led by Indicted Ald. Austin Spends More, Does Less Than Nearly All Others [https://news.wttw.com/2021/08/16/city-council-committee-led-indicted-ald-austin-spends-more-does-less-nearly-all-others](https://news.wttw.com/)
- WTTW, Evictions Jump after Ban Ends, but Tsunami Fails to Materialize in Chicago, Cook County: Data [https://news.wttw.com/2021/11/23/evictions-jump-after-ban-ends-tsunami-fails-materialize-chicago-cook-county-data](https://news.wttw.com/)
- The Red Line Project, Thousands of Illinois Bridges Graded Structurally Deficient [http://redlineproject.org/poorbridges.php](http://redlineproject.org/)


# 8 SQL

Samantha Sunne

DOI: [10.4324/9781003273301-9](https://doi.org/10.4324/9781003273301-9){aria-label="D.O.I. link to this document."}

Spreadsheet skills like sorting, filtering and formulas can get you very far in journalism. Some data journalists even say that 80 percent of data journalism can be done with these initial skills. But as you begin to work with larger and more complex datasets, you may want to use a more advanced method like SQL.

SQL stands for "structured query language," and it's a syntax that can be used in many different programs. It's an especially popular option for people who need to join multiple tables together or handle datasets so big they would make a spreadsheet program break down.

Technically, spreadsheet programs like Google Sheets and Microsoft Excel can process SQL, but it's not what they are designed to do. Excel can run SQL queries by connecting to other software programs, and Google Sheets has a powerful QUERY() function.

But just because you can work with millions of rows in Google Sheets doesn't mean you should! You will find your functions stalling and your screens freezing. Spreadsheet programs are designed to handle smaller tables, even if "small" in this case means a few million rows.

\* \* \*

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section

## Pro Tip ![](images/Pro_Tip_Icon.jpg) 

How is SQL pronounced? In conversation, it's usually referred to as "sequel" but can also be spelled out as S-​Q-​L. There are a variety of programs that use SQL in their name. And just like different dialects of the same language can exist in the same country, the preferred pronunciation of some tech terms can also vary depending on who you ask.

Both the programs and the syntax can be referred to either way. But the more you use these particular programs, the more you will become familiar with the lingo, making you sound more like an experienced data journalist.

</aside>

\* \* \*

To trade up, many people use programming languages like Python or desktop applications called "database managers," both of which can use SQL. To learn how it works, we will practice a story on the wealthiest cities in California.

We'll start with a dataset (shortlink: [https://bit.ly/incometable](https://bit.ly/)) that shows the population and median household income for every ZIP code in California. It comes from the 2010--​2014 American Community Survey, a five-​year demographics collection program by the US Census Bureau.

Unfortunately, the dataset records the ZIP code and the population in the same column, separated by a slash (/). It also doesn't list the names of places or towns, just their ZIP codes. Most journalism audiences will want to see the name of the town.

We will use SQL to clean, organize and analyze this data and ultimately merge it with another dataset to find a story on the richest locales in the Golden State.

:::: section
## Queries

When working with SQL, the keyword is in its middle name: Query.

In technical terms, a SQL query is a complete instruction in SQL syntax that can be executed by a computer. They are also called "SQL statements." In conversational terms, a query is like a question asked to a computer rather than a human being.

SQL is made up of individual keywords, commands and operators ([Table 8.1](#ch08.xhtml_t8_1)). To run queries, you'll need to understand a few of these keywords, but just like with sorting and filtering in spreadsheets, you can dive deep into a database with just a few basic commands.

+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ***Commands***                    |                                                                                                                                                                                                                                                                                                         |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SELECT                            | SELECT tells the computer which data to retrieve from a table. You can request all columns, just a few columns, or limit it to criteria like the ones below. The columns will appear in the order they are entered in the SELECT command, separated by commas.                                          |
|                                   |                                                                                                                                                                                                                                                                                                         |
|                                   | To run a calculation on your data, like SUM, you still need to start your query with the SELECT command. You can think of it as asking the computer to "show you" the sum.                                                                                                                              |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| FROM                              | FROM tells the computer which table you are retrieving data from. In the example above, the name of the table is "istanbul."                                                                                                                                                                            |
|                                   |                                                                                                                                                                                                                                                                                                         |
|                                   | The FROM command will be especially important to understand when we start to retrieve data from multiple datasets in the same query. This is one of the features that makes SQL stand out from spreadsheets.                                                                                            |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| WHERE                             | The WHERE command functions similarly to its use in English. You can use it as a filter so that the query only returns data meeting certain criteria.                                                                                                                                                   |
|                                   |                                                                                                                                                                                                                                                                                                         |
|                                   | In the WHERE clause above, we only want to see the population where the year is "2006." The WHERE clause must always be placed after the FROM clause, but before some other commands, like ORDER BY.                                                                                                    |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ORDER BY                          | ORDER BY is equivalent to sorting in a spreadsheet. You can use it to arrange rows alphabetically, chronologically, numerically and so on.                                                                                                                                                              |
|                                   |                                                                                                                                                                                                                                                                                                         |
|                                   | The ORDER BY clause will default to ascending order. If you want the opposite (large to small), you can specify that by adding the DESC keyword.                                                                                                                                                        |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GROUP BY                          | GROUP BY is a little more complex. This command groups together rows that have the same value in one of the table's columns, similar to the pivot tables we used in [Chapter 6](#ch06.xhtml_c6).                                                                                                        |
|                                   |                                                                                                                                                                                                                                                                                                         |
|                                   | This command is especially useful for calculating totals, such as the total population per state, or finding unique values in a column.                                                                                                                                                                 |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| HAVING                            | HAVING is a command that is almost identical to the WHERE command. The difference is that HAVING can filter groups, while WHERE can only filter rows.                                                                                                                                                   |
|                                   |                                                                                                                                                                                                                                                                                                         |
|                                   | If you use the GROUP BY command to create groups of rows and want to filter them by a certain condition, you will need to use a HAVING clause.                                                                                                                                                          |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LIMIT                             | This command limits the number of rows to return. It can be helpful when working with large datasets, or if you know your query will return too many rows for you to look at comfortably. For example, the command "LIMIT 10" would return only the first ten rows matching the criteria in your query. |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| OFFSET                            | OFFSET is a command that begins a query at a row other than the default. OFFSET is mostly used for declaring a header row.                                                                                                                                                                              |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| DISTINCT                          | DISTINCT is not technically a command itself, but it is an argument you can add to a SELECT command. It limits the output to unique values within a column. This tool is especially useful if you can't see the whole dataset and want to know all the values in a column.                              |
|                                   |                                                                                                                                                                                                                                                                                                         |
|                                   | In a spreadsheet program like Google Sheets, it is similar to the Values that appear in the Filter drop-​down menu for a column.                                                                                                                                                                         |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ***Functions***                   |                                                                                                                                                                                                                                                                                                         |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| COUNT()                           | COUNT() is a mathematical function in SQL that counts the number of rows meeting certain criteria. COUNT can be used for numerical values as well as text. For instance, you could count the number of rows containing the word "istanbul."                                                             |
|                                   |                                                                                                                                                                                                                                                                                                         |
|                                   | This can be especially helpful for data integrity checks. To find the number of rows in your dataset, you could use COUNT(\*), meaning "count all."                                                                                                                                                     |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SUM()                             | SUM is another mathematical function. Just like its spreadsheet counterpart, it returns the sum of the values you enter as parameters. SUM will only work on numerical values, not text, and null values (empty cells) will be considered 0.                                                            |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: *[Table 8.1*](#ch08.xhtml_t8_1b) Common SQL Keywords

For example, to ask, "What was the population of Istanbul in 2006?" you might write this query:


    SELECT population
    FROM istanbul
    WHERE year = 2006

The words at the beginning of each line -- ​SELECT, FROM and WHERE -- ​are called "commands." Each line is a "clause," and the equal sign is an "operator." All of these fit under the umbrella of SQL "keywords," and together they form a SQL query. Some programs, but not all, require a query to end in a semicolon (;).

::::: section

## Importing

SQL is a common language found in many programs and even programming languages across the digital world. So how, and where, should you use it?

It's safest to write SQL in programs that can save your queries, outputs and tables so that you don't lose them, or lose track of what you've done. (This is one reason to keep data diaries, which we learned about in [Chapter 4](#ch04.xhtml_c4).)

One option is a database manager, like SQL Server, MySQL or Microsoft Access. These programs are very popular among companies that record and analyze huge amounts of information, like sales databases. They are powerful but can be expensive.

There are some free options, like DB Browser, MySQL Workbench and SQLite Manager. And beyond that, there are some hybrid programs for working with data, like Tableau and Microsoft Power BI, that can perform both spreadsheet and SQL functions.

You can also use SQL in programming languages like Python and R. RStudio, which we used in [Chapter 6](#ch06.xhtml_c6), is capable of running SQL queries and has a relatively easy-​to-​use interface. In [Chapter 9](#ch09.xhtml_c9), Scraping Social Media, we will tackle installing and writing code.

All of these are viable options for running SQL queries. The question is, how big is your data, how big is your budget and what are you trying to accomplish?

To avoid having to install a language or GUI, we will use a website called DB Fiddle. DB Fiddle is an online sandbox -- ​a self-​contained environment that lets you execute functions and test code, without it affecting other parts of your computer. This allows us to see the outputs of various SQL statements without installing other programs or paying for a more powerful application.

Unlike database managers, DB Fiddle will not store queries or outputs, meaning it is not the best choice for a bigger or more complex analysis. Because it's a sandbox, it also does not have a very sophisticated import system. Instead, we will simply copy-​paste our values into the site.

\* \* \*

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 1 ![](images/Exercise_Icon.jpg) 

1.  Download this comma-​separated value (CSV) file of incomes in California (shortlink: [https://bit.ly/incometable](https://bit.ly/)), and open it in a text editor, such as Sublime Text. Do not use a spreadsheet program like Excel, because that can introduce new formatting. Highlight all of the data and copy it to your clipboard.
2.  Open DB-​[Fiddle.com](http://Fiddle.com) and click the Text to DDL button. This is where we will paste our data.
3.  In the pop-​up window, name the table "income_data." The name of the table will be very important later, so make sure you name it this exact text string, including the underscore and without quotes around it.
4.  Paste the copied values into the Formatted Text field.
5.  Click the Preview DDL button to get a glimpse at how your data looks as it is being imported.
6.  Click Append to Schema to load it into the sandbox.

</aside>

As you paste in the data, the two fields should be separated by a comma ([Figure 8.1](#ch08.xhtml_f8_1)). The second column is called "Zip / Population" and contains a slash in the middle of it. DB Fiddle should intake the income column as an integer and the ZIP code column as a "varchar."


These are two data types found in SQL. As we have learned from other programs, it's important for the computer to understand what kind of data is in each column. After all, you can't run a SUM() calculation on a list of names. Only a list of numbers.

SQL data types can sometimes vary by program, but integer and varchar are two of the most common types. An integer, sometimes shortened to Int, is a number.

A varchar datapoint is a text string made of "various characters." A varchar column, just like a text column in a spreadsheet, can contain letters, numbers or even entire phrases, all considered one datapoint. Because it is text, a varchar column should be wrapped in quotes.

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Pro Tip ![](images/Pro_Tip_Icon.jpg) 

You may have noticed that DB Fiddle includes more text at the top of the schema panel, including the words CREATE TABLE. With many SQL programs, you will simply import your data without needing to create a table, although typing it manually is an option, with commands like INSERT.

</aside>

\* \* \*

:::::::: section
## Filtering

Whenever you want to view the results of a query in the same place you are writing it, you will use the SELECT command. SELECT can also be thought of as a filter, because you are telling the computer which columns or calculations you want to see. Everything else will be hidden.

If you're not ready to filter yet, and want to see all the columns in a table, you can type the following clause to mean "show all."


    SELECT *

The asterisk (\*) is a common wildcard in many search syntaxes, meaning it can take the place of other characters.

Even if you are writing a calculation, like COUNT(), you will use the SELECT command to display the output. For example, a good query to keep in your pocket for "gut checks" is to count the null values (empty cells) in a dataset. That query would look something like this:


    SELECT COUNT(*)
    FROM income_data
    WHERE income IS NULL

In DB Fiddle, we can see that our "Zip / Population" column is wrapped in quotes, meaning it was imported as text. As we saw in [Chapter 4](#ch04.xhtml_c4), values sometimes need to be wrapped in quotes so that a program doesn't think the slash (or even the space) is a delimiter. The first column, "income," is only one word and so doesn't necessarily need quotes.

Therefore, a SELECT command for both columns would look like this:


    SELECT Income, 'Zip / Population'

Cleaning and importing may not be the most fun part of a data analysis, but it's always important to understand how your program is interpreting and storing your data. Skipping these steps can lead to disaster!

\* \* \*

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Pro Tip 

If you get error messages right away, quotation marks are usually to blame. If DB Fiddle claims the Zip column can't be found, try copying and pasting the field name (including quotes) from the SQL Schema panel.

Alternately, try deleting the quotation marks in the SQL Schema panel, where we pasted the data, or deleting and retyping them. Fonts can have different types of single quotation marks (opening, closing or neutral), and sometimes software programs will only accept a neutral (not slanted) quotation mark.

</aside>

\* \* \*

Now that we have imported our data into DB Fiddle, let's practice filtering by writing a query.

DB Fiddle will return the first 10 rows of our income table in a new Results panel but only the income column ([Figure 8.2](#ch08.xhtml_f8_2)). This is an example of two filters at work: the SELECT command, which retrieves columns, and the LIMIT command, which restricts the number of rows.


<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 2 ![](images/Exercise_Icon.jpg) 

1.  In the Query SQL panel of DB Fiddle, type the following SELECT statement:


        SELECT income
        FROM income _ data
        LIMIT 10

2.  Click Run at the top of the screen.

</aside>

Next, let's try filtering with the WHERE command. WHERE is a much more influential filter because it can work with search operators to limit rows to certain criteria ([Table 8.2](#ch08.xhtml_t8_2)). These searches are referred to as the "WHERE clause."

+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LIKE                              | The LIKE operator in SQL works similarly to the word "like" in English. It matches partial strings, making it useful for finding data if you don\'t know exactly what the value is, or if you want to return a collection of similar values.                                                           |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                   | For example, the operator "LIKE \'dog%\'" would return rows that contain "dog" or "dogs." It is often used in conjunction with wildcards like the percent sign (%). Without a LIKE operator, a WHERE command for a text string will only return exact matches for that string.                         |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                   | If you are using the LIKE operator on a text string, it needs to be wrapped in quotes.                                                                                                                                                                                                                 |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| AND                               | AND adds another condition to a WHERE clause. It is useful for limiting results beyond what you could filter with just one search condition.                                                                                                                                                           |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                   | The AND operator can combine searches for different columns and data types. For example, you could filter for rows where the median household income is above a certain amount, and the ZIP code is a certain number, combining text and numerical filters.                                            |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| OR                                | The AND operator narrows a search, but the OR operator widens it. A query containing the OR operator will return any row that matches either condition in a WHERE clause, casting a much wider net.                                                                                                    |
|                                   |                                                                                                                                                                                                                                                                                                        |
|                                   | In the example above, the query would return any row with a certain income *or* a certain ZIP code.                                                                                                                                                                                                    |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| IS NULL                           | This book has touched many times on the dangers of empty rows or null values. The method to find these in SQL is the condition IS NULL. It is most often used in a WHERE clause and can be complemented by its opposite, IS NOT NULL.                                                                  |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| --                                | An underscore (\_) is a wildcard - a character that stands in for other characters. An underscore will only match a single character. That is, a search for "do\_" will return "dog" but not "dogs." It is most useful when searching for values that you know probably exist, like an ID number.      |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \%                                | A percent sign (%) is a wildcard that will match any number of characters, making it a much broader search option. A search for "d%" would return "dog" as well as "dogs."                                                                                                                             |
|                                   |                                                                                                                                                                                                                                                                                                        |
|                                   | If you\'re looking for rows that contain a term anywhere in it, you can enter it between two percent signs, like "%dog%." Importantly, a percent sign will also return values where there is no character in that location, but it will not return null values.                                        |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \*                                | An asterisk (\*) is a wildcard meaning "all" and is a common sight in SQL statements. For example, "SELECT \*" means "select all columns," while "COUNT(\*)" means "count all rows."                                                                                                                   |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| =                                 | Unlike a wildcard, the equals sign (=) operator identifies a perfect match. This can be used for both strings and numbers.                                                                                                                                                                             |
|                                   |                                                                                                                                                                                                                                                                                                        |
|                                   | For example, the clause "WHERE breed = \'chihuahua\'" would only return rows that correctly spelled the word "chihuahua." If you\'re not confident in your source\'s spelling skills, as we saw in Chapter 4, Cleaning Data, you may want to instead use a wildcard, like "WHERE breed LIKE \'chi%\'". |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| != or \< \>                       | The not-equal-to operator is the opposite of the equal sign, meaning it will return any value that does *not* meet the search condition. Some SQL programs will require the user to enter either "!=" or "\< \>" even though they mean the same thing.                                                 |
|                                   |                                                                                                                                                                                                                                                                                                        |
|                                   | In many programs, you can add an exclamation mark (!) in front of a mathematical operator to mean "not." That is, "\>5" means "greater than 5," and "!\>5" means "not greater than 5."                                                                                                                 |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \>, \<, \>=, \<=                  | These operators hearken back to elementary math and can only be used on numerical values. The angle bracket that broadens away from the value, that is, "\>5", means "greater than," while its reverse means "less than."                                                                              |
|                                   |                                                                                                                                                                                                                                                                                                        |
|                                   | Adding an equal sign to these operators makes them "greater than or equal to" or "less than or equal to."                                                                                                                                                                                              |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| BETWEEN                           | The BETWEEN operator saves you some time when limiting results to a range between two values. For example, the clause "WHERE amount BETWEEN 5 AND 10" is the same as "WHERE amount \> = 5 AND amount \< = 10". The operator is inclusive, meaning it will also return values matching 5 and 10.        |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: *[Table 8.2*](#ch08.xhtml_t8_2b) Common Search Operators

So far, we have used the SELECT command to limit columns and the LIMIT command to limit rows. Now, let's use the WHERE command to filter our results for something much more interesting.

It's important to use the exact terminology for both commands and criteria. For example, if a table is named "income_data", with an underscore, but the FROM command calls from "income data", with a space, the query would produce an error message or simply not run at all. 

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 3 

1.  In DB Fiddle, change your SELECT clause to an asterisk, meaning "all columns."

        SELECT *
        FROM income _ data
        LIMIT 10

2.  Next, add a WHERE clause so that your final query looks like this:


        SELECT*
        FROM income _ data
        WHERE income>40000
        LIMIT 10

3.  Click Run to see a new output in your Results panel. The output should now only show incomes above \$40,000.

4.  Next, add an AND operator to your WHERE clause, to make the following query:


        SELECT *
        FROM income _ data
        WHERE income>40000
              AND income<60000
        LIMIT 10

5.  Click Run. Now, the output is limited to incomes that are both above \$40,000 and below \$60,000.

6.  Lastly, add a LIKE operator to your WHERE clause and click Run.


        SELECT *
        FROM income _ data
        WHERE income>40000
             AND income<60000
             AND `Zip / Population` LIKE '90%'
        LIMIT 10

7.  Bonus Question: How would you rewrite the query to pull incomes above \$100,000?

    With the LIKE operator, we need to use quotes (\') around the values because they are text strings. It limits the results to ZIP codes starting with "90", while the mathematical operators limit the results to incomes between \$40,000 and \$60,000 ([Figure 8.3](#ch08.xhtml_f8_3)).


</aside>
<aside class="boxed-text2" epub:type="tip" role="doc-tip">

::: section
### Nested Queries 

Another way to filter is to write a query inside another query, just like we wrote functions inside of other functions in a spreadsheet. These are called "nested queries" or "subqueries," and a simple version looks like this:


    SELECT “Zip / Population”
    FROM income _ data
    WHERE income >   (
         SELECT AVG(income)
         FROM income _ data)

Nested queries can also be used to connect two tables, which we will discuss later in this chapter. However, they can start to get confusing and may not be the best method for filtering down your data.

</aside>

Some SQL programs are case sensitive -- ​meaning you need to use the correct capitalization for both commands and criteria for it to work. Even if your program isn't case sensitive, the norm is to write your commands in all capital letters. This helps them stand out and is a generally accepted practice, even if a program doesn't necessarily need it to run.

Another general practice is to write each command on its own line, with clauses indented below it. Many programs will happily execute queries all written out in one long line. But giving each clause its own line, and writing the command in all capital letters, makes it easier for the human to read.

We have now limited our results to certain ZIP codes, and to a certain income range, but that's not all that we need to know. We want to find the highest incomes as well as their cities -- ​not just their ZIP code. And unfortunately for us, the ZIP codes are stored in a text string along with the population. So to continue our analysis, we will need to do a bit of cleaning.

:::: section

## Cleaning

SQL may not be the most efficient cleaning method at your fingertips, but it is capable. If a dataset contains many errors, like misspellings or empty rows, you may want to first run it through a cleaning method like spreadsheet functions, OpenRefine, or the other tools we talked about in [Chapter 4](#ch04.xhtml_c4). But if the data is relatively organized, editing some data in SQL may be the smartest choice. In the SQL world, this kind of work is called "data manipulation" because you are changing the data values themselves, not sorting or analyzing them.

One way to keep track is an "alias" -- ​a new or alternate name for a column. Aliases are especially useful when creating calculated columns, like totals or averages. They are established with the AS operator in a SELECT clause, like this:


    SELECT AVG(population) AS avg _ pop

We're going to clean the confusing "ZIP / Population" column by extracting the ZIP code and putting it in a new column called "ZIP." SQL uses many of the same functions you find in spreadsheet programs, including LEFT().

If you recall from [Chapter 6](#ch06.xhtml_c6), the LEFT() function extracts a certain number of characters from the left-​hand side of the specified column. In SQL, the column is usually the first parameter, and the number of characters is the second.

As you get more used to writing SQL, it will become safer to omit the original column and SELECT only your newly created field. But if you are unsure, it's fine to retrieve the original column as well, so you can see them side by side.

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 4 

1.  In DB Fiddle, delete your query and write a new one:


        SELECT income,
           'ZIP / Population',
           LEFT('ZIP / Population',5)
           AS ZIP
        FROM income _ data
        LIMIT 10

2.  Click Run.

Here, we are selecting three columns: the income, the Zip / Population, and a new column called ZIP. The ZIP column contains only the first five characters of the "ZIP / Population" column ([Figure 8.4](#ch08.xhtml_f8_4)).


</aside>

At this point, it would be smart to store this output as a new table. The table would have three columns, one of which is a simple five-​character ZIP code. Unfortunately, DB Fiddle doesn't allow us to store queries or tables, so in our practice sessions, we will need to keep establishing the calculated column in every query.

We've taken an important step: Separating the ZIP code from the area's population. But what towns are these? Journalism audiences don't know the ZIP codes of every town in California. For that, we'll have to venture into one of the biggest advantages of SQL: Joins.

:::::: section
## Joining

Joining datasets is one of the main reasons journalists use SQL instead of other analysis methods. While you can technically use two datasets at once in a spreadsheet program, SQL has dedicated tools for this and can handle much larger sets of data.

Luckily for us, the Census has another dataset of Postal Service ZIP code areas, including the city and county names. We will write a query to "join" those two datasets, using the ZIP code as a guide.

Unless there are errors, the extracted ZIP codes in the income table should exactly match the ZIP codes in the postal code table. This means we can use the WHERE command with the equal sign operator to find a perfect match.

In a Join, these are often called "keys." The ZIP in the income table is the "primary key," and the ZIP in the postal table is the "foreign key." The values must match exactly for the Join to work, which is why we extracted the ZIP code using the LEFT() function.

In a JOIN query, you use the SELECT command to choose columns, but this time you can choose columns from different datasets. If they happen to have the same field name, you can use a period to identify the source table, like this:


    SELECT income _ data.ZIP, postal _ data.ZIP
    FROM income _ data, postal _ data

That simple SELECT command would show two columns of ZIP codes -- ​one from the income_data table and another from the postal_data table. If the field name is unique, you do not need to use a period to specify the table it's from.

\* \* \*

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Pro Tip 

To run a join, you don't need to SELECT the joined column -- ​it is working as a kind of glue in the WHERE clause. But to be sure your queries are executing correctly, you can retrieve all of the columns including the keys. Some columns will be redundant, because the primary key will match the foreign key, but you can be sure that your Join is operating correctly.

</aside>

\* \* \*

Let's execute a simple SELECT statement to see a Join in action.

To keep track of the ZIP codes from different tables, we will use aliases. Let's call the ZIP from the income table "income_zip" and the ZIP from the postal code table "postal_zip".

\* \* \*

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 5 

1.  Download this CSV file of California ZIP codes (shortlink: [https://bit.ly/ziptable](https://bit.ly/)) and open it in a text editor. We can see there are four columns, with one named "zip" and one named "city." (Remember, exact column names are important.)

2.  Import it into DB Fiddle using the instructions in Exercise 1. Name the table "postal_data." It should now appear as a second dataset in the Schema SQL panel.

3.  In the Query SQL panel, write the following query:


        SELECT income,
            LEFT(`Zip / Population`,5) AS income_zip,
            postal _ data.zip AS postal _ zip,
            city
        FROM income _ data, postal _ data
        WHERE LEFT(`Zip / Population`,5) = postal _ data.zip
        LIMIT 10

4.  Click Run and look at the output.

    Here we selected four different columns: the income, the ZIP code from the income table, the matching ZIP code from the postal table, and the city from the postal data. This is an example of how a Join is powerful. Now that we have joined these datasets, we can see the place names for these incomes, not just their ZIP codes ([Figure 8.5](#ch08.xhtml_f8_5)).


</aside>
<aside class="boxed-text2" epub:type="tip" role="doc-tip">

::: section
### Inner and Outer Joins 

There is another kind of join called an "Outer Join," which returns rows even if they don't match a key. As you learn more SQL, you might come across terms like "Left Join," "Right Join" and even "Cross Join."

The type that we did is called an "Inner Join," and it limits the output to rows where the primary key matches the foreign key. Inner Joins are the most common and the most likely to be used in a data journalism analysis.

</aside>

So far, we have accomplished a lot of cleaning and analysis with SQL. We identified the cities in these ZIP codes and limited the results by income. But we still have a challenge ahead of us. Most large cities, like Los Angeles, have several or even dozens of ZIP codes -- ​but journalism audiences would likely think of them as the same city. We will move on to another powerhouse in the SQL syntax: Grouping.

:::: section

## Grouping

The GROUP BY command groups together rows with matching values, similar to pivot tables in spreadsheet programs. (Refer back to [Chapter 6](#ch06.xhtml_c6) for more on pivot tables.)

One good use of this is the postal code dataset. Instead of dozens of rows for ZIP codes in Los Angeles, we could group them into one row called "Los Angeles."

There is one downside to this method: Since we are compressing all of those rows into one, we can no longer see all of the individual ZIP codes or incomes.

This means we will have to use a calculated column rather than simply calling the income column. Calculated columns are usually created using SQL functions like COUNT() and SUM(). We will use the AVG() function to find the average income in each city.

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 6 

1.  Enter "AVG(income)" in your SELECT clause to create a calculated column of income averages.

2.  Second, add "city" as a second column. Because we are grouping by city, it makes sense to see each city listed in our output.

3.  Keep the FROM and WHERE clauses the same, since we are using the same tables and the same joining criteria.

4.  After the WHERE clause, add a GROUP BY clause to group the rows by city. It is not necessary to specify "postal_data.city" with a period, because there is only one column called "city".

5.  Keep the LIMIT 10 clause intact to avoid outputting more rows than you need. This can slow down your computer. The final query should look like this ([Figure 8.6](#ch08.xhtml_f8_6)):


        SELECT AVG(income), city
        FROM income _ data, postal _ data
        WHERE LEFT(`Zip / Population`,5) = postal _ data.zip
        GROUP BY city
        LIMIT 10


</aside>

We can now see that, for instance, the average income in Acampo, California, is around \$60,000.

To make our query less unwieldy, we omitted the ZIP code columns from our SELECT clause. Because they are listed in the WHERE clause, we know they are working to join the two datasets, but we don't actually need to show them.

Now we have a list of ten average incomes grouped together by city. We're almost there! The last step is simply to sort those incomes from highest to lowest.

::::: section
## Sorting

Sorting is a rather simple task within SQL, typically with the ORDER BY command.

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 7 

1.  Add an ORDER BY clause after your GROUP BY clause, to create this full query ([Figure 8.7](#ch08.xhtml_f8_7)):


        SELECT AVG(income), city
        FROM income _ data, postal _ data
        WHERE LEFT(`Zip / Population`,5) = postal _ data.zip
        GROUP BY city
        ORDER BY AVG(income) DESC
        LIMIT 10


    Remember that ORDER BY defaults to arranging values in ascending order, which is why we included the DESC keyword.

</aside>

\* \* \*

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Pro Tip 

You can also sort multiple columns with the ORDER BY clause. This option comes into play if several rows have the same value in one column. For example, this clause would sort alphabetically by country and then by city:


    ORDER BY country, city

</aside>

\* \* \*

And with that, we have our story! Atherton is the wealthiest city in California, at least by this measurement. The other nine cities provide some good context and additional information for the reader.

We used SQL for spreadsheet-​type functions, like filtering and sorting, as well as more advanced techniques like joining and grouping. In addition to this, SQL programs can process much more data than your average spreadsheet.

\* \* \*

<aside class="boxed-text2" epub:type="tip" role="doc-tip">

For more data journalism tips, tricks and exercises, visit the Data + Journalism blog at <http://dataplusjournalism.com>

</aside>

\* \* \*

::: section

## Footnotes

- How to Get Started with Data Journalism in Your Newsroom [https://www.americanpressinstitute.org/publications/reports/strategy-studies/how-to-get-started-data/](https://www.americanpressinstitute.org/)
- SQL Server [https://www.microsoft.com/en-us/sql-server/sql-server-downloads](https://www.microsoft.com/)
- MySQL <https://www.mysql.com/>
- Oracle [https://www.oracle.com/index.html](https://www.oracle.com/)
- Microsoft Access [https://www.microsoft.com/en-us/microsoft-365/access](https://www.microsoft.com/)
- DB Browser <https://sqlitebrowser.org/>
- SQLite [https://sqlite.org/index.html](https://sqlite.org/)
- Tableau <https://www.tableau.com/>
- Microsoft PowerBI [https://powerbi.microsoft.com/en-us/](https://powerbi.microsoft.com/)
- California Household Income [https://drive.google.com/file/d/10FmnemIAbDZlu4tlBSi5D_TTvoS_3GZ6/view?usp=sharing](https://drive.google.com/)
- California Household Income shortlink [https://bit.ly/incometable](https://bit.ly/)
- 2010--2014 American Community Survey [https://www.census.gov/programs-surveys/acs/technical-documentation/table-and-geography-changes/2014/5-year.html](https://www.census.gov/)
- MySQL Workbench [https://www.mysql.com/products/workbench/](https://www.mysql.com/)
- SQLite Manager [https://chrome.google.com/webstore/detail/sqlite-manager/njognipnngillknkhikjecpnbkefclfe](https://chrome.google.com/)
- QUERY() function [https://support.google.com/docs/answer/3093343?hl=en](https://support.google.com/)
- DB Fiddle <https://www.db-fiddle.com/>
- ZIP Code Tabulation Areas [https://www.census.gov/programs-surveys/geography/guidance/geo-areas/zctas.html](https://www.census.gov/)
- California ZIP Codes [https://drive.google.com/file/d/1cvym2cbUTRo4VqniVNDabAu2PWZEVqng/view?usp=sharing](https://drive.google.com/)
- California ZIP codes shortlink [https://bit.ly/ziptable](https://bit.ly/)


# 9 Scraping Social Media

Samantha Sunne

DOI: [10.4324/9781003273301-10](https://doi.org/10.4324/9781003273301-10){aria-label="D.O.I. link to this document."}

## Introduction

In 2015, two tenacious Associated Press reporters were facing a problem. Illinois state lawmaker Aaron Schock was facing accusations of corruption and bribery, and he wasn't returning their calls.

In an attempt to dig in to some of these accusations, the reporters turned to what was then an unusual source: Instagram.

"The AP extracted location data associated with each image then correlated it with flight records," Jack Gillum and Stephen Braun later explained in their story. "The AP identified at least one dozen flights worth more than \$40,000 on donors' planes since mid-​2011."

Gillum and Braun's story, using Instagram metadata, revealed a pattern of flashy and ethics-​violating behavior by the lawmaker. It partly inspired a congressional inquiry and also served as an introduction to social media investigations for many in the journalism industry.

These days, using Instagram as a source wouldn't be considered unusual. Journalists as well as their audiences are aware of how much data everyone is constantly releasing via social media networks.

We have scraped data from the web, but in this chapter, we will learn that many front-​end tools, like web browsers and mobile apps, are not the only way to interact with data. Combine that mentality with a "data frame of mind," and you are well on your way to exposing secrets on the Internet.

When Gillum and Braun pulled location data from Instagram posts, they were accessing "metadata," which has a rather circular definition: Metadata is data that describes other data. It's easier to think of metadata in real-​world examples.

For instance, look at this Instagram post by the World Health Organization (WHO) (shortlink: [https://bit.ly/whoinstagram](https://bit.ly/)). The post itself is the "data." But this data, in turn, carries its own collection of data, like the number of likes, the day it was uploaded, the user ID of the uploader and much more ([Figure 9.1](#ch09.xhtml_f9_1)). Oftentimes, when you are scraping or backgrounding something on the web, you are digging up the metadata.


:::::: section

## Digging into Code

Metadata is everywhere, but if you're looking at a web browser, an easy way to find it is by opening the "source code." Source code is the collection of code that creates whatever you are looking at, whether that's the HTML behind a web page or the JavaScript behind a "subscribe" button. Often, source code can help you achieve something that the point-​and-​click tools of a website cannot.

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 1 ![](images/Exercise_Icon.jpg) 

Right-​click on the image in this WHO Instagram post (shortlink: [https://bit.ly/whoinstagram](https://bit.ly/)) and try to choose "Save Image As." The option isn't there. That's because Instagram doesn't want to let you download images through its website. Instead, we will obtain the image through the website's source code.

Right-​click on the page's white space, and this time select "View Source" or "Page Source." This opens up the source code in a new tab. This page may look intimidating, but that's just because it's meant for a computer to read, not a human. The easiest way to navigate it is to search for recognizable, human-​readable parts. If you scroll down long enough, you will find elements you recognize, like the WHO's caption for this post.

This is called "looking under the hood," and it's not the most efficient way to navigate a page's source code. But it does offer a window into the complicated goings-​on behind a web page. An easier way to explore it is the Web Inspector, which we learned about in [Chapter 3](#ch03.xhtml_c3). Every browser has a Web Inspector functionality, though sometimes it goes by different names, like "developer tools." We will continue using Google Chrome.

Right-​click again on the image in the Instagram post, and this time, choose "Inspect" or "Inspect Element." Now, the Web Inspector will pop open in a panel. It highlights parts of the code so that you can see where exactly each part of the web page comes from ([Figure 9.2](#ch09.xhtml_f9_2)).


Because we clicked "Inspect" on the image, it should highlight the image's HTML element within the pop-​up panel. You may need to expand the section with the drop-​down arrow, or click on nearby parts of code, in order to find it.

You can also use the Web Inspector in the reverse order. In the Inspector's toolbar, select the cursor button to make sure you have the "inspect element" function enabled. Then you can click on different parts of the web page, and the Inspector will highlight them in the code accordingly.

In our Instagram post, the HTML containing the image should include the letters "src," meaning "source," and a long URL. This is the link to the image's real home on the web. Open it in a new tab to see the raw image, and now you can save it! This is an example of how you can use source code to be more than a passive web surfer.

</aside>
<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 2 

Now let's obtain the image using another function of the Web Inspector -- ​the Network panel. The Network panel shows you all of the different calls your browser is making to download site resources located on different servers.

Click on the Network tab to see a list of resources the page is using. If this tab is empty, refresh the page using your web browser. Then you can watch as the Network panel loads all the various elements and requests it uses to create the page ([Figure 9.3](#ch09.xhtml_f9_3)).


Sort the results by Type to find the images -- ​they will usually be png or jpg files. If you click on each one, you should find the raw image that we opened in Exercise 1.

Another option is to sort by file size. Some journalists have even had success finding entire databases through these Network panels.

</aside>

\* \* \*

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Pro Tip ![](images/Pro_Tip_Icon.jpg) 

As we discussed in [Chapter 1](#ch01.xhtml_c1), journalists are typically going after public information like government databases. In those cases, you don't need to worry about breaking laws or website terms of service.

But if a site has the information behind a paywall, under copyright, or after a CAPTCHA, those are clues that you may be violating its terms of service or even the law. Some sites also restrict the number of requests you can make per session, although that is often to avoid overloading their servers.

If in doubt, it is always best to reach out to the person or organization that publishes or maintains the data. In the journalism field, resources like the Student Press Law Center offer guidance on these topics.

</aside>

::: section
## Programming Languages

In [Chapter 3](#ch03.xhtml_c3), we briefly discussed programming languages -- ​tools you can use across many different platforms. R, Python, JavaScript and C++ are all examples of different programming languages.

There are hundreds of languages in existence, but only a handful tend to surface as the most common. Github, a popular website for sharing and editing code, publishes a list of the languages most commonly used on its site ([Figure 9.4](#ch09.xhtml_f9_4)). On Github, you can find scripts of code that other people have written and made freely available. This is referred to as "open-​source" code.


So, which language should you learn? To begin with, you should assess which would best meet your needs. For instance, R is popular in data journalism because of its large-​scale data analysis tools. JavaScript is popular for interactive items or animations. Both of these tasks are doable in Python.

If nothing else, you may want to simply look for a sample script of what you are trying to accomplish -- ​say, scraping the HTML of a website. The same task may be easier for you in one language than another.

In addition, languages like Python have active communities online that can give you support. You may know someone in person, a friend or newsroom coworker, who has some familiarity with a language. All of these are valid reasons for picking a language.

This book will mainly rely on Python, which is one of the most popular languages in data journalism. We also will not be delving too deeply into writing code: Software engineering is an enormous field in its own right, and we will only be learning enough to accomplish our tasks, like scraping metadata. Sometimes, the data is so hard to get that it's not worth the time and effort it takes to write a scraper. In those cases, it's better to request the data through a human source like a public records request or a public information officer -- even if you need to negotiate with them.

::::: section

## Coding Challenges

Writing code tends to have a higher learning curve, but it also pays higher dividends. You are free from the limitations of third-​party tools, but you also need to manually create your own.

Instead of downloading tweets with Twitonomy, for instance, you can create your own tweet downloader using the Twint Python library.

A "Python library" is a set of code that someone wrote in an existing programming language to accomplish specific tasks and shared with the world. Sometimes prepared bits of code are also referred to as "packages" or "modules."

You can find a list of useful libraries at the end of this chapter ([Table 9.1](#ch09.xhtml_t9_1)). With almost every script, you will need to install them as add-​ons to the language you installed on your computer, which is why you will sometimes see them referred to as "dependencies" or "requirements."

  --------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  pandas          Pandas is an extraordinarily useful Python library for data analysis. It turns tasks like parsing HTML and merging large data files into something as simple as a few lines of code.
  BeautifulSoup   BeautifulSoup has spent years as a popular Python library for scraping web pages into spreadsheets. It helps complete the intermediary step of "parsing" source code into chunks that can then be separated into rows and columns.
  pdftotext       Pdftotext is a tool run entirely in the Command Line. It scrapes text and data out of PDFs and can handle up to 20 documents at a time.
  CSV             CSV is the name of a file format that can be imported into spreadsheet programs, but in this case, it's also the name of a Python library for creating (or "writing") CSV files.
  t               t is a Ruby gem for accessing Twitter data. It can perform bulk Twitter operations like following and unfollowing from the command line.
  dplyr           dplyr is an R package that makes it easier to do the kind of data analysis you're used to doing in SQL and spreadsheet programs.
  --------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  : *[Table 9.1*](#ch09.xhtml_t9_1b) Useful Libraries

In this chapter, we will use code to access, download and analyze data from social media sites.

Writing functions and scripts in programming languages, rather than in a platform like Google Colab, comes with several hurdles. As with many things, it's best to take these hurdles one at a time, until you can at least run a function without getting an error message.

Though it can be daunting to learn to code, it is entirely possible to learn enough to aid your reporting!

\* \* \*

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Pro Tip ![](images/Pro_Tip_Icon.jpg) 

When writing code, you are inevitably going to encounter error messages or simply be unable to run a script. [Chapter 4](#ch04.xhtml_c4) of this book contains troubleshooting options for some common problems, but the most foolproof method is to simply copy the entire text of the error message and paste it into Google.

Most of the time, you'll find someone else has posted the same query and received a response. If you can't find your specific problem, try adding keywords like the name of the programming language.

</aside>

:::: section
## Coding Terminology

Many of these coding tasks come with an enormous amount of vocabulary that may be unfamiliar to you. While reading this chapter, and googling your error messages, you may come across phrases like "command line interface," "Python interpreter," "virtual environment" and other daunting terms.

Don't attempt to memorize these concepts and phrases right off the bat. It's not necessary to know all of these keywords, and even professional software engineers often find themselves looking up definitions and syntax.

If you are interested in learning to code further, you may want to become more well-​versed in this vocabulary. But because we are learning technology to aid journalism, and not the other way around, we won't go out of our way to learn the many different ways to install, store and run code. You will find a detailed glossary at the end of this chapter ([Table 9.2](#ch09.xhtml_t9_2)). But remember, there is no shame in googling!

  ----------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Programming Language**      A programming language is a defined set of words, phrases and syntax that helps humans communicate with computers.
                                Some languages are somewhat similar to human speech, like Python, and some are not, like binary.
  **Machine-Readable Data**     Machine-readable data can be thought of as data that is ready to be read and processed by a computer, with no additional steps necessary.
                                For example, a PDF is not necessarily "machine readable" because it is meant to be printed out and read by humans. A CSV *is* machine readable because it can be imported straight into a spreadsheet.
  **Structured Data**           Data that has been tagged and identified is considered "structured data." This makes it easier and faster for a computer to run functions and can also make the data more easily understood by humans.
  **Console**                   When trying out code, the console is where you view your various inputs and outputs. You can test functions by looking at the outputs that get printed in the console before trying to actually scrape and export the data.
                                It might not be smart, for instance, to run a whole scraper on Facebook's API before you're sure the script works.
  **Python Interpreter**        The Python Interpreter is a fancy name for the machine that runs Python on your computer. Running Python commands outside of the Interpreter may not work because your computer doesn't inherently understand every Python function.
                                Rather, you need to enter the Python Interpreter by typing "python" (or the most recent version, like "python3") into your CLI. You know you are in the Interpreter if the CLI shows three brackets (\>\>\>) at the beginning of each line instead of a dollar sign (\$).
  **Python Standard Library**   The Standard Library is the set of libraries that come automatically with Python. It includes basic functions like help() and print() so that you don't have to install additional libraries just to get support for your code. But to accomplish many data journalism tasks, you will need to install additional libraries.
  **Script**                    A script is a finite collection of code, which usually accomplishes a specific task or set of tasks. A common programming method is to write a script in a word processor, like a text editor, save that file on your computer and then run the script using the CLI.
  **Function**                  A function is a finite set of code, usually within a script, that accomplishes a certain task. For example, in Python, the print() function displays an output in a console, while bespoke functions like "scrapeFacebookPostsO" may be much more complex.
                                In many programming languages, they are written with the syntax "function()", where the parameters of the function are listed inside parentheses that come directly after the name of the function.
  **Parameter**                 A parameter is an input in a function. For example, in our function importHTML("URL", "HTML element"), the URL we want to scrape is the first parameter, and the HTML element is the second.
  **Argument**                  An argument is the value in a parameter. For example, in the function importHTML("[https://example.com/page](https://example.com/)", "table"), the first argument is the URL "[https://example.com/page](https://example.com/)" and the second argument is the HTML element "table."
  **Variable**                  A variable is like a nickname you use to refer to something when writing code. You will have to define what your variable refers to early on in the code in order to use it later.
                                One example is a URL. Instead of typing out a long URL, you can store it as a variable simply called "URL." Then you can tell your function to scrape "URL" rather than a long string starting with "https://".
  **Define**                    When you create a function inside a script, it is often called "defining" a function. It can also be called "declaring" or "stating."
                                "Define" usually means an object is being given a name so that a function can call on it later. See "variable" and "reference" in this glossary.
  **Parse**                     To parse means to separate bits of data based on labels or indicators. For example, the BeautifulSoup Python library helps users to scrape HTML by parsing out the text into HTML elements.
  **Object**                    An object is an entity within a bit of code that can contain many different variables, values and data types. In pandas, for instance, you need to store a dataset as an object before being able to export it to a spreadsheet.
  **Array**                     An array is a list of values, but it's not as simple as a human-written list or the HTML "list" element. Arrays help to store many values so that you can tell a function to operate on all of them rather than on each item individually. In addition, some data can only be downloaded and parsed through an array.
  **for loop**                  A "for loop" is a common programming technique that orders a function to run its task on every item in a list. For example, you could use a for loop to scrape a certain HTML element from every website in a list of websites. You can read a for loop as, "for every item in this list, do this function."
  **Reference**                 An empty code script is like a blank slate. Very often, something needs to be defined before it can be used. To a human, you could say something like, "I want to scrape this table." But to a computer, you would first need to "define" the table.
                                When you start running functions, it's common to get an error message called a Reference Error. This means you referred to something without defining it first. Look above the line where the error occurred to find where you should have defined it.
  **Pagination**                Pagination refers to the number of pages that contain the data you're looking for. This is often a challenge in scrapes where a database or list of results is spread out among many sequential webpages.
  **Call**                      "Call" often means to execute a bit of code or to send a request to something else. For example, running a function within a script can be "calling a function," while running a script to request data from an API is referred to as an "API call."
  **Run/Execute**               To run or execute a script is to make it actually perform the task it was designed to do. This is different from printing outputs in a console, which you will most likely do before actually running a script.
                                Many people write a script in one program, like a text editor, and then run it using a different program, like the CLI.
  **Debug**                     To debug is to test a bit of code for problems - not to actually execute the script. Often a code editing tool will return error messages or print outputs in a console to help you get ready to execute it.
  **Print**                     In Python, to "print" something means to display it as an output within a console. For example, running the function print("Hello") will simply return the text "Hello" inside your console. This is different from exporting or creating an end product, like a CSV.
                                Printing can be useful for checking your work as you go along. For example, you could print a variable in your console to make sure the variable is assigned correctly. Other languages, like JavaScript, have similar functions such as console.log().
  **Chain**                     To chain commands means to use one command to accomplish another. Sometimes this method saves time and space, and sometimes it is necessary to run a function at all. A chain is written with a period (.) between two commands.
                                For instance, the chain "pandas.read_html()" tells the computer to run the read_html() function that exists inside the pandas library. Without referring to the pandas library, the Python interpreter wouldn't know what the read_html() function is.
  **String**                    A string is a sequence of characters, like the word "January" or the text "04FG8n." While they may seem simple, strings are an important step between understanding human and computer language.
                                For instance, a computer doesn't automatically know that "January" is a month - it just recognizes it as a string of seven characters. Understanding this distinction can be very influential in the success of your parsing and scraping.
  **HTML**                      HTML stands for HyperText Markup Language. Despite having "language" in the name, it is not a programming language but rather a markup language - a set of rules and syntax designed to identify and categorize bits of content on a web page.
  **Log**                       A log is like a record of activity for a script or part of a script. A log will show you, for instance, the output of a function or an error message it caused. When your scrip fails, logs are critical to understanding what went wrong
  **Read and Write**            In the programming sphere, "read" usually means to use the contents of a file without changing it, while "write" means to change it or another file.
                                In this case, "Read" is somewhat analogous to "upload" or "import," while "write" is similar to "download" or "export." For example, to import an HTML file into your script, you might use the function read_html(), but to create a new row in a spreadsheet, you could use writerow().
  ----------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  : *[Table 9.2*](#ch09.xhtml_t9_2b) Programming Glossary

:::::: section

## The Command Line

The Command Line is an application that lets you communicate with the computer via simple lines of text. It's sometimes referred to as the "console," the "terminal" or the CLI, which stands for Command Line Interface. Often, you will write a script in a program like a text editor, but then run it using the Command Line.

On a Mac, the CLI is often accessed through an application called the Terminal. On Windows, it is called the Command Prompt.

As mentioned earlier in the chapter, writing code offers many advantages, one them being the ability to write your own applications. The downside is that you will need to manually set up tasks that happen automatically in third-​party tools.

Things like exporting a dataset, or importing it into a spreadsheet, are tasks that happened automatically when we scraped data using the Google Sheets IMPORTXML function. But when you're writing your own function, you'll need to manually write code to export the scraped HTML elements into a list that you can then import into a spreadsheet.

::::: section
### Installing Languages and Libraries

When learning to code, one of the biggest challenges can be the first step: Installing the necessary tools onto your computer. While you have probably heard of programming languages like Python, it may or may not be something you need to download and install.

The Python website has instructions for downloading and updating the Python language. Some scripts and libraries work better with earlier versions of Python, in which case you might want to use something like a virtual environment. See the glossary at the end of this chapter for guidance on opening and running Python.

In addition, in order to use Python or another language for a data journalism task, you will most likely need to install additional tools inside it, like libraries. Usually, you will install or load these libraries inside the script you are writing. These add-​ons are sometimes called "dependencies" or "requirements."

One of the biggest hurdles to programming can be just getting it set up on your computer. So have patience!

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
#### Pro Tip 

When programmers share prewritten code, it often contains "documentation" -- comments or notations between lines of code that help other programmers understand what the script is doing.

As you write your own code, you should strive to maintain your own documentation, or "docs" for short. This not only helps you keep track of your own work but also makes it reproducible, meaning others can reuse your code to scrape their own websites. Writing documented, reproducible code contributes to the "open web" and makes it easier for everyone to learn and use programming.

You can find many examples of "open-​source" code and documentation on Github, the code-​sharing website.

</aside>

\* \* \*

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 3 ![](images/Exercise_Icon.jpg) 

For this exercise, we will download and install the Python language onto our computers. If you have an Apple computer, or if you have written code before, you may already have Python ready to go. Here is how to find out: open the CLI and simply type the word "python" ([Figure 9.5](#ch09.xhtml_f9_5)).


On Mac computers, the Command Line is accessed via an application called Terminal. If you can\'t find the application in Finder, just search for it using the MacOS Spotlight Search. On Windows, the application is called the Command Prompt, or cmd.exe. The easiest way to find it is by searching for "cmd" in the Start Menu.

1.  Open the CLI. It should start with a screen showing the names of your computer and your user.
2.  Type the word "python" and press enter.
3.  If the CLI returns a series of text that contains the word "Python" followed by a number, like 2.7.10, that means you have Python installed. Type "quit()" and press enter to exit the Python interface.
4.  If it returns an error message, that means you do not have Python installed. In a web browser, go to python.org and follow the instructions to download the latest version.

</aside>

::: section
## Scraping with Code

Now, we will use Python to scrape live data from social media websites. Use the glossary at the end of this chapter and [Chapter 4](#ch04.xhtml_c4), Cleaning Data, to troubleshoot your progress. First, we will scrape a Twitter user's full history of tweets using a Python library called Twint. We're going to take a look at how often the US White House tweets about China.

On a regular web browser, you would have to scroll indefinitely to load all of a user's tweets, which can number in the millions. Twitter doesn't give you an option to download all of this data from its website, but you can create an application to download your own.

If, at the end, you find you are unable to execute the file, you may want to repeat the script in the browser-​based Google Colab platform. See [Chapter 3](#ch03.xhtml_c3) for instructions on how to use Google Colab.

:::: section

## File Paths

With programming, it's important to keep all of your scripts and code files in the correct folders. To do that, you'll need to write directories. The directory, or file path, is programming-​speak for a folder or a location on your computer.

It's often written out as "user/folder/subfolder" on a Mac and "user\\folder\\subfolder" on Windows. Sometimes you will need to manually type out a directory in order to execute code.

One easy way to move around folders in the Command Line is to use the "cd" command. This stands for "Change Directory," and you can type "cd \[folder name\]" to move into any folder as long as you are currently located in the folder that contains it. In this exercise, we will use the Desktop to make navigation as simple as possible ([Figure 9.6](#ch09.xhtml_f9_6)).


<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 4 

1.  On your Desktop, right-​click and create a new folder called "python_code".
2.  In the Command Line, which we opened in Exercise 3, type "pwd" and press enter. This will return the name of the folder you are currently in.
3.  Type "ls" to see a list of files and other folders inside this folder.
4.  If "Desktop" is among them, type "cd Desktop" to move to that folder.
5.  If "Desktop" is not an option, use the "cd" command to navigate to the folder that contains it. Specifically, you can use "cd.." to move back one folder, until you find the folder that contains the Desktop.
6.  Once you are in the Desktop, enter your "python_code" folder by typing "cd python_code".
7.  Type "pwd" again to make sure you are in the correct folder.

</aside>

:::: section
## Virtual Environments

Next up on our list is to create a virtual environment. A virtual environment lets you install and deploy bits of code, and entire programming languages, within a walled area inside your computer. This helps prevent the code from affecting other parts of your machine.

For example, you may need Python version 2 to run a certain script, because the script was written before Python 3 was released. You could load Python 2 into a virtual environment and run the script in there, without replacing the Python 3 that is installed on your computer. Virtual environments are often referred to with the shorthand "venv."

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 5 

1.  Make sure you are in your python_code folder using the navigation tools we learned in Exercise 4.
2.  Type "python3 -​m venv virtualenvironment" and press enter. This will create a virtual environment in that folder.
3.  Next, we will "turn on" the virtual environment. On a Mac, type "source virtualenvironment/bin/activate" and press enter. On Windows, type "virtualenvironment\\Scripts\\activate.bat".

After these steps, you should see the text "(virtualenvironment)" at the beginning of each terminal line. This indicates that we are now operating in a virtual environment.

</aside>

::::: section

## Installing Dependencies

Our last step, before actually writing code, is to install the libraries we need. Since we are using the Twint library, we can find the install instructions on the Twint website.

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 6 

In the Command Line, make sure you are in a virtual environment using the steps in Exercise 5. Type the following commands:


    install git
    git clone https://github.com/twintproject/twint.git
    cd twint
    pip3 install. -​r requirements.txt

This will install the Twint library. Your terminal will show each component as it downloads.

We're also going to use a tool called Jupyter Notebooks, which we will use to write and then execute our code. After installing Twint, install Jupyter Notebook by typing the following command into the Command Line and pressing enter:


    pip install jupyter

Once it is done loading, type "jupyter notebook" and press enter.

This will open a notebook in a new tab of a web browser. If you want to close the notebook to continue writing in the terminal, press Ctrl+C. Later, you can open it again by typing "jupyter notebook".

</aside>
<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Pro Tip 

You will often encounter problems and need to retrace your steps to figure out what went wrong. For example, if you're unable to create a virtual environment, try the command again with "python3" instead of "python." If you're unable to install a library, try it again with "pip3" rather than "pip."

It is always easiest to copy the error message, straight out of the terminal or script, and paste it into Google.

</aside>

:::: section
## Writing a Script

Here comes the part where we write our code! A Jupyter Notebook is like a midway point between a Command Line and a point-​and-​click tool. Once a Jupyter Notebook has opened in a browser tab, you can write and run code in "cells."

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 7 

In your Jupyter Notebook, click New \< Python3 to create a new Python file. In the first cell of the Jupyter Notebook, type the following text:


    import twint
    import nest _ asyncio
    nest _ asyncio.apply()

Create a new "cell" by clicking the plus sign (+) in the Jupyter Notebook toolbar. In this second cell, type the following text:


    c = twint.Config()
    c.Username = “whitehouse”
    c.Search = “China”
    c.Limit = 100
    c.Store _ csv = True
    c.Output = “white _ house _ china _ tweets.csv”
    twint.run.Search(c)

This will use Twint to find the most recent 100 tweets by the Twitter account \@whitehouse that contain the word "China" and export them into a CSV ([Figure 9.7](#ch09.xhtml_f9_7)). This CSV will go into the python_code folder that you created. This is one reason why it\'s important to keep track of which folders contain your code, source data, outputs and work logs.


</aside>

As stated earlier, there are far too many options in programming to cover in this chapter. If you would like to learn more about how to construct a Twint search, you can find documentation on the library's website.

::: section

## Scraping with APIs

API stands for Application Programming Interface. It's a way to communicate between two applications via programming, as opposed to something non-​programming, like typing in a search term.

APIs most often come in handy in data journalism when reporters are scraping data or creating an automated task. They let the reporter's code communicate with the source automatically.

Creating your own tool to obtain data by talking directly to the source's API may not be as difficult as you think. Take an excerpt of this script by Lam Thuy Vo, who used it to scrape Facebook comments for BuzzFeed News.


    import json
    import datetime
    import csv
    import time
    import ssl
    from utils import request _ until _ succeed, open _ csv _ w
    from secrets import FACEBOOK _ APP _ ID, FACEBOOK _ APP _ SECRET
    …
    # get authentication
    access _ token = FACEBOOK _ APP _ ID + "|" + FACEBOOK _ APP _ SECRET
    …
    # Construct the URL string
        base = "https://graph.facebook.com/v2.9"
        node = "/%s/comments" % status _ id
        fields = "?fields=id,message,like _ count,created _ time,
                 comments, from,attachment"
        parameters="&order=chronological&limit=%s&access _ to-
                     ken=%s" % \	(num _ comments, access _ token)
        url = base + node + fields + parameters
    …
    def scrapeFacebookPageFeedComments(page _ id, access _ token):
      # with open('%s _ facebook _ comments.csv' % file _ id, 'wb') as
    file:
      with open _ csv _ w('../output/%s _ facebook _ comments.csv' %
    file _ id) as file:
        w = csv.writer(file)
        w.writerow(["comment _ id", "status _ id", "parent _ id",
    "comment _ message",
           "comment _ author", "comment _ published", "comment _ likes"])

Due to changes in Facebook's API, this script no longer works, but you can see how Thuy Vo used it to download the text and metadata of Facebook comments and export the data into a CSV file. The script starts by importing the required libraries, then constructing custom URLs and then scraping data points from each Facebook comment.

APIs are different from scraping HTML, like we did with IMPORTXML or using Python, like we did with Twint. An API is more like an ongoing hose of information from one application to another.

There are some limitations to them, mainly because developers don't want you to overload their site with requests. The Twitter API, for instance, limits how many tweets you can scrape at one time. You also need an API key, which you must request from the website that runs the API. Twint and csv are two useful libraries for scraping social media data, but there are many, many more.

<aside class="boxed-text2" epub:type="tip" role="doc-tip">

Find more social media scraping tools on the Journalist's Toolbox: [http://bit.ly/scrapingsocial](http://bit.ly/)

</aside>

::: section
## Footnotes

- Associated Press, Politician Used Campaign Money on Private Jets, Massages and a Katy Perry Concert [https://web.archive.org/web/2021\*/https://apnews.com/article/e2f1f52c3eb34caca7d74e5bf90f27f9](https://web.archive.org/)
- Miami Herald, US Opens Criminal Inquiry of Resigning Illinois Congressman [https://web.archive.org/web/20220519104506/https://www.miamiherald.com/news/nation-world/national/article15459164.html](https://web.archive.org/)
- PoliticsNation, Tuesday, February 24, 2015 [https://www.nbcnews.com/id/wbna57031116](https://www.nbcnews.com/)
- World Health Organization Instagram [https://www.instagram.com/p/CQWGRuQjcW\_/](https://www.instagram.com/)
- Twitonomy <https://www.twitonomy.com/>
- Twint [https://github.com/twintproject/twint](https://github.com/)
- Python Beginners Guide [https://wiki.python.org/moin/BeginnersGuide/Download](https://wiki.python.org/)
- [Python.org](http://Python.org) [python.org](http://python.org)
- BuzzFace threads.py [https://github.com/gsantia/BuzzFace/blob/master/threads.py](https://github.com/)
- BuzzFace: A News Veracity Dataset with Facebook User Commentary and Egos [https://www.aaai.org/ocs/index.php/ICWSM/ICWSM18/paper/view/17825/17046](https://www.aaai.org/)
- BuzzFace [https://github.com/gsantia/BuzzFace](https://github.com/)
- Pandas <https://pandas.pydata.org/>
- BeautifulSoup [https://www.crummy.com/software/BeautifulSoup/bs4/doc/](https://www.crummy.com/)
- pdftotext [https://github.com/jalan/pdftotext](https://github.com/)
- csv [https://docs.python.org/3/library/csv.html](https://docs.python.org/)
- t [https://github.com/sferik/t](https://github.com/)


# 10 Data Visualization

Mike Reilley

DOI: [10.4324/9781003273301-11](https://doi.org/10.4324/9781003273301-11){aria-label="D.O.I. link to this document."}

When Alvin Chang was a Vox senior reporter in 2017, he started working on a series of stories showing how the American education system exacerbates existing inequities. It was a special project because he could use data to show the extent of the problem, dig into the history that led there and explain the policies that uphold this inequality.

But it wasn't the data that got Chang interested in this story.

Halfway through Chang's project, Tomas Monarrez, then a University of California at Berkeley postdoctoral student, contacted him to say that he had a study that showed that American school districts were drawing attendance zones to make racial segregation worse.

What intrigued Chang was that Monarrez had data on nearly every single public elementary school. But after a few hours of trying to make sense of his work, Chang realized what made this study special was *how* he was determining whether a district was making segregation worse.

Chang saw something in Monarrez's thinking that ultimately drove the story: If every American child went to the public school closest to where they live, schools would be very racially segregated because government policies of the past made our neighborhoods very segregated. But what Monarrez found was that many school districts drew their school zones to make school even more segregated than the underlying neighborhood. They had an opportunity to lessen the existing segregation, but instead they used this power to keep the systemically racist status quo.

The data for that story was crucial, but it is the visual explanations that made the piece work, said Chang, now the head of visuals and data for *The Guardian US*. He knew the story was powerful -- ​but only if he could explain the methodology in a way that conveyed the stakes.

The project included a feature where readers could look up their school district. But by the time they looked it up, Chang wanted them to recognize that their lives were shaped by school segregation. He wanted them to internalize that their school boards actively made a decision to put them in a classroom with kids of the same racial and class backgrounds, which is no different than what our schools were doing before the civil rights movement ([Figure 10.1](#ch10.xhtml_f10_1)).


Infographics are like glasses, says Alberto Cairo, who teaches data visualization at the University of Miami. If you take your glasses off, everything is blurry, but with your glasses on, everything comes into focus and makes sense.

This chapter discusses various types of interactive and animated charts and maps and how professional data journalists build them. It explains how to know which type of chart or map is right for your data. It explores how to choose the right colors, fonts and the size for your graphic. Using Flourish, Datawrapper and real-​world data, we will walk through the process of making a variety of charts and maps with exercises and training videos.

\* \* \*

::: section

## Building Charts: Types of Charts

A good chart can make readers smarter. They show trends and patterns that might not be obvious when looking at numbers in raw data. But, as Cairo has pointed out, charts can lie. And charts can be confusing or misleading, especially if the journalist chooses the wrong chart to present the data. There are dozens of types of charts available, so to get started, let's focus some of the basic charts and what data they can visualize.

::: section
## ![](images/Bar_Graph_Icon.jpg) Bar/Column Chart

Horizontal bar charts -- ​or vertical column charts -- ​feature rectangular bars with heights or lengths proportional to the values that they represent.

They're often used to compare year-​to-​year figures, percentages, etc., usually over time or between entities. For instance, it can show an increase in campaign contributions to a candidate over a 12-​month period or an increase in COVID-​19 positive tests over a few weeks.

::: section

## ![](images/Line_Chart_Icon.jpg) Line Charts

A line chart displays information as a series of data points called markers (data points) that are connected by straight or curved lines. Line charts are popular for sports data and stock market/finance charts as these show an asset's historical price action that connects a series of data points with a continuous line. The charts show continuous growth or decrease over a scale (typically time).

Line charts and bar charts can be interchangeable with some datasets, but bar charts break out individual points (years, etc.), whereas line charts represent continuous growth and change.

::: section
## ![](images/Pie_Graph_Icon.jpg) Pie Charts and Treemaps

These are typically used for budgets or breaking down parts of a whole. The "pieces of the pie" must be proportional to the data corresponding with it. So if 10 percent of a city budget is going to the police department, the proportion in the graphic should amass 10 percent of the overall chart (or pie).

Treemaps are a popular and effective way to break down a budget and other data. They are ideal for displaying large amounts of hierarchically structured (tree-​structured) data. The space in the visualization is split up into nested figures, usually rectangles that are sized and ordered by a quantitative variable. Example: Treemap (Shortlink: [https://bit.ly/treemapexample](https://bit.ly/)).

::: section

## ![](images/Interactive_Chart_Icon.jpg) Interactive and Animated Charts

Interactive charts allow the user to control what they see: for instance, zooming, hovering over a marker and using a search bar or a pulldown menu. It can also enable the exploration of data via the manipulation of chart images, with the color, brightness, size, etc. This gets the reader engaged and *involved* in the data.

Animated charts illustrate data by creating changes and movements in the chart. Changes over time are a great way to use animated graphics, for example:

- 2020 COVID-​19 Cases by State and Country (Shortlink: [https://bit.ly/covidcaseschart](https://bit.ly/))
- Baseball Home Runs in the Steroid Era [https://public.flourish.studio/visualisation/8443792/](https://public.flourish.studio/)

::: section
## ![](images/Venn_Diagram_Icon.jpg) Venn Diagrams

Lucidchart defines Venn diagrams as "overlapping circles or other shapes to illustrate the logical relationships between two or more sets of items. Often, they serve to graphically organize things, highlighting how the items are similar and different." Common elements of the sets are represented by the areas of overlap among the circles, which shows relationships or common areas of interest.

::: section

## ![](images/Hierarchy_Icon.jpg) Hierarchy and Organizational Charts

According to [OrgCharting.com](http://OrgCharting.com), hierarchical charts are typically used to show roles, ranks, levels or positions of people or things. They are designed in a format that shows the relationships between the entities, with the top of the chart typically kept for the most important or significant part of the system. These diagrams look like organizational charts in some ways, and you can use org chart makers to draw hierarchy charts as well.

There are many other types of charts -- ​timelines, scatterplots, etc. Be sure to look through chart libraries in tools like Flourish, Datawrapper and other tools we explore later in this chapter to find more templates and designs. Many of the templates have "dummy data" in them so you can see how to format the spreadsheet to make the chart work seamlessly.

:::::: section
## Visualizing a Story on Deadline

Journalists often think of data as structured numbers, but Chang said he believes text transcripts are some of the best data sources for journalists. The downside is that text analysis often returns murky and inconclusive results. But that was not the case for the Senate testimony of Supreme Court nominee Brett Kavanaugh and the woman accusing him of sexual assault, Christine Blasey Ford.

The morning after the hearing, Chang sat in bed reading through the transcript and noticed the extent to which Kavanaugh was unwilling to answer any questions about the allegations. He knew his biggest challenge for this story was going to be time: The window of interest for this story would be that morning, so he devised a plan that would allow him to finish relatively quickly.

First, he pasted the transcript into a text editor and started to denote the questions Kavanaugh and Ford answered and didn't answer. He read through the transcript several times to make sure his coding was correct.

Next, he visualized the data using a technique he had used in the past: Put the entire transcript onto the page, shrink the text to 1px and color the lines based on the coding. When he first saw the visual, his jaw dropped: Kavanaugh dodged a huge number of questions, while Ford answered all of them ([Figure 10.2](#ch10.xhtml_f10_2)).


This project was a good reminder that useful data analysis doesn't have to involve complex statistical methods. Chang published the story, took a shower and, when he got back to his computer, the visualization had gone viral and was being shown on several TV news shows.

Andy Boyle, former director of product engineering at the *Chicago Sun-​Times*, and his data team tackle the issue of homicides in the Windy City on both a daily and long-​term basis, which presents a variety of challenges.

Their Chicago homicide victims database lists the names of everyone killed by another person in the city of Chicago and is updated multiple times a day.

"While these dots on a map represent data points, what they really represent are human beings who've lost their lives," Boyle said. "They represent families, friends, people who feel the pain from the loss of a loved one. That's what we're hoping also gets conveyed when you look at this data, the human impact."

People are killed almost every day in Chicago, and the rates have gone up substantially since 2019. The *Sun-​Times* has a team of dedicated reporters who work around the clock covering shootings, homicides and other breaking news events, who spend time filling out a spreadsheet tracking the homicides as we learn about them ([Figure 10.3](#ch10.xhtml_f10_3)).


<aside class="boxed-text2" epub:type="tip" role="doc-tip">

::: section
### Tips for Creating Data Visualizations 

From **Alvin Chang, *Guardian US***

- **Remember that data isn't just numbers**; the numbers are descriptions of things in the real world. This is why it's so important to first understand what each column of your data is describing.
- **Your data viz doesn't have to tell people what to think**, but your design decisions should tell people what to look at. Not making that decision is also a decision -- ​but often the worst one, because that means you haven't fully grappled with what the reader should learn from your visualization.
- **Simple charts** are often the best. Bar charts and line charts are great.
- **There are many guidelines** for data visualization, but nothing beats showing your visuals to a bunch of people and asking them if their experience is what you intended. Sometimes, you can follow all the rules and still fail to communicate what you intended.
- **It can feel overwhelming** to think about the technical skills you need to learn in order to make a data visualization. But learning something new can be a wonderful experience, even if the end product isn't exactly what you had hoped to create. If you're willing to be bad at something, that means you're on the path to being good at it.

</aside>

Sometimes, Boyle said, they get the information from hearing about it over the police scanners and sometimes through press releases. Sometimes they don't find out until days later, when the body shows up at the Cook County Medical Examiner's Office.

Inaccuracy and discrepancies in how police classify homicide data is another issue. For instance, any homicides that occur on Chicago expressways aren't investigated by Chicago police but the Illinois State Police. So when the city of Chicago reports its homicide statistics, it does not include the homicides on the expressways, even though they occur well within city limits. They also don't always include cases the Medical Examiner's Office has deemed a homicide, but the Chicago Police Department either isn't the investigatory agency or disagrees with the medical examiner's office's findings, Boyle said.

"Our job is to try and give people the most accurate account of how many people were homicide victims within the city's limits," he said. "While our tracker doesn't track every single one -- ​and sometimes we do miss them -- ​our goal is to try and get as many as possible" ([Figure 10.4](#ch10.xhtml_f10_4)).


The database updates regularly, so within 10 minutes of a new homicide being added, the information flows into the graphic. They try to track as much information as possible about the homicide: Where did the incident occur? What was the cause? Shooting? Stabbing? Other? What was the person's ethnicity or race, their age, their gender?

Readers can filter this information, so they can look at individual community areas, which is a Chicago statistical area that's more or less like a large neighborhood grouping (Chicago has 77), or drill down by some of the other information.

<aside class="boxed-text2" epub:type="tip" role="doc-tip">

::: section
### Creating Data Graphics for TV 

**John Walton, BBC News**

There are a lot of similarities when working on graphics for broadcast and working on graphics for smartphones. Although broadcast tends toward landscape and smartphones tend toward portrait, both platforms have very limited space.

For simple charts, reducing using larger fonts and writing shorter titles aids reader understanding. You also can make the same basic chart usable for both digital and broadcast platforms when using graphics produced from code.

The BBC Data Team doesn't produce all the charts that get used on the broadcast by any means, but when they have a script set up and can offer colleagues a version of something they have made online, they pass it on for broadcast.

Although online has the advantage of more space, which means graphics can be a little more detailed, broadcast has the great strength of having a human voice to talk viewers through what they're seeing, which can be invaluable to aid understanding.

**LEARN MORE:** Walton recommends watching videos of data visualization expert Hans Rosling for a master class on how to talk to people about graphics. Rosling has done many TedEd talks on data visualizations, including this one (Shortlink: [https://bit.ly/roslingvideo](https://bit.ly/)).

</aside>

Becky Dale and Nassos Stylianou, data journalists on the BBC's Data Team, built a project in 2021 for both the BBC digital and broadcast departments. "Climate Change: World Now Sees Twice as Many Days over 50C" was developed as part of a BBC World Service series of programs and reports looking at climate change.

To create a data story for the series, Dale and Stylianou examined climate data to test the hypothesis that the number of days seeing temperatures of over 50 degrees Celsius (122 degrees Fahrenheit) was rising.

Walton said the guiding principle was to make climate change, which can sometimes be rather technical, readily understood. So, choosing the metric of days experiencing highs of over 50 degrees Celsius was a way of framing the story in a familiar way rather than expressing climate change as an increase in temperatures against a long-​term average above preindustrial levels. While the idea was simple, execution was not. It required the reporters to analyze more than *15 billion* data points.

"Their analysis had not been attempted by any other news organization, or indeed, by climate scientists," Walton said.

> So, Becky and Nassos had to work out a robust methodology to tackle the question. This led to them seeking support and advice from the University of Oxford, Berkeley Earth, Carbon Brief, the University of Reading, the UK Met Office and the Copernicus Climate Change Service.

<aside class="boxed-text2" epub:type="tip" role="doc-tip">

For more data visualization tips, tricks and exercises, visit the Data + Journalism blog at <http://dataplusjournalism.com>

</aside>

They also had to work with file types and data formats specific to climate science. The analysis and visualization were produced in 19 languages, for the BBC World Service, including Arabic, Persian, Punjabi, Chinese and Spanish.

Having delved deeply into a difficult and demanding piece of data analysis, Dale and Stylianou took a step back and thought about how best to convey their findings in a simple and engaging way to a general audience, Walton said.

Working with designers, they decided on a time series displayed on both a map and a bar chart at the same time. The map and the bar chart animate in tandem to show how many days had experienced these extreme temperatures and also to show how many areas around the planet were affected ([Figure 10.5](#ch10.xhtml_f10_5)).


Besides their work on the *Chicago Sun-​Times* daily homicide victims database, Boyle and data visualization developer Jesse Howe also build long-​term projects with homicide data. At the end of the calendar year, the *Sun-​Times* compiles all of the homicide data for that year and presents a series of graphics with an in-​depth story.

Their project at the end of 2021 focused on Chicago's most dangerous neighborhoods. They built a series of interactive choropleth maps that showed homicides by police districts and by neighborhoods. They built a line chart that compared the city's safest and most dangerous neighborhoods for homicides.

They also produced a line chart comparing the last decade of annual homicide data that showed 2021 -- ​with just shy of 800 homicides -- ​ranked as one of the worst in several years. Another line chart underscored another dangerous trend: Homicides peak during the hot, humid summer months in Chicago.

<aside class="boxed-text2" epub:type="tip" role="doc-tip">

::: section
### Creating Data Visualizations 

**Tips from John Walton, BBC News**

- **At the start, ask yourself: Will my data visualization tell the story better than words?** If not, ditch it. Graphics take time and effort to make, so it is best to only produce them when they will definitely add something to your story or project. A picture paints a thousand words, and your graphic should do the same.
- **Before you start cleaning**, sorting, filtering and analyzing the data, remember to always keep an original copy for reference, preserved in its pristine and unaltered state.
- **Think hard about your audience and be empathetic.** Will they understand your graphic? Average levels of number literacy may not be as high as you think, and your audience may be less used to reading charts and visualizations than you and your colleagues.
- **Where will people be looking at my data visualization?** Is your audience most likely to be looking at your chart on a phone, desktop or on broadcast? Each platform gives you a different canvas to work on. Mobile and broadcast demand clear and simple graphics, while desktop and print can offer more scope for detail.
- **Sometimes, data may just be too flawed to be of any use.** It may be incomplete, too old, collected poorly and in a partial manner. Whether you want to use data of this kind is a judgment call that can vary project by project.
- **If in doubt, always ask yourself:** "Does writing up or visualizing this data help people's understanding of the topic at hand?" If the answer's a straight "no," then it may be best to find another way to tell that particular story.

</aside>

::: section

## Building Charts and Maps

Lena Groeger, an award-​winning visual journalist, developed a framework for designing infographics that can pack a punch but still be easily understood by the viewer. She says whenever you are designing an infographic, ask yourself two simple questions:

- What is the audience supposed to understand, visually?
- What is that visual perception supposed to represent?

Take a line chart. When a reader looks at a line moving across an axis, what are they looking for? Quite simply, whether the line goes up and down. Second, what is that up or down line supposed to represent? The chart's title, caption and axis labels make this clear.

An upward-​trending line, typically, indicates an increase in whatever variable is named in the chart description. A downward line, of course, represents a decrease. In a real line chart, this line will most likely trend both up and down, but the audience is still able to ingest the information at a glance. That's one of the main reasons behind representing information in a visual form to begin with.

These are not hard-​and-​fast rules. Some line charts, for instance, use an inverted *Y*-​axis, meaning a downward line indicates an *increase* in the variable. But these are rare and can be confusing to the viewer. Even if you do not *have* to model your chart along the most typical methods, it is the simplest way to convey information to the audience.

If you find your own chart confusing, or are looking for the clearest way to convey information, ask yourself: What is the audience seeing at a glance? What are they supposed to take away from that glance? Sometimes this framework can help you figure out which kind of chart to use -- ​a pie chart, a bar chart, etc. Often, this will result in cutting out extraneous information, just like you would cut unnecessary details from a text story.

Cairo wrote in his book, *How Charts Lie*, that to understand a chart, readers must focus on "features that surround the content and support it -- ​the chart's scaffolding -- ​and on the content itself (how the data is represented or encoded)." A chart or map's "scaffolding" can go a long way in building trust with readers, an issue we explore in-​depth in [Chapter 11](#ch11.xhtml_c11). For instance, during the COVID-​19 pandemic, social media feeds filled with fake news charts and maps misrepresenting data for various countries, states, etc. Many of these graphics had little or no scaffolding and rarely had a link to source data or a credit. Without those key elements, readers should question the graphic's credibility.

Data journalists must consider form, function and scale when designing charts and maps: The function is the data, conveying the information to the reader. The form is the presentation of the data in pictorial or graphic format. Cairo believes that the questions the designer means for the reader to ponder dictate the form or, at the very least, constrain it to a limited set of choices. Because the function limits the form, the formula for a graphic's success is simple: Bad function (data) = bad form (graphic).

Scale matters as well. A dot on a bubble map must be sized in proportion to the data and other points on the map. The same is true for a bar chart: If data in a bar chart showing COVID-​19 positive cases shows China has four times as many cases as the US, the bar for China should be four times as long as the bar for the US. Skewing that, Cairo argues, is to mislead the reader.

"The same way that a long, deep and complex sentence can't be understood in the blink of an eye, charts that display rich and worthwhile information will often demand some work from \[readers\]," Cairo wrote.

That's why titles, introductions, footers with credits and source information, annotations, legends and scales are so important for charts and maps. They expedite the reader's understanding.

Once you're ready to create a visualization for a story, follow a simple process:

1.  Think of the idea: What story do you want to tell?
2.  Research the story and pull datasets.
3.  Sketch what you want to do with the graphic.
4.  Find a template (or a blank graphic) on the data viz software you want to use.
5.  Begin your design, prioritizing the most important datasets at the top.
6.  Add titles, descriptions, credits and sources to the chart.
7.  Publish and export it, or download it as a png image.
8.  Post to your site and share over social channels.

::: section
## Choosing the Right Chart

For journalists who are new to data visualizations, choosing the right chart to represent the data can be a challenge. When do I use a bar chart? A line chart? Is it best as a map? Or do I need a chart at all -- ​is the data better presented as a database, list or written into the story?

These are all questions journalists face when planning charts and infographics for their stories. There are a few approaches to take.

1.  Before opening any software, sketch your graphic on scratch paper first. Think through the *X*-​axis and *Y*-​axis. Use labels. Even write the title. This will bring the chart into focus. This is an important, often-​overlooked step that can save time in the long run.
2.  Try testing a dataset in the Explorer tab in the lower-​right corner of Google Sheets or in the charts tool in Microsoft Excel before loading the data into other software. These spreadsheet visualization tools do a good job of evaluating the data and selecting a chart to match. This is a quick, effortless step that can save you much time down the road.
3.  Look at chart-​building tools such as Flourish.studio or [Datawrapper.de](http://Datawrapper.de) for clues on how to structure a dataset to fit that particular template. Flourish templates all contain "dummy data" -- ​raw data that has been made up -- ​that helps you see the correct format to set up your spreadsheet.
4.  If you are just starting out in a newsroom, ask for help from the graphics editor or a veteran data journalist.
5.  Try using a visual guide, such as the Financial Times Visual Vocabulary cheat sheet, that is available as a handout, poster and more on Github. There are many other tools for chart selection on the Journalist's Toolbox.

::: section

## Choosing Colors and Fonts

Gradients and color shades are key to choropleth maps. For example, if you're building a map of COVID-​19 positive cases by country, the countries with more cases should be a darker shade than those with fewer cases. This, along with a legend, helps the reader understand the density of cases. The same holds true with a bubble map. The larger the bubble, the higher the density. But the bubble size must be proportional to the data in the other countries, states, cities, etc., so as not to misrepresent the data.

Some of your color choices are simple: Green and earthy tones for environmental graphics, for instance. But try to avoid other color combinations: Red for homicide and other crime statistics as readers identify it with blood, red and green mean Christmas to many readers and red and yellow are identified with McDonalds.

While choosing colors for your visualizations is hard, choosing colorblind-​safe colors is harder. In a three-​part blog post, Datawrapper offers great advice for taking colorblindness and color weakness into consideration.

For example, a red-​ and green-​blind person has problems distinguishing between red, green and brown, if their brightness is the same. Red and green might look gray to people who are red-​ and green-​colorblind. Same with purple and blue.

Datawrapper, Flourish and many other chart-​making tools take this into consideration and offer colorblind options when building charts and maps. The tools can usually be found on the main interface of your graphic workspace.

::::: section
## Chart-​Building Tools

There are hundreds of chart and infographic creation tools on the Internet. Many are free, or some cost a nominal fee.

Adobe Illustrator is a vector-​graphic building tool that has existed since 1985 and remains popular today. It's costly, but Adobe offers free trials through its Creative Cloud.

RStudio, which we explored in a previous chapter, offers chart-​making features as part of its open-​source integrated development environment for R. But for newbies, the point-​and-​click tools are a good start.

Here are a few of the easiest to use:

- Flourish and Datawrapper are among the most versatile and popular tools, and they offer free and paid versions.
- Infogr.am, Venngage and Canva offer basic infographic tools and are very intuitive. The Google Public Data Explorer lets you build graphics by linking directly to datasets, so no coding or spreadsheets are required.
- Tableau Public gives users more versatility by creating multiple graphics and maps from a single dataset and then merging them together into a single interactive "dashboard" that can be filtered or sorted to focus on a specific part of the data (city, ZIP code, etc.). In essence, it combines databases, charts and maps into one interface and offers advanced storytelling features. The tool was popular for building COVID-​19 dashboards during the early days of the pandemic.
- **Mobile tools:** Phone and tablet apps such as Chartistic, Icongraph and Viz provide infographic and static chart-​making tools. Canva also has a phone app, although the desktop version offers more control over design and is more intuitive to use.

<aside class="boxed-text2" epub:type="tip" role="doc-tip">

::: section
### Chart Exercises 

We have prepared several chart-​building exercises for you on these YouTube videos (shortlink: [https://bit.ly/djvideos](https://bit.ly/)). Simply select the tool you want to learn, and follow the directions in the video to set up the account, download the data and exercise and produce the chart. All data used in the examples are real, so you can publish and share your work when you are done.

1.  Flourish chart
2.  Datawrapper bar chart
3.  Venngage infographic
4.  Tableau Public chart and dashboard
5.  Tableau Public: Adding filters to a dashboard

Find all of the training videos at this link: [https://bit.ly/djvideos](https://bit.ly/), and experiment more with Flourish charts on this exercise: [http://bit.ly/googleflourish](http://bit.ly/)

</aside>

::: section
### Mapping

Like charts, a great map can tell a story on its own. A well-​crafted interactive map distinguishes itself from a print map in many ways. First, the map needs to reward the reader for clicking on it, whether it be a pinpoint, search button, zoom bar or a shape. When readers click, they expect to find more than just a number that we would see on a two-​dimensional map. So a good interactive map should contain a combination of the following:

1.  Multiple data points about the location
2.  Address or longitude--​latitude
3.  A short paragraph about the location or a link to read more
4.  Multimedia, if available: photos, video or audio

A map doesn't need all four elements, but a combination of at least two, to give the reader a deeper understanding of an issue. For instance, simply placing pinpoints of homicide locations on a map of Chicago isn't enough. Layering in a shapefile of Chicago neighborhoods or ZIP codes, making it searchable and adding a background paragraph or link to a news story from each pinpoint create a much more robust story.

::: section

## Types of Maps

There are dozens of different types of maps that you can use to tell a story, but these are some that are most commonly used by journalists:

- **Pin map:** The most common type of interactive map uses geocoding to assign map coordinate locations and provide data about that location. This is typically done through loading a spreadsheet into a tool such as Google MyMaps, [Carto.com](http://Carto.com) or another mapping tool. The map will geocode city names, names of buildings, street addresses, longitude--​latitude, postal codes and more.

- **Cluster map:** Also known as a bubble map, a cluster map is an excellent alternative to a pin map that might have several tightly packed markers together in one area, according to Maptive. So instead of a large conglomerate of pins, you get a clean cluster icon that displays key information and corresponds with the number of markers contained in it. Zooming in reveals individual markers that are clickable.

- **Choropleth map:** Popular during the COVID-​19 pandemic, these maps shade areas based on a value. For example, a country with more positive COVID-​19 cases is shaded darker than a country with fewer. A legend typically shows the gradient scale and range of the data. They're common because they are easy for readers to understand ([Figure 10.6](#ch10.xhtml_f10_6)).


- **Symbol map:** This map appends symbols that show location or another form of data that can be applied to geographical locations. Tableau Public cites symbol maps as a way to point out the cities that have been hit by hurricanes throughout a period of time with each symbol sized (scaled) to indicate the total number of hurricanes.

- **Locator map:** This map shows the location of a particular geographic area within its larger and presumably more familiar context. The map can be used on its own or as an inset for a larger map. For instance, highlighting Ireland in a map of the world to show its location.

- **Heat map:** Unlike choropleth maps, heat maps are not tied to a boundary. Instead, they have a color code using the density of points. If there is a high density of crimes in an area, it shades the area as red. Fewer cases are orange, yellow, etc.

::: section
## Geographic Information System Maps and Shapefiles

A Geographic Information System, or GIS, is a visual representation of quantifiable data that allows you to layer information on top of the map. These are usually shapefiles, such as Keyhole Markup Language (.KML) or another format that represents a shape such as a state, county, neighborhood, ZIP code or some other geospatial shape. They can be layered behind pinpoints on a map, such as homicides by a specific police precinct. Or they can be shaded to show density.

:::: section

## Building Maps: Tools

The Journalist's Toolbox website lists dozens of free and low-​cost mapping tools. Some of the most common mapping tools used by journalists include ArcGIS, the cloud-​based mapping software from Esri; [Carto.com](http://Carto.com) (great for animated time-​lapse maps); Google MyMaps; Open Street Map; MapBox; Maptive; StoryMap JS and Tableau Public, among many others. Flourish and Datawrapper are among the most popular as they have simple choropleth, symbol and locator map templates that are intuitive and easy to use.

MyMaps is one of the most basic tools for map-​building. It will handle a spreadsheet of data up to 1,000 rows and geolocate the addresses or other location data in the map. It allows for layering shapefiles and offers nine different base maps. Developers have control over shapes of the pinpoints and colors and can easily integrate text, images and videos into the pinpoints. The exercises in this chapter will get you started with this tool.

\* \* \*

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercises 

We have prepared several map-​building exercises for you on these YouTube videos (shortlink: [https://bit.ly/djmapvideos](https://bit.ly/)). Simply select the tool you want to learn and follow the directions in the video to set up the account, download the data and exercise and produce the chart. All data used in the examples are real, so you can publish and share your work when you are done.

1.  Google MyMaps
2.  Datawrapper choropleth and locator maps
3.  Tableau Public filtered maps
4.  Find all of the training videos and more on this YouTube playlist: [https://bit.ly/djmapvideos](https://bit.ly/)

</aside>

::: section
## Tools Used in This Chapter

Flourish <https://flourish.studio/>

Datawrapper <https://www.datawrapper.de/>

Infogra.am <https://infogram.com/>

Venngage <https://venngage.com/>

Canva <https://www.canva.com/>

Google Public Data Explorer [https://www.google.com/publicdata/directory](https://www.google.com/)

Tableau Public [https://public.tableau.com/en-​us/s/](https://public.tableau.com/)

Chartistic [https://apps.apple.com/us/app/chartistic-​charting-​app/id1127272574](https://apps.apple.com/)

Icongraph <https://www.icongraph.com/>

Viz App (iOS only) [https://apps.apple.com/gb/app/viz/id678141110](https://apps.apple.com/)

Google MyMaps <https://mymaps.google.com/>

Open Street Map <https://www.openstreetmap.org/>

ArcGIS [https://www.esri.com/en-​us/arcgis/about-​arcgis/overview](https://www.esri.com/)

[Carto.com](http://Carto.com) <https://carto.com/>

Open Street Map <https://www.openstreetmap.org/>

MapBox <https://www.mapbox.com/>

Maptive <https://www.maptive.com/>

StoryMap JS <https://storymap.knightlab.com/>

\* \* \*


## Footnotes

- Vox, We Can Draw School Zones to Make Classrooms Less Segregated: This Is How Well Your District Does [https://www.vox.com/2018/1/8/16822374/school-segregation-gerrymander-map](https://www.vox.com/)
- [AlbertoCairo.com](http://AlbertoCairo.com)
- Infographics Formula by Alberto Cairo [https://mindthegraph.com/blog/infographics-alberto-cairo/](https://mindthegraph.com/)
- BBC UK, How Many Coronavirus Cases Are There in My Area? [https://www.bbc.com/news/uk-51768274](https://www.bbc.com/)
- Chartbeat, Most Engaging Stories of 2020 [https://blog.chartbeat.com/2020/12/22/most-engaging-stories-2020/](https://blog.chartbeat.com/)
- BBC, Climate Change: World Now Sees Twice as Many Days Over 50C [https://www.bbc.co.uk/news/science-environment-58494641](https://www.bbc.co.uk/)
- Chicago Homicides Victims Database [https://graphics.suntimes.com/homicides/](https://graphics.suntimes.com/)
- Chicago Sun-Times Year-End Violence Story and Graphics (2021) [https://bit.ly/csthomicides](https://bit.ly/)
- Lena Groeger, What is Wrong with This Chart? [http://lenagroeger.s3.amazonaws.com/newschool/WrongWThisChart.pdf](http://lenagroeger.s3.amazonaws.com/)
- Alberto Cairo, How Charts Lie, pages 24, 34--36, 40 and 47
- *American Journalism Review*: Journalism Professors Used Legos to Teach Super Bowl Data Visualization [https://ajr.org/2015/02/02/journalism-professors-used-legos-teach-super-bowl-data-visualization/](https://ajr.org/)
- Financial Times Visual Vocabulary Cheat Sheet [https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary](https://github.com/)
- Journalist's Toolbox: Choosing the Right Chart [https://www.journaliststoolbox.org/2021/11/25/choosing-the-right-chart/](https://www.journaliststoolbox.org/)
- Datawrapper: How Your Colorblind and Colorweak Readers See Your Colors [https://blog.datawrapper.de/colorblindness-part1/](https://blog.datawrapper.de/)
- 2022 Chicago City Budget Treemap [https://public.flourish.studio/visualisation/8988206/](https://public.flourish.studio/)
- Lucid Charts: Venn Diagram Tutorial [https://www.lucidchart.com/pages/tutorial/venn-diagram](https://www.lucidchart.com/)
- [OrgCharting.com](http://OrgCharting.com): Hierarchy Charts [http://www.orgcharting.com/what-is-a-hierarchy-chart/](http://www.orgcharting.com/)
- Journalist's Toolbox: Charts and Infographics [https://www.journaliststoolbox.org/2022/05/16/online_journalism/](https://www.journaliststoolbox.org/)
- Tableau Public Dashboard: Chicago COVID-19 Cases by ZIP code [http://redlineproject.org/timeline/coviddashboard.php](http://redlineproject.org/)
- YouTube: Building a Flourish Chart [https://www.youtube.com/watch?v=qD2SBLvmuWE](https://www.youtube.com/)
- YouTube: Datawrapper Bar Charts [https://www.youtube.com/watch?v=pHm7V9CaKfM](https://www.youtube.com/)
- YouTube: Venngage Infographic Exercise [https://www.youtube.com/watch?v=a4xOQXFddVU&feature=youtu.be](https://www.youtube.com/)
- YouTube: Tableau Public Chart and Dashboard [https://www.youtube.com/watch?v=vTedRGIlMGY](https://www.youtube.com/)
- YouTube: Tableau Public -- Adding Filters [https://www.youtube.com/watch?v=QbmEhUNgX9s](https://www.youtube.com/)
- Google Flourish Exercises [http://bit.ly/googleflourish](http://bit.ly/)
- Earth Observing System [https://eos.com/blog/gis-mapping/](https://eos.com/)
- Tableau Public: Symbol Maps [https://www.tableau.com/data-insights/reference-library/visual-analytics/geospatial/symbol-maps](https://www.tableau.com/)


# 11 Ethics, Trust, Transparency and Posting Data Online

Mike Reilley

DOI: [10.4324/9781003273301-12](https://doi.org/10.4324/9781003273301-12){aria-label="D.O.I. link to this document."}

Ethical decision-​making with data stories can be tricky, so let's start with an exercise.

Let's say you are a data journalist at a local news outlet. You just downloaded your state's or region's gun license database from a data portal. As you sort through the spreadsheet, you see that you have addresses of everyone throughout the state/region who has been approved for a gun license (or in states like Illinois, a Firearm ID card). You decide that you could map this dataset and post it to your media outlet's website. You then decide to make the dataset searchable by posting it in a searchable template in Google Flourish or Datawrapper.

You embed both the map and the database in your content management system and publish them. You share them on social channels, post on Reddit and link to it off your site's home page. You go home feeling good that you've provided a great service to your community, right?

Fast-​forward to a few weeks later. Your crime reporter stops by your desk and mentions a series of break-​ins to homes in your community. The thieves are stealing guns. During questioning, police ask one of the suspects they caught how they knew where to find the right homes. The answer: Your map and searchable database of gun licenses.

This anecdote underscores the importance of thinking through not just the accuracy of data but what your audience can do with the data or visualization once it's published. Will it be used for good? For harm? Could it endanger someone?

These are tough, but necessary, questions to ask when planning data projects, particularly those involving public safety and crime. There are many resources that offer broad guidance when reporting with data. The Society of Professional Journalists (SPJ) provides the oldest and most broad-​based code of ethics available online or in downloadable, printable PDFs.

In the case of the gun licenses, the SPJ Code of Ethics addresses a few key areas:

- **Balance the public's need for information** against potential harm or discomfort. Pursuit of the news is not a license for arrogance or undue intrusiveness. In this case, the public's need to know where the gun owners lived was not critical to any story. The map and gun license database had no context. There was no story on an increase in crime in the area, and even then the need for a database is highly questionable. What public service does it serve? Does the public really need to know this information?

  Had the reporter been doing a story on an increase in gun licenses in an area of a city or region, analysis of the gun database would be appropriate. But the results *only* should be shared in the aggregate: "Cook County had a 20 percent increase in gun license applications from 2021 to 2022." By publishing the locations of the gun license applicants, it gave criminals a road map to find them, a classic example of causing harm.

- **Provide context. Take special care not to misrepresent or oversimplify in promoting, previewing or summarizing a story.** With the gun database, a simple phone call to local authorities would provide some much-​needed context: Most crimes aren't committed by legal gun owners but by criminals using stolen or black market firearms. By posting the database and map without context, it misrepresented the issue.

Data also can be manipulated and misrepresented just like any fact or quote. Journalists should always show extra care if working with data, as mistakes and ethical issues can arise in ways that are different from other stories. The SPJ Code of Ethics addresses this: *Never deliberately distort facts or context, including visual information. Clearly label illustrations and re-​enactments.* While this applies to photojournalists as well, data journalists should take this entry to heart.

*The Reader on Data Visualization* says that the topic of ethics in data visualization is not something that comes to the fore when we start working. It is rarely the case that one sets out to deceive without altering data. The topic of good ethics in data visualization is very important and it is the duty of the creator to take care of it.

Alberto Cairo, who teaches data journalism at the University of Miami in Florida, wrote a book, *How Charts Lie*, that addresses many ethical issues in presenting data visually. "Charts lie in a variety of ways -- ​displaying inaccurate data, oversimplifying stories and suggesting misleading patterns -- ​or are frequently misunderstood, such as the cone of uncertainty maps shown on TV every hurricane season."

To Cairo, data visualization is where journalism and engineering share a beer. Journalists who build graphics are "information engineers" similar to software developers or industrial designers.

"For us the information is as important as the effectiveness and efficiency of the displays we devise to convey it," Cairo wrote in a 2014 article titled "Ethical Infographics." "When we create a visualization, we're giving information a visual shape, we model it, we sculpt it. There should be a connection between the forms we choose and the tasks that our visualization is intended to facilitate.

"Creating a visualization isn't just an act of journalism, but also of engineering. To think about the ethics of news visualization -- ​a field waiting to be developed -- ​is to go beyond the grand themes traditionally covered in the literature on journalism ethics and to explore matters of effectiveness and efficiency. Journalists who design visualizations need to address questions related to what they should display and why, but also pay in-​ creased attention to how they should display it. In other words, visualization designers must think about the structures, styles and graphic forms that let audiences access information successfully in every situation."

This means double-​checking the *Y*-​axis on a bar or line chart to make sure the scale doesn't misrepresent the data. It means area maps can misrepresent geography and density if not placed in proper context. And it means pausing for a moment to think about the impact the data, visuals or story could have on your readers or viewers."

::: section
## The Importance of Transparency and Trust-​Building

Marilia Gehrke, a professor at Universidade Federal do Rio Grande do Sul, presented a paper at the 2020 Computation + Journalism Symposium titled "Transparency as a Key Element of Data Journalism." The paper focused on the growing need for transparency in data journalism in Brazil and globally. Gehrke wrote:

> In recent years, especially because of disinformation, transparency has been an important part of journalists' work. Transparent conduct involves opening methods and procedures of reporting. It means, overall, showing the audience how the information was obtained and verified until being published.

She interviewed 36 journalists, most of them data journalists who have been working in newsrooms for more than 10 years.

"A significant part of the respondents believes that transparency must be shown every day to the readers. Among the main reasons to rely on transparency as an important value in their practice is the necessity to increase credibility in journalism and combat disinformation. Furthermore, this research suggests that transparency seems to be connected to objectivity and journalists' ethics, but not necessarily to the news outlets' rules."

::: section

## Show Your Work

When former *Chicago Sun-​Times* Director of Product Engineering Andy Boyle worked for rival newspaper *Chicago Tribune*, their internal newsroom software-​oriented storytellers had adopted the mantra "Show Your Work," even printing it on T-​shirts they wore in the office. The principle is that a data journalist's work should be public and something that people can scrutinize and test.

"It should be able to face rigor," he said. "If we're saying, 'This is an accurate representation of this data,' then the audience should be able to get the data themselves, analyze it themselves, follow our methods and come to the same conclusions."

In his role at the *Sun-​Times*, whenever the team referred to an analysis of data, they shared a direct link to whatever it is they were analyzing, so readers could find the data themselves. Team members also wrote up their methodologies a few times, in case people wanted to follow along and do it themselves.

"If someone wants to say your work is bunk, it's harder for them to do that if they can go step-​by-​step and come to the same conclusions as you," he said. "Showing your work out in the open lends it much more credibility. Just like we try and use confidential sources only in very limited situations and try and get everyone to speak on the record, you should treat your data work as if you, the journalist, require your own work to be on the record."

"And if you can't explain how you got your analysis, you probably aren't in a good enough position yet to explain to your audience what the information means. Or if you feel you need to hide the way you've come up with your analysis, that's giving people less incentive to trust your work."

There are many ways journalists can give readers a peek behind the curtain and show them how data stories are built. They can post links to the raw datasets used in reporting the story. They can post their research and methodology to a GitHub page. They can link to datasets and the origin source from the footer of their graphics. They can post excerpts of their data diaries as sidebars to their main stories.

Some large data projects provide a box inside the article -- ​jokingly called a "nerd box" -- ​in many newsrooms, or even a footnote briefly explaining the methods. Journalists can also pare down a longer data diary, which we'll explore later in this chapter, into a Twitter thread to better explain how they reported, wrote and visualized the story.

David Eads posted on Vimeo and Twitter a 41-​minute video where he and reporters from the Marshall Project walked viewers through their data analysis and visualization process for an award-​winning investigation into K-​9 police dog bites. He also provided a short story about the reporting process for the project, which the Marshall Project collaborated on with the *Indianapolis Star*, [AL.com](http://AL.com) and the Invisible Institute.

Benefits to making data readily available can be far-​reaching. For instance, the *Washington Post* in 2019 examined the prescription opioid epidemic in the US by building a database on the sales of millions of painkillers. The *Post* made the data and its methodology open to the public and encouraged reporters from other media outlets to localize it. Journalists in more than 30 states participated, including a piece examining the opioid crisis in Chicago and Cook County.

That openness helps expose flaws in reporting as well. Alvin Chang, head of visuals and data for *The Guardian US*, was horrified when he realized he made a mistake in a story.

"Not because I got it wrong," he said, "but because I was the only person who realized I got it wrong. It showed me just how much faith people put in data visualizations, as if putting it in chart form somehow makes it more valid."

"My data transparency efforts are often about trying to explain what the data is, what question we asked of the data, how we conducted the analysis and what results it yielded. When my readers talk about my data visualization to their friends, I want them to be able to tell a story about what data was gathered, how it was parsed and what the findings were. I also link to datasets and occasionally share code, but my concept of 'transparency'" is often for the majority of readers who aren't data fluent.

Lynn Walsh is an assistant director of Trusting News, which teaches journalists how to be more open and build trust with readers. A former investigative TV news producer, Walsh said journalistic transparency and "showing your work" are designed to engender trust by showing that journalists are willing to draw attention to matters that might influence their work.

In addition to disclosure, transparency can refer to a broader kind of storytelling around journalism's motives, values and processes. News consumers do not have deep knowledge of how journalism operates, as a 2018 American Press Institute study shows. And when there is a void of understanding, readers are not often giving journalists the benefit of the doubt. Investigations and data-​heavy reporting often take time.

When news outlets publish these stories and say they spent months on them, people may wonder why they spent months on that specific topic. Instead of allowing them to wonder and come to their own conclusions (which would most likely be negative), they should explain why they choose to focus on the topic -- ​by tying it to their values and goals -- ​and also be transparent about how they did the reporting. Because these stories are also complicated and involve data, people will have many questions about why journalists chose that specific dataset or spoke to that expert or focused on that element of the data. Therefore, they must explain all of these to their users.

It has become common for journalists to do this by writing a "behind the story" piece to accompany long investigative projects. In these stories, an editor typically explains why a story was written and the work involved, lists team members and answers readers' questions. Those pieces are usually on a separate page from the main story, and often only the most dedicated readers will click through. Walsh and her Trusting News colleague, Joy Mayer, are firm believers in taking advantage of attention where it already exists -- ​in the story itself.

For example, if part of a story says a source wasn't available for comment, journalists could explain how they tried to reach the person. When they introduce an expert source, they could include information about their independence and reliability. When part of a story led a reporter to consult a conflict of interest policy, describe the situation and link to the policy, Walsh said.

But there's a major drawback: All of the extra information can often disrupt a story's flow. Walsh recommends that reporters experiment with what their CMS can do to set off type so it looks different from the narrative story, or use a "nerd box" to highlight or link off to the information. Try not to let internal conventions and comfort zones get in the way of important trust-​building opportunities. For example, Walsh's team worked with Gannett's regional-​based data and investigations unit that built a WordPress tool that allows pieces of a FAQ to be embedded throughout a text story. The tidbits (dubbed "trust nuggets" internally) made their debut in a story by reporter Lucille Sherman about a lack of oversight of midwives in Oklahoma. The story is part of a larger project about out-​of-​hospital births.

Walsh said there are two wonderful things about the "trust nuggets":

1.  **Each trust nugget offers actual information.** It doesn't just say "to learn why we started this investigation, click here." It gives enough background that the reader learns something about the journalists' values or processes without having to leave the page.
2.  **The trust nuggets appear where they're most needed.** They anticipate that where the story introduces a new character, readers might be curious about why that character is included. Or where a dataset is cited, readers might wonder why that was the right data to rely on.

Joy Mayer, Walsh's Trusting News colleague, wrote on Medium about the technology behind the "trust nugget" tool and when transparency is most needed. She pointed out that they work for TV and radio, too, as WUSA built transparency into an investigation of Washington, D.C., police practices.

Readers don't mostly show up to your journalism automatically curious about how and why it was put together. They typically care only when the behind-​the-​scenes information relates to the news they're consuming in the moment, Walsh said.

"Consider how you feel about other institutions you interact with," Walsh said. "When do you care to learn more about the leadership of your local school district, the manager of your local grocery store or the policies of a local nonprofit? Only when they intersect with your interests or your concerns, right?

"You don't just show up at the grocery store wondering about the background of the manager, their corporate philosophy on charitable giving or the values that guide their hiring."

For example, Walsh said it might be appropriate to reveal that the subject of a story has also been a donor to a news organization. Or a journalist's staff bio might reference financial investments, community involvement or family connections to an issue of high interest. Walsh, former president and ethics chair for the SPJ, cited Kara Swisher's Recode bio as an example of great transparency ([Figure 11.1](#ch11.xhtml_f11_1)).


Chang, at *The Guardian US*, cautioned journalists against placing too much trust in data. One of the flaws of data journalism is that it can't answer every question and is only one tool to describe the world and what's happening in it.

"It's not more trustworthy than a human source," Chang said.

> The biggest mistakes I've made are when I tried to use data to answer a question that can't be answered with data, or when I've assumed the data is correct. When you're working with other people who are fluent with data, it's easy to talk through some of these concerns and pivot when necessary.

But what if you are the only data journalist in the room and your editors see data journalism as a magic answer machine? That puts a lot of pressure on you to produce an answer from the data. This is why it's so important to have more data-​fluent people in newsrooms, especially in leadership positions. Chang said it's also why it's important to say "no" to editors if the data can't answer the question.

:::: section
## How to Post Data Online

Providing complete datasets gives readers the opportunity to pore over the raw figures journalists used in their story. Journalists have many options when posting data to the web.

<aside class="boxed-text2" epub:type="tip" role="doc-tip">

::: section
### Lynn Walsh's Tips for Building Trust with Data Stories 

1.  **Explain what investigative/data journalism is and isn't.** People have a lot of questions about how and why we choose to cover certain topics and stories. When we do not explain the why and how they make assumptions about it and often assume we are biased. Talk about why you invest time into these stories and how you choose which stories to select. Explaining this publicly can also help hold your team accountable for the type of journalism you want to produce. *The Seattle Times* recently answered these questions and more with a FAQ about its investigative team and how it operates.

2.  **Be transparent about your process**, which includes showing your work and linking to the original data and documents. Make sure to include these explanations within the reporting or at least linked to the main story. You want to catch people's attention and curiosity while they are engaging with your content and not expect them to find a separate story and click on it later. Some elements are worth explaining: What data you used and why, how you used the data, how you analyzed the data, who you relied on to be experts and why, what you still do not know or are left wondering about and where the data came from.

3.  **Be available to answer questions**, and remember, sometimes questions can be misinterpreted as criticism at first glance. Make sure you build in time to review comments on social media, emails, etc. It's really important that we pay attention to and engage with our users, and one of the best ways to do that is by responding to their comments, answering their questions and asking for their feedback.

    Some of the questions may be very basic, but if we want people to understand the sometimes complicated data, we may need to explain the very basic elements first. Also, sometimes questions are buried in criticism. That negative comment may be based on a misunderstanding of how the reporting process works. So, don't dismiss it. Instead, take time to respond and ask more specific questions to them to get at what they really want to know or do not understand. And if people do not understand elements of the story, take the time to produce FAQs or do a follow-​up story that helps them understand.

4.  **Make corrections.** We try so hard to not make mistakes, but sometimes they happen. If they do, make the correction quickly and publicly. Do not try to hide it or make the change without acknowledging it. Also, our reporting is done with the best information we have at the time of publication. If you receive new information after the story publishes or someone sees your story and can provide new details, do the update and link to the original story and update the original story.

</aside>

While not a dedicated data publishing platform, GitHub is a very powerful, capable, free platform on which to publish high-​quality data. It's popular among journalists for storing datasets and methodology for large projects, and the documents can be easily searched and downloaded.

Since it's free, any size newsroom -- ​from one staffer to hundreds -- ​can use the platform to share work. Some examples:

- **ProPublica:** [https://github.com/propublica](https://github.com/)

  Links to data and methodology from several big investigative projects. ProPublica also stores its news app and data style guides on GitHub so others can learn from them.

- **The Guardian:** [https://github.com/guardian](https://github.com/)

  Includes data and coding exercises

- **Vox:** [https://github.com/voxmedia](https://github.com/)

  Stores hundreds of projects as well as hiring guides, programming examples and more.

- **BBC:** [https://github.com/bbc/](https://github.com/)

  Offers open-​source code used on public facing services, internal services and educational resources.

- **Buzzfeed News:** [https://github.com/BuzzFeedNews/everything#guides](https://github.com/)

  Indexes all of its open-​source data, analysis, libraries, tools and guides. It releases not only the reporting methods but also the scripts used to pull, clean, analyze and visualize data.

- **New York Times:** [https://github.com/nytimes](https://github.com/)

  Resources range from data to immersive projects and has a very large repository for its in-​depth COVID-​19 data.

The easiest way to make a dataset available is to upload it in Google Sheets. You can use the Share settings in the upper-​right corner to set it to public viewing and then link to the data from your story or share it over social channels. This gives the audience a chance to inspect the raw data in view-​only mode, so it can't be tampered with.

Once your data is posted online as a Google Sheet, you can format it to be searchable in the Google Dataset Search tool, which we explored in [Chapter 1](#ch01.xhtml_c1). You must follow a set of criteria outlined on the tool's developer page ([Figure 11.2](#ch11.xhtml_f11_2)) to get the dataset listed in the search algorithm, including details about the dataset, source, methodology and more. It's an excellent way to steer traffic to your data and, possibly, your story.


Some tools, such as Datawrapper, give journalists the option of making the data available through a clickable link in the footer of a graphic. This is a simple, easy way for readers to access the raw data ([Figure 11.3](#ch11.xhtml_f11_3)).


Flourish's table and database templates make it easy to upload data to the web, make it searchable and embed in a story. For example, the *USA Today* college football coaches' salary spreadsheet was uploaded to Flourish's searchable database template and published in a matter of minutes. Readers can search the database ([Figure 11.4](#ch11.xhtml_f11_4)) by searching by name, conference or state. Datawrapper and Airtable also offer a searchable table template, and Flourish and Datawrapper have social media sharing buttons so readers can quickly upload links to the databases to send to social channels.


Tableizer is another free tool that can post data quickly to the web. Just cut and paste the data from your spreadsheet into the interface, select the font and header color you want in your table and hit the Tableize It! button. ([Figure 11.5](#ch11.xhtml_f11_5)). You'll get JavaScript code to embed the table in your site and a sample of what the table will look like.


::::: section

## Sharing Data on Social Media

Social media channels provide another medium to share data with an audience. Several months into the pandemic, Cherone started tweeting COVID-​19 data daily on her \@heathercherone account she uses for sharing WTTW news. She pulled data from the Chicago Department of Public Health and weaved in context from her reporting and covering announcements from the mayor's office and other sources.

Cherone "reverse engineered" the daily data updates on the city's dashboard to give readers a clear look at the data Governor JB Pritzker and Chicago mayor Lori Lightfoot were using to base public health decisions.

"I didn't do these daily updates at the start of the pandemic because we didn't have good data right away," Cherone said.

> "I started doing them when the second wave hit in the fall of 2020 and winter of 2021. That was because Pritzker and Lightfoot sent a really clear message about what would trigger increased restrictions for bars and restaurants, or if we would be able to open gyms and schools."

<aside class="boxed-text2" epub:type="tip" role="doc-tip">

For more examples of how to share data on social media, visit the Data + Journalism blog at <http://dataplusjournalism.com>

</aside>

The biggest challenge Cherone faced: "How do I make it readable for people and engaging?" She started by featuring the rolling, seven-​day positivity rate for the city, then used arrows for bullet points to work other data into the posts, such as the number of cases, tests, hospitalizations and deaths ([Figure 11.6](#ch11.xhtml_f11_6)).


"The test positivity was important because the governor was using that to Institute or lift rollbacks and the number of cases was important because the city was using that to either add or remove restrictions," Cherone said.

> "I knew that those two had to be there. Then it became clear that hospitalizations were also going to be especially key in the summer of 2021 because the governor reinstituted a mask mandate because of increasing hospitalizations. I added hospitalizations per day because I think it's really easy again to get lost in the data and percentages and not focus on the fact that this disease was killing two or more people a day."

Readers engaged with the tweets from the start, asking Cherone questions about the figures and for more context. Many questions came in about the confusing death rate, which was presented as a decimal because it was a rolling seven-​day rate, so Cherone explained how the data was calculated and provided a link to the data dashboard for readers to review ([Figure 11.7](#ch11.xhtml_f11_7)).


"A lot of people were really confused about the math involved there so I have a tweet that I did and I just use that one to respond to people saying, 'How could 6.8 have died?'" she said. "I think it's helpful to share the data with people because they care and are trying to make the right decisions for themselves and their families."

:::: section
### Data Diaries and Transparency

When Boyle works on a large project, he usually keeps a text document open where he walks through all of his steps. These "data diaries" can be helpful for journalists -- ​and fellow team members -- ​to retrace their steps on an analysis over months of research.

In the diary, Boyle addresses questions such as: Where did I download the data from and when? Where did I upload it for analysis? What sort of code did I write to actually do the analysis?

"I try and keep it all step by step, so someone else can go through everything I do -- ​or, more importantly, I can go through the steps again myself -- ​and get the same answers," he said.

> "It's basically the scientific method. Your work should be reproducible. Just like in journalism, we try and explain who told us a fact, or what document we got information from. We try and do the same when it comes to analyzing and sharing data."

Those data diaries can be used for more than internal purposes. They can be reproduced as short sidebar stories or "nerd boxes," which Walsh discussed earlier in this chapter. They also can be reproduced in short bursts on social media, such as a "Twitter thread."

Journalists use social media threads for many purposes: Explaining how a complex data story was reported, sharing a running narrative, live-​tweeting, descriptive writing and more. When done right, a thread can engage a social media audience in a very meaningful way.

Twitter threads are an effective way for data journalists to explain the research, reporting and visualization process to readers. If the reporter or designer is keeping a data diary -- ​a Google or Word document with a running narrative of the reporting, writing and visualization process -- ​those diary highlights can easily transform into a Twitter thread. In other words, it's the data journalist's chance to show how the sausage is made.

As a rule, most Twitter threads are around 10--​15 tweets, but you can make it shorter if need be. Weaving in links, photos, graphics, etc. helps visualize the thread and increase understanding for the reader. The graphics are particularly important as it's a way to showcase them to the reader and tease the story. Also, think of ways to *engage* the reader in the thread: A Twitter poll or pose a question to the reader at the end of the thread.

For your first tweet, you should always include a link to your story/project and set up the thread as an explanatory/how-​the-​sausage-​is-​made process or the lead to your narrative.

These examples from newsrooms show various approaches for writing effective Twitter threads for data stories. Study how each is structured and the conversational tone the author took in explaining the process.

**Mary Jo Webster: Minneapolis Star Tribune Justice Denied** [https://twitter.com/maryjowebster/status/1021424211880013827?s=12](https://twitter.com/)

She explains how she did data reporting on an investigative project. Explains what tools she used and how she went about editing the data. Good explanatory journalism and transparency. When you tell how the "sausage gets made," it builds trust with your reader ([Figure 11.8](#ch11.xhtml_f11_8)).


**David Eads: The Marshall Project** [https://twitter.com/eads/status/1341772612377202688?s=27](https://twitter.com/)

He explains how the Marshall Project investigated police K-​9 bites with this six-​tweet thread that includes a link to the story and an explanatory data video recorded on Zoom.

**NY Times: Tulsa's Black Wall Street** [https://twitter.com/singhvianjali/status/1397302024333627392?s=27](https://twitter.com/)

Great visuals tied to this "how-​to" of what Tulsa's Black Wall Street looked like before it was destroyed in the Tulsa Massacre.

**Karen Hao: How We Made Tech Review Graphics** [https://twitter.com/\_karenhao/status/1185647498418892808?s=12](https://twitter.com/)

Similar to Webster's approach that explains technique, software and process to the reader. Great transparency.

**BBC News Graphics: Theresa May Resignation in Data/Graphics** [https://twitter.com/bbcnewsgraphics/status/1131896210644754432?s=12](https://twitter.com/)

How the data team covered the British prime minister's resignation.

\* \* \*

<aside class="boxed-text2" epub:type="tip" role="doc-tip">

::: section
### Read More 

**Data and Diversity**

How can journalists make their data reporting more inclusive for diverse audiences? Read how to do it on our blog, <http://dataplusjournalism.com>

</aside>

::: section
## Tools Used in This Chapter

Google Dataset Search <https://datasetsearch.research.google.com/>

Google Dataset Search developers page [https://developers.google.com/search/docs/advanced/structured-​data/dataset](https://developers.google.com/)

Google Flourish <https://flourish.studio/>

Datawrapper <https://www.datawrapper.de/>

Tableizer <https://tableizer.journalistopia.com/>

Google's Data GIF Maker <https://datagifmaker.withgoogle.com/>

\* \* \*


## Footnotes

- Society of Professional Journalists Code of Ethics [https://www.spj.org/ethicscode.asp](https://www.spj.org/)
- The Reader on Data Visualization, Ch. 5 [https://mschermann.github.io/data_viz_reader/ethics.html#ref-ethical_infographics](https://mschermann.github.io/)
- Alberto Cairo, Ethical Infographics [https://www.dropbox.com/s/pqgmg02yz0pgju4/EthicalInfographics.pdf](https://www.dropbox.com/)
- Washington Post Uber Investigation GitHub page [https://github.com/comp-journalism/2016-03-wapo-uber](https://github.com/)
- The Marshall Project, Tracking Police K-9 Violence Using Data [https://vimeo.com/493807936/2375f9b7d0](https://vimeo.com/)
- The Marshall Project, We Investigated How Police Use Dogs as Weapons. Here's How You Can Do It Too [https://www.themarshallproject.org/2020/12/23/we-investigated-how-police-use-dogs-as-weapons-here-s-how-you-can-do-it-too](https://www.themarshallproject.org/)
- The Washington Post, Follow the Post's Coverage of the Opioid Epidemic [https://www.washingtonpost.com/national/2019/07/20/opioid-files/](https://www.washingtonpost.com/)
- The Red Line Project, Chicago, Cook County on Forefront of Opioid Crisis [http://redlineproject.org/opioids1.php](http://redlineproject.org/)
- The Oklahoman, We're Losing Children [https://stories.usatodaynetwork.com/unaccountable/](https://stories.usatodaynetwork.com/)
- The Oklahoman, Failure to Deliver [https://stories.usatodaynetwork.com/failuretodeliver/#](https://stories.usatodaynetwork.com/)
- American Press Institute, Americans and the News Media: What They Do -- and Don't -- Understand about Each Other [https://www.americanpressinstitute.org/publications/reports/survey-research/americans-and-the-news-media/](https://www.americanpressinstitute.org/)
- Trusting News, Investigative Team's "Trust Nuggets" Inject Transparency into Long Stories [https://medium.com/trusting-news/investigative-teams-trust-nuggets-inject-transparency-into-long-stories-2dc449b3add8](https://medium.com/)
- Trusting News, Earn Trust through Explaining the Process of Reporting [https://medium.com/trusting-news/earn-trust-through-explaining-the-process-of-reporting-3c0d1eb06397](https://medium.com/)
- Vox, Kara Swisher's Recode Bio [https://www.vox.com/authors/kara-swisher](https://www.vox.com/)
- Answering Your Questions about How the Seattle Times Does Investigative Journalism [https://www.seattletimes.com/seattle-news/times-watchdog/faq-how-the-seattle-times-does-investigative-journalism/](https://www.seattletimes.com/)
- ProPublica GitHub page [https://github.com/propublica](https://github.com/)
- ProPublica News App and Data Style Guides [https://github.com/propublica/guides](https://github.com/)
- The Guardian GitHub page [https://github.com/guardian](https://github.com/)
- Vox GitHub page [https://github.com/voxmedia](https://github.com/)
- BBC GitHub page [https://github.com/bbc/](https://github.com/)
- Buzzfeed News GitHub page [https://github.com/BuzzFeedNews/everything#guides](https://github.com/)
- New York Times GitHub page [https://github.com/nytimes](https://github.com/)
- Datawrapper, Nigerian Debt Pie Chart [https://www.datawrapper.de/\_/3q5YO/](https://www.datawrapper.de/)
- USA Today, College Football Coaches Salary Database [https://public.flourish.studio/visualisation/6431056/](https://public.flourish.studio/)


# 12 Math for Journalists: Writing with Numbers

Mike Reilley

DOI: [10.4324/9781003273301-13](https://doi.org/10.4324/9781003273301-13){aria-label="D.O.I. link to this document."}

A little humor can go a long way in data journalism. A long-​running joke among college journalism professors is that many college students flee the math, science and engineering departments for journalism schools because they think they can escape having to learn math.

How wrong they are.

Math calculations are vital to nearly any newsroom beat, whether you're covering city hall, working in sports or the business departments. While spreadsheets often handle the heavy lifting with formulas, journalists still must master some basic math skills to calculate specific data points and fact-​check data from other sources, such as a city budget.

WTTW political reporter Heather Cherone's story about Alderman Austin's committee spending, detailed in [Chapter 7](#ch07.xhtml_c7), was based on a comprehensive 236-​page report that would be overwhelming for many journalists. Cherone spent hours poring over the data, isolating the key numbers for the story. Then she stepped away from the story for a few hours to clear her mind, returned and double-​checked all the percentage calculations.

Taking that break gave Cherone a chance to look at the data with a fresh perspective before recalculating "because the last thing you want to do is get something wrong and mess up a percentage," she said. "It's mostly for peace of mind because you don't want to worry."

Without reliving a few years of middle-​school math, here are some ways we can make calculations easier for reporters, especially on deadlines.

::: section
## Figuring Percentage Change

Calculating percentage change can be painful but only if you calculate it as a fraction. Fractions aren't fun, as we know from eighth-​grade algebra, so it's better to think of a percentage change as a decimal.

For instance, let's say a company's \$135,000 marketing budget increases by 5 percent from one year to the next. To figure the new total, simply multiply \$135,000 by 1.05 (1.00 plus 0.05). Use a decimal instead of doing subtraction and fractions.

1.  \$135,000 × 1.05 = \$141,750 for the new budget

How you could write it as a sentence: "The company's marketing budget increased by 5 percent this year to \$141,750."

You apply the same approach if the budget has decreased. Let's say a company's marketing budget decreases by 8 percent; multiply it times 0.92 (1.00 minus 0.08) to get the new budget figure.

1.  \$227,000 × 0.92 = \$208,840 for the new budget

How you could write it as a sentence: "The company's marketing budget decreased by 8 percent this year to \$208,840."

What if you have the new and the old values and need to figure out the amount of the percentage change itself? Take the new value and subtract the old one, and then divide by the old one.

University of Missouri professor David Herzog abbreviates the calculation as "(N-​O)/O." Since reporters find themselves doing this often, he recommends a phrase to remember it: "Do journalists like doing math? NOO!"

::: section

## Percent Change and Percentage Points

An increase from 12 percent to 15 percent isn't a 3 percent increase. It's a three percentage point increase. This is important for budget stories as well as election data. Be very careful with percent and percentage points.

::: section
## Percentage Increases Exceeding 100 Percent

Reporters often make the mistake of miscalculating percentages over 100 percent. There's an easy way to keep it straight. Look what's increasing or decreasing and by how much, not at the percentages.

For example, let's say you're reading a city budget summary, and one of the line items said it increased 300 percent, from \$150,000 to \$450,000. You check the budget spreadsheet and see that the monetary figures are correct. But is it really a 300 percent increase? It's not. The amount has tripled (\$150,000 × 3 = \$450,000), but tripling is a 200 percent increase, not 300 percent increase. So it's simpler to tell the readers that the budget has tripled, as stating it as a 200 percent increase can be confusing.

:::: section

## Per Capita and Rates

We covered compiling rates and per capita in the spreadsheet chapters, but it's important to note that percent change in a value tells you only part of the story when you are comparing values for several communities or groups. Another important statistic is each group's *per capita* value. This figure helps you compare values among groups of different sizes.

Rates help readers better understand complex issues such as homicide data or COVID-​19 positive cases or vaccinations. They also give a more accurate picture of an issue by looking beyond just the totals for an issue but rather measuring it against another variable, such as population or number of tests administered, etc.

For example, take this fictional dataset of murders for one year in a sample of cities (Shortlink: [http://bit.ly/murderrates](http://bit.ly/)). When you sort them by column C, the total number of murders, you see that Chicago has the most (500), followed by New York City (419) and Detroit (386) ([Figure 12.1](#ch12.xhtml_f12_1)).


But when you figure population into the equation and sort it, you get a different result.

Start by putting this equation into cell D2 and dragging the handle on the cell down to the bottom to populate the column: =c2/b2 ([Figure 12.2](#ch12.xhtml_f12_2)).


This compiles murders by population, but the decimal figure would be hard to explain to readers. It becomes easier when we figure the rate per 100,000 residents in cell E2 by typing: =d2\*100000 and dragging down to autofill the other columns.

Now highlight the spreadsheet, go to the data menu and select Sort Range/Advanced Sorting Options, check the header row box and sort by descending order (Z to A) on Column E (Murders per 100k).

The next step is to highlight only column E and hit the decrease decimal button to round off the number to one decimal point.

Now your data shows a different result: The cities that have the highest murder rate per 100,000 residents ([Figure 12.3](#ch12.xhtml_f12_3)).


Now you can write a much more complete story about the murder rates in these cities. Detroit, New Orleans and St. Louis have the highest *murder rates*, while Chicago, New York City and Detroit have the highest *total number* of murders.

<aside class="boxed-text2" epub:type="tip" role="doc-tip">

::: section
### ![](images/Pro_Tip_Icon1.jpg) Percentage Increase/Decrease Tables 

Use this guide as reference for figuring increases and decreases:

- 50 percent increase = increased by half
- 100 percent increase = better to say doubled
- 200 percent increase = better to say tripled
- 300 percent increase = better to say quadrupled

</aside>

::: section
## Margin of Error in Polls

One of the most common errors political reporters make is to misrepresent polling data leading up to an election. It's critical to convey the flaws in polling to readers and viewers to avoid misleading who's a frontrunner in a race or in a study.

In his book, *A Journalist's Guide to Public Opinion Polls*, G. Evans Witt points out that the most common mistake by political journalists is misstating the nature of one candidate's margin over the other in a well-​conducted poll.

Knowing the sampling error margin in a poll you're reporting on is critical, Witt writes, and the figure should be rounded up to the nearest whole number. In other words, a 2.5 percentage point margin of error should be rounded up to 3 percentage points.

Witt cites three situations by using hypothetical polls with a sampling error margin of plus or minus 4 percent:

1.  Fifty-​two percent of the public says it would vote for Joe Biden for president, while 37 percent say they would vote for Donald Trump. The remainder are undecided.

    If the difference between the candidates' percentages is more than twice the sampling error, it's correct to say one candidate leads the other.

2.  What if the margin is narrower?

    1.  Biden 44 percent
    2.  Trump 41 percent
    3.  Undecided 15 percent

    This would be a dead heat, too close to call. It would be inaccurate to say that Biden leads Trump as the margin of error is 4 percent, and there are so many undecided voters. The poll only tells you that they're very close in terms of support.

3.  If the poll falls between the two previous cases:

    1.  Biden 47 percent
    2.  Trump 41 percent
    3.  Undecided 12 percent

    The margin is six percentage points, and the margin of error is four percentage points, so it would be safe to say Biden has a small lead or leads by a narrow margin. Still, we should be very careful in providing context for the poll and explain to the readers and viewers what the margin of error is.

Besides margin of error, you should closely scrutinize how poll questions are phrased and the sample size, with a particular focus on demographics. The same is true on survey results. Has it captured a large sample and a diverse one in terms of age, ethnicity, gender, religion, political views, geography and other categorizations? Challenge what you find before using it in a story.

::::: section

## The Off by One Error

Let's say you're rushing to write a 500-​word story, and you need to get it in at 5 p.m. It's currently 1 p.m. Watching the clock, you write 100 words per hour, reaching a stopping point right on deadline. But, bad news -- ​you're 100 words short!

You've run into a common mathematical trip-​up called the "off by one error." It has wide implications in math, programming and law and is sometimes called "the fence-​post problem" based on an easy-​to-​understand allegory.

If someone is building a fence that is 50 feet long, and they need a fence post every 10 feet, how many fence posts do they need?

It's tempting to say five, but the answer is actually six. The yards are distances, or spans, meaning they have a point at each end. If the builder only bought five posts, they would find the last boards hanging into empty space.

This counting process can be deceptively tricky, especially with time spans. Some measurements of time are items, and others are spans. For example, 2011--​2014 is three years, because years are counted as distances. But February 11 to 14 is four days, because days are counted as individual items.

How do you know if something is an item or a span? Try to reduce the equation to just one instance. For example, to build a 10-​foot fence, two fence posts are needed. That means the fence posts are items, while the fence itself is a span.

You can think of spans as entities that "touch" items. Ergo, the time span of a week -- ​Sunday to Saturday -- ​"touches" seven items, or seven days.

<aside class="boxed-text2" epub:type="tip" role="doc-tip">

::: section
### Items and Spans Quiz 

1.  [[Sally worked](#ch12.xhtml_que12_1b) from Monday to Friday and earned \$50,000. How much money did she make per day?]
2.  [[Mark worked](#ch12.xhtml_que12_2b) from 1 p.m. to 5 p.m. and earned \$50,000. How much did he earn per hour?]
3.  [[You are running](#ch12.xhtml_que12_3b) the SUM() function on the range B1:B4. How many values will the function count?]
4.  [[A recent](#ch12.xhtml_que12_4b) storm blew down street posts, and the city announced it will install new stop signs from 2nd Avenue to 8th Avenue. How many stop signs does the city need to order?]

::: section
### Answers: 

1.  [[Sally made](#ch12.xhtml_que12_1) \$10,000 per day. Days are items, meaning the dollar amount should be divided by the number of items in the list. Monday through Friday "touches" five days.]
2.  [[Mark earned](#ch12.xhtml_que12_2) \$12,500 per hour. Even though the time span of 1 p.m. to 5 p.m. "touches" four hours, hours are counted as distances.]
3.  [[The function will](#ch12.xhtml_que12_3) count four values, because the values exist in individual cells, or points.]
4.  [[The city needs](#ch12.xhtml_que12_4) to buy seven stop signs. Even though the distance between 2nd Avenue and 8th Avenue is six blocks, a stop sign is needed for every block that distance touches, which is seven.]

</aside>

::: section
## Mean, Median and Mode

**Mean (average):** It's easy to calculate. Just add up all the values in a set of data and then *divide* that sum by the number of values in the dataset.

**Median (middle):** When you write about "the average worker" this, or "the average household," you don't want to use the mean to describe those situations. You want a statistic that tells you something about the worker or the household in the middle -- ​the median.

It's easy to compile, just line up the values in your set of data, from largest to smallest. The one in the dead center is your median. In the example below, the median is five:


If it's an even set of numbers, take the two middle numbers, add them and divide by two to determine the median:


**6 6 + 5 = 11 11/2 is 5.5**


**Mode:** The mode is the value in a set that occurs the most often. It's not used often in news stories. But one instance would be showing the most popular example from a list of product prices.

\$385 \$227 \$227 \$666 \$922

\$385 \$227 \$666 \$999 \$1,090

\$385 \$385 \$1,090 \$999 \$666

\$227 \$667 \$385 \$921 \$1090

This is a bit of a brain tease, but if you look at it long enough, you'll see the mode is \$385, as it appears five times in the list. For large lists, it's best to use a spreadsheet formula, which is detailed later in this chapter.

To better understand how mean, median and mode work, let's apply the median, mean and mode to consumer retail purchases. For instance, you're analyzing a local electronics store's purchases for the holiday season. Here's an approach you could take:

- Use the median to describe how much money the typical customer spent at the electronics store. Median also can be used with Census data to best describe household income.

  It's commonly used in real estate to analyze home values in a particular area because it eliminates outliers.

- Use the mean to describe how much money the electronics store collected per customer this season. This figure typically skews larger than the median as it includes outliers, such as customers buying a home computer and others purchasing a set of earbuds.

- Use the mode to describe what was the most common/popular single item or price at the store. For example, an iPad price might be the most popular item sold around the holidays and will appear most often in the store's books.

::::::::: section

## Basic Google Sheets and Excel Formulas

Why use a calculator when you can let the spreadsheet do the heavy lifting for you?

:::: section
### Figuring Sums

This is the basic formula ([Table 12.1](#ch12.xhtml_t12_1)). You can adjust cell numbers based on columns/rows/needs: =SUM(B4:B13)

+-----------------------+-----------------------------------+-----------------------------------------------------------------------+
| **− (Minus key)**     | − (minus)                         | Use in a formula to subtract numbers or to signify a negative number. |
|                       |                                   |                                                                       |
|                       |                                   | Example: =18--12                                                      |
|                       |                                   |                                                                       |
|                       |                                   | Example: =24\*−5 (24 times negative 5)                                |
+-----------------------+-----------------------------------+-----------------------------------------------------------------------+
| **× (Multiply key)**  | \* (asterisk; also called "star") | Use in a formula to multiply numbers. Example: =8\*3                  |
+-----------------------+-----------------------------------+-----------------------------------------------------------------------+
| **÷ (Divide key)**    | / (forward slash)                 | Use in a formula to divide one number by another.                     |
|                       |                                   |                                                                       |
|                       |                                   | Example: =45/5                                                        |
+-----------------------+-----------------------------------+-----------------------------------------------------------------------+

: *[Table 12.1*](#ch12.xhtml_t12_1b) Basic Calculations

For short lists: =SUM(B4,B5,B6,B7); =SUM(B4+B5+B6+B7). But this formula works best for longer lists: =sum(B4:B700) to add the cells as a larger group.

Or, place your cursor in the first empty cell at the bottom of your list (or any cell, really) and press the plus sign, then click B4, press the plus sign again and click B5 and so on to the end, and then press Enter. Excel adds/totals this list you just "pointed to:" =+B4+B5+B6+B7.

::: section
### Average (Mean)

1.  =AVERAGE(B4:B13)

Adds the list, divides by the number of values, then provides the average.

::: section
### Median

1.  =MEDIAN(A2:A6)

Median of the 5 numbers in the range A2:A6. Because there are 5 values, the third is the median.

1.  =MEDIAN(A2:A7)

Median of the 6 numbers in the range A2:A7. Because there are six numbers, the median is the midway point between the third and fourth numbers.

::: section
### Mode

1.  =MODE(A2:A40)

Shows you the number that occurs most often.

::: section
### Maximum/Minimum Number in a List

1.  =MAX(B4:B13) returns the highest value in the list.
2.  =MIN(B4:B13) returns the lowest value in the list.

**Convert a Fraction into a Decimal**

Divide the top number by the bottom number: 5/8 = 0.625, 17/64 = 0.265

**Convert a Decimal into a Percentage**

Multiply by 100 (or simply move the decimal two places to the RIGHT): 0.421 = 42.1%

**Turn a Percentage into a Decimal**

Divide by 100 (or simply move the decimal two places to the LEFT): 122.4% = 1.224

::: section
## AP Style and Math

Most newsrooms follow *The Associated Press Stylebook* for writing with numbers. The AP's general rule: Spell out any number under 10, and use the numeral for 10 and up. But the AP has many exceptions to its own rule when working with various types of data. Here are a few of those exceptions to focus on:

1.  **Temperatures:** 7 degrees ... minus−5 degrees
2.  **Ages:** The 9-​year-​old boy...
3.  **Dimensions:** 1-​foot by 3-​foot wide tiles.
4.  **Height:** 5-​foot 10-​inch guard ... 5-​foot-​10, 5--​10
5.  **Weight:** 227 pounds, 9 pounds
6.  **Speed:** 5 mph, not five and not m.p.h.
7.  **Time:** 2:30 p.m., 9 a.m., not 9:00 AM or PM
8.  **Rank:** He was my No. 1 choice or first choice. Never use the pound sign \# for a ranking. (It can easily be confused for a hashtag.)
9.  **Sports:** The Bulls beat the Pacers 100--​93. Michael Jordan scored 32 points and had 6 assists. Jordan, a 6-​foot-​6 guard out of North Carolina, has led the Bulls in scoring in seven of 10 games this season.
10. **Monetary figures:** Millions and billions are spelled out: \$1 million, \$1 billion, but not thousands. \$1,387,222 is \$1.39 million or \$1.4 million, depending on how far you need to round up or down. \$30,000, not 30,000 dollars. Cents is spelled out: 10 cents, not \$0.10.

::: section

## Estimating Crowd Sizes

You can use [MapChecking.com](http://MapChecking.com) to estimate a crowd size from a past protest or event in your area. Use archived photos as reference to paint the perimeter and estimate the density. Does the attendance estimate you get differ from the once in the coverage? How big is the difference?

Should MapChecking not be available, you can use Google Earth's measure tool to estimate the square yardage or meters of an area and then multiply it by the density. This takes a bit more math work than MapChecking, but it's still a quick and easy way to get an estimate.

You also can estimate a crowd size using a formula shared by Arizona State professor and Pulitzer Prize--​winning data journalist Steve Doig:

1.  Calculate crowd area in square feet (length × width).
2.  Divide by 10 for a loose crowd (people are at arm's length from one another).
3.  Divide by 7.5 for a tight crowd (people are more shoulder to shoulder).

<aside class="boxed-text2" epub:type="tip" role="doc-tip">

For more tips on how to estimate crowd sizes, visit the Data + Journalism blog at <http://dataplusjournalism.com>

</aside>

::: section
## Math Quiz

1.  Springfield's city budget was \$27.8 million in 2022. In 2023 it's \$33.7 million. What percent change is it? How would you write it in a sentence for the story?

2.  Edit this sentence for accuracy, assuming you know the dollar figures are accurate:

    **The budget increased 300 percent from 4 billion to 12 billion dollars.**

3.  Subtract these two percentages: 50--​27 percent. What is the answer?

4.  The \$972,758 budget increased by 8 percent to what dollar figure?

5.  Edit this sentence for AP Style:

    **From 8:00 am to 1:30 pm, the temperature dropped from 8 to 12 below zero degrees. This was the largest decrease in temperature in the last two and one-​half years.**

6.  You are editing this story and you read the lead and a few paragraphs of the piece. You notice something is amiss. How do you handle this situation?

The United Way on Monday awarded \$23,000 in supplemental funds to three organizations.

**Later in the story, you spot this sentence:** "The supplemental funds will go to the Boy Scouts, \$11,000; the Girl Scouts, \$9,000; and the Salvation Army, \$4,000."

\* \* \*

::: section

## Math Quiz Answers:

1.  \$5.9 million increase divided by the original number (\$27.8 million) gives you 21.2 percent.

    "Springfield's 2023 city budget increased 21.2 percent from last year to a total of \$33.7 million." You also could include the 2022 dollar amount as well.

2.  "The budget tripled from \$4 billion to \$12 billion."

    Three hundred percent is quadrupling. If we know the \$4 billion and \$12 billion are correct, then it's tripling. It's better to use triple than a 200 percent increase. We also fixed the AP Style issue on dollars.

3.  The difference is 23 percentage points. Remember, when subtracting percentages, we use percentage points.

4.  \$972,758 × 1.08 = \$1,050,578.64. Or round off to \$1.05 million or round up to \$1.1 million. The former is more precise than the latter.

5.  From 8 a.m. to 1:30 p.m., the temperature dropped from 8 degrees to minus −12 degrees. This was the largest decrease in temperature in the last 2½ years. (Note: Some editors may accept 2.5 years.)

6.  The numbers in the second sentence don't add up to \$23,000. But which number(s) is wrong? The best thing to do would be to contact the reporter to see if there's a typo or reach out to a United Way official to confirm. Don't assume the dollar figure in the lead is wrong. It could be one of the totals in the second sentence.

\* \* \*

::: section
## Resources: Math for Journalists

**Journalist's Toolbox Math for Journalists** [https://www.journaliststoolbox.org/category/writing-​with-​numbers/Tip](https://www.journaliststoolbox.org/) sheets, calculators and more

**The Journalist's Resource: Statistics for Journalists** [https://journalistsresource.org/home/statistics-for-journalists/](https://journalistsresource.org/)

**The Guardian Data Blog** [https://www.theguardian.com/data](https://www.theguardian.com/)

**Venngage: Telling Stories with Data** [https://venngage.com/blog/data-​storytelling/](https://venngage.com/)

**MapChecking Crowd Estimate Tool** <https://www.mapchecking.com/>

**Crowd Safety and Crowd Risk Analysis** [https://www.gkstill.com/Support/crowd-​density/625sm/Density6.html](https://www.gkstill.com/) Visuals from Dr. Keith Still to measure crowd density.

**The Guardian: Trump Inauguration Crowd: Sean Spicer's Claim vs. the Evidence** [https://www.theguardian.com/us-​news/2017/jan/22/trump-​inauguration-​crowd-​sean-​spicers-​claims-​versus-​the-​evidence](https://www.theguardian.com/)

**Google Earth** <https://earth.google.com/>

\* \* \*


## Footnotes

- WTTW, City Council Committee Led by Indicted Ald. Austin Spends More, Does Less than Nearly All Others [https://news.wttw.com/2021/08/16/city-council-committee-led-indicted-ald-austin-spends-more-does-less-nearly-all-others](https://news.wttw.com/)
- Murder Rates Practice Exercise, Google Sheet [https://docs.google.com/spreadsheets/d/1WxUkktVBCrVmt6pPGDxU0Wj1heDTZ2PZ_OpwEwdut5c/edit?usp=sharing](https://docs.google.com/)
- [BusinessJournalism.org](http://BusinessJournalism.org), Newsroom Math Crib Sheet [https://businessjournalism.org/2017/09/newsroom-math-crib-sheet/](https://businessjournalism.org/)
- Murder Rates Shortlink [http://bit.ly/murderrates](http://bit.ly/)

\* \* \*

To read the book's addendum, visit the Data + Journalism blog at <http://dataplusjournalism.com>


# Index

<aside epub:type="tip" role="doc-tip">
Note: **Bold** page numbers refer to tables and *italic* page numbers refer to figures.
</aside>

- [Adobe Illustrator [193](#ch10.xhtml_term-1)]
- [American Community Survey [142](#ch08.xhtml_term-2)]
- [American Press Institute study, 2018 [203](#ch11.xhtml_term-3)]
- [American Road & Transportation Builders Association (ARTBA) [86](#ch05.xhtml_term-4), [90](#ch05.xhtml_term-5)]
- [AND operator **[148](#ch08.xhtml_term-6)**, *[151](#ch08.xhtml_term-7)*]
- [animated chart [[182--3](#ch10.xhtml_term-8)]]
- [Application Programming Interface (API) [[173--4](#ch09.xhtml_term-9)]]
- [asterisk (\*) [146](#ch08.xhtml_term-10)]
- [AstraZeneca [79](#ch04.xhtml_term-11)]
- [Austin, A. C. [134](#ch07.xhtml_term-12), [217](#ch12.xhtml_term-13)]

<!-- -->

- [Backrub, search engine [17](#ch01.xhtml_term-14)]
- [bar/column chart [182](#ch10.xhtml_term-15)]
- [Barrett, F. [128](#ch07.xhtml_term-16)]
- [basic Google search [11](#ch01.xhtml_term-17), [[17--18](#ch01.xhtml_term-18)]]
- [basic spreadsheets [86](#ch05.xhtml_term-19)]
  - analyzing bridge inspections [[91--4](#ch05.xhtml_term-20)]
  - Bridge Area data [95](#ch05.xhtml_term-21)
  - bridge inspections database in Google Sheets *[88](#ch05.xhtml_term-22)*
  - figuring rates [[98--101](#ch05.xhtml_term-23)];
  - filters and datasets [[95--6](#ch05.xhtml_term-24)], *[97](#ch05.xhtml_term-25)*
  - interviewing your dataset [[88--90](#ch05.xhtml_term-26)]
- [BBC time-lapse chart, on 50-degree Celsius days *[189](#ch10.xhtml_term-27)*]
- [Bell, M. [2](#ch00_fm09_intro.xhtml_term-28)]
- [Berkeley Earth Surface Temperatures dataset [[32--4](#ch02.xhtml_term-29)]]
- [Big Ten positive COVID-19 cases, by university [95](#ch05.xhtml_term-30), [96](#ch05.xhtml_term-31), *[96](#ch05.xhtml_term-32)*, [99](#ch05.xhtml_term-33), [109](#ch06.xhtml_term-34), [110](#ch06.xhtml_term-35)]
- [Bowser, M. [12](#ch01.xhtml_term-36)]
- [Boyle, A. [4](#ch00_fm09_intro.xhtml_term-37), [184](#ch10.xhtml_term-38), [185](#ch10.xhtml_term-39), [201](#ch11.xhtml_term-40), [211](#ch11.xhtml_term-41)]
- [Braun, S. [160](#ch09.xhtml_term-42)]
- [Bridge Area data [95](#ch05.xhtml_term-43)]
- [Brin, S. [17](#ch01.xhtml_term-44)]
- [broadcast audience [136](#ch07.xhtml_term-45)]
- [browser extension, data scraping with [61](#ch03.xhtml_term-46)]
- [bubble map [194](#ch10.xhtml_term-47)]

<!-- -->

- [Cairo, A. [181](#ch10.xhtml_term-48)]
  - *How Charts Lie* [191](#ch10.xhtml_term-49), [200](#ch11.xhtml_term-50)
- [[[Carto.com](http://Carto.com)] [194](#ch10.xhtml_term-51)]
- [causation [[119--20](#ch06.xhtml_term-52)]]
- [[[CDC.gov](http://CDC.gov) site, for SARS] [18](#ch01.xhtml_term-53), *[19](#ch01.xhtml_term-54)*]
- [Center for Public Integrity [72](#ch04.xhtml_term-55)]
- [Chang, A. [4](#ch00_fm09_intro.xhtml_term-56), [137](#ch07.xhtml_term-57), [180](#ch10.xhtml_term-58), [181](#ch10.xhtml_term-59), [184](#ch10.xhtml_term-60), [185](#ch10.xhtml_term-61), [202](#ch11.xhtml_term-62), [204](#ch11.xhtml_term-63), [205](#ch11.xhtml_term-64)]
- [chart-building tools [192](#ch10.xhtml_term-65), [193](#ch10.xhtml_term-66)]
- [charts [[181--2](#ch10.xhtml_term-67)], [186](#ch10.xhtml_term-68)]
  - bar/column chart [182](#ch10.xhtml_term-69)
  - *Chicago Sun-Times* homicides victims database [186](#ch10.xhtml_term-70)
  - hierarchy and organizational charts [183](#ch10.xhtml_term-71)
  - interactive and animated charts [[182--3](#ch10.xhtml_term-72)]
  - line charts [182](#ch10.xhtml_term-73)
  - pie charts and treemaps [182](#ch10.xhtml_term-74)
  - Venn diagrams [183](#ch10.xhtml_term-75)
- [Cherone, H. [5](#ch00_fm09_intro.xhtml_term-76), [134](#ch07.xhtml_term-77), [136](#ch07.xhtml_term-78), [[210--11](#ch11.xhtml_term-79)], *[211](#ch11.xhtml_term-80)*, [217](#ch12.xhtml_term-81)]
- [*Chicago Sun-Times*: choropleth maps [192](#ch10.xhtml_term-82), [194](#ch10.xhtml_term-83), *[195](#ch10.xhtml_term-84)*]
- homicides victims database [186](#ch10.xhtml_term-85), [188](#ch10.xhtml_term-86)
- [choropleth maps [192](#ch10.xhtml_term-87), [194](#ch10.xhtml_term-88), *[195](#ch10.xhtml_term-89)*]
- [cleaning method [4](#ch00_fm09_intro.xhtml_term-90), [152](#ch08.xhtml_term-91)]
- [CLI [*see* [Command Line Interface (CLI)](#ch13_index.xhtml_idx47)]]
- [ClimateWatch [33](#ch02.xhtml_term-92), [34](#ch02.xhtml_term-93)]
- [cluster map [194](#ch10.xhtml_term-94)]
- [code: and browser-based tools [4](#ch00_fm09_intro.xhtml_term-95)]
  - data scraping with [[59--61](#ch03.xhtml_term-96)]
  - scrapping [169](#ch09.xhtml_term-97)
- [coding: challenges [[165--6](#ch09.xhtml_term-98)]]
  - terminology [166](#ch09.xhtml_term-99)
- [colors, for data visualization [192](#ch10.xhtml_term-100)]
- [Command Line [167](#ch09.xhtml_term-101)]
  - navigation [169](#ch09.xhtml_term-102), [170](#ch09.xhtml_term-103)
- [Command Line Interface (CLI) [120](#ch06.xhtml_term-104), [167](#ch09.xhtml_term-105)]
- [comma-separated value (CSV) file [80](#ch04.xhtml_term-106), [174](#ch09.xhtml_term-107)]
- [CONCATENATE() formula [110](#ch06.xhtml_term-108), *[111](#ch06.xhtml_term-109)*, [112](#ch06.xhtml_term-110)]
- [CONCAT() function [112](#ch06.xhtml_term-111)]
- [Conditional Formatting [74](#ch04.xhtml_term-112)]
- [confounding variables [73](#ch04.xhtml_term-113)]
- [correlation [[119--20](#ch06.xhtml_term-114)]]
- [crowdsourcing [[45--6](#ch02.xhtml_term-115)], [128](#ch07.xhtml_term-116)]
- [*Crusade for Justice* [1](#ch00_fm09_intro.xhtml_term-117)]
- [CSV file [*see* [comma-separated value (CSV) file](#ch13_index.xhtml_idx48)]]
- [Cuillier, D. [10](#ch01.xhtml_term-118), [12](#ch01.xhtml_term-119), [13](#ch01.xhtml_term-120), [15](#ch01.xhtml_term-121)]

<!-- -->

- [Dale, B. [187](#ch10.xhtml_term-122)]
- [data acquiring process [4](#ch00_fm09_intro.xhtml_term-123), [[9--10](#ch01.xhtml_term-124)];]
- [academic studies and expert sources [[21--3](#ch01.xhtml_term-125)]]
- basic search [[17--18](#ch01.xhtml_term-126)]
- data portals [[16--17](#ch01.xhtml_term-127)]
- evaluation of information [[23--5](#ch01.xhtml_term-128)]
- [freedom of information (FOI) laws [10](#ch01.xhtml_term-129)]
- Google search operators [[18--20](#ch01.xhtml_term-130)]
- public records request [[10--13](#ch01.xhtml_term-131)]
- request and denial decision [[13--15](#ch01.xhtml_term-132)]
- web address hacking [23](#ch01.xhtml_term-133)
- [database-/data-driven journalism [4](#ch00_fm09_intro.xhtml_term-134)]
- [database managers [142](#ch08.xhtml_term-135)]
- [data cleaning process [71](#ch04.xhtml_term-136)]
- finding empty values [74](#ch04.xhtml_term-137)
- finding errors [[71--3](#ch04.xhtml_term-138)]
- macros [74](#ch04.xhtml_term-139)
- OpenRefine [[79--81](#ch04.xhtml_term-140)], *[81](#ch04.xhtml_term-141)*
- Regular Expressions [[75--6](#ch04.xhtml_term-142)], **[76](#ch04.xhtml_term-143)**
- spreadsheet formulas *[78](#ch04.xhtml_term-144)*, [[78--9](#ch04.xhtml_term-145)]
- text editors [79](#ch04.xhtml_term-146)
- troubleshooting common programming errors [[83--5](#ch04.xhtml_term-147)]
- troubleshooting common spreadsheet errors [[82--3](#ch04.xhtml_term-148)]
- [data diaries [211](#ch11.xhtml_term-149), [213](#ch11.xhtml_term-150)]
- [data fact-checking [71](#ch04.xhtml_term-151)]
- [[[Data.gov](http://Data.gov)] [16](#ch01.xhtml_term-152), [29](#ch02.xhtml_term-153)]
- [[[data.gov.ru](http://data.gov.ru), Russia's open data portal] [29](#ch02.xhtml_term-154), *[30](#ch02.xhtml_term-155)*]
- [data-infused summary graph [136](#ch07.xhtml_term-156)]
- [data journalism [2](#ch00_fm09_intro.xhtml_term-157)]
  - definition of [[2--5](#ch00_fm09_intro.xhtml_term-158)]
  - history of [[6--8](#ch00_fm09_intro.xhtml_term-159)]
  - impact of [6](#ch00_fm09_intro.xhtml_term-160)
- [*The Data Journalism Handbook* [6](#ch00_fm09_intro.xhtml_term-161)]
- [data journalists [71](#ch04.xhtml_term-162), [191](#ch10.xhtml_term-163)]
- [data manipulation [152](#ch08.xhtml_term-164)]
- [[[DataPlusJournalism.com](http://DataPlusJournalism.com) blog] [7](#ch00_fm09_intro.xhtml_term-165)]
- [data portals [[16--17](#ch01.xhtml_term-166)]]
- [data reporting process [1](#ch00_fm09_intro.xhtml_term-167), *[3](#ch00_fm09_intro.xhtml_term-168)*, [[3--4](#ch00_fm09_intro.xhtml_term-169)]]
- [data scraping process [[49--51](#ch03.xhtml_term-170)]]
  - with browser extension [61](#ch03.xhtml_term-171)
  - with code [[59--61](#ch03.xhtml_term-172)]
  - documents [[61--5](#ch03.xhtml_term-173)]
  - Freedom of Information resources [68](#ch03.xhtml_term-174)
  - historical stock prices [65](#ch03.xhtml_term-175)
  - IMPORTHTML [[56--8](#ch03.xhtml_term-176)], *[57](#ch03.xhtml_term-177)*
  - multiple tables on web pages [55](#ch03.xhtml_term-178)
  - real-time stock data, into Google sheet [[64--5](#ch03.xhtml_term-179)]
  - tools [[69--70](#ch03.xhtml_term-180)]
  - from web [[51--5](#ch03.xhtml_term-181)]
  - XPaths creation [[58--9](#ch03.xhtml_term-182)]
- [datasets [[88--90](#ch05.xhtml_term-183)], [95](#ch05.xhtml_term-184)]
- [data's homepage [16](#ch01.xhtml_term-185), *[16](#ch01.xhtml_term-186)*]
- [data stories [[127--9](#ch07.xhtml_term-187)]]
  - angles for [133](#ch07.xhtml_term-188)
  - on beat [[134--8](#ch07.xhtml_term-189)]
  - declutter [135](#ch07.xhtml_term-190)
  - human-centered reporting [[130--3](#ch07.xhtml_term-191)]
  - in narrative form *[132](#ch07.xhtml_term-192)*
  - summary paragraphs and making numbers [[129--30](#ch07.xhtml_term-193)]
- [data transparency [211](#ch11.xhtml_term-194), [213](#ch11.xhtml_term-195)]
- [data visualization [[180--1](#ch10.xhtml_term-196)]]
  - bar/column chart [182](#ch10.xhtml_term-197)
  - chart-building tools [193](#ch10.xhtml_term-198)
  - charts and maps [[190--1](#ch10.xhtml_term-199)]
  - *Chicago Sun-Times* homicides database [186](#ch10.xhtml_term-200)
  - colors and fonts [192](#ch10.xhtml_term-201)
  - Geographic Information System Maps and Shapefiles [196](#ch10.xhtml_term-202)
  - hierarchy and organizational charts [183](#ch10.xhtml_term-203)
  - interactive and animated charts [[182--3](#ch10.xhtml_term-204)]
  - Kavanaugh testimony for Vox *[184](#ch10.xhtml_term-205)*
  - line charts [182](#ch10.xhtml_term-206)
  - mapping [194](#ch10.xhtml_term-207)
  - maps [[194--6](#ch10.xhtml_term-208)]
  - pie charts and treemaps [182](#ch10.xhtml_term-209)
  - right chart [[191--2](#ch10.xhtml_term-210)]
  - in US cities [181](#ch10.xhtml_term-211)
  - Venn diagrams [183](#ch10.xhtml_term-212)
- [data.world featured datasets [40](#ch02.xhtml_term-213), *[41](#ch02.xhtml_term-214)*]
- [Datawrapper, data visualization tool [4](#ch00_fm09_intro.xhtml_term-215), [7](#ch00_fm09_intro.xhtml_term-216), [192](#ch10.xhtml_term-217), [193](#ch10.xhtml_term-218), [196](#ch10.xhtml_term-219), [199](#ch11.xhtml_term-220), [207](#ch11.xhtml_term-221), *[208](#ch11.xhtml_term-222)*]
- [date serial number format [74](#ch04.xhtml_term-223), *[74](#ch04.xhtml_term-224)*]
- [DB Fiddle [[144--6](#ch08.xhtml_term-225)], *[145](#ch08.xhtml_term-226)*, [147](#ch08.xhtml_term-227)]
- [deep web, searching [[28--9](#ch02.xhtml_term-228)]]
  - government databases [29](#ch02.xhtml_term-229)
  - manual data entry [45](#ch02.xhtml_term-230)
  - nongovernmental databases [[32--3](#ch02.xhtml_term-231)]
  - own database creation [[42--3](#ch02.xhtml_term-232)]
  - social media [[36--40](#ch02.xhtml_term-233)]
  - tech products and archives [40](#ch02.xhtml_term-234)
  - tech source [42](#ch02.xhtml_term-235)
- [*Democracy's Detectives* (Hamilton) [6](#ch00_fm09_intro.xhtml_term-236)]
- [dependencies, installation of [171](#ch09.xhtml_term-237)]
- ["Digital Master" (Zhu) [9](#ch01.xhtml_term-238)]
- [[[DiverseSources.org](http://DiverseSources.org)] [22](#ch01.xhtml_term-239)]
- [documents, data scrapping [[61--5](#ch03.xhtml_term-240)]]
- [Doig, S. [227](#ch12.xhtml_term-241)]
- [Dowdell, J. [71](#ch04.xhtml_term-242), [72](#ch04.xhtml_term-243)]
- [Dublin Ireland data portal [17](#ch01.xhtml_term-244)]

<!-- -->

- [Eads, D. [202](#ch11.xhtml_term-245)]
- [empty values [74](#ch04.xhtml_term-246)]
- [errors, in data [[71--3](#ch04.xhtml_term-247)]]
- [ethical decision-making [199](#ch11.xhtml_term-248)]
- ["Ethical Infographics" [200](#ch11.xhtml_term-249)]
- [European Environment Agency [34](#ch02.xhtml_term-250)]
- [Eurostat [16](#ch01.xhtml_term-251)]
- [Evans, T. [136](#ch07.xhtml_term-252)]
- [ExpertiseFinder [22](#ch01.xhtml_term-253)]
- [[[ExportComments.com](http://ExportComments.com) Interface] [[66--8](#ch03.xhtml_term-254)], *[67](#ch03.xhtml_term-255)*, [68](#ch03.xhtml_term-256)]
- [Eyre, E. [129](#ch07.xhtml_term-257)]

<!-- -->

- [Facebook [39](#ch02.xhtml_term-258)]
- [Fazlollah, M. [30](#ch02.xhtml_term-259)]
- [Federal Bureau of Investigation (FBI) [29](#ch02.xhtml_term-260), [30](#ch02.xhtml_term-261)]
  - Uniform Crime Report [30](#ch02.xhtml_term-262), [72](#ch04.xhtml_term-263)
- [Federal Election Commission (FEC) [80](#ch04.xhtml_term-264)]
- [Federal Highway Administration [87](#ch05.xhtml_term-265)]
  - National Bridge Inventory database [138](#ch07.xhtml_term-266), [139](#ch07.xhtml_term-267)
- [FIFA's list of World Cup finalists in 1938 [43](#ch02.xhtml_term-268), *[43](#ch02.xhtml_term-269)*]
- [figuring rates [[98--100](#ch05.xhtml_term-270)], [*[99--101](#ch05.xhtml_term-271)*]]
- [file paths [169](#ch09.xhtml_term-272)]
- [filters [95](#ch05.xhtml_term-273), *[97](#ch05.xhtml_term-274)*, [98](#ch05.xhtml_term-275)]
- [Financial Times Visual Vocabulary cheat sheet [192](#ch10.xhtml_term-276)]
- [Flourish, data visualization tool [4](#ch00_fm09_intro.xhtml_term-277), [7](#ch00_fm09_intro.xhtml_term-278), [102](#ch05.xhtml_term-279), [192](#ch10.xhtml_term-280), [193](#ch10.xhtml_term-281), [196](#ch10.xhtml_term-282), [199](#ch11.xhtml_term-283), [209](#ch11.xhtml_term-284), *[209](#ch11.xhtml_term-285)*]
- [Floyd, G. [68](#ch03.xhtml_term-286)]
- [FOI [*see* [*see* freedom of information (FOI)](#ch13_index.xhtml_idx59a)]]
- [FOIA [*see* [Freedom of Information Act (FOIA)](#ch13_index.xhtml_idx124)]]
- [FOIA Public Liaison [11](#ch01.xhtml_term-287)]
- [fonts, for data visualization [192](#ch10.xhtml_term-288)]
- [formulas [109](#ch06.xhtml_term-289), [**[109--10](#ch06.xhtml_term-290)**]]
- [free data visualization tools [7](#ch00_fm09_intro.xhtml_term-291)]
- [freedom of information (FOI): data resources [68](#ch03.xhtml_term-292)]
  - laws [10](#ch01.xhtml_term-293), [11](#ch01.xhtml_term-294)
  - legislation [33](#ch02.xhtml_term-295)
- [Freedom of Information Act (FOIA) [11](#ch01.xhtml_term-296), [14](#ch01.xhtml_term-297)]
- [functions [*see* [formulas](#ch13_index.xhtml_idx121)]]

<!-- -->

- [Gehrke, M. [201](#ch11.xhtml_term-298)]
- [Geographic Information System (GIS) maps [196](#ch10.xhtml_term-299)]
- [Gillum, J. [160](#ch09.xhtml_term-300)]
- [GIS maps [*see* [Geographic Information System (GIS) maps](#ch13_index.xhtml_idx127)]]
- [GitHub [164](#ch09.xhtml_term-301), *[164](#ch09.xhtml_term-302)*, [202](#ch11.xhtml_term-303), [207](#ch11.xhtml_term-304)]
- [Google Colaboratory [60](#ch03.xhtml_term-305), *[60](#ch03.xhtml_term-306)*]
- [Google Colab platform [166](#ch09.xhtml_term-307), [169](#ch09.xhtml_term-308)]
- [Google Dataset Search: interface [[19--20](#ch01.xhtml_term-309)], *[22](#ch01.xhtml_term-310)*]
- tool [207](#ch11.xhtml_term-311), *[208](#ch11.xhtml_term-312)*
- [Google Doc [25](#ch01.xhtml_term-313), [90](#ch05.xhtml_term-314), [94](#ch05.xhtml_term-315)]
- [Google Finance stock scraping spreadsheet [65](#ch03.xhtml_term-316), *[66](#ch03.xhtml_term-317)*]
- [Google MyMaps *[138](#ch07.xhtml_term-318)*, [194](#ch10.xhtml_term-319), [196](#ch10.xhtml_term-320)]
- [Google Public Data Explorer [193](#ch10.xhtml_term-321)]
- [Google Scholar [21](#ch01.xhtml_term-322), [22](#ch01.xhtml_term-323), *[22](#ch01.xhtml_term-324)*]
- [Google search operators [[18--19](#ch01.xhtml_term-325)]]
- [Google Sheets [51](#ch03.xhtml_term-326), [52](#ch03.xhtml_term-327), [58](#ch03.xhtml_term-328), [61](#ch03.xhtml_term-329), [74](#ch04.xhtml_term-330), *[75](#ch04.xhtml_term-331)*, [[108--10](#ch06.xhtml_term-332)]]
  - bridge inspections database in *[88](#ch05.xhtml_term-333)*
  - city budget in [102](#ch05.xhtml_term-334), *[103](#ch05.xhtml_term-335)*, [[103--5](#ch05.xhtml_term-336)]
  - decrease decimal and percent buttons in *[92](#ch05.xhtml_term-337)*
  - and excel formulas [[224--6](#ch12.xhtml_term-338)]
  - figuring murders in *[220](#ch12.xhtml_term-339)*, [221](#ch12.xhtml_term-340)
  - formatting toolbar in [74](#ch04.xhtml_term-341)
  - formulas [99](#ch05.xhtml_term-342)
  - highlighting data in *[93](#ch05.xhtml_term-343)*
  - IMPORTHTML [56](#ch03.xhtml_term-344), [167](#ch09.xhtml_term-345)
  - macro menu in *[75](#ch04.xhtml_term-346)*
  - percentage in [[91--4](#ch05.xhtml_term-347)]
  - QUERY() function [141](#ch08.xhtml_term-348), [144](#ch08.xhtml_term-349)
  - REGEXEXTRACT() [77](#ch04.xhtml_term-350)
  - scraping real- time stock data into [[64--5](#ch03.xhtml_term-351)]
- [Google's powerful (but hidden) advanced search tool [18](#ch01.xhtml_term-352)]
- [government agencies [7](#ch00_fm09_intro.xhtml_term-353), [9](#ch01.xhtml_term-354), [13](#ch01.xhtml_term-355), [14](#ch01.xhtml_term-356), [17](#ch01.xhtml_term-357), [23](#ch01.xhtml_term-358)]
- [Groeger, L. [49](#ch03.xhtml_term-359), [51](#ch03.xhtml_term-360), [190](#ch10.xhtml_term-361)]
- [Groskopf, C. [80](#ch04.xhtml_term-362)]
- [GROUP BY: command groups [156](#ch08.xhtml_term-363)]
  - syntax [117](#ch06.xhtml_term-364)
- [grouping values [117](#ch06.xhtml_term-365), [[156--7](#ch08.xhtml_term-366)]]

<!-- -->

- [Hamilton, J. T.: *Democracy's Detectives* [6](#ch00_fm09_intro.xhtml_term-367)]
- [heat map [196](#ch10.xhtml_term-368)]
- [hierarchy chart [183](#ch10.xhtml_term-369)]
- [historical stock prices, data scrapping [65](#ch03.xhtml_term-370)]
- [horizontal bar charts [182](#ch10.xhtml_term-371)]
- [Houston, B. [6](#ch00_fm09_intro.xhtml_term-372)]
- [*Houston Chronicle* [2](#ch00_fm09_intro.xhtml_term-373), [127](#ch07.xhtml_term-374)]
- [*How Charts Lie* (Cairo) [191](#ch10.xhtml_term-375), [200](#ch11.xhtml_term-376)]
- [human-centered reporting [[130--3](#ch07.xhtml_term-377)]]

<!-- -->

- [IF Error [113](#ch06.xhtml_term-378), *[113](#ch06.xhtml_term-379)*]
- [[[iFOIA.org](http://iFOIA.org)] [[11--12](#ch01.xhtml_term-380)], *[14](#ch01.xhtml_term-381)*]
- [IF Statements [112](#ch06.xhtml_term-382), *[113](#ch06.xhtml_term-383)*]
- [IMF [*see* [International Monetary Fund (IMF)](#ch13_index.xhtml_idx165)]]
- [IMPORTHTML [[56--9](#ch03.xhtml_term-384)], *[57](#ch03.xhtml_term-385)*, [167](#ch09.xhtml_term-386), [174](#ch09.xhtml_term-387)]
- [Independent Petroleum Association of America [33](#ch02.xhtml_term-388), *[33](#ch02.xhtml_term-389)*]
- [Infogr.am, data visualization tool [7](#ch00_fm09_intro.xhtml_term-390)]
- [infographic tools [181](#ch10.xhtml_term-391), [193](#ch10.xhtml_term-392)]
- [Inner Joins [156](#ch08.xhtml_term-393)]
- [interactive chart [[182--3](#ch10.xhtml_term-394)]]
- [International Monetary Fund (IMF) [29](#ch02.xhtml_term-395)]
- [investigative journalism [4](#ch00_fm09_intro.xhtml_term-396)]
- [Investigative Reporters and Editors (IRE) [6](#ch00_fm09_intro.xhtml_term-397)]

<!-- -->

- [JavaScript [164](#ch09.xhtml_term-398), [165](#ch09.xhtml_term-399)]
- [joining datasets [154](#ch08.xhtml_term-400), *[155](#ch08.xhtml_term-401)*, [156](#ch08.xhtml_term-402)]
- [Joining ZIP codes, from multiple datasets [154](#ch08.xhtml_term-403), *[155](#ch08.xhtml_term-404)*]
- [journalism school [89](#ch05.xhtml_term-405), [217](#ch12.xhtml_term-406)]
- [journalists, math for [218](#ch12.xhtml_term-407)]
  - AP style and [226](#ch12.xhtml_term-408)
  - basic Google Sheets and excel formulas [[224--6](#ch12.xhtml_term-409)]
  - crowd sizes estimation [[226--7](#ch12.xhtml_term-410)]
  - figuring percentage change [[217--18](#ch12.xhtml_term-411)]
  - margin of error in polls [[221--2](#ch12.xhtml_term-412)]
  - mean [223](#ch12.xhtml_term-413)
  - median [[223--4](#ch12.xhtml_term-414)]
  - mode [224](#ch12.xhtml_term-415)
  - off by one error [[222--3](#ch12.xhtml_term-416)]
  - per capita and rates [[218--21](#ch12.xhtml_term-417)]
  - percentage change and points [218](#ch12.xhtml_term-418)
  - percentage increases exceeding 100 percent [218](#ch12.xhtml_term-419)
- [Journalist's Toolbox [22](#ch01.xhtml_term-420), [69](#ch03.xhtml_term-421), [192](#ch10.xhtml_term-422), [196](#ch10.xhtml_term-423)]
- [Jupyter Notebook [171](#ch09.xhtml_term-424), [172](#ch09.xhtml_term-425), *[173](#ch09.xhtml_term-426)*]

<!-- -->

- [Kamb, L. [127](#ch07.xhtml_term-427)]
- [Katsaros, C. [95](#ch05.xhtml_term-428), [102](#ch05.xhtml_term-429)]
- [Kavanaugh, B. [183](#ch10.xhtml_term-430)]
- [Keyhole Markup Language (KML) [196](#ch10.xhtml_term-431)]
- [keywords, SQL [**[143--4](#ch08.xhtml_term-432)**]]

<!-- -->

- [languages and libraries, installation of [167](#ch09.xhtml_term-433)]
- [LEFT() function, in SQL [152](#ch08.xhtml_term-434), *[153](#ch08.xhtml_term-435)*]
- [Lightfoot, L. [134](#ch07.xhtml_term-436), [210](#ch11.xhtml_term-437)]
- [LIKE operator **[148](#ch08.xhtml_term-438)**, *[151](#ch08.xhtml_term-439)*]
- [LIMIT command [147](#ch08.xhtml_term-440), [150](#ch08.xhtml_term-441)]
- [line charts [182](#ch10.xhtml_term-442), [188](#ch10.xhtml_term-443), [190](#ch10.xhtml_term-444)]
- [LinkedIn [39](#ch02.xhtml_term-445)]
- [locator map [195](#ch10.xhtml_term-446), [196](#ch10.xhtml_term-447)]
- [Lucidchart [183](#ch10.xhtml_term-448)]
- [lurking variable [73](#ch04.xhtml_term-449)]

<!-- -->

- [macros [74](#ch04.xhtml_term-450), *[75](#ch04.xhtml_term-451)*]
- [Mahomes, P. [[129--30](#ch07.xhtml_term-452)]]
- [manual data entry [45](#ch02.xhtml_term-453)]
- [map [[194--6](#ch10.xhtml_term-454)], *[195](#ch10.xhtml_term-455)*]
- [[[MapChecking.com](http://MapChecking.com)] [[226--7](#ch12.xhtml_term-456)]]
- [mapping [194](#ch10.xhtml_term-457), [196](#ch10.xhtml_term-458)]
- [math for journalists [218](#ch12.xhtml_term-459)]
  - AP style and [226](#ch12.xhtml_term-460)
  - basic google sheets and excel formulas [[224--6](#ch12.xhtml_term-461)]
  - crowd sizes estimation [[226--7](#ch12.xhtml_term-462)]
  - figuring percentage change [[217--18](#ch12.xhtml_term-463)]
  - margin of error in polls [[221--2](#ch12.xhtml_term-464)]
  - mean [223](#ch12.xhtml_term-465)
  - median [[223--4](#ch12.xhtml_term-466)]
  - mode [224](#ch12.xhtml_term-467)
  - off by one error [[222--3](#ch12.xhtml_term-468)]
  - per capita and rates [[218--21](#ch12.xhtml_term-469)]
  - percentage change and points [218](#ch12.xhtml_term-470)
  - percentage increases exceeding 100 percent [218](#ch12.xhtml_term-471)
- [Mayer, J. [203](#ch11.xhtml_term-472), [204](#ch11.xhtml_term-473)]
- [*Memphis Free Speech* [1](#ch00_fm09_intro.xhtml_term-474)]
- [metadata [160](#ch09.xhtml_term-475), [161](#ch09.xhtml_term-476)]
- [Meyer, P. [7](#ch00_fm09_intro.xhtml_term-477)]
- [*Miami Herald* [10](#ch01.xhtml_term-478)]
- [Microsoft Academic [21](#ch01.xhtml_term-479)]
- [mobile tools [193](#ch10.xhtml_term-480)]
- [Monarrez, T. [180](#ch10.xhtml_term-481), [181](#ch10.xhtml_term-482)]

<!-- -->

- [National Archives [11](#ch01.xhtml_term-483)]
- [National Bridge Inventory Bridge Inspection Safety database [87](#ch05.xhtml_term-484)]
- [National Freedom of Information Coalition [15](#ch01.xhtml_term-485)]
- [National Institute for Computer-Assisted Reporting (NICAR) [6](#ch00_fm09_intro.xhtml_term-486)]
- [National Public Radio [22](#ch01.xhtml_term-487)]
- [National Statistical Institutes [16](#ch01.xhtml_term-488)]
- [nested elements *[51](#ch03.xhtml_term-489)*, [52](#ch03.xhtml_term-490)]
- [nested functions [114](#ch06.xhtml_term-491), *[116](#ch06.xhtml_term-492)*, [117](#ch06.xhtml_term-493)]
- [nested queries [151](#ch08.xhtml_term-494)]
- [Network panel [163](#ch09.xhtml_term-495)]
- [*New Precision Journalism* [7](#ch00_fm09_intro.xhtml_term-496)]
- [*New York Times* [34](#ch02.xhtml_term-497)]
- [NICAR [*see* [National Institute for Computer-Assisted Reporting (NICAR)](#ch13_index.xhtml_idx209)]]

<!-- -->

- [Obama, B. [80](#ch04.xhtml_term-498)]
- [Office of Government Information Services (OGIS) [11](#ch01.xhtml_term-499)]
- [Olsen, L. [2](#ch00_fm09_intro.xhtml_term-500), [[127--8](#ch07.xhtml_term-501)]]
- [online databases [22](#ch01.xhtml_term-502)]
- [Open Knowledge Foundation [16](#ch01.xhtml_term-503)]
- [OpenRefine programs [[79--81](#ch04.xhtml_term-504)], *[81](#ch04.xhtml_term-505)*, [152](#ch08.xhtml_term-506)]
- [ORDER BY command [157](#ch08.xhtml_term-507), *[158](#ch08.xhtml_term-508)*]
- [organizational chart [183](#ch10.xhtml_term-509)]
- [[[OrgCharting.com](http://OrgCharting.com)] [183](#ch10.xhtml_term-510)]
- [Outer Joins [156](#ch08.xhtml_term-511)]

<!-- -->

- [packages [124](#ch06.xhtml_term-512), *[124](#ch06.xhtml_term-513)*]
- [Page, L. [17](#ch01.xhtml_term-514)]
- ["Painkiller Profiteers" [129](#ch07.xhtml_term-515)]
- [painstaking process [71](#ch04.xhtml_term-516)]
- [Pandas Python library [59](#ch03.xhtml_term-517)]
- [pie charts [182](#ch10.xhtml_term-518)]
- [pin map [194](#ch10.xhtml_term-519)]
- [PIOs [*see* [public information officers (PIOs)](#ch13_index.xhtml_idx245)]]
- [pivot tables [117](#ch06.xhtml_term-520), *[118](#ch06.xhtml_term-521)*, [119](#ch06.xhtml_term-522)]
- [Power Five conferences [95](#ch05.xhtml_term-523)]
- [*Precision Journalism* [7](#ch00_fm09_intro.xhtml_term-524)]
- [presenting data [4](#ch00_fm09_intro.xhtml_term-525)]
- [Pritzker, J. B. [210](#ch11.xhtml_term-526)]
- [ProfNet [23](#ch01.xhtml_term-527)]
- [programming glossary [**[175--8](#ch09.xhtml_term-528)**]]
- [programming languages *[164](#ch09.xhtml_term-529)*, [[164--5](#ch09.xhtml_term-530)]]
- [public information officers (PIOs) [[11--13](#ch01.xhtml_term-531)], [17](#ch01.xhtml_term-532), [24](#ch01.xhtml_term-533)]
- [public records [10](#ch01.xhtml_term-534), [15](#ch01.xhtml_term-535)]
  - law [[12--13](#ch01.xhtml_term-536)]
  - request [[10--13](#ch01.xhtml_term-537)]
- [Pulitzer Prize for Explanatory Reporting, 2021 [45](#ch02.xhtml_term-538), *[45](#ch02.xhtml_term-539)*]
- [Python code [7](#ch00_fm09_intro.xhtml_term-540), [165](#ch09.xhtml_term-541)]
  - in MacOS terminal [168](#ch09.xhtml_term-542), *[169](#ch09.xhtml_term-543)*
- [Python library [165](#ch09.xhtml_term-544)]
- [Python website [167](#ch09.xhtml_term-545)]

<!-- -->

- [queries, SQL [[125--6](#ch06.xhtml_term-546)], [142](#ch08.xhtml_term-547)]

<!-- -->

- [R: analysis in [120](#ch06.xhtml_term-548), *[120](#ch06.xhtml_term-549)*]
- summary functions [[122--4](#ch06.xhtml_term-550)], *[123](#ch06.xhtml_term-551)*
- [RCFP's Open Government Guide [15](#ch01.xhtml_term-552)]
- [*Reader on Data Visualization* [200](#ch11.xhtml_term-553)]
- [real-time stock data, into Google sheet [[64--5](#ch03.xhtml_term-554)]]
- [[[RedLineProject.org](http://RedLineProject.org)] [95](#ch05.xhtml_term-555), [138](#ch07.xhtml_term-556)]
- [REGEXEXTRACT() formula *[77](#ch04.xhtml_term-557)*, [[77--8](#ch04.xhtml_term-558)], [117](#ch06.xhtml_term-559)]
- [Regular Expressions (RegEx) [[75--7](#ch04.xhtml_term-560)], **[76](#ch04.xhtml_term-561)**]
- [Reporters Committee for Freedom [14](#ch01.xhtml_term-562)]
- [RStudio [7](#ch00_fm09_intro.xhtml_term-563), [193](#ch10.xhtml_term-564)]
  - import wizard [121](#ch06.xhtml_term-565), *[122](#ch06.xhtml_term-566)*
- [RStudio Cloud [120](#ch06.xhtml_term-567), *[120](#ch06.xhtml_term-568)*]
- [RStudio Packages pane *[124](#ch06.xhtml_term-569)*]
- [RTI Rating [10](#ch01.xhtml_term-570)]
- [rule of thumb [136](#ch07.xhtml_term-571)]
- [Russell, D. [18](#ch01.xhtml_term-572)]

<!-- -->

- [Schock, A. [160](#ch09.xhtml_term-573)]
- [scraping social media [[160--1](#ch09.xhtml_term-574)]]
  - with APIs [[173--4](#ch09.xhtml_term-575)]
  - with code [169](#ch09.xhtml_term-576)
  - coding challenges [[165--6](#ch09.xhtml_term-577)]
  - coding terminology [166](#ch09.xhtml_term-578)
  - Command Line [167](#ch09.xhtml_term-579)
  - digging into code [161](#ch09.xhtml_term-580)
  - file paths [169](#ch09.xhtml_term-581)
  - installing dependencies [171](#ch09.xhtml_term-582)
  - languages and libraries, installation [167](#ch09.xhtml_term-583)
  - programming glossary [**[175--8](#ch09.xhtml_term-584)**]
  - programming languages [[164--5](#ch09.xhtml_term-585)]
  - script writing [172](#ch09.xhtml_term-586), [173](#ch09.xhtml_term-587)
  - virtual environments [170](#ch09.xhtml_term-588)
- [script writing [[172--3](#ch09.xhtml_term-589)]]
- [SEARCH() function [[114--15](#ch06.xhtml_term-590)]]
- [search operators [**[148--9](#ch08.xhtml_term-591)**], [150](#ch08.xhtml_term-592)]
- [*Seattle Post-Intelligencer* series [127](#ch07.xhtml_term-593)]
- [SELECT command [[146--7](#ch08.xhtml_term-594)], [154](#ch08.xhtml_term-595)]
- [sharing data, on social media [[210--11](#ch11.xhtml_term-596)]]
- [Sherman, L. [204](#ch11.xhtml_term-597)]
- [simple SELECT statement *[148](#ch08.xhtml_term-598)*, [154](#ch08.xhtml_term-599)]
- [social media [[36--40](#ch02.xhtml_term-600)]]
  - scraping comments from [[66--8](#ch03.xhtml_term-601)]
  - sharing data on [[210--11](#ch11.xhtml_term-602)]
- [social networks [40](#ch02.xhtml_term-603)]
- [Society of Professional Journalists (SPJ) [14](#ch01.xhtml_term-604), [199](#ch11.xhtml_term-605)]
- [software engineering [165](#ch09.xhtml_term-606)]
- [sorting [157](#ch08.xhtml_term-607), [159](#ch08.xhtml_term-608)]
- [Sort Range interface [92](#ch05.xhtml_term-609), *[93](#ch05.xhtml_term-610)*, [94](#ch05.xhtml_term-611)]
- [source code [161](#ch09.xhtml_term-612)]
- [SPJ [*see* [Society of Professional Journalists (SPJ)](#ch13_index.xhtml_idx278)]]
- [SPJ Code of Ethics [[199--200](#ch11.xhtml_term-613)]]
- [SPLIT() formula *[78](#ch04.xhtml_term-614)*, [[78--9](#ch04.xhtml_term-615)], [110](#ch06.xhtml_term-616)]
- [*Spotlight* (movie) [71](#ch04.xhtml_term-617)]
- [spreadsheet: data into [[87--8](#ch05.xhtml_term-618)]]
  - formulas [[78--9](#ch04.xhtml_term-619)]
  - program [74](#ch04.xhtml_term-620)
- [SQL [*see* [structured query language (SQL)](#ch13_index.xhtml_idx291)]]
- [SQL Schema panel [147](#ch08.xhtml_term-621)]
- [SQL statements [142](#ch08.xhtml_term-622), [144](#ch08.xhtml_term-623)]
- [structured query language (SQL) [46](#ch02.xhtml_term-624), [[141--2](#ch08.xhtml_term-625)]]
  - cleaning method [152](#ch08.xhtml_term-626)
  - filtering [146](#ch08.xhtml_term-627), [147](#ch08.xhtml_term-628), [150](#ch08.xhtml_term-629), [152](#ch08.xhtml_term-630)
  - grouping [[156--7](#ch08.xhtml_term-631)]
  - importing [142](#ch08.xhtml_term-632), [144](#ch08.xhtml_term-633)
  - joining datasets [154](#ch08.xhtml_term-634), *[155](#ch08.xhtml_term-635)*, [156](#ch08.xhtml_term-636)
  - keywords [**[143--4](#ch08.xhtml_term-637)**]
  - nested queries [151](#ch08.xhtml_term-638)
  - queries [142](#ch08.xhtml_term-639)
  - sorting [157](#ch08.xhtml_term-640), [159](#ch08.xhtml_term-641)
- [Stylianou, N. [187](#ch10.xhtml_term-642)]
- [sunshine laws [11](#ch01.xhtml_term-643), [14](#ch01.xhtml_term-644)]
- [survey tools [45](#ch02.xhtml_term-645)]
- [Swisher, K. [204](#ch11.xhtml_term-646), *[205](#ch11.xhtml_term-647)*]
- [symbol map [[194--5](#ch10.xhtml_term-648)]]

<!-- -->

- [Tableau Public [193](#ch10.xhtml_term-649), [194](#ch10.xhtml_term-650)]
- [Tableizer [209](#ch11.xhtml_term-651), *[210](#ch11.xhtml_term-652)*]
- [tab references [109](#ch06.xhtml_term-653)]
- [Tabula scraping interface [62](#ch03.xhtml_term-654), *[62](#ch03.xhtml_term-655)*]
- [tech source [42](#ch02.xhtml_term-656)]
- [*Texas Observer* [2](#ch00_fm09_intro.xhtml_term-657)]
- [text editors [79](#ch04.xhtml_term-658)]
- [Tharpe, C. [95](#ch05.xhtml_term-659), [102](#ch05.xhtml_term-660)]
- [Thuy Vo, L. [173](#ch09.xhtml_term-661), [174](#ch09.xhtml_term-662)]
- [tidyverse package [124](#ch06.xhtml_term-663), [125](#ch06.xhtml_term-664)]
- ["Transparency as a Key Element of Data Journalism" [201](#ch11.xhtml_term-665)]
- [transposing [117](#ch06.xhtml_term-666)]
- [treemaps [182](#ch10.xhtml_term-667)]
- [troubleshooting: common programming errors [[83--5](#ch04.xhtml_term-668)]]
  - common spreadsheet errors [[82--3](#ch04.xhtml_term-669)]
- ["trust nugget" tool [204](#ch11.xhtml_term-670)]
- [Twint Python library [165](#ch09.xhtml_term-671), [171](#ch09.xhtml_term-672)]
- [Twint website [171](#ch09.xhtml_term-673)]
- [Twitter *[37](#ch02.xhtml_term-674)*, [39](#ch02.xhtml_term-675)]

<!-- -->

- [*United States Petroleum Statistics* [33](#ch02.xhtml_term-676), *[33](#ch02.xhtml_term-677)*]
- [US Data Portal Github [17](#ch01.xhtml_term-678)]
- [useful libraries list [165](#ch09.xhtml_term-679), **[165](#ch09.xhtml_term-680)**]
- [US Postal Service performance data [23](#ch01.xhtml_term-681), *[24](#ch01.xhtml_term-682)*, [56](#ch03.xhtml_term-683)]

<!-- -->

- [varchar datapoint [[145--6](#ch08.xhtml_term-684)]]
- [Vasquez, D. [127](#ch07.xhtml_term-685)]
- [Venn diagrams [183](#ch10.xhtml_term-686)]
- [vertical column charts [182](#ch10.xhtml_term-687)]
- [virtual environments [167](#ch09.xhtml_term-688), [170](#ch09.xhtml_term-689)]

<!-- -->

- [Wallack, T. [14](#ch01.xhtml_term-690)]
- [Walsh, L. [5](#ch00_fm09_intro.xhtml_term-691), [[203--4](#ch11.xhtml_term-692)], [206](#ch11.xhtml_term-693)]
- [Walton, J. [7](#ch00_fm09_intro.xhtml_term-694), [135](#ch07.xhtml_term-695), [[187--9](#ch10.xhtml_term-696)]]
- [[[WashingtonPost.com](http://WashingtonPost.com)] [49](#ch03.xhtml_term-697), *[50](#ch03.xhtml_term-698)*]
- [web address, hacking [23](#ch01.xhtml_term-699)]
- [Web Inspector "inspect element" tool [162](#ch09.xhtml_term-700), *[162](#ch09.xhtml_term-701)*]
- [Web Inspector Network panel [163](#ch09.xhtml_term-702), *[163](#ch09.xhtml_term-703)*]
- [Web Inspector on Google Chrome [49](#ch03.xhtml_term-704), *[50](#ch03.xhtml_term-705)*, [58](#ch03.xhtml_term-706)]
- [web pages, multiple tables on [[55--8](#ch03.xhtml_term-707)]]
- [web scrapping, from data [[51--5](#ch03.xhtml_term-708)]]
- [Webster, M. J. [213](#ch11.xhtml_term-709), *[214](#ch11.xhtml_term-710)*]
- [Wells, I. B. [1](#ch00_fm09_intro.xhtml_term-711), [6](#ch00_fm09_intro.xhtml_term-712)]
- [WHERE command [150](#ch08.xhtml_term-713)]
- [WHO [*see* [World Health Organization (WHO)](#ch13_index.xhtml_idx342)]]
- [Willis, D. [[88--9](#ch05.xhtml_term-714)]]
- [WordPress tool [204](#ch11.xhtml_term-715)]
- [World Bank [16](#ch01.xhtml_term-716)]
- [World Economic Factbook [29](#ch02.xhtml_term-717)]
- [World Health Organization (WHO) [16](#ch01.xhtml_term-718), [160](#ch09.xhtml_term-719), *[161](#ch09.xhtml_term-720)*]
- [World Resource Institute [33](#ch02.xhtml_term-721)]
- [World Wide Web [17](#ch01.xhtml_term-722)]
- [writing code [59](#ch03.xhtml_term-723), [120](#ch06.xhtml_term-724), [165](#ch09.xhtml_term-725), [166](#ch09.xhtml_term-726), [167](#ch09.xhtml_term-727)]

<!-- -->

- [XPaths [[58--9](#ch03.xhtml_term-728)]]

<!-- -->

- [Zhu, P.: "Digital Master" [9](#ch01.xhtml_term-729)]
- [ZIP codes [[151--6](#ch08.xhtml_term-730)], *[155](#ch08.xhtml_term-731)*]
