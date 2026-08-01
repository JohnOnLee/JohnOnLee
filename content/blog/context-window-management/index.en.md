---
title: "How Are You Managing Your AI's Context Window?"
date: 2026-05-11
summary: "Bigger context windows didn't give better results. Notes on the context-management problems that keep recurring in real coding agent sessions."
---

Your AI coding agent has a 200K token context window. Maybe 500K. Maybe a million.

So... what actually changed?

Honestly, I'm still figuring that out. I expected bigger windows to deliver better results. The reality has been more nuanced.

---

## 1. The Window Got Bigger. Did Anything Actually Change?

The narrative is seductive: "200K tokens! I can dump my entire codebase in there." "1M tokens? Every issue, every doc, every chat log."

This is like saying "my hard drive is 2TB, so I'll keep every file on my desktop." Technically possible. But do you actually do that?

Research consistently shows that as context windows grow, retrieval accuracy degrades. The "lost in the middle" problem is real — AI pays most attention to the beginning and end, and everything in between fades. Bigger haystacks make needles harder to find.

But here's what I find more interesting: **how are we actually using these bigger windows?** Model spec comparisons are easy. "200K vs 1M" is a number you can compare. But "how well am I managing my context" has no number. It's invisible. So nobody looks at it.

---

## 2. What Actually Happens Inside a Claude Code Session

Here's what I've observed over a few months of using Claude Code with my team. No quantified data — just experiential patterns. If you've done actual measurement on this, I'd honestly love to hear about it.

A typical session has this rhythm:

- **Context gathering eats up a surprising amount of time.** Reading issues. Scanning docs. Exploring the codebase to figure out what's what. It repeats at the start of every session.
- **Re-verification is weirdly common.** My Claude discovers something. Tomorrow, my Claude (or my teammate's Claude) re-discovers the same thing. Not because the AI isn't capable. Because the AIs don't share memory.
- **Actual problem solving gets less time than you'd think.** After the first two phases, you finally get to the work you opened the session for.

Here's what matters: this isn't waste because the AI isn't smart enough. It's waste because **the AIs don't share what they know**. We've built incredible systems for CI/CD, code review, documentation. But when it comes to how our AI agents share knowledge as a team? Almost nothing.

**What about your team?**

---

## 3. Three Patterns I Keep Seeing

### 1. The Dump Truck

> "I have 200K tokens. Here's every file in the repo, 47 issues, the company handbook. Go."

I get it. You don't know what's relevant ahead of time. The temptation to "just put everything in" is real.

But then your AI is reasoning against mostly irrelevant context. Finding patterns in noise. Confidently proposing solutions to problems you don't have. Unnecessary noise eventually eats away at reasoning quality.

I did this early on. Still catch myself doing it. I haven't found a perfect solution — but just being aware of the pattern has helped.

### 2. Groundhog Day

"Our project uses pnpm workspaces. Auth is in `packages/auth`. Don't touch `legacy/`. Alice owns deployments."

Your human colleagues learned this on day one. Your AI has to re-learn it every single session.

If a human teammate asked you to re-explain the project structure every morning before they could start working, you'd have a serious conversation. But we accept this from AI without question. Why haven't we automated this repetition away yet?

### 3. The Genius Silo

This is the most fascinating one. And the most unsettling.

Same Claude model. Wildly different outcomes. When a senior engineer who knows the product's bones by heart picks up Claude, the AI becomes a "genius." The codebase's history, known landmines, unwritten conventions — all this invisible context dissolves into the AI's reasoning. Sessions are fast, almost magical.

When a junior engineer with less context picks up the exact same Claude, they come back empty-handed. Their Claude re-discovers, from scratch, what the senior's Claude figured out months ago. Burns tokens. Burns time. Builds frustration.

Here's what this means: AI, as a tool, isn't lifting the team's collective productivity. It's **trapped in individual silos of personal experience**. The senior gets faster and faster. The junior stays stuck. Claude has become a personal assistant, not a team tool.

And the team lead sees none of this. Doesn't know what the senior's Claude knows. Doesn't know what the junior's Claude is painfully re-learning. **These invisible walls are completely hidden.**

**Is this happening on your team too? Or have you found a different way?**

---

## 4. What I've Been Trying (Hypothesis Stage)

After months of experimenting, I've roughly settled on four principles. These are working hypotheses — if you've found better approaches, I genuinely want to hear them.

### 1. Relevance Over Volume

I stopped asking "how much can I fit?" and started asking "what actually matters right now?"

A small, well-curated context beats a massive dump. I'm convinced of this through experience. What "well-curated" actually means in practice — still experimenting.

### 2. Persistence Over Repetition

When my AI discovers something valuable — a pattern, a gotcha, an insight — I try not to let it die with the session.

At the end of each Claude Code session, I ask myself: "What did my Claude learn today that my teammate's Claude should know tomorrow?" It's not perfect, but it has saved the opening minutes of my next session more times than I can count.

### 3. Domain Sync

**Transplanting the senior engineer's business context into the AI's baseline assumptions.**

When a senior tells their Claude "this component is perf-critical, O(n²) won't fly," that judgment has months of domain knowledge baked into it. Domain Sync is about making that knowledge accessible to every teammate's Claude.

It's about converting individual expertise into the team's prompt assets. How far this can be automated — I don't know yet. But the direction feels right.

### 4. Routinized Results Verification

Not blindly trusting the AI's output. Systematically filtering it through past incidents and accumulated history.

A senior developer, reviewing Claude's code, unconsciously checks: "We had a similar PR that broke tests last time..." "This pattern looks like the one that caused the outage last year..." This filtering instinct — knowing how to *reject* well — is what truly separates seniors from juniors.

The problem: this filtering instinct has remained private, tacit knowledge. How do we turn "knowing how to ask well" into "knowing how to filter well" — and make that filtering instinct a baseline routine for every team Claude? This is what I'm most preoccupied with lately.

---

## 5. What I Actually Want to Know — Let's Think Together

With context windows exploding toward infinity, are we falling into the quantity trap while losing sight of quality?

What actually determines real-world productivity isn't benchmark scores. It's **the quality of context optimized for your specific product**. But that doesn't show up on any benchmark. So nobody looks at it. So I'm asking.

### Four Questions

Is your senior engineer's AI know-how and business context being transferred to other team members — or is it trapped inside individual chat windows? How many Genius Silos exist on your team?

As windows grow bigger, AI paradoxically loses the plot (Lost in the Middle). What filtering are you doing to counter this? Not just "use less context" — are there smarter ways to structure it?

In the "store it and forget it" pile, is stale, contaminated context quietly poisoning your AI's judgment? Is last year's "never touch `legacy/`" silently overriding this year's "migration complete, it's safe now"?

Is your team's AI getting smarter over time — or stuck in an endless loop of Groundhog Day explanations? Do you have any way to tell?

---

## 6. Closing

I've been staring at this problem for months. Building tools. Running experiments with my team. But I don't have the answers. I'm still experimenting.

So I'm asking: **how are you managing your AI coding agent's context window?**

Ideas? I want them. Disagreements? Even better. If your experience is "dumping everything into a big window works fine for us," I genuinely want to hear about that too. Let's figure this out together.

---

I'm experimenting with this problem directly through [Monet](https://github.com/team-monet/monet?utm_source=devto&utm_medium=post&utm_campaign=blog-launch) — an open-source platform for AI agents to share and control knowledge at the team level.

I'm looking for pilot partner teams. I'll help you set up Monet for your team, and together we'll find the automation points that fit your workflow. Interested? Leave a comment or open a [GitHub Issue](https://github.com/team-monet/monet/issues?utm_source=devto&utm_medium=post&utm_campaign=blog-launch).

---

*All examples and scenarios in this post are based on real experiences, adapted for the blog format.*