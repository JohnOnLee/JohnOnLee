---
title: "DeepSeek open-sources DeepInfer as Washington orders it out"
date: 2026-10-21
summary: "On October 20 DeepSeek published DeepInfer, the in-house inference framework behind its own services, on GitHub under the Apache 2.0 licence."
---

## DeepSeek put the engine it runs in production on GitHub under Apache 2.0

On October 20 DeepSeek published DeepInfer, the in-house inference framework behind its own services, on GitHub under the Apache 2.0 licence. [GitHub](https://github.com/deepseek-ai/DeepInfer)

For now it serves one model, DeepSeek-V4.1-Flash. It runs on Nvidia SM100 GPUs and Huawei Ascend 950 NPUs. The stack was built mainly on vLLM, with ideas taken from SGLang and Nvidia's TensorRT-LLM. The vLLM project thanked DeepSeek for crediting the community. [The Next Web](https://thenextweb.com/news/deepseek-deepinfer-open-source-inference-engine)

It splits inference work across many chips. Speculative decoding drafts several tokens ahead and verifies them in one pass. Outputs stay consistent from run to run, and answers get forced into set formats. The performance figures are DeepSeek's own: prompt processing measured on four SM100 GPUs, output generation on 64. No independent benchmark exists yet. [TechTarget](https://www.techtarget.com/ai/news/366652363/DeepSeek-makes-DeepInfer-open-source-to-cut-AI-costs) [Bloomberg](https://www.bloomberg.com/news/articles/2026-10-20/deepseek-unveils-open-source-tool-to-help-cut-ai-operating-costs)

## The same week, Washington told federal civilian agencies to rip DeepSeek out

DHS directed federal civilian agencies to stop using DeepSeek technology and to remove what is already installed. The order appeared in the Federal Register on October 20. Its wording is broad: it covers "all DeepSeek and DeepSeek-affiliate products, and third-party products and services developed using DeepSeek implementations." [The Register](https://www.theregister.com/security/2026/10/20/deepseek-deep-sixed-at-all-us-federal-civilian-agencies/5304010) [Federal Register](https://www.federalregister.gov/documents/2026/10/20/2026-21447/notice-of-order-regarding-exclusion-and-removal-of-deepseek-products-from-federal-civilian-executive)

What counts is unclear. The order does not say whether "developed using" means calling DeepSeek models through an API or building an app with DeepSeek's help. Gateways make it messier. OpenRouter and Vercel AI Gateway pick a provider for you by default, so a request can reach a DeepSeek model without anyone choosing it.

Two things are worth pinning down on your side: what you pay, and who you depend on. Route through a gateway and you should name the providers explicitly. Sell into US public sector or regulated markets and you should check your configuration and your contracts for which model runs where. The open release and the procurement order landed in the same week. A long single-vendor commitment is harder to justify on price alone now.

## The rest of today's news

- **MiniMax ships M3.1 Flash**: the company says agentic workloads cost 70% less than with its predecessor, at $0.15 per million input tokens and $0.60 output. "Space Bunny," the anonymous model that processed more than 200 trillion tokens, was an early version of it. [MiniMax](https://www.minimax.io/blog/minimax-m31f)
- **Anthropic's S-1 shows a first-half net loss above $80 billion**: the updated filing says the company may spend as much as $750 billion on computing. [WSJ](https://www.wsj.com/tech/ai/anthropic-revenue-growth-ipo-accaf0f1) [Channel News Asia](https://www.channelnewsasia.com/business/anthropic-logged-net-loss-over-80-billion-in-first-half-2026-wsj-reports-6476676)
- **OpenAI's GPT-6.1 Sol scores 97.9% on its COBOL migration eval**: up from 5.4%, and 86.6% at low reasoning effort. [Dataconomy](https://dataconomy.com/2026/10/20/openai-gpt-6-cobol-coding-migration-gains/) [OpenAI](https://openai.com/index/low-resource-programming-languages/)
- **ByteDance, Alibaba and Tencent order more than $35 billion of Nvidia chips**: over 3 million RTX PRO 5500 cards at about $11,400 each. [The Edge Malaysia](https://theedgemalaysia.com/node/822533)
- **Spotify removed 50 million AI slop and spam tracks from recommendations**: the company also changed its recommender to favour human artists. [The Verge](https://www.theverge.com/entertainment/1014284/spotify-ai-slop-spam-songs-removed)
- **Britain's FCA wants AI failures and near-misses reported**: the regulator says incident reporting must extend to significant AI failures as agents get more autonomous. [The Register](https://www.theregister.com/ai-and-ml/2026/10/20/uk-finance-watchdog-wants-firms-to-report-ai-failures-and-close-calls/5304078)