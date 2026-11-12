# Step 8: Montrose (2026-11-12, America/Denver)

**Rows:** 2 (1 Post Office, 1 Walmart Supercenter). City 9 of the batch approved on 2026-11-12 (Brighton, Windsor, Erie, Northglenn, Lafayette, Fountain, Evans, Johnstown, Montrose, Louisville; ranked from Census Vintage 2025, SUB-IP-EST2025-POP-08, where Montrose is rank 31 at 21,583). Montrose is a city in Montrose County; only addresses inside Montrose city limits ("Montrose city" in the Census geocoder; Montrose County) are listed. No businesses were contacted.

**Counts:** 2 locations; 1 money orders (Montrose Post Office); 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 1 Open evenings (the Walmart Supercenter), 2 Open weekends (the Post Office and the Walmart Supercenter). Hub-only rows: 1 (Walmart Supercenter 1058, "Money Services, call ahead"). The money-orders page lists 1 location. The evenings/weekends page lists 1 location (0 Open evenings, 1 Open weekends); the Walmart Supercenter is hub-only and does not appear on that page, because its official store page does not name a tracked service. No check-cashing or bill-pay page (zero listings). No holds.

## Method

- **USPS:** official USPS Location Finder (tools.usps.com, `requestType` po), same method as Johnstown, Evans, Fountain, Lafayette, Northglenn, Erie, Windsor, and Brighton. Searches at 5 and 15 miles around 81401 (Montrose), 81403 (Montrose), 81402 (Montrose PO Box ZIP), 81425 (Olathe), 81416 (Delta), 81432 (Ridgway), 81427 (Ouray), 81220 (Cimarron), 81415 (Crawford), and many other nearby official ZIPs listed in `montrose-usps-2026-11-12.md` returned 53 unique Post Office records (`docs/research/step8-browser/montrose-usps-locator-2026-11-12.jsonl`; pass notes in `montrose-usps-2026-11-12.md`). Official location pages were fetched on 2026-11-12, each on the first try: 1373677 Montrose, 1373668 Montrose Annex, 1375997 Olathe, 1360641 Delta, 1379328 Ridgway, and 1358060 Cimarron (all HTTP 200). Hours and services come from the same official locator record those pages display; retail hours means the BUSINESS hours block only.
- **City limits:** every candidate address was checked with the U.S. Census Bureau Geocoder (https://geocoding.geo.census.gov/geocoder/, address endpoint, Public_AR_Current / Current_Current, Incorporated Places, Census Designated Places and Counties layers) on 2026-11-12. Raw results: `montrose-usps-geocoder-2026-11-12.jsonl` (all 53 Post Office records) and `montrose-stores-geocoder-2026-11-12.jsonl` (Walmart Supercenter 1058 in Montrose and nearby Supercenter 5458 in Delta).
- **Fallback checks:** Census 2020 benchmark (Public_AR_Census2020) and current one-line lookups for the Montrose Post Office (321 S 1st St) and the left-out Montrose Annex (3025 Woodgate Rd); current-benchmark coordinates lookups of every official USPS locator map point; and, for Walmart 1058, address variants of `16750 S Townsend Ave` (including Townsend Ave / South Townsend / Townsend Avenue / S Townsend / S. Townsend Ave / S US Highway 550 / S Hwy 550 / Highway 550 / US Highway 550, and the 81403 ZIP) on the current and 2020 files, plus a current-benchmark coordinates lookup of the official store-page map point (38.449068, -107.863399; JSON-LD / `geoPoint` on the official Walmart store page https://www.walmart.com/store/1058-montrose-co, read 2026-11-12; not collected from OpenStreetMap). Raw results: `montrose-geocoder-fallback-2026-11-12.jsonl`. One listed row relies on the fallback: Walmart Supercenter 1058 (below). OpenStreetMap points were not used for any decision. The listed Post Office matches the current file, the 2020 file, and its official locator map point, all in Montrose city.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands.

## USPS

| Office | Address | Geocoder | Services | Retail hours |
|---|---|---|---|---|
| Montrose (1373677) | 321 S 1st St 81401 | Montrose city (321 S 1ST ST, MONTROSE, CO, 81401; Montrose County). 2020 file agrees; official locator point (38.47857, -107.876618) also Montrose city | Domestic and Inquiry Money Orders | Mon-Fri 08:00-17:00, Sat 10:00-12:00, Sun closed |

- Montrose Post Office: Open weekends (Saturday). Weekday retail closes at 17:00, so no Open evenings label. Phone 970-249-6654. URL https://tools.usps.com/locations/details/1373677. verification_status `verified_official_locator`. No duplicate, annex, or SDC record at 321 S 1st St.

### Left out (not held)

- **Montrose Annex 1373668** (3025 Woodgate Rd, Montrose 81401, 970-252-7246): official printed city is Montrose. The current address file did not match this street. The 2020 file did: 3025 WOODGATE RD, MONTROSE, CO, 81401, **Montrose city**. The official locator point (38.451995, -107.86379) is also in **Montrose city**, Montrose County. The office has no `BUSINESS` (retail) hours and no money orders. It is a carrier/delivery unit with lobby, PO Box access, and hold-mail/pickup windows, not a retail office. Left out, not a hold. It does not share a building with the 321 S 1st St retail office. Page HTTP 200.
- **Olathe 1375997** (215 N US Highway 50 Business Loop, Olathe 81425, 970-323-5936): money orders; Mon-Fri 09:00-16:30, Sat 09:30-12:00. Current file and official locator map point: **Olathe town**. The closest miss (the only other office in the 81401 15-mile search). Printed another town and outside Montrose, so left out, not held. Page HTTP 200.
- **Delta 1360641** (360 Meeker St, Delta 81416, 970-874-2652): money orders; Mon-Fri 09:00-17:00, Sat 10:00-12:00. Current file and official locator map point: **Delta city**. Left out, not held. Page HTTP 200.
- **Ridgway 1379328** (485 Clinton St, Ridgway 81432, 970-626-5576): money orders; Mon-Fri 08:30-16:30, Sat 09:00-12:00. Address no match on the current or 2020 file; official locator point is in **Ridgway town**, Ouray County. Left out, not held. Page HTTP 200.
- **Cimarron 1358060** (82111 E US Highway 50, Cimarron 81220, 970-252-8366): money orders; Mon-Fri 09:30-13:30, Sat 10:00-12:00. Address no match on the current or 2020 file; official locator point is in no incorporated place and no CDP (unincorporated Montrose County). Unincorporated places stay off the include list. Left out, not held. Page HTTP 200.
- **Ouray 1376452** (620 Main St, Ouray 81427): **Ouray city**. Left out, not held.
- **Crawford 1359758** (295 Highway 92, Crawford 81415): **Crawford town**. Left out, not held.
- Printed another place and the geocoder agrees it is outside Montrose: Cedaredge, Hotchkiss, Paonia, Austin (printed Austin; address and point in Orchard City town), Eckert (printed Eckert; address and point in Orchard City town), Nucla, Naturita, Norwood, and Redvale.
- Cory (1359343; address no match, point in Orchard City town) and Lazear (1370017; address no match, point in Lazear CDP): no retail `BUSINESS` hours and no money orders. Left out, not holds; neither is in Montrose city.
- Farther records in the sweep (Telluride, Ophir, Placerville, Silverton, Somerset, Gunnison, Almont, Parlin, Powderhorn, Whitewater, Palisade, Clifton, Fruitvale, Grand Junction, Grand Junction Carrier Annex, Lake City, Crested Butte, Molina, Mesa, Collbran, De Beque, Paradox, Bedrock, Pitkin, Rico, Gateway, Dolores, Lewis, Cortez, Yellow Jacket, Mancos, Egnar, Dove Creek, Sargents): outside the City of Montrose; see the locator and geocoder files. `grand-junction.csv` was not edited.
- Carrier annexes / no-retail records in the sweep besides Montrose Annex: Grand Junction Carrier Annex 1469994 (Grand Junction city; no retail hours, no money orders), Cory 1359343, Lazear 1370017, and Powderhorn 1378272 (unincorporated Gunnison County; no `BUSINESS` hours, no money orders). None of these is a Montrose hold.
- No shared-building pairs in the sweep. No office in the sweep is printed Montrose besides 1373677 and the left-out Annex. No record printed with another city falls inside Montrose city by address geocode or by locator map point. USPS contract postal units and Approved Postal Providers were not collected.

## King Soopers and Walmart

Official store pages were opened in a browser on 2026-11-12 (read-only; no sign-in, no store contact). Raw results: `docs/research/step8-browser/montrose-walmart-ks-2026-11-12.csv` and `.md` (opened rows: 1 Walmart Supercenter; 0 King Soopers). Walmart's official Montrose directory `/store-directory/co/montrose` listed 1 store (Montrose Supercenter). The official King Soopers city directory `/stores/grocery/co/montrose` showed "that page doesn't exist." No King Soopers store prints Montrose. No unexpected grocery or retail brands were added. City Market results from the King Soopers locator were recorded only and were not opened as a new brand.

### Added

- **Walmart Supercenter 1058**, Montrose Supercenter, 16750 S Townsend Ave, prints Montrose 81401. Official store page (https://www.walmart.com/store/1058-montrose-co, HTTP 200) lists a generic **Money Services** label only; check cashing, money orders, bill pay, and load/unload are not named, so all four service flags are false. Hub listing only; call ahead. Store hours Mon–Sun 6 a.m.–11 p.m. Phone 970-249-7544. verification_status `verified_official_store_page`.
- **Walmart 1058 fallback:** the official page prints Montrose, CO 81401. The Census geocoder found no address match on the current or 2020 file (variants listed under Method). The official store-page map point (38.449068, -107.863399) returns **Montrose city** (Montrose County, no CDP) in a Census coordinates lookup (current benchmark), so the row is included under the same documented fallback used for Walmart 1045 in Lafayette, Walmart 3018 in Fountain, Walmart 5370 in Longmont, King Soopers 00129 in Erie, and similar rows; the row's notes say so. Printed city and official map point agree; this is not a hold. OpenStreetMap was not used.

### Held for Richard

None. No Montrose-printed office or store geocodes outside the City of Montrose, and no other-city-printed office or store has an address match or official map point inside the City of Montrose.

### Left out (not held)

- **Walmart Supercenter 5458**, 37 Stafford Ln, prints Delta 81416. Current file: 37 STAFFORD LN, DELTA, CO, 81416, **Delta city** (Delta County). Left out, not a hold. About 25 miles away. The store page was not opened for full transcription. Not added to another city's CSV in this PR.
- **Walmart 1550**, Gunnison Store, 900 N Main St, Gunnison 81230, was not identified as a Supercenter and is outside the requested store type. Not opened.
- **King Soopers:** none prints Montrose. The official locator searches for Montrose, CO 81401 and 81403 returned four **City Market** results and no King Soopers store.
- **City Market (not an approved brand; not opened, no rows):** Downtown Montrose (128 S Townsend Ave, Montrose 81401), South Montrose (16400 S Townsend Ave, Montrose 81401), Delta (122 Gunnison River Dr, Delta 81416), and Hotchkiss (215 6th St, Hotchkiss 81419). These were recorded from the King Soopers locator by name and address only. City Market pages were not opened, the stores were not geocoded, and nothing was added. This is an omission, not a hold, same as Grand Junction. Open for Richard to decide later.
- Walmart Neighborhood Markets and fuel centers are not listed.

## Not changed

- Thornton holds (Eastlake Post Office, Walmart 4567), Walmart 4567, Fruitvale, the Castle Rock Post Office, City Market, Littleton holds, Erie 00129/00138, Lafayette 1045, Fountain 3018, `grand-junction.csv`, and every other city CSV; the Louisville Post Office Superior hold. Later batch cities (Louisville) were not started.

## Not collected

- Payday / title-loan storefronts, including ACE: omitted by policy.
- Stand-alone Western Union / MoneyGram agents and other grocery brands (City Market, Safeway, etc.) were not collected.
