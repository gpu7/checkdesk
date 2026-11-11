# Step 8: Thornton (2026-11-11, America/Denver)

**Rows:** 5 (4 King Soopers, 1 Walmart Supercenter hub-only, 0 USPS). City 3 of the approved six-city batch (Colorado Springs, Fort Collins, Thornton, Arvada, Westminster, Greeley). Only addresses inside Thornton city limits are listed. No businesses were contacted.

**Counts:** 5 locations; 4 money orders (4 King Soopers); 0 check cashing; 0 bill pay; 0 prepaid reload. Labels: 5 Open evenings, 5 Open weekends (the evenings/weekends page shows 4 because the hub-only Walmart row lists no service). No check-cashing or bill-pay page (zero listings).

## Method

- **USPS:** official USPS Location Finder (tools.usps.com, `locationType` PO). Searches at 5 and 15 miles around Thornton-area ZIPs (80229, 80233, 80241, 80260, 80602, 80023, 80234, 80221, 80640, 80614). The candidate's official record (`https://tools.usps.com/locations/details/<id>`) was read on 2026-11-11.
- **City limits:** every candidate address was checked with the U.S. Census Bureau Geocoder (https://geocoding.geo.census.gov/geocoder/, address endpoint, Public_AR_Current / Current_Current, Incorporated Places and Census Designated Places layers) on 2026-11-11. The `city` column keeps the official mailing city.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands.

## USPS

No Thornton USPS row is listed. The locator returned no office with a Thornton mailing city.

### Held for Richard: Eastlake Post Office (USPS 1361915)

- Official page: EASTLAKE, 12470 York St, Eastlake CO 80614, 303-252-7112. Services include Domestic and Inquiry Money Orders. Posted retail (BUSINESS) hours Mon-Fri 08:00-13:00 and 14:00-17:00, Sat 09:00-12:00, Sun closed (would be Open weekends, not Open evenings).
- Census geocoder: **no match** for the official address (12470 York St, Eastlake, 80614), and no match with the ZIP alone. The same street address matches only when entered as Thornton 80241 (12470 YORK ST, THORNTON, CO, 80241, Thornton city).
- Coordinate backup: the official locator point (39.922264, -104.958444) falls inside Thornton city on the Census coordinates endpoint (Incorporated Places, Current_Current).
- Held because the official address did not match and the official mailing city (Eastlake) differs from the geocoder's city. Not added.

### Out of city (geocoder confirmed)

- Northglenn, 11887 Washington St 80233: Northglenn city.
- Northview, 850 W 112th Ave, Northglenn 80234: Northglenn city.
- Henderson, 12210 Brighton Rd 80640: no incorporated place (unincorporated Adams County).
- Dupont, 8096 Brighton Rd, Commerce City 80022: Derby CDP (unincorporated).
- North Pecos, 1411 Cortez St, Denver 80221: Sherrelwood CDP (unincorporated).
- Westminster (3051 W 105th Ave) and other results (Denver, Commerce City, Brighton, Broomfield, etc.) are other cities. Westminster is a later batch city and was not started.
- USPS contract postal units and Approved Postal Providers were not collected.

## Walmart Supercenters and King Soopers

Official store pages were opened in a browser on 2026-11-11 (read-only; no sign-in, no store contact). Raw results: `docs/research/step8-browser/thornton-walmart-ks-2026-11-11.csv` and `.md` (19 detail pages: 10 King Soopers, 9 Walmart). The King Soopers Thornton city directory (kingsoopers.com/stores/grocery/co/thornton) lists the same four Thornton stores. Every address was run through the Census geocoder on 2026-11-11.

### Added (5 rows)

| Store | Address | Geocoder | Services listed |
|---|---|---|---|
| Walmart Supercenter 1231 Thornton Grant St | 9901 Grant St 80229 | Thornton city | Money Services only: hub only, all flags false |
| King Soopers 00024 104th and Washington | 750 E 104th Ave Unit A 80233 | Thornton city | Money orders |
| King Soopers 00068 Mission Trace | 3801 E 120th Ave 80233 | Thornton city | Money orders |
| King Soopers 00101 136th and Colorado Blvd | 13700 Colorado Blvd 80602 | Thornton city | Money orders |
| King Soopers 00116 136th and Quebec | 13525 Quebec St 80602 | Thornton city | Money orders |

- **Hours:** Walmart row uses store hours (Mon-Sun 6am-11pm). King Soopers rows use store hours (Sun-Sat 6 AM-11 PM), never pharmacy or fuel hours. All five are labeled Open evenings and Open weekends; the Walmart row does not appear on the evenings/weekends page because it lists no service.
- **Walmart:** the Thornton Supercenter page shows only the generic "Money Services" label; check cashing, money orders, bill pay, and load/unload are not named. All four flags are false; hub-only with "call ahead" copy. Chain fees are not applied. Denver Supercenter tags were not copied.
- **King Soopers:** `money_orders=true` on all four (each page tags "Money Orders"). No page tagged Check Cashing, bill pay, or prepaid reload, so there is no check-cashing or bill-pay page. No Western Union or MoneyGram text was recorded. (A web snippet of the Mission Trace page also shows "Account Funding" in its department list; it is not one of the four service tags and is not mapped.)
- No new fee rows. King Soopers fees stay "Not published, call ahead."

### Held for Richard

- **Walmart Supercenter 4567, Brighton E 128th Ave** (7101 E 128th Ave, printed Brighton 80602, 303-209-4339): the Census geocoder matches the address in **Thornton city**, but the official page prints Brighton. Page shows only generic "Money Services" (it would be hub-only, all flags false). Held because official city and geocoder disagree; not listed in either city.
- **Eastlake Post Office** (above).

### Left out

- Out of city (geocoder confirmed): King Soopers 00034 Federal Heights (prints Denver; Federal Heights city, already on the Federal Heights page), 00062 104th and Federal (Westminster), 00092 Commerce City Plaza and 00114 104th and Chambers (Commerce City), 00081 4th and Bromley Lane (Brighton), 00086 Broomfield on Sheridan (Broomfield). Walmart Supercenters 3867, 3824, 2223 (Westminster), 2752 (Commerce City), 1659 (Brighton).
- Walmart Neighborhood Markets: 3019 Thornton E 88th Ave (850 E 88th Ave, inside Thornton) and 4747 Northglenn are not listed by policy. Fuel centers are not separate rows.

### Coverage limits

King Soopers locator: 34 results on 4 pages; the 10 near Thornton were opened, and the Thornton city directory confirms four Thornton stores. Walmart finder search returned "0 stores", so the browser pass used Walmart's store directory instead; a press-and-hold challenge appeared and was completed. A public Walmart store list for Colorado showed no other Thornton-printed Walmart.

## Not collected

- Payday / title-loan storefronts, including ACE: omitted by policy.
- Stand-alone Western Union / MoneyGram agents and other grocery brands (City Market, Safeway, etc.) were not collected; the browser pass recorded no other-brand leads.
