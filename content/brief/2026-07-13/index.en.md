---
title: "AI / Startup Morning Brief — 2026-07-13"
date: 2026-07-13
summary: "Claude Code burns 33K tokens before reading your prompt — OpenCode uses just 7K: Systima's empirical benchmark reveals Claude Code consumes 33,000 tokens before even reading the u…"
description: "Claude Code burns 33K tokens before reading your prompt — OpenCode uses just 7K: Systima's empirical benchmark reveals Claude Code consumes 33,000 tokens before even reading the u…"
---

[AI/Startup Morning Brief — 2026-07-13]

## Key Shifts
- **Claude Code burns 33K tokens before reading your prompt — OpenCode uses just 7K**: Systima's empirical benchmark reveals Claude Code consumes 33,000 tokens before even reading the user's prompt, compared to 7,000 for OpenCode under identical conditions. The gap widens further when instruction files, MCP servers, and subagents are added. For teams deploying coding agents in production, token efficiency is becoming a critical infrastructure cost variable. [Systima](https://systima.ai/blog/claude-code-vs-opencode-token-overhead)
<!--more-->
- **George Hotz: "I love LLMs, I hate hype"**: The renowned hacker and AI founder published a calibrated take on the state of AI — genuinely excited about LLMs, self-driving cars, video generation, and coding agents, while rejecting both the "window is closing" FOMO narrative and the "AI doom" rhetoric. A signal for builders to stay grounded between extremes. [geohot](https://geohot.github.io/blog/jekyll/update/2026/07/12/i-love-llms.html)
- **Uber lobbies to keep robotaxi rides 85% human — a regulatory battle line forms**: Documents obtained by Wired show Uber is pushing New Jersey lawmakers to mandate "hybrid networks" where human drivers operate alongside autonomous vehicles. The proposed framework advantages existing ride-hailing platforms over pure-play AV developers. Mobility and autonomous vehicle founders should watch whether this regulatory blueprint spreads to other states. [Wired](https://www.wired.com/story/ubers-autonomous-vehicle-strategy-slow-their-adoption/)

## Startup / Product / Platform Radar
- **LARP — Revenue infrastructure for serious founders**: A new revenue and sales infrastructure tool purpose-built for founders, designed to replace spreadsheets and fragmented toolchains. Gained attention with 97 points on Hacker News. [LARP](https://www.larp.website/)
- **The State of MCP Security 2026 — first structured security assessment**: Canopii published the first systematic security evaluation of the Model Context Protocol (MCP). As MCP becomes the de facto standard for AI-tool integration, the emergence of security audits signals ecosystem maturation. [Canopii (HN)](https://news.ycombinator.com/item?id=48884647)
- **Adaptive Recall — MCP-based persistent memory for AI**: A memory system that goes beyond vector search by applying cognitive science models, connecting to AI assistants via the MCP protocol. [Adaptive Recall](https://www.adaptiverecall.com/)
- **Capn-hook — stop coding agents from repeating the same searches**: A CLI tool that prevents coding agents from redundantly searching for information they've already found, addressing a tangible workflow pain point. [GitHub](https://github.com/cyrusNuevoDia/capn-hook)

## AI Future Signals
- **Token efficiency emerges as a competitive axis in the coding agent market**: The 4.7x token overhead gap between Claude Code and OpenCode signals that the coding agent market is shifting from feature differentiation to infrastructure cost efficiency. At tens of thousands of wasted tokens per session, organizations with hundreds of developers could see annual cost differences in the millions. [Systima](https://systima.ai/blog/claude-code-vs-opencode-token-overhead)
- **The MCP ecosystem is crossing from experiment to production**: The same day brought an MCP security audit, an MCP-based memory service, and MCP developer utilities — a cluster of signals that the protocol ecosystem is maturing rapidly. The infrastructure layer connecting AI agents to tools and data is taking shape. [Canopii (HN)](https://news.ycombinator.com/item?id=48884647) · [Adaptive Recall](https://www.adaptiverecall.com/)

## Realistic Opportunities / Experiments
- **Token overhead optimization tools or services**: As Systima's benchmark demonstrates, tools that track and optimize coding agent token consumption are likely to see team-level adoption. A SaaS product packaging instruction file optimization, context window management, and MCP server tuning could deliver concrete cost savings. [Systima](https://systima.ai/blog/claude-code-vs-opencode-token-overhead)
- **MCP security scanner / audit tooling**: As more organizations deploy MCP servers, automated vulnerability scanning and auditing tools for MCP connections represent an emerging niche. Canopii's first assessment validates demand for this category. [Canopii (HN)](https://news.ycombinator.com/item?id=48884647)

## Uncertainties / Keep Watching
- **State-level spread of robotaxi hybrid-network regulation**: If Uber's New Jersey lobbying succeeds, similar "hybrid network" bills are likely to appear in other states. This marks the beginning of an open power struggle between autonomous vehicle developers (Waymo, Tesla) and incumbent ride-hailing platforms. [Wired](https://www.wired.com/story/ubers-autonomous-vehicle-strategy-slow-their-adoption/)
- **Direction of coding agent token efficiency competition**: Is Claude Code's 4.7x token surplus a philosophical design choice or simply optimization debt? Whether Anthropic closes the gap or the paradigm of "more context = better results" prevails will determine the cost trajectory for coding agent adoption at scale. [Systima](https://systima.ai/blog/claude-code-vs-opencode-token-overhead)