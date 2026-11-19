# Green Bay, Wisconsin USPS research (2026-11-18, America/Denver)

Third Wisconsin state city in the Census ranking (Vintage 2025, SUMLEV 162, POPESTIMATE2025). Census place is Green Bay city, GEOID 5531000, population 106,675. Official listed pages print Green Bay, WI. This is Green Bay, Wisconsin, at /green-bay/. This is not Green Bay town (SUMLEV 061), not Ashwaubenon, not De Pere, and not a Green Bay in another state. A Brown County geocode is not enough to list an office here. Hours are Central Time (The central zone under 49 CFR 71.6(a) is west of the boundary line described in 49 CFR 71.5 and east of the boundary line described in 49 CFR 71.7. Section 71.5 describes the Eastern-Central boundary under the heading Minnesota-Michigan-Wisconsin only along Michigan county lines in the Upper Peninsula (Gogebic, Ontonagon, Iron, Dickinson, and Menominee Counties) and then the western boundary of the State of Michigan; it does not enter Wisconsin. Section 71.7 describes the Central-Mountain boundary through Montana, North Dakota, South Dakota, Nebraska, Kansas, Oklahoma, and Texas, and does not mention Wisconsin. None of the five cities sits on a zone boundary.). OpenStreetMap was not used. Raw data: `/workspace/step8wi/`. Classification: `/workspace/checkdesk/research/wisconsin-geocode-classify-2026-11-18.md`.

Locator passes and official pages are the shared Wisconsin sweep (737 offices, all geocoded on the current and 2020 Census files, 0 errors). Classification still uses printed city and Census geocode, not the ZIP list. The five cities are ordinary incorporated places in their home counties, not independent cities. Milwaukee city has legal zero-population parts in Washington and Waukesha Counties; Madison, Green Bay, Kenosha, and Racine each sit in one home county. Classification uses place GEOIDs only, because a Milwaukee, Washington, or Waukesha County match would mix Milwaukee with other places in those counties. Out-of-state offices, including Madison, IL, stay off these lists. OpenStreetMap was not used.

## Listed (3)

- Downtown Green Bay (1438308, 118 N MONROE AVE, GREEN BAY 54301). Lists money orders. Official page prints Green Bay, WI. All four Census legs are in Green Bay city. BUSINESS hours: weekdays 8:00 a.m. to 5:30 p.m., Saturday 9:00 a.m. to 12:00 p.m., Sunday closed. Labeled Open evenings and Open weekends.
- Green Bay (1438317, 300 PACKERLAND DR, GREEN BAY 54303). Lists money orders. Official page prints Green Bay, WI. All four Census legs are in Green Bay city. BUSINESS hours: weekdays 8:30 a.m. to 6:00 p.m., Saturday 8:30 a.m. to 2:00 p.m., Sunday closed. Labeled Open evenings and Open weekends.
- John P Cofrin (1368469, 1950 COFRIN DR, GREEN BAY 54302). Lists money orders. Official page prints Green Bay, WI. All four Census legs are in Green Bay city. BUSINESS hours: weekdays 8:00 a.m. to 5:30 p.m., Saturday 9:30 a.m. to 12:00 p.m., Sunday closed. Labeled Open evenings and Open weekends.

## Held (1)

- Hansen Road (1438297, 790 HANSEN RD STE E, GREEN BAY 54304). Official page prints Green Bay, WI, and lists money orders. All four Census legs are in Ashwaubenon village, not Green Bay city. Held because the printed city and the geocode disagree, including a village. Map-point fallback is not used, because the official map point is not inside Green Bay city.

Ashwaubenon village, Green Bay town (SUMLEV 061), and other Brown County places stay off this list.

## Result

3 listed Post Offices, with money orders, in Green Bay city, with no map-point fallbacks. Three are labeled Open evenings: Downtown Green Bay, until 5:30 p.m., Green Bay, until 6:00 p.m., and John P Cofrin, until 5:30 p.m. All three publish Saturday hours and are labeled Open weekends. None publishes Sunday hours. Hours labeled Central Time. 1 hold.

## Site changes in this PR

- New `data/locations/green-bay.csv` and `/green-bay/`, `/green-bay/money-orders/`, and `/green-bay/after-hours/` pages.
- Green Bay is inserted under the existing Wisconsin section after Madison on the home page and `/cities/`. No other existing city CSV or page changed except the home and `/cities/` meta and list lines. The unsuffixed `/green-bay/` slug is new and does not collide with an existing page.
