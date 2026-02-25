<!-- chunk: 1/1 | source: 97a-nicar-2014.md | words: 3968 -->
<!-- headings: NICAR 2014 Tipsheets & Session Notes; nicar14-notes/1-1.md; nicar14-notes/1-2.html; Rifling through the mapping toolbox; Speakers:; Notes; More slides; nicar14-notes/1-2.md; nicar14-notes/1-3.html; Enhance your stories with statistics; Speakers:; Notes; More slides; nicar14-notes/1-3.md; nicar14-notes/1-4.html; Love your life, retire your servers; Speakers:; Notes; What can static sites do for you?; Static sites are bad for: -->

# NICAR 2014 Tipsheets & Session Notes


## nicar14-notes/1-1.md

#Welcome and overview

####Speakers:
* **[Mark Horvit][9721-001]**, *Executive Director, IRE*
* **[Megan Luther][9721-002]**, *Training Director, IRE*
* **[Jaimi Dowdell][9721-003]**, *Senior Training Director, IRE*


[9721-001]: https://twitter.com/markhorvit
[9721-002]: https://twitter.com/MeganLuther
[9721-003]: http://www.ire.org/about/staff-bios/
####Notes
More than 900 people registered for NICAR, the most ever. There are people from more than 20 countries here.

Check out [IRE's website](http://ire.org/) for benefits like training and the data library.

[IRE link](http://ire.org/events-and-training/event/973/1133/)

## nicar14-notes/1-2.html

# Rifling through the mapping toolbox


#### Speakers:

- **[Ryan McNeill](https://twitter.com/McNeill_Reuters)**, *data journalist, Reuters*
- **[Michael Corey](https://twitter.com/mikejcorey)**, *senior news applications developer, The Center for Investigative Reporting*

#### Notes

Opening example: Shapefile of the Florida coastline Goal: Create a 1-mile buffer zone Problem: The shape was way too complex; attempts became too memory intensive.

"What you need is a tool to solve the problem. No time for obsession."

Think about the end product when choosing the best tools to get there.

When using a geocoding tool, read the TOS:

- Required to use Lat/Lng on their map?
- Are you allowed to cache?
- Is there a rate limit?

(the last two are often at odds)

Some examples:

- [Google Geocoding API](https://developers.google.com/maps/documentation/geocoding/)
- [ArcGIS Online](http://www.esri.com/software/arcgis/arcgisonline)
- [Oatmeal (for Python)](https://pypi.python.org/pypi/python-omgeo) or [Ruby Geocoder](http://www.rubygeocoder.com/)

Use Caution:

- Doublecheck your results
- Lat/Lng may be wrong
- Check the precision field

Example: [Reuters' Ammonium Nitrate Map](http://www.reuters.com/article/interactive/idUSBRE94L19020130522?view=large)

- Hand-checked data
- Had to eliminate some that couldn't be confirmed
- Result: Undercounted facilities, but low risk of misidentifying

(Still did, due to old data provided by states)

Vector Web Map tools:

- [GeoJSON](http://geojson.org/)
- [TopoJSON](https://github.com/mbostock/topojson)
- [D3.js](http://d3js.org/)
- [Kartograph](http://kartograph.org/)

It's hard to find data that crosses international borders.

Example: [CIR's drug trafficking map](http://static.apps.cironline.org/border-seizures/)

Question: Where is a good place to start? Answer: [TileMill](https://www.mapbox.com/tilemill/)

Question: How can you use a huge dataset? Answer: Narrow it down. Clean the data. Use the accuracy field. Throw out P.O. Boxes and similar. Test if returned location and actual location are in the same county.

[Link to slides](https://docs.google.com/presentation/d/1IbN8EM1VSXcDz7_kSgY5ZBi13EqCogwiXBWTdOD4su8/)

[IRE link](http://ire.org/events-and-training/event/973/1189/)

#### More slides


## nicar14-notes/1-2.md

#Rifling through the mapping toolbox


####Speakers:
* **[Ryan McNeill](https://twitter.com/McNeill_Reuters)**, *data journalist, Reuters*
* **[Michael Corey](https://twitter.com/mikejcorey)**, *senior news applications developer, The Center for Investigative Reporting*

####Notes
Opening example: Shapefile of the Florida coastline
Goal: Create a 1-mile buffer zone
Problem: The shape was way too complex; attempts became too memory intensive.

"What you need is a tool to solve the problem. No time for obsession."

Think about the end product when choosing the best tools to get there.

When using a geocoding tool, read the TOS:

* Required to use Lat/Lng on their map?
* Are you allowed to cache?
* Is there a rate limit?

(the last two are often at odds)

Some examples:

* [Google Geocoding API](https://developers.google.com/maps/documentation/geocoding/)
* [ArcGIS Online](http://www.esri.com/software/arcgis/arcgisonline)
* [Oatmeal (for Python)](https://pypi.python.org/pypi/python-omgeo) or [Ruby Geocoder](http://www.rubygeocoder.com/)

Use Caution:

* Doublecheck your results
* Lat/Lng may be wrong
* Check the precision field

Example: [Reuters' Ammonium Nitrate Map](http://www.reuters.com/article/interactive/idUSBRE94L19020130522?view=large)

* Hand-checked data
* Had to eliminate some that couldn't be confirmed
* Result: Undercounted facilities, but low risk of misidentifying

(Still did, due to old data provided by states)

Vector Web Map tools:

* [GeoJSON](http://geojson.org/)
* [TopoJSON](https://github.com/mbostock/topojson)
* [D3.js](http://d3js.org/)
* [Kartograph](http://kartograph.org/)

It's hard to find data that crosses international borders.

Example: [CIR's drug trafficking map](http://static.apps.cironline.org/border-seizures/)

Question: Where is a good place to start? Answer: [TileMill](https://www.mapbox.com/tilemill/)

Question: How can you use a huge dataset? Answer: Narrow it down. Clean the data. Use the accuracy field. Throw out P.O. Boxes and similar. Test if returned location and actual location are in the same county.

[Link to slides](https://docs.google.com/presentation/d/1IbN8EM1VSXcDz7_kSgY5ZBi13EqCogwiXBWTdOD4su8/)

[IRE link](http://ire.org/events-and-training/event/973/1189/)

####More slides

## nicar14-notes/1-3.html

# Enhance your stories with statistics


#### Speakers:

- **[Steven Rich](https://twitter.com/dataeditor)**, *database editor, The Washington Post*
- **[Rob Barry](https://twitter.com/rob_barry)**, *investigative reporter, The Wall Street Journal*

#### Notes

"We're journalists, not scientists."

Don't overthink. Mostly you need to:

- Count
- Sum
- Group
- Think

Seek the middle. It often describes the group. Check the mean vs. the median.

Also quartiles and correlation. *Correlation does not equal causation.*

Histograms are powerful. A visualization of distribution. You can eyeball mean vs. median.

Checking fortuitous stock trades, using a Monte Carlo simulation to see if actual profit was likely.

Fisher's Exact Test is useful for small sample sizes and categorical data.

Linear regression is for continuous data. Logistic regression is for binary data.

Tips to help avoid mistakes:

- Try to prove yourself wrong
- Run it by your targets
- Ask an expert (in the newsroom or not)
- Make sure you're using the right test

Question: How to translate stats to English (for a story)? Answer: Think thoroughly about what you're actually saying to boil it down. Use a methodology box/page/etc. to explain in detail.

[IRE link](http://ire.org/events-and-training/event/973/1185/)

#### More slides


## nicar14-notes/1-3.md

#Enhance your stories with statistics


####Speakers:
* **[Steven Rich][9873-001]**, *database editor, The Washington Post*
* **[Rob Barry][9873-002]**, *investigative reporter, The Wall Street Journal*

[9873-001]: https://twitter.com/dataeditor
[9873-002]: https://twitter.com/rob_barry

####Notes

"We're journalists, not scientists."

Don't overthink. Mostly you need to:

* Count
* Sum
* Group
* Think

Seek the middle. It often describes the group. Check the mean vs. the median.

Also quartiles and correlation. *Correlation does not equal causation.*

Histograms are powerful. A visualization of distribution. You can eyeball mean vs. median.

Checking fortuitous stock trades, using a Monte Carlo simulation to see if actual profit was likely.

Fisher's Exact Test is useful for small sample sizes and categorical data.

Linear regression is for continuous data. Logistic regression is for binary data.

Tips to help avoid mistakes:

* Try to prove yourself wrong
* Run it by your targets
* Ask an expert (in the newsroom or not)
* Make sure you're using the right test

Question: How to translate stats to English (for a story)? Answer: Think thoroughly about what you're actually saying to boil it down. Use a methodology box/page/etc. to explain in detail.

[IRE link](http://ire.org/events-and-training/event/973/1185/)

####More slides

## nicar14-notes/1-4.html

# Love your life, retire your servers


#### Speakers:

- **[Andy Boyle](https://twitter.com/andymboyle)**, *news applications developer, Chicago Tribune*
- **[Tasneem Raja](https://twitter.com/tasneemraja)**, *data and graphic editor, Mother Jones*

#### Notes

Check out [Mother Jones' GitHub news quiz](https://github.com/motherjones/newsquiz)

[Tabletop.js](https://github.com/jsoma/tabletop) turns Google Spreadsheets into structured HTML.

##### What can static sites do for you?

Boston.com elections: One awesome dude's laptop.

Cheaper: Chicago Tribune's 2012 election traffic cost (you know, the one where the president was from Chicago?) was \~\$20.

Fast: How quickly do you need data online? Live link to the data, iframe a google spreadsheet, use [Tarbell](http://tarbell.tribapps.com/).

Non-techies in the newsroom can have control.

##### Static sites are bad for:

- Lots of feedback or input from users.
- Geospatial queries.
- Thousands of rows.

Check out [Chicago Tribune's Bootstrap Templates.](http://newsapps.github.io/bootstrap/)

[Presentation Link](http://nicar2014.s3.amazonaws.com/slides.html#/) [IRE link](http://ire.org/events-and-training/event/973/1184/)

#### More slides


## nicar14-notes/1-4.md

#Love your life, retire your servers


####Speakers:
* **[Andy Boyle][4004-001]**, *news applications developer, Chicago Tribune*
* **[Tasneem Raja][4004-002]**, *data and graphic editor, Mother Jones*


[4004-001]: https://twitter.com/andymboyle
[4004-002]: https://twitter.com/tasneemraja

####Notes

Check out [Mother Jones' GitHub news quiz](https://github.com/motherjones/newsquiz)

[Tabletop.js](https://github.com/jsoma/tabletop) turns Google Spreadsheets into structured HTML.

#####What can static sites do for you?

Boston.com elections: One awesome dude's laptop.

Cheaper: Chicago Tribune's 2012 election traffic cost (you know, the one where the president was from Chicago?) was ~$20.

Fast: How quickly do you need data online? Live link to the data, iframe a google spreadsheet, use [Tarbell](http://tarbell.tribapps.com/).

Non-techies in the newsroom can have control.

#####Static sites are bad for:

* Lots of feedback or input from users.
* Geospatial queries.
* Thousands of rows.

Check out [Chicago Tribune's Bootstrap Templates.](http://newsapps.github.io/bootstrap/)

[Presentation Link](http://nicar2014.s3.amazonaws.com/slides.html#/)

[IRE link](http://ire.org/events-and-training/event/973/1184/)

####More slides

## nicar14-notes/1-5.html

# The customized Census

### How to use microdata when you just can't find the right table


#### Speakers:

- **[Robert Gebeloff](https://twitter.com/gebeloffnyt)**, *data journalism specialist, The New York Times*
- **[Katie Genadek](http://usa.ipums.org/usa/cite.shtml)**, *director of outreach and dissemination, IPUMS*

#### Notes

Census microdata from [IPUMS](https://www.ipums.org/) gives you the full range of responses, some custom tables but there's also some data supression.

IPUMS is the Integrated Public Use Microdata Series.

It's standardized across years. Has documentation. And includes the American Community Survey from 2000-2012.

Example: How many Italian barbers are there?

You can find a total for the country. Then you can narrow it down to a particular state and gender.

But check out the confidence interval and raw numbers.

Another example: How many people might be affected by the ACA/Medicaid Gap in states that aren't expanding it.

Problem: Had to translate the census poverty levels to the Medicaid poverty levels. Also had to exclude unauthorized immigrants (might be included in census, but wouldn't be covered by Medicaid even if expanded).

[IRE link](http://ire.org/events-and-training/event/973/1139/)

## nicar14-notes/1-5.md

#The customized Census

### How to use microdata when you just can't find the right table


####Speakers:

* **[Robert Gebeloff][6764-001]**, *data journalism specialist, The New York Times*
* **[Katie Genadek][6764-002]**, *director of outreach and dissemination, IPUMS*


[6764-001]: https://twitter.com/gebeloffnyt
[6764-002]: http://usa.ipums.org/usa/cite.shtml

####Notes

Census microdata from [IPUMS](https://www.ipums.org/) gives you the full range of responses, some custom tables but there's also some data supression.

IPUMS is the Integrated Public Use Microdata Series.

It's standardized across years. Has documentation. And includes the American Community Survey from 2000-2012.

Example: How many Italian barbers are there?

You can find a total for the country. Then you can narrow it down to a particular state and gender.

But check out the confidence interval and raw numbers.

Another example: How many people might be affected by the ACA/Medicaid Gap in states that aren't expanding it.

Problem: Had to translate the census poverty levels to the Medicaid poverty levels. Also had to exclude unauthorized immigrants (might be included in census, but wouldn't be covered by Medicaid even if expanded).

**[Presentation exercise (PDF)](https://www.dropbox.com/s/wwmhsoj1qsqo3r7/Census.pdf)**

[Notes from Justin Myers](https://github.com/myersjustinc/nicar14-notes/blob/fa7dbe7b3d999a97c9a191fcf8ed9ff16f01f661/20140227_1400-the_customized_census.txt)

[IRE link](http://ire.org/events-and-training/event/973/1139/)

## nicar14-notes/1-6.md

#Make reporting better, together

###Collaborative reporting with GitHub


####Speakers:
* **[Ben Balter](https://twitter.com/BenBalter)**, *government evangelist, GitHub*

####Notes

Initial reporter's tool? Typewriter. Not collaborative. I produce, then send.

It's the same with email.

Open does not equal public. Open means open collaboration.

There's a continuum of stakeholders (not just developers), and all can/should be involved in creating the thing.

Follow the presentation. It's awesome.

**[Presentation Link](http://ben.balter.com/make-reporting-better-together/#/title)**

[IRE link](http://ire.org/events-and-training/event/973/1118/)

## nicar14-notes/2-1.md

#It's a disaster

###Datasets to have on hand for a disaster

####Speakers:

* **[Matt Jacob][4216-001]**, *reporter, The Dallas Morning News*
* **[Alex Richards][4216-002]**, *reporter, Chicago Tribune*

[4216-001]: https://twitter.com/matthewajacob
[4216-002]: https://twitter.com/alexrichards

####Notes

bit.ly/disaster2014

#####Bridges and dams

* National Bridge Inventory
* National Inventory of Dams
* Stanford's National Performance of Dams

#####Chemical Safety

* Tier 2 Reports — chemical inventories for companies, available through state agency
* No one aggregator of accidents
* The Dallas Morning News found that 90% of accident data is wrong

######Aircraft Info

* Registration Queries
* FAA/NTSB Safety Data
* FAA Service Difficulty Reports
* Wildlife Strike Database
* Flightaware

######Weather

* NWS (has shapefiles!)
* National Hurricane Center
* NCDC (extreme events)

#####Flooding

* FEMA Flood Maps & Hazard Data
* NWS Water Levels and forecasts

#####Earthquakes

* USGS has historical and real-time data

#####Prevention and cleanup

* Public Payrolls - Overtime Pay
* SBA disaster loans
* Charities established during/after disasters

[IRE link](http://www.ire.org/events-and-training/event/973/1235/)

## nicar14-notes/2-2.md

#Workflows for data projects

####Speakers:

* Moderator: **[Kevin Schaul][9910-001]**, *digital news developer, Star Tribune*
* **[Brian Boyer][9910-002]**, *visuals editor, NPR*
* **[John Perry][9910-003]**, *news apps team, Atlanta Journal-Constitution*
* **[Ben Welsh][9910-004]**, *developer and analyist, LA Times*


[9910-001]: https://twitter.com/kevinschaul
[9910-002]: https://twitter.com/brianboyer
[9910-003]: https://github.com/perryjg
[9910-004]: https://twitter.com/palewire

####Notes

**Stop doing stuff by hand. Automate it.**

Create a pipeline from start to finish.

Hack-novelist -> hack-analyst -> hack-developer

Brian Boyer's map script (on GitHub)

**use version control**

Can't automate all of it? Automate as much as possible and add the human part as a piece of the pipeline.

Can't automate **decisions**, can automate **processes**.

Use the power of email: update yourself on automated processes.

Django for data entry.

How to get editors to edit data? Scare them with it.

How to save the process? Open refine saves steps.

Project Manager vs. Editor vs. Programmer are three different hats.

**Always** work on a copy.

Fabric python app.

Keep your data all in one place.

Unit test when you are making a novel assertion.

Review process: **You** are responsible for the code you write.

[IRE link](http://www.ire.org/events-and-training/event/973/1151/)

## nicar14-notes/2-3.md

#Leaflet.js and Mapbox

####Speakers:

* **[Becca Aaronson](https://twitter.com/becca_aa)**, *developer and reporter, The Texas Tribune*

####Notes

Generate GeoJSON by joining shapefile to data in Qgis.

Import to tilemill & style it.

Add interactivity with mustaches.

[presentation link](http://j.mp/Oj7rRy)

[IRE link](http://www.ire.org/events-and-training/event/973/1096/)

## nicar14-notes/2-4.md

#How PANDA works

####Speakers:

* **[Brian Boyer][8508-001]**, *visuals editor, NPR*
* **[Christopher Groskopf][8508-002]**, *news apps developer, NPR*


[8508-001]: https://twitter.com/brianboyer
[8508-002]: https://twitter.com/onyxfish
####Notes

45k lines of javascript; 12k lines of python

How to support huge amounts of data with very small hardware requirements?

Solution: Search, not database.

#####Data Stack:

* PostgreSQL
* Solr

#####Web Stack

* Nginx
* usWGI
* python

Relational DB uses documents as objects, and documents have terms.

Inverted index uses terms as objects, and each has documents.

Solr thinks all the data is text, so it's very fast.

#####Ranking results

TF/IDF ranking (like google uses) is not what you want when searching structured data.

Can search on columns with dynamic columns.

Common name matching for aliases.

Some relational data: Metadata

How do you process >100MB uploads while maintaining a real-time UI? Asynchronous processing with celery.

How do you provide access for both people and machines? Program API first.

Even the GUI goes through the API using tastypie. It's an all JS client using Backbone.js — the least worst way.

**[Presentation slides](https://docs.google.com/presentation/d/1yLwVEfRFVbhJPL-yuAK6yVmdRzs8s5STiSiQBRPdcY4/pub?start=false&loop=false&delayms=3000&slide=id.p)**

[IRE link](http://www.ire.org/events-and-training/event/973/1123/)

## nicar14-notes/2-5.md

#Lightning Talks

##Refactor your code

####Speaker:

Christopher Groskopf

####Notes

Refactoring: Improving code quality without adding features.

What to fix:

1. Duplicated code
2. Long functions
3. Inconsistent style

---

##Favorite wee things

####Speaker:

Lena Groeger

####Notes
* Small multiples
* Tiny text
* tiny art
* baby steps
* mini maps
* tiny images

---

##Natural Language Processing in the kitchen

####Speaker:

Anthony Pesce

####Notes
Took a plaintext corpus and output recipes

---

##5 Algorithms in 5 minutes

####Speaker:

Chase Davis

####Notes
#####Vectorization
loops = slow; matrices = fast

#####Naive Bayes
Classifies stuff

#####Iterative algorithms
Change themselves

#####Vantage Point Trees
Fuzzy Search

#####Latent Dirichlet Allocation
Assigns topics to documents

---

##Bad data viz

####Speaker:

Katie Park

####Notes
Not everything needs to be a chart

Watch your scale

Know your data types

Doublecheck your info

Don't overdo it

---

##Calculus for Journalism

####Speaker:

Steven Rich

####Notes
Math = creative

Calculus = change

######Elk River Spill:
How much spilled?

Company and government gave estimates. Not inclined to trust them.

Can calculate an estimate of the rate of the leak.

---

##Detecting what isn't there

####Speaker:

Sisi Wei

####Notes
How do you know if you're being censored?

ProPublica did a series on "ghosting". Ghosting is the removal of data while keeping the user in the dark that it's been removed.

1. Collect everything. You can't know it disappeared if you didn't know it was there in the first place.

2. Deleted vs. censored. In ProPublica's case, there was a different error message when trying to access it.

---

##The whole internet in 5 minutes

####Speaker:

Jeremy Bowers

####Notes
Yep.

---

##How to raise an army

####Speaker:

Tyler Fisher

####Notes
Not code building, community building.

Create a self-guided digital literacy curriculum.

Have open lab hours.

Kill impostor syndrome.

---

##You Must Learn

####Speaker:

Ben Welsh

####Notes

Nothing we're doing is new.

No, seriously.

It's a wide world out there.

You've already been scooped by a computer.

It's about you *or* it's about the work.

[IRE link](http://www.ire.org/events-and-training/event/973/1147/)

## nicar14-notes/3-1.md

#Data in the sciences

####Speakers:

* Moderator: **[Sarah Cohen][5122-001]**, *editor, New York Times*
* **Carolyn Lauzon**, *biophysicist, AAAS Science and Technology Policy Fellowship*
* **Kathleen Ratcliff**, *AAAS Science & Technology Policy Fellowship*
* **Cynthia Hsu**, *AAAS Science & Technology Policy Fellowship*
* **[Beth M. Duckles][5122-002]**, *asst. prof. of sociology, Bucknell University and AAAS Science & Technology Policy Fellowship*


[5122-001]: https://twitter.com/sarahcnyt
[5122-002]: https://twitter.com/bduckles
####Notes

#####Finding bad data in medical images

Is the data good? Define good.

Input: Group of MRIs

Boxplots compare individual to aggregate.

#####Using math to explain nature

Step 0: Plot the data

Exponential vs. sigmoid growth

#####Quantifying and relating spatial patterns

Near things are more related than distant things.

All models are wrong, but some are useful.

Tool: SADIE

#####Working with Qualitative data

[IRE link](http://www.ire.org/events-and-training/event/973/1223/)

## nicar14-notes/3-2.md

#Presentation as a storytelling tool

####Speakers:

* Moderator: **[Chrys Wu][8390-001]**, Developer Advocate, The New York Times
* **[Alyson Hurt][8390-002]**, graphics editor, NPR
* **[Helene Sears][8390-003]**, senior editorial designer, BBC News Visual Journalism
* **[Aron Pilhofer][8390-004]**, editor of interactive news, The New York Times

[8390-001]: https://twitter.com/MacDiva
[8390-002]: https://twitter.com/alykat
[8390-003]: https://twitter.com/MateerS
[8390-004]: https://twitter.com/pilhofer

####Notes

**Snowfall-free zone**

What we're talking about is user-centric design.

#####Design process

1. Define — write a headline for the project *and display it*.
2. Brainstorm — no idea is bad
3. Wireframe/prototype — sanity check
4. Refine and perfect — start small and work up, not the other way around
5. Deliver

#####What's the story?

* Be a product development team
* Beware of feature creep
* Make choices

#####Planet Money T-Shirt

* User needs brainstorming
* Outline the process
* Have a visual styleguide
* Be a story architect
* Design a clear navigation path
* Prelaunch site (crowdsource enthusiasm)
* User test

**[Presentation slides](https://speakerdeck.com/macdiva/presentation-as-storytelling-tool-nicar14)**

[Notes from Stephen Suen](https://docs.google.com/document/d/1DNLjcdvlgjhGm9vtAna7jjPe_zg_js9dL7q4MbZFIeY/edit#)

[IRE link](http://www.ire.org/events-and-training/event/973/1145/)

## nicar14-notes/3-3.md

#Advanced Git

####Speakers:

* **[Jordan McCullough](https://twitter.com/thejordanmcc)**, _GitHub trainer_

####Notes

#####Creating a new Git repository

**git init** initializes a repository in your **pwd** (present working directory)

**git init [dir]** initializes a repository in a new subdirectory

**ls -a** will list everything in the pwd

**.git** is a directory. You can cd into it to see config files.

#####3-stage thinking

Working — staging — history

You work on files. You add them to staging. You commit to history.

**git log --oneline --stat** gives you a concise log

[Presentation slides](http://training.github.com/materials/slides/github-foundations.html#/)

[IRE link](http://ire.org/events-and-training/event/973/1102/)

## nicar14-notes/3-4.md

#You won't believe what static site generators can do for news apps

####Speakers:

* **[David Eads][6471-001]**, *news app developer, Chicago Tribune*
* **[Tyler Fisher][6471-002]**, *news apps intern, NPR Visuals Team*
* **[Brian Boyer][6471-003]**, *visuals editor, NPR*

[6471-001]: https://twitter.com/eads
[6471-002]: https://twitter.com/tylrfishr
[6471-003]: https://twitter.com/brianboyer

####Notes

NPR App Template

They use it for everything

It's customizeable

The guts:

* Flask app
* Fabric
* Jinja2
* Amazon S3
* Bootstrap

Starting a project:

* Clone the repo
* mkvirtualenv
* pip install requirements
* bootstrap (create files, push to remotes)
* create default GitHub issues & labels

Default app template has examples

Copy is handled through spreadsheets

**Fab update copy** command updates the copy

It's displayed through JINJA templates

One-touch deployment

* LESS and JST compiled
* Jinja baked to flat HTML
* CSS and JS minified and compressed into one file
* Everything gzipped
* pushed to S3

How to defeat caching? Timestamped files.

Also [Tarbell](http://blog.apps.chicagotribune.com/2013/06/07/meet-tarbell/).

[NPR App template slides](http://tylerjfisher.com/nicar-app-template/#/)

[IRE link](http://ire.org/events-and-training/event/973/1188/)

## nicar14-notes/3-5.md

#Cross-platform collaboration for data projects

####Speakers:

* **[Lorie Hearn][9297-001]**, *executive director & editor, inewsource*
* **Josh Kleinbaum**, *digital team senior managing editor, NBC's Owned Television Stations Group*
* **[John Walton][9297-002]**, *journalist, BBC Visual Journalism team*


[9297-001]: http://inewsource.org/
[9297-002]: https://twitter.com/walt_jw

####Notes

Map as story — example [Mello-Roos Tax](http://inewsource.org/mello-roos/)

Do a rolling investigation:

* get (and show) some data
* explain the data
* engage with the community
* repeat

Every platform requires different storytelling

Have to get buy-in from all your stakeholders

Desktop & mobile are different platforms

What do we have that no one else does? Dallas TV had extensive video archives of events surrounding Kennedy assassination.

What can we do that no one else can? Consider audience and platforms

They decided to do an app. Why? Heavy web search competition for the story, able to customize the app heavily.

Google maps don't work for historic stories: The street grid has changed.

[BBC Winter NHS project](http://www.bbc.com/news/health-25055444)

BBC's doing it on broadcast, online and social media

Reporter brought the idea to the viz team

They also created a bespoke [Facebook page](https://www.facebook.com/NHSWinter)

Lessons:

* Start in the same place
* Commit to the same goal
* What question are you answering?
* What resources will you commit?
* What do you do with the content?

[IRE link](http://ire.org/events-and-training/event/973/1240/)

## nicar14-notes/4-1.md

#Census I: Must-have data for every beat

####Speakers:

* **[Paul Overberg][1679-001]**, *database editor, USA Today*
* **Ronald Campbell**, *journalist*
* **[Mike Maciag][1679-003]**, *data editor, Governing Magazine*

[1679-001]: https://twitter.com/poverberg
[1679-003]: https://twitter.com/mmaciag

####Notes

#####20 stories in 20 minutes

1. Lopsided communities (lots of men/women/etc.)
2. Deaths v. births
3. 1940 census (It's public now)
4. ACS to look at congressional district demographics
5. Breaking news — mobile home fire (how many mobile homes are there here?)
6. Immigration
7. Internal Migration
8. "
9. Commuting
10. "
11. Housing
12. Health insurance
13. Family makeup changes
14. Source of heating (wood?)
15. Retrospectives
16. "
17. Internet access
18. Wage gap
19. Income & education
20. "

#####Census commuting data ([link](https://www.dropbox.com/s/283mpw3jrxooyql/census-commuting-tipsheet.pdf))

* Choose a topic (census subject definitions file, ACS subjects page link, American FactFinder search)
* Choose a geography (place, county, ZIP code, etc.)
* Choose an ACS dataset 1-, 3-, 5-year periods (1 year is more current but less precise)

Hazards:

* Check out the subject definitions file. It might not mean what you think it means.
* Check out the universe. It might not be counting who you think it's counting.

#####Must-have data ([link](https://www.dropbox.com/s/4f01to0ogor1czi/CensusI_Overberg.pdf))

**County Population Data**

* Released mid-March
* Totals since 2010
* Basic trend stories
* Think Metro areas
* Gets revised each year

**City-town estimates**

* Mid-may
* Totals since 2010, every town
* Back-revised
* Connect it to 2000-2010 estimates for longer-term stories

**County Business Patterns**

* May
* Tally of workers, payroll, number of establishments
* Breakdown of industry
* Every county, every year

**County age-race-sex-Hisp estimates**

* June
* Trends among minorities
* Diversity
* Age-race ratios

**American Community Survey**

* 3 waves: Sept., Nov., Dec.
* Data from previous year (or 3 or 5)
* Use as a peg, don't report on the release
* Use a comparison profile for quick-look

[IRE link](http://www.ire.org/events-and-training/event/973/1113/)

## nicar14-notes/4-2.md

#Census I: Must-have data for every beat

####Speakers:

* **[Joe Kokenge][3024-001]**, *data editor, San Antonio Express News*
* **[Abraham Epton][3024-002]**, *developer, Chicago Tribune News Apps Team*
* **[Brian Abelson][3024-003]**, *data scientist, Enigma*

[3024-001]: https://twitter.com/josephkokenge
[3024-002]: https://twitter.com/aepton
[3024-003]: https://twitter.com/brianabelson

####Notes

Basic bots

[ILCampaignCash](https://twitter.com/ILCampaignCash)

Private Twitterbot as newsroom tool

[IRE link](http://ire.org/events-and-training/event/973/1110/)

## nicar14-notes/4-3.md

#Census III: Mapping and presentation

####Speakers:

* **[John Keefe][1824-001]**, *senior editor, WNYC Data News Team*
* **[Chris Amico][1824-002]**, *journalist and co-founder, Homicide Watch and Learning Lab*


[1824-001]: https://twitter.com/jkeefe
[1824-002]: https://twitter.com/eyeseast

####Notes

Use Census Reporter to explore

FusionTables for quick mapping

CartoDB can convert to KML

Subtract water by adding water layer and merge the shapefiles, then take the difference

Checkout Mbostock's TopoJson stuff

Use Leaflet for the data layer, Mapbox for the base layer

[Notes](https://gist.github.com/eyeseast/655cd641d7871e69f24d)

[Water begone](http://johnkeefe.net/water-begone)

[IRE link](http://ire.org/events-and-training/event/973/1115/)

## nicar14-notes/README.md

nicar14-notes
=============

Notes from the sessions I'm attending at NICAR 14

#Nicar 2014
**February 27 - March 1, 2014**
**Baltimore, MD**

###27 February 2014
* [Conference welcome and overview](/1-1.md)
* [Rifling through the mapping toolbox](/1-2.md)
* [Enhance your stories with statistics](/1-3.md)
* [Love your life, retire your servers](/1-4.md)
* [The customized Census: How to use microdata when you just can't find the right table](/1-5.md)
* [Make reporting better, together — Collaborative reporting with GitHub](/1-6.md)

###28 February 2014
* [It's a disaster](/2-1.md)
* [Proper workflows for data projects](/2-2.md)
* [Building maps with leaflet and mapbox.js](/2-3.md)
* [How PANDA works: Software architecture for big data](/2-4.md)
* [Lightning Talks](/2-5.md)

###1 March 2014
* [A quick trip through data in the sciences](/3-1.md)
* [It's not just for looks: Presentation as a storytelling tool](/3-2.md)
* [Advanced GitHubbing and Git Internals](/3-3.md)
* [You won't believe what static site generators can do for news apps](/3-4.md)
* [Cross-platform collaboration for data projects](/3-5.md)

###2 March 2014
* [Census I: Must-have data for every beat](/4-1.md)
* [Build your bot army](/4-2.md)
* [Census III: Mapping and Presentation](/4-3.md)

#####Other Resources:
[Chrys Wu's huge list of NICAR stuff](http://blog.chryswu.com/2014/02/21/nicar14-slides-tutorials-links-tools/)
