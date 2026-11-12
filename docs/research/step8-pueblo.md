# Step 8: Pueblo (2026-11-12, America/Denver)

**Rows:** 8 (4 USPS, 2 King Soopers, 2 Walmart Supercenters hub-only). City 1 of the batch approved on 2026-11-12 (Pueblo, Centennial, Boulder, Longmont, Castle Rock; ranked from Census Vintage 2025, SUB-IP-EST2025-POP-08). Only addresses inside Pueblo city limits are listed. Pueblo West (unincorporated, a Census Designated Place) is not part of the City of Pueblo and is not listed. No businesses were contacted.

**Counts:** 8 locations; 6 money orders (4 USPS, 2 King Soopers); 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 6 Open evenings, 7 Open weekends. The evenings/weekends page lists 5 (4 Open evenings, 5 Open weekends): the two hub-only Walmart rows list no service, and the Midtown Post Office (weekdays 10:00-17:00, no weekend hours) earns neither label. No check-cashing or bill-pay page (zero listings).

## Method

- **USPS:** official USPS Location Finder (tools.usps.com, `locationType` PO), same method as Greeley/Westminster/Arvada. Searches at 5 and 15 miles around Pueblo-area ZIPs (81001, 81003, 81004, 81005, 81006, 81008, and Pueblo West 81007), plus wider 30- and 50-mile checks. Each candidate's official record (`https://tools.usps.com/locations/details/<id>`) was read on 2026-11-12. Retail (BUSINESS) hours, phone, and services come from that record; lobby, passport, and collection hours are not used.
- **City limits:** every candidate address was checked with the U.S. Census Bureau Geocoder (https://geocoding.geo.census.gov/geocoder/, address endpoint, Public_AR_Current / Current_Current, Incorporated Places and Census Designated Places layers) on 2026-11-12. Raw results: `docs/research/step8-browser/pueblo-usps-geocoder-2026-11-12.jsonl` and `pueblo-stores-geocoder-2026-11-12.jsonl`. Fallback checks (Census 2020 benchmark and coordinates lookup of the official USPS locator point) for two Post Offices: `pueblo-usps-geocoder-fallback-2026-11-12.jsonl`.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands.

## USPS

| Office | Address | Geocoder | Services | Retail hours |
|---|---|---|---|---|
| Belmont (1354585) | 1025 E US Highway 50 Byp 81001 | Pueblo city (official locator point; see below) | Domestic and Inquiry Money Orders | Mon-Fri 09:00-17:00, Sat 09:00-12:00, Sun closed |
| Midtown (1373010) | 1000 W 6th St Ste U 81003 | Pueblo city (official locator point; see below) | Domestic and Inquiry Money Orders | Mon-Fri 10:00-17:00, Sat and Sun closed |
| Pueblo (1378515) | 1022 Fortino Blvd 81008 | Pueblo city (matched as 1022 W FORTINO BLVD, same number and ZIP) | Domestic and Inquiry Money Orders | Mon-Fri 09:00-18:00, Sat 10:30-13:30, Sun closed |
| Sunset (1384024) | 3000 Wedgewood Dr 81005 | Pueblo city | Domestic and Inquiry Money Orders | Mon-Fri 09:00-17:30, Sat 10:30-13:00, Sun closed |

- Belmont: Open weekends (closes 17:00 on weekdays, so not Open evenings). Phone 719-543-7163.
- Midtown: no label. Phone 719-544-0365.
- Pueblo Post Office: Open evenings and Open weekends. Phone 719-543-4988.
- Sunset: Open evenings and Open weekends. Phone 719-564-3147.
- **Belmont, locator-point check (Westminster method):** the official USPS locator prints PUEBLO 81001. The current and Census 2020 address benchmarks, with every spelling tried (Byp, Bypass, E Highway 50), return only `1025 US HWY 50, PUEBLO, CO, 81008`: a different ZIP, about 3.6 km from the locator point. That match is not treated as the same address. The official USPS locator point (38.286995, -104.594254) falls inside Pueblo city on the Census coordinates lookup. Printed city and coordinates agree (Pueblo), so the row is included, with this recorded in the row notes. (The rejected 81008 match is also in Pueblo city, so no reading puts it in another place.)
- **Midtown, locator-point check (Westminster method):** the official locator prints PUEBLO 81003. The current and Census 2020 benchmarks returned no address match, with or without "Ste U" (without the ZIP, the geocoder offered only 1000 E 6th St, 81001, a different street direction, not used). The official USPS locator point (38.272504, -104.621066) falls inside Pueblo city on the Census coordinates lookup. Printed city and coordinates agree, so the row is included, with this recorded in the row notes.

Out of city (printed another place): Avondale 1353798 (Avondale CDP, unincorporated); Boone 1355427 (Boone town); Penrose 1377189 (Penrose CDP); Wetmore 1387412 (no address match; prints Wetmore). Beulah, Florence, Fountain, Rye, Cañon City, Colorado Springs, and other offices from the wider searches print other places and were not candidates. No Post Office in the locator results printed Pueblo West; no other Post Office printed Pueblo. USPS contract postal units and Approved Postal Providers were not collected.

## Walmart Supercenters and King Soopers

Official store pages were opened in a browser on 2026-11-12 (read-only; no sign-in, no store contact). Raw results: `docs/research/step8-browser/pueblo-walmart-ks-2026-11-12.csv` and `.md` (28 detail pages: 13 King Soopers, 15 Walmart, of which 10 Supercenters and 5 Neighborhood Markets). Every address was run through the Census geocoder on 2026-11-12. All 5 Pueblo-printed stores geocode inside Pueblo city. No store printed with another city geocodes inside Pueblo.

### Added (4 rows)

| Store | Address | Geocoder | Services listed |
|---|---|---|---|
| King Soopers 00043 Northside on 29th Street | 102 W 29th St 81008 | Pueblo city (page prints `29Th`; matched 102 W 29TH ST, same number, street, and ZIP) | Money orders |
| King Soopers 00012 Southside on Northern Avenue | 3050 W Northern Ave 81005 | Pueblo city | Money orders |
| Walmart Supercenter 842 Pueblo Dillon Drive | 4200 Dillon Dr 81008 | Pueblo city | Money Services only: hub only, all flags false |
| Walmart Supercenter 1001 Pueblo W Northern Ave | 4080 W Northern Ave 81005 | Pueblo city | Money Services only: hub only, all flags false |

- **Hours:** store hours only (Walmart Mon-Sun 6am-11pm; King Soopers Sun-Sat 6 AM-11 PM). Pharmacy, fuel, and holiday hours not used. All four are Open evenings and Open weekends.
- **Walmart:** each Supercenter page shows only the generic "Money Services" label; check cashing, money orders, bill pay, and load/unload are not named. All four flags false; hub-only with "call ahead" copy; chain fees not applied. Walmart 842 lists a Fuel Station as a department; it is not a separate row.
- **King Soopers:** both pages tag "Money Orders" and "Money Services" (`money_orders=true`). No check cashing, bill pay, prepaid reload, Western Union, or MoneyGram named. King Soopers fees stay "Not published, call ahead." Southside lists Gas Station/Diesel departments; not separate rows.

### Held for Richard

None in Pueblo. Every Pueblo-printed candidate matched inside Pueblo city, and no candidate printed with another city geocodes inside Pueblo. (Thornton's held Eastlake Post Office and Walmart 4567 were not touched.)

### Left out

- **Walmart Neighborhood Market 5828** (2730 S Prairie Ave, Pueblo 81005): geocodes inside Pueblo city, but Neighborhood Markets are excluded by policy (its page also shows no Money Services label).
- **Walmart Supercenter 3382** (78 N Mcculloch Blvd, printed Pueblo West 81007): the geocoder matched 78 N MCCULLOCH BLVD, PUEBLO WEST, CO, 81007 in the Pueblo West CDP, with no incorporated place. Pueblo West is unincorporated, not the City of Pueblo. Printed city and geocoder agree, so this is not a hold; it is left off. Unincorporated places stay off unless Richard asks.
- Out of city (geocoder confirmed or printed elsewhere): King Soopers 00417 Canon City (Cañon City city); 00153 Fountain (printed Fountain; no address match); Walmart 1273 (Fountain city) and 3018 (printed Fountain 80906; no address match). The Colorado Springs King Soopers (9) and Walmart (9) pages opened print Colorado Springs; those that matched geocode inside Colorado Springs city, and the rest had no match. They are not Pueblo candidates, and the Colorado Springs CSV was not changed (Constitution Avenue and other stores left off there stay off).
- Fuel centers are not separate rows.
- Existing city CSVs were not changed.

### Coverage limits

King Soopers locator ("Pueblo, CO"): 2 results, both opened. Fountain, Cañon City, and 9 Colorado Springs King Soopers were also opened; other Colorado Springs King Soopers (farther out) were not opened and are not Pueblo candidates. Walmart: official store directory for Pueblo (3 stores, all opened), Pueblo West (1), Fountain (2), and Colorado Springs (9); directories for Cañon City, Florence, Penrose, Rock Creek, Avondale, Rye, and Walsenburg returned no Walmart stores. A press-and-hold check appeared once and was completed. No new-brand leads surfaced.

## Not collected

- Payday / title-loan storefronts, including ACE: omitted by policy.
- Stand-alone Western Union / MoneyGram agents and other grocery brands (Safeway, Albertsons, etc.) were not collected.
