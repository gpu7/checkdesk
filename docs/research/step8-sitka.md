# Step 8: Sitka, AK (2026-11-14, America/Denver)

**Rows:** 1 (one Post Office). Fifth and last city of the approved Alaska batch (Anchorage, Juneau, Fairbanks, Wasilla, Sitka; one city at a time). Sitka is a consolidated city-borough (Census "Sitka city and borough", GEOID 0270540; county-equivalent Sitka City and Borough, GEOID 02220). Only addresses inside the city and borough whose official printed city is Sitka are listed. No businesses were contacted. Brands in scope for non-Colorado states: USPS and Walmart Supercenters only. This PR is USPS only; Walmart rows are omitted because the official walmart.com store locator was unavailable.

**Counts:** 1 location; 1 money order; 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 0 Open evenings, 0 Open weekends. The money-orders page lists 1. There is no `/sitka/after-hours/` page. The Sitka Post Office closes at 17:00 on weekdays (a 17:00 close does not count) and is closed on weekends, so it earns neither label. The site generator will not publish an empty locations list, the same rule that keeps cities without check cashing from getting an empty check-cashing page. No check-cashing or bill-pay page (zero listings). Holds: none.

Hours are copied as published and are local Sitka time (Alaska Time). `last_verified` is 2026-11-14 on every row. `verification_status` is `verified_official_locator` on every row.

## Method

- **USPS:** official USPS Location Finder API (`tools.usps.com`, `requestType` po), queried with curl the same way as Juneau, Fairbanks, and Wasilla. Pass 1: 5 and 15 miles around every Sitka ZIP (2 USPS-city codes listed for Sitka, AK by ZIP-Codes.com from USPS data last updated 2026-11-01: 99835 and 99836) and nearby official ZIPs for Juneau, Kake, Petersburg, Wrangell, Craig, Klawock, Hydaburg, Metlakatla, Haines, Skagway, Hoonah, Angoon, Yakutat, and Gustavus (32 queries, 19 unique records). Pass 2: 1, 2, 3, 10, and 20 miles around 9 Sitka/edge ZIPs (added 0). Queries around 99835 returned only the Sitka office at every radius from 1 to 20 miles. Total 19 records (`step8-browser/sitka-usps-locator-2026-11-14.jsonl`). Official location pages were fetched for all 19 records (all HTTP 200 on the first try); each page's embedded `poDetail` matched the API record. Retail hours means the BUSINESS block only. Full notes: `step8-browser/sitka-usps-2026-11-14.md`.
- **Walmart:** not collected. The official walmart.com store locator was unavailable, so no Walmart rows are in this PR.
- **City limits:** U.S. Census Bureau Geocoder, address endpoint and coordinates endpoint, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, Incorporated Places + CDPs + Counties. All 19 addresses and all 19 official locator map points on both benchmarks (`step8-browser/sitka-usps-geocoder-2026-11-14.jsonl`). OpenStreetMap was not used.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands. Coordinates for USPS rows are in the notes column (lat/lng columns stay blank, as in every city CSV).

## USPS (1 listed, Domestic and Inquiry Money Orders)

| Office | Address | Phone | Retail hours (Alaska Time) | Labels | Geocoder |
|---|---|---|---|---|---|
| Sitka Post Office (1381757) | 1207 Sawmill Creek Rd 99835 | 907-747-3381 | Mon-Fri 09:30-17:00 | none | Address (both files) and point (57.049543, -135.311298): Sitka city and borough |

The printed city is Sitka, which is treated as agreeing with the Census place name "Sitka city and borough."

### Held for Richard (not listed)

None.

### Left off (not holds)

- Port Alexander city (prints Port Alexander; not inside Sitka city and borough). Other-city offices: Kake, Petersburg, Wrangell (no money-order tags and an empty official phone, API and page agree), Craig, Klawock, Hydaburg, Metlakatla, the Juneau offices already listed or held on the Juneau pages, Haines, Skagway, Hoonah, Angoon, Yakutat, and Gustavus. Details in `sitka-usps-2026-11-14.md`.

## Walmart Supercenters

Not collected in this PR. The official walmart.com store locator was unavailable. No Walmart rows, no Walmart fee citations, and no Neighborhood Markets.

## Site changes in this PR

- New `data/locations/sitka.csv` and `/sitka/` and `/sitka/money-orders/` pages. No after-hours page, because no checked Sitka location qualifies and the generator will not publish an empty list. The hub, home, and `/cities/` do not link to a Sitka evenings-and-weekends page.
- Sitka added under Alaska on the home "Start here" list and on `/cities/`, after Wasilla. Home and `/cities/` meta descriptions now say "Anchorage, Juneau, Fairbanks, Wasilla, and Sitka, Alaska". No other city CSV or page changed. Colorado order is unchanged.

## Not changed

- Anchorage, Juneau, Fairbanks, Wasilla, Huntsville, Mobile, and every Colorado city. No Walmart rows were added.

## Not collected

- Walmart Supercenters: deferred until the official locator is available.
- Payday / title-loan storefronts, including ACE: omitted by policy.
- Stand-alone Western Union / MoneyGram agents, other grocery chains, and USPS contract postal units were not collected.
