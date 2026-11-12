# Step 8: Loveland (2026-11-12, America/Denver)

**Rows:** 6 (2 Post Offices, 2 King Soopers, 2 Walmart Supercenters). City 1 of the batch approved on 2026-11-12 (Loveland, Broomfield, Grand Junction, Parker, Littleton; ranked from Census Vintage 2025, SUB-IP-EST2025-POP-08). Only addresses inside the City of Loveland (incorporated place, "Loveland city" in the Census geocoder) are listed. No businesses were contacted.

**Counts:** 6 locations; 4 money orders (2 Post Offices, 2 King Soopers); 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 5 Open evenings, 6 Open weekends. The evenings/weekends page lists the 4 money-order locations (3 Open evenings, 4 Open weekends; the Valentine Post Office closes at 4:30 p.m. on weekdays, so it is Open weekends only). Both Walmart Supercenters are hub-only ("Money Services, call ahead"). No check-cashing or bill-pay page (zero listings).

## Method

- **USPS:** official USPS Location Finder (tools.usps.com, `locationType` PO), same method as Castle Rock/Longmont/Boulder. Searches at 5 and 15 miles around Loveland ZIPs (80537, 80538, 80539) returned 19 Post Office records (`docs/research/step8-browser/loveland-usps-locator-2026-11-12.jsonl`). Rows link the official location pages (`https://tools.usps.com/locations/details/<id>`); hours and services come from the same official locator record those pages display.
- **City limits:** every candidate address was checked with the U.S. Census Bureau Geocoder (https://geocoding.geo.census.gov/geocoder/, address endpoint, Public_AR_Current / Current_Current, Incorporated Places and Census Designated Places layers) on 2026-11-12. Raw results: `loveland-usps-geocoder-2026-11-12.jsonl` (all 19 Post Office records) and `loveland-stores-geocoder-2026-11-12.jsonl` (all 28 store pages).
- **Fallback checks** for addresses with no current-benchmark match: Census 2020 benchmark (Public_AR_Census2020) one-line lookups, plus coordinates lookups (current benchmark) of official USPS locator points; for two out-of-area King Soopers pages with no address match and no official map point in the research file, OpenStreetMap points were used as a supplementary, non-official check. Raw results: `loveland-geocoder-fallback-2026-11-12.jsonl`. No listed row needed the fallback; it was used only to confirm out-of-city candidates. The official locator points for both listed Post Offices also return Loveland city.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands.

## USPS

| Office | Address | Geocoder | Services | Retail hours |
|---|---|---|---|---|
| Loveland (1371037) | 446 E 29th St 80538 | Loveland city (446 E 29TH ST, LOVELAND, CO, 80538) | Domestic and Inquiry Money Orders | Mon-Fri 08:30-17:30, Sat 09:00-13:00, Sun closed |
| Valentine (1371038) | 601 Cleveland Ave 80537 | Loveland city (601 CLEVELAND AVE, LOVELAND, CO, 80537) | Domestic and Inquiry Money Orders | Mon-Fri 09:00-16:30, Sat 09:00-12:00, Sun closed |

- Loveland Post Office: Open evenings and Open weekends. Phone 970-663-3010.
- Valentine Post Office: Open weekends only (closes 16:30 on weekdays). Phone 970-667-5303. Official locator name "VALENTINE", printed city Loveland.
- No other Loveland-printed Post Office, and no duplicate record at either address, appeared in the locator results. No Loveland-printed office was found without money orders.

Out of city (printed another place, and the geocoder agrees or found no match): Berthoud 1354778 (Berthoud town); Johnstown 1368496 (Johnstown town); Milliken 1373182 (Milliken town); Mead 1372465 (Mead town); Windsor 1387952 and Win Carrier Annex 1560051 (Windsor town; the annex has no retail hours or money orders); Timnath 1384692 (Timnath town); Fort Collins 1363754 and Fort Collins CO SDC 1601572 at the same address, 301 Boardwalk Dr, and Old Town 1376040 (Fort Collins city; Fort Collins is already live and unchanged); Lyons 1371280 (Lyons town); Laporte 1369871 (Laporte CDP); Bellvue 1354562 (matched, in no place or CDP); Severance 1381248 (address matches were ambiguous across ZIPs; its official locator point returns Severance town); Masonville 1372106 and Hygiene 1367788 (no address match on the current or 2020 file; official locator points are in no incorporated place or CDP); Drake 1361283 (no current-file match; the 2020 file and the official locator point are in no place or CDP). No Post Office printed with another city geocodes inside Loveland. USPS contract postal units and Approved Postal Providers were not collected.

## King Soopers and Walmart

Official store pages were opened in a browser on 2026-11-12 (read-only; no sign-in, no store contact). Raw results: `docs/research/step8-browser/loveland-walmart-ks-2026-11-12.csv` and `.md` (28 detail pages: 21 King Soopers, 7 Walmart). The King Soopers locator returned 21 stores for "Loveland, CO" over 3 pages; all 21 were opened. Walmart's store finder was not run; Walmart's official store directories for Loveland, Fort Collins, Greeley and Timnath were used (the Colorado directory lists no Walmart in Windsor, Berthoud, Johnstown, Milliken, Wellington or Evans). The two Longmont Walmart Supercenters were not re-opened; they are in `longmont-walmart-ks-2026-11-12.csv` and already geocoded in Longmont (`longmont-stores-geocoder-2026-11-12.jsonl`, `longmont-geocoder-fallback-2026-11-12.jsonl`). No unexpected grocery or retail brands appeared. Every address was run through the Census geocoder on 2026-11-12.

### Added (4 store rows)

| Store | Address | Geocoder | Services listed | Store hours |
|---|---|---|---|---|
| King Soopers 00074 Eagle Drive | 1275 Eagle Dr 80537 | Loveland city (1275 EAGLE DR, LOVELAND, CO, 80537) | Money orders (and Money Services) | Sun-Sat 6 AM-11 PM |
| King Soopers 00044 29th Street | 253 E 29th St 80538 | Loveland city (253 E 29TH ST, LOVELAND, CO, 80538) | Money orders (and Money Services) | Sun-Sat 6 AM-11 PM |
| Walmart Supercenter 953 (Loveland N Denver Ave Supercenter) | 1325 Denver Ave 80537 | Loveland city (1325 DENVER AVE, LOVELAND, CO, 80537) | Generic "Money Services" only (hub-only) | Mon-Sun 6am-11pm |
| Walmart Supercenter 1008 (Loveland W 65th St Supercenter) | 250 W 65th St 80538 | Loveland city (250 W 65TH ST, LOVELAND, CO, 80538) | Generic "Money Services" only (hub-only) | Mon-Sun 6am-11pm |

- **Spelling/geocoder notes:** King Soopers prints "253 E 29Th St"; the row uses "253 E 29th St" (same address as the geocoder match). The official page names Walmart 953 "Loveland N Denver Ave Supercenter" but prints its address as "1325 Denver Ave" (no N prefix); the geocoder matched 1325 DENVER AVE. The locator printed the 29th Street store name as "29th Street Loveland" and the other as "Eagle Drive Loveland"; row names drop the repeated city.
- **Hours:** store hours only. Pharmacy, fuel, sensory-friendly, and holiday hours not used. All four stores are Open evenings and Open weekends.
- **King Soopers:** both Loveland pages tag "Money Orders" and "Money Services" (`money_orders=true`). No check cashing, bill pay, prepaid reload, Western Union, or MoneyGram named. "Account Funding" is not a tracked service and is not flagged. King Soopers fees stay "Not published, call ahead."
- **Walmart:** both Loveland Supercenter pages show only a generic "Money Services" label; check cashing, money orders, bill pay, and load/unload are not named, so all four flags are false. They are on the Loveland hub only, labeled to call ahead, and not on the money-order or evenings-and-weekends pages. Walmart chain fee maximums are not applied.

### Held for Richard

None in Loveland. All four Loveland-printed store pages and both Loveland-printed Post Offices geocode inside Loveland city on the current address file, and no candidate printed with another city geocodes inside Loveland. (Thornton's held Eastlake Post Office and Walmart 4567, and the Castle Rock Post Office, were not touched.)

### Left out

- **Fort Collins** (Fort Collins city; already live and unchanged): King Soopers JFK Parkway, Timberline, Midtown Marketplace (the only page in this pass naming Check Cashing and Western Union), CEDARWOOD, North College Marketplace; Walmart 2729 (1250 E Magnolia St) and 3177 (4625 S Mason St).
- **Windsor** (Windsor town; not in the approved batch): King Soopers Windsor (1520 Main St). Official city and geocoder agree it is outside Loveland, so it is left off, not held.
- **Timnath** (Timnath town): Walmart 4599 (4500 Weitzel St).
- **Greeley** (Greeley city; already live and unchanged): King Soopers North Gate Village, Westlake (geocoder matched 2100 N 35TH AVE), University Square; Walmart 5051 (920 47th Ave) and 980 (3103 S 23rd Ave; geocoder matched 3103 23RD AVE).
- **Longmont** (Longmont city; already live and unchanged): King Soopers North Main, Pace Street, Hover Street (geocoder matched 995 HOVER ST); Walmart 5370 and 905 from the Longmont file.
- **Farther south:** King Soopers Firestone (Firestone town; geocoder matched 6110 FIRESTONE TRL), Gun Barrel and 30th Street Boulder (Boulder city), Highway 287 and Arapahoe Road (Erie town), LOUISVILLE (Louisville city). King Soopers Frederick (5801 Silverstone Dr) and VISTA RIDGE (1891 State Highway 7, Erie) had no address match on the current or 2020 file; their OpenStreetMap points (supplementary, non-official) return Frederick town and Erie town.
- **Walmart Neighborhood Markets:** none appeared. Fuel centers are not separate rows.
- **Berthoud, Johnstown, Milliken, Wellington, Evans:** no King Soopers or Walmart store printed with those cities in either official source.

## Not collected

- Payday / title-loan storefronts, including ACE: omitted by policy.
- Stand-alone Western Union / MoneyGram agents and other grocery brands (Safeway, Sprouts, etc.) were not collected.
