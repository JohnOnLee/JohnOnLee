---
title: "Keep Your CLAUDE.md Light: Fewer Rules Win"
date: 2026-08-02
tags: ["coding-agents"]
summary: "A CLAUDE.md does not get better as it grows. Why piling up rules degrades your agent, what belongs in the file, and where the rest should live."
---

Every serious coding-agent user's CLAUDE.md walks the same road. It starts empty. Every incident adds a line. One day you look up and it's 500 lines long.

Then something strange happens. The more rules you add, the fewer rules the agent follows. You wrote it down, clearly, and it gets ignored. So you write the same rule again, louder. **Bold** it, add an exclamation mark, prefix it with "ALWAYS". It still gets ignored.

This guide is about what to take out of your CLAUDE.md, not what to put in. The short version: a good CLAUDE.md is a short constitution, not a long rulebook. If your tool reads AGENTS.md instead, the same principles apply.

## Why the file gets heavy

The path is always the same. The agent makes a mistake. You add a rule. It makes a different mistake. You add another.

Adding always feels justified in the moment: an incident just happened, and this sentence will prevent it. The problem is the other direction: the moment to delete a rule never arrives. You can't easily tell that deleting helped, and the damage of keeping everything accumulates slowly.

So a heavy CLAUDE.md isn't a sign of laziness. The incentives only point one way.

## Why heavy means worse

Three effects stack up.

**Context is a fixed cost.** Your CLAUDE.md rides along in every session, every turn. At 500 lines, you pay for 500 lines on every request. This isn't only about token pricing: it's attention taken off the actual task, prepaid. I wrote about the caching and context-cost mechanics in [Token Economics](/en/blog/token-economics/).

**Emphasis dilutes as it spreads.** With 5 rules, each one carries weight. With 50, each carries a fiftieth. Emphasizing everything is the same as emphasizing nothing. In a document with ten ALWAYSes, the eleventh is decoration.

**Contradictions get resolved silently.** A rulebook that grows for months accumulates clauses that collide. If "always write tests first" and "make only the minimal requested change" live in the same file, the model doesn't report the conflict. It quietly drops one side — and which side varies by the day. A good share of "the agent ignored my rule" moments are actually this.

## What stays, what goes

Three kinds of things deserve to stay.

- **What can't be learned from the code or docs**: why this architecture was chosen, team habits written down nowhere else
- **What applies to every session unconditionally**: tone, language, commit conventions
- **Safety boundaries**: anything that's hard to undo, like pushing to main or touching production

Four kinds of things should go.

- Anything readable from the code (directory tours, function lists)
- One-off instructions whose task is long finished
- Procedures needed only in specific situations (next section decides where they move)
- Things the model is already good at ("write clean code")

The litmus test is one line: **"If I delete this, what concretely gets worse in the next session?"** No specific answer, no seat in the file.

## Where the removed lines go

Being told to delete feels risky. Those rules are incident records. Can you afford to lose them?

You're not losing them. You're rehousing them. If CLAUDE.md is the constitution, everything else is statute. Keep identity and principles in the constitution; move concrete clauses somewhere that loads only when needed.

- **Situational procedures → skills (commands).** "Deploy in this order" has no business riding in every turn. Loading when someone calls `/deploy` is enough.
- **Mechanical repetition → hooks.** "Run lint before committing" is not a rule, it's automation. A hook fires regardless of what the model remembers. Deciding what to trust to memory versus machinery is the core move.
- **Accumulated knowledge → memory.** "Last time this bug was fixed like so" is not a rule, it's a memory. File-based or a dedicated tool, there should be a separate layer you search and retrieve from.
- **Project facts → docs next to the code.** Architecture explanations belong in README and docs. The agent reads them when it needs them.

Once this structure exists, every new rule request comes with a question: constitution or statute? It's almost always statute.

## Before and after

A typical before:

```markdown
# CLAUDE.md (excerpt, before the diet, ~500 lines total)
- Always respond in Korean
- Helper functions live in src/utils. UI components in src/components,
  API clients in src/api, hooks in src/hooks... (40 lines of structure tour)
- ALWAYS run npm run lint before committing
- Deployment MUST follow: 1) test 2) build 3) staging check 4) ...
- Do not edit config.ts directly (see incident, 2026-05-12)
- Write good commit messages
- ...
```

And after (this is the whole file, not an excerpt):

```markdown
# CLAUDE.md (after the diet, complete)

## Identity
Speak Korean, like a colleague. Conclusions first.

## Boundaries
- Never push directly to main. Ask before committing.
- Production config files are read-only.

## Delegation
- Deployment: /deploy skill
- Pre-commit lint: handled by a hook (not entrusted to model memory)
- Project history and past incidents: search memory
```

Where the missing 490 lines went is the entire point of this guide. Structure tours moved to docs, deploy steps to a skill, lint to a hook, incident records to memory. Nothing was lost. Everything went home.

## The maintenance routine

- **When an incident happens, flip the order.** Not "let's add a rule" but "where does this belong" — skill, hook, or memory? CLAUDE.md is the last resort.
- **Diet on a schedule.** Look back over your last ten sessions and find the rules that never fired once. Anything that fails the litmus test gets deleted.
- **Set a ceiling.** Mine is one screen. When the file starts scrolling, something needs to move out.

## Checklist

Open your CLAUDE.md and check five things.

1. Does every line make the next session concretely worse if deleted?
2. Is there anything the code itself could answer?
3. Does "ALWAYS" appear three times or more?
4. Do any clauses collide?
5. Does it fit on one screen?
