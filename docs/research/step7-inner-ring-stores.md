# Step 7: inner-ring Walmart Supercenter and King Soopers fill (2026-11-11, America/Denver)

Official store pages were opened in a browser on 2026-11-11 between about 09:16 and 09:35 America/Denver (read-only; no businesses contacted). Every new address was checked with the U.S. Census Bureau geocoder (https://geocoding.geo.census.gov/geocoder/, Public_AR_Current / Current_Current, Incorporated Places layer) on 2026-11-11. All 27 new addresses and King Soopers 00034 matched, and every match fell inside the named city. No geocoder disagreements.

## Added (27 rows)

| City | Walmart Supercenters (hub only) | King Soopers with money orders tagged | King Soopers hub only (Money Services, no money-order tag) |
|---|---|---|---|
| Aurora | 1492, 5334, 1689, 5137 | 00010, 00014, 00052, 00030, 00049, 00128, 00069, 00084 | 00139 Nine Mile |
| Lakewood | 4284, 2125 | 00031, 00059, 00040, 00060 | 00127 Belmar |
| Englewood | 2751 | 00065, 00109 | 00111 Fresh Fare (06:00-22:00) |
| Commerce City | 2752 (5990 Dahlia St) | 00092, 00114 | none |
| Wheat Ridge | none (no Supercenter in city limits) | 00057, 00020 | none |
| Federal Heights | none (no Supercenter in city limits) | 00034 (updated, not new) | none |

## Service flags

- **Walmart:** every new Supercenter page showed only a generic "Money Services" label in its Services list. Check cashing, money orders, bill pay, and load/unload were not named, and no fees were shown. All four service flags are therefore false, and the stores appear on city hubs only (Money Services, call ahead), like Denver King Soopers Union Station and Central Park. This differs from the three Denver Supercenters collected on 2026-11-10, whose pages named those services. We did not copy the Denver tags or Walmart chain policy onto these stores. Page copy says so on each affected hub.
- **King Soopers:** `money_orders=true` only where the store page tagged "Money Orders". Check cashing, bill pay, and prepaid reload were not tagged on any page, so they stay false. 00139, 00127, and 00111 tag only Money Services, so they are hub-only and do not appear on the money-order or evenings/weekends pages.
- No new fee rows. Existing fees.csv / fee-display.json entries are reused. King Soopers fees stay "Not published, call ahead."
- Because no new row lists check cashing, bill pay, or prepaid reload, no inner-ring check-cashing or bill-pay pages were added. The build refuses empty lists.

## King Soopers Federal Heights 00034

The store page was re-opened on 2026-11-11. It shows Sun-Sat 6 AM-11 PM, phone 303-427-9176, and Money Orders + Money Services tags (no check cashing). It still prints Denver, CO 80260. The Census geocoder again places 1575 W 84th Ave in Federal Heights city (Adams County), so the row stays on the Federal Heights page with the mailing-address note. `last_verified` is now 2026-11-11.

## Omitted

- Walmart Neighborhood Markets #4196 (15240 E Iliff Ave) and #3740 (21475 E Quincy Ave), Aurora: smaller format; their store pages were not opened for services.
- Out of city: Walmart Lakeside #5957 (nearest to Wheat Ridge), Denver #3566/#3533/#5676, Arvada, Thornton, and Westminster stores; King Soopers Denver, Thornton, Edgewater, Centennial, Arvada, Westminster, and others; and King Soopers fuel centers.
- Still omitted from Step 6: USPS North Pecos, Dupont, and other unincorporated Adams County (Sherrelwood, Derby) addresses, plus Watkins Post Office.

## Coverage limits

- King Soopers search pages 1-3 were read for each city (1-4 for Aurora). A store listed only on later pages could be missing.
- The Walmart city directories for Wheat Ridge, Commerce City, and Federal Heights were empty. The ZIP store finder (80033, 80212, 80022, 80260) found #2752 in Commerce City and no Supercenter in Wheat Ridge or Federal Heights.
- Walmart showed a bot check on some pages. One press-and-hold cleared it; no account or login was used.
