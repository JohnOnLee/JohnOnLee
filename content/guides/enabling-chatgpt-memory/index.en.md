---
title: "Managing ChatGPT Memory: Review, Edit, Delete"
date: 2026-08-20
tags: ["ai-memory"]
summary: "How ChatGPT memory works now: reading and correcting the memory summary, project-only memory, and temporary chats."
---

ChatGPT remembers you whether or not you asked it to. If its answers start matching your tone one day, or it explains something on the assumption you do a job you never mentioned, that's memory.

It isn't only ChatGPT. Claude has memory, and so do most of the coding tools shipping now. The model consults it to give you the answer you're more likely to want. Use it without knowing about it and you have no way to explain why an answer came out the way it did.

There used to be a step where you said "remember this" and one line got stored. Not anymore. ChatGPT keeps track of whatever it judges worth keeping from your chats. So this guide is about managing it rather than switching it on.

## Two screens are in circulation right now

The memory settings screen started changing in June 2026. The new one has a single memory control and a memory summary. The summary is a written account, organized by category, of what ChatGPT thinks it knows about you, rather than a list of stored items. The old screen has two toggles ("Reference saved memories" and "Reference chat history") and shows the saved items as a list.

The new screen is arriving by plan and region, so your account may still show the old one. What follows describes the new screen, with notes where the old one differs.

## Reading and correcting the memory summary

Settings → Personalization → Memory. The path is the same on web and in the app. Many accounts have memory on already, so opening it to see what's in there comes before switching anything on.

Open the memory summary and you get what ChatGPT has written down about you. Most people are surprised the first time they look. You can correct it two ways: type the correction, or highlight a sentence in the summary and delete it. To clear the lot, use "Delete and turn off memory" from the three-dot menu on that page. It does what it says, wiping the summary and turning memory off with it.

On the old screen you get two toggles instead. Saved memories are managed as a list of items; chat history reference has no list at all. If you cleared every saved item and ChatGPT still seems to know you, the second one is on.

One trap: deleting a conversation does not delete the memories that came out of it. Clearing your chat list and clearing your memory are separate jobs, so something you thought you cleaned up can keep feeding into answers.

## Seeing what went into an answer

A personalized answer comes with a way to see which information fed it, and you can edit that information from there. Grabbing one answer that came out wrong and deleting the cause is faster than reading the whole summary.

## Keeping memory inside one project

Projects have their own memory setting. A project either uses your default memory or project-only memory. Set it to project-only and ChatGPT draws on conversations inside that project but won't pull in memories or chats from outside it. What happens inside the project stays out of your other conversations too. Open the project, then the three-dot menu, then Project settings.

That setting earns its keep if you run work and personal life through one account.

## When you want one conversation left out

Use Temporary Chat. A temporary chat doesn't reference existing memories and doesn't create new ones, and it stays out of your history. That beats switching memory off account-wide because of one sensitive conversation. Leave it on, and open a temporary chat for whatever you'd rather not keep.

## Getting something out of it

Automatic storing doesn't mean automatic tidying. Two things are worth doing yourself.

**Nail down the preferences with a long shelf life.** "Code examples in TypeScript, not Python." How you work, which tools you use, how long you want answers and in what language: say it once and it holds for months. Don't store anything that only holds for this week.

**Prune it now and then.** Open the summary about once a month and fix what's gone stale. Memory only accumulates, it never retires anything on its own, so a project that ended last year can still sit underneath today's answer as an assumption.

The same feature works differently once it reaches your coding environment. What piles up there is a team's rules and decisions rather than a few lines of personal taste, and the harder question becomes what not to store. I wrote about that in [Coding Agent Memory](/en/guides/coding-agent-memory/).
