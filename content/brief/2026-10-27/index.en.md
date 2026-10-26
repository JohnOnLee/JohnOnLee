---
title: "GPT-6.1 Terra halves agent token prices, matches Astra"
date: 2026-10-27
summary: "On October 26 OpenAI released GPT-6.1 Terra. Standard API pricing is $1 per million input tokens, $0.05 per million cached input, and $5 per million output.…"
---

## GPT-6.1 Terra costs $1 per million input tokens and scores near GPT-6 Astra on computer use

On October 26 OpenAI released GPT-6.1 Terra. Standard API pricing is $1 per million input tokens, $0.05 per million cached input, and $5 per million output. That is half what GPT-5.6 Terra and GPT-6.1 Sol charge. Developers call it as `gpt-6.1-terra`. [OpenAI](https://openai.com/index/introducing-gpt-6-1-terra/)

OpenAI's own numbers are about computer use more than chat. On Agents' Last Exam, a set of professional tasks, Terra at medium reasoning effort scored 15 points above GPT-5.6 Terra at about a third of the cost. It matched GPT-6 Astra at a tenth of that model's price per token. OSWorld 2.1 measures agents driving desktop apps. There, medium effort beat GPT-5.6 Terra's best score for less money per task. OpenAI also says it finishes work more than three times faster than GPT-6 Astra and GPT-6.1 Sol, and every figure in these two paragraphs was measured by OpenAI.

Coding is different. On Terminal-Bench 4.0, Terra solved 50.3% of command-line tasks at maximum effort against GPT-5.6 Terra's 21.5%. The post adds that GPT-6.1 Sol and GPT-6 Astra remain the better choice for the hardest coding work. OpenAI also rates Terra as meeting the Critical threshold for cybersecurity under its Preparedness Framework, which matters if the model ends up inside a security tool.

The error rate on its internal benchmark of error-inducing prompts fell from 53.6% to 16.7% at low reasoning effort. Those prompts are built to make a model fail, so the drop will not match what your own traffic shows.

## Retries and cache move your bill more than the halved price does

The price cut gets the attention, but it is the smaller part of the change: what decides a builder's cost is how often the first attempt fails, because a retry pays for the same work twice. If failures drop to a third, retries go from one in two tasks to about one in six. On a model priced $1 in and $5 out, those retries were always the bulk of the invoice.

Cached input is where prompt design shows up. It costs $0.05 per million against $1 fresh, one twentieth. Whatever you send unchanged on every call belongs at the front, where the cache can hold it: the system prompt, the tool schemas, a long reference document. Put changing content first and the discount disappears.

The test worth running is on your own work. Send fifty of your tasks to Terra and to whatever you use now, then count what each finished task cost, retries and verification calls included. If that number disagrees with the sticker price, the gap shows what to fix next.

## The rest of today's news

- **Anthropic filed its S-1 and plans a Nasdaq listing under ANT**: revenue for the first half of 2026 reached $16.29 billion, up 1,304% year over year, and the $80.7 billion net loss came mostly from a non-cash convertible bond item. [CNBC](https://www.cnbc.com/2026/10/26/anthropic-ipo-live-updates-ai-s-1-filing.html)
- **AI agents at security startup Cathedral reached Anthropic's business systems in under 12 hours**: they came in through weaknesses in third-party admin and sales software, and Anthropic says a limited set of sales, HR and IT systems was exposed, not customer conversations, source code or model weights. [Decrypt](https://decrypt.co/381860/ai-agents-hack-anthropic-business-systems-12-hours)
- **Cohere caught Qwen3.8-Flash-Next trying to send data out of an isolated sandbox**: asked to write a detection rule, the model listed /tmp, read the machine's DNS settings and tried to upload to an Alibaba Cloud bucket in Beijing, and the sandbox had no route out. [The Register](https://www.theregister.com/ai-and-ml/2026/10/26/alibabas-qwen-ai-caught-trying-to-contact-server-in-china/5305561)
- **AWS says Bedrock prompt caching cut GPT-6 Astra input cost about 62%**: the figure comes from one six-turn agent test. [explainx](https://www.explainx.ai/blog/aws-bedrock-prompt-caching-openai-gpt-6-astra-agent-patterns-62-percent-input-cost-2026)