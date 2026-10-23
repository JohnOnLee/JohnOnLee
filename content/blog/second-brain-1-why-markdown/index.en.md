---
title: "Second Brain in Markdown (1): Why Obsidian and Plain Files"
date: 2026-10-23
tags: ["ai-memory", "coding-agents"]
summary: "Why my second brain is Obsidian and Markdown files: leaving Notion, the database memory that stalled at work, and the first requirement I set after."
---

I spent two weeks building a way to load my company's second brain into a database, and only then realized mine should just be a folder of Markdown files. I now view that folder in Obsidian, and my agents read and edit the files directly.

This series takes the second brain I use, O2B, apart one piece at a time. Part 1 is the bottom layer: why Obsidian and Markdown files.

## Why I left Notion for Obsidian

I used Notion first, before Notion had AI. To get an AI to work on a Notion page I had to keep copying the content over and pasting it in, and if the page had a table, I had to move that separately and fix it by hand.

Switching to Obsidian removed all of that. I tell the AI "the file is here, read it," and it reads it, edits it, and I see the result right there. The person and the AI are looking at the same file. I wrote that up in the [Obsidian + GitHub guide](/en/guides/obsidian-github-ai-notes/), so I'll keep it short here.

## The database I spent two weeks on stalled at work

Sharing a file with an AI was solved by Obsidian. Agent memory was where I took a wrong turn. As I wrote in the [agent memory retrospective](/en/blog/agent-memory-retrospective-2/), I was building Monet then, a platform that collects what agents remember. A team lead at my company introduced a second brain where agents summarize their work into Markdown, people review it, and Git shares it. It worked better than I expected. I still spent two weeks building a feature that converts those Markdown files into Monet's database memory. It roughly worked at home. At work I connected the lead's repository, and after the connection, nothing worked.

I never found the exact cause. What was clear is that files agents could already read existed, and I had added a database layer on top. Checking what had piled up inside Monet wasn't easy for a person either.

That's when I saw what was needed: a shared brain that people and agents both look at and edit. Monet was closer to one agent's own brain.

## So the first requirement was files

The first requirement for O2B, my second brain, came out of that: anything that has to last lives in files owned by a person, in Markdown. Three things follow.

- When a person edits a file, that edit is the truth. Nothing else needs fixing in a database or an agent's memory.
- Search indexes and embeddings are conveniences. If they vanish, rebuild them from the files.
- If any agent, model or runtime disappears, the brain stays readable and useful.

## What makes Markdown good for a second brain

It opens anywhere. Markdown is plain text, so you don't need Obsidian. It opens in VS Code, in a terminal, on GitHub's website or in any phone editor, and switching tools needs no export step.

Agents have no barrier to reading and editing it. An agent reads with `cat`, finds with `grep`, and opens a file to change it. Nobody has to open an API or export anything.

It also has room to grow. Folders, front matter (the block at the top of a file for properties like title, date and status) and links between documents all live in the same files. Use structure only where it's needed; you don't have to design the whole thing up front.

## Obsidian is just a window

Obsidian is comfortable to use: you move between notes with links and backlinks, browse a folder tree, and search. But I don't depend on it. I split the roles like this.

Markdown holds the content and is the source. Obsidian is the window a person looks through, and the folder survives without it. Git keeps history and moves files between machines.

## Three snags before I built it

Before building O2B I ran 15 Git checks and 9 Obsidian checks (Git 2.39.5, Obsidian 1.13.7). Moving between notes, search, link resolution and renaming all passed across repository boundaries, and so did edits made from outside Obsidian. Three things snagged.

- Cloning a parent repository doesn't bring the independent repositories inside it, so a deployment needs an explicit list of the repositories to fetch.
- A symlink doesn't carry the content of the file it points to.
- When two notes share a name, Obsidian resolves a link to just one of them, so an ambiguous link needs the full path.

There's also what those checks didn't establish. I haven't verified access separation, whether concurrent writes keep content intact, or restoring from a backup.

## To start

1. Make a folder and open it as a vault in Obsidian. The [guide](/en/guides/obsidian-github-ai-notes/) shows how.
2. Run `git init` in that folder and make a first commit.
3. Create a first file, `BRAIN.md`. What goes in it is the next part.

The tools keep changing, agents and models included. Ask your own second brain whether you could delete everything except one folder and still read it.
