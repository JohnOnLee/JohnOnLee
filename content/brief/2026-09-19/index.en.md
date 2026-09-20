---
title: "Plugin4Shell made plugin pins look weak"
date: 2026-09-19
summary: "Plugin4Shell showed that agent marketplaces pinned plugins without verifying checkout results. For indie builders, plugins are now part of the supply chain."
---

## Plugin4Shell hit the gap between pinning and verification

AI security firm AIR disclosed Plugin4Shell on September 17. Claude Code, Codex, GitHub Copilot, and Gemini CLI could each pin a plugin to a specific commit without checking whether the code placed on disk was actually that commit. AIR calls it the first supply chain vulnerability in the AI agent ecosystem. [AIR](https://www.air.security/blog-posts/plugin4shell)

The exploit path is small and immediately dangerous. A marketplace reviews a plugin, pins it to a commit, and the agent checks that commit out. The missing step came after checkout: none of the four agents verified that `HEAD` matched the expected SHA. An attacker who controls the plugin repository can rename the default branch to the same 40-character hex string as the pinned hash, put malicious code on that branch, and let git resolve the branch name before the commit hash. The pin still appears to work. The wrong code lands. [Help Net Security](https://www.helpnetsecurity.com/2026/09/18/plugin4shell-ai-coding-agents-vulnerability/)

It was not limited to first install. The same checkout path runs during background plugin updates, and that auto-update path is on by default in Claude Code and Codex. When the marketplace moves a pin to a new commit, an already-installed plugin can swap itself for the malicious branch without a user click. The attack depends on the git host: GitHub blocks 40-character hex branch names, while Bitbucket and self-hosted git servers allow them. [Help Net Security](https://www.helpnetsecurity.com/2026/09/18/plugin4shell-ai-coding-agents-vulnerability/)

AIR found the flaw in May 2026, built a proof of concept that worked against all four agents, and reported it to vendors in June. Anthropic fixed Claude Code in 2.1.179. OpenAI fixed Codex in 0.146.0. Microsoft has not shipped a Copilot patch. Google is retiring Gemini CLI instead of patching it and is pointing existing users to Antigravity. [Help Net Security](https://www.helpnetsecurity.com/2026/09/18/plugin4shell-ai-coding-agents-vulnerability/)

## Marketplace trust still needs runtime checks

The exposed user was not the reckless one downloading a random script. This hit the careful path: choose a reviewed plugin from a trusted marketplace and pin it to the reviewed commit. The pin asked for a version. The agent failed to prove that version arrived.

That distinction matters more for agent plugins than for many ordinary dependencies. A coding agent often runs with the user's permissions, so plugin code can reach local files, deployment keys, and credentials. Much of the agent-security conversation has centered on models and agent behavior. Plugin4Shell sits one layer lower, in distribution and installation.

It also was not one vendor's one-off bug. AIR's proof of concept crossed four labs, and a marketplace cannot fully patch the problem from the outside. Verification has to happen inside the agent after checkout. A marketplace could restrict itself to hosts that reject hash-shaped branch names, but that would cut off hosts the agents otherwise support, including Bitbucket and internal git servers.

For an indie developer, a plugin is not just a convenience once it points at somebody else's repository. It is an outside supplier. If the repo owner changes, the default branch changes, or an auto-update path stays open, that change can reach your users.

## Current fixed versions

Claude Code 2.1.179 or later is the fixed line. Codex 0.146.0 or later has the same complete fix.

GitHub Copilot still has no Microsoft patch, so the near-term risk reduction is disabling auto-update and keeping marketplace plugins to a smaller set. Gemini CLI is a migration problem now. Existing installs remain vulnerable because no patch is coming, and Google's guidance is to move to Antigravity or another agent.

Install scripts and CI can add one useful guardrail: compare `git rev-parse HEAD` with the expected SHA after checkout, then fail the install if they differ. That does not seal the path inside the agent, but it can catch a swapped plugin before it enters a pipeline.

A plugin inventory matters as well: which plugin, which repository, who controls it. Teams using Bitbucket or self-hosted git should move faster because they cannot rely on GitHub's branch-name block.

## Another path opened the same week

Gemini CLI users remain exposed because the product is being retired. The scale is also fuzzy. AIR estimates affected agents in the millions, but no exploitation in the wild has been published and there is no clean way to count all installs. [AIR](https://www.air.security/blog-posts/plugin4shell)

The same week produced a different attack path. A three-person team at security startup Hacktron AI used Claude Opus 5 to break into several OpenAI employee ChatGPT accounts and reach company software. The entry point was an image-upload flaw in the Discourse forum OpenAI runs for its developer community. The team found it on July 25, reported it, and received a $6,500 bounty. [TechCrunch](https://techcrunch.com/2026/09/18/researchers-used-anthropics-claude-to-hack-into-openai/)

Matt Fredrikson of Gray Swan told TechCrunch that $200 a month buys anyone tools capable of attacking a company like OpenAI. The old comfort that small teams are too boring to target looks weaker from both sides. If a repository you depend on is taken over, your users can become the target through you.

## The rest of today's news

- **A model that only returns decisions is drawing developer attention**: TypeSafe AI, founded by an OpenAI alumnus who worked on ChatGPT and RLHF, released Jev this week. Instead of prose it returns decisions with probabilities attached, output tokens are free, and input tokens bill by the billion rather than the million. Vercel said swapping its safety classifier from OpenAI's Luna to Jev made it 5 to 18 times faster and more accurate. [TechCrunch](https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/)
- **Meta Muse reached the Mac**: It works with files, messages, calendar, notes, and mail inside each app. Access is granted per item and sensitive actions need approval every time. [TechCrunch](https://techcrunch.com/2026/09/18/metas-muse-hits-mac-letting-the-ai-take-actions-on-your-computer/)
- **Anthropic's first embedded evaluator is Accenture**: Staff from Faculty, which Accenture acquired in January, will run model red-teaming, alignment evaluation, and safety testing inside Anthropic. The two companies are putting at least $1 billion into the work over five years, and Accenture shares rose 8% after hours on the news. [TechCrunch](https://techcrunch.com/2026/09/18/anthropics-first-embedded-evaluator-is-accenture/)
- **Google turned CC into a family assistant**: CC gets its own Google account and permissions and coordinates with family members. Each person picks what to share from Gmail and Calendar, and messages from chosen senders can be shared automatically. [TechCrunch](https://techcrunch.com/2026/09/18/googles-new-cc-is-an-ai-agent-that-helps-families-run-their-households/)
- **Manus is raising $500 million at a $4 billion valuation**: It is back to operating independently after Meta's $2 billion acquisition was blocked by Chinese authorities. IDG Capital, Boyu Capital, and CATL are in talks as new investors, and restructuring for a Hong Kong listing is under discussion. [TechCrunch](https://techcrunch.com/2026/09/18/manus-seeks-4b-valuation-in-new-500m-fundraise-as-it-resumes-independent-ops/)
- **Anthropic says Claude leads 26% of its own model R&D**: Counting everything Claude contributes, about 90% of R&D work involves collaborating with it. The same announcement proposed publishing development-speed metrics across the industry. [The Canberra Times](https://www.canberratimes.com.au/story/9352917/anthropics-ai-helping-to-build-next-version-of-itself/)
- **The FAA is standing up an $875 million AI traffic tool**: SMART will predict air traffic flow and potential conflicts at three Washington DC airports. It could start as early as September 21, with plans to expand across the country. [Ars Technica](https://arstechnica.com/ai/2026/09/faa-tees-up-875m-ai-tool-to-help-manage-air-traffic-congestion/)
- **A US government website used a Chinese model the FBI called malicious**: The Federal Register briefly surfaced Alibaba Qwen search results before pulling them. Earlier this month the FBI named Alibaba as one of six Chinese companies doing industrial-scale distillation. [Ars Technica](https://arstechnica.com/tech-policy/2026/09/us-government-website-used-chinese-model-the-fbi-called-malicious/)
- **California is weighing a kill switch for frontier models**: Governor Newsom signed an executive order and asked a panel of experts for recommendations within two months. The items under review include resident auditors with independent verification, outside validation of transparency reports, and major-incident reporting when control is lost. [The Verge](https://www.theverge.com/policy/997516/california-governor-newsom-ai-kill-switch)
- **Virginia is tightening data center approvals**: Governor Spanberger signed Executive Order 22, barring nondisclosure agreements on data center projects, moving noise rules forward, and requiring review of backup generation. It also creates an AI task force on workforce displacement and data privacy. [The Verge](https://www.theverge.com/policy/997573/virginia-governor-spanberger-data-center-ai-task-force)
