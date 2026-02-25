<!-- chunk: 4/4 | source: 33-data-journalism-wells.md | words: 13941 -->
<!-- headings: Geographic analysis {number="21"}; Automating analysis {number="22"}; 22.1 Automating downloads and imports {number="22.1"}; 22.2 Exploring the data {number="22.2"}; 22.3 Analysis {number="22.3"}; 22.4 Making updating graphics {number="22.4"}; Automating geographic analysis {number="23"}; 23.1 Mapping continuously {number="23.1"}; Basic Stats: Linear Regression and The T-Test {number="24"}; Linear Regression {number="25"}; T-tests {number="26"}; An intro to text analysis {number="27"}; 27.1 Going beyond a single word {number="27.1"}; 27.2 Sentiment Analysis {number="27.2"}; Writing with numbers {number="28"}; 28.1 How to write about numbers without overwhelming with numbers. {number="28.1"}; 28.2 When exact numbers matter {number="28.2"}; 28.3 An example {number="28.3"}; Ethics in data journalism {number="29"}; 29.1 Problems {number="29.1"} -->

#  Geographic analysis {number="21"}

In the previous chapter, we looked at Maryland's hospitals and used layers to show where hospitals sit on a map of Maryland's counties, and to show a bit of a pattern regarding concentration of the largest hospitals. Let's go little further.

First, let's load the libraries we'll need. We're also going to load tidycensus and set an API key for tidycensus.

``` 
library(tidyverse)
library(sf)
library(janitor)
library(tidycensus)
census_api_key("549950d36c22ff16455fe196bbbd01d63cfbe6cf")
```

    ## To install your API key for use in future sessions, run this function with `install = TRUE`.

And now let's load the dataframe of hospital information from the previous chapter, and filter for the 50 General Acute Care hospitals in Maryland.

``` 
md_hospitals <- st_read("data/Hospitals/Hospitals.shp") %>%
  filter(STATE == "MD") %>%
  filter(TYPE == "GENERAL ACUTE CARE")
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

For the rest of this chapter, we're going to work on building a map that will help us gain insight into geographic patterns in hospital bed availability by county in Maryland. Our question: by examining the number of hospital beds per 100,000 people in each county, what regional geographic patterns can we identify?

Each hospital exists inside of a county, so we're going to first calculate the total number of beds in each county. We do this by first converting the md_hospitals data to a standard dataframe (instead of a spatial dataframe) using as_tibble(), then grouping by county and totaling the number of beds. Finally, let's sort by total_beds to see which county has the most.

``` 
md_beds_by_county <- md_hospitals %>%
  as_tibble() %>%
  group_by(COUNTY) %>%
  summarise(
    total_beds = sum(BEDS)
  ) %>%
  arrange(desc(total_beds))

md_beds_by_county
```

    ## # A tibble: 22 x 2
    ##    COUNTY          total_beds
    ##    <chr>                <dbl>
    ##  1 BALTIMORE CITY        4505
    ##  2 MONTGOMERY            1298
    ##  3 BALTIMORE             1152
    ##  4 PRINCE GEORGE'S        789
    ##  5 ANNE ARUNDEL           673
    ##  6 ALLEGANY               371
    ##  7 HOWARD                 331
    ##  8 FREDERICK              308
    ##  9 WICOMICO               281
    ## 10 HARFORD                255
    ## # … with 12 more rows

So, what do we see here? Baltimore City has the most, followed by Montgomery, Baltimore County and Prince George's. All big counties.

Next, we'll go out and get population data for each county from tidycensus. The variable for total population is B01001_001.

``` 
md_county_population <- get_acs(geography = "county",
              variables = c(population = "B01001_001"),
              state = "MD")
```

    ## Getting data from the 2015-2019 5-year ACS

``` 
md_county_population
```

    ## # A tibble: 24 x 5
    ##    GEOID NAME                          variable   estimate   moe
    ##    <chr> <chr>                         <chr>         <dbl> <dbl>
    ##  1 24001 Allegany County, Maryland     population    71445    NA
    ##  2 24003 Anne Arundel County, Maryland population   571275    NA
    ##  3 24005 Baltimore County, Maryland    population   828018    NA
    ##  4 24009 Calvert County, Maryland      population    91511    NA
    ##  5 24011 Caroline County, Maryland     population    33049    NA
    ##  6 24013 Carroll County, Maryland      population   167699    NA
    ##  7 24015 Cecil County, Maryland        population   102552    NA
    ##  8 24017 Charles County, Maryland      population   159428    NA
    ##  9 24019 Dorchester County, Maryland   population    32138    NA
    ## 10 24021 Frederick County, Maryland    population   251422    NA
    ## # … with 14 more rows

Ultimately, we're going to join this county population table with our beds by county table, and then calculate a beds per 100,000 people statistic. But remember, we then want to visualize this data by drawing a county map that helps us pick out trends. Thinking ahead, we know we'll need a county map shapefile. Fortunately, we can pull this geometry information right from tidycensus at the same time that we pull in the population data by adding "geometry = TRUE" to our get_acs function.

``` 
md_county_population <- get_acs(geography = "county",
              variables = c(population = "B01001_001"),
              state = "MD",
              geometry = TRUE)
```

    ## Getting data from the 2015-2019 5-year ACS

    ## Downloading feature geometry from the Census website.  To cache shapefiles for use in future sessions, set `options(tigris_use_cache = TRUE)`.

    ## 
      |                                                                            
      |                                                                      |   0%
      |                                                                            
      |==                                                                    |   2%
      |                                                                            
      |==                                                                    |   3%
      |                                                                            
      |==                                                                    |   4%
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
      |=====                                                                 |   8%
      |                                                                            
      |======                                                                |   8%
      |                                                                            
      |=======                                                               |  10%
      |                                                                            
      |=======                                                               |  11%
      |                                                                            
      |========                                                              |  11%
      |                                                                            
      |=============                                                         |  19%
      |                                                                            
      |==============                                                        |  20%
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
      |======================                                                |  32%
      |                                                                            
      |=======================                                               |  33%
      |                                                                            
      |========================                                              |  34%
      |                                                                            
      |==========================                                            |  37%
      |                                                                            
      |==========================                                            |  38%
      |                                                                            
      |===========================                                           |  38%
      |                                                                            
      |===============================                                       |  44%
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
      |=====================================                                 |  52%
      |                                                                            
      |=====================================                                 |  53%
      |                                                                            
      |======================================                                |  55%
      |                                                                            
      |=======================================                               |  55%
      |                                                                            
      |========================================                              |  56%
      |                                                                            
      |=========================================                             |  58%
      |                                                                            
      |=============================================                         |  64%
      |                                                                            
      |==============================================                        |  66%
      |                                                                            
      |===============================================                       |  67%
      |                                                                            
      |===============================================                       |  68%
      |                                                                            
      |================================================                      |  68%
      |                                                                            
      |================================================                      |  69%
      |                                                                            
      |=================================================                     |  70%
      |                                                                            
      |========================================================              |  79%
      |                                                                            
      |=========================================================             |  82%
      |                                                                            
      |===========================================================           |  85%
      |                                                                            
      |==============================================================        |  88%
      |                                                                            
      |==============================================================        |  89%
      |                                                                            
      |================================================================      |  91%
      |                                                                            
      |================================================================      |  92%
      |                                                                            
      |=================================================================     |  92%
      |                                                                            
      |=================================================================     |  93%
      |                                                                            
      |====================================================================  |  97%
      |                                                                            
      |======================================================================| 100%

``` 
md_county_population
```

    ## Simple feature collection with 24 features and 5 fields
    ## Geometry type: MULTIPOLYGON
    ## Dimension:     XY
    ## Bounding box:  xmin: -79.48765 ymin: 37.91172 xmax: -75.04894 ymax: 39.72304
    ## Geodetic CRS:  NAD83
    ## First 10 features:
    ##    GEOID                             NAME   variable estimate moe
    ## 1  24035    Queen Anne's County, Maryland population    49632  NA
    ## 2  24005       Baltimore County, Maryland population   828018  NA
    ## 3  24003    Anne Arundel County, Maryland population   571275  NA
    ## 4  24013         Carroll County, Maryland population   167699  NA
    ## 5  24021       Frederick County, Maryland population   251422  NA
    ## 6  24039        Somerset County, Maryland population    25729  NA
    ## 7  24029            Kent County, Maryland population    19536  NA
    ## 8  24047       Worcester County, Maryland population    51765  NA
    ## 9  24027          Howard County, Maryland population   318855  NA
    ## 10 24033 Prince George's County, Maryland population   908670  NA
    ##                          geometry
    ## 1  MULTIPOLYGON (((-76.24918 3...
    ## 2  MULTIPOLYGON (((-76.3257 39...
    ## 3  MULTIPOLYGON (((-76.84036 3...
    ## 4  MULTIPOLYGON (((-77.31151 3...
    ## 5  MULTIPOLYGON (((-77.67716 3...
    ## 6  MULTIPOLYGON (((-75.95962 3...
    ## 7  MULTIPOLYGON (((-76.27737 3...
    ## 8  MULTIPOLYGON (((-75.66061 3...
    ## 9  MULTIPOLYGON (((-77.18711 3...
    ## 10 MULTIPOLYGON (((-77.07995 3...

We now have a new column, geometry, that contains the "MULTIPOLYGON" data that will draw an outline of each county when we go to draw a map.

The next step will be to join our population data to our hospital bed data on the county column.

But there's a problem. The column in our population data that has county names is called "NAME," and it has the full name of the county spelled out in title case -- first word capitalized and has "County" and "Maryland" in it. The beds data just has the uppercase name of the county. For example, the population data has "Anne Arundel County, Maryland" and the beds data has "ANNE ARUNDEL"

``` 
md_county_population
```

    ## Simple feature collection with 24 features and 5 fields
    ## Geometry type: MULTIPOLYGON
    ## Dimension:     XY
    ## Bounding box:  xmin: -79.48765 ymin: 37.91172 xmax: -75.04894 ymax: 39.72304
    ## Geodetic CRS:  NAD83
    ## First 10 features:
    ##    GEOID                             NAME   variable estimate moe
    ## 1  24035    Queen Anne's County, Maryland population    49632  NA
    ## 2  24005       Baltimore County, Maryland population   828018  NA
    ## 3  24003    Anne Arundel County, Maryland population   571275  NA
    ## 4  24013         Carroll County, Maryland population   167699  NA
    ## 5  24021       Frederick County, Maryland population   251422  NA
    ## 6  24039        Somerset County, Maryland population    25729  NA
    ## 7  24029            Kent County, Maryland population    19536  NA
    ## 8  24047       Worcester County, Maryland population    51765  NA
    ## 9  24027          Howard County, Maryland population   318855  NA
    ## 10 24033 Prince George's County, Maryland population   908670  NA
    ##                          geometry
    ## 1  MULTIPOLYGON (((-76.24918 3...
    ## 2  MULTIPOLYGON (((-76.3257 39...
    ## 3  MULTIPOLYGON (((-76.84036 3...
    ## 4  MULTIPOLYGON (((-77.31151 3...
    ## 5  MULTIPOLYGON (((-77.67716 3...
    ## 6  MULTIPOLYGON (((-75.95962 3...
    ## 7  MULTIPOLYGON (((-76.27737 3...
    ## 8  MULTIPOLYGON (((-75.66061 3...
    ## 9  MULTIPOLYGON (((-77.18711 3...
    ## 10 MULTIPOLYGON (((-77.07995 3...

``` 
md_beds_by_county
```

    ## # A tibble: 22 x 2
    ##    COUNTY          total_beds
    ##    <chr>                <dbl>
    ##  1 BALTIMORE CITY        4505
    ##  2 MONTGOMERY            1298
    ##  3 BALTIMORE             1152
    ##  4 PRINCE GEORGE'S        789
    ##  5 ANNE ARUNDEL           673
    ##  6 ALLEGANY               371
    ##  7 HOWARD                 331
    ##  8 FREDERICK              308
    ##  9 WICOMICO               281
    ## 10 HARFORD                255
    ## # … with 12 more rows

If they're going to join properly, we need to clean one of them up to make it match the other.

Let's clean the population table. We're going to rename the "NAME" column to "COUNTY," then convert it to uppercase while also removing ", Maryland" and "County." Next we'll remove any white spaces after that first cleaning step that, if left in, would prevent a proper join. We're also going to rename the column that contains the population information from "estimate" to "population" and select only the county name and the population columns, along with the geometry. That leaves us with this tidy table.

``` 
md_county_population <- md_county_population %>%
  rename(COUNTY = NAME) %>%
  mutate(COUNTY = toupper(str_remove_all(COUNTY,", Maryland|County"))) %>%
  mutate(COUNTY = str_trim(COUNTY,side="both")) %>%
  rename(population = estimate) %>%
  select(COUNTY, population, geometry)

md_county_population
```

    ## Simple feature collection with 24 features and 2 fields
    ## Geometry type: MULTIPOLYGON
    ## Dimension:     XY
    ## Bounding box:  xmin: -79.48765 ymin: 37.91172 xmax: -75.04894 ymax: 39.72304
    ## Geodetic CRS:  NAD83
    ## First 10 features:
    ##             COUNTY population                       geometry
    ## 1     QUEEN ANNE'S      49632 MULTIPOLYGON (((-76.24918 3...
    ## 2        BALTIMORE     828018 MULTIPOLYGON (((-76.3257 39...
    ## 3     ANNE ARUNDEL     571275 MULTIPOLYGON (((-76.84036 3...
    ## 4          CARROLL     167699 MULTIPOLYGON (((-77.31151 3...
    ## 5        FREDERICK     251422 MULTIPOLYGON (((-77.67716 3...
    ## 6         SOMERSET      25729 MULTIPOLYGON (((-75.95962 3...
    ## 7             KENT      19536 MULTIPOLYGON (((-76.27737 3...
    ## 8        WORCESTER      51765 MULTIPOLYGON (((-75.66061 3...
    ## 9           HOWARD     318855 MULTIPOLYGON (((-77.18711 3...
    ## 10 PRINCE GEORGE'S     908670 MULTIPOLYGON (((-77.07995 3...

Now we can join them.

``` 
md_beds_per_100k <- md_county_population %>%
  left_join(md_beds_by_county)
```

    ## Joining, by = "COUNTY"

``` 
md_beds_per_100k
```

    ## Simple feature collection with 24 features and 3 fields
    ## Geometry type: MULTIPOLYGON
    ## Dimension:     XY
    ## Bounding box:  xmin: -79.48765 ymin: 37.91172 xmax: -75.04894 ymax: 39.72304
    ## Geodetic CRS:  NAD83
    ## First 10 features:
    ##             COUNTY population total_beds                       geometry
    ## 1     QUEEN ANNE'S      49632         NA MULTIPOLYGON (((-76.24918 3...
    ## 2        BALTIMORE     828018       1152 MULTIPOLYGON (((-76.3257 39...
    ## 3     ANNE ARUNDEL     571275        673 MULTIPOLYGON (((-76.84036 3...
    ## 4          CARROLL     167699        189 MULTIPOLYGON (((-77.31151 3...
    ## 5        FREDERICK     251422        308 MULTIPOLYGON (((-77.67716 3...
    ## 6         SOMERSET      25729         89 MULTIPOLYGON (((-75.95962 3...
    ## 7             KENT      19536         26 MULTIPOLYGON (((-76.27737 3...
    ## 8        WORCESTER      51765         45 MULTIPOLYGON (((-75.66061 3...
    ## 9           HOWARD     318855        331 MULTIPOLYGON (((-77.18711 3...
    ## 10 PRINCE GEORGE'S     908670        789 MULTIPOLYGON (((-77.07995 3...

We have two NAs after we join, for Queen Anne's County and Caroline County. That's not an error. There are no General Acute Care hospitals in those counties, according to our data (it's why our beds table has 22 rows, not 24). So let's convert those values to 0 using replace_na().

``` 
md_beds_per_100k <- md_county_population %>%
  left_join(md_beds_by_county) %>%
  mutate(total_beds = replace_na(total_beds,0))
```

    ## Joining, by = "COUNTY"

``` 
md_beds_per_100k
```

    ## Simple feature collection with 24 features and 3 fields
    ## Geometry type: MULTIPOLYGON
    ## Dimension:     XY
    ## Bounding box:  xmin: -79.48765 ymin: 37.91172 xmax: -75.04894 ymax: 39.72304
    ## Geodetic CRS:  NAD83
    ## First 10 features:
    ##             COUNTY population total_beds                       geometry
    ## 1     QUEEN ANNE'S      49632          0 MULTIPOLYGON (((-76.24918 3...
    ## 2        BALTIMORE     828018       1152 MULTIPOLYGON (((-76.3257 39...
    ## 3     ANNE ARUNDEL     571275        673 MULTIPOLYGON (((-76.84036 3...
    ## 4          CARROLL     167699        189 MULTIPOLYGON (((-77.31151 3...
    ## 5        FREDERICK     251422        308 MULTIPOLYGON (((-77.67716 3...
    ## 6         SOMERSET      25729         89 MULTIPOLYGON (((-75.95962 3...
    ## 7             KENT      19536         26 MULTIPOLYGON (((-76.27737 3...
    ## 8        WORCESTER      51765         45 MULTIPOLYGON (((-75.66061 3...
    ## 9           HOWARD     318855        331 MULTIPOLYGON (((-77.18711 3...
    ## 10 PRINCE GEORGE'S     908670        789 MULTIPOLYGON (((-77.07995 3...

Our final step before visualization, let's calculate the number of beds per 100,000 for each county and sort from highest to lowest to see waht trends we can identify just from the table.

``` 
md_beds_per_100k <- md_county_population %>%
  left_join(md_beds_by_county) %>%
  mutate(total_beds = replace_na(total_beds,0)) %>%
  mutate(beds_per_100k = total_beds/population*100000) %>%
  arrange(desc(beds_per_100k))
```

    ## Joining, by = "COUNTY"

``` 
md_beds_per_100k
```

    ## Simple feature collection with 24 features and 4 fields
    ## Geometry type: MULTIPOLYGON
    ## Dimension:     XY
    ## Bounding box:  xmin: -79.48765 ymin: 37.91172 xmax: -75.04894 ymax: 39.72304
    ## Geodetic CRS:  NAD83
    ## First 10 features:
    ##            COUNTY population total_beds beds_per_100k
    ## 1  BALTIMORE CITY     609032       4505      739.6984
    ## 2        ALLEGANY      71445        371      519.2806
    ## 3          TALBOT      37167        132      355.1538
    ## 4        SOMERSET      25729         89      345.9132
    ## 5        WICOMICO     102539        281      274.0421
    ## 6         GARRETT      29235         55      188.1307
    ## 7      WASHINGTON     150109        247      164.5471
    ## 8      DORCHESTER      32138         46      143.1327
    ## 9       BALTIMORE     828018       1152      139.1274
    ## 10           KENT      19536         26      133.0876
    ##                          geometry
    ## 1  MULTIPOLYGON (((-76.71152 3...
    ## 2  MULTIPOLYGON (((-79.06756 3...
    ## 3  MULTIPOLYGON (((-76.34647 3...
    ## 4  MULTIPOLYGON (((-75.95962 3...
    ## 5  MULTIPOLYGON (((-75.92033 3...
    ## 6  MULTIPOLYGON (((-79.48765 3...
    ## 7  MULTIPOLYGON (((-78.36346 3...
    ## 8  MULTIPOLYGON (((-76.06544 3...
    ## 9  MULTIPOLYGON (((-76.3257 39...
    ## 10 MULTIPOLYGON (((-76.27737 3...

Let's take a look at the result of this table. Baltimore City is still up there at the top, even when measuring by beds per 100k. But there are some surpising ones at the top, some of Maryland's smallest counties! Allegany, Talbot, Somerset may not have that many beds, but they also don't have a lot of people.

Okay, now let's visualize. We're going to build a choropleth map, with the color of each county -- the fill -- set according to the number of beds per 100K on a color gradient.

``` 
ggplot() +
  geom_sf(data=md_beds_per_100k, aes(fill=beds_per_100k)) +
  theme_minimal()
```


``` 
ggplot() +
  geom_sf(data=md_beds_per_100k, aes(fill=beds_per_100k)) +
  theme_minimal() +
  scale_fill_viridis_b(option="magma")
```


So let's change the color scale to a "log" scale, which will help us see those differences a bit more clearly.

``` 
ggplot() +
  geom_sf(data=md_beds_per_100k, aes(fill=beds_per_100k)) +
  theme_minimal() +
  scale_fill_viridis_b(option="magma",trans = "log")
```

    ## Warning: Transformation introduced infinite values in discrete y-axis


The Eastern Shore and Western Maryland have more beds per capita than Central Maryland (with the exception of Baltimore City). And Southern Maryland -- PG, Charles, Calvert and St. Mary's -- has by far the fewest beds per capita of any other region.

`<!--chapter:end:20-geographicanalysis.Rmd-->`{=html}


#  Automating analysis {number="22"}

Many of the data analyses that you do will be largely one-off efforts -- you're going to do the analysis and write the story and be done. Maybe you'll come back to it in a couple of months or years, but really you're just doing it once.

But what happens when you have a long-running story, where you're going to update it every day, or every week? What changes when you're writing that code?

1.  How will this run again without changing anything?
2.  What questions do you have that have to be answered each time?
3.  What changes when you have to repeat questions to changing data?

The global COVID-19 pandemic is something we're going to be writing about and covering for some time. One element of it is data on vaccinations. That's reported frequently (mostly daily), and we'll be talking about it for some time. So it is an ideal candidate for repeating analysis -- scripting the questions we want to answer every week and doing so in a way that we can just load it without having to change anything.

Here's a real-world example: you are covering public health in Maryland, focusing on Prince George's County, and you want to see how many people are getting fully vaccinated over time. You could look at a county or state website, copy and paste some information into a file and then do some calculations, but there's a better way. Instead, let's build a system that goes out each day to retrieve the data, makes it easier to analyze and then calculates the percentage change in the number of people getting fully vaccinated between the latest date and a week earlier. And makes us a chart showing that.

Let's get some other libraries to our typical tidyverse import. We'll start with lubridate and janitor to help wrangle the data, and we're also going to add a library called `ggrepel`, which assists in putting tables on dots in charts.

You install it the same way you do anything else -- `install.packages("ggrepel")`.

``` 
library(tidyverse)
library(janitor)
library(lubridate)
library(ggrepel)
```

## 22.1 Automating downloads and imports {number="22.1"}

Now, where to find the data?

Maryland [publishes data daily on vaccinations on the state Department of Heath website](https://coronavirus.maryland.gov/#Vaccine).

The dashboard is a series of HTML pages placed on the main page via iframe. Like this one: <https://state-of-maryland.github.io/VaccineDashboardGraphs/VaccinationDosesDaily.html>. But if you view the source on that URL, there's ... no data. It's being pulled in from another URL. If we want to automate getting this data, we'll need to find out where it lives. One big clue is in the composition of that URL: "github.io." Are these files (and maybe the data) already on GitHub? Let's find out. The easiest thing to do is to go to the GitHub user: <https://github.com/state-of-maryland>. There's a repository there called `VaccineCSVs` that sounds pretty good. Let's check it out.

There are a lot of files here: <https://github.com/state-of-maryland/VaccineCSVs>, and we want to focus our attention on the ones that are frequently updated. There are a bunch of those, some of which end in .json and .csv.xml, but we want to focus on the ones that end in .csv. Let's use this one: <https://raw.githubusercontent.com/state-of-maryland/VaccineCSVs/master/MD_COVID19_TotalVaccinationsCountyFirstandSecondSingleDose.csv>

We'll read it into a dataframe like usual and clean up the column names:

``` 
county_vaccinations_by_date <- read_csv("https://raw.githubusercontent.com/state-of-maryland/VaccineCSVs/master/MD_COVID19_TotalVaccinationsCountyFirstandSecondSingleDose.csv") %>%
  clean_names()
```

    ## 
    ## ── Column specification ────────────────────────────────────────────────────────
    ## cols(
    ##   OBJECTID = col_double(),
    ##   VACCINATION_DATE = col_character(),
    ##   County = col_character(),
    ##   FirstDoseDaily = col_double(),
    ##   FirstDoseCumulative = col_double(),
    ##   SecondDoseDaily = col_double(),
    ##   SecondDoseCumulative = col_double(),
    ##   SingleDoseDaily = col_double(),
    ##   SingleDoseCumulative = col_double(),
    ##   AtLeastOneDose = col_double(),
    ##   FullyVaccinated = col_double(),
    ##   FullVaccinatedCumulative = col_double(),
    ##   AtLeastOneDoseCumulative = col_double()
    ## )

``` 
View(county_vaccinations_by_date)
```

## 22.2 Exploring the data {number="22.2"}

Each row represents vaccination stats for a single county on a single day, including cumulative figures. But when we read in that data, the `vaccination_date` column is formatted as a `<chr>`{=html} column, not as a date. Let's fix that using lubridate's handy `mdy_hms` function, which matches the format in the dataframe. Then we'll save `vaccination_date` as a date without the time:

``` 
county_vaccinations_by_date <- county_vaccinations_by_date %>%
  mutate(vaccination_date = date(mdy_hms(vaccination_date)))
```

Let's see if there's anything unusual in the data by counting the number of rows for each county:

``` 
county_totals <- county_vaccinations_by_date %>%
  group_by(county) %>%
  summarize(total = n())

View(county_totals)
```

There are totals for all of Maryland's jurisdictions, plus one for "Unknown" and one that's NA. All but the last one have roughly the same number of records. What's going on with the NA records?

``` 
county_vaccinations_by_date %>%
  filter(is.na(county))
```

    ## # A tibble: 208 x 13
    ##    objectid vaccination_date county first_dose_daily first_dose_cumulative
    ##       <dbl> <date>           <chr>             <dbl>                 <dbl>
    ##  1        1 2021-01-08       <NA>               8000                  8000
    ##  2        2 2021-01-13       <NA>                  1                  8001
    ##  3        3 2021-01-26       <NA>                  1                  8002
    ##  4        4 2021-02-06       <NA>                  1                  8003
    ##  5        5 2021-02-10       <NA>                 NA                  8003
    ##  6        6 2021-02-11       <NA>                  1                  8004
    ##  7        7 2021-02-13       <NA>                  1                  8005
    ##  8        8 2021-02-23       <NA>                  1                  8006
    ##  9        9 2021-03-06       <NA>                 NA                  8006
    ## 10       10 2021-03-08       <NA>                  1                  8007
    ## # … with 198 more rows, and 8 more variables: second_dose_daily <dbl>,
    ## #   second_dose_cumulative <dbl>, single_dose_daily <dbl>,
    ## #   single_dose_cumulative <dbl>, at_least_one_dose <dbl>,
    ## #   fully_vaccinated <dbl>, full_vaccinated_cumulative <dbl>,
    ## #   at_least_one_dose_cumulative <dbl>

They don't seem to pertain to any county (or no county), and it's not clear what these records represent. Let's remove them from our dataset:

``` 
county_vaccinations_by_date <- county_vaccinations_by_date %>%
  filter(!is.na(county))
```

Now we can start to interview this data.

Let's look at the most recent date, and that's something that takes on different meaning when we're talking about updating data. We need to make this generic so that every time we pull this up and run it, it's the most recent date at the top. This time, it's very simple:

``` 
county_vaccinations_by_date %>% arrange(desc(vaccination_date))
```

    ## # A tibble: 8,555 x 13
    ##    objectid vaccination_date county        first_dose_daily first_dose_cumulati…
    ##       <dbl> <date>           <chr>                    <dbl>                <dbl>
    ##  1      892 2021-11-23       Baltimore                  471               523442
    ##  2     1256 2021-11-23       Anne Arundel               235               377615
    ##  3     1544 2021-11-23       Baltimore Ci…              232               353969
    ##  4     1833 2021-11-23       Allegany                    13                32895
    ##  5     2459 2021-11-23       Cecil                       31                49289
    ##  6     2737 2021-11-23       Carroll                     85               108660
    ##  7     3028 2021-11-23       Calvert                     32                58787
    ##  8     3221 2021-11-23       Charles                     47                96284
    ##  9     3704 2021-11-23       Harford                     98               152295
    ## 10     4069 2021-11-23       Caroline                     4                15100
    ## # … with 8,545 more rows, and 8 more variables: second_dose_daily <dbl>,
    ## #   second_dose_cumulative <dbl>, single_dose_daily <dbl>,
    ## #   single_dose_cumulative <dbl>, at_least_one_dose <dbl>,
    ## #   fully_vaccinated <dbl>, full_vaccinated_cumulative <dbl>,
    ## #   at_least_one_dose_cumulative <dbl>

## 22.3 Analysis {number="22.3"}

Now is when we need to start asking ourselves -- what are the questions that are going to come up day after day? What about how this most current date compares to the previous day, or the previous week or month?

What if we just ranked them? Where does this date rank? For that, we'll create a new column called Rank using mutate and we'll use a function called `min_rank` to rank them. Let's start by looking at daily `fully_vaccinated` figures in Prince George's County. I'm going to save them to a dataframe called `ranked`:

``` 
ranked <- county_vaccinations_by_date %>%
  filter(county == "Prince George's") %>%
  mutate(rank = min_rank(desc(fully_vaccinated))) %>%
  arrange(desc(vaccination_date)) %>%
  select(county, vaccination_date, fully_vaccinated, rank)

View(ranked)
```

The most recent dates aren't among the highest-ranked, meaning that fewer people are getting fully vaccinated on a given day compared to previous dates.

Let's think about this a little more. What else could we do with this? What are the recurring questions? How about the percent change between the latest date and one week ago? To do that, we need to find the latest date, which we've arranged to be the first one in our `ranked` dataframe. But what about a week ago? Luckily, if we have one date we can calculate another one by adding or subtracting days:

``` 
latest_date <- ranked %>% slice(1)
one_week_ago <- ranked %>% filter(vaccination_date == latest_date$vaccination_date - 7)
latest_date <- latest_date %>%
  mutate(pct_change_week = (fully_vaccinated - one_week_ago$fully_vaccinated)/one_week_ago$fully_vaccinated *100)
```

The `one_week_ago$fully_vaccinated` syntax is a way to reference a specific column in a specific dataframe. In this case, it's a dataframe with exactly one row.

## 22.4 Making updating graphics {number="22.4"}

More than numbers, we are going to want to see this data so we can spot potential stories. We can build this in steps. First, let's just make a big bar chart.

``` 
ggplot() +
  geom_bar(data=ranked, aes(x=vaccination_date, weight=fully_vaccinated))
```


So that shows us that the trend is going down over time, which makes sense as fewer people in the county are unvaccinated. It also shows that just after vaccinations began there was an initial dip - supply problems? - before the figure leapt up in April and May.

Let's build up some more layers to highlight trends and the most recent spot.

Now, in ggplot, we can add multiple layers.

The first layer will be all the bars.

The second layer will just be the latest, and we'll make that bar red.

Then we'll add a point to the top of that line to really draw attention to it.

Then we'll use ggprepel to label it.

Then I'm going to add a smoothing line. That'll illustrate the trend clearly.

The rest is labeling and adjusting the text to make it look more like a news graphic.

``` 
ggplot() +
  geom_bar(data=ranked, aes(x=vaccination_date, weight=fully_vaccinated)) +
  geom_bar(data=latest_date, aes(x=vaccination_date, weight=fully_vaccinated), fill="red") +
  geom_point(data=latest_date, aes(x=vaccination_date, y=fully_vaccinated)) +
  geom_text_repel(data=latest_date, aes(x=vaccination_date, y=fully_vaccinated + 150, label="Latest date")) +
  geom_smooth(data=ranked, aes(x=vaccination_date, y=fully_vaccinated), method=loess, se=FALSE) +
  labs(title="Prince George's County Fully Vaccinated Tailing Off", x="Date", y="Fully Vaccinated") +
  theme_minimal() +
  theme(
    plot.title = element_text(size = 16, face = "bold"),
    axis.title = element_text(size = 8),
    plot.subtitle = element_text(size=10),
    panel.grid.minor = element_blank()
    )
```

    ## `geom_smooth()` using formula 'y ~ x'

    ## Warning: Removed 82 rows containing non-finite values (stat_smooth).


One thing we are missing? An automated summary. What if we programmatically wrote the description for this chart using the percent change calculation we did before?

First, we format the percent change to look more news graphic like and not with 7 significant digits.

``` 
changetext <- round(latest_date$pct_change_week[[1]], digits=2)
direction <- if_else(changetext > 0, "increased", "decreased")
```

Now we're going to use a function called paste to merge some text together. We're going to paste together a sentence fragment, the percent change number and another sentence fragment together to form a sentence. We'll save it as sub, because that's what it's called in ggplot -- a subtitle.

``` 
sub <- paste("The number of people in Prince George's County fully vaccinated on ", format(latest_date$vaccination_date, format="%B %d"), " ", direction, " by ", changetext, " percent compared to the week before", sep="")
```

Here's our sentence:

``` 
sub
```

    ## [1] "The number of people in Prince George's County fully vaccinated on November 23 decreased by -54.51 percent compared to the week before"

Now we can add that to our labels.

``` 
ggplot() +
  geom_bar(data=ranked, aes(x=vaccination_date, weight=fully_vaccinated)) +
  geom_bar(data=latest_date, aes(x=vaccination_date, weight=fully_vaccinated), fill="red") +
  geom_point(data=latest_date, aes(x=vaccination_date, y=fully_vaccinated)) +
  geom_text_repel(data=latest_date, aes(x=vaccination_date, y=fully_vaccinated + 150, label="Latest date")) +
  geom_smooth(data=ranked, aes(x=vaccination_date, y=fully_vaccinated), method=loess, se=FALSE) +
  labs(title="Prince George's County Fully Vaccinated Tailing Off", subtitle=sub, x="Date", y="Fully Vaccinated") +
  theme_minimal() +
  theme(
    plot.title = element_text(size = 16, face = "bold"),
    axis.title = element_text(size = 8),
    plot.subtitle = element_text(size=10),
    panel.grid.minor = element_blank()
    )
```

    ## `geom_smooth()` using formula 'y ~ x'

    ## Warning: Removed 82 rows containing non-finite values (stat_smooth).


This is going to be a story for months, if not years. So repeating this analysis is a must for a reporter covering health care in Maryland. We've set ourselves up to do this every week when the data comes out. We just open our notebook, go to Run \> Restart R and Run All Chunks and sit back and watch as it does it all again.

Then we go report.

`<!--chapter:end:21-automatinganalysis.Rmd-->`{=html}



#  Automating geographic analysis {number="23"}

One thing that has been very apparent with the coronavirus outbreak is that this is a very geographic story. Where cases are being found and how fast is news, so it would be a good idea for us to have updating maps. But to have that, we need to have updating data.

Good news.

The New York Times is making the data behind [their interactive trackers](https://www.nytimes.com/interactive/2020/us/coronavirus-us-cases.html) [available to others for free](https://github.com/nytimes/covid-19-data).

So we have a constantly updating data stream on Github, so that means we can make this work.

Let's get our libraries first:

``` 
library(tidyverse)
library(sf)
```

We can use `read_csv` to read a URL if that URL is to a csv file. And Github just happens to provide a direct link to the CSV of county COVID-19 reports. Here's what that looks like:

``` 
covid <- read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv")
```

    ## 
    ## ── Column specification ────────────────────────────────────────────────────────
    ## cols(
    ##   date = col_date(format = ""),
    ##   county = col_character(),
    ##   state = col_character(),
    ##   fips = col_character(),
    ##   cases = col_double(),
    ##   deaths = col_double()
    ## )

Let's look at what the New York Times is providing us:

``` 
head(covid)
```

    ## # A tibble: 6 x 6
    ##   date       county    state      fips  cases deaths
    ##   <date>     <chr>     <chr>      <chr> <dbl>  <dbl>
    ## 1 2020-01-21 Snohomish Washington 53061     1      0
    ## 2 2020-01-22 Snohomish Washington 53061     1      0
    ## 3 2020-01-23 Snohomish Washington 53061     1      0
    ## 4 2020-01-24 Cook      Illinois   17031     1      0
    ## 5 2020-01-24 Snohomish Washington 53061     1      0
    ## 6 2020-01-25 Orange    California 06059     1      0

If you look, we have a county and a date -- how many cases are reported in that county on that day. That means we can do some interesting progression charts.

Let's filter out Maryland first.

``` 
maryland <- covid %>% filter(state == "Maryland")
```

And we can create line chart like this:

``` 
ggplot() + geom_line(data=maryland, aes(x=date, y=cases, group=county, color=county))
```


The colors can be a little hard to make out, but when you have counties with a large number of cases, you'd use a different kind of scale called a log scale. It's a way of representing a very wide range of data in a more compact way (more details here: <https://en.wikipedia.org/wiki/Logarithmic_scale>). [YOU REALLY SHOULD WATCH THIS](https://www.ft.com/video/9a72a9d4-8db1-4615-8333-4b73ae3ddff8). You've no doubt seen the Financial Times coronavirus trajectory tracker. Hear why they are using a log scale. And here's what our chart looks like with it. Note the y-axis scale.

``` 
ggplot() + geom_line(data=maryland, aes(x=date, y=cases, group=county, color=county)) + scale_y_continuous(trans="log10")
```

    ## Warning: Transformation introduced infinite values in continuous y-axis


This presents a more consistent story of the increase in cases.

## 23.1 Mapping continuously {number="23.1"}

But for a map, we can't have multiple days. We need a single day. Ideally, it would be the most recent date. We can get it using the `max` function.

``` 
current <- maryland %>% summarize(max(date))
```

That will give us the most recent date in Maryland in a variable called `current`. And now we can filter the most recent data for Nebraska, regardless of when this runs.

I'm adding one piece to the end to make joining this to a map easier and just renaming fips to GEOID, because they are identical in both datasets and can be used for joining.

``` 
marylandcurrent <- maryland %>% filter(date == current[[1]]) %>% rename(GEOID = fips)
```

Now we can read in our counties map layer.

``` 
counties <- st_read("data/cb_2018_us_county_5m/cb_2018_us_county_5m.shp")
```

    ## Reading layer `cb_2018_us_county_5m' from data source 
    ##   `/Users/derekwillis/code/datajournalismbook/data/cb_2018_us_county_5m/cb_2018_us_county_5m.shp' 
    ##   using driver `ESRI Shapefile'
    ## Simple feature collection with 3233 features and 9 fields
    ## Geometry type: MULTIPOLYGON
    ## Dimension:     XY
    ## Bounding box:  xmin: -179.1473 ymin: -14.55255 xmax: 179.7785 ymax: 71.35256
    ## Geodetic CRS:  NAD83

And join the two together.

``` 
counties <- counties %>% left_join(marylandcurrent)
```

    ## Joining, by = "GEOID"

Since we have every county in the United States in our counties map layer, we can filter just Nebraska like this:

``` 
mdcounties <- counties %>% filter(STATEFP == 24)
```

So now, we have a geographic dataframe that has both the county shapes and the number of cases in the most recent data update. We just need to see it now:

``` 
ggplot() +
  geom_sf(data=mdcounties, aes(fill=cases)) +
  scale_fill_viridis_c(option = "plasma", trans = "sqrt") +
  theme_void() +
  labs(title = paste("COVID-19 cases as of ", current[[1]], sep=""))
```


As it stands, we can run this every day and get an up-to-date map.

`<!--chapter:end:22-automatingmapanalysis.Rmd-->`{=html}


#  Basic Stats: Linear Regression and The T-Test {number="24"}

A month into the Covid-19 pandemic, in April 2020, Reveal, an investigative reporting outfit, [wrote a story based on original data analysis showing that a disproportionate share of PPP loans](https://revealnews.org/article/bailout-money-bypasses-hard-hit-new-york-california-for-north-dakota-nebraska/) were going to states that Donald Trump won in 2016. In North Dakota, a state that gave a higher share of its vote to Trump than all but three states, 58 percent of small businesses got PPP loans. In Democratic-leaning New York, which was hit hard in the pandemic's first wave, only 18 percent of small businesses received loans. They wrote:

"Reveal's analysis found that businesses in states that Trump won in 2016 received a far greater share of the small-business relief funds than those won by his Democratic rival, Hillary Clinton. Eight of the top 10 recipient states -- ranked according to the proportion of each state's businesses that received funding -- went to Trump in 2016. Meanwhile, seven of the bottom 10 states, where the lowest proportion of businesses received funding, went to Clinton. Taken together, 32% of businesses in states that Trump won got Paycheck Protection Program dollars, we found, compared with 22% of businesses in states that went to Clinton."

It continued: "The figures were so stark that they sparked concerns of political interference. Rep. Jackie Speier, a California Democrat who serves on the House Oversight and Reform Committee, said the data raise questions about whether stimulus dollars were deliberately funneled to states that voted for Trump and have Republican governors."

The story didn't present any evidence of political meddling. Instead, it offered the results of several lines of data analysis that attempted to answer this central question: did red states get a bigger slice of the PPP pie than blue states?

Mostly, it used basic descriptive statistics, calculating rates, ranking states and computing averages. But the data set it used also presents an opportunity to use two slightly more advanced statistical analysis methods to look for patterns: linear regression, to examine relationships, and a t.test, to confirm the statistical validity of an average between two groups. So, let's do that here.

First, let's load libraries. We're going to load janitor, the tidyverse and a new package, [corrr](https://corrr.tidymodels.org/), which will help us do linear regression a bit easier than base R.

``` 
library(janitor)
library(tidyverse)
library(corrr)
```

Now let's load the data we'll be using. It has five fields:

- state_name
- vote_2016: whether Trump or Clinton won the state's electoral vote.
- pct_trump: the percentage of the vote Trump received in the state.
- businesses_receiving_ppe_pct: the percentage of the state's small businesses that received a PPP loan.
- ppe_amount_per_employee: the average amount of money provided by PPP per small business employee in the state.

``` 
reveal_data <- read_rds("data/reveal_data.rds")

reveal_data
```

    ## # A tibble: 51 x 5
    ##    state_name   vote_2016 pct_trump businesses_receiving_p… ppe_amount_per_empl…
    ##    <chr>        <chr>         <dbl>                   <dbl>                <dbl>
    ##  1 North Dakota Trump          63.0                      58                 7928
    ##  2 Nebraska     Trump          58.8                      56                 7244
    ##  3 South Dakota Trump          61.5                      53                 6541
    ##  4 Oklahoma     Trump          65.3                      50                 6499
    ##  5 Mississippi  Trump          57.9                      49                 5674
    ##  6 Iowa         Trump          51.2                      48                 6642
    ##  7 Kansas       Trump          56.6                      47                 7087
    ##  8 Hawaii       Clinton        29.4                      47                 7417
    ##  9 Maine        Clinton        43.5                      45                 6617
    ## 10 Arkansas     Trump          60.6                      44                 5549
    ## # … with 41 more rows



#  Linear Regression {number="25"}

Let's start with this question: did small businesses in states that voted more strongly for Trump get loans at higher rate than small businesses in Democratic states? We can answer it by examining the relationship or correlation between two variables, pct_trump and businesses_receiving_ppe_pct. How much do they move in tandem? Do states with more Trump support see bigger average PPP loans? Do extra Trumpy states get even more? Do super blue states get the least?

Let's start by plotting them to get a sense of the pattern.

``` 
reveal_data %>%
  ggplot() +
  geom_point(aes(x=pct_trump,y=businesses_receiving_ppe_pct)) +
  geom_smooth(aes(x=pct_trump,y=businesses_receiving_ppe_pct), method="lm")
```

    ## `geom_smooth()` using formula 'y ~ x'


Let's test another variable, the average amount of money provided by PPP per small business employee in the state.

``` 
reveal_data %>%
  ggplot() +
  geom_point(aes(x=pct_trump,y=ppe_amount_per_employee)) +
  geom_smooth(aes(x=pct_trump,y=ppe_amount_per_employee), method="lm")
```

    ## `geom_smooth()` using formula 'y ~ x'


We can be a bit more precise by calculating a statistic called the correlation coefficient, also called "r." r is a value between 1 and -1. An r of 1 indicates a strong positive correlation.

An increase in air temperature and air conditioning use at home is strongly-positively correlated: the hotter it gets, the more we have to use air conditioning. If we were to plot those two variables, we might not get 1, but we'd get close to it.

An r of -1 indicates a strong negative correlation. An increase in temperature and home heating use is strongly negatively correlated: the hotter it gets, the less heat we use indoors. We might not hit -1, but we'd probably get close to it.

A correlation of 0 indicates no relationship.

All r values will fall somewhere on this scale, and how to interpret them isn't always straightforward. They're best used to give general guidance when exploring patterns.

We can calculate r with a function from the corrr package called "correlate()." First, we remove the non-numeric values from our reveal_data (state name and a binary vote_2016 column), then we correlate.

``` 
reveal_data %>%
  select(-state_name, -vote_2016) %>%
  correlate() %>%
  select(term, pct_trump)
```

    ## 
    ## Correlation method: 'pearson'
    ## Missing treated using: 'pairwise.complete.obs'

    ## # A tibble: 3 x 2
    ##   term                         pct_trump
    ##   <chr>                            <dbl>
    ## 1 pct_trump                       NA    
    ## 2 businesses_receiving_ppe_pct     0.522
    ## 3 ppe_amount_per_employee          0.221

``` 
#glimpse(reveal_data)
```

The table this function produces generally confirms our interpretation of the two graphs above. The relationship between a state's pct_trump and ppe_amount_per employee is positive, but at .22 (on a scale of -1 to 1), the relationship isn't particularly strong. That's why the second graphic above was messier than the first.

The relationship between businesses in a state receiving ppe and the state's Trump vote is a bit stronger, if still moderate, .52 (on a scale of -1 to 1). Is this finding statistically valid? We can get a general sense of that by calculating the p-value of this correlation, a test of statistical significance. For that, we can use the cor.test function.

``` 
cor.test(reveal_data$pct_trump, reveal_data$businesses_receiving_ppe_pct)
```

    ## 
    ##  Pearson's product-moment correlation
    ## 
    ## data:  reveal_data$pct_trump and reveal_data$businesses_receiving_ppe_pct
    ## t = 4.2818, df = 49, p-value = 0.00008607
    ## alternative hypothesis: true correlation is not equal to 0
    ## 95 percent confidence interval:
    ##  0.2875734 0.6971386
    ## sample estimates:
    ##       cor 
    ## 0.5218038

This output is quite a bit uglier, but for our purposes there are two key pieces of information from this chunk of unfamiliar words. First, it shows the correlation calculated above: r 0.5218. Two, it shows the p-value, which is 0.00008607. That's very low, as far as p-values go, which indicates that there's a very slim chance that our finding is a statistical aberration.

Now let's test the other one, the relationship between the pct_trump and the ppe_amount_per_employee.

``` 
cor.test(reveal_data$pct_trump, reveal_data$ppe_amount_per_employee)
```

    ## 
    ##  Pearson's product-moment correlation
    ## 
    ## data:  reveal_data$pct_trump and reveal_data$ppe_amount_per_employee
    ## t = 1.5872, df = 49, p-value = 0.1189
    ## alternative hypothesis: true correlation is not equal to 0
    ## 95 percent confidence interval:
    ##  -0.05798429  0.46818515
    ## sample estimates:
    ##      cor 
    ## 0.221133

Again, it shows our r value of .22, which was weaker. And the p-value here is a much larger 0.12. That indicates a higher chance of our finding being a statistical aberration, high enough that I wouldn't rely on its validity.

p \< .05 is accepted in many scientific disciplines -- and by many data journalists -- as the cutoff for statistical significance. But there's heated debate about that level, and some academics question whether p-values should be relied on so heavily.

And to be clear, a low p-value does not prove that we've found what we set out to find. There's nothing on this graph or in the regression model output that proves that Trump's administration tipped the scales in favor of states that voted for it. It's entirely possible that there's some other variable -- or variables -- not considered here that explain this pattern.

All we know is that we've identified a potentially promising pattern, worthy of additional reporting and analysis to flesh out.


#  T-tests {number="26"}

Let's suppose we want to ask a related set of questions: did Trump states get higher ppp loan amounts per employee than states won by Clinton? Or did a larger percentage of businesses in states won by Trump receive, on average, a higher rate of PPP loans on average than states won by Clinton.

We can do this because, in our data, we have a column with two possible categorical values, Clinton or Trump, for each state.

We could just calculate the averages like we're used to doing.

``` 
reveal_data %>%
  group_by(vote_2016) %>%
  summarise(
    mean_ppp_amount_per_employee = mean(ppe_amount_per_employee),
    mean_businesses_receiving_ppe_pct = mean(businesses_receiving_ppe_pct)
  )
```

    ## # A tibble: 2 x 3
    ##   vote_2016 mean_ppp_amount_per_employee mean_businesses_receiving_ppe_pct
    ##   <chr>                            <dbl>                             <dbl>
    ## 1 Clinton                          5704.                              28.2
    ## 2 Trump                            6021.                              37.2

Examining this, it appears that in both categories there's a difference.

The average amount of ppp loans per employee in Clinton states is smaller than Trump states (6,000 to 5,700). And the average percentage of businesses that got loans in Trump states was larger -- 37% -- than Clinton states -- 28%. Should we report these as meaningful findings?

A t-test can help us answer that question. It can tell us where there's a statistically significant difference between the means of two groups. Have we found a real difference, or have we chanced upon a statistical aberration? Let's see by calculating it for the average loan amount.

``` 
t.test(ppe_amount_per_employee ~ vote_2016, data = reveal_data)
```

    ## 
    ##  Welch Two Sample t-test
    ## 
    ## data:  ppe_amount_per_employee by vote_2016
    ## t = -1.2223, df = 36.089, p-value = 0.2295
    ## alternative hypothesis: true difference in means between group Clinton and group Trump is not equal to 0
    ## 95 percent confidence interval:
    ##  -843.7901  209.1329
    ## sample estimates:
    ## mean in group Clinton   mean in group Trump 
    ##              5703.571              6020.900

We see our two means, for Trump and Clinton, the same as we calculated above. The t-value is approximately 1, the p-value here is .2295, both of which should which should give us pause that we've identified something meaningful. [More on t-tests here](https://conjointly.com/kb/statistical-student-t-test/)

Let's try the percentage of businesses getting ppp loans.

``` 
t.test(businesses_receiving_ppe_pct ~ vote_2016, data = reveal_data)
```

    ## 
    ##  Welch Two Sample t-test
    ## 
    ## data:  businesses_receiving_ppe_pct by vote_2016
    ## t = -3.182, df = 45.266, p-value = 0.002643
    ## alternative hypothesis: true difference in means between group Clinton and group Trump is not equal to 0
    ## 95 percent confidence interval:
    ##  -14.68807  -3.30241
    ## sample estimates:
    ## mean in group Clinton   mean in group Trump 
    ##              28.23810              37.23333

This is a bit more promising. T is much stronger -- about 3 -- and the p-value is .002. Both of these should give us assurance that we've found something statistically meaningful. Again, this doesn't prove that Trump is stacking the deck for states. It just suggests there's a pattern worth following up on.

`<!--chapter:end:23-basicstats.Rmd-->`{=html}



#  An intro to text analysis {number="27"}

Throughout this course, we've been focused on finding information in structured data. We've learned a lot of techniques to do that, and we've learned how the creative mixing and matching of those skills can find new insights.

What happens when the insights are in unstructured data? Like a block of text?

Turning unstructured text into data to analyze is a whole course in and of itself -- and one worth taking if you've got the credit hours -- but some simple stuff is in the grasp of basic data analysis.

To do this, we'll need a new library -- [tidytext](https://cran.r-project.org/web/packages/tidytext/vignettes/tidytext.html), which you can guess by the name plays very nicely with the tidyverse. So install it with `install.packages("tidytext")` and we'll get rolling.

``` 
library(tidyverse)
library(tidytext)
library(janitor)
library(lubridate)
```

Here's the question we're going to go after: How did federal politicians talk about the coronavirus pandemic on Twitter?

To answer this question, we'll use a dataset of tweets posted by federal politicians from both campaign and official accounts that mentioned either "COVID" or "coronavirus" beginning on Feb. 1, 2020. This dataset doesn't include retweets, only original tweets. Let's read in this data and examine it:

``` 
covid_tweets <- read_rds('data/covid_tweets.rds')
```

We can see what it looks like with head:

``` 
head(covid_tweets)
```

    ## # A tibble: 6 x 12
    ##        id user_name  content     created             branch state district title
    ##     <dbl> <chr>      <chr>       <dttm>              <chr>  <chr> <chr>    <chr>
    ## 1 1.46e18 RepCharli… "What are … 2021-11-24 21:53:05 H      FL    13       Hous…
    ## 2 1.46e18 swan4cong… "Joe Biden… 2021-11-24 21:42:53 H      GA    10       Hous…
    ## 3 1.46e18 TonyVargas "This than… 2021-11-24 21:32:43 H      NE    02       Hous…
    ## 4 1.46e18 RepGregSt… "I wonder … 2021-11-24 21:16:48 H      FL    17       Hous…
    ## 5 1.46e18 Squires20… "Don’t for… 2021-11-24 20:36:53 H      TX    22       Hous…
    ## 6 1.46e18 RepDerekK… "90% of Am… 2021-11-24 20:33:39 H      WA    06       Hous…
    ## # … with 4 more variables: first_name <chr>, last_name <chr>, gender <chr>,
    ## #   party <chr>

What we want to do is to make the `content` column easier to analyze. Let's say we want to find out the most commonly used words. We'll probably want to remove URLs from the text of the tweets since they aren't actual words. Let's use mutate to make that happen:

``` 
covid_tweets <- covid_tweets %>%
  mutate(content = gsub("http.*","", content))
```

If you are trying to create a list of unique words, R will treat differences in capitalization as unique and also will include punctuation by default, even using its `unique` function:

``` 
a_list_of_words <- c("Dog", "dog", "dog", "cat", "cat", ",")
unique(a_list_of_words)
```

    ## [1] "Dog" "dog" "cat" ","

Fortunately, this is a solved problem with tidytext, which has a function called `unnest_tokens` that will convert the text to lowercase and remove all punctuation. The way that `unnest_tokens` works is that we tell it what we want to call the field we're creating with this breaking apart, then we tell it what we're breaking apart -- what field has all the text in it. For us, that's the `content` column:

``` 
unique_words <- covid_tweets %>% select(content) %>%
  unnest_tokens(word, content)
View(unique_words)
```

Now we can look at the top words in this dataset. Let's limit ourselves to making a plot of the top 25 words:

``` 
unique_words %>%
  count(word, sort = TRUE) %>%
  top_n(25) %>%
  mutate(word = reorder(word, n)) %>%
  ggplot(aes(x = word, y = n)) +
  geom_col() +
  xlab(NULL) +
  coord_flip() +
      labs(x = "Count",
      y = "Unique words",
      title = "Count of unique words found in tweets")
```

    ## Selecting by n


Well, that's a bit underwhelming - a lot of very common (and short) words. This also is a solved problem in working with text data, and words like "a" and "the" are known as "stop words." In most cases you'll want to remove them from your analysis since they are so common. Tidytext provides a dataframe of them:

``` 
data("stop_words")
```

Then we're going to use a function we haven't used yet called an `anti_join`, which filters out any matches. So we'll `anti_join` the stop words and get a list of words that aren't stop words.

From there, we can get a simple word frequency by just grouping them together and counting them. We can borrow the percent code from above to get a percent of the words our top 10 words represent.

``` 
unique_words %>%
  anti_join(stop_words) %>%
  group_by(word) %>%
  tally(sort=TRUE) %>%
  mutate(percent = (n/sum(n))*100) %>%
  top_n(10)
```

    ## Joining, by = "word"

    ## Selecting by percent

    ## # A tibble: 10 x 3
    ##    word            n percent
    ##    <chr>       <int>   <dbl>
    ##  1 covid       78694   2.91 
    ##  2 19          51817   1.91 
    ##  3 covid19     44862   1.66 
    ##  4 amp         43735   1.62 
    ##  5 coronavirus 35713   1.32 
    ##  6 health      20832   0.769
    ##  7 pandemic    20494   0.757
    ##  8 relief      17576   0.649
    ##  9 people      14046   0.519
    ## 10 vaccine     12707   0.469

Those seem like more relevant unique words. Now, here's where we can start to do more interesting and meaningful analysis. Let's create two dataframes of unique words based on time: one for all of 2020 and the other for all of 2021:

``` 
unique_words_2020 <- covid_tweets %>%
  filter(created < '2021-01-01') %>%
  select(content) %>%
  unnest_tokens(word, content)

unique_words_2021 <- covid_tweets %>%
  filter(created >= '2021-01-01') %>%
  select(content) %>%
  unnest_tokens(word, content)
```

Then we can create top 10 lists for both of them and compare:

``` 
unique_words_2020 %>%
  anti_join(stop_words) %>%
  group_by(word) %>%
  tally(sort=TRUE) %>%
  mutate(percent = (n/sum(n))*100) %>%
  top_n(10)
```

    ## Joining, by = "word"

    ## Selecting by percent

    ## # A tibble: 10 x 3
    ##    word            n percent
    ##    <chr>       <int>   <dbl>
    ##  1 covid       47028   2.33 
    ##  2 covid19     36636   1.81 
    ##  3 19          34373   1.70 
    ##  4 coronavirus 34338   1.70 
    ##  5 amp         33559   1.66 
    ##  6 health      16697   0.826
    ##  7 pandemic    14957   0.740
    ##  8 relief      12672   0.627
    ##  9 people      10619   0.525
    ## 10 crisis       9125   0.451

``` 
unique_words_2021 %>%
  anti_join(stop_words) %>%
  group_by(word) %>%
  tally(sort=TRUE) %>%
  mutate(percent = (n/sum(n))*100) %>%
  top_n(10)
```

    ## Joining, by = "word"
    ## Selecting by percent

    ## # A tibble: 10 x 3
    ##    word         n percent
    ##    <chr>    <int>   <dbl>
    ##  1 covid    31666   4.61 
    ##  2 19       17444   2.54 
    ##  3 amp      10176   1.48 
    ##  4 vaccine   8982   1.31 
    ##  5 covid19   8226   1.20 
    ##  6 pandemic  5537   0.807
    ##  7 relief    4904   0.715
    ##  8 health    4135   0.603
    ##  9 vaccines  3516   0.512
    ## 10 people    3427   0.499

In the 2021 top 10 list, "vaccine" and its variations are much more prominent, which makes sense, while "testing" drops out of the top 10 compared to 2020.

## 27.1 Going beyond a single word {number="27.1"}

The next step in text analysis is using `ngrams`. An `ngram` is any combination of words that you specify. Two word ngrams are called bigrams (bi-grams). Three would be trigrams. And so forth.

The code to make ngrams is similar to what we did above, but involves some more twists.

So this block is is going to do the following:

1.  Use the covid_tweets data we created above, and filter for pre-2021 tweets.
2.  Unnest the tokens again, but instead we're going to create a field called bigram, break apart summary, but we're going to specify the tokens in this case are ngrams of 2.
3.  We're going to make things easier to read and split bigrams into word1 and word2.
4.  We're going to filter out stopwords again, but this time we're going to do it in both word1 and word2 using a slightly different filtering method.
5.  Because of some weirdness in calculating the percentage, we're going to put bigram back together again, now that the stop words are gone.
6.  We'll then group by, count and create a percent just like we did above.
7.  We'll then use top_n to give us the top 10 bigrams.

``` 
covid_tweets %>%
  filter(created < '2021-01-01') %>%
  unnest_tokens(bigram, content, token = "ngrams", n = 2) %>%
  separate(bigram, c("word1", "word2"), sep = " ") %>%
  filter(!word1 %in% stop_words$word) %>%
  filter(!word2 %in% stop_words$word) %>%
  mutate(bigram = paste(word1, word2, sep=" ")) %>%
  group_by(bigram) %>%
  tally(sort=TRUE) %>%
  mutate(percent = (n/sum(n))*100) %>%
  top_n(10)
```

    ## Selecting by percent

    ## # A tibble: 10 x 3
    ##    bigram                   n percent
    ##    <chr>                <int>   <dbl>
    ##  1 covid 19             32302   3.52 
    ##  2 health care           4388   0.478
    ##  3 public health         3908   0.426
    ##  4 covid19 pandemic      3206   0.349
    ##  5 town hall             3014   0.328
    ##  6 coronavirus pandemic  2915   0.318
    ##  7 19 pandemic           2670   0.291
    ##  8 covid relief          2246   0.245
    ##  9 relief package        2062   0.225
    ## 10 covid ー              1832   0.200

And we already have a different, more nuanced result. Health was among the top single words, and we can see that "health care" and "public health" are among the top 2-word phrases. What about after 2021?

``` 
covid_tweets %>%
  filter(created >= '2021-01-01') %>%
  unnest_tokens(bigram, content, token = "ngrams", n = 2) %>%
  separate(bigram, c("word1", "word2"), sep = " ") %>%
  filter(!word1 %in% stop_words$word) %>%
  filter(!word2 %in% stop_words$word) %>%
  mutate(bigram = paste(word1, word2, sep=" ")) %>%
  group_by(bigram) %>%
  tally(sort=TRUE) %>%
  mutate(percent = (n/sum(n))*100) %>%
  top_n(10)
```

    ## Selecting by percent

    ## # A tibble: 10 x 3
    ##    bigram               n percent
    ##    <chr>            <int>   <dbl>
    ##  1 covid 19         17357   5.35 
    ##  2 19 vaccine        2638   0.814
    ##  3 covid relief      2159   0.666
    ##  4 19 pandemic       1495   0.461
    ##  5 covid19 vaccine   1227   0.379
    ##  6 covid vaccine     1099   0.339
    ##  7 health care        908   0.280
    ##  8 covid19 pandemic   872   0.269
    ##  9 public health      860   0.265
    ## 10 19 relief          805   0.248

While "covid 19" is still the leading phrase, vaccine-related phrases dominate the top 10, and "public health" and "health care" have slipped down the list.

So far, we've only looked at the entire set of tweets, not any characteristics of who posted them. Would these lists be any different for Democrats and Republicans? To find out, we just need to add to our filter.

``` 
covid_tweets %>%
  filter(created < '2021-01-01', party == 'D') %>%
  unnest_tokens(bigram, content, token = "ngrams", n = 2) %>%
  separate(bigram, c("word1", "word2"), sep = " ") %>%
  filter(!word1 %in% stop_words$word) %>%
  filter(!word2 %in% stop_words$word) %>%
  mutate(bigram = paste(word1, word2, sep=" ")) %>%
  group_by(bigram) %>%
  tally(sort=TRUE) %>%
  mutate(percent = (n/sum(n))*100) %>%
  top_n(10)
```

    ## Selecting by percent

    ## # A tibble: 10 x 3
    ##    bigram                   n percent
    ##    <chr>                <int>   <dbl>
    ##  1 covid 19             22182   3.57 
    ##  2 health care           3398   0.547
    ##  3 public health         3314   0.534
    ##  4 town hall             2481   0.400
    ##  5 covid19 pandemic      2426   0.391
    ##  6 19 pandemic           1923   0.310
    ##  7 coronavirus pandemic  1903   0.307
    ##  8 covid relief          1525   0.246
    ##  9 relief package        1478   0.238
    ## 10 social distancing     1373   0.221

``` 
covid_tweets %>%
  filter(created < '2021-01-01', party == 'R') %>%
  unnest_tokens(bigram, content, token = "ngrams", n = 2) %>%
  separate(bigram, c("word1", "word2"), sep = " ") %>%
  filter(!word1 %in% stop_words$word) %>%
  filter(!word2 %in% stop_words$word) %>%
  mutate(bigram = paste(word1, word2, sep=" ")) %>%
  group_by(bigram) %>%
  tally(sort=TRUE) %>%
  mutate(percent = (n/sum(n))*100) %>%
  top_n(10)
```

    ## Selecting by percent

    ## # A tibble: 10 x 3
    ##    bigram                   n percent
    ##    <chr>                <int>   <dbl>
    ##  1 covid 19              9901   3.45 
    ##  2 coronavirus pandemic   966   0.336
    ##  3 health care            943   0.328
    ##  4 ー 19                  782   0.272
    ##  5 covid ー               782   0.272
    ##  6 covid19 pandemic       769   0.268
    ##  7 cares act              759   0.264
    ##  8 19 pandemic            733   0.255
    ##  9 american people        711   0.248
    ## 10 covid relief           703   0.245

Now we can begin to see some differences between the parties. We also could do the same for different kinds of accounts: the `title` column represents the role of the account, and if it includes "Candidate" then the tweet is from a campaign account. Let's compare House of Representatives' official and campaign tweets during 2020:

``` 
covid_tweets %>%
  filter(created < '2021-01-01', title == 'House Representative') %>%
  unnest_tokens(bigram, content, token = "ngrams", n = 2) %>%
  separate(bigram, c("word1", "word2"), sep = " ") %>%
  filter(!word1 %in% stop_words$word) %>%
  filter(!word2 %in% stop_words$word) %>%
  mutate(bigram = paste(word1, word2, sep=" ")) %>%
  group_by(bigram) %>%
  tally(sort=TRUE) %>%
  mutate(percent = (n/sum(n))*100) %>%
  top_n(10)
```

    ## Selecting by percent

    ## # A tibble: 10 x 3
    ##    bigram                   n percent
    ##    <chr>                <int>   <dbl>
    ##  1 covid 19             15796   3.53 
    ##  2 town hall             2265   0.507
    ##  3 health care           2093   0.468
    ##  4 public health         2033   0.455
    ##  5 covid19 pandemic      1851   0.414
    ##  6 19 pandemic           1522   0.341
    ##  7 coronavirus pandemic  1457   0.326
    ##  8 covid relief          1108   0.248
    ##  9 telephone town        1051   0.235
    ## 10 relief package        1010   0.226

``` 
covid_tweets %>%
  filter(created < '2021-01-01', title == 'House Candidate') %>%
  unnest_tokens(bigram, content, token = "ngrams", n = 2) %>%
  separate(bigram, c("word1", "word2"), sep = " ") %>%
  filter(!word1 %in% stop_words$word) %>%
  filter(!word2 %in% stop_words$word) %>%
  mutate(bigram = paste(word1, word2, sep=" ")) %>%
  group_by(bigram) %>%
  tally(sort=TRUE) %>%
  mutate(percent = (n/sum(n))*100) %>%
  top_n(10)
```

    ## Selecting by percent

    ## # A tibble: 10 x 3
    ##    bigram                   n percent
    ##    <chr>                <int>   <dbl>
    ##  1 covid 19              8378   3.38 
    ##  2 public health          778   0.314
    ##  3 covid ー               722   0.291
    ##  4 ー 19                  721   0.291
    ##  5 health care            721   0.291
    ##  6 19 pandemic            519   0.209
    ##  7 social distancing      518   0.209
    ##  8 coronavirus pandemic   512   0.207
    ##  9 town hall              482   0.195
    ## 10 covid relief           458   0.185

There are some differences here, too, but also some potential challenges to doing an analysis. For one, there are variations of words like "vaccine" that could probably be standardized - maybe using OpenRefine - that would give us cleaner results. There might be some words among our list of stop words that actually are meaningful in this context.

## 27.2 Sentiment Analysis {number="27.2"}

Another popular use of text analysis is to measure the sentiment of a word - whether it expresses a positive or negative idea - and tidytext has built-in tools to make that possible. We use word counts like we've already calculated and bring in a dataframe of words (called a lexicon) along with their sentiments using a function called `get_sentiments`. The most common dataframe is called "bing" which has nothing to do with the Microsoft search engine. Let's load it:

``` 
bing <- get_sentiments("bing")

bing_word_counts_2020 <- unique_words_2020 %>%
  inner_join(bing) %>%
  count(word, sentiment, sort = TRUE)
```

    ## Joining, by = "word"

``` 
bing_word_counts_2021 <- unique_words_2021 %>%
  inner_join(bing) %>%
  count(word, sentiment, sort = TRUE)
```

    ## Joining, by = "word"

``` 
View(bing_word_counts_2020)
View(bing_word_counts_2021)
```

Gauging the sentiment of a word can be heavily dependent on the context, and as with other types of text analysis sometimes larger patterns are more meaningful than individual results. But the potential with text analysis is vast: knowing what words and phrases that public officials employ can be a way to evaluate their priorities, cohesiveness and tactics for persuading voters and their colleagues. And those words and phrases are data.

`<!--chapter:end:24-textanalysis.Rmd-->`{=html}


#  Writing with numbers {number="28"}

The number one sin of all early career data journalist is to get really, really, really attached to the analysis you've done and include every number you find.

Don't do that.

Numbers tell you what. Numbers rarely tell you why. What question has driven most people since they were three years old? Why. The very first thing to do is realize that is the purpose of reporting. You've done the analysis to determine the what. Now go do the reporting to do the why. Or as an old editor of mine used to say "Now go do that reporting shit you do."

The trick to writing a numbers story is to frame your story around people. Sometimes, your lead can be a number, if that number is compelling. Often, your lead is a person, a person who is one of the numbers you are writing about.

Tell their story. Briefly. Then, let us hear from them. Let them speak about what it is you are writing about.

Then come the numbers.

## 28.1 How to write about numbers without overwhelming with numbers. {number="28.1"}

Writing complex stories is often a battle against that complexity. You don't want to overwhelm. You want to simplify where you can. The first place you can do that is only use exact numbers where an exact number is called for.

Where you can, do the following:

- Using ratios instead of percents
- Often, it's better to put it in counts of 10. 6 of 10, 4 of 10. It's easy to translate that from a percentage to a ratio.
- But be careful when your number is 45 percent. Is that 4 in 10 or 5 in 10?
- If a ratio doesn't make sense, round. There's 287,401 people in Lincoln, according to the Census Bureau. It's easier, and no less accurate, to say there's more than 287,000 people in Lincoln.

**A critical question your writing should answer: As compared to what?**

How does this compare to the average? The state? The nation? The top? The bottom?

One of the most damning numbers in the series of stories Craig Pittman and I wrote that became the book [Paving Paradise](https://www.amazon.com/Paving-Paradise-Floridas-Vanishing-Wetlands-ebook/dp/B004HZXZCE) was comparing approvals and denials.

We were looking at the US Army Corps of Engineers and their permitting program. We were able to get a dataset of just a few years of permits that was relatively clean. From that, we were able to count the number of times the corps had said yes to a developer to wipe out wetlands the law protected and how many times they said no.

They said yes 12,000 times. They said no once.

That one time? Someone wanted to build an eco-lodge in the Everglades. Literally. Almost every acre of the property was wetlands. So in order to build it, the developer would have to fill in the very thing they were going to try to bring people into. The corps said no.

## 28.2 When exact numbers matter {number="28.2"}

Sometimes ratios and rounding are not appropriate.

This is being written in the days of the coronavirus. Case counts are where an exact number is called for. You don't say that there are more than 70 cases in Lancaster County on the day this was written. You specify. It's 75.

You don't say almost 30 deaths. It's 28.

Where this also comes into play is any time there are deaths: Do not round bodies.

## 28.3 An example {number="28.3"}

[Read this story from USA Today and the Arizona Republic](https://www.azcentral.com/in-depth/news/local/arizona-wildfires/2019/07/22/wildfire-risks-more-than-500-spots-have-greater-hazard-than-paradise/1434502001/). Notice first that the top sets up a conflict: People say one thing, and that thing is not true.

> No one could have anticipated such a catastrophe, people said. The fire's speed was unprecedented, the ferocity unimaginable, the devastation unpredictable.

> Those declarations were simply untrue. Though the toll may be impossible to predict, worst-case fires are a historic and inevitable fact.

The first voice you hear? An expert who studies wildfires.

> Phillip Levin, a researcher at the University of Washington and lead scientist for the Nature Conservancy in Washington, puts it this way: "Fire is natural. But the disaster happens because people didn't know to leave, or couldn't leave. It didn't have to happen."

Then notice how they take what is a complex analysis using geographic information systems, raster analysis, the merging of multiple different datasets together and show that it's quite simple -- the averaging together of pixels on a 1-5 scale.

Then, the compare what they found to a truly massive fire: The Paradise fire that burned 19,000 structures.

> Across the West, 526 small communities --- more than 10 percent of all places --- rank higher.

And that is how it's done. Simplify, round, ratios: simple metrics, powerful results.

`<!--chapter:end:25-writingwithdata.Rmd-->`{=html}



#  Ethics in data journalism {number="29"}

[This originally appeared on Open News in March 2013](https://source.opennews.org/articles/public-info-doesnt-always-want-be-free/).

In 2009, a senior web editor asked me and another developer a question: could our development group build a new news application for Tampabay.com that displayed a gallery of mug shots? Stories about goofy crimes with strange mug shots were popular with readers. The vision, on the part of management, was a website that would display the mugshots collected every day from publicly available websites by two editors---well paid, professional editors with other responsibilities.

Newsrooms are many things. Alive. Filled with energy. Fueled by stress, coffee and profanity. But they are also idea factories. Day after day, ideas come from everywhere. From reporters on the beat. From editors reading random things. From who knows where. Some of them are brilliant. Some would never work. Most need more people and time than are available. And some are dumber than anyone cares to admit.

We thought this idea was nuts. Why would we pay someone, let alone an editor, to fetch mug shots from the Internet? Couldn't we do that with a scraper?

If only this were the most complex question we would face.

Because given enough time and enough creativity, scraping a mug shot website is easy. You need to recognize a pattern, parse some HTML and gather the pieces you need. At least that's how it should work. Police agencies that put mugs online usually buy software from a vendor. Apparently, those vendors enjoy making horrific, non-standard, broken-in-interesting-and-unique-ways HTML. You'll swear. A lot. But you'll grind it out. And that's part of the fun. Scraping isn't any fun with clean, semantic, valid HTML. And scraping mug shot websites, by that definition, is tons of fun.

The complexity comes when you realize the data you are dealing with represent real people's lives.

## 29.1 Problems {number="29.1"}

The first problem we faced, long before we actually had data, was that data has a life of its own. Because we were going to put this information in front of a big audience, Google was going to find it. That meant if we used our normal open door policy for the Googlebot, someone's mug shot was going to be the first record in Google for their name, most likely. It would show up first because most people dont actively cultivate their name on the web for visibility in Google. It would show up first because we know how SEO works and they dont. It would show up first because our site would have more traffic than their site, and so Google would rank us higher.

And that record in Google would exist as long as the URL did. Longer when you consider the cached versions Google keeps.

That was a problem because here are the things we could not know:

- Was this person wrongly arrested?
- Was this person innocent?
- Were the charges dropped against this person?
- Did this person lie about any of their information?

## 29.2 The Googlebot {number="29.2"}

So it turned out to be very important to know the Googlebot. It's your friend ... until it isn't. We went to our bosses and said words that no one had said to them before: we did not want Google to index these pages. In a news organization, the page view is the coin of the realm. It is --- unfortunately --- how many things are evaluated when the bosses ask if it was successful or not. So, with that in mind, Google is your friend. Google brings you traffic. Indeed, Google is your single largest referrer of traffic at a news organization, so you want to throw the doors open and make friends with the Googlebot.

But here we were, saying Google wasn't our friend and that we needed to keep the Googlebot out. And, thankfully, our bosses listened to our argument. They too didn't want to be the first result in Google for someone.

So, to make sure we were telling the Googlebot no, we used three lines of defense. We told it no in robots.txt and on individual pages as a meta tag, and we put the most interesting bits of data into a simple JavaScript wrapper that made it hard on the bot if the first two things failed.

The second solution had ramifications beyond the Googlebot. We decided that we were not trying to make a complete copy of the public record. That existed already. If you wanted to look at the actual public records, the sheriff's offices in the area had websites and they were the official keeper of the record. We were making browsing those images easy, but we were not the public record.

That freedom had two consequences: it meant our scrapers could, at a certain point and given a number of failures, just give up on getting a mug. Data entered by humans will be flawed. There will be mistakes. Because of that, our code would have to try and deal with that. Well, there's an infinite number of ways people can mess things up, so we decided that since we were not going to be an exact copy of the public record, we could deal with the most common failures and dump the rest. During testing, we were getting well over 98% of mugs without having to spend our lives coding for every possible variation of typo.

The second consequence of the decision actually came from the newspapers lawyers. They asked a question that dumbfounded us: How long are you keeping mugs? We never thought about it. Storage was cheap. We just assumed we'd keep them all. But, why should we do that? If we're not a copy of the public record, we dont have to keep them. And, since we didnt know the result of each case, keeping them was really kind of pointless.

So, we asked around: How long does a misdemeanor case take to reach a judgement? The answer we got from various sources was about 60 days. From arrest to adjudication, it took about two months. So, at the 60 day mark, we deleted the data. We had no way of knowing if someone was guilty or innocent, so all of them had to go. We even called the script The Reaper.

We'd later learn that the practical impacts of this were nil. People looked at the day's mugs and moved on. The amount of traffic a mug got after the day of arrest was nearly zero.

## 29.3 Data Lifetimes {number="29.3"}

The life of your data matters. You have to ask yourself, Is it useful forever? Does it become harmful after a set time? We had to confront the real impact of deleting mugs after 60 days. People share them, potentially lengthening their lifetime long after they've fallen off the homepage. Delete them and that URL goes away.

We couldn't stop people from sharing links on social media---and indeed probably didn't want to stop them from doing it. Heck, we did it while we were building it. We kept IMing URLs to each other. And that's how we realized we had a problem. All our work to minimize the impact on someone wrongly accused of a crime could be damaged by someone sharing a link on Facebook or Twitter.

There's a difference between frictionless and unobstructed sharing and some reasonable constraints.

We couldn't stop people from posting a mug on Facebook, but we didn't have to make it easy and we didn't have to put that mug front and center. So we blocked Facebook from using the mug as the thumbnail image on a shared link. And, after 60 days, the URL to the mug will throw a 404 page not found error. Because it's gone.

We couldn't block Google from memorializing someone's arrest, only to let it live on forever on Facebook.

## 29.4 You Are a Data Provider {number="29.4"}

The last problem didn't come until months later. And it came in the middle of the night. Two months after we launched, my phone rang at 1 a.m. This is never a good thing. It was my fellow developer, Jeremy Bowers, now with NPR, calling me from a hotel in Washington DC where he was supposed to appear in a wedding the next day. Amazon, which we were using for image hosting, was alerting him that our bandwidth bills had tripled on that day. And our traffic hadn't changed.

What was going on?

After some digging, we found out that another developer had scraped our site---because we were so much easier to scrape than the Sheriff's office sites---and had built a game out of our data called Pick the Perp. There were two problems with this: 1. The game was going viral on Digg (when it was still a thing) and Reddit. It was getting huge traffic. 2. That developer had hotlinked our images. He/she was serving them from our S3 account, which meant we were bearing the costs. And they were going up exponentially by the minute.

What we didn't realize when we launched, and what we figured out after Pick the Perp, was that we had become data provider, in a sense. We had done the hard work of getting the data out of a website and we put it into neat, semantic, easily digestible HTML. If you were after a stream of mugshots, why go through all the hassle of scraping four different sheriff's office's horrible HTML when you could just come get ours easily?

Whoever built Pick the Perp, at least at the time, chose to use our site. But, in doing so, they also chose to hotlink images---use the URL of our S3 bucket, which cost us money---instead of hosting the images themselves.

That was a problem we hadn't considered. People hotlink images all the time. And, until those images are deleted from our system, they'll stay hotlinked somewhere.

Amazon's S3 has a system where you can attach a key to a file that expires after X period of time. In other words, the URL to your image only lasts 15 minutes, or an hour, or however long you decide, before it breaks. It gives you fine grained control over how long someone can use your image URL.

So at 3 a.m., after two hours of pulling our hair out, we figured out how to sync our image keys with our cache refreshes. So every 15 minutes, a url to an image expired and Pick the Perp came crashing down.

While the Pick the Perp example is an easy one---it's never cool to hotlink an image---it does raise an issue to consider. Because you are thinking carefully about how to build your app the right way doesn't mean someone else will. And it doesn't mean they won't just go take your data from your site. So how could you deal with that? Make the data available as a download? Create an API that uses your same ethical constructs? Terms of service? All have pros and cons and are worth talking about before going forward.

## 29.5 Ethical Data {number="29.5"}

We live in marvelous times. The web offers you no end of tools to make things on the web, to put data from here on there, to make information freely available. But, we're an optimistic lot. Developers want to believe that their software is being used only for good. And most people will use it for good. But, there are times where the data you're working with makes people uncomfortable. Indeed, much of journalism is about making people uncomfortable, publishing things that make people angry, or expose people who don't want to be exposed.

What I want you to think about, before you write a line of code, is what does it mean to put your data on the internet? What could happen, good and bad? What should you do to be responsible about it?

Because it can have consequences.

On Dec. 23, the Journal News in New York published a map of every legal gun permit holder in their home circulation county. It was a public record. They put it into Google Fusion Tables and Google dutifully geocoded the addresses. It was a short distance to publication from there.

Within days, angry gun owners had besieged the newspaper with complaints, saying the paper had given criminals directions to people's houses where they'd find valuable guns to steal. They said the paper had violated their privacy. One outraged gun owner assembled a list of the paper's staff, including their home addresses, telephone numbers, email addresses and other details. The paper hired armed security to stand watch at the paper.

By February, the New York state legislature removed handgun permits from the public record, citing the Journal News as the reason.

There's no end of arguments to be had about this, but the simple fact is this: The reason people were angry was because you could click on a dot on the map and see a name and an address. In Fusion Tables, removing that info window would take two clicks.

Because you can put data on the web does not mean you should put data on the web. And there's a difference between a record being "public" and "in front of a large audience."

So before you write the first line of code, ask these questions:

- This data is public, but is it widely available? And does making it widely available and easy to use change anything?
- Should this data be searchable in a search engine?
- Does this data expose information someone has a reasonable expectation that it would remain at least semi-private?
- Does this data change over time?
- Does this data expire?
- What is my strategy to update or delete data?
- How easy should it be to share this data on social media?
- How should I deal with other people who want this data? API? Bulk download?

Your answers to these questions will guide how you build your app. And hopefully, it'll guide you to better decisions about how to build an app with ethics in mind.

`<!--chapter:end:26-ethics.Rmd-->`{=html}


#  Using GitHub {number="30"}

GitHub is a platform for managing and storing files, data and code built atop Git, a popular open source version control software. GitHub accounts are free and it's [easy to get started](https://docs.github.com/en/get-started/quickstart). The one prerequisite is that you have [Git installed on your local computer](https://docs.github.com/en/get-started/quickstart/set-up-git). There are installers for Mac, Windows and Linux.

## 30.1 How It Works {number="30.1"}

Version control is based on the ideas that you want to keep track of changes you make to a collection of files and that multiple people can work together without getting in each other's way or having to do things in a set order. For individual users, it's great for making sure that you always have your work.

GitHub users work in what are known as repositories on their local computers and also *push* changes to a remote repository located on GitHub. That remote repository is key: if you lose your computer, you can fetch a version of your files from GitHub. If you want to work with someone else on the same files, you can each have a local copy, push changes to GitHub and then pull each others' changes back to your local computers.

So, like Microsoft Word's track changes but with a remote backup and multiple editors.

## 30.2 Getting Started {number="30.2"}

After installing Git and signing up for a GitHub account, [download and install GitHub Desktop](https://docs.github.com/en/desktop/installing-and-configuring-github-desktop). It will have you sign into your GitHub account and then you'll have access to any existing repositories. If you don't have any, that's fine! You can [make one locally](https://docs.github.com/en/desktop/installing-and-configuring-github-desktop/overview/creating-your-first-repository-using-github-desktop).

GitHub has [good documentation for working in the Desktop app](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop), and while the emphasis in this book will be on using GitHub for version control, it also supports recording issues (read: problems or questions) with your files, contributing to projects that aren't yours and more.

## 30.3 Advanced Use {number="30.3"}

Although our focus is on the GitHub Desktop app, you can use Git and GitHub from your computer's command line interface, and GitHub has a purpose-built [command line client](https://docs.github.com/en/github-cli), too. GitHub can also serve as a publishing platform for many types of files, and entire websites are hosted on [GitHub Pages](https://docs.github.com/en/pages).

`<!--chapter:end:27-github.Rmd-->`{=html}
