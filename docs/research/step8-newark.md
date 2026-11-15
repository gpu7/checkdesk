# Newark, DE USPS research (2026-11-15)

America/Denver (MST). Step 8, third Delaware city, Post Offices only. Hours are Eastern Time. Census place: Newark city, GEOID 1050670, New Castle County (10003), POPESTIMATE2025 30,359 (Vintage 2025, SUMLEV 162). This is Newark, Delaware, not Newark, New Jersey or Newark, Maryland. OpenStreetMap was not used.

## Official ZIPs

ZIP-Codes.com city page `de-newark.asp` title: “Newark, DE ZIP Codes, Map and Demographics,” Data Last Updated November 1, 2026. search.asp title: “10 ZIP Codes in Newark, DE.” City page and search have the same ten unique codes.

| ZIP | Type | Listed city (search.asp) | County | City-page aliases |
|-----|------|--------------------------|--------|-------------------|
| 19702 | Standard | Newark | New Castle | Christiana |
| 19711 | Standard | Newark | New Castle | |
| 19712 | Unique | Newark | New Castle | Shared Firm Zip |
| 19713 | Standard | Newark | New Castle | |
| 19714 | P.O. Box | Newark | New Castle | |
| 19715 | P.O. Box | Newark | New Castle | |
| 19716 | Standard | Newark | New Castle | |
| 19717 | Standard | Newark | New Castle | |
| 19718 | Unique | Newark | New Castle | Christiana Medical Center |
| 19725 | Unique | Newark | New Castle | Shared Firm Zip |

Official printed-Newark ZIPs: 19702, 19711–19718, and 19725 (5 Standard, 2 P.O. Box, 3 Unique). All ten are listed Newark in New Castle County.

## Nearby collection and slug collisions

Pass 1 used prefixes 197 (Newark / southern New Castle), 198 (Wilmington), 193 (southern Chester County, PA), and 219 (Cecil County, MD). Nearby city pages were fetched from ZIP-Codes.com, with search.asp used on slug collisions.

Collisions (search.asp fallback used):

- Christiana, DE slug collided with the Newark city page; search.asp title “2 ZIP Codes in Christiana, DE” (19702 and 19718), both official Newark ZIPs with Christiana aliases.
- Elsmere, Newport, Greenville, Marshallton, and Stanton slugs collided with the Wilmington city page; search.asp used.
- Brookside, Glasgow, North Star, Pike Creek, Pike Creek Valley, and St. Georges have no ZIP-Codes.com city pages (404 / “0 ZIP Codes”).

The Newark, MD city page (`md-newark.asp`, ZIP 21841) is a different place on Maryland’s lower Eastern Shore and was not treated as an official Delaware Newark ZIP. It was not in the pass 1 inventory.

Pass 1 ZIP inventory: 63 unique codes (198: 25, 197: 20, 193: 9, 219: 9).

## Locator sweeps

Official USPS locator API, `requestType=po`.

- Pass 1: 63 ZIPs at 5 and 15 miles, 126 queries, 161 unique records, 0 fails, 2 printed Newark (both Delaware).
- Pass 2: the same 63 official and edge ZIPs at 1, 2, 3, 10, and 20 miles, 315 queries, 0 fails, +86 far records, still 2 printed Newark, 247 unique.

Locator dump: `docs/research/step8-browser/newark-usps-locator-2026-11-15.jsonl`.

The only records whose official printed city is Newark are Federal Post Office (1363269), 110 E Main St, 19711, 302-368-3833, and Newark Post Office (1374919), 401 Ogletown Rd, 19711, 302-737-5771. Both print Newark, DE. No printed-Newark, Maryland office appeared. The Newark Carrier Annex (1433199), 125 Rickey Blvd, 19701, 302-838-5027, prints Bear, not Newark.

## Official pages

All 247 official USPS location pages returned HTTP 200. Two far Maryland pages (Perry Point 1377261 and Worton 1388325) needed a single retry after an initial curl timeout (HTTP 000); both retries were HTTP 200. Embedded `poDetail` matched the locator API on address, phone, and BUSINESS hours for all 247 (`match_api` on all).

Federal (1363269) BUSINESS hours, Eastern Time: Mon–Fri 09:00–16:00; Sat 08:00–12:00; Sun closed. Tags: MONEYORDERSDOM and MONEYORDERSINQ. No Open evenings (16:00 close). Open weekends (Saturday).

Newark (1374919) BUSINESS hours, Eastern Time: Mon–Fri 07:30–18:00; Sat 08:00–13:00; Sun closed. Tags: MONEYORDERSDOM and MONEYORDERSINQ. Open evenings (weekday close 18:00). Open weekends (Saturday).

The Newark Carrier Annex official page has no BUSINESS block and no money-order tags.

## Geocoder

U.S. Census Bureau Geocoder, address and coordinates endpoints, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, layers Incorporated Places + CDPs + Counties. Classification uses only Newark city GEOID 1050670. Dump: `docs/research/step8-browser/newark-usps-geocoder-2026-11-15.jsonl`. 247 records, 0 errors. OpenStreetMap was not used.

Only two records have any leg in Newark city, and both print Newark:

1. **1363269 Federal, 110 E Main St, printed Newark.** Current address file: matched `110 E MAIN ST, NEWARK, DE, 19711`, Newark city GEOID 1050670 / New Castle County 10003. 2020 address file: same match, still in Newark city. Official map point (39.683651, -75.7486249) is in Newark city on both the current and 2020 benchmarks.

2. **1374919 Newark, 401 Ogletown Rd, printed Newark.** Current address file: matched `401 OGLETOWN RD, NEWARK, DE, 19711`, Newark city GEOID 1050670 / New Castle County 10003. 2020 address file: same match, still in Newark city. Official map point (39.683983, -75.7355769) is in Newark city on both the current and 2020 benchmarks.

The Newark Carrier Annex (1433199, printed Bear) is not in Newark city: the current address file matched `125 RICKY BLVD, BEAR, DE, 19701` in Glasgow CDP GEOID 1029350 / New Castle County 10003 (the official street is Rickey Blvd); the 2020 address file did not match; both official map points are in Glasgow CDP. It is not a hold.

No other printed city has a geocode leg inside Newark city. No printed-Newark office sits outside the city. No map-point fallbacks were used.

## Classification

- Listed: 2 (Federal Post Office 1363269 and Newark Post Office 1374919). Money orders: 2. Open evenings: 1 (Newark Post Office, weekday close 18:00; Monday–Friday open 07:30). Open weekends: 2 (Federal Saturday 08:00–12:00; Newark Saturday 08:00–13:00; both Sunday closed).
- Holds: none.
- In-city, not listed: none.
- Map-point fallbacks: none.
- Nearby Post Offices that print Bear, Wilmington, New Castle, Elkton, Hockessin, Middletown, and others geocode outside Newark city and are not holds.

## Raw files

`/workspace/step8nwk/` (official ZIP pages, nearby city/search HTML, locator JSON, official USPS pages, geocoder dump).
