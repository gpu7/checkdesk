# Illinois: five largest incorporated places (Census Vintage 2025)

Prepared 2026-11-16 (America/Denver). Same file and method as Alabama, Alaska, Arizona, Arkansas, California, Connecticut, Delaware, Florida, Georgia, Hawaii (CDP exception was one-time only), and Idaho. Standing instruction is to research and ship these five, largest first, one PR each, Post Offices only. Illinois uses incorporated places (SUMLEV 162) and excludes CDPs. Hours on the city pages are Central Time for all five (see Time zones below). Grouping is alphabetical: Illinois after Idaho. Do not start Indiana from this run.

## Source

**U.S. Census Bureau, Population Division, Vintage 2025 Population Estimates Program (PEP).**

- **Table:** *Annual Estimates of the Resident Population for Incorporated Places in Illinois: April 1, 2020 to July 1, 2025* (**SUB-IP-EST2025-POP-17**)
- **Figure used for ranking:** July 1, 2025 resident population estimate (`POPESTIMATE2025`)
- **Universe:** Incorporated places only. Census summary level **SUMLEV = 162**. The machine-readable state file has **1,294** such places, matching the official Excel table (1,294 place rows, populations identical). Census-designated places (CDPs) are not in this file and are excluded.
- **Geographic boundaries:** January 1, 2025
- **Release Date:** May 2026 (printed in the Excel table)
- **Official Excel table:** https://www2.census.gov/programs-surveys/popest/tables/2020-2025/cities/totals/SUB-IP-EST2025-POP-17.xlsx
- **Machine-readable state file (same vintage and figures):** https://www2.census.gov/programs-surveys/popest/datasets/2020-2025/cities/totals/sub-est2025_17.csv
- **Dataset landing page:** https://www.census.gov/data/datasets/time-series/demo/popest/2020s-total-cities-and-towns.html
- **File layout (defines SUMLEV 162 = incorporated place):** https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2020-2025/SUB-EST2025.pdf

**Suggested Citation:** U.S. Census Bureau, Population Division, “Annual Estimates of the Resident Population for Incorporated Places in Illinois: April 1, 2020 to July 1, 2025 (SUB-IP-EST2025-POP-17),” Release Date: May 2026.

July 1, 2025 totals in the Excel table were cross-checked against the CSV for every place in the ranking below, and for all 1,294 SUMLEV 162 rows and all seven estimate columns (`ESTIMATESBASE2020` through `POPESTIMATE2025`); they match (1,294 of 1,294). The CSV is UTF-8 (no encoding quirk in this state file). Local copies: `/tmp/il-census/sub-est2025_17.csv`, `/tmp/il-census/SUB-IP-EST2025-POP-17.xlsx`, and `/workspace/step8il/`.

The state total (SUMLEV 040) in the same CSV is **12,719,141**. Illinois has 102 counties (SUMLEV 050), all FUNCSTAT A.

## Five largest incorporated places (SUMLEV 162, POPESTIMATE2025)

| Illinois rank | Place (Census NAME) | July 1, 2025 population | PLACE FIPS | Notes |
|---:|---|---:|---|---|
| 1 | Chicago city | 2,731,585 | 14000 | Incorporated city in Cook County, with a DuPage County part of 0. Cook County total 5,194,625 (GEOID 17031; FUNCSTAT A). DuPage County total 934,298 (GEOID 17043; FUNCSTAT A). Two SUMLEV 157 county parts: Cook 2,731,585 and DuPage 0, which sum to the SUMLEV 162 place total. Census place GEOID 1714000. City-limits checks use that whole-place GEOID only, not a county part. This is the City of Chicago, not Chicago Heights, West Chicago, North Chicago, or East Chicago, Indiana. Nearby Cook municipalities (including Cicero, Evanston, Skokie, Oak Park, Berwyn, and the Norridge and Harwood Heights enclaves) are separate SUMLEV 162 places and must not be folded into a Chicago list. Check Desk pages use the name Chicago. Hours are Central Time. |
| 2 | Aurora city | 181,505 | 03012 | Incorporated city in four counties: Kane 110,937, DuPage 52,191, Will 11,876, and Kendall 6,501, which sum to the SUMLEV 162 place total. County totals: Kane 525,757 (GEOID 17089), DuPage 934,298 (GEOID 17043), Will 712,253 (GEOID 17197), Kendall 145,470 (GEOID 17093); all FUNCSTAT A. Census place GEOID 1703012. City-limits checks use that whole-place GEOID only. This is Aurora, Illinois, not Aurora, Colorado (already live at `/aurora/`). Check Desk uses the slug `/aurora-il/` (and `aurora-il.csv`), following the collision rule in PLAN.md and docs. North Aurora is a separate village and must not be folded in, nor may Elgin, Batavia, Montgomery, Oswego, Naperville, or Joliet. Naperville and Joliet are shipped third and fourth on their own pages. Check Desk pages use the name Aurora, Illinois, in page text so the Colorado city is not confused. Hours are Central Time. |
| 3 | Naperville city | 153,114 | 51622 | Incorporated city in two counties: DuPage 100,678 and Will 52,436, which sum to the SUMLEV 162 place total. County totals: DuPage 934,298 (GEOID 17043) and Will 712,253 (GEOID 17197); both FUNCSTAT A. Census place GEOID 1751622. City-limits checks use that whole-place GEOID only. Nearby municipalities (Aurora, Wheaton, Lisle, Warrenville, Woodridge, Bolingbrook, and Plainfield) are separate SUMLEV 162 places and must not be folded into a Naperville list. Aurora is shipped second on its own page. Check Desk pages use the name Naperville. Hours are Central Time. |
| 4 | Joliet city | 152,241 | 38570 | Incorporated city in two counties: Will 137,691 and Kendall 14,550, which sum to the SUMLEV 162 place total. County totals: Will 712,253 (GEOID 17197) and Kendall 145,470 (GEOID 17093); both FUNCSTAT A. Census place GEOID 1738570. City-limits checks use that whole-place GEOID only. Nearby municipalities (Bolingbrook, Plainfield, Romeoville, New Lenox, Lockport, Crest Hill, Shorewood, and the Will County part of Aurora and of Naperville) are separate SUMLEV 162 places and must not be folded into a Joliet list. Aurora and Naperville are shipped on their own pages. Check Desk pages use the name Joliet. Hours are Central Time. |
| 5 | Rockford city | 147,384 | 65000 | Incorporated city in Winnebago County, with an Ogle County part of 0. Winnebago County total 283,674 (GEOID 17201; FUNCSTAT A). Ogle County total 51,399 (GEOID 17141; FUNCSTAT A). Two SUMLEV 157 county parts: Winnebago 147,384 and Ogle 0, which sum to the SUMLEV 162 place total. Census place GEOID 1765000. City-limits checks use that whole-place GEOID only. This is Rockford, Illinois, in Winnebago County, not Rock Falls, Rock Island, or a Rockford in another state. Nearby Winnebago municipalities (Machesney Park, Loves Park, Roscoe, South Beloit, and Rockton) are separate SUMLEV 162 places and must not be folded into a Rockford list. Check Desk pages use the name Rockford. Hours are Central Time. |

Just outside this five: Elgin city 115,476; Springfield city 112,989; Peoria city 110,920. The gap from Rockford city to Elgin city is **31,908**. Elgin is a two-county place (Kane 90,821 plus Cook 24,655). None of those three is in this run.

## Quirks

Illinois has no FUNCSTAT C counties in this file and no SUMLEV 170 or 172 consolidated-government rows. None of the five is a consolidated city-county. Cook County (5,194,625) is much larger than Chicago and is a separate county government. Every SUMLEV 162 row in this state file has COUNTY = 000 (one whole-place total) and FUNCSTAT A. SUMLEV 157 rows are the county parts and were not used for ranking, except to confirm county composition and to document nearby municipalities that must stay out of each list.

The only FUNCSTAT C row in the file is Cicero township (SUMLEV 061, COUSUB 14364, population 81,858), a county subdivision coextensive with Cicero town. It is not a consolidated city-county and is not in this five.

**Whole place, not county parts.** Ranking uses the SUMLEV 162 whole-place total for every Illinois place. All five of the ranking cities span two or more counties, though Chicago’s DuPage part and Rockford’s Ogle part are 0. City-limits checks for the five use only each city’s own GEOID (1714000, 1703012, 1751622, 1738570, 1765000).

**CDPs are excluded.** This SUB-IP / sub-est file is incorporated places only; no CDP names appear. Nearby CDPs must not be folded into a city list, consistent with earlier states. The Hawaii CDP exception does not apply here.

**Legal types.** Of 1,294 SUMLEV 162 rows, 300 are cities, 978 are villages, and 16 are towns (the NAME of each ends in “ city”, “ village”, or “ town”). FUNCSTAT is A on all 1,294 incorporated-place rows. All five of the ranking are incorporated cities.

**Aurora slug collision.** Aurora, Colorado is already live at `/aurora/` (and `aurora.csv`). Check Desk’s documented rule (PLAN.md and the content plan) is to keep `/aurora/` for Colorado and disambiguate the later city with a state suffix: `/aurora-il/` and `data/locations/aurora-il.csv`. Page text should say Aurora, Illinois, so the two are not confused. North Aurora village (Kane County, 19,406) is a different place.

**Chicago name collisions and enclaves.** Chicago Heights, West Chicago, North Chicago, and East Chicago, Indiana, are different incorporated places and must not be folded into Chicago. Norridge village and Harwood Heights village are enclaves surrounded by Chicago and are separate SUMLEV 162 places; their offices stay off the Chicago list unless a geocode puts a Chicago-printed office inside Chicago city (in which case the usual printed-city versus geocode rules apply). O’Hare is inside Chicago city; nearby Rosemont, Schiller Park, and Des Plaines are not.

**Nearby municipalities that must not be folded in.** Cook County also contains Cicero (81,858), Evanston (76,380), Skokie (66,544), Oak Park (52,823), Berwyn (55,001), Des Plaines, Oak Lawn, and more than 100 other municipalities, plus the Norridge and Harwood Heights enclaves. DuPage County also contains Wheaton (54,065), Downers Grove, Elmhurst, Lombard, West Chicago, Warrenville, and Lisle, and county parts of Aurora and Naperville. Kane County also contains Elgin (Kane part 90,821), Carpentersville, St. Charles, Batavia, South Elgin, Geneva, and North Aurora. Will County also contains Bolingbrook, Plainfield, Romeoville, New Lenox, Lockport, Crest Hill, and county parts of Aurora, Naperville, and Joliet. Kendall County also contains Oswego, Yorkville, Plano, and county parts of Aurora and Joliet. Winnebago County also contains Machesney Park (22,805), Loves Park (22,086), Roscoe, South Beloit, and Rockton.

## Time zones

Illinois is entirely in the Central Time zone. Under **49 CFR 71.5**, the Central zone includes the entire State of Illinois. There is no Pacific, Mountain, or Eastern pocket in this state file’s geography. All five cities in this run are therefore labeled **Central Time**.

## Name collisions

Chicago, Aurora, Naperville, Joliet, and Rockford should be treated as the Illinois Census places above (GEOID 17 + PLACE FIPS). Chicago, Illinois, is not Chicago Heights, West Chicago, North Chicago, or East Chicago, Indiana. Aurora, Illinois, is not Aurora, Colorado, and is not North Aurora. Rockford, Illinois, is not Rock Falls, Rock Island, or a Rockford in another state.

Ship order: Chicago, Aurora, Naperville, Joliet, Rockford. Post Offices only. Hours labeled Central Time. Aurora uses the `/aurora-il/` slug.
