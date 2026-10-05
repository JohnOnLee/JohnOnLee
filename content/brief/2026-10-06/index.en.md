---
title: "Reflection Beam: 501B open weights due, cheap inference"
date: 2026-10-06
summary: "Reflection, a New York startup backed by Nvidia, unveiled its first open-weight model, Beam, on October 5. It is a text-only mixture-of-experts model with 501…"
---

## Nvidia-backed Reflection has announced Beam, its first open-weight model

Reflection, a New York startup backed by Nvidia, unveiled its first open-weight model, Beam, on October 5. It is a text-only mixture-of-experts model with 501 billion total parameters and 23 billion active, aimed at coding, reasoning, and agentic work, with a 1 million token context window. The company pretrained it on 23.8 trillion tokens, then ran high-compute reinforcement learning for four weeks across 10,500 Nvidia GB300 GPUs, generating more than 100 million rollouts. [Reflection](https://reflection.ai/blog/introducing-beam) · [TechCrunch](https://techcrunch.com/2026/10/05/reflection-debuts-beam-a-open-weight-ai-model-to-rival-chinese-models-at-lower-compute-cost/)

Reflection says Beam scores on par with Z.ai's GLM-5.2 while using three to four times less inference compute. Those numbers are the company's own, and nothing has been independently verified. GLM-5.2 shipped in July and was already superseded by GLM-5.3 in August; the strongest open models, like Moonshot's Kimi K3, still sit ahead. What arrived today is one more cheap, permissively licensed option, in a market where the West had almost none. [Fortune](https://fortune.com/2026/10/05/reflection-ai-unveils-beam-a-new-us-based-open-source-model-to-compete-with-china/)

You cannot download it yet. The announcement is a preview with a waitlist, and the weights, technical report, and model card arrive later this month under an Apache 2.0 license.

## A Western candidate for self-hosted coding agents, on paper

Beam's 23 billion active parameters put it on a rented GPU or two. Your laptop will not run it. The audience here is a team whose API bill has grown because it runs agent loops, not somebody experimenting with local inference on a MacBook. If the weights land under Apache 2.0, the fine-tune and the eval set stay yours, and there is somewhere to go when a vendor raises prices. Until now, that slot belonged almost entirely to Chinese open models.

The "America catches up to China" framing oversells it. Reflection measured against a model already two releases old, and the top of the open field is still Chinese. Cost is what moved today. Capability leadership did not change hands. Agent loops re-send the same context many times over, so token price turns into product cost, and that is the claim worth testing.

There is nothing to decide before the weights and independent evaluations arrive. Performance, hardware requirements, and the license text are all unconfirmed. If you are about to lock a coding agent into a closed API, waiting until the end of the month costs you little.

## The rest of today's news

- **llama.cpp v0.6.0 is out**: the ggml inference engine adds MTP speculative decoding for Qwen4Exp and support for GLM-5.3-Flash. [GitHub](https://github.com/ggml-org/llama.cpp/releases/tag/v0.6.0)
- **OpenAI will watermark ChatGPT text in the EU**: rolling out over weeks to ChatGPT and Codex users there; API developers worldwide can opt in for select models starting today, off by default. [TechCrunch](https://techcrunch.com/2026/10/05/openai-will-start-watermarking-chatgpts-text-in-the-eu/)
- **Reka previews Rho-1, a 19B omni model**: text, images, video, and actions handled inside one network. [Reka](https://reka.ai/news/rho-1-collapsing-the-multimodal-stack)
- **Aleph Alpha releases Kolibri, a European open-weight model**: supports German and English, weights on Hugging Face. [Aleph Alpha](https://aleph-alpha.com/en/news/kolibri-sovereign-ai-made-in-germany/)
- **Cohere launches North 2**: its enterprise agent platform adds cross-session memory and cost controls. [Unite.AI](https://www.unite.ai/cohere-launches-north-2-with-redesigned-agent-harness-and-memory/)
- **Malaysia previews a high-risk AI bill**: a risk-based framework expected in parliament early next year. [The Star](https://www.thestar.com.my/news/nation/2026/10/05/gobind-high-risk-ai-systems-to-face-stricter-safeguards-under-new-bill)