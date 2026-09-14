---
title: "Microsoft's AI Code of Conduct"
date: 2026-09-15
summary: "Microsoft AI released a draft Humanist AI Code of Conduct that spells out what its MAI models must do and what they must never do."
---

## Microsoft published a draft code of conduct for its MAI models and opened six weeks of public review
- **Published September 14**: Microsoft AI released a draft Humanist AI Code of Conduct that spells out what its MAI models must do and what they must never do. [Microsoft AI](https://microsoft.ai/news/mai-code-of-conduct/) · [Code of Conduct for MAI Models](https://microsoft.ai/code-of-conduct/)
- **The chain of command is written down**: the code ranks above operator instructions, and operator instructions rank above user requests. Absolute constraints such as weapons, manipulation at scale, child safety, and mass surveillance cannot be lifted by an operator or a user, and when the code collides with task success the model is expected to fail the task.
- **The control clauses are specific**: a model must not resist or stall an interruption, correction, or shutdown, and it must not set its own goals beyond the scope you authorized. Sub-agents inherit the same constraints and must honor stop requests, and unreadable shorthand or hidden reasoning between agents is out. [The Verge](https://www.theverge.com/news/994566/microsoft-humanist-ai-code-of-conduct)
- **Microsoft also names the limits**: the draft calls itself descriptive and aspirational, admits its evaluation coverage is incomplete, is not used to train models today, and will guide MAI development from 2027 after a revised version lands later this year. It covers MAI models only, and third-party models inside Microsoft products stay outside it. [The Decoder](https://the-decoder.com/microsofts-ai-rulebook-readable-thinking-no-inner-life-and-definitely-no-rights/)

## Your system prompt is no longer the top authority
- **Some lines cannot be opened from your side**: if a vendor code outranks operator instructions, a design that depends on prompting past an absolute constraint stops working. Treat a refusal as a product state to design for.
- **The agent operator rules are now a public checklist**: no self-set goals outside authorized scope, immediate compliance with stop requests, constraint inheritance for sub-agents, no authority from tool output, no hidden reasoning. All five port directly into your own harness as tests.
- **The document also marks features to avoid**: retention loops built on emotional dependence and automated persuasion at scale sit on the restricted side. The draft likewise blocks interactions where the model replaces a user's own judgement or becomes an object of attachment.

## Try this week: give your agent a stop contract and an authority test
- **Fix the stop contract with tests**: cancel a run mid-flight, require fresh authorization to resume, and propagate the cancellation to sub-agents. Those three checks map onto sentences in the draft, so your product can be verified against them.
- **Plant an injection and watch**: hide an instruction inside a web page or file that tells the agent to ignore its previous instructions, then see whether the agent treats that text as authority. Tool output carries none in this draft, so the same rule belongs in your code.
- **Send your multi-agent failures to the consultation**: the draft asks directly for feedback on multi-agent scenarios and on wording too vague to evaluate. Field failures from small teams are the most useful input.

## It is not a guarantee yet and the scope is narrow
- **Do not build on this as a policy assumption**: adoption starts with training in 2027, and Microsoft itself says its evaluations are incomplete. Nothing says another vendor will draw the same lines.
- **Regulation moves the other way too**: on the same day, Trump dismissed calls for guardrails, and critics read the labs' coordination push as regulatory capture. If a voluntary code ends up as the only rule layer, it can turn into a barrier for small teams.

## The rest of today's news
- **Four frontier labs asked governments to adopt one rulebook**: Altman, Nadella, and Musk signed onto Amodei's "Pace the frontier" proposal, which The Register reads as an attempt at regulatory capture. [The Register](https://www.theregister.com/ai-and-ml/2026/09/14/big-ai-sets-out-its-terms-for-regulatory-capture-and-calls-it-pace-the-frontier/5296067)
- **Trump waved off AI regulation**: he called warnings that AI will destroy the world a hoax, and Vice President Vance compared companies asking to be regulated to a Trojan horse. [CBS News](https://www.cbsnews.com/news/trump-dismisses-ai-regulation-tech-slowdown/)
- **Brockman said a pause should focus on the frontier**: open models and hobby projects are not where he puts the risk. [Bloomberg](https://www.bloomberg.com/news/articles/2026-09-14/openai-s-brockman-says-an-ai-pause-should-focus-on-frontier)
- **OpenAI bought camera startup Glass Imaging for $300 million**: its founders previously led Apple's Portrait Mode team. [TechCrunch](https://techcrunch.com/2026/09/14/openai-buys-smartphone-camera-maker-glass-imaging-for-300-million-report-says/)
- **Waymo opened robotaxi service in Las Vegas**: the city is its 15th commercial market. [TechCrunch](https://techcrunch.com/2026/09/14/waymo-opens-robotaxi-service-in-las-vegas/)
- **Claude Code weekly limits dropped 17% today**: the temporary 50% boost ended, leaving only the permanent 25% increase. [byteiota](https://byteiota.com/claude-code-weekly-limits-anthropic-cuts-17-today/)
- **Temporal raised $550M at a $12.55B valuation**: the company credits demand for durable execution as AI workloads raise the reliability bar. [Temporal](https://temporal.io/blog/temporal-raises-usd550m-series-e-at-usd12-55b-valuation-ai)
- **Apple's Siri code points to swappable models**: a Model Delegation mechanism would let Claude appear as a Siri extension the way ChatGPT does. [MacRumors](https://www.macrumors.com/2026/09/14/siri-can-be-swapped-out-for-chatgpt-claude/)