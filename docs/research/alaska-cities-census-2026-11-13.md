# Alaska: five largest incorporated places (Census Vintage 2025)

Research only. No pages, PRs, or deploys. Prepared 2026-11-13 (America/Denver). Same file and method as Alabama.

## Source

**U.S. Census Bureau, Population Division, Vintage 2025 Population Estimates Program (PEP).**

- **Table:** *Annual Estimates of the Resident Population for Incorporated Places in Alaska: April 1, 2020 to July 1, 2025* (**SUB-IP-EST2025-POP-02**)
- **Figure used for ranking:** July 1, 2025 resident population estimate (`POPESTIMATE2025`)
- **Universe:** Incorporated places only. Census summary level **SUMLEV = 162**. The machine-readable state file has **149** such places, matching the official Excel table (149 place rows). Census-designated places (CDPs) are not in this file and are excluded.
- **Geographic boundaries:** January 1, 2025
- **Release Date:** May 2026 (printed in the Excel table)
- **Official Excel table:** https://www2.census.gov/programs-surveys/popest/tables/2020-2025/cities/totals/SUB-IP-EST2025-POP-02.xlsx
- **Machine-readable state file (same vintage and figures):** https://www2.census.gov/programs-surveys/popest/datasets/2020-2025/cities/totals/sub-est2025_2.csv
- **Dataset landing page:** https://www.census.gov/data/datasets/time-series/demo/popest/2020s-total-cities-and-towns.html
- **File layout (defines SUMLEV 162 = incorporated place):** https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2020-2025/SUB-EST2025.pdf

**Suggested citation:** U.S. Census Bureau, Population Division, “Annual Estimates of the Resident Population for Incorporated Places in Alaska: April 1, 2020 to July 1, 2025 (SUB-IP-EST2025-POP-02),” Release Date: May 2026.

July 1, 2025 totals in the Excel table were cross-checked against the CSV for every populated place in the ranking below; they match. Local copies: `/workspace/step8anc/sub-est2025_2.csv`, `/workspace/step8anc/SUB-IP-EST2025-POP-02.xlsx`.

## Five largest incorporated places (SUMLEV 162, POPESTIMATE2025)

| Alaska rank | Place (Census NAME) | July 1, 2025 population | PLACE FIPS | Notes |
|---:|---|---:|---|---|
| 1 | Anchorage municipality | 287,155 | 03000 | Consolidated city-borough; coextensive with Anchorage Municipality (SUMLEV 050, FUNCSTAT C, same population) |
| 2 | Juneau city and borough | 31,609 | 36400 | Consolidated city-borough; coextensive with Juneau City and Borough (SUMLEV 050, FUNCSTAT C, same population) |
| 3 | Fairbanks city | 31,468 | 24230 | Incorporated city inside Fairbanks North Star Borough (borough total 93,972) — not consolidated |
| 4 | Wasilla city | 10,556 | 83080 | Incorporated city inside Matanuska-Susitna Borough (borough total 118,666) — not consolidated |
| 5 | Sitka city and borough | 8,319 | 70540 | Consolidated city-borough; coextensive with Sitka City and Borough (SUMLEV 050, FUNCSTAT C, same population) |

Just outside this five: Ketchikan city 7,939; Kenai city 7,924.

**Near tie:** Juneau (31,609) and Fairbanks city (31,468) are only **141** people apart. Juneau is ahead in this vintage.

## Quirks

- **Anchorage, Juneau, and Sitka are consolidated city-boroughs, and they do appear as SUMLEV 162 places** in this file, under the Census names “Anchorage municipality,” “Juneau city and borough,” and “Sitka city and borough.” Their place population equals the coextensive borough (SUMLEV 050) population. The file layout also defines SUMLEV 170 (consolidated city) and 172 (place within a consolidated city); **this Alaska vintage has no SUMLEV 170 or 172 rows**, the same pattern as Colorado (Denver and Broomfield appear only as SUMLEV 162).
- **Wrangell city and borough** (2,007) is a fourth coextensive city-borough that also appears as SUMLEV 162 (place population equals Wrangell City and Borough, SUMLEV 050, FUNCSTAT C). It is well below the top five.
- **Yakutat City and Borough** (672) and **Skagway Municipality** (1,104) appear only as SUMLEV 050 county-equivalents. They have **no SUMLEV 162 incorporated-place row** in this file, so they are not in the incorporated-place ranking.
- **CDPs are excluded.** This SUB-IP / sub-est file is incorporated places only; no CDP names appear. That matters in the Fairbanks and Mat-Su areas: Fairbanks North Star Borough (93,972) and Matanuska-Susitna Borough (118,666) are much larger than Fairbanks city and Wasilla city because most of their population lives in unincorporated communities (for example College and Badger near Fairbanks, and Knik-Fairview and other Mat-Su CDPs). Those CDPs are out of scope, consistent with the Alabama/Colorado rule.
- **Whole place, not county parts.** Every SUMLEV 162 row in this state file has COUNTY = 000 (one whole-place total). SUMLEV 157 rows are the county/borough parts and the “Balance of …” remainders; they were not used for ranking.

This list is for Richard’s confirmation before any Alaska city pages are built.
