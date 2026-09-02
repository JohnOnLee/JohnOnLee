---
title: "AI 레이더"
description: "매일 쏟아지는 AI 뉴스 중, 만드는 사람이 놓치지 말아야 할 변화와 신호를 골라 전합니다."
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
