# Tucson, AZ: USPS locator research (2026-11-14, America/Denver)

Research only until the city pages are shipped. No business was contacted. No browser was used. last_verified: 2026-11-14. Official detail pages that were fetched are marked verification_status `verified_official_locator`. Hours below are **Arizona Time** (Mountain Standard Time). Arizona does not observe daylight saving. City-limits wording: Tucson is an **incorporated city** in Pima County (Census "Tucson city" GEOID 0477000). The county is Pima County (GEOID 04019). Tucson is not a consolidated city-county. A USPS printed city of Tucson is treated as agreeing with that Census place name only when the address and official map point also fall inside Tucson city. Offices printed Tucson whose address or map point falls outside the city (in a CDP, another city, or unincorporated county land) are holds. Offices printed with other place names are left off, or held if they geocode inside Tucson city. Map-point fallback applies only when the printed city already agrees and the official map point is in Tucson city.

## Method

- **Locator:** official USPS Location Finder API (`https://tools.usps.com/UspsToolsRestServices/rest/POLocator/findLocations`, `requestType` po), queried with curl the same way as Phoenix. Pass 1 (`sweep.py`): 5 and 15 miles around every Tucson ZIP (the 55 USPS-city Tucson codes listed for Tucson, AZ by ZIP-Codes.com from USPS data last updated 2026-11-01, including 85634 and 85641, which also appear as official Sells and Vail ZIPs; 85713 aliases South Tucson; 85704, 85737, 85742, and 85755 are official Oro Valley ZIPs). Source page: https://www.zip-codes.com/city/az-tucson.asp (last updated November 1, 2026). Nearby official ZIPs not already on that list: Marana 85653 and 85658, Sahuarita 85629, Green Valley 85614 and 85622, Mount Lemmon 85619, Ajo 85321, Cortaro 85652, Rillito 85654, Benson 85602, and Sierra Vista 85613, 85635, 85636, 85650, and 85670. South Tucson official ZIP (search.asp) is 85713; Oro Valley official ZIPs are the four already on the Tucson list. 70 ZIPs, 140 queries, all JSON, **41 unique Post Office records**, 0 parse failures. Pass 2 (`sweep2.py`): additional official/fringe ZIPs (Hereford, Huachuca City, Oracle, Pomerene, Red Rock, Saint David, San Manuel, Topawa, Tubac, Amado) at 5, 15, and 20 miles, plus 1, 2, 3, 10, 20, and (on sparse edges) 50 mile widenings (117 queries, **31 added records**, all far from Tucson city). Total **72 records** (`usps_all.json`). Raw records are under `/workspace/step8tus/`.
- **Official pages:** `https://tools.usps.com/locations/details/<id>` fetched with curl about 1:16 PM MT for all 72 records. All returned **HTTP 200 on the first try**. Each page's embedded `poDetail` matched the API record on name, address, phone, BUSINESS hours, and map coordinates for all 72 (`pages.json`). Retail hours = the BUSINESS block only. Money-order service is taken from the office's own `poDetail` services list.
- **City limits:** all 72 addresses and all 72 official locator map points against Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, Incorporated Places + CDPs + Counties (`usps_geo_all.jsonl`). OpenStreetMap was not used.

## Candidate includes (8), money orders yes, HTTP 200, verified_official_locator

Retail hours are Arizona Time. "Open evenings" means a weekday BUSINESS close after 17:00 (a 17:00 close does not count). "Open weekends" means Saturday or Sunday retail. Official page for each: `https://tools.usps.com/locations/details/<id>`.

| ID | Office | Address | Phone | Retail (BUSINESS) hours | Evenings | Weekends | Geocode |
|---|---|---|---|---|---|---|---|
| 1385111 | CORONADO | 255 N Rosemont Blvd, Tucson, AZ 85711 | 520-571-7160 | Mon-Fri 09:00-17:00; Sat 10:00-14:00; Sun closed | no | yes | Current + 2020 address and both map points: Tucson city (GEOID 0477000); point 32.224996,-110.884871. MONEYORDERSDOM only. |
| 1439478 | DAVIS MONTHAN AFB | 5450 E Madera St, Tucson, AZ 85708 | 520-790-0180 | Mon-Fri 10:00-16:00; Sat/Sun closed | no | no | Address no-match after street-name and city-name retries on both files. Official map point 32.176705,-110.875899 is Tucson city (GEOID 0477000) on both files. Printed city is already Tucson, so the map-point fallback applies. MONEYORDERSDOM only. |
| 1385112 | DESERT FOOTHILLS | 1700 E River Rd, Tucson, AZ 85718 | 520-577-8929 | Mon-Fri 09:00-17:00; Sat/Sun closed | no | no | Current + 2020 address and both map points: Tucson city; point 32.287445,-110.947122 |
| 1385114 | FORT LOWELL | 6460 E Grant Rd, Tucson, AZ 85715 | 520-290-9718 | Mon-Fri 08:30-17:00; Sat 08:30-15:00; Sun closed | no | yes | Current + 2020 address and both map points: Tucson city; point 32.24968,-110.854257 |
| 1385118 | MISSION | 315 W Valencia Rd, Tucson, AZ 85706 | 520-889-8647 | Mon-Fri 09:00-17:00; Sat 10:00-14:00; Sun closed | no | yes | Current + 2020 address and both map points: Tucson city; point 32.133387,-110.973775. MONEYORDERSDOM only. |
| 1385121 | RINCON | 1099 S Pantano Rd, Tucson, AZ 85710 | 520-296-1279 | Mon-Fri 09:00-17:00; Sat 09:00-13:00; Sun closed | no | yes | Current + 2020 address and both map points: Tucson city; point 32.208031,-110.822924 |
| 1385123 | SILVERBELL | 975 N Silverbell Rd, Tucson, AZ 85745 | 520-388-9323 | Mon-Fri 09:00-17:00; Sat/Sun closed | no | no | Current + 2020 address and both map points: Tucson city; point 32.234594,-111.004368 |
| 1385124 | SUN | 2100 E Speedway Blvd, Tucson, AZ 85719 | 520-881-1175 | Mon-Fri 08:30-17:00; Sat/Sun closed | no | no | Current + 2020 address and both map points: Tucson city; point 32.235582,-110.940294 |

None of the eight includes has a weekday close after 17:00. Four have Saturday retail.

## In-city, not listed (4)

These print Tucson and geocode inside Tucson city on both files, but they are not candidate money-order includes.

1. **DOWNTOWN TUCSON (1385113)**, 141 S 6th Ave, Tucson, AZ 85701, 520-903-1958. No money-order tags. BUSINESS Mon-Fri 09:00-17:00, Sat/Sun closed. Point 32.220425,-110.968295, Tucson city.
2. **KINO RETAIL UNIT (1385115)**, 3655 N Oracle Rd Ste 101, Tucson, AZ 85705, 520-887-0306. No money-order tags. BUSINESS Mon-Fri 10:00-17:00, Sat/Sun closed. Point 32.272957,-110.978925, Tucson city.
3. **RINCON PLAZA RETAIL (1609896)**, 7545 S Houghton Rd Ste 149, Tucson, AZ 85747, 520-296-1279. No money-order tags and no BUSINESS hours. Point 32.114931,-110.771774, Tucson city.
4. **TUCSON (1439539)**, 1501 S Cherrybell Stra Rm 205, Tucson, AZ 85726, 520-388-5043. No money-order tags. BUSINESS Mon-Fri 09:00-18:30, Sat 08:30-15:30, Sun closed (evenings and weekends, but not listable without money-order tags). Point 32.204716,-110.945427, Tucson city.

## HOLDS (6)

1. **CASAS ADOBES (1439472)**, 6281 N Oracle Rd, printed **Tucson**, AZ 85704, 520-531-0695. Money orders yes; BUSINESS Mon-Fri 09:00-17:00, Sat 09:30-14:00. Current + 2020 address and both map points: **Casas Adobes CDP** (GEOID 0410670), Pima County, not Tucson city. Point 32.320565,-110.975644. Held because the printed city is Tucson but the address and official map point fall outside the city, in a CDP.
2. **MOUNTAIN VIEW (1385119)**, 7959 N Thornydale Rd, printed **Tucson**, AZ 85741, 520-744-6720. Money orders yes; BUSINESS Mon-Fri 08:30-17:00, Sat 09:00-16:00. Current + 2020 address and both map points: **Casas Adobes CDP** (GEOID 0410670). Point 32.350851,-111.047903. Held for the same printed-Tucson / outside-city rule.
3. **ORO VALLEY (1440333)**, 11900 N La Canada Dr, printed **Tucson**, AZ 85737, 520-229-0320. Money orders yes; BUSINESS Mon-Fri 08:30-17:00, Sat/Sun closed. Current + 2020 address and both map points: **Oro Valley town** (GEOID 0451600). Point 32.422756,-110.994842. Held because the address and official map point fall in a separate incorporated place.
4. **SAN XAVIER (1458921)**, 4700 W Valencia Rd, printed **Tucson**, AZ 85757, 520-883-3139. Money orders yes; BUSINESS Mon-Fri 09:00-16:00, Sat/Sun closed. Current + 2020 address and both map points: **Drexel Heights CDP** (GEOID 0420540). Point 32.134696,-111.064882. Held because the address and official map point fall outside Tucson city, in a CDP.
5. **SOUTH TUCSON (1439531)**, 2420 S 6th Ave, printed **Tucson**, AZ 85713, 520-903-9827. No money-order tags; BUSINESS Mon-Fri 11:00-13:00, Sat/Sun closed. Current + 2020 address and both map points: **South Tucson city** (GEOID 0468850), a separate incorporated city surrounded by Tucson. Point 32.194022,-110.96887. Held because the printed city is Tucson but the address and official map point fall in another city. The official locator name is South Tucson.
6. **VAIL ANNEX (1451483)**, 13333 E Colossal Cave Rd, printed **Vail**, AZ 85641, 520-762-5052. No money-order tags and no BUSINESS hours. Address no-match after street-name and city-name retries on both files. Official map point 32.045417,-110.714308: **Tucson city** (GEOID 0477000) on the current file (retried); Pima County only, no place and no CDP, on the 2020 file (retried). Held because the official printed city is Vail, not Tucson, and the current official map point falls inside Tucson city. The map-point fallback does not apply when the printed city already disagrees.

## Left off (omissions, not holds)

- No Green Valley-, Catalina-, Cortaro-, Rillito-, Mount Lemmon-, or Sahuarita-printed office geocodes inside Tucson city.
- Nearby other-city offices (printed city ≠ Tucson and the geocoder agrees outside Tucson city) include, among others: VAIL 1385618 (Vail CDP); MARANA 1371778 (Marana town); SAHUARITA 1380254 (Sahuarita town); GREEN VALLEY 1365557 (Green Valley CDP); CATALINA 1357277 (Catalina CDP); CORTARO 1359327 (address no-match; official map point in Marana town); RILLITO 1379344 (Rillito CDP); MOUNT LEMMON 1374025 (Summerhaven CDP); SELLS 1381182 (Sells CDP); AJO 1352519 (Ajo CDP); BENSON 1354669 (Benson city); and farther pass-2 offices (Sierra Vista, Fort Huachuca, Bisbee, Casa Grande, Nogales-area, and similar). Details and remaining address no-matches are in `usps_geo_all.jsonl`.

## Fetch failures

None of the 140 + 117 locator queries failed to parse. All 72 detail pages returned HTTP 200 on the first try and match the API. Davis Monthan AFB and Vail Annex address no-matches remain after retries; Davis Monthan is included on its official map point inside Tucson city, and Vail Annex is a hold. A leftover `http.txt` fragment from an unrelated earlier fetch in the same directory was rewritten to the 72 Tucson-area IDs before parsing.
