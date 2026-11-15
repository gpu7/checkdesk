# Wilmington, DE USPS research — 2026-11-15 (America/Denver)

First Delaware city. Classification used only Census "Wilmington city", GEOID 1077580, in New Castle County (GEOID 10003). Elsmere, New Castle, Newport, Newark, Bellefonte, and nearby CDPs such as Greenville, Edgemoor, Bear, and Claymont were not folded in. Hours are Eastern Time. Public sources only; no business was contacted.

## Official ZIPs

ZIP-Codes.com city page slug `de-wilmington` is not a collision (title Wilmington, DE, last updated November 1, 2026). search.asp title "25 ZIP Codes in Wilmington, DE". The city page and search.asp have the same 25 unique codes, all in New Castle County and all listed Wilmington (10 Standard, 3 P.O. Box, 12 Unique): 19801, 19802, 19803, 19804, 19805, 19806, 19807, 19808, 19809, 19810, 19850, 19880, 19884, 19885, 19886, 19890, 19891, 19892, 19893, 19894, 19895, 19896, 19897, 19898, 19899.

Neighborhood and nearby slugs that collided with the Wilmington city page (used search.asp fallback): Elsmere, Newport, Bellefonte, Arden, Ardencroft, Ardentown, Greenville, Talleyville, Stanton, Marshallton, and Edgemoor. Other nearby slug collisions, also handled with search.asp: Christiana with Newark, Minquadale with New Castle, and several Pennsylvania and New Jersey border slugs (Marcus Hook, Trainer, Linwood, Boothwyn, Carneys Point).

## Locator sweeps

Pass 1 used prefixes 197/198 plus nearby Pennsylvania 193/190 and New Jersey 080 ZIPs that appeared on border city pages (77 ZIPs), 5 and 15 miles (154 queries). 279 unique records, 0 failures, 9 printed Wilmington.

Pass 2 used 1, 2, 3, 10, and 20 mile widenings around 43 official and edge ZIPs: the official 25 plus Bear 19701, Newark 19702/19711/19713, Claymont 19703, Delaware City 19706, Hockessin 19707, Kirkwood 19708, Middletown 19709, Montchanin 19710, New Castle 19720/19721, Chester 19013, Marcus Hook 19061, Chadds Ford 19317, Kennett Square 19348, Penns Grove 08069, and Pennsville 08070 (215 queries). 0 failures, 16 added records far from Wilmington city (South Jersey, Maryland, and Lancaster County), still 9 printed Wilmington. Total 295 unique records in `wilmington-usps-locator-2026-11-15.jsonl`.

## Official pages

All 295 official pages returned HTTP 200 on the first try. Embedded `poDetail` matched the API record on all 295 (`match_api`).

The 9 records that print Wilmington:

| locatorID | Official name | Address | ZIP | Phone | BUSINESS | Money orders |
|-----------|---------------|---------|-----|-------|----------|--------------|
| 1445854 | RODNEY SQ | 500 DELAWARE AVE STE 1 | 19801 | 302-656-0228 | 07:00-17:30 weekdays; Saturday 09:00-14:00 | DOM and INQ |
| 1369772 | LANCASTER AVE | 1500 LANCASTER AVE | 19805 | 302-654-0725 | 08:00-17:00 weekdays; Saturday 08:00-14:00 | DOM and INQ |
| 1434659 | TALLEYVILLE | 3911 CONCORD PIKE | 19803 | 302-478-5753 | 07:30-18:00 weekdays; Saturday 08:30-15:30 | DOM and INQ |
| 1434217 | WILMINGTON | 3911 CONCORD PIKE | 19803 | 302-479-9501 | no BUSINESS block | none |
| 1445846 | NEWPORT | 1704 W NEWPORT PIKE | 19804 | 302-994-5029 | 08:00-17:00 weekdays; Saturday 08:00-13:00 | DOM and INQ |
| 1434209 | GREENVILLE | 3801 KENNETT PIKE STE A101 | 19807 | 302-652-1877 | 08:30-18:00 weekdays; Saturday 09:00-13:00 | DOM and INQ |
| 1434211 | MARSHALLTON | 3434 OLD CAPITOL TRL | 19808 | 302-998-1168 | 08:00-17:00 weekdays; Saturday 09:00-15:00 | DOM and INQ |
| 1434207 | EDGEMOOR | 4901 GOVERNOR PRINTZ BLVD | 19809 | 302-762-1833 | 08:00-17:30 weekdays; Saturday 08:00-15:00 | DOM and INQ |
| 1450269 | TALLEYVILLE CARRIER ANNEX | 3505 SILVERSIDE RD STE 103 | 19810 | 302-478-3201 | no BUSINESS block | none |

Sunday is closed at both listed offices. A 17:00 weekday close does not count as Open evenings; 17:30 does.

## Geocoder

U.S. Census Bureau Geocoder, address and coordinates endpoints, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, layers Incorporated Places + CDPs + Counties. OpenStreetMap was not used. Full dump: `wilmington-usps-geocoder-2026-11-15.jsonl`. No geocoder errors on 295 records.

Only two records have any geocode leg in Wilmington city (GEOID 1077580): Rodney Sq and Lancaster Ave. Both match in Wilmington city on both address files and both official-map-point legs. Rodney Sq unit STE 1 dropped; matched 500 DELAWARE AVE, WILMINGTON, DE, 19801. No map-point fallbacks. No other printed city has any geocode leg inside Wilmington city.

The other seven printed-Wilmington records sit in New Castle County but not in Wilmington city, so they are HOLDs:

- Talleyville and the second record also named Wilmington at 3911 Concord Pike: both files match 3911 CONCORD PIKE, WILMINGTON, DE, 19803, in New Castle County with no incorporated place and no CDP. Both official map points agree. The 1434217 record has no money-order tags and no BUSINESS block.
- Newport: both files match 1704 W NEWPORT PIKE, WILMINGTON, DE, 19804, in New Castle County with no incorporated place and no CDP. Both official map points agree. (This is not inside Newport town.)
- Greenville: unit STE A101 dropped; the current file matches 3801 KENNETT PIKE, WILMINGTON, DE, 19807 in Greenville CDP (GEOID 1031430). The 2020 address file did not match, including retries without the unit, with STE/SUITE/UNIT variants, and with printed city Greenville. Both official map points are in Greenville CDP, not Wilmington city.
- Marshallton: both files match 3434 OLD CAPITOL TRL, WILMINGTON, DE, 19808, in New Castle County with no incorporated place and no CDP. Both official map points agree.
- Edgemoor: the current address file did not match 4901 GOVERNOR PRINTZ BLVD after street-name retries (GOVERNOR PRINTZ BOULEVARD, GOV PRINTZ BLVD, shortened forms, ZIP variants, and printed city Edgemoor). The 2020 file matches 4901 GOVERNOR PRINTZ BLVD, WILMINGTON, DE, 19809 in Edgemoor CDP (GEOID 1023240). Both official map points are in Edgemoor CDP, not Wilmington city.
- Talleyville Carrier Annex: unit STE 103 dropped; both files match 3505 SILVERSIDE RD, WILMINGTON, DE, 19810, in New Castle County with no incorporated place and no CDP. Both official map points agree. No money-order tags.

Wilmington Box (1434636, 147 Quigley Blvd) prints New Castle, not Wilmington, and geocodes in New Castle County with no leg in Wilmington city.

## Classification

Listed (2), all money orders: Rodney Sq and Lancaster Ave. Open evenings: 1 (Rodney Sq). Open weekends: 2. Holds: 7 (Talleyville, the second Wilmington record at 3911 Concord Pike, Newport, Greenville, Marshallton, Edgemoor, and Talleyville Carrier Annex — all print Wilmington and sit outside Wilmington city). In-city, not listed: none.
