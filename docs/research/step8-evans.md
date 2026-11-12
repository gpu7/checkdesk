# Step 8: Evans (2026-11-12, America/Denver)

**Rows:** 1 (1 Post Office). City 7 of the batch approved on 2026-11-12 (Brighton, Windsor, Erie, Northglenn, Lafayette, Fountain, Evans, Johnstown, Montrose, Louisville; ranked from Census Vintage 2025, SUB-IP-EST2025-POP-08, where Evans is rank 29 at 22,500). Evans is a city in Weld County; only addresses inside Evans city limits ("Evans city" in the Census geocoder; Weld County) are listed. No businesses were contacted.

**Counts:** 1 location; 1 money orders (Evans Post Office); 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 0 Open evenings, 1 Open weekends (the Post Office; weekday retail closes at 17:00). Hub-only rows: none. The money-orders page lists 1 location. The evenings/weekends page lists 1 location (0 Open evenings, 1 Open weekends). No check-cashing or bill-pay page (zero listings). No holds.

## Method

- **USPS:** official USPS Location Finder (tools.usps.com, `requestType` po), same method as Fountain, Lafayette, Northglenn, Erie, Windsor, and Brighton. Searches at 5 and 15 miles around 80620 (Evans), 80631, 80632, 80634, 80639 (Greeley/UNC), 80645 (La Salle), 80643 (Keenesburg), 80534 (Johnstown), 80621 (Fort Lupton), 80615 (Eaton), 80633 (Greeley PO boxes), 80610 (Ault), 80650 (Pierce), 80644 (Kersey), and 80651 (Platteville) returned 40 unique Post Office records (`docs/research/step8-browser/evans-usps-locator-2026-11-12.jsonl`; pass notes in `evans-usps-2026-11-12.md`). Official location pages were fetched on 2026-11-12, each on the first try: 1362838 Evans, 1365513 Downtown Greeley, 1365514 Greeley, and 1369426 La Salle (all HTTP 200). Hours and services come from the same official locator record those pages display; retail hours means the BUSINESS hours block only.
- **City limits:** every candidate address was checked with the U.S. Census Bureau Geocoder (https://geocoding.geo.census.gov/geocoder/, address endpoint, Public_AR_Current / Current_Current, Incorporated Places, Census Designated Places and Counties layers) on 2026-11-12. Raw results: `evans-usps-geocoder-2026-11-12.jsonl` (all 40 Post Office records) and `evans-stores-geocoder-2026-11-12.jsonl` (all 5 King Soopers and Walmart Supercenter rows in the research CSV).
- **Fallback checks:** Census 2020 benchmark (Public_AR_Census2020) and current one-line lookups for the Evans Post Office (3344 11th Ave). Current-benchmark coordinates lookups of every official USPS locator map point. Raw results: `evans-geocoder-fallback-2026-11-12.jsonl`. Every in-scope King Soopers and Walmart Supercenter address matched the current file, so no store-page map-point fallback was used. OpenStreetMap points were not used for any decision. The listed Post Office matches the current file, the 2020 file, and its official locator map point, all in Evans city.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands.

## USPS

| Office | Address | Geocoder | Services | Retail hours |
|---|---|---|---|---|
| Evans (1362838) | 3344 11th Ave 80620 | Evans city (3344 11TH AVE, EVANS, CO, 80620; Weld County). 2020 file agrees; official locator point (40.381418, -104.69635) also Evans city | Domestic and Inquiry Money Orders | Mon-Fri 08:00-17:00, Sat 09:00-12:00, Sun closed |

- Evans Post Office: Open weekends (Saturday). Weekday retail closes at 17:00, so no Open evenings label. Phone 970-339-8293. URL https://tools.usps.com/locations/details/1362838. verification_status `verified_official_locator`. Window service hours match retail hours. Lobby and PO box access listed 00:01-23:59 daily are not retail and are not used. Last collection Mon-Fri 17:00, Sat 15:30 is not retail. Other listed services (passports by appointment, PO boxes, general delivery, burial flags, duck stamps, greeting cards, hold-mail/notice-left pickup, and bulk mail) are not Check Desk tracked services unless the site tracks passports. No duplicate, annex, or SDC record at 3344 11th Ave.

### Left out (not held)

- **Downtown Greeley 1365513** (925 11th Ave, Greeley 80631, 970-392-2782): money orders; Mon-Fri 07:30-17:30, Sat 09:00-13:00. Current file and official locator map point: **Greeley city**. Printed another city and outside Evans, so left out, not held. Page HTTP 200. `greeley.csv` was not edited.
- **Greeley 1365514** (930 39th Ave, Greeley 80634, 970-392-0298): money orders; Mon-Fri 07:30-17:30, Sat 09:00-13:00. Current file and official locator map point: **Greeley city**. Left out, not held. Page HTTP 200. `greeley.csv` was not edited.
- **La Salle 1369426** (524 N 2nd St, La Salle 80645, 970-284-6569): money orders; Mon-Fri 08:00-16:30, Sat 09:00-12:00. Current file and official locator map point: **La Salle town**. Left out, not held. Page HTTP 200.
- Printed another place and the geocoder agrees it is outside Evans: Kersey (Kersey town), Gilcrest (Gilcrest town), Milliken (Milliken town), Johnstown (Johnstown town), Platteville, Eaton, Lucerne (address no match, locator point in no place = unincorporated Weld County), Gill (unincorporated), and Galeton (unincorporated).
- Farther records in the 15-mile sweeps (Windsor, Win Carrier Annex, Severance, Ault, Pierce, Nunn, Wellington, Timnath, Loveland, Valentine, Berthoud, Mead, Fort Collins and the Fort Collins CO SDC duplicate at 301 Boardwalk Dr, Fort Lupton, Dacono, Frederick, Firestone, Erie, Erie Carrier Annex, Brighton, Brighton Carrier Annex, Henderson, Eastlake, Hudson, Keenesburg, Roggen): outside Evans; see the locator and geocoder files.
- Carrier annexes in the sweep (Win 1560051, Brighton 1555032, Erie 1546616) have no retail hours and no money orders, and none is in Evans.
- Only shared-building pair in the sweep: Fort Collins 1363754 / Fort Collins CO SDC 1601572 (301 Boardwalk Dr, Fort Collins). Not relevant to Evans.
- No office in the sweep is printed Evans besides 1362838. No record printed with another city falls inside Evans city by address geocode or by locator map point. USPS contract postal units and Approved Postal Providers were not collected.

## King Soopers and Walmart

Official store pages were opened in a browser on 2026-11-12 (read-only; no sign-in, no store contact). Raw results: `docs/research/step8-browser/evans-walmart-ks-2026-11-12.csv` and `.md` (5 rows: 3 King Soopers, 2 Walmart Supercenters). The official King Soopers city directory `/stores/grocery/co/evans` rendered only "loading" and listed no stores. Walmart's official Evans directory `/store-directory/CO/Evans` listed 0 stores. No King Soopers and no Walmart Supercenter prints Evans. No unexpected grocery or retail brands appeared. Every in-scope Supercenter and King Soopers address was run through the Census geocoder on 2026-11-12; all 5 matched the current file.

### Added

None. No King Soopers and no Walmart Supercenter prints Evans, so there is no store row to add.

### Held for Richard

None. No store printed with another city geocodes inside Evans city.

Priority nearby stores that were checked because they might sit inside Evans, but the current-file geocoder places each outside the city, in agreement with the printed city:

- **Walmart Supercenter 980**, Greeley S 23rd Ave Supercenter, 3103 S 23rd Ave, prints Greeley 80631 (about 1.12 mi from the 80620 search). Current file: 3103 23RD AVE, GREELEY, CO, 80631, **Greeley city** (Weld County). Left out, not a hold. Not added to `greeley.csv` in this PR (the store is already listed there).
- **King Soopers 00032** University Square, 2712 11th Ave, prints Greeley 80631 (about 1.2 mi). Current file: 2712 11TH AVE, GREELEY, CO, 80631, **Greeley city** (Weld County). Left out, not a hold. Not added to `greeley.csv` in this PR (the store is already listed there).
- **Walmart Supercenter 5051**, Greeley 47th Ave Supercenter, 920 47th Ave, prints Greeley 80634. Current file: 920 47TH AVE, GREELEY, CO, 80634, **Greeley city**. Left out, not a hold.
- **King Soopers 00011** Westlake, 2100 35th Ave, prints Greeley 80634. Current file: 2100 N 35TH AVE, GREELEY, CO, 80634, **Greeley city**. Left out, not a hold.
- **King Soopers 00117** North Gate Village, 6922 W 10th St, prints Greeley 80634. Current file: 6922 W 10TH ST, GREELEY, CO, 80634, **Greeley city**. Left out, not a hold.

### Left out (not held)

- Printed another city, and the geocoder agrees it is outside Evans (already-live stores in Greeley were not changed): the five Greeley stores above. Farther King Soopers and Walmart Supercenters listed in the locators but not opened for this run print other cities (Windsor, Firestone, Loveland, Fort Collins, Timnath, Longmont, Brighton, and farther Denver-metro Supercenters) and were not Evans candidates.
- No store in either locator printed Garden City, La Salle, Milliken, Kersey, Johnstown, or unincorporated Weld County.

## Not changed

- Thornton holds (Eastlake Post Office, Walmart 4567), Walmart 4567, Fruitvale, the Castle Rock Post Office, City Market, Littleton holds, Erie 00129/00138, Lafayette 1045, Fountain 3018, `greeley.csv`, `fountain.csv`, `erie.csv`, `thornton.csv`, and every other city CSV; the Louisville Post Office Superior hold. Later batch cities (Johnstown, Montrose, Louisville) were not started.

## Not collected

- Payday / title-loan storefronts, including ACE: omitted by policy.
- Stand-alone Western Union / MoneyGram agents and other grocery brands were not collected.
