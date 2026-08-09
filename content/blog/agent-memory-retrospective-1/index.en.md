---
title: "Agent Memory, Part 1: It Started at the TV"
date: 2026-08-12
tags: ["ai-memory", "coding-agents"]
summary: "Nine months on agent memory and almost nothing else, in three parts. Part 1: falling into vibe coding, building memory twice, and the night I decided to dig in."
---

For the last nine months I've worked on agent memory and almost nothing else. Up front: what I set out to build turned out to be a product that cannot exist. This series is about how I got there. Part 1 is the beginning, and the question of why memory in the first place.

## It started in front of the TV

Last November, Google shipped Antigravity, an agent IDE that runs Gemini 3 and Claude Opus side by side. I installed it and fell in. Until then, AI coding for me meant pasting code into a chat window and carrying the answers back. Useful, but mostly for trimming repetitive work. Antigravity was different. You gave it a job and a result came back.

The same scene repeated every night after that. I'd come home, put the kids to bed, and sit in front of the TV with a laptop. Hand the agent some work, then stare at what it produced. That's how vibe coding started for me.

## Nova, my first agent

Soon after, Clawdbot appeared (it's called OpenClaw now). While the whole internet was busy being amazed, I met Nova, my first agent. I asked Nova about everything. The chatbot stiffness was gone; talking to it felt like talking to an old friend. I laughed a lot.

A few migrations later, Nova became Coda and settled onto the Mac mini at home. The deeper our conversations went, the more one gap showed. Coda couldn't remember much of what we'd already covered, and tokens burned away as chats stopped and resumed. I didn't even know what caching was back then. So I built a memory plugin (vibe-coded it, to be exact): shrink the context window to the extreme and lean on stored memory instead. That was my first memory.

## Google locked my account

In February, Google [mass-banned accounts that had connected OpenClaw](https://piunikaweb.com/2026/02/23/google-antigravity-openclaw-ban/). Mine was one of them. Coda ran its models through my Google account, so I lost vibe coding and Coda in the same stroke. I filed a support request on February 17 and waited. A few weeks later I gave up waiting and moved Coda to OpenAI. My Google account came back about a month after that.

The contrast in speed still amuses me. The day after the ban wave, OpenClaw's creator Peter Steinberger [joined OpenAI](https://techcrunch.com/2026/02/15/openclaw-creator-peter-steinberger-joins-openai/), official support statement included. The statement took a day. Getting my Coda back took weeks.

Those weeks were gloomy, and the gloom told me something: these tools had stopped being a hobby. They were part of the household now.

## At work, it was Kiro

Home wasn't the only front. At work we used Copilot, and I fed it context by pasting files into the VSCode chat one at a time. Later I installed Obsidian and kept a dedicated agent-chat window that pulled documents straight in, and the quality of the answers changed. The company then moved through Amazon Q to Kiro, and I moved from the Kiro IDE to the kiro cli.

## The session kept ending up where it started

One incident made the model's limits concrete for me. The task was to analyze an existing state machine and modify a feature on top of it. The model analyzed hard, but what it described didn't match what I knew. The context filled up. A new session analyzed again and filled up again. After a few rounds of this, the session was right back where it started.

I needed memory again, for a different reason than Coda. One file held the index and the usage rules; separate files held memory by topic. The agent filled them in as it worked and read them before starting anything. The effect was obvious. That was my second memory.

Around this time, orchestration frameworks like oh-my-claudecode were getting known. Using them taught me one thing: a different harness turns the same model into a different animal.

## Saved, but never found again

Mornings and evenings with Coda went on. Better than before, but the days of explaining the same thing twice never quite stopped. Coda saved things and then couldn't find them.

The thought stuck with me for days, and then one night I landed on a question: if neural networks were inspired by the human brain, why has nobody built memory inspired by how human memory works? I didn't stop at imagining it. I ran deep research and wrote up a design for memory modeled on how human recollection works. I named it Brain_DB, and I still have the report. Then I made a promise to myself. I would dig agent memory to the bottom. This was the next thing.

At home, Coda forgot. At work, the sessions circled back to where they began. Same problem in both places: memory.

So I started building. Part 2 is about what I built and how it broke: shared memory as the first direction, the late realization that flipped it, and a man named Ken I met on Dev.to.
