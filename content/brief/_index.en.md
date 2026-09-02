---
title: "AI Radar"
description: "Daily signals for builders — the shifts in AI that actually matter, not just the news."
# 2026-09-02 experiment: briefs stay on the site, in RSS and on the home page,
# but leave every search engine's index and the sitemap. Google declined the
# site twice (index selection, AdSense "Low value content") with briefs at 79%
# of pages; this tests whether the ~50 original pages index once briefs are
# out of the corpus. See .claude/INFRA.md, "SEO reading — 2026-09-02".
# The section page and its paginated lists inherit it. PaperMod reads
# robotsNoIndex; layouts/sitemapindex.xml honors sitemap.disable.
cascade:
  params:
    robotsNoIndex: true
  sitemap:
    disable: true
---
