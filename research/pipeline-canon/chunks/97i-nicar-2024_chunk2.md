<!-- chunk: 2/2 | source: 97i-nicar-2024.md | words: 26002 -->
<!-- headings: Splitting Socrata addresses; The goal in a nutshell; Capturing the address; Capturing the city; Capturing the state; Capturing latitude; Capturing longitude; The substitution string; Limitations of regex101; Search and replace in the text editor; More Regex; It might be easier to show than explain; bit.ly/nicar-regex; Don't fear the regex; Special characters, commands and escape; Regex101.com; Our goal: Splitting addresses; Get the data into regex101; Capturing the address; New lines differe between Mac and PCs -->

## Splitting Socrata addresses


Many government agencies use [Socrata](https://opendata.socrata.com/) [as their open data portal: From Austin](https://data.austintexas.gov/) to [Boston; from](https://data.cityofboston.gov/)
[Los Angeles to](https://data.lacity.org/browse) [New York.](https://nycopendata.socrata.com/)


Some of the data sets in Austin have all the address parts crammed into a single field. Regex
can easily explode that into individual columns.


So, our goal is to turn this:


into this:

### The goal in a nutshell


We are building a pattern in our regular expression field, creating a group to capture each part
of the address that we want to keep. We'll continue the pattern outside the group until we get to
the next part we want to keep, when we'll create a new group, and so on.


[You'll want to reference your Regex Cheat Sheet](https://drive.google.com/file/d/0B8ConnGcXrv8MzE3SWtwU2NxQk0/view?usp=sharing) [(or this alternative).](https://drive.google.com/open?id=0B8ConnGcXrv8bnJwdEtWVGx4N0E)


Let's get started:

  - [View the file socrata_addresses.txt](https://raw.githubusercontent.com/utdata/regex-lesson/master/socrata_addresses.txt) and copy and paste the contents into the "TEST
STRING" of [regex101.com.](https://regex101.com/)

  - [Note this is just one column from a larger Socrata data set of restaurant inspection](https://data.austintexas.gov/Health-and-Community-Services/Food-Establishment-Inspection-Scores/ecmv-9xxi/about_data)
[scores in Austin, TX. (When I want to clean a single column of data, I often download the](https://data.austintexas.gov/Health-and-Community-Services/Food-Establishment-Inspection-Scores/ecmv-9xxi/about_data)
data and will just copy out one column into my text editor and work it before pasting back
the results into Excel, carefully making sure they still line up.)

  - Let's look at our data a little closer. This is really rows of data, even though there are six
lines of text here:


    - Notice the address, city, state, zip, latitude and longitude are all in the same "cell"
(what is inside the quote marks), but the content of the cell has returns in it. We
want to split these six distinct pieces into their own columns for each record.
Why? Many reasons, but one is to use the latitude and longitude for data
visualizations.


    - We will build a Regular Expression pattern to search and capture six groups of
text and then replace those groups with tabs between them so we can put them
back into Excel as columns.

  - In regex101, in the right-hand box of the REGULAR EXPRESSION string, make sure
there is a green **/gm** listed. If not, click on the / and choose the first two options “global”
and “multiline” [1]

### Capturing the address


  - We know that the first line starts at the beginning of the line, so we can start with this
token, which signifies that: `^`

  - Now, in the end, we don't want to keep the double-quote, so we won't put it inside a
group. We'll just add it to the pattern: `^` **`"`** .

  - Take note for a minute at the number of matches at the top right: There are 325
matches, and that is how many records we should end up with. You'll want to keep
referring back to that and making sure you have 325 groups.


  - Next, we'll start our first capture group with parenthesis: `^"` **`()`** . You'll see as you type in
the first parentheses, regex101 _might_ also put in the second and then put your cursor in
the middle of them. This is "code completion", and good code editors do this to help you
be more efficient. (If not, no big deal … just add it.)

  - Inside the parenthesis (our first group), we want to capture the whole address, which is
everything until the end of the line. The period token `.` means "any character", and `*`
means "zero or more", so put these together and we get everything: `^"(` **`.*`** `)` .


Let's take a minute to explain more about Regex101 and how it helps you.


On the modifier "gm": The "g" is for "global", as in find all occurrences, not just the first one.
The "m" is for "multi-line", which allows us to evaluate each line separately. I almost always use
"gm" when doing search and replace like this.


Each matching group gets a color, and the contents of the match is shown in MATCH
INFORMATION. The EXPLANATION section tells you exactly how each token is used, and the
QUICK REFERENCE section is a list of tokens you can use, more in depth than the cheat sheet
I've started you with.


OK .. on with it.


  - Before we can start capturing the second group with the city, we need to add the return
to the pattern so it can start recognizing the next line. But here's the drive-you-crazy
thing: Windows and Macs treat these differently. On a Mac, `\n` is a "new line". If you are
on a Windows machine, you'll need to use `\R` . The regex101 editor will recognize either,
but later when we do the search and replace in your code editor, you have to use the
character that works with your operating system. This tutorial will use Macs, so:
`^"(.*)` **`\n`** .

  - (If we end up with PC's in this lab, you'll need to use `\R` every time you see `\n` in this
tutorial.)

  - Sanity check: This what your screen should look like:


### Capturing the city


  - Now, let's grab the city. As we look through the list, we can see there is more than
Austin, and some of these names have spaces so we can't find just letters alone. There

  - Then we'll add the quantifier `+` to find "one or more" of what's in the character set:
`^"(.*)\n(\w` **`+`** `)` .

  - Make sure we are capturing all 325 groups. We should be good.

### Capturing the state


  - These are all the same, all in TX, so we don't really have to save it at all, but we will.
We'll use this to remind ourselves that you can also just match a string literally. First we
put the comma and space outside the second group, since we don't want to keep it:
`^"(.*)\n(\w+)` **`,`** .


Catching errors


  - Now, take a moment and check how many matching groups we have. Wait ... WHOA ...
we have only 314. What could've gone wrong?

  - Scroll down the Test string until you find something amiss. The colors help you spot
problems easily.


  - What is the difference between the working lines and the ones that aren't? Something
about the city.

  - BEE CAVE and WEST LAKE HILLS have spaces while AUSTIN and PFLUGERVILLE
do not. It looks like our city group did not capture a needed space, which wasn't really
revealed until we tried to carry out the pattern with the `,` that is found after the city. This
happens, a lot … we need to back up and fix the error.

  - Right now, our expression is this: `^"(.*)\n(\w+),` and the part that captures the city
is `(\w+)` . We need to use something called a "character set" that allows us to include
more than one token within a group. We signify this by putting what we want inside of
square brackets: So we need to put the `\w` inside square brackets along with the space
so we can catch both: `^"(.*)\n(` **`[\w`** **`]`** `+),` .


Back to the state


  - Then we create our third group with TX inside it: `^"(.*)\n([\w` `]+),` **`(TX)`** . We are
looking for the literal text TX because there are no other states in this data set. We can't
skip it because we need the pattern to continue.


Sanity check. Here is what you should have:


  - Again, we don't want to keep the space between the state and ZIP, so we'll put it outside
the third group, and start our fourth one for ZIP: `^"(.*)\n([\w` `]+),` `(TX)` **`()`** .

  - All of these zip codes are of the 5-digit variety, so this can be less complicated than it

`(\d*)` **`\n`** .


Sanity check: This is where we are …


### Capturing latitude


  - We don't want to keep the parenthesis that starts this last line, so we'll put it outside a
group. However, since parenthesis mean something special in regex, we need to escape
it with a backslash so it will find the character and not start the new group:
`^"(.*)\n([\w` `]+),` `(TX)` `(\d*)\n` **`\(`** . Code completion might make this tricky,
but you can do it!

  - Now we can start our new group, so go ahead and add the beginning and end
parentheses: `^"(.*)\n([\w` `]+),` `(TX)` `(\d*)\n\(` **`()`** .

  - Inside our fifth group, we need numbers and the decimal point. We will create a
character set using square brackets and put inside it `\d` for numbers and `\.` for the
decimal point, which we have to escape since . means "any character". We finish it off by

### Capturing longitude


  - We don't need the comma and space in our next group, so we put it outside to keep the
pattern going: `^"(.*)\n([\w` `]+),` `(TX)` `(\d*)\n\(([\d\.]+)` **`,`** .

  - We can get the longitude like we did latitude, but we have to add the hyphen to the
character set. So, create the group:

  - `^"(.*)\n([\w` `]+),` `(TX)` `(\d*)\n\(([\d\.]+),` **`()`** .

  - Add the character set:

  - Add our quantifier to get one or more:

  - `^"(.*)\n([\w` `]+),` `(TX)` `(\d*)\n\(([\d\.]+),` `([\d\-\.]` **`+`** `)` .

  - Because the trailing parentheses and quote are at the end of a line, we could ignore
them, but we won't. We'll add them to the end of the pattern, escaping the close
parentheses just to be sure:

  - `^"(.*)\n([\w` `]+),` `(TX)` `(\d*)\n\(([\d\.]+),` `([\d\-\.]+)` **`\)"`** .


You have it all! 325 matches into 6 different groups.

### The substitution string


Now that we have a pattern with our six groups of data, we can substitute them in any order we
want using a search and replace, and we can build our substitution string right here in
Regex101 as well.


In the left-hand navigation under the FUNCTION heading, click on the item called **Substitution** .
That should expand the SUBSTITUTION window.


Now we can build a substitution string, and we can see the cleaned data in the window below.


Our goal with the substitution string is to pull back our six groups, but to put tabs in between
each of them. If we can build a search and replace like this, then we can paste the result back
into Excel, and each group will become its own column.


A quick refresher from our intro: Once we've built a group, we can reference it in our substitution
string by order in which we captured it. So, if we want to reference our first group, we use this:
**`$1`** . Put that in the SUBSTITUTION string box, like this:


example.

  - Now we can add our next ordered group to our substitution string and see our city get
added on: `$1\t` **`$2`** .


Here is a sanity check:


  - Now that you see how it works, let's go ahead and add the rest of the groups, all with
tabs in between them: `$1\t$2` **`\t$3\t$4\t$5\t$6`** . Your screen might look a little
different than below if the lines start wrapping.


Now, you might try copy 'n' pasting this result into Excel or Google Sheets and it will become six
distinct columns.

### Limitations of regex101


This can work fine for a small data set, but things bog down on the site if you have many rows
or columns of data. I often use regex101 with sample text to figure out my patterns, but then use
them in a text editor or within a R or Python script. You can see how to use regex in
Find/Replace for various text editors below.


You can actually save this example in regex101 under SAVE & SHARE in the top left panel. If
you create a login with regex101 you can keep a dashboard of them.


My example is saved here: [https://regex101.com/r/dVFG6T/2/](https://regex101.com/r/dVFG6T/2/)


## Search and replace in the text editor


We are almost done. Go ahead and launch your text editor if you haven't already. I’ll show this
first in Visual Studio Code.


  - Take your TEST STRING data (not the expression, but the data) and paste it into a new
next file in your text editor. (Or grab it from the file you downloaded.)

  - Go under the **Edit** menu to **Replace** (or do control-H for PC, command-option-F for Mac)
to bring up the search window.

  - Copy the Regular Expression pattern you built in Regex101 and insert into the **Find** text
field in VS Code.

  - Copy the Substitution pattern and insert it into the **Replace** field.

  - Click on the button on the far-right of the Find line, the one that has `.*` in it.


Here is what the search and replace screen looks like in VS Code:


  - Now, hit the "Replace All" button to the far-right of the Replace field and watch the magic
happen.

  - Once you run the search and replace, you can copy and paste the results into a
spreadsheet and it will be six distinct columns. (If it doesn't, hollar.)



## More Regex


There are lots of sites and tutorials on regular expressions, but
[http://www.regular-expressions.info/ is one of my favorites.](http://www.regular-expressions.info/)


And remember, if you are stumped by something, chances are you are not the first. Google and
Stack Overflow are your friends. ChatGPT might be helpful, too, if you are good at prompts.


## It might be easier to show than explain

# bit.ly/nicar-regex



## Don't fear the regex

A regular expression (regex or regexp for short) is a special text string for describing a search pattern. Searching text with a pattern instead for a specific string of characters can be VERY useful for cleaning data. The concept is available in many programming languages and tools.

This lesson explains what regular expressions are, how they can be useful in your everyday life as a journalist, and reveals ONE SIMPLE CONCEPT that can change your life.

While we'll use [regex101.com](https://regex101.com/) to learn the syntax, that site can handle only so much data. In practice, I tend to use regex101 to test my patterns on sample data, but then execute them in a spreadsheet formula, code editor or in a programming language like R or Python.

Links you will need in a browser:

- [regex101.com](https://regex101.com/)
- [bit.ly/nicar-regex-sample](https://raw.githubusercontent.com/utdata/regex-lesson/main/socrata_addresses.txt)
- [bit.ly/nicar-regex-cheats](https://docs.google.com/document/d/0B8ConnGcXrv8MzE3SWtwU2NxQk0/edit?resourcekey=0-DhAumbANwf8d0AGz9dpWhQ)

NOTE: When you use the bit.ly links above you may get an advertising page before you get to the target page. You can just click **Continue to destination** to get past it.

Key concept: patterns
Let's say you have a list of phone numbers in 10-digit format -- `512-555-1212` -- but you want the area code to be in parenthesis: `(512) 555-1212`. You could do a simple search of the 512 area code followed by a dash `512-` and replace it with an area code in parenthesis and a space: `(512) `.

But what if there are different area codes in the list?

```
512-555-1211
301-333-1212
404-123-1213
```

With regular expressions, you can search for a pattern of characters. Instead of searching just for `512-`, you can look for "three numbers together at the beginning of a line that are then followed by a dash".

If you capture that matching pattern as a group, you can then replace that group with parenthesis outside it, no matter what the contents of the group. If that saved group is called `$1` then you can replace it with `($1)`  and it doesn't matter if `$1` is equal to `512-` or `301-`.


## Special characters, commands and escape

Let's touch quickly on the syntax of regular expressions. Don't get hung up if these sound like gibberish, because it will make more sense when we start using it. Your [Regex Cheat Sheet](https://drive.google.com/file/d/0B8ConnGcXrv8MzE3SWtwU2NxQk0/view?usp=sharing) (or [this alternative](https://drive.google.com/open?id=0B8ConnGcXrv8bnJwdEtWVGx4N0E)) comes in handy here.

Regular expressions use special characters to do special things, like match the beginning of a line. These commands are called tokens:

- `^` will find the beginning of a line.
- `+` will find "one or more" of whatever precedes it.

Regular expressions use the backslash (the one above return on the keyboard: `\`) with other characters to create more tokens to do special things:

- `\d` will find any number character (or digit).
- `\D` will match anything other than a number.
- `\t` is a tab character, because hitting the tab on the keyboard will perform the action instead of giving you the character.

But then sometimes, you actually need to find the character ^, and not use it as a command. Regular expressions use the \ to give the literal expression of a character that would otherwise be a token:

- `\*` will find the asterisk character instead of modifying the query to find "zero or more".

Enough of that. Let's do this, with the help of ...

### Regex101.com

[Regex101](https://regex101.com/) is a great way to not only build regex patterns, but to also learn how they work. Go ahead and launch that site in a browser so we can work with it here in a minute.

We're going to use this tool to split complicated address data into individual parts. Let's talk about the data first.



## Our goal: Splitting addresses

We will start with a single "column" of data that has been copied from a spreadsheet. It is the address column from a dataset on [Austin's public data portal](https://data.austintexas.gov/). The platform is common across many cities and government agencies.

In this data, all the address "parts" are crammed into a single field. Regex can easily explode that into individual columns.

So, our goal is to turn this:


into this:


We will build a pattern in our regular expression field, creating a group to capture each part of the address that we want to keep. We'll continue the pattern outside the group until we get to the next part we want to keep, when we'll create a new group, and so on.

You'll want to reference your [Regex Cheat Sheet](https://drive.google.com/file/d/0B8ConnGcXrv8MzE3SWtwU2NxQk0/view?usp=sharing) (or [this alternative](https://drive.google.com/open?id=0B8ConnGcXrv8bnJwdEtWVGx4N0E).



## Get the data into regex101

Let's get started:

1. Open this link [socrata_addresses_long.txt](https://raw.githubusercontent.com/utdata/regex-lesson/refs/heads/main/data/socrata_addresses_long.txt) in a new window of your browser. Copy the contents of that screen.
    - Some browsers might download the files instead of viewing. If so, go to  [this page](https://github.com/utdata/regex-lesson/blob/main/data/socrata_addresses_long.txt) and use the copy button in the tools there to get the content.
1. If not there already, go to [regex101.com](https://regex101.com/) and then paste that text into the "TEST STRING" field.

    Note this is just one column from a larger Socrata data set of restaurant inspection scores in Austin, TX. (Sometimes when I want to clean a single column of data, I’ll just copy out one column into my text editor and work it before pasting back the results into Excel, carefully making sure they still line up.)
    
    Let's look at our data a little closer. This is really two rows of data, even though there are six lines of text here:
    
    
    Notice the address, city, state, zip, latitude and longitude are all in the same "cell" (what is inside the quote marks), but the content of the cell has returns in it. We want to split these six distinct pieces into their own columns for each record. Why? Many reasons, but one is to use the latitude and longitude for data visualizations.
    
    We will build a Regular Expression pattern to search and capture six groups of text and then replace those groups with tabs between them so we can put them back into Excel as columns.

1. In regex101, in the right-hand box of the REGULAR EXPRESSION string, make sure there is a green **/gm** listed. If not, click on the **/** and choose the first two options "global" and "multiline". [^1]

[^1]: On the modifier "gm": The "g" is for "global", as in find all occurrences, not just the first one. The "m" is for "multi-line", which allows us to evaluate each line separately. I almost always use "gm" when doing search and replace like this.



## Capturing the address

For the next while, we'll be building our expression in the REGULAR EXPRESSION field in regex101. So when I say add or edit the expression, that's where we are doing it.

1. We know that the first line starts at the beginning of the line, so we can start with this token, which signifies that: `^`
1. Now, in the end, we don't want to keep the double-quote, so we won't put it inside a group. We'll just add it to the pattern: `^"`

    This is what it looks like: 


    Take note of the number of matches at the top right: There are 325 matches, and that is how many records we should end up with. You'll want to keep referring back to that and making sure you have 325 groups.

1. Next, we'll start our first capture group by adding parenthesis: `^"()`. You'll see as you type in the first parentheses, regex101 _might_ also put in the second and then put your cursor in the middle of them. This is "code completion", and good code editors do this to help you be more efficient. (If not, no big deal … just add it. It's a setting you can adjust later.)
1. Inside the parenthesis (our first group), we want to capture the whole address, which is everything until the end of the line. The period token `.` means "any character", and `*` means "zero or more", so put these together and we get everything: `^"(.*)`.

    Let's take a minute to explain more about Regex101 and how it helps you.
    
    
    Each matching group gets a color, and the contents of the match is shown in MATCH INFORMATION. The EXPLANATION section tells you exactly how each token is used, and the 	QUICK REFERENCE section is a list of tokens you can use, more in depth than the cheat sheet I've started you with.

    OK .. on with it.

1. Before we can start capturing the second group with the city, we need to add a return to the pattern (we'll use the token `\n`) so it can start recognizing the next line. So add that at the end: `^"(.*)\n`.

::: callout-warning

### New lines differe between Mac and PCs

Windows and MacOS sometimes treat new line tokens differently. On a Mac, `\n` is a "new line", but Windows uses `\R`. The regex101 editor will recognize either, and Visual Studio Code also seems to handle either, but if you are on Windows and have trouble, you might need to use `\R` instead of `\n` in some cases.


**Sanity check:** This what your screen should look like:



## Capturing the city

Now, let's grab the city. As we look through the list, we can see there is more than Austin, and some of these names have spaces so we can't find just letters alone.

1. There are MANY ways to do this, but we'll do it here by creating a group first:  `^"(.*)\n()`.
1. Then inside the group we'll put a token that looks for word characters:  `^"(.*)\n(\w)`.
1. Then we'll add the quantifier + to find "one or more" of what's in the character set: `^"(.*)\n(\w+)`.

Make sure we are capturing all 325 groups. We should be good.



## Capturing the state

These are all the same in this data, all in TX, so we don't really have to save it at all, but we will. We'll use this to remind ourselves that you can also just match a string literally.

1. First we put the comma and space outside the second group, since we don't want to keep it: `^"(.*)\n(\w+), `.

### Catching errors

Now, take a moment and check how many matching groups we have. Wait ... WHOA ... we have only 314. What could've gone wrong?

1. Scroll down the Test string until you find something amiss. The colors help you spot problems easily.


What is the difference between the working lines and the ones that aren't? Something about the city.

BEE CAVE and WEST LAKE HILLS have spaces while AUSTIN and PFLUGERVILLE do not. It looks like our city group did not capture a needed space, which wasn't really revealed until we tried to carry out the pattern with the ,  that is found after the city. This happens a lot  … we need to back up and fix the error.

Right now, our expression is this: `^"(.*)\n(\w+), ` and the part that captures the city is `(\w+)`. We need to use something called a "character set"  that allows us to include more than one token within a group. We signify this by putting what we want inside of square brackets: So we need to put the `\w` inside square brackets along with the space so we can catch both: `^"(.*)\n([\w ]+), `.

### Back to the state

1. Then we create our third group with TX inside it:  `^"(.*)\n([\w ]+), (TX)`. We are looking for the literal text TX because there are no other states in this data set. We can't skip it because we need the pattern to continue.

**Sanity check.** Here is what you should have:



## Capturing the ZIP

1. Again, we don't want to keep the space between the state and ZIP, so we'll put it outside the third group, and start our fourth one for ZIP: `^"(.*)\n([\w ]+), (TX) ()`.
1. All of these zip codes are of the 5-digit variety, so this can be less complicated than it might be with 9-digit ZIPs. Again, there are many ways to do this, but we'll use `\d` for the numbers and `*` to capture zero or more of them: `^"(.*)\n([\w ]+), (TX) (\d*)`.
1. Complete the pattern for this line with the new line token: `^"(.*)\n([\w ]+), (TX) (\d*)\n`.

**Sanity check.** This is where we are:




## Capturing latitude

1. We don't want to keep the parenthesis that starts this last line, so we'll put it outside a group. However, since parenthesis mean something special in regex, we need to escape it with a backslash so it will find the character and not start the new group: `^"(.*)\n([\w ]+), (TX) (\d*)\n\(`. Code completion might make this tricky, but you can do it!
- Now we can start our new group, so go ahead and add the beginning and end parentheses: `^"(.*)\n([\w ]+), (TX) (\d*)\n\(()`.
- Inside our fifth group, we need numbers and the decimal point. We will create a character set using square brackets and put inside it `\d` for numbers and `\.` for the decimal point, which we have to escape since . means "any character". We finish it off by using + to look for one or more of the characters in the set. Like this:
`^"(.*)\n([\w ]+), (TX) (\d*)\n\(([\d\.]+)`.


## Capturing longitude

- We don't need the comma and space in our next group, so we put it outside to keep the pattern going: `^"(.*)\n([\w ]+), (TX) (\d*)\n\(([\d\.]+), `.
- We can get the longitude like we did latitude, but we have to add the hyphen to the character set. So, create the group:
`^"(.*)\n([\w ]+), (TX) (\d*)\n\(([\d\.]+), ()`.
- Add the character set:
`^"(.*)\n([\w ]+), (TX) (\d*)\n\(([\d\.]+), ([])`.
- And inside of it, put `\d` for digits, `\-` for the hyphen and `\.` for the decimal point:
`^"(.*)\n([\w ]+), (TX) (\d*)\n\(([\d\.]+), ([\d\-\.])`.
Add our quantifier to get one or more:
`^"(.*)\n([\w ]+), (TX) (\d*)\n\(([\d\.]+), ([\d\-\.]+)`.
Because the trailing parentheses and quote are at the end of a line, we could ignore them, but we won't. We'll add them to the end of the pattern, escaping the close parentheses just to be sure:
`^"(.*)\n([\w ]+), (TX) (\d*)\n\(([\d\.]+), ([\d\-\.]+)\)"`.


You have it all! 325 matches into 6 different groups.



## The substitution string

Now that we have a pattern with our six groups of data, we can substitute them in any order we want using a search and replace, and we can build our substitution string right here in Regex101 as well.

In the left-hand navigation under the FUNCTION heading, click on the item called Substitution. That should expand the SUBSTITUTION window.


Now we can build a substitution string, and we can see the cleaned data in the window below.

Our goal with the substitution string is to pull back our six groups, but to put tabs in between each of them. If we can build a search and replace like this, then we can paste the result back into Excel, and each group will become its own column.

A quick refresher from our intro: Once we've built a group, we can reference it in our substitution string by order in which we captured it. So, if we want to reference our first group, we use this: `$1`.

1. Put that in the SUBSTITUTION string box, like this:


    You can see that Regex101 is now pulling back our address.

    We can't just type a tab key after our group because they keyboard command will move us to another box, so we use the token for tab, which is `\t`.
    
1. So, add that to the end of our substitution string to get this: `$1\t`. You'll see space get added into our substitution example.
1. Now we can add our next ordered group to our substitution string and see our city get added on`: $1\t$2`.

    Here is a **sanity check**:
    


1. Now that you see how it works, let's go ahead and add the rest of the groups, all with tabs in between them: `$1\t$2\t$3\t$4\t$5\t$6`. Your screen might look a little different than below if the lines start wrapping.


Now, you might try copy 'n' pasting this result into Excel or Google Sheets and it will become six distinct columns.


## Limitations of regex101

This can work fine for a small data set, but things bog down on the site if you have many rows or columns of data. I often use regex101 with sample text to figure out my patterns, but then use them in a text editor or within a R or Python script. You can see how to use regex in Find/Replace for various text editors below.

You can actually save this example in regex101 under SAVE & SHARE in the top left panel. If you create a login with regex101 you can keep a dashboard of them.

My example is saved here: <https://regex101.com/r/dVFG6T/2/>

> Reporting with Data students can stop here and save your regex101 link and submit it in Canvas. I’ll demo the rest in class.



## Using a code editor

We are almost done. Go ahead and launch your text editor if you haven't already. I’ll show this in Visual Studio Code.

1. Take your TEST STRING data (not the expression, but the data) and paste it into a new next file in your text editor. (Or grab it from the file you downloaded.)
1. Go under the *Edit* menu to *Replace* (or do control-H for PC, command-option-F for Mac) to bring up the search window.
1. Copy the Regular Expression pattern you built in Regex101 and insert into the *Find* text field in VS Code.
1. Copy the Substitution pattern and insert it into the *Replace* field.
1. Click on the button on the far-right of the Find line, the one that has `.*` in it.


    Here is what the search and replace screen looks like in VS Code:
    

1. Now, hit the "Replace All" button to the far-right of the Replace field and watch the magic happen.

Once you run the search and replace, you can copy and paste the results into a spreadsheet and it will be six distinct columns. (If it doesn't, hollar.)



## More Regex

There are lots of sites and tutorials on regular expressions, but <http://www.regular-expressions.info/> is one of my favorites.

And remember, if you are stumped by something, chances are you are not the first. Google and Stack Overflow are your friends. ChatGPT might be helpful, too, if you are good at prompts.



## Key concept: patterns

Let's say you have a list of phone numbers in 10-digit format -- 512-555-1212 -- but you want the area code to be in parentheses: (512) 555-1212. You could do a simple search of the "512" area code followed by a dash "512-" and replace it with an area code in parentheses and a space: "(512) ".

But what if there are different area codes in the list?

```txt
512-555-1211
301-333-1212
410-123-1213
```

With regular expressions, you can search for a pattern of characters. Instead of searching just for 512-, you can look for "three numbers together at the beginning of a line that are then followed by a dash".

If you capture that matching pattern as a group, you can then replace that group with parentheses outside it, no matter what the contents of the group. If that saved group is called `$1` then you can replace it with `($1)` and it doesn't matter if `$1` is equal to "512-" or "301-".


## Special characters, commands and escape

Let's touch quickly on the syntax of regular expressions. Don't get hung up if these sound like gibberish, because it will make sense more when we start using it. This [Cheatsheet](cheatsheet.qmd) comes in handy here.

Regular expressions use special characters to do special things, like match the beginning of a line. These commands are called tokens. Some examples:

`^` will find the beginning of a line

`+` will find "one or more" of whatever precedes it.


Regular expressions use the backslash (the one above return on a keyboard where the top tips to the left) with other characters to create more tokens to do special things:

`\d` will find any number character (or digit).

`\D` will match anything other than a number.

`\t` is a tab character, because hitting the tab on the keyboard will perform the action instead of giving you the character.

But then sometimes, you actually need to find the character ^, and not use it as a command. Regular expressions use the \ to give the literal expression of a character that would otherwise be a token:

`\*` will find the asterisk character instead of the token to find "zero or more".



## Defining our goal

We're going to use regular expressions to split complicated address data into individual parts. The sample we'll use is a column from some City of Austin data published on their Socrata open data portal.

It had all the address parts crammed into a single field. Regex can easily explode that into individual columns, which is more useful to us.

So, our goal is to turn this ...

```txt
"10111 N LAMAR BLVD
AUSTIN, TX 78753
(30.370945933000485, -97.6925542359997)"
"2620 LAKE AUSTIN BLVD
AUSTIN, TX 78703
(30.28190796500047, -97.77587573499966)"
```

... into this, with each address part separated with a tab:

```txt
10111 N LAMAR BLVD  AUSTIN  TX  78753    30.370945933000485  -97.6925542359997
2620 LAKE AUSTIN BLVD   AUSTIN  TX  78703   30.28190796500047   -97.77587573499966
```

With this change, we can copy/paste the results into a spreadsheet.


## The goal in a nutshell

We are building a pattern in our regular expression field, creating "capture groups" for each part of the address that we want to keep. We'll continue the pattern outside the group until we get to the next part we want to keep, when we'll create a new group, and so on.

You'll want to reference your [Regex-Cheatsheet.docx](resources/Regex-Cheatsheet.docx) or [Regular-expressions-syntax.pdf](resources/Regular-expressions-syntax.pdf) in the resources folder.

Let's get started:

1. From Visual Studio Code where you are working with this, open the file [data/socrata_addresses_copy.txt](data/socrata_addresses_copy.txt).

This text is just one column from a larger Socrata data set of restaurant inspection scores in Austin, TX. (When I want to clean a single column of data, I often download the data and will just copy out one column into my text editor and work it before pasting back the results into a new Excel column, carefully making sure they still line up.)

Let's look at our data a little closer. This example from the top of the file is just one "cell" of data, even though it has multiple lines of text

```txt
"10111 N LAMAR BLVD
AUSTIN, TX 78753
(30.370945933000485, -97.6925542359997)"
```

The address, city, state, zip, latitude and longitude are all in the same "cell" (what is inside the quote marks), but the content of the cell has returns in it. We want to split these six distinct pieces into their own columns for each record. Why? Many reasons, but one is to use the latitude and longitude for data visualizations.

We will build a Regular Expression pattern to **Find** and capture six groups of text and then **Replace** those groups with tabs between them so we can put them back into a spreadsheet as columns.



## Building our Find pattern

1. In your `data/socrata_addresses_copy.txt` file, do **Command-option-f** to open the Find and Replace box. (Or menu: Edit > Replace)

    The Find/Replace window will open at the top right.

2. Next to Find you'll find some options. Click on the one that is a period-asterisk: .*


### Capturing the address

We'll begin entering tokens into the "Find" prompt so we can see how to use tokens to capture patterns. In some cases, we'll "capture" the pattern using parentheses, so we can refer back to it later.

We know that the first line starts at the beginning of the line, so we can start with this token: `^`.

1. Add the `^` to the Find prompt.

    You'll see that the first character of each line is now highlighted.
    
2. Next we want to **add the double-quote** so we can continue the pattern from the beginning of each address. Add a double-quote after the first token, like this:

    `^"`

    You'll notice that now only the double-quote marks are selected.
    

3. Next, we'll start our first capture group with parentheses:

    `^"()`
    
    You'll see as you type in the open parentheses that you'll get an "error" in the Find box because it expects a closing parentheses. Make sure you add that, then put your cursor back between them.

4. Now, inside those parentheses, we'll add `.*` so the full line looks like this:

    `^"(.*)`

    You'll see that the rest of the line has been selected.
    
    Inside the parentheses (our first group), we want to capture the whole address, which is everything until the end of the line. The period token `.` means "any character", and `*` means "zero or more", so put these together and we get everything: `^"(.*)`.
    

::: callout-warning

### New lines differe between Mac and PCs

Windows and MacOS sometimes treat new line tokens differently. On a Mac, `\n` is a "new line", but Windows uses `\R`. The regex101 editor will recognize either, and Visual Studio Code also seems to handle either, but if you are on Windows and have trouble, you might need to use `\R` instead of `\n` in some cases.


5. Add `\n` to the end of the string to make:

    `^"(.*)\n`


### Capturing the city

As we look through the list, you can see we have some cities with more than one word -- like "BEE CAVE" -- so we need a way to capture both letters and spaces, but not other punctuation. There are MANY ways to do this, but we'll use a "character set" to show how to use more than one token at a time:

1. First, create a new group:

    `^"(.*)\n()`

2. Then inside the group, we have to build the "character set" using square brackets. Inside those brackets we'll ad a `\w` token to catch any word character, and a space so we can catch those, too. Lastly, we put a `+` token right after the character set to signify we want "one or more":

    `^"(.*)\n([\w ]+)`


### Capturing the state

These addresses are all in TX, so we don't really have to save it at all, but we will. We'll use this to remind ourselves that you can also just match a string literally.

1. First we put the comma and space outside the second group, since we don't want to keep it:

    `^"(.*)\n(\w+), `

    
    You can't see that trailing space in the image above, but make sure it is there.
    
2. Then we create our third group with TX inside it:

    `^"(.*)\n([\w ]+), (TX)`


We choose to find the literal text "TX" because there are no other states in this data set. We can't skip it because we need the pattern to continue.

### Capturing the ZIP

Again, we don't want to keep the space between the state and ZIP, so we'll put it outside the third group.

1. Add the comma, space and new group to start our fourth group:

    `^"(.*)\n([\w ]+), (TX) ()`

2. All of these zip codes are of the 5-digit variety, so this can be less complicated than it might be with 9-digit ZIPs. Again, there are many ways to do this, but we'll use `\d` for the numbers and `*` to capture zero or more of them. Add those inside the capture group:

    `^"(.*)\n([\w ]+), (TX) (\d*)`

3. Complete the pattern for this line with the new line token `\n`. (**NOTE:** Remember to change the `\n` to `\R` if we are on PCs):

    `^"(.*)\n([\w ]+), (TX) (\d*)\n`


### Capturing latitude

1. We don't want to keep the parentheses that starts this last line, so we'll put it outside any capture group. However, since parentheses mean something special in regex, we need to escape it with a backslash so it will find the character and not start the new group:

    `^"(.*)\n([\w ]+), (TX) (\d*)\n\(`


2. Now we can start our new group, so go ahead and add the beginning and end parentheses:

    `^"(.*)\n([\w ]+), (TX) (\d*)\n\(()`

3. Inside our fifth group, we need numbers and the decimal point. We will create a character set using square brackets and put inside it `\d` for numbers and `\.` for the decimal point, which we have to escape since `.` means "any character". We finish it off by using `+` to look for one or more of the characters in the set. Like this:

    `^"(.*)\n([\w ]+), (TX) (\d*)\n\(([\d\.]+)`
    
    
### Capturing longitude

1. We don't need the comma and space in our next group, so we put it outside to keep the pattern going:

    `^"(.*)\n([\w ]+), (TX) (\d*)\n\(([\d\.]+), `
    
2. We can get the longitude like we did latitude, but we have to add the hyphen to the character set. So, create the group:

    `^"(.*)\n([\w ]+), (TX) (\d*)\n\(([\d\.]+), ()`
    
3. Add the character set:

    `^"(.*)\n([\w ]+), (TX) (\d*)\n\(([\d\.]+), ([])`

4. And inside of it, put `\d` for digits, `\-` for the hyphen and `\.` for the decimal point:

    `^"(.*)\n([\w ]+), (TX) (\d*)\n\(([\d\.]+), ([\d\-\.])`

4. Add our quantifier to get one or more:

    `^"(.*)\n([\w ]+), (TX) (\d*)\n\(([\d\.]+), ([\d\-\.]+)`

5. Because the trailing parentheses and quote are at the end of a line, we could ignore them, but we won't. We'll add them to the end of the pattern, escaping the close parentheses just to be sure:

    `^"(.*)\n([\w ]+), (TX) (\d*)\n\(([\d\.]+), ([\d\-\.]+)\)"`

    

## The Replace string

Now that we have a pattern with our six groups of data, we keep or exclude them in any order we want using the **Replace** prompt and the _replace all_ icon.

Our goal is to bring back six of our groups, but to put tabs in between each of them. If we can build a search and replace like this, then we can paste the result back into Excel, and each group will become its own column.

A quick refresher from our intro: Once we've built a group, we can reference it in our substitution string by order in which we captured it. So, if we want to reference our first group, we use this: `$1`.

1. Add this to the Replace prompt:

    `$1`

2. Click the second icon next to the replace string (which is replace all):


3. Now that you've seen that, do **Edit > Undo** to put our data back!

    I wasn't trying to scare you there, but you needed to see how replacing with a capture group worked.
    
4. Update the **Replace** string to add a tab token `\t` between each group.

    `$1\t$2\t$3\t$4\t$5\t$6`

5. And then use the **replace all icon** to do the Find/Replace on all rows.


### Add to Excel or Google Sheets

The way this text is structured, you can copy it all and then paste it into an Excel or Google Sheets spreadsheet and you should get six distinct rows.




## More Regex

There are lots of sites and tutorials on regular expressions, but [regular-expressions.info](http://www.regular-expressions.info/) is one of my favorites.

And remember, if you are stumped by something, chances are you are not the first. Google and Stack Overflow are your friends. ChatGPT might be helpful, too, if you are good at prompts.


## 2024-reshaping-data-sheets-colab.md

Reshaping data 
Google Sheets
Apps Script
Google Colab
A guide by Huyen Nguyen, Kansas State University

For my slides:
https://bit.ly/48T57bz

Intro
Reshaping data is considered a part of analyzing and visualizing data. Basically, you will process your data for a  specific type of data visualization. 
Two approaches:
1. Convert data from a wide to a long format, or spread data (Unpivot Table)
2. Convert data from a long to a wide format, or summarize data (Pivot Table)

1. Wide to long
Normally, we reshape data from wide to long format when we have multiple columns, variables or measures that we want to consolidate or plot together.


Source: Unemployment Data / Bureau of Labor Statistics
Wide table
Long table
Line chart

Dataset #1 from BLS – Job Seekers
In some situations, you will need to collapse your data from multiple columns into just one column, for example, if you have to process historical unemployment data from the Bureau of Labor Statistics, to build a line chart.
The website is a bit hard to navigate around. You want to locate Historical 'A' Tables (Household data): Previous years and months. Select Tables.
Locate Table A-11. Unemployed persons by reason for unemployment
Under UNEMPLOYED AS A PERCENT OF THE CIVILIAN LABOR FORCE, check all boxes on the second column Seasonally Adjusted.
Click Retrieve data.


Who is counted as unemployed? 
The total unemployment figures cover more than the number of people who have lost jobs. They include people who have quit their jobs to look for other employment, workers whose temporary jobs have ended, individuals looking for their first job, and experienced workers looking for jobs after an absence from the labor force (for example, stay-at-home parents who return to the labor force after their children have entered school). Information also is collected for the unemployed on the industry and occupation of the last job they held (if applicable), how long they have been looking for work, their reason for being jobless (for example, did they lose or quit their job), and their job search methods.

https://www.bls.gov/cps/cps_htgm.htm#unemployed

Create a new spreadsheet on Google Sheets
Sign up/Launch Google Sheets, a spreadsheet tool to handle data in rows and columns
Make a copy of my Google Sheet here. File > Make a copy
Look at the first sheet Job seekers.
We are going to combine the months and the years in one single column and collapse all relevant values (in percent of unemployment ) in another column, in order to build a line chart. 


We will look at the reasons in Job losers and persons who completed temporary jobs, or the first data table.
https://www.bls.gov/charts/employment-situation/reasons-for-unemployment.htm

Google Sheets Function – Flatten()
The =FLATTEN() function helps consolidate all the values from one or more data ranges into a single column. 
Let's create a new sheet. Name it Job seekers_wtl
Create two new columns starting from cell A1. Name them Time and Percent, respectively.
In cell A2, type a formula to flatten the rows and columns into one single column. 
=FLATTEN('Job seekers'!B15:M15&'Job seekers'!A16:A73)


Google Sheets Function – ARRAYFORMULA()
To hold the range of consolidated values returned from the FLATTEN() function, we need to use the =ARRAYFORMULA() function because it enables the display of values into multiple rows and/or columns. 
So, we have this formula:
 =ARRAYFORMULA(FLATTEN('Job seekers'!A16:A73&'Job seekers'!B15:M15))
But if we just use this formula, the year and the month will stick together, so let's modify the FLATTEN formula by adding a vertical bar between the two ranges. Note: You can use any delimiters, like a space or a comma.
FLATTEN('Job seekers'!B15:M15&"| "&'Job seekers'!A16:A73)
Or, we will have this:
=ARRAYFORMULA(FLATTEN('Job seekers'!B15:M15&" "&'Job seekers'!A16:A73))


Do It Again – FLATTEN()
Now, we just need to collapse all percentage values into the second column using the same =FLATTEN() function. In cell B2, type or select the relevant data range on the Job seekers sheet.
=FLATTEN('Job seekers'!B16:M73)
This time, you don’t need to wrap the function inside the =ARRAYFORMULA() function because you just flatten one dimension, not using the &.
That's how you flip data from wide to long format in most cases. Voila! We're done!


Dataset #2 from DHS – Green card 
Lawful permanent residents (LPRs) are normally referred to as “green card” holders, or foreigners who have long-term working permits.  The U.S. Department of Homeland Security kept track of these people through a multi-table database. Table 4 contains data classified by state or territory of residence from 2013 to 2022. 
The Census Bureau estimated the US population based on its survey and published data on this site. 
Using =ARRAYFORMULA() and FLATTEN() functions,  please flip lawful permanent residents data from the wide to the long format. 
Hint: On a new sheet, you need to create three new columns: State or territory, Year, and Persons.

https://www.dhs.gov/ohss/topics/immigration/yearbook/2022

The case of 3 columns
With the first dataset, you need to flip a wide table to just a 2-column long table. But in this dataset, you need to flip the wide table to a 3-column long table: State or territory, Year, and Persons.
Unfortunately, using the formulas above can only return and store consolidated values in a single column.
If you need to flip and spread data into 2 columns, you need to use the SPLIT() function

https://www.dhs.gov/ohss/topics/immigration/yearbook/2022

Google Sheets Function – SPLIT()
Let’s say you wrote this formula:
=ARRAYFORMULA(FLATTEN('Greencard holders'!A5:A60& "|" & 'Greencard holders'!B4:K4))
If you need to split the newly created column into two columns, you can use the =SPLIT() function and wrap it around the =FLATTEN() function, as below.
SPLIT(FLATTEN('Greencard holders'!A5:A60& "| " & 'Greencard holders'!B4:K4), "| ")
Just make sure you wrap the above function inside the =ARRAYFORMULA() function as below.
=ARRAYFORMULA(SPLIT(FLATTEN('Greencard holders'!A5:A60& "|" & 'Greencard holders'!B4:K4), " |"))


* You can also go to Data > Split text to columns after selecting the newly flipped column. 

2. Long to wide
Normally, we create a pivot table when we have data in a long format with multiple categories or groups in one column and we want to see the summary statistics for each category/group. 

Source: Weekly United States COVID-19 Cases and Deaths/ Centers for Disease Control and Prevention
Wide table
Long table
Racing bar chart

Dataset #3 from CDC – COVID-19 
Since the start of the COVID-19 pandemic, COVID-19 data have been gathered by the CDC. Reporting of new Aggregate Case and Death Count data was discontinued May 11, 2023, with the expiration of the COVID-19 public health emergency declaration. 
The data can be accessed through this portal. The datatable was structured in a long format. If you want to create a racing bar chart, you will need to flip the data from a long to a wide format.
The task can be done easily by creating a Pivot table, a feature popular for data summary and drill-down.

https://www.dhs.gov/ohss/topics/immigration/yearbook/2022

Use Pivot Table
First, select the long table (the one with year and month separately) by placing your cursor inside it, then hold Cmd/Ctrl-A. 
Next, go to Insert > Pivot table > New sheet. Name the new sheet COVID-19_ltw
Under Rows, add state.
Under Columns, add data_updated.
Under Values, add tot_deaths.
Uncheck Show Totals


Dataset #4 from the GCP - CO2 
The Washington Post published a racing line chart on March 1, 2023. Harry Stevens, the reporter and designer, provides his data source and codebook at this link.
Estimates for every country’s carbon dioxide emissions since 1750 was gathered from The Global Carbon Project. The data was last updated on Oct. 17, 2022.
The data can be accessed through this portal. The datatable was also structured in a long format. If you want to create a racing line chart, you will need to flip the data from a long to a wide format.
This dataset has 3 ID columns, instead of one as Dataset #3.
https://www.dhs.gov/ohss/topics/immigration/yearbook/2022

The case of multiple ID columns
ID columns refer to the columns in the long table that you want to keep and not spread in the flipped table.
Using a Pivot table in Google Sheets may be the fastest and most efficient way to flip data from a long to a wide format. It works even when you have multiple ID columns in your datatable.

Use Pivot Table
First, select the long table (the one with year and month separately) by placing your cursor inside it, then hold Cmd/Ctrl-A. 
Next, go to Insert > Pivot table > New sheet. Name the new sheet CO2_ltw
Under Filters > Year > Filter by condition > Greater than or equal to 1900. You will notice that Google Sheets can’t flip data since 1750. 
Under Rows, add all 3 ID columns: Country, ISO 3166-1, and UN M49.
Under Columns, add Year.
Under Values, add Total.
Uncheck Show Totals


App Scripts

https://developers.google.com/apps-script/overview

What’s for?
Apps Script can be used to create custom functions interacting with your Google Sheet files and the data they contain. 
To write the scripts, you need to first go to Extensions > Apps Script and add the custom scripts. 
To learn how to write the scripts, check out this guide. 
In this session, we will adopt and revise the free scripts written by Robin Gertenbach, a data scientist working for Google. Using scripts is a faster way to reshape data. These scripts will generate two custom functions melt(), to reshape data from wide to long, and cast(), to reshape data from long to wide.
You just need to set up the scripts for one Google Sheets template, and you can make a copy and reuse it for multiple reshaping tasks.

https://developers.google.com/codelabs/apps-script-fundamentals-1#0

How to set up the scripts?
Please create a new spreadsheet.  Go to Extensions > Apps Script and add the custom scripts. You need to click on the Plus sign to add a new script or a new HTML page. 
First, please copy and paste all Robin’s code inside Auxilliaries.gs, Cast.gs, Front End.gs, and Melt.gs into Apps Script.  
Make sure you modified the function nativeType as in the sidebar.
Then, add an HTML page. Make sure you paste Robin’s LICENSE text between the <body> </body> HTML tags.
Save them all. 
If you are successful, you can start using the cast() and melt() functions in Google Sheets.
For your convenience, I have the scripts ready here for you to make a copy.
* Casts a string to a number of possible, otherwise returns the string.
*/
function nativeType(x) {
 if (!isNaN(Number(x))) {
   return Number(x);
 }
 // Check if the string represents a date in the format YYYY-MM-DD
 var dateRegex = /^\d{4}-\d{2}-\d{2}$/;
 if (dateRegex.test(x)) {
   return x;
 }
 return x;
}

https://developers.google.com/codelabs/apps-script-fundamentals-1#0

How to use custom functions?
WIDE TO LONG 
Type the MELT() function:
=MELT(<Table>, *<ID Columns>*, <Measure Column Name>, <Value Column Name>, <Blanks Behavior>)
Table is the range of the wide table. 
ID Columns are the range of the column headers that are not pivoted.
Measure Column Name (optional) contains the names of the molten columns.
Value Column Name (optional) contains the molten values.
Blanks Behavior (optional) controls how the melt function handles blank columns and or rows. No Removal is default.
 


LONG TO WIDE
Type the CAST() function:
=CAST(<Table>, <Measure Column>, <Value Column>, <Default Value>)
Table is the range of the long table.
Measure Column is the column that will be pivoted into multiple columns.
Value Column is the column that contains the actual measurement that will be populated into a two dimensional matrix.
Default Value The default value is equal to a blank cell.


https://github.com/rgertenbach/Reshape/blob/master/README.md

Wide to Long 
Let’s reuse the first dataset about job seekers.
You just need to create a new sheet and type:
=MELT('Job seekers'!A15:M73,'Job seekers'!A15, "Month", "Percent")

For the second dataset about green card holders, you can type:
=MELT('Greencard holders'!A4:K60, 'Greencard holders'!A4, "Year", "Persons")


Long to wide 
If you want to flip the first dataset from a long back to a wide format, you can type:
=CAST(Jobseekers_2!A1:C697, Jobseekers_2!B1, Jobseekers_2!C1)

If you want to flip the second dataset from a long back to a wide format, you can type:
=CAST('GCH 2_wtl'!A1:C561,'GCH 2_wtl'!B1,'GCH 2_wtl'!C1)
*The Apps Script we added to Google Sheets can’t flip long tables of the third and fourth datasets because both are too large for the script to handle. 

**Google Sheets can handle up to 10 million cells or 18,278 columns (column ZZZ) https://support.google.com/drive/answer/37603?sjid=15168927794972884782-NC

Google Colab
https://developers.google.com/apps-script/overview

What’s for?
To deal with large datasets, you need a more powerful platform or a programming language such as Python and R outside of Google Sheets.
A convenient platform for you to write Python/R code to reshape data and write the output back to Google Sheets is Google Colab.
To learn more about Colab, check out this introduction. 
For this training, please make a copy of my Colab notebook. 

https://developers.google.com/codelabs/apps-script-fundamentals-1#0

How to reshape data in Colab?
First, you need to upload your data to Google Drive,  create a new spreadsheet in Google Sheets, or upload your data to Colab directly (if datasets are too large, and then you have to use a different method to read data into a dataframe).
Then, connect Google Colab to Google Sheets using the gspread package.
Third, import the pandas package and use the pivot() function to flip data from a long to a wide format. To flip data from a wide to a long format, use the melt() function. 
Fourth, write the new dataframe back to your Google Sheets.
Let’s get started!
 
https://developers.google.com/codelabs/apps-script-fundamentals-1#0

Dataset #3 from CDC – COVID-19 
Since the start of the COVID-19 pandemic, COVID-19 data have been gathered by the CDC. Reporting of new Aggregate Case and Death Count data was discontinued May 11, 2023, with the expiration of the COVID-19 public health emergency declaration. 
We will reuse this dataset. 
To keep it simple, you can make a copy of my spreadsheet. The datatable was first structured in a long format. You will flip it in a wide format and reverse the process.

https://www.dhs.gov/ohss/topics/immigration/yearbook/2022

Dataset #4 from the GCP - CO2 
The Washington Post published a racing line chart on March 1, 2023. Harry Stevens, the reporter and designer, provides his data source and codebook at this link.
Estimates for every country’s carbon dioxide emissions since 1750 was gathered from The Global Carbon Project. The data was last updated on Oct. 17, 2022.
The data can be accessed through this portal. The datatable was also structured in a long format. If you want to create a racing line chart, you will need to flip the data from a long to a wide format.
Try using the pivot() function, but make sure you keep the ID columns or the index columns in Python.
wide_df = df.pivot(index=['Country', 'ISO 3166-1 alpha-3','UN M49'], columns='Year', values='Total')

Check out the long answer here and a short answer here. 
https://www.dhs.gov/ohss/topics/immigration/yearbook/2022

Dataset #5 from DW - Air Quality
Deutsche Welle (DW) published an article about air pollution in Europe, in collaboration with the European Data Journalism Network.
The data can be accessed through this GitHub account. DW processed data from  the Copernicus Atmospheric Monitoring Service (CAMS). 
There are several Excel files on the GitHub account. 
You can try flipping data in CAMS-Europe-Renalaysis-Countries-Yearly-2018-2022.xlsx file, which has a wide format, and CAMS-Europe-Forecast-Daily-2023.xlsx, which has a long format. 

Check out the short answer here. 

 the Copernicus Atmospheric Monitoring Service (CAMS)

Thank you for your attention!
I hope these tips are useful for your data processing projects.
If you have any questions, please feel free to contact: huyenme@ksu.edu



## 2024-text-analysis-languages.md

Text analysis in different languages for investigations

Link to these slides: bit.ly/nicar24-text-analysis 

Who’s who?
Lam Thuy Vo
(she/they)
CUNY/The Markup
Moderator
Fernanda Aguirre
(she/her)
The Examination
Chris Amico
(he/him)
Muckrock
Josephine Lukito 
(she/her)
University of Texas

Some text analysis concepts

Natural language processing
Turning text into data

Natural language processing	(NLP)
NLP helps computers understand, interpret and manipulate human language.

Some concepts
Corpus
Tokenizing
Stemming or lemmatizing

We’re entering the realm of endless jargon

Some concepts
Corpus
Tokenizing
Stemming or lemmatizing

A corpus (plural corpora) or text corpus is a large and structured set of texts 

Some concepts
Corpus
Tokenizing
Stemming or lemmatizing

Tokenizing is the process of splitting your corpus into subsections: phrases, sentences, words.

Some concepts
Corpus
Tokenizing
Stemming and lemmatization

The goal of both stemming and lemmatization is to reduce inflectional forms and sometimes derivationally related forms of a word to a common base form. 

For instance:
am, are, is →  be 
car, cars, car's, cars' →  car

The result of this mapping of text will be something like:

the boy's cars are different colors  
→ the boy car be differ color
https://nlp.stanford.edu/IR-book/html/htmledition/stemming-and-lemmatization-1.html 

Stemming usually refers to a crude heuristic process that chops off the ends of words in the hope of achieving this goal correctly most of the time, and often includes the removal of derivational affixes. Lemmatization usually refers to doing things properly with the use of a vocabulary and morphological analysis of words, normally aiming to remove inflectional endings only and to return the base or dictionary form of a word, which is known as the lemma . If confronted with the token saw, stemming might return just s, whereas lemmatization would attempt to return either see or saw depending on whether the use of the token was as a verb or a noun. 

Some concepts
Corpus
Tokenizing
Stemming and lemmatization

Stemming vs. lemmatization

Example: “saw”
(As in “I saw a bird, or was it a plane? I think it may have been Supergirl.”)

Stem:
saw → s

Lemma:
saw → see*

*  if the token is a verb!


https://nlp.stanford.edu/IR-book/html/htmledition/stemming-and-lemmatization-1.html 

Stemming usually refers to a crude heuristic process that chops off the ends of words in the hope of achieving this goal correctly most of the time, and often includes the removal of derivational affixes. Lemmatization usually refers to doing things properly with the use of a vocabulary and morphological analysis of words, normally aiming to remove inflectional endings only and to return the base or dictionary form of a word, which is known as the lemma. If confronted with the token saw, stemming might return just s, whereas lemmatization would attempt to return either see or saw depending on whether the use of the token was as a verb or a noun. 

Examples


TEXT ANALYSIS
English data
non-English data

Useful applications of text analysis:

Organizing documents
Exploratory exercise
Data analysis

Text processing

Tips:

Keep it simple
Use available resources
Research the backdrop of these resources
Automation still requires manual verification

My favorite techniques:

Entity extraction (Named Entity Recognition)
Identify themes (Topic Modeling)
Label types of words (Part Of Speech Tagging)
Split text into smaller units (Tokenization: sentences / words)
Find the base form of a word (Lemmatization)
Resolve relationships between entities (Coreference Resolution)
Find information based on the meaning of the query (Semantic Search)

Resources
Tools:
DocumentCloud - MuckRock
Aleph - OCCRP
Datashare - ICIJ
Pinpoint - Google


Resources
Python libraries:
Spacy
Stanza
NLTK
Transformers
BERTopic


Text analysis with DocumentCloud
Chris Amico
March 7, 2024

Upload
Extract
Analyze
Search
Annotate
Redact
Edit
Embed & Publish
Collaborate
Add-Ons

Uploading 
(and other ways to get files into DocumentCloud)


Web upload
Batch upload CLI
Scraper Add-On

Extract 
(text, tables, entities and more)

OCR
Entity extraction
Table extraction add-ons
Regex Add-On

Your automated analysis is only going to be as good as your OCR.


Search 
(across or within documents)

Documentation: https://www.documentcloud.org/help/search/

Ed ut perspiciatis unde omnis iste natus error sit voluptatem
Ed ut perspiciatis unde omnis iste

Annotate 
(for yourself, 
your team, 
the world)


Redact 
(and find bad redactions)


Edit (fix, combine, rotate)

Embed & Publish

Document
Page
Note
Project

There’s an Add-On for that
Some of my favorites:

Transcribe Audio (Whisper)
Klaxon
GPT 3.5 Turbo Playground
Custom metadata scraper
Bad Redactions
Scraper

Finding bad air days that don’t count
https://www.theguardian.com/us-news/2023/oct/16/epa-local-governments-dont-report-air-pollution-wildfire-smoke-data-across-us 

Finding bad air days that don’t count
Case Study
https://www.documentcloud.org/documents/23844714-ed_014139_00000407_formal_rif

Tools + Methods
Projects, Annotations & Add-Ons
Planning, Collaboration & Work

Dealing with Images and Audio
Image to Text: Optical Character Recognition (OCR)
Tesseract, in R and Python

Audio to Text: Automated Transcription/Speech-to-Text
Whisper (OpenAI-WhisperGUI)

Translation Tools
Language Detection
R: {textcat} (~60 languages)
Python: {langdetect} (~50 languages), {polyglot} (+100 languages)
Google Sheets: =DETECTLANGUAGE()

Language Translation
R: {translateR}
[$] Deepl: https://www.deepl.com/translator, {deeplr}
Python: {polyglot} 
Deepl: {deepl-python}
Google Sheets: =GOOGLETRANSLATE()

=DETECTLANGUAGE()
https://docs.google.com/spreadsheets/d/1LFRdBIKzHPCN2Qm8x5hZ8RQGKqqVBGwiWMcH5IaLxtY/edit#gid=0 


=GOOGLETRANSLATE()

https://docs.google.com/spreadsheets/d/1LFRdBIKzHPCN2Qm8x5hZ8RQGKqqVBGwiWMcH5IaLxtY/edit#gid=0 

https://developers.google.com/admin-sdk/directory/v1/languages 

Recognizing Inequitable Language Resources
What Language (e.g., “Bahasa Indonesia”, “Portuguese”)


https://medium.com/neuralspace/low-resource-language-what-does-it-mean-d067ec85dea5 

Finding non-English resources
What Language (e.g., “Bahasa Indonesia”, “Portuguese”)
Low-Resource Languages
High-Resource Languages
What Task
Tokenizer
Stemmer
Lemmatizer
“Part of Speech” tagger
What Type (e.g., R, Python, open source, user interface/ui/gui)
Indonesian tokenizer Python

Case: Brazilian Journalism
“Brazilian Capitol attack: The interaction between Bolsonaro’s supporters’ content, WhatsApp, Twitter, and news media” (forthcoming in HKS Misinfo Review)


Resources
Story about disinfo in Vietnamese communities |  Github code
Oscars NLP project | Github code
Immigration lawyer story | GitHub code

Questions?
Fernanda Aguirre
Email: fernanda@theexamination.org 
Twitter: @feragru

Chris Amico
Email: chris@muckrock.com 
Twitter: @eyeseast

Josephine Lukito
Email: jlukito@utexas.edu 
Twitter: @josephinelukito 

Lam Thuy Vo
Email: contactlamvo@gmail.com 
Twitter: @lamthuyvo


## Collections of data

Now we\'re going to talk about two ways you can use Python to group data into a collection: lists and dictionaries.

### Lists

A *list* is a comma-separated list of items inside square brackets: `[]`.

Here\'s a list of ingredients, each one a string, that together makes up a salsa recipe.

``` python
salsa_ingredients = ['tomato', 'onion', 'jalapeño', 'lime', 'cilantro']
```

To get an item out of a list, you\'d refer to its numerical position in the list \-- its *index* (1, 2, 3, etc.) \-- inside square brackets immediately following your reference to that list. In Python, as in many other programming languages, counting starts at 0. That means the first item in a list is item `0`.

``` python
salsa_ingredients[0]
```

``` python
salsa_ingredients[1]
```

You can use *negative indexing* to grab things from the right-hand side of the list \-- and in fact, `[-1]` is a common idiom for getting \"the last item in a list\" when it\'s not clear how many items are in your list.

``` python
salsa_ingredients[-1]
```

If you wanted to get a slice of multiple items out of your list, you\'d use colons (just like in Excel, kind of!).

If you wanted to get the first three items, you\'d do this:

``` python
salsa_ingredients[0:3]
```

You could also have left off the initial 0 \-- when you leave out the first number, Python defaults to \"the first item in the list.\" In the same way, if you leave off the last number, Python defaults to \"the last item in the list.\"

``` python
salsa_ingredients[:3]
```

Note, too, that this slice is giving us items 0, 1 and 2. The `3` in our slice is the first item we *don\'t* want. That can be kind of confusing at first. Let\'s try a few more:

``` python
# everything in the list except the first item
salsa_ingredients[1:]
```

``` python
# the second, third and fourth items
salsa_ingredients[1:4]
```

``` python
# the last two items
salsa_ingredients[-2:]
```

To see how many items are in a list, use the `len()` function:

``` python
len(salsa_ingredients)
```

To add an item to a list, use the [`append()`](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) method:

``` python
salsa_ingredients
```

``` python
salsa_ingredients.append('mayonnaise')
```

``` python
salsa_ingredients
```

Haha *gross*. To remove an item from a list, use the `pop()` method. If you don\'t specify the index number of the item you want to pop out, it will default to \"the last item.\"

``` python
salsa_ingredients.pop()
```

``` python
salsa_ingredients
```

You can use the [`in` and `not in`](https://docs.python.org/3/reference/expressions.html#membership-test-operations) expressions to test membership in a list (will return a boolean):

``` python
'lime' in salsa_ingredients
```

``` python
'cilantro' not in salsa_ingredients
```

### Dictionaries

A *dictionary* is a comma-separated list of key/value pairs inside curly brackets: `{}`. Let\'s make an entire salsa recipe:

``` python
salsa = {
    'ingredients': salsa_ingredients,
    'instructions': 'Chop up all the ingredients and cook them for awhile.',
    'oz_made': 12
}
```

To retrieve a value from a dictionary, you\'d refer to the name of its key inside square brackets `[]` immediately after your reference to the dictionary:

``` python
salsa['oz_made']
```

``` python
salsa['ingredients']
```

To add a new key/value pair to a dictionary, assign a new key to the dictionary inside square brackets and set the value of that key with `=`:

``` python
salsa['tastes_great'] = True
```

``` python
salsa
```

To delete a key/value pair out of a dictionary, use the `del` command and reference the key:

``` python
del salsa['tastes_great']
```

``` python
salsa
```

### Indentation

Whitespace matters in Python. Sometimes you\'ll need to indent bits of code to make things work. This can be confusing! `IndentationError`s are common even for experienced programmers. (FWIW, Jupyter will try to be helpful and insert the correct amount of \"significant whitespace\" for you.)

You can use tabs or spaces, just don\'t mix them. [The Python style guide](https://www.python.org/dev/peps/pep-0008/) recommends indenting your code in groups of four spaces, so that\'s what we\'ll use.

### `for` loops

You would use a `for` loop to iterate over a collection of things. The statement begins with the keyword `for` (lowercase), then a temporary `variable_name` of your choice to represent each item as you loop through the collection, then the Python keyword `in`, then the collection you\'re looping over (or its variable name), then a colon, then the indented block of code with instructions about what to do with each item in the collection.

Let\'s say we have a list of numbers that we assign to the variable `list_of_numbers`.

``` python
list_of_numbers = [1, 2, 3, 4, 5, 6]
```

We could loop over the list and print out each number:

``` python
for number in list_of_numbers:
    print(number)
```

We could print out each number *times 6*:

``` python
for number in list_of_numbers:
    print(number*6)
```

\... whatever you need to do in you loop. Note that the variable name `number` in our loop is totally arbitrary. This also would work:

``` python
for banana in list_of_numbers:
    print(banana)
```

It can be hard, at first, to figure out what\'s a \"Python word\" and what\'s a variable name that you get to define. This comes with practice.

Strings are iterable, too. Let\'s loop over the letters in a sentence:

``` python
sentence = 'Hello, IRE/NICAR!'

for letter in sentence:
    print(letter)
```

To this point: Strings are iterable, like lists, so you can use the same kinds of methods:

``` python
# get the first five characters
sentence[:5]
```

``` python
# get the length of the sentence
len(sentence)
```

``` python
'Hello' in sentence
```

You can iterate over dictionaries, too \-- just remember that dictionaries *don\'t keep track of the order that items were added to it*.

When you\'re looping over a dictionary, the variable name in your `for` loop will refer to the keys. Let\'s loop over our `salsa` dictionary from up above to see what I mean.

``` python
for key in salsa:
    print(key)
```

To get the *value* of a dictionary item in a for loop, you\'d need to use the key to retrieve it from the dictionary:

``` python
for key in salsa:
    print(salsa[key])
```

### `if` statements

Just like in Excel, you can use the \"if\" keyword to handle conditional logic.

These statements begin with the keyword `if` (lowercase), then the condition to evaluate, then a colon, then a new line with a block of indented code to execute if the condition resolves to `True`.

``` python
if 4 < 6:
    print('4 is less than 6')
```

You can also add an `else` statement (and a colon) with an indented block of code you want to run if the condition resolves to `False`.

``` python
if 4 > 6:
    print('4 is greater than 6?!')
else:
    print('4 is not greater than 6.')
```

If you need to, you can add multiple conditions with `elif`.

``` python
HOME_SCORE = 6
AWAY_SCORE = 8

if HOME_SCORE > AWAY_SCORE:
    print('we won!')
elif HOME_SCORE == AWAY_SCORE:
    print('we tied!')
else:
    print('we lost!')
```



## **1 Python syntax cheat sheet**


This notebook demonstrates some basic syntax rules of the Python programming language.


 - Basic data types

**–** Strings

**–** Numbers and math

**–** Booleans

 - Variable assignment

 - String methods

 - Comments

 - The print() function

 - Collections of data

**–** Lists

**–** Dictionaries

 - for loops

 - if statements


**1.0.1** **Basic** **data** **types**


Just like Excel and other data processing software, Python recognizes a variety of data types,
including three we’ll focus on here: - Strings (text) - Numbers (integers, numbers with decimals
and more) - Booleans ( `True` and `False` ).


You can use the built-in `[type()](https://docs.python.org/3/library/functions.html#type)` function to check the data type of a value.


**Strings** A string is a group of characters - letters, numbers, whatever - enclosed within single
or double quotes (doesn’t matter as long as they match). The code in these notebooks uses single
quotes. (The Python style guide doesn’t recommend one over the other: “Pick a rule and stick to
[it.”)](https://www.python.org/dev/peps/pep-0008/#string-quotes)


If your string _contains_ apostrophes or quotes, you have two options: _Escape_ the offending character
with a forward slash `\` :

```
'Isn \' t it nice here?'

```

… or change the surrounding punctuation:

```
"Isn't it nice here?"

```

The style guide recommends the latter over the former.


When you call the `type()` function on a string, Python will return `str` .


Calling the `str()` [function](https://docs.python.org/3/library/stdtypes.html#str) on a value will return the string version of that value (see examples
below).

```
[ ]: 'Investigative Reporters and Editors'

[ ]: type('hello!')

[ ]: 45

[ ]: type(45)

[ ]: str(45)

[ ]: type(str(45))

[ ]: str( True )

```

If you “add” strings together with a plus sign `+`, it will concatenate them:

```
[ ]: 'IRE' + '/' + 'NICAR'

```

**Numbers** **and** **math** Python recognizes a variety of numeric data types. Two of the most
common are integers (whole numbers) and floats (numbers with decimals).


Calling `int()` on a piece of numeric data (even if it’s being stored as a string) will attempt to
coerce it to an integer; calling `float()` will try to convert it to a float.

```
[ ]: 12

[ ]: 12.4

[ ]: type(12)

[ ]: type(12.4)

[ ]: int(35.6)

[ ]: int('45')

[ ]: float(46)

[ ]: float('45')

```

You can do basic math in Python. You can also do more [advanced](https://docs.python.org/3/library/math.html) math.

```
[ ]: 4+2

```

```
[ ]: 10-9

[ ]: 5*10

[ ]: 1000/10

```


**Booleans** Just like in Excel, which has `TRUE` and `FALSE` data types, Python has boolean data
types. They are `True` and `False`    - note that only the first letter is capitalized, and they are not
sandwiched between quotes.


Boolean values are typically returned when you’re evaluating some sort of conditional statement   comparing values, checking to see if a string is inside another string or if a value is in a list, etc.


Python’s [comparison](https://docs.python.org/3/reference/expressions.html#comparisons) operators include:


   - `>` greater than

   - `<` less than

   - `>=` greater than or equal to

   - `<=` less than or equal to

   - `==` equal to

   - `!=` not equal to

```
[ ]: True

[ ]: False

[ ]: 4 > 6

[ ]: 10 == 10

[ ]: 'crapulence' == 'Crapulence'

[ ]: type( True )

```

**1.0.2** **Variable** **assignment**


The `=` sign assigns a value to a variable name that you choose. Later, you can retrieve that value
by referencing its variable name. Variable names can be pretty much anything you want (as [long](https://thehelloworldprogram.com/python/python-variable-assignment-statements-rules-conventions-naming/)
as you follow [some](https://thehelloworldprogram.com/python/python-variable-assignment-statements-rules-conventions-naming/) basic rules).


This can be a tricky concept at first! For more detail, here’s a pretty good [explainer](https://www.digitalocean.com/community/tutorials/how-to-use-variables-in-python-3) from Digital
[Ocean.](https://www.digitalocean.com/community/tutorials/how-to-use-variables-in-python-3)

```
[ ]: my_name = 'Frank'

[ ]: my_name

```

You can also _reassign_ a different value to a variable name, though it’s usually better practice to
create a new variable.

```
[ ]: my_name = 'Susan'

[ ]: my_name

```

A common thing to do is to “save” the results of an expression by assigning the result to a variable.

```
[ ]: my_fav_number = 10 + 3

[ ]: my_fav_number

```

It’s also common to refer to previously defined variables in an expression:

```
[ ]: number_of_pro_sports_teams

```

**1.0.3** **String** **methods**


Let’s go back to strings for a second. String objects have a number of useful [methods](https://docs.python.org/3/library/stdtypes.html#string-methods)    - let’s use
an example string to demonstrate a few common ones.

```
[ ]: my_cool_string = ' Hello, friends!'

```

`upper()` converts the string to uppercase:

```
[ ]: my_cool_string.upper()

```

`lower()` converts to lowercase:

```
[ ]: my_cool_string.lower()

```

`replace()` will replace a piece of text with other text that you specify:

```
[ ]: my_cool_string.replace('friends', 'enemies')

```

`count()` will count the number of occurrences of a character or group of characters:

```
[ ]: my_cool_string.count('H')

```

Note that `count()` is case-sensitive. If your task is “count all the e’s,” convert your original string
to upper or lowercase first:


```
[ ]: my_cool_string.upper().count('E')

```

`[split()](https://docs.python.org/3/library/stdtypes.html#str.split)` will split the string into a list (more on these in a second) on a given delimiter (if you
don’t specify a delimiter, it’ll default to splitting on a space):

```
[ ]: my_cool_string.split()

[ ]: my_cool_string.split(',')

[ ]: my_cool_string.split('Pitt')

```

`strip()` removes whitespace from either side of your string (but not internal whitespace):

```
[ ]: my_cool_string.strip()

```

You can use a cool thing called “method chaining” to combine methods   - just tack ’em onto the
end. Let’s say we wanted to strip whitespace from our string _and_ make it uppercase:

```
[ ]: my_cool_string.strip().upper()

```

Notice, however, that our original string is unchanged:

```
[ ]: my_cool_string

```

Why? Because we haven’t assigned the results of anything we’ve done to a variable. A common
thing to do, especially when you’re cleaning data, would be to assign the results to a new variable:

```
[ ]: my_cool_string_clean = my_cool_string.strip().upper()

[ ]: my_cool_string_clean

```

**1.0.4** **Comments**


A line with a comment  - a note that you don’t want Python to interpret  - starts with a `#` sign.
These are notes to collaborators and to your future self about what’s happening at this point in
your script, and why.


Typically you’d put this on the line right above the line of code you’re commenting on:


Multi-line comments are sandwiched between triple quotes (or triple apostrophes):

```
''' this is a long comment '''

```

or

```
""" this is a long comment """

```

**1.0.5** **The** **`print()`** **function**


So far, we’ve just been running the notebook cells to get the last value returned by the code we
write. Using the `[print()](https://docs.python.org/3/library/functions.html#print)` function is a way to print specific things in your script to the screen.
This function is handy for debugging.


To print multiple things on the same line, separate them with a comma.

```
[ ]: print('Hello!')

[ ]: print(my_name)

[ ]: print('Hello,', my_name)

```

**1.1** **Collections** **of** **data**


Now we’re going to talk about two ways you can use Python to group data into a collection: lists
and dictionaries.


**1.1.1** **Lists**


A _list_ is a comma-separated list of items inside square brackets: `[]` .


Here’s a list of ingredients, each one a string, that together makes up a salsa recipe.

```
[ ]: salsa_ingredients = ['tomato', 'onion', 'jalapeño', 'lime', 'cilantro']

```

To get an item out of a list, you’d refer to its numerical position in the list – its _index_ (1, 2, 3, etc.)

   - inside square brackets immediately following your reference to that list. In Python, as in many
other programming languages, counting starts at 0. That means the first item in a list is item `0` .

```
[ ]: salsa_ingredients[0]

[ ]: salsa_ingredients[1]

```

You can use _negative_ _indexing_ to grab things from the right-hand side of the list – and in fact, `[-1]`
is a common idiom for getting “the last item in a list” when it’s not clear how many items are in
your list.

```
[ ]: salsa_ingredients[-1]

```

If you wanted to get a slice of multiple items out of your list, you’d use colons (just like in Excel,
kind of!).


If you wanted to get the first three items, you’d do this:

```
[ ]: salsa_ingredients[0:3]

```

You could also have left off the initial 0   - when you leave out the first number, Python defaults to
“the first item in the list.” In the same way, if you leave off the last number, Python defaults to
“the last item in the list.”


```
[ ]: salsa_ingredients[:3]

```

Note, too, that this slice is giving us items 0, 1 and 2. The `3` in our slice is the first item we _don’t_
want. That can be kind of confusing at first. Let’s try a few more:


To see how many items are in a list, use the `len()` function:

```
[ ]: len(salsa_ingredients)

```

To add an item to a list, use the `[append()](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)` method:

```
[ ]: salsa_ingredients

[ ]: salsa_ingredients.append('mayonnaise')

[ ]: salsa_ingredients

```

Haha _gross_ . To remove an item from a list, use the `pop()` method. If you don’t specify the index
number of the item you want to pop out, it will default to “the last item.”

```
[ ]: salsa_ingredients.pop()

[ ]: salsa_ingredients

```

You can use the `in` and `not` `in` expressions to test membership in a list (will return a boolean):

```
[ ]: 'lime' in salsa_ingredients

[ ]: 'cilantro' not in salsa_ingredients

```

**1.1.2** **Dictionaries**


A _dictionary_ is a comma-separated list of key/value pairs inside curly brackets: `{}` . Let’s make an
entire salsa recipe:


To retrieve a value from a dictionary, you’d refer to the name of its key inside square brackets `[]`
immediately after your reference to the dictionary:

```
[ ]: salsa['oz_made']

[ ]: salsa['ingredients']

```

To add a new key/value pair to a dictionary, assign a new key to the dictionary inside square
brackets and set the value of that key with `=` :

```
[ ]: salsa['tastes_great'] = True

[ ]: salsa

```

To delete a key/value pair out of a dictionary, use the `del` command and reference the key:

```
[ ]: del salsa['tastes_great']

[ ]: salsa

```

**1.1.3** **Indentation**


Whitespace matters in Python. Sometimes you’ll need to indent bits of code to make things
work. This can be confusing! `IndentationError` s are common even for experienced programmers.
(FWIW, Jupyter will try to be helpful and insert the correct amount of “significant whitespace”
for you.)


You can use tabs or spaces, just don’t mix them. The [Python](https://www.python.org/dev/peps/pep-0008/) style guide recommends indenting
your code in groups of four spaces, so that’s what we’ll use.


**1.1.4** **`for`** **loops**


You would use a `for` loop to iterate over a collection of things. The statement begins with the
keyword `for` (lowercase), then a temporary `variable_name` of your choice to represent each item
as you loop through the collection, then the Python keyword `in`, then the collection you’re looping
over (or its variable name), then a colon, then the indented block of code with instructions about
what to do with each item in the collection.


Let’s say we have a list of numbers that we assign to the variable `list_of_numbers` .

```
[ ]: list_of_numbers = [1, 2, 3, 4, 5, 6]

```

We could loop over the list and print out each number:


We could print out each number _times_ _6_ :


… whatever you need to do in you loop. Note that the variable name `number` in our loop is totally
arbitrary. This also would work:


It can be hard, at first, to figure out what’s a “Python word” and what’s a variable name that you
get to define. This comes with practice.


Strings are iterable, too. Let’s loop over the letters in a sentence:


To this point: Strings are iterable, like lists, so you can use the same kinds of methods:


```
[ ]: 'Hello' in sentence

```

You can iterate over dictionaries, too – just remember that dictionaries _don’t keep track of the order_
_that_ _items_ _were_ _added_ _to_ _it_ .


When you’re looping over a dictionary, the variable name in your `for` loop will refer to the keys.
Let’s loop over our `salsa` dictionary from up above to see what I mean.


To get the _value_ of a dictionary item in a for loop, you’d need to use the key to retrieve it from the
dictionary:


**1.1.5** **`if`** **statements**


Just like in Excel, you can use the “if” keyword to handle conditional logic.


These statements begin with the keyword `if` (lowercase), then the condition to evaluate, then a
colon, then a new line with a block of indented code to execute if the condition resolves to `True` .


You can also add an `else` statement (and a colon) with an indented block of code you want to run
if the condition resolves to `False` .


If you need to, you can add multiple conditions with `elif` .


## Login

::: mp-form-label
Username or E-mail

:::: mp-form-label
Password

::: mp-hide-pw


Remember Me

::: mp-spacer
 

::: submit

::: mp-spacer
 

::: mepr-login-actions
[Forgot Password](https://www.ire.org/login/?action=forgot_password)

![IRE favicon](https://www.ire.org/wp-content/uploads/2020/01/IRE_favicon.png)

To have full access to resources and the ability to register for events, please log into your member account!



## Login

::: mp-form-label
Username or E-mail

:::: mp-form-label
Password

::: mp-hide-pw


Remember Me

::: mp-spacer
 

::: submit

::: mp-spacer
 

::: mepr-login-actions
[Forgot Password](https://www.ire.org/login/?action=forgot_password)

[join ire](https://www.ire.org/join-ire/)[continue as guest](http://)

::: ct-section-inner-wrap
# Past IRE Board Members

::::::::::: ct-section-inner-wrap
An asterisk (\*) denotes service as board president; (dec) indicates the person is deceased.\

Paul Adrian (2000-2006)

Matt Apuzzo (2017-2019)

Rosemary Armao (1997-2001)

Bethany Barnes (2019-2021)

Roberta Baskin (1998-2000)

\*David Boardman (1997-2007)

Walt Bogdanich (1988-1992)

Ziva Branstetter (2013-2019)

Darla Cameron (2022-present)

John Camp (1990-1992)

Rose Ciotta (1993-2001)

Wendell Cochran (2006-2008)

\*Sarah Cohen (2010-2018)

Robert Cribb (2009-2014)

Bill Dedman (1990-1996)

Matt Dempsey (2018-2020)

\*David Dietz (1996-2004) (dec)

Steve Doig (2002-2006)

Andrew Donohue (2010-2018)

Leonard Downie Jr. (2009-2015)

Bob Drogin (1986-1989)

Bill Farr (1978-1985) (dec)

Renee Ferguson (2006-2008)

Jodie Fleischer (2019-present)

Jennifer Forsyth (2020-2022)

Ellen Gabler (2012-2018)

Cindy Galli (2019-present)

\*Manny Garcia (2006-2014)

Lisa Getter (1996-2000)

\*Matt Goldberg (2013-2019)

Marion Goldin (1984-1986)

Mark Greenblatt (2022-present)

Robert W. Greene (1978-1980) (dec)

Mike Grim (1984-1988)

\*James Grimaldi (2001-2009)

Jason Grotto (2008-2009)

Andy Hall (2002-2006)

\*Mary Hargrove (1983-1991)

Chris Heinbaugh (2001-2003)

Josh Hinkle (2021-present)

Kate Howard (2022-present)

Dianna Hunt (2003-2008)

\*David Cay Johnston (2009-2015)

Harry Jones (1979-1981)

Joel Kaplan (1996-2002)

Peter Karl (19983-1989)

Mark Katches (2004-2008)

Aaron Kessler (2022-present)

Dick Krantz (1980-1984)

Marisa Kwiatkowski (2020-2022)

Mark Lagerkvist (1999-2001)

Jennifer LaFleur (2018-2022)

Dick Levitan (1978-1979)

\*John Lindsay (1989-1999)

Penny Loeb (1992-1998)

Dick Lyneis (1978-1980)

Mike Masterson (1983-1988)

Mike McGraw (1994-2000) (dec)

\*Shawn McIntosh (1994-2006)

Josh Meyer (2011-2017)

\*Mark Middlebrook (1987-1993)

\*Judy Miller (1991-2001)

Stephen C. Miller (1998-2010)

T. Christian Miller (2013-2019)

Clark Mollenhoff (1978-1983) (dec)

\*James Neff (1991-1999, 2000-2002)

Mary Neiswender (1978-1984)

\*Deborah Nelson (1989-1997)

Margie Nichols (1988-1992)

Lise Olsen (2007-2011)

Jacquee Petchel (1994-1998)

\*Cheryl Phillips (2001-2011)

Aron Pilhofer (2010-2012)

Duane Pohlman (2001-2007)

\*James Polk (1978-1982)

Charles Postell (1982-1983)

\*Myrta Pulliam (1978-1991)

\*Tom Renner (1981-1987) (dec)

Steven Rich (2015-2021)

Jill Riepenhoff (2014-2020)

\*Joe Rigert (1982-1990)

Mark Rochester (2001-2003, 2020-2022)

Barbara Rodriguez (2021-present)

Brian M. Rosenthal (2019-present)

Hank Phillippi Ryan (1992-1994)

Neena Satija (2021-present)

Norberto Santana Jr. (2018-2020)

Andrew Schneider (1989-1990) (dec)

Bruce Selcraig (1980-1983)

Don Shelby (1983-1986)

Jay Shelledy (1978-1981)

Deborah Sherman (2003-2006)

Katrease Stafford (2020-2022)

Nancy Stancill (2003-2007)

Laura Sessions Stepp (1986-1990)

Pat Stith (1992-1994)

Drew Sullivan (1999-2001)

Olive Talley (1990-1994)

Jack H. Taylor Jr. (1980-1982)

Charlie Thompson (1985-1989)

\*Cheryl W. Thompson (2015-2021)

Lea Thompson (2006-2013)

Marilyn Thompson (2007-2009)

Lam Thuy Vo (2022-present)

Mc Nelly Torres (2008-2014)

\*Fredric Tulsky (1985-1993)

Norm Udevitz (1978-1980, 1982-1983)

\*Jerry Uhrhammer (1978-1985) (dec)

Jodi Upton (2018-2022)

Nicole Vap (2014-2020)

Matt Waite (2011-2013)

\*Mark Walker (2020-present)

Laura Washington (1993-1997)

Stuart Watson (2000-2004, 2012-2014)

Simone Weichselbaum (2022-present)

Lawan Williams (2008-2010)

Phil Williams (2008-2012, 2014-2016)

Duff Wilson (2006-2010)

Chrys Wu (2014-2016)

\*Alison Young (2007-2013)

Lee Zurik (2016-2020)

::::::::::::::: ct-section-inner-wrap
![Investigative Reporters & Editors](https://www.ire.org/wp-content/uploads/2020/01/StackedLogo_Ink.png)

Membership

[Join](https://www.ire.org/join-ire/)[Renew](https://www.ire.org/member-dashboard/?action=subscriptions)[Benefits](https://www.ire.org/join-ire/member-benefits/)

Quick Links

[News](https://www.ire.org/news/)[Events](https://www.ire.org/training/)[Resources](https://www.ire.org/resources/)[Awards](https://www.ire.org/awards/)[Fellowships & Scholarships](https://www.ire.org/training/fellowships-and-scholarships/)

Job Center\

[Find a Job](https://www.ire.org/find-a-job/)[Post a Job](https://www.ire.org/post-a-job/)

Our Organization

[About](https://www.ire.org/about-ire/)[Board of Directors](https://www.ire.org/about-ire/board-of-directors/)[Staff](https://www.ire.org/about-ire/ire-staff/)[Shop](https://www.ire.org/resources/shop/)[Pay an Invoice](https://irenicar.wufoo.com/forms/ire-online-invoice-payment/)

Get Involved\

[Donate](https://www.ire.org/donate/)[Advertise](https://www.ire.org/advertise-with-ire/)[Contact](https://www.ire.org/contact/)

[![](data:image/svg+xml;base64,PHN2Zz48dGl0bGU+VmlzaXQgb3VyIEZhY2Vib29rPC90aXRsZT48dXNlIHhsaW5rOmhyZWY9IiNveHktc29jaWFsLWljb25zLWljb24tZmFjZWJvb2stYmxhbmsiIC8+PC9zdmc+)](https://www.facebook.com/IRE.NICAR/)[![](data:image/svg+xml;base64,PHN2Zz48dGl0bGU+VmlzaXQgb3VyIEluc3RhZ3JhbTwvdGl0bGU+PHVzZSB4bGluazpocmVmPSIjb3h5LXNvY2lhbC1pY29ucy1pY29uLWluc3RhZ3JhbS1ibGFuayIgLz48L3N2Zz4=)](https://www.instagram.com/ire_nicar/)[![](data:image/svg+xml;base64,PHN2Zz48dGl0bGU+VmlzaXQgb3VyIFR3aXR0ZXI8L3RpdGxlPjx1c2UgeGxpbms6aHJlZj0iI294eS1zb2NpYWwtaWNvbnMtaWNvbi10d2l0dGVyLWJsYW5rIiAvPjwvc3ZnPg==)](https://twitter.com/IRE_NICAR)[![](data:image/svg+xml;base64,PHN2Zz48dGl0bGU+VmlzaXQgb3VyIExpbmtlZEluPC90aXRsZT48dXNlIHhsaW5rOmhyZWY9IiNveHktc29jaWFsLWljb25zLWljb24tbGlua2VkaW4tYmxhbmsiIC8+PC9zdmc+)](https://www.linkedin.com/company/investigative-reporters-and-editors/)

109 Lee Hills Hall, [Missouri School of Journalism](https://journalism.missouri.edu/)   \|   221 S. Eighth St., Columbia, MO 65201   \|   [573-882-2042](tel:573-882-2042)   \|   <info@ire.org>   \|   [Privacy Policy](https://www.ire.org/privacy-policy/)\


::: pswp__bg

:::::::::::::::::: pswp__scroll-wrap
:::::: pswp__container
::: pswp__item

::: pswp__item

::: pswp__item

:::::::: pswp__top-bar
::: pswp__counter

:::::: pswp__preloader
::::: pswp__preloader__icn
:::: pswp__preloader__cut
::: pswp__preloader__donut

::: pswp__share-tooltip

:::: pswp__caption
::: pswp__caption__center


::: cpops-drawer-notices-wrapper

:::::::::::: cpops-panel
::::: cpops-drawer-header
:::: cpops-drawer-header__heading
::: cpops-drawer-header__title
My cart


:::: cpops-drawer-cart
::: cpops-empty-cart
Your cart is empty.

Looks like you haven\'t made a choice yet.

:::::: cpops-drawer-footer
::::: cpops-cart-total
::: cpops-cart-line-items

::: wc-proceed-to-checkout
[Your cart is empty. Shop now](https://www.ire.org/shop/)

`<style type="text/css" id="ct_code_block_css_52">.oxy-menu-dropdown:hover .oxy-drop-menu {
    display: flex;
    flex-direction: column;
    opacity: 1;
}</style>`{=html}


## Cabinet Secretary

Font Size: A A A


- [](#)

  # Find a Form 

  :::::::::::::::::::::::: {}
  ***Please note:*** Internet Explorer is the recommended browser for state e-forms. [Learn more, including special instructions for Microsoft Edge users.](https://www.state.sd.us/eforms/secure/eforms/Instructions%20for%20using%20fillable%20Eforms.pdf){style="color: #fff;" target="_blank"}\
  \

  :::::::::: navcolumn
  ::: letter
  A
  - [Abstracter Licensing](/abstracters/forms.aspx)
  - [Accountancy Licensing](/accountancy/forms.aspx)
  - [Application (general) template for businesses](/localoffices/documents/general_application.docx){target="_blank"} (Microsoft Word format)
  - [Appraiser Certification](/appraisers/forms.aspx)
  - [Appraisal Management Company Registration](/appraisers/information_for_amcs.aspx)
  - [Architect Registration](/btp/architects.aspx#forms)
  - [Athletic Competition](/athleticcommission/forms.aspx)
  :::

  ::: letter
  B
  - [Banking](/banking/forms.aspx)
  - [Barbers and Barber Shops](/barber/forms.aspx)
  :::

  ::: letter
  C
  - [Chartered Bank](/banking/banks/forms_filings.aspx)
  - [Claim of Unpaid Wages](/employment_laws/forms.aspx)
  - [Consumer Complaints](/complaints.aspx)
  - [Cosmetology Licensing](/cosmetology/forms.aspx)
  :::

  ::: letter
  D
  - [Discrimination Complaints](/human_rights/forms.aspx)
  :::

  ::: letter
  E
  - [Electrical Licensing](/electrical/forms.aspx)
  - [Employment Application](/localoffices/job_search_tools/learn_basics.aspx#applications)
  - [Engineer Registration](/btp/forms_applications.aspx)
  :::

  ::: letter
  G
  - [General application template for businesses](/localoffices/documents/general_application.docx){target="_blank"} (Microsoft Word format)
  - [General Education Development (GED)®](/workforce_services/individuals/high_school_equivalency/default.aspx)
  :::

  ::: letter
  H
  - [Human Rights](/human_rights/forms.aspx)
  :::
  ::::::::::

  :::::::: navcolumn
  ::: letter
  I
  - [Independent Contractor Verification Application](https://sdeforms.na2.adobesign.com/public/esignWidget?wid=CBFCIBAA3AAABLblqZhCRdcqBMy4W3CJZ_oKWOPnsGEYlOqFjXvUzyMvpJZbLxHfWbIb3CJwiArasDQv2N6M*){target="_blank"}
  - [Trucking Company Vertification Application](https://sdeforms.na2.adobesign.com/public/esignWidget?wid=CBFCIBAA3AAABLblqZhAkyqlA3eT-go_I9FSBdRlkqiEhKvSOwRJuYkNnAY4KqLpQmidP1iTt8dcd2tZFrSc*){target="_blank"}
  - [Insurance Company Filings and Forms](/insurance/companies/filings_forms.aspx)
  - [Insurance Producer](/insurance/producers/forms.aspx)
  :::

  ::: letter
  J
  - [Job Orders (for employer seeking applicants)](/localoffices/services_businesses/recruitment_hiring/recruitment.aspx#online)
  :::

  ::: letter
  L
  - [Labor Market Information Center publications](/lmic/ordering_publications.aspx)
  - [Landscape Architect Registration](https://apps.sd.gov/LD17BTP/login.aspx){target="_blank"}
  - [Land Surveyor Registration](https://apps.sd.gov/LD17BTP/login.aspx){target="_blank"}
  :::

  ::: letter
  M
  - [Money Lender](/banking/money_lenders/default.aspx#forms)
  - [Money Transmitter](/banking/money_transmitters/default.aspx#forms)
  - [Mortgage Broker](/banking/mortgage_licenses/default.aspx#forms)
  - [Mortgage Lender](/banking/mortgage_licenses/mortgage_lender_license_information.aspx)
  - [Mortgage Transmitter](/banking/mortgage_licenses/default.aspx#forms)
  :::

  ::: letter
  N
  - [Nail Salon Licensing](/cosmetology/forms.aspx)
  - [New Hire Reporting](/ra/new_hire_reporting/forms.aspx)
  :::
  ::::::::

  ::::::::: navcolumn
  ::: letter
  P
  - [Petition for Decertification (for public employees)](https://sdeforms.na2.adobesign.com/public/esignWidget?wid=CBFCIBAA3AAABLblqZhAPs9Hotv4OU7trecLQnWcoeIKyjKNEh7wF-Xl0HB41fyqYZmury4tVYjvHYWmdTTQ*){target="_blank"}
  - [Petition for Election (for public employees)](https://sdeforms.na2.adobesign.com/public/esignWidget?wid=CBFCIBAA3AAABLblqZhCuAbWaHm_orF_k8f4nLwhCuXn22dXGjjAobCh9NTkBRj5_zBmILY9OkZ4YjbNyn6I*){target="_blank"}
  - [Petition for Hearing on Grievance (for public employees)](https://sdeforms.na2.documents.adobe.com/public/esignWidget?wid=CBFCIBAA3AAABLblqZhDeHtrBGMHhRGFt_Bqrs9QJVH9gj4iJdnDuSxL71tp6eEK9yLhS7GR3HMv3N96bQJI*){target="_blank"}
  - [Petition for Hearing on Unfair Labor Practice (for public employees)](https://sdeforms.na2.adobesign.com/public/esignWidget?wid=CBFCIBAA3AAABLblqZhATflFFf75nzQJ6KCjHtdRcrrC3RSiRuk18308HH6VotF9NvAMlX18upbs7_uMlVvs*){target="_blank"}
  - [Petition for Unit Determination (for public employees)](https://sdeforms.na2.adobesign.com/public/esignWidget?wid=CBFCIBAA3AAABLblqZhCanh3H2xcBjwez3qP4MPtyZX7i7jvUdxmij-K7evhW_riKGFCsX-g1UetVeC31daU*f){target="_blank"}
  - [Petroleum Release Service Registration](https://apps.sd.gov/LD17BTP/login.aspx)
  - [Plumbing Licensing](/plumbing/forms.aspx)
  - [Public Employee Labor Issues](/employment_laws/public_employment.aspx#forms)
  :::

  ::: letter
  R
  - [Real Estate (forms used in the business)](/realestate/real_estate_transaction_forms.aspx)
  - [Real Estate Licensing](/realestate/applications_for_licensing.aspx)
  - [Reemployment Assistance Benefits (formerly Unemployment Insurance Benefits)](/ra/forms.aspx#benefits)
  - [Reemployment Assistance Tax (formerly Unemployment Insurance Tax)](/ra/forms.aspx#tax)
  - [Request for Conciliation (for public employees)](https://sdeforms.na2.adobesign.com/public/esignWidget?wid=CBFCIBAA3AAABLblqZhB_rpigA_aemgLBx2TDbuhQ42b-2OcpP7GYLR6mVZSgkKS99--OAX0fqcTGEiIButE*){target="_blank"}
  - [Request for Fact Finding (for public employees)](https://sdeforms.na2.adobesign.com/public/esignWidget?wid=CBFCIBAA3AAABLblqZhDLFqdUTjgKSVERk0vfxHJ75XTZ3ecDDbZaf0DWnql2olyeUBM9Hn4flwihebCyghE*){target="_blank"}
  :::

  ::: letter
  S
  - [Securities](/securities/forms.aspx)
  :::

  ::: letter
  T
  - [Trust Company](/banking/trusts/default.aspx#forms)
  :::

  ::: letter
  U
  - [Unemployment Insurance Benefits-See Reemployment Assistance Benefits](/ra/forms.aspx#benefits)
  - [Unemployment Insurance Tax - See Reemployment Assistance Tax](/ra/forms.aspx#tax)
  :::

  ::: letter
  W
  - [Wage and Hour Issues](/employment_laws/forms.aspx)
  - [Workers\' Compensation](/workers_compensation/forms.aspx)
  - [Workforce Development Council](/workforce_services/wdc/default.aspx)
  :::
  :::::::::
  ::::::::::::::::::::::::

- [](#)

  # Login for Online Services

  ::::::::::::::::::: {}
  ::::::::::: navcolumn
  ::: letter
  A
  - [Appraiser Certification Program Online Renewal](https://apps.sd.gov/lb511/Login.aspx){target="_blank"}
  :::

  ::: letter
  :::

  ::: letter
  B
  - [Broker (Financial) Check](http://brokercheck.finra.org/){target="_blank"}
  :::

  ::: letter
  :::

  ::: letter
  F
  - [First Report of Injury](https://apps.sd.gov/ld66froinet/webform_registerlogin.aspx){target="_blank"}
  :::

  ::: letter
  I
  - [Investment Advisor Search](https://adviserinfo.sec.gov/IAPD/Default.aspx){target="_blank"}
  - [Insurance License Inquiry Services](https://www.sircon.com/ComplianceExpress/Inquiry/consumerInquiry.do?nonSscrb=Y){target="_blank"}
  :::

  ::: letter
  J
  - [Job Search on SDWORKS](https://www.southdakotaworks.org){target="_blank"}
  :::

  ::: letter
  N
  - [New Hire Reporting](https://apps.sd.gov/ld94empuimenu/default.aspx){target="_blank"}
  :::
  :::::::::::

  :::::: navcolumn
  ::: letter
  P
  - [Post a Job Opening on SDWORKS](https://www.southdakotaworks.org){target="_blank"}
  :::

  ::: letter
  R
  - [Real Estate Online License Renewal](https://sdrec.sd.gov/registration/login.aspx){target="_blank"}
  - [Reemployment Assistance Benefits Portal](https://www.sd.gov/rabenefits){target="_blank"}
  - [Reemployment Assistance - File a Claim](/ra/individuals/default.aspx)
  - [Reemployment Assistance - Make a Payment (Overpayments)](/ra/overpayments/collections.aspx#repayment)
  - [Reemployment Assistance - Request Weekly Payment](/ra/individuals/file_weekly_request_for_payment.aspx)
  - [Reemployment Assistance Tax Business Registration](https://apps.sd.gov/ld94empuimenu/default.aspx){target="_blank"}
  - [Reemployment Assistance Quarterly Report for Businesses](https://apps.sd.gov/ld94empuimenu/default.aspx){target="_blank"}
  :::

  ::: letter
  :::
  ::::::

  ::::: navcolumn
  ::: letter
  U
  :::

  ::: letter
  W
  - [Workers' Compensation Coverage Verification](https://www.ewccv.com/cvs/?ref=https://dlr.sd.gov/){target="_blank"}
  :::
  :::::
  :::::::::::::::::::

- [](#)

  # Learn About Programs

  ::::::::::::::::::::::::::::: {}
  ::::::::: navcolumn
  ::: letter
  :::

  ::: letter
  A
  - [Abstracters' Board of Examiners](/abstracters/default.aspx)
  - [Adult Education and Literacy](/workforce_services/individuals/adult_education.aspx)
  - [Affordable Connectivity Program (ACP)](/workforce_services/digital-opportunity/acp.aspx)
  - [Appraiser Certification](/appraisers/default.aspx)
  - [Appraisal Management Companies](/appraisers/information_for_amcs.aspx)
  - [Apprenticeship](/workforce_services/individuals/training_opportunities/apprenticeship.aspx)
  - [Athletic Commission](/athleticcommission/default.aspx)
  :::

  ::: letter
  B
  - [Banking Commission](/banking/commission.aspx)
  - [Banking Regulation](/banking/default.aspx)
  - [Board of Accountancy](/accountancy/default.aspx)
  - [Board of Barber Examiners](/barber/default.aspx)
  - [Board of Technical Professions](/btp/default.aspx)
  - [Boards and Commissions](/boards_commissions_councils.aspx)
  - [Bring Your A Game Training](/workforce_services/individuals/training_opportunities/soft_skills_training.aspx)
  - [Broker-Dealer Licensing](/securities/broker_dealer_licensing.aspx)
  - [Build Dakota Scholarships](https://www.builddakotascholarships.com/){target="_blank"}
  - [Business Opportunity Registration](/securities/business_opportunity_registration.aspx)
  :::

  ::: letter
  C
  - [Career Exploration and Planning](/workforce_services/individuals/career_exploration.aspx)
  - [Cosmetology Commission](/cosmetology/default.aspx)
  :::

  ::: letter
  D
  - [Dakota Roots](https://www.dakotaroots.com/){target="_blank"}
  - [Digital Opportunity](/workforce_services/digital-opportunity/default.aspx)
  - [Division of Banking](/banking/default.aspx)
  - [Division of Insurance](/insurance/default.aspx)
  - [Division of Labor and Management](/employment_laws/default.aspx)
  - [Division of Securities](/securities/default.aspx)
  - [Division of Reemployment Assistance (formerly Division of Unemployment Insurance)](/ra/default.aspx)
  :::

  ::: letter
  E
  - [Electrical Commission](/electrical/default.aspx)
  - [Employer Connection newsletter](/workforce_services/businesses/employer_connection.aspx)
  - [Employer Services](/workforce_services/businesses/default.aspx)
  - [English as a Second Language](/workforce_services/individuals/adult_education.aspx)
  - [Equal Opportunity to Services](/equal_opportunity/default.aspx)
  :::
  :::::::::

  ::::::::::::: navcolumn
  ::: letter
  F
  - [Federal Bonding Program](/workforce_services/federal-bonding/default.aspx)
  - [Federal Health Insurance Marketplace](https://www.healthcare.gov/){target="_blank"}
  - [Financial Institution License Verification](/banking/banks/information_for_consumers.aspx)
  - [Foreign Labor Certification](/workforce_services/foreign_labor/default.aspx)
  - [Franchise Registration](/securities/franchise_registration.aspx)
  :::

  ::: letter
  G
  - [General Educational Development (GED) ®](/workforce_services/individuals/high_school_equivalency/default.aspx)
  :::

  ::: letter
  H
  - [Healthcare Reform](/insurance/healthcare_reform.aspx)
  - [Health Insurance Companies Marketing in South Dakota](/insurance/company_listings/list_of_licensed_to_sell_in_sd.aspx)
  - [HIRE Vets Medallion Program](/veterans/hire_vets.aspx)
  - [Hot Careers](/lmic/menu_hot_careers.aspx)
  - [Human Rights](/human_rights/default.aspx)
  :::

  ::: letter
  I
  - [Insurance Consumer Information](/insurance/consumers.aspx)
  - [Insurance License Lookup](/insurance/license_inquiry_service.aspx)
  - [Insurance, Workers' Compensation](/insurance/workers_compensation.aspx)
  - [Investment Advisor Licensing](/securities/investment_adviser_licensing.aspx)
  - [Investor Education](/securities/investor_education.aspx)
  :::

  ::: letter
  J
  - [Job Fairs](/localoffices/job_search_tools/learn_basics.aspx#jobfairs)
  - [Job Search Workshops](/workforce_services/individuals/classes-workshops.aspx)
  - [Job Seeker Services](/workforce_services/individuals/default.aspx)
  :::

  ::: letter
  L
  - [Labor Bulletin, South Dakota e-](/lmic/elaborbulletin.aspx)
  - [Labor Disputes](/employment_laws/labor_disputes.aspx)
  - [Labor Laws](/employment_laws/default.aspx)
  - [Labor Market Statistics](/lmic/default.aspx)
  - [Layoff Assistance for Employers](/workforce_services/businesses/layoffs_closures.aspx)
  - [Labor Assistance for Individuals](/workforce_services/individuals/dislocated_individuals.aspx)
  - [Long-term Care Insurance](/insurance/long_term_care.aspx)
  :::

  ::: letter
  M
  - [Minimum Wage](/employment_laws/minimum_wage.aspx)
  - [Money Lender Regulation](/banking/money_lenders/default.aspx)
  - [Money Transmitter Regulation](/banking/money_transmitters/default.aspx)
  - [Mortgage Regulation](/banking/mortgage_licenses/default.aspx)
  - [Mutual Funds Regulation](/securities/default.aspx)
  :::

  ::: letter
  N
  - [National Career Readiness Certificates](/workforce_services/ncrc/default.aspx)
  - [New Hire Reporting](/ra/new_hire_reporting/default.aspx)
  :::

  ::: letter
  O
  - [Older Workers](/workforce_services/individuals/55plus.aspx)
  :::

  ::: letter
  P
  - [Plumbing Commission](/plumbing/commission.aspx)
  - [Plumbing Licensing](/plumbing/licensing.aspx)
  - [Posting Requirements for Employers](/employment_laws/posting_requirements.aspx)
  - [Postsecondary Graduate Outcomes System](/graduate_outcomes/default.aspx)
  :::
  :::::::::::::

  :::::::::: navcolumn
  ::: letter
  R
  - [Real Estate Commission](/realestate/default.aspx)
  - [Real Wage Calculator](https://apps.sd.gov/ge102wagecalculator/Index){target="_blank"}\
  - [Reemployment Assistance (formerly Unemployment Insurance)](/ra/default.aspx)
  - [Reemployment Assistance Advisory Council (formerly Unemployment Insurance Advisory Council)](../ra/advisory_council/default.aspx)
  - [Registered Apprenticeship](/workforce_services/individuals/training_opportunities/apprenticeship.aspx)[](/workforce_services/individuals/training_opportunities/apprenticeship.aspx)
  :::

  ::: letter
  S
  - [SDMyLife](https://www.sdmylife.com/)
  - [SD UpSkill](/workforce_services/individuals/sdupskill/default.aspx)
  - [SDWORKS](https://www.southdakotaworks.org){target="_blank"}
  - [Securities Regulation](/securities/default.aspx)
  - [Senior Community Service Employment Program (SCSEP)](/workforce_services/individuals/scsep/default.aspx)
  - [Sircon Licensing (Insurance)](http://www.sircon.com/resource/layout.jsp?page=southdakotaLps&type=southdakota){target="_blank"}
  - [South Dakota Workforce Initiatives (SDWINS) Publications](/publications/default.aspx){target="_blank"}
  - [StartTodaySD Apprenticeship Program](http://starttodaysd.com){target="_blank"}
  - [Stocks Regulation](/securities/default.aspx)
  - [Supplemental Nutrition Assistance Program (SNAP)](/localoffices/job_search_tools/other_programs.aspx#snap)
  :::

  ::: letter
  T
  - [Task Force on Trust Administration Review and Reform](/banking/trusts/trust_task_force.aspx)
  - [Technical Profession Registration](/btp/default.aspx)
  - [Temporary Assistance for Needy Families (TANF)](/localoffices/job_search_tools/other_programs.aspx#tanf)
  - [Termination from Employment](/employment_laws/termination.aspx)
  - [Training Opportunities](/workforce_services/individuals/training_opportunities/default.aspx)
  :::

  ::: letter
  U
  - [Unemployment Insurance - See Reemployment Assistance](#ra_link)
  - [Unemployment Insurance Advisory Council - See Reemployment Assistance Advisory Council](#raac_link)
  - [Unions](/employment_laws/unions.aspx)
  - [UpSkill](/workforce_services/individuals/sdupskill/default.aspx)
  :::

  ::: letter
  V
  - [Veterans' Services](/veterans/default.aspx)
  :::

  ::: letter
  W
  - [Wage and Hour Inquiries](/employment_laws/wage_hour_issues.aspx)
  - [Work-Based Learning (WBL) Toolkit](/workforce_services/individuals/young_adults/wbl_toolkit.aspx)
  - [Wage estimates for specific occupations](/lmic/menu_occupational_wages.aspx)
  - [Work Opportunity Tax Credit (WOTC)](/workforce_services/wotc/default.aspx)
  - [Worker Adjustment and Retraining Notification Act (WARN)](/workforce_services/businesses/layoffs_closures.aspx#warn)
  - [Workers' Compensation](/workers_compensation/default.aspx)
  - [Workers' Compensation Advisory Council](/workers_compensation/advisory_council.aspx)
  - [Workers' Compensation Insurance](/insurance/workers_compensation.aspx)
  - [Workforce Development Council](/workforce_services/wdc/default.aspx)
  - [Workforce Innovation and Opportunity Act (WIOA)](/workforce_services/wioa/default.aspx)
  - [Workforce Training and Education](/workforce_services/individuals/training_opportunities/default.aspx)
  - [Workkeys](/workforce_services/ncrc/ncrc_workkeys_provider_locations.aspx)
  :::

  ::: letter
  Y
  - [Youth Employment](/employment_laws/youth_employment.aspx)
  :::
  ::::::::::
  :::::::::::::::::::::::::::::

- [](https://www.facebook.com/SouthDakotaDLR/){target="_new" alt="Facebook SDDLR"}
- [](https://www.youtube.com/user/SouthDakotaDLR){target="_new" alt="Youtube SDDLR"}
- [](https://twitter.com/SouthDakotaDLR){target="_new" alt="Twitter DLR"}
- [](https://www.linkedin.com/organization/16238549){target="_new" alt="LinkedIn DLR"}
- [](https://dlr.sd.gov/social_media.aspx){target="_new" alt="All social media channels"}

- [Home to DLR](/default.aspx)
- [Home to Workforce Services for Businesses](/workforce_services/businesses/default.aspx)
- [Employment Laws](/employment_laws/default.aspx)
- [Individuals with Disabilities](/workforce_services/businesses/disability_resources.aspx)
- [Labor Market Information](/lmic/default.aspx)
- [Layoff/Closure Services](/workforce_services/businesses/layoffs_closures.aspx)
- [National Career Readiness Certificate](/workforce_services/ncrc/default.aspx)
- [Providing Apprenticeship Opportunities](../workforce_services/businesses/apprenticeship.aspx)
- [Recruitment & Hiring](/localoffices/services_businesses/recruitment_hiring/default.aspx)
- [Reemployment Assistance](/ra/businesses/default.aspx)
- [Veterans, Hiring](/veterans/business_benefits.aspx)
- [Workforce Training & Education](/workforce_services/businesses/workforce_training.aspx)
- [Find a Local Job Service Office](/localoffices/default.aspx)

# Workforce Services for Businesses



## Worker Adjustment and Retraining Notification Act (WARN)

\

The purpose of the **WARN Act** is to provide notice to workers so alternative employment or necessary training can be obtained on a timely basis. The WARN Act requires employers with at least 100 employees to provide written notice at least 60 days before ordering a plant closing or mass layoff to affected employees. South Dakota does not have any additional requirements beyond what the U.S. Department of Labor requires for a WARN to be issued. For more information regarding the WARN Act please visit the [U.S. Department of Labor\'s website](https://www.doleta.gov/layoff/warn.cfm){target="_blank"} or contact your [job service office](/localoffices/default.aspx).

###  

### WARN Notices received by the state of South Dakota

The actual WARN Notice documents available below through a link of the company name are in Adobe PDF format.

+:------------------------------------------------------------------------------------------------------------------------------------------:+:------------------------:+:--------------------:+:-------------------:+
| **Company**                                                                                                                                | **Location**             | **Date Received**    | **Employees\        |
|                                                                                                                                            |                          |                      | Affected**          |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [Transit Management of Sioux Falls, Inc.](/workforce_services/businesses/warn_notices/transit-management-sioux-falls.pdf){target="_blank"} | Sioux Falls              | 11/08/2023           | 91                  |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [Cygnus Home Services, LLC, dba Yelloh](/workforce_services/businesses/warn_notices/yelloh-rc.pdf){target="_blank"}                        | Rapid City               | 10/31/2023           | 10                  |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [Millenium Print Group](/workforce_services/businesses/warn_notices/millennium-print-group-howard.pdf){target="_blank"}                    | Howard                   | 09/17/2023           | 85                  |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [Tyson Foods](/workforce_services/businesses/warn_notices/tyson-dakota-dunes.pdf){target="_blank"}                                         | Dakota Dunes             | 05/26/2023           | 262                 |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [Banner Engineering](/workforce_services/businesses/warn_notices/banner-huron.pdf){target="_blank"}                                        | Huron                    | 03/08/2023           | 164                 |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [Avantara](/workforce_services/businesses/warn_notices/avantara-armour.pdf){target="_blank"}                                               | Armour                   | 08/08/2022           | 47                  |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [Avantara](/workforce_services/businesses/warn_notices/avantara-ipswich.pdf){target="_blank"}                                              | Ipswich                  | 03/31/2022           | 51                  |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [Aramark -- SDSU](/workforce_services/businesses/warn_notices/aramark-sdsu.pdf){target="_blank"}                                           | Brookings                | 03/17/2022           | 278                 |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [Aramark -- USD](/workforce_services/businesses/warn_notices/aramark-usd.pdf){target="_blank"}                                             | Vermillion               | 03/17/2022           | 233                 |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [LSC Communications LLC](/workforce_services/businesses/warn_notices/lsc-communciations.pdf){target="_blank"}                              | Beresford                | 02/21/2022           | 53                  |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [Molded Fiber Glass](warn_notices/mfg2.pdf){target="_blank"}                                                                               | Aberdeen                 | 06/07/2021           | 300                 |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [Remington Outdoor Company](/workforce_services/businesses/warn_notices/remington_outdoor_co.pdf){target="_blank"}                         | Sturgis                  | 10/07/2020           | 5                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [Sheraton](/workforce_services/businesses/warn_notices/sheraton_sf.pdf){target="_blank"}                                                   | Sioux Falls              | 05/13/2020           | 140                 |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [EROS](/workforce_services/businesses/warn_notices/eros.pdf){target="_blank"}                                                              | Sioux Falls /Garretson   | 04/23/2020           | 400                 |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [Bloomin\' Brands Inc. (Outback Steakhouse)](/workforce_services/businesses/warn_notices/bloomin_brands_outback.pdf){target="_blank"}      | Sioux Falls              | 04/27/2020           | 70                  |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [Visionworks](/workforce_services/businesses/warn_notices/visionworks.pdf){target="_blank"}                                                | Sioux Falls              | 04/04/2020           | 8                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [PBM Packaging Inc. (RR Donnelley)](/workforce_services/businesses/warn_notices/pbm_packaging.pdf){target="_blank"}                        | Howard                   | 03/04/2020           | 56                  |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [Littlelfuse Inc.](/workforce_services/businesses/warn_notices/littelfuse.pdf){target="_blank"}                                            | Rapid City               | 02/25/2020           | 125                 |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [MetaBank](/workforce_services/businesses/warn_notices/metabank.pdf){target="_blank"}                                                      | Brookings, Sioux Falls   | 11/20/2019           | 74                  |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [Covington Care and Rehabilitation Center](/workforce_services/businesses/warn_notices/covington_care_rehab_ctr.pdf){target="_blank"}      | Sioux Falls              | 05/31/2019           | 90                  |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [Mobridge Care and Rehabilitation Center](/workforce_services/businesses/warn_notices/mobridge_care_rehab.pdf){target="_blank"}            | Mobridge                 | 11/28/2018           | 67                  |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [TCF Bank](/workforce_services/businesses/warn_notices/tcf_bank.pdf){target="_blank"}                                                      | Sioux Falls              | 09/05/2018           | 145                 |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [Ditech](warn_notices/ditech.pdf){target="_blank"}                                                                                         | Rapid City               | 08/17/2018           | 39                  |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [Younkers (Bonton)](/workforce_services/businesses/warn_notices/bonton.pdf){target="_blank"}                                               | Sioux Falls              | 06/05/2018           | 158                 |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [Wells Fargo & Co.](/workforce_services/businesses/warn_notices/wells_fargo.pdf){target="_blank"}                                          | Aberdeen                 | 03/27/2018           | 108                 |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [Molded Fiber Glass Companies](/workforce_services/businesses/warn_notices/mfg.pdf){target="_blank"}                                       | Aberdeen                 | 02/15/2018           | 409                 |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [Bimbo Bakeries](/workforce_services/businesses/warn_notices/bimbo_bakeries.pdf){target="_blank"}                                          | Sioux Falls              | 09/08/2017           | 58                  |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [Buhler](warn_notices/buhler.pdf){target="_blank"}                                                                                         | Salem                    | 03/09/2016           | 63                  |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [Nash Finch Company](/workforce_services/businesses/warn_notices/nash_finch.pdf){target="_blank"}                                          | Rapid City               | 02/03/2015           | 49                  |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [Wyndham Hotel Group](/workforce_services/businesses/warn_notices/wyndham_hotel_group.pdf){target="_blank"}                                | Aberdeen                 | 09/09/2015           | 241                 |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [Asurion](/workforce_services/businesses/warn_notices/asurion.pdf){target="_blank"}                                                        | Rapid City               | 11/04/2014           | 227                 |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [Capital One](/workforce_services/businesses/warn_notices/capital_one_services.pdf){target="_blank"}                                       | Sioux Falls              | 06/24/2014           | 750                 |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [Minnesota Rubber & Plastic\                                                                                                               | Watertown                | 11/15/2013           | 171                 |
|   (Quadion LLC)](/workforce_services/businesses/warn_notices/quadion.pdf){target="_blank"}                                                 |                          |                      |                     |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [Raven - Aerostar](warn_notices/raven_aerostar.pdf){target="_blank"}                                                                       | Huron                    | 09/20/2013           | 75                  |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [Sargento](/workforce_services/businesses/warn_notices/sargento.pdf){target="_blank"}                                                      | North Sioux City         | 07/29/2013           | 39                  |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [Communication Services for the Deaf, Inc.](/workforce_services/businesses/warn_notices/csd.pdf){target="_blank"}                          | Sioux Falls              | 04/22/2013           | 43                  |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [Stream Global Services, Inc.](/workforce_services/businesses/warn_notices/stream_global_svcs.pdf){target="_blank"}                        | Vermillion               | 08/22/2012           | 180                 |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [Verifications](/workforce_services/businesses/warn_notices/verifications_abdn_mitchell.pdf){target="_blank"}                              | Aberdeen                 | ::: {align="center"} | 73                  |
|                                                                                                                                            |                          | 05/07/2012           |                     |
|                                                                                                                                            |                          | :::                  |                     |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [Verifications](/workforce_services/businesses/warn_notices/verifications_abdn_mitchell.pdf){target="_blank"}                              | Mitchell                 | ::: {align="center"} | 75                  |
|                                                                                                                                            |                          | 05/07/2012           |                     |
|                                                                                                                                            |                          | :::                  |                     |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [Hostess Brands](/workforce_services/businesses/warn_notices/hostess.pdf){target="_blank"}                                                 | Sioux Falls              | ::: {align="center"} | 10                  |
|                                                                                                                                            |                          | 05/04/2012           |                     |
|                                                                                                                                            |                          | :::                  |                     |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [Wells Fargo](warn_notices/wells_fargo_2012.pdf){target="_blank"}                                                                          | Aberdeen                 | ::: {align="center"} | 66                  |
|                                                                                                                                            |                          | 02/02/2012           |                     |
|                                                                                                                                            |                          | :::                  |                     |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [Bosselman Travel Center](/workforce_services/businesses/warn_notices/bosselman_travel_center.pdf){target="_blank"}                        | Rapid City               | ::: {align="center"} | 30                  |
|                                                                                                                                            |                          | 01/5/2012            |                     |
|                                                                                                                                            |                          | :::                  |                     |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [Rockwell Collins, Inc.](/workforce_services/businesses/warn_notices/rockwell_collins.pdf){target="_blank"}                                | Ellsworth Air Force Base | ::: {align="center"} | 8                   |
|                                                                                                                                            |                          | 10/24/2011           |                     |
|                                                                                                                                            |                          | :::                  |                     |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| [Alamo Group (SMC)](/workforce_services/businesses/warn_notices/alamo_group.pdf){target="_blank"}                                          | Sioux Falls              | ::: {align="center"} | 76                  |
|                                                                                                                                            |                          | 10/20/2011           |                     |
|                                                                                                                                            |                          | :::                  |                     |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| Premier Bankcard                                                                                                                           | Spearfish                | ::: {align="center"} | 335                 |
|                                                                                                                                            |                          | 05/23/2011           |                     |
|                                                                                                                                            |                          | :::                  |                     |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| Communication Services for the Deaf (CSD)                                                                                                  | Sioux Falls              | ::: {align="center"} | 79                  |
|                                                                                                                                            |                          | 03/29/2010           |                     |
|                                                                                                                                            |                          | :::                  |                     |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| Verety LLC                                                                                                                                 | South Dakota             | ::: {align="center"} | 1-5                 |
|                                                                                                                                            |                          | 03/19/2010           |                     |
|                                                                                                                                            |                          | :::                  |                     |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| Terex Load King                                                                                                                            | Elk Point                | ::: {align="center"} | 73                  |
|                                                                                                                                            |                          | 12/03/2009           |                     |
|                                                                                                                                            |                          | :::                  |                     |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| Terex Load King                                                                                                                            | Elk Point                | ::: {align="center"} | 10                  |
|                                                                                                                                            |                          | 08/24/2009           |                     |
|                                                                                                                                            |                          | :::                  |                     |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| Coventry Healthcare Inc.                                                                                                                   | Aberdeen                 | ::: {align="center"} | 73                  |
|                                                                                                                                            |                          | 08/19/2009           |                     |
|                                                                                                                                            |                          | :::                  |                     |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| Wells Fargo                                                                                                                                | Sioux Falls              | ::: {align="center"} | 114                 |
|                                                                                                                                            |                          | 07/30/2009           |                     |
|                                                                                                                                            |                          | :::                  |                     |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| Merillat                                                                                                                                   | Rapid City               | ::: {align="center"} | 158                 |
|                                                                                                                                            |                          | 07/17/2009           |                     |
|                                                                                                                                            |                          | :::                  |                     |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| VeraSun Energy Corporation                                                                                                                 | Sioux Falls              | ::: {align="center"} | ::: {align="right"} |
|                                                                                                                                            |                          | 05/25/2009           | 92                  |
|                                                                                                                                            |                          | :::                  | :::                 |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| Terex Load King                                                                                                                            | Elk Point                | ::: {align="center"} | 63                  |
|                                                                                                                                            |                          | 05/01/2009           |                     |
|                                                                                                                                            |                          | :::                  |                     |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| Hutchinson Technology Inc.                                                                                                                 | Sioux Falls              | ::: {align="center"} | 275                 |
|                                                                                                                                            |                          | 01/08/2009           |                     |
|                                                                                                                                            |                          | :::                  |                     |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| MPC                                                                                                                                        | North Sioux City         | ::: {align="center"} | ::: {align="right"} |
|                                                                                                                                            |                          | 01/02/2009           | 45                  |
|                                                                                                                                            |                          | :::                  | :::                 |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| MPC                                                                                                                                        | North Sioux City         | ::: {align="center"} | 89                  |
|                                                                                                                                            |                          | 11/05/2008           |                     |
|                                                                                                                                            |                          | :::                  |                     |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| Student Financial Loan Corporation\                                                                                                        | Aberdeen                 | ::: {align="center"} | ::: {align="right"} |
|   (SFLC)                                                                                                                                   |                          | 05/20/2008           | 18                  |
|                                                                                                                                            |                          | :::                  | :::                 |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| Qwest                                                                                                                                      | Sioux Falls              | ::: {align="center"} | ::: {align="right"} |
|                                                                                                                                            |                          | 01/24/2008           | 58                  |
|                                                                                                                                            |                          | :::                  | :::                 |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| Ideal Merchandising                                                                                                                        | Apollo Beach, FL         | ::: {align="center"} | ::: {align="right"} |
|                                                                                                                                            |                          | 12/06/2007           | 1                   |
|                                                                                                                                            |                          | :::                  | :::                 |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| Artic Cat                                                                                                                                  | Madison                  | ::: {align="center"} | ::: {align="right"} |
|                                                                                                                                            |                          | 11/12/2007           | 89                  |
|                                                                                                                                            |                          | :::                  | :::                 |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| Gateway                                                                                                                                    | North Sioux City         | ::: {align="center"} | ::: {align="right"} |
|                                                                                                                                            |                          | 10/11/2007           | 60                  |
|                                                                                                                                            |                          | :::                  | :::                 |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| Oak Valley Farms                                                                                                                           | Watertown                | ::: {align="center"} | ::: {align="right"} |
|                                                                                                                                            |                          | 07/30/2007           | 225                 |
|                                                                                                                                            |                          | :::                  | :::                 |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+
| Gillette Dairy                                                                                                                             | Rapid City               | ::: {align="center"} | ::: {align="right"} |
|                                                                                                                                            |                          | 05/16/2007           | 48                  |
|                                                                                                                                            |                          | :::                  | :::                 |
+--------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+----------------------+---------------------+

More information about WARN is available on the [U.S. Department of Labor website](https://doleta.gov/layoff/warn.cfm){target="_blank"}.

123 W. Missouri Ave. - Pierre, SD 57501\
Phone: [605.773.3101](tel:605-773-3101){target="_blank"} - For TTY services, call 711 \| Fax: 605.773.6184

[DLR Home](/) [State Home](https://www.sd.gov/cs){target="_blank"} [Request Public Records](https://www.sd.gov/cs?id=sc_cat_item&sys_id=f7f939eddbd4b150b2fb93d4f39619c0){target="_blank" rel="noreferrer noopener"} [Equal Opportunity](/equal_opportunity/default.aspx) [Accessibility Policy](https://www.sd.gov/cs/kb?id=kb_article_view&sysparm_article=KB0010219&sys_kb_id=2d79968d1b464910145542ecac4bcba0&spa=1){target="_blank"} [Contact Us](/staff_directory.aspx) [Disclaimer](https://www.sd.gov/cs/kb?id=kb_article_view&sysparm_article=KB0010221&sys_kb_id=d9449aa41b8c811062c8a8eae54bcbf2&spa=1){target="_blank"} [Privacy Policy](http://sd.gov/privacy.aspx){target="_blank"}

\
South Dakota Department of Labor & Regulation


## Requirements

To run the code at home, install the following packages:

```R
# install.packages("pak")
pak::pak(c("tidyverse", "chromote"))
```

To run the live web-scraping code you'll also need a copy of [Chrome](https://www.google.com/chrome/) installed on your computer.



## Introductions


###### Getting data off a website

Easy

~~1.~~ ~~Ofcial API~~


On Wednesday


2. Unofficial API


3. Static HTML


4. Dynamic HTML


Hard


1. HTML structure


2. rvest basics


3. Extracting data


4. Bonus content

Pagination, Live HTML, Unofficial APIs, LLMs


### HTML structure


###### HTML is a tree

```
 <!doctype html>
 <html lang="en-US">
 <head>
 <title>Page title</ title>
 <meta ...>
 <script ...></ script>
 ...
 </ head>
 <body>
 ...
 </ body> /
  html>

```

###### The tree is made up of elements

ttps://developer mozilla org/en-US/docs/Glossary/Element


###### The stuff you see on a page comes from the body

```
 <body>
  <h1>Top level heading</ h1>
  <p>A paragraph containing text that is <b>bold</ b> and
  an image:  </ p>
  <ul>
  <li>A bulleted list</ li>
  <li>Bullet two</ li>
  </ ul>
  <table>
  <tr><th>A</ th><th>B</ th></ tr>
  <tr><td>1</ td><td>2</ td></ tr>
  </ table> /
  body>

```

###### Best way to see the tree of a real page is to use DevTools

recommend Chrome for this even if it isn’t your daily driver


###### Or right-click and choose inspect


###### Your turn

[Go to <https://rvest.tidyverse.org/articles/starwars.html>,](https://rvest.tidyverse.org/articles/starwars.html)
open the developer tools, and use the "elements" view to
answer the following questions:


What element contains the film titles?


What element contains the name of the director? What
attributes does this element have?


How many paragraphs does the “crawl” at the start of each
movie have?


Where does the table of contents live relative to the film data?


###### Static vs dynamic

The HTML displayed in the elements pane is usually
generated from a HTML file that you can find in the sources
pane.


Sometimes, however, the HTML is generated **dynamically**
with Javascript. We’ll come back to this later, but I wanted to
illustrate the difference.


[Let’s look at <https://rvest.tidyverse.org/dev/articles/](https://rvest.tidyverse.org/dev/articles/starwars-dynamic.html)
[starwars-dynamic.html>](https://rvest.tidyverse.org/dev/articles/starwars-dynamic.html)


### rvest basics


###### Easiest to get data from HTML if it s already in a table

```
              <table>
              <tr>

```


Header


Row


```
<th>Character</ th>
<th>Role</ th>
<th>Affiliation</ th>
</ tr>
<tr>

```

```
<td>Luke Skywalker</ td>
<td>Jedi Knight</ td>
<td>Rebel Alliance</ td>
</ tr>
<tr>
<td>Darth Vader</ td>
<td>Sith Lord</ td>
<td>Galactic Empire</ td>
</ tr>
</ table>

```


Cell
(d = data)


###### Can read with html_table()

```
 library(rvest)
 html <- minimal_html("<table>
  <tr>
  <th>Character</ th>
  <th>Role</ th>
  <th>Affiliation</ th>
  </ tr>
  <tr>
  <td>Luke Skywalker</ td>
  <td>Jedi Knight</ td>
  <td>Rebel Alliance</ td>
  </ tr> /
  table>")
 html_table(html)

```

###### Let s look at a more realistic example

```
 # I want to get the sound track for Star Wars movie

 url <- "https://en.wikipedia.org/wiki/Star_Wars_(soundtrack)"
 html <- read_html(url)

 html |>
 html_table() |>
 _[5:8]

```

###### Can we do better than asking for tables 5 through 8?

```
 # I want to get the sound track for Star Wars movie

 url <- "https://en.wikipedia.org/wiki/Star_Wars_(soundtrack)"
 html <- read_html(url)

 html |>
 html_table() |>
 _[5:8]

```

###### Your turn

[Open <https://en.wikipedia.org/wiki/Star_Wars_(soundtrack)>](https://en.wikipedia.org/wiki/Star_Wars_(soundtrack))


Using the developer tools, can you find something in the
structure of the HTML that uniquely identifies these tables?


###### We can use html_elements() with CSS selectors

```
 url <- "https://en.wikipedia.org/wiki/Star_Wars_(soundtrack)"
 html <- read_html(url)

 html |>
 html_elements(".tracklist") |>
 html_table()

 # .tracklist means all elements with class tracklist

```

###### CSS selectors

**CSS** = cascading style sheets


Primary purpose is to separate the visual appearance (style)
from its underlying semantics.


Used to say (e.g.) “make this box blue” or “make all links
green”.


It’s a domain specific language for selecting elements in the
HTML tree. We’ll use it to identify the HTML elements that
contain the data we care about.


###### Most important selectors

= all elements with class "brown"
##### • .brown


= single element with id "abc"
##### • #abc


= all paragraphs
##### • p


= all paragraphs with "important" class
##### • p.important


= all bold elements that are descendants of a
##### • p b
paragraph


= all bold elements that are children of a paragraph
##### • p > b


###### Your turn

[Use <https://fukeout.github.io/> to learn and practice the](https://flukeout.github.io/)
most important selectors.


### Extracting data


1. Find the “rows” with html_elements()


2. Find the “columns” with html_element()


3. Extract the data with html_text2() or

html_attr()


4. Make a tibble


5. Clean it up


###### Your turn

[Head back to https://rvest.tidyverse.org/articles/](https://rvest.tidyverse.org/articles/starwars.html)
##### •
[starwars.html](https://rvest.tidyverse.org/articles/starwars.html)


What are the rows? How can you identify them with a css
##### •
selector?


What are the columns? How can you identify them with a
##### •
css selector?


# Solution
```
 starwars.R

```

###### Your turn

[Go to https://quotes.toscrape.com/](https://quotes.toscrape.com/)
##### •


Identify the rows and columns (including the URL to the
##### •
author page), and the selectors that will identify them.


(Challenge: how might store the tags in a list column? Why
##### •
might this be useful? What makes it hard?)


Scrape into a tibble
##### •


# Solution
```
 quotes.R

```

###### There s no difference when there s one match

**html_element()** **html_elements()**


###### There s a big difference when numbers of matches varies

**html_element()** **html_elements()**


###### tml_elements() is always one-to-one

**html_element()** **html_elements()**


###### tml_elements() vs html_element()


|html_elements()|html_element()|
|---|---|
|n -> m|n -> n|
|length(0)|NA|
|Find rows|Find column in each row|


###### Ways to find the selector

1. Directly inspecting the HTML


2. In DevTools, right-click & choose “Copy

selector” (then simplify)


3. SelectorGadget


###### Google for selector gadget

tps://chrome.google.com/webstore/detail/selectorgadget


###### More practice

[Scrape all the books off <http://books.toscrape.com/>](http://books.toscrape.com/)


Make sure to capture the (full) title, the rating, the path to the
cover image and the price.


(Don’t worry about the pagination yet)


### Pagination


# Demo
```
pagination.R

```

### Live HTML


###### Your turn

[<https://www.forbes.com/top-colleges/>](https://www.forbes.com/top-colleges/)


Where does the data live? What defines the rows and the
columns? (Hint: it looks like a table, but it’s not)


What happens if you try to read this data into R?


# Solution
```
forbes-live.R

```

### Unofficial API


###### Unofficial API

Most websites that dynamically generate HTML do so from a
###### •
JSON file.


If you can find that JSON file you can work with it directly,
###### •
making your life much easier.


Find it with network pane in the browser developer tools.
###### •


It’s often obvious, but even when not it’s worth spending 30
###### •
minutes on because it’ll easily save that much time.


(I think this Forbes site is an outlier; most of the time it will be a
###### •
bit easier.)


[Another useful resource is <http://inspectelement.org/apis.html>](http://inspectelement.org/apis.html)
###### •


###### Two useful heuristics to start with

Filter to “Fetch/XHR” + Sort by size (decreasing)
##### •


Use search to find text that you know must be in the data
##### •


###### This gives a giant curl call

```
  curl 'https://www.forbes.com/forbesapi/org/top-colleges/2023/position/true.json?

  limit=1000&fields=organizationName,academics,state,financialAid,rank,medianBaseSalary,campusSetting,studentPopulation,squareImage,uri,description,grade' \

  -X 'GET' \

  -H 'Accept: */*' \

  -H 'Sec-Fetch-Site: same-origin' \

  -H 'Cookie: _ga_DLD85VJ5QY=GS1.1.1706542437.3.1.1706542642.60.0.0; VWO=27.700;

  _ketch_consent_v1_=eyJiZWhhdmlvcmFsX2FkdmVydGlzaW5nIjp7InN0YXR1cyI6ImdyYW50ZWQiLCJjYW5vbmljYWxQdXJwb3NlcyI6WyJiZWhhdmlvcmFsX2FkdmVydGlzaW5nIl19LCJhbmFseXRpY3MiOnsic3RhdHVzIjoiZ3JhbnRlZCIsImNhbm9uaWNhb

  FB1cnBvc2VzIjpbImFuYWx5dGljcyJdfSwiZnVuY3Rpb25hbCI6eyJzdGF0dXMiOiJncmFudGVkIiwiY2Fub25pY2FsUHVycG9zZXMiOlsicHJvZF9lbmhhbmNlbWVudCIsInBlcnNvbmFsaXphdGlvbiJdfSwicmVxdWlyZWQiOnsic3RhdHVzIjoiZ3JhbnRlZCIsI

  mNhbm9uaWNhbFB1cnBvc2VzIjpbImVzc2VudGlhbF9zZXJ2aWNlcyJdfX0%3D;

  _swb_consent_=eyJlbnZpcm9ubWVudENvZGUiOiJwcm9kdWN0aW9uIiwiaWRlbnRpdGllcyI6eyJfZ29vZ2xlQW5hbHl0aWNzQ2xpZW50SUQiOiJHQTEuMi4zNTcxMjI4NjguMTcwNTI1OTE4OCIsInN3Yl93ZWJzaXRlX3NtYXJ0X3RhZyI6IjU3YzY4NDNhLWQ4ZT

  ktNDBjMy05YmMxLThjYWNkZWU3ZDE2OSJ9LCJqdXJpc2RpY3Rpb25Db2RlIjoidXNfZ2VuZXJhbCIsInByb3BlcnR5Q29kZSI6IndlYnNpdGVfc21hcnRfdGFnIiwicHVycG9zZXMiOnsiYW5hbHl0aWNzIjp7ImFsbG93ZWQiOiJ0cnVlIiwibGVnYWxCYXNpc0NvZG

  UiOiJkaXNjbG9zdXJlIn0sImJlaGF2aW9yYWxfYWR2ZXJ0aXNpbmciOnsiYWxsb3dlZCI6InRydWUiLCJsZWdhbEJhc2lzQ29kZSI6ImRpc2Nsb3N1cmUifSwiZnVuY3Rpb25hbCI6eyJhbGxvd2VkIjoidHJ1ZSIsImxlZ2FsQmFzaXNDb2RlIjoiZGlzY2xvc3VyZS

  J9LCJyZXF1aXJlZCI6eyJhbGxvd2VkIjoidHJ1ZSIsImxlZ2FsQmFzaXNDb2RlIjoiZGlzY2xvc3VyZSJ9fSwiY29sbGVjdGVkQXQiOjE3MDY1NDI1ODl9; _fbp=fb.1.1706121217898.164324328; _ga=GA1.2.357122868.1705259188;

  _gcl_au=1.1.1366914331.1705344922; _gid=GA1.2.412386523.1706542438; us_privacy=1---; usprivacy=1---; AWSALB=tnC2CAJGdokK0IsOKzBarRIkeT8r4YS5/

  wR6+n+A2VQX2Gfxa3lgP2KrEv6bGPRZyGIhGFvSCrNCftxLR8EXyMI3eDVjI5kBMLcIv9BthsZsyM9Vp0eTKR5yeR/H; AWSALBCORS=tnC2CAJGdokK0IsOKzBarRIkeT8r4YS5/

  wR6+n+A2VQX2Gfxa3lgP2KrEv6bGPRZyGIhGFvSCrNCftxLR8EXyMI3eDVjI5kBMLcIv9BthsZsyM9Vp0eTKR5yeR/H; BCSessionID=2ae07b14-70be-40b1-9e90-ed5d91b1be4f; ki_r=;

  ki_t=1706121218201%3B1706542438105%3B1706542587089%3B2%3B12; client_id=14d486f22e5f65b3107348cd0ffeaa50923; lux_uid=170654243670875530; AMP_TOKEN=%24NOT_FOUND; _swb=57c6843a
  d8e9-40c3-9bc1-8cacdee7d169; rbzid=CXwv4IPKOa5WMsN9vGfFx/FfHDJXwSL2pHJ/swUFnuvHRpgd1qGWgsSHDvkfxbe6A3W7IDkaJbmIeiPvd/wC7NLDIMS6nZ4N6B7HWA1lvWFqWciQ/+GZ1Bm7YCvrGGhXO59tvv6mZYAXbx6MHiL6+/

  BVKFl8m2Z5gx0M2r0M2j9D/QiW7bH4TR8S/oJmWPQi7TJT5F+3SMGf6SjtfG64f74hLDwf+zEy5y95JETCHlw7Og8eg5QO5AALhKK+rhPV4z7F29XqrM2aGXgKHz//+Q==; rbzsessionid=da3b925ab2cf238acdfa18f6e699045b;

  _ga_HY3LZWHH6W=GS1.1.1705344921.1.1.1705345703.0.0.0; _uetvid=a2f10940b3d711ee8c1881f6a3138e42; amp_9c5697=N1292876525...1hk77ksom.1hk77kvfo.2.2.4; notice_behavior=implied,us; fadve2etidvcnt=2;

  _clck=10sfr1j%7C2%7Cfif%7C0%7C1474; fadve2etid=N1292876525; fadvfpuid=FA77ce891e24882d9a03e9d2bc5bf16cf3; _ga_0Y2Y7WWQP1=GS1.1.1705259187.1.1.1705259215.0.0.0;

  _ga_JFZ3B3QM86=GS1.1.1705259187.1.1.1705259215.0.0.0; cmapi_cookie_privacy=permit 1,2,3; fadvuke2etid=N255829421; blaize_session=d72df655-7d08-4673-bbd3-beadbe316b40;

  blaize_tracking_id=418dd2e2-817f-48c7-9792-e36d6ce05bf9' \

  -H 'Sec-Fetch-Dest: empty' \

  -H 'Accept-Language: en-GB,en-US;q=0.9,en;q=0.8' \

  -H 'Sec-Fetch-Mode: cors' \

  -H 'Host: www.forbes.com' \

  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15' \

  -H 'Referer: https://www.forbes.com/top-colleges/' \

  -H 'Accept-Encoding: gzip, deflate, br' \

```

###### And you can translate to R with httr2::curl_translate()

```
  request("https://www.forbes.com/forbesapi/org/top-colleges/2023/position/true.json") |>

   req_method("GET") |>

   req_url_query(

   limit = "1000",

   fields = "organizationName,academics,state,financialAid,rank,medianBaseSalary,campusSetting,studentPopulation,squareImage,uri,description,grade",

   ) |>

   req_headers(

   Accept = "*/*",

   Cookie = "_ga_DLD85VJ5QY=GS1.1.1706542437.3.1.1706542642.60.0.0; VWO=27.700;

  _ketch_consent_v1_=eyJiZWhhdmlvcmFsX2FkdmVydGlzaW5nIjp7InN0YXR1cyI6ImdyYW50ZWQiLCJjYW5vbmljYWxQdXJwb3NlcyI6WyJiZWhhdmlvcmFsX2FkdmVydGlzaW5nIl19LCJhbmFseXRpY3MiOnsic3RhdHVzIjoiZ3JhbnRlZCIsImNhbm9uaWNhb

  FB1cnBvc2VzIjpbImFuYWx5dGljcyJdfSwiZnVuY3Rpb25hbCI6eyJzdGF0dXMiOiJncmFudGVkIiwiY2Fub25pY2FsUHVycG9zZXMiOlsicHJvZF9lbmhhbmNlbWVudCIsInBlcnNvbmFsaXphdGlvbiJdfSwicmVxdWlyZWQiOnsic3RhdHVzIjoiZ3JhbnRlZCIsI

  mNhbm9uaWNhbFB1cnBvc2VzIjpbImVzc2VudGlhbF9zZXJ2aWNlcyJdfX0%3D;

  _swb_consent_=eyJlbnZpcm9ubWVudENvZGUiOiJwcm9kdWN0aW9uIiwiaWRlbnRpdGllcyI6eyJfZ29vZ2xlQW5hbHl0aWNzQ2xpZW50SUQiOiJHQTEuMi4zNTcxMjI4NjguMTcwNTI1OTE4OCIsInN3Yl93ZWJzaXRlX3NtYXJ0X3RhZyI6IjU3YzY4NDNhLWQ4ZT

  ktNDBjMy05YmMxLThjYWNkZWU3ZDE2OSJ9LCJqdXJpc2RpY3Rpb25Db2RlIjoidXNfZ2VuZXJhbCIsInByb3BlcnR5Q29kZSI6IndlYnNpdGVfc21hcnRfdGFnIiwicHVycG9zZXMiOnsiYW5hbHl0aWNzIjp7ImFsbG93ZWQiOiJ0cnVlIiwibGVnYWxCYXNpc0NvZG

  UiOiJkaXNjbG9zdXJlIn0sImJlaGF2aW9yYWxfYWR2ZXJ0aXNpbmciOnsiYWxsb3dlZCI6InRydWUiLCJsZWdhbEJhc2lzQ29kZSI6ImRpc2Nsb3N1cmUifSwiZnVuY3Rpb25hbCI6eyJhbGxvd2VkIjoidHJ1ZSIsImxlZ2FsQmFzaXNDb2RlIjoiZGlzY2xvc3VyZS

  J9LCJyZXF1aXJlZCI6eyJhbGxvd2VkIjoidHJ1ZSIsImxlZ2FsQmFzaXNDb2RlIjoiZGlzY2xvc3VyZSJ9fSwiY29sbGVjdGVkQXQiOjE3MDY1NDI1ODl9; _fbp=fb.1.1706121217898.164324328; _ga=GA1.2.357122868.1705259188;

  _gcl_au=1.1.1366914331.1705344922; _gid=GA1.2.412386523.1706542438; us_privacy=1---; usprivacy=1---; AWSALB=tnC2CAJGdokK0IsOKzBarRIkeT8r4YS5/

  wR6+n+A2VQX2Gfxa3lgP2KrEv6bGPRZyGIhGFvSCrNCftxLR8EXyMI3eDVjI5kBMLcIv9BthsZsyM9Vp0eTKR5yeR/H; AWSALBCORS=tnC2CAJGdokK0IsOKzBarRIkeT8r4YS5/

  wR6+n+A2VQX2Gfxa3lgP2KrEv6bGPRZyGIhGFvSCrNCftxLR8EXyMI3eDVjI5kBMLcIv9BthsZsyM9Vp0eTKR5yeR/H; BCSessionID=2ae07b14-70be-40b1-9e90-ed5d91b1be4f; ki_r=;

  ki_t=1706121218201%3B1706542438105%3B1706542587089%3B2%3B12; client_id=14d486f22e5f65b3107348cd0ffeaa50923; lux_uid=170654243670875530; AMP_TOKEN=%24NOT_FOUND; _swb=57c6843a
  d8e9-40c3-9bc1-8cacdee7d169; rbzid=CXwv4IPKOa5WMsN9vGfFx/FfHDJXwSL2pHJ/swUFnuvHRpgd1qGWgsSHDvkfxbe6A3W7IDkaJbmIeiPvd/wC7NLDIMS6nZ4N6B7HWA1lvWFqWciQ/+GZ1Bm7YCvrGGhXO59tvv6mZYAXbx6MHiL6+/

  BVKFl8m2Z5gx0M2r0M2j9D/QiW7bH4TR8S/oJmWPQi7TJT5F+3SMGf6SjtfG64f74hLDwf+zEy5y95JETCHlw7Og8eg5QO5AALhKK+rhPV4z7F29XqrM2aGXgKHz//+Q==; rbzsessionid=da3b925ab2cf238acdfa18f6e699045b;

  _ga_HY3LZWHH6W=GS1.1.1705344921.1.1.1705345703.0.0.0; _uetvid=a2f10940b3d711ee8c1881f6a3138e42; amp_9c5697=N1292876525...1hk77ksom.1hk77kvfo.2.2.4; notice_behavior=implied,us; fadve2etidvcnt=2;

  _clck=10sfr1j%7C2%7Cfif%7C0%7C1474; fadve2etid=N1292876525; fadvfpuid=FA77ce891e24882d9a03e9d2bc5bf16cf3; _ga_0Y2Y7WWQP1=GS1.1.1705259187.1.1.1705259215.0.0.0;

  _ga_JFZ3B3QM86=GS1.1.1705259187.1.1.1705259215.0.0.0; cmapi_cookie_privacy=permit 1,2,3; fadvuke2etid=N255829421; blaize_session=d72df655-7d08-4673-bbd3-beadbe316b40;

  blaize_tracking_id=418dd2e2-817f-48c7-9792-e36d6ce05bf9",

   `Accept-Language` = "en-GB,en-US;q=0.9,en;q=0.8",

   Host = "www.forbes.com",

   `User-Agent` = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15",

   `Accept-Encoding` = "gzip, deflate, br",

    )>

```

###### Then simplify to the essentials

```
 url <- "https://www.forbes.com/forbesapi/org/top-colleges/2023/
 position/true.json"

 req <- request(url) |>
 req_url_query(limit = "1000") |>
 req_perform()

```

# Demo
```
forbes-api.R

```

###### f the data is stored as JSON in the HTML

This is a pain, but is fortunately relatively rare.


I have had some luck in the past with using the V8 R package
to run the javascript code and then extract the JSON object
back into R.


### LLMs


###### Houston pollen and mold counts

htt // h t h lth / i / ll ld


###### Prompt

Take the following data and covert it in to a call to
tibble::tribble, like the following two example rows for pollen


thresholds <- tibble(

~category, ~low, ~high, ~value,

"weed", 1, 9, "low",

"weed", 500, Inf, "extremely high"

)


Here's the data ...


## 2024-writing-with-numbers-tipsheet.pdf

**Writing with numbers**
NICAR 2024
MaryJo Webster
[maryjo.webster@startribune.com](mailto:maryjo.webster@startribune.com)
X: @ MaryJoWebster
# tinyurl.com/writing-numbers-nicar24


**Use numbers that readers can comprehend**

- Use rates, ratios, proportions, fractions for really big or really small numbers
–Don’t make them do the math
–Make comparisons easy to grasp

Bad example: “Nearly 37% of Minnesota's public school students are pupils of color,
according to Department of Education data, while 95% of the state's educators are white.”

Better: “Nearly 37% of Minnesota’s public school students are pupils of color compared
to 5% of the state’s educators.”
–Ditch the decimals

  - Each digit (plus the decimal point!) slows down the reader

  - Almost all data is flawed

  - Many of the numbers we use come from surveys

  - Don’t use decimals for something that can’t be divided (i.e. people)

  - Using decimals implies precision we can’t guarantee


**Do you need specific numbers?**
Think about your mission. Are you trying to show a trend or pattern? Do you truly need to
document the exact number? Is it possible the number you have is a rough estimate to begin
with?


Sometimes rounding generously and using “about” or “nearly” or “more than” gets the job done
better than the specific numbers. “Nearly 2,000” is easier to grasp than a more specific one like
1,965.


Use fractions – “about one-quarter” or “nearly two-thirds”


Maybe avoid numbers altogether. Example: “Males who killed favored firearms, while women
and girls chose knives as often as guns. More homicides occurred in Brooklyn than in any other
borough. More happened on Saturday”


**Make sure you are providing context and scale**
–Provide historical context or geographical comparisons or any other comparisons that help
show whether a number is “big” or “small.” Context always matters. Think of unemployment
rates – 6% is a very high rate of unemployment, but the number 6% on its own is considered
tiny. That can be true with a lot of other metrics, too.


example below, the topic is water and the yardsticks are things that hold liquid. We often use
“the length of a football field.” But keep in mind that not everyone is a football fan.
Example: “Only 3% of the world’s water is available for humans to drink.” Here’s the yardstick
they used: “If a large bucket were to represent all the seawater on the planet, and a coffee cup
the amount of freshwater frozen in glaciers, only a teaspoon would remain for us to drink.”


–Sometimes rates are necessary to ensure you are getting the context and scale correct.


**Avoid “number clutter”**
–Numbers slow readers down
–If you give readers one number followed by several more in quick succession, it’s possible the
reader will forget or not absorb that first number or even any of them.
–Pick a “star” number and make sure that one shines
–Question every number – do you really need it? Would this be better suited to a graphic?
–Target sentences or paragraphs where you clustered numbers together. Use rounding and
characterizing to eliminate numbers, move others to a different part of the story, put some in
graphics, etc.
–Try reading your story out loud and see where you find yourself slowing down
–Treat numbers like quotes: would paragraphsing get the point across better? Don’t put too
many quotes together.



## 2024-writing-with-numbers.md

Threads: @mjwebster71
X: @MaryJoWebster
Email: maryjo.webster@startribune.com

Deck:    tinyurl.com/writing-numbers-nicar24
Tipsheet:     tinyurl.com/numbers-tipsheet
Over the years, I’ve seen many reporters– and many editors! – who are nervous or downright afraid when it comes time to deal with numbers in a story, whether that’s from our own data analysis or from a press release or government report. 

As a data journalist, we generate dozens and dozens of numbers for every story we do and it’s really tempting to want to shove as many of them into a story as possible.

I’ve had people tell me they are afraid to change the wording from a press release for fear of screwing something up. 

There’s also a very common tendency to put too many numbers in a story, thinking that some readers might want the percentages, some might want the raw numbers, etc. 

I had one person tell me they felt the need to put all the numbers in a story so that it would be in the archive and could pull them up a year or two later when it comes time to do the same story again. All of these things lead to stories that are difficult to read, possibly to the point that we do our readers a disservice. 

So today’s lesson is going to focus on some best practices for writing – and editing – stories that have numbers in them and these tips will be useful whether that’s a story using data analysis or whether they are including numbers gleaned from reports or press releases. 

Before we begin, though, I have to give a shout out to Sarah Cohen, a long-time and very talented data journalist who was the first person to even open my eyes to this issue and whose book and various presentations over the years are the inspiration for this.

All that data in our data diaries…
 In 2000, only about 5% or fewer students left their home district. Over time, that share has climbed steadily, and in Minneapolis and St. Paul are now at 30%. In the Suburbs and Out state Minnesota the percentages are at about 12%  (as you might expect this percentage gets bigger depending how close the district is to Minneapolis or St. Paul)
25 districts lose more students than they take in; 23 districts take more in than they lose. For most districts we’re talking a few hundred students’ difference, but in Minneapolis we’re talking a difference of 4,500 and in St. Paul a difference of just over 2,000 students. (for comparison, Anoka-Hennepin’s difference is about 650 students; that’s a stark difference considering the three districts are pretty much the same size)

Percentage of St. Paul residents who attend school elsewhere, by race/ethnicity:
  White – 32%  (3,468 students)
  Asian – 28%  (4,539 students)
  Black – 28% (3,736 students)
  Hispanic – 29% (2,016 students)
  American Indian – 30% (176 students)
Brooklyn Center has the largest outflow of students – 40% -- but nearly half (48%) its enrollment is made up of students coming in from elsewhere.
Hopkins, where we’re seeing a lot of racial upheaval, is also fairly balanced, gaining about 200 students more than it loses. (it loses about 26% of its resident students; gains about 24% of its enrollment from elsewhere)
Minnetonka is the big winner – 31% of its enrollment is made up of students from elsewhere and it only loses 3% of its resident students 

As data journalists, we especially need to be careful about how many numbers we’re putting in our stories. Because we typically start with something like this…. A memo or data diary of all the interesting things we found as we spent hours — or days or weeks – poring through our really interesting data. When you’re in the midst of that, it’s really hard to let a lot of that work hit the cutting room floor. But it’s just like reporting. We gather a lot of information and then wade through it to find the most salient bits. 

About 26% of teachers this fall are people of color, according to an analysis of preliminary Department of Education data.
Students of color make up 64% of the 1.1 million K-12 students enrolled in schools in the fall of 2021, the most recent year enrollment data is available.
The analysis found that the teacher representation gap has decreased slightly since 2018, when it was 23% to 62%, a 39-point gap.
Latinos make up the largest share of students of color in the state. There is a 31-point gap between the share of teachers who are Latino at 16% and students at 47%.
The gap has decreased slightly since 2018, when about 14.4% of teachers were Latino,compared with 46% of students, a 31.6-point difference.
The data shows there is a large shortage of Native American teachers.
Of the nearly 60,000 teachers, only 1,156 of them are Native American, or about 2% of all teachers. Native Americans made up 4% of students.
Black teachers make up less than 4% of all teachers, which is below parity with Black students at 6%, the data shows.
Only Asian teachers, at about 3.6% of the total, are at parity with Asian students at 3%.

We don’t want it to end up like this…
If we’re not careful, it’s very easy to end up writing a story like this where it’s a long list of all your findings, peppered with too many numbers that end up leaving the reader confused.

What we’ll work on today:
Using numbers that readers can comprehend
Avoiding number clutter
Characterizing findings & writing without digits
Picking your “star” numbers & ditching the rest
There are a lot of things you can do, though, to avoid that and we’re going to work through a handful of approaches that will be applicable to any story you are writing that involves numbers.

I have an undergraduate degree in computational mathematics, but reading data doesn’t require special expertise in computing or math. 
Instead, it requires careful observation; thoughtful, curious questioning; and creative but also cautious interpretation—in short, it requires the modes of inquiry that lie at the heart of the humanities and social sciences. 
Data are not exclusively the province of computer coders, hackers, and quants. Data belong to a particular time and place, and they carry the imprint of that time and place.
First, let’s address the elephant in the room.  Math.  I hear over and over again from journalists that they are AFRAID to make any changes to numbers that are given to them because they aren’t good at math. I also hear data journalists feel compelled to put every last number in their story for fear that readers won’t believe them. 

I found these paragraphs in this book recently that lay out really nicely what journalists really do with data – “careful observation, thoughtful, curious questioning; and creative but also cautious interpretation”  

Really it’s just the same as being a reporter. 

That last part — “creative but also cautious interpretation”  – is a key piece to effectively using numbers in your stories. 

.005
5,825
Let’s do a couple quick exercises to help illuminate some of the issues we deal with regarding numbers. 

Can you comprehend the number .005? Can you visualize what .005 represents? Does it feel tangible to you? 

How about the number 5?

The number 56?

582?

How about 1 million? Can you visualize this many people in a place? Can you comprehend this much money?


1 billion
1 million
How about 1 billion? 

When you read 1 million and then 1 billion, it doesn’t seem all that different - right?  Just one letter difference.


1 million seconds =  ~11 days


1 billion seconds =  ~31 years
But the reality is that they are VERY  different from each other. It takes about just over 11 days for 1 million seconds to go by. 

But 1 billion seconds takes just over 31 YEARS.

(in case you’re wondering……  One trillion seconds is slightly over 31,688 years.)


As you just experienced,  people generally can’t comprehend numbers that are either too small or too big. 

So what’s too small or too big? Generally too small is anything below 1. Too big is generally anything more than something routine in your life:  When it comes to money this would be something like your mortgage payment or your paycheck or the amount of cash in your wallet.  I think about the value of my house, which is well below 5 million, and I still have a hard time putting my mind around that.  When it comes to quantities of things or people, think about if you were at a group event, at what point would the crowd be too big for you to guess how many people are there? For  me that would probably be somewhere around 50 or 100.  


Read this…
From 2008 through the 2012 and then into the 2016 presidential elections, the actual number of votes and the percentage of votes received by the Democratic candidate declined in Minnesota. 
In 2008 Barack Obama received 1,573,454 votes compared to John McCain’s 1,275,409 – a difference of 298,045. 
In 2012 the gap between Barack Obama and Mitt Romney narrowed to 225,942. 
Then in 2016 it was 44,765 between Hillary Clinton and Donald Trump – a steady narrowing of the gap between the Democratic and Republican candidate.
Let’s take a minute for another exercise. Read this paragraph at the same speed you would if you were reading this in a news story.

<pause for time to read>

Did you feel like you had to read it a second - or even third – time to understand what it was getting across?  Did you feel like you had to slow down while reading?

If you answered yes to either of those questions, then something is wrong with this paragraph. We’re going to come back to this.

Use numbers that readers can comprehend
The most basic thing you can do is to make sure our stories are using numbers that readers can comprehend. And there are a whole bunch of ways to do that.

Use rates, ratios, proportions, fractions
The state spends $16.6 billion per year on health care. 
--OR-- 
Annually, the state spends the equivalent of $3,000 per person on health care.

.07% of kindergarteners had a medical exemption to vaccines. 
--OR-- 
7 out of 10,000 kindergarteners had a medical exemption
As we saw in that first exercise, really small numbers and really big numbers are hard for readers to comprehend. A main way to solve this problem is to use rates, ratios, proportions and other methods of converting small or big numbers to something within that comfort zone. 

Don’t make the readers do the math
In Hastings, which has a population of about 22,100, there were six heroin arrests in 2011, according to a report from the drug task force. That's compared with eight arrests in Burnsville, a city with 60,300 residents. Eagan, a city of 64,200, had seven arrests.
There were nearly 3 arrests per 10,000 people in Hastings, compared to about 1 arrest per 10,000 people in both Burnsville and Eagan, which are each nearly three times the size of Hastings.
A related problem is that sometimes we make the readers do the math, such as in this example. Really this is just trying to say that the city of Hastings, which is smaller than the neighboring cities, has had a disproportionate share of heroin arrests (note: this was at the beginning of the latest opioid epidemic). But what the reporter really should have done is convert those arrests into per capita rates. 

<click to bring in a revised version>

And then you’ll see that there does appear to be a higher rate of arrests in Hastings than the larger cities.

Also note that in my suggested change, I’ve rounded those per capita rates to whole numbers – 3 and 1 . No decimals here. Keep it simple.

Make comparisons easy
Nearly 37% of Minnesota's public school students are pupils of color, according to Department of Education data, while 95% of the state's educators are white.
37% of students are people of color, compared to 5% of educators
Another thing that throws me as a reader is giving numbers that are essentially different sides of the coin. Here where the writer is describing the racial makeup of the students, he’s referring to the share of pupils of color. But then when he talks about the educators, he’s saying what share are white. 

Two problems with this: One is that you’re making the reader do the math to see the gap. Two, we’re not making the gap as visible as it needs to be. A lot of readers will automatically try to compare those two numbers and might be a little flummoxed. 

[advanace]
Something like this would be cleaner.

Ditch the decimals!!
Each digit (plus the decimal point!) slows down the reader
Almost all data is flawed
Many of the numbers we use come from surveys
Don’t use decimals for something that can’t be divided (i.e. people)
Using decimals implies precision we can’t guarantee

Decimals have very, very little place in the news. For starters, they slow the reader down and make it harder for them to comprehend a number.  For example, is 3 is easier to comprehend than 3.4 ???

But more importantly, there are several other reasons we should rarely use decimals. Almost all the data we ever reference in  stories is either flawed in some way or comes from surveys, which are inherently imperfect. There’s also a rule of thumb that we shouldn’t use decimals for something that can’t be divided. What would 3.4 percent of a human look like?  

And finally, it implies a level of precision that we can’t guarantee. We are not the scientists who are conducting precise experiments in a lab. We are not the ones who collected the data in the first place. We KNOW, without a doubt, that we are doing our best to get the most accurate information we can, but that is a big hill to climb. So there’s really no point in making readers think we’ve nailed it perfectly. 

Here’s an example where the decimals are completely uncalled for (this is based on a survey! And it’s about people!). 

A rewrite:  “For the first time in history in 2000, about half of the people in the USA were 35 or older. That age group is growing faster in the suburbs than in the cities….” (leave out the other numbers or relegate them to a graphic)

 “For the first time in history in 2000, about half of the people in the USA were 35 or older. That age group is growing slightly faster in the suburbs than in the cities. At the same time, growing numbers of minorities and immigrants are settling in the suburbs.” 

(leave out the other numbers or relegate them to a graphic)

Round generously & characterize
“Roughly”, “About”, “More than”
Use sentences that visualize a trend: “It rose in the spring, then dipped for several months”


My suggested changes for that last example also show how you can round and characterize numbers. 

We should always be thinking carefully about whether readers truly NEED the very specific numbers. What’s the goal of putting the numbers in the story in the first place? Most of the time we are trying to characterize something that’s happening – how big, how much change, how small, etc. In these situations, readers might only need a rough idea of what we’re talking about. Maybe saying that there were “about 13,000 incidents last year” is sufficient, instead of saying 13,486 or whatever that specific number is. 

This example on the right is from Denied Justice, an investigative project by the Star Tribune. We built our own database from police investigative files on sexual assaults throughout Minnesota. The data is a sampling of the cases – in other words, we knew from the start that our analysis was incomplete. And we also thought long and hard about our goal here – we wanted readers to grasp the scope. These grafs are from the first story in the series. We wanted to give readers the sweeping picture. We wanted them to remember that ALMOST A QUARTER of cases were never assigned to an investigator and “about 75 percent” were never forwarded to prosecutors. The real number behind that 75 percent is something more squishy – like 73.6 percent or something. And also notice the “1 in 10” – instead of using a percentage, we wanted readers to imagine 10 victims lined up in a row and that only 1 got a conviction in their case.

Of course, there will be times we need to put in a specific number, such as the fact that there were 95 homicides in the city last year. Sports and business reporting is where we see the greatest use of decimals, but I would recommend the same rule of thumb in those stories. Do we really need to know the specific batting average? Or do we just need to know that it was a certain amount higher than in years’ past?  (this also goes back to the idea of not making the readers do the math)

“The oldest killer was 88; he murdered his wife. The youngest was 9; she stabbed her friend. The women were more than twice as likely as men to murder a current spouse or lover. But once the romance was over, only the men killed their exes. The deadliest day was July 10, 2004, when eight people died in separate homicides. Five people eliminated a boss; 10 others murdered co-workers. Males who killed favored firearms, while women and girls chose knives as often as guns. More homicides occurred in Brooklyn than in any other borough. More happened on Saturday. And roughly a third are unsolved.”
Here’s another example from the New York Times. This is a lede on a story about murder in the city and is based on a data analysis of homicide data by Jo Craven-McGinty. It’s a very unique way to start a story, but it certainly caught my attention and provides almost a reference guide to the very, very many ways you can characterize data. Behind each of these sentences, there is certainly a specific number – but you don’t see them here.

Context and scale
What would a “good” number look like? What’s the standard or goal?
How does this compare to other places? 
How has this changed over time?
What is this as a portion of the whole?
Another way that numbers become incomprehensible to readers is when you don’t provide the context or the scale necessary to interpret that number. For example, an 8% unemployment rate is considered extremely high. But if someone isn’t familiar with the history of that, how would they know? 8 is a pretty small number, right? 

Let’s go back to my Denied Justice example. When we found out that our data was showing that 1 in 10 sex assault cases result in a conviction, we set out to try to find out if that’s high or low. We assumed it was low, of course. But what could we compare it to? This was a situation where we really couldn’t find a “standard” to measure it against because crime isn’t tracked that way. The police track their side using clearance rates and the courts track their side using conviction rates. But as we found, a ton of cases fall through the cracks between those two things. 

But for other things you should be able to find comparisons that help you show readers if something is too high or too low. There are often organizations that set standards for things – For example, what percentage of revenue can a non-profit reasonably use for administrative expenses?  There are also groups out there that report national or regional averages for all kinds of things. 

Comparing how your city or state fares compared to the national average on something is always a good option. Looking at how something has changed over time is another. For example, if you’re writing about unemployment hitting 8%, perhaps you’d want to include a sentence like “Prior to this, unemployment rates typically hovered around 3%. The last time it reached this level, the country was in the midst of its worst recession in decades.” 

 

Only three percent of the world’s water is available for humans to drink…..most is locked in polar ice caps and glaciers or is embedded in layers of rock.
How much is 3%?
Here’s an example – from a New Yorker article – where scale is really important. How much is 3%. Doesn’t sound like much, does it?

“If a large bucket were to represent all the seawater on the planet, and a coffee cup the amount of freshwater frozen in glaciers, only a teaspoon would remain for us to drink.”
New Yorker, Oct. 23, 2006, page 64

Here’s the sentence that followed. They used a concept known as a “yardstick” to put that 3% in context.. 
Notice how they used items that related to water -- bucket, cup, teaspoon.  The closer you can get to the topic you’re trying to visualize, the easier it will be for the reader. But you also want to make sure it is something that readers can visualize.
We often use things like “3 football fields” to represent the scale of something, but would the average reader really understand that? Especially one who isn’t a football fan?

Taylor Landing:
$1.3 million in funds

Port Arthur:
$4.1 million in funds
Sometimes the context and scale can be a little deceptive and it’s imperative to understand what’s behind those big numbers.

This story is a great example – it’s about federal aid disbursement in the wake of Hurricane Harvey in Texas. The paper got a list of dollar amounts going to each town in the area – such as the two listed here. Taylor Landing, a wealthy, white town and Port Arthur, a poor and primarily Black town.

Some journalists might have stopped there and simply reported the dollar amounts. If so, it would’ve looked like Port Arthur was getting a windfall.


Let’s compare….
Taylor Landing:
Small town, wealthy, white

$1.3 million in funds
22 affected residents
Port Arthur:
Bigger town, poor, primarily black
$4.1 million in funds
50,000 affected residents
But they dug a little deeper and looked at how those dollar amounts were determined. Turns out it’s based on the number of “affected” residents (which has a specific definition). Between these two very different towns, there was also a huge difference in the number of affected residents

Let’s compare….
Taylor Landing:
Small town, wealthy, white

$1.3 million in funds
22 affected residents

$60,000 per affected resident
Port Arthur:
Bigger town, poor, primarily black
$4.1 million in funds
50,000 affected residents

$84 per affected resident
If you do the simple math, you get a different story. The rich, white town was getting the windfall. The black, poor town was getting next to nothing.  The lesson here is making sure you understand how numbers are calculated. Or what goes into determining things like that.  The bottom line is that the reporter needs to truly understand the numbers they are using -- not just regurgitating them.  That requires asking questions and doing simple reporting.

Avoid ‘number clutter’
Up until now, we’ve talked about more specific things related to WHICH numbers to use in a story. But equally important is to look at HOW MANY numbers you’re using. 

I found this paragraph in an op-ed that my newspaper published recently about Minnesota’s massive racial income gap.  They apologized in this sentence for giving readers a “blizzard of numbers”


Here are the couple grafs right above that sentence and you can see that they’ve crammed in quite a few numbers. 

But do we need to give readers a blizzard of numbers?   

We’re going to go through a few more examples to show you various ways to balance which numbers the story truly needs, and various ways to give them to readers without the “blizzard”

Remember this?
From 2008 through the 2012 and then into the 2016 presidential elections, the actual number of votes and the percentage of votes received by the Democratic candidate declined in Minnesota. 
In 2008 Barack Obama received 1,573,454 votes compared to John McCain’s 1,275,409 – a difference of 298,045. 
In 2012 the gap between Barack Obama and Mitt Romney narrowed to 225,942. 
Then in 2016 it was 44,765 between Hillary Clinton and Donald Trump – a steady narrowing of the gap between the Democratic and Republican candidate.
Remember this that we read at the start of this session? 

55 digits!
From 2008 through the 2012 and then into the 2016 presidential elections, the actual number of votes and the percentage of votes received by the Democratic candidate declined in Minnesota. In 2008 Barack Obama received 1,573,454 votes compared to John McCain’s 1,275,409 – a difference of 298,045. In 2012 the gap between Barack Obama and Mitt Romney narrowed to 225,942. Then in 2016 it was 44,765 between Hillary Clinton and Donald Trump – a steady narrowing of the gap between the Democratic and Republican candidate.
This has 55 digits in it!  And yes, the years count as numbers and digits. There are some rules of thumb,  such as a recommendation that you don’t have more than two or three numbers in a paragraph. That’s pretty harsh, though, and hard to pull off sometimes. But if you combine reducing the numbers with some of the other tactics we just talked about – rounding, characterizing, using yardsticks, using rates – things can get more manageable. 

I can find example after example that is similar to this – and we’re going to look at a few others in a minute. But let’s stop and think about WHY do reporters too often put lots and lots of numbers in stories? (And why do editors let it through?)

In talking with reporters and editors in the last two newsrooms I’ve worked in, I’ve heard several interesting things. The main one being that reporters are afraid to change any numbers that were given to them and/or they think the numbers make their story more authoritative. Among data journalists, I think there’s just a tendency to prevent their great work from hitting the cutting room floor. I had one reporter tell me that they wanted specific numbers (not rounded ones) – like the ones in this paragraph – to be in the story because they would probably need to circle back to those numbers a year from now and they want to be able to pull up the archived story to get them.

None of these things are good reasons for putting lots of numbers in stories.

Is this better?
Between the 2008 and 2016 presidential elections, the actual number of votes and the percentage of votes received by the Democratic candidate declined in Minnesota.
 In Barack Obama’s first election, he received about 298,000 more votes than his Republican counterpart. That lead dwindled to about 225,000 in his next election. Hillary Clinton garnered about 45,000 more than Donald Trump.
The main place to start with a number-heavy section like this is to make two assessments:
What is the key point we’re trying to get across?
What numbers are super necessary?

In this example, the main point is actually already written in the first sentence – Democratic candidates in Minnesota have been receiving a smaller and smaller share of the votes with each passing election. 

I don’t know about you, but when I first read the original, it took me probably three readings to figure that out, despite the fact that it was already in the first sentence. My brain lost all of that once the writer took me into that sea of numbers. 

So then the main thing we need to do is use that second sentence to put some numbers in to back up the first statement. Notice here I’ve dropped it down to just the vote DIFFERENCES (dropped the actual vote counts) and I also employed some heavy rounding. 

Visualizations can help too
Since 2008, the actual number of votes and the percentage of votes received by the Democratic candidate for president has declined in Minnesota with each election. Barack Obama had nearly 300,000 more votes than his Republican opponent in his first election, but that dropped slightly in his second election. Hillary Clinton edged out Donald Trump by only about 45,000 votes.
I often have people tell me – oh no, we can’t do that kind of rounding! We need readers to see the exact  numbers so it shows we have the authority to back up what we’re saying!  

Well, how about we put the actual numbers into a graphic?  That solves that problem. (and in this day and age, I think we truly only need to worry about the digital publication, where we usually have plenty of space to add in graphics)

By putting those difference numbers into a graphic, I can reduce the number load in the narrative to just 3 numbers – and one of them is a year. Also notice that they are well spaced out from each other.

Let’s go back to our data memo…
o   In 2000, only about 5% or fewer students left their home district. Over time, that share has climbed steadily, and in Minneapolis and St. Paul are now at 30%. In the Suburbs and Out state Minnesota the percentages are at about 12%  (as you might expect this percentage gets bigger depending how close the district is to Minneapolis or St. Paul)
o   25 districts lose more students than they take in; 23 districts take more in than they lose. For most districts we’re talking a few hundred students’ difference, but in Minneapolis we’re talking a difference of 4,500 and in St. Paul a difference of just over 2,000 students. (for comparison, Anoka-Hennepin’s difference is about 650 students; that’s a stark difference considering the three districts are pretty much the same size)

o   Percentage of St. Paul residents who attend school elsewhere, by race/ethnicity:
  White – 32%  (3,468 students)
  Asian – 28%  (4,539 students)
  Black – 28% (3,736 students)
  Hispanic – 29% (2,016 students)
  American Indian – 30% (176 students)
Brooklyn Center has the largest outflow of students – 40% -- but nearly half (48%) its enrollment is made up of students coming in from elsewhere.
Hopkins, where we’re seeing a lot of racial upheaval, is also fairly balanced, gaining about 200 students more than it loses. (it loses about 26% of its resident students; gains about 24% of its enrollment from elsewhere)
Minnetonka is the big winner – 31% of its enrollment is made up of students from elsewhere and it only loses 3% of its resident students 

As data journalists, we especially need to be careful about how many numbers we’re putting in our stories. Because we typically start with something like this…. A memo or data diary of all the interesting things we found as we spent hours — or days or weeks – poring through our really interesting data. When you’re in the midst of that, it’s really hard to let a lot of that work hit the cutting room floor. But it’s just like reporting. We gather a lot of information and then wade through it to find the most salient bits. 

What is the core thesis or premise?
The number of students defecting from their home school districts has accelerated in the past 10 years and is having huge economic impact, particularly on the state’s two urban districts. 

So the first step after collecting all those findings, is to figure out the core thesis or key thing you are going to say based on your data analysis. Try to write it in a sentence like this that doesn’t use numbers. What is the trend or the key point you are trying to drive home with readers?

Minnesota students have had the right to attend school in other districts since 1990, but the number of elementary and high school students exercising that option is surging. Last year, about 132,000 Minnesota students enrolled in schools outside their home district, four times the number making that choice in 2000, a Star Tribune analysis shows.
Pick a “star”
After that, then figure out your “star” number. What’s the one number you want the reader to remember all the way to the end of the story? 

From that mess of data findings I showed you a minute ago and to back up that core thesis I showed you on the last slide, I chose “four times” as my star number. 

And this is the nut graf from the story we published. 

This huge increase in kids opting for school choice was the main point of the story.  Editors decided we needed to put in the 132,000 number as well, which I think actually steals the thunder from the four times figure, especially because it comes BEFORE the star number. We could have circled back in a subsequent paragraph to say that this is roughly 132,000 students. 

Also notice that we did the math for readers by saying “four times” –  We characterized our key finding without actually using the two numbers used to come up with the 4 times. 

Once you have your star number, then you can start prioritizing the other key numbers and figuring out where they can go in the story and which ones belong in graphics.

Beyond the “star” number…
What contextual numbers are necessary?
What would be best suited for a graphic?
What can be paraphrased or characterized?

Treat numbers like quotes
Would paraphrasing get the point across better?
Do we need to use the exact language?
Don’t want too many quotes together
Need to make sure quotes are put in context

To sum up, really what we’re doing here is treating numbers the same way we treat quotes from humans. Use the same rules of thumb about paraphrasing, not stringing too many quotes together, etc.

Bulletproofing
Fact check the numbers
Use your common sense
Read sentences out loud


Do the usual bulletproofing steps before publishing. Double check all your numbers. Do the math another time.  Use your common sense about how something is worded. Say a sentence out loud to see what it sounds like. (this is a really good test to see if you have too many numbers because you’ll notice yourself slowing down)


This fact-checking is especially important if the story has been edited and rewritten and rearranged multiple times. You run the distinct danger of introducing errors by simply changing the order of things or rewording a sentence or removing the important contextual information. The numbers themselves might still be the same, but you also need to make sure they are being portrayed to readers correctly.


Exercises

According to U.S. Census data from 2018, St. Louis Park has a population of just over 49,000 residents. Of that total, 83% are white, 7.7% are black, 3.8% are Latino, 3.7% are Asian and 3.3% cite two or more races. In Minnesota as a whole, 83.7% are white, 5.9% are black, 4.7% are Asian, 2.8% claim two or more races and 1% are American Indian, according to the most recent American Community Survey.
Nearly 20% of St. Louis Park’s 49,000 residents are non-white, which is slightly higher than the state as a whole. Blacks make up nearly 8%, while Asians, Latinos and people who identify as multiracial each make up about 3% of the city’s population.
Here’s an extremely common example – a string of numbers that leave the reader numb. Notice that the decimals are also making it exponentially harder to read. 

What’s the key point this is trying to get across?  Mainly that the city of St. Louis Park’s racial diversity is pretty similar to the state as a whole, and then a secondary point perhaps is that Blacks make up the largest minority group. 

<click to bring in revision>

Also note that the percentages for Asians, Latino and multiracial are all so close together – all hovering around 3% – that it’s perfectly fine to lump them together like this, which significantly reduces the number load.

This is also a good example where a graphic would allow you to share the specific numbers without bogging down the story.

https://www.startribune.com/with-kia-and-hyundai-thefts-still-soaring-minneapolis-city-council-calls-for-recall/600345252/

The approach, already used in cities like Madison, Wis., and Houston, has shown promising early results, she said. 
The unit made 326 contacts with people suffering from some degree of mental illness — 277 adults and 49 juveniles — between September and April. 
Of those, 149 people remained in their homes, 96 were taken to a hospital and 81 were gone before police arrived. 
None was taken to jail, according to Waite. Department statistics show that the number of such calls has jumped from 2,300 in 2011 to 6,499 last year, an increase of more than 182 percent. So far this year, police have fielded 3,150 EDP calls, the statistics show.
What’s the star? What do we truly need to keep? What could go in a graphic?

In the mid-1990s, Maine’s lawmakers and health officials made a pivotal decision to reduce the state’s reliance on nursing homes, a move intended to redirect  elderly residents toward “more homelike, less institutional” alternatives.

The policy change, enacted in 1993 amid a severe budget crunch, helped spark a dramatic transformation of the elder care system in Maine, where 21.7% of the population is 65 or older — the highest percentage in the country.

Between 1996 and 2022, the number of nursing home beds dropped by nearly 3,680, from a high of more than 10,000, sparing Maine the financial burden of subsidizing them. During the same period, the number of beds at what are known as residential care facilities almost doubled, jumping by more than 4,200. As a result, older Mainers and other residents with significant medical needs live in these homes. Residential care facilities in Maine resemble what are known generally as assisted living facilities.


https://themainemonitor.org/maine-residential-care-system-fails-ailing-seniors/


Over the past two generations, people have spent less and less time in marriage—they are marrying later, if at all, and divorcing more. 
In 1950, 27 percent of marriages ended in divorce; today, about 45 percent do. In 1960, 72 percent of American adults were married. In 2017, nearly half of American adults were single. 
According to a 2014 report from the Urban Institute, roughly 90 percent of Baby Boomer women and 80 percent of Gen X women married by age 40, while only about 70 percent of late-Millennial women were expected to do so—the lowest rate in U.S. history.
And while more than four-fifths of American adults in a 2019 Pew Research Center survey said that getting married is not essential to living a fulfilling life, it’s not just the institution of marriage they’re eschewing: In 2004, 33 percent of Americans ages 18 to 34 were living without a romantic partner, according to the General Social Survey; by 2018, that number was up to 51 percent.
https://www.theatlantic.com/magazine/archive/2020/03/the-nuclear-family-was-a-mistake/605536/?fbclid=IwAR2h7pxLC7KxwLvfn32zUHmWRFpBvOPC9EJoHmOjycRJeq2Q4gZm870GCx0
Where are we making readers do the math?
How can we characterize some of these sentences?
What should go into a graphic?


Questions?
