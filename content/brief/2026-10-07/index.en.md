---
title: "Mistral Large 4: 1T, half price"
date: 2026-10-07
summary: "Mistral opened a public preview of Mistral Large 4 on October 6. The company calls it le Chonk. It is a mixture-of-experts model with 1 trillion parameters and…"
---

## Mistral put a trillion-parameter model on its API today

Mistral opened a public preview of Mistral Large 4 on October 6. The company calls it le Chonk. It is a mixture-of-experts model with 1 trillion parameters and 49 billion active per token, and it takes image input and returns text. Mistral trained it from scratch on 3,800 Nvidia Grace Blackwell GPUs in its own European datacenters. Weights arrive at the end of this month. Until then, the company is red-teaming the model with cybersecurity partners and government bodies, which get it with reduced moderation. [Mistral](https://mistral.ai/news/mistral-large-4)

OpenRouter lists the model at $0.68 per million input tokens and $2.09 per million output. The list price, as measured by Artificial Analysis, is $1.36 in and $4.18 out, against a class median of $2.00 and $10.00. Cached input reads drop 90%, to $0.07 per million. [Artificial Analysis](https://artificialanalysis.ai/models/mistral-large-4)

Vendor claims and independent numbers diverge. Mistral says ML4 is the best open-weight model built in the US or Europe. Artificial Analysis scores the preview 38 on its Intelligence Index, 64th of 225 models. On the same firm's Cyber Index it sits in the top five, and it scores 82% on a test that asks a model to reproduce a real vulnerability and then patch it. Mistral notes that Claude Opus 5.5 and GPT-6 Astra score near zero on that test, because they refuse it.

## If you run agent loops, your cost math changed today

For an agent product, the token price is the product cost. Loops that resend the same context turn input price and cache discounts into margin. The preview is callable today, so you can run your own prompts and evals against it and compare. OpenRouter's price is half the list price, and nobody has said how long that lasts.

The weights matter too. If they land this month, your fine-tune and your eval set stay yours, and there is somewhere to go when a vendor raises prices. That slot has been almost entirely Chinese until now. This is the first European entry at the trillion-parameter scale.

## Self-hosting this is not a laptop job

A trillion parameters is a lot to hold. Even with 49 billion active, you need the full weight set loaded, so a laptop or a single consumer GPU will not run it. This is rented-cluster or on-premise territory, and heavier than Reflection's Beam from yesterday.

There is no license text yet either. Whether it is Apache 2.0 or carries commercial limits depends on the documentation that ships with the weights. Most benchmarks are Mistral's own; the third-party numbers are the Intelligence Index score and the cyber ranking. Sources even disagree on context length. Testing the price today and deciding at the end of the month are separate moves, so there is nothing to settle yet.

## The rest of today's news

- **DeepSeek doubles its round**: it is nearing 80 billion yuan (~$12 billion), with Tencent and CATL among the largest backers, and the total could reach 100 billion yuan ahead of an early 2027 listing. [CNBC](https://www.cnbc.com/2026/10/06/deepseek-funding-round.html)
- **Sierra and Meta open Personal Agent Protocol**: an OAuth-based open standard for how personal AI agents authenticate with businesses, with Walmart, Shopify and Stripe as founding partners and a v0.1 spec due later this month. [Sierra](https://sierra.ai/blog/introducing-personal-agent-protocol)
- **Google becomes anchor customer for US nuclear uprates**: a 20-year deal funds 890 MW of added capacity at Constellation plants, plus a separate 15-year agreement for 2,700 MW. [Google](https://blog.google/company-news/why-were-backing-americas-existing-nuclear-plants/)
- **Korea probes AI-driven bank hacks**: data on about 66,000 people was exposed across seven financial firms, and police assigned 28 investigators to the case. [Korea JoongAng Daily](https://www.koreajoongangdaily.com/korea/lee-orders-dedication-of-personnel-resources-to-handling-hacking-attacks/12906622)
- **EmbeddingGemma 2 ships**: a 740M embedding model that maps text, code, images, video and audio into one vector space, Apache 2.0 and built to run on-device. [Google Developers Blog](https://developers.googleblog.com/en/google-ai-edge-with-embeddinggemma-2/)
- **Kandinsky 6.0 Video goes open source**: 3B and 29B diffusion models that generate 5-second clips with 44 kHz audio, released under MIT. [GitHub](https://github.com/kandinskylab/kandinsky-6)