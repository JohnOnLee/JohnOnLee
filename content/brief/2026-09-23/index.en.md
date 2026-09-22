---
title: "OpenAI and Anthropic cut API prices the same afternoon"
date: 2026-09-23
summary: "OpenAI and Anthropic cut API prices on September 22 within 90 minutes of each other. GPT-6 Sol is $2 and $10 per million tokens, Claude Opus 5.5 $4 and $20."
---

## GPT-6 Sol, GPT-6 Luna, and Claude Opus 5.5 halved the price of a task in one day

OpenAI and Anthropic cut API prices on September 22 within 90 minutes of each other. GPT-6 Sol is $2 and $10 per million tokens, Claude Opus 5.5 $4 and $20.

OpenAI's GPT-6 Sol and Luna land at half the current promotional price of the GPT-5.6 versions. Sol is $2 in and $10 out per million tokens. Luna is $0.10 and $0.50. The company says Sol halved its mistakes on an internal factuality evaluation. Luna matches GPT-5.6 Sol on performance, it claims, for about 1% of the cost. Cached input tokens take a 90% discount, and developers now set the cache breakpoints themselves. Copilot added both models to its picker. [OpenAI](https://openai.com/index/introducing-gpt-6-sol-and-luna/) · [TechCrunch](https://techcrunch.com/2026/09/22/openai-launches-gpt-6-sol-and-luna/) · [TNW](https://thenextweb.com/news/openai-gpt-6-sol-luna-api-price-cut) · [GitHub Changelog](https://github.blog/changelog/2026-09-22-openais-gpt-6-sol-and-gpt-6-luna-now-available/)

Anthropic moved 90 minutes earlier. Opus 5.5 matches Fable 5.1 on performance. It costs 40% less to run than Opus 5 and writes output more than 30% faster. The list price is $4 in and $20 out per million tokens, 20% below Opus 5. Cache reads dropped 60%, to $0.20 per million tokens. Anthropic says those reads account for the bulk of what agentic and coding work costs. Outside groups ran the pre-release evaluations, among them Frontier Design and METR. One tester finished a 680,000-line code migration in under a day. Anthropic calls it the first release since it asked the industry publicly to pace the frontier, and it raised five-hour usage limits for paid subscribers by 20%. [Anthropic](https://www.anthropic.com/news/claude-opus-5-5) · [ZDNET](https://www.zdnet.com/innovation/anthropic-claude-opus-5-5-fable-5-1-performance-costs-less/)

Open weights pushed the floor down on the same day. Xiaomi published MiMo-V2.6-Pro under MIT. It tops the open-weight class with a score of 46 on the Artificial Analysis intelligence index, and among the models that firm tracks it has the lowest cost per task, at $0.13. The architecture is mixture-of-experts: 42 billion active parameters out of 1.02 trillion total. The price is $0.435 in and $0.87 out per million tokens, available through OpenRouter, Xiaomi's own API, and its app. Training took under six days and cost $2.62 million. Xiaomi shipped the training code and 7,000 reinforcement-learning task environments with it. [TNW](https://thenextweb.com/news/xiaomi-mimo-v2-6-open-weight-model-anthropic-distillation) · [Hugging Face](https://huggingface.co/XiaomiMiMo)

## The cuts landed hardest where agents actually spend

All three announcements measure cost per task, not per token. OpenAI reports that Sol at maximum reasoning finished 33.2% of AutomationBench tasks at $0.27 each. Claude Opus 5 finished 26.9%, at 11.1 times the cost. Vendor numbers deserve doubt. Price your product off a token rate card, though, and the arithmetic comes out wrong. What matters on the invoice is the cost of finishing one request.

Caching is where the real difference sits. Anthropic says cache reads make up most of what agent work costs. OpenAI now discounts cache hits by 90% and lets developers set the breakpoints. Reasoning effort can change mid-conversation. Tools can switch on and off. The cache survives either way. GitHub says that change cut the share of freshly processed prompt tokens by more than half. Push the full conversation history and tool definitions into every request, and these cuts mostly pass you by.

Cheap models can now guard expensive ones. GPT-6 Luna runs $0.10 per million input tokens. MiMo-V2.6-Pro comes in at $0.13 per task. A second model re-checking a stronger model's output was hard to justify on cost a month ago. Two cautions. The 50% cuts are measured against current promotional prices, and the open-weight lead has traded hands between Kimi and Qwen all year. The rate card is not a constant.

- Recompute cost per request from last week's logs. Pull it from real traces, not from the rate card.
- Keep the stable parts of a prompt at the front, meaning the system prompt and the tool definitions. Push timestamps and user input to the back. A cache only hits when the prefix matches.

## The rest of today's news

- **Meta admits Muse took inspiration from OpenClaw**: Nat Friedman, head of product at Meta Superintelligence Labs, posted on X that Muse was "definitely heavily inspired as a product by OpenClaw" while being built from scratch. [TechCrunch](https://techcrunch.com/2026/09/22/meta-admits-muses-likeness-to-openclaw-isnt-a-coincidence/)
- **Mirendil in talks for $1B at a $5B valuation**: Former Anthropic researchers founded the self-improving AI startup. Kleiner Perkins is in talks to lead the round. [Bloomberg Law](https://news.bloomberglaw.com/artificial-intelligence/ex-anthropic-staffers-ai-startup-in-talks-for-5-billion-value)
- **OpenAI opens training-time evaluations to outsiders**: The company is in talks with groups including METR and Redwood Research, with no partners or access terms settled yet. Sam Altman promised physical access and publication rights on September 12. [TNW](https://thenextweb.com/news/openai-evaluators-training-phase)
- **ShinyHunters claims FBI data**: The group says it used an Oracle PeopleSoft zero-day to take employee and applicant data from FBI-related services. A 5,000-record sample seen by 404 Media contains addresses, phone numbers and spouse details, and the FBI's jobs site was defaced. [404 Media](https://www.404media.co/we-hacked-the-fbi-hackers-say-they-have-data-on-all-fbi-employees/)