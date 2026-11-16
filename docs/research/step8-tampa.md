# Tampa, FL USPS research (2026-11-15)

America/Denver (MST). Step 8, third Florida city, Post Offices only. Hours are Eastern Time. Census place: Tampa city, GEOID 1271000, POPESTIMATE2025 413,554 (Vintage 2025, SUMLEV 162), inside Hillsborough County (GEOID 12057). This is Tampa, Florida, not a Tampa in another state. Temple Terrace is a separate incorporated city and is not listed here. OpenStreetMap was not used.

## Official ZIPs

ZIP-Codes.com city page `fl-tampa.asp` title: “Tampa, FL ZIP Codes, Map and Demographics,” Data Last Updated November 1, 2026. The page lists 55 unique codes. search.asp title: “55 ZIP Codes in Tampa, FL,” paginated (pages 1–2 fetched, 55 unique codes). The city-page and search lists match exactly.

Official printed-Tampa ZIPs are the **55** codes search lists as Tampa, all in Hillsborough (26 Standard, 23 P.O. Box, 6 Unique). No other-city ZIPs appear on the Tampa search or city page.

The Temple Terrace city-page slug collided with Tampa; search.asp title is “2 ZIP Codes in Temple Terrace, FL,” and those codes were treated as edge ZIPs, not official printed-Tampa ZIPs. Saint Petersburg was used for the Pinellas edge; search.asp “St. Petersburg” returned 0 ZIP Codes, and the Saint Petersburg search (“30 ZIP Codes in Saint Petersburg, FL”) was used instead.

## Locator sweeps

Official USPS locator API, `requestType=po`.

- Pass 1: 185 ZIPs (prefixes 336: 55, 335: 45, 337: 59, 346: 26), including all 55 official printed-Tampa ZIPs and official or edge ZIPs from nearby city searches, at 5 and 15 miles, 370 queries, 108 unique records, 0 fails, 19 printed Tampa (Florida).
- Pass 2: the same 185 official and edge ZIPs at 1, 2, 3, 10, and 20 miles, 925 queries, 0 fails, +16 far records, still 19 printed Tampa, 124 unique.

Locator dump: `docs/research/step8-browser/tampa-usps-locator-2026-11-15.jsonl`.

No printed-Tampa office from another state appeared.

## Official pages

All 124 official USPS location pages returned HTTP 200. Embedded `poDetail` matched the locator API on address, phone, and BUSINESS hours for all 124 (`match_api` on all).

## Geocoder

U.S. Census Bureau Geocoder, address and coordinates endpoints, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, layers Incorporated Places + CDPs + Counties. Classification uses only the SUMLEV 162 Tampa city GEOID 1271000, not Hillsborough County as a whole and not a CDP. Dump: `docs/research/step8-browser/tampa-usps-geocoder-2026-11-15.jsonl`. 124 records, 0 errors. OpenStreetMap was not used.

Twelve records have any leg in Tampa city, and all 12 print Tampa. The other seven printed-Tampa records have no leg in Tampa city.

### Map-point fallbacks (1)

**1438877 Tampa, 3501 Bessie Coleman Blvd Fl 3, printed Tampa.** Current and 2020 address files: no match after street-name, city, and ZIP retries (BESSIE COLEMAN BLVD, BOULEVARD, RD, ROAD, with and without FL 3 / FLOOR 3 / 3RD FLOOR; cities TAMPA and TAMPA INTERNATIONAL AIRPORT; ZIPs 33630, 33607, 33609, 33621, and empty ZIP). No retry snapped to a different street. Official map point (27.967803, -82.537581) is in Tampa city on both benchmarks. Listed (money-order tags and BUSINESS hours).

## Classification

- Listed: 11, all with money-order tags (DOM+INQ) and a BUSINESS hours block. Money orders: 11. Open evenings: 6 (Commerce, New Tampa, and West Tampa until 17:30; Hilldale and Peninsula Tampa until 18:00; Tampa until 22:00). Open weekends: 9 (Saturday hours; the Tampa Post Office also publishes Sunday 10:00–20:00). MacDill AFB is not labeled Open evenings or Open weekends. Commerce is evenings only (no weekend hours).
- Holds: 7, all print Tampa, with no geocode leg in Tampa city. All seven sit in a census-designated place: Carrollwood and Northdale Carrier Annex (Carrollwood CDP), Ehrlich (Northdale CDP), Falkenburg and Palm River Carrier Annex (Brandon CDP), Forest Hills (Lake Magdalene CDP), and Town N Country (Town 'n' Country CDP). CDPs stay off the list.
- In-city, not listed: 1. Tampa Carrier Annex (1384269, 4009 W Spruce St) prints Tampa and geocodes in Tampa city, but its official page does not list money orders and has no BUSINESS block.
- Map-point fallbacks used to list an office: 1 (Tampa Post Office at Bessie Coleman Blvd).
- No other printed city has a geocode leg inside Tampa city. Offices that print Temple Terrace, Plant City, Brandon, and other nearby cities geocode outside Tampa city and are not holds for Tampa.

## Raw files

`/workspace/step8tpa/` (official ZIP pages, nearby city/search HTML, locator JSON, official USPS pages, geocoder dump).
