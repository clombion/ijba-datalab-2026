<!-- chunk: 2/2 | source: 11-data-literacy.md | words: 24800 -->
<!-- headings: `|`; `Un` -->
<!-- sections: Data cleaning with OpenRefine and PDF extraction; Summary statistics and number comparisons; Data visualization and charting techniques -->

```
                                                         @
qt 102 » OFalion 4 :

```

```
+ OFalion 2
+ OFALLON (44 rom

```

```
& OF allon

```

```
+ Ofaitan 66 © Length Variance of Choices
+ Gallon (2 rows j
* + Tallon OFALLON 12 1075) © [sours} ] is f

                                               § mn BAP GOOG GOOII01

```

```
6 2075 + Kansas City (15
                  + KAHSAS CITY

```

```
Kansas City

```

```
Select All Deselect All Merge Selected & Re-Cluster Merge Selected & Close Clo

```

```

                wm e o ewneStLOUIS e «

 ssouri Ethics Commission.

l of clustering for variations of St. Louis.

 Merge Selected & Re-Cluster and Refine standardizes all of those St. Louis

ings. We see that we have a whole bunch more for O'Fallon, Kansas City, Lee’s
 and so on. If we were really using this column for analysis or visualization, we'd
go through each of these clusters, then apply all of the other methods and keying
s. Close the clustering box.
 export our cleaned data as an Excel file by picking Export | Excel at the top right.

reates a file in the older (.xls) format that has the same name as our project.
 is just a quick look at how Refine can detect and correct errors. Refine can also split
ge values in columns. It even has its own scripting language called GREL, which
ou to write code for cleaning data.
 Refine by closing your browser window, then close the window with the
d line terminal. If you forget to do the latter, Refine will continue to run in the
und.

TING DATA FROM PDFS

kle one last challenge that you might face while gathering data: converting data
nside PDF files into Excel files. Many government agencies publish data tables
 inside these PDFs. In order to work with the tables, we must first liberate them.

he PDF called fy2012_US_gov_net_cost.pdf. This one-page table, which docuhe net operating costs of federal agencies, was extracted from the larger Financial
of the U.S. Government for Fiscal Year 2012 that was released by the Department
easury. We could try copying and pasting the data into Excel, but that would not
 the column layout. So we'll instead need to use an online converter that will turn

 file into an Excel table. Cometdocs (at www.cometdocs.com) and Zamzar

zamzar.com) are two proven services. Sometimes one does better than the other,
ng on how the PDF is structured. So try both in real-life situations. (Note that
onversions will not work with PDFs that were created by scanning other

```

```
Convert button and pick Excel (xls) from the options list. Enter your email address and
Convert. Now check your email for a message from Cometdocs with the download lin
 Open the Excel file and you'll see Cometdocs did a good job converting the PDF.
only glitch is that some agencies, like Health and Human Services, take up more tha
line. We could clean that manually in the file if we needed to.

  9 (GainV/Loss
 10 from :
  14 Gross Earned Changes in Net
 12 {In billions of dollars) Cost Revenue Subtotal Assumptions Cost
 13 Department of Health and Human
 14 Services 924.0 67.8 856.2 03 8
 15 Social Security Administration . 825.4 03, S25 1i- 8
 16 Department of Defense 784,7 56.0 728.7 70.4 7
 17 Department of Veterans Affairs 213.6 41 209.6 149.3 3
 48 Interest on Treasury Securities Held by
 19 the Public 245.4 - 245.4 - 24
 20 Department of Agriculture 161.0 12.0 149.0 - 1
 21 Office of Personnel Management 48.2 19.1 oe 98.9 1
 22 Department of Labor 407.3 - 107.3 - 1
 23 Department of Transportation 79.0 0.8 78.2 ~
 24 Department of Housing and Urban
 25 Development 74.5 1.5 73.0 - |
 26 Department of Energy 60.8 4.3 56.5  27 Department of Homeland Security §8.2 29 48.3 04
 28 Department of Education 62.7 20.0 427  29 Department of Justice 38.9 43 37.6 
Source: Department of the Treasury.

Note: Data extracted from a PDF into an Excel file by Cometdocs.

 For students and professionals working with data, cleaning is an essential part
process. This chapter showed how you can get started to solve some of the most v
problems with Excel, OpenRefine and online PDF converters.

 Now that we know how to check and clean our data, we can move on to analyzing
discover meaning.

ON YOUR OWN

Use OpenRefine to continue cleaning the campaign contributions data file. Clea
spellings of at least 10 cities. Use all of the algorithms available under clustering. Which
worked the best? Why?

```

```
  a] a &.
= .

```

```
nial

```

```

```

```
 far, we have learned how to identify, obtain, evaluate and clean our data. All of this
 s necessary to get ready for the next step: learning how to analyze our data so we can
make better decisions or become more informed. This chapter introduces concepts
 help us develop best practices for analyzing data. Chapters 9 and 10 will show how
 Excel or other spreadsheet programs to generate meaningful information with
s and pivot tables.

n we work with data, we often generate what are called summary statistics. Some
es are counts, sums and averages. These numbers are used to take snapshots or
 descriptions of our data. We can generate these easily and they will tell us much
our data.

 book does not cover how to generate inferential statistics, which are used by
hers who have obtained data from a sample and want to use it to draw conclusions
the overall population. For example, researchers would use inferential statistics to
 the outcome ofa presidential election based on the responses of 1,000 likely voters.

overview of inferential statistics, you can read Seeing Through Statistics (Utts, 2014)
IBM SPSS Statistics Guide to Data Analysis (Norusis, 2011). Both are easy to undernd take a hands-on approach to learning.

n we work with data, we will often compare numbers, because raw numbers hardly
 meaningful by themselves. We create meaning when we compare them to other
s or benchmarks. Let’s explore this concept by considering how much money the
overnment spent in fiscal year 2012 on national defense programs (Financial
ement Service, 2013).
 federal government spent more than $680.4 billion on this category, which
s homeland security. Sounds like a pretty huge number, right? Maybe not so
when you compare it to the amount the U.S. government spent in the previous

ear (2011): more than $708.2 billion. Subtract those numbers and we see that
ng for defense actually decreased by around $27.8 billion. How significant of a
 was that for defense? Calculate the percent change and you get a 3.9 percent

e. By comparing numbers over time, we can generate some information that’s
 ing and meaningful.
TER

    COMPARISONS
    8 NUMBER SUMMARIES AND

```

```
 We can do the same by comparing defense spending to other categories. How does f
year 2012 spending on national defense stack up to spending on Social Security, the fed
program that guarantees income to retirees, survivors of deceased workers and disa

workers? In fiscal year 2012, the federal government spent more than $773.2 billio
Social Security. Compare that to the $680.4 billion in defense spending and you will
that it was $92.8 billion—or 13.6 percent—more.
 How significant, respectively, are defense and Social Security in terms of all spend
by the U.S. government? To calculate that we will need to compare each individual amo
to the more than $3.5 trillion in total outlays for 2012 to generate a percent of total. So
Security accounts for the largest share, at around 21.9 percent, or a little more than
fifth. Defense spending accounts for around 19.2 percent, or a little less than one fifth

SIMPLE SUMMARY STATISTICS

We'll start with the simplest kinds of numbers that we can generate from our data: s
mary statistics. Summary statistics are very useful because they can tell us a lot about
data. However, summary statistics can sometimes be misleading, as we shall see.
  Count tells us how many items we have in our data. It helps us to answer questions

start with, “How many ...?” In our spreadsheets, we can count data stored as numbe
text and dates.

  Sum gives us the total amount for all items in our data. For instance, we could sum
total number of people who were registered to vote, as noted in our voter turnout spr
sheet file. Sum helps us answer questions that start with, “How much... ?” Sum only wo
with data stored as numbers.
  Averages generate what statisticians call the central tendency, or a number that
represents a collection of numbers. Averages only work with data stored as numbers.
  Using averages can get tricky, because we have three measures at our disposal:

mean, the median and the mode. The mean is the arithmetic average, the number t
generated by adding our numbers and then dividing by the number of cases. This is p

ably the first average you learned in elementary school. So, if we have the three number

2 and 3, we would add them for a sum of 6, then divide by the number of cases (3) t
our average of 2.
  The median is the midpoint in a set of numbers, ordered from low to high. So
median for the same numbers would be 2. If we have an even number of numbers, spr
sheets calculate the median by running the mean on the two numbers in the middle. So

median for 1, 3, 5 and 7 would be 4 (3+5/2). As you can see, a median can be alittle con
ing at first, because it might be a number that does not appear in a data set.
  Outliers, or numbers that are notably low or high, can skew the mean. In t

instances, the median is a more accurate reflection of the central tendency. Numbers
an unlimited cap—such as incomes or home sale prices—are more prone to having o
ers. Major League baseball player salary data provide a great example. Players like the

```

```
other useful summary statistics can help us determine the range of values that we
 spreadsheet data that are stored as numbers or dates. The minimum is the smaller or earliest date in our data. The maximum is the largest number or most recent
 ur data.

RED TO WHAT?

lenge we face when analyzing data is in making our results meaningful to ourselves

thers. Whenever we have a raw number, it derives meaning from its relationship
 numbers. So we always want to ask, Compared to what? Fortunately, we have in
ytical toolbox a number of comparisons that are easy to generate using spreadograms. They are amount change or raw change, percent change, percent of total,
nd rates. We'll consider each of these using the federal outlays data from the intro in this chapter.
ee from the outlays report available online as a PDF at http://www. fiscal.treasury
reports/rpt/combStmt/cs2012/outlay.pdf that the federal government spent
an $14.7 billion on energy-related items in fiscal year 2012. That sounds like a
 t of money, certainly more than any of us will amass in our lifetimes.
ver, we have no way of knowing just how significant this amount is, because we
put it into context. Let’s compare the amount for 2012 to the amount for 2011,
as more than $12.0 billion. So to calculate the amount change or raw change we
 the amount from 2011 from the amount from 2012 and get a result of roughly
ion.
 7 billion increase sounds like a big boost for U.S. government spending on energy.
show just how big of an increase that is by comparing it to our starting point of
is generates the percent change. To calculate that, divide the amount change by
ting point. So we would divide $2.7 billion by $12.0 billion and get a result of
 22.2 percent.
urse, we should calculate the amount and percent change for all of our spending
es to get results that we could compare to those amounts for energy.
 go back to the $14.7 billion spent in fiscal year 2012. We can compare that amount
otal spent by the U.S. government that year to calculate the percent of total.
e $14.7 billion by more than [$3.53 ] [trillion ] [to ] [get ][just ][more ] [than ] [four-tenths ] [of ]
. So spending on energy was [just ][a ][sliver ][of ][the ][total ][pie ][in ][2012. ] [National ] [defense, ]
st, took up nearly one [fifth ] [(or ][around ] [19.2 ] [percent) ] [of ][the ][total. ]
mode is the number that appears most frequently in a data set. Our mode for 1, 2,
nd 12 would be 2. In this case, the mean (4.8) and median (3.8) are more represen the central tendency than the mode. In truth, we will rarely use the mode to generary statistics. We will use mean and median instead.
n annual pay, help push the mean way above the median.
 Dodgers’ Zack Greinke, who are at the top of the chart with tens of millions of

```

```
 Ratios also can help us understand relationships between numbers. Ratios are he
when we want to calculate proportions that show differences between numbers. To g
ate a ratio we take our number and divide it by another number to which we are dra

a comparison. For example, the average pay gap between U.S. chief executive offic

publicly traded corporations was 204:1 (Smith, 2013). In other words, for every $1 e
by a worker, the chief executive earned $204. In education, we often hear about stu
to-teacher ratios; they can help us determine if classrooms are overcrowded. With
federal spending data we can compare defense to energy spending to get a def
to-energy ratio. Divide the $680.4 billion for defense spending by the $14.7 billio
energy and we get a 46:1 ratio. So for every $1 the government spent on energy, it
$46 on defense.
  Finally, rates are helpful tools because they allow us to more fairly compare num
from areas with dissimilar populations. Rates helped The New York Times show that
cities like Rehoboth Beach in Delaware and Palm Springs in California had displace
Francisco and West Hollywood as strongholds for households headed by same-sex co
(Tavernise, 2011). The newspaper calculated rates of same-sex couples per 1,000 h
holds, using data from decennial censuses.
 Usually when we generate rates we first calculate a per capita—or per per
number. Then we multiply that by a standard number to normalize our results.
  The New York Times compared the same-sex couple population numbers to the
number of households in each city for its analysis. To do that, it divided the same
couples by the total number of households.
  After generating a per household rate, it multiplied that rate by 1,000 so it could ex
the number in terms of 1,000 households. Per capita rates are usually so small that th
fractions of numbers and don’t make much sense. So we normally multiply them
standard number, which is something the data source can provide. Crime rates bas
the FBI’s Uniform Crime Reporting System data are typically calculated per 100,000 pe
Medical and health-care statistics often are expressed in terms of 100,000 people.

BENCHMARKING

Another way to think about number comparisons is by thinking about benchmarks.
can have internal and external benchmarks. Internal benchmarks are numbers tha
contained within our data. For example, our ratio of 2012 defense to energy spending
be considered an internal benchmark because we are comparing two amounts fro
same year. Percent change could be considered an external benchmark because w
comparing a number from one year to that number in the previous year. Reports cr
by government agencies, or nongovernmental organizations using data, can be a b
marking tool. These reports often will contain summary statistics or other figures th
can compare to our own data.

```

```
that we've seen how we can use summary statistics and number comparisons to
meaning from our data, we're going to learn how to calculate summary statistics
er comparisons using Excel in the next two chapters.

R OWN

d the 2011 UScrime.xls from the book website and then open it. Inspect the file
hat it contains data about crimes as reported by U.S. cities to the FBI, along with
ns. Name and explain three number comparisons that you could make to gener meaningful statistics.

```

```
  WT stolen tne >i ree
 my Live wih r er ii \ al i: - tog Verh . :
        ; we Ades el wei ito

                      ih

               : " net hee? elem 29 Lorelipe Wyiihy ea ak i

                                ‘ my ; o, @€* ge ani
                 ; nes alk ping linahion gran) lng
                    Ve = Si air tu ti ig lly pape.

           ~~ ; 4 a 9 ; ;
                 ae ptt ae pe Ol hes ft oe
    ¥ : rot ri aie ar ee it ily es tng
       ge AN ———) «Sn Dew reap endl
— a Se Se nene eal AGe. Gl iesné Pade
 SS 2 - Nib ah chatmaiperk
           & nites # 101 DOG:

ae — = - - :

                                                  '
                                   try ees apes t

                         =o a sale! ane Saat

  ~ 2 = k i “ CSS) lan ohana neit
      it tear : —s eSee Wire . COIN Nnifan gue P| °
   1 FAY ila! SPATS
                  ae
     [
                              Id? ad See soe ibe ar eS es
    AE arr ite
       eS em Seay 2a ar aM
      eee: qe wiry irene a
  "ne

                    : a vie ite s1Nb OW ge ye

                                                      7 = + Px. a . i
                          ia : 7

                                     .

                        (1G e eats
                       we “sie ipearer io
                                  |

7 wes elie ca
           iy aire aie
             . ~ cin
                   sree ee h file / “ities el
            | ia as Pe ag ed Ya
        ;
                . ee a
 Gag Pile
                    * pany ahaa
           Seatie Sy
            (as j

                              ih, Mis + erable trang
        - Rd in TR, Lelpegy U4: eae
   j ; : Do eFheg

```

```
 ow that you know how summary statistics and number comparisons can help you
 find meaning inside data, it’s time to use Excel to run these calculations. We're
 going to work with a file called city_crime.xlsx from the book website for our
 in this chapter. In the next chapter, we'll learn how to use Excel to sort, filter and
and summarize our data.
n the file and examine it. You'll see that we have 2011 and 2012 population, violent
and property crime data for 31 U.S. cities with 2012 populations greater than
. Chicago and Tucson are missing because their crime data were incomplete.
TER

    COMPARISONS
    9 CALCULATING SUMMARY

    STATISTICS AND NUMBER

```

```
8 c 0
                 Violent

```

```
E

```

```
                               Population crime Property Population Violent Property
    State City 2011 2011 crime 2011 2012 crime 2012 crime 2012
EW YORK New York 8,211,875 $1,209 140,457 8,289,415 $2,993 142,760

AUFORNIA Los Angeles 3,837,207 20,045 86,330 3,855,122 18,547 87,478

EXAS Houston 2,143,628 20,892 168,336 2,177,273 21,610 107,678

 PENNSYLVANIA Philadelphia 1,530,873 18,268 59,617 1,538,957 17,853 56,997
RIZONA Phoenix 1,466,097 8,089 64,479 1,485,509 9,458 60,777

 VADA las Vegas Metropolitan Police Department 1,458,474 10,813 41,426 1,479,393 11,598 46,427

EXAS San Antonio 1,355,339 7,038 80,868 1,380,123 6,943 82,668

CAUFORNIA San Diego 1,316,919 5,104 29,709 1,338,477 5,529 31,700
 EXAS Dallas 1,223,021 8,330 61,859 1,241,549 8,380 $4,300

 AUFORNIA San Jose 957,062 3,206 24,972 976,459 3,547 28,463

LORIDA Jacksonville 834,429 5,182 36,113 840,660 5,189 34,674
 DIANA indianapolis 833,024 9,170 46,967 838,650 9,942 46,898

EXAS Austin 807,022 3A71. 42,250 32,901 3,405 43,472

AUFORNIA San Francisco 814,701 5,374 32,886 820,363 5.777 38,898
ORTH CAROLINA Charlotte-Mecklenburg 789,478 4,787 32,008 808,504 §,238 32,587

ederal Bureau of Investigation.

 orm Crime Report data from the FBI, open in Excel.

author created this spreadsheet using separate 2011 and 2012 FBI Uniform Crime
Excel files that he downloaded from the bureau's annual Crime in the United States
 at http://www.fbi.gov/about-us/cjis/ucr/ucr-publications#Crime. The FBI prota about eight major crimes: murder or non-negligent manslaughter, forcible rape,
 and aggravated assault all are categorized as violent crimes; burglary, larcenyotor vehicle theft and arson are categorized as property crimes.

```

```
generate some meaningful information

SUM CRIMES BY YEAR
As a first step, let’s calculate total crime for each year in each city. In Cell 11 type “T
crime 2011” for a column header and hit Enter. Type “Total crime 2012” in J1 for a col
header.
  In Cell 12, calculate New York City’s total crime for 2011 by entering this form
“=F2+D2”. All Excel formulas start with the = sign and use cell references as muc
possible. This tells Excel to add the value in D2 (the violent crimes for New York Ci

2011) to the value in E2 (the property crimes for New York City in 2011). You should

191,666 for your result. (Note: We can also subtract (—), divide (/) and multiply (

Excel.) :
 Copy this formula for 2011 crime down for all of the other cities by putting the cu
block in cell 12 and double-clicking on the block at the bottom right corner. (You could
drag this handle down until you get to cell 132 for Fresno.) Even though numbers ap
for the cities’ 2011 total crimes, our cells really contain formulas. We can check this ou
clicking into cell 13 for Los Angeles. Excel’s formula bar tells us that “=D3+E3” is what
cell contains. Notice that Excel was smart enough to adjust the formula by increasing
row number in each cell reference by one.

                             é D E 2 & 5 £ 3
                                Violent Total Total
                           Population crime Property Population Violent Property crime crime
       1 2011 2011 crime 2011 2012 crime 2012 crime 2012 2011 2012
      2 New York 8,211,875 51,209 440,457 8,289,415 52,993 142,760 191.666

      3 jLos Angeles 3,837,207 20,045 86,330 3,855,122 18,547 87,478| 406.375]

      4 Houston 2,143,628 20,892 108,336 2,177,273 21,610 107,678 429,228

            4 ‘Philadelphia 1,530,873 18,268 59,617 1,538,987 17,853 56,997 77,885

      § Phoenix 1,466,097 8,089 64,479 1,485,509 9 ASB 60,777 = 72,568
      7 Las Vegas Metropolitan Police Department 1,458,474 10,813 41,426 1,479,393 11,598 46,327 52.239
      8 San Antonio 1,355,339. 7,038 80,868 1,380,123 6,943 82,668 87.906
      9 San Diego 1,316,919 5,104 29,709 1,338,477 5,529 31,700 34,813
      10 Dallas 1,223,021 8,330 G1,859 1,241,549 3,380. $4,300 70,189

Source: Federal Bureau of Investigation.

Note: Calculating total crimes for cities.

 Now enter in J2 the formula to calculate total crimes for New York City in
(195,753): “=G2+H2”. Copy that down for all of the other cities.
  Practice safe computing by saving a working copy of the file using File | Save As, u
anew file name.

MINIMUM AND MAXIMUM NUMBERS

It would be good for us to know the range of numbers in each of our eight columns.
do that at the bottom of the sheet. Scroll down to Cell B34 and enter “Minimum”. B

```

```
 t the maximum of each column, enter this into Cell 35: “=MAX(C2:C32)” and
 the right. This generates some interesting data, such as the range of violent crime
in 2011—2,858 to 51,209.

  CHANGE

e analyzing these data for year-over-year trends we would want to know how much
hanged in each of our cities. We'll calculate the amount change. First enter “VC

 in Cell K1, “PC change” in Cell L1 and “Total crime change” in Cell M1.
 we will calculate amount change, starting with the violent crime change in Cell K2.
=G2-D2” to subtract the 2011 violent crimes for New York City from the 2012
 rimes. We see an increase of 1,784. Copy the formula down for all of the cities and

 some of them, including Los Angeles, experienced decreases in the number of
 rimes reported.
alculate the amount change for property crimes in cell L2, enter “=H2-E2” and
 or all. Likewise, calculate the amount change for all crimes in cell M2 by entering
 and copying for all of the cities.
 spreadsheet should look something like this:

     A a [Panne rae ee em Ye ee
                                                         - Total Total Total

                                crime crime vce PC crime
   State City 2011 2012 change change change |
 ew YORK New York 191,666 195,753 1,784 2,303 $,087

 ALIFORNIA Los Angeles - 106,375 106,025 -1,498 1,148 -350

 EXAS Houston 429,228 129,288 718 -658

 ENNSYLVANIA Philadelphia 77,885 74,850 -415 -2,620

 RIZONA Phoenix 72,568 70,235 1,369 ~-3,702
 EVADA Las Vegas Metropolitan Police Department 52,239 58,025 785 5,004
 XAS San Antonio 87,906 89,611 -95 1,800

 ALIFORNIA San Diego 34,813 37,229 425 1,994

 EXAS Dallas 70,189 62,680 50 ~=—--7,559

 eral Bureau of Investigation.

 lating amount change in Excel.

NG UP TO PERCENT CHANGE

 numbers to generate the percent change. We'll use columns N, O and P for those
orce the concept from the last chapter, the amount (or raw) change doesn’t say
ecause we lack context. That’s why we always want to compare the raw change to

ons. So enter “VC % change”, “PC % change” and “Total crime % change” as headers
1 of those columns.
ing the handle at the bottom right of the cursor.
   in Cell C34: “=MIN(C2:C32)”. This tells Excel to calculate the minimum num,480) for all cells from C2 through C32. Copy that formula for all of the other cells

 ach column we will need to compare the amount change to the starting points

```

```
returns less than a whole number: .03484. Excel is expressing percent in terms

number 1, because the column is formatted as general, not percentage. Soon, w
format the column as percentages, so we will see that the increase really is just
3.5 percent.
  In 2, enter this formula to calculate the percent change for property crimes: “=L2
This divides the amount change by the number in 2011. In P2, enter “=M2/12” to
the change in total crimes by the number in 2011. Copy the formulas down for colum
O and P.
  It’s difficult to distinguish between our numbers because Excel is reporting th
decimals. We will change the formatting so they appear as percentages instead. Selec

umns N through P, then right-click on any of the header letters. Select the Format Ce
option from the popup menu and the cell formatting box opens.

                      i ¥C % change
                              | | Currency j
                     i ae General format celts have no specific number format.
                        | | Date ‘
              i Time
           | | Percentage
         | | Fraction
             | | Scientific
             / ‘Text
                  | | Special
                            | 7 Custom

Source: Microsoft Excel for Windows 2013.

Note: Percent change column currently set to General.

 Under the Number tab, pick Percentage as the Category. Set the number of de
places to 1 and click OK to make the changes.

```

```
 Number

  General
  Number
  Currency
  Accounting
  Date
  Time

  Fraction
|. Scientific
}) i Text
 | Special
  Custom

 | .

```

```
      | Border | Fin | Protection |

 Sample

 VC % change

Decimat pisces: a r¥

```

```
     _ Percentage formats multiply the cell value by 100 and displays the result with a percent symbol.

rosoft Excel for Windows 2013.

g percent change column to Percentage with 1 decimal place.

we cansee that the data in our percent change columns really do look like percentages.
r work.

```

```
PC%

```

```
crime %

```

```
 3 CALIFORNIA
 ‘TEXAS
 ‘PENNSYLVANIA
 /ARIZONA
  N H
 =

  H j atten
  t
  TEXAS
11 CALIFORNIA

```

```
 Los Angeles

 Houston
 Philadelphia
 Phoenix
 Las Vegas Metropolitan Police Department

 San Antonio
 San Diego
 Dallas

_ San Jose

```

```
VC %

3.5%
 -7.5%
 3.4%
 -2.3%
 16.9%
 7.3%
 -1.3%
 8.3%
 0.6%
 10.6%

```

```
 1.6%
 1.3%
 -0.6%
 4.4%
 -5.7%
 12.1%
 2.2%
 6.7%
12.2%
 29.5%

```

```
 2.1%
 0.3%
 0.0%
 -3.9%
 -3,.2%
11.1%
 1.9%
 6.9%
~10.7%
27.1%

```

```
eral Bureau of Investigation.

t change columns properly formatted.

```

```
RUNNING RATES
Now we're ready to generate some more-meaningful information by calculating
rates. Rates allow us to more fairly compare areas that have different populations, s

New York City (more than 8.2 million) to Fresno (just a bit greater than 500,000).
 When we calculate rates, it’s a two-step process. First, we calculate a per pers
per capita, rate. Then, we calculate the rate per a set number of people. Here’s
we'll use the FBI’s standard of 100,000 people. We should calculate these rates fo

years, but we will stick to 2012, the most recent in our data file, for this lesson
Columns Q-V and enter these as headers in Row 1: “2012 VC per Cap”, “2012 P
cap”, “2012 Total crime per cap”, “2012 VC per 100k”, “2012 PC per 100k” and
Total crime per 100k”.
  In Q2 we will compare the number of violent crimes in 2012 to the population
same year. The formula is “=G2/F2”. Enter and copy it for all of the cities. We get .
for New York City, meaning not even one for every person. That number makes no
so we will later multiply it by 100,000.
  In R2, compare 2012 property crimes to population with this formula: “=H2
and copy it for all of the cities. In $2 compare total crimes for 2012 to population
the formula “=J2/F2” and copy it for all the cities as well. Your spreadsheet should
like this:

```

```
                                  2012 2012
                              | Total Tota
                      | 2012 ve crime 2012VC 2012PC crim
1 ine i OY, sins summa, POE SAP PO Cap per eap per 100k per 100k per 1
2 NEW YORK New York | 0.00639
3 CALIFORNIA Los Angeles | 0.00481
4 TEXAS Houston | 0,00993
§ PENNSYLVANIA Philadelphia | 0.0116
6 ARIZONA Phoenix | 0.00637
7 NEVADA Las Vegas Metropolitan Police Department 0.00784
8 TEXAS San Antonio | 0.00503
9 CALIFORNIA San Diego | 0.00413
10 TEXAS Dallas | 0.00675
11 CALIFORNIA San Jose | 0.00363 0.

```

```
    412 FLORIDA Jacksonville | 0.00617 0, 0.04742

Source: Federal Bureau of Investigation.

Note: Per capita crime rates.

 Now, we're ready to calculate rates per 100,000 population. In T2 for New York
enter “=Q2*100000” to multiply the per person violent crime rate by our standard.
better! Excel tells us that the rate is more than 639 violent crimes for every 100,000 p
Copy that down for the rest of the cities.

```

```
                                                i Total
                            | 2012 ve 2012 PC crime
 we re AY, trent PRE AOOK. par 100K: par 200k
  2 NEW YORK New York | 639.3 1722.2 2361.5
  3 CALIFORNIA Los Angeles 481.1 2269.1 2750.2
  4 TEXAS Houston 992.5 4945.5 5938.1
  5 PENNSYLVANIA Philadelphia 1160.1 3703.6 4863.7
  6 ARIZONA Phoenix | 636.7 4091.3 4728.0

  7 NEVADA Las Vegas Metropolitan Police Department 784.0 3138.2 3922.2
  8 TEXAS San Antonio 503.1 5989.9 6493.0
  9 CALIFORNIA San Diego | 443.1 2368.4 2781.4
  10 TEXAS Dallas 675.0 4373.6 5048.5
  11 CALIFORNIA San Jose | 363.3 2914.9 3278.2

 ederal Bureau of Investigation.

me rates per 100,000 population.

all the results for the violent crime rate per 100,000 and it looks like New York City
 middle of the pack. We'll figure that out for sure in the next chapter, when we learn
 sort our results. (Note: We could calculate per 100,000 person crime rates in one
ing a formula like this: =crime number/population* 100000.)

NG RATIOS

 use ratios in our analysis here to compare the numbers of property to violent
in each city. This could generate some interesting information by showing us in
ities property crimes are more prevalent. To do that, we will need to divide property
by violent crimes for each year in Columns W and X. Enter “2011 ratio” and “2012
nto the headers in Row 1.
2, we will compare 2011 property to violent crime, so enter “=E2/D2” and copy
 all of the cities. In X2, we [will ][compare ] [the ][2012 ] [figures ] [using ][“=H2/G2”. ] [Again, ]
mbers are not properly formatted, [so ] [change ] [them ] [to ] [numbers ] [with ] [one ] [decimal ]
ulate the other rates per 100,000 people by entering the following formula for the
y crime rate in U2: “=R2*100000”. Then, enter in V2 “=S$2*100000” for the total
ate per 100,000. Note that each city’s total crime rate per 100,000 is the sum of its
y and violent crime rates. Our results have an inconsistent number of decimal
because our columns are formatted as general. Using the Format Cells options,
 Columns T—-V to Number with one decimal place. Save your work. Your spreadhould look like this:

```

```


ot o

```

```
                             2011 «=. 2012

NEWYORK —_—_—New York noe a7
CALIFORNIA Los Angeles 4.3 AT

TEXAS Houston i 5.2 5.0
PENNSYLVANIA Philadelphia 3.3 3.2
ARIZONA Phoenix 8.0 6.4
NEVADA Las Vegas Metropolitan Police Department) 3.8 4.0

TEXAS San Antonio : 11.5, 11.9
CALIFORNIA San Diego ' 5.8 5.7
TEXAS Dallas 74 6.5

```

```
Source: Federal Bureau of Investigation.

Note: Ratios of property to violent crimes.

 New York City had 2.7 property crimes for every violent crime in 2012. In San Anto
property crimes were far more prevalent: nearly 12 for every instance of violent crime

PERCENT OF TOTAL

Another way to check on the prevalence of violent crime in each city is to compare vi
crimes to overall crime. We'll do this by calculating the percent of all crimes that are vio

  Use “2011 % violent” and “2012 % violent” for the headers in Columns Y and Z. I
calculate the percentage of crime that was violent in 2011 with this formula: “=D2/
Likewise, for 2012 enter “=G2/J2” in Z2. Copy the formulas for all the cities and format
cells as a number with one decimal place.

                                   2011 2012 2011% +2012 %
  Ae. Seen See ee ratio ratio _ violent _ violent
      2 NEW YORK New York 27 2.7 26.7% 27.1%
      3 CALIFORNIA Los Angeles | 43 47 18.8% 17.5%
      4 TEXAS Houston 5.2 5.0 16.2% 16.7%
     5 [PENNSYLVANIA Philadelphia | 33 3.2{ 23.5%] 23.9%
      6 ARIZONA Phoenix | 8.0 6.4 11.1% 13.5%

       7 NEVADA Las Vegas Metropolitan Police Department 3.8 40 20.7% 20.0%

       8 TEXAS San Antonio i 414.5 11.9 8.0% 7.7%
      9 CALIFORNIA San Diego i 5.8 5.7 14.7% 14.9%

Source: Federal Bureau of Investigation.

Note: Violéi crime percent of total calculations.

```

```
esults support our earlier observation: New York has a much larger proportion of

rime (27 percent) than San Antonio (7.7 percent).
the spreadsheet and close it. We'll use it again in the next chapter.

SUMMARIZING

 move on to the next chapter, where we'll learn how to manipulate our data even
 ll learn a couple more tricks using Excel summary functions. Open the modified

te_House_Staff.xlsx workbook, which was downloaded from the White House
 at http://www.whitehouse.gov/21stcenturygov/tools/salaries. Under law,
ial administrations are required to report staff salary data to Congress every year.
adsheet holds data about 460 staff members, including their names, positions and
We are going to calculate some basic summary statistics using these data.
 the end of the sheet and type some labels: type “Total pay” in B463, “Mean pay”

 and “Median pay” in B465. Next, calculate the sum and the two averages next to
.

63 enter the SUM function: “=SUM(C2:C461)”. Total cay $37,859,780]
s all of the numbers in > that cell range. In C464 enter Mean esa $82,331 oie
 la for the mean: “=AVERAGE(C2:C461)”. In C465
 formula for the median: “=MEDIAN(C2:C461)”. red te aa
those cells as currency with no decimal places and _jote: Calculating summary statistics.
e results at left.
tells us the staff earned more than $37.8 million. The mean salary was more than

 while the median was $70,000. Those are pretty close, so we can say that these
aren’t skewed high, as Major League baseball player salaries are.
ile | Save As to save a working copy of your file.
s chapter you learned how to use Excel to generate number comparisons that are
ul. In the next chapter, you will learn how to sort the data to find large numbers
resting patterns. You will also learn how to filter data and use pivot tables to create

es for categories in your data.

R OWN
d the comparisons.xlsx [file ][from ] [the ][book ] [website ] [and ] [follow ] [the ] [directions ] [on ]

he three worksheets.

```

```
                      aie }
       penn eal wurriay
                   ity riled .

                > an) iw
 oil cowk aA bare on Sestpaits aiaies ~
                       ra
rroirnyairwy Tey val Wa Eau £ wel at hats Fond bes be
                                        V
  2 tively tenn v ttt vik Page th ager
               ‘ 3 BC “4
     a - nm +70 ad
            Sinicitees sg =e

```

```
batho ar?
= ld TAP SuPer > mms Pi ON doe a
         its A ne mens es hue Aes ss
       GQ darhord Ds wrekee:

```

```
; A nt sphin eli ~— 7c)tetien ceralitl

```

```
bith af ctelodlt qubiesi Ree ve) Fisher a aah eed Sah
                      hens!
                                          ie

```

```
    wma oitiske, sit io eaes

        ‘fil
        oh

         i ke “ii Dey tn
 gts fesdety want Shays OY AN pa ‘
HSA ue tian iS Ta shan lgl seers wrprt bat oye TS
                 Lith eae ont vualresiag a x4 ahi baa
                               FE “a
       Sista

```

```
  ih PND Fal aphaentih Tike a Aah
iol SARS hake viata

```

```
                     ofl wah conan ge
            Ur Wiha ee Hh ani rabies a i ANE —

 wy
. eed La Lhe" -naiboarts
   ig, “4 snot hepa
      Teh aaa aE ALAR Re rv weg Re aoa ath
         i Lene ya say) OOS Sl ened ile

```

```
      y Mesehilam) as wok 1
                         wedkcnin licaueey aa Laipreed gio} syiliaele
           , (wily Rah alta
        a -. AS A il
ad yerdioo ia ten 1 oh (oes a

```

```
 ‘7 al ot) rio Cu wt oan dig in gieny Bogut) win a ic tag
           ¥

```

```
          acest wot ert wide or aE
~
                           rh pelt wry a sto
                    (=) sen
                             =~ eee
           fas
                                           teateh
      = |

                         om.

```


```
                   o
/ a

               o
        pe fale Adingit oi vai ut ‘aa
       Re

```

```
unning functions. That has helped us travel far toward our goal of going from data
o knowledge. Our next step is learning how to use Excel as a lightweight database
. We can use Excel to sort and filter our data so we can uncover meaningful patWe can use Excel pivot tables to group our data by categories and then calculate

ies (counts, sums and averages) for those groups.

NG

nd other spreadsheets allow us to sort our data in different ways. We can sort num
d dates in ascending order, meaning lowest to highest, or alphabetically with text.
ve any negative numbers, those would be listed first because they have a value lower
or any positive numbers. We're going to learn how to sort using our city_crime.xlsx
heet, so open that. We can use sorting to answer questions like, Which city had the
 increase in property crimes? Which city had the lowest violent crime rate in 2012?
city had the greatest ratio of property to violent crimes in 2012?
ing in Excel can be tricky because you first need to highlight all of the data you want
including the headers but excluding any summary functions calculated at the botthe sheet. If you fail to highlight all of your data, Excel may sort some of your colnd leave others unsorted. This is a big problem, because you'll have mismatched
ote: You can always undo a bad sort by using Ctrl-Z on your keyboard, or the Undo

e will practice safe computing by first highlighting the data we need to sort. Ona PC,
 cursor inside any of the cells containing data or headers. Then, hold down
ft-8 and Excel selects all of your data. Scroll down and see that the rows used to

e the minimum and maximum are unselected,
s how it should be. Mac users can highlight the
 far, we have used Excel to perform simple spreadsheet operations: doing math,
TER 10 SPREADSHEETS AS DATABASE
    MANAGERS

```

```
 data using the Command-A key combination.
 we are ready to sort and discover which city

```

```
Sort

```

```
 lowest violent crime rate in 2012. Select the Source: Microsoft Excel for Windows 2013.
b and then the big Sort button. Note: Excel sort button.

```

```
Sows: MVE HOS Hy Wingaag QA

NR POH GHZ ANALY BW

  tr the options, Sort by DU12 VC per 100K, Sort On Values and Order Smallest to
est. The dialg box should look like this

QS. MIDVSR PO! Hy WHA DUS WED

Noe: Sad Dy DOTD VOB MMs Vr HAQQALY QQQuisver Qgumnr

 CHK OR f sort and we see Ia Coluenn T that San Jose had the lowest property
rate in DOL, at 303.3. Austin is second lowest with 408.8,
  This opens the Sort dialog box, where we can set the options for sorting. Note th
cheek box ie the upper right should be checked, because our Excel sheet does have h
rows (the abels that we created in Chapter 9),

```

```
|

```

```
|

```

```
                          2012 ve 2012 Pc
1| State ty per 100k per 200k
2 [cAuFORNIA San Jose e [ "363.3 2914.9
3 TEXAS Austin | 408.8 5219.3
4 CALIFORNIA San Diego | 413.4 2368.4
5 TEXAS El Paso | 423.2 2429.3
6 CALIFORNIA Los Angeles | 481.1 2269.1
7 TEXAS San Antonio | S031 5989.9
8 OREGON Portland | $17.2 5092.3
9 CALIFORNIA Fresno | 543.4 5086.3
10 TEXAS Fort Worth | $87.5 4222.0

```

```
11. WASHINGTON Seattle | $97.6 5093.8

```

```
       412 KENTUCKY Louisville Metro | 598.8 4293.9

ederal Bureau of Investigation.

 sorted ascending by 2012 violent crime rate per 100,000 people.

 sort the data again to figure out which city had the highest total crime rate in 2012.
data block somehow became unselected, select it again using Ctrl-Shift-8. Select the
button again and make sure that the My data has headers option is checked.
, set Sort by to 2012 Total crime per 100k, Sort on to Values, and Order Largest

est. Select OK and look at the rates in Column V. Memphis is tops with 8,063.1,

 by Detroit at 7,915.0.

     ‘7 [TENNESSEE "Memphis
       3 MICHIGAN Detroit
       4 OKLAHOMA Oklahoma City
        5 INDIANA Indianapolis
       6 TEXAS San Antonio
       7 WISCONSIN Milwaukee
       @ NEW MEXICO Albuquerque
       9 MARYLAND Baltimore

 deral Bureau of Investigation.

 crime rate sorted descending.

can also sort using more than one column. Let’s learn how to do that by sorting our
t by state and then by city. We [will ][see ] [the ][states ] [listed ] [alphabetically. ] [If ][any ] [states ]
re than one city, we'll see those listed alphabetically within the states.

```

```
Source: Microsoft Excel for Windows 2013.

Note: Sorting by two columns.

  Click OK and we have our alphabetical sort, first by state and then by city. Note
California has more than one city, with Los Angeles at the top and San Jose at the bo
Save your file. You'll see that it’s saved with our state and city sort order. Now close t

Source: Federal Bureau of Investigation.

Note: Data sorted by state and city.

FILTERING

Another database function that’s built into Excel and other spreadsheets is filter
allows us to display only those rows of data that meet certain criteria. We will give

using the modified 2013_White_House_Staff.xlsx spreadsheet that we worked w
Chapter 9. Look in Column B of the spreadsheet, which lists the status of the empl
Most of these statuses are Employee. But some others say Detailee, to denote employ
other federal agencies who have been temporarily detailed to work in the White
 Make sure your data are highlighted and then select the Sort button. Sort by State
on Values and Order A to Z. Then select the Add Level button so we can sort by city
Set the Then by option to City, Sort on Values and Order A to Z.

```

```
the Office of Management and Budget’s Regulatory
e and Training Program. We'll use a filter to show only N\A
ho have been detailed to the White House, then show

```

```
arning at least $100,000.
, we need to put our cursor inside the block of data that
e to filter. Select the Data tab and then the big Filter but
```

```
   Filter

Source: Microsoft Excel for
Windows 2013.

```

```
ch looks like a funnel. Note: Excel filter button.
p-down arrows now appear next to each of our columns.

re the controls that we use to filter the data.

```

```
PRESS ASSISTANT
SPECIAL ASSISTANT TO THE PRESIDENT AND
DEPUTY COMMUNICATIONS DIRECTOR
DEPUTY ASSISTANT TO THE PRESIDENT AND |
SENIOR CONFIRMATIONS ADVISOR

```

```
  2 jAberger, Mane E
  3. Abraham. Yohsnnes A
  4 Adier, Caroline E.
  5 Agnew, David P.
  6 Aguilar, Rita C.

he White House.

p-down arrows for filters.

```

```
$42000.00 Per Annum
$120000.00 Per Annum
$7000.00 Per Annum
$153500.00 Per Annum
 $90000.00 Per Annum

```

```
k on the drop-down arrow for Column B and then select only Detailee from the list
ottom of the box. Click OK and we now see only the people who have been tempo
etailed to the White House.

```

```
      19 Baker, Lamar W.
       30 Berrigan, Elizabeth D.
       39 Brandt, Kate E.
       51 Calderon, Tovah R.
      64 Clark, Melanca D.
       86 Dawe, Christopher J.
      106 Elliott, Brandace N.
       111 Fazili, Sameera
       114 Ferrell, Taylor N.
      119 Flores, Andrea R.
     149 Gunja, Mushtaq Z.

       186 Johnson, Guy A.
     224 Lee, MarisaR.
      230 Leonard, Shelley D.
            oe
      251 270 ; McQuaid, Marquez, Laura Nicholas R. L.

he White House.

 filtered by Detailee in the Status column.

```

```
Detailee

Detailee
Detailee
Detailee
Detailee
Detailee
Detailee
Detailee
Detailee
Detailee
Detailee
Detailee

Detailee

Detailee

Detailee
Detailee

```

```
314 Parker, JaLynda L
318:Pearlman, Amanda J.

```

```
Detailee We havea few clues that our rows are filtered:
Detailee

```

```
Detailee

```

```
"ints neport to congress onwit [© nel appears next to the Status label in B1. The row

```

```
READY | 38 OF 460 RECORDS FOUN 33

```

```
Source: The White House.

Note: Excel status bar. The status bar shows
how many records have been filtered.

   Show rows where:
     Salary

```

```
bers turn blue. The unfiltered row numbers disap
And the status bar at the bottom right tells us “2
of 460 records found”. All of our other records st
there, but they’re just hidden behind the filter for
      Now we are going to filter to
      just those detailees who make at
      $100,000. Click the drop-down a

```

```
       is greater than or equal to “1000001 Cy ae

     Band © Or

   Use 7 to represent any single character
   Use * to represent any series of characters

Source: Microsoft Ex' cel for Windows 2013.

Note: Filtering for detailee records where the salary is $100,000 or

more.

```

```
next to Salary, then pick Number F
| Greater Than Or Equal To and a d
box appears. Enter 100000 (no d

sign or commas) in the box on the
and click OK.
 Excel shows us the 22 detailees

earned $100,000 or more.

```

```
 19 Baker, Lamar W.
30 Berrigan, Elizabeth D.
51 Calderon, Tovah R.
64 ‘Clark, Melanca D.
86 Dawe, Christopher J.
111 Fazili, Sameera
114 Ferrell, Taylor N.
149 Gunja, Mushtag Z.
224 Lee, Marisa R.
230 Leonard, Shelley D.
251 Marquez, Laura R.
270 McQuaid, Nicholas L.
273 Mehrbani, Rodin A.
283 Montoya, Elisa D.
286 Morales, Esther F.

```

```
 ‘Detailee $134999.
 Detailee $152635.
_ Detailee $155500.
 Detailee _ $140259.
 Detailee _ 3136134.
Detailee ____ $132009.
 Detailee i $136134.
 Detailee $100206.
 Detailee $105211.
 Detailee $123758.
 Detailee $132009.
 Detailee $117637.
 Detailee ; $132009.
 _ Detailee $162400.
 Detailee $108717.
 ‘Detailee $116535.

```

```
287 Morales, Ricardo O.
314 Parker, JaLynda L.

347 Riesen, Peter A.

```

```
368 Samuelson, Heather F.

384 Sharma, Avin P.

```

```
416 Thurston, Robin F.
443 Wheeler, Seth F.

```

```
BIL. i

```

```
   L. ‘Detailee __ $108717.
  A. Detailee $148510.
 Heather F. Detailee _«$123758.
  P. Detailee —__-$119238.
Robin F. Detailee ____-$119238.
Seth F. Detailee $225000.
om 2

```

```
           | 2013 Report to Congress on Whi |
READY 22 OF 460 RECORDS FOUND

```

```
an filter on even more columns. We could even build filters that search a range of
or even a few characters inside a text field.
filter is a temporary view of data in Excel. If we want to create a permanent copy we
py our filtered results and then paste them into a new sheet.
 these filtered rows by left clicking on the 1 for Row 1 and then dragging down to
. Right-click anywhere on your selected data and pick Copy. If you’re successful,
e pulsing dotted bars around your cells.

e White House.

red records selected.

e a new sheet by clicking on the plus button near the active worksheet tab at the botw put your cursor in Cell A1 of the new sheet and Paste. Success! The new data with
lees now appear in our new sheet. Widen the columns so you can see all the data.
 the sheet and close it.

```

```
GROUPING AND SUMMARIZING

 We will now use pivot tables to answer questions about methamphetamine sa
that were seized by law enforcement agencies worldwide in 2007 and later tested by th
Drug Enforcement Administration. Download the stride_meth.xlsx Excel file on the
website. The author obtained the spreadsheet from the DEA website at http://www. j
gov/dea/resource-center/stride-data.shtml and modified it for this exercise. The
extracts the data from its System to Retrieve Information from Drug Evidence II, an
mation system used to monitor trends in drug law enforcement operations (Drug Enf

ment Administration, n.d.a). The DEA delays release of the data, because it says that i

not want to jeopardize active investigations (Drug Enforcement Administration, n.d.
 Open the spreadsheet and note that it has 6,300 rows, including one for headers.
columns include the state or country where the methamphetamines were seized, ho
law enforcement agency obtained the drugs, the name of the drug, the potency on a
of 1 to 100, the weight, and the year and month in which the drugs were seized. We'l
pivot tables to determine which state or country had the greatest number of seizures
mitted to the DEA, which had the most meth by weight and which had the most p
meth on average.
  Insert a pivot table into a new worksheet. Drop State/Country into the Row
area and the state and country abbreviations appear in alphabetical order. Then
State/County in the Value fields area and Excel counts the number of times each st
country appears in our data. AK for Alaska is at the top with 19.
 To put the state or country with the highest number at the top, click in any of th
with a number, then right-click and pick Sort | Sort Largest to Smallest in the popup

California (CA) is tops with 1,385, followed by Texas (TX) with 580. These stat
number 1 and 2 in total population, so it shouldn’t surprise us to see them at the top
list. If we wanted to put these numbers into context, we would generate rates for all
states using their populations.
  Use File | Save As to save a working copy of the spreadsheet. Return to Sheet 1
ate a second pivot table. Drop State/Country into the row field area and then Po
into the value field area. Excel automatically sums the potency, which is not h
because states with more test results could have higher sums. We want to genera
average, instead, to see which states or countries had highest potency in their
meth. Click on the drop-down arrow to the right of Sum of Potency and select Av
from the list that appears.
In Chapter 6, we used Excel’s pivot table function to run simple integrity checks
gave us a better understanding of the values in each of our data columns. Here, w
use pivot tables to answer “How much?” or “How many” questions about categ

that we find in our data. For instance, we could have used pivot tables to deter
whether detailees or employees on the White House staff get paid more on aver

  Sort the numbers descending to see which state or country had the highest pot
Australia (AS) is at the top with 85 percent, followed by Saipan, Mariana Islands (T

```

```
                                       PivotTable Fields

of ‘State/< ntry 2 1 Choose fields to add to report
    ett :

                                                           Drag fields between areas below:

                                              % FILTERS i Be COLUMNS

           Sheet2 | Sheets | @

rug Enforcement Administration.

t table puts data into groups and summarizes.

might want to have some context here so we can see if some of the higher averages
ave resulted from one high test. So add the count of the State/Territory as a second
ue field. Save your spreadsheet.

         _ Source Name: Potency
         Sc es enna cy
  ' Custom Name: (Average of Potency

       Summarize Values By
                  roa ibility Mode} » Excel PRVOTTABLE TOOLS fo
         PAGELAYOUT © FORMULAS) =«(DATA = REVIEWS VIEW = Ei Maps”) DESIGN Herzog, David A |

                          eh Bicer PP §
 - Be | Ber Connections Refresh Cha eae Data Actions PACE Tess Ree IO ee 7

                              Fitter ¥) Tools
     INSERT ANALYZE

       —. aN a onl SR Fields, Thems, & Sets ~ ts #4 oe |
Gi redsanes ess Brith ay Group «| 08 Relationships i,

       Aicber Piet Calculations

```

```
:
( .

‘ :

```

```
Choose the type of calculation that you want to use to summarize

data from the selected field

```

```
                                                    PINOTIABLE TOOLS ?7 @ 
                      FORMULAS DATA REVIEW VIEW Esti Maps ANALYZE : DESIGN Herzog, David

                                   General +} FE conditional Forreeingy BP insect ~ i $e
                                        [29 Founat as Table + ao Delete + el + a

                    =e ; iy Cell Stytes ~ oa Formaty & +

Clipboard = % Alignment fi i ¢ j Styles Cells Editing

 8? 3 75.7833333333333

```

```
c

```

```
PivotTable Fields

Chane fields to edd te reports

ivi State/Country
() MethAcq
  Drug

```

```
  esses

Ww RBwWN VDA

```

```
                                6 { Potency
59.74420601 i Newt
   55.15 ' Seize Year
54,27383539 || £3 Seize Month

```

```
             53.86781227 |
              53,22727273 52.12135802 i Drag fields between areas below:
             51,60845154 3 i Y FILTERS _ 8 COLUMNS
                $1,25 i n
                 50.875
              49,89054054
                 47.255
             44,73766234 :
         So : i Count of 5. 7
              44,41666667
         Sheets  SheetS  Sheeti | Sheet. ... : {0} Defer Leyout Update

   READY

Source: Drug Enforcement Administration.

Note: Pivot table showing average meth average potency by state or country. Count added to provide context.

  Last, we are going to figure out which state had the most seized meth sent to the
for testing. Go back to Sheet 1 and create another pivot table. Put State/Country int

 |G @ o- = Se, rete wtsx « Eeced PIZOTTABLE TOOLS,

 ze HOME — INSERT  PAGELAYOUT = FORMULAS ~—s— DATA, AMALYZE DESIGN

```

```
 ec gi : if 7 “” 834 Format as Table + a Oetete ~ o) ¥ Sort Bi Fide
| % ciaa = 7S ad ‘ & ice ar} Bij Conations Formatting» BP insert Be Pio by

```

```
| 5 BI by 4 . = = * «! a on in

```

```
| Cupboard fo f% Abignment % Number 5 Ceti Editing
{i aes ail u tae $+ % > 4B UP Cell Styles + BZ tommat~ LS Fiteer~ Setect~

```

```
             he 974202, 205000002

                        D
                                        PivotTable Fields

SumofNtWwt | | Cheosefieldstoaddte report: a
‘State/Country «| Total ! :
          974,203
          244,856
          241,234
           62,984
          54,330 i
          50,510 i | Seize Month
          37,855
           37,639 i Drag fields between areas bekven
          37,056 i
           34,699 % PLTERS i Y COLUMNS:
          29,513.
          27,336
           24,072
           22,143
          20,741
         “SheetS | Sheeté | Sheett Sh .

```

```
lds area and Nt Wt into the value fields. Excel sums the weights for each
untry. Sort and format the data as numbers using commas. Meth from California

s the most tested by total weight at 974,203 pounds.
 your file and close it.
is chapter, we learned how to manipulate data by sorting, filtering and using pivot
o create summaries for groups. Experienced data users typically use database mangrams, such as Microsoft Access and MySQL, to create these groups and summawever, we can perform many of the same functions using spreadsheets.
 wraps up the data analysis section of the book. In this section, we learned why it’s
nt to place numbers into context, and how to put them in context by comparing
 others. We also learned how to calculate those comparisons as amount change,
 change, percent of total, rates, ratios and averages.

e next section, we dive into how visualization can help reveal patterns in our data
municate our results to others.

UR OWN

he stride_meth.xlsx file, answer these questions for California only: (1) In which
did the DEA receive the greatest number of meth seizures? (2) In which month did

 get the most meth, by weight? (3) In which month was the meth that California sent
EA the most potent? Filter your data and use pivot tables to answer these questions.

```

```
                    Fee
Cae, Jed prio nites al be ni aa
         otha baa a? 40 dye hatter
        ust erivus + cle tr ial

```

```
qi

```

```
>

```

```
: : -—

```

```
        yi vn Giel sate lnayy ot iil] ipod
  a2 itty Miedo So 8) tyeM a ab ACE tacepire bina eA pquor ney ; i Agvr mayer rei
    at ara? gale 7 alsa aici iitio ena ce au,
i bariieeet 5 aia sinls ctl seat cla Fo s pits Zefa sted sole Gudqucrw 2b

                       was LTisarthed pata at Gordo o
 va (TOE UST SAORSE Vlas te
             v one vars Nos galley gets Jon Pench Ape on
r 1s rp ; ty qery Hack Trott) creat tifa tag val we ane bade eda BOE fidgety of Tam

```

```
“hey TOT Seedy WRT AT avs yar ners 2 SA ad

```

```
a bol Sad

```

```
    i OO OL st 0) tis. neaepap
.

```

```
         iJ nao Testa, enpe ai
                                                   i)

                    wwe: ay
                                                2. Aa
f a yte

```

```
                           1 W

                                      ei vy (lav ‘air as SY O85 4 {j Sven

                                                                               p

            le

 Ss

              ;
   »e ; rj sey" stud vey iDtiTsitt Woe sre

          } “ $i i Teas 7 Mv t

        i oe Vase

          _

         ~~ “

— — i


            = Voit:
                            i

                  _

```

```
 easier to display data and share them with others. But data visualization has been
 used for decades as a means to help understand data patterns and communicate
 others. The goal of this section of the book is to provide a solid footing in the funls of data visualization. This section will touch on some best practices that have
fined over the years and some options for visualizing data accurately. Additionally,
section we'll learn how to create a number of different types of visualizations using
charting functions and online services offered by Google. We start this section with
 11, where we will explore some principles that will help us better understand data
ation.

VISUALIZATION DEFINED

zation is simply the act of creating charts based on data. We can easily visualize a

ata set, such as a spreadsheet file. Data scientists, using other tools, can visualize

s of more-complex data (sometimes called “big data”) from social networks, such

er and Facebook, to better understand the flow of information about disasters or

ents.

heir simplest, data visualizations can be barebones representations of data. Many
nalysts visualize data just for themselves, so they can get a better understanding of
ta. Sometimes it’s difficult to detect interesting or meaningful patterns by looking

mns and rows of data. In fact, data analysts will often create many different visual that can help show the data from different perspectives, or they will show a subset
ata. The techniques of exploratory data analysis, as promoted by statistician
key, use different types of graphs to get a better understanding (Tukey, 1977).

tatistical programs, such as SPSS, JMP, MATLAB and the open source R, have
tory data analysis functions. Excel’s charting tools allow us to accomplish many of
e basic goals, albeit with more effort.

 want to communicate to a specific audience, we might choose to create an infor graphic—a more elegant representation. We could use a graphic design program
be Illustrator to create a static information graphic, or we could use an interactive
ation tool like Tableau Desktop. The art of crafting information graphics is outside
e of this book. To learn more, [read ] [The ][Functional ] [Art ] [by ][Alberto ] [Cairo ] [(2013), ]
 This by Nathan Yau [(2011), ] [or ] [the ][books ] [of ][Edward ] [Tufte ] [(1983, ] [2006). ]
 ata visualization has been all the rage recently, as Web-based tools have made it
TER 11 VISUALIZING YOUR DATA

```

```
 “Graphics, charts, and maps are not just tools to be seen, but to be read and scrutin
The first goal of an infographic is not to be beautiful just for the sake of eye appeal,

above all, to be understandable first, and beautiful after that; or to be beautiful becau

its exquisite functionality,” wrote Cairo (2013, xx).
  In the words of information design guru Tufte, “Graphics reveal data” (1983, 13).
information designers have gravitated toward Tufte’s ideas, which emphasize simpli
In 1983, he issued his theory of graphical excellence, which includes instructions to

  Show the data

  Induce the viewer to think about the substance rather than about the methodolo
  graphic design, the technology of the graphic production, or something else

  Avoid distorting what the data have to say

  Present many numbers in a small space

  Make large data sets coherent

  Encourage the eye to compare different pieces of data

  Reveal the data at several levels of detail, from broad overview to the fine struct

  Serve a reasonably clear purpose: description, exploration, tabulation or decora

  Be closely integrated with the statistical and verbal descriptions of a data set (Tufte,

Reprinted with permission by Edward R. Tufte, Graphics Press Cheshire, CT.

SOME BEST PRACTICES

Here, then, are some quick guidelines for creating visualizations, whether they’re for
self, another person or a broader audience.

Give your chart a title. Use just a few words to describe what’s displayed. Include the

frame for your data (e.g., “State unemployment rate, 2000-2012”).

Label your chart elements. That includes the vertical and horizontal axes, legends an
other elements.

Include a source line. A source line reminds you about where you obtained the da
youre sharing your visualization, it shows others where you got the data. This is impo
because you want to give others the ability to try to replicate or even challenge your re

Display enough data to provide context. For instance, showing only three years of u
ployment data might mask the fact that the rate had been rising in earlier years.

by the author. Using data downloaded from the St. Louis Federal Reserve Bank’s
is to emphasize the content, and to help it tell a story.

  Let's look at this example of an Excel column chart that was created relatively qu

```

```
3/1/2013

10/1/2012

5/1/2012

12/1/2011

7/1/2011

2/1/2011

9/1/2010

4/1/2010

11/1/2009

6/1/2009

1/1/2009

8/1/2008

3/1/2008

10/1/2007

5/1/2007

12/1/2006

7/1/2006

2/1/2006

9/1/2005

4/1/2005

11/1/2004

6/1/2004

1/1/2004

8/1/2003

3/1/2003

10/1/2002

5/1/2002

12/1/2001

7/1/2001

2/1/2001

9/1/2000

4/1/2000

```

```
-_ ©
=
©
=!
oy
&
>
@
ao)
-~ a
—_ iL

```

```
GDPC1.

htCRefrom Departmof S ot mmurce: p://rri e Ex c Nved rhart. oce lumnt e seal nt, :

```

```
hange DPal S. arterly 00-2013 Percent change

```

```
and includes “the output of goods and services produced by labor and property loca

the United States” (Bureau of Economic Analysis, 2014). The U.S. Department of
merce’s Bureau of Economic Analysis releases the data quarterly. We can easily
looking at this chart how the GDP in the United States began shrinking in 2007,
global financial crisis began.

  Note that the chart title says, “Quarterly change U.S. Real GDP 2000-2013.” This
municates to viewers that the data are reported quarterly and expressed in terms
dollars. We prefer to use data based on real dollars because doing so takes into accoun
effects of inflation. The title also signals to viewers they are looking at data spannin
years 2000 to 2013.
 Our source line, placed just below the title, tells the viewers that the BEA prod
these data and gives them the link on FRED, in the event that they’d like to retrieve th
themselves.
 The vertical axis label shows viewers that the change is reported as percent, wit
axis scale ranging from 2.5 percent growth to 2.5 percent loss.
 The horizontal axis label tells viewers that each column represents the first da
quarter. The labels themselves mention the specific dates. Note that the St. Loui
adjusts all quarterly dates to the first date of the quarter (Federal Reserve Bank of St.

n.d.). Our data contain more than a decade of information, which is enough to sho
big picture of GDP growth and loss during those years.
 Now that we’ve seen some of the best practices in action, it’s time to learn which
options are the best for displaying different kinds of data.

```

```
   L
### `|`

        hen creating data visualizations, part of the challenge is picking the right type
        of chart. Excel gives us around a dozen options, everything from the simple pie
        chart to sparklines. So, the big question becomes, Which option should we
      That is, which will be the most appropriate and communicate the best? The
     depends on the kind of data that we want to visualize. Here is a guide to the chart
      and the data types that they’re best suited to display.

     IZING DATA WITH CHARTS

      rts are the best tool for showing proportions of the whole. These charts are the
      quivalent of using a spreadsheet to calculate the percent of total. As long as you use
      number of categories, pie charts can make it easy for people to understand pro      . For instance, this pie chart from a report by the U.S. Consumer Financial Protec      eau shows us that nearly half of complaints received by the Bureau were about
      s, at 48 percent. Complaints about credit cards, the next largest category, came
      percent of the total. Student loans made up just a sliver at 3 percent (Consumer

      l Protection Bureau, n.d.a).

                     WE Res
               a | r Consumer loan
                           3%
                                                                         ; | Student loan
                             8%
                                  Credit
                                  reporting

            48% Bank
                  Mortgage Y account .
                                    and service

                      21%
                          Credit card *Includes
                                 money
                                      transfers

         rfinance.gov/reports/a-snapshot-of-complaints-received-3/
        snapshot of complaints received. (n.d.). Consumer Financial Protection Bureau. Retrieved July 11, 2013, from http://
    TER 12 CHARTING CHOICES

         hart showing proportion of consumer complaints reported to federal authorities.

```

```
 Likewise, this pie chart from a federal spending report tells us an awful lot
how the U.S. government spent its money in fiscal year 2012. Roughly two-t
(66 percent) of all spending was by the Social Security Administration, Departme
Health and Human Services and the Department of Defense (Financial Manage

Service, 2013).

               Net Cost: FY 2012 ($3.8 trillion)

                  All Other

```

```
                                Department of
Interest on
Treasury Health and

```

```
Securities Held Human Servi:

```

```
by the Public 23%

```

```
      6%

   Department of
   Veterans Affairs
     9%
                                         Social Securit
                                         Administration
                                      22%
            Department of
              Defense
             21%

Source: Current report: Combined Statement of Receipts, Outlays and Balances. Financial Management Service. (n.
Retrieved from http://www. fiscal.treasury.gov/fsreports/rpt/combStmt/cs201 2/outlay.pdf

Note: 3-D pie charts distort data. The slice for the Department of Defense in the front looks bigger than the one for the Dep
of Health and Human Services in the back, but the Department of Defense’s share is actually 2 percentage points less.

  Pie charts have come under attack lately because they sometimes fail to make th
more understandable (Hickey, 2013). As Hickey suggests, avoid the temptation to
3-D pie charts (such as the one above) because they can distort results and make som
slices appear bigger than they ought to be.
  Vertical column charts are ideal for showing change over time when you have di
time-series data. Discrete time-series data are reported at defined intervals. Some
ples include the quarterly GDP data we saw visualized in Chapter 11, monthly unem
ment figures and annual four-year college tuition costs.
 We can even create stacked vertical column charts to show proportions over tim
instance, this chart visualizes not only the increase in enrollment at full-time d
granting institutions, but also the growing share of women attending college.

```

```
    =Males # Females

                                                Proj. proj. proj.

 tional Center for Education Statistics, Department of Education, Retrieved from http://nces.ed.gov/programs/digest/
t1.

ked vertical column chart showing proportions over time.

tered column charts allow us to compare categories over time by placing columns side
This clustered column chart provides a different view of our enrollment data. This
ws even better how the gap between female and male students has been widening.

    &Males #Females

                     004 2005 2006 2007 2008 2009 2010 2011 2015 2020
                                                  proj. proj. proj.

ered vertical column chart compares categories over time.
tional Center for Education Statistics, Department of Education, Retrieved from http://nces.ed.gov/programs/digest/
t1.

```

```
http://www.erh.noaa.gov/pbz/hourlyclimate.htm.

  Degrees F

      VAM MMM Ma Aaa ahahaha

                        Time

Source: National Weather Service, Retrieved from http://www.erh.noaa.gov/pbz/hourlyclimate.htm.

Note: Line charts show continuous time-series data, such as temperature readings.
 Line charts are a great choice when we have continuous time-series data. Contin
data are those that represent processes or conditions that occur continuously, such
outdoor temperatures. The use of the line is more appropriate because it suggests an

National Weather Service in Pittsburgh, Pennsylvania, on September 1, 2013, fou
ing phenomenon. In this chart, a line represents the hourly temperatures recorded

```


```
     =
      <x
     °
     ©
       N 1:00 AM AM 2:00 AM 3:00 4:00 AM
                              PM 11:00

Source: National Weather Service. Retrieved from http://www.erh.noaa.gov/pbz/
hourlyclimate.htm.

Note: More than one data element displayed on a line chart.
    90 90
                                80 3

                               70 £
  >
  Q 60 60 $

                                         a


 u 80

  2 70
                                     j=

                                                                     cc)
   o 3

```

```
  If we have more
one data element
we'd like to chart t
context or make com
sons, we can add
lines. With this chart
about relative hum
by the hour in Pitts
have been added.
that these data are p
on the same scale

temperature.
 We can choose
zontal bar charts

```

```
  Doctorate

  Master’s

 Bachelor's

 Associate’s

        0 500,000 1,000,000 1,500,000

tional Center for Education Statistics, Department of Education. Retrieved from http://nces.ed.gov/programs/digest/
dt11_283.asp?referrer=report.

 categories shown on a horizontal bar chart.

e did with the vertical columns chart earlier, we can show proportions by using
bars. The first chart below shows not only the total number of degrees, but also the
ion of women and men who earned them. We could also use a clustered bar chart
are the degrees earned by men and women in yet another way.

                                         & Male
 Doctorate | —
                                          & Female

 Master's |

 Bachelor’s

ssociate’s | 
       0 500,000 1,000,000 1,500,000

ing proportion with a stacked bar chart.
rks well because we have a small number of categories. It could get difficult to
and if we had too many.
ber of higher-education degrees granted in the United States 2009-2010. This

tional Center for Education Statistics, Department of Education. Retrieved from http://nces.ed.gov/programs/digest/
 data that are categorized in just a few ways. For instance, this bar chart shows us

dt11_283.asp?referrer=report.

```

```
    Doctorate |. @ Male
                                         @ Female

     Master’s

    Bachelor's

   Associate’s

                      500,000 1,000,000

Source: National Center for Education Statistics, Department of Education. Retrieved from http://nces.ed.gov/programs
d11/tables/dt11_283.asp?referrer=report.

Note: Comparing categories with a clustered bar chart.

 Scatterplots help us show whether we might have a relationship between two
variables. For instance, we could plot SAT or ACT scores against college freshman
point averages to see whether there is any relationship between high scores on those
dardized tests and student performance. The scatterplot below uses the crime data
Chapter 9 and shows the relationship between property crimes (the horizontal axi

violent crimes (the vertical axis). In general, we see that as the number of property

increases, so does the number of violent crimes. The chart includes a linear trend lin
shows the central tendency of the data. Any point that’s well above the trend line
sents a city whose violent crime numbers are higher than expected. Excel uses a stat
calculation called linear regression to determine the position of the linear trend li

      15,000 20,000 25,000 30,000 35,000 40,000 45,000 50,000
                         Property

Source: Federal Bureau of Investigation. Retrieved from http://www. fbi.gov/about-us/cjis/ucr/ucr-publications#Crime.

Note: Scatterplots for comparing variables.

```

```
                                     High
                                    Opening
                                      Closing
                                     Low

ahoo Finance. Retrieved from http://finance.yahoo.com/q/hp?s=G00G &a=07 &b=19&c=2004&d=10&e=6 &f=20138g
=66.

k chart, otherwise known as a boxplot.

klines are “intense, simd-sized graphics” (Tufte, Male, all education levels {
                              | Less than high school completion
) that area relatively new | High school completion\3\ .
 option in Excel spread- | _.SeBe.cotlest: no degree.
    kli d : Associate's degree ; ee

 Spar ines are place a Bachelor's or higher degree ..... |
individual cells and take | Bachelor’s degree ..
e of numbers or text.In | i | Master's : or ve higher a degree $
e can create line, bar and [Penatey all education levels
 sparklines. The spar- rae eal i ot ere aoe
                             | High school completion\3\
 n the spreadsheet here / Some college, no degree
ow median income has __ Associate's degree
                 | Bachelor's or higher degree ...., i
 from 1995 to 2011 for | ~~“ gacne1or's degree
d women, and by level of | | Master's or higher degree ..... | aN.
n. A sparkline is an
t tool for helping comterns in large data sets. Note: Sparklines are repetitive charts that fit inside cells.
              Source: National Center for Education Statistics, Department of Education.
sing prices, as represented by the inner bars. The outer lines display the high and
es.
k charts—or boxplots—can be used to visualize the performance of stocks over
any times, we see stock price data visualized as a line chart, but the stock chart can
 more detail than a simple line chart. Here we see monthly Google stock opening

```

```
                            se rac “
                           Z
                             & ~~
                       Garth F ge
            ee < 3 8 non : 4 : \ : 1 E Baexeg Wiweal

  a ee es WSN 4 : ‘ . bad
        Suthton (e) Sw = eet oO ae na ’ ~ Z : : . : yops % Fei
            Patk

                           Pe
                       y
                               & p ae Ss
               2y % ag * —
       Longview. Pare ase [wha ] & ty ie 3 © tene

            * < = < Ws Ss 2 yy » f
            A — * Baidegy
          & Twrnlekes * : . Sy:
          & ” OF-Leash Aree

                                               & New Ha a Ws £ New Hav

                                                     & Sugat oS ae
                                                                               #

                                  Gey x ie Yas
                          Garg Crews ReS BW

Source: Google maps; City of Columbia, Missouri.

Note: A Google Fusion Table map.

 Now that we know which charts are the best for our data, we’re going to learn
next chapter how to build these charts in Excel.

ON YOUR OWN

Find three charts or information graphics in print or on the Internet. Write a criti
each: How easy is it for you to understand? Was the chart the best choice for the data?
or why not? Did the chart have the necessary elements? Make sure you provide a c
each chart or a URL for it.
can use online programs, such as Google Fusion Tables. This Fusion Table map show
  Finally, a map is often the best way to visualize geogra
themselves and understand what’s happening near them. Out of the box, Excel is u
to create maps but can do so using plug-in programs. We can use geographic info
tion system (GIS) programs, such as ArcGIS or Quantum GIS, to create data maps.

location of residences where the Columbia (Missouri) Police Department respond
reports of nuisance parties. Most of the points are concentrated in areas with large amo

of student housing.

```

```

 ow we will use Excel to create the charts that we saw in Chapter 12. Download the
 charting.xlsx file from the website for this book and open it. It contains seven

 worksheets, which have labels on their tabs. The first one is Degrees conferred.
 t, like all of the others, has data that have been edited and formatted so it’s easier

 the charts. Often, the data we want to use for our charts are stored in columns or
 t aren’t neighbors. That makes it challenging to highlight just what we need. The
rces are noted at the bottom of each sheet and include URLs for download.

ART

rt by creating a pie chart to show the proportion of degrees conferred in 2009-2010,
 a from the National Center for Education Statistics. The first two rows hold the data we
 build the chart. It has the degree
 in the first row and the numbers
TER 13 CHARTING IN EXCEL

```

```
category in the second.
ight cells Al through E2. Then
e Insert tab and click on the droprow for the pie chart button.
t the 2-D Pie option and Excel — Source: Microsoft Excel for Windows 2013.

he chart just like that. Note: Excel chart type selector.

```

```
PivotChart

     «

```

```
     A 8 Gea <p E F G H I j K L ‘
  1 Associate's Bachelor's Master's Doctorate
  2 2009-2010 849,452 1,650,914 693,625 158,558
  3 Associate's Bachelor's Master's Doctorate
  4 Male 322,916 706,633 275,197 76,605

  5 Female 526,536 943,381 417,828 81,95%

  o SOURCE: National Center for Education Statistics
 10 http://nces.ed.gov/programis/digest/d11/tables/dt11_283.a:

                                                           w Associate's % Bachelor's * Master's # Doctorate

ional Center for Education Statistics, Department of Education.

```

```
 The chart is not very descriptive as it stands, so we are going to add some element
will help viewers make sense of it. Double-click on the chart title at the top; now we c
it. Let’s change the text to, “College degrees conferred 2009-2010”. The legend,

contains the color key for each degree, is at the bottom of the chart. Let’s move that
right of our pie. Click on the legend to resize and move it.

  Finally, we'll add a source line below the pie so we can cite the NCES and provide
to the data. Click on the Format tab and then look for the Insert Shapes tool on t
Select the Text Box tool and then use your cursor to enter the source information
first line and the URL on the second. Resize the pie chart area if there is not enough
for the source line. Our finished chart should look like this:

      College degrees conferred 2009-2010

                                      f2 Associate’s

                               © Bachelor’s

                                      f& Master’s

                                @ Doctorate

Source: National Center for Education Statistics, Department of Education.

Note: Pie chart with title, legend and source line.

 Examining this chart, we can see that nearly half of all degrees awarded were bach
degrees. Associate’s degrees make up about one quarter; master’s and doctorate de
combined, make up another quarter. We've done some work, so let’s create a working
of this file by picking File | Save As.

HORIZONTAL BAR CHARTS

again, highlight cells Al through E2. Pick Insert Bar Chart, then select 2-D Bar, Clu
Bar. Excel creates this chart. We could edit this if we wanted by modifying the
We can also use horizontal bar charts if we want to compare our degree categories.

```

```
  Doctorate

  Master’s

 Bachelor’s

 Associate’s

           500,000 1,000,000 1,500,000 2,000,000

 tional Center for Education Statistics, Department of Education.

 ontal bar chart.

 adding a source line. Excel has automatically chosen to use degree numbers in

nts of 500,000 for the horizontal axis labels.
t below our table we have another that breaks down the degrees earned by sex.
t cells A4 to E6. Insert a Bar Chart and pick Stacked. That will create the same
th four bars, this time showing the shares earned by women and by men.

 Doctorate |] Male
                            & Female

  Master's |

 Bachelor’s

ssociate’s |

          500,000 1,000,000 1,500,000 2,000,000

tional Center for Education Statistics, Department of Education.

 ed horizontal bar chart shows proportions.

 saw in Chapter 12, the clustered bar chart allowed us to see the differences more
So let’s build that. Instead of creating a new chart from scratch, we can right-click
hart area and then pick Change Chart Type. . . . Pick Clustered Bar from the box
ears and Excel creates this chart. It’s much easier to see the differences between the

th this one.

```

```
        Doctorate Male

                                        {3 Female
         Master’s

        Bachelor’s

       Associate’s

               200,000 400,000 600,000 800,000 1,000,000

Source: National Center for Education Statistics, Department of Education.

Note: Clustered horizontal bar chart compares categories.

COLUMN AND LINE CHARTS

Now that we’ve charted categorical data from one point in time, we are going to lear
to chart time-series data. Remember that we have two choices when charting time
data: (1) column charts for data that were recorded or reported at discrete points in

and (2) line charts for data that measure a continuous phenomenon, such as the wea
  We'll use the GDP data on the GDP sheet to create our first column chart. The
data are reported quarterly, as reflected by the dates stored in column A. Column B t
the percentage change from the previous quarter.
 Highlight Al through B54 to grab the data that we need to create our chart. Insert
Clustered Column chart. Excel creates a barebones chart that lacks a lot of descr

information. Also, we see that our horizontal axis labels have been stuffed into the m
of the chart, making them difficult to read.

    fo) o| t+MOMWOOR [
    ois) aaa es © gi ae awe
 0.50 9-9- -O-O-O-O-O-S O—-m—-O-O-O-O
   SN NE NE NENT NTN QQ NE
 -1.00 SS = o-oo ot AAR Se PS Se AS SS a eae Ont Ree Om Oo
                                                  = - —

Source: Department of Commerce, retrieved from FRED.

```

```
 going to clean this chart
iscover some tricks that we
ater. First, let’s fix the posithe horizontal axis labels.
e labels and then go to the
Axis Box that appears. Pick
mn chart button and open
s item. Use the drop-down
ow as the label position.
 we will label both of our
hart viewers can understand
ch means. Pick Add Chart
 from the Design tab and
s Titles | Primary Vertical. A
 appears. Enter “Percent

 Likewise, create a horizon label that says “Quarter”.

the chart to “Quarterly
U.S. real GDP 2000-2013”.

```

```
 Format Axis

  AXIS OPTIONS Y TEXT OPTIONS

            od
    <7 ~' > ee. a Tew ce
 > O is

   » AXIS OPTIONS

   TICK MARKS

  4 LABELS

    Label Position Low

   » NUMBER

Source: Microsoft Excel for Windows 2013.

Note: Format axis settings.

```

```
we want to insert a source line. Right now we don’t have enough room at the bothe chart. We can resize the chart plot area to free up some space. Click on the plot
 resizing handles appear. Drag them to make the plot area smaller.

 it looks much better, and someone can understand what it means.

rly change, U.S. real GDP 2000-2013

                                  l
             (Chin

       ot+ONnNOORRMDMDOADVOOrrANM
Ce Soe oo Sle Oe SOOO [OOO ] [Oo ] [T ] [Be ] [OS ] [8 ]
S S SS ee ee SH SRO iS
SwortortrortoroeovororoerseverserotrsF ic — +" i — cq = — br at Ta — ae
                    Quarter

partment of Commerce, retrieved from FRED.

```

```
 Our next column charts will be those in which we'll display fall enrollme
U.S. degree-granting institutions of higher education over time. Go to the Enrollme
to find these data from the NCES. Row 1 holds the categories for years. Rows 2 and
enrollment data that the author has reformatted so the vertical axis labels appear pr
when charting. The numbers are in millions, rounded up to whole numbers. The o
numbers appear in Rows 4 and 5 and are reported in thousands.
  Highlight cells Al through S3 and insert a Stacked Column chart to create this

Our chart shows increased enrollment since the 1970s, with women increasing their

                   2003 2004 2005 2006 2007 2008 2009 2010 2011 2015 20
                                                  proj. proj. pro

Source: National Center for Education Statistics, Department of Education.

Note: Stacked vertical column chart.

 Use Change Chart Type and pick Clustered Column. We see that more men
women had enrolled in 1970. Sometime in the 1980s women surpassed men. We c
that the current gap is expected to widen even more during the coming years.

     @Males @Females

    1970 1980 1990 2000 2002 2003 2004 2005 2006 2007 200:

```

```
 turn to charting using continuous time series data. Go to the PBGH Weather

hich has hourly temperature and relative humidity data from September 1, 2013;
or downloaded these data from the National Weather Service. First, we will plot
variable, the temperature. Then we will add the humidity readings.
t cells Al through B25 and insert a 2-D Line Chart. This chart appears. It looks like
eratures bounced around a lot on that date. That’s because the bottom value on
cal axis is 66 degrees. We can set that to a lower value to render a more accurate
of the temperature on that date.

  AM 12:00:00 AM [1:00:0] AM 2: [0] 0:0AM 3: 0 0:0AM 4: 0 0:0AM 5: 0 0:0AM 6: 0 0:0AM 7: 0 0:0AM 8: 0 0:0AM 9: 0 0:00 AM 10:00:0AM 11: 0 PM 12:0:0 0 PM [1:00:0] 0:00 PM 2: [0] 0:0PM 3: 0 0:0PM 4: 0 0:0PM 5: 0 0:0PM 6: 0 0:0PM 7: 0 0:0PM 8: 0 0:09:PM 0 0:00 PM 10:00:0PM 11: 0 0:00

 tional Weather Service.

 chart. Note that the temperatures appear more extreme than they were because the vertical axis starts at 66 degrees.

t the vertical axis labels and then, in the Format Axis box, set the Bounds

m to 40. The chart now looks much better.

       Format Axis

```

```
AXIS OPTIONS ¥

```

```
TEXT OPTIONS

```

```
& 2 i ill

“4. AXIS OPTIONS

  Bounds

   Minirnium

  Maxirnum

  Units

  Major

   Minor

```

```
      AM 12:00:00 AM [1:00:0] 2:AM [0] 0:0AM 3: 0 0:0AM 4: 0 0:0AM 5: 0 0:0AM 6: 0 0:0AM 7: 0 0:0AM 8: 0 0:0AM 9: 0 0:00 AM 10:00:011:AM 0 PM 12:0:0 0 PM [1:00:0] 0:00 PM 2: [0] 0:0PM 3: 0 0:0PM 4: 0 0:00 PM 5:00:0PM 6: 0 0:0PM 7: 0 0:0PM 8: 0 0:0PM 9: 0 0:00 10:00:00 PM 11:00PM

Source; National Weather Service.

Note: Temperature variation smoothed, thanks to vertical axis minimum lowered to 40 degrees.

 Next we will create a chart that has the temperature and relative humidity. Select
Al through C25 and insert a 2-D Line Chart. We get this chart, which shows both, p
on the same 0- to 100-point scale. Of course, we could modify that scale if we wanted

Source: National Weather Service.

Note: Line for relative humidity added to chart.

SCATTERPLOT

For our next chart we will again plot two variables. As we learned in the previous ch
scatterplots can help us see whether there is a relationship between numeric variables.
the Crimes worksheet, which has data about property crimes and violent crimes in citi
populations 500,000 to 999,999. Highlight the cells containing the data—B1 through

```

```
    5,000 10,000 15,000 20,000 25,000 30,000 35,000 40,000 45,000 50,000

ederal Bureau of Investigation.

terplot of property and violent crimes.

ge the title to “Crimes 2012”. Label the horizontal axis “Property” and the vertical
olent”. No city has fewer than 16,000 property crimes, so change the minimum
for that axis to 15000. Our chart looks better now.

                Crimes 2012

      20,000 25,000 30,000 35,000 40,000 45,000 50,000
                   Property

derai Bureau of Investigation.

erplot with new horizontal axis settings and labels.

 add a finishing touch, a linear trend line. Excel uses a statistical function called
egression to draw the line that’s a best fit for the data. Points that are very high
he line represent cities with more violent crimes than we would expect, based on

```

```
      16,000

      14,000

      12,000

      10,000

       8,000

       6,000

       4,000

       2,000

        15,000 20,000 25,000 30,000 35,000 40,000 45,000 50,000
                           Property

Source: Federal Bureau of Investigation.

Note: Scatterplot with linear trend line showing the central tendency.

STOCK CHART

Pick the Google stock sheet, which contains monthly performance data downloaded
Yahoo Finance. Note that when we create stock charts our data need to be ordered pro
date, opening price, high price, low price and closing price. Date represents the first day o
ing for each month. Highlight cells Al through E15 and Insert Stock, Surface or Radar
(the one that looks like a spiderweb). Then pick the Open-High-Low-Close option. Chan
vertical axis label’s minimum bounds to 600 to eliminate the empty space at the bottom.
also allows us to better distinguish how the stock performed in each month. We see that
of our inner bars, which display the closing and opening prices, are filled in. That’s Excel
of telling us that the stock closing price fell below its opening price in those months.

     OS RO ROD Re
    VARA Vv 9S Vv ‘e) v Vv v 9 Vv v ce)
   fees ORO SN UN RN ae SS
                  Open High Low Close

```

```
INES

p up this chapter by learning how to create sparklines. Pick the Median income
d data from the NCES. We have nine columns of salary amounts in different years
 than 50 categories. The procedure for creating sparklines is a little more involved
the other charts we’ve created so far. Click on the Line button in the Sparklines
d then set the Data Range to B2:J67. Next tell Excel where to put the sparklines.
tion Range needs to be K2:K67. Click OK and we’ve placed our sparklines in the
.

 ons, all education levels $36,900 $39,190] $37,990 $38,140] $37,970 $37,600] $39,800 $32, 560| $37,950
 than high school completion 23, 23,640| 23,660 22,320] 23,780 22,330| 21,450 21,660
 school completion\3\,680 32,650] 32,130 32,290] 31,420 31,320 31,370 30,850
 college, no degree ¥ 37,680] 36,140 35,020| 35,660 33,390] 34,760 33,940

 iate's degree > 39,180} 39,220 37,720) 37,750 37,540) 37,648 38,256) 37,

 lor's or higher degree, $2,240} 56,530 50,050} $3,510 52,180} 52,250 $0,270} S80,

 helor's degree, 52,130) 46,990 48,520| 48,630 48,060] 47,170 46,420

 ter's or higher degree i. 62,590} 57,520 $5,790) 62,390 $7,400] 62,050. 56,380

 ional Center for Education Statistics, Department of Education.

 ines.

 it for our lesson on making Excel charts. In the next chapter, we'll wrap up this

 n data visualization with a look at Web-based tools that allow us to create and

rts.

R OWN

d the Excel spreadsheet charting2.xlsx from the book website and use the data
 on each tab to create the best chart possible. Make a note of why you chose the
r chart type.

```

```
         we —_garintae
                          Dae at eo, eredih
        ehA

                     g we B) eka Tulhe seio-gpall Vig s nd rik ents

                 pail
       Veal SON yoott cee ees an ofl ya Ope

 vin

bavily ri ai H SOR amnesty WA sraly cis Gal U1 Aivoyaes 08
 xii? oti al netted » pit F sil] nn oil og OF mint yA Sib
 Wri)

     ns aes Hii sinin ping La

         : ee die dese may fina es Laue ti

                      vai) Itai sone Naa of A
                         mt

                          ;

            ¥"

                   ‘ ‘

                                                            (>

} ;

                                       ?

                      js

                                                               =) ~~
                                        *

```

```
          Pes peru 2

     aes eens
          He Lar pean 1 ghar oytioh
                            A> casas te std
Pee NY 4009 Geet iw Py Cpclalirend
    ea ur
        , ACE NT <e citer ry Skeid aS S16 5 Avtin Hea aie? ered ARAN, TY
                                   Sbaa
               anythin (MRE daedaiiieie eink act baie
                a

```

```
,
               paige tp es ih enon
             = bow the saat

```

```
| ih enon
aS} U Siti ia ea MR f

```

```
    sy ath aS} Siti ia
                            Re i
hry Hy U ea MR le anh ch Thais

```

```
= ae i Tae ‘ie rte ¢ aT ody ie Sif FB ob

            = fe | at

                            ae =

                           i
                                          ee

```

```
 s we saw in the last chapter, Excel is a powerful tool that we can use to create data
 visualizations for ourselves. Thanks to an explosion of Web 2.0 tools in the past

 several years, we have an abundance of options available for creating visualizaat we can share with the world. Numerous Web-based charting platforms have
, providing plenty of choices. Some of them have gained traction and developed a
er base, while others have been shuttered by their developers. In this chapter, we
 a look at some of the tools that have been around the longest and thus are more
 be around in the coming years. These tools are powerful and allow us to create
f the same charts that we can make in Excel. Anyone with more-advanced Web
and development skills can create even richer data visualizations.

re we learn about the tools, we're going to look at a few examples of interactive data
ations that have been created with government data.
 visualization shows us how much money has been budgeted and spent by the Cook
 Illinois, government over 20 years. Cook County includes Chicago and a number

  Cook County Budget

      Expiore Cook County's mudget trom 1993 to 2012 and learn how the money i being spent, Read tore or check oul the FAG

         Sam
          MB sadgeres WF seene

     2012 Cook County Budget $3,347,088,302.00 $0.00
                                      +9.6% budgeted from 2011

      Fund YXQ0UY? Budgeted vs. spent ;
       Si Suble Satety Fund $1,178,878,128.00 LL

      fi Bessh Fund $894,133,047,09 LL $A

     i Special Purpose Fund $714, 268,525.00 el

      SCaptal worovements $291 £38,590,00 3

       Eh Corperate Fund S183.018, 928,08 no) —

       + At the end of dee cunent focal Year. at sudit will be onriuced urd a rence iaued with thy Heal expenditures for gan deputinant, Laws sce

 ere’s the money going? (n.d.). Look at Cook: Brought to you by Cook County Commissioner John Fritchey. Retrieved
20, 2013, from http://lookatcook.com/
TER 14 CHARTING WITH WEB TOOLS

```

```
of the city’s suburbs. The line chart shows us that the city spends less money than
budgeted in any given year. The bar chart at the bottom right shows us that the

Safety Fund accounts for most of the spending, followed by the Health Fund. If we cl
the plus signs to the left of any of the fund names, we can drill down and get more de

data about that fund (Look at Cook, n.d.).
  This visualization from the federal Consumer Financial Protection Bureau sho
mortgage application activity across the United States, using a map and column charts
CFPB uses Home Mortgage Disclosure Act data for the visualization. We can set pa
ters to create customized charts that display mortgage activity for the Metropolitan

tical Areas that interest us. Here, the author created a clustered column chart that
mortgage activity in the MSA that includes Las Vegas, which was one of the country’

test real estate markets a few years back (Consumer Financial Protection Bureau, n.d

  Number of originations by 30,000 eee :
  loan type

  Many loans are insured or guaranteed by
  government programs offered by the Federal
  Housing Administration (FHA), the Department of
  Veterans Affairs (VA), or the Department of
  Agriculture’s Rural Housing Service (RHS) or 15,000
  Farm Service Agency (FSA). All other loans are
   classified as Conventional.

  Metropolitan Statistical Area @

    Las Vegas, Paradise -NV

```

```
Loan Type BH Conventional
           Mi FHA
           Miva

```

```
        2011 2012

LAS VEGAS, PARADISE - NV

```

```
             MIRHS Conventional SEN FHA
                          WU ib, ME RHS

    * All visualized data are for first-lien, owner-occupied, 1-4 family and manufactured homes.

Source: Home Mortgage Disclosure Act. (n.d.). CFPB. Retrieved December 20, 2013, from http:/(www.consumerfinance.go

Note: Online data visualization using government mortgage application data.

  Like many major U.S. cities, Houston has a 311 reporting system to help resident
businesses request services, such as sidewalk or pothole repairs. All of the reques
service, whether they’re made by telephone or online, are entered into a master dat
In addition to using the data to manage the requests, the city makes them available
and allows members of the public to create visualizations with the data. For example,
map created by the author shows that Nuisance on Property is the most common
for complaints, at nearly 9 percent of all cases (City of Houston, n.d.).

```

```
               Volume of Service Requests Received - Tree Map

 f Date Service Request Received:
 -00-23 at Qh Sea

 :

 :

 nt . BO Aad & Con TANCE
   mk ; ‘ y GY + Porson

 quest ny Type c le YB smecky Regex
ee A BH PeircSte e r » Se.
                                                               IBS sthorza Hew Bari.
                                                       Wh Axcorated Recycies

 strict

       °


 nt District
  Ses

                                                       Ye Cane in tesinele:
                                                          WB cove in sce
                                                       Be Cave in Sveet
                                             $ Cian of Read Diter:
                                                       BS Ciean Ravtion o %...
                          ; < SZ HG Civen Stoo Sewer
 on Zipcode y y ; {BS clew view Cosinet..
       = : é J > Bl Cosnpteint Form Re
 h z Conse aboul a Pr
                                                        $8 Contuines PMecemert
                                                        §S comsine: Protiem
                                           SP cout Surtece Spar
                                                      SS cusb Repair due te.
                                            @ Cumert stus or O.. a
                                                                           INE Paconrnae Hecnaued tn

 ity of Houston 311 Data Visualizations. (n.d.) Retrieved December 20, 2013, from http://performance.houstontx
 shboards

 active tree map visualization of calls to Houston 311 center.

 VISUALIZATION OPTIONS

 many options for creating visualizations that we can post on the Web and share.
f them come from established technology companies, such as Google and IBM.
come from relative newcomers like Infoactive and Infogram.
le Spreadsheets offer one of the easiest to use and most robust charting options.
 with a Google Drive or Gmail account can create these spreadsheets and charts. In
mple, the author has uploaded the charting.xlsx file that we used to create Excel
n the previous chapter.
 highlighting the desired data range, we just click the Insert chart . . . button and
Spreadsheets launches the Chart Editor, where we can customize our chart. After
 the chart, we can pick Publish chart .. . from the drop-down arrow at the top right.
ere we can get an embed code for an interactive chart that we can paste into a blog

 Web content management system.

```

```
       Chart Editor

          Start Charts Customize

     Data - Sect ranges. :
        ‘Degrees conferred'tA3:E5 Ea Chart title

        Combine ranges:

       ¥ Switch rows / columns

       ~ Use column A as headers:

          Use raw 3 as fabels:

       Recommended charts - More »
           —

                                  yerbos? axisLett title
 ht tin
 =~

Source: National Center for Education Statistics, Department of Education.

Note: Stacked bar charts in Google Spreadsheets.

             Publish chart

              Select a publish format I

               Paste this into any HTML page:

                 <script type="text/javascript” src="//ajax.googleapis, conmvaja
                 xistaticimodules/gviz/1 O/chart js"> {dataSourceUrn’"/
               docs. google.com/spreadsheetiiq7key=0AlekPTayybHGdE
              FNNURS2RmZngyd0FhaVidende aGc&transpose=1&headers=
            1Srange=A2%3AESSgii=0Spub=1","options {ttle TextStyie":{"b
                 old” true,"cotor’:"#000"16}, "vAxes”[(useFormat "fontSize”:
                FromData”™ true,“ttie’s","minValue”:null, “view Windo veMode™:n
                 ull, view Window” -null,"maxValue” null ZuseF ormatFromData”:
               true}}, “booleanRole”-“certainty*,"ttie”:"Degrees conferred 2009                2010","height”:262,”animation”{’duration”.500},"egend” “right”,
                “width”:494 tfocusTarget’ "series “hAxis” fuseFormatFromDa
                 fa™:true, “ttle™:",“minVValue“null, “view Window" :{"min”: null :
             tax’ ;,"maxValue” nul, "tookip’:,"sStacked false},"state”:
                Qh. wiew" 4). "eDefaul\/isualizaton” true, “charilype”"Barc A
                hart®,"chartName”:“Chart 1°3 </script>

Source: Google Spreadsheets.

Note: Embed code used for publishing Google Spreadsheet chart.

 Fusion Tables are the next step up in Google’s data visualization tool kit. Fusion
technically are still in the experimental phase, but they’ve been a popular visualizatio

```

```
t resulted:

 charting-GDP

  imported at Fri Deo 20 12:24:50 PST 2013 from charting.
  Edited at 2:24 PM
his example, the author used the existing Google Spreadsheet with the chart and imported the table for the GDP change. After changing some settings,

```

```
SS SSN RAL SSO SSMS

```

```
 File Edit Tools Help = Rows 1 ~

FE vo ters applied

  a 4 1-560f56 % »

```

```
| SSO Sica SSMS py

Ee

```

```
 Date
  7/1/2003
  10/1/2003
  4/1/2004
  4/1/2004
  7/1/2004
  10/1/2004
  1/1/2005
  4/1/2005
  7/1/2005
  10/4/2005
  4/1/2006
  4/1/2006
  7/1/2006
  10/1/2006
  4/1/2007
  4/1/2007
  7/1/2007
10/1/2007
  4/1/2008
  4/1/2008
  7/1/2008

```

```
Change

  1.68950257759395
  1.13429041423658
 0.598120614829544
 0.765069892552146
 0.877416907962389
 0.843756778251758
  1.69337023308502
 0.546091544800783
 0.816099088677587
 0.553421628920655
  1.2134706373504
 0.310729802562838
 0.087721702897552
 0.780586672509655
 0.065903902598113
  0.76995674934309
  0.67378634235084
 0.365425158116657
 -0.67150792539394
 0.495454972676136
 -0.495016433743957

```

```
Real GDP
  13374
 13525.7
 13606.6
 13710.7
  13831
 139477
 14100.2
 44177.2
 14292.9
  14372
 14546.4
 14591.6
 14604.4
 14718.4
 14728.1
 14841.5
 14941.5
 14996.1
 14895.4
 14969.2
 14895.1

```

```
partment of Commerce, retrieved from FRED.

```

```

Source: Department of Commerce, retrieved from FRED.

Note: GDP data in a Google Fusion Table chart.

 ManyEyes, from IBM, is another well-established data visualization platform that’s
used. After creating a free account, users can upload data by copying them from a sprea
and pasting them into a box. The author used the city crime data in the Charting sprea
to create this scatterplot to show the relationship between property and violent crimes

```

```
n x ° — (=) [o) je) [o)
nN
® 8,000
=
‘i 3) 6,000
pu
=
2 4,000
©
> 2,000
   10,000 20,000 30,000 40,000 50,
     Property crime 2012
                        Property crime 2012 °* °°
                                       10,000 30,000

```

```
— (=) [o) je) [o)

```

```
8,000

6,000

4,000

```

```
Source: Federal Bureau of Investigation.

Note: Crime scatterplot on ManyEyes.

EVALUATING WEB VISUALIZATION PLATFORMS

When evaluating Web-based data visualization platforms, it helps to consider po
strengths and weaknesses.
 On the plus side, most of these Web tools are available at no cost. We don’t
purchase or license any software, unlike when we want to use a commercial progr

```

```
ver, there are some drawbacks to consider when using these tools. One big conon is that you often surrender control of your data when you make it available on
tes. So make sure that you read the terms of service, which is a legally binding

nt that defines the relationship between you and the website. Also, read the privacy

t, which outlines how the website uses personal and other data that are submitted
.
 other drawbacks include downtime for Web applications. Even the most robust Web
s fail on occasion. Whom can you call at Google if your Fusion Table charts suddenly
 A related risk is that the visualization platform could be taken offline completely.
fact, happened several years ago to Swivel.com, a popular visualization platform.
Eyes’ and Google’s offerings remain good choices because of their longevity and
inside well-established tech companies.

NG FUSION TABLE CHARTS

this chapter, we are going to create some charts using Fusion Tables. You'll need to
ure that you have a Google account with Google Drive. Next, go to your Drive and
 the charting.xlsx Excel sheet. Convert it to the Google Docs format, if you are
d. Now we are ready to create some Fusion Tables based on the data.
nch Fusion Tables by visiting http://www.google.com/drive/apps

usiontables and clicking on the Create link. At the Import new table screen, pick
Spreadsheets. Select charting from your list.

      Select a spreadsheet

    | Spreadsheets Spreadsheets

                                                                  LAST MOTFIED:

                 4 charting 4.01 PM

                       (2) Mews Developer Jobs Dec20

                        [2] Webtogs/sites on Data-Driven Journatism Dec8

                       {41 international and Local Data Audits and indexes 0021

                      BBO - Grilifeier SonyDADC 24.Juni

                         (4) Asset and income/Expense

                        Open Data Sites & Tech Platforms

                         Or pane 4 wed eaters here:
her plusis that the service hosts our data. We don’t need to worry about getting and
 the data online. Moreover, the visualization platforms allow us to access our data
r we are in the world. So, there are some very strong benefits to using these services.

```

```
  First, we will create a line chart using the Pittsburgh weather data. Then, we will c
a column chart using the GDP data.

  To create the weather line chart, select the charting-PBGH Weather link, then cli
Next button to import the table.

               Import new table

                 Select the sheet to impart.

                shartina-Dearees conferres chatting GDP = sharting-Enratiment | charting-PBGH Weather ©

            Time : : “Temp A 2S
                 Time Tamp
               00:00 78

                                        | 1.06:00 75
                                      | 2.00:05 23
                  3:00:00 72
               4:00:00 1
               5:00:08 72
                                            a)

             New to Fusion Tables?

                Take a peek! Piay with @ data set or try 3 tutorial.

Source: National Weather Service.

Note: |mporting Google Spreadsheet for a Fusion Table.

  In the next screen, confirm that the column names are in Row 1 and click Next.

               import new table

                   Colurnn names are in row 4 »

                            Time
                              9:00:00
                              4:06:06

                            289-00

                              3:00:00
                         40000

                              5:00:00
                            $00.00

                   GM Ao WN @ SOA7.60.00
                          B9B00

                              9:00:00
                              40:00:00

                Rows datene tha header rom wit be ignored

             New to Fusion Tables?

               Take a peet! Play with 2 data set or tutoriat, try 9

Source: National Weather Service.

```

```
       impart new table

                   charting-PEGH Weather om,

       Allow export 2 2

        Attribute data to

        Attribution page fink

      Description “Imported at Mon Dec 23 14:05:48 FST 2013 from charting.

                           For exariple. what would you fike to remember about this table in @ year?

      New to Fusion Tables?

       Take 2 peek! Play with a data set or tutorial by 4

Google Fusion Tables.

adata box for Fusion Table. Metadata are data about the data and are a guide for others.

     charting-PBGH Weather

         imported at Mon Des 23 14:05:48 PST 2013 from charting

         Edited at 40% Pha

                                    _prvrsernetereemmentsttteternneeterieniieimstisorpsnnte tinauansuiialsssiéiiiee
       File Egit Tools Help | =Rows1~ ff Cards 1 Pe

           7 tio filters applied

            1-26 0f26 » »

National Weather Service.

a imported into a Google Fusion Table.
he final screen, we can add metadata that can help us and others understand what’s
Fusion Table. Instead, we'll just click Finish and our table appears.

k on the red plus sign and then Add chart. We now have the beginnings of a chart
screen. Change the chart type to Line chart.

```

```
   Configure categorical chart

   Category

   Sammarize data?

   Valves
  #Temp

    < Retotee Hurnisity

Source: National Weather Service.

Note: Google Fusion Table temperature line chart.

```

```
2:00 AM 160 AM

```

```
 We're not done: we still need to modify a number of our settings. Under values, let
Relative Humidity. Also, change Maximum categories to 26, because that’s the numb

rows we have in our data table. Much better! We're through, so click the Done butt

finish.

   Configure categorical chart

    Category

     Tene >

   Summarize data?

   Vames:

   Tere
   # Relatve Huricity

   Sort by

     Tome

   Maximem categories


                                                     32:00 PM 200 PM

Source: National Weather Service.

Note: Relative humidity data added to line chart.

 Now we'll create a column chart for the GDP quarterly change, which will be just
more complicated. Return to your Drive and select Create, then Fusion Table. (
option is missing, select Connect more apps and then search for it.) Go through the
steps as above to select the charting spreadsheet and then import charting-GDP. We
have this at the top of our screen:

```

```
harting-GDP

ported at Mon Dec 23 16:44:01 PST 2013 from charting.
ited at 6:44 PM

                           sain ide ic a enlace
            | = Rows1~ | icons.

                                                                                     esas sesso Re

  4 4-560f56 >» »

te Change Real GDP
4/1/2000 : 42365.2
4/1/2000 1.88836411865558 12598.7
7/1/2000 0.127790962559618 126148
10/1/2000 0.532707613279646 12682
4/4/2001 -0.286232455448662 12645.7
4/1/2001 0.530615149813759 127128
7/1/2004 -0.304417594865009 12674.1
10/1/2001 0.24538231511508 127052
4/1/2002 0.939772691496392 128246
4/1/2002 0.546605742089425 12894.7
7/1/2002 0.48081770029547 129567
10/1/2002 0.047851690631094 129629

 epartment of Commerce, retrieved from FRED.

 data in a Google Fusion Table.

want to display only the results from 2004 on, so click on Filter and then Date.
g boxes appear. Enter “2004” in the first box and click Enter to display from that
 Now we're ready to create the chart. Click on the plus sign and then select Add

 Column chart from the options. Enter 40 into Maximum categories box, because
 40 rows in our table. Click Done and we have our chart.

```

```
Source: Department of Commerce, retrieved from FRED.

Note: Google Fusion Table vertical column chart of GDP change.

  Let’s do one more thing: generate an embed code that we could use to post this on
or other website. Select Tools in the menu and then Publish. . . . This generates
HTML code that we could copy and paste. Of course, we would need to change our s
for the Fusion Table to Public for this code to work properly.

              Publish

                This table is private and will not be visible. Change visibility

              Send a link in email or 1M
           hitps:www. googie. comMusiontables/embedviz?containerid=goc

              Paste HTML te embed in a wedsite
           <iframe width="600" height="300" scrolling="no" frameborder="n

             Width 500

               Height 300

                 include data atirimsion

Source: Google Fusion Tables.

Note: Embed code for Google Fusion Table chart.

  This chapter concludes the data visualization section of the book. As we saw a
is pretty simple to create interactive charts using Web visualization tools like
Fusion Tables. This is just an introduction to quickly creating basic charts.

ON YOUR OWN

Find data that you can upload to a Google Spreadsheet and use them to create a

```

```
 t this point in the book, we have achieved all of our goals for navigating the world

 of data. We have learned how to identify, obtain, evaluate and clean data. We’ve

  learned how to analyze and visualize them. Indeed, we've covered a lot of ground
 previous 14 chapters. We've accomplished these goals using software that’s widely
le and easy for novices to grasp. It really is eye-opening to see what we can do with
 ools.

 ever, if we want to elevate our data analysis and visualization, we will need to learn
 Most people who analyze and visualize data use more than spreadsheets. They also
ograms like database managers and statistical software. Here, we'll take a cursory
 these programs and how they can help us understand data even better.

BASE MANAGERS

se managers, such as Microsoft Access and the open source MySQL, are designed
k with large files. Some database programs can easily work with millions of rows o
something that’s impossible with Excel’s default installation settings. (Windows

 can install an Excel Add-On called PowerPivot, which extends the program’s

ities.)
 Access, which is probably installed on the Windows computers in your campus’

ter labs, the program file size limit officially is 2 GB. However, the program will start
g erratically when the file size nears 1.5 GB.
er database managers are more forgiving. In MySQL, a table may have 2 GB to
 bytes (each terabyte has 1,000 GB). Databases may have more than one table, so the
es can be huge.
ny database programs use Structured Query Language to issue commands. Develn the 1970s, SQL is a powerful, yet relatively simple, database language that’s taught
ersity computer science classes.
me database programs, such as Access, also allow users to build queries using
cal user interface. These GUIs make query building much easier than writing
Unfortunately, they also deter users from discovering the benefits of learning

 de.
PTER

     NEXT LEVEL
    15 TAKING ANALYSIS TO THE

```

```
 There are some good arguments in favor of learning SQL. First, anyone who learns
on one database manager can apply that knowledge to another. So if we learn SQ

Access, it would be easy to write queries in MySQL with just some minor modificat
Second, anyone who learns SQL can talk intelligently to database administrator
government agencies, making it easier to negotiate for offline data. Third, learning
forces database users to think logically about their data and how they are structured.
 Database managers are usually relational; that is, they allow us to create relation
between the tables in our databases. This is important because database administrato
government agencies often store data in multiple tables.
 Database managers are especially powerful because they allow us to extract sp
pieces of data that interest us. For example, using a database manager and the Fe
Election Commission campaign contribution, data we could find all the contributio
Barack Obama or Mitt Romney that came from our zip code in the week before the No
ber 2012 general election. Another example: we could select records of high-pot
(90 percent or greater) meth samples in the STRIDE data from the Drug Enforce

Administration. Here’s a look at the STRIDE data, as imported to Microsoft Access.

 eas > : :
 Ea HOME CREATE: «s«EXTERNAL DATA =—sDATABASE TOOLS «= ADMINS) «ssELDS.Ss TABLE

  My mi _Y SL Ascending VF Selection i se New =D Totals # =
   — El Descending “SlAdvenced~ — Bsne D spaiting >- .
  ves : Ste Refresh a Find
         <= Pans Remove Sea “YW Toggie Fate Aly 2X Delete - ElMore~ Ry Ac®%-2- S== &
  News Gipboars Sort & Fite: Records Find Tat Formatting S
  All Access Obje... © « |=) Swvcmem\  eae = D State/fCount- MethAcg - Drog > Potency - ONTWE OC Seize Year + Seize Month   —— . AL s “-METHAMPHET/ 8 7402007
   SB ssc meth ™ ™ s s METHAMOHET: METHAMPHETS 34 38 391 87 2007 2007 1
                    xy x METHAMPHET/ 8 18 2007 1
                  NV . DEXTROMETHA BY 103 2007 1
              cA s DEXTROMETHA 96 4 2007 1
                  cA s DEXTROMETHA 68 225 2007 1
              cA $ DEXTROMETHA 31 28 2007 2
              cA s DEXTROMETHA 73 430 2007 1
               ™ s OEXTROMETHA 96 453 2007 1
                WA $ METHAMPHET: 53 2007 1
              oc P DEXTROMETHA 37 55 2007 1
               x > METHAMPHET! 45 26 2007 i
                wy Pp METHAMPHET: 10 Q 2007 1
                ™ L METHAMPHET/ 2 10 2007 1
               ™ t METHAMPHET/ 0 11 2007 i
               ™ L DEXTROMETHA 33 1 2007 i
              az s DEXTROMETHA 78 13 2007 i
              cA s METHAMPHETs y= $6 2007 1
               =MO $ METHAMPHET: 53 13 2007 2
              MT s METHAMPHET: 8 © 2007 1

                NM S. _. METHAMPRET: a AO BT ee ene
                   Record Md of 9293 | ne = Search

Source: Drug Enforcement Administration.

Note: Meth seizure data shown in Microsoft Access. Access is a Windows-based desktop database manager.

 If we run the following SQL code, Access returns only those records where
potency is 90 percent or greater.

```

```
 ride meth § 3) Query1 \

 ECT *
 M Stride_meth
 RE Potency>=90

een
 ] Stride meth | Query

```

```
Source: Microsoft Access 2013.

Note: SQL to retrieve data about meth that’s 90 percent potent or greater.

```

```
           DEXTROMETHA
           DEXTROMETHA
           DEXTROMETHA
           DEXTROMETHA |
           DEXTROMETHA
           DEXTROMETHA            DEXTROMETHA
           DEXTROMETHA
           DEXTROMETHA
           DEXTROMETHA
           'DEXTROMETHA _
           METHAMPHETs :
           _DEXTROMETHA “111 2007
            DEXTROMETHA 111 2007
           DEXTROMETHA 14-2007
           DEXTROMETHA 1.2007
           _DEXTROMETHA 207
           DEXTROMETHA 2007
           _DEXTROMETHA 4 2007
           DEXTROMETHA 1 2007
           DEXTROMETHA 2007
     YPONHAHH O HDHYHDE Fo VVUVXOAWDHHA H W 2 2007

                                           bh B ef tP h kok pa f Te a u ok t k of k k h e
cord: 4 4 1

Drug Enforcement Administration.

ery results showing meth that’s 90 percent potent or greater.

abase managers are also great tools for grouping and summarizing data. They allow
enerate results that are similar to pivot tables. For instance, we could use grouping
mmarizing to answer this question: Which state had the greatest number of meth

s? This SQL code generates the answer: California, with 1,385 seizures in 2007.

 meth) BI Queryt
T [state/country], Count(*)
 stride_meth
P BY [state/country]
R BY Count(*) DESC Source: Microsoft Access 2013.

                Note: SQL for grouping and summarizing.

```

```
                        4 '

    cal }

Source: Drug Enforcement Administration.

Note: Grouped and summarized results, similar
to those in a pivot table.
ee eer
 FE] Stride_meth 9) Query \
  state/count: ~ | Expri001 ~

```

```
 Data analysts often use database manager
create grouped and summarized reports like thi
  Finally, database managers allow us to link
together through a process called joining. So, if w
a database from a government agency that’s sto

more than one table, we can stitch the data
together to better make sense of it.
 We can see that database managers are
powerful programs that afford a lot of flexibili
data analysts.

STATISTICAL PROGRAMS

Though Excel has some statistical functions tha
be activated with the Analysis Toolpak a

```

```
program, most advanced data analysts prefer to use more robust standalone stati
programs, such as IBM’s SPSS, SAS or the open source R. Statistical programs can

generate a bunch of descriptive statistics, such as minimum, maximum, mean, med
count and sum. They can all run tests that allow us to see whether there’s any stati
relationship between variables. These are called inferential statistics.
 Some statistics programs, like SPSS, have GUIs that make generating statistics p
simple. However, it can be difficult to understand the output and determine whethe
results are meaningful, or statistically significant.
  In this example using SPSS to analyze the STRIDE data, the author has created a h
gram that shows the values for potency. A histogram is a chart that shows the distrib

          Wie s < E
       TAL S METHAMPHETAMINE HYDROCHLORIDE, ISOMER UNDETERMINED
      ‘TKS METHAMPHETAMINE HYDROCHLORIDE, ISOMER UNDETERMINED
         S METHAMPHETAMINE HYDROCHLORIDE, ISOMER UNDETERMINED
        KY X METHAMPHETAMINE HYDROCHLORIDE, ISOMER UNOETERMINED
          P DEXTROMETHAMPHETAMINE HYDROCHLORIDE
        CA S DEXTROMETHAMPHETAMINE HYDROCHLORIDE
        CA S_ DEXTROMETHAMPHETAMINE HYDROCHLORIDE

```

```
 S_DEXTROMETHAMPHETAMINE HYDROCHLORIDE
A'S METHAMPHETAMINE HYDROCHLORIDE, ISOMER UNDETERMINED

 L METHAMPHETAMINE HYDROCHLORIDE, ISOMER UNDETERMINED
 L METHAMPHETAMINE, ISOMER & SALT UNDETER

```

```
BSALBSSKoLBS.

```

```
                                 Mean = 42.67
                                      Std. Dev. = 34.534
                              -|N=6,299

 (2) So oO


               Potency

Drug Enforcement Administration.

h potency histogram in SPSS.

edical and social science research, analysts will often run descriptive statistics first
rstand their data. Then they will run inferential statistics to test their hypotheses.
tering statistics takes time and study. Most universities offer a great number of
asses, from the introductory to the advanced.

ces can also read Seeing through Statistics by Jessica Utts (2014), or The SPSS
o Data Analysis by Marija Norusis (2011). Both take clearheaded approaches to
g stats.
ember, though, that even if we do not step up to these more advanced programs,
still turn data into knowledge using the tools and concepts explored in this book.
t takes is a little practice and curiosity.
s in a column. The histogram includes information for the overall mean, standard
on and or count (N). The standard deviation is a statistic that reports how spread
 distribution is.

```

```
             - =

= — ~ ~ 7

           ~ =

                   Das

                — >

                                      y

                                               ity,

                         Pe “

```

```
ENDIX DATA TOOLKIT

  nyone who wants to work with data needs to have some basic tools: spreadsheets,

  text editors and data cleaner. These are the tools used in this book, along wit
  some other options.

ADSHEETS

 oft Excel comes as part of the standard Microsoft Office installation for Windows
ac. It’s installed on most university PC labs, as well as on many student laptops. Thi
uses Excel 2013 for Windows.

W 6- c-=: ~ Book’ ~ Excel 2? e - Sx

 e HOME © INSERT PAGE LAYOUT FORMULAS 7 DATA REVIEW VIEW : POWERPIVOT ; Herzog, David ~ 3)

                      Sg General > FE Conditional Formatting SF Insert > 3 Sy~ |

                                        = $ + % 9 E¥Formatas Tabley @X Delete > ly Mr
                            EF Cell Styles ~ 3 Formaty S~

                                                     Styles Celts Editing

 crosoft Excel 2013 for Windows.

el 2007 and later can open spreadsheet files with more than 1 million rows and more
 6,000 columns. Older versions of Excel (2003 and earlier) can only handle files wit
an 65,000 rows and 256 columns.

```

```
  More-recent (2008 and 2011) versions of Excel for Mac can open the same larger
as their Windows counterparts. Earlier versions of Excel for Mac share the same limi
their earlier Windows counterparts.
 Another great spreadsheet option is the open-source program Calc. You can downl
Calc as part of the free OpenOffice (https://www.openoftice.org/) or LibreOffice (htt
www libreoffice.org/) software suite. Calc runs on Windows and Mac computers and
ports large files (more than 1 million rows by 256 columns).
  Google Spreadsheets might be a good option for working with smaller files—there
20 MB limit for files that are uploaded and converted. Furthermore, you can have
400,000 cells. So if you have a spreadsheet with 40 columns, you are limited to 10
rows.
  Pivot tables in Google Spreadsheets are primitive when compared to Excel or Cale.
Google Spreadsheets shine at handling live data feeds from the Internet and allowing
to collaborate with others.

TEXT EDITORS

Text editors allow us to examine our text-based data files. In this book, we use Notepa
for Windows (http://notepad-plus-plus.org/), a free program. If you run into probl
trying to open large files, you might have to use other text editors, such as the free Pilot

Lite (http://www.pilotedit.com/) or the open-source Vim (http://www.vim.org/do
load.php).
  For Mac users, the free TextWrangler (http://www.barebones.com/products/te
wrangler/) and TextMate (http://macromates.com/) are good options.

DATA CLEANERS

We are using OpenRefine (http://openrefine.org/) in this book to clean data. OpenRef
is an open-source program for Windows and Mac computers. One of the creators of Op
Refine has said it should work comfortably with data files of up to 10 columns by 100
rows (Huynh, 2011).

```

```
     Glossary

thm: A set of steps that a computer uses to solve a problem.

numeric: A method of computer encoding that uses a mixture of text and numbers.

t change: The raw change from one point in time to another. Formula: new
r — original number.

 The American Standard Code for Information Interchange, which was developed
 and is used to represent text on all computers in the United States. ASCII text is the
ortable data format and comes in two main styles: delimited and fixed width.

tands for Active Server Pages, Microsoft’s scripting language. Web forms that have
tension use the script to pass data between the form and databases.

reports: Official reports that investigate the operations of government agencies.
reports can be used to uncover data held by these agencies. The U.S. Government
tability Office examines federal agencies, while state auditors examine state
s.

art: Charts that display data using horizontal bars. Good for displaying data that
o a few categories.

marks: Points of comparison that help make data more meaningful. These can be
al—or within a data set—or external.

e smallest unit of computerized data, literally a binary digit. Eight bits make up one

ference: An address that refers to a cell’s position in a spreadsheet, using the
ction of the column letter and row number.

l tendency: The average or number that’s used to best describe a set of numbers.

es include the mean, median and mode.

Stands for Cold Fusion, Adobe’s scripting language. Web forms that have this
on are using the script to pass data between the form and databases.

```

```
CKAN: An open-source Web portal that’s used for government open-data platf
Users include the federal government's Data.gov.

clustering: A function of data-cleaning tool OpenRefine that uses algorithms to id
similar text values.

column chart: Charts that display time-series data using vertical columns. Goo
displaying events that occur at well-defined, discrete points in time.

concatenation: Merge two or more text values using spreadsheets or other program
Excel, the concatenation character is the ampersand (&).

CSV: Short for comma-separated values, a type of delimited ASCII file. Sometimes us
a file extension.

data: Any computerized file that uses columnis and rows (a tabular structure) to org
information that’s represented as text, numbers and dates.

data documentation: Detailed data description that allows users to more
understand and work with data sets. Also referred to as data dictionary, record layou
layout or metadata.

data integrity check: A systematic examination of data that occurs before the ana
used to uncover shortcomings in the data.

data_notebook: A text or word processing file in which you record information
your data sources, as well as any data cleaning or analysis performed.

data portal: A Web platform used to distribute data; usually administered by govern
agencies.

database managers: Computer software designed to work with large data sets tha
stored in multiple tables. Examples include Microsoft Access and the open-source My

dBASE: A popular database file format used by a number of commercial database man
programs.

decennial census: An attempt to count every person in the United States that takes
every 10 years, those years ending with a “0.” The most recent decennial census was in

delimited text: An ASCII text file that uses special characters to mark the locati
column breaks.

delimiters: ASCII characters that are used to mark the location of column breaks. Com
and tabs are the most common, but others can be used.

Drivers Privacy Protection Act: Passed in 1994, the DPPA is a federal law that res
access to state driver’s license records.

E-FOIA: Stands for the Electronic Freedom of Information Amendments. Passed in

systems.
this law requires federal agencies to post on the Web lists of their major inform

```

```
y Educational Rights and Privacy Act: Enacted in 1974, FERPA is a federal law
arantees the privacy of student educational records.

tension: The second part ofa file name, coming after the period. Most file extensions
ee characters long.

width text: A type of ASCII text file in which all of the data are arranged into
s.

aphic data: Data files that can be displayed and analyzed using geographic
ation system programs.

aphic information system: Computer program that’s capable of displaying and
ing geographic data. Examples include ESRI’s ArcGIS Desktop and the open source
um GIS.

nment 2.0: A movement that started in the late 2000s that sought to use Web and
 computing technologies to increase citizen engagement.

cal user interface: A GUI is an interface that allows users to interact with a
er program visually.

 Insurance Portability and Accountability Act: HIPAA is a federal law enacted
 that makes personal health records private.

ram: A vertical column chart that’s used to show the distribution of values in a
t.

ntial statistics: The branch of statistics whose aim is to test a hypothesis about an
population based on the analysis of data taken from a sample.

ation graphic: Data visualization that is designed to communicate with a specific
e. Often created using design programs like Adobe Illustrator.

hart: Chart that is used to display time-series data that are continuous, such as
ature readings.
 An OpenRefine function that provides a list of all data values in a column and the
r of times each appears. Similar to a pivot table in Excel.

 regression: A statistical procedure that can be used to create a trend line for data
yed in a scatterplot chart.
 on charting.
atory data analysis: A systematic method for understanding data that relies
 code: HTML code that allows users to take content from external websites and
 it into their own blog or content management system.

rame: Large, powerful computer systems that can run more than one process. These
ers, which have been around since the 1960s, typically are employed by government
s and companies.

```

```
mean: The arithmetic average, which is calculated by adding a set of numbers and
dividing by the number of cases.

median: One of the averages. The middle number in a set of numbers that’s or
smallest to largest. If there are an even number of numbers, the median is the mean

two middle numbers.

mode: One of the averages. The number that appears most frequently in a data set.

Notepad++: A free text editor that is capable of handling large files and showing h

ASCII characters, such as tabs.

open-source software: software that is free in terms of cost and licensing.
the underlying source code is available to anyone who wants to examine or contr
to it.

open data: Data, usually provided by government agencies, made available at no cos
without restrictions on use. Often found on open-data portals.

open government: An initiative in the late 2000s that sought to increase govern
transparency, in part by making more data available to all, including Web and m
application developers.

outliers: Extreme values in a data set. May be inaccurate.

parse: Carve out a portion of a larger text string. Used in data cleaning.

percent change: Used to express change in terms of a percentage. Formula: (new nu
— original number)/original number.

percent of total: Used to show individual portions of the whole. Formula: indiv
share/total.

Perl: An open-source programming language that is sometimes used to clean data.

PHP: An open-source scripting language. Web forms that have this extension us
script to pass data between the form and databases.

pie chart: A chart best suited for displaying proportions of the whole.

pivot table: A spreadsheet feature that allows users to generate summaries of data
on categories and numeric values.

primary data: Data that are collected by researchers. The data usually are collected
a representative sample of the entire population.

Python: An open-source scripting language that is sometimes used to clean data.

rate: A statistic that controls for population. Usually expressed in terms of a sta
population, such as 100,000 people. Formula: number/population* 100,000.

```

```
ds retention schedules: Documents that provide detailed guidance to government
es about how long they should keep particular records.

 An open-source scripting language that is sometimes used to clean data.

rplot: A chart type that shows the relationship between two variables in a data set

dary data: Data that are collected by people other than ourselves.

s: Not as powerful as mainframes, these networked computers are usuaily dedicated
 task.

a: Seattle-based company that provides open-data platform services to government
es.

lines: Small charts that are placed inside individual Excel spreadsheet cells.

dsheet programs: Computer software, originally developed for accountants.
dsheets store data in tables and allow users to run mathematical calculations.

ard deviation: A statistic that reports how data values in a column are dispersed.

ardize: To convert variations (often misspellings) of a data value into one correc

 chart: An Excel chart type used to display opening, closing, high and low stoc

tured Query Language: SQL is a programming language used to manipulate dat
abase managers.

ary statistics: Statistics that provide a snapshot ofa data set. Includes counts, sums
erages.

ditors: Computer programs that are used to view and edit ASCII text files. Programs
e Notepad++ for Windows; TextMate and TextWrangler for the Mac.
ata: Data whose records or rows represent one person, place or thing. These data ar
ummarized.

ualifier: Optional characters that can be used in a delimited ASCII text file to denote
at should be kept intact inside a column.
udent-to-teacher ratio. Formula: student/teacher.
 Used to generate a number that expresses the relationship between two things, suc

r — original number.

to Columns: Spreadsheet function that allows users to carve data stored in one
hange: The amount of change from one point in time to another. Formula: new

n into multiple columns.

```

```
TextMate: A free and open-source ASCII text editor for Macs.

TextWrangler: A free ASCII text editor for Macs.

time-series data: Data that are reported at different points in time. Discrete time
data are used to store information about things that occur at well-defined points in
such as quarterly reports of the U.S. GDP. Continuous time series data are used to
information about phenomena that can occur at any time, such as temperatures.

trend line: An element of a scatterplot chart that shows the best fit of all of the po
Often based on a statistical procedure called linear regression.

visualization: A graphical display of data, created to help better understand it.

-xls: Excel spreadsheet file extension for original format.

.xlsx: Excel spreadsheet file extension for newer XML-based files. Introduced with
2007.

XML: Short for Extensible Markup Language, which stores and transports data. Ex
newer file format (with an .xlsx extension) is based on XML.

zip file: A compressed file, usually having a .zip extension. Must be unzippe
decompressed before its contents can be used.

```

```
     References

 R. (1989). From Data to Wisdom. Journal of Applied Systems Analysis, 16: 3-9.
 for Healthcare Research and Quality. (n.d.). Medical Expenditure Panel Survey. http://meps
rq.gov/mepsweb/
y General of Texas: Greg Abbott. (n.d.). How to Request Public Information. https://www
g.state.tx.us/open/requestors.shtml
exas.gov. (n.d.). Dangerous and Vicious Dogs. austintexas.gov/department/dangerous-andious-dogs

E. M., & Ghaziri, H. (2004). Knowledge Management. Prentice Hall.
 of Alcohol, Tobacco, Firearms and Explosives (ATF). (n.d.). ATF Fact Sheet: National
ponse Team. http://www.atf.gov/publications/factsheets/factsheet-national-tracing-center
ml
 of Economic Analysis (BEA). (2014, Aug. 28). Gross Domestic Product, Second Quarter 2014
cond Estimate); Corporate Profits, Second Quarter 2014 (Preliminary Estimate). http://www
a.gov/newsreleases/national/gdp/gdpnewsrelease.htm
 of Justice Statistics (BJS). (n.d.). All Data Collections. http://www.bjs.gov/index.cfm?ty=dca
 of Labor Statistics (BLS). (n.d.). Mass Layoff Statistics. http://www.bls.gov/mls/
 of Transportation Statistics (BTS). (n.d.). BTS Publications. http://www.rita.dot.gov/bts/
_publications
A. (2013). The Functional Art: An Introduction to Information Graphics and Visualization.
 Riders.
ia Department of Education. (n.d.a). 2010-11 Lorenzo Manor Elementary School Reporting
m for UMIRS Data. http://dq.cde.ca.gov/dataquest/Expulsion/ExpReports/SchoolExpRe.
x?cYear=2010-11&cChoice=ExpInfo3&cDistrict=0161309—San%20Lorenzo%20Unified&cC
nty=01,ALAMEDA &cNumber=6002653&cName=LORENZO%20MANOR%20
EMENTARY
ia Department of Education. (n.d.b). DataQuest. http://dq.cde.ca.gov/dataquest/
for Effective Government. (2013). Center for Effective Government Announces Launch: Press
ase. http://www. foreffectivegov.org/center-for-effective-government-announces-launch
 for Effective Government. (n.d.). Risk Management Plan (PRM) Database. http://www
net.org/db/rmp
l Accident Prevention Provisions, 68 CFR, Sec 68 (1994).
f Houston. (n.d.). 311 Performance Dashboards. http://performance.houstontx
v/311Dashboards

```

```
Coast Guard. (n.d.). Accident Statistics: Boating Safety Division. http://www.uscgboating.
  statistics/accident_statistics.aspx
Connecticut Office of Governmental Accountability. (n.d.). Freedom of Information Commiss
  http://www.ct.gov/foi/cwp/view.asp?a=3171 &q=488272
Consumer Financial Protection Bureau. (n.d.a). A Snapshot of Complaints Received. http:/
  .consumerfinance.gov/reports/a-snapshot-of-complaints-received-3/
Consumer Financial Protection Bureau. (n.d.b). The Home Mortgage Disclosure Act. http:/
  .consumerfinance.gov/hmda/
Coy, P. (2013, July 18). The Rise of the Intangible Economy: U.S. GDP Counts R&D, Artistic Crea
  http://www. businessweek.com/articles/2013-07-18/the-rise-of-the-intangible-economy-u  s-dot-gdp-counts-r-and-d-artistic-creation
Cuillier, D., & Davis, C. N. (2011). The Art of Access: Strategies for Acquiring Public Records
  Press.
Department of Agriculture (USDA). 2013, July. Fiscal Year 2012 Farm Service Agency Farm Assis
  Program Payments. USDA, Washington, DC. www.usda.gov/oig/webdocs/03401-0002-11.
Department of Education (DoE). (n.d.). Family Educational Rights and Privacy Act (FERPA). h
  www.ed.gov/policy/gen/guid/fpco/ferpa/index.html
Department of Health and Human Services (DHHS). (n.d.). Health Information Privacy. h
  www.hhs.gov/ocr/privacy/
Department of Justice (DoJ). (1996). FOIA Update: Congress Enacts FOIA Amendments. http:/
  justice.gov/oip/foia_updates/Vol_XVII_4/page1.htm
Drug Enforcement Administration (DEA). (n.d.a). DEA Major Information Systems. http:/
  justice.gov/dea/FOIA/FOIA_TOC.shtml
Drug Enforcement Administration (DEA). (n.d.b). STRIDE Data. http://www.justice.gov
  resource-center/stride-data.shtml
Environmental Protection Agency (EPA). (n.d.a) Emergency Planning and Community Righ
  Know Act (EPCRA). http://www.epa.gov/agriculture/Icra.html
Environmental Protection Agency (EPA). (n.d.b). Risk Management Plan (RMP) Rule. http:/
  .epa.gov/oem/content/rmp/index.htm
epic.org. (n.d.). Drivers Privacy Protection Act (DPPA) and the Privacy of Your State Motor V
  Record. http://epic.org/privacy/drivers/#introduction
Federal Aviation Administration (FAA). (n.d.). Airmen Certification Database. http://www. faa
  licenses_certificates/airmen_certification/releasable_airmen_download/
Federal Emergency Management Agency (FEMA). (n.d.). The Declaration Process. www.fema.
  declaration-process

Federal Highway Administration. (n.d.). Quick Find: Motor Vehicles. (n.d.). http://www.fhw
  .gov/policyinformation/quickfinddata/qfvehicles.cfm

Federal Reserve Bank of St. Louis. (n.d.) FRED FAQ. Economic Research. http://research.stlou
  .org/fred2/help-faq/#graph_formulas
FileInfo.com. (n.d.). Data File Formats. http://www. fileinfo.com/filetypes/data

Financial Management Service. (2013, Sept. 22). Current Report: Combined Statement of Rec
  Outlays and Balances. http://www fiscal.treasury.gov/fsreports/rpt/combStmt/cs2012/outlay
Food and Drug Administration (FDA). (n.d.). Total Diet Study. http://www.fda.gov/F
  FoodScienceResearch/TotalDietStudy/default.htm

Goldstein, J. (2013, July 2). Audit of City Crime Statistics Finds Mistakes by Police. The New
  Times. http://www.nytimes.com/2013/07/03/nyregion/audit-of-crime-statistics-fi
  mistakes-by-police.html

```

```
, S. (2013, March 14). Sunshine Week: University of Kansas responds to “Let’s Break FERPA”
 r. Student Press Law Center. http://www.splc.org/blog/splc/2013/03/sunshine-weekversity-of-kansas-responds-to-lets-break-ferpa-letter?p=4945
 W. (2013, Jun. 17). The Worst Chart in the World. Business Insider. http://www
sinessinsider.com/pie-charts-are-the-worst-2013-6#ixzz2WU7bwULY
 D. (2011). Google Refine Tutorial. http://davidhuynh.net/spaces/nicar2011/tutorial.pdf
niversity Consortium for Political and Social Research (ICPSR). (n.d.). List of Member
titutions and Subscribers. http://www.icpsr.umich.edu/icpsrweb/membership/
inistration/institutions
. (2012, Aug. 28). I.B.M. Mainframe Evolves to Serve the Digital World. The New York Times.
p://www.nytimes.com/2012/08/28/technology/ibm-mainframe-evolves-to-serve-theital-world.html?_r=2&hpw&&gwh=D08AE3D472E69C065942744D18AC8E11
 Cook. (n.d.). Where’s The Money Going? Brought to You by Cook County Commissioner
n Fritchey. http://lookatcook.com/
s Service. (n.d.) Major Information Systems. http://www.usmarshals.gov/readingroom/
 s. html
um, Q. E. (2012). Bad Data Handbook. O'Reilly Media.
m-Webster. (n.d.). Data: Definition. Online Dictionary and Thesaurus http://www.merriamster.com/dictionary/data
ft Developer Network. (n.d.). Introducing the Office (2007) Open XML File Formats. http://
n.microsoft.com/en-us/library/office/aa338205(v=office.12).aspx
l Center for Education Statistics (NCES). (n.d.). Publications & Products. http://nces.ed
v/pubsearch/index.asp?searchcat2=pubslast90&HasSearched=1
l Highway Traffic Safety Administration (NHTSA). (n.d.). Who We Are and What We Do.
tp://www.nhtsa.gov/About+NHTSA/Who+We+Are+and+What+We+Do
l Security Archive. (2007). File Not Found: 10 Years after E-FOIA, Most Federal Agencies Are
inquent. http://www.gwu.edu/~nsarchiv/NSAEBB/NSAEBB216/guidance.htm
 R. (2013, Nov. 8). Telephone interview with the author.
, M. J. (2011). SPSS Statistics Guide to Data Analysis. Pearson.
ssouri.org. (n.d.). Egg Licenses. http://openmissouri.org/data_sets/51-egg-licenses
rets.org. (2014). Most Expensive Races. http://www.opensecrets.org/overview/topraces.
?cycle=2012&display=allcands
, J. W. (2013). Best Practices in Data Cleaning: A Complete Guide to Everything You Need To
Before and After Collecting Your Data. Sage.
 (n.d.). Data: Definition and Pronunciation. Oxford Advanced American Dictionary. http://
donline.oxfordlearnersdictionaries.com/dictionary/data
ment Printing Office (GPO). (2001b). Vessel Numbering and Casualty and Accident

-2001-title33-vol2-part173

, McNeill, R., & Gebrekidan, S. (2013, July 8). Exclusive: U.S. System for Flagging Hazardous
micals Is Widely Flawed. http://www.reuters.com/article/2013/07/08/us-chemical-tieriiorting System, 33 CFR Sec. 173. http://www.gpo.gov/fdsys/granule/CFR-2001-title33-vol2/

SBRE9670K720130708

p://www.gpo.gov/fdsys/pkg/PLAW-109publ8/content-detail.html
ment Printing Office (GPO). (2001a). State Numbering and Casualty Reporting Systems, 33
 Sec. 174. http://www.gpo.gov/fdsys/granule/CFR-2010-title33-vol2/CFR-2010-title332-part174

Law 109-8. (2005). Bankruptcy Abuse Prevention and Consumer Protection Act of 2005.

```

```
Rowley, J. (2007). The Wisdom Hierarchy: Representations of the DIKW Hierarchy. Jour
  Information Science, 33(2): 163-180. http://jis.sagepub.com/content/33/2/163.full.pdf+h

Silver, N. (2012). The Signal and the Noise: Why So Many Predictions Fail—but Some
  Penguin Press.
Sinai, N., and Van Dyck, H. (2013, May 13). Recap: A Big Day for Open Data. http://www.white
  .gov/blog/2013/05/13/recap-big-day-open-data
Smith, E. B. (2013, May 2). Disclosed: The Pay Gap Between CEOs and Employees. http:
  .businessweek.com/articles/2013-05-02/disclosed-the-pay-gap-between-ceos-and-employ

Snyder, T., & Truman, J. (2013, June 26). Indicators of School Crime and Safety, 2012. http:
  .bjs.gov/index.cfm?ty=pbdetail&iid=4677
Socrata.com. (2014). Socrata Customer Spotlight. www.socrata.com/customer-spotlight/
Susko, J., Putnam, J., & Carroll, J. (2012, August 28). Bay Area School Safety Data Flawe
  Oversight. http://www.nbcbayarea.com/investigations/School-Safety-Data-Flawed
  Oversight-165171666.html |
Tavernise, S. (2011, August 25). New Numbers, and Geography, for Gay Couples. The New York
  http://www.nytimes.com/2011/08/25/us/25census.html?_r=1&
Texas Parks and Wildlife Department. (n.d.). Hunter Education Outdoor Learning Publica
  http://www.tpwd.state.tx.us/publications/learning/hunter_education/
Tufte, E. R. (1983). The Visual Display of Quantitative Information. Graphics Press.
Tufte, E. R. (2006). Beautiful Evidence. Graphics Press.
Tukey, J. W. (1977). Exploratory Data Analysis. Addison-Wesley.
U.S.C. Title 46. (2011). United States Code, 2011 Edition. Title 46—-SHIPPING. http://www.gpo
  fdsys/pkg/USCODE-2011-title46/html/USCODE-2011-title46-subtitlelI-partD-chap61-sec
  htm
United States Courts. (n.d.a). Bankruptcy Statistics. http://www.uscourts.gov/Statis
  BankruptcyStatistics.aspx
United States Courts. (n.d.b). Chapter 11. http://www.uscourts.gov/FederalCourts/Bankru
  BankruptcyBasics/Chapter11.aspx
Utts, J. M. (2014). Seeing Through Statistics, 4th edition. Duxbury Press.
Westhoff, P. (2013, Sept. 8). Telephone interview with the author.
Wolfram Alpha. (n.d.). Timeline of Systematic Data and the Development of Computable Knowl
  http://www.wolframalpha.com/docs/timeline/

Yau, N. (2011). Visualize This: The FlowingData Guide to Design, Visualization, and Stat
  Wiley.

```

```
Index

```

```
 R. L., 6
 ColdFusion, 22
es
ata analysis, 15-19
ata collection, 15-19
 entry by, 19-23
ata publication, 15-19
 storage by, 38-40
abase creation by, 15-19
ltural data, dirt in, 71-72
n Directory Releasable File, 42-43
thms, 8
numeric data, 42
an Library Association's State Agency
atabases, 55
can Standard Code for Information
nterchange. See ASCII
t change, 117, 123
 9, 46
reports, 52-53
 E. M., 7

e, Charles, 8
ptcies, 4-5
ptcy filings, 72
arts
cription of, 152-154
xcel, 158-160
zontal, 158-160
marking, 118

ts, 155
 of Alcohol, Tobacco, Firearms, and
xplosives, 20
 of Economic Analysis, 73
 of Justice Statistics, 36
 of Labor Statistics, 37
 of Transportation Statistics,
6-37
George H.W, 18

```

```
Calc, 188
Cell references, 122
Census Bureau, 35-36
Central tendency, 116
chm 22
Charts/charting
 bar, 152-154
 clustered column, 151
 data visualization using, 149-156
  ihn Beal, SVMS
  line, 152
 pie. See Pie charts
 stock, 155
 vertical column, 150-151
 web tools for. See Web tools
CKAN, 31, 33-34
Clustered column charts, 151
Clustering, 109-110
Coast Guard, 15-16
Column carving, 96-103
Column charts, in Excel, 160-164
Comma-delimited text files, 11
Comma-separated values (CSV) file, 11
Comparing data
  rates for, 118, 126-127
  ratios for, 118, 127-128
Computer servers, 58
Concatenation, 103-106
CSVelil
Cuillier, David, 62

Data
 alphanumeric, 42
 comparing. See Comparing data
 in dates, 106
 definition of, 3
 error-checking tools for, 70
 geographic, 156
 history of, 8-9
 offline. See Offline data
 primary, 6

```

```
 publication of, agencies involvement
    in, 15-19
 raw, 5
 run-on, 70
 secondary, 6
 visualizing. See Data visualization
Data analysis
 agencies involvement in, 15-19
 benchmarking, 118
 comparisons, 117-118
 database managers, 181-184
 exploratory, 145
Data cleaners, 188
Data cleaning
 column carving, 96-103
 concatenation, 103-106
 description of, 95
Data collection
 agencies involvement in, 15-19, 23
 changing rules for, 72
 for legal mandate fulfillment,
    15-19
Data comparisons, 117-118
Data documentation, 42
Data entry, in databases, 19-23
Data extraction, from PDFs, 111-112
Data files
 downloading of, 43-49
 formats of, 9-11
 information held by, 4-5
 inspecting of, 43-49
 unzipping of, 43-49
Data-information-knowledge-wisdom
  pyramid, 6-8
Data integrity checks
 big-picture checks, 76-78
 overview of, 75-76
 pivot tables for, 78-94
Data portals, 29-35
Data search, using Google Advanced Search,
  41-42
Data storage, by government agencies,
  38-40
Data visualization
 best practices for creating,
    146-148
 charts for, 149-156
 definition of, 145
 exploratory data analysis, 145
 online options for, 171-174
Database managers, 7, 181-184
Databases
 agencies that create, 15-19

```

```
  data entry in, 19-23
  reports from, 23-25
 Data.gov, 29, 33-35
 Data_Notebook, 32
 Dates, data in, 106
 Davis, Charles N., 62
 dBASE, 9
 Decennial census, 35
 Delimited text files
  comma-separated, 11, 44-45
  definition of, 9
  delimiter character used in, 47
  example of, 10-11
  image of, 44-45, 47
  text qualifiers used in, 45-46
’ Delimiters, 11
Department of Energy, 43
 Digital computers, 8
 Dirty data
  in agricultural data, 71-72
  environments for, 69
  as hindrance, 69-70
  overview of, 67-69
 Drivers Privacy Protection Act (DPPA),

 Electronic Freedom of Information Act
   Amendments (E-FOIA), 53
 Embed code, 171
 Environmental Protection Agency
  databases from, 17-18, 40
  purpose of, 18
  Risk Management Plan database of, 17
 ESPN, 7
 Excel
  bar charts in, 158-160
  charting in, 157-167
  column carving, 96-103
  column charts in, 160-164
  Comma Separated Values File, 44
  concatenation, 103-106
  data in dates, 106
  data types, 48
  description of, 187-188
  filtering, 134-137
  format of, 9
  grouping, 138-141
  horizontal bar charts in, 158-160
  line charts in, 160-164
  parse, 95
  pie charts in, 157-158
  PowerPivot with, 181
  purpose of, 4
  scatterplots in, 164-166

```

```
ng, 131-134
lines in, 167
arizing, 138-141
 to Columns tool, 95, 97
tory data analysis, 145
ble markup language. See XML

Educational Rights and Privacy Act
ERPA), 61-62
ervice Agency, 53
 Analysis Reporting System database,
8-19
 Aviation Administration, 42
 Deposit Insurance Corporation,
8-39
ensions, 9
g, 134-137
idth text files
ition of, 9
ple of, 9-10
nd Agricultural Policy Research
stitute (FAPRI), 71-72
m of Information Act, 58-61
m of Information Commission, 63
 Tables, 172-173, 175-180

phic data, 156
phic information system (GIS), 156
 Advanced Search, 25-26, 41-42, 49
 Spreadsheets, 171-173, 188
ment 2.0, 29
ment Accountability Office (GAO),
5-64
ment agencies. See Agencies
ment websites
au of Justice Statistics, 36
au of Labor Statistics, 37
au of Transportation Statistics,
 36-37
us Bureau, 35-36
 documentation from, 42
rtment of Labor, 37
s and reports from, 25-27
al user interface, 181
omestic product (GDP), 73
g, 138-141

Insurance Portability and
countability Act (HIPAA), 62
am, 184-185
h, Herman, 8
tal bar charts, in Excel, 158-160

```

```
Industrial Revolution, 8
Inferential statistics, 115
Information, in data-information-knowledge  wisdom pyramid, 6-7
Information graphic, 145
Inter-university Consortium for Political and
   Social Research, 41

Jacquard, Joseph Marie, 8

Key collision, 110
Knowledge
  creation of, 7
 decision making uses of, 7
 generation of, 7

Line charts
 description of, 152
  in Excel, 160-164
Linear regression, 154

Mainframes, 58
Mass layoffs, 72
Maximum numbers, 117, 122-123
Mean, 116, 129
Median, 116, 129
Medical insurance cosis, 72
Memo entries, 75
Metadata, 75
Microsoft
  Access, 58, 181-184
 Active Server Pages, 22
  data file formats, 9
  Excel. See Excel
 SQL Server, 58
Minimum numbers, 117, 122-123
Missouri Ethics Commission, 70
Missouri Sunshine Law, 59
Mode, 117
Motor vehicle registrations, 72-73
MySQL, 182

National Center for Education Statistics,
   37-38
National Freedom of Information Coalition
   (NFIOC), 63
National Highway Traffic Safety
   Administration, 18-19
National Safe Boating Council, 16
National Security Archive, 53
Nearest neighbor, 110
Nixon, Ron, 60-61
No Child Left Behind Act, 67-68

```

```
Nongovernmental websites, 54-56
Notepad++, 9, 44, 46, 188

Offline data
 audit reports, 52-53
 getting help with, 62-64
 identifying of, 51-57
 obstacles to obtaining, 61-62
 open-records request letter for, 60
 requesting of, 58-59
 research on, 57-58
 records retention schedules, 51-52
Open data policy, 54
Open data portals, 30-35
Open government, 29
Open Government Guide, 62-63
Open Knowledge Foundation, 31
Open-records request letter, for offline data,
Open-source software, 9
OpenRefine, 95, 107-112, 188
Oresme, Nicole, 8
Outliers, 69, 89, 116

Parse, 95
PDFs, data extraction from, 111-112
Percent change, 117, 123-125
Percent of total, 117, 128-129
Perl, 95
Pitbe
Pie charts
 description of, 149-150
 in Excel, 157-158
Pivot tables, for data integrity checks,
   78-94, 188
PowerPivot, 181
Primary data, 6
Public-records laws, 58 — 59
Punch cards, 8
Pythagoras, 8
Python, 95

Rates, for comparing data, 118, 126-127
Ratios, for comparing data, 118, 126-128
Raw change, 117, 123
Raw data, 5
Reporters Committee for Freedom of the
   Press, 60, 62
Reports
 from databases, 23-25
 on government websites, 25-26
Records retention schedules, 51—52

```

```
Risk Management Plan database, 17-18
Roper Center, 41
Rowley, Jennifer, 7
Ruby, 95
Run-on data, 70

Scatterplots
 description of, 154
 in Excel, 164-166
Schickard, Wilhelm, 8
Secondary data, 6
Servers, computer, 58
Show-Me Institute, 40-41
Silver, Nate, 7
Socrata, 31
Sorting data, 131-134
Sparklines
 description of, 155
 in Excel, 167
Spreadsheet programs, 9
Spreadsheets
 Excel, 187—188. See also Excel
 filtering in, 134-137
 Google, 171-173, 188
 grouping in, 138-141
 sorting in, 131-134
 summarizing in, 138-141
 types of, 9
SPSS, 184-185
Standard deviation, 185
Standardizes, 111
Statistical programs, 184-185
Statistics
 inferential, 115
 summary, 115-117
Stock charts
 description of, 155
 in Excel, 166
STRIDE data, 138-141, 182-185
Structured Query Language (SQL), 95,
   181-183
Summarizing, 138-141
Summary statistics
 calculation of, 121-122
 definition of, 115
 simple, 116-117
Sunshine Law, 59

Tabs, 45-46
Text editors, 9, 188
Text files, 9
Text qualifiers, 45-47

```

```
Columns tool, 95, 97-102
e, 188
ngler, 9, 44, 188
ies data, 150-151
ine, 154

partment of Labor, 37
rshals Service, 54
tal Service, 54

 column charts, 150-151
ations. See Data visualization

```

```
Web tools
 data visualization with, 171-174
 evaluation of, 174-175
 Fusion Tables, 172, 175-180
 overview of, 169-170
 platforms for, 174-175
Websites. See Government websites

xls, 9
XML, 9

Zip files, 44

```

```
fi

```

```
   About the Author

Herzog is associate professor at the Missouri School of Journalism in Columbia, where
 serves as the academic adviser to the National Institute for Computer-Assisted Reporting.
ches computer-assisted reporting (CAR) and data mapping to university students and
ional journalists. He writes and speaks frequently about data journalism, investigative
ing and access to information.

010-2011 fellow at the Reynolds Journalism Institute, Herzog led the team that launched
ssouri.org, an online resource that lists data sets held offline by state and local government
s.

joining the Missouri School of Journalism in 2002, Herzog spent nearly 15 years as a
per reporter and editor. He has reported for The Providence Journal, The Baltimore Sun and
rning Call in Allentown, Pennsylvania.

 a bachelor’s degree in Radio-Television-Film from Temple University.

n find him on the Web at dherzog.com and on Twitter at @davidherzog.

```

```
xactly what —
 looking for,
m basic _
nations to
vanced ~
cussion _

```

```
The essential online tool for researchers fro
world’s leading methods publisher

                         More conten
                           and new

     Looking for tips 10 set up a focus group?
     evigned SAGE Resenrch 12h Methods Oedine (SRMO} ix on ewerd-ewimning tro}
     «Tha Daisies, LNenty ‘Two thee entice major works 82 cormmnsasioned hooks “itn encyclopedias. Gena: colating véoos Bos” 9 se:ection sed aoc handbocks “Litie ct jos! Save Base stiches eens
     Presse prov fuethoack trough this cniine murray discus wth
    ket ‘988ng veess farese. on Check Methodemnos, hore a oncmen7 deott feedback t e meet rne ts Rocery. GAGE Kotheds
                                                               &theibury
  @SAGE researchmethods
             oe ws ited agi a taf SEA cedure hd cacao features add
                            this year!

```

```
                     Become a membto sav e ang r share research Sign up ix a ee
 never really Featured Videos
thing like this
fore, and | think
valuable.”

well, University
aska-Lincoln j
                             Watch video.
                              interviews
                              with leading
                           methodologists

                                           > Whats Hew? Turemale Male sar hececires © ne EGQ SA Eh 2 NBNREA? Eagn pK SBE HOS SABIE,

             @SAGE researchmethods

```

```
Search

```

```
Aevanews t
peed

```

```
                                   MW cunmeitos ontn
                                             Roaiyais

                                                                                         + a
ore the
odsMap ‘am
iscover * = ctioand neers
between
thods

                                      Uncover more
                                                        ip ET, ILM BONGO recromyyyyynes than 120,000
                                     pages of book,
                                         journal, and reference
                                      content to support
                                        your learning

```

```
                           re

                              Geri
                   ah ee
  aot i fii aE99 bine
      pat wy if wet sir Tt
et

                       mink. oe — .

                  GAP Relers “7
                         =e di

```

## `Un`

```
     DATE DUE

Q Herzog, David, 1963180.55 author.
.E4 Data literacy
H47

```

```
 hile yc learn to make sense of it all. In Data Literacy: A User’s Guide,

professionals to the fundamentals of data literacy, a key skill in today’s w
Assuming the reader has no advanced knowledge of data analysis or sta
this book shows how to create insight from publicly-available data throu
exercises using simple Excel functions. Extensively illustrated, step-by-st
instructions within a concise, yet comprehensive, reference will help rea
identify, obtain, evaluate, clean, analyze, and visualize data. A concluding
chapter introduces more sophisticated data analysis methods and tools
including database managers such as Microsoft Access and MySQL and
standalone statistical programs such as SPSS, SAS and R.

KEY FEATURES:

  = A unique approach weaves background information about data w
   practical, hands-on lessons that develop fundamental research ski
   students should understand

  = Easy-to-follow tutorials provide readers with step-by-step instru
   to quickly begin analyzing data without having advanced knowledg
   data analysis or statistics

  = Extensive illustrations throughout the book demonstrate to rea
   how to understand data

  = End-of-chapter On Your Own exercises challenge readers to de
   their skills through easy-to-use data files and questions to reinforc
   chapter learning objectives

                                                                                                 j Certified Chain of C
                                             Sagleek ls Promoting Sustainable F

                                                     INITIATIVE www.sfiprogram.org
                                                         Ss F1-01 268

                                                                 SFI label applies to text stock

               | 9
  = Student Study Site at study.sagepub.com/herzog includes data
   that readers can use to test their data literacy

```
