# Arkansas: five largest incorporated places (Census Vintage 2025)

Research only. No pages, PRs, or deploys. Prepared 2026-11-15 (America/Denver). Same file and method as Alabama, Alaska, and Arizona. This list is for Richard’s confirmation before any Arkansas city pages are built.

## Source

**U.S. Census Bureau, Population Division, Vintage 2025 Population Estimates Program (PEP).**

- **Table:** *Annual Estimates of the Resident Population for Incorporated Places in Arkansas: April 1, 2020 to July 1, 2025* (**SUB-IP-EST2025-POP-05**)
- **Figure used for ranking:** July 1, 2025 resident population estimate (`POPESTIMATE2025`)
- **Universe:** Incorporated places only. Census summary level **SUMLEV = 162**. The machine-readable state file has **501** such places, matching the official Excel table (501 place rows). Census-designated places (CDPs) are not in this file and are excluded.
- **Geographic boundaries:** January 1, 2025
- **Release Date:** May 2026 (printed in the Excel table)
- **Official Excel table:** https://www2.census.gov/programs-surveys/popest/tables/2020-2025/cities/totals/SUB-IP-EST2025-POP-05.xlsx
- **Machine-readable state file (same vintage and figures):** https://www2.census.gov/programs-surveys/popest/datasets/2020-2025/cities/totals/sub-est2025_5.csv
- **Dataset landing page:** https://www.census.gov/data/datasets/time-series/demo/popest/2020s-total-cities-and-towns.html
- **File layout (defines SUMLEV 162 = incorporated place):** https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2020-2025/SUB-EST2025.pdf

**Suggested citation:** U.S. Census Bureau, Population Division, “Annual Estimates of the Resident Population for Incorporated Places in Arkansas: April 1, 2020 to July 1, 2025 (SUB-IP-EST2025-POP-05),” Release Date: May 2026.

July 1, 2025 totals in the Excel table were cross-checked against the CSV for every populated place in the ranking below; they match (501 of 501 Excel place rows). Local copies: `/tmp/ar-census/sub-est2025_5.csv`, `/tmp/ar-census/SUB-IP-EST2025-POP-05.xlsx`.

The state total (SUMLEV 040) in the same CSV is **3,114,791**.

## Five largest incorporated places (SUMLEV 162, POPESTIMATE2025)

| Arkansas rank | Place (Census NAME) | July 1, 2025 population | PLACE FIPS | Notes |
|---:|---|---:|---|---|
| 1 | Little Rock city | 206,427 | 41000 | Incorporated city inside Pulaski County (county total 404,611; GEOID 05119). Not a consolidated city-county. Census place GEOID 0541000. |
| 2 | Fayetteville city | 106,623 | 23290 | Incorporated city inside Washington County (county total 271,213) — not consolidated |
| 3 | Fort Smith city | 90,855 | 24550 | Incorporated city inside Sebastian County (county total 130,641) — not consolidated. In this vintage the whole place is in one Arkansas county. |
| 4 | Springdale city | 90,685 | 66080 | Incorporated city split across two counties: Washington County part 78,235 and Benton County part 12,450. The SUMLEV 162 whole-place total is used for ranking. |
| 5 | Jonesboro city | 83,296 | 35710 | Incorporated city inside Craighead County (county total 116,957) — not consolidated |

Just outside this five: Rogers city 76,956; Conway city 72,328. North Little Rock city, a separate incorporated place in Pulaski County, is 65,120.

**Near tie:** Fort Smith city (90,855) and Springdale city (90,685) are only **170** people apart. Fort Smith is ahead in this vintage. Little Rock is well ahead of Fayetteville (a gap of 99,804).

## Quirks

- **Springdale is split across two counties.** The SUMLEV 162 row is the whole-place total (90,685). The SUMLEV 157 county parts are Springdale city (pt.) in Washington County (78,235) and Springdale city (pt.) in Benton County (12,450). Ranking uses the whole-place total, consistent with earlier states. The other four of the top five each have a single county part in this vintage that equals the whole-place total (Little Rock in Pulaski, Fayetteville in Washington, Fort Smith in Sebastian, Jonesboro in Craighead).
- **North Little Rock is a separate city**, not a neighborhood of Little Rock. It is the eighth-largest incorporated place in the state (65,120) and sits in the same county (Pulaski). It should not be folded into a Little Rock list.
- **No consolidated city-county.** None of the top five is coextensive with its county. Pulaski County’s 404,611 residents include Little Rock, North Little Rock, and other incorporated places plus an unincorporated remainder. The file layout also defines SUMLEV 170 (consolidated city) and 172 (place within a consolidated city); **this Arkansas vintage has no SUMLEV 170 or 172 rows**.
- **All top five are cities, not towns.** Of the 501 SUMLEV 162 rows, 315 are cities and 186 are towns. FUNCSTAT is A (active governmental unit) on all 501 incorporated-place rows.
- **CDPs are excluded.** This SUB-IP / sub-est file is incorporated places only; no CDP names appear. Those CDPs are out of scope, consistent with the Alabama/Alaska/Arizona/Colorado rule.
- **Whole place, not county parts.** Every SUMLEV 162 row in this state file has COUNTY = 000 (one whole-place total). SUMLEV 157 rows are the county parts and were not used for ranking, except to note Springdale’s split and to confirm the other four are single-county.
- **Fort Smith sits on the Arkansas–Oklahoma line**, but the Census place used here is the Arkansas incorporated place only (Sebastian County). Any Oklahoma-side municipality is a different place and a different state.

This list is for Richard’s confirmation before any Arkansas city pages are built.
