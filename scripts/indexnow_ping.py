#!/usr/bin/env python3
"""Tell IndexNow-participating search engines which URLs just changed.

Bing's 2026-08-21 site scan flagged a missing IndexNow setup as its only
high-severity item. Bing already ranks this site's content on page one, so the
gap there is how fast it hears about a change, not whether it likes the page.
The daily brief is the case that needs it: news-shaped content that is worth
little a week after it lands.

Google does not participate in IndexNow and this script does not help it. That
is not an oversight — Google's own bottleneck (0 impressions, 3 pages indexed
as of 2026-08-21) is external authority, which no ping protocol addresses.
Do not extend this expecting Google to answer.

Reads <loc>/<lastmod> out of ./public/sitemap.xml rather than walking content/,
so it submits exactly what the build published — the same discipline
seo_check.py follows. Runs AFTER the deploy step: a ping that lands before the
new HTML is live just sends crawlers to the previous version.

By default it submits only URLs whose lastmod is today (KST, matching the
site's timeZone) — the new brief plus whatever section pages it touched, about
a dozen URLs. IndexNow asks submitters to send what changed, not the whole
site; --all exists for the one-time seed submission when adopting the protocol
or after the key rotates.

Usage:
    python3 scripts/indexnow_ping.py [--all] [--public public]
    DRY_RUN=1 python3 scripts/indexnow_ping.py --all    # print, send nothing
"""
import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone

HOST = "john.onlee.io"
SITE = f"https://{HOST}"
KST = timezone(timedelta(hours=9))

# The shared endpoint forwards one submission to every participating engine
# (Bing, Naver, Yandex, Seznam), so this stays a single request even as that
# list changes.
ENDPOINT = "https://api.indexnow.org/indexnow"

# Not a secret: IndexNow proves ownership by having the submitter serve the key
# at a public URL, so the value ships in static/ and in every submission. It is
# the pairing that authenticates, not the secrecy. Rotating means adding the new
# file, updating both constants, and re-running with --all.
KEY = "b68c5558711ff4e1e34a1d80f9bfbfaf"
KEY_LOCATION = f"{SITE}/{KEY}.txt"

# IndexNow caps a submission at 10,000 URLs. The site is an order of magnitude
# under that, so this only matters if the sitemap ever explodes.
MAX_URLS = 10000

URL_ENTRY = re.compile(
    r"<url>\s*<loc>(?P<loc>[^<]+)</loc>(?:\s*<lastmod>(?P<lastmod>[^<]+)</lastmod>)?",
    re.DOTALL,
)


def changed_urls(sitemap_path: str, today: str, everything: bool):
    """URLs from the built sitemap, filtered to today's lastmod unless --all."""
    with open(sitemap_path, encoding="utf-8") as f:
        sitemap = f.read()

    urls = []
    for m in URL_ENTRY.finditer(sitemap):
        loc = m.group("loc").strip()
        if not loc.startswith(SITE):
            # IndexNow rejects a whole submission if any URL is off-host.
            continue
        if everything:
            urls.append(loc)
        elif (m.group("lastmod") or "").startswith(today):
            urls.append(loc)
    return urls


def submit(urls) -> int:
    payload = {
        "host": HOST,
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls,
    }
    req = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json; charset=utf-8",
                 "User-Agent": f"johnonlee-indexnow (+{SITE})"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req) as resp:
            # 200 accepted; 202 means the key is still being validated, which is
            # normal on the first submission after adding the key file.
            print(f"IndexNow accepted {len(urls)} URL(s) (HTTP {resp.status})")
            return 0
    except urllib.error.HTTPError as e:
        # 403 = key file missing or mismatched, 422 = a URL is off-host,
        # 429 = submitting too often. None of these should fail the deploy: the
        # site is already live by this point and a missed ping costs latency,
        # not correctness.
        print(f"IndexNow refused the submission: HTTP {e.code} {e.reason}",
              file=sys.stderr)
        print(e.read().decode(errors="replace")[:500], file=sys.stderr)
        return 0
    except urllib.error.URLError as e:
        print(f"IndexNow unreachable: {e.reason}", file=sys.stderr)
        return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true",
                    help="submit every sitemap URL, not just today's changes")
    ap.add_argument("--public", default="public",
                    help="path to the built site (default: public)")
    args = ap.parse_args()

    sitemap_path = os.path.join(args.public, "sitemap.xml")
    if not os.path.exists(sitemap_path):
        print(f"No sitemap at {sitemap_path}; run hugo first", file=sys.stderr)
        return 1

    today = datetime.now(KST).strftime("%Y-%m-%d")
    urls = changed_urls(sitemap_path, today, args.all)

    if not urls:
        print(f"Nothing with a {today} lastmod; nothing to submit.")
        return 0

    if len(urls) > MAX_URLS:
        print(f"Submitting the first {MAX_URLS} of {len(urls)} URLs")
        urls = urls[:MAX_URLS]

    if os.environ.get("DRY_RUN"):
        for u in urls:
            print(f"DRY RUN would submit: {u}")
        print(f"DRY RUN total: {len(urls)} URL(s)")
        return 0

    return submit(urls)


if __name__ == "__main__":
    sys.exit(main())
