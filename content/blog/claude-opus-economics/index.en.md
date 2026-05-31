---
title: "Claude Opus Prices Just Crashed 67%. Is Anthropic Still Making Money?"
date: 2026-05-20
---

Claude Opus pricing just collapsed. **67% in one year.**

| | Opus 4 (2025) | Opus 4.7 (2026) |
|---|---|---|
| Output | $75 / MTok | **$25 / MTok** |
| Input | $15 / MTok | **$5 / MTok** |

At this rate, Opus 4.8 will be $15. Maybe $10.

So I got curious: if prices are falling this fast... **how much does Anthropic actually make per token?** Spent a weekend doing napkin math. It's probably wrong in three places. Please fix it in the comments.

---

## What does one token actually cost?

Rent an H100 GPU: **~$2/hr** (committed use discount).

At 500 tokens/sec with batching:
```
1.8M tokens/hr ÷ $2 = $1.11 per million tokens
```

Anthropic charges $25.

**That's a 23x markup.** 💀

---

## But that's too simple

Add the real costs:

| What | Per MTok |
|---|---|
| Raw GPU | $1.11 |
| Infra overhead (networking, cooling, idle) | $0.44 |
| Training amortization ($300M ÷ 500T tokens) | $0.60 |
| **Total unit cost** | **$2.15** |

Still. $2.15 to make, $25 to sell. **10x margin**, right?

Wrong. Nobody pays list price.

- Cache hits: 98% cheaper ($0.50)
- Batch API: 50% off
- Enterprise: negotiated down

My guess: **average effective price is ~$15-20/MTok.**

Margin: still healthy at ~88%. But thinning fast.

---

## The dirty secret: the tokenizer tax

Opus 4.7 introduced a "new tokenizer." It uses **35% more tokens** for the exact same text.

So that "$25" price tag? For the same work you did on Opus 4, you're actually paying:

```
$25 × 1.35 = $33.75 effective
```

The real price drop isn't 67%. It's more like 55%.

Is this intentional margin engineering, or a genuine technical trade-off? You tell me.

---

## So how much does Anthropic actually make?



R&D alone is $500M-$1B/yr. A hundred million free users. Safety research. Sales team. The next training run.

Tokens are profitable. The company isn't.

---

## My prediction

Opus 4.8: $15/MTok output. New tokenizer: 50% more tokens.

The headline will say "prices dropped again." Your bill will stay the same.

---

## Tell me where I'm wrong

- Is 500 tok/sec per H100 realistic for a frontier MoE model?
- What do enterprise contracts actually pay?
- Is the 35% tokenizer overhead a margin play or a real trade-off?

If you work in AI infra, cloud pricing, or know Anthropic's real costs — **correct me in the comments.**

---

*I think about this stuff because I'm experimenting with this problem directly through [Monet](https://github.com/team-monet/monet?utm_source=devto&utm_medium=post&utm_campaign=blog-launch) — an open-source platform for AI agents to share and control knowledge at the team level. Token economics determines what's possible.*

*github.com/team-monet/monet*