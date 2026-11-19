"""Same-state links between published Check Desk city pages.

The city list is the grouping already published on /cities/: state headings
and the city links in each table. Each city index page links to other Check
Desk cities in that same state only. Selection walks forward from the city
in slug order and wraps around, capped so the block stays short. A cap of
one or more makes the directed graph a circulant, so every city in the
state can be reached by following these links. The block is not a
nearest-city list: coordinates are not used, and the heading does not say
nearby.

The /cities/ page has a real id on each state's heading, and city pages
link there. The build is deterministic and does not read the clock.
"""
import html
import re
from pathlib import Path

# Other cities shown besides the directory link. States with fewer cities
# show all of the others. One step would already connect the state; a short
# window keeps the hop count small without listing every city.
SIBLING_CAP = 6

_ARTICLE_CLOSE = "</article>"


def load(path):
    """Build the graph from src/pages/cities.html (or an equivalent page)."""
    text = Path(path).read_text()
    parts = re.split(r'<h2 id="([^"]+)">([^<]+)</h2>', text)
    if len(parts) < 4:
        raise SystemExit(f"no state headings in {path}")
    states = {}
    cities = []
    for i in range(1, len(parts), 3):
        state_id, state_name, body = parts[i], parts[i + 1], parts[i + 2]
        if state_id in states:
            raise SystemExit(f"duplicate state heading {state_id}")
        found = re.findall(
            r'<th scope="row"><a href="/([^"/]+)/">([^<]+)</a></th>', body
        )
        if not found:
            raise SystemExit(f"no city links under {state_name} in {path}")
        states[state_id] = state_name
        suffix = ", " + state_name
        for slug, name in found:
            short = name[: -len(suffix)] if name.endswith(suffix) else name
            cities.append({
                "slug": slug,
                "name": short,
                "state": state_id,
                "state_name": state_name,
            })
    return Graph(states, cities)


class Graph:
    def __init__(self, states, cities):
        self.states = states
        self.cities = cities
        seen = set()
        by_state = {}
        for city in cities:
            slug = city["slug"]
            if slug in seen:
                raise ValueError(f"duplicate city slug {slug}")
            if city["state"] not in states:
                raise ValueError(f"unknown state for {slug}")
            seen.add(slug)
            by_state.setdefault(city["state"], []).append(city)
        self.by_slug = {city["slug"]: city for city in cities}
        self.by_state = by_state
        counts = {}
        for city in cities:
            counts[city["name"]] = counts.get(city["name"], 0) + 1
        self.dup_names = {name for name, n in counts.items() if n > 1}
        for group in by_state.values():
            group.sort(key=lambda city: city["slug"])

    def siblings(self, slug, cap=SIBLING_CAP):
        """Other cities in this state. Empty when the state has only this city."""
        city = self.by_slug[slug]
        group = self.by_state[city["state"]]
        slugs = [item["slug"] for item in group]
        index = slugs.index(slug)
        count = len(group)
        take = min(cap, count - 1)
        picked = [group[(index + step) % count] for step in range(1, take + 1)]
        picked.sort(key=lambda item: (item["name"].lower(), item["slug"]))
        return picked

    def label(self, city):
        """Anchor text. A name used in more than one state keeps the state."""
        if city["name"] in self.dup_names:
            return city["name"] + ", " + self.states[city["state"]]
        return city["name"]

    def nav_html(self, slug):
        """Static section inserted at the bottom of the city index page."""
        city = self.by_slug[slug]
        state_name = self.states[city["state"]]
        heading_id = f"other-{city['state']}-cities"
        lines = [
            f'<section class="other-cities" aria-labelledby="{heading_id}">',
            f'<h2 id="{heading_id}">Other {html.escape(state_name)} cities</h2>',
        ]
        siblings = self.siblings(slug)
        if not siblings:
            return ""
        lines.append("<ul>")
        for other in siblings:
            href = "/" + other["slug"] + "/"
            text = html.escape(self.label(other))
            lines.append(f'<li><a href="{href}">{text}</a></li>')
        lines.append("</ul>")
        lines.append(
            f'<p class="small"><a href="/cities/#{city["state"]}">'
            f'All {html.escape(state_name)} cities</a></p>'
        )
        lines.append("</section>")
        return "\n".join(lines) + "\n"

    def inject(self, path, body):
        """Insert the section on a city index page, just before </article>.

        path is the builder's URL path, such as "denver/" or
        "denver/money-orders/". Pages that are not city indexes are
        returned unchanged.
        """
        if not path or "/" in path.strip("/"):
            return body
        slug = path.strip("/")
        if slug not in self.by_slug:
            return body
        nav = self.nav_html(slug)
        if not nav:
            return body
        if body.count(_ARTICLE_CLOSE) != 1 or not body.rstrip().endswith(_ARTICLE_CLOSE):
            raise SystemExit(
                f"{slug} should end with one </article> so the state links can be attached"
            )
        # Keep a blank line before the closing tag, as the source pages do.
        trimmed = body.rstrip()
        prefix = trimmed[: -len(_ARTICLE_CLOSE)].rstrip()
        return prefix + "\n\n" + nav + _ARTICLE_CLOSE + "\n"
