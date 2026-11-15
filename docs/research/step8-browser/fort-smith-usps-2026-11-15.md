# Fort Smith, AR: USPS locator research (2026-11-15, America/Denver)

Research only until the city pages are shipped. No business was contacted. No browser was used. last_verified: 2026-11-15. Official detail pages that were fetched are marked verification_status `verified_official_locator`. Hours below are **Central Time**. Arkansas observes daylight saving. City-limits wording: Fort Smith is an **incorporated city** in Sebastian County (Census "Fort Smith city" GEOID 0524550). The county is Sebastian County (GEOID 05131). Fort Smith is not a consolidated city-county. A USPS printed city of Fort Smith is treated as agreeing with that Census place name only when the address and official map point also fall inside Fort Smith city. Offices printed Fort Smith whose address or map point falls outside the city are holds. Offices printed with other place names are left off, or held if they geocode inside Fort Smith city. Map-point fallback applies only when the printed city already agrees and the official map point is in Fort Smith city.

Raw records are under `/workspace/step8fsm/`.

## Method

- **Locator:** official USPS Location Finder API (`https://tools.usps.com/UspsToolsRestServices/rest/POLocator/findLocations`, `requestType` po), queried with curl the same way as Little Rock and Fayetteville. Official Fort Smith, AR ZIP list: https://www.zip-codes.com/city/ar-fort-smith.asp (USPS data last updated November 1, 2026). The official table lists **13** codes: 72901, 72903, 72904, 72908, and 72916 (Standard); 72902, 72906, 72913, 72914, 72917, and 72918 (P.O. Box); 72905 and 72919 (Unique). Nearby official ZIPs not already on that list, queried in pass 1: Van Buren 72956 and 72957; Barling 72923; Alma 72921; Greenwood 72936; Lavaca 72941; Charleston 72933; Mulberry 72947; Hackett 72937; Mansfield 72944; Huntington 72940; Midland 72945; Hartford 72938; Waldron 72958; Paris 72855; Ozark 72949; Booneville 72927; Magazine 72943; Cedarville 72932; Rudy 72952; Mountainburg 72946; Uniontown 72955; Natural Dam 72948; Dyer 72935; Arkoma, OK 74901; Pocola, OK 74902; Roland, OK 74954; Moffett, OK 74946; Spiro, OK 74959; Sallisaw, OK 74955; and Poteau, OK 74953. ZIP-Codes.com slug notes: `ar-bonanza` redirects to the Fort Smith page; search.asp for “Bonanza, AR” returns 72916, already on the official Fort Smith list. Search.asp for “Kibler, AR” returns 0 official ZIPs. Search.asp for “Central City, AR” returned 71901 (Hot Springs National Park) and 72941 (Lavaca), which are not treated as Central City official ZIPs; 72941 was already queried as Lavaca. Search.asp for “Fort Coffee, OK” returns 74959, already queried as Spiro. Pass 1 (`sweep.py`): **44 ZIPs, 88 queries** at 5 and 15 miles, all JSON, **67 unique Post Office records**, 0 parse failures. Pass 2: 1, 2, 3, 10, and 20 mile widenings around 72901, 72903, 72904, 72908, 72916, 72956, 72923, 72936, 74901, and 72921 (50 queries, **0 added records**). Total **67 records** (`usps_all.json`). Only six offices print Fort Smith; no additional Fort Smith-printed office appeared in pass 2.
- **Official pages:** `https://tools.usps.com/locations/details/<id>` fetched with curl for all 67 records. All returned **HTTP 200 on the first try**. Each page’s embedded `poDetail` matched the API record (`pages.json`, `match_api` on all 67). Retail hours = the BUSINESS block only. Money-order service is taken from the office’s own `poDetail` services list.
- **City limits:** all 67 addresses and all 67 official locator map points against Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, Incorporated Places + CDPs + Counties (`usps_geo_all.jsonl`). Address geocoding used the office’s printed state (AR or OK), not a hardcoded AR, because the Fort Smith sweep includes Oklahoma-border offices. OpenStreetMap was not used.

## Candidate includes (4), money orders yes, HTTP 200, verified_official_locator

Retail hours are Central Time. “Open evenings” means a weekday BUSINESS close after 17:00 (a 17:00 close does not count). “Open weekends” means Saturday or Sunday retail. Official page for each: `https://tools.usps.com/locations/details/<id>`. All four print Fort Smith and have Current + 2020 address and both official map points in Fort Smith city (GEOID 0524550) / Sebastian County (GEOID 05131). All four list MONEYORDERSDOM and MONEYORDERSINQ.

| ID | Office | Address | Phone | Retail (BUSINESS) hours | Evenings | Weekends | Geocode |
|---|---|---|---|---|---|---|---|
| 1363726 | DOWNTOWN FORT SMITH | 1020 Garrison Ave, Fort Smith, AR 72901 | 479-494-7950 | Mon-Fri 08:00-16:30; Sat closed; Sun closed | no | no | Fort Smith city all four legs; point 35.383975,-94.4215459 |
| 1442400 | GMF FORT SMITH | 3318 S 74th St, Fort Smith, AR 72903 | 479-484-6401 | Mon-Fri 08:30-18:00; Sat 10:00-14:00; Sun closed | yes | yes | Fort Smith city all four legs; point 35.350319,-94.352412 |
| 1363844 | MIDLAND FORT SMITH | 3100 Wirsing Ave, Fort Smith, AR 72904 | 479-782-1635 | Mon-Fri 08:00-16:30; Sat closed; Sun closed | no | no | Fort Smith city all four legs; point 35.406423,-94.396356 |
| 1363842 | FIANNA HILLS | 2712 Market Trce, Fort Smith, AR 72908 | 479-648-9345 | Mon-Fri 08:00-16:30; Sat closed; Sun closed | no | no | Fort Smith city all four legs; point 35.301353,-94.4059669 |

One of the four includes has a weekday close after 17:00 (GMF Fort Smith, 18:00) and Saturday retail. The other three close at 16:30 and have no weekend retail.

## In-city, not listed (2)

Both print Fort Smith, sit at the same address as the listed GMF Fort Smith office (3318 S 74th St, 72903), and have all four geocode legs in Fort Smith city (GEOID 0524550). Neither lists money-order tags. Neither publishes a BUSINESS hours block.

1. **FORT SMITH (1363843)**. Official page services are bulk-mail and pickup related (BULKMAILACCEPT, and similar). No BUSINESS block, no MONEYORDERSDOM or MONEYORDERSINQ.
2. **FORT SMITH (1473448)**. Same address and phone as the GMF record. No BUSINESS block, no money-order tags.

## HOLDS

None. No Fort Smith-printed office geocodes outside Fort Smith city. No other-printed office geocodes inside Fort Smith city on any of the four legs.

## Left off (omissions, not holds)

61 other-printed offices in the 67-record Fort Smith sweep, all outside Fort Smith city on both Census files. Nearby other-city offices include Van Buren (2), Barling, Greenwood, Alma, Hackett, Lavaca, Arkoma (OK), Moffett (OK), Roland (OK), Pocola (OK), and farther Arkansas and Oklahoma offices. Details and remaining address no-matches among far offices are in `usps_geo_all.jsonl`.

## Fetch failures

None of the 88 + 50 locator queries failed to parse. All 67 detail pages returned HTTP 200 on the first try and match the API. No address no-matches among the six Fort Smith-printed records.

## Summary counts (USPS-only)

- **4** listable offices, all money orders
- **1** Open evenings (GMF Fort Smith)
- **1** Open weekends (GMF Fort Smith)
- **0** holds
- **2** in-city, not listed (both at 3318 S 74th St, no money-order tags and no BUSINESS hours)
- **61** other-printed offices left off
