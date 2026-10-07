---
title: "Claude Haiku 5.5: 10x cheaper"
date: 2026-10-08
summary: "Anthropic released Claude Haiku 5.5 on October 7. It charges $0.10 per million input tokens and $0.50 per million output, against $1 and $5 for Haiku 4.5. That…"
---

## Anthropic cut its small-model price to a tenth

Anthropic released Claude Haiku 5.5 on October 7. It charges $0.10 per million input tokens and $0.50 per million output, against $1 and $5 for Haiku 4.5. That is a tenth of the price. It holds while your prompt stays under 100,000 tokens. Past that line the rate jumps to $0.50 in and $2.50 out, and cached reads come in at $0.01. The context window is 1 million tokens with 128k output, and the model is live on the Claude API, Amazon Bedrock, Google Cloud and Microsoft Foundry. Anthropic says it costs about 75% less to run on average. [Anthropic](https://www.anthropic.com/claude-haiku-5-5) [Claude Platform](https://platform.claude.com/docs/en/models/haiku-5-5/overview)

There was a second price change the same day. Anthropic halved Sonnet 5.5's cache reads, which it says makes that model about 20% cheaper on most agentic work, and added a monthly API credit for Max and Team subscribers. OpenAI also pushed GPT-6 to every ChatGPT tier that day, with GPT-6 Luna taking the free tier. The cheap end of the market got repriced on both sides at once.

## The bill is set by the 100k line and a new tokenizer

What sets your product cost is not the rate card but the invoice. Cross 100,000 tokens and the input rate multiplies by five, so a loop that resends a long context on every call does not see the full cut. Batch calls take another 50% off input and output.

The tokenizer changed too. The same text counts as roughly 30% more tokens than on Haiku 4.5, which eats into the tenfold cut. Anthropic's 75% average already includes that effect. Moving short, repetitive calls first makes sense: classification, summarization, routing, subagents. Keep the hard turn on a larger model.

## The benchmarks are still the vendor's own

Most Haiku 5.5 numbers come from Anthropic's own system card. Third-party reruns may move the rankings, and the comparison with GPT-6 Luna depends on the workload. The 100k line and the tokenizer change are documented facts, which means your own token count and invoice are the only numbers that settle what you save.

## The rest of today's news

- **OpenAI puts GPT-6 on every tier**: Intelligent UI returns interactive charts, buttons and forms instead of plain text, first on paid plans and then on Free and Go from October 8. [OpenAI](https://openai.com/index/gpt-6-for-everyone/)
- **llama.cpp lands in Windows ML**: point a GGUF model at WinMLServer and get an OpenAI-compatible endpoint, with Windows picking GPU, NPU or CPU for you. [Windows Blog](https://blogs.windows.com/windowsexperience/2026/10/07/building-windows-for-hybrid-intelligence/)
- **Google opens Playground**: a Labs experiment where a text prompt builds a browser game you can play and share, US users aged 18 and up for now. [TechCrunch](https://techcrunch.com/2026/10/07/google-experiments-with-an-ai-powered-gaming-platform/)
- **Google opens SynthID checks to everyone**: a public site for verifying whether an image, video or audio clip came from a generator, against about 1 million checks a day. [TechCrunch](https://techcrunch.com/2026/10/07/googles-new-synthid-website-can-identify-ai-generated-media/)
- **Meta's Muse reaches iPad**: a dedicated iPad app a month after launch, with Sensor Tower estimating 6.6 million installs. [TechCrunch](https://techcrunch.com/2026/10/07/metas-muse-launches-on-ipad-just-a-month-after-its-mobile-debut/)
- **Tab emerges at a $300M valuation**: a stealth personal assistant built around everyday tasks, with the company declining to share funding details. [TechCrunch](https://techcrunch.com/2026/10/07/another-personal-ai-assistant-has-launched-meet-tab-which-emerged-from-stealth-with-a-300m-valuation/)