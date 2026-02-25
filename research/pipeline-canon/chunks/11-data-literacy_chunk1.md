<!-- chunk: 1/2 | source: 11-data-literacy.md | words: 39996 -->
<!-- headings: `DATA`; `LITERACY`; `arm:`; `=a` -->
<!-- sections: Defining data and file formats; Identifying and obtaining data from public sources; Evaluating, cleaning, and preparing data -->

```
 A User's buide
David herzo

```

```
0.55


```

```
Digitized by the Internet Archive
  in 2023 with funding from
  Kahle/Austin Foundation

```

```
 DATA
LITERACY

  A User’s Guide

```

```
SAGE was founded in 1965 by Sara Miller McCune to
support the dissemination of usable knowledge by publishing
innovative and high-quality research and teaching content.
Today, we publish more than 750 journals, including those
of more than 300 learned societies, more than 800 new
books per year, and a growing range of library products
including archives, data, case studies, reports, conference
highlights, and video. SAGE remains majority-owned by our
founder, and after Sara’s lifetime will become owned by a
charitable trust that secures our continued independence.

Los Angeles | London | Washington DC | New Delhi | Singapore | Boston

```

##### `DATA`
###### `LITERACY`

```
  A User’s Guide

     David Herzog

   Missouri School of Journalism

  @SAGE

```

```
  Angeles | London | New Delhi
  apore | Washington DC | Boston

  INFORMATION: Copyright © 2016 by SAGE Publications, Inc.

   Publications, Inc. All rights reserved. No part of this book may be reprod
   Teller Road or utilized in any form or by any means, electronic or
  sand Oaks, California 91320 mechanical, including photocopying, recording, or by
   l: order@sagepub.com information storage and retrieval system, without permi
                       in writing from the publisher.

    Publications Ltd.
SSAGE

```

```
ver's Yard

ty Road

n, EC1Y 1SP

d Kingdom

 Publications India Pvt. Ltd.

 1 Mohan Cooperative Industrial Area

ra Road, New Delhi 110 044

 Publications Asia-Pacific Pte. Ltd.

rch Street

04 Samsung Hub

pore 049483

sher: Matthew Byrnie

l Content Editor: Gabrielle Piccininni

```

```
Printed in the United States of America

Cataloging-in-publication data is available for this title fro
Library of Congress.


This book is printed on acid-free paper.

```

```
ial Assistant: Janae Masnovi / Certified Chain of Custody

```

```
       ; j SUSTAINABLE Promoting Sustainable Forestry
 Editor: Alison Hope ays www.sfiprogram.org
etter: Hurix Systems Pvt. Ltd. SFI-O -01268

```

```
SFI-O

```

```
SFI label applies to text stock

```

```
reader: Jennifer Grubba

er: Michael Ferreira

r Designer: Anupama Krishan
ting Manager: Liz Thornton SOR PLS MOORS mabe 5) 4es eon

```

```
     Brief Contents

ce: In praise of data literacy xi
owledgments xiii

ion I. Welcome to the world of data 1

pter 1. DATA DEFINED 3

ion II. Identifying and obtaining data 13

ter 2. CLUES FOR UNCOVERING DATA 15

ter 3. ONLINE DATABASES 29

ter 4. IDENTIFYING AND REQUESTING OFFLINE DATA

ion III. Evaluating and cleaning data 65

ter 5. DATA DIRT IS EVERYWHERE 67

ter 6. DATA INTEGRITY CHECKS 75

ter 7. GETTING YOUR DATA IN SHAPE 95

ion IV. Analyzing data 113

er 8. NUMBER SUMMARIES AND COMPARISONS 115

er 9. CALCULATING SUMMARY STATISTICS AND NUMBER
    COMPARISONS 121

er 10. SPREADSHEETS AS DATABASE MANAGERS 131

```

```
ction V. Visualizing data 143

apter 11. VISUALIZING YOUR DATA 145

apter 12. CHARTING CHOICES 149

apter 13>~ CHARTINGIN EXCEL 4137

apter 14. CHARTING WITH WEB TOOLS 169

apter 15. TAKING ANALYSIS TO THE NEXT LEVEL 181

pendix—Data toolkit 187
ossary 189
ferences 195
dex 199
out the Author 205

```

```
    Detailed Contents

ce: In praise of data literacy xi
owledgments xiii

ion I. Welcome to the world of data 1

pter 1. DATA DEFINED 3

bing the pyramid 6
 ef history of the data world 8
 file formats 9

ion II. Identifying and obtaining data 13

ter 2. CLUES FOR UNCOVERING DATA 15

 and why agencies collect, analyze and publish data 15
s from dataentry 19
 from reports 23
s to uncover forms and reports 25
yourown 26

ter 3. ONLINE DATABASES 29

nation: Data portals 29
 tical stockpiles 35
cy sites 38
overnmental resources 40
 search tricks 41
 forget the road map 42
loading, unzipping and inspecting data files 43
ourown 49

```

```
apter 4. IDENTIFYING AND REQUESTING OFFLINE DATA

her clues for offline data 51
nd the data nerd 57
questing the data 58
iting the data request 60
IA in action 60
gotiating through obstacles 61
tting help 62
 yourown 64

ection III. Evaluating and cleaning data 65

apter 5. DATA DIRT IS EVERYWHERE 67

l data are dirty 69
tecting dirt in agricultural data 71
hanged rules = changed data 72
 yourown 73

apter 6. DATAINTEGRITY CHECKS 75

g-picture checks 76
tailed checks 78
n yourown 94

apter 7. GETTING YOUR DATA IN SHAPE 95

olumn carving 96
ncatenate to paste 103
te tricks 106
wer scrubbing with OpenRefine 107
tracting data from PDFs 111
n yourown 112

ection IV. Analyzing data 113

apter 8. NUMBER SUMMARIES AND COMPARISONS. 115

mple summary statistics 116
ompared to what? 117
nchmarking 118
n yourown 119

```

```
    COMPARISONS 121

crimes by year 122
mum and maximum numbers 122
nt change 123
ing up to percent change 123
ing rates 126
ing ratios 127
nt of total 128
 summarizing 129
ourown 129

er 10. SPREADSHEETS AS DATABASE MANAGERS 131

ng 131
 ing 134
ping and summarizing 138
ourown 141

ion V. Visualizing data 143

ter 11. VISUALIZING YOUR DATA 145

visualization defined 145
 best practices 146

ter 12. CHARTING CHOICES 149

lizing data with charts 149
ourown 156

er 13. CHARTINGINEXCEL 157

hart 157
ontal bar charts 158
mn and line charts 160
erplot 164
 chart 166
lines 167
our own 167

```

```
hapter 14. CHARTING WITH WEB TOOLS 169

nline visualization options 171
valuating Web visualization platforms 174
reating Fusion Table charts 175
n your own 180

hapter 15.) TAKING ANALYSIS. TO THE NEXT EEVER Ist

atabase managers 181
atistical programs 184

ppendix: DATA TOOLKIT 187

preadsheets 187
xt editors 188
ata cleaners 188

lossary 189
eferences 195
ndex 199
bout the Author 205

```

```
Preface: In praise of data literacy

    ere living in an age awash in data, data that are used to make critical decisio
    in all aspects of our lives: in education, government, economics, public safe

    politics, international development, health care, marketing and more. Yet,
 of us, understanding and analyzing data is a dark art that we’d rather leave to t
rts.” We'd rather say, “In data we trust.”
owever, if we choose that path, we do so at our peril.
y desire to write this book developed around 2010, when the tech, business and po
media were mesmerized with all things data. You couldn’t go one day without readin

e Web, reports about how government open-data portals, social-media analytics, b
or data scientists were going to change the world. Only rarely did these reports men
any pitfalls or shortcomings that lurk inside data, potential traps that I’m famili
from more than two decades of experience as a journalist and educator.
wo events later underscored the need for us to get beyond the hype and really unde
 data.
rst, Nate Silver, then a blogger for The New York Times, predicted that Preside
k Obama would handily win reelection in 2012. Silver based his prediction on t
 l analysis of polling data from all 50 states. Before the election, many pundits, poli
 and campaign operatives had assailed Silver, saying that the race was really too clo

l. Not only was Silver correct about the strength of Obama’s victory, but the blogg
 lso accurately predicted the contests in all of the states.
hen came the revelation in the spring of 2013 that two Harvard economists h
 in making calculations for an influential study about federal government debt.

 tudy, the economists had concluded that economic growth plunges when de
ds 90 percent of gross domestic product. The study was treated as authoritative
 reports. Elected officials who opposed increased public spending used it to bolst
 positions. However, another team of economists later reviewed the data behind t
 and revealed their shortcomings, which included a Microsoft Excel spreadshee

lculation.

```

```
 These diverging examples show how important it is for us to become adept at u
a. We need to be data literate.
 The goal of this book is to help students develop key data literacy skills and practi
cause every student needs to be data literate, the book is aimed at undergraduates ac
 disciplines who are enrolled in classes that employ research skills. The book is a g
 navigating our data-rich world, and covers all steps: identifying, obtaining, evaluat
eaning, analyzing and visualizing data.
 There’s no shortage of textbooks that will help students learn introductory statis
thods using research data. However, this book is unique in that its goal is to im
ndamental nonscientific research skills that all students should know for their acade
d professional careers, using readily available software and government data.
 The book takes a distinctive approach by weaving in the background informat
out data with practical, hands-on lessons. For instance, Chapter 8 details best pract

creating number summaries and comparisons, while Chapters 9 and 10 show ho
ate those summaries and comparisons using Excel.
 The how-to chapters of the book liberally employ screen shots and step-by-step inst
ns to help students walk through the lessons. In addition, at the end of most chap
ere are “On your own” exercises or questions that students can work through
ctice. At the end of Chapter 3, students are challenged to uncover three state or
tabases that they can download.

 To help students and instructors, the author has created easy-to-use data files for
ssons and “On your own” exercises. You can find these on the SAGE Publications web
study.sagepub.com/herzog
 This book is structured into five sections. Section I is designed to introduce student
e world of data and how they are created. Section II will help students develop a
te of mind that will allow them to discover databases that are available on the Inte
offline at government agencies. Section III will lead them through the process of l

g how to evaluate, understand and clean data. In Section IV, students will learn
actices for analyzing data using Microsoft Excel spreadsheets. Section V focuses on
create charts using Excel and Google Fusion Tables.
 In the end, students will have learned key data literacy skills that will prepare them
e more advanced analytical skills that will come later in their studies.

```

```
    Acknowledgments

a his book carries my name as the author but, truth be told, it is the creation of man
    I'd like to thank some of them here.

      First and foremost, thanks go to all of the great journalists, educators a
  nts whom I've had the good fortune to learn from since joining the Missouri Scho
  rnalism in 2002. Much of what you read in this book was informed or inspired

  so, I would like to thank my colleagues, past and present, at Investigative Reporte
  ditors and the National Institute for Computer-Assisted Reporting, in particu
  tive Director Mark Horvit and former Executive Director Brant Houston. At the M

   School of Journalism, I would like to recognize my dean, R. Dean Mills, and depa
   chair Tom Warhover for their steadfast support over the years.
  deline Odle, an Honors College student at the university, assisted with resear
  g up interviews and reading the book copy with fresh eyes. Her contributions we
  able and helped improve this book immensely.
  m grateful for former colleague Charles Davis, now dean at the University of Georgia

   College, who connected me with SAGE Publications—CQ Press.
  anks to SAGE acquisition editor Matt Byrnie and editorial director Charisse Kiino
  enthusiasm about taking on this project. Also, thanks go to SAGE production edit
  e Cannon and Laura Barrett, assistant editor Gabrielle Piccininni and marketi
  er Liz Thornton for their contributions. I am indebted to copy editor Alison Ho
  r fine work in getting this book into shape. Thanks also to the following reviewers
  ok. I very much appreciate their constructive comments and recommendations:

   im Bernauer, Robert Morris University in Pennsylvania;

  oseph Hayden, University of Memphis;

  lbert May, The George Washington University;

  Stephen Siff, Miami University;

  and David Valentine, University of Missouri-Truman School of Public Affairs.

```

```
 Finally, thanks to family and friends who provided support as I’ve worked on this b
 particular, I’d like to thank my son, Ben, for his patience, especially on those days
adline when I was distracted with writing.

UBLISHER’S ACKNOWLEDGMENTS

AGE gratefully acknowledges the contributions of the following reviewers:

  James A. Bernauer, Robert Morris University

  Michael Tagler, Ball State in Indiana

  David C. Valentine, University of Missouri

```

```
         |
 pt onoe kev |
MELE oT
      hee ">

    ~ = i

             ' A

                     il

                  
            Ss

                                     i]

         S
                 SS
 = a
   = ?

           =

   > — ~

      S >
       =

        —

```

```
PTER 1 DATA DEFINED

 efore we start exploring our world of data, we need to have a solid grasp of exac
 what data are and aren't. This might seem like a technicality that we could igno
 but it’s important for us to develop an understanding, one that will prepare us
ts or professionals to communicate effectively with others who maintain and sh

If we’re able to express what we mean by data, we'll be more effective when we
 to obtain them from the Internet or by using open-records laws.
e word data, of course, is the plural of the Greek word datum, and has been around

ies. So it is nothing new. However, many people misunderstand and misuse the te
When people think, talk or write about data, they often are referring to informati

cally. For instance, they might say, “Those are some interesting data points,” or, “
ave data to back up that claim?” In those cases they really mean, “That’s some intere
formation,” or, “What evidence do you have to back up your claim?” In these cas
ight be referring to information that’s stored as text, statistics, tables or even chart
ctionaries can help us get closer to the definition of data that we'll use througho
ook. It’s true that some dictionaries define data more loosely. Merriam-Webster

 primary definition of data is this: “factual information (as measurements or stat
sed as a basis for reasoning, discussion, or calculation.” The Oxford Advanced Ame
ictionary (Oxford, n.d.) offers a similar primary definition: “facts or informatio
ally when examined and used to find out things or to make decisions.”

we read past those primary definitions, though, we get definitions that are more
 Oxford’s secondary definition of data is, “information that is stored by a compute

d, n.d.). This is correct, but not the whole story. After all, this definition wou
e any music files, Word documents or photos that you might have stored on yo
ter. Merriam-Webster gets a wee bit closer with its third definition: “information

ical form that can be digitally transmitted or processed” (Merriam-Webster, n.d
files can be digitally transmitted over computer networks and processed using p
 because data are composed of bits. Bits are the smallest units of computerized da
ne of these definitions nails it for our purposes or those of many professionals w
with data, however. So we will consider data to be any computerized file that u

ns and rows (a tabular structure) to organize data that are represented as text, nu
dates and the like. In addition, these files can be manipulated using programs l

```

```
preadsheets and database managers, and can be transmitted over computer network

e'll learn more about these types of files soon.

       A & ¢ 2
 1 MFG_FIRM_FEL_NUM LGL_NAME LINEL_ADRS LUINE2_ADRS CITY_RAME

 2 2008247634 Agostine Recca Conserve Alimentari Sri Contrada Santa Maria Scacee

  3 3007384564 Banaful & Co, 497 Sk Muhb Road Chittagong:

 4 3004398937 Prince Food Products Commercial Plot No 2, Main Road 1, Block 8, Section 1, Mi Dhaka
 5 2007450858 Bangas Itd Doulatdia,Chuadanga, bgangtadesh. Chuadanga

 6 3008512485 Square Consumer Products Merit Road Pabna 6600 Salgaria
  ? 2004276258 Barnier Zia Ou Batier 34110 Frontignan Montepellier

 & 3004276258 Bamier Zia Du Sarier 24110 Frontignan Montepettier

 s 3004276258 Barnier Zia Ou Brier 34116 Frontignan Montepellier
 1 3004276258 Barnier Zia Du Barier 34110 Frontignan Montepellier

 it 3004276258 Barnier Zia Du Barier 38110 Frontignan Montepellier

 12 3004276258 Barnier Zis Ou Barier 34110 Frostignan Montepellier

 33 3004276258 Bamier Zia Du Barier 34110 Frantignan Montepellier
 % 3064276258 Barnier Zia Ou Barier 34110 Frontignan Montepellier
 6 200425$266 Shanxi Changzhi Yunhai Foreign Trade Meat Co. itd NO,43 Changan Road Changzhi

 i 3004255266 Shanxi Changzhi Yunhai Foreign Trade Meat Co, itd NO.S1 Changan Road Changahi
  7 3008256772 Viyuan Haida Foodstuffs Co ttd Lucun Town Yiyuan Countyzibe City Shandong
        3008356772 Yiyuan Haida Foodstuffs Co itd Lucun Town Yiyuan Countyzibo City Shandong

  9 3004251160 Anhui Fuhuang Chaohu Sanzhen Co. itd Huangglu Town, Chaohu

 wo 3004251160 Anhui Fuhuang Cheohu Sanzhen Co, id Huangelu Town, Chaobu
 a 3009521500 THIEN MA SEAFOOD CO, LTD - FACTORY 3 2.L1E STREET 9, TRA NOCH ZONE O MON DISTRICT Ho Chi Mint:

 22 3008512445 Square Consumer Products Meri! Road Pabna 6600 Salgaria

 a 2008518445 Square Consumer Products Meri! Road Pabns 600 Saigaria

ource: Food and Drug Administration.

ote: Data in a spreadsheet.

 Data files may hold information that’s been summarized or aggregated in some way.

his example, these data about bankruptcies filed in U.S. courts have already been su
arized by federal court districts, circuits and type of bankruptcy (United States Court

.d.a). We can easily read the data in this table and see that, in the federal court district
assachusetts, 3,207 people and businesses filed for bankruptcy during the first quart
f 2013. Of those, 33 filed for Chapter 11 bankruptcy, in which businesses are allowed
eorganize and continue operating (United States Courts, n.d.b).
 The purpose of the Excel file that holds the bankruptcy summaries is to provide mea
ngful information to people who may not know how to manipulate raw data. Anyone who
ble to download this Excel file of summaries can get an understanding of bankruptcy fil
ctivity in this quarter. Think of it as a report, with the information already baked in.

    A B 6-3 5 é a 6 H {
   Table F-2. ;
   U.S. Bankruptcy Courts—Business and Nonbusiness Cases Commenced, by Chapter of the Bankruptcy Code,
   ‘ During the Three-Month Period Ending March 31, 2013, Based on Data Current as of March 31, 2013
                                           Predominant Nature of Debt*
    Circuit Total Total Total Total Total | Business Filin Nonbusiness Filings
    and Filings | Chapter| Chapter | Chapter | Chapter | Chapter | Chapter | Chapter | Chapter Chapter | Chapter | Chapte
   District | ime 4 11 12 13 Total 7 4 12 13 Total 7 13

```

```
TOTAL 272,296 189,083 163 80,737 8,512 4,990 103 689 263,784 183,380 $0,04

```

```
 3,448
 BOS
 2,427

10,626
 1,967
 3.397
 2,027
 4,370

```

```
166 o 192

```

```
{1

```

```
ON2C O P O N w 227 HYNawDC O M MA

```

```
8 (ME
9 NA
40 NH
41 RE
42 PR

43. 2ND
$4 (CT
4B NYN
46 NY, E
17 INY.S
48 (NY W
43 VT

```

```
%

o
V)

```

```
=

```

```
 her data files hold information that has not been summarized; these are considered
 ata. We usually can tell if data are raw because one row contains data about one
, place or thing. With the bankruptcies, a raw data file would provide one row with
 ed data about each bankruptcy filed by a business or a person. It would probably

 in the first row, headers to tell us what each column holds.
 e snapshot of the city of Seattle Police Department’s real-time incident reports pro a great example. Each row in the table represents a police report that an officer took

 he or she responded to an incident. As you can see from the headers, the officers

 data about the offense type, code, location, date, time and other details.

                                         Cty of Seattie Mebics Developers Data Potcy Hep Sign Up. Sign i te date. seattic.goy
© data seattle gov

 Seattle Police Department Police Report incident
  hive inckients att based on Relat sakes reports ixken by officers: when Jo-Jo~]
                                                                  ZoneHeat

   WARRARR-FELON 8600 BAS BLOCK oF ¢ 7 is & Ho

   VEH-THEFF-AUTO 2400 VEHICLE THEFT © 06/14/2012 OF 44.0 GO/4R2012 W.SOX OSAIBO1S NAO B7KK BLOCK OF SES $4 a

   YEH-THEFT-AUTO 2400 VEHICLE THEFT 08/14/2073 26.90:€ 0612/2073 US:00-C OA1420 12 OSAET 428% SLOCK OF ML

   BURGLARY-FORO 2208 BURGLARY ORNA2012 GEASL 06742012 9250-5 BBXX BLOCK OF 4 F

   ASSLT-NOMAGG 1200 ASSAULT GSAS{04S OSARC OGM472013 G24ASE 428% BLOCK OF

   ASSLTE-NONAGG 1300 ASSAULT OBMA4I2042 BSL GGIH2012 IZOAL 24XX BLOCK OF BEO

   ASSLT-NONMAGG 1360 ASSAULT OSAS2013 O14E:C OGM472013 12330 428X BLOCK OF E &

   THEFT-BULDING 2308 OTHER PROPERT 08/14/2043 S1:060 067402013 04°06.¢ TEX BLOCK OF GC KK

   DUEIQUGR $300 ou) O68/2013 O1GAC CB142843 O1:08C PRR GLORK OF 15,

   ROBEERY-STREE’ 1200 ROGRERY OBA4207S 190-0 GE4W2012 14:45: 5AY SiS JACKSOI K

   OBSTRUCT 4308 SBSTRUCT OGI1/2642 IREEK GHAB20143 41.506 2TKK BLOCK OF BD

  https://data.seattle.gov/Public-Safety/Seattle-Police-Department-Police-Report-Incident/7ais-f98f.

 eattle Police Department incident data.

 nicipalities, counties and states provide data files like these as part of open-govern initiatives that have gained momentum during the past several years. Seattle and other
 make data files like these available so citizens and other residents can better under how government operates. In addition, the city makes these files available in formats
developers can use to build mobile applications and Web applications that display
 locations.

 wever, to someone who is untrained in the ways of data, this file would be nearly
s. All an untrained person could do is download the incidents file, open it in a spread program and then scroll through it, looking for information. No one has run any
 ations yet, or generated a report.
 ll, we usually prefer to get raw data. Raw data afford us more flexibility when it comes
lysis. We can make our own decisions about how to summarize. We could use the file
 the Seattle Police Department to determine which block in the city has the greatest
er of reported crimes, or [the ][greatest ] [number ] [of ][reported ] [burglaries. ] [Additionally, ]
ata make it easier for us to examine [our ] [data ][and ][test ][the ][integrity—or ] [quality—of ][our ]
 as we will do later in Chapter [5. ][For ][more-sophisticated ] [data ][users, ] [raw ] [data ][are ] [better. ]

```

```
ind raw data online. Failing that, we would need to request the data from the U.S. Cour
System.
 The data files that we will work with in this book all are considered secondary data,
ata that are collected by individuals other than ourselves. Some academic disciplines a
rofessions analyze data that they've collected themselves; these are considered prima
ata. Primary data are used heavily in the natural and social sciences, as well as in med
ine. Such data are sometimes obtained by the process of sampling, or selecting a subs
from the whole population of whatever it is you are studying. As you progress in yo
academic career, you might work more with primary data.
 Here are some illustrations of primary data collection:

  e A research psychologist interested in the effectiveness of televised antismoki
   advertisements enlists subjects to watch the ads. The psychologist collects da
   about the subjects’ reactions by asking a series of questions.
  e A medical researcher testing an experimental cancer drug enlists subjects, some
  whom get the drug while others get a placebo. The researcher uses blood tests
   record white cell counts as a way of assessing the effectiveness of the drug.
  e A political polling consultant hired by a candidate running for office uses telepho
   interviews to ask questions of likely voters about what issues are important to the

CLIMBING THE PYRAMID

Data are our starting point—the raw material that we use to understand our world bett

s such, data sit at the bottom of the data-information-knowledge-wisdom (DIKW) hi
rchy. Operations research expert R. L. Ackoff spoke about this hierarchy more than t

decades ago (Ackoff, 1989).

                  Knowledge

 ource: R. L. Ackoff; illustration by author.

ote: The DIKW pyramid.

```

```
 used to create knowledge, and knowledge can be used to create wisdom,” wrote
er Rowley, a professor of marketing and management at the University of Bangor in
ited Kingdom (Rowley, 2007, 164.)
lofty goal, but possible. Here’s how the pieces fit together and how we can use them
end to the pyramid’s peak.
ta, the bottom of the pyramid,’ are the unprocessed symbols that represent
teristics of objects or people. These data are unorganized and have no meaning or
in isolation (Rowley, 2007). Because data constitute the base of the pyramid and

 a greater area, we can conclude that we are awash in data relative to the other

nts in the pyramid. Also, we can see that data serve as the foundation for all of the
levels.
ta can be used to step up to the next level of the pyramid: information. We create
mation by processing our data using computer programs. For example, we might
spreadsheet like Microsoft Excel to create totals or averages—descriptive statistics

re more meaningful to us. Or, as we will do later in this book, we might calculate
or ratios using our data. We could also use database managers like Microsoft Access
rform more-sophisticated analyses, something that is outside the scope of this
 Information is descriptive: it answers questions like Who? What? Where? When?

y, 2007).
er we've generated information, we aim to generate knowledge, which requires us to
 on the information. Knowledge is created when we take information and turn it into

hing that can be acted upon (Rowley, 2007). Knowledge helps us and all kinds of
ssionals—such as teachers, political researchers or business analysts—make better
ons.
 Nate Silver, the founder and editor in chief of ESPN’s FiveThirtyEight, put it, “The
 has come a long way since the day of the printing press. Information no longer is a
 commodity; we have more of it than we know what to do with. But relatively little of
eful. We perceive it selectively, subjectively, and without much self-regard for the
tions that this causes. We think we want information when we really want knowl
 (Silver, 2012, 17).
lping you learn how to get from data to knowledge is one of the central goals of this
After you have experience getting from data to knowledge, you may even be able to
to the peak and attain wisdom. But that takes experience, along with the exercise of

 and judgment (Rowley, 2007).
e important point to keep in mind is that working effectively with data requires
than computing. It requires thought and reflection on our own parts. As we climb
ramid, we rely less on computers and more on our own experiences and thoughts.
Awad and H. M. Ghaziri accounted for this dynamic when they modified Ackoff’s

```

```
           Nonalgorithmic o Nonprogrammable

                 Knowledge

 fae

Source: Awad and Ghaziri; illustration by author.

Note: Modified DIKW pyramid.

DIKW pyramid, shown above, for their business knowledge management textbook (Aw

and Ghaziri, 2004).
 As you can see, this modified pyramid shows that the data at the base can be mani
lated by computer programs or algorithms—a set of steps for solving a mathematic
problem. The steps up to information and knowledge are less reliant on programs
algorithms, and wisdom is not reliant on them at all.

A BRIEF HISTORY OF THE DATA WORLD

With all the recent buzz over open-data portals, big data and data science, it’s easy to o

look the roots of data and computing, which stretch back to 20,000 B.C. (The follow
discussion is based on Wolfram Alpha n.d.) That’s when our predecessors invented ar
metic as a tool for calculating numbers of objects. Then, in the years from 2150
1700 B.C., they created standards for measurement and multiplication. Later, in 500 B
Greek scholar and mystic Pythagoras promoted the idea that the world could be und
stood by numbers.
 Much later, during the Renaissance, Nicole Oresme developed the idea of represent
numbers by using graphs, which continue to be important tools for communicati
data. Nearly three centuries later, Wilhelm Schickard invented a wooden machine
could add up to six digits.
 The Industrial Revolution brought even more innovations that helped create
world of data, including Joseph Marie Jacquard’s use of punch cards to control the lo
at his weaving mill in France, Charles Babbage’s early mechanical computers and Herm
Hollerith’s use of punch cards to automatically tabulate results from the decenn
U.S. census.

  The 1940s ushered in the era of digital computers, those that used vacuum tube

perform calculations on data stored as a series of numbers. In 1963, the Ameri

```

```
ards Association developed the data-encoding system that still dominates comg in the United States. This system is called ASCII—short for the American StanCode for Information Interchange—and allows us to easily share data. ASCII text
re the most portable data files available. The 1970s brought other advances, such
ational database manager programs, interactive computing and the first personal

ters.

                                         /

 FILE FORMATS

ata files that you store on your computer, whether it’s a Mac or PC, can come in
eds of formats. Audio, video and graphics files all are stored differently and

their own file extensions (those characters that come after the file name and

d) (FileInfo.com, n.d.). For this book, we'll focus on using just a few different
 of data files that we can analyze using spreadsheet programs such as Excel or
ffice Calc.
crosoft has two file formats for Excel workbooks, which can hold multiple work. Excel 1997-2003 format workbooks have an .xls file extension. A more recent file

, introduced with Office 2007 for Windows, has an .xlsx extension and is based on
 or Extensible Markup Language. Microsoft says the XML-formatted files are

r, more robust and more interoperable than the .xls files (Microsoft Developer

rk, n.d.).
ide from using Excel’s native files, we can use files in other formats. Excel and Calc
pen OpenDocument spreadsheet format files. The files have an .ods extension and
developed as an XML-based open-source alternative to Excel’s proprietary formats.
both spreadsheet programs can work with the proprietary dBASE database file
. dBASE files have a .dbf extension
xt files are perhaps the most useful format of all because they can be read, pro and exported by all computers and data analysis programs. In the United
, these files are usually encoded with the ASCII characters, making them read
by mainframe computers, servers, Macs and PCs alike. These text files come in
ifferent flavors: fixed-width and delimited. You can examine both types using
 editor, such as Notepad++, which is a free and open-source software Winprogram that’s able to handle large files. TextWrangler is a good choice for
 that is also free.
e data inside fixed-width text files already are nicely arranged into columns and
The table looks just how we’d expect a data table to look. The following example is
e of aircraft types compiled by the Federal Aviation Administration. Each of the
 lines contains data about one type of aircraft. Eyeballing the file, we might make
solid, educated guesses about where [column ] [breaks ] [should ] [go, ] [but ][we ] [really ][can’t ]

e.

```

```
wy (2) \Uceriherssgd Downtosds\dats_ “comple oncrettta ‘ fps

```

```
 Fite Edit Search” View” Encoding” Language “Settings Maw Run Phagine: y
  ae a 9 8) & Se O)2¢|\ ae) 4 +(e

```

```
O)2¢|\ ae) 4

```

```
+(e

```

```
fe ee
  aucraft bt

    o5eB
    LSOOCLARK
   to oN 460186

```

```
3G A202
30 4A22
SE Ai4CcE
SR ATCi3¢
4ERTAZSWE
4F A23WE
4F A2Z3WE
4F A2aWE
4F A23WE
4F A2SWE
 ROG46E0
 RCG46EU
 RO

SR 4A25
  G46E0

```

```
01910061H72
22302021Q72
01402081872
63802021L72
01402041872
01402022872
11529263172
13819021972
N/A~SDR2L73
    2L73
S26S0102L75

```

```
       AERCNCAQSSB
BR 2A6 2009
3O 1A21 £00280
SIRCEXPAIL? INORDIO02

```

```
SY ATCLT 1012
SONTEXPALL7IULTIMATE 10265

```

```
09/09/2003GLARONCASS
O8/31/i9845WCLARK i000

03/22/1983SWSLINDSI00
20/O7/1S99GLAMTR NORD

03/22/198SSWSLINDS106
O3/22/1983SWSLINDSi09
02/09/2001CEBEECH 100

O3/ 22/1 933MMBOEINGIOG
907722 /1999NMLRHEEDIOI2

83/22/1983WPLKHEEDiOi2

03/22/1983WPLKREEDIO12
03/22/192SWPLKHEEDIOi3
03/22/1983WPLKHEEDIO32

03/22/L98SWPLREZEDLO1S
02/19/19S6EUCNTRARIO2

02/19/2986EUCNTRARIOL
10/30/2007GLCNTRARIO2Z
10/15/2008EUCNTRARIOL
93/22 /iS83EAMITCHLIO4
10/15/2008EUCNTRARION
03/22/19883CEROOS Ai

```

```
i100
Lioii
LIGLIMODELUNK
LiG2i3852
LiSiiss5ii¢d
L1612385215
LAOLASES3
LOLA
104AP
CENTRAIRIOIC
i02D PAGASE
CENTAURiO2
4O2P

```

```
 i &3h

```

```
ee

```

```
 Qo

```

```
i662

280A
LSOACMDR
L90BEECR
LOOBOEING

20ii*

10213853
2011385124
2021385215

48223853
LOLACENTR
iGZAPCENTR

I9ICCERTR
2OLDCENTR
LO3MITCRL
ZOLPCENTR
i6ZR00S
10200

```

```
 ww RO

```

```
Role ee ae

 6 3ho

M OR e
 iN)

```

```
ARISTROCRATLO2ZA

```

```
4H72

```

```
SR ArCL47

```

```
SR ATC210 1025
SR 4Hi5 192

SONCEXPAIQVIULTIMATE 15 3008

```

```
   102E
 GMOFoh an ee 1G LOQ2MITCRE

Mofo oN Bea 163008

```

```
13/01/2001EAGENAC 102

03/22/11 983EAMITCHLIO2

```

```
 GMOFoh an ee 1G

```

```

```

```
 an

a

```

```
2011385124 03/22/192SWPLKHEEDIOi3 2473
2021385215 03/22/1983WPLKHEEDIO32 52650152473
48223853 03/22/L98SWPLREZEDLO1S S2BSG202L73
LOLACENTR 02/19/19S6EUCNTRARIO2 19901022KQ0
iGZAPCENTR 02/19/2986EUCNTRARIOL 19902041K00
I9ICCERTR 10/30/2007GLCNTRARIO2Z 19901052K00
2OLDCENTR 10/15/2008EUCNTRARIOL 19901091K00
LO3MITCRL 93/22 /iS83EAMITCHLIO4 20091022872
ZOLPCENTR 10/15/2008EUCNTRARION 20001031K00
i6ZR00S 03/22/19883CEROOS Ai FEBOLOSIQIL
10200 O8/O8/19S0GLEMTR ULIMATOS6i2RFiL72
LOZRARISTOCROS/22/1983EAGENAC 102 4H72
102E 13/01/2001EAGENAC 102 SI 7IOLO43873.
LOQ2MITCRE 03/22/11 983EAMITCHLIO2 200020218742
163008 O4/21/1991GLAMTR 103008722052919Q7%
LOSEXECUTIVE1O/O2/2002GLAMIR 103 OS622672H72
2049* 03/22/1983WPLKHEEDIO4S 2174
104954 06/20/1993 50LKHEED1049 S2621022L74

```

```
3G EXPALERT2BUEHLEREXECUTIVE203
4R 6A5 2O49MODELUNK
4 6AS 204954

  Dos.Windows ANSI INS

```

```
2049*

104954

```

```
OS622672H72
S2621022L74

```

```
Normal text f length : 696605 fines : 7656

```

```
in:1 Cof:1 Sef:0|0

```

```
  t

Source: Federal Aviation Administration.

Note: Federal Aviation Administration aircraft data. The data are arranged in columns, which tells us this is a fixed-width tex

                                 Fortunately, the F
                            provides document
                               tion that tells us wh
                              the names for

```

```
SiTAircraft FTP

Model

Last_Change Date

Region

Make

```

```
columns should be,
where the breaks go.
this case, we see Mod
is the name of the f

column, and that
is a character colu
12 characters wide.
  In contrast, del
ited text looks lik
mess, aS you can
from the follow
earthquake report d
released by the U
Geological Survey.

```

```
Char

VarChar

VarChar
VaxrChar

VarChar

VarChar

VerChar

VarChar

VazChar

VarChar

VarChar

VarChar

```

```
@ APS

```

```
 te

 wn

```

```
Aircraft _Group

Regis Code
Design _Cnaracter

No_Engines

Type_ Engine

type _ Landing Gear
TC_Data_ Sheet Number

```

```
GRe Petbs p a ssa TC_Modei

```

```
     “3

     br ms

Source: Federal Aviation Administration.

```

```
her—it looks like a train wreck. However, if you look closely, you will see that commas
ate different pieces of data in each row. We call these comma-separated or
a-delimited text files. Data can be delimited by other ASCII characters such as the tab,

(1), tilde (~), exclamation point (!) or carat (*). Even though these data look gnarly, they
sier to import than data in a fixed-width file, because computer programs can read the
iters and automatically determine where the column breaks go.

    ile. Edit Search Aes “Encoding: "Language Sette = Run
    EG: > 6 Sit RO ee fe

```

```
 3 om A &

 &

 &

 Fe

ep

```

```
 01001", 3.9, 29, 644, 42.0638, 72.6236, 0, "Agawam", “MA”

"O2002",3.4,54,678,42.3752,-72.4617, 6, "Amherst", "MA"

"O2003",3.4,20,676,42.3911,-72.5244,0, "Amnerst”, "MA*

"02005",3.4,1, 793, 42.4203,-72.1062,5, "Barre*, "MA*

O3007",2,.0,2,674,42.2787, -72,4007,0, *Belchertawn", "MA"

"010160",2.0,1,674,42.1272,-732.2082,0, *Srimfieid", "MA"

"01013",4.8,18, 652, 42.1470,-72.6032,0, “Chicopee”, *MA"

*O4020",3.7,32,656,42.1759,-72,.5654, 0, “Chicopee”, "MA*

"91022",4.0,14, 659, 42.2968,-72.5425, 6, "Chicopee", "MA"

"01027",3.5,55,655,42.2952,-72.7424"Easthampton", 6, "MA"

#92028",4.0,6,652,42.0600,-72.4992,0,"Eaet Longmeadow", *MA"

®02030",4.6,7,641, 42,.0680,-72.6790,9, "Feeding Hilis”,”*MA”
*01031",3.8,1, 69%, 42.3641, -72.1977,0, "Gilbertville", "MA*

*O$3032",2.0,1,664,42.4587,-72,.38258,9, "Goshen, "MA"

"01033",2.9,2,666, 42.2603,~72.5039,%, "Granby", "MA

"$4034",3.4,1,626, 42.0857, -72.9564,5, "Granvilie”, “MA*

"53035",4.1,29,670, 42.3559, -72.5691, 0, "Hadley", “Ma”

"92036",5.2,3,657, 42.0641, -72.4155,5, "Hampden™, "MA"

°O25038",4¢.3,10,675,92.3850,-72.6071,9, "Hartfield", "KA*

"92039",2.0,14,667,42.4076,-72.6898, G, "“Haydenville’, "MA"

NOPG45" 4.221.655 49 .9323.-77 6471.6, "Rol ynke™ . Fake

```

```
       3474667 Ikn:i Col:1 Set:6|0 Dos Windows

: Geological Survey.

A comma-delimited text file. This delimited file uses commas as column separators and double quotation marks to
 text.

here is no convention for specifying extensions with text files, but you will often see

.csv (comma-separated values), .tsv (tab-separated values), .tab, .prn or .dat. If you
get a text file with an extension that Excel is unable to recognize, simply rename it with

f the extensions it does recognize.

ow that you know what data are, we re going to learn about clues that will help you
ver the data you need.

```

```
    ss ta ball

   See > i a _ nl —     ~ was                 % Lag
          ao ‘

                              s «< 7

            — aca
  : . ; a Fi. Re
 a - i= om ke = *
          oe 7
                            - (1 Bah: “ .)- omelet a a :
                      ~ed =a "IN _sby 2 Prete
                        =~ Oeste) Gieh.. owe
                      © ae! '                                            i Poe

                       “7 4 ; ~ Keegy A

                            e a eo ae
                      7 ° . wari o<—s 2
                         roy “nm =

    2 - a y ™ 7 > s ~~

             * = ed en ~ a
                    —— oS - S—. 2 = 3 S aa >, ‘| 6 e

                 —<- a 7 4 7 tie ad

             , 7 ee Pes ae

                             — ee by
       a 2 Ss ae
              ——— ee <y
 = sa S aw — 7

           Re muse shod
  ke att = RIE SRST Fahy? 0 “ys rigors Sin} nt iy eal] oT

        = ‘ ‘ boo ung

                   2 ; : imines
                                                                           7 — a 4 \. * oh ee bal :
     ~ 1 |, came
               Pia abe
             mm

                    a
       ; fi 4

  H ‘ ‘ ie si. =F

                                                   - if
                      j y i ARS Lue 7 a | nian oie ~4)

  ‘7 f ’ rh baled : ay myletup Wig ene = i

                    acne) Us a . Ai tf
              LOY Wud, A fk rice
                                  4 rH Y
   = FART Pils frit ts + ot t wil efessdlrrdsiw mental ie gto ad ae v*a
wo red ater ee ee Aid

               Aes eal igi hoek its

  OST etna e =e omy Saaanices
      ee sie al ets
 ried md fee masts C re:
Gh

 3)

```

```
ce

```

```
) ne of the big challenges in becoming data literate is being able to quickly identify
  data and determine which government agency keeps them. If the data are posted
  on the Internet, we can find and download them. If data are not posted online, we
equest them from the agency.
o meet that challenge we need to develop a data state of mind, one that opens our eyes

 proliferation of data online, in government agency mainframes and servers, and in
rsity libraries. After developing a data state of mind—or data antennae—it will be
 for us to see the possibilities. Data are everywhere.
nderstanding how and why government agencies process data is a good first step
d developing that data state of mind. Specifically, we'll examine how and why agen ollect, analyze and publish data. To look at it another way, we'll examine the data
 and output.

 AND WHY AGENCIES COLLECT, ANALYZE AND PUBLISH DATA

ly speaking, agencies collect, analyze and publish data for one or more of three pri
 reasons: (1) they’re required to do so by law, (2) agencies believe the data will help
 execute their missions or (3) agencies are participating in an open-government effort.
aws are one of the biggest motivations for state, local or federal government agencies
 lect data. Sometimes the laws specifically require the creation of a database. Other
 agencies use databases so they can comply with their responsibilities laid out in the

he U.S. Coast Guard’s Boating Accident Report Database holds data about recreal accidents reported to state law-enforcement authorities. In the most recent year

 ble, 2012, the Coast Guard recorded 4,515 accidents that killed 651 people and

d 3,000 injuries. The Coast Guard uses the database, which anyone can obtain by
ng a U.S. Freedom of Information Act request, to track boat accident trends and to

ate boating statistics publications that are posted on the Web (Coast Guard, n.d.).
dition, the Coast Guard provides a search interface that allows users to query the
ase and generate reports in tabular form that they can then export to an Excel

dsheet.
PTER 2 CLUES FOR UNCOVERING DATA

```

```
 Law = Boating Safety Resource Center
          Welcome to the official. websiteat the IS. Coast Guard's Boating Safety Diwis! tom

 Diaries the accident statistics available on the Coast Guard's website focus on national data. Using the Gropdown manus on this page, you may place filters on C
  Guard data by state, year, and one variable to obtain tables anWor graphs. Data from reports has been loaded for years 2005-2011. When future year's data tas been releas
  will be available for search. Please note that this data represents intormation sudmitted from the 56 reporting jurisdictions - 50 states, the District of Columbia (OC) and
  territories of Guam (GU}. American Samoa (4S), Northem Mariana Islands (MP), Puerto Rice (PR) and the Virgin Islands (¥1}. The code FE" tepresents accidents that occu
  under federal jurisdiction, The codes “AT (Atlantic Goean), “PC” (Pacific Ocean), and “GM" (any Gul!) represent accidents that occurred offshore. The information has subseque
  deen standardized by the Coast Guard for national use.

  Select: _CauseofDeath [x] ae | ee 2 fe aa

                                   Contact Susan Tomezuk for comments and inquiries

Source: Coast Guard. Retrieved from https://bard.cns-inc.com/Screens/PublicInterface/Reportt .aspx.

Note: Boating accident search page. The U.S. Coast Guard allows the public to search its database of recreational bo
accidents with this Web form.

 La =~ Boating Safety Resource Center
          Welcome to.the official websiteof the WS, Coast Guard's boaling Safety Devisiont

  Gveconehinate ie siicht Statistics avallanie on the on C
  Guard data by state. year, and one variable to obtain tables and/or graphs. Data from reports has seen loaded for years 2005-2011, When future year's data has been release
  will De available for search. Please note that this data represents information suzmitted from the 56 reporting jurisdictions - 50 states, the District of Columbia {DC) and
  ternitonies of Guam (GU), Amarican Samoa (4S), Northern Mariana Istands (MP), Puerto Rico (PR} and the Virgin islands (1). The code “FE” represents accidents that occu
  under federal jurisdiction, The codes “AT” (Atlantic Ocean}, "PC" (Pacific Ocean}. and “GM” (any Gulf} represent accidents that occurred offshore. The information has subseque
  been standardized by the Coast Guard for national use.

  Select: Cause of Death fe] State: FL eh Year: (2012

  Results: 4 Records Found

  Cause Of Death

  Cardiac Arrest

  Orewning

  Trauma

  Unknown

                                    Content Susan Tomen& for comments and inquivies

Source: Coast Guard. Retrieved from https://bard.cns-inc.com/Screens/Publicinterface/Report1 .aspx.

Note: Cause of death search results for the state of Florida, 2012.

 Publishing these data on the Web clearly is a benefit to law enforcement; boating sa
advocates, such as the National Safe Boating Council; and members of the public. Rega
less of these benefits, the Coast Guard is doing so because of a law. Congress in 1983 pas
legislation establishing the State Marine Casualty Reporting System within
U.S. Department of Transportation. The Coast Guard was part of the Department
Transportation and now is part of the Department of Homeland Security.

  The law, as amended the next year, says,

  (a) The Secretary shall prescribe regulations for a uniform State marine casua

```

```
d the manner of reporting. A State shall compile and submit to the Secretary
ports, information, and statistics on casualties reported to the State, including
formation and statistics concerning the number of casualties in which the use of
cohol contributed to the casualty.

) The Secretary shall collect, analyze, and publish reports, information, and statistics
 marine casualties together with findings and recommendations the Secretary
nsiders appropriate. Ifa State marine casualty reporting system provides that informaon derived from casualty reports (except statistical information) may not be publicly
sclosed, or otherwise prohibits use by the State or any person in any action or proceedg against a person, the Secretary may use the information provided by the State only in
e same way that the State may use the information. (U.S.C. Title 46, 2011)

e can see from the letter of the law that the Department of Transportation was under
s not just to compile these data from state agencies in a consistent format, but also to
ate reports and make them public.
though the law does not give instructions about what data elements need to be col for the reports, the department later developed regulations that determine when
ng accidents must be reported, by whom and within what time frame. In addition,

egulations specify the minimum data that should be collected, including location,
and date, weather and water conditions, the availability and use of personal flotation

 s and more (Government Printing Office, 2001a, 2001b).
other federal database that was created to comply with the law is the U.S. Environmenotection Agency’s Risk Management Plan database. The EPA’s RMP database holds data

 certain chemicals that are produced, stored or distributed at facilities across the counhese RMPs are supposed to be a tool to help local emergency responders, such as firers and paramedics, to
 plan for and respond Accident Totals by Year ?

es and explosions, like 300

```

```
eadly one at the West
izer Company in the

```

```

```

```
 of West, Texas, in 200

e EPA does not post the
ase online itself: the | 10°F
 to Know Network, a 50
t ofthe nonprofit Center
fective Government in 2004

ngton, DC, postsit. Visi
othe RTKNetwebsitecan — Source: Risk Management Plan Database. (n.d.). The Right-to-Know Network.
ne data that have already Retrieved j July 10, 2013, from http://www.rtknet.org/db/rmp/s ; } t.org/db/rmp/search.

    arized. such as this Note: U.S. hazardous chemical accidents by year. The nongovernmental Right

```

```
 Facility and parent names

               Facility Name 23)

           Parent Company Name ?:
  Facility, Parent, Owner or Operator Name 7:

 Location

         County

          State

         Zip Code

  Congressional District 2).

 Other search criteria

 Executive Summary Text ?:[

            Industry :? 2
          ee (searches alt pre

 Display options

  Level of Detail |?) §

   Output Type ®

    Sort order 7's: By fa

                                    Search Clear

urce: Risk Management Plan Database. (n.d.). The Right-to-Know Network. Retrieved July 10, 2013, from http://www.rtk
rg/db/rmp/search.

te: Right to Know Network’s U.S. Risk Management Plan search screen.

eportable accidents by year. Site visitors can also run more-complicated queries using a form

ill down and get details about particular facilities (Center for Effective Government, n.d.).
 Established in 1970 by President Richard Nixon, the EPA is in charge of enforcing fe
ral air, water and ground pollution laws. (In some states, the EPA has delegated duties

tate-level agencies.) The RMP database has its roots in the Clean Air Act of 1970, whic
ought to curtail air pollution caused by urbanization and industrialization.
 Twenty years later, President George H. W. Bush signed into law amendments wi
rovisions intended to prevent chemical accidents. The EPA developed rules and requir

cilities to comply by 1999 (Environmental Protection Agency, n.d.b).
 The regulations specify which 77 toxic and 63 flammable substances facility owners mu
eport, and at what threshold quantities. For example, facilities that have 10,000 pounds

nhydrous ammonia must report to the EPA (Chemical Accident Prevention Provision

994). The fertilizer factory in West had 54,000 pounds on hand in June 2011, according

he most recent EPA data on the RTKNet website (Center for Effective Government, n.d.).
 In other instances, government agencies create databases on their own initiative,
elp them meet their own strategic goals. The National Highway Traffic Safety Administr
ion is supposed to reduce deaths, injuries and economic losses caused by motor vehic

ccidents in the United States (National Highway Traffic Safety Administration, n.d
HTSA, part of the U.S. Department of Transportation, developed the Fatality Analys
eporting System database in 1975 as a tool for monitoring fatal traffic accidents across

```

```
                                                     SUBSCRIBE; SEARCH } Home

 NATIONAL 146)
 SRBELY, KOU DRIVING SAFETY { VEHICLE SAFETY { RESEARCH LAWS & REGULATIONS | ABOUT NHTSA

              Detailing the Factors Behind Traffic Fatalities on our Roads 
                  FARS is a nationwide census providing NHTSA, Congress and the American public yearly ‘
               data regarding fatal injuries suffered in motor vehicle traffic crashes. % NCSA Publications and Customized Data
                                                            Requests (CATS)
           How to Access FARS Data
             — EON yp / aR

              < Create your own fatality data run ontine by using the FARS Query System, Or download
                     ali FARS data fram 1975 to present from the FTP Site.

                         %» Fass a Query Using the FARS Web-Based Encyclopedia

                              >} 2010 FARS/MASS GES Standardization -- Posted 12/8/2011

                    » FARS and GES Auxillary Datasets Q & A -. Pested 9/9/2010 These files will
                 complement the standard FARS and GES files by providing new variables that have

                   been derived from all the commonly used NCSA analytical data classifications (e.g.

                    speeding related, race and ethnicity, etc).

                              * FARS Manuais and Docuntentation

                       2? 2003 FARS/NASS GES Changes (Sept. 14 Webinar Recording) -- Posted 9/23/2010

                    * Download Raw Data fram FTP Site

: National Highway Traffic Safety Administration. Retrieved from http://www.nhtsa.gov/FARS.

Fatality Analysis Reporting System home page.

try and giving researchers data that they could use to examine the causes. State agen
collect the data about the fatal crashes and then provide them to NHTSA, which com FARS and releases the data annually to the public. Transportation planners, safety
ates, journalists and attorneys all have used the data for research. NHTSA itself has
the data over the years to generate dozens of analytical reports available for download.
HTSA allows site users to query its data using a series of Web forms. More-advanced
users, such as those who have experience using database managers, can download raw
files back to 1975—the inaugural year for the database.
e can see that governments have different motivations for collecting, using and making

public. That’s important for us to consider later when we're testing our data, using integhecks. Our goals for working with the data can differ greatly from the goals of the people

e the agencies that collect them. For instance, we may be interested in determining
h industry group’s employees contributed the most money to candidates running for
nor in our state. However, our state probably records the occupation and employer—
ot industry category—of each contributor. That means we won't be able to answer that
ion without a lot of additional research and changes to our campaign contribution data.

S FROM DATA ENTRY
 begin to develop a data state of mind, we should keep our eyes open for clues that
rnment agencies are creating databases. Agencies have a multitude of ways to enter
into a database, some of them high tech, others rooted in the paper-bound ways of the

century.
      Fatality Analysis Reporting System (FARS)

```

```
 We may see government workers collecting data in the field using handheld c
puters as part of their jobs. For instance, parking enforcement officers in your
and on your campus might be using devices that allow them to enter violation d
and to print out, right on the spot, a ticket that looks like a store or ATM rece

Some units, which look like big, rugged calculators, have number and character
tons for the data entry. Others have touchscreens with styluses. Some even c
with GPS receivers so the officers can record the precise location of where a park

violation occurred. In a similar vein, other government agencies, such as fire depa
ments and health departments, have been using tablet devices to input onsite insp
tion data.
 When we see this data collection, we can assume that the data do not stay in the i

vidual handheld unit or tablet. In fact, these data later are transferred to a centrali
database that holds all of the inspections.

  Likewise, police officers do data entry in the field when they respond to calls from
dispatch centers. With the aid of their ruggedized laptop computers mounted next to t
in their cruisers, they use templates to enter distinct pieces of data about the report.
instance, an officer might enter data about the location, nature and outcome of an
dent, and the name and contact information of any witnesses interviewed at the sc
When the officer has completed the report, he or she can send it to the police departmen
centralized incident reporting system.

  Most data entry, however, is nowhere near as advanced. A lot of data entry is d

using paper or Web forms, so we should look for those, too, as clues. It’s hard to beli
but a lot of data at government agencies are entered manually. A clerk sits at a compu
and keys in data that someone has entered on a paper form. So, if you see someone ente

data in a government building, casually ask them what they’re doing and about the
they work with. Sometimes government agencies scan their forms and use software
digitally extract the data.
  If you're interested in a database, get a copy of the form that’s used to feed data int
Forms tell a lot about what you can expect to find in databases. You should assume tha

of the data collected on the form will be entered. You may be incorrect, but you sho
start with the assumption that more data are available.
  Here’s a good example of a government form used to collect data. The U.S. Bur

of Alcohol, Tobacco, Firearms and Explosives licenses firearms dealers, which incl
big box retail, sporting goods and hunting shops. Whenever a federal firearms lice

(or FFL) loses or has firearms stolen, the licensee must report that loss or theft to
ATF’s National Tracing Center within 48 hours. The ATF enters the data about
stolen firearms into the database and later searches them when law enforcement a

cies want to trace guns that were used in crimes (Bureau of Alcohol, Tobacco, Firea
and Explosives, n.d.).

```

```
Department of Fustice OMB No. 1140«0039 (07/31/2612)
u of Alcohol, Tobacco, Firearms and Explosives Federal Firearms Licensee Firearms
                     Inventory Theft/Loss Report

 tries must be in ink. Please read notices and instructions an reverse carefully bejore completing this form.
on A - Federal Firearms Licensee Information
l Firearms License Number Federal Firearms Licensee Telephone Number (Include area cade)

/Corporate Name

 Address of Federal Firearms Licensee

                                              Telephone Number (with arc code)

ame of Person Making Report

 Address of Person Making Report

on B - Theft/Loss Information
                                               Description of Incident
of Thefi/Loss Discovered L |Burgtary [TRobbery

                             fl Larceny cle issing faventory
 Notification

Notification

 and Telephone Number of the ATF Represeatative Notified (if this report is the result af an ATF compliance inspection, provide the name
elephone number of the ATF Inspector)

 Description of incident fe.¢.. How firearms were stolen, ete:

                                                          Serial Number

fication

eby certify that the information contained in this report is true and correct. | also understand that failure to report the theft or loss
irearm from my inveatory or collection within 48 hours of the discovery of the theft/loss ts violation of 18 U.S.C. § 923(¢16) panishas a felony.
ture of Licensee E

                                                                  AT? Form 3316.11
                                                                         Revised Seprembes 2009

 Bureau of Alcohol Tobacco, Firearms and Explosives, Department of Justice. Retrieved from https://www.atf.gov/files/
ownload/atf-f-3310-11.pdf.

ederal form used to report lost or stolen firearrns.

e boxes or fields on the form tell us exactly what gets collected. We see details about

FL, including license number and street address. The form asks for the contact

```

```
  It might be an overstatement to say government agencies love forms, but they certa
do thrive on them. In fact, if you type http://forms.gov in your browser, you'll land a
federal government’s portal for forms.

  Home | FAQs | Site Index | €-mail Your Question | Chat | FREE Publications Get Email Updates | Change Text

  AT: ah “yy * LES LOL TESTE TO j =
  USA«g * | |D searnthesovenment.. ss fe Oe ome)
        Government % Made Easy 1-800-FED-INFO (333-4636)

      Services Blog Topics Government Agencies : Contact Government SSS SSS

    Home > Reference Center > Government Forms be} Download Adobe Reader

  Government Forms

    Find federal forms and applications, by agency name.
                                                              Tax Forms

       Share iv] Tweet £-mail This Page ° tt
                                                                                                                     ile Y¥¢ fia
information of the person making the report; details about the theft or loss, inclu
when local police were contacted; type of incident; and a brief description. Also, th
space for data about the firearms stolen or lost, including the manufacturer, model
serial number.

```

```
* Tax e-File

```

```
                                                         vidual
Top Requested Forms An

```

```
Return Form (PDF)

```

```
      * 1049 (PDF) ~ U.S. Individual Income Tax Return % Ee Retur no eee na (POF)

       * 941 (PDF) - Employer's Quarterly Federal Tax Return ; * 1040EZ Individual Income
      * L9 (PDF) - Employment Eligibility Verification Tax Return Form (PDF)

       * V4 22-1995 (PDF) - Request for Change of Program or Place of Training | * IT: lait!
      . W-9 (PDF) - Request for Taxpayer Identification Number and Certification

   Administrative Office of the U.S. Courts
a ee ee eee

Source: Retrieved from http://www.usa.gov/Topics/Reference-Shelf/forms.shtml.

Note: Website for forms used by federal agencies.

  Some of the forms accessible from this portal are Web forms, not documents
as Microsoft Word or Adobe Acrobat files. More agencies, large and small, are emp

ing these online forms to collect data. For example, anyone who wants to ha

parade, run or other event using the streets in the city of Columbia, Missouri,

complete the following Web form, then click the Submit button. These data the
from the form into a database administered by the city. The form’s URL, which
-php extension, is our clue to the presence of a database. PHP is a programming
guage that lets Web forms pass data to databases. Also be on the lookout for

(Adobe ColdFusion) and .asp (Microsoft Active Server Pages), which can also
data from a Web form to a database. By examining the city’s form, we know th

```

```
 or Later Save & Continue Cancel Changes

 NT INFORMATION

 the applicant organizing this event on behalf of another organization? *

               Name: *

                 David Herzog

                  E-mail Address: david.herzog@gmail.com

                     Streel Address:

                   City: *

 ARY CONTACT: pols

                   E-mail Address:

 CONTACT Name: *
 nt than appiicant):

 INFORMATION

 NAME:

CATEGORY: * |
                             | Procession/Merch | Non-Competitive Athletic Event

                        ConcerlPerformance i Neighborhood Biock Pany

 City of Columbia, Missouri. Retrieved from https://Awww.gocolumbiamo.com/CMS/special_events/step1.php.

ty of Columbia, Missouri, form for parade permit applications.

 FROM REPORTS

we've been looking at how 2012

collection can help us TEXAS HUNTING INCIDENTS

r clues about databases. ANALYSIS
e're going to look at how

oducts of databases, such
rts, can help. Another way
king about this is that data

ion provides the input,
 provide the output.
 we saw earlier, agencies
ollect data to fulfill legal
tes or help them meet
ic goals. The same applies
ncies issuing reports. In

n, executive agencies—at
eral, state or local level—
 generate reports using
 the request of the legisladies that oversee them.
 Texas Parks and Wildlife
tment regulates hunting

```

```
uses to produce annual reports (Texas Parks and Wildlife Department, n.d.). These re

underlying data for this report came from a database.
summarize accidents for the year and, in some cases, provide data from other year
comparison. The summarized tables, like the ones below, provide a good clue tha

```

```
EQUIPMENT

Muzzleloader

```

```
   Percentage in parentheses (%)

0 Fn a
ins ei al —

```

```
Source: Texas Department of Parks and Wildlife, Retrieved from http://tpwd.state.tx.us/publica
pwdpubs/media/pwd_rp_k0700_1124_2012.pdf

Note: Table in hunting accidents report.

 We get an even stronger indication that these data came out of a database when
arrive at the section that provides details about the individual hunting incidents. (Two

accidents from 2012 are shown below.) Each has a header for the date, county, shoo

age, gender, firearm, animal hunted, whether the accident was self-inflicted and whe
the shooter had taken a hunters’ education course.

       2012 FATAL INCIDENTS FIREARM/BOW HUNTING RELATED (A)*
  *A. Firearm/Bow & Hunting Related—An accident/incident resulting from the discharge o
  a firearm or bow while hunting, which causes the injury or death of any person(s).

            Shooter’s Animal Self- Hunter Ed?
   Date County Age/Gender Firearm Hunted Inflicted? (Shooter)

   4-2 Bexar 36/M Rifle Opossum No No

  Comments: Shooter shot at an opossum after dark and did not see that his friend was
         the line of fire.

  Prevention: Always point the muzzle in a safe direction; always stay within a safe zone of
          fire; communicate with hunting companions; know where others are posi         tioned at all times; never fire from behind others; complete hunter education.

   11-10 Polk 42/M Rifle Deer No No

  Comments: Shooter was unloading his rifle at the rear of his truck after hunting. Gun
        discharged through the rear of the vehicle, striking victim in lower back as
        he sat in the cab of the truck.

  Prevention: Always point muzzle in a safe direction; treat every firearm as if it is loaded;
        handle firearms carefully; complete hunter education.

Source: Texas Department of Parks and Wildlife. Retrieved from http://tpwd.state.tx.us/publications/pwdpubs/media/
k0700_1124_2012.pdf

```

```
e U.S. Consumer Financial Protection Bureau began operations in 2011, the year
 t was established by the Dodd-Frank Wall Street Reform and Consumer Protection
odd-Frank sought to stem many of the mortgage, credit card and other consumer
ng predatory practices in the 2000s. The bureau takes and investigates consumer

aints. Consumers can even use an online form, such as this one, for credit card
aints.

f: fay Consumer Financial
 & > Protection Bureau

 ile a credit card complaint

 e'll forward your issue to your credit card company, give you a tracking number, and keep you
 pdated on the status of your complaint.

 . What 2. Desired 3. My information 4. Product
  happened? resolution inforreation

EG LEE,

 or credit card issues affecting your credit report, submit your complaint here.

 your issue is about debt collection actwites, submit a Gel

 esenbe what happened so we can underatand the isaue... *

 Consumer Financial Protection Bureau. Retrieved from https://help.consumerfinance.gov/app/creditcard/ask.

onsumer Financial Protection Bureau online complaint form.

 the summer of 2013, the CFPB released a 19-page report that provides a snapshot o
aints and how they are handled. The report relies heavily on summarized numbers
harts to communicate data about the complaints. Also, the report tells us that data
derived from a database of the complaints (Consumer Financial Protection Bureau,

 So no guesses here!

KS TO UNCOVER FORMS AND REPORTS

ng forms and reports on government websites can be a challenge. Many times, agen
catter them about rather than provide a centralized home for them, as the federal

 portal strives to do. Fortunately, we can use some Internet sleuthing tricks, using
e Advanced Search.
int your browser to http://www.google.com/advanced_search and you'll see a
interface that is much busier than the serene, default Google search page. The

```

```
a .gov) domain, or even for forms on the Pennsylvania Department of Education webs

words box. Then enter “education.state.pa.us” in the Then narrow your results by . .
or domain box. Now search and look at your results.
(education.state.pa.us). Go ahead and enter “form” in the Find pages with . . . all t

```

```
Find pages with..

ali these words:

this exact word or phrase:

ary of these words:

none of these words

numbers ranging from:

Then narrow your results
by.
language: any language

tegion: any region

last update: anytime

site or domain: ducation.state.pa.us

terms appearing: anywhere in the page

SafeSearch ‘Show most relevant results

reading level ‘no reading vel displayed

file type. any format

```

```
 To do this in the search box

  Type the important words: exicelor xav terrier

  Put eanct words in quates; “rat terrie:™

  Type Of betwern aif the words you want; miniature OR aban

  Put a minus sign just before words you don't want:
  -redent, ~*Jack Russehl”

“ist? perinds between the numbers and add ® unit of measure:
  20..95 tb, $200..3903, 7020..20%2

 5 Find pages in the lomuage you setect,

  © Find pages published in # pastiouier region,

  Find pages updated within the time you spacity.

  domain Smorch one tike site .edy, {ike .org witipedia. & ogo org ) or limit your results to a

“| Seurch tox terms in the whole page, page title, or web address, o
 | to the page you're looting for.

  Tet! SateGwarch whettver ta filter sexually explicit conten,

 A | Find pages at one reading level or just view the Jewel intes,

  Find pages in the format you prefer,

```

```
  usage rights Find pages you are tee to use yaursalt

Source: Google search.

Note: Google Advanced Search screen.

 You can also use the advanced search to restrict your results to PDF or Word file
using the file type drop-down list.
  After you get more experience running advanced searches, you can run them right f
the main Google search box by mimicking the syntax that appears after you run
advanced search. For our query, this says, “form site:education.state.pa.us”. Google tr
lates that as instructions for it to look for the word “form” anywhere inside the educat
state.pa.us domain. So if you want to look for forms on the EPA site, you'd type “f
site:epa.gov’. To get only PDF forms, try, “form site:epa.gov filetype:pdf”.
 Now that you are equipped with some tips for developing a data state of mind, w
going to tackle the world of online databases and develop some strategies for locating
downloading them. Being able to find relevant online data and download them is on
the key data literacy skills that you'll need to succeed.

ON YOUR OWN

Choose one of the two federal databases and find the law that led to the creation o
database: U.S. Food and Drug Administration’s Operational and Administrative Sys

```

```
e. Cite the law and write a few paragraphs explaining how the law made the datassible.
ry state has an agency whose mission is to collect and disclose political campaign
 data. Identify that agency in your state. Cite and summarize the law that gives the
 the authority to collect these data.
d a form that a federal, state or local government agency uses to collect data. Specify
you found the form, and include a URL if you downloaded it from the Internet.
data does the agency collect with the form? Try to find a corresponding database
and provide its URL if you are successful.

```

```
   =

                                                 7 : ate a : > '
at ot reed wet tn

```

```
imme, Bee shepard

```

```
> —
  +a iviemad apes ial

```

```
NT) Davie ¢ otra ae hi errpeics

```

```
    kegel

 } eu ee, i’ “arava
   ber? Ta) ont obit ghee
   ane Be ey
we is terns jueialerdl te

```

```
phone i

      b

```

```
            i. @ a _—>—~
         Lira oa <a Sie =

           . vile eng ay

            . eee a

   i rs! area
Vb ON Es 6 ae

      ATi lod © an
         yO. oO.
   = i

```

```
- S q

```

```
o

```

```
fy

```

```
Reticle Saar

```

```
PTER 3 ONLINE DATABASES

: perfect world, we would be able to easily download all of the data that we need from
  comfort of our computer keyboards. All government agencies, from the federal
 wn to the local, would post all of their public data on easy-to-find websites that have
 ell-indexed by search engines. The agencies would make their data available in for hat could be easily opened in our spreadsheet or other analysis and visualization
 ms. They would also provide copies of any documentation that we'd need to help
 tand the data, and make sure that the documentation is complete.
 t perfect world, of course, does not exist and never will. Although it’s impossible to
 the exact percentage of data that are available, it’s a safe bet that government agen general post less than half of their data online, despite the high-profile efforts that
 t of the open government movement. Agencies may post the data in formats that
 ficult to import into—or are too large for—spreadsheet programs. Agencies also
 st data without providing the documentation that users need to understand them.
 are all kinds of real-world challenges when it comes to finding the right data online
 ing them effectively.
 this chapter, you will learn effective techniques for quickly finding, understanding
 ing data sets from government agencies. Because the Internet changes daily, no one
 ate a list of must-know sites that we'll be able to use ten or even five years from now.
  best approach is to understand how government agencies store data online and
 the best practices that will help you find what you need in a reasonable amount of

 lso, when you find sites that you’d like to revisit, make sure you bookmark them so
 n reference them easily later.

 NATION: DATA PORTALS

 nment data portals have come into vogue with some agencies and members of the
  thanks to the Government 2.0 or open-government movement. The movement
 ig boost in May 2009, when the Obama administration launched Data.gov as a new
 destination for federal government data sets. The federal government's effort was
 modeled on efforts of early innovators, such as the D.C. Data Catalog.

 etimes, data portals can be frustrating to use. Agencies sometimes only link to
 g data, or they post only a limited number of data sets that might not be usetul.
#### `arm:`

```

```
  Besides the federal government, many other government entities have since laun

open data portals, such as Chicago; Austin, Texas; Montgomery County, Maryland;
Oregon. Some cities, such as Philadelphia, have partnered with nongovernment organ
tions to provide portals.

   Welcome to the City of Austin's
    Data Portal!

                      Suggest Data
                      Data aveMonth

                        Suggest a Data Set Ree) Set of the Month

                  Search & Browse Datasets and Views @
                     None
              Man No Gecered of Becksred Dangerous Dangerous Dog ne Gog Oty 204 Trem Sargon, County $099. Shouts otic ever aMteiy, be TUNMNG wets a amma wTye They ae CH SRreS fo be entrained at i hes and shoud be

                        Bunion Yom datas tecnico pesvibed fo hake 0h Location: rayon of atta tet Volos ite, Gharge const, xo Boughaut Os Chy of Aveta

Source: Dangerous and Vicious Dogs. (n.d.). City of Austin. Retrieved August 16, 2013, from austintexas.gov/depar
dangerous-and-vicious-dogs

Note: Data portal for city of Austin, Texas.

  open Connecting people with data

   d & Data on the Philadeiphia region is plentiful. Search and find that data
    ata on OpenDataPhiily and begin transtorming your city.
   PHILLY

                Search for data ‘

   DATA

    All Data

    Arts / Culture / History

    Budget / Finance

    Economy

    Education

    Elections / Politics

    Environment

    Food

    Health / Human Services

    Parks / Recreation

```

```
    Planning / Zoning

    Public Safety

    Real Estate / Land Records

Source: Open Data Philly. Retrieved from http://www.opendataphilly.org/.

```

```
Greater Philadelphia Geollistory Hetwrork by PACS
           906 the Athensoura of Philadelp

```

```
Note: OpenDataPhilly portal. The city of Philadelphia partners with a nongovernmental organization to make data available to th

```

```
end some time on the so-called open data sites and you notice some similarities
ms of the functions and appearances. That’s because two major data-hosting Web
orms—Socrata and CKAN—dominate. Socrata is a Seattle-based company that sells
n-data platform services to government agencies, numbering at least three dozen in

mmer of 2014 (Socrata.com, 2014). CKAN, on the other hand, is an open-source
atalog program that government agencies are allowed to deploy and use with no
ing costs. CKAN was developed by the Open Knowledge Foundation, a nonprofit
zation based in the United Kingdom.
’s explore one of the Socrata-powered sites: data.austintexas.gov. This is the offien data portal of the City of Austin, one that’s pretty manageable in terms of size
ase of navigation. The bottom half of the landing page lists data sets posted by
ty.

h & Browse Datasets and Views =

    Rame
   Map of Declared Dangerous Dogs ov
   No declared Reagerous Dag i the Cty of Austin and Trav €

    Municipsi Court Violation Location ©
    ‘This data is provided t¢ hain with anaiyss ot yErous ve the Cty of Auste

    Prowdies peeps restaurant inspection scores ee tor # m so insk three years. Oaine search of this data set alsa eeaiable sf
   Water tet 4 cnbertad Quality to Sampling assess a er aay i. creeks, i aquifers ah series and iakes in the Austin ares. Tha is rw ditts, provided deettly Irom aur Fats Sampie :
   Unclaimed YisL Biosterurer Property chaustiste.18/fnenceonte *wrge2dpges for formation yon find vous seme on the tal, Every year. various danartrants of
   Restesrant Inspect erst e
   Prpdes restaurant lor nspactinns performed watvn the tant tres years

```

```
Austin Lacation Fire nfsraation Station

```

```
fire, Be, ations, 96 stations

```

```
   Construction Plans in, SIBR's Pian &
    Hard copies of plans and drawings freee . Austin Idependest School District, Travis County, University af Texas at Austin, University of Texae Syston,

   4% ADORES SING - ADDRE $s CHARGES
    Oty of Austin sad Travis County eddress
   pone! Finance Online eCheckbaok ger & 8 @
     Me data set of the dats found i the Austin Fance Gaine

 Retrieved from Data.austintexas.gov.

 stin, Texas, data set listing on portal.

er we click on the link for restaurant inspection scores, a list of the inspections
s. Click the About button at the upper right and we get information about the data
ill help us understand them [better. ] [For ][instance, ] [we ] [see ] [that ][the ][data ] [are ] [for ][inspec-]
dating back three years, that they [have ][19,964 ][rows ] [and ][that ][they ][are ] [updated ][weekly]
 city Health and Human Services Department.

```

```
 About This Dataset

  Contributors 0

 ES Meta

  Category

  Permissions

  Tags restaurant, geodata,
                    health, fdheatth

  Row Count 18892

 gg Links

  Permalink hitps://data.austintexas.go:
                        inspecti

```

```
Short URL

```

```
 https /data.austintexas.g
CSI CR SOT Te)
             in

```

```
  ¥@ Licensing and Attribution

    Data Provided By City of Austin

    Source Link {none} |

  3 Additional Information

    Frequency Weekly

    Department Health Soe ees:
                           TVICES

Source: Retrieved from https://data.austintexas.gov/
dataset/Restaurant-Inspection-Scores-Chart/hqa6-stx4

Note: About box on Austin data portal. This box provides
some important information about the data provided.

```

```
  Before we download any data, we need
practice safe computing and document our wo
Create a word processing document or

 file with the name Data_Notebook; thi
going to be where we take notes about the data
get and what we do with them. Enter
 date, then “Austin restaurant inspections”
the URL “https://data.austintexas.gov/datas
Restaurant-Inspection-Scores/ecmy-9xxi”. Do

 forget to include details about the data, suc
 the number of rows, time span, update freque
and source.
  Now, on to downloading the restaurant ins
 tions file in Excel format onto our computers. C

 the Export button, then Download as XLSX to
 the most current Excel file format. It may take a
 seconds to download the file, depending on
 Internet connection and computer proces

 speed. Look for the downloaded Restaura
 Inspection_Scores.xlsx file and then open
 Excel. Now we have a copy of the file that we c
 analyze.
  Let’s practice safe computing again and m

 sure we downloaded all of the data: We can see

 we downloaded all seven columns. To check

 rows, hold the Ctrl and End keys on your keybo

Restauiers inspection, Scoresites « Ext 7 Ww 
```

```
      INSERT PAGELAYOUT © FORMULAS «(DATA REVIEW RW perros, Devia
      Asal WK x 4 ape QZ f e- eee Bip tot General eee ami? : ee, “2 (3 Eg | ecg Bl autesum ~ A oY Ly
 F Format Copy = Paints Meu. a ma- PEGE Bi hege& Center ~ $- % + “hgh Formattingy Conditional Formaten Table Styns7 Cub * +e i? Clee Sor Filtes & © Select Find & ©
Ahpboees * Fatt 4 Atigniaent % Humber % ‘Ste 6 Eviting

               Restaurant Name

```

```
40637887 Routine inspection
2801033 Routine Inspection
2801033 Routine inepection
2801033 Routine Inspection
7863033 Routine Inspection
10263619 Routine inspection
10263619 Routine inapection
10263619 Routine Inspection
10263619 Routine inspection
10263619 Routine inspection
10263619 Routine Inspection
A0GF7EAG Routine lnepaction
10677646 Routine inspection
10677646 Routine inspection
10632697 Routine inspection
19832697 Routine inspection
10679400 Routine inspection
 2800407 Routine inspection
 2800407 Routine inspection
 2800407 Routine Inspection

```

```
  111 Murphys Oot 76101
  15th Sreet Cafe "78701 09/13/2012
5 45th Street Cafe "e701 952272013
  16th Street Cafe ‘e701 01/28/2012
  15th Street Cale "78701 962372011
  4st Down and Stassney Sport 78745 09/29/2042
  4st Down and Stasenay Sport 78745 0412/2013
10 4st Down and Stassney Sport 78745 02/05/2010
  4et Down and Stassney Spor’78745 ope22012
12 Ist Down and Stassney Spot'78745 03/01/2011
  4st Down and Stassney Spot 78745 09/1272014
44 Ast Food Mart "7704 OBTZ13
15 | 1st Food Mat 7 o7r2gi2012
16 1st Food Mart 7 02/14/2013
 1-Stop Food Store 9321/2012
  1-Stop Food Store % 99132012
19 219 West 7 4270512012
21st St. College House 7 41/07/2012
  21st St. College House 7 422041
  21st St, Cofege House y 0802/2010
2 2st St. College House 02/03/2012

```

```
111 Murphys Oot 76101
15th Sreet Cafe "78701 09/13/2012

```

```
 83 111 CONGRESS AV
 93-303 W 15TH STAUS
 1 303 W 15TH STAUS
 93-303 W 15TH STAUS
 BE 303 W 15TH STAUS
 94 730 W STASSNEY  90 720 W STASSNEY
 87 730 W STASSNEY
 90 72.730 730 Wf W STASSNEY STASSNEY
 90.730 W STASSNEY
 100:1440'S 1ST STAUS:
 $F 1440 S 1ST STAUS
 97 1410 S 1ST STAUS”
 92 5101 AIRPORT BLY"
 976101 AIRPORT BLY.
 86 612 W GTH STAUST
 92 707 W 21ST STAUS

```

```
                                    85.707 W 21ST STAUS 2800407 Routine inspection
 House House y 0802/2010 02/03/2012 nannenna te 87707 707 PARR W W ALA 21ST 21ST ARAB IS. STAUS STAUE PAD 2800407 2800407 ann Routine Routine inspection Inspection
Restaurant Inspection Scores a fet

```

```
r at the same time and Excel takes you to the bottom right corner of the spreadsheet

sers, use the Command and End keys). We see that we have the same seven columns

e top, as well as 19,965 rows (one for the headers and 19,964 for the data, just as
in the About box).
n data portals also allow us to search. Let’s say you're an intern for a local
services agency that wants to better understand affordable housing in Austin.
e search box at the left of the data.austintexas.gov page to look for affordable
g. The results show us that the city indeed does offer data about affordable

g.

 Retrieved from Data.austintexas.gov.

 tin data portal search box.

w let’s go to the data portal for the federal government, Data.gov, which is built on
AN open-source platform. There are no data directly on the home page, but users
 to the data via the topic icons or the search box.

```

```
@ DATA GOV

```

```
DATA TOPICS+ IMPACT APPLICATIONS DEVELOPERS CONTACT

```

```
The home of the U.S. Government's open data

                   GET STARTED
                     WER 154.498 DATASETS

 Monthly House Price (ndexes

BROWSE TOPICS

```

```
Srlence &
Dannnante

```

```
  th $

  Energy

Public Safety

```

```
PGRN

  Gisbat
Penstameanninh

```

```
Geospatial

 ie

Weather

```

```
Health

```

```
ie

Education
x

dots & Skills

```

```
 The easiest point of entry is through the Data tab, which takes us to a list of data
that we can browse, filter or search. In the summer of 2013, Data.gov cataloged more

161,000 data sets. That number might seem impressive, but it is a little deceptive
overstates the real number. Many of the data sets that Data.gov links to are extrac
larger databases. For example, the EPA provides links to download Toxic Release In
tory data by state (or federal territory) and year. So the EPA considers the 2009 TRI

for Rhode Island as one data set, even though those data are part of a national data
covering many years.
 One of the best ways to look for data is to use the powerful filtering tools that are
of CKAN. On the left sidebar of the data set page we can filter by data set type, tags,
mats, groups, organizations (or specific agencies) and community categories. We can
filters to further zero in on the data we want. Click on Federal Highway Administratio
the Organization Filter and get just the data sets posted by that division of the U.S. Dep
ment of Transportation. Data.gov updates your results, showing you the new number

   Filter by location

                   Search datasets @)
   Enter loca’

               35 datasets found Order by: Relevance Ea

                   Organizations
             Formats GSD

               FHWA Traffic Volume Trend Monthly VMT Report - April 2009

                     Federal Highway Administration, Department of Transportation ~~ The Traffic Volume Trends
                  mony report is a natinal data report that provides quality controlied vehicle miles traveled data
                       for each State for ail roadways
           as
  Dataset Type

               FHWA Traffic Volume Trend Monthly VMT Report - April 2010

                    Federal highway Adminstration, Department of Transportation — The Traffic Volume Trends

                     manily report is a natinal data report that provides quality controlied vehicie miles traveled data
                     for each State for all roadways
  Tags Clear All xs
   volume data (35}

  vt (35) FHWA Traffic Volume Trend Monthly VIMT Report - April 2074

   vehicle miles traveled (35) Federal Highway Administration, Depariment of Transportation — The Traffic Volume Trends
                   monty report is 4 natinal dala report that provides quality controtied vehicle miles traveled data
   tvt (35) for each State for all roadvays

Source: Retrieved from http://catalog.data.gov/dataset.

Note: Search results for Excel files from the Federal Highway Administration on Data.gov.

that you have filtered for the FHWA. Filter more by picking XLS for Excel under
formats filter. The number of results is even smaller and you now have two f
displayed.
  Clear the filters by clicking the Xs next to them both.

```

```
rching is pretty easy, too. Just type a search term in the search box and then click
magnifying glass and you'll get data sets that meet your criteria. At this point you
o apply filters. Let’s say we want to find data that might tell us about the declared
rs that have occurred in our state. So go ahead and filter for just data that come
he Federal Emergency Management Agency, which is part of the U.S. Department

eland Security. Some of these data, including the Excel file of declared disasters,
be promising.

STICAL STOCKPILES

r great way to learn more about online data is to tap into the websites of governagencies whose mission is to provide statistical data. On the federal level, this
s the Census Bureau, the Bureau of Justice Statistics, the Bureau of Labor Statistics,
ional Center for Education Statistics and the Bureau of Transportation Statistics.
 state level, you might find similar agencies, such as the Missouri Economic Research
formation Center.
 U.S. Census Bureau is one of the biggest data providers in federal government. In
s mission is to provide quality data about people and the economy. Many of us know
nsus Bureau because of the decennial census, which is an attempt every ten years
t every person in the United States for the purpose of apportioning seats in the
ouse of Representatives.

             People | Business// Geography | Data Research | Newsroom

Resources for Emergency j
Preparedness and Recovery y Morthly Wholesale inventories a
Available : Released Uy 2013 Report 17.00 AU BOT, FAG $500.9 B RY
 The Census Bureau produces timely local Caen gh
 data that are critical to emergency y Yj intetaational Trade Walance
 planning. preparedness and recovery y iy nos ecelbAhaep Ee -$45.0 B ¥
 fforts. The Emergency Preparedness j Released 8/0 AM EDT, T4413 121%
 page now pivddes access to information Li Vaanuticherars Conde »
 about tomado-afleded areas May 2013 Report $485.0 B b

                                                      Released 10.00 AM EDT, 7/23 Rew Orders:
                                Hay Construction Released 2019 Report 10,00 AM Spending EDT, 7AAS $874.9 B aa

                                        nail

Census Bureau, Department of Commerce. Retrieved from http://www.census.gov.

 sus Bureau Homepage. The Census Bureau generates a huge stockpile of data about people, business and government.

 that’s just a sliver of what’s available from the Census Bureau. We can find

raphic data that are much more detailed, as well as data about construction
ng, retail trade, automobile [registrations ] [and ][home ] [ownership. ] [Dig ][deeper ][and ]
ll find data about government employment, payrolls, debt levels, assets and

```

```
budgets. Browse the navigation tabs on the Census Bureau website to get an id
the data it collects and makes available. The bureau’s American FactFinder prov
an interactive tool that allows users to build customized tables from the decen

census and the American Community Survey, a data set with more demograp
detail. The trade-off is that the ACS is based on a sample of the population and i
as statistically reliable as the decennial census.
 The Bureau of Justice Statistics is a division of the U.S. Department of Justice
has published dozens of data sets about crime, justice and law enforcement (Bu

of Justice Statistics, n.d.). Criminologists, policy analysts and social scientists ana

these data to help identify trends in incarceration, hate crime, identity theft
human trafficking. The BJS regularly publishes reports that are based on its own
yses of the data, such as one in June 2013 that looked at indicators of school c
and safety in 2012 using the National Crime Victimization Survey (Snyder

Truman, 2013).
 The Bureau of Transportation Statistics is part of the U.S. Department of Transpo
tion and compiles data sets about air, highway, rail and waterway travel. It even has
about Canadian and Mexican border crossings and oil and gas pipelines. Commerc

     ted States Depariment of Transporiation

  RESEARCH AND INNOVATIVE TECHNOLOGY ADMINISTRATION oe “About RITA | Press Room | Programs | RITA Publications| Linrary |Contac

  Bureau of Transportation Statistics

    Data and Statistics ~ Subject Areas ~ library = a Policies and Methods < ROOM BTS © Contact Us

  Hurricane Sandy.
  East Coast Air Travel | Delays. ae

   What's New

     Friday, July 12, 2043

    Geographic Databases for 2013 Releasud
     Friday, July 12, 2013 - The U.S. Department of Transportation's Bureau of Transportation Statistics, a part
     of the Research and Innovative Technology Administration, released the 2013 edition of the Mational
     Transportation Atlas Databases {NTAD} this week

     Friday, July 12, 2013

     National Transportation Statistics Updat

              aft of the Research ene Innovative Technology Adnerastiation (RITA), today ae Niptional
     Transportation Statistics (N1S) . a wel oply SIENCW BIW DSU) ANGE

    Thursday, July 11, 2013

        s Resort Two Tarmac Deiavs Over Three Hours on Domestic Flights, Ne Tarmac Delay Longer Than
                       Race

Source: Bureau of Transportation Statistics, Department of Transportation. Retrieved from http://www. rita.dot.gov/bts/.

Note: Bureau of Transportation Statistics website.

```

```
operators, journalists and airlines use BTS data to evaluate the cost of flying, onrformance and general airport activity.
s own researchers and others have used the data to create reports about drunken
 container port activity and the impact of the 9/11 attacks on U.S. travel (Bureau

portation Statistics, n.d.).

economic and employment statistics, the U.S. Department of Labor’s Bureau of
tatistics is one of the best resources. BLS collects authoritative data about employ
he labor force, compensation, mass layoffs and inflation (through the Consumer

dex and other indexes). In fact, the BLS data are the source of the government’s
numbers for unemployment and inflation. Economists and economic development
onals use these data on the job. The best way to find the data is to navigate by either
area or database name.

              ATISTICS

   Subject Areas » — Databases & Tools ~ Publications ~ Economic Releases ~ Beta v

    Medical care benefits were available to 85 percent of full-time private
    workers in March

     Medical care benefits were available to 85 percent of full-time private industry workers in
    March 2013 versus 24 percent of part-time workers, Paid sick leave was available to 24
     percent of full- time and 24 percent of part-time workers.

    CPI for all items increases 0.5% in June; gasoline, shelter, medical care, food
     all rise

    On @ seasonally adjusted basis, the Consumer Frice Index for All Urban Consumers increased
     9.5 percent in June after increasing 0.1 percent in May. The index for all tems less food and la Gao itt’ yi lft

     energy rose 0.2 percent in June, the same increase as in May. The Monthly Labor Review gets a

     HTM, | PDE | BSS 7 Local and Regione cr new look

                                                     Monthly Labor Review enters its 99th year

     Real average hourly earnings remains unchanged in June with a sleek new design and an eye to

     PPI for finished goods rises 0.2% in Jun: finished core advances 0.2% future.

     U.S. import prices fell 0.2% in June, vite U.S. export prices edged down 0.1% read more»

    Job openings remain at 3.8 milla in May; hires and separations rates litte changed

    June payroll employment increases (+195,000), unemployment rate unchanged (7.6%}
                                                read more # < 4234 5 >

                                                              Archives

antac wicnnaatioNn

ureau of Labor Statistics, Department of Labor. Retrieved from http://www.bls.gov/home.htm.

au of Labor Statistics website.

 about early childhood, primary, secondary, higher and adult education can be

n the National Center for Education Statistics site, run by the US. Department of

n. The center is a trove of data about costs, enrollment and crime at universities
er higher education institutions. It also provides data about student to teacher
 public schools. Recent reports using the center’s data include looks at private and

```

```
 TOS NIUE eccmnces EDUCATION STATISTICS

    Publications & Products Surveys & Programs Data. & Tools Fast Facts Schoo! Search News & Events About ls

   Welcome to NCES
    The National Center far Education Statistics (NCES} is the
     primary federal entity for collecting and analyzing data related to
     education.

   What's New

     HCES releases national and state revenues and expenditures ees
     for public elementary and secondary education for School 44 op
    Year 2010-11 (FY 11) (lui £6)
     This First Look report presents state-level data on revenues by Did You Know?
     source secondary and education expenditures for school dy function year for 2010-11. public elementary » more infe and Pubiic scheol students in 28 states scored higher than their peers in
                                        the nation: students in 15 states ang the District of Columbia scored
                                        flower than their peers nationally. The interactive map provides
    Postsecondary Institutions and Price of Attendance in 2012- details. » infe
     13; Degrees and Other Awards Conferred: 2011.12; and 12- = sparta
    Month Enrotiment: 2011-12: First Look (Provisional Data Snapshot
     This report Data} First released (ui Look 9) repartis on May 21, a revised 2013. =! rssefesk ing of the preliminary Sth TIMSS GRADE international) SCIENCE 2011 SCORE Assessment 2)
                              US. AVG. : 525 US AVG 525%
     The Nation's Report Card: Trends in Academic Progress TIMSS Scate AVG. : 800 TIMSS Scale,AVG
    2012 (ur 27}
     This report presents the results of the NAEP long-term trend
    assessments in reading and mathematics administered during
     the 2011~12 school vear to 9-, 13-, and 17-year-old
     Students. more » info

                                    Statement of Commitment to Scientific integrity
    indicators of School Crime and Safety, 2012 (un 26) by Princinal Statistical Agencies "(246 KB)
     This report presents data on crime at school from the
     nercnartnas afehidante tasrhare nrincinale oni tha manors!

Source: National Center for Education Statistics, Department of Education, http://ies.ed.gov/.

Note: National Center for Education Statistics website.

public schools, and the most popular majors for bachelor’s degrees (National Cente

Education Statistics, n.d.).

AGENCY SITES

It’s smart to become familiar with how agencies store data on their own sites, because
some data are hosted on or linked to data portals. This is where the hunt for data c
challenging because agencies sometimes scatter data around. Use website navigation
to look for words like Data, Open Data, Transparency and Statistics.
 The Federal Deposit Insurance Corporation, for example, links to its data throu
Industry Analysis navigation tab, then Bank Data & Statistics. The data include the
mary of Deposits, which has data about the amount of deposits taken in at each
branch location. Marketing analysts and regulators use the data to examine the le
competition within banking markets.
  See if the agency has its own data portal or page by typing the following in your bro
www.agencyname.gov/data. For example, entering “www.epa.gov/data” takes you
EPA’s Data Finder page.

```

```
      Federal Deposit
      insurance Corporation
        Each & itor Insured to at 250,000 peninsured bank

    BIDS ARR | Consumer Zotecion | _ Rewdations & Examinations, | As

BSWORY Soalvais > Bask Cate & Statistic

 DATA & STATISTICS

rchable databases to find information on specific banks, their branches. and the industry.

sta Guide

ses & Reports
                                                                                          Spline Subscription Senses
 comprehensive financial & structural information about every FDIC-insured institution ° Cole Subscription Serce

rch

 © User Guides
   nan

 © UBPR Data

Federal Deposit Insurance Corporation. Retrieved from https://www.fdic.gov/bank/statistical/index.html.

deral Deposit Insurance Corporation data about banks.

icomw to EPA's Data Finder. This site is a single place to find a vast selection of EPA data igs
urces, organized into topics such as air and water that are in easily downloadable farmats. Data @§.DATA.c OY
nder points to data in deymioadabla formats to speed up environmental research For each data EROS ATIONS PEOPLE
urce, yo Can see a basic overnew, including the geographic scale god other contextual
 ormation. then access the data source itself. Visit EPA’s Developer Resources Page

PA data is a great toai for developers. Please visit EPA's Developer Resource page
ttps/iweere.epa.gov/developer!; to see how EPA's data and senices can be of use to you
                                                   Quick Finder | AU Topics
 A also encourages you to share haw the site meets your needs and could be enhanced to help
u in the future. ‘ Please 3 visit the Data and - Developer Forum and share your ae comments and hie Ait Geatity cows Hazardous Radevaniick Waste — Spaciek Saiks & Land

ggestions Chemicals Haat Ettects Surtace Water
                                                     Cheap Citmate Change Health Manitoring Risks Wasies Watersheds
                                                            Pesticiles Viator
  Air| Climate Change | Health Risks | Pollutants & Contaminants { Waste | Vater
           View All Topics | Views Al Data Sources

```

```
r

 « Air Pollution
 ° Air Quality
 * Climate Changes
 * fore air topics

p of page

```

```
1) Basic Information

  Data and Developer Forum

```

```
Environmental Protection Agency. Retrieved from http://www.epa.gov/data/.

vironmental Protection Agency data page. Try to find agency data pages by typing “/data” after the agency's main URL.

```

```
datamo.gov
   State of Missouri Data Portal By

                      Mis $ O UR‘

                           Storm Aware

   Open Meetings Calendar 2011 State Expenditures County Sheriff's Office adie Weather Alert
       10 to our Gren Mestings E siating tow erow of ative ay ystems

Source: Retrieved from Data.mo.gov.

Note: State of Missouri data portal. Try to find data portals by typing “data” instead of “www” ina URL.

NONGOVERNMENTAL RESOURCES

Data from government agencies are used widely because they are considered to b

authoritative record. In addition, government data (at least in the United States) are

sidered to be free of licensing rules that restrict distribution and use. For journalists, off
documents and data provide an additional benefit: protection against libel suits. The
report privilege provides a shield to journalists who base their news accounts on fair
accurate use of official sources.

  However, nongovernmental organizations (or NGOs) also offer online data that we
use for our analyses. The Right to Know Network, which we visited in Chapter 2, p

several databases from the EPA. The data are from the EPA, but are distributed b
Center for Effective Government through the RTKNet site. Aside from promoting gov

ment transparency, the center advocates for progressive revenues (Center for Effe
Government, 2013) or higher tax rates for people with higher incomes (and vice versa)
the other side of the political spectrum, Missouri's Show-Me Institute posts salary dat
public employees that site visitors can download into an ASCII text file. The institut
 Or you can try typing data.
portal, you would type “data.mo.gov’.

```

```
mental problems. The institute gets its payroll data from the State Department of
stration.

```

```
      Highest-Pad Employees Pay by Agency : Pay by Positions
    & or

 otes: Many employees have more than ane
 n. Look up above for a Gross Pay Total.

```

```
VaRes

```

```
      ‘ Employee
212 CLIT PATIENT WORKERS,

```

```
              Data Hotes: Gross Pay does not include
              Fringe Benefits or Overtime.

Agency 3

MENTAL HEALTH CUENTPATIENT W/CRKER

```

```
ULTURE YANGALA, SEKHAR MENTAL HEALTH STARS Peay SICIAN SPECIALIST 047,125
CTIONS RVATION i: j i #2032 SRIPAL, ; HUANGTP, MENTAL He HEALTH PHYSICH YSICTAN, $326,984
NTARY MIC DEVELOPMENT AND SECONDARY EDUCATION | ADUSLMILLL, Sone etree NARAY20A R, MENTAL teas HEALTH MEDICS: a OR $291,296 ;

```

```
 EDUCATE AND SENIOR ATION SERVICES { REDOY, CHANDRA § MENTAL HEALTH vs s STAR PHYSICIAN ae. TALIST eee 2,
 NCE, ARY Fiti INST AND PROF REGISTRATION i | RADMAPESH, REBOAH ANN MENTAL HEALTH STAFF SAYSICIAN SPECIALIST $242,377

```

```
RADMAPESH, REBOAH ANN MENTAL HEALTH STAFF SAYSICIAN SPECIALIST $242,377

```

```
 AND INDUSTRIAL RELATIONS 2012 HAYREH, DAVENREZ J. S. MENTAL HEALTH STAPE PHYSICIAN SPECIALIST RBZ ©
 ATURE HEALTH PONCE, ARMANDO &, MENTAL HEATH SR PSYOMATRIST $223,526 Se

```

```
Show-Me Institute. Retrieved from http://www.showmeliving.org/payroll.

ssouri state data posted on the nongovernmental Show-Me Institute’s website.

ore using data from a nongovernmental source, ask,

How did the NGO obtain the data?
What did the NGO do to process or change the data?
What interest does the NGO have in making the data available?
Can you get the data directly from the official government source instead?

e NGO sites collect data that are not from governmental sources. The Roper Center
University of Connecticut and the Gallup Company both offer access to archives with
 opinion polling data. The Inter-university Consortium for Political and Social
ch at the University of Michigan archives data from social science researchers. If
ollege or university is a member of the consortium, you'll be able to download the
ssuming your computer is connected to your institution’s network (Inter-university

tium for Political and Social Research, n.d.).

SEARCH TRICKS

we used Google Advanced Search to uncover clues about data, we can use it to find
les that we can download. The trick is to think of words that appear on webpages

```

```
page at http://www.epa.gov/data for some ideas. We see that “downloadable” and “d
appear multiple times, which leads us to believe those terms will work well for our se
Go ahead and try “downloadable data site .gov” to look for pages with “downloadable”

“data” on websites that have .gov extensions. Your results list should have a mi

federal, state and local websites. Of course, you could try to narrow your search further
example, if you wanted to find only Excel files add “filetype:xls”. Try different search te

such as “download data,” and see what happens.

DON’T FORGET THE ROAD MAP

When downloading data from a government website, make sure you also download a

of any documentation. The data documentation, often stored as a Word, PDF or o
document file, usually is essential in helping understand what’s in the data file. There’

standard name for the documentation, so it might be called record layout, file layout,
dictionary or something entirely different. If you can’t download the documentation,
to get a copy of it from someone at the agency, using contact information that’s on
website.
 Whatever the name, the documentation usually provides some key pieces of info
tion about the data set:

  e Table names, along with record counts for each table.
  e Column or field names in each table, along with a field description, type of

   (character, number, date, etc.) and width.
  e Codes and their meanings. Data are often stored in codes, so the documentat
   should explain these. |

  For example, the Federal Aviation Administration routinely collects data a
licensed pilots and releases some of these data in the Airman Directory Releasable
On the same webpage where the FAA releases the data in two different text file form

it also provides documentation for each (Federal Aviation Administration, n.d.).
example from the nine-page documentation for the CSV (comma-separated value

delimited text) file says we have a table called Pilot Basic, which has 13 column
fields, starting with UNIQUE ID and ending with MEDICAL EXPIRE DATE. A
the fields are formatted as A, or alphanumeric. (Alphanumeric data use charac
to represent numbers and text.) The lengths tell us how many characters
be stored in each column. The remarks provide information about codes used (se

remarks for MEDICAL CLASS) and that the dates are stored in the MEDICAL D
and MEDICAL EXPIRE DATE columns as MMYYYY (or month, month, year,
year, year).

```

```
 NAME FORMAT LENGTH

asic record file

 ID
& MIDDLE NAME
 AME & SUFFIX

                                   02 4)tyr> mm

```

```
tc position = 'A’ or ‘C’ followed by a 7-digit number

Blank if foreign address

```

```
DE
RY-NAME

AL CLASS
AL DATE
AL EXPIRE DATE

```

```
          ee

                 1=First 2=Second 3=Third (Certificate Type “P” only)
             MMYYYY (Certificate Type “P” only)
al olodpe a t DON ADEN IWWOSD MMYYYY (Certificate Type “P” only)

```

```
 irmen Certification Database. (n.d.). FAA: Home. Retrieved July 22, 2013, from http://www.faa.gov/licenses_
 s/airmen_certification/releasable_airmen_download/

 documentation for the Federal Aviation Administration’s airmen database.

OADING, UNZIPPING AND INSPECTING DATA FILES

inal part of this chapter, we are going to download, unzip and inspect a delimited
 We'll work with fuel economy data from the U.S. Department of Energy kept at
www.fueleconomy.gov/feg/download.shtml. Under Find and Compare Cars Data,
ad the CSV file to a location on your computer where you can easily retrieve it. Then
 the Documentation link, which is our guide to understanding the contents of each
 (Make sure you record the details about the data in your data notebook. Do this
f the data you download.)

 enror | Eneroy Efficiency & ; Oiice of Transportation ‘U.S. ENVIRONMENTAL
 Y | Renewable Energy 8 Air Qualy | PROTECTION AGENCY
w. fueleconomy.gov

      U.S. government source for tudt econum

     Save Money & Fuel

nload Fuel Economy Data

 onomy data are the result of vehicle testing done at the Environmental Protection Agency's National Vehicle and Fuel Emissions
 ory in Ann Arbor, Michigan, and by vehicle manufacturers with oversight by EPA,

               revi { f

           Eee rue ia Data

 epartment of Energy. Retrieved from http://www.fueleconomy.gov/feg/download.shtml.

 al government website for vehicle fuel economy data.

```

```
 Find the file using Windows Explorer (or Finder if you are using a Mac). Right-cli
the file and pick Extract All . . . to launch the Windows unzipping utility. Change th
tination of the extracted files if you wish and then click Extract. You now have a
called vehicles.csv that contains a file of the same name. The compressed files usual
called zip files and have a .zip extension.

             Name > Date modified Type

            @ vehictes.csv D223 227 PRA Microsnft Exen’ Conia Separated Valuer Fle 22.382 KS

Source: Department of Energy.

Note: Comma-separated values file containing data about vehicle fuel efficiency. Windows computers usually display C
as Excel files.

 Windows identifies the file as a Microsoft Excel Comma Separated Values File. Be

the .csv file extension is associated with Excel, you can double-click on the file to op
Use Ctrl-End to navigate to the end of the file; you'll see it has 33,847 rows. Close t

now and don’t save any changes, if prompted.
  Vehicles.csv is a text—not an Excel—file, so we can view it in a text editor program
Windows, we'll use Notepad++, which is a free and open-source program that w
download from http://notepad-plus-plus.org/. Notepad++ has many more features
the stock Notepad that comes with Windows; it can open larger files than Notepad
also. (Mac users, install TextWrangler, which is a free program available at http:/
.barebones.com/products/textwrangler/.)
 Open vehicles.csv with your text editor and you should see something like this:

     2 baxrela06, berrelaAo®, chargei20, charge240, cLry0S, cit 08, ct yA0S, cit yAON, CLLYCD, cit yE, CLE PUE, Coz, COB, Co2TALIpipeAspm, cozTailpipeGrm,
     ¢ 15.689436,9.0,0.0, 17%, 0,9, 423. 1904761904762, 21,0.0,0,0.0,0.5,0,0,0.0,4,2.0,Rear-Wheel Drive, 9011, (FF3),
     } 3 +950562,0.0, 0.9,807. 9090909050309, 21, 0,0,0,9,.0,0.0,0.0,0.0,12,4,9, Rear-Wheel Drive, 22020, (GUZZ

  i # 22.19587,0.9 D.9, 32%.49814814814225,27,9.6,5,5.0,9.%,0,0,0.0,4,2.2, Front-Wheel Drive, 2100, (FFS},

  i $29. Secrecy Ae 7%.0, 207. 9090903096908, 12,0.9,9,0.9,0.0,0.9,%,.0,8,5.2,Rear-Wheel Drive, 2850,,-1, 49
  j é 0.0, 27,0.0,0,0.0/0,0,0.0;0.0,- 4, ~2,0.9, 46? . 7368424252632, 39,0.9,0,0, 3 0.9,6.0,9,0,4,2.2,4-Wheel or Ali-Wheel

  j Be . 78.0, 803. B5454545484544,32,5.0,9,0.0,6.0,9.5,0.0,4,1.8, Pront-Wheel Drive, 66620, (F

  } 4,9,0,35$.48,25,9.9,5,0,9,9.0,0.0,0.0,4,2,8, Front-wheel Drive, 66029, (FFS),-1,22000,R

                                                                              249.9, 372. 2GLGSEG EGGERT, 24,9.9,0,8.9,9,.0,0,.0,9.0,4%,2.8, Front-wheel Drive, 57905, (FFS}
  | 19.8, 34%. 8076923076923, 26,0.0,5,8.9,0.0,0.0,0.0,4,1.6, Kront-Wheel Drive, $7005, (FS)

     i 43.1244, °. 9. 1,0.0,355.48,25,0.0,0,0.0,0.0,0.0,9.9, eaves Drive, 57006, (EFS),-1,2206,R

     i 12.657024,% +0,-1,-1,9.0,343 . BO7ESZ307E9ZS, 20, 5.0, 9, 0,0,0.9,9.9,4,1.%, Front-Wheek Drive, 57006, (FFS

       48.689436,90 (-4,0.0, 423.1994761904762,21,0.0,9, MRCS WT GE ore Drive, 59007, {FFS

    3¢-43.73375,0.9, 2,9,0, 379.291 6666666667, 24,0.9,0. 9,0.0,9,9,0.%,4,2.0,Front-Wheel Drive, 59007, (FFS)
        15 .629436,0.0, 2, ©, 42%, 4804764904762,22,0,0, 0,0.9,0.6,6.0,%,2.0,Front-Wheel Q Drive, 59007, (FPS

                                           7 8.8, &, G24,6453846353246, 33,0 %.5,0.0,0.0,%,5.2,Rear-Wheel Drive, 2850,,-1, $2

                          9,9.0,9.0,-1,-2,9.9,386,59130434782606,23,9.0,0,0.0,0.%,9.0,9.0,4,2.0, Front-Wheel Drive, 54207, (FF
                             12-9, 0.8,-2, "4,3. 2, 484.35, 20,%,0,9,5.0,8,6,9,0,0.9,4,2.5,Rear-Wherl Drive, 60092, (FFS),-1, 2780, 0, Re
                         2, ; 2G, 423. 2AOSTELS04T62, 22,%,0,0,5.0,0.0,9.0,0.0,4,2.3,Rear-Wheel Drive, $0030, (FPS}

                                                                                0.0,-4,-1,9.0, 967.7368421052632,19,5.0,9,0.0,0.0,0.5,0.9,6,2.8,Front-Whsel Drive,

                                          9.0, -2,~4,0.%, 967. 7362423052632, 19,0.0,9,0.0,0.0,0.9,0.0,6,2.8,Pront-Wheel Drive,

                                          +9.0, 355.4375, 16,9.9,0,9.0,9.0,%,0,9.0,8,4.0,Rear-theel Drive, iZ971, (GUZZLER} {FF
                                   7-1,0.0,555.4375,16,0.9,0,0.9,0.0,5.9,0.¢,8,4.0,Rear-Wheel Drive, iZ071, (GUZZLER) (F
                      > io Desa ais 0,683. SPEER E TOR AS) ay a. he % a td 9.9,9,0,0,0, Ser By By Rkos se Beare Soja (OR

                              Jength 11654408 fines : 73842 inst Colit Setc0]0

Source: Department of Energy.

Note: Comma-separated values in a text editor. Note the commas, which are used for column delimiters, and the compress

```

```
ooks like a mess, as if someone took our data and squished them together. Actually,
how comma-delimited text files are supposed to look. The first line contains the
for our columns. Each comma denotes a column break to Excel and other programs.
rst line of data starts on the second line. Use Ctrl-End to navigate to the end of the
ad++ file and you'll see we have 33,847 rows—the same number we did when we
d it in Excel.

w, let’s download, unzip and inspect some tab-delimited data that are produced
 Food and Drug Administration for its Total Diet Study, which is supposed to
r the levels of contaminants in food. The Total Diet Study was started in 1961 as
ram for detecting radiation. Since then, it has expanded to look for the presence of

ides and industrial chemicals in food (Food and Drug Administration, n.d.).
te to the analytical results page at http://www.fda.gov/ForConsumers/
merUpdates/ucm184293.htm and download the O 2008 file under the Elements
g. Find the file named FY 08 O results only.zip and unzip it. You now have a text
led FY 08 O results only.txt. Excel does not recognize the .txt extension as a native
 we can’t just click on it to open it. Instead, open it using your text editor. The file
 look something like this:

```

```
Food Meme nal Type Sample QueLifier Replicate # Element Cong Trace LOD LOG Refere: ies

"Milk, whole, fluid * o ARSENIC i) 9.02

"Milk, whole, fiuid ” a ARSENIC 7 @.01

"Milk, “hole, fiuid * ° ARSENIC : 0.0%

"Milk, whole, fluid * g ARSENIC me 0.04
"Milk, lowfat (2%3, fluid * oO ARSENIC

"Milk, jopfar (2%), fivid “ © ARSENIC
"Milk, Zowfay (2%), fluid “ ARSENIC
"Milk, lowfar (2%), fluid * © ARSENIC
"Milk, chocolate, loyfar, fluid" ©

"Milk, chocolate, lowfat, flseid * Cc
"Milx, chocolate, jgwfar, fluid * o
"Milk, chocolate, jowfar, fluid * 2

"Wilk, skim, fisid ™ ARSEXIC

"Milk, skim, fluid * BRSERIC

"Milk, skim, fluid * ARSENIC

“Milk, skim, fiuid " a BRSEUIC
"Milk shake, chocolate, fast-food * 0
"Milk shake, chocolate, fast-food " >
"Milk shake, chocolate, fast-fo0d ”" 0
"Wilk shake, chocolate, fast-food " 0

"Cheese, American, processed " 0
"Cheese, Bmerican, processed * © ARSENIC
                      wes

      length : 290947 Jimves : 16137 in:1 Col:1 Sel:0{9 Doss\Windows

```

```
200802
200802
209803
200804
200802
255202
209803

200804
20080%
200862
200203
200804
200804

206602

```

```
 x

 =

 Z

 cE)


WON eM MYkn

```

```
 Food and Drug Administration.

 first glance, no delimiters are in this delimited-data file.

in, because this is a delimited text file, it looks like a mess—with squisheder data. We notice that the first row contains the column headers. The data them start in the second row. Also, some of the data have double quotation marks.
are called text qualifiers and [are ] sometimes [used ][in ][delimited ] [text ] [data ][to ][denote ]

```

```
text that should be kept intact inside a column. Single quotation marks also can be
as text qualifiers.
  But where are the delimiters—the tabs? Tabs are considered ASCII characters, but
are hidden, so we normally don’t see them. In Notepad++, we can make them appea

going to View | Show Symbol in the menu, then selecting Show All Characters.

 Fle Gt Sevch Vow Emoding. Language Setinge Moco fun ee :
 poOhl Gs .Bl4 eh) 2 €\ ae) « 1 24/20 8e) 2 8 ee a) s+ Bee

 x ference Material Qc Level QC unit 2Cct Recyd
       KOM TD M2 6 ES (AS & SE IN FOOD BY ACID DIGEST. HYDRIDE AA)

       KOM ID M2 6 ES (AS & SE IN FOOD BY ACID DIGEST. HYDRIDE AA)

        KCM TD M2 6 ES (AS & SE IN FOOD BY ACID DIGEST. HYDRIDE AA}

        KCM TD M2 & ES (AS & SE IN FOOD BY ACID DIGEST. RYDRIDE AA}

          KCM ID M2 & ES (AS & SE IN FOOD BY ACID DIGEST, HYDRIDE AA)

          KCM ID M2 & ES (AS 6 SE IN FOGD BY ACID DIGEST. HYDRIDE BA)

          KCM TD MZ & ES (AS s SE IN FOGD BY ACID DIGEST. HYDRIDE AA) HGAAS

          KCM TD M2 6 ES (AS & SE IN FOOD BY ACID DIGEST. HYDRIDE Ak) HGAAS
               KCM TD MZ & ES {AS & SE IN FOOD BY ACID DIGEST. HYDRIDE AA)

               KCM TD M2 6 ES (AS ¢ SE IN FOOD BY ACID DIGEST. HYDRIDE AA)
               KCM TD M2 & E5 (AS @ SE IN FOOD BY ACID DIGEST. HYDRIDE AA)

                KCM TD M2 4 E5 (AS & SE IN FOOD BY ACID DIGEST. HYDRIDE AA)

        KCH TD Mz ES (AS & SE IN FOOD BY ACID DIGEST. HYDRIDE AA}

        KOM TD M2 ES (AS & SE IN FOOD BY ACID DIGEST. HYDRIDE AA)

        KCM ITD M2 ES (AS & SE IN FOOR BY ACID DIGEST. HYDRIDE AA)

        Kew ID M2 ES (AS & SE IN FOOD BY ACZD DIGEST. HYDRIDE AA)

               KCM TD M2 & ES (AS & SE IN FOOD BY ACID DIGEST. HYDRIDE AA)

               KOM TD M2 4 ES (AS & SE IN FOOD BY ACID DIGEST. RYDRIGE AA}
               KCM TD M2 4 £5 (AS & SE IN FOOD BY ACID DIGEST. HYDRIDE AA)

               KOM TD M2 & ES (AS & SE IN FOOD BY ACID DIGEST. HYDRIDE AA)
            KCM TD M2 & ES (AS 6 SE IN FOOD BY ACID DIGEST. HYDRIDE AA)

             KCM TD M2 4 ES (AS & SE IN PCOD BY ACID DIGEST. AYDRIDE AA}
             SCM TD M2 & ES {AS & SE IN FOOD SY ACID DIGEST, HYDRIDE AA} é
  a i

Source: Food and Drug Administration.

Note: Tab characters used as delimiters, no longer hidden.

  Aha! Now we can see reddish arrows. Those are the tabs that serve as the column de
iters. We also see some periods, which represent spaces. Let’s now scroll over to the
side of the file and we can see two black blocks with white text. They say CR and LF
mean carriage return and line feed. These are hidden ASCII characters that are use
denote an end of the data record.

                  One last check: Let’s use Ctrl-End to see
 e pen many lines of data we have. We should see 16,
                  including header row. Close the text file now.
 CS Recent Weavbceke Time to open the file in Excel. Start Excel
                 then Open Other Workbooks in the pane on

  fam SkyDrive left. Select Computer and then use the Br
                 button to the right to look for the extracted
                     file.
                We won't see any files because Excel is loo
                 only for native Excel files. Change the File
                 option at the bottom right to All Files and the

                      file appears. Open it, and Excel launches a
  / Normal text file Bos\Windows ANS. NS

```

```
tep 1, we need to tell Excel what kind of text file—delimited or fixed-width—we’re
ng. Excel has correctly guessed delimited. (Excel sometimes gets this wrong, so

ure to check this.) Our data have headers in the first row, so we need check the box
ys My data has headers and start the import at Row 1 to capture these data.

                  | The Text Wizard has determined that your data is Delimited.

         ¥f this is correct, choose Next, or choose the data type that best describes your data,

        Original data type

        Choose the file type that best describes your data: 
        @ Delimited ~ Characters such as commas or tabs separate each field,

        © Fixed width  - Fields are aligned in columns with spaces between each field,

       Start import atrow: 1

      [) My data has headers,

        Preview of file C\Users\herzogdi\Downloads\FY¥ 08 © results only\FY 06 O results only. tet,

            ‘Feod NoFood NameAnsi TypeSample QualifierReplicate #£lementConct
          OOSOLI"Milk, whole, fluid "0 ARSENIC Gmg/kg 0.010.04
          QO802i"Milk, whole, fluid “Oo ARSENIC Omg/kg 0.010.04
          OO803i"Milk, whole, fiuid "0 ARSENIC Omg/kg 9.010.04
                         #1luid “Oo ARSENTC Omg/kg 6.010.04

Microsoft Excel 2013 for Windows.

 p 1 in the Excel text import wizard.

he next step, we need to specify the delimiter character, so make sure the box for Tab
ked. (If we need to specify a character other than any of those listed, just check the

box and enter the character in the box next to it.) At this step, we also need to tell the
 that we’re using double quotation marks as text qualifiers.

                    see Foes Ye Yi x

         This screen lets you set the delimiters your data contains. You can see how your text is affected in the
       preview below.

        Delimiters

                 ©) Treat consecutive delimiters as one

                     Text qualifier: ~

                                   al Type Bample Qualizier Replicate #

```

```
General, which means Excel takes a look at the contents of each column and make
educated guess about the format. This can be a problem because we might have a co

that includes zip codes, some of which have leading zeros. Take 02818 in East Greenw

Rhode Island, for example. If Excel imports this as general, it will treat it as a number
lop off the leading zero, leaving a zip code of 2818. Fortunately, we have a simple w
around: making the column text. We really should make all of the columns text to
any import flubs that may delete data. We can always change the format of the colum
Excel later.
 We can change the formats for all of the columns quickly by highlighting the firs
umn, then scrolling to the final column and selecting it with Ctrl-click. Now that all o
columns are highlighted, select Text as the column data format.

                                                        .

      Text Import Wizard - Step 3 of 2 ~ ZF . oO a es)

        This screen lets you select each column and set the Data Format,

       Column data format

          General
          s “General converts numeric values to numbers, date values to dates, and
       @ Text all remaining values to text.

           “2 Date: MDY [x]

          Do not import column {skip}

         | Data preview

Source: Microsoft Excel 2013 for Windows.

Note: Step 3 in the Excel text import wizard.

 Now click Finish, and Excel does the rest of the work. Depending on your software
tings, Excel displays green flags, which are just alerts saying data that look like numb
have been formatted as text.

```

```
  & EY 08 © results oriy-ot - Excel 7m ~ nex¥| H
 OME INSERT © PAGELAVOUT © FORMULAS «DATA —oREVIEW «VIEW Herzog, Daniel + FON Li |

                               Alignment ae Nurntses te Styler Cents Esiting
          f& | 2oneo2

           5 E F 6 ) ‘ ° P
             | ay

           Biv: EE Marge & Center 4B GB Sort 8 Pind 2
                                                    ©
 ares ; a : L wiiiss. BF iB, wrap Text a a) a ie ex ihe Heth Sie nell oa #
 BL Mv . « $+ % + Conditional Formetas Cel} Clelete Porrnat SS
                                                              : Formatting’ Tables Styler Sater Select
                                    yy

          ae Insert
                                  ©»

```

```
*, Food 1 1 No Milk, Milk, Food whoo who Nar O Anal Type Sample Q' Replicate Arsenic Element assenic ‘0 '0 Conc Trace %. . . . ReferenceQC Level QC unit AC% Recy Result Oe KOM Methor KOM TE TE i
4 i, ci Milk, SAitk, who who O O ARSENIC ARSENIC ‘0 ‘0 f . : : ; KeMTE KOM TE |
* K 3 2 2 Milk, Milk, Milk, lowfO lowtO lowfo ARSENIC ARSENIC ARSENIC '0 0 0 % 0. . . . KemTe KOMTE KOM TE
2, 3 Milk, Milk, choco lowtO ARSENIC arsenic a 0 aCe . . KOMTE KemTe | |
$ Mitk, choco ARSENIC '0 0. 0. KOMTE
r 3 3 Milk, Milk, choco choco ARSENIC ARSENIC 0 "0. %. KOMTE
“a + r ( 4 Milk, Milk, Milk, skire ski skin ARSENIC arsenic ARSENIC ‘0 0 ‘0
3 Milk, skie 0 ARSENIC 'D
ed Mitk shake ARSENIC 0

```

```
   FY 08 © results anty

ood and Drug Administration.

 file successfully imported in Excel.

haven't yet saved this as an Excel file, so let’s do that by clicking on the File tab, then
g Save As. Browse to a location where you are storing your files, and select Excel
ok (*.xlsx) as the file type. That does it!
is chapter we've covered a lot of ground, starting with identifying useful data on

rnet. We also learned how to download, unzip and inspect ASCII files in a text

he next chapter, we'll turn our attention to how we can learn about all of the data
vernment agencies keep offline and how we can obtain them informally or formally
 open-records requests.

UR OWN

gle Advanced Search to find data that your state or local government keeps online.
ree examples of data that you found and a brief summary of each example. Also,
 the search syntax you used to uncover these data.
 the data portal for your state or local government. How did you find it? Provide
es of three data sets that are on the portal.

```

```
    x 1 ie.
popstar) — © iy Wy

 jl 4 1 a :

 | Bs im — . Gres
 ’ = i; -? (8p) 4_ 6
fe hn we ee Pele a 5
     7) ee tf ah: — tet

   oi ™“ Pm ~ 7 = a pon Z i

                      | f

       | ‘

                          <— by ina } ¥

ep a ata) pitty i 904 Baty vif ie a i

   1 / @te baa te? Gop? perv i]t Ba TY iy ress Donbir

                          ~ i =

   a} Hi Ps pall i) si uli sige i :
               f) mit : . me) :

TSS - aT ed ; A e
   hese “wT a ¢ i : = he
              — 2nd ey .

 aS =. ’ = - : & eas. ey '
 Siu) ft0h4 fev Never ‘a Dayyent Trl tae la alive
         lasdd

                                                              a
    im ul PF er iy hity brain a « wd eros)
   as Fee et VY a sine

   oly

                     ;
 i. te erernrenes Win a bye Dorian ome ager a Aitoly tuly
                . elke wont terns Agen) Th
 rapt “ae deity ‘, — uae be henduhl iy és bua

```

```
5 hen) 7 bait (ye tan wet hens mg Ae a ae wy

```

```
& ne si
                                                     ;
                               § Dani? 2198.4)
                Te - he

```

```
          oS.
‘ i “ a they wont rk

```

# `=a`

```
        S we saw in the previous chapter, government agencies are posting a growing num       ber of data sets on the Internet. However, most governmental data sets are held
        offline for a variety of reasons, such as lack of financial or human resources, politi      itivity and the perception that the public might not be interested in the data. Finding
      data can be tough, but it can be even more challenging to identify and successfully
      databases that government agencies store offline. In this chapter we will learn some
      ches for further developing a data state of mind to become more aware of these
      data sets. We'll also learn how to use federal and state open-records laws to make
      requests for these databases, which are public information. Knowing the name
      database and how it’s kept is key to making a successful request using the federal
     om of Information Act or similar state laws.
      Chapter 2, we learned that some government agencies collect and use data because
      required to by law or because it helps them meet their strategic goals. We learned
       can uncover clues about databases by looking for data entry with handheld com       or with paper and electronic forms and in statistical reports. In Chapter 3, we
      d about data documentation. We can use all of these clues to help uncover offline
      es.

      CLUES FOR OFFLINE DATA

      tools are particularly well suited for helping identify offline data. These are resources
       records retention schedules, audit reports, federal agency major information sys      stings and nongovernmental organization sites.
     cords retention schedules provide details about records held by state and local
     nment agencies, and guidelines about how long those agencies need to keep the
      . Each state issues its own records retention schedules for state records, and some      issues a separate schedule for local records. Unfortunately, there is little uniformity
      ne state to another about what’s in the schedules and how to access them. The
      a Secretary of State provides a lookup form for its schedule. The Florida Depart
      f State offers the information in PDF, Word or Excel format. The Utah Department
     inistrative Services offers the information as webpages that you need to click
   PTER 4 IDENTIFYING AND REQUESTING

       OFFLINE DATA

```

```
 REAL PROPERTY SALE FILES (ITEM 14-3)

 Records which document the transfer of state owned real estate to non-state
 ownership, whether by transfer, trade, sale, or donation.

 RETENTION

 Record copy: Permanent. Retain by agency for 6 years after a deed of sale is
 recorded and then transfer to State Archives with authority to weed.

 Duplicate copies: Retain until administrative need ends and then destroy.

 SUGGESTED PRIMARY DESIGNATION

 Public.

 (Approved 07/90)

 ource: Utah Department of Administrative Services. Retrieved from http://archives.utah.gov/recordsmanagement/grs/stgr
htmi.

ote: Entry from Utah’s records retention schedule.

 Most records retention schedules do not distinguish whether a record is kept in a da

base or on paper. The schedules for Texas, Delaware, Ohio and New York State are so
of the exceptions, in that they mention computer files.
 Find records retention schedules by searching or by going to the Council of State Arc

ists website, which has links for state (http://www.statearchivists.org/arc/stat
res_sch_genlst.htm) and local records (http://www.statearchivists.org/arc/stat

res_sch_genlloc.htm) schedules.
 Audit reports generated by state or federal authorities examine the operations

government. The Government Accountability Office, which is the investigative arm of C
ress, monitors the performance of agencies and issues in-depth reports with results
recommendations for improvement. The reports can easily run dozens of pages, but you
get to the meat quickly by reading, in the full PDF report, the Summary of Findings or Wh
GAO Found section, as well as the Scope and Methodology. Ifa GAO auditor reviewed
databases for the report, he or she will list those in the Scope and Methodology. In the sta
auditors who are elected in statewide elections conduct audits and generate similar rep
we can use for getting clues about data.
  Federal inspectors’ general reports might also be helpful. Inspectors’ general offices
independent units within federal agencies and are supposed to investigate possible fr
waste and other wrongdoing. Look for references to databases in these reports, too.
hrough until you’ve found what you're after. The example below shows that

ears. The entry fails to mention whether any of the information is available as data, bu
east we know there’s a possibility.
gencies are supposed to keep records about the sale of state-owned real estate for

```

```
 example, this audit report from the U.S. Department of Agriculture examines
rm Assistance Program payments by the Farm Service Agency in the federal
ment's 2012 fiscal year. The inspector general says the FSA failed to adequately
ent payments. In the Scope and Methodology section of the report, the inspeceral noted that it used a sample of program payment data for its audit (Depart
of Agriculture, 2013). So we know that there’s a database of payments that we
request.
                                              /

pe and Methodology

obtained the universe of payments from FSA and statistically selected 80 payments
e from October 1, 2011, through September 30, 2012.12 FSA provided four data
cts that included program payments for all of fiscal year 2012, totaling $759 million.
 made the payments through 11 programs.'8

 Fiscal Year 2012 Farm Service Agency Farm Assistance Program Payments. (n.d.). U.S. Dept. of Agriculture. Retrieved
 013, from www.usda.gov/oig/webdocs/03401-0002-11 pdf.

thodology from federal inspector general report. The methodology shows that the inspector general obtained four data
 or its examination.

ernmental and nongovernmental websites have a lot to say about data that are kept
 by agencies. Under the Electronic Freedom of Information Act Amendments
A) of 1996, federal agencies are supposed to provide an index and description of

ajor information system webpages (Department of Justice, 1996).
 Act, signed into law by President Bill Clinton, directed federal agencies to create
nic reading rooms on their websites where the agencies could post documents and
equested repeatedly under FOIA. The electronic reading rooms are supposed to be
t where we can find the lists of major information systems as well.
e agencies have been better than others at disclosing details about their major
ation systems.
act, in 2007 most federal agencies were failing to comply with the law’s requirement
 indexes and descriptions of their major information systems, according to a study
National Security Archive at The George Washington University. As of that year,
y one out of every three agencies had posted detailed information:

trary to Congress’s intent to make agency record-keeping more transparent, the man in which agencies present record indexes and guides varies widely and is more confus than helpful for requesters. Many agencies have not attempted to describe their
ord holdings in a systematic and comprehensive way. The indexes and major informa system descriptions that are available vary widely in format and usability. . . .
ortunately, this congressional mandate has failed, at least with respect to providing
 public insight into agency record-keeping and publicly available information.
tional Security Archive, 2007)

```

```
 Some other agencies, such as the U.S. Postal Service and the U.S. Marshals Servi

continue to have their own listings. For instance, the Marshals Service lists
Warrant Information System as one of its dozen databases that it uses (Marsha

 ervice, n.d.a.).

                           History News Room 2 i Career Opport

    Freedom of Information/ Privacy Act

     Major Information Systems
                                      “FOIA E-Mail
      Listing of major Information systems in alphabetical order S

                                              FOIA/PA Officer
      Special Deputation Files Office of General

                                                       Counsel
      Employee Assistance Program Records Department of Justice

                                                             U.S. Marshals Service
 More recently, some federal agencies, such as the Drug Enforc
began removing the major information system listings on their own sites and referring
isitors to the Federal IT Dashboard at https://itdashboard.gov/ (Drug Enforceme

dministration, n.d.a).

```

```
Financial Management System

Joint Automated Booking Stations

```

```
Washington, DC
20530-1000 (202)

307-9054

```

```
Justice Detainee Information System Upon request, the

                                                   agency's electronic

```

```
Prisoner Processing and Population Management/Prisoner Tracking System

Prisoner Transportation/Automated Prisoner Scheduling System

Property Management and Motor Vehicle Information System

Standardized Tracking and Accounting Reporting System { Privacy Impact Assessment of STARS

Statistical Records and Report System

Warrant Information System

Witness Security Files Information System

```

```
Reading Room may
be accessed through
a computer located

at USMS.
headquarters in
Arlington, Virginia.

Please call (202)
307-9054 to make
arrangements,

```

```
Source: Marshals Service. Retrieved from http://www.usmarshals.gov/readingroom/titles.html.

Note: Marshals Service major information systems.

 A new initiative by the Obama administration could plug some of these holes. Un
the White House’s 2013 Open Data Policy, federal agencies are supposed to create d
inventories and post public versions of them (Sinai and Van Dyck, 2013). Ifimplemen

properly, these inventories could help to identify the offline databases.
 Nongovernmental websites can also tell you about what data these agencies have.
National Institute for Computer-Assisted Reporting Database Library, which is run by

Missouri School of Journalism and Investigative Reporters and Editors, lists more t
40 data sets from the federal government. Only journalists who are members of IRE

purchase the data, but anyone can scout for details about databases at the site. As an ex
ple, the database library (which the author has helped direct) provides data about fed

```

```
ederal Contracts

  urce General Services Administration

  le Size 5.9 GB (FY 2011), 5.8 GB (FY 2010)

  tes Covered FY 2011, FY 2010 {contact NICAR for data from FY 1979-2009)

 st Snapshot i

           Top 25 market or circulation over 100,000: $310
           26-50 market or circulation 50,000-100,000: $270
           50-200 market or circulation below 50,000: $135

           Subscription

           Top 25 market or circulation over 100,000: $650
           26-50 market or circulation $0,000-100,000: $565
           50-200 market or circulation below 50,000: $280

  y this Click here to purchase end download this database
  tabase

 National Institute for Computer-Assisted Reporting. Retrieved from http://www.ire.org/nicar/database-library/
 ederal-contracts/.

 AR Database Library entry for federal contracts data available to journalists.

  there are sites aimed at informing the public about data held by state and local
 . OpenMissouri (launched by the author in 2011) provides details about some 250
 es held by state agencies. This example from the state Department of Agriculture
 s details about an egg license database that is exportable to an Excel spreadsheet
 ssouri.org, n.d.).

                            Q Search Open Miszourl Contact Us

                                                       Ms
 SOURILORG 7 HOME DATASETS AGENCIES BLOG ABOUT

nna cae

 g licenses

 epartmenof Agricul t ure

  gory: Business and commerce. Health, Agriculture and food production

  ata format: Exportable te Microsoft Excel Period start date: 1/1/2011

  st:

  pdate frequency: Daily

  department's Weights and Measures division licenses egg producers. dealers and retaliers.

  information includes licensee name, address, and phone number. Also, state tax identification
  er where applicable

 gg licenses. (n.d.). Open Missouri. Retrieved July 25, 2013, from http://openmissouri.org/data_sets/51-egg-licenses

 Missouri entry for egg license data from the Missouri Department of Agriculture.

 her nongovernmental source that can be tapped to find information about offline
 all 50 states is the State Agency Databases wiki of the American Library Associa
```

```
documents and data have compiled the information since 2007 by scouring state ag

websites for searchable online databases. Often, these sites lack data that we can do
load. But we do know that there are databases behind these search forms that we

request.

            In every US State and the District of Columbia, agencies are creating database
                     __ of this content is available on search engines, but much of it is part of the inasi

                Since July 2007, librarians and other government information specialists have b
   main ees _ don't have tol ALA RUSA named [this site ] [one ] [of ][its ][Best ] [Free ] [Reference ] [Web ]
     # GODORT Wiki Home "Information here changes from time to time. Check out our last seven days’ @

     m GODORT on ALA es ‘ me
    Si if you have questions about this project, please contact: Daniel Cornwall &3, Sy

     # GODORT Events |.» Database definition for project purposes. @
  rrr" SADATFS Presentations and News Items
   godort administration
                     » 2012 Usage StatsQ
     a GODORT Char

     « Committees
    atraentons EERE ESE ee eee

     » Directory i Contents [hide} i

     » Bylaws / | | 4 State Agency Databases Across the Fifty States i
    ® Policies and | 2 Databases by Selected Subjects
     Procedures | 3 Other Project Resources |
     AgP e ndas a and Minutes pan ice fae ARE pet 3 SD eros Sawaal i
 rama State Agency Databases Across the Fifty States _

   official nea Contant "| SADATFS Volunteer Guide for prospective and current volunteers.

Source: American Library Association. Retrieved from http://wikis.ala.org/godort/index.php/State_Agency_Databases.

Note: State Agency Databases wiki. Volunteers from the American Library Association attempt to track state agency dat
on this wiki.

  Let’s visit the page for Colorado and look for the Cold Case Database, listed u
Public Safety (https://www.colorado.gov/apps/coldcase/index.html).
 By clicking on the Search tab and then the Click for more search options box
can see that users can search a number of ways: first, last or alias name, case type,
status, gender, age, year, race, eyes, hair, city, county, status, agency and more.
pretty safe guess that because the information is broken down that way on the se

form that there’s a data table (or tables) with those columns of data. So we c

request that table from the Colorado Bureau of Investigation, which is the agency
keeps the data.

```

```
      », Colorado Bureau
     | of Investigation (CBI)

        COLO CASE FILES
I: ex:

   First, Middle, Last, or Alias Name

  Case Type Case Status
      y Any Case Status 7)

                           Year
                     YearFrom Any Year v| YearTo |

  Agency
  All

  ) Click for more search options

  Age Gender oo bes Eye Color
  ge From i ; _ (All

                     Hair Color
  Height F
  Height ft [al vin Al

  Occupation
  “alt

```

```
    Colorado.gov

 ES supscatseronss

| susmir SEARCH |

```

```
 Colorado Bureau of Investigation. Retrieved from https://www.colorado.gov/apps/coldcase/index.hitm!.

ate of Colorado cold case database search.

THE DATA NERD

ou've identified an offline database, you may need to do some more research before
n request and obtain it. The agency employees who create or maintain the data can
ful because they are the ones who are most familiar with the system used for storing
trieving the data. Sometimes you can find technical contact information on the govt websites. Other times, you might need to call or email the agency to find the right
 person. In some government agencies, public affairs officers may try to prevent you
alking directly to the employees most familiar with the data. That’s unfortunate,
e public affairs officers are not as familiar with the data and can make the process
complex than it has to be. As a negotiating tactic, you can always ask to speak to the

```

```
ata specialist directly, in the interests of making things easier for everyone. That way
burden will be lessened for the public affairs officer.
 When you gather information about the offline database, you may need to addres

ange of technical issues about how the data are stored, processed and formatted. Th
iscussions can get pretty involved, but they usually touch on three common areas:
hysical device on which the data are stored, the database software used to process
manipulate the data and the format in which the file is stored.
 Some governments use mainframe computers for their data processing. Mainfram
re large, powerful machines that can run multiple processes and have been around si
he 1960s. Though mainframes are costly and sometimes seen as outmoded, they
remain popular in some businesses (Lohr, 2012). Other government agencies often emp
computer servers to run their database programs. Computer servers are less expens
than mainframes, but they also are unable to process the same amounts of data. Ma
times a computer server is dedicated to one task. Desktop computers—like Windows
and Macs—are the least powerful of the bunch and usually do not host database program
That said, government agency employees sometimes do create spreadsheets and databa
hat they then access on their own computers.
 Another consideration is the computer software that’s used to store and manipula

 he data. Sometimes that will be a spreadsheet program, such as Excel. However,
more likely that an agency uses a database manager. Database managers are of
relational—they allow users to relate multiple tables to each other. Government ag
ies usually run commercial database software, such as IBM’s DB2, Oracle, Syba
Microsoft SQL Server or Microsoft Access. All of those programs run on servers or ma
frames, with the exception of Access, which is a Windows desktop program. Open-sour
database manager programs, such as MySQL or PostgreSQL, are less common
government agencies.
  Unfortunately, all of these database programs store the data in their own forma
which are incompatible with each other. If agencies are unable to produce Excel files, t

should be able to create ASCII text (delimited or fixed-width), because that is the for
common to all computers.

REQUESTING THE DATA

After you know the name of the database and something about how the agency can prov
t to you, you'll need to request it. You can make an informal request for the data jus
asking for it by phone or in an email. Sometimes that works. Other times, you will nee
make a formal request using the federal or a state open-records law.
  If you want to get copies of offline data from a federal government agency, such as

DEA or EPA, you need to file a Freedom of Information Act request. If you want to get
from the state or any of the governmental entities within it, you would need to requ

```

```
ta using that state’s open-records law. So, if you wanted data from your local police
ent or county sheriff's office, you would need to exercise your rights under your
pen-records law.
 FOIA, enacted in 1966, and state open-records laws start from the premise that all
tion collected by the government for public purposes is open. Even though FOIA
of the state laws differ on many details, they all define some key points: response
ceptable responses, exemptions, data formats and costs. We'll look at how FOIA
 state law—the Missouri Sunshine Law—compare.
 gives the federal agencies 20 working days to respond to requests, compared to
ng days under the Missouri Sunshine Law. Federal agencies are required only to
 with an acknowledgement that they received a request, so requesters can wait a
me to get data. Some journalists have waited years to get files from the Federal
of Investigation, for example. In Missouri, agencies are supposed to provide the
deny the request, by providing legal reasons for doing so within the three working
hey are also allowed to take more time to fill the request, as long as they provide a
te reason.
he laws provide exemptions that allow government agencies to hold data that are
red nonpublic. FOIA has nine standard exemptions—including one for law
ment materials whose disclosure could reasonably be expected to disclose the idena confidential source. Another exemption blocks the release of documents that are
y classified as secret in the interest of national defense or foreign policy. The Misw has a number of exemptions, including some arrest records and calls to 911 disenters. Both laws have big loopholes in that they allow for records to be excluded
 laws.
her key consideration is how the laws treat requests for data. Most of the laws—
ng the Missouri Sunshine Law and FOIA—specifically state that electronic data are
just as paper documents are. In addition, some laws specify what rights you have
 of the data format desired. Under FOIA, federal agencies are supposed to provide
the format that’s requested if the agency is able to do so. Under the Missouri Sun
aw, the format in which the data are stored is considered the public record. Agennot required to produce data in other formats, though the law encourages them to

ic-records laws outline allowable costs. FOIA allows federal agencies to pass along
 and reviewing costs. The Missouri Sunshine Law allows agencies to charge copy staff salary costs. In addition, agencies can pass along programming costs when
oose to create a new record by putting existing records into a different format. FOIA
 Sunshine Law allow agencies to waive costs if the information contained in the
 is in the public interest, something that’s part of most state laws. Some states even
equesters to limit their fees to a certain dollar amount.

```

```
WRITING THE DATA REQUEST

A good open-records request letter is clear, concise and includes enough detail about
you are seeking. The letter should include

  e The name and contact information for the person filling the request;
  e Citation of the law under which the request is being made;

  e The name of the database, as it’s known inside the agency;

  e Thenames of the data columns, if known;
  e The time frame of the data;
  e The format in which you’d like to receive the data (along with the medium);

  e Request for the documentation;
  e Request for written explanation, in case of denial;
  e Fee waiver request or limitation; and
  e Your contact information.

  The Reporters Committee for Freedom of the Press has an online service called i
that allows users to build customized federal or state request letters; https://www.i
org/#l/.

          AvOUT wikt . FOIARESOURCES =‘ 1.0GIN REGISTER

      Welcome to ge. Pret

                               JOIN THE COMMUNITY. AND HARNE

                             Register >

           Create a FOIA or Deliver Request to Manage and Share
           Privacy Act Request the Relevant Agency All Communications

Source: Reporters Committee for Freedom of the Press. Retrieved from https://www.ifoia.org/#1/.

Note: iFOIA from the Reporters Committee for Freedom of the Press.

FOIA IN ACTION
Asa Washington correspondent for The New York Times, Ron Nixon uses data frequent
his reporting on federal agencies. (The following discussion is based on Nixon 20
   SSM? iFOIA.org”” 6°0@

```

```
metimes he can get what he needs from U.S. government websites or by making an

al request with someone who works for an agency. If those two avenues fail, Nixon
e files FOIA requests for the data.
on estimated that he files two or three FOIA requests a month, trying to obtain data
ries that he has on his to-do list. Getting data pursuant to a FOIA request can take a
 so Nixon says he tries to give himself plenty of time.
en he requests data, Nixon says he tries to be as specific as possible; he avoids makquests for everything in the database because FOIA officers in agencies usually kick
hose requests. “They always want you to narrow it down,” Nixon says. “If you know
ou're looking for, it helps.”
on recommends that requesters “do a lot of leg work” before filing requests. For
e, Nixon sometimes bases his requests on the information that’s collected on fedrms. Sometimes he looks at online federal agency FOIA logs to see what data others
lready requested. If someone has already requested and received data, the agency
 be able to easily provide a copy of those data.
en making FOIA requests, Nixon says to remember that fulfilling them is not a
y for federal agencies. Agencies do not have enough FOIA staff to do the job well.

ber that the FOIA staff members are overwhelmed, he says, and try to be as nice as
le to them when making or following up on requests.

TIATING THROUGH OBSTACLES

 life, getting the data you need can be tough: government agencies can put up many

 es, some of them legitimate and others not. Some of the common obstacles are
y issues, cost and ability to produce the data.
en, government agencies will tell you that they’re unable to produce the data because
a are private, which may very well be true. However, under FOIA and the state opens laws, the agencies are supposed to specify the section of the law that makes these

rivate. Just because someone thinks data are (or should be) private, doesn’t mean
 ey truly are under the law. Ask agencies to cite the law in writing so you have a copy
agency’s legal reasoning on the record.
ome of the data truly are private, you can probably get the public portion of the data.
 because under FOIA and the state open-records laws, agencies are supposed to diswhat’s public. For example, federal law prohibits the unauthorized disclosure of
Security numbers. If you want to get a database of city employees that includes Social
ty numbers, city hall is supposed to redact those private data and give you the rest.

 alphabet soup’s list of federal privacy laws—FERPA, HIPAA and DPPA—could bar
ure of some data stored in government databases.
RPA is the Family Educational Rights and Privacy Act, and ensures the privacy
ent educational records. Students have control of these records when they turn 18
ous bed rails in assisted-living and nursing homes, and how companies with federal
 ts also do business in Iran, despite U.S. government sanctions.

```

```
 HIPAA is the Health Insurance Portability and Accountability Act of 1996, wh
rotects individually identifiable health information (Department of Health and Hum

ervices, n.d.). No one would argue that our personal medical data should be relea
ithout our consent.

 DPPA, or the Drivers Privacy Protection Act, passed in 1994 after a number of hi
rofile incidents in which stalkers were able to get home address information from s
motor vehicle departments. DPPA restricts states from releasing the personal data c

ained in a person’s driving record (epic.org, n.d.). The law, however, does allow the d
o be provided for a number of purposes, including insurance, motor vehicle recalls
ourt proceedings.
  Costs can also become an obstacle. Agencies will sometimes say that providing
ata will cost a lot of money. Ask for a price quote in writing, with a breakdown of co
hat includes whatever is allowed under the law: copying, research, programming
o on. Even if the cost of the data is reasonable under the law, it still may be more t
ou can pay. Remember, you can always ask for a fee waiver in your request. Make s
hat you research the conditions for the waiver and state how your request meets th
onditions.
 Another real world obstacle is difficulty in getting the data in a format that you can
n Missouri, state agencies only must produce data in their original format. So, if the s
department of higher education has a particular database that’s stored as an Oracle
it doesn’t have to produce an Excel or ASCII file. In other cases, an agency may claim
t lacks the expertise to produce the data in a format that you can use. Or the agency mi
ave outsourced its information technology operations to a third-party vendor, makin
ifficult to figure out exactly how the vendor could output the data for you. Fortunate
most state laws say that government agencies cannot avoid their obligations under op
records laws by outsourcing their database operations to private vendors.

GETTING HELP

Negotiating for information (whether data or documents) from public agencies truly i
rt, one that requires more knowledge and nuance than this chapter can provi
f you want more in-depth guidance, check out The Art of Access by David Cuillier
Charles N. Davis (2011). It’s a great how-to guide that’s written for journalism students
working journalists, but the lessons can be applied by people in any field.
ent Press Law Center, which provides assistance to scholastic and university journalis
egulations drafted under FERPA allow school officials with a legitimate educatio
nterest to have access to these records (Department of Education, n.d.). FERPA

ublic colleges have denied requests for campus arrest records based on FERPA. The

ays FERPA ranks among the most common complaints that it receives and provides a P
uide to help requesters work through denials (Gregory, 2013).

 Another great resource is the Open Government Guide from the Reporters Committ
become a stumbling block when people seek data from public schools or universiti

```

```
G provides detailed information about FOIA, federal privacy and state open laws. The guide includes specific information about how the laws treat data.
ome states, dedicated agencies can sometimes assist in data requests. In Connectione who's denied a request for data or other records under the state Freedom of
tion Act can appeal that decision to the Freedom of Information Commission. The
mmission holds hearings about the complaints and decides whether the agencies
olated the law. If the agency has violated the law, the commission may order the

to produce the data (Connecticut Office of Governmental Accountability, n.d.).

exas, the attorney general's office gets involved in some data requests. When an
denies information, the agency is supposed to ask for a decision from the AG’s
Both the requester and the agency denying the information are then allowed to

 input to the AG’s office (Attorney General of Texas: Greg Abbott, n.d.).
ddition to these official government agencies, you can get help from nongovernmennizations. A good starting point for identifying such groups in your state is the

l Freedom of Information Coalition, which is based at the University of Missouri.
OIC (www.nfoic.org) represents the interests of state-level open government groups
 its website, provides links to them. So, if someone in Florida is looking for help with
ges getting data from a state or local agency, he or she can go to the NFOIC site, follow
o the Florida First Amendment Foundation and seek help from that organization.

                                HOME Search

      # National Freedom of Information Coalition

                             PROTECTING YOUR RIGHT TO OPEN GOVERNMENT

    ABO pe0IC Z “STATE FOL KNIGHT FOLE IS

     : We award grants that support the grow!

 ational Freedom of Information Coalition. Retrieved from www.nfoic.org.

gencies do not readily inform us about the data they keep. Fortunately, we can use
es—such as records retention schedules and search forms—to uncover databases.
onal Freedom of Information Coalition website. The NFOIC represents the interests of state-level open government groups.

e've seen, it can be tough to identify and obtain data that are held offline, as govern
```

```
 Our next step in working with the data is testing them, so we know their flaws
limits. Only after that can we analyze and visualize them.

ON YOUR OWN

Find your state’s open-records law. Cite it and write a few paragraphs describing
process for requesting data. Include details about any appeals or possible interventio
government officials in other agencies.
  Identify three possible offline databases in your state by using the American Lib
Association’s State Agency Databases wiki. Cite the URLs and write a summary of
columns of data the databases might contain.
  Identify your state or local open-government group using the NFOIC membership
Record the URL for the group’s website and contact information. Note whether the g
provides any assistance to the public.
  Find a federal GAO or state audit report that mentions a database. Cite the report
write a brief summary of the database and how the auditors used it.
  Find an instance in which FERPA privacy concerns by a public agency have resulte
student journalists being denied data or other information. Summarize the details. Do
believe this denial was legitimate? Why or why not?
 Write a mock open-records request letter asking for public employee data from
city for the past three years. Request the data as an Excel file, to be provided via email.
 Find your state in the Reporters Committee for Freedom of the Press Open Gove
ment Guide. How does your state’s law treat data? Does the law say computerized data
public records? What does the law say in terms of your rights to request data ina partic
format? Cite the law and write a summary.

```

```
    Re =

         '

) i

    * a

```

```
> =~

ioe
   ‘ea.

```

```
        ~
           =
= — —

             >

=
 SS =

  = =

        =
             .

       a

```

```
    Pear) ave gl

                                                  “yi inent lated r

  ee

   i

     ~

    =

    : ow
      Ya) i OV aMiives

              we

                                  7 un iueaelinee
                hhezh

     7 é o i j aa. ») ets

  aa Me
   .


  ae [Site us 7 pe vena

   ~~.

         aad ¥
                is K : : 2
 cw

 ae : > —
                      oe

              ~.
     ares iv binge Uv eg
   ' ahi cr             ma

        ereri a arenes

           a

= ate ‘ oe

            rie
  |
   rit pel yw er

```

```
   hen we get a data file—by downloading it or through a public
   records request—it’s tempting to want to start analyzing it right
   away.
ny students and even professionals would like to dive in by starting to run calcula o generate some results. But, at this point, we need to pause and take time to under our data better. What are the data’s strengths? What are their weaknesses? I
ng missing? How important are those missing data? Can we use the data to accuanswer any questions that we might have? Do we need to get other data that might

 answer our questions?
 of these questions deal with academic and professional ethics—particularly our
sibility to represent the world as truthfully as we can. As analysts, we have
o know our data inside and out. We need to have an intimate understanding o
 hortcomings. We owe the consumers of our data analysis—whether that’s other
chers, business clients or the public—the most accurate reading of our data that
 possibly deliver. This is even more crucial in an era when pretty much anyone

sily contribute and consume data on the Internet, and interact with each other.

 networked world, sharing information is almost a trivial act, albeit one that can
 y error tremendously. If we are careful and ethical, we can offer thoughtful
 s.
ndly trusting that government agencies and others will collect and report data accuis a neglect of duty on our part. Veteran data users will tell you that government data
 n the gamut from slightly messy to so flawed that the data are unusable.
y? Aren’t government agencies and other producers of data supposed to get it right?
ality is that government agencies often have poor data quality control, if they have
 all.
e’s an example from California, where the state Department of Education

 student-discipline data for schools for download on its website (California

tment of Education, n.d.b). California, and in fact all states, must disclose data
 discipline under the No Child Left Behind Act of 2001. This law was champi y President George W. Bush as a tool for improving the academic performance
advantaged children.
PTER 5 DATA DIRT 1S EVERYWHERE

```

```
      To create a report: (1) select a Level, (2) select |
      a Subject, and (3) click on the “Submit” Lowel |
      button.
                                pote Select caubsacke peron
      What's NEW? DataQuest Change Log
    What's in DataQuest?
       QuickQuest lets you find answers fast!

                                            QeteQuest Help i For Parents

                                                  Last Modified: Tuesday, March 23, 2010

Source: California Department of Education. Retrieved from http://dq.cde.ca.gov/dataquest/.

Note: California search tool for student public school performance data.

 Under the law, local school districts are supposed to report detailed data about stud

performance, including discipline, to state educational authorities. In California, one

mentary school, with 654 students, reported it had suspended students 306 times
bringing guns to school in the 2010-2011 school year. That reported number was cle
an outlier. In each of the five previous school years for which there are data the school ne
reported more than 131 suspensions for all reasons, and not just firearms incide

(California Department of Education, n.d.a).

  California Department of Education
  Safe & Healthy Kids Program Office
  Prepared $/15/2012 $:53:25 PM

                  2010-11 Lorenzo Manor Elementary School aid Form for UMIRS Data

                                                                                       Agency: San Lorenzo Unitied
      Purpose’ information To reporting Collact student system expuision, (UBIRS) suspension, and truancy information to satisty NCLB requirements related to “persistently dangestous” schools and the uniform management |CD Code: 0161309

                            COE Contact: Stephanie Papas - 916-445-2441 SPapas@cde ca uy

                                         Vioience/Drug Rate (Violence/Drug Total / Enroliment).
                                               Tokal of Persistently Dangerous Expulsions Only.

                                                        Number of Non-Studers Firearm incidents.
     persistently Was schoo! dangerous” at tisk of being for 2006-20097 designated NO! persistently Yias whoo! dangarnus” at risk of being for 2009-20307 designated NOL “persistently Véas echoval dangerous” at risk of being for 2010-2011? designated NO}

Source: Lorenzo Manor Elementary School - Suspension & Expulsion Information. (n.d.). DataQuest CA Dept. of Educ
Retrieved June 13, 2013, from http://dq.cde.ca.gov/dataquest/Expulsion/ExpReports/SchoolExpRe.aspx?cYear=2010-11
     DataQuest helps you find facts about California. ~~ 1. Select Level: —~ seen
      schools and districts.

                                    pe 3. Click Submit:
      Our Parents Page is another way to find data, sss
       Contact information for program related

```

```
rters at the NBC television station in San Francisco uncovered the erroneous data
nzo Elementary and pressed the state and local administrators for an explanation
ow such an error could slip by. The district superintendent said that he didn’t have
review the accuracy of the data. State administrators said they had no independent
in place and instead relied on the districts to report data accurately. So neither was

responsibility to ensure accurate data (Susko, Putnam, & Carroll, 2012). Since
e mistake has been corrected on the Education Department's website.
 alists at the Reuters news service in New York City discovered big flaws with a
 database of hazardous chemical storage that emergency responders use after fires
ustrial accidents, such as the April 2013 fertilizer plant explosion in West, Texas.
eral Emergency Planning and Community Right-to-Know Act requires the estabt of state and local networks to plan for emergencies involving hazardous chemiaddition, the Act requires facilities to report the presence of hazardous chemicals
ng certain amounts (Environmental Protection Agency, n.d.a). However, the
 news service found that facilities had misreported or failed to report chemicals.

 matters worse, neither federal nor local authorities were checking to make sure

rts were accurate (Pell, McNeill, & Gebrekidan, 2013).
eport ordered by the New York City police commissioner found that the
epartment’s reporting system had poor controls for guarding against intentional
lation of crime statistics. The report cited several instances of the police
ading felonies to less serious misdemeanors (Goldstein, 2013).
e might seem like extreme examples, but data flaws are not rare. Government agenen compelled by law, collect loads of data. But they don’t always set up processes to
stakes or run data-integrity checks themselves. That’s why we need to be data inves and look for things like outliers, or extreme values that could very well be errors.

ATA ARE DIRTY

e to keep in mind is that all data are dirty. But why? How did they get that way?
y data thrive in a number of different environments. As we saw in the examples above,
ent agencies generated dirty data because of poor or missing controls during the review

 However, if we take a step back we can see that dirty data abound where there are poor
 during the data entry process. It’s the old GIGO—garbage in, garbage out—effect.
k about how data get into a database. As you learned in Chapter 2, in government
 lerical workers often type data from paper forms into a data file. Data-entry clerks
 are low paid and perform this work for hours-long stretches. It’s grinding work.
you've entered data as a student worker or for a research project of your own.

asy to get distracted and make mistakes. It’s also easy, under normal circumstances,
 data inconsistently. So ifa clerk at your city health department is entering data about

d other animal-bite complaints, he or she could enter a street as “MacArthur Road”,

hur Road”, “MacArthur Rd.”, “McArthur Rd.”, “MacArthur Rd”, “McArthur Rd”
n. When you work closely with [data, ][you'll ][see ] [inconsistencies ] [like ][these ] [all ][the ][time. ]

```

```
 Sometimes you'll get data that are dirty or difficult to work with because of how
are stored in columns.
  Here’s an example: We like to see data about dates like this: month/day/year, so
write New Year’s Day as 1/1/2015. But the people who create database systems often
store that data as text. So we see 01012015 for New Year’s Day. In this case the fir
stands for the month: January. The second 01 stands for the day of the month. And th

four characters, 2015, are used to record the year.
 When someone creates a data file and then chooses to store columns with date da

text, it limits our ability to analyze the file. If the date data are stored as text, we're un
to run date formulas. So we won't be able to do things like calculate the time that
elapsed between dates, or figure out the day of the week based on a date.
 Another database design problem that we often grapple with is run-on data. This
pens when the person who created the file stuffs more data than we’d like into one col

  Until recently, the Missouri Ethics Commission, the agency that collects and diss
nates data about contributions to political campaigns in the state, reported data a

contributors in one column. Look at Column G, which is titled ContrInfo, for contrib
data.

 WAS: contribsttos (Compatibility Model - Excel 2 Be t ieh

 Fed HOME INSERT PAGE LAYOUT FORMULAS DATA REVIEW VE Hereg, David ~

       e py # Catibri “ji t le ema x? be" & r ip “i ae eer Conditionat Condi Formatting A « al Bes, Insert . my oy &
      by + . mah as Table Be petete + Bi- cones Paes
       EZ gyi x ~ | See ds x $+ . % > | RZ 8 Cell Styles ~ ieiformaty a Ly Fiters ete Be Select Find &
  Gipboard % Fort f Alignment % Number % Styles Celis Editing

   G15 Citizens for Quinn 14611 Manchester foad Ballwin 140 63014

   1 Reports! WEL Yi Yi 7 jj Yi, \ Z te EC
  2 14-Jan-08 Missouri Merchants & Manufacturers Assoc 16100 Chesterfield Pkwy W. Ste 210 Chesterfield MO 63017 15-Noy-07 $259.00
  3 14-Jan-08 106th Legislative District Republican Committee 222 W. Columbia Farmington MO 63640 -28-Dec-07 $2,500.00:

   4 14-Jan-08 34th Republican Senatorial District Coram 2125 Shannon Lane Saint joseph MO 64506 34-Dec-07 $6,000.60

   5 14-Jan-08 3rd Senatorial District Republican Committee 222 W. Columbia Street Farmington MO 63623 28-Dec-G7 $500.00
   § 44-Jan-08 Advocacy for Special Needs 101 €. High Street Jefferson City MO 65101 31-Dec-07 $1,250.00
   7 14-Jan-08 Alliance for Higher Education 101 €. High Street Jefferson City MO 65101 31-Dec-07 $1,250.00
   8 14-Jan-08 American Family Political Action Committ 4802 mitchell Saint inseph MO 64507 12-Nov-07 $275.00

   9 14-Jan-08 Aquila inc Employee Federal PAC 20 W. 9th Street 2nd Floor Kansas City MO 64105 | 28-Dec-67 $650.00
  10 14-Jan-08 Bank of America Missouri PAC 800 Market St 15th Floor Saint Louis MO 63101 3-Dec-07, $775.00

   V4, 14-lan-08 Bank of America Missouri PAC 800 Market St 15th Floor Saint Louis MO 62101 23-Dec-07 z
  12, 14-Jan-08 Butiders Association PAC K.C. Chapter Assaciated GeneralContractors of Ameria &The Builders Assoc 632 West 27-Dec-OF
  43) 14-Jan-08 Citizens for Brad Lager PO Box 316 Savannah MO 64485 34-Dec-67
  14 14-Jan-08 Citizens for Charlie Shields 47 Erin Court Saint Joseph MO 64507 i 02-Dec-07

  | 1: 14-Jan-08 Citizens for New Health Care Concepts 101 €. High Street Jefferson City MO 65101 31-Dec-07
    | 16| 14-Jan-08} Citizens for Quinn 14611 Manchester Road Ballwin MO 63011 18-Dec-07
  17. 14-Jan-08 Clemens for Missouri PO Box 913 Jefferson City MO 65102 i 18-Dec-07
values. So if you
the same road. Likewise, if you create a chart you'll get six visual elements instead of one
 Applications developers who create Web or computer desktop forms for data entry
build in error-checking tools. Or the forms can limit data input to a set of options.

you can see, constraining choices produces higher-quality data.
instance, a form might ask you to pick a city name from a drop-down list. You would
to pick New York instead of typing “NYC”, “New York City”, “NY”, “N.Y.” or “N.Y.C.

```

```
14-Jan-08 Coalition for Disability Rights 101 £. High Street Jefferson City MO 65101
   ©:

```

```
31-Dec-07

```

```
 this is fine if we'd like to just read it. However, the structure makes it impossible
 summarize contributions by city, zip code, street address or occupation. Compliatters more, rows in the column could have data about people, companies or
 committees giving money.
hese data stand, we're unable to easily answer questions like, Who is giving the
oney? How much money is coming from sources out of state? Are people from
ar workplaces making a large number of contributions? From which zip code has
 money come?
would need to do quite a bit of data scrubbing before you could answer all of those
s definitively. Fortunately, the Missouri Ethics Commission now provides a new

of the data file, one that organizes the individual pieces into columns of their own.

 &~ « mok2smalixis [Compatibility Maze) - Excel ? © ~ HR

 HOME INSERT PAGE LAYOUT FORMULAS DATA REVIEW VIEW Herzog, David ~ SS

                                  General a EEE Conditional Formatting Beinsert ws

                         Alignment & Humber ty tytes Celts Editing

      Blair 118 N Water Liberty Attorney 1/12/2012

     Darr 107 Wright Smithville Shook, Hardy 1/12/2012 :
 ana Curry 407 Shannon Smithville q Paridise Locker 4/12/2012
     Hitchborn 6485 Smithville : Retired 4/12/2012
     Greene POBox 914 Senithville Hl J Realtor (42/2012
     Becker 3611 NE 132nd Smithville ; Heatingand 1/42/2012
            118 N Water St Uberty B i 1/12/2012
            18408 Elm St Smithville : 4/12/2032
            225 KK Hwy Smithville 3/10/2012,
 y Perkins 404 4th St Smithville, < Retired 1/10/2012
    Hall 1400 NW 43Rd Kansas City % Attorney 1/11/2012
     Svetlic 7111 Kansas City i“ “Attorney 1/7/2012
    White 18185 Elm Platte City Retired 1/6/2012
     Foster 203 Highland Smithville Retired 1/6/2012
     Perkins ? O Box 591 Smithville St Luke's 2/2032
     Kissinger 5024 Smithville ‘Housewife 1/3/2012
     Burch 14700 North Parkville £ Platte Valley 4/12/2012 ie
  @:@

 ssouri Ethics Commission. Retrieved from http://www.mec.mo.gov/EthicsWeb/CampaignFinance/CF_ContrCSV.aspx

 oved data from Missouri Ethics Commission.

ge improvement, right? Committees, companies and individual contributors get

n columns. This would make it easier for us to create sums for each, using pivot
n addition, the first and last names get their own columns. Same goes for the street

 (two, in fact), city, state and zip code.
 we could answer the questions that we had posed earlier.

ING DIRT IN AGRICULTURAL DATA

d and Agricultural Policy Research Institute at the University of Missouri routinely
 data from U.S. and foreign government agencies that it uses to make projections
gricultural activity around the world. [Established ] [in ][1984 ] [with ] [a ][grant ][from ] [Con- ]
                     $-% % 2 159 Format Eiformaty at FF 2 Sot & find &
                                     Cw F 1 OR B33 BW ro cet styles as Table ~ Er delete > fittery Sefect~

```

```
ings that might have to be corrected or noted, FAPRI director Patrick Westhoff says.
following discussion is based on Westhoff 2013.) The analysts look over the data in
and create charts that help them spot data that are inconsistent or improbable, he sa
 Analysts examine supply and use data to see if they are in balance, Westhoff
That entails making sure the sum of production and imports equals the sum of domestic
exports and ending stocks. Sometimes FAPRI’s agricultural price data are missing inf
tion and analysts have to decide whether and how to fill in those missing values, he sa

  FAPRI also knows that some data, such as the U.S. Department of Agriculture’s
mates of Chinese grain supply and use, can be revised by the provider. Westhoff says
based on new data, the USDA has several times changed those estimates.
 Though FAPRI gets most of its data online, there are times that it manually enters
from published reports or from information obtained on a phone call, something tha

lead to human error, Westhoff says.

CHANGED RULES = CHANGED DATA

Changing rules for collecting data can also hurt your data quality, or at least limit
analysis later. Federal government agencies often tweak or even radically change their
collection methods and rules. Following are a few examples from the world of econ
data:

Mass layoffs. The Bureau of Labor Statistics began compiling mass layoff statistics sta

in 1995. In 2004, it narrowed the scope to cover only private sector, nonfarm workpla
and no longer counted layoffs in the public and agricultural sectors. So you're unab

accurately compare data from 2004 on with earlier years (Bureau of Labor Statistics,

Bankruptcy filings. In 2005 Congress passed and President George W. Bush signed
that makes it more difficult for some people to file for bankruptcy protection in the fe

courts (Public Law 109-8, 2005). As a result, any comparisons of bankruptcy stat
from 2006 on to earlier years would prove inaccurate (United States Courts, n.d.a).

Medical insurance costs. The U.S. Department of Housing and Human Services use
Medical Expenditure Panel Survey to estimate the cost of single-person and family
miums for employer-based health insurance policies. It’s considered the best measu
consumer health-insurance costs. In 2007, however, the survey was put on hold s
DHHS could improve its survey methods. Thus, data for 2007 are missing (Agenc

Healthcare Research and Quality, n.d.).

Motor vehicle registrations. The Federal Highway Administration releases data
vehicle registrations by state every year. It collects the data from the state offices

```

```
 the registrations. When the FHWA, which is part of the U.S. Department of

rtation, fails to get numbers from the state authorities, it substitutes numbers

rlier years (Federal Highway Administration, n.d.).

omestic product. The U.S. Bureau of Economic Analysis uses the GDP to measure
 of the U.S. economy, as defined by goods and services. In the summer of 2013 i
 “history on a grand scale” by including research and development spending as

ents (Coy, 2013). The BEA’s move caused the size of the GDP to grow. The BEA

lated its GDP figures going back to 1929, when the measure was introduced.
you can see, dirty data are the rule, not the exception. Get used to seeing inconsistenpos and misspellings, along with improperly structured data.
 data are flawed—the question that we need to answer is, How badly are they
 In the next chapter, you will learn how you can examine your data so thoroughly
u can make informed and ethical decisions about how to use them. We call this
 making data integrity checks.

UR OWN

ampaign contribution data for candidates running for state (not U.S.) offices in your
hat problems do you see in your data? Jot down three instances. How do you think
laws were introduced?

```

```
nuh fier Soothes i: elelvci Faz al aa ricer oy er mie

```

```
      fhe
                             rl
_ ar a ‘om ad eae
         nGNs yeaa; rere

```

```
; - 4 | ss : :

```

```
jes 14 Lew yh. ee a naretcron dt Woogie A

```

```
Ht PLOirte rymile site! enh dheaeay Wi ahaha spenteeiieradbt

```

```
    Video
                            orto Lo
ye puesta eels aces Sanita iapakgoull “ate tical we

```

```
 wre
             sy Wo Os ool nummer neds fe wand vcrwae: Nim alee ad iil
    hart acekene theme oy leanne
th ari
                ia aes aga aN
          us owl) ome xe igo That salad been take ike
eatenCstk ys

```

```
             “herd
                   laepllagmon
- Laos nada

```

```
  207 graced Wild ed eenaph: "ego do dewalt a Pe a

```

```
                    sneha ee anes

                     CiAkriy pens ‘My
ore LASS & (OO erage aS ein

  ai - ; Veli rile Ce

             ae
       E t

                             ,

        223 weer tte Liane chal mgr eT Faaeaae
Andie fs oval Saguenay lf iret - nbol tang fniiabdilaied eT ( TN
                       a

                            x a si

 witty pr

                                                                            TY Oe eu

             Haves — Lema > \ itera h ali
            i

         i, a hae He tie
               oe é3 eae cary [Saco * of al Lune i S
 = tay “ a ss a ; : a
                   etc; omg Vi gat +
          a!
                                             ;
        
                                                                                      : T'S :
        re
                                Di tr comes Weeelpiy rea he

               Ae Wo} ; bx sal) rg
       ey Nig <2
                 ——
  — a, 7
         e

```

```
 s we saw in the last chapter, we can expect to find errors in our data. Our next step
 is to figure out how extensive those errors are.
  To do that, we will run data integrity checks. Data integrity checks sound
aunting, but they really are just a way of systematically examining our data for
s. This chapter will demystify that process and show you how you can use Excel to
checks.
re going to learn how to do this using an Excel file that details spending by candir the 2012 U.S. Senate race in Texas that was originally downloaded as a comma
ed values (CSV) file from the Federal Election Commission’s data portal at http://
c.gov/data/CandidateDisbursement.do?format=html&election_yr=2012. You

nload this file (TX_all_senate.xls) from the website for this book.
open seat attracted more than 25 candidates to run in the primary election and was
d-most expensive Congressional race of the 2011-2012 campaign cycle, according

alysis of FEC data released through April 16, 2013 (OpenSecrets.org, 2014).
n you run data integrity checks you'll need to have your data documentation at your
e, it’s called the metadata and comes as a webpage at http://www.fec.gov/finance/
ure/metadata/CandidateDisbursements.shtml. As you learned in Chapter 3, the docuon can go by many other names: record layout, data dictionary, code book and so on.
ice safe computing by making a copy of the metadata for yourself, so you always
opy somewhere.
eading the metadata, we learn that campaigns must report spending when they
$200 in payments to a vendor during an election cycle. These data are a good guide
ical researchers, campaign operatives and others who want to keep track of candictivities. The metadata tell us how frequently candidates file reports and provide
e about filing amended information for those who submit paper reports, as Senate
tes do.

FEC also warns us about transactions marked as memo entries, which indicate that
ment was for a credit card bill. The individual payments to vendors using that
ard are listed separately. We want to exclude the memo entries from sums if we
the data later so we don’t inflate our results.
TER 6 DATA INTEGRITY CHECKS

```

```
information about the 26 columns that the FEC provides in the data file.

  Information contained in the file

  The Candidate disbursement file contains the following information:

```

```
com_id Committee ID

com_nam Committee Name

can_id Candidate 1D

ele_yea Election year

can_off | Candidate Office
can_off_sta State Candidate Office
eee Ys .
can_off_dis oe _ Gistrict ons sis Yi

             Line number from
fin_num Detailed Summary
            Page of FEC Form 3
   . “Link to image
iene “presentation

rec_com_id Committee Regie 1D

```

```
                                   “, Unique nine digit identifier used by the Commission t
Character a Bisons mien Urea 9 characters identify begin with each the potitical letter © committee, which is followed In general by eight committe
   ‘a "Name of committee or other Nax 90 Ll J : oO
Gece end reqitered witlithe FEC characters TV fhe arte of (ie comimitier

                                       First character ind office sought - H=House,
Character 9 characters S#Senate, P=Presidential. Columns 3-4 are the state
                                  abbreviation for Congressional candidates

Character Name of the candidate — ee _Ustof ail disclosure filings for this committee

Number characters General election year of the cycie in which hi this capaii
                                  running
      © Office abbreviation © character © BePresident; S=Senate; H=House

Character Postal abbreviation for State 2 characters

Number Pe candidates District number for House’ AX - CWO

         eategary of disbursement marae
Character page based of on FEC detailed Form summary 3 ae aracters = Descrintion of Form 3 {See page 6 of these istruction
    ‘ ___ Page where transaction may be |, 3 SS
ee Viewed asimage n Ke

```

```
Character Character digits < followed by eight

```

```
         If the disbursement goes to another committee cee
$ characters with the FEC, this would be the ID number of the
        committee receiving the payment

```

```
Source: Federal Election Commission, Retrieved from http://www.fec.gov/finance/disclosure/metadata/CandidateDisburs
shtml.

Note: Documentation for Federal Election Commission expenditure data.

 Tag tells us what the column is named in the data file.
  Field Name is a longer, more-descriptive name for the column.
 Data Type shows the data format. You'll see that ele_yea, the election year, is stor

a number.

  Description provides details about the contents of the column.
 Range tells the number of spaces for the data in each column.

  Explanation has even more details about the contents of the column.

          BIG-PICTURE CHECKS

          Immediately after we get a file, we want to answer a few bi
            ture questions before moving on to running the more-deta

            data-integrity checks. We need to ask,

```

```
   seers WME
  TX_all_senate

Source: Microsoft Excel for
Windows 2013.

Note: \con for Excel file with
federal campaign spending
data.

```

```
  What is the file format?
  How many rows do we have?
  Are all of the columns present with proper headers?
  So go ahead and find the file on your computer. Look
icon for it and make sure it’s a Microsoft Excel spreadsheet
Ona Windows computer, you can also look for the file exten
The extension .xls means it’s an Excel 1997-2003 workbook

```

```
 the file TX_all_senate.xls with Excel and you'll see this:

as

```

```
INSERT PAGE LAYOUT FORMULAS

   “ja a ae boa

              €

           % Alignment

       fe | canid

```

```
DATA

 S

 
```

```
REVIEW vEW

```

```
         OP Format as Tsble~
$-%* BS

```

```
Genera!

```

```
‘onditional Formatting =

```

```
@e

```

```
Herzog, David - FO

Sort & Find &
Filter © Select +
 £aiting

```

```
& Number

```

```
    on SMa aM.
       TED CRUZ FOR SENATE $2Tx00312 ;

       TED CRUZ FOR SENATE S2¥X00312

       TED CRUZ FOR SENATE S$27x00312

       TED CRUZ FOR SENATE $2TX00312

       TED CRUZ FOR SENATE S2TX00312

       TED CRUZ FOR SENATE S27X00312
 0492785 TED CRUZ FOR SENATE $27x00312
 0492785 TED CRUZ FOR SENATE $2TX00312
 692785 TED CRUZ FOR SENATE $2TX003i2
 0892785 TED CRUZ FOR SENATE S$27X00312
 492785 TED CRUZ FOR SENATE S$27K00312
 0492785 TED CRUZ FOR SENATE S27X00312
 0492785 TED CRUZ FOR SENATE S2TX00212
 0492785 TED CRUZ FOR SENATE S2TX00212
 a92785 TED CRUZ FOR SENATE S$27K00312
 0492785 TED CRUZ FOR SENATE S2¥K00312
 892785 TED CRUZ FOR SENATE $2TX00312

```

```
CRUZ, RAFAEL
CRUZ, RAFAEL
CRUZ, RAFAEL

CRUZ, RAFAEL
CRUZ, RAFAEL
CRUZ, RAFAEL
CRUZ, RAFAEL
CRUZ, RAFAEL
CRUZ, RAFAEL
CRUZ, RAFAEL
CRUZ, RAFAEL
CRUZ, RAFAEL
CRUZ, RAFAEL
CRUZ, RAFAEL

CRUZ, RAFAEL
CRUZ, RAFAEL
CRUZ, RAFAEL

```

```
can_off —_ can_off.

```

```
an Off dis

```

```
Hina ini
    17 bttp://image’
    47 bttp://images
    17 http://image!
    17 http://imaget
    17 http://immaget
    17 bttp://image:
    17 http;//image:
    17 hittp://image:
    47 http:/fimage:

```

```
  g
ele yea
   2012 S
   2012 S
   2012 $
   2012 s
   2012 $
   2012S
   2012 $
   2012 S
   2012S
   2012 s
   2012 $
   2012 $
   2012 s
   2032 $
   2012 S
   2012 S
   2012 S

```

```
con e se8 oe o ae oeogap

```

```
 > TX_alt_senate

```

```
 Pivot Table_TX_all senate_28

```

```
Pivot Table _Tx_all_se XE RR XAR A X SA

```

```
deral Election Commission.

al campaign spending data for Texas open in Excel.

 answer our second question: How many rows does the file have? We answer that
ng Excel to go to the end of the sheet by clicking Ctri-End on our keyboard

nd-End if you are using a Mac). Now we're at cell Z8023, or the very far right end

eet. So you have 8,023 rows, or 8,022 rows with data plus one header.

           2 Ti ail_senotexls {Compatibility Mode - Excel

```

```
 HOME

```

```
ENSERT PAGE LAYOUT FORIPALAAS

```

```
 ETA REVIEW SEW

```

```
Bp * +

```

```
 z “KK

    dy?

```

```
“Son, Find

```

```
Bp * 2 + Cale z
e FPu-|B

```

```
BP nse»

```

```
EX Delete +
ror &

```

```
Fitter » Select»
Editing

```

```
 d ts

```

```
      Font

     t
> dis_pur_des
  TELEFORUM
  SALARY
  RENT
  MAL
  MOBILE PHONE BANK
  POSTAGE
  REFUND PORTION OF 1/21/11 CONTRIBUTK
  REFUND PORTION OF 3/9/11 CONTRIBUTIO
  REFUND PORTION OF 3/30/11 CONTRIBUTION
  REFUND OF 3/31/11 CONTRIBUTION
  REFUND OF 1/21/11 CONTRIBUTION
  REFUND OF 1/21/11 CONTRIBUTION
  REFUND 1/20/11 & 3/22/11 CONTRIBUTIONS
  REFUND OF 1/21/11 CONTRIBUTION
  REFUND OF 9/6/11 CONTRIBUTION

```

```
Sets

```

```
$482.37 REFUND OF IN-KIND CONTRIBUTION

```

```
TX_all_ senate

```

```
Preot Table TX all senate 26

```

```
    General #5 Conditional Formatting +
                   Fortnat as Table
a SH BSE TE colstylec

  & Number % Styles

               ye 2
       raid bac ref id

           $817.16568

           $B17,16569

           $817,16570

           $817,16571

           $B17,36572

           $B17,16574
   10 Refunds of CoSB20A.12634
   10 Refunds of CoSB20A.12659
           SB20A,14865,

   10 Refunds of CoS#20A.15110

   10 Refunds of Co SB20A,15231

   10 Refunds of Co SB20A.15232

           SB20A,15363
   10 Refunds of Ca $820A.15508
   10 Refunds of Co SB20A.15509
  10 Refunds of cosaz0a.16016[

Pivot Table_TX allse .. @

```

```
deral Election Commission.

 f data in federal campaign spending Excel file.

```

```
  Scroll left to get to the A column. Now hit Ctrl-Home (or Command-Home) and y
returned to the top of your spreadsheet.
 Now for the third check: Look at the column headers in Row 1 and make sure th
the same as in the metadata. It’s tempting to change the headers to something that’s
meaningful to us. However, it’s best to practice safe computing by keeping the or
names. That way, anyone who works with the data can easily refer to the metadata.
 They do match and we're ready to move on to the next step: Data integrity check
each column.

DETAILED CHECKS

For these checks we will generate pivot tables that list each data value and the numb
times that value appears. You'll see quickly that these checks let us take a good look at
we have to work with. :

  Let’s start with the com_id column, which has nine characters and is used by the F
uniquely identify candidates. Each should start with one character, followed by eight d
  Here’s how to start the pivot table:

  1. Make sure your cursor is clicked inside one of the cells with data.

   Select the Insert tab and then the Pivot Table button.
  3. Excel asks you to Choose the data you would like to analyze. Excel should automati
   pick Select a table or range and highlight the data. Put the results into a new works
  4. Click OK

 | HOME — INSERT  PAGELAYOUT © FORMULAS DATA =—REVIEW «VIEW Herzog, David

     } . 7a sonra ' a rs ~~, me me 3
 | | Pascale _& Rece ue i Fable Wustations 5 Apps tar | Recomn ee me te EF bivotChart by Hyperlink Sey Text A Symbols

  | Tables Pinters Links °

  AL i fx
  | ) Choose the data that you want to ansiyze
 | oe ee ee rie of LL ee @ Select a table or range :
 peel i com_id nO com_nai DEM x 2 Tablemange: Toil Wii senatesASisiseiry eaneien poet En
 | 2 100493246 GLENN ADDISON SENATE & vie an extent data source 0
  3 1000493346 GLENN ADDISON SENATE CA aes - 0 17 hitp://im
  4} y a iS :

 js a ce ae te 17 hittp://im
 | 6 [000893245 GLENN ADDISON SENATE CA” OSE ISIE YOR Wea OE Eee are tapes vo Be placed 0 417 http:/fim
  7 100493346 GLENN ADDISON SENATE ss we ee 0 17 http:/fim
  | & {€00453246 GLENN ADDISON SENATE oS pie ai 9 17 http:f/im
   | | 9 {000493246 GLENN ADDISON SENATE CA o fons | beat. Sey 0 17 http://im
 | 10 [000493346 GLENN ADDISON SENATE CA “hoose whether you want ta analyze mostiple tables 0 17 http:/fim
    i | 11 t [c00493246 GLENN ADDISON SENATE CA Add 4 this data to the Dats Model 0 17 http://im
 | 12 1000493246 GLENN ADDISON SENATE CA 0 17 http:/fim
  | 13 1000493346 GLENN ADDISON SENATECA sieiaicics ibe oan panna = Q be bttp://im
 [24 {C00493246 GLENN ADDISON SENATE CAN $2TX00320 ADDISON, MA 2012 $ ™ 0 17 http:/Jim
 145 co0893246 GLENN ADDISON SENATE CAN 52TX00320 ADDISON, MA 2012 § ™ ° 47 http://im
  | 16 1000493346 GLENN ADDISON SENATE CAN S2TX00320 ADDISON, MA 2012 1% 0
 | 17 1600493346 GLENN ADDISON SENATE CAN S2TX00320 ADDISON, MA 2012'S ™ 0)
 | 48 [00493348 GLENN ADDISON SENATE CAN S2TX00320__ ADDISON, MA 2012 $ ™ 0

    | > TH all senate Voeck Table Th al senate 26 | Vieot table 1% allse # :

Source: Federal Election Commission.

Note: Create pivot table dialog box in Excel.

```

```
 Excel opens the pivot table designer.

                                     Smananaasusmmennemmammmnnt
 © e-: TK all_sensteals [Compatibility Mode] - Exced PIVOTIABLE TOGLS 7 Mw - mex
 HOME INSERT = PAGELAYOUT FORMULAS. «(DATA —sREVIEW ANALYZE DESIGN Henxog David « FM

 Active Field: SF a « ai § Be BS \, G8 A Fietds, tems, & Sets ~ VS 5

```

```
63 Fiekd Satin

```

```
i] ‘I Group c Chang: Pied hart Recommended Show
             . : Hor i PivotT ables

```

```
        Active Pinta Catvulations Tools

                                   | PivotTable Fields

                                                                                                                             | Choose fields to add to report

                                                             fof Lip eomid

                                                                    Drag fields between areas below:

                                                      Y FILTERS 7 COLUBINS

spja!4 oiJOL oy /@ vauues

    Sheetl : Xai senate Pivat Table TX all ser...

Microsoft Excel for Windows 2013.

el pivot table designer. Use this blank form to create a pivot tabie.

 PivotTable Fields selector on the right lists the headers for all of the columns in our

o you can see there an entry for com_id, the committee ID. The layout area on the
es us boxes for creating our pivot tables.
ting started is as simple as dragging a field name and dropping it on the layout.

t to make a pivot table for the com_id, so drag that field over to the ROWS box.
t to see the IDs listed in our column to the left.
, we want to create a column to the right that shows how many times each com_id

 in the data. So let’s drag the com_id from the list into the VALUES box. Excel, by
 says that it wants to count what we put in VALUES box. It’s smart enough to know

 can’t sum or average the com_id because the contents of the field are text, not
s. Excel then generates this pivot table report:

```

```
i\BwWs&- ¢& TX. all senatexls [Compatibility Mode] ~ Excel
     HOME INSERT = PAGELAYOUT «= FORMULAS) «= DATA REVIEW VIEW

```

```
 PIVOTIABLE TOOLS

ANALYZE DESIGN

Ss ER Fields, tern, & Sets ~

       Caloulations

```

```
 Lm a
 a) f
PivatChart Recornmended Show
      PivotTables
     Touts

```

```
  ee Active Fietd:
[PivatTable Count == of com_id
1 > AG Field Settings

```

```
Vv fae
   i Dyill Group

```

```
Active Fizid

```

```
fe — Countofeom_id

```

```
ik
i2

fez
\8
i3

```

```
“Y") PivatTable Fields

   _ Choose fields to add to report:

    (A com_id
        i) comoam
    {2 cen id
    i) ean pam,
    CD elec res:
    [7 can_off
        OS ane Att he

     Drag fields between areas belewt

```

```
                                                             ‘Y ALTERS {1 COLUMNS
 | 14 C00493536
 | 45 000496166 =

                                                                                    ¥ 3 § Count of com...

Source: Federal Election Commission.

Note: Pivot table counting com_id entries. Each com_id entry is listed, along with the number of times it appears in the

 We see 17 unique committee IDs, along with the number of items associated with
committee in the data file. They are listed in ascending order. We also see a total of 8,

which we recall is the total number of lines of data that we have. Finally, we see that
the com_id numbers start with one character and end with eight digits, just as the m
data said.
 So this column checks out fine.
 Make a note in your data notebook that 25 candidates ran for the Senate seat, so we
eight committees short. We could speculate that the other eight failed to spend eno

money to meet the reporting threshold, but we would need to verify that.

 Change the name of the Excel worksheet tab from “Sheet” to “com_id IC”, for com
integrity check. That way you'll know what’s on this tab. (Do this for all of your pivot

sheets.)
  Practice safe computing: We've made changes to our sheet, so let’s preserve the ori
and create a new, working version. Save a working version of the file by picking File |
As .. . Excel should remember that the file type is Excel 1997-2003 and the origina

name. You can add the number “1” to the file name, making this version TX_all_sena
After working with data for a while you will no doubt adopt a filernaming convention
fits your workflow.

 Now, let’s run a data integrity check on the com_nam. We had 17 entries in the co

field, so we would expect to see the same number when we count the names.
               TX_all_ senate Pivot Table TX allser ... G Defer Layout Update

```

```
      rat

     3 Count of com_nam
      le tcc
     S CASFORSENATE
     6 COMMITTEE TO ELECT LELA PITTENGER FOR UNITED STATES SENATE
     7 CRAIG JAMES FOR UNITED STATES SENATE
      8 (DEWHURST FOR TEXAS
     9 ELIZABETH AMES JONES FOR TEXAS INC
     40 FLORENCE SHAPIRO FOR TEXAS INC
     41 GARZA FOR TEXAS EXPLORATORY COMMITTEE
     12 GLENN ADDISON SENATE CAMPAIGN
     13 HUBBARD FOR SENATE CAMPAIGN
     14 JASON GIBSON FOR US SENATE
     15 MICHAEL WILLIAMS FOR CONGRESS
      46 PAULSADLER FOR SENATE
      47 PEOPLE FOR CURT CLEAVER; THE
     18 ROGER WILLIAMS FOR US SENATE COMMITTEE
     19 SANCHEZ FOR SENATE
     20 TED CRUZ FOR SENATE
  | 21 TEXANS FOR TOM LEPPERT
      22 Grand Tota!

deral Election Commission.

 table showing com_nam and how many times each appears.

 well because we have 17 unique committee names and the grand total adds up to

 the bottom.
next integrity check will be on can_id, which the metadata says should be nine

rs. The first character indicates the race, and the third and fourth indicate the
 we will expect to see “S” then “TX”.

               4 can_id ne
                5 SOTK00134
               6 soTxoo142
                7 S0TX00175
               8 SOTXO0217
               9 $2Tx00262
               40 $27K00270
               4% S2Tx00304
              12 $27X00312
                23 S2TX00320
               14 $2TK00338
               45 $27X00346
               26 S2TX00353
               17 $2TK00361
               48 $2TX00387
                19 $2TX00411
               20 $27K00429
             21 $27x00437_ |S
                  22 Grand Total

```

```
  That check confirms our thinking. Again, we have 17 candidates listed (one tied to

committee) and 8,022 total count.
 Along the same lines, we want to check the cand_name, which lists the names

candidates. We should see 17, with a total count of 8,022.

            Count of can_nam

```

```
 "ADDISON, MARSHALL GLENN
 ‘CASTANUELA, ANDREW PAREDES
 \CLEAVER, CURTIS C
 ‘CRUZ, RAFAEL EDWARD TED
Oo bh On Wrnu| DEWHURST, DAVID H
10 GARZA, STANLEY
11 GIBSON, JASON AARON
12 HUBBARD, SEAN PETER
13 JAMES, CRAIG
14 JONES, ELIZABETH AMES
15 | LEPPERT, THOMAS C
16 | PITTENGER, LELA MAE
17 SADLER, PAUL LINDSEY
18 SANCHEZ, RICARDO SAUCEDA
19 SHAPIRO, FLORENCE
20 | WILLIAMS, MICHAEL L

```

```
Oo bh On Wrnu

```

```
21 WILLIAMS,ROGER
22 |GrandTotal

```

```
Source: Federal Election Commission.

Note: Pivot table of can_nam, showing the candidate names and how many times each appears.

 That’s exactly what we have above.
 Next is ele_yea, or the election year. Since all of these candidates were running
2012 election, we should see only that date after our integrity check. Excel sums the
because they are stored as numbers, so we need to go into the pivot table settings an
Excel to count instead.

```

```
      ‘ 2. Sum of ele_yea
      4 \eleyea ir
        5 [
             oe tient
        6 ‘Grand Total.

 ederal Election Commission.

 t table showing ele_yea or year of the election. Excel sums the year values, which gives inaccurate results.

can change that by selecting the drop-down arrow on the Values box at the lower
hen picking value field settings. Using the box that appears, we can now select Count.

       Source Name: ele_yea
              , “custom Mae [count of ory hori cinuNe

      Summarize Values By | Show Values As |

       Choose the type of calculation that you want to use to summarize
        data from the selected field

        Average
        Max
                     | Ain
        Product

                      a) Wi

Microsoft Excel for Windows 2013.

nge to count in value field settings.

orked! We now see that 2012 appears 8,022 times.

        ‘Count aa, of ele RT yea Ee | 3 V ee
      ele eer yea |v [Total
             2012, 8022
               icici emieneemtninseommnieinanE ee eee
       Grand Total / 8022

 ederal Election Commission.

nt of ele_year. Now Excel reports accurate number. All of the entries are 2012, as expected.

```

```
have data about U.S. Senate candidates only, so we shouldn’t see “H” for U.S. Hous
“P” for president at all.

            4 canioff

              6 Grand Total

Source: Federal Election Commission.

Note: Pivot table for can_off column.

                 Our next couple of checks, for the state o

```

```
3 [count of can_off_sta
4 can_off_sta_
5 1X

6 Grand Total

```

```
race (can_off_ sta) and the district (can_off_d
likewise should generate no surprises. We sh

see “TX” for the state and 0 for the district (bec
there are no districts for U.S. Senate races: the

```

```
Source: Federal Election Commission. statewide contests).

Note: Pivot table with results for can_off_sta results.

Source: Federal Election Commission.

Note: Pivot table with results for can_off_dis column. All the entries are “O” because the data are for the Senate contests, not House

 Lin_num refers to the line number for the detailed summary page for FEC Form 3, w
is used to gather these data from the campaign committees. The line on the form cont
summary information, so any item listed as a row in the spreadsheet is a component of

               [count of lin_num ie

            119A
             20A

                ‘Grand Total
            can_off_dis |» [Total
          [sum of can_off_dis]

```

```
 lists seven different values, with 17 having the greatest number. Note that Excel

 data values stored as numbers to the right and those stored as text to the left. (If
 d, we could have formatted the entire column as text to avoid this annoying

eed more help in decoding what this all means, so we follow the Description of
 ink in the metadata and find a PDF document that explains what summary data
ch line. Committees use instructions located at http://www.fec.gov/pdf/forms/
.pdf when filing their reports.
age 7 of the documentation, the FEC tells us that Line 17 is supposed to summarize
ting expenses of committees and to provide details on what that covers. The FEC

 uctions for the other lines here, too.
 ext column, lin_ima, contains a URL that links to an image showing the spending
 m the original report filed by the committees. We don’t need to perform any
 ecause we wouldn't perform any analysis on this column, but would just use the
 r for looking up details.

next column, rec_com_id, is used to identify other committees that might receive
 rom our candidate committees for U.S. Senate in Texas. The committee IDs are
racters, starting with one letter.

         3 [count ofreccomidi

```

```
4 reccomid __|~ {Total
5 C00143743
6 = 00310532

```

```
 C00326835
8 (C00355461
9 C00457960
10 €00498121
12 SOTX00217
12 $2TX00270
13 $2TX00312
14 $2TX00338
15 S2TX00361
16 $2TX00411

```

```

```

```
 deral Election Commission.

 ts for rec_com_id column.

esting: out of our 8,022 total records, only a fraction (206) are for committee dis
ou could punch these into the FEC’s committee advanced search at http://www
nts to other committees. A dozen other committee ID numbers turn up in our

```

```
 Now, ifwe scroll to the bottom of our pivot table, we see we have around 1,780 en

with all 8,022 records accounted for.

         |1771 WOODALL, CYNTHIA
          1772, WOODFOREST NAT'L BANK
          |1773, WOODS, TOM
          4774} WOOT.COM INC
        1775 WORLD MAGAZINE
         1776 WORLEY PRINTING CO, INC.
         |1777 WORTHINGTON, CHRIS
         1778 WRIGHT, ROBERT J MR
         1779 WXXV
         1780 WYATT, JEANIE
         1781 WYNN LAS VEGAS
         1782 YELLOW CAB
         1783 YORK, PAUL W
         1784 ZEIDMAN, FRED S
          1785)

          1786 Grand Total

Source: Federal Election Commission.

Note: Dirty data in the rec_nam column. Note the date at the bottom.

 Now zip back to the top of the pivot table. We notice, for the first time, that we
lot of dirty data.
 Here are some examples:

  “ADOBE SYSTEMS” and “ADOBE SYSTEM, INC.”

  “ADVANTAGE RENT A CAR” and “ADVANTAGE RENT-A-CAR”

   Scroll down to find “AIRTRAN” and “AIRTRAN AIRWAYS”

  At this point, it’s easy to see how cleaning data can be a big job. A lot of peopl
Do I really need to clean everything up? Here, the answer is yes, if you wanted to d
tively be able to tell which vendor received the greatest number of payments or the
money.
 As with the vendor names, we can expect a lot of variation and dirt to appear
integrity checks of the recipient street address columns (rec_str1 and rec_str2).

 And so there is. Our check of rec_str_1 turns up some of these errors or inconsiste
 We have a number of blanks: 7,846 rows in this column have addresses.
 We have a number of PO boxes, which are not physical addresses.
 So far, our integrity checks hav
columns that we’ve looked at had little variation in terms of data values. That’s abo

change with the next column, for the name of the recipient (rec_nam).

  Street directional prefixes sometimes are spelled out, and sometimes are abbrev

```

```
get many fewer rows in our check of rec_str_2. For one thing, committees do not
t as often as rect_str_1. Here is what we find in terms of dirty data:

 boxes are listed in this column, too.

uite” is spelled out sometimes, abbreviated others.

loor” is spelled out sometimes, abbreviated others.

e do checks for rec_cit and rec_state, so we can see the location of the person,
y or committee that got the payment.

eck of rec_cit tells us:

 have 289 distinct values listed;

e vast majority of records have city data: 7,887 in all;

e city names are pretty consistent; and that

 do have some errors: “FORT WORTHZ” and “FT WORTHS” for Fort Worth.

eck of rec_sta reveals payments went to 39 states; and all the states are listed
y.
 might not be the best way to test the integrity of our locations, though. Cities don’t

lone—they’re part of states, right? We can use pivot tables to combine cities and
n our results. It’s a little more complicated than the pivot tables we've been building
Let’s walk through the steps.
t the pivot table and add rec_cit to your rows. Then add rec_sta to your rows and

ure it’s under rec_cit. Put rec_cit into the Data Fields area and make sure it’s set to
Your pivot table builder should look like this:

                              xis (Compatibility Mode) - Excel PIVOTIARE TOOLS 78 - xX
    HOME SNSERT PAGE LAYOUT WRULAS DATA REVIEW View ANALYZE DESIGN Herzog, David ~'S <2

   Active Fel x Pe 4 is we
ee able fee ann 4 mit De a Group * wart Tinelase Refresh acd Change Data 3 Actions 7/5
   Bi Field Settings . of Fite eects Source

            achive Pinte Fitter Data “a

                                                                                                        Hf

                              é F 6 H f i 4 res
                                           PivotTable Fields ~#

 ount of rec ct Choose fields ta add te report: Yr j
ec _cit ix irec stai7 secusted vA
 S ABILENE bs sec gti
 BILENE Total E 4 vec cit
 &CWORTH GA YZ rec.sta .
ACWORTH Total
SADDISON Tx Drag fields between areas below:
 ALBANY pOt SON Total oe. 1% : ¥ FuteRs #8 COLUMNS
 LBany Total t
AEDO IK
LEDOTotal Zi
 ALEXANDRIA VA om ROWS © VALUES
 LEXANORIA Total reece + | | Count ofrec ct >
B AUN EX ee, stis x
 LER TOO
 ALLEYTON ™ i ;
  > dian i Sheet3S is | secon Sheatis | iP Sheetls | } sheetie 0. @ vo Pe 4S + j Defer La y out out Ups Update
         Romeeernesereecernoree i

 ederal Election Commission.

```

```
731 2WASHINGTON
732 1 1
733 WASHINGTON Total

```

```
  It’s a little confusing, because Excel also tell
under each city, how many times each city appears.
can see this better by scrolling down to Washingto

```

```
Source: Federal Election Commission. Much better, isn’t it? We can see that we hav

```

```
Note: Detail of city and state pivot table.

```

```
Amarillo in Tennessee, which could very well

```

```
typo. Farther down the list, we see “Pittsburg” (missing an h) in Pennsylvania, an obv
misspelling that we'd want to clean up before we used the city column for analysis.
                 Our last address column check is rec_zip fo

```

```
3 |Countofrec zipi
4 reczip iv

```

```
zip code of the recipient.
  Straightaway we spot some problems—namely
codes with only four characters. That's in conflict with
metadata, which says a zip may have five or nine charac
  Let’s go back to our original sheet with the
and sort it by rec_zip, so we can get a better pictu
what the problem is. Practice safe computing: S
the entire sheet by clicking on the button betwee
and 1. This highlights everything and tells Excel
you want to keep your rows together while sortin
 Pick the Data tab and then the big Sort but
You get this dialog box, which allows you to con
how Excel sorts the sheet.
 Make sure the My data has headers box is che
because this tells Excel to use the header names i
Sort by drop-down list. Pick rec_zip and Smalles

```

```
Source: Federal Election Commission. Largest in the Order drop-down list. Excel sh
Note: Pivot table for rec_zip. look like this on your screen:

          | SL aAdd Level. 2 My data has headers

            | Cobumn

Source: Federal Election Commission.

Note: Excel sort dialog box.

```

```
he zip codes with four characters are from New England or New Jersey. Those zip codes

fe all have leading zeroes, which somehow got stripped out of our data. We would need
hose if we wanted to use the zip column for any analysis. We might also want to extract
racter zip codes from the ones with nine characters, to keep our data consistent.
 next couple of checks will be handy in looking for suspect values. These are
, or numbers that are so extreme that they might be incorrect. Suspect values
op up in columns that contain dates or numbers.

 dis_dat column tells us the date that the

```

```
ement was made. Because this comes from
2 federal election cycle, we expect all will be
e start of 2011 through the end of 2012.
 check reveals some flawed data that we see
 the top of our list. Namely, one instance of

16—a date in the far past! Next, the dates
th January 1, 2011, just as we expected. A
f the bottom of the pivot table shows all of
ies end within our expected time frame.
 for the amount of disbursement in the

o column.

```

```
 3 |Count of dis_dat be i

Source: Federal Election Commission.

Note: \ntegrity check for dis_dat column. This
shows we have an outlier, a date that’s so far in the
past that it’s no doubt an error.

```

```
        3 Countofdisamo
        4 disamo _ x |Total
         5 | -2400, 1
      6 -1503} 1
        7 | 500, 2
        8 -200, 2
        9 169 1
        10 -150, 1
         11 149.17) 1
        12 100 1
         13 79, 1
         14 50, 1
      15 25, 4
      16 0) 44
         17 | 1.13} 1
      18 a i
       19° 0.01 2

 ederal Election Commission.
_amo integrity check. Negative numbers are often used by the Federal Election Commission to indicate refunds.

```

```
  At first, you might think these results are odd—how can committees have nega
spending amounts? But if you are familiar with the FEC’s data, you know that nega
amounts are often used to denote refunds. They could be money that vendors returne
campaigns, or they could be typos.

  At the other end of our amount, we see two payments exceeding $1 million. That’s
compared to most of the other amounts, so we would want to look more closely at th

 Our next column (dis_pur_des) sets aside 100 characters for the campaigns to
free-form descriptions of the reason for the spending. So we expect that we'll get a l
variation and overlap.

```

```
 BALLOT ACCESS FEE
 BANK CHARGE
 BANK CHARGES
80 BANK FEE 144
81 BANK FEES 3
82 BANK SEE CHARGE 1
83 BANK SERVICE CHARGE 1
84 BANK SERVICE CHARGES 2
85 BANK SERVICE CHARGES, MEALS (SEE BELOW I 1

```

```
84 BANK SERVICE CHARGES

```

```
85 BANK SERVICE CHARGES, MEALS (SEE BELOW I

```

```
     86 BANK SERVICE FEE 14
    87 BANKING FEE 2
     88 BANNER 1
     89 BANNERS 2
     90 BATCHING/CAGING 1
     91 BEVERAGE - FUNDRAISER 1
                 2 BEVERAGE & WAIT PERSONS FOR FUNDRAISER 1

Source: Federal Election: Commission.

Note: \ntegrity check for dis_pur_des column. These results show a lack of standardization in how this column is filled

  Indeed, there are many ways that campaigns have entered bank fee disbursements,
example. We'd need to scrub this column a lot in order to use it.

                 Mem_cod, the next column, is impor
   Count of mem_cod because it tells us whether the data stored in a
  “imem_cod hold details from a credit card payment. An
 5 xX indicates an itemized payment that’s
 6 (blank) accounted for in a credit card payment. If we
 7 Grand Total lyze the data, we’d want to make sure that we’r
                double-summing or double-counting these it

```

```
Source: Federal Election Commission.

Note: Mem_cod integrity check.

```

```
 The pivot table tells us that we have 718 m
entries whose dollar amounts are also incl

```

```
in the credit card payment. An integrity check of the mem_tex column, used to

```

```
3 ae [Count of mem_tex
 mem fer ____ iran moxteortene etiam

```

```
Oo MWwsHm te&

```

```
[MEMO ITEM]

[MEMO ITEM] SUBITEMIZATION OF AMERICAN EXPRESS(02/16/11)

[MEMO ITEM] SUBITEMIZATION OF CARD SERVICE CENTER(02/20/12)

[MEMO ITEM] SUBITEMIZATION OF CARD SERVICE CENTER(03/22/12)

```

```
fx & [MEMO ITEM] SUBITEMIZATION OF CARD SERVICE CENTER(04/18/212)

```

```
 14 [MEMO ITEM] SUBITEMIZATION OF CARD SERVICE CENTER(05/18/12}

 i2 {MEMO TTEM] SUBITEMIZATION OF FASKEN MANAGEMENT LLC(12/29/1

 13 [MEMO ITEM] SUBITEMIZATION OF VIRGINIA BELL(01/29/11}

 24 ACCOUNTING SERVICES

 15 BANK CHARGES

 16 CONTRIBUTION

 17 FOOO/BEVERAGE

 eral Election Commission.

tex integrity check.

 of the entries are “[MEMO ITEM]”, with 582. We'd have to explore individual
more to make sense of this.
at_cod column is supposed to hold a code with a value from 001 to 012 that categorizes
n for the disbursement. As it did with zip codes, Excel stripped the leading zeroes.
t a big problem here. But we see 12 entries for 0 and eight entries for 17, which are

ur range of values, and some for “ENT” and “IND”, which are not listed in the metadata.
see that 005 and 008 do not appear in our data, leaving us with 10 valid codes in all.

             Count of cat_cod i al

        14,
          15 |
         16 |
          17 ENT
         18 IND
        19 (blank)
           20 ‘Grand Total

 eral Election Commission.

```

```
 A check of cat_des provides a list of the descriptions behind the codes.

       3 [count of cat_des

       5 Administrative/Salary/Overhead Expenses
       6 Advertising Expenses

        7 Campaign Event Expenses
       8 Campaign Materials
       3 Donations
       10 Loan Repayments
        11 Poiitical Contributions
       12 Refunds of Contributions
       13 Solicitation and Fundraising Expenses

        14 Travel Expenses

        16 Grand Total

Source: Federal Election Commission.

Note: Cat_des integrity check

 We get 10 descriptions, which match the 10 valid codes on our earlier check.
 We could have included the cat_code and cat_des together to get an even better

```

```


```

```
| Count of cat_cod |
catcod

```

```
hj hoa 21 Administrative/Salary/Overhead Expenses | 975
<= eee

ae
12/3 Total
Beira eee
14|4Total

16 6 Total
i a
18 7 Total
eae
20 9 Total
21.

```

```
ing around to our last checks, we expect to see unique values in the tra_id column,
s the transaction identification number. We can find the multiples by creating the
ble normally, then sorting the Count column descending, to put the biggest counts
op. Do that by right-clicking on any number in the Count column, then picking
ort Largest to Smallest.
 check shows several dozen IDs that have duplicates. We'd want to question the FEC
hat.

          4itraid et
           5 |se0427100212703
                ($B05101005126
                '$B0427100212711

               '$B0427100212673

                '$B0427100212699
             '$B0427100212674
             '$B0427100212707
             '$B0427100212675
             '$B051010051212
            $B0427100212676
             '$B0427100212697
             '$B0427100212677
             '$B0427100212701

Federal Election Commission.

_id integrity check.

 bac_ref_id, our last check, is used to identify whether a transaction is part of a
credit card transaction. This shows we have 95 records that are part of larger
tions.

           3| Count of bac_ref_id [
              4 bac_ref_id
             5 S$B17.12598
             6 $B17.14042
             7 $B17.14076
             8 $B17.14114
             9 $B17.14717
              10 $B17.14735
             11 $B17.14741
             12 $B17.15201
              13 $B17.15235
             14 $B17.15241
              15 SB17.15496
            16 (blank)
                17 Grand Total

```

```
doing these checks, we get to know our data inside and out. To recap, our data integ
checks here unmasked inconsistencies in the names and addresses of recipients. We
discovered some negative numbers, which are probably refunds.

  As students or professionals who use data to create information and knowledge,
important for us to know these data’s strengths and shortcomings.
  In the next chapter we will learn how to clean our data so we can analyze and visua
them later with confidence.

ON YOUR OWN

Download a copy of the 2014 disbursements files for the U.S. Senate candidates in
state from the FEC data portal at http://www.fec.gov/data/CandidateDisbursement
and run integrity checks. Keep notes in your data notebook. What problems do you
How would these problems impair your analysis?

```

```
    A

he previous chapter, we learned how to use integrity checks to uncover flaws in our
a. In this chapter we will learn some tricks that we can use to scrub some of the most
mmon data dirt. We will also learn some techniques for transforming our data, so
e better prepared for analysis and visualization.
will use Excel to perform most of our data cleaning and transforming tasks, but we
o use OpenRefine and a PDF conversion service.
l and other spreadsheet programs have built-in features and functions that can help
ata into shape. For example, we can use Excel’s Text to Columns tool to parse—or
ata that are stored in one column into multiple columns. This is useful when we have a

 for full names that are stored like, “Doe, Jane”. Using Text to Columns, we could carve

o one column for the last name, and another column for the first name. Excel also has a
 Duplicates tool that allows us to remove rows that hold data that are repeated. In addi
 can write formulas in our Excel spreadsheets to carve out data and then assemble them.

handy when we have dates stored as text, such as “20150101” for January 1, 2015.

nRefine (which runs on Windows, Mac and Linux computers) is an open-source
m from Google that lets users quickly run data integrity checks, then clean flawed
s creators call it a power tool for working with messy data (http://openrefine.org).
etdocs and Zamzar are two online converters that allow us to extract Excel files
DF tables.
n there are even more-powerful and more-complex tools for data cleaning that are
 the scope of this book. More-advanced data users will use database managers, such as
ft Access or MySQL, to clean data using string functions. String functions are code

 be inserted into the Structured Query Language (SQL) that these database managute. For instance, someone who’s adept with SQL can write queries to rearrange dates
roper format and put them into a new column. Data users who are even more advanced
cripts using programming languages like Python, Ruby, PHP or Perl to clean and
rm data sets. These programming languages allow users to process huge amounts of
re quickly than they could using traditional programs like database managers and
heets. In addition, a number of companies offer data cleaning services and software.
a deeper look at data cleaning, check out the Bad Data Handbook (McCallum, 2012)

 Practices in Data Cleaning (Osborne, 2013), which is geared to working with
 data collected for the purposes of research.
TER 7 GETTING YOUR DATA IN SHAPE

```

```
we'll start to tackle some of the most common challenges now.

COLUMN CARVING
Government agencies often stuff too much data into one column, which makes it diff
for us to work with them. In Chapter 5, we took a look at political campaign contribu
data from the Missouri Ethics Commission that stores all the identifying data about
tributors into one column. This is an extreme example of dirty data. Someone with adva
data-cleaning skills might be able to parse these data elements into separate fields, but

would take a lot of work. As shown in that chapter, the commission now provides t
data with the data broken down into multiple columns that users can work with better
 Most column parsing challenges are far simpler, such as the one in our spreadshee
dangerous dogs that have been reported to animal control authorities in the city of Aus
Texas. The city’s Animal Services Office allows people to fill out forms asserting that a

is dangerous or has bitten another animal (AustinTexas.gov, n.d.). The original fil
been modified for this exercise. The file is called Austin_Declared_Dangerous_Dogs.x

and has 40 rows, including one for the column headers. (You should have your data
book open so you can record any activities.)

 Wesee four columns, one each for the street address, zip code, description of the
and the dog’s location, which includes latitude and longitude points that some

  @ © Dany
       HOME INSERT  PAGELAYOUT FORMULAS DATA REVIEW VIEW

  oe Arial “16 «lk « o ea i ae: a (ey Prinet ~ 2+ bey

      Baked 7 ae * sh 4, Pig se 78 fe Formatting~ B Format Tabler as Styless Cal o BaFormaty Meet & €.> : oi Fier Select dp =

                      For G veatober te Styles Cais Editing

   cis = & Keely,spayed female, Red, Labrador Retriever mix

   2 1305 Webbendille Road 78721 Rex,neutered male,tan and white,Pit Bull mix 1205 Webberville Road?8721{30.278952179610542,
   3 1304 Webbenille Road 78721 Scooby neutered rogle,red. Labrador Retriever mix 1305 Webheralle Road78721(30.278952179610542,
   4 3904 Caney Creek 78732 Salty, male. brown and white Boxer 3904 Caney Creek78732(30.368250000437342. -97
   5 3310 Catalina Drive 78741 Junebug. spayed female tive tick Australian Cattle dog 3310 Catalina Drive78741(30.21942605449118, -97
   6 .11511 Catalonia Drive 78759 Bumpy.neutered male.white and black American Bull Terrier 41511 Catalonia Orive?8759(30.410837 755207353,
    7? 11511 Catatonia Drive 78759 Litle Gir spayed female brindle and white American Bull Tecier 11511 Catalonia Drive78789(30.410837755207353,
   8 (8501 Daleview Drive 78757 Nibbles female red and tan, Golden RetrieverChow mix 8501 Dateview Drive78757(30.38952290 1181313. S
   $ TOS Texas St 78705 Jack. neviered male. red/e/nite Labrador Retriever mix 705 Texas St78705(30,29690981952457, -97.72864
   20 12401 Cecil 78744 Pinky female,white Boxer mix 2401 Cacd?8744{30.16497926089337. -97.7728720
   £1 (2401 Cecit 78744 Smokey male, brown brindle,Pit Bull mix 2401 Cecil?8744(30.16497926089337, -97.7728720
   42 2404 Cecit 78744 Shebba,female white,Pit Bull mix 2404 Cec#78744(30 16497925089337, -97.7728720
   £3 13206 Billiem Drive T8757 Nibbles formale,red and tan, Golden Retriever/Chow mix 43206 Billiem Drive78757(30.383199999780315,    34 5806 Shoalwood Avenue 78756 Nippy female black and tan, Shepherd mix 5806 Shoahwood Avenue?8756(30.33499792847647,
   18 2620 East 3rd Street 78702 Keely spayed female Red Labrador Retriever mix 2520 East 3rd Street78702(30.255767657695174,
   16 1128 Richardine Avenue 78721 Mariey neutered male. white and trowm American Bulldog mix 1428 Richardine Avenue?8721430.269797081352237
   17 525 Shep Street 78748 Chico. male,chocelate and white Pointer mix 526 Shep Street?87$8(30.173695529301256. -87.7
   4B 2305 Thomedld Pass 18758 Lincoln male fawn and white Pit Bull Terrier 2305 Thornwild Pass78758(30.41308606028059,    19 1202 Richcreek Road 78757 Cali female. black. Labrador Retriever mix

          Dangerous dogs & y

Source: Retrieved from Data.austintexas.gov.

Note: Austin declared dangerous dog data. Note the Description of Dog column has four pieces of data, separated by a

```

```
 to create a webmap. The Description of Dog column has a lot of different bits
mashed together: the dog’s name, sex, color and breed. Each piece of data is
d by a comma, a pattern that is important to note before using the Text to
 tool.
get ready by saving a copy of the spreadsheet with a name other than the original,
 serve the original copy. We will work with the new file.

 use Text to Columns, it will overwrite our original data in Column C. We want to

 that for reference, so insert four columns to the right of Column C. We'll need four
 because we're going to parse out four data items. Right-click on Column D and
 rt from the popup menu four times. You should have blank columns from D
 G.
ice safe computing by copying the contents of Column C into Column D: RightC and pick Copy from the popup menu, then right-click on D and pick Paste. Your
eet should look like this with Column D highlighted:

```

```
- Pes Austin Declared Dangerous Seysadon Excel
 OME INSERT  PAGELAYOUT FORMULAS «DATA «REVIEW VIEW

```

```
x

```

```
  4. SA ike
PivotChart Power Line Column Winf
  - ew

```

```
                    Apps charts T Reports Sparvkhines Filters Links

                Description of Dog
          __... . .. ss. F

                                                   SIGE: Se.

 trieved from Data.austintexas.gov.

 iption of Dog column, ready for parsing.

 we’re ready to tell Excel to perform its magic. Click on the Data tab and then

d.
 to Columns button. Excel launches a Wizard that walks us through carving
data in three steps. In the first step, tell Excel the correct data type, which is

```

```
              The Text Wizard has determined that your data is Delimited.

                if this is correct, choose Next, or choose the data type that best describes your data,

               Original data type

              Choose the file type that best describes your data:

                    © | + Characters such as commas or tabs separate each field.

               ©) Fixed width - Fields are aligned in columns with spaces between each field.

              Preview of selected data

                scription of Bog
               ex,neutered male,tan and white, Pit Bull mix
                cooby, neutered male, red,Labrader Retriever mix
               alty,male,brown and white, Boxer
                junebug, spayed female,blue tick,Australian Cattle dog

Source: Microsoft Excel for Windows 2013.

Note: Step 1 of the Text to Columns Wizard for delimited data.

  Click Next and it’s time to set more options. We need to tell Excel that the delimi

a comma, so make sure only that box is checked in the Delimiters section. We have n

qualifiers (single or double quotation marks to denote text), so change that to None.

preview area, Excel draws lines where the column breaks will go, based on the posit

the comma delimiters.

                This screen lets you set the delimiters your data contains. You can see how your text is atfected
                 in the preview below.

                 Delimiters

           Tab
                 Semicoton (| Treat consecutive delimiters as one
       cai Tedt quatitier: ama

            Flothes |

                Data preview

Source: Microsoft Excel for Windows 2013.

Note: Step 2 of the Text to Columns Wizard for delimited data.

  Click Next and we're in the last step of our wizard, where we set the data types f
four columns that we are creating. Change all of these from General to Text. Do t

```

```
           —

        This screen lets you select each column and set the Data Format,

        Column data format

         &S General
         Text “General converts numeric values to numbers, date values
                                                     : to dates, and all remaining values to text.
          Date: “MDY

         ©) De not import column {skip}

      Destination: spsi ae

        Data preview

 icrosoft Excel for Windows 2013.

p 3 of the Text to Columns wizard for delimited data.

                           Austin Declared Dangerous Doga.xine- Excel eo - oO
  HOME INSERT PAGE LAYGUT FORMULAS DATA viEW Herzog, David - S|
 Refresh Fy) BCennections a 4: Le ao (PFE sop a! | : Ree 7 Ke Y= ee Ctear iki es © lash Fill re Duplicates ee &
  At x nY VW Advanced — eghumn: ation +

     Connections Fitter Date Tools Outune we a

           neutered male tan and white 1305 Webbenilie Road?
           neutered mate ted Labrador Retriever mix 1305 Webberiie Road?
          male brown and white Boxer 3904 Caney Creek?873
 g spayed fernale blue tick Australian Cattle dog 3310 Catalina Diwe7B74
           neutered male white and black American Bull Terer 11811 Catatonia Drive?
 i spayed female brindle and white Amencan Bull Tesier 11511 Catalonia Divve78
           fernale red and tan Golden Retriever/Chow mix 8501 Daleview Orive787

           neutered male redivfnite Labrador Retriever roix 705 Texas St78705(30.7
           female fhe Boxer mix 2401 Cecif78744(30. 16¢
         male brown twindle Pit Bull mix 2401 Cecil?8744(30_164
          female vite Pit Bult mix 2401 Ceail78744(30 164
           fernale ted and tan Golden Retriever/Chow mix 13206 Billiem Deve787€
           female black and tan Shepherd mix 5806 Shoahyood Avenut
          spayed femals Red Labrador Retriever mix 2520 East 3rd Street78!
           newmered male white and brown American Bulldog mix 1128 Richatdine Avenue

           male chocolate and white Pointer mix 625 Shep Street /3748(          male fawn and white Pit Bull Terrier 2305 Thornwild Pass 73)
          female black Labrador Retsiaver mix 1202 Richereek Road7é

    Dangerous dogs @ 4 i

 etrieved from Data.austintexas.gov.

 ed Description of Dog column. Note that each of the four pieces of data is stored in its own column.

Column D holds the name of the dog, Column E the sex and whether it’s been
d or spayed, F the color and G the breed. Now that we've placed the breed of
mn D will be modified. (This is why we saved the original in Column C.)
verwriting existing data, click OK. That's just Excel’s way of telling you that the data

```

```
“sex”, Fl to “color” and G1 to “breed”. Now save the file and close it because we
done with it for now.
 Carving up data using Text to Columns usually is more complicated than this bec
of the way government agencies store data. Get the Excel file fuel_economy2013.xlsx
the book website and open it. Make a working copy using File | Save As. This file from
U.S Department of Energy and the Environmental Protection Agency lists fuel econ

data for vehicles that are sold in the United States. The data are in 1,166 rows, inclu
one for the headers. Let’s scroll over to column AC, which provides descriptive data a
each vehicle’s drive system. The first line tells us that the drive system for one partic
variant of the Aston Martin V8 Vantage is “2-Wheel Drive, Rear”. That’s actually two pi
of data: the drive system is two-wheel and those two wheels are the rear ones. We could
the comma and space that follows it to carve this into two distinct columns.

  Using Insert, create two new columns, one for the number of wheels and the othe
designate which wheels propel the vehicle. Copy the contents of AC and paste them
AD. Make sure AD is highlighted and start the Text to Columns Function.
 Choose delimited in the first screen of the wizard and pick Next.

          The Text Wizard has determined that your data is Delimited,

           If this is correct, choose Next, or choose the data type that best describes your data.

          Original data type

         Choose He type that best describes your data:
          @ Di || «Characters such as commas or tabs separate each field,

                                       _) Fixed width - Fields are aligned in columns with spaces between each field.

           Preview of selected data:

         [a brive Desc
           i-Wheel Drive, Rear
           2-Wheel Drive, Rear
          4¢-Wheel Orive, Rear
         Is | ~Wheel Drive, Rear

Source: Microsoft Excel for Windows 2013.

Note: Step 1 in the Text to Columns wizard for delimited data.

  Set the delimiter to Comma only and make sure text qualifier is None. Excel gi
preview of howit’s going to parse the data. Look closely and you will see that Excel is inc
ing the spaces on either side of the comma as text. That’s OK for now. We'll fix that la

```

```
     This screen lets you set the delimiters your data contains. You can see how your text is affected
     in the preview below.

     Delimiters

    ©) Semicoton ©" Treat consecutive delimiters as one

             | Cancel ik <Back | ] Ciget >) (ce Finish el

icrosoft Excel for Windows 2013.

p 2 in the Text to Columns wizard for delimited data.

k Next to move on to the third and final step. Change both of these columns to Text
n Finish.

     This screen lets you select each column and set the Data Format.

     Column data format

     © General :
                        ‘General’ converts numeric values to numbers, date values
                     to dates, and all remaining values to text.
       © Date: (Mor [x] (Advanced... |

     *) Do not import column (skip}

   Destination: SADS1

     Data preview

icrosoft Excel for Windows 2013.

 3 in the Text to Columns wizard for delimited data.

```

```
“NumWheels” (for number of wheels) and AE “DriveWheels”.

                  a Te
          Drive Desc
         2-Wheel Drive, Rear
         2-Wheel Drive, Rear
         2-Wheel Drive, Rear
         2-Wheel Drive, Rear
           All Wheel Drive
         2-Wheel Drive, Rear
         2-Wheel Drive, Rear
         2-Wheel Drive, Rear
         2-Wheel Drive, Rear
         2-Wheel Drive. Rear
          All Wheel Drive

Source: Department of Energy.

Note: Data parsed, but with extraneous spaces.

 Our next step is to remove those extraneous spaces using Excel. We want to rem
these because the spaces technically are data (one of the basic ASCII characters) and c
throw off any analysis. Column AE has leading spaces in the cells. We have “Rear
“Front” for the values, when we really want no leading spaces in them. Excel’s TRIM f
tion can help here. TRIM removes any leading and trailing spaces, as well as duplic
spaces inside a text entry.

  Insert a new column to the right of AE and make sure it is formatted as General, or
your formula will appear, instead of “Rear” or “Front”. Format the column by highligh
it, then clicking the Home tab. Select General from the options in the drop-down list.

           Arial “ho. *|a aw = ov & |
      Bru- B+ &-a- El- $~% > aE f

       Clipboard tf Font % % Number %

               % he

           JURE 5 een etn La ede ny Serene
      1 |Drive Desc NumWheels _ DriveWheels —
    2 |2-Wheel Dnve, Rear 2-Wwheel Drive Rear
      3 |2-Wheel Drive, Rear _—-2-Wheel Drive Rear
      4 |2-Wheel Drive, Rear 2-VWiheel Drive - Rear
     5 |2-Wheel Drive, Rear 2-Wheel Drive Rear
    6 |All Wheel Drive All Wheel Drive
     7 |2-Wheel Drive, Rear —-2-Wheel Drive Rear
     8 |2-Wheel Drive, Rear —-2- Wheel Ore _ Rear
      9 |2-Wheel Drive, Rear 2-Wheel Drive Rear
      71% \2-\Wheel Drive, Rear 2-Wheel Drive Rear
      11 |2-Wheel Drive, Rear 2-Wheel Drive Rear

Source: Department of Energy.
                                                       Excel

                       PAGE LAYOUT
    Mo %~- > ¢ fuel_economy2013 xIsx 
           HOME INSERT FORMULAS DATA REVIEW VIEW

```

```
 MW: @- s fuel_economy2013.xkex + Excel

   FILE HOME INSERT PAGE LAYOUT FORMULAS DATA REVIEW VIEW

 AF2 ad fe — =TRIM(AE2}

ee
 1_ Drive Desc NumWheels DriveWheels DriveWheels2
 2 |2-Wheel Drive, Rear 2-Wheel Drive Rear Rear
 3 2-Wheel Drive, Rear 2-Wheel Drive Rear
 4 2-Wheel Drive, Rear 2-Wheel Drive Rear
 & 2-Wheel Drive, Rear 2-Wheel Drive Rear
 6 All Wheel Drive All Wheel Drive
 7 2-Wheel Drive. Rear 2-Wheel Drive Rear

 partment of Energy.

 function.

 are just two examples of how you can carve data in Excel using Text to Columns.
es we do the opposite and combine the contents of multiple columns into one.

 we turn to concatenation.

ENATE TO PASTE

ing to use concatenation to put election date data into a proper form. Open the
nout.xlsx Excel file, which holds data about voter turnout by precinct in Boone
 Missouri, during the November 2, 2010, general election. The spreadsheet has
 for the precinct or voting district, number of people who voted, number
d and date. All of the dates are recorded as “20101102”. Our goal is to turn all of
 11/2/2010.
 use the Text to Columns tool to carve the date and then use concatenation to
 pieces back together. Practice safe computing by copying the contents of
 D into Column E, which we will parse. Highlight E and pick the Text to
 button from the data menu. That launches a familiar wizard to help. Our
 not delimited this time, so punch the Fixed width button. We can tell that the
e fixed width because the characters for year, month and day are in consistent
.
ls in this column by double-clicking on the square at the bottom right of your
ox.
E2. Hit Enter and you should see the new, trimmed version. Copy this for all of
ll AF2, enter the trim formula: “=TRIM(AE2)”. This says, Trim the contents

                 = Ee
 ee Ble $= 9 eS

  Clipboard Alignment
  eae Ei « Anal ; General Tovecesannnnnssanutecooenpnsrnsiihiconennnannnnniinit “ 
                                                                                                                   +

       & Font Number
 “Oe

                           % te %

```

```
      Convert Text to Columns Wizard -Step1of3 ym Lf Bs

        The Text Wizard has determined that your data is Delimited.

        If this is correct, choose Next, or choose the data type that best describes your data,

         Original data type

        Choose the file type that best describes your data:

         ©) Delimited __- Characters such as commas or tabs separate each field.

       @ Fixed width — - Fields are aligned in columns with spaces between each field.

         Preview of selected data:

Source: Microsoft Excel for Windows 2013.

Note: Step 1 in Text to Columns for fixed-width text.

  Click Next and we're at Step 2. In this screen, we create the column dividers by cl
where we'd like them to go inside the Data preview area. Don’t worry if you put a
in the wrong position—Excel allows you to move or remove it. Create column brea
positions 4 and 6, just like this.

      This screen lets you set field widths (column breaks).
       Lines with arrows signify a column break.

        To CREATE a break line, click at the desired position.
        To DELETE a break line, double click on the line.
        To MOVE a break line, click and drag it.

       Data preview

```

```
     This screen lets you select each column and set the Data Format.

     Column data format

                ) General
                        ‘General’ converts numeric values to numbers, date values
                       to dates, and all remaining values to text.

     ©) Do not import column {skip}

     Destination: $&$1

     Data preview

Microsoft Excel for Windows 2013.

p 3 in Text to Columns for fixed-width text.

ess! Excel has put the year in Column E, month in F and date in G. Label those three
s accordingly and save a working copy of the file with File | Save as.

 1 Voting Registered Date ate
 2 360 1030 20101102)26"
 3. 234 420 _20101102)20"
 4 708 1153 zi
 5 474 1136 20101102/201
 6 75 2704 —-20101102)20
 7 162 1011 20101102)20
 a 373 759: 20101102/2010
 9 163 1026 —20101102)20'
  0 629 957 —- 20101102120
            503 1171 20101102|2010
               for 1212 oniniinsiaain

Boone County, Missouri, Clerk.

ed-width text parsed.

l Column H as “Date2”, which is where we'll put the restructured date that we'll

ith concatenation, which uses the ampersand (&) character.

ell H2 enter “=F2&“/””. This tells Excel to take the contents of cell F2 (or 11 for the
of November) and tack on a slash. We need to put the slash in double quotation
so Excel treats it as a text character. We get “11/” for a result, which is a good start.

 we will tack on the date, by building on the formula “=F2&"/"&G2”. Now we see
nish.
k Next and go to the final step. Make sure all of the new columns are set to text and

     ©) Date: _MDY Ix] [ae : ;

```

```
  As the last step, will add another slash and the year: “FIR /” &G2&"/" &E2”. Now

have “11/02/2010” in our cell. Copy this for all of the cells in Column H and format i

short date. Save the file and close it.

DATE TRICKS

Excel offers other functions that transform data stored in dates. These are handy for genera
a month or a year. Open the disaster_declarations.xlsx Excel file and we'll see how this wo
This file, originally downloaded from the federal government's Data.gov portal, holds

about more than 4,100 major disasters declared since 1953. Under federal law, state gover
may request a declaration ofa major disaster and receive federal assistance (Federal Emerge
Management Agency, n.d.). In Column G, we have a declaration date, but not a month or
So it would be difficult if we wanted to analyze the data from either of those dimensions.
  Excel’s YEAR and MONTH function can extract these data. We'll use another func
to generate the day of week, by name, for the declaration dates.
  Insert three columns between columns G and H, so we have a place to put the year, mo
and day of the week. Label these “Year”, “Month” and “Day”. Format these columns as Gene

  In cell H4, enter “=Year(G4)” and “1953” appears. Copy this formula for all of the c
  In cell 14, enter “=Month(G4)” and “5” appears for May. Copy this formula for all of the
  In cell J4, enter “=TEXT(A4, “dddd”)” and Sunday appears. Copy this formula for

the cells. The TEXT function, in this case, returns a text value from the data stored in
dddd tells Excel to generate the day using its full name. Use ddd to generate an abbreviat
 Use File | Save As to save a working copy of your file and close it.

                                       dizarter selsratord wee [Corpatiohty Mode) - Exel 76 ~ o

               INSERT PAGE LAYOUT FORMULAS DATA REAEW VEw Herzog, David «

                 9 KK Genvrat Geter «2 by a
      Big . Se = fe we 9.1 £ . ¢ ~% > ? “Bx ** og Formatting» Conditional nditional F Format Tabley ites as Styles» Col. @eformaty (en am | @~ Finer rere Select in

                                Algoment % Humber % ‘Stas Celts Editing

                                     5i2/1952 41952 5 DR Ternado TORNAD

           No Yes Yes Yes ™% SASH3S3 1983 $ fdonday DR Tomado TORNADO

            Ne Yeo Yes Yes tA §42911953 1983 5 Tuesday DR Flood “FLOOD

           No Yes Yea Yes wy BRIER 1863 6 Wednesday DR Tomads TORNADO

           No Yes Yes Yes MT BIBM953 1963 § Thursday DR Flood FLOODS

            No Yes Yes Yes wi BBI1ISS Bix! & Friday DR Tornede TORNADO

           No Yes Yes Yes MA 644111953 1983. 6 Gaturday DR Tomade TORNADO

           No Yes Yes Yes i& BANGER 1953 6 Sunday DR Piped FLOOD

            No Yes Yes Yes 7x 69853 4953 6 Monday DR Flood FLOOD

           to Yes Yes Yes He FAGES 1983 7 Wednesday DR Fire FOREST
           No Yes Yes Yes FL 40/22/1963 1953 10 Thursday OR Flood FLOOD

           Instructions | Metadata | Declaration co) 5 fy

Source: Federal Emergency Management Agency.

Note: Year, month and day extracted from date in Federal Emergency Management Agency disaster declaration data set.

```

```
 SCRUBBING WITH OPENREFINE

ine, a free and open-source program, can help for many data cleaning
es. (Find the program for Windows, Mac and Linux operating systems here:
/github.com/OpenRefine/OpenRefine/wiki/Installation-Instructions.) We'll
Refine to perform one of the most common, frustrating and time-consuming
tandardizing data entries. In Chapter 5, we learned how poor data-entry con lead to messy data. Such is the case in this Excel file of campaign contributions
 by the Missouri Ethics Commission named mo12contribs.xlsx. Open the file

 that we have 19,867 rows, including one for the headers. Each row represents
ign contribution made by a person, company or political committee. We can
educated guess that Column J, which has the city of the contributor, might have
typos.
 OpenRefine. In Windows, the program launches a command-line window, which
ht be familiar with if you have ever done any programming. Then it opens the
 inside your default browser—here Google Chrome. Note that the address that
 is pointed to is http://127.0.0.1:3333, which refers to your machine. In other

he browser is working locally, not over the Internet.

                               ny Server haund to 712

                                                  ps 77” Son

                      xefine } GET rennana/t ere /ge eysion (18ms

penRefine.

Refine command-line window. OpenRefine opens this window upon startup on Windows machines.

```

```
       > Google Refine
   2th al a

       Gor gle TEFING A osertoo! or working with mensy ost.
                               syne snt NN sso RSE RNA HOH RENAE EAA SSP EES MRED LITE IE ENMMEE

                      Create 9 project by importing data, What kinds of data files con | import?

                         TSV. CSV, "SV, Excel {xls and xlsx}, JSON, XML. ROF as XML, and Google Data documents are all supported. Susgumt for other formats can
                        be added with Google Refine extensions.
          Import Project
                      Get data from Locate one or more files on your computer to upload

                                        - This Computer

                     Web Addresses (URLs) Next»

                                                    2 Cliproard

                      Google Osta

Source: OpenRefine.

Note: OpenRefine create project screen.

  Let’s create a project in Refine, so we can clean the data. Click Create Project | Get
from | This Computer and find the mo12contribs.xlsx file. Click Next and Refine tak
to the next step for loading the file.
 Change the project name to “Campaign contributions” and make sure that the o
to parse next line as column header at the bottom is checked. This tells Refine to use th
row from the Excel file as column headers. Note that the top of the screen previews our

        Spe Google Ratine
        @ 2 © 31270013

                       KENNETH Wi WILSON:

                           412481 C11444 COZENS KEHNETH FOR P¢ WILSON Dart Valley 107 Wright Ror

                         12652 119194 KENNETH CINZEMS FOR YW 77LBON. Chisiana Suny AG? Ae Shannon

                        412483 C114794 CERZENS KERWETH FOR 8 HILOLNG Cheries = Hitchbor

            _” hss Parse data as
              | _ | Open kee Excel Document {xlsx} files Farnat seeadsheete Warksheots ore ! mot2emall to re% 19667 me Ze firgt rgnae ae fe 6 ning W, Wl x7 Store Store ae wank ada bank roms cots as nulis
          i) Wpase 1 in each row
             ROR AML fles next tines} as
                                 E column

                © Fixed-width fisld text files en dat .

                PC Axia test fen MOS rowis} of

Source: OpenRefine.
                                                 traders
                                    5 Line-besed text files 2 Discard 0
              | CSV/ TEV / separator tases fhes row(s} of
            SU Bes

                                                   intial

```

```
ign contributions x

 Filter Undo / Rado s
k Create project and Refine loads the data. By default, it shows only 10 rows at a time.
 change that ifyou like. Working with data in Refine typically takes two steps: detecta problems, then correcting them. One of the most common ways to detect the flaws
eating Facets, or views of your data that are very much like spreadsheet pivot tables.

```

```
 g facets and filters \
 facets and filters to select subsets
 r data to act on. Choase facet and
 methods from the menus at the top : fe Hat
 ch data column

 ure how to get started? R °-42482
 h these screencasts
                          4 112462

                                  S. 192658.

                              W285?

                                TW24SS

                                 442489

                            TZ850

Missouri Ethics Commission.

```

```
    COZENS FOR ‘ Bis
    RENNETH We
      WESON
CHiti94 CTZENS WENNETH FOR WY ur Darr
C111194  CMBENS WLSON FOR
      NENMETH W
      VALSON

Cis CIRZENS FOR
      KENNETH W
Citige OMENS WRSON FOR
     KENNETH ¥¢
CHHN194 WESOK COZENS FOR
      RERNETH
      swison
Ciitige CHRENS KERHETS FOR, WY
    ¥eLSON

Crise CRZENS FOR,
      KENNETH
      WASON

CIti184 CUAZENS FOR
      KENNETH WESOR 2

Cities COZENS FOR
      KENNETH YY
      WLSON

```

```
107 Winight
Vasiey Rd

Axe 407 Shannon

PBS Commertial

PE Bax 914

Det NE 18206
a

11S RVdoter S

18808 Ein St

225 BK Hwy

456 4 St

```

```
nRefine project screen, data successfully loaded.

te a Facet for the City column

king on its drop-down arrow,
lecting Facet | Text facet from
u. Scroll down the results and
 see, for example, that the city
uis (proper spelling) has been

```

```
ti hee Lise ee WS

```

```
1605 choices So

St Loui 2

st louis +7

ST Louis 1

```

```
by. name count

```

```
led many different ways. We
lick on the edit line for each
ling and manually change the
es to our proper spelling, but
uld take a whole lot of time.

tely, Refine has some powers that will allow us to clean up
isspelled city names en masse.
’s where Clustering can help.
ing uses algorithms designed
t text values that might be the

```

```
 ‘ST LOUIS 118

  St LOuis 2
  St Louis +33:
  St LOUIS +
  St louis 10
  st Louis 2

  St Lougs 1
  St Lous 4

   PP Bon

Source: Missouri Ethics Commission.

Note: Text facet for City column. Note that the results are very similar t
those created by an Excel pivot table.

```

```
              x Clty WS: > AIO © MECID Y Committee Nan’ “¥ Committee ¥ Company
           1605 choices : Sort by: name count Cluster “C000812 “ — Deuoeaane STLOUS COUNTY — Dooley Tea County for St
           SE Lou's = CENTRAL
          SEES : COMMIFTEE
             st fouls

           ST Louis
           ST LOUIS #+
           St LOuis 2
            St Louis #2
            St LOUIS
            St louis <
             st Louis

              St Lowes
            St Lous

                                  Apply Cancel :

                                            TERS Ese

Source: Missouri Ethics Commission.

Note: Manually editing a misspelling.

same. Go ahead and click the Cluster button on the Facet box for City. Refine empl
two methods for clustering—key collision and nearest neighbor. Each of those methods
multiple Keying Functions. By default, Refine clusters by key collision/fingerprint.
details about how these algorithms work, see the documentation at https://github.c
OpenRefine/OpenRefine/wiki/Clustering-In-Depth.
 Using key collision/fingerprint, Refine shows us how it has clustered city nam
including many St. Louis variants at the top of the list. Let’s look closely: Refine says

Cluster Size is 13, or that it found 13 different values for clustering here. The Row Coun
2,457. Under Values in Cluster, we see the 13 different spellings. Merge? asks whether
want to transform these values into something else. We do, so check this box. In
New Cell Value box, enter our proper spelling of St. Louis.

  Cluster & Edit column “City”

   This feature helps you find groups of different cell values that might be alternative representations of the same thing. For example, the two strings “New York" and “ne
   york” are very likely to refer to the same concept and just have capitalization differences, and “Gadel” and “Godel” probably refer to the same person. Find out more

  Method | key collision iD ie) 289 clusters fo

  Cluster Size RowCount ValuesinCluster == i asti<i«<S ew | "+. # Choices in Cluster

```

```
13 D457 + St Louis
                   * Bt Louis
                    « SF LOUIS

               St louis
                St Luis
                 st Louis
              ST LOUIS
               ST Louis (
               St Lows
                St Louis
             SELOUIS ©5 rx

```

```
St Louis

```

```
          © uss SE

_ # Rows in Cluster
q
|

        Bm 2800

 Average Length of Choices

```