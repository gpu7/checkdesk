# Winston-Salem, NC — community-named office added 2026-11-19

The Pfafftown Post Office is now listed on the Winston-Salem pages, under the rule approved 2026-11-19: the official page prints a community name, both the current and 2020 Census address files place the address inside Winston-Salem city (GEOID 3775000), money-order tags are present, and the displayed city stays the official printed USPS city. Official map points also fall in Winston-Salem city on both files. The original Winston Salem-printed rows are unchanged.

Added office (printed city in parentheses): Pfafftown (Pfafftown). Pfafftown is a community inside Winston-Salem city, not a separately incorporated place.

The Winston-Salem list is now 5 Post Offices, all with money orders (none Open evenings; one Open weekends: Pfafftown Saturday 9:00 a.m. to 11:00 a.m.). Pfafftown weekday retail closes at 4:00 p.m., so it is not labeled Open evenings. Hours stay Eastern Time. Because this is the first listed office with Saturday hours, a new after-hours page was created at /winston-salem/after-hours/, which adds one sitemap URL. Three Winston Salem-printed offices remain held for no money-order tags.

The body below is the original 2026-11-17 memo and is superseded for listed and hold counts.

# Winston-Salem, North Carolina USPS research (2026-11-17, America/Denver)

Fifth North Carolina state city in the Census ranking (Vintage 2025, SUMLEV 162, POPESTIMATE2025). Census place is Winston-Salem city, GEOID 3775000, population 257,271, in Forsyth County (GEOID 37067). Official listed pages print Winston Salem, NC, without the hyphen; Check Desk uses the Census place name Winston-Salem for the city field. This is not Kernersville, not Clemmons, not Lewisville, not Walkertown, and not Pfafftown. Hours are Eastern Time (49 CFR 71.4; the Eastern–Central boundary in 49 CFR 71.5 does not enter North Carolina). OpenStreetMap was not used. Raw data: `/workspace/step8nc/`. Classification: `/workspace/checkdesk/research/north-carolina-geocode-classify-2026-11-17.md`.

Official Winston-Salem self ZIPs are the 25 ZIPs listed as Winston-Salem, NC on the official city page (the city page title is Winston Salem, NC, without the hyphen). Classification still uses printed city and Census geocode, not the ZIP list. Locator passes and official pages are the shared North Carolina sweep (452 offices, all geocoded on the current and 2020 Census files, 0 errors). USPS locator and official pages print Winston Salem without a hyphen; 0 records print WINSTON-SALEM.

## Listed (4)

- Manor (1371687, 3331 HEALY DR, WINSTON SALEM 27103). Lists money orders. Official page prints Winston Salem, NC. All four Census legs are in Winston-Salem city. BUSINESS hours: weekdays 9:00 a.m. to 5:00 p.m., Saturday closed, Sunday closed. Not labeled Open evenings or Open weekends.
- North Point (1375405, 7840 N POINT BLVD STE 110, WINSTON SALEM 27106). Lists money orders. Official page prints Winston Salem, NC. All four Census legs are in Winston-Salem city. BUSINESS hours: weekdays 9:00 a.m. to 5:00 p.m., Saturday closed, Sunday closed. Not labeled Open evenings or Open weekends.
- Waughtown (1386666, 1995 PLEASANT ST, WINSTON SALEM 27107). Lists money orders. Official page prints Winston Salem, NC. All four Census legs are in Winston-Salem city. BUSINESS hours: weekdays 9:00 a.m. to 3:00 p.m., Saturday closed, Sunday closed. Not labeled Open evenings or Open weekends.
- Winston Salem (1388037, 1500 N PATTERSON AVE, WINSTON SALEM 27105). Lists money orders. Official page prints Winston Salem, NC. All four Census legs are in Winston-Salem city. BUSINESS hours: weekdays 9:00 a.m. to 3:00 p.m., Saturday closed, Sunday closed. Not labeled Open evenings or Open weekends.

## Held

### Other printed city (1)

- Pfafftown (1377346, 4715 YADKINVILLE RD, PFAFFTOWN 27040). Prints Pfafftown, NC, and lists money orders. All four Census legs are in Winston-Salem city, Forsyth County. Held because the printed city does not already match.

### No money-order tags (3)

- Center City (1357436, 200 TOWN RUN LN, WINSTON SALEM 27101). Prints Winston Salem, NC, and all four Census legs are in Winston-Salem city, but the official page does not list money orders. Held for no money-order tags.
- Hanes Mall (1366136, 3320 SILAS CREEK PKWY STE AU-502, WINSTON SALEM 27103). Prints Winston Salem, NC, and all four Census legs are in Winston-Salem city, but the official page does not list money orders. Held for no money-order tags.
- Winston Salem NC SDC (1594601, 1500 N PATTERSON AVE, WINSTON SALEM 27105). Prints Winston Salem, NC, and all four Census legs are in Winston-Salem city, but the official page does not list money orders. This is a different office from the listed Winston Salem office at the same street address. Held for no money-order tags.

Charlotte, Raleigh, Greensboro, and Durham stay on separate lists. Offices in South Carolina, Virginia, Tennessee, and Georgia stay off this list.

## Result

4 listed Post Offices, all with money orders. None is labeled Open evenings (a 5:00 p.m. close does not count). None publishes Saturday or Sunday hours, so there is no evenings-and-weekends page. Hours labeled Eastern Time. 4 holds: 1 other printed city (Pfafftown) and 3 with no money-order tags.

## Site changes in this PR

- New `data/locations/winston-salem.csv` and `/winston-salem/` and `/winston-salem/money-orders/` pages. No after-hours page, because no listed office is open evenings or weekends.
- Winston-Salem is inserted under the existing North Carolina section after Durham on the home page and `/cities/`. No other existing city CSV or page changed except the home and `/cities/` meta and list lines. The unsuffixed `/winston-salem/` slug is new and does not collide with an existing page.
