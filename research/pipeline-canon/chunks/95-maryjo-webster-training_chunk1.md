<!-- chunk: 1/1 | source: 95-maryjo-webster-training.md | words: 19341 -->
<!-- headings: DataJ; BeginnerExcel; Data Journalism: Beginner Excel; [By MaryJo Webster](https://twitter.com/MaryJoWebster); Looking around Excel; Key terms; Cursors; Prepping your data; Sorting; Prep for analysis; How do I\.....?; How formulas work; Percent change; SUM function; Percent of total; AVERAGE and MEDIAN functions; Shortcuts and other useful tricks; StribDataAcademy2019; Star Tribune Data Academy; To read ahead of time: -->

# DataJ
Data Journalism training materials created by @MaryJoWebster


---

MaryJo Webster PGP Fingerprint: 5EE8 3F00 F074 B05A CEC2 8ABC 8430 71A9 BFC9 AD62


---

# BeginnerExcel

::::::::::::::::: inner
# Data Journalism: Beginner Excel

## [By MaryJo Webster](https://twitter.com/MaryJoWebster)

------------------------------------------------------------------------

This tipsheet is specific to Microsoft Excel (2007 and newer) for Windows, however other spreadsheet software - such as Google Sheets - have the same functionality. Of course, the buttons and specific ways to do things might be different. But I often find answers by doing a web search using the Excel terms (i.e. how to format cells in Google Sheets). Excel for Mac has all the same functions, but looks slightly different, especially in terms of where buttons and various tools are stored.

------------------------------------------------------------------------

### Looking around Excel

This tutorial uses a spreadsheet called [MLBPayrolls](http://mjwebster.github.io/DataJ/spreadsheets/MLBpayrolls.xls){target="_blank"}

First, a few things about spreadsheets: Each sheet is made up of columns (labeled by letters) and rows (labeled by numbers). Each cell is identified by a cell address, consisting of the letter and number. For example, in this picture, the value Atlanta Braves is stored in cell A3. Note that when the cursor is on a cell, the cell is outlined in black. Note the small black square in the corner \-- we\'ll be using that in a couple minutes. Also note that the letter and number are highlighted in grey and the cell address is displayed in the upper left corner of the sheet. If you\'ve ever played the board game \"Battleship,\" you\'ll find this similar.

![A look around Excel](https://user-images.githubusercontent.com/4182043/32186288-b62e23a0-bd6f-11e7-83d9-ee83d9671f60.gif)

You\'ll also notice that your cursor will change as you move it around. Most of the time, it will look like a big fat white plus sign. But if you hover over the top of the black box (around Atlanta Braves) you will get a tool that allows you to move that cell and if you hover in the lower right corner - where that little black square is - you will get a thin black cross. That thin black cross is used for copying formulas down or across the page. We\'ll be using that a lot.

![Cursors](https://user-images.githubusercontent.com/4182043/32197007-a8509a08-bd90-11e7-9bf6-bb1d964c0f02.gif)

### Key terms

- **Columns** contain \"categories\" of data and are vertical
- **Rows** contain invidivdual records and are horizontal
- A **cell address** consists of a letter followed by a number, i.e. \"B4\"
- Each Excel file is described as a **workbook** which can contain multiple **worksheets**
- The **formula bar**, which is located in the menu bar, is similar to the address bar in a web browser. Here you can view and edit formulas that you\'ve created in the worksheet.

### Cursors

![Cursors list](https://user-images.githubusercontent.com/4182043/32188569-2f5a72e6-bd76-11e7-8803-38ab6c047761.png)

### Prepping your data

- Make sure the columns are labeled and that the column label only takes up one row.
- Any notes or titles \--or anything else that might be above or below the data table \-- should be separated from the data by a blank row (or more). Your data won\'t sort correctly if other information butts up against the table.
- No empty rows or empty columns within the area where the data is located.

![Prepping data](https://user-images.githubusercontent.com/4182043/32189314-69ed15c4-bd78-11e7-86e8-08028f851dbd.gif)

### Sorting

There are several ways to change the order that the rows appear in. I\'m purposely NOT going to show you the shortcut methods because they don\'t give you the full suite of options for sorting.

First thing to note: Sorting won\'t work correctly if you don\'t have your data set up properly, following the guidelines I noted in the previous section.

Second: Put your cursor somewhere in the chunk of data. Doesn\'t matter exactly where. Key thing is you don\'t want it parked out in the whitespace.

Third: Go to the data menu. Click the big button labeled \"Sort\". This will bring up a dialogue box. Look to see if the checkbox \"My data has headers\" is checked. If it\'s not, this is usually a sign that your data is not set up properly. Once that\'s checked, then the pull-down menu on the left will list the column labels in your data. Select the column label you want to sort on \-- in the example, I\'ve chosen Payroll2016 \-- and then you can select the order, either Smallest to Largest (ascending) or Largest to smallest (descending).

Note that if you choose the TEAM field, those options will be A to Z and Z to A. That\'s because TEAM consists of \"characters\". The Payroll2016 field consists of numbers only (numeric field).

![Sorting](https://user-images.githubusercontent.com/4182043/32190431-db989bfa-bd7b-11e7-95b4-be95187e2637.gif)

### Prep for analysis

The first thing to do is to make sure you understand what you\'re looking at.

What does each row represent? In this case, it\'s one row for each team, showing the total they spent on payroll in various years.

Are there any columns you don\'t understand? This data is pretty straightforward, showing that we have payroll totals for various years (but note that the years are not consecutive). Sometimes, though, you\'ll get data with a field that has codes in it or something that you don\'t understand. Be sure to go back to the place you got the data and get your questions answered.

Do you have all the data you need? In this case, the obvious questions might be to ensure you have all the teams you want and that you have payroll totals for all the years you want.

Is there anything missing that would be useful for our analysis? For example, I might want to add a column that indicates which league (AL or NL) each team plays in. It\'s quite common to need to add something to your data to make it more valuable. (We\'re not going to do that here, though)

Then you want to come up with the questions you want to ask. We\'re going into an \"interview,\" so it\'s a good idea to have a list of questions at the ready. But just like an interview with a human, it\'s okay to veer off your list at some point later. It helps, though, to have something to start with.

If you\'re having a hard time coming up with questions, start thinking of the 5 W\'s \-- who, what, when, where, why. Data is really bad at answering the \"why\" questions, but the others are easier. With this data, our \"who\" are the teams. We\'ve also got \"when\" since we have different points in time. The more detailed your data is, the more questions you will be able to ask. This dataset is very limited.

### How do I\.....?

There are two primary ways to do analysis in Excel. One is by creating new columns or rows to store the results of any formulas you run \-- such as creating a new column with percent change or creating a new row with a grand total that combines all the rows. The other is to use PivotTables to generate summaries, either counting rows or summing values together. We\'ll save PivotTables for the next tutorial (however, I\'ll note here that it\'s my favorite tool in Excel).

There are oodles of ways to use formulas and built-in Excel functions to do math, re-arrange your data, clean your data, or even generate new columns to add to your data table. I\'m going to focus on a few formulas and built-in math functions that are very commonly used \-- percent change, percent of total, average and median.

#### How formulas work

A [formula](https://support.office.com/en-us/article/Overview-of-formulas-in-Excel-ecfdc708-9162-49e8-b993-c311f47ca173) performs calculations or other actions on the data. It always starts with an equal sign (=), but after that there\'s a wide array of things you can do, including math calculations and using [built-in Excel functions.](https://support.office.com/en-us/article/Excel-functions-by-category-5f91f4e9-7b42-46d2-9bd1-63f26a86c0eb?ui=en-US&rs=en-US&ad=US) You type a formula either in a blank column to the right of your data, or in a blank row below your data. And you refer to the cell addresses, instead of the actual values. This allows you to type a math formula one time, then copy the formula and apply it to all the rows or columns of data. As a result, you can do something like calculate percent change for thousands of rows of data in a few seconds. Can you imagine trying to do that on a calculator?

In the video below, I\'m going to create two new columns on my table where I\'m going to use math formulas to calculate the dollar difference for each department\'s annual budget figures and then express those differences as percent change. I\'ll also add some new rows below my data, but I\'m keeping it separate with a blank row because these are totals that I don\'t want mixed into my data table the next time I use sort. I\'ll cover specifically how to do these formulas and functions later in the tutorial.

Note that I start each with an equal sign, then when I\'m finished typing I hit enter. Now my cursor is on the row below. So I need to put my cursor back on the cell where I did the formula, and get the \"black thin cross\" cursor to copy down my formula to the other rows (or in a couple cases, I copy across columns). You\'ll notice that you can either drag the thin cross, or you can double-click on your mouse and it will go down until it hits a blank cell in the column immediately to the left. As you copy down, Excel guesses that you want the formula to switch to the next row number. As you copy across, it knows that you want to stay on the same row, but switch to a new column letter.

![Formula basics](https://user-images.githubusercontent.com/4182043/32195406-28d75f96-bd8b-11e7-87dc-f09e596208e0.gif)

#### Percent change

One of the questions you likely came up with for our data is: Which team had the greatest increase (or decrease) in total payroll? So then the next step is to figure out which \"tool\" in Excel will get us that answer. Here\'s where you actually need to know a little bit about best practices in math and statistics first.

Let\'s focus in on two teams, the New York Yankees and the Oakland Athletics. The Yankees paid out more than \$222 million in 2016; the Athletics paid out just over \$86 million. If we calculate a simple difference between the 2016 and 2011, both teams show that they spent about \$20 million more in 2016 than they did in 2011. However, think about these like you would a city budget. A \$20 million increase is a drop in the bucket for a city that routinely spends \$200 million, while it\'s a huge increase for the city that spends \$60 or \$80 million, right?

![Percent change explained](https://user-images.githubusercontent.com/4182043/32194510-97775670-bd88-11e7-96eb-7166e21c18f6.gif)

General rule of thumb is that you\'ll want to use percent change (rather than simple subtraction) in any situation where the things you are comparing (city budgets, county populations, city crime totals, state spending, school enrollments) have a lot of underlying variability like we have here.

So, let\'s go back to our full dataset and create a new column to calculate percent change between our two most recent years. I\'ll add a column label in the first empty column.

The best way to remember the percent change formula is that it\'s NEW NUMBER minus OLD NUMBER divided by OLD NUMBER. A shorthand way to remember it is the word NO \-\-- (N-O)/O.

This will give you a positive number if it\'s an increase and a negative number if it\'s a decrease. Note in the video that after I typed the formula, I ended up with a value expressed in dollars. So I use the format cells option to change it to percentage.

![Percent change](https://user-images.githubusercontent.com/4182043/32194513-99c556a2-bd88-11e7-8b91-e341ffc867c1.gif)

#### SUM function

This data is a good example of a situation where we might want a grand total \-- the total spent on payroll across the whole baseball league. The data didn\'t come with a total, but even if it did, I\'d recommend calculating your own total just to check their work. (I\'ve seen front page stories where news organizations discovered errors in city government totals).

When you have a big column of numbers, the easiest way to get a grand total for a column (or a row) is to use the SUM function. The SUM function requires that you give it a \"range\" where the data is located. In this case, our data for the first year is stored in cells B3 through B32. The next year of data is C3 to C32, etc. I\'m going to add a blank row at row 34, and in cel B34 we\'ll type our formula: =SUM(b3:b32). Then you can copy that across to the other columns and Excel will automatically adjust the formula, assuming you want to switch to C3:C32 and D3:d32, etc.

![SUM function](https://user-images.githubusercontent.com/4182043/32198138-dc44c1dc-bd94-11e7-8aca-b4fcb2f60bc2.gif)

#### Percent of total

We might also want to know what percent of all money spent across the league is made up by the Yankees\' monstrous payroll. To do that, we\'d calculate percent of total. It will work best if we generate that calculation for all the teams so that we can see how they all compare to each other. In other words, how big is each slice of the pie?

The math for percent of total is to take the team amount and divide by a total for the whole league. It\'s a good thing, then, that we just calculated those totals in the step above. For this one, we\'ll just calculate the percent of total for the most recent year and we\'ll put that in the first blank column to the right of our data. Our formula will be the first team\'s value for 2016 \-- located in cell I3 \-- divided by the league total \-- located in cell I34. However, if we run that it works for the first row but we get an error message on the subsequent rows. If you look at the formula for the second row, you can see the problem. Excel guessed that you wanted to change the formula to I4/I35. You can see that I4 is correct, but what\'s in I35? Nothing.

So we need to tell Excel to ALWAYS stay on I35. This is called an anchor. Excel uses a dollar sign (\$) as an anchor. If you put a dollar sign in front of the letter in the cell address, it will always stay on the I column, but the row number could adjust automatically. If you put a dollar sign in front of the number in the cell address, it will stay on the row, but could adjust column letter if you copy across. Or you can put dollar signs in both positions to lock on that one cell. That\'s what we\'ll do here. (And yes, there are situations where you only want to anchor one but not the other.)

So go back to the original formula in I3 and adjust the formula \-- **=I3/\$I\$34** and then copy that down.

![Percent of total](https://user-images.githubusercontent.com/4182043/32198179-09107af8-bd95-11e7-8663-a566639c02b9.gif)

#### AVERAGE and MEDIAN functions

Just like how we totaled a column of numbers using the SUM function, we can also calculate the average or the median for a given column, using the AVERAGE and MEDIAN functions that are built into Excel. It works the same way: =AVERAGE(B3:B32) or =MEDIAN(B3:b32)

The rule of thumb in using average versus median is that you should use median (which returns the middle value) in situations where you have big outliers \-- either a few values that are really low or really high compared to the majority of the other values. This happens a lot with salary records or home sale prices, for example. You can test whether a median is warranted by calculating both on your dataset. If the two numbers are close together, you\'ll be okay using average. If they are not, then use the median.

![AVERAGE and MEDIAN functions](https://user-images.githubusercontent.com/4182043/32231559-eda51f0a-be23-11e7-874a-e3c609613ec1.gif)

### Shortcuts and other useful tricks

**To highlight your block of data**, put your cursor somewhere in the middle of your data, then push control-shift-asterisk (\*) at the same time. (Only works in Windows)

**To check the four corners of your highlighted data chunk**, highlight your data (using the trick we just mentioned), then push control-period (.) at the same time. And repeat this four times. Each time you push the keys, it will go to a different corner of the data. This is useful for mkaing sure you have highlighted the full chunk (and nothing extraneous) before sorting or copying.

**Freeze panes** is a useful way to keep your headers at the top of the page, so you can see them when you scroll down a big dataset. Place your cursor in the cell just below the row you want to lock into place (usually this would be somewhere around A2 or A3, depending which row your data starts on). Then go to the View menu and select \"Freeze panes.\" It will give you several options, such as freezing the top row or freezing one or more columns on the left, plus the top row.

**To return to the top of your data** push control and home keys at the same time. It will take you to A1.

**To highlight an entire column** put your cursor on the first cell of data, then push control-shift and the down arrow key. It will highlight all the way down until it hits a blank row. It works the same for rows, except you would push control-shift and the right arrow key.

**Paste Special** allows you to get rid of formulas, so that only the answers remain. Think carefully about whether you want to do this, though. Sometimes leaving the formulas there gives you a sort of \"paper trail\" of what you did, or allows others to see what you did. To use Paste Special, highlight the row(s) or column(s) that have the formulas. Copy the data using Ctrl-C or the copy button. Then put your cursor where you want to paste the data and right-mouse click, then choose \"Paste Special.\" A little box will come up: Under the Psate section at the top, choose \"Values\" and push OK.

**Hide columns:** You can hide columns to get them out of your way or to avoid printing them by highlighting the columns you want (click on teh letter at the top of the column) and right-mouse click to choose \"Hide columns.\" The columns will disappear. To get them back, highlight the two columns on either side of the ones that are missing and right-mouse click and choose \"Unhide columns.\"

**Add columns or rows:** To add a new column in the middle of your data, click on the letter of the column immediately to the RIGHT of where you want the new column. Make sure the whole column is highlighted (if you click on the letter above the column Excel will automatically highlight the whole column). Then right-mouse click and choose \"insert.\" To add a new row, click on the number of the row just BELOW where you want the new one. Make sure the whole row is highlighted, then right-mouse click and choose \"insert.\"

**Worksheets:** You can toggle between different worksheets in an Excel workbook using the tabs in the lower-left corner. They have default names of \"Sheet 1\" or \"Sheet 2\", etc. To change the name, double-chick on it and it will turn black\-- then you can start typing a new name. To add a new worksheet, you\'ll see a little button to the right of the tabs to add a worksheet. You can move worksheets around so they appear in a different order.

![Shortcuts](https://user-images.githubusercontent.com/4182043/32233453-6aeaef22-be28-11e7-878d-ce859faf9caf.gif)

That\'s it for this tutorial. Thanks for making it to the end! You can find more advanced Excel tutorials on [my main training page.](http://mjwebster.github.io/DataJ/)

DataJTraining is maintained by [mjwebster](https://github.com/mjwebster)\
This page was generated by [GitHub Pages](http://pages.github.com). Tactile theme by [Jason Long](https://twitter.com/jasonlong).


---

# StribDataAcademy2019

::::: inner
# Star Tribune Data Academy

This page contains materials for the Star Tribune Data Academy, including things that will be useful for you going forward. [Click here to see more of my training materials](http://mjwebster.github.io/DataJ/)

\

## To read ahead of time:

- [Interviewing data](http://mjwebster.github.io/DataJ/tipsheets/Interviewingdata.pdf)
- [Data literacy](https://mjwebster.github.io/DataJ/Other/DataLiteracy.pdf){target="_blank"}

# Data:

- [Data: U of M tuition over time](http://mjwebster.github.io/DataJ/spreadsheets/TuitionUMNTC.xlsx)
- New Yorker Cartoons [Click here for the exercise and explanations,](http://mjwebster.github.io/DataJ/spreadsheets/NewYorkerCartoonsExercise.docx){target="_blank"} and [click here to download the data.](http://mjwebster.github.io/DataJ/spreadsheets/new_yorker_cartoons.xlsx){target="_blank"}
- [Importing practice data (download, don\'t open)](http://mjwebster.github.io/DataJ/spreadsheets/importing_sample_data.csv)
- [Opioid deaths data (download, don\'t open)](http://mjwebster.github.io/DataJ/spreadsheets/opiate_deaths.csv)
- [Police incident data](http://opendata.minneapolismn.gov/datasets/police-incidents-2018){target="_blank"}
- Excel Magic [tipsheet](https://mjwebster.github.io/DataJ/tipsheets/ExcelMagic.pdf){target="_blank"} and
  data.
- [Student race data](https://mjwebster.github.io/DataJ/spreadsheets/student_race.csv){target="_blank"}
- [Exercise](http://mjwebster.github.io/DataJ/OpenRefine/OpenRefine_CleaningGovernorData.pdf){target="_blank"} and [Data for cleaning](http://mjwebster.github.io/DataJ/OpenRefine/Govenor.txt){target="_blank"} (right-mouse click to download)

## On-your-own challenge

- Option 1:[County population estimates data](http://mjwebster.github.io/DataJ/spreadsheets/popestimates_2018.xlsx){target="_blank"}and [exercise](http://mjwebster.github.io/DataJ/spreadsheets/population_estimates2018_exercise.docx){target="_blank"}
- Option 2: [St. Paul city salaries exercise](http://mjwebster.github.io/DataJ/spreadsheets/StPaulSalariesExercise_revised.docx){target="_blank"} and [data](http://mjwebster.github.io/DataJ/spreadsheets/stpaulsalaries_revised.txt){target="_blank"} and [record layout](http://mjwebster.github.io/DataJ/spreadsheets/stpaulsalaries_recordlayout.docx){target="_blank"}
- Option 3: [MMR vaccination data](http://mjwebster.github.io/DataJ/spreadsheets/mmr_vaccination.xlsx){target="_blank"} and [exercise](http://mjwebster.github.io/DataJ/spreadsheets/mmr_vaccination_exercise.docx){target="_blank"}

# Excel tipsheets

- [Excel cheat sheet](http://mjwebster.github.io/DataJ/tipsheets/Excel_cheat_sheet.docx)
- [Introduction to Excel tipsheet](http://mjwebster.github.io/DataJ/tipsheets/IntroductionToExcel.pdf){target="_blank"}
- [Pivot Tables tipsheet](http://mjwebster.github.io/DataJ/tipsheets/PivotTablesExcelv2.pdf){target="_blank"}
- [Pivot Tables cheat sheet (short version)](http://mjwebster.github.io/DataJ/tipsheets/PivotTablesCheatSheet.pdf){target="_blank"}
- [Beginner Excel tutorial](http://mjwebster.github.io/DataJ/BeginnerExcel.html)
- [Pivot Tables tutorial](http://mjwebster.github.io/DataJ/pivottables.html)
- [Importing to Excel](http://mjwebster.github.io/DataJ/tipsheets/ImportingToExcel2016.pdf)
- [Making charts in Excel](http://mjwebster.github.io/DataJ/spreadsheets/MakingChartsinExcel.pdf)
- [How to use VLOOKUP](https://mjwebster.github.io/DataJ/tipsheets/ExcelMagic.pdf){target="_blank"}

# Data visualizations

[CJ Sinner\'s presentation](https://docs.google.com/presentation/d/19NHYoVoky8guJfO1W1Cp10v-Do4yUmDMOrFf31MapFU/edit?usp=sharing)

# Other tipsheets

- [Basic steps for every data analysis](http://mjwebster.github.io/DataJ/tipsheets/BasicDataAnalysisSteps.pdf)
- [Data analysis road map](http://mjwebster.github.io/DataJ/tipsheets/DataAnalysiRoadMap.docx)
- [How to adjust for inflation](http://mjwebster.github.io/DataJ/tipsheets/InflationAdjust.pdf){target="_blank"} (from Sarah Cohen\'s \"Numbers in the Newsroom\")
- [How to avoid rookie mistakes](https://mjwebster.github.io/DataJ/Other/RookieMistakes.pdf){target="_blank"}
- [Tips for finding data](http://mjwebster.github.io/DataJ/Other/FindingData.pdf){target="_blank"}
- [Using Minnesota\'s public records law](http://mjwebster.github.io/DataJ/Other/UsingMNpublicRecordsLaw.pdf){target="_blank"}
- [Sample data request letter for MN](http://mjwebster.github.io/DataJ/Other/sample_data_request_letter.docx)
- [How to avoid data horror stories](http://mjwebster.github.io/DataJ/Other/HowToAvoidDataHorrorStories.pdf){target="_blank"}
- [Using data on a beat](http://mjwebster.github.io/DataJ/Other/UsingDataOnABeat.pdf){target="_blank"}
- [Tips for building your own dataset](http://mjwebster.github.io/DataJ/tipsheets/BuildingYourOwnData.pdf)
- [Involving your editor](http://mjwebster.github.io/DataJ/tipsheets/InvolvingYourEditor.pdf)
- [Using numbers correctly](http://mjwebster.github.io/DataJ/Other/Numeracy.pdf)
- [Wrestling with data (DDJ website)](https://datajournalism.com/read/longreads/wrestling-with-dirty-data){target="_blank"}
- Tipsheet: [Finding the Census data you want](https://docs.google.com/document/d/1SKzpqTUyD8vh2jdB0QmwOTrsQguRJiVXLQflk0dxC-0/edit?usp=sharing)

# Resources

- [Star Tribune data-driven work 2019](https://docs.google.com/document/d/1iVuNjEinC0_pMTq0TCWBTf0PwRmy_4gjRVwuLazpVxI/edit?usp=sharing)
- [Strib Dropoff FTP server](https://dropoff.startribune.com/)
- [Cometdocs](http://www.cometdocs.com/){target="_blank"} (for converting PDFs)
- Star Tribune Slack \-- Join the #data channel; most often the chatter on here is sharing and discussing interesting data-driven work from other news organizations. If you aren\'t on Slack, here are directions.
- Once you are on Slack, you might want to see if there are any channels in the [News Nerdery Slack](https://newsnerdery.slack.com/) ecosphere that you might want to join. For example, there\'s a \"helpme\" channel that is open to everyone; there is also a closed channel for women in data and digital journalism (Nerdettes); and many others that have specific missions.
- [NICAR Listserv](https://www.ire.org/resource-center/listservs/subscribe-nicar-l/). Run by Investigative Reporters and Editors, this old-school email listserv is still a key place that data journalists ask questions (and get answers) to solve problems they\'ve encountered. Some people also share links to data-driven stories they\'ve published. You don\'t need to be an IRE member to join the listserv, but you do in order to search the archives.
- [IRE\'s Extra! Extra! Blog](https://www.ire.org/blog/extra-extra/) This highlights data-driven and investigative stories published by news organizations around the world. Great source of inspiration.
- [All of MaryJo\'s training materials.](http://mjwebster.github.io/DataJ/)
- [Subscribe to Local Matters newsletter](https://visitor.r20.constantcontact.com/manage/optin?v=001jNS0O4Ui3OO7md-9Ryd0WOKdq14U-VfK9aIRH18MLku7VRyaaHESUptkwHw-8FO3X8Dhpw6_U4bO-hrpYrIzmYZy_m-F01qUfYYiFg0mDpo%3D)
- [Data journalism resources (gijn.org)](https://helpdesk.gijn.org/support/solutions/articles/14000036505-data-journalism)

# Other options beyond Excel

- SQL (structured query language) based programs such as Microsoft Access, mySQL, SQLLite. These allow you to work with much larger datasets and they are better equipped for joining datasets (like we did with VLOOKUP). Microsoft Access is on your computer but it has more limitations than other options. Materials for learning Access are on my [data training materials website.](http://mjwebster.github.io/DataJ/) If you want to try one of the other options, I can help you get the necessary software installed, etc.
- GIS (geographic information systems) software allows you to look for geographic patterns in your data. The free, open-source software [QGIS](https://qgis.org/en/site/) is used by several people in the newsroom and there are tutorials and directions online that make it relatively easy to learn.
- [The programming language called R](https://www.r-project.org/) is growing in popularity in data journalism and is the most widely used tool in academia and the larger data science community. Using the open-source interface called [RStudio](https://www.rstudio.com/) makes it seem more like a tool rather than a programming language. You can import/process/clean data, then do analysis and make charts and even publish web pages with your results. I\'ve been using it now for about a year and find it\'s increasingly becoming my \"go-to\" tool. I can point you to quite a few online tutorials written by fellow journalists, and a data journalist just published a textbook on learning R. And I\'d be glad to hold some beginner training sessions in the newsroom, as well.
- There are other programming languages out there as well. Another very popular one in the data journalism world is Python, which is useful for scraping websites, writing scripts to automate data cleaning and analysis. Several members of our data team have Python skills. Some data journalists use Python with an interface called [Jupyter Notebook](http://jupyter.org/), which allows you to see your code and your results in line with each other and to more easily share your results with others.

DataJTraining is maintained by [mjwebster](https://github.com/mjwebster)\
This page was generated by [GitHub Pages](http://pages.github.com). Tactile theme by [Jason Long](https://twitter.com/jasonlong).


---

# index

::::: inner
# Data Journalism

## MaryJo Webster\'s training materials

------------------------------------------------------------------------

This site has been replaced. [Click here to visit my new training materials site.](https://sites.google.com/view/mj-basic-data-academy/home)

DataJTraining is maintained by [mjwebster](https://github.com/mjwebster)\
This page was generated by [GitHub Pages](http://pages.github.com). Tactile theme by [Jason Long](https://twitter.com/jasonlong).


---

# pivottables

:::::::::::::: inner
# Data Journalism: Pivot Tables

## [By MaryJo Webster](https://twitter.com/MaryJoWebster)

------------------------------------------------------------------------

This tutorial uses a spreadsheet of [Minneapolis police reports.](http://mjwebster.github.io/DataJ/spreadsheets/Police_Incidents_2015.xlsx){target="_blank"}

Pivot Tables, which are available in Microsoft Excel and Google Sheets, are the most powerful tool (in my opinion) you have in a spreadsheet program. It allows you to take very detailed data \-- in this case, where one row represents a reported crime \-- and generate the summary findings that you need for your story. This usually answers your \"who, what, when, where\" questions (data is really bad at answering \"why\", so I\'m leaving that out.) and gives you the over-arching findings you\'re likely looking for.

For example, let\'s look at our sample data on reported crimes in Minneapolis. Some common questions we might have, include: Which neighborhood had the most reported crimes? What type of crime was most often reported? Which month had the most crimes?

![Top few rows of the police reports data](https://user-images.githubusercontent.com/4182043/33044284-f6b51be6-ce0d-11e7-89c0-8cc4bb0c4c43.gif)

Because each row of our data is a single crime, we can\'t just sort our spreadsheet to get the answers to our questions. All of those questions require \"grouping\" rows together based on specific values stored in the database. This kind of summarizing is one of the most common things you\'ll do in analyzing data. For example, to answer our first question about how many crimes in each neighborhood, we need our answer to show each neighborhood (listed just once) and the number of crimes reported there.

I find it helps to envision your answer before trying to create it. I\'d want it to look something like this:

![What I\'d want my answer to look like](https://user-images.githubusercontent.com/4182043/33043821-4e8c0890-ce0c-11e7-9c4b-c66fdfbfd6fe.PNG)

To get an answer like that, we\'ll use the Pivot Tables tool. This first video shows a very basic Pivot Table.

![Pivot Tables-Most crime reports by neighborhood](https://user-images.githubusercontent.com/4182043/33043823-4e9ffe40-ce0c-11e7-989b-123e38458812.gif)

Here are the steps shown in the video:

- Make sure your cursor is located somewhere inside your data (not out in the blank spaces). Also make sure all your columns are properly named. Without a name, the field won\'t be visible to the Pivot Table design tool.
- Go to the Insert menu and click on the Pivot Table button (on the far left)
- It will ask about the source of your data (it should guess correctly) and where you want to put the Pivot Table (default is a new worksheet). Just make sure these things are correct.
- The Pivot Table designer appears on a new sheet. On the right, you\'ll have a list of your fields and below that four boxes where we\'ll do the designing.
- The \"rows\" box is where you identify which column has the values you want to use as each row. In this case, I want one row for each neighborhood.
- The \"values\" box is where you do the counting or summing (or other math). In this case we are simply counting rows (each row is a police report) so it doesn\'t really matter what column you put in here.
- You can choose to count, sum, average or get minimum or maximum values (and other things) by clicking on the item you just put in the values box and choosing \"Value Field Settings.\"
- You can sort your results by putting your cursor on the first value of the column you want to sort and going to the Data menu and choose either A to Z or Z to A.

Helpful hint: As you\'re working in your Pivot Table, it\'s possible the field list and the four boxes on the right might disappear. Don\'t worry, you didn\'t do anything wrong! To get them back, simply click anywhere inside the Pivot Table results.

### Filtering your data

You can filter the data being used for the Pivot Table with the \"filters\" box on the designer. For example, let\'s say we want to find out how many burglaries were reported in each neighborhood. If you look at the original data, you\'ll see that the field called \"Offense\" has a code for burglary of a dwelling \-- \"BURGD\". So we\'ll put the \"offense\" column in the filters box. Then a pull-down menu will appear at the top of your results, giving you the option to pick which offense(s) you want to include in your answer.

![Pivot Tables-Filtering](https://user-images.githubusercontent.com/4182043/33043824-4ef1252c-ce0c-11e7-80b3-2e817cab290b.gif)

Note that you can filter on multiple fields. Just put any field(s) you want in the \"filters\" box and it will create multiple pull-down menus above your data.

### Making a cross-tab

A cross-tabulation is when you have two variables you want to measure against each other. One will be in the rows and the other in the columns. For example, we might want to know how many reports of each type of crime occurred each month (our data covers a 3-month period).

First, we need to make a little detour. Our data has a field indicating the date the crime was reported. But we need a column that only has the month. So we can add a new column to our data and use the MONTH() function to strip the month out of the date. (see the video)

Then we\'ll launch a new Pivot Table. This time the offense description will be in the rows; our new month field will go in the \"columns\" box ; and we\'ll put a count in the values box (like we did last time)

Note: After creating the new column, it might not show up in the list of fields for the Pivot Table. If not, go to the Analyze menu at top of screen and choose \"Refresh.\" (I\'ve shown this in the video, too). If you add a new column on the far right, you might need to choose \"Change data source\" and make sure it\'s grabbing the new column, as well.

![Pivot Tables-Making a cross-tab](https://user-images.githubusercontent.com/4182043/33043825-4f08fcf6-ce0c-11e7-8eb7-c47620340051.gif)

### Displaying percentages

So far, we\'ve just been counting the records and displaying raw numbers. But it is possible to display percentages. In the example we just did, we can tell Excel to display the \"row percentage\". In other words, it will show us what percentage of robberies, for example, occurred in each month. Or we could do a \"column percentage\" \-- which in this case would give us, for example, the percentage of all the crimes in June that were robberies. In the video, I\'m also going to filter the rows to just a couple categories so it\'s easier for you to see what it\'s doing on the row percentage. I\'ll have to turn that off to get accurate column percentages, though.

![Pivot Tables-Displaying percentages](https://user-images.githubusercontent.com/4182043/33043816-4d9dc1c6-ce0c-11e7-9909-156c06083acf.gif)

Let\'s switch to another dataset to show you some other features. For this part, we\'ll use a spreadsheet of [baseball salaries and payrolls](http://mjwebster.github.io/DataJ/spreadsheets/MLBpayrolls.xls){target="_blank"} that we also used in the [beginner excel tutorial.](http://mjwebster.github.io/DataJ/BeginnerExcel.html) We\'ll use the worksheet called \"Twins-Brewers\" that has the player salaries for the Twins and the Brewers from 2011.

We\'ll start by running a couple simple Pivot Tables \-- the total each team paid out, and the average paid out by position. (Note: the fact that we only have 2 teams in here makes this kind of useless. But imagine doing this with all the players, from all the teams.

![Pivot Tables-Baseball salaries by team and position](https://user-images.githubusercontent.com/4182043/33043817-4db2ea4c-ce0c-11e7-99f0-5bcab54e6204.gif)

### Adding a second value

We might want to know how many players this is counting up. Remember that each row of our data represents one player. So we can add a second math column (in the \"values\" box) and tell it to count. It doesn\'t matter which field you pick. To make it simple, I\'ll just pick \"player.\" Note that the order the items appear in the values box dictates which one comes first in your answer. You can drag and drop an item to flip spots.

The cross-tab feature can also come in handy here, if we put \"Team\" in the columns box we can see average salary each team pays, by position. However, since we still had the number of players in there, we end up with this crazy mess. So I took out the number of players. Now we have the average pay by position for each team (note that the overall average is in the \"grand total\" column now.

![Pivot Tables-Count players and average by team](https://user-images.githubusercontent.com/4182043/33043818-4dc34ab8-ce0c-11e7-95e2-9d79f4ab6cdf.gif)

### Adding multiple items in rows

What happens if you put two items in the \"rows\" box? I often find that this doesn\'t help me much. In this example, we\'ll move the team value out of the columns box and add it to rows. Note that it automatically falls in the second position \-- so the answer it gives displays the position first, then the teams. If you flip them around in the rows box, you get a different view.

![Pivot Tables-Multiple values in rows](https://user-images.githubusercontent.com/4182043/33043819-4e1f036c-ce0c-11e7-825c-576fe1d1daa8.gif)

### Running formulas

There may be times when you want to run some calculations on the results of your Pivot Table. I find that formulas get a little hinky when you try to set them up against the Pivot Table results. So I tend to copy and paste the results (except the headers!) to a new worksheet. Then add the headers and do the math there. Beware: If you copy the headers, it will just copy the whole Pivot Table \-- code and all.

### Other resources

- [Pivot Table video tutorials (Learnfree.org)](https://www.gcflearnfree.org/excel2013/pivottables/1/)
- [Guide to Pivot Tables (Chandoo)](https://chandoo.org/wp/excel-pivot-tables/)

DataJTraining is maintained by [mjwebster](https://github.com/mjwebster)\
This page was generated by [GitHub Pages](http://pages.github.com). Tactile theme by [Jason Long](https://twitter.com/jasonlong).


---

# IntroAnalysisWithR

```{r setup, include=FALSE}
#this is a standard piece of code that comes with an RMarkdown page when you create it.
#If you don't want your code to appear in the results, change echo to FALSE
knitr::opts_chunk$set(echo = TRUE)
```
#About
This is an RMarkdown page that is running an analysis of Minnesota death certificate data on people whose deaths involved opioids such as heroin, oxycodone, methadone, fentanyl, etc.
We are going to run through all the basic steps including loading packages, importing a .csv file of data, using the Tidyverse package called "dplyr" to run some analysis (similar to Pivot Tables in Excel) and then use a package called "ggplot2" to create a graphic of some of our findings. Finally we will "knit" this page in order to turn it into an HTML page where we can share our results with others.


If you haven't already, read this <a href="http://mjwebster.github.io/DataJ/R/ProsCons.html">Pros and Cons of R.</a>

#How to run this code on your own
You can download the RMarkdown page (called IntroAnalysisWithR.Rmd) used to build this webpage AND the data for this analysis (called "opiate_deaths.csv") from this <a href="https://github.com/mjwebster/DataJ/tree/gh-pages/R">github repo</a>
Save the RMarkdown file to a new directory on your computer. Create a sub-directory called "data" and put the opiate_deaths.csv file in that sub-directory. Open RStudio and go to the File menu and choose "New Project." It will ask you to pick a directory -- choose "Existing Directory" and navigate to the one where you stored in the RMarkdown page.
You'll name your project (whatever you want to name it) and it will create a file with a .RProj extension on it. That's the file you'll use to open your project in the future.
You should see that new file, plus your RMarkdown file and a "data" sub-folder in the Files tab on the right lower pane in RStudio. You can click on the data sub-folder to open that folder and confirm that your csv file is in there.
Open the RMarkdown page and you'll see all this text you were just reading.

#How to "run" a chunk of code
In an RMarkdown page you generally run each chunk of code separately. There are a number of ways to run a chunk. Put your cursor in the chunk you want to run. One option is to go to the "Run" button at the top of the page and choose one of the options from the pull-down list. There are also keyboard shortcuts for either launching a single line of code (In Windows: Control+Enter ) or an entire chunk (In Windows: Control+Shift+Enter). 

#Load packages
The first time you use R (and if you install an updated version) you will need to "install" packages. But every time you use R for any reason, you then need to "load" any of the installed packages that you want to use in your code.
Below I've provided some syntax that could be used in all your projects. It checks to see if the needed packages are installed and will install any that are missing.
Below that there are a series of library() commands to essentially turn on those packages for use in this particular RMarkdown page. You will need that every time you use R. However, the particular libraries/packages you need might differ from one project to another.

```{r, warning=FALSE, message=FALSE}

#This little piece of code checks to see if you have these packages installed on your computer and it will install them if you don't.
packages <- c("tidyverse", "janitor","ggthemes", "lubridate", "kntir", "htmltools", "rmarkdown", "kableExtra")
if (length(setdiff(packages, rownames(installed.packages()))) > 0) {
  install.packages(setdiff(packages, rownames(installed.packages())), repos = "http://cran.us.r-project.org")  
}

library(readr) #importing csv files; part of Tidyverse
library(dplyr) #general analysis; part of Tidyverse
library(ggplot2) #making charts ; part of Tidyverse

library(ggthemes) #this will help make our charts look better
library(janitor) #for data cleanup
library(lubridate) #for working with date fields

#we'll need these new packages for creating this markdown page to an HTMl page
library(rmarkdown)
library(knitr)
library(htmltools)
library(kableExtra)


```

#Import data
The data file we are going to use is stored in a sub-directory to our working directory. The sub-directory is called "data." Our data file is called "opiate_deaths.csv" and it is a comma-separated values text file.
We are going to use the readr package (which is part of Tidyverse) to import this file. Readr has a function called "read_csv" that is designed to import csv files.
This code below is the most basic we would need to import this data file. However, if we were to use this, readr would guess incorrectly and set our date fields to character. We also have a field showing the age of the person who died that we want to ensure comes in as a numeric field. If we don't do this, we will have trouble sorting by dates or calculating an average age, for example.
```{r, eval=FALSE}
deaths <- read_csv('./data/opiate_deaths.csv')
```
So we're going to one of the optional arguments that come with the read_csv function that allows us to set the column types. 
In the code below, it's setting the default to character ("c"), but then it's expressly telling R to set birthdate, deathdate and injury_date to a date format (col_date). Notice that col_date needs us to tell it how the date is displayed in our csv file. In this case, the dates show up as "5/5/2015". <a href="https://readr.tidyverse.org/reference/parse_datetime.html">This website</a> nicely explains the various options if your date fields are stored differently.

At the bottom of our code we are using a pipe operator (%>%) to have it also do one more thing as part of the import. It's going to run a function called clean_names() from the janitor package. This is a handy little tool that will convert all those uppercase field names to lowercase, ditch extra spaces in column names and things like that. R is case sensitive and doesn't like spaces or weird symbols in its column names, so this function comes in handy quite often. I tack it on to the end of my imports every time. Notice, however, that when i referred to my column names earlier in the code, I put them the way they are in the csv file because clean_names() hasn't done it's work yet.

```{r importdata, warning=FALSE, message=FALSE}

deaths <- read_csv('./data/opiate_deaths.csv',
                col_types=cols(.default="c",
                BIRTHDATE=col_date("%m/%d/%Y"),
                DEATHDATE=col_date("%m/%d/%Y"),
                INJURY_DATE=col_date("%m/%d/%Y"),
                AGEYEARS="i")) %>%
  clean_names()
```

#Analysis with dplyr
The dplyr package is very similar to Structured Query Language (SQL) and it is one way to create the equivalent of Pivot Table where you summarize your data. See my <a href="http://mjwebster.github.io/DataJ/R/RCheatSheet.html">R Cheat Sheet</a> for more on the basic syntax.
Let's start with simply selecting a few of the columns to display in our output.
Every query you run will start with the name of your dataframe (in this case we called it "deaths") and then use a pipe operator (%>%) to "link" operations. In this example below, our second operation is to simply display a few of the columns from our data. To do this we use the "select" syntax from dplyr.

```{r}
deaths %>%  select(firstname, lastname, deathdate)
```

##Select and filter
Now we'll add one more line of code, using the filter command to limit the number of rows that are returned in our output. In this case, we are asking for all the women who are identified as African American.
```{r}
deaths %>% 
   filter(gender=='F' , race=='African American') %>% 
   select(firstname, lastname, gender, deathdate)
```
##Other ways to filter
Who died in January 2015? This tells it to filter for deaths after or equal to 1/1/2015 and before 2/1/2015. Note the format of the dates (yyy-mm-dd) because that's how it's stored in the data frame.
```{r}
deaths %>%
  filter(deathdate>='2015-01-01', deathdate<'2015-02-01') %>% 
  select(lastname, firstname, gender, deathdate)
```

This tells it to show people who were Chinese or Japanese. Note the pipe character (|) is used to indicate "or". In the previous examples the comma was used to indicate "and".
```{r}
deaths %>%
  filter(race=='Chinese' | race=='Japanese') %>% 
  select(firstname, lastname, ageyears, race)
```
There are a lot of other things to learn about filtering data, but we'll save that for later.


#Indenting
You probably noticed that in the last couple batches of code, each piece is on its own line. I've indented them on purpose to make it easier to read. The key is that the pipe (%>%) needs to be at the end of a line (never at the beginning). Once you hit enter after the pipe, RStudio will automatically know you want to indent.
```{r, eval=FALSE}
deaths %>%
  filter(race=='Chinese' | race=='Japanese') %>% 
  select(firstname, lastname, ageyears, race)
```

#Summarizing our data
Up until now, we've been picking out pieces from our dataframe -- a few rows, a few columns. But usually we want to be able to summarize our data to find totals, percentages, averages and things like that.
The summarize (or "summarise" will also work) function in dplyr allows us to generate counts, sum up values in a column, calculate averages, etc.
The example below is simply counting the number of records in our data frame. Note the "n()" syntax -- this is how you tell R to count records, and that I'm creating a column that I'm calling "numrecords." The column will only appear in this temporary output. It will not be stored in a table.  I've added some extra spaces to make the code easier to read.
```{r}
deaths %>% summarize(numrecords = n() )
```

##Pivot Table
Most often, though, we want to summarize by "groups" within our data; this is what we usually use Pivot Tables for in Excel. For example, how many people of each gender died from opioid-related deaths?
Note that now I've added another piece -- group_by() -- and am telling it to form the groups based on the values in the "gender" column in our data.
```{r}
deaths %>%
  group_by(gender) %>% 
  summarise(numdeaths = n())
```
The query above was simply counting the number of records where the gender field listed "M" (male) and how many listed "F" (female). But we can use summarize to do all kinds of calculations.
For example, what was the average age by gender?
We'll use the mean() function to calculate an average on our "ageyears" column. Note I'm making a new column called "avg_age."
```{r}
deaths %>% 
  group_by(gender) %>% 
  summarize(avg_age = mean(ageyears))
```
We can also use summarize() to sum the values in a column. Unfortunately, this data only has one numeric field (ageyears) and it doesn't make sense to sum those values. 
But imagine you had a data frame listing each expenditure you made in your household last year and you want to get a total for each month. It would look something like this, assuming your data has a column indicating the month each expense occurred and a column called "amount_spent" identifying how much the item cost:
```{r, eval=FALSE}
myhousehold_expenses %>% 
  group_by(month) %>% 
  summarize(monthly_total = sum(amount_spent))
```

Let's return to our death data.


##Group by two variables
Sometimes we want to count or sum things based on 2 values. For example, we want to find out how many of the people who died were both women and African American.
```{r}
deaths %>% 
  group_by(gender, race) %>% 
  summarise(numdeaths = n())
```

#Sort our results
Let's add one more piece from dplyr -- arrange() -- so we can see our results in a prescribed order. For example, that last query we ran was very long. It might be nice to see the biggest group at the top. The default behavior for arrange() is ascending order, so in order to get the biggest on top (descending order), we need to add "desc" as part of the code.
```{r}
deaths %>% 
  group_by(gender, race) %>% 
  summarise(numdeaths = n()) %>% 
  arrange(desc(numdeaths))
```

#Filter summarized results
There are times you want to limit the results in your output in some way or another. You can do that by adding a filter command at the end of your query. In this example, we're telling it to only give us results for groups where there were more than 100 deaths.

```{r}
deaths %>% 
  group_by(gender, race) %>% 
  summarise(numdeaths = n()) %>% 
  arrange(desc(numdeaths)) %>% 
  filter(numdeaths>100)
```

#Mutate
This is one of my favorite features of dplyr. Mutate() allows you to add a new column, either to a temporary output or add it to a data frame. We'll start by adding a new column to our output. Remember the query about how many were men and how many were women? Wouldn't it be great to show percentages?
Notice that mutate() comes after summarize(). This is important because mutate is going to take the column we created in summarize() -- numdeaths -- and generate a percentage from it. Because we're grouping by gender, this is taking the numdeaths for the gender and dividing it by the total of the numdeaths column. And we're creating a new column called "pct".


```{r}

deaths %>% 
  group_by(gender) %>% 
  summarize(numdeaths = n()) %>% 
  mutate(pct = numdeaths/sum(numdeaths)) %>% 
  arrange(desc(pct))

```

#Put it all together
Let's put a bunch of things together in one query. We'll filter to only the women, then group them by race to find out how many women of each race died, what the average age was in each group and the percentage of the total women that each group accounts for.
We'll add a couple more things to fancy this up. First, you'll see that we're using the round function (from Base R)  to round our percentage to one decimal point. We're also multiplying it by 100 to make it a whole number. Note: the location of the parentheses on that calculation is really important and easy to get wrong.

```{r}
deaths %>% 
  filter(gender=='F') %>% 
  group_by(race) %>% 
  summarise(numdeaths = n(), avgage = round(mean(ageyears),1)) %>% 
  mutate(pct = round((numdeaths/sum(numdeaths)*100),1)) %>% 
  arrange(desc(pct))
```


#Add a new column
One of the questions we might have for this data is a simple one: How many people died each year? Our data, however, has the date of death, but not a separate field identifying the year. So let's create one. We'll use a package called lubridate that has a year() function, which will strip the year out of the date. Note: The date field needs to be stored as a true date field (not character). Remember how we fixed that on the import? This is why.

```{r}
#this is going to overwrite our existing data frame, pull everything from that existing data frame and then use mutate() -- from dplyr -- to add a new column called "deathyr"

deaths <-  deaths %>% mutate(deathyr = year(deathdate) )
```

Let's look at what that shows us:
```{r}
deaths %>%
  group_by(deathyr) %>%
  summarize(numdeaths = n())
  
```


#Cleaning dirty data
Let's start by looking at the hispanicethnicity field
```{r}
# let's look at this field to see where we've got a problem
deaths %>% group_by(hispanicethnicity) %>% summarise(count=n())
```
Notice the wide variety of ways that Hispanic and Non-Hispanic are listed? In order to get a good count, we need to make them consistent. This is called standardizing data.


##How to recode
We are going to create a new column -- called hispanic_new -- and use a function called case_when() to fix the problematic values.
```{r}
#case_when is from dplyr: https://dplyr.tidyverse.org/reference/case_when.html

deaths <-  deaths %>%
  mutate(hispanic_new = 
           case_when(hispanicethnicity=='Non-Hispanic' | 
hispanicethnicity=='NOT HISPANIC' | hispanicethnicity=='NOT-HISPANIC' | 
  hispanicethnicity=='non-hispanic' | hispanicethnicity=='NON-HISPANIC'~'NOT HISPANIC',
TRUE~toupper(hispanicethnicity)))

# the base R function called "toupper()" converts values to uppercase


#let's see our new column

deaths %>% 
  group_by(hispanic_new) %>% 
  summarise(numdeaths = n())

```


#Export data
If you want to export some or all of your data, you can use write.csv
It will spit out a file to your working directory
```{r}
#Let's spit out a subset of data -- in this case, the number of deaths by year

deaths_by_year <-  deaths %>%
  group_by(deathyr) %>%
  summarize(numdeaths = n())

#this will send a csv to your working directory
#if you don't include row.names it will add a column, numbering each row 1 through x.
write.csv(deaths_by_year, 'deaths_by_year.csv', row.names=FALSE)


#Another way to export a sub-set of your data is to include a filter in your write.csv code.
#In this example, I'm going to export all the columns from the main table, but only for the women who died
write.csv(deaths %>% filter(gender=='F'), 'women_deaths.csv', row.names=FALSE)


#You can send the file to a sub-directory like this (this assumes you have a sub-directory called "output")
#write.csv(deaths %>% filter(gender=='F', './output/women_deaths.csv', row.names=FALSE))


```

#Knit to HTML
<a href="https://rmarkdown.rstudio.com/articles_intro.html">About knitr</a>
Push the Knit button at the top of the page and it will automatically create an HTML file, as long as there are no errors in your code.
The code at the top of the page that says "echo=TRUE" means that the HTML page will include your code chunks and the results. Try running this page one time with echo=TRUE, open the HTML page (in your working directory) and see what it looks like. Then chase echo=FALSE and knit the page again and see how it has changed.
Also notice that the results of our queries don't look very pretty. It is possible to make prettier tables using <a href="https://cran.r-project.org/web/packages/kableExtra/vignettes/awesome_table_in_html.html">kable() and kableExtra()</a>, which come with the kntir package. 


---

# ExcelMagic

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
