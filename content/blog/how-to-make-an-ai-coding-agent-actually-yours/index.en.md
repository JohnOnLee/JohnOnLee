---
title: "How to Make an AI Coding Agent Actually Yours"
date: 2026-06-23
tags: ["coding-agents"]
summary: "I built Monet to fix the agent that forgets yesterday's conventions. How an agent that writes its own memory and reads back what mattered actually works."
---

If you work with an AI coding agent every day, you know the feeling.

**You clearly agreed on a convention yesterday — open a new session and it's a blank slate.** That I always use `type` over `interface` in TypeScript, that I said I didn't like that pattern in code review, the root cause of the bug we barely cornered last week — it acts like it's hearing every bit of it for the first time.

Do that enough times and you land on "I'll just do it myself."

**I built Monet to fix this** — to make a generic AI agent act like *my* agent. A system that learns my conventions, remembers how I like to work, and keeps track of the project's history on its own.

---

## How it works

The core is simple.

**Write — the agent decides for itself.** You never say "remember this." As it works, it records the decisions it makes, the patterns it spots, the issues it runs into. It filters the noise and keeps the signal.

**Read — what was useful comes back first.** It's not plain keyword search. The memories that actually got referenced and helped solve problems surface first; the zombie memories nobody touches sink to the bottom on their own.

**Grow — it gets smarter as it piles up.** The first task is slow — it doesn't know the codebase, the conventions, the bugs that keep blowing up. But once memory builds, the next task is faster: the pattern you found yesterday, the decision you made last week, that bug's root cause — no need to dig them up again. After a month or so, the agent stops feeling like a generic tool and starts moving like a dedicated engineer who knows this project inside out.

---

## How I got here

At first I just piled notes into one file — the agent jotting down what it learned as markdown, and me `include`-ing it at the start of each session. Simple, but the noise grew as the file grew.

So four months ago I built a proper memory system. **The old Monet.** MCP-based, built for agents to read and write, with team sharing in mind. But chasing team sharing made the solo experience fuzzy. It worked, technically — it just didn't fit my workflow.

**So I tore it down.** A few weeks ago I set the team-sharing goal aside and rebuilt Monet from scratch around one question: *can I actually use this every day?* As I write this, 12 agents read and write on the new Monet. There's no monitoring yet so I can't pull exact numbers, but searches are down and reads/writes are way up from before — which means the agent is curating what matters on its own.

---

## Honestly

At the vibe-coding stage, memory doesn't matter much. Most of it is brand-new features, and the bugs are simple. You tell the agent "fix this" and it's done inside the context window.

**But once the app gets complex, it's a different story.** To change one line you have to check ten related pieces of logic, and the agent crawls file to file hunting side effects. Mistakes go up. Even with 1M tokens, three context-compactions later you're back where you started.

At home I build fun things with agents on fresh code; at work I wrestle with 20-year-old code every day. **At work, agent memory isn't optional. Without it, the work doesn't move.**

So I started building a file-based indexed memory for myself. That was the start of Monet. These days I deliberately send the agents on laps at work — just to gather context. Most tickets wrap inside 20% context. The time I save is obvious; what matters more is the stress is gone.

Best of all: where I used to rack my brain over "how did I fix that bug again," now I just ask Kiro (our coding agent at work). It usually knows.

**Once you have dozens of agents and millions of lines of code, context stops being a byte problem and becomes an infrastructure problem.** And at that point, memory isn't a nice-to-have — it decides whether the work is even possible.

---

## Want to try it

- **Homepage**: [monet.team-monet.com](https://monet.team-monet.com)
- **GitHub**: [github.com/team-monet/with-monet](https://github.com/team-monet/with-monet) — the install harness (Apache-2.0)
- **100% local**: your code never leaves your machine — on-device embeddings, no network, no telemetry. Memory is a single SQLite file at `~/.monet` that you can open, back up, and export yourself.
- **Free to use.** The engine is a closed compiled binary, but the interface is standard MCP — works out of the box with Claude Code, Cursor, Codex, and other MCP-capable agents.

**I'd especially love for these people to try it:**

- developers who work with AI agents seriously, every day
- anyone who's felt the fatigue of "do I have to explain that *again*…"
- anyone who thinks "agent memory? why would I even need that?" (seriously — I want the counterarguments too)

---

*Every example and scenario in this post is from real experience.*
