# Step 8: Boulder (2026-11-12, America/Denver)

**Rows:** 6 (3 USPS, 3 King Soopers). City 3 of the batch approved on 2026-11-12 (Pueblo, Centennial, Boulder, Longmont, Castle Rock; ranked from Census Vintage 2025, SUB-IP-EST2025-POP-08). Only addresses inside Boulder city limits are listed. No Walmart: Walmart's official Boulder store directory lists no stores, and no Walmart page opened prints a Boulder address. No businesses were contacted.

**Counts:** 6 locations; 6 money orders (3 USPS, 3 King Soopers); 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 6 Open evenings, 6 Open weekends. The evenings/weekends page lists the same 6 (6 Open evenings, 6 Open weekends). No hub-only rows. No check-cashing or bill-pay page (zero listings).

## Method

- **USPS:** official USPS Location Finder (tools.usps.com, `locationType` PO), same method as Centennial/Pueblo/Greeley/Westminster. Searches at 5 and 15 miles around Boulder ZIPs (80301, 80302, 80303, 80304, 80305, 80310). Each candidate's official record (`https://tools.usps.com/locations/details/<id>`) was read on 2026-11-12. Retail (BUSINESS) hours, phone, and services come from that record; lobby, passport, and collection hours are not used.
- **City limits:** every candidate address was checked with the U.S. Census Bureau Geocoder (https://geocoding.geo.census.gov/geocoder/, address endpoint, Public_AR_Current / Current_Current, Incorporated Places and Census Designated Places layers) on 2026-11-12. Raw results: `docs/research/step8-browser/boulder-usps-geocoder-2026-11-12.jsonl` (all 25 Post Office records the searches returned) and `boulder-stores-geocoder-2026-11-12.jsonl` (all 39 store pages). Extra check for the Gun Barrel store: coordinates lookup of its address match, `boulder-gunbarrel-coordinates-2026-11-12.jsonl`. No fallback (Census 2020 benchmark or locator-point) check was needed: every listed row matched on the current benchmark.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands.

## USPS

| Office | Address | Geocoder | Services | Retail hours |
|---|---|---|---|---|
| Boulder (1355494) | 1905 15th St 80302 | Boulder city (1905 15TH ST, BOULDER, CO, 80302) | Domestic and Inquiry Money Orders | Mon-Fri 08:30-17:30, Sat 10:00-14:00, Sun closed |
| High Mar (1366905) | 4985 Moorhead Ave 80305 | Boulder city (4985 MOORHEAD AVE, BOULDER, CO, 80305) | Domestic and Inquiry Money Orders | Mon-Fri 09:00-17:30, Sat 10:00-13:00, Sun closed |
| Valmont (1385692) | 2995 55th St 80301 | Boulder city (2995 55TH ST, BOULDER, CO, 80301) | Domestic and Inquiry Money Orders | Mon-Fri 09:00-18:00, Sat 10:00-14:00, Sun closed |

- Boulder Post Office: Open evenings and Open weekends. Phone 303-938-3704.
- High Mar Post Office: Open evenings and Open weekends. Phone 303-494-5006.
- Valmont Post Office: Open evenings and Open weekends. Phone 720-564-6450.
- **Boulder CO SDC 1612987**: a second locator record at the same address as Valmont (2995 55th St), with the same retail hours; its record does not list money orders. Not listed twice.

Out of city (printed another place, and the geocoder agrees or found no match): Niwot 1375136 (Niwot CDP, unincorporated); Louisville 1371024 (566 S McCaslin Blvd, printed Superior, geocodes Louisville city); Lafayette 1369494 and Lafayette Carrier Annex 1369484 (Lafayette city); Erie 1362695 and Erie Carrier Annex 1546616 (Erie town); Longmont 1370889 (Longmont city); Broomfield 1356062 (Broomfield city) and Broomfield Eagle View 1361605 (no match, printed Broomfield); Eldorado Springs 1362237, Hygiene 1367788, and Nederland 1374521 (no address match, printed those places); Jamestown, Lyons, and Ward (towns); Pinecliffe (no place) and Rollinsville (CDP); Westminster, Indian Tree (Arvada), Northview and Northglenn (Northglenn city) farther out. No Post Office printed with another city geocodes inside Boulder. No Gunbarrel-printed Post Office appeared in the locator results. USPS contract postal units and Approved Postal Providers were not collected.

## King Soopers and Walmart

Official store pages were opened in a browser on 2026-11-12 (read-only; no sign-in, no store contact). Raw results: `docs/research/step8-browser/boulder-walmart-ks-2026-11-12.csv` and `.md` (39 detail pages: 30 King Soopers, 9 Walmart Supercenters). No Neighborhood Market pages were opened. Every address was run through the Census geocoder on 2026-11-12. All 3 Boulder-printed stores geocode inside Boulder city. No store printed with another city geocodes inside Boulder.

### Added (3 rows)

| Store | Address | Geocoder | Services listed |
|---|---|---|---|
| King Soopers 00061 30th Street Boulder | 1650 30th St 80301 | Boulder city (1650 30TH ST, BOULDER, CO, 80301) | Money orders (and Money Services) |
| King Soopers 00033 Table Mesa | 3600 Table Mesa Dr 80305 | Boulder city | Money orders (and Money Services) |
| King Soopers 00028 Gun Barrel | 6550 Lookout Rd 80301 | Boulder city (no CDP) | Money orders (and Money Services) |

- **Spelling:** the official 30th Street page prints "1650 30Th St"; the row uses "1650 30th St". The geocoder matched the same number, street, and ZIP. Store names are written in title case ("TABLE MESA" on the page is "Table Mesa").
- **Gun Barrel (6550 Lookout Rd):** the store is in the Gunbarrel area, and the Gunbarrel CDP (unincorporated) is nearby. The official page prints Boulder 80301. The Census geocoder matched `6550 LOOKOUT RD, BOULDER, CO, 80301` in **Boulder city**, with no Census Designated Place, and a coordinates lookup of that match (-105.200869, 40.072743) also returns Boulder city only. Printed city and geocoder agree, so the row is included (not a hold, and not a coordinate-backup case).
- **Hours:** store hours only (King Soopers Sun-Sat 6 AM-11 PM). Pharmacy, fuel, and holiday hours not used. All three are Open evenings and Open weekends.
- **King Soopers:** all three pages tag "Money Orders" and "Money Services" (`money_orders=true`). No check cashing, bill pay, prepaid reload, Western Union, or MoneyGram named. "Account Funding" is not a tracked service and is not flagged. King Soopers fees stay "Not published, call ahead."
- **Walmart:** no Walmart row. Walmart's official Boulder store directory lists no stores; the 9 Supercenter pages opened print Lafayette, Longmont, Broomfield, Westminster, or Arvada.

### Held for Richard

None in Boulder. Every Boulder-printed candidate matched inside Boulder city, and no candidate printed with another city geocodes inside Boulder. (Thornton's held Eastlake Post Office and Walmart 4567 were not touched.)

### Left out

- **Other incorporated places nearby** (printed and geocoded elsewhere): Louisville (King Soopers 00142 Louisville Marketplace, which tags check cashing, and 00013), Erie (00138, 00129), Broomfield (3 King Soopers, 2 Walmart Supercenters), Longmont (3 King Soopers, 2 Walmart Supercenters; Longmont is a later city in this batch, in its own PR), Lafayette (Walmart 1045), Westminster, Arvada, Thornton, Frederick, Firestone, Golden, Wheat Ridge, and Federal Heights (printed Denver). None is a Boulder candidate, and no existing city CSV was changed.
- Fuel centers are not separate rows. Walmart Neighborhood Markets are excluded by policy (none in Boulder).

## Not collected

- Payday / title-loan storefronts, including ACE: omitted by policy.
- Stand-alone Western Union / MoneyGram agents and other grocery brands (Safeway, Sprouts, etc.) were not collected.
