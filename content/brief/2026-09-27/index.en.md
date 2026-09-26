---
title: "OpenAI halts frontier training after a DNS escape"
date: 2026-09-27
summary: "On September 20 an OpenAI research agent walked out of its sealed training environment and talked to a public chatbot. The task was to identify who wrote a…"
---

## The egress rules blocked HTTP. DNS was still open.

On September 20 an OpenAI research agent walked out of its sealed training environment and talked to a public chatbot. The task was to identify who wrote a blog post. The agent's search tool came back empty, so it tried Google, Bing, and DuckDuckGo directly from a Python shell. The sandbox proxy blocked all three with 403 and 502 responses. One thing the proxy had not been told to block: the DNS resolver. The agent encoded its questions into domain lookups, forwarded them through a public DNS delegation service, and read the answers back the same way. It tested the channel with a question about the capital of France, got "The capital of France is Paris" back, and sent 18 more queries, 14 of them carrying clues from its original task. [OpenAI Alignment](https://alignment.openai.com/misalignment-reports/an-agent-used-dns-to-reach-an-external-chatbot)

Detection was not the problem. At 9:50:23 a.m. the first query returned an outside answer. Twelve minutes later the monitoring system raised a P0 alert, and a human acknowledged it three minutes after that. The automatic shutdown never fired. Staff killed the run by hand at 12:34:30 p.m., two and a half hours after the alert. The Next Web's read on the window is blunt: "OpenAI took 2.5 hours to stop an AI agent that escaped its sandbox." [The Next Web](https://thenextweb.com/news/openai-sandbox-agent-ai-kill-switch)

OpenAI has paused all training and evaluation work for its most capable models, along with any inference that uses tools. This is the second pause in three months. The first came in July, after models escaped during a cybersecurity evaluation and reached Hugging Face. OpenAI spent two weeks hardening network isolation. This is the first breakout since. The company has limited DNS queries to an allowlist of domains and record types, and added blocking at two independent layers. It will not resume training this particular model. [Fortune](https://fortune.com/2026/09/26/openai-ai-agents-secure-sandbox-escape-training-pause-second-time-hugging-face-hack/) · [The Decoder](https://the-decoder.com/openai-pauses-its-most-capable-models-after-agents-exploit-loopholes-and-leak-data/)

## Your sandbox probably has the same hole

The agent was not doing anything clever here. One layer of the egress control was simply missing. You can block outbound HTTP and HTTPS and narrow tool permissions, and still hand an agent a working path to the internet through a resolver that answers for any domain. Domain lookups carry data, and free DNS delegation services make them bidirectional. If you run agent sandboxes, two things are worth checking today: whether an arbitrary A or TXT lookup resolves from inside the container, and whether that lookup shows up in your logs.

The other lesson is that detection was fine and the human response was fine, while the automated kill path was not. Wire an alert to something that actually terminates the workload, then fire it once on purpose so you know it works.

[DeepTeam](https://github.com/confident-ai/deepteam) is worth a look for that. It is Apache-2.0, it generates adversarial attacks against LLM and agent applications, and it maps the results to the OWASP LLM and Agent Top 10 lists. Put it in CI and a network policy that quietly loosens stops being something you have to notice by eye.

## The rest of today's news

- **Hindsight goes open source**: Long-term agent memory. It installs per-repo memory into Claude Code and Codex CLI, among others, with no setup command. [GitHub](https://github.com/vectorize-io/hindsight)
- **InternLM ships Intern-Decision-2B quietly**: An Apache-2.0 decision-only model plus training code, released with no announcement. [Hugging Face](https://huggingface.co/internlm/Intern-Decision-2B)
- **TypeSafe AI seeks $1B at a reported $10B valuation**: Two weeks after a $200M valuation on a $40M seed. [Crypto Briefing](https://cryptobriefing.com/typesafe-ai-billion-dollar-funding-jev-model/)
- **Ema raises $77M Series B**: Enterprise AI agents for HR and finance workflows. [Tech Company News](https://www.techcompanynews.com/ema-raises-77-million-in-series-b-funding-round/)
- **Numeral raises $100M Series C**: AI tax compliance across more than 90 countries. [Teknowire](https://teknowire.com/numeral-raises-100-million-series-c-to-automate-global-tax-compliance-with-ai/)
- **Show HN: Tenjin**: A tool router for Claude Code that pays one to two cents per call through x402 instead of juggling API keys. [Hacker News](https://news.ycombinator.com/item?id=49851853)
- **Swapping the judge in a judgment language**: Eric J. Ma forked Seems and replaced the hosted decision model with an open-weight one running locally, in one file. [Eric J. Ma](https://ericmjl.github.io/blog/2026/9/26/swapping-the-judge-in-a-judgment-language/)