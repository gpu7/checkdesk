# Greensboro, NC — community-named office added 2026-11-19

The Colfax Post Office is now listed on the Greensboro pages, under the rule approved 2026-11-19: the official page prints a community name, both the current and 2020 Census address files place the address inside Greensboro city (GEOID 3728000), money-order tags are present, and the displayed city stays the official printed USPS city. Official map points also fall in Greensboro city on both files, in Guilford County. The original Greensboro-printed rows are unchanged. No after-hours page was added, because none of the listed offices has evening or weekend hours.

Added office (printed city in parentheses): Colfax (Colfax). Colfax is a community inside Greensboro city, not a separately incorporated place.

The Greensboro list is now 4 Post Offices, all with money orders (none Open evenings; none Open weekends). Hours stay Eastern Time. Four Seasons remains held on geocode and money-order grounds. Seven Greensboro-printed no-money-order offices also remain held. No neighborhood or community-named holds remain for this city.

The body below is the original 2026-11-17 memo and is superseded for listed and hold counts.

# Greensboro, North Carolina USPS research (2026-11-17, America/Denver)

Third North Carolina state city in the Census ranking (Vintage 2025, SUMLEV 162, POPESTIMATE2025). Census place is Greensboro city, GEOID 3728000, population 308,667, in Guilford County (GEOID 37081). Official listed pages print Greensboro, NC. This is not High Point, not Summerfield, not Oak Ridge, and not Colfax. Hours are Eastern Time (49 CFR 71.4; the Eastern–Central boundary in 49 CFR 71.5 does not enter North Carolina). OpenStreetMap was not used. Raw data: `/workspace/step8nc/`. Classification: `/workspace/checkdesk/research/north-carolina-geocode-classify-2026-11-17.md`.

Official Greensboro self ZIPs are the 28 ZIPs listed as Greensboro, NC on the official city page. Classification still uses printed city and Census geocode, not the ZIP list. Locator passes and official pages are the shared North Carolina sweep (452 offices, all geocoded on the current and 2020 Census files, 0 errors).

## Listed (3)

- Greensboro (1365616, 201 N MURROW BLVD, GREENSBORO 27401). Lists money orders. All four Census legs are in Greensboro city. BUSINESS hours: weekdays 9:00 a.m. to 5:00 p.m., Saturday closed, Sunday closed. Not labeled Open evenings or Open weekends.
- Spring Valley (1382559, 2300 SOABAR ST, GREENSBORO 27406). Lists money orders. All four Census legs are in Greensboro city. BUSINESS hours: weekdays 9:00 a.m. to 4:00 p.m., Saturday closed, Sunday closed. Not labeled Open evenings or Open weekends.
- Summit (1383932, 1585 YANCEYVILLE ST, GREENSBORO 27405). Lists money orders. All four Census legs are in Greensboro city. BUSINESS hours: weekdays 9:00 a.m. to 4:00 p.m., Saturday closed, Sunday closed. Not labeled Open evenings or Open weekends.

## Held

### Geocode mismatch (1)

- Four Seasons (1363917, 301 FOUR SEASONS TOWN CTR, GREENSBORO 27407). Prints Greensboro, NC. The current Census address file did not match. The 2020 address file and both official map points are in Greensboro city, Guilford County. The official page does not list money orders. Held as a geocode mismatch (and it would stay held for no money-order tags even after an address match).

### Other printed city (1)

- Colfax (1358640, 9052 W MARKET ST, COLFAX 27235). Prints Colfax, NC, and lists money orders. All four Census legs are in Greensboro city, Guilford County. Held because the printed city does not already match.

### No money-order tags (7)

- Battleground (1354214, 2941 BATTLEGROUND AVE, GREENSBORO 27408). Prints Greensboro, NC, and all four Census legs are in Greensboro city, but the official page does not list money orders. Held for no money-order tags.
- Friendly (1579853, 3116 NORTHLINE AVE, GREENSBORO 27408). Prints Greensboro, NC, and all four Census legs are in Greensboro city, but the official page does not list money orders. Held for no money-order tags.
- Greensboro NC Downtown SDC (1613005, 201 N MURROW BLVD, GREENSBORO 27401). Prints Greensboro, NC, and all four Census legs are in Greensboro city, but the official page does not list money orders. This is a different office from the listed Greensboro office at the same street address. Held for no money-order tags.
- Guilford (1365840, 5704 W MARKET ST, GREENSBORO 27409). Prints Greensboro, NC, and all four Census legs are in Greensboro city, but the official page does not list money orders. Held for no money-order tags.
- Hilltop Finance (1367046, 4615 W GATE CITY BLVD, GREENSBORO 27407). Prints Greensboro, NC, and all four Census legs are in Greensboro city, but the official page does not list money orders. Held for no money-order tags.
- Pleasant Ridge Annex (1574354, 1120 PLEASANT RIDGE RD, GREENSBORO 27498). Prints Greensboro, NC, and all four Census legs are in Greensboro city, but the official page does not list money orders. Held for no money-order tags.
- Westside Annex (1387370, 4528 W MARKET ST, GREENSBORO 27407). Prints Greensboro, NC, and all four Census legs are in Greensboro city, but the official page does not list money orders. Held for no money-order tags.

Charlotte, Raleigh, Durham, and Winston-Salem stay on separate lists. Offices in South Carolina, Virginia, Tennessee, and Georgia stay off this list.

## Result

3 listed Post Offices, all with money orders. None is labeled Open evenings (a 5:00 p.m. close does not count). None publishes Saturday or Sunday hours, so there is no evenings-and-weekends page. Hours labeled Eastern Time. 9 holds: 1 geocode mismatch (Four Seasons, also no money-order tags), 1 other printed city (Colfax), and 7 with no money-order tags.

## Site changes in this PR

- New `data/locations/greensboro.csv` and `/greensboro/` and `/greensboro/money-orders/` pages. No after-hours page, because no listed office is open evenings or weekends.
- Greensboro is inserted under the existing North Carolina section after Raleigh on the home page and `/cities/`. No other existing city CSV or page changed except the home and `/cities/` meta and list lines. The unsuffixed `/greensboro/` slug is new and does not collide with an existing page.
