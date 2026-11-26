#!/usr/bin/env python3
"""Audit internal links, canonicals, FAQ schema, titles, and same-state city links.

From the repo root:

    python3 site-src/tools/test_links.py

Builds the site once in a temporary directory. It does not write site-src/public/.
Titles over 60 characters and broken links, canonicals, or FAQ mismatches fail
the run. Meta descriptions outside 140-160 characters are reported as warnings.
"""
import html as html_mod
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "site-src"))
import statelinks  # noqa: E402

BUILD = ROOT / "site-src" / "build.py"
CITIES_PAGE = ROOT / "site-src" / "src" / "pages" / "cities.html"
BASE = "https://checkdesk.us/"
TITLE_MAX = 60
DESC_MIN = 140
DESC_MAX = 160

_ATTR = re.compile(r'''\b(?:href|src)\s*=\s*(["'])(.*?)\1''', re.I | re.S)
_CANON = re.compile(r'<link\s+rel="canonical"\s+href="([^"]+)"')
_OGURL = re.compile(r'<meta\s+property="og:url"\s+content="([^"]+)"')
_TITLE = re.compile(r"<title>(.*?)</title>", re.S)
_DESC = re.compile(r'<meta\s+name="description"\s+content="([^"]*)"')
_ROBOTS = re.compile(r'<meta\s+name="robots"\s+content="([^"]*)"', re.I)
_JSONLD = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)
_ID = re.compile(r'\sid="([^"]+)"')


def reachability(graph):
    for code, group in graph.by_state.items():
        slugs = [city["slug"] for city in group]
        outgoing = {
            city["slug"]: [item["slug"] for item in graph.siblings(city["slug"])]
            for city in group
        }
        for start in slugs:
            seen = set()
            stack = [start]
            while stack:
                cur = stack.pop()
                if cur in seen:
                    continue
                seen.add(cur)
                stack.extend(outgoing[cur])
            missing = [slug for slug in slugs if slug not in seen]
            if missing:
                raise SystemExit(f"{code}: {start} cannot reach {missing[:8]}")
        sets = [tuple(outgoing[slug]) for slug in slugs]
        if len(slugs) > statelinks.SIBLING_CAP + 1 and len(set(sets)) == 1:
            raise SystemExit(f"{code}: every city links to the same set")


def check_graph():
    graph = statelinks.load(CITIES_PAGE)
    if not graph.cities:
        raise SystemExit("cities.html produced an empty city graph")
    if len(graph.by_state) != 50:
        raise SystemExit(f"expected 50 states, found {len(graph.by_state)}")
    if min(len(group) for group in graph.by_state.values()) < 2:
        raise SystemExit("a published state has fewer than two cities")
    reachability(graph)
    # Colorado is the only state large enough that rotation has to vary.
    colorado = graph.by_state["colorado"]
    if len(colorado) <= statelinks.SIBLING_CAP + 1:
        raise SystemExit("Colorado should have more than 7 cities so rotation can be checked")
    first = [city["slug"] for city in colorado[:5]]
    varied = False
    for city in colorado:
        picked = [item["slug"] for item in graph.siblings(city["slug"])]
        if city["slug"] in picked:
            raise SystemExit(f"{city['slug']} links to itself")
        if len(picked) != statelinks.SIBLING_CAP or len(set(picked)) != statelinks.SIBLING_CAP:
            raise SystemExit(f"{city['slug']} should link to {statelinks.SIBLING_CAP} distinct cities")
        if any(graph.by_slug[slug]["state"] != "colorado" for slug in picked):
            raise SystemExit(f"{city['slug']} has a non-Colorado sibling")
        if not set(picked) <= set(first):
            varied = True
    if not varied:
        raise SystemExit("Colorado links must not all stay inside the alphabetical first cities")
    for state, group in graph.by_state.items():
        if len(group) <= statelinks.SIBLING_CAP + 1:
            for city in group:
                others = {item["slug"] for item in group if item["slug"] != city["slug"]}
                got = {item["slug"] for item in graph.siblings(city["slug"])}
                if got != others:
                    raise SystemExit(f"{city['slug']}: expected all other {state} cities, got {got}")
    # Names used in more than one state keep the state in the label.
    if graph.label(graph.by_slug["aurora"]) != "Aurora, Colorado":
        raise SystemExit(f"aurora label: {graph.label(graph.by_slug['aurora'])!r}")
    if graph.label(graph.by_slug["aurora-il"]) != "Aurora, Illinois":
        raise SystemExit(f"aurora-il label: {graph.label(graph.by_slug['aurora-il'])!r}")
    if graph.label(graph.by_slug["portland"]) != "Portland, Maine":
        raise SystemExit(f"portland label: {graph.label(graph.by_slug['portland'])!r}")
    if graph.label(graph.by_slug["portland-or"]) != "Portland, Oregon":
        raise SystemExit(f"portland-or label: {graph.label(graph.by_slug['portland-or'])!r}")
    if graph.label(graph.by_slug["denver"]) != "Denver":
        raise SystemExit(f"denver label: {graph.label(graph.by_slug['denver'])!r}")
    nav = graph.nav_html("denver")
    if "nearest" in nav.lower() or "nearby" in nav.lower():
        raise SystemExit("sibling nav must not say nearby or nearest")
    if 'href="/cities/#colorado"' not in nav:
        raise SystemExit("denver nav should link to /cities/#colorado")
    if "Other Colorado cities" not in nav:
        raise SystemExit("denver nav heading should be 'Other Colorado cities'")
    if 'href="/denver/"' in nav:
        raise SystemExit("denver nav links to itself")
    print("graph ok", len(graph.cities), "cities in", len(graph.by_state), "states")
    return graph


def plain_faq(fragment):
    """Same visible-text rules build.py uses for FAQPage JSON-LD."""
    x = re.sub(r"<sup>.*?</sup>", "", fragment, flags=re.S)
    x = html_mod.unescape(re.sub(r"<[^>]+>", "", x))
    x = re.sub(r"\s+", " ", x).strip()
    return re.sub(r"\s+([.,;:])", r"\1", x)


def jsonld_graph(html):
    blocks = _JSONLD.findall(html)
    if not blocks:
        return None
    if len(blocks) != 1:
        raise SystemExit(f"expected one JSON-LD block, found {len(blocks)}")
    return json.loads(blocks[0].strip().replace("<\\/", "</"))


def detail_pairs(html):
    return re.findall(r"<details><summary>(.*?)</summary>(.*?)</details>", html, re.S)


def visible_question_faqs(html):
    """FAQ schema follows question disclosures only, not every <details> list."""
    return [(q, a) for q, a in detail_pairs(html) if plain_faq(q).endswith("?")]


def assert_visible_faq_matches_schema(html, label):
    graph = jsonld_graph(html)
    visible = visible_question_faqs(html)
    if graph is None:
        if visible:
            raise SystemExit(f"{label}: FAQ details without JSON-LD")
        return
    articles = [node for node in graph["@graph"] if node.get("@type") == "Article"]
    faqs = [node for node in graph["@graph"] if node.get("@type") == "FAQPage"]
    if not articles:
        if faqs:
            raise SystemExit(f"{label}: FAQPage without an Article")
        return
    if not visible:
        if faqs:
            raise SystemExit(f"{label}: FAQPage markup without a visible FAQ")
        return
    if len(faqs) != 1:
        raise SystemExit(f"{label}: expected one FAQPage, found {len(faqs)}")
    canon = _CANON.search(html)
    if not canon or faqs[0].get("url") != canon.group(1):
        raise SystemExit(f"{label}: FAQPage url is not the page canonical")
    main = faqs[0]["mainEntity"]
    if len(main) != len(visible):
        raise SystemExit(f"{label}: FAQ count {len(visible)} visible vs {len(main)} in JSON-LD")
    names = []
    for (question, answer), item in zip(visible, main):
        q, a = plain_faq(question), plain_faq(answer)
        if not q or not a:
            raise SystemExit(f"{label}: empty FAQ question or answer")
        if item.get("@type") != "Question" or item.get("acceptedAnswer", {}).get("@type") != "Answer":
            raise SystemExit(f"{label}: FAQ entity types are not Question/Answer")
        if item.get("name") != q or item.get("acceptedAnswer", {}).get("text") != a:
            raise SystemExit(f"{label}: visible FAQ does not match JSON-LD ({q!r})")
        names.append(q)
    if len(names) != len({name.casefold() for name in names}):
        raise SystemExit(f"{label}: duplicate FAQ questions")
    for question, _ in detail_pairs(html):
        label_text = plain_faq(question)
        if not label_text.endswith("?") and label_text in names:
            raise SystemExit(f"{label}: non-question disclosure is in FAQPage ({label_text!r})")


def page_url(rel: Path) -> str:
    """Built file path (relative to the output dir) -> canonical URL."""
    posix = rel.as_posix()
    if posix == "index.html":
        return BASE
    if posix.endswith("/index.html"):
        return BASE + posix[: -len("index.html")]
    return BASE + posix


def built_page_path(out: Path, url_path: str) -> Path:
    """Map a site path to a file in the build output."""
    path = url_path.split("?", 1)[0]
    path = unquote(path)
    if path.endswith("/"):
        return out / path.lstrip("/") / "index.html"
    candidate = out / path.lstrip("/")
    return candidate


def ids_in(html: str) -> set:
    return set(_ID.findall(html))


def check_internal_links(out: Path, html: str, label: str, errors: list):
    for _, raw in _ATTR.findall(html):
        href = html_mod.unescape(raw.strip())
        if not href or href.startswith(("mailto:", "tel:", "data:", "javascript:")):
            continue
        parsed = urlparse(href)
        if parsed.scheme in ("http", "https"):
            if parsed.netloc and parsed.netloc not in {"checkdesk.us", "www.checkdesk.us"}:
                continue
            site_path = parsed.path or "/"
        elif parsed.scheme:
            errors.append(f"{label}: unsupported URL scheme in {href!r}")
            continue
        else:
            if href.startswith("#"):
                site_path = None
                fragment = href[1:]
                if fragment and fragment not in ids_in(html):
                    errors.append(f"{label}: missing fragment #{fragment}")
                continue
            if not href.startswith("/"):
                errors.append(f"{label}: relative link {href!r} (use a root-absolute path)")
                continue
            site_path = parsed.path or "/"
        fragment = parsed.fragment
        target = built_page_path(out, site_path)
        if not target.is_file():
            # Directory without a trailing slash should still fail, because
            # published page URLs use a trailing slash.
            errors.append(f"{label}: broken internal link {href!r}")
            continue
        if fragment:
            dest_html = target.read_text() if target.suffix == ".html" else ""
            if target.suffix == ".html" and fragment not in ids_in(dest_html):
                errors.append(f"{label}: {href!r} is missing #{fragment}")


def is_noindex(html: str) -> bool:
    m = _ROBOTS.search(html)
    return bool(m and "noindex" in m.group(1).lower())


def check_seo_head(html: str, rel: Path, warnings: list, errors: list):
    label = rel.as_posix()
    if is_noindex(html):
        return
    title_m = _TITLE.search(html)
    if not title_m:
        errors.append(f"{label}: missing <title>")
        return
    title = html_mod.unescape(re.sub(r"\s+", " ", title_m.group(1)).strip())
    if len(title) > TITLE_MAX:
        errors.append(f"{label}: title is {len(title)} characters (max {TITLE_MAX}): {title!r}")
    desc_m = _DESC.search(html)
    if not desc_m:
        errors.append(f"{label}: missing meta description")
    else:
        desc = html_mod.unescape(desc_m.group(1))
        if not desc.strip():
            errors.append(f"{label}: empty meta description")
        elif not DESC_MIN <= len(desc) <= DESC_MAX:
            warnings.append(
                f"{label}: meta description is {len(desc)} characters "
                f"(expected {DESC_MIN}-{DESC_MAX})"
            )
    expect = page_url(rel)
    if not expect.endswith("/") and rel.name == "index.html":
        expect = expect  # page_url already adds the slash for index.html
    canon_m = _CANON.search(html)
    if not canon_m:
        errors.append(f"{label}: missing canonical")
        return
    canon = canon_m.group(1)
    if canon != expect:
        errors.append(f"{label}: canonical {canon!r} != {expect!r}")
    if not canon.startswith(BASE) or (canon != BASE and not canon.endswith("/")):
        errors.append(f"{label}: canonical must be a https://checkdesk.us/ URL with a trailing slash")
    og_m = _OGURL.search(html)
    if not og_m:
        errors.append(f"{label}: missing og:url")
    elif og_m.group(1) != canon:
        errors.append(f"{label}: og:url {og_m.group(1)!r} does not match canonical")


def section_hrefs(html: str, heading_id_prefix: str = "other-") -> list:
    blocks = re.findall(
        r'<section class="other-cities"[^>]*>(.*?)</section>', html, re.S
    )
    if not blocks:
        return []
    return re.findall(r'href="(/[a-z0-9-]+/)"', blocks[0])


def check_site(out: Path, graph):
    errors = []
    warnings = []
    html_pages = sorted(p for p in out.rglob("*.html"))
    if not html_pages:
        raise SystemExit("build produced no HTML")
    city_pages_with_siblings = 0
    for path in html_pages:
        rel = path.relative_to(out)
        html = path.read_text()
        label = rel.as_posix()
        check_internal_links(out, html, label, errors)
        check_seo_head(html, rel, warnings, errors)
        if not is_noindex(html):
            try:
                assert_visible_faq_matches_schema(html, label)
            except SystemExit as exc:
                errors.append(str(exc))

        # Same-state links belong on city index pages only
        # (output path "slug/index.html", not a service subpage).
        parts = rel.parts
        is_city_index = (
            rel.name == "index.html"
            and len(parts) == 2
            and parts[0] in graph.by_slug
        )
        is_city_subpage = (
            rel.name == "index.html"
            and len(parts) == 3
            and parts[0] in graph.by_slug
        )
        heading = re.search(
            r'<section class="other-cities"[^>]*>\s*<h2 id="([^"]+)">([^<]+)</h2>',
            html, re.S
        )
        if is_city_index:
            slug = parts[0]
            expect = [item["slug"] for item in graph.siblings(slug)]
            if not expect:
                if heading:
                    errors.append(f"{label}: unexpected sibling section")
                continue
            if not heading:
                errors.append(f"{label}: missing Other cities section")
                continue
            hid, htext = heading.group(1), heading.group(2)
            state_name = graph.by_slug[slug]["state_name"]
            state_id = graph.by_slug[slug]["state"]
            if hid != f"other-{state_id}-cities" or htext != f"Other {state_name} cities":
                errors.append(f"{label}: bad sibling heading {hid!r} {htext!r}")
            hrefs = section_hrefs(html)
            got = [h.strip("/") for h in hrefs]
            if got != expect:
                errors.append(f"{label}: sibling links {got} != {expect}")
            if slug in got:
                errors.append(f"{label}: sibling list includes itself")
            if 'href="/cities/#' + state_id + '"' not in html:
                errors.append(f"{label}: missing All {state_name} cities link")
            section_text = heading.group(0).lower()
            if "nearby" in section_text or "nearest" in section_text:
                errors.append(f"{label}: sibling heading says nearby/nearest")
            city_pages_with_siblings += 1
        elif is_city_subpage and '<section class="other-cities"' in html:
            errors.append(f"{label}: sibling section should only appear on the city index")

        expect_sibling_pages = sum(1 for slug in graph.by_slug if graph.siblings(slug))
    if city_pages_with_siblings != expect_sibling_pages:
        errors.append(
            f"city pages with sibling links: {city_pages_with_siblings} != {expect_sibling_pages}"
        )

    # sitemap should list every indexable built page
    sm = (out / "sitemap.xml").read_text()
    robots = (out / "robots.txt").read_text()
    if f"Sitemap: {BASE}sitemap.xml" not in robots:
        errors.append("robots.txt is missing the sitemap line")
    if "Disallow:" in robots:
        errors.append("robots.txt should not disallow any path")
    for agent in ("GPTBot", "ClaudeBot", "PerplexityBot", "Google-Extended", "Applebot-Extended", "CCBot"):
        if f"User-agent: {agent}\nAllow: /" not in robots:
            errors.append(f"robots.txt should explicitly allow {agent}")

    if errors:
        print("\n".join(errors[:80]))
        if len(errors) > 80:
            print(f"... and {len(errors) - 80} more errors")
        raise SystemExit(f"audit failed: {len(errors)} error(s), {len(warnings)} warning(s)")
    for line in warnings:
        print("WARNING", line)
    print(
        "html ok",
        len(html_pages),
        "pages;",
        city_pages_with_siblings,
        "city pages with sibling links;",
        len(warnings),
        "description warning(s)",
    )
    return city_pages_with_siblings, warnings


def main():
    graph = check_graph()
    with tempfile.TemporaryDirectory() as tmp:
        print("building", tmp)
        subprocess.run([sys.executable, str(BUILD), "--out", tmp], check=True, cwd=ROOT)
        check_site(Path(tmp), graph)
    print("ok")


if __name__ == "__main__":
    main()
