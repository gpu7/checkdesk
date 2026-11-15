# New Haven, CT USPS research — 2026-11-15 (America/Denver)

Third Connecticut city. Classification used only Census "New Haven city", GEOID 0952000, in the South Central Connecticut Planning Region (GEOID 09170). West Haven, East Haven, Hamden, North Haven, and other nearby municipalities were not folded in. Hours are Eastern Time. Public sources only; no business was contacted.

## Official ZIPs

ZIP-Codes.com city page slug `ct-new-haven` is not a collision (title New Haven, last updated November 1, 2026). search.asp title "32 ZIP Codes in New Haven, CT". The city page and search.asp have the same 32 unique codes, all in South Central CT.

26 of those 32 are listed New Haven (5 Standard, 18 P.O. Box, 3 Unique): 06501, 06502, 06503, 06504, 06505, 06506, 06507, 06508, 06509, 06510, 06511, 06513, 06515, 06519, 06520, 06521, 06530, 06531, 06532, 06533, 06534, 06535, 06536, 06537, 06538, 06540.

The other 6 in the official New Haven search are listed as other cities and are not treated as official New Haven printed-city ZIPs, but they were included in pass 1: East Haven 06512; Hamden 06514, 06517, 06518; Bethany 06524; Woodbridge 06525.

Neighborhood slugs that collided with the New Haven city page (used search.asp fallback): Hamden, Westville, Fair Haven. Seymour's slug collided with Oxford.

## Locator sweeps

Pass 1 used prefixes 065/064 (62 ZIPs), 5 and 15 miles (124 queries). 133 unique records, 0 failures, 6 printed New Haven.

Pass 2 used 1, 2, 3, 10, and 20 mile widenings around 39 official and edge ZIPs: the official 32 plus West Haven 06516, East Haven 06512, Hamden 06514/06517/06518, North Haven 06473, Woodbridge 06525, Orange 06477, Branford 06405, Milford 06460/06461, Bethany 06524, and Wallingford 06492 (195 queries). 0 failures, 14 added records far from New Haven city (Long Island, Westport, Wilton, and similar), still 6 printed New Haven. Total 147 unique records in `new-haven-usps-locator-2026-11-15.jsonl`.

## Official pages

All 147 official pages returned HTTP 200 on the first try. Embedded `poDetail` matched the API record on all 147 (`match_api`).

The 6 records that print New Haven, all with both MONEYORDERSDOM and MONEYORDERSINQ and a BUSINESS retail-hours block:

| locatorID | Official name | Address | ZIP | Phone | Weekday BUSINESS | Saturday |
|-----------|---------------|---------|-----|-------|------------------|----------|
| 1434108 | NEW HAVEN | 50 BREWERY ST | 06511 | 203-782-7011 | 08:00-17:30 | 08:00-13:00 |
| 1434177 | YALE | 206 ELM ST | 06511 | 203-773-3454 | 09:00-17:30 | 08:00-12:00 |
| 1362940 | FAIR HAVEN | 230 GRAND AVE | 06513 | 203-773-3538 | 08:00-17:00 | 08:00-12:00 |
| 1387402 | WESTVILLE | 95 FOUNTAIN ST | 06515 | 203-389-8655 | 08:30-17:00 | 08:30-12:00 |
| 1352985 | AMITY RETAIL STORE | 1449 WHALLEY AVE | 06515 | 203-389-9881 | 08:00-17:00 | 08:00-12:00 |
| 1369007 | KILBY | 369 WASHINGTON AVE | 06519 | 203-782-3717 | 10:00-12:00 | 08:00-12:00 |

Sunday is closed at all six. A 17:00 weekday close does not count as Open evenings; 17:30 does. Kilby's weekday window is 10:00-12:00 only; Saturday hours still earn the Open weekends label.

## Geocoder

U.S. Census Bureau Geocoder, address and coordinates endpoints, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, layers Incorporated Places + CDPs + Counties. OpenStreetMap was not used. Full dump: `new-haven-usps-geocoder-2026-11-15.jsonl`.

All six printed-New-Haven offices match in New Haven city (GEOID 0952000) on both address files and both official-map-point legs. Matched addresses agree with the printed street, city, state, and ZIP. No map-point fallbacks. No printed-New-Haven office geocodes outside the city. No other printed city has any geocode leg inside New Haven city. In-city, not listed: none.

## Classification

Listed (6), all money orders, all four geocode legs in GEOID 0952000: New Haven, Yale, Fair Haven, Westville, Amity Retail Store, and Kilby. Open evenings: 2 (New Haven, Yale). Open weekends: 6. Holds: none.
