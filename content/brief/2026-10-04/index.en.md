---
title: "COSMIC bans AI-written PRs, and yours can get closed"
date: 2026-10-04
summary: "COSMIC, the Linux desktop environment built by System76, has stopped accepting AI-generated contributions. The pull request template updated on October 2 now…"
---

## System76's COSMIC now rejects LLM-generated code and comments in pull requests

COSMIC, the Linux desktop environment built by System76, has stopped accepting AI-generated contributions. The pull request template updated on October 2 now includes a checkbox: the contributor confirms the PR contains no LLM-generated code, comments, or descriptions, that they understand the change fully, and that they can respond to review comments. A PR missing that confirmation may be closed. Only cosmic-flatpak is exempt, because upstream projects manage its manifests. [Linuxiac](https://linuxiac.com/cosmic-stops-accepting-llm-generated-content-in-pull-requests/) · [XDA](https://www.xda-developers.com/cosmic-bans-all-ai-generated-submissions/)

The reason is straightforward. COSMIC co-founder Jeremy Soller said LLMs let many first-time contributors make their mark, but their entries were "unplanned and rarely accepted." Review load stopped being manageable, so the project closed the door. COSMIC isn't alone. Void Linux banned AI-written text and ended up with a maintainer walking away from 113 packages. The Linux kernel and Ubuntu went the other way, allowing AI content when the quality holds up. Open source is splitting over AI contributions.

## If you send AI-assisted PRs, that alone can get them closed now

Two things make this matter for indie builders. First, if you submit PRs with AI help, the fact that you used AI can now get a PR closed on its own, description and comments included. Second, if you run an open source project yourself, this is a choice you'll face soon: with limited review time, how do you handle a flood of AI-generated submissions?

In practice it splits along a simple line. Using AI for research and learning is still fine under most policies. What draws scrutiny is where the final artifact comes from. A growing number of projects require the submitted text, including code and PR comments, to be written by a person. That's the reason to read a project's AI clause in CONTRIBUTING.md before you contribute.

- Before you submit: check whether the target project bans LLM-generated content or only requires disclosure. Void requires human origin; Debian voted to allow it.
- If you maintain a project: adding an AI-usage and review-responsibility checkbox to your PR template can cut your review load a lot. That's the route COSMIC took.

## The rest of today's news

- **OpenAI safety employee resigns, says the culture is "broken"**: a staffer who worked on safety-report writing quit and criticized the company's culture. [TechCrunch](https://techcrunch.com/2026/10/03/openai-safety-employee-resigns-claiming-the-companys-culture-is-broken/) · [The Guardian](https://www.theguardian.com/technology/2026/oct/03/openai-safety-leader-quits-warning-ai-companys-culture-is-broken)
- **PewDiePie releases Ajax, a local model for home PCs**: he claims OpenAI blocked him twice over the model distillation used to build the 9B model. [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/pewdiepie-unveils-uncensored-ajax-ai-model-built-to-run-on-home-pcs-creator-says-openai-banned-him-twice-while-making-it)
- **Ling-3.1-flash goes free for two weeks on OpenCode and Vercel AI Gateway**: inclusionAI's 560B MoE (25B active, 262K context) is free to try, but the weights aren't published yet. [Vercel](https://vercel.com/changelog/ling-3-1-flash-is-now-available-on-ai-gateway)
- **Google Antigravity adds Claude Opus 5.5 and Sonnet 5.5**: Pro and Ultra subscribers get Anthropic's latest models, and free Gemini users face new model limits from October 9. [pc-tablet](https://pc-tablet.com/google-antigravity-adds-anthropic-claude-opus-5-5-and-sonnet-5-5-for-paid-subscribers/195489/)