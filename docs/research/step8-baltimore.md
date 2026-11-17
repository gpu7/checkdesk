# Baltimore, Maryland USPS research (2026-11-16, America/Denver)

First Maryland city (ship order: Baltimore, Frederick, Gaithersburg, Rockville, Bowie). Post Offices only. Hours labeled Eastern Time (49 CFR 71.4). Census place is Baltimore city, GEOID 2404000, Vintage 2025 population 569,997, an independent city, not Baltimore County. This is Baltimore, Maryland, not a Baltimore in another state, and not Towson, Catonsville, Dundalk, Essex, or Brooklyn. OpenStreetMap was not used.

ZIP inventory used zip-codes.com county pages for Baltimore City, Frederick, Montgomery, and Prince George's Counties plus Census-adjacent counties, including out-of-state counties that border a home county (899 in-scope ZIPs), and the official Baltimore, MD search.asp list. Official Baltimore self ZIPs are 21201, 21202, 21203, 21205, 21206, 21209, 21210, 21211, 21212, 21213, 21214, 21215, 21216, 21217, 21218, 21223, 21224, 21229, 21230, 21231, 21233, 21235, 21239, 21240, 21241, 21250, 21251, 21263, 21264, 21270, 21273, 21275, 21278, 21279, 21281, 21287, 21289, 21290, 21297, and 21298. The Baltimore search also lists Towson, Gwynn Oak, Pikesville, Sparrows Point, Middle River, Essex, Dundalk, Brooklyn, Curtis Bay, Halethorpe, Catonsville, Parkville, Nottingham, Rosedale, and Windsor Mill, which are not Baltimore self ZIPs. Locator pass 1 (5 and 15 miles) and pass 2 (1, 2, 3, 10, and 20 miles) found 661 unique offices. Official USPS location pages were fetched for all 661 (all HTTP 200). All 661 were geocoded on the Census current and 2020 address and coordinate files, 0 errors.

## Listed (21)

All twenty-one print Baltimore, MD, list money orders, and match Baltimore city on all four Census legs.

- Arlington (1353364, 3500 Dolfield Ave, 21215). Weekdays 10:00-16:30; Saturday 09:00-12:00.
- Baltimore (1434368, 900 E Fayette St Rm 118, 21233). Weekdays 08:30-19:00; Saturday 08:30-17:00.
- Calvert (1356676, 111 N Calvert St, 21202). Weekdays 09:00-14:00 and 15:00-17:00; Saturday closed.
- Carroll (1357114, 340 S Loudon Ave, 21229). Weekdays 10:00-14:00 and 15:00-16:00; Saturday 10:00-12:00.
- Clifton East End (1358363, 4200 Shannon Dr, 21213). Weekdays 10:00-16:00; Saturday 10:00-13:00.
- Druid (1361333, 1826 Pennsylvania Ave, 21217). Weekdays 10:00-16:00; Saturday 10:00-12:00.
- Fells Point (1376949, 714 S Wolfe St, 21231). Weekdays 10:00-14:00 and 15:00-17:00; Saturday 09:00-13:00.
- Franklin (1364031, 2401 Ashton St, 21223). Weekdays 10:00-13:30 and 14:30-17:00; Saturday 10:00-12:00.
- Govans (1365223, 4904 York Rd, 21212). Weekdays 10:00-17:00; Saturday 10:00-13:00.
- Hamilton (1366055, 4901 Harford Rd, 21214). Weekdays 10:00-12:30 and 13:30-16:00; Saturday 09:30-12:00.
- Hampden Roland Park (1366086, 919 W 34th St, 21211). Weekdays 09:00-13:00 and 14:15-17:00; Saturday 09:00-13:00.
- Highlandtown (1366953, 6221 Eastern Ave, 21224). Weekdays 09:00-16:30; Saturday 09:00-13:00.
- Market Center (1371905, 130 N Greene St, 21201). Weekdays 09:00-14:00 and 15:00-17:00; Saturday closed.
- Mondawmin Mall (1433118, 2401 Liberty Heights Ave, 21215). Weekdays 11:00-15:00; Saturday 11:00-13:30.
- Mount Washington (1374114, 5730 Cottonworth Ave, 21209). Weekdays 09:00-16:00; Saturday 09:00-14:00.
- Northwood (1375589, 1800 E Northern Pkwy, 21239). Weekdays 09:00-13:00 and 14:00-17:00; Saturday 09:00-13:00.
- Raspeburg (1378830, 6502 Belair Rd, 21206). Weekdays 10:00-16:00; Saturday 09:00-13:00.
- Roland Park (1379776, 732 Deepdene Rd, 21210). Weekdays 09:00-14:00 and 15:15-17:00; Saturday 09:00-13:00.
- Southeast (1434461, 340 S Highland Ave, 21281). Weekdays 09:00-13:00 and 14:30-17:00; Saturday 09:00-12:30.
- Walbrook (1386193, 1908 N Ellamont St, 21216). Weekdays 10:00-13:30 and 14:30-16:30; Saturday 10:00-12:00.
- Waverly (1386709, 3000 Homewood Ave, 21218). Weekdays 10:00-13:30 and 14:30-16:00; Saturday 10:00-12:00.

Evenings: 1 (the Baltimore Post Office at 900 E Fayette St Rm 118, until 19:00; a 17:00 close does not count). Weekends: 19 (Saturday only). Calvert and Market Center have no weekend retail hours. None publishes Sunday hours.

## Holds (3)

- Baltimore MD E Lexington SDC (1599148, 1000 E Lexington St, 21202). Prints Baltimore and geocodes in Baltimore city on all four legs, but the official page does not list money orders and has no published retail hours.
- South (1544054, 1200 S Hanover St Ste 100, 21230). Prints Baltimore and geocodes in Baltimore city on all four legs, and it has published retail hours, but the official page does not list money orders.
- Brooklyn South (1443187, 1500 Cherry Hill Rd, Brooklyn 21225). Prints Brooklyn, not Baltimore, so it is held even though all four Census legs fall in Baltimore city. The official page also does not list money orders.

## Result

21 listed Post Offices, all with money orders. 1 Open evenings. 19 Open weekends. Hours labeled Eastern Time. 3 holds. No map-point fallback.

## Site changes in this PR

- New `data/locations/baltimore.csv` and `/baltimore/`, `/baltimore/money-orders/`, and `/baltimore/after-hours/` pages.
- Baltimore is inserted as the first Maryland city after Maine on the home page and `/cities/`. `/westminster/` remains Westminster, Colorado. The Maryland census memo is added under `docs/research/`. No other city CSV or page changed except those meta and list lines.
