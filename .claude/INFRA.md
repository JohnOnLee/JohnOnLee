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
