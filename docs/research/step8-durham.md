# Durham, North Carolina USPS research (2026-11-17, America/Denver)

Fourth North Carolina state city in the Census ranking (Vintage 2025, SUMLEV 162, POPESTIMATE2025). Census place is Durham city, GEOID 3719000, population 305,561, mostly in Durham County (GEOID 37063) with small Wake County and Orange County parts. The listed offices are in Durham County. Official listed pages print Durham, NC. This is not Chapel Hill, not Carrboro, not Hillsborough, not Cary, not Raleigh, and not unincorporated Research Triangle Park. Hours are Eastern Time (49 CFR 71.4; the Eastern–Central boundary in 49 CFR 71.5 does not enter North Carolina). OpenStreetMap was not used. Raw data: `/workspace/step8nc/`. Classification: `/workspace/checkdesk/research/north-carolina-geocode-classify-2026-11-17.md`.

Official Durham self ZIPs are the 16 ZIPs listed as Durham, NC on the official city page. Classification still uses printed city and Census geocode, not the ZIP list. Locator passes and official pages are the shared North Carolina sweep (452 offices, all geocoded on the current and 2020 Census files, 0 errors).

## Listed (5)

- Durham (1438143, 323 E CHAPEL HILL ST, DURHAM 27701). Lists money orders. All four Census legs are in Durham city. BUSINESS hours: weekdays 9:00 a.m. to 5:00 p.m., Saturday closed, Sunday closed. Not labeled Open evenings or Open weekends.
- East Durham (1438145, 1100 N MIAMI BLVD, DURHAM 27703). Lists money orders. All four Census legs are in Durham city. BUSINESS hours: weekdays 9:30 a.m. to 4:00 p.m., Saturday 9:30 a.m. to 12:00 p.m., Sunday closed. Labeled Open weekends.
- Eno Valley (1438152, 311 MILTON RD, DURHAM 27712). Lists money orders. All four Census legs are in Durham city. BUSINESS hours: weekdays 9:00 a.m. to 4:00 p.m., Saturday closed, Sunday closed. Not labeled Open evenings or Open weekends.
- Shannon Plaza (1381328, 3710 SHANNON RD, DURHAM 27707). Lists money orders. All four Census legs are in Durham city. BUSINESS hours: weekdays 9:00 a.m. to 5:00 p.m., Saturday 9:00 a.m. to 1:30 p.m., Sunday closed. Labeled Open weekends.
- West Durham (1438285, 3520 KANGAROO DR, DURHAM 27705). Lists money orders. All four Census legs are in Durham city. BUSINESS hours: weekdays 9:00 a.m. to 4:00 p.m., Saturday 9:00 a.m. to 12:00 p.m., Sunday closed. Labeled Open weekends.

## Held

### Geocode mismatch (1)

- Research Triangle Park (1438239, 65 TW ALEXANDER DR, DURHAM 27709). Prints Durham, NC, and lists money orders, but all four Census legs are in unincorporated Durham County, with no incorporated place or CDP on either file. The official map point is not inside Durham city, so it is not listed under a map-point fallback. Held as a geocode mismatch.

### No money-order tags (1)

- North Durham (1438214, 3500 N ROXBORO ST STE 30, DURHAM 27704). Prints Durham, NC, and all four Census legs are in Durham city, but the official page does not list money orders. Held for no money-order tags.

Charlotte, Raleigh, Greensboro, and Winston-Salem stay on separate lists. Offices in South Carolina, Virginia, Tennessee, and Georgia stay off this list.

## Result

5 listed Post Offices, all with money orders. None is labeled Open evenings (a 5:00 p.m. close does not count). 3 are labeled Open weekends, Saturday only (Durham and Eno Valley have no Saturday or Sunday hours). Hours labeled Eastern Time. 2 holds: 1 geocode mismatch in unincorporated Durham County (Research Triangle Park) and 1 with no money-order tags (North Durham).

## Site changes in this PR

- New `data/locations/durham.csv` and `/durham/`, `/durham/money-orders/`, and `/durham/after-hours/` pages.
- Durham is inserted under the existing North Carolina section after Greensboro on the home page and `/cities/`. No other existing city CSV or page changed except the home and `/cities/` meta and list lines. The unsuffixed `/durham/` slug is new and does not collide with an existing page.
