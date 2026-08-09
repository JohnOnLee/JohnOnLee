---
title: "209 AI Code Reviews: Accurate Is Not Necessary"
date: 2026-08-11
tags: ["coding-agents"]
summary: "One security PR passed through 209 review conversations on its way to merge. Ninety percent were accurate. Where the human's job goes when accuracy is free."
---

Late last month a PR opened on our repo: [propagating secret taint across workflow steps](https://github.com/team-monet/aart/pull/10), a security feature. The numbers: 83 files, 21,962 lines added, 36 commits. And on the way to merge, 209 review conversations across two days. The code was written by Codex. The review was also Codex.

What those 209 conversations left behind is what this post is about.

## Ninety percent of the reviews were accurate

Let me be clear about one thing first. Codex reviews PRs well. By my feel, about 90% of its comments are accurate. It catches missed edge cases, drifted semantics, the spots a tired human reviewer would wave through. Before Codex I tried plenty of alternatives: having the main agent review its own work, attaching a different model as a subagent reviewer, running two-stage reviews. Even on code filtered that way, Codex still hooks one or two more.

But this isn't a Codex commercial. It's about what happens when accurate reviews arrive in unlimited supply. Accurate and necessary are different things.

## The tail chases the tail

The record of that first afternoon survives. I requested a review at 13:12, and by 15:08 I had posted twelve comments that begin with some variant of "addressed the latest findings." A round every ten minutes: one Codex comments, the other Codex fixes, the fixed code draws new comments, the fix of the fix draws more.

Take any single comment alone and there was nothing to argue with. These were accurate findings, arriving with P1 and P2 severity labels. The problem is the sum of directions. As rounds stacked up, the changes drifted toward ever-finer edge cases, away from what the feature exists to do.

This is not a Codex defect. It's structure. Coding agents and review agents are both trained to go all the way, and on this PR the two sides were even the same model. Put a Codex that fixes to the end face to face with a Codex that finds to the end, and an infinite cycle isn't an accident. It's the default.

## Define the end, or the end won't be your mountain

So the human's job moves. Reading reviews and applying them is something an agent now does more diligently than we do. What remains is defining the end: where this PR is done, which comments belong to this mountain and which ones are a trail to the next one over.

The model can't know that. What the product is for, which peak this climb is aiming at — that information isn't in the code. Leave the end undefined and the model will faithfully, accurately summit a mountain you never meant to climb.

That PR was headed the same way. That night, instead of chasing the findings, I wrote this down. Credentials used only for authentication stay usable. Secret values and anything derived from them get blocked automatically. I ratified those two sentences as the feature's contract. The next morning, the first line of my comment changed: not "addressed the latest findings" but "reworked around the ratified user contract." After that came one small follow-up and one final review request. A cycle that had run twelve rounds in two hours converged in two comments, and the PR merged.

Defining the end didn't mean killing the PR. It meant nailing down what the feature is for, instead of meeting each finding one by one. Once the contract existed, the accurate findings sorted themselves: the ones needed to keep it, and the ones that were accurate but not this mountain.

## The four principles the cycles left behind

After a few of these cycles I set principles for handling Codex reviews. Two weeks is early to call anything a principle, but two weeks of PRs later, these four are still holding.

- **Read each comment from the product's point of view.** Not "is this correct about the code" but "what changes for the user if I take it."
- **Weigh severity by user impact.** An accurate comment that prevents a crash and an accurate comment that polishes a name are not the same class.
- **Don't fix immediately.** Before reacting to a comment, understand how the fixed code will relate to what's already there. In a cycling PR, a hasty fix is next round's material.
- **If it's not a merge blocker, file it as an issue. Otherwise, ignore it.** An accurate comment that isn't needed now belongs in the tracker, not in this PR.

You can see what the four share. None of them are techniques for applying more review. They're techniques for applying less.

## Ignoring is judgment, not laziness

Looking back at the comments I ignored, most were good ignores. This feels wrong at first, because ignoring an accurate comment reads as laziness. But when 90%-accurate review arrives in unlimited supply, applying everything isn't diligence. It's losing the plot. An ignore is a judgment that this comment isn't our mountain, and that judgment is why a human is in the loop at all.

## What these principles assume

An honest line to close. These principles only work while someone who knows what the product is for stays in the loop. Ignore without knowing the essence and it really is laziness; you're not cutting the cycle, you're cutting quality.

One piece of homework remains. Could that essence be handed to the agent up front — not a human defining the end every time, but handing over the criteria for the end itself? I'm experimenting with that now. When the results pile up, I'll write them here.
