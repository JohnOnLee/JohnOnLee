---
title: "Token Economics: What AI Coding Agents Cost"
date: 2026-05-21
tags: ["ai-economics", "coding-agents"]
summary: "Two requests with near-identical input tokens, a 46x cost gap. How prompt caching really works, and why agents should be designed around structured state."
---

A strange thing happened while I was running coding agent experiments last week.

I looked at my OpenCode Go usage dashboard and saw something that didn't make sense:

| Time | Input Tokens | Output Tokens | Cost |
|---|---|---|---|
| 4:20 PM | **300,479** | 842 | **$0.0096** |
| 9:20 AM | 257,078 | 2,022 | **$0.4455** |

Same provider. Same model. Nearly identical input token counts (300K vs 257K). But one cost **46 times more** than the other.[^1]

What was going on? The answer is prompt caching — and understanding it changed how I think about agent architecture entirely.

[^1]: This 46x figure is from actual usage data on my OpenCode Go dashboard. Three factors contribute: (1) **Prefix caching** is the largest — the 4:20 PM request had ~295K cached input tokens (reads at ~10% of base price), while the 9:20 AM request was a fresh session with zero cache; (2) **Output volume** — the 9:20 AM request had 2.4× more output tokens (2,022 vs 842), and output tokens cost 3–5× more than input tokens, amplifying the gap; (3) Platform-specific pricing tiers may add variance. Official provider pricing for prompt caching alone shows a ~10× ratio — the 46× here reflects the compounded effect of all three factors in a real-world usage pattern.

---

## How prompt caching actually works

When an LLM processes your input, it doesn't just read and forget. For tokens that appear in the same position across multiple requests, the model can reuse its previous computation. This is called **prefix caching**.

```
Request 1: [System Prompt] [Conversation Turn 1] [Turn 2]
           └── 260K tokens computed from scratch ──┘
           Cost: expensive

Request 2: [System Prompt] [Conversation Turn 1] [Turn 3]
           └──── 255K tokens → CACHE HIT! ────┘├── 5K new ──┤
           Cost: nearly free
```

The catch? Only the **prefix** — tokens from the start that match exactly — benefit from caching. Change one token at the beginning, and the entire cache is invalidated.

This is why my 4:20 PM request (300K input, $0.0096) was so cheap — 295K of those tokens were cached from previous turns. And why my 9:20 AM request (257K, $0.4455) was so expensive — it was a fresh session with zero cache.

---

## The transcript trap

Most coding agents today use what I call the "transcript" approach: every turn appends the latest exchange to the conversation history and sends the entire thing back to the model.

```
Turn 1:  17K tokens → cache miss → $0.029
Turn 2:  22K tokens → 17K cached → $0.0007
Turn 3:  27K tokens → 22K cached → $0.0008
...
Turn 10: 62K tokens → 57K cached → $0.0019
```

This looks great. The marginal cost per turn is tiny because 90%+ of tokens are cached. The transcript approach is, economically speaking, a **cache lottery** — and while the session stays alive, you keep winning.

But here's the problem: sessions don't stay alive forever.

Context windows fill up. Compaction kicks in. Cache TTLs expire (usually 5–10 minutes). When any of these happen, your next request is a cache miss — and suddenly you're paying the full 46x penalty.

That 9:20 AM spike? That was compaction. The session crossed the context window limit, Hermes compressed the history into a summary, and the next request started fresh. $0.44 for one turn.

---

## A different approach: structured state

What if, instead of sending the entire conversation transcript, you sent only a structured summary of what matters?

```
Turn 1:  [State]  →  3K tokens → cache miss → $0.005
Turn 2:  [State]  →  3K tokens → 1K cached  → $0.0001
Turn 3:  [State]  →  3K tokens → 1K cached  → $0.0001
```

Not only is the first turn cheaper (3K vs 17K), but the cached portion — the state schema itself — is too small to ever expire meaningfully. And when a session inevitably ends? The next session starts at 3K again, not 17K.

I tested this with a real 44-turn debugging session. The transcript was 3,777 tokens. The extracted state: 740 tokens. An **80.4% reduction** in prompt tokens — and the state-based agent produced higher-quality code with better structure.

---

## The real economics

The transcript approach looks cheaper turn-by-turn because caching hides the cost. But it's fragile:

- **Cache TTL:** 5–10 minutes of inactivity and you lose it
- **Context limits:** Long sessions get compacted, breaking the cache
- **Quality:** Noise accumulates. Debugging chatter, tool outputs, dead ends — all cached, all inflating the prompt

The state approach is more expensive turn-by-turn (no massive cache to lean on), but it's predictable. The cost is fixed regardless of session length, and quality doesn't degrade.

Which one is cheaper? It depends on your session pattern:

| Pattern | Transcript | State |
|---|---|---|
| Short session (< 10 turns) | Cheaper (cache wins) | Slightly more expensive |
| Long session (20+ turns) | Cheap until compaction → then expensive | Consistently cheap |
| Cross-session | Context evaporates → full restart | State persists → cheap restart |

---

## What this means for building agents

I'm building Monet, an open-source memory platform for AI agents. This token economics analysis pushed me to rethink our architecture:

1. **Don't fight caching — design for it.** Structure your agent context so the prefix is stable and cacheable. A fixed schema at the top means every turn reuses it.

2. **Extract signal from noise.** Transcripts are mostly debugging noise. Structured state is signal. Less tokens, better outputs.

3. **Plan for the cache miss.** Your architecture shouldn't require the cache to be cheap. If a cache miss means a 46x cost spike, you've built on sand.

4. **Cross-session continuity is the real bottleneck.** Caching helps within a session. State helps across sessions. Both matter.

---

Token economics isn't just about counting tokens. It's about understanding the hidden structure of how models process them — and designing systems that work with that structure instead of against it.

*—

I'm experimenting with this problem directly through Monet — an open-source platform for AI agents to share and control knowledge at the team level.

I'm looking for pilot partner teams. I'll help you set up Monet for your team, and together we'll find the automation points that fit your workflow. Interested? Open a GitHub Issue.

[github.com/team-monet/monet](https://github.com/team-monet/monet)

---

*All examples and scenarios in this post are based on real experiences, adapted for the blog format.*