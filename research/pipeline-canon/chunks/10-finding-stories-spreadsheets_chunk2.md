<!-- chunk: 2/3 | source: 10-finding-stories-spreadsheets.md | words: 38263 -->
<!-- headings: What day did that date fall on? Which year was the worst? Extracting days, months and years from full dates; Extracting dates, months and years: DAY, MONTH and YEAR; Extracting days and months as words or years as '66, '94 etc: TEXT; Which day of the week? The `WEEKDAY` function; Month and year combinations; Using the Format Cells 'Custom' option to do the same thing to existing dates; Hours and minutes: HOUR, MINUTE, SECOND and TEXT again; Grabbing times of day and storing them as numbers using `TIMEVALUE` or `TIME`; When things don't go as you expect them to: dealing with errors in date functions; Recap; Finding the story: which outlets have consistently bad scores?; Find the story: what years and months are worst for hygiene inspections?; How old is someone? Ages and using `TODAY`'s date; Breaking down the problem; Calculating the years; Checking whether a birthday comes before or after a date; Making an adjustment based on the results; Using `TODAY` to calculate an age against today's date; Working things out to the hour or minute: `NOW`; Making it easy to understand: breaking the formula back up -->

## What day did that date fall on? Which year was the worst? Extracting days, months and years from full dates


This story from Ampp3d identifies the ‘worst’ years in one particular dataset


Dates are enormously useful bits of data. They can help us to find stories about peaks and troughs: whether things are getting better or worse; what times of the year or week are or were best or worst for a particular event - whether that event is a crime, or an extreme bit of weather.

But if you only have *dates* and you want to look more widely than *daily* trends you'll hit a problem: aggregating data by year or month is not as straightforward as you might expect. And trying to work out anything based on days of the week is another challenge altogether.

This is because, as mentioned previously, dates are not stored as a series of characters such as "11/11/14" but rather as a number: the number of days since January 1st 1900 (or in some cases, 1901).

So we can't simply ask "How many times does 'September' appear?" or "Which day of the week appears most often?" of a list of numbers like '41954'. Pivot tables will give us a different row for every date.

Instead, we need to *extract* the month, day or year from *each* date in turn - typically to create a new column whose values we can then count.

### Extracting dates, months and years: DAY, MONTH and YEAR

The functions `DAY`, `MONTH` and `YEAR` are designed for this purpose. Try the following:

- Open an empty spreadsheet and type a date in the first cell, A1 - for example '11/12/2013'.
- In cell B1 type the formula `=YEAR(A1)`.
- In cell C1 type the formula `=MONTH(A1)`.
- In cell D1 type the formula `=DAY(A1)`.

Each of those formulae should give you a number corresponding to the year, month, or day in the date it uses.

<aside class="warning blurb">

Make sure you know whether the dates use UK or US date formatting - and that the formulae are interpreting them correctly. UK dates use day/month/year; US dating uses month/day/year. Excel should format dates [based on your computer's region settings](http://excelsemipro.com/2011/06/regional-date-formats-in-excel/), but in some cases the creator of the spreadsheet may have formatted dates in a way which prevents this.

</aside>

This is very useful - but what if you don't want a number? What if you want that day or month as a word? Here we'll need a slightly more powerful function.

### Extracting days and months as words or years as '66, '94 etc: TEXT

The `TEXT` function allows you to grab the day, month or year *in a format you dictate*. For example, whereas `=DAY(A1)` would grab `11` for the date `11/12/2013`, what if you wanted it to say `Wednesday` or `Wed`? What if you wanted to grab `December` or `Dec`? What if you wanted to grab `13` rather than `2013`?

In order to allow you to specify this, `TEXT` has two parameters: the cell you want to work from, and the format of the date information you want to extract.

This format is expressed as a series of characters. For example, if you wanted the month you would use the series of characters `"MMMM"`; if you wanted the month as a three-character expression (i.e. `Dec`) then you would use `"MMM"`. Days are indicated by between one and four Ds, and years by Ys.

To show you how this works in practice, here are a series of `TEXT` formulae using different series of characters to indicate what they want to extract - followed by the result when used on the date 11/07/2013 (represented by `A1` in the formula):

- `=TEXT(A1,"MMMM")` gives you `July`
- `=TEXT(A1,"MMM")` gives you `Jul`
- `=TEXT(A1,"MM")` gives you `07`
- `=TEXT(A1,"M")` gives you `7`
- `=TEXT(A1,"D")` gives you `11`
- `=TEXT(A1,"DD")` gives you `11`
- `=TEXT(A1,"DDD")` gives you `Thu`
- `=TEXT(A1,"DDDD")` gives you `Thursday`
- `=TEXT(A1,"YYYY")` gives you `2013`
- `=TEXT(A1,"YYY")` gives you `2013`
- `=TEXT(A1,"YY")` gives you `13`
- `=TEXT(A1,"Y")` gives you `13`

You'll notice that the one-character options like `"M"`, `"D"` and `"Y"` will grab only one digit when the month or day is below 10 (i.e. the months January to September and the first nine days in every month), but if the month or day is 10 or higher, it will still show two digits. So in our examples above the 11th day is shown as `11` whether you use `"D"` or `"DD"`, but for the seventh month it does make a difference.

With years this doesn't make any difference at all: 2001 comes back as `01` whether you use `"Y"` or `"YY"`.

Only one of those letters can be used *five* times:

- `=TEXT(A1,"MMMMM")` gives you the first character of the month: `J` for July, for example, but also January and June - so, probably not much use then.

<aside class="tip blurb">

#### Which day of the week? The `WEEKDAY` function

`WEEKDAY` is yet another date function which can come in handy if you want to know which day of the week a date occurred - but *want that expressed as a number* between 1 and 7.

By default those numbers begin on Sunday (1) and end on Saturday (7). So the date September 11th 2001 (09/11/2001 in US date format or 11/09/2001 in UK date format), when used with the `WEEKDAY` function will return the value `3` - or Tuesday.

The full formula to calculate this looks like so: `=WEEKDAY("09/11/2001")` - or `=WEEKDAY(A2)` where the date is in cell A2.

However, if you *don't* want to start counting from Sunday the `WEEKDAY` function has an *optional* second parameter: a number which you can add to specify which day you want to count *from*.

A formula which has this second parameter will look something like this: `=WEEKDAY(A2,1)`

If you specify the value `2`, for example, in the formula `=WEEKDAY(A2,2)`, the days will be counted from Monday (1) to Sunday (7).

If you add the number `3` in the formula `=WEEKDAY(A2,3)` then the days will be counted in the same sequence, but will start counting from zero (0), with the highest possible value - Sunday - now represented by a 6.

The full list of values and what they do are as follows:

1 or 17: Sunday will be 1, through to Saturday as 7

2 or 11: Monday will be 1, through to Sunday as 7

3: Monday will be 0 through to Sunday as 6

12: Tuesday will be 1, through to Monday as 7

13: Wednesday will be 1 through to Tuesday as 7

14: Thursday will be 1, through to Wednesday as 7

15: Friday will be 1, through to Thursday as 7

16: Saturday will be 1, through to Friday as 7

If you try to use other values you will get a `#NUM!` error. You can also [find these values listed on Microsoft's support page for the `WEEKDAY` function](http://office.microsoft.com/en-gb/excel-help/weekday-function-HP010343015.aspx).

</aside>

#### Month and year combinations

You can also combine these characters in any way you want to generate specific date combinations. For example, if you wanted the month and the year together you could use a formula like this:

`=TEXT(A1,"MM YY")`

You can also add slashes, dashes, commas or other characters like so:

`=TEXT(A1,"MM/YY")`

Using one of these formulae allows you to generate whole columns showing just the year, month, or day on which an event occurred - as numbers, words, or three-character codes. Now you can calculate the trends you're looking for.

<aside class="warning blurb">

If you try to enter any date before 1900 Excel doesn't like it at all, and functions like `YEAR` and `DAY` will generate `#VALUE!` errors. In these cases it may be better to format the dates as text, and use some of the techniques detailed in subsequent chapters to extract numbers from those.

</aside>

### Using the Format Cells 'Custom' option to do the same thing to existing dates

If all you want is a series of months or days, you can actually use the **Format Cells** menu to change a date column in the same way.

This can be accessed by first selecting your date column (so that the results apply to the whole column), and then selecting the **Format** menu and, from that, **Cells**. A quicker approach is to right-click on your selection and select **Format cells** from the dropdown menu that appears - or using the keyboard shortcut CTRL + 1 (CMD + 1 on a Mac)

This should bring up the *Format cells* menu. You'll notice that this has a *Date* option to change how a date is displayed. Instead of the three series of digits separated by a slash, for example (i.e. 11/07/2013), you can choose a more natural language expression such as "Thursday, 11 July 13" and a number of other variations.


As always, this doesn't affect the underlying information (which is that number representing the number of days since the start of 1900) but it still shows *all* the information: day, month, year.

To show *only* that, select the *Custom* option at the bottom of the list of formatting options on the left. If the cell is already formatted as a date, then you should see date-related options suggested in the box underneath.


If not, you will see a series of other options. But it doesn't matter: either way you will need to type what you want into the box above those, and underneath *Type:*.

At the moment this will show something like `dd/mm/yyyy` and the grey *Sample* area above should show a preview of how that will affect the information in the first cell you're formatting.

Now, knowing those special series of characters used to specify 'a month as a word' or 'the day as a three character code' you can enter your own characters here:

- `mmmm` to show just the month for each date (as a full word)
- `mmm` to show just the month for each date as a three character code
- `ddd` to show just the day for each date as a three character code
- `dddd` to show just the day for each date as a full word

...and so on. As you type the characters you can see the effect on the preview immediately.

And of course these can be combined: `mmmm dd yy` will give you `July 11 13`; `yyyy-mmm-d` will give you `2013-Jul-11`.

You can add text strings here if you feel like it, by putting them in quotation marks like so: `mmmm "the" dd` which will produce `July the 11`. If you feel tempted to add "th" on the end, remember that this will apply to *all* dates, including the "1th", "2th", "3th" and so on.

Once applied, you will have a whole column containing just months, days, years, or any combination of those. The major disadvantage is that your original full dates are now hidden. This is why it's often better to use the `TEXT` function to fill extra columns with the specific data you want to work with, while leaving the full dates alone to be checked alongside that.


This story from the Birmingham Mail focuses on hours rather than days or months


### Hours and minutes: HOUR, MINUTE, SECOND and TEXT again

Sometimes you may come across dates that also include time information like so:

`06/06/2014 01:34`

If this is treated by Excel as a date (you can tell because it will be aligned right) then the same functions should work on this. `DAY`, `MONTH` and `YEAR` will still grab just that, and `TEXT` can be used for those ends too.

In addition, you can use three more functions to grab the hour, minute or second: `HOUR`, not surprisingly, `MINUTE` and... well of course, it's `SECOND`.

This formula, then, would grab the hour from any date in cell A2:

`=HOUR(A2)`

This includes dates without any specified hour (the result will be `0` - that is, midnight).

And this formula would grab the minute:

`=MINUTE(A2)`

Again, this will be `0` for dates without any hour or minute, because Excel assumes the time for those to be 00:00.

Finally, for those pieces of data where even the seconds are recorded, you might use the `SECOND` function in the same way:

`=SECOND(A2)`

The `TEXT` function also allows you to do the same with a little more control. This form example will give you the hour as a two-character result:

`=TEXT(A2,"HH")`

So for 01:34 the result will be `01`, rather than `1`, which would be the result of using `HOUR`.

A major peculiarity here is that the letter M can be used to identify both month and minute. Here's how it works:

In both the `TEXT` function and the **Format cells** menu the *default* assumption is that when you use `M` you mean 'month'. However, *if the M is used with H (hour) or S (second) it will assume you mean minute*. The following formula for example will grab the hour and minute, separated by a colon:

`=TEXT(A2,"HH:MM")`

And this will grab the minutes and seconds:

`=TEXT(A2,"MM:SS")`

It doesn't matter if no seconds are given in the cell - again it will count this as 'zero seconds'. So you can still use this to grab minutes and perform calculations with those.

And of course you can grab all three:

`=TEXT(A2,"HH:MM:SS")`

A final note on the `TEXT` function: it is not just designed to extract details from dates: [the same function can be used with numbers](http://www.techonthenet.com/excel/formulas/text.php) - particularly financial figures to add currency signs, commas, round up or down and add other formatting.


The Economist’s ‘Chart of the Day’ visualised over 2,200 goals by the minute in which they were scored


<aside>

#### Grabbing times of day and storing them as numbers using `TIMEVALUE` or `TIME`

A further function which is particularly useful if you're looking at times is `TIMEVALUE`.

`TIMEVALUE` does two things:

1.  Firstly, it will grab *just the time of day* from any timestamp - just as `TEXT` can grab just the minute and hour. So for example 12 midday on December 12 2012 is stored as simply `0.5` - that is, *half* of a day. This is particularly useful if you have data on a range of dates but are only interested in what *time* something happened.
2.  Secondly, `TIMEVALUE` will convert any time description *stored as text* so that it is stored as a number instead. So the phrase `"6:00 AM"` will be converted to `0.25`, allowing you to perform calculations such as asking if one time came before another, or how much time elapsed between one and another.

Note that if the time *is* stored as a number (check if it's aligned right) then `TIMEVALUE` will return a `#VALUE!` error. If the time is stored as text, it should be aligned *left*.

Note also that it does *not* work on more vague text expressions such as 'midday' or '12 midday', but only on the more specific sequence of text characters that Excel itself uses for a time (i.e. two pairs of digits separated by a colon, possibly followed by "AM" or "PM").

The `TIMEVALUE` function only needs one ingredient: the cell containing the date or time-as-text-string that you want to convert. A typical formula might look like this: `=TIMEVALUE(A2)`

A second function - `TIME` - is slightly more complex and less likely to be useful, but it's worth explaining as well.

`TIME` does much the same thing as `TIMEVALUE`: it converts a time into a number: a decimal point which describes what point of a day it is. So, 12 midday is 0.5: halfway through the day. 6am is 0.25: a quarter of the way through the day, and 6pm is 0.75: three-quarters of the way through the day. Other times are not so simple: 1am is 0.041666667, for example. But it's Excel's job to perform calculations with those.

The difference between `TIMEVALUE` and `TIME` is that whereas `TIMEVALUE` only needs one ingredient, `TIME` needs three: the hour, minute, and second of the time you want to convert.

So using `TIME` to convert 12 midday would look like this: `=TIME(12,0,0)` - that is: *convert 12 hours, 0 minutes and 0 seconds to a number*.

The most likely use case for this is where hours, minutes and seconds are stored in different columns in a particular dataset, and you want to combine them in a way that can be used in calculations.

</aside>

### When things don't go as you expect them to: dealing with errors in date functions

There are two errors you are likely to get when dealing with dates: the first is a problem with your source data (the dates themselves); the second is a problem with your results *other* than an error message. For example, you expect to see a number between 1 and 12 to indicate a month, but instead are seeing a whole new date.

If you have written a formula to extract part of a date and get a *whole* date as a result (and an odd one at that), it's probably because the cell you're writing in is formatted as date itself (and so the resulting number is formatted as a date).

Why is this a problem? Because the number `2013`, when formatted as a date, will appear as `05/07/1905` (the 5th of July 1905 was 2013 days after the start of 1900). The number `11` will be shown as `11/01/1900`, and so on.

To solve this problem just fix your formatting: select the cells in question and open the **Format cells** menu (either right-click, or use the *Format* menu at the top of the screen).

If, however, the problem is with your source data and you get a `#VALUE!` error when you try to use one of the date functions detailed above, it means that what you think is a 'date' actually isn't: most likely it's a series of characters that Excel hasn't been able to interpret as a date.

Throughout this chapter - and in the earlier chapter on *'Hitting the deadline: understanding and formatting the data'* I have explained how dates are actually stored as numbers: the amount of days since the start of 1900. Hours and minutes are stored as decimal places, so 12 midday would be .5.

If a date isn't stored this way - if it is expressed as a series of characters, or Excel thinks it is just a series of characters - then it cannot perform calculations and use date functions like `YEAR` (which are, after all, calculations to convert a number like 41466 into 2013).

This might happen for a number of reasons: it is not uncommon in data that has been extracted from a PDF, for example. Or it may be that extra characters have been entered, like "pm", or even extra spaces, which can cause problems. Sometimes it's to do with the way data entry is set up, and the 'date' is classified as a text field.

But whatever the reason, you have to deal with it. On this front, the function `DATEVALUE` is worth trying first.

`DATEVALUE` takes a series of characters and attempts to convert it into a value which can be understood as a date.

For example, `=DATEVALUE("18/10/2012")` will return the value `41200` (assuming the cell is formatted as 'general' or 'number' - if it is formatted as a date it will return `18/10/2012`).

Likewise, `=DATEVALUE(A2)` will do exactly the same to the contents of cell A2. If it works on one cell, you should be able to copy it down an entire column to perform the same conversion on a column full of dates-as-text. You can then format the column to show the numbers as dates, etc.

Because `DATEVALUE` works with text characters rather than underlying dates-as-numbers it is important to check that those dates use the same formatting as your system's date formatting. For example, if you're converting a US-style date format (month-day-year) but your computer system uses UK-style date formatting (day-month-year) or vice versa. In these cases you might need to treat it using the approaches detailed in the next chapter.

Likewise, if `DATEVALUE` gives you a `#VALUE!` error you'll need to use some different functions to extract parts of your date-as-text also detailed in the following chapters.

### Recap

- To find a story about trends in dates, you first need to **extract the month, day or year from each date**.
- The simple functions **`DAY`, `MONTH` and `YEAR` will extract just the day (number from 1 to 31), month or year** from any cell it uses as an ingredient. For example, `=YEAR(A1)` will give you the year of the date in cell A1.
- However, **those functions will only give you results as a number**: for example, `DAY` will return `10` for the 10th day, `21` for the 21st, and so on. It will not tell you what day of the week it was.
- **The `TEXT` function gives you much greater control over what date information you want to extract, and how it is shown**, including the ability to show days or months as words or three character codes.
- You can control what information you extract and how it is shown by using a series of characters for 'month', 'year', 'day', and so on, used as a second parameter in quotation marks like so: `=TEXT(A1,"DDDD")`. Four Ds for 'day', in this example, will extract the day as a word.
- As a general rule, **one character means 'one or two digits'; two characters means 'two digits'; three characters means 'a word as a three letter code' and four means 'a whole word'**. For a date in January each of these would return `1`, `01`, `Jan` and `January` respectively.
- **You can also combine more than one series of characters to generate combinations**, such as 'month/year' or 'day/month'. Such a formula would look something like this: `=TEXT(A1,"MMMM/YYYY")` or this: `=TEXT(A1,"DDDD/MMMM")`.
- **Dates are stored as the number of days since the beginning of 1900**. This allows Excel to make all sorts of calculations.
- **These numbers can be formatted in any way you like by using the *Format cells* menu** and selecting the *Date* options.
- **To display just the month, day or year of dates you can use the *Custom* section** and the same letter codes as the `TEXT` function, e.g. `mmmm`
- However, **it is best to extract parts of dates into a separate column so you can still see the original dates in full**.
- **`WEEKDAY` is another date function which will tell you on which day of the week a date occurred, expressed as a number between 1 and 7**.
- **You can specify whether `WEEKDAY` starts counting from Sunday, Monday, or any other day by using a second parameter**. You can also specify that it starts counting from zero.
- **Some dates include hours, minutes and seconds. These are stored as fractions of days**. So 12 midday, for example, is represented by adding an extra 0.5 to the number representing the date.
- **You can extract the hour, minute or second of a date using the `HOUR`, `MINUTE` or `SECOND` functions**.
- **You can also extract and combine hours, minutes and seconds using the `TEXT` function and *Custom* formatting option too**.
- **The codes to extract hours or seconds are `HH` and `SS`**.
- **Minutes can be extracted using `MM` *alongside* the `H` or `S` codes. However, Excel will assume you want the *month* if you use `MM` on its own**.
- The `TIMEVALUE` function can **convert text expressions of times into numerical ones. It can also extract times from date-and-time entries**.
- The `TIME` function can **combine and convert parts of times (hours, minutes and seconds) into a single time entry** - but you must give it all three parts separately.
- **If a date is stored as a series of characters instead of as a number, date functions will return an error: `#VALUE!`**. In these situations you can try to convert the series of characters into a date using the `DATEVALUE` function; or use other functions to extract the relevant part of the 'date' - for example the first two characters (day) or last four characters (year). We'll explain this process in the next chapter.
- **If the result of your formula to extract a year, month or day is another full date then it's likely the results have been wrongly formatted** to convert whole numbers like '2013' or '12' into a date based on that number of days since 1900. To fix this change the formatting to a number.

### Finding the story: which outlets have consistently bad scores?

At the end of the last chapter we looked at [some food hygiene ratings data]() and suggested that we could use the `AND` function to identify businesses with a particular *combination* of qualities. Here's how to do that:

1.  In column N your `AND` formula to identify which outlets scored 10 or above across all three criteria in columns K, L and M should look something like this: `=AND(K2>=9,L2>9,M2>9)` - or, if you were using the 'greater than or equals to' operator, this: `=AND(K2>=10,L2>=10,M2>=10)`
2.  Changing the formula so it returns TRUE if *any* rating is 15 or above would mean switching to the `OR` function like so: =OR(K2\>=15,L2\>=15,M2\>=15)
3.  Now, the tricky one. Finding out which outlets have a bad overall rating is straightforward: our formula would begin `=AND(A2<3,` ... but to add a criterion which tests whether the date was a year ago we need to make sure it can perform that calculation. There are a number of ways to do this...

> The simplest is to put your date in quotation marks. If one year ago was the first of January 2013, you might express 'less than' that date like so: `<"2013-01-01"`. Adding that to your formula would look like this: `=AND(A2<3,A2<"2013-01-01")`.
>
> A second option is to express that date as a number. To do this, type it in a cell somewhere and then change the formatting of that cell from 'date' to 'number'. The number for the first of January 2013 is 41275. See the chapter on dates for more on formatting.
>
> A third option is to put your date in another cell, and refer to that in your formula. For example, if you put the date in cell O1 (the first row in column O) your formula could test against that like so: `=AND(A2<3,A2<O1)`. However, remember that if you copy this formula down to further cells, that cell reference will change - to O2, then O3, O4, and so on. To fix it you need to use a dollar sign before the column name and row number, like so: \$O\$1 - making the formula look like this: `=AND(A2<3,A2<$O$1)`

<aside class="exercise_blurb blurb">

### Find the story: what years and months are worst for hygiene inspections?

In the [data for the previous exercise](https://drive.google.com/file/d/0B5To6f5Yj1iJeUM2VFZkaUc3MDQ/edit?usp=sharing) is a column called `RatingDate`. This contains date information for all the inspections. Based on this, try the following:


1.  At the moment the cells show the dates as numbers - e.g. `41137`. Select the whole column and change the formatting so we can see those formatted properly as dates.
2.  Insert a new column to the right of the date column. Call it 'Year'. Write a formula to extract the year from those dates. Copy it down the whole column so you have a year for each inspection.
3.  Insert another new column to the right of your new year column. Call it 'Month'. Write a formula to extract the month from the dates. Copy it down the whole column so you have a month for each inspection.
4.  You know what's coming don't you? Insert yet another new column to the right of your new month column. Call it 'Day'. This time, however, write a formula to extract the day in each date *as a word*, i.e. Monday, Tuesday, Wednesday etc. rather than 21, 22, 23, etc. Copy it down the whole column so you have a month for each inspection.
5.  How can you work out in which year or month, or on which day, the failing ratings (2 or below) are given? (There is more than one way).
6.  What issues might you need to watch for in drawing any conclusions about the 'worst' month, year or day etc?
7.  How might you account for those issues?

</aside>


## How old is someone? Ages and using `TODAY`'s date

Marion Urban is a French journalist with decades of experience. In 2014 she was preparing for the General Election the next year - and focusing on the data others would need to be able to report quickly.

In order to do this Marion had downloaded details on the candidates who had stood successfully in the previous election. "It was a very young intake," she noted. "But it wasn't easy to calculate their ages".

Indeed. You would think that calculating ages in Excel would be easy. But there is no off-the-shelf function to help you do so. Or at least, no easy-to-find function.

Instead there are a range of different approaches: some of them particularly, and unnecessarily complicated.

In this chapter I will outline one approach to calculating ages, which also illustrates a useful technique in using spreadsheets in stories: the ability to break down a problem into different parts.

I'll then show some other solutions to the same problem, and when those might be more appropriate.

### Breaking down the problem

If your spreadsheet problem isn't solvable with a single function, the best approach is often to break it down into smaller problems which, individually, can.

That is the case here.

For example: we *can* calculate an age by subtracting the year of a person's date of birth (DOB) from the year of another date (today, for example, or the election day).

But this approach has room for a small error: it is only correct if the person's date of birth comes *before* or *on* the date we are calculating against. If the person's date of birth comes *after* the date we are using, the result will be an age that is one year *older* than they are at the moment.

For example: if we take the year 2014 and subtract 1974 to find out the age of someone born that year, we will get the result 40. But if the date in question is January 30 2014, then that person born in 1974 will only be 40 if they were born on or before January 30 that year. If they were born any later they are still 39.

Once you've identified a possible error like this, **don't write it off immediately**. You may be able to add an 'error checking' formula to correct it - and that is the case here.

Ultimately the key question to ask is: *does this formula get me any closer to the result I need?*

In this case the answer is 'Yes': a simple subtraction formula of 'this year minus the year of the person's date of birth' will get us either the correct result, or one which is *only one year out*.

All we need is a way of identifying which result it is, and correcting the initial age accordingly.

### Calculating the years

First, however, we need to calculate the two years that we need to work with: the year of someone's date of birth; and the year of the date we want to calculate their age for (that might be today, or it might be a key date such as the day they were voted into power).

To calculate the year of the date of birth you can use the `YEAR` function like so:

`=YEAR(A2)`

The formula above takes any date in A2 and returns a number representing just the *year* in that date.

<aside class="warning blurb">

If you get a result which is not a four digit number but *yet another date* then **don't panic**: the result is not wrong: it's just the way the results are *formatted*.

Remember that all dates are stored as numbers. The number '2014', for example, is the way that Excel stores the date 06/07/1905 (2014 days since the beginning of the 20th century).

When that number is formatted as a date, you won't see the number 2014 but instead the date 06/07/1905.

To fix this, change the formatting. Right-click on the cell concerned and select **Format cells**. Then change the formatting from *date* to *Number* or *General*. You may also need to reduce the decimal places to avoid getting `2014.00`.

</aside>

To calculate the difference between two years - that is, the number of years between someone's date of birth and another date - simply subtract the result of one YEAR formula from another YEAR formula like so:

`=YEAR(B2)-YEAR(A2)`

Remember that the first `YEAR` function in that calculation should refer to the more recent date; you want to subtract the earlier year (a smaller number) from that.

Let's say, for example, that in column B we have the date of an election, repeated all the way down. In column A we have each candidate's date of birth.

The formula above - when also repeated down a column - grabs the year of the election date and subtracts from it the year of each candidate's date of birth.

Given that the election date is always the same, another way of doing this would be to avoid using a cell reference for the first date and enter it directly into the formula so:

`=YEAR("05/05/2005")-YEAR(A2)`

Or even simpler:

`=2005-YEAR(A2)`

The result should be a column of ages that are at worst a year out.

Now to correct those.

### Checking whether a birthday comes before or after a date

We've already described the factor that will separate the accurate results from those which are one year out: the individual's birthday will come *after* the date we are using as the basis of our subtraction.

We *could* use the TEXT function to identify that birthday, by just grabbing the day and month of any date. Here's how you would do that for a DOB in cell A2:

`=TEXT(A2,"ddmm")`

The two Ds and two Ms in `"ddmm"` indicate that we want **two character codes** for the day (D) and month (M).

The two digit code for the first day of any month would be 01; for the second day 02; and so on. The same two digit codes apply to each month too.

The results will range from 0101 (the first day of January) to 3112 (the 31st day of December).

However, this will be treated as a whole number - so 0107 (the first of July) will be treated as smaller than 0201 (the second of January).

Instead, then, we need to use the US date formatting approach of month-day:

`=TEXT(A2,"mmdd")`

The results will now range from 0101 (the first day of January) to 1231 (the 31st day of December).

When done this way we can be sure that all dates in February (beginning 02) will be greater than dates in January (beginning 01), and so on.

<aside class="tip blurb">

If you really want to check you can create a range for every date in the year and test them: that's what I did!

</aside>

To check if one date is later than another we can just use the '*greater than*' operator like so:

`=TEXT(A2,"mmdd")>TEXT(B2,"mmdd")`

This asks whether the result of the first TEXT formula (someone's birthday) is greater than the result of a second TEXT formula (the day of an election).

There are only two results: TRUE (yes, it is greater) or FALSE (no, it is not).

If it *is* greater it means that that person's birthday came after the election, and their age should be adjusted accordingly.

If it is *not* later, the age does not need adjusting.

### Making an adjustment based on the results

We *could* use an `IF` function to adjust the age based on the results of these calculations...

...but in this case we don't need it.

This is because, helpfully, **TRUE and FALSE are treated as 1 and 0 by Excel**: something we can use to our advantage in our formula.

We'll make this simpler by putting our initial age guess in column C. Our table so far, then, has these columns:

A: The person's DOB

B: The election date

C: A calculation to get an age which is either accurate or a year out: =YEAR(B2)-YEAR(A2) for row 2, and so on.

Now in D we can enter the following to correct that age in C:

`=C2-(TEXT(A2,"mmdd")>TEXT(B2,"mmdd"))`

The formula *starts with the age from C2* and subtracts *something* from it.

What it subtracts is the *result of a formula*, in parentheses: a TRUE or FALSE result to the question "Is A2's month-day greater than B2's month-day value?")

A TRUE result is the same as 1, so the result in those cases is `C2-1`. In other words the age is reduced by 1 because the person hadn't had their birthday.

A FALSE result is the same as 0, so the result is `C2-0`: in other words, the age is correct and does not need adjusting.

You can cut out the need for column C by putting that directly into the formula like so:

`=YEAR(B2)-YEAR(A2)-(TEXT(A2,"mmdd")>TEXT(B2,"mmdd"))`

And you can cut out the need for column B by putting the year *and the month-day value* directly into the formula too:

`=2005-YEAR(A2)-(TEXT(A2,"mmdd")>"0505")`

Note the two places where we've altered the formula: firstly at the start, with `2005` replacing `YEAR(B2)`; and secondly in the other point of the formula where B2 was mentioned: `TEXT(B2,"mmdd")`. In this case we don't need the `TEXT` function to tell us the month-day value because we know it will always be `"0505"` (I've shown you the other approach in case your dates are not always the same).

<aside>

If you're curious *what* using an `IF` function to perform the correction would look like, it would look like this (where C2 contains our initial this-year-minus-year-of-birth calculation):

`=IF(TEXT(A2,"mmdd")>TEXT(B2,"mmdd"),C2-1,C2)`

That formula says '*If* the date of the person's birth is greater than the date we are subtracting from, then return the result of C2 minus 1 (this-year-minus-year-of-birth minus one). *Otherwise*, return the result of C2' (this-year-minus-year-of-birth).

In other words: if the date is later, correct that initial calculation. But if it's not later, then stick with it.

</aside>

### Using `TODAY` to calculate an age against today's date

The same formula can be adjusted to apply to today's date using the `TODAY` function.

This function does exactly what you might expect: returns today's date. For that reason it has no ingredients at all: it is typed like this:

`=TODAY()`

In our case we can either use the formula `=TODAY()` in all the cells in column B, or put it directly into the formula where any references to that column were used, like so:

`=YEAR(TODAY())-YEAR(A2)-(TEXT(A2,"mmdd")>TEXT(TODAY(),"mmdd"))`

...But by *this* point you'd be forgiven for having lost track of how you got here.

The problem with long formulae like this - and the equivalent for an election date above - is that when you come back to the spreadsheet later it may not make much sense.

Worse, if anyone else has to use the spreadsheet they are likely to struggle even more to understand what is being calculated.

For those reasons **it is often better to have columns with each stage of the calculation clearly labelled**, rather than combine all the calculations into one complex, albeit impressive formula.

<aside class="tip blurb">

#### Working things out to the hour or minute: `NOW`

If you want to be even more precise than 'today' there is a similar function which will generate the *full* date including the current *hour and minute*.

`NOW` works much the same way as `TODAY`: it has no ingredients so you just need to include an empty pair of parentheses immediately after it, like so:

`=NOW()`

This time you will get a full date *and time* like so: `12/09/2014 15:52`

Once again you can combine this function with the `TEXT` function's options to grab minutes, hours and/or seconds if you want to calculate something down to that level of detail. For example, this would be useful when looking at data relating to peaks in mentions of a particular term on Twitter, or data relating to the times of day when accidents or crimes occur.

</aside>

### Making it easy to understand: breaking the formula back up

So let's take a moment to break those stages down:

1.  We begin with a column of dates of birth, called 'DATE OF BIRTH'
2.  Then we create a second column to hold the date(s) we're using as the start of our calculation: either today's date, in which case each cell will hold the formula `=TODAY()`, or a date in the past such as an election day. That date will be copied down the whole column. This will be called 'TODAY'S DATE' or 'ELECTION DATE'. So far, it's going to be pretty easy for any colleagues - or our future self - to understand this spreadsheet.
3.  Next we create a column to calculate the year of the later date minus the year of the date of birth. We call this 'AGE MAYBE ONE YEAR OUT' or 'AGE APPROX' or something similar.
4.  In the fourth column we write a formula to check *if* the age is a year out: specifically if the month-day value of the date of birth is greater than the month-day value of the date we're subtracting from. When copied down the column should be filled with results that are either `TRUE` or `FALSE`. That column is called 'AGE ONE YEAR OUT?'
5.  Finally we create a column that corrects that age where the value in the fourth column is `TRUE` (the month and day or birth is later than the month and day of the date we're subtracting from). We title that column 'CORRECTED AGE'.

How many columns you have depends on how clear you want the spreadsheet to be to yourself and others. For example it may be too simple to combine the last two into one column simply called 'CORRECTING AGE'.

But the point remains: there's no point combining multiple calculations into one powerful formula if the formula isn't going to make sense to you later, or if your data is going to be used by colleagues or people who come after you.

<aside>

#### How complicated can you make calculating an age?

Ian Balboa (see below) was one of the resources that Marion Urban came across when she was trying to find help in calculating ages. His 'hard way' of calculating an age looks like this:

`=IF(A1-DATE(YEAR(A1),1,1)>TODAY()-DATE(YEAR(TODAY()),1,1),1,0)`

Now that's some formula. I'll leave it to you to see if you can work out what it's doing - but if there was ever a case for splitting things up to make them clearer to others, this is it.

</aside>

### Other ways of calculating ages: the unsupported DATEDIF function

There are many different ways to arrive at the same results. Ian Balboa, for example, [notes](http://www.happy.co.uk/excel-hints-tips-calculating-age-from-date-of-birth/) that Excel *used* to have a function for calculating the difference between two dates: `DATEDIF`. But "The bad news is that for some reason Microsoft no longer supports this function in Excel."

What this means is that if you begin typing `=DATEDIF` in a modern version of Excel, you will notice that the software does not seem to recognise it in the way that it does with other functions: it doesn't attempt to finish the word 'DATEDIF' when you begin typing it; and it doesn't bring up a tooltip hinting at the parameters that the function needs, as it does with other functions.


When you begin typing other functions like DATE Excel suggests functions you might be trying to use


…However, when you type DATEDIF it doesn’t suggest that function


Likewise, there’s a tooltip that tells you the ingredients for DATE or other functions - but not for DATEDIF


So the `DATEDIF` function *will* work in Excel - but it's not **supported**: the software won't suggest it, or help you write it very much unless you go as far as to type the function and open the parenthesis, and then click on the link that appears in the tooltip. And that's only in *some* versions of Excel.


However, once you do open the parenthesis you will get a link to a Help file in some versions of Excel


This makes it a difficult function to use - because it does have some very specific ingredients.

`DATEDIF` needs three ingredients:

1.  A start date
2.  An end date
3.  And the units you want to count: for example the difference in years, months or days. These are indicated by specific codes, detailed below.

The first two ingredients are relatively straightforward: the only thing you need to remember is to place dates in quotation marks, e.g. `"05/05/2005"` - otherwise it will treat the date as a *calculation*: i.e. 5 divided by 5 divided by 2005.

You *can* include dates formatted as numbers - for example, 38477 for the fifth of May 2005 - but the extra effort involved in finding out the numerical equivalent for any date makes that pretty pointless. Just stick some quotation marks around it!

And of course you can use cell references instead to point at a cell containing a date - as long as Excel is treating that cell as a date and not as a string of text (text will be aligned left; numbers and dates aligned right).

The final ingredient - the units you want to count - is expressed as a one- or two-letter code in quotation marks. The three single character codes simply measure whole years, months or days as follows...

- `"Y"` will return the number of *whole* years between the start and end dates. This addresses the problem of birth dates that occur later than the end date.
- `"M"` will return the number of whole *months* between the start and end dates.
- `"D"` will return the number of days between both dates.

...but the three double-character codes essentially calculate *remainders* left over once the *whole* years or months are counted. The key in each is the second character:

- `"MD"` will return the number of *days* between the start and end date *after* whole years and whole months are counted. In other words, if someone is 12 years, five months and three days old, this code will return `3` (the number of days left). The maximum possible result, then, is 30 (31 days being a whole month).
- `"YM"` will return the number of whole months between the start and end date after subtracting whole years. So again, if there are 12 years, five months and three days between two dates, the result will be `5` (the number of whole months left after years are excluded). The maximum possible result, then, is 11 (12 months being a whole year).
- `"YD"` is a little different: it assumes your two dates are **less than a year apart**, and counts the number of days between them. The maximum possible result here is 364. This is very similar to using `"D"` to simply calculate the difference between two dates - the one difference is that limit: two dates which *are* more than a year apart will still return the result `364`.

As I say, because Excel doesn't support this function any more you will need to have these codes to hand when you use it.

<aside class="error blurb">

#### The `#NUM!` error

If you get a `#NUM!` error when using the `DATEDIF` function it is most likely because the start date is *later* than the end date. The function doesn't expect this, and cannot give you a negative result.

</aside>

You can combine the two sets of codes to calculate how old someone is in both years and months. For example, the following formula will calculate how old someone was on election day in years, based on a date of birth in cell A2, and an election date in cell B2:

`=DATEDIF(A2,B2,"Y")`


In the next cell you can use a similar formula to tell you how many months old they were *in addition to those years*:


The result of both gives you the full picture:


<aside class="tip blurb">

#### `DATEDIF` in Google Sheets

The `DATEDIF` function is much better supported in Google's own spreadsheets tool, [Google Sheets](http://sheets.google.com). Not only does Google Sheets suggest `DATEDIF` if you begin typing 'DATE' but it also has a comprehensive 'hint' box that appears once you open the parenthesis, including a link to even more information.


We'll be working with Google Sheets more later in the book.

</aside>

### Watching out for leap years in other calculations

Yet another method for calculating ages comes from journalism professor Steve Doig, who uses the following formula:

`=(DATE(2014,4,24)-B2)/365.25`

He explains:

> "The first part of the formula calculates the number of days between the two dates, which is then divided by 365,25 (the 0,25 accounts for leap years) to produce the years.

The leap year point is really important: remember that Excel stores dates as *the number of days* since 1900 - so years with 366 days will have those extra days added into the total. This is another example of identifying possible problems in calculations and building in corrections.

This is also the first appearance of the function `DATE`, which bears some explanation.

The `DATE` function **converts any date into a number**. This might seem a bit pointless given that Excel does this anyway: type 05/05/2005 into Excel and it will assume you mean May 5th 2005 and store it accordingly, as the number 37015 (although it will continue to format it as `05/05/1975`).

Indeed, you could rewrite the example formula above to strip out the `DATE` function entirely, so that it looked like so (with UK date formatting):

`=("24/4/2014"-A4)/365.25`

However, dates do not always play nicely. The `DATE` function is a useful way of **making sure that your date is understood correctly by Excel**.

The `DATE` function takes three ingredients: a year, a month, and a day of the month - *in that order*. If you have a date (or dates) which has been formatted unusually, this ensures that they are interpreted correctly.

But in order to do so, you'll need to be able to extract the different parts of any given 'date' - and that's the subject of the next chapter on `RIGHT`, `LEFT` and `MID`.

### Recap

- Ages can be particularly interesting angles to explore in any dataset: the oldest, youngest, or general demographic makeup of people in a dataset (younger, older) can all be newsworthy.
- There are a number of different ways of calculating an age, but none are straightforward.
- You can subtract one date's year from another date's year - but **some results could be one year older than the person's age if their birthday occurred later in the year than the date you are subtracting from**.
- **Using a function for error correction helps you identify the results you need to change**.
- In this case, we can **extract the month-day value of a date of birth and test if it is greater than the month-day value of the more recent date**, using the `TEXT` function and `"mmdd"` as our second ingredient.
- A `TRUE` or `FALSE` result (known as a Boolean) is also equal to 1 or 0. So **`TRUE` and `FALSE` can be used as 1 and 0 in any calculations** - quite handy if you need to subtract one from a number when something is TRUE.
- **The `DATEDIF` function allows you to calculate the difference between any two dates** in terms of days, whole months or whole years - so you can use it to calculate ages.
- **However, the `DATEDIF` function is not supported in modern versions of Excel**, so you have to know which ingredients are used, and in what order.
- **The `DATEDIF` function is, however, supported in Google Sheets**, where you can find help on using it.
- **The three ingredients of the `DATEDIF` function are, in order: the earlier date, the later date, and the units you want to count in**: years (`"Y"`), months (`"M"`) or days (`"D"`), or 'remainder' months or days once whole years or months have been counted.
- **If you get a `#NUM!` error when using the `DATEDIF` function it is most likely because the start date is *later* than the end date**.
- Another alternative is to **count the number of days between a date of birth and the more recent date, and divide that by 365.25** to get an age including decimal places.
- **The extra `.25` in that calculation is to account for leap years where there are 366 days**.
- If you want to calculate an age based on today's date, and ensure that the date is correct whenever we open the spreadsheet, **you can use the `TODAY` function to generate today's date**.
- **The `NOW` function does exactly the same, but also adds the current *time*.**
- **Both the `TODAY` and `NOW` functions have *no* parameters**: so they use empty parentheses like so: `=TODAY()` or `=NOW()`.

### Finding the story: what years and months are worst for hygiene inspections?

In the last chapter I outlined some challenges to extract years, months and days from a column called `RatingDate` and find the stories they told. Here are the solutions:

1.  To change numbers like `41137` into dates, select the whole column and right-click to select **Format cells**. Select the *Date* option on the left, and click **OK**. You can access the same menu by going to the **Format** menu at the top of your screen, and selecting **Cells...**, or pressing CTRL+1 (CMD+1 on a Mac).
2.  To extract the year from the dates in column G the formula is `=YEAR(G2)` for your first date, then copy it down the whole column so you have a year for each inspection. You can also use the formula `=TEXT(G2,"YYYY")`
3.  To extract the month from the dates in column G the formula is `=MONTH(G2)` for your first date, then copy it down the whole column so you have a month for each inspection. You can also use the formula `=TEXT(G2,"M")`
4.  To extract the day from the dates in column G as a word the formula is `=TEXT(G2,"DDDD")` for your first date, then copy it down the whole column so you have a day for each inspection.
5.  You can work out in which year or month, or on which day, the failing ratings (2 or below) are given in a number of ways. The quickest is a pivot table with your focus (year, for example) in the *rows* and *data* areas, and the rating used as a report filter (selecting those 2 or below). Pivot tables and advanced filters are covered in *[Data Journalism Heist](https://leanpub.com/datajournalismheist)*.

> An alternative is to use a series of `COUNTIFS` formulae, e.g. to count how many were rated below 3 in 2012: `=COUNTIFS(A:A,"<3",H:H,"2012")`

1.  If you are drawing any conclusions about the 'worst' month, year or day etc. you need to take account of the possibility that the year or month with the most failing inspections might simply be the year or month with the *most* inspections full stop. In other words, that year wasn't one for failing ratings, it was just one when lots of ratings were issued. This is particularly clear when you try to find out how many inspections there were in each year: 2013 saw 933 inspections, compared to 672 previous year and 273 in 2011 (this may be because ratings are only shown for businesses still operating, or it could be because more new businesses opened in that period, or it could be that more funding was given for inspections, or higher targets set - any of these might be interesting leads for stories!).
2.  To account for those issues you need to make sure you look at *proportions* rather than absolute numbers. In 2013, for example, 10% of establishments received a failing rating below 3. In 2012 4% did, and in 2010 and 2011 the figure is below 1%. Before 2010 *no* institutions received a failing mark...

> Does that sound right? At this point you should be pausing and thinking: *'I'm not seeing the full picture here'*. Just as the changing inspection numbers might raise questions, these proportions should make you pick up the phone to ask them. Your story might not be about those early years, but they are a clue to a wider problem: if the data only relates to currently operating businesses, then at the very least we need to revise our language to reflect that.

> So, "4% of establishments inspected in 2012 received a failing rating below 3"? Not necessarily if we are not seeing all the inspections. We can perhaps confidently report the most recent year's results, but to draw any comparisons with previous years we may have to request any data for businesses no longer operating (it would follow that institutions receiving a failing mark may go out of business).

<aside class="exercise_blurb blurb">

### Find the story: how old are Guantanamo prisoners?

At [this link you'll find a spreadsheet containing details on almost 800 individuals detained by the US Department of Defense at Guantanamo Bay, Cuba](https://drive.google.com/file/d/0B5To6f5Yj1iJa0xmbVNRZTdyQk0/edit?usp=sharing).

The spreadsheet was found on the site for the [Center for the Study of Human Rights in the Americas](http://humanrights.ucdavis.edu) by using the advanced search `"Date of Birth" Guantanamo filetype:xls`.

It has six fields (columns): a simple index number, most likely added by the creator of the sheet; a date of birth; a name; an 'ISN' code (you'd have to find out what this means); citizenship details; and their place of birth.

1.  Firstly, check that the date of birth is being treated as a number by Excel. How would you do this?
2.  Insert a new column between current columns B and C which gives us the age of each individual based on their date of birth. What formula will you use? Do you need to use more than one column?
3.  What sort of error checking might you need - whether in the sheet itself or through follow up phonecalls?
4.  Now that you have their ages what stories might you tell about those?

</aside>



## Grabbing or checking the first, middle or last part of a piece of information: `RIGHT`, `LEFT` and `MID`

Sometimes you only want to look at part of some data - for example the first or last part of a postcode, zip code, or telephone number. Dates which are stored as text rather than numbers are also prime candidates.

The functions `RIGHT`, `LEFT` and `MID` are tailor-made for those problems. These will, respectively, grab a specified number of characters from the end, beginning, or middle of a cell.

Used on their own they work particularly well where you always want the same number of characters - but they can also be combined with other functions to grab different amounts of text, as we'll see.

<aside>

#### Splitting names, dates, addresses and other data: text to columns

If your data already has a particular character that marks one part from another - such as a space between first name and surname, or slashes between day, month and year - then you can use the menu option **Text to columns...** (normally in the **Data** menu) to split it, rather than needing to use a function. Note that if you use this, the original column will no longer exist, so you might want to duplicate it first.

To use this function first make sure that the column you want to split is placed *in the last column of your data*. You may need to select it, cut or copy it, and paste it at the far right of your data to get it there.

This is because when you split the column *it will overwrite anything to the right of it*.

Once the column is in the right place, select it, and then go to **Data \> Text to columns...**


The *Text to columns wizard* will now open. The first option it presents you with is whether you are splitting 'Delimited' or 'Fixed width' data. Fixed width data can be split on a specified character position (for example, it can split all cells at the fourth character) but here we're talking about *delimited* data: that is, data where a specific character sets the limits of one part, such as the end of the first name or the day. Make sure this is selected and click **Next**.

The next step presents you with a number of common characters you can select as your delimiter: *space*, for example (which may separate a first name from a second name), and *comma* (which may separate the first line of an address from a second part, and a third part). If you want to split your data on either of those characters, or *tab*, or *semicolon*, then tick the relevant box and click **Next**. If you want to specify another character - such as a slash - then tick *Other:* and type the character in the box next to it. Note that you cannot enter multiple characters here.

In the final step you have some options to format the new columns you are creating. This defaults to 'general' and in most cases that will be fine. However, if one part of your data is a date, you can *select that column* in the preview at the bottom and then tick *Date:* in the area above and to the right of that. You can also, next to *Date:*, select what format the date uses - YMD (Year/Month/Date), MDY (Month/Date/Year) and so on.

Note when you change the format that the preview underneath reflects this: the first row describes the format of the column underneath. So you can see at a glance how each column is going to be formatted.

If you're happy with the preview then click **Finish** and you should now have at least two columns where you previously only had one.

In some cases, you may find moving columns around more hassle than using a `LEFT` function. Perhaps more likely, however, is that you want to retain your original data and use those other functions to extract from it, rather than splitting it up.

</aside>

### Grabbing characters from the beginning: LEFT

The `LEFT` function has two ingredients: the cell you want to use, and the number of characters you want to grab from the beginning (the left). If you wanted to grab the first two characters of cell A2, for example, you would use the following formula:

`=LEFT(A2,2)`

This function is particularly useful whenever you are working with any sort of code - whether commonly known codes like area codes or postcodes, or internal codes such as institution codes, invoice numbers and cost codes, where different parts refer to different things (just as in a telephone number the first part refers to the area).

If you only wanted the area codes from a list of phone numbers, for example, you could use this to grab them. You could also use this to separate different types of numbers: for example, the first two digits of mobile numbers might always be '07'; the first two digits of international numbers always '00'; and the first two digits of landlines always '01' or '02'.

Dates are worth a particular mention here - as you will get different results depending on whether the date is stored as a number, or as a series of text characters.

If the date is stored as a number it is easiest to use the functions detailed in the previous chapter on the functions `YEAR`, `MONTH` and `DAY`.

If it is stored as text, however, the `LEFT`, `RIGHT` and `MID` functions can help you out.

To give you an example: in the series of characters "2012-08-16" *not* stored as a date this formula will grab the first two: `20`. However, if it *is* a real date then it will grab the first two digits of that date *when expressed as a number*: `41` (the full number for that date is 41137).

If you get a result like this you know the date is stored as a number, and you should use `YEAR`, `MONTH` or `DAY` instead.

<aside>

#### Dealing with dates and partial dates stored as text: `DATEVALUE`

If you are trying to clean up dates that have been stored as text, take a look at the `DATEVALUE` function. This will convert a date which is stored as a text string, into a date which is stored as a number string.

The best way of demonstrating this is by using the `TEXT` function to show you what happens when dates are stored as text.

Type a date in cell A1 - for example `12/12/99`. Excel interprets this as a date and stores it as the number of days since 1900 (35044), but still *formats* the date as `12/12/99`. The date will be aligned right.

In cell B1 type the formula `=TEXT(A1,"dd/mm/yyyy")`. This will turn that date into some text which shows the days as two characters, followed by a slash, followed by the month as two characters, followed by another slash, and then the year as four characters. You can tell it's text because it's aligned *left*.

Now if you right click on cell B1 and select **Format cells...** you'll notice that changing the format to *General* or *Number* does not change the date in the same way that it would in cell A1.

In cell C1, then, you can turn the date-as-text-string *back* into a date-as-number by using the `DATEVALUE` function like so: `=DATEVALUE(B1)`

Unless C1 is formatted in some other way, you should see the result as a number: 35044. You can format this as a date by, again, right-clicking and selecting the **Format cells...** option, then choosing *Date*.

`DATEVALUE` is particularly good for dealing with **partial dates** - as long as they refer to this year. A text string like `12-Dec` will be interpreted by `DATEVALUE` as the 12th December *this year*, and converted accordingly.

</aside>

### Grabbing characters from the end: RIGHT

The `RIGHT` function works in exactly the same way as `LEFT`, with two parameters: the cell you want to use, and the number of characters you wish to grab - this time from the *end* (the right).

If you wanted to grab the *last four* characters of A2, then, you would use this formula:

`=RIGHT(A2,4)`

Again, with dates which are actually stored as the number of days since 1900 this will grab the final digits of that number.

What if the number of characters *depends* on the length of the data? Well you can include a calculation to work that out - we'll come onto this below.

### Grabbing characters from the middle: MID

The `MID` function is slightly more complicated, needing three parameters: the cell you want to extract from; *what character position you want to start grabbing from*; and how many characters you want to grab.

Obviously the starting point for `LEFT` and `RIGHT` is predetermined, but `MID` can start from anywhere - including the beginning (position 1).

*The starting character is included in the results* and the counting. For example, if you want to grab two characters from character position 3, it will grab that third character, and the fourth (two in total).

Remember also that spaces are counted as characters and will be grabbed just as text characters will be.

If cell A1 contained the string `Finding stories in spreadsheets`, then, here are some formulae using `MID` with the results:

`=MID(A1,1,5)` will get you 'Findi' (the five characters starting from position 1)

`=MID(A1,10,5)` will get you 'torie' (the five characters starting from position 10)

`=MID(A1,30,5)` will get you 'ts' - as there are only 31 characters in the string of text it's working with, this grabs the first two from position 30.

A `MID` formula working on this text which specified a starting position of 32 or higher would return nothing, because there are no characters from that position. But it will *not* generate an error.

<aside class="tip blurb">

#### When you don't know how many characters from the end: MID as an alternative to RIGHT

Because `MID` can hit the end of your text and not generate an error, the `MID` function can be a useful alternative to `RIGHT` when you do not know exactly how many characters you want to grab at the end of a cell, but you do know what position those characters start *from*.

In these cases, just set the number of characters to a value which you know will always capture *all* characters after your specified point, for example `100`. In practical terms this translates as 'grab all the characters from this point until the end'.

</aside>

### What if the starting position or number of characters *depends*? Introducing LEN

In the examples above we have had to specify how many characters we want to grab, or what position to start grabbing from. However, in many codes that number *is not always the same*.

UK postcodes are a great example of this: they come in two basic parts - the first part indicates the area, and the second a street or part of a street in that area. The postcode B422SU, for example, is split into 'B42' (an area in Birmingham) and '2SU'.

The second part of a UK postcode is *always* three characters - but the first part can be two, three, or four characters. Once you know that, you know that you can deduce the length of the first part by the length of the whole.

Let me explain what I mean: if the postcode is five characters long in total, then the first part is two characters (5 minus the 3 characters in the second part). If the postcode is six characters then the first part of it is three characters long; and a seven character postcode has a four-character first part.

Telephone numbers are similar: although area codes might be three, four or five characters long, we might be able to assume that the local number always takes up the final six digits.

Many other codes share similar characteristics. It's just a case of identifying them.

So: how do we work out the total number of characters in the postcode or telephone number? A function called `LEN`.

`LEN` will tell you the number of characters in a given cell - the *length* of that cell, in other words, spaces included. It only uses one parameter: the cell you want to measure, like so:

`=LEN(A2)`

You can use `LEN` to calculate the number of characters you need in a more sophisticated `LEFT`, `RIGHT` or `MID` function in one of two ways:

- Create a new column for the length of each cell, and use the relevant cell in that column for each `LEFT`, `RIGHT` or `MID` function.
- Use `LEN` *within* a `LEFT`, `RIGHT` or `MID` function, as a nested function.

For example: if we had our postcodes in column A, we might write the following formula in B2 to calculate how many characters the *first* part of each postcode should be:

`=LEN(A2)-3`

For any seven character postcodes, this will return `4` (seven minus three); for six character postcodes, `3`, and for five character postcodes `2`.

In column C, then, we can use that cell within a formula using the `LEFT` function like so:

`=LEFT(A2,B2)`

In other words: grab characters from the left in cell A2, for the number of characters specified in B2.

The *nested function* version of this would bring the `LEN` function directly into the formula without needing an extra column, like so:

`=LEFT(A2,LEN(A2)-3)`

In other words: grab characters from the left in cell A2, for the number of characters that you get by taking the length of A2 and subtracting 3.

You can use the same logic with the `MID` function or `RIGHT` function.

### What if the starting position or number of characters *depends*? Part two: SEARCH and FIND

Sometimes it is not the *length* of a code which determines how much you need to grab, but a particular character or characters *within* it.

Let's say, for example, that we have a collection of spending codes where the department code is always prefixed by a 'K'. All we need to know is 'at what position does the character K occur?' and then we can grab the characters following that.

The `SEARCH` function tells us just that: it searches for a specified character or characters in a specified cell, and returns a number for its position in that cell.

If cell A2 contains the code 123K45, then, we might use the following formula to tell us what position the K appears in:

`=SEARCH("K",A2)`

The function needs just two parameters: the characters being searched for; and the cell being looked in.

The result here is `4`, which can be used as the basis for a `MID` function or `RIGHT` (subtracting 4 from the length of the cell in question would give us the number of characters to grab from the end to get everything up to that point. We'd need to add 1 to include the K too).

The same function can be used to look for names: `=SEARCH(A2, "Smith")` will return 6, for example, if A2 contains "John Smith".

There is a third, *optional*, parameter for the `SEARCH` function: *where to start looking*. This is useful if you want to search more specifically within the last few characters of a cell.

If the specified character/s are *not* in the specified cell, you will get a `#VALUE!` error.

`SEARCH` is not case sensitive, so if you want to be a little fussier you can use the very similar `FIND` function. This has exactly the same parameters: what you're looking for; where you're looking; and an optional third parameter specifying what position you want to search from. But if you're searching for 'M' and it only has an 'm', the result will be a `#VALUE!` error.

<aside class="warning blurb">

For languages that support double-byte character sets (DBCS) such as Japanese, Chinese (Simplified), Chinese (Traditional), and Korean you can also use functions like `MIDB`, `LEFTB`, `RIGHTB`, `LENB`, `REPLACEB`, `SEARCHB` and `FINDB` functions which count each double-byte character as 2.

</aside>
<aside>

### Extracting characters by getting rid of the others: REPLACE

An alternative to using `LEN` to calculate the starting point of the text you want is to use a different function to get rid of the text that you *don't want*.

A useful function to that end is `REPLACE`. This will replace characters in any cell at a specified character position for a specified number of characters - rather like a reverse `MID`.

Unfortunately `REPLACE` is one of the more complex functions, requiring four parameters: the cell you want to use; what character to begin replacing from; how many characters to replace for; and what to replace those characters with.

If we had a six character code and wanted to grab the first three characters using this approach, the formula would look like this:

`=REPLACE(A2,4,3,"")`

Translated, this says: replace in cell A2, from the fourth character, for three characters, with nothing (`""`).

As with `MID` you can ensure the replacing runs to the end by using an artificially large number like 100:

`=REPLACE(A2,4,100,"")`

And like `MID`, this will not generate an error.

</aside>

### Recap

- The functions `RIGHT`, `LEFT` and `MID` will, respectively, **grab a specified number of characters from the end, beginning, or middle of a cell**.
- These can be **especially useful for codes where you just want to extract or test *part of* that code** - for example the first two digits of a telephone code, or the first half of a postcode or cost centre.
- If your data uses slashes, dashes, spaces, commas or other characters that you can split it on, *\*use the menu option \*Text to columns...* (normally in the *Data* menu) to do that. But first make sure that the column you want to split is placed in the last column of your data.
- **The `LEFT` and `RIGHT` functions have two ingredients: the cell you want to use, and the number of characters you want to grab** from the beginning (the left) or the end (the right).
- **The `MID` function needs another parameter: what character position you want to start grabbing from**. This comes second in sequence like so: 'What cell are you using, what position you want to start grabbing characters from, how many characters do you want to grab'.
- **Spaces are counted as characters too** so watch out for empty spaces at the start and end (consider using the `TRIM` function to remove them first) and remember to count them in the middle too!
- **The `LEN` function will tell you the number of characters in a given cell** including spaces, which can then be used to calculate the start or end position for a `MID`, `LEFT` or `RIGHT` function.
- **The `SEARCH` function will tell you the position of a specified character or characters in a cell**, which can then be used as the basis for a `MID`, `LEFT` or `RIGHT` function to grab characters from or up to that position.
- **The `FIND` function is the same as the `SEARCH` function, but is case sensitive**.
- **The `REPLACE` function offers an alternative option which will replace specified character positions with nothing**, leaving you everything else.

### Finding the story: how old are Guantanamo prisoners?

In the last chapter I linked to [a spreadsheet containing details on almost 800 individuals detained by the US Department of Defense at Guantanamo Bay, Cuba](https://drive.google.com/file/d/0B5To6f5Yj1iJa0xmbVNRZTdyQk0/edit?usp=sharing), and suggested some exercises in finding stories using the techniques for getting ages in Excel.

1.  You could check that the date of birth is being treated as a number by Excel in a number of ways. Firstly, by looking at the alignment: it's aligned right, which is how Excel aligns numbers. Secondly, you could right-click on the date and select **Format cells...** then reformat it as *number* or *general* - if it doesn't change to a number then it's a text string. Thirdly, you could use the function `ISNUMBER` to check if a specified cell contains a number - and copy that down a new column.
2.  A formula in column C to give us the age of each individual based on their date of birth might look like this: `=YEAR(TODAY())-YEAR(B2)-(TEXT(B2,"mmdd")>TEXT(TODAY(),"mmdd"))`. That formula has two parts: today's year minus the year of the date of birth - `=YEAR(TODAY())-YEAR(B2)` and then a TRUE/FALSE test on whether the month-day of the date of birth is greater than the month-day of today's date: `(TEXT(B2,"mmdd")>TEXT(TODAY(),"mmdd"))`. The result of that second part (TRUE = 1 and FALSE = 0) is subtracted from the first calculation.

> It will be clearer to put those two parts in two separate columns: `=YEAR(TODAY())-YEAR(B2)` in column C and `=TEXT(B2,"mmdd")>TEXT(TODAY(),"mmdd")` in column D, then combine them in a further column as `=C2-D2`.

> If you can remember the `DATEDIF` function it's much easier: `=DATEDIF(B2,TODAY(),"Y")`. That is: *give me the difference between the date in B2 and today's date, in years*.

> There's also Steve Doig's approach, which would give you an age including decimal places. That would be adapted as this formula: `=(TODAY()-B2)/365.25`. Remember not to reduce the decimal places which will round the number up!

<aside class="warning blurb">

Because the B column is formatted as a date, when you insert a new column it will use the same formatting for your results: 101 will be formatted as `04/10/00` or similar. Remember to format the cells in the new column as a number to prevent this happening.

</aside>

3: The answers above cover some of the error checking: for example, checking if someone's birth date is later than today's date, or ensuring that numbers are not rounded up. However, you'll also need some more traditional error checking: the first prisoner listed, for example, seems to have been born in 1913, making him over 100 years old. Or was he born in 2013, making him a mere baby?

> It seems Mohammed Sadiq was indeed born in 1913. [A document from the Department of Defense published on The Guardian website](http://www.theguardian.com/world/guantanamo-files/US9AF-000349DP) appears to confirm it. But whether he is over 100 - or has since died - we would also have to check.

> There are also rows towards the bottom of the spreadsheet which generate `#VALUE!` errors when you attempt to calculate an age. This is because the 'date of birth' field does not contain a date, but a string of text such as "26 yrs old in 07", "UNDISCLOSED", "UNKNOWN" or "c. 1974". Some further research might yield more information, but more likely we will have to be clear that a certain proportion of our figures are unknown.

4: The stories we might tell about these ages include: a story on the oldest prisoner in Guantanamo; a story on the youngest prisoner(s) in Guantanamo; a story on young prisoners generally - how old were they when they were arrested. Mohammed Sadiq, for example, according to that document, was 89 when he was detained in 2002. You could also write a story on the ageing section of prisoners. And of course you could chart the age distribution of prisoners from different countries: Sudanese prisoners, for example, tend to be much older than those with Yemeni citizenship. Is this because some prisoners are accused of being fighters while others are suspected of being politically powerful?

<aside class="exercise_blurb blurb">

### Find the story: what postcode areas are worst for hygiene inspections?

In [the food hygiene data you've been working on](https://drive.google.com/file/d/0B5To6f5Yj1iJeUM2VFZkaUc3MDQ/edit?usp=sharing) for the last couple of chapters is a 'PostCode' column. As explained in this chapter, UK postcodes can be anything from five to seven characters long, but the second part is always three characters.

1.  Create a new column which uses the `LEN` function to calculate the length of each postcode in turn.
2.  Create a new column which uses *that* column (the lengths of the postcodes) to calculate how long the first part of each postcode is: 2, 3 or 4.
3.  Create a third new column which uses the `LEFT` function and *that* column (the lengths of the first part of each postcode) to extract the first part of each postcode.
4.  In a fourth column try to write one *nested* function which uses both `LEN` and `LEFT` to grab the right number of characters from the left for each postcode. If it works you can delete the other three that it took to do the same job!
5.  In a further column see if you can get the same result by using the `REPLACE` function. There's no reason why you should use this more complex function instead for this particular job, but it's useful to get some experience in using it.
6.  How can you work out which postcode area appears most often?

</aside>


## Case study: When you get data in sentences: using `SEARCH` and error handling to extract numbers from phrases


In 2019 while working with the BBC Data Unit on [a story on unduly lenient sentences](https://www.bbc.co.uk/news/uk-47879288) I dealt with a spreadsheet where data was trapped in phrases: we needed to be able to take a collection of words such as "11 years and 5 months' imprisonment" and convert that into something that could be used in spreadsheet calculations (specifically, comparing the lengths of time represented by two different phrases).

It's a problem you come across every so often as a journalist --- especially with FOI requests --- so in this chapter I'll explain how we used a number of spreadsheet functions and techniques to do that.

First, here's what the data looks like:

  Original Sentence                             Revised Sentence
  --------------------------------------------- -------------------------------------
  9 years' imprisonment                         11 years and 5 months' imprisonment
  2 years' imprisonment suspended for 2 years   Sentence Unchanged
  12 years' imprisonment                        14 years' imprisonment
  22 months' imprisonment                       Sentence Unchanged

*(You can [find the data and other background in a GitHub repo here](https://github.com/BBC-Data-Unit/unduly-lenient-sentences).)*

### Break down the steps

The first thing to do in any situation like this is break down the task into its constituent problems/challenges. Well, we need to:

- Identify *where* the number of years is stated
- Extract that number of years
- Identify *where* the number of months is stated
- Extract that number of months
- Identify other context like 'suspended', 'minimum' etc.
- Convert years and months to a number
- Convert years and months to a common measure (total months)

### Identify where the years/months are detailed: using `SEARCH`

The function `SEARCH` will tell you where the first mention of a word appears. It's case-insensitive:

`=SEARCH("year",G14)`

*Translation: Search for where year appears in `I2`*

This (written in cell I2) returns a position, e.g. 4. If it doesn't find it, it returns `#VALUE`

We assume that the number of years appears 3 positions *before* that (one space, plus two digits). So we subtract 3 to get the position of the *number* of years.

`=search("year",G14)-3`

### Extract the number of years/months (and correct for problems)

If it's a single figure, we should get just the space before it, which we will deal with below. But if it's at the start of a line, we won't, and will get an error instead.

So we need a new column (L) to correct for that:

`=IF(I14=0,1,I14)`

Now nest that within a `MID` function to extract the numbers at that position:

`=MID(H14, IF(I14=0,1,I14),2)`

This grabs characters from that position, and continues grabbing for 2 characters.

However, this might also grab spaces if only one character is a digit.

### Handling an unnecessary space

To correct that unnecessary space, and make sure the result is formatted as a number, nest this again in an `INT` function (which turns a value into an integer):

`=INT(MID(I2, IF(K2=0,1,K2),2))`

We could use the `TRIM` function, which removes trailing and leading white space, but this would not change the *type* of data that the space surrounds.

Note that this process involves a lot of *trial and error*: our initial formula works for most cells, but we then focus on *error handling* with the cells where it does not.

You can adapt and repeat the above two processes for months, weeks and days - and also for the revised years, months and so on - to get the numbers you need.

### Converting to a common measure

Once you have columns extracting the numbers of years, months, weeks and days you need to be able to convert them to a common measure in order to perform any calculations. How much longer, for example, is 1 year and 2 months, than 0 years and 5 months?

The simple way to do this is to **convert all measures to the lowest common denominator**.

In this case that would be *days*, so:

- Multiply the years figures by 365 to get days (we could use 365.25 to account for leap years, but it's not relevant)
- Multiply the months by 31 (again, we don't need to use a decimal to account for the fact that month lengths vary - we only need a consistent figure that allows us to calculate differences)
- Multiply the weeks by 7

Once this is done, we can add up all those figures for each sentence to get a total number of days for that sentence.

Repeat for the revised sentence and you now have two figures that you can compare to get a new figure: the **difference** between the two sentences.

That difference can now be averaged (for example, the average change in sentence by offence), and converted accordingly (years, months and weeks) if needed.

### Manual cleaning: identifying unusual words

It's worth adding a column which just measures the length of the description cell, so you can sort it and pick out outliers:

`=LEN(I2)`

The longest cell on that basis is this one:

> *"4 years and 6 months' imprisonment with a licence extension of 2 years and 6 months"*

These unusual entries may contain more than one mention of the word being searched for ("years") or extra caveats which are important to factor in.

You decide to add a column checking for those key words:

`=COUNTIF(I2,"*licence*")`

This will count 1 if 'licence' is in that cell, or 0 if it is not. The asterisks are wildcards which mean 'any or no characters'.

### Adding a 'checking' formulae

You can use the same function to check whether a sentence mentions years or months:

`=COUNTIF(I2,"*year*")`

Any `0` value should *also* match any `#VALUE` error in your earlier `SEARCH` formula that looked for "year".

You can use filters to check that they all do, and investigate any that don't.

This may lead you to extra cleaning steps, or in most cases you might decide it is quicker to manually correct or clarify those entries.

<aside>

### Sometimes hard work ends up left out of the story

Despite all this work to extract the numbers from the data, in the end it was decided to leave this dimension out of the eventual story, as it became clear that the article was going to focus on the proportion of requests which were not eligible for review.

It's important to mention this because often in journalism --- and not just in data journalism --- you have to be prepared to leave out material because the focus of your story has changed, regardless of the work that went into it. Ultimately it doesn't matter how much work something involved: if it's not central to the story, then it shouldn't be there.

</aside>

### Key points

- Phrases like "10 years and 7 months" contain data, but it **needs to be extracted** in order for you to perform calculations, filter or sort.
- Extraction will often involve more than one step, so **try to break down the steps that you will need to perform** in order to get the data in the format needed.
- **Error handling** involves identifying errors generated by some of your formulae, and adapting the formula to handle those problems. The `IF` function is particularly useful for this, as you can specify what to do *if* your formula generates a particular type of result (you can combine it with error identifying functions like `ISERR`)
- When converting text to numbers remember that **spaces are text characters too**.
- You can **ensure that numbers are treated as numbers by using `INT` (for a round number, or integer) or `VALUE`**
- Add **checking formulae** that test your results in another way: above, for example, we used `COUNTIF` to correlate whether errors on a `SEARCH` for "year" matched up with a `0` result on a `COUNTIF` looking for the same thing.



## Putting names, addresses and other data back together: `CONCATENATE`, `&` and adding special characters with `CHAR`

In the previous chapters we've looked at extracting parts from, or splitting, data such as postcodes, names, codes and phone numbers. However, you may have the opposite problem: data which is already split but which you wish to combine: area codes and phone numbers; 'Address 1', 'Address 2' and 'Address 3'; forename and surname.

The `CONCATENATE` function can do this for you: it will take any cell references and strings provided as arguments (in the parentheses) and join them together.

The formula `=CONCATENATE(M2,N2)`, for example, will grab the contents of cell M2, and then cell N2, and give you the combined result. If M2 contains "Paul" and N2 contains "Bradshaw" then the result will be "PaulBradshaw".

You can give the formula as many ingredients as you want. It can be as simple as `=CONCATENATE(M2)` (kind of pointless, but anyway...) or as complex as `=CONCATENATE(M2,N2,A2,B2,O2,C2,P2,Q2,R2)`.

As you may have spotted, the problem with `CONCATENATE` is that spaces are often not included in the data. We don't want "PaulBradshaw"; we want "Paul Bradshaw".

This can be solved by adding *strings* of characters as extra ingredients instead of cell references. To grab M2, then a space, and then N2 you would need to adjust your formula like so:

`=CONCATENATE(M2," ",N2)`

Note that the string (in this case just a space) is in quotation marks. If you want to *add* quotation marks use a unique character that you can then replace using *Find and Replace...*. Here, for example, a 'pipe' symbol has been inserted:

`=CONCATENATE(M2,"|",N2)`

You can also add single quotation marks as an alternative:

`=CONCATENATE(M2,"'",N2)`

If you're adding characters like this it may be worth adding an extra column containing those characters, and using those in your formula instead. For example, if you filled column O with a quotation mark (type one in the first cell and copy down) then your formula could then be written like so:

`=CONCATENATE(M2,O2,N2)`

<aside class="tip blurb">

### Adding unusual characters: `CHAR`

If you want to add characters like quotation marks or ampersands without them being treated as operators you can also use the `CHAR` function. This generates a character based on its number within a system used by your computer to encode text. There are 255 of these: an upper case A, for example, is number 65, while the lower case a is number 97.

This number is given as an argument in parentheses after `CHAR`. For example, the number for a quotation mark character is 34, so `=CHAR(34)` will generate a quotation mark, and `=CONCATENATE(M2,CHAR(34),N2)` nests the same results inside a `CONCATENATE` function.

You can use the same function to generate unusual symbols such as those for 'trademark' (TM) - `CHAR(170)` - 'registered trademark' (R) - `CHAR(168)` - and copyright (C) - `CHAR(169)`. The 'degrees' symbol can be generated with `=CHAR(161)` and a 'paragraph' symbol with `=CHAR(166)`


Some of the character codes and the associated characters


Conversely, if you want to find out what the code is for any particular character, you can use the `CODE` function to do so. The formula `=CODE("&")`, for example, returns `38` - the code for an ampersand symbol.

When used on cell references it will return the code for the *first character* in that cell. So, if cell A1 contains the word FALSE, `=CODE(A1)` will return `70` (the code for the character F).

</aside>

### The alternative to `CONCATENATE`: `&`

You can achieve the same result as `CONCATENATE` by simply using the `&` operator. This formula, for example, grabs and concatenates M2 and N2:

`=M2&N2`

And this one concatenates M2, a space, and N2:

`=M2&" "&N2`

Some prefer one approach, some the other. I'll leave you to decide.

### Recap

- **The `CONCATENATE` function will combine the contents of one or more specified cells and/or specified strings of text**, each part separated by a comma, like so: `=CONCATENATE(M2,N2,O2)`
- **If you want to add spaces to the resulting concatenated text, you'll need to include those as ingredients in the function** (e.g. `=CONCATENATE(M2," ",O2)`), or put the spaces in another column whose cells you use in the formula.
- Because quotation marks are used to *indicate* a string, **if you want to *add* quotation marks you'll need to put those in a cell and refer to that**, or use the `CHAR` function.
- **The `CHAR` function can be used to add problematic characters such as quotation marks, as well as special characters like the copyright symbol**, like so: `=CHAR(34)`.
- If you need to work out which code to use, **the `CODE` function can be used to find out what code you need to use to generate a particular character**, e.g. `=CODE(A2)`.
- If there is more than one character in a cell **the `CODE` function will give you the code for the *first* character**.

### Tell the story: finding special characters

Create an empty sheet and select the first cell (A1). Use the **Edit \> Fill \> Series...** menu option detailed in the chapter on ranges to generate a range from 1 to 255 in that column.


In B1 write a formula to use that first number (1) as the basis for a `CHAR` function to generate the character encoded as number 1. That formula should be `=CHAR(A1)`

Copy that formula down the entire B column, so it repeats the process for cell A2 (the number 2), down to A255 (the number 255). In B255, then, the formula should read `=CHAR(A255)`

Browse the characters generated to see if any are of interest or use (`CHAR(240)` is an Apple symbol? 189 is the symbol for Omega; 198 for Delta). Save a copy so you can always refer to it later.

In the C column use the `CODE` function to find out the code for each character in the B column, i.e. put the formula `=CODE(B1)` into C1 and copy down the column. These codes should be exactly the same as the numbers in column A.

The `CHAR` and `CODE` functions are particularly useful when wishing to test for upper or lower case characters (which have different codes). We'll cover this in the next chapter but in the meantime try to work out two challenges:

- How might you use this knowledge to test if a character is upper or lower case?
- And how might you use it to *convert* a character from upper to lower case, or vice versa?

<aside class="exercise_blurb blurb">

### Finding the story: what postcode areas are worst for hygiene inspections?

In the last chapter I suggested using `LEN` and `LEFT` to grab parts of postcodes for food hygiene inspections. Here are the solutions:

1.  A formula using the `LEN` function to calculate the length of each postcode in turn would look like this: `=LEN(J2)` (if you created a new column after the postcodes - the cell reference may be different if you created it before).
2.  A formula which used *that* column (the lengths of the postcodes) to calculate how long the first part of each postcode was would look like this: `=K2-3` (assuming the K column contained your `LEN` formulae).
3.  A formula which used the `LEFT` function and *that* column (the lengths of the first part of each postcode) to extract the first part of each postcode would look like this: `=LEFT(J2,L2)` (assuming the L column contained the previous calculation).
4.  A *nested* function which used both `LEN` and `LEFT` to grab the right number of characters from the left for each postcode would look like this: `=LEFT(J2,LEN(J2)-3)`
5.  To get the same result by using the `REPLACE` function you would write a formula like so: `=REPLACE(J2,LEN(J2)-3,3,"")` - this uses the `LEN` function to calculate the *position* it needs to start replacing from: that is, the position 3 characters from the end (length minus 3).
6.  You can work out which postcode area appears most often by using a pivot table and placing the postcode area field in your 'rows' box and 'data' box. You can also use `COUNTIF` to count how many cells in the column contain a particular postcode.

</aside>


## More data cleaning: formatting text or numbers consistently with `UPPER`, `LOWER`, `PROPER` and `FIXED`


This map by the Center for Investigative Reporting needs locations formatted as ‘proper’ case


For this chapter I want to take a brief detour into a few simple formatting functions, firstly: `UPPER`, `LOWER` and `PROPER` for text, and then `FIXED` for numbers.

`UPPER`, `LOWER` and `PROPER` allow you to take the contents of any cell and format it consistently as either all upper case, all lower case, or all 'proper' case: that is, where the first letter in each word is capitalised.

Consistent formatting can be important both in the presentation of information and in trying to combine it.

For example: if you have a story where you expect to use the original data for a map or chart, the labels and legends will need to be clear and consistent. A map with 'PARIS' for one marker and 'new york' for another is going to look pretty unprofessional.

Likewise, because computers sometimes treat a lower case letter and an upper case letter as separate things, you might come across errors when trying to merge one dataset which uses 'Monsanto' and another which uses 'monsanto'.

Prevention is always better than cure.

All three text formatting functions have one ingredient: the cell you want to format as upper, lower or proper case. If you want to take whatever is in A2 and see it entirely in upper case the formula would be this:

`=UPPER(A2)`

If you wanted to see it in entirely lower case:

`=LOWER(A2)`

And it you wanted each word to begin with a capital, and the other letters to be lower case:

`=PROPER(A2)`

If A2 contained the name 'Mr jones' the results would be as follows:

- `=UPPER(A2)` : `MR JONES`
- `=LOWER(A2)` : `mr jones`
- `=PROPER(A2)` : `Mr Jones`

In most cases you'll want to use `PROPER` - but there may be instances where `UPPER` is more appropriate (such as postcodes and other codes - check that case is not significant). `LOWER` is least likely to be useful *on its own*. However, it can be a useful first stage in formatting text - as we'll come onto.

As with `TRIM` and `SUBSTITUTE` it's a good idea to create a new column for your 'cleaned' data, write a formula using `PROPER`, `UPPER` or `LOWER` to grab and format the contents of the first cell, and then copy it down the entire column.

<aside>

### Encoding and decoding text: making *just* the first character capitalised

You *can* make just the first letter of any cell capitalised by combining `LOWER` with `CODE` and `CHAR` and `MID`. This is a bit geeky but a good way to begin to look at text in the same way computers do.

With challenges like this, it's worth breaking down the problem first:

1.  We need to convert a cell to entirely lower case
2.  We then need to convert the first character to upper case
3.  And combine that with the characters from the second position onwards in the lower case version

Here's a formula which does all of that:

`=CHAR(CODE(LOWER(F5))-32)&MID(LOWER(F5),2,100)`

So what's going on here?

The `&` character in the middle is useful to identify as joining the results of two formulae. We can look at each separately.

1.  The first part, for example, uses three different functions. In the middle the `LOWER` function gets us a lower case version of whatever is in F5
2.  This is then used by the `CODE` function to find out the code for the first letter.
3.  The formula subtracts 32 from that figure to give us a code for its *upper case* equivalent. This is because the codes for upper and lower case characters are 32 places apart: a capital A is encoded as character number 65; a lower case a is encoded as character number 97; B and b are 66 and 98 respectively; and so on.
4.  That code is then used by the `CHAR` function to generate that upper case equivalent.

The second part of the formula, after the `&`, only uses two functions: in the middle, `LOWER` once again gets a lower case version of the contents of F5.

This is then used by the `MID` function to grab the text from the second character onwards, for 100 characters. Assuming it is never longer than 100 characters, this effectively means 'all characters from here'.

There's an alternative approach which might be described like this:

1.  We need to grab the first character of an upper case version of the cell
2.  And we need to grab the second character on of a lower case version of the cell
3.  Then combine the two

Here's *that* formula:

`=LEFT(UPPER(F6),1)&MID(LOWER(F6),2,100)`

This is a little easier to explain:

1.  Use `UPPER` to grab F6 and format it as all upper case
2.  Use the results of that as an ingredient for a `LEFT` function, which just grabs the first character from the left (i.e. the first capital letter).
3.  Add this using the `&` operator to the results of the next part:
4.  Use `LOWER` to grab F6 and format it as all lower case
5.  Use the results of that as an ingredient for a `MID` function, which grabs all characters from the second position onwards

A much simpler alternative is to avoid trying to do everything in one formula and instead create two separate columns - one to grab the first character and format it as upper case (`=UPPER(LEFT(F6,1))`) and one to grab the rest of the characters and format them as lower case (`=LOWER(MID(F6,2,100))`) - and then a third to combine the two (using `CONCATENATE` for example).

</aside>

### Rounding and formatting numbers: `FIXED` and `ROUND`

The `FIXED` and `ROUND` functions perform a similar formatting role with numbers: both will take the contents of any cell and give you that value to a specified number of decimal places.

Each function needs two ingredients: the cell you want to use, and the number of decimal places.

With `FIXED` there's also an optional third parameter: whether you want to omit commas from the result. This parameter only makes a difference if you are working in a language which uses commas to indicate decimal places (UK English doesn't). Put TRUE if you want commas to be omitted, or FALSE if you don't - if you do neither it will assume FALSE anyway.

One difference between the two functions is that `FIXED` will *always* contain the number of digits you specify; whereas `ROUND` will not add digits where they don't exist.

For example, if A2 contains the number 3, the formula `=FIXED(A2,1)` will give you `3.0`, the formula `=FIXED(A2,3)` will give you `3.000` and so on.

However, the formula `=ROUND(A2,1)` will give you `3`, and the formula `=ROUND(A2,3)` will also give you `3`. It will not add any more decimal places than the number originally had.

If A2 contains the number 3.1457, either of the formulae `=FIXED(A2,0)` or `=ROUND(A2,0)` will give you `3`, and either of the formulae `=FIXED(A2,2)` or `=ROUND(A2,2)` will give you `3.15` and so on.

If you wanted to omit commas you would add `,TRUE` at the end of the `FIXED` formiula like so: `=FIXED(A2,2,TRUE)`

Of course you could achieve the same *effect* by using the **Format cells** menu outlined in previous chapters, selecting *Number*, and specifying the decimal places there. However, `FIXED` and `ROUND` do not just create the *effect* of rounding numbers up or down: the resulting number is indeed *fixed*: 3.1457 is now 3.15 - if you add 1 to that number and format it to show four decimal places it is 4.1500, not 4.1457.

If you try to use `FIXED` or `ROUND` on a cell containing a word, it will return a `#VALUE!` error, meaning you are trying to use it with the wrong type of data.

However, if you use it with TRUE or FALSE, it will treat it as a 1 or 0. The formula `=FIXED(TRUE,3)` will give you `1.000`, for example. And `=FIXED(FALSE,1)` will give you `0.0`.

### Showing figures as millions or billions without all the zeroes

A similar situation where **Format cells...** comes in handy is where you have particularly long figures - for example numbers in the millions - and want to display them as '\$3m' rather than the full seven-digit version.

To do this, select the data you want to format and open the formatting window by selecting **Format \> Cells...** or using the keyboard shortcut CTRL+1 or CMD+1.

When the window appears, select the *Custom* option on the left (at the bottom).

As with custom date formatting, there are particular symbols and characters here that will do particular things:

- The hash symbol `#` is used to indicate the number this is affecting.
- Each comma symbol `,` is used to indicate that the number should be truncated to the nearest thousand (if one is used) or million (if two are used) or other multiples such as billions, trillions etc (more commas). For example `#,` will turn 3,000,000 into 3,000 and `#,,` (two commas) will turn 3,000,000 into 3.
- Each period symbol `.` is used to indicate whether to add decimal places - hashes after this indicate how many decimal places to run to.
- A currency symbol will be added to the figure wherever you put it.
- Other characters will need to be placed in quotation marks - for example "m" or "M" if you want to add that letter to indicate 'million'.

Using these symbols together, if you want to format a number like 3,457,900 into '£3m' you would enter the following in the box under *Type:*

`£#,,"m"`


This means:

- Insert a pound symbol
- Followed by the number
- Truncate it to the nearest million (two commas)
- Add the character 'm' at the end

Click **OK** and you should see that formatting now applied to the cells you selected.

Of course any figures below a million are now not going to show at all. But we can adapt the formatting a little further to help.

The solution is to *add decimal places* to our rounded figure. This will show anything below one million as a proportion of millions (i.e. 500,000 would be 0.5 million and 3,400,000 would be 3.4 million).

To do this, return to the **Format cells...** *custom* menu and add a period after the hash, followed by two *further* hashes (to indicate two decimal places) like so:

`£#.##,,"m"`

This means:

- Insert a pound symbol
- Followed by the number
- Followed by a decimal place
- Followed by two decimals
- Truncate the main number (before the period) to the nearest million (two commas)
- Add the character 'm' at the end

Try adapting your custom formatting to this. Now instead of '£3m' it should show '£3.46m'. Any figures lower than a million will be displayed with a zero before the decimal place, for example '£0.63m' or '£0.01m'.

### Recap

- **Consistent formatting can be important both in the presentation of information and in trying to combine it**.
- **The `UPPER` function will take the contents of any cell and give you it SHOUTING IN CAPITALS!**
- **The `LOWER` function will take the contents of any cell and give you it all in lower case**.
- **The `PROPER` function will take the contents of any cell and give you formatted so the first letter of each word is capitalised, with the others lower case**.
- When combined with functions like `LEFT` and `MID`, `CHAR` and `CODE` you can convert lower case characters to upper case, and vice versa.
- **The `FIXED` function will take the contents of any cell and give you it formatted to a specified number of decimal places**.
- `FIXED` does not just change how many decimal places are shown for a particular number - **it permanently rounds that number up or down**. Any further decimal places no longer apply, regardless of formatting applied.
- **If you try to use `FIXED` on a cell containing a word, it will return a `#VALUE!` error**.
- **If you use `FIXED` with a cell containing TRUE or FALSE, it will treat it as a 1 or 0**.
- **You can round numbers to the nearest million, billion, etc. by using the *Format cells...* option and the *Custom* section**.
- **You can also specify that those rounded numbers should include decimal places for 'parts of a million/billion/etc'** by using the period character in the same section.



## Changing rows into columns, and vice versa: `TRANSPOSE`

Sometimes your formatting problem is more than just whether words are upper or lower case - sometimes the whole table of data is the wrong way round: your columns should be rows and the rows should be columns.

There is a quick way to solve this in Excel - but it's not easy to find. It's called **transposing**.

Transposing is the process of switching rows into columns and vice versa. Here's an example of one typical table before transposing...


...and here's the same table after it has been transposed:


<aside class="warning blurb">

You'll note the transposed table is in different rows to the original. This is because in Excel you cannot paste on top of the original data when transposing. In Google Sheets, however, you can.

</aside>

There are two main ways of transposing data in Excel, and two ways of transposing in Google Sheets too. I'm going to start with the hardest way to transpose first, and then explain the easier methods.

### The `TRANSPOSE` function in Excel - for when you need data to always be transposed

There is a function for transposing data in Excel - but it's extremely complicated to employ.

Not surprisingly, the function is called `TRANSPOSE`. It takes just one argument - the range of cells you want to transpose - but there are two extra requirements that increase the complexity considerably:

1.  You must select the range of cells you wish to transpose into, rather than just one cell. This means you must know how many rows and columns your transposition is going to take up, and makes it unsuitable for large transpositions.
2.  The formula must be entered as an **array**. This means holding down CTRL+SHIFT+ENTER before finishing the formula to make it an **array formula**. Curly brackets will be added to indicate this, so the final formula will look like this in your formula bar: `{=TRANSPOSE(A1:B3)}`

I'll explain **array formulae** further in a separate chapter. However, one thing you do need to know now is that **you cannot create an array formula by simply typing the curly brackets yourself** - you *must* hold down CTRL+SHIFT+ENTER to convert the normal formula.

For this reason the array formula is also referred to as a '**CSE formula**'.

The *full* process for using the `TRANSPOSE` function for a three-rows-by-two-columns range of cells would go like so:

1.  Firstly, **click and drag to select the right range of cells to contain the *results* of your transposition**. In this case, 3 rows by 2 columns is going to transpose into 2 columns by 3 cells.
2.  Second, **with those cells still selected, begin typing your formula** (see image below).
3.  Finally, once you have finished typing the formula - but before pressing ENTER - **hold down CTRL+SHIFT+ENTER** (CSE) to turn it into an array formula by adding curly brackets around it.


An appropriate range of cells must be selected when you begin typing the TRANSPOSE formula


That formula will then be applied across those six cells, transposing accordingly.

What a convoluted process!

For that reason, I'd advise doing things this way *only if none of the other ways work for your purposes*. The same function in Google Sheets, for example (explained below), doesn't require any of that CTRL+SHIFT+ENTER nonsense - but you may not have access to, or wish to, use Google Sheets. And the paste-and-transpose approach explained later is a once-only process which doesn't continue to transpose once old data is overwritten.

The one major advantage of the `TRANSPOSE` function is that it will transpose *new* data when it is entered in the specified cells. The major disadvantage is that you need to select the right number of rows and columns for the transposed data. The bigger the range of cells, the harder this gets.

That isn't a problem for Google Sheets, however...

### The `TRANSPOSE` function in Google Sheets - no need for keyboard shortcuts

**Google Sheets**' version of the `TRANSPOSE` function requires no keyboard shortcuts, and **you do not need to select all the cells to be transposed into**.

Instead, you can use `TRANSPOSE` just as you do any other function, like so:

`=TRANSPOSE(A1:B3)`

Once you have type the formula and pressed ENTER, the transposed data will appear, with the first cell in the cell containing the formula, and the others appearing outwards from there.

If the cells below or to the right of that cell contain any data, **that data will be overwritten**. This is the key distinction between Excel and Google Sheets: Excel forces you to specify the cells to be overwritten so you know what's going to happen; Google Sheets is a little more cavalier.

If you get things wrong you can also 'Undo' your action, of course, but **it's always worth making sure that you transpose into an empty section of your spreadsheet** - even a new workbook.


Transposing in Google Sheets


A later chapter on Google Spreadsheets will go into more detail on how to set it up and some of the functions you can only use in that package.

### The Paste Special option: the one-off transpose

Perhaps the simplest way to transpose data is to avoid functions entirely. Instead, the **Paste Special...** menu offers an option to transpose at the same time as pasting cut or copied data.

<aside class="warning blurb">

As always, you should save a copy of your data before altering it. You may want to copy data from one sheet, and paste-and-transpose into a new sheet, so as to keep the two versions separate.

</aside>

1.  Select the data you want to transpose, and copy it using CTRL+C or **Edit\>Copy**.
2.  Select the cell where you want to begin pasting the transposed data. Remember that it will overwrite cells below and to the right, so this is best done in a new sheet.
3.  Select **Edit \> Paste Special...** and a new window should appear. ![](images/pastespecial.png){style="width: 143px"}
4.  On this window, tick the box marked *Transpose* towards the bottom. ![](images/missing.png){style="width: 28px"}
5.  Click **OK** and the transposed data should be pasted where you selected.

The same option is also available in Google Sheets, with the difference that you can paste data over the top of the copied data, which Excel will not let you do.

### Recap

- **Transposing is the process of converting rows to columns and vice versa**. A table with two columns and ten rows, for instance, when transposed would take up ten columns and two rows.
- You can transpose data in a spreadsheet by **using either the `TRANSPOSE` function or the Paste special \> transpose option**.
- When using the `TRANSPOSE` function in Excel **you must first select the range of cells to transpose into, then type the formula with those cells still selected**. You **must also hold down CTRL+SHIFT+ENTER to make it an array formula**.
- When using the `TRANSPOSE` function **in Google Sheets there is no need for keyboard shortcuts or an array formula**: you only need to type the formula in the cell where you want the transposed data to begin.
- However, **remember that in Google Sheets any data after the cell containing the formula may be overwritten with the transposed data**.
- You can also perform a one-off transpose by copying the data you want to transpose and **ticking the *Transpose* box in the *Edit \> Paste Special...* menu.**

<aside class="exercise_blurb blurb">

### Find the story: when's the worst time to turn up at hospital?


This story started with transposing data


To show how these techniques can come in useful, [download this data on waiting times at hospitals' Accident and Emergency (A&E) departments](https://drive.google.com/file/d/0B5To6f5Yj1iJTk9LV2tXTm5PWW8/edit?usp=sharing).

In this data each *row* is used for a different hospital trust, and each *column* is used for a different hour period.

If we wanted to *sort* the data to see the longest wait time for a particular hospital, we couldn't - because sorting works by columns. All we can sort at the moment is a particular hour: we can see what the longest or shortest wait is for a given hour, across *all* hospitals. But if we wanted to see what the longest wait was for *one* hospital, we can't.

Transposing the data solves this problem: when rows become columns we can pick the column for one hospital, and sort it. Download the data and transpose it into a new sheet in your workbook, then see if you can do the following:

1.  Sort the column for North West Strategic Health Authority to see which is the worst hour for long waits
2.  Sort the column for Alder Hey Children's NHS Foundation Trust - one of the trusts within that authority - to see whether their worst hour is the same as the region.
3.  Sort the column for ENGLAND overall to see what the worst hour is nationally.
4.  Now you can write a story about the worst hour for waits at one local children's hospital - and also put it into local and regional perspective.
5.  What considerations need to be made when telling this story?

</aside>


## Repeating calculations across multiple cells or to create the ingredients of a single function: array formulae

In the chapter on the `TRANSPOSE` function we introduced the concept of the **array formula**. This is a formula which **performs a calculation repeatedly**, with the results often displayed across an appropriate range of cells (e.g. 10 cells for a calculation repeated 10 times).

However, the results of those calculations can also be used as the basis of a function (e.g. `SUM` or `AVERAGE` those 10 results), with the overall result shown in just one cell. This makes more sense when explored through the examples below.

An array formula is indicated by curly brackets either side in the formula bar, like so: `{=TRANSPOSE(A1:B3)}`

But **you cannot type the curly brackets yourself**. Instead the brackets must be generated with a particular keyboard shortcut, as follows.

To create an array formula **you must hold down CTRL+SHIFT+ENTER** once typed. For this reason it is also referred to as a '**CSE formula**'.

### Arrays in practice: back to the drunk and disorderly data

To show how arrays work I am going to return to some data we worked with back in the chapter on basic calculations: [drunk and disorderly arrests](https://docs.google.com/spreadsheets/d/1iUMiNs7P5P1mEQXwsFDgIn8dF5ZnO4YhRcAEMsmciVI/edit?usp=sharing).

In that chapter you used a basic calculation to subtract 2011's December arrests figure from 2012's. You can perform that calculation for all 12 months and show the results in 12 separate cells by using an array formula as follows:

1.  Select the 12 cells where you want the results to appear. The obvious cells to select are D2 through to D13.
2.  With those 12 cells selected, type the following formula - but *don't press ENTER yet*: `=C2:C13-B2:B13`
3.  Now press **CTRL+SHIFT+ENTER**. Curly brackets will be added around the formula so that it looks like this in the formula bar: `{=C2:C13-B2:B13}` - and all 12 cells should now be filled with the results of 12 different calculations.


Type the array formula with all twelve cells selected


What is going on here? Well, the formula identifies two ranges of cells: C2:C13 and B2:B13. The 'minus' operator subtracts one from the other. But how can you subtract one range from another?

When entered in an array formula that cell range is treated as a *list to go through*. If each range contains 12 cells then it will perform 12 calculations, starting with the first item in each list, and continuing until the last item in each list. The operator determines what it does with each item.

In practice, then, it does the following:

- C2-B2
- C3-B3
- C4-B4
- C5-B5
- C6-B6

...and so on until C13-B13

If you replaced the minus sign with a multiplication operator, it would multiply each item in the first cell range by each item in the second cell range, in turn.

The same process could be used to multiply each number within a range by 10, in turn, by selecting 12 cells and typing the following formula:

`=C2:C13*10`

...Pressing CTRL+SHIFT+ENTER at the end to turn it into an array formula:

`{=C2:C13*10}`

Now it does the following:

- C2-10
- C3-10
- C4-10
- C5-10
- C6-10

...and so on. You get the idea.

### Changing or extending an array formula

Once you have created an array formula **you cannot delete it by simply selecting and deleting the first cell in which it appears**. Instead you must select *all* the cells which you originally selected when you typed it. Then right-click and select **Clear Contents**.

This complication has the advantage of protecting your array formula from accidental deletion - but it also makes it difficult to delete should you need to (the simple option is to delete the columns).

If you want to *change* your formula then you must:

1.  Select all the cells first before editing the formula
2.  Change the formula
3.  Remember to press CTRL+SHIFT+ENTER at the end to keep it as an array formula.

To **extend the formula** you must not only select all the cells, but also *any cells you wish to extend the formula into*.

For example: say we wanted to extend our array formula `{=C2:C13*10}` so that it included C14. We would need an extra cell to show the results of the extra calculation.

Originally the array formula was created by selecting cells D2 to D13: twelve cells for the twelve results.

To change the array, select the cells D2 to D14: this includes those cells covered by the array formula, but also one extra.

Then, in the formula bar edit the formula so it reads

`=C2:C14*10`

And then press CTRL+SHIFT+ENTER to make it an array formula:

`{=C2:C14*10}`

The results should now fill all *thirteen* cells selected for the array formula - including the result of the calculation using the thirteenth item in the array C2:C14.

In most cases array formulae perform the same function as copying a formula down or across a number of cells. However they can also be used in combination with functions to add up or average the results of doing so, as we'll see.

### Multiple calculations with one result: using an array formula in a single cell

The examples above involve using *one* array formula to calculate **multiple results** - for example the twelve results generated by multiplying twelve numbers by twelve other numbers, each in turn; or the ten results generated by dividing ten numbers by the number 365.

But you can *also* use an array formula to generate just **one result** using the same calculations: for example, the result of multiplying twelve numbers by twelve other numbers each in turn, *and then adding up all those results*; or the result of dividing ten numbers by the number 365 *and then averaging those ten numbers*.

Often these involve introducing a function. Here's one example which adapts our previous array formula - which produced twelve results - to create a new array formula that generates only one result: the result of calculating an average of those twelve numbers.

`{=AVERAGE(C2:C13-B2:B13)}`

The process of typing this formula is the same as before: type it in full without the curly brackets like so...

`=AVERAGE(C2:C13-B2:B13)`

...but instead of pressing ENTER press the keyboard combination CTRL+SHIFT+ENTER to indicate that you want the ranges to be treated as arrays. The curly brackets will be added in the process.

If you *don't* press CTRL+SHIFT+ENTER the formula doesn't work, and you will get a `#VALUE!` error.

Because this formula only generates one result, **you don't need to select multiple cells** before you type it. If you do, that single result will be repeated in every cell.

As this formula is that bit more complex it's worth clarifying exactly what it is doing, step by step:

1.  Start in the parenthesis: `(C2:C13-B2:B13)`. Here we have two *arrays* (lists): the twelve numbers in the range C2:C13, and the twelve numbers in the range B2:B13.
2.  The minus operator between those two arrays indicates that you want to take each number in the first range and subtract it from each number in the second range, in turn. This will create *twelve results*: C2-B2, C3-B3, and so on until C13-B13.
3.  The twelve results of those calculations are then used as the ingredient of the `AVERAGE` function to give just one average when all twelve numbers are added to together and the result divided by 12.

In this case, as it happens, the result could have been more simply calculated with this formula:

`=AVERAGE(C2:C13)-AVERAGE(B2:B13)`

Other examples might also have similarly simpler solutions.

Indeed, it may be clearer (if anyone else is going to see your spreadsheet) to split the calculation into two stages: a column showing the change for each month, then a cell calculating the average for that column.

So although array formulae are very impressive and powerful, most of the time you may decide for the purposes of clarity and simplicity to avoid them.

The most likely reason for you deciding to use an array formula is the **smaller and faster file sizes that are generated as a result**: a spreadsheet using a single array formula is smaller and quicker to use than one performing thousands of calculations separately to arrive at the same result.

However, given the power of modern computers your data would have to be very large for the difference to be noticeable.

Conversely, complex array formulae can actually *slow down* the performance of the spreadsheet. Trial and error should show you whether an array formula is making any difference for the better or worse in any specific case.

### Generating your own arrays

So far we've used array formulas to draw on the contents of cells. For example, we've created an array of twelve numbers by selecting the cell range C2:C13.

But you can also generate your own arrays of numbers by typing them directly, for example:

`={10, 20, 30}`

These are called **array constants**.

<aside>

It should be pointed out that arrays don't need to contain numbers: they can use cell references, text, TRUE/FALSE values, error values like `#N/A`, or even the results of formulae.

When using text in arrays, remember to put them in quotation marks like so: `={"Paul","John","George","Ringo"}`.

</aside>

If you thought array formulas were confusing - well, it gets worse: **those curly brackets are typed manually**.

So, you type the equals sign, then the opening curly bracket, then your array - each item separated by a comma - before the closing curly bracket. But **you must *still* press CTRL+SHIFT=ENTER to make this an array *formula***.

The result is an array constant within an array formula - *two* sets of curly brackets within each other:

`{={10, 20, 30}}`

To clarify: an array *constant* is created by *manually* placing curly brackets around the array of items. An array *formula* is created by pressing CTRL+SHIFT+ENTER once the formula has been completed, and this places curly brackets around the entire formula.

Although the two things look similar - each uses curly brackets - they are different things created in different ways.

<aside class="warning blurb">

Because array constants are different to array formulae, if you selected three cells and just typed an array constant such as `={5,10,15}`, the result would just fill just the *first* cell - i.e. only the first item in the array would be shown. The other cells would remain empty.

To make the array fill all three cells selected you would *also* need to create an array formula by pressing CTRL+SHIFT+ENTER after you had selected the three cells and entered the array. The resulting formula, then, would look like this:

`{={5,10,15}}`

</aside>
<aside>

#### Naming array constants

If you intend to use an array more than once you can create a **named array constant**. This involves creating and *naming* your array so you can refer to that name instead of typing in the array itself each time.

To create a named array constant, do the following:

1.  In Excel select **Insert \> Name \> Define...**.


1.  A window will appear with the title *Define Name*. This is where you create and name your array.


1.  The box at the top titled *Names in workbook* is where you name it. Enter a name here for your array.
2.  The box at the bottom titled *Refers to* is where you enter the array constant, or select the cell containing it. Enter an array here - for example `={365,31,7}`. Don't forget the equals operator.


1.  Click **OK**
2.  Now you can use that named array constant in any calculations, just as you would a function. For example, click in any cell and start typing


</aside>

### Array constants used in a formula

A manually created array constant is a useful alternative to arrays generated by referring to the contents of cells.

For example, let's say we had three cells - A2:C2 - containing values for a year's total, a month's total, and a week's total. We want to compare those by converting all three to a daily average.

We could use an array constant to divide each total by 365, 31, and 7 respectively like so:

`=A2:C2/{365;31;7}`

Remembering to select three cells for our results *before* typing the formula and pressing CTRL+SHIFT+ENTER to make it an *array* formula:

`{=A2:C2/{365,31,7}}`

If you selected three cells in one row before typing your array formula - that is, horizontally - then the first cell will be the result of A2/365, the second contains the result of B2/31 and the third C2/7.

But if you selected three cells *vertically*, in one column, then A2, B2 and C2 will all be divided by 365 - the first item in the array constant.

This is because array constants work in two directions: commas indicate items in a single *row*; but you can also use **semicolons** to indicate items in a *new* row.

In other words, if you wanted to display results vertically, *down* a column, you would need to use semicolons instead of commas like so:

`{=A2:C2/{365;31;7}}`

See the box below on filling ranges of cells with values for more on this.

<aside>

#### Filling ranges of cells with the values in an array

You can use very basic array formulae to fill ranges of cells with the numbers in any array constant.

Arrays using **commas** will fill cells **horizontally** from left to right.

Arrays using **semicolons** will fill cells **vertically** from top to bottom.

You can combine both commas and semicolons to fill cells in both directions.

For example, if you select three cells in one *column*, then type the array formula `{={1;2;3}}` (remembering to press CTRL+SHIFT+ENTER), it will fill the top one with `1`, the one underneath with `2`, and the bottom cell with `3`. This is because it uses semicolons.

If you select three cells in one *row*, then type the array formula `{={1,2,3}}` (remembering to press CTRL+SHIFT+ENTER), it will fill the left one with `1`, the middle one with `2`, and the right cell with `3`. This is because it uses commas.

You can demonstrate how the semicolon and commas are interpreted differently by selecting three cells in one *row*, then typing an array formula using an array constant with *semicolons* `{={1;2;3}}` (remembering to press CTRL+SHIFT+ENTER).

In this case it will fill each cell with `1`, because the semicolons indicate a vertical ordering, where the top item is always 1. If you extended the range of the array formula downwards, you would see the 2s and 3s added in the relevant rows (you cannot drag the black cross to do this - instead you have to alter the array formula as explained earlier).

You can combine commas and semicolons in an array constant to indicate their placement. For example:

={1,2,3;4,5,6;7,8,9}

This array constant shows three numbers in the first row (1,2,3) followed by a semicolon to indicate a new row underneath, then another three numbers (4,5,6), another semicolon, and a third series of three numbers (7,8,9) giving you a telephone-style grid of numbers arranged in a three-by-three grid.

Used within an array formula you would first select the three-by-three cell area to show the results, then type the array constant and CTRL+SHIFT+ENTER to make an array formula, giving you something like this:

{={1,2,3;4,5,6;7,8,9}}

</aside>
<aside class="tip blurb">

### Use TRANSPOSE to convert horizontal arrays into vertical arrays - and vice versa

You can use the TRANSPOSE function to force a horizontal array to display in cells vertically.

For example the array constant `={1,2,3}` will only work horizontally when combined with an array formula across three cells. However, selecting three cells vertically, in one column, and then typing the array formula `{=TRANSPOSE({1,2,3})}` (remember to press CTRL+SHIFT+ENTER) will transpose the horizontal array to appear vertically down those three cells.

Likewise, the result of any formula using an array constant can be transposed in the same way, like so: `{=TRANPOSE(A2:C2/{365,31,7})}`

</aside>

### Recap

- **An array formula performs multiple calculations at the same time**, often displaying the results across a range of cells rather than just one.
- Those multiple calculations are **performed against each item in the range(s) specified in the formula**, in turn, with the results being placed in each cell selected for the formula, also in turn.
- **You must select multiple cells before typing your formula** to ensure that there are enough cells for the multiple results to be shown.
- You can create an array formula with one range of cells (array) - for example multiplying each cell in that range by one number - **or you can create an array formula with more than one range of cells**, so that each item in one array is manipulated (multiplied, divided, added, subtracted etc.) by each item in another.
- **Those multiple calculations can also be used as the basis for a function such as `SUM` or `AVERAGE` by using the appropriate function with the array**, giving you a single result instead of multiple ones.
- **You cannot type the curly brackets of an array formula yourself**. The brackets must be generated with a particular keyboard shortcut.
- An array formula is **created by holding down CTRL+SHIFT+ENTER** instead of ENTER.
- You cannot delete an array formula by deleting a cell in which it appears. Instead **to delete an array formula you must select *all* the cells which you originally selected when you typed it**.
- To amend an array formula to include extra cells in any array, **you must select all the cells which you originally selected when you typed it - *and* enough neighbouring cells to display any extra results**. For example, if you want to amend an array performing ten calculations so that it now performs fifteen calculations, you must select fifteen cells before editing the formula - including the ten cells used to type the original formula.
- A spreadsheet using a single array formula is **smaller and quicker to use than one performing thousands of calculations separately** to arrive at the same result.
- You can *\*create your own arrays - called \*array constants* - by placing them in curly brackets. However, always remember you still need to press CTRL+SHIFT+ENTER to make the formula containing them an array formula.
- **Array constants can be horizontal - by using a comma to separate each item in the array - or vertical - by using a semicolon to separate each item in the array**. Horizontal arrays will be displayed across rows, while vertical arrays will be displayed down columns.
- You can **combine commas and semicolons to create arrays that go across rows *and* columns**.
- If you want to use an array constant more than once, create a **named array constant**. This is done through the **Insert \> Name \> Define...** menu. **You can then refer to the name of that array in any formulae, rather than typing in the whole array each time**.
- You can **use the TRANSPOSE function in an array formula to convert horizontal arrays into vertical ones, and vice versa**. You can also use it to convert the results of functions using array constants as ingredients.

### The last chapter's story: when's the worst time to turn up at hospital?

At the end of the chapter on transposing data, I posed some questions about [this data on waiting times at hospitals' Accident and Emergency (A&E) departments](https://drive.google.com/file/d/0B5To6f5Yj1iJTk9LV2tXTm5PWW8/edit?usp=sharing).

1.  The worst hour for long waits at North West Strategic Health Authority starts at 4am when you can expect to wait 161.4 minutes *on average*. That's almost two-and-three-quarter hours.
2.  For Alder Hey Children's NHS Foundation Trust the worst hour comes from 11pm, when patients can expect to wait for just over two hours.
3.  In England overall the worst hour is from midnight to 1am, when patients across the country are waiting over three-and-three-quarter hours.
4.  It seems that worst waits at that children's hospital (when this data was collected) are relatively short compared to the average in the region - and a lot shorter compared to the national average.
5.  In terms of considerations you'd need to be clear when this data was collected: waiting time data can be over a year old by the time it is released. You also need to be clear that these are *average* waiting times. In other words, between midnight and 1am many, many people will be waiting far longer than three hours and forty five minutes. And of course many will not wait so long. If you find an extreme human story to run alongside this, this may be worth mentioning. On the other side, [there are many ways that waiting time statistics can be massaged](http://www.theguardian.com/society/2014/jan/23/nhs-waiting-time-data-errors). Read up on these and make sure you ask about these when conducting follow up interviews.

### Detour: An introduction to Google Sheets - an always-connected spreadsheet tool

Google Sheets is Google's free spreadsheet tool. It is part of a suite of free tools that Google provides in its 'Google Drive' suite (formerly Google Docs).

As well as Google Sheets you can find the Microsoft Word-like Google Docs, the PowerPoint-like Google Slides, and Google Forms: a tool to create web forms for users to enter data directly.

If you have used Excel you should find Sheets easy to use instantly: it uses most of the same functions and has very similar menus.

However, it does *simplify* some functions, such as `TRANSPOSE` (see the chapter on `TRANSPOSE` for more detail), and also has some *extra* functions that take advantage of the fact that Google Sheets is web-based, which we'll explore in a later chapter.

This advantage is also its main disadvantage: data in Google Sheets is not as secure as data that only sits on your own computer. So if you're dealing with sensitive data and are concerned about others either hacking into your account or accessing it through legal avenues, then you may want to avoid such web-based services.

In these cases, however, you should also be careful of *emailing* any documents, given that web-based email services such as Gmail have exactly the same weaknesses.

You can use Google Sheets at [drive.google.com](https://drive.google.com/) - either log in with an existing Google account or sign up for a new one.

**You do not need to download anything** to use Google Drive once you are logged on. Instead use the red **CREATE** button in the upper left corner and select **Spreadsheet** to create a new blank spreadsheet online.


Once you click that button you should be taken to a new spreadsheet which you can rename by clicking on '*Untitled spreadsheet*' at the top of the screen.

When you are finished you can download the spreadsheet by clicking on the **File** menu, selecting **Download as** and then the format you require (Excel, CSV, or others).


To upload spreadsheets *into* Google Sheets use the red 'Upload' button next to the 'CREATE' button, and select **Files...**


Once uploaded, you can click on the file name to see the data. But to *convert* that spreadsheet to edit it in Google Sheets, select **File \> Open with Google Sheets**. This should now open up in an editable form.

It will also be listed in your files in Google Drive alongside the original Excel file (both will have the same name, but different icons).


You can also access Google Sheets directly by going to <https://docs.google.com/spreadsheets/>


### Make sure the settings are for your country

If you are based outside of the United States it's likely that you'll need to change some settings in Google Sheets.

Generally when you install Excel on your own computer you choose what country you're using it in, for example - but Google doesn't give you that option when you begin using Google Sheets.

Instead it generally assumes that your location is the US - and this has a significant impact on dates, and currencies.

To change your default location in Google Sheets select **File \> Spreadsheet settings...**.


This will bring up the *Spreadsheet settings* window, where you can see the settings for *Locale*, the *Time zone*, and *Recalculation* (this last setting relates to how often the spreadsheet re-runs certain functions - particularly those that generate the current time or date).


*Locale* is the obvious one to check. In the example above I see that Google Sheets assumes I'm in the *United States* - despite having my time zone set to the UK.

Because of this, if I type the date `05/06/2005` anywhere in the spreadsheet it assumes I mean May 6 2005, and not the 5th June 2005.

So I need to change this to United Kingdom if that's the dating system I'm using.

The time zone may seem like something that doesn't affect your work in spreadsheets, but if you're using functions like `NOW` or `TODAY` the time zone becomes important: if you've ever stayed up to watch celebrations around the world on New Year's Eve you'll have seen how different countries get to experience January 1st as 'today' while for you it's still December 31st (and vice versa). 'Today' isn't always the same for everyone.

You can see that if you wish to change the language being used, that's set elsewhere, in Google Drive settings overall.



## Grabbing data from elsewhere - `IMPORT` and `GOOGLE` functions in Google Sheets

Google has two *particular* sets of functions which Excel does not. Both involve connecting to the wider internet.

The first set of functions connect to other webpages and documents online, or sheets in a workbook. These all begin with 'IMPORT' and include `IMPORTHTML`, `IMPORTXML`, `IMPORTDATA`, `IMPORTFEED` and `IMPORTRANGE`.


Begin typing ‘import’ in Google Sheets and you will be shown a number of possible functions


The second set of functions connect to web *services* such as Google's own translation service [Google Translate](https://translate.google.com/) and its financial service [Google Finance](https://www.google.co.uk/finance).

These functions include `GOOGLEFINANCE` and `GOOGLETRANSLATE`.

`GOOGLEFINANCE` allows you to bring in various values of any specified company's stock (not just prices but also the Price-to-Earnings ratio and others), or to convert a number from one currency to another: for example convert the number 500 from dollars into euros (i.e. how many euros is 500 dollars right now).

Notably the function allows you to pull in historical data too: for example how much 500 dollars was worth in euros on Christmas Day 2013, or how much Apple stock was worth on September 12 2009.

`GOOGLETRANSLATE`, along with the rather wonderful `DETECTLANGUAGE`, allow you to identify what language any particular text is written in, and translate it.

I will cover these financial and translation functions in the next couple of chapters. In this chapter, however, I want to cover the more useful `IMPORT` functions.

<aside class="generic_inbar blurb google icon-google">

There's even a function called `GOOGLETOURNAMENT` which will bring in data for NCAA Division I Basketball Championship games. That's a little too esoteric for this book to cover, but if you do happen to be interested in basketball, you can [find out more about that function here](https://support.google.com/docs/answer/3093283)

</aside>

### Pulling data from another sheet: `IMPORTRANGE`


In Excel you can pull data from another sheet in the same workbook by adding the name of the sheet and an exclamation mark before the cell reference, like so:

`=Sheet1!A2`

But Google Sheets's `IMPORTRANGE` function extends this to sheets in *other* workbooks. There are two types of workbook you can use this to grab data from: your own spreadsheet workbooks; and those that others have made public.

I'll explain how it works for both of those in turn.

#### Using `IMPORTRANGE` with your own workbooks

The `IMPORTRANGE` function has two ingredients: the **key** for the spreadsheet workbook you want to import from, and the range of cells you want to import from it (including the sheet name if it's not the first one).

But what is this 'key'? Well, you can find the key in the URL of a spreadsheet when you open it:


When you look at a Google Sheets spreadsheet in your web browser the URL will look something like this:

`https://docs.google.com/spreadsheet/ccc?key=0ApTo6f5Yj1iJdGV1V1k4MEVPY2JQdGVUdnJqa1JaQUE&usp=drive_web#gid=0`

After the question mark are a series of **key-value pairs**, each pair separated by an ampersand. The URL above, for example, has three key-value pairs:

- `key=0ApTo6f5Yj1iJdGV1V1k4MEVPY2JQdGVUdnJqa1JaQUE`
- `usp=drive_web`
- `gid=0`

The first, as you can probably guess, is the key value pair containing the spreadsheet workbook's key.

You need to remember that the `key=` part is just a description. The key itself is the long series of characters after that: `0ApTo6f5Yj1iJdGV1V1k4MEVPY2JQdGVUdnJqa1JaQUE`

This is what you use in your `IMPORTRANGE` function as the first ingredient.

The second ingredient is the range of cells you want to grab. So the completed formula will look like this:

`=importrange("0ApTo6f5Yj1iJdGV1V1k4MEVPY2JQdGVUdnJqa1JaQUE","A2:C4")`

Note that *both the key and the cell range are in quotation marks*.

If you don't specify a sheet name the formula will assume you mean the first sheet in the workbook with that key.

If you want data from another sheet, specify it just as you would in Excel by adding the sheet name and an exclamation mark before the cell range:

`=importrange("0ApTo6f5Yj1iJdGV1V1k4MEVPY2JQdGVUdnJqa1JaQUE","Sheet2!A1:B10")`

As always you can simplify the formula by placing the key in its own cell and referencing that like so:

`=importrange(A1,"Sheet2!A1:B10")`


#### Using `IMPORTRANGE` to grab data from a public Google spreadsheet

An increasing number of organisations - including news organisations now make data available in a public spreadsheet. If this is a Google spreadsheet you can use `IMPORTRANGE` to grab data from that (if not, the other IMPORT functions should be able to grab it - see below).

The Guardian newspaper's Datablog, for example, often includes a link to 'Download the data' at the end of its articles. To demonstrate how `IMPORTRANGE` can be used with one of their spreadsheets, [take a look at one such article on Google user requests](http://www.theguardian.com/news/datablog/2011/nov/14/google-user-requests-data).


If you [click on 'get the data'](http://www.theguardian.com/news/datablog/2011/nov/14/google-user-requests-data#data), or scroll to the bottom of the piece, you'll find a link saying 'DATA: download the full spreadsheet'.


Clicking on that link takes you to [a Google spreadsheet which has been shared publicly by the journalist](https://docs.google.com/spreadsheet/ccc?key=0AonYZs4MzlZbdHFlZTBTTzlmUE41NmJXSXJaV3I5alE#gid=0). The URL for that is:

`https://docs.google.com/spreadsheet/ccc?key=0AonYZs4MzlZbdHFlZTBTTzlmUE41NmJXSXJaV3I5alE#gid=0`

As with your own spreadsheet, to use `IMPORTRANGE` with this you just need to copy the **key** from that URL, which comes after `key=` and *before any ampersands or hashes*:

`0AonYZs4MzlZbdHFlZTBTTzlmUE41NmJXSXJaV3I5alE`

You can now import data from the first sheet with a formula like this:

`=IMPORTRANGE("0AonYZs4MzlZbdHFlZTBTTzlmUE41NmJXSXJaV3I5alE","A1:G94")`

Note by the way that this workbook has a number of sheets, and none have the default titles of 'Sheet1' or 'Sheet2'. If you wanted to grab data from the third sheet you'd have to include its name like so:

`=IMPORTRANGE("0AonYZs4MzlZbdHFlZTBTTzlmUE41NmJXSXJaV3I5alE","CONTENT REMOVAL REQUESTS!A1:G94")`

#### Why wouldn't I just copy the spreadsheet?

Of course after all this fussing around with spreadsheet keys and functions, it would actually be a lot quicker to simply copy the spreadsheet or data you wish to import.

Indeed, if you are logged into Google Sheets when you are looking at a public spreadsheet, you can select **File \> Make a copy...** to copy the workbook into your own Google Drive.


In many cases this is going to be the right option. However, **if you expect the data to change** then *that* is when the IMPORT functions come into their own.

This is because every time you open your spreadsheet the latest data will be imported from that spreadsheet (or other data sources, which are handled by different IMPORT functions).

**The biggest danger is that the source data will disappear**: someone takes a spreadsheet offline, or turns sharing off. For that reason it's also a good idea to make a copy of the data anyway.

<aside class="question_blurb blurb">

#### How do you share a Google spreadsheet?

It's very easy to share a Google spreadsheet: in the upper right corner of any spreadsheet you are working on should be a blue button marked '**Share**'.


Clicking on this brings up a window where you can choose to share it with individuals (enter email addresses) or make the sheet completely public (click '*Get shareable link*')


Once you click on '*Get shareable link*' the button should turn green and you should now see a public URL which you can copy and share with others.


You can also use the drop down menu to specify whether others can edit the spreadsheet, or just add comments, or merely view it (the default).

If you can't see that button, the same options are also available by selecting the **File** menu and the **Publish to the web...**


</aside>

### Grabbing data from online CSVs and TXT files: `IMPORTDATA`

Clearly not all data is shared publicly in Google spreadsheets - but many organisations do publish their data in CSV and TXT documents online.

The Department for Environment and Rural Affairs (DEFRA) in the UK, for example, publishes pollution monitor data in dozens of CSV files for every monitor's location. [This, for example, is the page linking to the CSV files for Leominster](http://uk-air.defra.gov.uk/data/flat_files?site_id=LEOM). What is worth noting here is that the current year's data for hourly readings is published in a CSV file which is updated daily, so the `IMPORTDATA` function comes into its own as a way of getting the most recent data automatically without having to visit the site yourself.


The Met Office publishes its weather data in TXT files online. Selecting a weather station from their [historic station data page](http://www.metoffice.gov.uk/public/weather/climate-historic/#?tab=climateHistoric) takes you to [a file like this](http://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/eastbournedata.txt), containing data on rainfall, hours of sunshine, and maximum and minimum temperature for every month in every year since 1959 - including provisional data for the most recent five months. Once again this is updated so any `IMPORTDATA` formula will continue to show you the latest data without any need to grab it yourself.

NASA also publish all sorts of data as plain TXT files online. [Here, for example, is a text file containing data for the GLOBAL Land-Ocean Temperature Index from 1951-1980](http://data.giss.nasa.gov/gistemp/tabledata_v3/GLB.Ts+dSST.txt) (you can find more examples linked from [their page on GISS Surface Temperature Analysis (GISTEMP)](http://data.giss.nasa.gov/gistemp/).


NASA link to text files containing ocean temperature data


You can pull that data directly into a Google spreadsheet by using the `IMPORTDATA` function.

It's a very simple function with only one ingredient: the URL for the data you want to import. That URL must be for a CSV or TXT file: in other words, it must end in `.txt` or `.csv`

The formula to import CSV data from one of the DEFRA links, then, would be this:

`=IMPORTDATA("http://uk-air.defra.gov.uk/datastore/data_files/15min_site_pol_data/LEOM_SO2_2012.csv")`

And the formula to import TXT data from one of the NASA links would look like this:

`=IMPORTDATA("http://data.giss.nasa.gov/gistemp/tabledata_v3/GLB.Ts+dSST.txt")`

Once again you could also put the URL in a separate cell and refer to that instead (omitting the quotation marks).

### Grabbing data from webpage tables and lists: `IMPORTHTML`

The previous two IMPORT functions deal with published spreadsheets, whether hosted on Google Sheets, or in CSV or TXT files.

But `IMPORTHTML` deals with a trickier challenge: what if the table of data is published as part of a webpage full of other information?

`IMPORTHTML` can grab information stored in a HTML table or a HTML list. I mention HTML intentionally: information might *look* like it is in a table or list, but if it *isn't* contained in particular tags in the raw HTML, then this function will not work.

The HTML tags for tables and lists are as follows:

- A HTML table starts with a `<table>` tag, and ends with the `</table>` tag. In addition rows start and end with `<tr>` and `</tr>` and cells start and end with `<td>` and `</td>`
- An 'ordered list' (one that is numbered 1, 2, 3 and so on, or occasionally ordered with letters such as a, b, c) starts with `<ol>` and ends with `</ol>`. Each item in the list starts and ends with `<li>` and `</li>` (list item)
- An 'unordered list' (a bullet list) starts and ends with `<ul>` and `</ul>` with each item and starting and ending with `<li>` and `</li>`.

<aside class="tip blurb">

There's no need to check the raw HTML of a page before you use this function. Most information that looks like it's in a table or list *will* be, so it's only worth checking the HTML as part of the troubleshooting if your formula doesn't work first time.

</aside>

`IMPORTHTML` needs more information to deal with its particular challenge: three arguments, specifically, as follows:

1.  The URL you want to grab data from
2.  Whether you want to grab a table, or a list
3.  Which one you want, indicated by a number

So, for example, this formula...

`=IMPORTHTML("http://news.bbc.co.uk/1/shared/election2010/results/","table",2)`

...says *'Go to "http://news.bbc.co.uk/1/shared/election2010/results/", look for any tables, and grab the second (2) one'*.

Alternatively, a formula which was grabbing data from a list would look like this:

`=IMPORTHTML("http://baby-names.familyeducation.com/popular-names/boys/","list",12)`

Now, I know what you're thinking: '*How do I know that it's the second table, or the 12th list?*'

There are two possibilities here: either you look at the raw HTML and manually count each table or list until you get to the one you want... or you guess, and use trial and error to identify it.

I think you can guess which one I'm going to recommend.

Using trial and error - starting with the first table, then the second, and so on - is invariably much quicker than trying to identify the position of a table from the raw HTML.

For that reason it's often better to use cell references for each parameter rather than have all the information in the formula.

Below is one example of how that sort of approach works: in cell A1 we have the URL of the page we want to grab data from; in cell B1 we have the word 'list': note that there are no quotation marks around this or the URL; and in cell C1 we have the number 12.

In cell A2, then, we type an `IMPORTHTML` formula which refers to all three cells in turn, when their contents are needed:


By doing it this way we can easily change that number 12 to 11, or 10, or 13, and see what it grabs. Likewise, we can change 'list' to 'table' to grab that instead; or we can even change the URL to grab data from that (we can assume that it's not going to be in the 12th list, though, so those cells will have to change too).

Clearly I didn't begin by guessing the list I wanted here was the 12th one: cell C1 started off containing `1`, and I kept changing it until I got the result I wanted.

Note that you can use `IMPORTHTML` more than once, making it a good way to combine multiple small tables or lists from various webpages into one spreadsheet.

You could also put a list of URLs on one sheet in your workbook, and in each sheet a different `IMPORTHTML` formula referring to cells in that sheet.

<aside class="information blurb">

I talk in a lot more detail about the `IMPORTHTML` function in the first chapter of my book [Scraping for Journalists](https://leanpub.com/scrapingforjournalists) as a great introduction to the principles of scraping (automating the repetitive gathering of information from online sources).

</aside>

### Grabbing data from RSS feeds: `IMPORTFEED`

The `IMPORTFEED` function allows you to pull in data from RSS feeds (see box below for an explanation of what RSS feeds are).

RSS feeds are a particularly structured form of data (indeed, RSS is based on the XML format which the `IMPORTXML` function is designed to work with). The title or headline of each item in a feed, its author, date, summary, link to the full article or document, and other elements of content are all clearly and separately identified.

The `IMPORTFEED` function allows you to store those separately in your spreadsheet - and so analyse them accordingly. In effect it turns your spreadsheet into a very basic RSS reader.

<aside>

#### What is RSS?

RSS feeds are a way to follow updates from a particular organisation or website without having to keep checking their website.

The RSS stands for 'Really Simple Syndication' and *syndication* is a good way to describe what RSS does. If you've ever worked with syndicated news feeds - subscribing to a regular supply of stories, headlines or images from news agencies like Reuters, AP and the Press Association - then you will understand the principle: feeds of the latest updates from all the organisations that provide them are sent directly to you.

The key difference is that these feeds are *free*, and that it's not a few organisations providing them, but potentially thousands.

Every widely used blogging service, for example, includes RSS feeds: so every Wordpress.com blog, every Blogger.com blog and every Tumblr blog has its own RSS feed. And most news organisations have multiple RSS feeds: not just for the latest news headlines but often for specific sections, topics or journalists too.


The BBC News site has a page explaining - and linking to - RSS feeds for everything from news for Latin America to Have Your Say


Government departments and corporate press offices regularly provide RSS feeds: the UK's Office of National Statistics, for example, provides an RSS feed notifying subscribers of datasets it is releasing that day. And Data.gov.uk has RSS feeds for updates on the latest government datasets being added to the site.

RSS can save you the effort of making the same search over and over again: Google News and Google Alerts (when used on the Chrome browser) provide RSS feeds for any search you might conduct. Parliamentary monitoring site TheyWorkForYou provides RSS feeds for alerts when there is a new match against your specified search criteria (i.e. someone in Parliament mentions your chosen keywords); and WhatDoTheyKnow provides RSS feeds whenever a new Freedom of Information request containing your specified keywords is submitted using the site, or responded to. The site also offers RSS feeds for new requests or responses to or from specified bodies, or individuals.

To receive RSS feeds you need to create an account with an online RSS reader, or download an RSS reader to your computer. Feedly and Netvibes are two of the most popular web-based RSS readers with journalists, with each having particular advantages (Feedly works well on mobile; Netvibes allows you to share feeds with others). Check out those services for help on how to subscribe to RSS feeds, organise them into folders (a good practice to adopt) and check them.

</aside>
<aside class="tip blurb">

#### Finding an RSS feed's URL

To grab an RSS feed you will need to know its URL. This is not always easy to find.

Some websites will indicate that they have RSS feeds with an orange icon of the 'three bar' symbol for RSS, or the letters 'RSS', 'XML' or 'ATOM'. Alternatively you can use the Find function in your browser (CTRL+F or use the **Edit** menu) to search for the word 'RSS' on the page.

That icon will either link directly to the RSS feed, or to a page *about* the site's RSS feeds. You will be able to immediately tell which it is: a page about RSS will look like any other webpage, and should include a list of links to different RSS feeds offered by the site.

An RSS feed itself, however, will look like a collection of code. If you are using Chrome or Firefox it should be colour-coded accordingly: tags in purple and text content in black. (If you use other browsers including Internet Explorer and Safari, it may try to download the page as a file. Try to avoid these browsers if possible).


Once you have found the RSS feed itself, copy the URL to use in your formula. Often it ends in `.xml` or `/rss` or `/feed`: the URL for the BBC's US and Canada news, for example, is `http://feeds.bbci.co.uk/news/world/us_and_canada/rss.xml` and the URL for the Online Journalism Blog's RSS feed is `http://onlinejournalismblog.com/feed/`. The Guardian's RSS feed for columnist Charlie Brooker is at `http://www.theguardian.com/profile/charliebrooker/rss`.

Many blog services have relatively predictable RSS feed URLs. You can get the RSS feed for any site hosted on Wordpress.com, for example, by adding `/feed` to the base URL. So the RSS feed for myblog.wordpress.com will be myblog.wordpress.com/feed.

</aside>

The `IMPORTFEED` function needs only one ingredient: the URL of the feed in question. However, it also has three further *optional* arguments which you can choose to use to further filter the feed in question.

You can find more information on where those extra arguments go, and the values you can use by using the 'hint' box that appears when you type the function, and clicking on the link to the help files associated with it.


When you begin typing the formula you should get a list of options including IMPORTFEED


Once you select a specific function you get more information on the arguments it uses - and a link to the Help files


Clicking on the link brings up a window with examples of queries you can use in the formula


These optional arguments control the elements in the feed you want to grab (for example, only the author, or the title); whether you want to include column headers as an extra row; and how many items from the feed you want to grab.

A simple use of the `IMPORTFEED` function, then, would look like this:

`=IMPORTFEED("http://onlinejournalismblog.com/feed")`

In this case all items from the feed will be pulled into the spreadsheet, and split into as many columns as there are elements (title, author, date, and so on). Those elements will not be used as headings unless you use the optional parameter to do so.

A version of the formula that also uses the optional arguments might look like this:

`=IMPORTFEED("http://onlinejournalismblog.com/feed","items title","true",5)`

Here we are specifying, firstly, the feed URL; but also that we only want the 'title' element from each of the *items* in the feed; that we also want to grab the element names as headings; and that we only want the five most recent items in that feed.

There are only four qualities that you can grab from each item in a feed. These are:

- `"items title"`
- `"items summary"` (the content of each item)
- `"items url"`
- `"items created"` (the date of each item)

In addition you can also grab qualities of the feed as a whole by using `"feed"` instead of `"items"`, with the following options:

- `"feed title"`
- `"feed description"`
- `"feed author"`
- `"feed url"`

Or you can grab all of them by simply specifying `"feed"`

For more specific queries you will need to use the `IMPORTXML` function, which is also useful for RSS feeds because most RSS feeds use XML files.

### Grabbing data from an XML document - or a HTML webpage: `IMPORTXML`

`IMPORTXML` is the most powerful of the IMPORT functions. Its primary purpose is to enable you to pull in XML documents that are hosted online, but it can *also* be adapted to grab data from HTML webpages too.

Now you might think that that was `IMPORTHTML`'s job (hence the name). But while `IMPORTHTML` *does* allow you to grab data from HTML webpages, that data must be contained in a HTML *table* or *list*. `IMPORTXML` can grab data which *isn't* in a table or list. All you need to do is describe it.

But we're getting ahead of ourselves. Before I get into the detail of how you do that, I need to explain how `IMPORTXML` works for its intended purpose: with **XML documents**.

<aside class="question_blurb blurb">

#### What is XML?

XML stands for Extensible Markup Language. It is very similar to HTML in its appearance, but it is a much stricter, more structured language created for a different purpose: to describe data.

The best way to understand XML is to look at it like a table of data: every tag within those triangular brackets (chevrons) is like a column header; any text *between* tags is the data in that column.

So in XML you may see the same tag repeated - like `<author>` or `<latitude>` - but with different authors or latitudes between those tags each time they're used. Each of these different authors or latitudes is like a different cell in that column.

XML files often *nest* data, meaning the information is not all on the same level. For example, the tag `<teams>` might contain the tag `<team>` many times, and each of those tags might have a `<stadium>` and a `<players>` tag. Within the `<stadium>` tag are tags for names, locations and capacities; but within the `<players>` tag there might be tags for names, and within that tags for ages, position, goals scored and so on.

This is like a 'tree' of information, and getting information means identifying the branch or branches you need to go down to get it. Do you want a list of each `<team><stadium><name>`, for example, or each `<team><players><player><name>`?

Sometimes tags also include **attributes and values** which are separated by a space, like so:

`<description type="summary">`

In the example above `type` is the **attribute** and `"summary"` is the **value**. It often helps to be able to distinguish between these and the tags themselves. There are a number of ways of doing so: firstly, the attribute and value are not closed after the information they describe, so if you look at the closing tag (`</description>` in this case) you can tell which part is the tag.

Secondly, attributes and values always follow the pattern 'word, equals sign, double quotes, word(s), double quotes).

Thirdly, Chrome and Firefox helpfully colour-code the different elements in an RSS feed, making it easier to identify them. Tags are purple, and attributes and values colour coded differently. Text content is black.

You can find out more about XML by searching for the many guides online. [The W3 Schools guide](http://www.w3schools.com/xml/xml_whatis.asp) is relatively simple and includes information on XPath, which you need to use `IMPORTXML` well.

</aside>

The `IMPORTXML` function has two parameters: a **URL**, and a **query** (what you want from that URL).

The **URL** in this case would be an XML page, ending in `.xml` (although, as explained later, you can use this with HTML pages too).

The **query** is more complicated.

Other IMPORT functions we have looked at have only had a limited range of queries: `IMPORTHTML`, for example, only allows `"table"` and `"list"`; and `IMPORTFEED` allows four predefined queries each for grabbing information about either items within a feed, or the feed itself.

But `IMPORTXML` **allows you to craft any query you like**. This is its major strength.

But it also means you need to know more to use it.

Those queries use a little language called **XPath**. You don't *need* to learn the language to write queries - you can copy some simple examples - but understanding something about the language does give you more power to write the queries you need.

Thankfully XPath is very simple. At its core all you need to know is: *take the name of the tag containing your data, and put two slashes in front of it* like so: `"//tagname"`.

For example, you can find an XML file containing data on local authorities in the United Kingdom at <http://openlylocal.com/councils.xml>, which looks like this in the Chrome browser:


The first tag is `<councils type="array">`. Within that is the tag `<council>`, and within that numerous tags such as `<address>` and `<country>`.

To grab the contents of each 'councils' tag and put it in one row you would use the query `"//councils"` (note that the attribute-and-value `type="array"` are not used).

To grab the contents of each 'council' tag (note the singular) and put each 'council' in one row you would use the query `"//council"`.

To grab the contents of each 'address' tag and put each one in a different row, you would use the query `"//address"`.

Here is each query used in an `IMPORTXML` formula:

- `=IMPORTXML("http://openlylocal.com/councils.xml","//councils")`
- `=IMPORTXML("http://openlylocal.com/councils.xml","//council")`
- `=IMPORTXML("http://openlylocal.com/councils.xml","//address")`

Try each formula and see what happens (with some you'll have to wait a few seconds while it is *Loading...* the data).

With the first formula you only get one row: that is because `<councils>` is a tag containing *all councils*, and it only appears once. This is quite common in XML files, so if you get a similar result try looking at the next tag nested within the top one.

The second formula grabs that next tag instead: `<council>`. Because this tag appears more than once - in fact it appears once for every council - you will get as many rows as there are `<council>` tags.

What's more, each row will be split for any tags *within* that tag: so the first column will grab the `<address>` tag contents, the second column the `<annual-audit-letter>` tag, and so on.

The third formula drills down even further to grab `<address>`. Again, because this tag appears more than once - once for every council again - you will get as many rows as there are `<address>` tags.

But because there are no tags nested within this one, the results fill only one column.

As you can see, if you want to use this formula to grab every item in an online XML file, all you need to do is try a particular tag preceded by double slashes as your query, and if that doesn't work, try a different one.

B\> Not all XML files play nicely with this formula. For example, XML files of [food hygiene inspection details published by the UK's Food Standards Agency](http://ratings.food.gov.uk/open-data/en-GB), don't work with `IMPORTXML`. If it doesn't work for you, it may just be the file's fault, not yours. In this case, [try using a tool like Open Refine](https://github.com/OpenRefine/OpenRefine/wiki/Importers) to import the data and then export it as a spreadsheet.

#### More complex queries

You can write a more complex query which specifies the path to the tag you want. For example the query `"//councils//council//address"` means 'start in the `<councils>` tag, then within that go into each `<council>` tag' and grab the contents of each `<address>` tag.

This is particularly useful **if the same tag is being used twice in two different places** - something which can happen with a tag like 'address'.

Imagine, for example, an XML file which describes weather data. That file may have a tag for the address of the weather station recording the data, and another tag for the address of a particular location. The query for one might be something like `"//weather//station//address"` and the query for the other might be `"//weather//location//address"`.

You can also specify *which* item you want by using an **index** in square brackets like so:

`=IMPORTXML("http://openlylocal.com/councils.xml","//council[10]")`

The formula above will grab the contents of the 10th `<council>` tag in that XML file (the details for Bolton Council if you really want to know!).

And you can **specify tags with particular attributes and values** by also placing them in square brackets and prefixing the attribute with an `@` sign like so:

`=IMPORTXML("http://openlylocal.com/councils.xml","councils/council/created-at[@type='datetime']")`

*(Note that the value needs to be in single quotes otherwise it conflicts with the double quotes used to begin and end the query as a whole.)*

These techniques become particularly handy when it comes to using the function with HTML files, as we'll come onto.

<aside class="information blurb">

Live XML feeds are often provided to newsrooms for big sporting events. The New York Times's Jacqui Maher *[writes here about how they dealt with the XML feed for the 2012 Olympics](http://source.mozillaopennews.org/en-US/learning/london-calling-winning-data-olympics/)*

</aside>
<aside>

#### Identifying elements in an RSS feed

Many RSS feeds are XML files too. To specify a particular piece of information in an XML file you need to know what it's *called*.

To identify an element's name it's a good idea to look at the XML file (including RSS feeds) in a browser like Chrome or Firefox (Internet Explorer and Safari don't display RSS feed pages very well).

An RSS feed, for example, has two basic parts: the actual content, and the *tags* describing that content.

The top of the feed normally has tags describing the site as a whole: its title, description, and so on.


The start of the RSS feed for Online Journalism Blog


But not all RSS feeds show you the raw code: the BBC's RSS feeds, for example, are created in a way that makes them readable in Chrome:


Despite being an XML file, the BBC’s RSS feed doesn’t look like code in a browser like Chrome


In this case you need to right-click and select 'View source' to see the code itself.

However you get to see the code - straight away or by right-clicking - scroll down a little to see `<item>` tags - these are the individual posts.


Further down the RSS feed for Online Journalism Blog you can see ‘item’ tags - these are individual posts


The feed has a 'tree' structure, so within each `<item>` is a `<title>`, a `<link>`, a `<comments>` link, a `<pubDate>`, a `<dc:creator>` and a series of `<category>` tags before a `<description>` and the `<content>` itself

The *tag* is the name of the element: `<title>`, `<description>`, `<date>`, and so on.

Tags are *opened* and *closed*. The closing tag normally begins with a backslash, like so: `</author>`

The Google News RSS feed, for example, has tags for the `<channel>` as a whole, for each `<item>`, and for each item's `<title>`, `<link>`, `<category>` and `<description>`, among other things.

That RSS feed *does* work with `IMPORTXML`. However, the Online Journalism Blog feed, like most Wordpress feeds, does not. Nor does the [Office for National Statistics release calendar feed](http://www.ons.gov.uk/ons/release-calendar/rss.xml) or [the alerts feed on political monitoring site TheyWorkForYou](http://www.theyworkforyou.com/search/rss/?s=%22bedroom+tax%22). On the whole it's more likely that an RSS feed *won't* work with `IMPORTXML` than it will. But that doesn't mean you shouldn't try it!

</aside>

### Using `IMPORTXML` to grab data from HTML webpages

The principle of using `IMPORTXML` with HTML is not particularly different from using the function on XML files. This is because you are essentially performing the same two tasks: identifying a URL, and identifying a *path* through the *tags* in that URL to grab content.

To illustrate this, let's start with a simple `IMPORTXML` formula which uses a HTML webpage:

`=IMPORTXML("http://onlinejournalismblog.com/","//h1")`

This is going to the Online Journalism Blog and grabbing the contents of every `<h1>` tag - in other words, all the headlines and the title of the blog itself.

However, you can do a lot more with `IMPORTXML` because HTML pages tend to be much more complex than XML files, in terms of the variety of tags, their attributes and values, and the content contained within them.

<aside class="information blurb">

In Chapter 2 of [Scraping for Journalists](https://leanpub.com/scrapingforjournalists) I detail how to use `IMPORTXML` to scrape webpages - as well as learning some key principles which come in handy with more advanced scraping techniques. Here I'm just going to outline the basic workings of `IMPORTXML` when used on HTML webpages.

</aside>

Take, for example, the HTML behind [this page listing the latest journalism jobs on one recruitment site](http://www.gorkanajobs.co.uk/jobs/journalist/):


Here we have a number of tags including `<ul>`, `<li>`, `<a>`, `<h4>`, `` and ``.

Many of those tags will be used elsewhere on the page. But if we only want the *jobs* data on this page, then we want to be able to identify *only* those tags containing that data.

We can do this in a number of ways:

- By identifying a unique **path** to those tags. For example it's in an `<li>` tag within a `<ul>` within a `` within a ``, in which case you would use the query `"//div//div//ul//li"`
- By identifying the **attribute and value** of the tag. For example you could specify the contents of the tag `<li id="job44058" class="job regular cf">` by writing the query `"//li[@class='job regular cf']"` (note that the `id` attribute is not mentioned because this is unique to only one job, so it would only specify that one.
- By identifying the **position** of the tag. For example the query `"//ul[2]"` asks for the contents of the *second* `<ul>` (unordered list) tag.
- Through any **combination of the above**. For example `"//div/div/ul[1]/li[@class='job regular cf']"` identifies an exact path, the position (index) of one element in that path, and the attribute and value of another tag within that.

<aside class="tip blurb">

As always, **trial and error** is an important part of the process. It's not about getting the formula right first time, but trying different queries and seeing how useful the results are, triangulating between queries that are too narrow and queries that are too broad until you get the 'Goldilocks' query that is *just right*.

For that reason, it's often easier to put your URL and query in cells A1 and B1 (remembering that neither will need quotation marks when they're taken out of the formula), and write the formula to refer to those (e.g. `=IMPORTXML(A1,B1)` so you can just change the query cell rather than having to edit the formula directly.

</aside>

Note that any tags *within* your target tag will be treated as separate columns. So, within each `<li>` tag identified with the query above is a `<h4>` tag containing the job title, which will be placed in column A; a nested `<li>` tag containing the location, which will be placed in column B; another containing the wage; a `<p>` tag containing a description; a `` tag containing three different pieces of information; and another `<p>` tag containing the word 'New'.

### Grabbing links and other values that are not in visible text

One final thing you might want to do with `IMPORTXML` is grab *links*. These are distinct from the text on a webpage because although linked *text* might be visible, the actual URL being linked to is not.

The URL of a link is actually a *value*. When you make a link on a webpage the HTML looks something like this:

`<a href="http://onlinejournalismblog.com">Online Journalism Blog</a>`

The **tag** here is simply `<a>` (note that it is closed at the end with `</a>`).

This can have a number of **attributes** but the main one which makes it work is `href`: the *hyperlink reference*, i.e. the URL. The **value** of that attribute is the URL itself, in quotation marks.

To grab the link, use `//@href` instead of the tag name, like so:

`"//div//div//ul[1]//li//a//@href"`

This is slightly different from using it within square brackets (where it is describing properties of a tag whose text contents you want to grab).

The same principle can be used to grab any value: for example an image URL, title, or alternative description. The query to grab the alt tags of all images would be:

`"//img//@alt"`

Or you could specify a particular path which narrows down to only grab images within other tags.

<aside class="tip blurb">

#### Near-matches: using `starts-with` and `contains`

XPath has a couple more tricks up its sleeve in the `starts-with` and `contains` functions. These allow you to specify the attribute and value of a tag *without having to be absolutely precise*.

Using these in a query is a bit tricky, however. Both functions are used by adding them in square brackets immediately after the tag they refer to, like so: `li[contains`

And both `starts-with` and `contains` are **functions themselves**, which need to be followed by parentheses containing two parameters: the attribute, and what string of text its value should contain or start with.

For example, to specify that the class attribute of an `<li>` tag should contain the characters 'job' you would write this: `li[contains(@class, 'job')]`. The comma is worth highlighting here: note that you do not write `@class='job'` as you did previously. Here we're not saying that class='job', but rather that 'class' is the attribute, and 'job' is what it contains.

`starts-with` works the same way: a similar example using that would look like so: `li[starts-with(@class, 'job')]`

When used within a full query it might look something like this:

`"//div//div//ul[1]//li[contains(@class, 'job')]"`

</aside>

### Recap

- Google offers a number of functions which Excel doesn't have that allow you to **pull data from elsewhere**.
- `IMPORTRANGE`, `IMPORTDATA`, `IMPORTHTML`, `IMPORTXML` and `IMPORTFEED` allow you to bring in data from other Google spreadsheets; from online CSV and TXT files; from tables and lists on webpages; from XML files and HTML pages; and from RSS feeds respectively.
- The `IMPORTRANGE` function allows you to **pull data from any other Google Sheets spreadsheet** - either your own or one which has been made public.
- To grab data using this function **you will need to know the key of the Google spreadsheet in question**. This can be seen in the URL of the spreadsheet after `key=` and *before any ampersands or hashes*:
- If you don't specify a sheet name in `IMPORTRANGE` the formula will assume you mean the first sheet in the workbook with that key.
- The `IMPORTDATA` function allows you to **pull data from any public CSV or TXT file** - useful if you want data from one of the many public bodies who repeatedly update the same file online. Its only ingredient is the URL of that file, in quotation marks.
- The `IMPORTHTML` function allows you to grab a specific HTML **table or list** - useful where tables are updated online.
- `IMPORTHTML` will *only* work if the table or list is contained within the HTML tags `<table>`, `</ol>` or `<ul>` .
- `IMPORTHTML` needs three arguments: the URL you want to grab data from, in quotation marks; `"table"`, or `"list"` depending on which you want to grab; and a number to indicate which table or list you want (1 for first; 2 for second; and so on).
- `IMPORTFEED` will pull **data from an RSS feed**. It only requires one argument: the URL of the feed.
- RSS feeds are published by all sorts of organisations and web services. They can include the latest news reports, press releases or blog posts; search results for a specified query; the latest documents that have been published; or the latest data to have been collected; or times, dates and locations of forthcoming events, to name just some.
- By default, `IMPORTFEED` will pull in all items in the feed, and all elements of each item. But **you can specify that you only want certain elements, or a certain number of items, by using the optional parameters**. You can also specify that you want the element names to be added as column headings.
- `IMPORTXML` can be used to **import data from an XML document, including some RSS feeds - but it can also be adapted to grab data from a HTML webpage**.
- `IMPORTXML` uses a language called **XPath to express its queries** (what it wants to grab).
- XPath is a very simple language. **Used at a basic level it simply involves replacing the opening of a tag with a double slash**, so for example the XPath to specify the contents of the tag `<table>` is simply `//table`
- The result **should have as many rows as the number of times that tag appears in the target document**.
- **If there are any tags *within* that tag their contents will each be placed in separate columns** within each row.
- XPath **can specify a particular path to elements by identifying tags within tags**, again each tag preceded by a double slash like so: `//table//tr//td`
- You **can specify the position of an element by adding a number in square brackets** like so: `//table[1]//tr//td`
- You **can specify that you only want the contents of tags with particular properties** by adding them in square brackets: the attribute must be preceded by an `@` sign, and the value needs to be in *single* quotes, like so: `//table[@class='crimes']//tr//td`
- XPath has **a couple of functions that allow you to target tags who have properties starting with or containing specified characters**: `starts-with` and `contains`. These functions themselves need two parameters: the attribute, and the characters you are stipulating that attribute must start with or contain.
- **To use `IMPORTXML` with an RSS feed you will need to look at the feed in a browser like Chrome or Firefox**. Elements are named in *tags* contained in triangular brackets like so: `<date>`.
- **To use `IMPORTXML` with an HTML page you will need to look at the raw HTML in a browser like Chrome or Firefox** by right-clicking and selecting 'View Source' or similar, the identifying the tags containing the data you want (and their attributes and values if needed).
- **You only need to use IMPORT functions if you expect the data to change**, because it will always import the latest data. If you don't expect it to change then it will be quicker and easier to simply make a copy of the data.
- **IMPORT functions will stop working if the source data is taken offline**, or if sharing is turned off. So it's always a good idea to make a static copy of the data.

### Exercises

Use the `IMPORTFEED` function to pull in 'Disturbances' updates from [the Belgian rail company NMBS/SNCB](http://www.belgianrail.be/en/Default.aspx) (click on the 'Stations and Trains' tab). Can you spot the RSS feed?

Use the `IMPORTHTML` function to grab the table from the Irish Nurses and Midwives Organisation's 'Trolley Watch' page. The page updates every day. What issues might there be in grabbing information this way?

Use the `IMPORTDATA` function to grab [the weather data for Eastbourne](http://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/eastbournedata.txt)

Publish that sheet to the web and then use `IMPORTRANGE` to pull the most recent year's data from it.

Use the `IMPORTHTML` function to grab the third table on the football website Transfermarkt's [page on the football agency Eleven Management](www.transfermarkt.co.uk/eleven-management/beraterfirma/berater/474/plus/1). What's missing?

It grabs most of the information - but one column says `[TABLE]`. This means that there's a table *within* this table, which `IMPORTHTML` cannot grab. Can you use `IMPORTXML` to grab it instead?

The `IMPORTHTML` formula also just gives empty cells for the 'nationality' and 'club' columns. Why is this? How can you use `IMPORTXML` to grab those values?


## Dealing with data in another language: `GOOGLETRANSLATE` and `DETECTLANGUAGE`

In the last chapter I mentioned one of the special functions which you can only use in Google Sheets: `GOOGLETRANSLATE`.

This function is particularly useful if you're dealing with data in other languages, or where the language is mixed, and want to see it in your own.

<aside class="tip blurb">

If you are searching data for terms in your own language, these functions help you spot references using other languages. They also help you translate searches into a variety of other languages - a useful time-saver!

</aside>

Of course this function is only as effective as Google Translate itself, which you may be aware can be a bit hit-and-miss.

But when it comes to single-word entries it can be quite effective.

The `GOOGLETRANSLATE` function needs three ingredients: the string of text you want to translate (or the cell containing it); a special **two-character code** for the language you are translating *from*, and the code for the language you are translating *to*.

A formula to translate the contents of cell A2 from French into English, for example, would look like this:

`=GOOGLETRANSLATE(A2,"fr","en")`

When copied down a column so that each formula applies to a different cell (A2, then A3, and so on), this will fill the column with a translation of each cell in the column next to it (or whichever you specified). Handy.

<aside>

The language codes are actually *optional*. If you don't specify them then the function *defaults* to **automatically detecting the language** of the text specified, and translating it to the language of the system you are using.

In other words, if your system is set up to US English then it will translate to that language.

So if you didn't know what language a particular cell might be in, then you could write the formula like so:

`=GOOGLETRANSLATE(A2)`

If you are going to do this then it's advisable to use `DETECTLANGUAGE` in another column (explained below) as an error-checking element. This will tell you which language Google thinks each cell is in, and is using to translate from. If you think it's wrong then you can correct accordingly.

</aside>

How do you know the language codes to use? Well, you could search the web for 'two character language codes' and you'd end up on [a Wikipedia page like this one on 'List of ISO 639-1 codes'](http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) or [this Library of Congress page on 'Codes for the Representation of Names of Languages'](http://www.loc.gov/standards/iso639-2/php/code_list.php) (essentially the same thing).

Make sure you use the two-letter codes in the column for **ISO 639-1**. The others refer to three- and four-character codes.

<aside class="information blurb">

#### What does ISO mean?

ISO stands for the **International Organization for Standardization**, which maintains standards for all sorts of measurements to ensure that people in different countries can be sure they're talking about the same thing.

The ISO standard for language codes is ISO 639. There are actually six different parts to it: ISO 639-1, ISO 639-2, ISO 639-3, and so on.

These codes are used in all sorts of places: for example, in HTML webpages to declare what language they're written in. You can use the [w3schools.com page on country codes](http://www.w3schools.com/tags/ref_language_codes.asp) to find out more about that, and the page helpfully only gives the two-character ISO 639-1 codes too - so it's less confusing than the Wikipedia page above.

</aside>

### Detecting the language: `DETECTLANGUAGE`

If you're not sure what language all your cells are in, then the `DETECTLANGUAGE` function comes in very handy. Not always because it actually *does* get the language right: but more because it tells you what language Google *thinks* the cell is in, and therefore what language it is translating *from* if you haven't specified that.

The `DETECTLANGUAGE` function needs only one ingredient: the cell you want to translate, or the string of text itself, like so:

`=DETECTLANGUAGE(A2)`

Or:

`=DETECTLANGUAGE("Bonjour")`

Obviously it's much more likely you'll be using a cell reference.

The result will be one of those two-character country codes to indicate **which language Google thinks it is**. In the example above it will return `fr`, meaning it believes that "Bonjour" is French.

If it doesn't know what language it is - particularly if the cell is empty - then it will return `und`.

[Historical data from the European Investment Bank](http://www.eib.org/projects/loans/list/index.htm) is a good example of where this comes in useful. In the 1950s and 1960s the descriptions for projects given loans were entered in French. But in later decades those descriptions were written in English.

Using `DETECTLANGUAGE` allows you to identify which it is, and translate accordingly.

### Using `DETECTLANGUAGE` as part of `GOOGLETRANSLATE`

Although you can use `GOOGLETRANSLATE` to detect the language automatically (by not specifying it), you can also use `DETECTLANGUAGE` as part of the formula like so:

`=GOOGLETRANSLATE(A2,DETECTLANGUAGE(A2),"en")`

Or, more likely, you would fill a new column (let's say the B column) with the results of `=DETECTLANGUAGE` applied to each cell in A, and then use *those* cells in your formula like so:

`=GOOGLETRANSLATE(A2,B2,"en")`

This second approach is useful because it gives you that 'error-check' column showing which language Google thinks it is, rather than integrating it directly into the formula.


In this sheet the B column is used to show what language Google thinks each cell is in…


…Then in the next column that language is used in the GOOGLETRANSLATE function


This also allows you to **manually correct** any translations by changing the country code in the 'Language' column (deleting the `DETECTLANGUAGE` formula first).

### False friends and cognates

Many languages share the same roots (words related in this way are called **cognates**), and many words mean different things in different languages (called 'false friends' - as always [Wikipedia has a wonderful entry on this](http://en.wikipedia.org/wiki/False_friend)).

Portuguese words that could be Spanish or another Roman language, for example, include polémica, cláusula, tribunal, reclama, relativos, trasferidos, adeptos, somos and raptadas. Use the `DETECTLANGUAGE` function on those and it identifies five as Portuguese, three as Spanish, one as Italian and one as Romanian ([thanks to Samuel Negredo for the list](http://twitter.com/negredo/status/527588594878529536)).

'Mist', meanwhile, is a '**false friend**': the German word for 'manure', 'dung' or 'rubbish' (not to mention an exclamation of annoyance!), but also an English word for a type of fine fog.

So which 'mist' is it when you use `DETECTLANGUAGE`?

Not surprisingly (given the English bias of most software) the function will return `en` (English) rather than `de` (German) when used on 'Mist' in isolation.

But context matters: when 'mist' is part of the sentence "*Wenn der Hahn kräht auf dem Mist*" then `DETECTLANGUAGE` will return `de`. And `GOOGLETRANSLATE` will give you "If the rooster crows on the dung" (quite close to the real meaning "When the rooster crows on the dung heap").

### Tip: translating a term to generate search URLs in other languages

As well as translating existing data, the `GOOGLETRANSLATE` function can help save you time in generating your own data - for example URLs for searches in various languages.

To do this you need the following ingredients:

- A spreadsheet containing those two character language codes
- The term you want to translate
- A copy of the URL for a search on your chosen search engine

#### Grabbing a table of language codes

You can generate a spreadsheet containing two character language codes by copying and pasting from the [w3schools.com table of codes](http://www.w3schools.com/tags/ref_language_codes.asp) - or if you want to practise your `IMPORTHTML` function, you can import it by using the following formula:

`=IMPORTHTML("http://www.w3schools.com/tags/ref_language_codes.asp","table",1)`

*(If you do this, remember to copy and paste as **values only**, otherwise when you try to sort the data the `IMPORTHTML` formula will keep overwriting it).*

Once you have those codes in your spreadsheet you can begin using `GOOGLETRANSLATE` with each of them.

Give the next column a heading of 'Translation' and type the following formula:

`=GOOGLETRANSLATE("Olympic torch","en",B2)`

This will translate the phrase 'Olympic torch' from English (`"en"`) to whatever language represented by the code in cell B2.

If your first language is Abkhazian, represented by the code `ab`, then you will get a `#VALUE!` error. Don't worry. This is because Google Translate cannot handle that language.


Instead, **copy the formula down to see how it deals with better supported languages**.

Once you do, you'll notice that Afrikaans, Albanian and Arabic work, but Afar, Amharic and Aragonese don't.


When copied down the entire column the formula works on 75 of the languages, and generates an error on the others.

But 75 results is more than enough to be working with.

#### Using those results in a search

You can now insert each of those results into a search URL. All you need to know is the basic structure of the URL, and where to put your term.

A search for 'Olympic torch', for example generates a URL like this in Google: `https://www.google.co.uk/ search?q=olympic%20torch`

<aside class="tip blurb">

You may have tried this yourself and got a much longer URL including details on your browser, language, and even previous searches. But you can strip all that out to leave just the basic `q=` part after the question mark and it should still work.

</aside>

There are two parts to this URL. The first part is constant: it is the address of the site followed by a question mark and an equals operator:

`https://www.google.co.uk/search?q=`

That question mark indicates the beginning of your ***query***.

In this case our query is 'Olympic torch', but the space is replaced by `%20` to give us this:

`olympic%20torch`

We'll need to **add an extra column to replace those spaces so they work in a URL**. This is simply repeating the process outlined in the chapter on `TRIM` and `SUBSTITUTE` on generating URLs to speed up a name search.

*(You may find it useful to return to that chapter for a reminder on issues created by spaces in URLs and how different sites deal with those).*

In column D, then, we need to use `SUBSTITUTE` to do that, like so:

`=SUBSTITUTE(C2," ","%20")`

This takes the contents of cell C2, and replaces any spaces in that cell with `%20`. This won't work for the first two cells containing errors, but copy it down and for the first decent result, 'Olimpiese fakkel', you should get 'Olimpiese%20fakkel', and so on.


We're now ready to insert this into a search URL. Now we're up to column E, and the formula to do that simply adds our term to the end of the URL like so:

`="https://www.google.co.uk/search?q="&D2`

Note that the URL has to go in quotation marks because it is a *string*. This is followed by an ampersand to join that string to the string in cell D2 (again, of course, D2 is going to generate an error, but when this is copied down D4 and others will not).

You should now have a column full of 75 search URLs. Google Sheets should automatically make these clickable, so you can click on each and see the results.


This process saves you having to type 75 different searches to search in each language. You could also combine this with `IMPORTXML` to scrape the search results too, so you don't even have to click on each link.

<aside>

#### Advanced geekery: combining the translations into one search using `JOIN`

Of course you might not want to make 75 searches. Instead you might just want to conduct a search which covers all those variations. You can also do this by combining your 75 results into one long search. (*Well, actually not quite - as we'll see*).

The `JOIN` function is what you need here. This will, not surprisingly, join together any ingredients it is given, adding a 'delimiter' between each one.

First we need to **sort our results to put all the ones with error messages at the bottom**. You can do this by selecting any cell in that column and then clicking on the **Data** menu and selecting **Sort sheet by column C, A-Z...** (this will also work on column D or E, as the errors are carried across into those too).

Once you've done this the non-error results should be sitting in cells D2:D76. Those are the cells we might try to join.

Now you might think that we could join the contents of each translated cell, and place 'OR' between them, to tell Google we don't want to search for something with *all* of those terms in it.

In reality this challenge turns out to be much more complicated than it appears, for a number of reasons.

I'll save you the trouble of finding this out yourself (spoiler alert!) by explaining what I discovered when I tried to do this.

Firstly, it seems that adding the 'OR' in Google search via the URL doesn't quite work. Instead you need to **change the type of query**.

Let me explain. A 'normal' query in Google is preceded by `q=`, as explained earlier. But if you use [Google Advanced Search](http://www.google.co.uk/advanced_search) to conduct a search for 'any of these words' (i.e. an 'OR' query), the URL generated is slightly different.


Use the advanced search page to test what URL appears


The URL uses a different query code


This time the query terms are preceded by `as_oq=`

My guess is that this stands for 'advanced search OR query'. But that's just a hunch.

There's an important lesson here: always generate an example URL for the search you want before adapting it.

A quick bit of googling on that term (hey, they've got nothing to hide) throws up [a 'Search Protocol Reference document](http://static.googleusercontent.com/media/www.google.com/en//support/enterprise/static/gsa/docs/admin/72/gsa_doc_set/xml_reference/xml_reference.pdf) which confirms that `as_oq=` indicates an `OR` search.

So, we need to adapt the URL we are generating for these terms. Now it's going to look like `="https://www.google.com/search?as_oq="&` followed by the cell reference containing our joined list of terms.

For example, if we've used cell F2 to join those items into one long list our new formula will look like this:

`="https://www.google.com/search?as_oq="&F2`

Now, as it happens, when you use that `as_oq=` query **the 'OR' is automatically inserted between each word**, so we don't need to use that in our `JOIN` formula.

However, this creates a *new* problem: 'OR' is also inserted *in the middle of multiple-word phrases*. So we get `Antorcha OR olímpica OR Dhuxul OR Olympic` when what we really want is `"Antorcha olímpica" OR "Dhuxul Olympic"`.

If we add quotation marks around each phrase, that will stop this happening. But quotation marks indicate the start of a string in Google Sheets and will cause problems if we try to insert them in a formula.

So, **how do we create a quotation mark without *using* a quotation mark?** Think about that for a second before I give the answer - because we've covered it earlier.

Got it yet?

I'll give you a little longer.

A bit more time...

OK, then.

It's **the `CHAR` function**. This generates special characters based on their 'code' (*you may remember you can also use the `CODE` function to find out the code for any character*).

**The code for a quotation mark is `34`**. So we can generate it in our function by including `CHAR(34)`

But our problems aren't over yet. The final problem is this: the number of terms included. Testing this with a search containing all 75 terms generates an error on the search result page: "Your client has issued a malformed or illegal request".

In fact, when I tested this I was only able to get it to work on 50 or 51 search terms (depending on whether you replaced the spaces with `%20` or `+`, which also works).

But even then, not all terms are being searched - because Google has a limit of 32 words on queries. So even when it *doesn't* generate an error, pay attention to the warning at the top of the results which tells you which is the first word it ignores.


If you search for more than 32 terms Google will tell you the first word it is ignoring at the top of your results


In this case, most of our phrases contain two words, so it will only be able to search 16 phrases (16 times 2 = 32!) before it hits that limit.

Still, doing 16 searches all at once is still pretty good!

So, with all that testing, re-testing, googling, refining, tweaking and adapting - all integral elements of spreadsheet work and data journalism more generally - this is what we have...

Firstly, a formula to join 51 of the results together. This uses `JOIN`.

`JOIN` takes two ingredients: the **delimiter** you want to put between each ingredient; and the range of cells containing what you want to join.

Our delimiter is going to be a quotation mark, plus sign, and quotation mark, because we want every item to end with a quotation mark, then a plus sign, and another quotation mark for the next item, like so: `olímpica"+"Dhuxul%20Olympic`

Note that this will give us a list where the *first* item still lacks an opening quotation mark, and the *last* item lacks a closing quotation mark. We'll solve this later.

The formula in full looks like this:

`=JOIN(CHAR(34)&"+"&CHAR(34),D2:D51)`

This is quite an impressive `JOIN` formula. The first part of it combines three elements: a quotation mark: `CHAR(34)`, joined using `&` to a plus sign: `"+"`, joined to another quotation mark: `CHAR(34)`.

Those three characters - quotation mark, plus sign, quotation mark - will be inserted between each item in the resulting list.

A comma then indicates the start of the second ingredient: the range of cells containing all the items we want to join: `D2:D51`.

The result is a pretty long string - it's best to widen the column so it doesn't distort your sheet.


So now we have a list. This happens to be in cell F2 in the above example, but it could be anywhere.

Our next formula inserts the result of that into a URL. Of course we don't *have* to write two formulae: we could do all this together in just one, but it would look horrible and be harder to test and tweak. So. Our second formula looks like this:

`="https://www.google.com/search?as_oq="&CHAR(34)&F2&CHAR(34)`

All this formula is doing is **putting together a string**: in this case, a URL.

That string has four parts to it, each one joined by `&`:

- Firstly, the beginning of the URL including our special query code: `"https://www.google.com/ search?as_oq="`
- Secondly, an opening quotation mark: `CHAR(34)`. Remember how I said that the first item in our `JOIN` list would be lacking one? This is how we solve that, and insert a quotation mark before that *first* item in our list.
- Thirdly, the contents of cell `F2`: that long list of items created and delimited with quotation marks and plus signs with `JOIN`.
- And finally, a closing quotation mark: `CHAR(34)`. This is how we solve that problem of the last item in the list lacking one.

The result is a very long URL which conducts an 'OR' search on 50 different phrases, each one contained in quotation marks to specify that *exact* phrase rather than either word.


Now this is all very geeky and the example is esoteric - but hopefully you can see how these techniques could save you time in similar situations where you're having to do the same thing over and over again.

</aside>

### Recap

- The `GOOGLETRANSLATE` function allows you to **translate from one language to another**
- The `GOOGLETRANSLATE` function has **three ingredients: what you want to translate (normally a cell reference); what language that is in; and what language you want to translate it into**.
- In order to indicate which languages you're translating from or to, you need to use **two character country codes** called ISO 639-1 codes. You can find these in a range of places, including Wikipedia, the Library of Congress website and w3schools.com.
- The `GOOGLETRANSLATE` function can be used with just *one* ingredients: what you want to translate. In that case it will **make an educated guess about the language it is in**, and use your computer's default language for the language to translate into.
- The `DETECTLANGUAGE` function tells you **what language Google thinks a cell's contents are written in**. It will return the two-letter code for that language or, if it does not know, it will return '`und`'.
- The `DETECTLANGUAGE` function needs only one ingredient: **the cell containing the text whose language you want to detect**.
- `DETECTLANGUAGE` is **particularly useful as a way to error-check** Google Translate, where you are not specifying the language yourself.
- **Some words appear in more than one language, but mean different things**, what are called '**false friends**'.
- In these cases **the more context around the word (i.e. the more other words there are), the better judgement** Google Translate can make as to the language being employed.
- **Not all languages are supported by `GOOGLETRANSLATE`**: if you get a `#VALUE!` error, that's probably why (the error hint will explain if so).
- You can use `GOOGLETRANSLATE` as a way to **translate one search query in your own language into multiple search queries in different languages**, automating the manual process of translating and typing those searches yourself - but don't forget to replace spaces for the resulting search URLs using the `SUBSTITUTE` function.
- **Search queries can also be combined into one very long search query using the `JOIN` function**. However, remember that you also need to add quotation marks using `CHAR(34)` to specify exact phrases, and use a search URL with a different query code (`as_oq=`) to indicate 'OR' between them.

### `IMPORT` Exercises - tips

At the end of the last chapter I outlined some exercises to get experience with the various `IMPORT` functions in Google Sheets. Here are some answers and tips to help:

[The 'Disturbances' RSS feed from the Belgian rail company NMBS/SNCB is here](http://www.belgianrail.be/jp/sncb-nmbs-routeplanner/help.exe/en?tpl=rss_feed) (click on the 'Stations and Trains' tab).


[The Irish Nurses and Midwives Organisation's 'Trolley Watch' page is here](http://www.inmo.ie/6022). One key issue is that because the page updates every day your scraper will too. So if you want to keep any of that information you'll need to copy it elsewhere (use **Edit \> Paste Special \> Values only** so you are pasting the results, not the scraper).

When you use the `IMPORTHTML` function to grab the third table on the football website Transfermarkt's [page on the football agency Eleven Management](www.transfermarkt.co.uk/eleven-management/beraterfirma/berater/474/plus/1) you will notice two things missing: firstly, the name and position of each player, where one column says `[TABLE]`; and secondly, the nationality and club, which are represented by images, not text.

You can use `IMPORTXML` to grab that nested table like so (if the URL is in cell A1):

`=IMPORTXML(A1,"//table//table")`

You can use `IMPORTXML` to show the nationality by grabbing the image `alt=` attribute like so (if the URL is in cell A1):

`=IMPORTXML(A1,"//table//img[@class='flaggenrahmen']//@alt")`



## Converting currency or using stock prices: `GOOGLEFINANCE`

`GOOGLEFINANCE` is another Google Sheets function to take advantage of its connectivity to the web - and Google's own Finance service specifically - to pull in live and historical data on the stock market and currency exchange values.

As with `GOOGLETRANSLATE` you'll need to know **the particular codes used to refer to the currencies or stocks** that you want to use in your formula.

When it comes to **currency**, once again those codes come from the ISO: specifically [the ISO 4217 currency codes](http://www.xe.com/iso4217.php) which are three character codes like 'EUR' for euro or 'USD' for US dollar.

### Converting currency with `GOOGLEFINANCE`

Converting currency with `GOOGLEFINANCE` really means **grabbing the exchange rate between any two currencies**. That rate is then applied in your formula to any number you like.

For example, if you have a column full of amounts in dollars, and you want to convert them to euros, you just need to multiply each one by the US dollar-euro exchange rate.

Here's an example of using `GOOGLEFINANCE` to grab that exchange rate:

`=GOOGLEFINANCE("currency:USDEUR")`

Here `GOOGLEFINANCE` only uses one ingredient - but it's a complicated one which has three elements combined:

- What we want: `currency`
- The code for the currency we're converting *from*: `USD`
- The code for the currency we're converting *to*: `EUR`

Also importantly: those elements are **pushed together without any spaces, and placed in quotation marks**.

At the time of writing that rate is `0.8`, which means you need to multiply the dollar amount by 0.8 to get the same amount in euros.

If our dollar amounts were in column A, then, a full calculation would look like this:

`=A2*GOOGLEFINANCE("CURRENCY:USDEUR")`


We could then copy that down an entire column.

Alternatively, instead of having to grab the exchange value in every column, we could just grab it once and put it in a cell elsewhere - say E1 - and refer to that:

`=A2*$E$1`

Note that we need to fix that cell reference with dollar signs because we don't want it to change when we copy any formula down or across to other cells.

### Grabbing stock values with `GOOGLEFINANCE`

When it comes to stock prices `GOOGLEFINANCE` only needs *one* ingredient: **the code of the stock you want the price for**.

These can vary in length: for example Apple's stock symbol is 'AAPL'; the symbol for security company G4S is 'GFS'; and Agilent Technologies's stock uses the symbol 'A'.

Although lists exist of stock symbols - like [eoddata's list for the New York Stock Exchange](http://eoddata.com/symbols.aspx) - it's generally simplest to just use Google itself to search for 'stock market symbol' and the name of the company you're interested in.

A formula to grab the price for Microsoft stock (code 'MSFT'), then, looks like this:

`=GOOGLEFINANCE("MSFT")`


And of course you could instead place each stock symbol in its own cell, and refer to thta in the formula instead, like so:

`=GOOGLEFINANCE(A2)`

...where A2 contained the string `MSFT` (no quotation marks).

#### Grabbing more than just the price: extra options

But where `GOOGLEFINANCE` really comes into its own is with a range of **optional parameters** you can add, including the ability to call up details for **historical data** by specifying a date, or a date *range*.

These optional parameters are, in order:

1.  An **attribute** of the stock
2.  A **start date** for the period you want this for
3.  The **number of days** from that start date, or **end date** for the period
4.  An **interval** you want to specify during that period (daily data, or weekly).

Depending on how many you use, your formula can have one, two, three, four or five ingredients.

**Attributes** you can request using this function are too copious to list here. Google's [documentation on the `GOOGLEFINANCE function`](https://support.google.com/docs/answer/3093281?hl=en) provides a full list, but highlights include:

- `"priceopen"` - The price when the market opened
- `"high"` - The day's high price
- `"low"` - The day's low price
- `"changepct"` - the percentage change in the price of the stock since the close of yesterday's market
- `"volume"` - The day's [trading volume](http://www.investopedia.com/terms/v/volumeoftrade.asp)
- `"eps"` - The earnings per share (an [indicator of profitability](http://www.investopedia.com/terms/e/eps.asp)\]
- `"beta"` - the beta value (essentially a [measure of volatility](http://www.investopedia.com/articles/stocks/04/113004.asp))

We can add an attribute to the basic formula, then, to specify that we don't want the current price, but instead want to grab the trading volume:

`=GOOGLEFINANCE("MSFT","volume")`

We can compare that to Apple's trading volume with a similar formula:

`=GOOGLEFINANCE("AAPL","volume")`


#### Grabbing stock details for a particular date

That's two ingredients. Now let's add a third: a **date**.

`GOOGLEFINANCE` is a little fussy about how dates are entered. You need to use the `DATE` function to ensure that the date is encoded correctly. The function to look up the volume of trading on October 11th 2014, for example, would look like this:

`=GOOGLEFINANCE("MSFT","volume", DATE(2014,10,11))`

The `DATE` function takes three arguments: the year, the month, and the day, *in that order*.


<aside class="warning blurb">

Note that at this point your results will not just fill one cell: they will fill *four* cells: two headings (`Date` and the value you're grabbing: in this case, `Volume`); and the actual date and value underneath those. You'll need to make sure there's nothing in the cell underneath or to the right of your formula, or it will be overwritten.

</aside>

If that's too much work you can always put the date directly in another cell and use a cell reference like so:

`=GOOGLEFINANCE("MSFT","volume", E2)`

(Where your date is in cell E2).

One other thing to be aware of here: **if your date refers to a Saturday or Sunday you'll get an error because there's no trading**. Likewise if it's a 'market holiday': [financial sites will give you a list of these](http://www.thestreet.com/stock-market-news/11771386/market-holidays-2014.html).

#### Grabbing stock details for a particular range of dates

Having specified a single date we can add a further ingredient to turn that into a *range* of dates.

Note that **this will fill a lot more than one cell, so make sure you have lots of empty cells underneath and to the right to accommodate the data**.

Here's an example:

`=GOOGLEFINANCE("MSFT","volume", DATE(2014,10,11), DATE(2014,11,11))`

This formula will give us volume numbers for that stock from October 11th to November 11th (check that dates are not formatted in your version of Google Sheets).

These will fill 38 cells across two columns: the headings `Date` and `Volume`, then 18 dates under the first heading and 18 values under the second (remember Saturdays, Sunday and market holidays are not included).

You can also specify a number of days rather than an end date. The following version of the formula, for example, specifies `10` days after the start date:

`=GOOGLEFINANCE("MSFT","volume", DATE(2014,10,11), 10)`

Actually, this is 10 *trading* days, so we get the Monday 13th to Friday 17th (5 days) and the Monday 20th to Friday 24th (5 days) rather than 10 consecutive days.

Often, however, rather than specify particular dates financial formulae use the `TODAY` function to grab data in relation to today's date, such as the last 30 days' numbers, like so:

`=GOOGLEFINANCE("MSFT","volume",TODAY()-30,TODAY())`

This formula has four ingredients: firstly, the stock symbol (`"MSFT"`, the code for Microsoft stock); secondly the attribute `"volume"`; thirdly a start date which takes today's date and subtracts `30` from it; and finally an end date: `TODAY()`.


A final optional parameter allows you to specify whether you want details for every day, or every week. Given that not using this parameter means Google Sheets assumes you want daily data, the only reason you would use this is to specify you want weekly data.

You can specify daily data with `"DAILY"` or `1`

You can specify weekly data with `"WEEKLY"` or `7`

A final formula adding this parameter then would look like this:

`=GOOGLEFINANCE("MSFT","volume",TODAY()-30,TODAY(), "WEEKLY")`

Now instead of over 30 cells, you'll have ten: your two headings plus a date and value for each of the four weeks covered.


### Recap

- The `GOOGLEFINANCE` function allows you to **convert from one currency to another**.
- The `GOOGLEFINANCE` function also allows you to **find out the price of any company's stock on any given date**.
- Converting currency with `GOOGLEFINANCE` really means **grabbing the exchange rate between any two currencies** which you can then apply to an amount in one of those currencies.
- `GOOGLEFINANCE` only uses one ingredient when you need a currency conversion: **the word `CURRENCY:` followed by the two codes for each currency** (the currency we're converting from, and the one we're converting to), without any spaces, and in quotation marks. For example, `"CURRENCY:USDEUR"` (US dollars to euros) or `"CURRENCY:EURGBP"` (euros to British sterling).
- `GOOGLEFINANCE` also only needs one ingredient when you need a stock price: **the code of the stock you want the price for**.


## Publishing live data in a live chart

Because financial data, quite frankly, bores me, I thought this might be a nice excuse to briefly cover Google Sheets' ability to generate **live charts**.

This book is, of course, not about visualisation (for a good introduction I recommend Dona M. Wong's book *The Wall Street Journal Guide to Information Graphics*), but Google Sheets charts are worth mentioning here for the simple reason that a) you can publish and embed those charts on any webpage; and b) those published charts will then *change if the underlying data changes*.

In other words:

- You only have to use `GOOGLEFINANCE` once - but the data will change every day.
- You only have to create and publish a chart once - but it will also change every day.

To create a chart, select your data and then choose the **Insert** menu from the options at the top of the sheet. From that drop-down menu select **Chart...**


The *Chart Editor* window opens. This has three tabs: *Start*, *Charts*, and *Customise*.

It will default to the *Start* chart and suggest a *Recommended chart*, with a preview appearing on the right.


In this example the Chart Editor has recommended a histogram


You can choose what is recommended, or you can click on the *Charts* tab and select a different one: first selecting the general category (line, area, column, bar, and so on), and then selecting the specific type of chart within that (for example the 'line chart' category includes a straight line chart, smooth line chart, combo chart or radar chart)


Choosing a line chart in the Charts tab of the Chart Editor


Whichever you choose, once you click **Insert** the chart is placed in the same sheet as your data.

**Hover over the upper area of the chart and your cursor should change to a hand**, allowing you to click and drag the chart so it is not obscuring the data.

If you click on the chart you can also further customise it. For example, clicking on the title allows you to change and format that.

The key area to look for is the upper right corner of the chart, where there should be a down-pointing triangle.

Click on that to open a menu which includes the **Publish chart...** option.


That should open a new window titled *Publish to the web*. Here you have two options:

1.  To **link** to a webpage containing the chart;
2.  Or to get some code allowing you to **embed** the chart on your own webpage


<aside class="warning blurb">

If you have a site hosted on Wordpress.com the embed code will not work: Wordpress does not allow iframe embedding (the type used here). Instead you can always take a screengrab and link that to a webpage containing the chart using the **Link** option.

</aside>

Make sure you are looking at the **Link** options if that is what you want, or the **Embed** options if that is what you want.

Whichever it is, you should have two drop down menus. These allow you to choose different charts in your workbook, and whether you want 'interactive' (the chart responds to mouse actions like rollovers) or 'image' (it doesn't).

Click **Publish**.

The window should now change to show a URL for the published chart (if you picked **Link**), or the HTML code to embed it (if you picked **Embed**).


Copy and paste this into a new window to see the live chart.


So far, so standard. But here's the magic bit. *Try changing the data*, and see what happens.

Well, this is what happens if you change the stock symbol being grabbed:


This is *exactly the same URL*, but the chart has now changed *because the data feeding it has changed*.

Now, in reality that change doesn't happen instantly. The best way to test it is to use two different browsers: this prevents *caching* whereby a browser stores the webpage and doesn't properly refresh it by fetching the whole thing all over again.

In other words, when your chart is first published, copy the URL and open it in the same browser - let's assume that's Chrome.

When you change the data, or the data updates itself, paste the same URL into another browser: let's say Firefox, or Opera, or Safari, or (if you really have to) Internet Explorer.

You should see the change more quickly.

Of course after 10 or 20 minutes you should also be able to refresh the page in your original browser (Chrome, remember) and see the change too.

That's just testing. As I said, the real beauty here is that you don't have to change the data if you're using a function like `GOOGLEFINANCE` which is always grabbing data for that day or, if you're specifying historical data, data *relative* to today.

And that's not the only function you can use in this way. Think back to the chapters on Google Sheets' `IMPORT` functions: `IMPORTHTML`, `IMPORTXML`, `IMPORTFEED`, and `IMPORTDATA`. Any of those could also allow you to pull in data from elsewhere, and then publish a live chart which gives a visual representation of the data at that moment.

Cool.

### Recap

- Google Sheets can generate **live charts** which will update when the underlying data does (with a little lag).
- These charts can be found under **Insert \> Chart...**
- Once created, select the drop-down menu in the upper right corner of the chart, and then click **Publish chart...**
- **You can choose to *link* to a live chart on a webpage created by Google, or *embed* the same chart**.
- **You can also choose either a static *image*, or a more *interactive* version which presents extra information when the mouse rolls over data points**.
- When you click **Publish** a box will appear containing either the URL, or the HTML code to embed the chart.
- You can **use functions that fetch live data** to feed your live charts to get the best out of both. Those functions include `GOOGLEFINANCE`, `IMPORTHTML`, `IMPORTXML`, `IMPORTFEED`, and `IMPORTDATA`.

### Exercise: grabbing and visualising live data with `IMPORTHTML` and live charts

If you want to put some of these techniques into practice, here's a useful exercise:

Find a table which is regularly updated with numbers. For example, [Nottingham Trent University publishes monthly data on how much electricity each building is saving compared to others on campus](http://www.ntu.ac.uk/ecoweb/carbon_challenge/league_table/index.html); while the Irish Nurses and Midwives Organisation [publishes a daily 'Trolley Watch' table](http://www.inmo.ie/6022) showing how many additional patients are on beds, trolleys or chairs "above the stated complement" (it also has a live chart).

1.  Use `IMPORTHTML` to pull that data into a Google sheet. You might also try using `IMPORTXML` if it's not in a table and you're feeling ambitious.
2.  Use the techniques in this chapter to generate a chart for that data. But there's a problem: if there are numbers in the table that you don't want in the chart, you can't move them around (because the table is generated live by a formula in one cell, and cannot be altered). So how can you solve that?
3.  Once solved, generate a new chart based on that selection of data, and make it a live chart using the steps detailed in this chapter.


