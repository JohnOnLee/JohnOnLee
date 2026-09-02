---
title: "Fable 5.1: cache-read −75% rewrites agent economics"
date: 2026-09-02
summary: "Anthropic shipped Claude Fable 5.1 with cache-read pricing down 75% — agent products that reuse context get ~45% cheaper, so cost models deserve a redesign."
---

## Anthropic cut cache-read prices by 75%
- **Fable 5.1 is out — the most advanced coding & knowledge model yet**: Fable 5.1 is generally available, while Mythos 5.1 is reserved for trusted-access programs in cybersecurity and life sciences — the same model with different safeguards. Anthropic cut cache-read pricing by 75%, making typical workloads roughly 25% cheaper than Fable 5 (up to ~45% for agentic work), and introduced Enterprise Frontier Safeguards for zero data retention. [Anthropic](https://www.anthropic.com/claude-fable-and-mythos-5-1)

## Why your agent product's cost model needs a rewrite
- **The assumption that repeated context is expensive just broke**: A 75% cut to cache-read pricing directly favors long-running agents and agent teams that keep reusing the same context. With up to ~45% cheaper load for identical work, any cost model built without aggressive context caching is now overstating the bill. It's time to design with context reuse as a default, not an optimization.

## Try this now: cache-friendly agent architecture
- **Run an experiment in cache-first agent design**: Separate long system prompts, tool definitions, and conversation history into cacheable units and optimize for hit rate. If a cache-friendly structure is up to 45% cheaper for the same output, token-sensitive indie products can reset their pricing entirely.

## Still open: trusted-access boundaries and retention reality
- **The gating criteria for Mythos 5.1 are not public**: Shipping the same model with different safeguard levels is a new approach, but which use cases qualify for trusted access — and where feature parity with the general release ends — is unspecified. The enterprise zero-retention option (EFS) also has yet to be validated in real audit and compliance workflows.

## The rest of today's news
- **World Labs unveiled Atlas, an omni world model for spatial intelligence**: An autoregressive diffusion transformer handling text, images, video, and 3D natively — camera-controlled 1440p generation, real-scene reconstruction, and robot Real-to-Sim workflows. Early access applications are open. [World Labs](https://www.worldlabs.ai/blog/atlas)
- **Apple's CEO transition — John Ternus takes over with AI as his first test**: With Tim Cook as executive chairman and Ternus as CEO, a rebuilt Siri and Apple's first foldable iPhone are due September 9. Apple's bet on licensing Google Gemini (~$1B/year) faces a public verdict. [Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/john-ternus-becomes-apple-ceo-111908957.html)
- **OpenAI's Astra is the first model to cross the 'Critical' cyber threshold**: A perfect ExploitBench score and two autonomously found and exploited zero-days in modified tests. OpenAI says a more strongly guarded version ships "soon." [OpenAI](https://openai.com/index/path-to-astra/) · [CyberPress](https://cyberpress.org/openai-warns-astra-ai-could-develop-zero-day-exploits/)