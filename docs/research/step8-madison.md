# Madison, Wisconsin USPS research (2026-11-18, America/Denver)

Second Wisconsin state city in the Census ranking (Vintage 2025, SUMLEV 162, POPESTIMATE2025). Census place is Madison city, GEOID 5548000, population 286,233. Official listed pages print Madison, WI. This is Madison, Wisconsin, at /madison/. This is not Madison, Illinois, and not a Madison in another state. A Dane County geocode is not enough to list an office here. Hours are Central Time (The central zone under 49 CFR 71.6(a) is west of the boundary line described in 49 CFR 71.5 and east of the boundary line described in 49 CFR 71.7. Section 71.5 describes the Eastern-Central boundary under the heading Minnesota-Michigan-Wisconsin only along Michigan county lines in the Upper Peninsula (Gogebic, Ontonagon, Iron, Dickinson, and Menominee Counties) and then the western boundary of the State of Michigan; it does not enter Wisconsin. Section 71.7 describes the Central-Mountain boundary through Montana, North Dakota, South Dakota, Nebraska, Kansas, Oklahoma, and Texas, and does not mention Wisconsin. None of the five cities sits on a zone boundary.). OpenStreetMap was not used. Raw data: `/workspace/step8wi/`. Classification: `/workspace/checkdesk/research/wisconsin-geocode-classify-2026-11-18.md`.

Locator passes and official pages are the shared Wisconsin sweep (737 offices, all geocoded on the current and 2020 Census files, 0 errors). Classification still uses printed city and Census geocode, not the ZIP list. The five cities are ordinary incorporated places in their home counties, not independent cities. Milwaukee city has legal zero-population parts in Washington and Waukesha Counties; Madison, Green Bay, Kenosha, and Racine each sit in one home county. Classification uses place GEOIDs only, because a Milwaukee, Washington, or Waukesha County match would mix Milwaukee with other places in those counties. Out-of-state offices, including Madison, IL, stay off these lists. OpenStreetMap was not used.

## Listed (4)

- Hilldale (1366990, 601 SAWYER TER, MADISON 53705). Lists money orders. Official page prints Madison, WI. All four Census legs are in Madison city. BUSINESS hours: weekdays 9:00 a.m. to 6:00 p.m., Saturday 9:30 a.m. to 2:00 p.m., Sunday closed. Labeled Open evenings and Open weekends.
- Madison (1438330, 3902 MILWAUKEE ST, MADISON 53714). Lists money orders. Official page prints Madison, WI. All four Census legs are in Madison city. BUSINESS hours: weekdays 8:00 a.m. to 7:00 p.m., Saturday 8:00 a.m. to 4:00 p.m., Sunday closed. Labeled Open evenings and Open weekends.
- South Side (1382279, 820 W WINGRA DR, MADISON 53715). Lists money orders. Official page prints Madison, WI. All four Census legs are in Madison city. BUSINESS hours: weekdays 8:30 a.m. to 5:30 p.m., Saturday 10:00 a.m. to 2:00 p.m., Sunday closed. Labeled Open evenings and Open weekends.
- Westside (1387379, 733 STRUCK ST, MADISON 53711). Lists money orders. Official page prints Madison, WI. All four Census legs are in Madison city. BUSINESS hours: weekdays 9:30 a.m. to 7:00 p.m., Saturday 9:30 a.m. to 3:30 p.m., Sunday closed. Labeled Open evenings and Open weekends.

## Held (4)

- Cap Annex (1609176, 3902 MILWAUKEE ST, MADISON 53714). Official page prints Madison, WI. All four Census legs are in Madison city. Held because the official page does not list money orders. This is the same address as the listed Madison office.
- Capitol Station Retail (1492395, 2 E MIFFLIN ST STE 103, MADISON 53703). Official page prints Madison, WI. All four Census legs are in Madison city. Held because the official page does not list money orders.
- Madison Carrier Annex (1438523, 205 CORPORATE DR, MADISON 53714). Official page prints Madison, WI. All four Census legs are in Madison city. Held because the official page does not list money orders.
- University (1448458, 441 N LAKE ST, MADISON 53715). Official page prints Madison, WI. All four Census legs are in Madison city. Held because the official page does not list money orders.

Madison, Illinois, including the Madison, IL, office found in this sweep, stays off this list. Other Dane County places stay off this list.

## Result

4 listed Post Offices, with money orders, in Madison city, with no map-point fallbacks. Four are labeled Open evenings: Hilldale, until 6:00 p.m., Madison, until 7:00 p.m., South Side, until 5:30 p.m., and Westside, until 7:00 p.m. All four publish Saturday hours and are labeled Open weekends. None publishes Sunday hours. Hours labeled Central Time. 4 holds.

## Site changes in this PR

- New `data/locations/madison.csv` and `/madison/`, `/madison/money-orders/`, and `/madison/after-hours/` pages.
- Madison is inserted under the existing Wisconsin section after Milwaukee on the home page and `/cities/`. No other existing city CSV or page changed except the home and `/cities/` meta and list lines. The unsuffixed `/madison/` slug is new and does not collide with an existing page.
