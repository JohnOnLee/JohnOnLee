---
title: "OpenAI's GPT-6 Astra ships Critical-level cyber skills"
date: 2026-09-04
summary: "OpenAI started rolling out GPT-6 Astra, its new flagship, in phases on September 3. Companies in its application-based cybersecurity program, Daybreak, get…"
---

## OpenAI shipped GPT-6 Astra on September 3, its first model to clear the "Critical" cyber threshold
- **The launch**: OpenAI started rolling out GPT-6 Astra, its new flagship, in phases on September 3. Companies in its application-based cybersecurity program, Daybreak, get access first; ChatGPT Plus, Pro, Business and Enterprise, the API, and Amazon Web Services follow in the coming days. OpenAI calls it state-of-the-art across computer use, software engineering, professional work, and science. [CNBC](https://www.cnbc.com/2026/09/03/open-ai-astra-gpt-6-cyber.html)
- **The price signal**: $10 per million input tokens and $50 per million output tokens through the API, 2.5x GPT-5.6 Sol's promotional pricing and the same as Anthropic's Fable 5.1. Per OpenAI's API docs, a GPT-6 Astra prompt over 272K input tokens is billed at 2x input and cache and 1.5x output for the whole request. [The New Stack](https://thenewstack.io/openai-gpt6-astra-benchmarks/) · [OpenAI](https://developers.openai.com/api/docs/models/gpt-6-astra)
- **The rating**: Astra is OpenAI's first model to reach its internal "Critical" danger rating for cyber capability. It can find unknown vulnerabilities and craft new exploits in well-protected systems without a human guiding each step. OpenAI is restricting access to that advanced tier and says the model went through a formal review with the Trump administration before release. [OpenAI safety overview](https://openai.com/index/safety-overview-gpt-6-astra/)

## A gated frontier and a cheap volume tier are now two separate markets for your stack
- **What it changes for your product**: The capability frontier now opens first to enterprise programs such as Daybreak, so as an indie you are not the first to hold Astra's advanced tier. Your workshop is the volume layer, where cheap long-context models keep getting cheaper. Burning $50 per million output on every agent loop is now a luxury, so managing your agent's input-versus-output mix becomes ordinary cost work.
- **The agent quality bar moves up**: Astra's gains are not just cyber. It got noticeably better at multi-step work, respecting task boundaries, and finishing tedious tasks, OpenAI says. For anyone shipping agentic software, that long-horizon stickiness reads less as a benchmark number and more as a new floor for what users will expect.

## Run a standing security scan on your own repo and re-plan agent spend today
- **Experiment 1, a recurring security scan of your code**: AISLE found six unknown CVEs in curl, one of the most audited codebases on earth, right after OpenAI's and Anthropic's scanners reported zero. Autonomous security review is now a space an indie can enter; a cheap model on an hourly static scan is enough to start.
- **Experiment 2, re-shape your agent's cost**: At $50 output the loop budget changes. Make the agent summarize and compress the context it carries instead of re-reading it each turn, and chunk long prompts to stay under the 272K-token cliff where the whole request doubles.

## How long the gating and the premium hold is the open question
- **What to hold off on**: Building a product that assumes unfettered access to OpenAI's top-tier cyber capability is betting on access you may not get. Watch the release cadence before wiring your roadmap to it.
- **What to keep watching**: At Fable-level pricing, Astra is not the volume workhorse. Track how fast cheap open models like Qwen close the leaderboard gap, and keep the model choice isolated in code so you can swap. Powerful releases may keep moving slower behind safety reviews, as Astra's own pause after the Hugging Face breach showed.

## The rest of today's news
- **AISLE found six CVEs in curl after OpenAI and Anthropic reported zero**: Its autonomous scanner surfaced six low-severity CVEs in one of the most audited codebases in the world; curl maintainers patched all six. [AISLE](https://aisle.com/blog/aisle-discovered-six-curl-cves-after-openai-and-anthropic-found-zero)
- **GitHub Copilot App adds parallel agent sessions**: Developers can now run several AI agents at once for parallel coding work. [Developer news](https://bitcoinethereumnews.com/tech/github-copilot-app-adds-parallel-agent-sessions-for-developers/)
- **Anthropic reportedly plans its IPO prospectus after Labor Day**: The Information reports a late-September or early-October public listing is the target. [The Motley Fool](https://www.fool.com/investing/2026/09/03/anthropic-planning-unveil-ipo-details-labor-day/)