# Fayetteville, AR: USPS locator research (2026-11-15, America/Denver)

Research only until the city pages are shipped. No business was contacted. No browser was used. last_verified: 2026-11-15. Official detail pages that were fetched are marked verification_status `verified_official_locator`. Hours below are **Central Time**. Arkansas observes daylight saving. City-limits wording: Fayetteville is an **incorporated city** in Washington County (Census "Fayetteville city" GEOID 0523290). The county is Washington County (GEOID 05143). Fayetteville is not a consolidated city-county. A USPS printed city of Fayetteville is treated as agreeing with that Census place name only when the address and official map point also fall inside Fayetteville city. Offices printed Fayetteville whose address or map point falls outside the city are holds. Offices printed with other place names are left off, or held if they geocode inside Fayetteville city. Map-point fallback applies only when the printed city already agrees and the official map point is in Fayetteville city.

Raw records are under `/workspace/step8fyv/`.

## Method

- **Locator:** official USPS Location Finder API (`https://tools.usps.com/UspsToolsRestServices/rest/POLocator/findLocations`, `requestType` po), queried with curl the same way as Little Rock. Official Fayetteville, AR ZIP list: https://www.zip-codes.com/city/ar-fayetteville.asp (USPS data last updated November 1, 2026). The official table lists **6** codes: 72701, 72703, and 72704 (Standard); 72702 (P.O. Box); plus 72730 (also official Farmington) and 72764 (also official Springdale). Nearby official ZIPs not already on that list, queried in pass 1: Bentonville 72712, 72713, and 72716; Cave Springs 72718; Centerton 72719; Elkins 72727; Greenland 72737; Johnson 72741; Lincoln 72744; Lowell 72745; Pea Ridge 72751; Prairie Grove 72753; Rogers 72756, 72757, and 72758; Siloam Springs 72761; Springdale 72762, 72765, and 72766; West Fork 72774; Winslow 72959; and Gentry 72734. Tontitown’s city page slug redirects to the Fayetteville page; ZIP-Codes.com search.asp for “Tontitown, AR” returns 72704, 72762, and **72770** (72770 was added in the widening pass). Pass 1 (`sweep.py`): **28 ZIPs, 56 queries** at 5 and 15 miles, all JSON, **49 unique Post Office records**, 0 parse failures. Pass 2: 5 and 15 miles around 72770, plus 1, 2, 3, 10, and 20 mile widenings around 72770, 72701, 72703, 72704, 72730, 72727, 72774, 72959, 72761, and 72712 (52 queries, **7 added records**, all far from Fayetteville city). Total **56 records** (`usps_all.json`). Only two offices print Fayetteville; no additional Fayetteville-printed office appeared in pass 2.
- **Official pages:** `https://tools.usps.com/locations/details/<id>` fetched with curl for all 56 records. All returned **HTTP 200 on the first try**. Each page’s embedded `poDetail` matched the API record (`pages.json`, `match_api` on all 56). Retail hours = the BUSINESS block only. Money-order service is taken from the office’s own `poDetail` services list.
- **City limits:** all 56 addresses and all 56 official locator map points against Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, Incorporated Places + CDPs + Counties (`usps_geo_all.jsonl`). OpenStreetMap was not used.

## Candidate includes (2), money orders yes, HTTP 200, verified_official_locator

Retail hours are Central Time. “Open evenings” means a weekday BUSINESS close after 17:00 (a 17:00 close does not count). “Open weekends” means Saturday or Sunday retail. Official page for each: `https://tools.usps.com/locations/details/<id>`. Both print Fayetteville and have Current + 2020 address and both official map points in Fayetteville city (GEOID 0523290) / Washington County (GEOID 05143). Both list MONEYORDERSDOM and MONEYORDERSINQ.

| ID | Office | Address | Phone | Retail (BUSINESS) hours | Evenings | Weekends | Geocode |
|---|---|---|---|---|---|---|---|
| 1363230 | FAYETTEVILLE | 12 W Dickson St, Fayetteville, AR 72701 | 479-442-8286 | Mon-Fri 08:30-17:00; Sat 08:30-12:30; Sun closed | no | yes | Fayetteville city all four legs; point 36.067093,-94.1603909 |
| 1358142 | CB CRAFT | 1590 E Joyce Blvd, Fayetteville, AR 72703 | 479-973-0875 | Mon-Fri 09:00-18:00; Sat 10:00-14:00; Sun closed | yes | yes | Fayetteville city all four legs; point 36.120757,-94.137018 |

One of the two includes has a weekday close after 17:00 (CB Craft, 18:00). Both have Saturday retail. Neither publishes Sunday retail.

## In-city, not listed

None. No Fayetteville-printed office inside Fayetteville city lacks money-order tags.

## HOLDS (1)

1. **GREENLAND (1365601)**, 4500 S School Ave Ste P, printed **Greenland**, AR 72737, 479-443-5998. Money orders yes; BUSINESS Mon-Fri 08:30-12:00, 13:00-16:30, Sat 08:30-11:30. Address no-match after street-name and suite retries with city Greenland, on both Census files. A further retry using city Fayetteville matches the current address file in Fayetteville city (matched address 4500 S SCHOOL AVE, FAYETTEVILLE, AR, 72701); the 2020 file still has no match. Official map point 36.003761,-94.172086: **Fayetteville city** (GEOID 0523290) on both files. Held because the official printed city is Greenland, not Fayetteville, and the official map point falls inside Fayetteville city. The map-point fallback does not apply when the printed city already disagrees.

## Left off (omissions, not holds)

53 other-printed offices in the 56-record Fayetteville sweep, all outside Fayetteville city on both Census files. Nearby other-city offices include Springdale (2), Farmington, Tontitown, Elkins, Prairie Grove, West Fork, Rogers, Bentonville, Lowell, Cave Springs, plus farther offices (Siloam Springs, Bella Vista, and others). No Johnson-printed office was found. Details and remaining address no-matches among far offices are in `usps_geo_all.jsonl`.

## Fetch failures

None of the 56 + 52 locator queries failed to parse. All 56 detail pages returned HTTP 200 on the first try and match the API. No address no-matches among the two includes. Greenland’s address no-match with printed city Greenland remains after retries.

## Summary counts (USPS-only)

- **2** listable offices, both money orders
- **1** Open evenings (CB Craft)
- **2** Open weekends
- **1** hold (Greenland)
- **0** in-city, not listed
- **53** other-printed offices left off
