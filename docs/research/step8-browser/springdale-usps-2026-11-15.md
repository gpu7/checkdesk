# Springdale, AR: USPS locator research (2026-11-15, America/Denver)

Research only until the city pages are shipped. No business was contacted. No browser was used. last_verified: 2026-11-15. Official detail pages that were fetched are marked verification_status `verified_official_locator`. Hours below are **Central Time**. Arkansas observes daylight saving. City-limits wording: Springdale is one **incorporated Census place** spanning Washington and Benton counties (Census "Springdale city" GEOID 0566080). Ranking and city-limits checks use the whole-place boundary. Springdale is not a consolidated city-county. A USPS printed city of Springdale is treated as agreeing with that Census place name only when the address and official map point also fall inside Springdale city. Offices printed Springdale whose address or map point falls outside the city are holds. Offices printed with other place names are left off, or held if they geocode inside Springdale city. Map-point fallback applies only when the printed city already agrees and the official map point is in Springdale city.

Raw records are under `/workspace/step8sdal/`.

## Method

- **Locator:** official USPS Location Finder API (`https://tools.usps.com/UspsToolsRestServices/rest/POLocator/findLocations`, `requestType` po), queried with curl the same way as the earlier Arkansas cities. Official Springdale, AR ZIP list: https://www.zip-codes.com/city/ar-springdale.asp (USPS data last updated November 1, 2026). The official table lists **4** codes: 72762 and 72764 (Standard); 72765 and 72766 (P.O. Box). Nearby official ZIPs not already on that list, queried in pass 1: Fayetteville 72701, 72702, 72703, 72704, and 72730 (72764 is also official Fayetteville); Tontitown 72770 (search.asp; official Tontitown ZIPs are 72704, 72762, and 72770; the `ar-tontitown` slug redirects to the Fayetteville page); Johnson 72741; Elm Springs 72728 (72762 is also official Elm Springs); Lowell 72745; Cave Springs 72718; Rogers 72756, 72757, and 72758; Bentonville 72712, 72713, and 72716; Elkins 72727; Goshen 72735; Prairie Grove 72753; Centerton 72719; Pea Ridge 72751; Bella Vista 72714 and 72715; Siloam Springs 72761; West Fork 72774; Greenland 72737; Gentry 72734; Avoca 72711; Garfield 72732; and Gateway 72733. ZIP-Codes.com slug notes: `ar-bethel-heights` redirects to the Springdale page; search.asp for “Bethel Heights, AR” returns 72764, already on the official Springdale list. `ar-little-flock` redirects to the Rogers page; search.asp for “Little Flock, AR” returns 72756, already queried as Rogers. Search.asp for “Highfill, AR” returns 0 official ZIPs. The `ar-hindsville` city page hit a lookup limit; search.asp for “Hindsville, AR” returns 72738, which was added in pass 2. Pass 1 (`sweep.py`): **34 ZIPs, 68 queries** at 5 and 15 miles, all JSON, **54 unique Post Office records**, 0 parse failures. Pass 2: 5 and 15 miles around 72738, plus 1, 2, 3, 10, and 20 mile widenings around 72762, 72764, 72765, 72770, 72701, 72703, 72745, 72756, 72712, 72741, and 72738 (57 queries, **1 added record**, Witter 72776, far from Springdale city). Total **55 records** (`usps_all.json`). Only two offices print Springdale; no additional Springdale-printed office appeared in pass 2.
- **Official pages:** `https://tools.usps.com/locations/details/<id>` fetched with curl for all 55 records. All returned **HTTP 200 on the first try**. Each page’s embedded `poDetail` matched the API record (`pages.json`, `match_api` on all 55). Retail hours = the BUSINESS block only. Money-order service is taken from the office’s own `poDetail` services list.
- **City limits:** all 55 addresses and all 55 official locator map points against Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, Incorporated Places + CDPs + Counties (`usps_geo_all.jsonl`). OpenStreetMap was not used.

## Candidate includes (2), money orders yes, HTTP 200, verified_official_locator

Retail hours are Central Time. “Open evenings” means a weekday BUSINESS close after 17:00 (a 17:00 close does not count). “Open weekends” means Saturday or Sunday retail. Official page for each: `https://tools.usps.com/locations/details/<id>`. Both print Springdale and have Current + 2020 address and both official map points in Springdale city (GEOID 0566080) / Washington County (GEOID 05143), which is one part of this two-county Census place. Both list MONEYORDERSDOM and MONEYORDERSINQ.

| ID | Office | Address | Phone | Retail (BUSINESS) hours | Evenings | Weekends | Geocode |
|---|---|---|---|---|---|---|---|
| 1382568 | SPRINGDALE | 2811 Springdale Ave, Springdale, AR 72764 | 479-751-4441 | Mon-Fri 09:00-17:00; Sat 09:00-12:00; Sun closed | no | yes | Springdale city all four legs, Washington County; point 36.172149,-94.161951 |
| 1387201 | SPRINGDALE STATION | 429 Holcomb St, Springdale, AR 72764 | 479-751-4447 | Mon-Fri 09:00-16:30; Sat closed; Sun closed | no | no | Springdale city all four legs, Washington County; point 36.181498,-94.130836 |

Neither include has a weekday close after 17:00. One has Saturday retail (Springdale, 09:00-12:00). Neither publishes Sunday retail.

## In-city, not listed

None. No Springdale-printed office inside Springdale city lacks money-order tags.

## HOLDS

None. No Springdale-printed office geocodes outside Springdale city. No other-printed office geocodes inside Springdale city on any of the four legs.

## Left off (omissions, not holds)

53 other-printed offices in the 55-record Springdale sweep, all outside Springdale city on both Census files. Nearby other-city offices include Fayetteville (2), Tontitown, Elm Springs, Lowell, Rogers, Bentonville, Farmington, Cave Springs, Greenland, Goshen, and farther offices. No Johnson-printed office was found. Details and remaining address no-matches among far offices are in `usps_geo_all.jsonl`.

## Fetch failures

None of the 68 + 57 locator queries failed to parse. All 55 detail pages returned HTTP 200 on the first try and match the API. No address no-matches among the two includes.

## Summary counts (USPS-only)

- **2** listable offices, both money orders
- **0** Open evenings
- **1** Open weekends (Springdale Post Office)
- **0** holds
- **0** in-city, not listed
- **53** other-printed offices left off
