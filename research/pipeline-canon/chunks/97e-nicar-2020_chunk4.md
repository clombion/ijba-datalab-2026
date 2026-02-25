<!-- chunk: 4/4 | source: 97e-nicar-2020.md | words: 34554 -->
<!-- headings: How to sort rows; How to filter rows; Filtering selected rows with `"`; Filtering via frequency tables; Using frequency tables to select (and filter) for multiple values; Frequency tables; Multi-column frequencies; Adding \"aggregators\"; One-off calculations; Summarizing all columns; Basic column attributes; How to view all columns and their attributes; How to set column types; How to rename columns; How to expand, shrink, and remove columns; How to move columns\' positions; How to designate \"key\" columns; Manipulating columns from the Columns Sheet; Selecting and Unselecting Rows; One row at a time -->

## How to sort rows

The keys `[` and `]` sort rows in ascending and descending order, respectively.

For instance, you could do the following with the FAA dataset:

- Navigate to the `COST_REPAIRS` column
- Press `#` (if you haven\'t already) to tell VisiData it\'s a numeric column
- Press `]` to sort the column in descending order --- i.e., from highest to lowest

After that, you should see something like the following:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
<HEIGHT │ SPEED │ SPECIES            │ BIRDS_STRUCK │ EFFECT             │ DAMAGE │↓COST_REPAIRS#│>
 0      │ 143   │ Red-tailed hawk    │ 1            │ Engine Shut Down   │ S      │      6500000 │A
 25     │       │ Gadwall            │ 2-10         │ Precautionary Land…│ S      │      5818528 │A
        │       │ Mallard            │ 1            │ None               │ S      │      5548924 │A
 0      │       │ Gray partridge     │ 2-10         │ Precautionary Land…│ S      │      5427992 │A
 5000   │       │ American white pel…│ 2-10         │ Engine Shut Down   │ S      │      5111000 │
 250    │ 150   │ American coot      │ 1            │ Engine Shut Down   │ S      │      5000000 │A
 972    │ 180   │ Northern pintail   │ 2-10         │ Engine Shut Down   │ S      │      5000000 │A
 0      │ 96    │ Red-tailed hawk    │ 2-10         │ Engine Shut Down   │ S      │      4600279 │A
 10     │ 160   │ Bald eagle         │ 1            │ Precautionary Land…│ S      │      4500000 │
 400    │ 170   │ Canada goose       │ 2-10         │ Precautionary Land…│ S      │      3909837 │A
 10     │ 130   │ Rock pigeon        │ 11-100       │ Precautionary Land…│ S      │      3250000 │P
 2000   │ 230   │ Greater white-fron…│ 2-10         │ Precautionary Land…│ S      │      3228053 │A
 90     │ 141   │ Mallard            │ 2-10         │ Precautionary Land…│ S      │      3000000 │A
 0      │ 120   │ Bald eagle         │ 1            │ Engine Shut Down   │ S      │      2900000 │A
 8500   │       │ Snow goose         │ 11-100       │ Precautionary Land…│ S      │      2737462 │A
 0      │       │ Red-tailed hawk    │ 1            │ Precautionary Land…│ S      │      2300000 │A
 1200   │ 190   │ Turkey vulture     │ 2-10         │ Precautionary Land…│ S      │      2000000 │A
 400    │ 160   │ Unknown bird - med…│ 1            │ Engine Shut Down   │ S      │      2000000 │P
 2000   │ 220   │ Black vulture      │ 1            │ Engine Shut Down   │ S      │      2000000 │A
        │       │ Brown thrasher     │ 1            │ None               │ M      │      2000000 │A
 1000   │ 140   │ Great black-backed…│ 1            │                    │ S      │      1529013 │A
1› faa-wildlife-strikes|                                             ]   sort-desc      73448 rows 
</pre>


:::: tip
::: title
Tip

You can sort on multiple columns at once by \"key\"-ing those columns (via `!`) and then typing either `g[` (ascending) or `g]` (descending).


## How to filter rows

VisiData provides several ways to filter your datasets:

- Row selection + `"`
- Frequency tables + `Enter`
- Frequency tables + row selection + `g` + `Enter`

The sections below walk you through each approach.

### Filtering selected rows with `"`

In VisiData, pressing `"` will create a copy of your current sheet --- but one that contains only **selected** rows.

So, to view only wildlife strikes that involved hawks, you could do the following:

- Navigate to the `SPECIES` column
- Press `|` to select by searching, then type `hawk`, and then press `Enter`

At this point, you should see something like the following:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
<STATE │ AIRPORT            │ PHASE_OF_FLT │ HEIGHT │ SPEED │ SPECIES            │ BIRDS_STRUCK │ >
 FL    │ VERO BEACH MUNICIP…│ APPROACH     │        │       │ Unknown bird       │ 1            │ N 
 AK    │ KENAI MUNICIPAL AR…│ APPROACH     │        │       │ Unknown bird       │ 1            │ N 
 TX    │ DAVID WAYNE HOOKS …│              │        │       │ Unknown bird       │ 1            │ N 
 MO    │ LAMBERT-ST LOUIS I…│ APPROACH     │        │       │ Unknown bird       │ 1            │ N 
 FL    │ POMPANO BEACH AIRP…│ LANDING ROLL │ 0      │       │ Unknown bird       │ 1            │   
 VI    │ HENRY E ROHLSEN AR…│              │        │       │ Unknown bird       │ 1            │ O 
 TX    │ SAN ANTONIO INTL   │ APPROACH     │        │       │ Unknown bird       │ 1            │ N 
 TX    │ LONE STAR EXECUTIV…│ DEPARTURE    │        │       │ Unknown bird       │ 1            │ P 
 FL    │ TAMPA INTL         │ APPROACH     │ 6000   │       │ Unknown bird       │ 1            │ N 
 MO    │ LAMBERT-ST LOUIS I…│ APPROACH     │        │       │ Owls               │ 1            │ N 
•FL    │ OPA-LOCKA EXECUTIV…│ APPROACH     │        │       │ Hawks              │ 1            │ N 
 CA    │ NORMAN Y. MINETA S…│              │        │       │ Gulls              │ 1            │ N 
 FL    │ FORT LAUDERDALE/HO…│ APPROACH     │ 1500   │       │ Unknown bird - sma…│ 1            │ N 
 AR    │ FORT SMITH REGIONA…│ CLIMB        │        │       │ Unknown bird - sma…│ 1            │ N 
 AR    │ BILL AND  HILLARY …│ LANDING ROLL │ 0      │       │ Unknown bird - sma…│ 1            │ N 
       │ UNKNOWN            │ En Route     │        │       │ Unknown bird       │ 1            │ P 
 CA    │ METRO OAKLAND INTL │              │        │  ┌─────────────────────────────| statuses |─┐ 
 UT    │ SALT LAKE CITY INTL│              │        │  │ search wrapped                           │ 
 TX    │ GEORGE BUSH INTERC…│ CLIMB        │        │  │ 2164 matches for /hawk/                  │ 
 FL    │ ORLANDO SANFORD IN…│ APPROACH     │        │  │ selected 2164 rows                       │ 
 IL    │ CHICAGO O'HARE INT…│ CLIMB        │ 12000  │  └──────────────────────────────────────────┘ 
1› faa-wildlife-strikes|                               |   select-col-regex      73448 rows  •2164 
</pre>


Then, press `"`, which should give you something like the following:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
<STATE │ AIRPORT            │ PHASE_OF_FLT │ HEIGHT │ SPEED │ SPECIES            │ BIRDS_STRUCK │ >
 FL    │ OPA-LOCKA EXECUTIV…│ APPROACH     │        │       │ Hawks              │ 1            │ N 
 TX    │ GEORGE BUSH INTERC…│              │        │       │ Red-tailed hawk    │ 1            │   
 CO    │ DENVER INTL AIRPORT│ Landing Roll │ 0      │       │ Ferruginous hawk   │ 1            │   
 PR    │ LUIS MUNOZ MARIN I…│ Landing Roll │ 0      │       │ Hawks              │ 1            │ N 
 GA    │ DEKALB-PEACHTREE A…│ APPROACH     │        │       │ Hawks              │ 1            │ N 
 OK    │ RICHARD LLOYD JONE…│ APPROACH     │        │       │ Hawks              │ 1            │ N 
 AR    │ NW ARKANSAS REGION…│ DEPARTURE    │        │       │ Hawks              │ 1            │ N 
 TX    │ AUSTIN-BERGSTROM I…│ APPROACH     │        │       │ Hawks              │ 2-10         │ N 
 IL    │ QUAD CITY ARPT     │ APPROACH     │        │       │ Red-tailed hawk    │ 1            │ N 
 MO    │ LAMBERT-ST LOUIS I…│ APPROACH     │ 100    │       │ Hawks              │ 1            │ N 
       │ UNKNOWN            │ En Route     │ 500    │ 50    │ Hawks              │ 1            │ P 
 KY    │ LOUISVILLE INTL AR…│              │        │       │ Red-tailed hawk    │ 1            │   
 MO    │ KANSAS CITY INTL   │              │        │       │ Red-tailed hawk    │ 1            │   
 NY    │ JOHN F KENNEDY INTL│ Climb        │ 20     │ 155   │ Red-tailed hawk    │ 1            │ N 
 UT    │ SALT LAKE CITY INTL│ Approach     │ 75     │ 140   │ Rough-legged hawk  │ 1            │ N 
 BC    │ VANCOUVER INTL     │ Take-off run │ 0      │       │ Rough-legged hawk  │ 1            │ N 
 MD    │ BALTIMORE/WASH INT…│ Climb        │ 100    │       │ Red-tailed hawk    │ 1            │ N 
 FL    │ GAINESVILLE REG AR…│              │        │       │ Common nighthawk   │ 1            │   
 CA    │ LONG BEACH-DAUGH F…│ Landing Roll │ 0      │       │ Red-tailed hawk    │ 1            │ N 
 MD    │ BALTIMORE/WASH INT…│ Take-off run │ 0      │ 140   │ Hawks              │ 1            │ N 
 IL    │ CHICAGO O'HARE INT…│              │        │       │ Red-tailed hawk    │ 1            │   
2› faa-wildlife-strikes_selectedref|                                          "          2164 rows 
</pre>


### Filtering via frequency tables

From any row in any frequency table, you can press `Enter` to create a new dataset containing only the rows that match that value.

For instance, to view only the wildlife strikes that occurred in California, we might do the following from the main data sheet:

- Navigate to the `STATE` column
- Press `Shift-F` to create the frequency table
- Navigate down two rows, to the row for `CA`

At which point, you should see something like this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 STATE ║↓count♯│ percent%│ histogram                             ~║                                
       ║  9840 │   13.40 │ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ║
 TX    ║  7309 │    9.95 │ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■           ║
 CA    ║  5270 │    7.18 │ ■■■■■■■■■■■■■■■■■■■■                   ║
 FL    ║  4902 │    6.67 │ ■■■■■■■■■■■■■■■■■■                     ║
 CO    ║  3523 │    4.80 │ ■■■■■■■■■■■■■                          ║
 NY    ║  3434 │    4.68 │ ■■■■■■■■■■■■■                          ║
 IL    ║  3020 │    4.11 │ ■■■■■■■■■■■                            ║
 PA    ║  2475 │    3.37 │ ■■■■■■■■■                              ║
 TN    ║  2116 │    2.88 │ ■■■■■■■■                               ║
 NJ    ║  2085 │    2.84 │ ■■■■■■■■                               ║
 OH    ║  1914 │    2.61 │ ■■■■■■■                                ║
 MO    ║  1633 │    2.22 │ ■■■■■■                                 ║
 NC    ║  1620 │    2.21 │ ■■■■■■                                 ║
 KY    ║  1548 │    2.11 │ ■■■■■                                  ║
 MI    ║  1532 │    2.09 │ ■■■■■                                  ║
 GA    ║  1247 │    1.70 │ ■■■■                                   ║
 UT    ║  1225 │    1.67 │ ■■■■                                   ║
 LA    ║  1182 │    1.61 │ ■■■■                                   ║
 IN    ║  1174 │    1.60 │ ■■■■                                   ║
 WA    ║  1089 │    1.48 │ ■■■■                                   ║
 HI    ║  1052 │    1.43 │ ■■■■                                   ║
3› faa-wildlife-strikes_STATE_freq|                                    j   go-down         63 bins 
</pre>


From there, pressing `Enter` should create the filtered sheet we wanted:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
<STATE │ AIRPORT            │ PHASE_OF_FLT │ HEIGHT │ SPEED │ SPECIES            │ BIRDS_STRUCK │ >
 CA    │ NORMAN Y. MINETA S…│              │        │       │ Gulls              │ 1            │ N
 CA    │ METRO OAKLAND INTL │              │        │       │ Unknown bird       │ 1            │ N
 CA    │ LOS ANGELES INTL   │ CLIMB        │        │       │ Unknown bird       │ 1            │ P
 CA    │ LONG BEACH-DAUGH F…│ LANDING ROLL │ 0      │       │ Unknown bird       │ 1            │ N
 CA    │ NAPA COUNTY ARPT   │ LANDING ROLL │ 0      │       │ Unknown bird       │ 1            │ N
 CA    │ HAYWARD EXECUTIVE …│ Climb        │        │       │ Unknown bird - sma…│ 1            │ P
 CA    │ ONTARIO INTL ARPT  │              │        │       │ Owls               │ 1            │ N
 CA    │ LOS ANGELES INTL   │ APPROACH     │        │       │ Unknown bird       │ 1            │ N
 CA    │ LIVERMORE MUNICIPA…│ TAKE-OFF RUN │ 0      │       │ Unknown bird       │ 2-10         │ N
 CA    │ WHITEMAN AIRPORT   │ LANDING ROLL │ 0      │       │ Rock pigeon        │ 1            │ N
 CA    │ LIVERMORE MUNICIPA…│ APPROACH     │        │       │ Unknown bird       │ 1            │ N
 CA    │ JOHN WAYNE-ORANGE …│ APPROACH     │ 1700   │       │ Unknown bird - med…│ 1            │ N
 CA    │ CHINO AIRPORT      │              │        │       │ Unknown bird       │ 1            │ N
 CA    │ SAN FRANCISCO INTL…│ LANDING ROLL │ 0      │       │ Unknown bird       │ 1            │ N
 CA    │ SACRAMENTO INTL    │ APPROACH     │        │       │ Unknown bird       │ 1            │ N
 CA    │ SANTA MONICA MUNIC…│ APPROACH     │ 60     │       │ Unknown bird       │ 1            │ N
 CA    │ SACRAMENTO INTL    │              │        │       │ Unknown bird       │ 1            │ N
 CA    │ SACRAMENTO INTL    │ Climb        │ 1500   │ 210   │ Northern pintail   │ 2-10         │ P
 CA    │ LOS ANGELES INTL   │ Approach     │ 900    │ 135   │ Unknown bird - med…│ 1            │ N
 CA    │ SAN FRANCISCO INTL…│ Landing Roll │ 0      │ 90    │ Black-tailed jackr…│ 1            │ N
 CA    │ SACRAMENTO INTL    │ Approach     │ 1000   │ 135   │ Northern pintail   │ 1            │ N
4› faa-wildlife-strikes_CA|                                               Enter          5270 rows 
</pre>


### Using frequency tables to select (and filter) for multiple values

The approach above is great if you want to drill down on rows where a field equals one particular value. But what if you want to include a few different values? Select the rows of the frequency table you want to include, then press `g` + `Enter`.

Here\'s a practical example, using the FAA dataset. Let\'s say you want to filter for wildlife strikes at the five airports with the most reported incidents. To achieve that, you could take these steps:

- On the main data sheet navigate to the `AIRPORT` column, and press `Shift-F` to create a frequency table:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 AIRPORT            ║↓count♯│ percent%│ histogram                             ~║                   
 UNKNOWN            ║  8424 │   11.47 │ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ║
 DENVER INTL AIRPORT║  2756 │    3.75 │ ■■■■■■■■■■■■                           ║
 DALLAS/FORT WORTH …║  2392 │    3.26 │ ■■■■■■■■■■                             ║
 CHICAGO O'HARE INT…║  1583 │    2.16 │ ■■■■■■■                                ║
 JOHN F KENNEDY INTL║  1302 │    1.77 │ ■■■■■                                  ║
 MEMPHIS INTL       ║  1217 │    1.66 │ ■■■■■                                  ║
 SALT LAKE CITY INTL║  1179 │    1.61 │ ■■■■■                                  ║
 PHILADELPHIA INTL  ║  1131 │    1.54 │ ■■■■■                                  ║
 ORLANDO INTL       ║  1026 │    1.40 │ ■■■■                                   ║
 SACRAMENTO INTL    ║  1021 │    1.39 │ ■■■■                                   ║
 LA GUARDIA ARPT    ║   974 │    1.33 │ ■■■■                                   ║
 CHARLOTTE/DOUGLAS …║   960 │    1.31 │ ■■■■                                   ║
 NEWARK LIBERTY INT…║   917 │    1.25 │ ■■■■                                   ║
 LOUISVILLE INTL AR…║   841 │    1.15 │ ■■■                                    ║
 AUSTIN-BERGSTROM I…║   817 │    1.11 │ ■■■                                    ║
 LOUIE ARMSTRONG NE…║   809 │    1.10 │ ■■■                                    ║
 KANSAS CITY INTL   ║   807 │    1.10 │ ■■■                                    ║
 HARTSFIELD - JACKS…║   775 │    1.06 │ ■■■                                    ║
 GEORGE BUSH INTERC…║   746 │    1.02 │ ■■■                                    ║
 DETROIT METRO WAYN…║   734 │    1.00 │ ■■■                                    ║
 BALTIMORE/WASH INT…║   691 │    0.94 │ ■■■                                    ║
5› faa-wildlife-strikes_AIRPORT_freq|                       processing… Shift+F          1512 bins 
</pre>


- Then, select the top five entries (skipping `UNKNOWN`) using `s`:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 AIRPORT            ║↓count♯│ percent%│ histogram                             ~║                   
 UNKNOWN            ║  8424 │   11.47 │ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ║
•DENVER INTL AIRPORT║  2756 │    3.75 │ ■■■■■■■■■■■■                           ║
•DALLAS/FORT WORTH …║  2392 │    3.26 │ ■■■■■■■■■■                             ║
•CHICAGO O'HARE INT…║  1583 │    2.16 │ ■■■■■■■                                ║
•JOHN F KENNEDY INTL║  1302 │    1.77 │ ■■■■■                                  ║
•MEMPHIS INTL       ║  1217 │    1.66 │ ■■■■■                                  ║
 SALT LAKE CITY INTL║  1179 │    1.61 │ ■■■■■                                  ║
 PHILADELPHIA INTL  ║  1131 │    1.54 │ ■■■■■                                  ║
 ORLANDO INTL       ║  1026 │    1.40 │ ■■■■                                   ║
 SACRAMENTO INTL    ║  1021 │    1.39 │ ■■■■                                   ║
 LA GUARDIA ARPT    ║   974 │    1.33 │ ■■■■                                   ║
 CHARLOTTE/DOUGLAS …║   960 │    1.31 │ ■■■■                                   ║
 NEWARK LIBERTY INT…║   917 │    1.25 │ ■■■■                                   ║
 LOUISVILLE INTL AR…║   841 │    1.15 │ ■■■                                    ║
 AUSTIN-BERGSTROM I…║   817 │    1.11 │ ■■■                                    ║
 LOUIE ARMSTRONG NE…║   809 │    1.10 │ ■■■                                    ║
 KANSAS CITY INTL   ║   807 │    1.10 │ ■■■                                    ║
 HARTSFIELD - JACKS…║   775 │    1.06 │ ■■■                                    ║
 GEORGE BUSH INTERC…║   746 │    1.02 │ ■■■            ┌─────────────────────────────| statuses |─┐
 DETROIT METRO WAYN…║   734 │    1.00 │ ■■■            │ selected 1217 more rows                  │
 BALTIMORE/WASH INT…║   691 │    0.94 │ ■■■            └──────────────────────────────────────────┘
5› faa-wildlife-strikes_AIRPORT_freq|                           s   select-row       1512 bins  •5 
</pre>


- Next, press `g` + `Enter`. The result should look like this, with 9,250 rows (the total of those five airports):


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
<STATE │ AIRPORT            │ PHASE_OF_FLT │ HEIGHT │ SPEED │ SPECIES            │ BIRDS_STRUCK │ >
 CO    │ DENVER INTL AIRPORT│ LANDING ROLL │ 0      │       │ Unknown bird       │ 1            │ N
 CO    │ DENVER INTL AIRPORT│ Approach     │        │       │ Unknown bird       │ 1            │ N
 CO    │ DENVER INTL AIRPORT│ LANDING ROLL │ 0      │       │ Unknown bird       │ 1            │ N
 CO    │ DENVER INTL AIRPORT│ DEPARTURE    │        │       │ Unknown bird - sma…│ 1            │ N
 CO    │ DENVER INTL AIRPORT│ Landing Roll │ 0      │       │ Ferruginous hawk   │ 1            │
 CO    │ DENVER INTL AIRPORT│ DEPARTURE    │        │       │ Unknown bird - sma…│ 1            │ N
 CO    │ DENVER INTL AIRPORT│ LANDING ROLL │ 0      │       │ Unknown bird - sma…│ 2-10         │ N
 CO    │ DENVER INTL AIRPORT│ APPROACH     │        │       │ Unknown bird       │ 1            │ N
 CO    │ DENVER INTL AIRPORT│              │        │       │ Northern harrier   │ 1            │
 CO    │ DENVER INTL AIRPORT│ Take-off run │ 0      │       │ Unknown bird - med…│ 1            │
 CO    │ DENVER INTL AIRPORT│              │        │       │ Great horned owl   │ 1            │
 CO    │ DENVER INTL AIRPORT│              │        │       │ Short-eared owl    │ 1            │
 CO    │ DENVER INTL AIRPORT│ Approach     │        │       │ Horned lark        │ 1            │
 CO    │ DENVER INTL AIRPORT│              │        │       │ Horned lark        │ 1            │
 CO    │ DENVER INTL AIRPORT│ Climb        │ 500    │ 150   │ Unknown bird - sma…│ 1            │ N
 CO    │ DENVER INTL AIRPORT│              │        │       │ Western meadowlark │ 1            │
 CO    │ DENVER INTL AIRPORT│              │        │       │ Western meadowlark │ 2-10         │
 CO    │ DENVER INTL AIRPORT│ Landing Roll │ 0      │       │ Mourning dove      │ 1            │
 CO    │ DENVER INTL AIRPORT│ Take-off run │ 0      │ 145   │ Unknown bird - sma…│ 1            │ N
 CO    │ DENVER INTL AIRPORT│              │        │       │ Red-tailed hawk    │ 1            │  
 CO    │ DENVER INTL AIRPORT│              │        │       │ Horned lark        │ 1            │  
6› faa-wildlife-strikes_several|                                         gEnter          9250 rows 
</pre>




## Frequency tables

Frequency tables are dead-simple, but also quite powerful. For the dead-simple usage: Navigate to any column, and then press `Shift-F`. If you did that on the first column (\"OPERATOR\") of the FAA dataset, you should get something like this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 OPERATOR           ║↓count♯│ percent%│ histogram                             ~║                   
 UNKNOWN            ║ 23076 │   31.42 │ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ║
 SOUTHWEST AIRLINES ║  7752 │   10.55 │ ■■■■■■■■■■■■                           ║
 BUSINESS           ║  5868 │    7.99 │ ■■■■■■■■■                              ║
 AMERICAN AIRLINES  ║  4337 │    5.90 │ ■■■■■■■                                ║
 DELTA AIR LINES    ║  2817 │    3.84 │ ■■■■                                   ║
 FEDEX EXPRESS      ║  2709 │    3.69 │ ■■■■                                   ║
 UNITED AIRLINES    ║  2194 │    2.99 │ ■■■                                    ║
 US AIRWAYS         ║  1885 │    2.57 │ ■■■                                    ║
 UPS AIRLINES       ║  1773 │    2.41 │ ■■                                     ║
 SKYWEST AIRLINES   ║  1769 │    2.41 │ ■■                                     ║
 JETBLUE AIRWAYS    ║  1740 │    2.37 │ ■■                                     ║
 EXPRESSJET AIRLINES║  1347 │    1.83 │ ■■                                     ║
 AMERICAN EAGLE AIR…║  1041 │    1.42 │ ■                                      ║
 ENVOY AIR          ║   883 │    1.20 │ ■                                      ║
 ALASKA AIRLINES    ║   835 │    1.14 │ ■                                      ║
 REPUBLIC AIRLINES  ║   804 │    1.09 │ ■                                      ║
 MESA AIRLINES      ║   693 │    0.94 │ ■                                      ║
 AIR WISCONSIN AIRL…║   623 │    0.85 │ ■                                      ║
 PSA AIRLINES       ║   577 │    0.79 │                                        ║
 PRIVATELY OWNED    ║   516 │    0.70 │                                        ║
 PHI INC            ║   491 │    0.67 │                                        ║
2› faa-wildlife-strikes_OPERATOR_freq|                                  Shift+F           282 bins 
</pre>


With just one keystroke, VisiData has already told us something useful about the dataset: That the \"operators\" associated with 31% of the wildlife strikes are, according to the FAA, \"unknown.\" We have also learned, from the \"bins\" mini-report at the bottom-right of the screen, that there are 282 distinct values in the \"OPERATOR\" column.

### Multi-column frequencies

Sometimes you want to count how often **combinations** of columns occur. VisiData also makes this easy. First, turn the columns you want to count into \"key\" columns, using the `!` button. Then, type `gF`.

For instance, if we wanted to count the combinations of the \"OPERATOR\" and \"PERSON\" fields, we\'d hit `!` on each of those columns --- either from the main data sheet or in the Columns Sheet. Once you\'ve done that, you should see something like this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 OPERATOR           │ PERSON ║<BIRDS_STRUCK │ EFFECT             │ DAMAGE │ COST_REPAIRS │ REMAINS>
 BUSINESS           │ Tower  ║ 1            │ NONE               │ M      │              │ 0        
 BUSINESS           │ Tower  ║ 1            │ NONE               │ M      │              │ 0        
 BUSINESS           │ Tower  ║ 1            │ NONE               │ M      │              │ 0        
 DELTA AIR LINES    │ Tower  ║ 1            │ NONE               │ M      │              │ 0        
 BUSINESS           │ Tower  ║ 1            │                    │ M      │              │ 0        
 DELTA AIR LINES    │ Tower  ║ 1            │ Other              │ M?     │              │ 0        
 DELTA AIR LINES    │ Tower  ║ 1            │ NONE               │ M?     │              │ 0        
 BUSINESS           │ Tower  ║ 1            │ PRECAUTIONARY LAND…│ M?     │              │ 0        
 ALLEGIANT AIR      │ Tower  ║ 1            │ NONE               │ M?     │              │ 0        
 TRANS STATES AIRLI…│ Tower  ║ 1            │ NONE               │ M?     │              │ 0        
 BUSINESS           │ Tower  ║ 1            │ NONE               │ M?     │              │ 0        
 GOVERNMENT         │ Tower  ║ 1            │ NONE               │ M?     │              │ 0        
 AMERICAN AIRLINES  │ Tower  ║ 1            │ NONE               │ N      │              │ 0        
 EXPRESSJET AIRLINES│ Tower  ║ 1            │ NONE               │ N      │              │ 0        
 MESA AIRLINES      │ Tower  ║ 1            │ NONE               │ N      │              │ 0        
 BUSINESS           │ Tower  ║ 1            │ PRECAUTIONARY LAND…│ N      │              │ 0        
 DELTA AIR LINES    │ Tower  ║ 1            │ NONE               │ N      │              │ 0        
 DELTA AIR LINES    │ Tower  ║ 1            │ NONE               │ N      │              │ 0        
 LUFTHANSA          │ Tower  ║ 1            │ NONE               │ N      │              │ 0        
 BUSINESS           │ Tower  ║ 1            │ NONE               │ N      │              │ 0        
 SPIRIT AIRLINES    │ Tower  ║ 1            │ PRECAUTIONARY LAND…│ N      │              │ 0        
1› faa-wildlife-strikes|                                               !   key-col      73448 rows 
</pre>


Then, type `gF`, which should result in something like this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 OPERATOR           │ PERSON ║↓count♯│ percent%│ histogram                             ~║          
 UNKNOWN            │ Carcas…║ 22842 │   31.10 │ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ║
 SOUTHWEST AIRLINES │ Pilot  ║  5481 │    7.46 │ ■■■■■■■■■                              ║
 AMERICAN AIRLINES  │ Pilot  ║  2240 │    3.05 │ ■■■                                    ║
 BUSINESS           │ Pilot  ║  2061 │    2.81 │ ■■■                                    ║
 DELTA AIR LINES    │ Airpor…║  1793 │    2.44 │ ■■                                     ║
 BUSINESS           │ Airpor…║  1642 │    2.24 │ ■■                                     ║
 AMERICAN AIRLINES  │ Airpor…║  1481 │    2.02 │ ■■                                     ║
 FEDEX EXPRESS      │ Air Tr…║  1434 │    1.95 │ ■■                                     ║
 UNITED AIRLINES    │ Airpor…║  1351 │    1.84 │ ■■                                     ║
 UPS AIRLINES       │ Air Tr…║  1343 │    1.83 │ ■■                                     ║
 SOUTHWEST AIRLINES │ Airpor…║  1293 │    1.76 │ ■■                                     ║
 BUSINESS           │ Tower  ║  1094 │    1.49 │ ■                                      ║
 SKYWEST AIRLINES   │ Airpor…║  1024 │    1.39 │ ■                                      ║
 FEDEX EXPRESS      │ Pilot  ║   963 │    1.31 │ ■                                      ║
 EXPRESSJET AIRLINES│ Airpor…║   785 │    1.07 │ ■                                      ║
 JETBLUE AIRWAYS    │ Airpor…║   749 │    1.02 │ ■                                      ║
 US AIRWAYS         │ Air Tr…║   672 │    0.91 │ ■                                      ║
 US AIRWAYS         │ Airpor…║   656 │    0.89 │ ■                                      ║
 ALASKA AIRLINES    │ Airpor…║   599 │    0.82 │                                        ║
 DELTA AIR LINES    │ Tower  ║   572 │    0.78 │                                        ║
 AMERICAN EAGLE AIR…│ Pilot  ║   535 │    0.73 │                                        ║
2› faa-wildlife-strikes_OPERATOR-PERSON_freq|              processing… gShift+F           879 bins 
</pre>


To make it easier to read, type `g_`, which will expand the column widths:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 OPERATOR                │ PERSON                   ║↓count♯│ percent%│ histogram                  
 UNKNOWN                 │ Carcass Found            ║ 22842 │   31.10 │ ■■■■■■■■■■■■■■■■■■■■■■■■■■…
 SOUTHWEST AIRLINES      │ Pilot                    ║  5481 │    7.46 │ ■■■■■■■■■        
 AMERICAN AIRLINES       │ Pilot                    ║  2240 │    3.05 │ ■■■              
 BUSINESS                │ Pilot                    ║  2061 │    2.81 │ ■■■              
 DELTA AIR LINES         │ Airport Operations       ║  1793 │    2.44 │ ■■               
 BUSINESS                │ Airport Operations       ║  1642 │    2.24 │ ■■               
 AMERICAN AIRLINES       │ Airport Operations       ║  1481 │    2.02 │ ■■               
 FEDEX EXPRESS           │ Air Transport Operations ║  1434 │    1.95 │ ■■               
 UNITED AIRLINES         │ Airport Operations       ║  1351 │    1.84 │ ■■               
 UPS AIRLINES            │ Air Transport Operations ║  1343 │    1.83 │ ■■               
 SOUTHWEST AIRLINES      │ Airport Operations       ║  1293 │    1.76 │ ■■               
 BUSINESS                │ Tower                    ║  1094 │    1.49 │ ■                
 SKYWEST AIRLINES        │ Airport Operations       ║  1024 │    1.39 │ ■                
 FEDEX EXPRESS           │ Pilot                    ║   963 │    1.31 │ ■                
 EXPRESSJET AIRLINES     │ Airport Operations       ║   785 │    1.07 │ ■                
 JETBLUE AIRWAYS         │ Airport Operations       ║   749 │    1.02 │ ■                
 US AIRWAYS              │ Air Transport Operations ║   672 │    0.91 │ ■                
 US AIRWAYS              │ Airport Operations       ║   656 │    0.89 │ ■                
 ALASKA AIRLINES         │ Airport Operations       ║   599 │    0.82 │                  
 DELTA AIR LINES         │ Tower                    ║   572 │    0.78 │                  
 AMERICAN EAGLE AIRLINES │ Pilot                    ║   535 │    0.73 │                  
2› faa-wildlife-strikes_OPERATOR-PERSON_freq|                 g_   resize-cols-max        879 bins 
</pre>


With just a few more keystrokes, we\'ve learned something else: Virtually all wildlife strikes with \"unknown\" operators were identified based on carcasses found at the airport (rather than reports from pilots, for example).


## Adding \"aggregators\"

By default, frequency tables just count the number of times each value appears. But in VisiData, you can specify additional calculations by setting the column\'s \"aggregators\". (You might remember this field from the Columns Sheet.) In VisiData\'s aggregators include `min`, `max`, `mean`, `median`, `sum`, `distinct`, and others.

To add an aggregator to a column, navigate to that column and press `+`. VisiData will then prompt you to specify *which* aggregator you would like to add. You can type out your desired aggregator, or use `Control-x` to open the interactive chooser and select from a list of options.

For example, let\'s go back to the original FAA data sheet. Let\'s navigate to the \"COST_REPAIRS\" column, and then do the following:

- Press `#` to tell VisiData this is an integer column
- Press `+` to tell VisiData you want to add an aggregator
- At the prompt, type `sum` and then hit `Enter` to add the summation aggregator
- Navigate to the \"AIRPORT\" column, and press `Shift-F`

You should see something like this, with the `sum` calculation now appearing in your frequency table:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 AIRPORT            ║↓count♯│ COST_REPAIRS_sum#║                                                   
 UNKNOWN            ║  8424 │         17931422 ║                                                   
 DENVER INTL AIRPORT║  2756 │          9033148 ║                                                   
 DALLAS/FORT WORTH …║  2392 │           927920 ║                                                   
 CHICAGO O'HARE INT…║  1583 │          1146738 ║                                                   
 JOHN F KENNEDY INTL║  1302 │           310917 ║                                                   
 MEMPHIS INTL       ║  1217 │          4507487 ║                                                   
 SALT LAKE CITY INTL║  1179 │          6031324 ║                                                   
 PHILADELPHIA INTL  ║  1131 │          2213030 ║                                                   
 ORLANDO INTL       ║  1026 │            71500 ║                                                   
 SACRAMENTO INTL    ║  1021 │          3634816 ║                                                   
 LA GUARDIA ARPT    ║   974 │           381504 ║                                                   
 CHARLOTTE/DOUGLAS …║   960 │            86960 ║                                                   
 NEWARK LIBERTY INT…║   917 │           506489 ║                                                   
 LOUISVILLE INTL AR…║   841 │          1366299 ║                                                   
 AUSTIN-BERGSTROM I…║   817 │           545500 ║                                                   
 LOUIE ARMSTRONG NE…║   809 │           406000 ║                                                   
 KANSAS CITY INTL   ║   807 │            75660 ║                                                   
 HARTSFIELD - JACKS…║   775 │           284232 ║                                                   
 GEORGE BUSH INTERC…║   746 │            52000 ║                                                   
 DETROIT METRO WAYN…║   734 │            48983 ║                                                   
 BALTIMORE/WASH INT…║   691 │           339300 ║                                                   
3› faa-wildlife-strikes_AIRPORT_freq|                                   Shift+F          1512 bins 
</pre>


By default, frequency tables are sorted by the \"count\" column, but you can sort them by any other column.

:::: note
::: title
Note

When using aggregators, make sure that you\'ve assigned the proper type (`#` for integer columns, etc.) to the columns of interest, so that VisiData knows how to calculate the aggregations correctly.



## One-off calculations

From any data sheet, you can also run a single calculation on all rows --- or all selected rows --- in a column. To do that, navigate to the column and type `z+`, which will bring up the same aggregator-choice prompt as above. Type the aggregator you want, and press `Enter`. At the bottom of the screen, you\'ll see the result of the calculation.

You can try this on the FAA data sheet we\'ve been working with. Navigate to the \"COST_REPAIRS\" column, and then do the following:

- Press `#` to tell VisiData this is an integer column (if you haven\'t already)
- Type `z+` to see the result of an aggregator
- Type `sum` and then hit `Enter`

At the bottom of the screen, you should see something like this, indicating that the total *reported* cost of repairs is \$161,868,071:


<pre>
 DELTA AIR LINES    │ Tower  ║ 1            │ NONE               │ N      │             !│ 0       
 LUFTHANSA          │ Tower  ║ 1            │ NONE     ┌─────────────────────────────| statuses |─┐
 BUSINESS           │ Tower  ║ 1            │ NONE     │ COST_REPAIRS_sum=161868071               │
 SPIRIT AIRLINES    │ Tower  ║ 1            │ PRECAUTIO└──────────────────────────────────────────┘
1› faa-wildlife-strikes|                                       z+   memo-aggregate      73448 rows 
</pre>



## Summarizing all columns

To get a bird\'s-eye view of your entire dataset, press `Shift-I`, which will provide summary statistics for each of your columns:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 column            ║ errors  ♯│ nulls   ♯│ distinct♯│ mode    ~│ min     ~│ max     ~│ sum      │ >
 OPERATOR          ║        0 │        0 │      282 │ UNKNOWN  │          │          │          │  
 ATYPE             ║        0 │        0 │      400 │ UNKNOWN  │          │          │          │  
 INCIDENT_DATE     ║        0 │        0 │     2343 │ 10/30/14…│          │          │          │  
 STATE             ║        0 │        0 │       63 │          │          │          │          │  
 AIRPORT           ║        0 │        0 │     1512 │ UNKNOWN  │          │          │          │  
 PHASE_OF_FLT      ║        0 │        0 │       21 │          │          │          │          │  
 HEIGHT            ║        0 │        0 │      319 │          │          │          │          │  
 SPEED             ║        0 │        0 │      225 │          │          │          │          │  
 SPECIES           ║        0 │        0 │      641 │ Unknown …│          │          │          │  
 BIRDS_STRUCK      ║        0 │        0 │        5 │ 1        │          │          │          │  
 EFFECT            ║        0 │        0 │        8 │ None     │          │          │          │  
 DAMAGE            ║        0 │        0 │        6 │ N        │          │          │          │  
 COST_REPAIRS      ║    72145 │        0 │      478 │ 5000     │ 10       │ 6500000  │ 1618680…#│ 1
 PERSON            ║        0 │        0 │        7 │ Carcass …│          │          │          │  
 REMAINS_COLLECTED ║        0 │        0 │        2 │ 1        │          │          │          │  
 REMARKS           ║        0 │        0 │    61240 │          │          │          │          │  


4› faa-wildlife-strikes_describe|                                    Shift+I            16 columns 
</pre>


In VisiData, this is called the \"Describe Sheet\". You\'ll notice that there are only min/max/median/etc. calculations for the columns we\'ve given types --- just the `COST_REPAIRS` column so far. If we go back to the data sheet and tell VisiData that the `HEIGHT`, `SPEED`, and `BIRDS_STRUCK` fields are numbers, too, then pressing `Shift-I` will result in something like this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 column            ║ errors  ♯│ nulls   ♯│ distinct♯│ mode    ~│ min     ~│ max     ~│ sum      │ >
 OPERATOR          ║        0 │        0 │      282 │ UNKNOWN  │          │          │          │  
 ATYPE             ║        0 │        0 │      400 │ UNKNOWN  │          │          │          │  
 INCIDENT_DATE     ║        0 │        0 │     2343 │ 10/30/14…│          │          │          │  
 STATE             ║        0 │        0 │       63 │          │          │          │          │  
 AIRPORT           ║        0 │        0 │     1512 │ UNKNOWN  │          │          │          │  
 PHASE_OF_FLT      ║        0 │        0 │       21 │          │          │          │          │  
 HEIGHT            ║    35629 │        0 │      318 │ 0        │ 0        │ 31300    │ 33937719#│ 5
 SPEED             ║    48384 │        0 │      224 │ 140      │ 0        │ 374      │ 3614411 #│ 1
 SPECIES           ║        0 │        0 │      641 │ Unknown …│          │          │          │  
 BIRDS_STRUCK      ║     7966 │        0 │        1 │ 1        │ 1        │ 1        │ 65482   #│ 1
 EFFECT            ║        0 │        0 │        8 │ None     │          │          │          │  
 DAMAGE            ║        0 │        0 │        6 │ N        │          │          │          │  
 COST_REPAIRS      ║    72145 │        0 │      478 │ 5000     │ 10       │ 6500000  │ 1618680…#│ 1
 PERSON            ║        0 │        0 │        7 │ Carcass …│          │          │          │  
 REMAINS_COLLECTED ║        0 │        0 │        2 │ 1        │          │          │          │  
 REMARKS           ║        0 │        0 │    61240 │          │          │          │          │  


5› faa-wildlife-strikes_describe|                                    Shift+I            16 columns 
</pre>




## Basic column attributes

Every column in VisiData has the following basic properties, all of which can be modified:

- **Name**: Self explanatory.
- **Width**: The number of characters the column occupies on the screen.
- **Type**: The kind of data --- text, integer, float, currency, or date --- that the column will be interpreted as.

We\'ll get to a few other properties later.


## How to view all columns and their attributes

To see all the columns in your dataset, press `Shift-C`. This will open the \"Columns Sheet,\" which lists each column and its attributes. For the FAA dataset we\'ve been using, it should look like this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 name              ║ width#│ type │ fmtstr │ value              │ aggregators ║                    
 OPERATOR          ║    20 │      │        │ BUSINESS           │             ║                     
 ATYPE             ║    14 │      │        │ PA-28              │             ║                     
 INCIDENT_DATE     ║    19 │      │        │ 05/22/15 00:00:00  │             ║                     
 STATE             ║     7 │      │        │ FL                 │             ║                     
 AIRPORT           ║    20 │      │        │ VERO BEACH MUNICIP…│             ║                     
 PHASE_OF_FLT      ║    14 │      │        │ APPROACH           │             ║                     
 HEIGHT            ║      ⌀│      │        │                    │             ║                     
 SPEED             ║      ⌀│      │        │                    │             ║                     
 SPECIES           ║      ⌀│      │        │ Unknown bird       │             ║                     
 BIRDS_STRUCK      ║      ⌀│      │        │ 1                  │             ║                     
 EFFECT            ║      ⌀│      │        │ NONE               │             ║                     
 DAMAGE            ║      ⌀│      │        │ M                  │             ║                     
 COST_REPAIRS      ║      ⌀│      │        │                    │             ║                     
 PERSON            ║      ⌀│      │        │ Tower              │             ║                     
 REMAINS_COLLECTED ║      ⌀│      │        │ 0                  │             ║                     
 REMARKS           ║      ⌀│      │        │ N9240F was right b…│             ║                     


Shift+C› faa-wildlife-strikes_columns|                               Shift+C            16 columns 
</pre>


The Columns Sheet is handy for quickly getting a sense of your dataset\'s structure. You can navigate the sheet as if it were just another dataset. And just like you can do with a standard data sheet, you can leave this column sheet by pressing `q`.

:::: note
::: title
Note

The Columns Sheet is one of several \"metasheets\" in VisiData; the Sheets Sheet from the previous chapter is another example. You\'ll encounter a few other metasheets in this tutorial.



## How to set column types

Rather than guess at your column\'s data types, VisiData assumes that they\'re all plain-old text.

If a column of really is just text, then great.

But if that column is a number or date, and you want to do any math-y operations on your column (e.g., sorting, summing, averaging, et cetera), you\'ll have to specify its type.

To set a column\'s type, navigate over to that column and press one of the following keys:

  Keystroke                           Column type   Examples
  ----------------------------------- ------------- ---------------------------------------------
  `#`   Integer       `0`, `-1`, `5000000`
  `%`   Float         `0.5`, `-3.14`, `23.45557`
  `$`   Currency      `$4.99`, `€20`, `₹ 100 100`
  `@`   Date          `2018-04-06`, `April 6, 2018`, `04/06/2018`
  `~`   Text          *anything!*

When you do so, the corresponding symbol (e.g., `$` for currency) will appear in the column\'s heading.

For instance, here\'s what you should see if you navigate to the wildlife-strike database\'s `HEIGHT` column, and then press `#` to tell VisiData that the height values are integers:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
<STATE │ AIRPORT            │ PHASE_OF_FLT │ HEIGHT#│ SPEED │ SPECIES            │ BIRDS_STRUCK │ >
 FL    │ VERO BEACH MUNICIP…│ APPROACH     │       !│       │ Unknown bird       │ 1            │ N 
 AK    │ KENAI MUNICIPAL AR…│ APPROACH     │       !│       │ Unknown bird       │ 1            │ N 
 TX    │ DAVID WAYNE HOOKS …│              │       !│       │ Unknown bird       │ 1            │ N 
 MO    │ LAMBERT-ST LOUIS I…│ APPROACH     │       !│       │ Unknown bird       │ 1            │ N 
 FL    │ POMPANO BEACH AIRP…│ LANDING ROLL │      0 │       │ Unknown bird       │ 1            │   
 VI    │ HENRY E ROHLSEN AR…│              │       !│       │ Unknown bird       │ 1            │ O 
 TX    │ SAN ANTONIO INTL   │ APPROACH     │       !│       │ Unknown bird       │ 1            │ N 
 TX    │ LONE STAR EXECUTIV…│ DEPARTURE    │       !│       │ Unknown bird       │ 1            │ P 
 FL    │ TAMPA INTL         │ APPROACH     │   6000 │       │ Unknown bird       │ 1            │ N 
 MO    │ LAMBERT-ST LOUIS I…│ APPROACH     │       !│       │ Owls               │ 1            │ N 
 FL    │ OPA-LOCKA EXECUTIV…│ APPROACH     │       !│       │ Hawks              │ 1            │ N 
 CA    │ NORMAN Y. MINETA S…│              │       !│       │ Gulls              │ 1            │ N 
 FL    │ FORT LAUDERDALE/HO…│ APPROACH     │   1500 │       │ Unknown bird - sma…│ 1            │ N 
 AR    │ FORT SMITH REGIONA…│ CLIMB        │       !│       │ Unknown bird - sma…│ 1            │ N 
 AR    │ BILL AND  HILLARY …│ LANDING ROLL │      0 │       │ Unknown bird - sma…│ 1            │ N 
       │ UNKNOWN            │ En Route     │       !│       │ Unknown bird       │ 1            │ P 
 CA    │ METRO OAKLAND INTL │              │       !│       │ Unknown bird       │ 1            │ N 
 UT    │ SALT LAKE CITY INTL│              │       !│       │ Unknown bird       │ 1            │ N 
 TX    │ GEORGE BUSH INTERC…│ CLIMB        │       !│       │ Unknown bird       │ 1            │ N 
 FL    │ ORLANDO SANFORD IN…│ APPROACH     │       !│       │ Unknown bird       │ 1            │ N 
 IL    │ CHICAGO O'HARE INT…│ CLIMB        │  12000 │       │ Unknown bird       │ 1            │ P 
1› faa-wildlife-strikes|                                              #   type-int      73448 rows 
</pre>


:::: note
::: title
Note

As you can see above, if a cell cannot be converted into the type you\'ve assigned it, VisiData will display `!` in the right-side margin of that cell.

To entirely remove a column\'s assigned type, navigate to the column and type `z~`.


## How to rename columns

- Navigate to the column that you want to rename:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 OPERATOR           │ ATYPE        │ INCIDENT_DATE     │ STATE │ AIRPORT            │ PHASE_OF_FLT>
 BUSINESS           │ PA-28        │ 05/22/15 00:00:00 │ FL    │ VERO BEACH MUNICIP…│ APPROACH     │
 BUSINESS           │ BE-1900      │ 06/18/15 00:00:00 │ AK    │ KENAI MUNICIPAL AR…│ APPROACH     │
</pre>


- Press `^`, which enters column-name-editing mode (evident by the underscores and change in background highlighting):


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 OPERATOR           │ATYPE________   INCIDENT_DATE     │ STATE │ AIRPORT            │ PHASE_OF_FLT>
 BUSINESS           │ PA-28        │ 05/22/15 00:00:00 │ FL    │ VERO BEACH MUNICIP…│ APPROACH     │
 BUSINESS           │ BE-1900      │ 06/18/15 00:00:00 │ AK    │ KENAI MUNICIPAL AR…│ APPROACH     │
</pre>


- Then, type what you want the column to be renamed:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 OPERATOR           │Aircraft_____   INCIDENT_DATE     │ STATE │ AIRPORT            │ PHASE_OF_FLT>
 BUSINESS           │ PA-28        │ 05/22/15 00:00:00 │ FL    │ VERO BEACH MUNICIP…│ APPROACH     │
 BUSINESS           │ BE-1900      │ 06/18/15 00:00:00 │ AK    │ KENAI MUNICIPAL AR…│ APPROACH     │
</pre>


- And then press `Enter` to complete the process:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 OPERATOR           │ Aircraft     │ INCIDENT_DATE     │ STATE │ AIRPORT            │ PHASE_OF_FLT>
 BUSINESS           │ PA-28        │ 05/22/15 00:00:00 │ FL    │ VERO BEACH MUNICIP…│ APPROACH     │
 BUSINESS           │ BE-1900      │ 06/18/15 00:00:00 │ AK    │ KENAI MUNICIPAL AR…│ APPROACH     │
</pre>




## How to expand, shrink, and remove columns

When you load a dataset, VisiData will try to choose reasonable widths for your columns. You can adjust them in a few ways:

  Keystroke(s)                               Action
  ------------------------------------------ -------------------------------------------------------------------------
  `_`          Expands the width of **current column** to fit text in all visible rows
  `g_`         Expands the width of **all columns** to fit text in all visible rows
  `z_` + *n*   Sets the current column\'s width to *n* characters
  `-`          Hides the current column by setting its width to `0`
  `gv`         Unhides all columns
  `z-`         Shrinks the current column\'s width in half

:::: note
::: title
Note

**What\'s the deal with \"z\"?**

Much like with `g`, you\'ll notice that many VisiData commands can be prefixed with `z`. The effect is typically to narrow or specify the scope of the action; e.g., `-` hides a column entirely, while `z-` only shrinks it to half-width.


## How to move columns\' positions

Sometimes you want to view a dataset\'s columns in a different order than they appear in the dataset. To do that in VisiData, use the following keystrokes:

  Keystroke(s)                              Action
  ----------------------------------------- ----------------------------------------
  `Shift-H`   Moves column one position to the left
  `Shift-L`   Moves column one position to the right

:::: tip
::: title
Tip

Similarly, you can use `Shift-J` to move a row down one position, and `Shift-K` to move a row up one position.



## How to designate \"key\" columns

For any sheet, you can designate any number of columns as \"key\" columns. They serve two functions:

- They stay **pinned to the left-hand side** of the sheet when you scroll horizontally.
- They get **special treatment** for certain commands, such as when joining sheets. (More on this later.)

To turn a column into a key column (or vice-versa), navigate to that column and press `!`.

For example, say we\'ve navigated to the `AIRPORT` column of the FAA dataset. Pressing `!` will turn this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 OPERATOR           │ Aircraft     │ INCIDENT_DATE     │ STATE │ AIRPORT            │ PHASE_OF_FLT>
 BUSINESS           │ PA-28        │ 05/22/15 00:00:00 │ FL    │ VERO BEACH MUNICIP…│ APPROACH     │
 BUSINESS           │ BE-1900      │ 06/18/15 00:00:00 │ AK    │ KENAI MUNICIPAL AR…│ APPROACH     │
 BUSINESS           │ PA-46 MALIBU │ 09/20/15 00:00:00 │ TX    │ DAVID WAYNE HOOKS …│              │
 DELTA AIR LINES    │ B-717-200    │ 11/07/15 00:00:00 │ MO    │ LAMBERT-ST LOUIS I…│ APPROACH     │
 BUSINESS           │ BE-90 KING   │ 12/17/15 00:00:00 │ FL    │ POMPANO BEACH AIRP…│ LANDING ROLL │
 DELTA AIR LINES    │ B-757        │ 07/17/15 00:00:00 │ VI    │ HENRY E ROHLSEN AR…│              │
 DELTA AIR LINES    │ B-717-200    │ 08/02/15 00:00:00 │ TX    │ SAN ANTONIO INTL   │ APPROACH     │
 BUSINESS           │ C-414        │ 08/03/15 00:00:00 │ TX    │ LONE STAR EXECUTIV…│ DEPARTURE    │
 ALLEGIANT AIR      │ MD-80        │ 09/02/15 00:00:00 │ FL    │ TAMPA INTL         │ APPROACH     │
 TRANS STATES AIRLI…│ EMB-145      │ 09/07/15 00:00:00 │ MO    │ LAMBERT-ST LOUIS I…│ APPROACH     │
 BUSINESS           │ C-172        │ 11/28/15 00:00:00 │ FL    │ OPA-LOCKA EXECUTIV…│ APPROACH     │
 GOVERNMENT         │ EC120        │ 12/08/15 00:00:00 │ CA    │ NORMAN Y. MINETA S…│              │
 AMERICAN AIRLINES  │ A-321        │ 05/06/15 00:00:00 │ FL    │ FORT LAUDERDALE/HO…│ APPROACH     │
 EXPRESSJET AIRLINES│ CRJ100/200   │ 05/06/15 00:00:00 │ AR    │ FORT SMITH REGIONA…│ CLIMB        │
 MESA AIRLINES      │ CRJ900       │ 05/08/15 00:00:00 │ AR    │ BILL AND  HILLARY …│ LANDING ROLL │
 BUSINESS           │ HELICOPTER   │ 05/06/15 00:00:00 │       │ UNKNOWN            │ En Route     │
 DELTA AIR LINES    │ A-320        │ 05/07/15 00:00:00 │ CA    │ METRO OAKLAND INTL │              │
 DELTA AIR LINES    │ A-320        │ 05/08/15 00:00:00 │ UT    │ SALT LAKE CITY INTL│              │
 LUFTHANSA          │ A-380        │ 05/10/15 00:00:00 │ TX    │ GEORGE BUSH INTERC…│ CLIMB        │
 BUSINESS           │ C-172        │ 05/08/15 00:00:00 │ FL    │ ORLANDO SANFORD IN…│ APPROACH     │
 SPIRIT AIRLINES    │ A-319        │ 05/10/15 00:00:00 │ IL    │ CHICAGO O'HARE INT…│ CLIMB        │
1› faa-wildlife-strikes|                                          c   go-col-regex      73448 rows 
</pre>


\... into this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 AIRPORT            ║ OPERATOR           │ Aircraft     │ INCIDENT_DATE     │ STATE │ PHASE_OF_FLT>
 VERO BEACH MUNICIP…║ BUSINESS           │ PA-28        │ 05/22/15 00:00:00 │ FL    │ APPROACH     │
 KENAI MUNICIPAL AR…║ BUSINESS           │ BE-1900      │ 06/18/15 00:00:00 │ AK    │ APPROACH     │
 DAVID WAYNE HOOKS …║ BUSINESS           │ PA-46 MALIBU │ 09/20/15 00:00:00 │ TX    │              │
 LAMBERT-ST LOUIS I…║ DELTA AIR LINES    │ B-717-200    │ 11/07/15 00:00:00 │ MO    │ APPROACH     │
 POMPANO BEACH AIRP…║ BUSINESS           │ BE-90 KING   │ 12/17/15 00:00:00 │ FL    │ LANDING ROLL │
 HENRY E ROHLSEN AR…║ DELTA AIR LINES    │ B-757        │ 07/17/15 00:00:00 │ VI    │              │
 SAN ANTONIO INTL   ║ DELTA AIR LINES    │ B-717-200    │ 08/02/15 00:00:00 │ TX    │ APPROACH     │
 LONE STAR EXECUTIV…║ BUSINESS           │ C-414        │ 08/03/15 00:00:00 │ TX    │ DEPARTURE    │
 TAMPA INTL         ║ ALLEGIANT AIR      │ MD-80        │ 09/02/15 00:00:00 │ FL    │ APPROACH     │
 LAMBERT-ST LOUIS I…║ TRANS STATES AIRLI…│ EMB-145      │ 09/07/15 00:00:00 │ MO    │ APPROACH     │
 OPA-LOCKA EXECUTIV…║ BUSINESS           │ C-172        │ 11/28/15 00:00:00 │ FL    │ APPROACH     │
 NORMAN Y. MINETA S…║ GOVERNMENT         │ EC120        │ 12/08/15 00:00:00 │ CA    │              │
 FORT LAUDERDALE/HO…║ AMERICAN AIRLINES  │ A-321        │ 05/06/15 00:00:00 │ FL    │ APPROACH     │
 FORT SMITH REGIONA…║ EXPRESSJET AIRLINES│ CRJ100/200   │ 05/06/15 00:00:00 │ AR    │ CLIMB        │
 BILL AND  HILLARY …║ MESA AIRLINES      │ CRJ900       │ 05/08/15 00:00:00 │ AR    │ LANDING ROLL │
 UNKNOWN            ║ BUSINESS           │ HELICOPTER   │ 05/06/15 00:00:00 │       │ En Route     │
 METRO OAKLAND INTL ║ DELTA AIR LINES    │ A-320        │ 05/07/15 00:00:00 │ CA    │              │
 SALT LAKE CITY INTL║ DELTA AIR LINES    │ A-320        │ 05/08/15 00:00:00 │ UT    │              │
 GEORGE BUSH INTERC…║ LUFTHANSA          │ A-380        │ 05/10/15 00:00:00 │ TX    │ CLIMB        │
 ORLANDO SANFORD IN…║ BUSINESS           │ C-172        │ 05/08/15 00:00:00 │ FL    │ APPROACH     │
 CHICAGO O'HARE INT…║ SPIRIT AIRLINES    │ A-319        │ 05/10/15 00:00:00 │ IL    │ CLIMB        │
1› faa-wildlife-strikes|                                               !   key-col      73448 rows 
</pre>



## Manipulating columns from the Columns Sheet

You can do nearly all of the above from the Columns Sheet (`Shift-C`). When you\'re dealing with datasets with a particularly large number of columns, doing it this way can often be easier; you can see more of the columns at once, and you can adjust multiple columns at once.

- **Moving columns**: In the Columns Sheet, each column is represented as a row; you can reposition them using `Shift-J` and `Shift-K`.
- **Editing column names**: In the Columns Sheet, you can edit each column\'s name like you would any other row cell. Just navigate to the name, and press `e` to start editing.
- **Setting column types**: You can select multiple rows of the Columns Sheet and type `g$`, for example, to set all of the selected columns\' types to `currency`.
- **Setting column widths**: You can edit the `width` field of the Columns Sheet to adjust any column\'s width. You can also give multiple columns to the same width by selecting each of their rows, and typing `ge` + *number*, where *number* is the desired width.

For instance, here\'s the Columns Sheet for the FAA dataset before we\'ve made any changes:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 name              ║ width#│ type │ fmtstr │ value              │ aggregators ║                    
 OPERATOR          ║    20 │      │        │ BUSINESS           │             ║                     
 ATYPE             ║    14 │      │        │ PA-28              │             ║                     
 INCIDENT_DATE     ║    19 │      │        │ 05/22/15 00:00:00  │             ║                     
 STATE             ║     7 │      │        │ FL                 │             ║                     
 AIRPORT           ║    20 │      │        │ VERO BEACH MUNICIP…│             ║                     
 PHASE_OF_FLT      ║    14 │      │        │ APPROACH           │             ║                     
 HEIGHT            ║      ⌀│      │        │                    │             ║                     
 SPEED             ║      ⌀│      │        │                    │             ║                     
 SPECIES           ║      ⌀│      │        │ Unknown bird       │             ║                     
 BIRDS_STRUCK      ║      ⌀│      │        │ 1                  │             ║                     
 EFFECT            ║      ⌀│      │        │ NONE               │             ║                     
 DAMAGE            ║      ⌀│      │        │ M                  │             ║                     
 COST_REPAIRS      ║      ⌀│      │        │                    │             ║                     
 PERSON            ║      ⌀│      │        │ Tower              │             ║                     
 REMAINS_COLLECTED ║      ⌀│      │        │ 0                  │             ║                     
 REMARKS           ║      ⌀│      │        │ N9240F was right b…│             ║                     


Shift+C› faa-wildlife-strikes_columns|                               Shift+C            16 columns 
</pre>


Next, we use the `s` key to select the four columns we\'d like to change:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 name              ║ width#│ type │ fmtstr │ value              │ aggregators ║                    
 OPERATOR          ║    20 │      │        │ BUSINESS           │             ║                     
 ATYPE             ║    14 │      │        │ PA-28              │             ║                     
 INCIDENT_DATE     ║    19 │      │        │ 05/22/15 00:00:00  │             ║                     
 STATE             ║     7 │      │        │ FL                 │             ║                     
 AIRPORT           ║    20 │      │        │ VERO BEACH MUNICIP…│             ║                     
 PHASE_OF_FLT      ║    14 │      │        │ APPROACH           │             ║                     
•HEIGHT            ║      ⌀│      │        │                    │             ║                     
•SPEED             ║      ⌀│      │        │                    │             ║                     
 SPECIES           ║      ⌀│      │        │ Unknown bird       │             ║                     
•BIRDS_STRUCK      ║      ⌀│      │        │ 1                  │             ║                     
 EFFECT            ║      ⌀│      │        │ NONE               │             ║                     
 DAMAGE            ║      ⌀│      │        │ M                  │             ║                     
•COST_REPAIRS      ║      ⌀│      │        │                    │             ║                     
 PERSON            ║      ⌀│      │        │ Tower              │             ║                     
 REMAINS_COLLECTED ║      ⌀│      │        │ 0                  │             ║                     
 REMARKS           ║      ⌀│      │        │ N9240F was right b…│             ║                     


Shift+C› faa-wildlife-strikes_columns|                       s   select-row         16 columns  •4 
</pre>


We\'d like to make them all numeric columns, so we type `g#`, which results in this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 name              ║ width#│ type │ fmtstr │ value              │ aggregators ║                    
 OPERATOR          ║    20 │      │        │ BUSINESS           │             ║                     
 ATYPE             ║    14 │      │        │ PA-28              │             ║                     
 INCIDENT_DATE     ║    19 │      │        │ 05/22/15 00:00:00  │             ║                     
 STATE             ║     7 │      │        │ FL                 │             ║                     
 AIRPORT           ║    20 │      │        │ VERO BEACH MUNICIP…│             ║                     
 PHASE_OF_FLT      ║    14 │      │        │ APPROACH           │             ║                     
•HEIGHT            ║      ⌀│ int  │        │                    │             ║                     
•SPEED             ║      ⌀│ int  │        │                    │             ║                     
 SPECIES           ║      ⌀│      │        │ Unknown bird       │             ║                     
•BIRDS_STRUCK      ║      ⌀│ int  │        │ 1                  │             ║                     
 EFFECT            ║      ⌀│      │        │ NONE               │             ║                     
 DAMAGE            ║      ⌀│      │        │ M                  │             ║                     
•COST_REPAIRS      ║      ⌀│ int  │        │                    │             ║                     
 PERSON            ║      ⌀│      │        │ Tower              │             ║                     
 REMAINS_COLLECTED ║      ⌀│      │        │ 0                  │             ║                     
 REMARKS           ║      ⌀│      │        │ N9240F was right b…│             ║                     


Shift+C› faa-wildlife-strikes_columns|               g#   type-int-selected         16 columns  •4 
</pre>


And we\'d like to make them uniformly narrow, so we navigate to the width column and type `ge8` + `Enter`, which gives us this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 name              ║ width#│ type │ fmtstr │ value              │ aggregators ║                    
 OPERATOR          ║    20 │      │        │ BUSINESS           │             ║                     
 ATYPE             ║    14 │      │        │ PA-28              │             ║                     
 INCIDENT_DATE     ║    19 │      │        │ 05/22/15 00:00:00  │             ║                     
 STATE             ║     7 │      │        │ FL                 │             ║                     
 AIRPORT           ║    20 │      │        │ VERO BEACH MUNICIP…│             ║                     
 PHASE_OF_FLT      ║    14 │      │        │ APPROACH           │             ║                     
•HEIGHT            ║     8 │ int  │        │                    │             ║                     
•SPEED             ║     8 │ int  │        │                    │             ║                     
 SPECIES           ║      ⌀│      │        │ Unknown bird       │             ║                     
•BIRDS_STRUCK      ║     8 │ int  │        │ 1                  │             ║                     
 EFFECT            ║      ⌀│      │        │ NONE               │             ║                     
 DAMAGE            ║      ⌀│      │        │ M                  │             ║                     
•COST_REPAIRS      ║     8 │ int  │        │                    │             ║                     
 PERSON            ║      ⌀│      │        │ Tower              │             ║                     
 REMAINS_COLLECTED ║      ⌀│      │        │ 0                  │             ║                     
 REMARKS           ║      ⌀│      │        │ N9240F was right b…│             ║                     


                                                       ┌─────────────────────────────| statuses |─┐
                                                       │ set 4 cells to 1 values                  │
                                                       └──────────────────────────────────────────┘
Shift+C› faa-wildlife-strikes_columns|                ge   setcol-input         16 columns  [M] •4 
</pre>


To see how these changes have affected your data sheet, press `q` to exit the Columns Sheet, and then navigate over to the `HEIGHT` column:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
<STATE │ AIRPORT            │ PHASE_OF_FLT │ HEIGHT#│ SPEED #│ SPECIES            │ BIRDS_#│ EFFEC>
 FL    │ VERO BEACH MUNICIP…│ APPROACH     │       !│       !│ Unknown bird       │      1 │ NONE   
 AK    │ KENAI MUNICIPAL AR…│ APPROACH     │       !│       !│ Unknown bird       │      1 │ NONE   
 TX    │ DAVID WAYNE HOOKS …│              │       !│       !│ Unknown bird       │      1 │ NONE   
 MO    │ LAMBERT-ST LOUIS I…│ APPROACH     │       !│       !│ Unknown bird       │      1 │ NONE   
 FL    │ POMPANO BEACH AIRP…│ LANDING ROLL │      0 │       !│ Unknown bird       │      1 │        
 VI    │ HENRY E ROHLSEN AR…│              │       !│       !│ Unknown bird       │      1 │ Other  
 TX    │ SAN ANTONIO INTL   │ APPROACH     │       !│       !│ Unknown bird       │      1 │ NONE   
 TX    │ LONE STAR EXECUTIV…│ DEPARTURE    │       !│       !│ Unknown bird       │      1 │ PRECA… 
 FL    │ TAMPA INTL         │ APPROACH     │   6000 │       !│ Unknown bird       │      1 │ NONE   
 MO    │ LAMBERT-ST LOUIS I…│ APPROACH     │       !│       !│ Owls               │      1 │ NONE   
 FL    │ OPA-LOCKA EXECUTIV…│ APPROACH     │       !│       !│ Hawks              │      1 │ NONE   
 CA    │ NORMAN Y. MINETA S…│              │       !│       !│ Gulls              │      1 │ NONE   
 FL    │ FORT LAUDERDALE/HO…│ APPROACH     │   1500 │       !│ Unknown bird - sma…│      1 │ NONE   
 AR    │ FORT SMITH REGIONA…│ CLIMB        │       !│       !│ Unknown bird - sma…│      1 │ NONE   
 AR    │ BILL AND  HILLARY …│ LANDING ROLL │      0 │       !│ Unknown bird - sma…│      1 │ NONE   
       │ UNKNOWN            │ En Route     │       !│       !│ Unknown bird       │      1 │ PRECA… 
 CA    │ METRO OAKLAND INTL │              │       !│       !│ Unknown bird       │      1 │ NONE   
 UT    │ SALT LAKE CITY INTL│              │       !│       !│ Unknown bird       │      1 │ NONE   
 TX    │ GEORGE BUSH INTERC…│ CLIMB        │       !│       !│ Unknown bird       │      1 │ NONE   
 FL    │ ORLANDO SANFORD IN…│ APPROACH     │       !│       !│ Unknown bird       │      1 │ NONE   
 IL    │ CHICAGO O'HARE INT…│ CLIMB        │  12000 │       !│ Unknown bird       │      1 │ PRECA… 
1› faa-wildlife-strikes|                                               h   go-left      73448 rows 
</pre>




## Selecting and Unselecting Rows

Many VisiData commands --- such as filtering --- distinguish between selected and unselected rows. You can select and unselect rows in a few ways:

### One row at a time

  Keystroke(s)                        Action
  ----------------------------------- ----------------------------------------------------
  `s`   Select the current row
  `u`   Unselect the current row
  `t`   Toggle the current row between selected/unselected

For instance, pressing `s` while on the second row of the FAA dataset should have the following effect:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 OPERATOR           │ ATYPE        │ INCIDENT_DATE     │ STATE │ AIRPORT            │ PHASE_OF_FLT>
 BUSINESS           │ PA-28        │ 05/22/15 00:00:00 │ FL    │ VERO BEACH MUNICIP…│ APPROACH     │
•BUSINESS           │ BE-1900      │ 06/18/15 00:00:00 │ AK    │ KENAI MUNICIPAL AR…│ APPROACH     │
 BUSINESS           │ PA-46 MALIBU │ 09/20/15 00:00:00 │ TX    │ DAVID WAYNE HOOKS …│              │
 DELTA AIR LINES    │ B-717-200    │ 11/07/15 00:00:00 │ MO    │ LAMBERT-ST LOUIS I…│ APPROACH     │
 BUSINESS           │ BE-90 KING   │ 12/17/15 00:00:00 │ FL    │ POMPANO BEACH AIRP…│ LANDING ROLL │
 DELTA AIR LINES    │ B-757        │ 07/17/15 00:00:00 │ VI    │ HENRY E ROHLSEN AR…│              │
 DELTA AIR LINES    │ B-717-200    │ 08/02/15 00:00:00 │ TX    │ SAN ANTONIO INTL   │ APPROACH     │
 BUSINESS           │ C-414        │ 08/03/15 00:00:00 │ TX    │ LONE STAR EXECUTIV…│ DEPARTURE    │
 ALLEGIANT AIR      │ MD-80        │ 09/02/15 00:00:00 │ FL    │ TAMPA INTL         │ APPROACH     │
 TRANS STATES AIRLI…│ EMB-145      │ 09/07/15 00:00:00 │ MO    │ LAMBERT-ST LOUIS I…│ APPROACH     │
 BUSINESS           │ C-172        │ 11/28/15 00:00:00 │ FL    │ OPA-LOCKA EXECUTIV…│ APPROACH     │
 GOVERNMENT         │ EC120        │ 12/08/15 00:00:00 │ CA    │ NORMAN Y. MINETA S…│              │
 AMERICAN AIRLINES  │ A-321        │ 05/06/15 00:00:00 │ FL    │ FORT LAUDERDALE/HO…│ APPROACH     │
 EXPRESSJET AIRLINES│ CRJ100/200   │ 05/06/15 00:00:00 │ AR    │ FORT SMITH REGIONA…│ CLIMB        │
 MESA AIRLINES      │ CRJ900       │ 05/08/15 00:00:00 │ AR    │ BILL AND  HILLARY …│ LANDING ROLL │
 BUSINESS           │ HELICOPTER   │ 05/06/15 00:00:00 │       │ UNKNOWN            │ En Route     │
 DELTA AIR LINES    │ A-320        │ 05/07/15 00:00:00 │ CA    │ METRO OAKLAND INTL │              │
 DELTA AIR LINES    │ A-320        │ 05/08/15 00:00:00 │ UT    │ SALT LAKE CITY INTL│              │
 LUFTHANSA          │ A-380        │ 05/10/15 00:00:00 │ TX    │ GEORGE BUSH INTERC…│ CLIMB        │
 BUSINESS           │ C-172        │ 05/08/15 00:00:00 │ FL    │ ORLANDO SANFORD IN…│ APPROACH     │
 SPIRIT AIRLINES    │ A-319        │ 05/10/15 00:00:00 │ IL    │ CHICAGO O'HARE INT…│ CLIMB        │
1› faa-wildlife-strikes|                                        s   select-row      73448 rows  •1 
</pre>


VisiData has highlighted that row and indicated the number of selected rows (the `•1` in the bottom-right corner).

### All rows at the same time

  Keystroke(s)                         Action
  ------------------------------------ ---------------------------------------------
  `gs`   Select all rows
  `gu`   Unselect all rows
  `gt`   Toggle all rows between selected/unselected

### By matching patterns

  Keystroke(s)                                   Action
  ---------------------------------------------- ----------------------------------------------------------------------------------------
  `|` + *term*     Select all rows where *term* matches the **current column**
  `\\` + *term*    Unselect all rows where *term* matches the **current column**
  `g|` + *term*    Select all rows where *term* matches **any** column
  `g\\` + *term*   Unselect all rows where *term* matches **any** column
  `,`              Select all rows where the **current column** matches this row\'s value for that column
  `g,`             Select all rows matching **the current row** (for all non-hidden columns)

For instance, if you take the following steps:

- Navigate to the `STATE` column
- Press `|`
- Type `TX`
- Press `Enter`

\... you should see this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 OPERATOR           │ ATYPE        │ INCIDENT_DATE     │ STATE │ AIRPORT            │ PHASE_OF_FLT>
 BUSINESS           │ PA-28        │ 05/22/15 00:00:00 │ FL    │ VERO BEACH MUNICIP…│ APPROACH     │
 BUSINESS           │ BE-1900      │ 06/18/15 00:00:00 │ AK    │ KENAI MUNICIPAL AR…│ APPROACH     │
•BUSINESS           │ PA-46 MALIBU │ 09/20/15 00:00:00 │ TX    │ DAVID WAYNE HOOKS …│              │
 DELTA AIR LINES    │ B-717-200    │ 11/07/15 00:00:00 │ MO    │ LAMBERT-ST LOUIS I…│ APPROACH     │
 BUSINESS           │ BE-90 KING   │ 12/17/15 00:00:00 │ FL    │ POMPANO BEACH AIRP…│ LANDING ROLL │
 DELTA AIR LINES    │ B-757        │ 07/17/15 00:00:00 │ VI    │ HENRY E ROHLSEN AR…│              │
•DELTA AIR LINES    │ B-717-200    │ 08/02/15 00:00:00 │ TX    │ SAN ANTONIO INTL   │ APPROACH     │
•BUSINESS           │ C-414        │ 08/03/15 00:00:00 │ TX    │ LONE STAR EXECUTIV…│ DEPARTURE    │
 ALLEGIANT AIR      │ MD-80        │ 09/02/15 00:00:00 │ FL    │ TAMPA INTL         │ APPROACH     │
 TRANS STATES AIRLI…│ EMB-145      │ 09/07/15 00:00:00 │ MO    │ LAMBERT-ST LOUIS I…│ APPROACH     │
 BUSINESS           │ C-172        │ 11/28/15 00:00:00 │ FL    │ OPA-LOCKA EXECUTIV…│ APPROACH     │
 GOVERNMENT         │ EC120        │ 12/08/15 00:00:00 │ CA    │ NORMAN Y. MINETA S…│              │
 AMERICAN AIRLINES  │ A-321        │ 05/06/15 00:00:00 │ FL    │ FORT LAUDERDALE/HO…│ APPROACH     │
 EXPRESSJET AIRLINES│ CRJ100/200   │ 05/06/15 00:00:00 │ AR    │ FORT SMITH REGIONA…│ CLIMB        │
 MESA AIRLINES      │ CRJ900       │ 05/08/15 00:00:00 │ AR    │ BILL AND  HILLARY …│ LANDING ROLL │
 BUSINESS           │ HELICOPTER   │ 05/06/15 00:00:00 │       │ UNKNOWN            │ En Route     │
 DELTA AIR LINES    │ A-320        │ 05/07/15 00:00:00 ┌─────────────────────────────| statuses |─┐│
 DELTA AIR LINES    │ A-320        │ 05/08/15 00:00:00 │ search wrapped                           ││
•LUFTHANSA          │ A-380        │ 05/10/15 00:00:00 │ 7309 matches for /TX/                    ││
 BUSINESS           │ C-172        │ 05/08/15 00:00:00 │ selected 7309 rows                       ││
 SPIRIT AIRLINES    │ A-319        │ 05/10/15 00:00:00 └──────────────────────────────────────────┘│
1› faa-wildlife-strikes|                               |   select-col-regex      73448 rows  •7309 
</pre>


### Via expressions

In VisiData, you can select rows by evaluating a given Python **expression** for every row in your dataset.

:::: tip
::: title
Tip

If you\'re unfamiliar with Python, no worries. You can find an overview of simple and handy expressions [here](https://docs.python.org/3/tutorial/introduction.html).

These expressions can reference any column in your dataset (so long as the column name contains only letters, underscores, and numbers, and doesn\'t start with a number; in the next chapter, you\'ll learn how to rename columns). The two keystrokes for this are `z|` and `z\\`:

  Keystroke(s)                                   Action
  ---------------------------------------------- ----------------------------------------------------
  `z|` + *expr*    Select all rows where *expr* evaluates to `True`
  `z\\` + *expr*   Unselect all rows where *expr* evaluates to `True`

For instance, if you take the following steps:

- Type `gu` to unselect all rows
- Type `z|`
- Type `OPERATOR == "BUSINESS" and STATE == "FL"`
- Press `Enter`

\... you should see this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 OPERATOR           │ ATYPE        │ INCIDENT_DATE     │ STATE │ AIRPORT            │ PHASE_OF_FLT>
•BUSINESS           │ PA-28        │ 05/22/15 00:00:00 │ FL    │ VERO BEACH MUNICIP…│ APPROACH     │
 BUSINESS           │ BE-1900      │ 06/18/15 00:00:00 │ AK    │ KENAI MUNICIPAL AR…│ APPROACH     │
 BUSINESS           │ PA-46 MALIBU │ 09/20/15 00:00:00 │ TX    │ DAVID WAYNE HOOKS …│              │
 DELTA AIR LINES    │ B-717-200    │ 11/07/15 00:00:00 │ MO    │ LAMBERT-ST LOUIS I…│ APPROACH     │
•BUSINESS           │ BE-90 KING   │ 12/17/15 00:00:00 │ FL    │ POMPANO BEACH AIRP…│ LANDING ROLL │
 DELTA AIR LINES    │ B-757        │ 07/17/15 00:00:00 │ VI    │ HENRY E ROHLSEN AR…│              │
 DELTA AIR LINES    │ B-717-200    │ 08/02/15 00:00:00 │ TX    │ SAN ANTONIO INTL   │ APPROACH     │
 BUSINESS           │ C-414        │ 08/03/15 00:00:00 │ TX    │ LONE STAR EXECUTIV…│ DEPARTURE    │
 ALLEGIANT AIR      │ MD-80        │ 09/02/15 00:00:00 │ FL    │ TAMPA INTL         │ APPROACH     │
 TRANS STATES AIRLI…│ EMB-145      │ 09/07/15 00:00:00 │ MO    │ LAMBERT-ST LOUIS I…│ APPROACH     │
•BUSINESS           │ C-172        │ 11/28/15 00:00:00 │ FL    │ OPA-LOCKA EXECUTIV…│ APPROACH     │
 GOVERNMENT         │ EC120        │ 12/08/15 00:00:00 │ CA    │ NORMAN Y. MINETA S…│              │
 AMERICAN AIRLINES  │ A-321        │ 05/06/15 00:00:00 │ FL    │ FORT LAUDERDALE/HO…│ APPROACH     │
 EXPRESSJET AIRLINES│ CRJ100/200   │ 05/06/15 00:00:00 │ AR    │ FORT SMITH REGIONA…│ CLIMB        │
 MESA AIRLINES      │ CRJ900       │ 05/08/15 00:00:00 │ AR    │ BILL AND  HILLARY …│ LANDING ROLL │
 BUSINESS           │ HELICOPTER   │ 05/06/15 00:00:00 │       │ UNKNOWN            │ En Route     │
 DELTA AIR LINES    │ A-320        │ 05/07/15 00:00:00 │ CA    │ METRO OAKLAND INTL │              │
 DELTA AIR LINES    │ A-320        │ 05/08/15 00:00:00 │ UT    │ SALT LAKE CITY INTL│              │
 LUFTHANSA          │ A-380        │ 05/10/15 00:00:00 ┌─────────────────────────────| statuses |─┐│
•BUSINESS           │ C-172        │ 05/08/15 00:00:00 │ selected 625 rows                        ││
 SPIRIT AIRLINES    │ A-319        │ 05/10/15 00:00:00 └──────────────────────────────────────────┘│
1› faa-wildlife-strikes|                                    z|   select-expr      73448 rows  •625 
</pre>


:::: tip
::: title
Tip

Likewise, you can *search* via expressions using `z/` (search forward) and `z?` (search backward).


## Moving Rows

You can move the position of row up or down using the following commands:

  Keystroke(s)                              Action
  ----------------------------------------- ------------------------
  `Shift-K`   Move row up one spot
  `Shift-J`   Move row down one spot



## Editing Row Cells

Even if you don\'t want to edit your raw data in VisiData, knowing how to edit cells will still come in handy, since virtually *everything* --- including settings --- in VisiData is represented as columns and rows.

Here are the most basic commands:

  Keystroke(s)                                Action
  ------------------------------------------- -------------------------------------------------------
  `e`           Begin editing current cell
  `Enter`       Finish editing
  `Control-c`   Cancel editing
  `Control-a`   Move to beginning of line
  `Control-e`   Move to end of line
  `Control-k`   Clear contents from cursor\'s position to end of line

Other keys --- such as `Delete`, standard characters, and the arrow keys --- work as expected. You can find a handful of additional special commands in [VisiData\'s quick reference](http://visidata.org/man/).


## How to use the Sheets Sheet

VisiData\'s \"Sheets Sheet\" lists all currently-open sheets and makes it easy to jump between sheets.

From anywhere in VisiData, you can open the Sheets Sheet by pressing `Shift-S`.

If you\'ve just launched VisiData with a single dataset, pressing `Shift-S` will open a Sheets Sheet that looks something like this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 name               ║ type        │ pane#│ shortcut │ nRows#│ nCols#│ nVisibleCols#│ cursorDisplay>
 sheets             ║ SheetsSheet │    1 │ Shift+S  │     2 │    11 │           11 │ sheets        │
 faa-wildlife-strik…║ CsvSheet    │    1 │ 1        │ 73448 │    16 │           16 │ BUSINESS      │


Shift+S› sheets|                                                      Shift+S             2 sheets 
</pre>


Not very exciting. But as you start juggling more sheets --- frequency tables, multiple datasets, et cetera --- the Sheets Sheet becomes very handy.

You can navigate the Sheets Sheet much like you would any other sheet, with one main difference: Pressing `Enter` will open that row\'s sheet.

:::: warning
::: title
Warning

Pressing `d` on a Sheets Sheet will send that row\'s sheet to the \"sheets graveyard.\" (You can type `gS` to visit the graveyard, and revive sheets there via `Enter`.)



## How to rename a sheet

There are two ways to rename a sheet:

- Go to the **Sheets Sheet**, and navigate to the row representing the sheet you want to rename. Press `e` to go into editing mode, type the new name, and then press `Enter` to complete the renaming.
- Alternatively, while **in the sheet you want to rename**, press `Space` to raise the type-a-command prompt. Then, type `rename-sheet` and press `Enter`. At the next prompt, type the new name, and press `Enter` to complete the renaming.


## How to close/remove a sheet

To close the current sheet (removing it from VisiData), press `q`.

To close all sheets (and, hence, quitting VisiData in its entirety), type `gq`.

To access the \"sheets graveyard\", a listing of recently-closed sheets, type `gS`.



## How to *prevent* sheet closure/removal

You can prevent VisiData from quitting a sheet by \"guarding\" it. To do so, press `Space` to raise the type-a-command prompt. Then, type `guard-sheet` and press `Enter`.


## Quickly toggling between sheets

To flip back and forth between your current sheet and the previous one, press `Control-^`.

Additionally, VisiData assigns every sheet a numeric shortcut, visible at the bottom-left corner of the interface. You can jump to a sheet by pressing `Alt` plus the shortcut number --- for instance `Alt-1` to go to the first sheet you loaded.



## How to fix funky spreadsheets\' column names

By default, VisiData considers the first row of a tabular dataset to be its columns\' names. That\'s a safe assumption for many formats, but Excel spreadsheets often buck that trend, with titles, notes, or other cruft coming before the actual column names.

As previously noted, you can manually edit a column\'s name manually by pressing `^`, or by editing it from the Columns Sheet. But you can also auto-populate column names by doing the following:

- Navigate to the row that contains your desired column names.
- Type `g^` to name all *unnamed* columns with the values in this row, or `gz^` to name *all* columns (regardless of whether they\'re already named) with the values in this row.

If you\'d like to have VisiData *not* to load the first row as the header, you can do one of the following:

- Pass the `--header 0` option when you launch `vd` from the command line.

- From within VisiData, do this:

  > - Press `O` to open the Options Sheet
  > - Set the `header` option cell to `0`
  > - Press `q` to return to your spreadsheet
  > - Press `Control-r` to reload it


## About This Tutorial

:::: note
::: title
Note

This tutorial is not officially affiliated with VisiData, and is not intended as a comprehensive reference. You can learn more about VisiData from these official sources:

- [VisiData.org](https://visidata.org/)
- [VisiData\'s GitHub repository](https://github.com/saulpw/visidata)
- [Saul Pwanson\'s Patreon page](https://www.patreon.com/saulpw)
- [Saul Pwanson\'s case studies on YouTube](https://www.youtube.com/playlist?list=PLxu7QdBkC7drrAGfYzatPGVHIpv4Et46W)

### Tutorial Structure

This tutorial is divided into five sections:

  Section              Description                           Status
  -------------------- ------------------------------------- -----------------------
  The Big Picture      If you read nothing else \...         Draft complete
  Basic Usage          All you need to know to get started   Draft complete
  Intermediate Usage   Some of the handiest power-features   Draft complete
  Advanced Usage       How to bend VisiData to your whims    Four chapters drafted
  Practical Examples   Step-by-step walkthroughs             Two examples drafted

To be notified of new material and/or major updates, [sign up here](https://buttondown.email/intro-to-visidata).

### Tutorial Status

  ----------------------- --------------
  Tutorial last updated   `2024-03-08`
  VisiData version        `3.0.2`
  ----------------------- --------------



## About the author

[Jeremy Singer-Vine](https://www.jsvine.com/) is a journalist, computer programmer, and data editor based in New York City.


## Feedback / questions / corrections?

[File an issue on GitHub](https://github.com/jsvine/intro-to-visidata/issues) or email the author at <jsvine@gmail.com>.



## Acknowledgments

Many thanks to the following people for their feedback, suggestions, and fixes: [Saul Pwanson](http://saul.pw/), [Anja Kefala](https://github.com/anjakefala), [John Templon](https://twitter.com/jtemplon), [Scott Pham](https://twitter.com/scottpham), [Andrea Borruso](https://github.com/aborruso), [Felix Rosencrantz](https://github.com/frosencrantz), [Ram Rachum](https://github.com/cool-RR), [Ezequiel Garzon](https://github.com/ezequiel-garzon), [Joseph Reagle](https://github.com/reagle), [David Wales](https://github.com/daviewales), [\@rschwiebert](https://github.com/rschwiebert), [Martin Häcker](https://github.com/dwt).

About This Tutorial \<self\>

the-big-picture/what-is-visidata the-big-picture/installation the-big-picture/visidata-in-60-seconds

basics/getting-out-of-trouble basics/opening-files basics/navigating-visidata basics/understanding-sheets basics/understanding-rows basics/understanding-columns basics/sorting-and-filtering basics/summarizing-data basics/working-with-excel basics/saving-sheets

intermediate/creating-new-columns intermediate/joining-sheets intermediate/reshaping-data intermediate/large-cells intermediate/large-files

advanced/configuring-visidata advanced/extending-visidata advanced/debugging-visidata advanced/the-command-log

practical/high-flying-birds practical/distinctive-birds


## How to create an incremented column

You can add an incremented column with **sequential values** (akin to row numbers) by pressing `i`. Once you do that, VisiData will create this new column directly to the right of your current column:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 OPERATOR           │ A #│ ATYPE        │ INCIDENT_DATE     │ STATE │ AIRPORT            │ PHASE_O>
 BUSINESS           │  1 │ PA-28        │ 05/22/15 00:00:00 │ FL    │ VERO BEACH MUNICIP…│ APPROACH 
 BUSINESS           │  2 │ BE-1900      │ 06/18/15 00:00:00 │ AK    │ KENAI MUNICIPAL AR…│ APPROACH 
 BUSINESS           │  3 │ PA-46 MALIBU │ 09/20/15 00:00:00 │ TX    │ DAVID WAYNE HOOKS …│          
 DELTA AIR LINES    │  4 │ B-717-200    │ 11/07/15 00:00:00 │ MO    │ LAMBERT-ST LOUIS I…│ APPROACH 
 BUSINESS           │  5 │ BE-90 KING   │ 12/17/15 00:00:00 │ FL    │ POMPANO BEACH AIRP…│ LANDING… 
 DELTA AIR LINES    │  6 │ B-757        │ 07/17/15 00:00:00 │ VI    │ HENRY E ROHLSEN AR…│          
 DELTA AIR LINES    │  7 │ B-717-200    │ 08/02/15 00:00:00 │ TX    │ SAN ANTONIO INTL   │ APPROACH 
 BUSINESS           │  8 │ C-414        │ 08/03/15 00:00:00 │ TX    │ LONE STAR EXECUTIV…│ DEPARTU… 
 ALLEGIANT AIR      │  9 │ MD-80        │ 09/02/15 00:00:00 │ FL    │ TAMPA INTL         │ APPROACH 
 TRANS STATES AIRLI…│ 10 │ EMB-145      │ 09/07/15 00:00:00 │ MO    │ LAMBERT-ST LOUIS I…│ APPROACH 
 BUSINESS           │ 11 │ C-172        │ 11/28/15 00:00:00 │ FL    │ OPA-LOCKA EXECUTIV…│ APPROACH 
 GOVERNMENT         │ 12 │ EC120        │ 12/08/15 00:00:00 │ CA    │ NORMAN Y. MINETA S…│          
 AMERICAN AIRLINES  │ 13 │ A-321        │ 05/06/15 00:00:00 │ FL    │ FORT LAUDERDALE/HO…│ APPROACH 
 EXPRESSJET AIRLINES│ 14 │ CRJ100/200   │ 05/06/15 00:00:00 │ AR    │ FORT SMITH REGIONA…│ CLIMB    
 MESA AIRLINES      │ 15 │ CRJ900       │ 05/08/15 00:00:00 │ AR    │ BILL AND  HILLARY …│ LANDING… 
 BUSINESS           │ 16 │ HELICOPTER   │ 05/06/15 00:00:00 │       │ UNKNOWN            │ En Route 
 DELTA AIR LINES    │ 17 │ A-320        │ 05/07/15 00:00:00 │ CA    │ METRO OAKLAND INTL │          
 DELTA AIR LINES    │ 18 │ A-320        │ 05/08/15 00:00:00 │ UT    │ SALT LAKE CITY INTL│          
 LUFTHANSA          │ 19 │ A-380        │ 05/10/15 00:0┌─────────────────────────────| statuses |─┐ 
 BUSINESS           │ 20 │ C-172        │ 05/08/15 00:0│ set 73448 cells to 73448 values          │ 
 SPIRIT AIRLINES    │ 21 │ A-319        │ 05/10/15 00:0└──────────────────────────────────────────┘ 
1› faa-wildlife-strikes|                                       i   addcol-incr      73448 rows  [M]
</pre>


By default, VisiData will name the column `A` (or `B` if VisiData has already created an `A` column this session, and so on).

:::: note
::: title
Note

You can customize the \"step\" between values; to do that, type `zi`, and specify a number at the prompt. (Specifying `3`, for instance, would create the sequence `1, 4, 7, ...`.)



## How to create an expression column

Expression columns **evaluate** a given Python expression for every row in your dataset.

These expressions can reference any column in your dataset (so long as the column name contains only letters, underscores, and numbers, and doesn\'t start with a number).

:::: note
::: title
Note

If you\'re unfamiliar with Python, no worries. You can find an overview of simple and handy expressions [here](https://docs.python.org/3/tutorial/introduction.html).

You can create an expression column by pressing `=`. Once you do so, you\'ll see a prompt at the bottom of the screen. Then, type your desired expression and press `Enter`.

Perhaps the simplest expression column would be `=1`; for every row, the column\'s value would be `1`. Let\'s see how that looks:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 OPERATOR           │ 1  │ ATYPE        │ INCIDENT_DATE     │ STATE │ AIRPORT            │ PHASE_O>
 BUSINESS           │ 1 #│ PA-28        │ 05/22/15 00:00:00 │ FL    │ VERO BEACH MUNICIP…│ APPROACH 
 BUSINESS           │ 1 #│ BE-1900      │ 06/18/15 00:00:00 │ AK    │ KENAI MUNICIPAL AR…│ APPROACH 
 BUSINESS           │ 1 #│ PA-46 MALIBU │ 09/20/15 00:00:00 │ TX    │ DAVID WAYNE HOOKS …│          
 DELTA AIR LINES    │ 1 #│ B-717-200    │ 11/07/15 00:00:00 │ MO    │ LAMBERT-ST LOUIS I…│ APPROACH 
 BUSINESS           │ 1 #│ BE-90 KING   │ 12/17/15 00:00:00 │ FL    │ POMPANO BEACH AIRP…│ LANDING… 
 DELTA AIR LINES    │ 1 #│ B-757        │ 07/17/15 00:00:00 │ VI    │ HENRY E ROHLSEN AR…│          
 DELTA AIR LINES    │ 1 #│ B-717-200    │ 08/02/15 00:00:00 │ TX    │ SAN ANTONIO INTL   │ APPROACH 
 BUSINESS           │ 1 #│ C-414        │ 08/03/15 00:00:00 │ TX    │ LONE STAR EXECUTIV…│ DEPARTU… 
 ALLEGIANT AIR      │ 1 #│ MD-80        │ 09/02/15 00:00:00 │ FL    │ TAMPA INTL         │ APPROACH 
 TRANS STATES AIRLI…│ 1 #│ EMB-145      │ 09/07/15 00:00:00 │ MO    │ LAMBERT-ST LOUIS I…│ APPROACH 
 BUSINESS           │ 1 #│ C-172        │ 11/28/15 00:00:00 │ FL    │ OPA-LOCKA EXECUTIV…│ APPROACH 
 GOVERNMENT         │ 1 #│ EC120        │ 12/08/15 00:00:00 │ CA    │ NORMAN Y. MINETA S…│          
 AMERICAN AIRLINES  │ 1 #│ A-321        │ 05/06/15 00:00:00 │ FL    │ FORT LAUDERDALE/HO…│ APPROACH 
 EXPRESSJET AIRLINES│ 1 #│ CRJ100/200   │ 05/06/15 00:00:00 │ AR    │ FORT SMITH REGIONA…│ CLIMB    
 MESA AIRLINES      │ 1 #│ CRJ900       │ 05/08/15 00:00:00 │ AR    │ BILL AND  HILLARY …│ LANDING… 
 BUSINESS           │ 1 #│ HELICOPTER   │ 05/06/15 00:00:00 │       │ UNKNOWN            │ En Route 
 DELTA AIR LINES    │ 1 #│ A-320        │ 05/07/15 00:00:00 │ CA    │ METRO OAKLAND INTL │          
 DELTA AIR LINES    │ 1 #│ A-320        │ 05/08/15 00:00:00 │ UT    │ SALT LAKE CITY INTL│          
 LUFTHANSA          │ 1 #│ A-380        │ 05/10/15 00:00:00 │ TX    │ GEORGE BUSH INTERC…│ CLIMB    
 BUSINESS           │ 1 #│ C-172        │ 05/08/15 00:00:00 │ FL    │ ORLANDO SANFORD IN…│ APPROACH 
 SPIRIT AIRLINES    │ 1 #│ A-319        │ 05/10/15 00:00:00 │ IL    │ CHICAGO O'HARE INT…│ CLIMB    
1› faa-wildlife-strikes|                                       =   addcol-expr      73448 rows  [M]
</pre>


:::: note
::: title
Note

By default, the name of your new columns will be the expression you entered. As always, you can edit the column name by pressing `^` and typing the new name.

Also by default, the column will appear directly to the right of the column that was active when you pressed `=`. As always, you can move the column left or right using `Shift-H` and `Shift-L`.

Now, let\'s try creating a column *based on another column*. Let\'s say we want to identify wildlife strikes that were reported to have occurred at least 100 feet above ground. We could do the following:

- Navigate to the `HEIGHT` column
- Press `#` to tell VisiData the column\'s values should be interpreted as integers
- Press `=` to bring up the \"new column expr=\" prompt
- In the prompt, type `HEIGHT >= 100`
- Press `Enter`

You should see something like the following:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
<STATE │ AIRPORT            │ PHASE_OF_FLT │ HEIGHT#│ HEIGHT >= 100 │ SPEED │ SPECIES            │>
 FL    │ VERO BEACH MUNICIP…│ APPROACH     │       !│ False         │       │ Unknown bird       │1 
 AK    │ KENAI MUNICIPAL AR…│ APPROACH     │       !│ False         │       │ Unknown bird       │1 
 TX    │ DAVID WAYNE HOOKS …│              │       !│ False         │       │ Unknown bird       │1 
 MO    │ LAMBERT-ST LOUIS I…│ APPROACH     │       !│ False         │       │ Unknown bird       │1 
 FL    │ POMPANO BEACH AIRP…│ LANDING ROLL │      0 │ False         │       │ Unknown bird       │1 
 VI    │ HENRY E ROHLSEN AR…│              │       !│ False         │       │ Unknown bird       │1 
 TX    │ SAN ANTONIO INTL   │ APPROACH     │       !│ False         │       │ Unknown bird       │1 
 TX    │ LONE STAR EXECUTIV…│ DEPARTURE    │       !│ False         │       │ Unknown bird       │1 
 FL    │ TAMPA INTL         │ APPROACH     │   6000 │ True          │       │ Unknown bird       │1 
 MO    │ LAMBERT-ST LOUIS I…│ APPROACH     │       !│ False         │       │ Owls               │1 
 FL    │ OPA-LOCKA EXECUTIV…│ APPROACH     │       !│ False         │       │ Hawks              │1 
 CA    │ NORMAN Y. MINETA S…│              │       !│ False         │       │ Gulls              │1 
 FL    │ FORT LAUDERDALE/HO…│ APPROACH     │   1500 │ True          │       │ Unknown bird - sma…│1 
 AR    │ FORT SMITH REGIONA…│ CLIMB        │       !│ False         │       │ Unknown bird - sma…│1 
 AR    │ BILL AND  HILLARY …│ LANDING ROLL │      0 │ False         │       │ Unknown bird - sma…│1 
       │ UNKNOWN            │ En Route     │       !│ False         │       │ Unknown bird       │1 
 CA    │ METRO OAKLAND INTL │              │       !│ False         │       │ Unknown bird       │1 
 UT    │ SALT LAKE CITY INTL│              │       !│ False         │       │ Unknown bird       │1 
 TX    │ GEORGE BUSH INTERC…│ CLIMB        │       !│ False         │       │ Unknown bird       │1 
 FL    │ ORLANDO SANFORD IN…│ APPROACH     │       !│ False         │       │ Unknown bird       │1 
 IL    │ CHICAGO O'HARE INT…│ CLIMB        │  12000 │ True          │       │ Unknown bird       │1 
1› faa-wildlife-strikes|                                       =   addcol-expr      73448 rows  [M]
</pre>



## How to create new columns by splitting another one

You can split the text in any column in VisiData into two or more columns, based on a pattern (i.e., a \"regular expression\" a.k.a. \"regex\") that you provide.

To split a column, navigate to that column, and press `:`. At the bottom of the screen, VisiData you\'ll see a `split regex:` prompt. Enter your desired splitting pattern, and press `Enter`.

For a simple example, let\'s say we want to split the `INCIDENT_DATE` column into the date and time. Because the date and time are separated by a space, we can do this:

- Navigate to the `INCIDENT_DATE` column
- Press `:`
- At the prompt, press `Space` (since we want to split on the column\'s whitespace), and then hit `Enter`

Once you do that, you should see something like this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 OPERATOR           │ ATYPE        │ INCIDENT_DATE     │ INCIDENT_DATE_re   │ STATE │ AIRPORT     >
 BUSINESS           │ PA-28        │ 05/22/15 00:00:00 │ [2] 05/22/15; 00:0…│ FL    │ VERO BEACH M… 
 BUSINESS           │ BE-1900      │ 06/18/15 00:00:00 │ [2] 06/18/15; 00:0…│ AK    │ KENAI MUNICI… 
 BUSINESS           │ PA-46 MALIBU │ 09/20/15 00:00:00 │ [2] 09/20/15; 00:0…│ TX    │ DAVID WAYNE … 
 DELTA AIR LINES    │ B-717-200    │ 11/07/15 00:00:00 │ [2] 11/07/15; 00:0…│ MO    │ LAMBERT-ST L… 
 BUSINESS           │ BE-90 KING   │ 12/17/15 00:00:00 │ [2] 12/17/15; 00:0…│ FL    │ POMPANO BEAC… 
 DELTA AIR LINES    │ B-757        │ 07/17/15 00:00:00 │ [2] 07/17/15; 00:0…│ VI    │ HENRY E ROHL… 
 DELTA AIR LINES    │ B-717-200    │ 08/02/15 00:00:00 │ [2] 08/02/15; 00:0…│ TX    │ SAN ANTONIO … 
 BUSINESS           │ C-414        │ 08/03/15 00:00:00 │ [2] 08/03/15; 00:0…│ TX    │ LONE STAR EX… 
 ALLEGIANT AIR      │ MD-80        │ 09/02/15 00:00:00 │ [2] 09/02/15; 00:0…│ FL    │ TAMPA INTL    
 TRANS STATES AIRLI…│ EMB-145      │ 09/07/15 00:00:00 │ [2] 09/07/15; 00:0…│ MO    │ LAMBERT-ST L… 
 BUSINESS           │ C-172        │ 11/28/15 00:00:00 │ [2] 11/28/15; 00:0…│ FL    │ OPA-LOCKA EX… 
 GOVERNMENT         │ EC120        │ 12/08/15 00:00:00 │ [2] 12/08/15; 00:0…│ CA    │ NORMAN Y. MI… 
 AMERICAN AIRLINES  │ A-321        │ 05/06/15 00:00:00 │ [2] 05/06/15; 00:0…│ FL    │ FORT LAUDERD… 
 EXPRESSJET AIRLINES│ CRJ100/200   │ 05/06/15 00:00:00 │ [2] 05/06/15; 00:0…│ AR    │ FORT SMITH R… 
 MESA AIRLINES      │ CRJ900       │ 05/08/15 00:00:00 │ [2] 05/08/15; 00:0…│ AR    │ BILL AND  HI… 
 BUSINESS           │ HELICOPTER   │ 05/06/15 00:00:00 │ [2] 05/06/15; 00:0…│       │ UNKNOWN       
 DELTA AIR LINES    │ A-320        │ 05/07/15 00:00:00 │ [2] 05/07/15; 00:0…│ CA    │ METRO OAKLAN… 
 DELTA AIR LINES    │ A-320        │ 05/08/15 00:00:00 │ [2] 05/08/15; 00:0…│ UT    │ SALT LAKE CI… 
 LUFTHANSA          │ A-380        │ 05/10/15 00:00:00 │ [2] 05/10/15; 00:0…│ TX    │ GEORGE BUSH … 
 BUSINESS           │ C-172        │ 05/08/15 00:00:00 │ [2] 05/08/15; 00:0…│ FL    │ ORLANDO SANF… 
 SPIRIT AIRLINES    │ A-319        │ 05/10/15 00:00:00 │ [2] 05/10/15; 00:0…│ IL    │ CHICAGO O'HA… 
1› faa-wildlife-strikes|                                      :   addcol-split      73448 rows  [M]
</pre>


Each value in the new column is a list of the pieces that resulted from the split. But you probably want them each piece in its own column. To do that press `(`, which is the \"expand column\" command. Now you should see something like this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 OPERATOR           │ ATYPE        │ INCIDENT_DATE     │ INCIDENT_DATE_re[0]│ INCIDENT_DATE_re[1]│>
 BUSINESS           │ PA-28        │ 05/22/15 00:00:00 │ 05/22/15           │ 00:00:00           │F 
 BUSINESS           │ BE-1900      │ 06/18/15 00:00:00 │ 06/18/15           │ 00:00:00           │A 
 BUSINESS           │ PA-46 MALIBU │ 09/20/15 00:00:00 │ 09/20/15           │ 00:00:00           │T 
 DELTA AIR LINES    │ B-717-200    │ 11/07/15 00:00:00 │ 11/07/15           │ 00:00:00           │M 
 BUSINESS           │ BE-90 KING   │ 12/17/15 00:00:00 │ 12/17/15           │ 00:00:00           │F 
 DELTA AIR LINES    │ B-757        │ 07/17/15 00:00:00 │ 07/17/15           │ 00:00:00           │V 
 DELTA AIR LINES    │ B-717-200    │ 08/02/15 00:00:00 │ 08/02/15           │ 00:00:00           │T 
 BUSINESS           │ C-414        │ 08/03/15 00:00:00 │ 08/03/15           │ 00:00:00           │T 
 ALLEGIANT AIR      │ MD-80        │ 09/02/15 00:00:00 │ 09/02/15           │ 00:00:00           │F 
 TRANS STATES AIRLI…│ EMB-145      │ 09/07/15 00:00:00 │ 09/07/15           │ 00:00:00           │M 
 BUSINESS           │ C-172        │ 11/28/15 00:00:00 │ 11/28/15           │ 00:00:00           │F 
 GOVERNMENT         │ EC120        │ 12/08/15 00:00:00 │ 12/08/15           │ 00:00:00           │C 
 AMERICAN AIRLINES  │ A-321        │ 05/06/15 00:00:00 │ 05/06/15           │ 00:00:00           │F 
 EXPRESSJET AIRLINES│ CRJ100/200   │ 05/06/15 00:00:00 │ 05/06/15           │ 00:00:00           │A 
 MESA AIRLINES      │ CRJ900       │ 05/08/15 00:00:00 │ 05/08/15           │ 00:00:00           │A 
 BUSINESS           │ HELICOPTER   │ 05/06/15 00:00:00 │ 05/06/15           │ 00:00:00           │  
 DELTA AIR LINES    │ A-320        │ 05/07/15 00:00:00 │ 05/07/15           │ 00:00:00           │C 
 DELTA AIR LINES    │ A-320        │ 05/08/15 00:00:00 │ 05/08/15           │ 00:00:00           │U 
 LUFTHANSA          │ A-380        │ 05/10/15 00:00:00 │ 05/10/15           │ 00:00:00           │T 
 BUSINESS           │ C-172        │ 05/08/15 00:00:00 │ 05/08/15           │ 00:00:00           │F 
 SPIRIT AIRLINES    │ A-319        │ 05/10/15 00:00:00 │ 05/10/15           │ 00:00:00           │I 
1› faa-wildlife-strikes|                                        (   expand-col      73448 rows  [M]
</pre>




## How to create a new column by \"capturing\" it from another column

:::: note
::: title
Note

This approach requires a bit more knowlege of \"regular expressions\". If you\'re unfamiliar with regular expressions and don\'t want to learn them right now, feel free to skip to the next chapter.

Just like you can split a column by using `:`, you can extract part of a column into a new column by using `;`.

For instance, if you want to extract the first string of numbers from each aircraft type, (e.g., `28` from `PA-28`, `46` from `PA-46 MALIBU`, and `717` from `B-717-200`). To do that, take the following steps:

- Navigate to the `ATYPE` column
- Press `;`
- At the prompt, type `(\d+)` (with one set of parentheses for each capture group), and then hit `Enter`
- Press `(` to expand the new column\'s lists

Once you do that, you should see something like this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 OPERATOR           │ ATYPE        │ ATYPE_re │ INCIDENT_DATE     │ STATE │ AIRPORT            │ P>
 BUSINESS           │ PA-28        │ [1] 28   │ 05/22/15 00:00:00 │ FL    │ VERO BEACH MUNICIP…│ A… 
 BUSINESS           │ BE-1900      │ [1] 1900 │ 06/18/15 00:00:00 │ AK    │ KENAI MUNICIPAL AR…│ A… 
 BUSINESS           │ PA-46 MALIBU │ [1] 46   │ 09/20/15 00:00:00 │ TX    │ DAVID WAYNE HOOKS …│    
 DELTA AIR LINES    │ B-717-200    │ [1] 717  │ 11/07/15 00:00:00 │ MO    │ LAMBERT-ST LOUIS I…│ A… 
 BUSINESS           │ BE-90 KING   │ [1] 90   │ 12/17/15 00:00:00 │ FL    │ POMPANO BEACH AIRP…│ L… 
 DELTA AIR LINES    │ B-757        │ [1] 757  │ 07/17/15 00:00:00 │ VI    │ HENRY E ROHLSEN AR…│    
 DELTA AIR LINES    │ B-717-200    │ [1] 717  │ 08/02/15 00:00:00 │ TX    │ SAN ANTONIO INTL   │ A… 
 BUSINESS           │ C-414        │ [1] 414  │ 08/03/15 00:00:00 │ TX    │ LONE STAR EXECUTIV…│ D… 
 ALLEGIANT AIR      │ MD-80        │ [1] 80   │ 09/02/15 00:00:00 │ FL    │ TAMPA INTL         │ A… 
 TRANS STATES AIRLI…│ EMB-145      │ [1] 145  │ 09/07/15 00:00:00 │ MO    │ LAMBERT-ST LOUIS I…│ A… 
 BUSINESS           │ C-172        │ [1] 172  │ 11/28/15 00:00:00 │ FL    │ OPA-LOCKA EXECUTIV…│ A… 
 GOVERNMENT         │ EC120        │ [1] 120  │ 12/08/15 00:00:00 │ CA    │ NORMAN Y. MINETA S…│    
 AMERICAN AIRLINES  │ A-321        │ [1] 321  │ 05/06/15 00:00:00 │ FL    │ FORT LAUDERDALE/HO…│ A… 
 EXPRESSJET AIRLINES│ CRJ100/200   │ [1] 100  │ 05/06/15 00:00:00 │ AR    │ FORT SMITH REGIONA…│ C… 
 MESA AIRLINES      │ CRJ900       │ [1] 900  │ 05/08/15 00:00:00 │ AR    │ BILL AND  HILLARY …│ L… 
 BUSINESS           │ HELICOPTER   │         ⌀│ 05/06/15 00:00:00 │       │ UNKNOWN            │ E… 
 DELTA AIR LINES    │ A-320        │ [1] 320  │ 05/07/15 00:00:00 │ CA    │ METRO OAKLAND INTL │    
 DELTA AIR LINES    │ A-320        │ [1] 320  │ 05/08/15 00:00:00 │ UT    │ SALT LAKE CITY INTL│    
 LUFTHANSA          │ A-380        │ [1] 380  │ 05/10/15 00:00:00 │ TX    │ GEORGE BUSH INTERC…│ C… 
 BUSINESS           │ C-172        │ [1] 172  │ 05/08/15 00:00:00 │ FL    │ ORLANDO SANFORD IN…│ A… 
 SPIRIT AIRLINES    │ A-319        │ [1] 319  │ 05/10/15 00:00:00 │ IL    │ CHICAGO O'HARE INT…│ C… 
1› faa-wildlife-strikes|                            processing… (   expand-col      73448 rows  [M]
</pre>



## The sheet-joining three-step

To join two or more sheets in VisiData, you\'ll do the following:

1.  In the sheets you want to join, **mark the shared columns as \"keys\"**
2.  In the Sheets Sheet, **select the sheets you want to join**
3.  Press `&` to open the join-choice prompt, **type your desired join type** (or press `Control-x` to open the interactive chooser) and press `Enter`

VisiData supports seven types of joins:

  Join command   SQL equivalent      Description
  -------------- ------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  inner          `LEFT INNER JOIN`   Keeps only rows which match keys on all sheets
  outer          `LEFT OUTER JOIN`   Keeps all rows from first selected sheet
  full           `FULL OUTER JOIN`   Keeps all rows from all sheets (union)
  diff                               Keeps only rows NOT in all sheets
  append         `UNION ALL`         Keeps all rows from all sheets (concatenation)
  extend                             Copies first selected sheet, keeping all rows and sheet type, and extends with columns from other sheets
  merge                              Merges differences from other sheets into first sheet; keeps all rows from first sheet, updating any False-y values (e.g., `False`, `None`, `0`, `[]`) with non-False-y values from subsequent sheets, and adds unique rows from subsequent sheets

(Descriptions above come from VisiData\'s [Quick Reference](http://visidata.org/man/).)



## Practical example

To see an example of joining in action, see the [Distinctive Birds](../../practical/distinctive-birds/) chapter.


## Enabling multiline mode

By default, VisiData displays each row on a single line. You can switch to multiline mode (and toggle back out of it) by pressing `v`. Here\'s what that looks like:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
<PERSON │ REMAINS_COLLECTED │ REMARKS                                                              
 Tower  │ 0                 │ N9240F was right base to final on Runway 4, and he reported a bird   ║
                              strike to the left wing.  He did not need any assistance.  He landed ║
                              and taxied to the ramp, and said there was only minor damage done to ║
                              the left wing.                                                       ║
 Tower  │ 0                 │ ON FINAL, PILOT REPORTED HEARING IMPACT. AFTER LANDING AND           ║
                              INSPECTING AIRCRAFT, PILOT DISCOVERED DENT IN TIRE BOOT. UPON RUNWAY ║
                              INSPECTION A BIRD CARCASS WAS FOUND ON RUNWAY NORTH OF TAXIWAY       ║
                              DELTA.                                                               ║
 Tower  │ 0                 │ N952G, P46T/G, bird strike, no injuries reported, damage to vortex   ║
                              generator, pilot's name is Robert Nipper, 713-539-0797.              ║
                                                                                                   ║
                                                                                                   ║
 Tower  │ 0                 │ NO EMERGENCY: AFTER THE AIRCRAFT WAS AT THE GATE THE PILOT OF DAL939 ║
                              ADVISED THAT THEY HAD A BIRD STRIKE ON A 2 MILE FINAL TO RWY30R. A   ║
                              BIRD STRUCK THE RIGHT WING AND THE LANDING LIGHT. THE LANDING LIGHT  ║
                              WAS SHATTERED AND THERE WAS NO DAMAGE ON THE RIGHT                   ║
 Tower  │ 0                 │ MEDFLY1, A BE9L, VFR, LANDED RY 15. UPON CONTACTING GC, PILOT        ║
                              ADVISED HE HAD EXPERIENCED A BIRD STRIKE AND REQUESTED INSTRUCTIONS  ║
                              TO TAXI TO THE RAMP TO INSPECT THE ACFT. THE PILOT CALLED THE TOWER  ║
                              AND ADVISED THE THAT THE AIRCRAFT HAD LIGHT DAMAGE TO THE            ║
 Tower  │ 0                 │ DAL571 EXPERIENCED A BIRD INGESTION ON ARRIVAL TO STT ON JULY 17.    ║
1› faa-wildlife-strikes|                                      v   toggle-multiline      73448 rows 
</pre>


:::: note
::: title
Note

The default row height in multiline mode is 4 lines, but you can adjust this through VisiData\'s `default_height` setting.



## Scrolling within cells

To see more of a cell in single-line mode, you can scroll back and forth within a column using the following commands:

  Keystrokes                            Action
  ------------------------------------- -----------------------------------
  `zh`    Scroll text left
  `zl`    Scroll text right
  `zj`    Scroll text down
  `zk`    Scroll text up
  `gzh`   Scroll back to leftmost character
  `gzk`   Scroll back to topmost character

Here\'s how it looks in practice, starting with the same view as above:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
<PERSON │ REMAINS_COLLECTED │ REMARKS                                                              
 Tower  │ 0                 │ N9240F was right base to final on Runway 4, and he reported a bird s…║
 Tower  │ 0                 │ ON FINAL, PILOT REPORTED HEARING IMPACT. AFTER LANDING AND INSPECTIN…║
 Tower  │ 0                 │ N952G, P46T/G, bird strike, no injuries reported, damage to vortex g…║
 Tower  │ 0                 │ NO EMERGENCY: AFTER THE AIRCRAFT WAS AT THE GATE THE PILOT OF DAL939…║
 Tower  │ 0                 │ MEDFLY1, A BE9L, VFR, LANDED RY 15. UPON CONTACTING GC, PILOT ADVISE…║
 Tower  │ 0                 │ DAL571 EXPERIENCED A BIRD INGESTION ON ARRIVAL TO STT ON JULY 17. TH…║
 Tower  │ 0                 │ DAL1356 ADVISED LOCAL CONTROL OF A BIRD STRIKE SHORT FINAL/OVER THE …║
 Tower  │ 0                 │ N999RK WAS DEPARTING TO 87I AND ON DEPARTURE STRUCK A BIRD AND IT WA…║
 Tower  │ 0                 │ AAY843,MD80, ADVSD TPA APCH HE ENCOUNTERED BIRD STRIKE ON RADOME, BE…║
 Tower  │ 0                 │ LOF3351 hit a large bird, thought it was an owl, over the threshold,…║
 Tower  │ 0                 │ N5352K EXPERIENCED A BIRD STRIKE ON A 3-MILE FINAL FOR RWY 9R. THE A…║
 Tower  │ 0                 │ POLICE1 reported being struck by a seagull on the left front side of…║
 Tower  │ 0                 │ PILOT OF AAL1702 REPORTED BIRD STRIKE ON FINAL FOR RUNWAY 10L AT 150…║
 Tower  │ 0                 │ ASQ2607 REPORTED A BIRD STRIKE DURING TAKE OFF. PILOT STATED IT WAS …║
 Tower  │ 0                 │ ASH5753 WAS CLEARED TO LAND ON RY22L WHEN THEY HIT A BIRD IN THE FLA…║
 Tower  │ 0                 │ CMD8 BIRD STRIKE.  NEGATIVE EMERGENCY. MAKING PRECAUTIONARY LANDING …║
 Tower  │ 0                 │ DAL 1253-BIRD STRIKE REPORTED AFTER LANDING.                         ║
 Tower  │ 0                 │ Delta Airlines called to report a birdstrike on DAL2384 who had arri…║
 Tower  │ 0                 │ DLH441 reported receiving bird strikes climbing through 100 approxim…║
 Tower  │ 0                 │ AIRCRAFT ENCOUNTERED BIRD STRIKE OUTSIDE 5 MILES OF SFB WHILE ON APP…║
 Tower  │ 0                 │ Aircraft reported bird strike climbing out of 12000ft and requested …║
1› faa-wildlife-strikes|                                      v   toggle-multiline      73448 rows 
</pre>


After typing `zh`, the `REMARKS` column now looks like this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
<PERSON │ REMAINS_COLLECTED │ REMARKS                                                              
 Tower  │ 0                 │…trike to the left wing.  He did not need any assistance.  He landed …║
 Tower  │ 0                 │…G AIRCRAFT, PILOT DISCOVERED DENT IN TIRE BOOT. UPON RUNWAY INSPECTI…║
 Tower  │ 0                 │…enerator, pilot's name is Robert Nipper, 713-539-0797.               ║
 Tower  │ 0                 │… ADVISED THAT THEY HAD A BIRD STRIKE ON A 2 MILE FINAL TO RWY30R. A …║
 Tower  │ 0                 │…D HE HAD EXPERIENCED A BIRD STRIKE AND REQUESTED INSTRUCTIONS TO TAX…║
 Tower  │ 0                 │…E PILOT DID NOT REPORT A BIRD STRIKE TO THE ATCT. THE ATCT DID NOT F…║
 Tower  │ 0                 │…NUMBERS TO RY12R.  THE B717 LANDED WITHOUT INCIDENT.  PILOT ADVISED …║
 Tower  │ 0                 │…S INJESTED INTO THE RIGHT ENGINE. THE AIRCRAFT HAD MADE A PRECAUTION…║
 Tower  │ 0                 │…LOW 1ST OFFICERS' WINDOW, 30 NNE PIE AT 6,000 FT. PILOT KEVIN VAN TA…║
 Tower  │ 0                 │… taxied in and his taxi light was not working.                       ║
 Tower  │ 0                 │…IRCRAFT LANDED WITHOUT INCIDENT. THE STUDENT THINKS IT WAS A LARGER …║
 Tower  │ 0                 │… the windshield. Pilot: Chris Dominguez, (408) 219-8588, Moderate to…║
 Tower  │ 0                 │…0FT. NO DAMAGE REPORTED. SMALL BIRD ON WINDSHIELD.                   ║
 Tower  │ 0                 │…A SMALL BIRD. NO DAMAGE WAS REPORTED. ASQ2607 CLIMB WITHOUT ISSUE AN…║
 Tower  │ 0                 │…RE OVER THE RUNWAY.  BIRD WAS DESCRIBED AS SMALL AND BLACK.  RY OPS …║
 Tower  │ 0                 │…AT OAK.                                                              ║
 Tower  │ 0                 │…                                                                     ║
 Tower  │ 0                 │…ved RWY16R.                                                          ║
 Tower  │ 0                 │…ately 13 miles east of IAH. The aircraft was IMC and unable to deter…║
 Tower  │ 0                 │…ROACH CONTROL FREQUENCY. AIRCRAFT RETURNED BACK TO SFB AND LANDED RW…║
 Tower  │ 0                 │…leveling at 13000. Declared emergency with stall indication in one e…║
1› faa-wildlife-strikes|                                   zl   scroll-cells-right      73448 rows 
</pre>



## Diving into cells

Pressing `z` + `Enter` \"dives\" into your current cell, opening a \"Text Sheet\" that contains only that cell\'s value:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 text                                                                                              
 N9240F was right base to final on Runway 4, and he reported a bird strike to the left wing.  He d… 


2› faa-wildlife-strikes[0].REMARKS|                                     zEnter             1 lines 
</pre>


If your cell\'s value contains newlines, they\'ll appear as such in the Text Sheet. From a Text Sheet, you also can press `Control-o` to open the cell in your terminal\'s default text editor.

:::: tip
::: title
Tip

Similarly, whenever you\'re editing a cell within VisiData (i.e., via the `e` command), you can also run `Control-o` to open that cell in your terminal\'s default text editor.



## Select a random sample of rows

In VisiData, you can create a randomly-sampled copy of any sheet. To create a random-sample sheet, press `Space` to initiate the longname-command prompt, and type `random-rows`. At the prompt, type the number of rows you\'d like to include, and then press `Enter`.


## Only load part of the file

If you\'re only using VisiData to preview a dataset, consider loading just the beginning of the file.

### From the command-line

If you\'re working with a simple CSV file, you can accomplish this by using `head` on the command-line, combined with `vd -f csv` e.g.,:

    head -n 1000 faa-wildlife-strikes.csv | vd -f csv

That will load the first 1,000 lines of the file. (Because the `REMARKS` column contains some newline characters, the 1,000 lines correspond to slightly fewer than 1,000 rows.)

Alternatively, you can use a written-for-speed tool, such as [xsv](https://github.com/BurntSushi/xsv), to slice or filter the file before loading it into VisiData. E.g.,:

    xsv search "CHICAGO" faa-wildlife-strikes.csv | vd -f csv

### By halting the loading process

You can also just press `Control-c` while the data is loading, which will halt the loading process. VisiData handles this gracefully, and you can continue using the program just as you would if you hadn\'t halted the loading proces.

This approach works well if you\'re using a data source that\'s more complex than a CSV file, and if you don\'t care exactly how many lines are loaded.



## Caching dynamic columns

Dynamic columns (for instance, those created with the `=` command) are calculated \"lazily\" --- i.e., only when they\'re needed.

If you\'re running a lot of operations on a dynamic column --- perhaps calculating its average, median, and sum --- you can save some time by first \"caching\" it. When you cache a dynamic column, VisiData calculates its current state and never recomputes it.

To cache (or re-cache) a column, navigate to it in your sheet and type `z'`.


## Creating pivot tables

VisiData\'s pivot tables are similar to pivot tables you might have created in various spreadsheet programs. Pivot tables create a cross-tabulation of two or more columns in a dataset.

In VisiData, creating a pivot table involves the following steps:

- Use `!` to designate the column(s) you want to serve as the pivot table\'s rows.
- *Optional*: Use `+` to specify additional metrics you want the pivot table to calculate. (By default, the pivot table\'s sole metric will be the overall count for each grouping.)
- Navigate to the column you want to serve as the pivot table\'s columns.
- Press `Shift-W`

Let\'s say we want to cross-tabulate species by whether their remains were collected. First, let\'s designate the `SPECIES` column as a key column:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 SPECIES            ║<STATE │ AIRPORT            │ PHASE_OF_FLT │ HEIGHT │ SPEED │ BIRDS_STRUCK │ >
 Unknown bird       ║ FL    │ VERO BEACH MUNICIP…│ APPROACH     │        │       │ 1            │ N 
 Unknown bird       ║ AK    │ KENAI MUNICIPAL AR…│ APPROACH     │        │       │ 1            │ N 
 Unknown bird       ║ TX    │ DAVID WAYNE HOOKS …│              │        │       │ 1            │ N 
 Unknown bird       ║ MO    │ LAMBERT-ST LOUIS I…│ APPROACH     │        │       │ 1            │ N 
 Unknown bird       ║ FL    │ POMPANO BEACH AIRP…│ LANDING ROLL │ 0      │       │ 1            │   
 Unknown bird       ║ VI    │ HENRY E ROHLSEN AR…│              │        │       │ 1            │ O 
 Unknown bird       ║ TX    │ SAN ANTONIO INTL   │ APPROACH     │        │       │ 1            │ N 
 Unknown bird       ║ TX    │ LONE STAR EXECUTIV…│ DEPARTURE    │        │       │ 1            │ P 
 Unknown bird       ║ FL    │ TAMPA INTL         │ APPROACH     │ 6000   │       │ 1            │ N 
 Owls               ║ MO    │ LAMBERT-ST LOUIS I…│ APPROACH     │        │       │ 1            │ N 
 Hawks              ║ FL    │ OPA-LOCKA EXECUTIV…│ APPROACH     │        │       │ 1            │ N 
 Gulls              ║ CA    │ NORMAN Y. MINETA S…│              │        │       │ 1            │ N 
 Unknown bird - sma…║ FL    │ FORT LAUDERDALE/HO…│ APPROACH     │ 1500   │       │ 1            │ N 
 Unknown bird - sma…║ AR    │ FORT SMITH REGIONA…│ CLIMB        │        │       │ 1            │ N 
 Unknown bird - sma…║ AR    │ BILL AND  HILLARY …│ LANDING ROLL │ 0      │       │ 1            │ N 
 Unknown bird       ║       │ UNKNOWN            │ En Route     │        │       │ 1            │ P 
 Unknown bird       ║ CA    │ METRO OAKLAND INTL │              │        │       │ 1            │ N 
 Unknown bird       ║ UT    │ SALT LAKE CITY INTL│              │        │       │ 1            │ N 
 Unknown bird       ║ TX    │ GEORGE BUSH INTERC…│ CLIMB        │        │       │ 1            │ N 
 Unknown bird       ║ FL    │ ORLANDO SANFORD IN…│ APPROACH     │        │       │ 1            │ N 
 Unknown bird       ║ IL    │ CHICAGO O'HARE INT…│ CLIMB        │ 12000  │       │ 1            │ P 
1› faa-wildlife-strikes|                                               !   key-col      73448 rows 
</pre>


Then, navigate to the `REMAINS_COLLECTED` column, either by tapping `l` or the right-arrow until we get there, or by typing `c` followed by `REMAINS` and then `Enter`:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 SPECIES            ║<EFFECT             │ DAMAGE │ COST_REPAIRS │ PERSON │ REMAINS_COLLECTED │ RE…
 Unknown bird       ║ NONE               │ M      │              │ Tower  │ 0                 │ N9… 
 Unknown bird       ║ NONE               │ M      │              │ Tower  │ 0                 │ ON… 
 Unknown bird       ║ NONE               │ M      │              │ Tower  │ 0                 │ N9… 
 Unknown bird       ║ NONE               │ M      │              │ Tower  │ 0                 │ NO… 
 Unknown bird       ║                    │ M      │              │ Tower  │ 0                 │ ME… 
 Unknown bird       ║ Other              │ M?     │              │ Tower  │ 0                 │ DA… 
 Unknown bird       ║ NONE               │ M?     │              │ Tower  │ 0                 │ DA… 
 Unknown bird       ║ PRECAUTIONARY LAND…│ M?     │              │ Tower  │ 0                 │ N9… 
 Unknown bird       ║ NONE               │ M?     │              │ Tower  │ 0                 │ AA… 
 Owls               ║ NONE               │ M?     │              │ Tower  │ 0                 │ LO… 
 Hawks              ║ NONE               │ M?     │              │ Tower  │ 0                 │ N5… 
 Gulls              ║ NONE               │ M?     │              │ Tower  │ 0                 │ PO… 
 Unknown bird - sma…║ NONE               │ N      │              │ Tower  │ 0                 │ PI… 
 Unknown bird - sma…║ NONE               │ N      │              │ Tower  │ 0                 │ AS… 
 Unknown bird - sma…║ NONE               │ N      │              │ Tower  │ 0                 │ AS… 
 Unknown bird       ║ PRECAUTIONARY LAND…│ N      │              │ Tower  │ 0                 │ CM… 
 Unknown bird       ║ NONE               │ N      │              │ Tower  │ 0                 │ DA… 
 Unknown bird       ║ NONE               │ N      │              │ Tower  │ 0                 │ De… 
 Unknown bird       ║ NONE               │ N      │              │ Tower  │ 0                 │ DL… 
 Unknown bird       ║ NONE               │ N      │              │ Tower  │ 0                 │ AI… 
 Unknown bird       ║ PRECAUTIONARY LAND…│ N      │              │ Tower  │ 0                 │ Ai… 
1› faa-wildlife-strikes|                                          c   go-col-regex      73448 rows 
</pre>


Now, press `Shift+W` to create the pivot table:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 SPECIES            ║ 0   #│ 1   #║                                                                
 Unknown bird       ║ 6677 │  393 ║
 Owls               ║   36 │   23 ║
 Hawks              ║  202 │  106 ║
 Gulls              ║  559 │  525 ║
 Unknown bird - sma…║ 12544│ 1523 ║
 Sparrows           ║  346 │  542 ║
 Sandhill crane     ║   15 │   26 ║
 Unknown bird - med…║ 3585 │  322 ║
 Unknown bird - lar…║  769 │   58 ║
 Barn swallow       ║  246 │ 2838 ║
 Rock pigeon        ║  149 │ 1008 ║
 Barn owl           ║   22 │  517 ║
 Bank swallow       ║   14 │  267 ║
 Swallows           ║  152 │  302 ║
 Horned lark        ║   56 │ 2634 ║
 Northern pintail   ║    0 │   93 ║
 American robin     ║   32 │  644 ║
 American kestrel   ║   81 │ 2506 ║
 Microbats          ║   43 │  443 ║
 Mourning dove      ║  200 │ 3909 ║
 Free-tailed bats   ║    1 │   50 ║
2› faa-wildlife-strikes_pivot_REMAINS_COLLECTED_count|          Shift+W           641 grouped rows 
</pre>


\... and `g_` to auto-adjust the column widths:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 SPECIES               ║ 0    #│ 1   #║                                                            
 Unknown bird          ║  6677 │  393 ║
 Owls                  ║    36 │   23 ║
 Hawks                 ║   202 │  106 ║
 Gulls                 ║   559 │  525 ║
 Unknown bird - small  ║ 12544 │ 1523 ║
 Sparrows              ║   346 │  542 ║
 Sandhill crane        ║    15 │   26 ║
 Unknown bird - medium ║  3585 │  322 ║
 Unknown bird - large  ║   769 │   58 ║
 Barn swallow          ║   246 │ 2838 ║
 Rock pigeon           ║   149 │ 1008 ║
 Barn owl              ║    22 │  517 ║
 Bank swallow          ║    14 │  267 ║
 Swallows              ║   152 │  302 ║
 Horned lark           ║    56 │ 2634 ║
 Northern pintail      ║     0 │   93 ║
 American robin        ║    32 │  644 ║
 American kestrel      ║    81 │ 2506 ║
 Microbats             ║    43 │  443 ║
 Mourning dove         ║   200 │ 3909 ║
 Free-tailed bats      ║     1 │   50 ║
2› faa-wildlife-strikes_pivot_REMAINS_COLLECTED_count g_   resize-cols-max        641 grouped rows 
</pre>


The rows of the pivot table represent each species, while the columns represent the number of rows for each species that fall into each `REMAINS_COLLECTED` category.

This is a simple pivot table, since `REMAINS_COLLECTED` can only be either `0` or `1`, but pivot tables on more complex columns can end up much wider.

:::: note
::: title
Note

The order of the columns in a pivot table is based on the order the relevant values appear in the source sheet. If you want them to appear, instead, in alphabetical order, sort the source sheet\'s relevant column(s) first.



## Melting datasets

To \"melt\" a dataset is to reshape it from a \"wide\" format to a \"long\" one, specifically by converting each value in each column into its own row. If that concept is unfamiliar, the example below should help clarify.

Melting a dataset in VisiData involves the following steps:

- *Optional*: Use `!` to designate the column(s) you want to keep unmelted.
- *Optional*: Use `-` to hide the columns you don\'t want to appear, at all, in the melted sheet.
- Press `Shift+M`

If you skip the optional steps, pressing `Shift-M` on the original `faa-wildlife-strikes.csv` dataset creates this melted sheet:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 Variable          │ Value                                                                         
 OPERATOR          │ BUSINESS                                                                       
 ATYPE             │ PA-28                                                                          
 INCIDENT_DATE     │ 05/22/15 00:00:00                                                              
 STATE             │ FL                                                                             
 AIRPORT           │ VERO BEACH MUNICIPAL                                                           
 PHASE_OF_FLT      │ APPROACH                                                                       
 HEIGHT            │                                                                                
 SPEED             │                                                                                
 SPECIES           │ Unknown bird                                                                   
 BIRDS_STRUCK      │ 1                                                                              
 EFFECT            │ NONE                                                                           
 DAMAGE            │ M                                                                              
 COST_REPAIRS      │                                                                                
 PERSON            │ Tower                                                                          
 REMAINS_COLLECTED │ 0                                                                              
 REMARKS           │ N9240F was right base to final on Runway 4, and he reported a bird strike to … 
 OPERATOR          │ BUSINESS                                                                       
 ATYPE             │ BE-1900                                                                        
 INCIDENT_DATE     │ 06/18/15 00:00:00                                                              
 STATE             │ AK                                                                             
 AIRPORT           │ KENAI MUNICIPAL ARPT                                                           
3› faa-wildlife-strikes_melted|                                Shift+M       1175168 melted values 
</pre>


Now let\'s examine how the optional steps affect melting. Press `q` to return to the source sheet, and press `!` on each of the first two columns (`OPERATOR` and `ATYPE`):


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 OPERATOR           │ ATYPE        ║ INCIDENT_DATE     │ STATE │ AIRPORT            │ PHASE_OF_FLT>
 BUSINESS           │ PA-28        ║ 05/22/15 00:00:00 │ FL    │ VERO BEACH MUNICIP…│ APPROACH     │
 BUSINESS           │ BE-1900      ║ 06/18/15 00:00:00 │ AK    │ KENAI MUNICIPAL AR…│ APPROACH     │
 BUSINESS           │ PA-46 MALIBU ║ 09/20/15 00:00:00 │ TX    │ DAVID WAYNE HOOKS …│              │
 DELTA AIR LINES    │ B-717-200    ║ 11/07/15 00:00:00 │ MO    │ LAMBERT-ST LOUIS I…│ APPROACH     │
 BUSINESS           │ BE-90 KING   ║ 12/17/15 00:00:00 │ FL    │ POMPANO BEACH AIRP…│ LANDING ROLL │
 DELTA AIR LINES    │ B-757        ║ 07/17/15 00:00:00 │ VI    │ HENRY E ROHLSEN AR…│              │
 DELTA AIR LINES    │ B-717-200    ║ 08/02/15 00:00:00 │ TX    │ SAN ANTONIO INTL   │ APPROACH     │
 BUSINESS           │ C-414        ║ 08/03/15 00:00:00 │ TX    │ LONE STAR EXECUTIV…│ DEPARTURE    │
 ALLEGIANT AIR      │ MD-80        ║ 09/02/15 00:00:00 │ FL    │ TAMPA INTL         │ APPROACH     │
 TRANS STATES AIRLI…│ EMB-145      ║ 09/07/15 00:00:00 │ MO    │ LAMBERT-ST LOUIS I…│ APPROACH     │
 BUSINESS           │ C-172        ║ 11/28/15 00:00:00 │ FL    │ OPA-LOCKA EXECUTIV…│ APPROACH     │
 GOVERNMENT         │ EC120        ║ 12/08/15 00:00:00 │ CA    │ NORMAN Y. MINETA S…│              │
 AMERICAN AIRLINES  │ A-321        ║ 05/06/15 00:00:00 │ FL    │ FORT LAUDERDALE/HO…│ APPROACH     │
 EXPRESSJET AIRLINES│ CRJ100/200   ║ 05/06/15 00:00:00 │ AR    │ FORT SMITH REGIONA…│ CLIMB        │
 MESA AIRLINES      │ CRJ900       ║ 05/08/15 00:00:00 │ AR    │ BILL AND  HILLARY …│ LANDING ROLL │
 BUSINESS           │ HELICOPTER   ║ 05/06/15 00:00:00 │       │ UNKNOWN            │ En Route     │
 DELTA AIR LINES    │ A-320        ║ 05/07/15 00:00:00 │ CA    │ METRO OAKLAND INTL │              │
 DELTA AIR LINES    │ A-320        ║ 05/08/15 00:00:00 │ UT    │ SALT LAKE CITY INTL│              │
 LUFTHANSA          │ A-380        ║ 05/10/15 00:00:00 │ TX    │ GEORGE BUSH INTERC…│ CLIMB        │
 BUSINESS           │ C-172        ║ 05/08/15 00:00:00 │ FL    │ ORLANDO SANFORD IN…│ APPROACH     │
 SPIRIT AIRLINES    │ A-319        ║ 05/10/15 00:00:00 │ IL    │ CHICAGO O'HARE INT…│ CLIMB        │
1› faa-wildlife-strikes|                                               !   key-col      73448 rows 
</pre>


Then use `-` (or the Columns Sheet) to hide all the other columns except for `STATE` and `AIRPORT`:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 OPERATOR           │ ATYPE        ║ STATE │ AIRPORT            ║                                  
 BUSINESS           │ PA-28        ║ FL    │ VERO BEACH MUNICIP…║                                   
 BUSINESS           │ BE-1900      ║ AK    │ KENAI MUNICIPAL AR…║                                   
 BUSINESS           │ PA-46 MALIBU ║ TX    │ DAVID WAYNE HOOKS …║                                   
 DELTA AIR LINES    │ B-717-200    ║ MO    │ LAMBERT-ST LOUIS I…║                                   
 BUSINESS           │ BE-90 KING   ║ FL    │ POMPANO BEACH AIRP…║                                   
 DELTA AIR LINES    │ B-757        ║ VI    │ HENRY E ROHLSEN AR…║                                   
 DELTA AIR LINES    │ B-717-200    ║ TX    │ SAN ANTONIO INTL   ║                                   
 BUSINESS           │ C-414        ║ TX    │ LONE STAR EXECUTIV…║                                   
 ALLEGIANT AIR      │ MD-80        ║ FL    │ TAMPA INTL         ║                                   
 TRANS STATES AIRLI…│ EMB-145      ║ MO    │ LAMBERT-ST LOUIS I…║                                   
 BUSINESS           │ C-172        ║ FL    │ OPA-LOCKA EXECUTIV…║                                   
 GOVERNMENT         │ EC120        ║ CA    │ NORMAN Y. MINETA S…║                                   
 AMERICAN AIRLINES  │ A-321        ║ FL    │ FORT LAUDERDALE/HO…║                                   
 EXPRESSJET AIRLINES│ CRJ100/200   ║ AR    │ FORT SMITH REGIONA…║                                   
 MESA AIRLINES      │ CRJ900       ║ AR    │ BILL AND  HILLARY …║                                   
 BUSINESS           │ HELICOPTER   ║       │ UNKNOWN            ║                                   
 DELTA AIR LINES    │ A-320        ║ CA    │ METRO OAKLAND INTL ║                                   
 DELTA AIR LINES    │ A-320        ║ UT    │ SALT LAKE CITY INTL║                                   
 LUFTHANSA          │ A-380        ║ TX    │ GEORGE BUSH INTERC…║                                   
 BUSINESS           │ C-172        ║ FL    │ ORLANDO SANFORD IN…║                                   
 SPIRIT AIRLINES    │ A-319        ║ IL    │ CHICAGO O'HARE INT…║                                   
1› faa-wildlife-strikes|                                          gh   go-leftmost      73448 rows 
</pre>


Now press `Shift-M`. In the resulting melted sheet, `OPERATOR` and `ATYPE` (the columns you keyed with `!`) are preserved as standard columns while `STATE` and `AIRPORT` have been converted to `Variable-Value` pairs:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 OPERATOR           │ ATYPE        ║ Variable │ Value                           ║                  
 BUSINESS           │ PA-28        ║ STATE    │ FL                              ║                   
 BUSINESS           │ PA-28        ║ AIRPORT  │ VERO BEACH MUNICIPAL            ║                   
 BUSINESS           │ BE-1900      ║ STATE    │ AK                              ║                   
 BUSINESS           │ BE-1900      ║ AIRPORT  │ KENAI MUNICIPAL ARPT            ║                   
 BUSINESS           │ PA-46 MALIBU ║ STATE    │ TX                              ║                   
 BUSINESS           │ PA-46 MALIBU ║ AIRPORT  │ DAVID WAYNE HOOKS MEMORIAL ARPT ║                   
 DELTA AIR LINES    │ B-717-200    ║ STATE    │ MO                              ║                   
 DELTA AIR LINES    │ B-717-200    ║ AIRPORT  │ LAMBERT-ST LOUIS INTL           ║                   
 BUSINESS           │ BE-90 KING   ║ STATE    │ FL                              ║                   
 BUSINESS           │ BE-90 KING   ║ AIRPORT  │ POMPANO BEACH AIRPARK           ║                   
 DELTA AIR LINES    │ B-757        ║ STATE    │ VI                              ║                   
 DELTA AIR LINES    │ B-757        ║ AIRPORT  │ HENRY E ROHLSEN ARPT            ║                   
 DELTA AIR LINES    │ B-717-200    ║ STATE    │ TX                              ║                   
 DELTA AIR LINES    │ B-717-200    ║ AIRPORT  │ SAN ANTONIO INTL                ║                   
 BUSINESS           │ C-414        ║ STATE    │ TX                              ║                   
 BUSINESS           │ C-414        ║ AIRPORT  │ LONE STAR EXECUTIVE ARPT        ║                   
 ALLEGIANT AIR      │ MD-80        ║ STATE    │ FL                              ║                   
 ALLEGIANT AIR      │ MD-80        ║ AIRPORT  │ TAMPA INTL                      ║                   
 TRANS STATES AIRLI…│ EMB-145      ║ STATE    │ MO                              ║                   
 TRANS STATES AIRLI…│ EMB-145      ║ AIRPORT  │ LAMBERT-ST LOUIS INTL           ║                   
 BUSINESS           │ C-172        ║ STATE    │ FL                              ║                   
4› faa-wildlife-strikes_melted|                                Shift+M        146896 melted values 
</pre>



## Transposing columns and rows

In VisiData, you can press `Shift-T` to \"transpose\" any given sheet, essentially rotating the struture 90 degrees, so that the rows are represented as columns (and vice versa).

Pressing `Shift-T` on the original `faa-wildlife-strikes.csv` dataset should give you this result:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
                   ║                    │                    │                    │               >
 OPERATOR          ║ BUSINESS           │ BUSINESS           │ BUSINESS           │ DELTA AIR LINES
 ATYPE             ║ PA-28              │ BE-1900            │ PA-46 MALIBU       │ B-717-200
 INCIDENT_DATE     ║ 05/22/15 00:00:00  │ 06/18/15 00:00:00  │ 09/20/15 00:00:00  │ 11/07/15 00:00…
 STATE             ║ FL                 │ AK                 │ TX                 │ MO
 AIRPORT           ║ VERO BEACH MUNICIP…│ KENAI MUNICIPAL AR…│ DAVID WAYNE HOOKS …│ LAMBERT-ST LOU…
 PHASE_OF_FLT      ║ APPROACH           │ APPROACH           │                    │ APPROACH
 HEIGHT            ║                    │                    │                    │
 SPEED             ║                    │                    │                    │
 SPECIES           ║ Unknown bird       │ Unknown bird       │ Unknown bird       │ Unknown bird
 BIRDS_STRUCK      ║ 1                  │ 1                  │ 1                  │ 1
 EFFECT            ║ NONE               │ NONE               │ NONE               │ NONE
 DAMAGE            ║ M                  │ M                  │ M                  │ M
 COST_REPAIRS      ║                    │                    │                    │
 PERSON            ║ Tower              │ Tower              │ Tower              │ Tower
 REMAINS_COLLECTED ║ 0                  │ 0                  │ 0                  │ 0
 REMARKS           ║ N9240F was right b…│ ON FINAL, PILOT RE…│ N952G, P46T/G, bir…│ NO EMERGENCY: …


5› faa-wildlife-strikes_T|                                  processing… Shift+T            16 rows 
</pre>


If your source sheet has a key column, the values in that column will become the headers for the transposed sheet. For instance, here\'s the frequency table (with `Shift-F`) for the dataset\'s `OPERATOR` column:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 OPERATOR           ║↓count♯│ percent%│ histogram                             ~║                   
 UNKNOWN            ║ 23076 │   31.42 │ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ║
 SOUTHWEST AIRLINES ║  7752 │   10.55 │ ■■■■■■■■■■■■                           ║
 BUSINESS           ║  5868 │    7.99 │ ■■■■■■■■■                              ║
 AMERICAN AIRLINES  ║  4337 │    5.90 │ ■■■■■■■                                ║
 DELTA AIR LINES    ║  2817 │    3.84 │ ■■■■                                   ║
 FEDEX EXPRESS      ║  2709 │    3.69 │ ■■■■                                   ║
 UNITED AIRLINES    ║  2194 │    2.99 │ ■■■                                    ║
 US AIRWAYS         ║  1885 │    2.57 │ ■■■                                    ║
 UPS AIRLINES       ║  1773 │    2.41 │ ■■                                     ║
 SKYWEST AIRLINES   ║  1769 │    2.41 │ ■■                                     ║
 JETBLUE AIRWAYS    ║  1740 │    2.37 │ ■■                                     ║
 EXPRESSJET AIRLINES║  1347 │    1.83 │ ■■                                     ║
 AMERICAN EAGLE AIR…║  1041 │    1.42 │ ■                                      ║
 ENVOY AIR          ║   883 │    1.20 │ ■                                      ║
 ALASKA AIRLINES    ║   835 │    1.14 │ ■                                      ║
 REPUBLIC AIRLINES  ║   804 │    1.09 │ ■                                      ║
 MESA AIRLINES      ║   693 │    0.94 │ ■                                      ║
 AIR WISCONSIN AIRL…║   623 │    0.85 │ ■                                      ║
 PSA AIRLINES       ║   577 │    0.79 │                                        ║
 PRIVATELY OWNED    ║   516 │    0.70 │                                        ║
 PHI INC            ║   491 │    0.67 │                                        ║
6› faa-wildlife-strikes_OPERATOR_freq|                                  Shift+F           282 bins 
</pre>


It has `OPERATOR` as its key column, so transposing this sheet should result in something like this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 OPERATOR  ║ UNKNOWN            │ SOUTHWEST AIRLINES │ BUSINESS           │ AMERICAN AIRLINES  │ D>
 count     ║ [23076] [16] UNKNO…│ [7752] [16] SOUTHW…│ [5868] [16] BUSINE…│ [4337] [16] AMERIC…│ […
 percent   ║ 31.41814617144102 %│ 10.554405838143992%│ 7.989325781505283 %│ 5.904857858621066 %│ 3…%
 histogram ║ ■■■■■■■■■■■■■■■■■■…│ ■■■■■■■■■■■■       │ ■■■■■■■■■          │ ■■■■■■■            │ ■…


7› faa-wildlife-strikes_OPERATOR_freq_T|                                Shift+T             3 rows 
</pre>


:::: note
::: title
Note

If your source sheet has *multiple* key columns, VisiData will join together the columns\' values with the `_` character to create the header names.



## Open the wildlife-strikes dataset in VisiData

Run this command in your terminal:

    vd faa-wildlife-strikes.csv

If it worked, you should see something like this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 OPERATOR           │ ATYPE        │ INCIDENT_DATE     │ STATE │ AIRPORT            │ PHASE_OF_FLT>
 BUSINESS           │ PA-28        │ 05/22/15 00:00:00 │ FL    │ VERO BEACH MUNICIP…│ APPROACH     │
 BUSINESS           │ BE-1900      │ 06/18/15 00:00:00 │ AK    │ KENAI MUNICIPAL AR…│ APPROACH     │
 BUSINESS           │ PA-46 MALIBU │ 09/20/15 00:00:00 │ TX    │ DAVID WAYNE HOOKS …│              │
 DELTA AIR LINES    │ B-717-200    │ 11/07/15 00:00:00 │ MO    │ LAMBERT-ST LOUIS I…│ APPROACH     │
 BUSINESS           │ BE-90 KING   │ 12/17/15 00:00:00 │ FL    │ POMPANO BEACH AIRP…│ LANDING ROLL │
 DELTA AIR LINES    │ B-757        │ 07/17/15 00:00:00 │ VI    │ HENRY E ROHLSEN AR…│              │
 DELTA AIR LINES    │ B-717-200    │ 08/02/15 00:00:00 │ TX    │ SAN ANTONIO INTL   │ APPROACH     │
 BUSINESS           │ C-414        │ 08/03/15 00:00:00 │ TX    │ LONE STAR EXECUTIV…│ DEPARTURE    │
 ALLEGIANT AIR      │ MD-80        │ 09/02/15 00:00:00 │ FL    │ TAMPA INTL         │ APPROACH     │
 TRANS STATES AIRLI…│ EMB-145      │ 09/07/15 00:00:00 │ MO    │ LAMBERT-ST LOUIS I…│ APPROACH     │
 BUSINESS           │ C-172        │ 11/28/15 00:00:00 │ FL    │ OPA-LOCKA EXECUTIV…│ APPROACH     │
 GOVERNMENT         │ EC120        │ 12/08/15 00:00:00 │ CA    │ NORMAN Y. MINETA S…│              │
 AMERICAN AIRLINES  │ A-321        │ 05/06/15 00:00:00 │ FL    │ FORT LAUDERDALE/HO…│ APPROACH     │
 EXPRESSJET AIRLINES│ CRJ100/200   │ 05/06/15 00:00:00 │ AR    │ FORT SMITH REGIONA…│ CLIMB        │
 MESA AIRLINES      │ CRJ900       │ 05/08/15 00:00:00 │ AR    │ BILL AND  HILLARY …│ LANDING ROLL │
 BUSINESS           │ HELICOPTER   │ 05/06/15 00:0┌──────────────────────────────────| statuses |─┐│
 DELTA AIR LINES    │ A-320        │ 05/07/15 00:0│ saul.pw/VisiData v3.0.2                       ││
 DELTA AIR LINES    │ A-320        │ 05/08/15 00:0│ opening datasets/faa-wildlife-strikes.csv as  ││
 LUFTHANSA          │ A-380        │ 05/10/15 00:0│ csv                                           ││
 BUSINESS           │ C-172        │ 05/08/15 00:0│ Don't panic.                                  ││
 SPIRIT AIRLINES    │ A-319        │ 05/10/15 00:0└───────────────────────────────────────────────┘│
1› faa-wildlife-strikes|                                                                73448 rows 
</pre>



## Select only known species

For many of the wildlife strikes in the dataset, species is \"unknown\". We want to focus just on the known species, so we\'ll filter out the unknowns in this step.

First, navigate to the `SPECIES` column. Then, do the following:

- Press `|` to raise the select-by-search prompt
- Type `unknown`
- Press `Enter`

Once you do that, you should see something like this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
<STATE │ AIRPORT            │ PHASE_OF_FLT │ HEIGHT │ SPEED │ SPECIES            │ BIRDS_STRUCK │ >
•FL    │ VERO BEACH MUNICIP…│ APPROACH     │        │       │ Unknown bird       │ 1            │ N 
•AK    │ KENAI MUNICIPAL AR…│ APPROACH     │        │       │ Unknown bird       │ 1            │ N 
•TX    │ DAVID WAYNE HOOKS …│              │        │       │ Unknown bird       │ 1            │ N 
•MO    │ LAMBERT-ST LOUIS I…│ APPROACH     │        │       │ Unknown bird       │ 1            │ N 
•FL    │ POMPANO BEACH AIRP…│ LANDING ROLL │ 0      │       │ Unknown bird       │ 1            │   
•VI    │ HENRY E ROHLSEN AR…│              │        │       │ Unknown bird       │ 1            │ O 
•TX    │ SAN ANTONIO INTL   │ APPROACH     │        │       │ Unknown bird       │ 1            │ N 
•TX    │ LONE STAR EXECUTIV…│ DEPARTURE    │        │       │ Unknown bird       │ 1            │ P 
•FL    │ TAMPA INTL         │ APPROACH     │ 6000   │       │ Unknown bird       │ 1            │ N 
 MO    │ LAMBERT-ST LOUIS I…│ APPROACH     │        │       │ Owls               │ 1            │ N 
 FL    │ OPA-LOCKA EXECUTIV…│ APPROACH     │        │       │ Hawks              │ 1            │ N 
 CA    │ NORMAN Y. MINETA S…│              │        │       │ Gulls              │ 1            │ N 
•FL    │ FORT LAUDERDALE/HO…│ APPROACH     │ 1500   │       │ Unknown bird - sma…│ 1            │ N 
•AR    │ FORT SMITH REGIONA…│ CLIMB        │        │       │ Unknown bird - sma…│ 1            │ N 
•AR    │ BILL AND  HILLARY …│ LANDING ROLL │ 0      │       │ Unknown bird - sma…│ 1            │ N 
•      │ UNKNOWN            │ En Route     │        │       │ Unknown bird       │ 1            │ P 
•CA    │ METRO OAKLAND INTL │              │        │  ┌─────────────────────────────| statuses |─┐ 
•UT    │ SALT LAKE CITY INTL│              │        │  │ search wrapped                           │ 
•TX    │ GEORGE BUSH INTERC…│ CLIMB        │        │  │ 25988 matches for /unknown/              │ 
•FL    │ ORLANDO SANFORD IN…│ APPROACH     │        │  │ selected 25988 rows                      │ 
•IL    │ CHICAGO O'HARE INT…│ CLIMB        │ 12000  │  └──────────────────────────────────────────┘ 
1› faa-wildlife-strikes|                              |   select-col-regex      73448 rows  •25988 
</pre>


Now, all the unknown species are selected. But we want the *opposite* of that: only known species selected. To do that, let\'s toggle the selection-ing for all rows, by typing `gt` (mnemonic: \"global toggle\"). Once you do that, you should see something like this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
<STATE │ AIRPORT            │ PHASE_OF_FLT │ HEIGHT │ SPEED │ SPECIES            │ BIRDS_STRUCK │ >
 FL    │ VERO BEACH MUNICIP…│ APPROACH     │        │       │ Unknown bird       │ 1            │ N 
 AK    │ KENAI MUNICIPAL AR…│ APPROACH     │        │       │ Unknown bird       │ 1            │ N 
 TX    │ DAVID WAYNE HOOKS …│              │        │       │ Unknown bird       │ 1            │ N 
 MO    │ LAMBERT-ST LOUIS I…│ APPROACH     │        │       │ Unknown bird       │ 1            │ N 
 FL    │ POMPANO BEACH AIRP…│ LANDING ROLL │ 0      │       │ Unknown bird       │ 1            │   
 VI    │ HENRY E ROHLSEN AR…│              │        │       │ Unknown bird       │ 1            │ O 
 TX    │ SAN ANTONIO INTL   │ APPROACH     │        │       │ Unknown bird       │ 1            │ N 
 TX    │ LONE STAR EXECUTIV…│ DEPARTURE    │        │       │ Unknown bird       │ 1            │ P 
 FL    │ TAMPA INTL         │ APPROACH     │ 6000   │       │ Unknown bird       │ 1            │ N 
•MO    │ LAMBERT-ST LOUIS I…│ APPROACH     │        │       │ Owls               │ 1            │ N 
•FL    │ OPA-LOCKA EXECUTIV…│ APPROACH     │        │       │ Hawks              │ 1            │ N 
•CA    │ NORMAN Y. MINETA S…│              │        │       │ Gulls              │ 1            │ N 
 FL    │ FORT LAUDERDALE/HO…│ APPROACH     │ 1500   │       │ Unknown bird - sma…│ 1            │ N 
 AR    │ FORT SMITH REGIONA…│ CLIMB        │        │       │ Unknown bird - sma…│ 1            │ N 
 AR    │ BILL AND  HILLARY …│ LANDING ROLL │ 0      │       │ Unknown bird - sma…│ 1            │ N 
       │ UNKNOWN            │ En Route     │        │       │ Unknown bird       │ 1            │ P 
 CA    │ METRO OAKLAND INTL │              │        │       │ Unknown bird       │ 1            │ N 
 UT    │ SALT LAKE CITY INTL│              │        │       │ Unknown bird       │ 1            │ N 
 TX    │ GEORGE BUSH INTERC…│ CLIMB        │        │       │ Unknown bird       │ 1            │ N 
 FL    │ ORLANDO SANFORD IN…│ APPROACH     │        │       │ Unknown bird       │ 1            │ N 
 IL    │ CHICAGO O'HARE INT…│ CLIMB        │ 12000  │       │ Unknown bird       │ 1            │ P 
1› faa-wildlife-strikes|                                 gt   stoggle-rows      73448 rows  •47460 
</pre>


Now that we\'ve selected our desired rows, let\'s create a new sheet containing *only* those rows, by pressing `"`. The result should look something like this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
<STATE │ AIRPORT            │ PHASE_OF_FLT │ HEIGHT │ SPEED │ SPECIES            │ BIRDS_STRUCK │ >
 MO    │ LAMBERT-ST LOUIS I…│ APPROACH     │        │       │ Owls               │ 1            │ N 
 FL    │ OPA-LOCKA EXECUTIV…│ APPROACH     │        │       │ Hawks              │ 1            │ N 
 CA    │ NORMAN Y. MINETA S…│              │        │       │ Gulls              │ 1            │ N 
 TX    │ GEORGE BUSH INTERC…│ LANDING ROLL │ 0      │       │ Sparrows           │ 1            │ N 
 FL    │ VERO BEACH MUNICIP…│ DEPARTURE    │        │       │ Sandhill crane     │ 1            │ N 
 CA    │ ONTARIO INTL ARPT  │              │        │       │ Owls               │ 1            │ N 
 TN    │ MC GHEE TYSON ARPT │ APPROACH     │        │       │ Barn swallow       │ 1            │ N 
 SC    │ CHARLESTON AFB/INT…│ DEPARTURE    │        │       │ Gulls              │ 1            │ N 
 CA    │ WHITEMAN AIRPORT   │ LANDING ROLL │ 0      │       │ Rock pigeon        │ 1            │ N 
 WA    │ SEATTLE-TACOMA INTL│              │        │       │ Barn owl           │ 1            │ N 
 HI    │ KAHULUI ARPT       │ LANDING ROLL │ 0      │       │ Gulls              │ 1            │ N 
 TX    │ CORPUS CHRISTI INT…│ TAKE-OFF RUN │ 0      │       │ Gulls              │ 1            │ N 
 FL    │ TALLAHASSEE REGION…│ APPROACH     │        │       │ Gulls              │ 2-10         │ N 
 TX    │ JACK BROOKS REGION…│ APPROACH     │        │       │ Owls               │ 1            │ N 
 PA    │ CAPITAL CITY ARPT …│ LANDING ROLL │ 0      │       │ Bank swallow       │ 1            │ N 
 AL    │ MOBILE REGIONAL    │ APPROACH     │ 2000   │ 200   │ Gulls              │ 1            │ N 
 PA    │ HARRISBURG INTL    │ DEPARTURE    │        │       │ Swallows           │ 1            │ N 
 CT    │ BRADLEY INTL       │              │        │       │ Horned lark        │ 2-10         │   
 MA    │ GENERAL EDWARD LAW…│              │        │       │ Horned lark        │ 1            │   
 CA    │ SACRAMENTO INTL    │ Climb        │ 1500   │ 210   │ Northern pintail   │ 2-10         │ P 
 OH    │ RICKENBACKER INTL  │              │        │       │ American robin     │ 1            │   
2› faa-wildlife-strikes_selectedref|                                          "         47460 rows 
</pre>




## Rename the filtered sheet

By default, our sheet will be titled \"faa-wildlife-strikes_selectedref\". To make it slightly easier to distinguish from other sheets, let\'s rename it. To rename a sheet, do the following:

- Press `Space` to raise the type-a-command prompt
- Type `rename-sheet` (the command we want to use) and press `Enter`
- At the next prompt, type the new name we want; in this case `known_species`

At this point, you should see something like this:


<pre>
 MA    │ GENERAL EDWARD LAW…│              │        │       │ Horned lark        │ 1            │   
 CA    │ SACRAMENTO INTL    │ Climb        │ 1500   │ 210   │ Northern pintail   │ 2-10         │ P 
 OH    │ RICKENBACKER INTL  │              │        │       │ American robin     │ 1            │   
rename sheet to: known_species                                Space   rename-sheet      47460 rows 
</pre>


When you\'ve entered the name, press `Enter` to complete the edit (or `Control-c` to cancel the edit).


## Count the number of collisions per state

To get the denominator for our calculations, we\'ll want to know the total number of reported collisions for each state.

Back in our `known_species` sheet, navigate to the `STATE` column:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
<STATE │ AIRPORT            │ PHASE_OF_FLT │ HEIGHT │ SPEED │ SPECIES            │ BIRDS_STRUCK │ >
 MO    │ LAMBERT-ST LOUIS I…│ APPROACH     │        │       │ Owls               │ 1            │ N 
 FL    │ OPA-LOCKA EXECUTIV…│ APPROACH     │        │       │ Hawks              │ 1            │ N 
 CA    │ NORMAN Y. MINETA S…│              │        │       │ Gulls              │ 1            │ N 
 TX    │ GEORGE BUSH INTERC…│ LANDING ROLL │ 0      │       │ Sparrows           │ 1            │ N 
 FL    │ VERO BEACH MUNICIP…│ DEPARTURE    │        │       │ Sandhill crane     │ 1            │ N 
 CA    │ ONTARIO INTL ARPT  │              │        │       │ Owls               │ 1            │ N 
 TN    │ MC GHEE TYSON ARPT │ APPROACH     │        │       │ Barn swallow       │ 1            │ N 
 SC    │ CHARLESTON AFB/INT…│ DEPARTURE    │        │       │ Gulls              │ 1            │ N 
 CA    │ WHITEMAN AIRPORT   │ LANDING ROLL │ 0      │       │ Rock pigeon        │ 1            │ N 
 WA    │ SEATTLE-TACOMA INTL│              │        │       │ Barn owl           │ 1            │ N 
 HI    │ KAHULUI ARPT       │ LANDING ROLL │ 0      │       │ Gulls              │ 1            │ N 
 TX    │ CORPUS CHRISTI INT…│ TAKE-OFF RUN │ 0      │       │ Gulls              │ 1            │ N 
 FL    │ TALLAHASSEE REGION…│ APPROACH     │        │       │ Gulls              │ 2-10         │ N 
 TX    │ JACK BROOKS REGION…│ APPROACH     │        │       │ Owls               │ 1            │ N 
 PA    │ CAPITAL CITY ARPT …│ LANDING ROLL │ 0      │       │ Bank swallow       │ 1            │ N 
 AL    │ MOBILE REGIONAL    │ APPROACH     │ 2000   │ 200   │ Gulls              │ 1            │ N 
 PA    │ HARRISBURG INTL    │ DEPARTURE    │        │       │ Swallows           │ 1            │ N 
 CT    │ BRADLEY INTL       │              │        │       │ Horned lark        │ 2-10         │   
 MA    │ GENERAL EDWARD LAW…│              │        │       │ Horned lark        │ 1            │   
 CA    │ SACRAMENTO INTL    │ Climb        │ 1500   │ 210   │ Northern pintail   │ 2-10         │ P 
 OH    │ RICKENBACKER INTL  │              │        │       │ American robin     │ 1            │   
2› known_species|                                                 c   go-col-regex      47460 rows 
</pre>


Then, to create a frequency table for the column, press `Shift-F`. Once you do, you should see something like this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 STATE ║↓count♯│ percent%│ histogram                             ~║                                
 TX    ║  4670 │    9.84 │ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ║
       ║  4428 │    9.33 │ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■   ║
 CA    ║  3391 │    7.14 │ ■■■■■■■■■■■■■■■■■■■■■■■■■■■            ║
 FL    ║  3096 │    6.52 │ ■■■■■■■■■■■■■■■■■■■■■■■■■              ║
 CO    ║  2914 │    6.14 │ ■■■■■■■■■■■■■■■■■■■■■■■                ║
 NY    ║  2626 │    5.53 │ ■■■■■■■■■■■■■■■■■■■■■                  ║
 IL    ║  2153 │    4.54 │ ■■■■■■■■■■■■■■■■■                      ║
 NJ    ║  1681 │    3.54 │ ■■■■■■■■■■■■■                          ║
 PA    ║  1665 │    3.51 │ ■■■■■■■■■■■■■                          ║
 OH    ║  1515 │    3.19 │ ■■■■■■■■■■■■                           ║
 MI    ║  1234 │    2.60 │ ■■■■■■■■■■                             ║
 MO    ║  1140 │    2.40 │ ■■■■■■■■■                              ║
 UT    ║  1049 │    2.21 │ ■■■■■■■■                               ║
 WA    ║   874 │    1.84 │ ■■■■■■■                                ║
 HI    ║   873 │    1.84 │ ■■■■■■■                                ║
 GA    ║   824 │    1.74 │ ■■■■■■                                 ║
 NC    ║   813 │    1.71 │ ■■■■■■                                 ║
 MA    ║   801 │    1.69 │ ■■■■■■                                 ║
 TN    ║   774 │    1.63 │ ■■■■■■                                 ║
 IN    ║   773 │    1.63 │ ■■■■■■                                 ║
 LA    ║   737 │    1.55 │ ■■■■■                                  ║
3› known_species_STATE_freq|                                            Shift+F            63 bins 
</pre>




## Spruce up the frequency table

Because we\'ll later be joining this sheet to another sheet, let\'s hide the `percent` and `histogram` columns by navigating to each and pressing `-`.

Now the sheet should look something like this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 STATE ║↓count♯║                                                                                   
 TX    ║  4670 ║                                                   
       ║  4428 ║                                                   
 CA    ║  3391 ║                                                   
 FL    ║  3096 ║                                                                                   
 CO    ║  2914 ║                                                                                   
 NY    ║  2626 ║                                                                                   
 IL    ║  2153 ║                                                                                   
 NJ    ║  1681 ║                                                                                   
 PA    ║  1665 ║                                                                                   
 OH    ║  1515 ║                                                                                   
 MI    ║  1234 ║                                                                                   
 MO    ║  1140 ║                                                                                   
 UT    ║  1049 ║                                                                                   
 WA    ║   874 ║                                                                                   
 HI    ║   873 ║                                                                                   
 GA    ║   824 ║                                                                                   
 NC    ║   813 ║                                                                                   
 MA    ║   801 ║                                                                                   
 TN    ║   774 ║                                                                                   
 IN    ║   773 ║                                                                                   
 LA    ║   737 ║                                                                                   
3› known_species_STATE_freq|                                          -   hide-col         63 bins 
</pre>



## Count the number of collisions per state *and* species

Now that we have the denominator --- collisions per state --- let\'s calculate the numerator: collisions *per species* per state.

To do that, we\'ll want to create a frequency table for the *combination* of the `STATE` and `SPECIES` columns. Here\'s how:

- Use the Sheets Sheet (`Shift-S`) to navigate back to the `known_species` sheet
- Navigate to the `STATE` column, and press `!` to make it a \"key\" column
- Do the same thing for the `SPECIES` columns

At this point, you should see something like this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 STATE │ SPECIES            ║<AIRPORT            │ PHASE_OF_FLT │ HEIGHT │ SPEED │ BIRDS_STRUCK │ >
 MO    │ Owls               ║ LAMBERT-ST LOUIS I…│ APPROACH     │        │       │ 1            │ N
 FL    │ Hawks              ║ OPA-LOCKA EXECUTIV…│ APPROACH     │        │       │ 1            │ N
 CA    │ Gulls              ║ NORMAN Y. MINETA S…│              │        │       │ 1            │ N
 TX    │ Sparrows           ║ GEORGE BUSH INTERC…│ LANDING ROLL │ 0      │       │ 1            │ N
 FL    │ Sandhill crane     ║ VERO BEACH MUNICIP…│ DEPARTURE    │        │       │ 1            │ N
 CA    │ Owls               ║ ONTARIO INTL ARPT  │              │        │       │ 1            │ N
 TN    │ Barn swallow       ║ MC GHEE TYSON ARPT │ APPROACH     │        │       │ 1            │ N
 SC    │ Gulls              ║ CHARLESTON AFB/INT…│ DEPARTURE    │        │       │ 1            │ N
 CA    │ Rock pigeon        ║ WHITEMAN AIRPORT   │ LANDING ROLL │ 0      │       │ 1            │ N
 WA    │ Barn owl           ║ SEATTLE-TACOMA INTL│              │        │       │ 1            │ N
 HI    │ Gulls              ║ KAHULUI ARPT       │ LANDING ROLL │ 0      │       │ 1            │ N
 TX    │ Gulls              ║ CORPUS CHRISTI INT…│ TAKE-OFF RUN │ 0      │       │ 1            │ N
 FL    │ Gulls              ║ TALLAHASSEE REGION…│ APPROACH     │        │       │ 2-10         │ N
 TX    │ Owls               ║ JACK BROOKS REGION…│ APPROACH     │        │       │ 1            │ N
 PA    │ Bank swallow       ║ CAPITAL CITY ARPT …│ LANDING ROLL │ 0      │       │ 1            │ N
 AL    │ Gulls              ║ MOBILE REGIONAL    │ APPROACH     │ 2000   │ 200   │ 1            │ N
 PA    │ Swallows           ║ HARRISBURG INTL    │ DEPARTURE    │        │       │ 1            │ N
 CT    │ Horned lark        ║ BRADLEY INTL       │              │        │       │ 2-10         │  
 MA    │ Horned lark        ║ GENERAL EDWARD LAW…│              │        │       │ 1            │  
 CA    │ Northern pintail   ║ SACRAMENTO INTL    │ Climb        │ 1500   │ 210   │ 2-10         │ P
 OH    │ American robin     ║ RICKENBACKER INTL  │              │        │       │ 1            │  
2› known_species|                                                      !   key-col      47460 rows 
</pre>


Now, type `gF`, which will create a frequency table of all keyed columns. Once you do, you should see something like this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 STATE │ SPECIES            ║↓count♯│ percent%│ histogram                             ~║           
 CO    │ Horned lark        ║  1117 │    2.35 │ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ║
 TX    │ Mourning dove      ║   984 │    2.07 │ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■      ║
 TX    │ Rock pigeon        ║   339 │    0.71 │ ■■■■■■■■■■■                            ║
 HI    │ Pacific golden-plo…║   329 │    0.69 │ ■■■■■■■■■■■                            ║
 FL    │ Barn swallow       ║   316 │    0.67 │ ■■■■■■■■■■                             ║
 CO    │ Western meadowlark ║   307 │    0.65 │ ■■■■■■■■■■                             ║
 FL    │ Mourning dove      ║   304 │    0.64 │ ■■■■■■■■■■                             ║
 CO    │ Mourning dove      ║   282 │    0.59 │ ■■■■■■■■■                              ║
       │ Perching birds (y) ║   274 │    0.58 │ ■■■■■■■■■                              ║
 IL    │ American kestrel   ║   273 │    0.58 │ ■■■■■■■■■                              ║
 IL    │ Killdeer           ║   266 │    0.56 │ ■■■■■■■■■                              ║
 TX    │ Killdeer           ║   260 │    0.55 │ ■■■■■■■■                               ║
 UT    │ Horned lark        ║   260 │    0.55 │ ■■■■■■■■                               ║
 CA    │ American kestrel   ║   258 │    0.54 │ ■■■■■■■■                               ║
 FL    │ Killdeer           ║   236 │    0.50 │ ■■■■■■■■                               ║
 CA    │ Red-tailed hawk    ║   229 │    0.48 │ ■■■■■■■                                ║
 TX    │ Barn swallow       ║   219 │    0.46 │ ■■■■■■■                                ║
 CA    │ Cliff swallow      ║   213 │    0.45 │ ■■■■■■■                                ║
 NY    │ Barn swallow       ║   208 │    0.44 │ ■■■■■■■                                ║
 CA    │ Barn owl           ║   200 │    0.42 │ ■■■■■■                                 ║
 NY    │ American kestrel   ║   196 │    0.41 │ ■■■■■■                                 ║
4› known_species_STATE-SPECIES_freq|                                   gShift+F          5135 bins 
</pre>


Just like we did with the state-frequency table, let\'s simplify this table by removing the `percent` and `histogram` columns; navigate to each of those columns and press `-`, which should result in something like this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 STATE │ SPECIES            ║↓count♯║                                                              
 CO    │ Horned lark        ║  1117 ║                                                   
 TX    │ Mourning dove      ║   984 ║                                                   
 TX    │ Rock pigeon        ║   339 ║                                                   
 HI    │ Pacific golden-plo…║   329 ║                                                   
 FL    │ Barn swallow       ║   316 ║                                                   
 CO    │ Western meadowlark ║   307 ║                                                   
 FL    │ Mourning dove      ║   304 ║                                                   
 CO    │ Mourning dove      ║   282 ║                                                   
       │ Perching birds (y) ║   274 ║                                                   
 IL    │ American kestrel   ║   273 ║                                                   
 IL    │ Killdeer           ║   266 ║                                                   
 TX    │ Killdeer           ║   260 ║                                                   
 UT    │ Horned lark        ║   260 ║                                                   
 CA    │ American kestrel   ║   258 ║                                                   
 FL    │ Killdeer           ║   236 ║                                                   
 CA    │ Red-tailed hawk    ║   229 ║                                                   
 TX    │ Barn swallow       ║   219 ║                                                   
 CA    │ Cliff swallow      ║   213 ║                                                   
 NY    │ Barn swallow       ║   208 ║                                                   
 CA    │ Barn owl           ║   200 ║                                                   
 NY    │ American kestrel   ║   196 ║                                                   
4› known_species_STATE-SPECIES_freq|                                  -   hide-col       5135 bins 
</pre>




## Prepare the state-species frequency table for joining

There\'s just one step left before we can join the tables: making sure that the two frequency tables share the exact same key column. (VisiData uses each sheet\'s \"key\" columns to determine which rows to join.)

Because the key for the state-counts table is the `STATE` column, this table should also have `STATE` as its only key column. That means we need to un-key the `SPECIES` column. Luckily, that\'s easy. Just navigate to the `SPECIES` column and press `!` to toggle it\'s status from keyed to un-keyed:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 STATE ║ SPECIES            │↓count♯║                                                              
 CO    ║ Horned lark        │  1117 ║                                                   
 TX    ║ Mourning dove      │   984 ║                                                   
 TX    ║ Rock pigeon        │   339 ║                                                   
 HI    ║ Pacific golden-plo…│   329 ║                                                   
 FL    ║ Barn swallow       │   316 ║                                                   
 CO    ║ Western meadowlark │   307 ║                                                   
 FL    ║ Mourning dove      │   304 ║                                                   
 CO    ║ Mourning dove      │   282 ║                                                   
       ║ Perching birds (y) │   274 ║                                                   
 IL    ║ American kestrel   │   273 ║                                                   
 IL    ║ Killdeer           │   266 ║                                                   
 TX    ║ Killdeer           │   260 ║                                                   
 UT    ║ Horned lark        │   260 ║                                                   
 CA    ║ American kestrel   │   258 ║                                                   
 FL    ║ Killdeer           │   236 ║                                                   
 CA    ║ Red-tailed hawk    │   229 ║                                                   
 TX    ║ Barn swallow       │   219 ║                                                   
 CA    ║ Cliff swallow      │   213 ║                                                   
 NY    ║ Barn swallow       │   208 ║                                                   
 CA    ║ Barn owl           │   200 ║                                                   
 NY    ║ American kestrel   │   196 ║                                                   
4› known_species_STATE-SPECIES_freq|                                   !   key-col       5135 bins 
</pre>



## Join the two frequency tables

Now, for the moment we\'ve all been waiting for: Let\'s join the tables!

First, press `Shift-S` to open the Sheets Sheet:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 name                             ║ type           │ pane#│ shortcut │ nRows#│ nCols#│ nVisibleCol>
 sheets                           ║ SheetsSheet    │    1 │ Shift+S  │     5 │    11 │           11
 known_species_STATE-SPECIES_freq ║ FreqTableSheet │    1 │ 4        │  5135 │     5 │            3
 known_species                    ║ CsvSheet       │    1 │ 2        │ 47460 │    16 │           16
 known_species_STATE_freq         ║ FreqTableSheet │    1 │ 3        │    63 │     4 │            2
 faa-wildlife-strikes             ║ CsvSheet       │    1 │ 1        │ 73448 │    16 │           16


Shift+S› sheets|                                                     gk   go-top          5 sheets 
</pre>


Then navigate to the `known_species_STATE-SPECIES_freq` row, and press `s` to select it. Do the same for the `known_species_STATE_freq`, so that the Sheets Sheet now looks like this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 name                             ║ type           │ pane#│ shortcut │ nRows#│ nCols#│ nVisibleCol>
 sheets                           ║ SheetsSheet    │    1 │ Shift+S  │     5 │    11 │           11
•known_species_STATE-SPECIES_freq ║ FreqTableSheet │    1 │ 4        │  5135 │     5 │            3
 known_species                    ║ CsvSheet       │    1 │ 2        │ 47460 │    16 │           16
•known_species_STATE_freq         ║ FreqTableSheet │    1 │ 3        │    63 │     4 │            2
 faa-wildlife-strikes             ║ CsvSheet       │    1 │ 1        │ 73448 │    16 │           16


Shift+S› sheets|                                              s   select-row          5 sheets  •2 
</pre>


Press `&` to raise the sheet-joining prompt:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 name                             ║ type           │ pane#│ shortcut │ nRows#│ nCols#│ nVisibleCol>
 sheets                           ║ SheetsSheet    │    1 │ Shift+S  │     5 │    11 │           11
•known_species_STATE-SPECIES_freq ║ FreqTableSheet │    1 │ 4        │  5135 │     5 │            3
 known_species                    ║ CsvSheet       │    1 │ 2        │ 47460 │    16 │           16
•known_species_STATE_freq         ║ FreqTableSheet │    1 │ 3        │    63 │     4 │            2
 faa-wildlife-strikes             ║ CsvSheet       │    1 │ 1        │ 73448 │    16 │           16


                inner - only rows with matching keys on all sheets
                outer - only rows with matching keys on first selected sheet
                full - all rows from all sheets (union)
                diff - only rows NOT in all sheets
                append - all rows from all sheets; columns from all sheets
                concat - all rows from all sheets; columns and type from first sheet
                extend - only rows from first sheet; type from first sheet; columns from all sheets
                merge - merge differences from other sheets into first sheet (includin| Join Help ┐
                                                                                      │ HELPTODO  │
                                                                                      └───────────┘
choose jointype:                                           &   join-selected          5 sheets  •2 
</pre>


Type `inner` and press `Enter` to complete the action. After that, you should see something like this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 STATE ║ SPECIES            │ known♯│ known♯║                                                      
 CO    ║ Horned lark        │  1117 │  2914 ║
 CO    ║ Western meadowlark │   307 │  2914 ║
 CO    ║ Mourning dove      │   282 │  2914 ║
 CO    ║ Cliff swallow      │   148 │  2914 ║
 CO    ║ Lark bunting       │    91 │  2914 ║
 CO    ║ Rock pigeon        │    82 │  2914 ║
 CO    ║ American kestrel   │    78 │  2914 ║
 CO    ║ Red-tailed hawk    │    73 │  2914 ║
 CO    ║ Black-tailed jackr…│    61 │  2914 ║
 CO    ║ Killdeer           │    41 │  2914 ║
 CO    ║ Great horned owl   │    31 │  2914 ║
 CO    ║ Black-tailed prair…│    31 │  2914 ║
 CO    ║ Sparrows           │    30 │  2914 ║
 CO    ║ Western kingbird   │    25 │  2914 ║
 CO    ║ Desert cottontail  │    24 │  2914 ║
 CO    ║ Perching birds (y) │    20 │  2914 ║
 CO    ║ Burrowing owl      │    20 │  2914 ║
 CO    ║ Mountain bluebird  │    16 │  2914 ║
 CO    ║ Vesper sparrow     │    16 │  2914 ║
 CO    ║ Red-winged blackbi…│    15 │  2914 ║
 CO    ║ Little brown bat   │    15 │  2914 ║
5› known_species_STATE-SPECIES_freq+known_species_STATE_freq|                 &          5135 rows 
</pre>


The columns that had previously been called `count` in both sheets have been auto-prefixed with the name of their source sheet. Let\'s clarify things by using the `^` shortcut to rename them to `count` and `state_total`, respectively. On the `state_total` column, press `_` to expand the width to see the full name:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 STATE ║ SPECIES            │ count♯│ state_total♯║                                                
 CO    ║ Horned lark        │  1117 │        2914 ║
 CO    ║ Western meadowlark │   307 │        2914 ║
 CO    ║ Mourning dove      │   282 │        2914 ║
 CO    ║ Cliff swallow      │   148 │        2914 ║
 CO    ║ Lark bunting       │    91 │        2914 ║
 CO    ║ Rock pigeon        │    82 │        2914 ║
 CO    ║ American kestrel   │    78 │        2914 ║
 CO    ║ Red-tailed hawk    │    73 │        2914 ║
 CO    ║ Black-tailed jackr…│    61 │        2914 ║                                                
 CO    ║ Killdeer           │    41 │        2914 ║                                                
 CO    ║ Great horned owl   │    31 │        2914 ║                                                
 CO    ║ Black-tailed prair…│    31 │        2914 ║                                                
 CO    ║ Sparrows           │    30 │        2914 ║                                                
 CO    ║ Western kingbird   │    25 │        2914 ║                                                
 CO    ║ Desert cottontail  │    24 │        2914 ║                                                
 CO    ║ Perching birds (y) │    20 │        2914 ║                                                
 CO    ║ Burrowing owl      │    20 │        2914 ║                                                
 CO    ║ Mountain bluebird  │    16 │        2914 ║                                                
 CO    ║ Vesper sparrow     │    16 │        2914 ║                                                
 CO    ║ Red-winged blackbi…│    15 │        2914 ║                                                
 CO    ║ Little brown bat   │    15 │        2914 ║                                                
5› joined|                                                      _   resize-col-max       5135 rows 
</pre>


Finally, let\'s give the sheet a shorter name:

- Press `Space` to raise the type-a-command prompt
- Type `rename-sheet` and press `Enter`
- At the next prompt, type the new name we want; in this case `joined`



## Calculate each species\' state-level percentages

Now that we have the numerator and denominator in the same sheet, let\'s calculate the percentage of known-species collisions to each species in each state.

Let\'s say we want the new column to appear as the last column in the sheet, so let\'s navigate to the currently-last column by typing `gl`. Then let\'s create the new column by pressing `=`, typing `count * 100 / state_total`, and then pressing `Enter`.

Once you do that, you should see something like this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 STATE ║ SPECIES            │ count♯│ state_total♯│ count * 100 / state_total ║                    
 CO    ║ Horned lark        │  1117 │        2914 │ 38.33218943033631        %║
 CO    ║ Western meadowlark │   307 │        2914 │ 10.535346602608099       %║
 CO    ║ Mourning dove      │   282 │        2914 │ 9.67741935483871         %║
 CO    ║ Cliff swallow      │   148 │        2914 │ 5.078929306794784        %║
 CO    ║ Lark bunting       │    91 │        2914 │ 3.1228551818805763       %║
 CO    ║ Rock pigeon        │    82 │        2914 │ 2.8140013726835966       %║
 CO    ║ American kestrel   │    78 │        2914 │ 2.676733013040494        %║
 CO    ║ Red-tailed hawk    │    73 │        2914 │ 2.5051475634866165       %║
 CO    ║ Black-tailed jackr…│    61 │        2914 │ 2.0933424845573096       %║                    
 CO    ║ Killdeer           │    41 │        2914 │ 1.4070006863417983       %║                    
 CO    ║ Great horned owl   │    31 │        2914 │ 1.0638297872340425       %║                    
 CO    ║ Black-tailed prair…│    31 │        2914 │ 1.0638297872340425       %║                    
 CO    ║ Sparrows           │    30 │        2914 │ 1.029512697323267        %║                    
 CO    ║ Western kingbird   │    25 │        2914 │ 0.8579272477693891       %║                    
 CO    ║ Desert cottontail  │    24 │        2914 │ 0.8236101578586136       %║                    
 CO    ║ Perching birds (y) │    20 │        2914 │ 0.6863417982155113       %║                    
 CO    ║ Burrowing owl      │    20 │        2914 │ 0.6863417982155113       %║                    
 CO    ║ Mountain bluebird  │    16 │        2914 │ 0.5490734385724091       %║                    
 CO    ║ Vesper sparrow     │    16 │        2914 │ 0.5490734385724091       %║                    
 CO    ║ Red-winged blackbi…│    15 │        2914 │ 0.5147563486616334       %║                    
 CO    ║ Little brown bat   │    15 │        2914 │ 0.5147563486616334       %║                    
5› joined|                                                     =   addcol-expr       5135 rows  [M]
</pre>


It worked! But the column name is a bit wonky and literal. Let\'s make the following tweaks:

- Rename the column by navigating to it, pressing `^` to enter the column-name-editing mode, typing `pct_of_state`, and then pressing `Enter`.
- Press `%` to tell VisiData that it\'s a \"float\"-type numeric column. (By default, VisiData assumes that newly created columns are just plain-old text.)
- Press `_` to resize the column to fit its contents more precisely

Now the sheet should look something like this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 STATE ║ SPECIES            │ count♯│ state_total♯│ pct_of_state%║                                 
 CO    ║ Horned lark        │  1117 │        2914 │        38.33 ║             
 CO    ║ Western meadowlark │   307 │        2914 │        10.54 ║             
 CO    ║ Mourning dove      │   282 │        2914 │         9.68 ║             
 CO    ║ Cliff swallow      │   148 │        2914 │         5.08 ║             
 CO    ║ Lark bunting       │    91 │        2914 │         3.12 ║             
 CO    ║ Rock pigeon        │    82 │        2914 │         2.81 ║             
 CO    ║ American kestrel   │    78 │        2914 │         2.68 ║             
 CO    ║ Red-tailed hawk    │    73 │        2914 │         2.51 ║             
 CO    ║ Black-tailed jackr…│    61 │        2914 │         2.09 ║                                 
 CO    ║ Killdeer           │    41 │        2914 │         1.41 ║                                 
 CO    ║ Great horned owl   │    31 │        2914 │         1.06 ║                                 
 CO    ║ Black-tailed prair…│    31 │        2914 │         1.06 ║                                 
 CO    ║ Sparrows           │    30 │        2914 │         1.03 ║                                 
 CO    ║ Western kingbird   │    25 │        2914 │         0.86 ║                                 
 CO    ║ Desert cottontail  │    24 │        2914 │         0.82 ║                                 
 CO    ║ Perching birds (y) │    20 │        2914 │         0.69 ║                                 
 CO    ║ Burrowing owl      │    20 │        2914 │         0.69 ║                                 
 CO    ║ Mountain bluebird  │    16 │        2914 │         0.55 ║                                 
 CO    ║ Vesper sparrow     │    16 │        2914 │         0.55 ║                                 
 CO    ║ Red-winged blackbi…│    15 │        2914 │         0.51 ║                                 
 CO    ║ Little brown bat   │    15 │        2914 │         0.51 ║                                 
5› joined|                                                  _   resize-col-max       5135 rows  [M]
</pre>



## Sort by percentage

Of course, to answer our main question, we\'ll need to sort the column. To sort it descendingly, press `]`. Now you should see something like this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 STATE ║ SPECIES            │ count♯│ state_total♯│↓pct_of_state%║                                 
 SK    ║ Gulls              │     1 │           1 │       100.00 ║
 NS    ║ Striped skunk      │     1 │           1 │       100.00 ║
 NL    ║ Snow bunting       │     1 │           1 │       100.00 ║
 MB    ║ Mallard            │     1 │           2 │        50.00 ║
 MB    ║ Cedar waxwing      │     1 │           2 │        50.00 ║
 AB    ║ Canada goose       │     1 │           2 │        50.00 ║
 AB    ║ Perching birds (y) │     1 │           2 │        50.00 ║
 PI    ║ Yellow bittern     │    72 │         173 │        41.62 ║
 CO    ║ Horned lark        │  1117 │        2914 │        38.33 ║
 HI    ║ Pacific golden-plo…│   329 │         873 │        37.69 ║
 AZ    ║ Mourning dove      │   134 │         438 │        30.59 ║
 MS    ║ Mourning dove      │    60 │         197 │        30.46 ║
 WV    ║ Killdeer           │    21 │          78 │        26.92 ║
 VT    ║ American kestrel   │    29 │         109 │        26.61 ║
 IA    ║ Killdeer           │    49 │         189 │        25.93 ║
 UT    ║ Horned lark        │   260 │        1049 │        24.79 ║
 WY    ║ Greater sage-grouse│    10 │          41 │        24.39 ║
 IN    ║ Mourning dove      │   179 │         773 │        23.16 ║
 LA    ║ Barn swallow       │   168 │         737 │        22.80 ║
 MD    ║ European starling  │    90 │         405 │        22.22 ║
 BC    ║ Red-tailed hawk    │     2 │           9 │        22.22 ║
5› joined|                                                       ]   sort-desc       5135 rows  [M]
</pre>




## Limit to rows with at least 20 collisions

Hmmm, many of the highest-ranking species-state combinations seem to come from \"states\" --- like the striped skunk that was struck in Nova Scotia --- with very few reported collisions. So let\'s limit the results to species-state combinations with at least 20 reports.

To do that, we\'ll use `z|`, VisiData\'s \"select by expression\" command.

First, type `z|` to raise the selection prompt. Then, type `count >= 20`:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 STATE ║ SPECIES            │ count♯│ state_total♯│↓pct_of_state%║                                 
 SK    ║ Gulls              │     1 │           1 │       100.00 ║
 NS    ║ Striped skunk      │     1 │           1 │       100.00 ║
 NL    ║ Snow bunting       │     1 │           1 │       100.00 ║
 MB    ║ Mallard            │     1 │           2 │        50.00 ║
 MB    ║ Cedar waxwing      │     1 │           2 │        50.00 ║
 AB    ║ Canada goose       │     1 │           2 │        50.00 ║
 AB    ║ Perching birds (y) │     1 │           2 │        50.00 ║
 PI    ║ Yellow bittern     │    72 │         173 │        41.62 ║
 CO    ║ Horned lark        │  1117 │        2914 │        38.33 ║
 HI    ║ Pacific golden-plo…│   329 │         873 │        37.69 ║
 AZ    ║ Mourning dove      │   134 │         438 │        30.59 ║
 MS    ║ Mourning dove      │    60 │         197 │        30.46 ║
 WV    ║ Killdeer           │    21 │          78 │        26.92 ║
 VT    ║ American kestrel   │    29 │         109 │        26.61 ║
 IA    ║ Killdeer           │    49 │         189 │        25.93 ║
 UT    ║ Horned lark        │   260 │        1049 │        24.79 ║
 WY    ║ Greater sage-grouse│    10 │          41 │        24.39 ║
 IN    ║ Mourning dove      │   179 │         773 │        23.16 ║
 LA    ║ Barn swallow       │   168 │         737 │        22.80 ║
 MD    ║ European starling  │    90 │         405 │        22.22 ║
 BC    ║ Red-tailed hawk    │     2 │           9 │        22.22 ║
select by expr: count >= 20                                   z|   select-expr       5135 rows  [M]
</pre>


Next, press `Enter` to complete the action. Now you should see something like this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 STATE ║ SPECIES            │ count♯│ state_total♯│↓pct_of_state%║                                 
 SK    ║ Gulls              │     1 │           1 │       100.00 ║
 NS    ║ Striped skunk      │     1 │           1 │       100.00 ║
 NL    ║ Snow bunting       │     1 │           1 │       100.00 ║
 MB    ║ Mallard            │     1 │           2 │        50.00 ║
 MB    ║ Cedar waxwing      │     1 │           2 │        50.00 ║
 AB    ║ Canada goose       │     1 │           2 │        50.00 ║
 AB    ║ Perching birds (y) │     1 │           2 │        50.00 ║
•PI    ║ Yellow bittern     │    72 │         173 │        41.62 ║
•CO    ║ Horned lark        │  1117 │        2914 │        38.33 ║
•HI    ║ Pacific golden-plo…│   329 │         873 │        37.69 ║
•AZ    ║ Mourning dove      │   134 │         438 │        30.59 ║
•MS    ║ Mourning dove      │    60 │         197 │        30.46 ║
•WV    ║ Killdeer           │    21 │          78 │        26.92 ║
•VT    ║ American kestrel   │    29 │         109 │        26.61 ║
•IA    ║ Killdeer           │    49 │         189 │        25.93 ║
•UT    ║ Horned lark        │   260 │        1049 │        24.79 ║
 WY    ║ Greater sage-grouse│    10 │          41 │        24.39 ║
•IN    ║ Mourning dove      │   179 │         773 │        23.16 ║
•LA    ║ Barn swallow       │   168 │         737 │    ┌─────────────────────────────| statuses |─┐
•MD    ║ European starling  │    90 │         405 │    │ selected 498 rows                        │
 BC    ║ Red-tailed hawk    │     2 │           9 │    └──────────────────────────────────────────┘
5› joined|                                              z|   select-expr       5135 rows  [M] •498 
</pre>


Finally, press `"` to create a new sheet containing only the selected rows:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 STATE ║ SPECIES            │ count♯│ state_total♯│↓pct_of_state%║                                 
 PI    ║ Yellow bittern     │    72 │         173 │        41.62 ║
 CO    ║ Horned lark        │  1117 │        2914 │        38.33 ║
 HI    ║ Pacific golden-plo…│   329 │         873 │        37.69 ║
 AZ    ║ Mourning dove      │   134 │         438 │        30.59 ║
 MS    ║ Mourning dove      │    60 │         197 │        30.46 ║
 WV    ║ Killdeer           │    21 │          78 │        26.92 ║
 VT    ║ American kestrel   │    29 │         109 │        26.61 ║
 IA    ║ Killdeer           │    49 │         189 │        25.93 ║
 UT    ║ Horned lark        │   260 │        1049 │        24.79 ║
 IN    ║ Mourning dove      │   179 │         773 │        23.16 ║
 LA    ║ Barn swallow       │   168 │         737 │        22.80 ║
 MD    ║ European starling  │    90 │         405 │        22.22 ║
 TX    ║ Mourning dove      │   984 │        4670 │        21.07 ║
 NH    ║ American kestrel   │    24 │         117 │        20.51 ║
 PI    ║ Pacific golden-plo…│    35 │         173 │        20.23 ║
 SC    ║ Killdeer           │    45 │         229 │        19.65 ║
 ID    ║ American kestrel   │    30 │         172 │        17.44 ║
 VA    ║ Mourning dove      │    92 │         544 │        16.91 ║
 VA    ║ Killdeer           │    89 │         544 │        16.36 ║                                 
 NE    ║ Barn swallow       │    68 │         419 │        16.23 ║                                 
 AR    ║ Mourning dove      │    30 │         187 │        16.04 ║                                 
6› joined_selectedref|                                                        "           498 rows 
</pre>


There you have it! The [Yellow Bittern](https://en.wikipedia.org/wiki/Yellow_bittern) accounted for more than 40% of the reported, known-species collisions in \"PI\" (the [FAA\'s abbreviation](https://www.faa.gov/airports/airport_safety/wildlife/resources/media/2005_FAA_Manual_complete.pdf) for \"USA-possessed Pacific Islands,\" such as Guam). In Colorado, the Horned Lark has been nearly as collision-dominating, as has the Pacific Golden-Plover in Hawaii, and Mourning Doves in Arizona and Mississippi.


## Take it one step further

What if we want to find the species that are *disproportionately* involved in collisions in their state? How would you do that? (Hint: It involves just one more frequency table and one more join.)



## Open the wildlife-strikes dataset in VisiData

Let\'s start from the very beginning.

Run this command in your terminal:

    vd faa-wildlife-strikes.csv

If it worked, you should see something like this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 OPERATOR           │ ATYPE        │ INCIDENT_DATE     │ STATE │ AIRPORT            │ PHASE_OF_FLT>
 BUSINESS           │ PA-28        │ 05/22/15 00:00:00 │ FL    │ VERO BEACH MUNICIP…│ APPROACH     │
 BUSINESS           │ BE-1900      │ 06/18/15 00:00:00 │ AK    │ KENAI MUNICIPAL AR…│ APPROACH     │
 BUSINESS           │ PA-46 MALIBU │ 09/20/15 00:00:00 │ TX    │ DAVID WAYNE HOOKS …│              │
 DELTA AIR LINES    │ B-717-200    │ 11/07/15 00:00:00 │ MO    │ LAMBERT-ST LOUIS I…│ APPROACH     │
 BUSINESS           │ BE-90 KING   │ 12/17/15 00:00:00 │ FL    │ POMPANO BEACH AIRP…│ LANDING ROLL │
 DELTA AIR LINES    │ B-757        │ 07/17/15 00:00:00 │ VI    │ HENRY E ROHLSEN AR…│              │
 DELTA AIR LINES    │ B-717-200    │ 08/02/15 00:00:00 │ TX    │ SAN ANTONIO INTL   │ APPROACH     │
 BUSINESS           │ C-414        │ 08/03/15 00:00:00 │ TX    │ LONE STAR EXECUTIV…│ DEPARTURE    │
 ALLEGIANT AIR      │ MD-80        │ 09/02/15 00:00:00 │ FL    │ TAMPA INTL         │ APPROACH     │
 TRANS STATES AIRLI…│ EMB-145      │ 09/07/15 00:00:00 │ MO    │ LAMBERT-ST LOUIS I…│ APPROACH     │
 BUSINESS           │ C-172        │ 11/28/15 00:00:00 │ FL    │ OPA-LOCKA EXECUTIV…│ APPROACH     │
 GOVERNMENT         │ EC120        │ 12/08/15 00:00:00 │ CA    │ NORMAN Y. MINETA S…│              │
 AMERICAN AIRLINES  │ A-321        │ 05/06/15 00:00:00 │ FL    │ FORT LAUDERDALE/HO…│ APPROACH     │
 EXPRESSJET AIRLINES│ CRJ100/200   │ 05/06/15 00:00:00 │ AR    │ FORT SMITH REGIONA…│ CLIMB        │
 MESA AIRLINES      │ CRJ900       │ 05/08/15 00:00:00 │ AR    │ BILL AND  HILLARY …│ LANDING ROLL │
 BUSINESS           │ HELICOPTER   │ 05/06/15 00:0┌──────────────────────────────────| statuses |─┐│
 DELTA AIR LINES    │ A-320        │ 05/07/15 00:0│ saul.pw/VisiData v3.0.2                       ││
 DELTA AIR LINES    │ A-320        │ 05/08/15 00:0│ opening datasets/faa-wildlife-strikes.csv as  ││
 LUFTHANSA          │ A-380        │ 05/10/15 00:0│ csv                                           ││
 BUSINESS           │ C-172        │ 05/08/15 00:0│ Take a breath.                                ││
 SPIRIT AIRLINES    │ A-319        │ 05/10/15 00:0└───────────────────────────────────────────────┘│
1› faa-wildlife-strikes|                                                                73448 rows 
</pre>



## Tell VisiData that `HEIGHT` is an integer column

Navigate to the `HEIGHT` column, and press `#`.

You should see something like this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
<STATE │ AIRPORT            │ PHASE_OF_FLT │ HEIGHT#│ SPEED │ SPECIES            │ BIRDS_STRUCK │ >
 FL    │ VERO BEACH MUNICIP…│ APPROACH     │       !│       │ Unknown bird       │ 1            │ N 
 AK    │ KENAI MUNICIPAL AR…│ APPROACH     │       !│       │ Unknown bird       │ 1            │ N 
 TX    │ DAVID WAYNE HOOKS …│              │       !│       │ Unknown bird       │ 1            │ N 
 MO    │ LAMBERT-ST LOUIS I…│ APPROACH     │       !│       │ Unknown bird       │ 1            │ N 
 FL    │ POMPANO BEACH AIRP…│ LANDING ROLL │      0 │       │ Unknown bird       │ 1            │   
 VI    │ HENRY E ROHLSEN AR…│              │       !│       │ Unknown bird       │ 1            │ O 
 TX    │ SAN ANTONIO INTL   │ APPROACH     │       !│       │ Unknown bird       │ 1            │ N 
 TX    │ LONE STAR EXECUTIV…│ DEPARTURE    │       !│       │ Unknown bird       │ 1            │ P 
 FL    │ TAMPA INTL         │ APPROACH     │   6000 │       │ Unknown bird       │ 1            │ N 
 MO    │ LAMBERT-ST LOUIS I…│ APPROACH     │       !│       │ Owls               │ 1            │ N 
 FL    │ OPA-LOCKA EXECUTIV…│ APPROACH     │       !│       │ Hawks              │ 1            │ N 
 CA    │ NORMAN Y. MINETA S…│              │       !│       │ Gulls              │ 1            │ N 
 FL    │ FORT LAUDERDALE/HO…│ APPROACH     │   1500 │       │ Unknown bird - sma…│ 1            │ N 
 AR    │ FORT SMITH REGIONA…│ CLIMB        │       !│       │ Unknown bird - sma…│ 1            │ N 
 AR    │ BILL AND  HILLARY …│ LANDING ROLL │      0 │       │ Unknown bird - sma…│ 1            │ N 
       │ UNKNOWN            │ En Route     │       !│       │ Unknown bird       │ 1            │ P 
 CA    │ METRO OAKLAND INTL │              │       !│       │ Unknown bird       │ 1            │ N 
 UT    │ SALT LAKE CITY INTL│              │       !│       │ Unknown bird       │ 1            │ N 
 TX    │ GEORGE BUSH INTERC…│ CLIMB        │       !│       │ Unknown bird       │ 1            │ N 
 FL    │ ORLANDO SANFORD IN…│ APPROACH     │       !│       │ Unknown bird       │ 1            │ N 
 IL    │ CHICAGO O'HARE INT…│ CLIMB        │  12000 │       │ Unknown bird       │ 1            │ P 
1› faa-wildlife-strikes|                                              #   type-int      73448 rows 
</pre>


As you can see, many of the reported collisions are missing height data, or appear to have occurred on the ground (i.e., `HEIGHT == 0`).

So, let\'s focus only on collsions reported to have occurred above the ground.



## Select only rows where `HEIGHT` is greater than zero

To do that, we\'ll use `z|`, VisiData\'s \"select by expression\" command. Type `z|` and then, at the prompt, type `HEIGHT > 0`. You should see something like this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
<STATE │ AIRPORT            │ PHASE_OF_FLT │ HEIGHT#│ SPEED │ SPECIES            │ BIRDS_STRUCK │ >
 FL    │ VERO BEACH MUNICIP…│ APPROACH     │       !│       │ Unknown bird       │ 1            │ N 
 AK    │ KENAI MUNICIPAL AR…│ APPROACH     │       !│       │ Unknown bird       │ 1            │ N 
 TX    │ DAVID WAYNE HOOKS …│              │       !│       │ Unknown bird       │ 1            │ N 
 MO    │ LAMBERT-ST LOUIS I…│ APPROACH     │       !│       │ Unknown bird       │ 1            │ N 
 FL    │ POMPANO BEACH AIRP…│ LANDING ROLL │      0 │       │ Unknown bird       │ 1            │   
 VI    │ HENRY E ROHLSEN AR…│              │       !│       │ Unknown bird       │ 1            │ O 
 TX    │ SAN ANTONIO INTL   │ APPROACH     │       !│       │ Unknown bird       │ 1            │ N 
 TX    │ LONE STAR EXECUTIV…│ DEPARTURE    │       !│       │ Unknown bird       │ 1            │ P 
 FL    │ TAMPA INTL         │ APPROACH     │   6000 │       │ Unknown bird       │ 1            │ N 
 MO    │ LAMBERT-ST LOUIS I…│ APPROACH     │       !│       │ Owls               │ 1            │ N 
 FL    │ OPA-LOCKA EXECUTIV…│ APPROACH     │       !│       │ Hawks              │ 1            │ N 
 CA    │ NORMAN Y. MINETA S…│              │       !│       │ Gulls              │ 1            │ N 
 FL    │ FORT LAUDERDALE/HO…│ APPROACH     │   1500 │       │ Unknown bird - sma…│ 1            │ N 
 AR    │ FORT SMITH REGIONA…│ CLIMB        │       !│       │ Unknown bird - sma…│ 1            │ N 
 AR    │ BILL AND  HILLARY …│ LANDING ROLL │      0 │       │ Unknown bird - sma…│ 1            │ N 
       │ UNKNOWN            │ En Route     │       !│       │ Unknown bird       │ 1            │ P 
 CA    │ METRO OAKLAND INTL │              │       !│       │ Unknown bird       │ 1            │ N 
 UT    │ SALT LAKE CITY INTL│              │       !│       │ Unknown bird       │ 1            │ N 
 TX    │ GEORGE BUSH INTERC…│ CLIMB        │       !│       │ Unknown bird       │ 1            │ N 
 FL    │ ORLANDO SANFORD IN…│ APPROACH     │       !│       │ Unknown bird       │ 1            │ N 
 IL    │ CHICAGO O'HARE INT…│ CLIMB        │  12000 │       │ Unknown bird       │ 1            │ P 
select by expr: HEIGHT > 0                                        z|   select-expr      73448 rows 
</pre>


Then press `Enter`. Now you you should see the above-ground collisions selected:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
<STATE │ AIRPORT            │ PHASE_OF_FLT │ HEIGHT#│ SPEED │ SPECIES            │ BIRDS_STRUCK │ >
 FL    │ VERO BEACH MUNICIP…│ APPROACH     │       !│       │ Unknown bird       │ 1            │ N 
 AK    │ KENAI MUNICIPAL AR…│ APPROACH     │       !│       │ Unknown bird       │ 1            │ N 
 TX    │ DAVID WAYNE HOOKS …│              │       !│       │ Unknown bird       │ 1            │ N 
 MO    │ LAMBERT-ST LOUIS I…│ APPROACH     │       !│       │ Unknown bird       │ 1            │ N 
 FL    │ POMPANO BEACH AIRP…│ LANDING ROLL │      0 │       │ Unknown bird       │ 1            │   
 VI    │ HENRY E ROHLSEN AR…│              │       !│       │ Unknown bird       │ 1            │ O 
 TX    │ SAN ANTONIO INTL   │ APPROACH     │       !│       │ Unknown bird       │ 1            │ N 
 TX    │ LONE STAR EXECUTIV…│ DEPARTURE    │       !│       │ Unknown bird       │ 1            │ P 
•FL    │ TAMPA INTL         │ APPROACH     │   6000 │       │ Unknown bird       │ 1            │ N 
 MO    │ LAMBERT-ST LOUIS I…│ APPROACH     │       !│       │ Owls               │ 1            │ N 
 FL    │ OPA-LOCKA EXECUTIV…│ APPROACH     │       !│       │ Hawks              │ 1            │ N 
 CA    │ NORMAN Y. MINETA S…│              │       !│       │ Gulls              │ 1            │ N 
•FL    │ FORT LAUDERDALE/HO…│ APPROACH     │   1500 │       │ Unknown bird - sma…│ 1            │ N 
 AR    │ FORT SMITH REGIONA…│ CLIMB        │       !│       │ Unknown bird - sma…│ 1            │ N 
 AR    │ BILL AND  HILLARY …│ LANDING ROLL │      0 │       │ Unknown bird - sma…│ 1            │ N 
       │ UNKNOWN            │ En Route     │       !│       │ Unknown bird       │ 1            │ P 
 CA    │ METRO OAKLAND INTL │              │       !│       │ Unknown bird       │ 1            │ N 
 UT    │ SALT LAKE CITY INTL│              │       !│       │ Unknown bird       │ 1            │ N 
 TX    │ GEORGE BUSH INTERC…│ CLIMB        │       !│  ┌─────────────────────────────| statuses |─┐ 
 FL    │ ORLANDO SANFORD IN…│ APPROACH     │       !│  │ selected 22883 rows                      │ 
•IL    │ CHICAGO O'HARE INT…│ CLIMB        │  12000 │  └──────────────────────────────────────────┘ 
1› faa-wildlife-strikes|                                  z|   select-expr      73448 rows  •22883 
</pre>



## Create a new sheet with only the selected rows

To do so, press `"`. Once you do that, you should see something like this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
<STATE │ AIRPORT            │ PHASE_OF_FLT │ HEIGHT#│ SPEED │ SPECIES            │ BIRDS_STRUCK │ >
 FL    │ TAMPA INTL         │ APPROACH     │   6000 │       │ Unknown bird       │ 1            │ N 
 FL    │ FORT LAUDERDALE/HO…│ APPROACH     │   1500 │       │ Unknown bird - sma…│ 1            │ N 
 IL    │ CHICAGO O'HARE INT…│ CLIMB        │  12000 │       │ Unknown bird       │ 1            │ P 
 FL    │ TAMPA INTL         │ APPROACH     │     50 │       │ Unknown bird       │ 1            │ N 
 OR    │ SOUTHWEST OREGON R…│ APPROACH     │    300 │       │ Unknown bird       │ 1            │ N 
 ME    │ PORTLAND INTL JETP…│ CLIMB        │   1000 │       │ Unknown bird       │ 1            │ N 
 VA    │ ROANOKE REGNL ARPT…│ APPROACH     │   3000 │       │ Unknown bird       │ 1            │ N 
 FL    │ MIAMI INTL         │ APPROACH     │    400 │       │ Unknown bird       │ 1            │ N 
 NY    │ SYRACUSE HANCOCK I…│ APPROACH     │    200 │       │ Unknown bird       │ 1            │ N 
       │ UNKNOWN            │ EN ROUTE     │   8000 │       │ Unknown bird       │ 1            │ P 
 PA    │ PITTSBURGH INTL AR…│ APPROACH     │   6000 │       │ Unknown bird       │ 1            │ N 
 MD    │ BALTIMORE/WASH INT…│ APPROACH     │   1000 │       │ Unknown bird       │ 1            │ N 
 NC    │ RALEIGH-DURHAM INTL│ APPROACH     │   1000 │       │ Unknown bird       │ 1            │ N 
 MI    │ WILLOW RUN ARPT    │ APPROACH     │   3000 │       │ Unknown bird - lar…│ 1            │ N 
 AK    │ TED STEVENS ANCHOR…│ APPROACH     │    100 │       │ Unknown bird       │ 1            │ N 
       │ UNKNOWN            │ LOCAL        │     80 │       │ Unknown bird       │ 1            │ N 
 DC    │ RONALD REAGAN WASH…│ APPROACH     │    100 │       │ Unknown bird       │ 1            │ N 
 AL    │ BIRMINGHAM-SHUTTLE…│ APPROACH     │   1100 │       │ Unknown bird       │ 1            │ N 
 NY    │ LA GUARDIA ARPT    │ CLIMB        │    400 │       │ Unknown bird       │ 1            │ N 
 CA    │ JOHN WAYNE-ORANGE …│ APPROACH     │   1700 │       │ Unknown bird - med…│ 1            │ N 
 FL    │ TAMPA INTL         │ APPROACH     │   1000 │       │ Unknown bird       │ 1            │ N 
2› faa-wildlife-strikes_selectedref|                                          "         22883 rows 
</pre>




## Get the average collision height for each species

This is a two-step process. First, navigate to the `HEIGHT` column, and press `+` to add an aggregator. At the prompt at the bottom of the screen, type `mean` \...


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
<STATE │ AIRPORT            │ PHASE_OF_FLT │ HEIGHT#│ SPEED │ SPECIES            │ BIRDS_STRUCK │ >
 FL    │ TAMPA INTL         │ APPROACH     │   6000 │       │ Unknown bird       │ 1            │ N 
 FL    │ FORT LAUDERDALE/HO…│ APPROACH     │   1500 │       │ Unknown bird - sma…│ 1            │ N 
 IL    │ CHICAGO O'HARE INT…│ CLIMB        │  12000 │       │ Unknown bird       │ 1            │ P 
 FL    │ TAMPA INTL         │ APPROACH     │     50 │       │ Unknown bird       │ 1            │ N 
 OR    │ SOUTHWEST OREGON R…│ APPROACH     │    300 │    ┌─────────────────| Choose Aggregators |─┐ 
 ME    │ PORTLAND INTL JETP…│ CLIMB        │   1000 │    │ Start typing an aggregator name or     │ 
 VA    │ ROANOKE REGNL ARPT…│ APPROACH     │   3000 │    │ description.                           │ 
 FL    │ MIAMI INTL         │ APPROACH     │    400 │    │ Multiple aggregators can be added by   │ 
 NY    │ SYRACUSE HANCOCK I…│ APPROACH     │    200 │    │ separating spaces.                     │ 
       │ UNKNOWN            │ EN ROUTE     │   8000 │    │                                        │ 
 PA    │ PITTSBURGH INTL AR…│ APPROACH     │   6000 │    │ - Enter to select top aggregator.      │ 
                   mean - arithmetic mean of values      │ - Tab to highlight top aggregator.     │ 
                   median - median of values             │                                        │ 
                   avg - arithmetic mean of values       │ ## When Aggregator Highlighted         │ 
                   min - minimum value                   │                                        │ 
                   max - maximum value                   │ - Tab/Shift+Tab to cycle highlighted   │ 
                   mode - mode of values                 │ aggregator.                            │ 
                   sum - sum of values                   │ - Enter to select aggregators.         │ 
                   distinct - distinct values            │ - Space to add highlighted aggregator. │ 
                   count - number of values              │ - 0-9 to add numbered aggregator.      │ 
                   list - list of values                 └────────────────────────────────────────┘ 
choose aggregators: mean                                         +   aggregate-col      22883 rows 
</pre>


\... and then press `Enter`.

:::: note
::: title
Note

Adding an aggregator doesn\'t change the appearance of the sheet. But if you want to confirm that you\'ve added an aggregator correctly, you can press `Shift-C` to open up the Columns Sheet, and look at the `aggregators` field.

Then, to get the average for each animal, navigate to the `SPECIES` column, and press `Shift-F` to create a frequency sheet. It should look something like this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 SPECIES            ║↓count♯│ percent%│ histogram                             ~│ HEIGHT_mean%║     
 Unknown bird       ║  2098 │    9.17 │ ■■■■■■■■■                              │            !║
 Unknown bird - sma…║  8807 │   38.49 │ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ │            !║
 Unknown bird - lar…║   693 │    3.03 │ ■■                                     │            !║
 Unknown bird - med…║  3056 │   13.35 │ ■■■■■■■■■■■■■                          │            !║
 Gulls              ║   550 │    2.40 │ ■■                                     │            !║
 Northern pintail   ║    64 │    0.28 │                                        │            !║
 Barred owl         ║     3 │    0.01 │                                        │            !║
 Common raven       ║     4 │    0.02 │                                        │            !║
 Great blue heron   ║    38 │    0.17 │                                        │            !║
 American robin     ║   183 │    0.80 │                                        │            !║
 Rock pigeon        ║   219 │    0.96 │                                        │            !║
 Eastern meadowlark ║    77 │    0.34 │                                        │            !║
 Hawks              ║   131 │    0.57 │                                        │            !║
 Bald eagle         ║    42 │    0.18 │                                        │            !║
 Bonin petrel       ║     3 │    0.01 │                                        │            !║
 Killdeer           ║   199 │    0.87 │                                        │            !║
 Doves              ║    72 │    0.31 │                                        │            !║
 Turkey vulture     ║   178 │    0.78 │                                        │            !║
 Western meadowlark ║    52 │    0.23 │                                        │            !║
 Red-tailed hawk    ║   190 │    0.83 │                                        │            !║
 Rough-legged hawk  ║     6 │    0.03 │                                        │            !║
3› faa-wildlife-strikes_selectedref_SPECIES_freq|           processing… Shift+F           420 bins 
</pre>



## Sort the species by collision height

By default, frequency tables are sorted by the raw count of matching rows. To sort by the highest average collision height, navigate to the `mean_HEIGHT` column, and press `]`.

You should see something like this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 SPECIES            ║ count♯│↓HEIGHT_mean%║                                                        
 Eared grebe        ║     1 │    20000.00 ║
 Long-billed curlew ║     1 │    15000.00 ║
 Whimbrel           ║     1 │    12000.00 ║
 Lesser yellowlegs  ║     4 │     9925.00 ║
 Dusky flycatcher   ║     1 │     9500.00 ║
 Sanderling         ║     1 │     9500.00 ║
 Red-necked phalaro…║     4 │     8525.00 ║
 Clark's grebe      ║     1 │     8500.00 ║
 Northern saw-whet …║     1 │     8000.00 ║
 Grebes             ║     1 │     8000.00 ║
 Spotted sandpiper  ║     1 │     7700.00 ║
 Least flycatcher   ║     3 │     7566.67 ║
 Lark sparrow       ║     2 │     7400.00 ║
 Greater yellowlegs ║     3 │     7333.33 ║
 Pacific-slope flyc…║     3 │     7000.00 ║
 Seminole bat       ║     1 │     7000.00 ║
 Solitary sandpiper ║     2 │     6250.00 ║
 Pocketed free-tail…║     1 │     6000.00 ║
 Red-naped sapsucker║     2 │     5750.00 ║
 Cinnamon teal      ║     1 │     5600.00 ║
 Horned grebe       ║     2 │     5400.00 ║
3› faa-wildlife-strikes_selectedref_SPECIES_freq|                    ]   sort-desc        420 bins 
</pre>


Hrrrm, it seems like a lot of these species show up just a few times --- too few to be particularly informative. Let\'s do something about that.



## Limit the results to relatively common species

This step will seem familiar; it\'s a lot like how we selected only above-the-ground collisions.

First, type `z|` to raise the \"select by expression\" prompt. Then, type `count >= 20`:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 SPECIES            ║ count♯│↓HEIGHT_mean%║                                                        
 Eared grebe        ║     1 │    20000.00 ║
 Long-billed curlew ║     1 │    15000.00 ║
 Whimbrel           ║     1 │    12000.00 ║
 Lesser yellowlegs  ║     4 │     9925.00 ║
 Dusky flycatcher   ║     1 │     9500.00 ║
 Sanderling         ║     1 │     9500.00 ║
 Red-necked phalaro…║     4 │     8525.00 ║
 Clark's grebe      ║     1 │     8500.00 ║
 Northern saw-whet …║     1 │     8000.00 ║
 Grebes             ║     1 │     8000.00 ║
 Spotted sandpiper  ║     1 │     7700.00 ║
 Least flycatcher   ║     3 │     7566.67 ║
 Lark sparrow       ║     2 │     7400.00 ║
 Greater yellowlegs ║     3 │     7333.33 ║
 Pacific-slope flyc…║     3 │     7000.00 ║
 Seminole bat       ║     1 │     7000.00 ║
 Solitary sandpiper ║     2 │     6250.00 ║
 Pocketed free-tail…║     1 │     6000.00 ║
 Red-naped sapsucker║     2 │     5750.00 ║
 Cinnamon teal      ║     1 │     5600.00 ║
 Horned grebe       ║     2 │     5400.00 ║
select by expr: count >= 20                                       z|   select-expr        420 bins 
</pre>


Next, press `Enter` to complete the action. Because there are no high-count species in the visible part of the sheet, you won\'t notice much of effect at first; just some status messages in the sidebar:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 SPECIES            ║ count♯│↓HEIGHT_mean%║            ┌─────────────────────────────| statuses |─┐
 Eared grebe        ║     1 │    20000.00 ║            │ selected 24 rows                         │
 Long-billed curlew ║     1 │    15000.00 ║            │ [3x] selected 56 more rows               │
 Whimbrel           ║     1 │    12000.00 ║            │ [2x] selected 34 more rows               │
 Lesser yellowlegs  ║     4 │     9925.00 ║            │ [2x] selected 49 more rows               │
 Dusky flycatcher   ║     1 │     9500.00 ║            │ [2x] selected 39 more rows               │
 Sanderling         ║     1 │     9500.00 ║            │ selected 693 more rows                   │
 Red-necked phalaro…║     4 │     8525.00 ║            │ selected 23 more rows                    │
 Clark's grebe      ║     1 │     8500.00 ║            │ selected 183 more rows                   │
 Northern saw-whet …║     1 │     8000.00 ║            │ [2x] selected 32 more rows               │
 Grebes             ║     1 │     8000.00 ║            │ selected 3056 more rows                  │
 Spotted sandpiper  ║     1 │     7700.00 ║            │ selected 2098 more rows                  │
 Least flycatcher   ║     3 │     7566.67 ║            │ selected 211 more rows                   │
 Lark sparrow       ║     2 │     7400.00 ║            │ selected 64 more rows                    │
 Greater yellowlegs ║     3 │     7333.33 ║            │ selected 53 more rows                    │
 Pacific-slope flyc…║     3 │     7000.00 ║            │ selected 43 more rows                    │
 Seminole bat       ║     1 │     7000.00 ║            │ [4x] selected 20 more rows               │
 Solitary sandpiper ║     2 │     6250.00 ║            │ [3x] selected 25 more rows               │
 Pocketed free-tail…║     1 │     6000.00 ║            │ selected 37 more rows                    │
 Red-naped sapsucker║     2 │     5750.00 ║            │ selected 60 more rows                    │
 Cinnamon teal      ║     1 │     5600.00 ║            │ [2x] selected 48 more rows               │
 Horned grebe       ║     2 │     5400.00 ║            └───| Ctrl+P to view all status messages |[┘
3› faa-wildlife-strikes_selectedref_SPECIES_freq|            z|   select-expr        420 bins  •75 
</pre>


Now press `"` to create a new sheet containing only the selected rows. Tada!:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 SPECIES            ║ count♯│↓HEIGHT_mean%║                                                        
 Yellow-bellied sap…║    24 │     3585.42 ║                                                        
 Swainson's thrush  ║    56 │     3454.46 ║                                                        
 Snow goose         ║    34 │     3258.82 ║                                                        
 Hermit thrush      ║    49 │     2770.10 ║                                                        
 Red-eyed vireo     ║    39 │     2768.72 ║                                                        
 Unknown bird - lar…║   693 │     2691.92 ║                                                        
 Northern shoveler  ║    23 │     2602.17 ║                                                        
 American robin     ║   183 │     2545.00 ║                                                        
 White-throated spa…║    56 │     2426.79 ║                                                        
 Greater white-fron…║    32 │     2335.94 ║                                                        
 Unknown bird - med…║  3056 │     2260.49 ║                                                        
 Unknown bird       ║  2098 │     2253.93 ║                                                        
 Dark-eyed junco    ║    39 │     2031.28 ║                                                        
 Perching birds (y) ║   211 │     2018.73 ║                                                        
 Northern pintail   ║    64 │     1980.19 ║                                                        
 American coot      ║    53 │     1965.66 ║                                                        
 Unknown bird or bat║    43 │     1892.88 ║                                                        
 Red bat            ║    20 │     1750.00 ║                                                        
 Geese              ║    56 │     1696.88 ║                                                        
 Gadwall            ║    25 │     1675.80 ║                                                        
 Gray catbird       ║    37 │     1573.27 ║                                                        
4› faa-wildlife-strikes_selectedref_SPECIES_freq_selectedref|                 "            75 bins 
</pre>


Finally, type `g_` to widen all the columns, so that you can read all the names:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 SPECIES                     ║ count♯│↓HEIGHT_mean%║                                               
 Yellow-bellied sapsucker    ║    24 │     3585.42 ║                                               
 Swainson's thrush           ║    56 │     3454.46 ║                                               
 Snow goose                  ║    34 │     3258.82 ║                                               
 Hermit thrush               ║    49 │     2770.10 ║                                               
 Red-eyed vireo              ║    39 │     2768.72 ║                                               
 Unknown bird - large        ║   693 │     2691.92 ║                                               
 Northern shoveler           ║    23 │     2602.17 ║                                               
 American robin              ║   183 │     2545.00 ║                                               
 White-throated sparrow      ║    56 │     2426.79 ║                                               
 Greater white-fronted goose ║    32 │     2335.94 ║                                               
 Unknown bird - medium       ║  3056 │     2260.49 ║                                               
 Unknown bird                ║  2098 │     2253.93 ║                                               
 Dark-eyed junco             ║    39 │     2031.28 ║                                               
 Perching birds (y)          ║   211 │     2018.73 ║                                               
 Northern pintail            ║    64 │     1980.19 ║                                               
 American coot               ║    53 │     1965.66 ║                                               
 Unknown bird or bat         ║    43 │     1892.88 ║                                               
 Red bat                     ║    20 │     1750.00 ║                                               
 Geese                       ║    56 │     1696.88 ║                                               
 Gadwall                     ║    25 │     1675.80 ║                                               
 Gray catbird                ║    37 │     1573.27 ║                                               
4› faa-wildlife-strikes_selectedref_SPECIES_freq_selectedref| g_   resize-cols-max         75 bins 
</pre>



## Step 1: Use `vd` to open a data file

Download `faa-wildlife-strikes.csv <../../datasets/faa-wildlife-strikes.csv>`, a dataset of all aircraft-wildlife collisions [reported to the Federal Aviation Administration](https://wildlife.faa.gov/database.aspx) between 2010 and mid-2016.

From your terminal, move into the directory where you downloaded the dataset. Then run the following command:

    vd faa-wildlife-strikes.csv

If it worked, you should see something like this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 OPERATOR           │ ATYPE        │ INCIDENT_DATE     │ STATE │ AIRPORT            │ PHASE_OF_FLT>
 BUSINESS           │ PA-28        │ 05/22/15 00:00:00 │ FL    │ VERO BEACH MUNICIP…│ APPROACH     │
 BUSINESS           │ BE-1900      │ 06/18/15 00:00:00 │ AK    │ KENAI MUNICIPAL AR…│ APPROACH     │
 BUSINESS           │ PA-46 MALIBU │ 09/20/15 00:00:00 │ TX    │ DAVID WAYNE HOOKS …│              │
 DELTA AIR LINES    │ B-717-200    │ 11/07/15 00:00:00 │ MO    │ LAMBERT-ST LOUIS I…│ APPROACH     │
 BUSINESS           │ BE-90 KING   │ 12/17/15 00:00:00 │ FL    │ POMPANO BEACH AIRP…│ LANDING ROLL │
 DELTA AIR LINES    │ B-757        │ 07/17/15 00:00:00 │ VI    │ HENRY E ROHLSEN AR…│              │
 DELTA AIR LINES    │ B-717-200    │ 08/02/15 00:00:00 │ TX    │ SAN ANTONIO INTL   │ APPROACH     │
 BUSINESS           │ C-414        │ 08/03/15 00:00:00 │ TX    │ LONE STAR EXECUTIV…│ DEPARTURE    │
 ALLEGIANT AIR      │ MD-80        │ 09/02/15 00:00:00 │ FL    │ TAMPA INTL         │ APPROACH     │
 TRANS STATES AIRLI…│ EMB-145      │ 09/07/15 00:00:00 │ MO    │ LAMBERT-ST LOUIS I…│ APPROACH     │
 BUSINESS           │ C-172        │ 11/28/15 00:00:00 │ FL    │ OPA-LOCKA EXECUTIV…│ APPROACH     │
 GOVERNMENT         │ EC120        │ 12/08/15 00:00:00 │ CA    │ NORMAN Y. MINETA S…│              │
 AMERICAN AIRLINES  │ A-321        │ 05/06/15 00:00:00 │ FL    │ FORT LAUDERDALE/HO…│ APPROACH     │
 EXPRESSJET AIRLINES│ CRJ100/200   │ 05/06/15 00:00:00 │ AR    │ FORT SMITH REGIONA…│ CLIMB        │
 MESA AIRLINES      │ CRJ900       │ 05/08/15 00:00:00 │ AR    │ BILL AND  HILLARY …│ LANDING ROLL │
 BUSINESS           │ HELICOPTER   │ 05/06/15 00:0┌──────────────────────────────────| statuses |─┐│
 DELTA AIR LINES    │ A-320        │ 05/07/15 00:0│ saul.pw/VisiData v3.0.2                       ││
 DELTA AIR LINES    │ A-320        │ 05/08/15 00:0│ opening datasets/faa-wildlife-strikes.csv as  ││
 LUFTHANSA          │ A-380        │ 05/10/15 00:0│ csv                                           ││
 BUSINESS           │ C-172        │ 05/08/15 00:0│ As if I would talk on such a subject!         ││
 SPIRIT AIRLINES    │ A-319        │ 05/10/15 00:0└───────────────────────────────────────────────┘│
1› faa-wildlife-strikes|                                                                73448 rows 
</pre>




## Step 2: Test-drive a frequency table

One of VisiData\'s strengths is how quickly it lets you summarize your data. Frequency tables are a great example. To create one, press `Shift+F`.

If it worked, you should see something like this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 OPERATOR           ║↓count♯│ percent%│ histogram                             ~║                   
 UNKNOWN            ║ 23076 │   31.42 │ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ║
 SOUTHWEST AIRLINES ║  7752 │   10.55 │ ■■■■■■■■■■■■                           ║
 BUSINESS           ║  5868 │    7.99 │ ■■■■■■■■■                              ║
 AMERICAN AIRLINES  ║  4337 │    5.90 │ ■■■■■■■                                ║
 DELTA AIR LINES    ║  2817 │    3.84 │ ■■■■                                   ║
 FEDEX EXPRESS      ║  2709 │    3.69 │ ■■■■                                   ║
 UNITED AIRLINES    ║  2194 │    2.99 │ ■■■                                    ║
 US AIRWAYS         ║  1885 │    2.57 │ ■■■                                    ║
 UPS AIRLINES       ║  1773 │    2.41 │ ■■                                     ║
 SKYWEST AIRLINES   ║  1769 │    2.41 │ ■■                                     ║
 JETBLUE AIRWAYS    ║  1740 │    2.37 │ ■■                                     ║
 EXPRESSJET AIRLINES║  1347 │    1.83 │ ■■                                     ║
 AMERICAN EAGLE AIR…║  1041 │    1.42 │ ■                                      ║
 ENVOY AIR          ║   883 │    1.20 │ ■                                      ║
 ALASKA AIRLINES    ║   835 │    1.14 │ ■                                      ║
 REPUBLIC AIRLINES  ║   804 │    1.09 │ ■                                      ║
 MESA AIRLINES      ║   693 │    0.94 │ ■                                      ║
 AIR WISCONSIN AIRL…║   623 │    0.85 │ ■                                      ║
 PSA AIRLINES       ║   577 │    0.79 │                                        ║
 PRIVATELY OWNED    ║   516 │    0.70 │                                        ║
 PHI INC            ║   491 │    0.67 │                                        ║
2› faa-wildlife-strikes_OPERATOR_freq|                                  Shift+F           282 bins 
</pre>



## Step 3: Explore the menu

Pressing `Control-h` will open VisiData\'s menu system, where you can explore the most common commands:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 OPERATOR           ║↓count♯│ percent%│ histogram   │ VisiData Feature Guides           ⎘│         
 UNKNOWN            ║ 23076 │   31.42 │ ■■■■■■■■■■■■│ Version                    Ctrl+V  │
 SOUTHWEST AIRLINES ║  7752 │   10.55 │ ■■■■■■■■■■■■│ VisiData tutorial                  │
 BUSINESS           ║  5868 │    7.99 │ ■■■■■■■■■   │ Sheet commands            zCtrl+H ⎘│
 AMERICAN AIRLINES  ║  4337 │    5.90 │ ■■■■■■■     │ All commands             gzCtrl+H ⎘│
 DELTA AIR LINES    ║  2817 │    3.84 │ ■■■■        │ Quick reference           gCtrl+H  │
 FEDEX EXPRESS      ║  2709 │    3.69 │ ■■■■        │ Command list              zCtrl+H ⎘│
 UNITED AIRLINES    ║  2194 │    2.99 │ ■■■         └────────────────────────────────────┘
 US AIRWAYS         ║  1885 │    2.57 │ ■■■                                    ║
 UPS AIRLINES       ║  1773 │    2.41 │ ■■                                     ║
 SKYWEST AIRLINES   ║  1769 │    2.41 │ ■■                                     ║
 JETBLUE AIRWAYS    ║  1740 │    2.37 │ ■■                                     ║
 EXPRESSJET AIRLINES║  1347 │    1.83 │ ■■                                     ║
 AMERICAN EAGLE AIR…║  1041 │    1.42 │ ■                                      ║
 ENVOY AIR          ║   883 │    1.20 │ ■                                      ║
 ALASKA AIRLINES    ║   835 │ ┌────────────────── open-guide-index ────────────────────────────┐
 REPUBLIC AIRLINES  ║   804 │ │ open VisiData guides table of contents                         │
 MESA AIRLINES      ║   693 │ │                                                                │
 AIR WISCONSIN AIRL…║   623 │ │    ⎘ pushes sheet                                              │
 PSA AIRLINES       ║   577 │ └────────────────────────────────────────────────────────────────┘
 PRIVATELY OWNED    ║   516 │    0.70 │                                        ║
 PHI INC            ║   491 │    0.67 │                                        ║
2› faa-wildlife-strikes_OPERATOR_freq|                            Bksp   menu-help        282 bins 
</pre>


You can navigate the menu either with your arrow keys or by pointing and clicking with your mouse. To run a command from the menu, press `Enter` or click a second time on the selected item.



## Why use VisiData?

- 

  It\'s fast.

  :   - VisiData opens in a blink of an eye, and can load multi-megabyte datasets nearly instantly.

- 

  It\'s nimble.

  :   - VisiData makes it easy to search, filter, sort, and join any table.

- 

  It\'s great for getting a grasp of new datasets.

  :   - With just a few keystrokes, you can summarize any column.

- 

  It works with `lots of data formats <compatible-filetypes>`.

  :   - CSV, Excel, JSON, and more.

- 

  It\'s non-destructive.

  :   - VisiData won\'t alter your raw data unless you explicitly tell it to.

- 

  It\'s keyboard-driven.

  :   - You never have to reach for a mouse.

- 

  It lives in your terminal.

  :   - VisiData plays well with other command-line tools, and you can run it on remote servers via SSH.


## Why not use VisiData?

VisiData isn\'t for every task. You might want to choose another tool for:

- 

  Complex analysis.

  :   - You\'re probably better off using Python, R, or another programming language.

- 

  \"Literate\" analysis.

  :   - Although VisiData lets you save and replay your analyses, it\'s not as legible/flexible as Jupyter notebooks, R Markdown, or other tools.

- 

  Mission-critical analysis.

  :   - VisiData is well-engineered, but still a relatively young piece of software.



## 2020-web-scraping-puppeteer.md

Web Scraping
with Puppeteer
Jon Keegan / The Markup
@jonkeegan
keegan@themarkup.org

Slides: http://bit.ly/nicar20-puppeteer
Simple: https://github.com/jonkeegan/nicar2020-scraping-workshop
Detailed: https://github.com/jonkeegan/nicar2020/


What is Puppeteer?
Puppeteer is Google’s Node library that can control headless Chrome
It can:
Take screenshots and PDFs of pages
Automate form submission, UI testing, keyboard input
Serve as a testing environment for JavaScript / web page rendering
Scrape web pages (save HTML)
https://developers.google.com/web/tools/puppeteer
https://github.com/puppeteer/puppeteer


Also helpful: Puppeteer Recorder Chrome plugin	
Add this plugin: https://chrome.google.com/webstore/detail/puppeteer-recorder/djeegiggegleadkkbgopoonhjimgehda?hl=en
Allows you to “record” your browsing and user interactions, and generates the Puppeteer node you need to reproduce those actions.
Record clicks, input events etc. 
Record screenshots.
Pause the recording when navigating.
Monitor recorded events.
Export to Puppeteer code.
Tweak the settings of the generated code.

https://pptr.dev/#?product=Puppeteer&version=v2.1.1&show=api-overview

Try it out: https://try-puppeteer.appspot.com/


You can try out a super simple interactive example here: https://try-puppeteer.appspot.com/


Process for collecting data
Collect			Just request the page you want, wait for it to load, then save it all.
Parse / extract		At your leisure, load that saved page, and grab the data you seek.
Transform		Take that data and add to a database, save it as JSON, etc.

Amazon Simple Queue Service

Your to do list of URLs
Amazon Elastic Container Service

Dockerized tasks are triggered by items in SQS

(This is where Puppeteer runs)
Amazon Simple Storage Service

Save all HTML, screenshots and JSON
Build a pipeline

What we will scrape
Louisiana's Air Monitoring Data 
for New Orleans City Park

http://airquality.deq.louisiana.gov/Data/Site/CITYPARK/Date/2020-01-26


Source for key descriptions: https://www.epa.gov/air-trends
TIME
The hour when the data was collected
ITEMP
The temperature in degrees celsius
PM10
Describes inhalable particles, with diameters that are generally 10 micrometers and smaller.
PM2.5	

Describes fine inhalable particles, with diameters that are generally 2.5 micrometers and smaller.
WDIR
The wind direction in degrees
WSP
The wind speed in miles per hour

A note about organization
Use a consistent structure that allows for an easy look at the latest data. 

document.querySelector("table.data")


Capture script

STEP 1 - add your includes. fs for file system, and puppeteer. And add the URL we are going to scrape

STEP 2 - Let’s define an empty `init` function, and add the line that calls it. 

STEP 3 - Add a try catch block with a console message 

STEP 4 - This is where we instantiate puppeteer in `browser`, and set the configurations. Create a newPage object 


Define the browser behaviors. This is where you control the puppet!

Save the HTML

Take and save a screenshot of the page. 

Parse script

Include fs, cheerio and HtmlTableToJson. Define the URL, and the saved HTML we want to parse.

Empty init function wrapper, and call it. 

Add a try / catch in here. 

Use Cheerio to parse the HTML file into an object that you can traverse. Extract the table that holds the data we want. 

Clean up code with regex. Parse the HTML table and quickly turn it into JSON.

Save some metadata for the collection. Write the file out. 

Test the scripts

node collect.js
CITYPARK_2020-01-26.html
CITYPARK_2020-01-26.png

node parse.js
CITYPARK_2020-01-26.json 
Run the script. 

This is how the data should look


## Class outline

1. 🐍 [Python basics](session/python-basics.ipynb) (45 minutes to 1 hour)
2. 💧 Water break! (10 minutes)
3. 🔣 [HTML Basics](session/web-scraping-with-python.ipynb#HTML-basics) (15 minutes)
4. 🛠 [Scraping the web](session/web-scraping-with-python.ipynb#Web-Scraping-with-Python) (Remaining time)



## You will learn...

- Some Python basics
  - Data types: String, numeric, and Boolean types
  - Data structures: Lists and dictionaries
  - Control flow: `if... else` statements
  - Iteration: `for... in` statements
  - Functions: Reusable bits of code
- How to write and run Python code using Jupyter Notebooks
  - Retrieve web content with [`requests`](https://requests.readthedocs.io/en/master/)
  - Parse meaningful information from raw HTML with [`beautifulsoup4`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
  - Output tabular data with [`csv`](https://docs.python.org/3/library/csv.html)
- How to inspect source code in your browser
- How to go about getting unstuck


## Next steps

Looking to expand on what you've done in this workshop? Here are some new adventures:

- [Install Python on your own machine and learn how to manage Python dependencies](https://docs.google.com/document/d/1cYmpfZEZ8r-09Q6Go917cKVcQk_d0P61gm0q8DAdIdg/edit?usp=sharing)
- Learn how to run your scripts from the command line
  - 💡 Check out [this tutorial)](https://first-web-scraper.readthedocs.io/en/latest/) to review the scraping concepts covered in this class *and* learn the basics of the command line
- Keep writing simple scrapers!
  - 💡 For inspiration, check out [City Scrapers](https://github.com/City-Bureau/city-scrapers),
  a collection of scrapers that gathering information on public meetings,
  written by 60+ contributors of all skill levels
- Learn more precise HTML parsing approaches, e.g., [`lxml`](https://lxml.de/) and [`xpath`](https://devhints.io/xpath)
- Graduate to more complicated scraping tasks, e.g., scrapes that rely on state
  - 💡 For inspiration, check out [`python-legistar-scraper`](https://github.com/opencivicdata/python-legistar-scraper/),
  a Python library for scraping legislative data from the Legistar web interface and API



## Credits

The content for this course was cribbed heavily from IRE's [one-hour course on web scraping with Python](https://github.com/ireapps/teaching-guide-python-scraping).

Some copy in the HTML basics section was lifted from the canonical (to me) [First web scraper tutorial](https://first-web-scraper.readthedocs.io/en/latest/), also developed for IRE. When you're ready to move from Jupyter notebooks into the command line, I'd strongly recommend starting with this workshop!


## Who am I?

👋 I'm Hannah! I apply my journalism background to civic technology projects as
a Lead Developer at DataMade. These include:

- Writing a web driver to fill out a branching, stateful web form in service of
lowering the barrier to completing a prerequisite to doing business with or
receiving funds from the City of Chicago
- Maintaining an inter-system scrape, transform, load (ETL) pipeline
for legislative data
- Managing millions of payroll and pension records to power the
[Illinois Public Salaries Database](https://salary.bettergov.org/) and the
[Illinois Public Pensions Database](https://pensions.bettergov.org/)



## HTML basics

### What *is* a web page, anyway?

Generally, a web page consists of specifically formatted text files. Here are a few common types:

- `.html` (HyperText Markup Language) files give structure to a page
- `.css` (Cascading Style Sheet) files determine how the page looks
- `.js` (JavaScript) files add interactivity

Today, we\'ll focus on the HTML, which gives structure to the page.

Most HTML elements are represented by a pair of tags \-- an opening tag and a closing tag.

A table, for example, starts with `<table>` and ends with `</table>`. The first tag tells the browser: \"Hey! I got a table here! Render it as a table.\" The closing tag (note the forward slash!) tells the browser: \"Hey! I\'m all done with that table, thanks.\" Inside the table are nested more HTML tags representing rows (`<tr>`) and cells (`<td>`).

``` html
<table id="example-table" class="striped-table" style="width: 95%">
    <tr> <!-- Header -->
        <td>Column A</td>
        <td>Column B</td>
        <td>Column C</td>
    </tr>
    <tr> <!-- Row 1 --->
        <td>Row 1, Column A</td>
        <td>Row 1, Column B</td>
        <td>Row 1, Column C</td>
    </tr>
    <tr> <!-- Row 2 --->
        <td>Row 2, Column A</td>
        <td>Row 2, Column B</td>
        <td>Row 2, Column C</td>
    </tr>
</table>
```

HTML elements can have any number of attributes, such as IDs, which uniquely identify elements \--

``` html
<table id="example-table">
```

\-- classes, which identify a type of element \--

``` html
<table class="striped-table">
```

\-- and styles, which define how specific elements appear \--

``` html
<table style="width:95%;">
```

\-- that will be useful to know about when we\'re scraping.

### Inspecting HTML in your browser

You can look at the HTML that makes up a web page by *inspecting the source* in a web browser. We like Chrome and Firefox for this; today, we\'ll use Chrome.

#### Inspect element

You can inspect specific elements on the page by right-clicking on the page and selecting \"Inspect\" or \"Inspect Element\" from the context menu that pops up. Hover over elements in the \"Elements\" tab to highlight them on the page. This can be helpful when you\'re trying to figure how to uniquely identify the element you want to scrape.

#### View page source

To examine all of the source code that makes up a page, you can \"view source.\" In Chrome, right click anywhere in your browser window, then click \"View Page Source.\"

This will open a new tab showing you all of the HTML code that makes up that page. Ignore 99% of it and try to locate the element(s) that you want to target (use `Ctrl+F` on a PC and `⌘+F` to find).

### Practice

Let\'s give our new skills a whirl. Open up a Chrome browser and navigate to [the first page of Maryland\'s list of WARN letters](https://www.dllr.state.md.us/employment/warn.shtml). Your goal is to isolate the table element on the page.

There are many ways to grab content from HTML, and every page you scrape data from will require a slightly different trick. At this stage, your job is to find a pattern or identifier in the code for the element you'd like to extract, which we will then give as instructions to our Python code.

Inspect the table element or view the page source. How would you pick the table element out from the all of the elements that make up the page? Is it the only table? If not, does it have any attributes, like a class or ID, that would allow you to target it?


## Web Scraping with Python

The remainder of this notebook demonstrates how you can use the Python programming language to scrape information from a web page. The goal today: Scrape the main table on [the first page of Maryland\'s list of WARN letters](https://www.dllr.state.md.us/employment/warn.shtml) and, if time, write the data to a CSV that you can open with Excel.

### Import libraries

As we learned in the first section, Python provides some broadly useful objects, like strings and lists, and functions, like `type()` and `print()`, by default. For more specialized operations, like making web requests and parsing HTML, we need to import a few modules, from which we can access helpful objects and functions.

Today, we\'ll use two third-party Python libraries to help us scrape:

- `requests` is the de facto standard for making HTTP requests, similar to what happens when you type a URL into a browser window and hit enter.
- `bs4`, or BeautifulSoup, is a popular library for parsing HTML into a data structure that Python can work with.

**Note:** These libraries are installed separately from Python on a per-project basis. They\'re already in your working environment for this tutorial. If you want to revisit this tutorial on your own computer, or if you want to create a scraping project of your own, you can ([read more about IRE\'s recommendations for setting up Python projects here](https://docs.google.com/document/d/1cYmpfZEZ8r-09Q6Go917cKVcQk_d0P61gm0q8DAdIdg/edit#heading=h.od2v1nkge5t1)).

Use the `import` keyword to import the `requests` and `bs4` modules.

``` python
import requests
import bs4
```

Remember, you can use the `dir()` function to inspect the objects and methods included with a module, and the `help()` function to read more about a particular object or method.

``` python
dir(requests)
```

### Request the page

Next, we\'ll use the `get()` method of the `requests` library (which we just imported) to grab the web page.

Use the `help()` function to learn more about `requests.get`.

**Note**: Some third-party libraries come with more documentation than others, however popular ones (such as `requests`) tend to be just as, if not more, helpful than the standard Python library!

``` python
help(requests.get)
```

First, we\'ll define a variable `URL` as a string containing the web address we want to scrape.

``` python
URL = 'http://www.dllr.state.md.us/employment/warn.shtml'
```

Next, we\'ll use `requests.get` to retrieve the URL. Remember that you can can assign the output of an expression to a variable, so we\'ll store the response as a new variable. The variable name is arbitrary, but it\'s a great idea to use something that describes the value it\'s pointing to.

``` python
warn_page = requests.get(URL)
```

If you want to make sure that your request was successful, you can check the `status_code` attribute of the Python object that was returned:

``` python
warn_page.status_code
```

A `200` code means all is well. `404` means the page wasn\'t found, etc. [Here\'s one of our favorite lists of HTTP status codes](https://http.cat/) ([or here, if you prefer dogs](https://httpstatusdogs.com/)).

The object being stored as the `warn_page` variable came back with a lot of potentially useful information we could access. Use the `dir()` method to see all the attributes.

``` python
dir(warn_page)
```

Today, we\'re mostly interested in the `.text` attribute \-- the HTML that makes up the web page, same as if we\'d viewed the page source. Let\'s take a look:

``` python
warn_page.text
```

### ✍️ Try it yourself

Use the code blocks below to experiment with requesting web pages and checking out the HTML that gets returned.

Some ideas to get you started:

- `'http://ire.org'`
- `'https://web.archive.org/web/20031202214318/http://www.tdcj.state.tx.us:80/stat/finalmeals.htm'`
- `'https://www.nrc.gov/reactors/operating/list-power-reactor-units.html'`

``` python
```

``` python
```

``` python
```

``` python
```

``` python
```

### Turn your HTML into soup

The HTML in the `.text` attribute of the request object is just a string \-- a big ol\' chunk of text.

Before we start targeting and extracting pieces of data in the HTML, we need to turn that chunk of text into a data structure that Python can work with. That\'s where the [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) (`bs4`) library comes in.

We\'ll create a new instance of a `BeautifulSoup` object, which lives under the top-level `bs4` library that we imported earlier. We need to give it two things:

- The HTML we\'d like to parse \-- `warn_page.text`
- A string with the name of the type of parser to use \-- `html.parser` is the default and usually fine, but [there are other options](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser)

We\'ll save the parsed HTML as a new variable, `soup`.

``` python
soup = bs4.BeautifulSoup(warn_page.text, 'html.parser')
```

Nothing happened, which is good! You can take a look at what `soup` is, but it looks pretty much like `warn_page.text`, except a bit easier to read:

``` python
soup
```

If you want to be sure, you can use the Python function `type()` to check what sort of object you\'re dealing with:

``` python
# the `str` type means a string, or text
type(warn_page.text)
```

``` python
# the `bs4.BeautifulSoup` type means we successfully created the object
type(soup)
```

### ✍️ Try it yourself

Use the code blocks below to experiment fetching HTML and turning it into soup (if you fetched some pages earlier and saved them as variables, that\'d be a good start).

``` python
```

``` python
```

``` python
```

``` python
```

``` python
```

### Target and extract the data

Now that we have BeautifulSoup object loaded up, we can go hunting for the specific HTML elements that contain the data we need. Our general strategy:

1.  Find the main table with the data we want to grab
2.  Get a list of rows (the `tr` element, which stands for \"table row\") in that table
3.  Use a Python `for loop` to go through each table row and find the data inside it (`td`, or \"table data\")

To accomplish this, we\'ll use two `bs4` methods:

- [`find()`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find), which returns the first element that matches whatever criteria you hand it
- [`find_all()`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all), which returns a *list* of elements that match the criteria. ([Here\'s how Python lists work](Python%20syntax%20cheat%20sheet.ipynb#Lists).)

#### Find the table

To start with, we need to find the table. There are several ways to accomplish this, but because this is the only table on the page (view source and `Ctrl+F` to search for `<table` to confirm), we can simply say, \"Look through the `soup` object and find the table tag.\"

Translated, the code is: `soup.find('table')`. While we\'re at it, save the results of that search to a new variable, `table`.

Run these cells:

``` python
table = soup.find('table')
```

``` python
table
```

#### Find the rows in the table

Next, use the `find_all()` method to drill down and get a list of rows in the table:

``` python
rows = table.find_all('tr')
```

``` python
rows
```

To see how many items are in this list \-- in other words, how many rows are in the table \-- you can use the `len()` function:

``` python
len(rows)
```

#### Loop through the rows and extract the data

Next, we can use a [`for` loop](Python%20syntax%20cheat%20sheet.ipynb#for-loops) to go through the list of rows and start grabbing data from each one.

Quick refresher on *for loop* syntax: Start with the word `for` (lowercase), then a variable name to stand in for each item in the list that you\'re looping over, then the word `in` (lowercase), then the name of the list holding the items (`rows`, in our case), then a colon, then an indented block of code describing what we\'re doing to each item in the list.

Each piece of data in the row will be stored in a `td` tag, which stands for \"table data.\" So inside the loop \-- in the indented block \-- we\'ll use the `find_all()` method to get a list of every `td` tag inside the row. And from there, we can access the content inside each tag.

Our goal is to end up with a *list* of data for each row that we will eventually write out to a file. Typically you\'d probably do the work of looping and inspecting the results, step by step, in one code cell. But to show the thinking of how you might approach this (and to practice the syntax), we\'ll start by just printing out each row and then build from there. (`print('='*80)` will print a line of 80 equals signs \-- a way to help us see exactly what we\'re working with in each row.)

``` python
for row in rows:
    print(row)
    print('='*80)  # prints a divider line for easier visibility
```

Notice that the first item that prints is the header row with the column labels. You are free to keep these headers if you want, but I typically skip that row and define my own list of column names.

(Another thing to consider: On better-constructed web pages, the cells in the header row will be represented by `th` (\"table header\") tags, not `td` (\"table data\") tags. The next step in our `for` loop is, \"Find all of the `td` tags in this row,\" so that would be something you would need to deal with.)

We can skip the first row by using *list slicing*: adding square brackets after the name of the list with some instructions about which items in the list we want to select.

Here, the syntax would be: `rows[1:]`, which means, take everything in the `rows` list starting with the item in position 1 (the second item) to the end of the list. Like many programming languages, Python starts counting at 0, so the result will leave off the first item in the list \-- i.e. the item in position 0, i.e. the headers.

``` python
for row in rows[1:]:
    print(row)
    print('='*80)
```

Now we\'re cooking with gas! Now that we\'ve isolated the rows we want, let\'s start pulling the data out of each row. Start by using `find_all()` to grab a list of `td` tags:

``` python
for row in rows[1:]:
    cells = row.find_all('td')
    print(cells)
    print('='*80)
```

Now we have, for each row, a *list* of `td` tags. Next step is to look at the table and start grabbing specific values based on their position in the list and assigning them to human-readable variable names.

Quick refresher on list syntax: To access a specific item in a list, use square brackets `[]` and the index number of the item you\'d like to access. For instance, to get the first cell in the row \-- the date that each WARN report was issued \-- use `[0]`.

``` python
for row in rows[1:]:
    cells = row.find_all('td')
    warn_date = cells[0]
    print(warn_date)
    print('='*80)
```

This is returning the entire `Tag` object \-- we just want the contents inside it. You can access the `.text` attribute of the tag to get the text inside:

``` python
for row in rows[1:]:
    cells = row.find_all('td')
    warn_date = cells[0].text    
    print(warn_date)
```

In the next cell (`[1]`), the `.text` attribute will give you the NAICS code. In the third cell (`[2]`) you\'ll get the name of the business. Etc.

It\'s also generally good practice to trim off external whitespace for each value, and you can use the Python built-in string method `strip()` to accomplish this as you march across the row.

Which gets us this far:

``` python
for row in rows[1:]:
    cells = row.find_all('td')
    warn_date = cells[0].text.strip()
    naics_code = cells[1].text.strip()
    biz = cells[2].text.strip()
    print(warn_date, naics_code, biz)
```

### ✍️ Try it yourself

Now that you\'ve gotten this far, see if you can isolate the other pieces of data in each row.

``` python
for row in rows[1:]:
    cells = row.find_all('td')
    warn_date = cells[0].text.strip()
    naics_code = cells[1].text.strip()
    biz = cells[2].text.strip()
    
    # address
    
    # wia_code
    
    # total_employees
    
    # effective_date
    
    # type_code

    # print()
```

### Write the results to file

Now that we\'ve targeted our lists of data for each row, we can use Python\'s built-in [`csv`](https://docs.python.org/3/library/csv.html) module to write each list to a CSV file.

First, import the csv module.

``` python
import csv
```

Now define a list of headers to match the data (each column header will be a string) \-- run this cell:

``` python
HEADERS = ['warn_date', 'naics_code', 'biz', 'address', 'wia_code',
           'total_employees', 'effective_date', 'type_code']
```

Now, using something called a `with` block, open a new CSV file to write to and write some code to do the following things:

- Create a `csv.writer` object
- Write out the list of headers using the `writerow()` method of the `csv.writer` object
- Drop in the `for` loop you just wrote and, instead of just printing the contents of each cell, create a list of items and use the `writerow()` method of the `csv.writer` object to write your list of data to file

``` python
# create a file called 'warn-data.csv' in write ('w') mode
# specify that newlines are terminated by an empty string (this deals with a PC-specific problem)
# and use the `as` keyword to name the open file handler (the variable name `outfile` is arbitrary)
with open('warn-data.csv', 'w', newline='') as outfile:
    # go to the csv module we imported and make a new .writer object attached to the open file
    # and save it to a variable
    writer = csv.writer(outfile)

    # write out the list of headers
    writer.writerow(headers)
    
    # paste in the for loop you wrote earlier here -- watch the indentation!
    # it should be at this indentation level =>
    # for row in rows[1:]:
    #     cells = row.find_all('td')
    #     etc. ...
    # but at the end, instead of `print(warn_date, naics_code, ...etc.)`
    # make it something like
    # data_out = [warn_date, naics_code, ...etc.]
    # `writer.writerow(data_out)`
```

If you look in the folder, you should see a new file: `warn-data.csv`. Hooray!

🎉 🎉 🎉

### ✍️ Try it yourself

Putting it all together:

- Find a website you\'d like to scrape
- Use `requests` to fetch the HTML
- Use `bs4` to parse the HTML and isolate the data you\'re interested in
- Use `csv` to write the data to file

### Extra credit problems

1.  **Remove internal whitespace:** Looking over the data, you probably noticed that some of the values have some unnecessary internal whitespace, which you could fix before you wrote each row to file. Python does not have a built-in string method to remove internal whitespace, unfortunately, but [Googling around](https://www.google.com/search?q=python+remove+internal+whitespace) will yield you a common strategy: Using the `split()` method to separate individual words in the string, then `join()`ing the resulting list on a single space. As an example:

``` python
my_text = 'hello     world      how are      you?'

# split() will turn this into a list of words
my_text_words = my_text.split()
# ['hello', 'world', 'how', 'are', 'you?']

# join on a single space
my_text_clean = ' '.join(my_text_words)
print(my_text_clean)
# prints 'hello world how are you?'

# or, as a one-liner
my_text_clean = ' '.join(my_text.split())
```

1.  **Fetch multiple years:** The table we scraped has WARN notices for the current year, but the agency also maintains pages with WARN notices for previous years \-- there\'s a list of them in a section [toward the bottom of the page](https://www.dllr.state.md.us/employment/warn.shtml). See if you can figure out how to loop over multiple pages and scrape the contents of each into a single CSV.

2.  **Build a lookup table:** Each numeric code in the \"WIA Code\" column correspondes to a local area. See if you can figure out how to create a lookup dictionary that maps the numbers to their locations, then as you\'re looping over the data table, replace the numeric value in that column with the name of the local area instead. Here\'s a hint:

``` python
    lookup_dict = {
        '1': 'hello',
        '2': 'world'
    }

    print(lookup_dict.get('1'))
    # prints 'hello'

    print(lookup_dict.get('3'))
    # prints None
```

1.  **Fix encoding errors:** You might have noticed a few encoding problems \-- e.g., `Nestlé` is being renedered as `NestlÃ©`. This is due to an encoding problem \-- the `warn_page.text` is not encoded as `utf-8`. Using `decode()` and `encode()`, see if you can fix this. (Hint! It looks like the state of Maryland is a big fan of `latin-1`.)

``` python
```
