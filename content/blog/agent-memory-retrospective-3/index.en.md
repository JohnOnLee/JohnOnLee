---
title: "Agent Memory, Part 3: Perfection Is a Unicorn"
date: 2026-08-14
tags: ["ai-memory", "coding-agents"]
summary: "Clearing the wreckage sent me back to the first question: why does memory exist at all? An apple drawing, moments and principles, rules that changed nothing."
---

[Part 1](/en/blog/agent-memory-retrospective-1/) was about falling in. [Part 2](/en/blog/agent-memory-retrospective-2/) was about building things and watching them break. This is the last part. While clearing the wreckage I went back to the first question, and at the end of it I met the unicorn.

## I cut things first

The first job was a diet. I shrank the harness, cut the number of subagents, and merged scattered responsibilities. I rebuilt Monet and the harness around one aim: let the model use as much of its own ability as possible. And only then did I start asking again why memory is needed at all.

The usual assumption about agent memory is that storing well and retrieving well is the whole job. I assumed it too. But retrieved well, and then used how? Changing the question surfaced a more basic one. Why do people use coding agents in the first place? What do they want, and when are they satisfied?

The answer I landed on: the output that this team, this user, actually wants. Give two people the same instruction, "draw me an apple," and they expect different pictures. To produce what someone wants, the model has to know what that person wants. The method is surprisingly simple: describe the exact apple you want, or describe how to draw it. Provided, of course, that you know.

## Drawing an apple with code

I know nothing about painting. Still, I want a great apple drawing, with an agent's help. How? First, ask: "draw me a great apple." Take the picture, say what bothers you and what feeling you're after, and let the agent draw again. Repeat until you like it. That is how agents work today. The model moves on probability, shaped by its training, and the agent turns cycle after cycle closing the gap between what came out and what was expected.

Coding is similar. From an instruction the agent plans, writes a spec, writes code and tests, and cycles through checks: does it match the spec, do the tests pass, does the build hold. To get the output you want from this process, you have to explain what you want. If you knew everything from the start, you'd put it in the first prompt. There really was an era built on that: copying someone's supposedly perfect prompt, or engineering it further to fit your own taste. I think that era has passed, because two things are effectively impossible: "knowing everything" and "leaving nothing out." The work changes every time and keeps getting more complex, a perfect first prompt doesn't exist, and the cost of getting the wrong thing back is too high.

What remains is intervening in the process. When designing architecture, do it this way; when coding, this way; tests, this way. This should sound familiar. It's the standard content of CLAUDE.md and AGENTS.md. So is the problem solved? Something else feels familiar here. It's Stig's heavy prompt.

## It has to arrive at the right moment

What I want has to reach the agent at the moment it does that work. Which approach I prefer when it's weighing architecture, what the existing architecture looks like. If it isn't there at that moment, there's really no answer.

But there's a harder problem behind it. How do I collect and manage what I and my team want, without it becoming a burden? At which situations, at which moments, does it get injected? And how? Collecting means starting from what exists and continuously adding what gets discovered. I consider that one of agent memory's core jobs. Injection comes in two forms: push it through hooks that fire where needed, or have the agent read it in as the situation calls for it. I named the second one stages. At session start the agent learns which stages exist, and when a stage arrives, it reads the rules and applies them.

And what about things that must always apply, at every moment? Those I named principles, and they are just about the only content that has earned a place in CLAUDE.md. CLAUDE.md has to be managed strictly, and the reason goes beyond saving context. A model is trained inside a boundary, but nothing guarantees it always acts inside that boundary. So situations that require restraining the model keep coming up, and those restraints drift, very easily, into CLAUDE.md. It is a place that only fills up. Things with nowhere else to go land there, and they rarely leave.

## I thought I had it

It felt good. I thought I had found the whole answer. I built up my own principles and rules. Before long a small set of them was in place, and I confirmed they were injected or read in when needed.

But the behavior doesn't change. The output doesn't change either. One example. When coding is done, get a PR review from Codex, and here is how to handle what comes back. I wrote that as a rule, and there is even a monitoring script that watches the Codex review as it runs. For weeks, not one session ran that procedure correctly from the start. The rules were injected, sent, and read. And nothing moved. My trust in the agent went down instead, and as models get smarter, I expect this to get stronger, not weaker.

There is something I had to admit. "The way I want it done" and "the perfect output I want" never existed in the first place. What exists is the way the model was trained, and the way the model follows input. And that way will change with every new model and every new version. I had been sketching, in a place where no perfect product can exist, a product that isn't possible.

## The unicorn

When I first touched vibe coding through Antigravity, I believed the barrier to building had disappeared. So I spent my thinking not on how to build but on what to build, and I dug at agent memory without a break. Nine months later, this is where I landed.

Memory on its own no longer has a place to stand as a product. ChatGPT has memory built in. So does Claude. Storing, recalling when needed, answering with reference to it: all of that is table stakes now. From here on, memory has to be memory with a clear purpose.

And the thing I was trying to build, a memory that perfectly changes behavior and output, is a product that cannot exist. I call it a unicorn, for two reasons. Because it's an animal that doesn't exist. And because if someone actually built it, their company would become a unicorn overnight.

Part of me hopes this conclusion is wrong. It is also possible that my rules were simply clumsy. So I'm starting to measure. I want a record of which rule fired when, and what it prevented. In [a recent post](/en/blog/ai-code-review-209-conversations/) I wrote about handing agents the criteria for where work ends; this is that experiment's data too. In a few weeks I'll write here whether the numbers support the verdict or refute it.
