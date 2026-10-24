---
title: "Brotli CVE-2026-111497: each runtime patched separately"
date: 2026-10-25
summary: "Node.js disclosed CVE-2026-111497 in its October 21 security release. It is an out-of-bounds write in the Brotli decoder that Node.js bundles. An app that…"
---

## Brotli CVE-2026-111497 was fixed in February and shipped in October

Node.js disclosed CVE-2026-111497 in its October 21 security release. It is an out-of-bounds write in the Brotli decoder that Node.js bundles. An app that decompresses Brotli data an attacker controls can have its process memory corrupted or its code run by someone else, and Node.js lists remote code execution as a possible result. The fixes are in 22.23.4, 24.22.1 or 26.12.1. OpenAI's Codex Security team reported it. [Node.js](https://nodejs.org/en/blog/vulnerability/october-2026-security-releases)

The flaw does not sit inside Node.js alone. Google shipped Brotli 1.2.1 on October 21 and named this CVE as its security fix. GitHub's advisory says the Python packages brotli (below 1.2.1) and brotlicffi (below 1.2.1.0) carry the same bug. Python HTTP clients such as requests, httpx or aiohttp decompress Brotli automatically whenever those packages are installed. [GitHub advisory](https://github.com/advisories/GHSA-9v8h-qqgm-4m35)

On October 23 the security firm Aikido renamed it HTTP2Shell and worked out how far it reaches. Every runtime, proxy or gateway that bundles Brotli is in scope. The patch list now includes Bun 1.4.4, Envoy, Istio, curl. The list is still growing. The line that matters more to a builder sits elsewhere in Aikido's post. As of October 23 the advisory databases had not mapped this CVE to the PyPI packages, so pip-audit, Dependabot or Safety would not flag a vulnerable version. [Aikido](https://www.aikido.dev/blog/python-packages-vulnerable-node2shell-brotli-cve-2026-111497)

The root-cause fix is older than the disclosure. Aikido reports that it landed in Brotli's source in February, where nobody treated it as a security issue. The release carrying it was 1.2.1 on October 21. For eight months the same decoder shipped unchanged in Node.js, Bun, the Python packages. Vercel put WAF rules in front of the inbound path on October 21, with the caveat that the rules do not replace patching. [Vercel](https://vercel.com/kb/bulletin/node-js-security-advisory)

## Your scanner will not flag this one, so check the runtime version

Brotli has to reach your code in one of three ways. A server can inflate an incoming request body, which is what happens in an Express 5 setup with body-parser 2.x. It also arrives when your own code decompresses a Brotli response it fetched from somewhere else, and any direct node:zlib call feeds the decoder by hand. All three land in the same bundled decoder, which makes the runtime version the thing to check. Managed platforms that ship their own runtime can lag upstream, so check the version your provider runs as well as the one pinned in your repository. A container image keeps its old runtime until you rebuild it. Brotli responses fetched from other servers never pass your WAF. Node.js 20.x and older are end-of-life and get no fix.

Three checks for today:

- Run `node --version` on CI runners, container images or local machines. Move to 22.23.4, 24.22.1 or 26.12.1, then rebuild the images.
- Python projects: move to brotli 1.2.1 or brotlicffi 1.2.1.0 and up. Your scanner will not tell you.
- If you cannot upgrade yet, reject requests with `Content-Encoding: br` at the reverse proxy or middleware. Fetched Brotli responses stay uncovered.

## The rest of today's news

- **Block released Dessa, a speech model trained only on voice**: a full-duplex speech model trained from scratch on recordings of human conversation, with no text anywhere in the pipeline. It runs locally on a MacBook Pro M4 Max. Block published demo recordings instead of benchmarks and opened a waitlist. [TechCrunch](https://techcrunch.com/2026/10/24/blocks-new-voice-model-sounds-eerily-human/)
- **Moonshot cut the hacking ability of Kimi K3.1 Pro before release**: on October 24 Moonshot said it reduced the cyber-offensive capability of its newest model during training, ahead of the promised weight release. [Reuters](https://www.reuters.com/technology/moonshot-curbs-hacking-ability-new-kimi-model-fears-grow-over-ai-powered-2026-10-24/)
- **Apollo: no AI payoff outside the tech sector yet**: chief economist Torsten Slok wrote on October 24 that revenue per worker and profit margins are rising for the Mag 7 and flat for the S&P 493. [Apollo](https://www.apollo.com/wealth/insights-news/insights/daily-spark/no-signs-of-ai-payoff-outside-the-tech-sector)
- **Replit moved most of its AI spend from Anthropic to OpenAI**: per The Information, a deal worth more than $100M a year after OpenAI offered 30% or more off, while Anthropic discontinued its own discount. [Techmeme](https://www.techmeme.com/261024/p8)
- **Claude Code v2.1.310 shipped**: the Monitor tool and plugin monitors now run on Bedrock and Vertex, plus Foundry. [GitHub](https://github.com/anthropics/claude-code/releases/tag/v2.1.310)