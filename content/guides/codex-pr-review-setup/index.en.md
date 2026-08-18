---
title: "Codex PR Review: Automatic Reviews, Triggers, Review Rules"
date: 2026-08-21
tags: ["coding-agents"]
summary: "How to turn on Codex code review for a GitHub repo: automatic reviews, @codex trigger commands, and pinning review standards into AGENTS.md."
---

Codex's GitHub PR review works better than I expected. Before opening a PR I already review the code several ways, in Claude and in Codex both. I've had the main agent review it, attached a different model as a subagent reviewer, run it in two stages. Code that survives all of that still gets caught by Codex, always one or two things.

This guide covers turning it on. What happens after that is a bigger story, and I pick it up at the end.

## Turning it on

Setup itself is three steps.

1. Set up Codex cloud for the repo. That means installing the GitHub app and granting repo access, and you need push or admin permission to change repo settings.
2. In Codex settings, toggle `Code review` on for the repo.
3. To have every PR reviewed without asking, also turn on `Automatic reviews`. Leave it off and Codex only shows up when you call it.

Automatic review also means the review lands the moment you open the PR. If you'd rather not collect comments on a draft, leave it off and call Codex when the branch is ready.

You call it from a PR comment.

- `@codex review`: review this PR
- `@codex security review`: look at it from a security angle
- `@codex review for issues in the database migration`: narrow where it looks
- `@codex fix the P1 issue`: have Codex apply the fix itself

To pin review standards into the repo, add a `## Code Review Rules` section to `AGENTS.md` and break it into `###` items. Repo-wide rules go in the root file; rules that only apply to one service go in the AGENTS.md closest to that code.

One more thing worth knowing: Codex only posts P0 and P1 findings to GitHub. Small stuff never shows up, so anything that does usually carries weight. That's exactly what makes it hard. Every comment looks correct.

Setup takes five minutes. The rest is the hard part.

## What happens once it's on

Codex judges strictly from the code, and both the side filing comments and the side fixing them are built to keep going until they're done. If nobody steps in, the rounds multiply on their own. One security-feature PR passed through 209 review conversations before it merged.

Living through that cycle left me with four response principles: read comments from how the product behaves, weigh them by user impact, understand how the fix relates to the existing code before touching anything, and if it isn't a merge blocker, file an issue or ignore it. Where those principles came from and why each one holds is in [209 AI Code Reviews: Accurate Is Not Necessary](/en/blog/ai-code-review-209-conversations/). If this guide got your reviews turned on, that post is what to read next.
