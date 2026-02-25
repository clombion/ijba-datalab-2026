<!-- chunk: 2/3 | source: 41-journalists-toolbox-handbook.md | words: 39767 -->
<!-- headings: Tools for Visualizing Data; Finding Data; ***Google Dataset Search***; ***Our World in Data***; ***[USAFacts.org](https://www.USAFacts.org)***; ***Eurostat***; ***Google Public Data Explorer***; Video: How to Find Datasets; Scraping Data; Writing Data Stories; Mapping; Types of Maps; Cool Google MyMaps Examples; ***Santa Barbara Mudslides/Fires Evacuation Zones***; ***St. Louis Post-Dispatch Homicides Map***; ***Knoxville: Underground Railroad Bike Tour***; ***Nashville Pothole Repairs***; Diversity, Equity and Inclusion in Data Journalism; Video: Data Visualization Playlist; Video Mobile Apps: Data Visualization -->

## Tools for Visualizing Data

Ramos suggests young data journalists start by learning these five pieces of software:

1.  **Excel:** No way to get around learning the basics with Excel. Ramos does most of his work with Excel if the dataset is small enough.
2.  **Open Refine:** This is a free and intuitive tool to clean up dirty datasets that require a more manual approach.
3.  **QGIS:** The ability to map out data and combine it with multiple datasets for analysis is a game-changer.
4.  **Flourish:** It's free, and it's a great way to explore data viz if D3 is too daunting.
5.  **Pandas/Python:** Using the Pandas library with an iPython notebook is a user-friendly way to handle large datasets while documenting your work in comments and markups.

Medill's Mackenzie Warren, who oversaw digital reporting for Gannett, recommends five basic visualization tools as "must-haves" for young journalists starting with data reporting. You'll eventually graduate to more challenging software such as R and ArcGIS, but here are five tools to get started with:

- **Google MyMaps:** Still the simplest and most powerful tool for mapping. Beneath the "How do I get there from here?" primary function lies powerful databases that bring every address richly alive. <https://mymaps.google.com>
- **Infogram:** Good at combining interactive charts and maps with individual data points. <https://infogr.am>
- **Canva:** Extremely flexible collaboration and publishing tool. One feature I like is the Docs to Decks tool, which enables you to convert any document into a presentation. <https://canva.com>
- **Flourish and Datawrapper:** Easily build interactive maps, charts and animations based on structured data. [https://flourish.studio/](https://flourish.studio) \| [www.datawrapper.de](http://www.datawrapper.de)

There are hundreds of other mapping, chart and infographic tools on the market, including Venngage and Tableau Public; the latter is excellent for building dashboards of data using just a single dataset.

All of these tools have free models with paid upgrades for various features. The key is to find the right tool that works for you, which we'll explore in the exercises at the end of this chapter.

\* \* \*

::::::::: section
## Finding Data

Reporters have many options for finding datasets. They can file a Freedom of Information Act (FOIA) request, like Ramos did for the Chicago police reports for his story. They can build the dataset themselves, like Ramos did when he merged the stolen cars dataset with the police report data that included the cars' make and model.

Reporters can pull datasets from a local, county, state or federal government data portal, which you can find listed on the Journalist's Toolbox: [www.journaliststoolbox.org/category/public-records](http://www.journaliststoolbox.org)

Medical associations, advocacy and nonprofit organizations compile data. The Pew Research Center is always a good place to start for large studies on breaking news trends.

There also are independent data portals and search tools that maintain large datasets, some of which are outlined next:

::: section
### ***Google Dataset Search***

<https://datasetsearch.research.google.com>

This micro-search tool works much like Google Scholar, which searches only academic journals and case law. Dataset Search links you directly to a web page with raw datasets and provides a short summary of who created the dataset, methodology, years the data covers, etc. While Google doesn't fact-check the data, it does provide that short summary that reporters can use to decide if they want to download it.

::: section
### ***Our World in Data***

<https://ourworldindata.org>

With nearly 3,400 charts on more than 300 global topics, this tool was indispensable during the pandemic. Searches provide links and embed code on international health, business and other census-level datasets. You can easily link to or embed the prebuilt charts or download the datasets to build your own.

::: section
###  ***[USAFacts.org](https://www.USAFacts.org)***

[https://usafacts.org/](https://usafacts.org)

Founded by former Microsoft CEO Steve Ballmer, this nonpartisan, nonprofit organization cleans up census, health, economic, immigration and other data and visualizes it. Much like Our World in Data, you can link and embed the charts or download the datasets. USAFacts also writes stories about some of the data it posts.

::: section
### ***Eurostat***

[https://ec.europa.eu/eurostat](https://ec.europa.eu)

Eurostat is the statistical office of the European Union. The clearinghouse site provides hundreds of economic and some health datasets on European countries.

:::: section
### ***Google Public Data Explorer***

[www.google.com/publicdata/directory](http://www.google.com)

This is more than a portal; you can actually design the graphic in the tool, which directly links to the dataset. No need for spreadsheet downloads or learning a new tool. This is a popular tool for day-turn graphics, such as a chart of unemployment rates by state ([Figure 5.10](#ch05.xhtml__15031-5909_ch005_Figure_010)).

\* \* \*


<a href="#ch05.xhtml_R_15031-5909_ch005_Figure_010"><em>Figure</em> <em>5.10</em></a> Unemployment rates by select state, 1990–2023, in Google Public Data Explorer


<aside aria-label="box3" class="box1" epub:type="tip" role="doc-tip" title="box">

::: section

## Video: How to Find Datasets 

[www.youtube.com/watch?v=czd3Vs84xhk](http://www.youtube.com)

Learn how to use the data search tools in this training video.

</aside>

\* \* \*

::: section
## Scraping Data

Data scraping, also known as web scraping, is the process of importing information from a website, a PDF or other document into a spreadsheet or local file on a computer.

It's an efficient way to get data from the web beyond a download button on a page. A scraping formula creates a link between the web page being scraped and the spreadsheet. Then, when the web page updates, so does the spreadsheet. This saves time, is more efficient and produces cleaner results than cut-and-paste.

Scraping can be done over Google Sheets, but Microsoft Excel has some scraping functions as well. They can be done by writing short formulas, or with free and paid third-party tools and browser plug-ins. You can easily find some third-party tools in the Google Chrome Store. Most offer short training videos on how to use them. [https://chrome.google.com/webstore/search/web%20scraping](https://chrome.google.com)

::: section

## Writing Data Stories

In December 2016, the Charleston (West Virginia) Gazette-Mail reporters wrote a series of stories called "Painkiller Profiteers" on the state's rising number of prescription drugs. In the fifth paragraph of the in-depth story, reporter Eric Eyre wrote a summary paragraph for the ages.

> In six years, drug wholesalers showered the state with 780 million hydrocodone and oxycodone pills, while 1,728 West Virginia families fatally overdosed on those two painkillers, a Sunday Gazette-Mail investigation found.
>
> The unfettered shipments amount to 433 pain pills for every man, woman and child in West Virginia.

In two sentences, Eyre encapsulated the issue using three key data points, the last of which he calculated by dividing the 780 million pills by the state's population. More importantly, the 433 pain pills per resident brought the story into a crystal-clear focus and scaled the issue in an alarming way.

When writing for the web, specifically mobile, a paragraph should never be longer than three sentences in order to maintain clarity and readability on those devices. Spreading the data throughout the story and balancing it with human-centered anecdotes, quotes and context helps increase reader understanding of the issue, said Heather Cherone, who writes many data-driven stories as WTTW Chicago's political reporter.

Cherone favors keeping one or two statistics per paragraph and keeping the stories focused on the people impacted by the numbers, not just the statistics themselves. She and many other data journalists are the first to tell you: Great data stories don't *read* like data stories. They are stories about how issues impact human beings.

"Many readers' eyes glaze over at the sight of numbers, and they are very likely to stop reading and head over to TikTok and never return," she said. "Talking about a person rather than a percentage can make an issue come alive for readers, and make it clear what is at stake."

To prevent this, you need to declutter your data stories. Jennifer LaFleur and Holly Hacker, speaking at the 2022 NICAR conference in Atlanta, said reporters must simplify numbers and present them in a concise way. They offered these tips:

- The number 29,912 can be rounded up: Nearly 30,000.
- Round off percentages, too: 62.2% is 62%; 79.9% is 80%; 75% is three-fourths or three in four.
- The percentages 12.55% of women and 25% of men can be 1 in 8 women and 1 in 4 men.
- Instead of a 100% increase, say it doubled. It's easier for the reader to understand.
- Break data into bullet-point lists and pullout boxes.
- Could the data be better presented in a chart, infographic or database? Does it *need* to be written?

\* \* \*

::: section
## Mapping

Some of the most common mapping tools used by journalists include the aforementioned ArcGIS, the cloud-based mapping software from Esri; [Carto.com](https://www.Carto.com) (great for animated timelapse maps), Google MyMaps, Open Street Map, MapBox, Maptive, StoryMap JS and the aforementioned Tableau Public, among many others. Flourish and Datawrapper are among the most popular as they have simple choropleth, symbol and locator maps templates that are intuitive and easy to use.

MyMaps is one of the most basic tools for map-building. It will handle a spreadsheet of data up to 1,000 rows and geolocate the addresses or other location data in the map. It allows for layering shapefiles and offers nine different basemaps. Developers have control over shapes of the pinpoints and colors and can easily integrate text, images and videos into the pinpoints. The exercises in this chapter will get you started with this tool.

:::::::: section

## Types of Maps

There are dozens of different types of maps that you can use to tell a story, but these are some that are most commonly used by journalists:

- **Pin map:** The most-common type of interactive map uses geocoding to assign map coordinate locations and provide data about that location. This is typically done through loading a spreadsheet into a tool such as Google MyMaps, [Carto.com](https://www.Carto.com) or another mapping tool. The map will geocode city names, names of buildings, street addresses, longitude-latitude, postal codes and more.
- **Cluster map:** Also known as a bubble map, a cluster map is an excellent alternative to a pin map that might have several tightly packed markers together in one area, according to Maptive. So instead of a large conglomerate of pins, you get a clean cluster icon that displays key information and corresponds with the number of markers contained in it. Zooming in reveals individual markers that are clickable.
- **Choropleth map:** Popular during the COVID-19 pandemic, these maps shade areas based on a value. For example, a country with more positive COVID-19 cases is shaded darker than a country with fewer. A legend typically shows the gradient scale and range of the data. They're common because they are easy for readers to understand
- **Symbol map:** This map appends symbols to show location or another form of data that can be applied to geographical locations. Tableau Public cites symbol maps as a way to point out the cities that have been hit by hurricanes throughout a period of time, with each symbol sized (scaled) to indicate the total number of hurricanes.
- **Locator map:** Shows the location of a particular geographic area within its larger and presumably more familiar context. The map can be used on its own or as an inset for a larger map -- for instance, highlighting Ireland in a map of the world to show its location.
- **Heat map:** Unlike choropleth maps, heat maps are not tied to a boundary. Instead, they have a color-code using the density of points. If there is a high density of crimes in an area, it shades the area as red. Fewer cases are orange, yellow, etc.

\* \* \*

<aside aria-label="box4" class="box1" epub:type="tip" role="doc-tip" title="box">

::::::: section
## Cool Google MyMaps Examples 

For seven years I did Google tools trainings in newsrooms all over the United States and the world. Traveling to 41 states, I taught journalists, professors and students how to build basic maps in Flourish and Google MyMaps. Below are four basic MyMaps produced in newsrooms where I did trainings.

For students, MyMaps is a good "starter tool" for learning mapping.

::: section

## ***Santa Barbara Mudslides/Fires Evacuation Zones*** 

A Santa Barbara Independent map shows 17 of the 23 victims from the mudslides may have been living under no evacuation notice of any sort. This illustrates an important role mapping plays in keeping people safe. It was built by the Independent's Brandon Yedgari. [https://www.google.com/maps/d/viewer?mid=1cHTu9A0R2oZjex4umwbIqqA6TEFgBVL4&ll=34.42604599418186%2C-119.58643346234783&z=13](https://www.google.com)

::: section
## ***St. Louis Post-Dispatch Homicides Map*** 

A great visual archive of the year's homicides. Note the link at the bottom of each summary to the news story. [https://www.stltoday.com/news/multimedia/special/st-louis-area-homicide-map/html_5964376e-2259-5363-9c40-774bbc0d0970.html](https://www.stltoday.com)

::: section

## ***Knoxville: Underground Railroad Bike Tour*** 

The Knoxville News Sentinel found an effective way to complement a story on the Underground Railroad by building this map. [https://www.knoxnews.com/story/money/business/2018/06/12/conservative-liberal-bike-underground-railroad-route-inspire-unity/684846002](https://www.knoxnews.com)

::: section
## ***Nashville Pothole Repairs*** 

The Nashville Tennessean built this map with data produced off the city's data portal. [https://www.tennessean.com/story/news/2018/03/12/nashville-potholes-interstate-traffic-tennessee-department-transportation/408620002](https://www.tennessean.com)

</aside>

\* \* \*

::::: section

## Diversity, Equity and Inclusion in Data Journalism

In 2022, investigative reporter Samantha Sunne and I authored a book "Data + Journalism" and featured a bonus chapter on our book's blog about diversity, equity and inclusion, also known as DEI, in data reporting. Sunne, who authored the chapter, raised some critical questions: "How can we incorporate data, and keep up with trends, while keeping diversity and inclusion in mind? How can we avoid leaving some groups behind, or emphasizing a status quo that leaves historically excluded communities at a disadvantage?"

Part of the answer came from Neema Roshania Patel, editor of The Washington Post's Next Generation team, who wrote a terrific set of five framing questions for a story for Poynter:

1.   Are we including the voices of the people most affected by what's happening?
2.  How are we defining "experts" in this story?
3.  Are we engaging with a diverse range of sources, even when the story isn't explicitly about marginalized groups?
4.  Are we making assumptions about our readers?
5.  How are we explaining our process to sources?

As with any story, data-driven pieces need diverse sources and voices. This goes beyond interviewing people impacted by the issue. It also involves actively seeking diverse expert sources in stories on any subject.

But how do we find them? Here are some excellent databases:

- Sources of Color
- Journalists, PR pros and diverse experts all in one place. The site is free for journalists but charges PR pros.
- [DiverseSources.org](https://www.DiverseSources.org)
- Database of experts features underrepresented voices and perspectives in science, health and environment work.
- NPR Diverse Sources Database
- Find experts from racial and ethnic groups underrepresented in the media. It also includes a featured "source of the week" and a state-by-state map of experts in your area.
- People of Color Also Know Stuff
- This online platform connects journalists with subject matter experts and people of color who have stories to tell. POC uses customized matching to connect journalists with a diverse pool of potential interviewees.
- Editors of Color: Database of Diverse Expert Databases
- CUNY: Diverse Expert Databases
- Library lists research guides helpful for finding diverse sources.
- AAJA Studio -- AAPI Sources
- The Asian American Journalist Association's curated directory offers newsrooms a platform to connect with trusted AAPI media leaders, established policy experts, academics and community leaders.

\* \* \*

<aside aria-label="box5" class="box1" epub:type="tip" role="doc-tip" title="box">

::: section
## Video: Data Visualization Playlist 

Select from more than 20 videos in this playlist of data visualization tool trainings: Flourish, Datawrapper, Tableau Public, Google MyMaps and more.

[www.youtube.com/playlist?list=PL6hKc1ARJkZI3vPhOj71kow6zcpVM6VlJ](http://www.youtube.com)

::: section

## Video Mobile Apps: Data Visualization 

Learn how to build data visualizations on your smartphone or tablet with mobile apps.

[www.youtube.com/watch?v=K32P5RJXJos](http://www.youtube.com)

</aside>

\* \* \*

:::::::: section
## Exercises

:::: section
### ***Exercise 1: Scraping Data from a Web Page***

Watch this video first, then follow the remaining steps to scrape data from the FDIC Failed Banks list: [www.youtube.com/watch?v=yCSTqxcOrkU](http://www.youtube.com)

1.  Start with this formula:\
    `=IMPORTHTML(“URL”,”table”, 0)`

2.  Add this URL to the formula. This is the page we'll scrape: FDIC Failed Bank List\
    `=IMPORTHTML(“`[`www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/”,“ELEMENT`](http://www.fdic.gov)` HERE”, NUMBER OF ELEMENT ON PAGE HERE)`

3.  Add this type of element to the formula: table and 0\
    `=IMPORTHTML(“`[`www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/”,“table”,0`](http://www.fdic.gov)`)`

4.  Code you enter into cell A1 on the Google Sheet. Just copy and paste this into a Google Sheet:\
    `=IMPORTHTML(“`[`www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/”,“table”,0`](http://www.fdic.gov)`)`

    **\*\*Note:** Depending on your Google Sheets language settings, the delimiter in the function could be "," or ";" It's usually a comma.

5.  One problem: If you go to type on the screen after you scrape, your data disappears. This is because the spreadsheet is linked to the web page. When the web page updates, so does the sheet.\
    `=IMPORTHTML(“`[`www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/”,“table”,0`](http://www.fdic.gov)`)`

6.  To remedy the issue, highlight all the data on the screen and copy it. Then click on the Plus Sign in the lower left corner of the Google Sheet to open a new tab in the spreadsheet. Click on the "Sheet 2" language on the tab to rename it "EDITS" or whatever you want.

    **Pro tip:** You always, always, always work off a COPY of your dataset in case you mess something up.

7.  To paste the data into the new sheet, click into cell A1, then go to the **Edit \> Paste Special \> Paste values only** menu at the top and click (see [Figure 5.11](#ch05.xhtml__15031-5909_ch005_Figure_011)). Presto! Your data appears in the new sheet and is now editable. You still have your original scraped sheet in the first tab.


<a href="#ch05.xhtml_R_15031-5909_ch005_Figure_011"><em>Figure</em> <em>5.11</em></a> Google Sheets pulldown menu


**Learn more:** Practice the formula with these links below. Just paste one over the words URL and then place the entire formula into a Google sheet.

\
`=IMPORTHTML(“URL”,”table”, 0)`

- [www.nifc.gov/fire-information/statistics/wildfires](http://www.nifc.gov)
- [www.fhwa.dot.gov/bridge/nbi/no10/condition19.cfm](http://www.fhwa.dot.gov)
- [https://ourworldindata.org/covid-vaccinations#source-information-country-by-country](https://ourworldindata.org)
- [www.bls.gov/news.release/cpi.t02.htm](http://www.bls.gov)
- [www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list](http://www.fdic.gov)
- [www.prisonpolicy.org/origin/ny/zipcodes.html](http://www.prisonpolicy.org)
- [www.prisonpolicy.org/origin/ny/2020/zipcode.html](http://www.prisonpolicy.org)

\* \* \*

**Scraping PDFs and Images:** Many times datasets are embedded in native or scanned PDFs, such as older government documents or even data that the government doesn't want people to easily access. Data also can appear in photographs.

So that leads to the question: What tools do reporters need to scrape data from PDFs and images? There are many good choices:

- **Tabula:** <http://tabula.technology>
- Tabula is a free tool that you can download to your computer's hard drive. It scrapes tables out of. PDFs and offers strong security and privacy compared to other tools in which you upload a file to a live website.
  - **Training video:** [www.youtube.com/watch?v=eVQ93FTtph0](http://www.youtube.com)
- **[PDFtoExcel.com](https://www.PDFtoExcel.com):** [www.pdftoexcel.com](http://www.pdftoexcel.com)
- Scrape native and scanned PDFs with this free tool. Be careful with security as you are loading your document to a live website that could get hacked.
- **TinyWow:** <https://tinywow.com>
- Dozens of free file conversion tools, including PDF to Excel, converting spreadsheets, video, etc.
  - **Training video:** [www.youtube.com/watch?v=AvdpqJaMCQ8](http://www.youtube.com)
- **CometDocs:** [www.cometdocs.com](http://www.cometdocs.com)

For more data scraping exercises, visit <https://bit.ly/spjdatascrape>

\* \* \*

<aside aria-label="box6" class="box1" epub:type="tip" role="doc-tip" title="box">


::: section

## How to Scrape Data from an Image 

Set up a free account on Google Pinpoint ([https://journaliststudio.google.com/pinpoint](https://journaliststudio.google.com)), then watch the training video to see how to extract data from an image.

[www.youtube.com/watch?v=PYY_WsEXkX0&t=34s](http://www.youtube.com)

</aside>

\* \* \*

::: section
### ***Exercise 2: Chicago Homicides by Year Column Chart in Flourish.studio***

Before starting on the assignment, set up a free account at Flourish.studio. Then follow these step-by-step directions:

- Download the data from this folder: <http://bit.ly/chihomicide>. It's labeled "1chihomicidesbyyear1990--2021.csv" on the far left.
- Open the Column Chart template, hit the upload button in the upper right and upload the data. Click back on the preview tab to see what your data looks like. Note: The horizontal bar chart and line chart templates will work for this as well.
- In the upper left corner, type this into the Untitled Visualization field: Chicago Homicides by Year (1990--2021).
-  In the preview mode, click on the Footer menu on the right side of the interface.
- Place this text in the Title field: Chicago Homicides by Year (1990--2021).
- Place this text in the Text field: Chicago ended 2021 with 797 homicides, the most since 1996. It was 23 more than recorded in 2020 and 291 more than 2019. Chicago had 3,561 shooting incidents in 2021, just over 300 more than were recorded in 2020 and 1,415 more than in 2019.
- Go to the Footer menu on the right side of the page. In the Source: field type: Chicago Police Department. In the Source Link: field paste this link: [https://data.cityofchicago.org/browse?category=Public%20Safety](https://data.cityofchicago.org)
- In the notes section underneath the Source fields, add your credit: Graphic/Your Name.
- Hit the Export and Publish button in the upper right and follow the directions.
  - You also can add a second graphic with a searchable table by loading the same spreadsheet into the Table (default) template on Flourish.
- 10\. Here's what the chart should look like when finished: [https://public.flourish.studio/visualisation/8289582](https://public.flourish.studio)

\* \* \*

::: section
### ***Exercise 3: Datawrapper Choropleth Map***

I first learned this exercise during an online training by John Keefe, editor of weather data at The New York Times. It's one of the best ways to learn how to build a choropleth map.

1.  Set up a free account at <https://datawrapper.de>.
2.  Then download this data slugged Datawrapper COVID counties from this public folder: [https://drive.google.com/drive/folders/1yerJDT8-H34X5orfEgTZU8OccqjEqnAQ](https://drive.google.com)
3.  Then open Datawrapper and choose maps from the Create new project folder.
4.  Then choose the Choropleth Map option on the left side of the page. Now start the build:
    1.  Select USA-Counties (2022) from the list of map templates (should be on the first screen or search for it).
    2.  Load the dataset into the map (note some read columns are special PR codes; not an issue).
    3.  Go to the Match tab and change Values from Column E to Column G (rate). Click the bar to the right side of Column G and make sure Values is selected from the bottom of the pulldown menu ([Figure 5.12](#ch05.xhtml__15031-5909_ch005_Figure_011)).
    4.  Proceed to color palette and set to this: Steps, Natural Breaks (Jenks), categories at 5 and the red-yellow palette, the second from the top of the pulldown menu ([Figure 5.13](#ch05.xhtml__15031-5909_ch005_Figure_013)). Make sure the top setting, Select Column, is set to cases average per 100k.
    5.  Under Annotate, add headline, byline, etc. Here's the link to the source data from The New York Times to drop in the Link to Data field: [https://github.com/nytimes/covid-19-data](https://github.com). Here's how it all should look ([Figure 5.14](#ch05.xhtml__15031-5909_ch005_Figure_014)):
    6.  Now let's fix the tooltips so it shows the right information when you scroll over the counties. Turn on the tooltips toggle at the bottom of the Annotate tab (see [Figure 5.14](#ch05.xhtml__15031-5909_ch005_Figure_014)). Then delete the GEOID code from the top field and hit the blue "+county" button at the bottom to sub in the name of the county. That way people will see the county name and the data when they roll over the county on the map.

    - 7\. Finally, go to the Publish and Embed tab in the upper right corner and select the Visualization Only and Responsive iFrame Settings, then hit the blue publish button. Then copy the link or embed code as needed.

\* \* \*


<em>Figure</em> <em>5.12</em> Example of how to scrape data from a website using a Google Sheet


<a href="#ch05.xhtml_R_15031-5909_ch005_Figure_013"><em>Figure</em> <em>5.13</em></a> Datawrapper choropleth map settings


<a href="#ch05.xhtml_R_15031-5909_ch005_Figure_014"><em>Figure</em> <em>5.14</em></a> Datawrapper choropleth map settings


::: section
### ***Exercise 4: Create a Data Dictionary***

A data dictionary provides a detailed description of the dataset, which includes the meaning of each column, the type of the data and any other relevant information. Let's make one with a simple dataset:

- **Prompt:** Make a data dictionary with the following dataset, then paste the header and first 8--10 rows of data into ChatGPT.

Now try it yourself. Here's a practice dataset of bridge inspections: <https://bit.ly/bridgedataset>

Copy the first eight rows and paste after the prompt: Can you make a data dictionary with the following dataset:

Or paste this after it if you're using the ebook:

+---------------+-----------------------------+--------+--------------------------------------+-----------+
| *State*       | *Bridge Counts*\            |        | *Bridge Area (Square Meters)*\       |           |
+---------------+---------+---------+---------+--------+------------+------------+------------+-----------+
|               | *All*   | *Good*  | *Fair*  | *Poor* | *All*      | *Good*     | *Fair*     | *Poor*    |
+===============+=========+=========+=========+========+============+============+============+===========+
| ALABAMA       | 16,162  | 6,740   | 8,768   | 654    | 9,892,013  | 3,660,437  | 5,987,624  | 243,952   |
+---------------+---------+---------+---------+--------+------------+------------+------------+-----------+
| ALASKA        | 1,595   | 706     | 744     | 145    | 745,016    | 285,999    | 401,686    | 57,330    |
+---------------+---------+---------+---------+--------+------------+------------+------------+-----------+
| ARIZONA       | 8,320   | 5,098   | 3,085   | 137    | 5,875,021  | 3,193,076  | 2,598,212  | 83,732    |
+---------------+---------+---------+---------+--------+------------+------------+------------+-----------+
| ARKANSAS      | 12,902  | 6,598   | 5,678   | 626    | 6,807,904  | 3,293,464  | 3,207,207  | 307,234   |
+---------------+---------+---------+---------+--------+------------+------------+------------+-----------+
| CALIFORNIA    | 25,771  | 13,707  | 10,267  | 1,797  | 30,105,500 | 16,365,750 | 11,584,467 | 2,155,282 |
+---------------+---------+---------+---------+--------+------------+------------+------------+-----------+
| COLORADO      | 8,785   | 3,550   | 4,769   | 466    | 5,059,489  | 2,328,947  | 2,469,248  | 261,294   |
+---------------+---------+---------+---------+--------+------------+------------+------------+-----------+
| CONNECTICUT   | 4,336   | 1,256   | 2,805   | 275    | 3,439,401  | 590,320    | 2,498,953  | 350,127   |
+---------------+---------+---------+---------+--------+------------+------------+------------+-----------+
| DELAWARE      | 879     | 248     | 603     | 28     | 1,018,350  | 193,808    | 769,982    | 54,560    |
+---------------+---------+---------+---------+--------+------------+------------+------------+-----------+
| DIST. OF COL. | 244     | 60      | 174     | 10     | 566,541    | 74,311     | 437,114    | 55,116    |
+---------------+---------+---------+---------+--------+------------+------------+------------+-----------+
| FLORIDA       | 12,518  | 8,279   | 3,878   | 361    | 17,673,167 | 11,507,507 | 5,855,382  | 310,278   |
+---------------+---------+---------+---------+--------+------------+------------+------------+-----------+
| GEORGIA       | 14,940  | 6,796   | 7,703   | 441    | 10,336,351 | 5,189,559  | 4,938,988  | 207,804   |
+---------------+---------+---------+---------+--------+------------+------------+------------+-----------+

**Result:** You should get a table with a perfect dictionary of header terms, examples of the data and measured distance.

\* \* \*

::: section
## Footnotes

These resources do not include links from the exercises and training videos.

- 2020 COVID-19 Cases by State and Country: [https://public.flourish.studio/story/690567/?utm_source=embed&utm_campaign=story/690567](https://public.flourish.studio)
- American Journalism Review: How Journalism Professors Used Legos to Teach Super Bowl Data Visualization: [https://ajr.org/2015/02/02/journalism-professors-used-legos-teach-super-bowl-data-visualization](https://ajr.org)
- BBC: COVID-19 in the UK: [www.bbc.com/news/uk-51768274](http://www.bbc.com)
- Canva: <https://canva.com>
- CBS Chicago: More Than 7,000 Kias and Hyundais Have Been Stolen in Chicago: [www.cbsnews.com/chicago/video/more-than-7000-kias-and-hyundais-have-been-stolen-in-chicago-this-year/#x](http://www.cbsnews.com)
- Chartbeat: Most Engaging Stories of 2020: [https://blog.chartbeat.com/2020/12/22/most-engaging-stories-2020](https://blog.chartbeat.com)
- Data + Journalism Blog: DEI and Data Journalism: [https://dataplusjournalism.com/2023/01/02/bonus-chapter-diversity-equity-and-inclusion-in-data-reporting](https://dataplusjournalism.com)
- Datawrapper: [www.datawrapper.de](http://www.datawrapper.de)
- Eurostat: [https://ec.europa.eu/eurostat](https://ec.europa.eu)
- Flourish: <https://flourish.studio>
- Global Investigative Journalists Network Resource Center: [https://helpdesk.gijn.org/support/home](https://helpdesk.gijn.org)
- Google Chrome Store: [https://chrome.google.com/webstore/search/web%20scraping](https://chrome.google.com)
- Google Dataset Search: <https://datasetsearch.research.google.com>
- Google MyMaps: <https://mymaps.google.com>
- Google Public Data Explorer: [www.google.com/publicdata/directory](http://www.google.com)
- Infogram: <https://infogr.am>
- Journalist's Toolbox Data Journalism: [www.journaliststoolbox.org/category/data-visualization-and-online-tools](http://www.journaliststoolbox.org)
- Journalist's Toolbox Public Records: [www.journaliststoolbox.org/category/public-records](http://www.journaliststoolbox.org)
- Lucid Charts: What Is a Venn Diagram?: [www.lucidchart.com/pages/tutorial/venn-diagram](http://www.lucidchart.com)
- OrgCharting: What Is a Hierarchy Chart: [www.orgcharting.com/what-is-a-hierarchy-chart](http://www.orgcharting.com)
- Our World in Data: <https://ourworldindata.org>
- Pew Research Center: [www.pewresearch.org](http://www.pewresearch.org)
- ProPublica: Driven into Debt: [www.propublica.org/series/driven-into-debt](http://www.propublica.org)
- Treemap: Chicago 2022 City Budget Graphic: [https://public.flourish.studio/visualisation/8988206](https://public.flourish.studio)
- [USAFacts.org](https://www.USAFacts.org): <https://usafacts.org>
- WBEZ Chicago: Chicago's Towing Program Is Broken: [https://interactive.wbez.org/brokentowing](https://interactive.wbez.org)
- WBEZ Chicago: Lawsuit Challenges Constitutionality of Chicago's Car Impound Program: [www.wbez.org/stories/lawsuit-challenges-constitutionality-of-chicagos-car-impound-program/c29c21ef-abcd-482d-b890-257a942fc73f](http://www.wbez.org)
- WBEZ Chicago: Tens of Thousands of People Lost Driver's Licenses Over Unpaid Parking Tickets. Now, They're Getting Them Back: [www.wbez.org/stories/illinois-governor-pritzker-signs-law-ending-license-suspensions-for-parking-tickets/5da945db-08a0-4690-9a04-8f5f2f9c5904](http://www.wbez.org)


# 6 Mobile Journalism

DOI: [10.4324/9781003431787-7](https://doi.org/10.4324/9781003431787-7){aria-label="D.O.I. link to this document."}


**Key Resources**

- Smart Film School: [www.smartfilmschool.com/](http://www.smartfilmschool.com)
- The Smart School platform, founded by "Mobile Journalism" author Robb Montgomery, delivers certificate-level courses in mobile journalism, digital storytelling and smartphone video production that are used by universities, journalists, broadcasters, and media development training programs worldwide.
- Luma Fusion and VN Video Editor apps

\* \* \*

Shortly after the iPhone debuted in 2007, Robb Montgomery stood on a stage in Egypt, pulled his shiny new iPhone out of his pocket and told the audience that "this is the most powerful reporter's notebook ever invented."

Although BlackBerrys and other PDAs, as well as video phones, had been on the market years before Montgomery stepped on that stage, he saw the iPhone's potential. Some reporters had already practiced "backpack journalism" -- carrying small point-and-shoot cameras, an HDV camcorder, a Zoom H4 audio recorder and a laptop -- dating back to the early 2000s.

But the iPhone -- along with the Androids and other smartphone competitors -- changed everything. Now journalists carried a mobile newsroom in their pockets. They could document history with the push of a couple of buttons. It was truly a game-changer and still is 17 years later.

"The tools have gotten smaller and far more capable, but the opportunities for journalists to go out into the field to find, capture, edit, script and transmit a story without ever returning to the newsroom are the same," said Montgomery, author of two journalism textbooks: "Smartphone Video Storytelling" and "Mobile Journalism." "It is the fluency with picture language that is missing from most reporters' toolkits, not the tech."

When the iPhone debuted, the camera was "probably the worst feature of it," said Montgomery, a former Chicago newspaper editor who now teaches mobile documentary and short-form storytelling at his Smart Film School, which has served thousands of journalists from news organizations from India, Europe, the United States, Asia and the Middle East since 2015.

"It's the exact opposite of where we are now," he said. "With something like iPhone 13 ProMax, you have the ability to do amazing cinematography, documentary journalism, photojournalism and broadcast radio reporting -- whatever you want to do."

In this chapter, you'll learn how to use a smartphone to record video and audio, what apps to use to cover news stories, how to manage your mobile workflow, how to organize apps and how to build stories for a mobile audience.

::: section

## Mobile Journalism: Past, Present and Future

Before exploring where journalism is headed with mobile journalism, it's important to first understand its roots. Photojournalists have been using portable tools since the 35mm Leica camera hit the market in 1913. It gave reporters freedom to capture news from nearly anywhere.

As technology progressed, cameras became lighter. Video cameras meant news could be documented remotely and not shared only from a studio news desk. By 1940, RCA released the Walkie-Lookie, the first black-and-white portable camera that let journalists record what they saw on tape.

Over the years, the technology got better -- and smaller. By the early and mid-2000s, small HD cameras, video cams like the Sony Bloggie Cam and the DSLR cameras were widely used by journalists and the public. Technology is improving at a rapid pace, but Montgomery says that if you want to get good at "mojo," journalists should remember that it's not about the technology.

"The tech is only going to get better," Montgomery said. "It's never going to go back. Technology never, ever marches backward."

Mobile market data supports that perspective. As of 2022, there were more than 6.8 billion smartphone users worldwide (Statista, 2022). With the global population at 8 billion, that means a smartphone penetration of more than 80%. The number has increased rapidly: In 2016, there were 3.7 billion smartphone users, meaning the number increased by 86.5% in just seven years. Mobile commerce sales hit \$3.56 trillion by 2021.

Since 2013, mobile traffic began to surpass desktop traffic for many websites, including news sites. News audiences wanted their information on the go, which opened opportunities -- and challenges -- for journalists. While journalists are encouraged to write short, tight, stories for mobile, a 2016 Pew Center report found long-form stories actually perform better with mobile audiences.


<em>Figure</em> <em>6.1</em> Chart of U.S. cellphone and smartphone ownership from 2011 to 2021 <em>Source:</em> Pew Research Center. (Chart/Mike Reilley)


Pew studied 117 million mobile phone interactions on content from 30 news websites. It found that readers spend more than twice the amount of time reading and scrolling through articles longer than 1,000 words than they do short-form stories, according to the book "Mobile-First Journalism" (Routledge, Hill and Bradshaw). The study also said readers spent more time with longer content in the morning than in the evening.

Smartphones give everyone a chance to document history's rough draft. Mobile journalists are often the first to respond when covering crisis situations. Many of them blend into the crowd and don't stand out like a news crew.

Journalists, as well as eyewitnesses, can record breaking news stories from a variety of angles and perspectives. That's what makes crowdsourcing, which we explored in [Chapter 4](#ch04.xhtml__15031-5909_ch004), so important. Showing more perspectives on a story gives the reader better context.

During the George Floyd protests in Minneapolis and Chicago in 2020, video footage and photos from witnesses and the protesters themselves showed a much different perspective from video that the media or even police body cameras provided. Media showed wider shots. Protesters were in the trenches and shared video of police violence. Police social media accounts shared video of protesters assaulting police officers. One story, several perspectives.

The portability of smartphones gives journalists greater versatility to tell breaking news stories from the field. Instead of loading photos onto a laptop and posting to a website, the images can be shared immediately from the phone. Marc Settle, smartphone reporting trainer at the BBC College of Journalism, says the phones have reduced backpack journalism to a small bag containing a microphone, a tripod and some additional storage. A hotspot and extra battery is helpful, but really only three things are vital -- a phone, tripod and microphone.

Mobile-first thinking has been popular in Europe and many countries around the globe, but has been slow to gain footing in the United States, which still clings to more traditional online and broadcast storytelling. Still, many see the potential ... and progress.

Montgomery has taught mobile journalism workshops and courses in broadcast, print and digital newsrooms in more than 30 countries, and he sees a wide gap in the adoption rate globally. In Germany, the United States and other "tech-centric meccas" for journalists, mojo has not really taken off yet.

"In Asia, Latin America, France, Austria, U.K., Spain, Africa, Austria, Italy and Scandinavia, mojo is a well-known and practiced mode of operating in the field for top-end broadcasters and everyone else for that matter," he said. "The mojo storytelling obstacles for reporters of almost every stripe that I have worked with are the same.

"Their main obstacles are a lack of visual storytelling literacy rather than a lack of tech fluency."

Still, there's hope in the United States and beyond.

In a 2022 Harvard Nieman Lab post, Columbia University professor and visual journalist Mario Garcia predicted more newsrooms would go mobile-first in the coming years: "While there has been tremendous progress over the past year in gearing content to mobile devices, it's still a challenge -- one that will determine how successfully media houses across the planet can become mobile-first newsrooms, leading to more creation of stories crafted for mobile consumption, which in turn lead to higher retention levels and, of course, more subscribers.

Garcia wrote that the transition will require two things:

1.  **Restructuring the newsroom:** Doing so would incorporate more content managers whose main job is to follow stories, updating them as needed and using more video and audio as accessories to enhance content.
2.  **Incorporating new blood into the mix:** The majority of those making news content decisions should be digital natives. They understand that, in a mobile world, they don't follow editions -- but rather concentrate on stories and how to keep them constantly updated for those mobile readers who lean forward into their phones at all hours of the day and night.

::: section
## Visual Storytelling and Mobile Journalism

Montgomery said the key to visual storytelling is to understand the language behind the technology -- the language of filmmaking.

"That's why I love to teach this language to journalists because once you understand the language, then you begin to write," he said. "You have to learn how to speak and you have to learn how to listen to it."

To do this, you must learn to write to images, both still and moving. So once you have the photos and video in hand, you can write a script or do an on-the-fly voiceover to provide details that the multimedia cannot.

"Mojo kind of flips the script on you and says: No Picture, No Story," Montgomery said. "So we start out by learning how to report in pictures as a photojournalist, then working with shots as a filmmaker, and then learning how to write with those pictures like an editor, and then writing to those pictures like a scriptwriter.

"And that process is powerful. That allows you to practice it every day because the phone is in your pocket. The tech is always there. The apps are either free or low cost. Really, the reason for illiteracy is not the tech."

In his workshops, Montgomery helps journalists to produce compelling, visually led stories with their phones by adopting a simple workflow:

- Report *in* pictures first
- Then write *with* pictures
- And lastly, write *to* pictures

"In newsrooms where this reporting flow is understood as a standard reporting mode," he said, "reporters, editors and producers are better equipped to exploit the potential of the story forms that mobile journalism unleashes."

Montgomery followed that approach when building his award-winning "Ice Swimming" video during a 2018 training trip to Helsinki, Finland.

In the 91-second video, he uses slow-motion shots, still images and other video to show people climbing into the cold and hot pools while one of the participants narrates the story. He matches the videos and images up to the words the narrator says.

For example, when she mentions saunas, Montgomery uses a clip of people walking to the saunas. When she talks about climbing in and out of the cold pool, he has footage of that. When she talks about the warm pools, he has a shot of the steam rising off of one. The piece was honored as the "Best Film Shot on a Smartphone" at the Sunlight International Film Festival in 2019 in Berlin, and was a finalist at many other competitions.

"That's powerful to be able to write with pictures, and then be able to write to pictures whether you have a voiceover or you have text over video," Montgomery said. "Text and sequences, news stories told like this, are not something that were invented in the social media age. They're more than a century old."


<em>Figure</em> <em>6.2</em> Screenshot from Robb Montgomery’s “Ice Swimming” video, including closed captioning


Montgomery used the video and clips as a training example for the Nordic Press Association on that trip. He had never had a source do a voiceover to video and images before. He told the woman in the story that the "pictures are now going to interview you" and had her watch the video as she spoke.

"Mojo unlocks new ways of thinking because there are no limitations," he said. "You're looking at a sequence you're like, 'You know what, I could do a voiceover or I could do the traditional broadcast thing.' I could ask you to write a script and you will go through and make it very methodical.

"But I wanted something that was a little bit more immediate. And my sense was that if it was immediate, \[it\] might have some more emotional body and it worked. She just recorded what she saw and what she remembered in the movies. It was the pictures interviewing her."

\* \* \*

::: section

## Producing Smartphone Video

Early in the semester, I do a lecture with my students called "The 10 Commandments of Shooting Mobile Video." The training is built off a digital video training presentation Al Tompkins did at the Poynter Institute in St. Petersburg, Florida, in 2010. I always liked the framing for this lecture -- I do my best Charlton Heston impression -- but some of the tips and tricks have changed over the years as mobile phone camera technology improved.

My latest version of the 10 commandments:

1.  **Thou Shalt Not Zoom with Thy Lens.** Zoom with your feet, not the lens. Move closer to your subject and frame the shot. You'll get better-quality video and audio. Use the lens zoom on your phone only if you're in a restricted area and can't get closer to the subject. Remember, you're after sequences: wide, medium and close, so you'll want to move around a lot and shoot a variety of distances and angles.

    Think about the makeup of a story as sequences:

    1.  50% closeups
    2.  25% medium shots
    3.  25% wide shots

    The key is to shoot tightly and get those close shots.\
    A great example of shooting in sequences is this digital video about Mexican grey wolves produced by Laura Sposato, one of my former students at Arizona State's Cronkite News Digital Production Bureau. Sposato produced a video entirely narrated by the source and mixed in that range of sequences. Like Montgomery, she tied the audio to the video at key transitions. She used both an iPhone and a DSLR camera when shooting.

2.  **Thou Shalt Compose Thy Shots on the Thirds:** Your smartphone allows you to turn on the thirds framing option (it varies by type of phone). The intersecting lines on the third should have key elements of the shot. If you're shooting someone in an interview, don't center them in the shot. Instead, have them off to the left or right a little bit, so their face intersects with the upper thirds (see [Figure 6.3](#ch06.xhtml__15031-5909_ch006_Figure_003)).

3.  **Thou Shalt Keep Thy Shot Steady for at Least 10 Seconds With B-Roll.** Bring a tripod, even if you don't think you'll need it. If you don't have a tripod, use your elbows on a table to form a tripod. Or hold your elbows close to your body to stabilize the shot. Smartphones are heavier than you think, and after about 30 seconds, your hands will begin to shake.

4.  **Thou Shalt Think in Terms of Context, Not Just Soundbites.** Be careful with editing too tightly. Quotes can be edited down so tightly that it changes the meaning of what the person was saying. Remember to edit to the full context of what was being said, even if you have to paraphrase in a voice-over.

5.  **Thou Shalt Shoot a Variety of Angles.** Sposato's video was a classic example of this step. But the rule also applies when shooting and editing interview videos. Try not to cut off the top of a source's head or make them look squat when framing the shot. When you must frame a body, frame it in logical places, such as the waist, not the ankles, elbow or wrists.\
    And apply the rule of thirds -- one-third of the frame above the eyes, one-third below the neck. The space at the bottom is especially important if you're going to identify the source in lower-third text underneath their face. You don't want the text to run over the lower part of their face.

6.  **Thou Shalt Focus Thy Story Into Three Words.** "Who Did What?" or Noun-Verb-Object. It's a simple way to start the editing process. My students are sometimes overwhelmed by all of the video they have. That's a good thing, because they can be selective with edits and what they want to use in the story. But editing an hour of content into a three-minute mobile video can be daunting. Start with "who did what," then decide how you want to organize it: narrative, timeline, process, chapters, etc. Once you have that organizational structure, editing becomes much easier.

7.  **Thou Shalt Always Wear Thy Headphones When Recording and Editing.** I'm stunned by how many students don't wear headphones or at least ear pods when recording. If you don't have headphones, at least do some test audio before starting the interview.

8.  **Hold Thy Camera the Right Way.** Hold it vertically if you're shooting video for social channels, which use "vertical video." But if you're shooting for TV or YouTube, hold the phone horizontally. An easy way to remember it is, your TV sits horizontally, so should your phone.

9.  **Thou Shalt Seek Great Natural Sound and Not Talk While Shooting.** Over the years, I learned that I often said uh-huh as I interviewed people. This was OK as a newspaper journalist, though it probably annoyed some of my sources. But when I started to use my audio for the web, it was a catastrophe. I made an easy adjustment: Rather than speaking, I just nodded my head to show the sources that I understood what they were saying.\
    The same holds true with background noise. Interviewing someone near an elevator? Move away as the ding and the bustle from people getting on and off the elevator is distracting in the background. Avoid loud air conditioners, traffic, anything that can ruin the audio, unless you have no choice.

10. **Thou Shalt Put the Camera on the Shadow Side of the Subject.** Pay attention to perpendicular lighting that's coming from the sides of your subject. Move to the darker side of their face and shoot from that angle. If you shoot from the lit side, the opposite side of their face will look dark and sinister.


<a href="#ch06.xhtml_R_15031-5909_ch006_Figure_003"><em>Figure</em> <em>6.3</em></a> Mobile journalist Rob Layton uses the rule of thirds to frame his shot <em>Source:</em> Photo/Rob Layton


<em>Figure</em> <em>6.4</em> How to hold your smartphone <em>Source:</em> Illustration by Billy O’Keefe


I also remind students to bring a lens cloth to keep the lens clean (don't use your shirt) and to set the phone to airplane mode so incoming calls and alerts don't interrupt the video. Montgomery has these tips and many more in a poster you can hang in your newsroom or classroom ([Figure 6.5](#ch06.xhtml__15031-5909_ch006_Figure_005)).


<a href="#ch06.xhtml_R_15031-5909_ch006_Figure_005"><em>Figure</em> <em>6.5</em></a> Robb Montgomery’s smartphone video tips


::: section
## Ten Types of Mobile Video

In his book "Mobile Journalism", Montgomery focuses on 10 kinds of mobile videos that journalists can make with mobile devices. The most-common forms are as follows:

- **Quick Hit:** Short pieces of multimedia shot and produced in the field. It can be a quick scene or a short interview edited into a social media clip for Twitter, Instagram Stories, TikTok or SnapChats. This also can be some raw video from a breaking story.
- **Livestream:** Typically from a breaking news scene, this video is streamed over the reporter's phone to a livestream embed on a website or through a social media channel, such as Facebook Live or Twitter. Reporters will often narrate the video for a breaking story, unless it's a stream of a live interview or press conference.
- **Demonstration:** This type of video shows a process: how a chef makes a dish, how a bartender builds a cocktail, or how a musician plays a song. Try to think of stories that follow step-by-step processes.
- **Explainer:** This approach provides background on a complex issue, such as a whiteboard video explaining how mail-in voting works (built with the VideoScribe app). They typically display a sequence of events to provide a quick overview.
- **Kinogram:** This is a text-over-video approach that became popular during silent movies. It works well with short mobile videos as the text narrates the story if the audio quality is poor for some reason. You can layer in some rights-free music in the background to give the video a little more flavor.
- **News package:** These are shot as a traditional newscast video and features a reporter's voice-over, sound bites and visual sequences. The reporter also may do a stand-up introduction and close on the video.
- **Walkthrough:** The reporter acts as a tour guide of sorts through a scene, which can be done through video clips, selfie filming or a wide shot. The reporters narrate the scene as they walk through it.
- **Graphical:** A "by the numbers" story that can include charts, maps and other graphics to explain the issue. Whiteboard videos work well here, as well as slideshows in Flourish.studio, which you can play through as a slideshow and narrate as the graphics pop up. All you need to do is record your desktop on Quicktime Video or another screencasting tool, such as Screenr or Screencast-o-matic
- **Slideshow:** If you have a strong mix of photos and videos, slideshows are a great way to tell a story. I combined the slideshow approach with a timeline to show how an old building was torn down next to my home and a new, 10-floor apartment complex was built there.
- **Short documentary:** The most-demanding of all the approaches, these videos can last up to several minutes. The reporter uses visual sequences, natural sound and interviews with sources to build the video along with graphics and some text.

When you pitch a story idea to editors, think in terms of these types of videos to have a plan going in. Think of a "shot sheet" of sequences you can shoot. But also be flexible; many times my students returned from shooting a video and shifted to a new type of video format during the shoot. Let the content dictate the format, not vice versa.

:::: section

## What's in Your Bag? Mobile Gear

Phone, battery/charger, tripod/mount and microphone are the essentials, but Montgomery's gear kit also includes a grip that securely attaches your phone to any tripod, large or small, to keep shots stable. He also suggests using a lapel mic that can attach to your subject, and a facelight or reflector to illuminate your subject.

Røde Vlogger kits are useful for capturing good sound, and it also includes a small LED light, Montgomery said. Røde, Sennheiser and Shure microphones all produce great audio, he said. For iPhones, he recommends adding the Røde SC6-L two mic adapter.

A basic mobile kit can be relatively inexpensive if you watch for online sales, anywhere from \$200 to \$300 maximum. Kodak's lightweight tripods run \$30 and include a carrying case.

The gear is lightweight and easily fits in a small bag, making it appealing to journalists who travel or are working in remote areas and poor conditions.

\* \* \*

<aside aria-label="box1" class="box1" epub:type="tip" role="doc-tip" title="box">

::: section
## Settings for an iPhone's Native Camera 

Rob Layton, Assistant Professor of Mobile Journalism at Bond University in Gold Coast, Australia, said the most important app for any visual journalist is the native camera. He advocates for this ahead of third-party apps because it's an essential starting point.

"Journalists should understand what the native camera can do and set it up for their needs," he said.

"For example, Apple users should go to Settings \> Camera and explore the list of options. Under Formats, decide whether you need High Efficiency or Most Compatible. High Efficiency will use Apple's proprietary HEIF/HEVC format, which will reduce file size for sending but the files may not be compatible with non-Apple devices.

"Most Compatible will do as it says but image quality will be reduced. Another tip, while exploring Camera Settings, is to set video frame rates to match the country's electricity hertz cycle. This will avoid lights flickering in the video. For example, in Australia -- and most of the world -- the hertz cycle is 50hz per second, so set the frame rate to 25 as it is evenly divisible into 50.

"In the U.S., it's 60hz, so set the frame rate to 30. Further, look at the actual camera app and understand the functions. With Apple devices, tap and hold the screen to lock exposure and focus. Then, run a finger up or down to adjust exposure.

"You also need to understand the different focal lengths of each of the phone's cameras and how they will serve the story: ultra-wide/wide for establishing shots, 2x for medium shots, 3x for narrow field of view and bringing far objects closer. Once the native camera is understood, move on to more professional video camera apps, such as Filmic Pro, Cinema P3, BeastCam and Mavis."

</aside>

\* \* \*

:::: section

## What's Next? Wearables and ... Bikes?

Layton is using smartphones, Apple Watch and other mobile technology to document stories in new ways along Australia's Gold Coast. A surfer, journalist and educator, he incorporates mobile concepts and hands-on training into his classes at Bond University as well as his documentary projects.

For the past few years, Layton has been syncing the Apple Watch with his iPhone, iPad, laptop and other devices to produce incredible images in places you cannot shoot with a traditional tripod set-up. He mounts them to surfboards, his car's mirror and other places. The Apple Watch lets him zoom, set exposure and take photos without touching the iPhone, iPad, etc.

"The watch has really become an integral part of my mobile journalism workflow," he said. "I really struggle to think how I ever live without it.

"I use a watch as a remote for the native camera and for the filmic Pro app, which is probably the main reason that you would use your watch in mobile journalism. But I also use my watch for a lot of instant information. I'm working on a documentary about surfing so I need to know weather conditions at any given moment. My watch face is filled with at-a-glance information, such as sunrise and sunset times, wind strength and direction, swell size and direction, tides, all the conditions I need to know. Journalists should arrange their watch faces to reflect their areas of expertise."

Layton uses the Apple Watch app on iPhone to install the native camera interface to the watch face. That makes it possible for him to adjust some settings directly on Watch by tapping the three dots next to the shutter button, such as Live photos, HDR or swapping rear and front cameras. It also enables setting a timer, which is handy for quick behind-the-scenes shots. However, most settings should be done through the phone app itself.

Other features the watch provides:

- Use a Watch remote to frame yourself if you're doing a piece with a camera. Often solo journalists need to press record, then step in front of the phone for a moment, stop recording and playback to see their positioning. Apple Watch remote allows you to frame up in real time.
- On the native camera you tap and hold the screen to lock focus and exposure, and then run your finger up or down to adjust exposure. Once you have yourself framed, it is possible to set the focus and the exposure directly on the watch, but it's not possible to adjust exposure. It's best to do this directly on the phone first.
- It's also possible to toggle through the phone's cameras by turning the watch's crown dial.

The BBC is experimenting with mobile journalism in a different way. In the spring of 2023, it launched a "Bike Bureau" for green broadcasting. The modified electric cargo bike has a desk, several mounts for mobile cameras, microphones and lights. The desk provides a stable surface for a laptop or iPad if the reporter is doing a remote standup. It's designed for solo-operated and solar-powered TV and radio live reports, as well as other newsgathering tasks.

Montgomery said the bike bureau has potential with newsrooms large and small.

"If you don't have the BBC's budget, you've just got a waterproof bike bag, a tent and a German touring bike, and you're set," said Montgomery, who documented his own 1,000-kilometer bike trek in "The Grand Budapest Bike Tour." "You can get going for less than 100 bucks."

\* \* \*


<em>Figure</em> <em>6.6</em> Rob Layton’s iPhone rig to a sailboat (left) and the image it produced (right)


<em>Figure</em> <em>6.7</em> Using the Apple Watch to change settings and shoot images on a car-mounted iPhone <em>Source:</em> Photo courtesy Rob Layton


<aside aria-label="box2" class="box1" epub:type="tip" role="doc-tip" title="box">

::: section
## Jeremy Caplan: Seven Key Apps to Have on Your Smartphone 

Caplan, CUNY professor and author of the Wonder Tools newsletter, lists his five critical phone apps he uses regularly:

Google Photos is great not just for viewing and backing up my photo library but for sharing images and printing photo books.

Seek and Picture This are great nature apps for identifying animals and plants.

Wakeout is excellent for mini exercise breaks during the workday.

Snipd is my podcast app of choice, with a unique feature that makes it easy to highlight, save and share the best moments of whatever you're listening to.

Substack is what I use to publish my newsletter. I rely on the mobile app to read dozens of other Substacks and to publish Notes, short Tweet-length thoughts and curated tidbits. Along with Readwise Reader, it's where I do much of my online reading.

</aside>

\* \* \*

::: section

## Apps, Apps and More Apps

This book's introduction offered tips for managing your apps and organizing your mobile life using periodic check-ins to delete unused apps, erase photos, video and audio off your phone or storing them in apps like Google Photos. Google Drive or other multimedia servers.

It's also important to measure your screen time. My iPhone sends me weekly updates on whether my screen time is higher or lower than the previous week. Journalists also should organize their apps in a way that makes sense to them, so they can find them quickly without having to search for them.

If you have a lot of apps, like I do, you should organize them into folders by type of tool. This helps you stay organized and can easily access more of your most-used apps by simply tapping once to open the folder and once to open the app. If you leave your apps all over your phone, you'll have to swipe through many screens before finding what you need. The search field requires you to type, which also causes delays. So if you're using your phone for covering breaking news, I strongly recommend that you organize your apps similar to folders.

\* \* \*


::: section
## Sports Coverage: Four Key Apps from ESPN's Adam Rittenberg

Besides [Otter.ai](http://Otter.ai) for transcriptions, Rittenberg uses four phone apps for reporting on national college football issues for ESPN. Here's how he uses them:

- **YouTube:** The video archive helps on a number of levels, from press conferences or one-on-one interviews to game highlights or specific plays that I'm writing about. I will always watch coaches I don't know well to get a sense of how they approach the media and interviews, and how they conduct themselves in games. YouTube can be particularly helpful for older games or news broadcasts.
- **Instagram:** Many college athletes use IG as their preferred platform for major announcements, like whether they will stay in school or go to the NFL draft, or their transfer destinations. Although I am not active on IG, I will monitor it along with Twitter and other platforms to ensure we don't miss any major news items.
- **iTunes/Apple Podcasts:** The access these apps provide to notable podcasts are helpful to not only keep up with major storylines around college football, but research for specific stories. I can also listen to full-length interviews with coaches, players, administrators and other key figures around the sport.
- **Twitter:** I have a fairly large base of accounts I follow, which includes teams, coach accounts, athletes and many key media members, both national and local/regional. Twitter is particularly helpful during Mondays and Tuesdays of game weeks, as many coaches hold their main news conferences. I also use Twitter for post-practice updates, key in-season and offseason meetings, and to monitor major personnel announcements.
- College football has become much more transactional with the transfer portal, so following key players on social media -- or the media members who cover them -- is essential to keep up. Twitter is also very important in the recruiting space. Although I don't cover recruiting 24/7, I want to keep up with key commitments and signings, especially heading into the December signing period.
- **ESPN/Fox Sports/CBS Sports/NBC Sports:** I have to monitor as many key games as possible during college football Saturdays, and these apps help me keep track. I can watch live broadcasts or replays, as well as highlights of plays or press conferences generating the most interest/traction.

\* \* \*

:::: section

## Apps for Journalists

This is by no means a comprehensive list of apps for journalists. A reporter's or photojournalist's needs for apps vary by beats, platform and personal taste. New apps come to market every week, so there's always a new tool to try.

Most of the apps listed here are free, but a few will cost a few bucks. But if you think you will use them often, it will be money well spent. Always remember to check the iTunes or Google Play stores for updates. This will add new features to your apps and fix any bugs.

::: section
### ***Video and Audio Recording and Editing***

- **Video shooting:** Filmic Pro (iOS and Android)
- **Video editing:** Luma Fusion (iOS only, \$29), VN Video Editor (iOS and Android and free and a paid upgrade), Kinemaster (iOS and Android), VLLO, CapCut, PowerDirector, Alight Motion, FilmoraGo, Ferrite
- **Adobe Premiere Rush:** Basic video editor; a step up from iMovie app
- **VidStitch:** Build cool collage videos (think Brady Bunch opening or Zoom)
- **DoubleTake:** Record video with the front and rear cameras at the same time
- **Clips:** Add text to live video (vertical video only)
- **Clipomatic:** Add text to recorded video (vertical video only)
- **Quik:** Great video editing app from GoPro
- **Magisto and Flipagram:** Build/edit videos and audio slideshows in these easy-to-use apps
- **Emulsio:** Video stabilization app; intuitive to use -- just load your video and adjust settings
- **Mojo:** Video slideshows for Instagram stories
- **Audio recording:** Voice Record Pro (iOS), RecForge Lite (Android)
- **Audio editing:** Ferrite (iOS only), Hokusai, Anchor, Audio Evolution Mobile Studio (Android)
- **Stills photography:** VSCO (iOS, Android)
- **Photo editing:** Snapseed (iOS, Android)
- **Slideshows:** Inshot (slideshows), Adobe Spark Video, Storyline
- **Summary:** Luma Fusion is the Ferrari of mobile video editing apps. It's costly, but the interface resembles Adobe Premiere for desktop and you can do detailed editing. It's worth the cost. But if you're cash-strapped, try VN Video Editor, which has both free and paid versions. The basic free version offers many of the basic editing tools you'll need: layers, text, audio, music, transitions, export, etc.


<em>Figure</em> <em>6.8</em> The DoubleTake app in action <em>Source:</em> Photo courtesy Robb Montgomery


\* \* \*

::::::::: section
## Videos: How to Use Multimedia Editing Apps

- **VN Video Editor:** [www.youtube.com/watch?v=vQV743JqvnE](http://www.youtube.com)
- **Hokusai (Audio):** [www.youtube.com/watch?v=6NjzojQE2o0](http://www.youtube.com)
- **Anchor (Audio):** [www.youtube.com/watch?v=tr8deLLg4bw\*\*\*](http://www.youtube.com)

::: section
### ***Reporting***

- **Notability**
- Create a reporter's notebook on your phone. Catalogs everything -- photos, notes, video, etc.
- **Otter.ai**
- Transcribe audio in an instant. [Chapter 1](#ch01.xhtml__15031-5909_ch001) covers how to use this tool, and its benefits and drawbacks.
- **Police Radio**
- This app allows you to listen to police, fire and rescue and other emergency calls in several cities across the country, including Chicago. It may not be perfect, but it beats lugging a police scanner around.
- **ZIP Finder**
- Not sure of a city or neighborhood's ZIP? Find it here. Also: Google it.
- **The basics: Dictionary, Thesaurus, Factbook, Wolfram Alpha**
- Look things up quickly, fact-check, etc.
- **CalcBot 2 (formerly Convertbot)**
- Great tool for converting heights, weights and other measurements. I use it several times a week along with the calculator. Great for quick fact-checking on stories, too.
- **WeatherBug**
- I like the interface better than the Weather Channel's.
- **FlightTrack**
- Helpful for journalists who travel. I've found it to be very accurate for my flights the few times I've used it.
- **AP Stylebook**
- Some journalists like this app, which costs \$30, because it updates each year and they don't have to buy new print stylebooks. I prefer the online desktop or the print version as they're a little easier to use -- and are a few dollars cheaper.
- **Summary:** CalcBot is very useful for data journalists, and its interface provides greater versatility on the fly than just typing a conversion or math problem into Google. WeatherBug and FlightTrack are must-haves for any journalist traveling.

::: section
### ***Photography, Photo Editing and Effects***

- **Camera +**
- One of the best tools to shoot with. Zoom and has a "rule of thirds" grid that you can turn on when shooting.
- **Adobe Post**
- Layer text over photos. Super apps. Great for building mobile graphics. We'll use this in class. Other good ones: WordPhoto, Layout, Screenshots, ThingLink (make it interactive).
- **Mojo, Type Art, Hype Type and Ripl**
- Animated type for extra effects. These tools work well for creating social media graphics you can use on the fly.
- **This!**
- App by Tinrocket that lets you layer text and arrows on a photo to label things ([Figure 6.9](#ch06.xhtml__15031-5909_ch006_Figure_009)).


<a href="#ch06.xhtml_R_15031-5909_ch006_Figure_009"><em>Figure</em> <em>6.9</em></a> The This! App lets you layer text over images <em>Source:</em> Graphic by Mike Reilley/photo courtesy @WrigleyAerials


- **GIF Toaster**
- Allows you to create GIFs out of anything -- photos, video, photo bursts, and live photos.
- **Lightroom, Photoshop Express**
- Editing and effects that the iPhone camera won't let you do. It's only basic edits, but if you're working as a backpack journalist or filing a mobile report, this is a handy tool.
- **MultiResize**
- Batch edit photos for better productivity.
- **Photo Album**
- Keep all your photos in one place. It's a good alternative to Google Photos.
- **PhoneGrafer, Snapture, CameraBag, Camera Zoom**
- Zoom and add various lenses and features to your iPhone camera shoots. Choose one or two as you see fit. PhoneGrafer is my favorite, as it offers many settings and effects and has a built-in level to make sure your shot is true. PhoneGrafer usually costs a few bucks, but I picked it up for free during a holiday sale. Keep any eye out for a deal in the iTunes store.
- **Other photo editing apps:** Stop Motion Studio, Before & After and Life Lapse
- **Summary:** My students love the This! app. You can use it to label locations on an aerial shot, drop in descriptions on recipe foods and much more.

::: section
### ***Recording Audio***

- **Pro Recorder**
- One of the best field reporting audio apps around. CBS Radio reporters are using this app to record, store, edit and send sound bites.
- **Recorder**
- Another good recording app, but this one will allow you to record phone conversations. The app actually TELLS the person you are calling that the call is being recorded. As a journalist, you need to tell them as well. Never secretly tape a phone interview. It's illegal in many states, including Illinois.
- **Tape-a-Call**
- See recorder. Great for recording phone calls. Price fluctuates between \$3 and \$6.
- **Call Recorder**
- The mobile version of the great Skype desktop app. This comes in a paid or free version. Very similar interface to Tape-a-Call.
- **Voice Record Pro**
- This app offers a simple feature that's invaluable to many journalists: It can add a bookmark during a recording. A gentle tap on the screen (not so hard that it gets picked up by the microphone) produces a marker on the display so that when listening back, you can see exactly when a key moment happened during the recording.
- **n-Track and Røde Recorder**
- These cost a few bucks but have some great audio editing features. Interfaces are pretty easy to use. Very powerful tools. Good if you plan to do some radio work. Twisted Wave and iSaidWhat?! Apps are other pricy alternatives
- **Others: Voice Record Pro, Ringr, Call Recorder and Luci Rooms** (record up to five lines at once for a group podcast or interview and export as an. MP3 file.)
- **Summary:** Regardless of what recording app you use, you must use an iRig or other top brand mic, lapel mic or a shotgun mic with your phone when recording audio and video, or your audio won't sound good. Your mileage may vary with these apps, but I prefer Pro Recorder for in-person interviews and Tape-a-Call for phone interviews. [Otter.ai](http://Otter.ai) and Descript will record and export transcriptions, if you need that.

::: section
### ***Timelapse Video***

- **iMotion Pro (\$3)**
- The pro version gives you great flexibility on intervals, etc. and shoots in HD. The free version is powerful, too.
- **Lapse It (\$2)**
- Dashboard isn't as intuitive as iMotion, but it has a lot of settings and is a great tool.
- **Frameograph (\$5)**
- Only has 1-second to 10-minute intervals, but is otherwise a good app.
- **Time Lapse Camera (\$1)**
- Good, basic camera app. Has a free version, too. I'd spend a couple more bucks and get the Cadillac of time-lapse cameras, though.
- **Summary:** Each has strengths and weaknesses, but I like the flexibility of iMotion's Pro app the best. These tools go beyond the basic timelapse built into the iOS camera and provide greater stability.

::: section
### ***360-Degree Camera Apps***

- **Google Streetview**
- Shoot 360 photospheres and view online or in VR headset/Google Cardboard.
- **Bubbli**
- iOS only. Shoot 360-degree photo bubbles. Hold your phone horizontally and paint up and down in a circle to capture the area around you.
- **Fyuse**
- This 360 app allows you to shoot inward -- walk around a car, statue, etc. -- to capture a 3D circular tour. There are many great examples from users when you log in to the app.
- **Theta and Insta360 Nano**
- Apps work with the mobile 360 cameras. Control the cameras remotely from your phone.

::: section
### ***Data Journalism: Charts and Graphics***

- **Chartistic**
- This app can be used to create bar charts or pie charts with labels on the x-axis and y-axis.
- **Icongraph**
- Has a huge range of templates where you only need to add the data relevant to your story.
- **Alight Motion**
- For fast production of animated graphics, nothing beats Alight Motion. You can create templates for graphics you use all the time, too, so you can edit a package for the evening bulletin or web update without going into the office. It's available on iOS and Android, and costs \$5 a month.
- **Summary:** Both Chartistic and Icongraph produce static images but if you screen record while the image is generated, that will provide a video instead.

\* \* \*

***Video: Mobile Apps: Multimedia***

- Use these Journalist's Toolbox training videos to learn how to build videos, edit audio, build data visualizations and more.
- **Useful Mobile Apps for Journalists:** [www.youtube.com/watch?v=DoAzaB_zQ8s](http://www.youtube.com)
- **Data Visualizations:** [www.youtube.com/watch?v=K32P5RJXJos](http://www.youtube.com)
- Learn how to build data visualizations on your smartphone or tablet with apps.

\* \* \*

::: section

## The Chicago Stumbler Tumblr

In 2012, I was walking in my neighborhood when I rolled my right ankle in a large sidewalk divot about a block from my home. Poor sidewalk conditions are common in Chicago, and I wasn't paying close attention to where I was stepping.

I limped home, iced and elevated the ankle. Then I had a thought: Chicago's pothole problems have been well-documented by the local media. The potholes sprout like flowers every spring due to all of the salt on the streets and cold conditions from harsh winters. But what about the sidewalks? Has the media covered the city's poor sidewalk conditions?

A few web searches gave me the answer: There was very little reporting on sidewalk conditions. So I gave it some thought. How could my DePaul University journalism students who write for The Red Line Project website (<https://redlineproject.news>) cover the issue in an interesting way?

I had been toying with the idea of launching a Tumblr site to accompany The Red Line Project site, but I didn't have an idea to build it around. This was the opportunity: The Chicago Stumbler Tumblr (<https://chicagostumbler.tumblr.com>) was born ([Figure 6.10](#ch06.xhtml__15031-5909_ch006_Figure_010)).

We launched the site later that year and teased it off The Red Line Project home page. The concept was simple: Students would use their smartphones to shoot photos of poor sidewalk conditions and geolocate them. They would upload the photos to Tumblr from their phones and write a short description of the conditions and the precise location of the issue.

Students were required to shoot at least two sidewalks, and at the end of each post, they would include a "call to action" (Paul Bradshaw describes the call to action in [Chapter 1](#ch01.xhtml__15031-5909_ch001)) that told readers how to report broken sidewalks through a 311 phone call to the City of Chicago or through a website. The posts also asked readers to tweet their own photos of poor sidewalks to our \@redlineproject Twitter account so we could retweet them, which many did.

After a few academic quarters, we had documented hundreds of poor sidewalks. My teaching assistant, Lindsey Murphy, began to map the locations on [mymaps.google.com](https://www.mymaps.google.com). We soon learned that the sidewalk issue was citywide and not isolated to one area. We found that some of the worst conditions were in high-traffic areas: business districts, parks, downtown, Wrigley Field, etc.


<a href="#ch06.xhtml_R_15031-5909_ch006_Figure_010"><em>Figure</em> <em>6.10</em></a> The Chicago Stumbler Tumblr


The Chicago media began to notice. The Stumbler was featured in the Chicago Sun-Times, CBS 2 Chicago, WLUW (88.7 FM) radio and several community blogs. In January 2014, NBC 5 investigative reporter Chris Coffey emailed me with an interesting idea: What if my students teamed up with his reporting team to do a two-part investigative series on the city's poor sidewalk conditions. We didn't hesitate to say yes.

Over the next few months, during a brutally cold Chicago winter, Coffey and his team accompanied my students as they documented the sidewalk conditions. They pulled public records of sidewalk complaints and tracked how many were repaired ... and which ones have not. The records weren't hard to find. They're posted on the City of Chicago Data Portal.

They researched the city's "adopt a sidewalk" repair program in which the city shares repair costs with residents and local businesses. That program often went broke three months into the year. More importantly, they crowdsourced and found dozens of Chicagoans had sued the city -- up to \$6 million a year in some cases -- over injuries sustained tripping over poor sidewalk conditions.

The two-part series aired in March and May 2014. Coffey interviewed some of the students, and I worked the videos into a web-only package. His producer, Katie Smyser, worked with us to build maps and post PDFs of the sidewalk complaints. A form on the NBC 5 website fielded more sidewalk complaints from viewers.

Now, 12 years after I stepped in that divot and hurt my ankle, my students continue to document poor sidewalk conditions all over the city. The Stumbler project teaches students many modern storytelling techniques:

- **Mobile photography:** It requires them to frame a photo properly and from the safety of the sidewalk (a potholes project would require them to step onto dangerous Chicago streets). They have to shoot during the day, be wary of shade and shadows and shoot at a tight angle that shows the scale of the problem.
- **Think in terms of scale:** How can we show how big or deep that sidewalk divot is? I've had students use soft drink cups, skateboards and their backpacks to show scale. One sidewalk hole was so deep that it swallowed nearly half of the student's backpack when she set it in the hole.
- **Involve readers:** It teaches them about the aforementioned "call to action" and how to encourage the reader to get involved in the story and issue beyond just scrolling through the photos.
- **Think of others:** It shows them to show compassion and concern for others. Poor sidewalks are dangerous to everyone, but what about a person in a wheelchair? Someone skateboarding or pushing a baby stroller? To a small child who has just learned to walk? To the elderly who may be using a walker?
- **Geolocation:** Students have to be aware of where they are when shooting the photos and documenting them on the site. They need to give the precise location of the sidewalk: Street address, businesses nearby, north or south side of the street, at a corner, etc. Thinking through this can be challenging, especially if there's no street address available (vacant lot, etc.). I often use Google Earth to double-check the locations when grading the assignments.
- **Write descriptively:** As Chris Graves mentioned in [Chapter 1](#ch01.xhtml__15031-5909_ch001), journalists must learn to write what they see and hear, and write that in clear, descriptive language.
- **Use public records and mapping:** With the NBC 5 project, they learned how to use public records of 311 complaints to show the scale of the issue beyond the examples they documented with their smartphones. And by mapping the problem, they showed the reader how widespread the issue is.

\* \* \*


::::::: section
## Exercises

::: section
### ***Exercise 1: Develop Your Own Mobile Product***

Creating your own Chicago Stumbler project can be done in any city or on any college campus. If not sidewalks, maybe it's something else. Map the locations of emergency call phones on campus and document which ones aren't in working order.

Whether you're in a newsroom or classroom, organize into teams of three. Look over the Chicago Stumbler. Then each group can develop a concept for a stand-alone project that requires mobile reporting and photography to address a similar issue on or off campus.

Take a week to huddle and develop the ideas. Then present the ideas to the overall group. Stuck for ideas? Think about public safety and service to the community. Think about crowdsourcing and other ways to get the audience involved.

Then have the group vote on what they think is the best project and if they can turn the idea into an actual project. They can choose a couple and split them into groups. If it's in a classroom setting, introduce it in the first couple of weeks of the semester.

When your project is complete, share it on Twitter to the #toolboxproject hashtag so everyone here can see your work.

\* \* \*

::: section
### ***Exercise 2: Explainer or Process Video***

Record some video clips that explain a process or complex topic. Think of wide, medium and close sequences that you can shoot. Remember, these videos typically display a sequence of events to provide a quick overview, so the length is under two minutes.

Once you're done shooting, use Luma or VN Video Editor to assemble the clips, record the narration and add clips. If you don't have strong visuals, try the VideoScribe desktop tool (the phone app was discontinued in 2022) to create the video. Watch this video on how to produce basic whiteboard videos in VideoScribe: [https://www.youtube.com/watch?v=EgZP3pIrNSc](https://www.youtube.com). Doodly is another whiteboard option. Both tools are fee-based but you get seven-day free trials, which works for this assignment.

When your video is complete, share it on Twitter to the #toolboxproject hashtag so everyone here can see your work.

\* \* \*

::: section
### ***Exercise 3: Text on an Image***

Shoot a photo with your phone and use the This! app to layer text and directional arrows to various locations or items in the photo. A simple start: Lay out the ingredients to a recipe on a table and shoot down on them. Then label each using This! Or shoot down on a construction area from a nearby building and label the areas under construction, similar to the Wrigley Field example in this chapter. Then share your graphic over social media.

Watch this video on how to use This! [www.youtube.com/watch?v=SShKsacb2tE](http://www.youtube.com).

When your image is complete, share it on Twitter to the #toolboxproject hashtag so everyone here can see your work.

\* \* \*

::: section
### ***Exercise 4: Interview Story***

Prepare some "person-on-the-street" questions about current events, topics and issues in your area. Then take a tripod and mount your smartphone on it in landscape mode. Plug in a clip-on or handheld microphone and interview three people on your list of questions.

When shooting, make sure the camera is on the shadow side of the subject and that you're shooting from the chest up. Give the person plenty of space under their chin in case you need to add a lower-third to identify the person.

If possible, record some B-roll or photos that you can use to incorporate into the story.

Now load the clips into Luma Fusion or VN Video Editor, edit the clips and add text. Shoot for two minutes. Group the clips together by topics and use text cards as transitions. Export it, post it to YouTube and share over social channels, including the #toolboxproject Twitter hashtag so everyone here can see your work.

**Types of questions:** Public safety, campus issues, how you'll vote in an upcoming election and why, social justice issues, etc.

\* \* \*

::: section

## Footnotes

- ABC 7 Chicago: George Floyd Protests: [https://abc7chicago.com/chicago-protests-looting-suburbs-in/6222518](https://abc7chicago.com)
- BBC: The BBC Unveils Bike Bureau for Green Broadcasting: [www.bbc.com/news/av/entertainment-arts-65511794](http://www.bbc.com)
- The Chicago Stumbler Tumblr: <https://chicagostumbler.tumblr.com>
- City of Chicago Data Portal: Pothole Repairs: [https://data.cityofchicago.org/browse?q=pothole&sortBy=relevance](https://data.cityofchicago.org)
- Doodly: <https://click.doodly.com>
- Google MyMaps: <https://mymaps.google.com>
- Google Photos: [www.google.com/photos/about](http://www.google.com)
- Graphic: 10 Tips for Making Better Videos with Your Smartphone: [https://2.bp.blogspot.com/-pkfg3rx2QDk/WbJQ4LdOuHI/AAAAAAAAGpg/upm_rHR6UIc9efBLes5qfgCB6RK9UhG8ACLcBGAs/s1600/png.png](https://2.bp.blogspot.com)
- Graphic: U.S. Cellphone and Smartphone Ownership (2011--2021): [https://public.flourish.studio/visualisation/13822878](https://public.flourish.studio)
- [Journalism.co.uk](http://Journalism.co.uk): The Three Pillars of Mobile Journalism: [www.journalism.co.uk/news/the-three-pillars-of-mobile-journalism-q-a-with-marc-settle-smartphone-trainer-at-the-bbc/s2/a720043](http://www.journalism.co.uk)
- Journalist's Toolbox: Drones and VR: [www.journaliststoolbox.org/category/drones-and-vr-journalism](http://www.journaliststoolbox.org)
- Journalists Toolbox Training Video: VideoScribe: [www.youtube.com/watch?v=EgZP3pIrNSc](http://www.youtube.com)
- Mobile Journalism Textbook, Robb Montgomery: [https://robbmontgomery.com/book](https://robbmontgomery.com)
- NBC 5 Chicago: City Shells Out Millions to Settle Sidewalk Injury Cases: [www.nbcchicago.com/news/local/chicago-sidewalk-settlements-judgements/125061](http://www.­nbcchicago.com)
- Nieman Lab: More Newsrooms Go Mobile-First: [www.niemanlab.org/2022/12/more-newsrooms-go-mobile-first](http://www.niemanlab.org)
- Oberlo: How Many People Have Smartphones in 2023?: [www.oberlo.com/statistics/how-many-people-have-smartphones](http://www.oberlo.com)
- Pew Research Center Mobile Fact Sheet: [www.pewresearch.org/internet/fact-sheet/mobile/?tabId=tab-7cfdecc4-bb29-4a14-96f5-5ba4acd5c1a9-data](http://www.pewresearch.org)
- PictureThis: [www.picturethisai.com](http://www.picturethisai.com)
- Readwise Reader: [https://readwise.io/read](https://readwise.io)
- The Red Line Project Video: How Mail-in Voting Works: <https://bit.ly/illvotingvideo>
- Seek: [www.inaturalist.org/pages/seek_app](http://www.inaturalist.org)
- Smart Film School: [www.smartfilmschool.com](http://www.smartfilmschool.com)
- Snipd: [www.snipd.com](http://www.snipd.com)
- Substack: [https://substack.com/app](https://substack.com)
- Technologies Blog: Mobile Journalism: [https://blog.iotechnologies.com/mobile-journalism-constantly-online](https://blog.iotechnologies.com)
- Twitter: The Red Line Project: [https://twitter.com/redlineproject](https://twitter.com)
- Video: The Grand Budapest Bike Tour: [https://robbmontgomery.com/the-grand-budapest-bicycle-tour](https://robbmontgomery.com)
- Video: How to Use Anchor (Audio): [www.youtube.com/watch?v=tr8deLLg4bw](http://www.youtube.com)
- Video: How to Use Data Visualization Apps: [www.youtube.com/watch?v=K32P5RJXJos](http://www.youtube.com)
- Video: How to Use Hokusai (Audio): [www.youtube.com/watch?v=6NjzojQE2o0](http://www.youtube.com)
- Video: How to Use This! App: [www.youtube.com/watch?v=SShKsacb2tE](http://www.youtube.com)
- Video: How to Use VN Video Editor: [www.youtube.com/watch?v=vQV743JqvnE](http://www.youtube.com)
- Video: How to Vote by Mail in Illinois: [www.youtube.com/watch?v=veRjTWTWDfY&embeds_referring_euri=http%3A%2F%2Fredlineproject.org%2F&source_ve_path=OTY3MTQ&feature=emb_imp_woyt](http://www.youtube.com)
- Video: Ice Swimming: [www.youtube.com/watch?v=GyzRy3-wXAU](http://www.youtube.com)
- Video: Mexican Grey Wolf Count: [www.youtube.com/watch?v=U6U1cyDx-FU](http://www.youtube.com)
- Video: Useful Mobile Apps for Journalists: [www.youtube.com/watch?v=DoAzaB_zQ8s](http://www.youtube.com)
- VideoScribe: [www.videoscribe.co](http://www.videoscribe.co)
- Wakeout: <https://wakeout.app>


# 7 MultimediaPodcasting \| Audio \| Photo Editing

DOI: [10.4324/9781003431787-8](https://doi.org/10.4324/9781003431787-8){aria-label="D.O.I. link to this document."}


**Key Resources**

**Audio**

- Journalist's Toolbox AI Transcription and Audio: [https://journaliststoolbox.ai/transcription-and-audio](https://journaliststoolbox.ai)
- Adobe Audition
- Part of the paid Adobe creative suite, the more advanced audio editor for higher-end editing
- Adobe Podcast
- Record and edit podcasts quickly and easily
- Audacity
- Free audio-editing software you can download; has high-quality output and settings
- Hokusai
- iOS audio editing phone app
- Anchor.fm
- Record and distribute a podcast with just a couple of clicks on this iOS phone app
- Murf.ai
- AI-driven text-to-speech tool

\* \* \*

**Photos**

- Journalist's Toolbox AI: Image Creation Tools: [https://journaliststoolbox.ai/image-and-video-creation](https://journaliststoolbox.ai)
- Adobe Photoshop: [www.adobe.com/creativecloud/business/teams.html](http://www.adobe.com)
- Adobe Firefly: <https://firefly.adobe.com>
- National Press Photographers Association Code of Ethics: [https://nppa.org/resources/code-ethics](https://nppa.org)
- Adobe: Image User Guides: [www.adobe.com/legal/permissions/images-user-guides.html](http://www.adobe.com)
- Covers legal permissions on photos

\* \* \*

When Victor Hernandez arrived at WBUR in March 2021, he and his staff grasped the opportunity to try a new approach for the Boston NPR member station's podcasts.

Michelle Wu was elected Mayor of Boston that year, representing a background and lived experience dramatically different from her predecessors going back 200 years. Shifting demographics were also playing out in Boston neighborhoods as the city's population continued to rise among residents identifying as nonwhite. Boston's population was also growing younger, as nearly one-third of its residents that year were age 20--34, which is younger than most other major cities in the country.

The city's arts scene was also changing in the evolving post-pandemic era, as creators and cultural institutions bounced back from an extraordinary few years of duress.

Transportation, housing, education, technology, health care and other significant industries were also deeply impacting the lives of Bostonians and were being challenged, and in some cases, transformed before their very eyes ... and, in WBUR's case, ears.

In November 2021, WBUR launched "The Common" (see [Figure 7.1](#ch07.xhtml__15031-5909_ch007_Figure_001)), a daily podcast that explores civic issues and local changemakers influencing a rapidly changing *New Boston*.

The daily podcast publishes on weekdays at 6 a.m. and taps into news reporting and analysis from WBUR's newsroom as well as other journalists, experts and community voices. Each episode focuses on a single issue or challenge shifting the civic, political or cultural landscape of a changing Boston. Episodes are a listener-friendly 15 minutes or less.

"The Common" is hosted by Darryl C. Murphy, who was previously a transportation reporter at WBUR. Behind Murphy is a team of two dedicated podcast producers and a sound designer. WBUR Podcast executive producer Ben Brock Johnson oversees pod production efforts, including "The Common," and typically edits and reviews the episodes before they are prepared for publishing.

"What's different about 'The Common' in comparison to our broader portfolio of podcast products is this is aimed at a local audience and through a daily (habit-forming) listening experience," Hernandez said.


<a href="#ch07.xhtml_R_15031-5909_ch007_Figure_001"><em>Figure</em> <em>7.1</em></a> WBUR’s “The Common” podcast


"Most of WBUR's podcasts are geared toward a national/global audience ('Endless Thread,' 'Last Seen,' 'Circle Round,' 'On Point,' 'Here & Now,' 'Anything for Selena,' 'Dear Sugars,' etc.); however, we've been interested for a long while in developing a unique and engaging daily pod positioned to serve Great Boston communities."

Hernandez and his WBUR team are tapping into one of the biggest markets out there for journalists -- podcasts. According to DemandSage, there are 464.7 million podcast listeners globally as of 2023. This number is predicted to reach 504.9 million by 2024. The podcast industry market size is \$23.56 billion. There are over 5 million podcasts globally with over 70 million episodes between them.

In [Chapter 6](#ch06.xhtml__15031-5909_ch006), we covered audio-recording apps and microphones you can use with your mobile devices for audio reporting. In this chapter, you'll learn how to tap into the podcast market, and learn about the basic tools you need to record and edit podcasts and audio clips. You'll also learn how to edit photos using paid and free photo editing tools, as well as use the handy Adobe Firefly text-to-image tool to produce illustrations.

\* \* \*

<aside aria-label="box1" class="box1" epub:type="tip" role="doc-tip" title="box">

::: section
## Popular Audio Formats: 

- **MP3:** These compressed files are the most popular and play on nearly every platform or device.
- **WAV and AIFF:** Uncompressed, large audio files that are high quality but don't play well over Wi-Fi. These files can be easily compressed and formatted as MP3 files in any audio editing software.
- **WMA:** Windows Media Audio files that can be converted into mp3 files easily.

</aside>

\* \* \*

:::: section

## Audio Editing and Podcasting Tools

We have already learned how mobile devices have made recording video less-intrusive than large cameras, the same holds true for audio recording equipment when journalists engage reluctant or hard-to-access sources. A simple Røde, iRig or Shure MV7 hand-held microphone or small, wireless clip-on mic can provide high-quality audio without being as intrusive as a large recording device or a studio. Podcasting equipment is highly portable: a laptop, Blue microphone or even just recording on Zoom can put a guest or source at ease.

Before working with the editing tools, watch this video on writing for podcasts to learn the key steps for developing introductions: [https://www.youtube.com/watch?v=dfcongAw53g](https://www.youtube.com).

- **Adobe Audition**
- Part of the paid Adobe creative suite, the more advanced audio editor for higher-end editing.
- **Adobe Podcast**
- Record and edit podcasts quickly and easily.
- **Audacity**
- Free audio-editing software you can download. Has high-quality output and settings.
- **Hokusai**
- iOS audio editing phone app.
- **Anchor.fm**
- Record and distribute a podcast with just a couple of clicks on this iOS phone app.
- **Sodaphonic**
- A browser-based audio editor.
- **AudioTrimmer**
- Similar to SodaPhonic, a basic audio editing tool.
- **SoundCloud**
- Podcast hosting site.
- **Headliner.app**
- Transform your podcast into a video.
- **PodBean**
- A podcasting app that has received a lot of attention from developers in recent years. The app works well for listening to and creating podcasts -- and it integrates with the desktop version.
- **Riverside.fm**
- Remote interview recording software that supports local audio and video recording in studio quality. You receive separate audio (WAV) and video (MP4) tracks for each guest. Allows up to eight co-hosts/guests to join the recording remotely.
- **Snipd**
- Listen to podcasts, save highlights and discover highlights from others.
- **Descript**
- Audio word processor. Good for transcribing audio from interviews. The first 30 minutes are free, and paid after that. Also does podcasting, video editing and more.
- **Murf.ai**
- AI-driven text-to-speech tool.

\* \* \*

<aside aria-label="box2" class="box1" epub:type="tip" role="doc-tip" title="box">


::: section
## Video: Edit Audio with Hokusai 

USC's Amara Aguilar shows how to edit audio on your smartphone with the Hokusai app: [www.youtube.com/watch?v=j-QgUIIHQUg&list=UU8CCl01DmsE65wh-qPqjSLQ&index=6](http://www.youtube.com)

</aside>

\* \* \*

::: section

## Measuring a Podcast's Success

Based on in-depth audience survey information conducted in 2021, local audiences told WBUR that they're interested in more local stories that offer depth and context. The station is bullish on the opportunity to engage this curious audience.

Hernandez saw the early momentum: In just the first few months, the podcast saw a growing local audience, a steady flow of positive feedback notes from listeners and above-industry-average completion rates near 85%.

"We saw a marketplace opportunity with the lack of local daily news and culture pods available in Boston and knew we could add to the news diets of our local curious and community-concerned audiences through a new and compelling podcast," said Hernandez, who previously worked at CNN, Cascade Public Media and a tech startup.

"However, we've also provided space for Darryl and the team to drill into interesting topics, often deeply influencing changing Boston, through a more congenial and authentic approach than many daily news briefing-type pods out there."

Hernandez said it was important to WBUR that they sound more inviting and less buttoned-up than the garden-variety daily news pods. This grounding also allowed them to more carefully steer topics, voices and format to better connect with younger and more diverse audiences, which is a coveted strategic goal for most public media institutions seeking continued relevance across future generations.

"We also know the content and presentation will best land with local audiences who care about what is happening and why across the rapidly changing Boston region," Hernandez said.

To measure success, WBUR paid close attention to the following data points:

1.  Who's listening? (demographics insights)
2.  How many are listening? (subscribers and downloads)
3.  How are they coming to "The Common"? (platforms and behaviors -- example: so far, Amazon Alexa smart speaker is the most popular platform people are listening on)
4.  When are they listening? (so far, 8 a.m. is the #1 listening time)
5.  Are they returning regularly, or do they listen once and move on?
6.  Completion rates -- are they sticking around for most/all of the episode?
7.  Is the cross-platform promotion of other WBUR products/platforms seeing any measurable uptick when referenced in "The Common"? (example: when Darryl calls out more information or value additive in specific WBUR broadcasts, newsletters, live events, etc., are those audience members showing up elsewhere?)
8.  What is the level of offline engagement? (social media, showing up at "The Common" in-person events, etc.)

WBUR's metrics checklist mirrors that of many industry podcasts: who is listening, when and for how long. Podcast production platform [Riverside.fm](http://Riverside.fm) encourages creators to dig deep into their analytics and be patient. It takes time to build an audience, so make sure you take measure of it over a period of weeks and months, not just a few episodes. Understanding how the analytics work and exactly what they're measuring is key, too.

For example, Riverside says it's important to understand that "total listens" -- or the number of times someone presses play -- can mean repeat listens or people listening to episodes in two (or more) instances. It doesn't necessarily mean your audience has grown. Also, podcast subscriptions and downloads don't mean the person has listened. Instead, look for common themes in listener peaks, make changes to content when episodes don't perform well, and do more of what does well in multiple metrics, Riverside recommends.

Other recommendations from Riverside:

- **Study timing:** Could you get a bigger audience releasing the episode on a different day? A different time? Are you pushing it out over your social channels at the right time of day with the right hashtags?
- **Audience engagement:** Analyze your listener drop-off rate: are people skipping over your intro or ads? An NPR study showed that podcasts lose up to a third of their listeners in the first five minutes, so frontload the show with what's to come and a good hook or guest to make an early splash.
- Use your social media and subscription or donation site analytics as well to see how your fans interact with you outside of their podcast listening platforms. Make sure you're engaging with them in the comments section to show you value their support.
- **Location and device type:** Use this to discover where to host live events and to pitch to local brands for sponsorships for extra monetization opportunities.
- Learn about your listeners' device type and platform, and leverage this data to provide added value to these listeners.
- For example, if they're listening via YouTube, you can easily create additional content like video and live podcasting and share the podcast to a video audience as well. YouTube is often overlooked as a podcast platform. Riverside offers a live virtual recording studio. You also can use free audiogram tools like Headliner.app to produce visual podcasts for YouTube, Vimeo as well as social media teasers.
- **Leverage your assets:** Could you pull clips from your show and share them over social or share with other shows? Do you have transcripts from your shows? Post them online as a value-added feature. They're also searchable.
- **Study the outliers:** As with all data, you should always be wary of outliers and extreme changes in your statistics. For example, a recent data inflation issue with podcasts on Apple Watches showed much higher download rates.
- Look at the traffic for your best- and worst-performing episodes in the first four months. At what point in the podcast did they stop listening? Was a specific topic driving or hurting the amount of listening time? Too much banter from the hosts?
- It's also key to set reasonable benchmarks for your podcast in the first year. According to Podcast Host, the average podcast gets only 27 listens per episode, but the top 1% have almost 3,200 listens per episode. Eighty percent of podcasts don't survive past 10 episodes. You'll need time to build that audience.

Remember, there are no set lengths for podcasts. Some are short -- just a few minutes -- while others extend beyond an hour. Track your analytics to see how far into a podcast people are listening, and trim the length for future ones if you need to.

::: section
## Podcast Hosting Platforms

Most podcast hosting platforms come with additional features to grow your following. If you know what to look for in a podcast host, you can easily select a platform that will meet all of your needs and simplify your podcasting experience, instead of complicating it.

Apple Podcasts, Spotify for Podcasters, [Anchor.fm](http://Anchor.fm), YouTube and RedCircle are free podcast hosting sites. Buzzsprout and Podbean have both free and paid options. Simplecast, AudioBoom, Clyp and [Transistor.fm](http://Transistor.fm) all charge for hosting. You'll need to weigh the pros and cons of free sites vs. paid hosting. Before choosing one, make sure to study the analytics and SEO support that each offers.

Some of these platforms are all-in-one tools that allow you to record, edit and host all in one place, which could save you time and money in the long run. For shorter podcasts, you can easily record into Substack, the popular newsletter publishing tool, or Wordpress.

:::: section

## Recording Audio: Apps and Best Practices

We explored [Otter.ai](http://Otter.ai) and Descript for recording interviews in [Chapter 1](#ch01.xhtml__15031-5909_ch001), but there are other options for recording calls and in-person interviews over your smartphone. App stores are full of options, but three reliable ones are:

- **Rev:** A free call recorder tool that produces clean audio. It's simple to use and might be a good option if you're just starting out.
- **VoiceRecord Pro:** It's a free download in the App Store, but you can do paid upgrades.
- **TapeACall and Call Recorder Pro:** Paid apps with many great features. Useful for reporters who want to post the audio clips in a digital story.
- **Voice Recorder & Audio Editor:** It's a free download with in-app purchases that can get expensive. But it's a great all-in-one recorder and editor that produces quality audio.

Regardless of what app you're using, try to wear headphones when recording audio and definitely when editing. Do a test run with the app and audio before starting the interview, just to make sure you're getting quality sound. If you're outdoors, put a foam windsock on the microphone if it's windy, but test it first to make sure it doesn't muffle the sound too much.

Make sure you get the source's permission to record the call at the start, as it's illegal to surreptitiously record conversations in many countries and states. Make sure that permission is on the recording at the start of the interview.

Whether you're doing a podcast or just an audio interview, make sure you keep a relaxed, accessible style to your interviews. Have questions prepared, but don't read off a list. Keep control of the microphone and try to keep it about four to six inches from a source's mouth when recording. If you're in a podcast studio, coach the source on how far to sit from the mic before the show begins.

Try to avoid distractions, like rustling papers during the interview or podcast recording. If you make a mistake when recording, simply do the segment again or repeat the question later in the interview. You can always edit around it later.

\* \* \*

<aside aria-label="box3" class="box1" epub:type="tip" role="doc-tip" title="box">


::: section
## Create Audiograms 

Learn how to create an audiogram with the Headliner.app desktop tool in this training video: [www.youtube.com/watch?v=kIodgJEGcqg](http://www.youtube.com)

</aside>

\* \* \*

::: section

## Podcasts for a Student Media Outlet

Student media outlets have been slow to embrace podcasts, particularly student newspapers. I've always blamed semester-to-semester staff turnover and changes in student interests and expertise for failure to maintain long-running podcasts. Student radio stations have had much greater success with them, but even they can lag from year to year as students come and go.

One example of a terrific student podcast was Home Ed ([https://homeschooling.nycitynewsservice.com/podcast](https://homeschooling.nycitynewsservice.com)), created by Mary Steffenhagen of the City University of New York. The award-winning, one-off topical podcast explored the political, religious and legal forces surrounding the homeschooling movement in the United States. In less than 25 minutes, she examined a tragic incident in West Virginia when a student was being abused by her family and was pulled out of school when teachers reported the abuse. It exposed lax laws for homeschooling and care for the student. It incorporated many interviews and exposed serious issues about a growing trend in education.

During the pandemic, my UIC data and digital reporting students stepped up their efforts by using more audio and podcasts in our reporting for The Red Line Project (<https://redlineproject.news>), the student media outlet that covers news and urban affairs in Chicago neighborhoods.

With the student reporters and sources on lockdown, it was difficult to shoot live video interviews and get B-roll. Zoom video interviews looked like an episode of "The Brady Bunch" with all the small boxes. So we stripped the audio out of the Zoom interviews or recorded phone calls. We used audio, photos and audio slideshows instead of video.

We used SoundCloud to host and embed the audio into the stories. Most were short interviews with sources that featured interesting quotes or emotional interviews. We also launched a student-hosted podcast each semester called "Reporters Roundtable", ([https://redlineproject.news/podcast-red-line-project-radio](https://redlineproject.news)), where a few reporters would be interviewed by a student host about the stories and issues they wrote that semester. We posted them as a single podcast (see [Figure 7.2](#ch07.xhtml__15031-5909_ch007_Figure_002)), but we also broke up the interviews and posted them at the end of each student's story. We felt that it would lend additional transparency to our reporting process if the reporters, in their own words, explained how they went about it.


<a href="#ch07.xhtml_R_15031-5909_ch007_Figure_002"><em>Figure</em> <em>7.2</em></a> Red Line Project Radio Reporters Roundtable podcast


::: section
## The AI Factor: Text-to-Speech Tools

In late 2022, a flood of free and paid text-to-speech applications flooded the digital tools market. They're primarily used for voice-overs for radio promos or advertising. Instead of hiring voice talent, you could just type a short paragraph and tailor the voice to make it sound how you wanted.

This raises many legal and ethical concerns among journalists: Did the person actually say this? What do I believe? Should journalists even consider using a piece of audio in a story? Much like the ethics of AI-generated images, which will be explored later in this chapter and again in [Chapter 10](#ch10.xhtml__15031-5909_ch010), the best approach to take is cautious curiosity. Ethical guidelines for custom text-to-speech may include getting approval of voice talent; disclosure of synthetic voice use; permission from voice talent for use to create and train AI voice models for editorial or advertising/promotional use.

The free tools are easy to use. For example, [Murf.ai](http://Murf.ai) lets you upload a script or just type a few sentences into its interface. You can adjust the pitch and speed, add pauses and make the voice sound angry, happy, sad, excited or friendly. You can choose the gender and age group (young adult, middle-aged) of the speaker.

It also has a setting called "newscast." I tested this setting by uploading a script of Walter Cronkite detailing President Kennedy's shooting and later death on Nov. 22, 1963. It's one of the most famous newscasts in history.

While Cronkite's call showed compassion and, for a brief moment, emotion, the text-to-voice newscast was very robotic, direct and lacked the human element of delivering such horrible news to viewers.

Here's the text: Try it for yourself:

- **The breaking news bulletin:** Here is a bulletin from CBS News in Dallas, Texas. Three shots were fired at President Kennedy's motorcade in downtown Dallas. The first reports say that President Kennedy has been seriously wounded by this shooting.
- My audio: [https://murf.ai/share/litdpcvm](https://murf.ai)
- **Kennedy's death:** From Dallas, Texas, the flash apparently official, President Kennedy died at 1 p.m. Central Standard Time, 2 o'clock Eastern Standard Time, some 38 minutes ago. Vice President Lyndon Johnson has left the hospital, but we do not know to where he has proceeded. Presumably he will be taking the oath of office shortly and become the 36th president of the United States.
- My audio: [https://murf.ai/share/liteazvh](https://murf.ai) **\|** Cronkite's call: <https://bit.ly/cronkiteJFK>

The lesson I learned from this exercise: Tone and showing compassion, being human, matters in audio reporting. It's particularly important when delivering bad news to people. AI text-to-audio will certainly improve over time, but for now, it's not a sound option for hard news delivery.

\* \* \*

:::: section

## Ethics and Editing Photos

Before my students ever touch Photoshop or any other photo-editing software, I have them read two things:

1.  National Press Photographers Association Code of Ethics: [https://nppa.org/resources/code-ethics](https://nppa.org)
2.  Adobe Image User Guide, which covers legal permissions on photos: [www.adobe.com/legal/permissions/images-user-guides.html](http://www.adobe.com)

Understanding ethics and copyright law is critical for photo editing. For instance, are you editing the photo for clarity or manipulating what the reader is seeing? Do you need to explain the edits to the reader? If it's a photo illustration or rendering, you need to label it as such in the cutline.

For news photos, I stress cropping and only light edits in brightness/contrast, color balance and sharpening for online posting. Dropping out backgrounds, extreme crops or flipping an image horizontally can completely change the context of the image. Ask yourself: Am I editing this photo or manipulating it? If it's the latter, you shouldn't publish it.

If you're working with photos that are not yours or your publication's, make sure you have the rights to use it. Copyright law protects original works of authorship, meaning the person (or employer of the person) who shot the photo maintains those rights. You need written consent of the author to use that photo. Twitter embeds, stock photos, rights-free photos from Creative Commons and other sources are fine to use, but you must cite that in the cutline/credits of the photos. Photographers use reverse image search in TinEye and Google Images on a regular basis to track who is stealing their photos. At best, you'll get a cease and desist letter from them. At worst, you could be sued.

Photoshop has launched several generative AI tools that allow text commands to make photo edits, including removing backgrounds and even watermarks. A TikTok user took Photoshop's new AI tools in June 2023 and removed an image's watermark in only 30 seconds. That can put millions of dollars of photo revenues from stock images at risk and also violates copyright law.

There are legal ways to get images, including fair use, shoot them yourself, the aforementioned written consent, rights-free images through Creative Commons licenses or through stock image sites:

- StockIMG.ai: <https://stockimg.ai>
- [Shutterstock.com](https://www.Shutterstock.com): [www.shutterstock.com](http://www.shutterstock.com)
- Adobe Stock: <https://stock.adobe.com>
- [Pond5.com](https://www.Pond5.com): [www.pond5.com/](http://www.pond5.com)
- Rights-free photos, illustrations, music and video

MidJourney, DALL-E, Stable Diffusion burst on the scene in 2022 and 2023 to offer users new ways to create illustrations. And with them, they brought many ethical and copyright questions that we will explore in [Chapters 9](#ch09.xhtml__15031-5909_ch009) and [10](#ch10.xhtml__15031-5909_ch010). Using these text-to-image tools can be helpful for building a section banner, creating an image for a food page or a cutaway illustration of a car. But it could be harmful to use it to mislead readers by building a fake news photograph.

In [Chapter 10](#ch10.xhtml__15031-5909_ch010), we will use MidJourney to build the food and automobile illustrations for stories. Here, we'll use Firefly ([https://firefly.adobe.com/](https://firefly.adobe.com)) -- Adobe's free entry into the text-to-image market -- which was still in beta at the time this book was written.

Adobe trains Firefly using Adobe Stock images and other diverse image datasets which have been carefully curated to mitigate against harmful or biased content while also respecting artist's ownership and intellectual property rights. It's regularly tested and updated to avoid perpetuating harmful bias.

The tool is intuitive and incredibly easy to use. Once you open it, simply type your prompt in the field at the bottom of the screen. Here's a prompt I wrote to build a cutaway illustration of a two-story home.

Prompt: Cutaway of a two-story, four-bedroom light gray home with red shutters, flowers and other landscaping

My initial prompt was: cutaway of a two-story, four-bedroom. I added more detail to the prompt to get this version ([Figure 7.3](#ch07.xhtml__15031-5909_ch007_Figure_003)).


<a href="#ch07.xhtml_R_15031-5909_ch007_Figure_003"><em>Figure</em> <em>7.3</em></a> Adobe Firefly interface


What Firefly offers that MidJourney does not: A tool panel to the right with settings for art, photo, etc., filters, color and tone, lighting and composition -- tools similar to what you find in Photoshop's pulldown menus. In MidJourney, you have to write those filters into the prompt. Adobe has streamlined that process.

Which tool is the best? There are fans of DALL-E, MidJourney, Firefly and Stable Diffusion, as well as other tools. I like MidJourney's quality the best, and the ability to tailor a prompt to my exact needs. Firefly is not far behind because of its user-friendly interface and image quality.

Regardless of the tool you use, it's important to tell the reader that it's an AI-generated photo illustration. Some media outlets even mention what tool it was created in.

\* \* \*

<aside aria-label="box4" class="box1" epub:type="tip" role="doc-tip" title="box">


::: section
## Find Rights-Free Images 

Learn how to use Creative Commons and other search tools to find rights-free photos for your stories. Ideally, you'll shoot your own photos or use a staff photographer to shoot them. But if you're stuck and need a feature photo or a shot for a banner, these search tools will be helpful for finding images that you can own or use legally.

[www.youtube.com/watch?v=OaCplDh7XFs](http://www.youtube.com)

</aside>

\* \* \*

:::: section

## Photo Editing Desktop Tools and Mobile Apps

There are dozens of great photo editing tools on the market, some paid, some free. Keep in mind that some of the tools' editing features also may appear in your phone's basic camera editing suite as well. For example, the Google Pixel camera has a magic eraser you can eliminate items from a photo.

- Adobe Photoshop
- [www.adobe.com/creativecloud/business/teams.html](http://www.adobe.com)
- Paid software and the industry standard for photo editing. Built-in generative AI tools allow you to prompt editing commands. Also available as a phone app as PS Express.
- Adobe Firefly
- [https://firefly.adobe.com/](https://firefly.adobe.com)
- Text-to-image tool that also works with Google Bard.
- DALL·E 2 ([openai.com](https://www.openai.com))
- [https://openai.com/dall-e-2](https://openai.com)
- An AI system that can create realistic images and art from a description in natural language
- Microsoft Bing Image Creator
- [www.bing.com/images/create](http://www.bing.com)
- Create images right in chat. Just start typing what you want to create and the software will guide you.
- PhotoLeap
- [www.photoleapapp.com](http://www.photoleapapp.com)
- The AI-driven iOS phone app has cloud-based photo editing software that offers a number of editing options, including adding layers, using blending modes and applying special effects. It also uses AI to improve images and transform them into different images. You can also generate photos from scratch by writing text prompts.
- PhotoPea
- [www.photopea.com](http://www.photopea.com)
- A free, browser-based photo editor with tools similar to Photoshop. Good for file conversion and works with many formats.
- Pixlr
- <https://pixlr.com>
- Another free, browser-based photo editor.
- Fotor Background Remover
- [www.fotor.com/features/background-remover](http://www.fotor.com)

**Note:** For more AI text-to-image software, go to [Chapters 9](#ch09.xhtml__15031-5909_ch009) and [10](#ch10.xhtml__15031-5909_ch010). More mobile photo editing apps can be found in [Chapter 6](#ch06.xhtml__15031-5909_ch006).

\* \* \*

<aside aria-label="box5" class="box1" epub:type="tip" role="doc-tip" title="box">

::: section
## Landscape Social Image Resizer 

Learn how to size and crop images perfectly for various social channels using this free browser-based tool from Sprout Social.

[www.youtube.com/watch?v=LnEIdmjSoEk](http://www.youtube.com)

</aside>


:::::: section

## Exercises

::: section
### ***Exercise 1: Design a Podcast and Target an Audience***

Apply what you learned from Victor Hernandez in this chapter about developing a podcast. Form groups of two or three and brainstorm some topic ideas. Think of niche audiences and topics that would appeal to them. Think about a podcast that might appeal to a broad audience. Should it be campus-based? Community driven? Topical (sports, entertainment, etc.) Or could it appeal to a regional, national or even global audience?

Research the topic and see what is/isn't being done in your area -- are there other podcasts that touch on this topic? Survey your potential audience using Google Forms: what do they want to know? Who are some potential guests you could have on the show?

When you plan, think of ways you can visualize the podcast so it can be made available on YouTube as well as podcast-streaming platforms.

Then write a one- to two-page plan explaining the topic, target audience(s) and how you would execute it. Share with your class or team and vote on whether to pilot an episode.

\* \* \*

::: section
### ***Exercise 2: Record and Edit an Interview***

Record a two- to three-minute interview with someone who can speak with authority on a topic or series of topics (campus safety, elections, etc.) and edit the clip down to 30 seconds to one minute.

As you do the interview, make sure not to interrupt. Let the source finish and have a short pause afterward. This "dead air" in the interview will make it easier for you to edit. Keep eye contact with the source and nod as they answer, rather than saying "uh-huh," which will ruin the audio.

You can use the Hokusai app to edit it on your phone or download it to your desktop to edit in [AudioTrimmer.com](https://www.AudioTrimmer.com) or [Sodaphonic.com](https://www.Sodaphonic.com). The Voice Recorder & Audio Editor app also is a good option.

When you're done editing, launch a free [SoundCloud.com](https://www.SoundCloud.com) account and post the clips there. Share them on social media or post to your Wordpress site or Medium account.

Try to create at least two clips from the interview.

Think about ways you can incorporate these clips into your daily reporting with breaking or even project stories. Can you use short clips on social media to tease an upcoming story?

\* \* \*

::: section
### ***Exercise 3: Create Photo Illustrations Using AI***

Log in to Adobe Firefly (<https://firefly.adobe.com>) and try some of the prompts below to see what results you get. Try out the filters and editing tools on the right panel to fine-tune your results. Once you have an illustration you like, download it and tweet it to #toolboxAI so others can see your work. Provide an explanation in the tweet that includes the prompt you used to build the image. If you have multiple images to share, post them in a Twitter thread with explanations.

Here are a few prompts to get you started:

- **Prompt:** Rendering of downtown Chicago view from Lake Michigan
  - Compare your results to an actual photo of downtown Chicago. Is it accurate? (I had two that were and two that were not.)
  - If so, how would you describe it to the reader in a social-media post or story?
- **Prompt:** Overhead rendering of Dubai at sunset
  - Repeat the exercise with the filters and edits. Compare it to an actual sunset shot of Dubai. How accurate are your renderings and how would you present it to readers?

Remember, you can include your prompts in an image's metadata (alt tag). You also can add alt tags when you load an image into Twitter. We cover how to do that in [Chapter 4](#ch04.xhtml__15031-5909_ch004).

\* \* \*

::: section
## Footnotes

- Adobe Audition: [www.adobe.com/creativecloud/business/teams.html](http://www.adobe.com)
- Adobe Firefly: <https://firefly.adobe.com>
- [Anchor.fm](http://Anchor.fm) -- Spotify for Podcasters: <https://podcasters.spotify.com>
- Adobe: Image User Guides: [www.adobe.com/legal/permissions/images-user-guides.html](http://www.adobe.com)
- Adobe Photoshop: [www.adobe.com/creativecloud/business/teams.html](http://www.adobe.com)
- Adobe Podcast: <https://podcast.adobe.com>
- Adobe Stock: <https://stock.adobe.com>
- Audacity: [www.audacityteam.org](http://www.audacityteam.org)
- AudioTrimmer: <https://audiotrimmer.com>
- The Boston Globe: WBUR's Top Content Executive Makes Big Bet on Podcasts: [www.bostonglobe.com/2022/10/24/business/wburs-top-content-executive-makes-big-bet-podcasts](http://www.bostonglobe.com)
- CUNY Home Ed Podcast: [https://homeschooling.nycitynewsservice.com/podcast](https://homeschooling.nycitynewsservice.com)
- DemandSage: 48 Podcast Statistics: [www.demandsage.com/podcast-statistics](http://www.demandsage.com)
- Descript: [www.descript.com](http://www.descript.com)
- Fotor Background Remover: [www.fotor.com/features/background-remover](http://www.fotor.com)
- Headliner.app: [www.headliner.app](http://www.headliner.app)
- Hokusai: [https://apps.apple.com/us/app/hokusai-audio-editor/id432079746](https://apps.apple.com)
- Microsoft Bing Image Creator: [www.bing.com/images/create](http://www.bing.com)
- Murf.ai: <https://murf.ai>
- National Press Photographers Association Code of Ethics: [https://nppa.org/resources/code-ethics](https://nppa.org)
- PhotoLeap: [www.photoleapapp.com](http://www.photoleapapp.com)
- PhotoPea: [www.photopea.com](http://www.photopea.com)
- Pixlr: <https://pixlr.com>
- PodBean: [www.podbean.com](http://www.podbean.com)
- [Pond5.com](https://www.Pond5.com): [www.pond5.com](http://www.pond5.com)
- Red Line Project Reporter's Roundtable Podcast: [https://redlineproject.news/podcast-red-line-project-radio](https://redlineproject.news)
- Riverside.fm: [https://riverside.fm/homepage](https://riverside.fm)
- Riverside.fm: Podcast Analytics: [https://riverside.fm/blog/podcast-analytics](https://riverside.fm)
- [Shutterstock.com](https://www.Shutterstock.com): [www.shutterstock.com](http://www.shutterstock.com)
- Snipd: [www.snipd.com](http://www.snipd.com)
- Sodaphonic: <https://sodaphonic.com>
- SoundCloud: <https://soundcloud.com>
- StockIMG.ai: <https://stockimg.ai>
- Video: Knight Center: The Fundamentals of Writing for Audio: [www.youtube.com/watch?v=dfcongAw53g](http://www.youtube.com)
- Video: Walter Cronkite's Call on President Kennedy's Death: <https://bit.ly/cronkiteJFK>
- WBUR Boston: [www.wbur.org](http://www.wbur.org)
- WBUR: The Common: [www.wbur.org/podcasts/the-common](http://www.wbur.org)


# 8 Google Earth \| Satellite Imagery

DOI: [10.4324/9781003431787-9](https://doi.org/10.4324/9781003431787-9){aria-label="D.O.I. link to this document."}


**Key Resources**

- From Above: <https://bit.ly/fromaboveguide>
- A guide for journalists on how to use artificial intelligence to identify visual indicators in satellite images.
- Google Earth Suite downloads: [www.google.com/earth/versions](http://www.google.com)
- GIJN: Journalists' Guide to Using AI and Satellite Imagery for Storytelling:
- [https://gijn.org/2022/02/16/journalists-guide-to-using-ai-and-satellite-imagery-for-storytelling](https://gijn.org)

\* \* \*

In 2019, Reno Gazette Journal environment reporter Benjamin Spillman told the story of how two skiers survived a Sierra avalanche on Jobs Peak, a remote mountain an hour's drive south of Reno on the Nevada-California border. It was a harrowing story of one skier who was buried alive as his friend desperately dug in the snow to find him. It included a sunset helicopter rescue that saved their lives; they would have frozen to death after dark.

Spillman's story began:

> Aaron Zanto describes ski lines in snow the way a painter describes brush strokes on canvas.
>
> When he's skiing the Tahoe area backcountry, the 44-year-old firefighter from Kings Beach strives to make every line meaningful.
>
> "Something that's beautiful going up as well as beautiful going down," is how Zanto describes lines from a great day on snow.
>
> But not every line is beautiful, as Zanto learned during a ski day on Jobs Peak when an avalanche turned his partner's ski line into an ugly smear across the snow.

The story detailed how rescuers used the skiers' GPS trackers to locate them just in time. Spillman and Gazette Journal colleague Brian Duggan used that geolocation data to recreate the skiers' path on the mountain using Google Earth Pro, a free, downloadable software that allows users to create flyover videos and layer locations use shapefile, KML files and GPS data over the earth's landscape.

The result was a 1 minute, 53 second, narrated video that accompanied the story ([Figure 8.1](#ch08.xhtml__15031-5909_ch008_Figure_001)). It recreated the skiers' path and gave readers a sense of perspective of how difficult it was to reach the two men on the mammoth mountain.

Spillman and Duggan had learned the basics of Google Earth Pro during a series of training sessions I had done with the Gazette Journal staff over the previous two years. But the two journalists took that training to the next level with this story and multimedia project.

::: section

## Learning How to Use Satellite Imagery

Google Earth Suite tools and other geolocation, mapping and satellite tools can seem confusing, but they're actually simple to learn with a little training. Satellite imagery and interactive presentations fulfill a storytelling approach journalists have used for years: Show, don't tell. Don't just tell the reader that urban sprawl is an issue around Des Moines, Iowa; you can show it with the Google Earth Timelapse tools. Don't just tell the reader that there was a lot of flooding along the Missouri River in 2019; show it with satellite images. And don't tell the reader that the wildfire or hurricane damage was bad; show it. Give the reader a bird's-eye perspective on an issue.


<a href="#ch08.xhtml_R_15031-5909_ch008_Figure_001"><em>Figure</em> <em>8.1</em></a> Screengrab from the Reno Gazette Journal video on the Jobs Peak skiers


In this chapter, you'll learn how to use satellite imagery tools to produce video flyovers, capture current and historical satellite imagery to tell stories and create timelapses of environmental, disaster and urban changes over the last 40 years. You'll also learn how to use satellite images to fact-check stories and photos.

:::: section
## The Tools

Among the most popular tools are the Google Earth Suite, which provides journalists a bird's-eye view of the world around them. It's excellent for flyover videos and historical imagery (from Google Earth Pro), and you can even build timelapses that show radical environmental changes in Google Earth Engine Timelapse as well as Google Earth.

Since 2019, many journalists have shifted from Google Earth Pro -- software that you download for free to your desktop -- to Google Earth Studio, a browser-based tool used for building short video orbits, zooms and flyovers. The tool also lets you export still images from the web-based interface as well. Earth Studio has some, but not all, of the features of Earth Pro, but it's simple to use and produces fantastic 3D renderings of buildings and landscapes.

\* \* \*

<aside aria-label="box1" class="box1" epub:type="tip" role="doc-tip" title="box">


::: section

## Rights-Free Images 

All images from any Google Earth tools are rights-free. Many come from government agencies such as NASA, the USGS, etc., and are public record anyway. Just make sure the Google Earth watermark appears on the image or video, or add it to a cutline. If you have concerns, you can look up the legal requirements in the Google Brand Center ([https://google.com/permissions](https://google.com)).

Images from other sites may require permissions and fees before or even after downloading. Be sure to look for watermarks on photos and reach out to the sites and owners to get written permission before publishing. Some of the images can be expensive.

</aside>

\* \* \*

::::: section
## Google Earth Pro and Telling the Story of Chicago's Lakefront

Chicago's beaches are quickly washing away. The city's skyline that borders Lake Michigan has seen a threat of rising lake waters over the past decade. Beaches that border the lakefront are vanishing, homes on the North and South Sides of the city are getting washed away. It's a serious concern for city officials.

In the fall of 2020, three of my UIC communication students set out to document the problem as part of a class project they produced for The Red Line Project, our lab website that covers news and urban issues in the city. They used Facebook neighborhood pages to track down sources to interview for the story. They shot photos of the beaches. They talked to expert sources. But in the end, they had to show, not tell, the reader there was a problem.

Illustrating it wasn't easy. We didn't have a drone and a chopper ride was too expensive.

So we turned to three free tools:

- Google Earth Pro, which we downloaded to our lab iMacs.
- Juxtapose JS, an incredible photo slider tool developed by the Knight Lab at Northwestern University.
- Adobe Spark Video (now part of its Express creative suite) that they used to create a short social media video that also was embedded into the story.

The students targeted several beaches: Foster Beach, Ohio Street Beach, Oak Street, Montrose and the Belmont Harbor dog beach, which has nearly vanished in less than a decade.

The students opened Google Earth Pro, clicked on the "Show Historical Imagery" button (icon with the clock) at the top of the toolbar ([Figure 8.2](#ch08.xhtml__15031-5909_ch008_Figure_002)).

To download the image, they hit the Save Image button (third from the right) in that same toolbar. Some graphics will overlay the image. To turn them off, click on the Map Options button and uncheck the radio buttons. Then hit the "Save Image" button to the right and the image will download to your computer ([Figure 8.3](#ch08.xhtml__15031-5909_ch008_Figure_003)).


<a href="#ch08.xhtml_R_15031-5909_ch008_Figure_002"><em>Figure</em> <em>8.2</em></a> Belmont Harbor Dog Beach historical images interface in Google Earth Pro


<a href="#ch08.xhtml_R_15031-5909_ch008_Figure_003"><em>Figure</em> <em>8.3</em></a> Google Earth Pro map options button


Now that they had the most current image -- they vary by location -- the students used the slider at the top of the tool to move back in time and see what the beach looked like three, seven, even 10 years earlier. They chose an image from 2013 that showed a much bigger Belmont Harbor Dog Beach, and downloaded.


<a href="#ch08.xhtml_R_15031-5909_ch008_Figure_004"><em>Figure</em> <em>8.4</em></a> A Juxtapose slider of Chicago’s disappearing Foster Beach (<em>Interactive graphic</em>) <em>Source:</em> <a href="https://bit.ly/fosterbeachslider">https://bit.ly/fosterbeachslider</a> 


Now that they had two before/after images, they placed the images on our Wordpress server, saved the published link to the images and opened Juxtapose JS. It's an intuitive tool with a form on the home page interface that they used to build the photo slider. They pasted the photo links into their respective field, added the dates and source (Google Earth) and hit the publish button. Juxtapose gave them a hotlink and embed code to add it to the site ([Figure 8.4](#ch08.xhtml__15031-5909_ch008_Figure_004)).

Then the students downloaded before/after images of several other Chicago beaches and incorporated them into a short video in Adobe Spark Pro. Their original plan was to use the video to tease the story as part of a social media campaign, which you learned about in [Chapter 4](#ch04.xhtml__15031-5909_ch004); but the video turned out so well, they embedded it at the top of the story.

Juxtapose isn't the only tool where you can share slider images. Flourish.studio has a slider tool. And the Indianapolis Star used Canva and Instagram to share before/after images showing the growth of McCordsville, Indiana ([Figure 8.5](#ch08.xhtml__15031-5909_ch008_Figure_005)) as part of a series of posts about urban growth in the area.

\* \* \*


<a href="#ch08.xhtml_R_15031-5909_ch008_Figure_005"><em>Figure</em> <em>8.5</em></a> Indianapolis Star Instagram post with Google Earth images


<aside aria-label="box2" class="box1" epub:type="tip" role="doc-tip" title="box">


::: section

## Video: Basics of Google Earth Pro 

Learn how to use the tool for fact-checking, zoom-in videos and how to find locations on the moon and Mars. <https://bit.ly/earthprodemo>

</aside>

\* \* \*


::: section
### ***Exercise 1: Pick a Chicago Beach and Build Your Own Photo Slider***

Choose from this list of beaches and build your own photo slider like the UIC students did. Or choose an area of your campus or city. Maybe you've had a new football stadium or arena built, or a large retail or housing development. What did the area look like before, during and after construction?

- Belmont Harbor Dog Beach
- Oak Street Beach
- Foster Beach
- Montrose Beach
- Ohio Street Beach

\* \* \*

::::: section
## How to Use Google Earth Engine Timelapse

Timelines are a powerful storytelling tool for journalists. As mentioned earlier in the chapter, showing how an area changes over time can be worth thousands of written words about it. As of early 2023, Google has two timelapse tools that make it easy to incorporate timelapses into your reporting:

- Google Earth Engine Timelapse (1984--2021), which you can link to or embed in a website.
- You also can do timelapses in the Google Earth browser-based version with images from 1987 up to 2023, but you can only link to the interactives, not embed them in your page as with the Earth Engine Timelapse tool.

Timelapses are helpful for telling many types of stories. For instance, if you're writing a census story about population growth in your area, you could do a timelapse to see how the city has grown over the past 30 or 40 years.

For example, open Google Earth Engine Timelapse, then search on Las Vegas and zoom out a bit. You'll see the city's explosive growth, but also note how Lake Mead shrinks over time ([Figure 8.6](#ch08.xhtml__15031-5909_ch008_Figure_006)). You can get the embed code or link by clicking the button next to the search field. You can adjust the speed of the interactive player by clicking on the "0.5" link in the lower right corner of the player.


<a href="#ch08.xhtml_R_15031-5909_ch008_Figure_006"><em>Figure</em> <em>8.6</em></a> Google Earth Engine Timelapse frame of Las Vegas, Nevada. (<em>Interactive graphic</em>)


Some other cities to try are Dubai, Cancun, Cabo San Lucas and your city. The tool limits how far you can zoom in depending on the area. It stitches together hundreds of thousands of satellite images and can take some time to update.

An excellent example of how to use the tool came from a training I did at the San Antonio Express News. Staffer Fernando Ramirez built a slideshow of Earth images showing how Texas cities have changed over the years. The expansion on the I-35 corridor between Austin and San Antonio is amazing.

You can show development as well. Search for O'Hare International Airport and zoom in. You'll see the airport's south runway expansion explode on the earth's surface. Search for suburbs in your community and see the growth.

\* \* \*

<aside aria-label="box3" class="box1" epub:type="tip" role="doc-tip" title="box">

::: section

## Video: How to Use the Latest Version of Google Earth Engine Timelapse 

In this training video, learn how to use Timelapse to show population growth and environmental changes: [www.youtube.com/watch?v=TlmEz4o2wzQ](http://www.youtube.com)

</aside>

\* \* \*

Timelapse tools are best at showing environmental changes and disasters: wildfires, hurricane damage, flooding, drought, strip mining, deforestation and more. For example, open Google Earth Engine Timelapse, then search on Nebraska City, Nebraska. Watch the video play through and note that in 2019, the Missouri River, just to the east of the city, floods into farmland and washes out two highways: Interstate 29 and State Highway 2 ([Figure 8.7](#ch08.xhtml__15031-5909_ch008_Figure_007)). You can embed this graphic on your site, or do a screengrab of 2019 and use the image with your story.

You also can try this with the Malibu wildfires, Napa Valley wildfires, the Australia bushfires and the many hurricanes and typhoons that have hit cities around the world.

\* \* \*

<aside aria-label="box4" class="box1" epub:type="tip" role="doc-tip" title="box">

::: section
## Pro tip: Alternatives to Google Earth Pro for Historical Images 

While the Google Earth desktop version won't let you find historical images to download, you can use its timelapse tool to target a specific year and do a screengrab of the image. It's not as clean as the Earth Pro archives, though, but it works in a pinch. You also can find historical satellite images from other sources on JournalistsToolbox.ai.

</aside>


<a href="#ch08.xhtml_R_15031-5909_ch008_Figure_007"><em>Figure</em> <em>8.7</em></a> Missouri River flooding in 2019 in the Google Earth Timelapse browser-based tool


\* \* \*

:::: section

## How to Use the Google Earth Measure Tool

The measure tool is often overlooked by journalists, but it's a very useful tool that's available in the Google Earth desktop version. For example, suppose you are a reporter in Las Vegas covering the shooting at the Route 91 Harvest Festival in October 2017, and you needed to know how far the gunman was from the concert area. The gunman was perched in a suite in the Mandalay Bay hotel across the street from the open, outdoor concert venue.

This distance is important to know if you have the type of guns the suspected shooter was using. If you know the range of the guns and the distance the shooter was from the venue, you could tell readers -- and show them -- if all concert goers were in range of the gunfire.

Here are the steps to follow

1.  Open [Earth.google.com](https://www.Earth.google.com) and click on the ruler icon near the top left of the screen.
2.  Type Route 91 Harvest Festival in the search field and hit return.
3.  Use the +/− Zoom buttons in the lower right to show the concert area (concrete slab) along with the northeast corner of the Mandalay Bay hotel.
4.  Then click on the measure tool, a ruler icon at the bottom of the left toolbar on the left.
5.  Now click at the base of the northeast corner of the hotel and then double-click in the concert area. I chose the area near the bottom of the venue, where the stage was. A dialog box pops up and shows the distance (360 yards on mine). You can drag the ends of the line around to adjust the distances ([Figure 8.8](#ch08.xhtml__15031-5909_ch008_Figure_008)).
6.  You can adjust the type of distance in the pulldown menu in the dialog box. You can set it to yards, feet, meters, inches, miles, acres (area), even nautical miles over water.


<a href="#ch08.xhtml_R_15031-5909_ch008_Figure_008"><em>Figure</em> <em>8.8</em></a> Google Earth Measure tool from Las Vegas shooting


The tool also is helpful for measuring the distance of a police chase. You can use it to measure area, too, by clicking on corners around a specific area. This can be good for double-checking property and property tax records.

\* \* \*

<aside aria-label="box5" class="box1" epub:type="tip" role="doc-tip" title="box">

::: section
## Video: Google Earth Measure Tool and [MapChecking.com](https://www.MapChecking.com) 

Watch a step-by-step exercise on how to use the Earth Measure Tool and how to estimate crowd sizes using [MapChecking.com](https://www.MapChecking.com): [www.youtube.com/watch?v=L_3PeBUtcTw](http://www.youtube.com)

</aside>

\* \* \*

:::: section

## How to Use Satellite Images for Fact-Checking

Journalists often use satellite and street view imagery from Google Earth and other tools to fact-check images and other claims. The BBC News Africa Eye team famously did this in 2018 to uncover the truth of the slayings of two women and two children by the Cameroon military. The Cameroon government initially dismissed the video as "fake news." But BBC Africa Eye used forensic analysis of the viral video footage, proving exactly where this happened, when it happened and who was responsible for the killings.

Google Earth played a key role in the forensics work, which was detailed in a Twitter thread posted by the team as well as some stories and videos. The BBC used Google Earth to determine the location of the slayings (Cameroon's government claimed it occurred outside the country) by matching mountains in the background of the viral video to Earth's 3D imagery of the landscape.

It places the scene on a dirt road outside a town called Zelevet, in the far north of Cameroon, close to the border with Nigeria. Cameroon soldiers were fighting the jihadist group Boko Haram in that area.

Once they confirmed the general location, the fact-checkers looked at other details in the film -- tracks, buildings, trees -- and matched them with the satellite imagery ([Figure 8.10](#ch08.xhtml__15031-5909_ch008_Figure_010)).

The team also used archival images from Google to determine that the murders occurred during the hot dry season, matching the topography in the video to the archived photos.

The team used the video to match the uniforms of the soldiers in the video and their weapons to those worn and used by the Cameroon military. Another search in Google Earth showed that a small military camp was located near the area where the shootings occurred. A few searches on Facebook matched a soldier's page with that of the name of a soldier mentioned in the video.

Once the investigation was posted, the Cameroon government reversed its position and admitted its military was at fault.

Journalists around the world have used many other satellite image tools to fact-check and investigate coal plants, water conflicts, illegal flaring and Chinese re-education camps. Ed Boyda and Dan Hammer for Earthrise Media have recommended dozens of satellite imagery tools for investigations and fact-checking.

\* \* \*


::: section
### ***Exercise 2: Fact-Check a Photo***

Let's say you're working a social media shift for your outlet and someone you don't know tweets you a photo at you of this cathedral and it's on fire: <https://bit.ly/cathedralcheck>

You're unfamiliar with the Twitter account but nothing seems out of the ordinary in the bio or the stream of tweets. The person identifies the church as the Cathedrale de Monaco in Monaco City, near the Monaco Grand Prix F1 race route.

As a journalist, take pause before sharing this. Go to [earth.google.com](https://www.earth.google.com) and search Cathedrale de Monaco. You'll get a satellite view of the area. Now drag the small, orange "peg man" icon in the lower right corner of Google Earth to one of the blue lines that form in front of the church. You'll have a "Photo Sphere" of a streetview image of the church.

Upon closer examination, you'll see the Cathedrale de Monaco in Google Earth ([Figure 8.9](#ch08.xhtml__15031-5909_ch008_Figure_009)) looks nothing like the photo tweeted to you. That's because the photo the person sent is actually the Duomo in Milan, Italy. This is a common prank people like to play on journalists -- misrepresent a location or even take an old news photo and say that it happened today instead of several years ago.


<a href="#ch08.xhtml_R_15031-5909_ch008_Figure_009"><em>Figure</em> <em>8.9</em></a> The Cathedrale de Monaco shown in a Google Earth photo sphere


Don't fall for it. Take the time to fact-check on Google Earth.

\* \* \*

::: section
## Examples of Satellite Imagery in Storytelling

Newsrooms large and small have embraced the bird's-eye view for storytelling. Here are some creative uses of Google Earth and other satellite image tools from professional newsrooms:

- **NBC Bay Area: Hunters Point Shipyard Contamination, Cleanup and Development**
- [www.nbcbayarea.com/investigations/San-Francisco-Hunters-Point-Contamination-Cleanup-Development-494440271.html](http://www.nbcbayarea.com)
- **New York Times Graphic: Las Vegas Shooting: Chaos at a Concert and a Frantic Search at Mandalay Bay**
- [www.nytimes.com/interactive/2017/10/02/us/mandalay-bay-vegas-shooting.html?smid=tw-nytimes&smtyp=cur](http://www.nytimes.com)
- **Fort Myers Beach, Hurricane Ian: Earth archived satellite images:** [https://twitter.com/drewmacfarlane/status/1575542302180839446?s=51&t=He1_gWaGSB6La5vi7eN-nQ](https://twitter.com)
- **Desert Sun: Wildfire Prevention Video in San Diego**
- [www.desertsun.com/in-depth/news/2019/08/01/san-deigo-fire-chief-oks-wildfire-hazard-development-new-homes-adara-otay-ranch-chula-vista/1664951001](http://www.desertsun.com)
- **USA Today: Google Earth and Timelapse on Amazon Rainforest Wildfires**
- [www.usatoday.com/in-depth/news/2019/08/23/amazon-rainforest-six-charts-explain-why-fires-matter/2096257001](http://www.usatoday.com)
- **The Vanishing of Candlestick Park (Instagram)** [www.instagram.com/reel/CidnBmxASCj/?igshid=YmMyMTA2M2Y=](http://www.instagram.com)
- **USA Today Graphics: Social Video for Amazon Rainforest Wildfires**
- [https://twitter.com/usatgraphics/status/1165036342906097672l](https://twitter.com)
- **Decatur (Illinois) Herald Review: Bridges Project**
- [https://herald-review.com/news/local/public_safety/watch-now-macon-county-engineers-study-options-for-local-bridges/article_46899560--207f-59eb-916a-c59bdda8263a.html](https://herald-review.com)
- **Kelly Fincham: Before/After Slider: Concrete Sprawl in Bettystown Ireland Housing**
- [http://kellyfincham.com/myblog/concrete-sprawl-in-bettystown-housing](http://kellyfincham.com)
- **Wisconsin State Journal: Google Earth Pro Video of Wisconsin Men's Basketball Tour of New Zealand and Australia**
- [www.youtube.com/watch?v=MKu4Lzd9wi0](http://www.youtube.com)
- **Los Angeles Times: Google Earth Pro and Open Street Maps: Kobe Bryant Helicopter Crash**
- [https://twitter.com/palewire/status/1221576809558360064?s=12h](https://twitter.com)
- **Los Angeles Times: Google Earth Pro: Analysis of Kobe Bryant Helicopter Path**
- [www.latimes.com/projects/kobe-bryant-helicopter-crash-3d-map](http://www.latimes.com)
- **Louisville Courier-Journal: Tour of Nasty 9 Louisville Golf Holes**
- [www.courier-journal.com/story/sports/golf/2018/06/19/hardest-golf-holes-we-love-hate-louisville/703597002](http://www.courier-journal.com)

\* \* \*

::: section

## Satellite Imagery Tools

Besides the tools already mentioned in this chapter, here are some more resources for finding satellite images:

- **Google Earthview Chrome Plug-In**
- [https://chrome.google.com/webstore/detail/earth-view-from-google-ea/bhloflhklmhfpedakmangadcdofhnnoh?hl=en](https://chrome.google.com)
- **NASA Worldview**
- <https://worldview.earthdata.nasa.gov>
- Satellite imagery galore.
- **NASA LandSat Image Gallery**
- [https://svs.gsfc.nasa.gov/Gallery/Landsat.html](https://svs.gsfc.nasa.gov)
- Hundreds of satellite images of Earth that are rights-free.
- **Digital Globe**
- [www.maxar.com](http://www.maxar.com)
- Satellite and geospatial data resources. Requires a fee.
- **GIJN: Resources for Finding and Using Satellite Images**
- [https://gijn.org/resources-for-finding-and-using-satellite-images](https://gijn.org)
- **Chips App: Create Satellite Chips**
- [https://yoninachmany-streamlit-geospatial-streamlit-app-1qn4j9.streamlit.app/](https://yoninachmany-streamlit-geospatial-streamlit-app-1qn4j9.streamlit.app)
- An interactive web app for creating Landsat or other imagery chips for any location around the globe.
- **Kartaview**
- [https://kartaview.org/landing](https://kartaview.org)
- Works similar to Google Street View.

\* \* \*


:::::: section
:::: section
### ***Exercise 3: Create a Zoom-in with Google Earth Studio***

Before using Google Earth Studio ([www.google.com/earth/studio](http://www.google.com)), create a login with your Google/Gmail credentials, hit the arrow in the green "Blank Project" section and select one of the quick starts (spiral or orbit). Type a location into the field and click the arrow right button. Your video will appear (see [Figure 8.10](#ch08.xhtml__15031-5909_ch008_Figure_010)).

Then hit the red "Render" button in the upper right corner of the interface. Here's where it gets tricky. In the upper right corner, hit the request button for cloud rendering. In a few days, you'll receive an email granting you access.

This will allow you to store future projects in the cloud, and, more importantly, export them as MP4 video files (see [Figure 8.11](#ch08.xhtml__15031-5909_ch008_Figure_011)).

Without cloud rendering, you can still export the video as a JPEG image sequence, but you'll need to convert it to a MOV or MP4 file in another piece of software, such as Adobe Premiere. That's a bit of a hassle, so signing up for the free cloud rendering is the way to go.

Featured in [Figure 8.11](#ch08.xhtml__15031-5909_ch008_Figure_011) is the export interface for an Earth Studio orbit video of Wrigley Field. Note the "mp4" video option is checked in the upper right. You also can move the Google Earth watermark using the tools to the right of the video. The interface also gives you frames per second and dimensions for sizing your video.


<a href="#ch08.xhtml_R_15031-5909_ch008_Figure_010"><em>Figure</em> <em>8.10</em></a> Wrigley Field orbit in Google Earth Studio


<a href="#ch08.xhtml_R_15031-5909_ch008_Figure_011"><em>Figure</em> <em>8.11</em></a> Google Earth Studio video rendering interface


Once you hit the render button, the software will tell you the process has started, and it will email you several minutes later with a link and download option once it has finished.

\* \* \*

<aside aria-label="box6" class="box1" epub:type="tip" role="doc-tip" title="box">

::: section
## Video: Google Earth Studio 

Learn how to create zoom-in videos and export them in this browser-based tool.

<https://bit.ly/earthstudiovideo>

</aside>

\* \* \*

::: section
### ***Exercise 4: Google Earth Pro: Video Flyover of Big Ten Stadiums***

When I traveled around the United States doing Google tools trainings from 2016 to 2023, one of the most popular exercises I'd do with journalists was to teach them how to do tours in Google Earth Pro. You can do anything: A tour of local sights in your state, your college campus, cool architecture around the world, sports stadiums and arenas

Start by downloading Google Earth Pro here. You also can do this exercise in Google Earth Studio. Using Google Earth Pro, locate these stadiums and create a tour of them, then try to record and export the tour from the folder you create. Use the Earth Pro training video (<https://bit.ly/earthprodemo>) to see how Earth Pro works.

- Ohio Stadium (Columbus, Ohio/Ohio State University)
- Camp Randall Stadium (Madison, Wisconsin/University of Wisconsin)
- Memorial Stadium (Lincoln, Nebraska/University of Nebraska)
- Michigan Stadium (Ann Arbor Michigan/University of Michigan)
- Spartan Stadium (Lansing, Michigan/Michigan State)
- Beaver Stadium (Happy Valley, Pennsylvania/Penn State)
- Ryan Field (Evanston, Illinois/Northwestern University)
- Kinnick Stadium (Iowa City, Iowa/University of Iowa)
- TCF Bank Stadium (Minneapolis, Minnesota/University of Minnesota)
- Memorial Stadium (Champaign, Illinois/University of Illinois)
- Byrd Stadium (College Park, Maryland/University of Maryland)
- High Point Solutions Stadium (Piscataway Township, New Jersey/Rutgers University)
- Ross-Ade Stadium (West Lafayette, Indiana/Purdue University)
- Memorial Stadium (Bloomington, Indiana/Indiana University)
- The Rose Bowl (Pasadena, California/UCLA)
- The Los Angeles Coliseum (Los Angeles, California/USC)
- Autzen Stadium (Eugene, Oregon/University of Oregon)
- Husky Stadium (Seattle, Washington/University of Washington)

Some stadium tour examples:

- Hookem: Big 12 Stadium Tour in Google Earth
- <https://bit.ly/big12tour>
- Columbus Dispatch: Ohio State Football Road Schedule
- [www.youtube.com/watch?v=KO74tpmNts8](http://www.youtube.com)

\* \* \*

::: section

## Footnotes

- Adobe Express (Spark) Video Editor: [www.adobe.com/express/create/video](http://www.adobe.com)
- BBC News Africa Tweets on Cameroon Murders Digital Forensics: [https://twitter.com/BBCAfrica/status/1044186344153583616](https://twitter.com)
- BBC News: Cameroon: The Truth Behind a Viral Video Murder: [www.bbc.com/news/world-africa-45681690](http://www.bbc.com)
- DNAInfo Chicago: Lollapalooza Stages Within Assault Rifle Firing Distance from Chicago Hotel: [www.dnainfo.com/chicago/20171005/loop/chicago-hotel-las-vegas-shooter-stephen-paddock-lollapalooza-blackstone-map](http://www.dnainfo.com)
- Exercise: Cathedral Photo: <https://bit.ly/cathedralcheck>
- From Above: <https://bit.ly/fromaboveguide>
- GIJN: Journalists' Guide to Using AI and Satellite Imagery for Storytelling: [https://gijn.org/2022/02/16/journalists-guide-to-using-ai-and-satellite-imagery-for-storytelling](https://gijn.org)
- Google Brand Resource Center: [https://about.google/brand-resource-center](https://about.google)
- Google Earth: [https://earth.google.com/web](https://earth.google.com)
- Google Earth Engine Timelapse: [https://earthengine.google.com/timelapse](https://earthengine.google.com)
- Google Earth Pro Download (Google Suite): [www.google.com/earth/versions](http://www.google.com)
- Google Earth Studio: [www.google.com/earth/studio](http://www.google.com)
- Journalist's Toolbox Satellite Imagery: [www.journaliststoolbox.org/2023/03/24/satellite-imagery](http://www.journaliststoolbox.org)
- Juxtapose JS: <https://juxtapose.knightlab.com>
- Juxtapose Slider of Foster Beach: <https://bit.ly/fosterbeachslider>
- The Red Line Project: Why Is Chicago's Lakefront Washing Away? [https://redlineproject.org/rising_lakefront.php](https://redlineproject.org)
- Reno Gazette Journal: Broken Leg and Impending Darkness: How Two Skiers Survived a Sierra Avalanche on Jobs Peak: [www.rgj.com/story/life/outdoors/2019/03/22/nevada-skiers-barely-escaped-jobs-peak-accident-before-nightfall/2943310002](http://www.rgj.com)
- San Antonio Express News: How Texas Cities Have Changed Over the Years: [www.mysanantonio.com/news/local/texas/article/Google-Timelapse-shows-how-Texas-cities-changed-10691779.php](http://www.mysanantonio.com)
- State of the Planet: How Journalists Can Track Down Great Satellite Images in Realtime: [https://news.climate.columbia.edu/2021/03/31/find-satellite-images-journalism](https://news.climate.columbia.edu)
- Tech Journalism: Fact-Checking with Open Source Satellite Images: [https://techjournalism.medium.com/fact-checking-with-open-source-satellite-images-part-1-8a76962c76e5](https://­techjournalism.medium.com)
- Video: Columbus Dispatch: Ohio State Football Road Schedule: [www.youtube.com/watch?v=KO74tpmNts8](http://www.youtube.com)
- Video: Google Earth Pro Basics: <https://bit.ly/earthprodemo>
- Video: Google Earth Studio Training Video: <https://bit.ly/earthstudiovideo>
- Video: Hookem: Big 12 Stadium Tour in Google Earth: <https://bit.ly/big12tour>
- Video: How to Use Google Earth Engine Timelapse: [www.youtube.com/watch?v=TlmEz4o2wzQ](http://www.youtube.com)
- Video: How to Use the Google Earth Measure Tool: [www.youtube.com/watch?v=L_3PeBUtcTw](http://www.youtube.com)


# 9 Artificial Intelligence \| Productivity Tools

DOI: [10.4324/9781003431787-10](https://doi.org/10.4324/9781003431787-10){aria-label="D.O.I. link to this document."}

\* \* \*


**Key Resources**

- JournalistsToolbox.ai: <http://journaliststoolbox.ai>
- Google News Product Database: <https://learning.newsproduct.org>
- Beginner's Prompt Handbook: ChatGPT for Local News Publishers: <https://bit.ly/ailocalbook>
- Partnership on AI: Responsible Framework for Synthetic Media: [https://syntheticmedia.partnershiponai.org/#read_the_framework](https://syntheticmedia.partnershiponai.org)
- AI Tools for Local Newsrooms: <https://bit.ly/aitoolslocal>

\* \* \*

**Editor's note:** This chapter was written in the summer of 2023. AI tools are developing and disappearing on a daily basis, so some tools in this chapter may have changed or no longer exist. Check the [JournalistsToolbox.ai](http://JournalistsToolbox.ai) site for updates.

> Once upon a time, the world was a realm of unanswered questions and there was room in it for poetry. Man stood beneath the sky and he asked "why?". And his question was beautiful. The new world will be a place of answers and no questions, because the only questions left will be answered by computers, because only computers will know what to ask. Perhaps that is the way it has to be.
>
> -- British journalist James Cameron, 1969


<em>Figure</em> <em>9.1</em> AI may seem like an assembly line to some journalists, but it can speed productivity <em>Source:</em> Illustration/Billy O’Keefe


Google's Simon Rogers posted Cameron's cryptic quote in an "AI for Data Storytelling" post in March 2023 as hundreds of new AI tools were pouring into the market each week.

Rogers responded: "What Cameron didn't know was that data journalists would be the ones to answer those questions now; they just weren't able to find out the answers before AI was there to help them. That human factor leads to some really powerful work."

This chapter will examine the role that evolving AI tools play in the journalist's daily workflow and how they can improve efficiency. You'll learn from hands-on exercises the benefits, limitations and drawbacks of AI tools and how to use them correctly.

\* \* \*

<aside aria-label="box1" class="box1" epub:type="tip" role="doc-tip" title="box">

::: section
## Video Playlist: AI Tools 

Learn how to use dozens of AI-driven tools to make you more efficient in this YouTube playlist: <https://bit.ly/aitoolsvideo>

\* \* \*

</aside>

:::: section

## The Gold Rush of AI Tools

The influx of AI tools in 2023 -- they've been around for decades, by the way -- have set the news industry on alert. Would these automated tools eliminate jobs? Could they generate accurate content? How much human supervision does there need to be with the tools? Can they really make us more efficient, especially in smaller, local newsrooms?

People fear what they don't understand. When the web hit the mainstream in the mid-1990s as affordable home computers and dial-up modems flooded into homes, newsrooms feared that it would gut legacy media. Much of that fear was justified. Newsrooms panicked again with social media when Web 2.0 and smartphones arrived between 2005 and 2007. The shift to video for newspaper companies failed miserably a few years later. So we have seen a similar pattern as AI tools hit the mainstream market in the last couple of years.

Ashley Hamer of Descript, an AI-driven audio, video editing and transcription tool, summarized the concerns in a 2023 blog post:

> For many creators, their first reaction to generative AI tools like ChatGPT and DALL-E is fear: fear that they'll be replaced, or that human creativity will stop being valued. Those fears are valid, but there's another way to frame this new AI-centered world we're entering. That is, AI tools can free humans of creative blocks and mundane tasks so they can be more creative.
>
> In fact, there is a wide world of AI tools designed specifically to help specific kinds of creators free themselves from the tasks that slow them down and hamper their creativity. Are you a playwright who's trying to come up with the next scene? Maybe a musician trying to mix up an overused chord progression? Or, ahem, a podcaster who needs to make a quick correction to something you already recorded? There are AI tools out there for you.

So now, the question remains: How can AI be used ethically and accurately by journalists while also saving time and making the product better? I encourage journalists that I train to approach it with a "cautious curiosity." Study it and see how it can help you. Fact-check everything. Be skeptical but experimental. Apply sound ethics and keep an eye on copyright and intellectual property cases. Think before doing. Question everything. But stay open-minded.

"AI-fueled automation. The variety of digital storytelling themes have, thus far, required a lot of time and technical expertise to do, especially at the beginning," said Mackenzie Warren, who oversees Medill's Local News Accelerator. "As time goes on, the tools get simpler and more powerful and the producers get more capable. AI-fueled automation will accelerate both of those trends even further. We will be able to have more social, mobile, data and multimedia content than we'd ever dreamed possible -- instantly and on-command.

"This will require higher levels of scrutiny and editing to ensure that the quality and trustworthiness of the content matches the volume and speed with which we can create it. This also will raise the value of journalists as curators -- the ones to select and prioritize the small number of very best pieces of content from among an unlimited supply."

Much of the early focus in the AI gold rush has been on ChatGPT (Generative Pre-Trained Transformer), the open-source AI tool that can help you find information. It uses machine learning and pre-programming to find your answers. It sometimes cites sources, but not always, so fact-checking anything you find in the tool is paramount.

In early 2023 Microsoft invested \$10 billion in ChatGPT to leapfrog Google in the AI game. Some school districts banned it based on fears that students will use it to cheat.

\* \* \*

<aside aria-label="box2" class="box1" epub:type="tip" role="doc-tip" title="box">

::: section
## Video: ChatGPT Basics 

Learn how to write basic prompts and see what the OpenAI tool does well ... and what it does not. <https://bit.ly/gptvideo>

</aside>

\* \* \*

DALL-E, MidJourney and other text-to-image and text-to-video tools produce some stunning images, but also raise concerns about ethics, copyright, intellectual property, transparency, truth-telling and commercial use of the images produced.

Reporters also should be wary of PR press releases and pitches, some which are generated by AI tools and are inaccurate. For example, Kashmir Hill (@Kashmir Hill) tweeted in May 2023 about receiving a PR pitch that "expressed admiration for a book I did not write and which does not exist. The PR firm had used ChatGPT. Beware of AI hallucinations, early adopters."

But while the AI tools raise concerns, they also introduce many opportunities, said Jeff Jarvis, a journalism professor at the City University of New York (CUNY) and author of the book "Geeks Bearing Gifts". Jarvis wrote about AI's potential in a late 2022 blog post called "Writing and Exclusion".

"I am struck by the opportunity presented by generative AI -- lately and specifically ChatGPT -- to provide people with an opportunity to better express themselves, to help them write, to act as Cyrano at their ear," Jarvis wrote. "Fellow educators everywhere are freaking out, wondering how they can ever teach writing and assign essays without wondering whether they are grading student or machine. I, on the other hand, look for opportunity -- to open up the public conversation to more people in more ways."

AI isn't a means to an end with writing news stories -- something we'll explore later in this chapter -- but it offers many features that can help with writer's block, analyze and summarize text, rethink phrasing and help generate sources and ideas, all of which will have to be double-checked for accuracy. ChatGPT's plug-ins, such as ScholarAI and Daigram, can summarize research and visualize data accurately in a matter of seconds.

"This is an opportunity to teach students the limitations and biases of AI and large language models," Jarvis wrote. "Users must understand when they are listening to a machine that is trained merely to predict the next most sensible word, not to deliver and verify facts; the machine does not understand meaning.

"They also must realize when the data used to train a language model reflects the biases and exclusions of the web as source -- when it reflects society's existing inequities -- or when it has been trained with curated content and rules to present a different worldview. The creators of these models need to be transparent about their makings and users must be made aware of their limitations."

Digital media pioneer Damon Kiesow said his skepticism of most new technology recently is the entirely blinkered and self-serving nature of its greatest proponents.

"AI is going to be a huge benefit for journalists, if we think of it as a tool to improve, not replace, our creative work," said Kiesow, a Knight Chair in Digital Editing and Producing at the Reynolds Journalism Institute at the University of Missouri. "If we think of the model as 'spellcheck' but for everything, and 'Google Alerts' but for everything -- that is the foundation of the news-specific directions I would like to see us chasing.

"Unfortunately, the venture capital money is intent on disrupting Google's search dominance -- which is where the advertising money is -- and has created the most human-like AI to date: it thinks it knows everything and doesn't mind guessing with unearned confidence. We need to get past that hype cycle to start creating real value for the tech."

::: section

## What Can AI Do for Journalists?

Joe Amditis saw the potential AI has for small, local newsrooms, so in early 2023 he wrote a free book on Notion entitled "Beginner's Prompt Handbook: ChatGPT for Local News Publishers".

Amditis, assistant director for products and events at the Center for Cooperative Media at Montclair State University, created the book to offer specific examples on how to write good prompts and unexpected use cases for newsrooms.

"I decided to write this ebook after being duped into paying \$2 for a shitty prompt handbook that was clearly generated using ChatGPT instead of written by a real person," Amditis said. "It was frustrating to see the hustle-culture grifters taking advantage of this emerging technology without taking the time to actually explain its capabilities and limitations. I wanted to provide a reliable and informative guide that would help local news publishers effectively use ChatGPT to save time and stress."

He's quick to point out how AI can remove some of the routine, mundane journalists and other newsroom staff perform each day:

> Instantly generating summaries of public meetings and documents, creating tweets and social posts from news stories, drafting scripts for news broadcasts, even suggesting different headline variations -- all at the click of a button -- would be a game-changer for news organizations that are already strapped for people and resources.
>
> The same thing goes for generating invoices, public records requests, and even basic outreach emails. Not to mention the implications of ChatGPT's ability to generate code using natural-language inputs.

Amditis lists dozens of uses for ChatGPT and other AI for news publishers in his free book. Some of those, along with some examples from The Associated Press, are in [Table 9.1](#ch09.xhtml__15031-5909_ch009_tab_001).


  ------------------------------------------------------------------------------------------------------------------ ---------------------------------------------
  Automate public meeting summaries                                                                                  Email sorting and classification

  Rapid HTML construction, coding                                                                                    Organize and format police blotters

  Draft scripts for news broadcasts or podcasts                                                                      Generate interview questions

  Create outlines for plans and stories                                                                              Keyword lists and hashtags for SEO

  Brainstorming headlines                                                                                            Help with writer's block

  Create transcripts of audio/video recordings                                                                       Generate lists of story ideas

  Data scraping                                                                                                      Create data visualization

  Language translation                                                                                               Translate coding languages

  Create event agendas and materials                                                                                 Quickly creating lists of FAQs

  Respond to FAQs for a project or story                                                                             Summarize/extract info from a block of text

  Keyword extraction (metadata, reporter alerts)\                                                                    \
  Convert weather service alerts to other languages\                                                                 \
  Suggest alternative angles or perspectives for a story\                                                            
  Create social media calendars and publishing schedules                                                             

  Automating routine administrative tasks like scheduling, invoicing and record-keeping                               

  Draft meeting outlines, project budgets and grant proposals                                                         

  Generate templates for different types of news stories, like obituaries, crime reports and human-interest pieces    

  Generate customized newsletters based on user preferences and interests                                             

  Analyze social media and other online sources for story leads and trends                                            

  Generating news quizzes and other information-based games and activities                                            

  Create and execute onboarding and employee training protocols                                                       

  Categorize and label community feedback for later analysis and response                                             

  Develop AI chatbots for engaging with readers and providing customer service                                        

  Act as a learning guide for personal and professional development                                                   
  ------------------------------------------------------------------------------------------------------------------ ---------------------------------------------

  : [[Table 9.1](#ch09.xhtml_R_15031-5909_ch009_tab_001)] Uses for AI in local newsrooms

\* \* \*

Amditis said ChatGPT can be used for generating partnership agreements, memorandums of understanding for collaborative reporting projects and other journalism initiatives. The ability to have ChatGPT generate and populate template agreements like the Collaborative Journalism Partnership Agreement or a Collaborative Journalism MOU have made it much easier -- and cheaper -- for news collaboratives to use these types of documents as a starting place for establishing the relationships and obligations for their partners.

"We've got a few templates like that up on our collaborative journalism resource page," Amditis said. "I've also worked with local publishers in New Jersey such as Atlantic City Focus to use ChatGPT to help polish and refine grant proposals."

Aside from his deep list of possible use cases in his ebook, Amditis also sees potential in "superprompts" like TranscriptFixer 4.0 to have ChatGPT clean and extract relevant quotes from meeting or event transcripts, generate social posts based on the transcript and then explain the reasons and news judgment behind the decisions to select each quote.

\* \* \*

::: section
## Making AI Work in a Newsroom

Aimee Rinehart is the program manager for the Associated Press (AP) Local News AI initiative, which aims to narrow the growing technology gap between national and local newsrooms.

Rinehart said the AP follows an "80/20" rule when implementing AI technology: 80% of the work can be automated, but 20% of the work must be a human staffer editing and checking quality control at the back end before anything publishes. The approach combines automation with human judgment and reasoning, making the use of AI much safer.

Rinehart told an SPJ Ethics Week 2023 panel that AP uses AI for writing earnings reports but that those reports are always edited by a person before publishing. When AP uses natural language generation for earnings reports, it adds a tagline at the bottom of the article that explains it was generated by DataSkrive and data. The Washington Post also does this with its Heliograph project, and The Los Angeles Times as well with QuakeBot. Rinehart said each newsroom will have to develop its own rules on transparency.

Before incorporating AI into your student or professional newsroom's workflow, consider these questions:

- How can AI help serve everyone in a community?
- Where and how will it make the newsroom more efficient? Is it worth the time?
- How will we train editors and reporters on how to use it properly?
- What is the full breadth of AI potential within your publishing organization? What can it do for the business side as well as the newsroom?

Dalia Hashim at the Partnership on AI is running a AI + Local News workstream, with a list of AI tools for publishers and a guidebook for procurement. It also features a large database of tools and how they can be used by local newsrooms. "Local newsrooms form the foundation of a healthy information ecosystem, providing their communities with the context and meaning needed to make sense of a complex world," the site's introduction says. "AI tools have the potential to improve the business sustainability of these important institutions. These technologies also introduce new risks that AI-adopting newsrooms will need to understand and discuss."

::: section

## Using AI in Small Newsrooms

Newsrooms of any size can benefit from the use of AI tools, but they're particularly important for smaller staffs that need resources.

Art Director Matt Selva is one of six full-time staffers at Mainebiz, a business publication in Portland, Maine. Selva was tasked with designing cover art for reporter Renee Cordes' story on the recent Silicon Valley bank collapse. Cordes suggested they design the cover art as a scene from the infamous bank run in the holiday classic "It's a Wonderful Life." She found an Alamy stock photo of the scene, but they didn't want to use it as is and weren't sure of the legality of modifying it for use on the cover. Selva had been experimenting with AI on his own and thought this might be a good use case for it to generate a concept cover.

He created a number of image options with Midjourney using this prompt and slight variations:

> /imagine Jimmy Stewart standing on the right side foreground looking left wearing a puffer jacket. Crowd in background. colorized vintage film frame. "It's a Wonderful Life"

"I eventually got a composition I thought would work well but the Jimmy Stewart likeness wasn't great," he said, "so I used [Dreamstudio.ai](http://Dreamstudio.ai) to mask off the face and generate some new options. Once I was happy with that I upscaled the image to print resolution with another AI tool at [imglarger.com](https://www.imglarger.com)."


<em>Figure</em> <em>9.2</em> Matt Selva’s Mainebiz cover of AI-generated Jimmy Stewart


Then he brough the upscaled image into Photoshop and used some of the AI neural filters in its (June 2023) beta release to enhance the facial details and change Stewart's eye gaze direction. He also did some old-fashioned Photoshop work and added blurring, vignetting and grain to give it less of a digital sheen and obscure the faces of the crowd.

The magazine's cover art credit made it clear to the readers that the image was generated with the help of AI: "Image Generated with Midjourney and DreamStudio AI."

::: section
## Learning AI

Jarvis believes journalism instructors will soon be teaching the skill of prompt writing: how to get what you want out of a machine. "We started exercising this new muscle with DALL-E and other generative image AI -- and we learned it's not easy to guide the machine to draw exactly what we have in mind," he wrote. "At the same time, lots of folks are already using ChatGPT to write code."

Caplan, Jarvis' CUNY colleague, introduces students to AI through a 3E framework: "Explore, Experiment & Execute." First, they read about new services and capabilities and watch how others are using them. Then they experiment to see how these tools work and to identify their capabilities and limitations. Finally, they execute a project using AI in some way, to get a deeper feel for the tools.

"I try to take a sober approach, noting the potential and also the perils associated with new tools that disrupt traditional journalistic practices," Caplan said.

"I find value in the 'I do, We do, You do' approach. I show something, we explore it together, and then you, the student, give it a shot on your own or in a small team. We look at examples of what others are doing and consider the hurdles and potential pitfalls of relying on AI. Then we reflect on use-cases and think through scenarios to be prepared for how things may go wrong, and where the AI might be of most value."

Caplan said he loves experimenting with new tools because that "helps me learn and because every so often something arises that makes my work more enjoyable and efficient, and that's a gift."

::: section

## AI Newsroom Training

Warren oversaw the implementation of training and digital technology to large and small Gannett newsrooms for more than a decade before joining Medill's local news accelerator. He sees AI's potential to increase productivity as a way to make newsrooms more efficient.

"At an everyday level, the software/tools available lower the barrier to entry into the local news space because they further erode the control incumbents have wielded over the means of production and distribution," he said. "Broadly, that's been the story of the Internet as relates to local news.

"These tools are the same story but playing out in a microcosm, sort of at a Moore's Law pace. The better and easier-to-use digital storytelling tools become, the more opportunity there will be for new players to offer sophisticated local news coverage. Ultimately, everyone having access to the same tools means those that do the best reporting to feed into these tools will win."

Gannett has taken a cautious route in implementing AI tools into its workflow. It requires staff members to get permission from their direct reports before using it, and they must have a concrete reason why they need to use the tool. They also apply an approach similar to the AP, where human interaction is required before publishing.

\* \* \*

::: section
## Putting ChatGPT to the Test ... and Failing

In January 2023, an ABC News reporter worked with ChatGPT on air during a weekend edition of "Good Morning America." His prompt to ChatGPT asked it to write a script about ChatGPT in the style of an ABC News story. As the software produced the script as the cameras rolled, the reporter was shocked to find how accurate the script was, right down to the style, format and details that ABC News uses (watch the story: [https://www.goodmorningamerica.com/news/video/school-districts-banning-artificial-intelligence-tool-96738248](https://www.goodmorningamerica.com)).

But ChatGPT isn't always so effective, or accurate. In early versions of the software, its knowledge only runs up to 2021, so any more-recent requests usually lead to a default error message. But sometimes the software does strange things.

Shortly after the 2023 Chicago mayoral runoff election, I asked ChatGPT to write a news story about the results of the race. On the first try, it gave me the default error message. But a second try produced a result -- with wrong answers. Instead of detailing Brandon Johnson's upset over the favored Paul Vallas, it wrote a piece of fiction about Rebecca Martinez winning the race. Problem is, she didn't run for mayor ([Figure 9.3](#ch09.xhtml__15031-5909_ch009_Figure_003)).

I tried the same experiment in Google Bard, ChatGPT's rival. The result was a clumsily written, but accurate, rundown of the 2023 mayoral runoff. Names were spelled correctly. The vote count was correct. The background and bios appeared accurate on a first editing pass, save for one major error: Brandon Johnson is not the first African American to become Chicago's mayor since Harold Washington in 1983. Johnson's predecessor, Lori Lightfoot, was African American (third paragraph in [Figure 9.4](#ch09.xhtml__15031-5909_ch009_Figure_004)).


<a href="#ch09.xhtml_R_15031-5909_ch009_Figure_003"><em>Figure</em> <em>9.3</em></a> A case study in how NOT to use ChatGPT


<a href="#ch09.xhtml_R_15031-5909_ch009_Figure_004"><em>Figure</em> <em>9.4</em></a> Google Bard’s result on story generation


In March 2023, Google launched a free beta version of Bard, where you can register for it through your Gmail/Drive login. I saw some instant benefits and drawbacks

- **Benefits:** The results weren't perfect but much more accurate than ChatGPT. The interface lets you rank the result with a thumbs up or thumbs down. It has a button that lets you edit the prompt without entirely retyping it and has a "Google It" search button.
- **Drawbacks:** Still has some accuracy problems and it is spotty with attribution and link citations from results.

I had my UIC Advanced Data Journalism students write more prompts about various topics. Some asked ChatGPT or Bard to write about Chicago's top tourist attractions. Others asked it to write a story or bio about themselves -- or me. As a student read an AI-produced story about me in class, I could see that it gleaned information directly from my official UIC faculty bio and from [MikeReilley.com](https://www.MikeReilley.com). Google Bard produced a similar result.


<a href="#ch09.xhtml_R_15031-5909_ch009_Figure_005"><em>Figure</em> <em>9.5</em></a> Accurate HTML link code in ChatGPT


<a href="#ch09.xhtml_R_15031-5909_ch009_Figure_006"><em>Figure</em> <em>9.6</em></a> Accurate HTML table code in ChatGPT


At the end of class, I asked my students what they learned by working with the technology. Their answer: Don't ask ChatGPT and Bard to write stories with you. Have it help with research summary, draft code ([Figures 9.5](#ch09.xhtml__15031-5909_ch009_Figure_005) and [9.6](#ch09.xhtml__15031-5909_ch009_Figure_006)) and other tasks, but the tools aren't reliable enough at this point to write stories.

::: section

## Writing Good Prompts

At the Associated Press, Rinehart wants journalists to focus on eight tips for writing good prompts. We'll apply these tips in the prompt-writing exercises at the end of [Chapter 10](#ch10.xhtml__15031-5909_ch010).

1.  Break complex tasks into smaller steps.
2.  Use chain-of-thought and step-by-step prompting.
3.  Provide training examples to help with new or complex tasks.
4.  Add relevant contextual information whenever possible.
5.  Repeat the main instructions at the end.
6.  Include words or phrases to guide the responses.
7.  Use clear punctuation, headings and section markers.
8.  Specify the output structure you want.

Rinehart also warns to watch for gender bias in AI. For example, if you ask ChatGPT to write a love story, you'll get a typical heterosexual love story (e.g., ask it to write a Shakespeare-inspired love story). It's programmed to write in this format and doesn't take LGBTQ into consideration. Another instance: a result that assumes that the boss is a man and the assistant is a woman, Rinehart said.

In his book, "How to Start Writing Online," author Nicolas Cole discourages the use of single-sentence prompts, saying it's "like having a Ferrari and driving it 5 mph." Instead, he encourages people to treat the software like you would a newly hired intern. His five guidelines give a more structured path for the OpenAI tool to follow, same as you would an intern who's new to your industry:

1.  **Create constraints. Don't encourage assumptions.** If you give AI vague information, it will give you a vague conclusion. If you ask it a broad question, it will give you a broad answer. People who say ChatGPT "creates mediocre content" are giving it mediocre prompts.

2.  **Treat AI like a "digital intern" and invest in its training.** If you hired an intern tomorrow, you wouldn't give him/her one sentence of direction. You would:

    - Create a checklist
    - Explain why
    - Ask if he/she has any questions

    Do the same with ChatGPT.

3.  **You do the "thinking."** Tell AI how to "do the doing." You can't expect AI to think for you. Instead, whatever you want AI to help you create, you need to first understand:
    - Why you want what you want
    - What, specifically, you need
    - How you want it delivered

4.  **Talk to AI like a human, and give it only one task at a time. The best prompts don't ask AI to chase seven different ideas at once.**

    - You can ask AI if it's confused.
    - You can tell AI to "do that again."

    Remember: imagine you're hand-holding a college intern.

5.  If AI gives you the wrong output, that means you gave it the wrong input.
    - Sometimes, you need to workshop your prompts more than 10 times to figure out how to get what you need.
    - Even though you're writing English, think of it like you're writing code.

\* \* \*

::::: section
## The Best AI Writing and Editing Tools

During the AI gold rush, established tools such as Canva, Notion and Coda were hustling to implement new AI features to their interfaces. While some of it is hype, some of the tools have added some helpful AI features, Caplan said.

Caplan found that [Craft.do](http://Craft.do) has the best-designed implementation of any of the AI writing tools he has seen.

> You hit/and it gives you some options for adding directly into whatever doc you're working on. It works on the Mac and Windows apps, on the Web and on iOS.
>
> You can use the AI feature to summarize or explain something; create an outline; write a pros and cons list; generate keywords or hashtags; suggest a title; add to something you've written; or translate your text into English, Spanish, French, Italian, German, Dutch, Portuguese, Korean or Japanese.

I have used the Magic Write tool in Canva Docs for some of my stories. It's helpful when you're stuck and can't think of a transition or you need a quick writing tip. You simply hit the plus sign (+) in the left margin and the pulldown menu gives you options to style the text. At the top is the Magic Write tool. Select that option, then write a prompt of at least five words and Canva will produce some strikingly strong results. A test I tried with it is shown in [Figures 9.7](#ch09.xhtml__15031-5909_ch009_Figure_007) and [9.8](#ch09.xhtml__15031-5909_ch009_Figure_008).

\* \* \*

<aside aria-label="box3" class="box1" epub:type="tip" role="doc-tip" title="box">

::: section

## Video: Using Canva Docs with AI Features 

<https://bit.ly/canvadocsvideo>

This training video demonstrates some of the AI writing features in Canva Docs as well as the voice typing transcription feature in Google Docs.

</aside>

\* \* \*


<a href="#ch09.xhtml_R_15031-5909_ch009_Figure_007"><em>Figure</em> <em>9.7</em></a> Canva Docs Magic Write tool


<a href="#ch09.xhtml_R_15031-5909_ch009_Figure_008"><em>Figure</em> <em>9.8</em></a> Canva Docs Magic Write results


Caplan also predicts that the way we store, organize and use our notes is poised to change dramatically in the years ahead. Instead of hierarchical, folder-based notes services like Evernote, we'll see new personal knowledge management tools -- PKM -- expand, grow and gain popularity because they allow us to connect ideas, search and update our own past notes with natural queries and reliably find anything we need.

Caplan said that some of the new PKM services to watch include Tana, Capacities, Anytype, Obsidian, Roam, Logseq, Reflect, Mem and Bloks. At first they're of interest to early adopters and techies, but like Notion, the best of the bunch will find broad adoption.

You can find more AI writing and editing tools in [Chapter 1](#ch01.xhtml__15031-5909_ch001) and on [JournalistsToolbox.ai](http://JournalistsToolbox.ai). Among the best tools:

- Lex.page
- AI text-generation tool.
- Copy.ai
- AI text-generation tool.
- Notion AI
- Similar to Canva Docs, the revamped Notion AI (February 2023) installed an AI assistant that can offer writing/editing suggestions, generate idea lists and more.
- Postwise.ai
- AI-driven Twitter writing tool
- Jasper.ai
- A basic AI copywriting tool that works for multiple platforms. Good for journalists, PR pros and more.
- Jenni.ai
- A good writing assistant if you're stuck with writer's block.
- [Typli.Ai](http://Typli.Ai) -- AI Writer and SEO Writing Assistant
- Intuitive AI content tool that combines AI writing and an SEO assistant. Cost is \$29 a month.
- AISEO
- AI writing assistant, copywriting and paraphrasing tool.
- Repurpose.io
- Tool for automating workflows. Good for autoposting social media.
- Vista Social: AI Assistant for Writing Social Media Posts
- Uses ChatGPT technology to help you write better social posts. Has a free account option.
- Canva Docs
- Canva launched this tool in the second half of 2022 as a competitor for Google Docs. It includes a few AI tools, including the "Magic" tool that lets you type in a topic, and it gives you some text related to that topic. It's good for breaking writer's block. Canva has a free account with some paid accounts starting as low as \$128 annually (Fall 2022 prices).
- Fireflies
- Transcribes notes from meetings, creates highlights, etc.
- Google Pinpoint
- This tool uses AI to analyze PDFs, strip text from images and transcribe audio.
- Tldv.io
- Takes meeting notes for you, transcribes them.
- Google Sheets: Help Me Organize
- Introduced by Google in summer 2023, this tool lets you load a prompt directly into sheets for creating a template. For example, try this prompt: client and pet roster for a dog-walking business. Then select the table or whatever format you want. It will give you a table with dummy data to organize the data into the table cells. This can be useful for organizing crime data, analyzing city budgets or just organizing your source lists and tasks.

::: section
### ***Editing Tools***

- DeepL Write
- Cut/paste a selection of text and this tool will tell you how to improve it. Has free and paid models.
- QuillBot Paraphraser
- Reworks copy into a more professional style. Good for writing formal emails. Has free and paid models.
- Headline Hero
- Paste in a story and it gives you headline options based on settings you enter.
- Hemingway Editor
- Paste in a story and it analyzes and grades the piece based on active voice, brevity, etc.
- WordTune Spices
- Advanced word processing tool. Has free and paid models.

\* \* \*

::: section
## Other Useful AI Tools

While AI tools are a huge help to reporters and writers, there are many other automation tools that newsrooms can use. AI tools have emerged for podcasting, video editing, creating images (MidJourney, DALL-E and others we'll explore later in the chapter). These tools can save thousands of hours of editing time

Hamer of [Descript.com](http://Descript.com) outlined some of the best AI-driven multimedia tools in a 2023 blog post ([https://www.descript.com/blog/article/the-ultimate-list-of-ai-tools-for-creators](https://www.descript.com)). Nearly all of the tools have free and paid models. Here are some of my favorites from her list, along with her descriptions of the tools:

::: section

## Podcasting Tools

- Descript: An AI-powered editor that automatically transcribes your audio and video recordings so that you can edit them just like text. It also uses AI to remove background noise and improve recording quality with a click (via Studio Sound), detects filler words like "um" and "uh," and can insert AI voices -- even correct misspoken words with a synthesized version of your own voice, if you want -- via its Overdub feature.
- Podcastle: A cloud recorder and AI-powered editor that lets you record a remote interview, edit, and mix all in one app. It also has transcription capabilities, an AI-powered sound quality tool called Magic Dust, and AI voices.
- Resound: Resound is an AI-powered audio editor built to automatically detect filler words like "um" and "uh" and remove them from your recording. Another good option is Speechify, a text-to-audio tool.
- Adobe Podcast: This is Adobe's answer to Descript -- an AI-powered text-based audio editor that can automatically enhance speech. It also enables remote recording.
- Auphonic: Upload your file, and Auphonic will automatically optimize your recording and polish up the quality of the audio. You can choose from a variety of audio algorithms, including a leveler, normalization, filtering, and noise reduction, and it can even stitch an intro and outro onto your episode if you want.
- Cleanvoice.ai: Like Auphonic, Cleanvoice is a standalone AI audio tool that can remove unwanted sounds, but it focuses more on speech imperfections like filler words, stutters and those spitty, clicky mouth sounds.
- Listnr: If you want AI voices, Listnr's got them. Paste text into their text-to-speech converter, and the app will convert it into one of their 600 voices in seconds. At that point, it's ready to turn into a podcast, use as a video voiceover, star in a "Home Alone" contraption to scare away burglars, whatever you need it for.
- Alitu: Alitu brands itself as an AI-powered one-stop shop for podcast production. You can record remotely with hosts or guests, polish up the audio, edit the content, generate transcripts and publish all from a single platform.
- Dubb: If you're more interested in the recording part of podcasting than the marketing part, Dubb is for you. It uses AI to generate not only transcripts, but episode titles, show notes, newsletter content, Twitter threads, even generative AI TikTok videos.

::: section
## Video Editing and Creation

- Runway: Half AI image generator, half AI-powered video editor, Runway can either create a video from scratch using only text or edit your video with futuristic tools like background or object removal, motion tracking, and automatic "beat" detection, along with staples like automatic noise removal and subtitles.
- Aug X Labs: Its automatic B-roll is powered by AI. Just upload an audio or video recording, and Aug X Labs' prompt-to-video tool will add relevant images based on what's being said.
- Pictory: Pictory is an AI-powered video generator and editor that can create videos from scripts and blog posts with AI text-to-speech voices and automatic B-roll footage. You can also use it to edit existing videos with a Descript-style text-based editor, and even create short snippets for social media with just a few clicks.
- Synthesia: You've heard of text-to-speech, but what about text-to-virtual-avatar? With just plain text (in up to 65 languages), Synthesia generates a realistic-looking virtual avatar to deliver your lines talking-head style. Instead of watching stock footage paired with an AI voice, you can watch a realistic "person" walk you through an instructional video or product demo, which, while definitely in uncanny valley territory, is a lot more engaging. (Descript uses Synthesia for internal presentations all the time, in fact.) The personal plan is \$30 for 10 video credits/month.
- D-ID: D-ID can generate talking humans, but it can *also* generate talking monsters. That's because it can combine facial images -- either real ones or AI-generated ones -- with audio or text to make them speak.
- Elai: Elai mixes automatic video generation with AI avatars for a really easy way to make videos in minutes. You can generate footage from a blog post URL, product images and descriptions, or even a slide deck, then choose your human avatar and put the AI to work.
- InVideo: InVideo lets you create entire videos in minutes from a script, article, or blog post -- or existing footage -- with an eye-popping 6,000 templates organized by platform, industry, and content type. It can also remove backgrounds, add AI voiceovers, and automatically resize your video for any platform.
- VEED: VEED is a web-based video editor that can do screen recording, automatic subtitles, AI voiceovers and a bunch of other things to make your videos look polished and professional.

::: section

## Automation and Productivity

In March 2023, the International Journalists' Network compiled a list of useful AI tools for productivity: "AI-powered tools can help journalists streamline information-gathering and uncover hidden stories within datasets. new/s/leak, short for 'NetWork of Searchable Leaks,' for example, is a free tool that uses both language technology and visualizations to help journalists sift through large amounts of text data and identify relevant material and unexpected connections more effectively."

Other tools IJNET shared:

- **Tagging:** While automatic tagging might sound like a boring use of AI, it's an important step in assuring valuable information won't be lost within the databases. Varia provides a categorization system with intelligent search and retrieval capabilities.
- **Text-to-speech and speech-to-text:** Text-to-speech AI, such as Eleven Labs, can convert written text into natural speech, making information more accessible for those with visual impairments. Speech-to-text software like Trint can transcribe audio and video in multiple languages, facilitating access to a broader audience, including those with hearing loss. YouTube also offers free captioning capabilities.
- **Monitoring events and topics in real time:** This activity is crucial for keeping up with the fast pace of news. AI has made this easier with tools like NewsWhip, which predicts the stories and topics that will trend in the hours ahead, tracking public and media interest.
- **Social media:** Another tech platform, Factmata, analyzes social media, articles and blog posts to group similar opinions into narratives and offer insights on popularity and virality. Using these, journalists can stay on top of the latest developments and gain a deeper understanding of online conversations.
- **Text-to-audio:** Audemic, a marketing tool, can also help journalists and content creators save valuable time in their newsgathering and reporting process. Users can upload a scientific paper, and the software will generate an audio version of the text. Additionally, they can quickly access an overview, skip to specific sections, listen to the audio, highlight important information and take notes easily.

\* \* \*

::: section
## MidJourney, DALL-E and Image-Generation Tools

Beyond ChatGPT, the other AI technology to make the greatest impact on journalism were the image-generation tools such as DALL-E (made by OpenAI), MidJourney (which works through [Discord.com](https://www.Discord.com)) and Stable Diffusion, among others. Ashley Hamer's blog post ([https://www.descript.com/blog/article/the-ultimate-list-of-ai-tools-for-creators](https://www.descript.com)) highlighted some of the best options:

- Midjourney: Midjourney is one of the many image generators that have taken the art world by storm. In the free version, you use it by sending chat prompts to the AI in Discord, which is good and bad -- you get to see everyone else's art, but they also get to see yours. If you use a paid version, your prompts and images can be seen only by you.
- DALL-E 2: Made by OpenAI, the same company that built ChatGPT, DALL-E 2 is also capable of stunning AI-generated images. It's particularly good at copying different art styles and can produce photorealistic images more successfully than other generators.
- Stable Diffusion/Stability AI: Allows you to ask for a particular image with both a positive prompt and a negative prompt. You can also adjust a "guidance" slider that determines how closely the image generator sticks to your prompt.
- Lexica: A search engine for every image ever made using Stable Diffusion, which can help you find/improve on prompts.
- Stockimg.ai: This tool is designed for practical purposes like book covers, logos, posters, digital wallpaper, and the like.
- Adobe Firefly: Adobe has partnered with Google to integrate Firefly into Google Bard, the company's rival AI software to ChatGPT. This was introduced at the Google I/O conference in May 2023. Users can prompt an illustration in Bard, which will then connect seamlessly to Firefly to create the image. Firefly has some cool features aimed at solving problems for creatives and visual journalists: AI video editing, 3D modeling, text-to-image, photo editing and more. Be careful with ethics when using this tool on news photographs.

I've tinkered with many of these tools but have used MidJourney and Firefly the most for various personal and professional projects. I find MidJourney's simple interface and ability to work well with [Discord.com](https://www.Discord.com) streamlines my workflow.

MidJourney launched in open beta in July 2022 by a San Francisco company with only 10 employees. The team built an AI-powered text-to-illustration tool that lets you build original, high-resolution images in a few seconds. The tool is free but has paid upgrades (I pay \$10 a month), and you use the tool through a bot in Discord. You'll need accounts on both and must connect MidJourney to Discord, which is easily prompted at setup. I recommend setting up Discord first, then logging into it through a prompt that MidJourney provides during its set-up process.

::: section

## Using Text-to-Image Journalistically, Ethically and Legally

A competitor to Open AI's DALL-E and Stable Diffusion, MidJourney lets you create illustrations, memes, logos and other pieces of art quickly. I would recommend labeling them as such if you publish them and even explain to the reader how you made it. In fact, I used MidJourney to design the header logos on many of the [JournalistsToolbox.ai](http://JournalistsToolbox.ai) pages.

Amditis' ebook, "Beginner's Prompt Handbook: ChatGPT for Local News Publishers," offers specific examples on how to write good prompts and unexpected use cases for newsrooms with text-to-image tools. As with most tools, MidJourney can be used for fake news. This was the case with the hundreds of memes of Donald Trump "fleeing police" that made the rounds on social media prior to his late March 2023 indictment.

Be careful with text-to-image. It can be dangerous in the hands of those with bad intentions or those unprepared. Consult the SPJ and NPPA codes of ethics for advice on handling photo illustrations. Also, Santa Clara University's Markkula Center for Applied Ethics has an excellent guide, "Ethical Questions About Generative AI." The U.S. Copyright Office ruled in late February that images created with the tool don't fall under copyright jurisdiction. This could change over time, however.

Journalists are also closely watching a lawsuit that stock photo provider Getty Images filed in February 2023 against Stability AI. The suit said Stability AI misused more than 12 million Getty photos to train its Stable Diffusion AI image-generation system. Getty said Stability scraped the images without a license.

At the International Center for Journalists Media Party Conference in June 2023, Dalia Hashim of Partnership on AI presented questions newsrooms should ask before using generative artificial intelligence and text-to-image prompts. Journalists also need to communicate to the audience how and why they are using AI on the project. Questions Hashim raised in her talk included the following:

- Are we comfortable with using generative AI tools that were trained using others' content without consent? Can we find or make tools that are not derivative?
- How are we going to put guardrails around the use of AI tools in the newsroom?
- Where could our workflow be automated? Where do we need a human in the loop?
- If we are using AI to produce content, how will we label it?
- How will we ensure the accuracy of AI-aided content?
- If we're collecting data from the audiences, how is it going to be used, and who owns it?

Hashim also encouraged journalists to use the Partnership on AI's framework on responsible practices for newsrooms' AI use, alongside its AI tools database for local newsrooms.

::: section
## Testing It Out

I've built a working document on AI tools on a Google Doc (<https://bit.ly/aiguides>) that includes background on MidJourney and some prompts, lenses, filters and ideas to get you started.

I began with some basic prompts by telling MidJourney to imagine A BMW sports car on a beach at sunset, ultra realistic -- v 5 -- ar 3:2.

The last two prompts told it to use the most current "version 5" of MidJourney and that the aspect ratio should be 3:2 (horizontal, 2:3 for vertical iPhones). Other prompts let you add filters, lenses (which MidJourney is still figuring out) and more. The result included the image presented in [Figure 9.9](#ch09.xhtml__15031-5909_ch009_Figure_009).

It took about one minute to produce these images. By pressing a button underneath these samples, I could "upscale" each image for a higher resolution that I could then download and use. I suggest using the MidJourney Prompt Book, which features a variety of tips and a database of prompts that you can use for greater detail.

Writing good prompts -- both for the chat applications and the image-generation tools -- is a useful skill for all journalists, but particularly for young journalists coming out of college. The skill requires good descriptive writing, the ability to research and edit on the fly. Working with my students, I've found that MidJourney helps them understand how to write descriptively ... and then see instant results.


<a href="#ch09.xhtml_R_15031-5909_ch009_Figure_009"><em>Figure</em> <em>9.9</em></a> MidJourney results for a BMW on a beach <em>Source:</em> Prompt by Mike Reilley


As newsroom budgets wane, money for food and dining photography for the features section has dried up with it. That's where AI-generated images can help, as long as the journalist identifies it as an AI-generated photo in the cutline. The SPJ Code of Ethics can be helpful here: Never deliberately distort facts or context, including visual information. Clearly label illustrations and re-enactments.

Let's say you're writing about healthy breakfasts and need an image of a grain bowl and fresh fruit. Try this prompt in [Discord.com](https://www.Discord.com):

> /imagine A breakfast bowl with whole great and fresh blueberries, ultra realistic --ar 2:3 --v 5

Be sure to include your credit and "created using AI in MidJourney" in the cutline. [Figure 9.10](#ch09.xhtml__15031-5909_ch009_Figure_010) displays the result.

\* \* \*


<a href="#ch09.xhtml_R_15031-5909_ch009_Figure_010"><em>Figure</em> <em>9.10</em></a> Breakfast bowl with blueberries, created by Mike Reilley using AI in MidJourney


::: section

## Footnotes

- Adobe Firefly: <https://firefly.adobe.com>
- Adobe Podcast: <https://podcast.adobe.com>
- AI for Data Storytelling, Simon Rogers: [https://simonrogers.net/2023/03/28/ai-for-data-storytelling](https://simonrogers.net)
- AI + Local News Workstream: [https://partnershiponai.org/workstream/local-news](https://partnershiponai.org)
- AI Tools for Local Newsrooms: <https://bit.ly/aitoolslocal>
- AI Tools for Local Newsrooms Database: [https://airtable.com/shrQeIsvzGoTbdp7b/tblvwDhL4X23V1pTp/viwN8zctay9H2N0ir?blocks=hide](https://airtable.com)
- AISEO: <https://aiseo.ai>
- Alitu: <https://alitu.com>
- Audemic: <https://audemic.io>
- Aug X Labs: [www.augxlabs.com](http://www.augxlabs.com)
- Auphonic: <https://auphonic.com>
- Beginner's Prompt Handbook: ChatGPT for Local News Publishers: [https://jamditis.notion.site/jamditis/Beginner-s-prompt-handbook-ChatGPT-for-local-news-publishers-15d1f07d5b194265a41fdd42955679b4](https://jamditis.notion.site)
- Bloks: [www.bloks.app](http://www.bloks.app)
- Canva Docs: [www.canva.com/docs](http://www.canva.com)
- Capacities: <https://capacities.io>
- ChatGPT: [https://chat.openai.com/chat](https://chat.openai.com)
- ChatGPT Exercises and Prompts, Mike Reilley: <https://bit.ly/aiguides>
- Cleanvoice: <https://cleanvoice.ai>
- Collaborative Journalism Resource Page: [https://collaborativejournalism.org/guides](https://collaborativejournalism.org)
- Collaborative Partnership Agreement: [https://docs.google.com/document/d/1_0eRCBNduqFA8N20MPf-gNafEyDjQerlCnYxsSHzqJs/copy](https://docs.google.com)
- Copy: [www.copy.ai](http://www.copy.ai)
- DALL-E 2: [https://openai.com/product/dall-e-2](https://openai.com)
- DeepLWrite: [www.deepl.com/write](http://www.deepl.com)
- Descript: [www.descript.com](http://www.descript.com)
- Descript: The Ultimate List of AI Tools for Creators, Ashley Hamer: [www.descript.com/blog/article/the-ultimate-list-of-ai-tools-for-creators](http://www.descript.com)
- D-ID: [www.d-id.com](http://www.d-id.com)
- Discord: <https://discord.com>
- Eleven Labs: <https://beta.elevenlabs.io>
- Ethical Questions About Generative AI, Markkula Center for Applied Ethics: [www.scu.edu/ethics-spotlight/generative-ai-ethics/ethical-questions-about-generative-ai](http://www.scu.edu)
- Factmata: <https://factmata.com>
- Fireflies: <https://fireflies.ai>
- Geeks Bearing Gifts, Jeff Jarvis: [https://press.journalism.cuny.edu/book/geeks-bearing-gifts](https://press.journalism.cuny.edu)
- Good Morning America: School Districts Banning AI Tool: [www.goodmorningamerica.com/news/video/school-districts-banning-artificial-intelligence-tool-96738248](http://www.goodmorningamerica.com)
- Google Bard: <https://bard.google.com>
- How to Start Writing Online: <https://startwritingonline.com>
- International Journalists' Network: Non-Writing AI Tools Every Journalist Should Know About: [https://ijnet.org/en/story/non-writing-ai-tools-every-journalist-should-know-about](https://ijnet.org)
- InVideo: <https://invideo.io>
- Jasper.ai: [www.jasper.ai](http://www.jasper.ai)
- Jenni.ai: <https://jenni.ai>
- Journalist's Toolbox Training Video: Canva Docs: <https://bit.ly/canvadocsvideo>
- Journalist's Toolbox Training Video: ChatGPT Basics: <https://bit.ly/gptvideo>
- Journalist's Toolbox: AI Tools for Journalists: [www.journaliststoolbox.org/2023/05/09/ai-tools-for-journalists](http://www.journaliststoolbox.org)
- Lex.page: <https://lex.page>
- Lexica: <https://lexica.art>
- Listnr: [www.listnr.tech/ai-podcast](http://www.listnr.tech)
- Logseq: <https://logseq.com>
- Mem: <https://mem.ai>
- MidJourney: [www.midjourney.com/home](http://www.midjourney.com)
- MidJourney Prompt Book: [https://enchanting-trader-463.notion.site/Midjourney-AI-Guide-41eca43809dd4d8fa676e648436fc29c](https://enchanting-trader-463.notion.site)
- New/s/Leak: [www.newsleak.io/about](http://www.newsleak.io)
- NewsWhip: [www.newswhip.com](http://www.newswhip.com)
- Notion: [www.notion.so](http://www.notion.so)
- Obsidian: <https://obsidian.md>
- Partnership on AI: Responsible Framework for Synthetic Media: [https://syntheticmedia.partnershiponai.org/#read_the_framework](https://syntheticmedia.partnershiponai.org)
- Pictory: <https://pictory.ai>
- Podcastle: <https://podcastle.ai>
- Postwise: <https://postwise.ai>
- QuillBot: <https://quillbot.com>
- Reflect: <https://reflect.app>
- Repurpose: <https://repurpose.io>
- Resound: [www.resound.fm](http://www.resound.fm)
- Reuters: Getty Images Lawsuit Says Stability AI Misused Photos to Train AI: [www.reuters.com/legal/getty-images-lawsuit-says-stability-ai-misused-photos-train-ai-2023-02-06](http://www.reuters.com)
- Roam Research: <https://roamresearch.com>
- Runway: <https://runwayml.com>
- Speechify: <https://speechify.com>
- SPJ Code of Ethics: [www.spj.org/ethicscode.asp](http://www.spj.org)
- Stable Diffusion: [https://huggingface.co/spaces/stabilityai/stable-diffusion](https://huggingface.co)
- StockIMG.ai: <https://stockimg.ai>
- Synthesia: [www.synthesia.io](http://www.synthesia.io)
- Tana: <https://tana.inc>
- Tl;vd: <https://tldv.io>
- TranscriptFixer 4.0: [https://jamditis.notion.site/Superprompt-TranscriptFixer-4-0-73891d44a2314c0499749ce07954e070](https://jamditis.notion.site)
- Trint: <https://trint.com>
- Typli.io: <https://typli.ai>
- Varia: [www.varia.media](http://www.varia.media)
- VEED: [www.veed.io](http://www.veed.io)
- Vista Social: <https://vistasocial.com>
- Wonder Tools: AI Writing Tools, Jeremy Caplan: [https://wondertools.substack.com/p/aiwriting](https://wondertools.substack.com)
- Wonder Tools Newsletter: [https://wondertools.substack.com/p/newai](https://wondertools.substack.com)
- Wordtune Spices: [www.wordtune.com/spices](http://www.wordtune.com)


# 10 AI \| Productivity Tools and Exercises

DOI: [10.4324/9781003431787-11](https://doi.org/10.4324/9781003431787-11){aria-label="D.O.I. link to this document."}

\* \* \*


**Key Resources**

- JournalistsToolbox.ai: <http://journaliststoolbox.ai>
- Google News Product Database: <https://learning.newsproduct.org>
- Beginner's Prompt Handbook: ChatGPT for Local News Publishers: <https://bit.ly/ailocalbook>

\* \* \*

You won't find a bigger advocate for AI tools in local newsrooms than Joe Amditis of the Center for Cooperative Media in New Jersey. One of the reasons he wrote the Beginner's Prompt Handbook (<https://bit.ly/ailocalbook>) was to help news leaders better understand how to use the tool and overcome any fears they or staff may have in using it.

His basic rule: Fact-check everything.

"Just like with any copy you receive from a freelancer or reporter, you have to meticulously verify and back up the statements and claims before you publish them if you want to retain any semblance of trust with your community or audience," he said. "The same thing goes for copy that's generated, enhanced or supplemented by generative AI tools and other comparable software.

"Journalists need to stop thinking and talking about these tools as factual information generators and start treating them like the text formatters and template generators they really are. All these tools are doing at their core is trying to predict what the next most likely word or phrase will be, based on the database of information they were trained on and the additional context and instructions provided by the user."

In the book, Amditis writes about disclosure and transparency, providing a few examples of how newsrooms and publications are approaching that issue. Ultimately, Amditis said, it's up to the individual journalists, editors and newsrooms to decide the best approaches and policies for their journalism.

Some newsrooms include their AI use in their principles and policies pages on their websites and mention it in image cutlines or at the end of a story. DragonFly Editorial posted a personal policy page on ethical AI use on its site. Lynn Walsh of Trusting News placed a disclosure at the end of her 2023 post on newsroom diversity mentioning how she used AI for writing the piece.

Amditis cautions that journalists need to be more careful and intentional about how they talk about AI technology. In particular, about all the fearmongering and misinformation from guests and hosts on various public and mainstream media outlets.

"They seem to be eager to discuss ChatGPT and other tools on the air, but clearly haven't spent enough time playing around with them or studying them to the point where they are able to speak about their capabilities and limitations in a responsible and accurate way," he said.

He also worries about what happens when the right-wingers and neo-Nazi groups start using AI tools to harass and target underserved and vulnerable populations.

\* \* \*

<aside aria-label="box1" class="box1" epub:type="tip" role="doc-tip" title="box">


::: section
## Course Handout 

Download this handout for the latest AI tools, tips and resources: <https://bit.ly/aibookresources>

</aside>

\* \* \*

Another fear with AI tools is that they will replace journalists, tightening the media job market even more than it is now. According to a June 2023 Reuters article, analysts at Goldman Sachs estimated that 18% of global jobs could be automated, and that AI could render 7% of the U.S. workforce redundant, especially in white-collar industries. Others say that journalists aren't at risk of losing their jobs to AI, but they might lose it to someone who knows how to *use* AI.

Amditis takes a realistic, but optimistic view on the role AI will play in the industry.

"You can bet that the companies and CEOs who have owned -- and gutted -- newsrooms over the decades will certainly try to 'replace' them if they believe it will improve their bottom line," he said. "We can't really do anything about that as individuals, but we can, and should, continue to build power among newsroom workers through things like collective action and unionization.

"This happens pretty much every time a new technology comes along that makes it easier or more efficient to do a task or job. Instead of using the tools to invest in employees and, by extension, better journalism, many owners simply see them as a shortcut to higher profit margins.

"That's not an indictment of the tools -- and it's not like we can simply un-invent them even if it was -- it's an indictment of the relationship between journalism, a supposed public good, and capitalism, and journalism's position within a market that is not built to preserve public goods if they don't turn a profit."

Amditis sees journalism jobs and the roles and responsibilities of individual journalists as changing and evolving alongside the new technologies and tools. But he doesn't think these changes will be much different than those that came on the heels of information tools like Encarta, Google, Photoshop or word processors.

"I can speak into my computer microphone and have the words appear on my screen alongside grammatical and spelling recommendations from tools like Grammarly and Google Docs," Amditis said. "Now we have tools that can help us clean up, finish, rearrange, and suggest alternatives for our copy, among other things.

"If the very existence of your job is threatened by those things, then that might be an issue with the nature of that job or the way your employer understands the value of that job. It's not necessarily an issue with the tools that happen to make it easier and more accessible for more people to do those jobs."

:::: section

## Chrome Extensions for AI Tools

We've explored many productivity tools for journalists in this book. But the AI tools -- specifically the Google Chrome browser extensions -- have been some of the most effective.

Chief among them is ChatGPT for Google, which allows ChatGPT to work alongside Google when you search. Once installed, the extension launches a small window to the right of any Google search and drops the ChatGPT results next to the Google results. This is a major time-saver, as journalists don't need to hop between browser tabs when researching.


<a href="#ch10.xhtml_R_15031-5909_ch010_Figure_001"><em>Figure</em> <em>10.1</em></a> ChatGPT for Google browser extension


 [Figure 10.1](#ch10.xhtml__15031-5909_ch010_Figure_001) shows an example of a Google search with the ChatGPT extension results running to the right side.

In this example, I searched for LGBTQ expert sources, which provided a list of websites to the left. To the right, ChatGPT for Google offered its choices for expert sources. While there was an obvious overlap with GLAAD, both offered some different resources to find key sources. If my search had been more specific (e.g. name five LGBTQ expert sources), I would have received lists of specific people.

As always, any source found on Google, ChatGPT or any other search tool or website should be vetted before reaching out for an interview.

Here are some more useful Chrome browser extensions, and you can find more on [JournalistsToolbox.ai](http://JournalistsToolbox.ai). You can find all of the extensions by searching their names in the Google Chrome store: [https://chrome.google.com/webstore/category/extensions](https://chrome.google.com)

- Bing Chat for All Browsers
- You need a Microsoft account that has access to the new Bing Chat to use the extension. If you don't have access to Bing Chat, you can join the waitlist at [bing.com/chat](https://www.bing.com).
- TweetGPT
- A chrome extension that uses ChatGPT to write tweets
- Blackbox
- AI coding assistant
- AskCodi
- AI code optimization tool
- Auto RegEx
- AI RegEx creator
- AI Code Snippets
- Fireflies
- Allows you to record and transcribe meetings, summarize emails and documents, as well as YouTube articles, etc.
- SciSpace Copilot
- Find and interpret complex research papers by highlighting text, number or chart
- YouTube Summary
- This Glasp plug-in gives you a summary and highlights key points of a long video you don't have time to watch
- ChatGPT Prompt Genius
- Learn how to write powerful prompts to level up your ChatGPT
- Teamsmart AI
- Helps you brainstorm, to write drafts and review code
- Merlin
- Lets ChatGPT and GPT-4 work on any website.

\* \* \*

<aside aria-label="box2" class="box1" epub:type="tip" role="doc-tip" title="box">

::: section
## Pro Tip: Five Productivity Tools from Jeremy Caplan of CUNY 

Not all productivity tools use AI. The Journalist's Toolbox features a deep list of both AI and non-AI productivity tools ([https://www.journaliststoolbox.org/2023/05/25/ai-tools-for-journalists](https://www.journaliststoolbox.org)). Here's a list of five favorites from Jeremy Caplan:

- **Superhuman:** I use it to act on hundreds of email messages daily. The keyboard shortcuts, text snippets and other speed-enhancing features mean I can be more responsive to colleagues, students and readers than I would be if I had to use a slower, more clunky email client.
- **Readwise Reader:** I rely on it as my reading hub. It helps me stay on top of articles I save for later, newsletters I subscribe to and YouTube channels I keep up with. It also saves and organizes all my highlights and links them to my notes, so I can refer back to -- and share -- notable passages in books, articles or anything else I've read over the years. \[See Caplan's blog post about how to use it: [https://wondertools.substack.com/p/reader](https://wondertools.substack.com).\]
- **Craft:** I use this mostly for creating documents I share with readers and students. Visual cards help divide up sections of a document so that readers can open up a drawer to see what's inside, rather than having to scroll through long pages of text as they might in a Google Doc. It has AI built in, and works seamlessly on mobile devices, desktop and the Web. \[See Caplan's blog post about how to use it: [https://wondertools.substack.com/p/craft](https://wondertools.substack.com).\]
- **Slido:** This is my go-to resource for live polling and Q&A when teaching live classes and workshops. I love being able to type poll.new and create an instant word cloud poll on the spot to gauge the energy in the room or to check on how people are doing, what they understand, and what their preferences are.
- **Apple Reminders:** This is my simple way of keeping track of my tasks and obligations. I also use it to keep lists of sites to explore, books to read and writing ideas. I've used dozens of fancier task apps -- this is a category where simple is best. And I rely on the voice capabilities to dictate reminders without having to look at a screen.

</aside>

\* \* \*

::: section

## ChatGPT Plug-ins

In the spring of 2023, ChatGPT began offering plug-ins that opened the tool up to new tasks. These plug-ins worked directly in ChatGPT as opposed to the Chrome plug-ins that work with a separate browser.

ScholarAI is a useful ChatGPT plug-in for journalists. Once installed, you can ask it to search thousands of scholarly publications on a specific topic and summarize it. Then you can ask it to write Twitter threads and other functions using that summary. It provides citations and links to the research as well, so you can fact-check it as you go.

Some other plug-ins worth installing are:

- **Wolfram:** Computation, math, curated knowledge and real-time data through Wolfram Alpha.
- **ChatwithPDF/Ask Your PDF:** Search and make queries of PDFs you link off to. You can turn them into a database of sorts that you can analyze with sub-prompts.
- **PromptPerfect:** Type the word perfect to improve the prompt you just wrote.
- **Photorealistic:** Helps you create realistic prompts for MidJourney image creation.
- **Daigr.am:** A simple chart-building tool that requires no coding. Once installed, you can prompt the tool to design a specific chart with a dataset (cut-and-paste the prompt and the data together) and then modify the chart or even change the format entirely using sub prompts.

\* \* \*

::: section
## Advanced Data Analysis and ChatGPT

In the summer of 2023, OpenAI released the long-awaited Advanced Data Analysis application for paid ChatGPT-Plus users. The tool works much like a plug-in but exists outside the GPT plug-in store. To turn it on, go into the settings and hit the toggle button to green.

Advanced Data Analysis essentially allows the most advanced AI available, GPT-4, to upload and download information, and to write and execute programs. It helps you edit videos, create charts, analyze data, calculate complex math problems, convert files and more in just seconds. You can upload files as large as 100 MB.

I've found it most useful as a data analysis and graphic-building tool. Although it reduces the amount of "AI hallucinations" that ChatGPT is known for, it's not perfect. Be careful with anything you build or use in the tool and fact-check everything.

\* \* \*


::::::::: section

## Exercises

::: section
### ***Exercise 1: Creating a Chart with Daigr.am***

We're going to use the Daigr.am ChatGPT plug-in to build a bar chart of homicides in Chicago. Start by going to the ChatGPT settings in the lower left corner of the interface and turning on the ChatGPT plug-ins feature.

Then go to the header and click on GPT-4 (or current version) on the top right button. And go to the Plug-ins pulldown menu. At the bottom of the menu, select the Plug-in Store option and a dialogue box will open with some plug-ins listed. In the search field, type Daigram and hit the install button. Then make sure it's checked in the top pulldown menu (you can activate three at a time as of July 2023), so the plug-in is active in ChatGPT.

Then type in the prompt and the data listed below. You can also cut-and-paste it out of this document to save time: <https://bit.ly/daigram>

Use Daigr.am to generate a bar chart with the following data:

**Chicago Homicides by Year (1990--2023)**

***Year Homicides***

- 1990: 854
- 1991: 928
- 1992: 943
- 1993: 855
- 1994: 931
- 1995: 828
- 1996: 796
- 1997: 761
- 1998: 704
- 1999: 643
- 2000: 633
- 2001: 667
- 2002: 656
- 2003: 601
- 2004: 453
- 2005: 451
- 2006: 471
- 2007: 448
- 2008: 513
- 2009: 460
- 2010: 438
- 2011: 436
- 2012: 507
- 2013: 422
- 2014: 420
- 2015: 491
- 2016: 778
- 2017: 658
- 2018: 569
- 2019: 506
- 2020: 774
- 2021: 797
- 2022: 723

Data Source: Chicago Police Dept.: [https://data.cityofchicago.org/browse?q=Murder&sortBy=relevance](https://data.cityofchicago.org)

Chart by \[ENTER YOUR NAME\]

You should wind up with something that looks like this: [https://daigr.am/5196bb4b.svg](https://daigr.am)

You can tweak the prompt a bit to add specific colors, a description under the title, etc.

*Note:* You can change the chart type with a second prompt such as this:

> Can you convert this data into an area chart?

\* \* \*

::: section
### ***Exercise 2: Google AutoDraw***

Start by opening this tool: [www.autodraw.com](http://www.autodraw.com)

Autodraw is one of Google's early stand-alone AI-driven tools. It's built for people who can't draw very well, but need a rights-free icon or logo. Just launch the software in your browser and make sure your browser's ad blockers are turned off so you can see the icons appear at the top of the screen as you draw.

To use it, just hold down your cursor and start sketching an object on the page. The more detail you provide -- such as the bicycle I attempted to draw ([Figure 10.2](#ch10.xhtml__15031-5909_ch010_Figure_002)) -- the closer Autodraw gets to providing a refined icon you can use in the toolbar ([Figure 10.3](#ch10.xhtml__15031-5909_ch010_Figure_003)). Just click on the icon and it will replace your rough sketch in the interface. You can use the tools on the left side of the screen to change colors, add text and many other features. You can download the image and use it in any project.

Autodraw is particularly helpful for building small icons you can import into mapping software, such as [MyMaps.Google.com](https://www.MyMaps.Google.com).


<a href="#ch10.xhtml_R_15031-5909_ch010_Figure_002"><em>Figure</em> <em>10.2</em></a> Mike’s goofy bicycle sketch in Autodraw


<a href="#ch10.xhtml_R_15031-5909_ch010_Figure_003"><em>Figure</em> <em>10.3</em></a> Mike’s drawing converted to a bicycle icon in Autodraw


<em>Figures</em> <em>10.4</em> and 10.5 Juxtapose slider: Before/after images of Mike’s bicycle drawing in Autodraw


::: section
### ***Exercise 3: Google Pinpoint***

Start by opening this tool and logging into your Google account: [https://journaliststudio.google.com/pinpoint/about](https://journaliststudio.google.com)

Pinpoint uses AI to perform a variety of tasks that are helpful to journalists. I use it for three things:

1.  Analyze PDFs to find the number of times a name or phrase appears in large documents
2.  Transcribe audio
3.  Extract text from an image

You can practice by logging into the software for free with your Google credentials (Gmail login) and uploading a short audio clip. The interface will give you analysis on the right, including the number of times certain phrases appear in the clip. You can click on the PDF at the bottom of the page ([Figure 10.6](#ch10.xhtml__15031-5909_ch010_Figure_006)) to get the transcript of the audio.

To analyze PDFs, simply upload them to Pinpoint, which will automatically build a menu on the right side of how many times a word appears in a document. For example, The New York Times published its analysis of the 2021 Trump impeachment documents, and you can track how many times a particular name or word appeared in the documents. You can click on the name in the toolbar and it will highlight where it appears in the documents. Your documents are private until you hit the "Publish" button in the upper right corner of the interface, should you wish to share them.

To extract text from an image, simply upload the photo to Pinpoint and click on the PDF that appears in the main interface. You should get an accurate transcription of any text that appears on the photo. It's a little hit-and-miss with photos of handwritten notes or blurry photos, so be sure to double-check all of the transcriptions.


<a href="#ch10.xhtml_R_15031-5909_ch010_Figure_006"><em>Figure</em> <em>10.6</em></a> Audio clip analysis in Google Pinpoint


\* \* \*


<a href="#ch10.xhtml_R_15031-5909_ch010_Figure_007"><em>Figure</em> <em>10.7</em></a> ChatGPT prompt for writing tips


::: section
### ***Exercise 4: ChatGPT***

Start by setting up a free account **(** <https://chat.openai.com>) or upgrade to a paid ChatGPT Plus account (\$20 a month) if you want to use plug-ins.

A few things to remember: ChatGPT is often incorrect and biased with its answers. But many users leverage its ability to answer specific questions and simplify complicated topics. For instance, I asked it for tips for writing shorter paragraphs and it provided some solid advice, just as Canva Docs did earlier in the book ([Figure 10.7](#ch10.xhtml__15031-5909_ch010_Figure_007)).

**Getting started:** Here are a few practice prompts to try with ChatGPT once you set up an account and log in to [https://chat.openai.com/chat](https://chat.openai.com):

Will you help me update my resume?

- Results: You should get some relevant tips. Include your resume text if you want deeper analysis and try this prompt: Analyze this resume and offer tips for improvement

Where did ChatGPT come from?

Result: It likely won't be able to answer.

- Tell me about the mining sector in South Africa (or another topic)

  Five tips for writing shorter paragraphs

  Gross domestic product of India prior to 2020

<!-- -->

- Remember, it can't give you any information newer than 2021, though that could change with future updates to the software.

Please write an API post request method in typescript

Mess with it a bit: Try a riddle: You have one fair coin, and one biased coin that lands Heads with probability ¾. You pick one of the coins at random and flip it three times. It lands Heads all three times. Given this information, what is the probability that the coin you picked is the fair one?

This should prompt a funny result ...

Why are you so helpful? What do you want in return?

This should prompt a funny result as well.

Ask ChatGPT to write about you. You'll be interested in what it finds. Mine was more accurate than I thought it would be

Is it self-aware? Give me 30 jobs that AI won't overtake and the reasons why

**Headlines:** Have it write an SEO-driven headline for a news brief that you cut and paste into the interface at the end of the prompt.

**Story research:** I'm not keen on asking ChatGPT to write a story for you, but you could use it to research a story as long as you closely fact-check the results. The Miami Herald successfully wrote an interesting story about the city's tourism using ChatGPT. But other publications have had disastrous results, including several experiments we've tried in my classes.

Ask it to write a story about Chicago and tourism. Start with these prompts, then work in some of your own questions. No need to write the story. Just ask the questions.

What are the best things about Chicago (or a city of your choosing)

Best places to visit in Chicago

Five affordable Chicago restaurants

You can pull from the answers to help build your story and fact-check it.

**For fun:** Brian Miller, a former student of mine who now works in community relations for the Florida Highway Patrol, asked ChatGPT to write a distracted driving campaign song in the style of Taylor Swift. I replicated it in [Figure 10.8](#ch10.xhtml__15031-5909_ch010_Figure_008). It wasn't bad, although I'm not much of a T-Swift fan.

::: section
### ***Exercise 5: Data Analysis Exercises***

These prompts are experimental. Fact-check any analysis you unearth in ChatGPT-4 or a more current prompt.

Analysis prompt: I want you to act as a data scientist and analyze the dataset. Provide me with the exact and definitive answer for each question. Do not provide me with the code snippets for the questions. The dataset is provided below. Consider the given dataset for analysis. The first row of the dataset contains the header.

\[ChatGPT will ask for the data\]


<a href="#ch10.xhtml_R_15031-5909_ch010_Figure_008"><em>Figure</em> <em>10.8</em></a> Taylor Swift song


Paste the dataset into ChatGPT Copy and paste the dataset from Excel/Google Sheets to ChatGPT (including column headers; ChatGPT has a character limit of 2,048).

For fun: To create a silly data viz image, try this prompt to get a silly column chart:

- How many legs does a giraffe have? Answer in the form of a one-page PDF download. No talk: just go

\* \* \*

::: section
### ***Exercise 6: Organizing an Outline in ChatGPT and Google Bard***

AI tools are good at providing outlines, summaries, structure and organizing projects or thoughts. You can put this to the test in ChatGPT and Bard with anything you want.

For example, I entered the same prompt into ChatGPT and Bard: organize a book chapter entry about four good AI writing tools. The results:

::::::::::::: section
## **ChatGPT:** 

Chapter Title: Harnessing the Power of AI: Four Exceptional Writing Tools

### ***Introduction:*** 

- Briefly explain the growing importance of AI in the field of writing and how it has revolutionized the way we create content.
- Highlight the benefits of using AI writing tools, such as improved efficiency, enhanced creativity, and higher quality output.

***Section 1: Tool 1 -- "AutoWriter Pro: Transforming Ideas into Polished Prose"***

- Discuss the features and capabilities of AutoWriter Pro, an AI-powered writing tool designed to assist in generating well-structured and engaging content.
- Highlight its ability to analyze input data, understand context and produce coherent and coherent writing pieces.
- Provide examples of how AutoWriter Pro can be utilized for various writing tasks, such as blog posts, essays and marketing copy.

***Section 2: Tool 2 -- "CreativeWords: Igniting Imagination with AI-Driven Inspiration"***

- Explore CreativeWords, an AI writing tool that specializes in generating creative and original content.
- Explain how CreativeWords employs sophisticated algorithms to inspire users by offering unique ideas, suggestions and stylistic variations.
- Discuss its usefulness in overcoming writer's block, sparking creativity and enabling writers to explore new angles and perspectives.

***Section 3: Tool 3 -- "GrammarGuardian: Elevating Writing Quality through Intelligent Editing"***

- Introduce GrammarGuardian, an advanced AI tool focused on improving the quality of writing through intelligent editing and proofreading.
- Highlight its ability to detect grammatical errors, punctuation mistakes and stylistic inconsistencies.
- Discuss how GrammarGuardian provides suggestions and explanations to help users enhance their writing skills and produce error-free content.

***Section 4: Tool 4 -- "LanguageMaster: Enhancing Language Proficiency with AI-Powered Tutoring"***

- Explore LanguageMaster, an AI writing tool that functions as a personalized language tutor, aiding users in improving their writing proficiency.
- Discuss its features, such as grammar and vocabulary exercises, interactive writing prompts and real-time feedback on language usage.
- Explain how LanguageMaster adapts to individual learning needs and provides targeted recommendations to enhance overall writing skills.

### ***Conclusion:*** 

- Summarize the key advantages of using AI writing tools, including increased productivity, improved creativity, enhanced language proficiency, and higher-quality content.
- Emphasize the role of AI as a valuable ally for writers, assisting them in overcoming challenges and achieving their full potential.
- Encourage readers to explore and leverage the power of AI writing tools to elevate their writing abilities and accomplish their writing goals.

**Bard's response:**

### ***Introduction*** 

Artificial intelligence (AI) writing tools are becoming increasingly popular as they offer a variety of benefits to writers, including:

- Increased productivity: AI writing tools can help writers to produce more content in less time.
- Improved quality: AI writing tools can help writers to produce more high-quality content.
- Enhanced creativity: AI writing tools can help writers to come up with new and innovative ideas.
- Reduced costs: AI writing tools can help businesses to save money on content creation costs.

***Four Good AI Writing Tools***

There are a number of AI writing tools available on the market, but some of the most popular and effective tools include:

- Jasper: Jasper is a comprehensive AI writing tool that can be used for a variety of tasks, including writing blog posts, articles, social media posts, and more. Jasper is powered by GPT-3, one of the most advanced language models in the world, and it can generate high-quality content that is both informative and engaging.
- [Copy.ai](http://Copy.ai): [Copy.ai](http://Copy.ai) is an AI writing tool that is specifically designed for copywriting. [Copy.ai](http://Copy.ai) can generate catchy headlines, persuasive sales copy, and effective marketing materials. It is also powered by GPT-3, and it can produce high-quality content that is tailored to your specific needs.
- Anyword: An AI writing tool that can be used to create a variety of content, including blog posts, articles, social media posts, and more. Anyword is powered by a proprietary AI language model, and it can generate high-quality content that is both informative and engaging.
- Sudowrite: An AI writing tool that is specifically designed for fiction writing. Sudowrite can help you to brainstorm ideas, develop characters, and plot out your story. It is also powered by GPT-3, and it can generate high-quality content that is both creative and engaging.

### ***Conclusion*** 

- AI writing tools are a powerful tool that can help writers to produce more high-quality content in less time. If you are looking for an AI writing tool to help you with your writing, then any of the four tools listed above would be a great option.

\* \* \*

**Summary:** Both tools produced reasonably good outlines with different examples of tools, some of which I previously mentioned in this chapter. I would sub in my own examples rather than solely trust AI recommendations, but I *would* follow the outlines that the tools produced. Both were eerily similar to how I previously wrote the entries in this chapter.

\* \* \*


<a href="#ch10.xhtml_R_15031-5909_ch010_Figure_009"><em>Figure</em> <em>10.9</em></a> Data dictionary created in ChatGPT


::: section
### ***Exercise 7: Create a Data Dictionary in ChatGPT***

A data dictionary provides a detailed description of the dataset, which includes the meaning of each column, the type of the data and any other relevant information. Let's make one with a simple dataset and this prompt: Can you make a data dictionary with the following dataset. Then paste the header and first 8--10 rows of data into ChatGPT.

Try it yourself. Here's a practice dataset of bridge inspections: <https://bit.ly/bridgedataset>

Copy the first eight rows from that sheet and paste it after this prompt: Can you make a data dictionary with the following dataset:

Result: You should get a table with a perfect dictionary of header terms, examples of the data and measured distance ([Figure 10.9](#ch10.xhtml__15031-5909_ch010_Figure_009)).

\* \* \*

::::::: section
### ***Exercise 8: Creating Illustrations in MidJourney and Discord***

Set up a [https://discord.com/](https://discord.com) account first, then connect it to MidJourney while setting up that account: [www.midjourney.com/home](http://www.midjourney.com)

Image-generation tools teach journalists good descriptive writing skills, as evidenced by the following prompt. Load it into Discord and see:

- /imagine 1990s glamor photo, medium overhead shot from above, sharp focus low-light photography shot on Fujifilm, capturing an Italian woman with tired eyes resting on a tufted couch, wearing a royal Versace sequin gown, luxurious Parisian mansion, dim chandelier lighting, elegant, glamorous, sophisticated royalty. It's been a long night. -- ar 16:9 -- v5

As I wrote earlier in this book, be careful when labeling the images you generate when you publish them. Make it clear that it's a photo illustration, and even add the prompt you used to generate it into the alt tags for the photos. You can insert alt tags in Photoshop or when uploading images to Twitter. The more transparent, the better. Under no circumstances should you use image-generation tools to mislead anyone or recreate a breaking news scene.

If you think a photo you find online might be created using an image-generation tool, simply check the alt tags or reverse image search it in [images.google.com](https://www.images.google.com) to see if it has appeared elsewhere online and in what context.

MidJourney and its competitors are handy for creating section headers for websites. I've used many on [JournalistsToolbox.ai](http://JournalistsToolbox.ai), and for food illustrations and other feature-driven projects, and for the aforementioned food journalism photos.

**For fun -- a prompt for Top Gun fans:**

- /imagine Action scene still Top Gun, of a F14 fighter plane accompanied by fighter squadron fighting enemy fighter jets above somewhere in the middle east, flying high, firing air-to-air missiles, intense Battle scene, epic, ultra realistic, action movie, shot with DJI Phantom 4 Pro drone camera, eye Bird's view, golden hour, hyper-detailed, directed by Ridley Scott -- ar 235:100 -- s 1000 -- q 2 -- v 5

**For fun -- a prompt for Star Wars fans:**

- /imagine Editorial photo of a futuristic Jakku desert landscape with a spaceship boneyard, noon mood, featured in national geographic, close up shot, 32k, cinematic composition, professional color grading, film grain, atmosphere, wondrous, cinematic glamor shot --v 5

**Adding details to prompts:** The more detail you provide, the better your prompts will be. You can add lighting, camera type, camera angles, and even theme the prompt to a specific movie director. Here are a handful of my favorite prompts to work with. Try mixing and matching them with a specific image you want to generate.

::: section
#### *MidJourney Lighting Prompts*

And class is now in session ...

**→ Natural Lighting**

- "Sunlight" -- Common source of lighting for outdoor images.
- "Moonlight" -- Natural lighting that creates a soft/ethereal effect.
- "Firelight" or "Candlelight" -- Warm and cozy light source that helps create rustic and romantic effects for indoors.
- "Cloudy Skies" or "Overcast" -- Soft and diffused natural light for portrait photography.
- "Reflections" -- Can provide artistic shimmering and dreamy effect when paired with other lighting.

**→ Ambient Lighting**

- "Overhead" -- Light fixtures like ceiling lights or chandeliers for lighting indoor scenes.
- "Wall Sconces" -- Adds a decorative element to a room while providing a soft, indirect lighting effect.
- "Table Lamps" -- May provide warm and cozy effect OR bright and harsh lighting.
- "Floor Lamps" -- Helps provide warm and cozy effect, but also lights the corners of the scene.
- "Natural Light" -- "Windows" or "Skylights" can provide consistent lighting throughout the scene.

**→ Artificial and Directional Lighting**

- "Studio Lights" -- Powerful/controlled light source best for portrait, product and fashion.
- "Strobe Lights" -- Flash photography with bright light to illuminate the subject.
- Sunny -- Canon EOS 5D Mark IV camera with a Canon EF 24--70mm f/2.8L II USM lens
- Partly Cloudy -- Nikon D850 camera with a Nikkor 24--70mm f/2.8E ED VR lens
- Rainy -- Sony Alpha a7 III camera with a Sony FE 16--35mm f/2.8 GM lens and waterproof housing
- Snowy -- Canon EOS-1D X Mark II camera with a Canon EF 24--105mm f/4L IS II USM lens and waterproof housing
- Overcast -- Panasonic Lumix GH5S camera with a Panasonic Lumix 12--35mm f/2.8 II lens
- Foggy -- Sony Alpha a7R IV camera with a Sony FE 70--200mm f/2.8 GM OSS lens

::: section
#### *MidJourney Camera Angles and Shots*

- Eye-level shot:
- Sony Alpha a7 III camera with a Sony FE 24--105mm f/4 G OSS lens
- Low-angle shot:
- Sony Alpha a7 III camera with a Sony FE 16--35mm f/2.8 GM lens
- High-angle shot:
- Nikon D850 camera with a Nikkor 24--70mm f/2.8E ED VR lens
- Extreme low-angle shot:
- Canon EF 14mm f/2.8L II USM lens on a Canon EOS 5D Mark IV camera with a low-angle tripod
- Extreme high-angle shot:
- Canon EF 70--200mm f/2.8L IS III USM lens on a Canon EOS 5D Mark IV camera with a high-angle tripod
- Side-angle (side-view):
- Panasonic Lumix GH5S camera with a Panasonic Lumix 12--35mm f/2.8 II lens
- Shot from behind:
- Nikon D850 camera with a Nikkor 70--200mm f/2.8E FL ED VR lens
- Close-up shot:
- Canon EF 50mm f/1.2L USM lens on a Canon EOS 5D Mark IV camera

::: section
#### *Time of the Day*

- Sunrise: Sony A7R IV camera with a Canon RF 15--35mm f/2.8L IS USM lens
- Morning: Fujifilm X-T4 camera with a Fujinon XF 16--55mm f/2.8 R LM WR lens
- Afternoon: Sony A7 III camera with a Sony FE 70--200mm f/2.8 GM OSS lens
- Golden Hour: Canon EOS R5 camera with a Canon RF 50mm f/1.2L USM lens
- Sunset: Sony A7R IV camera with a Sony FE 16--35mm f/2.8 GM lens
- Twilight: Panasonic Lumix S1H camera with a Panasonic Lumix S Pro 50mm f/1.4 lens
- Night: Sony A7S III camera with a Sigma 35mm f/1.2 DG DN Art lens

::: section
#### *Ambiance and Styling*

- Dark and moody: Sony a7S III with Sony FE 50mm f/1.4 ZA lens
- Bright and vibrant: Canon EOS R6 with Canon EF 16--35mm f/2.8L III USM lens
- Fantasy: Fujifilm X-T4 with Fujinon XF 56mm f/1.2 R lens
- Historical: Fujifilm GFX 100S with Fujinon GF 23mm f/4 R LM WR lens or Nikon Z7 II with Nikkor Z 50mm f/1.2 S lens

\* \* \*

::: section

## Footnotes

- ChatGPT: [https://chat.openai.com/chat](https://chat.openai.com)
- ChatGPT Daigram Chart Example: [https://daigr.am/5196bb4b.svg](https://daigr.am)
- ChatGPT Daigram Exercise: <https://bit.ly/daigram>
- Craft Docs: [www.craft.do](http://www.craft.do)
- Discord: <https://discord.com>
- Google AutoDraw: [www.autodraw.com](http://www.autodraw.com)
- Google Bard: <https://bard.google.com>
- Google Chrome Store: [https://chrome.google.com/webstore/category/extensions](https://chrome.google.com)
- Google Pinpoint: [https://journaliststudio.google.com/pinpoint/about](https://journaliststudio.google.com)
- Journalist's Toolbox Productivity Training Video: <https://bit.ly/productivityvid>
- Journalist's Toolbox: AI Tools for Journalists: [www.journaliststoolbox.org/2023/05/09/ai-tools-for-journalists](http://www.journaliststoolbox.org)
- Medium, Joe Amditis, "The Nazi Chatbots Are Coming": [https://medium.com/centerforcooperativemedia/the-nazi-chatbots-are-coming-432dc907f492](https://medium.com)
- MidJourney: [www.midjourney.com/home](http://www.midjourney.com)
- New York Times Trump Impeachment Documents in Pinpoint: [https://journaliststudio.google.com/pinpoint/search?collection=eff94de951c2a840](https://journaliststudio.google.com)
- Personal Policy on Ethical AI Use: [https://dragonflyeditorial.com/policy-on-ethical-ai-use](https://dragonflyeditorial.com)
- Readwise Reader: [https://readwise.io/read](https://readwise.io)
- Slido: [www.slido.com](http://www.slido.com)
- SPJ Code of Ethics: [www.spj.org/ethicscode.asp](http://www.spj.org)
- Superhuman: <https://superhuman.com>
- Trusting News: See How Newsrooms Talk Publicly About Improving Diversity in Their Coverage: [https://medium.com/trusting-news/see-how-newsrooms-talk-publicly-about-improving-diversity-in-their-coverage-e3600ca42baf](https://medium.com)
- Wonder Tools: Craft Docs, Jeremy Caplan: [https://wondertools.substack.com/p/craft](https://wondertools.substack.com)
- Wonder Tools: Readwise Reader, Jeremy Caplan: [https://wondertools.substack.com/p/reader](https://wondertools.substack.com)


# 11 Digital Security \| Advanced ChatGPT and Data Visualization Exercises

DOI: [10.4324/9781003431787-12](https://doi.org/10.4324/9781003431787-12){aria-label="D.O.I. link to this document."}


**Key Resources**

- JournalistsToolbox.ai: <http://journaliststoolbox.ai>
- ChatGPT: <https://chat.openai.com>
- Global Investigative Journalism Network Safety and Security: [https://helpdesk.gijn.org/support/solutions/articles/14000036509-safety-and-security](https://helpdesk.gijn.org)
- Mojo Manual: Safe Reporting: [www.mojo-manual.org/safe-reporting](http://www.mojo-manual.org)

\* \* \*

::: section
## Digital Security

CUNY Professor Jeremy Caplan studies thousands of apps and tools and offers advice to professional journalists and other professionals in his Wonder Tools newsletter. When asked about what he uses for digital security, Caplan offered some sage but lighthearted advice.

He suggests a physical security key, like the \$25 Yubikey, for two-factor authentication to protect important accounts like your email and bank information. He also recommends 1Password for securely managing passwords, adding that it has a program to provide free premium access to journalists.

"And avoid online raffles," Caplan said. "Use less of Facebook and other tracking apps."

Caplan's last recommendation was a little tongue-in-cheek, but there's truth to it: Being careful about what you *do* online can be as important as any safety software or app you put on your computer or phone.

In this chapter, you'll learn about digital security tools, apps and techniques to keep you, your sources and your data safe. You'll also work with some advanced AI and data visualization exercises: data scraping, scraping Google Finance data viz charts and maps with Flourish.studio, Datawrapper, Canva and Infogram. You'll also learn about some more ChatGPT prompts and plug-ins for journalists.

::: section

## Start by Minding Your Passwords

Between 2011 and 2017, Google found that the most popular passwords used on its sites and tools were: (1) 123456; (2) "password" and (3) 1234568. A criminal doesn't even need to use software to hack an account using those passwords.

Passwords, along with two-factor authentication, are a first line of defense in protecting your reporting and personal information. They can mean the difference between a routine day and a huge headache.

Password managers such as 1Password and Google Smart Lock offer a secure way to store them and use them on any site you open without having to remember and retype them. There are many other two-step verification tools available to journalists. Many newsrooms have their own. I've been using the Duo app for years for teaching and had no issues. Google also offers two-step verification at [security.google.com](https://www.security.google.com).

One of the easiest ways to get hacked is to let a password get out in the open. Avoid using the same password for multiple accounts and never, ever, store them in a server like Google Drive. It's too easy for them to be discovered.

And don't think of digital security in terms of pass*words* but rather a pass*phrase*. A phrase is something you can easily remember, and by taking the first letter of each word, combine it with some numbers and characters and, presto! ... you have a secure passphrase.

Example: My friends Tom and Jasmine send me a funny email once a day that converts to this passphrase:

**MfT&Jsmafe1ad!!!**

The phrase and random series of letters and numbers makes it much more difficult for hackers to run scripts to hack your accounts, than, say, using your high school alma mater's nickname and the year you were born -- or other things that are readily available about you online.

Another good line of defense: Google's Password Alert is a Chrome extension that helps Google Workspace and Cloud Identity users avoid phishing attacks by detecting when they enter their Google password into any websites other than the Google sign-in page.

Here are some other tips for keeping your passwords secure:

- Change your password every four months
- Ensure all your passwords are unique
- Make sure all passwords are a minimum of 16 characters
- Use upper/lowercase, numbers, special characters
- Use nonsensical words (not in dictionary) or, better yet, a passphrase

If you need more help, Reporters Without Borders has a 12-minute video on creating passwords. [https://www.youtube.com/watch?v=tw6A-A_Nw_U](https://www.youtube.com)

::: section
## Virtual Private Networks

Before I can file my students' grades at UIC, I must first pass through two-factor authentication, then log in through a virtual private network (VPN) to access the grading system. This software ensures that my students' privacy, and mine, is secure.

A VPN is a useful tool that protects your online activity by creating a secure "tunnel" that sits between your device and the site or service you're trying to access. A VPN acts as a gatekeeper between your device and whatever you're trying to interact with -- a government website, social media service, a streaming service, or some files stored on your company's private network.

Many people use VPNs to access email and corporate files outside the office. Foreign journalists use them to visit sites and access content that isn't available in their country. They also protect you from others tracking your Internet traffic while browsing the web. This is extremely important for investigative and international journalists who may have their devices seized by authorities.

Tools like Google Safe Browsing protect people from dangerous websites, apps and ads across Google products. And we share our technology with other companies to help you stay safe on other apps and browsers, including Firefox and Safari. Google's Safe Browsing technology automatically helps protect devices by showing warnings to users in Chrome, Google Search and Gmail when they attempt to navigate to sites or download files that it detects as malware or phishing sites or files.

Google Drive also scans documents for malware. [Sync.com](https://www.Sync.com) is a free cloud storage system that is encrypted and more secure and is easy to use.

::: section

## DDoS Protection

A popular tool among hacktivists, a Distributed Denial of Service (DDoS) attack is a method that criminals use to overwhelm an online service, like a website, by bombarding it with fake Internet traffic from multiple different locations. The sheer amount of traffic prevents real users from accessing the targeted sites or online services.

While typically not a threat to individual journalists, it can bring down a media company's website quickly and cheaply -- some DDoS services cost as little as \$5. There are several defenses a site can take to stay safe, from increasing bandwidth to implementing server-level protections. It's best to discuss the options with your webmaster and IT staff before implementing products.

::: section
## Mobile Security

Mobile devices can be easily lost or stolen. Authorities once confiscated my iPhone at the French border, only to find that they couldn't see much because of the security apps I use:

- **Freedome:** This is my go-to mobile VPN app. It costs \$40 a year but is worth it. Turn it on with one click and you can surf the web safely and securely.
- **Find My iPhone:** Location tracker allows you to follow your phone's location from your iMac, MacBook, iPad or other devices. I use this along with an Air Tag in my gear bag in case the two are separated.
- **Signal:** This app provides encrypted messages on smartphones. If the phone is taken, no one can understand what was written there. It's extremely popular among investigative journalists. I also use WhatsApp periodically.
- **Lookout Mobile Security:** This app provides the user with many benefits to protecting information and is considered one of the best security apps for iPhone.
- **Private Browsers:** Just like on desktops and laptops, you should use private browsing mode on mobile browsers, too. Private browsers won't ward off all attacks, but they do provide some basic security. In my experience, DuckDuckGo provides the best privacy settings.

::: section

## Phishing Attacks

Admit it, you've probably clicked on a link or PDF attachment in an email from a sender you weren't familiar with, and all kinds of craziness took place. If so, you were the victim of one type of "phishing" scam -- attempts to trick you into granting unauthorized access to your account or to infect your machine with malware. Malware or "malicious software" is any software or mobile application designed to harm a computer, mobile device, the software it's running, or its users.

If someone steals your password, they could gain unauthorized access to your account. They could steal personal information, pretend to be you to send unwanted or harmful emails, or use your account to reset the passwords for your other accounts.

Hackers reach out to targets through email, telephone, text message, PDFs or apps, posing as a legitimate person or trusted organization in order to trick you into providing sensitive personal information. They may link you to a credible-looking login page that tricks you into giving your username and password or granting permissions to a malicious app. Once your password is revealed, the hacker could access your account or infect your machine. Studies have shown up to half of all newsrooms around the world have been victims of phishing scams.

Google recommends that journalists watch for these techniques in phishing scams:

- Be wary of requests for personal information. Don't reply to suspicious emails, instant messages or pop-up windows that ask for passwords or financial information.
- Some sophisticated phishing attacks can occur through infected documents and PDF attachments.
- Never click on questionable links. Always double-check the URL to make sure you're entering your data into a legitimate website or app.
- Watch out for impersonators requesting money, claiming to be stranded in a foreign country or saying their phone is stolen and can't be called.
- If you receive an account security notification from Google, go to [security.google.com](https://www.security.google.com) instead of clicking on links in the email to check your account security status.

::: section
## Email Security Tips

The Global Investigative Journalism Network (GIJN) cites three critical tips for dealing with email security in its digital self-defense guide:

- If you travel to a country known for spying on the media, don't rely on an email provider based there.
- At home, use a secure provider -- you can tell if your email is secured by looking for the "https" in the address bar. Gmail is secure by default, while Yahoo and Facebook settings can be adjusted. Why? If you use a free wireless network, anyone can tap into your screen with a simple and free software program. That's a problem if you're communicating with a source.
- Don't assume your employer is protecting your account. Ask your technology desk about what precautions it takes, and consider getting a personal account.
- PGP -- Pretty Good Privacy acronym. It's a way to encrypt emails by using one key to lock and the other to unlock. You give the key that locks the chest so people can send you files and messages. But only you have the key to unlock the content.

::: section
