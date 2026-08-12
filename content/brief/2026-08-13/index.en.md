---
title: "Grok 4.6, Qwen3.8, DeepSeek V4 Pro ship in one day"
date: 2026-08-13
summary: "The Grok 4.5 successor is built to carry complex, multi-step work to completion — research, codebase analysis, or turning an idea into a working app. SpaceXAI…"
---

## Startup / Product / Platform Radar
- **SpaceXAI (xAI) ships Grok 4.6, tuned for long-running agents**: The Grok 4.5 successor is built to carry complex, multi-step work to completion — research, codebase analysis, or turning an idea into a working app. SpaceXAI says it matches GPT-5.6 Sol with a 61 on the Artificial Analysis Intelligence Index, and it is available today in Cursor and Grok Build. [SpaceXAI](https://x.ai/news/grok-4-6)
- **Qwen3.8-2.4T-A95B brings a Max-class model to open weights**: Alibaba's Qwen released a 2.4T-parameter, 95B-active MoE model — the first Qwen-Max-class model available openly. It improves coding, professional work, research, and long-horizon agentic tasks, with 262K native context extensible past 1M tokens. [Hugging Face](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)
- **DeepSeek V4 Pro 0813 reaches general availability**: The GA release of DeepSeek's large-scale MoE model, priced at $0.435 input / $0.87 output per 1M tokens, with a 1M-token context window and up to 384K output tokens. [OpenRouter](https://openrouter.ai/deepseek/deepseek-v4-pro-0813)
- **Lovable confirms a $13.3B valuation with a $400M Series C**: The app-generation startup raised $400M led by Menlo Ventures and EQT's Scaleup Europe Fund, after passing $500M in annualized run-rate revenue in June. [TechCrunch](https://techcrunch.com/2026/08/12/lovable-confirms-new-13-3b-valuation-raises-another-400m/) · [Lovable](https://lovable.dev/blog/series-c)
- **Made by Google '26: Pixel 11, Pixel Watch 5, Pixel Tag, and a Gemini push**: Google announced the Pixel 11 lineup, a new AirTag rival, and a broad set of on-device Gemini features. [TechCrunch](https://techcrunch.com/2026/08/12/google-unveils-pixel-11-lineup-new-airtag-rival-and-gemini-features-at-made-by-google-2026/)

## AI Future Signals
- **Frontier capability is commoditizing fast — and going open**: Qwen3.8's open Max-class release plus DeepSeek V4 Pro's sub-$1 token pricing show frontier performance is no longer locked to a few closed labs. Teams should design for model portability rather than vendor lock-in. [Hugging Face](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) · [OpenRouter](https://openrouter.ai/deepseek/deepseek-v4-pro-0813)
- **Training-data consent shifts to opt-out by default**: Amazon will train on Twitch streamers' content unless creators opt out. Twitch's CPO admitted "if this was opt-in, nobody would opt in." It signals how platform-scale training data is increasingly assumed rather than requested. [TechCrunch](https://techcrunch.com/2026/08/12/amazon-will-train-on-twitch-streamers-content-by-default-unless-they-opt-out/) · [The Verge](https://www.theverge.com/tech/979112/twitch-streamers-can-now-opt-out-from-training-amazons-ai)

## Realistic Opportunities / Experiments
- **Prototype long-context agentic apps on DeepSeek V4 Pro**: $0.435/$0.87 per 1M tokens with a 1M context window makes it cheap to ship multi-step agents that ingest an entire codebase or corpus at once. [OpenRouter](https://openrouter.ai/deepseek/deepseek-v4-pro-0813)
- **Self-host a Max-class model with Qwen3.8**: With 95B active parameters and vLLM/SGLang compatibility, teams can now run frontier-grade inference in-house for data-sovereign professional and enterprise workloads. [Hugging Face](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)

## Uncertainties / Keep Watching
- **Is AI-coding funding getting frothy?**: Cognition is reportedly in talks to raise at a $40B valuation just months after $26B, and Blacksmith jumped ~10x to $550M in under a year. Nothing is closed, and the revenue multiples behind these numbers are unproven. [TechCrunch](https://techcrunch.com/2026/08/12/ai-coding-startup-cognition-reportedly-already-in-talks-to-raise-at-40b-valuation/) · [TechCrunch](https://techcrunch.com/2026/08/12/blacksmiths-valuation-jumps-10x-to-550m-as-ai-coding-fuels-software-validation/)
- **Frontier benchmark claims are largely self-reported**: Grok 4.6's "matches GPT-5.6 Sol" claim rests on vendor-published system cards and leaderboards, not independent verification. Test models against your own workloads before committing. [SpaceXAI](https://x.ai/news/grok-4-6)