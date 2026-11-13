# Step 8: Louisville (2026-11-12, America/Denver)

**Rows:** 2 (2 King Soopers). City 10 of the batch approved on 2026-11-12 (Brighton, Windsor, Erie, Northglenn, Lafayette, Fountain, Evans, Johnstown, Montrose, Louisville; ranked from Census Vintage 2025, SUB-IP-EST2025-POP-08, where Louisville is rank 32 at 20,581). Louisville is the last city in this Census-ranked batch. Louisville is a city in Boulder County; only addresses inside Louisville city limits ("Louisville city" in the Census geocoder; Boulder County) are listed. No businesses were contacted.

**Counts:** 2 locations; 2 money orders (both King Soopers); 1 check cashing (King Soopers 00142 Louisville Marketplace); 0 bill pay; 0 prepaid reload. Labels on the hub: 2 Open evenings and 2 Open weekends (both King Soopers stores publish 6 a.m.–11 p.m. daily). Hub-only rows: 0. The money-orders page lists 2 locations. The evenings/weekends page lists 2 locations (2 Open evenings, 2 Open weekends). The check-cashing page lists 1 location (00142). No bill-pay page (zero listings). One hold: USPS 1371024, the office named Louisville, which prints Superior.

## Method

- **USPS:** official USPS Location Finder API (`https://tools.usps.com/UspsToolsRestServices/rest/POLocator/findLocations`, `requestType` po), same method as Montrose, Johnstown, Evans, Fountain, Lafayette, Northglenn, Erie, Windsor, and Brighton. Queried with curl; no browser. First pass: 5 and 15 miles around 80027 (Louisville/Superior; they share this official ZIP, and Superior has no unique ZIP), 80026 (Lafayette), 80023, 80020, 80021 (Broomfield), 80516 (Erie), 80301, 80303 (Boulder), 80031 (Westminster), 80025 (Eldorado Springs), 80544 (Niwot), and 80514 (Dacono) returned 71 unique Post Office records. Second pass: 80027 at 10 and 20 miles (0 new relative to the combined first pass), plus 5 and 15 miles around 80030 (Westminster), 80302, 80304, 80305 (Boulder), 80503 (Longmont), 80234, 80233 (Northglenn), 80501 (Longmont), and 80005 (Arvada/Westminster edge), added 7 farther offices. Together: **78 unique Post Office records**. All 44 queries returned JSON. Raw locator records: `docs/research/step8-browser/louisville-usps-locator-2026-11-12.jsonl`. Pass notes: `louisville-usps-2026-11-12.md`. Official location pages were fetched with curl on 2026-11-12 at about 3:53–3:54 p.m. MT, each on the first try (HTTP 200): 1371024 (named Louisville, printed Superior), 1369494 Lafayette, 1369484 Lafayette Carrier Annex, 1366905 High Mar, 1356062 Broomfield, 1361605 Broomfield Eagle View, 1362695 Erie, 1546616 Erie Carrier Annex, 1355494 Boulder, 1385692 Valmont, 1612987 Boulder CO SDC, and 1362237 Eldorado Springs. Hours and services come from the same official locator record those pages display; retail hours means the `BUSINESS` hours block only.
- **City limits:** every candidate address was checked with the U.S. Census Bureau Geocoder (https://geocoding.geo.census.gov/geocoder/, address endpoint, Public_AR_Current / Current_Current, Incorporated Places, Census Designated Places and Counties layers) on 2026-11-12. Raw results: `louisville-usps-geocoder-2026-11-12.jsonl` (all 78 Post Office records) and `louisville-stores-geocoder-2026-11-12.jsonl` (King Soopers 00013 and 00142 in Louisville; nearby Walmart 5341 and King Soopers Miramonte and 287 in Broomfield; Walmart 1045, already on the Lafayette page, had no current-file address match). Official USPS locator map points were also checked against the current benchmark. For 1371024 and for records with no current-file address match, one-line lookups were run against the Census 2020 file and the current file (`louisville-geocoder-fallback-2026-11-12.jsonl`). OpenStreetMap was not used.
- **King Soopers and Walmart:** official store pages were opened in a browser on 2026-11-12 (read-only; no sign-in, no store contact). Raw results: `docs/research/step8-browser/louisville-walmart-ks-2026-11-12.csv` and `.md`. The official King Soopers Louisville directory (`kingsoopers.com/stores/grocery/co/louisville`, HTTP 200) lists exactly the two stores that print Louisville. The official Walmart Louisville directory (`walmart.com/store-directory/co/louisville`, HTTP 200) is empty: no Walmart prints Louisville. No unexpected grocery or retail brands were added.

## Post Offices

### Held for Richard (do not auto-include)

- **Louisville (USPS 1371024) — HOLD.** Official name Louisville; official printed city **Superior**, CO 80027. Address 566 S McCaslin Blvd. Phone 303-665-0030. Money orders yes (`MONEYORDERSDOM`, `MONEYORDERSINQ`). Retail hours Mon–Fri 09:00–17:30, Sat 09:00–12:00, Sun closed. Weekday retail closes after 17:00, so it would be marked Open evenings if it were an include; it is open Saturdays. URL: https://tools.usps.com/locations/details/1371024 (HTTP 200, first try). verification_status `verified_official_locator`. last_verified 2026-11-12.
  - Current address file: 566 S MCCASLIN BLVD, SUPERIOR, CO, 80027, **Louisville city**, Boulder County (x -105.164208507346, y 39.961837731036).
  - 2020 address file: the same matched address, **Louisville city**.
  - Official locator map point 39.96163, -105.159983 → **Louisville city**, Boulder County.
  - Official printed city (Superior) and the geocoder / map point (Louisville city) disagree, so this is a hold, not a candidate include. There is no separate Superior Post Office in the sweep, and no official record prints city Louisville. Window service hours match retail hours. This hold was approved as a hold in the Louisville build brief and was not added.

### Left out (not held)

- There is **no Louisville Carrier Annex** (or other Louisville-printed carrier/SDC record) in the sweep.
- Nearby offices printed with other cities, where the geocoder or official map point agrees they are outside Louisville city. All list money orders unless noted:
  - Lafayette 1369494, 603 S Public Rd, Lafayette 80026 (Lafayette city). Already live on the Lafayette page. `lafayette.csv` was not edited. Page HTTP 200.
  - Lafayette Carrier Annex 1369484, 109 Kimbark St, Lafayette 80026: no `BUSINESS` (retail) hours and no money orders. Current file: Lafayette city. Left out as an annex with no retail and no tracked service, not a hold. Page HTTP 200.
  - High Mar 1366905, 4985 Moorhead Ave, Boulder 80305 (Boulder city). Page HTTP 200.
  - Broomfield 1356062, 280 E 1st Ave, Broomfield 80020 (Broomfield city). Page HTTP 200.
  - Broomfield Eagle View 1361605, 8800 W 116th Cir, Broomfield 80021: no current-file or 2020 address match; official locator point is in Broomfield city, Broomfield County. Already handled on the Broomfield page. `broomfield.csv` was not edited. Page HTTP 200.
  - Erie 1362695, 150 Wells St, Erie 80516 (Erie town, Weld County). Already live on the Erie page. `erie.csv` was not edited. Page HTTP 200.
  - Erie Carrier Annex 1546616, 621 Mitchell Way, Erie 80516: no retail, no money orders (Erie town). Page HTTP 200.
  - Boulder 1355494, 1905 15th St, Boulder 80302 (Boulder city). Page HTTP 200.
  - Valmont 1385692 and Boulder CO SDC 1612987 share 2995 55th St, Boulder 80301 (Boulder city). Valmont lists money orders; the SDC does not. Pages HTTP 200.
  - Eldorado Springs 1362237, 3330 Eldorado Springs Dr, Eldorado Springs 80025: no current-file or 2020 address match; official locator point is in Eldorado Springs CDP, Boulder County (unincorporated). Left out as an unincorporated CDP outside Louisville city, not a hold. Page HTTP 200.
  - Niwot 1375136 (Niwot CDP, unincorporated Boulder County). Left out as an unincorporated CDP, not a hold.
  - Westminster, Longmont, Northglenn, and farther offices in the 15- and 20-mile sweeps: outside Louisville city; see the locator and geocoder files.
- USPS contract postal units and Approved Postal Providers were not collected, the same as for earlier cities.
- Fetch failures: none. All 44 locator API queries returned JSON, and all 12 detail pages returned HTTP 200 on the first try.

## King Soopers and Walmart

Official store pages were opened in a browser on 2026-11-12 (read-only; no sign-in, no store contact). Raw results: `docs/research/step8-browser/louisville-walmart-ks-2026-11-12.csv` and `.md`.

### Added

- **King Soopers 00013**, King Soopers Louisville, 1375 E South Boulder Rd, prints Louisville, CO 80027. Official store page (https://www.kingsoopers.com/stores/grocery/co/louisville/louisville/620/00013, HTTP 200) tags **Money Orders** and **Money Services**. Check cashing, bill pay, and prepaid reload were not tagged and are not inferred. Store hours Sun–Sat 6 a.m.–11 p.m. Phone 303-673-1800. verification_status `verified_official_store_page`. last_verified 2026-11-12. Current file: 1375 E SOUTH BOULDER RD, LOUISVILLE, CO, 80027, **Louisville city**, Boulder County (x -105.127638888193, y 39.987005310458). The 2020 address file agrees (Louisville city). Full money-order row; fee not published, call ahead. The page also shows a Fuel Center; fuel is not a separate row.
- **King Soopers 00142**, King Soopers Louisville Marketplace, 1171 W Dillon Rd, prints Louisville, CO 80027. Official store page (https://www.kingsoopers.com/stores/grocery/co/louisville/louisville-marketplace/620/00142, HTTP 200) tags **Check Cashing**, **Money Orders**, and **Money Services**. Bill pay and prepaid reload were not tagged and are not inferred. Store hours Sun–Sat 6 a.m.–11 p.m. Phone 303-214-1200. verification_status `verified_official_store_page`. last_verified 2026-11-12. Current file: 1171 W DILLON RD, LOUISVILLE, CO, 80027, **Louisville city**, Boulder County (x -105.167537481124, y 39.962145510469). The 2020 address file agrees (Louisville city). This is the check-cashing row; the site generates `/louisville/check-cashing/`. The page also shows a Fuel Center; fuel is not a separate row.

### Held for Richard

None among the stores. The only hold in this city is USPS 1371024, above. No Louisville-printed store geocodes outside Louisville city, and no other-city-printed store that was geocoded has an address match inside Louisville city.

### Left out (not held)

- **Walmart Supercenter 5341**, 500 Summit Blvd, prints Broomfield, CO 80021. Official page https://www.walmart.com/store/5341-broomfield-co (HTTP 200) lists generic Money Services only. Closest Walmart to 80027 (about 2.82 mi per the Walmart finder). Current file: 500 SUMMIT BLVD, BROOMFIELD, CO, 80021, **Broomfield city**, Broomfield County. The 2020 file agrees. Printed another city and geocodes there, so left out, not a hold. Not added to another city's CSV in this PR.
- **Walmart Supercenter 1045**, 745 US Highway 287, prints Lafayette, CO 80026. Already live on the Lafayette page as a hub-only map-point fallback. Official page prints Lafayette. The Census address geocoder found no match on the current or 2020 file (same miss documented for Lafayette). Not added as a second row. `lafayette.csv` was not edited.
- **King Soopers Miramonte and 287**, 1150 US Highway 287, prints Broomfield, CO 80020. Current file: 1150 US HWY 287, BROOMFIELD, CO, 80020, **Broomfield city**, Broomfield County. The 2020 file agrees. Printed another city and geocodes there, so left out, not a hold. Already on the Broomfield page; `broomfield.csv` was not edited.
- Farther Westminster and other Walmart stores listed by name only in the research note were not near-edge candidates and were not geocoded for this page.
- **Walmart:** none prints Louisville. The official Louisville directory is empty.
- Walmart Neighborhood Markets and fuel centers are not listed.

## Not changed

- Thornton holds (Eastlake Post Office, Walmart 4567), Walmart 4567, Fruitvale, the Castle Rock Post Office, City Market, Littleton holds, Erie 00129/00138, Lafayette 1045, Fountain 3018, Montrose 1058, `lafayette.csv`, `broomfield.csv`, `erie.csv`, and every other existing city CSV. No city beyond Louisville was started, and no further batch was proposed or built.

## Not collected

- Payday / title-loan storefronts, including ACE: omitted by policy.
- Stand-alone Western Union / MoneyGram agents and other grocery brands (City Market, Safeway, etc.) were not collected.
