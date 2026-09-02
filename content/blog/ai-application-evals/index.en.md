---
title: "What AI Engineer Job Ads Actually Screen For"
date: 2026-09-04
tags: ["ai-careers"]
summary: "Skip the framework anxiety. Senior AI engineer postings ask for evals, latency, and cost per request. Plus the real size of the Australian market."
---

Decide to become an AI engineer and the first thing you meet is a framework list. Learn LangChain? People say LangGraph is rising. What about CrewAI, AutoGen? Picking wrong feels like it will cost you a year.

The posting data settles that anxiety first. An agent-specialist job board [tallied 1,135 of its own listings](https://agentic-engineering-jobs.com/ai-agent-frameworks-job-market-2026) from March–May 2026 (the site doesn't name its operator, so read it as a snapshot). More than half of those ads name no framework at all. The ads that do name them average 2.31 each: LangChain in 392, LangGraph 256, LlamaIndex 150, CrewAI 106, AutoGen 74; and even LangChain, the market default, appears alone in only one of its eight listings. This is not a pick-one game.

The salary data points the same way, harder. Postings that name frameworks have medians of $185–190K, roughly $20K *below* the agent segment's overall median of $213K. Naming frameworks doesn't buy you a premium. For scale: the posted-salary median across 43,480 US AI-engineering ads is $176,000 ([Axial Search](https://axialsearch.com/insights/ai-engineering-jobs)). The agent segment sits a bit above that, though the two tallies differ in window and method, so don't read the gap as precise.

Of the [five functions](/en/blog/ai-operator-map/) AI jobs sort into, this installment covers Application.

## The sentences that repeat in real postings

Strip away the framework lists and read what senior postings ask for, and different words keep coming back. Two engineering ads and one PM ad that states the same demands from the other side. Condensed here; originals at the links.

- "Design evaluation harnesses and quality scoring — we use Langfuse, rubrics to measure safety, effectiveness, and personalization." ([Future](https://job-boards.greenhouse.io/future/jobs/4683133005), Applied AI Engineer, $215,000–250,000)
- "Improve our observability and instrumentation to profile agent behavior… design and implement infrastructure for low-latency agent execution." ([Harvey](https://www.harvey.ai/company/careers/04eb457b-e985-4e3b-9635-0a2b867ada97), Senior and Staff Software Engineer, Agents, $193,400–340,000)
- A role partnering with engineering and AI leadership across LLM orchestration, latency, caching, reliability, evaluation, observability, and cost; the phrase "cost per successful outcome" comes from here. ([HighLevel](https://jobs.lever.co/gohighlevel/13cbdf7e-ec82-4a0f-aec1-3bc55add776d), Principal PM, Conversation AI)

What the three postings share isn't a framework name; it's evals and operating numbers. And an eval isn't anything exotic: it's automated grading of whether your system answered well, against a set of reference answers you wrote: a golden dataset.

## You can put down the fine-tuning worry

The fear that this job requires training models keeps a lot of builders out. In a survey of 1,340 practitioners ([LangChain's own survey](https://www.langchain.com/state-of-agent-engineering), late 2025), 57% do not fine-tune at all. The working baseline is a base model plus prompting plus retrieval (RAG), tightened by evals. In the same survey, 57.3% already run agents in production and 89% have some form of observability. Learning evaluation and operations gets you closer to the ads than going back to ML math does.

## Tool names barely appear in the ads

Eval tools are only starting to register in job ads. In UK posting counts (ITJobsWatch, 2 September 2026), just two names show up at all: [LangSmith](https://www.itjobswatch.co.uk/jobs/uk/langsmith.do) (38 postings over six months) and [Langfuse](https://www.itjobswatch.co.uk/jobs/uk/langfuse.do) (31); Braintrust has no page. The salary columns aren't readable yet either; last year's samples were two or three postings each. That thinness is the signal: what companies screen for isn't a tool name but whether you can design evaluations and read operating numbers.

One protocol is the exception. MCP (Model Context Protocol) shows up in 17–24% of postings for every one of the five frameworks, the only thing in that data that cuts across all of them. Its security problems are growing just as fast, so "I can use MCP" has to mean "I can use it safely."

One fast-growing title deserves a caution: Forward Deployed Engineer, embedded with customers and accountable through production, [grew 729% in a year on US Indeed's index](https://www.aol.com/articles/job-postings-tech-role-grown-185134000.html). But the same title spans two pay tiers: an FDE at a frontier lab and an FDE at an ordinary enterprise are different jobs. Don't judge by the title alone.

## The actual size of the Australian market

If you're reading from Australia, set expectations from local numbers. On SEEK, ["ai engineer"](https://au.seek.com/ai-engineer-jobs) returns 1,177 listings, ["langchain"](https://au.seek.com/langchain-jobs) 30, and ["llm"](https://au.seek.com/llm-jobs) 101 (2 Sep 2026; keyword matches, so treat ratios loosely). LLM-specific roles are still few. The named hiring is real: Commonwealth Bank, including its subsidiary Bankwest, [is hiring GenAI and agentic engineers](https://au.seek.com/job/94157906), and [recruiter listings](https://au.seek.com/job/94242359) run to AUD $230–340k. Rough bands: $130–165k mid, $165–200k senior, $200–230k+ principal (aggregated from recruiter guides such as [Big Wave Digital](https://bigwavedigital.com.au/ai-engineer-salary-sydney-2026/), not official statistics).

## So what do you build?

Not a framework mastered; one small thing finished. Build a retrieval-backed Q&A over some documents and write fifty reference answers yourself. Automate the grading, measure latency and cost per request, and keep the records. Those are the words the postings above keep repeating.

What this project gives you is hands-on experience with evaluation and instrumentation. It does not substitute for the production-scale experience the senior ads also want. But juniors who arrive having done it are rare. You'll touch a couple of frameworks building it. You don't need to finish learning them first.

Next up: Enablement, the role that helps employees actually use AI well.
