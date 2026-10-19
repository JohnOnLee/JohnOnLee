---
title: "OpenCode console leak: API keys billed, defenders blocked"
date: 2026-10-20
summary: "On October 17 OpenCode said attackers broke into its hosted console overnight. The company put the affected group at 1.4% of Console users, limited to people…"
---

## API keys leaked out of OpenCode's console, and the defenders could not analyse the attack

On October 17 OpenCode said attackers broke into its hosted console overnight. The company put the affected group at 1.4% of Console users, limited to people who had linked external AI provider accounts. Console is where some users store the API keys they use to reach OpenAI, Anthropic and Google. Co-founder Dax Raad said the breach was in Console, not in OpenCode itself, and that those keys never reach the company. The open-source app and the command-line tool were untouched. [TechCrunch](https://techcrunch.com/2026/10/19/hackers-hit-ai-coding-tool-opencode-running-up-charges-on-users-ai-accounts/)

Spending alerts started firing the same night. One developer reported OpenAI, Anthropic and Google spend alerts all going off before bed. Charges reached hundreds of dollars on individual accounts, and a few users described totals above $1,000. Anthropic and Google blocked the keys they believed were exposed, and OpenAI said it worked with OpenCode to restore access and refund the credits the attack consumed. OpenCode says refunds are under way. The notice it sent to affected users described unauthorised access to a legacy system and told them to revoke and replace their provider keys from each provider dashboard. [Cybersecurity News](https://cybersecuritynews.com/opencode-security-breach/)

Stopping the attack ran into a second problem. Raad said attackers tried to break in non-stop for 48 hours, so the team kept AI defensive agents running around the clock. The commercial models it turned to helped for a while, then refused to continue once the malicious code tripped their safety filters. OpenCode later received access to OpenAI's Daybreak Blue programme, which gives vetted users models that are less likely to refuse defensive security work, and Raad said that improved the investigation. Hugging Face hit the same wall in July and called it the asymmetry problem. David Sacks, co-chair of the President's Council of Advisors on Science and Technology, wrote that the guardrails backfired. [TechCrunch](https://techcrunch.com/2026/10/19/hackers-hit-ai-coding-tool-opencode-running-up-charges-on-users-ai-accounts/)

## Where you keep your keys is what sets the size of the bill

The money in this incident took a simple route. A key attached to a provider account ended up in someone else's hands, requests ran through it, and the invoice arrived at the key's owner. What a product team controls sits in front of that. Issue a separate key per project, set a spend limit at the provider, and switch on spend alerts, and a breach has a ceiling. If you keep keys inside a third-party workspace, that workspace becomes part of your service.

Your defensive tooling deserves the same look. An incident forces you to read logs and malicious code, and if the model you delegate that to stops at a safety filter you are on your own at the worst moment. One open-weight model you can run yourself is cheap cover for that hour. The timing is worth a note: the breach landed the same night OpenCode made GLM-5.3-Flash free.

## The distillation attack label still has no supporting evidence

OpenCode calls this a breach tied to a large-scale distillation attack. It has not said how the attackers got in, how long they stayed, or how many keys were involved. Some observers called the framing an overstretch, arguing the incident looks like a straightforward breach whose use for distillation is unproven. The company says the incident is still ongoing.

Two things are worth tracking: whether OpenCode publishes a technical report, and how the providers handle charges run up with stolen keys. Until that is settled, the monthly spend limit is the control you actually hold.

## The rest of today's news

- **Nvidia releases open models for agents**: a 120-billion-parameter Nemotron 3.5 Super VL for enterprise agents, plus two lightweight Bolt models that run locally on AI PCs and DGX Spark workstations. [TechCrunch](https://techcrunch.com/2026/10/19/nvidia-launches-new-open-models-to-run-agents-in-the-enterprise-and-on-pcs/)
- **AWS ships TorchNeuron**: the tool moves PyTorch apps onto Amazon's Trainium chip with one line of configuration. [TechCrunch](https://techcrunch.com/2026/10/19/amazon-is-taking-its-biggest-shot-at-nvidia-yet-with-new-torchneuron-dev-tool/)
- **Apple bans apps that hide nudify features until after review**: the developer guidelines now require content filtering and reporting tools, and bar undocumented features. [TechCrunch](https://techcrunch.com/2026/10/19/apple-updates-guidelines-to-ban-nudify-apps-masquerading-as-regular-apps-to-pass-review/)
- **DeepSeek opens its search and fetch APIs at $0.75 per 1,000 calls**: server-side search through Claude Code and Codex on DeepSeek models stays free until October 31. [WebProNews](https://www.webpronews.com/deepseek-opens-in-house-search-and-fetch-apis-to-developers/)
- **Schwab and JPMorgan block outside AI agents from client accounts**: Schwab is preparing read-only MCP access and keeps money movement in its own tools. [Agent News Daily](https://agentnewsdaily.com/brief/2026-10-19)
- **Tenstorrent raises $1.5B at a $6.2B valuation**: the inference chip maker will scale silicon for serving open-weight models. [TechCrunch](https://techcrunch.com/2026/10/19/tenstorrent-hits-6-2b-valuation-to-scale-open-weight-ai-chips/)
- **Developers are using coding agents to strip ads and tracking from smart TVs**: projects such as dumbtv and individual write-ups have spread this week. [TechCrunch](https://techcrunch.com/2026/10/19/people-are-using-ai-to-make-their-smart-tvs-dumb-again/)