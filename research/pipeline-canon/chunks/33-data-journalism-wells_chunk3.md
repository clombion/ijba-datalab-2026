<!-- chunk: 3/4 | source: 33-data-journalism-wells.md | words: 37691 -->
<!-- headings: Filters and selections {number="9"}; 9.1 Combining filters {number="9.1"}; Data Cleaning Part I: Data smells {number="10"}; 10.1 Wrong Type {number="10.1"}; Remove scientific notation; Load the tidyverse; Load the data; 10.2 Missing Data {number="10.2"}; 10.3 Gaps in data {number="10.3"}; 10.4 Supicious Outliers {number="10.4"}; Data Cleaning Part II: Janitor {number="11"}; 11.1 Cleaning headers {number="11.1"}; cleaning function; display the cleaned dataset; cleaning function; display the cleaned dataset; 11.2 Changing data types {number="11.2"}; cleaning function; display the cleaned dataset; cleaning function -->

#  Filters and selections {number="9"}

More often than not, we have more data than we want. Sometimes we need to be rid of that data. In `dplyr`, there's two ways to go about this: filtering and selecting.

**Filtering creates a subset of the data based on criteria**. All records where the amount is greater than 150,000. All records that match "College Park." Something like that. **Filtering works with rows -- when we filter, we get fewer rows back than we start with.**

**Selecting simply returns only the fields named**. So if you only want to see city and amount, you select those fields. When you look at your data again, you'll have two columns. If you try to use one of your columns that you had before you used select, you'll get an error. **Selecting works with columns. You will have the same number of records when you are done, but fewer columns of data to work with.**

Now we'll import a dataset of PPP applications from Maryland that is in the data folder in this chapter's pre-lab directory. It has loan applications from all over the state, so one way to filter is to isolate on "county" - Maryland has both counties and Baltimore City as jurisdictions. Let's start by loading tidyverse and reading in the Maryland data:

``` 
library(tidyverse)
```

``` 
maryland_ppp <- read_csv('data/ppp_applications_md.csv')
```

    ## 
    ## ── Column specification ────────────────────────────────────────────────────────
    ## cols(
    ##   .default = col_character(),
    ##   id = col_double(),
    ##   amount = col_double(),
    ##   naics_code = col_double(),
    ##   non_profit = col_logical(),
    ##   jobs_retained = col_double(),
    ##   date_approved = col_datetime(format = ""),
    ##   loan_number = col_double(),
    ##   sba_office_code = col_double(),
    ##   term = col_double(),
    ##   sba_guaranty_percentage = col_double(),
    ##   initial_approval_amount = col_double(),
    ##   current_approval_amount = col_double(),
    ##   undisbursed_amount = col_double(),
    ##   servicing_lender_location_id = col_double(),
    ##   utilities_proceed = col_double(),
    ##   payroll_proceed = col_double(),
    ##   mortgage_interest_proceed = col_double(),
    ##   rent_proceed = col_double(),
    ##   refinance_eidl_proceed = col_double(),
    ##   health_care_proceed = col_double()
    ##   # ... with 5 more columns
    ## )
    ## ℹ Use `spec()` for the full column specifications.

The data we want to filter on is in `project_county_name`. So we're going to use filter and something called a comparison operator. We need to filter all records equal to "PRINCE GEORGES." The comparison operators in R, like most programming languages, are == for equal to, != for not equal to, \> for greater than, \>= for greater than or equal to and so on.

**Be careful: `=` is not `==` and `=` is not "equal to." `=` is an assignment operator in most languages -- how things get named.**

``` 
prince_georges <- maryland_ppp %>% filter(project_county_name == "PRINCE GEORGES")

head(prince_georges)
```

    ## # A tibble: 6 x 55
    ##        id name   amount state address city  zip   naics_code business_type race 
    ##     <dbl> <chr>   <dbl> <chr> <chr>   <chr> <chr>      <dbl> <chr>         <chr>
    ## 1  9.38e7 PARTN… 1.09e6 MD    4857 W… Lanh… 2070…     238210 Corporation   Unan…
    ## 2  9.38e7 VILLA… 4.70e5 MD    8601 A… Capi… 2074…     611110 Limited  Lia… Unan…
    ## 3  9.38e7 GOSHE… 3.46e5 MD    4310 P… Bren… 2072…     721199 Limited  Lia… Blac…
    ## 4  9.38e7 AMERI… 1.62e5 MD    1522 P… Bowie 2071…     238990 Corporation   Blac…
    ## 5  9.94e7 BAYOU… 1.41e5 MD    5151 I… OXON… 2074…     722511 Corporation   Unan…
    ## 6  9.94e7 UNION… 1.28e5 MD    6810 F… Bran… 20613     813110 Non-Profit O… Unan…
    ## # … with 45 more variables: gender <chr>, veteran <chr>, non_profit <lgl>,
    ## #   jobs_retained <dbl>, date_approved <dttm>, lender <chr>,
    ## #   congressional_district <chr>, loan_number <dbl>, sba_office_code <dbl>,
    ## #   processing_method <chr>, loan_status <chr>, term <dbl>,
    ## #   sba_guaranty_percentage <dbl>, initial_approval_amount <dbl>,
    ## #   current_approval_amount <dbl>, undisbursed_amount <dbl>,
    ## #   franchise_name <chr>, servicing_lender_location_id <dbl>,
    ## #   servicing_lender_name <chr>, servicing_lender_address <chr>,
    ## #   servicing_lender_city <chr>, servicing_lender_state <chr>,
    ## #   servicing_lender_zip <chr>, rural_urban_indicator <chr>,
    ## #   hubzone_indicator <chr>, business_age_description <chr>,
    ## #   project_city <chr>, project_county_name <chr>, project_state <chr>,
    ## #   project_zip <chr>, utilities_proceed <dbl>, payroll_proceed <dbl>,
    ## #   mortgage_interest_proceed <dbl>, rent_proceed <dbl>,
    ## #   refinance_eidl_proceed <dbl>, health_care_proceed <dbl>,
    ## #   debt_interest_proceed <dbl>, originating_lender_city <chr>,
    ## #   originating_lender_state <chr>, loan_status_date <date>,
    ## #   originating_lender_location_id <dbl>, lmi_indicator <chr>, ethnicity <chr>,
    ## #   forgiveness_amount <dbl>, forgiveness_date <date>

And just like that, we have just Prince Georges, which we can verify looking at the head, the first six rows.

We also have more data than we might want. For example, we may only want to work with the name, address, city, zip code and amount of Prince George's applicants.

To simplify our dataset, we can use select.

``` 
selected_prince_georges <- prince_georges %>% select(name, address, city, zip, amount)

head(selected_prince_georges)
```

    ## # A tibble: 6 x 5
    ##   name                     address                 city          zip      amount
    ##   <chr>                    <chr>                   <chr>         <chr>     <dbl>
    ## 1 PARTNERS ELECTRIC SERVI… 4857 Walden Ln          Lanham        20706-4… 1.09e6
    ## 2 VILLAGE ACADEMY OF MARY… 8601 Ashwood Dr         Capitol Heig… 20743-3… 4.70e5
    ## 3 GOSHEN HOUSE TRADING LLC 4310 Pennwood Rd        Brentwood     20722-1… 3.46e5
    ## 4 AMERICAN CABLING COMPANY 1522 Pointer Ridge Pl … Bowie         20716-1… 1.62e5
    ## 5 BAYOU II, INC            5151 INDIAN HEAD HWY    OXON HILL     20745-2… 1.41e5
    ## 6 UNION BETHEL AME CHURCH  6810 Floral Park Road   Brandywine    20613    1.28e5

And now we only have five columns of data for whatever analysis we might want to do.

## 9.1 Combining filters {number="9.1"}

So let's say we wanted to know how many Prince George's applications were from non-profit organizations and applied for more than \$150,000. We can do this a number of ways. The first is we can chain together a whole lot of filters.

``` 
large_prince_georges_nonprofit <- maryland_ppp %>% filter(project_county_name == "PRINCE GEORGES") %>% filter(business_type == "Non-Profit Organization") %>% filter(amount > 150000)

nrow(large_prince_georges_nonprofit)
```

    ## [1] 145

That gives us 145 applicants. But that's silly and repetitive, no? We can do better using boolean operators -- AND and OR. In this case, AND is `&` and OR is `|`.

The difference? With AND, all three things must be true to be included. With OR, any of those three things can be true and it will be included. A Prince George's corporation will get included because it applied for more than \$150k. One of the conditions is true.

Here's the difference.

``` 
and_prince_georges <- maryland_ppp %>% filter(project_county_name == "PRINCE GEORGES" & business_type == "Non-Profit Organization" & amount > 150000)

nrow(and_prince_georges)
```

    ## [1] 145

So AND gives us the same answer we got before. What does OR give us?

``` 
or_prince_georges <- maryland_ppp %>% filter(project_county_name == "PRINCE GEORGES" | business_type == "Non-Profit Organization" | amount > 150000)

nrow(or_prince_georges)
```

    ## [1] 54321

So there's 54,321 applications from Maryland applicants who are EITHER in Prince George's OR a non-profit organization OR applied for more than \$150,000. Or is inclusive; AND is exclusive.

A general tip about using filter: it's easier to work your way towards the filter syntax you need rather than try and write it once and trust the result. Each time you modify your filter, check the results to see if they make sense. This adds a little time to your process but you'll thank yourself for doing it because it helps avoid mistakes.

`<!--chapter:end:08-filters.Rmd-->`{=html}


#  Data Cleaning Part I: Data smells {number="10"}

Any time you are given a dataset from anyone, you should immediately be suspicious. Is this data what I think it is? Does it include what I expect? Is there anything I need to know about it? Will it produce the information I expect?

One of the first things you should do is give it the smell test.

Failure to give data the smell test [can lead you to miss stories and get your butt kicked on a competitive story](https://source.opennews.org/en-US/learning/handling-data-about-race-and-ethnicity/).

With data smells, we're trying to find common mistakes in data. [For more on data smells, read the GitHub wiki post that started it all](https://github.com/nikeiubel/data-smells/wiki/Ensuring-Accuracy-in-Data-Journalism). Some common data smells are:

- Missing data or missing values
- Gaps in data
- Wrong type of data
- Outliers
- Sharp curves
- Conflicting information within a dataset
- Conflicting information across datasets
- Wrongly derived data
- Internal inconsistency
- External inconsistency
- Wrong spatial data
- Unusable data, including non-standard abbreviations, ambiguous data, extraneous data, inconsistent data

Not all of these data smells are detectable in code. You may have to ask people about the data. You may have to compare it to another dataset yourself. Does the agency that uses the data produce reports from the data? Does your analysis match those reports? That will expose wrongly derived data, or wrong units, or mistakes you made with inclusion or exclusion.

But with several of these data smells, we can do them first, before we do anything else.

We're going to examine three here as they apply to the PPP loan data we've been working with: wrong type, missing data and gaps in data.

## 10.1 Wrong Type {number="10.1"}

First, let's look at **Wrong Type Of Data**.

We can sniff that out by looking at the output of `readr`.

Let's load the tidyverse.

``` 

# Remove scientific notation
options(scipen=999)
# Load the tidyverse
library(tidyverse)
```

Then let's load the Maryland slice of PPP loan data we've used previously.

This time, we're going to load the data in a CSV format, which stands for comma separated values and is essentially a fancy structured text file. Each column in the csv is separated -- "delimited" -- by a comma from the next column. The file has a ".gz" extension on the end because it's zipped up to keep the file sizes smaller.

We're also going to introduce a new argument to our function that reads in the data, read_csv(), called "guess_max." As R reads in the csv file, it will attempt to make some calls on what "data type" to assign to each field: number, character, date, and so on. The "guess_max" argument says: look at the values in the whatever number of rows we specify before deciding which data type to assign. In this case, we'll pick 10.

``` 

# Load the data
ppp_maryland_loans <- read_csv("data/ppp_loan_data/processed/md/ppp_loans_md.csv.zip", guess_max=10)
```

    ## 
    ## ── Column specification ────────────────────────────────────────────────────────
    ## cols(
    ##   .default = col_character(),
    ##   id = col_double(),
    ##   amount = col_double(),
    ##   naics_code = col_double(),
    ##   non_profit = col_logical(),
    ##   jobs_retained = col_double(),
    ##   date_approved = col_date(format = ""),
    ##   loan_range_sort_key = col_logical(),
    ##   previous_loan_range = col_logical(),
    ##   previous_name = col_logical(),
    ##   loan_number = col_double(),
    ##   sba_office_code = col_double(),
    ##   term = col_double(),
    ##   sba_guaranty_percentage = col_double(),
    ##   initial_approval_amount = col_double(),
    ##   current_approval_amount = col_double(),
    ##   undisbursed_amount = col_double(),
    ##   franchise_name = col_logical(),
    ##   servicing_lender_location_id = col_double(),
    ##   utilities_proceed = col_double(),
    ##   payroll_proceed = col_double()
    ##   # ... with 13 more columns
    ## )
    ## ℹ Use `spec()` for the full column specifications.

    ## Warning: 15708 parsing failures.
    ## row            col           expected                                                          actual                                                   file
    ##  21 franchise_name 1/0/T/F/TRUE/FALSE ZIPS Dry Cleaners                                               'data/ppp_loan_data/processed/md/ppp_loans_md.csv.zip'
    ## 126 franchise_name 1/0/T/F/TRUE/FALSE Quiznos                                                         'data/ppp_loan_data/processed/md/ppp_loans_md.csv.zip'
    ## 375 franchise_name 1/0/T/F/TRUE/FALSE Nissan North America, Inc. - Dealer Sales and Service Agreement 'data/ppp_loan_data/processed/md/ppp_loans_md.csv.zip'
    ## 400 franchise_name 1/0/T/F/TRUE/FALSE Hampton Inn & Suites                                            'data/ppp_loan_data/processed/md/ppp_loans_md.csv.zip'
    ## 405 franchise_name 1/0/T/F/TRUE/FALSE Express Employment Professional                                 'data/ppp_loan_data/processed/md/ppp_loans_md.csv.zip'
    ## ... .............. .................. ............................................................... ......................................................
    ## See problems(...) for more details.

Pay attention to the red warning that signals "one or more parsing issues." It advises us to run the problems() function to see what went wrong. Let's do that.

``` 
problems(ppp_maryland_loans)
```

    ## # A tibble: 15,708 x 5
    ##      row col       expected    actual                     file                  
    ##    <int> <chr>     <chr>       <chr>                      <chr>                 
    ##  1    21 franchis… 1/0/T/F/TR… ZIPS Dry Cleaners          'data/ppp_loan_data/p…
    ##  2   126 franchis… 1/0/T/F/TR… Quiznos                    'data/ppp_loan_data/p…
    ##  3   375 franchis… 1/0/T/F/TR… Nissan North America, Inc… 'data/ppp_loan_data/p…
    ##  4   400 franchis… 1/0/T/F/TR… Hampton Inn & Suites       'data/ppp_loan_data/p…
    ##  5   405 franchis… 1/0/T/F/TR… Express Employment Profes… 'data/ppp_loan_data/p…
    ##  6   417 franchis… 1/0/T/F/TR… Mason's Lobster            'data/ppp_loan_data/p…
    ##  7   480 franchis… 1/0/T/F/TR… Smoothie King              'data/ppp_loan_data/p…
    ##  8   510 franchis… 1/0/T/F/TR… Restore Hyper Wellness + … 'data/ppp_loan_data/p…
    ##  9   554 franchis… 1/0/T/F/TR… Quiznos                    'data/ppp_loan_data/p…
    ## 10   652 franchis… 1/0/T/F/TR… Structural Elements        'data/ppp_loan_data/p…
    ## # … with 15,698 more rows

It produces a table of all the parsing problems. It has 15,708 rows, which means we have that many problems. In almost every case here, the `readr` library has guessed that a given column was of a "logical" data type -- True or False. It did it based on very limited information -- only 1,000 rows. So, when it hit a value that looked like a date, or a character string, it didn't know what to do. So it just didn't read in that value correctly.

The easy way to fix this is to set the guess_max argument higher. It will take a little longer to load, but we'll use every single row in the data set to guess the column type -- 195,865

``` 
ppp_maryland_loans <- read_csv("data/ppp_loan_data/processed/md/ppp_loans_md.csv.zip", guess_max=195865)
```

    ## 
    ## ── Column specification ────────────────────────────────────────────────────────
    ## cols(
    ##   .default = col_character(),
    ##   id = col_double(),
    ##   amount = col_double(),
    ##   naics_code = col_double(),
    ##   non_profit = col_logical(),
    ##   jobs_retained = col_double(),
    ##   date_approved = col_date(format = ""),
    ##   loan_range_sort_key = col_logical(),
    ##   previous_loan_range = col_logical(),
    ##   previous_name = col_logical(),
    ##   loan_number = col_double(),
    ##   sba_office_code = col_double(),
    ##   term = col_double(),
    ##   sba_guaranty_percentage = col_double(),
    ##   initial_approval_amount = col_double(),
    ##   current_approval_amount = col_double(),
    ##   undisbursed_amount = col_double(),
    ##   servicing_lender_location_id = col_double(),
    ##   utilities_proceed = col_double(),
    ##   payroll_proceed = col_double(),
    ##   mortgage_interest_proceed = col_double()
    ##   # ... with 11 more columns
    ## )
    ## ℹ Use `spec()` for the full column specifications.

This time, we got no parsing failures. And if we examine the data types `readr` assigned to each column using glimpse(), they generally make sense.

``` 
glimpse(ppp_maryland_loans)
```

    ## Rows: 195,865
    ## Columns: 63
    ## $ id                             <dbl> 99443772, 99444241, 99445051, 99445208,…
    ## $ name                           <chr> "TARBIYAH ACADEMY INC", "J &AMP; M DRYW…
    ## $ slug                           <chr> "tarbiyah-academy-inc-8387378410", "j-a…
    ## $ amount                         <dbl> 149000.0, 146000.0, 140400.0, 139527.0,…
    ## $ state                          <chr> "MD", "MD", "MD", "MD", "MD", "MD", "MD…
    ## $ address                        <chr> "6785 Business Pkwy Ste 108", "10413 Fo…
    ## $ city                           <chr> "Elkridge", "Union Bridge", "PHOENIX", …
    ## $ zip                            <chr> "21075-6353", "21791", "21131-2229", "2…
    ## $ naics_code                     <dbl> 611110, 238310, 623110, 311920, 561730,…
    ## $ business_type                  <chr> "Corporation", "Subchapter S Corporatio…
    ## $ race                           <chr> "Asian", "Unanswered", "Unanswered", "U…
    ## $ gender                         <chr> "Male Owned", "Unanswered", "Unanswered…
    ## $ veteran                        <chr> "Non-Veteran", "Unanswered", "Unanswere…
    ## $ non_profit                     <lgl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA,…
    ## $ jobs_retained                  <dbl> 25, 6, 18, 23, 15, 25, 14, 11, 24, 5, 1…
    ## $ date_approved                  <date> 2021-02-13, 2020-05-01, 2020-04-28, 20…
    ## $ lender                         <chr> "Bank of America, National Association"…
    ## $ congressional_district         <chr> "MD-02", "MD-08", "MD-01", "MD-08", "MD…
    ## $ loan_range_sort_key            <lgl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA,…
    ## $ previous_loan_range            <lgl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA,…
    ## $ previous_name                  <lgl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA,…
    ## $ loan_number                    <dbl> 8387378410, 7763877705, 1414477305, 806…
    ## $ sba_office_code                <dbl> 373, 373, 373, 353, 373, 373, 373, 373,…
    ## $ processing_method              <chr> "PPS", "PPP", "PPP", "PPP", "PPS", "PPP…
    ## $ loan_status                    <chr> "Exemption 4", "Exemption 4", "Paid in …
    ## $ term                           <dbl> 60, 24, 24, 24, 24, 24, 60, 60, 24, 60,…
    ## $ sba_guaranty_percentage        <dbl> 100, 100, 100, 100, 100, 100, 100, 100,…
    ## $ initial_approval_amount        <dbl> 149000.0, 146000.0, 140400.0, 139527.0,…
    ## $ current_approval_amount        <dbl> 149000.0, 146000.0, 140400.0, 139527.0,…
    ## $ undisbursed_amount             <dbl> 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, …
    ## $ franchise_name                 <chr> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA,…
    ## $ servicing_lender_location_id   <dbl> 9551, 44449, 124055, 46391, 434059, 304…
    ## $ servicing_lender_name          <chr> "Bank of America, National Association"…
    ## $ servicing_lender_address       <chr> "100 N Tryon St, Ste 170", "222 Delawar…
    ## $ servicing_lender_city          <chr> "CHARLOTTE", "WILMINGTON", "ROCKVILLE",…
    ## $ servicing_lender_state         <chr> "NC", "DE", "MD", "NY", "VA", "MD", "NY…
    ## $ servicing_lender_zip           <chr> "28202-4024", "19801-1621", "20850-6238…
    ## $ rural_urban_indicator          <chr> "U", "U", "U", "U", "R", "R", "R", "U",…
    ## $ hubzone_indicator              <chr> "N", "N", "N", "N", "N", "Y", "Y", "N",…
    ## $ business_age_description       <chr> "Existing or more than 2 years old", "U…
    ## $ project_city                   <chr> "Elkridge", "Union Bridge", "PHOENIX", …
    ## $ project_county_name            <chr> "HOWARD", "CARROLL", "BALTIMORE", "MONT…
    ## $ project_state                  <chr> "MD", "MD", "MD", "MD", "MD", "MD", "MD…
    ## $ project_zip                    <chr> "21075-6353", "21791-0001", "21131-2229…
    ## $ utilities_proceed              <dbl> 1, NA, NA, 3926, 1, NA, 1, NA, NA, NA, …
    ## $ payroll_proceed                <dbl> 148997.0, 146000.0, 140400.0, 88000.0, …
    ## $ mortgage_interest_proceed      <dbl> NA, NA, NA, 0, NA, NA, NA, NA, NA, NA, …
    ## $ rent_proceed                   <dbl> NA, NA, NA, 42062, NA, NA, NA, NA, NA, …
    ## $ refinance_eidl_proceed         <dbl> NA, NA, NA, 0, NA, NA, NA, NA, NA, NA, …
    ## $ health_care_proceed            <dbl> NA, NA, NA, 5539, NA, NA, NA, NA, NA, N…
    ## $ debt_interest_proceed          <dbl> NA, NA, NA, 0, NA, NA, NA, NA, NA, NA, …
    ## $ originating_lender_city        <chr> "CHARLOTTE", "WILMINGTON", "ROCKVILLE",…
    ## $ originating_lender_state       <chr> "NC", "DE", "MD", "NY", "VA", "MD", "VA…
    ## $ loan_status_date               <date> NA, NA, 2021-05-12, 2021-01-22, NA, 20…
    ## $ originating_lender_location_id <dbl> 9551, 44449, 124055, 46391, 434059, 304…
    ## $ old_slug                       <chr> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA,…
    ## $ lmi_indicator                  <chr> "N", "Y", "N", "Y", "N", "Y", "N", "N",…
    ## $ unmatched_original             <lgl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA,…
    ## $ unmatched_updated              <lgl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA,…
    ## $ previous_jobs_reported         <lgl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA,…
    ## $ ethnicity                      <chr> "Not Hispanic or Latino", "Unknown/NotS…
    ## $ forgiveness_amount             <dbl> NA, NA, 141554.40, 140486.49, NA, 13427…
    ## $ forgiveness_date               <date> NA, NA, 2021-02-25, 2020-12-30, NA, 20…

Things that should be characters -- like state, city, name -- are characters (chr). Things that should be numbers (dbl) -- like amount -- are numbers. Date columns -- like date_approved -- are stored as dates.

There are some minor problem. The id column is a good example. It read in as a number (dbl), which makes sense, because it really is just a string of numbers. But we'd never need to do math on these values; it wouldn't make sense to add two ids together, for example. So it is probably best stored as a character. The opposite would be more problematic. If something that should be stored as a number we want to do math on was stored as a character, we couldn't actually use it to do math.

We can fix that pretty easily, by overwriting the column while changing the data type, using mutate()

``` 
ppp_maryland_loans <- ppp_maryland_loans %>%
  mutate(id = as.character(id))
```

When we glimpse() the dataframe again, it's been changed

``` 
glimpse(ppp_maryland_loans)
```

    ## Rows: 195,865
    ## Columns: 63
    ## $ id                             <chr> "99443772", "99444241", "99445051", "99…
    ## $ name                           <chr> "TARBIYAH ACADEMY INC", "J &AMP; M DRYW…
    ## $ slug                           <chr> "tarbiyah-academy-inc-8387378410", "j-a…
    ## $ amount                         <dbl> 149000.0, 146000.0, 140400.0, 139527.0,…
    ## $ state                          <chr> "MD", "MD", "MD", "MD", "MD", "MD", "MD…
    ## $ address                        <chr> "6785 Business Pkwy Ste 108", "10413 Fo…
    ## $ city                           <chr> "Elkridge", "Union Bridge", "PHOENIX", …
    ## $ zip                            <chr> "21075-6353", "21791", "21131-2229", "2…
    ## $ naics_code                     <dbl> 611110, 238310, 623110, 311920, 561730,…
    ## $ business_type                  <chr> "Corporation", "Subchapter S Corporatio…
    ## $ race                           <chr> "Asian", "Unanswered", "Unanswered", "U…
    ## $ gender                         <chr> "Male Owned", "Unanswered", "Unanswered…
    ## $ veteran                        <chr> "Non-Veteran", "Unanswered", "Unanswere…
    ## $ non_profit                     <lgl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA,…
    ## $ jobs_retained                  <dbl> 25, 6, 18, 23, 15, 25, 14, 11, 24, 5, 1…
    ## $ date_approved                  <date> 2021-02-13, 2020-05-01, 2020-04-28, 20…
    ## $ lender                         <chr> "Bank of America, National Association"…
    ## $ congressional_district         <chr> "MD-02", "MD-08", "MD-01", "MD-08", "MD…
    ## $ loan_range_sort_key            <lgl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA,…
    ## $ previous_loan_range            <lgl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA,…
    ## $ previous_name                  <lgl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA,…
    ## $ loan_number                    <dbl> 8387378410, 7763877705, 1414477305, 806…
    ## $ sba_office_code                <dbl> 373, 373, 373, 353, 373, 373, 373, 373,…
    ## $ processing_method              <chr> "PPS", "PPP", "PPP", "PPP", "PPS", "PPP…
    ## $ loan_status                    <chr> "Exemption 4", "Exemption 4", "Paid in …
    ## $ term                           <dbl> 60, 24, 24, 24, 24, 24, 60, 60, 24, 60,…
    ## $ sba_guaranty_percentage        <dbl> 100, 100, 100, 100, 100, 100, 100, 100,…
    ## $ initial_approval_amount        <dbl> 149000.0, 146000.0, 140400.0, 139527.0,…
    ## $ current_approval_amount        <dbl> 149000.0, 146000.0, 140400.0, 139527.0,…
    ## $ undisbursed_amount             <dbl> 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, …
    ## $ franchise_name                 <chr> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA,…
    ## $ servicing_lender_location_id   <dbl> 9551, 44449, 124055, 46391, 434059, 304…
    ## $ servicing_lender_name          <chr> "Bank of America, National Association"…
    ## $ servicing_lender_address       <chr> "100 N Tryon St, Ste 170", "222 Delawar…
    ## $ servicing_lender_city          <chr> "CHARLOTTE", "WILMINGTON", "ROCKVILLE",…
    ## $ servicing_lender_state         <chr> "NC", "DE", "MD", "NY", "VA", "MD", "NY…
    ## $ servicing_lender_zip           <chr> "28202-4024", "19801-1621", "20850-6238…
    ## $ rural_urban_indicator          <chr> "U", "U", "U", "U", "R", "R", "R", "U",…
    ## $ hubzone_indicator              <chr> "N", "N", "N", "N", "N", "Y", "Y", "N",…
    ## $ business_age_description       <chr> "Existing or more than 2 years old", "U…
    ## $ project_city                   <chr> "Elkridge", "Union Bridge", "PHOENIX", …
    ## $ project_county_name            <chr> "HOWARD", "CARROLL", "BALTIMORE", "MONT…
    ## $ project_state                  <chr> "MD", "MD", "MD", "MD", "MD", "MD", "MD…
    ## $ project_zip                    <chr> "21075-6353", "21791-0001", "21131-2229…
    ## $ utilities_proceed              <dbl> 1, NA, NA, 3926, 1, NA, 1, NA, NA, NA, …
    ## $ payroll_proceed                <dbl> 148997.0, 146000.0, 140400.0, 88000.0, …
    ## $ mortgage_interest_proceed      <dbl> NA, NA, NA, 0, NA, NA, NA, NA, NA, NA, …
    ## $ rent_proceed                   <dbl> NA, NA, NA, 42062, NA, NA, NA, NA, NA, …
    ## $ refinance_eidl_proceed         <dbl> NA, NA, NA, 0, NA, NA, NA, NA, NA, NA, …
    ## $ health_care_proceed            <dbl> NA, NA, NA, 5539, NA, NA, NA, NA, NA, N…
    ## $ debt_interest_proceed          <dbl> NA, NA, NA, 0, NA, NA, NA, NA, NA, NA, …
    ## $ originating_lender_city        <chr> "CHARLOTTE", "WILMINGTON", "ROCKVILLE",…
    ## $ originating_lender_state       <chr> "NC", "DE", "MD", "NY", "VA", "MD", "VA…
    ## $ loan_status_date               <date> NA, NA, 2021-05-12, 2021-01-22, NA, 20…
    ## $ originating_lender_location_id <dbl> 9551, 44449, 124055, 46391, 434059, 304…
    ## $ old_slug                       <chr> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA,…
    ## $ lmi_indicator                  <chr> "N", "Y", "N", "Y", "N", "Y", "N", "N",…
    ## $ unmatched_original             <lgl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA,…
    ## $ unmatched_updated              <lgl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA,…
    ## $ previous_jobs_reported         <lgl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA,…
    ## $ ethnicity                      <chr> "Not Hispanic or Latino", "Unknown/NotS…
    ## $ forgiveness_amount             <dbl> NA, NA, 141554.40, 140486.49, NA, 13427…
    ## $ forgiveness_date               <date> NA, NA, 2021-02-25, 2020-12-30, NA, 20…

## 10.2 Missing Data {number="10.2"}

The second smell we can find in code is **missing data**.

We can do that by grouping and counting columns. In addition to identifying the presence of NA values, this method will also give us a sense of the distribution of values in those columns.

Let's start with the "franchise" column. The following code groups by the franchise name column, counts the number in each group, and then sorts from highest to lowest.

There are 192,959 NA values in this column. This makes sense. Not every business will be a franchisee of a larger company like Subway or Dunkin'. In this case, the presence of so many NAs isn't really concerning.

``` 
ppp_maryland_loans %>% 
  group_by(franchise_name) %>% 
  summarise(
    count=n()
  ) %>%
  arrange(desc(count))
```

    ## # A tibble: 582 x 2
    ##    franchise_name                                        count
    ##    <chr>                                                 <int>
    ##  1 <NA>                                                 192959
    ##  2 Subway                                                  275
    ##  3 7-Eleven, Inc - Individual Store Franchise Agreement    127
    ##  4 Dunkin' Donuts                                          109
    ##  5 IHOP                                                     53
    ##  6 Jiffy Lube                                               51
    ##  7 ZIPS Dry Cleaners                                        48
    ##  8 Holiday Inn Express (License Agreement)                  44
    ##  9 Dunkin' Donut/Baskin-Robbins Co-Brand                    42
    ## 10 Popeyes Louisiana Kitchen                                41
    ## # … with 572 more rows

Now let's try the "forgiveness_amount" column, which represents the amount of the loan that was forgiven, or not required to be paid back. In this case, there are 135,073 NA values. The rest have different dollar amounts.

``` 
ppp_maryland_loans %>% 
  group_by(forgiveness_amount) %>% 
  summarise(
    count=n()
  ) %>%
  arrange(desc(count))
```

    ## # A tibble: 58,637 x 2
    ##    forgiveness_amount  count
    ##                 <dbl>  <int>
    ##  1                NA  135073
    ##  2             20977.     15
    ##  3             21011.     14
    ##  4             21009.     13
    ##  5             21025.     11
    ##  6             21003.     10
    ##  7             21010.     10
    ##  8             20985.      9
    ##  9             20970.      8
    ## 10             20972.      8
    ## # … with 58,627 more rows

Do the 135,073 NAs represent loans that weren't forgiven?

Do they represent loans that might have been forgiven, but the data is simply missing the amount of money?

We could check the documentation, which isn't particularly helpful. It only says the column represents "forgiveness amount."

We could check the "forgiveness_date" column, to see how many NAs it has: 135,703, the same number as the number of NAs in "forgiveness_amount."

``` 
ppp_maryland_loans %>% 
  group_by(forgiveness_date) %>% 
  summarise(
    count=n()
  ) %>%
  filter(is.na(forgiveness_date)) %>%
  arrange(desc(count))
```

    ## # A tibble: 1 x 2
    ##   forgiveness_date  count
    ##   <date>            <int>
    ## 1 NA               135073

We can group by forgiveness_amount and forgiveness_date to determine whether one is NA when the other is NA. Because this grouping has 135,073 rows, too, we know this to be the case.

``` 
ppp_maryland_loans %>%
  group_by(forgiveness_amount, forgiveness_date) %>%
  summarise(
    count=n()
  ) %>%
  filter(is.na(forgiveness_date)) %>%
  arrange(desc(count))
```

    ## `summarise()` has grouped output by 'forgiveness_amount'. You can override using the `.groups` argument.

    ## # A tibble: 1 x 3
    ## # Groups:   forgiveness_amount [1]
    ##   forgiveness_amount forgiveness_date  count
    ##                <dbl> <date>            <int>
    ## 1                 NA NA               135073

Before we decide to base a publishable finding on this column, we should call the custodian of the data to confirm our hypothesis of NA values in these columns, that they represent loans that have not been forgiven.

## 10.3 Gaps in data {number="10.3"}

Let's now look at **gaps in data**. It's been my experience that gaps in data often have to do with time, so let's first look at "date_approved," so we can see if there's any missing months, or huge differences in the number of loans by month. Let's start with Date. If we're going to work with dates, we should have `lubridate` handy for `floor_date`.

``` 
library(lubridate)
```

The `floor_date` function will allow us to group by month, instead of a single day.

``` 
ppp_maryland_loans %>% 
  mutate(month_year_approved = floor_date(date_approved, "month")) %>%
  group_by(month_year_approved) %>% 
   summarise(
    count=n()
  ) %>%
  arrange(month_year_approved)
```

    ## # A tibble: 11 x 2
    ##    month_year_approved count
    ##    <date>              <int>
    ##  1 2020-04-01          45040
    ##  2 2020-05-01          27057
    ##  3 2020-06-01           7569
    ##  4 2020-07-01           4021
    ##  5 2020-08-01           1862
    ##  6 2021-01-01          14153
    ##  7 2021-02-01          19734
    ##  8 2021-03-01          23939
    ##  9 2021-04-01          31282
    ## 10 2021-05-01          21150
    ## 11 2021-06-01             58

So, our data starts in April 2020, the month that has more loans -- 45,040 -- than any other month. That makes sense, as the program launched at the start of the pandemic, in April 2020. The number of loans declines each month through August 2020, as the initial round of the program worked through the initial funding allocation.

Then, there are no loans until January 2021. Does the four-month gap in loans in this dataset represent a problem? Are we missing a bunch of records?

Probably not. The program was reauthorized a few times. For example, it expired in August 2020, before being reauthorized with new loans being given in January 2021.

It's good to be aware of all gaps in data, but they don't always represent a problem.

## 10.4 Supicious Outliers {number="10.4"}

Any time you are going to focus on a column for analysis, you should check for suspicious values. Are there any unusually large values or unusually small values? Are there any values that should not exist in the data?

Let's consider the loan amount column from our Maryland PPP data, and find the largest (max) and smallest (min) amount.

``` 
ppp_maryland_loans %>% 
  summarise(max_amount = max(amount),
            min_amount= min(amount))
```

    ## # A tibble: 1 x 2
    ##   max_amount min_amount
    ##        <dbl>      <dbl>
    ## 1   10000000          6

The largest amount is \$10 million which is the maximum size of a loan under the program. If the max amount was larger than \$10 million, that would be suspicious. Similarly, if the smallest amount was a negative number, that would also raise an eyebrow. What about \$6? That does seem a little odd. Why would someone take out a loan for that amount of money?

Let's take a look at the full record set for any loan less than \$100.

``` 
ppp_maryland_loans %>% 
 filter(amount < 100)
```

    ## # A tibble: 2 x 63
    ##   id     name   slug   amount state address city  zip   naics_code business_type
    ##   <chr>  <chr>  <chr>   <dbl> <chr> <chr>   <chr> <chr>      <dbl> <chr>        
    ## 1 99620… GETGF… getgf…      6 MD    7101 R… BALT… 2121…     453220 Limited  Lia…
    ## 2 99620… LEGAC… legac…     78 MD    4201 N… BOWIE 2071…         NA Partnership  
    ## # … with 53 more variables: race <chr>, gender <chr>, veteran <chr>,
    ## #   non_profit <lgl>, jobs_retained <dbl>, date_approved <date>, lender <chr>,
    ## #   congressional_district <chr>, loan_range_sort_key <lgl>,
    ## #   previous_loan_range <lgl>, previous_name <lgl>, loan_number <dbl>,
    ## #   sba_office_code <dbl>, processing_method <chr>, loan_status <chr>,
    ## #   term <dbl>, sba_guaranty_percentage <dbl>, initial_approval_amount <dbl>,
    ## #   current_approval_amount <dbl>, undisbursed_amount <dbl>,
    ## #   franchise_name <chr>, servicing_lender_location_id <dbl>,
    ## #   servicing_lender_name <chr>, servicing_lender_address <chr>,
    ## #   servicing_lender_city <chr>, servicing_lender_state <chr>,
    ## #   servicing_lender_zip <chr>, rural_urban_indicator <chr>,
    ## #   hubzone_indicator <chr>, business_age_description <chr>,
    ## #   project_city <chr>, project_county_name <chr>, project_state <chr>,
    ## #   project_zip <chr>, utilities_proceed <dbl>, payroll_proceed <dbl>,
    ## #   mortgage_interest_proceed <dbl>, rent_proceed <dbl>,
    ## #   refinance_eidl_proceed <dbl>, health_care_proceed <dbl>,
    ## #   debt_interest_proceed <dbl>, originating_lender_city <chr>,
    ## #   originating_lender_state <chr>, loan_status_date <date>,
    ## #   originating_lender_location_id <dbl>, old_slug <chr>, lmi_indicator <chr>,
    ## #   unmatched_original <lgl>, unmatched_updated <lgl>,
    ## #   previous_jobs_reported <lgl>, ethnicity <chr>, forgiveness_amount <dbl>,
    ## #   forgiveness_date <date>

We have two businesses, "GETGFTD LLC" and "LEGACY SPINE AND PAIN LLC" that both got very small loans of \$6 and \$78. Scan through the columns. Let's check for internal consistency. There are other columns in the data that have related information: initial_approval_amount, current_approval_amount and payroll_proceed. Let's select just those columns

``` 
ppp_maryland_loans %>% 
 filter(amount < 100) %>%
  select(name, amount, initial_approval_amount, current_approval_amount, payroll_proceed)
```

    ## # A tibble: 2 x 5
    ##   name            amount initial_approval_a… current_approval_a… payroll_proceed
    ##   <chr>            <dbl>               <dbl>               <dbl>           <dbl>
    ## 1 GETGFTD LLC          6                   6                   6               6
    ## 2 LEGACY SPINE A…     78                  78                  78              78

Those are all the same value, so at least this number is internally consistent. But is it correct? Did someone mistype it when entering the data?

A call to the bank -- Bank of America in both cases -- or the companies could help resolve this mystery. Or a call to the SBA -- the owner of the data -- to ask about small values generally may help us understand if small values like this are suspicious or not.

`<!--chapter:end:09-datasmells.Rmd-->`{=html}


#  Data Cleaning Part II: Janitor {number="11"}

The bane of every data analyst's existence is data cleaning.

Every developer, every data system, every agency, the all have opinions about how data gets collected. Some decisions make sense from the outside. Some decisions are based entirely on internal politics: who is creating the data, how they are creating it, why they are creating it. Is it automated? Is it manual? Are data normalized? Are there free form fields where users can just type into or does the system restrict them to choices?

Your journalistic questions -- what you want the data to tell you -- is almost never part of that equation.

So cleaning data is the process of fixing issues in your data so you can answer the questions you want to answer. Data cleaning is a critical step that you can't skip past. A standard metric is that 80 percent of the time working with data will be spent cleaning and verifying data, and 20 percent the more exciting parts like analysis and visualization.

The tidyverse has a lot of built-in tools for data cleaning. We're also going to make use of a new library, called `janitor` that has a bunch of great functions for cleaning data. Let's load those now.

``` 
library(tidyverse)
library(janitor)
```

    ## 
    ## Attaching package: 'janitor'

    ## The following objects are masked from 'package:stats':
    ## 
    ##     chisq.test, fisher.test

Now let's load a tiny slice of our Maryland PPP loan dataset. To make the cleaning demonstration in this chapter easier, this dataset only has six rows and seven columns. All six of these loans are from Arnold, Maryland. The full data set has more loans for Arnold, but we're only showing these six here.

``` 
arnold_md_loans <- read_rds("data/ppp_loan_data/processed/md/arnold_md_loans.rmd")
```

Let's glimpse it to get a sense of it, to examine the column data types and possible values.

``` 
glimpse(arnold_md_loans)
```

    ## Rows: 6
    ## Columns: 7
    ## $ `1_id`           <dbl> 93761495, 93761495, 93762575, 99479443, 99490480, 995…
    ## $ NAME             <chr> "STUART JONES LLC", "STUART JONES LLC", "CHAPELWOOD E…
    ## $ amount           <chr> "693361", "693361", "559000", "39700", "28422", "1933…
    ## $ `street address` <chr> "700 Mill Creek Rd", "700 Mill Creek Rd", "1511 RITCH…
    ## $ city             <chr> "Arnold", "Arnold", "ARNOLD", "Arnld", "arnold", "Ano…
    ## $ state            <chr> "MD", "MD", "MD", "MD", "MD", "MD"
    ## $ zip              <chr> "21012-1111", "21012-1111", "21012-2398", "21012", "2…

And let's examine the full data set.

``` 
arnold_md_loans
```

    ## # A tibble: 6 x 7
    ##     `1_id` NAME                   amount `street address`   city  state zip     
    ##      <dbl> <chr>                  <chr>  <chr>              <chr> <chr> <chr>   
    ## 1 93761495 STUART JONES LLC       693361 700 Mill Creek Rd  Arno… MD    21012-1…
    ## 2 93761495 STUART JONES LLC       693361 700 Mill Creek Rd  Arno… MD    21012-1…
    ## 3 93762575 CHAPELWOOD ENTERPRISE… 559000 1511 RITCHIE HWY   ARNO… MD    21012-2…
    ## 4 99479443 VINEVE LLC             39700  1506 Ritchie Hgwy  Arnld MD    21012   
    ## 5 99490480 ARNOLD CHIROPRACTIC C… 28422  1507 ritchie hwy   arno… MD    21012   
    ## 6 99535547 SPARKS ELECTRICAL SER… 19335  1238 Birchcrest C… Anold MD    21012

There are a number of issues with this data set that might get in the way of asking questions and receiving accurate answers. They are:

- The column headers are inconsistently styled (note: I've purposely dirtied these up, which is why they look different than previous versions of this data we've loaded). The first column "1_id" starts with a number. The "NAME" column is all caps, while the rest are lowercase. And "street address" has a space in it. Those problems will make them hard to analyze, to refer to in functions we write.
- The amount column is stored as a character, not a number. If we try to do math to it -- say, calculate the average loan size -- it won't work.
- There's a fully duplicated row -- a common problem in data sets. The first row is exactly the same as the second.
- The city field has five different forms -- including misspellings -- of Arnold. If we wanted to group and count the number of loans in Arnold, this inconsistency would not let us do that correctly.
- The zip field mixes five digit ZIP codes and nine digit ZIP codes. If we wanted to group and count the number of loans in a given ZIP code, this inconsistency would not let us do that correctly.
- The street address field is inconsistent. It has multiple variations of Ritchie Hwy.

Let's get cleaning. Our goal will be to build up one block of code that does all the necessary cleaning in order to answer this question: what is the total amount of loans made to businesses in Arnold, MD in ZIP code 21012?

## 11.1 Cleaning headers {number="11.1"}

One of the first places we can start with cleaning data is cleaning the column names (or headers).

Every system has their own way of recording headers, and every developer has their own thoughts of what a good idea is within it. R is most happy when headers are lower case, without special characters.

If column headers start with a number, or have a space in between two words, you have to set them off with backticks when using them in a function. Generally speaking, we want one word (or words separated by an underscore), all lowercase, that don't start with numbers.

The `janitor` library makes fixing headers trivially simple with the function `clean_names()`

``` 

# cleaning function
cleaned_arnold_md_loans <- arnold_md_loans %>%
  clean_names()

# display the cleaned dataset
cleaned_arnold_md_loans
```

    ## # A tibble: 6 x 7
    ##      x1_id name                   amount street_address     city  state zip     
    ##      <dbl> <chr>                  <chr>  <chr>              <chr> <chr> <chr>   
    ## 1 93761495 STUART JONES LLC       693361 700 Mill Creek Rd  Arno… MD    21012-1…
    ## 2 93761495 STUART JONES LLC       693361 700 Mill Creek Rd  Arno… MD    21012-1…
    ## 3 93762575 CHAPELWOOD ENTERPRISE… 559000 1511 RITCHIE HWY   ARNO… MD    21012-2…
    ## 4 99479443 VINEVE LLC             39700  1506 Ritchie Hgwy  Arnld MD    21012   
    ## 5 99490480 ARNOLD CHIROPRACTIC C… 28422  1507 ritchie hwy   arno… MD    21012   
    ## 6 99535547 SPARKS ELECTRICAL SER… 19335  1238 Birchcrest C… Anold MD    21012

This function changed `NAME` to `name`. It put an underscore in `street_address` to get rid of the space. And it changed `1_id` to `x1_id`. That last one was an improvement -- it no longer starts with a number -- but it's still kind of clunky.

We can use a tidyverse function `rename()` to fix that. Let's just call it `id`

``` 

# cleaning function
cleaned_arnold_md_loans <- arnold_md_loans %>%
  clean_names() %>%
  rename(id = x1_id)

# display the cleaned dataset
cleaned_arnold_md_loans
```

    ## # A tibble: 6 x 7
    ##         id name                   amount street_address     city  state zip     
    ##      <dbl> <chr>                  <chr>  <chr>              <chr> <chr> <chr>   
    ## 1 93761495 STUART JONES LLC       693361 700 Mill Creek Rd  Arno… MD    21012-1…
    ## 2 93761495 STUART JONES LLC       693361 700 Mill Creek Rd  Arno… MD    21012-1…
    ## 3 93762575 CHAPELWOOD ENTERPRISE… 559000 1511 RITCHIE HWY   ARNO… MD    21012-2…
    ## 4 99479443 VINEVE LLC             39700  1506 Ritchie Hgwy  Arnld MD    21012   
    ## 5 99490480 ARNOLD CHIROPRACTIC C… 28422  1507 ritchie hwy   arno… MD    21012   
    ## 6 99535547 SPARKS ELECTRICAL SER… 19335  1238 Birchcrest C… Anold MD    21012

## 11.2 Changing data types {number="11.2"}

Right now, the amount column is stored as a character. Do you see the little `<chr>` under the amount column in the table above? If we wanted to do math to it, we'd get an error, like so.

``` 

# cleaning function
total_arnold_md_loans <- cleaned_arnold_md_loans %>%
  summarise(total_amount = sum(amount))
```

    ## Error: Problem with `summarise()` column `total_amount`.
    ## ℹ `total_amount = sum(amount)`.
    ## x invalid 'type' (character) of argument

``` 
# display the cleaned dataset
total_arnold_md_loans
```

    ## Error in eval(expr, envir, enclos): object 'total_arnold_md_loans' not found

We got an "invalid 'type' (character)" error. So let's fix that using the mutate() function in concert with as.numeric(). We'll reuse the same column name, so it overwrites it.

``` 

# cleaning function
cleaned_arnold_md_loans <- arnold_md_loans %>%
  clean_names() %>%
  rename(id = x1_id) %>%
  mutate(amount = as.numeric(amount))
  

# display the cleaned dataset
cleaned_arnold_md_loans
```

    ## # A tibble: 6 x 7
    ##         id name                   amount street_address     city  state zip     
    ##      <dbl> <chr>                   <dbl> <chr>              <chr> <chr> <chr>   
    ## 1 93761495 STUART JONES LLC       693361 700 Mill Creek Rd  Arno… MD    21012-1…
    ## 2 93761495 STUART JONES LLC       693361 700 Mill Creek Rd  Arno… MD    21012-1…
    ## 3 93762575 CHAPELWOOD ENTERPRISE… 559000 1511 RITCHIE HWY   ARNO… MD    21012-2…
    ## 4 99479443 VINEVE LLC              39700 1506 Ritchie Hgwy  Arnld MD    21012   
    ## 5 99490480 ARNOLD CHIROPRACTIC C…  28422 1507 ritchie hwy   arno… MD    21012   
    ## 6 99535547 SPARKS ELECTRICAL SER…  19335 1238 Birchcrest C… Anold MD    21012

Notice that the amount has been converted to a `<dbl>`, which is short for double, a number format. When we attempt to add up all of the amounts to create a total, this time it works fine.

``` 

# cleaning function
total_arnold_md_loans <- cleaned_arnold_md_loans %>%
  summarise(total_amount = sum(amount))

# display the cleaned dataset
total_arnold_md_loans
```

    ## # A tibble: 1 x 1
    ##   total_amount
    ##          <dbl>
    ## 1      2033179

## 11.3 Duplicates {number="11.3"}

One of the most difficult problems to fix in data is duplicate records in the data. They can creep in with bad joins, bad data entry practices, mistakes -- all kinds of reasons. A duplicated record isn't always there because of an error, but you need to know if it's there before making that determination.

So the question is, do we have any records repeated?

Here we'll use a function called `get_dupes` from the janitor library to check for fully repeated records in our cleaned data set.

``` 
cleaned_arnold_md_loans %>% 
  get_dupes()
```

    ## No variable names specified - using all columns.

    ## # A tibble: 2 x 8
    ##         id name          amount street_address   city  state zip      dupe_count
    ##      <dbl> <chr>          <dbl> <chr>            <chr> <chr> <chr>         <int>
    ## 1 93761495 STUART JONES… 693361 700 Mill Creek … Arno… MD    21012-1…          2
    ## 2 93761495 STUART JONES… 693361 700 Mill Creek … Arno… MD    21012-1…          2

In this case, the first two records in our table are fully duplicated. Every field is identical in each.

We can fix this by adding the function `distinct()` to our cleaning script. This will keep only one copy of each unique record in our table

``` 

# cleaning function
cleaned_arnold_md_loans <- arnold_md_loans %>%
  clean_names() %>%
  rename(id = x1_id) %>%
  mutate(amount = as.numeric(amount)) %>%
  distinct()
  

# display the cleaned dataset
cleaned_arnold_md_loans
```

    ## # A tibble: 5 x 7
    ##         id name                   amount street_address     city  state zip     
    ##      <dbl> <chr>                   <dbl> <chr>              <chr> <chr> <chr>   
    ## 1 93761495 STUART JONES LLC       693361 700 Mill Creek Rd  Arno… MD    21012-1…
    ## 2 93762575 CHAPELWOOD ENTERPRISE… 559000 1511 RITCHIE HWY   ARNO… MD    21012-2…
    ## 3 99479443 VINEVE LLC              39700 1506 Ritchie Hgwy  Arnld MD    21012   
    ## 4 99490480 ARNOLD CHIROPRACTIC C…  28422 1507 ritchie hwy   arno… MD    21012   
    ## 5 99535547 SPARKS ELECTRICAL SER…  19335 1238 Birchcrest C… Anold MD    21012

## 11.4 Cleaning strings {number="11.4"}

The rest of the problems with this data set all have to do with inconsistent format of values in a few of the columns. To fix these problems, we're going to make use of mutate() and a new function, `case_when()` in concert with "string functions" -- special functions that allow us to clean up columns stored as character strings. The tidyverse package `stringr` has lots of useful string functions, more than we'll learn in this chapter.

Let's start by cleaning up the zip field. Remember, three of rows had a five-digit ZIP code, while two had a nine-digit ZIP code, separated by a hyphen.

We're going to write code that tells R to keep the first five digits on the left, and get rid of anything after that by using `mutate()` in concert with `str_sub()`, from the `stringr` package.

``` 

# cleaning function
cleaned_arnold_md_loans <- arnold_md_loans %>%
  clean_names() %>%
  rename(id = x1_id) %>%
  mutate(amount = as.numeric(amount)) %>%
  distinct() %>%
  mutate(zip = str_sub(zip, start=1L, end=5L))
  

# display the cleaned dataset
cleaned_arnold_md_loans
```

    ## # A tibble: 5 x 7
    ##         id name                      amount street_address     city  state zip  
    ##      <dbl> <chr>                      <dbl> <chr>              <chr> <chr> <chr>
    ## 1 93761495 STUART JONES LLC          693361 700 Mill Creek Rd  Arno… MD    21012
    ## 2 93762575 CHAPELWOOD ENTERPRISES, … 559000 1511 RITCHIE HWY   ARNO… MD    21012
    ## 3 99479443 VINEVE LLC                 39700 1506 Ritchie Hgwy  Arnld MD    21012
    ## 4 99490480 ARNOLD CHIROPRACTIC CENT…  28422 1507 ritchie hwy   arno… MD    21012
    ## 5 99535547 SPARKS ELECTRICAL SERVIC…  19335 1238 Birchcrest C… Anold MD    21012

Let's break down this line of code. It says: take the value in each zip column and extract the first character on the left (1L) through the fifth character on the left (5L), and then use that five-digit zip to overwrite the zip column.

We'll use a different set of functions to standardize how we standardize the different flavors of the word "Arnold" in the city column. Let's start by changing every value to title case -- first letter uppercase, subsequent letters lowercase -- using the `str_to_title()` function from `stringr`.

``` 

# cleaning function
cleaned_arnold_md_loans <- arnold_md_loans %>%
  clean_names() %>%
  rename(id = x1_id) %>%
  mutate(amount = as.numeric(amount)) %>%
  distinct() %>%
  mutate(zip = str_sub(zip, start=1L, end=5L)) %>%
  mutate(city = str_to_title(city))
  

# display the cleaned dataset
cleaned_arnold_md_loans
```

    ## # A tibble: 5 x 7
    ##         id name                      amount street_address     city  state zip  
    ##      <dbl> <chr>                      <dbl> <chr>              <chr> <chr> <chr>
    ## 1 93761495 STUART JONES LLC          693361 700 Mill Creek Rd  Arno… MD    21012
    ## 2 93762575 CHAPELWOOD ENTERPRISES, … 559000 1511 RITCHIE HWY   Arno… MD    21012
    ## 3 99479443 VINEVE LLC                 39700 1506 Ritchie Hgwy  Arnld MD    21012
    ## 4 99490480 ARNOLD CHIROPRACTIC CENT…  28422 1507 ritchie hwy   Arno… MD    21012
    ## 5 99535547 SPARKS ELECTRICAL SERVIC…  19335 1238 Birchcrest C… Anold MD    21012

That was enough to standardize two values (ARNOLD and arnold). The only ones that remain are the two clear misspellings (Arnld and Anold). To fix those, we're going to do some manual editing. And for that, we're going to use `case_when()`, a function that let's us say if a value meets a certain condition, then change it, and if it doesn't, don't change it.

``` 

# cleaning function
cleaned_arnold_md_loans <- arnold_md_loans %>%
  clean_names() %>%
  rename(id = x1_id) %>%
  mutate(amount = as.numeric(amount)) %>%
  distinct() %>%
  mutate(zip = str_sub(zip, start=1L, end=5L)) %>%
  mutate(city = str_to_title(city)) %>%
  mutate(city = case_when(
    city == "Anold" ~ "Arnold",
    TRUE ~ city
  ))
  

# display the cleaned dataset
cleaned_arnold_md_loans
```

    ## # A tibble: 5 x 7
    ##         id name                      amount street_address     city  state zip  
    ##      <dbl> <chr>                      <dbl> <chr>              <chr> <chr> <chr>
    ## 1 93761495 STUART JONES LLC          693361 700 Mill Creek Rd  Arno… MD    21012
    ## 2 93762575 CHAPELWOOD ENTERPRISES, … 559000 1511 RITCHIE HWY   Arno… MD    21012
    ## 3 99479443 VINEVE LLC                 39700 1506 Ritchie Hgwy  Arnld MD    21012
    ## 4 99490480 ARNOLD CHIROPRACTIC CENT…  28422 1507 ritchie hwy   Arno… MD    21012
    ## 5 99535547 SPARKS ELECTRICAL SERVIC…  19335 1238 Birchcrest C… Arno… MD    21012

This is a little complex, so let's break it down.

What the code above says, in English, is this: Look at all the values in the city column. If the value is "Anold," then (that's what the "\~" means, then) replace it with the word "Arnold." If it's anything other than that (that's what "TRUE" means, otherwise), then keep the existing value in that column.

We could fix "Arnld" by adding another line inside that function, that looks identical: `city == "Arnld" ~ "Arnold"`. Like so.

``` 

# cleaning function
cleaned_arnold_md_loans_ <- arnold_md_loans %>%
  clean_names() %>%
  rename(id = x1_id) %>%
  mutate(amount = as.numeric(amount)) %>%
  distinct() %>%
  mutate(zip = str_sub(zip, start=1L, end=5L)) %>%
  mutate(city = str_to_title(city)) %>%
  mutate(city = case_when(
    city == "Anold" ~ "Arnold",
    city == "Arnld" ~ "Arnold",
    TRUE ~ city
  ))
  

# display the cleaned dataset
cleaned_arnold_md_loans_
```

    ## # A tibble: 5 x 7
    ##         id name                      amount street_address     city  state zip  
    ##      <dbl> <chr>                      <dbl> <chr>              <chr> <chr> <chr>
    ## 1 93761495 STUART JONES LLC          693361 700 Mill Creek Rd  Arno… MD    21012
    ## 2 93762575 CHAPELWOOD ENTERPRISES, … 559000 1511 RITCHIE HWY   Arno… MD    21012
    ## 3 99479443 VINEVE LLC                 39700 1506 Ritchie Hgwy  Arno… MD    21012
    ## 4 99490480 ARNOLD CHIROPRACTIC CENT…  28422 1507 ritchie hwy   Arno… MD    21012
    ## 5 99535547 SPARKS ELECTRICAL SERVIC…  19335 1238 Birchcrest C… Arno… MD    21012

Instead of specifying the exact value, we can also solve the problem by using something more generalizable, using a function called str_detect(), which allows us to search parts of words.

The second line of our case_when() function below now says, in English: look in the city column. If you find that one of the values starts with "Arnl" (the "\^" symbol means "starts with"), then (the tilde \~ means then) change it to "Arnold."

``` 

# cleaning function
cleaned_arnold_md_loans <- arnold_md_loans %>%
  clean_names() %>%
  rename(id = x1_id) %>%
  mutate(amount = as.numeric(amount)) %>%
  distinct() %>%
  mutate(zip = str_sub(zip, start=1L, end=5L)) %>%
  mutate(city = str_to_title(city)) %>%
  mutate(city = case_when(
    city == "Anold" ~ "Arnold",
    str_detect(city,"^Arnl") ~ "Arnold",
    TRUE ~ city
  ))
  

# display the cleaned dataset
cleaned_arnold_md_loans
```

    ## # A tibble: 5 x 7
    ##         id name                      amount street_address     city  state zip  
    ##      <dbl> <chr>                      <dbl> <chr>              <chr> <chr> <chr>
    ## 1 93761495 STUART JONES LLC          693361 700 Mill Creek Rd  Arno… MD    21012
    ## 2 93762575 CHAPELWOOD ENTERPRISES, … 559000 1511 RITCHIE HWY   Arno… MD    21012
    ## 3 99479443 VINEVE LLC                 39700 1506 Ritchie Hgwy  Arno… MD    21012
    ## 4 99490480 ARNOLD CHIROPRACTIC CENT…  28422 1507 ritchie hwy   Arno… MD    21012
    ## 5 99535547 SPARKS ELECTRICAL SERVIC…  19335 1238 Birchcrest C… Arno… MD    21012

That only changed one value "Arnld." Imagine that there were other rows with values like "Arnlid,""Arnl" or "Arnlod." By using str_detect(city,"\^Arnl"), we pick up any values that start with "Arnl," so it would change all four of these. If we used city == "Arnld," it would only pick up one.

Lastly, there's the issue with inconsistent spelling of Ritchie Hwy in the street address column. Do we need to clean this?

Remember the motivating question that's driving us to do this cleaning: What's the total amount of loans (at least in this tiny slice of data) for Arnold, MD in ZIP code 21012?

We don't need the street_address field to answer that question. So we're not going to bother cleaning it.

That's a good approach for the future. A good rule of thumb is that you should only spend time cleaning fields that are critical to the specific analysis you want to do.

`<!--chapter:end:10-janitor.Rmd-->`{=html}



#  Data Cleaning Part III: Open Refine {number="12"}

Gather 'round kids and let me tell you a tale about your author. In college, your author (Matt Waite) got involved in a project where he mapped crime in the city, looking specifically in the neighborhoods surrounding campus. This was in the mid 1990s. Computers were under powered. Tools were pretty primitive. I was given a database of nearly 50,000 calls for service.

And then I learned that addresses were not stored in a standard way. However the officer wrote it down, that's how it was recorded.

What did that mean?

It meant the Lincoln (Nebraska) Police Department came up with dozens of ways to say a single place. And since the mapping software needed the addressed to be in a specific form, I had to fix them. For example, I will go to my grave knowing that Lincoln High School's street address is 2229 J Street. Police officers wrote down LHS, L.H.S., Lincoln HS, Lincoln H.S., LHS (J Street), 2229 J, 2229 J ST, St., Street and on and on and on. That one was relatively easy. The local convenience store chain, with 8 locations around the city, was harder. I had to use the patrol district to locate them.

It took me four months to clean up more than 30,000 unique addresses and map them.

I tell you this because if I had Open Refine, it would have taken me a week, not four months.

Every time I talk about Open Refine, I remember this, and I get mad.

Fortunately (unfortunately?) several columns in the PPP loan data we're working with are flawed in exactly the same way. There are dozens of variations on just "Baltimore."

We're going to explore two ways into Open Refine: Through R, and through Open Refine itself.

## 12.1 Refinr, Open Refine in R {number="12.1"}

What is Open Refine?

Open Refine is a software program that has tools -- algorithms -- that find small differences in text and helps you fix them quickly. How Open Refine finds those small differences is through something called clustering. The algorithms behind clustering are not exclusive to Open Refine, so they can be used elsewhere.

Enter `refinr`, a package that contains the same clustering algorithms as Open Refine but all within R. Go ahead and install it if you haven't already by opening the console and running `install.packages("refinr")`. Then we can load libraries as we do.

``` 
library(tidyverse)
library(refinr)
library(janitor)
```

Let's load our full Maryland PPP loans data.

Now let's try and group and count the number of loans by city. To make it a bit more managable, let's use another string function from `stringr` and filter for cities that start with the uppercase "A" or lowercase "a" using the function `str_detect()` with a regular expression.

The filter function in the codeblock below says: look in the city column, and pluck out any value that starts with (the "\^" symbol means "starts with") a lowercase "a" OR (the vertical "\|," called a pipe, means OR) an uppercase "A."

``` 
md_loans %>%
  group_by(city) %>%
  summarise(
    count=n()
  ) %>%
  filter(str_detect(city, "^a|^A")) %>%
  arrange(city)
```

    ## # A tibble: 62 x 2
    ##    city                    count
    ##    <chr>                   <int>
    ##  1 ABDULREZAK H ISSAC          1
    ##  2 Abell                       3
    ##  3 ABELL                       2
    ##  4 aberdeen                    3
    ##  5 Aberdeen                  456
    ##  6 ABERDEEN                  192
    ##  7 Aberdeen Proving Ground    13
    ##  8 ABERDEEN PROVING GROUND     2
    ##  9 Abereen                     1
    ## 10 abigdon                     2
    ## # … with 52 more rows

There are lots of problems in this data that will prevent proper grouping and summarizing. We've learned several functions to do this manually.

By using the Open Refine package for R, `refinr`, our hope is that it can identify and standardize the data with a little more ease.

The first merging technique that's part of the `refinr` package we'll try is the `key_collision_merge`.

The key collision merge function takes each string and extracts the key parts of it. It then puts every key in a bin based on the keys matching.

One rule you should follow when using this is: **do not overwrite your original fields**. Always work on a copy. If you overwrite your original field, how will you know if it did the right thing? How can you compare it to your original data? To follow this, I'm going to mutate a new field called clean_city and put the results of key collision merge there.

``` 
cleaned_md_loans <- md_loans %>%
  mutate(city_clean=key_collision_merge(city)) %>%
  select(id:city, city_clean, everything())

cleaned_md_loans
```

    ## # A tibble: 195,865 x 64
    ##         id name    slug   amount state address city  city_clean zip   naics_code
    ##      <dbl> <chr>   <chr>   <dbl> <chr> <chr>   <chr> <chr>      <chr>      <dbl>
    ##  1  9.94e7 TARBIY… tarbi… 149000 MD    6785 B… Elkr… Elkridge   2107…     611110
    ##  2  9.94e7 J &AMP… j-amp… 146000 MD    10413 … Unio… Union Bri… 21791     238310
    ##  3  9.94e7 DULANE… dulan… 140400 MD    4 Wind… PHOE… Phoenix    2113…     623110
    ##  4  9.94e7 QUARTE… quart… 139527 MD    4972 W… Rock… Rockville  20852     311920
    ##  5  9.94e7 ORCHAR… orcha… 133400 MD    1855 W… Owin… Owings     2073…     561730
    ##  6  9.94e7 FRUITL… fruit… 133000 MD    402 MA… EAST… EASTON     2160…     531120
    ##  7  9.94e7 YOUNIV… youni… 130520 MD    5000 T… Oakl… Oakland    2155…     621610
    ##  8  9.94e7 FRANKL… frank… 121862 MD    14805 … Spar… Sparks     2115…     812990
    ##  9  9.94e7 RACE P… race-… 121100 MD    1 RAIL… WEST… Westminst… 2115…     451110
    ## 10  9.94e7 VITAL … vital… 120165 MD    1701 P… Broo… Brookevil… 2083…     541330
    ## # … with 195,855 more rows, and 54 more variables: business_type <chr>,
    ## #   race <chr>, gender <chr>, veteran <chr>, non_profit <lgl>,
    ## #   jobs_retained <dbl>, date_approved <date>, lender <chr>,
    ## #   congressional_district <chr>, loan_range_sort_key <lgl>,
    ## #   previous_loan_range <lgl>, previous_name <lgl>, loan_number <dbl>,
    ## #   sba_office_code <dbl>, processing_method <chr>, loan_status <chr>,
    ## #   term <dbl>, sba_guaranty_percentage <dbl>, initial_approval_amount <dbl>,
    ## #   current_approval_amount <dbl>, undisbursed_amount <dbl>,
    ## #   franchise_name <chr>, servicing_lender_location_id <dbl>,
    ## #   servicing_lender_name <chr>, servicing_lender_address <chr>,
    ## #   servicing_lender_city <chr>, servicing_lender_state <chr>,
    ## #   servicing_lender_zip <chr>, rural_urban_indicator <chr>,
    ## #   hubzone_indicator <chr>, business_age_description <chr>,
    ## #   project_city <chr>, project_county_name <chr>, project_state <chr>,
    ## #   project_zip <chr>, utilities_proceed <dbl>, payroll_proceed <dbl>,
    ## #   mortgage_interest_proceed <dbl>, rent_proceed <dbl>,
    ## #   refinance_eidl_proceed <dbl>, health_care_proceed <dbl>,
    ## #   debt_interest_proceed <dbl>, originating_lender_city <chr>,
    ## #   originating_lender_state <chr>, loan_status_date <date>,
    ## #   originating_lender_location_id <dbl>, old_slug <chr>, lmi_indicator <chr>,
    ## #   unmatched_original <lgl>, unmatched_updated <lgl>,
    ## #   previous_jobs_reported <lgl>, ethnicity <chr>, forgiveness_amount <dbl>,
    ## #   forgiveness_date <date>

To examine changes `refinr` made, let's examine the changes it made to cities that start with the letter "A."

``` 
cleaned_md_loans %>%
  group_by(city_clean, city) %>%
  summarise(
    count=n()
  ) %>%
  filter(str_detect(city, "^a|^A")) %>%
  arrange(city)
```

    ## `summarise()` has grouped output by 'city_clean'. You can override using the `.groups` argument.

    ## # A tibble: 62 x 3
    ## # Groups:   city_clean [38]
    ##    city_clean              city                    count
    ##    <chr>                   <chr>                   <int>
    ##  1 ABDULREZAK H ISSAC      ABDULREZAK H ISSAC          1
    ##  2 Abell                   Abell                       3
    ##  3 Abell                   ABELL                       2
    ##  4 Aberdeen                aberdeen                    3
    ##  5 Aberdeen                Aberdeen                  456
    ##  6 Aberdeen                ABERDEEN                  192
    ##  7 Aberdeen Proving Ground Aberdeen Proving Ground    13
    ##  8 Aberdeen Proving Ground ABERDEEN PROVING GROUND     2
    ##  9 Abereen                 Abereen                     1
    ## 10 abigdon                 abigdon                     2
    ## # … with 52 more rows

It got a bunch of things right. It merged three variations of "Aberdeen" -- "aberdeen,""Aberdeen" and "ABERDEEN" -- and it didn't merge it with "Aberdeen Proving Ground," which are two distinct places. But it wasn't smart enough to convert "Abereen" to "Aberdeen."

It also merged "Annapolis" and "ANNAPOLIS" under "Annapolis," and was smart enough not to merge it with "Annapolis Junction," which is not the same city. But it wasn't smart enough to merge "Annapoils" or "Annalpolis."

There's another merging algorithim that's part of refinr that works a bit differently, called `n_gram_merge()`. Let's try applying that one.

``` 
cleaned_md_loans <- md_loans %>%
  mutate(city_clean=n_gram_merge(city)) %>%
  select(id:city, city_clean, everything())

cleaned_md_loans
```

    ## # A tibble: 195,865 x 64
    ##         id name    slug   amount state address city  city_clean zip   naics_code
    ##      <dbl> <chr>   <chr>   <dbl> <chr> <chr>   <chr> <chr>      <chr>      <dbl>
    ##  1  9.94e7 TARBIY… tarbi… 149000 MD    6785 B… Elkr… Elkridge   2107…     611110
    ##  2  9.94e7 J &AMP… j-amp… 146000 MD    10413 … Unio… Union Bri… 21791     238310
    ##  3  9.94e7 DULANE… dulan… 140400 MD    4 Wind… PHOE… Phoenix    2113…     623110
    ##  4  9.94e7 QUARTE… quart… 139527 MD    4972 W… Rock… Rockville  20852     311920
    ##  5  9.94e7 ORCHAR… orcha… 133400 MD    1855 W… Owin… Owings     2073…     561730
    ##  6  9.94e7 FRUITL… fruit… 133000 MD    402 MA… EAST… EASTON     2160…     531120
    ##  7  9.94e7 YOUNIV… youni… 130520 MD    5000 T… Oakl… Oakland    2155…     621610
    ##  8  9.94e7 FRANKL… frank… 121862 MD    14805 … Spar… Sparks     2115…     812990
    ##  9  9.94e7 RACE P… race-… 121100 MD    1 RAIL… WEST… Westminst… 2115…     451110
    ## 10  9.94e7 VITAL … vital… 120165 MD    1701 P… Broo… Brookevil… 2083…     541330
    ## # … with 195,855 more rows, and 54 more variables: business_type <chr>,
    ## #   race <chr>, gender <chr>, veteran <chr>, non_profit <lgl>,
    ## #   jobs_retained <dbl>, date_approved <date>, lender <chr>,
    ## #   congressional_district <chr>, loan_range_sort_key <lgl>,
    ## #   previous_loan_range <lgl>, previous_name <lgl>, loan_number <dbl>,
    ## #   sba_office_code <dbl>, processing_method <chr>, loan_status <chr>,
    ## #   term <dbl>, sba_guaranty_percentage <dbl>, initial_approval_amount <dbl>,
    ## #   current_approval_amount <dbl>, undisbursed_amount <dbl>,
    ## #   franchise_name <chr>, servicing_lender_location_id <dbl>,
    ## #   servicing_lender_name <chr>, servicing_lender_address <chr>,
    ## #   servicing_lender_city <chr>, servicing_lender_state <chr>,
    ## #   servicing_lender_zip <chr>, rural_urban_indicator <chr>,
    ## #   hubzone_indicator <chr>, business_age_description <chr>,
    ## #   project_city <chr>, project_county_name <chr>, project_state <chr>,
    ## #   project_zip <chr>, utilities_proceed <dbl>, payroll_proceed <dbl>,
    ## #   mortgage_interest_proceed <dbl>, rent_proceed <dbl>,
    ## #   refinance_eidl_proceed <dbl>, health_care_proceed <dbl>,
    ## #   debt_interest_proceed <dbl>, originating_lender_city <chr>,
    ## #   originating_lender_state <chr>, loan_status_date <date>,
    ## #   originating_lender_location_id <dbl>, old_slug <chr>, lmi_indicator <chr>,
    ## #   unmatched_original <lgl>, unmatched_updated <lgl>,
    ## #   previous_jobs_reported <lgl>, ethnicity <chr>, forgiveness_amount <dbl>,
    ## #   forgiveness_date <date>

To examine changes `refinr` made with this algorithm, let's again look at cities that start with the letter "A." Examining Aberdeen and Annapolis, we see there wasn't a substantial change from the previous method.

``` 
cleaned_md_loans %>%
  group_by(city_clean, city) %>%
  summarise(
    count=n()
  ) %>%
  filter(str_detect(city, "^a|^A")) %>%
  arrange(city)
```

    ## `summarise()` has grouped output by 'city_clean'. You can override using the `.groups` argument.

    ## # A tibble: 62 x 3
    ## # Groups:   city_clean [36]
    ##    city_clean              city                    count
    ##    <chr>                   <chr>                   <int>
    ##  1 ABDULREZAK H ISSAC      ABDULREZAK H ISSAC          1
    ##  2 Abell                   Abell                       3
    ##  3 Abell                   ABELL                       2
    ##  4 Aberdeen                aberdeen                    3
    ##  5 Aberdeen                Aberdeen                  456
    ##  6 Aberdeen                ABERDEEN                  192
    ##  7 Aberdeen Proving Ground Aberdeen Proving Ground    13
    ##  8 Aberdeen Proving Ground ABERDEEN PROVING GROUND     2
    ##  9 Abereen                 Abereen                     1
    ## 10 Abingdon                abigdon                     2
    ## # … with 52 more rows

That's how you use the Open Refine r package, refinr.

Now let's upload the data to the interactive version of OpenRefine, which really shines at this task.

## 12.2 Manually cleaning data with Open Refine {number="12.2"}

Open Refine is free software. [You should download and install it](https://openrefine.org/). Refinr is great for quick things on smaller datasets that you can check to make sure it's not up to any mischief.

For bigger datasets, Open Refine is the way to go. And it has a lot more tools than refinr does (by design).

After you install it, run it. Open Refine works in the browser, and the app spins up a small web server visible only on your computer to interact with it. A browser will pop up automatically.

You first have to import your data into a project. Click the choose files button and upload a csv of the Maryland loans.


After your data is loaded into the app, you'll get a screen to look over what the data looks like. On the top right corner, you'll see a button to create the project. Click that.


Open Refine has many, many tools. We're going to use one piece of it, as a tool for data cleaning. To learn how to use it, we're going to clean the "city" field.

First, let's make a copy of the original city column so that we can preserve the original data while cleaning the new one.

Click the dropdown arrow next to the city column, choose "edit column" \> Add column based on this column.


Now, let's get to work cleaning the city column.

Next to the city field name, click the down arrow, then facet, then text facet.


After that, a new box will appear on the left. It tells us how many unique cities there are: 1,977. And, there's a button on the right of the box that says Cluster.


Click the cluster button. A new window will pop up, a tool to help us identify things that need to be cleaned, and quickly clean them.


The default "method" used is a clustering algorithim called "key collision," using the fingerprint function. This is the same method we used with the refinr package above.

At the top, you'll see which method was used, and how many clusters that algorithm identified. There are several different methods, each of which work slightly differently and produce different results.


Then, below that, you can see what those clusters are. Right away, we can see how useful this program is. It identified 9,903 rows that have some variation on "Silver Spring" in the city field: Silver Spring, SILVER SPRING, silver spring, Silver spring, silver Spring and so on. It proposed changing them all to "Silver Spring."

Using human judgement, you can say if you agree with the cluster. If you do, click the "merge" checkbox. When it merges, the new result will be what it says in New Cell Value. Most often, that's the row with the most common result.


Now begins the fun part: You have to look at all 533 clusters found and decide if they are indeed valid. The key collision method is very good, and very conservative. You'll find that most of them are usually valid.

Be careful! If you merge two things that aren't supposed to be together, it will change your data in a way that could lead to inaccurate results.

When you're done, click Merge Selected and Re-Cluster.


If any new clusters come up, evaluate them. Repeat until either no clusters come up or the clusters that do come up are ones you reject.

Now. Try a new method, maybe the "nearest neighbor levenshtein" method. Notice that it finds even more variations of Silver Spring, using a slightly different approach.


Rinse and repeat.

You'll keep doing this, and if the dataset is reasonably clean, you'll find the end.

When you're finished cleaning, click "Merge Selected & Close."


Then, export the data as a csv so you can load it back into R.


A question for all data analysts -- if the dataset is bad enough, can it ever be cleaned?

There's no good answer. You have to find it yourself.

`<!--chapter:end:11-openrefine.Rmd-->`{=html}


#  Cleaning Data Part IV: PDFs {number="13"}

The next circle of Hell on the Dante's Inferno of Data Journalism is the PDF. Governments everywhere love the PDF and publish all kinds of records in a PDF. The problem is a PDF isn't a data format -- it's a middle finger, saying I've Got Your Accountability Right Here, Pal.

It's so ridiculous that there's a constellation of tools that do nothing more than try to harvest tables out of PDFs. There are online services like [CometDocs](https://www.cometdocs.com/) where you can upload your PDF and point and click your way into an Excel file. There are mobile device apps that take a picture of a table and convert it into a spreadsheet. But one of the best is a tool called [Tabula](https://tabula.technology/). It was build by journalists for journalists.

There is a version of Tabula that will run inside of R -- a library called Tabulizer -- but the truth is I'm having the hardest time installing it on my machine, which leads me to believe that trying to install it across a classroom of various machines would be disastrous. The standalone version works just fine, and it provides a useful way for you to see what's actually going on.

Unfortunately, harvesting tables from PDFs with Tabula is an exercise in getting your hopes up, only to have them dashed. We'll start with an example.

## 13.1 Easy does it {number="13.1"}

Tabula works best when tables in PDFs are clearly defined and have nicely-formatted information. Here's a perfect example: [active voters by county in Maryland](https://elections.maryland.gov/press_room/2020_stats/Eligible%20Active%20Voters%20by%20County%20-%20PG20.pdf).

[Download and install Tabula](https://tabula.technology/). Tabula works much the same way as Open Refine does -- it works in the browser by spinning up a small webserver in your computer.

When Tabula opens, you click browse to find the PDF on your computer somewhere, and then click import. After it imports, click autodetect tables. You'll see red boxes appear around what Tabula believes are the tables. You'll see it does a pretty good job at this.


Now you can hit the green "Preview & Export Extracted Data" button on the top right. You should see something very like this:


You can now export that extracted table to a CSV file using the "Export" button. And then we can read it into R:

``` 
voters_by_county <- read_csv("data/tabula-Eligible Active Voters by County - PG20.csv")
```

    ## 
    ## ── Column specification ────────────────────────────────────────────────────────
    ## cols(
    ##   County = col_character(),
    ##   DEM = col_number(),
    ##   REP = col_number(),
    ##   BAR = col_number(),
    ##   GRN = col_number(),
    ##   LIB = col_number(),
    ##   WCP = col_number(),
    ##   OTH = col_number(),
    ##   UNA = col_number(),
    ##   TOTAL = col_number()
    ## )

``` 
voters_by_county
```

    ## # A tibble: 25 x 10
    ##    County              DEM    REP   BAR   GRN   LIB   WCP   OTH    UNA  TOTAL
    ##    <chr>             <dbl>  <dbl> <dbl> <dbl> <dbl> <dbl> <dbl>  <dbl>  <dbl>
    ##  1 Allegany          12820  22530    20    74   204    19   395   7674  43736
    ##  2 Anne Arundel     174494 135457   105   564  1922   197  2715  90162 405616
    ##  3 Baltimore City   311610  30163   130   802   951   290  3289  52450 399685
    ##  4 Baltimore County 313870 142534   134   898  2227   297  5872 100576 566408
    ##  5 Calvert           24587  28181    20    89   332    30   567  14178  67984
    ##  6 Caroline           6629  10039     2    33    86    17   163   4208  21177
    ##  7 Carroll           33662  63967    27   155   670    38  1072  25770 125361
    ##  8 Cecil             21601  30880     8   103   341    49   727  15110  68819
    ##  9 Charles           72416  24711    19   112   349    83   763  19849 118302
    ## 10 Dorchester         9848   8730     4    19    78    12   148   3348  22187
    ## # … with 15 more rows

Boom - we're good to go.

## 13.2 When it looks good, but needs a little fixing {number="13.2"}

Here's a slightly more involved PDF. Check out the table on page 4 of [this SBA PDF](https://www.sba.gov/sites/default/files/2021-06/PPP_Report_Public_210531-508.pdf).


Looks like a spreadsheet, right? Save that PDF file to your computer in a place where you'll remember it (like a Downloads folder).

Now let's repeat the steps we did to import the PDF into Tabula and autodetect the tables. Page 4 should look like this:


We just want the table on page 4, which shows 2021 loan activity by type of lender, so hit the "Clear All Selections" button to remove the red boxes. Now, in Tabula, let's draw a box around the table on page 4. Click and drag to draw the box.

Now you can hit the green "Preview & Export Extracted Data" button on the top right. You should see something very like this:


You can now export that extracted table to a CSV file using the "Export" button. And then we can read it into R:

``` 
lender_types <- read_csv("data/tabula-PPP_Report_Public_210531-508.csv")
```

    ## 
    ## ── Column specification ────────────────────────────────────────────────────────
    ## cols(
    ##   `Lender Type` = col_character(),
    ##   `Lender Count` = col_number(),
    ##   `Loans Approved` = col_number(),
    ##   `Net Dollars` = col_character()
    ## )

``` 
lender_types
```

    ## # A tibble: 13 x 4
    ##    `Lender Type`                 `Lender Count` `Loans Approved` `Net Dollars`  
    ##    <chr>                                  <dbl>            <dbl> <chr>          
    ##  1 Banks and S&Ls($10B or more)             112          1807532 $118,331,350,2…
    ##  2 Banks and S&Ls(less than $10…           4105          1812102 $101,504,685,2…
    ##  3 Fintechs (and other State Re…             41          1210098 $21,918,632,833
    ##  4 Small Business Lending Compa…             13           823576 $15,463,750,507
    ##  5 Microlenders                              34           532480 $8,540,740,467 
    ##  6 Credit Unions (less than $10…            851           152366 $5,160,428,953 
    ##  7 Non Bank CDFI Funds                        9           276271 $5,047,040,642 
    ##  8 Farm Credit Lenders                       47            35923 $870,150,045   
    ##  9 Credit Unions ($10B or more)               8            14903 $438,573,935   
    ## 10 Certified Development Compan…             19            16409 $419,677,207   
    ## 11 To Be Confirmed                            2              250 $4,779,785     
    ## 12 BIDCOs                                     1               19 $298,236       
    ## 13 Total                                   5242          6681929 $277,700,108,0…

## 13.3 Cleaning up the data in R {number="13.3"}

The good news is that we have data we don't have to retype. The bad news is, it's hardly in importable shape.

See the "Net Dollars" column? Thanks to the dollar signs, R doesn't recognize those values as numbers. The column names seem ok, but having spaces in them is a pain. Let's fix that by re-importing it and calling `mutate` so that the new `net_dollars` column is numeric.

``` 
lender_types <- read_csv("data/tabula-PPP_Report_Public_210531-508.csv", skip=1, col_names=c("type", "count", "approved", "net_dollars"))
```

    ## 
    ## ── Column specification ────────────────────────────────────────────────────────
    ## cols(
    ##   type = col_character(),
    ##   count = col_number(),
    ##   approved = col_number(),
    ##   net_dollars = col_character()
    ## )

``` 
lender_types <- lender_types %>% mutate(net_dollars=as.numeric(parse_number(net_dollars)))
lender_types
```

    ## # A tibble: 13 x 4
    ##    type                                 count approved  net_dollars
    ##    <chr>                                <dbl>    <dbl>        <dbl>
    ##  1 Banks and S&Ls($10B or more)           112  1807532 118331350203
    ##  2 Banks and S&Ls(less than $10B)        4105  1812102 101504685266
    ##  3 Fintechs (and other State Regulated)    41  1210098  21918632833
    ##  4 Small Business Lending Companies        13   823576  15463750507
    ##  5 Microlenders                            34   532480   8540740467
    ##  6 Credit Unions (less than $10B)         851   152366   5160428953
    ##  7 Non Bank CDFI Funds                      9   276271   5047040642
    ##  8 Farm Credit Lenders                     47    35923    870150045
    ##  9 Credit Unions ($10B or more)             8    14903    438573935
    ## 10 Certified Development Companies         19    16409    419677207
    ## 11 To Be Confirmed                          2      250      4779785
    ## 12 BIDCOs                                   1       19       298236
    ## 13 Total                                 5242  6681929 277700108079

All things considered, that was pretty easy. Many - most? - electronic PDFs aren't so easy to parse. Sometimes you'll need to open the exported CSV file and clean things up before importing into R. Other times you'll be able to do that cleaning in R itself.

Here's the sad truth: THIS IS PRETTY GOOD. It sure beats typing it out. And since many government processes don't change all that much, you can save the code to process subsequent versions of PDFs.

`<!--chapter:end:12-pdfs.Rmd-->`{=html}



#  Combining and joining {number="14"}

Often, as data journalists, we're looking at data across time or at data stored in multiple tables. And to do that, we need to often need to merge that data together.

Depending on what we have, we may just need to stack data on top of each other to make new data. If we have 2019 data and 2018 data and we want that to be one file, we stack them. If we have a dataset of cows in counties and a dataset of populations in county, we're going to join those two together on the county -- the common element.

Let's explore.

## 14.1 Combining data (stacking) {number="14.1"}

Let's say that we have county population estimates for three different years - [2010](https://umd.box.com/s/vsuyt7v1gtb2u0aerliv5eixfmzfgt17), [2015](https://umd.box.com/s/2qijnwfygsrfin9d2o1krhzw5o8vza30) and [2020](https://umd.box.com/s/uqkeaabkvs4ge0l10j3w3sa76q3z1v16) - in three different files. They have the same record layout and the same number of counties. We can combine them into a single dataframe.

Let's do what we need to import them properly. I've merged it all into one step for each of the three datasets.

``` 
library(tidyverse)
```

``` 
popestimate_2010 <- read_csv("data/popestimate_2010.csv")
```

    ## 
    ## ── Column specification ────────────────────────────────────────────────────────
    ## cols(
    ##   SUMLEV = col_double(),
    ##   REGION = col_double(),
    ##   DIVISION = col_double(),
    ##   STATE = col_double(),
    ##   COUNTY = col_double(),
    ##   STNAME = col_character(),
    ##   CTYNAME = col_character(),
    ##   YEAR = col_double(),
    ##   POPESTIMATE = col_double()
    ## )

``` 
popestimate_2015 <- read_csv("data/popestimate_2015.csv")
```

    ## 
    ## ── Column specification ────────────────────────────────────────────────────────
    ## cols(
    ##   SUMLEV = col_double(),
    ##   REGION = col_double(),
    ##   DIVISION = col_double(),
    ##   STATE = col_double(),
    ##   COUNTY = col_double(),
    ##   STNAME = col_character(),
    ##   CTYNAME = col_character(),
    ##   YEAR = col_double(),
    ##   POPESTIMATE = col_double()
    ## )

``` 
popestimate_2020 <- read_csv("data/popestimate_2020.csv")
```

    ## 
    ## ── Column specification ────────────────────────────────────────────────────────
    ## cols(
    ##   SUMLEV = col_double(),
    ##   REGION = col_double(),
    ##   DIVISION = col_double(),
    ##   STATE = col_double(),
    ##   COUNTY = col_double(),
    ##   STNAME = col_character(),
    ##   CTYNAME = col_character(),
    ##   YEAR = col_double(),
    ##   POPESTIMATE = col_double()
    ## )

All three of these datasets have the same number of columns, all with the same names, so if we want to merge them together to compare them over time, we need to stack them together. The verb here, in R, is `bind_rows`. You tell the function what you want to combine and it does it, assuming that you've got column names in common containing identically formatted data.

Since we have three dataframes, we're going to need to pass them as a list, meaning they'll be enclosed inside the `list` function.

``` 
estimates <- bind_rows(list(popestimate_2010, popestimate_2015, popestimate_2020))
```

And boom, like that, we have 9,852 rows of data together instead of three dataframes. There are plenty of uses for `bind_rows`: any regularly updated data that comes in the same format like crime reports or award recipients or player game statistics.

## 14.2 Joining data {number="14.2"}

More difficult is when you have two separate tables that are connected by a common element or elements.

Let's start by reading in the Maryland PPP loan applications data:

``` 
maryland_ppp <- read_csv('data/ppp_applications_md.csv')
```

    ## 
    ## ── Column specification ────────────────────────────────────────────────────────
    ## cols(
    ##   .default = col_character(),
    ##   id = col_double(),
    ##   amount = col_double(),
    ##   naics_code = col_double(),
    ##   non_profit = col_logical(),
    ##   jobs_retained = col_double(),
    ##   date_approved = col_datetime(format = ""),
    ##   loan_number = col_double(),
    ##   sba_office_code = col_double(),
    ##   term = col_double(),
    ##   sba_guaranty_percentage = col_double(),
    ##   initial_approval_amount = col_double(),
    ##   current_approval_amount = col_double(),
    ##   undisbursed_amount = col_double(),
    ##   servicing_lender_location_id = col_double(),
    ##   utilities_proceed = col_double(),
    ##   payroll_proceed = col_double(),
    ##   mortgage_interest_proceed = col_double(),
    ##   rent_proceed = col_double(),
    ##   refinance_eidl_proceed = col_double(),
    ##   health_care_proceed = col_double()
    ##   # ... with 5 more columns
    ## )
    ## ℹ Use `spec()` for the full column specifications.

One of the columns we have is called `naics_code`, which is a six-digit number used by the federal government "in classifying business establishments for the purpose of collecting, analyzing, and publishing statistical data related to the U.S. business economy." More details at [the official NAICS site](https://www.census.gov/naics/).

But unless you have a particular interest in memorizing what those more than 1,000 codes actually mean, the codes themselves don't help you understand what type of business any individual applicant has. Luckily, we can merge that information into our data using a join.

Using a [CSV file of the 2017 NAICS codes](https://umd.box.com/s/thou3merdzwzbdimbvd06zkax1zndcsk), let's read the file into R:

``` 
naics_codes <- read_csv('data/naics_codes.csv')
```

    ## 
    ## ── Column specification ────────────────────────────────────────────────────────
    ## cols(
    ##   naics_code = col_double(),
    ##   title = col_character()
    ## )

To put the Maryland applications and NAICS codes together, we need to use something called a join. There are different kinds of joins. It's better if you think of two tables sitting next to each other. A `left_join` takes all the records from the left table and only the records that match in the right one. A `right_join` does the same thing. An `inner_join` takes only the records where they are equal. There's one other join -- a `full_join` which returns all rows of both, regardless of if there's a match -- but I've never once had a use for a full join.

In the best-case scenario, the two tables we want to join share a common column. In this case, both of our tables have a column called `naics_code` that has the same characteristics: both are six-digit numbers.

We can do this join multiple ways and get a similar result. We can put the Maryland file on the left and the NAICS codes on the right and use a left join to get them all together. And we use `by=` to join by the correct column. And to avoid rendering hundreds of rows of data, I'm going to count the rows at the end. The reason I'm going this is important: **Rule 1 in joining data is having an idea of what you are expecting to get**. So with a left join with applications on the left, I have 195,869 applications, so I expect to get 195,869 rows when I'm done.

``` 
maryland_ppp %>% left_join(naics_codes, by="naics_code") %>% select(name, naics_code, title) %>% nrow()
```

    ## [1] 195869

Remove the nrow and run it again for yourself. By default, `dplyr` will do a "natural" join, where it'll match all the matching columns in both tables. So if we take out the by, it'll use all the common columns between the tables. That may not be right in every instance but let's try it. If it works, we should get 195,869 rows.

``` 
maryland_ppp %>% left_join(naics_codes) %>% select(name, naics_code, title)
```

    ## Joining, by = "naics_code"

    ## # A tibble: 195,869 x 3
    ##    name                       naics_code title                                  
    ##    <chr>                           <dbl> <chr>                                  
    ##  1 BAYWOOD HOTELS INC.            721110 Hotels (except Casino Hotels) and Mote…
    ##  2 PARTNERS ELECTRIC SERVICE…     238210 Electrical Contractors and Other Wirin…
    ##  3 RP3 LLC                        541810 Advertising Agencies                   
    ##  4 SUSHI KO CHEVY CHASE LLC.      722511 Full-Service Restaurants               
    ##  5 VILLAGE ACADEMY OF MARYLA…     611110 Elementary and Secondary Schools       
    ##  6 GOSHEN HOUSE TRADING LLC       721199 All Other Traveler Accommodation       
    ##  7 WEAVER BOAT WORKS              336612 Boat Building                          
    ##  8 BOBS OVERHEAD DOOR REPAIR…     238290 Other Building Equipment Contractors   
    ##  9 PARENTS FOR MONTESSORI ED…     611110 Elementary and Secondary Schools       
    ## 10 HARVEST PRINCE FREDERICK …     722511 Full-Service Restaurants               
    ## # … with 195,859 more rows

Since we only have one column in common between the two tables, the join only used that column. And we got the same answer. If we had more columns in common, you could see in your results columns with .X after them - that's a sign of duplicative columns between two tables, and you may decide you don't need both moving forward.

Let's save our joined data to a new dataframe, but this time let's remove the select function so we don't limit the columns to just three.

``` 
maryland_ppp_with_naics <- maryland_ppp %>% left_join(naics_codes)
```

    ## Joining, by = "naics_code"

Now, with our joined data, we can answer questions in a more useful way. But joins can do even more than just provide lookups; they can bring in additional data to enable you to ask more sophisticated questions.

Let's try adding zip code demographic data to the mix. Using [a file from the state's data catalog](https://umd.box.com/s/2xsq2rpkmg4ct3a77vt8j5bu4vu1z0tf), we can read it into R:

``` 
maryland_zcta <- read_csv('data/maryland_zcta.csv')
```

    ## 
    ## ── Column specification ────────────────────────────────────────────────────────
    ## cols(
    ##   .default = col_double(),
    ##   FIRST_CLAS = col_character(),
    ##   FIRST_MTFC = col_character(),
    ##   FIRST_FUNC = col_character(),
    ##   REPORT_2_P = col_character(),
    ##   REPORT_9_P = col_character()
    ## )
    ## ℹ Use `spec()` for the full column specifications.

You'll want to keep open the [data documentation](https://geodata.md.gov/imap/rest/services/Demographics/MD_CensusData/FeatureServer/1) that hosts the data, because the field names are abbreviations.

Note that this file describes Zip Code Tabulation Areas, which are very similar to but not always identical to zip codes (there's a [good explanation from the Census Bureau](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/zctas.html)). Bottom line: "In most instances the ZCTA code is the same as the ZIP Code for an area."

Again, we can use a `left_join` to make our demographic data available. This time we'll need to specify the two fields to join because they do not have identical names. We'll use `zip` from our PPP data and `ZCTA5N` from the demographic data:

``` 
maryland_ppp_with_naics_and_demographics <- maryland_ppp_with_naics %>% left_join(maryland_zcta, by=c("zip"="ZCTA5N"))
```

    ## Error: Can't join on `x$zip` x `y$zip` because of incompatible types.
    ## ℹ `x$zip` is of type <character>>.
    ## ℹ `y$zip` is of type <double>>.

You probably got an error when running that:

Error: Can't join on `x$zip` x `y$zip` because of incompatible types. ℹ `x$zip` is of type `<character>`{=html}\>. ℹ `y$zip` is of type `<double>`{=html}\>

Let's unpack this: R is saying it can't join those two columns because one of them is a character column and the other is a double (number) column. When joining, *the two columns need to have the same data type*.

We can fix that using our pal `mutate`. Let's change the ZCTA data to be a character, since zip codes aren't really useful as numbers (nobody needs to know the average zip code value).

``` 
maryland_zcta <- maryland_zcta %>% mutate(across(ZCTA5N, as.character))
```

Now we can re-run the join:

``` 
maryland_ppp_with_naics_and_demographics <- maryland_ppp_with_naics %>% left_join(maryland_zcta, by=c("zip"="ZCTA5N"))

maryland_ppp_with_naics_and_demographics
```

    ## # A tibble: 195,869 x 95
    ##         id name  amount state address city  zip   naics_code business_type race 
    ##      <dbl> <chr>  <dbl> <chr> <chr>   <chr> <chr>      <dbl> <chr>         <chr>
    ##  1  9.38e7 BAYW… 2   e6 MD    9130 G… Colu… 2104…     721110 Corporation   Unan…
    ##  2  9.38e7 PART… 1.09e6 MD    4857 W… Lanh… 2070…     238210 Corporation   Unan…
    ##  3  9.38e7 RP3 … 7.88e5 MD    7250 W… Beth… 2081…     541810 Limited  Lia… Unan…
    ##  4  9.38e7 SUSH… 6.56e5 MD    5455 W… Chev… 2081…     722511 Limited  Lia… Unan…
    ##  5  9.38e7 VILL… 4.70e5 MD    8601 A… Capi… 2074…     611110 Limited  Lia… Unan…
    ##  6  9.38e7 GOSH… 3.46e5 MD    4310 P… Bren… 2072…     721199 Limited  Lia… Blac…
    ##  7  9.38e7 WEAV… 3.31e5 MD    389 De… Trac… 2077…     336612 Corporation   Unan…
    ##  8  9.38e7 BOBS… 3.18e5 MD    100 Ey… Essex 2122…     238290 Corporation   Unan…
    ##  9  9.38e7 PARE… 2.84e5 MD    1641 W… Anna… 2140…     611110 Non-Profit O… Unan…
    ## 10  9.38e7 HARV… 2.42e5 MD    680 Pr… Prin… 2067…     722511 Limited  Lia… Asian
    ## # … with 195,859 more rows, and 85 more variables: gender <chr>, veteran <chr>,
    ## #   non_profit <lgl>, jobs_retained <dbl>, date_approved <dttm>, lender <chr>,
    ## #   congressional_district <chr>, loan_number <dbl>, sba_office_code <dbl>,
    ## #   processing_method <chr>, loan_status <chr>, term <dbl>,
    ## #   sba_guaranty_percentage <dbl>, initial_approval_amount <dbl>,
    ## #   current_approval_amount <dbl>, undisbursed_amount <dbl>,
    ## #   franchise_name <chr>, servicing_lender_location_id <dbl>,
    ## #   servicing_lender_name <chr>, servicing_lender_address <chr>,
    ## #   servicing_lender_city <chr>, servicing_lender_state <chr>,
    ## #   servicing_lender_zip <chr>, rural_urban_indicator <chr>,
    ## #   hubzone_indicator <chr>, business_age_description <chr>,
    ## #   project_city <chr>, project_county_name <chr>, project_state <chr>,
    ## #   project_zip <chr>, utilities_proceed <dbl>, payroll_proceed <dbl>,
    ## #   mortgage_interest_proceed <dbl>, rent_proceed <dbl>,
    ## #   refinance_eidl_proceed <dbl>, health_care_proceed <dbl>,
    ## #   debt_interest_proceed <dbl>, originating_lender_city <chr>,
    ## #   originating_lender_state <chr>, loan_status_date <date>,
    ## #   originating_lender_location_id <dbl>, lmi_indicator <chr>, ethnicity <chr>,
    ## #   forgiveness_amount <dbl>, forgiveness_date <date>, title <chr>,
    ## #   OBJECTID_1 <dbl>, ZCTA5CE10 <dbl>, FIRST_STAT <dbl>, FIRST_GEOI <dbl>,
    ## #   FIRST_CLAS <chr>, FIRST_MTFC <chr>, FIRST_FUNC <chr>, STATE <dbl>,
    ## #   AREALAND <dbl>, AREAWATR <dbl>, POP100 <dbl>, HU100 <dbl>, NHW <dbl>,
    ## #   NHB <dbl>, NHAI <dbl>, NHA <dbl>, NHNH <dbl>, NHO <dbl>, NHT <dbl>,
    ## #   HISP <dbl>, PNHW <dbl>, PNHB <dbl>, PNHAI <dbl>, PNHA <dbl>, PNHNH <dbl>,
    ## #   PNHO <dbl>, PNHT <dbl>, PHISP <dbl>, POP65_ <dbl>, PCTPOP65_ <dbl>,
    ## #   MEDAGE <dbl>, VACNS <dbl>, PVACNS <dbl>, PHOWN <dbl>, PWOMORT <dbl>,
    ## #   PRENT <dbl>, PLT18SP <dbl>, REPORT_2_P <chr>, REPORT_9_P <chr>

Now, if you use the tiny black right arrows to see what's in those demographic columns, you'll see ... a lot of NAs. What's going on there? Are there zip codes in the PPP data that aren't in the ZCTA data? If you go back using the left arrows, you can see that the PPP zip codes often are zip+4, and we're using the ZCTA5N field to join, which is a 5-character field. But not all of the PPP codes are zip+4. So we'll need to use `mutate` once more to give us a PPP zip field that is exactly 5 characters. Let's do this on the original `maryland` dataframe so we can then do the join using our new `zip5` field:

``` 
maryland_ppp_with_naics <- maryland_ppp_with_naics %>% mutate(zip5 = str_sub(zip, 1, 5))
maryland_ppp_with_naics_and_demographics <- maryland_ppp_with_naics %>% left_join(maryland_zcta, by=c("zip5"="ZCTA5N"))
```

Now we've got PPP data and demographic data by zip code. That means we can draw from both datasets in asking our questions. For example, we could see the mean and median loan amount in zip codes with different demographic characteristics. Let's start with zip codes that have more than 50 percent non-Hispanic Black population.

We get this by using filter followed by summarize. In this case, we want PNHB \> 50:

``` 
maryland_ppp_with_naics_and_demographics %>%
  filter(PNHB > 50) %>%
  summarize(
    count = n(),
    avgamount = mean(amount),
    medamount = median(amount))
```

    ## # A tibble: 1 x 3
    ##   count avgamount medamount
    ##   <int>     <dbl>     <dbl>
    ## 1 44032    53836.     20000

According to our query, there were 44,032 loans approved in zip codes with more than 50 percent non-Hispanic Black population, and the average amount was \$53,836 and the median amount was \$20,000.

Let's change that to zip codes with more than 50 percent non-Hispanic white population:

``` 
maryland_ppp_with_naics_and_demographics %>%
  filter(PNHW > 50) %>%
  summarize(
    count = n(),
    avgamount = mean(amount),
    medamount = median(amount))
```

    ## # A tibble: 1 x 3
    ##    count avgamount medamount
    ##    <int>     <dbl>     <dbl>
    ## 1 113937    88140.     20833

And we get a greater number of loans with a higher average and median amount. But that's not the end of the story, or of our questions. We'll need to ask more.

Let's break this down one more step. What if we added `rural_urban_indicator` -- if the loan recipient is located in a rural or urban area -- as a group_by. Does that change anything for the previous queries?

``` 
maryland_ppp_with_naics_and_demographics %>%
  filter(PNHB > 50) %>%
  group_by(rural_urban_indicator) %>%
  summarize(
    count = n(),
    avgamount = mean(amount),
    medamount = median(amount))
```

    ## # A tibble: 2 x 4
    ##   rural_urban_indicator count avgamount medamount
    ##   <chr>                 <int>     <dbl>     <dbl>
    ## 1 R                       148    44329.     19621
    ## 2 U                     43884    53869.     20000

``` 
maryland_ppp_with_naics_and_demographics %>%
  filter(PNHW > 50) %>%
  group_by(rural_urban_indicator) %>%
  summarize(
    count = n(),
    avgamount = mean(amount),
    medamount = median(amount))
```

    ## # A tibble: 2 x 4
    ##   rural_urban_indicator count avgamount medamount
    ##   <chr>                 <int>     <dbl>     <dbl>
    ## 1 R                     18337    73694.     20833
    ## 2 U                     95600    90911.     20833

In both cases, urban applicants got more approvals for higher average and median amounts, and the gap between majority-white zip codes and majority-Black zip codes was larger for urban applicants than for rural ones.

Joining datasets allows you to expand the range and sophistication of questions you're able to ask. It is one of the most powerful tools in a journalist's toolkit.

`<!--chapter:end:13-merging.Rmd-->`{=html}


#  Scraping data with Rvest {number="15"}

Sometimes, governments put data online on a page or in a searchable database. And when you ask them for a copy of the data underneath the website, they say no.

Why? Because they have a website. That's it. That's their reason. They say they don't have to give you the data because they've already given you the data, never mind that they haven't given to you in a form you can actually load into R with ease.

Lucky for us, there's a way for us to write code to get data even when an agency hasn't made it easy: webscraping.

One of the most powerful tools you can learn as a data journalist is how to scrape data from the web. Scraping is the process of programming a computer to act like a human that opens a web browser, goes to a website, ingests the HTML from that website into R and turns it into data.

The degree of difficulty here goes from "Easy" to "So Hard You Want To Throw Your Laptop Out A Window." And the curve between the two can be steep. You can learn how to scrape "Easy" in a day. The hard ones take a little more time, but it's often well worth the effort because it lets you get stories you couldn't get without it.

In this chapter, we'll show you an easy one. And in the next chapter, we'll so you a moderately harder one.

Let's start easy.

We're going to use a library called `rvest`, which you can install it the same way we've done all installs: go to the console and `install.packages("rvest")`.

Like so many R package names, rvest is a bad pun. You're supposed to read it to sound like "harvest," as in "harvesting" information from a website the same way you'd harvest crops in a field.

We'll load these packages first:

``` 
library(rvest)
```

    ## 
    ## Attaching package: 'rvest'

    ## The following object is masked from 'package:readr':
    ## 
    ##     guess_encoding

``` 
library(tidyverse)
library(janitor)
```

For this example, we're going to work on loading a simple table of data from the Bureau of Labor Statistics. This is a table of industry sectors (each with a two-digit NAICS code) that we could make use of in our analysis of PPP loan data.

Recall that our PPP loan data has six-digit NAICS codes for each industry, which allows us to identify the industry for each loan. For example 212221 is the code for "Gold Mining Industry."

A six-digit NAICS code is the most specific. As we remove numbers from the right to create five-digit, four-digit, three-digit and two-digit codes, the industries they represent get broader. Here's an example:

- 212221 - Gold Mining Industry
- 2122 - Metal Ore Mining Industry (which includes gold mining and things like silver mining, iron mining and copper mining)
- 21 - Mining, Quarrying, and Oil and Gas Extraction Industry (which contains the metal mining industries mentioned above, but also oil drilling, coal mining and more).

It might be useful to have a lookup table of those top-level, two-digit NAICS codes (also called sector codes) for our analysis, to help us answer questions about what specific top-level industries got loans. L

Let's suppose we can't find a table like that for download, but we do see a version on the BLS website at this URL: <https://www.bls.gov/ces/naics/>.


Or, we could write a few lines of webscraping code to have R do that for us!

In this simple example, it's probably faster to do it manually than have R do it for us. And this table is unlikely to change much in the future.

Why would we ever write code to grab a single table? There's several reasons:

1.  Our methods are transparent. If a colleague wants to run our code from scratch to factcheck our work, they don't need to repeat the manual steps, which are harder to document than writing code.
2.  Let's suppose we wanted to grab the same table every day, to monitor for changes (like, say, a table on a health department website that has COVID case numbers that update every day). Writing a script once, and pressing a single button every day is going to be much more efficient than doing this manually every day.
3.  If we're doing it manually, we're more likely to make a mistake, like maybe failing to copy every row from the whole table.
4.  It's good practice to prepare us to do more complex scraping jobs. As we'll see in the next chapter, if we ever want to grab the same table from hundreds of pages, writing code is much faster and easier than going to a hundred different pages ourselves and downloading data.

So, to scrape, the first thing we need to do is start with the URL. Let's store it as an object called naics_url.

``` 
naics_url <- "https://www.bls.gov/ces/naics/"
```

When we go to the web page, we can see a nicely-designed page that contains our information.

But what we really care about, for our purposes, is the html code that creates that page.

In our web browser, if we right-click anywhere on the page and select "view source" from the popup menu, we can see the source code. Or you can just copy this into Google Chrome: <view-source:https://www.bls.gov/ces/naics/>.

Here's a picture of what some of the source code looks like.


Okay, step 1.

Let's write a bit of code to tell R to go to the URL for the page and ingest all of that HTML code. In the code below, we're starting with our URL and using the read_html() function from rvest to ingest all of the page html, storing it as an object called naics_industry.

``` 

# read in the html 
naics_industry <- naics_url %>%
  read_html() 

# display the html below
naics_industry
```

    ## {html_document}
    ## <html lang="en-us">
    ## [1] <head>\n<meta http-equiv="Content-Type" content="text/html; charset=UTF-8 ...
    ## [2] <body class="layout-fixed">\n\t\t\t\t<!-- P ...

If you're running this code in R Studio, in our environment window at right, you'll see naics_industry as a "list of 2."

This is not a dataframe, it's a different type of data structure a "nested list."

If we click on the name "naics_industry" in our environment window, we can see that it's pulled in the html and shown us the general page structure. Nested within the `<html>` tag is the `<head>` and `<body>`, the two fundamental sections of most web pages. We're going to pull information out of the `<body>` tag in a bit.


Now, our task is to just pull out the section of the html that contains the information we need.

But which part do we need from that mess of html code? To figure that out, we can go back to the page in a web browser like chrome, and use built in developer tools to "inspect" the html code underlying the page.

On the page, find the data we want to grab -- "Table 2. NAICS Sectors" - and right click on the word "Sector" in the column header of the table. That will bring up a dropdown menu. Select "Inspect," which will pop up a window called the "element inspector" that shows us where different elements on the page are located, what html tags created those elements, and other info.


The entire table that we want of naics sectors is actually contained inside an html `<table>`. It has a header row `<thead>` that contains the column names and a `<tbody>` that contains one row `<tr>` per industry sector code.

Because it's inside of a table, and not some other kind of element (like a ``), rvest has a special function for easily extracting and converting html tables, called html_table(). This function extracts all six html tables on the page, only one of which we actually want

``` 

# read in the html and extract all the tables
naics_industry <- naics_url %>%
  read_html() %>%
  html_table()

# display the tables below
naics_industry
```

    ## [[1]]
    ## # A tibble: 4 x 3
    ##   Conversion               `Reference Month Implemented` `Date Released` 
    ##   <chr>                    <chr>                         <chr>           
    ## 1 SIC to NAICS 2002        May 2003                      June 6, 2003    
    ## 2 NAICS 2002 to NAICS 2007 January 2008                  February 1, 2008
    ## 3 NAICS 2007 to NAICS 2012 January 2012                  February 3, 2012
    ## 4 NAICS 2012 to NAICS 2017 January 2018                  February 2, 2018
    ## 
    ## [[2]]
    ## # A tibble: 21 x 2
    ##    Sector Description                                  
    ##    <chr>  <chr>                                        
    ##  1 11     Agriculture, Forestry, Fishing and Hunting   
    ##  2 21     Mining, Quarrying, and Oil and Gas Extraction
    ##  3 22     Utilities                                    
    ##  4 23     Construction                                 
    ##  5 31-33  Manufacturing                                
    ##  6 42     Wholesale Trade                              
    ##  7 44-45  Retail Trade                                 
    ##  8 48-49  Transportation and Warehousing               
    ##  9 51     Information                                  
    ## 10 52     Finance and Insurance                        
    ## # … with 11 more rows
    ## 
    ## [[3]]
    ## # A tibble: 11 x 2
    ##    Division                        Description                                  
    ##    <chr>                           <chr>                                        
    ##  1 A                               Agriculture, Forestry, And Fishing           
    ##  2 B                               Mining                                       
    ##  3 C                               Construction                                 
    ##  4 D                               Manufacturing                                
    ##  5 E                               Transportation, Communications, Electric, Ga…
    ##  6 F                               Wholesale Trade                              
    ##  7 G                               Retail Trade                                 
    ##  8 H                               Finance, Insurance, And Real Estate          
    ##  9 I                               Services                                     
    ## 10 J                               Public Administration                        
    ## 11 Source: www.osha.gov/pls/imis/… Source: www.osha.gov/pls/imis/sic_manual.html
    ## 
    ## [[4]]
    ## # A tibble: 6 x 6
    ##   SIC              SIC     SIC        NAICS          NAICS  NAICS   
    ##   <chr>            <chr>   <chr>      <chr>          <chr>  <chr>   
    ## 1 "Level"          "Code1" "Example2" Level          Code1  Example2
    ## 2 "Division"       "Alpha" "D"        Sector         XX     31      
    ## 3 "Major Group"    "XX"    "20"       Subsector      XXX    311     
    ## 4 "Industry Group" "XXX"   "203"      Industry Group XXXX   3114    
    ## 5 "Industry"       "XXXX"  "2037"     NAICS Industry XXXXX  31141   
    ## 6 ""               ""      ""         U.S. Industry  XXXXXX 311411  
    ## 
    ## [[5]]
    ## # A tibble: 4 x 4
    ##   Positions `Example Value` `Field Name`             `All Possible Values`    
    ##   <chr>     <chr>           <chr>                    <chr>                    
    ## 1 1-2       CE              Survey Abbreviation      CE                       
    ## 2 3         U               Seasonal Adjustment Code S,U                      
    ## 3 4-11      31335311        Industry Code            00000000 through 90932999
    ## 4 12-13     01              Data Type Code           01 through 99            
    ## 
    ## [[6]]
    ## # A tibble: 4 x 4
    ##   Positions `Example Value` `Field Name`             `All Possible Values`
    ##   <chr>     <chr>           <chr>                    <chr>                
    ## 1 1-2       EE              Survey Abbreviation      EE                   
    ## 2 3         S               Seasonal Adjustment Code S,U                  
    ## 3 4-9       000000          Industry Code            000000 through 959000
    ## 4 10-11     01              Data Type Code           01 through 83

In the environment window at right, look at naics_industry. Note that it's now a "list of 6."

Click on it to open it up. It should look like this.


They're numbered 1 to 6. The first 1 has 4 rows and 3 columns, the second has 21 rows and 2 columns, and so on.

To examine what's in each dataframe, mouse over the right edge (next to the word columns) on each row, and click the little scroll icon. The icon will be hidden until you mouse over it.

Click on the scroll icon for the first dataframe examine it.


That's not the one we want!

Let's try clicking on the scroll icon for row 2.


That's more like it! So, all we need to do now is to store that single dataframe as an object, and get rid of the rest. We can do that with this code, which says \"keep only the second dataframe from our nested list. If we wanted to keep the third one, we'd change the number 2 to number 3.

``` 

# Read in all html from table, store all tables on page as nested list of dataframes.
naics_industry  <- naics_url %>%
  read_html() %>%
  html_table()

# Just keep the second dataframe in our list

naics_industry <- naics_industry[[2]]


# show the dataframe

naics_industry
```

    ## # A tibble: 21 x 2
    ##    Sector Description                                  
    ##    <chr>  <chr>                                        
    ##  1 11     Agriculture, Forestry, Fishing and Hunting   
    ##  2 21     Mining, Quarrying, and Oil and Gas Extraction
    ##  3 22     Utilities                                    
    ##  4 23     Construction                                 
    ##  5 31-33  Manufacturing                                
    ##  6 42     Wholesale Trade                              
    ##  7 44-45  Retail Trade                                 
    ##  8 48-49  Transportation and Warehousing               
    ##  9 51     Information                                  
    ## 10 52     Finance and Insurance                        
    ## # … with 11 more rows

We now have a proper dataframe.

From here, we can do a little light cleaning. Let's use clean_names() to standardize the column names. Then let's use slice() to remove the last row -- row number 21 -- which contains source information that will complicate our use of this table later.

``` 
# Read in all html from table, store all tables on page as nested list of dataframes.
naics_industry <- naics_url %>%
  read_html() %>%
  html_table()


# Just keep the second dataframe in our list, standardize column headers, remove last row

naics_industry <- naics_industry[[2]] %>%
  clean_names() %>%
  slice(-21)

# show the dataframe
naics_industry
```

    ## # A tibble: 20 x 2
    ##    sector description                                                           
    ##    <chr>  <chr>                                                                 
    ##  1 11     Agriculture, Forestry, Fishing and Hunting                            
    ##  2 21     Mining, Quarrying, and Oil and Gas Extraction                         
    ##  3 22     Utilities                                                             
    ##  4 23     Construction                                                          
    ##  5 31-33  Manufacturing                                                         
    ##  6 42     Wholesale Trade                                                       
    ##  7 44-45  Retail Trade                                                          
    ##  8 48-49  Transportation and Warehousing                                        
    ##  9 51     Information                                                           
    ## 10 52     Finance and Insurance                                                 
    ## 11 53     Real Estate and Rental and Leasing                                    
    ## 12 54     Professional, Scientific, and Technical Services                      
    ## 13 55     Management of Companies and Enterprises                               
    ## 14 56     Administrative and Support and Waste Management and Remediation Servi…
    ## 15 61     Educational Services                                                  
    ## 16 62     Health Care and Social Assistance                                     
    ## 17 71     Arts, Entertainment, and Recreation                                   
    ## 18 72     Accommodation and Food Services                                       
    ## 19 81     Other Services (except Public Administration)                         
    ## 20 92     Public Administration

And there we go. We now have a nice tidy dataframe of NAICS sector codes.

In the next chapter, we'll look at a more complicated example.

`<!--chapter:end:14-rvest.Rmd-->`{=html}



#  Advanced rvest {number="16"}

In the last chapter, we demonstrated a fairly straightforward example of web scraping to grab a list of NAICS industry sector codes from the BLS website.

We're going to graduate to a more challenging example, one that will help us gather information about the number of employees in each industry sector.

What makes this more challenging? Well, the information we need is all contained on multiple pages, one page per sector. We need to write code to visit each page, and then merge them into a single data frame.

This is challenging stuff, so don't feel dissuaded if it all doesn't click the first time through. Like many things, web scraping is something that gets easier with lots of practice.

First we start with libraries, as we always do.

``` 
library(tidyverse)
library(rvest)
library(janitor)
```

Now, let's run the code we wrote in the last chapter, to get a tidy list of NAICS sector codes and names from [https://www.bls.gov/ces/naics/](%22https://www.bls.gov/ces/naics/%22).

``` 
# Define url of page we want to scrape

naics_url <- "https://www.bls.gov/ces/naics/"


# Read in all html from table, store all tables on page as nested list of dataframes.
naics_industry  <- naics_url %>%
  read_html() %>%
  html_table()

# Just keep the second dataframe in our list, standardize column headers, remove last row

naics_industry <- naics_industry[[2]] %>%
  clean_names() %>%
  slice(-21)


# show the dataframe
naics_industry
```

    ## # A tibble: 20 x 2
    ##    sector description                                                           
    ##    <chr>  <chr>                                                                 
    ##  1 11     Agriculture, Forestry, Fishing and Hunting                            
    ##  2 21     Mining, Quarrying, and Oil and Gas Extraction                         
    ##  3 22     Utilities                                                             
    ##  4 23     Construction                                                          
    ##  5 31-33  Manufacturing                                                         
    ##  6 42     Wholesale Trade                                                       
    ##  7 44-45  Retail Trade                                                          
    ##  8 48-49  Transportation and Warehousing                                        
    ##  9 51     Information                                                           
    ## 10 52     Finance and Insurance                                                 
    ## 11 53     Real Estate and Rental and Leasing                                    
    ## 12 54     Professional, Scientific, and Technical Services                      
    ## 13 55     Management of Companies and Enterprises                               
    ## 14 56     Administrative and Support and Waste Management and Remediation Servi…
    ## 15 61     Educational Services                                                  
    ## 16 62     Health Care and Social Assistance                                     
    ## 17 71     Arts, Entertainment, and Recreation                                   
    ## 18 72     Accommodation and Food Services                                       
    ## 19 81     Other Services (except Public Administration)                         
    ## 20 92     Public Administration

We'll use this table to help us get to our end goal: a single dataframe with the number of employees in each industry sector.

It will look like this when we're done.


Unfortunately, that information doesn't exist in a single tidy table on a single page we can scrape all at once. We're going to have to scrape it from lots of different pages, and build it ourselves.

Let's next take a look at the web page that has detailed employment information for one of our sectors, 22, Mining, Quarrying, and Oil and Gas Extraction.

We can find it here: <https://www.bls.gov/iag/tgs/iag22.htm>.

A few scrolls down the page, there's a table that has employee statistics.

The table is called "Employment and Unemployment." There's a row in the tabled for "Employment, all employees (seasonally adjusted)." And in that row, there's a value for the number of employees -- in thousands -- in June 2021.

The table shows that for the mining sector, it was 538.6 -- or 538,600 -- in June 2021. That's the value we want to ingest in R.


We don't just want it for mining. We want it for all sectors!

But we'll start by writing code just to get it from this one sector page, then modify that code to get it from every sector's page

First, let's define the URL of the page we want to get the information from.

``` 
# Define url of the page we want to get
url <- "https://www.bls.gov/iag/tgs/iag22.htm"
```

Next, let's read in the html of that page, and store it as an object called employment_info.

``` 

# Define url of the page we want to get
url <- "https://www.bls.gov/iag/tgs/iag22.htm"

# Get employment html
employment_info <- url %>%
  read_html()  


# Display it so we can see what it looks like
employment_info
```

    ## {html_document}
    ## <html lang="en">
    ## [1] <head>\n<meta http-equiv="Content-Type" content="text/html; charset=UTF-8 ...
    ## [2] <body>\r\n<!-- ****************************************** Begin HEADER ** ...

Now, let's set to picking out the information we need from the raw html.

We can use the web inspector in our web browser (Chrome) to figure out where the table is located.

Go to the web page and right click on the word "Data Series" in the table, then pick "inspect" to pull up the menu.

Notice two things. First, all of this information is contained in a proper html `<table>`. And that table has an id property of "iag22emp1." Designers use these IDs to help style the page, to target certain elements with CSS. We can use it to scrape.


Here, we can use that id property to pick out just the table we want, and leave all the others behind. We do that with a new function from rvest called html_element(), employing a bit of information about that element stored in what's called the [xpath](https://en.wikipedia.org/wiki/XPath). Xpath is a query language that helps us write programs that target specific parts of web pages.

The syntax is a little unwieldy, I know.

But essentially what the html_element function says is "find the html element that has an id of iag22emp1, using the xpath method, and get rid of all other elements."

``` 
# Define url of the page we want to get
url <- "https://www.bls.gov/iag/tgs/iag22.htm"


# Get employment html page and select only the table with employment information
employment_info <- url %>%
  read_html() %>%
  html_element(xpath = '//*[@id="iag22emp1"]')

# Display it so we can see what it looks like
employment_info
```

    ## {html_node}
    ## <table class="regular" id="iag22emp1">
    ## [1] <caption></caption>
    ## [2] <thead><tr>\n<th class="stubhead" id="iag22emp1.h.1.1">Data series</th>\r ...
    ## [3] <tbody>\n<tr>\n<th headers="iag22emp1.h.1.1" id="iag22emp1.r.1"><p class= ...
    ## [4] <tfoot><tr class="footnotes">\n<td class="footnotes" colspan="6">\r\n\t<p ...

We've now isolated the table on the page that contains the information we need, and gotten rid of everything else.

From here, we can use the html_tables() function to transform it from messy html code to a proper dataframe.

``` 

# Define url of the page we want to get
url <- "https://www.bls.gov/iag/tgs/iag22.htm"

# Get employment html page and select only the table with employment information, then transform it from html to a table.
employment_info <- url %>%
  read_html() %>%
  html_element(xpath = '//*[@id="iag22emp1"]') %>%
  html_table() 


# Display it so we can see what it looks like
employment_info
```

    ## # A tibble: 6 x 6
    ##   `Data series`          Backdata    Jul.2021   Aug.2021   Sep.2021   Oct.2021  
    ##   <chr>                  <chr>       <chr>      <chr>      <chr>      <chr>     
    ## 1 Employment (in thousa… ""          ""         ""         ""         ""        
    ## 2 Employment, all emplo… ""          "538.9"    "536.7"    "(p)536.5" "(p)536.7"
    ## 3 Employment, productio… ""          "429.1"    "426.9"    "(p)426.8" "(p)427.4"
    ## 4 Unemployment           ""          ""         ""         ""         ""        
    ## 5 Unemployment rate      ""          "3.4%"     "2.7%"     "3.1%"     "1.8%"    
    ## 6 Footnotes(p) Prelimin… "Footnotes… "Footnote… "Footnote… "Footnote… "Footnote…

Now we have a proper dataframe of 6 rows and 6 columns.

It has much more information than we need, so let's clean it up to isolate only the "Employment, all employees (seasonally adjusted)" value for June 2021.

Use clean_names() to standardize the column names, use slice() to keep only the second row, and use select() to keep two columns data_series and jul_2021.

``` 
# Define url of the page we want to get
url <- "https://www.bls.gov/iag/tgs/iag21.htm"


# Get employment html page and select only the table with employment information, then transform it from html to a table.
employment_info <- url %>%
  read_html() %>%
  html_element(xpath = '//*[@id="iag21emp1"]') %>%
  html_table() 

# Keep only second row with seasonally adjusted, bind back to each_row_df
employment_info <- employment_info %>%
  clean_names() %>%
  slice(2) %>%
  select(data_series, jul_2021)


# Display it so we can see what it looks like
employment_info
```

    ## # A tibble: 1 x 2
    ##   data_series                                      jul_2021
    ##   <chr>                                            <chr>   
    ## 1 Employment, all employees  (seasonally adjusted) 592.5

Okay, so we've successfully obtained the employment numbers for one of our sectors. That's great.

But remember our original charge: to get a table with employment numbers for ALL sectors, not just one.

This is a little tricky, because, remember, the information for each sector is on a different page!

The info for mining is on this page: <https://www.bls.gov/iag/tgs/iag21.htm>.

The info for construction is on this page: <https://www.bls.gov/iag/tgs/iag23.htm>.

We have 20 sectors to get through.

We could get the info we need by copying the codeblock we just wrote 20 times, and change the url at the top each time.

But that's not a great approach.

What if we needed to change the code? We'd need to change it 20 times!

In programming, there's a principle called "DRY" which stands for "Don't Repeat Yourself." If you find yourself copying the same code over and over again, with minor changes, it's better to find a way to avoid that.

## 16.1 Using for loops {number="16.1"}

Fortunately, there's a programming paradigm called "iteration" that is helpful here, using a method called a "for loop."

Every programming language has its own version of a "for loop," and R is no different.

A "for loop" says: "let's take a list of things, and do the same thing to each item on that list."

Let's look at a very simple example to help illustrate the values of for loops.

We're going to write code to print out 10 industry sectors.

First, let's do it the repetitive way. We're writing the same print function over and over, just changing the sector name each time.

``` 
print("Agriculture, Forestry, Fishing and Hunting")
```

    ## [1] "Agriculture, Forestry, Fishing and Hunting"

``` 
print("Mining, Quarrying, and Oil and Gas Extraction")
```

    ## [1] "Mining, Quarrying, and Oil and Gas Extraction"

``` 
print("Utilities")
```

    ## [1] "Utilities"

``` 
print("Construction")
```

    ## [1] "Construction"

``` 
print("Manufacturing")
```

    ## [1] "Manufacturing"

``` 
print("Wholesale Trade")
```

    ## [1] "Wholesale Trade"

``` 
print("Retail Trade")
```

    ## [1] "Retail Trade"

``` 
print("Transportation and Warehousing")
```

    ## [1] "Transportation and Warehousing"

``` 
print("Information")
```

    ## [1] "Information"

``` 
print("Finance and Insurance")
```

    ## [1] "Finance and Insurance"

We repeated print() 10 times, with minor modifications each time. Lots of repetition, which we seek to avoid if possible.

Now let's look at how we might do that a little more efficiently with a "for loop."

First let's make a list of sectors, and save it as an object called "list_of_sectors." The c() function tells R that we're making a list.

``` 
list_of_sectors <- c("Agriculture, Forestry, Fishing and Hunting", "Mining, Quarrying, and Oil and Gas Extraction", "Utilities", "Construction", "Manufacturing",
"Wholesale Trade", "Retail Trade", "Transportation and Warehousing", "Information", "Finance and Insurance")
```

And now let's write a "for loop" to print out sector on that list.

``` 
# Define list of sectors
list_of_sectors <- c("Agriculture, Forestry, Fishing and Hunting", "Mining, Quarrying, and Oil and Gas Extraction", "Utilities", "Construction", "Manufacturing",
"Wholesale Trade", "Retail Trade", "Transportation and Warehousing", "Information", "Finance and Insurance")


# Make a for loop and run it
for (sector in list_of_sectors) {
  print(sector)
}
```

    ## [1] "Agriculture, Forestry, Fishing and Hunting"
    ## [1] "Mining, Quarrying, and Oil and Gas Extraction"
    ## [1] "Utilities"
    ## [1] "Construction"
    ## [1] "Manufacturing"
    ## [1] "Wholesale Trade"
    ## [1] "Retail Trade"
    ## [1] "Transportation and Warehousing"
    ## [1] "Information"
    ## [1] "Finance and Insurance"

That's many fewer lines of code. Let's break down what we just saw, starting with for `(sector in list_of sectors)`.

The information inside the parentheses tells R what list to use -- list_of_sectors -- and how to identify list elements later on -- sector.

It's important that the thing on the right side of "in" use the exact name of the list we want to loop through -- in this case "list_of_sectors."

If we try to feed it something different -- say "sector_list" -- it won't work, because our actual list is called something else -- "list_of_sectors." This code throws an error.

``` 
# Define list of sectors
list_of_sectors <- c("Agriculture, Forestry, Fishing and Hunting", "Mining, Quarrying, and Oil and Gas Extraction", "Utilities", "Construction", "Manufacturing",
"Wholesale Trade", "Retail Trade", "Transportation and Warehousing", "Information", "Finance and Insurance")


# For loop that refers to a list that doesn't exist!  
for (sector in sector_list) {
  print(sector)
}
```

    ## Error in eval(expr, envir, enclos): object 'sector_list' not found

The name on the left side of "in" -- the word we're assigning to represent each element -- is totally arbitrary.

We could use any character string, even something simple like "x."

What matters is that we use the same character string inside of the curly braces {}, the section of the "for loop" that tells R what to do to each element -- in this case, print it out.

To illustrate this, note that the code works just fine if we change it to say this:

``` 
# Define list of sectors
list_of_sectors <- c("Agriculture, Forestry, Fishing and Hunting", "Mining, Quarrying, and Oil and Gas Extraction", "Utilities", "Construction", "Manufacturing",
"Wholesale Trade", "Retail Trade", "Transportation and Warehousing", "Information", "Finance and Insurance")


# For loop with x that stands in for each element in our list, instead of sector 
for (x in list_of_sectors) {
  print(x)
}
```

    ## [1] "Agriculture, Forestry, Fishing and Hunting"
    ## [1] "Mining, Quarrying, and Oil and Gas Extraction"
    ## [1] "Utilities"
    ## [1] "Construction"
    ## [1] "Manufacturing"
    ## [1] "Wholesale Trade"
    ## [1] "Retail Trade"
    ## [1] "Transportation and Warehousing"
    ## [1] "Information"
    ## [1] "Finance and Insurance"

But it does NOT work if we call each element one thing -- x -- in the first line of our "for loop," and use a different name to refer to it inside of the curly braces.

In this code below, it has no idea what we mean by "sector_name," because we haven't defined that anywhere.

``` 
# Define list of sectors
list_of_sectors <- c("Agriculture, Forestry, Fishing and Hunting", "Mining, Quarrying, and Oil and Gas Extraction", "Utilities", "Construction", "Manufacturing",
"Wholesale Trade", "Retail Trade", "Transportation and Warehousing", "Information", "Finance and Insurance")


# For loop that includes instructions that refer to a variable that doesn't exist.
for (x in list_of_sectors) {
  print(sector_name)
}
```

    ## Error in print(sector_name): object 'sector_name' not found

We can also write for loops to iterate over a range of numbers, instead of a list of characters. The syntax is a little different.

The code below says: "for each number in a range of numbers from 1 to 10, print the number."

``` 
# For loop that includes instructions that refer to a variable that doesn't exist.
for (number in 1:10) {
  print(number)
}
```

    ## [1] 1
    ## [1] 2
    ## [1] 3
    ## [1] 4
    ## [1] 5
    ## [1] 6
    ## [1] 7
    ## [1] 8
    ## [1] 9
    ## [1] 10

Here's a minor variation on that approach that we'll make use of below.

Instead of giving the for loop an explicit number range, like 1:10, we can tell it to use 1 to "the number of rows in a dataframe" as our list of things to loop through.

Remember the naics_industry dataframe we loaded first? It has 20 rows.

``` 
naics_industry
```

    ## # A tibble: 20 x 2
    ##    sector description                                                           
    ##    <chr>  <chr>                                                                 
    ##  1 11     Agriculture, Forestry, Fishing and Hunting                            
    ##  2 21     Mining, Quarrying, and Oil and Gas Extraction                         
    ##  3 22     Utilities                                                             
    ##  4 23     Construction                                                          
    ##  5 31-33  Manufacturing                                                         
    ##  6 42     Wholesale Trade                                                       
    ##  7 44-45  Retail Trade                                                          
    ##  8 48-49  Transportation and Warehousing                                        
    ##  9 51     Information                                                           
    ## 10 52     Finance and Insurance                                                 
    ## 11 53     Real Estate and Rental and Leasing                                    
    ## 12 54     Professional, Scientific, and Technical Services                      
    ## 13 55     Management of Companies and Enterprises                               
    ## 14 56     Administrative and Support and Waste Management and Remediation Servi…
    ## 15 61     Educational Services                                                  
    ## 16 62     Health Care and Social Assistance                                     
    ## 17 71     Arts, Entertainment, and Recreation                                   
    ## 18 72     Accommodation and Food Services                                       
    ## 19 81     Other Services (except Public Administration)                         
    ## 20 92     Public Administration

We can use that information in our for loop by using the nrow() function, which calculates the number of rows in a dataframe. Here's a quick demonstration of how that works.

``` 
nrow(naics_industry)
```

    ## [1] 20

To put it all together, the code below says "make a list of numbers that starts at 1 and ends at the number of rows in the naics_industry dataframe (which is 20), then print out each of these numbers."

``` 

# For loop that includes instructions that refer to a variable that doesn't exist.
for (row_number in 1:nrow(naics_industry)) {
  print(row_number)
}
```

    ## [1] 1
    ## [1] 2
    ## [1] 3
    ## [1] 4
    ## [1] 5
    ## [1] 6
    ## [1] 7
    ## [1] 8
    ## [1] 9
    ## [1] 10
    ## [1] 11
    ## [1] 12
    ## [1] 13
    ## [1] 14
    ## [1] 15
    ## [1] 16
    ## [1] 17
    ## [1] 18
    ## [1] 19
    ## [1] 20

These were basic examples of how "for loops" work. Next, we'll learn to apply "for loops" to efficentily extract information from multiple web pages.

## 16.2 Looping and rvest {number="16.2"}

First, let's look at the codeblock we wrote earlier to extract the number of employees in the mining sector.

``` 
# Define url of the page we want to get
url <- "https://www.bls.gov/iag/tgs/iag21.htm"


# Get employment html page and select only the table with employment information, then transform it from html to a table.
employment_info <- url %>%
  read_html() %>%
  html_element(xpath = '//*[@id="iag21emp1"]') %>%
  html_table() 

# Keep only second row with seasonally adjusted, bind back to each_row_df
employment_info <- employment_info %>%
  clean_names() %>%
  slice(2) %>%
  select(data_series, jul_2021)


# Display it so we can see what it looks like
employment_info
```

    ## # A tibble: 1 x 2
    ##   data_series                                      jul_2021
    ##   <chr>                                            <chr>   
    ## 1 Employment, all employees  (seasonally adjusted) 592.5

This contains all the steps we needed to extract the information from one sector page. We're now going to modify this function so we can use it to extract information from each sector page, writing code that keeps us from repeating ourselves too much.\
First, we need to build a list of URLs to loop through in a "for loop." We can do that using the dataframe we made in the last chapter.

``` 
# Define url of page we want to scrape

naics_url <- "https://www.bls.gov/ces/naics/"


# Read in all html from table, store all tables on page as nested list of dataframes.
naics_industry  <- naics_url %>%
  read_html() %>%
  html_table()

# Just keep the second dataframe in our list, standardize column headers, remove last row

naics_industry <- naics_industry[[2]] %>%
  clean_names() %>%
  slice(-21)


# show the dataframe
naics_industry
```

    ## # A tibble: 20 x 2
    ##    sector description                                                           
    ##    <chr>  <chr>                                                                 
    ##  1 11     Agriculture, Forestry, Fishing and Hunting                            
    ##  2 21     Mining, Quarrying, and Oil and Gas Extraction                         
    ##  3 22     Utilities                                                             
    ##  4 23     Construction                                                          
    ##  5 31-33  Manufacturing                                                         
    ##  6 42     Wholesale Trade                                                       
    ##  7 44-45  Retail Trade                                                          
    ##  8 48-49  Transportation and Warehousing                                        
    ##  9 51     Information                                                           
    ## 10 52     Finance and Insurance                                                 
    ## 11 53     Real Estate and Rental and Leasing                                    
    ## 12 54     Professional, Scientific, and Technical Services                      
    ## 13 55     Management of Companies and Enterprises                               
    ## 14 56     Administrative and Support and Waste Management and Remediation Servi…
    ## 15 61     Educational Services                                                  
    ## 16 62     Health Care and Social Assistance                                     
    ## 17 71     Arts, Entertainment, and Recreation                                   
    ## 18 72     Accommodation and Food Services                                       
    ## 19 81     Other Services (except Public Administration)                         
    ## 20 92     Public Administration

This gives us the sector code and name for each industry.

Now let's have a look at the URLs for a few of the pages we want to grab data from.

- Mining, Quarrying, and Oil and Gas Extraction: <https://www.bls.gov/iag/tgs/iag21.htm>.
- Utilities: <https://www.bls.gov/iag/tgs/iag22.htm>.
- Construction: <https://www.bls.gov/iag/tgs/iag23.htm>

Notice a pattern?

They all start with "<https://www.bls.gov/iag/tgs/iag>." The next bit of information is different for each one; with the two-digit sector code for each sector. The remainder is identical in all three links, ".htm."

Because they're all the same, we can use the information in the dataframe we just loaded to make all the URLs we need.

We're going to use mutate() and paste0() to concatenate (mash together) the things that stay constant in every url (the beginning and end) with the things that are different (the sector number, stored in the column called sector).

``` 
# Make a column with URL for each sector. 
naics_industry <- naics_industry %>%
  mutate(sector_url = paste0("https://www.bls.gov/iag/tgs/iag",sector,".htm"))


# Display it
naics_industry
```

    ## # A tibble: 20 x 3
    ##    sector description                                  sector_url               
    ##    <chr>  <chr>                                        <chr>                    
    ##  1 11     Agriculture, Forestry, Fishing and Hunting   https://www.bls.gov/iag/…
    ##  2 21     Mining, Quarrying, and Oil and Gas Extracti… https://www.bls.gov/iag/…
    ##  3 22     Utilities                                    https://www.bls.gov/iag/…
    ##  4 23     Construction                                 https://www.bls.gov/iag/…
    ##  5 31-33  Manufacturing                                https://www.bls.gov/iag/…
    ##  6 42     Wholesale Trade                              https://www.bls.gov/iag/…
    ##  7 44-45  Retail Trade                                 https://www.bls.gov/iag/…
    ##  8 48-49  Transportation and Warehousing               https://www.bls.gov/iag/…
    ##  9 51     Information                                  https://www.bls.gov/iag/…
    ## 10 52     Finance and Insurance                        https://www.bls.gov/iag/…
    ## 11 53     Real Estate and Rental and Leasing           https://www.bls.gov/iag/…
    ## 12 54     Professional, Scientific, and Technical Ser… https://www.bls.gov/iag/…
    ## 13 55     Management of Companies and Enterprises      https://www.bls.gov/iag/…
    ## 14 56     Administrative and Support and Waste Manage… https://www.bls.gov/iag/…
    ## 15 61     Educational Services                         https://www.bls.gov/iag/…
    ## 16 62     Health Care and Social Assistance            https://www.bls.gov/iag/…
    ## 17 71     Arts, Entertainment, and Recreation          https://www.bls.gov/iag/…
    ## 18 72     Accommodation and Food Services              https://www.bls.gov/iag/…
    ## 19 81     Other Services (except Public Administratio… https://www.bls.gov/iag/…
    ## 20 92     Public Administration                        https://www.bls.gov/iag/…

While we're at it, we're going to use the same method to programatically build the "xpath" for the table on each sector page.

Recall that when we wrote our function that got information from just the mining page, the xpath targeted an element with an ID of "iag21emp1." Why 21? That's the sector code for mining.

If we look for that exact element ID on other sector pages, we won't find it! That's because it's different for each page.

On the Utilities page (sector code 22), the ID for the table we want is "iag22emp1." On the Construction page (sector code 23), it's "iag23emp1." We can also build this programatically, because it follows a predictable pattern.

``` 
# Make a column with URL and xpath ID for each sector
naics_industry <- naics_industry %>%
  mutate(sector_url = paste0("https://www.bls.gov/iag/tgs/iag",sector,".htm")) %>%
  mutate(sector_xpath_id =paste0("iag",sector,"emp1"))


# Display it
naics_industry
```

    ## # A tibble: 20 x 4
    ##    sector description                       sector_url           sector_xpath_id
    ##    <chr>  <chr>                             <chr>                <chr>          
    ##  1 11     Agriculture, Forestry, Fishing a… https://www.bls.gov… iag11emp1      
    ##  2 21     Mining, Quarrying, and Oil and G… https://www.bls.gov… iag21emp1      
    ##  3 22     Utilities                         https://www.bls.gov… iag22emp1      
    ##  4 23     Construction                      https://www.bls.gov… iag23emp1      
    ##  5 31-33  Manufacturing                     https://www.bls.gov… iag31-33emp1   
    ##  6 42     Wholesale Trade                   https://www.bls.gov… iag42emp1      
    ##  7 44-45  Retail Trade                      https://www.bls.gov… iag44-45emp1   
    ##  8 48-49  Transportation and Warehousing    https://www.bls.gov… iag48-49emp1   
    ##  9 51     Information                       https://www.bls.gov… iag51emp1      
    ## 10 52     Finance and Insurance             https://www.bls.gov… iag52emp1      
    ## 11 53     Real Estate and Rental and Leasi… https://www.bls.gov… iag53emp1      
    ## 12 54     Professional, Scientific, and Te… https://www.bls.gov… iag54emp1      
    ## 13 55     Management of Companies and Ente… https://www.bls.gov… iag55emp1      
    ## 14 56     Administrative and Support and W… https://www.bls.gov… iag56emp1      
    ## 15 61     Educational Services              https://www.bls.gov… iag61emp1      
    ## 16 62     Health Care and Social Assistance https://www.bls.gov… iag62emp1      
    ## 17 71     Arts, Entertainment, and Recreat… https://www.bls.gov… iag71emp1      
    ## 18 72     Accommodation and Food Services   https://www.bls.gov… iag72emp1      
    ## 19 81     Other Services (except Public Ad… https://www.bls.gov… iag81emp1      
    ## 20 92     Public Administration             https://www.bls.gov… iag92emp1

Lastly, we're going to use filter to remove the "Public Administration" sector, because there's no page for it. We'll have to get that information some other way.

``` 
# Make a column with URL and xpath ID for each sector, remove the Public Administration sector
naics_industry <- naics_industry %>%
  mutate(sector_url = paste0("https://www.bls.gov/iag/tgs/iag",sector,".htm")) %>%
  mutate(sector_xpath_id =paste0("iag",sector,"emp1")) %>%
  filter(description != "Public Administration")

# Display it
naics_industry
```

    ## # A tibble: 19 x 4
    ##    sector description                       sector_url           sector_xpath_id
    ##    <chr>  <chr>                             <chr>                <chr>          
    ##  1 11     Agriculture, Forestry, Fishing a… https://www.bls.gov… iag11emp1      
    ##  2 21     Mining, Quarrying, and Oil and G… https://www.bls.gov… iag21emp1      
    ##  3 22     Utilities                         https://www.bls.gov… iag22emp1      
    ##  4 23     Construction                      https://www.bls.gov… iag23emp1      
    ##  5 31-33  Manufacturing                     https://www.bls.gov… iag31-33emp1   
    ##  6 42     Wholesale Trade                   https://www.bls.gov… iag42emp1      
    ##  7 44-45  Retail Trade                      https://www.bls.gov… iag44-45emp1   
    ##  8 48-49  Transportation and Warehousing    https://www.bls.gov… iag48-49emp1   
    ##  9 51     Information                       https://www.bls.gov… iag51emp1      
    ## 10 52     Finance and Insurance             https://www.bls.gov… iag52emp1      
    ## 11 53     Real Estate and Rental and Leasi… https://www.bls.gov… iag53emp1      
    ## 12 54     Professional, Scientific, and Te… https://www.bls.gov… iag54emp1      
    ## 13 55     Management of Companies and Ente… https://www.bls.gov… iag55emp1      
    ## 14 56     Administrative and Support and W… https://www.bls.gov… iag56emp1      
    ## 15 61     Educational Services              https://www.bls.gov… iag61emp1      
    ## 16 62     Health Care and Social Assistance https://www.bls.gov… iag62emp1      
    ## 17 71     Arts, Entertainment, and Recreat… https://www.bls.gov… iag71emp1      
    ## 18 72     Accommodation and Food Services   https://www.bls.gov… iag72emp1      
    ## 19 81     Other Services (except Public Ad… https://www.bls.gov… iag81emp1

We're left with a dataframe of 19 rows and 4 columns. It now contains everything we need.

Next, we'll construct a "for loop" to extract the info we need from each page. We're going to build it up step-by-step, beginning with the the basic elements of our "for loop."

The codeblock below says: "Make a list with the row numbers from 1 to the number of rows in our naics_industry dataframe (which is 19). Then, for each element of that list (1, 2, 3, 4, 5 and so on up to 19), use slice() to keep only the one row that matches that number and save this newly created dataframe as each_row_df. Print out the dataframe. Then go to the next element on the list and do the same thing. Keep doing that until we hit number 19, then stop."

We get 19 dataframes, each with one row, one for each sector.

``` 
# For loop, iterating over each row in our naics industry dataframe

for(row_number in 1:nrow(naics_industry)) {
    
    # Keep only the row for a given row number, get rid of every other row
    each_row_df <- naics_industry %>%
      slice(row_number) 
    
    # To help us see what's happening as we build this, we're going to print the thing we're creating.  
    print(each_row_df)
      
}
```

    ## # A tibble: 1 x 4
    ##   sector description                   sector_url                sector_xpath_id
    ##   <chr>  <chr>                         <chr>                     <chr>          
    ## 1 11     Agriculture, Forestry, Fishi… https://www.bls.gov/iag/… iag11emp1      
    ## # A tibble: 1 x 4
    ##   sector description                    sector_url               sector_xpath_id
    ##   <chr>  <chr>                          <chr>                    <chr>          
    ## 1 21     Mining, Quarrying, and Oil an… https://www.bls.gov/iag… iag21emp1      
    ## # A tibble: 1 x 4
    ##   sector description sector_url                            sector_xpath_id
    ##   <chr>  <chr>       <chr>                                 <chr>          
    ## 1 22     Utilities   https://www.bls.gov/iag/tgs/iag22.htm iag22emp1      
    ## # A tibble: 1 x 4
    ##   sector description  sector_url                            sector_xpath_id
    ##   <chr>  <chr>        <chr>                                 <chr>          
    ## 1 23     Construction https://www.bls.gov/iag/tgs/iag23.htm iag23emp1      
    ## # A tibble: 1 x 4
    ##   sector description   sector_url                               sector_xpath_id
    ##   <chr>  <chr>         <chr>                                    <chr>          
    ## 1 31-33  Manufacturing https://www.bls.gov/iag/tgs/iag31-33.htm iag31-33emp1   
    ## # A tibble: 1 x 4
    ##   sector description     sector_url                            sector_xpath_id
    ##   <chr>  <chr>           <chr>                                 <chr>          
    ## 1 42     Wholesale Trade https://www.bls.gov/iag/tgs/iag42.htm iag42emp1      
    ## # A tibble: 1 x 4
    ##   sector description  sector_url                               sector_xpath_id
    ##   <chr>  <chr>        <chr>                                    <chr>          
    ## 1 44-45  Retail Trade https://www.bls.gov/iag/tgs/iag44-45.htm iag44-45emp1   
    ## # A tibble: 1 x 4
    ##   sector description              sector_url                     sector_xpath_id
    ##   <chr>  <chr>                    <chr>                          <chr>          
    ## 1 48-49  Transportation and Ware… https://www.bls.gov/iag/tgs/i… iag48-49emp1   
    ## # A tibble: 1 x 4
    ##   sector description sector_url                            sector_xpath_id
    ##   <chr>  <chr>       <chr>                                 <chr>          
    ## 1 51     Information https://www.bls.gov/iag/tgs/iag51.htm iag51emp1      
    ## # A tibble: 1 x 4
    ##   sector description          sector_url                         sector_xpath_id
    ##   <chr>  <chr>                <chr>                              <chr>          
    ## 1 52     Finance and Insuran… https://www.bls.gov/iag/tgs/iag52… iag52emp1      
    ## # A tibble: 1 x 4
    ##   sector description                 sector_url                  sector_xpath_id
    ##   <chr>  <chr>                       <chr>                       <chr>          
    ## 1 53     Real Estate and Rental and… https://www.bls.gov/iag/tg… iag53emp1      
    ## # A tibble: 1 x 4
    ##   sector description                     sector_url              sector_xpath_id
    ##   <chr>  <chr>                           <chr>                   <chr>          
    ## 1 54     Professional, Scientific, and … https://www.bls.gov/ia… iag54emp1      
    ## # A tibble: 1 x 4
    ##   sector description                  sector_url                 sector_xpath_id
    ##   <chr>  <chr>                        <chr>                      <chr>          
    ## 1 55     Management of Companies and… https://www.bls.gov/iag/t… iag55emp1      
    ## # A tibble: 1 x 4
    ##   sector description                        sector_url           sector_xpath_id
    ##   <chr>  <chr>                              <chr>                <chr>          
    ## 1 56     Administrative and Support and Wa… https://www.bls.gov… iag56emp1      
    ## # A tibble: 1 x 4
    ##   sector description          sector_url                         sector_xpath_id
    ##   <chr>  <chr>                <chr>                              <chr>          
    ## 1 61     Educational Services https://www.bls.gov/iag/tgs/iag61… iag61emp1      
    ## # A tibble: 1 x 4
    ##   sector description                sector_url                   sector_xpath_id
    ##   <chr>  <chr>                      <chr>                        <chr>          
    ## 1 62     Health Care and Social As… https://www.bls.gov/iag/tgs… iag62emp1      
    ## # A tibble: 1 x 4
    ##   sector description                 sector_url                  sector_xpath_id
    ##   <chr>  <chr>                       <chr>                       <chr>          
    ## 1 71     Arts, Entertainment, and R… https://www.bls.gov/iag/tg… iag71emp1      
    ## # A tibble: 1 x 4
    ##   sector description                sector_url                   sector_xpath_id
    ##   <chr>  <chr>                      <chr>                        <chr>          
    ## 1 72     Accommodation and Food Se… https://www.bls.gov/iag/tgs… iag72emp1      
    ## # A tibble: 1 x 4
    ##   sector description                    sector_url               sector_xpath_id
    ##   <chr>  <chr>                          <chr>                    <chr>          
    ## 1 81     Other Services (except Public… https://www.bls.gov/iag… iag81emp1

We're almost to the part where we can go out and fetch the html we need. Before we do that, let's store as part of our loop an object called "url," which contains the URL of the page for each sector.

The syntax with the dollar sign is a little funky, but "each_row_df\$sector_url" says "from the each_row_df dataframe, grab the information in the sector_url column." Because the column has only one row, there's one value.

We're going to do something simliar with the xpath for our employment table by using the information in the sector_xpath_id column.

That code also looks a little unwieldly. Recall that the xpath for the mining industry was `'//*[@id="iag22emp1"]'`.

In the code below, we're building the xpath dynamically by pasting together the parts that stay the same for each xpath -- `'//*[@id="'` and `'"]'` -- and the parts that change for each sector, pulled from the xpath_sector_id column.

To see how this is working, we're going to edit our print statement at the end a bit, printing the row_number and the dynamically created url and xpath.

``` 

# For loop, iterating over each row in our naics industry dataframe

for(row_number in 1:nrow(naics_industry)) {
    
    # Keep only the row for a given row number, get rid of every other row
    each_row_df <- naics_industry %>%
      slice(row_number) 
      
    # Define url of page to get
    url <- each_row_df$sector_url
    
    # Define id of table to ingest
    xpath_employment_table <- paste0('//*[@id="',each_row_df$sector_xpath_id,'"]')
    
    # To help us see what's happening as we build this, we're going to print the thing we're creating.  
    print(paste0("ROW NUMBER:", row_number," URL: ",url," XPATH:",xpath_employment_table))
      
}
```

    ## [1] "ROW NUMBER:1 URL: https://www.bls.gov/iag/tgs/iag11.htm XPATH://*[@id=\"iag11emp1\"]"
    ## [1] "ROW NUMBER:2 URL: https://www.bls.gov/iag/tgs/iag21.htm XPATH://*[@id=\"iag21emp1\"]"
    ## [1] "ROW NUMBER:3 URL: https://www.bls.gov/iag/tgs/iag22.htm XPATH://*[@id=\"iag22emp1\"]"
    ## [1] "ROW NUMBER:4 URL: https://www.bls.gov/iag/tgs/iag23.htm XPATH://*[@id=\"iag23emp1\"]"
    ## [1] "ROW NUMBER:5 URL: https://www.bls.gov/iag/tgs/iag31-33.htm XPATH://*[@id=\"iag31-33emp1\"]"
    ## [1] "ROW NUMBER:6 URL: https://www.bls.gov/iag/tgs/iag42.htm XPATH://*[@id=\"iag42emp1\"]"
    ## [1] "ROW NUMBER:7 URL: https://www.bls.gov/iag/tgs/iag44-45.htm XPATH://*[@id=\"iag44-45emp1\"]"
    ## [1] "ROW NUMBER:8 URL: https://www.bls.gov/iag/tgs/iag48-49.htm XPATH://*[@id=\"iag48-49emp1\"]"
    ## [1] "ROW NUMBER:9 URL: https://www.bls.gov/iag/tgs/iag51.htm XPATH://*[@id=\"iag51emp1\"]"
    ## [1] "ROW NUMBER:10 URL: https://www.bls.gov/iag/tgs/iag52.htm XPATH://*[@id=\"iag52emp1\"]"
    ## [1] "ROW NUMBER:11 URL: https://www.bls.gov/iag/tgs/iag53.htm XPATH://*[@id=\"iag53emp1\"]"
    ## [1] "ROW NUMBER:12 URL: https://www.bls.gov/iag/tgs/iag54.htm XPATH://*[@id=\"iag54emp1\"]"
    ## [1] "ROW NUMBER:13 URL: https://www.bls.gov/iag/tgs/iag55.htm XPATH://*[@id=\"iag55emp1\"]"
    ## [1] "ROW NUMBER:14 URL: https://www.bls.gov/iag/tgs/iag56.htm XPATH://*[@id=\"iag56emp1\"]"
    ## [1] "ROW NUMBER:15 URL: https://www.bls.gov/iag/tgs/iag61.htm XPATH://*[@id=\"iag61emp1\"]"
    ## [1] "ROW NUMBER:16 URL: https://www.bls.gov/iag/tgs/iag62.htm XPATH://*[@id=\"iag62emp1\"]"
    ## [1] "ROW NUMBER:17 URL: https://www.bls.gov/iag/tgs/iag71.htm XPATH://*[@id=\"iag71emp1\"]"
    ## [1] "ROW NUMBER:18 URL: https://www.bls.gov/iag/tgs/iag72.htm XPATH://*[@id=\"iag72emp1\"]"
    ## [1] "ROW NUMBER:19 URL: https://www.bls.gov/iag/tgs/iag81.htm XPATH://*[@id=\"iag81emp1\"]"

Armed with the URL and xpath for each sector web page, we can now go out and get the employment table for each sector.

We'll read in the html from the url we just stored; extract the table that has the xpath ID we just created; and then transform the html table code into a proper dataframe.

The dataframe is hidden inside a nested list, which we'll have to extract in the next step.

So, when you run this code, it will print out 19 dataframes inside of nested lists, each containing one dataframe.

``` 
# For loop, iterating over each row in our naics industry dataframe

for(row_number in 1:nrow(naics_industry)) {
    
    # Keep only the row for a given row number, get rid of every other row
    each_row_df <- naics_industry %>%
      slice(row_number) 
      
    # Define url of page to get
    url <- each_row_df$sector_url
    
    # Define id of table to ingest
    xpath_employment_table <- paste0('//*[@id="',each_row_df$sector_xpath_id,'"]')
    
    # Get employment table from each page by going to each url defined above, reading in the html with read_html(), extracting the table with the id generated by the xpath code using html_elements), and then turning the html into a proper dataframe using html_table(). The dataframe is in a nested list, which we'll have to extract in the next step.
    employment_info <- url %>%
      read_html() %>%
      html_elements(xpath = xpath_employment_table) %>%
      html_table() 
    
    # To help us see what's happening as we build this, we're going to print the thing we're creating.  
    print(employment_info)
    
      
}
```

    ## [[1]]
    ## # A tibble: 2 x 6
    ##   `Data series`     Backdata Jul.2021 Aug.2021 Sep.2021 Oct.2021
    ##   <chr>             <lgl>    <chr>    <chr>    <chr>    <chr>   
    ## 1 Unemployment      NA       ""       ""       ""       ""      
    ## 2 Unemployment rate NA       "7.6%"   "5.7%"   "5.0%"   "5.1%"  
    ## 
    ## [[1]]
    ## # A tibble: 6 x 6
    ##   `Data series`       Backdata    Jul.2021    Aug.2021    Sep.2021    Oct.2021  
    ##   <chr>               <chr>       <chr>       <chr>       <chr>       <chr>     
    ## 1 Employment (in tho… ""          ""          ""          ""          ""        
    ## 2 Employment, all em… ""          "592.5"     "598.8"     "(p)603.7"  "(p)608.6"
    ## 3 Employment, produc… ""          "433.6"     "439.3"     "(p)444.6"  ""        
    ## 4 Unemployment        ""          ""          ""          ""          ""        
    ## 5 Unemployment rate   ""          "8.9%"      "10.2%"     "7.3%"      "10.0%"   
    ## 6 Footnotes(p) Preli… "Footnotes… "Footnotes… "Footnotes… "Footnotes… "Footnote…
    ## 
    ## [[1]]
    ## # A tibble: 6 x 6
    ##   `Data series`          Backdata    Jul.2021   Aug.2021   Sep.2021   Oct.2021  
    ##   <chr>                  <chr>       <chr>      <chr>      <chr>      <chr>     
    ## 1 Employment (in thousa… ""          ""         ""         ""         ""        
    ## 2 Employment, all emplo… ""          "538.9"    "536.7"    "(p)536.5" "(p)536.7"
    ## 3 Employment, productio… ""          "429.1"    "426.9"    "(p)426.8" "(p)427.4"
    ## 4 Unemployment           ""          ""         ""         ""         ""        
    ## 5 Unemployment rate      ""          "3.4%"     "2.7%"     "3.1%"     "1.8%"    
    ## 6 Footnotes(p) Prelimin… "Footnotes… "Footnote… "Footnote… "Footnote… "Footnote…
    ## 
    ## [[1]]
    ## # A tibble: 10 x 6
    ##    `Data series`         Backdata    Jul.2021   Aug.2021   Sep.2021   Oct.2021  
    ##    <chr>                 <chr>       <chr>      <chr>      <chr>      <chr>     
    ##  1 Employment (in thous… ""          ""         ""         ""         ""        
    ##  2 Employment, all empl… ""          "7,425"    "7,424"    "(p)7,454" "(p)7,498"
    ##  3 Employment, producti… ""          "5,517"    "5,504"    "(p)5,522" "(p)5,522"
    ##  4 Unemployment          ""          ""         ""         ""         ""        
    ##  5 Unemployment rate     ""          "6.1%"     "4.6%"     "4.5%"     "4.0%"    
    ##  6 Job openings, hires,… ""          ""         ""         ""         ""        
    ##  7 Job openings          ""          "377"      "384"      "(p)316"   ""        
    ##  8 Hires                 ""          "430"      "395"      "(p)341"   ""        
    ##  9 Separations           ""          "402"      "439"      "(p)336"   ""        
    ## 10 Footnotes(p) Prelimi… "Footnotes… "Footnote… "Footnote… "Footnote… "Footnote…
    ## 
    ## [[1]]
    ## # A tibble: 10 x 6
    ##    `Data series`         Backdata    Jul.2021   Aug.2021   Sep.2021   Oct.2021  
    ##    <chr>                 <chr>       <chr>      <chr>      <chr>      <chr>     
    ##  1 Employment (in thous… ""          ""         ""         ""         ""        
    ##  2 Employment, all empl… ""          "12,389"   "12,438"   "(p)12,46… "(p)12,52…
    ##  3 Employment, producti… ""          "8,617"    "8,649"    "(p)8,660" "(p)8,716"
    ##  4 Unemployment          ""          ""         ""         ""         ""        
    ##  5 Unemployment rate     ""          "4.2%"     "3.6%"     "3.9%"     "3.3%"    
    ##  6 Job openings, hires,… ""          ""         ""         ""         ""        
    ##  7 Job openings          ""          "974"      "889"      "(p)899"   ""        
    ##  8 Hires                 ""          "526"      "518"      "(p)504"   ""        
    ##  9 Separations           ""          "452"      "527"      "(p)479"   ""        
    ## 10 Footnotes(p) Prelimi… "Footnotes… "Footnote… "Footnote… "Footnote… "Footnote…
    ## 
    ## [[1]]
    ## # A tibble: 10 x 6
    ##    `Data series`         Backdata    Jul.2021   Aug.2021   Sep.2021   Oct.2021  
    ##    <chr>                 <chr>       <chr>      <chr>      <chr>      <chr>     
    ##  1 Employment (in thous… ""          ""         ""         ""         ""        
    ##  2 Employment, all empl… ""          "5,722.1"  "5,716.9"  "(p)5,724… "(p)5,737…
    ##  3 Employment, producti… ""          "4,547.8"  "4,549.2"  "(p)4,558… "(p)4,569…
    ##  4 Unemployment          ""          ""         ""         ""         ""        
    ##  5 Unemployment rate     ""          "4.6%"     "4.3%"     "3.7%"     "4.2%"    
    ##  6 Job openings, hires,… ""          ""         ""         ""         ""        
    ##  7 Job openings          ""          "291"      "261"      "(p)320"   ""        
    ##  8 Hires                 ""          "199"      "203"      "(p)197"   ""        
    ##  9 Separations           ""          "177"      "220"      "(p)175"   ""        
    ## 10 Footnotes(p) Prelimi… "Footnotes… "Footnote… "Footnote… "Footnote… "Footnote…
    ## 
    ## [[1]]
    ## # A tibble: 10 x 6
    ##    `Data series`         Backdata    Jul.2021   Aug.2021   Sep.2021   Oct.2021  
    ##    <chr>                 <chr>       <chr>      <chr>      <chr>      <chr>     
    ##  1 Employment (in thous… ""          ""         ""         ""         ""        
    ##  2 Employment, all empl… ""          "15,355.3" "15,377.5" "(p)15,43… "(p)15,47…
    ##  3 Employment, producti… ""          "13,068.6" "13,089.0" "(p)13,14… "(p)13,18…
    ##  4 Unemployment          ""          ""         ""         ""         ""        
    ##  5 Unemployment rate     ""          "6.4%"     "6.5%"     "6.1%"     "5.4%"    
    ##  6 Job openings, hires,… ""          ""         ""         ""         ""        
    ##  7 Job openings          ""          "1,245"    "1,346"    "(p)1,231" ""        
    ##  8 Hires                 ""          "905"      "1,010"    "(p)892"   ""        
    ##  9 Separations           ""          "913"      "1,100"    "(p)843"   ""        
    ## 10 Footnotes(p) Prelimi… "Footnotes… "Footnote… "Footnote… "Footnote… "Footnote…
    ## 
    ## [[1]]
    ## # A tibble: 6 x 6
    ##   `Data series`          Backdata    Jul.2021   Aug.2021   Sep.2021   Oct.2021  
    ##   <chr>                  <chr>       <chr>      <chr>      <chr>      <chr>     
    ## 1 Employment (in thousa… ""          ""         ""         ""         ""        
    ## 2 Employment, all emplo… ""          "5,792.9"  "5,860.2"  "(p)5,917… "(p)5,972…
    ## 3 Employment, productio… ""          "5,052.6"  "5,089.7"  "(p)5,119… "(p)5,152…
    ## 4 Unemployment           ""          ""         ""         ""         ""        
    ## 5 Unemployment rate      ""          "7.3%"     "6.4%"     "5.7%"     "5.1%"    
    ## 6 Footnotes(p) Prelimin… "Footnotes… "Footnote… "Footnote… "Footnote… "Footnote…
    ## 
    ## [[1]]
    ## # A tibble: 10 x 6
    ##    `Data series`         Backdata    Jul.2021   Aug.2021   Sep.2021   Oct.2021  
    ##    <chr>                 <chr>       <chr>      <chr>      <chr>      <chr>     
    ##  1 Employment (in thous… ""          ""         ""         ""         ""        
    ##  2 Employment, all empl… ""          "2,745"    "2,778"    "(p)2,782" "(p)2,792"
    ##  3 Employment, producti… ""          "2,183"    "2,207"    "(p)2,216" "(p)2,219"
    ##  4 Unemployment          ""          ""         ""         ""         ""        
    ##  5 Unemployment rate     ""          "5.6%"     "4.4%"     "4.0%"     "3.5%"    
    ##  6 Job openings, hires,… ""          ""         ""         ""         ""        
    ##  7 Job openings          ""          "181"      "193"      "(p)243"   ""        
    ##  8 Hires                 ""          "106"      "112"      "(p)113"   ""        
    ##  9 Separations           ""          "85"       "91"       "(p)72"    ""        
    ## 10 Footnotes(p) Prelimi… "Footnotes… "Footnote… "Footnote… "Footnote… "Footnote…
    ## 
    ## [[1]]
    ## # A tibble: 9 x 6
    ##   `Data series`       Backdata    Jul.2021    Aug.2021    Sep.2021    Oct.2021  
    ##   <chr>               <chr>       <chr>       <chr>       <chr>       <chr>     
    ## 1 Employment (in tho… ""          ""          ""          ""          ""        
    ## 2 Employment, all em… ""          "6,545.1"   "6,550.3"   "(p)6,544.… "(p)6,553…
    ## 3 Unemployment        ""          ""          ""          ""          ""        
    ## 4 Unemployment rate   ""          "3.1%"      "3.5%"      "2.0%"      "1.8%"    
    ## 5 Job openings, hire… ""          ""          ""          ""          ""        
    ## 6 Job openings        ""          "354"       "285"       "(p)298"    ""        
    ## 7 Hires               ""          "164"       "134"       "(p)193"    ""        
    ## 8 Separations         ""          "140"       "173"       "(p)191"    ""        
    ## 9 Footnotes(p) Preli… "Footnotes… "Footnotes… "Footnotes… "Footnotes… "Footnote…
    ## 
    ## [[1]]
    ## # A tibble: 9 x 6
    ##   `Data series`       Backdata    Jul.2021    Aug.2021    Sep.2021    Oct.2021  
    ##   <chr>               <chr>       <chr>       <chr>       <chr>       <chr>     
    ## 1 Employment (in tho… ""          ""          ""          ""          ""        
    ## 2 Employment, all em… ""          "2,291.9"   "2,303.7"   "(p)2,316.… "(p)2,328…
    ## 3 Unemployment        ""          ""          ""          ""          ""        
    ## 4 Unemployment rate   ""          "2.8%"      "2.6%"      "3.8%"      "2.2%"    
    ## 5 Job openings, hire… ""          ""          ""          ""          ""        
    ## 6 Job openings        ""          "199"       "183"       "(p)112"    ""        
    ## 7 Hires               ""          "89"        "79"        "(p)68"     ""        
    ## 8 Separations         ""          "82"        "81"        "(p)57"     ""        
    ## 9 Footnotes(p) Preli… "Footnotes… "Footnotes… "Footnotes… "Footnotes… "Footnote…
    ## 
    ## [[1]]
    ## # A tibble: 6 x 6
    ##   `Data series`       Backdata    Jul.2021    Aug.2021    Sep.2021    Oct.2021  
    ##   <chr>               <chr>       <chr>       <chr>       <chr>       <chr>     
    ## 1 Employment (in tho… ""          ""          ""          ""          ""        
    ## 2 Employment, all em… ""          "9,839.0"   "9,906.3"   "(p)9,961.… "(p)10,00…
    ## 3 Employment, produc… ""          "7,593.2"   "7,612.3"   "(p)7,580.… ""        
    ## 4 Unemployment        ""          ""          ""          ""          ""        
    ## 5 Unemployment rate   ""          "3.2%"      "2.7%"      "2.5%"      "2.6%"    
    ## 6 Footnotes(p) Preli… "Footnotes… "Footnotes… "Footnotes… "Footnotes… "Footnote…
    ## 
    ## [[1]]
    ## # A tibble: 4 x 6
    ##   `Data series`       Backdata    Jul.2021    Aug.2021    Sep.2021    Oct.2021  
    ##   <chr>               <chr>       <chr>       <chr>       <chr>       <chr>     
    ## 1 Employment (in tho… ""          ""          ""          ""          ""        
    ## 2 Employment, all em… ""          "2,329.8"   "2,336.9"   "(p)2,339.… "(p)2,345…
    ## 3 Employment, produc… ""          "1,526.8"   "1,522.9"   "(p)1,522.… ""        
    ## 4 Footnotes(p) Preli… "Footnotes… "Footnotes… "Footnotes… "Footnotes… "Footnote…
    ## 
    ## [[1]]
    ## # A tibble: 4 x 6
    ##   `Data series`       Backdata    Jul.2021    Aug.2021    Sep.2021    Oct.2021  
    ##   <chr>               <chr>       <chr>       <chr>       <chr>       <chr>     
    ## 1 Employment (in tho… ""          ""          ""          ""          ""        
    ## 2 Employment, all em… ""          "8,770.3"   "8,835.1"   "(p)8,852.… "(p)8,901…
    ## 3 Employment, produc… ""          "7,755.2"   "7,839.8"   "(p)7,894.… ""        
    ## 4 Footnotes(p) Preli… "Footnotes… "Footnotes… "Footnotes… "Footnotes… "Footnote…
    ## 
    ## [[1]]
    ## # A tibble: 9 x 6
    ##   `Data series`       Backdata    Jul.2021    Aug.2021    Sep.2021    Oct.2021  
    ##   <chr>               <chr>       <chr>       <chr>       <chr>       <chr>     
    ## 1 Employment (in tho… ""          ""          ""          ""          ""        
    ## 2 Employment, all em… ""          "3,576.1"   "3,634.2"   "(p)3,613.… "(p)3,630…
    ## 3 Unemployment        ""          ""          ""          ""          ""        
    ## 4 Unemployment rate   ""          "6.7%"      "6.1%"      "3.9%"      "3.0%"    
    ## 5 Job openings, hire… ""          ""          ""          ""          ""        
    ## 6 Job openings        ""          "221"       "188"       "(p)129"    ""        
    ## 7 Hires               ""          "143"       "213"       "(p)109"    ""        
    ## 8 Separations         ""          "88"        "116"       "(p)89"     ""        
    ## 9 Footnotes(p) Preli… "Footnotes… "Footnotes… "Footnotes… "Footnotes… "Footnote…
    ## 
    ## [[1]]
    ## # A tibble: 10 x 6
    ##    `Data series`       Backdata    Jul.2021    Aug.2021    Sep.2021   Oct.2021  
    ##    <chr>               <chr>       <chr>       <chr>       <chr>      <chr>     
    ##  1 Employment (in tho… ""          ""          ""          ""         ""        
    ##  2 Employment, all em… ""          "20,044.8"  "20,058.5"  "(p)20,09… "(p)20,13…
    ##  3 Employment, produc… ""          "17,594.0"  "17,603.8"  "(p)17,55… ""        
    ##  4 Unemployment        ""          ""          ""          ""         ""        
    ##  5 Unemployment rate   ""          "3.8%"      "3.9%"      "3.1%"     "2.7%"    
    ##  6 Job openings, hire… ""          ""          ""          ""         ""        
    ##  7 Job openings        ""          "1,813"     "1,565"     "(p)1,702" ""        
    ##  8 Hires               ""          "763"       "764"       "(p)800"   ""        
    ##  9 Separations         ""          "728"       "722"       "(p)768"   ""        
    ## 10 Footnotes(p) Preli… "Footnotes… "Footnotes… "Footnotes… "Footnote… "Footnote…
    ## 
    ## [[1]]
    ## # A tibble: 10 x 6
    ##    `Data series`       Backdata    Jul.2021    Aug.2021    Sep.2021   Oct.2021  
    ##    <chr>               <chr>       <chr>       <chr>       <chr>      <chr>     
    ##  1 Employment (in tho… ""          ""          ""          ""         ""        
    ##  2 Employment, all em… ""          "2,093.4"   "2,156.8"   "(p)2,196… "(p)2,217…
    ##  3 Employment, produc… ""          "2,031.8"   "2,017.6"   "(p)1,855… ""        
    ##  4 Unemployment        ""          ""          ""          ""         ""        
    ##  5 Unemployment rate   ""          "8.3%"      "7.7%"      "7.2%"     "6.5%"    
    ##  6 Job openings, hire… ""          ""          ""          ""         ""        
    ##  7 Job openings        ""          "234"       "218"       "(p)184"   ""        
    ##  8 Hires               ""          "199"       "151"       "(p)159"   ""        
    ##  9 Separations         ""          "119"       "212"       "(p)249"   ""        
    ## 10 Footnotes(p) Preli… "Footnotes… "Footnotes… "Footnotes… "Footnote… "Footnote…
    ## 
    ## [[1]]
    ## # A tibble: 10 x 6
    ##    `Data series`       Backdata    Jul.2021    Aug.2021    Sep.2021   Oct.2021  
    ##    <chr>               <chr>       <chr>       <chr>       <chr>      <chr>     
    ##  1 Employment (in tho… ""          ""          ""          ""         ""        
    ##  2 Employment, all em… ""          "13,115.3"  "13,122.8"  "(p)13,17… "(p)13,31…
    ##  3 Employment, produc… ""          "11,759.2"  "11,724.5"  "(p)11,49… ""        
    ##  4 Unemployment        ""          ""          ""          ""         ""        
    ##  5 Unemployment rate   ""          "9.2%"      "9.4%"      "7.8%"     "7.7%"    
    ##  6 Job openings, hire… ""          ""          ""          ""         ""        
    ##  7 Job openings        ""          "1,793"     "1,518"     "(p)1,394" ""        
    ##  8 Hires               ""          "1,443"     "1,135"     "(p)1,002" ""        
    ##  9 Separations         ""          "1,005"     "1,278"     "(p)1,169" ""        
    ## 10 Footnotes(p) Preli… "Footnotes… "Footnotes… "Footnotes… "Footnote… "Footnote…
    ## 
    ## [[1]]
    ## # A tibble: 10 x 6
    ##    `Data series`         Backdata    Jul.2021   Aug.2021   Sep.2021   Oct.2021  
    ##    <chr>                 <chr>       <chr>      <chr>      <chr>      <chr>     
    ##  1 Employment (in thous… ""          ""         ""         ""         ""        
    ##  2 Employment, all empl… ""          "5,709"    "5,745"    "(p)5,735" "(p)5,768"
    ##  3 Employment, producti… ""          "4,642"    "4,676"    "(p)4,672" "(p)4,700"
    ##  4 Unemployment          ""          ""         ""         ""         ""        
    ##  5 Unemployment rate     ""          "4.9%"     "5.0%"     "4.2%"     "3.5%"    
    ##  6 Job openings, hires,… ""          ""         ""         ""         ""        
    ##  7 Job openings          ""          "501"      "500"      "(p)382"   ""        
    ##  8 Hires                 ""          "327"      "243"      "(p)239"   ""        
    ##  9 Separations           ""          "275"      "239"      "(p)304"   ""        
    ## 10 Footnotes(p) Prelimi… "Footnotes… "Footnote… "Footnote… "Footnote… "Footnote…

In this next step, we use employment_info \<- employment_info\[\[1\]\] to extract each dataframe from the nested list. Then we'll tidy up the dataframe a bit. We'll use the get rid of all the information we don't need in the table, by using slice() to keep only the second row. We'll also standardize the column names with clean_names().

``` 

# For loop, iterating over each row in our naics industry dataframe

for(row_number in 1:nrow(naics_industry)) {
    
    # Keep only the row for a given row number, get rid of every other row
    each_row_df <- naics_industry %>%
      slice(row_number) 
      
    # Define url of page to get
    url <- each_row_df$sector_url
    
    # Define id of table to ingest
    xpath_employment_table <- paste0('//*[@id="',each_row_df$sector_xpath_id,'"]')
    
    # Get employment table from each page by going to each url defined above, reading in the html with read_html(), extracting the table with the id generated by the xpath code using html_elements), and then turning the html into a proper dataframe using html_table().  The dataframe is in a nested list, which we'll have to extract in the next step.
    employment_info <- url %>%
      read_html() %>%
      html_elements(xpath = xpath_employment_table) %>%
      html_table() 
    
    # Grab the dataframe out of the list (it's the first and only element inside the list); clean up the field names with clean_names(); use slice(2) to keep only the second row; 
    employment_info <- employment_info[[1]] %>%
      clean_names() %>%
      slice(2) 
    
    # To help us see what's happening as we build this, we're going to print the thing we're creating.  
    print(employment_info)
    
      
}
```

    ## # A tibble: 1 x 6
    ##   data_series       backdata jul_2021 aug_2021 sep_2021 oct_2021
    ##   <chr>             <lgl>    <chr>    <chr>    <chr>    <chr>   
    ## 1 Unemployment rate NA       7.6%     5.7%     5.0%     5.1%    
    ## # A tibble: 1 x 6
    ##   data_series                       backdata jul_2021 aug_2021 sep_2021 oct_2021
    ##   <chr>                             <chr>    <chr>    <chr>    <chr>    <chr>   
    ## 1 Employment, all employees  (seas… ""       592.5    598.8    (p)603.7 (p)608.6
    ## # A tibble: 1 x 6
    ##   data_series                       backdata jul_2021 aug_2021 sep_2021 oct_2021
    ##   <chr>                             <chr>    <chr>    <chr>    <chr>    <chr>   
    ## 1 Employment, all employees  (seas… ""       538.9    536.7    (p)536.5 (p)536.7
    ## # A tibble: 1 x 6
    ##   data_series                       backdata jul_2021 aug_2021 sep_2021 oct_2021
    ##   <chr>                             <chr>    <chr>    <chr>    <chr>    <chr>   
    ## 1 Employment, all employees  (seas… ""       7,425    7,424    (p)7,454 (p)7,498
    ## # A tibble: 1 x 6
    ##   data_series                      backdata jul_2021 aug_2021 sep_2021  oct_2021
    ##   <chr>                            <chr>    <chr>    <chr>    <chr>     <chr>   
    ## 1 Employment, all employees  (sea… ""       12,389   12,438   (p)12,469 (p)12,5…
    ## # A tibble: 1 x 6
    ##   data_series                     backdata jul_2021 aug_2021 sep_2021  oct_2021 
    ##   <chr>                           <chr>    <chr>    <chr>    <chr>     <chr>    
    ## 1 Employment, all employees  (se… ""       5,722.1  5,716.9  (p)5,724… (p)5,737…
    ## # A tibble: 1 x 6
    ##   data_series                    backdata jul_2021 aug_2021 sep_2021   oct_2021 
    ##   <chr>                          <chr>    <chr>    <chr>    <chr>      <chr>    
    ## 1 Employment, all employees  (s… ""       15,355.3 15,377.5 (p)15,434… (p)15,47…
    ## # A tibble: 1 x 6
    ##   data_series                     backdata jul_2021 aug_2021 sep_2021  oct_2021 
    ##   <chr>                           <chr>    <chr>    <chr>    <chr>     <chr>    
    ## 1 Employment, all employees  (se… ""       5,792.9  5,860.2  (p)5,917… (p)5,972…
    ## # A tibble: 1 x 6
    ##   data_series                       backdata jul_2021 aug_2021 sep_2021 oct_2021
    ##   <chr>                             <chr>    <chr>    <chr>    <chr>    <chr>   
    ## 1 Employment, all employees  (seas… ""       2,745    2,778    (p)2,782 (p)2,792
    ## # A tibble: 1 x 6
    ##   data_series                     backdata jul_2021 aug_2021 sep_2021  oct_2021 
    ##   <chr>                           <chr>    <chr>    <chr>    <chr>     <chr>    
    ## 1 Employment, all employees  (se… ""       6,545.1  6,550.3  (p)6,544… (p)6,553…
    ## # A tibble: 1 x 6
    ##   data_series                     backdata jul_2021 aug_2021 sep_2021  oct_2021 
    ##   <chr>                           <chr>    <chr>    <chr>    <chr>     <chr>    
    ## 1 Employment, all employees  (se… ""       2,291.9  2,303.7  (p)2,316… (p)2,328…
    ## # A tibble: 1 x 6
    ##   data_series                     backdata jul_2021 aug_2021 sep_2021  oct_2021 
    ##   <chr>                           <chr>    <chr>    <chr>    <chr>     <chr>    
    ## 1 Employment, all employees  (se… ""       9,839.0  9,906.3  (p)9,961… (p)10,00…
    ## # A tibble: 1 x 6
    ##   data_series                     backdata jul_2021 aug_2021 sep_2021  oct_2021 
    ##   <chr>                           <chr>    <chr>    <chr>    <chr>     <chr>    
    ## 1 Employment, all employees  (se… ""       2,329.8  2,336.9  (p)2,339… (p)2,345…
    ## # A tibble: 1 x 6
    ##   data_series                     backdata jul_2021 aug_2021 sep_2021  oct_2021 
    ##   <chr>                           <chr>    <chr>    <chr>    <chr>     <chr>    
    ## 1 Employment, all employees  (se… ""       8,770.3  8,835.1  (p)8,852… (p)8,901…
    ## # A tibble: 1 x 6
    ##   data_series                     backdata jul_2021 aug_2021 sep_2021  oct_2021 
    ##   <chr>                           <chr>    <chr>    <chr>    <chr>     <chr>    
    ## 1 Employment, all employees  (se… ""       3,576.1  3,634.2  (p)3,613… (p)3,630…
    ## # A tibble: 1 x 6
    ##   data_series                    backdata jul_2021 aug_2021 sep_2021   oct_2021 
    ##   <chr>                          <chr>    <chr>    <chr>    <chr>      <chr>    
    ## 1 Employment, all employees  (s… ""       20,044.8 20,058.5 (p)20,092… (p)20,13…
    ## # A tibble: 1 x 6
    ##   data_series                     backdata jul_2021 aug_2021 sep_2021  oct_2021 
    ##   <chr>                           <chr>    <chr>    <chr>    <chr>     <chr>    
    ## 1 Employment, all employees  (se… ""       2,093.4  2,156.8  (p)2,196… (p)2,217…
    ## # A tibble: 1 x 6
    ##   data_series                    backdata jul_2021 aug_2021 sep_2021   oct_2021 
    ##   <chr>                          <chr>    <chr>    <chr>    <chr>      <chr>    
    ## 1 Employment, all employees  (s… ""       13,115.3 13,122.8 (p)13,172… (p)13,31…
    ## # A tibble: 1 x 6
    ##   data_series                       backdata jul_2021 aug_2021 sep_2021 oct_2021
    ##   <chr>                             <chr>    <chr>    <chr>    <chr>    <chr>   
    ## 1 Employment, all employees  (seas… ""       5,709    5,745    (p)5,735 (p)5,768

We now have 19 dataframes, each containing one row each and two columns, one of which is the employment number for a given sector for jul_2021. But we're missing information about what industry sector these employment numbers represent.

We can add that back in by using bind_cols() to reconnect the each_row_df, which contains the sector code and the sector name.

``` 
# For loop, iterating over each row in our naics industry dataframe

for(row_number in 1:nrow(naics_industry)) {
    
    # Keep only the row for a given row number, get rid of every other row
    each_row_df <- naics_industry %>%
      slice(row_number) 
      
    # Define url of page to get
    url <- each_row_df$sector_url
    
    # Define id of table to ingest
    xpath_employment_table <- paste0('//*[@id="',each_row_df$sector_xpath_id,'"]')
    
    # Get employment table from each page by going to each url defined above, reading in the html with read_html(), extracting the table with the id generated by the xpath code using html_elements), and then turning the html into a proper dataframe using html_table().  The dataframe is in a nested list, which we'll have to extract in the next step.
    employment_info <- url %>%
      read_html() %>%
      html_elements(xpath = xpath_employment_table) %>%
      html_table() 
    
    # Grab the dataframe out of the list (it's the first and only element inside the list); clean up the field names with clean_names(); use slice(2) to keep only the second row; use bind_cols() to append the sector code and name to this table.
    employment_info <- employment_info[[1]] %>%
      clean_names() %>%
      slice(2) %>% 
      bind_cols(each_row_df) 
    
    # To help us see what's happening as we build this, we're going to print the thing we're creating.  
    print(employment_info)
    
      
}
```

    ## # A tibble: 1 x 10
    ##   data_series  backdata jul_2021 aug_2021 sep_2021 oct_2021 sector description  
    ##   <chr>        <lgl>    <chr>    <chr>    <chr>    <chr>    <chr>  <chr>        
    ## 1 Unemploymen… NA       7.6%     5.7%     5.0%     5.1%     11     Agriculture,…
    ## # … with 2 more variables: sector_url <chr>, sector_xpath_id <chr>
    ## # A tibble: 1 x 10
    ##   data_series   backdata jul_2021 aug_2021 sep_2021 oct_2021 sector description 
    ##   <chr>         <chr>    <chr>    <chr>    <chr>    <chr>    <chr>  <chr>       
    ## 1 Employment, … ""       592.5    598.8    (p)603.7 (p)608.6 21     Mining, Qua…
    ## # … with 2 more variables: sector_url <chr>, sector_xpath_id <chr>
    ## # A tibble: 1 x 10
    ##   data_series    backdata jul_2021 aug_2021 sep_2021 oct_2021 sector description
    ##   <chr>          <chr>    <chr>    <chr>    <chr>    <chr>    <chr>  <chr>      
    ## 1 Employment, a… ""       538.9    536.7    (p)536.5 (p)536.7 22     Utilities  
    ## # … with 2 more variables: sector_url <chr>, sector_xpath_id <chr>
    ## # A tibble: 1 x 10
    ##   data_series    backdata jul_2021 aug_2021 sep_2021 oct_2021 sector description
    ##   <chr>          <chr>    <chr>    <chr>    <chr>    <chr>    <chr>  <chr>      
    ## 1 Employment, a… ""       7,425    7,424    (p)7,454 (p)7,498 23     Constructi…
    ## # … with 2 more variables: sector_url <chr>, sector_xpath_id <chr>
    ## # A tibble: 1 x 10
    ##   data_series    backdata jul_2021 aug_2021 sep_2021 oct_2021 sector description
    ##   <chr>          <chr>    <chr>    <chr>    <chr>    <chr>    <chr>  <chr>      
    ## 1 Employment, a… ""       12,389   12,438   (p)12,4… (p)12,5… 31-33  Manufactur…
    ## # … with 2 more variables: sector_url <chr>, sector_xpath_id <chr>
    ## # A tibble: 1 x 10
    ##   data_series    backdata jul_2021 aug_2021 sep_2021 oct_2021 sector description
    ##   <chr>          <chr>    <chr>    <chr>    <chr>    <chr>    <chr>  <chr>      
    ## 1 Employment, a… ""       5,722.1  5,716.9  (p)5,72… (p)5,73… 42     Wholesale …
    ## # … with 2 more variables: sector_url <chr>, sector_xpath_id <chr>
    ## # A tibble: 1 x 10
    ##   data_series    backdata jul_2021 aug_2021 sep_2021 oct_2021 sector description
    ##   <chr>          <chr>    <chr>    <chr>    <chr>    <chr>    <chr>  <chr>      
    ## 1 Employment, a… ""       15,355.3 15,377.5 (p)15,4… (p)15,4… 44-45  Retail Tra…
    ## # … with 2 more variables: sector_url <chr>, sector_xpath_id <chr>
    ## # A tibble: 1 x 10
    ##   data_series   backdata jul_2021 aug_2021 sep_2021  oct_2021 sector description
    ##   <chr>         <chr>    <chr>    <chr>    <chr>     <chr>    <chr>  <chr>      
    ## 1 Employment, … ""       5,792.9  5,860.2  (p)5,917… (p)5,97… 48-49  Transporta…
    ## # … with 2 more variables: sector_url <chr>, sector_xpath_id <chr>
    ## # A tibble: 1 x 10
    ##   data_series    backdata jul_2021 aug_2021 sep_2021 oct_2021 sector description
    ##   <chr>          <chr>    <chr>    <chr>    <chr>    <chr>    <chr>  <chr>      
    ## 1 Employment, a… ""       2,745    2,778    (p)2,782 (p)2,792 51     Information
    ## # … with 2 more variables: sector_url <chr>, sector_xpath_id <chr>
    ## # A tibble: 1 x 10
    ##   data_series    backdata jul_2021 aug_2021 sep_2021 oct_2021 sector description
    ##   <chr>          <chr>    <chr>    <chr>    <chr>    <chr>    <chr>  <chr>      
    ## 1 Employment, a… ""       6,545.1  6,550.3  (p)6,54… (p)6,55… 52     Finance an…
    ## # … with 2 more variables: sector_url <chr>, sector_xpath_id <chr>
    ## # A tibble: 1 x 10
    ##   data_series   backdata jul_2021 aug_2021 sep_2021 oct_2021 sector description 
    ##   <chr>         <chr>    <chr>    <chr>    <chr>    <chr>    <chr>  <chr>       
    ## 1 Employment, … ""       2,291.9  2,303.7  (p)2,31… (p)2,32… 53     Real Estate…
    ## # … with 2 more variables: sector_url <chr>, sector_xpath_id <chr>
    ## # A tibble: 1 x 10
    ##   data_series   backdata jul_2021 aug_2021 sep_2021 oct_2021 sector description 
    ##   <chr>         <chr>    <chr>    <chr>    <chr>    <chr>    <chr>  <chr>       
    ## 1 Employment, … ""       9,839.0  9,906.3  (p)9,96… (p)10,0… 54     Professiona…
    ## # … with 2 more variables: sector_url <chr>, sector_xpath_id <chr>
    ## # A tibble: 1 x 10
    ##   data_series   backdata jul_2021 aug_2021 sep_2021 oct_2021 sector description 
    ##   <chr>         <chr>    <chr>    <chr>    <chr>    <chr>    <chr>  <chr>       
    ## 1 Employment, … ""       2,329.8  2,336.9  (p)2,33… (p)2,34… 55     Management …
    ## # … with 2 more variables: sector_url <chr>, sector_xpath_id <chr>
    ## # A tibble: 1 x 10
    ##   data_series   backdata jul_2021 aug_2021 sep_2021 oct_2021 sector description 
    ##   <chr>         <chr>    <chr>    <chr>    <chr>    <chr>    <chr>  <chr>       
    ## 1 Employment, … ""       8,770.3  8,835.1  (p)8,85… (p)8,90… 56     Administrat…
    ## # … with 2 more variables: sector_url <chr>, sector_xpath_id <chr>
    ## # A tibble: 1 x 10
    ##   data_series    backdata jul_2021 aug_2021 sep_2021 oct_2021 sector description
    ##   <chr>          <chr>    <chr>    <chr>    <chr>    <chr>    <chr>  <chr>      
    ## 1 Employment, a… ""       3,576.1  3,634.2  (p)3,61… (p)3,63… 61     Educationa…
    ## # … with 2 more variables: sector_url <chr>, sector_xpath_id <chr>
    ## # A tibble: 1 x 10
    ##   data_series   backdata jul_2021 aug_2021 sep_2021 oct_2021 sector description 
    ##   <chr>         <chr>    <chr>    <chr>    <chr>    <chr>    <chr>  <chr>       
    ## 1 Employment, … ""       20,044.8 20,058.5 (p)20,0… (p)20,1… 62     Health Care…
    ## # … with 2 more variables: sector_url <chr>, sector_xpath_id <chr>
    ## # A tibble: 1 x 10
    ##   data_series   backdata jul_2021 aug_2021 sep_2021 oct_2021 sector description 
    ##   <chr>         <chr>    <chr>    <chr>    <chr>    <chr>    <chr>  <chr>       
    ## 1 Employment, … ""       2,093.4  2,156.8  (p)2,19… (p)2,21… 71     Arts, Enter…
    ## # … with 2 more variables: sector_url <chr>, sector_xpath_id <chr>
    ## # A tibble: 1 x 10
    ##   data_series   backdata jul_2021 aug_2021 sep_2021  oct_2021 sector description
    ##   <chr>         <chr>    <chr>    <chr>    <chr>     <chr>    <chr>  <chr>      
    ## 1 Employment, … ""       13,115.3 13,122.8 (p)13,17… (p)13,3… 72     Accommodat…
    ## # … with 2 more variables: sector_url <chr>, sector_xpath_id <chr>
    ## # A tibble: 1 x 10
    ##   data_series   backdata jul_2021 aug_2021 sep_2021 oct_2021 sector description 
    ##   <chr>         <chr>    <chr>    <chr>    <chr>    <chr>    <chr>  <chr>       
    ## 1 Employment, … ""       5,709    5,745    (p)5,735 (p)5,768 81     Other Servi…
    ## # … with 2 more variables: sector_url <chr>, sector_xpath_id <chr>

Then we'll do a little bit of cleaning.

Let's use parse_number() to remove the comma from the jul_2021 number and convert it from a character to number. We'll use rename() to make the jul_2021 column name a little more descriptive. And then we'll use select() to keep only the columns we want to keep -- the sector number, the sector name, and the jul_2021 employment number.

``` 

# For loop, iterating over each row in our naics industry dataframe
for(row_number in 1:nrow(naics_industry)) {
    
    # Keep only the row for a given row number, get rid of every other row
    each_row_df <- naics_industry %>%
      slice(row_number) 
      
    # Define url of page to get
    url <- each_row_df$sector_url
    
    # Define id of table to ingest
    xpath_employment_table <- paste0('//*[@id="',each_row_df$sector_xpath_id,'"]')
    
    # Get employment table from each page by going to each url defined above, reading in the html with read_html(), extracting the table with the id generated by the xpath code using html_elements), and then turning the html into a proper dataframe using html_table().  The dataframe is in a nested list, which we'll have to extract in the next step.
    employment_info <- url %>%
      read_html() %>%
      html_elements(xpath = xpath_employment_table) %>%
      html_table() 
    
    # Grab the dataframe out of the list (it's the first and only element inside the list); clean up the field names with clean_names(); use slice(2) to keep only the second row; use bind_cols() to append the sector code and name to this table; turn jul_2021 column into a proper number, and rename it.  Then select only three columns we need. 
    employment_info <- employment_info[[1]] %>%
      clean_names() %>%
      slice(2) %>% 
      bind_cols(each_row_df) %>%
      mutate(jul_2021 = parse_number(jul_2021)) %>%
      rename(jul_2021_employees = jul_2021) %>%
      select(sector,description,jul_2021_employees) 
    
    # To help us see what's happening as we build this, we're going to print the thing we're creating.  
    print(employment_info)
    
    
}
```

    ## # A tibble: 1 x 3
    ##   sector description                                jul_2021_employees
    ##   <chr>  <chr>                                                   <dbl>
    ## 1 11     Agriculture, Forestry, Fishing and Hunting                7.6
    ## # A tibble: 1 x 3
    ##   sector description                                   jul_2021_employees
    ##   <chr>  <chr>                                                      <dbl>
    ## 1 21     Mining, Quarrying, and Oil and Gas Extraction               592.
    ## # A tibble: 1 x 3
    ##   sector description jul_2021_employees
    ##   <chr>  <chr>                    <dbl>
    ## 1 22     Utilities                 539.
    ## # A tibble: 1 x 3
    ##   sector description  jul_2021_employees
    ##   <chr>  <chr>                     <dbl>
    ## 1 23     Construction               7425
    ## # A tibble: 1 x 3
    ##   sector description   jul_2021_employees
    ##   <chr>  <chr>                      <dbl>
    ## 1 31-33  Manufacturing              12389
    ## # A tibble: 1 x 3
    ##   sector description     jul_2021_employees
    ##   <chr>  <chr>                        <dbl>
    ## 1 42     Wholesale Trade              5722.
    ## # A tibble: 1 x 3
    ##   sector description  jul_2021_employees
    ##   <chr>  <chr>                     <dbl>
    ## 1 44-45  Retail Trade             15355.
    ## # A tibble: 1 x 3
    ##   sector description                    jul_2021_employees
    ##   <chr>  <chr>                                       <dbl>
    ## 1 48-49  Transportation and Warehousing              5793.
    ## # A tibble: 1 x 3
    ##   sector description jul_2021_employees
    ##   <chr>  <chr>                    <dbl>
    ## 1 51     Information               2745
    ## # A tibble: 1 x 3
    ##   sector description           jul_2021_employees
    ##   <chr>  <chr>                              <dbl>
    ## 1 52     Finance and Insurance              6545.
    ## # A tibble: 1 x 3
    ##   sector description                        jul_2021_employees
    ##   <chr>  <chr>                                           <dbl>
    ## 1 53     Real Estate and Rental and Leasing              2292.
    ## # A tibble: 1 x 3
    ##   sector description                                      jul_2021_employees
    ##   <chr>  <chr>                                                         <dbl>
    ## 1 54     Professional, Scientific, and Technical Services               9839
    ## # A tibble: 1 x 3
    ##   sector description                             jul_2021_employees
    ##   <chr>  <chr>                                                <dbl>
    ## 1 55     Management of Companies and Enterprises              2330.
    ## # A tibble: 1 x 3
    ##   sector description                                           jul_2021_employe…
    ##   <chr>  <chr>                                                             <dbl>
    ## 1 56     Administrative and Support and Waste Management and …             8770.
    ## # A tibble: 1 x 3
    ##   sector description          jul_2021_employees
    ##   <chr>  <chr>                             <dbl>
    ## 1 61     Educational Services              3576.
    ## # A tibble: 1 x 3
    ##   sector description                       jul_2021_employees
    ##   <chr>  <chr>                                          <dbl>
    ## 1 62     Health Care and Social Assistance             20045.
    ## # A tibble: 1 x 3
    ##   sector description                         jul_2021_employees
    ##   <chr>  <chr>                                            <dbl>
    ## 1 71     Arts, Entertainment, and Recreation              2093.
    ## # A tibble: 1 x 3
    ##   sector description                     jul_2021_employees
    ##   <chr>  <chr>                                        <dbl>
    ## 1 72     Accommodation and Food Services             13115.
    ## # A tibble: 1 x 3
    ##   sector description                                   jul_2021_employees
    ##   <chr>  <chr>                                                      <dbl>
    ## 1 81     Other Services (except Public Administration)               5709

We're getting very close to the finished table we showed at the beginning.

But right now, each bit of sector information is separated between 19 different dataframes.

We want them in one dataframe.

We can fix this by creating an empty dataframe called "employment_by_sector_all" using tibble(), placing it before our "for loop."

And inside our "for loop" at the end, we'll bind each employment_info dataframe to the newly created empty dataframe.

``` 
# Create an empty dataframe to hold results 
employment_by_sector_all <- tibble()


# For loop, iterating over each row in our naics industry dataframe
for(row_number in 1:nrow(naics_industry)) {
    
    # Keep only the row for a given row number, get rid of every other row
    each_row_df <- naics_industry %>%
      slice(row_number) 
      
    # Define url of page to get
    url <- each_row_df$sector_url
    
    # Define id of table to ingest
    xpath_employment_table <- paste0('//*[@id="',each_row_df$sector_xpath_id,'"]')
    
    # Get employment table from each page by going to each url defined above, reading in the html with read_html(), extracting the table with the id generated by the xpath code using html_elements), and then turning the html into a proper dataframe using html_table().  The dataframe is in a nested list, which we'll have to extract in the next step.
    employment_info <- url %>%
      read_html() %>%
      html_elements(xpath = xpath_employment_table) %>%
      html_table() 
    
    # Grab the dataframe out of the list (it's the first and only element inside the list); clean up the field names with clean_names(); use slice(2) to keep only the second row; use bind_cols() to append the sector code and name to this table; turn jul_2021 column into a proper number, and rename it.  Then select only three columns we need. 
    employment_info <- employment_info[[1]] %>%
      clean_names() %>%
      slice(2) %>% 
      bind_cols(each_row_df) %>%
      mutate(jul_2021 = parse_number(jul_2021)) %>%
      rename(jul_2021_employees = jul_2021) %>%
      select(sector,description,jul_2021_employees) 
    
    # Bind each individual employment info table to our employment_by_sector_all dataframe
    employment_by_sector_all <- employment_by_sector_all %>%
      bind_rows(employment_info)
    
}

# Display the completed dataframe
employment_by_sector_all
```

    ## # A tibble: 19 x 3
    ##    sector description                                          jul_2021_employe…
    ##    <chr>  <chr>                                                            <dbl>
    ##  1 11     Agriculture, Forestry, Fishing and Hunting                         7.6
    ##  2 21     Mining, Quarrying, and Oil and Gas Extraction                    592. 
    ##  3 22     Utilities                                                        539. 
    ##  4 23     Construction                                                    7425  
    ##  5 31-33  Manufacturing                                                  12389  
    ##  6 42     Wholesale Trade                                                 5722. 
    ##  7 44-45  Retail Trade                                                   15355. 
    ##  8 48-49  Transportation and Warehousing                                  5793. 
    ##  9 51     Information                                                     2745  
    ## 10 52     Finance and Insurance                                           6545. 
    ## 11 53     Real Estate and Rental and Leasing                              2292. 
    ## 12 54     Professional, Scientific, and Technical Services                9839  
    ## 13 55     Management of Companies and Enterprises                         2330. 
    ## 14 56     Administrative and Support and Waste Management and…            8770. 
    ## 15 61     Educational Services                                            3576. 
    ## 16 62     Health Care and Social Assistance                              20045. 
    ## 17 71     Arts, Entertainment, and Recreation                             2093. 
    ## 18 72     Accommodation and Food Services                                13115. 
    ## 19 81     Other Services (except Public Administration)                   5709

Ta da! The end result is a nice tidy dataframe with the number of employees in June 2021 for each sector.

It's always a good idea to spot check the results, especially any values that look suspciously high or low.

The value for "Agriculture, Forestry, Fishing and Hunting" seems suspiciously low, compared with the other values.

Let's figure out why.

Here's the table on the mining sector page: <https://www.bls.gov/iag/tgs/iag21.htm>


In the second row of this table, it has the unemployment rate. Nowhere on the page can we find information on the number of employees. We would need to do additional research to track down a valid number if we plan on using this table, but for now we're going to replace it with an NA using na_if.

``` 

# remove the suspicious value for agriculture. 
employment_by_sector_all <- employment_by_sector_all %>%
  mutate(jul_2021_employees = na_if(jul_2021_employees,7.5))

# display it
employment_by_sector_all
```

    ## # A tibble: 19 x 3
    ##    sector description                                          jul_2021_employe…
    ##    <chr>  <chr>                                                            <dbl>
    ##  1 11     Agriculture, Forestry, Fishing and Hunting                         7.6
    ##  2 21     Mining, Quarrying, and Oil and Gas Extraction                    592. 
    ##  3 22     Utilities                                                        539. 
    ##  4 23     Construction                                                    7425  
    ##  5 31-33  Manufacturing                                                  12389  
    ##  6 42     Wholesale Trade                                                 5722. 
    ##  7 44-45  Retail Trade                                                   15355. 
    ##  8 48-49  Transportation and Warehousing                                  5793. 
    ##  9 51     Information                                                     2745  
    ## 10 52     Finance and Insurance                                           6545. 
    ## 11 53     Real Estate and Rental and Leasing                              2292. 
    ## 12 54     Professional, Scientific, and Technical Services                9839  
    ## 13 55     Management of Companies and Enterprises                         2330. 
    ## 14 56     Administrative and Support and Waste Management and…            8770. 
    ## 15 61     Educational Services                                            3576. 
    ## 16 62     Health Care and Social Assistance                              20045. 
    ## 17 71     Arts, Entertainment, and Recreation                             2093. 
    ## 18 72     Accommodation and Food Services                                13115. 
    ## 19 81     Other Services (except Public Administration)                   5709

And we're done.

A note about advanced scraping -- every site is different. Every time you want to scrape a site, you'll be puzzling over different problems. But the steps remain the same: find a pattern, exploit it, clean the data on the fly and put it into a place to store it.

`<!--chapter:end:15-advancedrvest.Rmd-->`{=html}



#  Intro to APIs: The Census {number="17"}

There is truly an astonishing amount of data collected by the US Census Bureau. First, there's the Census that most people know -- the every 10 year census. That's the one mandated by the Constitution where the government attempts to count every person in the US. It's a mind-boggling feat to even try, and billions get spent on it. That data is used first for determining how many representatives each state gets in Congress. From there, the Census gets used to divide up billions of dollars of federal spending.

To answer the questions the government needs to do that, a ton of data gets collected. That, unfortunately, means the Census is exceedingly complicated to work with. The good news is, the Census has an API -- an application programming interface. What that means is we can get data directly through the Census Bureau via calls over the internet.

Let's demonstrate.

We're going to use a library called `tidycensus` which makes calls to the Census API in a very tidy way, and gives you back tidy data. That means we don't have to go through the process of importing the data from a file. I can't tell you how amazing this is, speaking from experience. The documentation for this library is [here](https://walker-data.com/tidycensus/). Another R library for working with Census APIs (there is more than one) is [this one](https://github.com/hrecht/censusapi) from Hannah Recht, a journalist with Kaiser Health News.

First we need to install `tidycensus` using the console: `install.packages("tidycensus")`

``` 
library(tidyverse)
library(tidycensus)
```

To use the API, you need an API key. To get that, you need to [apply for an API key with the Census Bureau](https://api.census.gov/data/key_signup.html). It takes a few minutes and you need to activate your key via email. Once you have your key, you need to set that for this session. Just FYI: Your key is your key. Do not share it around.

``` 
census_api_key("YOUR KEY HERE", install=TRUE)
```

The two main functions in tidycensus are `get_decennial`, which retrieves data from the 2000 and 2010 Censuses (and soon the 2020 Census), and `get_acs`, which pulls data from the American Community Survey, a between-Censuses annual survey that provides estimates, not hard counts, but asks more detailed questions. If you're new to Census data, there's [a very good set of slides from Kyle Walker](http://walker-data.com/umich-workshop/census-data-in-r/slides/#1), the creator of tidycensus, and he's working on a [book](https://walker-data.com/census-r/index.html) that you can read for free online.

It's important to keep in mind that Census data represents people - you, your neighbors and total strangers. It also requires some level of definitions, especially about race & ethnicity, that may or may not match how you define yourself or how others define themselves.

So to give you some idea of how complicated the data is, let's pull up just one file from the decennial Census. We'll use Summary File 1, or SF1. That has the major population and housing stuff.

``` 
sf1 <- load_variables(2010, "sf1", cache = TRUE)

sf1
```

    ## # A tibble: 8,959 x 3
    ##    name    label                                concept         
    ##    <chr>   <chr>                                <chr>           
    ##  1 H001001 Total                                HOUSING UNITS   
    ##  2 H002001 Total                                URBAN AND RURAL 
    ##  3 H002002 Total!!Urban                         URBAN AND RURAL 
    ##  4 H002003 Total!!Urban!!Inside urbanized areas URBAN AND RURAL 
    ##  5 H002004 Total!!Urban!!Inside urban clusters  URBAN AND RURAL 
    ##  6 H002005 Total!!Rural                         URBAN AND RURAL 
    ##  7 H002006 Total!!Not defined for this file     URBAN AND RURAL 
    ##  8 H003001 Total                                OCCUPANCY STATUS
    ##  9 H003002 Total!!Occupied                      OCCUPANCY STATUS
    ## 10 H003003 Total!!Vacant                        OCCUPANCY STATUS
    ## # … with 8,949 more rows

Note: There are thousands of variables in SF1. That's not a typo. Open it in your environment by double clicking. As you scroll down, you'll get an idea of what you've got to choose from.

If you think that's crazy, try the SF3 file from 2000.

``` 
sf3 <- load_variables(2000, "sf3", cache = TRUE)

sf3
```

    ## # A tibble: 16,520 x 3
    ##    name    label                         concept                                
    ##    <chr>   <chr>                         <chr>                                  
    ##  1 H001001 Total                         HOUSING UNITS [1]                      
    ##  2 H002001 Total                         UNWEIGHTED SAMPLE HOUSING UNITS BY OCC…
    ##  3 H002002 Total!!Occupied               UNWEIGHTED SAMPLE HOUSING UNITS BY OCC…
    ##  4 H002003 Total!!Vacant                 UNWEIGHTED SAMPLE HOUSING UNITS BY OCC…
    ##  5 H003001 Total                         100-PERCENT COUNT OF HOUSING UNITS [1] 
    ##  6 H004001 Percent of occupied housing … PERCENT OF HOUSING UNITS IN SAMPLE BY …
    ##  7 H004002 Percent of vacant housing un… PERCENT OF HOUSING UNITS IN SAMPLE BY …
    ##  8 H005001 Total                         URBAN AND RURAL [7]                    
    ##  9 H005002 Total!!Urban                  URBAN AND RURAL [7]                    
    ## 10 H005003 Total!!Urban!!Inside urbaniz… URBAN AND RURAL [7]                    
    ## # … with 16,510 more rows

Yes. That's more than 16,000 variables to choose from. I told you. Astonishing.

So let's try to answer a question using the Census. What is the fastest growing state since 2000?

To answer this, we need to pull the total population by state in each of the decennial census. Here's 2000.

``` 
p00 <- get_decennial(geography = "state", variables = "P001001", year = 2000)
```

Now 2010.

``` 
p10 <- get_decennial(geography = "state", variables = "P001001", year = 2010)
```

Let's take a peek at 2010.

``` 
p10
```

As you can see, we have a GEOID, NAME, then variable and value. Variable and value are going to be the same. Because those are named the same thing, to merge them together, we need to rename them.

``` 
p10 %>% select(GEOID, NAME, value) %>% rename(Population2010=value) -> p2010

p00 %>% select(GEOID, NAME, value) %>% rename(Population2000=value) -> p2000
```

Now we join the data together.

``` 
alldata <- p2000 %>% inner_join(p2010)
```

And now we calculate the percent change.

``` 
alldata %>% mutate(change = ((Population2010-Population2000)/Population2000)*100) %>% arrange(desc(change))
```

And just like that: Nevada.

You may be asking: hey, wasn't there a 2020 Census? Where's that data? The answer is that it's coming - the Census Bureau has a [schedule of releases](https://www.census.gov/programs-surveys/popest/about/schedule.html).

## 17.1 The ACS {number="17.1"}

In 2010, the Census Bureau replaced SF3 with the American Community Survey. The Good News is that the data would be updated on a rolling basis. The bad news is that it's more complicated because it's more like survey data with a large sample. That means there's margins of error and confidence intervals to worry about. By default, using `get_acs` fetches data from the 5-year estimates (currently 2015-2019), but you can specify 1-year estimates for jurisdictions with at least 65,000 people (many counties and cities).

Here's an example using the 5-year ACS estimates:

What is Maryland's richest county?

We can measure this by median household income. That variable is `B19013_001`, so we can get that data like this (I'm narrowing it to the top 20 for simplicity):

``` 
md <- get_acs(geography = "county",
              variables = c(medincome = "B19013_001"),
              state = "MD",
              year = 2019)
```

    ## Getting data from the 2015-2019 5-year ACS

``` 
md <- md %>% arrange(desc(estimate)) %>% top_n(20, estimate)

md
```

    ## # A tibble: 20 x 5
    ##    GEOID NAME                             variable  estimate   moe
    ##    <chr> <chr>                            <chr>        <dbl> <dbl>
    ##  1 24027 Howard County, Maryland          medincome   121160  2169
    ##  2 24009 Calvert County, Maryland         medincome   109313  3736
    ##  3 24031 Montgomery County, Maryland      medincome   108820  1009
    ##  4 24003 Anne Arundel County, Maryland    medincome   100798  1103
    ##  5 24017 Charles County, Maryland         medincome   100003  2950
    ##  6 24021 Frederick County, Maryland       medincome    97730  1897
    ##  7 24035 Queen Anne's County, Maryland    medincome    97034  3765
    ##  8 24013 Carroll County, Maryland         medincome    96769  1983
    ##  9 24037 St. Mary's County, Maryland      medincome    89845  3200
    ## 10 24025 Harford County, Maryland         medincome    89147  1748
    ## 11 24033 Prince George's County, Maryland medincome    84920   802
    ## 12 24015 Cecil County, Maryland           medincome    76887  2518
    ## 13 24005 Baltimore County, Maryland       medincome    76866   944
    ## 14 24041 Talbot County, Maryland          medincome    73547  3785
    ## 15 24047 Worcester County, Maryland       medincome    63499  2925
    ## 16 24043 Washington County, Maryland      medincome    60860  1550
    ## 17 24011 Caroline County, Maryland        medincome    58638  3620
    ## 18 24029 Kent County, Maryland            medincome    58598  5650
    ## 19 24045 Wicomico County, Maryland        medincome    56956  2596
    ## 20 24019 Dorchester County, Maryland      medincome    52917  3255

Howard, Calvert, Montgomery, Anne Arundel, Charles. What do they all have in common? Lots of suburban flight from DC and Baltimore. But do the margins of error let us say one county is richer than the other. We can find this out visually using error bars. Don't worry much about the code here -- we'll cover that soon enough.

``` 
md %>%
  mutate(NAME = gsub(" County, Maryland", "", NAME)) %>%
  ggplot(aes(x = estimate, y = reorder(NAME, estimate))) +
  geom_errorbarh(aes(xmin = estimate - moe, xmax = estimate + moe)) +
  geom_point(color = "red") +
  labs(title = "Household income by county in Maryland",
       subtitle = "2015-2019 American Community Survey",
       y = "",
       x = "ACS estimate (bars represent margin of error)")
```


As you can see, some of the error bars are quite wide. Some are narrow. But if the bars overlap, it means the difference between the two counties is within the margin of error, and the differences aren't statistically significant. So is the difference between Calvert and Montgomery significant? Nope. Is the difference between Howard and everyone else significant? Yes it is.

Let's ask another question of the ACS -- did any counties lose income from the time of the global financial crisis to the current 5-year window?

Let's re-label our first household income data.

``` 
md19 <- get_acs(geography = "county",
              variables = c(medincome = "B19013_001"),
              state = "MD",
              year = 2019)
```

    ## Getting data from the 2015-2019 5-year ACS

And now we grab the 2010 median household income.

``` 
md10 <- get_acs(geography = "county",
              variables = c(medincome = "B19013_001"),
              state = "MD",
              year = 2010)
```

    ## Getting data from the 2006-2010 5-year ACS

What I'm going to do next is a lot, but each step is simple. I'm going to join the data together, so each county has one line of data. Then I'm going to rename some fields that repeat. Then I'm going to calculate the minimium and maximum value of the estimate using the margin of error. That'll help me later. After that, I'm going to calculate a perent change and sort it by that change.

``` 
md10 %>%
  inner_join(md19, by=c("GEOID", "NAME")) %>%
  rename(estimate2010=estimate.x, estimate2019=estimate.y) %>%
  mutate(min2010 = estimate2010-moe.x, max2010 = estimate2010+moe.x, min2019 = estimate2019-moe.y, max2019 = estimate2019+moe.y) %>%
  select(-variable.x, -variable.y, -moe.x, -moe.y) %>%
  mutate(change = ((estimate2019-estimate2010)/estimate2010)*100) %>%
  arrange(change)
```

    ## # A tibble: 24 x 9
    ##    GEOID NAME  estimate2010 estimate2019 min2010 max2010 min2019 max2019  change
    ##    <chr> <chr>        <dbl>        <dbl>   <dbl>   <dbl>   <dbl>   <dbl>   <dbl>
    ##  1 24039 Some…        42443        37803   39092   45794   31139   44467 -10.9  
    ##  2 24011 Caro…        58799        58638   56740   60858   55018   62258  -0.274
    ##  3 24045 Wico…        50752        56956   49313   52191   54360   59552  12.2  
    ##  4 24037 St. …        80053        89845   77742   82364   86645   93045  12.2  
    ##  5 24017 Char…        88825       100003   87268   90382   97053  102953  12.6  
    ##  6 24047 Worc…        55487        63499   52749   58225   60574   66424  14.4  
    ##  7 24043 Wash…        52994        60860   51261   54727   59310   62410  14.8  
    ##  8 24023 Garr…        45760        52617   43729   47791   50065   55169  15.0  
    ##  9 24025 Harf…        77010        89147   75782   78238   87399   90895  15.8  
    ## 10 24031 Mont…        93373       108820   92535   94211  107811  109829  16.5  
    ## # … with 14 more rows

So according to this, Somerset and Caroline counties lost ground from the financial meltdown to now.

But did they?

Look at the min and max values for both. Is the change statistically significant?

The ACS data has lots of variables, just like the decennial Census does. To browse them, you can do this:

``` 
v19 <- load_variables(2019, "acs5", cache=TRUE)
```

And then view `v19` to see what kinds of variables are available via the API.

## 17.2 "Wide" Results {number="17.2"}

Although one of the chief strengths of tidycensus is that it offers a, well, tidy display of Census data, it also has the ability to view multiple variables spread across columns. This can be useful for creating percentages and comparing multiple variables.

## 17.3 Sorting Results {number="17.3"}

You'll notice that we've used `arrange` to sort the results of tidycensus functions, although that's done after we create a new variable to hold the data. There's another way to use `arrange` that you should know about, one that you can use for exploratory analysis. An example using median household income from 2019:

``` 
md19 <- get_acs(geography = "county",
              variables = c(medincome = "B19013_001"),
              state = "MD",
              year = 2019)
```

    ## Getting data from the 2015-2019 5-year ACS

``` 
arrange(md19, desc(estimate))
```

    ## # A tibble: 24 x 5
    ##    GEOID NAME                          variable  estimate   moe
    ##    <chr> <chr>                         <chr>        <dbl> <dbl>
    ##  1 24027 Howard County, Maryland       medincome   121160  2169
    ##  2 24009 Calvert County, Maryland      medincome   109313  3736
    ##  3 24031 Montgomery County, Maryland   medincome   108820  1009
    ##  4 24003 Anne Arundel County, Maryland medincome   100798  1103
    ##  5 24017 Charles County, Maryland      medincome   100003  2950
    ##  6 24021 Frederick County, Maryland    medincome    97730  1897
    ##  7 24035 Queen Anne's County, Maryland medincome    97034  3765
    ##  8 24013 Carroll County, Maryland      medincome    96769  1983
    ##  9 24037 St. Mary's County, Maryland   medincome    89845  3200
    ## 10 24025 Harford County, Maryland      medincome    89147  1748
    ## # … with 14 more rows

In this case we don't save the sorted results to a variable, we can just see the output in the console.

`<!--chapter:end:16-census.Rmd-->`{=html}


#  Visualizing your data for reporting {number="18"}

Visualizing data is becoming a much greater part of journalism. Large news organizations are creating graphics desks that create complex visuals with data to inform the public about important events.

To do it well is a course on its own. And not every story needs a feat of programming and art. Sometimes, you can help yourself and your story by just creating a quick chart, which helps you see patterns in the data that wouldn't otherwise surface.

Good news: one of the best libraries for visualizing data is in the tidyverse and it's pretty simple to make simple charts quickly with just a little bit of code. It's called [ggplot2](https://ggplot2.tidyverse.org/).

Let's revisit some data we've used in the past and turn it into charts. First, let's load libraries. When we load the tidyverse, we get ggplot2.

``` 
library(tidyverse)
```

The dataset we'll use is the PPP loan data for Maryland. Let's load it.

``` 
ppp_maryland <- read_csv("pre_labs/pre_lab_09/data/ppp_loans_md.csv.zip")
```

    ## 
    ## ── Column specification ────────────────────────────────────────────────────────
    ## cols(
    ##   .default = col_character(),
    ##   id = col_double(),
    ##   amount = col_double(),
    ##   naics_code = col_double(),
    ##   non_profit = col_logical(),
    ##   jobs_retained = col_double(),
    ##   date_approved = col_date(format = ""),
    ##   loan_range_sort_key = col_logical(),
    ##   previous_loan_range = col_logical(),
    ##   previous_name = col_logical(),
    ##   loan_number = col_double(),
    ##   sba_office_code = col_double(),
    ##   term = col_double(),
    ##   sba_guaranty_percentage = col_double(),
    ##   initial_approval_amount = col_double(),
    ##   current_approval_amount = col_double(),
    ##   undisbursed_amount = col_double(),
    ##   servicing_lender_location_id = col_double(),
    ##   utilities_proceed = col_double(),
    ##   payroll_proceed = col_double(),
    ##   mortgage_interest_proceed = col_double()
    ##   # ... with 12 more columns
    ## )
    ## ℹ Use `spec()` for the full column specifications.

    ## Warning: 12802 parsing failures.
    ##    row      col           expected                                           actual                                            file
    ## 170056 old_slug 1/0/T/F/TRUE/FALSE aditi-llc-d139eb25916444a03984f38eebda4e63       'pre_labs/pre_lab_09/data/ppp_loans_md.csv.zip'
    ## 170057 old_slug 1/0/T/F/TRUE/FALSE jvef-inc-00d405e42fed70949e474a678fb7cefe        'pre_labs/pre_lab_09/data/ppp_loans_md.csv.zip'
    ## 170058 old_slug 1/0/T/F/TRUE/FALSE mak-express-inc-9cc921dee107cb65c6728e818fb49c2a 'pre_labs/pre_lab_09/data/ppp_loans_md.csv.zip'
    ## 170059 old_slug 1/0/T/F/TRUE/FALSE pro-coat-llc-133a6b10843b022d479acb6bce5755c7    'pre_labs/pre_lab_09/data/ppp_loans_md.csv.zip'
    ## 170060 old_slug 1/0/T/F/TRUE/FALSE dvcanvass-llc-7b4219ba6ad6aa4b4b8fcb47b8d683c4   'pre_labs/pre_lab_09/data/ppp_loans_md.csv.zip'
    ## ...... ........ .................. ................................................ ...............................................
    ## See problems(...) for more details.

## 18.1 Bar charts {number="18.1"}

The first kind of chart we'll create is a simple bar chart.

It's a chart designed to show differences between things -- the magnitude of one thing, compared to the next thing, and the next, and the next.

So if we have thing, like a county, or a state, or a group name, and then a count of that group, we can make a bar chart.

So what does the chart of the top 10 maryland counties with the most total PPP loans look like?

First, we'll create a dataframe of those top 10, called maryland_ppp_top_counties.

``` 
maryland_ppp_top_counties <- ppp_maryland %>%
  group_by(project_county_name) %>%
  summarise(
    total_loans = n()
  ) %>% 
  arrange(desc(total_loans)) %>%
  head(10)

maryland_ppp_top_counties
```

    ## # A tibble: 10 x 2
    ##    project_county_name total_loans
    ##    <chr>                     <int>
    ##  1 MONTGOMERY                38782
    ##  2 PRINCE GEORGES            34409
    ##  3 BALTIMORE                 28789
    ##  4 BALTIMORE CITY            20004
    ##  5 ANNE ARUNDEL              17336
    ##  6 HOWARD                    12011
    ##  7 FREDERICK                  6666
    ##  8 HARFORD                    6301
    ##  9 CHARLES                    4398
    ## 10 CARROLL                    4040

Now let's create a bar chart using ggplot.

With ggplot, the first thing we'll always do is draw a blank canvas that will house our chart. We start with our dataframe name, and then (%\>%) we invoke the ggplot() function to make that blank canvas. All this does is make a gray box, the blank canvas that will hold our chart.

``` 
maryland_ppp_top_counties %>%
  ggplot()
```


Next we need to tell ggplot what kind of chart to make.

In ggplot, we work with two key concepts called geometries (abbreivated frequently as geom) and asthetics (abbreviated as aes).

Geometries are the shape that the data will take; think of line charts, bar charts, scatterplots, histograms, pie charts and other common graphics forms.

Asesthetics help ggplot know what component of our data to visualize -- why we'll visualize values from one column instead of another.

In a bar chart, we first pass in the data to the geometry, then set the aesthetic.

In the codeblock below, we've added a new function, geom_bar().

Using geom_bar() -- as opposed to geom_line() -- says we're making a bar chart.

Inside of that function, the asthetic, aes, says which columns to use in drawing the chart.

We're setting the values on the x axis (horizontal) to be the name of the county. We set weight to total loans, and it uses that value to "weight" or set the height of each bar.

One quirk here with ggplot.

After we've invoked the ggplot() function, you'll notice we're using a + symbol. It means the same thing as %\>% -- "and then do this." It's just a quirk of ggplot() that after you invoke the ggplot() function, you use + instead of %\>%. It makes no sense to me either, just something to live with.

``` 
maryland_ppp_top_counties %>%
  ggplot() +
  geom_bar(aes(x=project_county_name, weight=total_loans))
```


This is a very basic chart. But it's hard to derive much meaning from this chart, because the counties aren't ordered from highest to lowest by total_loans. We can fix that by using the reorder() function to do just that:

``` 
maryland_ppp_top_counties %>%
  ggplot() +
  geom_bar(aes(x=reorder(project_county_name,total_loans), weight=total_loans))
```


This is a little more useful. But the bottom is kind of a mess, with overlapping names. We can fix that by flipping it from a vertical bar chart (also called a column chart) to a horizontal one. coord_flip() does that for you.

``` 
maryland_ppp_top_counties %>%
  ggplot() +
  geom_bar(aes(x=reorder(project_county_name,total_loans), weight=total_loans)) +
  coord_flip()
```


Is this art? No. Does it quickly tell you something meaningful? It does.

We're mainly going to use these charts to help us in reporting, so style isn't that important.

But it's worth mentioning that we can pretty up these charts for publication, if we wanted to, with some more code. To style the chart, we can change or even modify the "theme," a kind of skin that makes the chart look better.

It's kind of like applying CSS to html. Here I'm changing the theme slightly to remove the gray background with one of ggplot's built in themes, theme_minimal()

``` 
maryland_ppp_top_counties %>%
  ggplot() +
  geom_bar(aes(x=reorder(project_county_name,total_loans), weight=total_loans)) +
  coord_flip() + 
  theme_minimal()
```


First, you have to install and load a package that contains lots of extra themes, called [ggthemes](https://yutannihilation.github.io/allYourFigureAreBelongToUs/ggthemes/).

``` 
#install.packages('ggthemes')
library(ggthemes)
```

And now we'll apply the economist theme from that package with theme_economist()

``` 
maryland_ppp_top_counties %>%
  ggplot() +
  geom_bar(aes(x=reorder(project_county_name,total_loans), weight=total_loans)) +
  coord_flip() + 
  theme_economist()
```


``` 
maryland_ppp_top_counties %>%
  ggplot() +
  geom_bar(aes(x=reorder(project_county_name,total_loans), weight=total_loans)) +
  coord_flip() + 
  theme_economist() +
  labs(
    title="Maryland Counties with Most PPP Loans",
    x = "total loans",
    y = "county",
    caption = "source: SBA PPP loan database"
    
  )
```


## 18.2 Line charts {number="18.2"}

Let's look at how to make another common chart type that will help you understand patterns in your data.

Line charts can show change over time. It works much the same as a bar chart, code wise, but instead of a weight, it uses a y.

So, let's create a dataframe with a count of Maryland loans for each date in our dataframe.

``` 
ppp_maryland_loans_by_date <- ppp_maryland %>%
  group_by(date_approved) %>%
  summarise(
    total_loans=n()
  )

ppp_maryland_loans_by_date 
```

    ## # A tibble: 235 x 2
    ##    date_approved total_loans
    ##    <date>              <int>
    ##  1 2020-04-03             28
    ##  2 2020-04-04            262
    ##  3 2020-04-05            487
    ##  4 2020-04-06            830
    ##  5 2020-04-07           1164
    ##  6 2020-04-08           1354
    ##  7 2020-04-09           1777
    ##  8 2020-04-10           1728
    ##  9 2020-04-11           1243
    ## 10 2020-04-12            528
    ## # … with 225 more rows

And now let's make a line chart to look for patterns in this data.

We'll put the date on the x axis and total loans on the y axis.

``` 
ppp_maryland_loans_by_date %>%
  ggplot() + 
  geom_line(aes(x=date_approved, y=total_loans))
```


It's not super pretty, but there's an obvious pattern! There are a ton of loans right at the beginning of the program. There's a trickle for the next few months, and then no loans at all for several months.

At the beginning of 2021, there's another spike, and a pretty steady level with some fluctuations until July 2021. We know from previous chapters the explanation for this: there was a flood of loans when the program was first authorized, but it eventually ran out of money, and then it was later reauthorized.

Right now, it's kind of hard to see specifics, though. Exactly when did loans fall to zero? August 2020?

We can't really tell. So let's modify the x axis to have one tick mark and label per month. We can do that with a function called scale_x_date().

We'll set the date_breaks to appear for every month; if we wanted every week, we'd say date_breaks = "1 week." We can set the date to appear as month abbreviated name (%b) and four-digit year (%Y).

``` 
ppp_maryland_loans_by_date %>%
  ggplot() + 
  geom_line(aes(x=date_approved, y=total_loans)) + 
  scale_x_date(date_breaks = "1 month", date_labels = "%b-%Y")
```


Those are a little hard to read, so we can turn them 45 degrees to remove the overlap using the theme() function for styling. With "axis.text.x = element_text(angle = 45, hjust=1)" we're saying, turn the date labels 45 degrees.

``` 
ppp_maryland_loans_by_date %>%
  ggplot() + 
  geom_line(aes(x=date_approved, y=total_loans)) + 
  scale_x_date(date_breaks = "1 month", date_labels = "%b-%Y") +
  theme(
    axis.text.x = element_text(angle = 45,  hjust=1)
  )
```


Again, this isn't as pretty as we could make it. But by charting this, we can quickly see a pattern that can help guide our reporting.

We're just scratching the surface of what ggplot can do, and chart types. There's so much more you can do, so many other chart types you can make. But the basics we've shown here will get you started.

`<!--chapter:end:17-visualizingforreporting.Rmd-->`{=html}



#  Visualizing your data for publication {number="19"}

Doing data visualization well, and at professional level, takes time, skill and practice to perfect. Understanding it and doing it at a complex level is an entire class on it's own. It uses some of the same skills here -- grouping, filtering, calculating -- but then takes that data and turns it into data pictures.

But simple stuff -- and even some slightly complicated stuff -- can be done with tools made for people who aren't data viz pros.

The tool we're going to use is called [Datawrapper](https://www.datawrapper.de/).

First, let's get some data and work with it. Let's use a cleaned-up version of 2021 PPP loan totals by type of lender. Let's look at it.

``` 
library(tidyverse)
```

``` 
lender_types <- read_csv("data/lender_totals_2021.csv")
```

    ## 
    ## ── Column specification ────────────────────────────────────────────────────────
    ## cols(
    ##   type = col_character(),
    ##   net_dollars = col_double()
    ## )

``` 
head(lender_types)
```

    ## # A tibble: 6 x 2
    ##   type                                  net_dollars
    ##   <chr>                                       <dbl>
    ## 1 Banks and S&Ls ($10B+)               118331350203
    ## 2 Banks and S&Ls (<$10B)               101504685266
    ## 3 Fintechs (and other State Regulated)  21918632833
    ## 4 Small Business Lending Companies      15463750507
    ## 5 Microlenders                           8540740467
    ## 6 Credit Unions (<$10B)                  5160428953

## 19.1 Datawrapper {number="19.1"}

Making charts in Datawrapper is preposterously simple, which is the point. There are dozens of chart types, and dozens of options. To get from a csv to a chart to publication is very, very easy.

First, go to [datawrapper.de](https://www.datawrapper.de/) and sign up for an account. It's free.

Once logged in, you'll click on New Chart.


The first thing we'll do is upload our CSV that we created before. Click on XLS/CSV and upload the file.


Next up is to check and see what Datawrappper did with our data when we uploaded it. As you can see from the text on the left, if it's blue, it's a number. If it's green, it's a date. If it's black, it's text. Red means there's a problem. This data is very clean, so it imports cleanly. Click on the "Proceed" button.


Click on Refine. The first option we want to change is the Number Format, because we have currency figures to display and we want to make it as easy as possible for readers to understand what we're displaying. Datawrapper has an excellent reference for its [custom formats](https://academy.datawrapper.de/article/207-custom-number-formats-that-you-can-display-in-datawrapper) that you can consult. Let's choose `$0.[00]a`, which adds a dollar sign and abbreviates larger amounts:


Now we need to annotate our charts. Every chart needs a title, a source line and a credit line. Most need chatter (called description here). Click on the "Annotate" tab to get started.

Really think about the title and description: the title is like a headline and the description is provides some additional context. Another way to think about it: the title is the most important lesson from the graphic, and the description could be the next most important lesson or could provide more context to the title.


To publish, we click the "Publish & Embed" tab. Some publication systems allow for the embedding of HTML into a post or a story. Some don't. The only way to know is to ask someone at your publication. Every publication system on the planet, though, can publish an image. So there's always a way to export your chart as a PNG file, which you can upload like any photo.


### 19.1.1 Making a Map {number="19.1.1"}

Let's create a choropleth map - one that shows variations between the total number of approved PPP applications across Maryland counties. First, we'll need to generate that data using our collection of Maryland PPP loans.

``` 
maryland_ppp <- read_rds("data/maryland_ppp.rds")
```

First, we'll create a dataframe that has county (jurisdiction) level counts of approved applications. Run the following code to do that. There are some mistakes in the data, so we're going to remove those with a filter after doing the counting.

``` 
md_counties <- maryland_ppp %>%
    group_by(project_county_name) %>%
    summarise(count=n())
```

Let's deal with those seemingly extraneous records that don't appear to be MD PPP applications:

``` 
md_counties <- maryland_ppp %>%
    group_by(project_county_name) %>%
    summarise(count=n()) %>%
    filter(count > 6)
```

In order to make a map, we need to be able to tell Datawrapper that a certain column contains geographic information (besides the name of the county). The easiest way to do that for U.S. maps is to use something called a [FIPS Code](https://www.census.gov/programs-surveys/geography/guidance/geo-identifiers.html). You should read about them so you understand what they are, and think of them as a unique identifier for some geographical entity like a state or county. Our maryland_ppp dataframe doesn't have a FIPS code for each county, but this is a solved problem thanks to the Tigris library. Let's install it:

``` 
#install.packages('tigris',repos = "http://cran.us.r-project.org")
library(tigris)
```

    ## To enable 
    ## caching of data, set `options(tigris_use_cache = TRUE)` in your R script or .Rprofile.

    ## 
    ## Attaching package: 'tigris'

    ## The following object is masked from 'package:tidycensus':
    ## 
    ##     fips_codes

Once we've done that, we have access to a dataframe containing all fips codes. Let's isolate the Maryland codes:

``` 
all_fips <- fips_codes %>% as_tibble()
md_fips <- all_fips %>% filter(state == 'MD')
```

Looks good, but there are two issues: Datawrapper expects a 5-digit FIPS code (the state code plus the county code, so "24001" for Allegany County) and the county names don't match the `project_county_name` in the PPP data. Let's fix the first issue - adding a full FIPS code based on its components using the function `str_c`, which concatenates multiple strings:

``` 
md_fips <- md_fips %>% mutate(fips_code = str_c(state_code, county_code))
```

Now we'll deal with the county names in `md_counties`. They are all caps and contain no punctuation, we could:

1.  Change counties in `md_counties` to match `md_fips`
2.  Change counties in `md_fips` to match `md_counties`

Let's do the latter. We'll use mutate to create an uppercase version of the name, remove \" COUNTY\", replace the quotemarks with nothing and change St. Mary's so it matches the PPP data:

Change the county names in `md_fips`

``` 
md_fips <- md_fips %>% mutate(match_county = str_to_upper(county)) %>%
   mutate(match_county = str_replace(match_county, ' COUNTY', '')) %>%
   mutate(match_county = str_replace(match_county, "'", "")) %>%
   mutate(match_county = str_replace(match_county, "ST. MARY", "SAINT MARY"))
```

Now we'll join `md_counties` and `md_fips` together using our new `match_county` column:

``` 
md_counties_with_fips <- md_counties %>%
  left_join(md_fips, by=c('project_county_name'='match_county'))
```

Then we'll write `md_counties_with_fips` to a CSV in the data folder using write_csv:

``` 
write_csv(md_counties_with_fips, "data/md_counties.csv")
```

Go back to Datawrapper and click on "New Map." Click on "Choropleth map" and then choose "USA \>\> Counties (2018)" for the map base and click the Proceed button.

Now we can upload the `md_counties.csv` file we just saved using the Upload File button. It should look like the following image:


We'll need to make sure that Datawrapper understands what the data is and where the FIPS code is. Click on the "Match" tab and make sure that yours looks like the image below:


Click the "Proceed" button (you should have to click it twice, since the first time it will tell you that there's no data for 3,199 counties - the rest of the U.S.). That will take you to the Visualize tab.

You'll see that the map currently is of the whole nation, and we only have Maryland data. Let's fix that.

Look for "Hide regions without data" under Appearance, and click the slider icon to enable that feature. You should see a map zoomed into Maryland with some counties in various colors.

But it's a little rough visually, so let's clean that up.

Look for the "Show color legend" label and add a caption for the legend, which is the horizontal bar under the title. It represents the extent of the data from smallest number of loans to largest. Then click on the "Annotate" tab to add a title, description, data source and byline. The title should represent the headline, while the description should be a longer phrase that tells people what they are looking at.

That's better, but check out the tooltip by hovering over a county. It's not super helpful. Let's change the tooltip behavior to show the county name and a better-formatted number.

Click the "Customize tooltips" button so it expands down. Change {{ fips }} to {{ county }} and {{ count }} to {{ FORMAT(count, "0,0.\[00\]")}}

Ok, that looks better. Let's publish!

Click the "Proceed" button until you get to the "Publish & Embed" tab, then click "Publish Now."

`<!--chapter:end:18-visualizingforpublication.Rmd-->`{=html}


#  Geographic data basics {number="20"}

Up to now, we've been looking at patterns in data for what is more than this, or what's the middle look like. We've calculated metrics like per capita rates, or looked at how data changes over time.

Another way we can look at the data is geographically. Is there a spatial pattern to our data? Can we learn anything by using distance as a metric? What if we merge non-geographic data into geographic data?

The bad news is that there isn't a One Library To Rule Them All when it comes to geo queries in R. But there's one emerging, called Simple Features, that is very good.

Go to the console and install it with `install.packages("sf")`

To understand geographic queries, you have to get a few things in your head first:

1.  Your query is using planar space. Usually that's some kind of projection of the world. If you're lucky, your data is projected, and the software will handle projection differences under the hood without you knowing anything about it.
2.  Projections are cartographers making opinionated decisions about what the world should look like when you take a spheroid -- the earth isn't perfectly round -- and flatten it. Believe it or not, every state in the US has their own geographic projection. There's dozens upon dozens of them.
3.  Geographic queries work in layers. In most geographic applications, you'll have multiple layers. You'll have a boundary file, and a river file, and a road file, and a flood file and combined together they make the map. But you have to think in layers.
4.  See 1. With layers, they're all joined together by the planar space. So you don't need to join one to the other like we did earlier -- the space has done that. So you can query how many X are within the boundaries on layer Y. And it's the plane that holds them together.


## 20.1 Importing and viewing data {number="20.1"}

Let's start with the absolute basics of geographic data: loading and viewing. Load libraries as usual.

``` 
library(tidyverse)
library(sf)
```

    ## Linking to GEOS 3.8.1, GDAL 3.2.1, PROJ 7.2.1

``` 
library(janitor)
```

First: an aside on geographic data. There are many formats for geographic data, but data type you'll see the most is called the shapefile. It comes from a company named ERSI, which created the most widely used GIS software in the world. For years, they were the only game in town, really, and the shapefile became ubiquitous, especially so in government and utilities.

So more often than not, you'll be dealing with a shapefile. But a shapefile isn't just a single file -- it's a collection of files that combined make up all the data that allow you to use it. There's a .shp file -- that's the main file that pulls it all together -- but it's important to note if your shapefiles has a .prj file, which indicates that the projection is specified.

The data we're going to be working with is a file from the Department of Homeland Security that is every hospital in the US and the number of beds they have. I'm writing this during the days of coronavirus, and suddenly the number of hospital beds is a top concern. So let's look at where hospital beds are and how many of them are there.

When you do, it should look something like this:


Simlar to `readr`, the `sf` library has functions to read geographic data. In this case, we're going to use `st_read` to read in our hospitals data. And then glimpse it to look at the columns.

``` 
hospitals <- st_read("data/Hospitals/Hospitals.shp")
```

    ## Reading layer `Hospitals' from data source 
    ##   `/Users/derekwillis/code/datajournalismbook/data/Hospitals/Hospitals.shp' 
    ##   using driver `ESRI Shapefile'
    ## Simple feature collection with 7581 features and 32 fields
    ## Geometry type: POINT
    ## Dimension:     XY
    ## Bounding box:  xmin: -176.6403 ymin: -14.29024 xmax: 145.7245 ymax: 71.29285
    ## Geodetic CRS:  WGS 84

``` 
glimpse(hospitals)
```

    ## Rows: 7,581
    ## Columns: 33
    ## $ OBJECTID   <dbl> 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, …
    ## $ ID         <chr> "0005793230", "0053391362", "0011190023", "0017090028", "00…
    ## $ NAME       <chr> "CENTRAL VALLEY GENERAL HOSPITAL", "LOS ROBLES HOSPITAL & M…
    ## $ ADDRESS    <chr> "1025 NORTH DOUTY STREET", "150 VIA MERIDA", "4060 WHITTIER…
    ## $ CITY       <chr> "HANFORD", "WESTLAKE VILAGE", "LOS ANGELES", "HOLLYWOOD", "…
    ## $ STATE      <chr> "CA", "CA", "CA", "CA", "CA", "CA", "CA", "CA", "CA", "CA",…
    ## $ ZIP        <chr> "93230", "91362", "90023", "90028", "91706", "90712", "9101…
    ## $ ZIP4       <chr> "NOT AVAILABLE", "NOT AVAILABLE", "NOT AVAILABLE", "NOT AVA…
    ## $ TELEPHONE  <chr> "NOT AVAILABLE", "NOT AVAILABLE", "NOT AVAILABLE", "(323) 4…
    ## $ TYPE       <chr> "GENERAL ACUTE CARE", "GENERAL ACUTE CARE", "GENERAL ACUTE …
    ## $ STATUS     <chr> "CLOSED", "OPEN", "OPEN", "OPEN", "OPEN", "OPEN", "OPEN", "…
    ## $ POPULATION <dbl> 49, 62, 127, 100, 95, 172, 49, 101, 16, 78, 87, 269, 42, 27…
    ## $ COUNTY     <chr> "KINGS", "VENTURA", "LOS ANGELES", "LOS ANGELES", "LOS ANGE…
    ## $ COUNTYFIPS <chr> "06031", "06111", "06037", "06037", "06037", "06037", "0603…
    ## $ COUNTRY    <chr> "USA", "USA", "USA", "USA", "USA", "USA", "USA", "USA", "US…
    ## $ LATITUDE   <dbl> 36.33616, 34.15494, 34.02365, 34.09639, 34.06304, 33.85971,…
    ## $ LONGITUDE  <dbl> -119.64567, -118.81574, -118.18416, -118.32523, -117.96744,…
    ## $ NAICS_CODE <chr> "622110", "622110", "622110", "622110", "622110", "622110",…
    ## $ NAICS_DESC <chr> "GENERAL MEDICAL AND SURGICAL HOSPITALS", "GENERAL MEDICAL …
    ## $ SOURCE     <chr> "http://www.oshpd.ca.gov/HID/Facility-Listing.html", "http:…
    ## $ SOURCEDATE <chr> "2016-02-04T00:00:00.000Z", "2018-08-08T00:00:00.000Z", "20…
    ## $ VAL_METHOD <chr> "IMAGERY/OTHER", "IMAGERY/OTHER", "IMAGERY/OTHER", "IMAGERY…
    ## $ VAL_DATE   <chr> "2014-02-10T00:00:00.000Z", "2014-02-10T00:00:00.000Z", "20…
    ## $ WEBSITE    <chr> "http://www.hanfordhealth.com", "http://www.losrobleshospit…
    ## $ STATE_ID   <chr> "NOT AVAILABLE", "NOT AVAILABLE", "NOT AVAILABLE", "NOT AVA…
    ## $ ALT_NAME   <chr> "NOT AVAILABLE", "NOT AVAILABLE", "NOT AVAILABLE", "HOLLYWO…
    ## $ ST_FIPS    <chr> "06", "06", "06", "06", "06", "06", "06", "06", "06", "06",…
    ## $ OWNER      <chr> "PROPRIETARY", "PROPRIETARY", "PROPRIETARY", "PROPRIETARY",…
    ## $ TTL_STAFF  <dbl> -999, -999, -999, -999, -999, -999, -999, -999, -999, -999,…
    ## $ BEDS       <dbl> 49, 62, 127, 100, 95, 172, 49, 101, 16, 78, 87, 269, 42, 27…
    ## $ TRAUMA     <chr> "NOT AVAILABLE", "NOT AVAILABLE", "NOT AVAILABLE", "NOT AVA…
    ## $ HELIPAD    <chr> "N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "Y", "N",…
    ## $ geometry   <POINT [°]> POINT (-119.6457 36.33616), POINT (-118.8157 34.15494…

This looks like a normal dataframe, and mostly it is. We have one row per hospital, and each column is some feature of that hospital: the name, the address, it's open/closed status and more. What sets this data apart from other dataframes we've used is the last column, "geometry," which is of a new data type. It's not a character or a number, it's a "POINT," which is composed of a longitude value and a latitude value. When we plot these on a grid of latitude and longitude, it will place a point where those two numbers intersect.

Let's look at just Maryland hospitals. Good news -- `sf` plays very nicely with the tidyverse, so we can filter data the way we are accustomed.

``` 
md_hospitals <- hospitals %>% 
  filter(STATE == "MD")

md_hospitals
```

    ## Simple feature collection with 72 features and 32 fields
    ## Geometry type: POINT
    ## Dimension:     XY
    ## Bounding box:  xmin: -79.40098 ymin: 37.99756 xmax: -75.21133 ymax: 39.677
    ## Geodetic CRS:  WGS 84
    ## First 10 features:
    ##    OBJECTID         ID
    ## 1       234 0003120785
    ## 2       364 0000921287
    ## 3       365 0001021205
    ## 4       366 0002321202
    ## 5       367 0003721215
    ## 6       368 0004121201
    ## 7       370 0004821224
    ## 8       397 0003421740
    ## 9       404 0003521742
    ## 10      443 0001920910
    ##                                                          NAME
    ## 1  GLADYS SPELLMAN SPECIALTY HOSPITAL AND NURSING CARE CENTER
    ## 2                                      JOHNS HOPKINS HOSPITAL
    ## 3                                   KENNEDY KREIGER INSTITUTE
    ## 4                                        MERCY MEDICAL CENTER
    ## 5                                 SINAI HOSPITAL OF BALTIMORE
    ## 6                       UNIVERSITY OF MARYLAND MEDICAL CENTER
    ## 7                        JOHNS HOPKINS BAYVIEW MEDICAL CENTER
    ## 8                                  BROOK LANE HEALTH SERVICES
    ## 9                                      MERITUS MEDICAL CENTER
    ## 10                                        HOLY CROSS HOSPITAL
    ##                      ADDRESS          CITY STATE   ZIP          ZIP4
    ## 1        3001 HOSPITAL DRIVE   HYATTSVILLE    MD 20785 NOT AVAILABLE
    ## 2    600 NORTH  WOLFE STREET     BALTIMORE    MD 21287 NOT AVAILABLE
    ## 3             707 N BROADWAY     BALTIMORE    MD 21205 NOT AVAILABLE
    ## 4          301 ST PAUL PLACE     BALTIMORE    MD 21202 NOT AVAILABLE
    ## 5    2401 WEST BELVEDERE AVE     BALTIMORE    MD 21215 NOT AVAILABLE
    ## 6             22 S GREENE ST     BALTIMORE    MD 21201 NOT AVAILABLE
    ## 7        4940 EASTERN AVENUE     BALTIMORE    MD 21224 NOT AVAILABLE
    ## 8     13218 BROOK LANE DRIVE    HAGERSTOWN    MD 21740 NOT AVAILABLE
    ## 9  11116 MEDICAL CAMPUS ROAD    HAGERSTOWN    MD 21742 NOT AVAILABLE
    ## 10     1500 FOREST GLEN ROAD SILVER SPRING    MD 20910 NOT AVAILABLE
    ##         TELEPHONE               TYPE STATUS POPULATION          COUNTY
    ## 1  (301) 497-7953    CHRONIC DISEASE CLOSED         30 PRINCE GEORGE'S
    ## 2  (410) 955-9540 GENERAL ACUTE CARE   OPEN        951  BALTIMORE CITY
    ## 3  (443) 923-9305 GENERAL ACUTE CARE   OPEN         70  BALTIMORE CITY
    ## 4  (410) 332-9237 GENERAL ACUTE CARE   OPEN        281  BALTIMORE CITY
    ## 5  (410) 601-5131 GENERAL ACUTE CARE   OPEN        467  BALTIMORE CITY
    ## 6  (410) 328-8667 GENERAL ACUTE CARE   OPEN        800  BALTIMORE CITY
    ## 7  (410) 550-0123 GENERAL ACUTE CARE   OPEN        477  BALTIMORE CITY
    ## 8  (301) 733-0330        PSYCHIATRIC   OPEN         65      WASHINGTON
    ## 9  (240) 313-9500 GENERAL ACUTE CARE   OPEN        247      WASHINGTON
    ## 10 (301) 754-7000 GENERAL ACUTE CARE   OPEN        409      MONTGOMERY
    ##    COUNTYFIPS COUNTRY LATITUDE LONGITUDE NAICS_CODE
    ## 1       24033     USA 38.93088 -76.92156     622110
    ## 2       24510     USA 39.29611 -76.59197     622110
    ## 3       24510     USA 39.29928 -76.59282     622110
    ## 4       24510     USA 39.29292 -76.61288     622110
    ## 5       24510     USA 39.35230 -76.66209     622110
    ## 6       24510     USA 39.28791 -76.62493     622110
    ## 7       24510     USA 39.29068 -76.54678     622110
    ## 8       24043     USA 39.67700 -77.61060     622110
    ## 9       24043     USA 39.62219 -77.68256     622110
    ## 10      24031     USA 39.01472 -77.03574     622110
    ##                                NAICS_DESC
    ## 1  GENERAL MEDICAL AND SURGICAL HOSPITALS
    ## 2  GENERAL MEDICAL AND SURGICAL HOSPITALS
    ## 3  GENERAL MEDICAL AND SURGICAL HOSPITALS
    ## 4  GENERAL MEDICAL AND SURGICAL HOSPITALS
    ## 5  GENERAL MEDICAL AND SURGICAL HOSPITALS
    ## 6  GENERAL MEDICAL AND SURGICAL HOSPITALS
    ## 7  GENERAL MEDICAL AND SURGICAL HOSPITALS
    ## 8  GENERAL MEDICAL AND SURGICAL HOSPITALS
    ## 9  GENERAL MEDICAL AND SURGICAL HOSPITALS
    ## 10 GENERAL MEDICAL AND SURGICAL HOSPITALS
    ##                                                          SOURCE
    ## 1  http://dhmh.maryland.gov/ohcq/docs/Forms/DispForm.aspx?ID=89
    ## 2   http://dhmh.maryland.gov/ohcq/pages/licensee-directory.aspx
    ## 3   http://dhmh.maryland.gov/ohcq/pages/licensee-directory.aspx
    ## 4   http://dhmh.maryland.gov/ohcq/pages/licensee-directory.aspx
    ## 5   http://dhmh.maryland.gov/ohcq/pages/licensee-directory.aspx
    ## 6   http://dhmh.maryland.gov/ohcq/pages/licensee-directory.aspx
    ## 7   http://dhmh.maryland.gov/ohcq/pages/licensee-directory.aspx
    ## 8   http://dhmh.maryland.gov/ohcq/pages/licensee-directory.aspx
    ## 9   http://dhmh.maryland.gov/ohcq/pages/licensee-directory.aspx
    ## 10  http://dhmh.maryland.gov/ohcq/pages/licensee-directory.aspx
    ##                  SOURCEDATE    VAL_METHOD                 VAL_DATE
    ## 1  2012-10-25T00:00:00.000Z       IMAGERY 2014-03-12T00:00:00.000Z
    ## 2  2018-08-09T00:00:00.000Z       IMAGERY 2014-02-10T00:00:00.000Z
    ## 3  2018-08-09T00:00:00.000Z       IMAGERY 2014-02-10T00:00:00.000Z
    ## 4  2018-08-09T00:00:00.000Z       IMAGERY 2014-02-10T00:00:00.000Z
    ## 5  2018-08-09T00:00:00.000Z       IMAGERY 2014-02-10T00:00:00.000Z
    ## 6  2018-08-09T00:00:00.000Z       IMAGERY 2014-02-10T00:00:00.000Z
    ## 7  2018-08-09T00:00:00.000Z IMAGERY/OTHER 2014-02-10T00:00:00.000Z
    ## 8  2018-08-09T00:00:00.000Z       IMAGERY 2014-02-10T00:00:00.000Z
    ## 9  2018-08-09T00:00:00.000Z       IMAGERY 2014-02-10T00:00:00.000Z
    ## 10 2018-08-09T00:00:00.000Z       IMAGERY 2014-02-10T00:00:00.000Z
    ##                                                                                        WEBSITE
    ## 1                                                              http://www.dimensionshealth.org
    ## 2                                                               http://www.hopkinsmedicine.org
    ## 3                                                                http://www.kennedykrieger.org
    ## 4                                                                       http://www.mdmercy.com
    ## 5                                            http://www.lifebridgehealth.org/Sinai/Sinai1.aspx
    ## 6                                                       http://www.umms.org/hospitals/ummc.htm
    ## 7                                                                http://www.hopkinsbayview.org
    ## 8                                                                     http://www.brooklane.org
    ## 9  http://www.meritushealth.com/For-Hospital-Patients-and-Visitors/Meritus-Medical-Center.aspx
    ## 10                                                              http://www.holycrosshealth.org
    ##         STATE_ID      ALT_NAME ST_FIPS       OWNER TTL_STAFF BEDS
    ## 1  NOT AVAILABLE NOT AVAILABLE      24 PROPRIETARY      -999   30
    ## 2  NOT AVAILABLE NOT AVAILABLE      24  NON-PROFIT      -999  951
    ## 3  NOT AVAILABLE NOT AVAILABLE      24  NON-PROFIT      -999   70
    ## 4  NOT AVAILABLE NOT AVAILABLE      24  NON-PROFIT      -999  281
    ## 5  NOT AVAILABLE NOT AVAILABLE      24  NON-PROFIT      -999  467
    ## 6  NOT AVAILABLE NOT AVAILABLE      24  NON-PROFIT      -999  800
    ## 7  NOT AVAILABLE NOT AVAILABLE      24  NON-PROFIT      -999  477
    ## 8  NOT AVAILABLE NOT AVAILABLE      24  NON-PROFIT      -999   65
    ## 9  NOT AVAILABLE NOT AVAILABLE      24  NON-PROFIT      -999  247
    ## 10 NOT AVAILABLE NOT AVAILABLE      24  NON-PROFIT      -999  409
    ##                      TRAUMA HELIPAD                   geometry
    ## 1             NOT AVAILABLE       Y POINT (-76.92156 38.93088)
    ## 2  LEVEL I, LEVEL PEDIATRIC       Y POINT (-76.59197 39.29611)
    ## 3             NOT AVAILABLE       Y POINT (-76.59282 39.29928)
    ## 4             NOT AVAILABLE       N POINT (-76.61288 39.29292)
    ## 5                  LEVEL II       Y  POINT (-76.66209 39.3523)
    ## 6                      PARC       Y POINT (-76.62493 39.28791)
    ## 7                  LEVEL II       Y POINT (-76.54678 39.29068)
    ## 8             NOT AVAILABLE       N    POINT (-77.6106 39.677)
    ## 9                 LEVEL III       Y POINT (-77.68256 39.62219)
    ## 10            NOT AVAILABLE       N POINT (-77.03574 39.01472)

We have 72 hospitals, according to this data.

What kind of hospitals do we have?

``` 
md_hospitals %>%
  group_by(TYPE) %>%
  summarise(
    count=n()
  ) %>%
  arrange(desc(count))
```

    ## Simple feature collection with 7 features and 2 fields
    ## Geometry type: GEOMETRY
    ## Dimension:     XY
    ## Bounding box:  xmin: -79.40098 ymin: 37.99756 xmax: -75.21133 ymax: 39.677
    ## Geodetic CRS:  WGS 84
    ## # A tibble: 7 x 3
    ##   TYPE           count                                                  geometry
    ##   <chr>          <int>                                            <GEOMETRY [°]>
    ## 1 GENERAL ACUTE…    50 MULTIPOINT ((-79.40098 39.41344), (-77.24226 39.18068), …
    ## 2 PSYCHIATRIC       11 MULTIPOINT ((-77.19896 39.09986), (-76.98002 39.00257), …
    ## 3 MILITARY           4 MULTIPOINT ((-77.09359 39.00129), (-76.06292 39.54994), …
    ## 4 CHRONIC DISEA…     2    MULTIPOINT ((-76.92156 38.93088), (-75.59572 38.3823))
    ## 5 LONG TERM CARE     2   MULTIPOINT ((-76.66465 39.35458), (-77.71631 39.66243))
    ## 6 REHABILITATION     2   MULTIPOINT ((-77.20068 39.09859), (-75.54862 38.36924))
    ## 7 SPECIAL            1                                POINT (-76.80099 39.37272)

Let's narrow our data to only look at the 50 "General Acute Care hospitals."

``` 
md_hospitals <- hospitals %>% 
  filter(STATE == "MD") %>%
  filter(TYPE == "GENERAL ACUTE CARE")

md_hospitals
```

    ## Simple feature collection with 50 features and 32 fields
    ## Geometry type: POINT
    ## Dimension:     XY
    ## Bounding box:  xmin: -79.40098 ymin: 37.99756 xmax: -75.21133 ymax: 39.64783
    ## Geodetic CRS:  WGS 84
    ## First 10 features:
    ##    OBJECTID         ID                                     NAME
    ## 1       364 0000921287                   JOHNS HOPKINS HOSPITAL
    ## 2       365 0001021205                KENNEDY KREIGER INSTITUTE
    ## 3       366 0002321202                     MERCY MEDICAL CENTER
    ## 4       367 0003721215              SINAI HOSPITAL OF BALTIMORE
    ## 5       368 0004121201    UNIVERSITY OF MARYLAND MEDICAL CENTER
    ## 6       370 0004821224     JOHNS HOPKINS BAYVIEW MEDICAL CENTER
    ## 7       404 0003521742                   MERITUS MEDICAL CENTER
    ## 8       443 0001920910                      HOLY CROSS HOSPITAL
    ## 9       446 0002520744                 FORT WASHINGTON HOSPITAL
    ## 10      473 0004521502 WESTERN MARYLAND REGIONAL MEDICAL CENTER
    ##                      ADDRESS            CITY STATE   ZIP          ZIP4
    ## 1    600 NORTH  WOLFE STREET       BALTIMORE    MD 21287 NOT AVAILABLE
    ## 2             707 N BROADWAY       BALTIMORE    MD 21205 NOT AVAILABLE
    ## 3          301 ST PAUL PLACE       BALTIMORE    MD 21202 NOT AVAILABLE
    ## 4    2401 WEST BELVEDERE AVE       BALTIMORE    MD 21215 NOT AVAILABLE
    ## 5             22 S GREENE ST       BALTIMORE    MD 21201 NOT AVAILABLE
    ## 6        4940 EASTERN AVENUE       BALTIMORE    MD 21224 NOT AVAILABLE
    ## 7  11116 MEDICAL CAMPUS ROAD      HAGERSTOWN    MD 21742 NOT AVAILABLE
    ## 8      1500 FOREST GLEN ROAD   SILVER SPRING    MD 20910 NOT AVAILABLE
    ## 9      11711 LIVINGSTON ROAD FORT WASHINGTON    MD 20744 NOT AVAILABLE
    ## 10    12500 WILLOWBROOK ROAD      CUMBERLAND    MD 21502 NOT AVAILABLE
    ##         TELEPHONE               TYPE STATUS POPULATION          COUNTY
    ## 1  (410) 955-9540 GENERAL ACUTE CARE   OPEN        951  BALTIMORE CITY
    ## 2  (443) 923-9305 GENERAL ACUTE CARE   OPEN         70  BALTIMORE CITY
    ## 3  (410) 332-9237 GENERAL ACUTE CARE   OPEN        281  BALTIMORE CITY
    ## 4  (410) 601-5131 GENERAL ACUTE CARE   OPEN        467  BALTIMORE CITY
    ## 5  (410) 328-8667 GENERAL ACUTE CARE   OPEN        800  BALTIMORE CITY
    ## 6  (410) 550-0123 GENERAL ACUTE CARE   OPEN        477  BALTIMORE CITY
    ## 7  (240) 313-9500 GENERAL ACUTE CARE   OPEN        247      WASHINGTON
    ## 8  (301) 754-7000 GENERAL ACUTE CARE   OPEN        409      MONTGOMERY
    ## 9  (301) 292-7000 GENERAL ACUTE CARE   OPEN         37 PRINCE GEORGE'S
    ## 10 (240) 964-2196 GENERAL ACUTE CARE   OPEN        371        ALLEGANY
    ##    COUNTYFIPS COUNTRY LATITUDE LONGITUDE NAICS_CODE
    ## 1       24510     USA 39.29611 -76.59197     622110
    ## 2       24510     USA 39.29928 -76.59282     622110
    ## 3       24510     USA 39.29292 -76.61288     622110
    ## 4       24510     USA 39.35230 -76.66209     622110
    ## 5       24510     USA 39.28791 -76.62493     622110
    ## 6       24510     USA 39.29068 -76.54678     622110
    ## 7       24043     USA 39.62219 -77.68256     622110
    ## 8       24031     USA 39.01472 -77.03574     622110
    ## 9       24033     USA 38.72856 -76.99270     622110
    ## 10      24001     USA 39.64783 -78.73324     622110
    ##                                NAICS_DESC
    ## 1  GENERAL MEDICAL AND SURGICAL HOSPITALS
    ## 2  GENERAL MEDICAL AND SURGICAL HOSPITALS
    ## 3  GENERAL MEDICAL AND SURGICAL HOSPITALS
    ## 4  GENERAL MEDICAL AND SURGICAL HOSPITALS
    ## 5  GENERAL MEDICAL AND SURGICAL HOSPITALS
    ## 6  GENERAL MEDICAL AND SURGICAL HOSPITALS
    ## 7  GENERAL MEDICAL AND SURGICAL HOSPITALS
    ## 8  GENERAL MEDICAL AND SURGICAL HOSPITALS
    ## 9  GENERAL MEDICAL AND SURGICAL HOSPITALS
    ## 10 GENERAL MEDICAL AND SURGICAL HOSPITALS
    ##                                                         SOURCE
    ## 1  http://dhmh.maryland.gov/ohcq/pages/licensee-directory.aspx
    ## 2  http://dhmh.maryland.gov/ohcq/pages/licensee-directory.aspx
    ## 3  http://dhmh.maryland.gov/ohcq/pages/licensee-directory.aspx
    ## 4  http://dhmh.maryland.gov/ohcq/pages/licensee-directory.aspx
    ## 5  http://dhmh.maryland.gov/ohcq/pages/licensee-directory.aspx
    ## 6  http://dhmh.maryland.gov/ohcq/pages/licensee-directory.aspx
    ## 7  http://dhmh.maryland.gov/ohcq/pages/licensee-directory.aspx
    ## 8  http://dhmh.maryland.gov/ohcq/pages/licensee-directory.aspx
    ## 9  http://dhmh.maryland.gov/ohcq/pages/licensee-directory.aspx
    ## 10 http://dhmh.maryland.gov/ohcq/pages/licensee-directory.aspx
    ##                  SOURCEDATE    VAL_METHOD                 VAL_DATE
    ## 1  2018-08-09T00:00:00.000Z       IMAGERY 2014-02-10T00:00:00.000Z
    ## 2  2018-08-09T00:00:00.000Z       IMAGERY 2014-02-10T00:00:00.000Z
    ## 3  2018-08-09T00:00:00.000Z       IMAGERY 2014-02-10T00:00:00.000Z
    ## 4  2018-08-09T00:00:00.000Z       IMAGERY 2014-02-10T00:00:00.000Z
    ## 5  2018-08-09T00:00:00.000Z       IMAGERY 2014-02-10T00:00:00.000Z
    ## 6  2018-08-09T00:00:00.000Z IMAGERY/OTHER 2014-02-10T00:00:00.000Z
    ## 7  2018-08-09T00:00:00.000Z       IMAGERY 2014-02-10T00:00:00.000Z
    ## 8  2018-08-09T00:00:00.000Z       IMAGERY 2014-02-10T00:00:00.000Z
    ## 9  2018-08-09T00:00:00.000Z       IMAGERY 2014-02-10T00:00:00.000Z
    ## 10 2018-08-09T00:00:00.000Z       IMAGERY 2014-02-10T00:00:00.000Z
    ##                                                                                        WEBSITE
    ## 1                                                               http://www.hopkinsmedicine.org
    ## 2                                                                http://www.kennedykrieger.org
    ## 3                                                                       http://www.mdmercy.com
    ## 4                                            http://www.lifebridgehealth.org/Sinai/Sinai1.aspx
    ## 5                                                       http://www.umms.org/hospitals/ummc.htm
    ## 6                                                                http://www.hopkinsbayview.org
    ## 7  http://www.meritushealth.com/For-Hospital-Patients-and-Visitors/Meritus-Medical-Center.aspx
    ## 8                                                               http://www.holycrosshealth.org
    ## 9                                                             http://www.fortwashingtonmc.org/
    ## 10                                                                         http://www.wmhs.com
    ##         STATE_ID      ALT_NAME ST_FIPS      OWNER TTL_STAFF BEDS
    ## 1  NOT AVAILABLE NOT AVAILABLE      24 NON-PROFIT      -999  951
    ## 2  NOT AVAILABLE NOT AVAILABLE      24 NON-PROFIT      -999   70
    ## 3  NOT AVAILABLE NOT AVAILABLE      24 NON-PROFIT      -999  281
    ## 4  NOT AVAILABLE NOT AVAILABLE      24 NON-PROFIT      -999  467
    ## 5  NOT AVAILABLE NOT AVAILABLE      24 NON-PROFIT      -999  800
    ## 6  NOT AVAILABLE NOT AVAILABLE      24 NON-PROFIT      -999  477
    ## 7  NOT AVAILABLE NOT AVAILABLE      24 NON-PROFIT      -999  247
    ## 8  NOT AVAILABLE NOT AVAILABLE      24 NON-PROFIT      -999  409
    ## 9  NOT AVAILABLE NOT AVAILABLE      24 NON-PROFIT      -999   37
    ## 10 NOT AVAILABLE NOT AVAILABLE      24 NON-PROFIT      -999  371
    ##                      TRAUMA HELIPAD                   geometry
    ## 1  LEVEL I, LEVEL PEDIATRIC       Y POINT (-76.59197 39.29611)
    ## 2             NOT AVAILABLE       Y POINT (-76.59282 39.29928)
    ## 3             NOT AVAILABLE       N POINT (-76.61288 39.29292)
    ## 4                  LEVEL II       Y  POINT (-76.66209 39.3523)
    ## 5                      PARC       Y POINT (-76.62493 39.28791)
    ## 6                  LEVEL II       Y POINT (-76.54678 39.29068)
    ## 7                 LEVEL III       Y POINT (-77.68256 39.62219)
    ## 8             NOT AVAILABLE       N POINT (-77.03574 39.01472)
    ## 9             NOT AVAILABLE       Y  POINT (-76.9927 38.72856)
    ## 10                LEVEL III       Y POINT (-78.73324 39.64783)

That gives us 50 hospitals in Maryland. Where are they?

We can simply plot them on a longitude-latitude grid using ggplot.

``` 
md_hospitals %>%
  ggplot() + 
  geom_sf() + 
  theme_minimal()
```


Each point is a hospital. Each hospital has been plotted according to its degrees of longitude and latitude.

If you know anything about the state of Maryland, you can kinda pick out the shape of the state there. The point in the top left is in Western Maryland. The point at the extreme bottom right is on the Eastern Shore. But this map is not exactly ideal. It would help to have a state and county map layered underneath of it, to help make sense of the spatial nature of this data.

This is where layering becomes more clear. First, we want to go out and get another shapefile, this one showing Maryland county outlines.

Instead of loading it from our local machine, like we did above, we're going to use a package to directly download it from the U.S. Census. The package is called `tigris` and it's developed by the same person who made `tidycensus`.

In the console, install tigris with the install packages function

Then load it:

``` 
library(tigris)
```

Now, let's use the counties() function from tigris to pull down a shapefile of all U.S. counties.

``` 
counties <- counties() 
```

    ## 
      |                                                                            
      |                                                                      |   0%
      |                                                                            
      |                                                                      |   1%
      |                                                                            
      |=                                                                     |   1%
      |                                                                            
      |=                                                                     |   2%
      |                                                                            
      |==                                                                    |   2%
      |                                                                            
      |==                                                                    |   3%
      |                                                                            
      |===                                                                   |   4%
      |                                                                            
      |===                                                                   |   5%
      |                                                                            
      |====                                                                  |   5%
      |                                                                            
      |====                                                                  |   6%
      |                                                                            
      |=====                                                                 |   6%
      |                                                                            
      |=====                                                                 |   7%
      |                                                                            
      |======                                                                |   8%
      |                                                                            
      |======                                                                |   9%
      |                                                                            
      |=======                                                               |  10%
      |                                                                            
      |=======                                                               |  11%
      |                                                                            
      |========                                                              |  11%
      |                                                                            
      |========                                                              |  12%
      |                                                                            
      |=========                                                             |  12%
      |                                                                            
      |=========                                                             |  13%
      |                                                                            
      |==========                                                            |  14%
      |                                                                            
      |===========                                                           |  15%
      |                                                                            
      |===========                                                           |  16%
      |                                                                            
      |============                                                          |  16%
      |                                                                            
      |============                                                          |  17%
      |                                                                            
      |============                                                          |  18%
      |                                                                            
      |=============                                                         |  18%
      |                                                                            
      |=============                                                         |  19%
      |                                                                            
      |==============                                                        |  19%
      |                                                                            
      |==============                                                        |  20%
      |                                                                            
      |===============                                                       |  21%
      |                                                                            
      |===============                                                       |  22%
      |                                                                            
      |================                                                      |  22%
      |                                                                            
      |================                                                      |  23%
      |                                                                            
      |=================                                                     |  24%
      |                                                                            
      |=================                                                     |  25%
      |                                                                            
      |==================                                                    |  25%
      |                                                                            
      |==================                                                    |  26%
      |                                                                            
      |===================                                                   |  26%
      |                                                                            
      |===================                                                   |  27%
      |                                                                            
      |===================                                                   |  28%
      |                                                                            
      |====================                                                  |  28%
      |                                                                            
      |====================                                                  |  29%
      |                                                                            
      |=====================                                                 |  29%
      |                                                                            
      |=====================                                                 |  30%
      |                                                                            
      |=====================                                                 |  31%
      |                                                                            
      |======================                                                |  31%
      |                                                                            
      |=======================                                               |  32%
      |                                                                            
      |=======================                                               |  33%
      |                                                                            
      |========================                                              |  34%
      |                                                                            
      |========================                                              |  35%
      |                                                                            
      |=========================                                             |  35%
      |                                                                            
      |=========================                                             |  36%
      |                                                                            
      |==========================                                            |  36%
      |                                                                            
      |==========================                                            |  37%
      |                                                                            
      |===========================                                           |  38%
      |                                                                            
      |===========================                                           |  39%
      |                                                                            
      |============================                                          |  40%
      |                                                                            
      |=============================                                         |  41%
      |                                                                            
      |=============================                                         |  42%
      |                                                                            
      |==============================                                        |  43%
      |                                                                            
      |==============================                                        |  44%
      |                                                                            
      |===============================                                       |  44%
      |                                                                            
      |===============================                                       |  45%
      |                                                                            
      |================================                                      |  46%
      |                                                                            
      |=================================                                     |  46%
      |                                                                            
      |=================================                                     |  48%
      |                                                                            
      |==================================                                    |  48%
      |                                                                            
      |==================================                                    |  49%
      |                                                                            
      |===================================                                   |  49%
      |                                                                            
      |===================================                                   |  50%
      |                                                                            
      |===================================                                   |  51%
      |                                                                            
      |====================================                                  |  51%
      |                                                                            
      |====================================                                  |  52%
      |                                                                            
      |=====================================                                 |  52%
      |                                                                            
      |=====================================                                 |  53%
      |                                                                            
      |=====================================                                 |  54%
      |                                                                            
      |======================================                                |  54%
      |                                                                            
      |======================================                                |  55%
      |                                                                            
      |=======================================                               |  55%
      |                                                                            
      |=======================================                               |  56%
      |                                                                            
      |========================================                              |  57%
      |                                                                            
      |========================================                              |  58%
      |                                                                            
      |=========================================                             |  59%
      |                                                                            
      |==========================================                            |  59%
      |                                                                            
      |==========================================                            |  60%
      |                                                                            
      |===========================================                           |  61%
      |                                                                            
      |===========================================                           |  62%
      |                                                                            
      |============================================                          |  62%
      |                                                                            
      |============================================                          |  63%
      |                                                                            
      |=============================================                         |  64%
      |                                                                            
      |=============================================                         |  65%
      |                                                                            
      |==============================================                        |  65%
      |                                                                            
      |==============================================                        |  66%
      |                                                                            
      |===============================================                       |  67%
      |                                                                            
      |================================================                      |  68%
      |                                                                            
      |================================================                      |  69%
      |                                                                            
      |=================================================                     |  70%
      |                                                                            
      |==================================================                    |  71%
      |                                                                            
      |==================================================                    |  72%
      |                                                                            
      |===================================================                   |  73%
      |                                                                            
      |====================================================                  |  74%
      |                                                                            
      |====================================================                  |  75%
      |                                                                            
      |=====================================================                 |  75%
      |                                                                            
      |=====================================================                 |  76%
      |                                                                            
      |======================================================                |  76%
      |                                                                            
      |======================================================                |  77%
      |                                                                            
      |======================================================                |  78%
      |                                                                            
      |=======================================================               |  78%
      |                                                                            
      |=======================================================               |  79%
      |                                                                            
      |========================================================              |  80%
      |                                                                            
      |=========================================================             |  81%
      |                                                                            
      |=========================================================             |  82%
      |                                                                            
      |==========================================================            |  83%
      |                                                                            
      |===========================================================           |  84%
      |                                                                            
      |===========================================================           |  85%
      |                                                                            
      |============================================================          |  86%
      |                                                                            
      |=============================================================         |  87%
      |                                                                            
      |==============================================================        |  88%
      |                                                                            
      |==============================================================        |  89%
      |                                                                            
      |===============================================================       |  90%
      |                                                                            
      |===============================================================       |  91%
      |                                                                            
      |================================================================      |  91%
      |                                                                            
      |================================================================      |  92%
      |                                                                            
      |=================================================================     |  92%
      |                                                                            
      |=================================================================     |  93%
      |                                                                            
      |==================================================================    |  94%
      |                                                                            
      |==================================================================    |  95%
      |                                                                            
      |===================================================================   |  95%
      |                                                                            
      |===================================================================   |  96%
      |                                                                            
      |====================================================================  |  96%
      |                                                                            
      |====================================================================  |  98%
      |                                                                            
      |===================================================================== |  98%
      |                                                                            
      |===================================================================== |  99%
      |                                                                            
      |======================================================================| 100%

``` 
glimpse(counties)
```

    ## Rows: 3,233
    ## Columns: 18
    ## $ STATEFP  <chr> "31", "53", "35", "31", "31", "72", "46", "48", "06", "21", "…
    ## $ COUNTYFP <chr> "039", "069", "011", "109", "129", "085", "099", "327", "091"…
    ## $ COUNTYNS <chr> "00835841", "01513275", "00933054", "00835876", "00835886", "…
    ## $ GEOID    <chr> "31039", "53069", "35011", "31109", "31129", "72085", "46099"…
    ## $ NAME     <chr> "Cuming", "Wahkiakum", "De Baca", "Lancaster", "Nuckolls", "L…
    ## $ NAMELSAD <chr> "Cuming County", "Wahkiakum County", "De Baca County", "Lanca…
    ## $ LSAD     <chr> "06", "06", "06", "06", "06", "13", "06", "06", "06", "06", "…
    ## $ CLASSFP  <chr> "H1", "H1", "H1", "H1", "H1", "H1", "H1", "H1", "H1", "H1", "…
    ## $ MTFCC    <chr> "G4020", "G4020", "G4020", "G4020", "G4020", "G4020", "G4020"…
    ## $ CSAFP    <chr> NA, NA, NA, "339", NA, "490", NA, NA, NA, NA, "534", "352", N…
    ## $ CBSAFP   <chr> NA, NA, NA, "30700", NA, "41980", "43620", NA, NA, NA, "22300…
    ## $ METDIVFP <chr> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, N…
    ## $ FUNCSTAT <chr> "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "…
    ## $ ALAND    <dbl> 1477652222, 680962890, 6016819475, 2169270569, 1489645188, 87…
    ## $ AWATER   <dbl> 10690952, 61582307, 29089486, 22849484, 1718484, 32509, 18198…
    ## $ INTPTLAT <chr> "+41.9158651", "+46.2946377", "+34.3592729", "+40.7835474", "…
    ## $ INTPTLON <chr> "-096.7885168", "-123.4244583", "-104.3686961", "-096.6886584…
    ## $ geometry <MULTIPOLYGON [°]> MULTIPOLYGON (((-97.01952 4..., MULTIPOLYGON (((…

This looks pretty similar to our hospital shapefile, in that it looked mostly like a normal dataframe with the exception of the new geometry column.

But instead of POINT, this geometry is of the datatype "MULTIPOLYGON." Points are shape data represented by one pair of longitude or latitude coordinates. Polygons are made up of LOTS of pairs of longitude and latitude coordinates, connected by a boundary line into a complex shape.

If you've ever filled in a "connect the dots" picture by drawing lines between points, in order to reveal a hidden shape, then you're familiar with the concept.

This county shapefile has all 3233 U.S. counties. We only want the Maryland counties, so we're going to filter the data to only keep Maryland counties. There is no STATE column, but there is a STATEFP column, with each number representing a state. Maryland's FP number is 24.

``` 
md_counties <- counties %>%
  filter(STATEFP == "24")
```

To see what this looks like, let's plot it out with ggplot. We can pretty clearly see the shapes of Maryland counties.

``` 
md_counties %>%
  ggplot() + 
  geom_sf() + 
  theme_minimal()
```


With this county map, we can layer our hospital data.

Something to note: The layers are rendered in the order they appear. So the first geom_sf is rendered first. The second geom_sf is rendered ON TOP OF the first one.

We're also going to change things up a bit to put the datasets we want to display INSIDE of the geom_sf() function, instead of starting with a dataframe. We have two to plot now, so it's easier this way.

``` 
ggplot() + 
  geom_sf(data=md_counties) + 
  geom_sf(data=md_hospitals) +
  theme_minimal()
```


Well, hospitals are clustered around the state's most populous areas, the Baltimore to Washington corridor. There are fewer hospitals in rural Eastern and Western counties. And two counties have no hospital at all.

This is a pretty blunt visualization. Not all hospitals are equal. Some have more beds than the others, and bed space is a critical factor in how full hospitals get during COVID-19 surges.

We can get a sense of where the largest hospitals are, by changing the color of the points according to the number of beds. We do this by setting the aesthetic -- or aes -- to use the BEDS column inside of the geom_sf function. To make the differences easier to see, we're going to change the fill of the counties white, too, and use a special color palette, viridis magma. We're also going to make the points slightly bigger.

``` 
ggplot() + 
  geom_sf(data=md_counties, fill="white") + 
  geom_sf(data=md_hospitals, aes(color=BEDS), size=2) +
  scale_colour_viridis_b(option="magma") + 
  theme_minimal() 
```


With these changes, what else can we make out here? Well, not only are most hospitals clustered in the center of Maryland, the largest ones are too. Rural areas have fewer and typically smaller hospitals.

`<!--chapter:end:19-geographicbasics.Rmd-->`{=html}


