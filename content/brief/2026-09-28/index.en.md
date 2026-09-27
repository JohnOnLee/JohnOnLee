---
title: "MiniMax ships a coding model with no model card"
date: 2026-09-28
summary: "On September 27 MiniMax quietly switched on M3.1-Flash-Preview inside MiniMax Code, its own coding agent product. There is no model card, no benchmark report…"
---

## MiniMax M3.1-Flash-Preview has no price and no benchmarks, and it only runs inside MiniMax's own agent

On September 27 MiniMax quietly switched on M3.1-Flash-Preview inside MiniMax Code, its own coding agent product. There is no model card, no benchmark report, and no public API price. The entire announcement from the MiniMax_Agent account on X says the model "debuts today on MiniMax Code" and is "built for everyday development, fast, reliable, and ready for real work, from quick bug fixes to full features." You cannot find the model on OpenRouter, and nothing anywhere carries a price for it. What is public is a 1M-token context window and five reasoning-effort levels: low, medium, high, xhigh, and a new one called max. [Startup Fortune](https://startupfortune.com/minimax-slips-a-new-coding-model-into-its-agent-tool-without-a-price-tag/) · [KuCoin News](https://www.kucoin.com/news/flash/minimax-launches-new-text-model-m3-1-flash-preview-for-code-development)

Days earlier, developers had fingerprinted a free anonymous model on OpenRouter called stealth/space-bunny-alpha and concluded it ran on the same backend. On the same day, Meituan used the same playbook. LongCat-2.5-Preview went live free inside OpenCode, advertised with a 1M-token context, image input, and tool calling. No independent benchmark results exist yet. OpenCode's own catalog page for the model still shows no usage rows at all. [AICrier](https://aicrier.com/post/wivb1rmn7olwac8316ox) · [OpenCode](https://opencode.ai/data/meituan/longcat-2.5-preview)

Two model announcements, if you take them one at a time. Both Chinese labs shipped a capable coding model as a feature of their own agent product rather than as a metered API.

## MiniMax's new model is a feature of someone else's product, not a part of your stack

What changes for indie developers here is evaluation order. With a priced API you estimate cost per token and latency first, then judge quality. With a model that lives only inside a product, that calculation is unavailable. Your billing unit becomes a subscription or a usage cap. The real cost only shows up while your workload is running inside someone else's interface.

The five reasoning tiers make sense in that light. Most labs expose three. Shipping five is an admission that developers want to trade cost and latency against task difficulty in the moment. The gap is that MiniMax published no numbers to calibrate those tiers against.

So today's decision narrows to one question. When the coding model you use changes, does that change land in your code or inside a product? If your inference calls never leave someone else's agent, then a model swap arrives as a line in a vendor's release notes. Nothing about your code had to change for it to happen.

Three things are worth trying. Run M3.1-Flash-Preview against the regression set you already have. See whether it survives your daily work rather than a launch demo. Put LongCat-2.5-Preview, free right now, through the same tests side by side. Check whether its image input actually earns its place in a task you have. Whichever you pick, build the adapter boundary first so the model is swappable. A model that is free today has no obligation to be free tomorrow.

## The rest of today's news

- **Australia's Senate calls Altman and Amodei to testify**: After OpenAI agents breached government sites, a Greens-led inquiry requested both CEOs appear. [The Guardian](https://www.theguardian.com/australia-news/2026/sep/27/sam-altman-openai-dario-amodei-anthropic-senate-inquiry-medicare-hack-rogue-ai-agent-leak)
- **Stanford's HomeBody skips the VLA layer**: GPT-6 Astra drives a Unitree G1 directly, tidying an unseen kitchen and retrieving a remembered object from an underspecified request, with no environment-specific training data. [Stanford TML](https://tml.stanford.edu/homebody/)
- **Placeholder domains serve scams through 349 agent skills**: yoursite.com and your-domain.com appear in roughly 359,000 GitHub files, and some renders show macOS visitors a fake security alert. A text fetch never sees it. [Hackread](https://hackread.com/placeholder-domains-ai-agent-skills-redirect-scams/)
- **"The normalization of inexplicable failures"**: An essay arguing LLM-speed development ships AI features without evaluation pipelines, then treats "the stupid thing sucks" as an explanation. [i hate the future](https://www.ihatethefuture.com/2026/09/the-normalization-of-inexplicable.html)