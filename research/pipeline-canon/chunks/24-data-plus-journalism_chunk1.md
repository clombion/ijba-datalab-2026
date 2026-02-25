<!-- chunk: 1/2 | source: 24-data-plus-journalism.md | words: 38846 -->
<!-- headings: Tables; Figures; Acknowledgments; IntroductionThe Power of Data Storytelling; What Is Data Journalism?; Ethics, Trust and Data; Impact of Data Journalism; History of Data Journalism; Footnotes; 1 Acquiring Data; Using FOI Laws; Making a Public Records Request; Pro Tip ![](images/Pro_Tip_Icon.jpg); Appealing a Request Denial; Five Tips for Getting Public Records; Using Data Portals; Read More: Glossary ![](images/Read_More_Icon.jpg); Basic Search; Google's Powerful (but Hidden) Advanced Search Tool; Google Search Operators -->

Designed cover image: © Illustration by Billy O'Keefe

First published 2023

by Routledge

605 Third Avenue, New York, NY 10158

and by Routledge

4 Park Square, Milton Park, Abingdon, Oxon, OX14 4RN

*Routledge is an imprint of the Taylor & Francis Group, an informa business*


The right of Mike Reilley and Samantha Sunne to be identified as authors of this work has been asserted in accordance with sections 77 and 78 of the Copyright, Designs and Patents Act 1988.


*Trademark notice*: Product or corporate names may be trademarks or registered trademarks, and are used only for identification and explanation without intent to infringe.

*Library of Congress Cataloging-in-Publication Data*

Names: Reilley, Mike, 1965-- author. \| Sunne, Samantha, 1991-- author.

Title: Data + journalism: a story-driven approach to learning data reporting / Mike Reilley and Samantha Sunne.

Other titles: Data \[plus\] journalism

Description: New York: Routledge, 2022. \| Includes bibliographical references and index.

Identifiers: LCCN 2022028643 \| ISBN 9781032226125 (hardback) \| ISBN 9781032225913 (paperback) \| ISBN 9781003273301 (ebook)

Subjects: LCSH: Journalism---Data processing. \| Data mining.

Classification: LCC PN4784.E5 R45 2023 \| DDC 070.4/0285---dc23/eng/20220924

LC record available at <https://lccn.loc.gov/2022028643>


DOI: [10.4324/9781003273301](http://dx.doi.org/10.4324/10.4324/9781003273301){aria-label="D.O.I. link to this document."}

Typeset in Goudy

by codeMantra

Access the companion website: <http://dataplusjournalism.com>


**To my parents, who taught me never to give up. And to my wife, Isabella, who helped me beat cancer.**

**---​Mike**

**To my mom, who always said I could be a writer.**

**---​Samantha**


# Tables

- [2.1 A table of World Cup winners by year](#ch02.xhtml_t2_1)
- [2.2 A table of World Cup winners by country](#ch02.xhtml_t2_2)
- [4.1 Useful RegEx Phrases](#ch04.xhtml_t4_1)
- [6.1 Common Formulas](#ch06.xhtml_t6_1)
- [8.1 Common SQL Keywords](#ch08.xhtml_t8_1)
- [8.2 Common Search Operators](#ch08.xhtml_t8_2)
- [9.1 Useful Libraries](#ch09.xhtml_t9_1)
- [9.2 Programming Glossary](#ch09.xhtml_t9_2)
- [12.1 Basic Calculations](#ch12.xhtml_t12_1)


# Figures

- [0.1 Ida B. Wells](#ch00_fm09_intro.xhtml_f0_1)
- [0.2 The data reporting process (Illustration/Billy O'Keefe)](#ch00_fm09_intro.xhtml_f0_2)
- [1.1 iFOIA.org's letter generator](#ch01.xhtml_f1_1)
- [1.2 Our World in Data's homepage](#ch01.xhtml_f1_2)
- [1.3 Site: operator search on the CDC.gov site for SARS](#ch01.xhtml_f1_3)
- [1.4 Google Dataset Search interface](#ch01.xhtml_f1_4)
- [1.5 Google Scholar author page](#ch01.xhtml_f1_5)
- [1.6 US Postal Service performance data](#ch01.xhtml_f1_6)
- [2.1 data.gov.ru, Russia's open data portal](#ch02.xhtml_f2_1)
- [2.2 The *United States Petroleum Statistics*, published by the Independent Petroleum Association of America](#ch02.xhtml_f2_2)
- [2.3 Twitter advanced search](#ch02.xhtml_f2_3)
- [2.4 data.world featured datasets](#ch02.xhtml_f2_4)
- [2.5 FIFA's list of World Cup finalists in 1938](#ch02.xhtml_f2_5)
- [2.6 The 2021 Pulitzer Prize for Explanatory Reporting award winning project, Shielded](#ch02.xhtml_f2_6)
- [3.1 WashingtonPost.com viewed through the Web Inspector on Google Chrome](#ch03.xhtml_f3_1)
- [3.2 Obtaining data from sources diagram (Illustration/Billy O'Keefe)](#ch03.xhtml_f3_2)
- [3.3 Nested Tables diagram (Illustration/Billy O'Keefe)](#ch03.xhtml_f3_3)
- [3.4 Scraping with ImportHTML](#ch03.xhtml_f3_4)
- [3.5 Scraping specific data with ImportXML](#ch03.xhtml_f3_5)
- [3.6 Google Colaboratory](#ch03.xhtml_f3_6)
- [3.7 Tabula scraping interface](#ch03.xhtml_f3_7)
- [3.8 Google Finance stock scraping spreadsheet](#ch03.xhtml_f3_8)
- [3.9 ExportComments.com Interface](#ch03.xhtml_f3_9)
- [3.10 Download interface on ExportComments.com](#ch03.xhtml_f3_10)
- [4.1 The date serial number format](#ch04.xhtml_f4_1)
- [4.2 The Macro menu in Google Sheets](#ch04.xhtml_f4_2)
- [4.3 The REGEXEXTRACT() formula](#ch04.xhtml_f4_3)
- [4.4 The SPLIT() formula](#ch04.xhtml_f4_4)
- [4.5 OpenRefine text facet](#ch04.xhtml_f4_5)
- [4.6 The OpenRefine cluster window](#ch04.xhtml_f4_6)
- [5.1 Bridge inspections database in Google Sheets](#ch05.xhtml_f5_1)
- [5.2 The decrease decimal and percent buttons in Google Sheets](#ch05.xhtml_f5_2)
- [5.3 Highlighting data in the sheet prior to sorting](#ch05.xhtml_f5_3)
- [5.4 Sort Range in the Data pull-​down menu](#ch05.xhtml_f5_4)
- [5.5 Sort Range interface](#ch05.xhtml_f5_5)
- [5.6 Big Ten positive COVID-​19 cases by university](#ch05.xhtml_f5_6)
- [5.7 Data/Create a Filter pull-​down menu](#ch05.xhtml_f5_7)
- [5.8 Filters](#ch05.xhtml_f5_8)
- [5.9 Filter pull-​down](#ch05.xhtml_f5_9)
- [5.10 Sum formula](#ch05.xhtml_f5_10)
- [5.11 Autofill columns](#ch05.xhtml_f5_11)
- [5.12 The sorted sheet](#ch05.xhtml_f5_12)
- [5.13 City budget percent change column in Google Sheets](#ch05.xhtml_f5_13)
- [5.14 City Budget percentage of total budget column in Google Sheets](#ch05.xhtml_f5_14)
- [5.15 Budget totals a fact-​check totals rows on the city budget in Google Sheets](#ch05.xhtml_f5_15)
- [6.1 The Concatenate formula](#ch06.xhtml_f6_1)
- [6.2 IF statements](#ch06.xhtml_f6_2)
- [6.3 IFError formula](#ch06.xhtml_f6_3)
- [6.4 The nested Search and Mid functions](#ch06.xhtml_f6_4)
- [6.5 The pivot table editor](#ch06.xhtml_f6_5)
- [6.6 The finished pivot table](#ch06.xhtml_f6_6)
- [6.7 The RStudio Cloud panes](#ch06.xhtml_f6_7)
- [6.8 The RStudio import wizard](#ch06.xhtml_f6_8)
- [6.9 R summary functions](#ch06.xhtml_f6_9)
- [6.10 The RStudio Packages pane](#ch06.xhtml_f6_10)
- [6.11 Filtering in R](#ch06.xhtml_f6_11)
- [7.1 Structuring a data story in narrative form. (Illustration/Billy O'Keefe)](#ch07.xhtml_f7_1)
- [7.2 A layered map of 2014 Chicago pothole repairs by neighborhood. The map was built in Google MyMaps](#ch07.xhtml_f7_2)
- [8.1 Importing via the text to DDL window in DB fiddle](#ch08.xhtml_f8_1)
- [8.2 The simple SELECT statement](#ch08.xhtml_f8_2)
- [8.3 The AND and LIKE operators](#ch08.xhtml_f8_3)
- [8.4 The LEFT() function in SQL](#ch08.xhtml_f8_4)
- [8.5 Joining ZIP codes from multiple datasets](#ch08.xhtml_f8_5)
- [8.6 Selecting the average income and city](#ch08.xhtml_f8_6)
- [8.7 Ordering by average income](#ch08.xhtml_f8_7)
- [9.1 WHO Instagram post](#ch09.xhtml_f9_1)
- [9.2 The Web Inspector "inspect element" tool](#ch09.xhtml_f9_2)
- [9.3 The Web Inspector Network panel](#ch09.xhtml_f9_3)
- [9.4 Popular coding languages on Github](#ch09.xhtml_f9_4)
- [9.5 Python in a MacOS terminal](#ch09.xhtml_f9_5)
- [9.6 Navigating the command line](#ch09.xhtml_f9_6)
- [9.7 Script and output in Jupyter Notebook](#ch09.xhtml_f9_7)
- [10.1 How Chang used choropleth maps and Monarrez's data to visualize segregation in six US cities](#ch10.xhtml_f10_1)
- [10.2 Chang's visualization of the Kavanaugh testimony for Vox](#ch10.xhtml_f10_2)
- [10.3 *Chicago Sun-​Times* homicides victims database](#ch10.xhtml_f10_3)
- [10.4 *Chicago Sun-​Times* homicides database: Profiles of victims in Auburn Gresham neighborhood](#ch10.xhtml_f10_4)
- [10.5 BBC time ​lapse chart on 50-​degree Celsius days](#ch10.xhtml_f10_5)
- [10.6 *Chicago Sun-​Times* choropleth map shows which Chicago police districts have the most homicides per 10,000 people in 2021](#ch10.xhtml_f10_6)
- [11.1 Ethics statement from Kara Swisher's Vox Media bio](#ch11.xhtml_f11_1)
- [11.2 Google Dataset Search posting criteria](#ch11.xhtml_f11_2)
- [11.3 This open-​source graphic from Datawrapper has a link to the source of the data and a "Get the Data" link to the spreadsheet](#ch11.xhtml_f11_3)
- [11.4 College football coaches salary database made with Flourish](#ch11.xhtml_f11_4)
- [11.5 Tableizer with Chicago's annual homicide rate data in it](#ch11.xhtml_f11_5)
- [11.6 Heather Cherone's daily COVID-​19 data updates](#ch11.xhtml_f11_6)
- [11.7 Cherone responds to Twitter followers who have questions about the city's COVID-​19 death rate](#ch11.xhtml_f11_7)
- [11.8 Mary Jo Webster's Twitter thread for Justice Denied](#ch11.xhtml_f11_8)
- [12.1 Murders sorted in descending order](#ch12.xhtml_f12_1)
- [12.2 Figuring murders by population in Google Sheets](#ch12.xhtml_f12_2)
- [12.3 Figuring murders per 100,000 residents in Google Sheets](#ch12.xhtml_f12_3)


# Acknowledgments

We would like to thank many people who helped us with the writing and publishing of this book. Being a first-​time author can be challenging, but a great support team and cooperation from many professional journalists made it much easier. We're grateful to our publisher, Routledge, and the team of Lizzie Cox, Hannah McKeating and Priscille Biehlmann, who helped us navigate the process. Their patience and sense of humor were greatly appreciated.

We also want to thank David Cuillier of the University of Arizona, for lending us his expertise on freedom of information and public records around the world. Lise Olsen, an investigative journalist with the *Texas Observer* and author of the book *Code of Silence*, shared nearly three decades of experience writing data-​driven stories. Heather Cherone, the Chicago politics reporter at WTTW, shared how to work data reporting into daily online and TV news coverage.

Alvin Chang, head of visuals and data for *The Guardian US*, gave us some keen insights into designing graphics, and Lynn Walsh of Trusting News kept us on the cutting edge of building trust with readers through data stories. John Walton, data journalism editor at BBC News' data journalism team, and Andy Boyle, director of product engineering at the *Chicago Sun-​Times*, shared their innovative graphics and databases for international and local audiences.

Mike would like to thank his department chair at the University of Illinois--​Chicago, Zizi Papacharissi, for her encouragement and longtime support not only for this textbook but also for moving data journalism to the core of University of Illinois--​Chicago's journalism offerings.

Samantha would like to thank the community at Investigative Reporters and Editors, who elevate journalism in every field, and give a salute to the data journalists who made this whole universe possible, including Steve Doig, Sarah Cohen, Brant Houston and Cheryl Phillips, among others. Thank you to Carlie Procell, Lukas Udstuen and Lucia Walinchus for their technical expertise; Jian Chung Lee for individual projects; and Marissa DeCuir of Books Forward for advice.


# IntroductionThe Power of Data Storytelling

DOI: [10.4324/9781003273301-1](https://doi.org/10.4324/9781003273301-1){aria-label="D.O.I. link to this document."}

In 1892, nearly 75 years before data journalism found its way into newsrooms, Ida B. Wells returned to Memphis from a promotional tour for her newspaper, the *Memphis Free Speech*. She found the city in peril -- ​a white mob had lynched three Black men after a conflict between a white man and a Black man had escalated for a few days.

Wells began to research why those and many other lynchings happened -- ​by using what we know today as data reporting techniques.

She went to the places where the lynchings happened, compiling data from newspapers and firsthand interviews. She counted not just the lynchings but also how many had occurred due to an accusation of a Black man attacking or harassing a white woman. This provided the foundation for a series of articles and editorials that she published in the *Free Speech*. In her autobiography, *Crusade for Justice*, Wells later wrote, "They had committed no crime against white women. This is what opened my eyes to what lynching really was."

After publishing a series of articles and editorials using the data, Wells was issued a warning from those she exposed: If she returned, she would be lynched. After a mob in Memphis trashed her newspaper office, friends in New York implored her not to go back -- ​and she didn't ([Figure 0.1](#ch00_fm09_intro.xhtml_f0_1)).


While Wells didn't have RStudio, SQLite or glitzy mapping software to tell her story, she understood one of the fundamentals of data journalism -- ​in order to show the scale of a problem, just start counting.

Her story, portrayed in an audio mini-​documentary on the Center for Documentary Studies' Scene on Radio, clearly shows the impact of what we know today as data journalism. It tells complicated stories more clearly than relying on words, quotes and anecdotes alone. Data lends credibility to stories and unearths disturbing trends and corruption. Today, it helps the reader understand a story on a deeper level through analyses, maps, charts and databases.

Wells' boots-​on-​the-​ground reporting, combined with her data analysis, lifted her story to a different level. That's the goal of this textbook -- ​to elevate your reporting by taking a different approach. Data reporting techniques have existed for more than a century as journalists have collected and counted information for stories. But with the emergence of technology in the latter half of the 20th century, computer-​assisted reporting and what we know today as data journalism became embedded in newsrooms large and small.

"Data journalism has been important -- ​crucial -- ​for more than 30 years now," said Lise Olsen, an investigative reporter and editor at the *Texas Observer* whose work has appeared in Inside Climate, NBC, *Houston Chronicle*, and in documentaries on A&E and CNN. "Without knowing how to analyze data, a journalist must go nearly blind into the world of reporting.

"So much data is digital, that if a reporter doesn't know how to interpret numbers, statistics or recognize basic formats, he or she will miss crucial opportunities or be far too easily fooled by spin masters and fake news."

::: section

## What Is Data Journalism?

> *What makes it data journalism isn't the form, it's the starting point in a data source we corralled, cleaned and interpreted.*
>
> -- ​Melissa Bell, Vox Media publisher

Those words, written by Bell in 2015, best summarize *Data + Journalism*'s approach. Data journalism is the use of data and statistical analysis to uncover, better explain and/or provide context to a news story. Some data stories take months to report and publish, while others can be turned around in a day or two. Either way, reporters, editors and designers follow a process to tell those stories.

Specialized data journalism skills focus on acquiring, cleaning, analyzing and visualizing data, a process we follow in this book ([Figure 0.2](#ch00_fm09_intro.xhtml_f0_2)):

- **Acquiring data** includes knowing what public records exist and how to obtain them, as well as seeking numbers suitable for spreadsheets or databases.
- **Cleaning data** involves software and human intelligence to standardize spelling, punctuation and formatting to obtain accurate counts.
- **Analyzing data** may be accomplished with spreadsheets, programming languages, database management systems or visual representations to find commonalities or outliers.
- **Presenting data** involves building maps, interactive charts or graphics to enable audiences to comprehend the analysis or personalize the data through interactives.


This book follows that reporting process, offering the skills and exercises journalists need to practice the craft. It is much like a Swiss Army knife -- ​it exposes you to many aspects of data journalism, ranging from coding to point-​and-​click tools. You'll work with RStudio and SQL to analyze data. You'll scrape data from websites, social media and PDFs using code and browser-​based tools. You learn how to visualize data with tools such as Datawrapper and Flourish.

For decades, journalism has been taught as a trade, and this book helps readers learn by working with real-​world data -- ​datasets that are updated regularly by government agencies and other authoritative sources.

This book serves as the latest chapter in the ever-​evolving data journalism landscape. Our approach pays homage to the fundamentals of the past with a look to technologies of the present and the future. Moreover, it covers not just how to crunch numbers but also how to put a human "face" to data, resulting in compelling news stories based on solid analysis. It also explores how to use and build databases, create visualizations with datasets and build trust with readers through transparency, accuracy and sound research.

How important is a human element in a data story? Alvin Chang, head of data and visuals at *The Guardian US*, said each source gives him a slightly sharper view of the issue he's writing about. But he often wonders if his biases led him to talk to a self-​selecting group of people. "What if I just needed to talk to more people? What if I'm missing the larger story?

"It forces us to test the theses of our stories using the scientific method, rather than just through our individual experiences," Chang said. "Sometimes it reveals human experiences that we weren't previously aware of. And ultimately, it helps us be more curious and empathetic journalists."

On one level, data journalism is shorthand for database-​ or data-​driven journalism, where journalists find stories and create conclusions by analyzing large datasets. It is also closely associated with investigative journalism and overlaps with data visualization, as it requires close collaboration between journalists and digital and design specialists to find ways to present data through interactives, written stories, databases, videos, maps and charts.

Data-​driven journalism applies to nearly any beat or topic that journalists cover, said Andy Boyle, former director of Product Engineering at the *Chicago Sun-​Times*.

"If you have a data-​oriented frame of mind, it will help you in everything you do, not just in your journalism career, but in your life," he said. "Everything is data, and the quicker you understand that, the faster you'll be able to find stories.

"It's just another skill in your toolbox, but an important one that lifts your work to greater heights, gives it more of a scientific or academic rigor, and makes your stories potentially be even more powerful."

Heather Cherone, the politics reporter at WTTW News, the PBS station in Chicago, uses data reporting on a regular basis on her coverage of city hall and the state legislature. She says data skills are "crucial for all journalists."

"The world we live in is awash in data," she said. "Our job is to help make sense of that raw information by translating it into clear knowledge that informs the lives of our readers and viewers.

"To do that, journalists have to know how to find that data, which often takes old-​fashioned reporting. It is also important to analyze that data without fear or favor and without a desired conclusion."

::: section
## Ethics, Trust and Data

Lynn Walsh is the co-​founder and assistant director of Trusting News, which teaches journalists how to be more open and build trust with readers. Part of her job is to help data journalists learn how to be more transparent in their reporting and explain the process we cover in this book. In [Chapter 11](#ch11.xhtml_c11), we explore some of those transparency techniques with Walsh and other journalists.

Walsh, a former investigative TV news producer, said journalists often don't explain that data (or good data) on a specific topic or issue doesn't exist. This is something readers and viewers typically want to know but are rarely told.

For example, during the first few months of the COVID-​19 pandemic, journalists were criticized and accused of hiding information related to how many people were recovering from the virus. Readers and viewers were saying journalists were hiding this information because they wanted to focus on the number of infections and deaths instead of the more positive stories of recovery.

"As journalists, we are limited to what we can report on and provide data about," Walsh said.

"If the data doesn't exist, it doesn't mean we are hiding information, it means we don't have it to share. Yes, in some cases, we can create our own databases and in some cases we do, but that is not always possible or feasible and that can take a lot of resources."

Technical skills can be acquired -- ​not without effort -- ​but with time people can learn the technical side of working with data. But far less time is spent teaching and developing the skills needed to find story ideas -- ​and good story ideas are the true currency of all forms of journalism.

In reality, the federal, state and local health departments were not tracking the information, or doing a poor job of it. Explaining these limitations around data can be helpful to users. Explaining how we get data (freedom of information or public records) and the limits of the data -- ​what it does not include because it was not collected by the agency -- ​is also helpful, Walsh said.

"We should realize a lot of people do not know what FOI is or that the general public has a right to access certain information," she said. "Adding media literacy elements explaining how public records work can also be helpful to the audience.

"If we do not explain these elements of our reporting, people will make assumptions that we are purposefully trying to hide data, push a certain agenda, etc. Also, if you do create your own database and collect your own data, explain why you had to do this, as the data didn't exist, why you thought it was important to invest the time in doing this and how you did it."

::: section

## Impact of Data Journalism

Data journalism walks hand in hand with investigative reporting, which is why so many data reporting skills are taught at annual conferences such as Investigative Reporters and Editors (IRE) and the National Institute for Computer-​Assisted Reporting (NICAR). Data and public records lend credibility to investigative stories and reaffirm one of journalism's basic premises: Show, don't tell.

Just how valuable are these investigative stories? In his book, *Democracy's Detectives*, author James T. Hamilton did a cost-​and-​benefit analysis of several investigative stories. He showed that for every \$1 a media outlet spent on an investigative story, the net policy of benefits to the public was as much as \$287.

Good data-​driven stories do more than win awards. They effect change at many levels of government and society as a whole.

::: section
## History of Data Journalism

While Ida B. Wells didn't have a laptop or smartphone to do her work, she took to heart the concept of looking for patterns and then writing about it. But it wasn't until more than a half century later that newsrooms began to adopt data journalism.

In his 2021 article, "The History of Data Journalism" for *The Data Journalism Handbook* website, University of Illinois professor Brant Houston outlined the evolution of what we know today as data journalism and computer-​assisted reporting. "Many practitioners date the beginning of computer-​assisted reporting and data journalism to 1952 when the CBS network in the United States tried to use experts with a mainframe computer to predict the outcome of the presidential election," Houston wrote. "That's a bit of a stretch, or perhaps it was a false beginning because they never used the data for the story."

Houston traced the true origins of data journalism -- ​and one of its key founders -- ​to the Detroit riots in the summer of 1967. Dozens were killed and more than 1,000 people were injured in the violence, but some Detroit newspaper reporters dug deeper into the cause of the riots in the wake of what occurred.

Among those reporters was Philip Meyer, who used a social science approach to gathering data and telling the story of the riots in a new way. In doing so, Meyer pioneered what we know today as data journalism, eventually writing the book *Precision Journalism*, which has been revised several times as *New Precision Journalism*. The book is a mainstay in data journalism and social science college courses.

The evolution of desktop computers, software and the Internet opened new opportunities in the 1980s and 1990s. Spreadsheets helped reporters analyze city budgets and build large databases that could be maintained over years. New digital tools and phone apps emerged, making it easier to gather data. Drones, sensors and other technologies offered new opportunities. In the last decade, tools such as RStudio and code such as Python gave data journalists the chance to ask questions of data like never before.

Free data visualization tools like Flourish, Datawrapper, Infogr.am and many others help reporters build interactive charts and graphics with nothing more than a spreadsheet. Journalists have more ways to tell stories than ever before. Arc-​GIS, [Carto.com](http://Carto.com), MapBox, Open Street Map, Google Earth and MyMaps give readers a birds-​eye view of an issue.

Data journalism skills are essential in today's newsrooms, according to academic research. Surveys show that many professional journalists want to improve their abilities to work with data. The demand for data journalism instruction exists both in the journalism industry and others, and in the United States and abroad.

John Walton, data journalism editor at BBC News' data journalism team, said journalists need to be able to interpret data, have a solid understanding of statistics and crucially they need to be able to communicate what they have found in the data to readers who may never peek within the tiny cells of a spreadsheet. News organizations unable to deploy data journalists can't really hope to report on the modern world in all its rich complexity. It's as simple as that.

But Walton also cautioned that data journalists shouldn't focus too much on the technical side of the craft and that journalism itself should always come first. What really counts is shoe-​leather reporting, the curiosity to seek out stories, the imagination to see the opportunities for storytelling using data and the doggedness to stick with a complicated investigation, no matter where it leads.

"A journalist can be equipped with all the technical skills in the world," Walton said, "but if they don't have ideas for stories they will always be beaten to the punch by someone with a good idea for a story but only a fairly basic grasp of how to sort a spreadsheet."

In this book, you will learn not just how to crunch numbers but also how to humanize data, resulting in compelling news stories based on solid analysis.

It features training videos, tip sheets and links to resources for finding, cleaning and analyzing data. The [DataPlusJournalism.com](http://DataPlusJournalism.com) website includes additional exercises, diversity in data, changes in data journalism and software and many tips, tricks and resources. Chapter and exercise updates can also be found on the blog.


## Footnotes

- Scene on Radio, More Truth <https://www.sceneonradio.org/s4-​e11-​more-​truth/>
- Vox, What Is Data Journalism? [https://www.vox.com/2015/2/4/7975535/what-​is-​data-​journalism](https://www.vox.com/)
- Sage, Journalism & Mass Communication Educator [https://bit.ly/sagejmce](https://bit.ly/)
- American Press Institute, How to Teach Data Journalism in Journalism Schools [https://bit.ly/dataapiarticle](https://bit.ly/)
- Nieman Lab, Journalists Know They Need to Get Better with Data and Statistics, But They Have a Long Way to Go [https://bit.ly/niemanlabdata](https://bit.ly/)
- The Data Journalism Handbook, The History of Data Journalism [http://bit.ly/datajhistory](http://bit.ly/)
- Ida B. Wells Papers, University of Chicago Library [https://bit.ly/idabwellsdata](https://bit.ly/)


# 1 Acquiring Data

Mike Reilley

DOI: [10.4324/9781003273301-2](https://doi.org/10.4324/9781003273301-2){aria-label="D.O.I. link to this document."}


Pearl Zhu, author of the "Digital Master" book series, wrote that we are "moving slowly into an era where big data is the starting point, not the end." This is true, and it begs a question: Where do we really *start* with acquiring the data we need for a news story?

There are many avenues to pursue: federal, regional, and local data portals; contacting a government agency; doing original research to build a dataset and doing online searches. And once we locate the data, how can we capture it in a format that helps us tell the story?

The RTI Rating reports that freedom of information (FOI) laws, on a global scale, are relatively new. As of 2022, 134 countries have laws on the books, more than 100 of which only adopted laws in the past 22 years.

Sweden has the oldest FOI laws, dating back to a 1766 law that gives Swedes the right to gain government documents. Some dispute this, saying China was ahead of the curve several centuries earlier, but Sweden is widely considered the first.

Other countries lagged behind until the mid-​20th century, with the US, France, Japan, Israel, Colombia and 22 other countries all adopting FOI laws during the last century. Russia, Switzerland, Germany, Mexico and Argentina have followed suit, but the efficacy of those laws depends on the courts and governing bodies in those countries.

::: section
## Using FOI Laws

University of Arizona professor David Cuillier has taught public records reporting for decades, has studied public records denials and has testified before Congress on public records laws. He has trained thousands of journalists on how to obtain records and use them as concrete data in their reporting.

"Public records provide credible, substantive 'proof' for story angles that sources have a difficult time refuting," he said. "They avoid being spun by officials."

For example, when the *Miami Herald* in 2017 heard that juvenile detention there was a rough place, they knew they wouldn't get much confirmation from officials. But in obtaining surveillance video through public records laws, they showed the public actual brawls among detainees, often egged on by guards. The story, "Fight Club," was a 2018 Pulitzer Prize finalist.

Likewise, when a broadcaster heard the Boise, Idaho, mayor was using the city credit card for buying personal items, the city denied it. But after reviewing that surveillance video from a public records request, the KBCI-​TV station showed the mayor and his cronies hauling loot into his office, caught red-​handed.

"The mayor was fired and imprisoned for that and other shenanigans," Cuillier said. "That is the power of public records."

This chapter focuses on obtaining datasets through public records searches, data portals, FOI requests and how to scrape data from a web page or a PDF using a variety of tools and techniques.

\* \* \*

:::: section

## Making a Public Records Request

While the FOI's impact varies by country, all FOI laws tend to have requirements for filing, and agencies are given a specific amount of time to respond. No matter where they are working, it is the reporter's responsibility to look up the particular laws in their country, state, province, etc.

When you cannot find datasets through searches or a data portal, you must turn to government agencies to find them. While datasets are increasingly available online, many are still kept hidden deep in government offices at the federal, state and local levels, for a variety of reasons. So reporters must contact public information officers (PIOs) to request the documents.

Typically, this can be handled through a routine phone call, email or visit to the agency. But if those avenues aren't fruitful, reporters must use a Freedom of Information law to request the public document.

According to the National Archives, FOI (5 U.S.C. 552, as amended) provides any person with the statutory right to request information from executive branch agencies of the US government. This right of access is subject to nine statutory FOI exemptions, which provide agencies the authority to withhold records in whole or in part. FOIA requesters may appeal any such withholding, or other adverse decision, back to the agency and may also file a lawsuit to seek redress in federal court. Before going to court, requesters are encouraged to contact the agency's FOIA Public Liaison at any time for assistance and to utilize mediation services offered by the Office of Government Information Services (OGIS).

Journalists aren't the only ones who file FOI requests. Lawyers do, and private and public businesses, including banks, file them. So do everyday citizens who are curious about what is going on in their communities. But for journalists, FOI and other "sunshine" laws, which can vary by state and country, can greatly enhance the depth and scope of reporting. Backing up a story with public documents lends a high level of credibility to reporting.

\* \* \*


<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Pro Tip ![](images/Pro_Tip_Icon.jpg) 

When you start on a beat, go to the agency office or website that you're covering. Study the forms that the agency collects. What kinds of data are they gathering from the public? How are they organizing it, and what formats do they keep it in (Excel, Word, etc.)? Check the city, county, state or federal data portal to see if the information is readily available. Is some of it withheld? Find out why. This also serves as a road map for when you need to pull data later on. You'll already know what information is being collected.

</aside>

\* \* \*

There are many FOI form letters available with a basic Google search. You can download them as Word or Google documents and simply fill out the form and send to the agency by either email or registered US mail. But there are some free websites that help reporters not only write the letters but also track them. [iFOIA.org](http://iFOIA.org) from the Reporters Committee for Freedom of the Press is one of the best, as well as the Student Press Law Center Public Records Letter Generator**.**

Once you set up a free account on [iFOIA.org](http://iFOIA.org), you can use several pull-​down menus to select the agency and letter you want to use. When filling out the letter, be sure to be very specific about the records you want and what format you want them sent as (Excel, Word, shapefile, etc.).

Be specific about the type of record you want, what dates the records cover and what the topic is. Simply asking for "all of the mayor's email correspondence" is too broad. However, requesting the mayor's emails over the past three years discussing the public funding of a new bridge with the city's CFO is more specific and gives the agency a better road map to find the records. This typically cuts down on denials.

Listing a specific file format in the request is especially important; otherwise, the agency can send the documents as PDFs, which make it harder to extract data, though we'll explore some tools to do that later in the chapter. It's also wise to stipulate what costs you would cover for file transfer or, if need be, photocopying (sounds old school, we know). Make sure you have the name and title of the PIO and the correct mailing and email addresses on the letter.

"In many states, if a requester wants the data electronically, the agency must provide it in that format -- ​can't convert to PDFs and print out on paper," Cuillier said. "Also, in some states, such as Arizona, they are required to provide the meta-​data, if requested."

The form letters stipulate that the agency has 30 days or less to respond to the request. [iFOIA.org](http://iFOIA.org) will notify you of when those 30 days are over, which is particularly helpful if the reporter is managing dozens of requests at once.

After the 30 days, the agency may fulfill the request, deny it or ask for more information from you. If denied, immediately file an appeal letter, which is available through [iFOIA.org](http://iFOIA.org). If denied, an agency must list a specific state or federal statute backing the denial rather than citing a broad "internal policy" -- ​a popular excuse.

"Agencies are always figuring out ways to game the system," Cuillier said.

"Using privacy apps like Signal has been going on for some years. Another scam is having files hosted on private servers or with a nonprofit, and then claiming the files aren't in their possession. The most common tactics are simply ignoring requests, inflating copy fees, or making up reasons for denial. The only way to stop it is to sue the agency, and unfortunately that does not happen enough."

Government officials can be clever in hiding their work from public records law. Aides to Washington, D.C., Mayor Muriel Bowser used WhatsApp, the Facebook-​owned messaging app, to skirt public records laws in 2019. And in 2020, NCAA officials used a third-​party platform to hide discussions about COVID-​19 and the football season.

Cuillier said agencies create all kinds of reasons they can't deliver on a request. If they say the software can't export the data, then reporters should ask what company made it, contact that company and ask why their software can't export data.

"The company will say it certainly can and explain how, or link them up with the agency to help them export," he said. "I haven't encountered data yet that can't be exported."

He said some agencies will say they keep their data with a private vendor, or in a system created through a vendor, and that the whole system is proprietary, even the data dictionary, and can't be released because of an agreement.

"That is bogus," he said. "Agencies can't make agreements with companies that don't follow state public records law."

Pursuing public records will test your patience, but the payoff is worth it. Being persistent, especially after a denial, is key, Cuillier said.

"Keep at it until you get the records," he said. "Look at it as a maze, where you run into a dead-​end, but just maneuver around until you get to the cheese.

"It takes persistence, tenacity and sometimes a little psychology. Don't take officials' denials at face value -- ​check with records experts. Find out what other agencies do (peer pressure is effective at getting records). Team up with other journalism organizations. Always appeal denials (a third of the time it will kick them loose). And triangulate your records work with people sourcing -- ​they go hand-​in-​hand. Sometimes you are better off getting the records leaked to you, rather than wasting time in court."

:::: section
## Appealing a Request Denial

If an agency denies your request for public records, you should appeal the denial immediately. Many agencies will fulfill the request immediately as the appeals letter is a sign that you mean business and won't go away until you get the record.

Although it varies by country, most appeals must be submitted within 30 days of the denial. Ask the PIO to review your FOI request and denial decision. Give reasons why you think the denial was wrong, cite any federal or local laws that apply and refer to any communication you've had with the agency in the past. And be sure to include a copy of your request and denial in the appeal document.

<aside class="boxed-text2" epub:type="tip" role="doc-tip">

For more data journalism tips, tricks, exercises and an archive of data portals, visit the Data + Journalism blog at <http://dataplusjournalism.com>.

</aside>

Most agencies have 20 working days to respond to the appeal, though that time may vary by agency and country. Keep in mind that the agency might take a bit longer to decide on the appeal, and they must notify you of that delay.

Some government agencies, such as the US Department of Health and Human Services, post steps on how to appeal an FOI denial. Make sure you check with the agencies you cover for specific criteria they may have to prevent any further delays.

When denied and thwarted by a hostile agency/official, ramp up the pressure and make it harder for them to say "no" than to say "yes." That means writing stories about the denial, quoting experts, the elected officials and average people affected. Survey surrounding agencies to show that the recalcitrant agency is an outlier (peer pressure is extremely effective). Submit 10 more requests about their expense reports, disciplinary records, claims against the agency, emails about your requests and anything else that might expose wrongdoing so common in agencies run by ego-​driven, defensive and arrogant officials. During all this, keep your cool and take the high road.

Todd Wallack of WBUR in Boston has a great strategy when a government agency rejects one of his FOI requests. He immediately files an appeal letter with the agency and then files a separate FOI request requesting the internal emails from the agency officials discussing why his initial public records request was denied. Wallack says this accomplishes two things:

1.  Prompts the agency to take the initial request more seriously and disclose the documents
2.  The emails help him better understand the denial process

When you receive a denial or if your appeal is denied, there are many organizations you can turn to for help. The Society of Professional Journalists (SPJ) helps journalists all over the world in their pursuit of public records. SPJ's FOI committee plays a watchdog role on agencies and has dozens of resources to help.

The Reporters Committee for Freedom of the Press provides a variety of resources on public records and open meetings laws, also known as sunshine laws, right to know laws or FOIAs. These laws -- ​primarily focused on the US -- ​provide a legal basis for access to government records and meetings, with certain exceptions, and are used by reporters and news media organizations to inform the public on the workings of the government.

The organization has a FOIA Wiki on submitting requests, exemptions, administrative appeals and most other topics related to the federal FOIA. It also has a free iFOIA online tool to create, file and track federal, state or local public records requests. The tool not only helps you file the request letter to the proper agency but also sends you alerts for when the agency must respond and seamlessly provides appeals letters ([Figure 1.1](#ch01.xhtml_f1_1)).


RCFP's Open Government Guide is a collection of every US state's open records and open meetings laws. Each state is arranged according to a standard outline, which helps journalists compare the laws in various states on specific topics.

Like RCFP, MuckRock helps you file, track and share public records requests. The site offers great tips on filing FOI requests as well as a state-​by-​state FOI laws guide.

Another useful resource is the National Freedom of Information Coalition, a nonprofit, nonpartisan organization of state and regional affiliates representing 39 states, commonwealths, territories and districts. The organization provides transparency education and guidance, offers financial support for FOI litigation, provides a state-​by-​state resource guide and undertakes evidence-​based research projects.

<aside class="boxed-text2" epub:type="tip" role="doc-tip">

::: section
### Five Tips for Getting Public Records 

There are so many strategies in acquiring public records, but here are five from David Cuillier that work for a lot of journalists internationally:

1.  Get to know the records officers. Go to coffee or lunch with them (pay your own way) and ask what their job entails. Ask what bugs them about requesters. Ask for tips in requesting records. Ask what records they have seen that few people request and could be really interesting. If they and other record custodians see you as a real person, then they are more likely to help you and offer you further records that you might not have known about.
2.  Hone your letter with specific keywords for agencies to use in their search. More and more agencies are searching for records electronically, so if you can provide keywords that will find what you need, it will speed things up. One of the fastest-​increasing reasons for denial today is the response, "We do not have records responsive to your request." In other words, they couldn't find what you needed because they didn't have the right keywords.
3.  Invest time into finding the existence of records. It is essential to know what records agencies have to craft a specific letter. That means scouring agency websites for references to reports, records and data. It means looking at forms that agencies have people fill out (that information likely feeds into a monster database that can be requested). Look at retention lists and public record logs. Go to agencies and talk to workers about what they do all day -- ​and how they record that activity.
4.  Find an hour each week to set aside as your records time. Turn off email and the phone and spend the time submitting a public records request and following up on pending requests. This will get agencies used to you, so when you come to them with sensitive requests, they won't recoil. Also, if you get amazing records out of just half of those requests, you will have 26 kick-​butt stories produced every year, helping your news organization, your career and, most importantly, your community.

</aside>

:::: section

## Using Data Portals

Data portals have emerged over the past decade as a rich resource for finding datasets for stories. It's also a great place to find story ideas.

Many governments have data portals -- ​vast online catalogs where you can browse or search for open data on diverse subjects. The US government, for instance, has [Data.gov](http://Data.gov), an index of hundreds of thousands of datasets posted by myriad agencies.

International organizations have data libraries, too. The data portals of the United Nations, World Health Organization and World Bank include datasets on topics ranging from education and economic indicators to crime and social trends.

Our World in Data is a free, open-​source portal containing nearly 3,300 charts across 300 topics, including a deep COVID-​19 data archive. The charts are easily embeddable into a web page, and the site offers an easy data download so you can build your own charts with the datasets.

The portal features datasets on the environment, the economy, census/population, industry and employment and public health, among other topics. It also includes a newsletter digest that updates when new datasets are added to the site ([Figure 1.2](#ch01.xhtml_f1_2)).


Journalists in Europe often tap into Eurostat, the statistical office of the European Union (EU). The site produces European statistics in partnership with National Statistical Institutes and other national authorities in the EU member states and includes the statistical authorities of the European Economic Area (EEA) countries and Switzerland.

The Open Knowledge Foundation has assembled a list of about 600 data portals around the world. It may take some searching, but you can find relevant datasets by entering keywords and sorting the results by date.

Many government agencies and municipalities store thousands of routine datasets online and accessible to the public. These relieve PIOs from having to chase down data requests from reporters, lawyers and anyone else requesting the documents.

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Read More: Glossary ![](images/Read_More_Icon.jpg) 

Journalists love to use jargon when working with data. Even the most basic terms can get confusing when not explained clearly.

In this book, we often refer to the word "import," which equates to "upload." We're importing or uploading the files to the web.

The term "export" equates to "download." We're exporting/downloading the data from the portal.

We'll define more terms throughout the book.

</aside>

Portals give journalists the chance to inspect datasets and download them by simply hitting a button. Many contain routine data -- ​city repairs, county or regional health data, national crime data, etc. They also include shapefiles that include states, provinces, bus and train lines, political districts, wards and districts. These shapefiles are critical for building maps.

Reporters covering local and regional news download datasets from city, county and state data portals. For example, the City of Chicago data portal contains city budget data, crime statistics over the past two decades, restaurant inspections, public transportation ridership data and many other data that are useful for reporters looking for public-​records driven stories.

Data portals are relatively easy to find. Newsrooms often compile lists of them on shared documents, and there are many search tools beyond a basic Google search -- ​for example, "Dublin Ireland data portal" -- ​that can help you find what you're looking for.

If a Google search produces no results, the US Data Portal Github page provides links to dozens of state, county and city portals in one page. [DataPortals.org](http://DataPortals.org) has a searchable map of nearly 600 data portals from around the world. Better Data Portal offers search across Socrata data portals, and Statista provides clean datasets from all over the world for a fee.

\* \* \*

::: section
## Basic Search

Working from their Stanford dorm rooms in the mid-​1990s, graduate students Larry Page and Sergey Brin built a search engine that used links to determine the importance of individual pages on the World Wide Web. They called this search engine Backrub.

Thankfully, that search engine evolved by 1998 and was renamed to Google, the go-​to search engine we use in everyday life. But the search engine also has many tools and features that help data journalists quickly locate datasets.

::: section

## Google's Powerful (but Hidden) Advanced Search Tool

It can be hard to find, but Google has an advanced search interface that lets you specify even more exactly what you're looking for: Words or phrases to include or exclude from the results, number ranges, the domain or site and other criteria.

You can find this tool by clicking on "Settings" in the lower right corner of Google's main search page. With the advanced interface, you might search for documents that have been posted on federal government websites in the past year about student debt, loans and tuition at colleges and universities around the world, etc. Simply use the various fields to isolate your search.

\* \* \*

::::: section
## Google Search Operators

Dan Russell, a senior research scientist at Google, has compiled a list of dozens of search operators to help you find the information you want. Russell also offers a free course on Power Searching with Google.

::: section
### Filetype

This operator helps you search the web for a specific type of file: .xlsx, .ppt, .pdf. Type this into a Google search field and see the results:

1.  Filetype:xlsx Sydney Australia positive COVID-​19 cases

The Sydney and New South Wales government health data pages typically show up on the first page of search results, along with a page of Sydney COVID-​19 data from Our World in Data.

::: section
### Site

Search within a specific website for information on sublevel pages. This is particularly helpful with government websites -- ​and some media websites -- ​that have poor search engines built in. Use Google to work around it by typing this into the Google search field:

1.  Site:[cdc.gov](http://cdc.gov) SARS

The result is a deep list of SARS-​related pages useful to journalists: About page, fact sheet, FAQ, historical timeline, etc. ([Figure 1.3](#ch01.xhtml_f1_3)).


There are many other useful search operators that Russell recommends:

1.  **Site minus site.** A search like \[ site:[nyc.gov](http://nyc.gov) -​site:[www.nyc.gov](http://www.nyc.gov) \] will give you sites in [NYC.gov](http://NYC.gov) that do NOT begin with WWW. That's handy for finding subdomains within a particular site, which you can then use **site:** to search.
2.  **Stars in site search**. A search like \[ site:\*.law.\*.edu \] will find all of the EDU sites with ".law" in the domain name. Also try: \[ site:\*.[nyc.gov](http://nyc.gov) \] to match all of the [NYC.gov](http://NYC.gov) sites with a subdomain. Also: \[ site:\*.nasa.\* inurl:education \] gives lots of good clues about education sites at NASA.

\* \* \*

:::: section

## Google's Dataset Search Engine

In 2018, Google launched its Dataset Search, a database of millions of datasets posted by academic researchers, nonprofit organizations, companies and government agencies ([Figure 1.4](#ch01.xhtml_f1_4)). To have a dataset appear in the database, developers must format the data and provide detailed information about the dataset to Google's satisfaction.


Google's reasoning: Datasets are easier to find when they include clear and consistent supporting information, such as the data's description, source and file format. Those details can help journalists determine whether a dataset is worth downloading, thus saving hours of research time.

As you type keywords into the Dataset Search box, Google suggests possible datasets. Moreover, you can filter the research results by when the data was posted, its format and whether you must pay to download the data. Just use the filters tab at the top of the interface.

The tabs down the left side of the interface allow you to move to various datasets. As you click each tab, the description of the dataset -- ​provided by the data's producers -- ​appears on the right side of the interface. This includes the format, any special permissions (most are public records or available under Creative Commons licenses) and details of the dataset methodology.

It's important to note that Google doesn't fact-​check the datasets. It merely guides you to the datasets and provides information about them so you can vet the data yourself. It's an incredibly efficient tool for finding clean datasets on deadline.

Journalists also can have their datasets listed in the search engine by completing the steps outlined on the tool's developer page.

\* \* \*

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise ![](images/Exercise_Icon.jpg) 

1.  Go to [Google.com](http://Google.com) and type in "US mass shootings data," and see what appears on the first screen. Are you getting datasets in your results? Try it with other countries. You likely will get news stories and blog posts, not datasets.
2.  Now type this search operator text into [Google.com](http://Google.com): "filetype:xlsx US mass shootings". You should get a more robust search result featuring datasets from Kaggle and Stanford Libraries.
3.  Now go to the Google Dataset Search tool, and type in US mass shootings. Use the toolbar down the left side to view the different datasets. Details of each dataset are featured on the right. Your first result is typically the best result, even better than using the search operator in step 2.

**Video**: How to use Google Dataset Search

[https://www.youtube.com/watch?v=dxMretoIA3Q](https://www.youtube.com/)

</aside>

::: section
## Other Search Options

While Google is a valuable search tool for data journalists, there are other useful tools for searching the Internet for datasets, including:

- Bing, Microsoft's search engine
- Yahoo!
- Some journalists prefer DuckDuckGo or Startpage because they vow to protect your privacy by not tracking your search history. In China, which has banned Google, the most popular search engine is Baidu; in Russia, it's Yandex.

::: section

## Academic Studies and Expert Sources

With any data story, it's important to seek outside experts who can help you understand your subject. Find them early in your reporting process as they can help guide you to good datasets and assist in the cleaning process.

Remember, someone somewhere studies the subject you're writing about. Ask them basic questions, and get their input through every step of the process. Academics have developed standard methodologies to study all kinds of things. You don't need to reinvent them. You'll end up with a better analysis and a measure of credibility you could never achieve on your own.

Research by scholars with deep expertise also can make your news stories more authoritative. But peer-​reviewed journal articles may be too long and dense for reporters on tight deadlines. The Shorenstein Center on Media, Politics and Public Policy at the Harvard Kennedy School created Journalist's Resource, which curates and summarizes academic research relevant to newsworthy issues.

The website's database contains thousands of summaries of academic and governmental research on topics from economics and the environment to politics and social issues. The summaries translate jargon and abstruse statistics into everyday language. Journalist's Resource also includes tip sheets for reporters, including data journalism.

In addition, two specialty search engines -- ​Google Scholar and Microsoft Academic -- ​can help you find scholarly research. Scholar lets you search academic journals and case law and filter it by publication year, etc. Thousands of academic journal articles are listed there, and many of their authors have contact pages that show a list of all of their publications.

Each page has a "follow" button that alerts you when the academic publishes or edits an article. This is particularly helpful when writing about an ongoing issue and you want to keep up with the academic's work.

Google Scholar also is good for finding expert sources. Simply click on the author's name if hotlinked to go to his or her bio page ([Figure 1.5](#ch01.xhtml_f1_5)). There, you'll find past publications, areas of expertise and more. Hitting the blue Follow button next to the bio subscribes you to that author so you receive an email when the author publishes.


The authors typically have a link to a homepage or contact information, so reporters can reach out to them directly. If there's no link, simply Google the author's name and find the contact page.

You also can look for knowledgeable sources in online databases such as ExpertiseFinder and [DiverseSources.org](http://DiverseSources.org), which feature underrepresented voices about science, health and the environment. National Public Radio features a database of diverse expert sources organized by state, and Sources of Color assists both journalists and public relations (PR) pros with finding and pitching diverse experts.

The Journalist's Toolbox has an entire page devoted to expert source databases, including a deep archive of diverse experts.

Cision, the company that operates PR Newswire, has two services to connect experts with journalists:

- Help a Reporter Out -- ​Journalists can send their story idea to HARO, and Cision will forward it to a network of media relations practitioners at universities, think tanks and other institutions. The PR staff then look for in-​house experts who might contact the reporter.
- ProfNet -- ​With ProfNet, journalists not only can pitch their stories to prospective sources but also sign up for email alerts about experts available to discuss timely topics in the news.

::: section
## Hacking a Web Address to Find Archived Data

Many times, government agencies don't maintain an easy-​to-​navigate archive of their records on the web, providing only the most current dataset. To find older datasets, you can hack the web address of the most recent dataset as agencies have consistent URLs for naming files.

For instance, the US Postal Service publishes its quarterly performance report on its website. The data table shows the percentage of mail delivered on time in each postal district. Here is the page of quarter 3 data from 2020 ([Figure 1.6](#ch01.xhtml_f1_6)).


Here is the website address for that table. Note that we boldfaced the fiscal year and quarter:

[https://about.usps.com/what/performance/service-​performance/fy2020-​q3-​single-​piece-​first-​class-​mail-​quarterly-​performance.html](https://about.usps.com/)

To find quarter 4 data, simply change the q3 in the URL to q4:

[https://about.usps.com/what/performance/service-​performance/fy2020-​q4-​single-​piece-​first-​class-​mail-​quarterly-​performance.html](https://about.usps.com/)

You also can change the year and the quarter to find more pages:

[https://about.usps.com/what/performance/service-​performance/fy2021-​q1-​single-​piece-​first-​class-​mail-​quarterly-​performance.html](https://about.usps.com/)

This can be an effective way to sort through government sites and other poorly navigated websites to find data buried deep in the archives.

::: section

## Evaluating the Information You Find Online

The rise in the volume and speed of data production might be overwhelming for some journalists, especially when they don't typically use large datasets for research and storytelling. But the urgency and eagerness to make use of data, and the technology available to process it, should not distract us from our underlying quest for accuracy.

Testing and verifying data is one of the most challenging parts of data reporting. It's also one of the most important, so don't rush the process. Build time into your reporting process to check and recheck your data.

1.  One verification method is to compare datasets from different sources. For example, compare the homicide statistics compiled by local police with that of state police, logs kept by media outlets, etc. What doesn't add up? What slips through the cracks in one dataset may appear in another.

2.  It's also important to check with the PIO or data experts in a government office or organization about what criteria are used in building the dataset. Data experts in the open records office are particularly helpful, because they work with the data all the time and compile reports for journalists who request the data. Ask them to explain what the fields mean.

    Some data developers post these criteria in a Github page or in their Google Dataset Search post. You can compare these criteria among various datasets. For instance, some organizations classify a mass shooting as having three or more victims. Others use 10 or more. Some 13 or more. Those criteria greatly adjust the number of mass shootings in the database. It's important to explain those criteria to the reader and how it compares to other datasets.

    Remember, data can be bad for lots of reasons. Sometimes, the records are wrong or incomplete. Other times, the actual methods for collecting the data produce inaccuracies. If the data are wrong, so is the story.

3.  If your data is in a spreadsheet, do a quick sort and filter on the data, skills you will learn in [Chapters 5](#ch05.xhtml_c5) and [6](#ch06.xhtml_c6) of this book. Sorting and filtering will expose any data missing from the sheet. Contact the PIO or source of the data to fill in the gaps.

4.  Verify all conversions -- ​Celsius/Fahrenheit, miles/kilometers, milligrams/micrograms, etc. Check your units. Don't confuse parts per million and parts per billion. Make sure your verbal descriptions are correct.

5.  Keep a data diary that will help track of how you're analyzing your data. Keep a log of any changes or corrections you're making. List where you got the data, when, the software and steps you took to get it, clean it and analyze it. List it as a process. It's helpful in finding mistakes or replicating the process for future stories. A simple Google Doc will suffice.

6.  Verify your data with actual, on-​the-​ground reporting. Does your data describe a place? Go there. Does it describe a person? Talk to them.

\* \* \*

::: section
## Tools and Resources from This Chapter

RTI Rating [rating.org/](http://rating.org/)

FOIA Wiki [https://foia.wiki/wiki/Main_Page](https://foia.wiki/)

[iFOIA.org](http://iFOIA.org) <https://www.ifoia.org/>

Student Press Law Center Public Records Letter Generator [https://splc.org/lettergenerator/](https://splc.org/)

MuckRock <https://www.muckrock.com/>

Better Data Portal <http://www.betterdataportal.com/>

[Data.gov](http://Data.gov) <https://www.data.gov/>

United Nations Data <https://data.un.org/>

World Health Organization [https://www.who.int/data/gho](https://www.who.int/)

World Bank <https://data.worldbank.org/>

Statista <https://www.statista.com/>

Our World in Data <https://ourworldindata.org/>

Eurostat [https://ec.europa.eu/eurostat](https://ec.europa.eu/)

Open Knowledge Foundation: [DataPortals.org](http://DataPortals.org) <http://dataportals.org/>

Google Advanced Search [https://www.google.com/advanced_search](https://www.google.com/)

Power Searching with Google [https://coursebuilder.withgoogle.com/sample/course?use_last_location=true](https://coursebuilder.withgoogle.com/)

Google Dataset Search <https://datasetsearch.research.google.com/>

Video: How to Use Google Dataset Search [https://www.youtube.com/watch?v=dxMretoIA3Q](https://www.youtube.com/)

Google Dataset Search Developers Page [https://developers.google.com/search/docs/advanced/structured-​data/dataset](https://developers.google.com/)

Yahoo! <https://www.yahoo.com/>

DuckDuckGo <https://duckduckgo.com/>

StartPage <https://www.startpage.com/>

Baidu <http://www.baidu.com/>

Yandex <https://yandex.ru/>

Bing <https://www.bing.com/>

Expertise Finder <https://expertisefinder.com/>

[DiverseSources.org](http://DiverseSources.org) <https://diversesources.org/>

NPR Sources [https://training.npr.org/sources/](https://training.npr.org/)

Sources of Color <https://sourcesofcolor.com/>

Journalist's Toolbox Expert Sources [https://www.journaliststoolbox.org/category/expert-​sources/](https://www.journaliststoolbox.org/)

Help a Reporter Out (HARO) <https://www.helpareporter.com/>

ProfNet [https://profnet.prnewswire.com/ProfNetHome/Profnet-​Journalists.aspx](https://profnet.prnewswire.com/)

US Postal Service Quarterly Performance Report [https://about.usps.com/what/performance/service-​performance/fy2020-​q3-​single-​piece-​first-​class-​mail-​quarterly-​performance.html](https://about.usps.com/)

\* \* \*

::: section

## Public Records and Search Tools

Beyond what we've covered in this chapter, here are some more helpful tools for finding data and public records.

Google search operators [https://support.google.com/websearch/answer/2466433?hl=en](https://support.google.com/)

FEC Itemizer from ProPublica [https://projects.propublica.org/itemizer/](https://projects.propublica.org/)

Itemizer allows you to browse electronic campaign finance filings from the Federal Election Commission to see individual contributions and expenditures reported by committees raising money for federal elections. As of October 2018, these filings include Senate candidate or Senate party committees, which previously filed their reports on paper.

The FOIA Machine <https://www.foiamachine.org/>

Automate your FOIA requests.

Amazon's IRS Form 990 Filings [https://registry.opendata.aws/irs990/](https://registry.opendata.aws/)

Machine-​readable data from certain electronic 990 forms filed with the IRS from 2011 to present are available for anyone to use via Amazon S3.

Government Attic <https://governmentattic.org/>

Provides electronic copies of thousands of interesting federal government documents obtained under the Freedom of Information Act.

Journalist's Toolbox search tools page [https://www.journaliststoolbox.org/category/search-​engines/](https://www.journaliststoolbox.org/)

Journalist's Toolbox public records and FOIA pages [https://www.journaliststoolbox.org/category/public-​records/](https://www.journaliststoolbox.org/)

Social Searcher <https://www.social-searcher.com/>

Collates postings on social media networks.

\* \* \*

## Footnotes

- [FreedomInfo.org](http://FreedomInfo.org) [http://www.freedominfo.org/about-us/](http://www.freedominfo.org/)
- Statista, Where Do Freedom of Information Laws Exist [https://www.statista.com/chart/17879/global-freedom-of-information-laws/](https://www.statista.com/)
- National Freedom of Information Coalition, National Freedom of Information Laws [https://www.nfoic.org/international-foi-laws/](https://www.nfoic.org/)
- Miami Herald, Fight Club [https://www.miamiherald.com/news/local/community/miami-dade/article209052374.html](https://www.miamiherald.com/)
- HHS.gov, How to File a FOIA Appeal [https://www.hhs.gov/foia/faqs/how-do-i-appeal-a-denial/index.html](https://www.hhs.gov/)
- NPR, DC Officials Use WhatsApp [https://www.npr.org/local/305/2019/10/09/768529012/d-c-officials-using-whats-app-for-city-business-may-skirt-open-records-laws?t=1570705980449](https://www.npr.org/)
- The Journalist's Resource <https://journalistsresource.org/>
- The Journalist's Resource: Know Your Research [https://journalistsresource.org/type/know-your-research/](https://journalistsresource.org/) An archive of tip sheets for journalists, including data journalism.


# 2 Searching the Deep Web

Samantha Sunne

DOI: [10.4324/9781003273301-3](https://doi.org/10.4324/9781003273301-3){aria-label="D.O.I. link to this document."}

Searching the web is an inveterate skill among reporters, but online information goes much deeper than what appears in a Google search. Being a data reporter means digging beyond a basic search and into the many databases and repositories of information available on the deep web.

The "deep web" is a term for all of the data that is not indexed by search engines -- ​that is, not considered by Google and others as a potential search result. It includes things like Facebook profiles, records in a searchable database or the time and date of a YouTube video. It is not the "dark web," which is a highly anonymized, hard-​to-​reach part of the web that is not accessible through regular web browsers.

As surprising as it may seem, the "deep web" makes up most of the content on the web. This chapter will share examples of these kinds of "deep web" data sources and how to find similar ones for your stories.

But the best way to find data is the same as finding any other type of source: shoe-​leather reporting. Often, your search for data will begin with an online query, but it won't stop there.

Journalism vets often recommend calling up sources or stakeholders -- ​like the chief of police, the state auditor's office or an industry rep -- ​and ask them about what data is collected and where. Better yet, stage a broad conversation where you can ask about data as well as other sources like documents, other human sources and topics to look into. Building a stable of sources, and establishing rapport with them, is as important in data reporting as it is in any other part of journalism.

This traditional form of reporting has the added benefit of being able to check your data, your theories and your findings. You can use expert sources, government officials, public relations representatives and other stakeholders to confirm your findings, get their opinion on them or at least get a feel for whether they sound reasonable. We'll talk about this more in [Chapter 4](#ch04.xhtml_c4), Cleaning Data.

In addition, databases, despite having "data" in the name, are often in a format that is not ready to be downloaded or analyzed. Usually, there are web pages, PDF documents, search bars and other doorways that create additional steps for the data reporter. Future chapters will address how to obtain and prepare this data for analysis, but for now, we will focus on how to locate them.

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section

## Pro Tip ![](images/Pro_Tip_Icon.jpg) 

When searching an online database, you can sometimes get it to return *all* of the records by leaving the search bar blank. You can also try entering wildcards like "\*" and "%%". These tricks don't work with every database, but they are always worth trying.

</aside>

::: section
## Government Databases

A big part of the "deep web" is databases, which are often searchable from within a web page. The databases themselves may pop up in an online search, but the records they contain won't.

For example, the International Monetary Fund (IMF), a financial institution joined by almost every country in the world, has an online data portal including the organization's widely used World Economic Factbook.

The Factbook includes downloadable Excel files with economic data on dozens of countries, such as Canada's gross domestic product growth in 2019 (1.9 percent) or Kazakhstan's unemployment rate in 2020 (4.9 percent).

The Factbook itself may come up in a search engine, but the data points won't, because they are inside an Excel file hosted on that page. These data points are part of the so-​called deep web.

Government open data portals, like [Data.gov](http://Data.gov) from the US, were discussed in [Chapter 1](#ch01.xhtml_c1) ([Figure 2.1](#ch02.xhtml_f2_1)). Other useful databases include court records, campaign finance disclosures, crime maps, patents, health inspections, city budgets and many, many more. For a particular story or beat, it's most effective to ask human sources for ideas on where to find data.


::::::: section

## How to Determine If a Government Source Is Reliable

In the data journalism field, government databases are considered more reliable than other sources because they are subject to laws like public information and anti-​corruption rules. This means the government has more incentive to publish accurate and comprehensive information. But it doesn't mean a database is reliable just because it came from a government.

In 2013, a team of Russian journalists made a discovery that later would have an enormous impact on elections around the world. A group of online provocateurs were working together to sow discord in online groups around Russian (and later, American) elections. The group, it turned out, was being partly funded by the Russian government, which the journalists discovered through the government's data on financial contracts.

Another unreliable government database, though for different reasons, is the Federal Bureau of Investigation's (FBI) national dataset on crimes in the US.

Because the FBI collects this information from individual cities, police departments and sheriff's offices, any error that is in their collection will be carried over to the national data. It faces the additional pitfall of errors being introduced in transfer, data being categorized differently or not being submitted at all.

The report "provides a wealth of information about crimes, but it is only as good as the agencies that report data," reporter Mark Fazlollah wrote in a guide for Investigative Reporters and Editors.

The FBI and the Russian data portal are examples of government databases that can be tricky but insightful sources nonetheless. In general, you should evaluate a dataset's reliability by fact-​checking and cross-​checking it with other sources. These can be human, like an expert source, or nonhuman, like another dataset. When you have created your findings, always do bulletproofing, which we will address in [Chapter 4](#ch04.xhtml_c4).

<aside class="boxed-text2" epub:type="tip" role="doc-tip">

::: section
### Proxy Sources 

If you can't find a proper dataset for your story, you can sometimes use something called a proxy source. This is data that is similar or is expected to correlate with the data you are looking for.

For example, Google Trends shows trends in Google searches. These can show, for instance, that searches for a political candidate rose dramatically after a debate. This does not mean that the political candidate became more popular, or even technically, more discussed, but it does show that they were more googled.

It can be useful to use proxy data in a story, but you should be clear what the data is actually representing. You may also want to note in your story that actual data was not available.

</aside>
<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 1 ![](images/Exercise_Icon.jpg) 

Let's explore crime data with the FBI Crime Data Explorer: <https://crime-data-explorer.app.cloud.gov/>

1.  Open the Crime Data Explorer page and navigate to the Crime Data Explorer.
2.  Using the Location dropdown, filter for your state. If you are not in the US, choose a state you are interested in.
3.  In the Agency Select box, start typing the name of your city, university or a law enforcement agency you are interested in.
4.  In Year Select, choose 2020.
5.  Scroll down to look at the crime trends by state and agency. You can see data on the total numbers of crimes as well as subcategories.
6.  Try to verify this data by finding the same information from the law enforcement agency itself. You can do this by looking at the agency's website, calling their public information officer or filing a public records request for the data.

The agency's data may or may not match what is in the FBI data. When in doubt, it is always best to get data from the original source, in this case, your local law enforcement agency.

</aside>
<aside class="boxed-texte" epub:type="tip" role="doc-tip">

:::: section
### Examples 

These are a few examples of "deep web" data sources around the world. As a data journalist, you will probably need to find more localized datasets, which you can find through interviews and Internet searches of your own.

+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ***Data Portals***                          |                                                                                                                                                                                          |
+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Data.gov](http://Data.gov)                 | The US's federal open data portal is a hub for agencies and departments from different levels of government.                                                                             |
+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [data.go.jp](http://data.go.jp)             | Many countries and states have their own open data portals. This one, from Japan, collects data from government agencies as well as some nongovernmental groups. |
+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| UNdata                                      | The United Nations' data hub can be filtered down by topic and country.                                                                                                                  |
+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ***Court Documents***                       |                                                                                                                                                                                          |
+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PACER                                       | PACER is the US government's portal for federal court records. The federal court is different from city, state, appellate and other court systems.                                       |
+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| International Court of Justice              | The United Nations tries war crimes in this international court, with records dating back to 1946.                                                                                       |
+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| EUR-Lex                                     | The Court of Justice of the European Union enforces laws established by the European Union and publishes court records dating back to the 1970s.                                         |
+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ***Legislation***                           |                                                                                                                                                                                          |
+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| United Nations Treaty Series                | This is a non-comprehensive collection of international treaties collected by the United Nations.                                                                                        |
+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Library of Congress                         | Federal US legislation is tracked by this library, including bill sponsors and amendments.                                                                                               |
+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ***Financial Disclosures***                                                                                                                                                                                                            |
+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| US Federal Election Commission (FEC)        | The FEC is the body responsible for tracking campaign finance disclosures for federal political campaigns in the US.                                                                     |
+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| US Securities and Exchange Commission (SEC) | The SEC tracks financial information filed by companies that are being traded on the stock market, including their revenue and value.                                                    |
+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| IMF Data                                    | The International Monetary Fund's portal includes international economic sources like the Direction of Trade Statistics.                                                                 |
+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

</aside>

::: section
## Nongovernmental Databases

Sometimes, the best place to find data is from a nongovernmental party like an industry group, nonprofit or advocacy organization. This is typically because no government decided to collect the data or make it public. An example is the Berkeley Earth Surface Temperatures dataset, which contains hundreds of years of land and ocean temperature data. No governmental group has collected or published such a comprehensive inventory of historical temperatures, which is influential in climate change research.

These third parties can be think tanks, tech companies, academic departments, news outlets and more. However, each of these sources may have their own agenda, which should be taken into account both in writing your story and in assessing the data.

In many cases, you should be more skeptical of third-party sources than of government sources. Government releases are usually subject to mandated reporting, such as freedom of information (FOI) legislation, that enforce accurate and publicly available information. With a few exceptions, private groups don't face the same rules.

Nevertheless, these groups may be the best -- or only -- places to find data for your story. And in some cases, they are more accurate or comprehensive than the government that monitors the issue.

:::::: section

## How to Determine If a Nongovernmental Source Is Reliable

The Berkeley dataset is one of many climate change-​related datasets available online. The Independent Petroleum Association of America, an industry group of American oil and gas companies, publishes the *United States Petroleum Statistics* ([Figure 2.2](#ch02.xhtml_f2_2)). The World Resource Institute, which aims to reduce worldwide carbon emissions, maintains a website called ClimateWatch.


Both of these groups have implicit biases, on either side of the climate crisis. This doesn't necessarily mean that they are being false or misleading, but it could affect which data they collect and how they present it.

So how can we determine which sources to use and how trustworthy the information is? The answer is the same as any other journalism source: due diligence and backgrounding. One way to do this is to read the group's About page. Sometimes you can find their funders, tax forms, donors or other background information.

For example, the Berkeley Earth Surface Temperatures is published by Berkeley Earth, a nonprofit that claims to provide neutral, fact-​checked data on climate change. It shares its mission, funders and source data on the group's website, which all serve as indicators of trustworthiness. It has also been cited as a source by the European Environment Agency and the *New York Times*, meaning those outlets most likely did their own research and found the group to be credible.

It's also smart to search the group online, including in news sources. You can even post on a journalism forum with questions. Always look at your sources through a skeptical journalistic lens.

When in doubt, it's best to share this potential bias with your audience. This can be a simple statement like, "ClimateWatch, which advocates for a reduction in carbon emissions, collected this data from private companies." This clarifies your source and allows your audience to make their own decisions about how credible it is.

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 2 ![](images/Exercise_Icon.jpg) 

1.  Open the *United States Petroleum Statistics* (shortlink: [https://bit.ly/petroleumstatistics](https://bit.ly/)), a report containing data on oil rigs from 2017.
2.  First, look at the data format and its source. Its first page indicates it was published by the Independent Petroleum Association of America, and the end of the URL indicates it is a PDF.
3.  On the report, look at Table 1, "Exploration Activity." You may be able to copy and paste this table into a spreadsheet program, but it is easier with a tool like Tabula. We will address how to scrape data out of PDFs in the next chapter.
4.  Describe two to three other sources where you could potentially get this data. Think: What government agency would track oil rigs? Would it be federal or state? Are there any advocacy groups or nonprofits that would do this as well?

When using nongovernmental data sources, it's often important to ask yourself whether it is the best (or only) place to find and use the data you are looking for. In [Chapter 3](#ch03.xhtml_c3), we will learn how to actually extract and use this report data in a technical sense.

</aside>
<aside class="boxed-texte" epub:type="tip" role="doc-tip">

:::: section
### Examples 

+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ***Less Neutral Sources***                                                                                                                                                                                                                                         |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Political Organizations    | Lobbying groups sometimes publish their own resources. Examples include the National Rifle Association's (NRA) database of State Gun Laws and the International Labour Organization's ILOSTAT hub.                                    |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Advocacy Groups            | Advocacy groups are organizations that explicitly support a cause. Some create resources such as ClimateWatch by the World Resources Institute.                                                                                       |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Stakeholders               | A stakeholder is any person or institution directly involved in, or affected by, the issue at hand. A list of World Cup competitors is maintained by FIFA, which is the organizing committee and therefore an active stakeholder.     |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Industry Groups            | Companies or private groups sometimes form to track information pertaining to a certain industry, such as the National Retail Foundation's State of Retail.                                                                           |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Think Tanks                | Think tanks are organizations that produce research and recommendations on a certain topic. Some advocate for one point of view, like the Heritage Foundation, and others claim to be nonpartisan, such as the Brookings Institution. |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Professional Associations  | A professional association is a group that offers membership within a certain industry. This includes the American Bar Association (ABA), which offers an enormous amount of legal research on its website.                           |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ***More Neutral Sources***                                                                                                                                                                                                                                         |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| News Organizations         | News outlets sometimes publish and maintain their own databases, such as ICIJ's Offshore Leaks and ProPublica's Dollars for Docs.                                                                                                     |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Universities               | Many universities around the world track and publish data, like the UK Data Archive from the University of Essex.                                                                                                                     |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Academic Papers            | Scholarly papers can be an excellent source of data, as long as they are not funded by a stakeholder. One example is "Assessing the Performance of Freedom of Information" by the Columbia Law School.                                |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Scientific Papers          | Peer-​reviewed papers also tend to be trustworthy sources, as long as they are not funded by stakeholders. An example is "Global Trends in Lifespan Inequality" by the Centre d'Estudis Demogràfics.                                   |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Transparency Organizations | Some groups simply advocate for transparency overall. These include Charity Navigator, the Sunlight Foundation and OpenCorporates.                                                                                                    |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

</aside>

::::::: section
## Social Media

In addition to data collected by public and private entities, you can find a lot of data on people, companies, news topics and more from social media.

A good tool to have in your toolbox, no matter which platform you are using, is the syntax for advanced searches. "Syntax" is a word meaning the set of words and phrases you can use in a certain language.

[Chapter 1](#ch01.xhtml_c1) covered some of this syntax in Google. We learned how to search within websites with Google's "site:" filter, find files with "filetype:", exclude results with the minus sign (−) and find near-​results with the asterisk (\*) wildcard. These search operators are also available on other search engines and within social media sites themselves.

Many of these sites have advanced search pages, where you can click and type your search terms. But, in general, it's better to learn the syntax so that you can write your own queries. For example, on Twitter, searching "@WhiteHouse" returns any tweet that tags the White House account, but "from:WhiteHouse" returns only posts tweeted *by* that account.

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 3 

Here, we will find a news-​relevant tweet with Twitter's advanced search syntax. The site has its own Advanced Search page, but it is only available to users logged in to their Twitter accounts.

1.  In a web browser, type in "[twitter.com/whitehouse](http://twitter.com/)". You do not need to have a Twitter account.
2.  In the search bar, type "from:whitehouse 'build back better act' since:2020--​01-​01".
3.  Click on "Latest" in the toolbar, below the search bar, to sort the tweets in chronological order.

This search takes advantage of three advanced search operators ([Figure 2.3](#ch02.xhtml_f2_3)). "From:" limits the results to only tweets posted by the US White House's official Twitter account. The quotes around the phrase "build back better act" limit the tweets to ones mentioning this exact phrase, as opposed to individual mentions of "build" or "act." And the date filter, "since:", limits the tweets to ones posted after the date in the search.


Twitter offers a full list of search operators on its support site.

</aside>

Because platforms and search engines often use different search operators, sometimes it is easier or more effective to do a search on Google instead. To do this, you will need to understand URLs and how they work. We will discuss URLs more in [Chapter 3](#ch03.xhtml_c3), Scraping Data.

Let's look at the URL of this Reddit post:

[https://www.reddit.com/r/news/comments/ru92dd/tornadoes_from_rare_supercell_caused_damage_in/](https://www.reddit.com/)

<aside class="boxed-text2" epub:type="tip" role="doc-tip">

::: section
### Post IDs 

In social media, posts, users, pages, locations and other criteria are often given IDs. For example, you can find the ID of your Facebook account by navigating to your profile and looking at the URL. It should look something like this:

"[https://www.facebook.com/profile.php?**id=1156612157**](https://www.facebook.com/)"

Once you know the ID, you can use it in tasks like scraping and backgrounding.

</aside>

The URL contains several different usable parts: "[reddit.com](http://reddit.com)", which is the website; "/r/news/", which is the "news" subreddit, a subsection of the site; "/comments/", indicating the content is a post; "ru92dd", a unique ID for the post; and the beginning of the post title.

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 4 

1.  In Google, type the following search: "site:[reddit.com/r/newsinurl:/comments/Coronavirus vaccine](http://reddit.com/)". This should return a list of Google results that are all r/news posts about COVID vaccines.
2.  In your search, change "vaccine" to "conspiracy." How does this change your results?
3.  Try adding quotes ("") around "Coronavirus vaccine". This should limit your results to that exact phrase.

By looking at how Reddit constructs its URLs, we were able to use Google's advanced search to find posts from a subreddit that mention a certain phrase. If a social media site's search feature doesn't help you do what you want to do, you can often use this workaround.

</aside>
<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
#### Pro Tip 

You can create a Google Alert for these searches and save them to your Google account. This way, when a new result for your search is indexed by Google, you will receive an email in your inbox.

Google Alerts are not instantaneous -- ​they typically update once a day -- ​but they can be a good way to monitor for tweets or new posts if you can't do that within the social media site itself.

</aside>

::::::: section

## How to Determine If a Social Media Source Is Reliable

Social media companies are not typically required to disclose their data. For example, Discord may make an announcement of how many users it has, but it is not legally required to.

One exception is "public" companies -- ​meaning those that are being traded on the stock market. In the US, when a company "goes public," it starts being regulated by the SEC, meaning it has to disclose certain information every year. Other countries have similar laws and regulations, so it may be helpful to look up what local requirements are, similar to researching FOI laws.

Because it is legally required, and a company can be fined for incorrect or misleading information, the reports are often considered a more reliable source than numbers published on a web page. There have, of course, been instances of companies lying in legally mandated reports, but the consequences are much higher.

On the other hand, getting data from a press release or announcement can be much easier and doesn't necessarily need to be disbelieved. As a journalist, it's always smart to state your source and sometimes even explain why one is more trustworthy than another.

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Pro Tip 

When googling, you can use the site filter with only the domain, in order to get any website on that domain. For example, "site:.gov" will return only government websites, while "site:.edu" will return educational institutions.

</aside>
<aside class="boxed-texte" epub:type="tip" role="doc-tip">

:::: section
### Examples 

In addition to Google and advanced search pages, there are many third-​party tools for analyzing social media content. Beware that many of these tools, especially if they're free, are in danger of falling out of date, moving behind a paywall or disappearing entirely.

That's why it's important to know the fundamentals, like search syntax, so you can keep up with whichever tools are available. The most foolproof way to navigate it is to ask your fellow journalists (or even just Google!) for the most recent active tools.

\* \* \*

  ------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ***Facebook***       
  Who Posted What                             This bare-​bones site locates Facebook posts within a specific time range, location or profile.
  Sow Search                                  Another simple page that offers a search of public Facebook posts, pages, profiles, videos and events by location and date.
  CrowdTangle                                 This Facebook-​owned browser extension lets users track posts and content being shared across different social networks, like Facebook, Twitter and Instagram.
  ***Twitter***                               
  Politwoops                                  ProPublica, a nonprofit news organization, created this database of tweets deleted by newsworthy politicians.
  followerwonk                                followerwonk searches bios, followers, profile names and other criteria to analyze a Twitter user or connection.
  Social Bearing                              This media analysis tool shows tweets, hashtags, photos and other Twitter content based on a keyword search.
  ***LinkedIn***      
  LinkedIn Advanced Search                    This social network for business connections offers a robust search feature that will filter by name, location, connection and current and past employment.
  PhantomBuster                               This is a tool meant to help influencers and marketers scrape data out of LinkedIn, Twitter and other social media sites. You can export spreadsheets of LinkedIn users, companies and more.
  ***Other Social Networks***                 
  InVID                                       InVID analyzes YouTube uploads and other content for metadata including location, upload time and thumbnails.
  Snapchat Snap Map                           The Snap Map is a widely used feature showing recent Snapchat broadcasts by user and location.
  [redditsearch.io](http://redditsearch.io)   This tool by PushShift lets you filter Reddit searches by user, comment, subreddit, date and more.
  Telegram Telegago                           Telegago searches Telegram, one of the most popular messaging apps in the world, for messages, channels, contacts, bots and more.
  Discord Disboard                            Disboard searches public servers, or groups, on Discord, an application for group texts, video chat and streaming.
  VKontakte Vk.watch                          This paid, Russian-​language tool searches users on VKontakte, one of the most popular social networks in Russia.
  ClubhouseDB                                 This is a database of users and clubs on Clubhouse, a quickly growing social network popular among celebrities and public figures in the US.
  Gravatar Email Checker                      Search for someone's email address to see if they have a photo or avatar uploaded in Gravatar, a WordPress-​based profile picture site.
  SMAT                                        This tool created by open knowledge advocates searches for phrases on Gab, Telegram, Parler and smaller social networks.
  ------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

</aside>
<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
#### Pro Tip 

Social media searches will only return public content -- ​that is, posts or profiles that are not switched to private or only visible to certain circles. The "deep web" does not mean a user is "hacking" into private information -- ​just information that does not necessarily come up on search engines.

</aside>

\* \* \*

::::: section
## Tech Products and Archives

### Introduction

A lot of data is collected by tech companies, and most of it is not shared. Some of this is in the "deep web" -- ​the data that is not indexed by search engines -- ​and some of it is simply stored in the companies' private servers. Still, companies do voluntarily share some information, and it can be a good catchall for other datasets or ways to find source information.

These include nonprofits like Wikipedia, tech products like Google Scholar and websites by data enthusiasts like data.world ([Figure 2.4](#ch02.xhtml_f2_4)). Much data can also be found in past versions of pages, like the Internet Archive and Google Cache.


<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
#### Exercise 5 

The Internet Corporation for Assigned Names and Numbers (ICANN) is a nonprofit that maintains databases of many of the touchstones of the Internet, like IP addresses and domain names. One of them, WHOIS, contains the name, phone number, physical address and email address of whoever a website is registered to.

Since 2018, much of this information has been private, but a third-​party research group archived many websites' registration in a tool called the WHOIS History Search: [https://whois-history.whoisxmlapi.com/lookup](https://whois-history.whoisxmlapi.com/).

1.  In a web browser, open the WHOIS History Search. You may need to create a free account.
2.  In the WHOIS History Search, type in a website you are reporting on or interested in.
3.  Look at the most recent record. It most likely shows the registrant as a pseudonym or company.
4.  Scroll down to an earlier year, like 2017. For many sites, the registration will show the site's registrant, LLC company, phone number and address.

WHOIS data can be an excellent way to background websites, track down sources or find connections between entities.

</aside>

::::: section

## How to Determine If a Tech Source Is Reliable

Data provided by private tech companies and nonprofits should be evaluated along the same lines as nongovernmental sources. Again, remember to background the source (and ideally, the source's source) and keep a skeptical mind. They don't have mandated reporting and potentially may have a bias.

<aside class="boxed-texte" epub:type="tip" role="doc-tip">

:::: section
### Examples 

+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *Transparency Initiatives*                                                                                                                                                                                      |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Wikipedia         | Wikipedia is widely considered a credible source for detailed lists and tables of data. Each entry links to its source for the information.                                                 |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Data Commons      | Data Commons, supported by Google, is an "open knowledge" repository that brings many open datasets into one place.                                                                         |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Internet Archive  | The Internet Archive is a nonprofit repository of billions of web pages, as well as other media like books and audio files.                                                                 |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *Data Collectors*                                                                                                                                                                                               |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Statista          | Statista is a private company offering an enormous collection of data on topics and sources around the world. Some of the sources for datasets are hidden behind a paywall.                 |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Our World in Data | Our World in Data is a global data repository owned by a nonprofit and run by a research team at Oxford University.                                                 |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Kaggle            | Kaggle is a crowdsourced repository where millions of data enthusiasts upload datasets. It is owned by Google.                                                                              |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| data.world        | data.world bills itself as a collaborative data community and has been used by the Associated Press to share data with member organizations. You can search for datasets or share your own. |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *Data Products*                                                                                                                                                                                                 |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Google Scholar    | Google Scholar is an excellent place to find academic and scientific papers as well as court records. Some of these papers include their research data in full.                             |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Google Trends     | Google Trends tracks the billions of Google searches performed every day and displays them as trendlines.                                                                                   |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Westlaw           | Westlaw is a legal information database owned by Thomson Reuters. It offers a large archive of laws, case records and court transcripts.                                                    |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LexisNexis        | LexisNexis offers legal records as well as an enormous collection of public records, such as property deeds and tax assessments.                                                            |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

</aside>

:::::::: section
## Create Your Own Database

If you can't find or access the database you are looking for, you may want to create your own. One advantage is that you can later publish the dataset, creating useful resources for your audience. [Chapter 11](#ch11.xhtml_c11), Ethics, Trust, Transparency and Posting Data Online, will cover this in more detail.

The first step is to determine whether it's worth the effort. Downloading a dataset from the web is one thing, but creating your own involves a lot of time, effort and planning. That's in addition to the research, due diligence and bulletproofing that you always do.

For the technology side, make sure you are separating out values and variables as much as possible. For a table of the FIFA World Cup, it might make sense to enter one winner as "Italy 1934." But what if, later, you want to be able to show a smaller list of all the 1934 competitors? Or all the years that Italy won? From a computational standpoint, it would be better to enter "Italy" and "1934" in separate columns.

Especially if you are creating your own file, always keep a copy of raw data files somewhere else. These should be accessible somewhere on your computer, like in a folder for the story, but should be entirely untouched from when you downloaded them. You can give them a name like "FIFA raw data."

\* \* \*

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 6 

We're going to practice planning a story on the most successful soccer teams in the world. FIFA, the organization that plans the international soccer World Cup, has a list of the winners on its website dating back to 1930. Each year gets a web page with a list of the top four winners, looking something like this ([Figure 2.5](#ch02.xhtml_f2_5)):


This website would be a good candidate for scraping -- ​computationally extracting the data -- ​but for now we will form a plan for collecting the data manually.

1.  In a word document, write an outline for a story on which countries have the most successful teams. Rely on your earlier journalism training: What is the most important aspect to the story? What information does the audience *most* want to know?

2.  Write a lede with the letters "TK" (to come) to note where the data and findings will go. For example, "France won TK World Cups from 1930 to 2022."

3.  Create a list of the information you would need to find this out.

4.  Next, create a list of rows, separating out each variable, so you can run the proper analysis. There are several ways to design your table, but here are two examples ([Tables 2.1](#ch02.xhtml_t2_1) and [2.2](#ch02.xhtml_t2_2)).

    ::: 
      *Year*   *First Place*   *Second Place*   *Third Place*   *Fourth Place*
      -------- --------------- ---------------- --------------- ----------------
      1930     Uruguay         Argentina        US              Yugoslavia
      1934     Italy           Czechoslovakia   Germany         Austria

      : *[Table 2.1*](#ch02.xhtml_t2_1b) A table of World Cup winners by year
    :::

    ::: 
      *Country*   *Year*   *Placement*
      ----------- -------- -------------
      Uruguay     1930     1
      Argentina   1930     2
      US          1930     3

      : *[Table 2.2*](#ch02.xhtml_t2_2b) A table of World Cup winners by country
    :::

As you can see, it can be a lot of work to manually enter this data. Each of these tables has advantages and disadvantages when it comes to the ease of your analysis, which will come later.

</aside>
<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Pro Tip 

Many journalists also recommend creating a "notes" or "miscellaneous" field, typically all the way to the right in the spreadsheet. You don't even need to know what it is for yet -- ​but it will act as a catchall for annotations, reminders, attributions or unanswered questions.

Make sure to create it as a separate column so that you aren't combining values and comments in the same cell.

</aside>

\* \* \*

<aside class="boxed-texte" epub:type="tip" role="doc-tip">

::: section
#### Examples 

Once you have designed your database and found your source, there are many ways to collect the data.

</aside>

::: section
### Manual Entry

Manual data entry -- ​the method we used in the FIFA exercise -- ​can be one of the most time-​consuming but also one of the most precise ways to collect and store data. This can be anything from one reporter keeping track of their findings in a spreadsheet to a team of journalists creating databases in advanced programs.

Two good tools for this method are Google Sheets and Airtable. Both are free, or have free tiers, and offer sophisticated features for multiple users to store, tag and organize data.

Past data journalists have also taken advantage of resources like students, civic data enthusiasts and short-​term hires for data entry. In 2021, Reuters won a Pulitzer Prize for a project on qualified immunity for police. Part of the project relied on students at Stanford distilling thousands of court records into a database ([Figure 2.6](#ch02.xhtml_f2_6)).


::: section
### Crowdsourcing

Crowdsourcing means soliciting data or volunteer work from the public. Survey tools, like Google Forms and Survey Monkey, can make the technological aspect of this data collection easy.

Crowdsourcing is often considered one aspect of "engagement reporting" -- ​making the audience more of a player in a story's reporting than a passive recipient. In 2017, ProPublica published a call for submissions with the title "Do You Know Someone Who Died or Nearly Died in Childbirth? Help Us Investigate Maternal Health." The result was a widely read story on childbirth-​related deaths and injuries in the US.

::: section

## Combining Existing Data

Sometimes, data is available, but it doesn't quite suit your purposes. For a story on wildfires in California, for example, you could collect data from the National Interagency Fire Center, the California Department of Forestry and Fire Protection, the University of California -- ​Riverside or other sources. Each of these will have different advantages and disadvantages to their data collection.

Because each of them tracks and records data on wildfires in a different way, combining them might mean manually entering them in a spreadsheet. If they have matching columns, you can join them using a tool called Structured Query Language, to be discussed in [Chapter 8](#ch08.xhtml_c8).

## Footnotes

- IMF Data [https://www.imf.org/en/Data](https://www.imf.org/)
- World Economic Outlook [https://www.imf.org/en/publications/weo](https://www.imf.org/)
- World Economic Outlook Update January 2021 [https://www.imf.org/en/Publications/WEO/weo-database/2020/October](https://www.imf.org/)
- Global Investigative Journalism Network, How They Did It: The Real Russian Journalists Who Exposed the Troll Factory in St. Petersburg [https://gijn.org/2018/03/26/real-russian-journalists-exposed-troll-factory-st-petersburg/](https://gijn.org/)
- Hidden Crimes: UCR Data, and What's Not There [https://www.ire.org/product/tipsheet-3313/](https://www.ire.org/)
- FBI Crime Data Explorer [https://crime-data-explorer.app.cloud.gov/pages/home](https://crime-data-explorer.app.cloud.gov/)
- [Data.gov](http://Data.gov) [Data.gov](http://Data.gov)
- Open Data Portal Russia [Data.gov.ru](http://Data.gov.ru)
- UNdata <https://data.un.org>
- PACER <https://pacer.uscourts.gov/>
- Search \| International Court of Justice [https://www.icj-cij.org/en/advanced-search](https://www.icj-cij.org/)
- International Criminal Court [https://www.icc-cpi.int/Pages/cases.aspx](https://www.icc-cpi.int/)
- United Nations Treaty Series [https://treaties.un.org/pages/UNTSOnline.aspx?id=3&clang=\_en](https://treaties.un.org/)
- Library of Congress <https://www.congress.gov>
- US Federal Election Commission [https://www.fec.gov/data/](https://www.fec.gov/)
- US Securities and Exchange Commission [https://www.sec.gov/dera/data](https://www.sec.gov/)
- Berkeley Earth Surface Temperatures <http://berkeleyearth.org/>
- United States Petroleum Statistics [https://www.ipaa.org/economics/](https://www.ipaa.org/)
- Petroleum Statistics shortlink [https://bit.ly/petroleumstatistics](https://bit.ly/)
- ClimateWatch <https://www.climatewatchdata.org/>
- Independent Petroleum Association of America <https://www.ipaa.org/>
- State Gun Laws [https://www.nraila.org/gun-laws/state-gun-laws/](https://www.nraila.org/)
- ILOSTAT <https://ilostat.ilo.org>
- FIFA World Cup [https://www.fifa.com/tournaments/mens/worldcup](https://www.fifa.com/)
- National Retail Federation <https://nrf.com/>
- State of Retail [https://nrf.com/topics/economy/state-retail](https://nrf.com/)
- About Heritage [https://www.heritage.org/about-heritage/impact](https://www.heritage.org/)
- About Us \| The Brookings Institution [https://www.brookings.edu/about-us/](https://www.brookings.edu/)
- American Bar Association <https://www.americanbar.org>
- Offshore Leaks Database <https://offshoreleaks.icij.org>
- Dollars for Docs Data (2017--2018) [https://www.propublica.org/datastore/dataset/dollars-for-docs](https://www.propublica.org/)
- UK Data Archive <https://www.data-archive.ac.uk/>
- Assessing the Performance of Freedom of Information [https://www.sciencedirect.com/science/article/abs/pii/S0740624X10000614](https://www.sciencedirect.com/)
- Global Trends in Lifespan Inequality [https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0215742](https://journals.plos.org/)
- Charity Navigator <https://www.charitynavigator.org/>
- Sunlight Foundation <https://sunlightfoundation.com/>
- OpenCorporates <https://opencorporates.com>
- Twitter Advanced Search [https://twitter.com/search-advanced?lang=en](https://twitter.com/)
- Rules and filtering: Standard v1.1 [https://developer.twitter.com/en/docs/twitter-api/v1/rules-and-filtering/search-operators](https://developer.twitter.com/)
- Tornadoes from Rare Supercell Caused Damage in Georgia r/news [https://www.reddit.com/r/news/comments/ru92dd/tornadoes_from_rare_supercell_caused_damage_in/](https://www.reddit.com/)
- Who Posted What <https://whopostedwhat.com>
- Sow Search <https://www.sowsearch.info>
- CrowdTangle <https://www.crowdtangle.com/>
- Politwoops [https://projects.propublica.org/politwoops/](https://projects.propublica.org/)
- Followerwonk <https://followerwonk.com>
- Social Bearing <https://socialbearing.com>
- LinkedIn Advanced Search [https://www.linkedin.com/search](https://www.linkedin.com/)
- PhantomBuster <https://phantombuster.com/>
- InVID Project <https://www.invid-project.eu/>
- Snap Map <https://map.snapchat.com/>
- Reddit Finder [https://archivesort.org/redditfinder](https://archivesort.org/)
- Telegago [https://cse.google.com/cse?&cx=006368593537057042503:efxu7xprihg#gsc.tab=0](https://cse.google.com/)
- Public Discord Servers [https://disboard.org/servers](https://disboard.org/)
- Vk.watch <https://vk.watch/>
- Clubhouse Database <https://clubhousedb.com>
- Gravatar Email Checker [https://en.gravatar.com/site/check/](https://en.gravatar.com/)
- SMAT <https://www.smat-app.com/>
- WHOIS History Search [https://drs.whoisxmlapi.com/whois-history](https://drs.whoisxmlapi.com/)
- Wikipedia [https://en.wikipedia.org/wiki/Main_Page](https://en.wikipedia.org/)
- Data Commons <https://datacommons.org/>
- Internet Archive <https://archive.org/>
- Statista <https://www.statista.com/>
- Our World in Data <https://ourworldindata.org/>
- Kaggle <https://www.kaggle.com/>
- data.world <https://data.world>
- Google Scholar <https://scholar.google.com/>
- Google Trends [https://trends.google.com/trends/](https://trends.google.com/)
- Westlaw [https://legal.thomsonreuters.com/en/westlaw](https://legal.thomsonreuters.com/)
- LexisNexis [https://www.lexisnexis.com/en-us/gateway.page](https://www.lexisnexis.com/)
- Shielded [https://www.reuters.com/investigates/section/usa-police-immunity/](https://www.reuters.com/)
- How Stanford Students Helped with a Pulitzer Prize-Winning Project [https://news.stanford.edu/report/2021/06/15/stanford-students-helped-pulitzer-prize-winning-project/](https://news.stanford.edu/)
- Do You Know Someone Who Died or Nearly Died in Childbirth? Help Us Investigate Maternal Health [https://www.propublica.org/getinvolved/help-propublica-and-npr-investigate-maternal-mortality](https://www.propublica.org/)


# 3 Scraping Data

Mike Reilley and Samantha Sunne

DOI: [10.4324/9781003273301-4](https://doi.org/10.4324/9781003273301-4){aria-label="D.O.I. link to this document."}

Reporters often grouse when government officials fulfill a public information request by sending a PDF or a web page with data embedded in tables. This is often done to frustrate reporters, even after they've specifically asked for the data to be sent in a spreadsheet, Word doc or other usable format.

Appealing to get the data in the requested format can take days, even weeks. And government agencies also may charge for that.

But there are many free tools to solve this problem and extract data from web pages and pesky PDFs.

Data scraping is the process of extracting information from a source file into a spreadsheet, when it's more difficult than simply clicking "Download." You can "scrape" data from a website, PDF, image or other document. It's an efficient way to get data and, in some cases, to channel that data to another website.

Lena Groeger, a journalist, designer and developer with ProPublica, often must scrape data to build interactive graphics, databases and other data-​driven projects.

"A web page is basically a bunch of stuff that gets downloaded," she tells journalists she trains on scraping.

"Really, that's it. Slightly more technically, it's a bunch of different files that get downloaded -- ​some text files and maybe some images. The best way to see the "behind the scenes" of a webpage is to use a tool called the web inspector to actually look at these files."

The Web Inspector is a panel available in every browser that lets you navigate through the components that go into rendering the web page you see. It also has several features to help achieve better performance, find bugs, check mobile views and more ([Figure 3.1](#ch03.xhtml_f3_1)).


For example, go to [WashingtonPost.com](http://WashingtonPost.com), then right-​click and select "Inspect Element." You can now look at the contents of the files making up the page, including the underlying HTML, the Cascading Style Sheets (CSS) that style the page and much more. Viewing a page with a Web Inspector also shows code for tables \<table\>, table rows \<tr\> and table data \<td\> that can be scraped into a Google Sheet.

A "table" is a word you will come across often in your data journalism journey. A table is generally referred to as anything with rows and columns. You'll find tables in PDFs, spreadsheets, pieces of paper and many other sources. In this case, it is a very specific HTML element that is identifiable by the \<table\> tag.

Data scraping gives journalists extra artillery in acquiring data, which we explored in [Chapter 1](#ch01.xhtml_c1). If seeking data from a source doesn't work, try downloading or scraping it on a computer ([Figure 3.2](#ch03.xhtml_f3_2)).


Typically, journalists scrape data to move it into a spreadsheet so they can manipulate and analyze it to find patterns and develop story ideas. This data often explores assumptions or theories journalists have about an issue or story idea. We'll refine the storytelling process in later chapters, but first, we must master the basics of obtaining data from the web and from PDFs.

:::::: section

## Scraping from the Web

At ProPublica, Groeger creates influential and award-​winning infographics by combining programming knowledge with visual design and human-​centered storytelling. In order to build these incredible data visualizations, Groeger must first find the datasets that power those graphics. Sometimes, she'll simply download a file from a web portal. But other times the data is nested in web tables without a download button. So how can she extract it? This is a subset of data scraping called "web scraping."

There are many tools at her disposal, but one she often reaches for is a simple scraping formula: =IMPORTHTML(\"URL\", \"ELEMENT\", NUMBER OF ELEMENT ON PAGE)

Many of us have used spreadsheet formulas before to solve a math problem. If you are new to formulas or functions, we will cover them more in [Chapter 5](#ch05.xhtml_c5).

This formula tells your Google Sheet to go to the web and scrape a page located at a specific uniform resource locator (URL). You'll select the HTML element to scrape (usually a table) and where that element appears on the web page. For this last part, you'll often type 0 (zero) as it tells the sheet to go to the first table on the page.

An HTML element is an individual component of a much longer "HTML document" -- ​aka, the web page you are looking at. Elements are recognizable by their distinctive \<\> tags. That is, if you find "\<table\>" in the HTML of a web page, that means you are looking at the beginning of a table element. It ends with a "\</table\>" tag.

The scraping formula works because web tables have what are called "nested elements," elements that are embedded inside other elements. So within an HTML \<table\> element, you'll find a table row \<tr\>, and within those rows, you'll find table data \<td\> code that creates the small cells that include the data we seek. Because of this nested format, we can identify and scrape a table element and all of the elements inside of it ([Figure 3.3](#ch03.xhtml_f3_3)).


The scraping formula also provides another feature helpful to journalists. Once linked to a web page, the formula continues to update the spreadsheet as the web page is updated. For instance, if you scrape an election results page on election night, the results will continue to update in the sheet as the web page is updated, up to once a day. This is an excellent option for reporters tracking government pages that update daily, weekly, monthly, etc.

To do analysis or to save a snapshot of the data, you must make a copy of the dataset and work off that copy. Google Sheets won't allow you to work on the scraped page. Once you start editing, you'll get an error message.

\* \* \*

With this kind of scraping, the first step is to understand the URL you are going to scrape from: [https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/](https://www.fdic.gov/). Web scraping, and this method of web scraping in particular, requires very specific URLs to work. In this case, we are looking at a website called "fdic" on a government domain, that is, ending in ".gov". We are looking at a specific web page on that website called "failed-​bank-​list", and it is in a section called "resources" and various subsections.

It's important to understand the difference between websites and web pages, especially with scraping. If you don't cite this specific URL -- ​for instance, if you try to scrape a table on "[fdic.gov](http://fdic.gov)" -- ​you will get very different results.

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 1 ![](images/Exercise_Icon.jpg) 

The best way to learn how to use the scraping formula is to test it out on some datasets. In this book, we will use Google Sheets for a variety of data tasks, because it is free and only needs to be run in a web browser. If you do not have a Google Drive account, you can create one for free.

For this exercise, we're going to scrape a table of failed banks tracked by the Federal Deposit Insurance Corporation (FDIC). The FDIC is a US government agency that insures banks so that people feel comfortable depositing their money there. If you look through the list, you can see that several small banks in various US states have closed their doors over the years. This web page lists closures going back to the year 2000.

1.  To get started, open a Google Sheet by going to your browser and typing "sheets.new" into the URL bar and hitting return. A spreadsheet will appear. If you need to, sign into your Google Drive account or create a new one.

2.  Label your spreadsheet: Click in the upper left and name it "FDIC scrape."

3.  Next, type in this formula. Do not copy and paste, as this is likely to cause errors.

    =IMPORTHTML(\"URL\", \"ELEMENT\", NUMBER OF ELEMENT ON PAGE)

4.  Add this URL to the formula: [https://www.fdic.gov/resources/resolutions/bank-​failures/failed-​bank-​list/](https://www.fdic.gov/)

5.  Enter "table" as the element. Be careful not to delete any code, and don't leave a space after the web address when pasting it in.

6.  Now add the table number (in this case a 0 as you're starting at the top of the first page). It should look like this:

    =IMPORTHTML(\"[https://www.fdic.gov/resources/resolutions/bank-​failures/failed-​bank-​list/](https://www.fdic.gov/)\", \"table\", 0)

7.  Press enter. If you get an error message, review the steps above, copy and paste your error message into Google or see the Troubleshooting Common Spreadsheet Errors section in [Chapter 4](#ch04.xhtml_c4).

    **\*Note:** Depending on your Google Sheets language settings, the delimiter in the function could be "," or ";" but is usually a comma.

8.  If done correctly, the entire table of banks should appear in your spreadsheet. Once you have scraped the page, do a slow scroll to make sure you haven't missed any data or there are no garbles ([Figure 3.4](#ch03.xhtml_f3_4)).


9.  Now you're ready to edit, sort and filter. There's just one problem: If you go to type on the screen after you scrape, your data disappears. This is because the spreadsheet is linked to the web page, as discussed earlier. When the web page updates, so does the sheet. That prevents us from editing.

10. To remedy the issue, highlight all the data on the screen and copy it. One way to highlight everything without scrolling down is by pressing Ctrl+A or Cmd+A. Then click on the Plus Sign in the lower left corner of the Google Sheet to open a new tab. Click on the "Sheet 2" language on the tab to rename it "EDITS" or whatever you want.

11. To paste the data into the new sheet, click on cell A1 and then click Edit \> Paste Special \> Values only. Presto! Your data appears in the new sheet and is now editable. You still have your original scraped sheet in the first tab, which will update up to once a day.

12. Now you have your dataset in a format you can edit. But there's another issue (who said scraping was easy, right?): It appears that the date format changed to a number that looks something like a ZIP code. This sometimes happens when cutting and pasting dates that use both letters and numbers.

</aside>
<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Pro Tip 

You always, always, always work off a COPY of your dataset in case you mess something up. You may want to save an offline copy by clicking File \> Download \> Microsoft Excel.

</aside>

It's an easy fix. Just click on the letter C to highlight the column, then go to the pull-​down menu at top of the page and select Format \> Number \> Date, and it will reformat the dates for you.

You have probably noticed that scraping the data directly from a website came with some garbles -- ​for instance, the header row contains repeated terms, like "CityCity". Watch for these small glitches as you scrape and move data, and check it after each step in the process. We'll talk about this more in [Chapter 4](#ch04.xhtml_c4).

Now your dataset is ready to be sorted, filtered and analyzed. There will be more spreadsheet work and more scraping in [Chapters 5](#ch05.xhtml_c5), [6](#ch06.xhtml_c6) and [9](#ch09.xhtml_c9).

<aside class="boxed-text2" epub:type="tip" role="doc-tip">


- Video: Scraping in Google Sheets and Tabula: [https://bit.ly/sheetscrape](https://bit.ly/)

</aside>
<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
#### Exercise 2 ![](images/Exercise_Icon.jpg) 

Here are some more pages you can practice scraping with this formula. Just plug one of these web addresses into the formulas below.

**Ireland Trolley Ward Watch** [https://www.inmo.ie/Trolley_Ward_Watch](https://www.inmo.ie/)

**National Interagency Fire Center: US Wildfires** [https://www.nifc.gov/fire-​information/statistics/wildfires](https://www.nifc.gov/)

1.  Type "sheets.new" into the browser window.

2.  Paste both links into the area where it says URL in the formulas below.

    1.  =IMPORTHTML(\"URL\", \"table\", 0)
    2.  =IMPORTHTML(\"URL\", \"table\", 0)

3.  Copy the formula and paste into cell A1 in your sheet, and then repeat the steps for making a copy of the data.

</aside>

::: section
## When You Have Multiple Tables on a Page

Some web pages have several tables, like this example from Washington, D.C.'s, COVID-​19 testing site. We're looking for the table that appears fourth on the page and focuses on the addresses of testing centers. To scrape only this table, you must tweak the table number at the end of the formula to 3. It's not 4, as your table numbers start with 0. Here's the formula to try:

=IMPORTHTML(\"[https://coronavirus.dc.gov/testing](https://coronavirus.dc.gov/)\", \"table\", 3)

This table would be good for a map or list in a story, as it contains the addresses of the testing locations.

::::: section

## Scraping More Than Tables

Besides IMPORTHTML, Google Sheets offers a few other formulas for scraping data from the web.

- IMPORTRANGE: Imports a range of cells from a specified spreadsheet.
- IMPORTFEED: Imports an RSS or ATOM feed.
- IMPORTDATA: Imports data at a given URL in comma-​separated value (CSV) or tab-​separated value (TSV) format.

You can also use a more flexible formula called IMPORTXML. It's very similar to IMPORTHTML but with a much more complex section to it:

1.  =IMPORTXML(\"URL\", \"XPath\")

What makes this formula flexible is the second parameter, the XPath. A "parameter" is the variable you are entering into a formula so the formula knows what to do. The IMPORTXML formula has two parameters: a URL and an XPath.

An XPath is like an address to a very, very specific point on the web. Think of it like a physical address. Let's say a mailman is walking down the street, delivering letters and packages all over the city. He reaches into his bag and pulls out an envelope with the name "Mary Contrera" on it. How does he know where it goes?

The mailman needs to know not just what city Mary lives in but what road she lives on and where her building lies on the road. Sometimes he needs to know the number of an apartment within that building or the floor it's on. Luckily, the envelope has an address on it, like this:

1.  421 Crescent Drive, Apt. 4, Maughantown, NY 80123

This tells the mailman that the letter is going to the building numbered 421, on the street "Crescent Drive," in the town of Maughantown in the state of New York. This address is read from smallest to largest.

Right away, you might notice some not-​insignificant leaps of logic here. For instance, when the mailman reads the mailing address, he actually reads the zip code first -- ​the last part. A ZIP code itself is made up of multiple codes designating areas within areas.

<aside class="boxed-text2" epub:type="tip" role="doc-tip">

For more data journalism tips, tricks and exercises, visit the Data + Journalism blog at <http://dataplusjournalism.com>

</aside>

And this address has an apartment number between the street name and city name, further complicating the procedure. Mail deliverers and computers alike are trained to read these addresses and sort the mail accordingly. With this method, the US Postal Service is able to sort and deliver more than 173 million pieces of mail every day.

The postal address system makes that possible, and so does the XPath system on the web. Just like the mailman, a web browser needs to know what to show you, and it needs to process billions or even trillions of these requests each and every day.

Let's say you're doing a story on the Mountain National Bank and want to know what state it's in. How does the computer know to show you that, and not, say, the state of the Mountain Heritage Bank? It doesn't inherently know where this information is, just like the mailman doesn't automatically know where Mary lives.

The answer is the data's XPath, which looks something like this:

1.  //table//tr\[56\]/td\[3\]

This might seem confusing at first, but that's only because we're accustomed to reading physical addresses, designed for humans, and not digital addresses, designed for computers. But we can break it into parts and decipher it the same way.

Unlike a mailing address, an XPath is read from largest to smallest. This one says, "on this page, in the table, in table row 57, in table column 3."

If you find that cell in the human-​targeted version of the FDIC website, you'll find your answer -- ​the Mountain National Bank is in TN, or Tennessee ([Figure 3.5](#ch03.xhtml_f3_5)).


So how can we use XPaths to get our hands on some data? The answer is to learn to construct your own. This can be easy or hard, depending on the complexity of your data and the source code.

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 3 ![](images/Exercise_Icon.jpg) 

Later in this book, we'll explore some of the more complicated aspects of using source code, but for now, let's use this simple example to scrape the failed bank page.

In your Google Sheet, use the + sign at the bottom of the window to open a new tab within your Sheet. Rename it to "IMPORTXML scrape" or something similar. In the first cell (A1), type this formula:

=IMPORTXML(\"[https://www.fdic.gov/resources/resolutions/bank-​failures/failed-​bank-​list](https://www.fdic.gov/)\", \"//table//tr\[56\]/td\[3\]\")

If you hit enter, the sheet should populate with exactly one piece of data: The state where the bank is located. That's because the XPath we gave it, the second parameter in the formula above, points to this exact piece of data on a long page full of data. Again, if you get an error message, review the steps above or refer to the Troubleshooting section in [Chapter 4](#ch04.xhtml_c4).

</aside>
<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 4 

You can edit the XPath to show other bits of data, for instance, the state of the Mountain Heritage Bank. If you look at the web page, the Mountain Heritage Bank is the 167th row in the table, so you would change "tr\[56\]" to "tr\[167\]".

</aside>

:::: section
## Creating XPaths

That leads us to the next question: How do you create your XPath or find the XPath of an existing piece of data? This chapter will explain two possible ways. Each has its own benefits and drawbacks.

One way is to read through the source code. You can view the source code of a web page by right-​clicking on a white space and selecting "View Source."

You have already learned the basics of nested HTML elements. Simply string those together, with slashes in between, to narrow down the code until you get to just the data you want, like this.

1.  //div\[3\]//ul\[2\]/li\[1\]/a\[1\]

Another way is to open the data you want in the Web Inspector. As we discussed earlier in this chapter, you can open an element in the Web Inspector by right-​clicking on it and selecting "Inspect element." Once the Web Inspector panel has opened, you can right-​click again on the element within the code panel.

It should give you a number of options including Copy. Hovering over Copy should give you the option "Copy XPath." You can copy and paste that XPath straight into your formula (remember to put it inside quotes).

But there is a drawback to this cheat code: Often, the XPath copied from the Web Inspector contains extra elements and bits of code that Google Sheets struggles to read. This is one of the many road bumps that exist when you try to work with source code across different programs.

The way over this hurdle is to simply paste in your copied XPath and troubleshoot from there. You can cut out HTML elements you're unfamiliar with, like "tbody." You can use the "View Source" tool to see the source code and determine which elements your data is nested in. You can use your critical thinking to figure out extraneous elements (e.g., does your XPath really need to say "div/div/div/div/div/"?).

Even with these road bumps, you can see how IMPORTXML is a much more flexible formula than IMPORTHTML. IMPORTHTML will only pull in a whole table (or a list), but XML can pull in just part of a table, the whole table itself or even more. Instead of one table cell, you could give the address for a whole column, or even a descriptor, like all the text that is bold.

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 5 

Let's try using IMPORTXML to scrape another specific kind of data -- ​a whole category.

Earlier, we changed an XPath to the 22nd row by changing the number in the element "tr\[\]." We could instead collect all of the rows by deleting that limiter entirely.

//table/td\[3\]

Changing your formula to this XPath should result in the spreadsheet importing all of the rows of data, but only the fourth column.

</aside>

::::: section

## Scraping with Code

Now we're going to experiment with a slightly more ambitious way to scrape: Writing our own code! Here is the simple code script we are going to run, using a Python library called Pandas.


    import pandas
    table   =   pandas.read _ html("https://www.fdic.gov/resources/
    resolutions/bank-​failures/failed-​bank-​list/")
    output _ table = table[0]
    output _ table.to _ csv("failed _ banks.csv")

Luckily, there are only four steps. Let's read through them:

1.  "Import pandas" installs the Pandas Python library. Usually, when writing code, you'll need to install add-​ons to make it work. In Python, these are called "libraries," but they go by different names in different languages.
2.  The second line imports the HTML where our table is located. Once again, make sure you are using the exact URL and not just the website as a whole.
3.  The third line identifies which table we want, similar to the third parameter in the IMPORTHTML function. This example is easy because there is only one table on that page. We use the number "0" because that's often how a computer counts -- ​the first instance of something is considered number zero.
4.  Lastly, we convert the HTML table into a CSV and give our file a name.

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 6 

Let's try it. Later in [Chapter 9](#ch09.xhtml_c9), we will install Python on our computers and create our own programs, but for now, we'll just use a Google Drive tool called Colaboratory.

Colaboratory is basically Google Docs for code. First, you'll need to enable it as an add-​on for Google Drive. You can do this in Drive by clicking New \> More \> Connect more apps and search for "Colaboratory."

Once you have it installed, in your Google Drive, click New \> More \> Google Colaboratory. This will create a Colaboratory file, called a "notebook." Name your notebook "FDIC scrape."

Then, type each of the four steps into your notebook ([Figure 3.6](#ch03.xhtml_f3_6)). You can create new lines by clicking "+ Code" at the top. Once the four lines are in the coding interface, click Runtime \> Run all to execute it. A file will appear in the Files section, which looks like a small folder in the left-​hand sidebar.


You have now obtained data through websites, spreadsheet formulas and writing your own code.

</aside>
<aside class="boxed-text2" epub:type="tip" role="doc-tip">

For more data journalism tips, tricks and exercises, visit the Data + Journalism blog at <http://dataplusjournalism.com>

</aside>
<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Pro Tip: Legal Issues and Data Scraping 

Much of the data that journalists scrape is public record, like government databases. But some datasets are proprietary and are protected by copyright law, including many in academic research.

Always check for usage rights, and reach out to the authors if you're unsure if you can use the dataset without paying a fee. Google Dataset Search is a good tool for this as you can filter out the paid websites in your search.

</aside>

:::: section
## Scraping with a Browser Extension

Besides the scraping formulas, there are many other ways to scrape web pages. One of the easiest to use is Scraper, which is available for free on this Github page: [http://mnmldave.github.io/scraper/](http://mnmldave.github.io/)

Once you install the extension in your browser, a small icon with a putty knife appears in the plug-​ins area at the top of your browser. There's no need to click on it. The installation has turned your browser into a scraping machine.

It's important to note that this tool works differently than the formulas. It is a "one-​time" scrape, similar to copy-​pasting the data. It doesn't continually scrape the web page into the sheet, like the Google Sheets formula does.

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 7 ![](images/Exercise_Icon.jpg) 

Practice the Google Chrome scraper extension with these datasets. It's a snap. Just highlight the row you want to scrape, right-​click on it (Control+click on a Mac) and the data appears in a dialog box. Just hit the "Copy to Clipboard" button, and paste it into your spreadsheet. It works with Google Sheets or Excel.

**FDIC Failed US Banks List** [https://www.fdic.gov/resources/resolutions/bank-​failures/failed-​bank-​list/](https://www.fdic.gov/)

**ESPN: 2019 Major League Baseball Attendance** [http://www.espn.com/mlb/attendance/\_/year/2019](http://www.espn.com/)

</aside>

::::::: section

## Scraping Documents

There's a running joke that if you want to tick off journalists, just email them a dataset in PDF format. PDFs are the scourge of the data journalism world as they provide valuable data but in a format that's useless. You cannot sort, filter or analyze the data in a PDF, so you must first extract it. The same applies to Microsoft Word, plain text files and other documents.

When requesting public documents, journalists should always ask for them in the electronic format they want to use, like an Excel sheet. But the records often arrive as a PDF.

Adobe Acrobat Pro allows users to convert PDFs into spreadsheets, Word docs or other usable formats. But many newsrooms don't have the software as it's very expensive.

There are many free tools that will easily scrape data from both "native" PDFs -- ​such as Excel or Word documents saved in a PDF format -- ​and "scanned" PDFs that have been scanned from old paper records.

Tabula is a free software you can download to your Mac or PC that scrapes tables out of PDFs. It was created by journalists and is wildly popular among investigative journalists because it's secure. Rather than loading the PDF to a live website like [PDFtoExcel.com](http://PDFtoExcel.com), they can scrape the file right on their desktop, which is much more secure.

Tabula doesn't work on scanned or image PDFs. But what it can do is identify and scrape tables throughout a whole document, even if it's many pages. Just download the software at Tabula.technology to get started ([Figure 3.7](#ch03.xhtml_f3_7)).


<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 8 

Let's use Tabula to scrape a table out of a PDF with state voter registration statistics from the Nevada Secretary of State's office.

1.  To get started, download the PDF to your computer from this folder: [https://bit.ly/scrapepdfs](https://bit.ly/)
2.  Now open Tabula from the applications folder on your computer. It should open as a tab in a web browser.
3.  In the Tabula interface, select the blue "Browse" button, and select the Nevada PDF you downloaded. The name of the file will appear in the text field.
4.  Hit the gray "Import" button next to the field to import the PDF.
5.  Your PDF will appear in the interface. Click the gray "Autodetect Tables" button above the PDF. This will turn your table pink.
6.  Now hit the green "Preview & Export Data" button in the upper right corner. This will convert your PDF into a table.
7.  In the export format dropdown menu, select CSV -- ​for a CSV file -- ​and hit the export button.
8.  Your spreadsheet will download to your computer. Then you can open the file in Excel or Google Sheets to clean and format the data.

</aside>
<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 9 

Let's repeat the steps from the previous scraping exercise; only this time we'll scrape the file on North Carolina COVID-​19 outbreaks located in this folder: [https://bit.ly/scrapepdfs](https://bit.ly/). The North Carolina data is a much larger file and will take longer to scan and download. Repeat the steps in Exercise 8 to scrape and open it on your computer.

</aside>
<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
#### Exercise 10 

Another method to scrape is to use simple websites. These tend to be very simple and are therefore easy to use but not as powerful or customizable as spreadsheet formulas or downloadable software.

[PDFtoExcel.com](http://PDFtoExcel.com) is a free tool that lets you directly load a PDF into this browser-​based tool for a free scrape. It will convert native PDFs as well as scanned PDFs by using optical character recognition (OCR) software built into it.

A word of caution: Be careful with scanned documents and OCR. Characters often get misread. A 3 can look like an 8 when converted, or a 7 may appear as a 2. After scraping, make sure to carefully review the spreadsheet to make sure the data is clean.

1.  Go to this folder: [https://bit.ly/scrapepdfs](https://bit.ly/) to download the scanned PDF from the Clinton Foundation's 2003 Form 990.
2.  Open [PDFtoExcel.com](http://PDFtoExcel.com) and hit the red upload button.
3.  Select your PDF, and it will upload. You'll need to wait up to a minute as it converts, even for a smaller file.
4.  Once it's converted, a red button titled "Free Download" appears. Hit that button, and your spreadsheet will download to your computer. You can clean and format it in Excel or Google Sheets.

The free version of PDF to Excel works fine for smaller documents such as the one you just scraped. It offers a \$5 monthly version that reduces wait time and allows you to process a larger batch of files.

Another drawback to PDFtoExcel is security. You're loading a document to the live web, which means it's vulnerable. If you need to scrape a sensitive document, use Tabula.

</aside>

\* \* \*

<aside class="boxed-text2" epub:type="tip" role="doc-tip">


[https://bit.ly/videoscrape](https://bit.ly/)

</aside>
<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
##### Exercise 11 

**Scrape Data from Google Finance**

Business and tech reporters keep a close eye on the stock exchange. Google Finance ([https://www.google.com/finance/](https://www.google.com/)) lets you not only build a free portfolio of stocks to track, but you can also use formulas in Google Sheets to scrape real-​time and historical stock prices and other data.

To get started, open our practice spreadsheet (shortlink: [https://bit.ly/scrapefinance](https://bit.ly/)), and make a copy of it by going to File \> Make a Copy.

Note that there are two tabs at the bottom of the sheet. One for our first two exercises and a third for the single stock focus exercise.

These exercises will walk you through how to set up your own spreadsheet and write specific formulas. You also can consult this list of Google Finance scraping formulas: [https://bit.ly/scrapeformulas](https://bit.ly/)

</aside>

::: section
## Scraping Real-​Time Stock Data into a Google Sheet

1.  Open sheets.new in a browser window.

2.  In Row 1, create a header. Type "symbol" in cell A1, "price" in B1, "pe" in C1 and "price52" in D1. The phrase "pe" means price earnings ratio, and "price52" is the 52-​week high price.

3.  In Column 1 under "symbol," type some stock symbols in rows 2--​4:

    1.  goog
    2.  vz
    3.  nke
    4.  f

    Those are the symbols for Google, Verizon, Nike and Ford. Those symbols and cells are what the Sheet will use to pull the correct data from Google Finance.

4.  Now you're ready to scrape data into each of the cells:

    In cell B2, type: =googlefinance(A2,B1) and hit return for the price

    In cell C2, type: =googlefinance(A2,C1) and hit return for the price earnings ratio

    In cell D2, type: =googlefinance(A2,D1) and hit return for the 52-​week high price

    Repeat these steps for the other cells, changing A2 to A3, A4, A5, etc.

    These functions will auto-​update over time so you'll see current prices.

::: section

## How to Scrape Historical Stock Prices

1.  In the same spreadsheet, type: =GOOGLEFINANCE(a4, \"price\",\"12/09/2020\", today(), \"daily\") in cell E1 to get daily ending prices since Dec. 9, 2020 (or adjust date/price category as you see fit).
2.  Type: =GOOGLEFINANCE(a3, \"price\",\"12/09/2020\", today(), \"weekly\") in cell G1 to get end-​of-​week prices since Dec. 9, 2020 (or adjust date/price category as you see fit).
3.  These functions will auto-​update over time so you'll see current prices.

:::: section
## Focusing a Sheet onto One Stock

1.  Open a Google Sheet by typing sheets.new into the browser field.

2.  Set up a sheet to look like [Figure 3.8](#ch03.xhtml_f3_8), and then in cell B2 under Value, type this formula and hit return:

    1.  =GOOGLEFINANCE(\"AAPL", A2)

    Then grab the blue square in the lower right of the cell and drag down: It will populate the sheet with data from Apple stock, and it'll update as the market changes.


**Formulas:** To get help on any of the formulas, click on the blue button on the cell when you type in =GOOGLEFINANCE. You also can see them when you hit return after typing in Googlefinance, and you can find many of them listed here: [https://support.google.com/docs/answer/3093281?hl=en](https://support.google.com/)

<aside class="boxed-text2" epub:type="tip" role="doc-tip">

**Training Video: How to Scrape Google Finance.** Review how to do these exercises in this short video: [https://bit.ly/gfinancevideo](https://bit.ly/)

</aside>
<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 12 

**Scraping Comments from Social Media**

We will explore social media scraping with code in [Chapter 9](#ch09.xhtml_c9), but a quick and easy way to extract comments, tweets and more from social media posts is to use a browser-​based tool called [ExportComments.com](http://ExportComments.com). You can scrape up to 100 comments on a post for free, and there are pricing options for larger data pulls. Prices range from \$11 for three days of use up to \$200 for a monthly business plan for larger scrapes. Only the paid accounts require a sign-​in.

The tool works for Facebook, Twitter, Instagram, YouTube, TikTok and many other social channels. It's easy to use. Just take the link from the top level of the social media post, paste it into the field on the interface and hit Start Export Process. After a minute or two, you'll get an interface for you to download the scrape and export in several formats, including Excel and CSV files. Once the comments are in a spreadsheet, it's easier to sort and filter and look for trends. You also can do a search for specific keywords to see how often they appear in the comments.

Security is always a concern when pulling data from the web. Although the posts are public, you may not want a record of your scrape on the Export Comments site. It offers a "private export" button underneath the list of social channels to increase privacy.

Let's put the tool to the test by pulling the 100 latest comments from a post on the National Rifle Association's official Twitter account. Type this URL into the [ExportComments.com](http://ExportComments.com) search field (or search for another Twitter post and try that; [Figure 3.9](#ch03.xhtml_f3_9)):


[https://twitter.com/NRA/status/1490059049316065281](https://twitter.com/)

Once the URL is in the field, you get several options that let you narrow the export to just followers or those followed by the account you selected. Or you can check the box asking for nested comments.

Hit the Start Export Process button, and wait a couple of minutes for your download interface to appear ([Figure 3.10](#ch03.xhtml_f3_10)):


Now just hit the green download button, and the file will download. The pull-​down menu gives you several export file format options.

Besides extracting comments, the tool also helps you pull hashtagged comments and other data from the social media accounts. Export Comments isn't perfect, but it can be very handy for quick analysis on social media reactions to controversial breaking news stories, such as the Charlottesville protests, George Floyd protests, mask mandates and others.

</aside>

::: section

## Resources for Getting Data

**Freedom of Information (FOI) Resources**

Besides [iFOIA.org](http://iFOIA.org), there are many other free tools and guides available to help you find public records:

SPJ FOIA Guide for Professional Journalists [https://www.spj.org/foi-​guide-​pros.asp](https://www.spj.org/)

SPJ FOI Toolkit [https://www.spj.org/foitoolkit.asp](https://www.spj.org/)

Student Press Law Center Public Records Letter Generator [https://splc.org/lettergenerator/](https://splc.org/)

Journalist's Toolbox Public Records and FOI Resources [https://www.journaliststoolbox.org/category/public-​records/](https://www.journaliststoolbox.org/)

MuckRock FOIA 101 Guides [https://www.muckrock.com/project/foia-​101-​tips-​and-​tricks-​to-​make-​you-​a-​transparency-​master-​234/](https://www.muckrock.com/)

\* \* \*

::: section
## Data Scraping Tools

Here are some other data scraping tools to help with deadline reporting. Most of them are free. Find more data scraping tools in Journalist's Toolbox: [https://www.journaliststoolbox.org/category/data-​scraping/](https://www.journaliststoolbox.org/)

[Import.io](http://Import.io) <https://www.import.io/>

If your data is behind a login, inside an image, or if you need to interact with a website, this paid tool has you covered. Once you enter a web page, you simply point and click on the items of interest, and [Import.io](http://Import.io) will learn to extract them into your dataset. Once extractors are fully trained, they can be set to run on a schedule over multiple different web pages, creating large datasets ready for transformation, analysis and integration into your applications and internal systems.

Scrapy <https://scrapy.org/>

The "Scraping with Code" section of this chapter mentioned Python libraries -- ​essentially add-​ons to the language of Python itself. Scrapy is a fast, open-​source and collaborative library for extracting data from websites.

BeautifulSoup [https://pypi.org/project/beautifulsoup4/](https://pypi.org/)

BeautifulSoup is another Python library for pulling data out of HTML and XML files. It's one of the most popular tools in Python for scraping pages on the web.

Outwit Hub <https://www.outwit.com/>

Outwit is a desktop app that can identify HTML elements on a web page and scrape them. The free version lets you download 100 rows at a time, and it can handle pagination -- ​finding and scraping rows of data on multiple pages.

ParseHub <https://www.parsehub.com/>

A desktop app that can identify and scrape elements and sub-​elements. The free version lets you scrape 200 pages at a time.

CometDocs <https://www.cometdocs.com/>

This tool not only converts PDFs into Excel files but also provides the ability to host documents. It is one of the most consistently accurate conversion tools outside of Adobe Acrobat, which is a paid tool.

Online OCR <https://www.onlineocr.net/>

Good for scraping smaller files.

XML Grid [https://xmlgrid.net/xml2text.html](https://xmlgrid.net/)

Have data buried in an XML file? You can use this CSV file scraper to extract it.

Google Keep <https://keep.google.com/>

Google's note-​taking app lets you export text out of an image. Just click on "Grab Image Text" and pop it into the text of your note. Google Pinpoint ([https://journaliststudio.google.com/pinpoint/about](https://journaliststudio.google.com/)) and MacOS Monterey can also do this with text in images. iOS phone software also can extract small amounts of text from an image by clicking on the yellow lines around the text.

::: section

## Tools Used in This Chapter

Google Sheets <http://sheets.google.com>

Google Dataset Search <https://datasetsearch.research.google.com/>

Google Chrome Data Scraper Plug-​in [http://mnmldave.github.io/scraper/](http://mnmldave.github.io/)

Tabula.technology <https://tabula.technology/>

PDF to Excel <https://www.pdftoexcel.com/>

Folder to download PDFs [https://drive.google.com/drive/folders/17WF-​GhDbbawCfbU-​RsEKGHMuTWs7PpTc](https://drive.google.com/)

\* \* \*

## Footnotes

- Washington DC COVID-19 Testing Sites [https://coronavirus.dc.gov/testing](https://coronavirus.dc.gov/)
- Our World in Data: COVID-19 Vaccinations by Country [https://ourworldindata.org/covid-vaccinations#source-information-country-by-country](https://ourworldindata.org/)
- Pew Research Center: Religious Composition by Country, 2010-2050 [https://www.pewforum.org/2015/04/02/religious-projection-table/](https://www.pewforum.org/)
- Ireland Trolley Ward Watch [https://www.inmo.ie/Trolley_Ward_Watch](https://www.inmo.ie/)
- Association of Food and Drug Officials Directory [https://www.afdo.org/directories/dslo/results/?q=Georgia&unifyfda=1&bystate=1&selected_facets=area_exact:%22100%22](https://www.afdo.org/)
- FDIC Failed Banks List [https://www.fdic.gov/bank/individual/failed/banklist.html](https://www.fdic.gov/)
- National Interagency Wildfire Center Wildfires Data [https://www.nifc.gov/fireInfo/fireInfo_stats_totalFires.htm](https://www.nifc.gov/)


# 4 Cleaning Data

Samantha Sunne

DOI: [10.4324/9781003273301-5](https://doi.org/10.4324/9781003273301-5){aria-label="D.O.I. link to this document."}

In 2016, the movie *Spotlight* won the Academy Award for Best Picture, the highest award in the American film industry. The movie also won praise from journalists for its accurate portrayal of the painstaking process in the *Boston Globe*'s investigation of the Catholic Church child abuse scandal. The *Globe*'s investigative team uncovered evidence by interviewing stakeholders, reviewing public records and compiling data from printed church directories.

In one scene, the team huddles around a phone, asking a researcher for his opinion on its findings. "Does that sound right to you?" the editor asks. "In terms of scale?"

This is an example of data fact-​checking, or as data journalists would have it, "bulletproofing." It's one of the most vital steps to a valid and ethical data analysis for journalism and often includes a subset of data work called "cleaning."

In *Spotlight*, the expert's advice bolsters the team's findings and also provides them with new clues. Data journalists recommend doing these kinds of "data integrity checks" during and after the analysis itself.

Data from government databases, papers and websites is often "dirty," meaning it is unorganized, incorrect, incomplete or contains other flaws that prevent accurate analysis. This chapter addresses tactics for finding those flaws, fixing them and making sure your analysis is ready to produce the best journalism possible.

Many errors will come from your source data, meaning you need to clean it after scraping or importing it. It's most prudent (and in some cases unavoidable) to clean your data at this point, to avoid errors and headaches later.

At the end of this chapter, you will find a list of common errors in spreadsheets and code and likely solutions for them.

:::: section

## How to Find Errors

As with other aspects of data journalism, sometimes the most important part of your task is the old-​fashioned reporting. Data journalists almost always recommend bulletproofing data analysis with a series of interviews, cross-​references and "gut checks."

Pulitzer Prize--​winning data journalist Jaimi Dowdell said that exciting findings, especially, need to be fact-​checked. "If you get an amazing analysis, look first to see if you've made a mistake," she advised as a trainer for Investigative Reporters and Editors.

Sometimes, data cleaning can be quite simple. For instance, with the table of failed banks we scraped in [Chapter 3](#ch03.xhtml_c3), the header row contains some doubled-​up terms, like "CityCity". If there is only a cell where there is a problem, it's easiest to simply click on the cell and type the correct value manually, that is, "City".

A deep dive, like the kind Dowdell specializes in, can involve a long list of checking and cleaning tasks. The Center for Public Integrity, a pioneering news nonprofit, shared the process for its story "Power Trips." In order to investigate tens of thousands of financial documents on congressional staffers, the team:

1.  Scanned paper reports and converted them to PDFs,
2.  Scraped the data from PDFs and imported it to a computer program,
3.  Checked the resulting 30,000 rows of data against source documents,
4.  Standardized alternate spellings and misspellings of names,
5.  Cross-​referenced reports with other documents, like calendars,
6.  Identified and flagged missing information,
7.  Filtered the data for a relevant time span, and
8.  Interviewed congressional staffers on potential ethics violations.

And this was all before doing the data analysis itself.

As you go through your importing and analysis, keep these overarching questions in mind. You don't necessarily need to do each of these checks for every dataset you ever use, but use them to identify the types of problems likely to occur.

1.  **Save the original version.** In a completely separate file, store the dataset exactly as you obtained it from the source. Give this file a name like "raw dataset," and do your analysis on a copy of it.
2.  **Background your data.** Anytime you obtain data from an outside source, you should background it the same way you would an interview subject. Who or what is the source? Is it a primary source, or did they collect it from somewhere else? Could they have a bias or a blind spot that would skew your analysis?
3.  **Find the methodology.** How was the data collected? Was it aggregated from other sources, like the Federal Bureau of Investigation's (FBI) Crime Data Explorer? Was it typed in by hand or scanned from a document? What errors could have occurred in the collection or the aggregation?
4.  **Keep a data diary.** Create a detailed list of all the actions you took when working with the data, including importing, cleaning and filtering. Include the full text of formulas and queries. This can also take the form of saved query files in SQL and documentation in code. We will explore data diaries more in [Chapter 11](#ch11.xhtml_c11).
5.  **Double-​check.** Does the row count in your spreadsheet match the one in the source data? Do a "spot check" -- ​a random sampling of data points to check against the source. If you find problems, you may want to try importing again with a different program.
6.  **Run tests.** Use formulas like SUM() and COUNTA() to check for problems. Make quick data visualizations, or use the MAX() and MIN() formulas to look for outliers. Do your double-​checking in a completely separate program, like a calculator, rather than the same spreadsheet.
7.  **Cross-​reference.** Has anyone else published stories, reports or analyses of the same or similar data? What did they find? Are your findings similar? Can you find the same data from a different source?
8.  **Don't allow for confirmation bias.** Are you interpreting the data in a way that supports your story, or are you being truly neutral? Can someone else in the newsroom, who is unfamiliar with the source or the story, proofread it? If the data doesn't support your theory -- ​or outright disproves it -- ​be honest with your readers.
9.  **Keep your critical thinking hat on.** Does this seem like the correct number of records for such a dataset? For a poll or a scientific paper, how big is the sample? Does the finding fall within the margin of error? (See [Chapter 12](#ch12.xhtml_c12) for more tips on using polling data.)
10. **Find the data dictionary.** A data dictionary, or record layout, is a guide to the field names in a dataset. They are commonly found in very large datasets, like FBI data. This helps especially with field names that are vague or jargony.
11. **Consult human experts**. Sometimes, this is the most important part of your data cleaning to-​do list. You should always check your assumptions and confirm your understanding with the source of the data. Expert sources can also provide insight or confirm your findings. For an especially large or novel analysis, you may want to check your entire methodology. Ask whether there is anything you're missing, or anything else you should look into.

If major problems arise, and you think you can't clean or vet the data enough to write the story ethically, it's best not to use it at all.

<aside class="boxed-text2" epub:type="tip" role="doc-tip">

::: section
### Confounding Variables 

A "confounding variable" isn't a variable that's especially confusing -- ​it's a variable that might affect your findings but isn't visible in the dataset. It's also called a "lurking variable."

Consider a 2018 CBS story about new Starbucks cafes making home values rise. Are home values actually going up because it's easier to get a cup of coffee? Or are there other factors at play?

Remember to keep these possibilities in mind when implying any correlation -- ​or stricter yet, causation -- ​between variables. You can read more on correlation and causation in [Chapter 6](#ch06.xhtml_c6).

</aside>

::: section
## Finding Empty Values

As we will learn in [Chapter 5](#ch05.xhtml_c5), Basic Spreadsheets, a single empty cell can bring down an entire data analysis, making it one of the first errors a data journalist looks for. Blank rows can truncate filters, skew averages or trigger error messages. Some programs will auto-​populate empty cells with the value "0," which has another meaning entirely.

In some contexts, these are called "blank fields" or "null values." There are several methods for finding these. In a spreadsheet program, you can use formulas like ISBLANK() or IFERROR(). Other programs, like SQL Server, use functions like ISNULL(). Microsoft Excel has a special copy-​down command to fill in missing values that are missing but implied. In Google Sheets, you can jump to the last populated row using the keyboard shortcut Ctrl+Down/Cmd+Down.

Another option is Conditional Formatting -- ​formatting cells based on the value inside them. This tool is controlled via point-​and-​click buttons in the formatting menu and can help you find null values as well as outliers and patterns. For a small enough dataset, scrolling through is always an option!

:::: section

## Macros

In [Chapter 3](#ch03.xhtml_c3), Scraping Data, we already accomplished some cleaning when we scraped a table of failed banks. When we copy-​pasted the scraped values into a new tab, the dates were converted into a five-​digit number that looks something like this ([Figure 4.1](#ch04.xhtml_f4_1)):


These are sometimes called "date serial numbers," and they are a valid format for a computer to analyze. It's not so readable for humans, though, so we used the formatting toolbar in Google Sheets to convert it back to a "Month/Date/Year" format. This is an example of data cleaning.

Now, we will automate that formatting using a tool called a "macro." A macro is a recorded action that a spreadsheet program can then run automatically.

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 1 ![](images/Exercise_Icon.jpg) 

We will try creating a macro in our table of failed banks we scraped in [Chapter 3](#ch03.xhtml_c3).

1.  Open the table you created in [Chapter 3](#ch03.xhtml_c3), and navigate to the tab that contains only values. (Earlier, we copy-​pasted these values so that they don't change -- ​Google Sheets executes the scraping function every day, so the first tab is liable to change.)
2.  Highlight cell F2 and click Extensions \> Macros \> Record macro. This will pop open a box with a blinking red light indicating that Google Sheets is recording our actions. Check the radio button for "Use relative references."
3.  Still highlighting cell F2, click Format \> Number \> Date, or a specific date format like "MM-​DD-​YYYY". Click the green Save button. Give your macro a name, like "Format Date".
4.  Highlight the rest of Column F and click Extensions \> Macros \> Format Date. This will format the rest of the cells according to the action we performed in cell F2.

Macros are just one of many ways to clean, rearrange or reformat data. Different methods will work better depending on your data and the problems you are facing ([Figure 4.2](#ch04.xhtml_f4_2)).


</aside>

:::::: section
## Regular Expressions

We will continue experimenting with cleaning by using a technique called Regular Expressions. Regular Expressions, or RegEx, is a syntax that can be used to identify patterns of text and numbers in spreadsheets. It also works in programming languages like Python and R.

Just like with programming and functions in general, it's best not to try to memorize all of the syntax in Regular Expressions ([Table 4.1](#ch04.xhtml_t4_1)). Instead, use support sites and instructions like the one in Google Sheets to guide your RegEx creations.

+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \\w                               | A lowercase "w" in RegEx stands for "word character," that is, characters that are not punctuation. Underscores (\_) are counted as word characters, but other punctuation marks are not.                                                        |
|                                   |                                                                                                                                                                                                                                                  |
|                                   | The "w" command can help with removing extraneous punctuation marks, like "\[" and "\<", that sometimes come with data scraped from the web. It is helpful because it can return both numbers and letters.                                       |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \\d                               | A lowercase "d" stands for "digit" and can be useful when extracting only numbers from a line of text. For example, extracting street numbers from a list of addresses.                                                                          |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \\                                | A backslash (\\) indicates that you are using RegEx to find matching patterns, not search for the text itself. Using just "w" in the RegExExtract() formula would return only the letter "w", but "\\w" would return any alphanumeric character. |
|                                   |                                                                                                                                                                                                                                                  |
|                                   | If listed before a punctuation mark, a backslash functions as an "escape." This means adding a backslash before a character like a period ("\\.") indicates you want to look for an actual period, not use it as a wildcard (see below).         |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| .                                 | A period (.) is a wildcard, meaning it will match any character. This can be useful if you don't know which characters are going to occur in between the ones you want, such as phone numbers that include parentheses and ones that don't.      |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[1--​5\]                          | Instead of the letter "d", you can specify a list of numbers you are looking for, like 1 through 5. The phrase "\[0--​9\]" would return any numeric character.                                                                                    |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[a--​z\]                          | The same is true for letters. "\[c--​t\]" will return the first character that matches a letter between those letters, or you can use "\[a--​z\]" to mean any letter in the alphabet.                                                              |
|                                   |                                                                                                                                                                                                                                                  |
|                                   | RegEx is case sensitive, so "\[a--​z\]" will return lowercase letters, while "\[A--​Z\]" will return uppercase.                                                                                                                                    |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \+                                | A plus sign (+) indicates you want to extract all characters identified in your command. Searching for "\\w" would return the first alphanumeric character, but "\\w+" returns the first as well as all of the ones that come after it.          |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: *[Table 4.1*](#ch04.xhtml_t4_1b) Useful RegEx Phrases

\* \* \*

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 2 

For this method, we will use a dataset of Coronavirus vaccines available in 2021 (shortlink: [https://bit.ly/vaccinetable](https://bit.ly/)). The data comes from Our World in Data, a website run by a research team at Oxford University.

Because this data was also scraped from the web, the sheet contains some extraneous characters and mismatched data formats. First, we will remove the asterisks in Column A using RegEx.

1.  Make a copy of the vaccine table (shortlink: [https://bit.ly/vaccinetable](https://bit.ly/)).

2.  Give Column E the name "RegEx".

3.  In cell E2, type the following formula and press enter.

    1.  =REGEXEXTRACT(A2, "\\w+")

4.  Copy the formula down to apply to the rest of your data.

</aside>
<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Pro Tip ![](images/Pro_Tip_Icon.jpg) 

Keyboard shortcuts are just one way to "copy down" your formula to apply to other rows. Another method is to hover over the bottom-​right corner of the function cell until the cursor becomes a thin black plus sign. (The cursor's appearance may vary by program.)

Click and drag the plus sign down to the bottom row of your data. For spreadsheets containing many rows, this is not efficient, but it can be convenient if you have only a few rows.

</aside>

This is a very simple Regular Expressions syntax that returns only alphanumeric characters. The formula REGEXEXTRACT() in Google Sheets returns characters that match the queries you are writing in RegEx ([Figure 4.3](#ch04.xhtml_f4_3)). We will learn more about functions in [Chapter 5](#ch05.xhtml_c5).


::::: section

## Spreadsheet Formulas

REGEXEXTRACT() is just one of the many, many formulas in Google Sheets that can help you with your data cleaning. We're going to experiment with another one called SPLIT() that separates parts of a cell's value based on a delimiter. A "delimiter" is the character that defines where the columns begin and end.

In the case of our vaccine table, we can see that Our World in Data used commas to separate the list of available vaccines in each country. So our SPLIT() formula should look something like this:

=SPLIT(D2, \", \")

The SPLIT() formula has two parameters: the cell to split and the delimiter. If you recall from [Chapter 3](#ch03.xhtml_c3), a "parameter" is a variable inside a formula that tells a formula what to do. You need to wrap the comma in quotes so that the program knows it is a piece of text to search for ([Figure 4.4](#ch04.xhtml_f4_4)).


<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 3 

1.  Give Column F the name "Vaccine 1".

2.  In cell F2, type the following formula and press enter.

    =SPLIT(D2,\", \")

3.  This should populate Row 2 of Column F, and additional columns, with the vaccines listed in cell D2.

4.  Rename Columns G, H and I with the titles "Vaccine 2", "Vaccine 3" and "Vaccine 4".

5.  Copy your formula down to the rest of the rows in Column F.

The SPLIT() formula creates a new column for every vaccine in the list.

</aside>
<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Pro Tip 

Most Google Sheets formulas only populate the columns they are located in. SPLIT() populates additional columns to the right, which can be very powerful, but also dangerous, as it could overwrite data located to the right. You could also run into an error message refusing to overwrite existing data.

If your cell contains more than four or five values to split up, it's best to use a different cleaning method. Using SPLIT() to populate dozens of columns will make your spreadsheet harder to use, not easier. At that point, a journalist would likely split values into rows, not columns.

</aside>

Make sure you understand which delimiter the source data is using, because that can have enormous effects on the integrity of your data.

For instance, we can also see Our World in Data used slashes (/) to indicate multiple names for the same vaccine. In other datasets, the slash could be the delimiter. Pipes (\|), semicolons (;) and tabs are other common delimiters you may come across.

::: section
## Text Editors

Many programs have Find and Replace functions, but with very large datasets, it can be easier to use a text editor like Microsoft Word, Sublime Text, TextEdit or many other free programs.

They can be an especially good option for finding small bits of text that occur very often in your dataset. This could be double spaces that should be single or semicolons that should be commas.

Text editors usually navigate data by "strings" -- ​bits of grouped text. Because strings can contain numbers, letters, punctuation and spaces, all of which are counted as characters, try to think in terms of "strings" rather than words, phrases or other terms that we would use verbally.

For example, "AstraZeneca " and "AstraZeneca" are both text strings, but the first is one character longer. Unlike humans, many text editors and data programs will consider them to be two separate values.

In addition, many text editors (and some spreadsheet programs) use different font colors to help the user distinguish bits of text and code. For example, in Google Sheets, formula names are shown in green and parameter values in black.

:::: section

## OpenRefine

As a reporter, you will often come across columns of names, dates, places and people. This creates many possibilities for misspellings, alternate spellings, abbreviations and acronyms.

As we have learned, a data analysis program will usually read "Barack Obama", "B. Obama" and "President Barack Obama" as completely different entities, even though we know they are the same person.

In addition, human-​entered or human-​edited data is especially prone to incorrect or inconsistent entries. Christopher Groskopf, the author of the "Quartz Guide to Bad Data," once encountered a dataset with more than 250 different spellings of the word "Chihuahua."

Programs like OpenRefine are designed to combat this very problem. OpenRefine uses a collection of linguistic analysis techniques to identify and "cluster" rows containing similar values or ones that OpenRefine thinks are related, like "Central Intelligence Agency" and "CIA." You can then batch edit these values or rename them.

Let's try this out by cleaning this dataset of people who donated to Obama's run for the US House of Representatives in 2000 (shortlink: [https://bit.ly/obama2000](https://bit.ly/)).

When opening this dataset, you will find that it is a comma-​separated values (CSV) file containing 571 rows. It contains the names and addresses of donors, as well as how much they donated, and some additional data recorded by the Federal Election Commission (FEC).

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 4 

1.  Download the Obama donors dataset to your computer (shortlink: [https://bit.ly/obama2000](https://bit.ly/)).
2.  Download the free OpenRefine desktop app from [OpenRefine.org](http://OpenRefine.org). Launch the app, which will open as a new tab in your web browser.
3.  Import the obama2000.csv dataset by uploading it from your computer and clicking Next. In the import wizard, make sure the comma is selected as the delimiter. To finish importing, click "Create Project."

<!-- -->

5.  Scrolling over to the "contributor_city" column, it appears that "Chicago" is misspelled in one of the first rows.
6.  We will create a "text facet" to see if any other cities are misspelled, and rename them. Open the drop-​down menu in the "contributor_city" column, and choose Facet \> Text facet. This will create a pop-​up panel showing the various cities and the number of rows they occur in ([Figure 4.5](#ch04.xhtml_f4_5)).
7.  Click "Cluster" in the panel to open a new pop-​up window where you can batch edit the city names. In the top-​left corner, change "key collision" to "nearest neighbor."
8.  Type "Chicago" into the boxes for New Cell Value.
9.  In the "Merge?" column, check the boxes for the five spellings of Chicago, and click Merge Selected & Close. The cities should now be renamed to consistent spellings ([Figure 4.6](#ch04.xhtml_f4_6)).

There are also multiple spellings of Glen Ellyn and Cambridge. With these, you should do some external research to figure out which is the correct spelling.

This is just one tool that is possible with OpenRefine, and one small step in verifying and cleaning this dataset, but batch editing values in this way can save you a lot of time.

</aside>

:::: section
## Troubleshooting Common Spreadsheet Errors

Below is a list of common errors and popular solutions for them. Remember there are many potential solutions, varying by program and project aim, and you may need to do some digging of your own.

+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Leading Zeros                     | Leading zeros are common in text values that are read as numerals. For instance, the ZIP code for Jersey City, New Jersey, is "07097." Some programs would read that as the number 7,097, which is incorrect.                                                                                                                                              |
|                                   |                                                                                                                                                                                                                                                                                                                                                            |
|                                   | You can avoid this problem by designating a text format while importing or wrapping the values in quotes to indicate they are text strings.                                                                                                                                                                                                                |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Spaces                            | On the flip side, some imported values will contain extra characters you don't want -- ​like trailing spaces at the end of a text string. Remember that a computer counts every character in a text string, meaning they can affect your functions and outputs.                                                                                             |
|                                   |                                                                                                                                                                                                                                                                                                                                                            |
|                                   | One way to remove leading or trailing spaces is the TRIM() function. However, this will not delete white space characters in the middle of text, like a double space.                                                                                                                                                                                      |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Duplicate Rows                    | Some datasets will have duplicate rows -- ​specifically, rows that are identical in every column. It can take some digging to find out why the duplicate exists. It's possible that it is a valid record that should be included in the analysis, or perhaps it should be removed.                                                                          |
|                                   |                                                                                                                                                                                                                                                                                                                                                            |
|                                   | Duplicates can be hidden with filters or removed with tools like OpenRefine. Google Sheets also has a data cleaning feature that removes duplicate rows based on matching columns.                                                                                                                                                                         |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Incorrect Formats                 | As we discussed in [Chapter 3](#ch03.xhtml_c3), importing data can be one of the toughest parts of a data project, as the process can be prone to errors. For example, "5556934563" could be a phone number, a unique identifier or an amount over 5 billion. Each of these data types will be interpreted differently in analysis.                        |
|                                   |                                                                                                                                                                                                                                                                                                                                                            |
|                                   | Many spreadsheet and database programs will have import processes that let you specify the data format before completing the import. You can also change the format after the fact using the formatting toolbar in a spreadsheet program or queries in a tool like SQL.                                                                                    |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Incorrect Range                   | Double-​check the ranges in your formula bar, conditional formatting and filters to make sure they contain all the data you need. If the filter doesn't contain the whole dataset, rows will be separated from their data in other columns.                                                                                                                 |
|                                   |                                                                                                                                                                                                                                                                                                                                                            |
|                                   | This is another reason empty rows or cells can trip up your analysis -- ​often programs will stop a filter or a formula when it reaches the first empty row.                                                                                                                                                                                                |
|                                   |                                                                                                                                                                                                                                                                                                                                                            |
|                                   | In Google Sheets, cells are in a filter when they have a thin green line around them. When in doubt, you should always be able to open a pop-​up interface to control your filter and specify the range there.                                                                                                                                              |
|                                   |                                                                                                                                                                                                                                                                                                                                                            |
|                                   | To select all the data in your spreadsheet, click on a populated cell and select all (Ctrl+A or Cmd+A). To highlight every single cell in the sheet, not just the ones that contain data, click on an empty cell and select all from there.                                                                                                                |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Delimiters                        | A CSV is a "comma-​separated values" file, meaning the data columns are separated by a comma. Another common format is TSV, for "tab-​separated values."                                                                                                                                                                                                     |
|                                   |                                                                                                                                                                                                                                                                                                                                                            |
|                                   | But delimiters -- ​also called "separators" -- ​can technically be any character. Additionally, CSVs can contain data where a comma is *not* a delimiter -- ​like in the value "4,392."                                                                                                                                                                       |
|                                   |                                                                                                                                                                                                                                                                                                                                                            |
|                                   | Most programs will be adept at interpreting these values, but occasionally, you will see an unusual separator, like a pipe (\|). Watch out for these options in import wizards.                                                                                                                                                                            |
|                                   |                                                                                                                                                                                                                                                                                                                                                            |
|                                   | If the delimiter also occurs within values, you can format that column in a formatting toolbar or wrap it in quotes.                                                                                                                                                                                                                                       |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Rounded Digits                    | In a spreadsheet program, you can often make decimal points visible or invisible using the formatting bar. This doesn't affect the value itself -- ​just how it is presented to you.                                                                                                                                                                        |
|                                   |                                                                                                                                                                                                                                                                                                                                                            |
|                                   | In a few cases, it may be that one program actually *converted* a value into one with fewer digits -- ​that is, rounded it up or down. For example, Facebook shows the number of comments on a post as "3.4K" rather than 3,454. This can affect your final analysis, so it's best to watch for these rounded numbers while still in the acquisition phase. |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| International Punctuation         | This textbook uses American English for spreadsheet formulas and other inputs. Some keyboards and programs will use different syntax according to their native language. For example, in Germany, Google Sheets uses a semicolon (;) rather than a colon (,) to separate parameters.                                                                       |
|                                   |                                                                                                                                                                                                                                                                                                                                                            |
|                                   | If you use a computer or a keyboard that is not English, consider looking up the specific syntax and punctuation for your language and region.                                                                                                                                                                                                             |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

:::: section

## Troubleshooting Common Programming Errors

Error messages are unfortunately common in both spreadsheets and programming, as we will discover in [Chapter 9](#ch09.xhtml_c9). Many programs will helpfully list the line number where your error occurs, which can at least help you narrow down the potential culprits.

Researching your own solutions to programming problems is going to be vital. Search engines like Google and forums like StackOverflow will be an essential resource. In her book *Mining Social Media: Finding Stories in Internet Data*, data journalist Lam Thuy Vo claims that researching errors is an integral part of becoming a programmer.

"One day we might have to analyze text-​based reactions, and another day we might be looking at thousands of images," she wrote. "To be a good coder, in other words, means that you have to be a *resourceful* coder, one who knows how to look for and ask for help solving any problems you encounter."

This is a list of some of the most common road bumps, which often come down to a simple letter or punctuation mark. You will be surprised at how often the most intimidating of errors are solved by the simplest of solutions!

+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Missing or Incorrect Characters        | Perhaps the most common error of all is a wrong or missing character. For instance, an XPath might use square brackets (\[\]) to offset an identifying class, not parentheses, as one might assume.                                                                                                            |
|                                        |                                                                                                                                                                                                                                                                                                                |
|                                        | Read carefully through both your error message (if you have one) and your code to see if you can find the missing piece. If not, a search engine is the easiest way to narrow it down.                                                                                                                         |
+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Language Variation                     | Each programming language (and other tools like SQL and RegEx) uses its own syntax. The syntax is the series of words, punctuation and "grammar" that rules the language.                                                                                                                                      |
|                                        |                                                                                                                                                                                                                                                                                                                |
|                                        | For example, RegEx is case sensitive, meaning it considers "A" and "a" to be two different values, but others wouldn't. Some programs allow spaces between parameters in a function, and others don't.                                                                                                         |
|                                        |                                                                                                                                                                                                                                                                                                                |
|                                        | Overall, it is best to be consistent. If you use capitalization for a value in the beginning, continue using that format throughout.                                                                                                                                                                           |
+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Copy and Paste                         | We don't recommend copy-​pasting formulas from a website or an ebook. Some programs fail to correctly interpret fonts and characters pasted from other programs. Quotes are the usual culprit.                                                                                                                  |
|                                        |                                                                                                                                                                                                                                                                                                                |
|                                        | The best practice is to always type in formulas and values by hand.                                                                                                                                                                                                                                            |
+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Quotes                                 | A common road bump is that some programs use single quotes (') and others use double ("). Some use both.                                                                                                                                                                                                       |
|                                        |                                                                                                                                                                                                                                                                                                                |
|                                        | If any of your functions are not running, an easy first troubleshooting step is to delete all the quotes and retype them in manually. If that doesn't work, manually replace single quotes with double quotes, or vice versa.                                                                                  |
+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parentheses                            | Parentheses and other characters that are used to offset parts of code, like brackets ({}), can get confusing, especially when working with nested functions.                                                                                                                                                  |
|                                        |                                                                                                                                                                                                                                                                                                                |
|                                        | Carefully check each parenthesis to see if it is paired with a beginning or an ending parenthesis. If you have too many on one side, the function will not work.                                                                                                                                               |
|                                        |                                                                                                                                                                                                                                                                                                                |
|                                        | Programs like Google Sheets and text editors like Sublime Text will also help by highlighting matching parentheses or making them a different color.                                                                                                                                                           |
+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Changed Source Code                    | When your script is communicating with another program, like a scraper or an API, it is dependent on that other code. For example, if a website uses the tag \<h1\> to enhance text, but later changes it to \<h2\>, a scraper will suddenly find no values matching the \<h1\> tag.                           |
|                                        |                                                                                                                                                                                                                                                                                                                |
|                                        | If your scraper stops working entirely, you may need to look at the source to see if anything has changed.                                                                                                                                                                                                     |
+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Conflicting Language Versions          | In [Chapter 9](#ch09.xhtml_c9), we will talk about downloading, installing and updating versions of programming languages. Because they need to be downloaded and installed, your languages could be out of date, or you could need a certain version in order to use a certain library.                       |
|                                        |                                                                                                                                                                                                                                                                                                                |
|                                        | Your error message will likely show something along these lines. If the message refers to a version, it's best to search for that message in a search engine, whether or not you think you have that version installed. The version you have or want could be in a different file path or virtual environment. |
+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Install Failures                       | Installing languages can be tough, but libraries even tougher. Libraries that were made by individuals, rather than published by an official company, might require some extra steps.                                                                                                                          |
|                                        |                                                                                                                                                                                                                                                                                                                |
|                                        | Use the library's website, Github page or search engine results to find the extra steps you need to successfully install the package.                                                                                                                                                                          |
+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Conflicting File Paths and Directories | The file path of your programming language, script files and source data all matter. The computer will look for libraries and files in the directory you specify or the one you are currently in. If it cannot find a file that it needs to run a script, like a dependency, it won't run.                     |
|                                        |                                                                                                                                                                                                                                                                                                                |
|                                        | Use the Command Line to find the location of your files and notebooks. One trick to identify a file path is to simply drag and drop a file into the CLI from the computer's file interface, like the MacOS Finder or Windows File Explorer.                                                                    |
+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Messy Source Data                      | Source data is often unlabeled or labeled in a way that isn't helpful for our purposes. To tackle this, you will have to get creative in how you identify, export and import the data. It might also mean doing additional manual identification, like inserting tags in a text editor, after exporting it.    |
+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Reference Error                        | This is a common error that typically means you are calling a variable without defining it first. If you ever get an error message containing "ref" or "reference," it's likely that you need to define the variable before your script can move on.                                                           |
|                                        |                                                                                                                                                                                                                                                                                                                |
|                                        | When writing code, you will often find yourself having to define things you thought were implied. Remember, when writing a brand-​new script, it doesn't know that an apple is a fruit, or even that it's an object. It just knows that "apple" is a five-​character text string.                                |
|                                        |                                                                                                                                                                                                                                                                                                                |
|                                        | Computers also read scripts vertically, in almost all cases. This means the variable needs to be defined above the line where the error occurs. Search with Ctrl+F or Cmd+F for the variable to find where it should have been defined.                                                                        |
+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

## Footnotes

- Bulletproofing Your Stories [https://slideplayer.com/slide/1452564/](https://slideplayer.com/)
- Power Trips Archives [https://publicintegrity.org/topics/politics/congress/power-trips/](https://publicintegrity.org/)
- This Is How Much a Starbucks Adds to the Price of a Nearby Home [https://web.archive.org/web/20210614022911/https://www.cbsnews.com/news/starbucks-makes-property-values-jump-study-shows/](https://web.archive.org/)
- Coronavirus (COVID-19) Vaccinations [https://ourworldindata.org/covid-vaccinations](https://ourworldindata.org/)
- Regex cookbook -- Top 10 Most wanted regex [https://web.archive.org/web/20210723025002/](https://web.archive.org/) [https://medium.com/factory-mind/regex-cookbook-most-wanted-regex-aa721558c3c1](https://medium.com/)
- REGEXEXTRACT [https://support.google.com/docs/answer/3098244?hl=en](https://support.google.com/)
- Quartz Guide to Bad Data [https://qz.com/572338/the-quartz-guide-to-bad-data/](https://qz.com/)
- OpenRefine <https://openrefine.org/>
- Obama Donors Dataset [https://drive.google.com/file/d/1f4Pa3gftUQE4bs8gpqrbhp1JsV-E3hTx/view?usp=sharing](https://drive.google.com/)
- Obama Donors Shortlink [https://bit.ly/obama2000](https://bit.ly/)
- StackOverflow <https://stackoverflow.com/>
- Mining Social Media: Finding Stories in Internet Data <http://socialdata.site/>


# 5 Basic Spreadsheets

Mike Reilley

DOI: [10.4324/9781003273301-6](https://doi.org/10.4324/9781003273301-6){aria-label="D.O.I. link to this document."}

A bridge collapse in Genoa, Italy, in the summer of 2018 left 43 people dead and the media around the world scrambling for localized story angles about crumbling infrastructure in their country. They need to look no further than a couple of spreadsheets.

In the US, MSNBC aired a story shortly after the collapse that was based on a recent study of US bridge inspections from the American Road & Transportation Builders Association (ARTBA).

The story touched on the study's highlights: 54,259 US bridges were "structurally deficient," and the bridges in the study were on average 67 years old. The article also revealed which states had the most and fewest structurally deficient bridges.

But that piece only scratched the surface about the condition of the nation's bridges. It was based on only one study and cited just a few statistics. That may be fine for a short national cable TV report, but closer examination using basic data analysis would yield more meaningful information -- ​and potential story ideas -- ​particularly for local news outlets.

For that, you need a spreadsheet. Microsoft Excel or Google Sheets works best, unless you're among the Mac-​loving loyalists to Apple's Numbers software. Downloading or scraping data from a website and then sorting, filtering and analyzing that information is one of the foundational blocks of data journalism.

Spreadsheets seem imposing to many journalists. Many of us became writers to avoid math courses in high school and college, right? But even the simplest spreadsheet skills can produce newsworthy results and drive your reporting in new ways.

This chapter focuses on how to download and analyze a spreadsheet to find data points for news stories.

\* \* \*

<aside class="boxed-text2" epub:type="tip" role="doc-tip">


</aside>
<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section

## Exercise 1 

**Getting Started: Loading Data into a Spreadsheet**

Every year, the US Federal Highway Administration posts data about bridge inspections. The National Bridge Inventory database rates bridges as being in Good, Fair or Poor condition. By sorting and filtering the data in a spreadsheet, you can determine which states have the most bridges and highest percentage of bridges in each category. You also can create a new category -- ​Fair-​Poor -- ​to group the subpar bridges together.

We'll show you how to do this using the 2019 NBI data. But later, you can apply these skills to the data for the most recent year.

We're using Google Sheets for this exercise, but if you prefer Excel, you can follow the same steps, though the tools you'll use are named a little differently. You'll develop a preference over time.

1.  Download the NBI dataset from here: [https://bit.ly/ch5spreadsheet](https://bit.ly/). Use the arrow or three vertical dots in the upper-​right-​hand corner to download it to your computer, and then drag and drop that file into a Google Drive folder.

    Or you can use the "Open With" pull-​down menu at the top of the page, select Google Sheets and then go to the File menu and select "Make a Copy."

    **Pro tip:** To move around quickly on a large dataset, hold down the CMD (Apple) key and use the directional arrows to move up-​down and side-​to-​side. On a PC, hold down the Control key and use the arrows.

2.  Develop the habit of always working with a copy of the original data. By clicking on the tab of this worksheet, you can duplicate it. You might do this repeatedly during your analysis, naming each sheet whenever you make a significant change to the data. That way, you will have an audit trail of your work.

3.  The first row of any dataset you work with should be labels of what each column of data represents ([Figure 5.1](#ch05.xhtml_f5_1)). It should never start with just the data. In this case, there are two series of labels: Bridge Counts and Bridge Area (in meters). For this exercise, we'll focus on the Bridge Counts. Lock your column headings in place so that as you scroll down, you can always see what each column means. In Google Sheets, you do this by going to View \> Freeze \> 1 row.


4.  Do a slow scroll through your dataset and make sure the set is complete and there are no empty or garbled cells. Data entry with some government entities can be spotty. Make sure your set passes initial inspection before starting any analysis. If data is missing or garbled, contact the public information officer for that government agency to get the issue cleared up.

</aside>

:::: section
## Interviewing Your Dataset

ProPublica's Derek Willis builds incredible data visualizations and databases on all kinds of social and economic issues. He knows his way around a spreadsheet, so when he talks about them, you listen closely. Willis uses a popular approach to spreadsheet analysis: He interviews data the same way he would a person.

"Interviewing is a skill. I've heard this repeatedly as a college student, at journalism conferences and in newsrooms," Willis wrote in a July 2014 *MediaShift* article. "Not all of us are born with the ability to form penetrating questions or to extract crucial details from sources. Like any skill, interviewing takes practice and preparation."

Willis argues that

> journalists who wouldn't consider themselves "data journalists" already have the necessary foundation for asking good questions of data. Just as you would background a person you were interviewing for a story, data has its own history. Interviewing data takes some practice, but the benefits for journalists are plentiful. You'll learn how to find the holes in data (and there are always holes), how to avoid misinterpretations and how to find better stories.

<aside class="boxed-text2" epub:type="tip" role="doc-tip">

For more data journalism tips, tricks and exercises, visit the Data + Journalism blog at <http://dataplusjournalism.com>

</aside>

Think about it: Our first week in journalism school, we were taught to ask these basic questions when interviewing for a news story:

- Who?
- What?
- When?
- Where?
- Why?
- How/how much?

So what if you were writing a story about a city budget? You might ask the city manager, the mayor or the city treasurer questions like:

- How much did the budget increase?
- Who got the biggest raise? Whose pay was cut?
- Why was the police budget cut? How much?
- Where is the increased funding for schools coming from? (Hint: Bet your property taxes went up!)

The same questions apply when sorting and filtering your data. Look over the header labels, and start asking yourself some questions:

- How many bridges in my state were in good condition? That's easy, just look in the corresponding cell.
- What percentage of bridges in my state were in poor condition? You'll need to use a spreadsheet formula (gasp!) to calculate that. Don't worry, we'll show you how.
- What percentage of bridges in my state were in fair-​poor condition? We'll need to add cells together and divide by the total number of bridges in my state.
- And finally, where did my state rank among all states in poor bridges? Fair? Fair-​poor?
- Who had the most poor bridges? Who had the least?

Once you start this analysis, you'll develop a list of data points that will help guide your story. When I teach this approach to students, I have them type the data points into a Google Doc as they do the analysis so they won't forget them. In the end, they have a list of data and an outline for a great story in the process.

This interview approach works well for datasets of all sizes. It's particularly helpful in teaching college students or professional students who might feel overwhelmed by even a smaller dataset. At the very least, it's an excellent way to think through a complex sheet of data in a way we can all grasp as journalists.

Sunne applied the interviewing data approach to a KBIA story about federal inspections and violations at an animal sanctuary in Columbia, Missouri. (shortlink: [https://bit.ly/sunnestory](https://bit.ly/)) She found a downloadable USDA database of animal welfare checks and simply filtered the welfare checks for Missouri.

"I had just graduated from the University of Missouri, and sorted them in order of who had the most violations," she said.

> Lo and behold, the dirtiest and most dangerous exotic animal location in the state was right there in my college town, a couple miles south of the mall. So that was a pretty easy, obvious story that I ended up producing for the NPR station there.

<aside class="boxed-text2" epub:type="tip" role="doc-tip">

::: section
### Exercise Quick Challenge: Calculation Percentage 

According to the ARTBA bridge inspections study, 54,259 of 612,677 US bridges are rated "structurally deficient." How would we figure that as a percentage for our readers? And how would we write it?

**Answer:** Divide 54,259 by 612,667 to get 8.8 percent. This can easily be done on your phone calculator app. We'll show you how to do it on a spreadsheet later in this exercise.

</aside>

::: section

## Analyzing Bridge Inspections: Calculate Percentages in Google Sheets

Once your data is in the Google Sheet, use these steps to calculate the percentage of fair bridges, poor bridges and fair-​poor bridges for each state. Let the spreadsheet do the heavy lifting for you by using the formulas below to calculate the percentages.

Think of your spreadsheet like the grid on the game Battleship you played as a kid: Cell J2 contains some data. Is it a hit or a miss? How do I use it? Same with cell K20, C13, etc.

Now you're ready to do some analysis.

1.  Row 1 should be the labels of each column. Every row below that should contain state data, starting with Alabama.

2.  Now go to cell J1, and type the words Percentage Fair. In cell K1, add the words Percentage Poor. And in cell L1, type the words Percentage Fair-​Poor.

3.  In column J, in the Alabama row: Figure the percentage of fair bridges by pasting this formula into cell J2: =D2/B2

    \* While you have cell J2 highlighted, hit CMD-​C (Control-C on a PC) to copy it and then drag the cursor to the bottom of the J row, so all of the column is highlighted. Then hit the Paste button (CMD-V on Mac, CTRL-​C on PC) and voila! It will calculate all of the percentages for each state/row.

    **Troubleshooting:** If the column doesn't calculate properly, just hit CMD-​Z (Mac) or CTRL-​Z (PC) to back out of the calculations and repeat the steps. It should work after a couple of attempts.

4.  With the J column highlighted, click the decrease decimal point button a few times to move the decimal point over a few places on the data so it's down to three decimals. (See [Figure 5.2](#ch05.xhtml_f5_2). The hand is over the button, two to the left of the \$ button.)


    **Pro Tips**

    1.  You can skip the decimal step by hitting the percentage sign button (%) to convert the decimals into a percentage, and it automatically rounds off the decimals for you. You'll need to repeat these steps for every column of data.
    2.  Another way to convert to percentages: Click on the J column at the top to highlight the whole column, then right click (Control+Click on Mac) to get the pull-​down menu and select Format Cells. On the next interface, select Percentages. It will convert the decimals into a percentage with two decimal points.

5.  In column K, in the Alabama row: Figure the percentage of poor bridges by pasting this formula into cell K2: =E2/B2

    \* Then copy that formula and select all of column K and hit paste. It will calculate all of the percentages for each state/row.

6.  In column L, in the Alabama row: Figure the percentage of fair/poor bridges by pasting this formula into cell L2: =(D2+E2)/B2

    In essence, you're adding the fair and poor columns together and dividing by the total number of bridges.

    \* Then copy that formula down column L.

7.  Before sorting we're going to insert what is called a "data moat" between the totals at the bottom of the sheet and all of the states and districts. Just click on the Totals row, go to the Insert button at the top menu and select Insert/Rows/Insert Row Above.

8.  Now we're going to sort by column L and order them from highest to lowest percentage. Now drag your cursor from cell A1 across the data you want to sort, excluding, of course, the Totals row (see [Figure 5.3](#ch05.xhtml_f5_3)).


9.  Now go to the Data pull-​down at the top of the menu and select Sort Range, and then select Advanced range sorting options (see [Figure 5.4](#ch05.xhtml_f5_4)).


10. In the Sort menu, make sure to check the Data Has Header Row box and change the column pull-​down menu to Percentage Fair (column L) and the order Z to A, and then hit the Sort button (see [Figure 5.5](#ch05.xhtml_f5_5)).

11. Now your sheet is sorted by state/Puerto Rico (be mindful of totals in row 34) in order of highest to lowest Fair-​Poor condition bridges. Now you're ready to answer the questions below in the Challenge section.

You can also repeat these sorting steps for columns J (Percentage Fair) and K (Percentage Poor) to see where your state ranks in those categories.

Be sure to write your data findings out in a Google Doc as you sort. Your story will begin to write itself.

::: section
## Exercise Challenge: Answer These Questions

1.  Which three states had the most fair/poor bridges by percentage? (Be mindful that Guam, Puerto Rico and the US Virgin Islands are not states.)
2.  Which three states had the least?
3.  Where does Illinois rank among all states with fair/poor bridges? (Be mindful that Row 34 is a Totals column and you have a header in row 1, as well as nonstates in the list.)
4.  Where does your state rank on the list? Be sure to save these answers as you'll use them to write a short story for an exercise in [Chapter 7](#ch07.xhtml_c7), Writing a Data Story.

::: section

## Answers

1.  Most: Rhode Island, District of Columbia and West Virginia. (Listing Puerto Rico is fine, but it's not a state.)

2.  Least: Florida, California and Mississippi

3.  th. It's 37th in the sheet, but take into account the header row, Puerto Rico, which is not a state, and that Totals appear in row 34.

    **Pro tip:** To avoid the Totals row appearing in the sort, insert a blank row between Wyoming and Totals before sorting. This is called a "data moat," much like a moat around a castle. It's designed to keep totals away from other rows of data in budgets and other datasets. Also make sure to select just the data you want to sort above the moat, or the totals will get mixed into the list.

:::: section
## On Your Own: Analyze Bridges by Area

You can repeat these percentage formulas and sort for the columns showing the Bridge Area data -- ​the length of the bridges in each state. This can yield some interesting and different results.

For example, Iowa is bordered by two very large bridges over the Missouri and Mississippi Rivers that are considerably larger than the Sutliff Bridge over the tiny Cedar River. California also has many large, expansive bridges.

Compiling the percentages of poor or fair bridges by area will produce different results from states that have a large number of poor bridges that are smaller in area. Try it on your own, and compare the results. It will give the reader a more complete picture of the issue.


<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Pro Tip ![](images/Pro_Tip_Icon.jpg) 

If you need to create a new Google Sheet from scratch, simply type Sheets.new into a browser window. Name the new sheet in the upper-​left corner, and then go to File/Move to and save it to a specific folder in your Google Drive.

</aside>

::: section

## Filters and Datasets

In the fall of 2020, the Big Ten Conference made a controversial decision to start the football season more than a month later than most Power Five conferences. The conference based its decision on research about COVID-​19 possibly causing heart disease in players. The decision was lambasted by the media and drew outrage from athletic officials, coaches, players and fans.

The plan backfired. The Big Ten started the season later, right as COVID-​19 cases began to spike. Several games were canceled as players and coaches got sick. But just how bad was COVID-​19 on the Big Ten campuses?

As the season drew to a close, Chris Katsaros and Charles Tharpe, two reporters for [RedLineProject.org](http://RedLineProject.org) based in Chicago, examined the number of cases on each campus. They used filters and basic mathematical formulas to determine which campuses had the most cases and which had the most per 1,000 students. The latter data point was important as the Big Ten has a wide range of student enrollment: Ohio State has more than 61,000 students, while Northwestern has just over 22,000. Enrollment obviously impacted the chances for an outbreak and had to be factored into the equation.

They did it by loading this spreadsheet into Google Sheets: [http://bit.ly/bigtencovid19](http://bit.ly/). The dataset has three tabs at the bottom:

1.  Big Ten Daily COVID-​19 cases, which we'll use for filtering exercises.
2.  Big Ten COVID-​19 cases per 1,000 students, which we'll use for math calculations.
3.  The answer key for the cases per 1,000 students.

<aside class="boxed-text2" epub:type="tip" role="doc-tip">


</aside>

::: section
## Getting Started

Once you have downloaded the spreadsheet and opened it in Google Drive, click on the Big Ten Daily COVID-​19 cases in the bottom-​left tab and inspect the data (see [Figure 5.6](#ch05.xhtml_f5_6)). Use the CMD (CTRL on PC) arrow up/down keys to move from the top to the bottom of the dataset, and do a slow scroll through some of the sections to see data for the various schools. Note that Column F is a running total for positive cases, not positive tests per day.


The daily data are grouped by university. While useful, the sheet has 1,894 rows and is cumbersome to use. It would be much easier if you could examine just the rows for each school, right? That's why you should use filters, which help journalists isolate specific data in a large set.

The name of the school appears in Column A, so if we can isolate that, we can easily inspect each school's data.

1.  Go to the Data pull-​down menu at the top of the spreadsheet and select Create a Filter from the menu (see [Figure 5.7](#ch05.xhtml_f5_7)).


2.  Once you create the filter, small triangular icons appear in your header row next to the words in each cell (see [Figure 5.8](#ch05.xhtml_f5_8)).


3.  Click on the filter next to University in cell A1. In the interface, hit the Clear button, and then click on Illinois to select it. Then hit the green OK button (see [Figure 5.9](#ch05.xhtml_f5_9)).


4.  The spreadsheet will isolate only the 147 rows for the University of Illinois in Champaign. You can then sort and reorder the spreadsheet by cases or tests to begin asking questions of the data, much like we did in sorting the bridges database.

The advantage of using filters is you can extract the isolated data by copying it to a new sheet, tab or saving it as its own sheet. The original dataset is still there. All you have to do is go back to the Data pull-​down menu and select Turn off Filter and the complete dataset will return.

We'll do more filtering and sorting in [Chapter 6](#ch06.xhtml_c6), Advanced Spreadsheets and R.

:::: section

## Figuring Rates

Rates help level the playing field when making comparisons. They have been very helpful in calculating COVID-​19 data by comparing rates in large cities to those in smaller towns. They're also used when comparing homicides between larger and smaller cities.

Spreadsheet formulas are extremely helpful in calculating math problems, both basic and complex. We'll apply some of those formulas to our second exercise: Big Ten Cases per 1,000 students. Click on that tab in the Big Ten exercise spreadsheet you have opened, and inspect the data.

We'll use formulas to total the positive cases, enrollment and the average positive cases per school in the Totals row at the bottom of the spreadsheet. The average will be helpful in seeing which schools are above or below the average.

<aside class="boxed-text2" epub:type="tip" role="doc-tip">

::: section
### Google Sheets Formulas 

Google compiled a deep list of formulas (functions), so you don't have to memorize them. Bookmark this to keep it handy. You'll use it a lot: [https://bit.ly/googlesheetsform](https://bit.ly/)

</aside>

Then we'll figure the rate for each school by dividing the positive cases per school by the enrollment and normalizing it to 1,000 students. Normalizing the data gives readers scale and helps them better understand the impact on each school rather than just looking at raw numbers.

1.  Click in cell B17 and type this formula: =sum(b2:b15) and hit return ([Figure 5.10](#ch05.xhtml_f5_10)). As you finish typing, the answer should pop up in blue just above the formula. You should get 41,422 positive cases. Remember, think of your spreadsheet as a game of Battleship: You want to summarize cells B2 to B15. These formulas work in rows as well, which we discovered in the bridge inspections exercise.


2.  Now click in cell C17 and type this formula =sum(c2:c15) and hit return.

3.  You now have two data points for your story: During the fall football season, Big Ten schools had 41,422 positive COVID-​19 cases, while their total enrollments stood at 607,980. Not earth-​shattering, but it's a good start.

4.  Now let's make a new column. In cell D1, type "Cases per 1k students".

5.  Click in cell D17 and type in this formula: =b17/c17\*1000. You should get 68.1. (Tip: Use the decrease decimal button in the top toolbar to round down the number to one-​tenth.) We now know that the average number of positive cases per 1,000 students on a Big Ten campus in fall 2020 was 68.1. This number will be helpful when we calculate and sort the cases per 1,000 for each school.

6.  Now go to cell D2 and type this formula: =b2/c2\*1000 and hit return. You should get 88.56, and Google Sheets will give you the option to autofill the rest of the cells to get the totals for each row. Click the green checkmark to do so (see [Figure 5.11](#ch05.xhtml_f5_11)).


7.  Click the decrease decimal point button a few times to round off the data to one-​tenth. Then highlight only rows 1 through 15, and sort the data Z to A by the "Cases per 1k students" column.

    You'll see Penn State surges past Ohio State as the leader in positive cases per 1,000 students. Indiana and Iowa also are near the top, the two Michigan Schools hovered right at the average and Minnesota, Maryland and Rutgers had the lowest rates ([Figure 5.12](#ch05.xhtml_f5_12)).


::::: section
## Turning the Data into a Story

After Katsaros and Tharpe finished filtering, sorting and calculating the rates, they interviewed expert sources and did some additional reporting for the story. They used the data to create a small database of Big Ten university cases and slick animated graphics in Google Flourish, which you'll learn to use in a later chapter.

The story, published in December 2020, highlighted not just the total number of cases but the rate per 1,000 students at each school. Normalizing the data gave a clearer picture of what was happening on Big Ten campuses. Ohio State dropped from first (total cases) to second behind Penn State in cases per 1,000 students. In an ironic twist, Ohio State beat Northwestern, which had the fewest cases, in the Big Ten Championship game. One stat that didn't appear in the box score: Not one Northwestern football player tested positive for COVID-​19 the entire season.

We'll explore more writing approaches in [Chapter 7](#ch07.xhtml_c7).

\* \* \*

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 2 ![](images/Exercise_Icon.jpg) 

**City Budget**

For our next exercise, we're going to analyze a fictitious city budget. Download or make a copy of the exercise here: [https://bit.ly/citybud](https://bit.ly/).

Note the budget has department revenues and expenses. We're going to compile the percentage change between last year's and this year's budgets for each department's revenues and expenses. Then we will compile the percentage of the total budget each department is getting. Finally, we'll double-​check the totals that the city has given us to make sure they are correct. Note that the budget has a data moat between the totals and each department row.

Follow these steps, and use the formulas below. Apply what you learned on previous exercises to fill in the columns. Be prepared to answer some questions at the end of the exercise.

1.  **Column D: Figure percent change**

    Start by labeling cell D1: Percent Change.

    The formula you'll use is =(new budget-​old budget)/old budget (this is also known as the NOO acronym). So type this formula into cell D2 and drag the cell border down or hit Autofill to fill the rest of the column: =(c2-​b2)/b2

    Delete any errors in the blank rows, then highlight all of column D and click on the % button in the toolbar and click the decimal left button next to it once to move the percentage over to one decimal point. Your spreadsheet should look like this when finished ([Figure 5.13](#ch05.xhtml_f5_13)):


2.  **Percentage Total Budget column**

    In order to figure the percentage of total budget each department gets, we have to anchor the cells in C16 and C31, the totals, to get the correct total.

    Start by labeling cell E1: "Percentage Total Budget." In cell E2, paste this formula, and fill the cells under it by dragging the cursor or using autofill. Be sure to stop at E14, the end of the expenses section: =c2/\$c\$16

    In cell E20, paste this formula, and repeat the steps above that you used to fill the expenses section: =c20/\$c\$31

    Your spreadsheet should look like this ([Figure 5.14](#ch05.xhtml_f5_14)):


3.  **Fact-​checking budget totals**

    City officials added a Totals row under each budget to summarize all department expenses and revenues for each year. You always need to fact-​check this figure as there can be errors. Use the =SUM formula we used earlier in the chapter to calculate the totals.

    In Cell B17, type: =sum(b2:b14)

    In Cell C17, type: =sum(c2:c14)

    In Cell B32, type: =sum(b20:b29)

    In Cell C32, type: =sum(c20:c29)

    Do the totals match the totals the city gave you? It looks like only one total was correct. Here's what your sheet should look like ([Figure 5.15](#ch05.xhtml_f5_15)):


</aside>
<aside class="boxed-text2" epub:type="tip" role="doc-tip">

::: section
### Budget Challenge Questions 

1.  You notice that the revenue and expenses totals in the columns don't match the sum of all of the departments. Something is amiss. As a reporter writing this city budget story, what would you do?
2.  How would you write the story about this budget? What are the biggest changes or key departments to focus on? Summarize your analysis in a few short paragraphs.

</aside>

::: section

## Challenge Answers

1.  Don't assume the totals the city gave you are wrong. The error could occur in the individual department numbers. A few typos, anything. A good reporter would contact the city treasurer or other official handling the budget and trace back the error. It could be a reporting error or a typo or something could be amiss.
2.  There are a few angles. I would start with finding out why the police and health departments have double-​digit expense increases. More hires? A lawsuit settlement? Why the change? And it looks like the parks and recreation department spent nearly 12 percent less than the previous year. Was a major project eliminated? Other cuts?

As for revenues, the big increase came in the "revenue from other sources" category. What were they? And are these revenues expected to carry over into future budgets that the city can count on?

\* \* \*

::: section
## Resources

Try some of these tools and primers to extend your knowledge of spreadsheets.

Google Sheets vs. Microsoft Excel: The Differences Are Disappearing [https://bit.ly/sheetsexcel](https://bit.ly/)

Journalists argue this in newsrooms across the country. Sheets are better for collaboration on multi-​staff investigative projects. And there are fewer differences between the software compared to just a few years ago.

Data journalism training: Beginner Excel [https://sites.google.com/view/mj-basic-data-academy/home](https://sites.google.com/)

Mary Jo Webster of the Minneapolis Tribune offers a great beginning Excel tutorial.

Journalist's Toolbox Public Records [http://bit.ly/jtbpublicrecords](http://bit.ly/)

Search dozens of public records and data portals to find spreadsheets to sort, filter and develop into stories.

Investigative Reporters and Editors [https://www.ire.org/resources/](https://www.ire.org/)

IRE offers dozens of case studies, exercises and online training with spreadsheets.

\* \* \*


## Footnotes

- BBC, Italy Bridge Collapse: Genoa Death Toll Reaches 43 [https://bbc.in/3G7ctKe](https://bbc.in/)
- MSNBC, Almost 1 in 10 US Bridges Needs Repairing [https://on.msnbc.com/3IGq8tq](https://on.msnbc.com/)
- American Road & Transportation Builders Safety Report <https://artbabridgereport.org/>
- National Bridge Inventory -- Bridge Inspection Safety Database [https://bit.ly/ch5spreadsheet](https://bit.ly/)
- MediaShift, Take an Interviewing Approach to Find Stories in Data [http://mediashift.org/2014/07/take-an-interviewing-approach-to-find-stories-in-data/](http://mediashift.org/)
- KBIA, Columbia Animal Sanctuary Regularly Cited by USDA Inspectors [https://www.kbia.org/environment/2016-05-11/columbia-animal-sanctuary-cited-regularly-by-usda-inspectors#stream/0](https://www.kbia.org/)
- Bureau of Transportation: County Transportation Statistics [https://data.bts.gov/Research-and-Statistics/County-Transportation-Profiles/qdmf-cxm3](https://data.bts.gov/)
- The Red Line Project, Thousands of Bridges Graded 'Structurally Deficient' [http://redlineproject.org/poorbridges.php](http://redlineproject.org/)
- Google Sheets Functions List [https://support.google.com/docs/table/25273?hl=en](https://support.google.com/)
- Journalist's Toolbox Training Video: Determining Rates in Google Sheets [https://bit.ly/toolbxorates](https://bit.ly/)
- Google Sheets: Big Ten School COVID-19 Positivity Rates [http://bit.ly/bigtencovid19](http://bit.ly/)
- The Red Line Project, Saturday Night Football During COVID-19, Less Beer, More Masks 2020 [http://redlineproject.org/big_ten_covid.php](http://redlineproject.org/)


# 6 Advanced Spreadsheets and R

Samantha Sunne

DOI: [10.4324/9781003273301-7](https://doi.org/10.4324/9781003273301-7){aria-label="D.O.I. link to this document."}

## Introduction

So far, we have learned the basics of spreadsheet operations -- ​creating one, establishing data types and filtering for relevant data. In this chapter, we will expand our repertoire of formulas and learn additional point-​and-​click tools that make analysis in a spreadsheet easy.

Throughout this book, we will continue to use Google Sheets. Sheets differs from Microsoft Excel, probably the world's most famous spreadsheet program, in a few key ways.

First, it is based entirely online, unlike Excel, which only connects to the Internet to sync files across Microsoft products. Google Sheets is free with a Google account, but only a limited version of Excel is free with a Microsoft account.

Excel is a paid desktop app, which means it tends to have more robust tools and processing power. For example, at the time of writing, Excel could handle billions of data points, while Google Sheets could handle up to 10 million.

This doesn't take into account the reality of manipulating millions of rows over an Internet connection. Excel can work offline thanks to its desktop app, while Google Sheets' offline functionality is limited.

There are also free spreadsheet desktop apps, like OpenOffice, though they may also offer limited functionality compared to the big two. If you work with so much data that your spreadsheet program starts to fail or freeze, we will learn about even more powerful programs in [Chapter 8](#ch08.xhtml_c8).

In the end Google Sheets and Excel have similar functionalities, at least for the average data user, and they become more and more alike as time goes by. Throughout your reporting career, you should utilize whichever program makes the most sense for you.

In this chapter, we will continue to analyze the dataset of COVID-​19 cases in Big Ten universities from [Chapter 5](#ch05.xhtml_c5) (you can download it or make a copy here: [http://bit.ly/bigtencovid19](http://bit.ly/)).

<aside class="boxed-text2" epub:type="tip" role="doc-tip">

::: section
### Referencing Tabs 

We learned how to write cell references, like B2 -- ​what about tab references? In Google Sheets, spreadsheet tabs each have a name, even if that name is just something like "Sheet1." If you want to refer to a cell or range within that sheet, you can use an exclamation point (!) between the tab name and cell range, like this: "Sheet1!A2:D10."

If your tab has a name with spaces, it should be wrapped in single quotes, like this: "'Big Ten Daily Covid-​19 Cases'!A2:D10."

You most likely will only need to reference tabs if you're running calculations across multiple tabs. But the ability to refer to different tables will come in handy especially when we write SQL queries in [Chapter 8](#ch08.xhtml_c8).

</aside>

::::: section

## Formulas

Formulas, also called functions, are one of the key tools in the spreadsheet toolbox. We have already used several of them for scraping, cleaning, fact-​checking and analysis.

In addition to the ones we have already learned, these are some of the most common and useful formulas you will encounter ([Table 6.1](#ch06.xhtml_t6_1)). These are for Google Sheets, but other programs will have similar functions with slightly different names and limitations.

+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| AVERAGE()                         | AVERAGE() returns the average of a list of numbers, also sometimes called a "mean." The program calculates it by tallying the sum of values and dividing it by the number of values in the list.                             |
|                                   |                                                                                                                                                                                                                              |
|                                   | You can use this function on individual cells or a range or both. It will ignore any text values.                                                                                                                            |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MEDIAN()                          | The median is different from the average in that it returns the "middle" number between the highest and lowest. If there are two equal numbers in the middle, the program will calculate the average of those two.           |
|                                   |                                                                                                                                                                                                                              |
|                                   | Just like AVERAGE(), the MEDIAN() formula only works on numbers, but it can take a list of ranges or cells. You can learn more about the difference between the median and the average in [Chapter 12](#ch12.xhtml_c12).     |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MODE()                            | The mode is the number that occurs most often in a list. Once again, the MODE() function will only work on numerical values but can take ranges and individual cells.                                                        |
|                                   |                                                                                                                                                                                                                              |
|                                   | See [Chapter 12](#ch12.xhtml_c12) for more ideas on why you might want to find the mode in a list.                                                                                                                           |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| COUNTA()                          | The COUNTA() function, as its name suggests, counts values in a range or list. For instance, if your dataset has 1,102 rows, but some are empty, you could use COUNTA(A1:A1102) to see how many actually contain values.     |
|                                   |                                                                                                                                                                                                                              |
|                                   | Like the other functions, COUNTA() can intake ranges, cells and individual values.                                                                                                                                           |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| COUNTIF()                         | COUNTIF() is a more advanced version of COUNT(): It will only count values meeting a certain condition. For instance, if you wanted to count the values above 10,000 in a list, you could use COUNTIF(A2:A1102,\"\>10000\"). |
|                                   |                                                                                                                                                                                                                              |
|                                   | COUNTIF() can count text values. It also takes two parameters: the range to search and the condition to check against.                                                                                                       |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SUMIF()                           | SUMIF() is similar in that it adds up the cells meeting the criteria, as opposed to counting them.                                                                                                                           |
|                                   |                                                                                                                                                                                                                              |
|                                   | Like COUNTIF(), SUMIF() has two parameters: the range to search and the criteria. Unlike COUNTIF(), it only works on numerical values. You can also use it to calculate sums in one column based on another column.          |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LEFT()                            | LEFT() is a simple formula that returns a certain number of characters from the left hand side of a value. For example, if cell A2 has the value "Australia," the formula LEFT(A2,5) would return "Austr".                   |
|                                   |                                                                                                                                                                                                                              |
|                                   | It can be useful for cleaning or isolating bits of data, the same as we did with the SPLIT() function.                                                                                               |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| RIGHT()                           | RIGHT() extracts a certain number of characters from the right hand side of a value.                                                                                                                                         |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: *[Table 6.1*](#ch06.xhtml_t6_1b) Common Formulas

<aside class="boxed-text2" epub:type="tip" role="doc-tip">

::: section
### Hiding Columns 

After writing formulas, it can be helpful to hide the column the formula was working on, to keep your spreadsheet tidy. You can hide rows and columns in most spreadsheet programs by right-​clicking on the row or column and selecting "Hide." This is different from deleting and even technically different from filtering.

The program only makes the columns invisible, and you can re-​expand them later. In Google Sheets, you would do this by clicking on the small left-​ and right-​pointing arrows in the column bar.

Just like with filters, make sure you don't forget which columns or rows you hid. Often the program will indicate that there are columns hidden by including small arrows.

</aside>

::::: section
## Concatenate

In [Chapter 4](#ch04.xhtml_c4), we learned the SPLIT() formula to separate individual vaccines that were listed in the same column. The CONCATENATE() formula is kind of the opposite: It pulls values from different columns and puts them in the same cell.

Let's say we're making a map of COVID-​19 cases at Big Ten universities, and we want the city and state to be in the same column. We can do that using the CONCATENATE() formula.

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 1 ![](images/Exercise_Icon.jpg) 

1.  Open your spreadsheet of Big Ten Covid cases from [Chapter 5](#ch05.xhtml_c5), and make sure you're on the first tab, "Big Ten Daily Covid-​19 Cases."

2.  Give Column G the name "City and State."

3.  In cell G2, type this formula and press enter:

    =CONCATENATE(B2, C2)

    That gives us a confusing result--​the city and state are squished together as one long text string. Let's use another feature of CONCATENATE(), which is to specify additional characters or strings to add. The usual way to write a city and state in American English would be "City Name, State Name." We'll make the spreadsheet emulate that by adding \", \" in between the two values.

4.  In cell G2, edit your formula to add a third parameter, like this:

    =CONCATENATE(B2, \", \", C2)

5.  Copy down your formula to apply to the rest of the rows.

6.  Click on the letter B to highlight Column B. Hold down the Shift key, and click on the letter C to also highlight Column C.

7.  Right-​click on the column names and select "Hide columns".

Now we have a new column combining columns B and C ([Figure 6.1](#ch06.xhtml_f6_1)). If you were to actually use a mapping tool, you may need to use the Paste Special \> Values technique we learned in [Chapter 3](#ch03.xhtml_c3) to input it in a mapping tool. Paste Special \> Values pastes the values as plain text rather than as a formula.


</aside>
<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Pro Tip 

While typing in your Concatenate formula, Google Sheets may suggest the shorter-​named CONCAT() function. This is just a minimized version of concatenate, and it can only combine two values. If you want to add a third element, like the comma and space characters, you will need to use the full CONCATENATE() function.

</aside>

::: section

## IF Statements

When you're writing formulas in spreadsheets, and not quite writing your own code yet, IF statements are one of the most powerful tools in your toolbox. It's basically like writing a conditional sentence right into your spreadsheet cell.

Here is the IF formula:

1.  =IF(CELL meets CRITERIA, then THIS, otherwise THAT)

It makes more sense when you see it in action. Using our COVID spreadsheet as an example:

1.  =IF(F2\>20, \"High case rate\", \"Low case rate\")

You can read the function from left to right, as you would a sentence. If the number of confirmed cases at a school (F2) is greater than 20, the spreadsheet will print the phrase "High case rate." If it is *not* greater than 20, it will print "Low case rate" ([Figure 6.2](#ch06.xhtml_f6_2)). And that's it!


You can also write nested IF functions. If you recall from [Chapter 3](#ch03.xhtml_c3), when we talked about HTML, "nested" means to wrap one function inside another. A nested IF statement might look like this:

1.  =IF(F2=0, \"No cases\", IF(F2\>20, \"High case rate\", \"Low case rate\"))

This adds a third parameter. If F2 is zero, the spreadsheet will write "No cases." If F2 is not zero, then the computer will turn to the second IF function: The same one we wrote above. This provides three possibilities for what the cell will populate with, all based on values in Column F.

As you can see, IF statements are a useful tool but are still limited. For instance, what if you wanted more than three possible outcomes? You could technically keep writing nested IF statements within IF statements within IF statements -- ​but that gets messy! Once you get to that point, it's better to use another method.

::: section
## IF Error

One common use of IF statements is to avoid pesky error messages. For example, if you are running a conditional on a cell that is empty, Google Sheets will sometimes populate your cell with "#DIV/0", meaning it tried to run a formula on a nonexistent piece of data.

This can be confusing, so you can avoid them altogether using a subset of Google Sheets IF functions called IFERROR(). It looks like this:

1.  =IFERROR(FORMULA is an error, then THIS)

The simplicity of IFERROR() is that you don't actually need to specify an outcome. If there is an error in the formula or calculation, IFERROR() will simply leave the cell blank. If you think your formula is liable to prompt errors, you can wrap it in an IFERROR() formula, like this:

1.  =IFERROR(A2/B2)

For example, if we tried to calculate the number of tests per confirmed cases, the first two rows would return errors. Wrapping that calculation in an IFERROR() formula would replace these errors with simple blank rows ([Figure 6.3](#ch06.xhtml_f6_3)).


::::: section

## Nested Functions

:::: section
### Mid

Another useful nested formula to know is the SEARCH() function. As we learned earlier, the LEFT() function pulls a certain number of characters from the left and RIGHT() from the right. But what if we don't know how many characters to pull, or we want to start somewhere in the middle? The MID() function does that. It takes three parameters:

1.  =MID(CELL to search, POSITION to start at, NUMBER OF CHARACTERS to extract)

For example, this formula in our COVID spreadsheet would return the first five letters of the name of the university. We know it would return the first five because we ordered the formula to start at character number 1.

1.  =MID(A2, 1, 5)

Let's say we want to chart the number of COVID cases by month and need a column showing the month that each count was taken in. We could use =LEFT(D2,1) to extract just the first character from the date.

This would give us the number 7 in Row 2, meaning July, but what about October? In Row 89, we need to pull two characters, not one. But if we use =LEFT(D2,2), we get a slash (/) in some rows! How frustrating.

One answer is the SEARCH() function.

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
#### Pro Tip 

If you don't know what to enter for MID's third parameter, the number of characters to extract, one hack is to give a large number like 100 to extract all characters. But, even if you're reasonably confident that all your data is less than 100 characters, you should scroll through to make sure. While you can make reasonable assumptions as you go along, never publish your assumptions without doing at least a cursory check like we learned in [Chapter 4](#ch04.xhtml_c4).

</aside>

::::: section
## Search

The SEARCH() function can be confusing at first, but it is useful.

It returns the position of a character or string in a cell. For instance, if we have a column of expenses, the formula SEARCH(\"\$\", A2) would return the number "1" because the expense starts with a dollar sign. If the cell doesn't contain a dollar sign, SEARCH() would return the "#VALUE!" error message.

Like MID(), the SEARCH() function takes three parameters:

1.  =SEARCH(for CHARACTER, in CELL, starting at POSITION)

For example, in our COVID spreadsheet, cell A2 contains the word "Illinois." This formula would return the number 4:

1.  =SEARCH(\"i\", A2,3)

The letter "i" is actually the first letter in the cell, meaning it has position 1. But because the starting position is 3, SEARCH() counts the next "i" after that, which is position 4. If you plan to start at the first character, it is fine to omit the third parameter entirely.

You can see how the SEARCH() function can be powerful, but also a bit confusing. It's best to remember that computers think differently than us, and we are on their turf. If you are running into errors, it also never hurts to use a search engine.

\* \* \*

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 2 ![](images/Exercise_Icon.jpg) 

Let's use MID(), SEARCH() and nested functions to make a "Month" column in our Big Ten spreadsheet.

1.  First, give Column H the name "Month." In cell H2, we will start with our MID() formula.

    The first two parameters are rather easy: We know the Date is in cell D2, and we know we want to start from the beginning. So our formula looks like this:

    1.  =MID(D2,1,?)

    The third parameter is a question mark (?) because we don't know how many characters to extract. In July, we want one, but in October, two.

    Let's use the SEARCH() function to figure it out. As we know, the SEARCH() function returns the position of a character or string of characters. How can it help us isolate the month? By looking for a slash (/).

2.  Give Column I the name "Slash Position." In cell I2, enter this SEARCH() function, and copy it down to the rest of the rows:

    1.  =SEARCH(\"/\", D2,1)

    Cell I2 should populate with the number 2, because the slash was the second character in D2. In cell H89, it should show 3. Progress!

    Now, let's put our SEARCH and MID tools together.

3.  In cell H2, replace the question mark with your SEARCH formula, creating a nested formula. Copy it down to apply to the rest of the rows.

    1.  =MID(D2,1,SEARCH(\"/\", D2,1))

    Well--​it kind of worked. We can see that H2 returned the number 7, and H89 returned 10, but they also included the slash. That isn't going to look very good on a chart.

    Because the MID formula takes a number as its third parameter (the number of characters to extract), that SEARCH function is actually telling the computer a number. And that number is one too many, as we can see by the long list of numbers containing slash marks after them. Let's remove it with a simple math equation: subtraction.

4.  Add the text "-​1" to your third parameter to reduce the position by one. It should go after the parentheses creating the SEARCH function but before the parentheses closing the MID function.

    1.  =MID(D2,1,SEARCH(\"/\", D2,1)-​1)

    And voila! Copying this rather confusing-​looking formula down the rest of our sheet returns a simple number for each month ([Figure 6.4](#ch06.xhtml_f6_4)). No extra slash marks and no cutoff months, either.


</aside>
<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Pro Tip 

When working with nested functions, make sure you have the correct number of parentheses. Sometimes you can type too many, or a program will autofill one for you.

You can check by clicking on each parenthesis and making sure it has a pair at either end of the formula. Programs like Google Sheets will also try to help you by highlighting the punctuation marks in bold or different font colors.

</aside>

These nested functions may look daunting, but as with so many other skills in this book, they will become less so the more you use them. In some cases, the REGEXEXTRACT() formula we learned in [Chapter 4](#ch04.xhtml_c4) may be a better method for extracting parts of a text string.

:::::: section

## Pivot Tables

A pivot table is a fantastic way to organize your data and get straight to the point. Its key function is that it groups together values in order to create a summary. This is similar to the GROUP BY syntax we will learn in [Chapter 8](#ch08.xhtml_c8) but with the advantage of point-​and-​click tools.

Grouping values is an extremely common task you will find yourself doing, so it's best to get comfortable with pivot tables now. One hurdle is that the interface for creating one can be confusing, just like the name ("pivot" refers to "pivoting" the rows and columns to make new combinations).

We will learn to make one in Google Sheets, but each program will, of course, have its own buttons and steps.

<aside class="boxed-text2" epub:type="tip" role="doc-tip">

::: section
### Transposing 

Switching the places of the rows and columns is called Transposing, and it's a useful feature, even if it's somewhat uncommon. Transposing is different from "pivoting," because it does not group any rows together: It simply rotates the entire table by 90 degrees, so to speak.

In Google Sheets, the easiest way to transpose is to highlight all the data, copy it to your clipboard and then, on a new tab, click Paste special \> Transposed.

</aside>
<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 3 ![](images/Exercise_Icon.jpg) 

We're going to find out which months had the most COVID cases, using a pivot table.

1.  Create a new pivot table by clicking Insert \> Pivot table.
2.  In the pop-​up window, confirm your data range. It should be your full dataset, consisting of several columns and more than 1,000 rows.
3.  Check the radio button for New Sheet and click Create. This will open the pivot table editor in a new tab.

In the pivot table editor, we have four options to work with: Rows, Columns, Values and Filters. Clicking the Add button will create a new instance of that category for *every* instance of that variable. For instance, clicking Add \> University in the Columns section would create 14 new columns, because there are 14 universities in the Big Ten Conference ([Figure 6.5](#ch06.xhtml_f6_5)).


So, before creating a pivot table, think: What would my ideal table look like? You can even sketch it out on a napkin. If you end up with far too many columns, or the wrong values in your rows, you can click the X in the variable box to delete it.

</aside>
<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
#### Exercise 4 

In this case, our ideal table would have a row for every month and a value showing the number of COVID-​19 cases that month. Let's make it!

1.  In the pivot table editor, click the Add button in the Rows section, and select Month. The pivot table will create a row for every month.
2.  The values we want to see are the number of COVID-​19 cases. So in the Values section, click Add \> Confirmed Cases.
3.  Right away, the table creates a SUM of the total COVID-​19 cases per month. This is the key to a pivot table.
4.  The next step is sorting, which is managed in the Rows section.
5.  In the Month variable box, choose the drop-​down for Confirmed Cases and the drop-​down for Descending.

Our finished table should have a month in every row, followed by the sum of confirmed cases that month ([Figure 6.6](#ch06.xhtml_f6_6)). It should be sorted in order of COVID-​19 cases, from largest to smallest.


Thanks to this table-​of-​a-​table, we can see that COVID-​19 cases were highest in the autumn months.

As with many of the tools addressed in this book, this is only the start of pivot tables. You can choose additional variables in the Row section to create subsections, or drag a column to the Filter section to filter for only rows meeting a certain criteria. You can Count or Average the case numbers instead of Sum them.

Try experimenting to find which school had the most cases or other conclusions you might want to use for your story.

</aside>

::: section
## Correlation and Causation

It may be tempting to say that COVID-​19 cases spiked due to students returning to campus, or because of the cold weather, but we don't actually know for sure.

This is the difference between correlation and causation. "Correlation" means two values are related, while "causation" means that one *caused* the other. This is notoriously hard to establish with data alone, and it's not ethical to imply causation without doing additional research.

One way around this is to share that cases were highest in the fall and also share opinions from experts that it may be due to students returning to campus. This way, you are accurately conveying your findings, as well as possible reasons why, without overstating them.

Another method is to be clear with your audience that you don't actually have enough evidence of causation, like this: "COVID-​19 cases were highest in the fall, but the data did not make it clear why."

If you aren't comfortable enough, you can simply avoid mentioning correlation or causation at all: "COVID-​19 cases were highest in September, October and November." You also don't want to imply causation and later turn out to be wrong!

:::: section

## Analysis in R

You can also take your analysis skills to the next level by writing code. We will learn more about how to write and deploy code in [Chapter 9](#ch09.xhtml_c9), but one of its main advantages is that it can be used for analyzing very large sets of data. This chapter will offer a short introduction to doing spreadsheet-​type analysis in a more in-​depth program.

R, despite its extremely short name, is the name of a programming language. Like other languages, it can be downloaded to your computer and used to run functions and write scripts. In this case, we will simply use R in a browser-​based tool called RStudio Cloud.

The RStudio desktop app is a graphical user interface (GUI) for R, meaning a point-​and-​click program for writing and running R code. RStudio is free to download and use, but it requires the user to install the R language on their computer, which can lead to other complications (more on this in [Chapter 9](#ch09.xhtml_c9)).

RStudio Cloud avoids this by running all of its work in the cloud. It is not capable of quite as much computing power as a desktop app -- ​let alone straight through a Command Line Interface -- ​but it is more than enough for the purposes of this initial journalistic analysis.

RStudio is meant for all kinds of R coding projects, not just analysis, so its appearance can be customized extensively. Because we are importing data and writing analysis commands, we will start with three main panels, or "panes." These are the Console, Environment and Files panes ([Figure 6.7](#ch06.xhtml_f6_7)).


<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 5 ![](images/Exercise_Icon.jpg) 

We will learn how to do the same tasks we did in Google Sheets, like importing and filtering, in R. First, we will open the GUI and create a new project file.

1.  In a web browser, go to RStudio.Cloud and create a free account.
2.  Create a new project by clicking New Project \> New RStudio Project in the top-right corner of the workspace.
3.  In the top toolbar, change the project name to "big_ten_covid." In many programs, but especially in programming, it's best to avoid spaces and instead use underscores () in just about everything from functions to file names.
4.  In one pane, make sure the Console tab is selected. This is where we will write our commands. Set another pane to display the Environment and another to show Files. The Environment shows the tables we are working with.

You can experiment with other panes and views, like History, which shows your past commands, and Packages, which shows add-on tools you can install.

</aside>

:::: section
## Importing

Now that we have created an RStudio project, we can begin our analysis.

\* \* \*

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 6 

1.  Download the COVID-​19 spreadsheet (the first tab) as a CSV by clicking File \> Download \> Comma Separated Values. Once it has downloaded, rename the file to "Big-​Ten-​Covid-​Cases.csv." This name will make it easier to reference in R.
2.  Upload the CSV to RStudio Cloud by clicking the "Upload files to server" button in the Files pane. It looks like a white square with an up arrow.
3.  Use the upload wizard to select the COVID-​19 file. Once uploaded, you should see it listed in your Files panel.
4.  Next, import it into your project by clicking File \> Import dataset \> From text (base).
5.  In the import wizard, make sure the data preview looks correct and that the separator is a comma.
6.  Click Import. You should now see a preview of your table in a new pane.

</aside>

When importing, RStudio offers the user several options for specifying their data ([Figure 6.8](#ch06.xhtml_f6_8)). These include the separator (the delimiter), the character encoding, whether the data uses single or double quotes and whether it contains a header row.


Generally speaking, if you are unsure about importing options, it's best to leave the default selection as is. If problems arise, refer back to [Chapter 4](#ch04.xhtml_c4) for troubleshooting and common solutions. Using a web search to research your own solution is always an option.

One thing that the import wizard does not address is data types. Remember, these are formats for columns, such as dates, numbers and text. Later on, we will learn how to see and edit these data types.

:::: section

## Summaries

As we said in the Introduction, R can be used for very large datasets. Often, these datasets are too big for a computer to even attempt to display (imagine trying to skim millions of rows!). Instead, these more advanced data programs will display overviews, or summaries, of your data tables.

Now that we have imported our data, let's pull up a summary to make sure that it looks correct.

\* \* \*

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 7 

1.  In the Console pane, type the command "head([Big.Ten.Covid.Cases](http://Big.Ten.Covid.Cases))" and press enter. This will return a list of the first few rows of your dataset.

2.  Next, type "nrow([Big.Ten.Covid.Cases](http://Big.Ten.Covid.Cases)") and press enter. This will return the number of rows ([Figure 6.9](#ch06.xhtml_f6_9)).


</aside>

These are called summary functions, and they are used to get a sense of the data you are working with before you start executing commands on it. After importing, you should be thinking critically about your dataset and potential problems it could have. Summary functions help you make sure the row count and other factors seem at least in the ballpark of correct.

They are also useful for the "gut checks" we talked about in [Chapter 4](#ch04.xhtml_c4). For example, if you open the original CSV in a text editor, does it show the same number of rows as the answer to the nrow() function?

RStudio is a GUI, which means it offers buttons and menus as an alternative to typing out commands. For instance, if you scroll up in your Console pane, you may see the function read.csv(). This is the function that ran when we selected the "Upload files to server" button in the Files pane.

These buttons and drop-​down menus may feel more comfortable because they are what we are familiar with, from web browsers to Google Sheets. As you progress in your data journey, you will become more comfortable with writing your own functions and commands.

:::: section
## Packages

In order to do this analysis in RStudio, we have to install an add-​on called a "package." These packages are extremely common when working with programming languages, and we will learn more about them in [Chapter 9](#ch09.xhtml_c9). In the case of RStudio, they can be found in the Packages tab of the Files pane ([Figure 6.10](#ch06.xhtml_f6_10)).


We'll start by installing a package called tidyverse.

\* \* \*

<aside class="boxed-text" epub:type="tip" role="doc-tip">

::: section
### Exercise 8 

1.  In the Files pane, navigate to the Packages tab, and click the Install button.

2.  In the pop-​up window, search for "tidyverse" in the Packages field.

3.  Leave all other options on the default and click Install. You will see the Console pane fill with text as RStudio installs the package.

4.  Once it has installed, check the radio button next to tidyverse in the Packages tab to load it into your project.

    1.  Now you have the tidyverse package installed and are ready to use the RStudio program to write queries.

</aside>

:::: section
