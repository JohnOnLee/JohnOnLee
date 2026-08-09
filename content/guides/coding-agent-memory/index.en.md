---
title: "Coding Agent Memory: Storing Everything Fails"
date: 2026-08-03
tags: ["coding-agents", "ai-memory"]
summary: "I build an agent memory platform, and this week we reversed its direction. What store-everything memory breaks, and where state, facts, and principles belong."
---

In [How to Keep Your CLAUDE.md Light](/en/guides/keeping-claude-md-light/), I pointed to memory as one of the places your trimmed-out rules should go. This guide is about that memory layer.

Before we start, a disclosure. I'm building [Monet](https://github.com/team-monet/monet), a memory platform for AI agents. And this week we reversed its direction: we dropped generic memory, the store-anything-recall-anything layer. This post is the record of the failures that forced that call.

## If you're explaining the same thing a third time

When a session ends, the agent forgets everything. The design direction you settled yesterday, the reason you rejected that library — gone by the next session. Catch yourself explaining the same context for the third time and you reach the conclusion everyone reaches: add memory.

We did. Then the next problem arrives.

## Why store-everything memory fails

The first time you wire up memory, there is so much to save. Session summaries, task state, work in progress, decisions, fragments of conversation. Forgetting was the problem, so remembering more must be better. Everything goes in.

A few weeks later, three things collapse.

**Retrieval dies.** Search for "why did we pick this structure" and ten activity logs come back first. The one line that holds the reason gets buried under piles of "edited file A, tested B today." The more you store, the harder it gets to pull anything out.

**State lies.** Save "next step: X" and by the time the next session opens, X is usually already done. A human handled it, or priorities moved. Task state drifts from reality within a day, and memory hands that stale snapshot to the next session with full confidence.

**Old memories beat the present.** Once stored, a claim keeps showing up in search even after it turns out wrong. If adding the new decision doesn't retire the old one, the next session trusts whichever it finds first.

None of these come from storing too little. They come from storing everything.

## Route to three places

So we reversed direction. Instead of one memory that accepts anything, information gets routed by kind.

**Anything recoverable from code, git, or files: don't store it.** Directory layout, function lists, past commits. The next session can read them directly, and a direct read is always current. The litmus test from the last guide works unchanged here: "if I delete this, what concretely gets worse next session?"

**Task state and decision records: send them to the tracker, PRs, and docs next to the code.** What's done and what's next is issue work. Why A over B, and which alternatives died, belongs in ticket threads, PR descriptions, and ADRs. A decision should be read inside the context of the work that produced it, and that's where the next person digging into the code will look. A state snapshot in memory starts aging the moment it's written; a tracker issue stays current until the day it closes.

**Memory keeps only what steers the agent's behavior.** The mistakes you've corrected more than once, the things you told it never to do, the way this user likes to work. And the principles and rules those records add up to. This is all that lives nowhere else now, and it's the part that doesn't go stale: it gains value as it accumulates.

## What memory is for: principles and rules

After the routing, memory gets thin. Thin is what makes it strong. What remains is two layers: the record of corrections, and the principles and rules distilled from that record. When the same correction shows up three times, it isn't an incident anymore. It's a rule.

When you store a rule, store two things with it: when it fires, and why it exists. "Never force-push" alone leaves the next session with no idea when to look it up. "Fires right before git push --force; exists because we wiped main's history last month" makes the rule show up on time, and an agent that knows the reason actually follows it.

Corrections have to be first-class. When a memory turns out wrong, don't add the new version next to it; explicitly retire the old one. Otherwise both versions stay searchable, and the next session grabs either.

## Where to start

- **A markdown file.** One lessons.md in the repo, holding repeated corrections and the rules they turned into, solves half of this. Zero setup, grep for search. Most people should start here. Decision records go to PRs and ADRs, not this file.
- **Your agent's built-in memory.** If your tool ships a memory layer, like Claude Code's memory directory, use it — but the routing above is on you, because built-in memory won't refuse anything.
- **A dedicated memory tool.** When you need rules that carry their trigger and reason, first-class corrections, and a layer that refuses state, that's when a dedicated tool earns its place. It's where Monet is headed now, which makes me an interested party. Read accordingly.

The failures above are verified: we lived them for weeks. Whether the new direction is right is still being tested. All I can claim today is the shape of the failure, so that's where this post stops.

## Checklist

If you already run a memory layer, check five things.

1. Are activity logs or session summaries piling up in memory?
2. Is "next step" or a decision's rationale stored in memory? (The tracker and the PR are their homes.)
3. Does every stored rule carry its trigger and its reason?
4. Is there an explicit way to retire a memory that turned out wrong?
5. When you search, is the first result actually the memory you wanted?
