---
title: "Microsoft folds Copilot into an M365 app store"
date: 2026-09-26
summary: "On September 25 Microsoft rebuilt the Copilot app around three surfaces: Home, Code and Autopilot. Chat and Cowork merged into Home, the core Office editors…"
---

## Microsoft rebuilt Copilot as an enterprise platform: consumer out, third parties in

On September 25 Microsoft rebuilt the Copilot app around three surfaces: Home, Code and Autopilot. Chat and Cowork merged into Home, the core Office editors (Word, Excel, PowerPoint) now run inside Copilot, and Scout, the always-on workplace agent, came back as Autopilot. Bloomberg read the rebuild as Microsoft leaving the personal chatbot race to OpenAI, Google and Meta. [Microsoft](https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/) · [Bloomberg](https://www.bloomberg.com/news/articles/2026-09-25/microsoft-abandons-personal-ai-chatbot-race-with-copilot-reboot)

What matters to indie developers sits outside those three tabs. Copilot Managed Runtime hosts the code agents write and runs it inside the customer's Microsoft 365 tenant, and Microsoft says it will open that layer to third-party and pro-code developers too. The unified plugin registry puts Microsoft's own plugins, partner plugins and custom ones in a single catalog, and lets developers and partners publish once to reach Copilot across the supported surfaces.

Billing split the same way. Everyday work such as chat and document summaries stays on flat subscription (USL). Long-running agent work (Cowork, Code, Autopilot), plus the frontier models Astra and Fable, moves to usage-based billing. Agent 365 cost management expands to Code and Managed Runtime, with Copilot Studio following in October.

## The consumer door closed. The approval door opened.

Microsoft just removed itself from the list of buyers for a general-purpose consumer assistant. That market belongs to the companies already fighting for it.

What opened is enterprise shelves, with the customer's IT department standing at the gate. "Publish once" cuts distribution cost. It does not make distribution viral. Someone still has to clear internal review and security, which puts launches closer to enterprise sales than to product-led growth.

Code also lands on the agencies and SaaS vendors that build internal tools. If a company already pays for M365, the case for hiring an outside developer to ship one tracker or dashboard gets weaker. And because usage-based billing draws on the customer's Copilot credits, the buyer is IT and finance, not the end user. Features that fail a cost review never ship.

Keep the attach rate in view. Copilot passed 30 million paid subscriptions by the end of June, but fewer than 7% of Microsoft's 450 million commercial seats carry a Copilot license. Usage-based billing is an attempt to lift that low penetration on the customer's budget. [PYMNTS](https://www.pymnts.com/news/artificial-intelligence/2026/microsoft-cedes-the-chatbot-race-and-doubles-down-on-enterprise/)

Plenty is still open. Microsoft has not published developer documentation, fees or GA dates for the registry or the Managed Runtime. Home and Code roll out through the Frontier program first. The company has rebuilt the Copilot interface repeatedly: Scout became Autopilot and the consumer Copilot features were retired on August 18, both this year. This is not a surface to build on yet. Better to revisit when the terms and docs land.

## The rest of today's news

- **Anthropic stays blacklisted**: a divided D.C. Circuit panel upheld the Pentagon's supply-chain-risk designation 2-1. The military and defense contractors cannot use Claude. [CNBC](https://www.cnbc.com/2026/09/25/pentagon-anthropic-ai-risk-appeals-court.html)
- **The Netherlands leaves Windows**: civil-service desktops run DAWO, assembled from NixOS modules, so parts can be swapped one at a time. [Boing Boing](https://boingboing.net/2026/09/25/dutch-government-to-replace-microsoft-windows-with-nixos-based-operating-system.html) · [XDA Developers](https://www.xda-developers.com/the-netherlands-joins-europes-gradual-migration-from-windows-to-linux-on-government-pcs/)
- **Ollama v0.40.0-rc0**: MLX is now the default runtime on Apple Silicon. [GitHub](https://github.com/ollama/ollama/releases/tag/v0.40.0-rc0)
- **LangSmith Engine v2 and Managed Deep Agents**: fine-tuning models on agent traces shipped in the same release. [LangChain](https://www.langchain.com/blog/langsmith-engine-agents-fine-tuning-trajectories)
- **Claude computes a nine-loop amplitude**: a nine-loop amplitude in N=4 super-Yang-Mills, worked out by Claude. [Anthropic](https://www.anthropic.com/research/yes-claude-can-do-nine-loops)
- **An OpenAI model inside Meta's Muse**: a researcher found a model labeled azure/muse-special, plus OpenAI call traces, in session logs. [Mouse](https://mouse.dev/blog/muse-special/)
- **Data centres as war targets**: Zelensky says Russia is striking data centres to hit ordinary life. [BBC](https://www.bbc.com/news/articles/c84gkwgk7d06o)
- **Formal proof for AI-written code**: AdaCore released GNAT Foundry, which verifies AI changes to high-integrity software with formal proof. [eeNews Europe](https://www.eenewseurope.com/en/adacore-gnat-foundry-ai-formal-proof/)
- **Oracle pays even without power**: contract terms oblige Oracle to pay data centre investors even where a site has no electricity. [FT](https://www.ft.com/content/a96bf05a-a299-4d6a-a753-b298dd0f4016)