<!-- chunk: 1/3 | source: 10-finding-stories-spreadsheets.md | words: 32508 -->
<!-- headings: Finding Stories in Spreadsheets; Recipes for interviewing data - and getting answers; Paul Bradshaw; Table of Contents; Guide; Introduction; Starter jargon: cells, sheets and workbooks; Stories about change, stories in context: basic calculations; Cell references; Calculating a change; Calculating a proportion; Ratios: calculating a proportion as '1 in 10'; Combining both: calculating what proportion a change is; Recap; Find the story: are there more drunk and disorderly arrests?; Saving time to hit a deadline: repeating and fixing a calculation across cells; Shortcut: repeating a calculation down hundreds of cells with one double-click; What if I want to fix the cell reference so it doesn't change when pasted?; Recap; The last chapter's story: are there more drunk and disorderly arrests? -->

## Finding Stories in Spreadsheets

### Recipes for interviewing data - and getting answers

 

#### Paul Bradshaw

 

This book is for sale at <http://leanpub.com/spreadsheetstories>

This version was published on 2019-07-29


\*   \*   \*   \*   \*

This is a [Leanpub](http://leanpub.com) book. Leanpub empowers authors and publishers with the Lean Publishing process. [Lean Publishing](http://leanpub.com/manifesto) is the act of publishing an in-progress ebook using lightweight tools and many iterations to get reader feedback, pivot until you have the right book and build traction once you do.

\*   \*   \*   \*   \*


For Orrell, Entwistle, Howard and Sewart, who did something noble I will always be grateful for.


## Table of Contents

<nav xmlns:epub="http://www.idpf.org/2007/ops" epub:type="landmarks" id="guide">


## Guide

1.  [Begin Reading](#chap00.xhtml)

</nav>


## Introduction

I've yet to meet a spreadsheet that didn't have a story to tell.

More often than not, they are bursting with those stories.

Some have stories of success and (often more interestingly) failure. Others can hold a mirror up to ourselves, and tell stories about where we've been, and where we're going; how we've changed, and how we've stayed the same.

Some spreadsheets will shout stories of alarm, while others whisper about curiosities we might have otherwise missed. Some will tell stories about secrets. Some will tell stories about lies.

The key to all these stories, as with all sources, is knowing *what questions to ask*.

This book is about those questions.

In fact, it is *full* of those questions, in the language that spreadsheets understand. They include questions like:

- How much has something changed?
- Who or where experienced the most change? Who changed the least?
- Which company or person got the most money?
- What is typical - and who stands out the most as being atypical?
- How often does a name appear? Where?
- Can you show me just the parts I'm interested in?
- How much was spent in total on something?
- Have I got things right?
- Where is information missing?
- What is unusual in this data?
- Where should I be looking?

Some techniques in this book are about helping the spreadsheet get into a position where it can answer questions it couldn't answer before: breaking dates down into years or months, extracting regions or names, for example, or combining it with other sets of data.

**If you are new to spreadsheets** you can read the book in the order it's written, with each chapter building on concepts and techniques introduced in the chapter before, plus a number of exercises and questions to give you spreadsheet experience alongside exercising your editorial muscles - the latter is just as important as the technical skills if you're going to be telling stories.

But the book is also written for **those who already have spreadsheet experience**: you can dip into chapters like a recipe book to find the chapter that tackles the question you want to ask. And once you've read it the first time, it's designed to be used again and again that way.

For that reason, please don't approach the book as something to be 'memorised' from beginning to end - it is better to remember what's possible *in general* with spreadsheets, and play with the techniques that are useful to you.

Then, when you need to do something particular, you will know you can find it in these pages.

The more often you use particular techniques, the more they will be retained in your memory, and the less you will need to refer to this book.

Oh, and if you have a question which isn't answered here, let me know and I'll try to update the book.

Later I will tackle some useful tips and techniques when getting to know a spreadsheet. But first, let's get stuck in with some basic calculations.

<aside class="tip blurb">

#### Starter jargon: cells, sheets and workbooks

I'll be using a number of terms from the start which I should explain now:

People often talk about 'spreadsheets' to mean one of two different things: either a document containing a number of different *sheets* of data, or just *one* of those sheets.

To avoid confusion I'm going to use the phrase **workbook** to refer to a spreadsheet *document* as a whole, and **sheet** or **spreadsheet** to refer to one of those individual sheets.

I'll also talk about **cells** - these are the individual boxes on a spreadsheet containing a piece of data.

</aside>



## Stories about change, stories in context: basic calculations


Working out a proportion can generate surprising results - and raise more questions


At its most basic, a spreadsheet acts as a calculator. They can add, subtract, divide, and multiply, and through a combination of those can calculate averages, proportions, rates, and various other things which can provide an insight into the data.

Calculations in Excel are normally referred to as **formulae**, and every formula begins with an equals sign:

`=`

This tells Excel that you are not directly entering information, but rather are expecting it to do some *work*.

After the equals sign comes the calculation. Try the following in any cell in an empty spreadsheet:

`=15+145`

As soon as you press Enter, the calculation is performed and the cell shows the result (160 hopefully).

Most of the time, however, Excel is used to perform calculations on values that are in cells elsewhere in the spreadsheet.

### Cell references

Every cell in a spreadsheet has its own reference, based on the row and column it is in. The very first cell, for example, is in column A and row 1, which makes it cell **A1** (the letter can be found above at the top of the column; the row number can be found to the far left).

The cell next to that in column B is **B1**, (different column, same row); and the cell *underneath* A1 is **A2** (same column, different row).

If in doubt, you can find out the **cell reference** (the location of the cell - in this case A1) by selecting it and looking along the bar just above your column letters.


To the left of this bar is a box that shows you the cell reference, and after that is a longer box which shows what that cell has in it. That longer box is called the **Formula bar**.

Note that if the cell contains a formula, you will see the formula and *not* the results of the formula - which is what you see in the sheet itself.

These cell references make it possible to perform calculations on data in your sheet.

For example, try typing 15 in cell A1, and 145 in cell B1.

Now in cell C1, type the following:

`=A1+B1`


The formula in C1 - note that the formula bar above shows the formula while the cell shows the result


That formula adds whatever value is in A1, to whatever is in B1.

There are two advantages to this:

- If the value in A1 changes, your formula automatically re-calculates. Try it and see (make sure you press Enter after changing the value).
- If you have two or more columns of numbers and want to create a new column full of the same calculation for each row, it's very easy to do so.

We'll see the second in action in the next chapter.

### Calculating a change

Before then, it's worth exploring some commonly-used calculations you'll need to tell stories from your data.

One of the most common of those stories is about *change*. Change is, almost by definition, newsworthy, and an integral part of storytelling. When things change, it makes the news.

But how big a change was it - and from what?

A calculation to find out how much something has changed is a straightforward subtraction:

**What something is now MINUS what something was before**.

For example: if this year there were 1000 assaults in Aberdeen, and last year there were 600, the calculation is:

`1000-600`

The result of that is `400`. In other words, assaults have gone up by 400.

Sometimes you will get a negative result, which means something has dropped.

Let's change our example to show that: this time let's say this year there were 1000 assaults in Aberdeen, and last year there were actually 1100. Now the calculation is:

`1000-1100`

And the result is `-100`. In other words, assaults have gone down, by 100.

Unfortunately, when we look at change in terms of an absolute number: up by 400, or down by 100, that doesn't tell us whether 400 or 100 is a lot, or not very much. And that's when *proportions* come in handy.


This story is based on calculating a proportion - although it needs the context of what the proportions are for techniques other than restorative disposals


### Calculating a proportion

An equally common calculation used in stories about numbers is **what proportion one thing is of another**. Here are just a few examples:

- [95% of Birmingham events budget spent on Conservative Party Conference](http://www.birminghampost.co.uk/news/regional-affairs/questions-over-95-birmingham-events-7028090)
- [US spends 17.9% of its GDP on healthcare](http://www.theguardian.com/news/datablog/2012/jun/30/healthcare-spending-world-country)
- [The most successful UK universities get 11% of their alumni to donate money](http://www.nytimes.com/2007/04/15/weekinreview/15lyall.html?pagewanted=print&_r=0)
- [Almost one in three criminals given treatment which involves speaking to their victims reoffend](http://www.maidenhead-advertiser.co.uk/News/Areas/Maidenhead/Almost-a-third-of-criminals-given-restorative-disposals-reoffend-05022014.htm)

Calculating a proportion is a simple division: **dividing a part by the whole**.

If the US spends \$2.6 trillion on health, and its total GDP is \$14.5 trillion, then to get the proportion above you divide 2,600,000,000,000 by 14,500,000,000,000.

The result is 0.179 (rounded down to three decimal places) - or 17.9%.

How is 0.179 the same as 17.9%? A useful approach is to think of it like this: 1 is the same as 100% - anything below 1 is a *fraction* of 1: 0.5 is *half* of 1; 0.25 is a *quarter* of 1; and so on.

0.5, then, can also be expressed as 50%, and 0.25 can be expressed as 25%.

To see those decimals as percentages we can do one of two things: either multiply them by 100 (0.5 x 100 = 50) to bring them to the other side of the decimal place, or simply change the formatting of the cell containing the result.

The latter is probably the better practice, as it retains the 'true' number and we can still perform calculations with it (100 times 50% is 50, for example, whereas 100 times 50 is 5000).

To do this, right click on the cell and select `Format cells...` - or use the keyboard shortcut CTRL+1. On the window that appears change the formatting to **Percentage** - you can also specify how detailed that percentage is.


### Ratios: calculating a proportion as '1 in 10'

One of the examples above doesn't present the proportion as a percentage, but rather a *ratio*: *1 in 3*. This is a particularly clear way of presenting a proportion: it's much easier for readers to visualise the proportion 'one in three' than the rather abstract figure of '33%' (which you can get if you divide one by three - 0.33, or 33%).

So how do you express a percentage as a ratio? The most straightforward way is to look at the clear markers along the way.

For example:

- 0.05 is one in twenty (5%)
- 0.10 is one in ten (10%)
- 0.20 is one in five (20%)
- 0.25 is one in four - or a quarter (25%)
- 0.33 is one in three (33%)
- 0.40 is two in every five (40%)
- 0.5 is one in two (50%)
- 0.6 is three in every five (60%)
- 0.66 is two in every three (66%)
- 0.75 is three-quarters, or three in every four (75%)
- 0.8 is four out of every five (80%)
- 0.9 is nine out of every ten (90%)
- 0.95 is nineteen out of every twenty (95%)

Whatever your figure is, look at the proportion closest to it, and use that as a basis with the qualifier 'more than' or 'almost'.

For example:

- 0.06 is 'over one in twenty'
- 0.09 is 'almost one in ten'
- 0.23 is 'more than one in five'
- 0.27 is 'over a quarter'
- 0.36 is 'more than one in three'
- 0.39 is 'just under two in every five'
- 0.49 is 'almost half'

...and so on.

You can also use multipliers of some of the proportions in the main list: 0.15, for example, is three times 'one in twenty' and so could be expressed as 'three in every twenty' and 0.3 is 'six in every twenty'.

The more you do this, the more it becomes second nature. Until then, keep the list above as a useful reminder.

### Combining both: calculating what proportion a change is


This Washington Times story on welfare spending is all about calculating change as a proportion of the previous figures


So back to our change in assaults. Now we know how to calculate a proportion, we can calculate just how significant that rise of 400 assaults, or fall of 200, is.

The question is: what do we divide it by? The latest number, or the older one?

The answer lies in the way we would express it: 'Assaults have risen' or 'assaults have fallen'. Implicit in that is this: '*from what it used to be*'.

So: **you must divide your change by the original figure it has *changed from***

If assaults were 600 and have gone up to 1000, we need to work out how big a change that represents from the original figure of 600, i.e.

`=400/600`

The result is 0.66 - 66% higher, or two-thirds higher, *than its previous figure*.

The fall of 100 means a calculation like this:

`=-100/1100`

That's -0.09, or a drop of 9% *from its previous figure*.

Now when it comes to increases you need to be very careful about your language. You might talk about something being 66% *higher*, but you can also talk about figures being 166% what they were (the 66% increase plus the original figure - 100%). Make sure you are clear yourself about what it is you are saying.

Beware also of confusing *percent* with *percentage points*: the latter is used more often in politics, where a party's lead on a rival party might increase from 3% to 6% - that's an increase of three *percentage points* but also a 'doubling of their lead'. Try to avoid using "percentage points" outside of these very specific areas where usage has been better established, as they can cause confusion.

Another issue is whether you use the word 'percent' or the symbol '%'. If in doubt, check the style guides available online such as the [APA grammar of percentage](http://blog.apastyle.org/apastyle/2011/11/the-grammar-of-mathematics-percentage.html)

To see this process in practice, look at just one story in The Washington Times, *'[Welfare spending jumps 32% during Obama's presidency](http://www.washingtontimes.com/news/2012/oct/18/welfare-spending-jumps-32-percent-four-years/?page=all)'*. The numbers behind the headline are given low down in the article:

> "Welfare spending as measured by obligations stood at \$563 billion in fiscal year 2008, but reached \$746 billion in fiscal year 2011, a jump of 32 percent."

So, 746 minus 563 is 183. 183 divided by 563 (the starting figure) is 0.325 - or 32.5%.

### Recap

- Calculations are called **formulae** in Excel and other spreadsheet software
- A formula begins with an equals operator like so: `=`
- Formulae can work with numbers or strings (indicated by quotation marks), but are most likely to use **cell references** like `A2` or `B300`.
- To calculate how much something has changed, take what something is now minus what it was before.
- To calculate what proportion the change represents, take that amount of change and divide it by the earlier figure (that it's changed from).
- Try to express proportions as a ratio such as 'almost one in ten' or 'over a quarter' - often this is easier for the reader to take in and understand than a dry, precise percentage - unless the precision is important.
- Beware of confusing *percent* with *percentage points* - the latter is used much less and has a different meaning.

<aside class="exercise_blurb blurb">

### Find the story: are there more drunk and disorderly arrests?


At [this link](https://docs.google.com/spreadsheets/d/1iUMiNs7P5P1mEQXwsFDgIn8dF5ZnO4YhRcAEMsmciVI/edit?usp=sharing) you'll find a simple spreadsheet showing the number of people arrested for being drunk and disorderly in every month for two years. Download it by selecting **File \> Download as \> Microsoft Excel (xlsx)** or **Comma-separated values (CSV)**.


You want to know *if arrests are going up or down*. Here's how:

1.  Open the spreadsheet. Create a simple formula in D13, at the end of December's figures, to calculate the change in arrests that month between 2011 and 2012
2.  Did it go up or down? By how much?
3.  Can you write a new calculation to work out how much that is as a percentage change? Remember that you're looking at that change as a percentage of arrests in the *first* year.
4.  Can you express that calculation as a proportion, e.g. 'one in ten' or 'half of'? What proportion would it be?
5.  Why might it be important to have arrest numbers for each month of the last two years, rather than just looking at how arrests have changed in the last two months?
6.  What headline might you use for this story - and what terms might you avoid?
7.  Apart from whether arrests have gone up or down between the two years, what other stories might we look for in this data?
8.  We'll cover how to repeat this calculation for all months in the next chapter, but see if you can copy the calculations for all the months.

I'll give the answers at the end of the next chapter.

</aside>


## Saving time to hit a deadline: repeating and fixing a calculation across cells

At the end of the last chapter I mentioned two advantages to using cell references in your calculations (for example: `=A1+B1`). In particular the fact that you can create a whole column full of calculations with a double-click.

Let's continue with the data you typed in during the last chapter (if you don't have it any more there's a screenshot below) to do that now:

- Type 20 in cell A2 and 110 in cell B2.
- Select cell C1 where you typed your first formula, and copy it (press CTRL+C - CMD+C on a Mac, or right-click and select *Copy*)
- Move to cell C2 and paste what you've just copied (press CTRL+V - CMD+V on a Mac, or right-click and select *Paste*).


Crucially, when you copy and paste a formula with cell references in Excel it **doesn't paste exactly the same formula** - it changes the cell references *relative* to where you are copying from.

Why? Because it assumes - probably correctly - that you don't want to do the same calculation with *exactly* the same figures again. Instead it assumes you want to do the same calculation but with different figures: the figures in the next row, or column.

If you're copying and pasting a formula down a column, it will apply it to the relevant figures in each *row* (in our case, the numbers in columns A and B in each row).

If you're copying and pasting a formula across a row - for example, where you want to calculate a grand total for the values in each column above - it will apply it to the relevant figures in each *column*.

Try that now, then. In cell A3 type the following:

`=A1+A2`

Now copy that formula and paste it into cell B3. There, it should change to:

`=B1+B2`


### Shortcut: repeating a calculation down hundreds of cells with one double-click

Now, copying and pasting a formula over and over is a silly way to spend your time, so if there's only one shortcut you remember in Excel it's this one: the **black cross double-click**.

Double-clicking on the black cross copies a formula down a column; clicking and dragging it copies the formula across or down whatever range you want.

To see this in action, first delete the formula you pasted in cell C2 so we're back to where you were after you'd typed the first formula in C1.

Now, **click on C1** so that that cell is selected. When you hover over that cell, or any other, your mouse pointer should be a white cross. This is the 'safe' cross - you can't do anything with this other than select cells.


The ‘safe’ white cross


To get the *black cross* move your pointer over the bottom right corner of the cell (where there's a small block) until it changes to a black cross. This cross is actually called the **fill handle**


The black cross - or fill handle - appears when you hover over the bottom right corner of a cell


When the black cross appears you can do a couple of things:

- *Click and drag* across or down cells to copy that formula across those (again, changing the formula so it applies to cells in different columns or rows), or:
- *Double-click* to copy the formula down until it hits an empty cell to the left

This last option is an enormous time-saver. As long as your cell is *to the right of a column which doesn't have any empty cells*, when you double-click that black cross, it will repeat the formula all the way to the bottom of the table - potentially thousands of rows.

For this reason the shortcut is **best attempted next to a column that you know to be full**.

<aside class="tip blurb">

Remember that it doesn't matter whether your formula is written in the cells before the data that it's calculating with, or after. And you can always cut the column and move it where you want it (right-click at the top of the column, select **Cut**, then right-click on the column you want to insert it next to, and select **Insert cut cells**).

</aside>

### What if I want to fix the cell reference so it doesn't change when pasted?

If you want to write a formula where one of the cell references stays the same when the cell is copied and pasted, you use the **dollar sign** to fix each part of it.

Take the formula `=B1+B2`, for example. If you want that B1 to *always* be B1, no matter where you copy it, add dollar signs before the `B` and the `1` like so:

`=$B$1+B2`

Now try copying that cell to other places on your sheet. You'll notice that `B2` changes relative to where you've pasted it, but `$B$1` always stays `$B$1`.

You can also just fix the column reference, or the row reference, by using the dollar sign once like so:

`=$B1+B2` (to fix the `B` but not the `1`).

`=B$1+B2` (to fix the `1` but not the `B`).

In other words, place the dollar sign *before* the part you want to fix.

In most cases **it's simplest to fix both the row and column**. But there may be occasional cases where you want to copy and paste a formula and only want to fix part of that. When you come up against that situation, come back here.

### Recap

- If you **copy formulae** down or across into new cells, any cell references will be changed accordingly. When copying *down*, for example, the row reference (the number) will change. And when you copy *across*, the column reference (the letter) will change. This is because Excel assumes you want to apply the same formula to the cell in that row or column.
- If you *don't* want to change a cell reference when copying formulae, **use the dollar sign** before the part of the cell reference you want to fix, e.g. `$A$2` to fix a reference to cell A2 wherever that is copied to.
- To copy a formulae down an entire column, select the cell containing it and hover over the bottom right corner of that cell so that your cursor changes from a white cross to a **black cross**. Then double-click. This only works as long as there is data *to the left*.

### The last chapter's story: are there more drunk and disorderly arrests?

At the end of the last chapter I set a series of challenges for a dataset showing the number of people arrested for being drunk and disorderly in every month for two years. Here are the answers:

1.  The formula to calculate the change in arrests between December 2011 and January 2012 is `=C13-B13`. In other words: the December 2012 arrests minus the arrests in December 2011.
2.  Arrests went down by 27.
3.  To work out how much that is as a proportion you can use the formula `=D13/B13` (assuming your formula to calculate the change is in D13, and the December 2011 arrests figure is in B13). This should give you the result `-0.107569721`, which you can format to two decimal places as `-0.11`, or -11%.
4.  You can express that as "A drop of more than one in ten" or "a tenth fewer arrests", but that's not too pretty so you might end up plumping for 'a drop of 10%'. It's a style choice.
5.  If you only had arrest numbers for the last two months, it might be influenced by seasonal factors. For example, December - not surprisingly - is a high month for drunk and disorderly arrests compared to the preceding month. We want to compare like with like, and November and December don't allow us to do that. Comparing one December with another, however, does.
6.  A headline might say 'Drink arrests down by a tenth' or 'Xmas drink arrests drop', or something similar - but we couldn't say 'Drunkenness down by a tenth' or 'Fewer drunks at Xmas, say police'. This is because we need to be careful that we talk about *arrests* rather than drunkenness, because the two are not the same. Arrests *may* be down because fewer people are getting drunk and disorderly, but they could also be down because police resources are being deployed elsewhere, or because there are fewer police officers this year due to cuts, or because of changes in policy, law or strategy (for example, the police force deciding to caution rather than arrest, or laws being changed to make it harder to make an arrest for that offence). It might be a combination of all those factors, and others.
7.  Other stories in this data might include a look at monthly fluctuation: December/January and July/August seem notably higher than other months. You could speak to a police officer in a unit which tackles alcohol-related crime, or talk to the police press office, about why that might be and how they plan for that. You might get reaction to the figures from local pubs or businesses affected. You might look ahead to future initiatives.

Be prepared to move your data 'angle' down the story as it becomes less about the data and more about the conversations you have as a result of the data. In a story about a new initiative to tackle drunkenness, the data becomes background, not the lead.

And of course, there's nothing stopping you doing *all* those stories: the surprising numbers; the reaction to those; the feature on what it's like to police Friday night; the brief piece about a new initiative; and so on. Before you know it, it's time to get the next year's data and start all over again.

<aside class="exercise_blurb blurb">

### Find the story: drunk and disorderly arrests

Now you know how to copy a calculation down a column, try approaching the [drunk and disorderly arrests data](https://docs.google.com/spreadsheets/d/1iUMiNs7P5P1mEQXwsFDgIn8dF5ZnO4YhRcAEMsmciVI/edit?usp=sharing) afresh, and type a calculation that works out the change at the end of the first row of data, then use the black cross double-click to repeat it down the column.

Repeat the same process for a second column calculating what *proportion* that change represented year-on-year.

Which month had the biggest change? And which the lowest?

</aside>



## How much did it cost? How many people were affected? The first function: adding a series of cells with `SUM`


Financial totals can make attention-grabbing headlines - although it isn’t always made clear why it’s significant


When it comes to numbers of people, however, the significance is often clearer. This story from the Birmingham Mail has a simple premise: how many people have been affected by a new policy


One of the most common stories you'll want to tell with a spreadsheet is 'How much did it cost?' These are *grand total* stories, and involve one of the most basic calculations you will want to perform in your spreadsheet: **adding up the values across a number of cells**.

Now, you could do this with a very long formula like so:

`=A1+A2+A3+A4+A5`

...And so on. But that would be laborious. It is for this reason that spreadsheets have what are called **functions**.

Functions are words that have special meanings in Excel and other spreadsheet software. They are a shortcut for a series of instructions.

The function for adding up a series of cells, for example, is called `SUM`. All you need to do to use `SUM` is tell it what cells you want to add up, in parentheses after the function.

<aside class="warning blurb">

### Functions in different languages

Throughout this book I will be using the English language names for functions. However, if your spreadsheet software is not set up to use English then many functions will have different names. `SUM`, for example, is still `SUM` in Danish, but `SOMMA` in Italian and `SUMA` in Spanish and `SOMA` in Portuguese.

Many translators of Excel functions are available, including [Dolf Trieschnigg's website](http://dolf.trieschnigg.nl/excel/index.php), or you can search for 'Excel function SUM in Russian', replacing the function and language names with your own.

</aside>

To add the values in cells A1 to A5 using that function, then, you might write the following:

`=SUM(A1:A5)`

It is easiest to think of functions as being like recipes: instead of having to write out 'add this and then add that and then add that' you can simply say: 'use the CAKE recipe with these ingredients', or 'use the PIE recipe with these ingredients'.

Once you know that you can start to guess which sets of common instructions are going to be recipes - functions - in your spreadsheet software. Here are just a few instructions which have their own one-word functions:

- 'Add all these figures up'
- 'Calculate an average for these figures'
- 'Tell me if a cell contains an error'
- 'Count how many numbers I have in this column'
- 'Extract the month from this date'
- 'Replace the full stops in this cell with commas'

There are dozens and dozens more, too.

Once you know this, you can start to *search for useful functions whenever you come across a task or problem which you think others may have already solved*, adding the word "function". For example, you might search Google for 'Excel function extract day from date' or 'Google spreadsheets function count blank cells'.

<aside class="information blurb">

#### Why functions and not buttons

You can perform sums and other basic calculations using some of the buttons in Excel, but I'll be focusing on functions in this book for a few reasons:

- Firstly, typing functions is often quicker than using buttons. It's especially quick when you want to combine results - for example using a sum as part of a bigger calculation. You also have more control over where the results go.
- Secondly, the placements and availability of buttons varies widely between spreadsheet software, and between different versions of Excel, so it's difficult to give a consistent guide to their use. Knowing functions means you can use the same techniques whatever version of spreadsheet software you end up on (although there are a few which are specific to Google spreadsheets or Excel - I'll mention this at the time).
- Finally, once you get beyond basic calculations there won't always be buttons available to do what you need. You might as well start as you mean to go on...

</aside>


Another SUM story - this time adding up how much empty housing there is across a number of countries


Using Freedom of Information to find out the costs of things is a well-worn approach - this article also picks out the biggest single spends, giving it more concrete details and context


### If functions are recipes, arguments are the ingredients

You can't cook a recipe without ingredients, and so (just as with our `SUM` example) every function is followed by at least one ingredient, in parentheses. These are called **arguments**.

In our first example above, `SUM` was the function and `A1:A5` was the argument.

Sometimes you will get an error message because you didn't 'supply the right arguments'. For example, you may have submitted too many or too few (or none at all). Normally the error message will give you clues, and even a link to more information. And of course you can search for more information on that error. But knowing the jargon helps.

<aside class="information blurb">

#### Argument or parameter?

You may see the term **parameter** also used to refer to a function's ingredients. This is the name for what type(s) of ingredients a function needs *in general*. So, for example, the `SUM` function has one parameter: a range of cells to add up. But the *formula* `=SUM(A1:A5)` supplied one **argument**: the *specific* range of cells A1 to A5.

In other words, when you read about a function you will hear about the parameters it uses; but when you actually use them, you will be supplying your own specific arguments. The same jargon is used in programming (for example, advanced scraping or data visualisation), where functions are common, so if you understand this you'll have a head start if you decide to try out programming.

</aside>

Back to our formula, then. You'll notice that we specify a range of cells using the colon symbol:

`=SUM(A1:A5)`

So if we wanted to add all the cells from A1 to A500 we could adapt it like so:

`=SUM(A1:A500)`

You can also select cells across more than one column. If we wanted to add all the cells from A1 in the top left of our range to B500 as the bottom right (last) cell we could select them with this range:

`=SUM(A1:B500)`

Crucially, functions like SUM which work with numbers will **ignore any words in the specified cell range**. In other words, text does not cause it any problems.

For that reason, if all you want to do is add up all the numbers in a column you can often do so much more quickly by just using the column *letters* like so:

`=SUM(A:A)`

This simply means: *use the SUM function on all the numbers in column A*.

The same principle applies to rows:

`=SUM(1:1)`

Would mean *add the values in all cells in row 1*.

<aside class="warning blurb">

#### Checks to make when specifying a column- or row-only range

If you are going to specify a column or row range such as A:A or 1:1, check the following:

- The heading is not numerical, e.g. years or dates. If they are, they will be included in the sum.
- There is no grand total at the bottom of your column or the end of your row. This will also be included in the sum, giving you a total twice as large as it should be.
- There are no further tables beneath the one you are working with (the formula would add all numbers in column A in that table too).

You can check these issues quickly using the keyboard shortcuts explained in the chapter on getting to know the spreadsheet - CTRL or CMD and the cursor keys - to explore the edges of your table.

</aside>

### When there's more than one ingredient: commas and semicolons

The SUM function is a simple recipe, and so only needs one ingredient. But other functions take more than one - as we'll see in further chapters.

In these cases, each ingredient - argument - is separated by a comma (in English language versions of software) or semicolon (in Spanish, Portuguese, German and other language versions).

In fact, SUM is unusual in that it can take one or *more than one* argument: you can add more than one range of cells by simply adding a comma or semicolon between each one like so:

`=SUM(A1:A5,A7:A9)`

`=SUM(A1:A5;A7:A9)`

This adds together the values in cells A1 to A5, and from A7 to A9.

But before we come on to other functions with multiple ingredients, there are some other simple ones to explore.

<aside class="information blurb">

For the rest of this book I'll be using commas, but remember to use semicolons instead if your software uses those.

</aside>

### Recap

- **Functions** are words that have special meanings in Excel and other spreadsheet software: a shortcut for a series of instructions.
- Functions are always followed by parentheses containing the ingredients it needs. These are called **arguments** (specifically) or **parameters** (in general).
- If a function uses more than one parameter, each one is **separated by a comma or semi-colon**, depending on the language of the software you're using.
- You can **search for useful functions** whenever you come across a task or problem which you think the designers of the spreadsheet software may have already solved, adding the word "function".
- Specify a range of cells by putting a colon between the first and last cell in that range, e.g. `A2:A300`.
- You can *more quickly* **select a whole column or row** by only using the letter or number of that column or row, e.g. `A:A` or `1:1`

<aside class="exercise_blurb blurb">

### Find the story: drunk and disorderly arrest totals

To finish with our [drunk and disorderly arrests data](https://docs.google.com/spreadsheets/d/1iUMiNs7P5P1mEQXwsFDgIn8dF5ZnO4YhRcAEMsmciVI/edit?usp=sharing), type a calculation using the `SUM` function that **works out the totals for each year**.

1.  What formula will add up all the numbers for 2011, and what formula will do the same for 2012? (You can always copy the calculation into a cell to the right and it will apply relevant cells for the next year)
2.  Why might using a column range like `B:B` not be a good idea in this case?
3.  What formula would calculate the change from 2011 to 2012?
4.  Based on the result of that, what formula would calculate that change as a percentage?
5.  What simple stories might you tell about these totals?
6.  What other data could you look for to make a stronger story?

The answers will be at the end of the next chapter.

</aside>


## Who's top, who's bottom? `MAX`, `MIN`, and sorting


This piece in The Independent is based on maximums and minimums


One of the simplest stories to tell about data is who's top and who's bottom. And there are a number of ways of quickly finding these stories in your spreadsheet.

Clearly, you're generally looking for the biggest and smallest numbers in a particular column. You *can* bring these to the top of your spreadsheet by clicking somewhere in your data and using the **Sort** functionality in Excel - by clicking either the **Sort** button:


The sort button in Excel - note the drop-down options next to it


...or selecting **Sort** from the **Data** menu.


The sort option in Excel’s data menu


The *button* - if your software shows it - is often faster. But make sure your headings are in the first row first (we'll talk more about checking your data out in the next chapter).

Choosing **Sort** from the *menu*, however, will give you more *control*.

This is because the menu option brings up a new window where you can specify how you want the data to be sorted based on multiple criteria:


The sort window in Excel


- Firstly, you specify the column to be sorted on (if you don't have headings in your first row, this will either use the text that's there instead, or you can untick the box marked *My list has headers* in the upper right to be given choices to sort on Column A, B etc.)


The sort window in Excel


- Secondly, you can specify what to sort on (normally values)
- Thirdly, you can specify the order: initially A to Z or Z to A, although if you select a numerical column this will change to 'Smallest to largest' or 'Largest to smallest'. You can also select a 'Custom list' - for example sorting by days of the week or months of the year.

At the bottom left of the window are a 'plus' and 'minus' button which allow you to add or remove extra sort criteria. Each new criteria is applied in order: for example in data on crime you might sort by the number of offences first (largest to smallest), and then by the name of the police force in alphabetical order (A to Z), or by size of force, and so on.

Although this sort functionality is very useful, sometimes you simply want a quick answer to the question: "What's the biggest value in this range of cells" - or you want to use it in a bigger calculation. For that, the `MAX` and `MIN` functions come in very handy.

### MAX and MIN

`MAX` and `MIN` are quite simple functions: they only need one argument: the range of cells you want to find the maximum or minimum number in. A typical formula which brings back the biggest number in column B, then, might look like this:

`=MAX(B:B)`

Or you might specify a particular range within that column like so:

`=MAX(B2:B4123)`

Once you press Enter, the calculation is performed, and you should see the biggest number from that range in the cell where you typed the formula.

You can try this with some test data.

Let's say we're writing a story about a charity fun run. One of the obvious stories to tell might be who the oldest and youngest runners are.

To show how you might find those using Excel, **type a small table with some names and ages** like this:


Now in an empty cell - preferably to the right of your main table and with an empty column in between - type your `MAX` formula.


When you press enter you should see the biggest age 'returned' (displayed). That's the age of the oldest runner:


But the formula is still working, so if the data changes - a new, older, runner enters, or the oldest runner drops out, this will be reflected in the cell where you typed the formula, which should now show the new value.

If you **add a new entry who is older than the rest**, your `MAX` formula result will change to reflect this - assuming it was looking at that cell too. This is why using a *column-only* range like `B:B` is often simpler than specifying row *numbers* too (conversely, you might specify row numbers to avoid including any new entries which come after them).


Note that `MAX` and `MIN`, like most number-only functions in Excel, will helpfully ignore text, so a formula which looks down the whole of column B will ignore the headings and any text entries such as 'N/A' or 'no data'.

The `MIN` function works in exactly the same way: it needs to know which range of cells you want the minimum value from, like so:

`=MIN(B:B)`

Or so:

`=MIN(B2:B4123)`

You can try this with your own data under the previous formula:


Now, we have no way of knowing how many times this maximum or minimum appears, or which person they relate to. For that you might want to use the **Sort** options detailed above, but you can also use other functions detailed in later chapters: particularly `COUNTIF` (for counting how many times it appears) and `VLOOKUP` for finding the name next to it.

But what we *can* do is combine the result of the `MAX` or `MIN` formula with another to work out the proportion of the total.

For example, if we had a column showing how much different runners had raised for charity, we could use the `MAX` function to identify the most money:


We could then use the `SUM` function to calculate the total raised by everyone:


To work out what proportion of fundraising the biggest fundraiser was responsible for, we just need to divide the *biggest amount* raised by the *total* raised:


The result is expressed as a decimal (unless your cells are formatted differently) - in this case it means 43% (you can reformat the cell as percentage to see that, or multiply it by 100):


So we might report that just one fundraiser was responsible for raising 43% of money, or "over two fifths", or that four in every ten pounds were donated to one particular fundraiser.

We could use the same functions to work out an average - but there are better functions for that, which we'll come on to next.

### Recap

- Use the **Sort buttons** to bring the biggest and smallest values in your data to the top.
- Use the **Sort option** in the *Data* menu to sort on more than one column at the same time (e.g. by amount and then by name, alphabetically).
- The `MAX` function will give you **the biggest number** in the range of cells specified.
- The `MIN` function will give you the *smallest* number in the range of cells specified.
- **A formula is always working**, so if the data changes the result of your formula will change in response.
- Numerical functions like `MAX` and `MIN` **will ignore non-numerical data**, so it's no problem if your range contains text or empty cells too.
- You can calculate how much that is as a proportion of the total by taking the results of your `MAX` or `MIN` formulae and **dividing that part by the total** (or the results of the `SUM` function)

### The last chapter's story: drunk and disorderly arrest totals

At the end of the last chapter we looked to finish with the [drunk and disorderly arrests data](https://docs.google.com/spreadsheets/d/1iUMiNs7P5P1mEQXwsFDgIn8dF5ZnO4YhRcAEMsmciVI/edit?usp=sharing) by working out the totals for each year. Here are the answers:

1.  The formula to add up all the numbers for 2011 is `=sum(B2:B13)`. The formula to do the same for 2012 is `=sum(C2:C13)`
2.  Using a column range like `B:B` is not a good idea in this case because it will also add the years in the heading - 2011, or 2012.
3.  The formula to calculate the change from 2011 to 2012 is `=C14-B14` (assuming you typed the `SUM` formulae in those two cells).
4.  The formula to calculate that change as a percentage would be `=D14/B14` (assuming the formula above is in D14 and the first year's total is in B14).
5.  Two simple stories you could tell would be about the number of arrests last year, or the change between years, e.g. 'Drunk and disorderly arrests down 16%' or '2400 arrested for being drunk and disorderly last year'. The latter could be made more meaningful and concrete by converting into a daily or weekly rate, e.g. '46 people a week arrested for being drunk and disorderly in 2012'
6.  Two years' data isn't a lot to draw conclusions - a 16% drop could be significant, or typical: we don't know. So more historical data would help provide more context. You might also look for national rates (are arrests down nationally, and at a higher or lower rate? Does this data 'buck the trend'?), or data on neighbouring areas to see how these figures sit in that context. You might also add population data in this case to draw conclusions on arrests per person in each region.



## Detour: getting to know the spreadsheet - useful shortcuts and tips to avoid mistakes

In the last two chapters we came across some potential pitfalls in our data when using cell ranges: the `SUM` function, for example, can include grand totals if we're not careful; while using the *sort* functionality in Excel often relies on your headings being in the first row.

For that reason it's worth knowing how to explore your spreadsheet quickly whenever you first open it, in order to check for common problems and make sure your data is fit for your purposes.

[Here's one spreadsheet](https://drive.google.com/file/d/0B5To6f5Yj1iJZm10WmtlUUVpaWM/edit?usp=sharing) (select **File\>Download** to save a version to your computer) which is typical of the sort of data some organisations publish - it looks fine to a human, but presents us with a number of problems should we want to dig a little deeper using spreadsheet software.


Here are just some pitfalls to watch out for when you receive a dataset:

- Empty rows in the middle of the data
- Empty columns in the middle of the data
- Grand totals at the end of the data
- Rows before your header row which Excel thinks are your headers
- Data which looks like one thing (e.g. numbers) but Excel thinks are another (e.g. text)
- Merged cells

Now look at that image again. Empty rows in the middle of the data? Check. Rows before your header row which Excel thinks are your headers? Check.

Some of these are easy to spot at the top of the data, but others - well, you can get tired of endless scrolling. Instead of that - which can be time-consuming, clumsy and imprecise, try the following keyboard shortcuts:

### Keyboard shortcuts to explore your data quickly

- Select the first cell in your data. You want to be in a column which should have no empty entries - normally the first column fits the bill.
- Hold down CTRL (CMD on a Mac) and the *down arrow key*. This should take you down to the cell *before the first empty cell* in that column.

In most cases, this will be the last cell with data in it. But not all.

Look around this first empty cell. Some spreadsheets will have more data *below*: it may be a *different table* with new headings, or it may be a *new section of data in this table* (for example, a second region).

<aside class="information blurb">

In some cases, it may just be an empty cell, and the data continues in another column. In that case, move to that column, and repeat the process: hold down CTRL (or CMD) and the *down arrow key* to take you down again until you hit a completely empty row.

</aside>

As far as Excel is concerned, if there's an empty row then that's the end of one table of data, and the start of another. If you want to make any calculations that involve both, you may have problems.

There's another thing to look for in this last cell of data: it may be a **grand total**. You need to know this, because again, if you want to make calculations a grand total might cause an error, such as double-counting your values.

I'll mention when these features become problematic elsewhere, but it's good to check the edges of your data first so you know what's there.

You can use similar keyboard shortcuts for going to the other edges of your data:

- Hold down CTRL (CMD on a Mac) and the *up arrow key* to take you up to the cell *below the first empty cell* in that column (or the very first cell if there are no empty cells above).
- Hold down CTRL (CMD on a Mac) and the *right arrow key* to take you to the cell on the right *before the first empty cell* in that row. (Again, this might be the last cell, or you can see that there's more data after the empty cell)
- Hold down CTRL (CMD on a Mac) and the *left arrow key* to take you to the leftmost cell *before the first empty cell* in that row (or the very first cell in that row if there are no empty cells to the left).

Try these shortcuts so you know where the last column and row is.

### Changing your data: remove empty rows before the headings

<aside class="warning blurb">

#### First copy your data!

Before you make any changes to a spreadsheet, **make a copy of it**. You can then always go back to it if you make a mistake, or check back against this copy to make sure you haven't got things wrong. Select `File > Save As...` to save the working version under a different name.

You may want to make more than one copy at different stages - giving them names based on which version they are, or what question you're answering.

</aside>

Some official data will come with several rows of descriptions before the actual headings. That's helpful to you - but confusing for Excel, which will look for your headings in row 1.

To delete a row, right-click on the **row number** to the left of the cells and select `Delete` from the menu that appears. For example, to delete row 1, click on the number 1 at the start of that row.


To delete more than one row at once, *click and drag* from the first row number to the last row number you want to delete. Then right-click in the numbers you've just highlighted and select `Delete` from the menu that appears.

For example, to delete the first five rows click on the row number 1, hold down the mouse, drag down to the row number 5, then release. Right-click on any of those numbers while highlighted and you'll see the menu with `Delete` on it.

The same process applies to deleting empty columns at the start of your data: right-click on the A at the top of the first column and select `Delete` to remove that; click and drag across more than one column letter to highlight them and then delete those.

At the end of this process the first row of your sheet should contain your headings. If the headings are split across more than one row then you may need to tidy them up so that this isn't the case - but not necessarily: it depends on what you want to do (see notes in the relevant chapter).

<aside class="warning blurb">

#### Dealing with merged cells

Merged cells are a particularly awkward problem. To un-merge cells you can normally select all your cells and then in the **Home** menu in Excel, select **Unmerge cells** from the *Merge* menu ([more on the Office help pages](https://support.office.com/en-us/article/Merge-and-unmerge-cells-5cbd15d5-9375-4540-907f-c673a93fcedf)).

That's the easy part. The difficult part is making sure that doing so does not put **values in the wrong place** (or result in values missing from the place they should be). In one case, for example, I worked on a government spreadsheet which used merged cells to indicate values for two administrative areas which at one point in the period covered were a single unit, but at other points were separate.

In a case like this it is best to explore specific data cleaning processes and tools like Open Refine, which are not covered in this book. *[Using OpenRefine](https://www.packtpub.com/big-data-and-business-intelligence/using-openrefine)* by Verborgh and De Wilde, provides a good introduction.

</aside>

### Recap

- **Use the *CTRL+cursor key* keyboard shortcuts**ÃŸ to explore the edges of your data at the start of any project
- **Watch out for empty rows** - Excel will treat this as the end of one table and the start of another. If this isn't the case, remove them.
- If your heading row isn't the first row, **delete other rows that come before your headings** (such as page titles).
- **Always keep a copy of the unaltered data** so you can check against it later, or revert to it if you need to.


## Hitting the deadline: understanding and formatting the data - number or text

Do spreadsheets dream of electric sheep? Do they think?

Spreadsheets certainly look at data in a particular way, and if you're going to ask a spreadsheet to do something for you, it helps if you see things from its point of view.

Having explored the edges of your data - just a few seconds with those keyboard shortcuts - it's well worth taking a quick look at the columns and checking what types of data they contain.

You may see names, dates, amounts, addresses - but broadly these are going to fit into two types:

- Numbers
- Text

If your spreadsheet software gets the data type wrong, that can cause problems in two ways:

- If it thinks a number is text, it cannot perform calculations with them.
- If it thinks text is a number (for example a reference code or telephone number), it might strip out a zero at the start, or display it in an odd way (for example showing a reference code as a date)

There's a quick way to see at a glance what type of data Excel thinks it is dealing with: if it thinks you have filled a cell with **text**, it will align it to the **left**. If it thinks that information is a **number** it will put it to the **right**.


In this data text is left-aligned and numbers right-aligned. Note how the ID codes are aligned left because they contain numbers and text


<aside class="information blurb">

There are two other types of data which you are unlikely to come across in published spreadsheets but which you may end up generating yourself by using formulae: TRUE/FALSE values (sometimes called **Booleans**); and errors (generally preceded by a hash, such as `#N/A` or `#ERR`). We'll tackle these in later chapters.

</aside>

### Numbers

What a number looks like to you depends on how it's been formatted. An amount of cash, for example, could be shown as any of the following:

- Â£6,500,000
- 6500000
- 6500000.00
- 6,500,000

<aside class="information blurb">

#### Integers and floats

Strictly speaking, there are more types of numbers - particuarly **integers** - whole numbers with no decimal places - and **floats** - numbers that include decimal places. If you ever come across that jargon, you'll know what it means.

</aside>

You can change this by highlighting the cell or cells containing the data (click, or click-and-drag), then right-click and select `Format cells...`. Alternatively, you can use the keyboard shortcut CTRL+1 (CMD+1 on a Mac).

This will open a window with various options down the left hand side: number, currency, date, and so on.


If you click on any of these, the main area of the window on the right will show further options: for example, whether you want thousand separators (commas or full stops depending on the conventions of your country), how many decimal places you want to show, and whether and where you want to include a currency symbol (you can also choose which symbol).

<aside class="tip blurb">

#### What if it's a number but Excel thinks it's text?

If you have numbers that Excel thinks is text, try to remove the things that may be causing this. For example, currency signs can sometimes be problematic - use the Find and Replace option (normally under *Edit \> Find...* - then select the *Replace* button or tab) to find and replace all currency signs (leave the 'replace with' box empty).

Extra spaces can also be problematic. I once saw a spreadsheet where payment amounts were treated as text because each amount was preceded by a *space and a pound sign*. It was that space that was the real problem - but to be safe we copied the space and pound sign, then pasted it into the *Find* box in the Find and replace window so we knew it was replacing exactly what we'd found.

</aside>

### Text

It's easy to focus on the numbers in your data, but Excel can also perform calculations with text. These include:

- Counting how many times a particular piece of text occurs
- Testing if a particular piece of text contains something else, such as a specific string of characters
- Measuring the length of text
- Splitting text on particular characters or at particular points
- Extracting parts of text

Some things that look like numbers are actually text: you're not going to want to perform calculations with phone numbers, for example.

Conversely, some things that look like text are actually numbers: 11th September 2011 is recorded by spreadsheet software as a number (40797 in most cases) so that it can perform calculations with that date, such as which date was the earliest and latest, or how many days, minutes or months elapsed between two dates.

But if your spreadsheet is showing those dates as text (aligning them to the left, or failing to perform calculations) then you may need to extract the numerical information from those dates separately - see the chapter covering dates for more information.

### Recap

- Excel treats most data as numbers or text. This limits the calculations it can perform on that data.
- Excel will align data to the left if it thinks it is text; it will align data that it thinks is numbers to the right.
- You can format data so it appears differently using the *Format* option - this includes converting decimals to percentages, adding currency symbols and thousand separators, and specifying how many decimal places to show.



## Best sellers and averages: `MEDIAN`, `AVERAGE` and `MODE`


This article is based on looking at averages - but it uses medians because the data is financial


Averages may not sound noteworthy - after all, we tend to assume news is interested in the extremes of who's top and bottom - but they form an important benchmark to a number of stories we can tell with spreadsheets.

By their very nature, some things will always be above average or lower than average. A headline that screams *'Half of hospitals below average'* is statistically illiterate, or at least pretending to be. But averages do provide a context over *time*.

For example, if an individual hospital, school or police force is performing *consistently* well below average, we may want to investigate further (causes may or may not be under the institution's control: local deprivation, understaffing or even poor data collection may all be factors)

Averages can also be useful to compare lots of individual pieces of data in a clear way. If we want to fairly compare the performance of sportswomen or organisations, for example, it is often better to compare their average performance than their best or worst individual performances, at least if we are interested in consistency or the bigger picture. Here are just two examples:

- [Comparing the social media performance of articles on different news sites](http://www.themediabriefing.com/article/social-media-analysis-of-3-explanatory-journalism-sites-vox-fivethirtyeight-538-theupshot) - images below.
- [Comparing average life expectancy with average 'healthy life expectancy'](http://www.interhacktives.com/2014/05/09/visualise-healthy-life-expectancy-disparity/) (how many years a person can expect to live in good health).

And thirdly, averages, of course, *change*: and change is generally newsworthy. Take, for example, the following:

- [An article on how length of the average life sentence in Ireland has increased](http://www.irishexaminer.com/ireland/average-lsquolifetermrsquo-in-prison-rises-to-18-years-267499.html)
- [A similar article from the New York Times on how the average length of prison stays in general have changed](http://www.nytimes.com/2012/06/06/us/average-prison-stay-grew-36-percent-in-two-decades.html?_r=0).


The Irish Examiner’s article shows lengths of life sentences have more than doubled in 30 years, challenging preconceptions


A national census, for example, provides a raft of stories every decade which hold a mirror up to who we are and what we do.

The average age, wage, life expectancy, and other factors may challenge our preconceptions: and if it's surprising, it's *news*.

One of the roles that journalism plays is to ensure we have an accurate self-image - as a nation, as a region, a community, or an industry.

If you are wealthier, for example, the evidence suggests you tend to overestimate the average wage, while a significant majority of people tend to think they are 'above average' on measures such as intelligence.

We assume most people are 'like us', except when it flatters our egos, and both can lead to errors of judgement, including political policy that impacts on millions. So a 'journalism of averages' is an essential corrective to those assumptions.

More colourfully, averages also provide a springboard to write about individual towns or cities, teams or companies, and even individuals, which represent the 'State of the Nation' or the 'Face of the Industry'.

### Calculating an average: AVERAGE, MEDIAN or MODE?

Calculating an average is similar to calculating a total, maximum or minimum: you use a function with one parameter: the range of cells you want to use as the basis for the calculation.

But there's a twist: there isn't just *one* function to calculate an average: there are *three*. And that's because there is more than one type of average.

The `AVERAGE` function will calculate a **mean**: that is, what number you would get if you added all the values up and divided by how many values you had.

For example, if you had ten numbers you would add them all up and divide by ten to get the mean.

This is important, because people often assume that an average means half the values are higher, and half lower, when actually that's not always the case with a *mean* average.

The `MEDIAN` function, however, will calculate a median average: that is, what number you would get if you *lined up* all the values from smallest to biggest and picked **the value in the middle**.

In this case around half the values *should* be lower, and half higher (with rare exceptions - see note below).

For example, if you had nine numbers you would line them all up from lowest to highest and pick the number in the fifth position (four numbers are either the same or higher; four are either the same or lower). If you had ten numbers you would line them up in the same way but, because there is no middle position you would take the two in the middle (in this case the fifth and sixth positions) and calculate a mid-point between them.

<aside class="warning blurb">

In some very unusual cases, half of values will not be higher and lower than a median. For example, if your nine numbers include five 5s and the numbers 6, 7, 8 and 9 then the median will still be 5 despite there being *no* numbers lower than that.

This is because when ranged from lowest to highest 5 is still the number in the middle. Half of the values, however, are still *higher*. This doesn't change what you're saying about 5 being the average but it is worth noting this quirk in the numbers, which may be newsworthy in itself, and perhaps expressing it differently as the 'most common'.

If you think your data may be unusual enough to fit a pattern like this, consider testing it using the `MODE` function below, or the `COUNTIF` function detailed in the next chapter.

</aside>

Finally, the `MODE` function will calculate the **most common** value.

This is the least-used type of average, but does come in useful if you want to find out the 'best-selling' item (as long as it's numerical) - for example, the most common shoe size, or the age declared by most users of dating sites.

It is also the best sort of average to use (if you must) when looking at **ratings** such as when customers or citizens are asked to rate service on a scale of 1 to 5 or 1 to 7 (where the lowest number is something like 'poor' and the highest 'excellent').

This is because ratings are actually *categories* not numbers: a rating of 2 is not twice as good as a rating of 1 but a category judgement.

That said, if you are dealing with ratings it is much better to show the proportion of people who gave each rating: for example, "20% rated service as 'excellent' and 10% as 'very good'".

<aside class="tip blurb">

#### Converting text to numbers: IF

If you want to calculate the most common value, but it's expressed as text, see the chapter on the `IF` function to find out how to convert it to a number.

</aside>

Crucially, all three functions will *ignore any text or empty cells in the range specified*.

In other words, the formula `=AVERAGE(A1:A10)` calculates an average across ten cells - but if cell A1 contains a heading (text) it will only divide the total by nine: the numbers of cells containing numbers.


The average shown here is the total of all 9 cells with numbers divided by 9 - even though 10 cells are specified it ignores the text cell


Likewise, if cell A5 happened to be empty, it would ignore that too, and divide the total value of all the cells containing numbers by eight: the numbers of cells being added up.


The average shown here is the total of all 8 cells with numbers divided by 8 - even though 10 cells are specified it ignores the text cell and the empty cell


This is particularly useful if you have large columns of numbers. Let's say you had 15,000 rows in one dataset, and added up all the values using `=SUM`. Would you then divide the total by 15,000 to get an average? What if some were blank? Or contained text entries like "N/A"? The AVERAGE, MEDIAN and MODE functions tackle this problem neatly.

It also means you can safely use the cell range `A:A` without worrying about headers.

Using the three functions to calculate averages for column A would look like so:

`=AVERAGE(A:A)`

`=MEDIAN(A:A)`

`=MODE(A:A)`

Normally your choice is going to be between the 'best selling' line, or one of the two more conventional 'average' measures. So, if it's the latter, which do you choose?

### Man made or natural?

If you are concerned with communication (and this book is all about stories), the key consideration has to be: *what does my audience think I mean when I say 'the average'?*

In most cases, your audience will assume you mean a midpoint, above which half of things sit, and below which the other half sits.

<aside>

If your audience is particularly numerate (financial or scientific, for example) you might assume that they know that an average doesn't necessarily mean the midpoint. However, you might also assume that they also know what a median is.

</aside>

When it comes to natural phenomena - heights, weights, numbers of children, and so on - the mean *is* likely to sit around just such a midpoint: half of heights are likely to be above it, half below it.

But when it comes to man-made phenomena, distributions are not so even - and especially so when it comes to *money*.


This article from The Media Briefing uses medians to compare how many times articles from different sites after readers complained that one ‘big hit’ could skew the mean


In comparison, see how the same data can have a very different mean average


When dealing with data about money we have to remember that, while there may be some unusually large values (executives earning millions; projects costing billions), it is unlikely that there are correspondingly *small* values to counterbalance them (employees whose annual wage would only pay for a loaf of bread; projects that cost pennies).

The [European Investment Bank's loans database](http://www.eib.org/projects/loans/list/) is a particularly good example of this. The *mean* for all the loans listed in that database, calcuated using `=AVERAGE`, is almost 53 million euros. But only *one in four* loans are larger than that amount.

*Three quarters* of loans are actually *below* the mean (how to count that proportion is explained in the next chapter).


The mean average of European Investment Bank loans, and the median average: the difference is almost 30 million euros


This is because a few very large loans skew the mean. Or, put in the words of an old joke about averages:

> "Bill Gates walks into a bar. The average punter becomes a millionaire."

You can reasonably expect that if you wrote that the "average loan was almost 53 million euros", most readers would assume that meant a significant proportion - around half - was of that value or higher.

They would be wrong. Which means you are not writing clearly - with your audience in mind.

A median, in that case, would be better. The median value of those loans was 25 million euros at the time of writing.

And because it's a median, we can say definitively that almost half the loans made were 25 million euros or higher.

The downside is that you may need to explain what a median is, and why you're using it.

Regional newspaper *The Birmingham Post* did this in their [reporting on falling wages](http://www.birminghampost.co.uk/news/news-opinion/jonathan-walker-britains-50bn-pay-4726269) by adding a line which paraphrased what a median is.

Another approach is to add a small box-out which shows the difference between the mean and the median.


Text from an article about falling wages, which uses a median average


Ultimately, you're probably safest working out *both* the mean and median for your numbers (after all, it doesn't take long to type a formula like `=MEDIAN(F:F)`), and seeing how different they are.

If the difference is significant, that may be the start of a story itself. An organisation where the median wage is significantly lower than the mean may be one where the bosses take home large wages. Unusually so? Unjustifiably so? You'd have to look further.

Likewise you can use this knowledge to avoid being misled yourself. An organisation may use an artificially inflated average to gloss over low pay: knowing the difference means you can ask the organisation which boasts "Our average worker earns Â£30,000", "Is that a mean or a median?"

Further enquiries may lead to a story fact-checking and debunking the boast: "Bosses rapped over wage claims as figures reveal most workers earn below Â£25,000".

How do you count how many? That's the subject of next chapter.

### Recap

- **Averages can be newsworthy** in the surprising stories that they tell us about our country, region or industry. They can also be newsworthy in how they change over time or space.
- **Some things will always be above average or lower than average** - that's not news. But being *consistently* so may be an interesting lead to follow - if you pick up the phone and ask questions.
- **There is more than one type of average**: a mean (`AVERAGE`) divides the total by the number of values; a `MEDIAN` is the middle value if you lined up all values from smallest to largest; and a `MODE` is the *most common* value in a selection.
- **A mean average can be skewed by very large values in the dataset**. For that reason it is often better to use a *median*.
- **A mode can be used to identify the *best selling* item** - as long as it is represented by a numerical value.

<aside class="exercise_blurb blurb">

### Find the story: political donations

[At this link you will find a spreadsheet containing donations to British political parties in 2013-14](https://drive.google.com/file/d/0B5To6f5Yj1iJZUphX0N1c2QtbUE/edit?usp=sharing). You can find similar data using [the Electoral Commission's donations database](https://pefonline.electoralcommission.org.uk/search/searchintro.aspx) and selecting the option to download as CSV at the bottom of your search results.

This is a bigger dataset that previously, with over 1,700 rows. Remember to use the CTRL+arrow key shortcuts to navigate to the edges of the data and check for grand totals or other tables.

1.  What was the mean average donation made to political parties during the period covered?
2.  What was the median average donation?
3.  What was the most common donation made?
4.  Can you use the `MAX` and \`MIN functions detailed in the previous chapter to identify the biggest and smallest single donations? Can you use the *Sort* options to identify them?
5.  Can you calculate what proportion the biggest donation was as a percentage of all donations? How might you express that in a story so that it is meaningful (and not just a percentage)?

</aside>


## How many payments? How many people? Counting, not adding up: `COUNT`


The Bureau of Investigative Journalism’s Naming the Dead project is all about counting


In the last chapter we looked at calculating averages, and how some averages are far from representative of the numbers as a whole. At the European Investment Bank, for example, i noted that only a quarter of loans were 'above average'.

But how did I know it was only a quarter? I used one of the *counting* functions.

Counting is different to adding up - or 'summing'. If we were looking at a football club's wage bill, for example, we might *add up* all the wages but *count* how many there were (in other words, how many employees). You might add up all the players' *ages*, and count *how many* players there are over 30, and so on.

A count allows us to put totals into perspective: one football club might have a larger wage bill than another (calculated using SUM), but it might also have more players (calculated using COUNT). Their rivals across the city may have fewer players but be paying them more money each.

The most basic counting function is `COUNT`. Like other basic functions, it only has one parameter: the range of cells you want to count.

A typical formula using it would look like this:

`=COUNT(F:F)`

The `COUNT` function only counts **numbers**. So, as with AVERAGE, MEDIAN and MODE, a heading cell will not be included in the calculation.

The formula `=COUNT(A1:A10)` would give you the result 9 in a range of cells where A1 contained a heading and the other nine contained numbers. And if cell A5 happened to be empty, it would - like the functions that calculate averages - ignore that too, giving a count of eight cells containing numbers.


The formula only counts the cells containing numbers - not headings or empty cells


If you don't want to be so fussy, there are variations on the COUNT function to suit you:

- `COUNTA` will count *anything* - text or numbers - but not blanks.
- `COUNTBLANK` will count just the empty cells

You can combine these however you wish to ask the question you need. For example, if you wanted to know how many cells contained text you could do the following:

1.  Use COUNTA to count all cells with text or numbers in a range of cells
2.  Use COUNT to count all cells with numbers in the same range
3.  Subtract the result of 2 from the result of 1

The safest way to do this would be to perform each calculation in a different column, like so:

1.  In cell C1: `=COUNTA(A1:A10)`
2.  In cell C2: `=COUNT(A1:A10)`
3.  In cell C3: `=C1-C2`

You can also combine them all into one formula - but we'll cover that technique in a separate chapter.

<aside>

#### Describe what you've counted carefully

When writing about what you've counted, make sure you are accurate in how you describe it. The first version of the [story about kidnappings in Nigeria below](http://fivethirtyeight.com/datalab/mapping-kidnappings-in-nigeria/), for example, was based on counting *media reports* of kidnappings, but mistakenly described them as simply kidnappings. The two are not the same.


This story from data journalism startup FiveThirtyEight made a mistake in how it described what it was counting - their apology is useful to learn from


When counting by location, a second mistake was made. Reporter Mona Chalabi writes: "If the location of a reported kidnapping isn't in a media report, GDELT defaults the location to the center of Nigeria. So that part of the country is overrepresented in the animated map."

</aside>

### The story is what's missing: COUNTBLANK

At first glance, `COUNTBLANK` might not look a very interesting formula, but empty cells can be very interesting indeed.

For example, say you had a dataset showing each expense claimed by a group of politicians. One of the columns contains data on what the money was claimed for.

If even 10% of cells in that column were blank - empty - then that means in one in ten claims the politician didn't declare what they were claiming the money for (or someone else failed to record it). At this point you might want to look further to see if this was a general pattern, or one or two individuals with a much higher rate of non-declaration. You'd probably also want to find out what the requirements are: if they're not required to declare this, that's a story. If they are, then what is being done about this?

In any dataset where you would expect full disclosure, `COUNTBLANK` can be very useful in giving a quick overview. You may have also noticed that it's also very useful for non-numerical data such as description fields.

The Bureau of Investigative Journalism's project [Naming The Dead](http://www.thebureauinvestigates.com/namingthedead/?lang=en) is all about missing information: alongside the numbers reported killed is the number who have been identified. Sometimes the story - or the start of the story - is as simple as this.


In the Bureau of Investigative Journalism’s Naming The Dead project, the number reported killed is contrasted against the much smaller number whose identity is known


But what if non-disclosure is not represented by a completely blank cell? What if, instead, someone simply types 'Unknown' or 'N/A', or enters a value of 0, or even 999999?

This is where the second level of counting functions come in - and we'll need a whole new chapter for them.

### Recap

- Counting functions **do not total up values** - they instead count *how many values there are*.
- The `COUNT` function **only counts numerical values** - it ignores text and empty cells.
- You can **use the `COUNTA` function to count numbers *and* text** - but not blank cells
- To find out how many cells have text, simply use both functions and subtract the `COUNT` of cells with numbers from the `COUNTA` of cells with numbers or text, leaving you only the number of cells with text.
- `COUNTBLANK` will tell you \*\*how many empty cells there are in a specified range. This is useful for identifying where there are issues with data because significant amounts of it are missing - a lack of transparency perhaps?

### The last chapter's story: political donations

In the previous chapter I linked to [a spreadsheet containing donations to British political parties in 2013-14](https://drive.google.com/file/d/0B5To6f5Yj1iJZUphX0N1c2QtbUE/edit?usp=sharing). Here are the answers to the questions raised:

1.  The average (mean) donation made to political parties during the period covered was £19,218. This was calculated with the formula `=AVERAGE(B:B)`
2.  The median average donation was only £3,000, calculated with the formula `=MEDIAN(B:B)`
3.  The most common donation was £2,000. We can find that out with the formula `=MODE(B:B)`
4.  The biggest and smallest single donations were £1,744,539.80 and £495 respectively. The formulae to calculate those are `=MAX(B:B)` and `=MIN(B:B)`. Using sort to bring those to the top shows you that the House of Commons was the name of the largest donor (to the Labour Party), and GMB (a trade union) was the source of the smallest donation (also to the Labour Party).
5.  That biggest donation was 5% of all money donated. This can be calculated by dividing the result of your `MAX` formula above, by the result of using a `SUM` function to get the overall total. You can do this in separate cells (one for each formula, then a third to divide the result of one by the other), or all at once with the following formula: `=MAX(B:B)/SUM(B:B)`. You might that in a story so that it is meaningful by saying "One in every twenty pounds" or similar

<aside class="exercise_blurb blurb">

### Find the story: missing donations data?

1.  Use the `COUNT` function to calculate how many numbers there are in your donations spreadsheet's donations column (*Value*). Is that how many you would expect? Use CTRL and the downward arrow to quickly get to the bottom of the column and see what row number it is.
2.  Use the `COUNTA` function to calculate how many cells in the column contain numbers *or* text. Is the result what you would expect? Why?
3.  Use the `COUNTBLANK` function to calculate how many *empty* cells there are in the cells where donation amounts should be.
4.  Use the `COUNTBLANK` function to calculate how many *empty* cells there are in the column describing the *Nature / Provision* of the donation. Why might these cells be empty? What other information in the data can help you understand possible justifications for these cells being empty?
5.  Do the techniques above tackle all possible ways that people might avoid giving information?

</aside>



## Only count if... setting criteria for a formula: `COUNTIF`


This Daily Mail story counts how many staff earn above a particular threshold - how would you report this story?


The `COUNTIF` function allows us to count how many cells in a particular range *meet a specific criteria*. This means it needs *two parameters*: the range of cells we want to check; and the criteria we want to count against, like so (don't forget to check if your software uses semicolons instead of commas):

`=COUNTIF(A1:A10,"10000")`

These criteria can be numerical or textual. In the example above, we're counting how many cells in the range A1:A10 contain the value "10000". If we wanted to count how many contained the word "Wages", we would write it like so:

`=COUNTIF(A1:A10,"Wages")`

Note that in both cases we put quotation marks around the criteria. In fact, the formula with a numerical criteria doesn't need them, but it's a good habit to get into because not having those quotation marks can cause problems in other situations. For example, if we type a word or symbol without quotation marks, Excel will assume we're referring to a function, or are asking it to do something else.

<aside class="information blurb">

#### Quotation marks and strings

The term for a series of characters within quotation marks is a **string**. The quotation marks indicate that there is nothing special about these characters: they are just that - a *string* of characters to be checked against or inserted.

</aside>

### Counting something specific

It's unlikely that you'll be counting specific numbers anyway. More likely is that you'll be counting how many values are greater than, or less than, a particular value.

To do that, you can add a 'greater than' or 'less than' symbol before the value like so:

`=COUNTIF(A1:A10,">10000")`

This formula is now saying '*Count how many cells in the range A1 to A10 contain a value greater than 10000*'.

You can also use this symbol for 'greater than or equal to':

`>=`

And this one for 'less than or equal to:'

`<=`

In our European Investment Bank loans data, then, once we had calculated the *mean* we could use that with `COUNTIF` to count how many cells had a value *higher than that*. And we could do the same with the *median* too.

Once we knew how many cells were above average, we could divide that by the number of cells containing numbers (using `COUNT`) to find out what percentage of that total the number represented (0.25, or 25%) (See the chapter on calculating proportions and percentages if you need a refresher on this process).

### Looking for cells containing words within sentences: the wildcards


If you want to count how many cells contain ‘Iraq’ or ‘Italy’, COUNTIF allows you to do that - although this story from Ampp3d probably just used a pivot table…


The formula `=COUNTIF(A1:A10,"Wages")` looks for cells containing the string of characters "Wages" - but, importantly, it will only count *exact matches where cells only contain that and nothing else*.

In practice, using text strings like that with `COUNTIF` only works properly if your data is very consistently entered - and text entries often aren't.

Once, for example, I collected some data about decisions by a body responsible for hearing appeals against Freedom of Information decisions. In those decisions the BBC was described in different rows as 'BBC', "B.B.C.", and 'British Broadcasting Corporation". A simple `=COUNTIF(A:A,"BBC")` would only have picked up one of those three.

Even where the naming looks consistent, some cells may have extra spaces before, after, or in the middle, which will not match your criteria exactly (Excel counts a space as a character).

The only situations where text is entered consistently are where the person entering data is selecting from a drop-down list of limited possibilities.

Assuming that's not the case, we might need to broaden our criteria.

You can do that with the `COUNTIF` function by adding **wildcards**. These perform the same role as the Joker - the wildcard - does in many card games: it can stand for *any card*.

There are two wildcards you can use: the asterisk, and the question mark. Here's an example using the question mark - note that it goes inside the quotation marks to form part of your string:

`=COUNTIF(A1:A10,"?ages")`

The **question mark** means '*any single character*'. Described in full, the formula says 'Count how many cells in the range A1 to A10 contain any single character followed by a, g, e, s.'

So in this example the formula would count cells that contain 'Wages', 'Cages' and 'pages', but not 'sausages' (because 'saus' is not a single character) or 'ages' (because there is no single character before it).

For this reason, the question mark is the least used of the two wildcards. It is useful if you are looking for a very limited number of possibilities, but otherwise you'll probably need the **asterisk**.

Here's an example of using the asterisk wildcard:

`=COUNTIF(A1:A10,"*ages")`

The **asterisk** means '*none or any characters*'. With this wider option the formula now counts cells that contain 'Wages', 'Cages' and 'pages', 'sausages' *and* 'ages', plus sentences such as 'My skin ages'.

But because the asterisk is only at the start, it will *not* match any cells where there are any characters *after* the characters 'ages', including spaces. So 'My skin ages every day' will *not* be counted, because it does not match the criteria 'none or any characters followed by a, g, e, s.'

Neither will 'sausages are cool', or 'sausages.' (the full stop at the end does not appear in our criteria), or even 'sausages ' (the space after the last character isn't in our criteria either).

To solve this problem, you may want to place asterisks both before and after the specific characters, like so:

`=COUNTIF(A1:A10,"*ages*")`

<aside class="tip blurb">

#### The value of the space

The space character can be very useful when counting. Try adding a space *before* or *after* your wildcard so that the formula only counts when there is also a space in the place you expect it to be (before or after a word, for example).

If you were looking for 'hire' as a word in some contexts, but didn't want contexts where it was part of 'shire' then `=COUNTIF(A:A,"* hire*"` - with the space between the wildcard and the 'h' - would do that.

</aside>

### Trial and error: the single-cell test

Using wildcards can be a process of trial and error: too narrow and you may miss results; too broad and you may catch results you don't want to count.

For that reason, instead of using `COUNTIF` to count across a whole column, one useful technique is to create a series of `COUNTIF` formulae which each count a *single cell*.

These formulae would be copied down a new column, giving a series of results which would be 1 or 0 for each cell.

By sorting that column to bring all the positive results to the top, you could quickly identify the matches and see if any don't match what you're looking for.

For example, you might create a column next to column A which has the following in the first 3 cells:

`=COUNTIF(A1,"*ages")`

`=COUNTIF(A2,"*ages")`

`=COUNTIF(A3,"*ages")`

...and so on (copying the cells all the way down). This way, once sorted, you can look at all the positive results (the ones that count '1' match) and see if they are what you were meaning to count.

You can even use `=SUM` to total up the numbers in that column and give you a total number of matches.

<aside>

#### Case study: Finding corporate torchbearers using COUNTIF

How do you find a needle in a haystack? As part of [one investigation into Olympic torchbearers](https://leanpub.com/8000holes) I wanted to pull out which torchbearers mentioned corporate sponsors in their stories. I could have used the *Find* option - but that would have meant doing it over and over again. So, instead, I used the `COUNTIF` function to bring them all to the top.

The formula was relatively simple. `=COUNTIF(A1,"*adidas*")` would tell me if cell A1 contained none or any characters followed by 'adidas', followed by none or any characters. Copying that formula down the whole column (6,000 nomination stories), and then **sorting** the table on that column brought 21 rows to the top where the result was '1'.

[Seven of those matches had additional stories](http://helpmeinvestigate.com/olympics/adidass-torchbearers-share-a-common-story/) - and further investigation revealed that many of them were executives at corporate partners of adidas, breaking the guidelines issues by the organisers of the Olympic Torch Relay. It was a quick way to find the leads in a large dataset.

</aside>

### Counting against combined criteria: COUNTIFS

One final counting function, `COUNTIFS`, adds something extra: *combined* criteria.

Let's say I was looking at a table of sports results and wanted not just to count how many times the home team had scored more than 2 goals - but how many times *one particular team* had scored more than 2 goals.

If the home team was in column A and the goals for in column C, a typical `COUNTIFS` formula to calculate that would look like this:

=COUNTIFS(A:A,"Liverpool",C:C,"\>2")

The `COUNTIFS` function can have any number of arguments, as long as they are *even*: two, four, six, eight, and so on are all fine. This is because they work in pairs. If the function has an *odd* number of arguments - i.e. not all pairs - then it will generate an error: **Not enough arguments were entered for this function**.

In the formula above, there are two pairs - two sets of criteria: cells in column A containing "Liverpool"; and cells in column C containing a value 'greater than 2'.


A countifs formula to count how many rows meet two criteria


You can add as many other criteria as you like - but remember that the formula only counts how many *rows* meet *all* your criteria. It does not count how many meet *either*.

A good way to think about this is to follow the logic of a computer, which runs something like this:

- Go through each row.
- Does the cell in column A contain "Liverpool"? No? Then move to the next row, and don't count.
- Yes? Then check the next criteria. Does the cell in column C contain a value greater than two? No? Then move to the next row, and don't count.
- Yes? Are those all the criteria? Yes? Then count this row.

If you want to count things that match either one thing *or* another, then you'll need the `OR` function, which we'll cover in another chapter. Before then, we have more to find out about this whole 'if' business...

### Recap

- The `COUNTIF` function counts **how many cells in a range meet a criteria** (specified by you in the second parameter)
- It's best to get in the habit of **putting your criteria in quotation marks** to avoid errors.
- Numerical criteria can be a specific value, like "1000" or "500", or it can **use operators** like the symbols for 'greater than' or 'less than'.
- **Text criteria have to match exactly**, including spaces - unless you use a *wildcard*.
- The question mark wildcard `?` represents 'any single character'
- The asterisk wildcard `*` represents 'none or more of any character'. It's much more flexible and used more often than the question mark wildcard.
- You can **use spaces intelligently** to exclude wildcards applying to a wider range of matches than you want.
- You can also **position wildcards intelligently at only the start or end** of your text to specify where you expect your specified characters to appear
- You can use `COUNTIF` against a range to count how many cells in that range meet the criteria - but **you can also use `COUNTIF` against one cell at a time** to give a 'yes' or 'no' answer (1 or 0) for each row.
- The `COUNTIFS` function **counts cells against more than one criteria**
- The `COUNTIFS` function **must have pairs of cell ranges and criteria** or it will generate an error.

### The last chapter's story: missing donations data?

1.  There are 1766 numbers in the donations spreadsheet's donations column (*Value*) according to the results of the formula `=COUNT(B:B)`. Given that the last value in the column is in row 1767 (using CTRL and the downward arrow to quickly get to the bottom of the column and see what row number it is), that is how many we would expect.
2.  There are 1767 cells containing text or numbers in the donations spreadsheet's donations column (*Value*) according to the results of the formula `=COUNTA(B:B)`. This is what we would expect based on the 1766 numbers identified above, plus the one heading cell containing text.
3.  There are no blank cells in the cells where donation amounts should be - that is those from B2 to B1767. The formula to use to check that is `=COUNTBLANK(B2:B1767)` - using `=COUNTBLANK(B:B)` will count all the blank cells in that column *underneath* the table, which we don't want to count.
4.  The column describing the *Nature / Provision* of the donation is column H. The formula `=COUNTBLANK(H2:H1767)` tells us how many blank cells there are in that column and this table. The cells may be empty because there is no requirement to report that information for particular types of donation (or the description only applies to certain types of donation). Column G is a useful clue: if you use CTRL and the downward arrow in column H to quickly skip to the blank cells you may notice that they are consistently of the type 'Cash' or 'Exempt trust'. Does this justify non-reporting? Best to pick up the phone and ask.
5.  The techniques above *don't* tackle all possible ways that people might avoid giving information. As you scanned the information you may have noticed the use of 'Other' as a description of the nature of their donation. That isn't exactly helpful. Similar examples might include 'No detail provided' or 'N/A' or even '-', which would be counted as a text entry.

<aside class="exercise_blurb blurb">

### Find the story: how many donations fit the bill?

Still in the [spreadsheet containing donations to British political parties in 2013-14](https://drive.google.com/file/d/0B5To6f5Yj1iJZUphX0N1c2QtbUE/edit?usp=sharing), it's time to be a bit more specific in our counting. See if you can find out the following:

1.  How many donations are below £1,000?
2.  What proportion of donations are below £1,000? (Not the proportion of total donations, but the *number* of donations).
3.  How many donations are described as being of donor type 'individual'? What is this as a proportion? How might you express this in a story?
4.  How many donations were made to either the Scottish Green Party or the Scottish National Party? What is this as a proportion?
5.  How many donations were both 'individual' *and* below Â£1,000?
6.  What further data might you need to provide extra context for the Scottish party donations?

</aside>


## If... continued: setting criteria for a sum: `SUMIF`

`COUNTIF` isn't the only function that allows you to set conditions for a calculation. The `SUM` function we met in an earlier chapter has its own equivalent: `SUMIF`.

`SUMIF` can have either two or three arguments (ingredients). The third argument is something new: an **optional argument**.

You can tell that this argument is optional because it will be enclosed in square brackets on the tooltip which appears when you type the function in Excel or free spreadsheet software such as Google Spreadsheets and open your parentheses.


When you open the parentheses on a SUMIF formula, the optional argument is indicated by square brackets


The reasons for this argument being optional are best explained with a concrete example.

Let's say we wanted to *add up* how many goals were scored by the home team in games where that team scored more than 2 goals (this is the 'if' part of our formula).

In this example, the criteria (home goals scored) is the same as what we want to add up (home goals).

However, if we wanted to add up how many goals were scored if the team was called "Liverpool", the criteria (team name) and what we're adding (goals scored) are different.

In the first case, we only need two piece of information (arguments): where our home goals are, and what the criteria is for adding them up.

In the second case, we need *three* pieces of information: where our team names are; what the criteria is regarding those; and where the related numbers are that we need to add up.

And that's how the arguments for `SUMIF` run:

- first is the range of cells to be tested;
- second is the criteria to look for.
- And third, if needed, is the range of cells to be added up instead of the first one.

Here's an example of each:

`=SUMIF(C:C,">2")`

*Translation*: for each row, test the value in column C, *if* that value is greater than 2, add it up to the running total.

`=SUMIF(A:A,"Liverpool",C:C)`

*Translation*: for each row, test the value in column A, *if* that value is "Liverpool", add the value in *column C* to the running total.

<aside class="warning blurb">

Note that this formula won't add up cell ranges across more than one column: specifying C:D will not add both home goals from column C and away goals from column D - it will just take the value in the first column (C). To do that you'll need another `SUMIF` formula. For example, this: `=SUMIF(A:A,"Liverpool",C:C)+SUMIF(A:A,"Liverpool",D:D)`

</aside>

If you want to do this for a number of different text categories, you may be better using a **pivot table**. These are explored in my book [Data Journalism Heist](https://leanpub.com/DataJournalismHeist)

We'll return to IF later on - but before then I need to look at some other functions.

### Recap

- `SUMIF` **adds up all the numbers that meet a particular criteria - or where cells in the same row meet that criteria**.
- `SUMIF` has an **optional argument** - this is an ingredient you can use but don't have to (in this case, the range of cells to be added up if it's different to the range you want to apply your criteria to).
- **Optional arguments are indicated by square brackets** in the tooltip that appears when you type your formula.

### The last story: how many donations fit the bill?

Here are the answers to the questions posed at the end of the last chapter:

1.  There are 127 donations below £1,000. The formula used is `=COUNTIF(B:B,"<1000")`
2.  7% of donations are below £1,000. This is calculated by dividing the result of `=COUNTIF(B:B,"<1000")` by `=COUNT(B:B)`. Or, to put it all in one formula: `=COUNTIF(B:B,"<1000")/COUNT(B:B)`
3.  832 donations are described as being of donor type 'individual'. The formula to calculate this is `=COUNTIF(F:F,"Individual")`. Individual donations account for 47% of all donations - the number of individual donations divided by the number of rows of data (1766 - don't forget that the heading row does not contain data). If some rows were missing data you might use the formula `=COUNTA(F2:F1767)` to find out how many rows contained information and divide by that.

The resulting proportion might be expressed in a story as "almost half of all donations to political parties come from individuals, according to new data from the Electoral Commission".

1.  24 donations were made to either the Scottish Green Party or the Scottish National Party. The formula for this is `=COUNTIF(A:A,"Scottish*")` - note that the wildcard is only needed at the end because both parties *begin* with the characters 'Scottish'. As a proportion this is just over 1%, or "only one in every hundred donations".
2.  598 donations were both 'individual' *and* below £10,000. You need the `COUNTIFS` function to do this: `=COUNTIFS(F:F,"Individual",B:B,"<10000")`
3.  All sorts of data might provide extra context for the Scottish party donations - but some that spring to mind include the proportion or number of voters living in Scotland, and the proportion or number of votes that Scottish parties received. Based on those figures, would we expect those parties to receive one in a hundred donations? Are they doing better or worse than those proportions would suggest?

<aside class="exercise_blurb blurb">

### Find the story: what proportion of donations came from small donors?

1.  In the last chapter you *counted* how many donations were under £10,000. Now you can use `SUMIF` to calculate the *value* of all the donations under £10,000.
2.  Work out what proportion of all donations these made up.

</aside>



## Putting the story into context, or looking from a fresh angle: merging data from different tables using `VLOOKUP`

Combining data is often a great way of telling new stories about spreadsheets. For example: you may have one table showing **pass rates** for each school in an area, and another table showing their **addresses**. Combining these would allow you to identify geographical patterns, or to place them on a map.

You could also combine the **addresses** with **poverty rates** for different locations, or **unemployment** to see if there's a possible relationship (remembering that *correlation does not equal causation*), or to identify the schools performing particularly well *despite* local conditions.

The VLOOKUP function is one of the most widely-used tools in combining data in this way. It stands for *Vertical* lookup, and means that the spreadsheet will look up and down a column (i.e. vertically) for whatever you ask it.

<aside>

#### Horizontal lookup?

A similar function, HLOOKUP, does the same across rows (the H standing for Horizontal) - but this is much less often used. It works exactly the same otherwise, however.

</aside>

#### Prepare the ingredients

If you want to merge information from two tables, you need the following ingredients:

- Two tables containing the data, *in the same workbook*. It doesn't matter if they're on separate sheets, or on one. Unless they're very small, however, I'd recommend keeping them on separate sheets.
- Each table must have a column in common. It doesn't have to have the same heading, but it must have the same *data*. For example, both tables could have a column for institution names, or area, or ID code, postcode, and so on. VLOOKUP looks for a match between the two tables based on this.
- That column must be **to the left of anything you want to grab** from a table. So you may need to rearrange your columns a little

Check your data meets all requirements before continuing.

<aside class="information blurb">

#### Getting two sheets into the same workbook

If your two tables are in different workbooks, you can bring them into the same one by doing the following:

- Open both workbooks in Excel.
- Right-click on the tab at the bottom of the sheet you want to move (this will have the sheet name on it), and select **Move or Copy**.
- In the window that appears, there should be a drop-down menu with a list of all the workbooks currently open in Excel. Select the one you want to copy or move this to.
- Tick the box marked **Make a copy** - otherwise this sheet will be taken *out* of this workbook.
- Click **OK** and the sheet should now be in your other workbook.

</aside>

Once you've got all of those ingredients, you're ready to start writing your formula to combine that data.

### Dry run: two small tables on the same sheet

It's best to illustrate this on a small level first, before looking at how it works with larger tables.

- In your spreadsheet, create two very simple tables on the same sheet, with an empty column between them. Give the first table the headings 'Country' and 'Population', and the second table the headings 'Country' and 'Births'. We're going to use VLOOKUP to grab the population from one table and put it next to the relevant country in the other.
- Type some *names* of countries in the relevant column in both tables. At least *some* of the countries should appear in both tables. It doesn't matter what order they appear in - in fact, you'll see the point of VLOOKUP best when the orders don't match up.
- Type some numbers for the populations and births. The numbers don't really matter for the purpose of this exercise - so type any you like.


Now normally these two tables would be much longer, and likely on separate worksheets - but starting this way makes it easier to see the process and avoid some early errors (which we'll come onto later).

Before you write the VLOOKUP formula you need to decide which table, of the two, you want to bring the data *into*. You will write your formula in this table, and it will grab data from the other table.

We'll choose the births one, for two reasons: firstly because our focus is going to be on *births* per person in a country; and secondly because there are more empty columns to the right of this one.

Right-click on the top of the column to the right of the one containing the data that is in *both tables* (in this case 'Country') and select 'Insert' to add a new column after that.

Call this column 'Pop (vlookup)'.


<aside>

You can put your vlookup column anywhere you want, but it makes most sense to put it next to the column containing the data you're looking to match on. You can always move the column of results later.

</aside>

In the first cell of that new column, start typing the formula `=VLOOKUP(`. You'll notice once you open the parenthesis, the tooltip appears telling you the ingredients this function needs.


Here's a rough translation of what those ingredients mean:

- `lookup_value` means the value you are 'looking up'.
- `table_array` means the range of cells (array) containing what you're looking up *and* what you want to bring back.
- `col_index_num` means the index number of the column with the values you you want to fetch back (in this case the populations). An index is a position like first, second, third, and so on - expressed as 1, 2, 3, and so on.
- `[range_lookup]` - this is another optional ingredient, which basically asks whether you want the nearest match.

Put in plainer language, a VLOOKUP formula really means something like this:

`=VLOOKUP(WHAT YOU ARE LOOKING FOR,WHERE YOU ARE LOOKING,WHICH COLUMN TO BRING BACK,NEAREST MATCH - TRUE OR FALSE)`

Let's begin filling this formula up. Our first ingredient is what we are looking for. This is always the cell containing the value that *should* also be in the other table.

That's our country, which is in cell D2. So our formula should now read:

`=VLOOKUP(D2,`


With a comma to end our first ingredient, we now enter the most important ingredient: the range of cells containing that ***and*** what we are looking for.

In this case, that's columns A and B. The best way to do this is to select the range using your mouse by clicking and dragging across the two column letters. After typing a comma to end that ingredient, our formula reads like so:

`=VLOOKUP(D2,A:B,`


<aside class="warning blurb">

#### Using column ranges in VLOOKUP

In the example above we used a column range like A:B for a reason. You could have clicked and drag across a cell range like A2:B4 - but the problem with that is that if you copied this VLOOKUP formula down to the cell below, A2:B4 would become A3:B5 - missing out the first row - and so on.

We don't want to omit rows, so it's generally better to use column ranges like A:C, assuming you don't have extra tables below that you want ignored.

</aside>

Our third ingredient is the index of the column we want to bring back. This will be a number, such as 1 for the first column in our range; 2 for the second and so on.

It's important to remember that this index refers to the column *in that range of cells*. For example:

- In the column range A:C, index 3 is column C (the third column in that range)
- In the column range B:F, index 3 is column D (the third column in *that* range)

And so on.

In our case, we want to bring back the value in the second column: the country's population, so our formula needs to look like this:

`=VLOOKUP(D2,A:B,2,`


The final ingredient may be an optional one, but we do need to specify it.

This is whether we want this formula to grab the nearest match - TRUE or FALSE.

If you don't specify either, Excel will assume you mean TRUE, and it will bring back the nearest match to your value.

In most cases, we don't want this. If we're looking for the population of Afghanistan, we don't want Excel to bring back the population of Armenia.

For that reason, type FALSE for this ingredient (it doesn't have to be upper case), and close the parenthesis:

`=VLOOKUP(D2,A:B,2,false)`


This formula now means this:

`=VLOOKUP(LOOK FOR THE VALUE IN D2,IN THE RANGE A:B,BRING BACK THE VALUE IN THE 2ND COLUMN IN THAT RANGE,BUT ONLY IF IT'S AN EXACT MATCH)`

If your country in D2 was in column A in the other table, it should have brought back the population next to it.

If it wasn't, then it should generate a `#N/A` error.

If you got that error, and didn't expect it, check if you spelled the country exactly the same in both cells, including extra spaces. To check, copy from one and paste over the other.

Also check if the countries are in the *first* column in the range you specified (A:B in the example above)?

Once you've typed the formula once, you can obviously copy it down a whole column to look for each cell's value in turn. When copied to cell E3, for example, the formula should read:

`=VLOOKUP(D3,A:B,2,FALSE)`

And in E4:

`=VLOOKUP(D4,A:B,2,FALSE)`

And so on.

This means you can now write a simple calculation to divide the births by population to get a birth rate per head (or times that by 1,000 to get a birth rate per thousand).


### Using VLOOKUP on data in different sheets

One of the occasions where I used VLOOKUP was to bring together figures on charges for rape with figures on rape reports. These two sets of data were brought into the same workbook, but were clearly much bigger than the tables above, and occupied different sheets.

You can look for data in another sheet like so:

`'sheetname'!A:B`

...replacing *sheetname* with the name of the sheet in question, but not forgetting to include the single quotation marks and exclamation mark.

<aside class="information blurb">

#### Typing a VLOOKUP formula

The best way to avoid mistakes with this formula is to type it as far as the first comma, and then *use your mouse to click on the sheet containing the data you want to bring back*. Then, click and drag across the column letters containing both what you're matching on and what you want to bring back (*clicking and dragging across A and B is quicker than trying to click and drag from A2 to B400, for example*).

Watch the formula box as you do this: the cell references - including the name of the sheet - will be automatically added to the formula as you click first on the sheet and then on the columns.

Before you click on anything else look in that formula box above your spreadsheet. You can continue to edit the formula without clicking back to your original sheet (which you don't need to do anyway). To do this, click in the formula box, and add the final two ingredients.

When you press enter after the formula is finished you will be taken back to the sheet you started on - and the cell with the result.

</aside>

In the rape data, for example, the sheet I wanted to pull data from was called 'rape offences', and so the formula looked like this:

`=VLOOKUP(A6,'rape offences'!A:E,5,FALSE)`

A6 contained the name of a police force. That police force, and around 40 others, were named in column A of the 'rape offences' sheet, and the data I wanted was in column E - so the range I was looking in had to be A:E, and the index 5.

### Those pesky #N/A results

Once again, if there is no match for what you are looking for, it will show `#N/A`. There are three possible reasons for this:

- There is no match at all. The name does not appear in that other table.
- There is no match *in the first column of the range you specified*. Perhaps you specified the wrong range of cells? Check.
- The name *does* appear in that column, but is typed slightly differently. For example, you may have 'Devon and Cornwall' in one table but 'Devon & Cornwall' in the other. That slight difference is enough to create a mismatch.

If you get a column full of `#N/A`, then it's probably a problem with the range you're looking in - or the data you're looking in (or from) is consistently formatted with an extra space or other character which is leading to a mismatch. In the next chapter we'll tackle some useful functions for stripping this out.

If there are lots of #N/A errors, you may need to re-evaluate your data. Perhaps you need another way to match. Names, for example, are often inconsistently used and entered. But codes tend to be much more consistent. If you have the option, use these to match separate sets of data.

Otherwise, even a few `#N/A` results is good news: it means you've got a much smaller manual workload than if you matched them yourself.

You can now *sort* your data to bring those `#N/A` results to the top, and check each one manually.

For that manual process, try using the Find option under the Edit menu (or use the keyboard shortcut CTRL + F) to search yourself for what the VLOOKUP formula was supposed to find.

If your value isn't there at all, then no problem: the formula works: it *should* return an error if there's no match.

If the value is slightly different, then try altering it manually so it matches, and see if the VLOOKUP formula works when you return to the table containing it.

If you find yourself having to make the same sort of change more than once (such as removing a space, or changing an ampersand to the word 'and'), then try some of the functions explained in the next chapter.

<aside class="warning blurb">

#### Storing the results

The VLOOKUP formula is always working, so if the values change anywhere, so will the results of any formula looking in those cells.

That can be a good thing where you want that. But if you want to keep these results as they were, it's a good idea to copy them and then paste on top using Edit \> Paste special \> Values only (or values). This converts the (live) formula into the (static) results.

</aside>

### Recap

- `VLOOKUP` allows you to **combine two sets of data** - but the two sets must have a column of data in common to 'look up'.
- If your two sets of data are in separate workbooks, **move them into the same workbook**.
- The column **doesn't need to have the same heading** in each table.
- If the two sets share more than one column of data, **pick the one least prone to inconsistent naming**. Names of places or organisations, for example, may not use 'and' and '&' consistently, meaning you can miss some matches. But codes that represent each place, person or organisation should not have this problem.
- `HLOOKUP` is a similar function but it **looks horizontally across a row for a match**, rather than vertically down a column.
- In the table containing the data you're looking for (*not* the one where you're writing the formula) **the column containing the matching data must be to the left of what you want to retrieve**. You may have to move the column to achieve this

> To move a column right-click on the letter at the top and select **Cut**. Then right-click on the column before which you want to insert it, and select **Insert cut cells**

- The `VLOOKUP` function has four parameters: the cell containing data you want to match on; the range of cells containing both that same data and some data you want to retrieve; which column *in that range* contains the data you want to retrieve; and whether you want the nearest match (true or false - generally no, so 'false')
- Remember the number of the column containing the data you want back is based on what you've selected, so in the range `B:D`, the second (2) column is C, not B.
- In a formula data from a separate sheet is indicated by its name followed by an exclamation mark, all in inverted commas, before the cell or cell range. Data on 'Sheet 1' for example will be identified by `'Sheet 1!'` before the cell range.
- Once you run the formula cells where a match cannot be found will show the error message `#N/A`. If all your cells show this error, go over the exercise again: check your formula is looking in the right place.
- If you have a few errors sort your data to bring errors to the top and try to work out what the problem might be - do they have something in common on one of the sheets, such as a word such as 'and', or a footnote reference such as `[1]`?

### The last chapter's story: what proportion of donations came from small donors?

1.  The total value of all the donations under £10,000 comes to £3,904,750.26. The formula is `=SUMIF(B:B,"<10000")`
2.  This is 11.5% of all donations, calculated by dividing the result of that calculation by `=SUM(B:B)`. Or you can write it all in one formula like so: =SUMIF(B:B,"\<10000")/SUM(B:B)\`

<aside class="exercise_blurb blurb">

### Find the story: baby names - which are the biggest risers and fallers?

Data journalism doesn't have to be all about hard news and statistics. Here's an example of using spreadsheet skills to react to new data and quickly give the headlines on what's changed since the previous month, year, or even a decade ago.

[Download the data on baby names from here](https://drive.google.com/file/d/0B5To6f5Yj1iJWkJvQWFIc1RXb0k/edit?usp=sharing) (select **File \> Download**) and use `VLOOKUP` to answer these questions:

- Starting in the latest names, can you add a new column to tell you their position a year ago? (given in the other sheet)
- Can you then add a fourth column calculating the change between this year's position and the previous position? Remember a change from 5 to 3 should be 2, and a change from 3 to 5 would be the negative number -2 - you need to check your results to make sure your calculation is the right way around.
- Does the calculation generate any errors where it cannot find a match? Are they not in the data, or has some other error been made?
- Once you've fixed any repeating errors, who is the biggest riser?
- Is this actually the biggest riser? How might particularly big risers be missed in this process?
- How do you tackle the names which didn't appear at all in the older rankings?
- Can you repeat the process to find out the biggest falls from 2013's names? (Clue: you need to start in the older data)

</aside>


## My data is dirty! Basic cleaning using `TRIM`, `CLEAN` and `SUBSTITUTE`

If you're using one piece of data as the basis for another - such as using VLOOKUP to match data - then you may need to clean it up a little.

Thankfully, Excel has a number of functions that take care of that repetitive work. We'll cover many of these over the next few chapters, but we begin with the simplest: `TRIM`, `CLEAN and `SUBSTITUTE\`.

### Those pesky spaces

The most basic is `TRIM`. This will trim extra spaces at the beginning and end of any cell. It needs only one ingredient: the cell you want to trim spaces from. If you wanted to trim cell A2, then, you would write a formula like so:

`=TRIM(A2)`

The example above simply takes whatever is in A2, removes any spaces at the end and beginning, and puts it in the cell where you type the formula. Typically you would need to copy this formula down the entire column to apply it to each cell in turn, creating a new 'trimmed' or 'cleaned' column.

<aside>

#### When is a space not a space? Find and replace

Sometimes what looks like a space may actually be a slightly different character, which `TRIM` will not affect. In this case you may want to use the **Replace...** option in the **Edit** menu.


This opens up a new window where you can specify what character you want to replace, and what you want to replace it with.

Before you select **Replace...** double-click on the cell containing the pesky non-space character and then click and drag to select *only that character*. Then copy it (the quickest way is CTRL+C or CMD+C). Once your *Replace* window is open paste it into the first box (*Find what:*). Leave the second box empty because you want to replace it with nothing.

Click **Replace all** to see the results. It should also tell you how many replacements it's made. That number should match the number of cells you think contain the character. If it's higher it may have affected other cells as well.

Note that using **Replace...** with a normal space character will also replace every space in your data - a rather more brutal and more problematic approach than `TRIM`.

If your problematic space is always in the same position (for example the first character) then you can also look into using the `REPLACE` function - dealt with in a later chapter.

</aside>

### Getting rid of 'non printing' characters: `CLEAN`

The `CLEAN` function is designed to remove a number of invisible characters which are different to the basic space character and so cannot be dealt with by `TRIM` (although they will probably be dealt with individually by using find and replace as detailed above).

You can [find a list of these characters at Ascii-code.com](http://www.ascii-code.com/): they include things like carriage return, escape, back space and horizontal tab.

You use `CLEAN` just as you do `TRIM`: the function followed by a cell reference in parentheses like so:

`=CLEAN(A2)`

The result will be the contents of A2 minus any of those non printing characters.

You can of course combine both like so:

`=CLEAN(TRIM(A2))`

This uses the results of `TRIM(A2)` as the ingredient for the `CLEAN` function, so both are applied.

### And or ampersand? Substituting particular words or characters

Spaces are one thing, but what if you want to deal with other characters? That's where `SUBSTITUTE` comes in. This is a cell-by-cell version of the Find and Replace you might sometimes use on the Edit menu of Excel or Word.

`SUBSTITUTE` needs three arguments: the cell with the text you want to work with; what particular character or characters you want to substitute in that (if they are there); and what you want to replace that with.

There's also a *fourth*, optional, argument: *how many times you want to do the replacing*.

`SUBSTITUTE` is particularly useful when you have one set of data which uses one convention, and a second which uses a different one. The example I've already mentioned is the convention to use an ampersand and the convention to use the word 'and'. Others include:

- Percent vs %
- Decimal places to indicate thousands vs commas
- Dr vs Doctor vs no title at all

If we wanted to 'clean' some data to change the convention being used, we might use a formula like this:

`=SUBSTITUTE(A2,"&","and")`

This means:

`=SUBSTITUTE(THE CONTENTS OF A2, SUBSTITUTE '&', WITH 'AND')`

If the cell does not contain the '&' sign, then it is not substituted. If for some reason, we only wanted it to substitute the *first* ampersand, we could use that extra argument like so:

`=SUBSTITUTE(A2,"&","and",1)`

But otherwise, it will assume we want to substitute *any* instance of '&'.

Again, when copied down a column, it will repeat this process on each cell next to it: A2 becomes A3, then A4, and so on.

Here's an example of that in action with some country names - note that it makes no difference to names without an ampersand, but does change 'Antigua & Barbuda':


#### Replacing something with nothing

Of course you can use `SUBSTITUTE` to replace characters with nothing at all. Say, for instance, that we had a list of names but didn't want titles complicating things, we could write the following:

`=SUBSTITUTE(A2,"Mr","")`

Or:

`=SUBSTITUTE(A2,"Mrs","")`

Both of these replace the two or three characters "Mr" or "Mrs" with "" - that is, nothing.

<aside class="tip blurb">

#### What if I want to substitute a quotation mark?

Because Excel uses quotation marks to indicate the beginning and end of a string of characters, it's not easy to use quotation marks as *just another character*. For example, this formula, which tries to say 'replace a quotation mark with nothing' will generate an error: `=SUBSTITUTE(A6,""","")`

The solution is to use another function within Excel: `CHAR`. `CHAR` is used to convert codes used by computers into characters. These codes are called ASCII (American Standard Code for Information Interchange) and there are 255 numbers. For example, the letter 'A' is encoded as the number 65 by computers.

The ASCII code for quotation marks is 34. So instead of writing `"""`, you can use `CHAR(34)`. The formula in full using this would be `=SUBSTITUTE(A6,CHAR(34),"")` Note that there are no quotation marks around `CHAR(34)` because this is not a string - it's another formula. In fact, it's what's called a **nested function**, and we'll deal with them in the next chapter.

</aside>
<aside>

### Case study: generating URLs to speed up a name search

One investigation for the Mirror newspaper in the UK involved a spreadsheet containing hundreds of company names. In order to turn this into a story, we needed to identify the directors of each company, and then search to see if those individuals were connected with any newsworthy activity (for example, convicted criminals, political donors, tax evasion, subjects of frequent complaints, etc.)

The traditional method would see a person (or in this case, a team of journalism students) typing each company name into a website providing details on company directors, such as [Duedil](http://duedil.com), or [Companies House](http://www.companieshouse.gov.uk/).

A repetitive process like this is a prime candidate for some computer assistance.

Rather than type in each name manually, then, we could use the =SUBSTITUTE function to help generate a URL for each company which would take the user directly to a page of search results.

Here's what I mean:

A search for the company 'Homezone Housing Ltd' on Duedil generates the following URL:

`https://www.duedil.com/beta/search/companies?name=Homezone%20Housing%20Ltd`

A search for the company EBM Properties Ltd generates this URL:

`https://www.duedil.com/beta/search/companies?name=EBM%20PROPERTIES%20LTD`

Note that each URL is exactly the same apart for the name of the company at the end. In fact, we can express it like so:

`"https://www.duedil.com/beta/search/companies?name="` followed by company name

If we have a series of cells containing company names the formula for adding each one to that URL would look like this:

`="https://www.duedil.com/beta/search/companies?name="&A2` - where the company name is in cell A2 the first time. When copied down, obviously A2 changes to A3, A4, and so on.

But there's one other thing about those URLs: any spaces were replaced in the browser with `%20` - that's because you cannot have spaces in a web address.

To add this extra bit of formatting, we can use the `=SUBSTITUTE` function to replace every space with `%20`. This can be done in a separate column with a formula like so:

`=SUBSTITUTE(A2," ", "%20")`

In other words: grab A2, but substitute every space, with the characters `%20`.

If this formula was in B2, we would then rewrite our SUBSTITUTE formula to grab the results like so:

`="https://www.duedil.com/beta/search/companies?name="&B2`

Of course you could skip that intermediate stage of substituting, and write a formula which combined both. That would look like this:

`="https://www.duedil.com/beta/search/companies?name="&SUBSTITUTE(A2," ","%20")`

All that this does is replace `B2` with the formula we wrote in B2: `=SUBSTITUTE(A2," ","%20")`- but omits the `=` sign because that is only needed once, at the start of the formula (and we've already done that)

Note that you need to check the URL that is being generated first. For example, if you were sure that the companies were named accurately, you could skip the search results URL and jump straight to the company page URL instead. That looks like this - note that it uses dashes instead of `%20` but also that you need a company number in part of the URL too (which you would also need in your spreadsheet):

`https://www.duedil.com/company/IP28306R/homezone-housing-limited`

Google uses the `+` sign, so your SUBSTITUTE formula would look like this:

`=SUBSTITUTE(A2," ","+")`

There's also something else to consider: if your data has any extra spaces before or after the names, that will cause problems, so you may need to add the `TRIM` function, which gets rid of spaces at the start and end of cells. Again you could do this in a separate column like so:

`=TRIM(A2)`

...and then reference the cell with that formula in your next stage.

You could also combine both SUBSTITUTE and TRIM like so:

`=SUBSTITUTE(TRIM(A2)," ","+")`

The principle is, again, the same: you're just replacing the cell reference with the formula that cell contains.

You could even combine all three stages like so:

`="https://www.google.co.uk/search?q="&substitute(trim(A2)," ","+")`

</aside>

### Recap

- `TRIM` will remove extra spaces before and after data in any cell. This is useful to ensure data is consistent and can be properly matched.
- Some 'special' spaces are not affected by `TRIM`, however, so if they've still not disappeared after using `TRIM`, copy the offending space and use the **Edit \> Replace...** option to paste that space character into the 'find' box, leaving the 'replace' box empty (so it is replaced with nothing). Make sure you note how many of these are replaced in your data (it will tell you) and that it matches what you would expect.
- `SUBSTITUTE` will substitute a particular character (such as '&') or string of characters (such as 'and') with whatever you specify (including no characters). This is similar to 'find and replace' but only affects the cell specified.
- `SUBSTITUTE` takes three arguments: the cell containing the text you want to clean up; what you want to substitute (in quotation marks); and what you want to substitute it with.
- If you only want to substitute the first, or the first two or three, instances of a particular character or string of characters, you can specify this in your formula as an extra argument after those.
- If no character/s is/are found, nothing is substituted.
- Because quotation marks are used to indicate a string, if you want to substitute a quotation mark itself you need to use another function: `CHAR`. This is a way of indicating a character by its ASCII code. The formula to indicate a quotation mark, for example, is `=CHAR(34)` so using this within a `SUBSTITUTE` formula would look something like this: `=SUBSTITUTE(A6,CHAR(34),"")`
- The `TRIM` and `SUBSTITUTE` functions only work on one cell at a time, so copy them down an entire column to create a new 'trimmed' or 'cleaned' version of another.

### The last chapter's story: baby name trends

At the end of the last chapter we talked about using `VLOOKUP` to find out where one year's most popular baby names had been in the previous year's table. [The data on baby names is here](https://drive.google.com/file/d/0B5To6f5Yj1iJWkJvQWFIc1RXb0k/edit?usp=sharing) (select **File \> Download**).

- To add a new column to tell you the names' position a year ago you would put a title in cell C1 (say, '*Rank in 2013*') and then in the cell underneath the first formula `=VLOOKUP(B2,'2013namesgirls'!A:B,2,FALSE)`. For Amelia (the name in `B2` in this sheet) the result should be 6 (her position in the sheet '2013namesgirls'. Copy the formula down the whole column to repeat.
- To calculating the change between this year's position and the previous position, give your fourth column the title '*Change since 2013*'. The first calculation, in the cell underneath (D2) would be `=C2-A2` - in other words, the previous position minus the new position. For the top name, Amelia, the result is 5 - in other words, a rise of 5 from 6 to 1. For Ava in position 6, the result is -5. This is because she dropped 5 places from 1 to 6. It's a nice bit of colour to add to our story that Ava and Amelia swapped places.
- The calculation generates a number of `#N/A` errors where it cannot find a match, including the bottom six names. We can look for these in the other sheet just to check.
- The biggest riser is Jessica, which rose 29 places according to our calculation. And we can check this in our data: she was 32nd in 2013 and is now 3rd.
- But is this actually the biggest riser? Not necessarily: the two names after Jessica - Emily and Lily in 4th and 5th position respectively - don't appear in the 2013 rankings at all. These names have come from nowhere!
- How do we tackle the names which didn't appear at all in the older rankings? Because the 2013 rankings go down to 40th position we can say that the very highest position either of these two names could have occupied was 41st. So Emily, now in 4th, has risen at least 37 places (`=41-4`). Now we need to make a decision: either we gather more data to find out what positions these two names occupied the previous year (in which case we probably need to check the other non-matches too), or we phrase our reporting carefully to avoid specifics and say something like "Emily and Lily were not in the top 40 last year but have shot into the top five". It depends how important that detail is, and how much time we have.
- To repeat the process to find out the biggest falls in 2013's rankings we need to switch to that year's data. But there's a problem: in the 2014 numbers the names appear *after* the rankings. Remember that when you specify a range for `VLOOKUP` to look down the *first* cell must contain the matching data (the names). So before you write the formula you need to either *move* the rankings column in the 2014 sheet so it appears after the names, or *copy* it after the names.

Moving the column shouldn't create any problems for the formulae you've already written. They will automatically change to reflect the new position of the data. But let's say I copy the rankings column and paste it in column E of our 2014 data.

Now, **back in the 2013 sheet** I need to type the following in cell C1: `=VLOOKUP(A2,'2014girlsnames'!B:E,4,FALSE)`. This formula looks for the name in A3 on this sheet, in the other sheet '2014girlsnames' and the range `B:E` on that sheet. This is because the column B contains the names so it needs to be the first column in our range. The next part of the formula specifies that we want the *4th* column in that range, which is column E (we're counting from column B, remember). And finally `FALSE` says we don't want nearest matches but only exact ones.

Copy that formula down the column to repeat, and then create a new column to calculate the change from this year to the next. This time it is `=B2-C2`. Actually we've already done this calculation in the other sheet, where the biggest fall was Freya (down 17 places from 2nd to 19th), but there are lots more `#N/A` errors where names have dropped out of the rankings entirely (noting that the earlier table is the top 40 and the most recent is the top 30. Imogen looks particularly interesting here: 4th in 2013, she must have dropped at least 27 places in order not to feature in the top 30. Once again, you'll need to get some more comprehensive data to get the precise details.

<aside class="exercise_blurb blurb">

#### Find out the figures in your own country

Baby names are published by many national statistical organisations. Try to find your country's own statistical service (there's a [list published by Wikipedia here](http://en.wikipedia.org/wiki/List_of_national_and_international_statistical_services) and use the VLOOKUP function to compare rankings in different years.

</aside>



## Detour: generating consecutive numbers or dates

In the exercise at the end of the chapter on `VLOOKUP` we worked with some ranked data: that is, each row had a rank from 1 for first, 2 for second, and so on.

But what if those rankings weren't in the data? Could you add it without having to type into every cell?

Well this would be a pretty short chapter if the answer was 'no'. So yes, of course you can. Here's how:

In Excel and other spreadsheet software, if you type a number or text in a cell you can then copy it into other cells by clicking and dragging the black cross that appears when you hover over the bottom corner:


Before… click and drag on the bottom left corner to copy in any direction


…and after


But if you type *two consecutive numbers* and then select those together:


Select the cells containing both numbers…


When you click on the black cross and drag downwards, it assumes you want to continue the sequence:


So, instead of simply copying 1 and 2, it continues 3, 4, 5, and so on.

This is exactly how you might generate a rankings column against data which doesn't have it: you just need to type `1` and `2` in the cells next to the top two entries, select both cells, and then hover over the bottom corner until you see the black cross. Then double-click to copy it all the way down until there's an empty cell to the left.

You can also use this to generate a sequence of years: start with 1975 and 1976, and Excel will assume you want to copy those down to create 1977, 1978, 1979 and so on.

### Other number sequences

The same process works with any numerical sequence. For example, you could type the numbers `10` and `20` in your first cells, and the same process would copy the numbers Excel assumes would come next: 30, 40, 50, and so on.

Start with `2` and `4` and you'll get 6, 8, 10, 12 and every alternate number after that.

Whatever the difference between the first two numbers, it will continue with that: `3` and `7` will copy down to add 11, 15 and 19. `1` and `60` will copy down to add 119, 178, 237 - each of which is 59 numbers apart.

### Text sequences: days and months

This works with certain words too. Try typing `Monday` and `Tuesday` into the first two cells respectively.


Now, select them both and click and drag when you get the black cross in the bottom right corner. The sequence will continue on to Sunday, and then start again from Monday:


This works with months as well - whichever two you start with.

And it works with three-character versions: `Mon`, `Tue` will copy down to add Wed, Thu, Fri... while `Jan` and `Feb` will copy down to create Mar, Apr, May...

For any other text, Excel will assume you merely want to repeat the pattern you've created. So typing `First` and `Second` in your first two cells and then copying down will create series of further cells which continue to alternate `First` and `Second`.

This can still have its uses. If you know your data is in bunches - whether two, three, four, or more - you only have to type the categories once, then select them and click and drag on that black cross to repeat the categories in that order over and over again.

This obviously assumes that your data is consistently ordered in the same way, so you'd need to make some spot checks. And a better way to do this would be to use one of the `IF` functions detailed in the following chapters.

### Getting more control over your ranges - the Fill Series option

You can generate these effects more directly by using the menu option **Edit \> Fill \> Series...**


This is much less simple than clicking and dragging the black cross, but if you want unusual sequences then this might be a good place to look.

Here's how you do it with numbers:

1.  Type your first number into a cell. With that selected, go to the **Edit** menu and select **Fill \> Series...**
2.  Specify whether you want the series of numbers to appear underneath this number, in **Columns**, or to the right, in **Rows**.
3.  Specify whether you want the series to be **linear** (i.e. the numbers increase by the same amount each time) or **growth** (an exponential increase, e.g. each number multiplied). So for example, using growth with a *step value* of 5 would create a sequence from 20 to 100 (20x5) to 500 (100x5). But using linear with a step value of 5 would create a sequence from 20 to 25, 30, 35.
4.  Next specify the **Step value**. This is how much your number increases by each time. As explained above, if you specified *linear* above the number will increase by this value in each cell; if you specified *growth* the number will be multiplied by this value each time.
5.  Finally specify a **Stop value**. This is the highest number you want it to go to. It doesn't need to be exact, but just a ballpark figure of the maximum value you want in your range.
6.  Click **OK**. The cells underneath your original cell should now be filled with a sequence matching the one you described.

You can use the same process and select **Date**. If you want to use this you *must write your first date as a full date* rather than a word such as `Monday`. This is so that Excel can treat it as a number and perform calculations as such. See the chapters on data types and dealing with dates for more on how to work with dates and show them as days, months, or years.


## Using more than one function at a time: nested functions

On a couple of occasions so far I've shown examples of using more than one function at the same time. Sometimes these are combined in a calculation, such as adding one result to another, or dividing one by another.

You may remember the following formula at the end of the `SUMIF` chapter, for example, which added together the results of using `SUMIF` twice in the same formulae:

`=SUMIF(A:A,"Liverpool",C:C)+SUMIF(A:A,"Liverpool",D:D)`

Combining functions like this can often help you perform calculations more quickly than if you performed them separately.

For example, in the chapter on `MAX` and `MIN` we performed one calculation to calculate the maximum value in a range:


And then another to calculate the sum total of all values in that range:


Then a third to divide the result of one by the result of the other:


To combine these three formulae into one you simply need to replace each cell reference with the *formula inside that cell* - omitting the *equals* sign (the *equals* sign only needs to be used once at the start of the whole formula - using it more than once will be interpreted as a request to compare the two things either side of that sign).

For example, our final formula above is `=E4/E5`

We can replace `E4` with the formula in that cell, remembering to remove the *equals* sign because we're already using one (otherwise it would start with two equals signs):

`=MAX(C:C)/E5`

And we can replace `E5` with the formula in *that* cell like so:

`=MAX(C:C)/SUM(C:C)`

In other words: take the MAX of column C, and divide it by the SUM of column C.

The most common mistake when doing this is including more than one *equals* sign (or equals *operators* in the jargon of spreadsheets). Remember that you *only use the equals sign once*, at the start of the formula to indicate that you want Excel to perform a calculation and you're not entering data directly.

<aside>

#### Comparing results

As well as the more obvious options such as multiplying two values by each other, remember that you can also *compare* the results of two formulae to give a `TRUE` or `FALSE` result.

For example, using an *equals* operator within a formula (aside from the one at the start) will test if the value to the left is the same as that on the right. So `=MAX(C:C)=SUM(C:C)` will return `FALSE`.

The symbols for greater than (`>`) and less than (`<`) can be used in the same way.

You can also use `<>` to test if something is *not equal to* (think literally "less than or greater than"). This can be quite useful for testing for errors (where you know a number should not be greater than, less than, or equal to another number), or for comparing different time periods ("is this max higher than that max?")

</aside>

### Nesting functions

The examples above - using addition, division, comparison and so on - are relatively straightforward. Where things become more complex are when you want to use the result of one function *within* another function.

This is known as **nesting** functions, and they often involve parentheses *within* parentheses, for one of the ingredients, like so:

`=VLOOKUP(MAX(B:B),B:C,2,false)`

Above we have a `VLOOKUP` function which uses as its *first* argument - what it is looking for - the result of a `MAX` function.

Because `MAX` is nested within the other function, we have two pairs of parentheses, and this is where things sometimes get confusing.

The key thing to remember is this idea of 'nesting' - one thing *within* another. An alternative way to think of this is as Russian dolls: each pair of parentheses comes *within* another pair.

Excel and other spreadsheet software try to help here by adding colour coding for each parenthesis: you can tell where an opening bracket is later closed by looking for a closing bracket of the same colour. Sometimes it's not easy to tell the difference in colour - but the more parentheses you have nested within others, the more colours are used.

You might also notice that when you type each closing parenthesis, Excel highlights its matching *opening* parenthesis by making it slightly bolder. Try watching this while typing a simple formula - it comes in very useful when trying to close multiple parentheses (you can see which ones you're closing, and spot when you've closed the first one to be opened (which is the last one you close).

You might find it easiest to start from the middle and work outwards. So in the above example our *innermost* parentheses are attached to `MAX`, and that is in turn contained within the parentheses for `VLOOKUP`.

If you count the brackets in (opening), and out (closing), it makes more sense. And remember that parentheses are generally attached to a function, so once you've given all the ingredients to that function, close the bracket.

The more nesting there is, the more complex this becomes. But helpfully, if you omit a parenthesis Excel will tell you, and suggest a solution (normally to add an extra bracket where it's required).

The one function where this most often happens is `IF` - the subject of our next chapter.

<aside>

#### Example: multiple substitutions at once

In an earlier chapter we used the `SUBSTITUTE` function to correct or remove particular strings of characters. To remove more than one would require multiple columns, each working on the results of the previous one - unless you use nested functions.

In this case we use the results of *one* `SUBSTITUTE` function as the starting point for *another*. This looks like this:

`=SUBSTITUTE(SUBSTITUTE(A2,"Rt Hon",""),"Sir","")`

Again, reading from the inside out makes most sense here: we have replaced "Rt Hon" with nothing (""), and used the results of that as the basis for a function which replaces "Sir" with nothing ("").

You could also wrap the whole thing in a `TRIM` function to trim spaces from the results, like so:

`=TRIM(SUBSTITUTE(SUBSTITUTE(A2,"Rt Hon",""),"Sir",""))`

Logically, this is the same process we use in mathematical calculations. If something is in parentheses it must be calculated before the results are used. So `12 + 3 * 10` is `42` (because in maths multiplication takes place before addition), but `(12 + 3) * 10` is `150` (because the parentheses force us to perform the addition first, and then multiply the results of that)

</aside>

### Recap

- *Nesting* functions inside each other **allows you to perform multiple actions together** which might otherwise require separate cells or columns.
- When starting with nested functions **it can be helpful to first write each part in its own cell**, and then write a formula which uses those cell references. To then change this into a single nested formula, replace the cell references with the formulae within each.
- Nested functions can help you make calculations more quickly - and make you feel very clever! But pride can come before a fall: **don't create a nested function just because it's impressive**: make sure there's a good reason for doing so.
- **Sometimes it makes more sense *not* to nest a function**: for example, if you want to be able to see each stage of the calculation separately in order for you or others to be able to check those, or look for unusual results. In these cases, put each part in its own column and use cell references in those columns for the final formula.
- When nesting, you will open new parentheses before previous parentheses have been closed. This means you need to **make sure you close all parentheses at the end**. Thankfully, Excel will remind you if you haven't, and suggest a correction.
- You can **nest `SUBSTITUTE` functions within each other to perform multiple substitutions** at once, along with other cleaning functions like `TRIM`.

<aside class="exercise_blurb blurb">

### Find the story: simplifying names to make them consistent with another dataset

To explore nested functions we're going to return to some political donations data. This time, however, we're dealing with individual politicians rather than political parties.

You can [download the spreadsheet here](https://docs.google.com/file/d/0B5To6f5Yj1iJRWtkVVNTZ3lKZjg/edit). It's a much-shortened version of some results from searching the [Electoral Commission donations database](https://pefonline.electoralcommission.org.uk/search/searchintro.aspx). You can perform your own search and download the results if you want to do this with a larger dataset.

In this case we're going to use nested functions to 'clean up' the names in the list so that we can match them with a second set of data (on the second sheet of the downloadable workbook) which gives each politician's political party.

In the donations data politicians' names include titles like 'The Rt Hon', 'Sir', 'Dr', 'Mr' and so on, and also include suffixes like 'MP' and 'QC'.

However, in the second set of data each politician's name is given without these titles. For example, one set of data refers to "The Rt Hon David Cameron MP" but the other simply "David Cameron".

The `SUBSTITUTE` function could be used to do this - but we'd have to have a separate column for each title and suffix. To save space and time, then, a nested function might be useful.

1.  Download the data and make sure you're in the first sheet, which has just two columns: 'Donee' and 'Total'. Write a title for the third column, C, where you're going to clean those names - try something like 'Cleaned name' or 'Simple name'. In the second row of that column, where the first name appears, write a formula which uses two `SUBSTITUTE` functions, nested within each other, to first replace "The Rt Hon " with "", and then use the results of that as the ingredient for a further `SUBSTITUTE` function which replaces " MP" with "".
2.  Copy this formula down the whole column of names. Does it clean up all the names? Or does the function need adapting?
3.  Undo the copying of that formula (or delete the results) and edit the formula again, to nest a third `SUBSTITUTE` function, this time replacing another title or suffix.
4.  Repeat this process for any more titles or suffixes you think need substituting. Your formula will now be getting pretty long!
5.  Why might you use this technique instead of the 'Find and Replace' option? (This can be found in the Edit menu: **Edit \> Replace...**)
6.  Try nesting the whole formula within another function - `TRIM` - to get rid of any extra spaces before or after this. Why might we do this last rather than first?
7.  For a real challenge, try nesting the whole formula within a `VLOOKUP` function to look for the results in the other sheet showing each politician's party.
8.  This is really impressive. But why might nesting the cleaning formula within a `VLOOKUP` function not be the best approach?

</aside>



## Generating categories and other extra data: `IF`

Data doesn't always come with the labels you want it to have. A column of earnings doesn't generally come with a series of categories saying 'above average' or 'below average'. Likewise if you have a spreadsheet of food ratings ranging from 0 to 5 you may need to translate those into 'Satisfactory' or 'Improvement needed' if you want to add those labels to a map.

The `IF` function does this very well. It will test a value (for example: is it above or below a particular value; is it a particular string of text?) and depending on whether it does or does not meet that test, returns one of two values that you specify: one where the test is met, and a second where it is not met.

Here's a simple example. Let's say we had some data on wages in a particular sector, and we know the average wage is Â£26,500. We'd like to classify each wage based on whether it was above or below that average. Here's how we might do it for our first wage, if it was in cell B2:

`=IF(B2>26500,"Above average","Below average")`

What is that doing? Something like this:

`=IF(TEST THIS,RESULT IF TEST MET, RESULT IF TEST NOT MET)`

The formula reads quite sensibly: If B2 is above 26500 then put "Above average" (in the cell where the formula is being typed). Otherwise put "Below average".

Although the function is called `IF`, it is, strictly speaking, an "If/Else" function.

These are very common in programming. Every time you play a computer game, for example, there are probably thousands of if/else tests being made every second - for example "If the score is above 10000, add 1 to the player's number of lives, else do not" or "If the player's health is below 0, end game, else do not" or "If this pixel and that pixel are overlapping, subtract 1 from the player's lives".

If/else is best imagined as a sort of 'fork in the road' that tests something and takes a path depending on the answer. In our case above, it takes the road of classifying B2 as "above average" if it is above 26,500, or takes the road of classifying it as "below average" if that test is not met.

The classification is done by putting the specified string of characters ("Above average") in the cell where we type the formula.

We can then copy that formula down a column to repeat it for each cell in turn and give us a whole column full of one classification or the other.

Once we have that we can count how many rows are "Above average", or we can filter our data to only show those rows, and perform other calculations on that.

But you may have spotted a weakness in our if/else test...

### Testing more than one thing - nested IF

In our `IF` formula above we classified numbers above 26500 as "Above average", and anything else as "Below average". But what if one of those numbers is 26500 exactly? That's not below average, it's average.

We also have to remember that not every cell might have a number in it - our formula as it stands will classify empty cells as "Below average" and text entries could be classified as "Above average" because of the way Excel sees text characters.

To tackle that we need an *extra* `IF` function which tests those other possibilities. Here's an example:

`=IF(B2>26500,"Above average",IF(B2<26500,"Below average","Average"))`

You can see immediately that, because the IF statement has so many arguments, it's harder to 'read' than the examples shown in the nested functions chapter.

Showing the two `IF` functions on separate lines makes it slightly easier:

- `=IF(B2>26500,"Above average",`
- `IF(B2<26500,"Below average","Average"))`

And writing out the process - the 'forks in the road' - also makes it easier. So, for example, the formula above says:

- IF B2 is above 26500, return "Above average". Otherwise:
- IF B2 is below 26500, return "Below average". Otherwise:
- Return "Average".

If any test is met, the process stops *at that point*. So for example if B2 is above 26500, the formula does not need to continue to the next `IF` test.

Note the two closing parentheses at the end. The last one closes the *first* IF statement; the first closes the *second* IF statement. You can imagine how these closing parentheses pile up if you add more IF tests.

Helpfully, Excel does colour code these so you can find each bracket's twin, and if you did leave one out, Excel will come up with an error window and suggest a correction which you can accept to have it change the formula for you accordingly.

Now we still might need to add another test in case the value is zero, an empty cell, or text. We'll come onto this next.

<aside class="tip blurb">

#### Ordering your IF tests - a process of elimination

If you have more than one `IF` in your formula, it generally works best to work from the highs and lows inwards. If you have 5 ranges for example, your `IF` tests might go like this:

- Is it above 4?
- Is it below 1?
- Is it above 3?
- Is it below 2?

The pool of numbers remaining after each question gets smaller and smaller until the only numbers left would be 3s.

An alternative would be to work from the highest values down like so:

- Is it above 4?
- Is it above 3?
- Is it above 2?
- Is it above 1?

This should still work because although for a value of 5 the answer is 'Yes' to each test, the formula only goes as far as the first 'Yes'.

But because that feels less logical, you may prefer the 'circling around' approach listed above. It's really up to you.

</aside>

### Hello operators: comparing beyond 'greater than' or 'less than'

The 'greater than' and 'less than' symbols - `>` and `<` respectively - are not the only ones you can use. These are called **operators** - in fact, specifically **comparison operators** - and you can find a [full list on Microsoft's support pages](http://office.microsoft.com/en-gb/excel-help/about-calculation-operators-HP005198697.aspx).

Other operators include:

- `>=` ('Greater than or equal to')
- `<=` ('Less than or equal to')
- `<>` ('Not equal to')

And of course you can use `=` to test something specific.

You can also use more than one operator at the same time: for example, `>3<6` means 'greater than 3 and less than 6'

You don't need to use `IF` to use operators and make tests - see the next chapter for more.

<aside class="tip blurb">

If you have trouble remembering which is which, it's useful to look at the symbol itself: one side is 'greater than' (taller than) the other. Whichever value is on that side is the one you're asking 'is that greater than' the value at the narrow end.

</aside>

### Testing text: combining IF with other functions

You can use an IF statement to check for text values too - although it will only work with exact matches and you cannot use wildcards as you can with `COUNTIF`.

Such a formula would look like this - note that we need quotation marks around the text string we're testing for:

`=IF(A7="Barry","My friend","Not my friend")`

That cell would have to contain "Barry" and nothing else, including spaces, for it to return "My friend".

There are ways of making the test broader by nesting other functions, including `COUNTIF`, and many of these techniques revolve around the idea of something being **true or false**.

#### Using COUNTIF to give a true/false answer

In an earlier chapter I showed how `COUNTIF` can be used to count how many cells across a range meet a particular criteria - but also how it can be used to perform a test cell-by-cell, counting 1 or 0 depending if the cell contains the text being sought.

Now Excel doesn't just see 1 and 0 as numbers - it also sees it as an expression of the concept 'true' (1) or 'false' (0), and these numbers can be used in this way within a formula.

Here's an example of how `COUNTIF` can be used within a formula to test exactly the same thing as earlier:

`=IF(COUNTIF(A7,"Barry"),"My friend","Not my friend")`

Let's break that down:

- `IF`, as always, has three ingredients: a test; what to do if it's met; and what to do if it's not.
- The test in this case uses a `COUNTIF` function to count if A7 has "Barry" in it. The result is going to be 1 (yes) or 0 (no).
- A result of 1 will be treated as TRUE, so "My friend" will be returned.
- Otherwise, "Not my friend" will be returned.

In fact, any number above 0 will be treated as 'true'.

Now this is useful because `COUNTIF` is unique in Excel in that it allows you to use the `*` wildcard to stand for 'none or any characters' - something which the `IF` function does not allow you to do.

So we can use that functionality within a nested function like so:

`=IF(COUNTIF(A7,"*Barry*"),"My friend","Not my friend")`

Now this returns "My friend" if the characters "Barry" are *anywhere* in that cell, not just if the cell's value is *exactly* "Barry".

For some of the other tests - whether this is text or an empty cell, we need a separate chapter...

### Recap

- The `IF` function **allows you to create new data based on existing data** - for example, turning numbers into categories based on what range they fall in.
- **A single `IF` function will provide one of two results**: one if a criterion is met, and the second if it is not.
- However, **you can nest multiple `IF` functions within each other** to create more than two results: each extra `IF` function runs when a criterion is not met (or, indeed, if the criterion is met)
- When nesting `IF` functions you need to **make sure that they work logically in a process of elimination**: either eliminating from the top down, from the bottom up, or alternating between top and bottom until only the middle values are left for the final tests.
- `IF` functions use **comparison operators** such as `=` (equal to), `>` (greater than), `<` (less than), `>=` (greater than or equal to), `<=` (less than or equal to) and `<>` (not equal to)
- You can **use more than one operator at the same time**, for example asking if something is greater than one number and less than another.
- The `IF` function **can be used in conjunction with a nested `COUNTIF` function if you want to use wildcards** for your tests (these cannot be used with `IF`).
- It can also be used in conjunction with functions that give a TRUE or FALSE results, such as the `ISERROR` and similar 'is' functions, and the `AND`, `OR` and `NOT` functions, which we'll cover in following chapters.

### The last chapter's story: simplifying names to make them consistent with another dataset

At the end of the last chapter we looked at using nested functions with [some political donations data](https://docs.google.com/file/d/0B5To6f5Yj1iJRWtkVVNTZ3lKZjg/edit). Here are some answers to the questions and tasks posed:

1.  The formula to first replace "The Rt Hon " with "", and then use the results of that as the ingredient for a further `SUBSTITUTE` function which replaces " MP" with "" is as follows in row 2: `=SUBSTITUTE(SUBSTITUTE(A2,"The Rt Hon ","")," MP","")`.
2.  When copied down the whole column of names it cleans up many of the names but not all. Some names have 'Mr', 'Dr', 'Ms' and 'QC'. We need to adapt the formula.
3.  To nest a third `SUBSTITUTE` function put the existing formula in parenthesis like so: `=(SUBSTITUTE (SUBSTITUTE(A2,"The Rt Hon ","")," MP",""))` then add your new `SUBSTITUTE` function at the start: `=SUBSTITUTE (SUBSTITUTE(SUBSTITUTE(A2,"The Rt Hon ","")," MP",""))` and what it is substituting at the end, *before* the closing parenthesis: `=SUBSTITUTE (SUBSTITUTE(SUBSTITUTE(A2,"The Rt Hon ","")," MP",""),"Mr ","")`
4.  A formula which tackles all the titles and suffixes might look like this: `=SUBSTITUTE(SUBSTITUTE (SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(A12,"The Rt Hon ","")," MP",""),"Mr ","")," QC",""),"Dr ",""),"Ms ","")`
5.  You might use this technique instead of the 'Find and Replace' option for two reasons: firstly because it only applies to one column and doesn't affect any other data, but secondly: it also leaves your original column intact, so you don't lose it, and can compare the results with it.
6.  To nest the whole formula within another `TRIM` function to get rid of any extra spaces before or after simply add `TRIM(` at the start and a closing parenthesis `)` at the end like so: `=TRIM(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(A12,"The Rt Hon ","")," MP",""),"Mr ","")," QC",""),"Dr ",""),"Ms ",""))`. We would do this last rather than first because the `SUBSTITUTE` functions actually look *for* and rely on extra spaces. We also want to make sure the final results are trimmed.
7.  To nest the whole formula within a `VLOOKUP` function which looked for the result in the other sheet showing each politician's party, you might write something like this: `=VLOOKUP(SUBSTITUTE (SUBSTITUTE(SUBSTITUTE(A2,"The Rt Hon ","")," MP",""),"Mr ",""),MPs!C:D,2,FALSE)` - I've shortened the `SUBSTITUTE` element so it isn't maddening to read.
8.  Nesting the cleaning formula within a `VLOOKUP` function might not be the best approach because you want to treat cleaning and lookups as two separate columns. Having clean names in their own column will help you with the lookups that don't work - and there are quite a few of these, including those with middle names or initials. For more on how to clean these by extracting the first and last names in any cell up see the later chapters on `SEARCH`, `RIGHT` and `LEFT`

<aside class="exercise_blurb blurb">

### Find the story: converting restaurant ratings into categories

[Download the data from this link](https://drive.google.com/file/d/0B5To6f5Yj1iJeVZVSy1WV2RSam8/edit?usp=sharing). This is a sample of food hygiene inspection data on institutions in the category 'Hospitals/Childcare/Caring Premises'. In the column 'Rating value' each institution that has been inspected is given a rating from 0 to 5. A rating of 3 is considered satisfactory, but anything below that (0, 1 or 2) means that improvements are required.

We need to add a new column to this data which tells us which category each institution falls into: does it need improvement, or is it OK? We can then use this for a chart, or for descriptions if we wanted to map these.

Insert a new column to the right of the ratings, so that the new column is in column D. Call it 'Pass or fail?' This is where you'll do your work.

1.  In the first cell below that column header (D2) write a formula which uses the `IF` function to test whether the ratings value next to it (in column C) is below 3. If it is, return "Fail". If it's not below 3, however, it should return the value "Pass".
2.  Copy the formula down the entire column so it works for each cell in turn. Is the formula sound?
3.  How might you use a *nested* `IF` function to create more than two outcomes?

</aside>


## Detour: testing whether something is TRUE or FALSE

In the last chapter we touched on using the `IF` function with **comparison operators** to compare values and generate new data, such as categories. However, you don't need the `IF` function to generate two categories in particular: TRUE, and FALSE.

TRUE and FALSE are a special kind of data: **logical values**, also known as **Boolean values**.

You can generate logical values by comparing one thing with another. For example: `=5>2` returns TRUE because, yes, five is greater than two. That's true. And `=5<2` returns FALSE because five is not less than two.

Clearly this becomes more useful when you are using it with cell references. If we simply wanted to know if a food hygiene rating was lower than 3 in each cell of a column, we could use the following formula to test the value in C2:

`=C2<3`

Numbers 0, 1 and 2 (and negative numbers) would return TRUE; any others would return FALSE.

If all you want to do is sort or filter your data on a criteria that you can test logically, then a simple logical test like this may be more straightforward than using an `IF` function.

### Logical tests with text

You can also use this to test for *text* values, for example:

`=C2="Exempt"`

Remember that the equals sign at the start of this formula doesn't do anything apart from tell the spreadsheet software to perform some sort of calculation. The *second* equals operator is the one that compares two values: one before it and the other after it.

Don't forget the 'not equal to' operator here: `<>`. This can be used to return TRUE if one value is *not* equal to another.

And of course, you can use comparison operators to compare one cell with another. For example, if you had one column of original data and another of 'cleaned' data you could **check whether one cell is the same as the other** (i.e. has it been cleaned) like so:

`=A2=B2`

...which would test whether two values are the same.

Other uses for these operators include testing whether a figure has gone up or not: asking if the cell containing this year's murder rate is greater than the cell containing last year's murder rate (a formula like `=B2>A2`) essentially gives you a TRUE/FALSE response to the statement 'the murder rate has gone up'.

The `IF` function is in many ways a slightly more powerful TRUE/FALSE test - the difference is that you can specify what value it returns (instead of merely TRUE) if your logical test is true, and what it returns if it's false.

### Adding up TRUE and FALSE

TRUE and FALSE have numerical values too: TRUE is valued as 1, and FALSE as 0. So the result of this formula:

`=TRUE+TRUE`

...is 2. Likewise `=TRUE+FALSE` is 1, and `=FALSE+FALSE` is 0.

Confusingly, however, these numbers are not recognised by functions like `SUM`, `MAX` and `MIN`, and `AVERAGE` (although I cannot think why you should want to calculate an average of what are basically 'yes' and 'no' answers). Trying to use a `MEDIAN` function on a series of cells which *only* contain logical values will return the error `#NUM!`; the `AVERAGE` function will give the error `#DIV/0!` (if there are any numbers there too, the formula will only base its calculation on those numbers, ignoring the TRUE and FALSE values). `SUM,` `MAX` and `MIN` will all return `0`.

So if you want to perform calculations on more than a couple of logical values, you'll need to find a way to convert it to a number - which, funnily enough, you can do with an `IF` function like so: `=IF(E2=FALSE,0,1)`

### Functions which return logical results

In addition to simple comparison operators, there are also a number of functions which will return TRUE or FALSE results. These include `AND`, `OR`, `NOT`, and a number of functions which test for a particular type of data, such as `ISTEXT`, `ISNUMBER` and `ISERROR` - and we cover them in the following chapters.

### Recap

- **You don't need the `IF` function to generate two categories: TRUE and FALSE**.
- TRUE and FALSE are known as **logical values** or **Boolean values**
- With numbers you can generate a series of TRUE or FALSE results classifying each number as **above, or not above, a particular value, or equal to, not equal to, and so on**
- **With text values you can test if the text is equal to, or not equal to, another text value** using the equals and not equals (`<>`) operators.
- You can also use these techniques to **check whether one cell is the same as the other** - particularly useful to sort data by whether it has been changed or not, for example during cleaning.
- And you can use comparison operators to **check whether a number has gone up from one period to the next** by checking if one period's value is greater than another.
- **TRUE is valued the same as 1, and FALSE as 0**. However, numerical calculation functions such as `SUM` ignore TRUE and FALSE values entirely.



## Finding errors or missing data - and testing data types: `ISERR`, `ISBLANK`, `ISTEXT` and others

If you want to check that a formula is being used on the right sort of data - or make sure that it is only applied to a certain type of data - then Excel's `IS` functions are enormously useful.

Functions like `ISTEXT`, `ISBLANK` and `ISERR` take one argument, and will return "TRUE" or "FALSE" depending on whether it *is* indeed text, blank, an error, or whatever the function is testing for.

For example when you type the following formula and press Enter:

`=ISBLANK(A2)`

...You will get `TRUE` if A2 is blank (and `FALSE` if it's not).

You can see a full list of these functions by typing `=IS` in Excel and seeing the options that drop down as you type.


All take one argument (a cell) and this is what they do:

### Functions for testing data types

- `ISNUMBER` returns TRUE if the cell contains a number, and FALSE if it does not
- `ISBLANK` returns TRUE if the cell is blank (empty), and FALSE if it is not
- `ISTEXT` returns TRUE if the cell contains text, and FALSE if it does not
- `ISNONTEXT` returns TRUE if the cell contains something other than text (including a blank cell), and FALSE if it contains text.
- `ISLOGICAL` returns TRUE if the cell contains a TRUE or FALSE value, and FALSE if it contains anything else - for example text, a number, or nothing at all.
- `ISEVEN` and `ISODD` will test if a number is odd or even. If the cell contains something other than a number, then you will get a `#VALUE!` error.

### Functions that look for errors, or types of errors

- `ISERROR` returns TRUE if the cell contains one of a whole range of error messages, including `#N/A`, `#VALUE!`, `#REF!`, `#DIV/0!`, `#NUM!`, `#NAME?`, and `#NULL!`. It will return FALSE if the cell does not contain one of those.
- `ISERR` returns TRUE if the cell contains an error message *except #N/A*, and FALSE if it does not
- `ISNA` returns TRUE if the cell contains the **#N/A** error message, and FALSE if it does not
- `ISREF` is one of the most hard to understand error-checking functions, largely because it is so esoteric. It basically tests if the value supplied is a *valid* reference. What is confusing about the function is that it will always return true if your value is a cell reference. For example `=ISREF(A2)` will always be TRUE, because `A2` is a cell reference (it does not look at what is in A2). In contrast `=ISREF("My name")` will return FALSE, because the value is a string of text, *not* a cell reference.

In short, you are unlikely to come across an opportunity to use `ISREF` unless you're using it with the functions `INDIRECT` or `OFFSET` which allow you to generate cell references - in other words, you can use it to check if those cell references are valid.

<aside>

One function, `ISPMT`, does not test anything but rather calculates an interest payment based on 4 pieces of information. As it's not relevant to the scope of this chapter, we will not cover it here.

</aside>

### Using `IS` functions in practice: an error-checking column

In practice these functions are most useful when combined with a spreadsheet's *sort* functionality, or another function, such as `IF`.

Below, for example, is some sample data on donations. Here we've added an 'info missing' column which uses the `ISBLANK` function to look for a missing donor name.


On the third name the function (`=ISBLANK(B4)`) returns TRUE because there is no donor name - it *is blank*.

You could apply that formula down a column with thousands of entries and use the **Sort** option (normally in the **Data** menu) to sort the table on that column in order to bring all the matches to the top.

Alternatively you could generate new data which wasn't simply 'TRUE' or 'FALSE' by *nesting* `ISBLANK` (or any other of the functions detailed above) inside an `IF` function like so:

`=IF(ISBLANK(B2),"DATA MISSING!","Data present")`

The formula above translates as follows:

- IF the formula `ISBLANK(B2)` returns TRUE...
- Put "DATA MISSING!" in this cell. Otherwise...
- Put "Data present" in this cell.

### Recap

- **`IS` functions allow you to test whether a cell contains a particular *type* of data**, such as numbers, text, errors, empty cells and TRUE/FALSE values.
- **They return TRUE or FALSE** depending on whether the cell does or does not contain that type of data.
- The `ISBLANK` function is particularly useful for **looking for *missing* data in your dataset**.
- These functions **can be combined effectively with `IF` functions** to create new values - for example "No data!" or "Not graded" - based on the type of data found.

### The last chapter's story: converting restaurant ratings into categories

In the last chapter we worked on [some food hygiene inspection data](https://drive.google.com/file/d/0B5To6f5Yj1iJeVZVSy1WV2RSam8/edit?usp=sharing) to create a new column that classified the 'Rating value' in that row as 'Pass' or 'fail'. Here are the answers to the two questions:

1.  The formula in D2 which uses the `IF` function to test whether the ratings value next to it (in column C) is below 3 would look like this: `=IF(C2<3,"Fail","Pass")`. Alternatively, you might have written it like this: `=IF(C2>2,"Pass","Fail")` or even used the 'greater than or equal to' or 'less than or equal to' operators like so: `=IF(C2<=2,"Fail","Pass")` or `=IF(C2>=3,"Pass","Fail")`.
2.  When you copy the formula down the entire column so it works for each cell in turn you should notice that it misleadingly classifies 'AwaitingInspection' and 'Exempt' as either 'Pass' or 'Fail' - whichever you set as your second result. In other words, neither meet your first criteria (testing for a value which is above or below a number) because it is not a number at all.
3.  To solve this problem you might try a nested `IF` function which performs a second numerical test which applies to all remaining numbers, leaving only those text entries which should not be classified as 'pass' or 'fail'. That might look like this: `=IF(C2<3,"Fail",IF(C2>2,"Pass","NO RATING"))`. However, if you try this on the text ratings like 'Exempt' it actually comes back as 'Pass', so you need another approach.

> Another approach can use a combination of operators like so: `=IF(C6>2<6,"Pass",IF(C6<3,"Fail","NO RATING"))`. Alternatively you can test for the specific text like so: `=IF(C2<3,"Fail",IF(C2="Exempt","NO RATING","Pass"))`. A further nested `IF` function will be needed for the second non-numerical rating, 'AwaitingInspection': `=IF(C2<3,"Fail",IF(C2="Exempt","NO RATING",IF(C2="AwaitingInspection","NO RATING","Pass")))`. We can also use the techniques covered in this chapter to simplify things...

<aside class="exercise_blurb blurb">

### Find the story: classifying non-rated hygiene reports

Following on from the challenge above, try the following:

1.  Adapt one of the nested `IF` functions in the formula so that, using one of the 'IS' functions, instead of checking for a specific text value, it merely checks for *any* text.

</aside>


## Testing two things at once: `AND`, `OR` and `NOT`

Although `IF` allows you to test a cell against one criterion at a time, sometimes you want to test if a value meets *multiple criteria*. For this the functions `AND`, `OR` and `NOT` come in very handy. They work as follows:

- `AND` tests whether a value meets *all* criteria specified. Each criterion is separated by a comma, like so (you can have as many as you like): `=AND(A2>89,B2<11)`
- `OR` tests whether a value meets *any* of a series of criteria. Again, you can have as many criteria as you like, and each criterion is separated by a comma, like so: `=OR(A2>89,B2<11)`
- `NOT` tests that a value *does not* meet the criterion specified. With this function you can only specify *one* criterion, like so: `=NOT(A2>89)`

The result of all three functions will always be TRUE (yes it does) or FALSE (no it doesn't).

This means that these functions, like the 'IS' functions earlier, work particularly well with the `IF` function (see below).

But they can also be used to sort or filter your data accordingly.

### Finding outliers at the top or bottom: OR

With numerical data, these functions play an important role where you're looking for values in a particular range. If you wanted to check whether a cell was in the top 10% (90-100) *or* the bottom 10% (0-10) you might use the following formula which employs `OR`:

`=OR(A2>89,A2<11)`

### Finding one of a series of possible text values: OR

The same function can be used to check for a number of text values. For example, you could use `OR` to check if a cell containing the day a particular crime was committed contains a weekend day:

`=OR(A2="Saturday",A2="Sunday")`

Or that a month is a summer month:

`=OR(A2="June",A2="July",A2="August")`

### Finding numbers in the middle, or in a particular range: AND

For number values that lie in the middle, the `AND` function is more useful. If we wanted to ask 'Does this value lie between 11 and 89?' we could use `AND` to do that like so:

`=AND(A2>10,A2<90)`

### Applying criteria across multiple columns

`AND` is particularly powerful when applied across more than one column. For example, if we had results for different exams in different columns, we might use `AND` to find rows where someone had done particularly well in one exam, but surprisingly badly in another:

`=AND(A2>90,B2<10)`

We might also use it with text data in the same way to find rows where two columns had particular values:

`=AND(A2="Sunday",B2="August")`

### Combining with `IF` to avoid multiple `IF` tests

In earlier chapters we looked at nested functions, and how to use multiple nested `IF` functions to test multiple criteria and create new data in response.

In some cases, however, using `AND`, `NOT` or `OR` can avoid the need for nested `IF` statements - for example, where you are using more than one `IF` statement to generate the same result.

For example, in our food ratings data, text entries like 'Exempt' were being classed as 'above 3' and therefore a 'pass'. But we can tackle this by using `AND` in the formula to check that the number is also below 6 as follows:

`=IF(AND(C6>2,C6<6),"Pass",IF(C6<3,"Fail","NO RATING"))`

This formula first tests if the value is greater than 2 AND less than 6 - if so it returns "Pass" - then tests if the value is less than 3 - and returns "Fail" if so - and then for anything which doesn't meet either criteria, returns "NO RATING".

Alternatively you might add a test to see if the cell contains a number using `ISNUMBER`.

Clearly we don't need to use this if we could do the same with only a combination of operators - but if we wanted to test criteria across multiple cells in the same row, for example, we will definitely need `AND` or `OR`.

### Making multiple negative tests

Although `NOT` can only test something does not meet *one* criterion, you can combine it with `AND` or `OR` to test it does not meet multiple criteria. Sounds counter-intuitive? Here's an example of what I mean:

`=AND(NOT(A2<90),NOT(B2<90))`

This formula basically asks a series of questions and if the answer to them all is 'yes' (TRUE) then the formula will return 'yes' - TRUE - too. Although the questions are negative ("is this *not* something"), the answers are still positive ("*Yes*, it *is* not something. That is true.")

To illustrate this further, here are the results of the `NOT` functions in the above formula. There are four possible outcomes:

1.  Both `NOT`s return FALSE (A2 and B2 are both less than 90)
2.  The first `NOT` returns TRUE (A2 is *not* less than 90), the second `NOT` returns FALSE (B2 *is* less than 90)
3.  The first `NOT` returns FALSE (A2 *is* less than 90), the second `NOT` returns TRUE (B2 is *not* less than 90)
4.  Both `NOT`s return TRUE (both A2 and B2 are *not* less than 90)

Remember that `AND` looks to test if *all* criteria within its parentheses are met - that is, if all criteria are themselves TRUE. So of the four possible outcomes (FALSE/FALSE, TRUE/FALSE, FALSE/TRUE and TRUE/TRUE) only the last one will meet the criteria. If this is the case, the full `AND` function will return TRUE. For the other three outcomes it will return FALSE.

Compare this to using the same formula but with `OR` rather than `AND`:

`=OR(NOT(A2<90),NOT(B2<90))`

In this case, *any* criteria needs to be met to get a TRUE result. So while the first outcome (FALSE/FALSE) does not meet any, all the other three outcomes meet at least one criteria (have at least one TRUE result) and so the `OR` function would return TRUE for any of those combinations.

In the exercise we'll be looking at using these functions to bring out possibly newsworthy rows in a dataset.

### Recap

- The functions `AND` and `OR` allow you to **test if a value meets a number of criteria**.
- **Each criterion is separated by a comma** (or semicolon in some languages).
- The `NOT` function allows you to **test if a value *does not meet* one criterion**.
- **The result will always be logical**: TRUE or FALSE.
- This means it can be **combined with the `IF` function** to avoid having to nest more and more `IF` tests
- You can use these functions to **test cells in multiple columns at once** - identifying rows with a particular combination of characteristics.

### The last chapter's story: classifying non-rated hygiene reports

At the end of the last chapter I asked how you could use one of the 'IS' functions inside an `IF` function so that, instead of checking for a specific text value, it merely checks for *any* text.

1.  For that you'll need to test if it's text using `ISTEXT` - and the formula would look like this: `=IF(C2<3,"Fail",IF(ISTEXT(C2),"NO RATING","Pass"))`

<aside class="exercise_blurb blurb">

### Find the story: which outlets have consistently bad scores?

[At this link you can find a more extensive dataset on food hygiene ratings](https://drive.google.com/file/d/0B5To6f5Yj1iJeUM2VFZkaUc3MDQ/edit?usp=sharing). This time we not only have an overall 'RatingValue' from 0 to 5 (with some 'Exempt' or 'AwaitingInspection'), but we have three other scores, which the final rating is based on. These are:

1.  Scores - Hygiene
2.  Scores - Structural
3.  Scores - ConfidenceInManagement

It's always wise to explore the data a little and try to understand it. In this case, for example, a high score is *not* good. We can tell because businesses which get a 5 rating overall seem to have scores of 0 and 5 for these individual criteria.

Conversely, the first business which gets a rating of 1 overall has individual marks of 10, 20 and 20 respectively for hygiene, 'structural' and 'confidence in management'.

Some searching for those terms and the organisation responsible (in this case the Food Standards Agency) will normally turn up some explanations. And here it does confirm that, firstly, the scales are different (from 0 to 25) and, secondly, higher scores mean worse performance.

Knowing this, we can perhaps drill down into our data a little more by using the functions covered in this chapter.

1.  Create a new column headed 'ALL BAD?' at the end of the data - in column N - and use `AND` to identify which outlets scored poorly - say, 10 or above - across all three criteria in columns K, L and M. Remember a poor score is actually a high score here.
2.  Change the formula so it returns TRUE if *any* rating is 15 or above, not necessarily all.
3.  Use `AND` to see which outlets have a bad overall rating *and* were inspected more than a year ago. This is a little trick - you need to remember that dates are stored as numbers by Excel so the question is: how do you express the date one year ago as a number? Check the chapter on data types and dates if you need a refresher.

</aside>


