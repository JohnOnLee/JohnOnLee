---
title: "Gemini 4 Carbon tops the index, open only to defenders"
date: 2026-10-29
summary: "Google announced Gemini 4 Carbon on October 28. Google positions it as the company's strongest frontier model, built for security work. Carbon ranks first on…"
---

## Carbon takes first place, and only cyber defenders can call it

Google announced Gemini 4 Carbon on October 28. Google positions it as the company's strongest frontier model, built for security work. Carbon ranks first on the Artificial Analysis Intelligence Index v5.0 at 59. Its security scores are 88.2% on SEC-bench Pro for finding vulnerabilities, 54.8% on ExploitGym for proving they are exploitable, and 71.0% on CWE-bench for patching the root cause. [Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/) [Ars Technica](https://arstechnica.com/ai/2026/10/google-announces-gemini-4-carbon-its-latest-frontier-ai-model-that-you-cant-use/)

Almost nobody can call it yet: access opens this week to a subset of cyber defenders, widens to trusted partners through Google's Fairwind program, and is promised to developers, businesses and consumers "as soon as possible" with no date attached. Argon, the previous model, went through the same staged release. Ars Technica expects a few weeks before a wide release if Carbon follows it.

Pricing arrived before access did. During the introductory period Carbon costs $2 per million input tokens and $10 per million output tokens, with cached input at 95% off, then doubles to $4 and $20. Ars Technica asked Google when the discount ends and got no date. Argon's discount runs through the end of November.

The benchmark claims need context. Google measured the security scores without guardrails, and some results elsewhere are internal. On Gray Swan's indirect prompt injection evaluation, Carbon resisted every attempt, a 0.0% success rate against 0.7% for Argon, 1% for Claude Opus 5.5 and 8.5% for GPT-6 Astra. Ars Technica reads the field as one neighbourhood where every frontier model lands within a few points.

## A few points on an index is not a reason to move your stack

The improvements worth your attention are behavioural, not the security scores. Google says Carbon makes about half as many unsupported claims as Argon. When the evidence is ambiguous, it pulls the sources and shows the user the discrepancy instead of guessing. It cuts overreach by 26% and under-service by 29%. The four failures that break products are invented facts, quiet guessing, edits outside scope and skipped steps. Each one is testable on the model you already run. Ask something with a single fact deliberately missing and see whether the model says so. Give it a task with a file boundary and see whether it crosses.

Security is the part that reaches small teams last. A model that finds and patches vulnerabilities is worth money to a two-person team, but its first users are defence organisations and Google has published no API date. Nothing about your review process should change until it does.

Price is the other open item: with no end date for the introductory rate, a feature whose unit economics depend on Carbon is a bet on a date nobody has published. Your stack does not change this week, so when you next pick a model, read the access terms and the price expiry next to the score.

## The rest of today's news

- **SK hynix posts an 80% operating margin and sees memory shortages through 2030**: Q3 revenue reached 104.6 trillion won and operating profit 83.3 trillion won, both records. SK hynix says demand will outrun supply through 2030, and more than half of its 2027-2028 capacity is locked into long-term deals with 14 customers. [SK hynix](https://news.skhynix.com/en/q3-2026-business-results/)
- **Reddit rolls out a For You feed worldwide**: the home screen splits into an algorithmic For You tab and a Following tab, arriving over the next few weeks. [TechCrunch](https://techcrunch.com/2026/10/28/reddit-is-the-latest-platform-to-embrace-the-for-you-feed/)
- **NVIDIA releases Nemotron 3.5 Transcribe**: open weights, 40 languages, speaker attribution in 13, recordings up to an hour, shipped with the Granary v2 data pipeline and fine-tuning recipes. [Hugging Face](https://huggingface.co/blog/nvidia/nemotron-transcribe-granary)
- **ChatGPT Dots can be texted now**: US Pro users in a preview can send text, photos or voice notes over iMessage and RCS, and the agent messages first when a task moves. [Engadget](https://www.engadget.com/2300235/openai-now-lets-you-text-your-dot-agent/)