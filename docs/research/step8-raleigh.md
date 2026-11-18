# Raleigh, North Carolina USPS research (2026-11-17, America/Denver)

Second North Carolina state city in the Census ranking (Vintage 2025, SUMLEV 162, POPESTIMATE2025). Census place is Raleigh city, GEOID 3755000, population 506,306, mostly in Wake County (GEOID 37183) with a small Durham County part. The listed offices are in Wake County. Official listed pages print Raleigh, NC. This is not Cary, not Apex, not Wake Forest, not Holly Springs, not Fuquay-Varina, not Garner, not Morrisville, and not Durham. Hours are Eastern Time (49 CFR 71.4; the Eastern–Central boundary in 49 CFR 71.5 does not enter North Carolina). OpenStreetMap was not used. Raw data: `/workspace/step8nc/`. Classification: `/workspace/checkdesk/research/north-carolina-geocode-classify-2026-11-17.md`.

Official Raleigh self ZIPs are the 43 ZIPs listed as Raleigh, NC on the official city page. Classification still uses printed city and Census geocode, not the ZIP list. Locator passes and official pages are the shared North Carolina sweep (452 offices, all geocoded on the current and 2020 Census files, 0 errors).

## Listed (7)

- Avent Ferry Raleigh (1456392, 2100 LAKE DAM RD, RALEIGH 27606). Lists money orders. Documented map-point fallback after 2020 address retries. BUSINESS hours: weekdays 9:00 a.m. to 5:00 p.m., Saturday 9:00 a.m. to 12:00 p.m., Sunday closed. Labeled Open weekends.
- Brentwood (1355768, 2777 BRENTWOOD RD, RALEIGH 27604). Lists money orders. All four Census legs are in Raleigh city. BUSINESS hours: weekdays 9:00 a.m. to 4:30 p.m., Saturday 10:00 a.m. to 12:00 p.m., Sunday closed. Labeled Open weekends.
- Capitol (1438418, 311 NEW BERN AVE, RALEIGH 27601). Lists money orders. All four Census legs are in Raleigh city. BUSINESS hours: weekdays 9:00 a.m. to 5:00 p.m., Saturday closed, Sunday closed. Not labeled Open evenings or Open weekends.
- Century (1357559, 300 FAYETTEVILLE ST, RALEIGH 27601). Lists money orders. All four Census legs are in Raleigh city. BUSINESS hours: weekdays 9:00 a.m. to 4:00 p.m., Saturday closed, Sunday closed. Not labeled Open evenings or Open weekends.
- North Ridge (1438217, 7800 FALLS OF NEUSE RD, RALEIGH 27615). Lists money orders. All four Census legs are in Raleigh city. BUSINESS hours: weekdays 9:00 a.m. to 4:30 p.m., Saturday 9:00 a.m. to 1:00 p.m., Sunday closed. Labeled Open weekends.
- Sunnybrook (1438267, 236 SUNNYBROOK RD, RALEIGH 27610). Lists money orders. All four Census legs are in Raleigh city. BUSINESS hours: weekdays 9:00 a.m. to 4:30 p.m., Saturday 10:00 a.m. to 12:00 p.m., Sunday closed. Labeled Open weekends.
- Westgate (1438410, 1 FLORETTA PL RM 208, RALEIGH 27676). Lists money orders. All four Census legs are in Raleigh city. BUSINESS hours: weekdays 9:00 a.m. to 5:00 p.m., Saturday 9:00 a.m. to 2:00 p.m., Sunday closed. Labeled Open weekends.

## Held

### No money-order tags (8)

- Five Points (1438161, 2009 FAIRVIEW RD, RALEIGH 27628). Prints Raleigh, NC, and all four Census legs are in Raleigh city, but the official page does not list money orders. Held for no money-order tags.
- Hilburn Annex (1438420, 6508 HILBURN DR, RALEIGH 27613). Prints Raleigh, NC, and all four Census legs are in Raleigh city, but the official page does not list money orders. Held for no money-order tags.
- Method (1438194, 3919 BERYL RD, RALEIGH 27607). Prints Raleigh, NC, and all four Census legs are in Raleigh city, but the official page does not list money orders. Held for no money-order tags.
- Millbrook (1438197, 4901 DEPARTURE DR, RALEIGH 27616). Prints Raleigh, NC, and all four Census legs are in Raleigh city, but the official page does not list money orders. Held for no money-order tags.
- Neuse (1438210, 6320 CAPITAL BLVD STE 120, RALEIGH 27616). Prints Raleigh, NC, and all four Census legs are in Raleigh city, but the official page does not list money orders. Held for no money-order tags.
- North Hills (1579852, 3016 WAKE FOREST RD, RALEIGH 27609). Prints Raleigh, NC, and all four Census legs are in Raleigh city, but the official page does not list money orders. Held for no money-order tags.
- Oberlin Village (1544435, 806 OBERLIN RD, RALEIGH 27605). Prints Raleigh, NC, and all four Census legs are in Raleigh city, but the official page does not list money orders. Held for no money-order tags.
- Raleigh (1438236, 1 FLORETTA PL RM 88, RALEIGH 27676). Prints Raleigh, NC, and all four Census legs are in Raleigh city, but the official page does not list money orders. This is a different office from the listed Westgate office at 1 Floretta Pl Rm 208. Held for no money-order tags.

Charlotte, Greensboro, Durham, and Winston-Salem stay on separate lists. Offices in South Carolina, Virginia, Tennessee, and Georgia stay off this list.

## Result

7 listed Post Offices, all with money orders. None is labeled Open evenings (a 5:00 p.m. close does not count). 5 are labeled Open weekends, Saturday only (Capitol and Century have no Saturday or Sunday hours). Hours labeled Eastern Time. 8 holds, all with no money-order tags. Avent Ferry Raleigh is listed under a documented map-point fallback.

## Site changes in this PR

- New `data/locations/raleigh.csv` and `/raleigh/`, `/raleigh/money-orders/`, and `/raleigh/after-hours/` pages.
- Raleigh is inserted under the existing North Carolina section after Charlotte on the home page and `/cities/`. No other existing city CSV or page changed except the home and `/cities/` meta and list lines. The unsuffixed `/raleigh/` slug is new and does not collide with an existing page.
