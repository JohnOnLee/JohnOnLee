---
title: "Cloudflare absorbs Deno, ends Deno Deploy"
date: 2026-10-10
summary: "On October 9, Cloudflare and Deno announced that the entire Deno team is joining Cloudflare. Ryan Dahl, who created Node.js, and co-founder Bert Belder will…"
---

## Cloudflare has taken on the whole Deno team, and Deno's runtime and hosting service are winding down

On October 9, Cloudflare and Deno announced that the entire Deno team is joining Cloudflare. Ryan Dahl, who created Node.js, and co-founder Bert Belder will lead the work of merging celld back into workerd. celld is the open-source implementation of Workers and Durable Objects that Deno shipped in August; workerd is Cloudflare's open-source runtime. Both companies describe the goal the same way: make the Workers programming model a supported way to run servers on your own hardware as well as on Cloudflare's network. The acquisition price was not disclosed. [Deno](https://deno.com/blog/cloudflare) [Cloudflare](https://blog.cloudflare.com/deno-joins-cloudflare/) [The New Stack](https://thenewstack.io/cloudflare-acquires-deno-ryan-dahl/)

The timelines are written into the announcement. The Deno runtime gets monthly bug fixes and security patches for one more year; after that, Deno stops developing it, the code stays open source, and anyone who wants to continue is welcome to. Deno Deploy keeps running for six months and then shuts down, with migration support to Cloudflare Workers for paying customers. The JSR package registry stays up and moves its infrastructure to Cloudflare. Cloudflare also said that after open-sourcing workerd it expected the community to adapt it to every environment and that never happened, and that its self-hosted Durable Objects support stopped at a single instance, good enough for local testing but unable to scale.

## The near-term work is a migration checklist, and the open question comes after that

If you run something on Deno Deploy, you have six months. If you only use the runtime and manage your own servers, you are keeping a runtime that will receive no new features a year from now. Nothing breaks today, but if you planned to build new services on Deno next quarter, decide the direction before that.

The change that will last longer than these deadlines is who owns the exit route. workerd is the same code Cloudflare runs in production, and it existed so that teams could move a Workers app to their own infrastructure. The team that built the substitute, celld, has now joined Cloudflare, and the self-hosted version of Durable Objects will be built by Cloudflare itself. That model suits agent products well. A Durable Object behaves like a small server with its own SQLite database and holds WebSocket connections, so per-user state and live connections for an agent harness can be sharded the same way. celld is a single Rust binary whose only external dependency is an object storage bucket.

None of it is ready to put in production. The merged workerd and celld does not exist yet, and both companies promise only more announcements in the coming months. Neither a shutdown date for Deno Deploy nor an end date for runtime support was published, just a year and six months. If you were planning to self-host, this is a good week to spin celld and workerd up locally rather than to commit a new project to Deno as its default runtime.

## The rest of today's news

- **Anthropic opens dynamic workflows in Claude Managed Agents to beta**: an agent writes a workflow program that runs up to 1,000 sub-agents in phases and merges their results. Anthropic says a single agent found 14 to 27 of 70 bugs planted in a 116,000-line codebase, while the workflow found 66. [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview)
- **Oxide Computer raises a $445M Series D**: led by Eclipse with AMD Ventures and existing investors. The on-premises cloud hardware company says it paid income tax in spring 2026 out of ordinary operations. [Oxide](https://oxide.computer/blog/our-445m-series-d)
- **OpenAI defends firing three safety researchers**: the company called it a significant breach of trust and denied the dismissals were about speaking out, while the researchers warn of a chilling effect. [CNBC](https://www.cnbc.com/2026/10/09/openai-fired-researchers-ai-concerns.html)
- **OpenAI's annualized revenue is near $50bn, with $70bn projected by year-end**: the $50bn figure is as of the end of September, and Bloomberg reports the company told investors it expects $70bn or more by December. [TNW](https://thenextweb.com/news/openai-revenue-70bn-year-end-50bn-september)
- **Arena raises $200M Series B and ships an Alignment Index**: the AI evaluation company is valued at $3.1bn in a round co-led by Lightspeed and Khosla, and published a metric for whether agents follow instructions and report completion accurately. [Tech Startups](https://techstartups.com/2026/10/09/startup-funding-news-today-october-9-2026-arena-bloomx-ocean-scanntech-more/)