## Data Journalism Heist

### How to get in, get the data, and get the story out - and make sure nobody gets hurt

 

#### Paul Bradshaw

 

This book is for sale at <http://leanpub.com/DataJournalismHeist>

This version was published on 2015-06-10


\*   \*   \*   \*   \*

This is a [Leanpub](http://leanpub.com) book. Leanpub empowers authors and publishers with the Lean Publishing process. [Lean Publishing](http://leanpub.com/manifesto) is the act of publishing an in-progress ebook using lightweight tools and many iterations to get reader feedback, pivot until you have the right book and build traction once you do.

\*   \*   \*   \*   \*


## Table of Contents

- [Huh?](#chap00.xhtml_leanpub-auto-huh)
- [The scouting mission: where's the data?](#chap01.xhtml_leanpub-auto-the-scouting-mission-wheres-the-data)
  - [Scouting a local government website](#chap01.xhtml_leanpub-auto-scouting-a-local-government-website)
- [Getting in](#chap02.xhtml_leanpub-auto-getting-in)
  - [The crowbar of data journalism: pivot tables](#chap02.xhtml_leanpub-auto-the-crowbar-of-data-journalism-pivot-tables)
  - [Who might your story be about?](#chap02.xhtml_leanpub-auto-who-might-your-story-be-about)
  - [*What* about that who might we want to find out?](#chap02.xhtml_leanpub-auto-what-about-that-who-might-we-want-to-find-out)
  - [Advanced filters - a dry run](#chap02.xhtml_leanpub-auto-advanced-filters---a-dry-run)
  - [Advanced filters - using wildcards](#chap02.xhtml_leanpub-auto-advanced-filters---using-wildcards)
- [Getting (the data) out](#chap03.xhtml_leanpub-auto-getting-the-data-out)
- [The Debrief](#chap04.xhtml_leanpub-auto-the-debrief)
  - [No one gets hurt](#chap04.xhtml_leanpub-auto-no-one-gets-hurt)
  - [Why does it matter - why do I care?](#chap04.xhtml_leanpub-auto-why-does-it-matter---why-do-i-care)


## Huh?

***Rusty**: You'd need at least a dozen guys doing a combination of cons.*

***Danny**: Like what, do you think?*

***Rusty**: Off the top of my head, I'd say you're looking at a Boeski, a Jim Brown, a Miss Daisy, two Jethros and a Leon Spinks, not to mention the biggest Ella Fitzgerald ever.*"

*Ocean's Eleven* (2001)

Can you learn data journalism in an hour?

That was the challenge I was set in late 2011, when I was invited to Bristol to deliver a short workshop. There was a certain appeal in the challenge: there is a myth that data journalism has to be complicated, spectacular, or resource-intensive. But data journalism is not always like that.

For every headline-grabbing [Wikileaks story](http://www.theguardian.com/world/iraq-war-logs) or [MPs' expenses saga](http://www.telegraph.co.uk/news/newstopics/mps-expenses/), there are dozens of everyday uses of data journalism that go unnoticed. It might be working out who's the top-scoring Englishman in the Premier League, or seeing whether there's been an outbreak of flu in your area. It might be finding out the worst performing schools, or that season's biggest fashion trends.

So I stripped back everything to some basic techniques. This book covers the bare bones of data journalism: the basic skills to do those simple stories - from finding data in the first place, to getting to the story you want quickly, to following it up and telling it well.

Can you learn data journalism in an hour? Not all of it. But you can learn enough to get started, and get your first stories. More importantly, you can learn enough to see what's possible, with results that provide a basis to begin to learn more (I'll talk about places to go next at the end).

So this is the 'Data Journalism Heist': nothing illegal, but rather a concept designed to reinforce the rough and ready, fast and clean aspect of this approach - as well as the importance of the last part: '*No one gets hurt*'.

It is a book all about speed, and we're wasting time. Time to get started.


## The scouting mission: where's the data?

Every good heist begins with a 'recce': a reconnaissance mission to check out the site of our operation. Data journalism has a number of key sites to 'recce':

- If your government, region or city has an open data portal, that should have regular updates. You can [find a list at CKAN](http://ckan.org/instances/): open data sites range from the UK's [data.gov.uk](http://data.gov.uk), to regional and city sites like [Waterloo](http://www.regionofwaterloo.ca/en/regionalgovernment/OpenDataHome.asp) in Canada, [Emilia-Romagna](http://datablog.ahref.eu/en/ahref-log/opendata/open-data-la-regione-emilia-romagna-presenta-il-suo-portale) in Italy, or [Chicago](https://data.cityofchicago.org/) in the US;
- If there's an office of national statistics, sign up for updates. [One list of national statistical bodies can be found on Wikipedia](http://en.wikipedia.org/wiki/List_of_national_and_international_statistical_services);
- FOI requests are often a good source of data. If you have a site in your country that allows people to send and monitor these (such as [Whatdotheyknow.com](http://whatdotheyknow.com) in the UK and [AskTheEU](http://www.asktheeu.org) for EU-related FOI requests) then these often provide an alert facility. Also look for specific bodies' disclosure logs - where they publish FOI requests received.

Take some time to check these out. It's a good idea to have data regularly come to you - either by email or, if you use an RSS reader to follow feeds from various sites, that.

  ------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you are reporting on - or particularly interested in - a specific field like crime, health, education, welfare or the environment, try to find bodies (local, national and international) that publish data regularly in that area.

Here are just a few general sources of regular data in the UK alone:

- Education: the Higher Education Statistics Agency (HESA), the Higher Education Funding Council (HEFCE) and Universities and Colleges Admission Service (UCAS) all hold data on universities and students. Ofsted, the regulator of schools, hold data on pupils and education at pre-16 level.
- The NHS Information Centre (NHSIC) and Health Episode Statistics (HES) hold data on hospital admissions and local doctors.
- NOMIS holds data on the labour market: where people are employed and unemployed.
- Data.police.uk holds data on crime and policing

### Scouting a local government website

This scouting mission concerns a typical type of data which you might find landing in your alerts regularly: local government spending.

In England every local council is required to publish data on its spending over £500. To find it, search for `expenditure 500` and the name of a local authority. In our case, we're going to look at Birmingham - the biggest local authority in Europe.

*What the data contains doesn't really matter here: the point is the exercises you'll be going through in looking at it. You can apply the same process to most regular public datasets, whether it's employment data, environmental information, or weather.*

Birmingham City Council's expenditure data is at [Birmingham.gov.uk/payment-data](http://www.birmingham.gov.uk/payment-data). You'll find monthly spending data going back over the last year, and can request older data by email.

It comes in two formats: PDFs, and spreadsheets. Given the choice, always avoid PDFs.

If you prefer to work on some international data, download [loans data from the European Investment Bank](http://www.eib.org/projects/loans/list/index.htm) - change the search to the widest possible criteria and then use the (easy to miss) *Export* link at the bottom of the page to get an Excel spreadsheet.

The spreadsheets are shown here as a Microsoft Excel icon, but they are actually **CSV** files which will work on any spreadsheet software, including free options like Google Drive spreadsheets and [Open Office](http://www.openoffice.org/) (which can also open Excel spreadsheets).

  ----------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ----------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Click on the most recent *spreadsheet* version of the spending data (not the PDF) and download it to your computer. Make sure you save it somewhere you can find later, like your desktop.

Once downloaded, open it in your preferred spreadsheet software - either by double-clicking it or [uploading to a web-based tool like Google Drive](https://support.google.com/drive/answer/2424368?hl=en&ref_topic=2375187).

Now, we're in.

  ------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ![information](images/leanpub_info-circle.png) | #### Other ways of getting information:                                                                                                                                                                                                                                                                              |
|                                                                             |                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                             | Building contacts is no less important in data journalism than other forms of journalism: these are the people who can alert you to the existence of data, or even leak it to you.                                                                                                                                                                                                 |
|                                                                             |                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                             | You can also request data using a 'right to information' law, such as the Freedom Of Information Act (FOI). Heather Brooke's book *Your Right To Know* is an essential reference book for that. Finally, you can 'scrape' data using software or programming. See my book *[Scraping for Journalists](http://leanpub.com/scrapingforjournalists)* if you want to learn about that. |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


## Getting in

*"Sometimes it takes an outsider, someone with fresh eyes to see the truth."*

― Ally Carter, *Heist Society*

Once we're in the data, we need to know where we're going. We don't want to spend a minute longer than we have to.

Every dataset will have stories it can tell. Here are just some typical stories often found in data, some taking more work than others:

1.  **Top of the pops/flops**: *who is top or bottom?*
2.  **'Holding up a mirror'** - or 'the face behind the figures': *what does the data tell us about ourselves as a country, industry or region?*
3.  **A freak occurrence/unusual change**: *what changed in the data from one time or place to another - and why?*
4.  **A claim debunked or supported**: *does the data support claims being made by a politician, 'expert' or pundit?*
5.  **Trend**: *what's going up or going down?*
6.  **Postcode lottery**: *are people in different places getting different treatment or access, or being charged differently?*
7.  **"Juking the stats"/"No accountability"**: *is the data reliable or complete? Or is someone trying to prevent people seeing it? Or is it not even collected in the first place? Why not?*
8.  **Victims, Winners and Losers**: *what's the impact of that data in real life? What are the human stories - including reaction to the data itself?*
9.  **Things happen together**: *does one thing go up when another thing goes up? Or does one thing go down when another goes up, or vice versa? Note that this does not mean* causation.
10. **"It's not working"**: *if someone made a change in the past about how things were done, has it had the impact that was promised?*

+------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ![question](images/leanpub_question-circle.png) | #### What stories could our spending data tell? And how quickly do we need to find out?                                                        |
|                                                                              |                                                                                                                                                                                                                                                             |
|                                                                              | Spend five minutes looking at the fields (column labels) in your dataset and five minutes going through that list and writing down potential data stories. The dataset alone may not answer your questions - but it may set you on the journey to doing so. |
+------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

You will often find yourself distracted by many different possible stories in the data - but if you're up against a deadline then you'll need to be focused.

We'll be focusing on one of the simplest stories to tell with data: who is top or bottom. Specifically: who gets the most money?

### The crowbar of data journalism: pivot tables

The quickest way to 'crack open' our data and get a good overview of it is by using a **pivot table**.

A pivot table can *aggregate* figures in our data so that, for example, we can combine all payments by company to see how much they got *in total*, rather than just how much *each payment* was (which is what it tells us at the moment). It could also aggregate all the payments by department, to see who is spending the most money in total.

Pivot tables can also *count* things - so we can find out *how many* payments were made to a company, and which one had the most; or how many companies there are, or which department made the most payments.

Before you begin creating a pivot table, *make sure you select just one of the cells containing data* - no more than one: don't select a column or a range of cells. Just click in *one*.

With that cell selected, find the pivot table option.

Look across the top of your screen in Excel: you should have menu options including **File**, **Edit**, **View**, and so on.

The pivot table option is usually found under the **Data** menu. But in some versions of Excel it can be found under **Insert**. Explore to see which one it is for you: you're looking for something like '*Insert pivot table*' or '*Pivot report*'.

If you can't find it, use the **Help** menu to search for 'pivot'.


Once you find the pivot table option, click on it. A new window should appear checking that Excel has understood correctly where your data is. This is why you needed to make sure you were *somewhere in your data* before you started this. Excel will automatically detect the edges of your data from that point - in other words, where it hits an empty row or column it will take that to be the limits of the cells containing data.


The window that appears when you create a pivot table - note the dotted line to the right of the window showing where it thinks the edge of your data is

Check it's understood correctly where your data is - a dotted line will have appeared around the edges of the data it thinks you want to play with - if it's wrong, start again making sure that you are starting with only one cell selected (*do not press any cursor keys while still in the new window* - trust me on this one). Then click *OK*.

What happens now depends on your version of Excel, but you should be able to see an *empty* pivot table with the following areas:

- One area saying '**Data**' or 'Data area' or '**Values**'
- One area saying '**Row**' or 'Row area' or 'Row labels'
- One area saying '**Column**' or 'Column area' or 'Column labels'

Look around to see if you can find these. If possible, click on the table area. Below are images showing three common views (if you have a different view, please get in touch and I'll update the book).


Whichever version of Excel you're using, what happens next is the same: you are going to fill some of those boxes with the subjects of your story by dragging them from the list of fields (column headings).

The first box to focus on is *Rows*. Rows normally concern the *who* of our story...

...So, who could we tell a story about?

### Who might your story be about?

If you have a dataset it's a good idea to look through the fields and think of possible stories to tell about the subjects.

Let's do that with our data:

- **Doc (invoice) numbers**? Probably not - although if these are supposed to be unique you could look for situations where they are not, and ask why.
- **Companies**? Yes: 'Company X received £Ym', or 'Companies of type B received £Am'
- **Vendor No.**? We have company names, which are essentially the same thing, so in most circumstances we're going to use those instead. However, if there is a situation where the company name is not given, this might give us another way to identify them - which we'll come onto...
- **Amounts**? Possibly: 'X payments over £1m' - but this is more likely to be the 'what' of our story.
- **Dates**? There might be instances where there is a story in dates: for example, did a council splurge recklessly just before the end of the financial year? Or did spending dry up when the money ran out because of poor financial management - and what might the impact of that be? We could tell a story of spending over time, but that would be about *amounts*, not dates. Again, in that story dates would be the 'what'
- **Directorate**? Yes. These are the parts of the council that made the payment, so 'Department of Y spent £X' is quite a likely story.
- **Cost centre code**? Not for now - but if we can figure out what it means then this will provide an even more accurate story of 'Cost centre Y spent £X'

So, we've narrowed our field to two strong candidates for the 'who' part of our story: companies, and directorates.

Let's drag **companies** into the *Row* box (if you have more than one, try just one and see what happens - sometimes there is more than one way to do the same thing, and you can always try the other method next time).

Your pivot table should now update to show a list of all the companies in the data.

This is quite useful in itself: our original data had one row for every payment. If we wanted to look through those manually we would have to glance through over 15,000 rows.

This list has much fewer rows - we could look through it for any interesting companies.

But we're on a deadline, so we need to move on.


### *What* about that who might we want to find out?

Let's choose a 'what' for our story about the companies. This should be pretty obvious: most of the examples we explored earlier focused on spending or receiving **money**. So that's our 'what': here represented by the **Amount** field.

The 'what' of the story needs to go into the **Values** field. So drag *amount* there.

The pivot table should update again: to the right of our list of companies should now be a figure: the payments made to that company.


How those payments are counted depends on how the data is interpreted.

In most cases, Excel or Google Drive will see that these are numbers and assume that you want to add them all together, with a function called SUM. If that has happened, your Values box should say 'SUM of Amount'.


Sometimes, however - generally when the data is not numeric - it will think you want to *count* how many there are, with a function called... (can you bear the suspense?) ...COUNT. If that has happened, your Values box should say 'COUNT of Amount'.


#### Changing the calculation

If your pivot table is counting and you want it to add up, or you want to make a different calculation, right-click on the area that says 'SUM of Amount' and select `Field settings...` (on a Mac you just need to click on the 'i' icon on that area).


The `PivotTable Field` window will appear. There are two areas to play with here:

- On the left, under *Summarize by:* are the options to aggregate values by their SUM, or COUNT, or AVERAGE, etc. You can also choose to just show the biggest value (i.e. the largest individual payment) for each row (MAX) or smallest (MIN). If you can't see SUM, make sure you scroll up.
- On the right the `Number...` button allows you to change how the number displays. If you're dealing with money, for example, you can choose 'currency' here, which will add a currency sign and thousand separators (i.e. the figure 1000000 will become £1,000,000 - much easier to understand).

Choose what you want to show and click **OK**. The pivot table should update.

#### What about the columns?

You may be tempted to add some columns to your pivot table. In most cases this will complicate the table to the point where any clarity is lost. Instead, it's generally better to create a new pivot table to look at the thing you wanted to add as a column - or use the report filter to switch between different elements (explained below).

The exception is if you add a column based on a field in your data with only a few options, for example 'Yes' or 'No', 'Male' or 'Female', or rating numbers like 1, 2, 3, 4 and 5.

#### Working with columns in a pivot table - and seeing percentages of rows

If you do have data like this which will work on columns, you can get your pivot table to display your results as percentages rather than simply whole numbers.

To do that, in the `PivotTable Field` window click on the button named **Options \>\>**

This will open a new area of the window titled *Show data as:*


The drop-down menu here allows you to specify whether you want to show your numbers differently to 'normal'. For example **% of row** will show your values not as a whole number (for example the number of payments or inspections, or the amount of money), but in terms of their percentage of that row (for example, the proportion of all inspections, or the percentage of payments to that company).

Similarly, **% of column** will show you what each cell's value represents as a proportion of the column in which it sits, and **% of total** will tell you exactly that.

There are other more complex options here too that allow you to display the value in terms of its percentage of, or difference from, another value, such as the previous year's number, or a specific or gender or category.


In this example the value is being shown as a percentage difference from the previous year

And '**Running total in**' will show the values mounting up across or down, depending on that base field you choose. Choosing your 'year' field, for example, will mean each year's value in the pivot table is actually that year's total plus all the preceding years'. Choosing your category field will mean the values increase as each category appears in each row, so that the last category in your pivot table rows will show the totals for *all* categories (a running total of that category and all preceding ones).

For video tutorials on some of these techniques [see this Contextures tutorial](http://www.contextures.com/xlPivot10.html#PctDiffFrom).

#### Bringing the cream to the top

At the moment the data will be sorted by the rows - companies listed in alphabetical order. We don't want that.

To sort it by amount, select any cell in that column, then click on **Data \> Sort...** and select *descending* (or you can just click on the Z-A button if you have one). In some cases you'll need to choose the column you want to sort, from a drop-down menu.

Straight away you can see who the top ten (and more) recipients of money are: some names may be self-explanatory, others will need a quick search (and a phonecall if you still don't understand what something is).

Depending what month you are looking at, you might now start to follow up one of these leads to tell some of the following stories:

- Millions being paid every month on equal pay settlements
- Profile: the region's biggest construction projects
- Outsourcing of public services leaves millions of pounds of spending closed to public scrutiny
- Council urged to cut its energy bills

Spotting these stories is easier if you spend time reading the local news, but it's also a good starting point to begin familiarising yourself with the local news: searching for company names may bring up previous reports involving them. It will also give you ideas for new angles or angles that can be re-visited.

There are also many other possible leads if you continue to scan down the list of companies, however. Don't overlook the smaller amounts - these sometimes include quirky recipients (my personal favourite was a chicken hire company) or ones that raise questions (what's the story behind a gift bought from a 'business gifts' company?) which might make for more colourful items.

Here is a list of some of the questions you might write down as you scan down the list of companies:

- How much is spent on care homes? Who benefits most? What about companies with a bad history? You could also ask the same question of children's homes.
- How much is spent through agencies on temporary staff? Why are temporary staff being hired at the same time as redundancies are being made?
- There are a lot of charities. How big a role does the voluntary sector have in providing public services? Are they at risk from cuts?
- There are large payments to sporting bodies such as the British Cycling Federation and the Lawn Tennis Association - what is that for? (A similar lead was followed up for [this front page story by the Manchester Evening News](http://www.manchestereveningnews.co.uk/news/greater-manchester-news/you-splash-out-300k-australian-4033385) - shown in the image below.
- There are payments to other councils - what is that for?
- How much is spent on transport? Who is that for?
- There are some B&B (bed and breakfast) hotels in the list costing tens of thousands of pounds - what for? (That spending was the source of [this front page story in the Birmingham Post](http://www.birminghammail.co.uk/news/local-news/city-council-spends-nearly-1m-1330817) - see second image below)
- Why are they spending thousands on Starbucks?
- Why are they spending over £1000 on Jaguar hire?

And:

- Redacted personal data - what's that all about?


You'll notice that many of these stories don't require any further work on the data - so at this point it's time to **make a clean exit, and start speaking to people**. If that's you, skip to the last chapter now.

For some, however, you're talking about more than one company - and for that you're going to need a second technique.

+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ![information](images/leanpub_info-circle.png) | #### Calculations for context                                                                                                                                                                                                                              |
|                                                                             |                                                                                                                                                                                                                                                                                                                 |
|                                                                             | You may need a grand total, or the value of the average payment, to put your story into context. To calculate those find an *empty* column and type one of the following formulae in any cell, replacing `D:D` with the letter for the column containing the values you want to add up or find the average for: |
|                                                                             |                                                                                                                                                                                                                                                                                                                 |
|                                                                             | - `=SUM(D:D)`                                                                                                                                                                                                                                                                                                   |
|                                                                             | - `=AVERAGE(D:D)`                                                                                                                                                                                                                                                                                               |
|                                                                             |                                                                                                                                                                                                                                                                                                                 |
|                                                                             | (For example, if you wanted the total of all the values in column A, change the formula to `=SUM(A:A)`. And if you wanted the average payment from column C, change the formula to `=SUM(C:C)`).                                                                                                                |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ![tip](images/leanpub_key.png) | #### Stay focused: the mantra of data journalism                                                                                                                                                                   |
|                                                             |                                                                                                                                                                                                                                                                                           |
|                                                             | Data has so many potential stories that it can be easy to get distracted following multiple avenues of enquiry. Adding columns to our pivot table will just make it more confusing to interpret. We need to be quick - so keep things simple wherever you can. This is a heist, remember! |
+-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

### Advanced filters - a dry run

If you want to get an overview of several companies - say, all those providing temporary staff, or transport, or care homes - then you'll need to lump them together somehow.

A good way of doing this is to use **advanced filters** to find payments that have something in common - for example, companies with the word 'taxi' in the name.

Advanced filters are one of two types of filters used in Excel. The other is the **automatic filter**. This is an easier filter to apply: simply select **Data \> Filter** and the top of each column in your data will turn into a drop-down menu.


That drop-down menu can then be used to filter the data below: for example, you could click on the drop-down menu for 'Vendor name', untick 'Select All' and then scroll down, ticking the companies you only want to show.

For a quicker way of doing the same, instead of scrolling down you can use the search box in the drop-down menu to find companies that contain the term you're looking for - and then tick them from here (some versions of Excel will automatically select them for you).


This easy way of filtering is very appealing - but you are likely to need a lot more control over your filter than this, as we'll see. And that's where the advanced filter option comes in.

#### Create an advanced filter

To create an advanced filter you first need to create a separate 'mini table' showing what your filter categories and terms are. This table must:

- Have at least one empty column between it and your main data
- Use exactly the same column heading(s) as those in the main data that you want to filter on.

Here's an example of the most basic mini table for an advanced filter, with just one criteria:


Note the following:

- The original data is in columns A-H, so the next column - I - has been **left empty**. This is so that Excel does not confuse the new table (in column J) with the other data.
- The new table uses exactly the same heading as the column we want to filter on: 'Vendor Name'. It is best to **copy and paste this heading from the original data** to get it exactly right - for example 'Vendor name' would not work because it has a small 'n'. Double spaces and spaces before and after column headings can cause similar problems.
- Under that column heading we have one entry: 'ELMDON CARS (TAXIS) LTD' - again, this has been copied and pasted from the original data because advanced filters will only bring back **exact matches** - unless we use special characters, which we'll come on to.

For a dry run, **create a similar mini table in your own spreadsheet** - remembering to leave an empty column, and copy and paste the column heading and the name of one entry in that column.

Once you've created that, you're ready to use the advanced filter. But before you do that...

**Make sure your cursor is somewhere in the original data first**. This is because, like pivot tables, Excel is going to use this to guess which data you want to filter - and of course you want to filter the original data, not the new mini table. Once your cursor is back in that main data you can select **Advanced filter**.

The advanced filter, like the automatic filter, is normally under the **Data** menu.


Once you click on 'Advanced filter...' you should see a new window appear with some options. The main ones you want to look for are the **List range** box, which should show the range of cells you want to filter: something like `$A$1:$H$16283`.

Ignore the dollar signs (these fix each part of the cell location references so they cannot be changed), what that means is it is selecting data from cell A1 (column A, row 1) to cell H16283 (column H, row 16283). If your spreadsheet has more rows or columns the second cell reference will be different - but the principle is the same.

Clicking in this box should also make a faint dotted line appear in the background spreadsheet, around your original data (like it does in the pivot table wizard) so you can visibly see the edges of the data Excel has assumed you want to filter.


The box underneath this - titled **Criteria range:** - is where you tell Excel about your little mini table, where you listed the column name and criteria you want to filter on.

Click in that box, and then click and drag across the two cells in your mini table to select them (you may have to move the Advanced Filter window first, which you can do by clicking at the top of it and dragging it aside).

As you do this, the cell references should appear in the box. This time it may look a bit more complicated: something like `'300627Payments_over_£500_Octobe'!$J$1:$J$2` - this is because this time the cell reference includes the sheet name too, followed by an exclamation mark before the cells themselves: J1 to J2.

Don't worry about checking this (avoid using the arrow keys to try to see the end of that reference - it will move the cursor on the sheet instead) - the main thing is that a **dashed line should have appeared around your mini table** to indicate that it has been selected.

You can also forget about the other options on this window. Instead, click **OK** and you should see the results of your advanced filter appear.

With my example, I have four rows of results (you may have more). Note the row numbers, however - they are not sequential:


This is because the filter only *hides* non-matching data. Likewise, our mini table has disappeared too - apart from the heading. The rows under that heading have been hidden. That's important, as we'll find out.

Now, we could have done all this much more quickly with an automatic filter. But this was just a dry run - now we'll really use the power of advanced filters.

### Advanced filters - using wildcards

I said previously that you needed your criteria to be an **exact match** with the company names in the data - unless we use special characters. Those special characters are called **wildcards**, because they act like jokers in a pack of cards: they can stand for any other character.

The two wildcard characters in Excel are:

- an asterisk: `*` which stands for 'none or any characters'
- and a question mark: `?` which stands for 'any *single* character'

The difference is subtle but important, as we'll see.

Wildcards allow us to be much more open in our criteria. For example, instead of having to know the exact company name, we could use the following:

`*TAXI*`

This will bring back any rows where the `Vendor Name` field contains *none or any characters* followed by the letters T, A, X, I, followed by *none or any characters*.


In other words that will match any companies with names containing the characters T, A, X, I, in that order.

Treating the characters separately is important here: 'Bob's Taxidermist' would be caught by the same criteria, for example (we'll deal with excluding those results later).

Now, again, we could have something similar with an automatic filter - but an advanced filter allows you to do this with *multiple criteria*. So, underneath `*TAXI*` we could also add:

`*COACH*`

`*TRANSPORT*`

`*CAR*`

`*HIRE*`

`*BUS*`

...and any other key terms you can expect to appear in the name of taxi firms.


Try that now with your own advanced filter. You'll need to clear your old filter first - which you can do by selecting the **Data** menu and clicking on **Clear filters** or similar. Then change the criteria in your mini table - making sure to leave the heading as it was.

When you go through the process of creating a new advanced filter (**Data \> Advanced filter**), remember to put your cursor back in the main data first, and specify the criteria range again, as it is now a longer range of cells than it was previously (in the example above, seven cells rather than two).


Now you should get hundreds of results - including many irrelevant ones. Why? Because our `*CAR*` criteria is matching against words like 'CARE' (so all the care home companies are included), and `*HIRE*` is matching against words like 'YORKSHIRE'.

To reduce the likelihood of this happening we need to add just one character to our criteria: **a space**.

It's easy to overlook spaces in company names and other data, but computers see these as a character like any other, and in fact they are hugely useful in filtering. Look at the difference between these:

- `*CAR*`
- `*CAR *`

The first option will match 'CAR HIRE' *and* 'CARE HOME'.

The second will not match 'CARE HOME', because it is looking for a space after the R.

However, for the same reason it will also not match 'HIRE CARS'. To address that you might add another criteria: `*CARS*`

Apply the same principle to `*HIRE*` - this time putting the space *before* it like so:

`* HIRE*`

This is for two reasons:

- 'YORKSHIRE' and other county names could have a space after them anyway.
- Actual hire company names would be likely to have the characters 'HIRE' at the end, *without* any space after those characters, but a space before them: for example 'CAR HIRE'

Try to look for similar patterns in your data when filtering it. For example: how would you exclude all the results that match 'BUS' with company names using the word 'BUSINESS'?

Now, clear your filter, make those changes to your mini table of criteria, and apply a new advanced filter.


At this stage you will still have some mismatches - but as long as they don't dominate the results as they did previously, we can filter them out more quickly using pivot tables, as I'll explain in the next section.


## Getting (the data) out

***Danny**: There's a ninety-five pound Chinese man with a hundred sixty million dollars behind this door.*

***Linus**: Let's get him out.*

*Ocean's Eleven* (2001)

Once you've tweaked your advanced filter to the point where you have some decent results, you can use the same pivot table techniques to get an overview on *that* - but not yet.

For the moment this filtered data is just a *view* of the data - rows that don't match our criteria are still there, but hidden, so any pivot table we generate will also include those hidden rows.

To address this, we need to copy the filtered data into a new sheet:

- While the data is still filtered, select CTRL+A to select all (CMD+A on a Mac).
- Press CTRL+C (CMD+C on a Mac) to copy the selection - or select the menu **Edit\>Copy** if you prefer.
- You'll notice that the copied data has dashed lines across it - this is because you are only copying the filtered data, *not* the hidden data.


- Create a new sheet to paste this data into, by selecting the **Insert** menu and then **Sheet \> Blank sheet** (you can also right-click at the tabs across the bottom and select **Insert sheet**, or press SHIFT+F11)
- Paste the copied data into this sheet by pressing CTRL+V (CMD+V on a Mac) or **Edit\>Paste**
- Scroll to the bottom of the sheet to check it has only pasted the filtered data: there should be a couple hundred rows rather than over 15,000.

You can now use this data to generate a pivot table, as you did before with the whole data. So do that, putting *Vendor Name* in the rows, and *Invoice amount* in the data area to give you a total for each company.

This will also give you a list of companies which is easier to whittle down further: at the top of the column containing the company names should be a coloured cell saying **Row labels**. On the right of that is a downward arrow that opens up a drop-down menu showing all the company names. Click on this and you can untick any companies you *don't* want to appear on this pivot table.


Above we can see that ALLSPORTS SCHOOLS COACHING LTD is not a transport company, so we can untick that. Likewise CENTRAL COACHING AND SPORTS ACADEMY, DOABA TENT HIRE SERVICE, JOHN GALLAGHER SPORT COACHING and so on (These are just examples in my data - look for similar examples in your own.)

Some might not be immediately obvious: is FREIGHT TRANSPORT ASSOCIATION a transport company? A quick search on Google will tell you it's a trade body, so that can be excluded as well. What about FINESSE COACHES LTD? That could be a coach in either sense of the word, but it turns out to be the vehicle kind. And in fact, while Googling, you may find a public inquiry judgement relating to a company of the same name in the Midlands by the Traffic Commissioner, dated a year previously. *That's* something to follow up - perhaps with other companies here too (but don't get thrown off track: finish the story you're working on before beginning another).

Once you've filtered out the companies you don't want in this table, you have a dataset you can re-pivot for a number of possible stories:

- Who's getting the most money?
- Who's spending the most on transport?
- What sort of companies are being used?

Sorting column B from largest to smallest again would bring our biggest recipient to the top (in my data that's one taxi company getting £67,000 in this one month alone).

What if we wanted to look at spenders? Well, we still need to retain the filter on company names: to do that, drag the 'Vendor Name' from the Rows box into the **Filter** box. That will just give us a grand total - but we can also drag something new into Rows: **Directorate**. Your four boxes should now look something like this (depending what version of Excel you're using):


This helps us understand who's spending the money, and perhaps what on.

The overwhelming majority of payments, for example, are being made by the directorate 'CYPF' - another quick search, phonecall or local knowledge would tell you this stood for 'Children, Young People and Families'. This [covers](http://www.birmingham.gov.uk/cs/Satellite?c=Page&childpagename=Legal-Services%2FPageLayout&cid=1223092568895&pagename=BCC%2FCommon%2FWrapper%2FWrapper) "all business areas relating to education and social care for children and young people".

So these may include taxis and coaches for transporting pupils to and from school (individually and in groups), and on school and other trips, among other things.

From this point you could drill down further to just look at spending by a particular directorate - it all depends on what you're interested in, or what's more newsworthy at the moment. For example:

- If the council is making lots of redundancies, spending money on temporary staff may be worth focusing on.
- If someone in the council is making statements about wasting public money, is their department practising what she preaches?
- If there are big cuts, where is money being spent unnecessarily? Or where are cuts *not* being made?
- If there are cuts elsewhere - for example in welfare payments - how might that be having an impact at a local level? For example: an increase in homelessness shown by increased spending on bed and breakfast accommodation.
- If a particular issue is making the headlines, such as teenage obesity or roads in need of repair, how much money is being spent on that issue, or how has that changed?

You can add many more - the more you read the news, the more questions will spring to mind (you'll also spot the names of people to ask about them).

For example, in our data, if you were only interested in spending by one department (say, Adults and Communities), you could click on the drop-down menu next to **Row labels** and tick just that one. Then:

- drag *Directorate* to the **Report filter** box, and
- drag *Vendor Name* back into the **Rows** box

...so you'd have something like this:


**Have a play around with different combinations of filters and rows**. And as always, be ready to leave the data and pick up the phone at the earliest opportunity: this spreadsheet isn't going to give you the story alone.

#### Finding related data - search techniques of the professionals

Where phonecalls don't work there are some other techniques you can use to try to find additional information and data on your story. **Cost codes**, for example, can be very useful - *if* you know what they refer to. In the example above each item of spending has a 'Cost Cente' \[sic\] code which refers to a more specific part of the authority than the directorate.

If you were interested in spending which seemed to have the cost code RBL23, you could look online to see if that cost code is mentioned in any documents. The following would help narrow the search in different ways:

- Searching for `RBL23 filetype:xls` on Google will only show you spreadsheets containing the code
- Searching for `RBL23 filetype:pdf` on Google will only show you PDFs containing the code
- Searching for `RBL23 site:birmingham.gov.uk` on Google will only show you pages and documents on the Birmingham council website

You can adapt the same techniques to other documents types (`filetype:doc` for Word docs, for example) and sites (`site:gov.uk` for all local and central government sites, for example). The terms `site:` and `filetype:` are called **search operators** - these can save you a lot of time looking for information generally.

Sometimes you will find a spreadsheet or document which lists all the codes in your data, and adds extra data (for example where schools or authorities are represented by a code, you might find resources like [this](http://www.dwp.gov.uk/docs/faqs-la-code-list.xls) listing who they are, their addresses, and so on.

Sometimes you will find other documents, such as guidance, or details on individual payments, or templates for submitting information. All of these can be useful if you have to resort to a Freedom of Information request, because they tell you what information is gathered (or should be!).

If you can't find more detail, try picking up the phone again to the part of the authority that publishes the data - there may be contact details on the page where it is published, or you may have to call the switchboard and ask if they can put you through to whoever is responsible.

If that person can't help then try the officer responsible for Freedom of Information requests - again, it may be that they can help you without you having to submit a formal request.

Even if both people cannot help, don't see it as a failure: you've made two useful contacts!

The final option, then, is the Freedom of Information (FOI) request. This can be made directly to the authority (search for "freedom of information email" or similar, with the name of the body - most have a webpage which provides details), or through a free service like [WhatDoTheyKnow](http://whatdotheyknow.com/) or [AsktheEU](http://www.asktheeu.org/). In the US you can get help from sites like the Reporters Committee for Freedom of the Press's [FOIA Letter Generator](http://www.rcfp.org/foia).

*The advantage of services like WhatDoTheyKnow is they make it much easier to make and track FOI requests, and easier for others with a similar interest to find and even help you. The disadvantage is that your request is public, so if you want to retain some sort of 'exclusivity' to the information, you won't. If you lack confidence in making FOI requests, sites like WhatDoTheyKnow are probably a good way to start.*

When making an FOI request relating to data, check the following:

- Are you requesting the data in **digital spreadsheet format** (CSV or XLS)? If you don't specify this, the data may come back as a PDF, or even printed on paper, which isn't helpful.
- Ask if **different parts of the codes have particular meanings**. For example, the first two characters might refer to a department, and the next three to something else.
- Try requesting the '**data dictionary**' for the data you've been working on. This is a list of all the fields in the database - not just those that they published. You should explain that, too, as they might claim they don't know what that is, or that they don't have one. Alternatively, you might request the full data, including any fields that have not been published - bearing in mind the next point...
- **Anticipate any objections** that may be made. Typical exemptions under FOI laws include cost, privacy, and commercial confidentiality. If you can familiarise yourself with those exemptions, and judgements relating to them, then quote them in your request. For example, you might point out their own obligations under those exemptions (e.g. having to explain the reasoning, or help you rephrase the request). You can also shape your request to explicitly exclude information which may be subject to exemptions, such as personal data.
- Remember that you can request **documents** as well as data: are there documents which might shed more light on your story, such as individual payment receipts (payment reference numbers of some kind are helpful to quote here) or claim forms. Policy or guidance documents might be useful too: for example, on spending, commissioning or claiming money.

As requests like these often take weeks or even months, it's worth making these requests even before you plan to chase any stories, so you have basic contextual data available when the next datasets come out.


## The Debrief

*"Rusty: You look down, they know you're lying and up, they know you don't know the truth. Don't use seven words when four will do. Don't shift your weight, look always at your mark but don't stare, be specific but not memorable, be funny but don't make him laugh. He's got to like you then forget you the moment you've left his side. And for God's sake, whatever you do, don't, under any circumstances...*

*"Livingston: Rus?*

*"Rusty: Yeah?*

*"Livingston: Come look at this?"*

*"Rusty: Sure."*

*Ocean's Eleven* (2001)

Once again: once you have your story lead, there's no need to waste more time in the data. And turning that lead into a story means adding context, colour, and people.

Let's take some of the 'top of the pops' stories we identified earlier:

- Millions being paid every month on equal pay settlements
- Profile: the region's biggest construction projects
- Outsourcing of public services leaves millions of pounds of spending closed to public scrutiny
- Council urged to cut its energy bills

How might you flesh that data out? In the case of *Millions being paid every month on equal pay settlements* you might want to use the same techniques on other data to add some historical data, add up how much has been paid in total, and which was the biggest month.

But equally, you will need to get some reaction and explanation of this: you'll need to ask the body spending the money, and the body receiving it, some questions. As always the 'five Ws and a H' are useful starting points:

- Why are you spending this money? (If you don't already know from previous reports)
- How much has been spent, and how much is yet to be spent? (Even if you think you know, it's always good to see what answer you get, or check your figures)
- When does it end? When did it begin?
- What is the impact of this? (Where is the money being taken from)
- Who does this affect?
- Where does this affect? (There may be some areas suffering more than others as a result)

The same applies to the profile piece on construction projects. This data gives you a list of the names getting the most money - but you'll need to speak to them to find out what it's going on, and speak to the council to find out why they're spending money on those projects.

The other two stories rely on *reactions*: in *Outsourcing of public services leaves millions of pounds of spending closed to public scrutiny* you need to ask a relevant body or individual why that's important and how they feel about that. An organisation that campaigns for transparency in public office or spending, or even a political party that relies on that transparency to hold power to account, would likely have an opinion on this.

The hypothetical *Council urged to cut its energy bills* is a headline subject to change: once you speak to some people (an expert on energy efficiency; the council) or perhaps look at other councils' energy bills or historical bills, you might decide to go with *Council cuts energy bills by 50%* or *Council praised for energy policy*. But you won't know what your story is until you seek some reaction on the information you've obtained.

#### Visualising the data

If you want to create a chart or map to illustrate your data there are dozens of online tools you can use. For charts [Datawrapper](http://datawrapper.de/) is one of the quickest and simplest to use - with the added bonus that it can create print-friendly PDFs too. But you might also want to try out Google Charts (in the **Insert** menu in a Google spreadsheet) or [Many Eyes](http://www-958.ibm.com/software/analytics/manyeyes/). [Tableau Public](http://www.tableausoftware.com/public/) is incredibly powerful for a free download (currently PC only) but that also means more time finding out how to make it work.

Different types of charts are better for different types of stories. Before you visualise any data, ask yourself whether you are telling a story about comparison (e.g. one thing is smaller or bigger than another), composition (e.g. half of spending goes on one thing), distribution (e.g. activity across the day), or relationships (e.g. the larger the population, the higher crime). Journalism stories are normally about composition or comparison.

Once you know that, here are typical chart types to try:

- Comparison between items: bar or column chart
- Comparison over time: line chart
- Composition during one period: pie chart or tree map
- Composition over time: stacked area chart
- Distribution: histogram or scattergram
- Relationships: scattergram or bubble chart

The key to clear data visualisation is to strip the data down to the bare essentials. This is no different to what a journalist does with any text story: cutting out waffle and irrelevant detail until the core of the story remains. In data visualisation, try to avoid having more than four or five data points: slices of a pie, bars or lines in a chart. Any more and it becomes hard to see what you are telling a story about.

To do this, pick the top four or five, or divide into fewer, broader, categories, or drill down to just the top four or five within *one* category. Try showing one item compared to 'everything else' or the 'average'.

For the same reason, avoid using too many colours: there's no need to have a separate colour for every bar, for example. Instead use one colour for your focal point, and another for everything else: in a bar chart for example, the key bar might be red, and *all the others* dark grey. In a pie chart or line graph all the non-focal slices might be different shades of grey, and so on.

If you want to map your data the same principles apply: pick as few colours as possible if you can. In terms of websites to try out, [BatchGeo](http://batchgeo.com/) is a good introductory tool - simply paste your data into the empty box on the homepage (although the free version has a limit to the number of rows you can map). [OpenHeatMap](http://www.openheatmap.com/) is a good option if you want to map areas like constituencies or regions - make sure to [read the documentation](https://github.com/petewarden/openheatmap/wiki) to find out how to ensure your data works with it. [Google Fusion Tables](http://www.google.com/drive/apps.html#fusiontables) gives you much more control than either, but has a steeper learning curve - look for guides and videos online.

### No one gets hurt

Remember to treat data as a *source like any other*. It is there to be questioned, followed-up and cross-referenced. Data is, after all, compiled by humans and published by humans. It is humans who decide when to gather it and how to classify it. All of these decisions influence what the final data looks like.

For example, you may find an enormous payment to an individual whose name has been redacted - but when you ask for more details you find it was actually to a school whose name sounds like a person: someone redacted it without realising.

You may look at recycling rates and see that the local authority is the worst in the country - but a phonecall to the authority suggests they're actually 'just' the worst in the region.

In each case you mustn't take those replies at face value: it's just another source. Nor should you report it as 'he said, she said'. Look for evidence, revisit your data, speak to an independent expert, or whatever will help you be confident which party is correct, and no one is getting hurt unjustifiably.

### Why does it matter - why do I care?

A good story answers two questions in its first few pars: why does this story matter, and why do I care? The *impact* mentioned above is the key piece of information here: for example, expensive energy bills matter because they take money away from other services that a body delivers. Construction investment matters because it creates jobs, or disrupts neighbours' lives, or damages the environment, or protects it (which one matters most depends on who your readers are!). A powerful person's reaction to something matters because they might use their power to change things.

But just reporting on that can leave the story a little dry. To engage people with things that matter, we need to explain why they should care - and often that's about engaging the *human* side of things.

Your story lead may have come from data, but the story itself doesn't have to have numbers - and it should certainly have people. However much money is being spent on construction, or energy, what makes us care about it is reading about the woman who has been unemployed for a year and has just found a job - or the couple who had to sell their house after living there for 50 years because they just cannot take the noise any more. Or the swimmers who cannot use their swimming pool because the council is spending too much on energy bills.

And that is where I stop talking, and you start digging. Never forget that any data you work with is a means to an end, not the end itself. Pivot tables and filters are tools to help get you somewhere quicker - they will give you the hard facts (if the data is sound) to start your enquiries from. They will make it harder for people to avoid answering your questions, or to smear your reporting. But in the end, you'll need to *tell* your story about people first, and numbers second.

Now get out there and start planning your own heist!

### Where next?

At some point you will probably need to expand your skillset into other areas of data journalism. Here is a list of those areas, and some useful resources for each:

#### Getting data

We've covered some sources of data releases in this book, and touched on Freedom of Information. FOI laws will differ from country to country, so look for local resources. In the UK Heather Brooke's *Your Right to Know* is a great reference volume, while Montague and Amin's *FOIA Without the Lawyer* is a useful complement.

Most introductory journalism textbooks will cover the process of making contacts - consider building relationships with FOI officers, data analysts, statisticians, academics and others who work with data directly and can explain the problems with it.

The final way of getting data is **scraping**: automating the collection of data from anything from one to thousands of webpages or online documents. If you want to know more about that my book *[Scraping for Journalists](https://leanpub.com/scrapingforjournalists)* covers the skills from very basic simple scrapers right through to more powerful tools.

#### Data cleaning

Sadly there aren't many comprehensive resources on data cleaning (I may write an ebook on that some day!), but check out the online documentation for **Open Refine** (formerly Google Refine), and blogs like Tony Hirst's [OUseful.info](http://OUseful.info). You can also find a number of [posts about data cleaning on my Online Journalism Blog](http://onlinejournalismblog.wordpress.com/tag/google-refine/).

#### Statistics

There are some excellent books that you should check out if you don't want to overlook problems with the data you're working on. *[How to Lie With Statistics](http://astore.amazon.co.uk/onlijourblog-21/detail/0140136290)* by Darrell Huff is a classic - and also mercifully succinct if you don't like big books. Michael Blastland and Andrew Dilnot's *[The Tiger That Isn't](http://astore.amazon.co.uk/onlijourblog-21/detail/1846681111)* is a very insightful read into problems with statistics, written by the people behind a radio programme all about the subject, and Kaiser Fung's *[Numbers Rule Your World](http://astore.amazon.co.uk/onlijourblog-21/detail/0071626530)* is a similar book from someone who blogs about the same topics. Ben Goldacre's *[Bad Science](http://astore.amazon.co.uk/onlijourblog-21/detail/0007240198)* not only looks specifically at science and health stories, but is also a very enjoyable read.

#### Visualisation

*[The Wall Street Guide to Information Graphics](http://astore.amazon.co.uk/onlijourblog-21/detail/0393072959)* by Dona Wong is one of the most accessible books I've read on visualisation in general. *[Visualize This](http://astore.amazon.co.uk/onlijourblog-21/detail/0470944889)* by Nathan Yau covers the technical side of visual communication.

#### Spreadsheet formulae

You can get a number of general purpose books on Excel and spreadsheet software. These are generally aimed at people using them for non-journalistic purposes, so you need a bit of imagination.

A different approach is to simply search for what you need to do and the words 'Excel' or 'Google spreadsheets', e.g. "adding two numbers Excel" or "calculating a percentage Excel". You'll generally find a helpful tutorial, and if you prefer videos, use YouTube.

My next book, *[Telling stories with spreadsheets: recipes for interviewing data - and getting answers](https://leanpub.com/spreadsheetstories/)*, demonstrates a range of techniques for asking more questions of your data, from calculating percentages to adding extra data, cleaning it, and combining data from different sources.

If you find any other books useful that aren't mentioned here, please let me know and I'll add it to the book, along with an acknowledgement.
