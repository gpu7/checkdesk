# Step 8: Littleton (2026-11-12, America/Denver)

**Rows:** 3 (1 Post Office, 2 King Soopers). City 5 of the batch approved on 2026-11-12 (Loveland, Broomfield, Grand Junction, Parker, Littleton; ranked from Census Vintage 2025, SUB-IP-EST2025-POP-08). Only addresses inside the City of Littleton (incorporated place, "Littleton city" in the Census geocoder; Arapahoe County for all three rows) are listed. No businesses were contacted.

**Counts:** 3 locations; 2 money orders (Littleton Post Office and King Soopers 00122 Mineral and Broadway); 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 2 Open evenings, 3 Open weekends. The evenings/weekends page lists the 2 money-order locations (1 Open evenings, 2 Open weekends). King Soopers 00131 Littleton and Broadway is hub-only ("Money Services, call ahead"), the same treatment as King Soopers 00111 Fresh Fare in Englewood. No check-cashing or bill-pay page (zero listings).

## Method

- **USPS:** official USPS Location Finder (tools.usps.com, `locationType` PO), same method as Parker/Grand Junction/Broomfield. Searches at 5 and 15 miles around ZIPs 80120, 80122, 80123, 80127, 80128 (Littleton mailing ZIPs), 80125, and 80129 returned 57 Post Office records (`docs/research/step8-browser/littleton-usps-locator-2026-11-12.jsonl`). Four records print Littleton (Littleton 1370671, Columbine Hills 1358798, Ken Caryl Ranch 1432798, and the Littleton CO Kn Cl Ranch SDC 1613887); a fifth, the Littleton CO Highlands SDC 1613886, prints Highlands Ranch. The Littleton office's official location page (`https://tools.usps.com/locations/details/1370671`) was loaded on 2026-11-12 (HTTP 200) and shows Money Orders (Domestic, Inquiry); hours and services come from the same official locator record that page displays.
- **City limits:** every candidate address was checked with the U.S. Census Bureau Geocoder (https://geocoding.geo.census.gov/geocoder/, address endpoint, Public_AR_Current / Current_Current, Incorporated Places, Census Designated Places and Counties layers) on 2026-11-12. Raw results: `littleton-usps-geocoder-2026-11-12.jsonl` (all 57 Post Office records) and `littleton-stores-geocoder-2026-11-12.jsonl` (all 67 store rows in the research CSV).
- **Fallback checks:** Census 2020 benchmark (Public_AR_Census2020) and current one-line lookups for every Littleton-printed address (including those with no current-file match), and current-benchmark coordinates lookups of every official USPS locator point. Raw results: `littleton-geocoder-fallback-2026-11-12.jsonl`. No listed row used a fallback; all three listed rows matched inside Littleton city on both the current and 2020 address files.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands.

## USPS

| Office | Address | Geocoder | Services | Retail hours |
|---|---|---|---|---|
| Littleton (1370671) | 5753 S Prince St 80120 | Littleton city (5753 S PRINCE ST, LITTLETON, CO, 80120; Arapahoe County); 2020 file and official locator point (39.612975, -105.016656) also Littleton city | Domestic and Inquiry Money Orders | Mon-Fri 09:00-17:00, Sat 09:00-13:00, Sun closed |

- Littleton Post Office: Open weekends (Saturday hours). Not Open evenings: weekday retail hours close at 17:00. Phone 303-795-7346.
- No duplicate record appeared at the Littleton address.

### Printed Littleton, outside the city (held, not added)

The official printed city (Littleton) and the Census results disagree, so these are not listed, by the same rule as Grand Junction's Fruitvale Post Office:

- **Columbine Hills (1358798)**, 6698 S Iris St, Littleton 80123; Domestic and Inquiry Money Orders; Mon-Fri 09:00-17:30, Sat 09:00-13:00. No address match on the current or 2020 file; the official locator point (39.596008, -105.104854) returns **Ken Caryl CDP** (Jefferson County), no incorporated place.
- **Ken Caryl Ranch (1432798)** and its duplicate record **Littleton CO Kn Cl Ranch SDC (1613887)**, same building at 8200 Shaffer Pkwy, Littleton 80127 (one building); Domestic and Inquiry Money Orders on both records; Mon-Fri 09:00-18:00, Sat 09:00-13:00. No match on the current file; the 2020 file matches 8200 SHAFFER PKWY in **Ken Caryl CDP**, and both official locator points return Ken Caryl CDP.

### Out of the city (left off, not held)

Printed another place, and the geocoder agrees it is outside Littleton: Englewood 1362625 and Downtown Englewood 1362621 (Englewood city); Centennial 1439625 and Tower 1432755 (Centennial city; already listed under Centennial, not changed); Highlands Ranch 1439610 and Littleton CO Highlands SDC 1613886 (same building, Highlands Ranch CDP; the SDC record lists no money orders); Greenwood Village 1439554; Bear Valley 1354325 and the other Denver offices (Denver city); Glendale 1440283; Lakewood 1439615 and Lakewood CO SDC 1612989 (no address match; official locator points return Lakewood city); Edgewater 1439601; the Aurora, Arvada, Golden, Wheat Ridge, Westminster (Harris Park), Parker, and Castle Rock offices (their own cities; Castle Rock 1357260 not changed); Morrison 1373847 (no place on the address match; locator point returns Morrison town); and the Conifer, Evergreen, Idledale, Indian Hills, Kittredge, Louviers, Sedalia, and Buffalo Creek offices (CDPs or unincorporated). No Post Office printed with another city geocodes inside Littleton. USPS contract postal units and Approved Postal Providers were not collected.

## King Soopers and Walmart

Official store pages were opened in a browser on 2026-11-12 (read-only; no sign-in, no store contact). Raw results: `docs/research/step8-browser/littleton-walmart-ks-2026-11-12.csv` and `.md` (67 rows: 48 King Soopers, 19 Walmart). The eight Littleton-printed pages (six King Soopers, two Walmart Supercenters) were opened fresh, along with nine nearby King Soopers pages and Walmart Englewood 2751 and Denver 5676; the other 48 nearby rows were copied from the same-day Parker, Castle Rock, and Centennial research files. The King Soopers Littleton locator returned 32 results; one was a fuel center (Green Mountain Fuel, 198 S Union Blvd, Lakewood), not a row. The Walmart store finder returned no stores for "Littleton, CO"; Walmart's official Colorado and Littleton store directories listed two Littleton Supercenters. No unexpected grocery or retail brands appeared. Every address was run through the Census geocoder on 2026-11-12.

### Added (2 store rows)

| Store | Address | Geocoder | Services listed | Store hours |
|---|---|---|---|---|
| King Soopers 00122 Mineral and Broadway | 7901 S Broadway 80122 | Littleton city (7901 S BROADWAY, LITTLETON, CO, 80122; Arapahoe County; 2020 file agrees) | Money orders (and Money Services) | Sun-Sat 6 AM-11 PM |
| King Soopers 00131 Littleton and Broadway | 100 W Littleton Blvd 80120 | Littleton city (100 W LITTLETON BLVD, LITTLETON, CO, 80120; Arapahoe County; 2020 file agrees) | Generic "Money Services" only (hub-only); money orders not tagged | Sun-Sat 6 AM-11 PM |

- Phones from the official pages: 00122 303-738-5700; 00131 303-615-3000.
- **Hours:** store hours only. Pharmacy, fuel, sensory-friendly, and holiday hours not used. Both are Open evenings and Open weekends (the hub-only store carries the labels on the hub only).
- **Services:** service flags follow only the tags on each page. Mineral and Broadway tags "Money Orders" and "Money Services" (`money_orders=true`). Littleton and Broadway tags "Money Services" but not "Money Orders", so all four flags are false and it is on the hub only, not on the money-order or evenings-and-weekends pages. No check cashing, bill pay, prepaid reload, or Western Union on either page. "Account Funding" is not a tracked service and is not flagged. King Soopers fees stay "Not published, call ahead."

### Printed Littleton, outside the city (held, not added)

Each official page prints Littleton, but the Census geocoder places the address outside Littleton city on the current file (and the 2020 file where it matched). Official printed city and geocoder disagree, so none is listed:

| Store | Address | Current file | 2020 file | Services on page |
|---|---|---|---|---|
| King Soopers 00041 Coalmine and Pierce | 6760 S Pierce St 80128 | Columbine CDP, Jefferson County | Columbine CDP | Money orders |
| King Soopers 00078 Columbine Knolls Village | 8126 S Wadsworth Blvd 80128 | Columbine CDP, Jefferson County | Columbine CDP | Money orders |
| King Soopers 00050 Governors Plaza | 9820 W Belleview Ave 80123 | No place or CDP, Jefferson County (matched as 9820 W BELLEVIEW ST, same number and ZIP) | Same | Money orders |
| King Soopers 00025 Ken Caryl (printed "KEN CARYL") | 11747 W Ken Caryl Ave 80127 | Ken Caryl CDP, Jefferson County | Ken Caryl CDP | Money orders |
| Walmart Supercenter 1308 (Littleton W Quincy Ave Supercenter) | 7700 W Quincy Ave 80123 | **Denver city**, Denver County | No match | Generic Money Services only |
| Walmart Supercenter 5049 (Littleton W Coal Mine Ave Supercenter) | 13420 W Coal Mine Ave 80127 | Dakota Ridge CDP, Jefferson County | No match | Generic Money Services only |

Map points from the King Soopers and Walmart pages were not read; they are not needed, since no row is added on the address results alone and each address matched outside the city.

### Left out (not held)

- **Englewood** (Englewood city): King Soopers 00065, 00109, 00111; Walmart Supercenter 2751.
- **Denver** (Denver city): King Soopers 00001, 00007, 00019 Bear Valley (3100 S Sheridan Blvd), 00026, 00029, 00035, 00056, 00072, 00150; Walmart Supercenter 5676. Walmart Supercenter 3566 (9400 E Hampden Ave, printed Denver) geocodes in Aurora city, not Littleton.
- **Lakewood** (Lakewood city): King Soopers 00031, 00040, 00059, 00127; Walmart Supercenters 2125, 4284.
- **Centennial** (Centennial city; already listed under Centennial, not changed): King Soopers 00016, 00047, 00063; Walmart Supercenter 3313.
- **Highlands Ranch** (unincorporated CDP; printed city and geocoder agree): King Soopers 00008, 00027, 00108, 00110; Walmart Supercenter 1252.
- **Greenwood Village** (00096, 00100), **Glendale** (00124), **Castle Pines** (00091), **Castle Rock** (00125, 00132; Walmart 984; not changed), **Parker** (00075, 00088, 00126, 00175; Walmart 2892; not changed), and **Aurora** (00010, 00014, 00030, 00049, 00069, 00084, 00107, 00128, 00139; Walmart Supercenters 1492, 1689, 5137, 5334): their own cities.
- **Walmart Neighborhood Markets** (excluded by standing policy): Aurora 4196, Aurora 3740, Centennial 3126, Denver 3128 (1442 S Parker Rd; Four Square Mile CDP). None prints Littleton.
- Fuel centers (Green Mountain Fuel; Aurora Fuel at 19001 E Quincy Ave and 1369 S Havana St) are not separate rows.
- No store or Post Office printed with another city geocodes inside Littleton, so there is no reverse-check hold.

## Not collected

- Payday / title-loan storefronts, including ACE: omitted by policy.
- Stand-alone Western Union / MoneyGram agents and other grocery brands were not collected.
- Thornton's held Eastlake Post Office and Walmart 4567, the Castle Rock Post Office, and Grand Junction's held Fruitvale Post Office were not touched. City Market was not added.
