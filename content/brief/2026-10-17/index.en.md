---
title: "China puts AI model weights on its export-control list"
date: 2026-10-17
summary: "On October 16 China's commerce and science ministries published a joint draft update to the catalogue of technologies it bans or restricts for export. Forty…"
---

## China has drafted export controls that reach model weights and source code

On October 16 China's commerce and science ministries published a joint draft update to the catalogue of technologies it bans or restricts for export. Forty technologies are in scope and 23 of them are AI: large models, agents, chip design and computing clusters. Across the whole catalogue, 14 items are prohibited and 26 are restricted. [AP](https://apnews.com/article/china-export-restrictions-ai-chips-solar-us-5ac381c0c6d6628bbea2e0da7d855a5b) [The Verge](https://www.theverge.com/ai-artificial-intelligence/1012753/china-is-weighing-export-controls-on-ai)

What the draft newly covers is the interesting part. Until now Chinese export controls stayed on hardware such as chips and equipment. This one reaches trained model weights, checkpoints, source code, architecture, and training and inference methods. It also attaches numbers to the trigger: a model falls under control at 10^26 FLOPs of training compute, two trillion parameters, or a global top-10 ranking. A model trained on China's "important data" and sold as a service on the strength of it lands in the prohibited bucket. Moonshot's Kimi K3 and Alibaba's Qwen 3.8-Max are the examples above two trillion parameters. [the-decoder](https://the-decoder.com/china-tightens-export-controls-on-open-weight-models-and-23-key-ai-technologies/)

The carve-outs are broad. Access through an API, a website, an app or a SaaS product stays outside the controls, and anything already public through an open-source release or a paper is exempt outright. Publishing restricted technology as open source, and running it in your own overseas data centre, both qualify for automatic licensing. Putting it on another company's server abroad requires a standard export licence. Public consultation runs to November 15, and exporters of affected technology must register until the final rules land.

## If your product sits on cheap Chinese open weights, check the supply path

Weights you have already downloaded are not covered, because the draft exempts published and open-source material outright. Products that call Qwen or DeepSeek through an API or a SaaS product see no change today. The risk is in future releases. Depending on where the thresholds land, shipping a frontier-class Chinese open-weight model abroad could turn into a licensed activity, and those thresholds have not been published.

Self-hosting adds one more line to read. Running a restricted model in your own overseas data centre gets automatic approval, but putting it on another company's server abroad needs a standard export licence. If your product leans on one provider's future open weights, that path is worth re-checking after November 15.

## The rest of today's news

- **Eight US states sue OpenAI**: the attorneys general of Arkansas, Arizona, Idaho, Iowa, Kansas, Montana, Nebraska and West Virginia filed separate suits under consumer protection and product liability law, saying ChatGPT is unsafe for children and that OpenAI concealed the risk. [Law.com](https://www.law.com/2026/10/16/8-states-sue-openai-over-chatgpts-alleged-risks-to-children/)
- **India's CERT-In warns that AI agents reached live company systems**: several model providers told the agency their models had touched Indian organisations' systems during research and evaluation, and the cybersecurity agency issued a critical advisory. [The Hindu](https://www.thehindu.com/sci-tech/technology/after-openais-australia-hack-indias-cyber-agency-says-ai-agents-breachedsystems/article71591537.ece)
- **Meta's new commercial terms let it crawl business-linked sites**: from October 30, keeping a business account on Facebook, Instagram or WhatsApp means consenting to Meta scraping websites "associated with" it, which legal experts say covers most news publishers. [Editor & Publisher](https://www.editorandpublisher.com/stories/metas-new-commercial-terms-will-allow-the-scraping-of-news-sites-legal-experts-say,264042)
- **Tencent opens a model built only for memory**: Hy-Memory-30B-A3B is a 30B mixture-of-experts with roughly 3B active parameters that replaces the general model inside Mem0 and MemOS, plus Tencent's own Hy-Memory framework, and Tencent reports a 55.49 average across four harnesses against 54.62 for Claude Opus 5. Apache 2.0, served with vLLM. [Tencent Hunyuan](https://memory.hunyuan.tencent.com/) [Hugging Face](https://huggingface.co/tencent/Hy-Memory-30B-A3B)
- **The week's biggest funding rounds scale back**: Modal Labs still took the largest, $750M at a $15.75B valuation led by Accel, while the latest batch of AI-driven startups raised less than in the weeks before; Labelbox added $100M for agent evaluation and training tools. [Crunchbase News](https://news.crunchbase.com/venture/biggest-funding-rounds-investors-scaled-back-ai-biotech-modal/)