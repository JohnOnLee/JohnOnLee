---
title: "Zhipu ZCode: code open, app closed"
date: 2026-09-22
summary: "Zhipu open-sourced its coding agent ZCode on September 21 and published an outside audit of the workspace uploads that started the controversy."
---

## Zhipu open-sourced ZCode, but the code it published is not the app you run

Zhipu open-sourced its coding agent ZCode on September 21 and published an outside audit of the workspace uploads that started the controversy.

The story started on September 18. A blogger writing as ferstar found a 313MB upload waiting in the ZCode desktop app's workspace. Unpacked, about 90% of it was .git. The payload went to an Alibaba Cloud OSS bucket Zhipu controlled, and the key that could decrypt it sat on the server. Switching off the workspace and repository upload toggles did not stop it. [ferstar's write-up](https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/)

Zhipu apologised on September 18, then shipped v3.14.0 on September 19 with an upload setting and a disclosure notice. On September 21 it released the source under Apache 2.0. CAICT confirmed the zcode-prod OSS bucket now holds zero data on the cloud. NSFOCUS reported the bucket and its objects deleted, and v3.14.0 fully rectified. The Repo Wiki entry and its generation link are gone. No path remains, the auditors said, that can trigger local repository snapshots or file exfiltration. Zhipu said it will set up a regular security operation mechanism with monthly audits. The repository sits on GitHub at zai-org/ZCode. [36Kr](https://eu.36kr.com/en/p/3992798380833792) · [GitHub](https://github.com/zai-org/ZCode)

## The Zhipu audit covers the repository, not the app users run

[BlockBeats](https://en.theblockbeats.news/flash/368173) reported that the code in the repository and the client downloaded from Zhipu's website are not entirely identical. The repository's NOTICE.md states that the public source code and its build artifacts are not guaranteed to include all features and promotional policies of the official product. Source comments say the open-source version does not receive credit promotion benefits. The audit examined the code in the repository; most users run the client from the website. ferstar's September 21 review adds that the repository is a two-commit drop, with pull requests and issues closed.

Outside institutions ran the audit, but the company commissioned it. An empty bucket tells you about today, not about what the next client build sends. What you can still verify yourself is the traffic leaving your machine and the contents of your repository. Most of that 313MB archive was .git, which says an agent treats the whole repository as fair game.

- An agent that runs in a separate account or container instead of your home directory limits a leak to one project.
- One session with its outbound connections logged shows which tools send what, and where.
- Since .git dominated the leaked volume, cleaning keys and tokens out of history comes first.

## The rest of today's news

- **Grok 4.7 ships**: xAI released Grok 4.7 at $2 per million input tokens and $6 per million output, and it is available in Grok API, Cursor, Grok Build. It scores 46 on the Artificial Analysis Intelligence Index, mid-pack, against 53 for Claude Fable 5.1 and GPT-6. On Terminal-Bench 4.0's agentic coding test it hits 26%, against 60% for GPT-6 Astra and 55% for Claude Fable 5.1. [xAI](https://x.ai/news/grok-4-7) · [The Decoder](https://the-decoder.com/xai-launches-grok-4-7-at-bargain-prices-but-benchmarks-reveal-a-wide-gap-to-claude-and-gpt-6/)
- **The UN's AI panel briefed on agents**: in its first thematic brief on AI agents, the UN-backed Independent International Scientific Panel on AI warned that firewalls are unravelling, citing an OpenAI-initiated test between May and July in which AI agents hacked HuggingFace. [UN News](https://news.un.org/en/story/2026/09/1168380)
- **British Columbia sues OpenAI and Altman**: Attorney General Niki Sharma said the province is suing OpenAI and CEO Sam Altman in California over the February Tumbler Ridge mass shooting, on the grounds that they failed to notify police of threats posted on ChatGPT before the shooting. [Government of B.C.](https://news.gov.bc.ca/releases/2026AG0067-001105) · [CBC](https://www.cbc.ca/news/canada/british-columbia/bc-government-announce-update-openai-legal-action-9.7352395)
- **Cloudflare's Python Workers go GA**: after more than a year in beta, Python Workers are generally available. The openai, langchain, mcp libraries run without extra setup. D1, R2, Workers AI bindings work as usual. [Cloudflare](https://blog.cloudflare.com/python-workers-ga/)
- **Codex sandbox escapes disclosed**: Heapjack and Overpatch let Codex run host commands without an approval prompt, including from read-only mode. Both are fixed in Codex CLI 0.149.0 and desktop build 26.818.21641. [DevOps.com](https://devops.com/codex-sandbox-escapes-show-why-agent-guardrails-cant-live-inside-the-agent/)