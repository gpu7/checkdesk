# Step 8: Colorado Springs (2026-11-11, America/Denver)

**Rows:** 24 (9 USPS, 5 Walmart Supercenters hub-only, 10 King Soopers), including 4 rows added in the coordinate-backup follow-up below. City 1 of the approved six-city batch (Colorado Springs, Fort Collins, Thornton, Arvada, Westminster, Greeley). Only addresses inside Colorado Springs city limits are listed. No businesses were contacted.

## Method

- **USPS:** official USPS Location Finder (tools.usps.com, `locationType` PO). Searches around every Colorado Springs ZIP (80903-80911, 80915-80925, 80927, 80938, 80939, 80951) plus wider 20-mile searches from 16 of them. Each candidate's official detail page (`https://tools.usps.com/locations/details/<id>`) was opened on 2026-11-11, and the address, phone, posted retail (BUSINESS) hours, and money-order services were copied from that page.
- **City limits:** every candidate address was checked with the U.S. Census Bureau Geocoder (https://geocoding.geo.census.gov/geocoder/, Public_AR_Current / Current_Current, Incorporated Places and Census Designated Places layers) on 2026-11-11. The `city` column keeps the official mailing city.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows.

## USPS included (8)

| USPS id | Office | Address | Mon-Fri | Sat | Labels |
|---|---|---|---|---|---|
| 1439566 | Colorado Springs (main) | 201 E Pikes Peak Ave 80903 | 09:00-17:30 | 08:00-13:00 | Open evenings, Open weekends |
| 1355790 | Briargate | 8585 Criterion Dr 80920 | 09:00-17:30 | 09:00-15:00 | Open evenings, Open weekends |
| 1353145 | Antares | 2641 E Uintah St 80909 | 09:00-17:00 | 07:30-13:00 | Open weekends |
| 1357895 | Cheyenne Mountain | 1540 S 8th St 80905 | 09:00-17:30 | 08:00-13:00 | Open evenings, Open weekends |
| 1375306 | North End | 2940 N Prospect St 80907 | 09:00-17:00 | 09:30-13:00 | Open weekends |
| 1379690 | Rockrimmon | 5001 Centennial Blvd 80919 | 09:00-17:00 | 08:00-13:00 | Open weekends |
| 1384416 | Templeton | 4356 Montebello Dr 80918 | 09:00-17:30 | 08:30-14:00 | Open evenings, Open weekends |
| 1439639 | West End | 204 S 25th St 80904 | 09:00-17:00 | 08:30-13:00 | Open weekends |

All eight list Domestic and Inquiry Money Orders. Sunday is closed at every office. `money_orders=true`; check cashing, bill pay, and prepaid reload false (not listed).

## USPS excluded

- **Cimarron Hills 1440232** (5925 Galley Rd, mailing Colorado Springs 80915): geocoder places it in Cimarron Hills CDP (unincorporated El Paso County).
- **Security 1381131** (5755 Kittery Dr, mailing Colorado Springs 80911): Security-Widefield CDP.
- **Fort Carson 1363752** (1611 McDonald St, mailing Colorado Springs 80913): Fort Carson CDP.
- **General Mail Facility 1364595** (3655 E Fountain Blvd Ste 106, 80910; Mon-Fri 09:00-18:00, Sat 09:00-13:30; Domestic + Inquiry Money Orders): the Census geocoder returned no address match (with or without the suite, Current and Census 2020 benchmarks). The locator's own coordinates (38.812737, -104.759994) fall inside Colorado Springs city, but by the same rule used for Watkins in Step 6 it is not listed without a clean address match. **Flagged for review.**
- **West End Carrier Annex 1443285** (2410 Robinson St): no money-order services and no retail hours listed; carrier unit.
- Manitou Springs, Fountain, Monument, USAF Academy, Cadet, Cascade, Green Mountain Falls, Peyton, and other offices have non-Colorado Springs mailing cities and are outside the city.
- USPS contract postal units and Approved Postal Providers were not collected.

## Walmart Supercenters and King Soopers

Official store pages were opened in a browser on 2026-11-11 (read-only; no sign-in, no store contact). Raw results: `docs/research/step8-browser/colorado-springs-walmart-ks-2026-11-11.csv` and `.md` (38 rows: 16 King Soopers grocery results from 2 search pages, 17 Walmart Supercenters and 5 Neighborhood Markets from the Walmart finder's 50-mile set). Every address, including the out-of-city ones, was run through the Census geocoder (address endpoint, Public_AR_Current) on 2026-11-11. The printed city on the store page was not trusted on its own.

### Added (12 rows)

| Store | Address | Geocoder | Services listed |
|---|---|---|---|
| Walmart Supercenter 1434 | 707 S 8th St 80905 | Colorado Springs city | Money Services only: hub only, all flags false |
| Walmart Supercenter 1200 | 3201 E Platte Ave 80909 | Colorado Springs city | Money Services only: hub only, all flags false |
| Walmart Supercenter 3582 | 1575 Space Center Dr 80915 | Colorado Springs city | Money Services only: hub only, all flags false |
| Walmart Supercenter 1896 | 8250 Razorback Rd 80920 | Colorado Springs city | Money Services only: hub only, all flags false |
| King Soopers 00006 Westside Uintah | 1750 W Uintah St 80904 | Colorado Springs city | Money orders |
| King Soopers 00133 Centennial Blvd and Fillmore | 3250 Centennial Blvd 80907 | Colorado Springs city | Money orders |
| King Soopers 00058 Cheyenne Meadows Center | 815 Cheyenne Meadows Rd 80906 | Colorado Springs city | Money orders |
| King Soopers 00103 Hancock Plaza | 2910 S Academy Blvd 80916 | Colorado Springs city | Money orders |
| King Soopers 00076 Hartsel Drive | 3570 Hartsel Dr 80920 | Colorado Springs city | Money orders |
| King Soopers 00119 Briargate | 9225 N Union Blvd 80920 | Colorado Springs city | Money orders |
| King Soopers 00151 Flying Horse | 2731 N Gate Blvd 80921 | Colorado Springs city (matched as "2731 N Gate Rd"; same number, street, ZIP) | Check cashing, money orders |
| King Soopers 00130 Academy and Austin Bluffs | 3620 Austin Bluffs Pkwy 80918 | Colorado Springs city | Money Services only: hub only, all flags false |

- **Hours:** Walmart rows use the store hours (Mon-Sun 6am-11pm), not sensory-friendly or holiday lines; the Nov 26 holiday closure is in `hours_notes`. King Soopers rows use store hours (Sun-Sat 6 AM-11 PM), never pharmacy or fuel hours. All 12 are labeled Open evenings and Open weekends, but the hub-only rows do not appear on the evenings/weekends page because they list no service.
- **Walmart:** every Colorado Springs Supercenter page showed only the generic "Money Services" label; check cashing, money orders, bill pay, and load/unload were not named. All four flags are false; the stores are hub-only with "call ahead" copy. Chain fees are not applied to them.
- **King Soopers:** `money_orders=true` only where the page tagged "Money Orders". Flying Horse is the only page that tagged "Check Cashing", so it is the only `check_cashing=true` row and the only entry on the new `/colorado-springs/check-cashing/` page. It also lists Western Union, which is recorded in notes and not mapped to a service flag. No page tagged bill pay or prepaid reload, so there is no bill-pay page.
- No new fee rows. King Soopers fees stay "Not published, call ahead."

### Held: printed Colorado Springs, but no Census address match (flagged for Richard)

The Census address geocoder returned no match (one-line and parsed, with and without ZIP). As a secondary check only, OpenStreetMap Nominatim coordinates for each address were run through the Census coordinates endpoint. They are **not listed** pending a decision, by the same rule as Watkins (Step 6) and the General Mail Facility above:

| Store | Address | Coordinate check (Census boundaries on an OSM point) | Services on page |
|---|---|---|---|
| King Soopers 00053 Woodmen and Academy | 6930 N Academy Blvd 80918 | inside Colorado Springs city | Money orders |
| King Soopers 00098 Stetson Hills | 6030 Stetson Hills Blvd 80923 | inside Colorado Springs city | Money orders |
| Walmart Supercenter 5123 | 5550 E Woodmen Rd 80920 | inside Colorado Springs city (address geocoder only offered "5550 Woodmen Ridge Vw", a different street; rejected) | Money Services only |
| King Soopers 00134 Constitution Avenue | 7915 Constitution Ave 80951 | **outside any incorporated place** (unincorporated El Paso County) | Money Services only |

00134 should stay off. If Richard accepts a coordinate-based check, 00053, 00098, 5123, and the General Mail Facility could be added in a follow-up.

### King Soopers 00077 "Monument" (flagged, not listed)

The official page prints 1070 W Baptist Rd, Colorado Springs, CO 80921, and its heading says Monument. The Census geocoder matches the address inside **Monument town**, not Colorado Springs city. Monument is not an approved city, so the store is not listed anywhere. It tags Money Orders.

### Left out

- Walmart Neighborhood Markets 3176 (1725 N Union Blvd), 3082 (1622 S Academy Blvd), 3083 (665 N Murray Blvd), 3175 (4142 Austin Bluffs Pkwy). All geocode inside Colorado Springs, but Neighborhood Markets are out of scope, and their pages did not show Money Services. Pueblo NM 5828 is out of area.
- Out of city (printed city confirmed by the geocoder where it matched): Walmart 3018 Fountain Venetucci Blvd (printed Fountain 80906; no address match), 1273 Fountain, 4335 Falcon (unincorporated), 3805 Woodland Park, 3227 Monument, 1019 Canon City, 3382 Pueblo West, 842 and 1001 Pueblo, 4639 Elizabeth, 984 Castle Rock, 2892 Parker; King Soopers 00153 Fountain, 00147 Falcon, 00431 Woodland Park, 00417 Canon City.
- Fuel centers are not separate rows.

### Coverage limits

King Soopers search: 16 grocery results on 2 pages, all opened. Walmart finder: one 50-mile result set of 22, all opened.

## Not collected

- Payday / title-loan storefronts, including ACE: omitted by policy.
- Stand-alone Western Union / MoneyGram agents and other grocery brands were not collected. City Market was noted only in passing by the browser pass; no money-service pages were read for it, and no new brand was added.

## Follow-up: coordinate-backup inclusion approved (2026-11-11)

Richard approved adding the four held locations on 2026-11-11. Each printed a Colorado Springs address, the Census address geocoder returned no match, and a Census coordinates lookup placed the point inside Colorado Springs city limits (OpenStreetMap Nominatim points for the three stores; the official USPS locator point 38.812737, -104.759994 for the General Mail Facility). No new official pages were read for services; flags, hours, and phones come from the 2026-11-11 official-page records above and in `step8-browser/` (USPS phone and hours re-read from the official locator data on 2026-11-11). `last_verified` is 2026-11-11, and each row's notes record the placement method.

| Row | Address | Services (official page) | Hours used | Labels |
|---|---|---|---|---|
| King Soopers 00053 Woodmen and Academy | 6930 N Academy Blvd 80918 | Money orders | Store Sun-Sat 6 AM-11 PM | Open evenings, Open weekends |
| King Soopers 00098 Stetson Hills | 6030 Stetson Hills Blvd 80923 | Money orders | Store Sun-Sat 6 AM-11 PM | Open evenings, Open weekends |
| Walmart Supercenter 5123 | 5550 E Woodmen Rd 80920 | Money Services only: hub only, all flags false, no fee applied | Store Mon-Sun 6am-11pm (Nov 26 closure in notes) | Open evenings, Open weekends (not on evenings/weekends page) |
| USPS General Mail Facility 1364595 (retail counter) | 3655 E Fountain Blvd Ste 106 80910 | Domestic + Inquiry Money Orders | Mon-Fri 09:00-18:00, Sat 09:00-13:30, Sun closed | Open evenings, Open weekends |

Still off: King Soopers 00134 Constitution Avenue (map point outside city limits) and King Soopers 00077 Monument (geocoder places it in Monument town). The hub's "not listed yet" copy no longer names the four added locations, and the hub, money-order, and evenings/weekends pages note the coordinate method.
