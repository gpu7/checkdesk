# Step 8: Centennial (2026-11-12, America/Denver)

**Rows:** 6 (2 USPS, 3 King Soopers, 1 Walmart Supercenter hub-only). City 2 of the batch approved on 2026-11-12 (Pueblo, Centennial, Boulder, Longmont, Castle Rock; ranked from Census Vintage 2025, SUB-IP-EST2025-POP-08). Only addresses inside Centennial city limits are listed. Highlands Ranch (unincorporated, a Census Designated Place) is not part of the City of Centennial and is not listed. No businesses were contacted.

**Counts:** 6 locations; 5 money orders (2 USPS, 3 King Soopers); 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 6 Open evenings, 6 Open weekends. The evenings/weekends page lists 5 (5 Open evenings, 5 Open weekends): the hub-only Walmart row lists no service. No check-cashing or bill-pay page (zero listings).

## Method

- **USPS:** official USPS Location Finder (tools.usps.com, `locationType` PO), same method as Pueblo/Greeley/Westminster/Arvada. Searches at 5 and 15 miles around Centennial-area ZIPs (80015, 80016, 80111, 80112, 80121, 80122, 80155, 80161; the 15-mile search for 80155 returned no data, and the other ZIPs cover the same area). Each candidate's official record (`https://tools.usps.com/locations/details/<id>`) was read on 2026-11-12. Retail (BUSINESS) hours, phone, and services come from that record; lobby, passport, and collection hours are not used.
- **City limits:** every candidate address was checked with the U.S. Census Bureau Geocoder (https://geocoding.geo.census.gov/geocoder/, address endpoint, Public_AR_Current / Current_Current, Incorporated Places and Census Designated Places layers) on 2026-11-12. Raw results: `docs/research/step8-browser/centennial-usps-geocoder-2026-11-12.jsonl` (all 53 Post Office records the searches returned) and `centennial-stores-geocoder-2026-11-12.jsonl` (all 52 store pages). No fallback (Census 2020 benchmark or locator-point) check was needed: every listed row matched on the current benchmark.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands.

## USPS

| Office | Address | Geocoder | Services | Retail hours |
|---|---|---|---|---|
| Centennial (1439625) | 2221 E Arapahoe Rd 80122 | Centennial city (2221 E ARAPAHOE RD, CENTENNIAL, CO, 80122) | Domestic and Inquiry Money Orders | Mon-Fri 09:00-17:30, Sat 09:00-13:00, Sun closed |
| Tower (1432755) | 18555 E Smoky Hill Rd 80015 | Centennial city (18555 E SMOKY HILL RD, CENTENNIAL, CO, 80015) | Domestic and Inquiry Money Orders | Mon-Fri 08:00-18:00, Sat 09:00-13:00, Sun closed |

- Centennial Post Office: Open evenings and Open weekends. Phone 303-794-1285.
- Tower Post Office: Open evenings and Open weekends. Phone 303-699-8907.

Out of city (printed another place, and the geocoder agrees or found no match): Greenwood Village 1439554 (6855 S Dayton St, Greenwood Village city); Highlands Ranch 1439610 and its SDC record 1613886 (9609 S University Blvd, Highlands Ranch CDP, unincorporated); Littleton 1370671 (5753 S Prince St, Littleton city); Englewood 1362625 and Downtown Englewood 1362621 (Englewood city); Gateway, Aurora, Buckingham, Hoffman Heights, Altura, Fletcher (Aurora city); Parker 1376837 (Parker town); and Denver, Lakewood, Commerce City, Castle Rock, Franktown, Louviers, Sedalia, Watkins, and other offices farther out. No Post Office printed with another city geocodes inside Centennial. No other Post Office in the locator results printed Centennial. USPS contract postal units and Approved Postal Providers were not collected.

## Walmart Supercenters and King Soopers

Official store pages were opened in a browser on 2026-11-12 (read-only; no sign-in, no store contact). Raw results: `docs/research/step8-browser/centennial-walmart-ks-2026-11-12.csv` and `.md` (52 detail pages: 30 King Soopers, 22 Walmart, of which 17 Supercenters and 5 Neighborhood Markets). Two "Aurora Fuel" center listings from the King Soopers locator were not opened as stores (fuel centers). Every address was run through the Census geocoder on 2026-11-12. All 5 Centennial-printed stores geocode inside Centennial city. No store printed with another city geocodes inside Centennial.

### Added (4 rows)

| Store | Address | Geocoder | Services listed |
|---|---|---|---|
| King Soopers 00063 County Line and Holly | 8200 S Holly St 80122 | Centennial city | Money orders (and Money Services) |
| King Soopers 00016 Smoky Hill and Himalaya | 19711 E Smoky Hill Rd 80015 | Centennial city | Money orders (and Money Services) |
| King Soopers 00047 Cherrywood Square | 7575 S University Blvd 80122 | Centennial city | Money orders (and Money Services) |
| Walmart Supercenter 3313 Centennial E Briarwood Ave | 10900 E Briarwood Ave 80112 | Centennial city | Money Services only: hub only, all flags false |

- **Hours:** store hours only (Walmart Mon-Sun 6am-11pm; King Soopers Sun-Sat 6 AM-11 PM). Pharmacy, fuel, and holiday hours not used. All four are Open evenings and Open weekends.
- **Walmart:** the Supercenter page shows only the generic "Money Services" label; check cashing, money orders, bill pay, and load/unload are not named. All four flags false; hub-only with "call ahead" copy; chain fees not applied.
- **King Soopers:** all three pages tag "Money Orders" and "Money Services" (`money_orders=true`). No check cashing, bill pay, prepaid reload, Western Union, or MoneyGram named. King Soopers fees stay "Not published, call ahead." The check-cashing tag on Virginia Village (Denver) and the Western Union mention on Cottonwood Drive (Parker) belong to other cities and were not applied here.

### Held for Richard

None in Centennial. Every Centennial-printed candidate matched inside Centennial city, and no candidate printed with another city geocodes inside Centennial. (Thornton's held Eastlake Post Office and Walmart 4567 were not touched.)

### Left out

- **Walmart Neighborhood Market 3126** (16746 E Smoky Hill Rd, Centennial 80015): geocodes inside Centennial city, but Neighborhood Markets are excluded by policy (its page also shows no Money Services label).
- **Highlands Ranch (unincorporated, CDP):** King Soopers 00110 Quebec St (8673 S Quebec St), 00027 University and Colorado (9551 S University Blvd), 00108 Red Cedar Drive (4000 Red Cedar Dr), Walmart Supercenter 1252 (6675 Business Center Dr), and the Highlands Ranch Post Office. Each prints Highlands Ranch and geocodes in the Highlands Ranch CDP with no incorporated place. Printed city and geocoder agree, so these are not holds; they are left off. Unincorporated places stay off unless Richard asks.
- **Other incorporated places nearby** (printed and geocoded elsewhere): Greenwood Village (King Soopers 00100, 00096), Aurora (9 King Soopers, 4 Walmart Supercenters, 2 Neighborhood Markets), Englewood, Littleton, Parker, Castle Pines, Glendale, Denver, Castle Rock, Commerce City, and Lakewood stores. Some of these print one city and geocode in another (for example Walmart 3566, printed Denver, geocodes in Aurora; Walmart 1308, printed Littleton, geocodes in Denver; Walmart 5049, printed Littleton, geocodes in the Dakota Ridge CDP; Walmart 3740, printed Aurora, matched with no place; Neighborhood Market 3128, printed Denver, geocodes in the Four Square Mile CDP). None of them is in Centennial, they are not Centennial candidates, and no existing city CSV was changed.
- Fuel centers are not separate rows.
- Existing city CSVs were not changed.

### Coverage limits

King Soopers locator ("Centennial, CO"): 32 results across 4 pages; all 30 grocery store pages opened, 2 fuel centers excluded. Walmart's store finder returned 0 stores for "Centennial, CO", so Walmart's official Colorado/city store directories and nearby-store listings were used (22 pages opened). Neither directory had Greenwood Village or Lone Tree Walmart entries. A press-and-hold check appeared once and was completed. No new-brand leads surfaced.

## Not collected

- Payday / title-loan storefronts, including ACE: omitted by policy.
- Stand-alone Western Union / MoneyGram agents and other grocery brands (Safeway, Albertsons, etc.) were not collected.
