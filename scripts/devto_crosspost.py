#!/usr/bin/env python3
"""Cross-post new English posts to Dev.to as drafts.

Scans content/blog and content/guides for index.en.md files dated within the
last 14 days (KST, matching the site's timeZone). Posts whose canonical URL is
not yet on the Dev.to account are uploaded as DRAFTS with canonical_url set to
john.onlee.io, so each one still gets a human review before publishing.

Env: DEVTO_API_KEY (required unless DRY_RUN=1)
"""
import json
import os
import re
import sys
import time
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

SITE = "https://john.onlee.io"
KST = timezone(timedelta(hours=9))
LOOKBACK_DAYS = 14
API = "https://dev.to/api"

# Site tags use our fixed vocabulary; Dev.to tags must be established ones
# (lowercase, no hyphens) to reach their feeds. Cap is 4 per article.
DEVTO_TAG_MAP = {
    "coding-agents": ["ai", "programming"],
    "ai-memory": ["ai", "programming"],
    "ai-economics": ["ai", "programming"],
    "ai-business": ["ai", "startup"],
    "writing-with-ai": ["ai", "writing"],
    "site-building": ["webdev", "hugo"],
}


def parse_front_matter(text: str) -> dict:
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    if not m:
        return {}
    fields = {}
    for key in ("title", "summary"):
        km = re.search(rf'^{key}:\s*"(.*)"\s*$', m.group(1), re.MULTILINE)
        if km:
            fields[key] = km.group(1)
    dm = re.search(r"^date:\s*(\d{4}-\d{2}-\d{2})", m.group(1), re.MULTILINE)
    if dm:
        fields["date"] = dm.group(1)
    tm = re.search(r"^tags:\s*\[(.*)\]", m.group(1), re.MULTILINE)
    if tm:
        fields["tags"] = [t.strip().strip('"') for t in tm.group(1).split(",") if t.strip()]
    fields["body"] = m.group(2).strip()
    return fields


def devto_tags(site_tags):
    out = []
    for t in site_tags:
        for dt in DEVTO_TAG_MAP.get(t, []):
            if dt not in out:
                out.append(dt)
    return (out or ["ai"])[:4]


def absolutize_links(body: str) -> str:
    # Site-relative markdown links become absolute so they work on Dev.to.
    return re.sub(r"\]\(/", f"]({SITE}/", body)


def candidates(today: date):
    for section in ("blog", "guides"):
        for f in sorted(Path("content").glob(f"{section}/*/index.en.md")):
            fm = parse_front_matter(f.read_text(encoding="utf-8"))
            if not fm.get("title") or not fm.get("date"):
                continue
            d = datetime.strptime(fm["date"], "%Y-%m-%d").date()
            if today - timedelta(days=LOOKBACK_DAYS) <= d <= today:
                slug = f.parent.name
                yield {
                    "title": fm["title"],
                    "description": fm.get("summary", "")[:150],
                    "canonical_url": f"{SITE}/en/{section}/{slug}/",
                    "body_markdown": absolutize_links(fm["body"]),
                    "tags": devto_tags(fm.get("tags", [])),
                }


def api_request(path: str, key: str, payload=None):
    req = urllib.request.Request(
        f"{API}{path}",
        data=json.dumps(payload).encode() if payload else None,
        headers={"api-key": key, "Content-Type": "application/json",
                 "Accept": "application/vnd.forem.api-v1+json",
                 "User-Agent": "johnonlee-crosspost (+https://john.onlee.io)"},
        method="POST" if payload else "GET",
    )
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)


def main() -> int:
    today = datetime.now(KST).date()
    posts = list(candidates(today))
    if not posts:
        print("No posts in the lookback window; nothing to do.")
        return 0

    if os.environ.get("DRY_RUN"):
        for p in posts:
            print(f"DRY RUN candidate: {p['title']} -> {p['canonical_url']}")
        return 0

    key = os.environ.get("DEVTO_API_KEY")
    if not key:
        print("DEVTO_API_KEY is not set", file=sys.stderr)
        return 1

    existing = set()
    for page in range(1, 6):
        batch = api_request(f"/articles/me/all?per_page=100&page={page}", key)
        if not batch:
            break
        for a in batch:
            existing.add(a.get("canonical_url") or a.get("url"))

    created = 0
    for p in posts:
        if p["canonical_url"] in existing:
            print(f"Already on Dev.to, skipping: {p['canonical_url']}")
            continue
        api_request("/articles", key, {"article": {**p, "published": False}})
        print(f"Draft created: {p['title']}")
        created += 1
        time.sleep(1)

    print(f"Done. {created} draft(s) created.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
