#!/usr/bin/env python3
"""Fail the build when the rendered site regresses on SEO basics.

Runs against ./public after `hugo`, so it checks what search engines actually
receive rather than what the front matter says. Every rule here exists because
the 2026-08-09 audit found it broken or found it one edit away from breaking.

Two severities, because they need different responses:

  structural  A template or config fault — every page is wrong at once, and one
              edit fixes all of them. Always fails the build.
  content     A backlog item on one page: an overlong title, a post missing its
              translation. Reported always, fails only under --strict, so a
              stale backlog never blocks tomorrow's brief from publishing.

There is also a source mode that reads content/ front matter directly, with no
Hugo build and no dependencies. It exists so whoever *writes* a post — including
Hermes Agent, which commits the daily brief straight into this repo — can catch
an overlong title at authoring time instead of after publish.

Usage:
    hugo --minify && python3 scripts/seo_check.py [--public public] [--strict]
    python3 scripts/seo_check.py --source [path ...]
"""
import argparse
import collections
import glob
import os
import re
import sys
import unicodedata
from html.parser import HTMLParser

BASE = "https://john.onlee.io"

# Google truncates a title by pixel width, not character count, and a Hangul
# syllable renders about twice as wide as a Latin letter (an approximation, but
# the right direction — counting characters let Korean titles run roughly double
# the real width). Titles carry a " | John on Lee" suffix, which comes from
# `title:` in hugo.yaml; keep the two in step.
#
# Truncation starts near 60 columns, but a truncated title still ranks the same
# — the cost is click-through, not position. So the limit sits at 75, where
# Google reliably cuts or rewrites the title outright. Titles between 60 and 75
# do get truncated in results; that is an accepted trade for one enforced
# number. A softer "aim for 60" target was considered and dropped: whatever the
# check enforces is what gets written, so a second unenforced number would only
# drift out of step with this one. Revisit once there is real click-through
# data to argue from.
MAX_TITLE = 75
MAX_DESC = 160
TITLE_SUFFIX = " | John on Lee"


def columns(text):
    """Approximate rendered width: East Asian wide/fullwidth chars count 2."""
    return sum(2 if unicodedata.east_asian_width(c) in ("W", "F") else 1
               for c in text)

# Pages that are redirect stubs or error pages: exempt from content rules.
SKIP_SUFFIXES = ("/404.html",)


class Head(HTMLParser):
    """Collects the head tags and body links this check reasons about."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.meta = {}
        self.title = ""
        self.canonical = None
        self.hreflang = []
        self.hrefs = []
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == "title":
            self._in_title = True
        elif tag == "meta":
            name = (d.get("name") or d.get("property") or "").lower()
            if name:
                self.meta[name] = d.get("content", "")
        elif tag == "link":
            rel = (d.get("rel") or "").lower()
            if "canonical" in rel:
                self.canonical = d.get("href")
            if "alternate" in rel and d.get("hreflang"):
                self.hreflang.append((d["hreflang"], d.get("href", "")))
        elif tag == "a":
            self.hrefs.append(d.get("href", ""))

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data


FM_FIELD = r'^{key}:\s*(?:"(?P<q>(?:[^"\\]|\\.)*)"|(?P<p>[^\n#]+?))\s*$'


def front_matter_field(block, key):
    """Read one scalar field out of a YAML front-matter block.

    Deliberately regex-based rather than a YAML dependency: this mode has to run
    anywhere the brief is written, including places that have only stock Python.
    """
    m = re.search(FM_FIELD.format(key=key), block, re.MULTILINE)
    if not m:
        return None
    value = m.group("q")
    if value is not None:
        return value.replace('\\"', '"')
    return m.group("p").strip().strip("'")


def check_source(paths):
    """Check content/ front matter without building the site."""
    targets = []
    for p in paths or ["content"]:
        if os.path.isdir(p):
            targets += glob.glob(os.path.join(p, "**", "*.md"), recursive=True)
        elif os.path.isfile(p):
            targets.append(p)
        else:
            # A caller passing the wrong date should get a sentence, not a
            # traceback — this runs unattended inside the brief generator.
            print(f"error: no such file or directory: {p}", file=sys.stderr)
            return 2

    if not targets:
        print(f"error: no markdown files under: {', '.join(paths or ['content'])}",
              file=sys.stderr)
        return 2

    issues = []
    checked = 0
    for path in sorted(set(targets)):
        text = open(path, encoding="utf-8").read()
        m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
        if not m:
            continue
        block = m.group(1)
        checked += 1

        title = front_matter_field(block, "title")
        if title:
            rendered = columns(title + TITLE_SUFFIX)
            if rendered > MAX_TITLE:
                over = rendered - MAX_TITLE
                issues.append(
                    f"{path}: title renders {rendered} columns wide "
                    f"(max {MAX_TITLE}); cut {over} more "
                    f"(Korean characters count 2)"
                )

        # `description` wins in the template; `summary` is the usual field.
        desc = (front_matter_field(block, "description")
                or front_matter_field(block, "summary"))
        if desc and columns(desc) > MAX_DESC:
            issues.append(
                f"{path}: description {columns(desc)} columns "
                f"(max {MAX_DESC})")

        # Every post ships as a ko+en pair. Only bundles are paired this way;
        # a lone .md (like a section _index) is not necessarily a post.
        base = os.path.basename(path)
        for this_lang, other_lang in (("ko", "en"), ("en", "ko")):
            if base.endswith(f".{this_lang}.md"):
                twin = path[: -len(f".{this_lang}.md")] + f".{other_lang}.md"
                if not os.path.exists(twin):
                    issues.append(f"{path}: no {other_lang} translation alongside it")

    for i in issues:
        print(f"content: {i}", file=sys.stderr)
    print(f"\nseo_check --source: {checked} files, {len(issues)} issue(s)")
    return 1 if issues else 0


def load_pages(root):
    for dirpath, _, filenames in os.walk(root):
        for name in filenames:
            if name not in ("index.html", "404.html"):
                continue
            path = os.path.join(dirpath, name)
            url = "/" + os.path.relpath(path, root).replace("index.html", "")
            yield url, path


def target_exists(root, href):
    path = href.split("#")[0].split("?")[0]
    if not path:
        return True
    fs = os.path.join(root, path.lstrip("/"))
    if os.path.isdir(fs):
        return os.path.exists(os.path.join(fs, "index.html"))
    return os.path.exists(fs)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--public", default="public", help="built site directory")
    ap.add_argument("--strict", action="store_true",
                    help="also fail on content issues, not just structural ones")
    ap.add_argument("--source", action="store_true",
                    help="check content/ front matter instead of a built site")
    ap.add_argument("paths", nargs="*",
                    help="with --source: files or directories to check")
    args = ap.parse_args()

    if args.source:
        return check_source(args.paths)

    root = os.path.abspath(args.public)
    if not os.path.isdir(root):
        print(f"structural: {root} does not exist — run hugo first", file=sys.stderr)
        return 1

    structural, content, noindexed = [], [], []
    descriptions = collections.defaultdict(list)
    checked = 0

    for url, path in sorted(load_pages(root)):
        html = open(path, encoding="utf-8").read()
        head = Head()
        head.feed(html.split("</head>")[0])
        body = Head()
        body.feed(html)

        # Redirect stubs (Hugo aliases) carry no robots tag and are not content.
        robots = head.meta.get("robots", "")
        if not robots:
            continue
        # Pages deliberately kept out of the index (robotsNoIndex in front
        # matter) do not have to satisfy rules about how they rank, but they
        # must not also be advertised in the sitemap.
        if "noindex" in robots:
            noindexed.append(url)
            continue
        if url.endswith(SKIP_SUFFIXES):
            continue

        if not head.canonical:
            structural.append(f"{url}: no canonical link")
            continue
        # Paginated list pages (/brief/page/2/) canonicalize to page 1, so they
        # are not independently indexed and share its title and description by
        # design. Only pages that are their own canonical get content rules.
        if head.canonical.rstrip("/") != (BASE + url).rstrip("/"):
            continue
        checked += 1

        title = head.title.strip()
        desc = head.meta.get("description", "").strip()

        if not title:
            structural.append(f"{url}: no <title>")
        elif columns(title) > MAX_TITLE:
            content.append(f"{url}: title {columns(title)} columns (max {MAX_TITLE})")

        if not desc:
            structural.append(f"{url}: no meta description")
        else:
            descriptions[desc].append(url)
            if columns(desc) > MAX_DESC:
                content.append(
                    f"{url}: description {columns(desc)} columns (max {MAX_DESC})")

        # Social cards: PaperMod only emits these from a page cover, and the
        # site-wide default lives in hugo.yaml's cascade. Losing that cascade
        # silently downgrades every share to a bare text card.
        if not head.meta.get("og:image"):
            structural.append(f"{url}: no og:image")
        if head.meta.get("twitter:card") != "summary_large_image":
            structural.append(f"{url}: twitter:card is not summary_large_image")

        # A missing ko/en pair is a content gap (that post was never translated).
        # A missing x-default when the pair *does* exist is a template fault.
        langs = {lang for lang, _ in head.hreflang}
        if "ko" not in langs or "en" not in langs:
            content.append(f"{url}: no ko/en translation pair (got {sorted(langs - {'x-default'})})")
        elif "x-default" not in langs:
            structural.append(f"{url}: hreflang missing x-default")

        for href in body.hrefs:
            if not href or href.startswith(("#", "mailto:", "tel:", "javascript:")):
                continue
            if href.startswith(BASE):
                href = href[len(BASE):]
            if href.startswith("http"):
                continue
            if href.startswith("/") and not target_exists(root, href):
                structural.append(f"{url}: broken internal link -> {href}")

    # Head assets the theme links on every page; a missing one 404s site-wide.
    # favicon.ico is linked by nothing, but browsers and crawlers request it by
    # convention — Google's coverage report logged it as a 404 on 2026-06-06.
    for asset in ("og-default.png", "safari-pinned-tab.svg", "favicon.png",
                  "favicon.ico", "apple-touch-icon.png"):
        if not os.path.exists(os.path.join(root, asset)):
            structural.append(f"static asset referenced in <head> is missing: /{asset}")

    sitemaps = ""
    for name in ("sitemap.xml", "robots.txt"):
        target = os.path.join(root, name)
        if not os.path.exists(target) or os.path.getsize(target) == 0:
            structural.append(f"{name} is missing or empty")
        elif name.endswith("sitemap.xml"):
            sitemaps = open(target, encoding="utf-8").read()

    # layouts/sitemapindex.xml replaces Hugo's split index with one flat urlset
    # at the root, so every listed URL sits inside the sitemap's own directory.
    # If that override is ever lost, the root sitemap silently becomes an index
    # of /ko/ and /en/ children again, and the listings go out of path scope.
    if sitemaps:
        if "<sitemapindex" in sitemaps:
            structural.append(
                "sitemap.xml is a sitemap index again — layouts/sitemapindex.xml "
                "should render one flat urlset at the root")
        listed = sitemaps.count("<loc>")
        if listed < checked:
            structural.append(
                f"sitemap.xml lists {listed} URLs but {checked} pages are indexable")

    # A sitemap entry says "index this" while the page says "noindex" — Google
    # reports the contradiction rather than picking a side.
    for url in noindexed:
        if f"<loc>{BASE}{url}</loc>" in sitemaps:
            structural.append(f"{url}: noindex page is still listed in the sitemap")

    # Duplicate descriptions are how the tag pages ended up sharing the site
    # blurb. A ko page and its en translation never collide (different
    # languages), so any repeat here means a template fell back to the default.
    for desc, urls in descriptions.items():
        if len(urls) > 1:
            structural.append(
                f"{len(urls)} pages share one description "
                f"({', '.join(sorted(urls))}): {desc[:60]!r}"
            )

    for c in sorted(content):
        print(f"content: {c}")
    for s in sorted(structural):
        print(f"structural: {s}", file=sys.stderr)

    print(f"\nseo_check: {checked} indexable pages, "
          f"{len(structural)} structural, {len(content)} content")

    if structural:
        print("structural faults block the deploy — one config or template edit "
              "fixes each of these.", file=sys.stderr)
    if content and not args.strict:
        print("content issues are reported only; run with --strict to fail on them.")

    if structural or (args.strict and content):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
