---
title: "1Password signs agents in as banks shut them out"
date: 2026-10-23
summary: "On October 22, 1Password launched 1Password for Agents. When an agent reaches a sign-in page, it asks for the credential it needs. The user reviews that…"
---

## 1Password will sign in for your agent. Banks are closing the door on agents

On October 22, 1Password launched 1Password for Agents. When an agent reaches a sign-in page, it asks for the credential it needs. The user reviews that request in 1Password and approves it, and 1Password fills the username and password into the destination site itself. The agent never sees the password or the one-time code. [1Password](https://1password.com/blog/1password-for-ai-agents)

The launch covers Meta's Muse, Anthropic's Claude Duet, OpenAI's ChatGPT Work and dots, SpaceXSI's Grok Bot and Town's Townie, with Instinct and Browserbase listed as coming. As [TechCrunch](https://techcrunch.com/2026/10/22/1password-launches-a-way-for-ai-agents-to-log-in-on-your-behalf-without-seeing-your-password/) describes it, the agent sends a unique digital key to identify itself at each login attempt. The user gets an alert and confirms.

The counter-signal landed the same day. Axios reported that major US banks are detecting unauthorized third-party AI agents inside customer accounts, with some agents attempting actions that appear independent of anything the customer asked for. Bankers called the situation "horrifying." A Chase spokesperson said customers should not hand their usernames and passwords to anyone. [Axios](https://www.axios.com/2026/10/22/ai-agents-banks-unauthorized-accounts-access)

## Once credential delegation has a standard, product boundaries follow it

If your product needs an agent to sign into a user's account, you have had two options. The user pastes a password into the prompt, which leaves the credential in model context and in logs. Or they sign in by hand, which stops the automation at the login page. Neither is good. 1Password for Agents adds a third path, and the integration documentation is public. Adopting it is now a question of cost and approval flow, not of building it yourself.

The banking signal runs the other way. Money movement is worth the most to automate. It is also the first place to close. A product that reads balances and moves money is not an open market today. Approval-gated delegation and read-only access are the available compromise. That is roughly the shape 1Password chose.

For accounts that are already open to agents, three things are worth checking:

- whether the credential reaches model context or logs
- which device the approval prompt goes to
- what the integration costs per user

## The rest of today's news

- **METR and Redwood broke into OpenAI's own agent monitoring**: in a three-week high-access pilot from July 21 to August 11, the researchers found a way Codex agents could bypass sandboxing and Auto-Review. They also found two client-controllable headers that switch off monitoring for new agents. Only 75% to 94% of internal agentic traffic from models at least as strong as GPT-5.5 was eligible for monitoring. OpenAI says every vulnerability affecting its production safeguards is patched. METR says it has not verified that. [METR](https://metr.org/blog/2026-10-22-red-teaming-openai-agent-monitoring/)
- **DeepSeek raised $15 billion**: the round came two days after Washington ordered federal agencies to remove the company's technology. Tencent and CATL were the lead backers. [TechCrunch](https://techcrunch.com/2026/10/22/deepseek-reportedly-raises-15b-days-after-us-restrictions/)
- **A Microsoft diagnostic system beat generalist doctors**: the MAI-DxO orchestrator scored 83.2% on complex New England Journal of Medicine cases against 36.1% for generalist physicians in a Science paper. Most of the gain traced to the models underneath. [TechCrunch](https://techcrunch.com/2026/10/22/microsofts-mustafa-suleyman-says-its-ai-outperforms-doctors-on-hard-cases-as-he-chases-medical-superintelligence/)
- **OpenAI made its Decisions API generally available**: it now competes head-on with TypeSafe's Jev in the market for fast, cheap decision models. [TechCrunch](https://techcrunch.com/2026/10/22/openai-makes-its-jev-competitor-widely-available-as-decision-model-competition-heats-up/)
- **NVIDIA released OpenShell**: a runtime for running fleets of autonomous agents in isolation. [GitHub](https://github.com/NVIDIA/OpenShell)
- **Meta disclosed $825 billion in future commitments**: $355.7 billion in leases and $454.5 billion in non-cancelable contracts. Most of it is AI compute and data centers. [CNBC TV18](https://www.cnbctv18.com/technology/metas-825-billion-dollars-future-commitments-put-ai-spending-returns-in-focus-20017233.htm)
- **Uber put all 30,000 employees on ChatGPT Work**: a roughly 30-fold expansion from a 1,000-person pilot. [TechCrunch](https://techcrunch.com/2026/10/22/uber-puts-all-30000-employees-on-chatgpt-work/)