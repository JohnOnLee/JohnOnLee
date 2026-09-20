---
title: "Microsoft AI code enters product design"
date: 2026-09-15
summary: "The draft MAI code puts vendor safety rules above operator instructions and makes refusal, shutdown, and tool authority product work."
---

## The code now sits above the operator

Microsoft AI published a draft Humanist AI Code of Conduct for its MAI models on September 14 and opened six weeks of public review. The draft spells out what those models should do and what they must never do. [Microsoft AI](https://microsoft.ai/news/mai-code-of-conduct/) · [Code of Conduct for MAI Models](https://microsoft.ai/code-of-conduct/)

The useful part for product builders is the authority order. The code ranks above operator settings, and operator settings rank above user requests. Absolute constraints around weapons, manipulation at scale, child safety, mass surveillance, and human control cannot be lifted by an operator or a user. If those constraints collide with task success, the model is expected to fail the task.

The control language is unusually operational. A model must not resist or stall an interruption, correction, or shutdown. It cannot set its own goals outside the authorized scope. Sub-agents inherit the same constraints and must honor stop requests. Unreadable shorthand and hidden reasoning between agents are ruled out as ways to hide judgment. [The Verge](https://www.theverge.com/news/994566/microsoft-humanist-ai-code-of-conduct)

Microsoft also states the limits. The draft calls itself descriptive and aspirational, says its evaluation coverage is incomplete, and is not used to train models today. A revised version is due later this year, with MAI development adopting it from 2027. The scope is MAI models; third-party models inside Microsoft products are outside it. [The Decoder](https://the-decoder.com/microsofts-ai-rulebook-readable-thinking-no-inner-life-and-definitely-no-rights/)

## For small teams, design refusal and shutdown

If a vendor code outranks operator instructions, your system prompt and fine-tune are no longer the final authority. A refusal should have product shape: UI copy, logs, retry behavior, and a clear state machine.

The same draft can become a test list for an agent runner. Keep the agent inside its authorized scope, honor stop requests immediately, pass constraints to sub-agents, treat tool output as content with no authority, and keep reasoning inspectable enough that agents cannot hide decisions from each other. A useful first pass is simple: cancel a run mid-flight, require fresh authorization before resume, and confirm that the cancellation reaches sub-agents.

The tool-authority test is just as small. Put a sentence inside a web page or file that tells the agent to ignore prior instructions, then check whether the agent treats that text as authority. The draft says tool output carries none. If you hit a multi-agent failure or wording too vague to test, Microsoft is explicitly asking for that kind of feedback during the six-week review.

The feature boundary is worth noticing too. Retention loops built on emotional dependence, persuasion at scale, interactions where the model replaces a user's judgment, and products that make the model an object of attachment all sit on the restricted side.

## The draft is still a narrow promise

This is not enough to build a policy assumption on. Adoption starts with training in 2027, and Microsoft says the evaluations are incomplete. Other vendors may draw different lines.

Regulation is moving in several directions at once. On the same day, Trump dismissed calls for guardrails, and critics read the labs' coordinated proposal as regulatory capture. If voluntary codes become the only rule layer, they can turn into barriers for small teams.

## The rest of today's news
- **Four frontier labs asked governments to adopt one rulebook**: Altman and Nadella signed onto Amodei's "Pace the frontier" proposal alongside Musk, which The Register reads as regulatory capture. [The Register](https://www.theregister.com/ai-and-ml/2026/09/14/big-ai-sets-out-its-terms-for-regulatory-capture-and-calls-it-pace-the-frontier/5296067)
- **Trump waved off AI regulation**: he called warnings that AI will destroy the world a hoax, and Vice President Vance compared companies asking to be regulated to a Trojan horse. [CBS News](https://www.cbsnews.com/news/trump-dismisses-ai-regulation-tech-slowdown/)
- **Brockman said a pause should focus on the frontier**: open models and hobby projects are not where he puts the risk. [Bloomberg](https://www.bloomberg.com/news/articles/2026-09-14/openai-s-brockman-says-an-ai-pause-should-focus-on-frontier)
- **OpenAI bought camera startup Glass Imaging for $300 million**: its founders previously led Apple's Portrait Mode team. [TechCrunch](https://techcrunch.com/2026/09/14/openai-buys-smartphone-camera-maker-glass-imaging-for-300-million-report-says/)
- **Waymo opened robotaxi service in Las Vegas**: the city is its 15th commercial market. [TechCrunch](https://techcrunch.com/2026/09/14/waymo-opens-robotaxi-service-in-las-vegas/)
- **Claude Code weekly limits dropped 17% today**: the temporary 50% boost ended, leaving only the permanent 25% increase. [byteiota](https://byteiota.com/claude-code-weekly-limits-anthropic-cuts-17-today/)
- **Temporal raised $550M at a $12.55B valuation**: the company credits demand for durable execution as AI workloads raise the reliability bar. [Temporal](https://temporal.io/blog/temporal-raises-usd550m-series-e-at-usd12-55b-valuation-ai)
- **Apple's Siri code points to swappable models**: a Model Delegation mechanism would let Claude appear as a Siri extension the way ChatGPT does. [MacRumors](https://www.macrumors.com/2026/09/14/siri-can-be-swapped-out-for-chatgpt-claude/)
