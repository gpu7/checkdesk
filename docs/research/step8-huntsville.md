# Step 8: Huntsville, AL (2026-11-12 research, shipped 2026-11-13, America/Denver)

**Rows:** 11 (6 Post Offices, 5 Walmart Supercenters). First Check Desk city outside Colorado. Richard approved an Alabama batch (Huntsville, then Mobile, Birmingham, Montgomery, Tuscaloosa, one city at a time); only Huntsville is in this PR. Huntsville is a city ("Huntsville city", GEOID 0137000, in the Census geocoder); every listed row is in Madison County. Only addresses inside Huntsville city limits are listed. No businesses were contacted. Brands in scope for Alabama: USPS and Walmart Supercenters only (no King Soopers, no other grocery chains).

**Counts:** 11 locations; 6 money orders (all six Post Offices); 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 6 Open evenings (Wynn Drive Post Office and the five Walmart Supercenters), 9 Open weekends (West, Mastin Lake, Wynn Drive, and Haysland Post Offices, and the five Walmart Supercenters). Hub-only rows: 5 (Walmart Supercenters 375, 433, 332, 434, 7324; "Money Services, call ahead"). The money-orders page lists 6 locations. The evenings/weekends page lists 4 locations (1 Open evenings, 4 Open weekends); the Walmart Supercenters are hub-only and do not appear there. No check-cashing or bill-pay page (zero listings). Holds: 4 (2 Post Offices, 2 Walmart Supercenters), none listed.

Hours are copied as published and are local Huntsville time (Central Time). The after-hours label table on `/huntsville/after-hours/` says Central Time instead of Mountain Time.

## Method

- **USPS:** official USPS Location Finder (tools.usps.com, `requestType` po), same method as the Colorado Step 8 cities. Pass 1: 5 and 15 miles around every Huntsville ZIP (35801-35808, 35810-35816, 35824, 35893, 35896-35899) and nearby ZIPs for Madison, Harvest, Meridianville, Owens Cross Roads, New Hope, Brownsboro, Gurley, New Market, Toney, Hazel Green, Athens, and Somerville (72 queries, 51 unique records). Pass 2: 1, 2, 3, 10, and 20 miles around 12 Huntsville/edge ZIPs (added 1 farther record). Total 52 records (`docs/research/step8-browser/huntsville-usps-locator-2026-11-12.jsonl`). Official location pages were fetched for all 9 Huntsville-printed records, Normal, and the 11 nearest other-city offices (21 pages, all HTTP 200 on the first try); each page's embedded `poDetail` matched the API record for name, address, phone, and BUSINESS hours. Retail hours means the BUSINESS block only. Full notes: `step8-browser/huntsville-usps-2026-11-12.md`.
- **Walmart:** official walmart.com store directory and store pages, opened in a browser on 2026-11-12 (read-only, no sign-in, no store contact). Walmart's "Robot or human?" check blocked the Madison, Harvest, and Owens Cross Roads directories on the first pass; after Richard cleared it on 2026-11-13, those directories and store pages 2690, 5703, and 5197 loaded. Notes and CSV: `step8-browser/huntsville-walmart-2026-11-12.md` / `.csv`.
- **City limits:** U.S. Census Bureau Geocoder (https://geocoding.geo.census.gov/geocoder/), address endpoint, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, Incorporated Places + CDPs + Counties layers. USPS: all 52 addresses (`huntsville-usps-geocoder-2026-11-12.jsonl`), every official locator map point on the current benchmark, one-line current and 2020 lookups for every Huntsville-printed address plus Normal and Redstone Arsenal, and 2020-benchmark point checks for Redstone Arsenal, Normal, Haysland, and Wall Triana (`huntsville-geocoder-fallback-2026-11-12.jsonl`). Walmart: address and official store-page map point on both benchmarks for the five Huntsville stores plus 2690, 5703, and 5197 (lookups run 2026-11-13 about 9:50 AM MT; `huntsville-stores-geocoder-2026-11-12.jsonl`; summary `huntsville-walmart-geocode-2026-11-12.md` / `.csv`). OpenStreetMap was not used.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands. Walmart rows use `verified_official_store_page`; USPS rows use `verified_official_locator`. `last_verified` is 2026-11-12 on every row. Coordinates are kept in the notes column (lat/lng columns stay blank, same as every other city CSV).

## USPS (6 listed)

| Office | Address | Phone | Retail hours | Labels | Geocoder |
|---|---|---|---|---|---|
| Downtown Huntsville (1361171) | 615 Clinton Ave W 35801 | 256-532-0391 | Mon-Fri 08:30-17:00; Sat/Sun closed | none | Address (current + 2020) and point (34.726786, -86.593801): Huntsville city |
| West (1387203) | 3605 Governors Dr SW 35805 | 256-534-6459 | Mon-Fri 08:30-17:00; Sat 09:00-12:00 | Open weekends | Address (current + 2020) and point (34.719744, -86.616236): Huntsville city |
| Mastin Lake (1372120) | 2501 Mastin Lake Rd NW 35810 | 256-852-7094 | Mon-Fri 09:00-17:00; Sat 10:00-12:00 | Open weekends | Address (current + 2020) and point (34.771558, -86.59622): Huntsville city |
| Wynn Drive (1388386) | 645 Wynn Dr NW 35816 | 256-722-4749 | Mon-Fri 08:30-18:00; Sat 10:00-14:00 | Open evenings, Open weekends | Address (current + 2020) and point (34.74001, -86.65364): Huntsville city |
| Haysland (1366562) | 8401 Whitesburg Dr SE 35802 | 256-882-7413 | Mon-Fri 08:30-17:00; Sat 09:00-12:00 | Open weekends | See note; point (34.655045, -86.565484): Huntsville city (current + 2020) |
| Huntsville (1367688) | 3408 Wall Triana Hwy 35813 | 256-461-6630 | Mon-Fri 08:30-17:00; Sat/Sun closed | none | Address current: Huntsville city (2020 file matched the same street with ZIP 35824, Huntsville city); point (34.667511, -86.7535159): Huntsville city (current + 2020) |

All six list Domestic and Inquiry Money Orders (MONEYORDERSDOM, MONEYORDERSINQ). No Sunday retail anywhere. Wynn Drive also lists passport services (out of scope, not used).

- **Haysland (documented include):** the Census address match normalized the street to `8401 WHITESBURG WAY, HUNTSVILLE, AL, 35802` (Huntsville city) on both files, not the official Whitesburg Dr SE (about 0.38 km from the USPS point). Inclusion basis is the official USPS locator map point, which is in Huntsville city on the current and 2020 benchmarks; the address match is supporting evidence. Printed city and geocode agree, so it is not a hold. Kept as an include in the 2026-11-13 plan; Richard was told and can ask for it to be held instead.
- **Wall Triana (1367688)** shares 3408 Wall Triana Hwy with two non-retail records (1449999, 1472078); only 1367688 is listed.

### Held for Richard (not listed)

1. **Redstone Arsenal Post Office (1437778)**, 3710 Aerobee Rd, prints Huntsville, AL 35808, 256-650-1153. Money orders; Mon-Fri 09:30-13:30 and 14:30-16:30. No Census address match on the current or 2020 file (also tried with "Redstone Arsenal" as the city); the official locator point (34.67864, -86.625659) is in **Redstone Arsenal CDP** (no incorporated place) on both benchmarks. Printed city and geocode disagree. Also on a military installation.
2. **Normal Post Office (1375204)**, 100 Drake Dr, prints Normal, AL 35762, 256-852-4000. Money orders; Mon-Fri 08:00-11:30 and 12:30-16:30. No address match in either file; the official locator point (34.783609, -86.571544) is in **Huntsville city** on both benchmarks. Printed city and geocode disagree.

### Left off (not holds)

- **1449999** and **1472078** (3408 Wall Triana Hwy, Huntsville): no BUSINESS hours, no money orders.
- Other-city offices whose printed city and geocode agree outside Huntsville: Madison 1371387 (Madison city), Harvest 1366415 (Harvest CDP), Meridianville 1372765 (Meridianville CDP), Owens Cross Roads 1376485 (point in Owens Cross Roads city), New Hope 1374753 (New Hope city), Brownsboro, Gurley (Gurley town), Ryland, Capshaw, Hazel Green, Toney, New Market, and farther offices listed in `huntsville-usps-2026-11-12.md`.

## Walmart Supercenters (5 listed, hub-only)

All five official store pages show only a generic **Money Services** label; check cashing, money orders, bill pay, and load/unload are not named, so all four service flags are false. Store hours Mon-Sun 6 a.m.-11 p.m. on every page. Hub listing only; call ahead.

| Store | Official name | Address | Phone | Geocoder |
|---|---|---|---|---|
| 375 | Huntsville 3031 Memorial Parkway Sw Drake Supercenter | 3031 Memorial Pkwy SW 35801 | 256-536-2870 | No address match (current or 2020). Official store-page point (34.703017, -86.585392): Huntsville city on both benchmarks. **Included on the map-point fallback** |
| 433 | Huntsville Sparkman Drive Nw Supercenter | 2200 Sparkman Dr NW 35810 | 256-852-2236 | Address and point: Huntsville city (both files) |
| 332 | Huntsville University Drive Nw Supercenter | 6140a University Dr NW 35806 | 256-837-7272 | Matched `6140A UNIVERSITY DR NW`; address and point: Huntsville city (both files) |
| 434 | Huntsville 11610 Memorial Parkway Sw Supercenter | 11610 Memorial Pkwy SW 35803 | 256-881-0581 | Address and point: Huntsville city (both files) |
| 7324 | Huntsville Winchester Rd Ne Supercenter | 2165 Winchester Rd NE 35811 | 256-716-6773 | Address and point: Huntsville city (both files) |

- **Walmart 375 fallback:** printed Huntsville 35801; no Census address match on either file even though the same `Memorial Pkwy SW` form matched for store 434 (likely a missing address range for 3031). The official store-page map point falls in Huntsville city, Madison County, on the current and 2020 benchmarks, so the row is included under the same documented fallback used for Montrose 1058, Lafayette 1045, Fountain 3018, and similar rows. Printed city and map point agree; not a hold.

### Held for Richard (not listed)

- **Walmart Supercenter 5703**, Madison Hwy 72 W Supercenter, 8580 Hwy 72 W, prints Madison, AL 35758, 256-716-6951. Census matched `8580 US HWY 72, MADISON, AL, 35758` with incorporated place **Huntsville city**; the official map point (34.751176, -86.773609) is also Huntsville city on both benchmarks. Printed city and geocode disagree.
- **Walmart Supercenter 5197**, Owens Cross Roads Supercenter, 330 Sutton Rd SE, prints Owens Cross Roads, AL 35763, 256-534-4140. Census matched `330 SUTTON RD, OWENS CROSS ROADS, AL, 35763` with incorporated place **Huntsville city**; the official map point (34.657641, -86.485439) is also Huntsville city on both benchmarks. Printed city and geocode disagree.

Both show only generic Money Services on their official pages.

### Left off (not held)

- **Walmart Supercenter 2690**, 8650 Madison Blvd, Madison 35758: address and point in Madison city.
- **Walmart Neighborhood Markets** 5925 (2305 Jordan Ln SW, Huntsville), 5716 (9020 Bailey Cove Rd SE, Huntsville), and 7342 (7140 Wall Triana Hwy, Madison): excluded format (policy).
- **Huntsville Al Store 7254** (1 Cotton Valley Drive NW): the directory does not label it a Supercenter; excluded.
- Harvest and Owens Cross Roads Walmart directories list no stores.

## Site changes in this PR

- New `data/locations/huntsville.csv` and `/huntsville/`, `/huntsville/money-orders/`, `/huntsville/after-hours/` pages.
- Home "Start here" list and `/cities/` are now grouped by state, states alphabetical (Alabama, then Colorado). Colorado rows keep their existing order, including older out-of-order rows (Lakewood before Lafayette, Parker before Littleton). Home guide links moved under their own "Guides" subheading so they do not sit under Colorado.
- `/cities/` meta title and description name Huntsville, Alabama and no longer say "the Colorado cities"; Louisville (missing from that title since #38) was added to the list. Home meta description names Huntsville, Alabama. No `/alabama/` page, no map, no top-nav changes.

## Not changed

- Every Colorado city CSV and city page. Colorado holds (Thornton, Littleton, Erie, Louisville/Superior, etc.) unchanged. Mobile and the rest of the Alabama batch were not started.

## Not collected

- Payday / title-loan storefronts, including ACE: omitted by policy.
- Stand-alone Western Union / MoneyGram agents, other grocery chains, and USPS contract postal units were not collected.
