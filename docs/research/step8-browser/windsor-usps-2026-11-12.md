# Windsor, CO: USPS locator research (2026-11-12, America/Denver)

Research pass (copied here for the Windsor build; see `docs/research/step8-windsor.md`). No business was contacted. No browser was used. last_verified: 2026-11-12.

## Method

- **Locator:** official USPS Location Finder API (`https://tools.usps.com/UspsToolsRestServices/rest/POLocator/findLocations`, `requestType` po), queried with curl, the same way as Brighton, Littleton, and Parker. Searches at 5 and 15 miles around 80550 and 80551 (Windsor), 80528, 80524, and 80525 (Fort Collins), 80634 and 80631 (Greeley), 80516 (Erie), 80534 (Johnstown), 80543 (Milliken), 80615 (Eaton), 80538 (Loveland), 80547 (Timnath), and 80610 (Ault) returned **62 unique Post Office records**. Every query returned JSON. Raw records: `windsor-usps-locator-2026-11-12.jsonl` (this folder).
- **Official pages:** `https://tools.usps.com/locations/details/<id>` fetched with curl at about 3:22 PM MT. 1387952 Windsor: HTTP 200. 1560051 WIN Carrier Annex: HTTP 200. 1381248 Severance: HTTP 200. 1384692 Timnath: HTTP 200. Each page loaded on the first try . Hours and services come from the official locator record that these pages display. Retail hours means the `BUSINESS` hours block only.
- **Town limits:** U.S. Census Geocoder address endpoint, Public_AR_Current / Current_Current (Incorporated Places, CDPs, and Counties layers), checked for all 62 records (`windsor-usps-geocoder-2026-11-12.jsonl`). I also looked up every official USPS locator map point against the current benchmark. For both Windsor-printed addresses I ran one-line lookups against both the Census 2020 file and the current file. Map-point and one-line results: `windsor-geocoder-fallback-2026-11-12.jsonl`.

## Candidate include (1)

| Office | Address | Phone | Services | Retail hours | Geocoder |
|---|---|---|---|---|---|
| Windsor (1387952) | 215 6th St, Windsor 80550 | 970-833-3010 | Money orders, Domestic and Inquiry (MONEYORDERSDOM, MONEYORDERSINQ) | Mon-Fri 08:30-17:00, Sat 09:00-12:00, Sun closed | Current file: 215 6TH ST, WINDSOR, CO, 80550, **Windsor town**, Weld County. The 2020 file agrees (Windsor town), and so does the official locator point (40.479372, -104.905553). |

- URL: https://tools.usps.com/locations/details/1387952 (HTTP 200). verification_status: verified_official_locator.
- It is open Saturdays. Weekday retail closes at 17:00, so it is not "Open evenings". Window service hours match retail hours. The lobby and PO boxes are open 24 hours, but that is not retail.
- No duplicate or SDC record at 215 6th St.

## Holds

- **None.** No record printed Windsor geocodes outside Windsor town. No record printed with another city falls inside Windsor town on either the address geocode or the locator map point. Only the two Windsor-printed records return Windsor town.

## Left out (not holds)

- **WIN Carrier Annex (1560051)**, 1070 Diamond Valley Dr Ste 500, Windsor 80550, 970-833-3010 (the same phone as the Windsor Post Office). It is a carrier/delivery unit: its services are CALLREFERRAL, CARRIER, and DELIVERYUNIT. It has no retail (BUSINESS) hours and no money orders. The current and 2020 files both match 1070 DIAMOND VALLEY DR, WINDSOR, in Windsor town (Weld County), and so does the locator point. It is left out because it is an annex with no retail and no services. Page HTTP 200.
- Nearby offices printed with other cities, where the geocoder agrees they are outside Windsor. All of these list money orders unless noted:
  - Severance 1381248, 320 1st St, Severance 80546: Mon-Fri 08:00-12:00, Sat 08:00-11:00. The current address match returns **Eaton town**, but the locator point returns Severance town. Neither is Windsor.
  - Timnath 1384692 (Timnath town), Eaton 1361975 (Eaton town), Johnstown 1368496 (Johnstown town), Milliken 1373182 (Milliken town)
  - Greeley 1365514, 930 39th Ave, and Downtown Greeley 1365513 (Greeley city)
  - Lucerne 1371125: no address match; the locator point is unincorporated Weld County
  - Evans, Ault, La Salle, Pierce, Kersey, Gilcrest, Platteville, Berthoud, Wellington, Nunn, Mead, Frederick, Firestone, and Dacono (each in its own town or city). Gill and Galeton are in unincorporated Weld County.
  - Fort Collins 1363754 and Fort Collins CO SDC 1601572: same building at 301 Boardwalk Dr, Fort Collins city. Unlike the Aurora SDC, this SDC record does list money orders. Old Town 1376040 is also in Fort Collins city.
  - Loveland 1371037 and Valentine 1371038 (Loveland city)
  - Laporte (Laporte CDP), plus Bellvue, Masonville, and Drake (unincorporated Larimer County)
  - The far edge of the 80516 15-mile sweep:
    - Erie 1362695 and Erie Carrier Annex 1546616 (Erie town)
    - Lafayette and Lafayette Carrier Annex (Lafayette city)
    - Louisville 1371024, printed Superior (Louisville city)
    - Longmont (Longmont city)
    - Niwot (Niwot CDP)
    - Boulder, Valmont, and High Mar (Boulder city). Valmont 1385692 and Boulder CO SDC 1612987 share a building, and the SDC record has no money orders.
    - Hygiene and Eldorado Springs (no address match; the locator points are unincorporated Boulder County and Eldorado Springs CDP)
    - Broomfield and Broomfield Eagle View (Broomfield city)
    - Northglenn and Northview (Northglenn city)
    - Eastlake (locator point in Thornton city)
    - Westminster and Harris Park (Westminster city)
    - Brighton and Brighton Carrier Annex (Brighton city)
    - Henderson (unincorporated Adams County)
    - Fort Lupton (Fort Lupton city)
    - Indian Tree (Arvada city)
    - North Pecos (Sherrelwood CDP)
    - Dupont (Derby CDP)
- USPS contract postal units and Approved Postal Providers were not collected, the same as earlier cities.

## Fetch failures

- None. All 28 locator API queries returned JSON, and all 4 detail pages returned HTTP 200 on the first try.
