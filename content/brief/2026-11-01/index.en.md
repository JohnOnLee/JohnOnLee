---
title: "Claude can't certify human text"
date: 2026-11-01
summary: "Anthropic has extended text watermarking to older Claude models, with no customer option to turn it off."
---

## Anthropic's Claude watermark is beyond your product's control

Anthropic has extended text watermarking to older Claude models, with no customer option to turn it off.

Anthropic embeds the watermark in the text at the model level, so it appears in your product's API output and travels wherever someone copies and pastes that text. Some editing leaves it intact. The company is applying this approach after signing the EU AI Act's Article 50(2) Code of Practice on Transparency of AI-Generated Content. Your product cannot switch it off. A feature that generates text with these models has no basis to promise customers that a human wrote it. [Anthropic](https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content)

An email to API customers names four newly added models: Claude Mythos 5, Opus 4.7, Opus 4.6 and Sonnet 4.6. Of those, Opus 4.6 and Sonnet 4.6 carry the watermark only at the default temperature, top_p and top_k. Anthropic tells customers who rely on watermarking for compliance to keep those defaults. Its email attaches no such condition to Mythos 5 or Opus 4.7. If your product uses the mark to classify text, you also need to check which model and settings produced the marked output. [The Decoder](https://the-decoder.com/anthropics-watermark-rollout-leaves-a-loophole-on-two-older-claude-models/)

But detecting a mark does not prove Claude wrote the text, because Anthropic says proofreading and translation also produce watermarked output. A person can supply the ideas and draft, then acquire the mark by having Claude process their writing. Your product would label that work as AI writing if it treated detection as proof of authorship.

A missing mark does not prove human authorship either. Short passages may lack a reliable signal. Heavy editing can erase it, according to Anthropic's own account of the limitations. If your product fails to detect a watermark in its output, that result gives you no basis to tell a customer that a human wrote the text. Neither result establishes authorship, so a feature that makes prose sound natural loses its basis for promising human authorship.

Detection is currently in private preview for eligible organisations and enterprises required to verify watermarking under EU law. Anthropic plans to widen access to its detection API over time. You cannot build on the assumption that every developer can immediately add this detector to a product. Even with access, the limitations prevent a reliable distinction between proofread human writing and short AI passages.

Anthropic explicitly tells developers who deploy Claude in their own products to independently assess what Article 50 requires of their products and services. A watermark in the model does not establish that your product has met its obligations. Customer notices and classification results need to make the limitation clear: watermarking cannot certify human authorship.

## The rest of today's news

- **OpenAI misses its funding target**: The company secured about $11 billion against a $30 billion target, at a $1.25 trillion valuation below its $1.4 trillion aim. [TechCrunch](https://techcrunch.com/2026/10/31/openai-reportedly-lowers-funding-target-for-new-round/) [The Decoder](https://the-decoder.com/openai-raises-just-11-billion-of-its-30-billion-target-as-big-investors-lose-their-ai-appetite/)
- **Daybreak Blue training policy changes**: OpenAI announced plans to train on cybersecurity session data from November 29, then promised a separate opt-out after a backlash; interactions flagged in safety reviews can still be used for safety purposes. [The Decoder](https://the-decoder.com/openai-plans-to-train-models-on-daybreak-blue-cybersecurity-session-data-that-was-previously-off-limits/)
- **VOLTA uses AI to appraise victims**: Cisco Talos documented an infostealer that sends stolen evidence to an LLM to rank victims' assets by monetisation value and switches models when one refuses. [Cisco Talos](https://blog.talosintelligence.com/appraisal-by-ai-model-driven-victim-prioritization-in-the-volta-infostealer/)
- **Prospero coding harness released**: Chris Wellons released a harness built with C++ and Dear ImGui that ships without model providers, requiring users to connect an API or llama.cpp themselves. [nullprogram](https://nullprogram.com/blog/2026/10/31/)