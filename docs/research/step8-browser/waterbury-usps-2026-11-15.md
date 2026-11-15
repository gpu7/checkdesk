# Waterbury, CT USPS research — 2026-11-15 (America/Denver)

Fifth Connecticut city. Classification used only Census "Waterbury city", GEOID 0980000, in the Naugatuck Valley Planning Region (GEOID 09140). Prospect, Wolcott, Naugatuck, Watertown, Middlebury, Oakville, and other nearby municipalities were not folded in. Hours are Eastern Time. Public sources only; no business was contacted.

## Official ZIPs

ZIP-Codes.com city page slug `ct-waterbury` is not a collision (title Waterbury, CT, last updated November 1, 2026). search.asp title "17 ZIP Codes in Waterbury, CT". The city page and search.asp have the same 17 unique codes.

15 of those 17 are listed Waterbury in Naugatuck Vly (7 Standard, 8 P.O. Box): 06701, 06702, 06703, 06704, 06705, 06706, 06708, 06710, 06720, 06721, 06722, 06723, 06724, 06725, 06726.

The other 2 in the official Waterbury search are listed as other cities and are not treated as official Waterbury printed-city ZIPs, but they were included in pass 1: Prospect 06712 (Naugatuck Vly); Wolcott 06716 (Capitol).

Neighborhood slugs that collided with the Waterbury city page (used search.asp fallback): East End and Plaza. The Wolcott slug `ct-wolcott` also collided with the Waterbury city page; Wolcott ZIPs were taken from search.asp (title "2 ZIP Codes in Wolcott, CT"), which includes 06705 listed as Waterbury (already an official Waterbury ZIP) and 06716 listed as Wolcott. Other nearby slug collisions, also handled with search.asp: Watertown with Oakville, Thomaston with Northfield, Seymour with Oxford, Union City with Naugatuck, Washington with New Preston Marble Dale, and Forestville with Bristol.

## Locator sweeps

Pass 1 used prefixes 067/064 (53 ZIPs), 5 and 15 miles (106 queries). 159 unique records, 0 failures, 5 printed Waterbury.

Pass 2 used 1, 2, 3, 10, and 20 mile widenings around 40 official and edge ZIPs: the official 17 plus Bristol 06010/06011, Ansonia 06401, Beacon Falls 06403, Cheshire 06408/06410/06411, Derby 06418, Meriden 06450/06451, Seymour 06478/06483, Southbury 06488, Southington 06489, Middlebury 06762, Naugatuck 06770, Northfield 06778, Oakville 06779/06795, Plymouth 06782, Terryville 06786, Thomaston 06787, and Woodbury 06798 (200 queries). 0 failures, 25 added records far from Waterbury city (Hartford-area and similar), still 5 printed Waterbury. Total 184 unique records in `waterbury-usps-locator-2026-11-15.jsonl`.

## Official pages

All 184 official pages returned HTTP 200 on the first try. Embedded `poDetail` matched the API record on all 184 (`match_api`).

The 5 records that print Waterbury:

| locatorID | Official name | Address | ZIP | Phone | BUSINESS | Money orders |
|-----------|---------------|---------|-----|-------|----------|--------------|
| 1434163 | WATERBURY | 135 GRAND ST | 06701 | 203-574-6521 | 08:00-18:00 weekdays; Saturday 08:00-12:00 | DOM and INQ |
| 1361710 | EAST END | 159 MANOR AVE STE 6 | 06705 | 203-574-6512 | 09:00-17:00 weekdays; Saturday 08:30-12:30 | DOM and INQ |
| 1369722 | LAKEWOOD | 797 LAKEWOOD AVE | 06703 | 203-757-7511 | 09:00-17:00 weekdays; Saturday 09:00-12:30 | DOM and INQ |
| 1377781 | PLAZA | 41 WIGWAM AVE | 06704 | 203-759-3642 | 08:30-17:00 weekdays; Saturday 08:30-12:30 | DOM and INQ |
| 1470634 | WATERBURY | 135 GRAND ST | 06701 | 203-574-6521 | no BUSINESS block | none |

Sunday is closed at all four listed offices. A 17:00 weekday close does not count as Open evenings; 18:00 does. The second record at 135 Grand St is a separate locator ID (1470634, ZIP+4 06701-9901) with no services and no hours on its official page. Several offices do not share a phone number except the two Grand St records, which publish the same number; the published numbers are kept.

## Geocoder

U.S. Census Bureau Geocoder, address and coordinates endpoints, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, layers Incorporated Places + CDPs + Counties. OpenStreetMap was not used. Full dump: `waterbury-usps-geocoder-2026-11-15.jsonl`.

All five printed-Waterbury records have all four geocode legs in Waterbury city (GEOID 0980000). Current-file county is the Naugatuck Valley Planning Region (GEOID 09140); the 2020 file still reports New Haven County (GEOID 09009). No map-point fallbacks. No printed-Waterbury office geocodes outside the city. No other printed city has any geocode leg inside Waterbury city.

Waterbury Post Office and the second Grand St record: official ZIP 06701 vs both address files matching 135 GRAND ST, WATERBURY, CT, 06702, same street and still in Waterbury city (not a fallback). The official map point (41.553526, -73.042476) is also in Waterbury city on both files.

East End: unit STE 6 dropped; matched 159 MANOR AVE, WATERBURY, CT, 06705, all four legs in Waterbury city.

Lakewood: official page is 797 LAKEWOOD AVE, ZIP 06703 (a P.O. Box ZIP). Both address files match 797 LAKEWOOD RD, WATERBURY, CT, 06704, still the same street and still in Waterbury city (not a fallback). The official map point (41.571149, -73.008132) is also in Waterbury city on both files.

Plaza matches 41 WIGWAM AVE, WATERBURY, CT, 06704 on both address files, in Waterbury city, with the official map point (41.582978, -73.035529) also in the city on both files.

## Classification

Listed (4), all money orders: Waterbury, East End, Lakewood, and Plaza. Open evenings: 1 (Waterbury). Open weekends: 4. Holds: none. In-city, not listed: the second Waterbury locator record at 135 Grand St (1470634; no BUSINESS block, no money-order tags).
