# Richmond, Virginia USPS research (2026-11-18, America/Denver)

Third Virginia state city in the Census ranking (Vintage 2025, SUMLEV 162, POPESTIMATE2025). Census place is Richmond city, GEOID 5167000, population 237,257. Official listed pages print Richmond, VA. This is Richmond, Virginia, an independent city, at /richmond/. This is not Richmond County, Virginia, and not a Richmond in another state. Offices that geocode entirely in Henrico County stay off this list. Hours are Eastern Time (The eastern zone under 49 CFR 71.4 is west of 67°30′ W. longitude and east of the boundary line described in 49 CFR 71.5, and includes all of the State of Maine, but does not include any part of the Commonwealth of Puerto Rico. Section 71.5 describes the Eastern-Central boundary through Michigan, Indiana, Kentucky, and Tennessee, and then along the Tennessee-Georgia, Alabama-Georgia, and Florida-Georgia lines; it does not mention Virginia and does not enter the state. None of the five cities sits on a zone boundary.). OpenStreetMap was not used. Raw data: `/workspace/step8va/`. Classification: `/workspace/checkdesk/research/virginia-geocode-classify-2026-11-18.md`.

Locator passes and official pages are the shared Virginia sweep (292 offices, all geocoded on the current and 2020 Census files, 0 errors). Classification still uses printed city and Census geocode, not the ZIP list. The five cities are independent cities (county equivalents). OpenStreetMap was not used.

## Listed (7)

- Capitol (1356960, 700 E MAIN ST, RICHMOND 23219). Lists money orders. Official page prints Richmond, VA. All four Census legs are in Richmond city. BUSINESS hours: weekdays 7:30 a.m. to 5:00 p.m., Saturday closed, Sunday closed. Not labeled Open evenings or Open weekends.
- Central Richmond (1357500, 205 N 2ND ST, RICHMOND 23241). Lists money orders. Official page prints Richmond, VA. All four Census legs are in Richmond city. BUSINESS hours: weekdays 9:30 a.m. to 11:00 a.m. and 12:00 p.m. to 4:00 p.m., Saturday closed, Sunday closed. Not labeled Open evenings or Open weekends.
- Forest Hill (1363674, 1021 HIOAKS RD, RICHMOND 23225). Lists money orders. Official page prints Richmond, VA. All four Census legs are in Richmond city. BUSINESS hours: weekdays 10:00 a.m. to 5:00 p.m., Saturday 9:00 a.m. to 1:00 p.m., Sunday closed. Labeled Open weekends.
- Northside (1375554, 3004 NORTH AVE, RICHMOND 23222). Lists money orders. Official page prints Richmond, VA. All four Census legs are in Richmond city. BUSINESS hours: weekdays 10:00 a.m. to 1:00 p.m. and 2:00 p.m. to 4:00 p.m., Saturday closed, Sunday closed. Not labeled Open evenings or Open weekends.
- Southside (1382390, 2101 HOPKINS RD, RICHMOND 23224). Lists money orders. Official page prints Richmond, VA. All four Census legs are in Richmond city. BUSINESS hours: weekdays 9:00 a.m. to 5:00 p.m., Saturday 9:00 a.m. to 1:00 p.m., Sunday closed. Labeled Open weekends.
- Stewart (1383568, 3517 FLOYD AVE, RICHMOND 23221). Lists money orders. Official page prints Richmond, VA. All four Census legs are in Richmond city. BUSINESS hours: weekdays 9:00 a.m. to 5:00 p.m., Saturday 9:00 a.m. to 12:00 p.m., Sunday closed. Labeled Open weekends.
- Westhampton (1387300, 805 GLENBURNIE RD, RICHMOND 23226). Lists money orders. Official page prints Richmond, VA. Map-point fallback (medium confidence). BUSINESS hours: weekdays 8:00 a.m. to 5:00 p.m., Saturday 10:00 a.m. to 2:00 p.m., Sunday closed. Labeled Open weekends.

## Held (6)

- Bellevue (1437262, 5327 CHAMBERLAYNE RD, RICHMOND 23227). Official page prints Richmond, VA, and lists money orders. All four Census legs are in Henrico County with no incorporated place or CDP. Held because the office is outside Richmond city. The official map point is not inside the city, so map-point fallback is not used.
- West End (1437409, 2220 DABNEY RD, RICHMOND 23230). Official page prints Richmond, VA, and lists money orders. All four Census legs are in Henrico County with no incorporated place or CDP. Held because the office is outside Richmond city. The official map point is not inside the city, so map-point fallback is not used.
- Richmond (1437368, 1801 BROOK RD, RICHMOND 23232). Official page prints Richmond, VA. The current address file and both official map-point legs are in Richmond city; the 2020 address file did not match. Held because the Census geocoder does not place both the address and the official map point fully inside the city, and because the official page does not list money orders. Map-point fallback is not used, because the office has no money-order tags. This is the same address as Richmond VA S&DC.
- Richmond VA S&DC (1582129, 1801 BROOK RD, RICHMOND 23232). Official page prints Richmond, VA. The current address file and both official map-point legs are in Richmond city; the 2020 address file did not match. Held because the Census geocoder does not place both the address and the official map point fully inside the city, and because the official page does not list money orders. Map-point fallback is not used, because the office has no money-order tags. This is the same address as the held Richmond office.
- East End (1361712, 414 N 25TH ST, RICHMOND 23223). Official page prints Richmond, VA. All four Census legs are in Richmond city. Held because the official page does not list money orders.
- Saunders (1476296, 1645 W BROAD ST, RICHMOND 23220). Official page prints Richmond, VA. All four Census legs are in Richmond city. Held because the official page does not list money orders.

This is not Richmond County. Offices that geocode entirely in Henrico County stay off this list.

## Result

7 listed Post Offices, all with money orders, all in the independent city of Richmond, including one documented map-point fallback (Westhampton). None is labeled Open evenings. Four publish Saturday hours and are labeled Open weekends: Forest Hill and Southside, 9:00 a.m. to 1:00 p.m.; Stewart, 9:00 a.m. to 12:00 p.m.; Westhampton, 10:00 a.m. to 2:00 p.m. None publishes Sunday hours. Hours labeled Eastern Time. 6 holds.

## Site changes in this PR

- New `data/locations/richmond.csv` and `/richmond/`, `/richmond/money-orders/`, and `/richmond/after-hours/` pages.
- Richmond is inserted under the existing Virginia section after Chesapeake on the home page and `/cities/`. No other existing city CSV or page changed except the home and `/cities/` meta and list lines. The unsuffixed `/richmond/` slug is new and does not collide with an existing page.
