---
title: "StepFun Step 5 API, weights Oct 15"
date: 2026-09-21
summary: "StepFun announced Step 5 Preview on September 20, 2026. Calls opened through its own products and API the same day. describes a sparse mixture-of-experts model…"
---

## StepFun opened a 600B MoE through its API and kept the weights for October 15
StepFun announced Step 5 Preview on September 20, 2026. Calls opened through its own products and API the same day. [StepFun's documentation](https://platform.stepfun.ai/docs/en/guides/models/step-5-preview) describes a sparse mixture-of-experts model with 600B total parameters, 27B active per token and a 1M-token context window that accepts text, image and video input. The spec table lists a maximum output of 64k tokens. The Chat Completions section on that same page says max_tokens defaults to no limit. Those two numbers disagree. Measure the ceiling before you design around long outputs.
Pricing runs $1.00 per million input tokens and $2.70 per million output. Cache hits cost $0.05. That is five times the input price and 2.3 times the output price of Step 3.7 Flash, the previous flagship. [Artificial Analysis](https://artificialanalysis.ai/models/step-5) separately scores it 44 on its Intelligence Index, at $0.71 per task and 99.8 output tokens per second.
The weights are not out. StepFun says the full set follows on October 15. On announcement day the Hugging Face repository held a single .gitattributes file, as [OrcaRouter](https://www.orcarouter.ai/blog/step-5-preview-open-weights) documented. The company's claim of costing an eighth of Opus 5, and its own benchmark scores, come with no published method. Cite the source when you use those numbers. The evaluation board dates the model September 18, two days before the announcement. It was callable before it was named.

## What you can decide today is where each request goes, priced per task
Until the weights arrive, Step 5 Preview is a rented model priced by one company. Which requests you send to it is the decision available today. The number that should drive that decision is not the price per million tokens but what one finished task costs. The $0.71 that Artificial Analysis measures reflects how much this model talks. Running the Intelligence Index, it produces about 160 million output tokens against a median of 92 million. At $2.70 per million output tokens, verbosity moves the bill faster than the price sheet suggests.
The $0.05 cache price is conditional. It applies only when you resend the same prefix, and most agent loops rebuild that prefix on every turn. An agent loop that rebuilds a 1M context every turn pays the full $1.00 input rate, while a pipeline that reuses a stable long context pays a twentieth of it. Same model, same usage, and a very different number at the end of the month.
Three checks are worth running now.
- Measure output tokens per task on your own workload. Multiply that by the rate; the per-token price alone tells you little.
- Check whether the changing part of your prompt sits ahead of the stable context. Reordering it can move your input rate between $1.00 and $0.05.
- Pin the model name and the price in config, not in code. If the weights really land on October 15, you will want to swap the endpoint without touching the pipeline.

## The rest of today's news
- **Alibaba released Qwen-Image-2.1 weights**: an image generation and editing model whose visual generative component is 7B, with native transparent RGBA output and up to ten reference images. The qwen-research license bars commercial use without a separate grant. [Hugging Face](https://huggingface.co/Qwen/Qwen-Image-2.1)
- **Tencent showed off Gander**: it handles speech, images and text while working in the background, splitting a conversational cerebellum from a swappable brain. It interrupted users in only 8% of benchmark cases, the best of its group, but trailed on task accuracy. [The Decoder](https://the-decoder.com/tencents-gander-aims-to-keep-talking-while-it-works-in-the-background/)
- **World model companies will not say what they are building**: AMI Labs and World Labs both described themselves as still in a research phase, with no commercial timeline. [TechCrunch](https://techcrunch.com/2026/09/20/world-model-companies-are-keeping-a-lot-of-secrets/)
- **A podcast episode framed the AI slowdown debate**: Anthropic's proposal to pace the frontier ran into Jensen Huang's argument that the backlash is a hoax and regulation is unnecessary. [TechCrunch](https://techcrunch.com/2026/09/20/is-the-ai-industry-really-ready-to-slow-down/)