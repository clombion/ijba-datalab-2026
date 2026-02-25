<!-- chunk: 1/4 | source: 97e-nicar-2020.md | words: 32650 -->
<!-- headings: NICAR 2020 Tipsheets & Session Notes; 2020-advanced-dj-browser.md; 2020-advanced-sql.md; 2020-ap-datakit.md; AP DataKit; Page: /; Basic, adaptable project; Create projects as quickly; Simple, adaptable project structure; Integrate with cloud storage; Quickstart installation guide; 1. Install datakit-project; 2. Grab a template; 3. Get to work; 4. Adapt to your workflow; Community Contributions; Better collaborations, less mess; Annual Report for Calendar 2018; Owner Ticker; Owner Ticker -->

# NICAR 2020 Tipsheets & Session Notes




## 2020-advanced-dj-browser.md

Advanced data journalism through a browser
Alex Richards, Syracuse University
#NICAR20

Follow along:    bit.ly/n20-browser

The problem(s)
An IT department that won’t let you
Install problems when leading a class or workshops
Computer labs that won’t let you
Parachuting in
Trying to share data exploration and analysis with journalism colleagues who don’t have the same environment
Other reporters
Your editor
Outside sources

Now you know where to start if you’re interested in Python, R or JavaScript
These online tools and services can get you past initial hurdles


Notebooks in the cloud
What are notebooks?

Google Colaboratory
colab.research.google.com
What is it?
Platform that “allows anybody to write and execute arbitrary python code through the browser.”
Cost?
Free, but offers a $10/mo “pro” tier for additional computing resources.
“Colab” is in the name, so can I collaborate with others?
Share a notebook like any Google Drive document, but don’t count on real-time editing — users report delays.
Which languages can I use?
Officially, Python 2/3. Unofficially, it supports R, but it requires a workaround.
How long will a notebook run?
Up to 12 hours with a 60-minute inactivity timeout. (Pro tier = 24 hours.)


Google Colaboratory
Example:
Colab notebook (Python) looking at Stanford Open Policing data-
bit.ly/n20-py-colab
Quick R example-
bit.ly/n20-r-colab
Other points of interest:
Can turn a notebook hosted on GitHub into a live, interactive version (just point it there from the main Colab page)
TRY: https://github.com/varner/nicar2020-nlp-workshop

Binder
mybinder.org
What is it?
Turn a GitHub repo into a live, interactive experience by running notebooks or RStudio through a browser.
Cost?
Free.
Can I collaborate with others?
It draws everything from GitHub, so you can through pull requests, etc.

Which languages can I use?
Python and R (via Jupyter); RStudio (How that all works here)
Downsides?
Finickier than the others because of limited computing resources. Slow to start up. Will only let you idle for about 10 min.
Upsides?
No logins, no accounts for potential users. Just point them at a URL. When it works, it works.

Binder
Example:
Texas death row scraper:
bit.ly/syr_scrape
The original repo:
https://github.com/richardsalex/live-notebook-example

Microsoft Azure Notebooks
notebooks.azure.com
What is it?
A “service for anyone to develop and run code in their browser using Jupyter.”
Cost?
Free (for now?)
Can I collaborate with others?
Others can clone a public “project,” and mess with their own copy.
Which languages can I use?
Python, R

How long will a notebook run?
Eight-hour run time (possibly longer), 60-min. timeout.
Downsides?
Works off of older versions of some libraries, like seaborn.
May delete large data files after 60 days of inactivity!
You can view notebooks without logging in — like Colab, you’ll need an account for anything interactive.

Microsoft Azure Notebooks
Example:
An Azure Notebooks project with Python and R notebooks:
bit.ly/n20-azure


Kaggle
www.kaggle.com
What is it?
Data science, gamified. A byproduct of people competing to solve problems: working code notebooks in the cloud.
Cost?
Free.
Can I collaborate with others?
Others can clone/fork public projects; you can also add direct collaborators.
Which languages can I use?
Python, R (RMarkdown)
How long will a notebook run?
Nine hours; 60-minute inactivity timeout.
Anything interesting?
You can store a lot of data with Kaggle. Not only do a bunch of public, user-added data sets exist, you can upload 20GB files.
Also integrates easily with BigQuery and Google Cloud Storage.


Kaggle
Example:
Kaggle Python notebook
bit.ly/n20-kaggle


Others (not exhaustive)
https://cocalc.com/
https://datalore.io/

Wait — where can I learn more?
Python
“First Python notebook: Data analysis on deadline”
Friday, 9 a.m. – 5:45 p.m. (all day) • Studio 6, 2nd floor (pre-reg, fee)
“Python 1: The fundamentals (repeat)”
Sunday, 9 – 10 a.m. (1 hour) • Studio 6, 2nd floor
^ follow by more advanced sessions


R and RStudio
“Exploring the tidyverse in R”
Saturday, 9 a.m. – 5:45 p.m. (all day) • Studio 7, 2nd floor (pre-reg, fee)
“R 1: Intro to R and RStudio (repeat)”
Saturday, 2:15 – 3:15 p.m. (1 hour) • Studio 2, 2nd floor
^ followed by more advanced sessions


Specifically R

RStudio Cloud
What is it?
A cloud-based RStudio instance where you can create different workspaces and conduct different analyses.
Cost?
Free. (Still a product in beta.)
Can I collaborate with others?
Like Azure, others can clone a public project and work with their own copy. BUT: multiple accounts can participate in a workspace with different roles and modify a project together.
Limits?
— 1Gb memory, single CPU core
– One private space (ideal for a class or news projects, say) with a max of 10 users; you can request more resources based on need.
Downsides?
Like others, can suffer from significant performance issues.
Example:
bit.ly/syr_r


Bonus: JavaScript

Observable
observablehq.com
What is it?
JS-based data viz canvas. Differences = other “cells” update in real time as changes are made; you can pull things in from other Observable notebooks.
Cost?
Free. ($9/mo./person for “teams” — like Slack’s pricing model.)

Can I collaborate?
Fork/merge process similar to GH; you can comment on other notebooks. Paid teams gives real-time collaboration.
Which languages can I use?
JavaScript (with some modifications).
No login required to mess around.
Example:
Interactive NOPD police zones map
http://bit.ly/n20-leaflet


Observable
Where can I learn more?
“First Observable notebook: Prototyping with polish”
Thursday, 2:15 – 5:45 p.m. (3.5 hours) • Studio 3, 2nd floor
(pre-reg, fee)
The 2020 version of the class
bit.ly/n20-observable


Glitch
glitch.com
What is it?
Collaborative Node.js coding platform — projects/applications work live on the site.
Cost?
Free (premium features planned).
Can I collaborate?
You can invite others to work with you and to directly edit your project.

Which languages can I use?
JavaScript / Node.js environment.
Limits?
4,000 requests/hr.; projects sleep after five minutes of inactivity and can’t run for more than 12 hours; size and memory ceiling.
Example:
Congress Tracker by Jason Crane (using ProPublica’s Congress API)

https://glitch.com/~congress-tracker-example

Glitch
Where can I learn more?
Not specifically about Glitch, but the underlying tech:
“First graphics app: Node.js in the newsroom”
Saturday, 9 a.m. – 5:45 p.m. (all day) • Studio 3, 2nd floor
(Pre-reg, fee)


Double-bonus: Your own server!

The Littlest JupyterHub
tljh.jupyter.org
What is it?
A way to provide roughly 50-100 users with the same coding environment. Made for folks who are not network admins.
Out in the cloud, you’re running a single VM/container — little muss, little fuss.
How is this different than the other examples?
You’re in control: you specify how users log in, what data they have access to, what resources are available to them. You can set this up on services like Digital Ocean, AWS and others.

RStudio Server on AWS
What is it?
“[A] browser-based interface to a version of R running on a remote Linux server.” Users can access their own workspaces and share server-side computing resources.
Why might I want to do this?
All the reasons we’ve discussed + if you want to make a Shiny app or create an API that serves data over the web.
How?
RStudio Server has a free version. OR...

Pre-built Amazon Machine Images:
http://www.louisaslett.com/RStudio_AMI/
^ make it so you don’t have to interact with the command line at all.
Example:
(Using a cloud-based Shiny Server + RStudio)
Sharon Machlis’ NICAR tweet tracker-
apps.machlis.com/shiny/nicar20/


Questions?

Thanks!
richards.alex@gmail.com
@alexrichards
DECK: bit.ly/n20-browser

(Credit to DataSchool.io for exposing me to a couple of options I hadn’t known about before)


## 2020-advanced-sql.md

Advanced SQL
Date handling, subqueries and more

Link to these slides
http://bit.ly/nicarsql4


Getting started
Open DB Browser for SQLite, if it’s not open already, and open the osha.sqlite file


Dates in SQLite
SQLite stores dates as text, unlike some other relational databases. To treat them as dates, use the date() function.


SELECT MIN(DATE(open_date)), MAX(DATE(open_date))
FROM inspections


Extracting date parts
To extract parts of the date -- year, month, day, etc. -- use the strftime() function.

To select the year ('%Y'):

SELECT strftime('%Y', open_date)
FROM inspections

 


Extracting date parts 
To select the month ('%m'):

SELECT strftime('%m', open_date)
FROM inspections

To get the day, you’d specify '%d' -- see the full list of directives here.


 


Quick date format check
The strftime function will return NULL if you attempt to parse an invalid date.
You can use it to run some limited integrity checks on columns with date values.

SELECT *, strftime('%Y', open_date) AS date_test
FROM inspections
WHERE date_test IS NULL


 


Quick date format check
The strftime function will return NULL if you attempt to parse an invalid date.
You can use it to run some limited integrity checks on columns with date values.

SELECT *, strftime('%Y', open_date) AS date_test
FROM inspections
WHERE date_test IS NULL


 


Using date parts in a query
Another trick with strftime: Extracting part of a date on the fly and using the resulting value elsewhere in your query. For instance, if you wanted to group inspections by year:

SELECT strftime('%Y', open_date) AS 'Year', COUNT(*)
FROM inspections
GROUP BY 1
ORDER BY 2 DESC


 


Exercise in small groups

Practice grabbing pieces of the date from the close_date column and grouping by year.


 


Exercise in small groups

Practice grabbing pieces of the date from the close_date column and grouping by year.


 


Finding the difference between dates

Use the function Julianday() to convert the date string into the number of the day according to the Julian calendar (the number of days since noon in Greenwich on November 24, 4714 B.C.). 

Once the dates are converted to numbers, you can simply subtract them:

SELECT julianday(close_case_date) - julianday(open_date)
    AS days_open
FROM inspections
ORDER BY 1 desc


 


Converting Julian date values to years
To convert the Julian date difference to years (roughly),  simply divide the number by 365.25:

SELECT (julianday(close_case_date) - julianday(open_date)) / 365.25
    AS years_open
FROM inspections
ORDER BY 1 desc


 


Subqueries
A subquery is simply a full SQL query that is nested inside another query. We’ll go through a few examples of when nested queries can come in handy. First, a few general tips: 

When writing nested queries, it’s helpful to write the inner query (subquery) first, then build the outer query on top of that.
You must give the inner query a name using AS and set it off using parentheses.
Use tabs to set off lines of your query so that you can easily read them.


 


Use a subquery to count distinct field values
Write a subquery selecting all the DISTINCT records, and then query those results with a COUNT(*):


SELECT COUNT(*)
FROM (SELECT DISTINCT * FROM inspections) AS temp
 


Include the distinct count in a query
Create a new column that has a count of how many times each establishment appears in the table:

SELECT a.*, b.estab_count
FROM inspections AS a
INNER JOIN (SELECT estab_name, COUNT(*) AS estab_count
            FROM inspections
            GROUP BY 1) AS b
ON a.estab_name = b.estab_name



## 2020-ap-datakit.md

# AP DataKit
_Source: https://datakit.ap.org_


============================================================

## Page: /

- 
    
- 
    

    AP DataKit - Home
  
  
    
    
  
    AP DATAKIT
    
# Basic, adaptable project

      organization

    
    
    AP DataKit is an open-source command-line tool designed to better structure and manage projects. It makes it easier to standardize and share work among members of your team, and to keep your past projects organized and easily accessible for future reference.
      

      

      AP DataKit works off a basic framework that includes the core product and a few key plugins to help you manage where your data files and code are stored and updated.
  

  
    
      
        


## Create projects as quickly
as news breaks

        Using [Cookiecutter](https://github.com/audreyr/cookiecutter) templates, projects can be spun up quickly whenever needed.
      
      
        terminal
        
          
- datakit project create
          Creating project from template: /Users/lfenn/.cookiecutters/cookiecutter-r-project

          full_name [Larry Fenn]:

          email [lfenn@ap.org]:

          project_name [New Project]: Hudson Helicopter Crash

          project_slug [hudson-helicopter-crash]

          project_short_description [TK: short project description]: Pull FAA data on helicopter crashes
          
-  cd hudson-helicopter-crash
        
      
    
  

  
    
      
        

## Simple, adaptable project structure

        Keep all parts of a project cleanly separated: data, code, configuration, documentation.
      
       
        terminal
        
          ├── README.md

          ├── analysis

          │   ├── analysis.R

          │   ├── graphs.Rmd

          │   └── story_lines.R

          ├── config

          │   └── datakit-data.json

          ├── data

          │   ├── manual

          │   ├── processed

          │   └── source

          ├── docs

          ├── output

          │   └── totals_over_time.csv

          └── trump-counties-employment.Rproj
        
      
    
  

  
    
      
        


## Integrate with cloud storage
and hosting

        Automate data and code syncing to take the guesswork out of storage and backup.
      
       
        terminal
        
          
- datakit data push
          EXECUTING: aws s3 sync --profile default data/ s3://data.ap.org/projects/2019/trump-counties-employment/data/

          upload: data/manual/trumpjobs.sqlite to s3://data.ap.org/projects/2019/trump-counties-employment/data/manual/trumpjobs.sqlite

          upload: data/reports/graphs.html to s3://data.ap.org/projects/2019/trump-counties-employment/data/reports/graphs.html

          upload: data/source/LAUS/laucnty15.xlsx to s3://data.ap.org/projects/2019/trump-counties-employment/data/source/LAUS/laucnty15.xlsx

          upload: data/source/LAUS/laucnty16.xlsx to s3://data.ap.org/projects/2019/trump-counties-employment/data/source/LAUS/laucnty16.xlsx

          upload: data/source/LAUS/laucnty17.xlsx to s3://data.ap.org/projects/2019/trump-counties-employment/data/source/LAUS/laucnty17.xlsx

          upload: data/source/LAUS/laucnty18.xlsx to s3://data.ap.org/projects/2019/trump-counties-employment/data/source/LAUS/laucnty18.xlsx
        
      
    
  
  
  
    
# Quickstart installation guide

    For Python 3. If you do not have Python 3 installed on your machine, [get the latest version here](https://www.python.org/downloads/).
    More detailed installation documents are available [here](https://datakit-project.readthedocs.io/).
  
  

  

  
  
  
    
      
        

## 1. Install datakit-project

        This is our most popular plugin and sets you up nicely to use other plugins in the future if you want.
      
      
        terminal
        
          
- pip install datakit-project
        
      
    
  

  
  

  
    
      
        


## 2. Grab a template

        DataKit uses [Cookiecutter](https://github.com/cookiecutter/cookiecutter) templates for project structure and initial configuration.
        The following templates are available:
        
          
- [Python project template](https://github.com/associatedpress/cookiecutter-python-project): This is a Jupyter-specific cookiecutter which uses `pipenv`.
          
- [R project template](https://github.com/associatedpress/cookiecutter-r-project): This is a R project cookiecutter which uses an RStudio `.Rproj` file.
          
- [Generic template](https://github.com/associatedpress/cookiecutter-generic-project): This is a basic cookiecutter which defines only the folder structure, a project `README`, and a `.gitignore` file. If your project workflow isn't covered by the Python or R project templates, or you want to develop your own project template, this is the place to start.
        
      
      
        terminal
        
          
- datakit project create -t https://github.com/associatedpress/cookiecutter-r-project.git
        
      
    
  

  
  

  
    
      
        

## 3. Get to work

        On the command line, `datakit project create` will create a project with a standardized file structure.
      
      
        terminal
        
          
- datakit project create
        
      
    
  

  
  

  
    
      
        


## 4. Adapt to your workflow

        Additional plugins can help you manage the storage of flat data files, sync your code to GitLab or GitHub and push your output to data.world for sharing. Grab other plugins or develop your own!
      
      
        
          
- Data storage and backup: Amazon S3 sync - [datakit-data](https://datakit-data.readthedocs.io/en/latest/)
          
- Version control:
              
                
- GitHub integration - [datakit-github](https://github.com/associatedpress/datakit-github/)
                
- GitLab integration - [datakit-gitlab](https://github.com/associatedpress/datakit-gitlab/)
              
          
- Publishing shareable output: Data.world - [datakit-dworld](https://github.com/associatedpress/datakit-dworld/)
        
      
    
  

  
  

  
    
      
        

## Community Contributions

        Useful DataKit plugins from around the community:
      
      
        
          
- Data storage and backup:
            
              
- Google Drive - [datakit-data-gdrive](https://bitbucket.org/quickhand/datakit-data-gdrive/src/master/)
            
          
- Version control:
            
              
- Bitbucket - [datakit-data-bitbucket](https://bitbucket.org/quickhand/datakit-bitbucket/src/master/)
            
        
      
    
  

  

  
    


## Better collaborations, less mess

    Questions? Comments? Drop us a line at [datateam@ap.org](mailto:datateam@ap.org?Subject=DataKit)
    

    More information on the [AP's data journalism program](https://www.ap.org/en-us/formats/data-journalism)


## Annual Report for Calendar 2018

The Honorable A. Mitchell McConnell Jr. (McConnell, A. Mitchell Jr.)

- Filed 05/15/2019 @ 10.03 AM


The following statements were checked before filing:


I certify that the statements I have made on this form are true, complete and correct to the best of my

knowledge and belief.
I understand that reports cannot be edited once filed. To make corrections, I will submit an _electronic_
amendment to this report.


I _omitted_ assets because they meet the three-part test for exemption.


Part 1. Honoraria Payments or Payments to Charity in Lieu of Honoraria

Did any individual or organization pay you or your spouse more than $200 or donate any amount to a
charity on your behalf, for an article, speech, or appearance? No


Part 2. Earned and Non-Investment Income

Did you or your spouse have reportable earned income or non-investment income? Yes


#


Who
Was
Paid Type Who Paid Amount Paid


1 Self Other
(Required Minimum
Distribution)


2 Spouse Other
(Pay-out of Deferred
Compensation Deferred Stock Units
Vesting)

3 Spouse Other
(Pay-out of Deferred
Compensation Deferred Stock Units
Vesting)


Part 3. Assets


Mitch IRA
MLPA
Louisville,
Kentucky

Wells Fargo &
Company
San
Francisco,
CA

Vulcan
Materials
Birmingham,
AL


$8,480.00


- $1,000


- $1,000


Did you, your spouse, or dependent child own any asset worth more than $1000, have a deposit
account with a balance over $5,000, or receive income of more than $200 from an asset? Yes


Asset Asset Type Owner Value Income Type Income


1 Republic Bank and
Trust
(Louisville, KY)
_Type:_ Checking,

2 MNNAX - Victory
Munder Multi-Cap A


3 VHCAX-Vanguard
Capital Opportunity
Adm (NASDAQ)

4 VSIAX-Vanguard Small
Cap Value Index
Admiral (NASDAQ)

5 VFIAX-Vanguard 500
Index Admiral
(NASDAQ)

6 A. Mitchell McConnell,
Jr. Revocable Trust

6.1 Merrill Lynch
(Louisville, KY)
_Type:_ Money Market
Account,


Bank Deposit Self $15,001 $50,000


Interest, None (or
less than
$201)


Trust
General Trust


Trust
General Trust


Trust
General Trust


Trust
General Trust


Trust
General Trust


Self $15,001 $50,000


Self $250,001 $500,000


Self $250,001 $500,000


Self $250,001 $500,000


Self


Excepted
Investment
Fund,


Excepted
Investment
Fund,


Excepted
Investment
Fund,


Excepted
Investment
Fund,


$5,001 $15,000


$15,001 $50,000


$5,001 $15,000


$5,001 $15,000


Bank Deposit Self $15,001 $50,000


Dividends, $201 $1,000


Interest, None (or
less than
$201)


7 Mitch IRA MLPA Retirement
Plans
IRA


Self


7.1 Bank of America
(Louisville, Kentucky)
_Type:_ IRA Cash Accounts,

7.2 SCPB-SPDR Barclays
Short Term Corp Bd ETF
(NYSEArca)


7.3 VCSH - Vanguard
Short-Term Corporate
Bond ETF (NASDAQ)


7.4 IWM-iShares Russell


7.5 SPY - SPDR S&P 500
ETF


7.6 VO-Vanguard Mid-Cap
ETF


8 Vanguard 529 College
Savings Plan
_Institution:_ Vanguard


Mutual Funds
Exchange
Traded
Fund/Note

Mutual Funds
Exchange
Traded
Fund/Note

Mutual Funds
Exchange
Traded
Fund/Note

Mutual Funds
Exchange
Traded
Fund/Note

Mutual Funds
Exchange
Traded
Fund/Note

Education
Savings Plans
529 College
Savings Plan


Bank Deposit Self $1,001 $15,000


Self $15,001 $50,000


Self $15,001 $50,000


Self $15,001 $50,000


Self $50,001 $100,000


Self $15,001 $50,000


Self


Excepted
Investment
Fund,


Excepted
Investment
Fund,


Excepted
Investment
Fund,


Excepted
Investment
Fund,


Excepted
Investment
Fund,


None (or
less than
$201)


None (or
less than
$201)


None (or
less than
$201)


None (or
less than
$201)


None (or
less than
$201)


Asset Asset Type Owner Value Income Type Income


8.1 Vanguard Aggressive
Growth Portfolio (Age
Based)

9 Vanguard 529 College
Savings Plan
_Institution:_ Vanguard


9.1 Vanguard Aggressive
Growth Portfolio (Age
Based)

10 VMMXX-Vanguard
Money Market Reserves
(NASDAQ)

11 VMSXX - Vanguard
Municipal Money
Market Fund

12 VFIAX-Vanguard 500
Index Admiral
(NASDAQ)

13 Real Property with
Carriage House Rental
_Description:_ Real
Property with Carriage
House Rental
(Washington, DC)

14 UBS Pension Trust (9
items)

14.1 UBS (uninvested cash
held by UBS)
(Washington, DC)
_Type:_ Checking,

14.2 WGIFX-American Funds
Capital World Gr&Inc F2
(NASDAQ)

14.3 SDSCX-Dreyfus/The
Boston Co Sm/Md Cp Gr
I (NASDAQ)

14.4 FEGIX-First Eagle Gold I
(NASDAQ)


14.5 PEQPX-Principal Equity
Income P (NASDAQ)


14.6 GFFFX-American Funds
Growth Fund of Amer
F2 (NASDAQ)

14.7 DPFFX-Delaware
Diversified Income Instl
(NASDAQ)


Mutual Funds
Mutual Fund


Education
Savings Plans
529 College
Savings Plan

Mutual Funds
Mutual Fund


Mutual Funds
Mutual Fund


Mutual Funds
Mutual Fund


Mutual Funds
Mutual Fund


Real Estate
Residential


Trust
General Trust


Self $50,001 $100,000


Self


Self $50,001 $100,000


Joint None (or
less than
$1,001)


Joint $1,000,001 $5,000,000


Joint $5,000,001 $25,000,000


Joint $1,000,001 $5,000,000


Spouse


None, None (or
less than
$201)


None, None (or
less than
$201)


Rent/Royalties, $15,001 $50,000


Interest, None (or
less than
$201)


Excepted
Investment
Fund,


Excepted
Investment
Fund,


Excepted
Investment
Fund,


None (or
less than
$201)


$15,001 $50,000


$100,001 $1,000,000


Bank Deposit Spouse None (or
less than
$1,001)


Mutual Funds
Mutual Fund


Mutual Funds
Mutual Fund


Mutual Funds
Mutual Fund


Mutual Funds
Mutual Fund


Mutual Funds
Mutual Fund


Mutual Funds
Mutual Fund


Spouse $15,001 $50,000


Spouse $1,001 $15,000


Spouse $1,001 $15,000


Spouse $15,001 $50,000


Spouse $15,001 $50,000


Spouse $15,001 $50,000


Excepted
Investment
Fund,


Excepted
Investment
Fund,


Excepted
Investment
Fund,


Excepted
Investment
Fund,


Excepted
Investment
Fund,


Excepted
Investment
Fund,


None (or
less than
$201)


None (or
less than
$201)


None (or
less than
$201)


None (or
less than
$201)


None (or
less than
$201)


None (or
less than
$201)


Asset Asset Type Owner Value Income Type Income


14.8 TGBAX-Templeton
Global Bond Adv
(NASDAQ)

14.9 PGDPX - Principal
Global Div Inc P
(NASDAQ)

15 (Heritage Foundation
403(b)) SWGXX Schwab Government
Money Fund 
16 (Heritage Foundation
403(b)) VFIAXVanguard 500 Index
Admiral

17 (Heritage Foundation
403(b)) PREIX-T. Rowe
Price Equity Index 500
(NASDAQ)
_Filer comment:_ Previously
only noted as
"Retirement;" but also
part of "Heritage
Foundation 403(b)."

18 (Heritage Foundation
Retirement) SWGXX Schwab Government
Money Fund

19 (Heritage Foundation
Retirement) ARTKXArtisan International
Value Investor

20 (Heritage Foundation
Retirement) BARAXBaron Asset Retail

21 (Heritage Foundation
Retirement) FAIRXFairholme

22 (Heritage Foundation
Retirement) LSBDXLoomis Sayles Bond
Instl

23 (Heritage Foundation
Retirement) OAKMXOakmark I

24 (Heritage Foundation
Retirement) RSEIXRoyce Special Equity
Instl

25 (Heritage Foundation
Retirement) SLASXSelected American
Shares S


Mutual Funds
Mutual Fund


Mutual Funds
Mutual Fund


Mutual Funds
Mutual Fund


Mutual Funds
Mutual Fund


Mutual Funds
Mutual Fund


Mutual Funds
Mutual Fund


Mutual Funds
Mutual Fund


Mutual Funds
Mutual Fund


Mutual Funds
Mutual Fund


Mutual Funds
Mutual Fund


Mutual Funds
Mutual Fund


Mutual Funds
Mutual Fund


Mutual Funds
Mutual Fund


Spouse $1,001 $15,000


Spouse $1,001 $15,000


Spouse $100,001 $250,000


Spouse $15,001 $50,000


Spouse $100,001 $250,000


Spouse None (or
less than
$1,001)


Spouse $1,001 $15,000


Spouse $1,001 $15,000


Spouse $15,001 $50,000


Spouse $1,001 $15,000


Spouse $15,001 $50,000


Spouse $1,001 $15,000


Spouse $15,001 $50,000


Excepted
Investment
Fund,


Excepted
Investment
Fund,


Excepted
Investment
Fund,


Excepted
Investment
Fund,


Excepted
Investment
Fund,


Excepted
Investment
Fund,


Excepted
Investment
Fund,


Excepted
Investment
Fund,


Excepted
Investment
Fund,


Excepted
Investment
Fund,


Excepted
Investment
Fund,


Excepted
Investment
Fund,


Excepted
Investment
Fund,


None (or
less than
$201)


None (or
less than
$201)


None (or
less than
$201)


None (or
less than
$201)


None (or
less than
$201)


None (or
less than
$201)


None (or
less than
$201)


None (or
less than
$201)


None (or
less than
$201)


None (or
less than
$201)


None (or
less than
$201)


None (or
less than
$201)


None (or
less than
$201)


Asset Asset Type Owner Value Income Type Income


26 (Heritage Foundation
Retirement) PRMSX-T.
Rowe Price Emerging
Markets Stock

27 (Heritage Foundation
Retirement) VGSLXVanguard REIT Index
Adm

28 (Heritage Foundation
Retirement) WIIBX Segall Bryant & Hamill
Plus Bond Fund
Institutional
_Filer comment:_ Security
name change in 2018;
formerly "(Heritage
Foundation Retirement)
WIIBX-Westcore Plus
Bond Institutional"

29 (Retirement) Deutsch
VSI Capital Growth Mutual of America
_Filer comment:_ Tax
Deferred Annuity

30 SunTrust Solid Choice
Banking
(Washington, DC)
_Type:_ Checking,

31 SunTrust Advantage
Money Market Account
(Washington, DC)
_Type:_ Money Market
Account,

32 Suntrust Business
Checking (Firebird
International LLC)
(Washington, DC)
_Type:_ Checking,
_Filer comment:_ Firebird
International LLC is a
single member LLC and
this entity does not have
any value other than the
cumulative value of its
individual assets.


Mutual Funds
Mutual Fund


Mutual Funds
Mutual Fund


Mutual Funds
Mutual Fund


Mutual Funds
Mutual Fund


Spouse $1,001 $15,000


Spouse $1,001 $15,000


Spouse $1,001 $15,000


Spouse $100,001 $250,000


Excepted
Investment
Fund,


Excepted
Investment
Fund,


Excepted
Investment
Fund,


Excepted
Investment
Fund,


None (or
less than
$201)


None (or
less than
$201)


None (or
less than
$201)


None (or
less than
$201)


Bank Deposit Spouse $1,001 $15,000


Bank Deposit Joint $250,001 $500,000


Bank Deposit Spouse $250,001 $500,000


Interest, None (or
less than
$201)


Interest, $201 $1,000


None, None (or
less than
$201)


Asset Asset Type Owner Value Income Type Income


33 Suntrust Business
Money Market
Performance (Firebird
International LLC)
(Washington, DC)
_Type:_ Money Market
Account,
_Filer comment:_ Firebird
International LLC is a
single member LLC and

this entity does not have
any value other than the
cumulative value of its
individual assets.

34 Suntrust Personal
Savings Account
(Washington, DC)
_Type:_ Savings,


Bank Deposit Spouse $50,001 $100,000


Bank Deposit Spouse $1,001 $15,000


Interest, $201 $1,000


Interest, None (or
less than
$201)


35 UBS IRA (7 items) Retirement
Plans
IRA


Excepted
Investment
Fund,


Excepted
Investment
Fund,


Excepted
Investment
Fund,


Excepted
Investment
Fund,


Excepted
Investment
Fund,


Excepted
Investment
Fund,


Excepted
Investment
Fund,


35.1 WGIFX-American Funds
Capital World Gr&Inc F2
(NASDAQ)

35.2 FEGIX-First Eagle Gold I
(NASDAQ)


35.3 PEQPX-Principal Equity
Income P (NASDAQ)


35.4 RSPYX-RS Partners Y
(NASDAQ)


35.5 GFFFX-American Funds
Growth Fund of Amer
F2 (NASDAQ)

35.6 DPFFX-Delaware
Diversified Income Instl
(NASDAQ)

35.7 TGBAX-Templeton
Global Bond Adv
(NASDAQ)

36 Scottrade
(Washington, DC)
_Type:_ Brokerage Sweep
Account, Checking,

37 TRBCX-T. Rowe Price
Blue Chip Growth
(NASDAQ)

38 PRITX-T. Rowe Price
International Stock Fd
(NASDAQ)


Mutual Funds
Mutual Fund


Mutual Funds
Mutual Fund


Mutual Funds
Mutual Fund


Mutual Funds
Mutual Fund


Mutual Funds
Mutual Fund


Mutual Funds
Mutual Fund


Mutual Funds
Mutual Fund


Spouse


Spouse $50,001 $100,000


Spouse $15,001 $50,000


Spouse $50,001 $100,000


Spouse $15,001 $50,000


Spouse $50,001 $100,000


Spouse $50,001 $100,000


Spouse $15,001 $50,000


None (or
less than
$201)


None (or
less than
$201)


None (or
less than
$201)


None (or
less than
$201)


None (or
less than
$201)


None (or
less than
$201)


None (or
less than
$201)


Bank Deposit Spouse None (or
less than
$1,001)


Interest, None (or
less than
$201)


Mutual Funds
Mutual Fund


Mutual Funds
Mutual Fund


Spouse $250,001 $500,000


Spouse $50,001 $100,000


Excepted
Investment
Fund,


Excepted
Investment
Fund,


$5,001 $15,000


$2,501 $5,000


Asset Asset Type Owner Value Income Type Income


39 RPMGX-T. Rowe Price
Mid-Cap Growth
(NASDAQ)

40 PRSCX-T. Rowe Price
Science & Tech
(NASDAQ)

41 OTCFX-T. Rowe Price
Small-Cap Stock
(NASDAQ)

42 (Pension Trust) VUSXX

   - Vanguard Treasury
Money Market
_Filer comment:_
Converted within the
Pension Trust from
Vanguard 500 Index to
Vanguard Treasury
Money Market in 2018.

43 VGIAX-Vanguard
Growth & Income Adm
(NASDAQ)

44 VMSXX - Vanguard
Municipal Money
Market Fund

45 VFIAX-Vanguard 500
Index Admiral
(NASDAQ)

46 (IRA) VFIAX-Vanguard
500 Index Admiral
(NASDAQ)

47 WFC-Wells Fargo &
Company (NYSE)


48 Wells Fargo &
Company/phantom
stock (Director
Deferred
Compensation)
_Company:_ Wells Fargo &
Company (San Francisco,
CA) _Description:_ Phantom
stock (Director Deferred
Compensation)

49 Vulcan Materials
Deferred Compensation
_Filer comment:_ All vested
in April 2018 - no more
deferred compensation.

49.1 VMC - Vulcan Materials
Company


Mutual Funds
Mutual Fund


Mutual Funds
Mutual Fund


Mutual Funds
Mutual Fund


Mutual Funds
Mutual Fund


Mutual Funds
Mutual Fund


Mutual Funds
Mutual Fund


Mutual Funds
Mutual Fund


Mutual Funds
Mutual Fund


Corporate
Securities
Stock

Deferred
Compensation


Deferred
Compensation
Deferred
Compensation

- Other


Corporate
Securities
Stock


Spouse $250,001 $500,000


Spouse $15,001 $50,000


Spouse $50,001 $100,000


Spouse $1,000,001 $5,000,000


Spouse $250,001 $500,000


Spouse $100,001 $250,000


Spouse $1,000,001 $5,000,000


Spouse $100,001 $250,000


Spouse $500,001 $1,000,000


Spouse $250,001 $500,000


Spouse


Spouse $250,001 $500,000


Excepted
Investment
Fund,


Excepted
Investment
Fund,


Excepted
Investment
Fund,


Excepted
Investment
Fund,


Excepted
Investment
Fund,


Excepted
Investment
Fund,


Excepted
Investment
Fund,


Excepted
Investment
Fund,


Dividends, $15,001 $50,000


None, None (or
less than
$201)


Dividends, $2,501 $5,000


$15,001 $50,000


$5,001 $15,000


$5,001 $15,000


None (or
less than
$201)


$5,001 $15,000


$5,001 $15,000


$15,001 $50,000


None (or
less than
$201)


Asset Asset Type Owner Value Income Type Income


50 UBS CSSP (via
Ingersoll-Rand)


Deferred
Compensation
Deferred
Compensation

- Other


Spouse


Spouse $100,001 $250,000


Spouse $15,001 $50,000


Spouse


50.1 IR-Ingersoll-Rand Plc Corporate
Securities
Stock


Dividends, $2,501 $5,000


51 MNNAX-Victory Munder
Growth Opportunities A
(NASDAQ)


Mutual Funds
Mutual Fund


Excepted
Investment
Fund,


$201 $1,000


52 UBS PSP Trust
General Trust


52.1 UBS (uninvested cash
held by UBS)
(Washington, D.C.)
_Type:_ Checking,

52.2 JHIGX - JHancock
International Growth R2


52.3 JDVPX - JHancock
Disciplined Value R2


53 Elaine L Chao
Revocable Trust
_Filer comment:_ Electron
Global was the
underlying asset.
Redeemed in 2016.


Bank Deposit Spouse $1,001 $15,000


Interest, None (or
less than
$201)


Mutual Funds
Mutual Fund


Mutual Funds
Mutual Fund


Trust
General Trust


Spouse $15,001 $50,000


Spouse $15,001 $50,000


Spouse None (or
less than
$1,001)


Excepted
Investment
Fund,


Excepted
Investment
Fund,


None, None (or
less than
$201)


None (or
less than
$201)


None (or
less than
$201)


Part 4a. Periodic Transaction Report Summary

In this section, electronically filed periodic transaction report (PTR) transactions are displayed for you.
Have you filed any paper-based PTRs in this period? No


Asset
Name Type Amount Comment


#


Transactio
n Date Owner Ticker


1 03/05/2018 Spouse WFC Wells
Fargo &
Company


2 06/01/2018 Spouse WFC Wells
Fargo &
Company


3 09/06/2018 Spouse WFC Wells
Fargo &
Company


4 12/05/2018 Spouse WFC Wells
Fargo &
Company


Purchase $1,001 $15,000


Purchase $1,001 $15,000


Purchase $1,001 $15,000


Purchase $1,001 $15,000


Dividend Reinvestment


Dividend Reinvestment


Dividend Reinvestment


Dividend Reinvestment


Part 4b. Transactions

Did you, your spouse, or dependent child buy, sell, or exchange an asset that exceeded $1,000? Yes


Transacti
on Type


Transactio
n Date Amount Comment


# Owner Ticker


Asset
Name


1 Self MNNAX Victory
Munder
Multi-Cap
Fund Class
A

2 Self MNNAX Victory
Munder
Multi-Cap
Fund Class
A


3 Self -- Vanguard
Aggressive
Growth
Portfolio
(Age Based)


4 Self -- Vanguard
Aggressive
Growth
Portfolio
(Age Based)

5 Self VHCAX Vanguard
Capital
Opportunity
Fund
Admiral
Shares

6 Self VHCAX Vanguard
Capital
Opportunity
Fund
Admiral
Shares

7 Self VSIAX Vanguard
Small Cap
Value Index
Fund
Admiral
Shares

8 Self VSIAX Vanguard
Small Cap
Value Index
Fund
Admiral
Shares

9 Self VSIAX Vanguard
Small Cap
Value Index
Fund
Admiral
Shares


Purchase 12/19/2018 $1,001 $15,000


Purchase 12/19/2018 $1,001 $15,000


Purchase 12/03/2018 $1,001 $15,000


Purchase 12/03/2018 $1,001 $15,000


Purchase 12/18/2018 $1,001 $15,000


Purchase 12/18/2018 $15,001 $50,000


Purchase 03/21/2018 $1,001 $15,000


Purchase 06/21/2018 $1,001 $15,000


Purchase 09/27/2018 $1,001 $15,000


Capital Gains
Reinvestment


Dividend
Reinvestment


-

-

Dividend
Reinvestment


Capital Gains
Reinvestment


Dividend
Reinvestment


Dividend
Reinvestment


Dividend
Reinvestment


Transacti
on Type


Transactio
n Date Amount Comment


# Owner Ticker


Asset
Name


10 Self VSIAX Vanguard
Small Cap
Value Index
Fund
Admiral
Shares

11 Self VFIAX Vanguard
500 Index
Fund
Admiral
Shares

12 Self VFIAX Vanguard
500 Index
Fund
Admiral
Shares

13 Self VFIAX Vanguard
500 Index
Fund
Admiral
Shares

14 Self VFIAX Vanguard
500 Index
Fund
Admiral
Shares

15 Spouse TRBCX T. Rowe
Price Blue
Chip Growth
Fund

16 Spouse PRITX T. Rowe
Price
International
Stock Fund

17 Spouse RPMGX T. Rowe
Price MidCap Growth
Fund

18 Spouse PRSCX T. Rowe
Price
Science and
Technology
Fund

19 Spouse OTCFX T. Rowe
Price SmallCap Stock
Fund

20 Joint VFIAX Vanguard
500 Index
Fund
Admiral
Shares


Purchase 12/21/2018 $1,001 $15,000


Purchase 03/23/2018 $1,001 $15,000


Purchase 06/27/2018 $1,001 $15,000


Purchase 09/25/2018 $1,001 $15,000


Purchase 12/14/2018 $1,001 $15,000


Purchase 12/13/2018 $1,001 $15,000


Purchase 12/17/2018 $1,001 $15,000


Purchase 12/13/2018 $15,001 $50,000


Purchase 12/14/2018 $1,001 $15,000


Purchase 12/13/2018 $1,001 $15,000


Purchase 03/23/2018 $15,001 $50,000


Dividend
Reinvestment


Dividend
Reinvestment


Dividend
Reinvestment


Dividend
Reinvestment


Dividend
Reinvestment


Dividend
Reinvestment


Dividend
Reinvestment


Dividend
Reinvestment


Dividend
Reinvestment


Dividend
Reinvestment


Dividend
Reinvestment


Transacti
on Type


Transactio
n Date Amount Comment


# Owner Ticker


Asset
Name


21 Joint VFIAX Vanguard
500 Index
Fund
Admiral
Shares

22 Joint VFIAX Vanguard
500 Index
Fund
Admiral
Shares

23 Joint VFIAX Vanguard
500 Index
Fund
Admiral
Shares

24 Spouse VGIAX Vanguard
Growth and
Income
Fund
Admiral
Shares

25 Spouse VGIAX Vanguard
Growth and
Income
Fund
Admiral
Shares


26 Spouse -- (IRA) VFIAX

             - Vanguard
500 Index
Admiral


27 Spouse -- (IRA) VFIAX

             - Vanguard
500 Index
Admiral


28 Spouse -- (IRA) VFIAX

             - Vanguard
500 Index
Admiral


29 Spouse -- (IRA) VFIAX

             - Vanguard
500 Index
Admiral


30 Spouse -- JDVPX John
Hancock
Funds
Disciplined
Value Fund
Class R2
(UBS PSP)


Purchase 06/27/2018 $15,001 $50,000


Purchase 09/25/2018 $15,001 $50,000


Purchase 12/14/2018 $15,001 $50,000


Purchase 06/15/2018 $1,001 $15,000


Purchase 12/18/2018 $15,001 $50,000


Purchase 03/23/2018 $1,001 $15,000


Purchase 06/27/2018 $1,001 $15,000


Purchase 09/25/2018 $1,001 $15,000


Purchase 12/14/2018 $1,001 $15,000


Purchase 12/17/2018 $1,001 $15,000


Dividend
Reinvestment


Dividend
Reinvestment


Dividend
Reinvestment


Dividend
Reinvestment


Dividend
Reinvestment


Dividend
Reinvestment


Dividend
Reinvestment


Dividend
Reinvestment


Dividend
Reinvestment


Dividend
Reinvestment


Transacti
on Type


Transactio
n Date Amount Comment


# Owner Ticker


Asset
Name


31 Spouse -- WGIFX American
Funds
Capital
World
Gr&Inc F2
(UBS
Pension
Trust)


32 Spouse -- GFFFX American
Funds The
Growth
Fund of
America
Class F2
(UBS
Pension
Trust)


33 Spouse -- PEQPX Principal
Equity
Income
(UBS
Pension
Trust)


34 Spouse -- PEQPX Principal
Equity
Income
(UBS IRA)


35 Spouse -- WGIFX American
Funds
Capital
World
Gr&Inc F2
(UBS IRA)


36 Spouse -- RSPYX Victory RS
Partners
Fund Class
Y (UBS IRA)


37 Spouse -- GFFFX American
Funds The
Growth
Fund of
America
Class F2
(UBS IRA)


Purchase 12/19/2018 $1,001 $15,000


Purchase 12/24/2018 $1,001 $15,000


Purchase 12/20/2018 $1,001 $15,000


Purchase 12/20/2018 $1,001 $15,000


Purchase 12/19/2018 $1,001 $15,000


Purchase 12/20/2018 $1,001 $15,000


Purchase 12/24/2018 $1,001 $15,000


Dividend
Reinvestment


Dividend
Reinvestment


Dividend
Reinvestment


Dividend
Reinvestment


Dividend
Reinvestment


Dividend
Reinvestment


Dividend
Reinvestment


Transacti
on Type


Transactio
n Date Amount Comment


# Owner Ticker


Asset
Name


38 Spouse MNNAX Victory
Munder
Multi-Cap
Fund Class
A

39 Spouse MNNAX Victory
Munder
Multi-Cap
Fund Class
A


40 Spouse -- (Pension
Trust)
VFIAX Vanguard
500 Index
Fund
Admiral
Shares


Part 5. Gifts


Purchase 12/19/2018 $1,001 $15,000


Purchase 12/19/2018 $1,001 $15,000


Sale
(Full)


04/02/2018 $1,000,001

        $5,000,000


Capital Gains
Reinvestment


Dividend
Reinvestment


Converted within the
Pension Trust from
Vanguard 500 Index
to Vanguard Treasury
Money Market


Did you, your spouse, or dependent child receive any reportable gift during the reporting period? Yes


# Date


Recipien
t Gift Value From


1 02/14/2018 Self 17th Annual
Waterways
Council Inc.
Leadership
Award plaque


2 10/20/2018 Self Veterans of
Foreign Wars
(VFW) Gold
Medal of
Merit


3 09/06/2018 Self Plaque from
Minor League
Baseball in
recognition of
leadership
and public
service


Part 6. Travel


$468.97 Waterways Council
Washington, DC


$398.00 The Veterans of Foreign Wars of the United
States
Kansas City, Mo


$826.28 Minor League Baseball
St. Petersburg, FL


Did you, your spouse, or dependent child receive any reportable travel? No


Part 7. Liabilities

Did you, your spouse, or dependent child have a reportable liability worth more than $10,000 at any


time? No


Part 8. Positions

Did you hold any outside positions during the reporting period? Yes


#


Position
Dates Position Held Entity Entity Type Comments


1 Jun
1994 to
present


Other (Member,
Visiting
Committee
(Uncompensated))


University
of
Kentucky
College of
Law
Lexington,
Kentucky


Other (Public
University/Law
School)


None


Part 9. Agreements

Did you have any reportable agreement or arrangement with an outside entity? Yes


# Date Parties Involved Type Status and Terms


1 Oct


Sentinel, an imprint
of Penguin
Publishing Group, a
division of Penguin
Random House LLC
(Sentinel)
New York, New
York


Other
(Compensation
and Royalty
Agreement)


A contract in which the undersigned agreed to
complete a manuscript in exchange for publication and $325,000 in compensation,
payable in installments, by Sentinel. The contract also provides for royalty payments in the
following manner: 15% of the retail price for all
hardcover editions of the book sold; 7.5% to
10% of the retail price for all trade edition and
mass market paperback copies sold; and 25%
of the receipts for e-book edition sales.


Part 10. Compensation

If this is your first report, or you are a candidate did you receive compensation of more than $5,000
from a single source in the two prior years? This is not my first report.


Attachments & Comments

_No attachments added._
_No comments added._



## Start with pdfplumber docs:

## https://github.com/jsvine/pdfplumber#extracting-tables



##  To rotate each page 90 degrees, I first ran: 

##  pdftk 116sdoc10_p1207_1225.pdf cat 1-endeast output 116sdoc10_p1207_1225_rotated.pdf
##

from pdfplumber import pdfplumber
IN_PATH = '116sdoc10_p1207_1225_rotated.pdf'

the_pdf = pdfplumber.open(IN_PATH)
pg = the_pdf.pages[0]
im = pg.to_image(resolution=150)

im
```


``` python
# finding tables with no defaults doesn't work very well. 


pg.to_image().debug_tablefinder()
```


``` python


## Even though the below isn't the table we want, it's still doing useful work

## It's going to be useful to identify the headers later.


## Also note we can plug the bounding box of the first row in for use later

tablesfound = pg.debug_tablefinder()
main_table = tablesfound.tables[0]

# Get the bounding box of the first row
top_region_bbox = main_table.rows[0].bbox

# I wasn't sure of the var name, I found it with this
# I could've read the docs too
# main_table.rows[0].__dict__

# Print the first row with this
pg.crop(top_region_bbox).to_image()



## IMPORTANT - THIS IS A DEMO, TO DO THIS FOR REAL YOU'D WANT TO 


## VERIFY THAT THIS WORKED ON EVERY PAGE, NOT JUST THIS ONE

## THIS IS FROM A 3000-PAGE PDF, IT'S NOT AS TRIVIAL AS IT SOUNDS

```


``` python
# The bbox is (x0, y0, x1, y1)
# so we could print the rest of the page with

pg.crop((top_region_bbox[0], top_region_bbox[3],top_region_bbox[2],pg.height)).to_image()

# This *is* the region we want to extract data from. We'll return to this in a bit. 
```


``` python


## Is it just a matter of cropping... not really

px = pg.crop((10, 200, pg.width, pg.height))
px.to_image().debug_tablefinder()
```


``` python
# From table.py source
# https://github.com/jsvine/pdfplumber/blob/master/pdfplumber/table.py#L391
# TABLE_STRATEGIES = [ "lines", "lines_strict", "text", "explicit" ]
# DEFAULT_TABLE_SETTINGS = {
#     "vertical_strategy": "lines",
#     "horizontal_strategy": "lines",
#     "explicit_vertical_lines": [],
#     "explicit_horizontal_lines": [],
#     "snap_tolerance": DEFAULT_SNAP_TOLERANCE,
#     "join_tolerance": DEFAULT_JOIN_TOLERANCE,
#     "edge_min_length": 3,
#     "min_words_vertical": DEFAULT_MIN_WORDS_VERTICAL,
#     "min_words_horizontal": DEFAULT_MIN_WORDS_HORIZONTAL,
#     "keep_blank_chars": False,
#     "text_tolerance": 3,
#     "text_x_tolerance": None,
#     "text_y_tolerance": None,
#     "intersection_tolerance": 3,
#     "intersection_x_tolerance": None,
#     "intersection_y_tolerance": None,
# }

config = {
    'vertical_strategy':'text',
}

px.to_image().debug_tablefinder(config)

```


``` python
px = pg.crop((10, 100, pg.width, pg.height))

config = {
    'vertical_strategy':'text',
    'horizontal_strategy':'text',
}

px.to_image().debug_tablefinder(config)
```


``` python
px = pg.crop((10, 100, pg.width, pg.height))

config = {
    'vertical_strategy':'text',
    'horizontal_strategy':'text',
    'keep_blank_chars':True
}

px.to_image().debug_tablefinder(config)
#     "keep_blank_chars": False,
```


``` python

## We can do an ok job with some of it if we are precise enough

px = pg.crop((0, 130, pg.width, 200))

config = {
    'vertical_strategy':'text',
    'horizontal_strategy':'text',
    'keep_blank_chars':True
}

px.to_image().debug_tablefinder(config)
#     "keep_blank_chars": False,
```


``` python


## But it gets messy

px = pg.crop((0, 130, pg.width, 400))

config = {
    'vertical_strategy':'text',
    'horizontal_strategy':'text',
    'keep_blank_chars':True
}

px.to_image().debug_tablefinder(config)
#     "keep_blank_chars": False,
```


``` python

## What if we just tell it where the lines should be? 

px = pg.crop((0, 130, pg.width, 200))

config = {
    #'vertical_strategy':'text',  
    #'horizontal_strategy':'text',
    'keep_blank_chars':True,
    'explicit_vertical_lines': [170,180],
    'explicit_horizontal_lines': [150,170]
    
    
}

px.to_image().debug_tablefinder(config)
#     "keep_blank_chars": False,

```


``` python


## Even though this seems harder, if we can just figure out where rows / columns

## start and end we will be in business, kinda



## Looking at the table it seems like each new payee would be a way to divide this up.


## Earlier we found just the header section, can we identify the column where payees are? 


## If we identify the payees column, then the location of each new payee

## then we feed those values back in as explicit lines. 


## If this seems convoluted, try doing this with pandas greater-than less-than selectors... 


```

``` python
# earlier on we were able to isolate the "top" of the page, we can actually isolate
# where payees by using the third cell

payee_header_region = main_table.rows[0].cells[2]

pg.crop(payee_header_region).to_image()
```


``` python
# The bbox is (x0, y0, x1, y1)
payee_header_region
```

    (Decimal('202.247'), Decimal('99.107'), Decimal('339.659'), Decimal('130.070'))

``` python
# Ok so we want to isolate the part of the page that's under *just* the payees header

under_payees_region = (payee_header_region[0],payee_header_region[3],payee_header_region[2],pg.height)
under_headers_region = (0,payee_header_region[3],pg.width,pg.height)

pg.crop(under_payees_region).to_image()
#pg.crop(under_headers_region).to_image()
```


``` python


config = {
    'vertical_strategy':'text',
    'horizontal_strategy':'text',

}


pg.crop(under_payees_region).to_image().debug_tablefinder(config)
```


``` python

## Not bad! The next step is to extract just the tops of these cells. 


## But note that we want to skipp the empty 

# extract the debugging info
tablesfound_debug = pg.crop(under_payees_region).debug_tablefinder(config)

# extract the tables that go with it
tables = pg.crop(under_payees_region).extract_tables(config)

print("num tables found %s" % len(tables))

y_values = []
for j, row in enumerate(tablesfound_debug.tables[0].rows):
    ytop = row.cells[0][1]
    
    # This is the value of the corresponding cell, because each column
    # has one item we know it's the first one
    cell_value = tables[0][j][0]
    if cell_value:
        y_values.append(ytop)
        
print("Y separators are %s" % y_values)


## 
```

    num tables found 1
    Y separators are [Decimal('137.581'), Decimal('144.058'), Decimal('150.031'), Decimal('156.004'), Decimal('161.977'), Decimal('167.950'), Decimal('173.922'), Decimal('179.895'), Decimal('185.868'), Decimal('191.841'), Decimal('207.202'), Decimal('219.588'), Decimal('231.973'), Decimal('244.358'), Decimal('262.277'), Decimal('280.195'), Decimal('292.581'), Decimal('304.966'), Decimal('317.351'), Decimal('329.737'), Decimal('347.655'), Decimal('360.040'), Decimal('372.426'), Decimal('384.811'), Decimal('397.196'), Decimal('415.115'), Decimal('427.500'), Decimal('439.885'), Decimal('452.271'), Decimal('464.656'), Decimal('477.042'), Decimal('489.427')]

``` python
# Now using the header from earlier, find the column separators.


# x0 y0 x1 y1 
main_table.rows[0].cells[0]
line_breaks = []
line_breaks.append(main_table.rows[0].cells[0][0])

for cell in main_table.rows[0].cells:
    print(cell)
    if cell:
        line_breaks.append(cell[2])
    else:
        print('skipping')
#print("breaks are %s" % line_breaks)
```

    (Decimal('70.332'), Decimal('99.107'), Decimal('140.687'), Decimal('130.070'))
    (Decimal('140.687'), Decimal('99.107'), Decimal('202.247'), Decimal('130.070'))
    (Decimal('202.247'), Decimal('99.107'), Decimal('339.659'), Decimal('130.070'))
    (Decimal('339.659'), Decimal('99.107'), Decimal('428.701'), Decimal('116.695'))
    None
    skipping
    (Decimal('428.701'), Decimal('99.107'), Decimal('647.460'), Decimal('130.070'))
    (Decimal('647.460'), Decimal('99.107'), Decimal('711.585'), Decimal('130.070'))

``` python

config = {
       'explicit_vertical_lines': line_breaks,
        'explicit_horizontal_lines': y_values
}


pg.crop(under_headers_region).to_image().debug_tablefinder(config)
```


``` python
# This is almost right! But note that the right column
# is a little off, if you look at the whole image
# they don't respect the lines
line_breaks[5] = 675 # 

# That's kinda a dangerous hack we don't know how well it works

config = {
        'explicit_vertical_lines': line_breaks,
        'explicit_horizontal_lines': y_values,
        'text_tolerance': 1,
        'text_x_tolerance': 1,
        'text_y_tolerance': 1,
        'keep_blank_chars':True,
}

pg.crop(under_headers_region).to_image().debug_tablefinder(config)

```


``` python
import csv


# syntax is a wee big funky see this https://github.com/jsvine/pdfplumber/issues/176
result = [ table.extract(x_tolerance = 1)
  for table in pg.crop(under_headers_region).find_tables(config) ]

outputwriter = csv.writer(open("senateoutput1.csv", 'w'))

for row in result[0]:
    print(row)
    outputwriter.writerow(row)
```

    ['', '', '', '', '', '']
    ['', '', 'BAIN, J MATTHEW', '', 'DISTRICT DIRECTOR', '37,499.96']
    ['', '', 'SMITH, ALVARO R', '', 'LEGISLATIVE CORRESPONDENT', '21,000.00']
    ['', '', 'ARMER, DEREK A', '', 'LEGISLATIVE CORRESPONDENT TO JUL. 15 AND FROM AUG. 11 TO AUG. 14', '12,111.06']
    ['', '', 'ENGLERT, PAYTON A', '', 'STAFF ASSISTANT', '25,499.96']
    ['', '', 'CAMPBELL, CLAYTON D', '', 'DISTRICT DIRECTOR FROM MAY 23', '31,111.08']
    ['', '', 'VELEZ-GREEN, ALEXANDER J', '', 'LEGISLATIVE ASSISTANT FROM MAY 22', '26,874.99']
    ['', '', 'BOLLINGER, ERIN S', '', 'INTERN FROM SEP. 18', '446.87']
    ['', '', 'KISHI, DANIEL M', '', 'LEGISLATIVE CORRESPONDENT FROM JUL. 15', '11,188.87']
    ['', '', 'LAVALLEY, ROBERT CLINTON', '', 'INTERN FROM SEP. 10', '1,260.00']
    ['', '', 'GRUENDER, BENJAMIN L', '', 'FIELD REPRESENTATIVE FROM SEP. 16', '1,458.33']
    ['DHAW20190001', '05/03/2019', 'CITIBANK - TRAVEL CBA CARD', '03/04/2019 03/06/2019', 'STAFF TRANSPORTATION\nAIRFARE FOR E JOHNSON KANSAS CITY TO WASHINGTON DC AND RETURN', '920.68']
    ['DHAW20190002', '05/24/2019', 'CITIBANK - TRAVEL CBA CARD', '03/10/2019 05/15/2019', 'STAFF TRANSPORTATION\nAIRFARE FOR S COWING KANSAS CITY TO WASHINGTON DC AND RETURN', '907.96']
    ['DHAW20190003', '05/03/2019', 'CITIBANK - TRAVEL CBA CARD', '03/01/2019 03/02/2019', 'STAFF TRANSPORTATION\nAIRFARE FOR M BERG WASHINGTON DC TO SAINT LOUIS AND RETURN', '737.94']
    ['DHAW20190004', '04/03/2019', 'CITIBANK - TRAVEL CBA CARD', '03/21/2019 03/24/2019', 'STAFF TRANSPORTATION\nAIRFARE FOR K FORD 3/21 WASHINGTON DC TO SAINT LOUIS, KANSAS CITY; 3/24 SAINT LOUIS TO\nWASHINGTON DC', '903.90']
    ['DHAW20190005', '05/28/2019', 'CITIBANK - TRAVEL CBA CARD', '03/21/2019 03/24/2019', "SENATOR'S TRANSPORTATION\nAIRFARE FOR SEN HAWLEY AS FOLLOWS: 3/21 WASHINGTON DC TO SAINT LOUIS TO KANSAS\nCITY; 3/24 SAINT LOUIS TO WASHINGTON DC", '798.90']
    ['DHAW20190026', '05/03/2019', 'CITIBANK - TRAVEL CBA CARD', '04/16/2019 04/17/2019', 'STAFF TRANSPORTATION\nAIRFARE FOR M BERG WASHINGTON DC TO SPRINGFIELD AND RETURN', '521.00']
    ['DHAW20190027', '05/02/2019', 'CITIBANK - TRAVEL CBA CARD', '04/15/2019 04/18/2019', 'STAFF TRANSPORTATION\nAIRFARE FOR R LEAVITT WASHINGTON DC TO KANSAS CITY, SAINT LOUIS AND RETURN', '349.60']
    ['DHAW20190029', '05/16/2019', 'CITIBANK - TRAVEL CBA CARD', '05/07/2019 05/09/2019', 'STAFF TRANSPORTATION\nAIRFARE FOR D HARTMAN SAINT LOUIS MO TO WASHINGTON DC AND RETURN', '477.60']
    ['DHAW20190031', '05/28/2019', 'CITIBANK - SENATOR IBA CARD', '05/10/2019 05/11/2019', "SENATOR'S TRANSPORTATION\nTRAIN FARE FOR SEN HAWLEY WASHINGTON DC TO NEW YORK NY AND RETURN", '618.00']
    ['DHAW20190032', '06/13/2019', 'CITIBANK - SENATOR IBA CARD', '05/24/2019 05/25/2019', "SENATOR'S TRANSPORTATION\nAIRFARE FOR SEN HAWLEY WASHINGTON DC TO SPRINGFIELD MO, SAINT LOUIS MO AND\nRETURN", '553.30']
    ['DHAW20190033', '06/04/2019', 'CITIBANK - TRAVEL CBA CARD', '05/24/2019 05/25/2019', 'STAFF TRANSPORTATION\nAIRFARE FOR M BERG WASHINGTON DC TO SPRINGFIELD, ST. LOUIS AND RETURN', '601.30']
    ['DHAW20190034', '06/04/2019', 'CITIBANK - TRAVEL CBA CARD', '05/24/2019 05/25/2019', 'STAFF TRANSPORTATION\nAIRFARE FOR R BURLESON WASHINGTON DC TO SPRINGFIELD, ST. LOUIS AND RETURN', '601.30']
    ['DHAW20190040', '06/04/2019', 'CITIBANK - TRAVEL CBA CARD', '05/29/2019 05/31/2019', 'STAFF TRANSPORTATION\nAIRFARE FOR J RESES WASHINGTON DC TO KANSAS CITY AND RETURN', '304.30']
    ['DHAW20190041', '06/13/2019', 'CITIBANK - TRAVEL CBA CARD', '04/13/2019 04/27/2019', "SENATOR'S TRANSPORTATION\nAIRFARE FOR SEN HAWLEY WASHINGTON DC TO SPRINGFIELD MO, AMARILLO TX AND RETURN", '697.00']
    ['DHAW20190045', '07/10/2019', 'CITIBANK - SENATOR IBA CARD', '06/29/2019 07/07/2019', 'STAFF TRANSPORTATION\nAIRFARE FOR SEN HAWLEY AS FOLLOWS: 6/29 WASHINGTON DC TO SPRINGFIELD; 7/7\nSPRINGFIELD TO WASHINGTON DC', '1,112.00']
    ['DHAW20190046', '07/11/2019', 'CITIBANK - TRAVEL CBA CARD', '07/01/2019 07/07/2019', 'STAFF TRANSPORTATION\nAIRFARE FOR J MACGREGOR WASHINGTON DC TO KANSAS CITY, SPRINGFIELD AND RETURN', '728.30']
    ['DHAW20190047', '07/12/2019', 'CITIBANK - TRAVEL CBA CARD', '07/01/2019 07/03/2019', 'STAFF TRANSPORTATION\nAIRFARE FOR K FORD DETROIT MI TO ST LOUIS, SPRINGFIELD AND RETURN', '463.30']
    ['DHAW20190049', '07/25/2019', 'CITIBANK - SENATOR IBA CARD', '07/07/2019 07/07/2019', "SENATOR'S TRANSPORTATION\nAIRFARE FOR SEN HAWLEY SPRINGFIELD TO WASHINGTON DC", '70.00']
    ['DHAW20190067', '09/04/2019', 'CITIBANK - TRAVEL CBA CARD', '08/17/2019 08/25/2019', 'STAFF TRANSPORTATION\nAIRFARE FOR C NAYLOR KANSAS CITY MO TO SAN DIEGO CA AND RETURN', '685.01']
    ['DHAW20190068', '09/04/2019', 'CITIBANK - TRAVEL CBA CARD', '08/12/2019 08/14/2019', 'STAFF TRANSPORTATION\nAIRFARE FOR C MESSERVY WASHINGTON DC TO SPRINGFIELD AND RETURN', '411.49']
    ['DHAW20190069', '09/09/2019', 'CITIBANK - TRAVEL CBA CARD', '08/12/2019 08/14/2019', 'STAFF TRANSPORTATION\nAIRFARE FOR A VELEZ-GREEN WASHINGTON DC TO SPRINGFIELD AND RETURN', '411.49']
    ['DHAW20190070', '09/09/2019', 'CITIBANK - TRAVEL CBA CARD', '08/12/2019 08/14/2019', 'STAFF TRANSPORTATION\nAIRFARE FOR C WEIHS WASHINGTON DC TO SPRINGFIELD AND RETURN', '411.49']

``` python
# It's a bit unclear why the words are getting extracted like that? 

words = pg.crop(under_headers_region).extract_words(x_tolerance=1, y_tolerance=1)
words
```

    [{'x0': Decimal('201.881'),
      'x1': Decimal('215.275'),
      'top': Decimal('137.581'),
      'bottom': Decimal('144.563'),
      'text': 'BAIN,'},
     {'x0': Decimal('216.706'),
      'x1': Decimal('219.271'),
      'top': Decimal('137.581'),
      'bottom': Decimal('144.563'),
      'text': 'J'},
     {'x0': Decimal('220.692'),
      'x1': Decimal('246.618'),
      'top': Decimal('137.581'),
      'bottom': Decimal('144.563'),
      'text': 'MATTHEW'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('451.991'),
      'top': Decimal('137.581'),
      'bottom': Decimal('144.563'),
      'text': 'DISTRICT'},
     {'x0': Decimal('453.418'),
      'x1': Decimal('480.215'),
      'top': Decimal('137.581'),
      'bottom': Decimal('144.563'),
      'text': 'DIRECTOR'},
     {'x0': Decimal('680.285'),
      'x1': Decimal('703.111'),
      'top': Decimal('137.581'),
      'bottom': Decimal('144.563'),
      'text': '37,499.96'},
     {'x0': Decimal('201.881'),
      'x1': Decimal('219.260'),
      'top': Decimal('143.553'),
      'bottom': Decimal('150.535'),
      'text': 'SMITH,'},
     {'x0': Decimal('220.692'),
      'x1': Decimal('241.501'),
      'top': Decimal('143.553'),
      'bottom': Decimal('150.535'),
      'text': 'ALVARO'},
     {'x0': Decimal('242.928'),
      'x1': Decimal('246.632'),
      'top': Decimal('143.553'),
      'bottom': Decimal('150.535'),
      'text': 'R'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('461.131'),
      'top': Decimal('143.553'),
      'bottom': Decimal('150.535'),
      'text': 'LEGISLATIVE'},
     {'x0': Decimal('462.563'),
      'x1': Decimal('509.597'),
      'top': Decimal('143.553'),
      'bottom': Decimal('150.535'),
      'text': 'CORRESPONDENT'},
     {'x0': Decimal('680.285'),
      'x1': Decimal('703.111'),
      'top': Decimal('143.553'),
      'bottom': Decimal('150.535'),
      'text': '21,000.00'},
     {'x0': Decimal('201.881'),
      'x1': Decimal('221.828'),
      'top': Decimal('149.526'),
      'bottom': Decimal('156.508'),
      'text': 'ARMER,'},
     {'x0': Decimal('223.260'),
      'x1': Decimal('240.930'),
      'top': Decimal('149.526'),
      'bottom': Decimal('156.508'),
      'text': 'DEREK'},
     {'x0': Decimal('242.360'),
      'x1': Decimal('245.776'),
      'top': Decimal('149.526'),
      'bottom': Decimal('156.508'),
      'text': 'A'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('461.119'),
      'top': Decimal('149.526'),
      'bottom': Decimal('156.508'),
      'text': 'LEGISLATIVE'},
     {'x0': Decimal('462.550'),
      'x1': Decimal('509.576'),
      'top': Decimal('149.526'),
      'bottom': Decimal('156.508'),
      'text': 'CORRESPONDENT'},
     {'x0': Decimal('511.002'),
      'x1': Decimal('518.122'),
      'top': Decimal('149.526'),
      'bottom': Decimal('156.508'),
      'text': 'TO'},
     {'x0': Decimal('519.553'),
      'x1': Decimal('530.097'),
      'top': Decimal('149.526'),
      'bottom': Decimal('156.508'),
      'text': 'JUL.'},
     {'x0': Decimal('531.529'),
      'x1': Decimal('537.235'),
      'top': Decimal('149.526'),
      'bottom': Decimal('156.508'),
      'text': '15'},
     {'x0': Decimal('538.662'),
      'x1': Decimal('549.493'),
      'top': Decimal('149.526'),
      'bottom': Decimal('156.508'),
      'text': 'AND'},
     {'x0': Decimal('550.917'),
      'x1': Decimal('566.019'),
      'top': Decimal('149.526'),
      'bottom': Decimal('156.508'),
      'text': 'FROM'},
     {'x0': Decimal('567.442'),
      'x1': Decimal('579.980'),
      'top': Decimal('149.526'),
      'bottom': Decimal('156.508'),
      'text': 'AUG.'},
     {'x0': Decimal('581.409'),
      'x1': Decimal('587.115'),
      'top': Decimal('149.526'),
      'bottom': Decimal('156.508'),
      'text': '11'},
     {'x0': Decimal('588.542'),
      'x1': Decimal('595.662'),
      'top': Decimal('149.526'),
      'bottom': Decimal('156.508'),
      'text': 'TO'},
     {'x0': Decimal('597.100'),
      'x1': Decimal('609.638'),
      'top': Decimal('149.526'),
      'bottom': Decimal('156.508'),
      'text': 'AUG.'},
     {'x0': Decimal('611.068'),
      'x1': Decimal('616.773'),
      'top': Decimal('149.526'),
      'bottom': Decimal('156.508'),
      'text': '14'},
     {'x0': Decimal('680.285'),
      'x1': Decimal('703.111'),
      'top': Decimal('149.526'),
      'bottom': Decimal('156.508'),
      'text': '12,111.06'},
     {'x0': Decimal('201.881'),
      'x1': Decimal('227.531'),
      'top': Decimal('155.499'),
      'bottom': Decimal('162.481'),
      'text': 'ENGLERT,'},
     {'x0': Decimal('228.957'),
      'x1': Decimal('250.052'),
      'top': Decimal('155.499'),
      'bottom': Decimal('162.481'),
      'text': 'PAYTON'},
     {'x0': Decimal('251.478'),
      'x1': Decimal('254.894'),
      'top': Decimal('155.499'),
      'bottom': Decimal('162.481'),
      'text': 'A'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('444.576'),
      'top': Decimal('155.499'),
      'bottom': Decimal('162.481'),
      'text': 'STAFF'},
     {'x0': Decimal('446.003'),
      'x1': Decimal('474.505'),
      'top': Decimal('155.499'),
      'bottom': Decimal('162.481'),
      'text': 'ASSISTANT'},
     {'x0': Decimal('680.285'),
      'x1': Decimal('703.111'),
      'top': Decimal('155.499'),
      'bottom': Decimal('162.481'),
      'text': '25,499.96'},
     {'x0': Decimal('201.881'),
      'x1': Decimal('230.674'),
      'top': Decimal('161.472'),
      'bottom': Decimal('168.454'),
      'text': 'CAMPBELL,'},
     {'x0': Decimal('232.106'),
      'x1': Decimal('256.336'),
      'top': Decimal('161.472'),
      'bottom': Decimal('168.454'),
      'text': 'CLAYTON'},
     {'x0': Decimal('257.758'),
      'x1': Decimal('261.461'),
      'top': Decimal('161.472'),
      'bottom': Decimal('168.454'),
      'text': 'D'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('451.984'),
      'top': Decimal('161.472'),
      'bottom': Decimal('168.454'),
      'text': 'DISTRICT'},
     {'x0': Decimal('453.412'),
      'x1': Decimal('480.201'),
      'top': Decimal('161.472'),
      'bottom': Decimal('168.454'),
      'text': 'DIRECTOR'},
     {'x0': Decimal('481.628'),
      'x1': Decimal('496.730'),
      'top': Decimal('161.472'),
      'bottom': Decimal('168.454'),
      'text': 'FROM'},
     {'x0': Decimal('498.153'),
      'x1': Decimal('509.265'),
      'top': Decimal('161.472'),
      'bottom': Decimal('168.454'),
      'text': 'MAY'},
     {'x0': Decimal('510.700'),
      'x1': Decimal('516.405'),
      'top': Decimal('161.472'),
      'bottom': Decimal('168.454'),
      'text': '23'},
     {'x0': Decimal('680.285'),
      'x1': Decimal('703.111'),
      'top': Decimal('161.472'),
      'bottom': Decimal('168.454'),
      'text': '31,111.08'},
     {'x0': Decimal('201.881'),
      'x1': Decimal('239.505'),
      'top': Decimal('167.445'),
      'bottom': Decimal('174.427'),
      'text': 'VELEZ-GREEN,'},
     {'x0': Decimal('240.935'),
      'x1': Decimal('272.011'),
      'top': Decimal('167.445'),
      'bottom': Decimal('174.427'),
      'text': 'ALEXANDER'},
     {'x0': Decimal('273.436'),
      'x1': Decimal('276.001'),
      'top': Decimal('167.445'),
      'bottom': Decimal('174.427'),
      'text': 'J'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('461.119'),
      'top': Decimal('167.445'),
      'bottom': Decimal('174.427'),
      'text': 'LEGISLATIVE'},
     {'x0': Decimal('462.550'),
      'x1': Decimal('491.051'),
      'top': Decimal('167.445'),
      'bottom': Decimal('174.427'),
      'text': 'ASSISTANT'},
     {'x0': Decimal('492.478'),
      'x1': Decimal('507.580'),
      'top': Decimal('167.445'),
      'bottom': Decimal('174.427'),
      'text': 'FROM'},
     {'x0': Decimal('509.003'),
      'x1': Decimal('520.114'),
      'top': Decimal('167.445'),
      'bottom': Decimal('174.427'),
      'text': 'MAY'},
     {'x0': Decimal('521.542'),
      'x1': Decimal('527.248'),
      'top': Decimal('167.445'),
      'bottom': Decimal('174.427'),
      'text': '22'},
     {'x0': Decimal('680.285'),
      'x1': Decimal('703.111'),
      'top': Decimal('167.445'),
      'bottom': Decimal('174.427'),
      'text': '26,874.99'},
     {'x0': Decimal('201.881'),
      'x1': Decimal('232.666'),
      'top': Decimal('173.417'),
      'bottom': Decimal('180.399'),
      'text': 'BOLLINGER,'},
     {'x0': Decimal('234.097'),
      'x1': Decimal('246.353'),
      'top': Decimal('173.417'),
      'bottom': Decimal('180.399'),
      'text': 'ERIN'},
     {'x0': Decimal('247.779'),
      'x1': Decimal('251.196'),
      'top': Decimal('173.417'),
      'bottom': Decimal('180.399'),
      'text': 'S'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('447.424'),
      'top': Decimal('173.417'),
      'bottom': Decimal('180.399'),
      'text': 'INTERN'},
     {'x0': Decimal('448.849'),
      'x1': Decimal('463.948'),
      'top': Decimal('173.417'),
      'bottom': Decimal('180.399'),
      'text': 'FROM'},
     {'x0': Decimal('465.373'),
      'x1': Decimal('477.057'),
      'top': Decimal('173.417'),
      'bottom': Decimal('180.399'),
      'text': 'SEP.'},
     {'x0': Decimal('478.487'),
      'x1': Decimal('484.190'),
      'top': Decimal('173.417'),
      'bottom': Decimal('180.399'),
      'text': '18'},
     {'x0': Decimal('687.430'),
      'x1': Decimal('703.123'),
      'top': Decimal('173.417'),
      'bottom': Decimal('180.399'),
      'text': '446.87'},
     {'x0': Decimal('201.881'),
      'x1': Decimal('216.701'),
      'top': Decimal('179.390'),
      'bottom': Decimal('186.372'),
      'text': 'KISHI,'},
     {'x0': Decimal('218.128'),
      'x1': Decimal('236.657'),
      'top': Decimal('179.390'),
      'bottom': Decimal('186.372'),
      'text': 'DANIEL'},
     {'x0': Decimal('238.083'),
      'x1': Decimal('242.357'),
      'top': Decimal('179.390'),
      'bottom': Decimal('186.372'),
      'text': 'M'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('461.119'),
      'top': Decimal('179.390'),
      'bottom': Decimal('186.372'),
      'text': 'LEGISLATIVE'},
     {'x0': Decimal('462.550'),
      'x1': Decimal('509.576'),
      'top': Decimal('179.390'),
      'bottom': Decimal('186.372'),
      'text': 'CORRESPONDENT'},
     {'x0': Decimal('511.002'),
      'x1': Decimal('526.104'),
      'top': Decimal('179.390'),
      'bottom': Decimal('186.372'),
      'text': 'FROM'},
     {'x0': Decimal('527.527'),
      'x1': Decimal('538.072'),
      'top': Decimal('179.390'),
      'bottom': Decimal('186.372'),
      'text': 'JUL.'},
     {'x0': Decimal('539.503'),
      'x1': Decimal('545.209'),
      'top': Decimal('179.390'),
      'bottom': Decimal('186.372'),
      'text': '15'},
     {'x0': Decimal('680.285'),
      'x1': Decimal('703.111'),
      'top': Decimal('179.390'),
      'bottom': Decimal('186.372'),
      'text': '11,188.87'},
     {'x0': Decimal('201.881'),
      'x1': Decimal('228.976'),
      'top': Decimal('185.363'),
      'bottom': Decimal('192.345'),
      'text': 'LAVALLEY,'},
     {'x0': Decimal('230.403'),
      'x1': Decimal('251.780'),
      'top': Decimal('185.363'),
      'bottom': Decimal('192.345'),
      'text': 'ROBERT'},
     {'x0': Decimal('253.212'),
      'x1': Decimal('275.734'),
      'top': Decimal('185.363'),
      'bottom': Decimal('192.345'),
      'text': 'CLINTON'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('447.424'),
      'top': Decimal('185.363'),
      'bottom': Decimal('192.345'),
      'text': 'INTERN'},
     {'x0': Decimal('448.849'),
      'x1': Decimal('463.948'),
      'top': Decimal('185.363'),
      'bottom': Decimal('192.345'),
      'text': 'FROM'},
     {'x0': Decimal('465.373'),
      'x1': Decimal('477.057'),
      'top': Decimal('185.363'),
      'bottom': Decimal('192.345'),
      'text': 'SEP.'},
     {'x0': Decimal('478.487'),
      'x1': Decimal('484.190'),
      'top': Decimal('185.363'),
      'bottom': Decimal('192.345'),
      'text': '10'},
     {'x0': Decimal('683.143'),
      'x1': Decimal('703.116'),
      'top': Decimal('185.363'),
      'bottom': Decimal('192.345'),
      'text': '1,260.00'},
     {'x0': Decimal('201.881'),
      'x1': Decimal('232.660'),
      'top': Decimal('191.336'),
      'bottom': Decimal('198.318'),
      'text': 'GRUENDER,'},
     {'x0': Decimal('234.093'),
      'x1': Decimal('260.031'),
      'top': Decimal('191.336'),
      'bottom': Decimal('198.318'),
      'text': 'BENJAMIN'},
     {'x0': Decimal('261.459'),
      'x1': Decimal('264.312'),
      'top': Decimal('191.336'),
      'bottom': Decimal('198.318'),
      'text': 'L'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('442.869'),
      'top': Decimal('191.336'),
      'bottom': Decimal('198.318'),
      'text': 'FIELD'},
     {'x0': Decimal('444.294'),
      'x1': Decimal('490.456'),
      'top': Decimal('191.336'),
      'bottom': Decimal('198.318'),
      'text': 'REPRESENTATIVE'},
     {'x0': Decimal('491.886'),
      'x1': Decimal('506.986'),
      'top': Decimal('191.336'),
      'bottom': Decimal('198.318'),
      'text': 'FROM'},
     {'x0': Decimal('508.411'),
      'x1': Decimal('520.094'),
      'top': Decimal('191.336'),
      'bottom': Decimal('198.318'),
      'text': 'SEP.'},
     {'x0': Decimal('521.525'),
      'x1': Decimal('527.228'),
      'top': Decimal('191.336'),
      'bottom': Decimal('198.318'),
      'text': '16'},
     {'x0': Decimal('683.143'),
      'x1': Decimal('703.116'),
      'top': Decimal('191.336'),
      'bottom': Decimal('198.318'),
      'text': '1,458.33'},
     {'x0': Decimal('88.617'),
      'x1': Decimal('127.119'),
      'top': Decimal('207.202'),
      'bottom': Decimal('214.184'),
      'text': 'DHAW20190001'},
     {'x0': Decimal('155.088'),
      'x1': Decimal('180.768'),
      'top': Decimal('207.202'),
      'bottom': Decimal('214.184'),
      'text': '05/03/2019'},
     {'x0': Decimal('201.881'),
      'x1': Decimal('225.543'),
      'top': Decimal('207.202'),
      'bottom': Decimal('214.184'),
      'text': 'CITIBANK'},
     {'x0': Decimal('226.975'),
      'x1': Decimal('228.683'),
      'top': Decimal('207.202'),
      'bottom': Decimal('214.184'),
      'text': '-'},
     {'x0': Decimal('230.105'),
      'x1': Decimal('250.066'),
      'top': Decimal('207.202'),
      'bottom': Decimal('214.184'),
      'text': 'TRAVEL'},
     {'x0': Decimal('251.498'),
      'x1': Decimal('262.043'),
      'top': Decimal('207.202'),
      'bottom': Decimal('214.184'),
      'text': 'CBA'},
     {'x0': Decimal('263.475'),
      'x1': Decimal('278.011'),
      'top': Decimal('207.202'),
      'bottom': Decimal('214.184'),
      'text': 'CARD'},
     {'x0': Decimal('347.317'),
      'x1': Decimal('372.997'),
      'top': Decimal('207.202'),
      'bottom': Decimal('214.184'),
      'text': '03/04/2019'},
     {'x0': Decimal('392.388'),
      'x1': Decimal('418.068'),
      'top': Decimal('207.202'),
      'bottom': Decimal('214.184'),
      'text': '03/06/2019'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('444.576'),
      'top': Decimal('207.202'),
      'bottom': Decimal('214.184'),
      'text': 'STAFF'},
     {'x0': Decimal('446.003'),
      'x1': Decimal('493.317'),
      'top': Decimal('207.202'),
      'bottom': Decimal('214.184'),
      'text': 'TRANSPORTATION'},
     {'x0': Decimal('687.430'),
      'x1': Decimal('703.123'),
      'top': Decimal('207.202'),
      'bottom': Decimal('214.184'),
      'text': '920.68'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('450.563'),
      'top': Decimal('213.175'),
      'bottom': Decimal('220.157'),
      'text': 'AIRFARE'},
     {'x0': Decimal('451.991'),
      'x1': Decimal('462.819'),
      'top': Decimal('213.175'),
      'bottom': Decimal('220.157'),
      'text': 'FOR'},
     {'x0': Decimal('464.243'),
      'x1': Decimal('467.660'),
      'top': Decimal('213.175'),
      'bottom': Decimal('220.157'),
      'text': 'E'},
     {'x0': Decimal('469.095'),
      'x1': Decimal('494.175'),
      'top': Decimal('213.175'),
      'bottom': Decimal('220.157'),
      'text': 'JOHNSON'},
     {'x0': Decimal('495.603'),
      'x1': Decimal('516.412'),
      'top': Decimal('213.175'),
      'bottom': Decimal('220.157'),
      'text': 'KANSAS'},
     {'x0': Decimal('517.839'),
      'x1': Decimal('529.519'),
      'top': Decimal('213.175'),
      'bottom': Decimal('220.157'),
      'text': 'CITY'},
     {'x0': Decimal('530.949'),
      'x1': Decimal('538.068'),
      'top': Decimal('213.175'),
      'bottom': Decimal('220.157'),
      'text': 'TO'},
     {'x0': Decimal('539.507'),
      'x1': Decimal('574.845'),
      'top': Decimal('213.175'),
      'bottom': Decimal('220.157'),
      'text': 'WASHINGTON'},
     {'x0': Decimal('576.272'),
      'x1': Decimal('583.681'),
      'top': Decimal('213.175'),
      'bottom': Decimal('220.157'),
      'text': 'DC'},
     {'x0': Decimal('585.105'),
      'x1': Decimal('595.936'),
      'top': Decimal('213.175'),
      'bottom': Decimal('220.157'),
      'text': 'AND'},
     {'x0': Decimal('597.360'),
      'x1': Decimal('618.734'),
      'top': Decimal('213.175'),
      'bottom': Decimal('220.157'),
      'text': 'RETURN'},
     {'x0': Decimal('88.617'),
      'x1': Decimal('127.119'),
      'top': Decimal('219.588'),
      'bottom': Decimal('226.570'),
      'text': 'DHAW20190002'},
     {'x0': Decimal('155.088'),
      'x1': Decimal('180.768'),
      'top': Decimal('219.588'),
      'bottom': Decimal('226.570'),
      'text': '05/24/2019'},
     {'x0': Decimal('201.881'),
      'x1': Decimal('225.543'),
      'top': Decimal('219.588'),
      'bottom': Decimal('226.570'),
      'text': 'CITIBANK'},
     {'x0': Decimal('226.975'),
      'x1': Decimal('228.683'),
      'top': Decimal('219.588'),
      'bottom': Decimal('226.570'),
      'text': '-'},
     {'x0': Decimal('230.105'),
      'x1': Decimal('250.066'),
      'top': Decimal('219.588'),
      'bottom': Decimal('226.570'),
      'text': 'TRAVEL'},
     {'x0': Decimal('251.498'),
      'x1': Decimal('262.043'),
      'top': Decimal('219.588'),
      'bottom': Decimal('226.570'),
      'text': 'CBA'},
     {'x0': Decimal('263.475'),
      'x1': Decimal('278.011'),
      'top': Decimal('219.588'),
      'bottom': Decimal('226.570'),
      'text': 'CARD'},
     {'x0': Decimal('347.317'),
      'x1': Decimal('372.997'),
      'top': Decimal('219.588'),
      'bottom': Decimal('226.570'),
      'text': '03/10/2019'},
     {'x0': Decimal('392.388'),
      'x1': Decimal('418.068'),
      'top': Decimal('219.588'),
      'bottom': Decimal('226.570'),
      'text': '05/15/2019'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('444.576'),
      'top': Decimal('219.588'),
      'bottom': Decimal('226.570'),
      'text': 'STAFF'},
     {'x0': Decimal('446.003'),
      'x1': Decimal('493.317'),
      'top': Decimal('219.588'),
      'bottom': Decimal('226.570'),
      'text': 'TRANSPORTATION'},
     {'x0': Decimal('687.430'),
      'x1': Decimal('703.123'),
      'top': Decimal('219.588'),
      'bottom': Decimal('226.570'),
      'text': '907.96'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('450.563'),
      'top': Decimal('225.560'),
      'bottom': Decimal('232.542'),
      'text': 'AIRFARE'},
     {'x0': Decimal('451.989'),
      'x1': Decimal('462.819'),
      'top': Decimal('225.560'),
      'bottom': Decimal('232.542'),
      'text': 'FOR'},
     {'x0': Decimal('464.245'),
      'x1': Decimal('467.661'),
      'top': Decimal('225.560'),
      'bottom': Decimal('232.542'),
      'text': 'S'},
     {'x0': Decimal('469.098'),
      'x1': Decimal('490.752'),
      'top': Decimal('225.560'),
      'bottom': Decimal('232.542'),
      'text': 'COWING'},
     {'x0': Decimal('492.173'),
      'x1': Decimal('512.980'),
      'top': Decimal('225.560'),
      'bottom': Decimal('232.542'),
      'text': 'KANSAS'},
     {'x0': Decimal('514.416'),
      'x1': Decimal('526.098'),
      'top': Decimal('225.560'),
      'bottom': Decimal('232.542'),
      'text': 'CITY'},
     {'x0': Decimal('527.534'),
      'x1': Decimal('534.654'),
      'top': Decimal('225.560'),
      'bottom': Decimal('232.542'),
      'text': 'TO'},
     {'x0': Decimal('536.086'),
      'x1': Decimal('571.426'),
      'top': Decimal('225.560'),
      'bottom': Decimal('232.542'),
      'text': 'WASHINGTON'},
     {'x0': Decimal('572.847'),
      'x1': Decimal('580.255'),
      'top': Decimal('225.560'),
      'bottom': Decimal('232.542'),
      'text': 'DC'},
     {'x0': Decimal('581.686'),
      'x1': Decimal('592.516'),
      'top': Decimal('225.560'),
      'bottom': Decimal('232.542'),
      'text': 'AND'},
     {'x0': Decimal('593.942'),
      'x1': Decimal('615.314'),
      'top': Decimal('225.560'),
      'bottom': Decimal('232.542'),
      'text': 'RETURN'},
     {'x0': Decimal('88.617'),
      'x1': Decimal('127.119'),
      'top': Decimal('231.973'),
      'bottom': Decimal('238.955'),
      'text': 'DHAW20190003'},
     {'x0': Decimal('155.088'),
      'x1': Decimal('180.768'),
      'top': Decimal('231.973'),
      'bottom': Decimal('238.955'),
      'text': '05/03/2019'},
     {'x0': Decimal('201.881'),
      'x1': Decimal('225.543'),
      'top': Decimal('231.973'),
      'bottom': Decimal('238.955'),
      'text': 'CITIBANK'},
     {'x0': Decimal('226.975'),
      'x1': Decimal('228.683'),
      'top': Decimal('231.973'),
      'bottom': Decimal('238.955'),
      'text': '-'},
     {'x0': Decimal('230.105'),
      'x1': Decimal('250.066'),
      'top': Decimal('231.973'),
      'bottom': Decimal('238.955'),
      'text': 'TRAVEL'},
     {'x0': Decimal('251.498'),
      'x1': Decimal('262.043'),
      'top': Decimal('231.973'),
      'bottom': Decimal('238.955'),
      'text': 'CBA'},
     {'x0': Decimal('263.475'),
      'x1': Decimal('278.011'),
      'top': Decimal('231.973'),
      'bottom': Decimal('238.955'),
      'text': 'CARD'},
     {'x0': Decimal('347.317'),
      'x1': Decimal('372.997'),
      'top': Decimal('231.973'),
      'bottom': Decimal('238.955'),
      'text': '03/01/2019'},
     {'x0': Decimal('392.388'),
      'x1': Decimal('418.068'),
      'top': Decimal('231.973'),
      'bottom': Decimal('238.955'),
      'text': '03/02/2019'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('444.576'),
      'top': Decimal('231.973'),
      'bottom': Decimal('238.955'),
      'text': 'STAFF'},
     {'x0': Decimal('446.003'),
      'x1': Decimal('493.317'),
      'top': Decimal('231.973'),
      'bottom': Decimal('238.955'),
      'text': 'TRANSPORTATION'},
     {'x0': Decimal('687.430'),
      'x1': Decimal('703.123'),
      'top': Decimal('231.973'),
      'bottom': Decimal('238.955'),
      'text': '737.94'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('450.563'),
      'top': Decimal('237.946'),
      'bottom': Decimal('244.928'),
      'text': 'AIRFARE'},
     {'x0': Decimal('451.989'),
      'x1': Decimal('462.819'),
      'top': Decimal('237.946'),
      'bottom': Decimal('244.928'),
      'text': 'FOR'},
     {'x0': Decimal('464.245'),
      'x1': Decimal('468.518'),
      'top': Decimal('237.946'),
      'bottom': Decimal('244.928'),
      'text': 'M'},
     {'x0': Decimal('469.944'),
      'x1': Decimal('484.478'),
      'top': Decimal('237.946'),
      'bottom': Decimal('244.928'),
      'text': 'BERG'},
     {'x0': Decimal('485.904'),
      'x1': Decimal('521.245'),
      'top': Decimal('237.946'),
      'bottom': Decimal('244.928'),
      'text': 'WASHINGTON'},
     {'x0': Decimal('522.671'),
      'x1': Decimal('530.078'),
      'top': Decimal('237.946'),
      'bottom': Decimal('244.928'),
      'text': 'DC'},
     {'x0': Decimal('531.505'),
      'x1': Decimal('538.625'),
      'top': Decimal('237.946'),
      'bottom': Decimal('244.928'),
      'text': 'TO'},
     {'x0': Decimal('540.056'),
      'x1': Decimal('555.159'),
      'top': Decimal('237.946'),
      'bottom': Decimal('244.928'),
      'text': 'SAINT'},
     {'x0': Decimal('556.590'),
      'x1': Decimal('571.980'),
      'top': Decimal('237.946'),
      'bottom': Decimal('244.928'),
      'text': 'LOUIS'},
     {'x0': Decimal('573.412'),
      'x1': Decimal('584.241'),
      'top': Decimal('237.946'),
      'bottom': Decimal('244.928'),
      'text': 'AND'},
     {'x0': Decimal('585.667'),
      'x1': Decimal('607.039'),
      'top': Decimal('237.946'),
      'bottom': Decimal('244.928'),
      'text': 'RETURN'},
     {'x0': Decimal('88.617'),
      'x1': Decimal('127.119'),
      'top': Decimal('244.358'),
      'bottom': Decimal('251.340'),
      'text': 'DHAW20190004'},
     {'x0': Decimal('155.088'),
      'x1': Decimal('180.768'),
      'top': Decimal('244.358'),
      'bottom': Decimal('251.340'),
      'text': '04/03/2019'},
     {'x0': Decimal('201.881'),
      'x1': Decimal('225.543'),
      'top': Decimal('244.358'),
      'bottom': Decimal('251.340'),
      'text': 'CITIBANK'},
     {'x0': Decimal('226.975'),
      'x1': Decimal('228.683'),
      'top': Decimal('244.358'),
      'bottom': Decimal('251.340'),
      'text': '-'},
     {'x0': Decimal('230.105'),
      'x1': Decimal('250.066'),
      'top': Decimal('244.358'),
      'bottom': Decimal('251.340'),
      'text': 'TRAVEL'},
     {'x0': Decimal('251.498'),
      'x1': Decimal('262.043'),
      'top': Decimal('244.358'),
      'bottom': Decimal('251.340'),
      'text': 'CBA'},
     {'x0': Decimal('263.475'),
      'x1': Decimal('278.011'),
      'top': Decimal('244.358'),
      'bottom': Decimal('251.340'),
      'text': 'CARD'},
     {'x0': Decimal('347.317'),
      'x1': Decimal('372.997'),
      'top': Decimal('244.358'),
      'bottom': Decimal('251.340'),
      'text': '03/21/2019'},
     {'x0': Decimal('392.388'),
      'x1': Decimal('418.068'),
      'top': Decimal('244.358'),
      'bottom': Decimal('251.340'),
      'text': '03/24/2019'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('444.576'),
      'top': Decimal('244.358'),
      'bottom': Decimal('251.340'),
      'text': 'STAFF'},
     {'x0': Decimal('446.003'),
      'x1': Decimal('493.317'),
      'top': Decimal('244.358'),
      'bottom': Decimal('251.340'),
      'text': 'TRANSPORTATION'},
     {'x0': Decimal('687.430'),
      'x1': Decimal('703.123'),
      'top': Decimal('244.358'),
      'bottom': Decimal('251.340'),
      'text': '903.90'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('450.563'),
      'top': Decimal('250.404'),
      'bottom': Decimal('257.386'),
      'text': 'AIRFARE'},
     {'x0': Decimal('451.989'),
      'x1': Decimal('462.819'),
      'top': Decimal('250.404'),
      'bottom': Decimal('257.386'),
      'text': 'FOR'},
     {'x0': Decimal('464.245'),
      'x1': Decimal('467.661'),
      'top': Decimal('250.404'),
      'bottom': Decimal('257.386'),
      'text': 'K'},
     {'x0': Decimal('469.098'),
      'x1': Decimal('483.631'),
      'top': Decimal('250.404'),
      'bottom': Decimal('257.386'),
      'text': 'FORD'},
     {'x0': Decimal('485.052'),
      'x1': Decimal('495.035'),
      'top': Decimal('250.404'),
      'bottom': Decimal('257.386'),
      'text': '3/21'},
     {'x0': Decimal('496.461'),
      'x1': Decimal('531.802'),
      'top': Decimal('250.404'),
      'bottom': Decimal('257.386'),
      'text': 'WASHINGTON'},
     {'x0': Decimal('533.228'),
      'x1': Decimal('540.636'),
      'top': Decimal('250.404'),
      'bottom': Decimal('257.386'),
      'text': 'DC'},
     {'x0': Decimal('542.062'),
      'x1': Decimal('549.183'),
      'top': Decimal('250.404'),
      'bottom': Decimal('257.386'),
      'text': 'TO'},
     {'x0': Decimal('550.619'),
      'x1': Decimal('565.722'),
      'top': Decimal('250.404'),
      'bottom': Decimal('257.386'),
      'text': 'SAINT'},
     {'x0': Decimal('567.153'),
      'x1': Decimal('583.969'),
      'top': Decimal('250.404'),
      'bottom': Decimal('257.386'),
      'text': 'LOUIS,'},
     {'x0': Decimal('585.401'),
      'x1': Decimal('606.208'),
      'top': Decimal('250.404'),
      'bottom': Decimal('257.386'),
      'text': 'KANSAS'},
     {'x0': Decimal('607.634'),
      'x1': Decimal('620.741'),
      'top': Decimal('250.404'),
      'bottom': Decimal('257.386'),
      'text': 'CITY;'},
     {'x0': Decimal('622.168'),
      'x1': Decimal('632.151'),
      'top': Decimal('250.404'),
      'bottom': Decimal('257.386'),
      'text': '3/24'},
     {'x0': Decimal('633.577'),
      'x1': Decimal('648.679'),
      'top': Decimal('250.404'),
      'bottom': Decimal('257.386'),
      'text': 'SAINT'},
     {'x0': Decimal('650.111'),
      'x1': Decimal('665.501'),
      'top': Decimal('250.404'),
      'bottom': Decimal('257.386'),
      'text': 'LOUIS'},
     {'x0': Decimal('666.932'),
      'x1': Decimal('674.053'),
      'top': Decimal('250.404'),
      'bottom': Decimal('257.386'),
      'text': 'TO'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('463.666'),
      'top': Decimal('256.377'),
      'bottom': Decimal('263.359'),
      'text': 'WASHINGTON'},
     {'x0': Decimal('465.096'),
      'x1': Decimal('472.503'),
      'top': Decimal('256.377'),
      'bottom': Decimal('263.359'),
      'text': 'DC'},
     {'x0': Decimal('88.617'),
      'x1': Decimal('127.119'),
      'top': Decimal('262.277'),
      'bottom': Decimal('269.259'),
      'text': 'DHAW20190005'},
     {'x0': Decimal('155.088'),
      'x1': Decimal('180.768'),
      'top': Decimal('262.277'),
      'bottom': Decimal('269.259'),
      'text': '05/28/2019'},
     {'x0': Decimal('201.881'),
      'x1': Decimal('225.543'),
      'top': Decimal('262.277'),
      'bottom': Decimal('269.259'),
      'text': 'CITIBANK'},
     {'x0': Decimal('226.975'),
      'x1': Decimal('228.683'),
      'top': Decimal('262.277'),
      'bottom': Decimal('269.259'),
      'text': '-'},
     {'x0': Decimal('230.105'),
      'x1': Decimal('250.066'),
      'top': Decimal('262.277'),
      'bottom': Decimal('269.259'),
      'text': 'TRAVEL'},
     {'x0': Decimal('251.498'),
      'x1': Decimal('262.043'),
      'top': Decimal('262.277'),
      'bottom': Decimal('269.259'),
      'text': 'CBA'},
     {'x0': Decimal('263.475'),
      'x1': Decimal('278.011'),
      'top': Decimal('262.277'),
      'bottom': Decimal('269.259'),
      'text': 'CARD'},
     {'x0': Decimal('347.317'),
      'x1': Decimal('372.997'),
      'top': Decimal('262.277'),
      'bottom': Decimal('269.259'),
      'text': '03/21/2019'},
     {'x0': Decimal('392.388'),
      'x1': Decimal('418.068'),
      'top': Decimal('262.277'),
      'bottom': Decimal('269.259'),
      'text': '03/24/2019'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('457.530'),
      'top': Decimal('262.277'),
      'bottom': Decimal('269.259'),
      'text': "SENATOR'S"},
     {'x0': Decimal('458.961'),
      'x1': Decimal('506.275'),
      'top': Decimal('262.277'),
      'bottom': Decimal('269.259'),
      'text': 'TRANSPORTATION'},
     {'x0': Decimal('687.430'),
      'x1': Decimal('703.123'),
      'top': Decimal('262.277'),
      'bottom': Decimal('269.259'),
      'text': '798.90'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('450.563'),
      'top': Decimal('268.323'),
      'bottom': Decimal('275.305'),
      'text': 'AIRFARE'},
     {'x0': Decimal('451.989'),
      'x1': Decimal('462.819'),
      'top': Decimal('268.323'),
      'bottom': Decimal('275.305'),
      'text': 'FOR'},
     {'x0': Decimal('464.245'),
      'x1': Decimal('474.792'),
      'top': Decimal('268.323'),
      'bottom': Decimal('275.305'),
      'text': 'SEN'},
     {'x0': Decimal('476.223'),
      'x1': Decimal('497.882'),
      'top': Decimal('268.323'),
      'bottom': Decimal('275.305'),
      'text': 'HAWLEY'},
     {'x0': Decimal('499.314'),
      'x1': Decimal('506.152'),
      'top': Decimal('268.323'),
      'bottom': Decimal('275.305'),
      'text': 'AS'},
     {'x0': Decimal('507.578'),
      'x1': Decimal('534.085'),
      'top': Decimal('268.323'),
      'bottom': Decimal('275.305'),
      'text': 'FOLLOWS:'},
     {'x0': Decimal('535.521'),
      'x1': Decimal('545.504'),
      'top': Decimal('268.323'),
      'bottom': Decimal('275.305'),
      'text': '3/21'},
     {'x0': Decimal('546.931'),
      'x1': Decimal('582.271'),
      'top': Decimal('268.323'),
      'bottom': Decimal('275.305'),
      'text': 'WASHINGTON'},
     {'x0': Decimal('583.692'),
      'x1': Decimal('591.100'),
      'top': Decimal('268.323'),
      'bottom': Decimal('275.305'),
      'text': 'DC'},
     {'x0': Decimal('592.531'),
      'x1': Decimal('599.652'),
      'top': Decimal('268.323'),
      'bottom': Decimal('275.305'),
      'text': 'TO'},
     {'x0': Decimal('601.078'),
      'x1': Decimal('616.181'),
      'top': Decimal('268.323'),
      'bottom': Decimal('275.305'),
      'text': 'SAINT'},
     {'x0': Decimal('617.627'),
      'x1': Decimal('633.018'),
      'top': Decimal('268.323'),
      'bottom': Decimal('275.305'),
      'text': 'LOUIS'},
     {'x0': Decimal('634.449'),
      'x1': Decimal('641.569'),
      'top': Decimal('268.323'),
      'bottom': Decimal('275.305'),
      'text': 'TO'},
     {'x0': Decimal('643.001'),
      'x1': Decimal('663.808'),
      'top': Decimal('268.323'),
      'bottom': Decimal('275.305'),
      'text': 'KANSAS'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('441.446'),
      'top': Decimal('274.296'),
      'bottom': Decimal('281.278'),
      'text': 'CITY;'},
     {'x0': Decimal('444.299'),
      'x1': Decimal('454.285'),
      'top': Decimal('274.296'),
      'bottom': Decimal('281.278'),
      'text': '3/24'},
     {'x0': Decimal('455.713'),
      'x1': Decimal('470.820'),
      'top': Decimal('274.296'),
      'bottom': Decimal('281.278'),
      'text': 'SAINT'},
     {'x0': Decimal('472.252'),
      'x1': Decimal('487.646'),
      'top': Decimal('274.296'),
      'bottom': Decimal('281.278'),
      'text': 'LOUIS'},
     {'x0': Decimal('489.073'),
      'x1': Decimal('496.195'),
      'top': Decimal('274.296'),
      'bottom': Decimal('281.278'),
      'text': 'TO'},
     {'x0': Decimal('497.617'),
      'x1': Decimal('532.967'),
      'top': Decimal('274.296'),
      'bottom': Decimal('281.278'),
      'text': 'WASHINGTON'},
     {'x0': Decimal('534.394'),
      'x1': Decimal('541.803'),
      'top': Decimal('274.296'),
      'bottom': Decimal('281.278'),
      'text': 'DC'},
     {'x0': Decimal('88.617'),
      'x1': Decimal('127.119'),
      'top': Decimal('280.195'),
      'bottom': Decimal('287.177'),
      'text': 'DHAW20190026'},
     {'x0': Decimal('155.088'),
      'x1': Decimal('180.768'),
      'top': Decimal('280.195'),
      'bottom': Decimal('287.177'),
      'text': '05/03/2019'},
     {'x0': Decimal('201.881'),
      'x1': Decimal('225.543'),
      'top': Decimal('280.195'),
      'bottom': Decimal('287.177'),
      'text': 'CITIBANK'},
     {'x0': Decimal('226.975'),
      'x1': Decimal('228.683'),
      'top': Decimal('280.195'),
      'bottom': Decimal('287.177'),
      'text': '-'},
     {'x0': Decimal('230.105'),
      'x1': Decimal('250.066'),
      'top': Decimal('280.195'),
      'bottom': Decimal('287.177'),
      'text': 'TRAVEL'},
     {'x0': Decimal('251.498'),
      'x1': Decimal('262.043'),
      'top': Decimal('280.195'),
      'bottom': Decimal('287.177'),
      'text': 'CBA'},
     {'x0': Decimal('263.475'),
      'x1': Decimal('278.011'),
      'top': Decimal('280.195'),
      'bottom': Decimal('287.177'),
      'text': 'CARD'},
     {'x0': Decimal('347.317'),
      'x1': Decimal('372.997'),
      'top': Decimal('280.195'),
      'bottom': Decimal('287.177'),
      'text': '04/16/2019'},
     {'x0': Decimal('392.388'),
      'x1': Decimal('418.068'),
      'top': Decimal('280.195'),
      'bottom': Decimal('287.177'),
      'text': '04/17/2019'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('444.576'),
      'top': Decimal('280.195'),
      'bottom': Decimal('287.177'),
      'text': 'STAFF'},
     {'x0': Decimal('446.003'),
      'x1': Decimal('493.317'),
      'top': Decimal('280.195'),
      'bottom': Decimal('287.177'),
      'text': 'TRANSPORTATION'},
     {'x0': Decimal('687.430'),
      'x1': Decimal('703.123'),
      'top': Decimal('280.195'),
      'bottom': Decimal('287.177'),
      'text': '521.00'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('450.563'),
      'top': Decimal('286.168'),
      'bottom': Decimal('293.150'),
      'text': 'AIRFARE'},
     {'x0': Decimal('451.989'),
      'x1': Decimal('462.819'),
      'top': Decimal('286.168'),
      'bottom': Decimal('293.150'),
      'text': 'FOR'},
     {'x0': Decimal('464.245'),
      'x1': Decimal('468.518'),
      'top': Decimal('286.168'),
      'bottom': Decimal('293.150'),
      'text': 'M'},
     {'x0': Decimal('469.944'),
      'x1': Decimal('484.478'),
      'top': Decimal('286.168'),
      'bottom': Decimal('293.150'),
      'text': 'BERG'},
     {'x0': Decimal('485.904'),
      'x1': Decimal('521.245'),
      'top': Decimal('286.168'),
      'bottom': Decimal('293.150'),
      'text': 'WASHINGTON'},
     {'x0': Decimal('522.671'),
      'x1': Decimal('530.078'),
      'top': Decimal('286.168'),
      'bottom': Decimal('293.150'),
      'text': 'DC'},
     {'x0': Decimal('531.505'),
      'x1': Decimal('538.625'),
      'top': Decimal('286.168'),
      'bottom': Decimal('293.150'),
      'text': 'TO'},
     {'x0': Decimal('540.056'),
      'x1': Decimal('574.263'),
      'top': Decimal('286.168'),
      'bottom': Decimal('293.150'),
      'text': 'SPRINGFIELD'},
     {'x0': Decimal('575.689'),
      'x1': Decimal('586.519'),
      'top': Decimal('286.168'),
      'bottom': Decimal('293.150'),
      'text': 'AND'},
     {'x0': Decimal('587.945'),
      'x1': Decimal('609.317'),
      'top': Decimal('286.168'),
      'bottom': Decimal('293.150'),
      'text': 'RETURN'},
     {'x0': Decimal('731.069'),
      'x1': Decimal('748.894'),
      'top': Decimal('286.616'),
      'bottom': Decimal('295.150'),
      'text': 'B'},
     {'x0': Decimal('88.617'),
      'x1': Decimal('127.119'),
      'top': Decimal('292.581'),
      'bottom': Decimal('299.562'),
      'text': 'DHAW20190027'},
     {'x0': Decimal('155.088'),
      'x1': Decimal('180.768'),
      'top': Decimal('292.581'),
      'bottom': Decimal('299.562'),
      'text': '05/02/2019'},
     {'x0': Decimal('201.881'),
      'x1': Decimal('225.543'),
      'top': Decimal('292.581'),
      'bottom': Decimal('299.562'),
      'text': 'CITIBANK'},
     {'x0': Decimal('226.975'),
      'x1': Decimal('228.683'),
      'top': Decimal('292.581'),
      'bottom': Decimal('299.562'),
      'text': '-'},
     {'x0': Decimal('230.105'),
      'x1': Decimal('250.066'),
      'top': Decimal('292.581'),
      'bottom': Decimal('299.562'),
      'text': 'TRAVEL'},
     {'x0': Decimal('251.498'),
      'x1': Decimal('262.043'),
      'top': Decimal('292.581'),
      'bottom': Decimal('299.562'),
      'text': 'CBA'},
     {'x0': Decimal('263.475'),
      'x1': Decimal('278.011'),
      'top': Decimal('292.581'),
      'bottom': Decimal('299.562'),
      'text': 'CARD'},
     {'x0': Decimal('347.317'),
      'x1': Decimal('372.997'),
      'top': Decimal('292.581'),
      'bottom': Decimal('299.562'),
      'text': '04/15/2019'},
     {'x0': Decimal('392.388'),
      'x1': Decimal('418.068'),
      'top': Decimal('292.581'),
      'bottom': Decimal('299.562'),
      'text': '04/18/2019'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('444.576'),
      'top': Decimal('292.581'),
      'bottom': Decimal('299.562'),
      'text': 'STAFF'},
     {'x0': Decimal('446.003'),
      'x1': Decimal('493.317'),
      'top': Decimal('292.581'),
      'bottom': Decimal('299.562'),
      'text': 'TRANSPORTATION'},
     {'x0': Decimal('687.430'),
      'x1': Decimal('703.123'),
      'top': Decimal('292.581'),
      'bottom': Decimal('299.562'),
      'text': '349.60'},
     {'x0': Decimal('731.069'),
      'x1': Decimal('748.894'),
      'top': Decimal('295.150'),
      'bottom': Decimal('299.086'),
      'text': '-'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('450.563'),
      'top': Decimal('298.553'),
      'bottom': Decimal('305.535'),
      'text': 'AIRFARE'},
     {'x0': Decimal('451.989'),
      'x1': Decimal('462.819'),
      'top': Decimal('298.553'),
      'bottom': Decimal('305.535'),
      'text': 'FOR'},
     {'x0': Decimal('464.245'),
      'x1': Decimal('467.949'),
      'top': Decimal('298.553'),
      'bottom': Decimal('305.535'),
      'text': 'R'},
     {'x0': Decimal('469.375'),
      'x1': Decimal('490.182'),
      'top': Decimal('298.553'),
      'bottom': Decimal('305.535'),
      'text': 'LEAVITT'},
     {'x0': Decimal('491.608'),
      'x1': Decimal('526.949'),
      'top': Decimal('298.553'),
      'bottom': Decimal('305.535'),
      'text': 'WASHINGTON'},
     {'x0': Decimal('528.375'),
      'x1': Decimal('535.783'),
      'top': Decimal('298.553'),
      'bottom': Decimal('305.535'),
      'text': 'DC'},
     {'x0': Decimal('537.214'),
      'x1': Decimal('544.335'),
      'top': Decimal('298.553'),
      'bottom': Decimal('305.535'),
      'text': 'TO'},
     {'x0': Decimal('545.761'),
      'x1': Decimal('566.568'),
      'top': Decimal('298.553'),
      'bottom': Decimal('305.535'),
      'text': 'KANSAS'},
     {'x0': Decimal('568.005'),
      'x1': Decimal('581.112'),
      'top': Decimal('298.553'),
      'bottom': Decimal('305.535'),
      'text': 'CITY,'},
     {'x0': Decimal('582.538'),
      'x1': Decimal('597.641'),
      'top': Decimal('298.553'),
      'bottom': Decimal('305.535'),
      'text': 'SAINT'},
     {'x0': Decimal('599.072'),
      'x1': Decimal('614.462'),
      'top': Decimal('298.553'),
      'bottom': Decimal('305.535'),
      'text': 'LOUIS'},
     {'x0': Decimal('615.904'),
      'x1': Decimal('626.733'),
      'top': Decimal('298.553'),
      'bottom': Decimal('305.535'),
      'text': 'AND'},
     {'x0': Decimal('628.159'),
      'x1': Decimal('649.531'),
      'top': Decimal('298.553'),
      'bottom': Decimal('305.535'),
      'text': 'RETURN'},
     {'x0': Decimal('731.069'),
      'x1': Decimal('748.894'),
      'top': Decimal('299.086'),
      'bottom': Decimal('305.658'),
      'text': '1'},
     {'x0': Decimal('88.617'),
      'x1': Decimal('127.119'),
      'top': Decimal('304.966'),
      'bottom': Decimal('311.948'),
      'text': 'DHAW20190029'},
     {'x0': Decimal('155.088'),
      'x1': Decimal('180.768'),
      'top': Decimal('304.966'),
      'bottom': Decimal('311.948'),
      'text': '05/16/2019'},
     {'x0': Decimal('201.881'),
      'x1': Decimal('225.543'),
      'top': Decimal('304.966'),
      'bottom': Decimal('311.948'),
      'text': 'CITIBANK'},
     {'x0': Decimal('226.975'),
      'x1': Decimal('228.683'),
      'top': Decimal('304.966'),
      'bottom': Decimal('311.948'),
      'text': '-'},
     {'x0': Decimal('230.105'),
      'x1': Decimal('250.066'),
      'top': Decimal('304.966'),
      'bottom': Decimal('311.948'),
      'text': 'TRAVEL'},
     {'x0': Decimal('251.498'),
      'x1': Decimal('262.043'),
      'top': Decimal('304.966'),
      'bottom': Decimal('311.948'),
      'text': 'CBA'},
     {'x0': Decimal('263.475'),
      'x1': Decimal('278.011'),
      'top': Decimal('304.966'),
      'bottom': Decimal('311.948'),
      'text': 'CARD'},
     {'x0': Decimal('347.317'),
      'x1': Decimal('372.997'),
      'top': Decimal('304.966'),
      'bottom': Decimal('311.948'),
      'text': '05/07/2019'},
     {'x0': Decimal('392.388'),
      'x1': Decimal('418.068'),
      'top': Decimal('304.966'),
      'bottom': Decimal('311.948'),
      'text': '05/09/2019'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('444.576'),
      'top': Decimal('304.966'),
      'bottom': Decimal('311.948'),
      'text': 'STAFF'},
     {'x0': Decimal('446.003'),
      'x1': Decimal('493.317'),
      'top': Decimal('304.966'),
      'bottom': Decimal('311.948'),
      'text': 'TRANSPORTATION'},
     {'x0': Decimal('687.430'),
      'x1': Decimal('703.123'),
      'top': Decimal('304.966'),
      'bottom': Decimal('311.948'),
      'text': '477.60'},
     {'x0': Decimal('731.069'),
      'x1': Decimal('748.894'),
      'top': Decimal('305.658'),
      'bottom': Decimal('312.231'),
      'text': '1'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('450.563'),
      'top': Decimal('310.939'),
      'bottom': Decimal('317.921'),
      'text': 'AIRFARE'},
     {'x0': Decimal('451.991'),
      'x1': Decimal('462.819'),
      'top': Decimal('310.939'),
      'bottom': Decimal('317.921'),
      'text': 'FOR'},
     {'x0': Decimal('464.243'),
      'x1': Decimal('467.947'),
      'top': Decimal('310.939'),
      'bottom': Decimal('317.921'),
      'text': 'D'},
     {'x0': Decimal('469.374'),
      'x1': Decimal('494.738'),
      'top': Decimal('310.939'),
      'bottom': Decimal('317.921'),
      'text': 'HARTMAN'},
     {'x0': Decimal('496.170'),
      'x1': Decimal('511.272'),
      'top': Decimal('310.939'),
      'bottom': Decimal('317.921'),
      'text': 'SAINT'},
     {'x0': Decimal('512.702'),
      'x1': Decimal('528.092'),
      'top': Decimal('310.939'),
      'bottom': Decimal('317.921'),
      'text': 'LOUIS'},
     {'x0': Decimal('529.521'),
      'x1': Decimal('537.781'),
      'top': Decimal('310.939'),
      'bottom': Decimal('317.921'),
      'text': 'MO'},
     {'x0': Decimal('539.209'),
      'x1': Decimal('546.328'),
      'top': Decimal('310.939'),
      'bottom': Decimal('317.921'),
      'text': 'TO'},
     {'x0': Decimal('547.760'),
      'x1': Decimal('583.097'),
      'top': Decimal('310.939'),
      'bottom': Decimal('317.921'),
      'text': 'WASHINGTON'},
     {'x0': Decimal('584.518'),
      'x1': Decimal('591.927'),
      'top': Decimal('310.939'),
      'bottom': Decimal('317.921'),
      'text': 'DC'},
     {'x0': Decimal('593.358'),
      'x1': Decimal('604.188'),
      'top': Decimal('310.939'),
      'bottom': Decimal('317.921'),
      'text': 'AND'},
     {'x0': Decimal('605.613'),
      'x1': Decimal('626.987'),
      'top': Decimal('310.939'),
      'bottom': Decimal('317.921'),
      'text': 'RETURN'},
     {'x0': Decimal('731.069'),
      'x1': Decimal('748.894'),
      'top': Decimal('312.231'),
      'bottom': Decimal('318.803'),
      'text': '9'},
     {'x0': Decimal('88.617'),
      'x1': Decimal('127.119'),
      'top': Decimal('317.351'),
      'bottom': Decimal('324.333'),
      'text': 'DHAW20190031'},
     {'x0': Decimal('155.088'),
      'x1': Decimal('180.768'),
      'top': Decimal('317.351'),
      'bottom': Decimal('324.333'),
      'text': '05/28/2019'},
     {'x0': Decimal('201.881'),
      'x1': Decimal('225.543'),
      'top': Decimal('317.351'),
      'bottom': Decimal('324.333'),
      'text': 'CITIBANK'},
     {'x0': Decimal('226.975'),
      'x1': Decimal('228.683'),
      'top': Decimal('317.351'),
      'bottom': Decimal('324.333'),
      'text': '-'},
     {'x0': Decimal('230.105'),
      'x1': Decimal('254.910'),
      'top': Decimal('317.351'),
      'bottom': Decimal('324.333'),
      'text': 'SENATOR'},
     {'x0': Decimal('256.342'),
      'x1': Decimal('264.609'),
      'top': Decimal('317.351'),
      'bottom': Decimal('324.333'),
      'text': 'IBA'},
     {'x0': Decimal('266.031'),
      'x1': Decimal('280.567'),
      'top': Decimal('317.351'),
      'bottom': Decimal('324.333'),
      'text': 'CARD'},
     {'x0': Decimal('347.317'),
      'x1': Decimal('372.997'),
      'top': Decimal('317.351'),
      'bottom': Decimal('324.333'),
      'text': '05/10/2019'},
     {'x0': Decimal('392.388'),
      'x1': Decimal('418.068'),
      'top': Decimal('317.351'),
      'bottom': Decimal('324.333'),
      'text': '05/11/2019'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('457.530'),
      'top': Decimal('317.351'),
      'bottom': Decimal('324.333'),
      'text': "SENATOR'S"},
     {'x0': Decimal('458.961'),
      'x1': Decimal('506.275'),
      'top': Decimal('317.351'),
      'bottom': Decimal('324.333'),
      'text': 'TRANSPORTATION'},
     {'x0': Decimal('687.430'),
      'x1': Decimal('703.123'),
      'top': Decimal('317.351'),
      'bottom': Decimal('324.333'),
      'text': '618.00'},
     {'x0': Decimal('731.069'),
      'x1': Decimal('748.894'),
      'top': Decimal('318.803'),
      'bottom': Decimal('325.375'),
      'text': '1'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('443.721'),
      'top': Decimal('323.324'),
      'bottom': Decimal('330.306'),
      'text': 'TRAIN'},
     {'x0': Decimal('445.146'),
      'x1': Decimal('458.819'),
      'top': Decimal('323.324'),
      'bottom': Decimal('330.306'),
      'text': 'FARE'},
     {'x0': Decimal('460.255'),
      'x1': Decimal('471.082'),
      'top': Decimal('323.324'),
      'bottom': Decimal('330.306'),
      'text': 'FOR'},
     {'x0': Decimal('472.507'),
      'x1': Decimal('483.053'),
      'top': Decimal('323.324'),
      'bottom': Decimal('330.306'),
      'text': 'SEN'},
     {'x0': Decimal('484.483'),
      'x1': Decimal('506.137'),
      'top': Decimal('323.324'),
      'bottom': Decimal('330.306'),
      'text': 'HAWLEY'},
     {'x0': Decimal('507.562'),
      'x1': Decimal('542.893'),
      'top': Decimal('323.324'),
      'bottom': Decimal('330.306'),
      'text': 'WASHINGTON'},
     {'x0': Decimal('544.324'),
      'x1': Decimal('551.730'),
      'top': Decimal('323.324'),
      'bottom': Decimal('330.306'),
      'text': 'DC'},
     {'x0': Decimal('553.155'),
      'x1': Decimal('560.275'),
      'top': Decimal('323.324'),
      'bottom': Decimal('330.306'),
      'text': 'TO'},
     {'x0': Decimal('561.705'),
      'x1': Decimal('573.666'),
      'top': Decimal('323.324'),
      'bottom': Decimal('330.306'),
      'text': 'NEW'},
     {'x0': Decimal('575.102'),
      'x1': Decimal('589.632'),
      'top': Decimal('323.324'),
      'bottom': Decimal('330.306'),
      'text': 'YORK'},
     {'x0': Decimal('591.062'),
      'x1': Decimal('598.182'),
      'top': Decimal('323.324'),
      'bottom': Decimal('330.306'),
      'text': 'NY'},
     {'x0': Decimal('599.612'),
      'x1': Decimal('610.439'),
      'top': Decimal('323.324'),
      'bottom': Decimal('330.306'),
      'text': 'AND'},
     {'x0': Decimal('611.864'),
      'x1': Decimal('633.231'),
      'top': Decimal('323.324'),
      'bottom': Decimal('330.306'),
      'text': 'RETURN'},
     {'x0': Decimal('88.617'),
      'x1': Decimal('127.119'),
      'top': Decimal('329.737'),
      'bottom': Decimal('336.719'),
      'text': 'DHAW20190032'},
     {'x0': Decimal('155.088'),
      'x1': Decimal('180.768'),
      'top': Decimal('329.737'),
      'bottom': Decimal('336.719'),
      'text': '06/13/2019'},
     {'x0': Decimal('201.881'),
      'x1': Decimal('225.543'),
      'top': Decimal('329.737'),
      'bottom': Decimal('336.719'),
      'text': 'CITIBANK'},
     {'x0': Decimal('226.975'),
      'x1': Decimal('228.683'),
      'top': Decimal('329.737'),
      'bottom': Decimal('336.719'),
      'text': '-'},
     {'x0': Decimal('230.105'),
      'x1': Decimal('254.910'),
      'top': Decimal('329.737'),
      'bottom': Decimal('336.719'),
      'text': 'SENATOR'},
     {'x0': Decimal('256.342'),
      'x1': Decimal('264.609'),
      'top': Decimal('329.737'),
      'bottom': Decimal('336.719'),
      'text': 'IBA'},
     {'x0': Decimal('266.031'),
      'x1': Decimal('280.567'),
      'top': Decimal('329.737'),
      'bottom': Decimal('336.719'),
      'text': 'CARD'},
     {'x0': Decimal('347.317'),
      'x1': Decimal('372.997'),
      'top': Decimal('329.737'),
      'bottom': Decimal('336.719'),
      'text': '05/24/2019'},
     {'x0': Decimal('392.388'),
      'x1': Decimal('418.068'),
      'top': Decimal('329.737'),
      'bottom': Decimal('336.719'),
      'text': '05/25/2019'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('457.530'),
      'top': Decimal('329.737'),
      'bottom': Decimal('336.719'),
      'text': "SENATOR'S"},
     {'x0': Decimal('458.961'),
      'x1': Decimal('506.275'),
      'top': Decimal('329.737'),
      'bottom': Decimal('336.719'),
      'text': 'TRANSPORTATION'},
     {'x0': Decimal('687.430'),
      'x1': Decimal('703.123'),
      'top': Decimal('329.737'),
      'bottom': Decimal('336.719'),
      'text': '553.30'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('450.563'),
      'top': Decimal('335.783'),
      'bottom': Decimal('342.765'),
      'text': 'AIRFARE'},
     {'x0': Decimal('451.991'),
      'x1': Decimal('462.819'),
      'top': Decimal('335.783'),
      'bottom': Decimal('342.765'),
      'text': 'FOR'},
     {'x0': Decimal('464.243'),
      'x1': Decimal('474.791'),
      'top': Decimal('335.783'),
      'bottom': Decimal('342.765'),
      'text': 'SEN'},
     {'x0': Decimal('476.219'),
      'x1': Decimal('497.879'),
      'top': Decimal('335.783'),
      'bottom': Decimal('342.765'),
      'text': 'HAWLEY'},
     {'x0': Decimal('499.313'),
      'x1': Decimal('534.650'),
      'top': Decimal('335.783'),
      'bottom': Decimal('342.765'),
      'text': 'WASHINGTON'},
     {'x0': Decimal('536.071'),
      'x1': Decimal('543.480'),
      'top': Decimal('335.783'),
      'bottom': Decimal('342.765'),
      'text': 'DC'},
     {'x0': Decimal('544.911'),
      'x1': Decimal('552.030'),
      'top': Decimal('335.783'),
      'bottom': Decimal('342.765'),
      'text': 'TO'},
     {'x0': Decimal('553.454'),
      'x1': Decimal('587.671'),
      'top': Decimal('335.783'),
      'bottom': Decimal('342.765'),
      'text': 'SPRINGFIELD'},
     {'x0': Decimal('589.100'),
      'x1': Decimal('598.785'),
      'top': Decimal('335.783'),
      'bottom': Decimal('342.765'),
      'text': 'MO,'},
     {'x0': Decimal('600.208'),
      'x1': Decimal('615.311'),
      'top': Decimal('335.783'),
      'bottom': Decimal('342.765'),
      'text': 'SAINT'},
     {'x0': Decimal('616.741'),
      'x1': Decimal('632.131'),
      'top': Decimal('335.783'),
      'bottom': Decimal('342.765'),
      'text': 'LOUIS'},
     {'x0': Decimal('633.560'),
      'x1': Decimal('641.820'),
      'top': Decimal('335.783'),
      'bottom': Decimal('342.765'),
      'text': 'MO'},
     {'x0': Decimal('643.248'),
      'x1': Decimal('654.078'),
      'top': Decimal('335.783'),
      'bottom': Decimal('342.765'),
      'text': 'AND'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('449.712'),
      'top': Decimal('341.755'),
      'bottom': Decimal('348.737'),
      'text': 'RETURN'},
     {'x0': Decimal('88.617'),
      'x1': Decimal('127.119'),
      'top': Decimal('347.655'),
      'bottom': Decimal('354.637'),
      'text': 'DHAW20190033'},
     {'x0': Decimal('155.088'),
      'x1': Decimal('180.768'),
      'top': Decimal('347.655'),
      'bottom': Decimal('354.637'),
      'text': '06/04/2019'},
     {'x0': Decimal('201.881'),
      'x1': Decimal('225.543'),
      'top': Decimal('347.655'),
      'bottom': Decimal('354.637'),
      'text': 'CITIBANK'},
     {'x0': Decimal('226.975'),
      'x1': Decimal('228.683'),
      'top': Decimal('347.655'),
      'bottom': Decimal('354.637'),
      'text': '-'},
     {'x0': Decimal('230.105'),
      'x1': Decimal('250.066'),
      'top': Decimal('347.655'),
      'bottom': Decimal('354.637'),
      'text': 'TRAVEL'},
     {'x0': Decimal('251.498'),
      'x1': Decimal('262.043'),
      'top': Decimal('347.655'),
      'bottom': Decimal('354.637'),
      'text': 'CBA'},
     {'x0': Decimal('263.475'),
      'x1': Decimal('278.011'),
      'top': Decimal('347.655'),
      'bottom': Decimal('354.637'),
      'text': 'CARD'},
     {'x0': Decimal('347.317'),
      'x1': Decimal('372.997'),
      'top': Decimal('347.655'),
      'bottom': Decimal('354.637'),
      'text': '05/24/2019'},
     {'x0': Decimal('392.388'),
      'x1': Decimal('418.068'),
      'top': Decimal('347.655'),
      'bottom': Decimal('354.637'),
      'text': '05/25/2019'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('444.576'),
      'top': Decimal('347.655'),
      'bottom': Decimal('354.637'),
      'text': 'STAFF'},
     {'x0': Decimal('446.003'),
      'x1': Decimal('493.317'),
      'top': Decimal('347.655'),
      'bottom': Decimal('354.637'),
      'text': 'TRANSPORTATION'},
     {'x0': Decimal('687.430'),
      'x1': Decimal('703.123'),
      'top': Decimal('347.655'),
      'bottom': Decimal('354.637'),
      'text': '601.30'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('450.563'),
      'top': Decimal('353.628'),
      'bottom': Decimal('360.610'),
      'text': 'AIRFARE'},
     {'x0': Decimal('451.989'),
      'x1': Decimal('462.819'),
      'top': Decimal('353.628'),
      'bottom': Decimal('360.610'),
      'text': 'FOR'},
     {'x0': Decimal('464.245'),
      'x1': Decimal('468.518'),
      'top': Decimal('353.628'),
      'bottom': Decimal('360.610'),
      'text': 'M'},
     {'x0': Decimal('469.944'),
      'x1': Decimal('484.478'),
      'top': Decimal('353.628'),
      'bottom': Decimal('360.610'),
      'text': 'BERG'},
     {'x0': Decimal('485.904'),
      'x1': Decimal('521.245'),
      'top': Decimal('353.628'),
      'bottom': Decimal('360.610'),
      'text': 'WASHINGTON'},
     {'x0': Decimal('522.671'),
      'x1': Decimal('530.078'),
      'top': Decimal('353.628'),
      'bottom': Decimal('360.610'),
      'text': 'DC'},
     {'x0': Decimal('531.505'),
      'x1': Decimal('538.625'),
      'top': Decimal('353.628'),
      'bottom': Decimal('360.610'),
      'text': 'TO'},
     {'x0': Decimal('540.056'),
      'x1': Decimal('575.684'),
      'top': Decimal('353.628'),
      'bottom': Decimal('360.610'),
      'text': 'SPRINGFIELD,'},
     {'x0': Decimal('577.111'),
      'x1': Decimal('585.088'),
      'top': Decimal('353.628'),
      'bottom': Decimal('360.610'),
      'text': 'ST.'},
     {'x0': Decimal('586.534'),
      'x1': Decimal('601.924'),
      'top': Decimal('353.628'),
      'bottom': Decimal('360.610'),
      'text': 'LOUIS'},
     {'x0': Decimal('603.356'),
      'x1': Decimal('614.185'),
      'top': Decimal('353.628'),
      'bottom': Decimal('360.610'),
      'text': 'AND'},
     {'x0': Decimal('615.616'),
      'x1': Decimal('636.988'),
      'top': Decimal('353.628'),
      'bottom': Decimal('360.610'),
      'text': 'RETURN'},
     {'x0': Decimal('88.617'),
      'x1': Decimal('127.119'),
      'top': Decimal('360.040'),
      'bottom': Decimal('367.022'),
      'text': 'DHAW20190034'},
     {'x0': Decimal('155.088'),
      'x1': Decimal('180.768'),
      'top': Decimal('360.040'),
      'bottom': Decimal('367.022'),
      'text': '06/04/2019'},
     {'x0': Decimal('201.881'),
      'x1': Decimal('225.543'),
      'top': Decimal('360.040'),
      'bottom': Decimal('367.022'),
      'text': 'CITIBANK'},
     {'x0': Decimal('226.975'),
      'x1': Decimal('228.683'),
      'top': Decimal('360.040'),
      'bottom': Decimal('367.022'),
      'text': '-'},
     {'x0': Decimal('230.105'),
      'x1': Decimal('250.066'),
      'top': Decimal('360.040'),
      'bottom': Decimal('367.022'),
      'text': 'TRAVEL'},
     {'x0': Decimal('251.498'),
      'x1': Decimal('262.043'),
      'top': Decimal('360.040'),
      'bottom': Decimal('367.022'),
      'text': 'CBA'},
     {'x0': Decimal('263.475'),
      'x1': Decimal('278.011'),
      'top': Decimal('360.040'),
      'bottom': Decimal('367.022'),
      'text': 'CARD'},
     {'x0': Decimal('347.317'),
      'x1': Decimal('372.997'),
      'top': Decimal('360.040'),
      'bottom': Decimal('367.022'),
      'text': '05/24/2019'},
     {'x0': Decimal('392.388'),
      'x1': Decimal('418.068'),
      'top': Decimal('360.040'),
      'bottom': Decimal('367.022'),
      'text': '05/25/2019'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('444.576'),
      'top': Decimal('360.040'),
      'bottom': Decimal('367.022'),
      'text': 'STAFF'},
     {'x0': Decimal('446.003'),
      'x1': Decimal('493.317'),
      'top': Decimal('360.040'),
      'bottom': Decimal('367.022'),
      'text': 'TRANSPORTATION'},
     {'x0': Decimal('687.430'),
      'x1': Decimal('703.123'),
      'top': Decimal('360.040'),
      'bottom': Decimal('367.022'),
      'text': '601.30'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('450.563'),
      'top': Decimal('366.013'),
      'bottom': Decimal('372.995'),
      'text': 'AIRFARE'},
     {'x0': Decimal('451.989'),
      'x1': Decimal('462.819'),
      'top': Decimal('366.013'),
      'bottom': Decimal('372.995'),
      'text': 'FOR'},
     {'x0': Decimal('464.245'),
      'x1': Decimal('467.949'),
      'top': Decimal('366.013'),
      'bottom': Decimal('372.995'),
      'text': 'R'},
     {'x0': Decimal('469.375'),
      'x1': Decimal('497.595'),
      'top': Decimal('366.013'),
      'bottom': Decimal('372.995'),
      'text': 'BURLESON'},
     {'x0': Decimal('499.026'),
      'x1': Decimal('534.367'),
      'top': Decimal('366.013'),
      'bottom': Decimal('372.995'),
      'text': 'WASHINGTON'},
     {'x0': Decimal('535.788'),
      'x1': Decimal('543.196'),
      'top': Decimal('366.013'),
      'bottom': Decimal('372.995'),
      'text': 'DC'},
     {'x0': Decimal('544.627'),
      'x1': Decimal('551.748'),
      'top': Decimal('366.013'),
      'bottom': Decimal('372.995'),
      'text': 'TO'},
     {'x0': Decimal('553.174'),
      'x1': Decimal('588.802'),
      'top': Decimal('366.013'),
      'bottom': Decimal('372.995'),
      'text': 'SPRINGFIELD,'},
     {'x0': Decimal('590.233'),
      'x1': Decimal('598.221'),
      'top': Decimal('366.013'),
      'bottom': Decimal('372.995'),
      'text': 'ST.'},
     {'x0': Decimal('599.652'),
      'x1': Decimal('615.042'),
      'top': Decimal('366.013'),
      'bottom': Decimal('372.995'),
      'text': 'LOUIS'},
     {'x0': Decimal('616.473'),
      'x1': Decimal('627.303'),
      'top': Decimal('366.013'),
      'bottom': Decimal('372.995'),
      'text': 'AND'},
     {'x0': Decimal('628.734'),
      'x1': Decimal('650.106'),
      'top': Decimal('366.013'),
      'bottom': Decimal('372.995'),
      'text': 'RETURN'},
     {'x0': Decimal('88.617'),
      'x1': Decimal('127.119'),
      'top': Decimal('372.426'),
      'bottom': Decimal('379.408'),
      'text': 'DHAW20190040'},
     {'x0': Decimal('155.088'),
      'x1': Decimal('180.768'),
      'top': Decimal('372.426'),
      'bottom': Decimal('379.408'),
      'text': '06/04/2019'},
     {'x0': Decimal('201.881'),
      'x1': Decimal('225.543'),
      'top': Decimal('372.426'),
      'bottom': Decimal('379.408'),
      'text': 'CITIBANK'},
     {'x0': Decimal('226.975'),
      'x1': Decimal('228.683'),
      'top': Decimal('372.426'),
      'bottom': Decimal('379.408'),
      'text': '-'},
     {'x0': Decimal('230.105'),
      'x1': Decimal('250.066'),
      'top': Decimal('372.426'),
      'bottom': Decimal('379.408'),
      'text': 'TRAVEL'},
     {'x0': Decimal('251.498'),
      'x1': Decimal('262.043'),
      'top': Decimal('372.426'),
      'bottom': Decimal('379.408'),
      'text': 'CBA'},
     {'x0': Decimal('263.475'),
      'x1': Decimal('278.011'),
      'top': Decimal('372.426'),
      'bottom': Decimal('379.408'),
      'text': 'CARD'},
     {'x0': Decimal('347.317'),
      'x1': Decimal('372.997'),
      'top': Decimal('372.426'),
      'bottom': Decimal('379.408'),
      'text': '05/29/2019'},
     {'x0': Decimal('392.388'),
      'x1': Decimal('418.068'),
      'top': Decimal('372.426'),
      'bottom': Decimal('379.408'),
      'text': '05/31/2019'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('444.576'),
      'top': Decimal('372.426'),
      'bottom': Decimal('379.408'),
      'text': 'STAFF'},
     {'x0': Decimal('446.003'),
      'x1': Decimal('493.317'),
      'top': Decimal('372.426'),
      'bottom': Decimal('379.408'),
      'text': 'TRANSPORTATION'},
     {'x0': Decimal('687.430'),
      'x1': Decimal('703.123'),
      'top': Decimal('372.426'),
      'bottom': Decimal('379.408'),
      'text': '304.30'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('450.563'),
      'top': Decimal('378.398'),
      'bottom': Decimal('385.380'),
      'text': 'AIRFARE'},
     {'x0': Decimal('451.989'),
      'x1': Decimal('462.819'),
      'top': Decimal('378.398'),
      'bottom': Decimal('385.380'),
      'text': 'FOR'},
     {'x0': Decimal('464.245'),
      'x1': Decimal('466.810'),
      'top': Decimal('378.398'),
      'bottom': Decimal('385.380'),
      'text': 'J'},
     {'x0': Decimal('468.241'),
      'x1': Decimal('485.627'),
      'top': Decimal('378.398'),
      'bottom': Decimal('385.380'),
      'text': 'RESES'},
     {'x0': Decimal('487.053'),
      'x1': Decimal('522.394'),
      'top': Decimal('378.398'),
      'bottom': Decimal('385.380'),
      'text': 'WASHINGTON'},
     {'x0': Decimal('523.820'),
      'x1': Decimal('531.228'),
      'top': Decimal('378.398'),
      'bottom': Decimal('385.380'),
      'text': 'DC'},
     {'x0': Decimal('532.654'),
      'x1': Decimal('539.774'),
      'top': Decimal('378.398'),
      'bottom': Decimal('385.380'),
      'text': 'TO'},
     {'x0': Decimal('541.205'),
      'x1': Decimal('562.013'),
      'top': Decimal('378.398'),
      'bottom': Decimal('385.380'),
      'text': 'KANSAS'},
     {'x0': Decimal('563.449'),
      'x1': Decimal('575.130'),
      'top': Decimal('378.398'),
      'bottom': Decimal('385.380'),
      'text': 'CITY'},
     {'x0': Decimal('576.551'),
      'x1': Decimal('587.381'),
      'top': Decimal('378.398'),
      'bottom': Decimal('385.380'),
      'text': 'AND'},
     {'x0': Decimal('588.812'),
      'x1': Decimal('610.184'),
      'top': Decimal('378.398'),
      'bottom': Decimal('385.380'),
      'text': 'RETURN'},
     {'x0': Decimal('88.617'),
      'x1': Decimal('127.119'),
      'top': Decimal('384.811'),
      'bottom': Decimal('391.793'),
      'text': 'DHAW20190041'},
     {'x0': Decimal('155.088'),
      'x1': Decimal('180.768'),
      'top': Decimal('384.811'),
      'bottom': Decimal('391.793'),
      'text': '06/13/2019'},
     {'x0': Decimal('201.881'),
      'x1': Decimal('225.543'),
      'top': Decimal('384.811'),
      'bottom': Decimal('391.793'),
      'text': 'CITIBANK'},
     {'x0': Decimal('226.975'),
      'x1': Decimal('228.683'),
      'top': Decimal('384.811'),
      'bottom': Decimal('391.793'),
      'text': '-'},
     {'x0': Decimal('230.105'),
      'x1': Decimal('250.066'),
      'top': Decimal('384.811'),
      'bottom': Decimal('391.793'),
      'text': 'TRAVEL'},
     {'x0': Decimal('251.498'),
      'x1': Decimal('262.043'),
      'top': Decimal('384.811'),
      'bottom': Decimal('391.793'),
      'text': 'CBA'},
     {'x0': Decimal('263.475'),
      'x1': Decimal('278.011'),
      'top': Decimal('384.811'),
      'bottom': Decimal('391.793'),
      'text': 'CARD'},
     {'x0': Decimal('347.317'),
      'x1': Decimal('372.997'),
      'top': Decimal('384.811'),
      'bottom': Decimal('391.793'),
      'text': '04/13/2019'},
     {'x0': Decimal('392.388'),
      'x1': Decimal('418.068'),
      'top': Decimal('384.811'),
      'bottom': Decimal('391.793'),
      'text': '04/27/2019'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('457.530'),
      'top': Decimal('384.811'),
      'bottom': Decimal('391.793'),
      'text': "SENATOR'S"},
     {'x0': Decimal('458.961'),
      'x1': Decimal('506.275'),
      'top': Decimal('384.811'),
      'bottom': Decimal('391.793'),
      'text': 'TRANSPORTATION'},
     {'x0': Decimal('687.430'),
      'x1': Decimal('703.123'),
      'top': Decimal('384.811'),
      'bottom': Decimal('391.793'),
      'text': '697.00'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('450.563'),
      'top': Decimal('390.784'),
      'bottom': Decimal('397.766'),
      'text': 'AIRFARE'},
     {'x0': Decimal('451.991'),
      'x1': Decimal('462.819'),
      'top': Decimal('390.784'),
      'bottom': Decimal('397.766'),
      'text': 'FOR'},
     {'x0': Decimal('464.243'),
      'x1': Decimal('474.791'),
      'top': Decimal('390.784'),
      'bottom': Decimal('397.766'),
      'text': 'SEN'},
     {'x0': Decimal('476.219'),
      'x1': Decimal('497.879'),
      'top': Decimal('390.784'),
      'bottom': Decimal('397.766'),
      'text': 'HAWLEY'},
     {'x0': Decimal('499.313'),
      'x1': Decimal('534.650'),
      'top': Decimal('390.784'),
      'bottom': Decimal('397.766'),
      'text': 'WASHINGTON'},
     {'x0': Decimal('536.071'),
      'x1': Decimal('543.480'),
      'top': Decimal('390.784'),
      'bottom': Decimal('397.766'),
      'text': 'DC'},
     {'x0': Decimal('544.911'),
      'x1': Decimal('552.030'),
      'top': Decimal('390.784'),
      'bottom': Decimal('397.766'),
      'text': 'TO'},
     {'x0': Decimal('553.454'),
      'x1': Decimal('587.671'),
      'top': Decimal('390.784'),
      'bottom': Decimal('397.766'),
      'text': 'SPRINGFIELD'},
     {'x0': Decimal('589.100'),
      'x1': Decimal('598.785'),
      'top': Decimal('390.784'),
      'bottom': Decimal('397.766'),
      'text': 'MO,'},
     {'x0': Decimal('600.208'),
      'x1': Decimal('626.148'),
      'top': Decimal('390.784'),
      'bottom': Decimal('397.766'),
      'text': 'AMARILLO'},
     {'x0': Decimal('627.582'),
      'x1': Decimal('634.132'),
      'top': Decimal('390.784'),
      'bottom': Decimal('397.766'),
      'text': 'TX'},
     {'x0': Decimal('635.561'),
      'x1': Decimal('646.392'),
      'top': Decimal('390.784'),
      'bottom': Decimal('397.766'),
      'text': 'AND'},
     {'x0': Decimal('647.817'),
      'x1': Decimal('669.190'),
      'top': Decimal('390.784'),
      'bottom': Decimal('397.766'),
      'text': 'RETURN'},
     {'x0': Decimal('88.617'),
      'x1': Decimal('127.119'),
      'top': Decimal('397.196'),
      'bottom': Decimal('404.178'),
      'text': 'DHAW20190045'},
     {'x0': Decimal('155.088'),
      'x1': Decimal('180.768'),
      'top': Decimal('397.196'),
      'bottom': Decimal('404.178'),
      'text': '07/10/2019'},
     {'x0': Decimal('201.881'),
      'x1': Decimal('225.543'),
      'top': Decimal('397.196'),
      'bottom': Decimal('404.178'),
      'text': 'CITIBANK'},
     {'x0': Decimal('226.975'),
      'x1': Decimal('228.683'),
      'top': Decimal('397.196'),
      'bottom': Decimal('404.178'),
      'text': '-'},
     {'x0': Decimal('230.105'),
      'x1': Decimal('254.910'),
      'top': Decimal('397.196'),
      'bottom': Decimal('404.178'),
      'text': 'SENATOR'},
     {'x0': Decimal('256.342'),
      'x1': Decimal('264.609'),
      'top': Decimal('397.196'),
      'bottom': Decimal('404.178'),
      'text': 'IBA'},
     {'x0': Decimal('266.031'),
      'x1': Decimal('280.567'),
      'top': Decimal('397.196'),
      'bottom': Decimal('404.178'),
      'text': 'CARD'},
     {'x0': Decimal('347.317'),
      'x1': Decimal('372.997'),
      'top': Decimal('397.196'),
      'bottom': Decimal('404.178'),
      'text': '06/29/2019'},
     {'x0': Decimal('392.388'),
      'x1': Decimal('418.068'),
      'top': Decimal('397.196'),
      'bottom': Decimal('404.178'),
      'text': '07/07/2019'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('444.576'),
      'top': Decimal('397.196'),
      'bottom': Decimal('404.178'),
      'text': 'STAFF'},
     {'x0': Decimal('446.003'),
      'x1': Decimal('493.317'),
      'top': Decimal('397.196'),
      'bottom': Decimal('404.178'),
      'text': 'TRANSPORTATION'},
     {'x0': Decimal('683.143'),
      'x1': Decimal('703.116'),
      'top': Decimal('397.196'),
      'bottom': Decimal('404.178'),
      'text': '1,112.00'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('450.563'),
      'top': Decimal('403.242'),
      'bottom': Decimal('410.224'),
      'text': 'AIRFARE'},
     {'x0': Decimal('451.989'),
      'x1': Decimal('462.819'),
      'top': Decimal('403.242'),
      'bottom': Decimal('410.224'),
      'text': 'FOR'},
     {'x0': Decimal('464.245'),
      'x1': Decimal('474.792'),
      'top': Decimal('403.242'),
      'bottom': Decimal('410.224'),
      'text': 'SEN'},
     {'x0': Decimal('476.223'),
      'x1': Decimal('497.882'),
      'top': Decimal('403.242'),
      'bottom': Decimal('410.224'),
      'text': 'HAWLEY'},
     {'x0': Decimal('499.314'),
      'x1': Decimal('506.152'),
      'top': Decimal('403.242'),
      'bottom': Decimal('410.224'),
      'text': 'AS'},
     {'x0': Decimal('507.578'),
      'x1': Decimal('534.085'),
      'top': Decimal('403.242'),
      'bottom': Decimal('410.224'),
      'text': 'FOLLOWS:'},
     {'x0': Decimal('535.521'),
      'x1': Decimal('545.504'),
      'top': Decimal('403.242'),
      'bottom': Decimal('410.224'),
      'text': '6/29'},
     {'x0': Decimal('546.931'),
      'x1': Decimal('582.271'),
      'top': Decimal('403.242'),
      'bottom': Decimal('410.224'),
      'text': 'WASHINGTON'},
     {'x0': Decimal('583.692'),
      'x1': Decimal('591.100'),
      'top': Decimal('403.242'),
      'bottom': Decimal('410.224'),
      'text': 'DC'},
     {'x0': Decimal('592.531'),
      'x1': Decimal('599.652'),
      'top': Decimal('403.242'),
      'bottom': Decimal('410.224'),
      'text': 'TO'},
     {'x0': Decimal('601.078'),
      'x1': Decimal('636.721'),
      'top': Decimal('403.242'),
      'bottom': Decimal('410.224'),
      'text': 'SPRINGFIELD;'},
     {'x0': Decimal('638.153'),
      'x1': Decimal('645.283'),
      'top': Decimal('403.242'),
      'bottom': Decimal('410.224'),
      'text': '7/7'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('462.542'),
      'top': Decimal('409.215'),
      'bottom': Decimal('416.197'),
      'text': 'SPRINGFIELD'},
     {'x0': Decimal('463.968'),
      'x1': Decimal('471.088'),
      'top': Decimal('409.215'),
      'bottom': Decimal('416.197'),
      'text': 'TO'},
     {'x0': Decimal('472.520'),
      'x1': Decimal('507.860'),
      'top': Decimal('409.215'),
      'bottom': Decimal('416.197'),
      'text': 'WASHINGTON'},
     {'x0': Decimal('509.281'),
      'x1': Decimal('516.689'),
      'top': Decimal('409.215'),
      'bottom': Decimal('416.197'),
      'text': 'DC'},
     {'x0': Decimal('88.617'),
      'x1': Decimal('127.119'),
      'top': Decimal('415.115'),
      'bottom': Decimal('422.097'),
      'text': 'DHAW20190046'},
     {'x0': Decimal('155.088'),
      'x1': Decimal('180.768'),
      'top': Decimal('415.115'),
      'bottom': Decimal('422.097'),
      'text': '07/11/2019'},
     {'x0': Decimal('201.881'),
      'x1': Decimal('225.543'),
      'top': Decimal('415.115'),
      'bottom': Decimal('422.097'),
      'text': 'CITIBANK'},
     {'x0': Decimal('226.975'),
      'x1': Decimal('228.683'),
      'top': Decimal('415.115'),
      'bottom': Decimal('422.097'),
      'text': '-'},
     {'x0': Decimal('230.105'),
      'x1': Decimal('250.066'),
      'top': Decimal('415.115'),
      'bottom': Decimal('422.097'),
      'text': 'TRAVEL'},
     {'x0': Decimal('251.498'),
      'x1': Decimal('262.043'),
      'top': Decimal('415.115'),
      'bottom': Decimal('422.097'),
      'text': 'CBA'},
     {'x0': Decimal('263.475'),
      'x1': Decimal('278.011'),
      'top': Decimal('415.115'),
      'bottom': Decimal('422.097'),
      'text': 'CARD'},
     {'x0': Decimal('347.317'),
      'x1': Decimal('372.997'),
      'top': Decimal('415.115'),
      'bottom': Decimal('422.097'),
      'text': '07/01/2019'},
     {'x0': Decimal('392.388'),
      'x1': Decimal('418.068'),
      'top': Decimal('415.115'),
      'bottom': Decimal('422.097'),
      'text': '07/07/2019'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('444.576'),
      'top': Decimal('415.115'),
      'bottom': Decimal('422.097'),
      'text': 'STAFF'},
     {'x0': Decimal('446.003'),
      'x1': Decimal('493.317'),
      'top': Decimal('415.115'),
      'bottom': Decimal('422.097'),
      'text': 'TRANSPORTATION'},
     {'x0': Decimal('687.430'),
      'x1': Decimal('703.123'),
      'top': Decimal('415.115'),
      'bottom': Decimal('422.097'),
      'text': '728.30'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('450.563'),
      'top': Decimal('421.088'),
      'bottom': Decimal('428.070'),
      'text': 'AIRFARE'},
     {'x0': Decimal('451.991'),
      'x1': Decimal('462.819'),
      'top': Decimal('421.088'),
      'bottom': Decimal('428.070'),
      'text': 'FOR'},
     {'x0': Decimal('464.243'),
      'x1': Decimal('466.808'),
      'top': Decimal('421.088'),
      'bottom': Decimal('428.070'),
      'text': 'J'},
     {'x0': Decimal('468.238'),
      'x1': Decimal('502.438'),
      'top': Decimal('421.088'),
      'bottom': Decimal('428.070'),
      'text': 'MACGREGOR'},
     {'x0': Decimal('503.862'),
      'x1': Decimal('539.200'),
      'top': Decimal('421.088'),
      'bottom': Decimal('428.070'),
      'text': 'WASHINGTON'},
     {'x0': Decimal('540.627'),
      'x1': Decimal('548.036'),
      'top': Decimal('421.088'),
      'bottom': Decimal('428.070'),
      'text': 'DC'},
     {'x0': Decimal('549.460'),
      'x1': Decimal('556.580'),
      'top': Decimal('421.088'),
      'bottom': Decimal('428.070'),
      'text': 'TO'},
     {'x0': Decimal('558.011'),
      'x1': Decimal('578.819'),
      'top': Decimal('421.088'),
      'bottom': Decimal('428.070'),
      'text': 'KANSAS'},
     {'x0': Decimal('580.247'),
      'x1': Decimal('593.353'),
      'top': Decimal('421.088'),
      'bottom': Decimal('428.070'),
      'text': 'CITY,'},
     {'x0': Decimal('594.785'),
      'x1': Decimal('629.002'),
      'top': Decimal('421.088'),
      'bottom': Decimal('428.070'),
      'text': 'SPRINGFIELD'},
     {'x0': Decimal('630.431'),
      'x1': Decimal('641.262'),
      'top': Decimal('421.088'),
      'bottom': Decimal('428.070'),
      'text': 'AND'},
     {'x0': Decimal('642.687'),
      'x1': Decimal('664.060'),
      'top': Decimal('421.088'),
      'bottom': Decimal('428.070'),
      'text': 'RETURN'},
     {'x0': Decimal('88.617'),
      'x1': Decimal('127.119'),
      'top': Decimal('427.500'),
      'bottom': Decimal('434.482'),
      'text': 'DHAW20190047'},
     {'x0': Decimal('155.088'),
      'x1': Decimal('180.768'),
      'top': Decimal('427.500'),
      'bottom': Decimal('434.482'),
      'text': '07/12/2019'},
     {'x0': Decimal('201.881'),
      'x1': Decimal('225.543'),
      'top': Decimal('427.500'),
      'bottom': Decimal('434.482'),
      'text': 'CITIBANK'},
     {'x0': Decimal('226.975'),
      'x1': Decimal('228.683'),
      'top': Decimal('427.500'),
      'bottom': Decimal('434.482'),
      'text': '-'},
     {'x0': Decimal('230.105'),
      'x1': Decimal('250.066'),
      'top': Decimal('427.500'),
      'bottom': Decimal('434.482'),
      'text': 'TRAVEL'},
     {'x0': Decimal('251.498'),
      'x1': Decimal('262.043'),
      'top': Decimal('427.500'),
      'bottom': Decimal('434.482'),
      'text': 'CBA'},
     {'x0': Decimal('263.475'),
      'x1': Decimal('278.011'),
      'top': Decimal('427.500'),
      'bottom': Decimal('434.482'),
      'text': 'CARD'},
     {'x0': Decimal('347.317'),
      'x1': Decimal('372.997'),
      'top': Decimal('427.500'),
      'bottom': Decimal('434.482'),
      'text': '07/01/2019'},
     {'x0': Decimal('392.388'),
      'x1': Decimal('418.068'),
      'top': Decimal('427.500'),
      'bottom': Decimal('434.482'),
      'text': '07/03/2019'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('444.576'),
      'top': Decimal('427.500'),
      'bottom': Decimal('434.482'),
      'text': 'STAFF'},
     {'x0': Decimal('446.003'),
      'x1': Decimal('493.317'),
      'top': Decimal('427.500'),
      'bottom': Decimal('434.482'),
      'text': 'TRANSPORTATION'},
     {'x0': Decimal('687.430'),
      'x1': Decimal('703.123'),
      'top': Decimal('427.500'),
      'bottom': Decimal('434.482'),
      'text': '463.30'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('450.563'),
      'top': Decimal('433.473'),
      'bottom': Decimal('440.455'),
      'text': 'AIRFARE'},
     {'x0': Decimal('451.991'),
      'x1': Decimal('462.819'),
      'top': Decimal('433.473'),
      'bottom': Decimal('440.455'),
      'text': 'FOR'},
     {'x0': Decimal('464.243'),
      'x1': Decimal('467.660'),
      'top': Decimal('433.473'),
      'bottom': Decimal('440.455'),
      'text': 'K'},
     {'x0': Decimal('469.095'),
      'x1': Decimal('483.627'),
      'top': Decimal('433.473'),
      'bottom': Decimal('440.455'),
      'text': 'FORD'},
     {'x0': Decimal('485.049'),
      'x1': Decimal('507.559'),
      'top': Decimal('433.473'),
      'bottom': Decimal('440.455'),
      'text': 'DETROIT'},
     {'x0': Decimal('508.990'),
      'x1': Decimal('514.684'),
      'top': Decimal('433.473'),
      'bottom': Decimal('440.455'),
      'text': 'MI'},
     {'x0': Decimal('516.112'),
      'x1': Decimal('523.232'),
      'top': Decimal('433.473'),
      'bottom': Decimal('440.455'),
      'text': 'TO'},
     {'x0': Decimal('524.656'),
      'x1': Decimal('531.207'),
      'top': Decimal('433.473'),
      'bottom': Decimal('440.455'),
      'text': 'ST'},
     {'x0': Decimal('532.650'),
      'x1': Decimal('549.466'),
      'top': Decimal('433.473'),
      'bottom': Decimal('440.455'),
      'text': 'LOUIS,'},
     {'x0': Decimal('550.898'),
      'x1': Decimal('585.104'),
      'top': Decimal('433.473'),
      'bottom': Decimal('440.455'),
      'text': 'SPRINGFIELD'},
     {'x0': Decimal('586.529'),
      'x1': Decimal('597.360'),
      'top': Decimal('433.473'),
      'bottom': Decimal('440.455'),
      'text': 'AND'},
     {'x0': Decimal('598.792'),
      'x1': Decimal('620.166'),
      'top': Decimal('433.473'),
      'bottom': Decimal('440.455'),
      'text': 'RETURN'},
     {'x0': Decimal('88.617'),
      'x1': Decimal('127.119'),
      'top': Decimal('439.885'),
      'bottom': Decimal('446.867'),
      'text': 'DHAW20190049'},
     {'x0': Decimal('155.088'),
      'x1': Decimal('180.768'),
      'top': Decimal('439.885'),
      'bottom': Decimal('446.867'),
      'text': '07/25/2019'},
     {'x0': Decimal('201.881'),
      'x1': Decimal('225.543'),
      'top': Decimal('439.885'),
      'bottom': Decimal('446.867'),
      'text': 'CITIBANK'},
     {'x0': Decimal('226.975'),
      'x1': Decimal('228.683'),
      'top': Decimal('439.885'),
      'bottom': Decimal('446.867'),
      'text': '-'},
     {'x0': Decimal('230.105'),
      'x1': Decimal('254.910'),
      'top': Decimal('439.885'),
      'bottom': Decimal('446.867'),
      'text': 'SENATOR'},
     {'x0': Decimal('256.342'),
      'x1': Decimal('264.609'),
      'top': Decimal('439.885'),
      'bottom': Decimal('446.867'),
      'text': 'IBA'},
     {'x0': Decimal('266.031'),
      'x1': Decimal('280.567'),
      'top': Decimal('439.885'),
      'bottom': Decimal('446.867'),
      'text': 'CARD'},
     {'x0': Decimal('347.317'),
      'x1': Decimal('372.997'),
      'top': Decimal('439.885'),
      'bottom': Decimal('446.867'),
      'text': '07/07/2019'},
     {'x0': Decimal('392.388'),
      'x1': Decimal('418.068'),
      'top': Decimal('439.885'),
      'bottom': Decimal('446.867'),
      'text': '07/07/2019'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('457.530'),
      'top': Decimal('439.885'),
      'bottom': Decimal('446.867'),
      'text': "SENATOR'S"},
     {'x0': Decimal('458.961'),
      'x1': Decimal('506.275'),
      'top': Decimal('439.885'),
      'bottom': Decimal('446.867'),
      'text': 'TRANSPORTATION'},
     {'x0': Decimal('690.288'),
      'x1': Decimal('703.128'),
      'top': Decimal('439.885'),
      'bottom': Decimal('446.867'),
      'text': '70.00'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('450.563'),
      'top': Decimal('445.858'),
      'bottom': Decimal('452.840'),
      'text': 'AIRFARE'},
     {'x0': Decimal('451.989'),
      'x1': Decimal('462.819'),
      'top': Decimal('445.858'),
      'bottom': Decimal('452.840'),
      'text': 'FOR'},
     {'x0': Decimal('464.245'),
      'x1': Decimal('474.792'),
      'top': Decimal('445.858'),
      'bottom': Decimal('452.840'),
      'text': 'SEN'},
     {'x0': Decimal('476.223'),
      'x1': Decimal('497.882'),
      'top': Decimal('445.858'),
      'bottom': Decimal('452.840'),
      'text': 'HAWLEY'},
     {'x0': Decimal('499.314'),
      'x1': Decimal('533.521'),
      'top': Decimal('445.858'),
      'bottom': Decimal('452.840'),
      'text': 'SPRINGFIELD'},
     {'x0': Decimal('534.947'),
      'x1': Decimal('542.067'),
      'top': Decimal('445.858'),
      'bottom': Decimal('452.840'),
      'text': 'TO'},
     {'x0': Decimal('543.493'),
      'x1': Decimal('578.844'),
      'top': Decimal('445.858'),
      'bottom': Decimal('452.840'),
      'text': 'WASHINGTON'},
     {'x0': Decimal('580.265'),
      'x1': Decimal('587.673'),
      'top': Decimal('445.858'),
      'bottom': Decimal('452.840'),
      'text': 'DC'},
     {'x0': Decimal('88.617'),
      'x1': Decimal('127.119'),
      'top': Decimal('452.271'),
      'bottom': Decimal('459.253'),
      'text': 'DHAW20190067'},
     {'x0': Decimal('155.088'),
      'x1': Decimal('180.768'),
      'top': Decimal('452.271'),
      'bottom': Decimal('459.253'),
      'text': '09/04/2019'},
     {'x0': Decimal('201.881'),
      'x1': Decimal('225.543'),
      'top': Decimal('452.271'),
      'bottom': Decimal('459.253'),
      'text': 'CITIBANK'},
     {'x0': Decimal('226.975'),
      'x1': Decimal('228.683'),
      'top': Decimal('452.271'),
      'bottom': Decimal('459.253'),
      'text': '-'},
     {'x0': Decimal('230.105'),
      'x1': Decimal('250.066'),
      'top': Decimal('452.271'),
      'bottom': Decimal('459.253'),
      'text': 'TRAVEL'},
     {'x0': Decimal('251.498'),
      'x1': Decimal('262.043'),
      'top': Decimal('452.271'),
      'bottom': Decimal('459.253'),
      'text': 'CBA'},
     {'x0': Decimal('263.475'),
      'x1': Decimal('278.011'),
      'top': Decimal('452.271'),
      'bottom': Decimal('459.253'),
      'text': 'CARD'},
     {'x0': Decimal('347.317'),
      'x1': Decimal('372.997'),
      'top': Decimal('452.271'),
      'bottom': Decimal('459.253'),
      'text': '08/17/2019'},
     {'x0': Decimal('392.388'),
      'x1': Decimal('418.068'),
      'top': Decimal('452.271'),
      'bottom': Decimal('459.253'),
      'text': '08/25/2019'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('444.576'),
      'top': Decimal('452.271'),
      'bottom': Decimal('459.253'),
      'text': 'STAFF'},
     {'x0': Decimal('446.003'),
      'x1': Decimal('493.317'),
      'top': Decimal('452.271'),
      'bottom': Decimal('459.253'),
      'text': 'TRANSPORTATION'},
     {'x0': Decimal('687.430'),
      'x1': Decimal('703.123'),
      'top': Decimal('452.271'),
      'bottom': Decimal('459.253'),
      'text': '685.01'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('450.563'),
      'top': Decimal('458.244'),
      'bottom': Decimal('465.226'),
      'text': 'AIRFARE'},
     {'x0': Decimal('451.991'),
      'x1': Decimal('462.819'),
      'top': Decimal('458.244'),
      'bottom': Decimal('465.226'),
      'text': 'FOR'},
     {'x0': Decimal('464.243'),
      'x1': Decimal('467.947'),
      'top': Decimal('458.244'),
      'bottom': Decimal('465.226'),
      'text': 'C'},
     {'x0': Decimal('469.374'),
      'x1': Decimal('490.470'),
      'top': Decimal('458.244'),
      'bottom': Decimal('465.226'),
      'text': 'NAYLOR'},
     {'x0': Decimal('491.897'),
      'x1': Decimal('512.706'),
      'top': Decimal('458.244'),
      'bottom': Decimal('465.226'),
      'text': 'KANSAS'},
     {'x0': Decimal('514.141'),
      'x1': Decimal('525.821'),
      'top': Decimal('458.244'),
      'bottom': Decimal('465.226'),
      'text': 'CITY'},
     {'x0': Decimal('527.250'),
      'x1': Decimal('535.510'),
      'top': Decimal('458.244'),
      'bottom': Decimal('465.226'),
      'text': 'MO'},
     {'x0': Decimal('536.938'),
      'x1': Decimal('544.057'),
      'top': Decimal('458.244'),
      'bottom': Decimal('465.226'),
      'text': 'TO'},
     {'x0': Decimal('545.496'),
      'x1': Decimal('556.043'),
      'top': Decimal('458.244'),
      'bottom': Decimal('465.226'),
      'text': 'SAN'},
     {'x0': Decimal('557.472'),
      'x1': Decimal('574.000'),
      'top': Decimal('458.244'),
      'bottom': Decimal('465.226'),
      'text': 'DIEGO'},
     {'x0': Decimal('575.425'),
      'x1': Decimal('582.546'),
      'top': Decimal('458.244'),
      'bottom': Decimal('465.226'),
      'text': 'CA'},
     {'x0': Decimal('583.978'),
      'x1': Decimal('594.809'),
      'top': Decimal('458.244'),
      'bottom': Decimal('465.226'),
      'text': 'AND'},
     {'x0': Decimal('596.233'),
      'x1': Decimal('617.607'),
      'top': Decimal('458.244'),
      'bottom': Decimal('465.226'),
      'text': 'RETURN'},
     {'x0': Decimal('88.617'),
      'x1': Decimal('127.119'),
      'top': Decimal('464.656'),
      'bottom': Decimal('471.638'),
      'text': 'DHAW20190068'},
     {'x0': Decimal('155.088'),
      'x1': Decimal('180.768'),
      'top': Decimal('464.656'),
      'bottom': Decimal('471.638'),
      'text': '09/04/2019'},
     {'x0': Decimal('201.881'),
      'x1': Decimal('225.543'),
      'top': Decimal('464.656'),
      'bottom': Decimal('471.638'),
      'text': 'CITIBANK'},
     {'x0': Decimal('226.975'),
      'x1': Decimal('228.683'),
      'top': Decimal('464.656'),
      'bottom': Decimal('471.638'),
      'text': '-'},
     {'x0': Decimal('230.105'),
      'x1': Decimal('250.066'),
      'top': Decimal('464.656'),
      'bottom': Decimal('471.638'),
      'text': 'TRAVEL'},
     {'x0': Decimal('251.498'),
      'x1': Decimal('262.043'),
      'top': Decimal('464.656'),
      'bottom': Decimal('471.638'),
      'text': 'CBA'},
     {'x0': Decimal('263.475'),
      'x1': Decimal('278.011'),
      'top': Decimal('464.656'),
      'bottom': Decimal('471.638'),
      'text': 'CARD'},
     {'x0': Decimal('347.317'),
      'x1': Decimal('372.997'),
      'top': Decimal('464.656'),
      'bottom': Decimal('471.638'),
      'text': '08/12/2019'},
     {'x0': Decimal('392.388'),
      'x1': Decimal('418.068'),
      'top': Decimal('464.656'),
      'bottom': Decimal('471.638'),
      'text': '08/14/2019'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('444.576'),
      'top': Decimal('464.656'),
      'bottom': Decimal('471.638'),
      'text': 'STAFF'},
     {'x0': Decimal('446.003'),
      'x1': Decimal('493.317'),
      'top': Decimal('464.656'),
      'bottom': Decimal('471.638'),
      'text': 'TRANSPORTATION'},
     {'x0': Decimal('687.430'),
      'x1': Decimal('703.123'),
      'top': Decimal('464.656'),
      'bottom': Decimal('471.638'),
      'text': '411.49'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('450.563'),
      'top': Decimal('470.629'),
      'bottom': Decimal('477.611'),
      'text': 'AIRFARE'},
     {'x0': Decimal('451.991'),
      'x1': Decimal('462.819'),
      'top': Decimal('470.629'),
      'bottom': Decimal('477.611'),
      'text': 'FOR'},
     {'x0': Decimal('464.243'),
      'x1': Decimal('467.947'),
      'top': Decimal('470.629'),
      'bottom': Decimal('477.611'),
      'text': 'C'},
     {'x0': Decimal('469.374'),
      'x1': Decimal('497.878'),
      'top': Decimal('470.629'),
      'bottom': Decimal('477.611'),
      'text': 'MESSERVY'},
     {'x0': Decimal('499.313'),
      'x1': Decimal('534.650'),
      'top': Decimal('470.629'),
      'bottom': Decimal('477.611'),
      'text': 'WASHINGTON'},
     {'x0': Decimal('536.071'),
      'x1': Decimal('543.480'),
      'top': Decimal('470.629'),
      'bottom': Decimal('477.611'),
      'text': 'DC'},
     {'x0': Decimal('544.911'),
      'x1': Decimal('552.030'),
      'top': Decimal('470.629'),
      'bottom': Decimal('477.611'),
      'text': 'TO'},
     {'x0': Decimal('553.454'),
      'x1': Decimal('587.671'),
      'top': Decimal('470.629'),
      'bottom': Decimal('477.611'),
      'text': 'SPRINGFIELD'},
     {'x0': Decimal('589.100'),
      'x1': Decimal('599.931'),
      'top': Decimal('470.629'),
      'bottom': Decimal('477.611'),
      'text': 'AND'},
     {'x0': Decimal('601.356'),
      'x1': Decimal('622.729'),
      'top': Decimal('470.629'),
      'bottom': Decimal('477.611'),
      'text': 'RETURN'},
     {'x0': Decimal('88.617'),
      'x1': Decimal('127.119'),
      'top': Decimal('477.042'),
      'bottom': Decimal('484.023'),
      'text': 'DHAW20190069'},
     {'x0': Decimal('155.088'),
      'x1': Decimal('180.768'),
      'top': Decimal('477.042'),
      'bottom': Decimal('484.023'),
      'text': '09/09/2019'},
     {'x0': Decimal('201.881'),
      'x1': Decimal('225.543'),
      'top': Decimal('477.042'),
      'bottom': Decimal('484.023'),
      'text': 'CITIBANK'},
     {'x0': Decimal('226.975'),
      'x1': Decimal('228.683'),
      'top': Decimal('477.042'),
      'bottom': Decimal('484.023'),
      'text': '-'},
     {'x0': Decimal('230.105'),
      'x1': Decimal('250.066'),
      'top': Decimal('477.042'),
      'bottom': Decimal('484.023'),
      'text': 'TRAVEL'},
     {'x0': Decimal('251.498'),
      'x1': Decimal('262.043'),
      'top': Decimal('477.042'),
      'bottom': Decimal('484.023'),
      'text': 'CBA'},
     {'x0': Decimal('263.475'),
      'x1': Decimal('278.011'),
      'top': Decimal('477.042'),
      'bottom': Decimal('484.023'),
      'text': 'CARD'},
     {'x0': Decimal('347.317'),
      'x1': Decimal('372.997'),
      'top': Decimal('477.042'),
      'bottom': Decimal('484.023'),
      'text': '08/12/2019'},
     {'x0': Decimal('392.388'),
      'x1': Decimal('418.068'),
      'top': Decimal('477.042'),
      'bottom': Decimal('484.023'),
      'text': '08/14/2019'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('444.576'),
      'top': Decimal('477.042'),
      'bottom': Decimal('484.023'),
      'text': 'STAFF'},
     {'x0': Decimal('446.003'),
      'x1': Decimal('493.317'),
      'top': Decimal('477.042'),
      'bottom': Decimal('484.023'),
      'text': 'TRANSPORTATION'},
     {'x0': Decimal('687.430'),
      'x1': Decimal('703.123'),
      'top': Decimal('477.042'),
      'bottom': Decimal('484.023'),
      'text': '411.49'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('450.563'),
      'top': Decimal('483.014'),
      'bottom': Decimal('489.996'),
      'text': 'AIRFARE'},
     {'x0': Decimal('451.991'),
      'x1': Decimal('462.819'),
      'top': Decimal('483.014'),
      'bottom': Decimal('489.996'),
      'text': 'FOR'},
     {'x0': Decimal('464.243'),
      'x1': Decimal('467.660'),
      'top': Decimal('483.014'),
      'bottom': Decimal('489.996'),
      'text': 'A'},
     {'x0': Decimal('469.095'),
      'x1': Decimal('505.297'),
      'top': Decimal('483.014'),
      'bottom': Decimal('489.996'),
      'text': 'VELEZ-GREEN'},
     {'x0': Decimal('506.721'),
      'x1': Decimal('542.059'),
      'top': Decimal('483.014'),
      'bottom': Decimal('489.996'),
      'text': 'WASHINGTON'},
     {'x0': Decimal('543.486'),
      'x1': Decimal('550.895'),
      'top': Decimal('483.014'),
      'bottom': Decimal('489.996'),
      'text': 'DC'},
     {'x0': Decimal('552.319'),
      'x1': Decimal('559.439'),
      'top': Decimal('483.014'),
      'bottom': Decimal('489.996'),
      'text': 'TO'},
     {'x0': Decimal('560.877'),
      'x1': Decimal('595.083'),
      'top': Decimal('483.014'),
      'bottom': Decimal('489.996'),
      'text': 'SPRINGFIELD'},
     {'x0': Decimal('596.509'),
      'x1': Decimal('607.339'),
      'top': Decimal('483.014'),
      'bottom': Decimal('489.996'),
      'text': 'AND'},
     {'x0': Decimal('608.764'),
      'x1': Decimal('630.138'),
      'top': Decimal('483.014'),
      'bottom': Decimal('489.996'),
      'text': 'RETURN'},
     {'x0': Decimal('88.617'),
      'x1': Decimal('127.119'),
      'top': Decimal('489.427'),
      'bottom': Decimal('496.409'),
      'text': 'DHAW20190070'},
     {'x0': Decimal('155.088'),
      'x1': Decimal('180.768'),
      'top': Decimal('489.427'),
      'bottom': Decimal('496.409'),
      'text': '09/09/2019'},
     {'x0': Decimal('201.881'),
      'x1': Decimal('225.543'),
      'top': Decimal('489.427'),
      'bottom': Decimal('496.409'),
      'text': 'CITIBANK'},
     {'x0': Decimal('226.975'),
      'x1': Decimal('228.683'),
      'top': Decimal('489.427'),
      'bottom': Decimal('496.409'),
      'text': '-'},
     {'x0': Decimal('230.105'),
      'x1': Decimal('250.066'),
      'top': Decimal('489.427'),
      'bottom': Decimal('496.409'),
      'text': 'TRAVEL'},
     {'x0': Decimal('251.498'),
      'x1': Decimal('262.043'),
      'top': Decimal('489.427'),
      'bottom': Decimal('496.409'),
      'text': 'CBA'},
     {'x0': Decimal('263.475'),
      'x1': Decimal('278.011'),
      'top': Decimal('489.427'),
      'bottom': Decimal('496.409'),
      'text': 'CARD'},
     {'x0': Decimal('347.317'),
      'x1': Decimal('372.997'),
      'top': Decimal('489.427'),
      'bottom': Decimal('496.409'),
      'text': '08/12/2019'},
     {'x0': Decimal('392.388'),
      'x1': Decimal('418.068'),
      'top': Decimal('489.427'),
      'bottom': Decimal('496.409'),
      'text': '08/14/2019'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('444.576'),
      'top': Decimal('489.427'),
      'bottom': Decimal('496.409'),
      'text': 'STAFF'},
     {'x0': Decimal('446.003'),
      'x1': Decimal('493.317'),
      'top': Decimal('489.427'),
      'bottom': Decimal('496.409'),
      'text': 'TRANSPORTATION'},
     {'x0': Decimal('687.430'),
      'x1': Decimal('703.123'),
      'top': Decimal('489.427'),
      'bottom': Decimal('496.409'),
      'text': '411.49'},
     {'x0': Decimal('428.335'),
      'x1': Decimal('450.563'),
      'top': Decimal('495.400'),
      'bottom': Decimal('502.382'),
      'text': 'AIRFARE'},
     {'x0': Decimal('451.989'),
      'x1': Decimal('462.819'),
      'top': Decimal('495.400'),
      'bottom': Decimal('502.382'),
      'text': 'FOR'},
     {'x0': Decimal('464.245'),
      'x1': Decimal('467.949'),
      'top': Decimal('495.400'),
      'bottom': Decimal('502.382'),
      'text': 'C'},
     {'x0': Decimal('469.375'),
      'x1': Decimal('486.186'),
      'top': Decimal('495.400'),
      'bottom': Decimal('502.382'),
      'text': 'WEIHS'},
     {'x0': Decimal('487.617'),
      'x1': Decimal('522.958'),
      'top': Decimal('495.400'),
      'bottom': Decimal('502.382'),
      'text': 'WASHINGTON'},
     {'x0': Decimal('524.384'),
      'x1': Decimal('531.792'),
      'top': Decimal('495.400'),
      'bottom': Decimal('502.382'),
      'text': 'DC'},
     {'x0': Decimal('533.218'),
      'x1': Decimal('540.339'),
      'top': Decimal('495.400'),
      'bottom': Decimal('502.382'),
      'text': 'TO'},
     {'x0': Decimal('541.770'),
      'x1': Decimal('575.977'),
      'top': Decimal('495.400'),
      'bottom': Decimal('502.382'),
      'text': 'SPRINGFIELD'},
     {'x0': Decimal('577.403'),
      'x1': Decimal('588.232'),
      'top': Decimal('495.400'),
      'bottom': Decimal('502.382'),
      'text': 'AND'},
     {'x0': Decimal('589.659'),
      'x1': Decimal('611.030'),
      'top': Decimal('495.400'),
      'bottom': Decimal('502.382'),
      'text': 'RETURN'}]

``` python
```



## 2020-data-docs-arsenal.md

Data & Docs 
For Your Arsenal: IRE 2020
Samah Assad, WBBM/CBS Chicago
Kate Martin, Carolina Public Press


Covering & uncovering: COVID-19
Racial disparities
Request medical examiner data or physical reports of deaths. Then map to show where. Enrich with data from Census & Bureau of Labor Statistics. And don’t step checking. 
Unemployment
How is your state dept. handling surge in claims? FOIA new hires, system contracts, training, etc. Build a timeline of any failures. U.S. Dept. of Labor maintains good contextual data.
Nursing home infections and deaths
Request this information from your state department of health. Initially North Carolina kept this information hidden. Our news collaboration pried nursing home data loose. 
PPP loans
Look up filings made by public companies here, which is how we found this out. Explore SBA data. 


#Transparency 

COVID-19 tips: cont’d
Hospitals
-Check in with overflow sites - how are they doing? How much did it cost? 
-Capacity: many studies are tracking this
-Equipment & PPE 
Domestic violence
Request from EMS and/or police data/stats on DV calls. How were victims reporting abuse during lockdown and has it changed?
Death certificates
Request them from county registers of deeds, then examine each one for COVID-19 or probable COVID-19. (* Death certificates are not public in every state) 

Resource requests
Ask state Emergency Operations Center for requests for PPE, staffing and other emergency aid. (Info should be a database)
Track spending
FOIA from state comptroller all expenditures and/or contracts on COVID-19 purchases. Build database overtime to catch any patterns or interesting expenditures.
Congregate living testing
Nursing homes, jails, migrant housing: the virus spreads quickly in cramped quarters. Get data on viral spread from state health departments.

Policing/crime 
Arrest/outcome data  Example: sexual assault
Asset forfeiture
Search warrant data
Settlements/payouts 
Police militarization or surveillance gear
Police/EMS response times

Courts and conviction data
Get data from the state court system:
Should include fields like: defendant, charged crime, case disposition, convicted crime, etc
Explore the data and ask questions
How many charged with sexual assault are convicted? Do they plead down?
Calculate by county/judicial district
Talk to sources: Rape crisis centers, assault victim advocates, state attorney general
Seeking conviction series

City government
311 data
What are key issues impacting residents & how well is the city’s response system built to handle it? Example: Housing
PR expenditures
How are cities spending tax dollars to beat negative press? Example: Utility departments; conference expenditures, agendas & materials

Inspector General reports
Has the IG ever investigated the issue you’re looking into? 
Infrastructure: More than Potholes 
Street resurfacing -- how does your city choose where to spend the money?

Procurement data can be the bread and butter of your beat.

Massive document shredding at Cherokee County DSS raises questions

Education 
Educator misconduct data
Public school demographics
Seclusion and restraint
How schools spend your $$
Student success by grade, demographics


I mean...seriously, guys...

County or state government data
Property tax delinquents
Voter registration data - great for contacts and identity verification
Pet license database - people who won’t give you their cell number do want to get their dogs back
Property or parcel databases - who owns that land?
FOIA logs - what are other people requesting (most are not reporters)

Health
Mother childbirth deaths
Does your state have a mortality review committee? What reports are they producing?
Opioid prescriptions
You can now see how many pills were shipped into your community at the height of the crisis
Doctor disciplinary records
Have any contributed to the opioid crisis?

Routine records
Mileage reports: Can show you where people of interest are going and possibly why.

Census data: censusreporter.org is very user friendly

Vendor lists
Internal phone directories
Employee rosters and org trees
Contracts database
Legal fees

Some more fun ones!
Emails from PR people...about you
Have you ever FOIA’d yourself? It’s fun.
Recordings & notes
From interviews you have with officials. How are they strategizing PR?

Campaign contributions
State & federal candidate lookups
Investigating nonprofits
Guidestar & Propublica’s nonprofit explorer are your best friends!
Wildlife carcass removal database How states figure out where to put the deer crossing signs
Card swipes
Got a tip about someone important (and highly paid) not showing up to work? Get their swipes.


Complaints about important people
Ya never know.

Always remember...


A PDF is not a spreadsheet. 

ALWAYS fight for that spreadsheet.

ALWAYS appeal.


FOIA on, warriors. 

Email & follow us!
sfassad@cbs.com @SAssadNews
kmartin@carolinapublicpress.org @KateReports


Data & Docs 
For Your Arsenal: IRE 2020
Samah Assad, WBBM/CBS Chicago
Kate Martin, Carolina Public Press


## 2020-data-journalism-team-of-one.md

**Being Scrappy: Data journalism as a team of one**  
Samah Assad, CBS Chicago/WBBM, @sassadnews  
Carolyn Thompson, Independent journalist, [@caroethompson](https://twitter.com/CaroEThompson)

**Organization and time management** 

* Create your own tracking systems, priority lists and alerts if you don’t have an editor holding you to account. This is especially helpful in the case of sources, FOIAs, and following up on requests for data and documents. (I like [Things](https://apps.apple.com/us/app/things-3/id904237743) as a way to set up tasks with deadlines, or the free version of [Todoist](https://todoist.com/))  
* For FOIAs, create a system (spreadsheet or whatever is easiest for you) that tracks what you’ve sent, legal timeline, when to follow up, each time contact was made, and alerts to action.  
* Have a creative mindset but give yourself structured systems to be disciplined.   
* Give yourself cutoff dates for how long you have to dig into something before deciding you can’t move forward (for a coding problem, it can be 20 mins, for a story idea, maybe it’s a few days, for a data cleaning project, maybe it’s 3 weeks, etc.)  
* Never, never, never touch your raw data\! Always make copies just in case.


**Collaboration and getting help/second eyes on your work**

* Design a wide network of expert resources that you can call on for advice or data analysis and cultivate those relationships BEFORE you need them  
* Find some journalists or coders in your newsroom or networks who also might be willing to give your work a second look. (Carolyn has a small group of supportive freelance friends who hold each other to account and provide support when needed \- be that technical, journalistic, or just for venting about frustrations)  
* Find an expert and build a relationship of respect. Let them challenge your method. Let them poke holes in your research. Let them ask questions. This will help you defend the decision-making process and write your methodology later.  
* Build relationships with your region’s auditor general, and with mapping and IT experts inside institutions that interest you. This can also help guide your requests to communications contacts.  
* See whether other journalists in other regions have done similar stories to the one you’re doing. Read their stories and methods, and reach out to them for advice. Often people are thrilled to share their lessons learned from a hard project and to know that they’re contributing to your work. Consider offering them a note \- this project was inspired by… \- if you want to show your appreciation.  
* Don’t discount working with startups, NGOs, granting organizations and academic researchers who have an interest in your reporting. Be clear and transparent about roles and define journalistic boundaries early. For more formal agreements, consider signing an MOU making it clear what role you each have and that they do not have say in your story. Be transparent in your stories about who you worked with and why.

**Working with editors/producers (especially those unfamiliar with data)**

* Transparency is critical. Don’t talk down to them, help them understand what you’re trying to achieve and why it can take time. Keep them apprised of your process (not all the details, but the big picture.) For an editor who isn’t as tech-savvy, make a notebook or Excel doc showing the steps you did so they and others can understand  
* Argue for an expandable methodology section. Even if only a few people read it, it’s the knowledgeable ones who do.  
* Keep track of all your steps. You need to be able to defend your work and it can be used in the future for other stories. (Try tools like [Workbench](https://workbenchdata.com/), [Jupyter Notebooks](https://jupyter.org/), etc for this. In Excel, consider making separate tabs for each step of work.)  
* Keep notes (whether within your code or in a separate document) throughout the process of how you’re doing everything, which choices you’re making, and why, so that you can easily understand and summarize at the end when you’re writing your methodology or explaining your decision-making. This is also to help you replicate the work in future.  
* Work with graphics artists early on if possible, and consider creating mock-ups to help them visualise your goal

**Transparency**

* Admit what you don’t know or couldn’t figure out. Don’t be ashamed about being unable to see the entire picture \- sometimes stories come in stages.   
* Those missing pieces can also become part of the story. Sometimes it will spark someone who does. Or write another story about it instead.

**Resources for data analysis** 

* IRE (and NICAR) \- make use of your membership\! These groups have [listservs](https://www.ire.org/resource-center/listservs), Slack channels, mentorship and training programs, [databases](https://www.ire.org/nicar), and research teams ready to help you.  
* Use the tools built to offer journalists free research: [OCCRP’s investigative dashboard](https://investigativedashboard.org/), [satellite companies](https://www.digitalglobe.com/), etc.  
* Join [online communities](https://newsnerdery.org/) for lonely coders or data journalists  
* Find your experts (look at academic publications, check who was quoted in articles on the topic, consider finding people who aren’t quoted as often, use [expert databases](https://gijn.org/2016/05/23/resources-guides-to-finding-expert-sources/) such as [https://500womenscientists.org/request-a-scientist](https://500womenscientists.org/request-a-scientist))  
* Take online courses (Coursera, Knight Center, among many others. Here’s a good list: [https://gijn.org/data-journalism-training-courses/](https://gijn.org/data-journalism-training-courses/)) and consider doing intensive bootcamp or training programs ([IRE](https://www.ire.org/events-and-training) offers many, in Canada check out [King’s College Data School](https://ukings.ca/programs/non-credit/data-school/) in Halifax)  
* Read publications about great reporting, including [IJNET](https://ijnet.org/en), [GIJN](https://gijn.org/), [Poynter](https://www.poynter.org/)  
* Apply for grants ([Pulitzer Center](https://pulitzercenter.org/), [Fund for Investigative Journalism](http://fij.org/), [IWMF](https://www.iwmf.org/), and many others. A good list here: [GIJN](https://gijn.org/grants-and-fellowships-2/#reporting) and on [IJNET](https://ijnet.org/en/opportunities))  
* Find your city’s hacks/hackers group ([https://hackshackers.com/](https://hackshackers.com/))

*And lastly, get excited\! Being the only one on a project might seem intimidating, but it’s also freeing. You can get creative, try things out, build your own networks, and pitch projects that interest you. Have fun\!*



## 2020-editing-data-story.md

Editing the data story

NICAR 2020

Maud Beelman, Howard Center for Investigative Journalism
Jennifer LaFleur, Investigative Reporting Workshop


Note cards

	Your job
	
What do you most want to get out of this class?

What is your biggest frustration when it comes to 
data-driven stories?

What is your best practice when it comes to workflow on data stories?


 


TELL THEM IF THEY DON’T KNOW ANSWER TO LAST QUESTION NOT TO WORRY ABOUT IT.


What we’re covering

The data and the process
Vetting the data and methodology
Going from data to story
Writing the story
Discussion and questions
Occasional festive banter


 


 


The tools
Data analysis: spreadsheets, databases, statistical tools, mapping, scraping – and a host of tools and programs that can save tons of work
If something seems like too much work, it probably is. Try to find a better solution.
Take advantage of being the IRE/NICAR  community - everyone is here to share and help!
 
 


GRACE HOPPER, ONE OF THE FIRST FEMALE COMPUTER OPERATORS


It’s not just about the software or code
Critical, logical thinking
Basic math
Understanding the context of the data 
Verifying the data with ground truth
Good organizational skills
Asking questions
Knowing which tool to use and how to use it
Knowing how to interpret results


 
 


Getting the data 
Find downloadable data online
Scrape it 
Request via open records laws
Build your own database


 
 


The role of data


 
 


Foundational data
Decorative data
Responsive data


The analyses 
Complex analyses of data
Basic analysis - Sometimes we’re just counting


 
 


The editor’s role in data projects
Be clear, consistent about goals
Ask what kinds of data are available
Discuss known/suspected problems with the data 
Encourage creative thinking, brainstorm solutions
Ask reporters what worries them
Backstop frequently throughout 
Do your own research
Discuss methodology
Look at the data with/without your reporter 
Challenge the data (not the reporter)


 
 


10 questions every editor should ask 
Does the data answer our questions? Does it tell us something we didn’t think to ask?
Where did you find the data? 
How did you vet/clean the data? 
How did you calculate those numbers?
Are you keeping a data diary? 
Did you replicate your data work? Could someone else? 
Have you consulted experts or done a scientific lit review?
Do we need a white paper?
Can you write a nerd graf/story now?
What is the significance of the data? 


 
 


Don’t ask me questions about the data! I’m fine.

AARRRGGGHHHH!
How long will it take?
Why can’t we say blah, blah, blah?
How come I never get enough time for projects?
Isn’t it good enough?
Would you like fries with that data?
You probably wouldn’t understand.
What do you mean there are problems?


Bulletproofing the data


Data checks
What is the source of the data?
How many records should you have/do you have?
Is data missing?
Is the data within reasonable ranges?
Is everything included?
Are there consistency issues?
Are totals within reasonable bounds?
Have you done internal checks?
Are there duplicates?
Gut check


Questions

Do my findings make sense?
Compared to what?  
- Company XX has done XX terrible thing, 
but what about other companies in the same industry?
- XX people have a higher rate of XX
Should you report a rate or a raw number?
Is your data on the same scale?


jl ADDED


Other considerations

Are there codes that you don’t understand or questions you need answered?
Can you go look at one? Ground truth
Is the data a sample with a margin of error?
Are changes over time reasonable? 
How else could you look at the data?
Are there lurking variables?
With maps -- did you use the right projection?
Are you matching data sets?
Beware data portals. 


Changes over time
Year 1
Year 2
Year 3
Year 4
Year 5
Year 6


Matching data
A name is not enough. Lots of people have the same name


Some notes about polling data

Read the methodology
Know the sample size and margin of error
Know the questions
Know who funded the research
If the source won’t provide the methodology, that’s a red flag.
Don’t report numbers for which you haven’t checked the methodology.


https://www.huffpost.com/entry/corona-beer-coronavirus-poll_n_5e598955c5b6450a30be6b33


	Best practices
Look at your data
Maintain a consistent universe of cases
Keep a data diary or detailed markdown file
Backup your data (Never work from original)
Check against reports
Make sure you’re using the right tool
Check with experts from different sides of the issue
Show findings to the targets and experts
Duplicate your work - don’t just rerun the same script that could have a created an error
Have another person duplicate your work


 
 


Let’s bulletproof some data!

Breakout rooms! 
Go to http://bit.ly/nicarschools

Make a copy of the doc so you aren’t all working on the same file!

Take about 12 minutes:
What questions do you have?
What problems do you see?


 
 


ADDED THIS - STILL NEED LINK TO DATA


11-minute break


How can an editor backstop all this?


	Understand the methodology

It should be logical, make sense
Find similar stories and study what they did
Check with experts from different sides
Find a guide
Use the IRE Resource Center
Understand the process of how data was gathered
 

 
 


Other backstops

Ask for a copy of the record layout
Ask for who else may have done similar research
Read that research
Read the documentation or data “how to” file
Find the experts
Ask for a detailed description of the work (white paper to nerd box)
Seek a second opinion from a trusted colleague
Have a backstop process in place


HAVE JEN TALK BRIEFLY ABOUT REVEAL BACKSTOP PROCESS


	Data diary
For backstop
For story footnoting/lawyering
For staying on track
What you did
How you did it
File names
Copy of code/syntax
Should be clear so that your editor and colleagues can make sense of it

 
 


DIFFERENT EXAMPLES OF DATA DIARIES--WASHINGTON DC TRAFFIC ACCIDENTS PLUS CODE FOR CLEANING DATA

Data diary

Later you can link back to page or number in fact check
Highlight everything that was derived from data (or docs) and go back and check


Gathering your own data

Pitfalls
Time and effort
Accuracy concerns
Consistency concerns

Benefits
Totally original data reporting
Control over all aspects of the data


 
 


Reminders
Leave time for follow up after collecting your data 
If you’ve built a database, set a cut-off date
Use verification or double entry
Attempt to get “ground truth”


 
 


Workflow
You need to have one
Everyone needs to use it
Make sure all parties are included in the beginning
Project management system
Google doc
Github
Backout scheduling


 
 


Writing the data story


The Basics
Thesis, what is it, how does the data support it
Outline the project and the story/ies
Footnote story memos and drafts (increases accuracy and saves time)
Lovelady the findings
Write the nut grafs first
Structure is as important as prose
Avoid number overload use your the strongest finding from your data.
Going from your data findings to your story is little different than going from note/findings to your story.


I also tell my reporters — and I can’t repeat it to them enough — that almost every story is a people story; that they should research a problem or an issue or a trend for its human qualities and write in terms of real people with real problems. And I tell them particularly on complex non-spot news stories, to use an outline. 
-- Steve Lovelady, 1978 ASNE 


The (very) Basic Outline*
Lead: straight, anecdotal, scene or a combo thereof
Nut graf(s)
Major findings/themes that support the nut(s)
Theme #1, data points/supporting material
Theme #2, data points/supporting material
etc...
Closing: Tie up the loose ends, come full circle or go forward


*general guidelines; good writers know when/how to break the rules
(My favorite combo lead)  Parkland Memorial Hospital, by its own calculation, seriously harms two patients a day. Jessie Mae Ned was one of them. 


The Details

Story Structure: The two most basic organizational methods 
Chronology (or reverse chronology) is the easiest to write and for a reader to follow. Warning: don’t make the reader jump time.* 
Thematic structure is more complicated to write, but can be effective for the right material. 
Even within a thematic structure, you can use internal chronology. 

DISCUSS HSI STORY STRUCTURE THAT BREAKS THIS RULE

THIS IS COMBO CHRONO AND ANECDOTAL

JEN will talk about


More Details
Characters: Who are they and what themes/points do they illustrate? Will the reader care about them?
Data: Gives you an entire population to choose the best characters and scenes. 

Scenes: Which ones illustrate themes? Often a good way to get into a story, especially if you’re telling something that happened in the past, i.e., a chronology.

WE TOLD THE HSI SHOOTINGS STORY WITH A SCENE BECAUSE IT ILLUSTRATED MANY OF OUR FINDINGS

THIS WAS A GLOBAL DATA-DRIVEN INVESTIGATION


The Implant Files

Driving this investigation was data collected by the U.S. Food and Drug Administration
The analysis guided reporters to problem devices and helped focus reporting
AP decided to look at spinal cord stimulators


DATA LED US TO DEVICES AND VICTIMS

COLUMBIA, South Carolina (AP) — Desperate for relief after years of agony, Jim Taft listened intently as his pain management doctor described a medical device that could change his life.
It wouldn’t fix the nerve damage in his mangled right arm, Taft and his wife recalled the doctor saying, but a spinal-cord stimulator would cloak his pain, making him “good as new.”
Taft’s stimulator failed soon after it was surgically implanted. After an operation to repair it, he said, the device shocked him so many times that he couldn’t sleep and even fell down a flight of stairs. Today, the 45-year-old Taft is virtually paralyzed, a prisoner in his own bed, barely able to get to the bathroom by himself.
“I thought I would have a wonderful life,” Taft said. “But look at me.”
For years, medical device companies and doctors have touted spinal-cord stimulators as a panacea for millions of patients suffering from a wide range of pain disorders, making them one of the fastest-growing products in the $400 billion medical device industry. Companies and doctors aggressively push them as a safe antidote to the deadly opioid crisis in the U.S. and as a treatment for an aging population in need of chronic pain relief.
But the stimulators — devices that use electrical currents to block pain signals before they reach the brain — are more dangerous than many patients know, an Associated Press investigation found. They account for the third-highest number of medical device injury reports to the U.S. Food and Drug Administration, with more than 80,000 incidents flagged since 2008.
Patients report that they have been shocked or burned or have suffered spinal-cord nerve damage ranging from muscle weakness to paraplegia, FDA data shows. Among the 4,000 types of devices tracked by the FDA, only metal hip replacements and insulin pumps have logged more injury reports.
The FDA data contains more than 500 reports of people with spinal-cord stimulators who died, but details are scant, making it difficult to determine if the deaths were related to the stimulator or implant surgery.
WE TOLD THE STORY ANECDOTALLY AND THEMATICALLY

NON-TRADITIONAL STORY-TELLING based on text analysis. THIS IS AN EXAMPLE OF A STRAIGHT-WRITTEN STORY. WE could also just flip through these as good examples of how data stories have been told. But I think this one also came up with some data analysis tools. 

https://www.reuters.com/investigates/section/ocean-shock/
a BEAUTIFUL data story


“This project began with a little moment: Reporter Maurice “Mo” Tamman, who lives on a sailboat in New York Harbor, noticed fish in nearby waters that were normally found farther south. He started digging into the data, and he discovered that marine creatures are fleeing warming seas, in an epic underwater refugee crisis.”

Read more about the methodology


The top: Doesn’t have to be all number, 
number, number...but sometimes it can.


HERE THE NUMBERS ARE THE STORY BECAUSE THE EXTENT OF THE PROBLEM WAS PREVIOUSLY UNKNOWN.

JEN DOES THIS ONE

JEN DOES THIS ONE

JEN DOES THIS ONE


The Nerd box
Details of what you did, why, and how you did it
Keeps story flowing
Adds transparency
You don’t always need one
Sometimes you need something more extensive
Write it before writing story


CAN WE GIVE EXAMPLES THAT ILLUSTRATE POINT 2 AND POINT 4? I think we can discuss. I moved your last point to the top to avoid the irony - unless that was intended.


Dissect a story’s structure
Form groups of 7 or 8

For your story, find the nut graph, the major findings, the organizational structure, and how the methodology was handled.
11 minutes and then we will discuss:

GROUPS  1 & 2
http://bit.ly/nicar_ds1

GROUPS 3 & 4
http://bit.ly/nicar_ds2

GROUPS 5 & 6
http://bit.ly/nicar_ds3


MEYER AWARD WINNER AND FINALIST FOR 2020 AND KAISER HEALTH NEWS; LISA GIRION can’t be in Groups 1 or 2


Words matter

Making conclusions you can’t back up 
Rates versus raw numbers
The more dilemma
Percent versus percentage points
False precision: 53.14 percent
Avoid number overload
Adjust money for inflation
When analyzing income or home values, use median rather than average
Keep numbers to graphics 

DISCUSS FIRST BULLET POINT RE EDITOR OVER-REACH AND THE NEED FOR REPORTERS TO PUSH BACK IF NEEDED.


Don’t forget about the graphics/apps

They can’t be an afterthought
Text need to be edited
Data needs to be rechecked
Need a workflow – that’s not just email

GRAPHICS HELP TELL COMPLEX DATA STORIES, BUT HAVE TO BE THOUGHT THROUGH AT FRONT END

Courtesy Scott Pham, BuzzFeed


Final Thoughts
You don’t have to be able to do data analyses to be able to understand, manage and data-driven stories.
But you should have an understanding of its power and limits.
You do have to be an organized, logical thinker.
Don’t be intimidated by your data reporter’s skills; have him/her walk you through everything.
Editors’ job = keep reporters focused, listen. 
Don’t be annoyed by editors’ questions.
There are no dumb questions!

JL added second and fifth bullet. 
Isn’t this directed more at reporters than editors? “Don’t be annoyed by editors’ questions.”


this is our signal to go to the cards, unless there isn’t time.

Resources:

Numbers in the newsroom, by Sarah Cohen, available from IRE
How not to be wrong, by Jordan Ellenberg
A mathematician reads the newspaper by John Allen Paulos
How to lie with statistics - an oldie but goodie by Darrell Huff 
IRE Resource Center - tip sheets and story examples


Thank you!

mbeelman@asu.edu  @maudbeelman

jlafleur@irworkshop.org  @j_la28

This presentation is available at the conference site or at bit.ly/nicar20editdata


FOLLOW-UP NOTES:

Our class notes are here.
Pitch form example is here.



## 2020-excel-magic.pdf

###### Table of contents:


### **Excel Magic**

This handout contains a variety of functions and tricks that can be used for cleaning
and/or analyzing data in Excel. This handout refers to data in an Excel file called
“ExcelMagic.xlsx"

##### **Date Functions:**

**Month-Day-Year** (use worksheet called “Dates”):
This is one of my all-time favorite tricks. It works in both Excel and Access. It allows you to grab
just one piece of a date. So if you have a series of dates and you want a new field that just gives
the year. Or if you want a new field to just list the month.

=Year(Datefield)
=Month(Datefield)
=Day(Datefield)

So if you have 4/3/04, here’s what you’ll get with each formula:
Year: 2004
Month: 4
Day: 3 (it gives the date, as in the 3rd day of the month)

**Weekday:**
This works much the same way as the above formula, but instead it returns the actual day of the
week (Monday, Tuesday, etc). However the results come out as 1 (for Sunday), 2 (for Monday).
=Weekday(Datefield)

Here’s what the answers look like for one week in January:


Note: If you want the 1 value to represent Monday (then 2 for Tuesday, 3 for Wednesday, et),
add a 2 on to the formula like this:
=weekday(datefield,2)

**Displaying words instead of numbers:**
Go to Format > Cells and choose Custom and type “ddd” in the Type box provided. It will display
1 as “Sun”, 2 as “Mon”, etc. However, the underlying information will remain the numbers. So if
you want to base an IF..THEN statement on this field or something like that, your formula would
need to refer to the numbers.


If you imported some data and your Date field stayed as text and is not being recognized as a
true date (which is necessary for proper sorting), here’s how you can fix it. The date has to
appear like a real date --- in other words, either 3/4/04 or March 4, 2004 or 4-March-2004 or
one of the other recognized date formats. You can tell that Excel is not recognizing it as a date if


=DATEVALUE(String)

The String that goes inside the parentheses is the cell where your data starts.
Example: =DATEVALUE(b2)

**Datedif**
Useful for calculating ages from birthdates. It gives you the difference between two dates in
whatever unit of measure you specify.

=Datedif(Date 1, Date 2, Unit of Measure)

Units of Measure:
“y” --- years
“m” ---months
“ym” ---number of months since the last year

You can use the TODAY() function to refer to today’s date. Or you could put a specific date in
there (with quotes around it)

Examples:
=Datedif(b2,today(), “y”)
=Datedif(b2, “1/1/2004”, “y”)

**Weeknum:**
This one requires that you have the Analysis ToolPak installed. It is an add-in for Excel. If the
install of Excel was done properly, you should be able to go to the Tools Menu and choose “Addins” and then click the check box next to Analysis ToolPak. If that option is grayed out that
means you need to re-install Excel.
Weeknum returns the number that corresponds to where the week falls numerically during the
year. The formula looks like this:
=Weeknum(celladddress)


You can use Weeknum and Weekday (listed above) in conjunction with Pivot Tables to display
data in a sort of calendar form. This would be useful if you’re looking for patterns in your data
based on the calendar.

To do that, you need to add fields to your data with WeekNum and WeekDay corresponding to
the date in that field. Then create a Pivot Table, with WeekNum in the Row, WeekDay in the
Column and whatever field you want to count or sum in the Data box. (I found that you need to
leave the WeekDay output as 1, 2, 3, etc., so that it will display in the proper order. I tried to
have them display as “Mon”, “Tues”, etc and it wouldn’t put them in order)

**Response Times (use worksheet called “time”):**
One of the most common things journalists want to do with a date/time field is to calculate
response times of local public safety units. To do this, you need to make sure to have full
date/time fields for all the key time points you want to compare (i.e. time of 911 call, dispatch
time, arrival time, cleared time). Be sure that these have dates for each time, as well, because
calls that occur just before midnight might result in an arrival or cleared time occurring on a
different date.

Even if you’re not doing response times, a useful formula you might need would be this one to
strip the time portion off of a date/time field:

=TIME(HOUR(h4),MINUTE(h4),SECOND(h4))

The best approach for calculating a response time is to convert your time into seconds. Here are
the steps you’ll need to do that. (use the worksheet called “TIME” to follow along):

This assumes that you have a date/time field (i.e. “3/31/2013 12:00 PM” or “3/31/2013 14:00”):

=TIME(HOUR(h4),MINUTE(h4),SECOND(h4))*86400

Note: 86400 is the number of seconds in a 24-hour period. So this answer is really representing
the time as the number of seconds that have elapsed since midnight.

If you have response times with just a time—no date (i.e. “12:00 pm), then you can just multiply
that by 86400.

To deal with calls that run across midnight (call received in p.m. and the arrival time is in a.m.),
we need to be able to handle these differently than the other calls. So we need our formula to
be able to check for that.

The simplest would be to have it look to see if the receive date is different than the arrive date.
However, our fields have both date AND time. So it might help if we add new fields that just
hold the dates.

So we’ll create “RECEIVE DATE” AND “ARRIVE DATE” fields and populate them using these
formulas:

=DATE(YEAR(H4),MONTH(H4),DAY(H4))


- Note the “DATE” function used here requires you to put the year first, then month, then day. A
little counterintuitive .

Of course, if you’re feeling confident, you could build that date function into the formula below.
It would just make a really long and complex formula.

Now we can calculate the response time – the difference between the receive time and the
arrive time, and display our answer in minutes.

Here’s the formula, then I’ll explain:

=(IF(N4=O4, **M4-K4**, (86400-K4)+M4))/60

This criteria portion of this IF statement is “N4=O4” – it’s looking to see if the “receive date” and
“arrive date” are on the same day (if not, that’s an indicator that this runs across midnight).

If that’s true, it subtracts M4-K4 (arrive time seconds minus receive time seconds)
If the criteria is false, it subtracts 86400 (number of seconds in a day) from K4 (the receive time)
and then adds the arrive time.

This strange formula puts the receive time and the arrive time into the same time frame to
make it possible to subtract without getting a negative number.

Finally, we have this whole formula surrounded by parentheses and then divide by 60 off the
end. This converts the answer from seconds to minutes.


##### **Text or String Functions:**

(use worksheets called “BasicStrings”, “split names” or “split address”)
These are extremely handy tools that you can use for data cleanup (particularly splitting names)
or during analysis. They allow you to grab only a piece of the information in a field based on
certain criteria. These functions are also available in other software, including most SQL
database programs, and coding languages like R and Python. They often work in a similar
fashion but have slight variations in syntax.

**LEFT:** This tells the computer to start at the first byte on the left side of the field. Then we have
to tell it how many bytes (or characters) to take.
Syntax: LEFT(celladdress, number of bytes to take)
Example: LEFT(B5, 5) --- this will extract the first 5 characters of the contents of cell B5

**MID:** To use this function, you have to tell the computer which cell to work on, where to start
and where to stop. If you want to take everything that remains in the field, just put a really big
number in that will likely encompass all possibilities.
Syntax: MID(celladdress, byte number to start at, number of bytes to take)
Example: MID(B5,10,4) --- this will start at the 10 [th] byte and take 4 bytes.

**SEARCH:** This works as a sort of search tool to tell the computer to either start or stop taking a
“string” at a certain character (or space). This is how we can tell the program to split a name
field at the comma, for example. For this type of work, it is used in conjunction with the MID
function. The character you what to find should be enclosed in quotes.
Syntax: SEARCH(“character we want to find”, celladdress)
Example: SEARCH(“,”,B5)

You can combine this with Mid to explain that you either want to start or stop at a
certain character (even if the character isn’t located at the same byte in every record).


EXAMPLE: MID(b5, search(“,”, b5), 100)
**the above example uses the search function to find the “start” position, then tells the
computer to take 100 bytes from there.


EXAMPLE: MID(b5, 10, search(“,”, b5))
**the above example uses search to find the “end” position.

**Note: If you don’t want to include the character that you searched for in your result, use a –1
or +1 just after the search phrase to either go back a space (-1) or move forward and start a
space farther (+1). Here’s an example that will start at the comma, then move one space
forward and take 100 bytes from there:
=mid(b5, search(“,”,b5)+1, 100)

There is also a **RIGHT** function, which starts at the first byte on the right side of the field and
then you can tell it how many bytes to take. (it isn’t as useful as the others, however)


###### **Basic Strings:**

(use the worksheet called “BasicStrings”)
When I teach people how to use string functions, usually the first response I get is: “Why can’t
you just use Text-to-Columns?” This great feature (found under the Data menu) is very handy if
the column you are trying to split is delimited by something. For example, names such as:
“Smith, John”

But sometimes it won’t work and sometimes your data won’t be that neat and tidy. And when

The data in this worksheet is an example of that very
situation. This is school district expenditure data that
had been reported to the state through their financial
accounting database called UFARS. Each row is a
“bucket” of expenditures, coded by the revenue source
used (“finance”), by the “program” it was spent on and
by the “object” for the expenditure (i.e. “food”,
“postage”, “salaries”, “health insurance”)

In the first column you can see those codes are all
strung together, separated neatly by dashes. (Yes, the
first two rows only have one of the three types of codes)

I wanted to separate these out into their own columns – finance, program and object.

I tried to do text-to-columns, first by making a copy of that column and dropping it in a blank
column. Then highlighting that column and selecting “Text-to-Columns” from the data menu. I
told Excel, it was delimited by a dash (“other”) and to treat consecutive delimiters as one. It
looked like everything would work perfectly. But then the new columns no longer had the
leading zeros (which are necessary)!

That’s when I realized string functions would save the day.

To get the finance code (the first three digits), I used the LEFT() function.
=LEFT(a6, 3)

To get the program code (the middle code), I used the MID() function. You tell it which cell to
work on, which byte to start on, and then how many bytes to take. (Note: you have to look
carefully to see how many dashes are in there. The second code starts at byte 9)
=MID(a6, 9, 3)

And to get the last code, you can either use MID in the same fashion….
=MID(a6, 16,3)

OR….
You can use the RIGHT function
=RIGHT(a6, 3)


###### **Splitting names:**

**Dealing with middle initials:**
You can make string functions even more versatile by combining in some other Excel functions.
Here we’re going to use the LEN function – which calculates the length of a string – and an IF
function – which allows you to tell Excel to look for certain criteria and to do one thing if the
criteria is met, and something else if it is not.

Previously, we split them into Lastname and Restname – but we have the middle initials lumped
together with the first name. Here we’re going to separate those out.

First we need to assess whether we have a consistent pattern we can rely on. In most of these
records, you’ll see we have either a solo first name or a first name with a middle initial. You’ll
also want to make sure they are consistent in terms of periods – are there either no periods on
all records? Or periods on all records? The formula we’re going to use below assumes there are
no periods. And if you’re at all unsure about whether periods exist in your data, I’d recommend
doing a replace-all to get rid of them before you try to split the names.

We also need to keep an eye out for any other variations, especially around the middle initial.
Here we have one record that breaks the pattern – Alex Baldwin has his suffix in there.
“Alexander R III”

Since we don’t have very many records with a suffix, here we’re going to just edit those by hand.
If you had a very large dataset and you don’t know where they all are, there are various
techniques for finding the suffixes and separating them off into a new field. My quick
recommendation would be to use a VLOOKUP to find all the variations, isolate those records and
then use a string function (much like we’re doing here) to split them out.

So for now, I’m going to create a suffix field and edit the Alex Baldwin record by hand.
The logic we’re going to use here is to first figure out how long – or how many bytes – each
name consists of (including the middle initial). Then we’re going to “test” whether or not the
second to last byte is a space – if so, we’re going to assume that there’s a middle initial on the
end.

The way to measure how many bytes of data are in a cell is a function called “LEN”
Let’s try it out….
=len(d3)

(Note: you would probably want to check for leading or trailing spaces first and get rid of them
by either creating a new column using the TRIM function --- =trim(d3) --- or by cleaning up the
data in a program like OpenRefine)

This function returns the number of bytes. If you look at Tom Hanks, for example, it says the
restname cell is 5 bytes. That’s 3 bytes for “Tom”, 1 byte for the space and 1 byte for his middle
initial.


use those first)

We’re also going to name our columns so that we can
use those names, instead of cell addresses in our
formulas. Highlight the data in the column with the
“restname” (include the column label) and right-mouse
click and choose “Define Name”.

In the dialog box that comes up (see image), you’ll see
that it guesses you want to call this RESTNAME – if you
included the column label in the section you highlighted.
You can choose to name it something else, though, if
you want. Make sure that the “Refers to” section is
covering the full extent of your data. Click OK.

We can now combine the LEN function, with a MID function and an IF function to test whether
or not there’s a space there. This step is just to show you how it works. (Anywhere that it says
“RESTNAME” is referring to the named label we just created)

=IF(MID(RESTNAME, LEN(RESTNAME)-1, 1)=””, “TRUE”, “FALSE”)

Remember IF statements have three parts – the criteria to look for, what to do if it’s true and
what to do if it’s false.

The formula – MID(RESTNAME, len(RESTNAME)-1, 1)=”” --- is our criteria part. The LEN function
minus 1 tells MID where to start and then we say just grab that one byte. And it’s testing
whether or not that one byte equals a space.

If it does equal a space, we’re dropping the word “true” into our column and if it does not, we’re
dropping in the word “false”

If you copy it down, you’ll see that it worked perfectly.

So now let’s adjust it to make it actually split apart data.

We can keep almost all the formula – we’re just going to edit the “true” and “false” parts.

We’ll change the true part to the string function that’s needed to put the middle initial in this
column, by putting in RIGHT(RESTNAME,1)

And then we’ll change the false part to just two double-quote marks. This is how you tell it to
leave the cell blank.

=IF(MID(RESTNAME, LEN(RESTNAME)-1, 1)=" ", RIGHT(RESTNAME,1), "")


just a couple tweaks

We’ll leave the criteria part of the formula the same
=IF(MID(RESTNAME, LEN(RESTNAME)-1, 1)=" ",

Then this time the true portion needs to be what to do if there is a middle initial – in this case
we want to tell it to start on the left and go until it hits the space. Remember that are LEN
formula -1 gives us the spot! And we’ll Trim it just in case.

LEFT(RESTNAME,TRIM(LEN(RESTNAME)-1)),

Then the false portion of our formula is what to do if there is NOT a middle initial. In that case,
we merely want to copy over the contents of the D column. We’ll trim it, just in case.

TRIM(RESTNAME))

Here’s full formula:
=IF(MID(RESTNAME,LEN(RESTNAME)-1,1)=" ",LEFT(RESTNAME,TRIM(LEN(RESTNAME)1)),TRIM(RESTNAME))

Be sure to troll through your data and look for anomalies. Use the Filter feature or run a Pivot
Table to look for problem records.

###### **Trick for splitting apart city and state when it’s not delimited**

(use worksheet called “citystate”)
This trick is only going to work in specific circumstances, but it’s one you might encounter with
some frequency. Here’s the deal…you’ve got a spreadsheet that has a column containing both
the city name (or perhaps a county name) and a two-digit state abbreviation but there isn’t a
comma separating the two items, so it’s not easy to parse.

You can use the LEN function to determine how long the full string is and then subtract 2 digits
to find out what byte position that last space is at. (since that’s the byte position you want to
use for splitting the info).

So in column B, put in this formula and copy it down:
=len(a2)-2

A2 is the first cell where our data (city-state column) is located. The first part of the formula –
LEN(A2) – is calculating the number of bytes there are in the cell. And then -2 is just subtracting
two bytes.

Check your numbers on a few examples to make sure it’s hitting the right position. Then you can
use that number you just created (in the B column)

To grab the city name:
=LEFT(a2,b2)


above?

Then you can grab the state abbreviation either by using:
=RIGHT(A2,2)
OR
=MID(A2,B2,2)

###### **Other text functions:**

**SUBSTITUTE(cell, oldtext, newtext):** Allows you to mass replace (or elimination) of a specific
word or phrase in a column. For example, I have a list of school districts and the names of the


Here’s the formula I used in the above example:
=SUBSTITUTE(a3, “PUBLIC SCHOOL DISTRICT”, “”)

In the above example I’m leaving the “newtext” part of the formula blank because I don’t want
to replace the phrase with something else. If you wanted to change it — perhaps you want it to
say, “Schools” — then you could put that within that last set of quotes.

The function is very specific. For example it won’t replace the phrase “PUBLIC SCHOOL DIST”
because it’s not an exact match.

**EXACT(text1, text2):** (use worksheet called “Exact”) Compares two strings to see whether they
are identical. This is great for if you are trying to line up two sets of lists. Let’s say each contains
the 50 states, so you want to align them by the name of the state (which appears in both lists). It
returns FALSE if the two items are not identical.


times you tell it. The most interesting use of this I found is to generate a sort of bar chart on the
fly. So for example, let’s say you have a list with totals of something in column B.

You could have it create bar charts using the
pipe “|” character based on the total number,
like this:
=REPT(“|”, b2)

When you copy this down to the remaining
rows you’ll see it create a bar for each line.

**LEN(text)** : Returns the length in number of bytes.

**PROPER(text)** : Converts the data in the cell to proper case. LOWER and UPPER are also
available.


#### **IF Statements:**

(use worksheets called “BasicIF”, “More BasicIF”)
These are one of several LOGICAL functions that are available in Excel. It’s an extremely
powerful tool for a variety of tasks, most notably for assigning categories to your data based on
certain criteria and for some data cleanup functions that require looking for patterns. Essentially
they allow you to do one thing if your criteria is true, and another thing if your criteria is false.
Later, we’ll talk about nested IF functions that allow you to use multiple criteria.

A basic IF statement consists of:
1) What we’re going to measure as being either true or false
2) What to do if it’s true
3) What to do if it’s false

=IF(criteria, true, false)

Let’s try this out with the “BasicIF” worksheet. This has salary data from the St. Paul police
department. The chief has just announced that everyone is getting a 1% raise, but all will get a
minimum raise of $350 (if 1% of their salary is less than $350).


So for the story, I want to figure out how much additional money this is going to mean (the total
of the “raise” column) based on the current workforce, and then generate a new salary for each
individual.

So the crux of our formula is this: If 1% of the person’s salary is less than $350, then the amount
of their raise will be $350. If not, then it will be 1% of their salary.

As we did earlier, let’s make this easier on ourselves by assigning “names” to our columns and
also the values we’re going to need in our formula

Start by typing $350 in G1 cell at the top of the page. Click on that cell and name it “minimum”
(you can either right-mouse click and choose “define name” or you can go to upper left of the
page and overwrite where it says G1)

And then type 1% in another blank cell—let’s use G2 – and name that one “RaisePct”

Then highlight the whole Salary column (including the label) and name it Salary

Here’s our criteria part:
=if(Salary*RaisePct<Minimum,


=if(Salary * RaisePct < Minimum, Minimum,

And the false part will be the salary times 1%
=if(Salary * RaisePct < Minimum, Minimum, Salary * RaisePct)


Now we can add together the original salary and the raise to get their new salary

--------------------##### **Basic nested IF statements:**

In the MoreBasicIF worksheet, let’s look at this data on scores from football games. The data
shows us the scores for the home team and the visit team, but it doesn’t tell us who won the
game.

Since it’s possible for an NFL game to end in a tie (and several did in 2018), let’s first look at
what we’d need to do to figure out if a game ended in a tie. Then we’ll put that together with
another IF statement to create a new field that tells us which team won the game, or if it ended
in a tie.

Let’s just look at the formula we’d need to figure out a tie.
=IF(f2=g2, “tie”, “not tie”)
The criteria portion is simply – “Is the home score equal to the visit score?”
Then the true portion tells it to put the word “tie” in the new field.
And the false portion says to put the words “not tie” in the new field.


name of the winning team.

To get that, we need to “nest” two IF statements together.
First, we need to determine if the game ended in a tie. If that’s true, it will put the word “tie” in
our new field.
If it’s false, Excel will evaluate our second IF statement – if the home score is greater than the
visit score, then grab the name of the home team; if not, then grab the name of the visit team.

In other words, the second IF statement is the “false” portion of our first IF statement.

Here’s what it looks like….
=IF(f2=g2, “tie”, if( f2>g2, d2, e2) )


Let’s do one more nested IF statement on this worksheet. I want a column indicating whether
the home team won the game, the visit team won the game or that it ended in a tie.
So our new column will have either “home”, “visit” or “tie” as the values.

##### **Using IF to copy down blank columns:**

(use worksheet called “Copy down”)
I use this quite frequently when I get data that lists a team name as a title, then all the players or
all the game dates below that. But I want to apply the team name to each record.

The trick is that you need to have a pattern to follow. In the example below, the pattern is that
the B column is always blank on the lines where the team name is listed. And it’s not blank
anywhere else.


So this formula is going to look to see if the B cell is blank:
=IF(b2= “”, a2,c2)
Then it’s going to put the contents of A2 (in this case, “Arizona Cardinals”) in the field if it finds it
to be true. If it’s not true, it looks to the cell directly above (c2) to essentially copy down the
team name.

**Combining other functions:**
Now that you know the basics of an IF statement, you can jazz it up with all kinds of other
functions. You just place the function as either the criteria, the true part or the false part. Of
course, you can use multiple functions in the same IF statement if necessary.

Examples (I’ve just made these up!):
If a date (located in b2) is for a Monday, then put the word Monday in a new cell, otherwise do
nothing:
=if(weekday(b2)=2, “Monday”, “”)

If a date (located in b2) is equal to another date (located in c2), then put the word “Same” in the
new field, otherwise calculate the difference in months:

=if(b2>c2, “Same”, datedif(b2,c2, “m”))

**Using a wildcard search:**
You can use the SEARCH function to look for a word or symbol contained within other text,
however it gets a little tricky to make it work properly. You have to add the ISERROR function. If
you want to get in this deep, I recommend checking out the help file on these functions.
Otherwise, here’s a quick hit to get you started:


This example assumes you have a list of cities and states and you
want to flag all of the ones that are in Texas. In this case, the state
name is written out in full.

So if it finds Texas, this formula instructs it to put an X in the C
column, otherwise leave it blank.

=IF(ISERROR(SEARCH("*Texas*",B4,1)>0)=FALSE, "X","")

The criteria part of this stretches from the ISERROR all the way to the FALSE. The ISERROR is
necessary because it will give you an error message if it doesn’t find the word. It’s the only way
you can instruct the computer to do something in the false portion of your answer (even if that
means just leaving it blank).

The following portion:
SEARCH(“*Texas*”, b4, 1)
If used alone, this portion will return a 1 if it finds the search term and an error message if it
doesn’t. So then you need to add the IF portion to give it two options. By adding the ISERROR
and the =FALSE, you can sidestep the error message.


##### **More nested IF statements:**

(use worksheet called “NestedIF_2”)
This is data on schools in Minneapolis. It identifies (only by number) the principals at each
school, each year. Some schools have up to 8 years’ worth of data, others have fewer years
because they haven’t been open the whole 8 years. Our goal is to figure out how many different
principals each school has had during this time. We can’t just count the number of records,
cause you’ll just get the number of years’ worth of data we have for each school. There are
quicker ways to do this in SQL, but if you want to stay working in Excel, this is a good solution.

We’ll start by **making sure the data is sorted** by school number and then by data year,
ascending. The school number is the only consistent identification we have for a school (names
sometimes change from year to year).

Our IF statement is going to first figure out if we’re on the first record for a school or not. If it is
the first record, it will mark that record with a “1” (our first principal). If it’s not, it will do a
second IF statement that looks to see if the person number is the same as the person number in
the row above. If it is the same number, it’ll put a 0 in (since this is not a new principal). If it’s a
different number, it will put in a 1 (a new principal). When we’re finished, we’ll have a column
we can use in a pivot table to SUM the number of principals.

Let’s **put our formula** in cell F10.

Here’s the first part of our formula (the ellipsis indicates the part we haven’t finished yet)
It’s looking to see if the school number on row 10 is the same as on row 9 and puts in the
number 1 if that’s true. We haven’t gotten to the false portion yet.

=if(d10<>d9), 1, …..)

You’re probably thinking, duh! Row 9 is the header row! Yes, you’re right. But it will make more
sense when you go farther down into your data.

Here’s the full formula:

=if(d10<>d9), 1, **if(e10<>e9), 1, 0)** )

The second IF formula is embedded in the “false” portion of our first IF statement; in other
words, it will only put that formula to use if it’s on a record where the school number matched
the row above.

This second IF formula looks at the person number in column E. It puts the number 1 in if the
person number doesn’t match the row above (a new principal) and puts in 0 if it does match the
row above.

When copy the formula down the page and you look at your results, you should see that there is
always a 1 in the first row for each school (probably the 09-10 school year). And then there
should only be another 1 for that same school if there’s a new principal in a subsequent year.

Now that you have this filled in (make sure there’s a header on that column!) and then you can
build a Pivot Table that has the school number in the rows and SUM of the column F. That will


that you might also want to count up how many years for each school so you can say something
like…. Bryn Mawr had 3 principals in 8 years, while Ramsey Middle had 1 in 3 years.)

##### **Even more complicated nested IF statements:**

(use worksheet called “Nested IF”)

The sheet in ExcelMagic called “Nested IF” has data from Minnesota’s gay marriage battle. It has
one record for each state house district. Then in columns B through G we have results from a
2012 statewide ballot measure calling for a ban on gay marriage. The last three columns indicate
the legislator in that district in 2013, their party affiliation (DFL=Democrat) and how they voted
on a bill in 2013 that allowed gay marriage. (Ultimately the bill was signed into law).

The goal here was to find legislators who were not in sync with their district on this issue.
Political analysts were saying these would be the legislators who would be targeted by the
opposing party in the next round of elections.

So there are two things we can do here:

1) First, let’s identify which districts approved the ballot measure (PctYes>.5) or not.
2) Second, let’s identify which legislators voted the opposite of their constituents.
3) Then, of the ones who were opposite of their constituents, which districts either passed
or opposed the 2012 ballot measure by a large margin (60% or more)

**Step 1** - In the “Ballot Result” column, let’s identify whether ballot measure passed (Y) or not (Y)
or if there was a tie (TIE)

We’ll need a nested IF statement to do that. Remember that an IF statement is made up of 3
parts – the criteria (Excel calls it the “logical test”), what to do if it’s true, and what to do if it’s
false. When you “nest” an IF statement you just drop it into either the true spot or the false spot
of the first IF statement.

So in this example, I want to see if the PctYes was greater than 50%, and put “Y” in our column if
that’s true. If that’s false, then I want to check for a tie and put “tie” in if it’s true, and put “N” in
if that’s false.
=IF(CRITERIA1, TRUE, IF(CRITERIA2, TRUE, FALSE))

**So let’s name some columns to make this easier.
Highlight the E column (PctYes) and right-mouse click and choose “Define Names”. Call this
“PctYes”

Repeat the process for columns I (“LegisVote”) and J (“BallotResult”)—we’ll need those later.

Exact formula for this one:
=IF(PctYes>0.5, “Y”, if(PctYes=0.5, “tie”, “N”))


**Step 2** - let’s now identify which district have “opposites” – the legislator voted one way on the
gay marriage bill in 2013 and his/her constituents went the other way on the 2012 amendment.
We’ll use the field we just created (ballot result) and “LegisVote,” which shows how the
legislator voted in 2013 as a yes or no.

The tricky thing about this one is that “Y” on the amendment and “No” on the Legislator’s vote
actually mean the same thing – both are opposed to gay marriage.

I want a new field that says either “opposite”, “both opposed” or “both in favor”

We’re going to use 3 IF statements for this one. There are different ways to set this up, but it
works generally the same way.

=if(LegisVote= “no”, if(BallotResult=”Y”, “both opposed”, “opposite”), if(BallotResult=”N”, “both
in favor”, “opposite”))


Here’s how to interpret this. First it looks to see if there’s a “No” in the LegisVote column (I). If
true, then it looks to see if there’s a “Y” in the Ballot Result column (J). If that’s true that means
both are opposed. (In other words, we had true on first IF and true on second IF). If the Ballot
result column is NOT “Y”, then it’s going to insert “opposite.” (in other words, true on first IF,
but false on second IF).

The third IF statement is actually the FALSE portion of the first IF statement. So that one won’t
even kick in unless I7=”NO” (our first criteria) is false – in other words, the legislator voted “yes”
So in that scenario, the legislator voted “yes” (it failed the first IF statement), so it skips past the
second IF statement and goes to the 3 [rd] IF statement to see if the ballot result (J) is “N”. If that’s
true, then it says “both in favor”. If it’s false, then it says “opposite”(legislator voted “yes” and
constituents approved the ban).


criteria in the same IF statement. In this, we’re going to nest 2 IF statements, both using the
AND function.
Here’s how the AND fits into an IF statement:
=IF(AND(criteria1, criteria2), true, false)

Here’s the formula we’ll use for this one:
=if(AND(LegisVote=”yes”, BallotResult=”N”), “both in favor”, if(AND(LegisVote=”no”,
BallotResult=”Y”), “both opposed”, “opposite”))

This first looks to see if the legislators and constituents are both in favor, if that’s false then it
looks to see if they are both opposed. And then if that’s ALSO false (now we’ve got 2 false Ifs),
then it says there’s an “opposite” going on.

###### **Using IF functions to re-arrange data**

(Use worksheet called “crime”)
One of the most common situations where I use IF statements is to rearrange data that comes
to me in a “report” fashion or has some other problem that makes it difficult or impossible to do
even simple things like sort or PivotTables.

The “crime” worksheet is Uniform Crime Report data that I got from the Minnesota Bureau of
Criminal Apprehension. This is exactly how it came to me.


You can see that there are 5 rows for each jurisdiction, each separated by a blank row. The 5
rows include one that shows total offenses (marked “O”), one that shows total cleared offenses
(marked “C”), one that has the percentage cleared (marked “%”), one that shows the crimes per
100,000 (crime rate, marked “R”) and then there’s another line that simply has the population
that was used to calculate the crime rate.

The biggest problem with this data, though, is that the identifying information about the
jurisdiction is NOT attached to each row. Each piece of identifying information – name of city or
county, whether it’s sheriff, PD or county total, the ID number for the jurisdiction and the
population – are listed separately on each of the five rows.


So that’s the first problem that needs to be solved before you can rip apart this sheet and rearrange to your liking. And IF statements are a great way to fix it.

Step 1:
Create 4 new fields (I put mine on the left side of the data) to hold our identifying information –
city/county, type of jurisdiction, ID number, and population.

Step 2:
IF functions need a pattern in order to work. The pattern we have is that the row marked as “O”
is always the first record for each jurisdiction. So we can essentially use this to tell Excel that it’s
time to switch to a new jurisdiction.

And if the IF statement is on a row that doesn’t have an “O” that means it’s still on the same
jurisdiction it was on in the previous row (with exception of those blank rows, but we don’t care
about those anyway)

Here’s how we’ll set up the first IF statement to populate the new County/City column:
=IF(f9= “O”, E9, A8)

This is saying, if the F column=”O”, then grab the contents of E9 (the name of the county/city), if
it’s not then grab whatever the formula dropped into our new column in the row directly above.
The first line doesn’t make sense – if you look at A8, that’s the header row.


But copy the formula down and then look at the formula in line 10.


find an “O”, so instead of grabbing E10 (which is what the formula says would happen if the
criteria is true) it has grabbed A9 – the value that the formula just dropped in the first row.

Go ahead and copy down the whole sheet and you’ll see that it should appropriately switch to a
new jurisdiction each time it encounters an “O” row. But you should check it periodically
throughout the sheet to make sure nothing went wrong somewhere down the line (the only
reason a problem would occur is if the 5 rows per jurisdiction pattern suddenly changes…i.e.
that there are only 4 rows or there are 6 rows per jurisdiction)

Now we can use very similar formulas for the three other columns. The only change is what
piece of info we grab if it’s true or false.


Once you have all four columns populated and checked your work, you can Copy-PasteSpecialValues to get rid of the formulas.

Then if you fix the header row (so that it’s all on one row and that all columns have headers),
you can turn on Filter and isolate the records you want to move. For example, you could select
all the “O” records (offenses) and put those in a separate worksheet.


##### **Using IF statements to deal with election data:**

(use worksheet “IF_election”)
Election data often comes to us with just raw vote totals for each candidate and no indication of
who won that precinct or county or whatever geography we’re looking at. This solution uses a
combination of various Excel functions – IF, LARGE, MAX, INDEX, MATCH – to give you an
answer.

However, this solution only works if your data is structured so that there is one row for each
geography and the candidate vote totals are in separate columns. (If your data comes with one
row for each candidate – meaning multiple rows for each geography – you can use a Pivot Table
to get it into this structure).


Here’s the big bad formula that we’re going to end up with….
=IF(LARGE(D3:i3,1)>LARGE(d3:i3,2), INDEX($D$2:$i$2,1, MATCH(MAX(D3:i3),D3:i3,0)),"Tie")

But to help you understand how this works, I’m going to break it down into pieces and then put
it together at the end.

First let’s look at this function called LARGE. This allows you to look at an array of data (in this
case, the vote totals for each candidate in a given county) and determine which is the largest, or
second largest, etc.

In a new column on row 3 (where our data starts), type:
=LARGE(D3:I3, 1)

This will give us the vote total that is the largest out of all the votes. In our example, it is
returning 7,229 for Hennepin County.

In another new column on row 3, type:
=LARGE(D3:I3,2)

This will give us the vote together that is the second largest. It’s giving us 3,784 for Hennepin
County.

If there were a tie -- if two candidates both got 7,229 votes, then the second largest formula
would return that same number.

So we can use those two pieces to test whether or not we’ve got a tie situation. We’ll embed
those two pieces into an IF statement.


Put this in another new column, just to test it out:

=if(LARGE(d3:i3,1)>LARGE(d3:i3,2), “no tie”, “tie”))

That’s going to end up being the core piece of our formula, but instead of dropping the phrase
“no tie” into our worksheet, we want it to give us the name of a winner. So next we need to
build the portion of the formula that we will drop in that spot (where it now says “no tie”)

The first piece of that uses the INDEX function. This allows you to specify an array of data and
have it return a value from a particular row and particular column.

For example:
=INDEX($d$2:$i$2, 1, 3)

This looks at D2 to i2 (and because of the anchors, it will always look at that row when you copy
the formula down) and it will grab whatever is housed in the first row and the third column.  If
you try this out in the worksheet, it will return “Huckabee” cause that’s what’s in the third
column of that array.

We’re going to have it reference the header column – where the names are located – so that we
can use that to drop the name of the winner into our data. (Just make sure the header row has
the names the way you want them! In my example, I’m just using their last names.)


But we don’t want our final formula to be hard-coded like that to just the third column (it always
says “Huckabee”!!). We want that value – referring to the column – to change depending who
has the biggest vote total.

That’s where the MATCH function comes in.

MATCH lets you compare two things and it will return the column number where it finds the
match. So in this case, we want to find the biggest value out of the vote totals (remember, that
we’ve already screened out any possible ties – this formula will only do its work on rows where
there is not a tie).

The MAX function will tell us the biggest between columns d and i.
=MAX(d3:i3)

Let’s add that into a MATCH function—it will become the first argument (i.e. the “Lookup
value”)


The second argument in our function --- “d3:i3” – is the “lookup array” – in other words, this is
the range of cells where MATCH is going to look to find the same value that matches the value
returned by Max(d3:i3)

The zero at the end of the MATCH formula is merely telling Excel to only do an EXACT match.
(I.e. the “match type”)

If you try this out in the spreadsheet, it will return the number 4 for Hennepin County. In other
words, the 4 [th] column in our array (the column for Romney) has the biggest value.

Now let’s look back at the INDEX function. Remember that you have to tell Index which column
number to go to. In the example above, we hard-coded it to the 3 [rd] column. But instead, we can
drop this MATCH function into that space in our formula and get the correct answer for each
row of our data.

Try this out in a new column:
=INDEX($D$2:$I$2,1, MATCH(MAX(D3:I3),D3:I3,0))

You’ll see that this is working, but if you copy it all the way down, you’ll get wrong answers for
the ones that have ties. So now we can put all our pieces together, to deal with those ties.

=IF(LARGE(D3:i3,1)>LARGE(d3:i3,2), INDEX($D$2:$i$2,1, MATCH(MAX(D3:i3),D3:i3,0)),"Tie")

This formula will work regardless of how many candidates you have. Just adjust the ranges
(d3:i3 or d2:i2) to match the ranges in your worksheet.

#### **Lookup Tables:**

(use worksheets called “lookups”, “lookup2”)
The VLOOKUP and HLOOKUP functions allow you to use Excel more like a relational database
program. So if you haven’t made the leap to Access yet, here’s how you can get more
functionality out of Excel.

Both functions are useful for cases where you have data that relates to another chunk of data,
with one field in common. They work best if you have the data in the same workbook, but it can
be on separate worksheets. This might be the list of 50 states with current Census estimate data
in one worksheet and the same list with last year’s data in another worksheet. Or it might be a
one-to-many relationship where you have a list of cell phone calls and another table that groups
the time of day into categories (such as morning, evening and afternoon).

The difference between VLOOKUP and HLOOKUP is that VLOOKUP will troll through your lookup
table vertically (all in one column). HLOOKUP goes through it horizontally, or all in one row.

To demo this, we’ll use a very simple example. One worksheet has data from the Census County
Business Patterns, but each record is only identified by the county FIPS number. I want to add a
field that shows the county name. A second worksheet has the names associated with the FIPS
numbers.


VLOOKUP requires that the field you’re matching on is the
farthest left column of the lookup table, like in my example
pictured here. (Below I’ll show you how to use different
functions if your table is not set up this way).

In this example, my Business Patterns data is in one
worksheet and this lookup table is in a worksheet called
“Lookup2”. Our formula will need to reference that name, so
it’s a good idea to name your worksheets when you do this.

Here’s the structure for VLOOKUP:
VLOOKUP(cell, range of lookup table, column number,
range_lookup)

The cell is the first cell in your data table. In this case it would be the cell containing the first FIPS
number I want to look up.

Range of lookup table is the upper left corner of your lookup table to the lower right corner,
encompassing all fields. In the example pictured above, it would be worded like this:
Lookup2!$A$3:$B$89

“Lookup2!” is how we refer to the other worksheet, then you need to anchor ($) the starting cell
(A3) and ending cell (B89).

The column number refers to the column number of your lookup table that you want to return
in your data. In this case, I want column 2, which contains the name of the county.

For range_lookup you either put TRUE or FALSE. True will first search for an exact match, but
then look for the largest value that is less than your data value. FALSE will only look for an exact
match. In this case we want to use FALSE. You’ll see below when you would want to use True.

So here is our final formula:
=VLOOKUP(B3, Lookup2!$A$3:$B$89,2, FALSE)

**Name your lookup:** You can simplify this formula by naming your lookup table. Highlight
the cells in your lookup table, in this case A3 to B89. Go to the Insert Menu and choose
Name, then choose Define. Then type in a name (all one word). For this example, let’s
say I called it “FIPSlkup”.
Then you can change your formula to this:
=VLOOKUP(B3, FIPSlkup, 2, FALSE)


(use worksheet called “classify”)
This is crime report data that tells me the date and time of the incident, but I want to
add a column that identifies which police shift the call came in on. I’ve heard that some
shifts are particularly bad about ignoring calls that come in just before shift change. So
I’ve created a table indicating the start of each shift.


Note that I have the night shift in there twice. That’s because I need to tell Excel what to
do with the times that occur just after midnight. Without that, Excel doesn’t know what
to do with the calls that occur between midnight and 6 am.

Also note another important point --- the table is in chronological order. This is
important when you’re doing an inexact match.

The reason is that Excel is going to take the time of each call and compare it to this
lookup table, first determining whether it falls at or after 12:00 am, but before 6 a.m. If
not, then it will move down to the next one.

The only thing different in this VLOOKUP formula compared to the first one we did is
that the final argument is TRUE.


##### **MATCH and INDEX:**

As I mentioned above, there is another option if your lookup
table is set up differently. Let’s say the FIPS table starts with
the state name and state FIPS in the first two columns, then
has the county FIPS number in the 3rd column. (this is the
worksheet “lookup3”) Obviously VLOOKUP won’t work
because of the placement of that county FIPS column.

Instead you can use a combination of INDEX and MATCH functions. Let’s break it apart first to
see how it works.

Index will go to the data range specified and return the value at the intersection of the row
number and the column number that you provided to it. So, using this alone requires that we
provide specific column and row numbers.

To simplify our formulas, let’s name our lookup table. Highlight the whole table in the
worksheet called “Lookup3” and right-mouse click and choose “define name” – change the
name to “FIPS”

We’ll go back to the worksheet called “Lookup” to do our work.

We could use this formula to get it to return “Anoka”, which is in the 3rd row (the header counts
as a row) of the FIPS lookup table and the fourth column. Just try out this formula on the first
row and see what happens
=INDEX(FIPS, 3,4)

But when trying to match this back to the big data table for all the records, we need more
flexibility. So instead of hard-coding the row number, we’re going to drop the MATCH function
into its place.

We need Match to just look in the C column (where the county FIPS codes are stored), so let’s
name that column. In the lookups3 worksheet, highlight the C column, right-mouse click and
choose “define name.” Let’s call this “FIPScode”

=MATCH(FIPScode, FALSE)

So this is going to the C column (FIPScode) and by setting FALSE, we are saying we want an exact
match.

Here’s the final formula:
=INDEX(FIPS, MATCH(B3, FIPScode, FALSE),4)


Remember that the 4 at the end of our formula is referring to the 4 [th] column in our lookup table.

B3 is the column in our big data table – in worksheet “lookups” – that has the FIPS code that we
are matching to the lookup table. (you could name this column and replace the B3 with a name,
if you want)



## **Misc:**

##### **Anchors:**

When you need to use an anchor ($) in a formula, here’s a quick way to insert it without a lot of
typing. So here’s an example. Let’s say you need to do a percent of total, like in the example
below. Type the formula without the anchors
=b2/b8

And then push the F4 key. It will insert the $ to lock the B8 cell. This locks it so that it won’t
change if you copy the formula down, or copy across.

A bit more about anchors…..If you want to allow the column to change but not the row, you
would only use the anchor in front of the number. If you want to allow the row to change, but
not the column, then you only use the anchor in front of the column letter.

##### **Rank:**

This is a more sophisticated way to rank your records and to account for ties.

=RANK(This Number, $Start Range$:$End Range$, Order)

  - This Number should be the cell where your data starts.

  - Start Range should be the cell where your data starts. Anchor with dollar signs.

  - End Range should be the last cell of your data. Anchor with dollar signs.


assigned #1).

Example: =RANK(B2,$B$2:$B$100,1)

##### **PercentRank:**

Returns the rank — or relative standing - within the dataset as a percentage. So for example, if
you had a list of the payrolls for all of the Major League Baseball Teams, you could do a percent
rank on the payroll to find out which team (the Yankees, of course) have the greatest
percentage of the total.

=PERCENTRANK(array, x, significance)
Array: The range of data that you want to compare each item to
X: the value for which you want to know the percent rank
Significance: an optional value that allows you to set the number of digits

Example:
=PERCENTRANK($a$2:$a$30, a2, 2)

Also check out **PERCENTILE** and **QUARTILE** functions in the Help file.

##### **Round:**

=ROUND(cell, num_digits): For this one you tell it which cell to do its work on and then the
number decimals you want to round to. For the num_digits you can use something like this.

These examples show how it would round the number 1234.5678

 0 puts it to the nearest integer (1235)
 1 goes to one decimal place (1234.6)
 -1 goes to the nearest tenth (1230)
 -2 to the nearest hundreth (1200)
 -3 to the nearest thousandth. (1000)

###### **Copying down a single date:**

Excel’s wonderful feature of copying down (or across) formulas becomes a bit of a nightmare
when you simply want to copy down the same date. Excel will think you want to go on to the
next day, then the next, and the next, etc. Here’s the trick for disabling that:

**Hold down the Control (Ctrl) key while dragging/copying down the first instance of the date.


##### **Using column names instead of cell addresses:**

Are you sick of typing cell addresses? You can set up your worksheet so that the headers you’ve
typed for each column can be used as cell addresses in your formulas instead. Here’s how it
works…. First thing to do is make sure your headers are all filled out, that they are single words
(no spaces, no punctuation), and that they are stored on the first line of your worksheet. Next,
highlight all of your data (my favorite way to do this is to put your cursor somewhere in your
dataset and hit Control-Shift-Asterisk).

Go to the Formulas ribbon and look for “Name Manager” and a button that says “Create from
selection.” In the dialog box that comes up make sure that ONLY the “top row” choice is
selected.

Once this is set you can use your field names instead of cell addresses by simply typing the
column name instead of the cell address. So for example, our basic nested IF formula that
looked at NFL game scores, could use cell names instead of the addresses, like this:


You can click on “Name Manager” in the formulas ribbon to see which names you’ve already
defined (and delete any you don’t want)

##### **Understanding Errors:**

**#DIV/0! :** This almost always means the formula is trying to divide by zero or a cell that is blank.
So to fix this, first check to make sure that your underlying data is correct. In many cases, you
will have zeros. For example, the number of minority students in some schools in Minnesota
might be zero, so I have to use an IF statement whenever trying to calculate the percentage of
minority students. Here’s how I get around the error, assuming the number of minority students
is in cell B2 and the total enrollment is in C2. If the number of minority students is greater than
zero, it does the math. Otherwise it puts zero in my field.
=if(b2>0, b2/c2, 0)

**#N/A:** This is short for “not available” and it usually means the formula couldn’t return a
legitimate result. Usually see this when you use an inappropriate argument or omit a required
argument. Hlookup and Vlookup return this if the lookup value is smaller than the first value in
the lookup range.

**#NAME?:** You see this when Excel doesn’t recognize a name you used in a formula or when it
interprets text within the formula as an undefined name. In other words, you’ve probably got a
typo in your formula.


a math formula).

**#REF!:** Your formula contains an invalid cell reference. For example, it might be referring to a
blank cell or to a cell that has since been deleted.

**#VALUE!** : Means you’ve used an inappropriate argument in a function. This is most often caused
by using the wrong data type.

###### **Tableau Reshaper Tool (only works in Windows Excel 2007 and newer):**

Download here and follow the directions to install in Excel :
[http://kb.tableausoftware.com/articles/knowledgebase/addin-reshaping-data-excel](http://kb.tableausoftware.com/articles/knowledgebase/addin-reshaping-data-excel)

This is a great tool for “normalizing” data, whether you plan to put it into Tableau Public
(visualization software) or not.

Let’s start with the worksheet called “Reshaper1.” This has enrollment data from the University
of Minnesota, broken down by race, gender, ethnicity and residency status. For a visualization,
like Tableau, or even some analysis purposes, it would be better to have the data lined up with
one item (or group total) per line – and keep the grand total attached to each group. Like this:

Year GrandTotal Group Value
1997 32342 Men 15470
1997 32342 Women 15872
Etc.

Tableau Reshaper is perfect for this.

First, a little prep work to make this work the best.

  - Make sure the headers that are on your columns (in this case, the group names) are
presented EXACTLY as you want them to appear in the final data.

  - Make sure that the columns you want to convert are all on the right side of your
spreadsheet and the columns that you want attached to each row are all on the left
side.

Then to make the reshaper tool work, you
put your cursor on the first cell that you want
converted (notice on the screen capture
above, my cursor is on C10 – the first piece of
data I want to put in rows).

Finally, go to the Tableau menu (which was
added to your menu options when you
installed it) and choose “Reshape Data”. It
will ask what cell you want to start with – and
since you put your cursor there previously, it
should guess correctly.


**EXAMPLE 2:**
**For this next one, use the “Reshaper2” worksheet:**
Below is an image of data from one of the health insurance exchanges set up under the
Affordable Care Act. Each row is an insurance product offered in a particular rating area
(geographic area). The premium costs are listed by age, going across the columns (age 0-20, 21,
22, 23, etc)


To analyze this data – and present it in a visualization – I want each age to have its own row. So
instead of one row for each insurance product in a rating area, we’ll end up with 45 (there are
45 age groups in this data)

To reshape, put your cursor on the first data point – in this case F2 – and push the “Reshape
Data” button under the Tableau ribbon.

It will push the data out to a new worksheet.
Note: If the new data file exceeds 1 million rows, this will automatically export your results as a
.CSV file


##### **Build hyperlinks with a formula**

(use worksheet called “hyperlinks”
_These directions are geared for a Windows machine. But it’s likely that with a tweak or two, it_
_will work for Mac as well. More details:_
_https://www.contextures.com/excelhyperlinkfunction.html#formulawritten_

A colleague of mine got data on condemnations in the city. Each record in the spreadsheet had
basic information about the house that got condemned, but then there was also a Word
document for each one containing a copy of the letter the city sent to the occupants.

The spreadsheet included a column with the name of the Word document that matched each
record. All the names were something like this: 4317705_3396272_14084914.doc

She asked me if there was a way to hyperlink to each of those documents, so she could launch
open the Word document right from Excel. Yes, there is! And this will work whether you are
linking to Word documents, other Excel files or PDFs. The key is that the name and the file
extension (.doc, .docx, .xlsx, .pdf, etc) be listed with the name of the file. (If it’s not, you can you
concatenate to tack it on in a new column of your spreadsheet)

Another helpful thing is that you should have your spreadsheet and the documents stored near
each other. These directions will show you what I’d recommend as best practice – that the
documents be stored in a sub-directory of the folder where you have the spreadsheet.

So, for this example, let’s say our main folder is called “condemn”. And our spreadsheet is in
that folder.

Make a sub-folder inside “condemn” and call it “documents” and put all those Word documents
in that directory.
/condemn/documents

Then go into your spreadsheet and create a new column where you will put the hyperlink.

We’ll use an Excel function called HYPERLINK(), which has 2 arguments. The first is the path to
the document. The second is the name you want to appear on the URL you are creating.

Notice below, I’ve highlighted in yellow the first argument – the file path. You can see that we
are hard-coding the path, then concatenating (&) that with the contents of E2, which contains
the file name. We want that to change as we copy the formula down the data.

Also note that the path has a period at the front of it to tell Windows to go into a sub-directory.

=HYPERLINK(“.\documents\” & E2, E2)

The second argument – in this case, the second instance of E2, is simply telling it what to display
when the URL appears on the worksheet. I’m just telling it to display the file name. You could do
something like this and it would say “open document” for every row:

=HYPERLINK(“.\documents\” & E2, “open document”)


## 2020-graph-databases-networks.md

Exploring networks with graph databases
@leilahaddou 
bit.ly/nicar-graphs-20

Donor
Politician
Company
Government contracts?
Favourable legislation?
Land or property deals?
Company

https://www.nbcnews.com/tech/social-media/russian-trolls-went-attack-during-key-election-moments-n827176

https://offshoreleaks.icij.org/pages/database
Examples

What are graph databases?
Creating nodes and relationships
Importing a dataset
Basic querying with Cypher
Session plan 

What is a graph database?

What is a graph database?
In a graph, the data is either …

  … a node
… a relationship 
… an attribute
Leila Haddou
NICAR 2020
IS_AT

Getting started 

Getting started

Getting started

Getting started

Getting started

Building our graph
We’ll use three Cypher Commands to build our graph: 
CREATE
LOAD CSV
MERGE


Creating nodes 
CREATE (p:Person {name:“Leila Haddou”})
Leila Haddou
This assigns an alias (nickname!) and label to our node! 
Attributes or properties go in curly braces. 

This is a property pair.

The property key is ‘name’ and the property value is ‘Leila Haddou’
Building our graph

Creating nodes 
CREATE (p:Person {name:“Leila Haddou”})
Leila Haddou
NICAR 2020
CREATE (e:Event {title:“NICAR 2020”})
Building our graph

Push the run button! 
Building our graph

Building our graph

Building our graph

Creating nodes 
CREATE (p:Person {name:“Leila Haddou”})
Leila Haddou
NICAR 2020
CREATE (e:Event {title:“NICAR 2020”})
Building our graph
IS_AT
CREATE (p)-[r:IS_AT]->(e)

Loading data from a CSV file
Political donations to Prime Minister Boris Johnson and the Conservative party from Jan 2019 to Jan 2020

Source: http://search.electoralcommission.org.uk/

Loading data from a CSV file

Graph model
Loading data from a csv file

Donor
Recipient
DONATED_TO
Value
Date
Donation Type
Name
Name
Status 


Loading data from a CSV file
CREATE
LOAD CSV WITH HEADERS FROM ‘https://raw.githubusercontent.com/leilahaddou/leilahaddou.github.io/master/nicar-20-graph-donations%20(1).csv’ AS row  

Loading data from a CSV file

Loading data from a CSV file
MERGE (d:Donor {name:row.DonorName, status:row.DonorStatus, donationType:row.DonationType}) 
Donor
Recipient
DONATED_TO
Value
Date
Donation Type

Name
Name
Status 
Donation Type
LOAD CSV WITH HEADERS FROM ‘https://raw.githubusercontent.com/leilahaddou/leilahaddou.github.io/master/nicar-20-graph-donations%20(1).csv’ AS row  

Loading data from a CSV file
MERGE (d:Donor {name:row.DonorName, status:row.DonorStatus}) 
MERGE (r:Recipient {name:row.RegulatedEntityName}) 
LOAD CSV WITH HEADERS FROM ‘https://raw.githubusercontent.com/leilahaddou/leilahaddou.github.io/master/nicar-20-graph-donations%20(1).csv’ AS row  

Loading data from a CSV file
MERGE (d:Donor {name:row.DonorName, status:row.DonorStatus}) 
MERGE (r:Recipient {name:row.RegulatedEntityName}) 
CREATE (d)-[dt:DONATED_TO]->(r)
LOAD CSV WITH HEADERS FROM ‘https://raw.githubusercontent.com/leilahaddou/leilahaddou.github.io/master/nicar-20-graph-donations%20(1).csv’ AS row  


Graph model
Loading data from a csv file

Donor
Recipient
DONATED_TO
Value
Date
Donation Type

Name
Name
Status 


Loading data from a CSV file
MERGE (d:Donor {name:row.DonorName, status:row.DonorStatus}) 
MERGE (r:Recipient {name:row.RegulatedEntityName}) 
CREATE(d)-[dt:DONATED_TO {date:row.AcceptedDate, type:row.DonationType, value:toInteger(row.Value)}]->(r)
LOAD CSV WITH HEADERS FROM ‘https://raw.githubusercontent.com/leilahaddou/leilahaddou.github.io/master/nicar-20-graph-donations%20(1).csv’ AS row  

Loading data from a CSV file

Querying our database

The Cypher Query Language 
CREATE
LOAD CSV
MERGE


MATCH
LIMIT
WHERE
RETURN


Querying our database

MATCH (x)
RETURN x
LIMIT 10
Every query must start with a match and end with a return.
match any type of node
then return them
but only ten of them

Querying our database

What we’ll be doing
Exact match on name of donor or recipient
Fuzzy match on name of donor or recipient
Find donors by total amount they donated

Querying our database

MATCH (d:Donor)
WHERE d.name = ‘Lakshmi Mittal’
RETURN d
match a donor node
With this exact name
And return the node!

Querying our database

MATCH (d:Donor)
WHERE d.name =~ ‘.*Bamford.*’
RETURN d
Make the search fuzzy

Querying our database

MATCH (d:Donor)
WHERE d.name =~ ‘(?i).*Bamford.*’
RETURN d
Case insensitive

Querying our database

Challenge
Can you find any Lords in our database?

Querying our database

MATCH (d:Donor)
WHERE d.name =~ ‘Lord.*’
RETURN d

Querying our database


Querying our database

MATCH (d)-[t:DONATED_TO]->(r)
WHERE d.name =~ ‘.*Bamford.*’
RETURN DISTINCT r.name, d.name

Querying our database

MATCH (d)-[t:DONATED_TO]->(r)
WHERE t.value >= 100000
RETURN d

Further resources
Whenever you’re writing Cypher, it’s useful to have the Refcard up.
This is a brief one-page description of everything you can do with Cypher.
It doesn’t go into a lot of detail, but it’s great for reminding you of syntax.
Find it now -- Google for: ‘cypher refcard’

Further resources
What the MATCH looks like on the refcard.
There’s some more complex things we haven’t covered, like matching relationships.


neo4j.com/sandbox
Further resources
The Neo4j Sandbox at neo4j.com/sandbox has some good resources for getting started with graphs.
This would be a good next step.
You can load in data from Twitter or the public Panama Papers data and then explore.

Leila Haddou


@leilahaddou

leila.haddou@gmail.com



## The problem

First, let\'s visit [a website](https://www.washingtonpost.com/).


It looks so nice! So wonderful! Try to pick out the **titles**, the **bylines**, the **article summaries** and the **pictures that go with each article**.

While we see it visually, each page is made up of **code**. We can see that code by right-clicking and selecting **View source**.


Here\'s the source code:


**Discussion:** What does this have to do with the visuals we saw above?


## APIs

An API - Application Programming Interface - is just a way of saying \"things computers can understand.\" Computers can understand this:

``` python
print("Hello world")
```

Computers can also understand this:

``` python
{
    "session": "Hitchhiker's Guide to APIs",
    "type": "hands-on",
    "instructor": "Jonathan Soma"
}
```

We\'re mostly going to be focusing on **web APIs that deal with data.** Kind of, somewhat.

An easy place to track down APIs is **a government open data portal.** You might try [New Orleans\' Open Data Portal](https://data.nola.gov/) and find out it\'s actually pretty rough, and instead meander over to [Baton Rouge\'s Open Data Portal](https://data.brla.gov/) instead. Click **Browse Data** to see all the data they have, and [sort by recently updated](https://data.brla.gov/browse?sortBy=last_modified).

So many things updated in the past day! Amazing! You\'re incredible, Baton Rouge!

**Discussion topic:** What\'s going on?



## Crime, always crime

Everyone\'s favorite topic is **crime**, so let\'s submit to that and [Baton Rouge Crime Incidents](https://data.brla.gov/Public-Safety/Baton-Rouge-Crime-Incidents/fabb-cnnu). We can easily [browse it](https://data.brla.gov/Public-Safety/Baton-Rouge-Crime-Incidents/fabb-cnnu/data) or [download a CSV](https://data.brla.gov/api/views/fabb-cnnu/rows.csv?accessType=DOWNLOAD).

But we\'re here to talk about **APIs**, so let\'s click around under **Export** and find whatever has the word **API** on it.


The **API Endpoint** sounds like something cool and good, let\'s look at it: <https://data.brla.gov/resource/fabb-cnnu.json>

    [{"file_number":"2000020176","offense_date":"2020-03-04T00:00:00.000","offense_time":"0135","crime":"BATTERY","a_c":"COMMITTED","offense":"13:35.3","offense_desc":"DOMESTIC ABUSE BATTERY/CC","address":"3548 RIDGEMONT DR","st_number":"3548","st_name":"RIDGEMONT","st_type":"DR","city":"BATON ROUGE","state":"LA","new_zip":"70814","district":"3","zone":"A","subzone":"3","complete_district":"3A3","council":"5","crime_prevention_dist":"PARK FOREST","geolocation":{"latitude":"30.481541","longitude":"-91.070749","human_address":"{\"address\": \"3548 RIDGEMONT DR\", \"city\": \"BATON ROUGE\", \"state\": \"LA\", \"zip\": \"70815\"}"},":@computed_region_8siy_mghw":"2",":@computed_region_i2e6_956r":"5",":@computed_region_uvg4_nwq8":"18",":@computed_region_idcr_7zcb":"18",":@computed_region_jrqt_zu77":"2",":@computed_region_8tu6_j4iw":"9845",":@computed_region_hfgy_t898":"5",":@computed_region_92rf_uvyc":"1",":@computed_region_9v63_zwfd":"5",":@computed_region_qfmj_2fwi":"57",":@computed_region_tqy7_429i":"25",":@computed_region_tm4z_r3je":"5"}
    ,{"file_number":"2000020144","offense_date":"2020-03-03T00:00:00.000","offense_time":"2331","crime":"CRIMINAL DAMAGE TO PROPERTY","a_c":"COMMITTED","offense":"13:56","offense_desc":"CRIM DAM TO PROP/SIMPLE/CC","address":"12451 CATE AV","st_number":"12451","st_name":"CATE","st_type":"AV","city":"BATON ROUGE","state":"LA","new_zip":"70815","district":"3","zone":"D","subzone":"2","complete_district":"3D2","council":"6","crime_prevention_dist":"NONE","geolocation":{"latitude":"30.463379","longitude":"-91.044452","human_address":"{\"address\": \"12451 CATE AV\", \"city\": \"BATON ROUGE\", \"state\": \"LA\", \"zip\": \"\"}"},":@computed_region_8siy_mghw":"18",":@computed_region_i2e6_956r":"6",":@computed_region_uvg4_nwq8":"29",":@computed_region_idcr_7zcb":"29",":@computed_region_jrqt_zu77":"18",":@computed_region_8tu6_j4iw":"9847",":@computed_region_hfgy_t898":"6",":@computed_region_92rf_uvyc":"46",":@computed_region_9v63_zwfd":"6",":@computed_region_qfmj_2fwi":"42",":@computed_region_tqy7_429i":"11",":@computed_region_tm4z_r3je":"6"}
    .....
    .....
    .....

Uh okay sure, cool, I guess? It looks like it\'s something called **JSON**.


## Being visual about it

We\'ll use [Postman](https://www.postman.com/) to work through this a little bit.


### Using the JSON output

If you aren\'t too sure about how JSON works, you can convert the contents of a lot of APIs into CSV format using [online tools](https://json-csv.com/).



## Being programmers about it

We could also be programmers about it!

``` python
# Requests will download the dataset for us
import requests

response = requests.get('https://data.brla.gov/resource/fabb-cnnu.json')
response.json()
```

``` python
# We could also give it to pandas to turn it into a filterable CSV-y thing

import pandas as pd
pd.set_option("display.max_columns", 100)

response = requests.get('https://data.brla.gov/resource/fabb-cnnu.json')
df = pd.DataFrame(response.json())
df.head()
```

``` python
# Just like Postman, we can use filters!
response = requests.get('https://data.brla.gov/resource/fabb-cnnu.json?offense_desc=ASSAULT/AGG')
df = pd.DataFrame(response.json())
df.head()
```


## APIs for APIs

What\'s up with the [API documenation page](https://dev.socrata.com/foundry/data.brla.gov/fabb-cnnu)? We love Python and know the word \"pandas\" so let\'s click \"Python pandas.\"


It seems to have a lot of the same kind of words (?), but it doesn\'t have a URL in there. But it gets the data, right?

This is a **different kind of API**. It\'s a **Python library API** instead of a **web API**. This means it\'s a way of talking to *Python* instead of a way of talking to the *web*. Behind the scenes Python is talking to the web API for you and doing the dirty work of putting all those parameters in the URL and making the request.

Why\'s this a big deal? Sometimes it\'s just easier to write Python than trying to talk to a URL! Not always, but sometimes.

**Let\'s do it!** We\'ll first install the library that Socrata Open Data uses in the code above, `sodapy`.

``` python
# Install sodapy
!pip install sodapy
```

Now we can adapt the code from the example.

``` python
from sodapy import Socrata

# Connect to Baton Rouge Open Data
client = Socrata("data.brla.gov", None)

# Ask for this dataset, 200 rows
results = client.get("fabb-cnnu", limit=200)

# Send it to pandas
results_df = pd.DataFrame.from_records(results)
results_df.head()
```

### Changing up cities

We can do this [from anywhere](https://controllerdata.lacity.org/Revenue/city-revenue-by-month-transportation/ymah-xfmh)

``` python
client = Socrata("controllerdata.lacity.org", None)

# load the data
crime_df = pd.DataFrame(client.get('ymah-xfmh', limit=10))
crime_df.head()
```



## API keys

We keep getting a weird warning:

    WARNING:root:Requests made without an app_token will be subject to strict throttling limits.

Sometimes you need to tell the API who you are! That way it can be rude to the people who use it too much or charge you money or whatever. We\'ll come back to that in a little bit.

``` python
```

# Other APIs

While Socrata runs a lot of Open Data portals and standardizes the way you interact with them, almost every other API is totally unique! Let\'s visit the weather service [Dark Sky](http://darksky.net/) and sign up for an account.

Once you click into the developer section, it gives you a nice example API call. How nice! But wait, **why\'s the URL look so weird?**


## API keys

When you use some APIs, you need to prove who you are in order for them to allow you to use the service. Socrata will allow you to make a few calls without signing up, but Dark Sky demands that you always always always have an API key.

- API keys are sometimes **in the URL:** <http://www.example.com/api/d34db33f/planets>
- API keys are sometimes **a parameter in the URL:** <http://www.example.com/api/planets?api_key=d34db33f>
- API keys are sometimes **separate keys you have to combine using a terrible thing called OAuth that we won\'t talk about here,** but oh boy I hope you\'re using a library if you run into that.
- **Signed requests** use the API key and a little bit of encryption magic to confirm that yes, it\'s you, and yes, that\'s exactly the request you wanted to make. If you run across these it\'s also best to switch to a library.



## Using Postman

Let\'s start by testing out the DarkSky URL using Postman, and seeing how to adjust it to import the data for another location.


## Using Python

Now let\'s try using Python/pandas. It\'s going to be a little different than last time!

``` python
response = requests.get('https://api.darksky.net/forecast/15074402c474e3dab67f7377e1f95519/48.8267,-74.4233')
pd.DataFrame(response.json()['hourly']['data'])
```



## Using Python, v2

Are there Python bindings for the API?

``` python
!pip install darksky_weather
```

``` python
from darksky.api import DarkSky, DarkSkyAsync
from darksky.types import languages, units, weather

API_KEY = '15074402c474e3dab67f7377e1f95519'

# Synchronous way
darksky = DarkSky(API_KEY)

latitude = 42.3601
longitude = -71.0589
forecast = darksky.get_forecast(
    latitude, longitude,
    extend=False, # default `False`
    lang=languages.ENGLISH, # default `ENGLISH`
    values_units=units.AUTO, # default `auto`
    exclude=[weather.MINUTELY, weather.ALERTS], # default `[]`,
    timezone='UTC' # default None - will be set by DarkSky API automatically
)
```

``` python
forecast.currently.temperature
```

``` python
```

# Secret APIs

Socrata APIs are usually useless since the data often also comes as a CSV. Other APIs are often useless because you can just use a library instead of beautiful hand-crafted web urls.

But there\'s one very very very important time that APIs are useful: **super secret website APIs!** If you\'ve ever tried to scrape a site and failed because the URLs didn\'t seem to \"work right,\" let\'s show the best-kept secret of scraping: skipping scraping at all, and using the provider\'s unadvertised API!

``` python
```

# Other APIs

While data APIs are the most common kind in data journalism, once you know how APIs work there are many, many others that you might want to use.

- **Geocoding APIs** can convert locations into latitude and longitude. Google Maps has a good one (sining up for billing is a bit complicated) while the Census Bureau has a free one (but slow and somewhat picky).
- **Communication APIs** enable you to text or call (Twilio) or send emails (Mailgun, Sendgrid).
- **Billing APIs** can be used to charge people money. Stripe has high fees but excellent documentation, while you can also use ones like Paypal.

For most of these APIs they\'ll offer up both a talk-directly-to-a-URL API, as well as a official or unofficial libraries. Which one you use is up to you, go with whatever you feel more comfortable with.

``` python
```


## The problem

First, let\'s visit [a website](https://www.washingtonpost.com/).


It looks so nice! So wonderful! Try to pick out the **titles**, the **bylines**, the **article summaries** and the **pictures that go with each article**.

While we see it visually, each page is made up of **code**. We can see that code by right-clicking and selecting **View source**.


Here\'s the source code:


**Discussion:** What does this have to do with the visuals we saw above?



## APIs

An API - Application Programming Interface - is just a way of saying \"things computers can understand.\" Computers can understand this:

``` python
print("Hello world")
```

Computers can also understand this:

``` python
{
    "session": "Hitchhiker's Guide to APIs",
    "type": "hands-on",
    "instructor": "Jonathan Soma"
}
```

We\'re mostly going to be focusing on **web APIs that deal with data.** Kind of, somewhat.

An easy place to track down APIs is **a government open data portal.** You might try [New Orleans\' Open Data Portal](https://data.nola.gov/) and find out it\'s actually pretty rough, and instead meander over to [Baton Rouge\'s Open Data Portal](https://data.brla.gov/) instead. Click **Browse Data** to see all the data they have, and [sort by recently updated](https://data.brla.gov/browse?sortBy=last_modified).

So many things updated in the past day! Amazing! You\'re incredible, Baton Rouge!

**Discussion topic:** What\'s going on?


## Crime, always crime

Everyone\'s favorite topic is **crime**, so let\'s submit to that and [Baton Rouge Crime Incidents](https://data.brla.gov/Public-Safety/Baton-Rouge-Crime-Incidents/fabb-cnnu). We can easily [browse it](https://data.brla.gov/Public-Safety/Baton-Rouge-Crime-Incidents/fabb-cnnu/data) or [download a CSV](https://data.brla.gov/api/views/fabb-cnnu/rows.csv?accessType=DOWNLOAD).

But we\'re here to talk about **APIs**, so let\'s click around under **Export** and find whatever has the word **API** on it.


The **API Endpoint** sounds like something cool and good, let\'s look at it: <https://data.brla.gov/resource/fabb-cnnu.json>

    [{"file_number":"2000020176","offense_date":"2020-03-04T00:00:00.000","offense_time":"0135","crime":"BATTERY","a_c":"COMMITTED","offense":"13:35.3","offense_desc":"DOMESTIC ABUSE BATTERY/CC","address":"3548 RIDGEMONT DR","st_number":"3548","st_name":"RIDGEMONT","st_type":"DR","city":"BATON ROUGE","state":"LA","new_zip":"70814","district":"3","zone":"A","subzone":"3","complete_district":"3A3","council":"5","crime_prevention_dist":"PARK FOREST","geolocation":{"latitude":"30.481541","longitude":"-91.070749","human_address":"{\"address\": \"3548 RIDGEMONT DR\", \"city\": \"BATON ROUGE\", \"state\": \"LA\", \"zip\": \"70815\"}"},":@computed_region_8siy_mghw":"2",":@computed_region_i2e6_956r":"5",":@computed_region_uvg4_nwq8":"18",":@computed_region_idcr_7zcb":"18",":@computed_region_jrqt_zu77":"2",":@computed_region_8tu6_j4iw":"9845",":@computed_region_hfgy_t898":"5",":@computed_region_92rf_uvyc":"1",":@computed_region_9v63_zwfd":"5",":@computed_region_qfmj_2fwi":"57",":@computed_region_tqy7_429i":"25",":@computed_region_tm4z_r3je":"5"}
    ,{"file_number":"2000020144","offense_date":"2020-03-03T00:00:00.000","offense_time":"2331","crime":"CRIMINAL DAMAGE TO PROPERTY","a_c":"COMMITTED","offense":"13:56","offense_desc":"CRIM DAM TO PROP/SIMPLE/CC","address":"12451 CATE AV","st_number":"12451","st_name":"CATE","st_type":"AV","city":"BATON ROUGE","state":"LA","new_zip":"70815","district":"3","zone":"D","subzone":"2","complete_district":"3D2","council":"6","crime_prevention_dist":"NONE","geolocation":{"latitude":"30.463379","longitude":"-91.044452","human_address":"{\"address\": \"12451 CATE AV\", \"city\": \"BATON ROUGE\", \"state\": \"LA\", \"zip\": \"\"}"},":@computed_region_8siy_mghw":"18",":@computed_region_i2e6_956r":"6",":@computed_region_uvg4_nwq8":"29",":@computed_region_idcr_7zcb":"29",":@computed_region_jrqt_zu77":"18",":@computed_region_8tu6_j4iw":"9847",":@computed_region_hfgy_t898":"6",":@computed_region_92rf_uvyc":"46",":@computed_region_9v63_zwfd":"6",":@computed_region_qfmj_2fwi":"42",":@computed_region_tqy7_429i":"11",":@computed_region_tm4z_r3je":"6"}
    .....
    .....
    .....

Uh okay sure, cool, I guess? It looks like it\'s something called **JSON**.



## Being visual about it

We\'ll use [Postman](https://www.postman.com/) to work through this a little bit.


### Using the JSON output

If you aren\'t too sure about how JSON works, you can convert the contents of a lot of APIs into CSV format using [online tools](https://json-csv.com/).


## Being programmers about it

We could also be programmers about it!

``` python
# Requests will download the dataset for us
import requests

response = requests.get('https://data.brla.gov/resource/fabb-cnnu.json')
response.json()
```

``` python
# We could also give it to pandas to turn it into a filterable CSV-y thing

import pandas as pd
pd.set_option("display.max_columns", 100)

response = requests.get('https://data.brla.gov/resource/fabb-cnnu.json')
df = pd.DataFrame(response.json())
df.head()
```

``` python
# Just like Postman, we can use filters!
response = requests.get('https://data.brla.gov/resource/fabb-cnnu.json?offense_desc=ASSAULT/AGG')
df = pd.DataFrame(response.json())
df.head()
```



## APIs for APIs

What\'s up with the [API documenation page](https://dev.socrata.com/foundry/data.brla.gov/fabb-cnnu)? We love Python and know the word \"pandas\" so let\'s click \"Python pandas.\"


It seems to have a lot of the same kind of words (?), but it doesn\'t have a URL in there. But it gets the data, right?

This is a **different kind of API**. It\'s a **Python library API** instead of a **web API**. This means it\'s a way of talking to *Python* instead of a way of talking to the *web*. Behind the scenes Python is talking to the web API for you and doing the dirty work of putting all those parameters in the URL and making the request.

Why\'s this a big deal? Sometimes it\'s just easier to write Python than trying to talk to a URL! Not always, but sometimes.

**Let\'s do it!** We\'ll first install the library that Socrata Open Data uses in the code above, `sodapy`.

``` python
# Install sodapy
!pip install sodapy
```

Now we can adapt the code from the example.

``` python
from sodapy import Socrata

# Connect to Baton Rouge Open Data
client = Socrata("data.brla.gov", None)

# Ask for this dataset, 200 rows
results = client.get("fabb-cnnu", limit=200)

# Send it to pandas
results_df = pd.DataFrame.from_records(results)
results_df.head()
```

### Changing up cities

We can do this [from anywhere](https://controllerdata.lacity.org/Revenue/city-revenue-by-month-transportation/ymah-xfmh)

``` python
client = Socrata("controllerdata.lacity.org", None)

# load the data
crime_df = pd.DataFrame(client.get('ymah-xfmh', limit=10))
crime_df.head()
```


## API keys

We keep getting a weird warning:

    WARNING:root:Requests made without an app_token will be subject to strict throttling limits.

Sometimes you need to tell the API who you are! That way it can be rude to the people who use it too much or charge you money or whatever. We\'ll come back to that in a little bit.

``` python
```

# Other APIs

While Socrata runs a lot of Open Data portals and standardizes the way you interact with them, almost every other API is totally unique! Let\'s visit the weather service [Dark Sky](http://darksky.net/) and sign up for an account.

Once you click into the developer section, it gives you a nice example API call. How nice! But wait, **why\'s the URL look so weird?**



## API keys

When you use some APIs, you need to prove who you are in order for them to allow you to use the service. Socrata will allow you to make a few calls without signing up, but Dark Sky demands that you always always always have an API key.

- API keys are sometimes **in the URL:** <http://www.example.com/api/d34db33f/planets>
- API keys are sometimes **a parameter in the URL:** <http://www.example.com/api/planets?api_key=d34db33f>
- API keys are sometimes **separate keys you have to combine using a terrible thing called OAuth that we won\'t talk about here,** but oh boy I hope you\'re using a library if you run into that.
- **Signed requests** use the API key and a little bit of encryption magic to confirm that yes, it\'s you, and yes, that\'s exactly the request you wanted to make. If you run across these it\'s also best to switch to a library.


## Using Postman

Let\'s start by testing out the DarkSky URL using Postman, and seeing how to adjust it to import the data for another location.



## Using Python

Now let\'s try using Python/pandas. It\'s going to be a little different than last time!

``` python
response = requests.get('https://api.darksky.net/forecast/15074402c474e3dab67f7377e1f95519/48.8267,-74.4233')
pd.DataFrame(response.json()['hourly']['data'])
```


## Using Python, v2

Are there Python bindings for the API?

``` python
!pip install darksky_weather
```

``` python
from darksky.api import DarkSky, DarkSkyAsync
from darksky.types import languages, units, weather

API_KEY = '15074402c474e3dab67f7377e1f95519'

# Synchronous way
darksky = DarkSky(API_KEY)

latitude = 42.3601
longitude = -71.0589
forecast = darksky.get_forecast(
    latitude, longitude,
    extend=False, # default `False`
    lang=languages.ENGLISH, # default `ENGLISH`
    values_units=units.AUTO, # default `auto`
    exclude=[weather.MINUTELY, weather.ALERTS], # default `[]`,
    timezone='UTC' # default None - will be set by DarkSky API automatically
)
```

``` python
forecast.currently.temperature
```

``` python
```

# Secret APIs

Socrata APIs are usually useless since the data often also comes as a CSV. Other APIs are often useless because you can just use a library instead of beautiful hand-crafted web urls.

But there\'s one very very very important time that APIs are useful: **super secret website APIs!** If you\'ve ever tried to scrape a site and failed because the URLs didn\'t seem to \"work right,\" let\'s show the best-kept secret of scraping: skipping scraping at all, and using the provider\'s unadvertised API!

``` python
```

# Other APIs

While data APIs are the most common kind in data journalism, once you know how APIs work there are many, many others that you might want to use.

- **Geocoding APIs** can convert locations into latitude and longitude. Google Maps has a good one (sining up for billing is a bit complicated) while the Census Bureau has a free one (but slow and somewhat picky).
- **Communication APIs** enable you to text or call (Twilio) or send emails (Mailgun, Sendgrid).
- **Billing APIs** can be used to charge people money. Stripe has high fees but excellent documentation, while you can also use ones like Paypal.

For most of these APIs they\'ll offer up both a talk-directly-to-a-URL API, as well as a official or unofficial libraries. Which one you use is up to you, go with whatever you feel more comfortable with.

``` python
```



## Removing `__MACOSX` file from zip file

After compressing, do:

```
zip -d bikes_data.zip "__MACOSX*"
zip -d bikes_data.zip "*.DS_Store"

zip -d austin_tweet_data.zip "__MACOSX*"
zip -d austin_tweet_data.zip "*.DS_Store"

aws s3 cp chopper_data.zip s3://qz-aistudio-public/workshops/chopper_data.zip --acl public-read

```


## Seconds in the file name:

https://stackoverflow.com/questions/50099869/ffmpeg-output-images-filename-with-time-position

```
ffmpeg -i source -vf fps=1,select='not(mod(t,5))' -vsync 0 -frame_pts 1 %d.jpg

or

ffmpeg -i source -vf fps=1 -vsync 0 -frame_pts 1 %04d.jpg
```



## Jeremy's code for listing the confusing images

```
interp = ClassificationInterpretation.from_learner(learn)
losses,idxs = interp.top_losses()

for p in learn.data.valid_ds.x.items[idxs]:
  print(p, )
```


## Managing the facebook files

Jeremy's 1,700 categorizations were in JSONL format. To turn that into a csv with just the fields I wanted,
I used the command-line tool `json2csv`:

```
npm install -g json2csv
node json2csv --input only_labeled.jsonl --output ads_and_categories.csv --ndjson --fields "text","label"
```

The ads file downloaded from ProPublica was 3GB and contained 165,000 lines.

```
$ wc -l fbpac-ads-en-US.csv 
  164600 fbpac-ads-en-US.csv
```

Then took a slice:

```
tail -n 5000 fbpac-ads-en-US.csv > fbpac-ads-en-US-slice.csv
```



## Welcome

The code here supports workshops taught by members of the Quartz, helping journalists learning machine learning.

The key materials are in the `notebooks` folder. More on that below.


## Videos

Many of the notebooks in the `notebooks` folder pair up with [a set of videos](https://qz.ai/series-machine-learning-videos/) originally recorded for an online class provided by the [UT Knight Center for Journalism in the Americas](https://knightcenter.utexas.edu/). They are now online for free!



## A note about notebooks

These workshops exist in Jupyter Notebooks (formerly IPython notebooks, which is why notebook files end in `.ipynb`). Because we'll be doing machine learning, we also need a GPU, which is a fast parallel-processor that speeds up the math we use for training models. 

At the time of this writing, the [Google Colaboratory](https://colab.research.google.com) platform provides both a notebook enviroment _and_ a GPU for free. So these notebooks are designed to work particularly well with Google Colab.

If you know how to spin up another platform – such as Amazon's EC2 – the notebooks should work there, too.


## Getting started, with Google Colab

Here's how to get started with these workshops using Google Colaboatory.

- Go to [Google Colaboratory](https://colab.research.google.com).
- In the top bar of the welcome window, pick "Github."
- Enter `quartz` on the long blue line and press Return.

 

- From the list that appears, make sure `aistudio-workshops` is the selected repository and then click on the notebook for the lesson you'd like.

 

- For many (though not all) of these lessons, we'll want to turn on the GPU. From the "Runtime" menu, pick "Change runtime type."

 

- Then form the "Hardware accellerator" dropdown, pick "GPU."

 

- You want to run the first code cell in the notebook, by tapping the "play" button on the cell that includes the code `## ALL GOOGLE COLAB USERS RUN THIS CELL`

 

- You may get one or two warnings, which you can safely dismiss:

 

 

You're all set!



## More resources

- Examples, walk-throughs and other materials are available at the [Quartz AI Studio](https://qz.ai) website.
- Many of the projects here use the great library made by [fast.ai](https://fast.ai)
- Some of the notebooks are also based on what we learned taking fast.ai's great [practical deep learning class](https://course.fast.ai/), which you should consider, too!


## Resources

- Quartz AI Studio: <https://qz.ai>
- fast.ai: <https://fast.ai>
- practical deep learning: <https://course.fast.ai/>



## A note about notebooks

These workshops exist in Jupyter Notebooks (formerly IPython notebooks, which is why notebook files end in `.ipynb`{style="font-family: Menlo, Consolas, \"DejaVu Sans Mono\", monospace;"}). Because we\'ll be doing machine learning, we also need a GPU, which is a fast parallel-processor that speeds up the math we use for training models.

At the time of this writing, the [Google Colaboratory](https://colab.research.google.com) platform provides both a notebook enviroment *and* a GPU for free. So these notebooks are designed to work particularly well with Google Colab.

If you know how to spin up another platform -- such as Amazon\'s EC2 -- the notebooks should work there, too.


## Getting started, with Google Colab

Here\'s how to get started with these workshops using Google Colaboatory.

- Go to [Google Colaboratory](https://colab.research.google.com).
- In the top bar of the welcome window, pick \"Github.\"
- Enter `quartz`{style="font-family: Menlo, Consolas, \"DejaVu Sans Mono\", monospace;"} on the long blue line and press Return.


- From the list that appears, make sure `aistudio-workshops`{style="font-family: Menlo, Consolas, \"DejaVu Sans Mono\", monospace;"} is the selected repository and then click on the notebook for the lesson you\'d like.


- For many (though not all) of these lessons, we\'ll want to turn on the GPU. From the \"Runtime\" menu, pick \"Change runtime type.\"


- Then form the \"Hardware accellerator\" dropdown, pick \"GPU.\"


- You want to run the first code cell in the notebook, by tapping the \"play\" button on the cell that includes the code `## ALL GOOGLE COLAB USERS RUN THIS CELL`{style="font-family: Menlo, Consolas, \"DejaVu Sans Mono\", monospace;"}


- You may get one or two warnings, which you can safely dismiss:


You\'re all set!


