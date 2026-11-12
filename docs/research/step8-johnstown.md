# Step 8: Johnstown (2026-11-12, America/Denver)

**Rows:** 1 (1 Post Office). Town 8 of the batch approved on 2026-11-12 (Brighton, Windsor, Erie, Northglenn, Lafayette, Fountain, Evans, Johnstown, Montrose, Louisville; ranked from Census Vintage 2025, SUB-IP-EST2025-POP-08, where Johnstown is rank 30 at 22,433). Johnstown is a statutory town; only addresses inside the Town of Johnstown limits ("Johnstown town" in the Census geocoder; the town spans Weld and Larimer counties) are listed. No businesses were contacted.

**Counts:** 1 location; 1 money orders (Johnstown Post Office); 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 0 Open evenings, 1 Open weekends (the Post Office; weekday retail closes at 16:30). Hub-only rows: none. The money-orders page lists 1 location. The evenings/weekends page lists 1 location (0 Open evenings, 1 Open weekends). No check-cashing or bill-pay page (zero listings). No holds.

## Method

- **USPS:** official USPS Location Finder (tools.usps.com, `requestType` po), same method as Evans, Fountain, Lafayette, Northglenn, Erie, Windsor, and Brighton. Searches at 5 and 15 miles around 80534 (Johnstown) and many nearby official ZIPs (Milliken, Gilcrest, Mead, Berthoud, Windsor, Loveland, Greeley, Evans, Firestone, Platteville, and farther offices listed in `johnstown-usps-2026-11-12.md`) returned 69 unique Post Office records (`docs/research/step8-browser/johnstown-usps-locator-2026-11-12.jsonl`; pass notes in `johnstown-usps-2026-11-12.md`). Official location pages were fetched on 2026-11-12, each on the first try: 1368496 Johnstown, 1373182 Milliken, 1364775 Gilcrest, 1372465 Mead, and 1354778 Berthoud (all HTTP 200). Hours and services come from the same official locator record those pages display; retail hours means the BUSINESS hours block only.
- **Town limits:** every candidate address was checked with the U.S. Census Bureau Geocoder (https://geocoding.geo.census.gov/geocoder/, address endpoint, Public_AR_Current / Current_Current, Incorporated Places, Census Designated Places and Counties layers) on 2026-11-12. Raw results: `johnstown-usps-geocoder-2026-11-12.jsonl` (all 69 Post Office records) and `johnstown-stores-geocoder-2026-11-12.jsonl` (all 5 opened King Soopers and Walmart Supercenter rows).
- **Fallback checks:** Census 2020 benchmark (Public_AR_Census2020) and current one-line lookups for the Johnstown Post Office (121 Castle Pines Ave). Current-benchmark coordinates lookups of every official USPS locator map point. Raw results: `johnstown-geocoder-fallback-2026-11-12.jsonl`. Every opened King Soopers and Walmart Supercenter address matched the current file, so no store-page map-point fallback was used. OpenStreetMap points were not used for any decision. The listed Post Office matches the current file, the 2020 file, and its official locator map point, all in Johnstown town.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands.

## USPS

| Office | Address | Geocoder | Services | Retail hours |
|---|---|---|---|---|
| Johnstown (1368496) | 121 Castle Pines Ave 80534 | Johnstown town (121 CASTLE PINES AVE, JOHNSTOWN, CO, 80534; Weld County). 2020 file agrees; official locator point (40.3327, -104.906784) also Johnstown town | Domestic and Inquiry Money Orders | Mon-Fri 08:30-13:00 and 14:00-16:30, Sat 09:30-12:00, Sun closed |

- Johnstown Post Office: Open weekends (Saturday). Weekday retail closes at 16:30, with a midday closure from 13:00 to 14:00, so no Open evenings label. Phone 970-587-4246. URL https://tools.usps.com/locations/details/1368496. verification_status `verified_official_locator`. Window service hours match retail hours. Lobby and PO box access listed 00:01-23:59 daily are not retail and are not used. Last collection Mon-Fri 16:30, Sat 12:00 is not retail. Other listed services (passports by appointment, PO boxes, general delivery, burial flags, duck stamps, greeting cards, hold-mail/notice-left pickup, and bulk mail) are not Check Desk tracked services unless the site tracks passports. No duplicate, annex, or SDC record at 121 Castle Pines Ave.

### Left out (not held)

- **Milliken 1373182** (1009 Broad St, Milliken 80543, 970-587-3332): money orders; Mon-Fri 07:30-12:00 and 13:00-16:30, Sat 09:00-11:00. Current file and official locator map point: **Milliken town**. The closest miss (the only other office in the 80534 5-mile search). Printed another town and outside Johnstown, so left out, not held. Page HTTP 200.
- **Gilcrest 1364775** (301 Main St, Gilcrest 80623, 970-737-2934): money orders; Mon-Fri 09:30-12:30 and 13:30-16:30, Sat 09:00-11:00. Current file and official locator map point: **Gilcrest town**. Left out, not held. Page HTTP 200.
- **Mead 1372465** (350 Welker Ave, Mead 80542, 970-535-4612): money orders; Mon-Fri 08:00-12:00 and 13:00-16:30, Sat 08:00-10:00. Current file and official locator map point: **Mead town**. Left out, not held. Page HTTP 200.
- **Berthoud 1354778** (425 3rd St, Berthoud 80513, 970-532-5379): money orders; Mon-Fri 08:00-16:30, Sat 09:30-12:30. Current file and official locator map point: **Berthoud town**. Left out, not held. Page HTTP 200.
- **Windsor 1387952** (215 6th St, Windsor 80550, 970-833-3010): money orders; Mon-Fri 08:30-17:00, Sat 09:00-12:00. Current file and official locator map point: **Windsor town**. Left out, not held. `windsor.csv` was not edited.
- **WIN Carrier Annex 1560051** (1070 Diamond Valley Dr Ste 500, Windsor 80550): **Windsor town**. No retail hours and no money orders. Left out, not a hold. `windsor.csv` was not edited.
- **Evans 1362838** (3344 11th Ave, Evans 80620, 970-339-8293): money orders; Mon-Fri 08:00-17:00, Sat 09:00-12:00. Current file and official locator map point: **Evans city**. Already live on the Evans page. Left out, not held. `evans.csv` was not edited.
- **Downtown Greeley 1365513** (925 11th Ave, Greeley 80631) and **Greeley 1365514** (930 39th Ave, Greeley 80634): both **Greeley city**. Left out, not held. `greeley.csv` was not edited.
- **Loveland 1371037** (446 E 29th St, Loveland 80538) and **Valentine 1371038** (601 Cleveland Ave, Loveland 80537): both **Loveland city**. Left out, not held. `loveland.csv` was not edited.
- **Firestone 1363406** (478 1st St, Firestone 80520): **Firestone town**. Left out, not held.
- **Platteville 1377758** (400 Marion St, Platteville 80651): **Platteville town**. Left out, not held.
- Printed another place and the geocoder agrees it is outside Johnstown: La Salle (La Salle town), Timnath (Timnath town), Frederick (Frederick town), Dacono (Dacono city), Fort Lupton, Longmont, Eaton, and Kersey.
- Lucerne (1371125; address no match on current or 2020, point in no place = unincorporated Weld), Gill (1364780, unincorporated Weld), Galeton (1439603, unincorporated Weld): all outside Johnstown.
- Farther records in the 15-mile sweeps (Severance, Ault, Pierce, Nunn, Wellington, Fort Collins and the Fort Collins CO SDC duplicate at 301 Boardwalk Dr, Old Town, Erie, Erie Carrier Annex, Lyons, Hygiene, Niwot, Masonville, Drake, Laporte, Bellvue, Brighton, Brighton Carrier Annex, Lafayette, Lafayette Carrier Annex, Eastlake, Henderson, Hudson, Keenesburg, Northglenn, Northview, Broomfield, Broomfield Eagle View, Westminster, Harris Park, Louisville printed Superior, Boulder, Valmont, Boulder CO SDC, High Mar, Indian Tree, Eldorado Springs, Dupont, North Pecos, Jamestown, Allenspark, Estes Park, Briggsdale): outside Johnstown; see the locator and geocoder files.
- Carrier annexes in the sweep (WIN 1560051, Erie 1546616, Brighton 1555032, Lafayette 1369484) have no retail hours and no money orders, and none is in Johnstown. Northview (1375562, Northglenn city) also has no retail hours and no money orders.
- Shared-building pairs in the sweep, neither in Johnstown: Fort Collins 1363754 / Fort Collins CO SDC 1601572 (301 Boardwalk Dr, Fort Collins); Valmont 1385692 / Boulder CO SDC 1612987 (2995 55th St, Boulder).
- No office in the sweep is printed Johnstown besides 1368496. No record printed with another city falls inside Johnstown town by address geocode or by locator map point. USPS contract postal units and Approved Postal Providers were not collected.

## King Soopers and Walmart

Official store pages were opened in a browser on 2026-11-12 (read-only; no sign-in, no store contact). Raw results: `docs/research/step8-browser/johnstown-walmart-ks-2026-11-12.csv` and `.md` (opened rows: 3 King Soopers, 2 Walmart Supercenters). Walmart's official Johnstown directory `/store-directory/co/johnstown` listed 0 stores. The official King Soopers city directory `/stores/grocery/co/johnstown` showed "that page doesn't exist." No King Soopers and no Walmart Supercenter prints Johnstown. No unexpected grocery or retail brands appeared. Every opened Supercenter and King Soopers address was run through the Census geocoder on 2026-11-12; all 5 matched the current file.

### Added

None. No King Soopers and no Walmart Supercenter prints Johnstown, so there is no store row to add.

### Held for Richard

None. No store printed with another city or town geocodes inside the Town of Johnstown.

Priority nearby stores that were checked because they might sit inside Johnstown, but the current-file geocoder places each outside the town, in agreement with the printed city:

- **Walmart Supercenter 1008**, 250 W 65th St, prints Loveland 80538. Current file: 250 W 65TH ST, LOVELAND, CO, 80538, **Loveland city** (Larimer County). Left out, not a hold. Not added to `loveland.csv` in this PR.
- **Walmart Supercenter 953**, 1325 Denver Ave, prints Loveland 80537. Current file: 1325 DENVER AVE, LOVELAND, CO, 80537, **Loveland city** (Larimer County). Left out, not a hold. Not added to `loveland.csv` in this PR.
- **King Soopers 00104**, 1520 Main St, prints Windsor 80550. Current file: 1520 MAIN ST, WINDSOR, CO, 80550, **Windsor town** (Weld County). Already live on the Windsor page. Left out, not a hold. `windsor.csv` was not edited.
- **King Soopers 00105**, 6110 Firestone Blvd, prints Firestone 80504. Current file matched 6110 FIRESTONE TRL, FIRESTONE, CO, 80504, **Firestone town** (Weld County). Left out, not a hold. Not added to another city's CSV in this PR.
- **King Soopers 00074**, 1275 Eagle Dr, prints Loveland 80537. Current file: 1275 EAGLE DR, LOVELAND, CO, 80537, **Loveland city** (Larimer County). Left out, not a hold. Not added to `loveland.csv` in this PR.

### Left out (not held)

- Printed another city or town, and the geocoder agrees it is outside Johnstown (already-live stores in Windsor and Loveland were not changed): the five stores above. Farther King Soopers and Walmart Supercenters listed in the locators but not opened for this run print other cities (Greeley, Longmont, and farther Denver-metro Supercenters) and were not Johnstown candidates.
- No store in either locator printed Johnstown, Milliken, Mead, Gilcrest, Berthoud, or unincorporated Weld or Larimer County.

## Not changed

- Thornton holds (Eastlake Post Office, Walmart 4567), Walmart 4567, Fruitvale, the Castle Rock Post Office, City Market, Littleton holds, Erie 00129/00138, Lafayette 1045, Fountain 3018, `windsor.csv`, `loveland.csv`, `evans.csv`, `greeley.csv`, and every other city CSV; the Louisville Post Office Superior hold. Later batch cities (Montrose, Louisville) were not started.

## Not collected

- Payday / title-loan storefronts, including ACE: omitted by policy.
- Stand-alone Western Union / MoneyGram agents and other grocery brands were not collected.
