# Step 8: Juneau, AK (2026-11-14, America/Denver)

**Rows:** 3 (all Post Offices). Second city of the approved Alaska batch (Anchorage, Juneau, Fairbanks, Wasilla, Sitka; one city at a time). Juneau is a consolidated city-borough (Census "Juneau city and borough", GEOID 0236400; county-equivalent Juneau City and Borough, GEOID 02110). Only addresses inside the city and borough whose official printed city is Juneau are listed. No businesses were contacted. Brands in scope for non-Colorado states: USPS and Walmart Supercenters only. This PR is USPS only; Walmart rows are omitted because the official walmart.com store locator was unavailable.

**Counts:** 3 locations; 3 money orders (all three Post Offices); 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 2 Open evenings (Mendenhall and Auke Bay), 2 Open weekends (the same two). The money-orders page lists 3. The evenings/weekends page lists 2 (2 Open evenings, 2 Open weekends). Federal Station is on the hub and money-orders page only. No check-cashing or bill-pay page (zero listings). Holds: 1 Post Office (Douglas), none listed.

Hours are copied as published and are local Juneau time (Alaska Time). `last_verified` is 2026-11-14 on every row. `verification_status` is `verified_official_locator` on every row.

## Method

- **USPS:** official USPS Location Finder API (`tools.usps.com`, `requestType` po), queried with curl the same way as Anchorage and the Alabama cities. Pass 1: 5 and 15 miles around every Juneau ZIP (8 USPS-city codes listed for Juneau, AK by ZIP-Codes.com from USPS data last updated 2026-11-01) and nearby official ZIPs for Gustavus, Haines, Hoonah, Angoon, Skagway, Pelican, Tenakee Springs, Elfin Cove, Kake, Petersburg, Sitka, and Yakutat (42 queries, 16 unique records). Pass 2: 1, 2, 3, 10, and 20 miles around 14 Juneau/edge ZIPs (added Pelican 1377100 at 20 miles around 99832). Total 17 records (`step8-browser/juneau-usps-locator-2026-11-14.jsonl`). Official location pages were fetched for all 17 records (all HTTP 200 on the first try); each page's embedded `poDetail` matched the API record. Retail hours means the BUSINESS block only. Full notes: `step8-browser/juneau-usps-2026-11-14.md`.
- **Walmart:** not collected. The official walmart.com store locator was unavailable, so no Walmart rows are in this PR.
- **City limits:** U.S. Census Bureau Geocoder, address endpoint and coordinates endpoint, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, Incorporated Places + CDPs + Counties. All 17 addresses and all 17 official locator map points on both benchmarks (`step8-browser/juneau-usps-geocoder-2026-11-14.jsonl`). OpenStreetMap was not used.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands. Coordinates for USPS rows are in the notes column (lat/lng columns stay blank, as in every city CSV).

## USPS (3 listed, all Domestic and Inquiry Money Orders)

| Office | Address | Phone | Retail hours (Alaska Time) | Labels | Geocoder |
|---|---|---|---|---|---|
| Federal Station (1363268) | 709 W 9th St 99801 | 907-586-7987 | Mon-Fri 09:00-17:00 | none | Address (both files) and point (58.301561, -134.420355): Juneau city and borough |
| Mendenhall (1372690) | 9491 Vintage Blvd 99801 | 907-789-0934 | Mon-Fri 09:00-18:00; Sat 11:00-16:00 | Open evenings, Open weekends | Current address Juneau city and borough; 2020 address no match after street-name retries; point (58.372977, -134.593189) Juneau city and borough on both. Included on the current address and official map point. Printed city is Juneau. |
| Auke Bay (1439374) | 11899 Glacier Hwy 99801 | 907-789-0680 | Mon-Fri 11:00-13:00/14:00-17:30; Sat 12:00-15:00 | Open evenings, Open weekends | Address (both files) and point (58.387245, -134.649189): Juneau city and borough. Official locator name is Auke Bay; official printed city is Juneau. |

The printed city on all three is Juneau, which is treated as agreeing with the Census place name "Juneau city and borough."

### Held for Richard (not listed)

1. **Douglas Post Office (1439392)**, 804 3rd St, printed **Douglas**, AK 99824, 907-364-2445. Money orders; Mon-Fri 13:00-17:30, Sat 13:00-15:00. Address and official map point (58.276233, -134.393534) are in Juneau city and borough on both benchmarks. Printed city and geocode disagree. Douglas is a community inside the city and borough, not a separate incorporated place.

### Left off (not holds)

- No Juneau-printed carrier annex or no-retail record appeared. Other-city offices whose printed city and geocode agree outside Juneau: Gustavus, Haines, Hoonah, Angoon, Skagway, Elfin Cove (Census address file misfires to Cove, TX/UT; official map point is Elfin Cove CDP), Tenakee Springs, Kake, Petersburg, Sitka, Port Alexander, Yakutat, and Pelican. Details in `juneau-usps-2026-11-14.md`.

## Walmart Supercenters

Not collected in this PR. The official walmart.com store locator was unavailable. No Walmart rows, no Walmart fee citations, and no Neighborhood Markets.

## Site changes in this PR

- New `data/locations/juneau.csv` and `/juneau/`, `/juneau/money-orders/`, `/juneau/after-hours/` pages.
- Juneau added under Alaska on the home "Start here" list and on `/cities/`, after Anchorage. Home and `/cities/` meta descriptions now say "Anchorage and Juneau, Alaska". No other city CSV or page changed. Colorado order is unchanged.

## Not changed

- Anchorage, Huntsville, Mobile, and every Colorado city. Fairbanks and the rest of the Alaska batch were not started. No Walmart rows were added.

## Not collected

- Walmart Supercenters: deferred until the official locator is available.
- Payday / title-loan storefronts, including ACE: omitted by policy.
- Stand-alone Western Union / MoneyGram agents, other grocery chains, and USPS contract postal units were not collected.
