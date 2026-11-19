# Racine, Wisconsin USPS research (2026-11-18, America/Denver)

Fifth Wisconsin state city in the Census ranking (Vintage 2025, SUMLEV 162, POPESTIMATE2025). Census place is Racine city, GEOID 5566000, population 77,908. Official listed pages print Racine, WI. This is Racine, Wisconsin, at /racine/. This is not Caledonia, and not a Racine in another state. A Racine County geocode is not enough to list an office here. Hours are Central Time (The central zone under 49 CFR 71.6(a) is west of the boundary line described in 49 CFR 71.5 and east of the boundary line described in 49 CFR 71.7. Section 71.5 describes the Eastern-Central boundary under the heading Minnesota-Michigan-Wisconsin only along Michigan county lines in the Upper Peninsula (Gogebic, Ontonagon, Iron, Dickinson, and Menominee Counties) and then the western boundary of the State of Michigan; it does not enter Wisconsin. Section 71.7 describes the Central-Mountain boundary through Montana, North Dakota, South Dakota, Nebraska, Kansas, Oklahoma, and Texas, and does not mention Wisconsin. None of the five cities sits on a zone boundary.). OpenStreetMap was not used. Raw data: `/workspace/step8wi/`. Classification: `/workspace/checkdesk/research/wisconsin-geocode-classify-2026-11-18.md`.

Locator passes and official pages are the shared Wisconsin sweep (737 offices, all geocoded on the current and 2020 Census files, 0 errors). Classification still uses printed city and Census geocode, not the ZIP list. The five cities are ordinary incorporated places in their home counties, not independent cities. Milwaukee city has legal zero-population parts in Washington and Waukesha Counties; Madison, Green Bay, Kenosha, and Racine each sit in one home county. Classification uses place GEOIDs only, because a Milwaukee, Washington, or Waukesha County match would mix Milwaukee with other places in those counties. Out-of-state offices, including Madison, IL, stay off these lists. OpenStreetMap was not used.

## Listed (2)

- Racine (1438341, 603 MAIN ST, RACINE 53403). Lists money orders. Official page prints Racine, WI. All four Census legs are in Racine city. BUSINESS hours: weekdays 10:00 a.m. to 1:30 p.m. and 2:00 p.m. to 5:00 p.m., Saturday closed, Sunday closed. Not labeled Open evenings or Open weekends.
- West Racine (1438405, 1300 PERRY AVE, RACINE 53406). Lists money orders. Official page prints Racine, WI. All four Census legs are in Racine city. BUSINESS hours: weekdays 9:00 a.m. to 6:00 p.m., Saturday 9:00 a.m. to 4:00 p.m., Sunday closed. Labeled Open evenings and Open weekends.

## Held (1)

- Four Mile Station (1363914, 2635 4 MILE RD, RACINE 53404). Official page prints Racine, WI, and lists money orders. All four Census legs are in Caledonia village, not Racine city. Held because the printed city and the geocode disagree, including a village. Map-point fallback is not used, because the official map point is not inside Racine city.

Caledonia village and other Racine County places stay off this list.

## Result

2 listed Post Offices, with money orders, in Racine city, with no map-point fallbacks. One is labeled Open evenings: West Racine, until 6:00 p.m. One publishes Saturday hours and is labeled Open weekends: West Racine, 9:00 a.m. to 4:00 p.m. None publishes Sunday hours. Hours labeled Central Time. 1 hold.

## Site changes in this PR

- New `data/locations/racine.csv` and `/racine/`, `/racine/money-orders/`, and `/racine/after-hours/` pages.
- Racine is inserted under the existing Wisconsin section after Kenosha on the home page and `/cities/`. No other existing city CSV or page changed except the home and `/cities/` meta and list lines. The unsuffixed `/racine/` slug is new and does not collide with an existing page.
