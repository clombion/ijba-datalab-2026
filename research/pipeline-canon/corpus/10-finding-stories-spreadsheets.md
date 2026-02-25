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
