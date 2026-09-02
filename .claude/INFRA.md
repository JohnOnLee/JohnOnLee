# Infrastructure notes — onlee.io

Reference for future changes. Last updated: 2026-08-09.

## Topology

| Piece | What | Where |
|---|---|---|
| DNS | Cloudflare (zone `onlee.io`) | dash.cloudflare.com |
| Email | iCloud custom domain — MX `mx01/mx02.mail.icloud.com`, SPF `include:icloud.com`, `apple-domain` TXT | **Never touch these records** |
| Web (this site) | `john.onlee.io` → GitHub Pages (this repo, Actions deploy on push to main), Cloudflare-proxied, Always Use HTTPS ON | `.github/workflows/hugo.yaml` |
| Apex `onlee.io` | Dummy `A @ 192.0.2.1` (proxied) + Redirect Rule `301 → https://john.onlee.io<path>` | Cloudflare DNS + Rules → Redirect Rules |

## Why the apex redirect exists

Added 2026-08-02 for Google AdSense site verification: AdSense registers the
root domain (`onlee.io`) and crawls it, but the site lives on the `john`
subdomain. The dummy A record makes Cloudflare answer for the apex; the
redirect rule sends everything to `john.onlee.io`. Email is unaffected —
mail routing uses only the MX records above.

## If you later host a real site at the apex

1. Delete the Redirect Rule (`onlee.io → john.onlee.io`).
2. Replace the dummy `A @ 192.0.2.1` with the real hosting target.

That's all. The AdSense site registration (root-domain based) survives this;
ads only appear where the ad code is included.

## Adding another subdomain site later

Just add its DNS record. The redirect rule matches `hostname equals onlee.io`
only, so subdomains are untouched.

## Search / ads wiring in this repo

- Search-console verification tags: `hugo.yaml` → `params.analytics.*.SiteVerificationTag`
  (Google Search Console itself is a domain property verified via DNS TXT).
- Bing Webmaster Tools needs no tag: it is verified through its Google Search
  Console connection. Only add `params.analytics.bing` if that link is removed.
- Sitemap: `layouts/sitemapindex.xml` overrides Hugo's split index and renders
  one flat `<urlset>` at `/sitemap.xml`. Hugo still writes `/ko/sitemap.xml`
  and `/en/sitemap.xml`, but nothing points at them — they are orphans, and the
  `/ko/` one lists root URLs that sit outside its own directory, which the
  sitemaps.org path rule disallows. Never submit those two to a search console.
- `scripts/seo_check.py` runs in the deploy workflow and fails the build on
  structural faults. `--source` checks front matter with no Hugo build; the
  brief generator runs that before committing.
- AdSense loader: `layouts/_partials/extend_head.html`, gated to `/guides/`
  pages and the `params.adsenseClient` value in `hugo.yaml`.
- `ads.txt` (after AdSense approval): put it in `static/ads.txt`. Crawlers
  reaching `onlee.io/ads.txt` follow the 301 to `john.onlee.io/ads.txt`,
  which the spec permits.
- IndexNow: `scripts/indexnow_ping.py` submits the day's changed URLs after
  the deploy step. The key lives at `static/<key>.txt` and is repeated in the
  script — not a secret, since the protocol authenticates by having the
  submitter serve that key at a public URL. Reaches Bing, Naver, Yandex and
  Seznam through the shared endpoint. **Google does not participate**, so
  nothing here moves the Google numbers below.
- Briefs are indexable like everything else. The 2026-09-02 noindex cascade
  lasted one commit (`f39d01c`, removed the same day — see that reading). If a
  section ever has to leave the index, that commit is the working recipe:
  `cascade.params.robotsNoIndex` plus `cascade.sitemap.disable` in the
  section `_index`, honored by PaperMod and `layouts/sitemapindex.xml`; RSS,
  llms.txt and the home page do not depend on either.

## SEO baseline — 2026-08-09

Measured the day the SEO pass shipped (commit `91b093d`), so a later reading
has something to compare against. Site first published 2026-05-31; the Google
Search Console property was only added 2026-08-05, which is why its history
starts there.

| Metric | Google | Bing |
|---|---|---|
| URLs discovered | 59 | 164 |
| Indexed | 3 | — |
| Impressions | 0 | 9 |
| Sitemap: pages discovered | not recorded | 0 |

Site had 192 indexable pages at the time. Both consoles had the new flat
sitemap submitted on 2026-08-09, after the deploy.

Google's 52 "crawled - currently not indexed" broke down as 11 RSS feeds,
5 dead tag URLs from the pre-2026-08-05 taxonomy, 1 paginator, and 37 real
pages. Last-crawled dates: 34 in June, 13 in July, 5 in August — Google
crawled the site in June and went quiet. The 2 reported 404s were
`/favicon.ico` (fixed in that commit) and `/en/brief/2026-06-10/` (a brief
deliberately removed in `e1a12f1`, so the 404 is correct).

### What the reading means

Bing ranked the same content on page one — PaperMod-related queries at
positions 4–9, and a question about Opus pricing at 3. (Queries paraphrased:
they are other people's searches, and this file is public.)
So the content is indexable and rankable, and the gap is discovery on
Google's side, not quality. Do not reopen the theory that Google suppresses
the aggregated briefs: briefs are 72% of the site but only 42% of the
not-indexed set, and original blog posts were hit harder.
Reopened on 2026-09-02; see that reading.

### When to look

- **2–3 days** — sitemap processing. Bing's "pages discovered" should move
  off 0 toward ~192. **If it does not, the sitemap path-scope diagnosis was
  wrong** and the cause is somewhere else.
- **1–2 weeks** — recrawl. Last-crawled dates on the not-indexed set should
  start moving off June.
- **3–4 weeks** — indexing decisions. Whether the indexed count leaves 3 is
  the real outcome measure.

Impressions staying near zero in that window is not yet a signal; volume
lags indexing.

## SEO reading — 2026-08-21

Day 12 against the baseline above. Read from the Google Search Console
Coverage and Coverage-Drilldown exports and the Bing SEO summary, all dated
2026-08-21; GSC's own data runs through 08-17, so the latest column is that.

| Metric | 2026-08-09 | 2026-08-21 |
|---|---|---|
| Indexed (Google) | 3 | **3** |
| Not indexed (Google) | 56 | 212 |
| Impressions (Google) | 0 | **0** |
| Indexable pages on the site | 192 | 226 |

The 212 splits into 148 "Discovered – currently not indexed", 60 "Crawled –
currently not indexed", 2 404s, 1 noindex, 1 redirect.

### The two checkpoints above, answered

**Recrawl (1–2 weeks): did not happen.** The not-indexed set's last-crawled
months are 34 June / 13 July — identical counts to 08-09, not merely similar.
Only August moved, 5 → 13, and every new entry is a page first published after
the baseline. Google recrawled none of the 47 URLs it had already declined.

**Indexing decisions (3–4 weeks): no movement.** Indexed has been exactly 3
since the property's first data point on 08-05. The "Crawled – currently not
indexed" bucket now carries **Validation: Failed** — Google re-evaluated on
request and declined again.

### What the reading means

The 08-09 diagnosis was right about the plumbing and the plumbing is now done.
Re-verified live against Googlebot on 08-21: 200s, `index, follow`,
self-canonical, bidirectional hreflang with x-default, JSON-LD, unique
titles and descriptions, a sitemap with real per-page lastmod and no dead
URLs, TTFB 0.1–0.4s, apex redirect in one hop. Neither console reports a
single structural fault. There is no configuration fix left to make.

What replaced it is a crawl-and-authority ceiling. 148 URLs — effectively all
of them briefs — were discovered and then never fetched at all, which is a
different failure from being fetched and rejected. Bing's site scan the same
day names the cause in its own words, and it is the only moderate-or-worse
finding it has besides the missing IndexNow setup: *the site lacks inbound
links from high-quality domains.*

The brief-suppression theory stays closed, and the new numbers argue against
it harder than the old ones: briefs are 71% of the sitemap but 32% of the
not-indexed set, while blog and guides are 20% of the sitemap and 28% of it.
Reopened on 2026-09-02; see that reading.

One pattern worth recording without a verdict: 15 of the 17 not-indexed
blog/guide pages are `/en/`, only 2 are Korean, and **all 15 have a Dev.to
twin** — 19 posts are live there, every one canonical'd back to a
john.onlee.io URL that returns 200 in zero redirects (verified via the public
Dev.to API on 08-21). Korean posts are never cross-posted, since
`devto_crosspost.py` globs `index.en.md` only. That is a clean correlation and
a plausible aggravator — a low-authority copy of content Google already has
from a domain it trusts — but it is not established. With only 3 pages
indexed site-wide there is no control group of un-cross-posted English pages
to compare against. Do not act on it as a cause without that evidence.

### When to look

- **2–3 days** — IndexNow. Bing/Naver crawl latency on a new brief should
  drop to hours. The protocol itself is confirmed working, so a flat reading
  means the engines are ignoring the hint, not that the wiring is broken:
  on 2026-08-21 the post-deploy ping was accepted for that day's 14 URLs
  (HTTP 202, key pending) and the `--all` seed for all 232 (HTTP 200, key
  validated). **If the wiring ever does break it will be silent** — the step
  carries `continue-on-error`, so read the deploy log, not the build status.
- **2–4 weeks** — whether manually requesting indexing in GSC moves anything.
  The fair test is the 26 original pages Google had discovered but never
  fetched; the 16 it fetched and declined are not, since it has already said
  no to those twice. Of the 26, **10 were submitted by hand on 2026-08-21**
  (8 Korean, 2 English — Korean first, since those have no Dev.to twin
  competing for the same content). The remaining 16 follow at the ~10/day
  quota. If a meaningful share of the 10 leaves the not-indexed set while the
  never-submitted remainder does not, manual submission is worth continuing;
  if neither moves, it is not, and the authority ceiling is the whole story.
- **The outcome measure is unchanged and still unmet:** indexed leaving 3.
  Nothing in this pass targets it, because nothing in this repo can. That one
  moves when other domains link here.

## SEO reading — 2026-09-02

Day 24 against the baseline. Read from the Coverage *Validation* export for
"Crawled – currently not indexed" (dated 2026-09-02) and the AdSense decision
John relayed the same day. The full Coverage chart was not exported, so the
indexed count is unread; a Google `site:` query was blocked by bot detection.

| Metric | 2026-08-21 | 2026-09-02 |
|---|---|---|
| "Crawled – currently not indexed" URLs | 60 | 72 |
| of which re-fetched since 08-21 and declined again | — | 22 |
| Left the bucket | — | 0 |
| AdSense | under review | **rejected: "Low value content"** |

### What moved

The validation run cannot pass and its verdict carries no information: 11 RSS
feeds, 5 tag pages and a paginator sit in the bucket and are not indexable
content. Do not start another validation for this bucket; read the Coverage
chart instead.

The 08-21 manual-submission test has half its answer. Eight Korean originals
entered the bucket with last-crawled 2026-08-21 — the submission date, and
none of them was in the bucket before — so they are read as the 8 Korean
submissions (the submitted list was never recorded, so this is inference).
All eight were fetched the same day and declined. Manual submission buys a
fetch, not an index decision. Google also recrawled 10 English pages on its
own between 08-22 and 08-29 and declined every one of them again.

### The brief theory, reopened

The 08-09 and 08-21 readings closed the theory that the aggregated briefs
drag the site down, on the proportions inside the crawled bucket. On
2026-09-02 AdSense rejected the site for "Low value content" (minimum content
requirements, thin content). That is a second, independent, site-level
quality verdict from Google on a site whose pages are 79% agent-curated
briefs: 186 of 236 content pages, against 32 blog and 18 guide pages, about
25 unique pieces once translations are paired. The rejection does not prove
the briefs are the cause — a three-month-old domain with 25 originals and no
inbound links can draw the same verdict — but the proportions argument no
longer closes the question.

Live re-verification the same day found nothing technical: 200s,
`index, follow`, self-canonical, hreflang with x-default, JSON-LD, a Googlebot
UA served through Cloudflare without a challenge, privacy and about pages in
both languages, the AdSense meta site-wide. All 24 Dev.to posts still
canonical to john.onlee.io, and Korean pages with no Dev.to twin were declined
too, so the twin stays unacted.

### The experiment, and what overtook it

`f39d01c` cascaded `robotsNoIndex: true` and `sitemap.disable: true` over
`content/brief/` so the ~50 original pages would be the whole corpus Google
sees while the digests stayed on the site. It was live for about half an hour
(verified: sitemap 264 → 76 URLs, `seo_check` 0 structural).

The same evening John replaced the digests outright (`12e3883`, `98c5524`,
committed as Coda Lee): the 92 daily briefs from 2026-05-29 to 08-31 were
deleted in both languages — 184 URLs now return 404 — and 09-01 and 09-02
were rewritten as one analysis per event: a headline, four lenses (the facts,
what it means for an indie builder, what to build next, open risks) and the
rest of the day as one-line capsules, about 400 words per language. That made
the cascade counter-productive — the only pages it still hid were the two new
analyses and the section page — so the commit recording this removes it.
Briefs are back to the site default: indexable, in the sitemap.

What the reading now tests: with the digests gone and the brief section
carrying analysis, does Indexed leave 3? A yes says the digests were diluting
the site; a no with the corpus this clean says the ceiling is authority
alone. There is no cascade to revert any more; the deleted digests live in
git history before `12e3883` if they are ever wanted back.

### When to look

- **AdSense** — do not request a re-review yet. A reviewer now sees analyses
  instead of digests, but two pieces is not a corpus; re-apply once the
  event-led briefs have a few weeks of volume behind them and the originals
  have grown.
- **4–6 weeks (early-to-mid October)** — pull the full Coverage export. The
  report will show a 404 spike — up to 184 deleted brief URLs — which is
  correct and needs no action; the 148 "Discovered – currently not indexed"
  entries drain as Google fetches them and gets 404. The outcome measure is
  unchanged: Indexed leaving 3.
