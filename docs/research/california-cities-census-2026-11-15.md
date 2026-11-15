# California: five largest incorporated places (Census Vintage 2025)

Prepared 2026-11-15 (America/Denver). Same file and method as Alabama, Alaska, Arizona, and Arkansas. Standing instruction is to research and ship these five, largest first, one PR each, Post Offices only.

## Source

**U.S. Census Bureau, Population Division, Vintage 2025 Population Estimates Program (PEP).**

- **Table:** *Annual Estimates of the Resident Population for Incorporated Places in California: April 1, 2020 to July 1, 2025* (**SUB-IP-EST2025-POP-06**)
- **Figure used for ranking:** July 1, 2025 resident population estimate (`POPESTIMATE2025`)
- **Universe:** Incorporated places only. Census summary level **SUMLEV = 162**. The machine-readable state file has **483** such places, matching the official Excel table (483 place rows). Census-designated places (CDPs) are not in this file and are excluded.
- **Geographic boundaries:** January 1, 2025
- **Release Date:** May 2026 (printed in the Excel table)
- **Official Excel table:** https://www2.census.gov/programs-surveys/popest/tables/2020-2025/cities/totals/SUB-IP-EST2025-POP-06.xlsx
- **Machine-readable state file (same vintage and figures):** https://www2.census.gov/programs-surveys/popest/datasets/2020-2025/cities/totals/sub-est2025_6.csv
- **Dataset landing page:** https://www.census.gov/data/datasets/time-series/demo/popest/2020s-total-cities-and-towns.html
- **File layout (defines SUMLEV 162 = incorporated place):** https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2020-2025/SUB-EST2025.pdf

**Suggested citation:** U.S. Census Bureau, Population Division, “Annual Estimates of the Resident Population for Incorporated Places in California: April 1, 2020 to July 1, 2025 (SUB-IP-EST2025-POP-06),” Release Date: May 2026.

July 1, 2025 totals in the Excel table were cross-checked against the CSV for every populated place in the ranking below; they match (483 of 483 Excel place rows; the one name difference is the ñ in La Cañada Flintridge, same population). Local copies: `/tmp/ca-census/sub-est2025_6.csv`, `/tmp/ca-census/SUB-IP-EST2025-POP-06.xlsx`.

The state total (SUMLEV 040) in the same CSV is **39,355,309**.

## Five largest incorporated places (SUMLEV 162, POPESTIMATE2025)

| California rank | Place (Census NAME) | July 1, 2025 population | PLACE FIPS | Notes |
|---:|---|---:|---|---|
| 1 | Los Angeles city | 3,869,089 | 44000 | Incorporated city inside Los Angeles County (county total 9,694,934; GEOID 06037). Not a consolidated city-county. Census place GEOID 0644000. |
| 2 | San Diego city | 1,406,106 | 66000 | Incorporated city inside San Diego County (county total 3,282,248; GEOID 06073) — not consolidated. Census place GEOID 0666000. |
| 3 | San Jose city | 989,814 | 68000 | Incorporated city inside Santa Clara County (county total 1,914,391; GEOID 06085) — not consolidated. Census place GEOID 0668000. |
| 4 | San Francisco city | 826,079 | 67000 | Consolidated city-county. The incorporated place (SUMLEV 162) is treated as the city. It is coextensive with San Francisco County (GEOID 06075): the place total and the county total are the same 826,079, and the county is the only California county in this file with FUNCSTAT C. Census place GEOID 0667000. |
| 5 | Fresno city | 555,549 | 27000 | Incorporated city inside Fresno County (county total 1,035,456; GEOID 06019) — not consolidated. Census place GEOID 0627000. |

Just outside this five: Sacramento city 536,449; Long Beach city 450,469; Oakland city 440,838. The gap from Fresno to Sacramento is **19,100**.

**No near tie at the cutoff.** Los Angeles is well ahead of San Diego. San Francisco is well ahead of Fresno (a gap of 270,530).

## Quirks

- **San Francisco is a consolidated city-county.** The instruction is to treat the incorporated place as the city. This vintage has **no SUMLEV 170 (consolidated city) or 172 (place within a consolidated city) rows**. The SUMLEV 162 row “San Francisco city” and the SUMLEV 050 row “San Francisco County” have the same July 1, 2025 population (826,079). San Francisco County is the only one of California’s 58 counties with FUNCSTAT C (consolidated government with a single set of officials); the other 57 counties are FUNCSTAT A. City-limits checks use the Census place “San Francisco city” (GEOID 0667000), which is coextensive with the county. South San Francisco city is a separate incorporated place (64,941) in San Mateo County and must not be folded into San Francisco.
- **No other top-five place is a consolidated city-county.** Los Angeles, San Diego, San Jose, and Fresno each sit inside a larger county. Los Angeles County’s 9,694,934 residents include Los Angeles city, Long Beach, and many other incorporated places plus unincorporated remainder. Long Beach (450,469) is a separate city in the same county and must not be folded into a Los Angeles list.
- **No multi-county splits in the top five.** Each of the five has a single SUMLEV 157 county part that equals the whole-place total. Every SUMLEV 162 row in this state file has COUNTY = 000 (one whole-place total). SUMLEV 157 rows were not used for ranking, except to confirm county and coextensiveness.
- **All top five are cities, not towns.** Of the 483 SUMLEV 162 rows, 462 are cities and 21 are towns. FUNCSTAT is A on all 483 incorporated-place rows.
- **CDPs are excluded.** This SUB-IP / sub-est file is incorporated places only; no CDP names appear. Those CDPs are out of scope, consistent with earlier states.
- **Los Angeles neighborhood postal cities are not separate Census places in this ranking.** Van Nuys, Hollywood, San Pedro, and similar names that appear as USPS printed cities are neighborhoods or postal designations inside or next to Los Angeles city. They will be classified later by official printed city and Census place, not by this ranking. Only the incorporated place “Los Angeles city” is in the five-city list.
- **Whole place, not county parts.** Ranking uses the SUMLEV 162 whole-place total, consistent with earlier states.

Ship order: Los Angeles, San Diego, San Jose, San Francisco, Fresno. Post Offices only.
