# Manchester, New Hampshire USPS research (2026-11-17, America/Denver)

First New Hampshire city in the Census ranking (Vintage 2025, SUMLEV 162, POPESTIMATE2025). Census place is Manchester city, GEOID 3345140, population 116,818, in Hillsborough County (GEOID 33011). Official listed pages print Manchester, NH. This is not Nashua, not a town in the Balance of Hillsborough County, and not Manchester, Massachusetts. Hours are Eastern Time (49 CFR 71.4; the Eastern–Central boundary in 49 CFR 71.5 does not enter New Hampshire). OpenStreetMap was not used. Raw data: `/workspace/step8nh/`. Classification: `/workspace/checkdesk/research/new-hampshire-geocode-classify-2026-11-17.md`.

Official Manchester self ZIPs are the 9 ZIPs listed as Manchester, NH on the official city page: 03101, 03102, 03103, 03104, 03105, 03106, 03108, 03109, and 03111. Locator passes and official pages are the shared New Hampshire sweep (780 offices, all geocoded on the current and 2020 Census files, 0 errors).

## Listed (2)

- Downtown (1371606, 1000 ELM ST STE 15104, MANCHESTER 03101). Lists money orders. All four Census legs are in Manchester city. BUSINESS hours: weekdays 8:30 a.m. to 5:00 p.m., Saturday 9:00 a.m. to 12:00 p.m., Sunday closed. A 5:00 p.m. close does not count as Open evenings. Labeled Open weekends.
- Manchester (1434550, 955 GOFFS FALLS RD STE 998, MANCHESTER 03103). Lists money orders. All four Census legs are in Manchester city. BUSINESS hours: weekdays 7:30 a.m. to 7:00 p.m., Saturday 7:30 a.m. to 2:00 p.m., Sunday closed. Labeled Open evenings and Open weekends.

No map-point fallback.

## Held

- Manchester South (1371624, 7 PERIMETER RD STE 2, MANCHESTER 03103). Prints Manchester, NH, and all four Census legs are in Manchester city, but the official page does not list money orders and has no BUSINESS hours block.

No other office in the New Hampshire locator sweep geocodes into Manchester city. Manchester, Massachusetts, appears in the sweep but prints Manchester, MA, and is outside this list.

## Result

2 listed Post Offices, both with money orders. 1 Open evenings. 2 Open weekends. Hours labeled Eastern Time. 1 hold (no money-order tags).

## Site changes in this PR

- New `data/locations/manchester.csv` and `/manchester/`, `/manchester/money-orders/`, and `/manchester/after-hours/` pages.
- Manchester is inserted under a new New Hampshire section after Nevada on the home page and `/cities/`. No existing city CSV or page changed except those meta and list lines. The unsuffixed `/manchester/` slug is new and does not collide with an existing page.
