---
title: "DeepSeek V4.1 Flash 1017: new model, same API name"
date: 2026-10-18
summary: "On October 17 DeepSeek published DeepSeek-V4.1-Flash-1017 and called it a minor update to the V4.1 Flash that shipped on September 10. The same work now…"
---

## DeepSeek shipped V4.1 Flash 1017 and opened its search API

On October 17 DeepSeek published DeepSeek-V4.1-Flash-1017 and called it a minor update to the V4.1 Flash that shipped on September 10. The same work now finishes in less time and fewer output tokens. The API name and the price stay where they were. Calls to `deepseek-flash` land on the new model, and the older names `deepseek-v4-flash` and `deepseek-v4-flash-vision-exp` are retired and rerouted to it. [DeepSeek change log](https://api-docs.deepseek.com/updates)

A million tokens of cache-hit input costs $0.003 off-peak and $0.006 at peak. Cache-miss input costs $0.15 and $0.30, and output costs $0.60 and $1.20. Context runs to one million tokens with up to 384K of output, and the model takes images. The same day DeepSeek opened Search and Fetch APIs on its in-house search engine, priced at $0.75 per 1,000 successful requests. [Search & Fetch guide](https://api-docs.deepseek.com/guides/search/)

The benchmark numbers are DeepSeek's own, with Terminal-Bench run through the Claude Code harness and DeepSWE through Mini-SWE-V2. Terminal-Bench 4.0 goes from 31.2 to 42.3, DeepSWE v1.1 from 74.2 to 77.0, and HLE sits at 42.6 without tools. MIT-licensed weights went up on Hugging Face the same day. Repository files total around 510GB, and the release passed 600 points on Hacker News. [Hugging Face](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)

## Leave the code alone and next week it calls a different model

What changed for a builder is not the score. The name your code calls is the same, and the model behind it is not. The invoice and the price list look identical too. If your output shifted as though someone had edited the prompt, this is a candidate explanation.

Two numbers are worth re-measuring, and the first is your own eval. The published figures come from DeepSeek's harnesses, not yours: Terminal-Bench through Claude Code, DeepSWE through Mini-SWE-V2. The second is the cache line. A cache hit costs $0.003 per million input tokens and a miss costs $0.15, a fiftyfold gap for the same tokens, so an agent that keeps its system prompt and tool schemas stable at the front of the context pays a different bill for identical work.

If self-hosting was on your list, check the size before the licence. The weights are MIT, so commercial use carries no restriction. Picking up the 8-bit or FP8 build does not help either, because the repository runs to around 510GB. This is not a laptop model. Where a provider exposes a dated model ID, that path is how you hold the version steady.

Search and Fetch is priced to replace a search vendor. At $0.75 per 1,000 requests, compare it against what you pay today. Index coverage and Korean-language quality are for you to test, and no public evaluation exists yet.

Every performance figure here is vendor-reported and nobody has reproduced it independently. The next update can arrive the way this one did, with the API name and the price untouched.

## The rest of today's news

- **OpenCode breach exposes stored API keys**: OpenCode said on October 17 that unauthorised access to a legacy system exposed provider keys stored by 1.4% of Console users, including OpenAI, Anthropic and Google keys, and users report unexpected charges on connected accounts. [Blockonomi](https://blockonomi.com/opencode-security-breach-exposes-api-keys-of-1-4-of-console-users/)
- **Replit makes OpenAI its default**: Amjad Masad said at TechCrunch Disrupt that the platform no longer works with Anthropic, making ChatGPT the default for Replit Agent while Claude stays available as an option. [TechCrunch](https://techcrunch.com/2026/10/17/replit-is-no-longer-working-with-anthropic-ceo-says/)
- **Vercel AI Gateway adds V4.1 Flash 1017**: the model reached the gateway the same day. [Vercel Changelog](https://vercel.com/changelog/deepseek-v4-1-flash-1017-now-available-on-ai-gateway)