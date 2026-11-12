# Step 8: Fountain (2026-11-12, America/Denver)

**Rows:** 3 (1 Post Office, 2 Walmart Supercenters). City 6 of the batch approved on 2026-11-12 (Brighton, Windsor, Erie, Northglenn, Lafayette, Fountain, Evans, Johnstown, Montrose, Louisville; ranked from Census Vintage 2025, SUB-IP-EST2025-POP-08, where Fountain is rank 28 at 29,450). Fountain is a city in El Paso County; only addresses inside Fountain city limits ("Fountain city" in the Census geocoder; El Paso County) are listed. No businesses were contacted.

**Counts:** 3 locations; 1 money orders (Fountain Post Office); 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 2 Open evenings, 3 Open weekends. Hub-only rows: 2 (Walmart Supercenters 1273 and 3018, "Money Services, call ahead"). The money-orders page lists 1 location. The evenings/weekends page lists the 1 money-order location (0 Open evenings, 1 Open weekends); the two Walmart Supercenters are hub-only and do not appear there. No check-cashing or bill-pay page (zero listings). No holds.

## Method

- **USPS:** official USPS Location Finder (tools.usps.com, `requestType` po), same method as Lafayette, Northglenn, Erie, Windsor, and Brighton. Searches at 5 and 15 miles around 80817 (Fountain), 80911 (Security-Widefield), 80906, 80910, 80916, 80913 (Fort Carson), 80925, 80929, 80840, 80908, 80926, 80902, 80809, 80864, 80808, 80915, 80909, 80903, 80905, 80914, 80930, plus a second pass over 80918, 80920, 80922, 80923, 80927, 80938, 80939, 80951, 80907, 80904, 80919, 80831, 80921, 80917, 81008, and 80928, returned 38 unique Post Office records (`docs/research/step8-browser/fountain-usps-locator-2026-11-12.jsonl`; pass notes in `fountain-usps-2026-11-12.md`). Official location pages were fetched on 2026-11-12, each on the first try: 1363906 Fountain, 1381131 Security, and 1363752 Fort Carson (all HTTP 200). Hours and services come from the same official locator record those pages display; retail hours means the BUSINESS hours block only.
- **City limits:** every candidate address was checked with the U.S. Census Bureau Geocoder (https://geocoding.geo.census.gov/geocoder/, address endpoint, Public_AR_Current / Current_Current, Incorporated Places, Census Designated Places and Counties layers) on 2026-11-12. Raw results: `fountain-usps-geocoder-2026-11-12.jsonl` (all 38 Post Office records) and `fountain-stores-geocoder-2026-11-12.jsonl` (all 7 in-scope King Soopers and Walmart Supercenter rows in the research CSV; the two Neighborhood Markets were not geocoded because they are excluded by policy).
- **Fallback checks:** Census 2020 benchmark (Public_AR_Census2020) and current one-line lookups for the Fountain Post Office (101 S Santa Fe Ave); for the left-out Security, Fort Carson, and General Mail Facility addresses; for Walmart 1273 address variants of 6310 S Us Highway 85-87; for Walmart 3018 address variants (`4425 Venetucci Blvd` and `4425 Venetucci Boulevard`, Fountain CO 80906, Fountain CO 80817, and Colorado Springs CO 80906); and for King Soopers 00153 address variants (`6255 Sawcut Pt`, `6255 Sawcut Point`, `6255 Saw Cut Pt`, `6255 Saw Cut Point`, and `6255 Sawcut Pt.`, Fountain CO 80817). Current-benchmark coordinates lookups of the official USPS locator map point for 1363906, and of the official store-page map points for Walmart 1273 (38.740386, -104.736809), Walmart 3018 (38.768632, -104.781091), Walmart 1434, Walmart 1200 (JSON-LD / `geoPoint` on each official Walmart store page, read 2026-11-12; not collected from OpenStreetMap), and King Soopers 00153 (Bing Maps `cp=` embed on its official King Soopers store page, 38.7204448, -104.71195, read 2026-11-12). Raw results: `fountain-geocoder-fallback-2026-11-12.jsonl`. One listed row relies on the fallback: Walmart Supercenter 3018 (below). OpenStreetMap points were not used for any decision. The listed Post Office and Walmart 1273 match the current file, the 2020 file, and their official map points, all in Fountain city.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands.

## USPS

| Office | Address | Geocoder | Services | Retail hours |
|---|---|---|---|---|
| Fountain (1363906) | 101 S Santa Fe Ave 80817 | Fountain city (101 S SANTA FE AVE, FOUNTAIN, CO, 80817; El Paso County). 2020 file agrees; official locator point (38.682837, -104.705178) also Fountain city | Domestic and Inquiry Money Orders | Mon-Fri 08:00-17:00, Sat 09:00-13:00, Sun closed |

- Fountain Post Office: Open weekends (Saturday). Weekday retail closes at 17:00, so no Open evenings label. Phone 719-382-4623. URL https://tools.usps.com/locations/details/1363906. verification_status `verified_official_locator`. Window service hours match retail hours. Lobby and PO box access listed 00:01-23:59 daily are not retail and are not used. Last collection Mon-Fri 17:00, Sat 15:15 is not retail. Other listed services (parcel lockers, general delivery, PO boxes, burial flags, duck stamps, greeting cards) are not Check Desk tracked services. No passport service and no self-service kiosk listed. No duplicate, annex, or SDC record at 101 S Santa Fe Ave.

### Left out (not held)

- **Security 1381131** (5755 Kittery Dr, printed Colorado Springs 80911, 719-390-3192): money orders and passports; Mon-Fri 09:00-17:00, Sat 08:00-14:00. Current and 2020 files: **Security-Widefield CDP** (unincorporated El Paso County); official locator map point agrees. Printed another city and outside Fountain, so left out, not held. Page HTTP 200.
- **Fort Carson 1363752** (1611 McDonald St, printed Colorado Springs 80913, 719-579-9617): money orders; Mon-Fri 09:00-16:30, Sat 09:30-12:00. Current and 2020 files: **Fort Carson CDP**; official locator map point agrees. Left out, not held. Page HTTP 200.
- **General Mail Facility 1364595** (3655 E Fountain Blvd Ste 106, Colorado Springs 80910): money orders, Mon-Fri to 18:00. No address match in the current or 2020 file; official locator map point is in Colorado Springs city. Already handled on the Colorado Springs page. Left out here; `colorado-springs.csv` was not edited. The street name "Fountain Blvd" is not the city.
- **West End Carrier Annex 1443285** (2410 Robinson St, Colorado Springs 80904): no retail hours and no money orders; Colorado Springs city. Left out. It does not share a building with West End 1439639.
- Other Colorado Springs-printed offices (all money orders, all Colorado Springs city unless noted): Cimarron Hills 1440232 (Cimarron Hills CDP), Cheyenne Mountain 1357895, Antares 1353145, Colorado Springs main 1439566, North End 1375306, West End 1439639, Templeton 1384416, Rockrimmon 1379690, Briargate 1355790.
- Farther towns, each in its own municipality, CDP, or unincorporated area: Manitou Springs, Cascade (Cascade-Chipita Park CDP), USAF Academy and Cadet (Air Force Academy CDP), Green Mountain Falls, Peyton (CDP), Monument, Palmer Lake, Woodland Park and Tamarac, Elbert (CDP), Larkspur, Victor, Penrose (CDP), Cripple Creek, Divide/Yoder/Rush (matched, unincorporated), Calhan, Ramah, and Pueblo/Belmont/Midtown/Sunset (Pueblo city; Midtown had no address match, locator point in Pueblo city).
- No office in the sweep is printed Fountain besides 1363906. No record printed with another city falls inside Fountain city by address geocode or by locator map point. USPS contract postal units and Approved Postal Providers were not collected.

## King Soopers and Walmart

Official store pages were opened in a browser on 2026-11-12 (read-only; no sign-in, no store contact). Raw results: `docs/research/step8-browser/fountain-walmart-ks-2026-11-12.csv` and `.md` (9 rows: 3 King Soopers, 4 Walmart Supercenters, 2 Walmart Neighborhood Markets excluded by policy). The official King Soopers city directory `/stores/grocery/co/fountain` lists one grocery store in Fountain. Walmart's official store finder for 80817 lists two Supercenters that print Fountain (1273 and 3018). No unexpected grocery or retail brands appeared (no City Market). All 7 in-scope Supercenter and King Soopers addresses were run through the Census geocoder on 2026-11-12; 5 matched the current file. Walmart 3018 and King Soopers 00153 had no current-file or 2020-file address match.

### Added

| Store | Address | Geocoder | Services on the official page | Store hours |
|---|---|---|---|---|
| Walmart Supercenter 1273 (Fountain S South Us Hwy 85 87 Supercenter) | 6310 S Us Highway 85-87 80817 | Current file: 6310 US HWY 85, FOUNTAIN, CO, 80817, **Fountain city** (El Paso County). 2020 file agrees. Official store-page map point (38.740386, -104.736809) also returns Fountain city | Generic "Money Services" only (hub-only) | Mon-Sun 6am-11pm |
| Walmart Supercenter 3018 (Fountain Venetucci Blvd Supercenter) | 4425 Venetucci Blvd 80906 | No address match on the current or 2020 file (variants listed under Method). Official store-page map point (38.768632, -104.781091) returns **Fountain city** (El Paso County, no CDP) in a Census coordinates lookup (current benchmark) | Generic "Money Services" only (hub-only) | Mon-Sun 6am-11pm |

- **Walmart 1273:** the official page prints Fountain, CO 80817, and the current file, the 2020 file, and the official map point all place it in Fountain city, so the row is included. Services: the page shows "Money Services" only. Money orders, check cashing, bill pay, and prepaid reload (load/unload) are not named, so all four flags are false; nothing is inferred from chain policy. No Western Union mention. Hub listing only, labeled "Money Services, call ahead"; not on the money-order or evenings/weekends pages. Unpublished fees stay "Not published, call ahead." Hours are store hours only (daily 6 a.m. to 11 p.m.), so the hub labels it Open evenings and Open weekends; money desk hours are not published.
- **Walmart 3018 fallback:** the official page prints Fountain, CO 80906 (80906 is a Colorado Springs ZIP). The Census geocoder found no address match on the current or 2020 file. The official store-page map point falls inside Fountain city, so the row is included under the same documented fallback used for Walmart 1045 in Lafayette, Walmart 5370 in Longmont, King Soopers 00129 in Erie, the Westminster Post Office, and Pueblo Midtown/Belmont; the row's notes say so. Printed city and official map point agree; this is not a hold. The row is not added to `colorado-springs.csv`. Services and hours are the same pattern as Walmart 1273 (generic "Money Services" only; store hours daily 6 a.m. to 11 p.m.).

### Held for Richard

None. No Fountain-printed store geocodes outside Fountain city, and no store printed with another city geocodes inside Fountain city. Walmart 3018 is included, not held, because the official page prints Fountain and the official map point is in Fountain city.

### Left out (not held)

- **King Soopers 00153** Fountain King Soopers, 6255 Sawcut Pt, prints **Fountain**, CO 80817. No address match on the current or 2020 file (variants listed under Method). Official store-page map point (38.7204448, -104.71195) returns **Fountain city** (El Paso County). The official page lists no Money Services and no money orders (Gas Station / Fuel Center is a feature only, not a row), so the store is omitted under the no-services rule, same as Parker King Soopers 00175. It is not a hold.
- Printed another city, and the geocoder agrees it is outside Fountain:
  - **Colorado Springs** (Colorado Springs city): King Soopers 00103 Hancock Plaza (2910 S Academy Blvd) and 00058 Cheyenne Meadows Center (815 Cheyenne Meadows Rd); Walmart Supercenters 1434 (707 S 8th St) and 1200 (3201 E Platte Ave). Official printed city and current-file geocode (and, for the two Walmarts, official map points) all agree they are in Colorado Springs. Left out, not held. Not added to `colorado-springs.csv` in this PR.
- Farther King Soopers and Walmart Supercenters listed in the locators but not opened for this run print other cities (further Colorado Springs stores, Falcon, Pueblo West, Pueblo, Woodland Park, Monument, Canon City, Elizabeth) and were not Fountain candidates.
- Walmart Neighborhood Markets 3082 (Colorado Springs S Academy Blvd) and 3083 (N Murray Blvd): excluded by policy; pages not opened for this run.

## Not changed

- Thornton holds (Eastlake Post Office, Walmart 4567), Walmart 4567, Fruitvale, the Castle Rock Post Office, City Market, Littleton holds, Erie 00129/00138, Lafayette 1045, `erie.csv`, `thornton.csv`, `colorado-springs.csv`, and every other city CSV; the Louisville Post Office Superior hold. Later batch cities (Evans, Johnstown, Montrose, Louisville) were not started.

## Not collected

- Payday / title-loan storefronts, including ACE: omitted by policy.
- Stand-alone Western Union / MoneyGram agents and other grocery brands, including City Market, were not collected.
