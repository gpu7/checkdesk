# Step 8: Wasilla, AK (2026-11-14, America/Denver)

**Rows:** 1 (one Post Office). Fourth city of the approved Alaska batch (Anchorage, Juneau, Fairbanks, Wasilla, Sitka; one city at a time). Wasilla is an incorporated city inside Matanuska-Susitna Borough (Census "Wasilla city", GEOID 0283080; county-equivalent Matanuska-Susitna Borough, GEOID 02170), not a consolidated city-borough. Only addresses inside Wasilla city whose official printed city is Wasilla are listed. Offices printed Wasilla whose address or official map point falls outside the city are held. Offices printed with other place names are left off, or held if they geocode inside the city. No businesses were contacted. Brands in scope for non-Colorado states: USPS and Walmart Supercenters only. This PR is USPS only; Walmart rows are omitted because the official walmart.com store locator was unavailable.

**Counts:** 1 location; 1 money order; 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 1 Open evenings (Wasilla Post Office, weekday close 17:30), 0 Open weekends. The money-orders page lists 1. The evenings/weekends page lists 1 (1 Open evenings, 0 Open weekends). No check-cashing or bill-pay page (zero listings). Holds: 1 Post Office (Wasilla Annex), not listed.

Hours are copied as published and are local Wasilla time (Alaska Time). `last_verified` is 2026-11-14 on every row. `verification_status` is `verified_official_locator` on every row.

## Method

- **USPS:** official USPS Location Finder API (`tools.usps.com`, `requestType` po), queried with curl the same way as Fairbanks, Juneau, and Anchorage. Pass 1: 5 and 15 miles around every Wasilla ZIP (5 USPS-city codes listed for Wasilla, AK by ZIP-Codes.com from USPS data last updated 2026-11-01) and nearby official ZIPs for Palmer, Sutton/Chickaloon, Talkeetna, Trapper Creek, Willow, and Houston (22 queries, 11 unique records). Pass 2: 1, 2, 3, 10, and 20 miles around all 11 of those ZIPs (added 0). Total 11 records (`step8-browser/wasilla-usps-locator-2026-11-14.jsonl`). Official location pages were fetched for all 11 records (all HTTP 200 on the first try); each page's embedded `poDetail` matched the API record. Retail hours means the BUSINESS block only. Full notes: `step8-browser/wasilla-usps-2026-11-14.md`.
- **Walmart:** not collected. The official walmart.com store locator was unavailable, so no Walmart rows are in this PR.
- **City limits:** U.S. Census Bureau Geocoder, address endpoint and coordinates endpoint, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, Incorporated Places + CDPs + Counties. All 11 addresses and all 11 official locator map points on both benchmarks (`step8-browser/wasilla-usps-geocoder-2026-11-14.jsonl`). OpenStreetMap was not used.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands. Coordinates for USPS rows are in the notes column (lat/lng columns stay blank, as in every city CSV).

## USPS (1 listed, Domestic and Inquiry Money Orders)

| Office | Address | Phone | Retail hours (Alaska Time) | Labels | Geocoder |
|---|---|---|---|---|---|
| Wasilla Post Office (1386558) | 401 N Main St 99654 | 907-376-5327 | Mon-Fri 09:00-17:30 | Open evenings | Address (both files) and point (61.583617, -149.440788): Wasilla city |

The printed city is Wasilla, which is treated as agreeing with the Census place name "Wasilla city."

### Held for Richard (not listed)

1. **Wasilla Annex (1386557)**, 626 N Bobby Day Cir, printed **Wasilla**, AK 99654, 907-376-4206. No money-order tags and no BUSINESS hours on the official page or in the API. Address file did not match after street-name retries. Official map point (61.586544, -149.372444) is in South Lakes CDP (GEOID 0272135), Matanuska-Susitna Borough, on both benchmarks — outside Wasilla city.

### Left off (not holds)

- Other-city offices whose printed city and geocode agree outside Wasilla city: Houston city, Palmer city, Willow CDP, Sutton-Alpine CDP, Chickaloon CDP (prints Sutton), Talkeetna CDP, Trapper Creek CDP, Eagle River and Chugiak (Anchorage municipality; already held on the Anchorage pages). No Big Lake or Meadow Lake Post Office appeared. Details in `wasilla-usps-2026-11-14.md`.

## Walmart Supercenters

Not collected in this PR. The official walmart.com store locator was unavailable. No Walmart rows, no Walmart fee citations, and no Neighborhood Markets.

## Site changes in this PR

- New `data/locations/wasilla.csv` and `/wasilla/`, `/wasilla/money-orders/`, `/wasilla/after-hours/` pages.
- Wasilla added under Alaska on the home "Start here" list and on `/cities/`, after Fairbanks. Home and `/cities/` meta descriptions now say "Anchorage, Juneau, Fairbanks, and Wasilla, Alaska". No other city CSV or page changed. Colorado order is unchanged.

## Not changed

- Anchorage, Juneau, Fairbanks, Huntsville, Mobile, and every Colorado city. Sitka was not started in this PR. No Walmart rows were added.

## Not collected

- Walmart Supercenters: deferred until the official locator is available.
- Payday / title-loan storefronts, including ACE: omitted by policy.
- Stand-alone Western Union / MoneyGram agents, other grocery chains, and USPS contract postal units were not collected.
