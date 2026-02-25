<!-- chunk: 3/3 | source: 10-finding-stories-spreadsheets.md | words: 23543 -->
<!-- headings: Comparing change visually by generating sparkline charts for every row: `SPARKLINE`; Writing a `SPARKLINE` formula; Customising how the sparkline appears: bar charts; Sparkline bar charts with more than two numbers; Keeping it relative: specifying minimum and maximum scale; Maximum limits on sparkline bar charts; Setting colours in sparklines; Recap; Last chapter exercise: grabbing and visualising live data with `IMPORTHTML` and live charts; Asking questions (or allowing users to), SQL-style: `QUERY`; Forming the question: `Select`, `Where` and `Order by`; Selecting which columns you want to show in the results; Specifying a criteria for which results are shown; Ordering the results; Showing only the top few results: `limit`; How is `QUERY` different from SQL?; More complex clauses: `group by` and `pivot`; Adding more than one calculation column; Labelling your columns; Calculations with text data -->

## Comparing change visually by generating sparkline charts for every row: `SPARKLINE`

Using charts and maps to represent data is beyond the scope of this book - with one exception: **sparklines**.

Sparklines are tiny line or bar charts which are drawn *within a cell in your spreadsheet*. Unlike data visualisation more generally, their purpose is entirely personal: a way for you to, at a glance, interpret the data in each row or column.

Google Sheets has a special function for drawing these tiny sparklines: `SPARKLINE`.

You cannot use `SPARKLINE` in Excel. Instead [more recent versions of the software allow you to create them using buttons](http://www.howtogeek.com/howto/16759/how-to-use-sparklines-in-excel-2010/).

Here's what a typical series of sparklines looks like:


As you can see, they are very small indeed.

Those tiny charts show seven or so numbers in a line chart. In the example above, specifically, the values of a stock over several days of trading. But the values could be anything.

<aside>

The example above is actually using the `GOOGLEFINANCE` function we explored in a previous chapter. If you're interested, the formula is `=SPARKLINE(GOOGLEFINANCE("msft","price",TODAY()-10, TODAY())` - but we're going to start with some easier examples.

</aside>

What sparklines allow you to is *at a glance* **see how a series of values are behaving**.

In the example above we can see instantly that:

- The first sparkline (Microsoft stock) rose in value and then stayed there;
- The second sparkline (Apple stock) has been up and down;
- And the third sparkline (Amazon) dropped before rising.

Obviously sparklines' use is not limited to seeing how stocks behave: you could use the same function to show you how crimes have changed over a series of years in a number of different areas; or how accident numbers have behaved; or incidences of disease; or levels of poverty; or educational performance; sporting performance; and so on.

Below, for example, are sparklines showing how the end-of-season points totals of football clubs in the English Premier League have changed over four years:


Note that the years must be in order, and that non-applicable years must be empty


Now, some clubs have only been in the Premiership for a couple of seasons, and some have only been there for one season.

The `SPARKLINE` function can deal with there only being two or three numbers in the cells, and the others being empty: in those cases it will generate a sparkline for the two or three numbers it finds: for example, Southampton, which only has two seasons' values, generates a straight sparkline showing the change from one value (at the bottom, because it is their lowest total) to the other (at the top, because it is their highest).

However, **if there is only one number, or if any cell contains an error message** like `#N/A`, then `SPARKLINE` will generate an `#N/A` error.

For that reason, **if you expect cells to contain errors then you should do some cleaning first**, such as find-and-replace on errors.

### Writing a `SPARKLINE` formula

The `SPARKLINE` function can have up to two ingredients:

1.  The range of data you want to show in your sparkline;
2.  And *how* you want the sparkline to be formatted.

The second ingredient is optional, and in cases where you don't want to compare sparklines with each other, you can safely ignore it.

If all you do is specify the range of cells containing your data, then the `SPARKLINE` function will use a standard sparkline to show it.

The only times you *need* to specify the second parameter is if you want to keep all sparklines to the same minimum and/or maximum, or to use a sparkline bar chart, as we'll come onto later.

So, a basic `SPARKLINE` formula will look like this:

`=SPARKLINE(A2:A4)`

That particular example takes the values in cells A2 to A4 (three values, if none of those cells are empty) and generates a standard sparkline from those.

The example below, in contrast, uses the cells `B1:T1` as its ingredient for the first row, and this is copied down to do the same for row 2.

Again, what the sparkline shows you is something that isn't immediately apparent from the data itself: that Bolton's performance has improved in the last few games: showing a visible increase in goals scored, and a drop in goals conceded. That happens to coincide with the appointment of a new manager.


### Customising how the sparkline appears: bar charts

The second, optional, ingredient in the `SPARKLINE` function is specific instructions on how the sparkline looks.

This parameter can be quite complicated, because it can involve all sorts of options including

- The type of chart (line or bar)
- The minimum value on the horizontal axis (line charts only)
- The maximum value on the horizontal axis
- The minimum value on the vertical axis (line charts only)
- The maximum value on the vertical axis (line charts only)

Here, then, is a `SPARKLINE` formula which uses that second optional parameter to specify that it doesn't want a line chart (the default), but instead a bar chart:

`=SPARKLINE(A2:B2,{"charttype","bar"})`

Note that this second parameter is placed inside curly brackets:

`{"charttype","bar"}`

In this case, the first item is the type of information we want to specify (`"charttype"`), and the second is the *value* of that (`"barchart"`), with the two separated by a comma.

What you get may be at first confusing, because **the bar chart runs horizontally**.


A series of sparkline bar charts, using the values to the left. On the right are extra calculations to show in numbers what the bar charts are showing visually


The example above tries to make the process clearer: the `SPARKLINE` formula visualises the contents of two cells in columns A and B, using the chart type `"bar"` to do so.

The resulting bar charts show one bar (in orange) from the left to illustrate the number in column A in the same row, followed by a second bar (in blue) to illustrate the number in column B.

Everything is relative so, for example, in row 8 the figure `2000` from cell A8 only fills half of the bar chart because the other number `2000` in B8 is just as large. But in row 6 the figure `400` fills up two-thirds because the other number is much smaller: `200`.

The chart **assumes that one number is not part of the other**. So, for example, this could not be used if any of your columns was a 'total' while others were a 'part'.

To illustrate this I've added two columns to the right of the sparklines: a total of both numbers, and a calculation to show the column A number as a percentage of that.

That percentage is essentially what the orange bar shows - but only when there are only two numbers being used.

#### Sparkline bar charts with more than two numbers

When you use the same technique on more than two numbers you essentially get a stacked bar chart - but one that is stacked **horizontally**, and what's more: only uses two colours.

This, for example, is what happens when we create sparkline bar charts for those Bolton goals scored and conceded:


It's pretty, but it's hard to understand what it *means* unless you can get your head around the workings underlying it. And what makes it more difficult is that **the zero values are not shown at all**.

The 'Goals conceded' row is perhaps easier to understand: looking at the bar chart from left to right you can see:

- The first (orange) 'bar' represents 3 goals conceded.
- The next five (blue, orange, blue, orange, blue) are all the same, slightly shorter, size, and all represent 2 goals conceded, five games in a row.
- Next we have a large orange chunk about the same size as the one for when 3 goals were conceded - but the chart says only 1 goal was conceded. So why is that?

The answer is that it's actually *two* orange bars, because the blue bar in between is non-existent: it represents the zero number of goals conceded in that match.

Put another way: the orange bar for 1 goals is nestled next to the orange bar for 2 goals, with no blue bar (zero goals) in between. That creates the visual effect of an orange bar which is '3 goals' wide.

By now you should have realised that **sparkline bar charts are not best used for any data which contains zeroes, or which contains too many numbers**.

The more numbers you try to include, and the smaller the differences between them, the less utility the sparkline bar chart has.

### Keeping it relative: specifying minimum and maximum scale

You may have spotted a problem with using sparklines to visually compare different elements: the sparklines are all relative.

In our sparklines for stock prices at the start of this chapter, for example, we could see how prices had changed: but we had no idea what those prices were changing from or to.

And there are big differences: Microsoft had gone from 48.68 to 49.58; Apple from 109.01 to 114.18 and Amazon from 299.86 to 327.82.

So, firstly, each sparkline shows the stock starting from the same point, even though each one started from very different prices.

Secondly, each sparkline shows a different *range*: Microsoft moved by only 0.9; Apple by more than five times that and Amazon by more than five times *Apple* (over thirty times the change that Microsoft experienced).

That was in absolute terms, but you could also look at the changes proportionally: Microsoft's change represented an increase of less than 2% but Amazon's was over 9%.

You get the picture.

**Specifying the minimum and/or maximum values for the sparkline is a good way to correct this if you want all your sparklines to be using the same base or maximum**.

And you can do this in your second parameter with these labels:

- `"xmin"`
- `"xmax"`
- `"ymin"`
- `"ymax"` for line charts
- or simply `"max"` if it is a bar chart

The first letter of each label specifies the **axis**: for example `"xmin"` and `"xmax"` say you want to specify the minimum and maximum values on the x axis (horizontal). Replace x with y and you're specifying the values for the y axis (vertical)

<aside>

#### Maximum limits on sparkline bar charts

In the case of the bar charts there is only one axis, so `"max"` simply specifies what the full length of the cell should represent.

Setting the `"max"` to be the value of the biggest entry, for example, means all other sparkline bar charts will now be reduced accordingly so that the bars take up the proportion of *that* value, rather than of the total of all numbers used in that formula.

Here, for example, is a formula which grabs the numbers in A2 and B2, shows them in a bar chart, and specifies that the maximum value should be 4000:

`=SPARKLINE(A2:B2,{"charttype","bar";"max",4000})`

And here is the effect on the sparkline bar charts:


In this example we have added a maximum to the axis, so the bar charts don’t fill the entire cell unless the values add up to that total


However, if the maximum value is *smaller* than the total of any values, the bar chart will be 'chopped off'. Here's what happens when we change the maximum to 2500:


In this example the max has been set at 2500, which makes one bar misleading: the first value of 2000 takes up 80% of that bar, while the second value - also 2000 - only takes up the last 20% before it is chopped off


</aside>

As with the chart type, the value is specified by naming it: `"ymin"` followed by a comma, and the value you want to use, e.g. `"ymin", 0`

Note that the quality needs to be **in quotation marks** but the value *does not*.

**If you want to use more than one type-value pair, then each pair must be separated by a semi colon**, like so:

`"ymin", 0; "ymax", 100`

And of course remember this is all in those curly brackets:

`{"ymin", 0; "ymax", 100}`

For a line chart you can specify **any or all of the minimum and maximum values**; and you *don't* have to specify the chart type.

Returning to our example of Premiership team points finishes, then, we can set our sparklines to have a base of 36, if that's the lowest points total over that period, like so:

`=SPARKLINE(B2:E2,{"ymin",36})`

Now the teams that consistently score more points will have more stable sparklines, because their lowest performance (64 points for Chelsea in 2012 and Manchester United in 2014) is no longer taken as the base for their sparkline.


Equally we could set a *maximum* value for the sparklines, like so:

`=SPARKLINE(B2:E2,{"ymax",90})`

The biggest impact here will be on those teams who finish with *lower* points totals, because their sparklines will now not 'peak' at the top of the cell. Only those teams scoring close to the maximum value (90, in this case) will see their sparklines peak.


Note that Southampton’s line, which previously ran from bottom to top, is now tempered by the upper range it’s been given


And of course you will most likely want to use both, so that *all* sparklines are using the same base and range, like so:

`=SPARKLINE(C2:F2,{"ymin",36;"ymax",90})`

The picture that emerges now is of relative stability: most teams score within a more narrow range of points than the default sparklines suggested.


Only Newcastle United stand out in row 9 (one season on 65 points nestled between three seasons scoring in the 40s) and Liverpool in row 12 (scoring in the 50s for two seasons then breaking into the 60-70 range before narrowly missing out on the title with 84 points).

<aside>

#### Setting colours in sparklines

If you want to change the colours of sparklines you can do that too. For line charts you just have to select the cells containing your sparklines and change the *font* colour (not the fill colour).

For bar charts you need to alter the formula itself to add values for `"color1"` and `"color2"` like so (only available in the new version of Google Sheets):

`=SPARKLINE(A2:B2,{"charttype","bar";"max",4000;"color1","red"; "color2","green"})`

You can use words for common colours like 'blue' and 'black', or [hexadecimal codes](http://www.w3schools.com/tags/ref_colorpicker.asp) for more specific colours like so:

`=SPARKLINE(A2:B2,{"charttype","bar";"max",4000;"color1","#CC66FF"; "color2","#99FF33"})`


At this point we’ve left journalism behind. Time to get back on track


</aside>

### Recap

- `SPARKLINE` is a function which you can use in Google Sheets to draw sparklines in a particular cell
- Sparklines are **tiny line or bar charts which are drawn *within a cell in your spreadsheet***.
- Sparklines can be useful as a quick way for you to, at a glance, **interpret the data in each row or column**.
- You cannot use the `SPARKLINE` function in Excel. Instead [more recent versions of the software allow you to create them using buttons](http://www.howtogeek.com/howto/16759/how-to-use-sparklines-in-excel-2010/).
- The `SPARKLINE` function has **two parameters: the cells you want to visualise; and *how* you want to visualise that**.
- **The second parameter is optional**: if you do not specify that then it will generate a line chart with the minimum and maximum points corresponding to the lowest and highest values in that particular range.
- This means that **two sparkline charts may have different bases and peaks**, unless the maximum and minimum are specified in the formula.
- **Specifying the minimum and/or maximum values for the sparkline is a good way to correct this if you want all your sparklines to be using the same base or maximum**.
- **You can specify that you want to generate a bar chart** using `{"charttype","bar"}` as your second ingredient.
- The sparkline bar chart will **create a bar horizontally, across the cell**.
- **Each bar in that bar chart will correspond to a value in the range specified**. If you specify more than two numbers this can create a 'bar code' effect which is not always easy to interpret.
- **Sparkline bar charts are best not used for any data which contains zeroes, or which contains too many numbers**.
- **Zero values will not be shown**, for the obvious reason that zero is nothing.
- You can **specify the colours of the bar chart by using `"color1"` and `"color2"` followed by the name or hexadecimal value of the colour in quotation marks**, e.g. `{"charttype","bar";"color1","#CC66FF"; "color2","#99FF33"}`.
- You can **specify the colour of a line chart by changing the text colour for those cells**.
- **If you want to specify more than just one quality of a chart then each quality-value pair must be separated by a semi colon**, like so: `"ymin", 0; "ymax", 100`

### Last chapter exercise: grabbing and visualising live data with `IMPORTHTML` and live charts

At the end of the chapter on live charts I included an exercise which involved finding a table which is regularly updated with numbers such as [Nottingham Trent University's](http://www.ntu.ac.uk/ecoweb/carbon_challenge/league_table/index.html) or [that of the Irish Nurses and Midwives Organisation](http://www.inmo.ie/6022).

1.  To use `IMPORTHTML` to pull that data into a Google sheet you might write something like `=IMPORTHTML("http://www.inmo.ie/6022","table",1)`
2.  To generate a chart for that data you will need to grab some of those values into a separate, simpler, chart that omits columns you don't want. The simplest way to do that is to find an empty column and type `=B1` to grab the first cell of the first column you want (for example, hospital names). Then, next to that, `=F1` to grab the first cell of the other column you want (for example, totals). Then select both cells and copy down however many cells you need to grab all rows for those columns.
3.  You can now select all the cells in your new table (essentially columns B and F from the original) and generate a new chart using **Insert \> Chart**. Then click on the upper right corner to select the menu which allows you to publish that chart, following the steps to link or embed according to your preference.


## Asking questions (or allowing users to), SQL-style: `QUERY`


The BBC track public health data and allow users to ‘query’ it themselves, in a simple way


The Mirror’s Ampp3d data team also allow users to query data relevant to them


One of the most useful functions only available in Google Sheets is `QUERY`. If you've ever used Structured Query Language (SQL) then `QUERY` will be very familiar to you: it allows you to form questions of your data like: '*Select all the lines in this data where the first name is Alice and the age is over 25* or: *Group all the data by city, and count how many entries there are in each*'.

If you *haven't* used SQL then you may be excused for thinking "Well, I can do all of that with other functions and pivot tables". And of course, you can.

There are two major advantages to using `QUERY`, however:

1.  Firstly, it allows you to quickly perform a number of calculations and filters all at once
2.  And secondly, it allows you to *dynamically generate versions of your data* which answer particular questions.

That second part will bear some further explanation. But let me put it like this: if your data is published, `QUERY` allows you to create as many different URLs as the number of questions you can come up with. Each URL will show a different view on your data which answers that question. The user writes the query (either literally in the URL, or by entering criteria on a form), not you.

### Forming the question: `Select`, `Where` and `Order by`

`QUERY` has two required parameters, plus a third, optional, parameter. These are:

1.  The **range of cells** containing the data you want to run your query on
2.  The **query** itself, expressed as a string inside quotation marks
3.  Optionally, the *number of header rows you want* on the result. If you don't specify this, the formula will take an educated guess. Most of the time you have no need to use this (it results in some odd formatting if you specify fewer or more columns than you're getting)

The **range of cells** you specify is likely to be the cells containing a table, somewhere in your workbook. In many cases it's going to be on another sheet entirely, in order to keep your results separate.

The **query** is where the real work is done. Here you will need to know a number of special commands, called **clauses**.

These **clauses** are taken from the [Google Visualization API Query Language](https://developers.google.com/chart/interactive/docs/querylanguage) - but you really only need to know five. And these work exactly the same way as they do in SQL:

- `Select` is used to identify which columns you want to **show** (not necessarily the ones you're questioning)
- `Where` is used to specify **conditions**, such as 'Where this column has this value' or 'Where that column is below this value'
- `Group by` is used to **aggregate** results, in the same way as a pivot table might group payments by company. For example you might group results (for example totals or averages) by each country listed in column D, or each category in column E.
- `Order by` is used to **order** the results: for example by a numerical column (highest to lowest, or lowest to highest), or by a text column (alphabetically A to Z or Z to A)
- `Pivot` is used to turn values into new column headings. For example if you wanted a column for every year or location in the data.

As you can see, most of these clauses use simple language and are pretty intuitive to use.

#### Selecting which columns you want to show in the results

By way of example, here's a very simple `QUERY` formula:

`=QUERY(A1:D200,"select C,D")`

The first ingredient, `A1:D200` specifies where the data is contained.

The second ingredient is the query: `"select C,D"`

There is one clause in that query: **select**.

All that this does is use `select` to say that it only wants to show two columns of results from that range specified in the first parameter: C and D.

Note that these are separated by a comma and not a semi-colon.

**You can put those columns in any order**. So, for example, we could say `"select C,D,A"` and the result would show column C, then D, then A in that order.

But **you must use upper case letters to identify columns**: "`select c,d`" will generate a `#VALUE!` error.

We've not added any more clauses such as conditions, ordering or grouping. So all that this does at the moment is grab two columns from the original data, and show the contents. So we have 200 results.

#### Specifying a criteria for which results are shown

Now let's take that formula and add an extra clause like so:

`=QUERY(A:D,"select C,D where B='Aintree'")`

Now there are *two* clauses in the query: **select** and **where**: `"select C,D where B='Aintree'"`

The `where` clause sets a condition: it now doesn't want *all* cells in C and D; it only wants those *where* the value in B is 'Aintree'.

Note that because this value is *also* a string, we need to use **single quotes** to identify it: otherwise it would be confused with the double quotes inside which this whole query sites.

<aside>

If your criteria involves numbers rather than strings then you do not need quotes at all, for example:

`=QUERY(A:D,"select C,D where E>5000")`

Remember that dates are stored as numbers too, so you just need to know the number for the date you want to use as your criteria. So for example dates after March 12 2011 would be 'greater than 40614'. See the chapter on dates for more on how to find this number and work with it.

</aside>

Our 200 results have now been narrowed to just 22 which match the query. And the query still only fetches the details in columns C and D.


You can create multiple criteria or alternative criteria (i.e. data which meets this criterion *or* that criterion), but we'll come onto that below.

#### Ordering the results

Fancy upping the ante to three clauses? OK, then: let's **order** the results by name of horse, which is column D:

`=QUERY(A1:D200,"select C,D, A where B='Aintree' order by D")`

This third clause is `order by` and all it needs is the column letter you want to order by.

By default it will order **in ascending order**: from A to Z or, in the case of numbers, from lowest to highest.

To order it **in descending order** - from Z to A or largest to smallest - add `desc` like so:

`=QUERY(A1:D200,"select C,D,A where B='Aintree' order by D desc")`

You can specify ascending order too, with `asc`:

`=QUERY(A1:D200,"select C,D, A where B='Aintree' order by D asc")`

And you can order by multiple columns in order. For example:

`=QUERY(A1:D200,"select C,D, A where B='Aintree' order by A asc, C desc")`

The formula above first orders by A (the date, earliest first) and then by C (the cause of death, in descending order).

Where there is more than one entry with the same date, then, those entries are further sorted by cause of death.

Note that in this clause, there is a **comma** after `A asc` and before `C desc`.

<aside class="tip blurb">

#### Showing only the top few results: `limit`

One extra clause which can come in useful is `limit`: this specifies that you only want a certain number of rows of results. For example, you could limit results to the top 3, or the bottom 5, or the top 10.

As you can imagine this is best combined with `order by`. So if we wanted to show the five biggest amounts in column C we would specify somewhere in our query `order by C desc limit 5`.

</aside>
<aside>

#### How is `QUERY` different from SQL?

`QUERY` is a great way to get started on Structured Query Language, which you'll need if you want to question large and/or multiple datasets.

The one main difference is that SQL uses `FROM` to identify what table or tables it is fetching data from (by the table's name), e.g. `SELECT * FROM Horsefatalities`. The `QUERY` function, however, just specifies the source data as its first parameter, and by referring to the cells rather than the name of any file.

A second difference is that SQL is often used to grab data from more than one table, [using `JOIN` to combine data from each](http://www.w3schools.com/sql/sql_join.asp) into a new table. Sadly [Google's query language](https://developers.google.com/chart/interactive/docs/querylanguage) does not include a `JOIN` clause.

Finally, SQL's big advantage is that it is querying *files* (flat spreadsheets in CSV format, for example), rather than running *within* a spreadsheet. This means large datasets which you *could* query with SQL would be too big for Google Sheets, or constantly crash or freeze Excel.

Those differences aside, however, there's not much in it. Once you've used `QUERY` on smaller datasets it should be relatively easy to pick up SQL.

</aside>

### More complex clauses: `group by` and `pivot`

The `group by` clause is not quite as simple as other clauses. This is because it needs to be combined with a calculation such as `SUM`, `AVG`, `MAX` or `COUNT`.

These are called **aggregation functions** and are very similar to similarly-named functions in Excel or Google Sheets (with some key differences I'll come on to).

<aside class="information blurb">

A list of **aggregation functions** is [available in the documentation for Google's Query Language](https://developers.google.com/chart/interactive/docs/querylanguage#aggregation_functions)

</aside>

Here's an example of what I mean. In the chapters on `GOOGLETRANSLATE` and averages I mentioned [a dataset from the European Investment Bank](http://www.eib.org/projects/loans/list/) which shows details on every loan issued by the bank. When opened in a spreadsheet it has the following columns:

> A: Name of recipient
>
> B: Region
>
> C: Country
>
> D: Sector
>
> E: Date of signature
>
> F: Signed amount
>
> G: Description

If we wanted to query that data to **group** it into total amounts for every region, we would write the query like so:

`=QUERY('Sheet 1'!A1:H211,"select B, sum(F) group by B")`

In that formula above we are grabbing the data from another sheet, called 'Sheet 1': specifically cells A1 to H211 on that sheet (for the sake of simplicity I'm not going to select thousands of rows).

The *query* we are running on that data is to `select` B (the region). Note that we need a **comma** immediately before we move on to the `group by` clause.

We then use `SUM` to specify that we want to total up the values in column F (the loan amounts) *and* group those sums by B (the region).

It might sound like we're doing the same thing twice but that's one of the quirks of `QUERY`: [the documentation specifies](https://developers.google.com/chart/interactive/docs/querylanguage#Group_By) that "every column listed in the `select` clause must be listed in the `group by` clause" (with some exceptions).

And we don't actually get *just* column B in the end result: we also get a second column, which has a name that prefixes the column we are summing with the word `sum`: in this case `sum Signed Amount (euro symbol)`.


If you want to pull in more than just the column you are grouping by, you'll still have to list it under `group by`.

See, for example, what happens when I change `select B` in the formula above to `select B,C`, so that the formula reads `=QUERY('EIB loans 200rows'!A1:G211,"select B,C, SUM(F) group by B")`


You get a `#VALUE!` error.

Making sure we *also* change `group by` to refer to the same columns - `group by B,C` - solves the problem.


And you can do more than grouping by sum: you can group by `MAX` (maximum amount for each country, region, etc.); by `MIN` (minimum amount for each); `COUNT`; or average.

Notably, **the average is not calculated using AVERAGE**. Instead you must use `AVG`, like so:

`=QUERY('Sheet 1'!A1:H211,"select B, avg(F) group by B")`

#### Adding more than one calculation column

Using `AVG` or `SUM` will generate a table with a column specifically containing the averages or sums grouped by the column you specified.

But what if you want to do both? Well, you can.

All you have to do is add a **comma** between the two calculations. Here, for example, is a formula which groups by region (column B) the average loan values and the total amount of loans (F):

`=QUERY('Sheet 1'!A1:H211,"select B, avg(F), sum(F) group by B")`

You can add more and more columns by adding another comma and the calculation you want to use.

<aside class="tip blurb">

#### Labelling your columns

You can change the headings in the results of your query by using the `label` clause.

The `label` clause should be followed by the letter of the column and the label you want to use for that, in inverted commas, like so: `label B 'Total loans'` or for more than one: `label B 'Part of the world', C 'Part of the region'`.

</aside>

#### Calculations with text data

Two of these functions - `AVG` and `SUM` - only work with numerical data. But curiously the other three - `MAX`, `MIN` and `COUNT` - will work with text data too, unlike the functions of the same name in Excel/Google Sheets, which only work with or count numbers.

When used with text `MAX`, for example, will give you the entry which is **alphabetically last**. So, 'zebra' rather than 'ant'.

Conversely, `MIN` will give you the entry which comes first alphabetically: 'aardvark' rather than 'zonkey', then (a zonkey is a cross between a zebra and a donkey! And don't get me started on zedonks...)

`COUNT` will count numbers *or* text. So, for example, if B contained the region for each loan and we simply wanted to know how many loans there were to each region we could try the following:

`=QUERY('Sheet 1'!A1:H211,"select B, count(C) group by B")`

In this case the query counts how many entries there are in column C, and groups them by region (column B). So if there are 52 entries in C for the region 'South Africa', and 4 for 'European Union', then the resulting table will show that, and so on for all other regions.

<aside class="warning blurb">

#### Why we don't count the same column

Why don't we just `count` the same column we're selecting and grouping by, as we might in a pivot table? Well, using *any* column that we're selecting/grouping will generate an error. Sorry, that's just the way it is.

So, the following formula will generate an error:

`=QUERY('Sheet 1'!A1:H211,"select B, count(B) group by B")`

And so will this:

`=QUERY('Sheet 1'!A1:H211,"select B,C count(C) group by B,C")`

You just need to make sure you're counting a column which doesn't have any empty cells.

</aside>

#### The `pivot` clause: adding new columns

Adding the `pivot` clause to your query is a little like using the `TRANSPOSE` function or command: it will effectively switch columns and headings from how they might have looked otherwise.

The key difference is that `pivot` allows you to specify what headings you want to use. If, for example, you had regions in column B then adding `pivot B` to your query would create a heading for each region. If you had years in column C then using `pivot C` would likewise create a heading for each year.

As with `group by`, `pivot` works best with some sort of **aggregate function** like `SUM`, `COUNT`, and so on. Here's one relatively simple example:

`=QUERY('Sheet 1'!A1:G211,"select count(C) pivot B")`

Here the query part of the formula is counting the values in column C, and using `pivot` to specify that it wants the results split into columns based on the values in column B.


In many ways `pivot` is similar to `group by`: automatically the results of that `COUNT` are aggregated (grouped) by whatever is in column B.

The difference, of course, is that you get a very wide table rather than a tall one. Which one you want depends on what you need to do with it, but in most cases a tall one is easier to interpret.

### Writing queries with multiple or alternative criteria

Until now I've only talked about `where` clauses with only one criterion. But often you want to set multiple criteria, for example:

- You only wanted results in one particular category AND above a certain value.
- You wanted results from this category OR this category OR that category.
- You wanted results from this category OR below a certain value.

If you wanted to run a query like those which sets multiple criteria then you will need to use **parentheses** with the `where` clause.

Here is an example:

`=query(A1:D200,"select C,D,A where (B='Aintree' OR B='Wolverhampton')")`

The key part to look at is right after `where`: now we open a parenthesis, start our original criterion `B='Aintree'` then add `OR` and a second criterion, before closing the parenthesis.

If you want the criteria to *all* apply then you need to add `AND` instead of `OR` like so:

`=query(A1:D200,"select C,D,A where (B='Aintree' AND C='Broke Neck')")`

And of course remember you can do this with numeric criteria too:

`=query('Sheet 1'!A11:G221,"select B,C,D,F where (F>5000000 AND D='Energy')")`

### Generating 'hackable' URLs which allow users to see the data their own way

This last part is perhaps the most exciting element of the `QUERY` function - but also the most difficult to explain.

It involves creating what's called a **hackable URL**.

<aside>

A hackable URL has nothing to do with hacking in the popular sense of 'hacking into a system'. Instead, 'hackable' means that an individual can construct their own URL to get different results. ('Hacking' is often misrepresented in media reports as being something illegal. In fact, programmers use the term 'hacking' or 'hack' to refer to any sort of quick fix or workaround).

Search results are one of the most common types of hackable URL. Here, for example, is the URL for results from Twitter's search tool:

`https://twitter.com/search?q=excel`

The URL shows the search query: `q=excel`

You can 'hack' that URL to show results for any search term. For example, replace `q=excel` with `q=spreadsheets` and you'll get a webpage showing results for the search query 'spreadsheets'.

These sorts of hackable URLs allow you to conduct multiple queries quickly. In fact, we've used them already: in the chapter on `GOOGLETRANSLATE` we generated search URLs in other languages by adding terms to the end of the URL `https://www.google.co.uk/search?q=`

</aside>

You will need three ingredients to make up this URL. I'll explain each in turn below:

1.  A **'base URL'** including your spreadsheet's **'key'**
2.  Your **query** in URL form
3.  And a little extra part of your URL to make it display in HTML

In addition, if your spreadsheet has more than one sheet and you want to specify which one, you will also need a **GID** parameter

#### The 'base URL' for public spreadsheets

The '**base URL**' is the term for the part of the URL which always forms the basis of our full URL.

In the examples above, the base URLs are `https://twitter.com/search?q=` and `https://www.google. co.uk/search?q=`

When it comes to public Google spreadsheets that base URL is:

`https://docs.google.com/spreadsheets/d/`

But your specific spreadsheet will have a longer base URL that also includes the **key** for your spreadsheet. To get this, you will need to share your Google spreadsheet publicly.

Open your spreadsheet and click on the **Share** button in the upper right corner.


A new window should open. Click on the grey link in the upper right corner of *that* window that says **Get sharable link**.


Copy the sharable link and paste it into your browser address bar or, better still, a text editor like Notepad (Windows) or TextEdit (Mac).


The key in this URL is highlighted


In the middle of that URL should be your spreadsheet **key**. It comes *after* `https://docs.google.com/ spreadsheets/d/` but *before* any further backslashes like this: `/pubhtml?gid=1535563184&single=true`

The key will be made up of a random collection of letters and numbers - something like this: `1AI8u3TgWnytsngAX0CoWh9mGWT-cSudNvZLyBa79aG0`

In full, then, your specific spreadsheet's base URL should look something like this:

`https://docs.google.com/spreadsheets/d/1AI8u3TgWnytsngAX0CoWh9mGWT-cSudNvZLyBa79aG0`

Copy that part of the URL into another browser or into a text editor - but don't press Enter yet, because **you'll need another part of the URL** too.

#### Adding some code to use the Google Visualisation API Query Language

Now this next part might throw you a bit, but bear with me on this.

*At the end of the URL you have so far*, add the following:

`/gviz/tq?`

This should give you a URL which looks like this (your key will be different):

`https://docs.google.com/spreadsheets/d/1AI8u3TgWnytsngAX0CoWh9mGWT-cSudNvZLyBa79aG0/gviz/tq?`

If you are using a browser like Chrome (not all browsers will support this stage) and pressed Enter now you would get a page full of JSON code.


An example of the JSON generated when you add /gviz/tq to a Google Sheet sharable URL


This is your data represented as JSON code. That can be quite useful in itself if you wanted to use that as a feed for a dynamic visualisation. But that's not what we're doing. We need to do two more things:

1.  add a query to drill down into that data; and
2.  add a parameter to display that as HTML, not JSON.

#### Formatting a query for a URL - and escaping special characters

To add a query to our URL we need to add the characters `tq=` followed by the query as we would write it in a formula - but **with all spaces, operators and inverted commas 'escaped'**.

**'Escaping'** a character means representing it with a special symbol or code. This is generally done for characters which would otherwise be interpreted as *commands* or which can cause problems.

For example, as mentioned earlier in this book, browsers can not handle **spaces** in web addresses, so they are replaced by ('escaped with') either `%20` or `+`.

In our case we will need to replace spaces with `%20`, but that's not all.

Some of the characters which might be similarly problematic in a query include the equals operator, 'greater than' and 'less than' operators, plus operator, and inverted commas.

The 'codes' for those are as follows:

- Inverted comma (`'`): `%27`
- Less than (`<`): `%3C`
- Equals (`=`): `%3D`
- Greater than (`>`): `%3E`
- Plus sign (`+`): `%2B`

Here's an example of a query using some of those escaped characters to show you what I mean:

`tq=select%20A%20where%20C%3D%27Poland%27`

This means `select A where C='Poland'`

Here's the same code with the non-escaped elements in bold:

tq=**select**%20**A**%20**where**%20**C**%3D%27**Poland**%27

The spaces are easy to spot. There are three of those before the equals sign (`%3D`) which comes immediately before the first of two inverted commas (`%27`).

**You don't need to remember all of these codes**. Helpfully, [the reference page for Google's Query Language](https://developers.google.com/chart/interactive/docs/querylanguage) includes a [section](https://developers.google.com/chart/interactive/docs/querylanguage#Setting_the_Query_in_the_Data_Source_URL) with a tool to "encode or decode a query string".


Google’s encode/decode tool


All you need to do is type your query into the box on the left, click **Encode \>** and the box on the right will give you an 'escaped' version which you can paste into your URL.

**Remember to prefix that query with `tq=`**

Once you've generated your query your URL so far should look something like this:

`https://docs.google.com/spreadsheets/d/1AI8u3TgWnytsngAX0CoWh9mGWT-cSudNvZLyBa79aG0/gviz/ tq?tq=select%20A%20where%20C%3D%27Poland%27`

When you put that URL into a JSON-friendly browser like Chrome and press Enter your page of JSON should look much shorter - because now this is not *all* data, but only **the data generated by your query**.


Again, this can be useful if you're working with a developer or a piece of script which requires a JSON input.

But if you *do* want a HTML page showing your results, you just need to add one last parameter to your URL.

#### Presenting the results as a HTML table

The extra bit in your URL that you need is this:

`&tqx=out:html`

This specifies the **output**: HTML is just one option; CSV is another.

When you add that to the end of your URL it should look something like this:

`https://docs.google.com/spreadsheets/d/1AI8u3TgWnytsngAX0CoWh9mGWT-cSudNvZLyBa79aG0/gviz/ tq?tq=select%20A%20where%20C%3D%27Poland%27&tqx=out:html`

And the page should change from confusing JSON code to a plain old HTML table like this:


<aside class="tip blurb">

Tony Hirst identified some of these processes way back in 2009. His post on [Using Google Spreadsheets as a Database with the Google Visualisation API Query Language](http://blog.ouseful.info/2009/05/18/using-google-spreadsheets-as-a-databace-with-the-google-visualisation-api-query-language/) and [Using Google Spreadsheets Like a Database - The QUERY Formula](http://blog.ouseful.info/2010/01/19/using-google-spreadsheets-like-a-database-the-query-formula/) are well worth reading if you want to explore this further - although note that some of the processes have now changed, so you'll need this chapter too.

</aside>
<aside>

#### More than one sheet? Add the GID parameter to specify which sheet

So far we've assumed that your data is on the first sheet of your Google Sheets workbook. But if you want to use these techniques to query different sheets you'll need to add something called the **GID parameter**: a sort of 'ID number' used to identify each specific *sheet* in your workbook.

To find this GID look in your sharable URL, after the key but also after `/pubhtml?`. It will be prefixed by the characters `gid=`.


The GID parameter highlighted in one Google Sheets sharable URL


Copy this parameter, including the `gid=` part. It should look something like this:

`gid=1535563184`

Now you just need to add it to the end of the URL, **prefixing it with the equals operator**, like so:

`&gid=1535563184`

The query will now be applied to that sheet in the workbook identified by the spreadsheet key.

</aside>

### Using a form to allow users to generate their own results pages

So far we've generated the queries ourself. But what if we want users to be able to query the raw data?

One option would be to explain how to first write those queries in Google Query Language, and then encode it into a URL, as we have here.

But that's going to exclude a lot of users. A better option would be to create a form which allows users to enter or select criteria, and then be taken to a URL which encodes those criteria.

There are a number of ways of doing this with HTML, JavaScript, PHP or other languages. Those processes are beyond the scope of this book but if you are familiar with coding, or want to use this as an opportunity to code, the key principles are that you need to take the values being entered or selected in the form, encode those so they work in a URL (in other words, escape special characters and spaces), and then insert them into the URL with the other ingredients described in this chapter.

### Examples of `QUERY` being used in code

Tony Hirst's experiments with the `QUERY` function show the potential of these 'hackable URLs' in making it easier for users to explore your data.

In [the 'Guardian Datastore Explorer](http://ouseful.open.ac.uk/datastore/gspreadsheetdb4.php) he created an interface which allowed users to select one of The Guardian newspaper's public Google spreadsheets (or directly enter a spreadsheet ID):


...and then enter a query in a form:


The background to that is [explained here](http://blog.ouseful.info/2009/05/22/first-steps-towards-a-generic-google-spreadsheets-query-tool/)

Of course rather than require users to enter the query into the form you could provide them with a drop-down menu or more narrow query (such as 'contains'). The possibilities are as wide as your imagination - and of course what you can learn about code!

### Recap

- `QUERY` allows you to **form questions of your data**. These often include terms like 'Select', 'Group by', 'Order by' and 'Where'. When put together a query might mean something like: '*Select all the data from these four columns where the first name column contains "Alice" and the age is over 25* or: *Group all the data by city, and count how many entries there are in each*'.
- Because Google Sheets is web-based, `QUERY` allows you to *dynamically generate versions of your data* which answer particular queries from users.
- `QUERY` has two required parameters, plus a third, optional, parameter. These are: the **range of cells** to query; the **query** itself, and how many header rows you want (optional and generally unnecessary).
- The query itself **uses clauses to filter, sort, pivot, group and display** results.
- **The `select` clause determines what columns you want to show in your results**.
- **You must use upper case letters to identify columns**: "`select c,d`" will generate a `#VALUE!` error.
- **The `order by` clause determines what columns you want to order the results by**.
- By default it orders in ascending order, but **you can specify that it order in descending order by adding `desc`**.
- **You can order by more than one column**, in order.
- **You can put those columns in any order**.
- **The `where` clause determines what criteria you want to set for showing results**: for example that they be above or below a particular number, or contain or start with particular text.
- **You can combine multiple criteria, or set alternative criteria**.
- **The `pivot` clause is used to turn values into new column headings**. For example if you wanted a column for every year or location in the data.
- Although the `QUERY` function allows you to use SQL-style commands in powerful ways, **it is worth exploring SQL itself** if you want to work with big datasets or join datasets together. The [SQLite plugin for Firefox](https://addons.mozilla.org/en-us/firefox/addon/sqlite-manager/) allows you to get started with that without having to download any standalone software.
- **The `group by` clause allows you to aggregate numbers instead of having a row for each one**: for example showing the *total* of all loans for each company (i.e. grouped by company), or the average, or maximum, minimum, or count.
- To use the `group by` clause **you need to indicate how you are aggregating by using an aggregate function** with the value being averaged in parenthesis, e.g. `SUM(F)`. The aggregate functions include `SUM`, `MAX`, `MIN`, and `COUNT`, but for an average you must use `AVG`.
- **Your `group by` clause must specify the same columns as your `select` clause** - otherwise the formula will generate a `#VALUE!` error.
- **The `limit` clause allows you to limit results to a specified number**, e.g. `limit 5` would only show the first 5 results of the query. When combined with `order by`, this allows you to limit results to the top 3, or the bottom 5, or the top 10.
- **The `label` clause allows you to replace the default headings with your own choice**.
- **A hackable URL is one that an individual can change in a meaningful way to get different results**.
- **The 'base URL' is the term for the part of the URL which always forms the basis of our full URL**.
- You can **create a hackable URL by combining your base URL with extra details** such as the key of your particular spreadsheet and parameters which specify that you want to run a query on that spreadsheet, that you want to output in HTML, and the query itself.
- **To get a key for your spreadsheet you must first share it** (publish it) using the *Share* button.
- **You can also specify a particular sheet in that spreadsheet by using the `gid=` parameter**.
- **When you encode a query in the URL you must escape special characters** like spaces, inverted commas, and operators such as 'equals', 'greater than' and 'less than'.
- **You can use a tool on the reference for Google Query Language to encode your query** so that it works in the URL
- **To specify that you want to query the spreadsheet, add `/gviz/tq?` to the URL**.
- When you do this, **by default the spreadsheet - or results of a query - will be displayed in JSON format**.
- **To specify that you want to see the results in a HTML table, add `&tqx=out:html`** to your URL
- Because the URL is hackable, **you can also write HTML or other code which turns users' inputs into new URLs that show the results on applying their criteria**.



## Adding some randomness: spreading out locations randomly using `RAND`


Randomness played a key part in making it possible to see more than one person from the same place


Randomness might strike you as an odd thing to be actually *wanting* in your data. But sometimes it can be useful.

Let me give you just one example: one local journalist in Wales wanted to map people from the area who would be carrying the Olympic torch. But they had a problem: several people share the same general 'location', a town or city rather than a specific street or latitude and longitude.

When 'geocoded' (converted to latitude and longitude), the pointers for each person from the same location sat on top of each other, with the uppermost marker hiding all the others beneath it.

If you wanted to show the density of torchbearers in different areas you could 'scatter' the markers slightly so people can get a visual impression of the distribution of individuals.

A quick way to 'scatter' those locations is to use the `RAND` function, and its fussier brother, `RANDBETWEEN`.

<aside class="tip blurb">

Clearly this brings up some issues around misleading users, so you must be careful to state clearly that "positions are indicative and not exact" - but that is the case even before you do this, because these locations are very approximate to begin with.

A better solution to this problem is to change the size of the marker based on the number of people it represents, if you are able to technically. But for the purposes of demonstrating this function, let's assume you want to show a different visual 'story'.

</aside>

### `RAND`: Give me a number between 1 and 0

`RAND` is one of those rare functions without any ingredients at all. You simply write it as follows:

`=RAND()`

The parentheses are empty.

The result of that formula will be a number between `0.00` and `0.99`. A random number.

<aside class="information blurb">

Actually, no number generated by a desktop computer is *truly* random, because it has to use a recipe of some sort (an algorithm) to generate it. So strictly speaking these numbers are described as **psuedo-random**. That's fine for most use cases.

</aside>

You can now use that number to alter another number: for example, multiplying it by the random number, dividing, adding or subtracting.

For example, when a random number is generated using `RAND` down one column, and then multiplied by number 5, you end up with results varying from 0.09 to 4.45.

But in most cases 0-0.99 is going to be too small or too big a range, and you're going to want to take more control. That's where `RANDBETWEEN` comes in.


<aside class="warning blurb">

Whenever you change the spreadsheet - adding new data, sorting, and so on - the random numbers **re-generate**.

If you only want to generate the random numbers *once* and stick with those (especially if there are calculations based on those) then you must **Copy** those numbers (or the results of calculations) and then select **Paste special \> Values only**. This will paste the *results* of the formulae rather than the formulae themselves, stopping any further random number generation.

</aside>

### `RANDBETWEEN`: Give me a number between whatever I say!

The `RANDBETWEEN` functions allows you to specify what *range* your random number falls between.

In the case of mapping points above, for example, it takes some trial and error to find the range of random numbers which still keeps the latitude and longitude within a relevant range.

Let's say we only want to move the latitude and longitude by a maximum of 0.05. In that case we might use the following formula to generate the shift:

`=RANDBETWEEN(-0.5,0.5)`

...But **it won't work**. Why? Because `RANDBETWEEN` only works with **integers**: that is, whole numbers.

Is this a problem? Only for a moment. Because if we do want a smaller number we can work out a way to *turn* that integer into a fraction. I'll give you a moment to think about it.

Still waiting...

A little more time..?

OK.

All you have to do is **divide the result by 10 or 100** (or a similar number).

Instead of trying to generate a number between -0.5 and 0.5, then, we can generate a number between -5 and 5:

`=RANDBETWEEN(-5,5)`

Then, in a separate column, we divide that number by 10:

`=A2/10`


Alternatively we could combine the two into the following formula:

`=RANDBETWEEN(-5,5)/10`

In this case the results are only going to go to one decimal point: it will either be -0.5, -0.4, -0.3, and so on up to 0.5. So there are only 11 possible outcomes (-0.5 to -0.1, 0.1 to 0.5, and 0.0)

We could generate a wider range of random outcomes by generating a wider initial range and dividing by 100 like so:

`=RANDBETWEEN(-50,50)/100`


Now we have 50 possible outcomes below 0.0 (-0.50, -0.49, -0.48 and so on), and 50 possible outcomes above 0.0 (0.01, 0.02 and so on), plus 0.0 itself: a total of 101 outcomes.

Once you have the range you want you can use that to randomly vary your initial data (in this case the longitude and latitude of locations) *within a determined range*.


Above, then, we have four columns:

- Firstly, generating a random number between -50 and 50.
- Secondly, dividing that number by 100 to get a (still random) number between -0.50 and 0.50.
- Thirdly, our original latitude values: all the same as they refer to the same town
- And fourth, that latitude, minus the random decimal.

That final calculation looks like this in row 2:

`=C2-B2`

Alternatively you could turn three columns into one by combining A, B and D with the following:

`=C2-(RANDBETWEEN(-50,50)/100)`

If the decimal is a negative this actually results in an increase in the latitude: for example 49.1833 minus -0.50 is 49.6833 (remember: "*two negatives makes a positive*"). So our final numbers can be higher as well as lower.

(If it makes more sense to you, *add* the random number instead. In that case adding a negative number results in a lower number; and adding a positive number results in a higher number)

It will probably take a few attempts to get the right range of randomness.

<aside class="tip blurb">

If you want to make sure there are no entries with the *same* random number, add in an error-checking formula which uses `COUNTIF` to check if the same number exists more than once in the range of cells.

</aside>

### Recap

- **Random functions can be useful for introducing some 'noise' into your data** if, for example, you want to randomly scatter locations.
- You must be careful to **make it clear in any resulting journalism that this has been done, and why**.
- The `RAND` function **generates a random number between `0.00` and `0.99`**.
- The `RAND` function **uses empty parentheses** like so: `=RAND()` because the ingredients (the range) is predetermined.
- The `RANDBETWEEN` function **generates a random number between whichever two integers you specify**. For example: `=RANDBETWEEN(0,1000)` will generate a number between 0 and 1000.
- You **must use integers** for `RANDBETWEEN`: **integers are whole numbers** rather than those with decimal places.
- **To convert the resulting integers into a range of random numbers to decimal places, divide it**: by 10 to get a number to one decimal place; by 100 to get a number to two decimal places; and so on.
- This can be done **within the same formula**, e.g. `=RANDBETWEEN(-50,50)/100`

### Exercise: generate random placemarks on a map - within reason

[At this link is some sample data for a series of points all in the same town](https://docs.google.com/spreadsheet/ccc?key=0ApTo6f5Yj1iJdEdGc3BEaTJTakNzN25aTi01Ym9kX1E&usp=sharing).

Download the data and use the random number generation techniques to **scatter the latitude *and* longitude values** within a range of your choice.

Map the results using [BatchGeo](http://batchgeo.com/) or a mapping tool of your choice. Make sure you select the latitude and longitude as the columns to map on.

See if the results are scattered too widely, or tightly. Then repeat the process to narrow or broaden the range of randomness, and keep testing the results until you're happy.

If you prefer to do this for an area you have knowledge of, replace the latitude and longitude with those for another area of your choice (tip: search for a location on Bing Maps and the resulting map should include a latitude and longitude).


## Is this value ranked high or low? What value is 3rd? `RANK`, `LARGE` and `SMALL`


Many stories are based on finding out where your own country or region ranks in the latest data


Right at the start of this book I talked about *sorting* data to find out which values come top or bottom. However, there is a family of functions which will give you a lot more control in finding out not just who is top or bottom, but the **rank** of any value in any series of values.

This is particularly useful if you want to ***compare ranks***.


Ranking isn’t just about statistics - it can be used in consumer stories too


For example, say you had a table showing school performance across the last two years.

Each table shows the percentage of pupils achieving the top grades in that year. You can use `RANK` to find out what rank each percentage would have placed the school in for each year.

But once you have both ranks, you can also calculate if they have moved up (from a lower rank to a higher one), or down, and which schools have moved the most.

Another common situation is where you have a table for different institutions or individuals showing dozens of scores on various measures and different scales. These can be converted to ranks for easier comparison - and also to calculate 'average' ranks (or highest or lowest) for each institution or individual to help focus or speed up your process of identifying newsworthy entries.


Here we see the raw data the headline above is based on - as it stands we cannot see whether these figures are better or worse than other areas


Similarly, you can use `PERCENTRANK` to see what percentage of other values a number ranks *above*. For example, if a team has conceded 45 goals this season the `PERCENTRANK` function could tell you 'They have conceded more goals than 95% of teams in the league'.

Here is how both functions work:

### Using the `RANK` function

The `RANK` function needs at least two ingredients:

- The value you want to rank
- And the range of values you want to rank it within (an array of cells)

There is also a third optional argument:

- Whether you want to rank in descending or ascending order

A typical formula looks like this:

`=RANK(C2,C1:C3000)`

The first ingredient, then, is the cell containing our value: `C2`

And the second ingredient is the range of cells we want to rank it within: `C1:C3000`. Text values are ignored.

By default it will give us the rank where values are ranked in **descending** order: that is, from biggest to smallest.

Of course this makes sense if we are dealing with values where more is better, like test scores, goals scored, or crimes solved, or (sometimes) income.

However, if we are dealing with values where *less* is better, like goals conceded, or crimes committed, or (sometimes) money spent then we need to rank it in **ascending** order.

To do this, add `1` as a third argument like so:

`=RANK(C2,C1:C3000,1)`

<aside class="information blurb">

If there is more than one of the same value, then `RANK` will return the *earliest* rank for the value. In other words, if the value occupies 3rd, 4th and 5th position then the result of the formula will be `3`.

</aside>

#### `RANK` is replaced by `RANK.AVG` and `RANK.EQ`

The `RANK` function has actually been replaced by two slightly more specific versions of the function: `RANK.AVG` and `RANK.EQ`. It may be that later versions of Excel stop supporting the more simply-named function.

`RANK.EQ` works exactly the same as explained above.

`RANK.AVG`, however, returns an *average* rank rather than the rank of the value when it first appears.

What this means is that if the specified value occupies 3rd, 4th and 5th position when placed in order (descending or ascending) then the result of the formula will be `4`.

If the value just occupies 4th and 5th position then the result of the formula will be `4.5`.

<aside>

Patrick Scott, a data journalist who works in Trinity Mirror's data unit, uses `RANK` and `LARGE` regularly in his work.

"I scraped [data on public health outcomes](https://www.nhs.uk/Service-Search/performance/Results?ResultsViewId=1003), ranked each local authority on each measure, calculated their average rank and then ranked their average rank."

The resulting stories included ['*Buckinghamshire is one of the top 10 healthiest areas in England*'](http://www.getbucks.co.uk/news/local-news/buckinghamshire-one-top-10-healthiest-8142556) and ['*Wokingham named second healthiest area in the country*'](http://www.getreading.co.uk/news/local-news/wokingham-named-second-healthiest-area-8144742).


One of the stories based on Patrick’s work with the RANK function


In another set of stories Patrick looked at children who were not going to school in their own local authorities, based on a [government dataset](https://www.gov.uk/government/statistics/schools-pupils-and-their-characteristics-january-2015).

"This was a bit more involved but essentially we knew that a child was probably most likely to go to a school in the local authority in which they live. So we wanted to know what the second most popular local authority was.

"To do this manually would have taken forever seeing as we'd have to look across 200-ish columns for each of the 200-ish rows. But using =LARGE(data,2) gives us the number we want and putting this in an INDEX formula gives us the name of the destination authority."


One of the stories based on Patrick’s work with the LARGE function


</aside>

### Finding values at a particular rank: `LARGE` and `SMALL`

Two further functions come in very handy if you want to reverse the process - and get an answer to a question like 'What value is 10th highest?' or 'Which value is second from bottom?'

`LARGE` and `SMALL` count from the top and bottom respectively. `LARGE` will tell you the value which is a specified position from the top (the 'nth largest') and `SMALL` will tell you the value which is a specified position from the bottom.

Each needs two ingredients: the array of cells you want to look at, and the rank you want to grab (from the top or bottom, depending on the function).

So, in a range of ten cells containing the numbers 1 to 10, this formula:

`=LARGE(A1:A10,3)`

...will return the answer `8`, because `8` is the third largest value in that sequence (10 being the first largest, and 9 being the second largest).

This formula, however:

`=SMALL(A1:A10,3)`

...will return the answer `3`, because `3` is the third *smallest* value in the same sequence (1 being the smallest, and 2 being the second smallest).

It does not matter if the values are ordered in any way, and text and empty cells will be ignored.

It is also worth pointing out that if the same number appears twice, it will be ranked accordingly. So, if you put this sequence in column A:

`1, 2, 1, 5, 3, 2, 5, 9, 100`

...the result of `=SMALL(A:A,3)` and `=SMALL(A:A,4)` would both be `2`, because there are two instances of `2`, and when arranged from smallest to largest `2` appears third and then fourth.

> ### Exercise: where does a region rank for youth offending?
>
> [At this link](https://drive.google.com/file/d/0B5To6f5Yj1iJc1o3TzFNTWRfQlk/view?usp=sharing) you will find some data on youth offending. If you move your mouse to the top you should get a button to download a copy to your computer.
>
> The data lists the numbers of offences by under 18s in each local authority in England and Wales. There is a column for each type of offence, which means you can rank where they stand for different offences. This is a good dataset to learn some useful techniques when it comes to ranking.
>
> Firstly, because the data is so big, it may be better to create your rankings on a separate sheet. To do this, first copy the header row, and then copy the column of authorities. Make sure that they are in the same order and you *do not change the order* at any point (for example, don't sort).
>
> Now in cell B2 you can write a formula that references the numbers in the other sheet to give you a rank, like so:
>
> `=RANK.EQ('Offences by authority'!B2,'Offences by authority'!B2:B160)`
>
> This formula tells us that Barking and Dagenham (the first authority) is ranked 37th on arson (the first offence).
>
> ::: 
> 
> 
> 
> :::
>
> Now we need to get the rankings for the other authorities.
>
> Before you do this, **add dollar signs to fix the cell references of the range you're ranking within**. If you do not do this, when you copy the formula down the range will change each time, meaning that rankings will not be comparable. Here's how that formula changes when you add those dollar signs:
>
> `=RANK.EQ('Offences by authority'!B2,'Offences by authority'!B$2:B$160)`
>
> Now copy that formula down the entire B column to get the rank for each authority for arson.
>
> Spot any problems? If you skipped to the bottom of the column (always a good practice) you may have seen that there is a 'grand total' row. This is going to cause problems for our ranking.
>
> ::: 
> 
> 
> Watch out for grand total rows that affect rankings
> 
> :::
>
> **Make sure you delete the grand total row - not only in this calculations sheet but also in the original sheet**: remember that it is the original sheet which is used to work out the ranking.
>
> Now when you go back to the top of the column Barking and Dagenham is ranked 36th.
>
> That should give you the rankings for one offence. To get rankings for all offences you can now copy the formula across into the other columns. Start by copying it from B2 and pasting it into C2.
>
> ::: 
> 
> 
> 
> :::
>
> Now the formula is looking at C2 in the other sheet, and ranking it against the range C2:C159 in the other sheet, like so: `=RANK.EQ('Offences by authority'!C2,'Offences by authority'!C$2:C$159)`
>
> If you don't get a formula like this it may be down to where you have placed your dollar signs in the original formula. Placing it before the B will fix that too - so check that's not happening.
>
> You can now click the bottom right corner of this cell and drag across all the other columns so it repeats the calculation for each one. Then select all the cells you've just created and double-click on the bottom right corner to copy it down the entire sheet.
>
> At this point you have a rank for every authority on every offence - but remember that all these formulae are always working on the original data. **If the original data is changed in any way - for example sorted - then your formulae will be wrong**.
>
> For this reason, once you have made your calculations it is a good idea to copy all the cells containing the results, and paste them as *values only* (you can do this by right-clicking on a cell and selecting **Paste special \> Values only**).
>
> Now you can much more quickly look at a particular area (say, your own) and identify areas where it is ranking highly - or, in contrast, has much lower numbers than most areas.
>
> But there's another problem. You've probably already spotted it.
>
> It helps to look at who's ranking highly on most of these offences. Kent comes top for quite a few: Violence Against The Person; Theft And Handling Stolen Goods; Breach Of Bail. Birmingham comes top for Robbery, Racially Aggravated and Motoring Offences.
>
> Both of these are large authorities, with large populations. And it highlights a problem with any dataset that only gives you absolute numbers rather than proportions or per capita figures: the biggest places will invariably come top; and the smallest places will invariably come near the bottom.
>
> What you need to do, then, is make sure you are comparing per capita figures. To do that you'll need to track down the populations of each area, and divide the offences by that. That will give you a very small decimal, so you may want to multiply this by 1,000 to get a 'per thousand' figure which is more meaningful.
>
> But even that isn't necessarily ideal in this case: remember this data relates to *youth* offences: that is, offences by people under 18. In any country you will have areas which have younger populations (urban centres, for example) and areas which attract older populations.
>
> So if our story is about the criminality of local youth we might make it truly comparably by using the population figures for under 18s specifically (in this case you can also exclude under-10s). The local census figures are going to be a good source for this, and the chapter on `VLOOKUP` will help you to combine figures.
>
> Once you have more proportional figures you can run the ranking again to make it a more accurate comparison.
>
> Before I end, a final note of caution on crime data: remember too that there is a difference between offences and *offenders*: one person can commit many crimes, so be careful not to misrepresent that in how you write about it. And there's always [another story to be had in the data behind the individuals who have committed the most crimes...](http://www.dailymail.co.uk/news/article-2530743/Prolific-offender-given-just-police-cautions-FIFTY-crimes-spanning-12-years-scale-soft-justice-Britain-revealed.html)

### Recap

- `RANK` allows you to **find out the rank of any specified value within a specified range** of numbers.
- Ranking can be particularly useful as a way of **quickly seeing where your country or local area ranks well or badly** across a range of measures - and spotting that story quicker.
- The `RANK` function **has been replaced by `RANK.AVG` and `RANK.EQ`**.
- All `RANK` functions have three arguments: **the value you want to rank; the range of values you want to rank it within (an array of cells); and (optionally) whether you want to rank in descending or ascending order**.
- **By default values will be ranked in descending order** (from biggest to smallest).
- **To specify that you want it ranked in ascending order, use `1` as the third argument** like so: `=RANK(C2,C1:C3000,1)`
- If the value appears more than once both `RANK` and `RANK.EQ` **will give you the highest rank** at which it appears.
- `RANK.AVG`, however, will give you the **average rank** if the value appears more than once.
- `LARGE` will give you **the value ranked in a specified number position**, from a specified array. For example `=LARGE(A:A,1)` will give you the first ranked (largest) value in column A.
- `SMALL` will give you **the value ranked in a specified number position of smallest values**, from a specified array. For example `=SMALL(A:A,1)` will give you the *smallest* ranked value in column A, and `=SMALL(A:A,9)` will give you the 9th smallest value in that column.
- If you're calculating ranks and copying the formula down, remember to **fix the range reference using the dollar sign** to avoid the range changing for each formula.
- **Watch out for grand totals** in your ranges: these will always be ranked top, meaning the 'worst' or 'best' places will end up ranking 'second'. Make sure to delete grand total rows before writing your formulae.
- **Make sure data is comparable** - for example it is per capita or proportional, rather than absolute totals where the populations differ. Of course in some contexts totals *are* comparable because the story compares a single person, team or organisation (e.g. the top goalscorer; team conceding the most goals; organisation making the most money).



## What percentile is this at or above? `PERCENTRANK` and `PERCENTILE`


This story from the St Peter Herald in Minnesota uses percentiles to put population growth into context


It is quite useful in reporting data stories to be able to say what percentage of values a number is above, or below. This is done with a *percentile*.

A **percentile** is a measure used to indicate where a value sits in relation to all other values. Or, as [a description on Wikipedia of percentile rank](https://en.wikipedia.org/wiki/Percentile_rank) puts it:

> "The percentile rank of a score is the percentage of scores in its frequency distribution that are the same or lower than it. For example, a test score that is greater than or equal to 75% of the scores of people taking the test is said to be at the 75th percentile rank."

In many countries, for example, babies' weights and heights will be regularly measured in comparison to all other babies to give an indication as to whether your baby is within normal ranges - and if their growth is consistent.

If your child is on the 95th percentile for height it means that they are taller than almost 95% of other children at the same age. If they are on the 10th percentile then only 10% of other children of the same age are as small as they are, or smaller. (As an aside, if you're a parent remember that some of these measures should be treated with skepticism: they can be based on surveys of child heights and weights taken many decades ago, and average heights have changed since then).

Conversely, you may want to know what value represents the '90th percentile' in any dataset to be able to report a piece of context like "90% of donations are below \$1000".

### Percentile functions


FiveThirtyEight uses percentile ranks here to compare the performance of basketball teams


The two main functions for looking at percentiles are `PERCENTILE` and `PERCENTRANK`.

One starts with the value and calculates its percentile; the other starts with a percentile and gives you a value:

- The function `PERCENTRANK` gives you the percentage of values *below* a specified value;
- The function `PERCENTILE` gives you the value which *sits at* a specified percentile.

### What percent of values are smaller? `PERCENTRANK`

Whereas `RANK` gives you the **ordinal** rank of a value (what position it comes when all values are ordered), `PERCENTRANK` tells you what percentage of values in a range are **smaller than** that value. In order to do this, it needs the same two ingredients as `RANK` - but in reverse order:

- *First*, what range ('array') of cells contains all the values; and
- Secondly, the value you want to calculate the 'percent rank' on.
- Additionally, there is a third optional parameter: the number of decimal places you want to show (known as *significance*). If you don't specify this, it will give you a result to **three decimal places**

Although three decimal places may sound like a lot, it's worth pointing out that in percentage terms that only gives you *one* decimal place: for example 1 means 100%; 0.1 means 10%, 0.01 means 1% and 0.011 means 1.1%. This will become important later.

Here's an example of a basic `PERCENTRANK` formula:

`=PERCENTRANK(A2:A10, A6)`

`A2:A10` is the range of cells containing all the values.

And `A6` is the value whose percent rank we want, in relation to those values.

If we wanted the result to just one decimal place (not a good idea, as explained above) we would add a third parameter like so:

`=PERCENTRANK(A2:A110, A6, 1)`

There are two mildly confusing aspects to `PERCENTRANK`:

1.  Firstly, it **only counts what percentage of values fall below your value**
2.  Secondly, that percentage is based on values **except the value itself**. So, for example, if your range contains 100 numbers then the percentage will be out of the 99 numbers other than your specified value.

In the example below A6 contains the number `5`, cells A2 to A5 contain numbers 1 to 4, and cells A7 to A10 contain the numbers 6 to 9. The result of the formula is `0.5`, or 50% (It doesn't matter if the numbers are in order or not).


Note that when you include text or empty cells those are ignored in the calculation


This is because four of the *other* numbers are below 5, and four are above 5. So 50% of the **other** numbers are below 5.

Actually, it is *irrelevant* how many numbers are *higher* than 5. Even if we changed all the higher numbers to be the same number - 5 - then the result of `PERCENTRANK` would be the same, because four of the eight *other* numbers are *below* 5, and that is what the function calculates.


Even if no numbers are higher than the value you specify, the calculation will still be based on those lower


That is an extreme example, but it is worth bearing in mind and checking for when you make your calculation. For example, you could use `COUNTIF` to check how many values are the same as the one you are ranking.

If want to know how many values are lower *or equal to* a specified number then you are looking for what **percentile** it falls on.

#### `PERCENTRANK` is replaced by `PERCENTRANK.EXC` and `PERCENTRANK.INC`

As with the `RANK` function, newer versions of Excel prefer you to use the more specific `PERCENTRANK.EXC` and `PERCENTRANK.INC` to `PERCENTRANK`.

`PERCENTRANK.INC` is to all intents and purposes the same as `PERCENTRANK`. The `.INC` part means '**inclusive**', and refers to the fact that results can include both 0.0 (0%) and 1.0 (100%).

In contrast, `PERCENTRANK.EXC` gives results **exclusive** of either 0 or 1.

Again, this is best illustrated with an example: if we asked for the percent rank of the number 10 in a range of numbers from 1 to 10, both `PERCENTRANK.INC` and `PERCENTRANK` would return `1`, meaning 100% of (other) values in that array are lower than that value.

`PERCENTRANK.EXC`, however, returns `0.909`. It will never return `1`.


This screenshot shows the results of three formulae: the first uses PERCENTRANK, the last uses PERCENTRANK.INC and the selected middle one uses PERCENTRANK.EXC


### What value is at the nth percentile? `PERCENTILE`


Percentiles seem to be more widely used in Indian media coverage, where education can be extremely competitive


Whereas `PERCENTRANK` takes as its starting point a particular value, `PERCENTILE` starts with the percentile you are looking for.

To do that, the `PERCENTILE` function takes two arguments:

- The array of cells you want to use as the basis for your percentile calculation;
- And the percentile you want to identify: for example `0.9` means you want to identify the value at the 90th percentile and `0.1` means 'find me the value at the 10th percentile'.

Say for example you have a spreadsheet full of payments in column N and want to work out what value would be at the 90th percentile (that is, what value 90% of payments are below or the same as). The formula would read like this:

`=PERCENTILE(N:N, 0.9)`

Similarly if you wanted to work out the value at the 99th percentile you would write it like so:

`=PERCENTILE(N:N, 0.99)`

If you use a number higher than 1 or lower than 0 you will get a `#NUM!` error.

<aside class="tip blurb">

Note that `PERCENTILE` looks at your data from smallest to largest. In situations where the 'top' results are smaller (for example faster times or lower crime rates) then you would need to adapt your percentage accordingly.

For example, if you wanted to get the 'best' 5% where 'best' means lowest, you would use `=PERCENTILE(N:N, 0.05)` to give you the value at the 5th percentile in your data. Anything below the value at that percentile (i.e. faster times, lower crime rates, fewer errors) would be the 'top 5%' in the sense of 'best'.

</aside>

#### `PERCENTILE` is replaced by `PERCENTILE.EXC` and `PERCENTILE.INC`

Once again, newer versions of Excel prefer you to use the more specific `PERCENTILE.EXC` and `PERCENTILE.INC` to `PERCENTILE`.

`PERCENTILE.INC` performs the same calculation as `PERCENTILE` - but whereas `PERCENTILE` cannot work with more than 8,191 data points (you will get a #NUM! error), `PERCENTILE.INC` can work with larger datasets.

`PERCENTILE.EXC` is much the same but will not calculate percentiles at 0 or 1 (100%) - the `.EXC` means 'exclusive' of those numbers. You will get a `#NUM!` error if you try to calculate either percentile.

### Exercise: using both sets of functions with marathon race times

[At this link you will find a spreadsheet](https://drive.google.com/file/d/0B5To6f5Yj1iJMDZGTXdSamtvT1k/view?usp=sharing) for the times of around 4,700 runners in one marathon (not all finished: some withdrew and others were disqualified). We're going to use our functions to tell the story of just how well some runners did, and what time a runner would have to make in order to finish in the top 10%.

A good habit is to always test your formula on a result you *should* be able to predict. In this case, let's test `PERCENTRANK` on the top performing runners.

The results are already sorted by finishing order (and if they weren't, we could sort them by time in ascending order anyway) so we already know who finished first: they are in row 2, and their time in cell F2.

So this formula should tell us what percentage of runners they rank above:

`=PERCENTRANK(F:F,F2)`

The result is `0.000`: this runner - the best of all - ranked above *no* other runner.

Now remember that both `PERCENTILE` and `PERCENTRANK` rank from highest to lowest. What's the highest time in our race? It's the time of the runner who finished last. What's the lowest time? That of the runner who finished quickest - and first.

For our runner in F2 what the result really means is that 0% of runners finished with a time that was *less* than this person. No runner was faster.

To get a 'ranking' of how many were *slower* we will need to subtract any result we get from 1:

`=1-PERCENTRANK(F:F,F2)`

This allows us to invert the calculation: if a runner was *slower* than 5% of other participants, then they were *faster* than 95%.

We subtract from 1 rather than 100% because they really mean the same thing: if you type `1` and then format that number as a percentage, you will get `100%`.

And of course, in this case, 1-0 is 1. In other words, 100% of runners were ranked below this one.

We can try performing the calculation on a different runner's time to get a result which is more meaningful. But there are so many runners here that those finishing second, third, fourth and fifth will all still give you results of `1` **even though 100% of runners clearly did not finish below them**. This is a problem.

Why do we get this result? It comes down to that third parameter. Remember that `PERCENTRANK` by default gives you a result to three decimal places. In practical terms that means that the highest result before 100% that you can get is `0.999` - or 99.9%. The lowest result before 0% is 0.1% (`0.001`).

Anything above 99.9%, then - for example 99.95% - will return as 1, or 100%. And anything below 0.1% - for example 0.01% - will return as 0.

To solve this, just add that third parameter to specify that you want your result to go to more than three decimal places:

`=1-PERCENTRANK(F:F,F2,5)`

You will probably need to change the formatting on the results too: if your result is still `1.00` this is because it's still only to two decimal places. Right-click on the cell and select **Format cells...** to change the decimal places on your number.

If your result looks like a time that's because the cell has inherited that formatting from the other cells. Just change the formatting to a number with enough decimal places as above.

With all that checking done we can pick a runner who is particularly noteworthy. In this case let's pretend a local celebrity (or even a reporter who took it up as a challenge) has finished in 341st position. How many other runners did he rank above?

This formula will tell us how many other runners were *faster*:

`=PERCENTRANK(F:F,F342,5)`

That is, 7.6%

And this formula will tell us how many runners the celebrity or reporter *was faster than*:

`=1-PERCENTRANK(F:F,F342,5)`

That person was faster than 92% of runners. Not bad.

> #### Further checks
>
> The second-placed runner in our data has a time which only 0.02% of other runners are lower than. Or, put another way, he is faster than 99.98% of the other runners who received a time.
>
> That 0.02% is just one runner: the winner of the marathon. Because we know that we should test that, too, to check the calculation is working correctly. The hypothesis we're testing is that 0.02% is also the result of one runner divided by all other runners who *have a finishing time*.
>
> I say how many runners *have a finishing time* because, like many calculating functions, the `PERCENTRANK` function ignores cells without numbers in them (quite right: if someone didn't finish the race and doesn't have a time, we cannot say that someone is faster or slower than them).
>
> We can count those by using the `COUNT` function: `=COUNT(F:F)` will tell us how many numbers there are in column F. But remember also that `PERCENTRANK` *excludes* the cell it is calculating a rank for. So we need to take 1 away from our result too: `=COUNT(F:F)-1`.
>
> Finally, we can calculate what percentage of runners our one winner represents by dividing that 1 person by that number of runners: `=1/(COUNT(F:F)-1)`
>
> The result in this case is `0.000222` - or 0.02%.
>
> If you were particularly eagle-eyed you may have noticed that two runners have finishing times but were disqualified and "withdrawn during the race" respectively (I'm not sure how you can be withdrawn but still finish - perhaps another lead to chase up!). You can choose to filter your data to remove these if you want.

Our other challenge was to be able to say "How well did you do in the marathon?"

Remembering again that high numbers = slow times and low numbers = time, we can start by asking: "What time would you need to be in the top 10%?" Here's the function:

`=PERCENTILE(F:F,0.1)`

This is looking for the value in column F which is at the 10th percentile: that is, where 90% of numbers are larger (slower) and 10% smaller (faster).

If your result looks like this - `0.143836806` - then you need to make sure that you're formatting that result to display as a time. Right-click on the cell and select **Format cells...** to change it to *Time*.

The time at the 10th percentile is `03:27:08`

Repeat this process for `0.2`, `0.3` and so on to get the times at each percentile you want. You could even create a little chart (or even an interactive calculator) for runners to check their performance against - remembering of course that the 20th percentile means 'You were faster than 80% of runners', and so on.

### Recap

- `RANKPERCENT` allows you to **see what percentage of numbers in a range are below a specified value**. It is useful for putting a result into context: for example, being able to say that a school performed better than 90% of others, or that only 15% of runners were quicker than you were!
- `PERCENTILE` gives you the value which *sits on* a specified percentile. It is useful for reporting key benchmarks in a story or field: for example that to finish in the top 5% of performances you would need to achieve a particular time, or to be among the 10% most profitable companies you would need to make a particular amount of money.
- `RANKPERCENT` **does not include the value itself**. So if the result is `1` that means 100% of *other* numbers are lower than that value.
- Make sure you are accurate in your language when reporting the results: e.g. "95% of *other* runners" or even "95% of other runners who completed the race"
- **A more recent version of `RANKPERCENT` is `RANKPERCENT.INC`**. This does exactly the same thing, but is distinguished from another variant, `RANKPERCENT.EXC`
- `RANKPERCENT.EXC` will calculate a rank percent, but **exclusive of the results 0 or 1**. In other words, whereas 100% or 0% of values can be below a number in a `RANKPERCENT` or `RANKPERCENT.INC` (inclusive) formula, this cannot happen with `RANKPERCENT.EXC`
- **A more recent version of `PERCENTILE` is `PERCENTILE.INC`**. This does exactly the same thing, and will also handle more cells, but is distinguished from another variant, `PERCENTILE.EXC`
- `PERCENTILE.EXC` will calculate the value at a specified percentile, but **exclusive of those at 0% or 100%**.
- `PERCENTRANK` ranks based on the biggest numbers being ranked highest, and smaller numbers being ranked lowest. If you are dealing with situations where low numbers should be ranked high (e.g. quick running times, low crime rates) then consider inverting the results by subtracting them from 100% (for example, if 5% of runners have times which are smaller numerically then that means 95% of runners take longer to finish).
- The `PERCENTRANK` functions will by default give you **results to three decimal places**. You can specify a different number of decimal places by adding that number as a third parameter.
- `PERCENTRANK` results above 99.9% (`0.999`) or below 0.1% (`0.001`) will be rounded up to 100% (`1`) or 0% (`0`). **This can be misleading** if the result is actually 0.09% or 99.95% so consider specifying more decimal places.
- A good habit is to always **test your formula on a result you *should* be able to predict**: for example the top or one of the top results.
- Watch out for results which you may want to exclude from your calculation: for example runners who are disqualified.


## Classifying data into top, middle and bottom quarters: `QUARTILE`


This map by PFEye classifies projects by contract value: you can use arbitrary values to distinguish large ones from small, or you can use quartiles


It can be very useful to categorise large ranges of data into values that are particularly high, particularly low, and those which sit around the middle.

But the challenge is often knowing where the draw the line: at what point is a number 'high', and when is it not?

[One interactive map by the investigative website PFEye](https://pfeyeblog.wordpress.com/2015/05/26/mapped-where-are-the-most-costly-pfi-contracts/), for example, looked at the use of private finance in the public sector ([you can download the raw data here by clicking File \> Download...)](https://www.google.com/fusiontables/DataSource?docid=1a5eIgg64bBjV9kFGbRyK78UQbWB0XjdbjrdX-d0L&pli=1#rows:id=1). They decided to colour code each contract on the map as follows:

> "The data is split into categories of contract value; contracts under £25m, those between £25m and £50m, schemes less than £100m, £100m to £150m and those topping £150m."


These are meaningful categories - but arbitrary: the contracts are not evenly distributed between these five categories. In fact, the contracts are distributed as follows:

- A fifth of contracts are worth £15.3m or less
- A fifth of contracts are worth between £15.3m and £27.7m
- A fifth of contracts are worth between £27.7m and £50.5m
- A fifth of contracts are worth between £50.5m and £92.6m
- And a fifth of contracts are worth over £92.6m

Comparing these with those categories chosen by the original map you can see that two of the five categories (£100-£150m and £150m and above) have been allocated to the top fifth, while in contrast the bottom two fifths of contracts are squeezed into just one of the five categories in the map (below £25m).

Is this an accurate representation of the distribution of loans?

Perhaps the large amounts skew our perception - as journalists - of the data. After all the top fifth of loans by value range from £92,600,000 to £2,687,600,000. You can understanding wanting to allocate that vast range into two categories - and it may be meaningful to do so, as long as you are aware that you are doing so.

Using quartiles - and in this case, *quintiles* (explained below) - allows you to at the very least get an accurate overview of the *distribution* of values. Beyond that, you can also use this information in your reporting (for example "the top fifth of contracts range in value from...") and to colour code or classify datapoints in maps or charts.

### Using the `QUARTILE` function

The `QUARTILE` function is a particularly quick way of finding out where to draw those lines.

Based on a range of numbers it will tell you exactly **where to draw the lines** which will separate the values in that range into four quarters:

- The bottom quarter of values (those below the 'first quartile')
- The top quarter of values (those above the 'third quartile')
- The 'lower-middle' quarter of values that sit between the first and second quartile.
- And the 'upper-middle' quarter of values that sit between the second and third quartile.

To do this it needs two ingredients:

- The range of cells containing the values that you want quartiles for
- And the quartile that you want: for example `1` for the first quartile (the value below which a quarter of values fall)

Here, for example, is the formula to calculate the first quartile in column F:

`=QUARTILE(F:F, 1)`

And here is the formula to calculate the *second* quartile in column F:

`=QUARTILE(F:F, 2)`

Some of these values can be obtained more easily with other functions. For example the result of:

`=QUARTILE(F:F, 2)`

Should be the same as this:

`=MEDIAN(F:F)`

Because the second quartile is also the point where half of values are higher, and half are lower. In other words, the median.

And the result of this:

`=QUARTILE(F:F, 4)`

Should be the same as this:

`=MAX(F:F)`

Because the value at the fourth quartile (at which four-quarters of values are below or the same) will also be the highest value.

<aside class="warning blurb">

#### The `#VALUE!` error

If you get a `#VALUE!` error it's most likely because one of the cells in your range contains an error too. If there's too much data to look for this manually, try sorting the data to bring those errors to the top - or use the `ISERROR` function to check on a cell by cell basis.

</aside>

### Applying quartile values to classify data into four quarters

Once you can calculate the quartiles you can use these as the basis for an `IF` function which classifies a number into four quarters based on whether it is above, below or between particular quartiles (see the chapter on `IF` statements if you need to know how to use these).

Here is a simple formula which just creates two classes: 'bottom quarter' or 'top three quarters':

`=IF(F2<QUARTILE(F:F,1),"Bottom quarter","Top three quarters")`

We can add a third class by nesting a further `IF` statement within this one:

`=IF(F2<QUARTILE(F:F,1),"Bottom quarter",IF(F2>QUARTILE(F:F,3),"Top quarter","Middle"))`

This tests, firstly, if cell F2 contains a value which is below the first quartile for column F and if so, puts the string of text "Bottom quarter" into this cell; then (if not), it checks if it contains a value which is above the third quartile: if it does, then the string "Top quarter" is put in this cell. If neither condition is met, it puts the string "Middle" into the cell.

If we wanted a class for all four quarters we would need a final `IF` statement like so:

`=IF(F2<QUARTILE(F:F,1),"Bottom quarter",IF(F2>QUARTILE(F:F,3),"Top quarter",IF(F2>QUARTILE(F:F,2),"Upper middle quarter","Lower middle quarter")))`

This last statement in particular can be written in all sorts of ways, of course, ruling out various possibilities in different orders.

> ### Using `PERCENTILE` to classify data using quintiles
>
> Although there is no QUINTILE function, you can use the `PERCENTILE` function to much the same effect by identifying the values at the 20th, 40th, 60th and 80th percentiles. Here, for example, is how you identify the first quintile (the 20th percentile):
>
> `=PERCENTILE(F:F,0.2)`
>
> Knowing those values you can use an `IF` statement to again classify values in terms of where they sit in five categories.
>
> And of course you can use the same principles to divide values into ten categories, or six, or however many you want. The principle to bear in mind is that the more categories you create, the more complicated things become and the less clear the story is. So keep things simple and clear wherever you can unless there's a good reason to do otherwise.

### Recap

- **A quartile is one of the values that sits at the four 'quarter points' in a series of values**: the first quartile is the value below which a quarter of values will sit; the second quartile is the value below which two quarters of values sit (and two quarters - or half - above); and the third quartile is the value below which three quarters of values sit (and a quarter above). The fourth quartile is the value which is the same or higher than four quarters of values.
- The **second quartile is the same as a median**; the fourth quartile is the same as the maximum.
- The `QUARTILE` function will **tell you a specified quartile** (first, second, third or fourth) for a range of values.
- A `QUARTILE` function **can be combined with an `IF` function to classify data into four quarters** (or two quarters and the half in the middle, or one quarter and the other three quarters).
- You can **use the `PERCENTILE` function to calculate quintiles** and other ways of dividing your values.



## Cross referencing and advanced cell references: naming cells and using `INDIRECT`, `INDEX` and `MATCH`


This story came from using MATCH and INDEX - see the case study below


So far in this book we have referenced cells using a letter-number coordinate (the letter of the column followed by the number of the row). However, there are other ways to reference cells.

In particular there are two ways of referencing cells that this chapter outlines:

1.  You can 'name' cells and use those names as a reference instead
2.  You can store a cell reference in a different cell, and refer to that in your formula. If you want to change the calculation then you only need to change that cell, not the whole formula.

### Naming cells

You can give a cell a distinctive name in Excel by clicking on the box to the left of the formula box. The formula box can be found above the main spreadsheet but below the menu bar options. The cell reference appears in a box at the same level.


You can see the cell reference box showing ‘A1’ in this example


When you click on that cell reference you will notice it shifts to the left and is now highlighted. In addition you may see a tooltip hint that tells you to "*Enter a name for a cell range, or select a named range from the list*"


When clicked on, ‘A1’ becomes highlighted and editable


Type the name you want to give to that cell and then press Enter.

For example, you could call a cell 'Paul' if you wanted to:


And then refer to that in a calculation:


Note in the cell where the formula is typed, the name of the cell is blue


Even though you have named a cell, you can still use normal cell coordinates to identify the same cell.

Note that when you type a name that has been used as a cell reference, it is coloured **blue**. If the name is *not* used for a cell on that sheet, it will *not* be coloured blue.

If you try to use a name which is not used for a cell on that sheet, you will also get a `#NAME?` error when you press Enter.


Because Karen is not the name of any cell, it is coloured black


You can name cell *ranges* as well as individual cells. To do this, just select the range of cells first, and then proceed exactly as you would when naming one cell (clicking on the cell reference box and typing your chosen name).

That range can then be used as you would any range of cells. For example if you named a range of cells `familyages` you could use that range in `=SUM(familyages)` or `=MEDIAN(familyages)`, and so on.

### `INDIRECT`

The `INDIRECT` function allows you to reference a cell 'indirectly' or to *generate* a cell reference based on another value. For example, if you had a column containing cell references, or a partial cell reference (such as rank), then `INDIRECT` would allow you to turn that into a cell reference.

The simplest example of this would be this:

- In cell A1 you type the following characters: `A2`
- In cell A2 you type `"Hello"`
- In cell B1 you type `=INDIRECT(A1)`

Now, that formula looks in cell A1, sees the cell reference `A2`, and then looks there, where it finds the string `"Hello"`.


The formula here looks in A1 for a cell reference, then grabs the contents of the referenced cell instead


If you simply typed `=A1` you would get the result `A2` - *not* the contents of cell A2. In other words, `INDIRECT` treats the string of characters `A2` as a reference. Without that function it simply treats `A2` as two characters with no particular meaning.


If you have named cells (as explained above) then you can use those names too. The string of characters `paul` in this situation would be treated by `INDIRECT` as a reference to a cell somewhere named `paul`.


In this example cell A1 has been named ‘paul’ and the formula references that instead


`INDIRECT` can also generate a cell reference by grabbing values from more than one cell, like so:

`=INDIRECT(A1&B1)`

If cell A1 contained the character `A` and cell B1 contained the character `2` then the formula above would look for something in cell `A2`.


Likewise you could provide part of the cell reference yourself like so:

`=INDIRECT(A1&2)`

If cell A1 again contained the character `A` then that would be combined with the digit `2` and the formula would look for something in cell `A2`.


Similarly you can generate a cell reference by performing calculations - and this is where `INDIRECT` proves most useful, as I'll come onto in a moment.

Here for example:

`=INDIRECT("A"&B1+1)`

Now this generates a cell reference in column A by taking whatever number is in cell B1 and adding 1. If cell B1 contains the number `10` then the result is A11 (character `A` and 10+1).

<aside class="warning blurb">

Note that you must put the column letter in quotation marks!

</aside>


In this example B1 contains the number 2 but the formula adds 1 to that, so the final result references cell A3


Why is this useful..?

### Cross-referencing cells based on values in other cells

The most obvious application of this is where you can use a value in one cell to find a value in another. Examples here might include rankings or numerical codes which, when ranked in order, can be referenced accordingly.

Here, for example, we have a small list of crimes which are only identified by a numerical code - plus a small table listing what those codes mean, ranked in code order:


We can use the `INDIRECT` function to formulate a cell reference based on each code:


Note that we add 1 to the code number because they don't begin until row 2 (1 is in row 2, 2 is in row 3 and so on).

Of course this is a very simple example: the codes might begin with 1001, for example, in which case we would have to subtract 999 from each number (1001-999 would get you 2, for row 2)

We would also have to make sure that the codes did not have any gaps (if the codes ran from 1 to 100, for example, we would have to make sure that none of those numbers were missing from the list. We can always generate a complete list using the techniques detailed elsewhere in this book).

Of course you can achieve the same results as this example using `VLOOKUP`. But you get the idea.

### `INDEX`

The `INDEX` function returns data from a specified range of cells based on its position *within those cells*. It is particularly useful when you need to use a rank or category to locate related data (if the rank is 3 we might want what is in the third cell of a particular range of cells).

For example, we know that A2 is the *first* column and the *second* row in the spreadsheet as a whole. But what if we wanted the first column and second row from a table that is somewhere else on a spreadsheet?

That's what `INDEX` allows us to grab.

Here's an example:

`=INDEX(A2:D35, 2, 1)`

This formula will go to the range *A2:D35* and grab the contents of the second row and first column *in that range* (in other words, B2)

The `INDEX` function normally needs three ingredients:

- The array of cells you want to look in;
- The row *within that array* and...
- The column *within that array* you want to grab.

You specify both the row and column with an *index*: in other words a number indicating the position of the row or column within that array of cells: `1` for the first row or column in that array; `2` for the second and so on.

So, `=INDEX(B2:D35, 1, 2)` uses `1` to indicate the *first row* in the array `B2:D35` (that is row 2 in the spreadsheet as a whole) and `2` to indicate the *second column* in the array `B2:D35` (that is column C in the spreadsheet as a whole).

<aside class="warning blurb">

If you get a `#REF!` error from your formula, check that you have entered both a row *and* a column index in your formula, separated by commas. If that's not the cause, check that you're not looking for a reference *outside* of the range: for example specifying row 3 when your range only has two rows.

</aside>

#### Just looking in one row, or one column

If your array (range of cells) only takes up one row, or one column, then you only need *one* index. For example:

`=INDEX(E1:G1,2)`

In this example our array only occupies one row (row 1) so the `2` is interpreted as meaning 'column 2 in this single row array'. Column 2 in the array E1:G1 is F1.

Likewise if we specify an array with only one *column*:

`=INDEX(F2:F4,3)`

In this example the `3` is interpreted as meaning 'row 2 in this single column array'. Row 2 in the array F2:F4 is F3.

#### Looking in more than one place: multiple arrays

You can use the `INDEX` function to look across multiple arrays, or grab more than one cell. This is sometimes called an *INDEX reference function* or *reference syntax*.

Say we have two tables:

- The first table, in cell range A1:B10, shows crime figures of a type we'll call 'type 1'
- A second table, in cell range D1:D20, shows crime figures of a type we'll call 'type 2'

We can use one `INDEX` function to grab details from either like so:

`=INDEX((A1:B10,D1:D20),1,1,2)`

Firstly, note that **the list of arrays is placed inside its own parentheses**, and separated with commas like so:

`(A1:B10,D1:D20)`

This is then followed by a comma, and the other three ingredients:

- The index of the row in that array that you want to grab from (`1`)
- The index of the column in that array that you want to grab from (also `1`)
- And **which array** in your list you want to look in (in this case, `2`)

That `2` means that this formula will look inside the array `D1:D20`, the *second* array in the list at the start of the formula.

The cell in the first row and first column of that array, then, would be D1.

If we changed that `2` to `1` it would look instead at the cell in the first row and first column of the *first* array specified: `A1:B10`. That would be A1.

Of course rather than type `1` or `2` directly into our formula, we will be more likely to reference another cell specifying crime type in our formula.

#### Grabbing more than one value to perform calculations

The same syntax can be used to grab a *series* of values by using a *zero* index like so:

`=INDEX(F2:H3,2,0)`

This formula means *go to the cell range F2:H3, find the second row in that range, and then grab all the values in that range*.

If you wanted to grab all the values in one *column* in that range, you would use a zero index for the row parameter instead like so:

`=INDEX(F2:H3,0,2)`

Type either formula, however and it *will not work*. Specifically, it will generate a `#VALUE!` error.

This is because it cannot show all the values in one cell. Instead, you will need to *nest* a formula like this inside another in order to *do something* with those valuations: for example, add them up using `SUM`, calculate an average, and so on. Here are some examples:

`=SUM(INDEX(F2:H3,2,0))`

`=AVERAGE(INDEX(F2:H3,2,0))`

`=COUNT(INDEX(F2:H3,2,0))`

### Working out which index to grab: `MATCH`

The final function in this chapter is ideal for using with either `INDEX` or `INDIRECT`: the `MATCH` function will find out what position a specified value is situated at. In other words, it will find its *index*.

Here's a very simple example to illustrate: say we put the numbers 1 to 10, in order, from cells A1 down to cell A10, so that cell A1 contained '1' and A10 contained '10'.

This formula would tell you what position '5' was in that range:

`=MATCH(5, A1:A10, 0)`

...and because '5' would be the fifth cell in that range, the result would also be `5`.

But if '5' was in the last cell, the result would be `10`; if it was in the first (A1) it would be `1`, and so on.

The `MATCH` function needs three ingredients:

- The value you are looking for (this can be either a number or a string. If you're looking for a string it needs to be in quotation marks like so: `"Angus"`)
- The array, or range, of cells you are looking for it in
- How exact a match you want.

This last argument can be one of three values:

- `0` means you only want the formula to work if there is an exact match. If it does not find an exact match it will return `#N/A`
- `1` means you want it to find the closest match that is the same *or less than* your value. For example in the formula `=MATCH(100, A1:A10, 1)` if that array contained the figures 99 and 101, you would get `99`
- `-1` means you want it to find the closest match that is the same *or more than* your value. For example in the formula `=MATCH(100, A1:A10, -1)` if that array contained the figures 99 and 101, you would get `101`

Most of the time you will specify `0`.

The key use case for `MATCH` is when you can use that position to find something else out. For example if the match is in the third cell in a range, and you can then look for the third label in another range that relates to that.

Of course you can also use `VLOOKUP` and `HLOOKUP` in similar ways, but those functions require the looked-for value to be in the first column or row of your array. For this reason, sometimes `MATCH` is more relevant.

> #### Case study: Patrick Scott, Trinity Mirror Data Unit
>
> Data journalist Patrick Scott used `INDEX` and `MATCH` as part of a [story on children going to schools outside of their local area](http://www.getwestlondon.co.uk/news/west-london-news/one-10-london-children-travel-9464965) (see the image at the top of this chapter).
>
> > "Essentially we knew that a child was *most* likely to go to a school in the local authority in which they live," he explains. "So we wanted to know what the *second most popular* local authority was.
>
> > "To do this manually would take forever: we'd have to look across 200-ish columns for each of the 200-ish rows."
>
> Instead, Patrick used the `LARGE` function to find the second biggest number, combined it with `MATCH` to identify which column that was in, and then used *that* with `INDEX` to grab the authority at the same position.
>
> The final formula looked like this:
>
> `=INDEX($F$1:$FA$1,MATCH(LARGE(F3:FA3,2),F3:FA3,0))`
>
> The formula makes more sense when you break it down by each stage (remember that you can do each stage in a different column if you find that easier). Here is the same formula broken into three different stages:
>
> `LARGE(F3:FA3,2)`
>
> This is the first stage: working out what is the second largest number in the cell range F3:FA3.
>
> That is then used as the first ingredient in the `MATCH` formula:
>
> `MATCH(LARGE(F3:FA3,2),F3:FA3,0)`
>
> This formula looks for that number (the second largest remember) in the same range (F3:FA3), specifying that it only wants an exact match (`0`).
>
> The result should be an index showing what position that number sits at. For example, the third cell in that range, or `3`.
>
> Finally, in the full formula we began with, the `INDEX` function is used to look for the value in the third cell in a different range: row 1 containing the headings, from column F onwards: `$F$1:$FA$1`
>
> The dollar signs are used to fix this cell reference so that when the formula is copied down it doesn't change.

### Exercise: Finding where schoolchildren go outside their area

See if you can replicate Patrick Scott's work on schools data to identify which area schoolchildren go to school outside their own.

You can find the data at the Department for Education's release on [Schools, pupils and their characteristics](https://www.gov.uk/government/statistics/schools-pupils-and-their-characteristics-january-2015). There are a number of documents linked from this page: you will need to download the 'Cross-border movement matrix tables: SFR16/2015'.

It is quite an intimidating dataset: down the left are around 150 different areas in England, and across the top the same areas are listed again in the same number of columns.


You should be able to use the same formula as Patrick to find the second highest number in each row, and then identify what position that sits in, before grabbing the name of the authority that the position corresponds with.

Make sure you check your results to ensure that the positions match (that is, you are not grabbing the name of the authority next to the one you actually need).

Try adapting your formula so that you can find the *third* most popular area for each local authority.

### Recap

- **There is more than one way of referencing a cell in a spreadsheet**. You can use a cell reference like `A2`; you can 'name' cells and use those names as a reference instead; you can store a cell reference in a different cell, and refer to that in your formula. Or you can 'formulate' or 'calculate' a cell reference using functions like `INDIRECT` or look within specific arrays using `INDEX`.
- To give a cell (or a range of cells) a name in Excel **click on the cell's reference** when it is shown in the box to the left of the formula box above the spreadsheet itself.
- Sometimes you need to grab information from a spreadsheet based on other information, such as the position of another value, or a combination of other bits of information. In this situation `MATCH` can be useful for finding that information, and `INDIRECT` or `INDEX` can be useful for using it to grab the right cell.
- The `INDIRECT` function allows you to **indirectly reference a cell based on values elsewhere in a spreadsheet**.
- The `INDEX` function allows you to **reference a cell based on its position** within a specified array of cells, or more than one array of cells.
- The `INDEX` function also allows you to **grab the values from more than one cell** - but this must be used as part of a formula which calculates something using those values, such as a `SUM`, `AVERAGE` or `COUNT`.
- The `MATCH` function allows you to **find out the index of a value** (or the value closest to it) in a specified range of cells.
- You can specify that you want an exact match, or the value which is closest to or less than, or closest to or more than, a particular value.


## Getting statistical: correlation with `CORREL` and other ways of testing data


My personal favourite from Spurious Correlations


***"Correlation does not mean causation."*** This is the mantra of the data journalist. Just because two things both go up at the same time, it does not mean that one causes another, however straightforward it may seem.

In fact there's [a whole site dedicated to spurious correlations: tylervigen.com](http://www.tylervigen.com), which is well worth browsing both for an illustration of how easily it is done - and just for a good laugh.

I start this chapter with that mantra because as soon as you begin to work with statistical functions in Excel you begin to enter a whole new world which offers both new power and new responsibility.

The power that these functions give you is the ability to better hold others' data and claims to account. But the responsibility is to be careful what claims you make yourself. Science is not the same as journalism.

### How strong is the relationship between two columns of numbers?


This article finds a .76 correlation between the share of the vote a state gave to Obama and its ratio of female-to-male earnings


The `CORREL` function indicates how strong a relationship there is between two sets of numbers: what is called the **correlation coefficient**.

For example, if your first set of numbers was:

> `1, 2, 3, 4, 5, 6, 7, 8`

...and your second set of numbers was:

> `10, 20, 30, 40, 50, 60, 70, 80`

...then there would be a direct relationship between those two sets: each number in series 2 is ten times the number in the same position in series 1.

This would be represented by the correlation coefficient `1` (often expressed in statistics as `+1`).

The relationship does not have to be so obvious as that. If your second set of numbers was:

> `5, 20, 35, 50, 65, 80, 95, 110`

...then the correlation coefficient would *also* be `1`: this is because as each number in series 1 increases by 1, each number in series 2 increases by 15.

In both the examples above, as one set of numbers increases, the other does too. This is known as a **positive correlation**. But the relationship can also be a negative one.

For example, if your first set of numbers was:

> `1, 2, 3, 4, 5, 6, 7, 8`

...and your second set of numbers was:

> `99, 98, 97, 96, 95, 94, 93, 92`

...then the correlation coefficient would be `-1`.

A correlation of either -1 or +1 is called a **perfect correlation**. Needless to say this sort of correlation is very unlikely.

Most of the time you will get a correlation coefficient anywhere between -0.99 and +0.99.

But at what point does a correlation become meaningful? The answer is: it doesn't; it's the wrong question. Correlation has no *meaning*, only significance.

So:

- A **strong** correlation would be one above 0.8 or below -0.8;
- A **weak** correlation would be one below 0.5 and above -0.5

In *[What Analytics Can Teach Us About the Beautiful Game](https://fivethirtyeight.com/features/what-analytics-can-teach-us-about-the-beautiful-game/)*, for example, Neil Paine notes that:

> "As for the long ball, it's proven futile in today's game. During the 2013-14 English Premier League season, the percentage of a team's passes classified as "long" by Whoscored.com's data was very negatively correlated with how many goals it scored."

A [footnote to the article](https://fivethirtyeight.com/features/what-analytics-can-teach-us-about-the-beautiful-game/#fn-4) notes that the correlation coefficient was -0.8, just on the borderline of a strong negative correlation.

<aside class="tip blurb">

If you want to have a bit of fun with this, while improving your understanding of correlation, try the 'Guess the Correlation' game at [guessthecorrelation.com](http://guessthecorrelation.com/).


Guess the Correlation. Can you beat my high score?


</aside>

### Using the `CORREL` function

The `CORREL` function needs *two* arguments: the array of cells containing your first set of values; and the array containing the second set. Here's an example:

> `=CORREL(A2:A9, B2:B9)`

**Each array must have the same number of cells**. If they don't, you will get an `#N/A` error.

Not all the values in your cells need to be numbers. If your second set of data in the previous example was this:

> `99, 98, NO DATA, 96, 95, NO DATA, 93, 92`

...then you will not get an error. The same is the case if you had empty cells: the key test is does the *formula* refer to the same number of cells in each array. For example this formula:

> `=CORREL(A2:A9, B2:B8)`

...is trying to compare a first array of 8 cells with a second array of 7 cells. That won't work.

### Once you have a result


Chart from the article Should Travelers Avoid Flying Airlines That Have Had Crashes in the Past?


If you find a strong correlation between two sets of numbers there may be a relationship, or there may not be.

The data journalism site FiveThirtyEight illustrates this beautifully with [one article that allows you to find correlations that suggest that the U.S. economy is affected by whether Republicans or Democrats are in office](https://fivethirtyeight.com/features/science-isnt-broken/#part2). There are enough elements for you to find correlations that favour either party.


This FiveThirtyEight interactive allows you to correlate different variables


This is sometimes called the **multiple comparisons problem**: [the more variables you can look at, the more likely it is that you find a correlation between any two of them](http://www.graphpad.com/guides/prism/6/statistics/index.htm?beware_of_multiple_comparisons.htm).

This problem is particularly compounded by the rise of **big data**: large datasets with lots of different variables. In some ways, 'Spurious Correlations', the site I opened this chapter with, is one example of that: taking lots of different variables and producing ridiculous correlations.

So in many ways for journalists a weak correlation is more useful than a strong one: it can help rule out a potential avenue of enquiry, while a strong correlation proves nothing.

In the article *[Should Travelers Avoid Flying Airlines That Have Had Crashes in the Past?](https://fivethirtyeight.com/features/should-travelers-avoid-flying-airlines-that-have-had-crashes-in-the-past/)*, for example (shown above), Nate Silver uses correlation to explore whether there is any relationship between airlines and accidents, and suggest that there isn't.

Correlation also helps with **factchecking**: if a politician or other public figure is bandying around the phrase 'strong correlation' then you can confidently say "There is no strong correlation".

### Recap

- The `CORREL` function allows you to find out the **correlation coefficient** of two sets of numbers: in other words, how strong a relationship there is between the two sets of numbers.
- The `CORREL` function needs **two arguments: two sets of numbers** (normally represented by cell range references) which you want to obtain the correlation coefficient for.
- Those two cell ranges **must contain the same number of cells**, or the formula will generate an error. It does not matter if some cells are blank or contain text.
- Correlation is represented in the result of the `CORREL` formula as a number on **a scale from -1 to +1**.
- You can have a **positive correlation (indicated by a figure above zero) or a negative correlation (indicated by a figure below zero)**: in a positive correlation both sets of numbers get larger at the same time; in a negative correlation one set gets larger as the other gets smaller.
- A correlation of either -1 or +1 is called a **perfect correlation**.
- It is very unlikely that you would have a complete absence of correlation (`0`). But **anything between -0.5 and +0.5 is still considered weak correlation**.
- A **strong correlation would be one above 0.8 or below -0.8**.
- Always remember that **correlation is not causation**, and there are hundreds of examples of figures with a strong correlation where there is no relationship at all. If you establish a strong correlation that does not prove anything: explore the issue further with statistical experts or specialist academics in the field you are looking at.

### Try it out

In late 2015 the Daily Mail [reported](http://www.dailymail.co.uk/news/article-3326389/Police-stop-searches-40.html) on a 40% drop in the use of stop and search by police. Police chiefs were quoted in the article blaming the reduction for a rise in knife crime.


Try to find data on both stop and search and knife crime. Can you find evidence of any correlation between the two? Is it strong, weak, or is there no correlation at all?

Find academics who have already researched this issue, and read what they have written, including their methods. If you're writing an article about this, give them a call to find out what advice they would give you.



## The final chapter: next steps

Over the course of this book we have covered a wide range of techniques that come in useful at every stage of the data journalism process: getting data in the first place; shaping it into an 'accommodating' state when it comes to answering questions; spotting interesting data points in spreadsheets; checking for errors; and telling the resulting story.

From `IMPORT` functions and methods of splitting and combining data, to formulae that add up, average, classify, rank, correlate and convert data, you should now have a varied toolkit that allows you to deal with a range of situations and questions - and, against a deadline, at speed.

<aside>

Of course there are dozens of functions we haven't covered in this book. Some have mathematical uses which are unlikely to come in useful in journalism (trigonometry, for example), and some are just plain esoteric (like `ARABIC`, which converts a roman numeral into a number).

But you never know when one might come in handy, so if you do come across a problem it is sometimes worth looking at [Excel's list of functions](https://support.office.com/en-us/article/Excel-functions-alphabetical-b3944572-255d-4efb-bb96-c6d90033e188) and searching for key words which relate to your challenge.

</aside>

Aside from the functions, however, I hope you have been inspired by the examples throughout the book to spot all sorts of potential stories in datasets that pass most journalists by.

Perhaps more importantly, you should have a broader understanding of the workings of spreadsheets and what is called '*computational thinking*': the ability to break down a problem into logical steps, which can then be addressed through programming. Because ultimately functions and formulae *are* programming. It is not about memorising formulae and being able to reproduce them on demand, but rather to know what is possible and be able to access examples.

One of the most basic steps in computational thinking is simply the ability to identify your problem and search effectively for solutions: adding the terms 'Excel' and 'function' to your problem in Google can be surprisingly effective.

Often, however, there will be more than one problem that you need to solve, and more than one function to find for that. And in those cases computational thinking is about connecting those steps together in a logical order.

I will give you a particularly convoluted example from a story I worked on. In response to an FOI request we had been sent a spreadsheet with a column showing amounts and descriptions together, such as "10 bottles of alcohol". We wanted to extract the number and the description into two separate columns so we could count them.

Breaking the problems down using computational thinking, we might come up with something like this (remembering that there is always more than one way to solve a problem):

1.  Find the first space in that cell
2.  Grab the characters before that space
3.  Test if it is a number
4.  If it is, grab everything before that first space and put in one cell
5.  And put everything after that first space and put in another cell
6.  If it is not, classify it for follow up treatment

Each of those problems can then be tackled separately:

1.  Finding a space can be done using the `SEARCH` function.
2.  Grabbing characters up to a specified position can be done using `LEFT`
3.  Testing can be done using `IF` and looking for a number can be done using `ISNUMBER` (but after testing this out you'd realise you also need `INT` to convert text into a number first),
4.  Grabbing characters from a middle position can be done using `MID`, or we can use `RIGHT` with `LEN` to grab from the end to that position.

The formula would build, then, something like this, with each formula being *nested* within the next one:

1.  `=SEARCH(" ", B2)`
2.  `=LEFT(B2,(SEARCH(" ",B2)-1))`
3.  `=INT(LEFT(B2,(SEARCH(" ",B2)-1)))`
4.  `=ISNUMBER(INT(LEFT(B2,(SEARCH(" ",B2)-1))))`
5.  `=IF(ISNUMBER(INT(LEFT(B2,(SEARCH(" ",B2)-1)))), INT(LEFT(B2,(SEARCH(" ",B2)-1))), "NOT A NUMBER")`

This is just an extreme example for demonstration purposes. The point is about that logical process.

### What else can Excel do? Add-ins, templates and VBA

This has been a pretty big book, but there is still a lot more that Excel can do if you want to dig deeper.

In particular, you can use **Add-ins** or templates to add extra functionality to Excel; and you can create your own functionality using **VBA**.

Add-ins are collections of extra functionality. Typically each add-in is designed to tackle a particular collection of common problems, such as advanced or bulk statistical analysis; dealing with large datasets; different visualisation techniques; and add-ins that allow you to access specific datasets. There are also some that allow you to use Excel in particular business areas such as investment, productivity, scheduling and even SEO.

Some add-ins are produced by Microsoft. You might ask why these don't come pre-installed with Excel: well, if all of these were included by default it would make Excel - already a very large piece of software - even bigger and slower. The other advantage of add-ins is that they can be made *after* a version of Excel is released, and added in later.

Perhaps the best known add-in is the **Analysis ToolPak**. This provides additional functionality around statistical analysis such as Anova (**An**alysis **o**f **v**ariance **a**nalysis), regressions, histograms and t-tests. It also has a 'descriptive statistics' tool which provides an overview of various statistical dimensions of your dataset.

This can be [loaded directly from Excel itself if you have the PC version](https://support.office.com/en-us/article/Load-the-Analysis-ToolPak-6a63e598-cd6d-42e3-9317-6b40ba1a66b4?CorrelationId=9b17511a-f8a8-4046-a5af-28eac0dfe360&ui=en-US&rs=en-US&ad=US) or the 2016 Mac version of Excel; for earlier Mac versions you'll [need to download third party versions](https://support.microsoft.com/en-us/kb/2431349) such as [StatPlus:mac LE](http://www.analystsoft.com/en/products/statplusmacle/).

You can also find a useful overview of the functionality at [this post by Jonathan Frayman](http://www.interhacktives.com/2015/02/17/use-statistical-functions-excel/)

#### Specialist datasets

Some add-ins bring in particular datasets: the [Quandl add-in](https://www.quandl.com/help/excel), for example, allows you to "search through, find and download any of Quandl's millions of datasets directly from within Microsoft Excel". The Federal Reserve Bank of St. Louis offers its own add-in called [FRED](https://research.stlouisfed.org/fred-addin/), as [does the U.S. Energy Information Administration (EIA)](https://www.eia.gov/todayinenergy/detail.cfm?id=20412)

#### Big datasets

Another popular add-in is **Power Pivot**: this allows you to work with particularly big datasets by using a compression algorithm. [According to the capacity specification](https://msdn.microsoft.com/en-us/library/gg413465(v=sql.110).aspx) Power Pivot allows you to handle up to around 2 million rows *and* columns: this compares to a limit of 16,386 columns by 1,048,576 rows in Excel 2013.

As you might guess, Power Pivot allows you to create **pivot tables** with those large datasets, but it also adds increased VLOOKUP powers.

Once again if you're a Mac user you won't find it easy to use Power Pivot: it has been [included in the 2016 version of Excel for Mac](http://www.theregister.co.uk/2015/03/06/whats_new_in_office_2016_for_the_mac/), but there have been [problems reported with Office 2016 and the El Capitan OS](http://www.macrumors.com/2015/10/05/microsoft-office-2016-el-capitan-bugs/).

There are of course other ways to handle big datasets: if you have to do this regularly then it is worth exploring R or SQL.

**R** is a programming language which is used to query datasets, typically using the free software **R Studio**. You can find lots of tutorials and communities online: R Bloggers [has a good list of where to start](http://www.r-bloggers.com/how-to-learn-r-2/)

**SQL** stands for Structured Query Language. This has been around for decades and is also well supported with tutorials and tools. Ignore the expensive software options when it comes to SQL: you can find lots of free and open source software for running SQL queries on data, including [SQLite](https://www.sqlite.org/) and [PostgreSQL](http://www.postgresql.org/). The Firefox plugin [SQLite Manager](https://addons.mozilla.org/en-GB/firefox/addon/sqlite-manager/) is a good way to get started: it allows you to turn Firefox into a SQL database; and if you like mapping you can also [learn SQL by running queries in the mapping tool CartoDB](http://academy.cartodb.com/courses/sql-postgis/intro-to-sql-and-postgis/). See the chapter on the `QUERY` function for more on SQL queries.

#### Visualisation add ins


Add ins that provide extra visualisation functionality include the [Radial Bar Chart add-in](https://store.office.com/radial-bar-chart-WA103857593.aspx?assetid=WA103857593&sourcecorrid=e37f7e9a-cf40-499d-904e-8792dfe40ada&searchapppos=0), [Geographic Heat Map](Geographic%20Heat%20Map) and [Histogram 2D](Histogram%202D).


You can create bubble charts using the [Bubbles add-in](https://store.office.com/bubbles-WA103147117.aspx?assetid=WA103147117&sourcecorrid=f3684a9d-3a54-458d-bc49-8ec416e7af6c&searchapppos=0) and gauges using the [Gauge add-in](https://store.office.com/gauge-WA103524919.aspx?assetid=WA103524919&sourcecorrid=7bc634f1-c0ce-4970-bf40-8027e253e966&searchapppos=1).

If there are other charts you'd like to create in Excel try searching for that type in the [Office Store](https://store.office.com/appshome.aspx). Some are free while others come with a small cost, like an app.

#### Templates


Another area to explore if you're looking for additional functionality in Excel is **templates**: these are essential spreadsheets that have already been created by other people which already have formulae or other elements included, and which address tasks or challenges that are shared by others. Basic examples featured on the [Microsoft Office templates directory](https://templates.office.com/en-us/templates-for-Excel) include loan calculators, planners for gifts or trips, schedulers and expense trackers.

#### NodeXL: Network graphs

One particular template-cum-add-in worth mentioning is **NodeXL**: this is a hugely useful tool if you want to generate network graphs showing relationships between different entities in a dataset.

A very simple network graph is used to show the team behind NodeXL on the [official website](https://nodexl.codeplex.com/)


But you will find more complex examples used in journalism to show 'who knows who', to map the connections between corporations, individuals, and government - or indeed the lack of connections: I, Scientist used network analysis to [show how US lawmakers "don't work together anymore"](http://iscientist.co.uk/2015/05/us-lawmakers-dont-work-together-anymore/), including an animated gif of the networks changing over time.


Mauro Martino’s network analysis from I, Scientist


The Reuters project Connected China used it as a way to explore power networks in that country while BBC's Newsnight programme used it to look at Twitter conversation behaviour in the run up to a general election. You can watch a promo video of the Reuters project at [https://www.youtube .com/watch?v=tCnhMVVK4kI](https://www.youtube.com/watch?v=tCnhMVVK4kI) and a video of Newsnight at <https://www.youtube.com/watch?v=5A9c6Yyw47k>.

It has even been used just to flesh out fictional worlds. Andrew J. Beveridge and Jie Shan, for example, used network graphs to visualise the connections and importance of characters in the TV series *Game of Thrones*, while Vadim Makarenko and Aleksander Derylo used similar techniques to create an [explorable interactive of the relationships between James Bond films and brands](http://biqdata.wyborcza.pl/the-interactive-map-of-james-bond).


Image by Andrew J. Beveridge and Jie Shan


#### Excel VBA (Visual Basic for Applications)

As well as downloading add-ins made by others, you can write your own scripts for particular problems or processes.

**Excel VBA** (Visual Basic for Applications) is the name of the programming language of Excel that you can do this in.

The website Excel Easy [lists 16 different things you can do with VBA](http://www.excel-easy.com/vba.html), with tutorials for each. These range from creating **macros** and automatically changing text, to displaying instructions to users and creating interfaces (such as forms or drop-down menus).

A **macro** is basically a set of instructions: if you are having to perform a series of actions more than once then macros can save you a lot of time by automating that. Examples include:

- Fetching data from a particular source (and anything you have to do to that, such as transposing or converting)
- 'Find and replace'-type text manipulation tasks
- Conversion tasks like converting currency or dates from one system to another
- Checking for triggers or conditions ('if' statements) that then mean you have to perform a series of actions (which can then be included in the macro)

You may be intimidated by macros at first - you will be looking at raw code - but it is important to remember that *you don't have to write code from scratch*: most of the time you will be able to find example macros that you can copy or adapt from tutorials or resources.

This is perfectly fine and indeed the way most people learn programming. A good path goes like this:

1.  Follow a tutorial where you copy and paste a macro, then test it works.
2.  Try to understand what one part of that macro is doing, then change that part so it does something slightly different (for example, affects a different cell or range; or makes a slightly different change).
3.  Read around VBA so that you understand one part of it (such as variables, or loops) and play with that.
4.  Repeat the process above with different parts of macros, different tutorials, and different parts of VBA, as you steadily expand your knowledge.

It is always useful to start with a problem which applies to **you**, rather than learning processes which have no relevance. This will make you more motivated, and more likely to remember the process.

### Tell me your problems

Because this is an ebook created using Leanpub it is possible for me to add updates and corrections, and as with [my other books](https://leanpub.com/u/paulbradshaw) that is very much my plan.

If you have bought this on Leanpub please make sure you are subscribed to receive notifications of new additions to the book and download the most up to date version.

As I bring this book to a close, I also want to encourage you to **get in touch** if you have a problem which it does not solve. It is one of the most enjoyable aspects of writing and teaching to find a new problem to solve, and help someone solve it!

Even better, if you have worked on a story using these techniques please do let me know about it. It's great to see them being put into practice, and I'm always keen to include extra examples in the book.

You can [find me on Twitter \@paulbradshaw](https://twitter.com/paulbradshaw/) and other contact details are [listed on my blog](http://onlinejournalismblog.com/), where I often publish data journalism tools and tips. I'll see you there!
