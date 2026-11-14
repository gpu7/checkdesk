# Step 8: Fairbanks, AK (2026-11-14, America/Denver)

**Rows:** 1 (one Post Office). Third city of the approved Alaska batch (Anchorage, Juneau, Fairbanks, Wasilla, Sitka; one city at a time). Fairbanks is an incorporated city inside Fairbanks North Star Borough (Census "Fairbanks city", GEOID 0224230; county-equivalent Fairbanks North Star Borough, GEOID 02090), not a consolidated city-borough. Only addresses inside Fairbanks city whose official printed city is Fairbanks are listed. Offices printed Fairbanks whose address or official map point falls outside the city are held. Offices printed with other place names are left off, or held if they geocode inside the city. No businesses were contacted. Brands in scope for non-Colorado states: USPS and Walmart Supercenters only. This PR is USPS only; Walmart rows are omitted because the official walmart.com store locator was unavailable.

**Counts:** 1 location; 1 money order; 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 1 Open evenings (Downtown Station, weekday close 17:30), 0 Open weekends. The money-orders page lists 1. The evenings/weekends page lists 1 (1 Open evenings, 0 Open weekends). No check-cashing or bill-pay page (zero listings). Holds: 3 Post Offices (Fairbanks Main Office, College, Fort Wainwright), none listed.

Hours are copied as published and are local Fairbanks time (Alaska Time). `last_verified` is 2026-11-14 on every row. `verification_status` is `verified_official_locator` on every row.

## Method

- **USPS:** official USPS Location Finder API (`tools.usps.com`, `requestType` po), queried with curl the same way as Anchorage and Juneau. Pass 1: 5 and 15 miles around every Fairbanks ZIP (15 USPS-city codes listed for Fairbanks, AK by ZIP-Codes.com from USPS data last updated 2026-11-01) and nearby official ZIPs for Fort Wainwright, Ester, Clear, Anderson, Nenana, Healy, Cantwell, Delta Junction, Fort Greely, Tok, Manley Hot Springs, Minto, Central, and Circle (58 queries, 20 unique records). Pass 2: 1, 2, 3, 10, and 20 miles around 25 Fairbanks/edge ZIPs (added 0). One-off follow-ups added Central 1357498 (50 miles around 99730) and Tanacross 1439449 plus Tok 1384764 (found via 99776; 5- to 50-mile queries around 99780 returned only Northway). Total 23 records (`step8-browser/fairbanks-usps-locator-2026-11-14.jsonl`). Official location pages were fetched for all 23 records (all HTTP 200 on the first try); each page's embedded `poDetail` matched the API record. Retail hours means the BUSINESS block only. Full notes: `step8-browser/fairbanks-usps-2026-11-14.md`.
- **Walmart:** not collected. The official walmart.com store locator was unavailable, so no Walmart rows are in this PR.
- **City limits:** U.S. Census Bureau Geocoder, address endpoint and coordinates endpoint, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, Incorporated Places + CDPs + Counties. All 23 addresses and all 23 official locator map points on both benchmarks (`step8-browser/fairbanks-usps-geocoder-2026-11-14.jsonl`). OpenStreetMap was not used.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands. Coordinates for USPS rows are in the notes column (lat/lng columns stay blank, as in every city CSV).

## USPS (1 listed, Domestic and Inquiry Money Orders)

| Office | Address | Phone | Retail hours (Alaska Time) | Labels | Geocoder |
|---|---|---|---|---|---|
| Downtown Station (1361212) | 315 Barnette St 99701 | 907-452-3223 | Mon-Fri 09:30-17:30 | Open evenings | Address (both files) and point (64.842568, -147.723458): Fairbanks city |

The printed city is Fairbanks, which is treated as agreeing with the Census place name "Fairbanks city."

### Held for Richard (not listed)

1. **Fairbanks Main Office (1439417)**, 5400 Mail Trail Rd, printed **Fairbanks**, AK 99709, 907-455-5444. Money orders; Mon-Fri 09:30-18:00, Sat/Sun closed. Address and official map point (64.815682, -147.881225) are in College CDP (GEOID 0216750), Fairbanks North Star Borough, on both benchmarks — outside Fairbanks city.
2. **College Post Office (1439388)**, 755 Fairbanks St, printed **Fairbanks**, AK 99709, 907-479-6021. Money orders; Mon-Fri 10:00-17:30, Sat 11:00-15:00. Official locator name is College. Address and official map point (64.848484, -147.828121) are in College CDP on both benchmarks — outside Fairbanks city.
3. **Fort Wainwright Post Office (1439402)**, 3726 Neely Rd, printed **Fort Wainwright**, AK 99703, 907-356-7602. Money orders; Mon-Fri 10:30-13:00/14:00-16:30, Sat/Sun closed. Address and official map point (64.827373, -147.642119) are in Fairbanks city on both benchmarks. Printed city and geocode disagree.

### Left off (not holds)

- Other-city offices whose printed city and geocode agree outside Fairbanks city: North Pole city, Eielson AFB CDP, Ester CDP, Salcha CDP, Nenana city, Anderson city, Clear (prints Clear; geocodes Anderson city), Healy CDP, Denali Park CDP, Cantwell CDP, Delta Junction city (address file matches a no-place point in Southeast Fairbanks Census Area away from the official map point, which is in Delta Junction city), Manley Hot Springs CDP (no money-order tags), Minto CDP, Rampart CDP, Circle CDP, Central CDP, Tok CDP, Tanacross CDP, and Northway CDP. Details in `fairbanks-usps-2026-11-14.md`.

## Walmart Supercenters

Not collected in this PR. The official walmart.com store locator was unavailable. No Walmart rows, no Walmart fee citations, and no Neighborhood Markets.

## Site changes in this PR

- New `data/locations/fairbanks.csv` and `/fairbanks/`, `/fairbanks/money-orders/`, `/fairbanks/after-hours/` pages.
- Fairbanks added under Alaska on the home "Start here" list and on `/cities/`, after Juneau. Home and `/cities/` meta descriptions now say "Anchorage, Juneau, and Fairbanks, Alaska". No other city CSV or page changed. Colorado order is unchanged.

## Not changed

- Anchorage, Juneau, Huntsville, Mobile, and every Colorado city. Wasilla and Sitka were not started. No Walmart rows were added.

## Not collected

- Walmart Supercenters: deferred until the official locator is available.
- Payday / title-loan storefronts, including ACE: omitted by policy.
- Stand-alone Western Union / MoneyGram agents, other grocery chains, and USPS contract postal units were not collected.
