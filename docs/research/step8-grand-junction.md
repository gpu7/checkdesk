# Step 8: Grand Junction (2026-11-12, America/Denver)

**Rows:** 3 (1 Post Office, 2 Walmart Supercenters). City 3 of the batch approved on 2026-11-12 (Loveland, Broomfield, Grand Junction, Parker, Littleton; ranked from Census Vintage 2025, SUB-IP-EST2025-POP-08). Only addresses inside the City of Grand Junction (incorporated place, "Grand Junction city" / Mesa County in the Census geocoder) are listed. No businesses were contacted.

**Counts:** 3 locations; 1 money orders (Grand Junction Post Office); 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 3 Open evenings, 3 Open weekends. The evenings/weekends page lists the 1 money-order location (1 Open evenings, 1 Open weekends). Both Walmart Supercenters are hub-only ("Money Services, call ahead"). No check-cashing or bill-pay page (zero listings). No King Soopers rows (none in the area).

## Method

- **USPS:** official USPS Location Finder (tools.usps.com, `locationType` PO), same method as Broomfield/Loveland/Castle Rock. Searches at 5 and 15 miles around Grand Junction ZIPs (81501, 81503, 81504, 81505, 81506, 81507) returned 8 Post Office records (`docs/research/step8-browser/grand-junction-usps-locator-2026-11-12.jsonl`). Rows link the official location pages (`https://tools.usps.com/locations/details/<id>`); hours and services come from the same official locator record those pages display. The official location pages for 1365312, 1439602 and 1469994 were also loaded on 2026-11-12 (HTTP 200); 1365312 shows Money Orders.
- **City limits:** every candidate address was checked with the U.S. Census Bureau Geocoder (https://geocoding.geo.census.gov/geocoder/, address endpoint, Public_AR_Current / Current_Current, Incorporated Places, Census Designated Places and Counties layers) on 2026-11-12. Raw results: `grand-junction-usps-geocoder-2026-11-12.jsonl` (all 8 Post Office records) and `grand-junction-stores-geocoder-2026-11-12.jsonl` (all 6 Walmart store pages).
- **Fallback checks:** Census 2020 benchmark (Public_AR_Census2020) one-line lookups and current-benchmark coordinates lookups of official USPS locator points, for the Fruitvale Post Office (held, below), and for Walmart 1058 in Montrose (no address match on either file; an OpenStreetMap point was used as a supplementary, non-official check, returning Montrose city, matching the printed city). Raw results: `grand-junction-geocoder-fallback-2026-11-12.jsonl`. No listed row used a fallback.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands.

## USPS

| Office | Address | Geocoder | Services | Retail hours |
|---|---|---|---|---|
| Grand Junction (1365312) | 241 N 4th St 81501 | Grand Junction city (241 N 4TH ST, GRAND JUNCTION, CO, 81501; Mesa County); official locator point also Grand Junction city | Domestic and Inquiry Money Orders | Mon-Fri 09:00-17:15, Sat 10:00-13:30, Sun closed |

- Grand Junction Post Office: Open evenings (closes 17:15 on weekdays) and Open weekends. Phone 970-244-3400.
- **Grand Junction Carrier Annex (1469994)**, printed 734 Scarlet St, Grand Junction 81505: geocoder matched 734 SCARLET DR in Grand Junction city (official locator point also Grand Junction city). Its official record lists no retail (BUSINESS) hours and no money orders or other tracked service (carrier/delivery unit, PO pickup only), so it is not added, the same way the Castle Rock Post Office was handled. Reported for Richard to decide later.
- No duplicate records at the same address appeared.

### Held for Richard

- **Fruitvale Post Office (1439602)**, 2923 North Ave Ste 4, printed **Grand Junction**, CO 81504; phone 970-241-0826; official locator lists Domestic and Inquiry Money Orders; retail hours Mon-Fri 09:00-17:00, Sat 09:00-12:30. The Census geocoder matches 2923 NORTH AVE, GRAND JUNCTION, CO, 81504 on both the current and 2020 address files, but in **no incorporated place and no CDP** (unincorporated Mesa County). The official USPS locator point (39.076688, -108.510858) also returns no place or CDP on the coordinates lookup. Official printed city and geocoder disagree, so it is **held and not added**. (Nearby Walmart 1280 at 2881 North Ave is inside the city.)

### Out of city (left off, not held)

Printed another place and the geocoder agrees it is outside Grand Junction: Clifton 1358375 (Clifton CDP); Palisade 1376630 (Palisade town); Fruita 1364219 (Fruita city); Loma 1370811 (Loma CDP); Whitewater 1387591 (no place or CDP, Mesa County). No Post Office printed with another city geocodes inside Grand Junction. USPS contract postal units and Approved Postal Providers were not collected.

## Walmart and King Soopers

Official store pages were opened in a browser on 2026-11-12 (read-only; no sign-in, no store contact). Raw results: `docs/research/step8-browser/grand-junction-walmart-ks-2026-11-12.csv` and `.md` (6 Walmart detail pages: 5 Supercenters, 1 Neighborhood Market; 0 King Soopers). Walmart's store finder was not run; Walmart's official store directories for Grand Junction, Delta, Montrose and Rifle were used (the Colorado directory has no Fruita, Palisade or Clifton listings). Every address was run through the Census geocoder on 2026-11-12.

### Added (2 store rows)

| Store | Address | Geocoder | Services listed | Store hours |
|---|---|---|---|---|
| Walmart Supercenter 5099 (Grand Junction Rimrock Ave Supercenter) | 2545 Rimrock Ave 81505 | Grand Junction city (2545 RIMROCK AVE, GRAND JUNCTION, CO, 81505) | Generic "Money Services" only (hub-only) | Mon-Sun 6am-11pm |
| Walmart Supercenter 1280 (Grand Junction N Ave Supercenter) | 2881 North Ave 81501 | Grand Junction city (2881 NORTH AVE, GRAND JUNCTION, CO, 81501) | Generic "Money Services" only (hub-only) | Mon-Sun 6am-11pm |

- Phones from the official pages: 5099 970-248-0031; 1280 970-241-6061.
- **Walmart:** both pages show only a generic "Money Services" label; check cashing, money orders, bill pay, and load/unload are not named, so all four flags are false. They are on the Grand Junction hub only, labeled to call ahead, and not on the money-order or evenings-and-weekends pages. Walmart chain fee maximums are not applied. No page mentions Western Union.
- **Hours:** store hours only. Pharmacy, fuel, sensory-friendly, and holiday hours not used. Both stores are Open evenings and Open weekends.

### Left out

- **King Soopers:** the official King Soopers locator search for "Grand Junction, CO" returned 7 stores, none of them King Soopers. There is no King Soopers row.
- **City Market (not an approved brand; not opened, no rows):** all 7 King Soopers-locator results were City Market stores. City Market is a brand Check Desk has not been approved to list, so these pages were not opened and nothing was added. Printed names/addresses from the locator: 12th Street Grand Junction (2600 N 12th St, Grand Junction 81501); Orchard Mesa (2770 Highway 50, Grand Junction 81503); 24 Road Grand Junction (630 24 Rd, Grand Junction 81505); Clifton (569 32 Rd, Grand Junction 81504); Fruita (135 S Plum St, Fruita 81521); Delta (122 Gunnison River Dr, Delta 81416); Hotchkiss (215 6th St, Hotchkiss 81419). These were not geocoded or checked for services. No Safeway appeared. Open for Richard to decide later.
- **Walmart Neighborhood Market 4491** (Grand Junction Warrior Way, 541 Warrior Way 81504): geocoder places it in Grand Junction city (541 WARRIOR WAY, GRAND JUNCTION, CO, 81504), but Neighborhood Markets are excluded by standing policy; its page also shows no Money Services tag. Its fuel station is not a row.
- **Walmart Supercenters in other cities:** Delta 5458 (37 Stafford Ln; Delta city); Rifle 5232 (1000 Airport Rd; Rifle city); Montrose 1058 (16750 S Townsend Ave; no Census address match on current or 2020 file; OpenStreetMap point returns Montrose city). Official city and geocoder agree they are outside Grand Junction.
- Fuel centers are not separate rows.

## Not collected

- Payday / title-loan storefronts, including ACE: omitted by policy.
- Stand-alone Western Union / MoneyGram agents and other grocery brands (City Market, Safeway, etc.) were not collected.
