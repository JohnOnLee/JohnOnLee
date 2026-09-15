---
title: "Gemini 3.8 Live for voice agents"
date: 2026-09-16
summary: "both are native speech-to-speech models, available today through the Gemini Live API and AI Studio."
---

## Google shipped Gemini 3.8 Live and 3.8 Live Extended Thinking, aimed straight at the cascaded voice pipeline
- **Live on 15 September**: both are native speech-to-speech models, available today through the Gemini Live API and AI Studio. [Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/)
- **Priced per minute**: $0.005/min for audio input and $0.018/min for audio output. A ten-minute call costs $0.05 in plus $0.18 out, so $0.23; an hour costs $1.38. [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing)
- **Asynchronous function calling sits at the center of the release**: tool calls run in the background while the audio response keeps streaming, and Google positions both models against chaining ASR, an LLM and TTS. [Google for Developers](https://blog.google/innovation-and-ai/technology/developers-tools/build-real-time-voice-applications-gemini-audio/)
- **What else the Live API exposes**: live visual context, alphanumeric precision for confirmation codes and claim numbers, 97 languages with accent consistency, and merging real-time audio with structured data. Extended Thinking reasons in the background while it speaks, and opens with cues like "let me check that".
- **The benchmark numbers**: 3.8 Live Extended Thinking takes first place on Artificial Analysis' Speech to Speech Quality Index at 82.6, with 68.6% on τ-Voice, 35.1% on τ-Voice-banking and 97.7% on Big Bench Audio. [MarkTechPost](https://www.marktechpost.com/2026/09/15/google-releases-gemini-3-8-live-and-3-8-live-extended-thinking-for-production-grade-voice-agents/)
- **Hosted only**: there are no open weights and no self-hosting path. You reach the models through streaming partners such as LiveKit, Pipecat, Vercel and Agora, and 9to5Google reports the same models now sit behind Gemini Live and Gmail. [9to5Google](https://9to5google.com/2026/09/15/gemini-3-8-live-announced/)

## $0.23 for a ten-minute call is the number that reopens your voice stack decision
- **You can delete the three-stage pipeline**: the code wiring ASR to an LLM to TTS, plus the turn-taking and interruption handling in between, collapses into one session. Your latency budget stops being split three ways.
- **The workaround for silence goes away**: the model keeps talking while a tool runs. Instead of pre-recording "one moment please" clips and playing them back, you let async function calling and spoken progress carry the wait.
- **Per-minute billing turns call length into unit cost**: $0.23 for ten minutes and $1.38 for an hour scale linearly. If your product offers free calls, a session cap and idle-session teardown belong in the design before the pricing page.
- **Model portability lives in the abstraction layer**: calling the Live API directly ties you to Google. Put LiveKit or Pipecat in between and your session code survives a model swap.

## What to try now: delete the filler audio and push tool calls to the background
- **Drop the filler clips and compare**: remove your "checking that now" audio, let the model talk until the tool returns, then measure perceived wait against the old cascade.
- **Put the camera into the conversation**: visual context arrives live, so a support flow that reads a claim number off a photo or an error off a screen fits inside one session.
- **Use Extended Thinking as a narration pattern**: on slow jobs, the early acknowledge cue plus step-by-step narration turns dead air into visible progress you can design around.
- **Price a ten-minute call both ways**: add up your current STT, LLM and TTS rates for the same conversation and compare against $0.23. The switch date usually comes out as a number rather than an opinion.

## The caveats around the benchmarks matter more than the headline score
- **τ-Voice-banking at 35.1% is low**: on regulated flows like banking, agents still finish roughly a third of the tasks. Marketing that promises full automation is premature.
- **The free tier feeds training**: Google's price sheet marks free-tier traffic as "used to improve our products". If real customer voices run through your product, treat the paid tier as the baseline.
- **Long-call behavior is unproven**: the published numbers come from benchmarks and short demos. Context retention and interruption handling past thirty minutes need your own tests.
- **Cost tracks conversation length**: a session left open bills idle time too. Any plan with unlimited calls converts straight into loss.

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