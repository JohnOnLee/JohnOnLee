---
title: "Gemini 3.8 Live reopens voice-stack math"
date: 2026-09-16
summary: "Minute pricing and async tool calls make voice-agent design about session cost plus wait handling and model portability."
---

## Google is going after the cascaded voice stack

Google released Gemini 3.8 Live and Gemini 3.8 Live Extended Thinking on September 15. Both are native speech-to-speech models, available now in the Gemini Live API and AI Studio. [Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/)

Pricing is per minute: $0.005/min for audio input and $0.018/min for audio output. A ten-minute call costs $0.05 in plus $0.18 out, so $0.23; an hour costs $1.38. [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing)

Asynchronous function calling is the product detail to watch. Tool calls run in the background while audio keeps streaming, and Google positions the models as an alternative to chaining ASR, an LLM, and TTS. [Google for Developers](https://blog.google/innovation-and-ai/technology/developers-tools/build-real-time-voice-applications-gemini-audio/)

The Live API also exposes live visual context, alphanumeric precision for confirmation codes and claim numbers, 97 languages with accent consistency, and real-time audio merged with structured data. Extended Thinking reasons in the background while it speaks, then opens with cues like "let me check that".

The benchmark numbers are strong. 3.8 Live Extended Thinking ranks first on Artificial Analysis' Speech to Speech Quality Index at 82.6, with 68.6% on τ-Voice, 35.1% on τ-Voice-banking, and 97.7% on Big Bench Audio. [MarkTechPost](https://www.marktechpost.com/2026/09/15/google-releases-gemini-3-8-live-and-3-8-live-extended-thinking-for-production-grade-voice-agents/)

The hosting story is closed. There are no open weights and no self-hosting path. You reach the models through streaming partners including LiveKit/Pipecat/Vercel/Agora. 9to5Google reports that the same models now sit behind Gemini Live and Gmail. [9to5Google](https://9to5google.com/2026/09/15/gemini-3-8-live-announced/)

## Voice products now have a simpler unit-cost model

For indie developers, the useful change is not the model name. It is the way code and cost collapse into one session. Wiring ASR, an LLM, and TTS together, then handling turns and interruptions between them, can shrink into a single live connection.

Async tool calls also change wait-state design. Remove the old "checking that now" filler audio, let the model speak while the tool runs, and compare perceived wait against the old cascade. If live visual context is useful in your product, try a support flow that reads a claim number from a photo or an error from a screen inside the same session.

Minute billing turns call length into unit cost. The $0.23 ten-minute call and $1.38 hour scale roughly linearly, so free-call products need session caps and idle-session teardown before the pricing page goes live. Add up your current STT plus LLM plus TTS rates for the same ten-minute conversation; the stack switch becomes a number.

Portability belongs in the abstraction layer. Calling the Live API directly ties the product to Google, so LiveKit or Pipecat can keep the session code stable while the model changes underneath.

## Check before promising automation

τ-Voice-banking at 35.1% is low. In regulated flows like banking, agents still finish roughly a third of the tasks. Product copy that promises full automation is early.

The free tier feeds training. Google's price sheet marks free-tier traffic as "used to improve our products". If real customer voices run through the product, treat the paid tier as the baseline.

Long-call behavior still needs testing. The published numbers come from benchmarks and short demos, so context retention and interruption handling past thirty minutes need your own runs.

Cost tracks conversation length. A session left open bills idle time too. Any plan with unlimited calls converts straight into loss.

## The rest of today's news
- **Developers found ways to run Claude Code without Anthropic models**: proxy workarounds are circulating. [The Information](https://www.theinformation.com/articles/developers-find-ways-use-claude-code-without-anthropic-models)
- **Meta opened WhatsApp Business setup to AI agents**: a new MCP server lets coding agents handle WhatsApp templates and troubleshooting. [TechCrunch](https://techcrunch.com/2026/09/15/meta-now-lets-ai-agents-handle-the-boring-parts-of-whatsapp-business-setup/)
- **OpenAI backed the FRONTIER Act**: the bipartisan House plan requires third-party safety assessments, and the same day brought reports that three labs have been discussing safety for weeks. [Politico](https://www.politico.com/news/2026/09/15/openai-backs-bipartisan-house-plan-for-third-party-safety-assessments-01076588) · [TechCrunch](https://techcrunch.com/2026/09/15/openai-anthropic-google-have-been-in-talks-on-ai-safety-for-weeks/)
- **TypeSafe launched Jev and raised $40M in seed funding**: the model returns typed decisions with probabilities instead of prose, at $0.042 per million input tokens. [TypeSafe](https://typesafe.ai/blog/introducing-system-one-models-and-jev)
- **Factory raised $200M at a $5B valuation**: triple its valuation from five months ago, with automatic task-level model routing cutting token spend by more than 60%. [Factory](https://factory.com/news/5-billion-valuation)
- **404 Media: agents with account access are already harming the internet**: a roundup of the damage caused by agents holding real permissions. [404 Media](https://www.404media.co/theres-a-100-chance-ai-agents-are-already-ruining-the-internet/)
- **South Korea's KISA is writing security guidelines for autonomous agents**: a checklist for companies deploying agentic services, possibly covering physical AI. [The Star](https://www.thestar.com.my/tech/tech-news/2026/09/15/south-korea-to-develop-new-security-guidelines-for-autonomous-ai-agents)
- **74 of 102 F-Droid apps updated that day looked AI-written**: a three-tier eyeball judgement of repositories, not code analysis. [tintotint](https://tintotint.eu/whacky-corner/f-droid_slop/)
- **The OpenAI Foundation opened its $125M Public Data for Health program**: the first grant is $40M to UNC's cancer center for personalized vaccine data. [OpenAI Foundation](https://openaifoundation.org/news/public-data-for-health) · [UNC](https://news.unchealthcare.org/2026/09/unc-lineberger-secures-40m-from-openai-foundation-to-make-cancer-vaccines-more-effective/)
- **US Commerce told Kalshi to pull its AI compute price index**: national security grounds, plus a request to freeze new compute contracts for 60 days. [Semafor](https://www.semafor.com/article/09/15/2026/commerce-dept-ordered-kalshi-to-take-down-ai-compute-futures-product)
- **Profound raised $180M at a $1.8B valuation**: an AEO toolset for brand visibility in AI search, doubling its valuation in seven months. [TechCrunch](https://techcrunch.com/2026/09/15/aeo-startup-profound-hits-unicorn-valuation-raises-180m-series-d-7-months-after-last-round/)
