# Check Desk — Step 6 inner-ring collection notes

**Date checked / last_verified:** 2026-11-11 (America/Denver), except King Soopers Federal Heights 00034 (2026-11-10, see below).
**Scope (approved):** Aurora, Lakewood, Commerce City, Englewood, Wheat Ridge, Federal Heights. No other cities.
**City files:** `data/locations/aurora.csv`, `lakewood.csv`, `commerce-city.csv`, `englewood.csv`, `wheat-ridge.csv`, `federal-heights.csv`.

## Method

- **USPS:** official USPS Location Finder (tools.usps.com). Retail Post Offices (`locationType` PO) were found with locator searches around every ZIP that touches the six cities (80010–80019, 80045, 80247, 80214, 80215, 80226–80228, 80232, 80235, 80022, 80037, 80640, 80110, 80111, 80113, 80150, 80033, 80034, 80212, 80221, 80234, 80260, and neighbors). Each included office's official detail page (`https://tools.usps.com/locations/details/<id>`) was then opened on 2026-11-11 and its address, phone, posted retail (BUSINESS) hours, and money-order services were copied from that page.
- **City limits:** every candidate address was checked with the U.S. Census Bureau Geocoder (https://geocoding.geo.census.gov/geocoder/, Public_AR_Current benchmark, Incorporated Places layer) on 2026-11-11. A row goes in a city file only if the geocoder places it inside that city. The `city` column keeps the official mailing city from the source.
- **Walmart and King Soopers:** walmart.com (bot wall / blocked redirect) and kingsoopers.com (HTTP/2 reset, timeouts, HTTP 500 via fetch) did not load from this environment on 2026-11-11. No Walmart or King Soopers store in the six cities was added from memory, search snippets, or archives. The only grocery row is King Soopers Federal Heights 00034, which was opened on its official store page on 2026-11-10 (Step 4, `docs/research/step4-browser/kingsoopers-2026-11-10.md`), so its `last_verified` stays 2026-11-10.
- Fees reuse existing rows in `data/providers/fees.csv` (USPS money-order tiers; King Soopers money orders unpublished). No new fee rows.

## Included rows (13)

| City | Location (USPS id / store) | Address (official) | Weekday retail hours | Sat | Labels |
|---|---|---|---|---|---|
| Aurora | Altura PO 1352881 | 15355 E Colfax Ave Unit A, Aurora 80011 | 09:00–17:00 | 09:00–13:00 | Open weekends |
| Aurora | Aurora PO 1353711 | 16890 E Alameda Pkwy, Aurora 80017 | 08:00–18:00 | 07:30–15:00 | Open evenings, Open weekends |
| Aurora | Fletcher PO 1363520 | 1550 Dayton St, Aurora 80010 | 09:00–17:00 | closed | none |
| Aurora | Gateway PO 1364551 | 2500 S Abilene St, Aurora 80014 | 08:00–18:00 | 08:00–15:00 | Open evenings, Open weekends |
| Aurora | Hoffman Heights PO 1367142 | 738 Peoria St Ste D, Aurora 80011 | 09:00–17:00 | 09:00–13:00 | Open weekends |
| Aurora | Buckingham PO 1442456 | 1074 S Ironton St Unit D, Aurora 80012 | 09:00–16:30 | closed | none |
| Commerce City | Commerce City PO 1358845 | 7351 Magnolia St, Commerce City 80022 | 09:00–17:00 | 09:00–13:00 | Open weekends |
| Commerce City | Adams City PO 1439552 | 6655 Brighton Blvd, Commerce City 80022 | 09:00–11:00, 12:00–16:00 | closed | none |
| Englewood | Downtown Englewood PO 1362621 | 3330 S Broadway, Englewood 80113 | 09:00–17:00 | 09:00–13:00 | Open weekends |
| Englewood | Englewood PO 1362625 | 915 W Lehigh Ave, Englewood 80110 | 09:00–17:30 | 09:00–13:00 | Open evenings, Open weekends |
| Lakewood | Lakewood PO 1439615 | 10799 W Alameda Ave, Lakewood 80226 | 08:30–18:00 | 09:30–12:30 | Open evenings, Open weekends |
| Wheat Ridge | Wheat Ridge PO 1387437 | 4210 Wadsworth Blvd, Wheat Ridge 80033 | 09:00–17:00 | 09:00–14:00 | Open weekends |
| Federal Heights | King Soopers Federal Heights 00034 | 1575 W 84th Ave, Denver 80260 (mailing) | store 06:00–23:00 daily | 06:00–23:00 | Open evenings, Open weekends |

All USPS rows list Domestic Money Orders (Fletcher and Hoffman Heights list Domestic Money Orders only; the rest also list Inquiry Money Orders). Sunday is closed at every Post Office. Service flags: `money_orders=true` on all 13; `check_cashing`, `bill_pay`, `prepaid_reload` false on all 13 (not listed on the official pages). Adams City publishes split weekday windows; the validator and table renderer now accept `HH:MM-HH:MM,HH:MM-HH:MM`.

## Held-over locations from Step 4

- **King Soopers Federal Heights 00034:** Census geocoder places 1575 W 84th Ave in **Federal Heights city** (Adams County). Added to `federal-heights.csv` with the official Denver 80260 mailing address and a note.
- **USPS North Pecos 1375398** (1411 Cortez St, Denver, CO 80221; Mon–Fri 09:00–17:00, Sat 09:30–12:30; Domestic + Inquiry Money Orders): Census geocoder places it in **unincorporated Adams County (Sherrelwood CDP)**, not Denver and not any of the six cities, both by address and by the locator's coordinates. **Not listed anywhere.** Adding unincorporated Adams County would be new scope.

## Excluded (and why)

- **Edgewater PO 1439601** (1990 Depew St, mailing Lakewood 80214): inside the City of Edgewater, not Lakewood.
- **Dupont PO 1361498** (8096 Brighton Rd, mailing Commerce City 80022): Census geocoder places it in unincorporated Adams County (Derby CDP).
- **Watkins PO 1386636** (33151 E 16th Dr, Watkins 80137): mailing city Watkins; the address did not match in the Census geocoder, though the locator's coordinates fall inside Aurora limits. Not placed in Aurora without a clean address match. Flagged for review.
- **Glendale PO 1440283** (mailing Denver 80246): City of Glendale. **Tower PO 1432755** (mailing Centennial): Centennial. Neither is in scope.
- **USPS SDC / carrier annex entries** (Aurora CO SDC, Lakewood CO SDC): no money-order services listed; not retail counters.
- **Payday / title-loan storefronts, including ACE:** omitted from every city file by policy.

## Gaps

- **No Walmart or King Soopers rows in Aurora, Lakewood, Commerce City, Englewood, or Wheat Ridge**, and no other grocery rows in Federal Heights. Their official store pages need a browser pass. As a result, no inner-ring city has a check-cashing, bill-pay, or prepaid-reload list yet, and no `/<city>/check-cashing/` or `/<city>/bill-pay/` pages were published (the build refuses empty lists).
- **No Post Office inside Federal Heights** turned up on the official locator.
- USPS contract postal units and Approved Postal Providers were not collected.
- Western Union / MoneyGram stand-alone agents were not collected (same decision as Denver).
- No coordinates are stored in the CSVs.
