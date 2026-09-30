---
title: "Gemini 4 Argon is out, but nobody can use it"
date: 2026-10-01
summary: "On September 30, Google announced Gemini 4 Argon, its new frontier model. It lands in place of the Gemini 3.5 Pro that Google teased in June, and it marks the…"
---

## Google is back at the frontier after months away. The door opens only for cyber defenders

On September 30, Google announced Gemini 4 Argon, its new frontier model. It lands in place of the Gemini 3.5 Pro that Google teased in June, and it marks the company's return to the front line after a summer spent shipping small Flash models. Argon is not generally available. It is going out first to a small set of trusted cyber defenders in the Fairwind Program, then to paid API customers and Google AI Ultra subscribers. Google has not promised a date. [Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/) · [Ars Technica](https://arstechnica.com/ai/2026/09/google-announces-gemini-4-argon-ai-model-but-you-cant-use-it-yet/)

Argon raises the output token limit to 1 million, up from 64K. It scores 77.9% on DeepSWE v1.1, a benchmark for real long-horizon software engineering, ahead of GPT-6 Astra, Fable 5.1, and Opus 5.5. It takes first place on the Vals Index, which weights economic impact across finance, coding, legal, and tax work. Pricing is $2 per million input tokens and $10 per million output tokens during the introductory period, rising to $4 and $20 afterward, with cached input tokens at 95% off. [Ars Technica](https://arstechnica.com/ai/2026/09/google-announces-gemini-4-argon-ai-model-but-you-cant-use-it-yet/)

Google is already running it internally. Argon analyzed fleet-wide profiling telemetry and freed up 300 TiB of memory across Google's data centers. It is working on C/C++ to Rust migrations of core libraries and more than 800,000 lines of the Fuchsia Zircon kernel. On a quantum optimization problem, it produced a result using 40% fewer resources than the best published baseline, in minutes. On security, Wiz used Argon to find a critical vulnerability in healthcare software used by hospitals worldwide, a flaw earlier frontier models missed. [Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/)

## A closed door is time to design

For indie builders there is nothing to do today. The API is not open. But the numbers that matter when it opens are worth working through now. A 1 million output limit at an introductory $2 in and $10 out changes the cost math for agent products that want one long run instead of many short calls. If your pipeline is currently split into repeated calls, price out what a single long call would cost and how much latency it would save. And plan for the price doubling once the introductory period ends. [Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/)

What is still unresolved matters too. Google has not committed to a date for wider access, and most of the benchmarks it published are its own. Until independent reproductions show up, treat the rankings as provisional. The prompt injection robustness and alignment monitoring claims are also just that, claims. Keep them on the list to verify yourself once the API actually opens.

## The rest of today's news

- **FTC opens a sweeping probe into Anthropic and OpenAI**: The first official US enforcement action on rogue AI agents. The FTC plans to compel information and executive testimony from Anthropic, OpenAI, and the research group Metr. [The Guardian](https://www.theguardian.com/us-news/2026/sep/30/ftc-investigation-anthropic-openai)
- **OpenAI details a large-scale distillation campaign by Moonshot**: OpenAI says it disrupted a coordinated effort to extract protected reasoning, peaking at 16,000 requests in July, and traced a core cluster to Moonshot AI. [The Verge](https://www.theverge.com/ai-artificial-intelligence/1002854/openai-claims-moonshot-extracted-its-data-to-train-ai-models)
- **Reddit ends RSS support and restricts Old Reddit**: Starting November 13, Reddit drops RSS feeds and limits Old Reddit to accounts that used it within the last six months. The company cites scraping and automated abuse. [The Verge](https://www.theverge.com/tech/1002788/old-reddit-ai-scraping)
- **ElevenLabs doubles its valuation to $22B**: A $300 million tender offer let employees sell stock at twice the $11 billion valuation from February. [TechCrunch](https://techcrunch.com/2026/09/30/ai-voice-startup-elevenlabs-doubles-valuation-to-22b/)
- **Flow Engineering raises $50M at a $750M valuation**: The hardware design AI startup's Series B was co-led by Valar and Atreides, with Sequoia participating. [TechCrunch](https://techcrunch.com/2026/09/30/valor-atreides-and-sequoia-back-ai-startup-flow-engineering-at-750m-valuation/)
- **Restate raises a $20M Series A**: The durable execution company wants durability to be a building block for backends and agent loops, not a heavy workflow layer. Singular led the round. [Restate](https://restate.dev/blog/announcing-series-a/)
- **Anthropic's IPO filing shows a $42B net loss for 2025**: Revenue grew 4.6-fold to nearly $4.6 billion, while the prospectus also lays out $518 billion in planned cloud and computing spending. [Daring Fireball](https://daringfireball.net/linked/2026/09/30/reuters-anthropic-ipo-prospectus)