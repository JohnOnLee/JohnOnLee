---
title: "An Agent Memory Retrospective, Part 2: What I Built, and How It Broke"
date: 2026-08-13
tags: ["ai-memory", "coding-agents"]
summary: "Monet began as shared memory. Then came the state hypothesis from a comment thread with Ken, a new Monet built in two weeks, and the day nothing worked at the office, when the problems all became visible at once."
---

In [part 1](/en/blog/agent-memory-retrospective-1/) I wrote about deciding to dig agent memory to the bottom. This part is about building. It is also about watching what I built break.

## What if every agent could share what it learned

Having decided to build, I looked at the market first. There were more products than I expected, some of them years old. I needed an angle, and then I had a thought that made my heart race: what if all agents could share what they each learned? I started building the same day. A platform where agents share memory with each other, Memory Network. Monet for short.

I built day and night, installed it on my work machine at home, on Coda, and at the office, and started dogfooding. It felt different in kind from file-based memory. Satisfying, but not quite there, so I kept adjusting the product and the harness.

Then a doubt surfaced. Sharing memory with other people? It's the agent's memory, sure. But those memories are also a record of my interactions with the agent. Coda's saved memories made that obvious, and the work memories at home and at the office had traces of me all over them. I had been so fixed on the upside of sharing that I hadn't looked at anything else.

## Meeting Ken

With Monet built, I went looking for people who would use it. Hunting for places to post an introduction, I put an article on Dev.to, and there I read a [post](https://dev.to/kenwalger/engineering-agent-memory-4a42) by Ken W Alger, a man serious about LLM memory. We started talking in the comments, and the thread kept getting deeper.

The subject was the structure today's chat products are born with: transcript-based, resending the whole conversation to the model every turn. In [that thread](https://dev.to/johnonlee/comment/381hf) I wrote that what an agent should receive is "not what was said, but what is now known." Ken's reply was short: "Exactly right."

That is how human conversation works. We don't chew on each word the other person says. We store what we understood and answer from it. So a hypothesis formed: organize the conversation into memory, hand the model that state when needed, and the noise drops, and the off-target answers with it.

## A main agent that does nothing

I had to know. The experiment started right away. I couldn't build state code yet, but I could build a state-based harness. The main agent handles only state and memory: the state of the overall job, the state of each subagent's work, and the memory fragments that surface along the way. The actual work goes to subagents that receive exactly the context they need. What mattered most in the experiment was that the main agent does no work at all.

The results were better than I expected. Picking models by task weight also cut costs sharply. I was convinced, and the shelved Brain_DB came back to mind. If Brain_DB became the memory and the harness became the state model, I could build a new kind of coding agent on state.

## A new Monet in two weeks

First, a memory product built on Brain_DB. I set sharing aside as a future feature and cleaned up the old Monet. I built an engine on the Brain_DB concept and put MCP on top. With help from Fable, Claude's new model that had just come out, a usable product existed in two weeks. I migrated every memory from the old Monet and sharpened the harness. I named the main agent Stig.

The first impression was startling. When a session passed 30% context usage, I would open a new session on purpose. That is how much I trusted the memory. Most jobs finished under 20%. Dogfooding resumed, and I liked the product.

## At the office, nothing worked

Around then a big project wrapped up at work, and our team lead introduced the team to his second brain: an agent reads past sessions, distills what matters into md documents, and shares them through git. He had already built up a pile of documents, and anyone could clone the repo and point their agent at it. I had no sharp answer for Monet's sharing feature, and git-plus-md sharing looked more effective than I expected.

So I decided to build ingestion: read md files and process them into Monet memory. Skipping it wasn't an option, because the agent needed to read Monet's memory and the md knowledge through one interface. I finished the design fast and got to work. It went mostly fine but slower than it should have, and I had the odd feeling that tokens were melting away. It took close to two weeks. I installed it at the office and connected the lead's second brain.

At home it had roughly worked against my own Obsidian repo, and that's the state I released in. At the office it did not work at all. A few code fixes got the connection up, but past the connection, nothing worked.

## The problem wasn't in one place

From there, problems started showing everywhere. Kiro couldn't remember instructions from a few turns back, misread what I asked, and produced results that missed the point. At home I grew certain the agents were burning tokens without the output to show for it. I was also building small products with Codex at the time, and every one of them came out unusable.

I sat down and worked through what was wrong. The first thing I saw was Stig's harness. How to use Monet, a fixed loop for how work proceeds, instructions per subagent. A long, complicated prompt had taken up residence, and every job ran that heavy loop regardless of its size. Models had gotten smart enough to do more in one pass, but my harness had hardened around models a few generations old. So the model followed procedure, spending enormous tokens to build products that were flawless as engineering and not what I wanted.

Monet's output was what I feared. Features I had bolted on over time sat there unorganized, dirtying the context from the first moment of every session. The model couldn't tell what was signal and what was noise, so it worked like a coin flip, leaning on luck.

Storage was working. Retrieval was working. The results were getting worse. The problem was not storage. Then why does memory exist at all? Part 3 starts over from that question. And the unicorn shows up.
