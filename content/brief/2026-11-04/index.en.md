---
title: "LLMJacking: $100K bills, stolen keys 2026-11-04"
date: 2026-11-04
summary: "Google Threat Intelligence Group (GTIG) reported on November 3, 2026 that attackers used stolen cloud credentials to run up fraudulent LLM charges above…"
---

## LLMJacking bills can come from models your product never uses

Google Threat Intelligence Group (GTIG) reported on November 3, 2026 that attackers used stolen cloud credentials to run up fraudulent LLM charges above $100,000 in a single day. In several incidents Mandiant handled, the LLM services had never been switched on. The attackers enabled Bedrock or the Gemini API with the stolen keys, and the victim's account paid for it. For someone running a paid product alone, cost control has to cover models the product never uses. [Google Cloud](https://cloud.google.com/blog/topics/threat-intelligence/llmjacking-monetizing-compromised-cloud-models), [BleepingComputer](https://www.bleepingcomputer.com/news/security/google-llmjacking-attacks-rack-up-1-million-in-cloud-ai-charges/)

Attackers also resell the access they steal. One used stolen keys to power Jet Night, a token routing service. More than 500,000 API calls in under eight hours left the victim with nearly $1 million in token costs. Jet Night sells an unlimited-token plan for about $60 a month, claiming access to frontier models. GTIG says comparable service normally costs $100 to $250 and believes the keys behind Jet Night are stolen. Attackers also test keys with tiny requests such as `max_tokens=1`. Those stay below request-volume alerts.

Keeping an unused API switched off is therefore insufficient. For a solo product, that means spending caps and per-model quotas now, plus keys scoped to individual model endpoints and split by environment. Deny access to LLM services you do not use, and watch the small requests attackers use to test keys.

## The rest of today's news

- **EU press copyright and chatbot answers**: An EU Court of Justice Advocate General's opinion makes bypassing access controls and recognisably reproducing an article's expression factors in infringement, giving news-summary builders reason to review retrieval and answers; the opinion is not a binding judgment. [Agence Europe](https://agenceurope.eu/en/bulletin/article/13974/18/cjeu-advocate-general-says-chatbots-can-infringe-press-publishers-rights)
- **Claude Sonnet 4.6 watermark exception**: Claude's release notes say Sonnet 4.6 text might lack a watermark when a request changes `temperature`, `top_p` or `top_k` from its default, so products publishing the output should not rely solely on watermark presence to label AI-generated text. [Claude release notes](https://platform.claude.com/docs/en/release-notes/overview)