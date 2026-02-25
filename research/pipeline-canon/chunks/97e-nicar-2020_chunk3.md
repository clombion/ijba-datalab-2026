<!-- chunk: 3/4 | source: 97e-nicar-2020.md | words: 37166 -->
<!-- headings: How to sort rows[¶](#how-to-sort-rows "Permalink to this headline"); How to filter rows[¶](#how-to-filter-rows "Permalink to this headline"); Filtering selected rows with \"[¶](#filtering-selected-rows-with "Permalink to this headline"); Filtering via frequency tables[¶](#filtering-via-frequency-tables "Permalink to this headline"); Using frequency tables to select (and filter) for multiple values[¶](#using-frequency-tables-to-select-and-filter-for-multiple-values "Permalink to this headline"); Frequency tables[¶](#frequency-tables "Permalink to this headline"); Multi-column frequencies[¶](#multi-column-frequencies "Permalink to this headline"); Adding "aggregators"[¶](#adding-aggregators "Permalink to this headline"); One-off calculations[¶](#one-off-calculations "Permalink to this headline"); Summarizing all columns[¶](#summarizing-all-columns "Permalink to this headline"); Basic column attributes[¶](#basic-column-attributes "Permalink to this headline"); How to view all columns and their attributes[¶](#how-to-view-all-columns-and-their-attributes "Permalink to this headline"); How to set column types[¶](#how-to-set-column-types "Permalink to this headline"); How to rename columns[¶](#how-to-rename-columns "Permalink to this headline"); How to expand, shrink, and remove columns[¶](#how-to-expand-shrink-and-remove-columns "Permalink to this headline"); How to move columns' positions[¶](#how-to-move-columns-positions "Permalink to this headline"); How to designate "key" columns[¶](#how-to-designate-key-columns "Permalink to this headline"); Manipulating columns from the Columns Sheet[¶](#manipulating-columns-from-the-columns-sheet "Permalink to this headline"); Selecting and Unselecting Rows[¶](#selecting-and-unselecting-rows "Permalink to this headline"); One row at a time[¶](#one-row-at-a-time "Permalink to this headline") -->

## How to sort rows[¶](#how-to-sort-rows "Permalink to this headline")

The keys \[ and [\]] sort rows in ascending and descending order, respectively.

For instance, you could do the following with the FAA dataset:

- Navigate to the `COST_REPAIRS` column
- Press \# (if you haven't already) to tell VisiData it's a numeric column
- Press [\]] to sort the column in descending order --- i.e., from highest to lowest

After that, you should see something like the following:

::: ansi2html

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

Tip

You can sort on multiple columns at once by "key"-ing those columns (via !) and then typing either g\[ (ascending) or [g\]] (descending).


## How to filter rows[¶](#how-to-filter-rows "Permalink to this headline")

VisiData provides several ways to filter your datasets:

- Row selection + \"
- Frequency tables + Enter
- Frequency tables + row selection + g + Enter

The sections below walk you through each approach.

### Filtering selected rows with \"[¶](#filtering-selected-rows-with "Permalink to this headline")

In VisiData, pressing \" will create a copy of your current sheet --- but one that contains only **selected** rows.

So, to view only wildlife strikes that involved hawks, you could do the following:

- Navigate to the `SPECIES` column
- Press \| to select by searching, then type `hawk`, and then press Enter

At this point, you should see something like the following:

::: ansi2html

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

Then, press \", which should give you something like the following:

::: ansi2html

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

### Filtering via frequency tables[¶](#filtering-via-frequency-tables "Permalink to this headline")

From any row in any frequency table, you can press Enter to create a new dataset containing only the rows that match that value.

For instance, to view only the wildlife strikes that occurred in California, we might do the following from the main data sheet:

- Navigate to the `STATE` column
- Press Shift-F to create the frequency table
- Navigate down two rows, to the row for `CA`

At which point, you should see something like this:

::: ansi2html

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

From there, pressing Enter should create the filtered sheet we wanted:

::: ansi2html

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

### Using frequency tables to select (and filter) for multiple values[¶](#using-frequency-tables-to-select-and-filter-for-multiple-values "Permalink to this headline")

The approach above is great if you want to drill down on rows where a field equals one particular value. But what if you want to include a few different values? Select the rows of the frequency table you want to include, then press g + Enter.

Here's a practical example, using the FAA dataset. Let's say you want to filter for wildlife strikes at the five airports with the most reported incidents. To achieve that, you could take these steps:

- On the main data sheet navigate to the `AIRPORT` column, and press Shift-F to create a frequency table:

::: ansi2html

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

- Then, select the top five entries (skipping `UNKNOWN`) using s:

::: ansi2html

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

- Next, press g + Enter. The result should look like this, with 9,250 rows (the total of those five airports):

::: ansi2html

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



## Frequency tables[¶](#frequency-tables "Permalink to this headline")

Frequency tables are dead-simple, but also quite powerful. For the dead-simple usage: Navigate to any column, and then press Shift-F. If you did that on the first column ("OPERATOR") of the FAA dataset, you should get something like this:

::: ansi2html

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

With just one keystroke, VisiData has already told us something useful about the dataset: That the "operators" associated with 31% of the wildlife strikes are, according to the FAA, "unknown." We have also learned, from the "bins" mini-report at the bottom-right of the screen, that there are 282 distinct values in the "OPERATOR" column.

### Multi-column frequencies[¶](#multi-column-frequencies "Permalink to this headline")

Sometimes you want to count how often **combinations** of columns occur. VisiData also makes this easy. First, turn the columns you want to count into "key" columns, using the ! button. Then, type gF.

For instance, if we wanted to count the combinations of the "OPERATOR" and "PERSON" fields, we'd hit ! on each of those columns --- either from the main data sheet or in the Columns Sheet. Once you've done that, you should see something like this:

::: ansi2html

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

Then, type gF, which should result in something like this:

::: ansi2html

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

To make it easier to read, type g\_, which will expand the column widths:

::: ansi2html

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

With just a few more keystrokes, we've learned something else: Virtually all wildlife strikes with "unknown" operators were identified based on carcasses found at the airport (rather than reports from pilots, for example).


## Adding "aggregators"[¶](#adding-aggregators "Permalink to this headline")

By default, frequency tables just count the number of times each value appears. But in VisiData, you can specify additional calculations by setting the column's "aggregators". (You might remember this field from the Columns Sheet.) In VisiData's aggregators include `min`, `max`, `mean`, `median`, `sum`, `distinct`, and others.

To add an aggregator to a column, navigate to that column and press +. VisiData will then prompt you to specify *which* aggregator you would like to add. You can type out your desired aggregator, or use Control-x to open the interactive chooser and select from a list of options.

For example, let's go back to the original FAA data sheet. Let's navigate to the "COST_REPAIRS" column, and then do the following:

- Press \# to tell VisiData this is an integer column
- Press + to tell VisiData you want to add an aggregator
- At the prompt, type `sum` and then hit Enter to add the summation aggregator
- Navigate to the "AIRPORT" column, and press Shift-F

You should see something like this, with the `sum` calculation now appearing in your frequency table:

::: ansi2html

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

By default, frequency tables are sorted by the "count" column, but you can sort them by any other column.

Note

When using aggregators, make sure that you've assigned the proper type (`#` for integer columns, etc.) to the columns of interest, so that VisiData knows how to calculate the aggregations correctly.



## One-off calculations[¶](#one-off-calculations "Permalink to this headline")

From any data sheet, you can also run a single calculation on all rows --- or all selected rows --- in a column. To do that, navigate to the column and type z+, which will bring up the same aggregator-choice prompt as above. Type the aggregator you want, and press Enter. At the bottom of the screen, you'll see the result of the calculation.

You can try this on the FAA data sheet we've been working with. Navigate to the "COST_REPAIRS" column, and then do the following:

- Press \# to tell VisiData this is an integer column (if you haven't already)
- Type z+ to see the result of an aggregator
- Type `sum` and then hit Enter

At the bottom of the screen, you should see something like this, indicating that the total *reported* cost of repairs is \$161,868,071:

::: ansi2html

     DELTA AIR LINES    │ Tower  ║ 1            │ NONE               │ N      │             !│ 0       
     LUFTHANSA          │ Tower  ║ 1            │ NONE     ┌─────────────────────────────| statuses |─┐
     BUSINESS           │ Tower  ║ 1            │ NONE     │ COST_REPAIRS_sum=161868071               │
     SPIRIT AIRLINES    │ Tower  ║ 1            │ PRECAUTIO└──────────────────────────────────────────┘
    1› faa-wildlife-strikes|                                       z+   memo-aggregate      73448 rows 


## Summarizing all columns[¶](#summarizing-all-columns "Permalink to this headline")

To get a bird's-eye view of your entire dataset, press Shift-I, which will provide summary statistics for each of your columns:

::: ansi2html

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

In VisiData, this is called the "Describe Sheet". You'll notice that there are only min/max/median/etc. calculations for the columns we've given types --- just the `COST_REPAIRS` column so far. If we go back to the data sheet and tell VisiData that the `HEIGHT`, `SPEED`, and `BIRDS_STRUCK` fields are numbers, too, then pressing Shift-I will result in something like this:

::: ansi2html

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



## Basic column attributes[¶](#basic-column-attributes "Permalink to this headline")

Every column in VisiData has the following basic properties, all of which can be modified:

- **Name**: Self explanatory.
- **Width**: The number of characters the column occupies on the screen.
- **Type**: The kind of data --- text, integer, float, currency, or date --- that the column will be interpreted as.

We'll get to a few other properties later.


## How to view all columns and their attributes[¶](#how-to-view-all-columns-and-their-attributes "Permalink to this headline")

To see all the columns in your dataset, press Shift-C. This will open the "Columns Sheet," which lists each column and its attributes. For the FAA dataset we've been using, it should look like this:

::: ansi2html

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

The Columns Sheet is handy for quickly getting a sense of your dataset's structure. You can navigate the sheet as if it were just another dataset. And just like you can do with a standard data sheet, you can leave this column sheet by pressing q.

Note

The Columns Sheet is one of several "metasheets" in VisiData; the Sheets Sheet from the previous chapter is another example. You'll encounter a few other metasheets in this tutorial.



## How to set column types[¶](#how-to-set-column-types "Permalink to this headline")

Rather than guess at your column's data types, VisiData assumes that they're all plain-old text.

If a column of really is just text, then great.

But if that column is a number or date, and you want to do any math-y operations on your column (e.g., sorting, summing, averaging, et cetera), you'll have to specify its type.

To set a column's type, navigate over to that column and press one of the following keys:

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Keystroke                                         Column type   Examples
  ------------------------------------------------- ------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \#   Integer       `0`, `-1`, `5000000`

  %    Float         `0.5`, `-3.14`, `23.45557`

  \$   Currency      `$4.99`, `€20`, `₹`` ``100`` ``100`

  @    Date          `2018-04-06`, `April`` ``6,`` ``2018`, `04/06/2018`

  \~   Text          *anything!*
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When you do so, the corresponding symbol (e.g., `$` for currency) will appear in the column's heading.

For instance, here's what you should see if you navigate to the wildlife-strike database's `HEIGHT` column, and then press \# to tell VisiData that the height values are integers:

::: ansi2html

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

Note

As you can see above, if a cell cannot be converted into the type you've assigned it, VisiData will display `!` in the right-side margin of that cell.

To entirely remove a column's assigned type, navigate to the column and type z\~.


## How to rename columns[¶](#how-to-rename-columns "Permalink to this headline")

- Navigate to the column that you want to rename:

::: ansi2html

      File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
     OPERATOR           │ ATYPE        │ INCIDENT_DATE     │ STATE │ AIRPORT            │ PHASE_OF_FLT>
     BUSINESS           │ PA-28        │ 05/22/15 00:00:00 │ FL    │ VERO BEACH MUNICIP…│ APPROACH     │
     BUSINESS           │ BE-1900      │ 06/18/15 00:00:00 │ AK    │ KENAI MUNICIPAL AR…│ APPROACH     │

- Press \^, which enters column-name-editing mode (evident by the underscores and change in background highlighting):

::: ansi2html

      File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
     OPERATOR           │ATYPE________   INCIDENT_DATE     │ STATE │ AIRPORT            │ PHASE_OF_FLT>
     BUSINESS           │ PA-28        │ 05/22/15 00:00:00 │ FL    │ VERO BEACH MUNICIP…│ APPROACH     │
     BUSINESS           │ BE-1900      │ 06/18/15 00:00:00 │ AK    │ KENAI MUNICIPAL AR…│ APPROACH     │

- Then, type what you want the column to be renamed:

::: ansi2html

      File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
     OPERATOR           │Aircraft_____   INCIDENT_DATE     │ STATE │ AIRPORT            │ PHASE_OF_FLT>
     BUSINESS           │ PA-28        │ 05/22/15 00:00:00 │ FL    │ VERO BEACH MUNICIP…│ APPROACH     │
     BUSINESS           │ BE-1900      │ 06/18/15 00:00:00 │ AK    │ KENAI MUNICIPAL AR…│ APPROACH     │

- And then press Enter to complete the process:

::: ansi2html

      File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
     OPERATOR           │ Aircraft     │ INCIDENT_DATE     │ STATE │ AIRPORT            │ PHASE_OF_FLT>
     BUSINESS           │ PA-28        │ 05/22/15 00:00:00 │ FL    │ VERO BEACH MUNICIP…│ APPROACH     │
     BUSINESS           │ BE-1900      │ 06/18/15 00:00:00 │ AK    │ KENAI MUNICIPAL AR…│ APPROACH     │



## How to expand, shrink, and remove columns[¶](#how-to-expand-shrink-and-remove-columns "Permalink to this headline")

When you load a dataset, VisiData will try to choose reasonable widths for your columns. You can adjust them in a few ways:

  --------------------------------------------------------------------------------------------------------------------------------------------------------
  Keystroke(s)                                             Action
  -------------------------------------------------------- -----------------------------------------------------------------------------------------------
  \_          Expands the width of **current column** to fit text in all visible rows

  g\_         Expands the width of **all columns** to fit text in all visible rows

  z\_ + *n*   Sets the current column's width to *n* characters

  -           Hides the current column by setting its width to `0`

  gv          Unhides all columns

  z-          Shrinks the current column's width in half
  --------------------------------------------------------------------------------------------------------------------------------------------------------

Note

**What's the deal with "z"?**

Much like with `g`, you'll notice that many VisiData commands can be prefixed with `z`. The effect is typically to narrow or specify the scope of the action; e.g., - hides a column entirely, while z- only shrinks it to half-width.


## How to move columns' positions[¶](#how-to-move-columns-positions "Permalink to this headline")

Sometimes you want to view a dataset's columns in a different order than they appear in the dataset. To do that in VisiData, use the following keystrokes:

  -------------------------------------------------------------------------------------------------------
  Keystroke(s)                                           Action
  ------------------------------------------------------ ------------------------------------------------
  Shift-H   Moves column one position to the left

  Shift-L   Moves column one position to the right
  -------------------------------------------------------------------------------------------------------

Tip

Similarly, you can use Shift-J to move a row down one position, and Shift-K to move a row up one position.



## How to designate "key" columns[¶](#how-to-designate-key-columns "Permalink to this headline")

For any sheet, you can designate any number of columns as "key" columns. They serve two functions:

- They stay **pinned to the left-hand side** of the sheet when you scroll horizontally.
- They get **special treatment** for certain commands, such as when joining sheets. (More on this later.)

To turn a column into a key column (or vice-versa), navigate to that column and press !.

For example, say we've navigated to the `AIRPORT` column of the FAA dataset. Pressing ! will turn this:

::: ansi2html

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

... into this:

::: ansi2html

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


## Manipulating columns from the Columns Sheet[¶](#manipulating-columns-from-the-columns-sheet "Permalink to this headline")

You can do nearly all of the above from the Columns Sheet (Shift-C). When you're dealing with datasets with a particularly large number of columns, doing it this way can often be easier; you can see more of the columns at once, and you can adjust multiple columns at once.

- **Moving columns**: In the Columns Sheet, each column is represented as a row; you can reposition them using Shift-J and Shift-K.
- **Editing column names**: In the Columns Sheet, you can edit each column's name like you would any other row cell. Just navigate to the name, and press e to start editing.
- **Setting column types**: You can select multiple rows of the Columns Sheet and type g\$, for example, to set all of the selected columns' types to `currency`.
- **Setting column widths**: You can edit the `width` field of the Columns Sheet to adjust any column's width. You can also give multiple columns to the same width by selecting each of their rows, and typing ge + *number*, where *number* is the desired width.

For instance, here's the Columns Sheet for the FAA dataset before we've made any changes:

::: ansi2html

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

Next, we use the s key to select the four columns we'd like to change:

::: ansi2html

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

We'd like to make them all numeric columns, so we type g#, which results in this:

::: ansi2html

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

And we'd like to make them uniformly narrow, so we navigate to the width column and type ge8 + Enter, which gives us this:

::: ansi2html

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

To see how these changes have affected your data sheet, press q to exit the Columns Sheet, and then navigate over to the `HEIGHT` column:

::: ansi2html

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



## Selecting and Unselecting Rows[¶](#selecting-and-unselecting-rows "Permalink to this headline")

Many VisiData commands --- such as filtering --- distinguish between selected and unselected rows. You can select and unselect rows in a few ways:

### One row at a time[¶](#one-row-at-a-time "Permalink to this headline")

  -----------------------------------------------------------------------------------------------------
  Keystroke(s)                                     Action
  ------------------------------------------------ ----------------------------------------------------
  s   Select the current row

  u   Unselect the current row

  t   Toggle the current row between selected/unselected
  -----------------------------------------------------------------------------------------------------

For instance, pressing s while on the second row of the FAA dataset should have the following effect:

::: ansi2html

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

VisiData has highlighted that row and indicated the number of selected rows (the `•1` in the bottom-right corner).

### All rows at the same time[¶](#all-rows-at-the-same-time "Permalink to this headline")

  ---------------------------------------------------------------------------------------------------
  Keystroke(s)                                      Action
  ------------------------------------------------- -------------------------------------------------
  gs   Select all rows

  gu   Unselect all rows

  gt   Toggle all rows between selected/unselected
  ---------------------------------------------------------------------------------------------------

### By matching patterns[¶](#by-matching-patterns "Permalink to this headline")

  ---------------------------------------------------------------------------------------------------------------------------------------------------
  Keystroke(s)                                                Action
  ----------------------------------------------------------- ---------------------------------------------------------------------------------------
  \| + *term*    Select all rows where *term* matches the **current column**

  \\ + *term*    Unselect all rows where *term* matches the **current column**

  g\| + *term*   Select all rows where *term* matches **any** column

  g\\ + *term*   Unselect all rows where *term* matches **any** column

  ,              Select all rows where the **current column** matches this row's value for that column

  g,             Select all rows matching **the current row** (for all non-hidden columns)
  ---------------------------------------------------------------------------------------------------------------------------------------------------

For instance, if you take the following steps:

- Navigate to the `STATE` column
- Press \|
- Type `TX`
- Press Enter

... you should see this:

::: ansi2html

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

### Via expressions[¶](#via-expressions "Permalink to this headline")

In VisiData, you can select rows by evaluating a given Python **expression** for every row in your dataset.

Tip

If you're unfamiliar with Python, no worries. You can find an overview of simple and handy expressions [here](https://docs.python.org/3/tutorial/introduction.html).

These expressions can reference any column in your dataset (so long as the column name contains only letters, underscores, and numbers, and doesn't start with a number; in the next chapter, you'll learn how to rename columns). The two keystrokes for this are z\| and z\\:

  ---------------------------------------------------------------------------------------------------------------------------------------------------------
  Keystroke(s)                                                Action
  ----------------------------------------------------------- ---------------------------------------------------------------------------------------------
  z\| + *expr*   Select all rows where *expr* evaluates to `True`

  z\\ + *expr*   Unselect all rows where *expr* evaluates to `True`
  ---------------------------------------------------------------------------------------------------------------------------------------------------------

For instance, if you take the following steps:

- Type gu to unselect all rows
- Type z\|
- Type `OPERATOR`` ``==`` ``"BUSINESS"`` ``and`` ``STATE`` ``==`` ``"FL"`
- Press Enter

... you should see this:

::: ansi2html

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

Tip

Likewise, you can *search* via expressions using z/ (search forward) and z? (search backward).


## Moving Rows[¶](#moving-rows "Permalink to this headline")

You can move the position of row up or down using the following commands:

  ----------------------------------------------------------------------------------------------
  Keystroke(s)                                           Action
  ------------------------------------------------------ ---------------------------------------
  Shift-K   Move row up one spot

  Shift-J   Move row down one spot
  ----------------------------------------------------------------------------------------------



## Editing Row Cells[¶](#editing-row-cells "Permalink to this headline")

Even if you don't want to edit your raw data in VisiData, knowing how to edit cells will still come in handy, since virtually *everything* --- including settings --- in VisiData is represented as columns and rows.

Here are the most basic commands:

  ---------------------------------------------------------------------------------------------------------------
  Keystroke(s)                                             Action
  -------------------------------------------------------- ------------------------------------------------------
  e           Begin editing current cell

  Enter       Finish editing

  Control-c   Cancel editing

  Control-a   Move to beginning of line

  Control-e   Move to end of line

  Control-k   Clear contents from cursor's position to end of line
  ---------------------------------------------------------------------------------------------------------------

Other keys --- such as `Delete`, standard characters, and the arrow keys --- work as expected. You can find a handful of additional special commands in [VisiData's quick reference](http://visidata.org/man/).


## How to use the Sheets Sheet[¶](#how-to-use-the-sheets-sheet "Permalink to this headline")

VisiData's "Sheets Sheet" lists all currently-open sheets and makes it easy to jump between sheets.

From anywhere in VisiData, you can open the Sheets Sheet by pressing Shift-S.

If you've just launched VisiData with a single dataset, pressing Shift-S will open a Sheets Sheet that looks something like this:

::: ansi2html

      File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
     name               ║ type        │ pane#│ shortcut │ nRows#│ nCols#│ nVisibleCols#│ cursorDisplay>
     sheets             ║ SheetsSheet │    1 │ Shift+S  │     2 │    11 │           11 │ sheets        │
     faa-wildlife-strik…║ CsvSheet    │    1 │ 1        │ 73448 │    16 │           16 │ BUSINESS      │


    Shift+S› sheets|                                                      Shift+S             2 sheets 

Not very exciting. But as you start juggling more sheets --- frequency tables, multiple datasets, et cetera --- the Sheets Sheet becomes very handy.

You can navigate the Sheets Sheet much like you would any other sheet, with one main difference: Pressing Enter will open that row's sheet.

Warning

Pressing d on a Sheets Sheet will send that row's sheet to the "sheets graveyard." (You can type gS to visit the graveyard, and revive sheets there via Enter.)



## How to rename a sheet[¶](#how-to-rename-a-sheet "Permalink to this headline")

There are two ways to rename a sheet:

- Go to the **Sheets Sheet**, and navigate to the row representing the sheet you want to rename. Press e to go into editing mode, type the new name, and then press Enter to complete the renaming.
- Alternatively, while **in the sheet you want to rename**, press Space to raise the type-a-command prompt. Then, type `rename-sheet` and press Enter. At the next prompt, type the new name, and press Enter to complete the renaming.


## How to close/remove a sheet[¶](#how-to-close-remove-a-sheet "Permalink to this headline")

To close the current sheet (removing it from VisiData), press q.

To close all sheets (and, hence, quitting VisiData in its entirety), type gq.

To access the "sheets graveyard", a listing of recently-closed sheets, type gS.



## How to *prevent* sheet closure/removal[¶](#how-to-prevent-sheet-closure-removal "Permalink to this headline")

You can prevent VisiData from quitting a sheet by "guarding" it. To do so, press Space to raise the type-a-command prompt. Then, type `guard-sheet` and press Enter.


## Quickly toggling between sheets[¶](#quickly-toggling-between-sheets "Permalink to this headline")

To flip back and forth between your current sheet and the previous one, press Control-\^.

Additionally, VisiData assigns every sheet a numeric shortcut, visible at the bottom-left corner of the interface. You can jump to a sheet by pressing Alt plus the shortcut number --- for instance Alt-1 to go to the first sheet you loaded.



## How to fix funky spreadsheets' column names[¶](#how-to-fix-funky-spreadsheets-column-names "Permalink to this headline")

By default, VisiData considers the first row of a tabular dataset to be its columns' names. That's a safe assumption for many formats, but Excel spreadsheets often buck that trend, with titles, notes, or other cruft coming before the actual column names.

As previously noted, you can manually edit a column's name manually by pressing \^, or by editing it from the Columns Sheet. But you can also auto-populate column names by doing the following:

- Navigate to the row that contains your desired column names.
- Type g\^ to name all *unnamed* columns with the values in this row, or gz\^ to name *all* columns (regardless of whether they're already named) with the values in this row.

If you'd like to have VisiData *not* to load the first row as the header, you can do one of the following:

- Pass the `--header`` ``0` option when you launch `vd` from the command line.

- From within VisiData, do this:

  > ::: {}
  > - Press O to open the Options Sheet
  > - Set the `header` option cell to `0`
  > - Press q to return to your spreadsheet
  > - Press Control-r to reload it
  > :::


## About This Tutorial[¶](#about-this-tutorial "Permalink to this headline")

Note

This tutorial is not officially affiliated with VisiData, and is not intended as a comprehensive reference. You can learn more about VisiData from these official sources:

- [VisiData.org](https://visidata.org/)
- [VisiData's GitHub repository](https://github.com/saulpw/visidata)
- [Saul Pwanson's Patreon page](https://www.patreon.com/saulpw)
- [Saul Pwanson's case studies on YouTube](https://www.youtube.com/playlist?list=PLxu7QdBkC7drrAGfYzatPGVHIpv4Et46W)

### Tutorial Structure[¶](#tutorial-structure "Permalink to this headline")

This tutorial is divided into five sections:

  ----------------------------------------------------------------------------------
  Section              Description                           Status
  -------------------- ------------------------------------- -----------------------
  The Big Picture      If you read nothing else ...          Draft complete

  Basic Usage          All you need to know to get started   Draft complete

  Intermediate Usage   Some of the handiest power-features   Draft complete

  Advanced Usage       How to bend VisiData to your whims    Four chapters drafted

  Practical Examples   Step-by-step walkthroughs             Two examples drafted
  ----------------------------------------------------------------------------------

To be notified of new material and/or major updates, [sign up here](https://buttondown.email/intro-to-visidata).

### Tutorial Status[¶](#tutorial-status "Permalink to this headline")

  ----------------------------------------- -------------------------------------------------------
  Tutorial last updated                     `2024-03-08`

  VisiData version                          `3.0.2`
  ----------------------------------------- -------------------------------------------------------



## About the author[¶](#about-the-author "Permalink to this headline")

[Jeremy Singer-Vine](https://www.jsvine.com/) is a journalist, computer programmer, and data editor based in New York City.


## Feedback / questions / corrections?[¶](#feedback-questions-corrections "Permalink to this headline")

[File an issue on GitHub](https://github.com/jsvine/intro-to-visidata/issues) or email the author at [jsvine@gmail.com](mailto:jsvine%40gmail.com).



## Acknowledgments[¶](#acknowledgments "Permalink to this headline")

Many thanks to the following people for their feedback, suggestions, and fixes: [Saul Pwanson](http://saul.pw/), [Anja Kefala](https://github.com/anjakefala), [John Templon](https://twitter.com/jtemplon), [Scott Pham](https://twitter.com/scottpham), [Andrea Borruso](https://github.com/aborruso), [Felix Rosencrantz](https://github.com/frosencrantz), [Ram Rachum](https://github.com/cool-RR), [Ezequiel Garzon](https://github.com/ezequiel-garzon), [Joseph Reagle](https://github.com/reagle), [David Wales](https://github.com/daviewales), [\@rschwiebert](https://github.com/rschwiebert), [Martin Häcker](https://github.com/dwt).



## How to create an incremented column[¶](#how-to-create-an-incremented-column "Permalink to this headline")

You can add an incremented column with **sequential values** (akin to row numbers) by pressing i. Once you do that, VisiData will create this new column directly to the right of your current column:

::: ansi2html

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

By default, VisiData will name the column `A` (or `B` if VisiData has already created an `A` column this session, and so on).

Note

You can customize the "step" between values; to do that, type zi, and specify a number at the prompt. (Specifying `3`, for instance, would create the sequence `1,`` ``4,`` ``7,`` ``...`.)



## How to create an expression column[¶](#how-to-create-an-expression-column "Permalink to this headline")

Expression columns **evaluate** a given Python expression for every row in your dataset.

These expressions can reference any column in your dataset (so long as the column name contains only letters, underscores, and numbers, and doesn't start with a number).

Note

If you're unfamiliar with Python, no worries. You can find an overview of simple and handy expressions [here](https://docs.python.org/3/tutorial/introduction.html).

You can create an expression column by pressing =. Once you do so, you'll see a prompt at the bottom of the screen. Then, type your desired expression and press Enter.

Perhaps the simplest expression column would be `=1`; for every row, the column's value would be `1`. Let's see how that looks:

::: ansi2html

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

Note

By default, the name of your new columns will be the expression you entered. As always, you can edit the column name by pressing \^ and typing the new name.

Also by default, the column will appear directly to the right of the column that was active when you pressed =. As always, you can move the column left or right using Shift-H and Shift-L.

Now, let's try creating a column *based on another column*. Let's say we want to identify wildlife strikes that were reported to have occurred at least 100 feet above ground. We could do the following:

- Navigate to the `HEIGHT` column
- Press \# to tell VisiData the column's values should be interpreted as integers
- Press = to bring up the "new column expr=" prompt
- In the prompt, type `HEIGHT`` ``>=`` ``100`
- Press Enter

You should see something like the following:

::: ansi2html

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


## How to create new columns by splitting another one[¶](#how-to-create-new-columns-by-splitting-another-one "Permalink to this headline")

You can split the text in any column in VisiData into two or more columns, based on a pattern (i.e., a "regular expression" a.k.a. "regex") that you provide.

To split a column, navigate to that column, and press :. At the bottom of the screen, VisiData you'll see a `split`` ``regex:` prompt. Enter your desired splitting pattern, and press Enter.

For a simple example, let's say we want to split the `INCIDENT_DATE` column into the date and time. Because the date and time are separated by a space, we can do this:

- Navigate to the `INCIDENT_DATE` column
- Press :
- At the prompt, press Space (since we want to split on the column's whitespace), and then hit Enter

Once you do that, you should see something like this:

::: ansi2html

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

Each value in the new column is a list of the pieces that resulted from the split. But you probably want them each piece in its own column. To do that press (, which is the "expand column" command. Now you should see something like this:

::: ansi2html

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



## How to create a new column by "capturing" it from another column[¶](#how-to-create-a-new-column-by-capturing-it-from-another-column "Permalink to this headline")

Note

This approach requires a bit more knowlege of "regular expressions". If you're unfamiliar with regular expressions and don't want to learn them right now, feel free to skip to the next chapter.

Just like you can split a column by using :, you can extract part of a column into a new column by using ;.

For instance, if you want to extract the first string of numbers from each aircraft type, (e.g., `28` from `PA-28`, `46` from `PA-46`` ``MALIBU`, and `717` from `B-717-200`). To do that, take the following steps:

- Navigate to the `ATYPE` column
- Press ;
- At the prompt, type `(\d+)` (with one set of parentheses for each capture group), and then hit Enter
- Press ( to expand the new column's lists

Once you do that, you should see something like this:

::: ansi2html

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


## The sheet-joining three-step[¶](#the-sheet-joining-three-step "Permalink to this headline")

To join two or more sheets in VisiData, you'll do the following:

1.  In the sheets you want to join, **mark the shared columns as "keys"**
2.  In the Sheets Sheet, **select the sheets you want to join**
3.  Press & to open the join-choice prompt, **type your desired join type** (or press Control-x to open the interactive chooser) and press Enter

VisiData supports seven types of joins:

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Join command   SQL equivalent                                                                                                                                                                                                           Description
  -------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  inner          `LEFT`` ``INNER`` ``JOIN`   Keeps only rows which match keys on all sheets

  outer          `LEFT`` ``OUTER`` ``JOIN`   Keeps all rows from first selected sheet

  full           `FULL`` ``OUTER`` ``JOIN`   Keeps all rows from all sheets (union)

  diff                                                                                                                                                                                                                                    Keeps only rows NOT in all sheets

  append         `UNION`` ``ALL`                                                                                       Keeps all rows from all sheets (concatenation)

  extend                                                                                                                                                                                                                                  Copies first selected sheet, keeping all rows and sheet type, and extends with columns from other sheets

  merge                                                                                                                                                                                                                                   Merges differences from other sheets into first sheet; keeps all rows from first sheet, updating any False-y values (e.g., `False`, `None`, `0`, [`[]`]) with non-False-y values from subsequent sheets, and adds unique rows from subsequent sheets
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

(Descriptions above come from VisiData's [Quick Reference](http://visidata.org/man/).)



## Practical example[¶](#practical-example "Permalink to this headline")

To see an example of joining in action, see the [Distinctive Birds](../../practical/distinctive-birds/) chapter.


## Enabling multiline mode[¶](#enabling-multiline-mode "Permalink to this headline")

By default, VisiData displays each row on a single line. You can switch to multiline mode (and toggle back out of it) by pressing v. Here's what that looks like:

::: ansi2html

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

Note

The default row height in multiline mode is 4 lines, but you can adjust this through VisiData's `default_height` setting.



## Scrolling within cells[¶](#scrolling-within-cells "Permalink to this headline")

To see more of a cell in single-line mode, you can scroll back and forth within a column using the following commands:

  ----------------------------------------------------------------------------------------------------
  Keystrokes                                         Action
  -------------------------------------------------- -------------------------------------------------
  zh    Scroll text left

  zl    Scroll text right

  zj    Scroll text down

  zk    Scroll text up

  gzh   Scroll back to leftmost character

  gzk   Scroll back to topmost character
  ----------------------------------------------------------------------------------------------------

Here's how it looks in practice, starting with the same view as above:

::: ansi2html

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

After typing zh, the `REMARKS` column now looks like this:

::: ansi2html

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


## Diving into cells[¶](#diving-into-cells "Permalink to this headline")

Pressing z + Enter "dives" into your current cell, opening a "Text Sheet" that contains only that cell's value:

::: ansi2html

      File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
     text                                                                                              
     N9240F was right base to final on Runway 4, and he reported a bird strike to the left wing.  He d… 


    2› faa-wildlife-strikes[0].REMARKS|                                     zEnter             1 lines 

If your cell's value contains newlines, they'll appear as such in the Text Sheet. From a Text Sheet, you also can press Control-o to open the cell in your terminal's default text editor.

Tip

Similarly, whenever you're editing a cell within VisiData (i.e., via the e command), you can also run Control-o to open that cell in your terminal's default text editor.



## Select a random sample of rows[¶](#select-a-random-sample-of-rows "Permalink to this headline")

In VisiData, you can create a randomly-sampled copy of any sheet. To create a random-sample sheet, press Space to initiate the longname-command prompt, and type `random-rows`. At the prompt, type the number of rows you'd like to include, and then press Enter.


## Only load part of the file[¶](#only-load-part-of-the-file "Permalink to this headline")

If you're only using VisiData to preview a dataset, consider loading just the beginning of the file.

### From the command-line[¶](#from-the-command-line "Permalink to this headline")

If you're working with a simple CSV file, you can accomplish this by using `head` on the command-line, combined with `vd`` ``-f`` ``csv` e.g.,:

::: highlight
    head -n 1000 faa-wildlife-strikes.csv | vd -f csv

That will load the first 1,000 lines of the file. (Because the `REMARKS` column contains some newline characters, the 1,000 lines correspond to slightly fewer than 1,000 rows.)

Alternatively, you can use a written-for-speed tool, such as [xsv](https://github.com/BurntSushi/xsv), to slice or filter the file before loading it into VisiData. E.g.,:

::: highlight
    xsv search "CHICAGO" faa-wildlife-strikes.csv | vd -f csv

### By halting the loading process[¶](#by-halting-the-loading-process "Permalink to this headline")

You can also just press Control-c while the data is loading, which will halt the loading process. VisiData handles this gracefully, and you can continue using the program just as you would if you hadn't halted the loading proces.

This approach works well if you're using a data source that's more complex than a CSV file, and if you don't care exactly how many lines are loaded.



## Caching dynamic columns[¶](#caching-dynamic-columns "Permalink to this headline")

Dynamic columns (for instance, those created with the = command) are calculated "lazily" --- i.e., only when they're needed.

If you're running a lot of operations on a dynamic column --- perhaps calculating its average, median, and sum --- you can save some time by first "caching" it. When you cache a dynamic column, VisiData calculates its current state and never recomputes it.

To cache (or re-cache) a column, navigate to it in your sheet and type z\'.


## Creating pivot tables[¶](#creating-pivot-tables "Permalink to this headline")

VisiData's pivot tables are similar to pivot tables you might have created in various spreadsheet programs. Pivot tables create a cross-tabulation of two or more columns in a dataset.

In VisiData, creating a pivot table involves the following steps:

- Use ! to designate the column(s) you want to serve as the pivot table's rows.
- *Optional*: Use + to specify additional metrics you want the pivot table to calculate. (By default, the pivot table's sole metric will be the overall count for each grouping.)
- Navigate to the column you want to serve as the pivot table's columns.
- Press Shift-W

Let's say we want to cross-tabulate species by whether their remains were collected. First, let's designate the `SPECIES` column as a key column:

::: ansi2html

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

Then, navigate to the `REMAINS_COLLECTED` column, either by tapping l or the right-arrow until we get there, or by typing c followed by `REMAINS` and then Enter:

::: ansi2html

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

Now, press Shift+W to create the pivot table:

::: ansi2html

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

... and g\_ to auto-adjust the column widths:

::: ansi2html

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

The rows of the pivot table represent each species, while the columns represent the number of rows for each species that fall into each `REMAINS_COLLECTED` category.

This is a simple pivot table, since `REMAINS_COLLECTED` can only be either `0` or `1`, but pivot tables on more complex columns can end up much wider.

Note

The order of the columns in a pivot table is based on the order the relevant values appear in the source sheet. If you want them to appear, instead, in alphabetical order, sort the source sheet's relevant column(s) first.



## Melting datasets[¶](#melting-datasets "Permalink to this headline")

To "melt" a dataset is to reshape it from a "wide" format to a "long" one, specifically by converting each value in each column into its own row. If that concept is unfamiliar, the example below should help clarify.

Melting a dataset in VisiData involves the following steps:

- *Optional*: Use ! to designate the column(s) you want to keep unmelted.
- *Optional*: Use - to hide the columns you don't want to appear, at all, in the melted sheet.
- Press Shift+M

If you skip the optional steps, pressing Shift-M on the original `faa-wildlife-strikes.csv` dataset creates this melted sheet:

::: ansi2html

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

Now let's examine how the optional steps affect melting. Press q to return to the source sheet, and press ! on each of the first two columns (`OPERATOR` and `ATYPE`):

::: ansi2html

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

Then use - (or the Columns Sheet) to hide all the other columns except for `STATE` and `AIRPORT`:

::: ansi2html

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

Now press Shift-M. In the resulting melted sheet, `OPERATOR` and `ATYPE` (the columns you keyed with !) are preserved as standard columns while `STATE` and `AIRPORT` have been converted to `Variable-Value` pairs:

::: ansi2html

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


## Transposing columns and rows[¶](#transposing-columns-and-rows "Permalink to this headline")

In VisiData, you can press Shift-T to "transpose" any given sheet, essentially rotating the struture 90 degrees, so that the rows are represented as columns (and vice versa).

Pressing Shift-T on the original `faa-wildlife-strikes.csv` dataset should give you this result:

::: ansi2html

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

If your source sheet has a key column, the values in that column will become the headers for the transposed sheet. For instance, here's the frequency table (with Shift-F) for the dataset's `OPERATOR` column:

::: ansi2html

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

It has `OPERATOR` as its key column, so transposing this sheet should result in something like this:

::: ansi2html

      File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
     OPERATOR  ║ UNKNOWN            │ SOUTHWEST AIRLINES │ BUSINESS           │ AMERICAN AIRLINES  │ D>
     count     ║ [23076] [16] UNKNO…│ [7752] [16] SOUTHW…│ [5868] [16] BUSINE…│ [4337] [16] AMERIC…│ […
     percent   ║ 31.41814617144102 %│ 10.554405838143992%│ 7.989325781505283 %│ 5.904857858621066 %│ 3…%
     histogram ║ ■■■■■■■■■■■■■■■■■■…│ ■■■■■■■■■■■■       │ ■■■■■■■■■          │ ■■■■■■■            │ ■…


    7› faa-wildlife-strikes_OPERATOR_freq_T|                                Shift+T             3 rows 

Note

If your source sheet has *multiple* key columns, VisiData will join together the columns' values with the `_` character to create the header names.



## Open the wildlife-strikes dataset in VisiData[¶](#open-the-wildlife-strikes-dataset-in-visidata "Permalink to this headline")

Run this command in your terminal:

::: highlight
    vd faa-wildlife-strikes.csv

If it worked, you should see something like this:

::: ansi2html

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


## Select only known species[¶](#select-only-known-species "Permalink to this headline")

For many of the wildlife strikes in the dataset, species is "unknown". We want to focus just on the known species, so we'll filter out the unknowns in this step.

First, navigate to the `SPECIES` column. Then, do the following:

- Press \| to raise the select-by-search prompt
- Type `unknown`
- Press Enter

Once you do that, you should see something like this:

::: ansi2html

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

Now, all the unknown species are selected. But we want the *opposite* of that: only known species selected. To do that, let's toggle the selection-ing for all rows, by typing gt (mnemonic: "global toggle"). Once you do that, you should see something like this:

::: ansi2html

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

Now that we've selected our desired rows, let's create a new sheet containing *only* those rows, by pressing \". The result should look something like this:

::: ansi2html

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



## Rename the filtered sheet[¶](#rename-the-filtered-sheet "Permalink to this headline")

By default, our sheet will be titled "faa-wildlife-strikes_selectedref". To make it slightly easier to distinguish from other sheets, let's rename it. To rename a sheet, do the following:

- Press Space to raise the type-a-command prompt
- Type `rename-sheet` (the command we want to use) and press Enter
- At the next prompt, type the new name we want; in this case `known_species`

At this point, you should see something like this:

::: ansi2html

     MA    │ GENERAL EDWARD LAW…│              │        │       │ Horned lark        │ 1            │   
     CA    │ SACRAMENTO INTL    │ Climb        │ 1500   │ 210   │ Northern pintail   │ 2-10         │ P 
     OH    │ RICKENBACKER INTL  │              │        │       │ American robin     │ 1            │   
    rename sheet to: known_species                                Space   rename-sheet      47460 rows 

When you've entered the name, press Enter to complete the edit (or Control-c to cancel the edit).


## Count the number of collisions per state[¶](#count-the-number-of-collisions-per-state "Permalink to this headline")

To get the denominator for our calculations, we'll want to know the total number of reported collisions for each state.

Back in our `known_species` sheet, navigate to the `STATE` column:

::: ansi2html

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

Then, to create a frequency table for the column, press Shift-F. Once you do, you should see something like this:

::: ansi2html

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



## Spruce up the frequency table[¶](#spruce-up-the-frequency-table "Permalink to this headline")

Because we'll later be joining this sheet to another sheet, let's hide the `percent` and `histogram` columns by navigating to each and pressing -.

Now the sheet should look something like this:

::: ansi2html

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


## Count the number of collisions per state *and* species[¶](#count-the-number-of-collisions-per-state-and-species "Permalink to this headline")

Now that we have the denominator --- collisions per state --- let's calculate the numerator: collisions *per species* per state.

To do that, we'll want to create a frequency table for the *combination* of the `STATE` and `SPECIES` columns. Here's how:

- Use the Sheets Sheet (Shift-S) to navigate back to the `known_species` sheet
- Navigate to the `STATE` column, and press ! to make it a "key" column
- Do the same thing for the `SPECIES` columns

At this point, you should see something like this:

::: ansi2html

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

Now, type gF, which will create a frequency table of all keyed columns. Once you do, you should see something like this:

::: ansi2html

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

Just like we did with the state-frequency table, let's simplify this table by removing the `percent` and `histogram` columns; navigate to each of those columns and press -, which should result in something like this:

::: ansi2html

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



## Prepare the state-species frequency table for joining[¶](#prepare-the-state-species-frequency-table-for-joining "Permalink to this headline")

There's just one step left before we can join the tables: making sure that the two frequency tables share the exact same key column. (VisiData uses each sheet's "key" columns to determine which rows to join.)

Because the key for the state-counts table is the `STATE` column, this table should also have `STATE` as its only key column. That means we need to un-key the `SPECIES` column. Luckily, that's easy. Just navigate to the `SPECIES` column and press ! to toggle it's status from keyed to un-keyed:

::: ansi2html

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


## Join the two frequency tables[¶](#join-the-two-frequency-tables "Permalink to this headline")

Now, for the moment we've all been waiting for: Let's join the tables!

First, press Shift-S to open the Sheets Sheet:

::: ansi2html

      File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
     name                             ║ type           │ pane#│ shortcut │ nRows#│ nCols#│ nVisibleCol>
     sheets                           ║ SheetsSheet    │    1 │ Shift+S  │     5 │    11 │           11
     known_species_STATE-SPECIES_freq ║ FreqTableSheet │    1 │ 4        │  5135 │     5 │            3
     known_species                    ║ CsvSheet       │    1 │ 2        │ 47460 │    16 │           16
     known_species_STATE_freq         ║ FreqTableSheet │    1 │ 3        │    63 │     4 │            2
     faa-wildlife-strikes             ║ CsvSheet       │    1 │ 1        │ 73448 │    16 │           16


    Shift+S› sheets|                                                     gk   go-top          5 sheets 

Then navigate to the `known_species_STATE-SPECIES_freq` row, and press s to select it. Do the same for the `known_species_STATE_freq`, so that the Sheets Sheet now looks like this:

::: ansi2html

      File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
     name                             ║ type           │ pane#│ shortcut │ nRows#│ nCols#│ nVisibleCol>
     sheets                           ║ SheetsSheet    │    1 │ Shift+S  │     5 │    11 │           11
    •known_species_STATE-SPECIES_freq ║ FreqTableSheet │    1 │ 4        │  5135 │     5 │            3
     known_species                    ║ CsvSheet       │    1 │ 2        │ 47460 │    16 │           16
    •known_species_STATE_freq         ║ FreqTableSheet │    1 │ 3        │    63 │     4 │            2
     faa-wildlife-strikes             ║ CsvSheet       │    1 │ 1        │ 73448 │    16 │           16


    Shift+S› sheets|                                              s   select-row          5 sheets  •2 

Press & to raise the sheet-joining prompt:

::: ansi2html

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

Type `inner` and press Enter to complete the action. After that, you should see something like this:

::: ansi2html

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

The columns that had previously been called `count` in both sheets have been auto-prefixed with the name of their source sheet. Let's clarify things by using the \^ shortcut to rename them to `count` and `state_total`, respectively. On the `state_total` column, press \_ to expand the width to see the full name:

::: ansi2html

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

Finally, let's give the sheet a shorter name:

- Press Space to raise the type-a-command prompt
- Type `rename-sheet` and press Enter
- At the next prompt, type the new name we want; in this case `joined`



## Calculate each species' state-level percentages[¶](#calculate-each-species-state-level-percentages "Permalink to this headline")

Now that we have the numerator and denominator in the same sheet, let's calculate the percentage of known-species collisions to each species in each state.

Let's say we want the new column to appear as the last column in the sheet, so let's navigate to the currently-last column by typing gl. Then let's create the new column by pressing =, typing `count`` ``*`` ``100`` ``/`` ``state_total`, and then pressing Enter.

Once you do that, you should see something like this:

::: ansi2html

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

It worked! But the column name is a bit wonky and literal. Let's make the following tweaks:

- Rename the column by navigating to it, pressing \^ to enter the column-name-editing mode, typing `pct_of_state`, and then pressing Enter.
- Press % to tell VisiData that it's a "float"-type numeric column. (By default, VisiData assumes that newly created columns are just plain-old text.)
- Press \_ to resize the column to fit its contents more precisely

Now the sheet should look something like this:

::: ansi2html

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


## Sort by percentage[¶](#sort-by-percentage "Permalink to this headline")

Of course, to answer our main question, we'll need to sort the column. To sort it descendingly, press [\]]. Now you should see something like this:

::: ansi2html

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



## Limit to rows with at least 20 collisions[¶](#limit-to-rows-with-at-least-20-collisions "Permalink to this headline")

Hmmm, many of the highest-ranking species-state combinations seem to come from "states" --- like the striped skunk that was struck in Nova Scotia --- with very few reported collisions. So let's limit the results to species-state combinations with at least 20 reports.

To do that, we'll use z\|, VisiData's "select by expression" command.

First, type z\| to raise the selection prompt. Then, type `count`` ``>=`` ``20`:

::: ansi2html

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

Next, press Enter to complete the action. Now you should see something like this:

::: ansi2html

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

Finally, press \" to create a new sheet containing only the selected rows:

::: ansi2html

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

There you have it! The [Yellow Bittern](https://en.wikipedia.org/wiki/Yellow_bittern) accounted for more than 40% of the reported, known-species collisions in "PI" (the [FAA's abbreviation](https://www.faa.gov/airports/airport_safety/wildlife/resources/media/2005_FAA_Manual_complete.pdf) for "USA-possessed Pacific Islands," such as Guam). In Colorado, the Horned Lark has been nearly as collision-dominating, as has the Pacific Golden-Plover in Hawaii, and Mourning Doves in Arizona and Mississippi.


## Take it one step further[¶](#take-it-one-step-further "Permalink to this headline")

What if we want to find the species that are *disproportionately* involved in collisions in their state? How would you do that? (Hint: It involves just one more frequency table and one more join.)



## Open the wildlife-strikes dataset in VisiData[¶](#open-the-wildlife-strikes-dataset-in-visidata "Permalink to this headline")

Let's start from the very beginning.

Run this command in your terminal:

::: highlight
    vd faa-wildlife-strikes.csv

If it worked, you should see something like this:

::: ansi2html

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


## Tell VisiData that `HEIGHT` is an integer column[¶](#tell-visidata-that-height-is-an-integer-column "Permalink to this headline")

Navigate to the `HEIGHT` column, and press \#.

You should see something like this:

::: ansi2html

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

As you can see, many of the reported collisions are missing height data, or appear to have occurred on the ground (i.e., `HEIGHT`` ``==`` ``0`).

So, let's focus only on collsions reported to have occurred above the ground.



## Select only rows where `HEIGHT` is greater than zero[¶](#select-only-rows-where-height-is-greater-than-zero "Permalink to this headline")

To do that, we'll use z\|, VisiData's "select by expression" command. Type z\| and then, at the prompt, type `HEIGHT`` ``>`` ``0`. You should see something like this:

::: ansi2html

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

Then press Enter. Now you you should see the above-ground collisions selected:

::: ansi2html

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


## Create a new sheet with only the selected rows[¶](#create-a-new-sheet-with-only-the-selected-rows "Permalink to this headline")

To do so, press \". Once you do that, you should see something like this:

::: ansi2html

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



## Get the average collision height for each species[¶](#get-the-average-collision-height-for-each-species "Permalink to this headline")

This is a two-step process. First, navigate to the `HEIGHT` column, and press + to add an aggregator. At the prompt at the bottom of the screen, type `mean` ...

::: ansi2html

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

... and then press Enter.

Note

Adding an aggregator doesn't change the appearance of the sheet. But if you want to confirm that you've added an aggregator correctly, you can press Shift-C to open up the Columns Sheet, and look at the `aggregators` field.

Then, to get the average for each animal, navigate to the `SPECIES` column, and press Shift-F to create a frequency sheet. It should look something like this:

::: ansi2html

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


## Sort the species by collision height[¶](#sort-the-species-by-collision-height "Permalink to this headline")

By default, frequency tables are sorted by the raw count of matching rows. To sort by the highest average collision height, navigate to the `mean_HEIGHT` column, and press [\]].

You should see something like this:

::: ansi2html

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

Hrrrm, it seems like a lot of these species show up just a few times --- too few to be particularly informative. Let's do something about that.



## Limit the results to relatively common species[¶](#limit-the-results-to-relatively-common-species "Permalink to this headline")

This step will seem familiar; it's a lot like how we selected only above-the-ground collisions.

First, type z\| to raise the "select by expression" prompt. Then, type `count`` ``>=`` ``20`:

::: ansi2html

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

Next, press Enter to complete the action. Because there are no high-count species in the visible part of the sheet, you won't notice much of effect at first; just some status messages in the sidebar:

::: ansi2html

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

Now press \" to create a new sheet containing only the selected rows. Tada!:

::: ansi2html

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

Finally, type g\_ to widen all the columns, so that you can read all the names:

::: ansi2html

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


## Step 1: Use `vd` to open a data file[¶](#step-1-use-vd-to-open-a-data-file "Permalink to this headline")

Download [`faa-wildlife-strikes.csv`](../../_downloads/a61d9b28e9a942e1254bffeb8289a447/faa-wildlife-strikes.csv), a dataset of all aircraft-wildlife collisions [reported to the Federal Aviation Administration](https://wildlife.faa.gov/database.aspx) between 2010 and mid-2016.

From your terminal, move into the directory where you downloaded the dataset. Then run the following command:

::: highlight
    vd faa-wildlife-strikes.csv

If it worked, you should see something like this:

::: ansi2html

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



## Step 2: Test-drive a frequency table[¶](#step-2-test-drive-a-frequency-table "Permalink to this headline")

One of VisiData's strengths is how quickly it lets you summarize your data. Frequency tables are a great example. To create one, press Shift+F.

If it worked, you should see something like this:

::: ansi2html

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


## Step 3: Explore the menu[¶](#step-3-explore-the-menu "Permalink to this headline")

Pressing Control-h will open VisiData's menu system, where you can explore the most common commands:

::: ansi2html

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

You can navigate the menu either with your arrow keys or by pointing and clicking with your mouse. To run a command from the menu, press Enter or click a second time on the selected item.



## Why use VisiData?[¶](#why-use-visidata "Permalink to this headline")

- 

  It's fast.

  :   - VisiData opens in a blink of an eye, and can load multi-megabyte datasets nearly instantly.

- 

  It's nimble.

  :   - VisiData makes it easy to search, filter, sort, and join any table.

- 

  It's great for getting a grasp of new datasets.

  :   - With just a few keystrokes, you can summarize any column.

- 

  It works with [lots of data formats](../../basics/opening-files/#compatible-filetypes).

  :   - CSV, Excel, JSON, and more.

- 

  It's non-destructive.

  :   - VisiData won't alter your raw data unless you explicitly tell it to.

- 

  It's keyboard-driven.

  :   - You never have to reach for a mouse.

- 

  It lives in your terminal.

  :   - VisiData plays well with other command-line tools, and you can run it on remote servers via SSH.


## Why not use VisiData?[¶](#why-not-use-visidata "Permalink to this headline")

VisiData isn't for every task. You might want to choose another tool for:

- 

  Complex analysis.

  :   - You're probably better off using Python, R, or another programming language.

- 

  "Literate" analysis.

  :   - Although VisiData lets you save and replay your analyses, it's not as legible/flexible as Jupyter notebooks, R Markdown, or other tools.

- 

  Mission-critical analysis.

  :   - VisiData is well-engineered, but still a relatively young piece of software.



## `vd` command-line arguments

When you launch `vd`, you can specify certain behaviors via arguments on the command-line.

For instance, to tell VisiData to ignore the first three lines of your input file, you\'d run the following:

    vd my-spreadsheet.csv --skip 3

To see the full list of configurable options, run `vd -h | less`:


<pre>
vd(1)                        Quick Reference Guide                       vd(1)

NAME
     VisiData — a terminal utility for exploring and arranging tabular data

SYNOPSIS
     vd [options] [input ...]
     vd [options] --play cmdlog [-w waitsecs] [--batch] [-i] [-o output]
        [field=value]
     vd [options] [input ...] +toplevel:subsheet:col:row

DESCRIPTION
     VisiData is an easy-to-use multipurpose tool to explore, clean, edit, and
     restructure data. Rows can be selected, filtered, and grouped; columns
     can be rearranged, transformed, and derived via regex or Python expres‐
     sions; and workflows can be saved, documented, and replayed.

   REPLAY MODE
     -p, --play=cmdlog       replay a saved cmdlog within the interface
     -w, --replay-wait=seconds
                             wait seconds between commands
     -b, --batch             replay in batch mode (with no interface)
     -i, --interactive       launch VisiData in interactive mode after batch
:
</pre>


(Press `Space` to scroll down the list.)


## The global options sheet

You can also set most of the same options, plus additional color/display options, through the \"global options sheet\". To launch that sheet, press `Shift-O`. You should see something like this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 option             ║ global_value       │ default            │ description                        
 visidata_dir       ║ ~/.visidata/       │ ~/.visidata/       │ directory to load and store additi… 
 debug              ║                    │ False              │ exit on error and display stacktra… 
 disp_menu          ║                    │ True               │ show menu on top line when not act… 
 disp_menu_keys     ║                    │ True               │ show keystrokes inline in submenus  
 color_menu         ║                    │ black on 68 blue   │ color of menu items in general      
 color_menu_active  ║                    │ 223 yellow on black│ color of active menu items          
 color_menu_spec    ║                    │ black on 34 green  │ color of sheet-specific menu items  
 color_menu_help    ║                    │ black italic on 68…│ color of helpbox                    
 disp_menu_boxchars ║                    │ ││──┌┐└┘├┤         │ box characters to use for menus     
 disp_menu_more     ║                    │ »                  │ command submenu indicator           
 disp_menu_push     ║                    │ ⎘                  │ indicator if command pushes sheet … 
 disp_menu_input    ║                    │ …                  │ indicator if input required for co… 
 disp_menu_fmt      ║                    │ | VisiData {vd.ver…│ right-side menu format string       
 undo               ║                    │ True               │ enable undo/redo                    
 disp_float_fmt     ║                    │ {:.02f}            │ default fmtstr to format float val… 
 disp_int_fmt       ║                    │ {:d}               │ default fmtstr to format int values 
 col_cache_size     ║                    │ 0                 #│ max number of cache entries in eac… 
 disp_formatter     ║                    │ generic            │ formatter to create the text in ea… 
 disp_displayer     ║                    │ generic            │ displayer to render the text in ea… 
 disp_splitwin_pct  ║                    │ 0                 #│ height of second sheet on screen    
 disp_note_none     ║                    │ ⌀                  │ visible contents of a cell whose v… 
Shift+O› global_options|                                   Shift+O   quit-sheet        242 options 
</pre>


To customize an option navigate to the `global_value` cell in the option\'s row, and press `e` to edit it, like you would with any other cell in VisiData.

For example, to change VisiData\'s default column width from 20 to 10, navigate down to the `default_width` row, over to the `global_value` cell, press `e`, type `10`, and then press `Enter`. Once you do, the global options sheet should look like this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 option             ║ global_value       │ default            │ description                        
 disp_selected_note ║                    │ •                  │                                     
 disp_sort_asc      ║                    │ ↑↟⇞⇡⇧⇑             │ characters for ascending sort       
 disp_sort_desc     ║                    │ ↓↡⇟⇣⇩⇓             │ characters for descending sort      
 color_default      ║                    │ white on black     │ the default fg and bg colors        
 color_default_hdr  ║                    │ bold               │ color of the column headers         
 color_bottom_hdr   ║                    │ underline          │ color of the bottom header row      
 color_current_row  ║                    │ reverse            │ color of the cursor row             
 color_current_col  ║                    │ bold               │ color of the cursor column          
 color_current_cell ║                    │                    │ color of current cell, if differen… 
 color_current_hdr  ║                    │ bold reverse       │ color of the header for the cursor… 
 color_column_sep   ║                    │ 246 blue           │ color of column separators          
 color_key_col      ║                    │ 81 cyan            │ color of key columns                
 color_hidden_col   ║                    │ 8                  │ color of hidden columns on metashe… 
 color_selected_row ║                    │ 215 yellow         │ color of selected rows              
 color_clickable    ║                    │ underline          │ color of internally clickable item  
 color_code         ║                    │ bold white on 237  │ color of code sample                
 color_heading      ║                    │ bold 200           │ color of header                     
 color_guide_unwrit…║                    │ 243 on black       │ color of unwritten guides in Guide… 
 force_256_colors   ║                    │ False              │ use 256 colors even if curses repo… 
 quitguard          ║                    │ False              │ confirm before quitting modified s… 
 default_width      ║ 10                #│ 20                #│ default column width                
Shift+O› global_options|                                        e   edit-option        242 options 
</pre>


As with any other sheet, you can leave the global options sheet, and return to your previous sheet, by pressing `q`.



## Sheet-specific options sheets

As the name suggests, the changes you make on the *global* options sheet affect your entire VisiData session. To change VisiData\'s behavior for just one sheet, type `zO` to edit the \"sheet options sheet\":


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 option             ║ sheet_value        │ default            │ description                        
 visidata_dir       ║                    │ ~/.visidata/       │ directory to load and store additi… 
 debug              ║                    │ False              │ exit on error and display stacktra… 
 disp_menu          ║                    │ True               │ show menu on top line when not act… 
 disp_menu_keys     ║                    │ True               │ show keystrokes inline in submenus  
 color_menu         ║                    │ black on 68 blue   │ color of menu items in general      
 color_menu_active  ║                    │ 223 yellow on black│ color of active menu items          
 color_menu_spec    ║                    │ black on 34 green  │ color of sheet-specific menu items  
 color_menu_help    ║                    │ black italic on 68…│ color of helpbox                    
 disp_menu_boxchars ║                    │ ││──┌┐└┘├┤         │ box characters to use for menus     
 disp_menu_more     ║                    │ »                  │ command submenu indicator           
 disp_menu_push     ║                    │ ⎘                  │ indicator if command pushes sheet … 
 disp_menu_input    ║                    │ …                  │ indicator if input required for co… 
 disp_menu_fmt      ║                    │ | VisiData {vd.ver…│ right-side menu format string       
 undo               ║                    │ True               │ enable undo/redo                    
 disp_float_fmt     ║                    │ {:.02f}            │ default fmtstr to format float val… 
 disp_int_fmt       ║                    │ {:d}               │ default fmtstr to format int values 
 col_cache_size     ║                    │ 0                 #│ max number of cache entries in eac… 
 disp_formatter     ║                    │ generic            │ formatter to create the text in ea… 
 disp_displayer     ║                    │ generic            │ displayer to render the text in ea… 
 disp_splitwin_pct  ║                    │ 0                 #│ height of second sheet on screen    
 disp_note_none     ║                    │ ⌀                  │ visible contents of a cell whose v… 
zShift+O› faa-wildlife-strikes_options|                   zShift+O   quit-sheet        242 options 
</pre>


It the sheet options sheet operates just like the global options sheet, but applies only to the sheet you were on when you typed `zO`.


## The `~/.visidatarc` file

The approaches above all affect only your current VisiData session. When you quit VisiData, those customizations evaporate.

To persist your customizations from session to session, you can specify them in your computer\'s `~/.visidatarc` file.

Open that file in the editor of your choosing and, for each option you wish to modify, write `options.my_example_option = my_custom_value`.

For instance:

    options.default_width = 10
    options.encoding = "latin-1"
    options.bulk_select_clear = True

\... and then save the file. Next time you run VisiData, these options will take effect.

:::: note
::: title
Note

The `~/.visidatarc` file expects its commands to be written in Python. For basic options-setting, it doesn\'t matter too much whether you know Python, as long as you follow the pattern in the example above. Numbers can be written plainly, strings of characters should be wrapped in quotation marks, and `True`/`False` values need to be written exactly as such.

:::: tip
::: title
Tip

If you know Python and are willing to acquaint yourself with [VisiData\'s architecture](https://www.visidata.org/docs/api/), you can use your `~/.visidatarc` file to customize VisiData in ways far more powerful than simple option-setting --- including [creating your own commands](https://github.com/saulpw/visidata/blob/stable/docs/customize.md#how-to-configure-commands).



## Examining cell errors

In the [Understanding Columns](../../basics/understanding-columns/) chapter, we\'ve already seen an example of what a cell-specific error looks like, when we told VisiData that the `HEIGHT` column values of the wildlife-strikes dataset should be integers (using `#`):


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


VisiData obeyed but marked some cells with a `!` error/warning annotation --- specifically the empty cells, because Python considers it impossible to convert nothingness a whole number.

In some cases, we can intuit why a cell is marked with a `!`. In other cases, we might want to know more. To do so, navigate to the cell and type `z` + `Control-e`. If we do this on the second cell of the `HEIGHT` column, here\'s what we\'ll see:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 text                                                                           ║                  
 Traceback (most recent call last):                                             ║                   
 File "lib/python3.10/site-packages/visidata/wrappers.py", line 105, in wrapply ║                   
 return func(*args, **kwargs)                                                   ║                   
 ValueError: invalid literal for int() with base 10: ''                         ║                   


zCtrl+E› faa-wildlife-strikes_cell_error|                              zCtrl+E             4 lines 
</pre>


If you use Python frequently, this output may look familiar; it\'s the \"stack traceback\" for the error that VisiData encountered while trying to convert the blank cell (an empty string) to an integer. If you don\'t use Python frequently or at all, you may still be able to get a sense of the issue at hand; the final line is usually the most descriptive.

The error sheet is like any other sheet in VisiData, so you can quit it and return to the previous sheet by pressing `q`.

:::: note
::: title
Note

There are, in fact, two types of cell errors:

- Errors caused by type conversions, as demonstrated above. VisiData flags these with a **yellow** exclamation mark.
- Errors stemming from dynamic column expressions, such as `=HEIGHT / 0`. VisiData flags these with a **red** exclamation mark.


## Examining general errors

Let\'s try creating a general error on purpose. Let\'s press `=` to create a new column, and type `(` at the prompt, and then `Enter`. We\'ll be greeted by an error message at the bottom of the screen:


<pre>
 DELTA AIR LINES    │ A-320        │ 05/07/15 00:00:00 │ CA    │ METRO OAKLAND INTL │              │
 DELTA AIR LINES    │ A-320        │ 05/08/15 00:00:┌────────────────────────────────| statuses |─┐│
 LUFTHANSA          │ A-380        │ 05/10/15 00:00:│ SyntaxError: '(' was never closed (<expr>,  ││
 BUSINESS           │ C-172        │ 05/08/15 00:00:│ line 1)                                     ││
 SPIRIT AIRLINES    │ A-319        │ 05/10/15 00:00:└─────────────────────────────────────────────┘│
1› faa-wildlife-strikes|                                           =   addcol-expr      73448 rows 
</pre>


Why\'s that? In Python, all open parentheses need to be closed.

To examine this general error in greater detail, we can press `Control-e` --- now, or at any point until you trigger another error --- to reveal its full traceback in a VisiData text sheet:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 text                                                                                ║             
 Traceback (most recent call last):                                                  ║              
 File "lib/python3.10/site-packages/visidata/basesheet.py", line 211, in execCommand ║              
 escaped = super().execCommand2(cmd, vdglobals=vdglobals)                            ║              
 File "lib/python3.10/site-packages/visidata/extensible.py", line 79, in wrappedfunc ║              
 r = oldfunc(*args, **kwargs)                                                        ║              
 File "lib/python3.10/site-packages/visidata/basesheet.py", line 76, in execCommand2 ║              
 exec(code, vdglobals, LazyChainMap(vd, self))                                       ║              
 File "addcol-expr", line 1, in <module>                                             ║              
 'VisiData: a curses interface for exploring and arranging tabular data'             ║              
 File "lib/python3.10/site-packages/visidata/column.py", line 544, in __init__       ║              
 self.expr = expr or name                                                            ║              
 File "lib/python3.10/site-packages/visidata/column.py", line 570, in expr           ║              
 self.compiledExpr = compile(expr, '<expr>', 'eval') if expr else None               ║              
 File "<expr>", line 1                                                               ║              
 (                                                                                   ║              
 ^                                                                                   ║              
 SyntaxError: '(' was never closed                                                   ║              


Ctrl+E› errors_recent|                                        Shift+G   go-bottom         17 lines 
</pre>


:::: tip
::: title
Tip

You can type `g` + `Control-e` to open a sheet listing all general errors you have encountered during your current VisiData session.



## How to report a bug

If you encounter an error that seems to come from a bug within VisiData itself (rather than an invalid command), follow [VisiData\'s \"Help and Support\" instructions](https://github.com/saulpw/visidata#help-and-support). The developers ask that bug reports include a \"command log\" that reproduces the issue, so that they can investigate it with more precision. The next chapter demonstrates how to do so.


## How to install a plugin

Installing a plugin so involves two steps:

- First, make the plugin available to VisiData. Depending on the plugin, you\'ll do this either by saving the plugin file to your `~/.visidata/` directory, or by running `pip install [plugin_package_name]`.
- Then, use your `~/.visidatarc` configuration file to import the plugin. If you\'ve saved your plugin as `~/.visidata/myplugin.py`, all you need to do is add a line that says `import myplugin`.

### Example

To demonstrate, let\'s install [a \"dedupe\" plugin](https://github.com/jsvine/visidata-plugins):

- Open [this file](https://raw.githubusercontent.com/jsvine/visidata-plugins/master/plugins/dedupe.py) in your browser and save it to `~/.visidata/dedupe.py` on your computer.
- Open your `~/.visidatarc` file, add `import dedupe` on a new line, and save the file.

That\'s it. Next time you start VisiData, you should have access to two new commands: `select-duplicate-rows` and `dedupe-rows`.

Let\'s give the plugin a spin. Download `dedupe-example.csv <../../datasets/dedupe-example.csv>` and open it in VisiData:

    vd dedupe-example.csv

You should see this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 animal │ name   ║
 dog    │ Apollo ║
 dog    │ Bambi  ║
 dog    │ Cutie  ║
 fish   │ Fido   ║
 fish   │ Fido   ║


                                                   ┌─────────────────────────────────| statuses |─┐
                                                   │ saul.pw/VisiData v3.0.2                      │
                                                   │ opening datasets/dedupe-example.csv as csv   │
                                                   │ I can see you're trying to invent something! │
                                                   └──────────────────────────────────────────────┘
1› dedupe-example|                                                                          5 rows 
</pre>


Press `Space` to initiate the longname-command prompt, and type `dedupe-rows`:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 animal │ name   ║
 dog    │ Apollo ║
 dog    │ Bambi  ║
 dog    │ Cutie  ║
 fish   │ Fido   ║
 fish   │ Fido   ║


                                                 ┌─────────────────────────────| Choose Command |─┐
                                                 │ Start typing a command longname or keyword in  │
                                                 │ its helpstring.                                │
              dedupe-rows                        │                                                │
         *    addcol-regex-subst - add column der│ - Enter to execute top command.                │
              addcol-subst - add column derived f│ - Tab to highlight top command.                │
         ]    sort-desc - sort descending by curr│                                                │
        g]    sort-keys-desc - sort descending by│ ## When Command Highlighted                    │
         )    contract-col - remove current colum│                                                │
        z)    contract-col-depth - remove current│ - Tab/Shift+Tab to cycle highlighted command.  │
   Shift+D    cmdlog-sheet - open current sheet's│ - Enter to execute highlighted command.        │
  gShift+Y    syscopy-selected - yank (copy) sele│ - 0-9 to execute numbered command.             │
 gzShift+Y    syscopy-cells - yank (copy) content└────────────────────────────────────────────────┘
command name: dedup                                          Space   exec-longname          5 rows 
</pre>


Press `Enter` to execute the command. Now you should see a new copy of the sheet, but with the duplicate row removed:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 animal │ name   ║
 dog    │ Apollo ║
 dog    │ Bambi  ║
 dog    │ Cutie  ║
 fish   │ Fido   ║


                                                      ┌──────────────────────────────| statuses |─┐
                                                      │ No key cols specified. Using all columns. │
                                                      └───────────────────────────────────────────┘
2› dedupe-example_deduped|                                                Space             4 rows 
</pre>




## Where to find plugins

Here is a (likely incomplete) list of resources:

- [jsvine/visidata-plugins](https://github.com/jsvine/visidata-plugins)
- [ajkerrigan/visidata-plugins](https://github.com/ajkerrigan/visidata-plugins)
- [anjakefala/vd-plugins](https://github.com/anjakefala/vd-plugins)

:::: warning
::: title
Warning

As with any software you download, plugins may contain malicious code. If you\'re unsure whether a plugin is safe to install, err on the side of caution.


## Viewing the command log

From anywhere within VisiData, you can press `D` to view the command log relevant to your current sheet. It ignores actions you may have taken outside of the current sheet\'s direct lineage. Essentially, it answers the question: What steps did I take to get here?

Let\'s start with a simple example, following these steps:

- Initiate a fresh VisiData session with `vd faa-wildlife-strikes.csv`
- Rename the sheet to `strikes`: Press `Space` to raise the type-a-command prompt, type `rename-sheet`, press `Enter`, and type `strikes`, and then press `Enter` again
- Navigate to the `AIRPORT` column
- Press `F` to generate a frequency sheet of the `AIRPORT` columns
- Navigate to the sixth row, and press `s` to select it

You should see something like this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 AIRPORT            ║↓count♯│ percent%│ histogram                             ~║                   
 UNKNOWN            ║  8424 │   11.47 │ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ║
 DENVER INTL AIRPORT║  2756 │    3.75 │ ■■■■■■■■■■■■                           ║
 DALLAS/FORT WORTH …║  2392 │    3.26 │ ■■■■■■■■■■                             ║
 CHICAGO O'HARE INT…║  1583 │    2.16 │ ■■■■■■■                                ║
 JOHN F KENNEDY INTL║  1302 │    1.77 │ ■■■■■                                  ║
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
 DETROIT METRO WAYN…║   734 │    1.00 │ ■■■            │ selected 1217 rows                       │
 BALTIMORE/WASH INT…║   691 │    0.94 │ ■■■            └──────────────────────────────────────────┘
2› strikes_AIRPORT_freq|                                        s   select-row       1512 bins  •1 
</pre>


Now press `D` to open the command log for this sheet:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 sheet              │ col     │ row            │ longname     │ input              │ keystrokes │ …
                   ⌀│        ⌀│               ⌀│ open-file    │ faa-wildlife-strik…│ o          │  ⌀
 faa-wildlife-strik…│         │                │ rename-sheet │ strikes            │           ⌀│ R
 strikes            │ AIRPORT │                │ freq-col     │                    │ Shift+F    │ o
 strikes_AIRPORT_fr…│         │ キMEMPHIS INTL │ select-row   │                    │ s          │ s


Shift+D› strikes_AIRPORT_freq_cmdlog|                        Shift+D             4 logged commands 
</pre>


Two things you\'ll see that you might not have expected:

- The command to open `faa-wildlife-strikes.csv` appears in the log, with \"longname\" `open-file`. Passing filenames to VisiData on the command line is equivalent to opening them *within* the program via `open-file` or keyboard shortcut `o`.
- Navigational commands do *not* appear in the command log. The reason: Navigating around a sheet doesn\'t alter its contents. For the frequency sheet (`freq-col`) and row-selection (`select-row`) commands, VisiData has captured the necessary context via the log\'s `col` and `row` columns.



## Saving the command log

The command log behaves *virtually* the same as any other sheet in VisiData. That means you can sort, filter, and otherwise edit its rows, columns, and cells. That also means you can save just like you\'d save any other sheet, with `Control-s`. Doing so with the example above should raise a prompt that looks like this:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 sheet              │ col     │ row            │ longname     │ input              │ keystrokes │ …
                   ⌀│        ⌀│               ⌀│ open-file    │ faa-wildlife-strik…│ o          │  ⌀
 faa-wildlife-strik…│         │                │ rename-sheet │ strikes            │           ⌀│ R
 strikes            │ AIRPORT │                │ freq-col     │                    │ Shift+F    │ o
 strikes_AIRPORT_fr…│         │ キMEMPHIS INTL │ select-row   │                    │ s          │ s


save to: strikes_AIRPORT_freq_cmdlog.vdj            Ctrl+S   save-sheet          4 logged commands 
</pre>


As you\'ll see, VisiData suggests its own `.vd` file extension. That helps distinguish command logs from other files, but it\'s not necessary. It\'s just a tab-separated-values file, and you can save it with the `.tsv` extension if you prefer. For the sake of the subsequent steps in this tutorial, let\'s save it as `example-cmdlog.vd`, in the same directory as `faa-wildlife-strikes.csv`.


## Replaying the full command log

To fully replay the `example-cmdlog.vd` log we saved in the section above, run the following command from your computer\'s terminal:

    vd --play example-cmdlog.vd

Note that, this time, we don\'t point VisiData to the dataset itself, since that information (the path to the dataset) is now specified within the command log. If the replay worked, you should see VisiData advance through each step (some more quickly than others), ultimately arriving at the result you previously obtained manually:


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 AIRPORT            ║↓count♯│ percent%│ histogram                             ~║                   
 UNKNOWN            ║  8424 │   11.47 │ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ║
 DENVER INTL AIRPORT║  2756 │    3.75 │ ■■■■■■■■■■■■                           ║
 DALLAS/FORT WORTH …║  2392 │    3.26 │ ■■■■■■■■■■                             ║
 CHICAGO O'HARE INT…║  1583 │    2.16 │ ■■■■■■■                                ║
 JOHN F KENNEDY INTL║  1302 │    1.77 │ ■■■■■                                  ║
•MEMPHIS INTL       ║  1217 │    1.66 │ ■■■■■                                  ║
 SALT LAKE CITY INTL║  1179 │    1.61 │ ■■■■■                                  ║
 PHILADELPHIA INTL  ║  1131 │    1.54 │ ■■■■■                                  ║
 ORLANDO INTL       ║  1026 │    1.40 │ ■■■■                                   ║
 SACRAMENTO INTL    ║  1021 │    1.39 │ ■■■■                                   ║
 LA GUARDIA ARPT    ║   974 │    1.33 │ ■■■■         ┌───────────────────────────────| statuses |─┐
 CHARLOTTE/DOUGLAS …║   960 │    1.31 │ ■■■■         │ saul.pw/VisiData v3.0.2                    │
 NEWARK LIBERTY INT…║   917 │    1.25 │ ■■■■         │ opening example-cmdlog.vdj as vdj          │
 LOUISVILLE INTL AR…║   841 │    1.15 │ ■■■          │ Was I the same when I got up this morning? │
 AUSTIN-BERGSTROM I…║   817 │    1.11 │ ■■■          │ opening faa-wildlife-strikes.csv as csv    │
 LOUIE ARMSTRONG NE…║   809 │    1.10 │ ■■■          │ Rename current sheet                       │
 KANSAS CITY INTL   ║   807 │    1.10 │ ■■■          │ open Frequency Table grouped on current    │
 HARTSFIELD - JACKS…║   775 │    1.06 │ ■■■          │ column, with aggregations of other columns │
 GEORGE BUSH INTERC…║   746 │    1.02 │ ■■■          │ select current row                         │
 DETROIT METRO WAYN…║   734 │    1.00 │ ■■■          │ selected 1217 rows                         │
 BALTIMORE/WASH INT…║   691 │    0.94 │ ■■■          └────────────────────────────────────────────┘
3› strikes_AIRPORT_freq|                                            select-row       1512 bins  •1 
</pre>


You can adjust the replay behavior via various command line arguments, such as:

    vd --play example-cmdlog.vd --replay-wait 2

\... which will pause two seconds between each of the logged steps. And:

    vd --play example-cmdlog.vd --batch --output cmdlog-results.csv

\... which will replay the command log in \"batch\" mode (displaying status messages but not the full VisiData interface) and, when complete, will save the final sheet to `cmdlog-results.csv`.



## Sharing command logs on GitHub

Command logs can help you demonstrate specific VisiData behavior to others, especially if that behavior involves more than a few steps. You\'ll want to do this, for instance, when filing potential bug reports [via VisiData\'s GitHub repository](https://github.com/saulpw/visidata/#help-and-support). Some advice for doing so:

- When attaching a command log to a GitHub issue or comment, you\'ll need to change the file extension, since GitHub will reject fileames ending in `.vd`. The developers recommend appending `.txt` to the filename; in the example above, that would be `example-cmdlog.vd.txt`.
- If replaying the command log requires a specific dataset, attach that dataset in the same message and aim to make it as simple as possible. Alternatively, you can use a dataset from VisiData\'s [sample_data directory](https://github.com/saulpw/visidata/tree/stable/sample_data) (for instance, as done in [this issue](https://github.com/saulpw/visidata/issues/1315)).


## How to move one row/column at a time

You can use your keyboard\'s arrow keys to navigate between columns.

Alternatively, you can use the `h`/`j`/`k`/`l` keys to move left/down/up/right. (That convention, like several others in VisiData, is [borrowed from the vim text editor](http://www.catonmat.net/blog/why-vim-uses-hjkl-as-arrow-keys/).)

When you first open a dataset in VisiData, you\'ll start in the top-left corner:


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
 BUSINESS           │ HELICOPTER   │ 05/06/15 00:00:00 │       │ UNKNOWN            │ En Route     │
 DELTA AIR LINES    │ A-320        │ 05/07/15 00:0┌──────────────────────────────────| statuses |─┐│
 DELTA AIR LINES    │ A-320        │ 05/08/15 00:0│ saul.pw/VisiData v3.0.2                       ││
 LUFTHANSA          │ A-380        │ 05/10/15 00:0│ opening datasets/faa-wildlife-strikes.csv as  ││
 BUSINESS           │ C-172        │ 05/08/15 00:0│ csv                                           ││
 SPIRIT AIRLINES    │ A-319        │ 05/10/15 00:0└───────────────────────────────────────────────┘│
1› faa-wildlife-strikes|                                                                73448 rows 
</pre>


If you press the down-arrow and then the right-arrow (or, correspondingly, `j` and then `l`), you should see the row and column selectors move:


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
 BUSINESS           │ HELICOPTER   │ 05/06/15 00:00:00 │       │ UNKNOWN            │ En Route     │
 DELTA AIR LINES    │ A-320        │ 05/07/15 00:00:00 │ CA    │ METRO OAKLAND INTL │              │
 DELTA AIR LINES    │ A-320        │ 05/08/15 00:00:00 │ UT    │ SALT LAKE CITY INTL│              │
 LUFTHANSA          │ A-380        │ 05/10/15 00:00:00 │ TX    │ GEORGE BUSH INTERC…│ CLIMB        │
 BUSINESS           │ C-172        │ 05/08/15 00:00:00 │ FL    │ ORLANDO SANFORD IN…│ APPROACH     │
 SPIRIT AIRLINES    │ A-319        │ 05/10/15 00:00:00 │ IL    │ CHICAGO O'HARE INT…│ CLIMB        │
1› faa-wildlife-strikes|                                              l   go-right      73448 rows 
</pre>




## How to move faster

You can use these keystrokes to move more than one column or row at a time:

  Keystroke(s)                                                                         Moves cursor \...
  ------------------------------------------------------------------------------------ -------------------------
  `gj`                                                   to last row
  `gk`                                                   to first row
  `gh`                                                   to leftmost column
  `gl`                                                   to rightmost column
  `PageDown`/`Control-F`   one page down (forward)
  `PageUp`/`Control-B`     one page up (backward)

:::: note
::: title
Note

**What\'s the deal with \"g\"?**

As you learn to use VisiData, you\'ll notice that many commands can be prefixed with `g`. In general, prefixing a command with `g` applies it more broadly. (You can think of `g` as shorthand for \"global.\")

Hence the above: `h` navigates one column to the left, while `gh` moves *all the way* to the left.


## How to move via searching

In VisiData you can hop between columns using [regular expressions](http://2017.compciv.org/guide/topics/regular-expressions/regex-early-overview.html). (If you\'re not familiar with regular expressions, don\'t worry; for the purposes here, you can just think of them as \"search terms.\")

:::: note
::: title
Note

Searches in VisiData are, by default, *case-insensitive*. You can change this in [VisiData\'s options](../../advanced/configuring-visidata) by setting the `regex_flags` value to an empty string (instead of the default `I`).

To **find a row**, type these commands, followed by `Enter`:

  Keystroke(s)                                   Action
  ---------------------------------------------- -------------------------------------
  `/` + *regex*    Search forward in *current* column
  `?` + *regex*    Search backward in *current* column
  `g/` + *regex*   Search forward in *all* columns
  `g?` + *regex*   Search backward in *all* columns

Some VisiData commands, like the ones directly above, will prompt you to enter some text.

To demonstrate, move to the first column of the FAA dataset (if you\'re not already there) and type `/`. At the bottom-left of the screen, you\'ll see a prompt that says `search regex:`:


<pre>
search regex:                                                       /   search-col      73448 rows 
</pre>


Then, type `united`:


<pre>
search regex: united                                                /   search-col      73448 rows 
</pre>


Then, press `Enter`. Your cursor should now be at the first row matching \"united\":


<pre>
  File  Edit  View  Column  Row  Data  Plot  System  Help     | VisiData 3.0.2 | Alt+H for help men
 OPERATOR           │ ATYPE        │ INCIDENT_DATE     │ STATE │ AIRPORT            │ PHASE_OF_FLT>
 AIR WISCONSIN AIRL…│ CRJ100/200   │ 05/09/15 00:00:00 │ NC    │ PIEDMONT TRIAD INTL│ APPROACH     │
 SKYWEST AIRLINES   │ CRJ100/200   │ 05/11/15 00:00:00 │ TX    │ GEORGE BUSH INTERC…│ APPROACH     │
 HORIZON AIR        │ DHC8 DASH 8  │ 05/10/15 00:00:00 │ OR    │ PORTLAND INTL (OR) │ Climb        │
 EXPRESSJET AIRLINES│ CRJ100/200   │ 05/11/15 00:00:00 │ TN    │ TRI-CITIES REGIONA…│ LANDING ROLL │
 UPS AIRLINES       │ MD-11        │ 05/12/15 00:00:00 │ CO    │ DENVER INTL AIRPORT│ LANDING ROLL │
 BUSINESS           │ BE-200 KING  │ 05/12/15 00:00:00 │ TX    │ VALLEY INTL        │ LANDING ROLL │
 DELTA AIR LINES    │ MD-90-30     │ 05/12/15 00:00:00 │ VA    │ RICHMOND INTL      │ TAKE-OFF RUN │
 ALASKA AIRLINES    │ B-737        │ 05/12/15 00:00:00 │ FL    │ TAMPA INTL         │ APPROACH     │
 AMERIFLIGHT        │ BE-99        │ 05/13/15 00:00:00 │ OR    │ SOUTHWEST OREGON R…│ APPROACH     │
 ENVOY AIR          │ EMB-145      │ 05/14/15 00:00:00 │ TN    │ LOVELL FIELD ARPT  │ LANDING ROLL │
 REPUBLIC AIRLINES  │ EMB-170      │ 05/14/15 00:00:00 │ SC    │ CHARLESTON AFB/INT…│ DEPARTURE    │
 HORIZON AIR        │ DHC8 DASH 8  │ 05/14/15 00:00:00 │ AK    │ FAIRBANKS INTL ARPT│ DEPARTURE    │
 SPIRIT AIRLINES    │ A-319        │ 05/14/15 00:00:00 │ TX    │ GEORGE BUSH INTERC…│ LANDING ROLL │
 SHUTTLE AMERICA    │ EMB-170      │ 05/12/15 00:00:00 │ ME    │ PORTLAND INTL JETP…│ CLIMB        │
 AMERICAN AIRLINES  │ MD-83        │ 05/14/15 00:00:00 │ CA    │ LOS ANGELES INTL   │ CLIMB        │
 BUSINESS           │ DHC8 DASH 8  │ 05/13/15 00:00:00 │ VA    │ ROANOKE REGNL ARPT…│ APPROACH     │
 BUSINESS           │ C-172        │ 05/15/15 00:00:00 │ GA    │ DEKALB-PEACHTREE A…│ DEPARTURE    │
 PIEDMONT AIRLINES  │ DHC8 DASH 8  │ 05/16/15 00:00:00 │ VA    │ CHARLOTTESVILLE-AL…│ DEPARTURE    │
 MESA AIRLINES      │ CRJ700       │ 05/16/15 00:00:00 │ DC    │ WASHINGTON DULLES …│ DEPARTURE    │
 BUSINESS           │ C-340        │ 05/18/15 00:00:00 │ FL    │ VERO BEACH MUNICIP…│ DEPARTURE    │
 UNITED AIRLINES    │ B-737        │ 05/18/15 00:00:00 │ WA    │ SEATTLE-TACOMA INTL│ APPROACH     │
1› faa-wildlife-strikes|                                            /   search-col      73448 rows 
</pre>


Once you\'ve executed a search, you can **cycle through all the matching rows**:

  Keystroke(s)                        Action
  ----------------------------------- -------------------------------
  `n`   Move to next matching row
  `N`   Move to previous matching row

You can also jump between **columns**:

  Keystroke(s)                                  Action
  --------------------------------------------- ----------------------------------
  `c` + *regex*   Jump to the next matching column



## How to move to a specific row/column number

To jump to the *nth* row or column, you can use these commands:

  Keystroke(s)                               Action
  ------------------------------------------ ---------------------------
  `zr` + *n*   Jump to row number *n*
  `zc` + *n*   Jump to column number *n*


## How to move with your mouse

In addition to using your keyboard, you can use your mouse or trackpad to navigate between rows:

- **Click** a row to move the VisiData cursor to it
- **Scroll** to scroll through the rows

:::: tip
::: title
Tip

Feeling lost in a sheet? Press `Control-g` to display your cursor\'s row and column number at the bottom of VisiData\'s interface.



## How to open a file

The easiest way to open a dataset in VisiData is to specify it directly when invoking `vd`, like so:

    vd faa-wildlife-strikes.csv

If you\'ve downloaded the `faa-wildlife-strikes.csv <../../datasets/faa-wildlife-strikes.csv>` file, and you run the command above, you should see this:


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


Let\'s break it down:

- **Top row** (directly below the menu): This displays your dataset\'s columns --- at least as many as can fit on your screen.
- **Sidebar** (the green box): This contains status messages based on what you have just done or usage guidance for multi-step commands.
- **Bottom row**: This tells you what dataset you\'re viewing (`faa-wildlife-strikes` on the far left), often some status information, the number of rows loaded (73,448).
- **Highlighted column and row**: These indicate your current position in the dataset.

:::: note
::: title
Note

Depending on the width and height of your terminal, you\'ll see more/fewer columns and rows.


## How to close a file

If you\'ve just opened a single file, you can close it by typing `q`.

If you\'ve opened a collection of files --- more on that later --- you can close them all at once by typing `gq`.



## How to specify the file\'s format

VisiData guesses which kind of file you\'re trying to open based on the file\'s extension. For instance, it will try to open `my-csv-data.xlsx` as an Excel file. To override that default, specify the filetype with the `--filetype` flag. For instance:

    vd my-csv-data.xlsx --filetype csv

You can also use the shorter `-f` flag:

    vd my-csv-data.xlsx -f csv


## Compatible filetypes

VisiData can open [a range of filetypes](https://www.visidata.org/formats/), including:

### Tabular data

- CSV files, and any other delimiter-separated formats
- Excel spreadsheets (requires `pip3 install xlrd openpyxl`)
- Fixed-width files
- SQLite databases
- Postgres databases (requires `pip3 install psycopg2`)
- MySQL databases (requires `pip3 install mysqlclient`)
- HDF5 files (requires `pip3 install h5py`)
- .sas7bdat files (requires `pip3 install sas7bdat`)
- .xpt files (requires `pip3 install xport`)
- .sav files (requires `pip3 install savReaderWriter`)
- .dta files (requires `pip3 install pandas`)

### Nested Data

- JSON / JSONL
- XML (requires `pip3 install lxml`)
- YAML (requires `pip3 install PyYAML`)

### Geospatial data

- Shapefiles (requires `pip3 install pyshp`)
- MBTiles (requires `pip3 install mapbox-vector-tile`)

### Directories

- Standard Unix directories
- ZIP files
- [Frictionless Data Packages](https://frictionlessdata.io/data-package/#the-data-package-suite-of-specifications) (requires `pip3 install datapackage`)

### Misc.

- HTML (looks for `<table>` tags; requires `pip3 install lxml`)
- Website URLs (downloads the HTML, and then looks for `<table>` tags; requires `pip3 install lxml`)
- [.rec files](https://www.gnu.org/software/recutils/)
- .pcap files (requires `pip3 install dpkt dnslib`)
- \... [and more](https://www.visidata.org/formats/)


