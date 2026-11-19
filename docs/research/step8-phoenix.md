# Phoenix, AZ — community-named office added 2026-11-19

The Laveen Post Office is now listed on the Phoenix pages, under the rule approved 2026-11-19: the official page prints a community name, both the current and 2020 Census address files place the address inside Phoenix city (GEOID 0455000), money-order tags are present (Domestic Money Orders), and the displayed city stays the official printed USPS city. Official map points return Maricopa County only, with no incorporated place, on both the current and 2020 files; that caveat does not fail the listing standard and is documented in the row notes and on the Phoenix pages. The original Phoenix-printed rows are unchanged.

Added office (printed city in parentheses): Laveen (Laveen). Laveen is a community inside Phoenix city, not a separately incorporated place.

The Phoenix list is now 17 Post Offices, all with money orders (one Open evenings, unchanged: Phoenix on Van Buren Street until 5:30 p.m.; fifteen Open weekends, Saturday only, including Laveen 10:00 a.m. to 12:30 p.m.). Hours stay Arizona Time. The Laveen Annex stays held (no money-order tags and no retail hours). Five Phoenix-printed no-money-order offices remain held.

The body below is the original 2026-11-14 memo and is superseded for listed and hold counts.

# Step 8: Phoenix, AZ (2026-11-14, America/Denver)

**Rows:** 16 (sixteen Post Offices). First city of the approved Arizona batch (Phoenix, Tucson, Mesa, Gilbert, Chandler; one city at a time). Phoenix is an incorporated city in Maricopa County (Census "Phoenix city", GEOID 0455000; county Maricopa County, GEOID 04013), not a consolidated city-county. Only addresses inside Phoenix city whose official printed city is Phoenix are listed. No businesses were contacted. Brands in scope for non-Colorado states: USPS and Walmart Supercenters only. This PR is USPS only; Walmart rows are omitted because the official walmart.com store locator was unavailable.

**Counts:** 16 locations; 16 money order; 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 1 Open evenings, 14 Open weekends. The money-orders page lists 16. The after-hours page lists 14 (the fourteen offices with Saturday hours; the Phoenix Post Office on Van Buren Street also has weekday hours until 17:30). The Downtown Phoenix and Capitol Post Offices close at 17:00 or earlier and are closed on weekends, so they appear on the hub and money-orders pages but not on after-hours. No check-cashing or bill-pay page (zero listings). Holds: Laveen Post Office (1369967) and Laveen Annex (1443888). In-city, not listed (no money-order tags): Northwest, Sunnyslope, Northwest Annex, Phoenix AZ North Valley SDC, and Phoenix Rio Salado AZ S&DC.

Hours are copied as published and are local Phoenix time (Arizona Time, Mountain Standard Time; Arizona does not observe daylight saving). `last_verified` is 2026-11-14 on every row. `verification_status` is `verified_official_locator` on every row.

## Method

- **USPS:** official USPS Location Finder API (`tools.usps.com`, `requestType` po), queried with curl the same way as the Alaska cities. Pass 1: 5 and 15 miles around every Phoenix ZIP (the 71 USPS-city codes listed for Phoenix, AZ by ZIP-Codes.com from USPS data last updated 2026-11-01) and nearby official ZIPs for Glendale, Scottsdale, Tempe, Mesa, Chandler, Gilbert, Peoria, Avondale, Tolleson, Paradise Valley, Litchfield Park, Goodyear, El Mirage, Surprise, Youngtown, Cave Creek, Carefree, Buckeye, Gila Bend, Sun City, Sun City West, Laveen, Apache Junction, and Queen Creek / San Tan Valley (186 ZIPs, 372 queries, 85 unique records). Pass 2: new official ZIPs (Arlington, Black Canyon City, Cashion, Higley, Morristown, Tonopah, Waddell, Wickenburg, Wittmann, Casa Grande, Dateland) plus 1, 2, 3, 10, 20, and (on sparse edges) 50 mile widenings (177 queries, 34 added records, all far from Phoenix city). Total 119 records (`step8-browser/phoenix-usps-locator-2026-11-14.jsonl`). Official location pages were fetched for all 119 records (all HTTP 200 on the first try); each page's embedded `poDetail` matched the API record. Retail hours means the BUSINESS block only. Full notes: `step8-browser/phoenix-usps-2026-11-14.md`.
- **Walmart:** not collected. The official walmart.com store locator was unavailable, so no Walmart rows are in this PR.
- **City limits:** U.S. Census Bureau Geocoder, address endpoint and coordinates endpoint, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, Incorporated Places + CDPs + Counties. All 119 addresses and all 119 official locator map points on both benchmarks (`step8-browser/phoenix-usps-geocoder-2026-11-14.jsonl`). OpenStreetMap was not used.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands. Coordinates for USPS rows are in the notes column (lat/lng columns stay blank, as in every city CSV).

## USPS (16 listed, Domestic and Inquiry Money Orders except Sierra Adobe, which is Domestic only)

| Office | Address | Phone | Retail hours (Arizona Time) | Labels | Geocoder |
|---|---|---|---|---|---|
| Ahwatukee Post Office (1352453) | 11010 S 51st St 85044 | 480-893-1748 | Mon-Fri 08:30-16:30; Sat 10:00-13:00 | weekends | Address (both files) and point (33.346623, -111.975768): Phoenix city |
| Arcadia Post Office (1353256) | 3920 E Thomas Rd 85018 | 602-957-2693 | Mon-Fri 08:30-16:30; Sat 09:00-15:00 | weekends | Address (both files) and point (33.480979, -111.996513): Phoenix city |
| Boulder Hills Post Office (1433173) | 2550 E Rose Garden Ln 85050 | 602-494-0031 | Mon-Fri 08:30-16:30; Sat 10:00-15:00 | weekends | Address (both files) and point (33.67762, -112.027466): Phoenix city |
| Cactus Post Office (1356567) | 2901 E Greenway Rd 85032 | 602-867-3359 | Mon-Fri 08:30-16:30; Sat 09:00-14:00 | weekends | Address (both files) and point (33.625747, -112.01903): Phoenix city |
| Capitol Post Office (1356957) | 2 S 35th Ave 85009 | 602-484-0719 | Mon-Fri 08:30-16:30; Sat/Sun closed | none | Address (both files) and point (33.44713, -112.135206): Phoenix city |
| Daisy Mountain Post Office (1444552) | 44047 N 43rd Ave 85087 | 623-551-7950 | Mon-Fri 08:30-16:30; Sat 10:00-13:00 | weekends | Address (both files) and point (33.884295, -112.151394): Phoenix city |
| Downtown Phoenix Post Office (1361211) | 522 N Central Ave Lbby 85004 | 602-253-9648 | Mon-Fri 09:00-17:00; Sat/Sun closed | none | Address (both files) and point (33.454288, -112.074456): Phoenix city |
| Maryvale Post Office (1372071) | 4415 N Maryvale Pkwy 85031 | 623-848-2821 | Mon-Fri 08:30-16:30; Sat 10:00-13:00 | weekends | Address (both files) and point (33.500518, -112.17296): Phoenix city |
| Northeast Post Office (1375505) | 5021 N 20th St 85016 | 602-957-6412 | Mon-Fri 08:30-16:30; Sat 09:00-14:00 | weekends | Address (both files) and point (33.510352, -112.038194): Phoenix city |
| Osborn Post Office (1376354) | 3905 N 7th Ave 85013 | 602-235-9189 | Mon-Fri 08:30-16:30; Sat 09:00-14:00 | weekends | Address (both files) and point (33.493214, -112.08296): Phoenix city |
| Pecos Post Office (1377075) | 16825 S Desert Foothills Pkwy 85048 | 480-460-0228 | Mon-Fri 08:30-16:30; Sat 10:00-12:00 | weekends | Address (both files) and point (33.292989, -112.062652): Phoenix city |
| Phoenix Post Office (1377405) | 4949 E Van Buren St Rm 187 85026 | 602-225-3158 | Mon-Fri 08:00-17:30; Sat 09:00-17:00 | evenings, weekends | Address (both files) and point (33.449286, -111.976168): Phoenix city |
| Shaw Butte Post Office (1381372) | 12208 N 19th Ave 85029 | 602-331-4284 | Mon-Fri 08:30-16:30; Sat 09:00-14:00 | weekends | Address (both files) and point (33.597746, -112.100583): Phoenix city |
| Sierra Adobe Post Office (1381633) | 1902 W Union Hills Dr 85027 | 623-434-3580 | Mon-Fri 08:30-16:30; Sat 09:00-15:00 | weekends | Address (both files) and point (33.655491, -112.100581): Phoenix city. MONEYORDERSDOM only. |
| South Mountain Post Office (1382218) | 6825 S 7th St 85042 | 602-243-9131 | Mon-Fri 08:30-16:30; Sat 09:00-12:00 | weekends | Address (both files) and point (33.384437, -112.063663): Phoenix city |
| Washington Post Office (1386542) | 8155 N Black Canyon Hwy 85021 | 602-995-4292 | Mon-Fri 08:30-16:30; Sat 10:00-13:00 | weekends | Address (both files) and point (33.556872, -112.111733): Phoenix city |

The printed city is Phoenix, which is treated as agreeing with the Census place name "Phoenix city" only when the address and official map point also fall inside Phoenix city. Daisy Mountain is in ZIP 85087 (also the official New River ZIP); both Census files still place the address and map point in Phoenix city, not New River CDP or Anthem CDP.

### Held for Richard (not listed)

- Laveen Post Office (1369967), 9307 S 51st Ave, printed Laveen, AZ 85339. Address (both files) in Phoenix city; official map point, retried, in unincorporated Maricopa County (no place, no CDP). Held because the printed city is Laveen and the address geocodes inside Phoenix city.
- Laveen Annex (1443888), 3721 W Dobbins Rd, printed Laveen, AZ 85339. Same printed-city / address-in-Phoenix hold. No money-order tags and no BUSINESS hours.

### Left off (not holds)

- In-city, no money-order tags (print Phoenix, geocode in Phoenix city, not listed as money-order locations): Northwest (1375581), Sunnyslope (1384006), Northwest Annex (1433525), Phoenix AZ North Valley SDC (1614793), and Phoenix Rio Salado AZ S&DC (1582542).
- Nearby other-city offices, including Mesa (8), Gilbert (4), Scottsdale (4), Tempe (4), Chandler (3), Glendale (3), and the rest of the Valley and farther pass-2 offices. No Paradise Valley, Guadalupe, Anthem, Desert Hills, New River, or San Tan Valley printed office appeared. Details in `phoenix-usps-2026-11-14.md`.

## Walmart Supercenters

Not collected in this PR. The official walmart.com store locator was unavailable. No Walmart rows, no Walmart fee citations, and no Neighborhood Markets.

## Site changes in this PR

- New `data/locations/phoenix.csv` and `/phoenix/`, `/phoenix/money-orders/`, and `/phoenix/after-hours/` pages.
- Phoenix added under a new Arizona heading on the home "Start here" list and on `/cities/`, after Alaska and before Colorado. Home and `/cities/` meta descriptions now say "Anchorage, Juneau, Fairbanks, Wasilla, and Sitka, Alaska, in Phoenix, Arizona" (home) and "Phoenix, Arizona" (cities). No other city CSV or page changed. Colorado order is unchanged.
- Arizona five-city Census memo and Phoenix USPS research files are in `docs/research/`.
