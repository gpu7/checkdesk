# New Orleans, Louisiana USPS research (2026-11-16, America/Denver)

First Louisiana city in the standing 50-state run (ship order: New Orleans, Baton Rouge, Shreveport, Lafayette, Lake Charles). Post Offices only. Hours labeled Central Time.

## Census place

New Orleans city, GEOID 2255000, Vintage 2025 population 362,154. The SUMLEV 162 place equals Orleans Parish (GEOID 22071, FUNCSTAT C). Census publishes no balance label and no SUMLEV 170 row. There are no other incorporated places in Orleans Parish. Nearby Jefferson Parish places, including Metairie, Kenner, Gretna, Elmwood, River Ridge, Harahan, and Westwego, are not on this page.

## Listed (6)

All six print New Orleans, LA, list Domestic Money Orders on the official USPS location page, and match New Orleans city (GEOID 2255000) on both Census address files and both official map points. No map-point fallback. OpenStreetMap was not used.

- Bywater (1356548, 1521 Poland Ave, New Orleans, 70117). Weekdays 09:00-15:00; Saturday 09:00-12:00.
- Carrollton (1357128, 3400 S Carrollton Ave, New Orleans, 70118). Weekdays 08:00-16:30; Saturday 08:00-12:00.
- Lake Forest Station (1369573, 9600 Lake Forest Blvd, New Orleans, 70127). Weekdays 08:30-16:30; Saturday 09:00-12:00.
- New Orleans Main Office Window Service (1374825, 701 Loyola Ave, New Orleans, 70113). Official locator name: N O MAIN OFC WINDOW SVE. Weekdays 07:30-19:00; Saturday 08:00-15:00.
- Station A Algiers (1383422, 3901 MacArthur Blvd, New Orleans, 70114). In the Algiers neighborhood, still inside New Orleans city. Weekdays 08:30-17:00; Saturday 08:30-12:00.
- Uptown Station (1385560, 2000 Louisiana Ave, New Orleans, 70115). Weekdays 08:00-16:30; Saturday 08:00-12:00.

Evenings: 1 (New Orleans Main Office Window Service until 19:00). Weekends: 6 (all Saturday, none Sunday). A 17:00 close does not count as Open evenings.

## Holds (9)

### Official page does not list money orders (7)

All seven print New Orleans, LA and geocode in New Orleans city on all four legs.

- Central Carrier Annex (1578078, 1300 Florida Ave, 70119; no BUSINESS hours).
- Central Carrier Station (1357503, 1300 Florida Ave, 70119; no BUSINESS hours).
- Chef Menteur (1357763, 5919 Chef Menteur Hwy, 70126).
- Gentilly Finance (1364630, 2051 Caton St, 70122).
- Lafayette Square (1369498, 600 S Maestri Pl, 70130; midday closure 13:00-14:00 weekdays). This is the New Orleans neighborhood office, not Lafayette, Louisiana (`/lafayette-la/`) and not Lafayette, Colorado (`/lafayette/`).
- Lakeview (1369695, 6319 Marshal Foch St, 70124).
- New Orleans (1374824, 701 Loyola Ave, 70113; no BUSINESS hours). Same printed street as the listed window-service office.

### Mid City Finance (1372913)

501 Moss St, New Orleans 70119. Official page lists only Inquiry Money Orders, not Domestic Money Orders, so it is not listed (it does publish Saturday hours 08:30-13:00). Address retries (8 street variants, with and without ZIP 70119, current and 2020 files, 32 queries) never matched 501 Moss St in New Orleans city. Lookups that produced a hit consistently snapped to 501 MOSS LN, NEW ORLEANS, LA, 70123 in River Ridge CDP (GEOID 2265150), Jefferson Parish, a different street and ZIP. The official USPS locator map point (29.974048, -90.091995) is in New Orleans city on both the current and 2020 benchmarks. Not listed; no map-point fallback, because the page does not list Domestic Money Orders.

### Printed New Orleans but not inside the city (1)

- Elmwood (1438932, 5720 Citrus Blvd, New Orleans 70123). Lists Domestic Money Orders and Inquiry Money Orders. Both official map points fall in Elmwood CDP (GEOID 2223567), Jefferson Parish, not New Orleans city. Neither the current nor the 2020 Census address file matched 5720 CITRUS BLVD. Held as a printed-city vs geocode mismatch.

No other office in the Louisiana locator sweep geocodes into New Orleans city. No hold_other_printed_city rows.

## Result

6 listed Post Offices, all with money orders. 1 Open evenings. 6 Open weekends. Hours labeled Central Time. 9 holds (7 no money-order tags inside the city; Mid City Finance, inquiry-only and no in-city address match; Elmwood, in Elmwood CDP). No map-point fallback.

## Site changes in this PR

- New `data/locations/new-orleans.csv` and `/new-orleans/`, `/new-orleans/money-orders/`, and `/new-orleans/after-hours/` pages.
- New Orleans is added as the first Louisiana city, after Kentucky, on the home page and `/cities/`. Home and `/cities/` meta now say Louisville, Lexington, Bowling Green, Owensboro, and Covington, Kentucky, and New Orleans, Louisiana. Lafayette, Colorado (`/lafayette/`, `data/locations/lafayette.csv`) was not changed. The Louisiana Census Vintage 2025 ranking memo is added under `docs/research/`. No other city CSV or page changed except those meta and list lines.
