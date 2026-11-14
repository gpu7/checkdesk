# Arizona: five largest incorporated places (Census Vintage 2025)

Research only. No pages, PRs, or deploys. Prepared 2026-11-14 (America/Denver). Same file and method as Alabama and Alaska. This list is for Richard’s confirmation before any Arizona city pages are built.

## Source

**U.S. Census Bureau, Population Division, Vintage 2025 Population Estimates Program (PEP).**

- **Table:** *Annual Estimates of the Resident Population for Incorporated Places in Arizona: April 1, 2020 to July 1, 2025* (**SUB-IP-EST2025-POP-04**)
- **Figure used for ranking:** July 1, 2025 resident population estimate (`POPESTIMATE2025`)
- **Universe:** Incorporated places only. Census summary level **SUMLEV = 162**. The machine-readable state file has **91** such places, matching the official Excel table (91 place rows). Census-designated places (CDPs) are not in this file and are excluded.
- **Geographic boundaries:** January 1, 2025
- **Release Date:** May 2026 (printed in the Excel table)
- **Official Excel table:** https://www2.census.gov/programs-surveys/popest/tables/2020-2025/cities/totals/SUB-IP-EST2025-POP-04.xlsx
- **Machine-readable state file (same vintage and figures):** https://www2.census.gov/programs-surveys/popest/datasets/2020-2025/cities/totals/sub-est2025_4.csv
- **Dataset landing page:** https://www.census.gov/data/datasets/time-series/demo/popest/2020s-total-cities-and-towns.html
- **File layout (defines SUMLEV 162 = incorporated place):** https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2020-2025/SUB-EST2025.pdf

**Suggested citation:** U.S. Census Bureau, Population Division, “Annual Estimates of the Resident Population for Incorporated Places in Arizona: April 1, 2020 to July 1, 2025 (SUB-IP-EST2025-POP-04),” Release Date: May 2026.

July 1, 2025 totals in the Excel table were cross-checked against the CSV for every populated place in the ranking below; they match. Local copies: `/tmp/az-census/sub-est2025_4.csv`, `/tmp/az-census/SUB-IP-EST2025-POP-04.xlsx`.

The state total (SUMLEV 040) in the same CSV is **7,623,818**.

## Five largest incorporated places (SUMLEV 162, POPESTIMATE2025)

| Arizona rank | Place (Census NAME) | July 1, 2025 population | PLACE FIPS | Notes |
|---:|---|---:|---|---|
| 1 | Phoenix city | 1,665,481 | 55000 | Incorporated city inside Maricopa County (county total 4,689,558) — not a consolidated city-county |
| 2 | Tucson city | 548,371 | 77000 | Incorporated city inside Pima County (county total 1,074,685) — not consolidated |
| 3 | Mesa city | 513,656 | 46000 | Incorporated city inside Maricopa County |
| 4 | Gilbert town | 287,285 | 27400 | Incorporated **town** (not a city) inside Maricopa County; still a SUMLEV 162 incorporated place |
| 5 | Chandler city | 278,748 | 12000 | Incorporated city inside Maricopa County |

Just outside this five: Glendale city 260,572; Scottsdale city 243,006.

**Near tie:** Gilbert town (287,285) and Chandler city (278,748) are **8,537** people apart. Gilbert is ahead in this vintage. Phoenix is far ahead of Tucson (a gap of 1,117,110).

## Quirks

- **Gilbert is legally a town, not a city**, but it is an incorporated place and appears as SUMLEV 162 under the Census name “Gilbert town.” It belongs in this ranking. The same is true of other Arizona towns (45 of the 91 SUMLEV 162 rows are towns; 46 are cities). Queen Creek town (89,770) is the next town on the list, well below the top five.
- **No consolidated city-county.** None of the top five is coextensive with its county. Phoenix, Mesa, Gilbert, and Chandler are all inside Maricopa County, whose 4,689,558 residents include many other incorporated places and a large unincorporated remainder (SUMLEV 157 “Balance of Maricopa County” is 330,319). Tucson is inside Pima County the same way. The file layout also defines SUMLEV 170 (consolidated city) and 172 (place within a consolidated city); **this Arizona vintage has no SUMLEV 170 or 172 rows**, the same pattern as Alaska and as Denver and Broomfield in Colorado (those two appear only as SUMLEV 162).
- **CDPs are excluded.** This SUB-IP / sub-est file is incorporated places only; no CDP names appear. That matters in the Phoenix and Pinal areas, where some unincorporated communities are large. Those CDPs are out of scope, consistent with the Alabama/Alaska/Colorado rule.
- **Whole place, not county parts.** Every SUMLEV 162 row in this state file has COUNTY = 000 (one whole-place total). SUMLEV 157 rows are the county parts and the “Balance of …” remainders; they were not used for ranking. None of the top five is split across counties in this vintage. (Some smaller or later-ranked places are, including Peoria city, Apache Junction city, Queen Creek town, and Sedona city.)
- **FUNCSTAT is A** on all 91 incorporated-place rows (active governmental unit).

This list is for Richard’s confirmation before any Arizona city pages are built.
