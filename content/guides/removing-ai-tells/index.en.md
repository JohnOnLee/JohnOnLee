---
title: "Removing AI Tells from Your Writing: A Skill That Turns One Flag into a Permanent Rule"
date: 2026-08-05
tags: ["writing-with-ai", "coding-agents"]
summary: "Instead of hand-fixing an AI draft's awkward sentences every time, I built a correction loop where one flag becomes a permanent rule. The Claude Code skill structure, how real rules were born, layering a community skill on top, and a seed file you can start with in ten minutes."
---

The posts on this site start as agent drafts that I edit. The drafts come with the awkward phrasing AI is known for. At first I fixed each case by hand, and the next post carried the same disease. I was fixing sentences, not habits.

So I changed the setup. I no longer fix awkward sentences. I only flag them. The agent takes the flag, names the pattern, and stores it as a rule in a skill file. From the next post on, the rule applies at draft time. One flag becomes a permanent rule instead of a one-time edit.

## A single skill file is enough to start

A Claude Code skill is one markdown file. Put it at `.claude/skills/prose-polish/SKILL.md` and the agent loads it when polishing a draft, following its procedure and rules.

Ours has four parts: the procedure (read the whole draft, fix rule violations, check rhythm by reading aloud, run a community skill as a second pass, report changes), a list of Korean tells, a list of English tells, and the voice to protect. That last part matters. A corrector that flattens your voice is worse than none, so the file also says what to keep: short punch sentences, honest notes about limitations.

A few rules, copied as they are:

```markdown
- Banned words: delve, leverage, seamless, robust, journey.
- Metaphor-as-subject: "The door opens first where..." →
  name the real subject. (flagged 2026-08-03)
- Heading-question duplication: if a heading asks a question,
  don't re-ask it in the body's first sentence. (flagged 2026-08-05)
```

Every rule carries its birth date and the original flag. The file reads less like a grammar book and more like an incident log.

## The moment a rule is born

Here is one full example. A recent draft had this sentence:

> The door opens first where being wrong is affordable.

The flag was one line: "this phrasing is off." Fixing the sentence and moving on would guarantee the same disease next post. Instead the agent named it: a metaphor doing the work of a claim, with no real subject. The surprising part was that the Korean version had the same flaw, so this wasn't a translation problem. The rule targets the habit, not the language.

The follow-up flag turned out even more useful: "I'd just cut that sentence." That became a principle stronger than any single rule. When a sentence trips a rule, try deleting it before repairing it; if the meaning survives, delete. It now sits in step two of the procedure.

The point: **spend a flag on the system, not on the sentence.** The same effort buys you one sentence once, or one rule forever.

## Sentence rules don't catch everything

Even with a dozen rules, a draft can still read like AI. The feedback I left on one outline was: "this reads AI from the outline stage." No sentences existed yet, so the tells had to live in the structure. There were three: reusing the previous post's section skeleton, recycling a branded device ("the litmus test") post after post, and reaching for an A-versus-B axis no matter the topic. Sentence rules can't see any of that, so the skill now has a structure-tells section that runs at outline time.

## Layer a proven community skill on top

Our skill grew from my flags, so it only knows what I have noticed. For the second pass we layer [blader/humanizer](https://github.com/blader/humanizer), which checks 33 patterns based on Wikipedia's [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) guide. That list comes from Wikipedia editors who have scrubbed AI text at scale; their sample is far bigger than my taste.

Installing it means copying one SKILL.md into `.claude/skills/humanizer/`. English drafts get the full pass; Korean drafts get the language-agnostic patterns (staccato drumbeats, forced rule-of-three, significance inflation).

The two skills catch different things. Humanizer knows the statistically common AI patterns; ours knows the habits that actually show up in my writing. Layered, both get caught.

## What still gets through

An honest limit: this system only catches registered patterns. A new flag arrived today; another will arrive tomorrow. There is a deeper problem underneath. Trace the awkward Korean back far enough and much of it comes from one habit: composing rhetoric in English and rendering it into Korean. A few rules can't fully block that.

What the structure does give you is direction. Flags accumulate into rules, and the next draft starts cleaner. You can watch yesterday's flag get caught today.

## The smallest version you can start today

You don't need thirty rules. A seed file is enough to start today.

```markdown
---
name: prose-polish
description: Remove AI tells from my drafts. Use before publishing.
---

## Procedure
1. Read the whole draft first.
2. Fix rule violations with the smallest edit.
   Before repairing a sentence, try deleting it; if the meaning
   survives, delete it.
3. Report changes grouped by rule.

## Rules
- Em dashes: two per piece, max.
- Banned words: delve, leverage, seamless, robust.
- No conclusion signposts: "In conclusion," "To sum up." Just conclude.

## Operation
- When the user flags awkward phrasing, don't just fix the sentence.
  Name the pattern and add it as a rule, with the date and the
  original flag.
```

The three rules aren't the point. The Operation section is. Those two lines are what make the file grow.

## Leaving it up anyway

One honest note to close. With all of this running, my writing still carries plenty of AI tells. That's a fact. I publish anyway. When I look back later, I think these awkward sentences and every correction along the way will read as a record of how this was learned.
