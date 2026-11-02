---
title: "gemini-2.5-pro retires Dec 1"
date: 2026-11-03
summary: "From December 1, Google will reroute Gemini 2.5 Pro and 2.5 Flash API requests to other Flash models and bill the rates of the models they land on."
---

## gemini-2.5-pro moves to gemini-3.8-flash: pick your model before Google does

From December 1, Google will reroute Gemini 2.5 Pro and 2.5 Flash API requests to other Flash models and bill the rates of the models they land on.

Requests to `gemini-2.5-pro` go to `gemini-3.8-flash`; requests to `gemini-2.5-flash` go to `gemini-3.5-flash-lite`. Your code can stay untouched, but the model answering your users changes anyway. Both old models have left Google AI Studio's picker, and the API is open only to accounts that used them before. The [deprecations page](https://ai.google.dev/gemini-api/docs/deprecations) calls its dates the earliest possible ones. These two entries still name December 1 for shutdown and same-day rerouting, and Google announced no separate migration window.

The price moves twice. Gemini 3.8 Flash costs $0.75 per million input tokens and $3.75 per million output tokens through December 31, then $1.50 and $7.50 from January 1, 2027; Google calls the year-end rate introductory in its [3.8 Flash guide](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.8). Gemini 2.5 Pro charged $1.25 and $10.00 for prompts up to 200k tokens. On those published [prices](https://ai.google.dev/gemini-api/docs/pricing), December input runs at 60% of the Pro rate and output at 37.5%. In January input costs 20% more than 2.5 Pro and output 25% less. The comparison is arithmetic, and a December bill is a bad basis for setting margins.

Leaving the model ID alone means a different model answers your customers from December 1. Decide which model the product should use, set that ID yourself, and finish the parameter work. Google's breaking changes cover function calling and `thought_signature` validation. `thinking_level` replaces `thinking_budget`, and some sampling parameters and prefilled model turns are removed ([release notes](https://ai.google.dev/gemini-api/docs/changelog)). The default thinking level on 3.8 Flash is `medium`, so swapping the ID while sending the old settings does not finish the migration. Google asks developers to review the migration guides before December 1. Leave it to the automatic reroute, and Google picks both the model that serves your customers and the day your bill changes.

## The rest of today's news

- **Anthropic message threads enter public beta**: median time to first token drops about 35% on 500k to 1M token requests while token usage and prices stay the same, but a thread expires five minutes after its last request and the model cannot change mid-thread. [Anthropic](https://claude.com/resources/articles/message-threads)
- **GitHub Actions blocks pull_request_target by default**: public repositories need an explicit policy allowance from December 2, so check the affected runs in Insights before the November 9 and 16 brownouts. [GitHub Changelog](https://github.blog/changelog/2026-11-02-pull_request_target-blocked-by-default-december-2/)
- **New York Times and other publishers sue Brave**: the new suit alleges scraping, sales to AI firms and paywall bypass; the claims are unproven, and a product built on news content should check whether its ingestion is licensed. [Reuters](https://www.reuters.com/legal/litigation/new-york-times-sues-maker-brave-web-browser-over-copyrights-2026-11-02/)