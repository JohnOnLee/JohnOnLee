---
title: "Gemini 4 Carbon: wait to switch"
date: 2026-10-29
summary: "Google announced Gemini 4 Carbon on October 28, 2026. It has not published a date for small teams to use the API."
---

## Carbon ranks first, but has no API date for small teams

Google announced Gemini 4 Carbon on October 28, 2026. It has not published a date for small teams to use the API.

Google describes Carbon as its strongest frontier model, built to find and fix security vulnerabilities; on the Artificial Analysis Intelligence Index v5.0, it ranks first with a score of 59. [Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/)

Carbon scored 88.2% on SEC-bench Pro for finding vulnerabilities, 54.8% on ExploitGym for proving they can be exploited, and 71.0% on CWE-bench for patching the root cause. Finding a vulnerability and fixing its cause are different jobs. The relevant result depends on the work you intend to give it. Google measured these security scores without guardrails, and some other results come from internal evaluations.

In Gray Swan's indirect prompt injection evaluation, the attack success rate was 0.0%. That does not establish that Carbon will avoid hallucinations or skipped steps, and Ars Technica describes frontier models as landing within a few points of each other. The scores alone are not enough to justify replacing your current model. [Ars Technica](https://arstechnica.com/ai/2026/10/google-announces-gemini-4-carbon-its-latest-frontier-ai-model-that-you-cant-use/)

Google plans to give a subset of cyber defenders access this week, expand to trusted partners through its Fairwind program, then reach developers, businesses and consumers as soon as possible. Argon followed the same sequence, so Ars Technica expects a few weeks before broad access if Carbon follows it. Google has promised no such date, which leaves a small team without a firm basis for scheduling adoption.

Introductory rates are $2 per million input tokens and $10 per million output tokens, with cached input 95% off. After the discount, input and output rates double to $4 and $20. Whether the discount will still apply when you can use it is unknown. Ars Technica asked Google for an expiry date and received none, and Argon's November discount says nothing about Carbon's. You need the access schedule and the discount period together to judge the cost of adoption.

## What to test in your current model while Carbon is closed

Google says Carbon makes about half as many unsupported claims as Argon. When evidence is ambiguous, it retrieves sources and shows the user the discrepancy instead of guessing. Google also reports a 26% reduction in acting outside the instruction's scope and a 29% reduction in skipping required steps.

You can check whether your current model stops guessing when evidence is ambiguous. Give it conflicting evidence and examine whether it explains the disagreement or fills the gaps by guessing. Displaying a source does not establish that the answer follows from it, so check the support for the answer too.

Scope violations and omissions need separate checks. Specify the allowed work and the required steps, then examine whether the model did something unasked and whether it skipped something necessary. Completing the request does not establish that it respected both conditions. Testing your current model this way gives you the same requests to compare against Carbon once you can use it.

The decision to change your stack can wait for the access schedule and the pricing terms. Meanwhile, testing what your current model actually does gives you a basis for comparison.

## The rest of today's news

- **SK hynix Q3 2026 results**: Revenue of 104.6 trillion won and operating profit of 83.3 trillion won were both records, with an 80% operating margin; the company says demand will exceed supply through 2030 and has locked more than half its 2027-2028 capacity into long-term deals with 14 customers. [SK hynix](https://news.skhynix.com/en/q3-2026-business-results/)
- **Reddit For You**: Reddit is splitting its home screen into an algorithmic For You tab and a Following tab worldwide over the next few weeks. [TechCrunch](https://techcrunch.com/2026/10/28/reddit-is-the-latest-platform-to-embrace-the-for-you-feed/)
- **NVIDIA Nemotron 3.5 Transcribe**: The open-weight transcription model supports 40 languages, speaker attribution in 13 and recordings up to one hour, with the Granary v2 data pipeline and fine-tuning recipes released alongside it. [Hugging Face](https://huggingface.co/blog/nvidia/nemotron-transcribe-granary)
- **ChatGPT Dots texting preview**: US Pro users can send text, photos or voice notes over iMessage and RCS, and the agent sends a message first when a task progresses. [Engadget](https://www.engadget.com/2300235/openai-now-lets-you-text-your-dot-agent/)