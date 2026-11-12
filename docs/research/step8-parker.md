# Step 8: Parker (2026-11-12, America/Denver)

**Rows:** 5 (1 Post Office, 3 King Soopers, 1 Walmart Supercenter). City 4 of the batch approved on 2026-11-12 (Loveland, Broomfield, Grand Junction, Parker, Littleton; ranked from Census Vintage 2025, SUB-IP-EST2025-POP-08). Only addresses inside the Town of Parker (incorporated place, "Parker town" / Douglas County in the Census geocoder) are listed. No businesses were contacted.

**Counts:** 5 locations; 4 money orders (Parker Post Office and 3 King Soopers); 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 5 Open evenings, 5 Open weekends. The evenings/weekends page lists the 4 money-order locations (4 Open evenings, 4 Open weekends). The Walmart Supercenter is hub-only ("Money Services, call ahead"). No check-cashing or bill-pay page (zero listings).

## Method

- **USPS:** official USPS Location Finder (tools.usps.com, `locationType` PO), same method as Grand Junction/Broomfield/Castle Rock. Searches at 5 and 15 miles around ZIPs 80134 and 80138 (Parker) and 80016 and 80112 (north and west of town) returned 41 Post Office records (`docs/research/step8-browser/parker-usps-locator-2026-11-12.jsonl`). Only one record prints Parker. Its official location page (`https://tools.usps.com/locations/details/1376837`) was loaded on 2026-11-12 (HTTP 200) and shows Money Orders; hours and services come from the same official locator record that page displays.
- **City limits:** every candidate address was checked with the U.S. Census Bureau Geocoder (https://geocoding.geo.census.gov/geocoder/, address endpoint, Public_AR_Current / Current_Current, Incorporated Places, Census Designated Places and Counties layers) on 2026-11-12. Raw results: `parker-usps-geocoder-2026-11-12.jsonl` (all 41 Post Office records) and `parker-stores-geocoder-2026-11-12.jsonl` (all 47 store rows in the research CSV).
- **Fallback checks:** Census 2020 benchmark (Public_AR_Census2020) one-line lookups for every address with no current-file match, and current-benchmark coordinates lookups of official USPS locator points (Parker, Sedalia, Elizabeth, Watkins, Columbine Hills, Ken Caryl Ranch and its SDC). Raw results: `parker-geocoder-fallback-2026-11-12.jsonl`. No listed row used a fallback; every listed row matched inside Parker town on the current address file.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands.

## USPS

| Office | Address | Geocoder | Services | Retail hours |
|---|---|---|---|---|
| Parker (1376837) | 18695 Pony Express Dr 80134 | Parker town (18695 PONY EXPRESS DR, PARKER, CO, 80134; Douglas County); official locator point (39.522141, -104.771892) also Parker town | Domestic and Inquiry Money Orders | Mon-Fri 08:30-18:00, Sat 09:00-12:00, Sun closed |

- Parker Post Office: Open evenings (closes 18:00 on weekdays) and Open weekends. Phone 303-805-2109.
- No other Post Office record prints Parker, and no duplicate record appeared at the Parker address. (Duplicates elsewhere, such as Highlands Ranch 1439610 and the Littleton CO Highlands SDC 1613886 at 9609 S University Blvd, Aurora 1353711 and Aurora CO SDC 1613885 at 16890 E Alameda Pkwy, and Ken Caryl Ranch 1432798 and its SDC 1613887 at 8200 Shaffer Pkwy, are outside Parker.)

### Out of town (left off, not held)

Printed another place, and the geocoder agrees it is outside Parker: Franktown 1364042 (Franktown CDP); Tower 1432755 and Centennial 1439625 (Centennial city, already listed under Centennial; not changed); Highlands Ranch 1439610 and Littleton CO Highlands SDC 1613886 (Highlands Ranch CDP); Greenwood Village 1439554 (Greenwood Village city); Castle Rock 1357260 and Castle Rock Annex 1577757 (Castle Rock town; not changed); Elizabeth 1362284 (no address match on the current or 2020 file; official locator point returns Elizabeth town); Sedalia 1381134 (2020 file and official locator point both return Sedalia CDP); Louviers 1371030 (Louviers CDP); Watkins 1386636 (no address match; official locator point returns Aurora city); the Aurora offices (Aurora, Aurora CO SDC, Gateway, Buckingham, Hoffman Heights, Altura, Fletcher; Aurora city); Littleton 1370671 (Littleton city); Columbine Hills 1358798 (no address match; official locator point returns Ken Caryl CDP); Ken Caryl Ranch 1432798 and SDC 1613887 (2020 file and official locator point return Ken Caryl CDP); Englewood and Downtown Englewood (Englewood city); Glendale 1440283 (Glendale city); and the Denver offices (Denver city). No Post Office printed with another city geocodes inside Parker. USPS contract postal units and Approved Postal Providers were not collected.

## King Soopers and Walmart

Official store pages were opened in a browser on 2026-11-12 (read-only; no sign-in, no store contact). Raw results: `docs/research/step8-browser/parker-walmart-ks-2026-11-12.csv` and `.md` (47 rows: 32 King Soopers, 15 Walmart). The five Parker-printed pages were opened fresh; the 42 nearby out-of-town rows were copied from the same-day Castle Rock and Centennial research files (`castle-rock-walmart-ks-2026-11-12.csv`, `centennial-walmart-ks-2026-11-12.csv`). The King Soopers locator returned 33 results for "Parker, CO"; one was a fuel center (Aurora Fuel 00630), not a row. No unexpected grocery or retail brands appeared. Every address was run through the Census geocoder on 2026-11-12.

### Added (4 store rows)

| Store | Address | Geocoder | Services listed | Store hours |
|---|---|---|---|---|
| King Soopers 00075 Stroh Ranch | 12959 S Parker Rd 80134 | Parker town (12959 PARKER RD, PARKER, CO, 80134) | Money orders (and Money Services) | Sun-Sat 6 AM-11 PM |
| King Soopers 00088 Crossing at Stonegate | 17031 Lincoln Ave 80134 | Parker town (17031 E LINCOLN AVE, PARKER, CO, 80134) | Money orders (and Money Services) | Sun-Sat 6 AM-11 PM |
| King Soopers 00126 Cottonwood Drive | 17761 Cottonwood Dr 80134 | Parker town (17761 COTTONWOOD DR, PARKER, CO, 80134) | Money orders (and Money Services); page also lists Western Union | Sun-Sat 6 AM-11 PM |
| Walmart Supercenter 2892 (Parker Supercenter) | 11101 S Parker Rd 80134 | Parker town (11101 S PARKER RD, PARKER, CO, 80134) | Generic "Money Services" only (hub-only) | Mon-Sun 6am-11pm |

- Phones from the official pages: 00075 303-840-1223; 00088 720-851-7750; 00126 303-334-9540; Walmart 2892 303-805-0029.
- **Spelling/geocoder notes:** the Stroh Ranch page prints "12959 S Parker Rd"; the geocoder returns "12959 PARKER RD" (same number, street, and ZIP). The Crossing at Stonegate page prints "17031 Lincoln Ave"; the geocoder returns "17031 E LINCOLN AVE". Rows keep the printed form.
- **Hours:** store hours only. Pharmacy, fuel, sensory-friendly, and holiday hours not used. All four are Open evenings and Open weekends.
- **King Soopers:** the three listed pages tag "Money Orders" and "Money Services" (`money_orders=true`). No check cashing, bill pay, or prepaid reload named. Cottonwood Drive also lists Western Union; that is noted in the row and not mapped to a service flag. "Account Funding" is not a tracked service and is not flagged. King Soopers fees stay "Not published, call ahead."
- **Walmart:** the Parker Supercenter page shows only a generic "Money Services" label; check cashing, money orders, bill pay, and load/unload are not named, so all four flags are false. It is on the Parker hub only, labeled to call ahead, and not on the money-order or evenings-and-weekends pages. Walmart chain fee maximums are not applied. The page does not mention Western Union.

### Held for Richard

None. Every Parker-printed candidate with a money service geocodes inside Parker town on the current address file, and no candidate printed with another city geocodes inside Parker. (Thornton's held Eastlake Post Office and Walmart 4567, the Castle Rock Post Office, and Grand Junction's held Fruitvale Post Office were not touched.)

### Left out

- **King Soopers 00175 Parker** (6755 Prospector Ln, printed Parker CO 80134; 24 hours; phone 303-285-7000): its official store page, opened 2026-11-12, lists no Money Services tag and no tracked service, so it has no row whatever its city-limit status. The Census geocoder found no address match on the current or 2020 address file (`parker-geocoder-fallback-2026-11-12.jsonl`). An official map point could not be read from the King Soopers page by script (the site refused the non-browser request), so city limits are unresolved. Because there is nothing to list, this is recorded as a no-services omission, not a hold. (Supplementary, non-official observation from the Castle Rock pass: an OpenStreetMap point for this store returned unincorporated Douglas County. It was not used as the basis for this decision.)
- **Highlands Ranch** (unincorporated CDP; printed city and geocoder agree): King Soopers 00008 Wildcat Reserve, 00027 University and Colorado, 00108 Red Cedar Drive, 00110 Quebec St Highland Ranch; Walmart Supercenter 1252 (6675 Business Center Dr).
- **Castle Pines** (separate city): King Soopers 00091 Castle Pines (7284 Lagae Rd).
- **Castle Rock** (Castle Rock town; already listed under Castle Rock, not changed): King Soopers 00125 Promenade Parkway, 00132 Ridge Road; Walmart Supercenter 984.
- **Aurora** (Aurora city): King Soopers 00010 Village Green, 00014 Peoria Street, 00030 Havana and Mississippi, 00049 Iliff at Buckley, 00069 Quincy Place Mission Viejo, 00084 Arapahoe Crossing (6412 S Parker Rd), 00107 Smoky Hill and Arapahoe, 00128 Hampden Crossing, 00139 Nine Mile; Walmart Supercenters 1492, 1689, 5137, 5334.
- **Centennial** (Centennial city; already listed under Centennial, not changed): King Soopers 00016, 00047, 00063; Walmart Supercenter 3313.
- **Elizabeth:** Walmart Supercenter 4639 (2100 Legacy Cir, printed Elizabeth); the geocoder matched 2100 LEGACY LOOP, ELIZABETH, CO, 80107 in Elbert County with no place or CDP. Not in Parker.
- **Englewood** (Englewood city): King Soopers 00065, 00109, 00111; Walmart Supercenter 2751.
- **Littleton-printed** (Littleton city, or Ken Caryl, Columbine, Dakota Ridge CDPs, unincorporated Jefferson County, or Denver city): King Soopers 00025, 00041, 00050, 00078, 00122, 00131; Walmart Supercenters 1308 (geocodes Denver city) and 5049. Littleton itself is a later city and was not built here.
- **Walmart Neighborhood Markets** (excluded by standing policy): Centennial 3126, Aurora 4196, Aurora 3740 (21475 E Quincy Ave; no place or CDP, Arapahoe County). None prints Parker.
- Fuel centers (Aurora Fuel 00630, and fuel centers mentioned on the Stroh Ranch and Cottonwood Drive pages) are not separate rows.

## Not collected

- Payday / title-loan storefronts, including ACE: omitted by policy.
- Stand-alone Western Union / MoneyGram agents and other grocery brands were not collected.
