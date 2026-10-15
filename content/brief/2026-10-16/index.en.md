---
title: "Meta's 816B Muse Spark Open runs on two Mac Studios"
date: 2026-10-16
summary: "On October 15 Meta released the weights for Muse Spark Open, an 816B-parameter model with a 1M-token context and text, image, video, audio input."
---

## Meta released 816B of open weights that need a two-Mac desk

On October 15 Meta released the weights for Muse Spark Open, an 816B-parameter model with a 1M-token context and text, image, video, audio input. [Meta AI Research](https://research.meta.ai/blog/muse-spark-open) [Hugging Face](https://huggingface.co/collections/meta-models/muse-spark-open)

The size of the model and the machine it needs show where it fits. It is a mixture of experts that activates 42B parameters per token, so it never computes all 816B at once. On a desk it runs on two M5 Ultra Mac Studios with 512GB of unified memory each, joined by MLX into a single terabyte. Apple has not shipped the 512GB Mac Studio yet. The 256GB version already sells for over $10,000. [MacRumors](https://www.macrumors.com/2026/10/15/meta-muse-spark-open-mac-studio/)

Weights are also on Amazon SageMaker AI, Google Cloud Model Garden and Microsoft Foundry Models. Inference comes through Baseten, Fireworks AI, Groq, Modal, Nebius, OpenRouter, Together AI. SGLang, vLLM, TensorRT-LLM, llama.cpp, MLX, Unsloth all support the model on day one. The licence is the Muse Model License, dated October 15. You may copy, modify, distil and distribute it for free as long as your product carries a "Built with Muse Spark Open" notice. A business that sells model access as a service and passes $20 million in gross revenue over any 12 months must notify Meta and sign a separate agreement. Internal use, or use as a component inside your own product, is exempt. [Unite.AI](https://www.unite.ai/metas-816b-parameter-muse-spark-open-weights-are-now-public/)

## On Meta's own card, it leads on agents and trails on coding

The numbers come from the model card Meta published alongside the weights. On agentic evaluations it scores 61.8 on JobBench and 89.2 on MCP-Atlas, the highest in the card's table. Coding goes the other way. It reaches 76.4 on Terminal-Bench 2.1, against Kimi K3 at 85.0, and 39 on the Artificial Analysis Intelligence Index, against GLM 5.3 at 45 and Kimi K3 at 44. "Most capable US open-weight model" compares it with American models only.

For an indie builder, the change is in how you choose a model. A superlative in a release post tells you less than the benchmark that matches your workload. If your product is an agent reading documents and screens, this model is a candidate. If generating code is the core, Chinese open weights are still ahead.

Tuning is the second thing that opened. The full weights are public, so you can fine-tune on your own data with TorchTitan, Hugging Face TRL or Unsloth and run the result on rented GPUs. Fireworks and Together sell managed training too. You can put a model tuned on your own data into a product without buying two Macs.

Not everything is settled. The full evaluation report is not out, and Meta notes in the card that fine-tuning can weaken the safety training. Apple has given no ship date or price for the 512GB Mac Studio.

## The rest of today's news

- **Perplexity open-sources SPACE**: the sandbox that isolates its agents, with state recovery and network controls, is out under Apache 2.0, and CoreWeave, Akamai, Crusoe will offer it to their customers. [Perplexity](https://www.perplexity.ai/hub/blog/open-sourcing-space)
- **NVIDIA releases Nemotron 3.5 Super VL**: a 120B vision-language MoE that activates 12B parameters per token, reads text, images, documents, video, and runs on vLLM and SGLang from day one. [NVIDIA](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning/)
- **FTC demands documents from OpenAI and Anthropic**: roughly 50 pages of civil investigative demands covering safety incidents, safeguards, privacy practices went to both labs. [Ars Technica](https://arstechnica.com/tech-policy/2026/10/ftc-probes-if-openai-anthropic-security-incidents-harmed-americans-report-says/)
- **Anthropic posts $16.8B in Q3 revenue**: up 45% from $11.6B and profitable on an adjusted basis, though growth fell from 143% to 46% and investors are discussing a valuation nearer $1.5T than $2T. [CNBC](https://www.cnbc.com/2026/10/15/anthropics-third-quarter-revenue-hits-16point8-billion-ipo.html)
- **$1 trillion wiped off AI and chip stocks**: Nvidia and AMD sank in a global tech rout over AI funding worries, with SK Hynix down more than 10%, Samsung 8.7% and Advantest nearly 14%; 20 of the largest AI and semiconductor names shed over $1 trillion this week. [CNBC](https://www.cnbc.com/2026/10/15/sk-hynix-samsung-softbank-stocks-asia-tech-rout-ai-funding-worries.html)
- **Figma ships Specs, a design rulebook for agents**: a Markdown editor holding a team's design language that people and AI agents both read, with code layers now in public beta. [Figma](https://www.figma.com/blog/introducing-figma-specs/)
- **Bluesky turns Attie into social vibe coding**: the custom-feed tool now builds quizzes, games, websites on the AT Protocol. [TechCrunch](https://techcrunch.com/2026/10/15/bluesky-expands-its-ai-powered-attie-app-to-let-anyone-build-websites-games-and-more/)