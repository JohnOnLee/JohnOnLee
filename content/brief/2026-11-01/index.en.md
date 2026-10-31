---
title: "Claude watermark has no opt-out"
date: 2026-11-01
summary: "Anthropic has extended Claude's text watermark to four older models, and there is no customer switch for it."
---

## The Claude watermark sits in the model, out of your product's reach

Anthropic has extended Claude's text watermark to four older models, and there is no customer switch for it.

The newly marked models are Claude Mythos 5, Opus 4.7, Opus 4.6 and Sonnet 4.6; models such as Opus 5.5 already carried the mark. [Anthropic](https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content) lists the coverage, and [The Decoder](https://the-decoder.com/anthropics-watermark-rollout-leaves-a-loophole-on-two-older-claude-models/) reports the email to API customers with its settings caveat.

The mark is an imperceptible pattern in word choice. Anthropic says it leaves the meaning and the readability of a response alone, and that output quality is unaffected. That second claim is disputed: blogger John Gruber argues that no two synonyms mean exactly the same thing, so picking words to fit a watermark key costs precision. Because the mark lives in the text, it travels when someone copies and pastes, and can survive some editing. It is applied at the model level, so it appears on every surface: the API, the Claude apps, Claude Code, Claude Cowork, Claude Tag. Output served through cloud partners such as AWS and Microsoft Foundry carries it too.

Support differs by model. Fable 5.1, Opus 5.5 and Sonnet 5.5 also mark cloud-partner output and add C2PA credentials to files. The older models added this week carry Anthropic's own text watermark only, with no cloud-partner mark and no C2PA credentials on files. Where you call the model changes what your output carries.

Two of the older models depend on settings as well. On Opus 4.6 and Sonnet 4.6 the mark applies only at default temperature, top_p and top_k, and a small change to any one of them drops it. Anthropic's email tells customers who rely on the mark for compliance to keep those defaults. The same email attaches no such condition to Mythos 5 or Opus 4.7. If your product treats a mark as a signal, it needs to know which model produced the text and whether the defaults were kept.

## A mark, or the absence of one, will not settle who wrote the text

A detected mark does not prove Claude wrote the original. Anthropic documents that limit itself. Proofreading leaves a mark. So does translation, summarising or simply converting a file, even when the ideas came from somewhere else. Someone can also excerpt or combine that output afterwards. A product that checks a customer's draft and calls every marked result AI-written misdescribes the work it did.

A missing mark does not prove a person wrote the text either. A short passage may be too weak a signal, heavy editing or paraphrase can break detection, and translation or mixed sources complicate it. Conversion and screenshots strip file metadata, some file types are unsupported, and older models predate marking. A feature that treats a negative result as proof of human writing cannot account for those cases.

Neither result identifies the author. What your product can still say is what it did with the text: it proofread a draft, or the text ran through a particular model. You can verify those claims, and they describe the job instead of guessing at a person.

Detection is not open yet. Anthropic runs it as a private preview for organisations that must verify under EU law, such as regulators and newsrooms, and for enterprises with their own compliance duties. It plans to widen API access over time. The free Claude Content Checker reads Claude-issued content credentials in files; it does not judge whether text came from a person.

Anthropic signed the Article 50(2) transparency Code of Practice, and still tells developers who deploy Claude in their own products to work out what Article 50 requires of them. A mark in the model does not settle your product's obligation. Anthropic says technical guidance will follow as it becomes available. Until it does, a product should not harden its design around the mark.

## The rest of today's news

- **DeepSeek begins charging for search**: From midnight Beijing time on November 1, DeepSeek charges $0.75 per 1,000 successful requests for Search and for Fetch, after both were free, including server-side calls made through DeepSeek Harness, Claude Code or Codex. [DeepSeek](https://api-docs.deepseek.com/quick_start/pricing)
- **Daybreak Blue data goes into training**: OpenAI said it will train on Daybreak Blue cybersecurity session data from November 29, data previously kept out of training, then promised a separate opt-out after a backlash; interactions flagged in safety reviews can still be used for safety purposes. [The Decoder](https://the-decoder.com/openai-plans-to-train-models-on-daybreak-blue-cybersecurity-session-data-that-was-previously-off-limits/)