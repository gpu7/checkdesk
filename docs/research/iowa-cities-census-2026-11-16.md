# Iowa: five largest incorporated places (Census Vintage 2025)

Prepared 2026-11-16 (America/Denver). Same file and method as Alabama, Alaska, Arizona, Arkansas, California, Connecticut, Delaware, Florida, Georgia, Hawaii (CDP exception was one-time only), Idaho, Illinois, and Indiana. Standing instruction is to research and ship these five, largest first, one PR each, Post Offices only. Iowa uses incorporated places (SUMLEV 162) and excludes CDPs. Hours on the city pages are Central Time for all five (see Time zones below). Grouping is alphabetical: Iowa after Indiana. Do not start Kansas from this run.

## Source

**U.S. Census Bureau, Population Division, Vintage 2025 Population Estimates Program (PEP).**

- **Table:** *Annual Estimates of the Resident Population for Incorporated Places in Iowa: April 1, 2020 to July 1, 2025* (**SUB-IP-EST2025-POP-19**)
- **Figure used for ranking:** July 1, 2025 resident population estimate (`POPESTIMATE2025`)
- **Universe:** Incorporated places only. Census summary level **SUMLEV = 162**. The machine-readable state file has **939** such places, matching the official Excel table (939 place rows, populations identical). Census-designated places (CDPs) are not in this file and are excluded.
- **Geographic boundaries:** January 1, 2025
- **Release Date:** May 2026 (printed in the Excel table)
- **Official Excel table:** https://www2.census.gov/programs-surveys/popest/tables/2020-2025/cities/totals/SUB-IP-EST2025-POP-19.xlsx
- **Machine-readable state file (same vintage and figures):** https://www2.census.gov/programs-surveys/popest/datasets/2020-2025/cities/totals/sub-est2025_19.csv
- **Dataset landing page:** https://www.census.gov/data/datasets/time-series/demo/popest/2020s-total-cities-and-towns.html
- **File layout (defines SUMLEV 162 = incorporated place):** https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2020-2025/SUB-EST2025.pdf

**Suggested Citation:** U.S. Census Bureau, Population Division, “Annual Estimates of the Resident Population for Incorporated Places in Iowa: April 1, 2020 to July 1, 2025 (SUB-IP-EST2025-POP-19),” Release Date: May 2026.

July 1, 2025 totals in the Excel table were cross-checked against the CSV for every place in the ranking below, and for all 939 SUMLEV 162 rows and all seven estimate columns (`ESTIMATESBASE2020` through `POPESTIMATE2025`); they match (939 of 939). The CSV is UTF-8 (no encoding quirk in this state file). Local copies: `/tmp/ia-census/sub-est2025_19.csv`, `/tmp/ia-census/SUB-IP-EST2025-POP-19.xlsx`, and `/workspace/step8ia/`.

The state total (SUMLEV 040) in the same CSV is **3,238,387**. Iowa has 99 counties (SUMLEV 050), all FUNCSTAT A.

## Five largest incorporated places (SUMLEV 162, POPESTIMATE2025)

| Iowa rank | Place (Census NAME) | July 1, 2025 population | PLACE FIPS | Notes |
|---:|---|---:|---|---|
| 1 | Des Moines city | 212,086 | 21000 | Incorporated city in two counties: Polk 211,882 and Warren 204, which sum to the SUMLEV 162 place total. County totals: Polk 516,546 (GEOID 19153) and Warren 57,331 (GEOID 19181); both FUNCSTAT A. Census place GEOID 1921000. City-limits checks use that whole-place GEOID only. This is Des Moines, Iowa, not West Des Moines and not a Des Moines in another state. Nearby municipalities (West Des Moines, Urbandale, Johnston, Altoona, Clive, Grimes, Pleasant Hill, Bondurant, Windsor Heights, Norwalk, Indianola, and Carlisle) are separate SUMLEV 162 places and must not be folded into a Des Moines list. Ankeny is shipped fifth on its own page and must not be folded in either. Check Desk has no existing `/des-moines/` page, so the slug is `/des-moines/`. Check Desk pages use the name Des Moines. Hours are Central Time. |
| 2 | Cedar Rapids city | 137,935 | 12000 | Incorporated city in Linn County. Linn County total 232,028 (GEOID 19113; FUNCSTAT A). One SUMLEV 157 county part: Linn 137,935, which equals the SUMLEV 162 place total. Census place GEOID 1912000. City-limits checks use that whole-place GEOID only. Nearby Linn municipalities (Marion, Hiawatha, Robins, Fairfax, Mount Vernon, Center Point, Ely, Lisbon, and Palo) are separate SUMLEV 162 places and must not be folded into a Cedar Rapids list, nor may Iowa City, Coralville, or North Liberty (Johnson County; Iowa City is just outside this five). Check Desk has no existing `/cedar-rapids/` page, so the slug is `/cedar-rapids/`. Check Desk pages use the name Cedar Rapids. Hours are Central Time. |
| 3 | Davenport city | 100,358 | 19000 | Incorporated city in Scott County. Scott County total 175,259 (GEOID 19163; FUNCSTAT A). One SUMLEV 157 county part: Scott 100,358, which equals the SUMLEV 162 place total. Census place GEOID 1919000. City-limits checks use that whole-place GEOID only. This is Davenport, Iowa, not a Davenport in another state. Nearby Scott municipalities (Bettendorf, Eldridge, Le Claire, Walcott, and Blue Grass) are separate SUMLEV 162 places and must not be folded into a Davenport list, nor may the Illinois Quad Cities (Moline, Rock Island, East Moline, and Silvis), which are outside this state file. Check Desk has no existing `/davenport/` page, so the slug is `/davenport/`. Check Desk pages use the name Davenport. Hours are Central Time. |
| 4 | Sioux City city | 86,356 | 73335 | Incorporated city in two counties: Woodbury 86,354 and Plymouth 2, which sum to the SUMLEV 162 place total. County totals: Woodbury 106,649 (GEOID 19193) and Plymouth 25,697 (GEOID 19149); both FUNCSTAT A. Census place GEOID 1973335. City-limits checks use that whole-place GEOID only. This is Sioux City, Iowa, not South Sioux City, Nebraska, and not North Sioux City, South Dakota. Nearby Iowa municipalities (Sergeant Bluff, Moville, and Le Mars) are separate SUMLEV 162 places and must not be folded into a Sioux City list, nor may the Nebraska or South Dakota places across the rivers. Check Desk has no existing `/sioux-city/` page, so the slug is `/sioux-city/`. Check Desk pages use the name Sioux City. Hours are Central Time. |
| 5 | Ankeny city | 77,833 | 02305 | Incorporated city in Polk County. Polk County total 516,546 (GEOID 19153; FUNCSTAT A). One SUMLEV 157 county part: Polk 77,833, which equals the SUMLEV 162 place total. Census place GEOID 1902305. City-limits checks use that whole-place GEOID only. Nearby Polk municipalities (Des Moines, West Des Moines, Urbandale, Johnston, Altoona, Bondurant, Polk City, and Alleman) are separate SUMLEV 162 places and must not be folded into an Ankeny list. Des Moines is shipped first on its own page. Check Desk has no existing `/ankeny/` page, so the slug is `/ankeny/`. Check Desk pages use the name Ankeny. Hours are Central Time. |

Just outside this five: Iowa City city 76,229; West Des Moines city 74,224; Ames city 68,220. The gap from Ankeny city to Iowa City city is **1,604**. None of those three is in this run.

## Quirks

Iowa has no FUNCSTAT C counties in this file and no SUMLEV 170 or 172 consolidated-government rows. The file’s only summary levels are 040 (state), 050 (county), 157 (place-county part), and 162 (incorporated place). None of the five is a consolidated city-county. Every SUMLEV 162 row in this state file has COUNTY = 000 (one whole-place total) and FUNCSTAT A. SUMLEV 157 rows are the county parts and were not used for ranking, except to confirm county composition and to document nearby municipalities that must stay out of each list.

**Whole place, not county parts.** Ranking uses the SUMLEV 162 whole-place total for every Iowa place. Des Moines and Sioux City each span two counties (Warren’s Des Moines part is 204; Plymouth’s Sioux City part is 2). City-limits checks for the five use only each city’s own GEOID (1921000, 1912000, 1919000, 1973335, 1902305).

**CDPs are excluded.** This SUB-IP / sub-est file is incorporated places only; no CDP names appear. Nearby CDPs must not be folded into a city list, consistent with earlier states. The Hawaii CDP exception does not apply here.

**Legal types.** All 939 SUMLEV 162 rows are cities (the NAME of each ends in “ city”). FUNCSTAT is A on all 939 incorporated-place rows. Iowa does not use village or town as a Census legal type in this file. All five of the ranking are incorporated cities.

**No slug collisions among this five.** Existing Check Desk location slugs were checked on 2026-11-16. None of `/des-moines/`, `/cedar-rapids/`, `/davenport/`, `/sioux-city/`, or `/ankeny/` is in use, so none of this five needs a state-suffix slug. West Des Moines and Iowa City are outside this five and also have no existing pages; they must not reuse a Des Moines or other city’s slug if they are shipped later.

**Name collisions and nearby places that must not be folded in.** Des Moines, Iowa, is not West Des Moines (74,224; four counties, mostly Polk and Dallas) and is not a Des Moines in another state. Polk County also contains Ankeny (shipped fifth), Urbandale (48,570), Johnston (25,065), Altoona (22,796), Clive (Polk part 11,204; whole place 19,861), Grimes, Pleasant Hill (11,239), Bondurant (9,647), and Windsor Heights (5,059). Warren County also contains Indianola (16,829), Norwalk (15,004), and Carlisle, plus a 204-person part of Des Moines. Linn County also contains Marion (42,732), Hiawatha (7,432), Robins (3,366), Fairfax, Mount Vernon, Center Point, Ely, Lisbon, and Palo; Iowa City (76,229), Coralville, and North Liberty are in Johnson County and are a separate metro. Scott County also contains Bettendorf (40,710), Eldridge (6,954), Le Claire (4,741), Walcott, and Blue Grass; the Illinois Quad Cities (Moline, Rock Island, East Moline, Silvis) are outside this state file and must stay off a Davenport list. Woodbury County also contains Sergeant Bluff (5,324) and Moville; Plymouth County also contains Le Mars (10,760) and only 2 people in Sioux City. South Sioux City, Nebraska, and North Sioux City, South Dakota, are different incorporated places in other states.

## Time zones

Iowa is entirely in the Central Time zone. Under **49 CFR 71.6**, the Central zone includes that part of the United States west of the boundary in **49 CFR 71.5** and east of the boundary in **49 CFR 71.7**. Iowa lies entirely between those lines. There is no Pacific, Mountain, or Eastern pocket in this state file’s geography. All five cities in this run are therefore labeled **Central Time**.

## Name collisions

Des Moines, Cedar Rapids, Davenport, Sioux City, and Ankeny should be treated as the Iowa Census places above (GEOID 19 + PLACE FIPS). Des Moines, Iowa, is not West Des Moines and is not a Des Moines in another state. Davenport, Iowa, is not a Davenport in another state and is not Bettendorf or the Illinois Quad Cities. Sioux City, Iowa, is not South Sioux City, Nebraska, and is not North Sioux City, South Dakota.

Ship order: Des Moines, Cedar Rapids, Davenport, Sioux City, Ankeny. Post Offices only. Hours labeled Central Time. None of this five needs a state-suffix slug.
