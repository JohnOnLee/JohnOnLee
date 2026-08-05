---
title: "How Deep Does Your Coding Agent Setup Go?"
date: 2026-05-31
tags: ["coding-agents"]
summary: "Two developers, same tool, wildly different setups. How deep coding agent customization goes — from bare defaults to full pipelines — and what actually pays off."
---

Two developers. Both use Claude Code.

One opens a terminal, types `claude`, and asks it to fix a bug. The other has 500 lines of CLAUDE.md, five custom MCP servers, and a sub-agent pipeline that reviews PRs while they sleep.

Same tool. Completely different experience.

**Fill out the survey and you'll see how others answered live — immediately.**

Most discussions focus on which tool to pick. I'm more curious about what happens after — how far people take the one they chose. So I put together a 2-minute survey to find out.

## The Five Levels

Here's how I'm thinking about customization depth:

**🅱️ L1: Bare** — Default install. You run the basic commands.

**📝 L2: Rules** — You actively maintain rules/context files (CLAUDE.md, AGENTS.md, .cursorrules).

**🔧 L3: Dialed In** — Custom system prompts, per-project settings, model switching.

**⚙️ L4: Extended** — Custom tools or integrations. Slash commands, CI/CD hooks, MCP servers — the tool has abilities you built yourself.

**🏗️ L5: Orchestrated** — Multi-agent workflows, sub-agents, automated pipelines that span multiple sessions. The agent isn't a tool anymore. It's infrastructure.

These aren't a ranking. There's no "L5 is better than L1." A team that needs stability and predictability might be right at L1. A solo dev shipping fast might thrive at L4. The point is that the gap exists, and nobody has measured it.

## The Survey

Seven questions. Anonymous. You can see live results after submitting.

→ **[forms.gle/22hwLNNzk5BQZ2QP6](https://forms.gle/22hwLNNzk5BQZ2QP6)**

It asks which tool you use, where you land on the spectrum, how satisfied you are, whether you plan to customize more, and a few demographic questions to slice the data.

## Why This Matters

Two patterns I'm watching for:

**Tool vs. depth.** Do certain tools naturally pull users toward specific levels? Claude Code ships with extension points built in. Cursor and Windsurf focus on getting you productive immediately. Does that divergence show up in how people actually use them?

**Depth vs. satisfaction.** More customization might mean more satisfaction — or it might mean more friction. The person who spent 40 hours tuning a pipeline has higher standards than the person running defaults. Where does the curve peak?

I don't have answers yet. That's what the survey is for.

**→ [forms.gle/22hwLNNzk5BQZ2QP6](https://forms.gle/22hwLNNzk5BQZ2QP6)**

Full analysis once we have enough data. Help get us there — share the link and fill it out if you haven't.

*All examples and scenarios in this post are based on real experiences, adapted for the blog format.*

---

*I think about this stuff because I'm experimenting with the problem directly through [Monet](https://github.com/team-monet/monet?utm_source=devto&utm_medium=post&utm_campaign=blog-launch) — an open-source platform for AI agents to share and control knowledge at the team level.*