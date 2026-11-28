# Sacramento, California USPS research (2026-11-28, America/Denver)

Sixth California state city in the Census ranking (Vintage 2025, SUMLEV 162, POPESTIMATE2025). Census place is Sacramento city, GEOID 0664000, population 536,449. Official listed pages print Sacramento, CA. This is Sacramento, California, in Sacramento County, at /sacramento/. It is not West Sacramento (in Yolo County), Elk Grove, Rancho Cordova, Citrus Heights, Folsom, Roseville, or another separately incorporated place, and it is not a Census designated place such as Arden-Arcade, Florin, Foothill Farms, Lemon Hill, North Highlands, or Rosemont. Hours are Pacific Time (California is in the Pacific zone under 49 CFR 71.8). OpenStreetMap was not used. Raw data: `/workspace/checkdesk-seo/nightly/sacramento/`. Classification: `/workspace/checkdesk-seo/nightly/sacramento/classify.json`.

Locator passes and official pages are the Sacramento-area locator sweep (41 offices, all geocoded on the current and 2020 Census files, 0 errors). Classification still uses printed city and Census geocode, not the ZIP list.

## Listed (9)

- Broadway (1355937, 2121 BROADWAY, SACRAMENTO 95818). Lists money orders. Official page prints Sacramento, CA. All four Census legs are in Sacramento city. BUSINESS hours: weekdays 8:30 a.m. to 5:00 p.m., Saturday closed, Sunday closed. Not labeled Open evenings or Open weekends.
- Camellia (1356743, 4750 J ST, SACRAMENTO 95819). Lists money orders. Official page prints Sacramento, CA. All four Census legs are in Sacramento city. BUSINESS hours: weekdays 8:30 a.m. to 5:00 p.m., Saturday closed, Sunday closed. Not labeled Open evenings or Open weekends.
- Del Paso Heights (1360560, 3817 MARYSVILLE BLVD, SACRAMENTO 95838). Lists money orders. Official page prints Sacramento, CA. All four Census legs are in Sacramento city. BUSINESS hours: weekdays 10:00 a.m. to 5:00 p.m., Saturday 10:00 a.m. to 12:00 p.m., Sunday closed. Labeled Open weekends.
- Fort Sutter (1363851, 1618 ALHAMBRA BLVD, SACRAMENTO 95816). Lists money orders. Official page prints Sacramento, CA. All four Census legs are in Sacramento city. BUSINESS hours: weekdays 9:00 a.m. to 5:00 p.m., Saturday 9:30 a.m. to 5:00 p.m., Sunday closed. Labeled Open weekends.
- Land Park (1369795, 5930 S LAND PARK DR, SACRAMENTO 95822). Lists money orders. Official page prints Sacramento, CA. All four Census legs are in Sacramento city. BUSINESS hours: weekdays 9:00 a.m. to 5:00 p.m., Saturday 10:00 a.m. to 2:00 p.m., Sunday closed. Labeled Open weekends.
- North Natomas (1456393, 4401 GATEWAY PARK BLVD STE 130, SACRAMENTO 95834). Lists money orders. Official page prints Sacramento, CA. All four Census legs are in Sacramento city. BUSINESS hours: weekdays 9:00 a.m. to 4:30 p.m., Saturday closed, Sunday closed. Not labeled Open evenings or Open weekends.
- Oak Park (1375730, 2929 35TH ST, SACRAMENTO 95817). Lists money orders. Official page prints Sacramento, CA. All four Census legs are in Sacramento city. BUSINESS hours: weekdays 9:00 a.m. to 5:00 p.m., Saturday closed, Sunday closed. Not labeled Open evenings or Open weekends.
- Parkway (1376871, 4301 BROOKFIELD DR, SACRAMENTO 95823). Lists money orders. Official page prints Sacramento, CA. Map-point fallback (medium confidence). BUSINESS hours: weekdays 10:00 a.m. to 5:00 p.m., Saturday 10:00 a.m. to 3:00 p.m., Sunday closed. Labeled Open weekends.
- Sacramento (1380219, 2000 ROYAL OAKS DR, SACRAMENTO 95813). Lists money orders. Official page prints Sacramento, CA. All four Census legs are in Sacramento city. BUSINESS hours: weekdays 10:00 a.m. to 6:00 p.m., Saturday 9:30 a.m. to 4:30 p.m., Sunday closed. Labeled Open evenings and Open weekends.

## Held (10)

- Arden (1353283, 2801 ARDEN WAY, SACRAMENTO 95825), Town and Country (1384884, 2929 FULTON AVE, SACRAMENTO 95821). Lists money orders; prints Sacramento, CA. All four Census legs are in Arden-Arcade CDP. Held, not in Sacramento city.
- Colonial (1358731, 6024 44TH ST, SACRAMENTO 95824): all four legs in Lemon Hill CDP. Held.
- Florin (1363575, 7250 ELK GROVE FLORIN RD, SACRAMENTO 95829): all four legs in Florin CDP. Held.
- Foothill Farms (1363633, 5420 KOHLER AVE, SACRAMENTO 95841): all four legs in North Highlands CDP. Held.
- Perkins (1377226, 9500 KIEFER BLVD, SACRAMENTO 95827): all four legs in Rosemont CDP. Held.
- Downtown Plaza (1610415), Centre (1357547), Sacramento CA SDC (1601561): print Sacramento, CA; official pages do not list money orders. Held. Elkhorn Carrier Annex (1362330): no money-order tags and no Sacramento city geocode. Held.

Offices printing West Sacramento, Elk Grove, Rancho Cordova, Citrus Heights, Carmichael, Rio Linda, North Highlands, and other nearby places found in the locator sweep stay off this list.

## Result

9 listed Post Offices (8 clean, 1 map-point fallback), all with money orders, all in Sacramento County. One is labeled Open evenings: Sacramento, until 6:00 p.m. Five publish Saturday hours and are labeled Open weekends. None publishes Sunday hours. Hours labeled Pacific Time. 10 holds.

## Site changes in this PR

- New `data/locations/sacramento.csv` and `/sacramento/`, `/sacramento/money-orders/`, and `/sacramento/after-hours/` pages.
- Sacramento is inserted under the existing California section after Fresno on the home page and `/cities/`. No other existing city CSV or page changed except the home and `/cities/` meta and list lines. The unsuffixed `/sacramento/` slug is new and does not collide with an existing page.
