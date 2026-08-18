---
title: "Connect GitHub to ChatGPT: Obsidian Vault as Project Context"
date: 2026-08-18
tags: ["writing-with-ai"]
summary: "How to wire a GitHub-hosted Obsidian vault into ChatGPT: connecting the app, scoping repo access, and attaching the vault to a project."
---

Once you finish [putting your Obsidian vault on GitHub](/en/guides/obsidian-github-ai-notes/), what you have is a repository full of md files. On its own that is a backup. It starts being useful when ChatGPT can read it.

Three steps. Connect GitHub to ChatGPT, scope the access down to the vault repository, then create a project and attach that repository to it. After that you just talk inside the project.

Obsidian has an easy time here for a boring reason: the vault is already nothing but markdown files in folders, so there is nothing to export or convert before handing it to a model. The format you read is the format the model reads. An app that keeps your notes in its own database would have stopped you at this step.

## Connect GitHub

Open Settings and go to Apps. Depending on your build it may still say Connectors; same place. Find GitHub in the list, connect it, and GitHub's OAuth screen takes over. That screen is where you pick which account and which repositories ChatGPT gets to see.

Slow down here. Clicking through gives away everything, and I picked the vault repository only. Notes carry a lot more private material than code does, and unlike a code repo I have never gone file by file asking whether a given line is fine for someone else to read. You can change the scope later: Settings → Apps, open GitHub, then Choose repositories.

A private vault is fine. Access follows whatever your GitHub account already has permission to see, so there is no reason to make the repo public. There was never a good reason to publish your notes anyway.

If you are on a work account, GitHub may not appear in the list at all. On Enterprise and Edu workspaces an admin has to allow apps in workspace settings before anyone can connect one.

## Create a project and attach the vault

Connecting the account is not the end of it. You still create a project and attach the vault repository to that project as a source.

The project is worth the extra step. You can point at a repository from a normal chat, but then you explain yourself again every time. A project shares its sources and its instructions across every conversation inside it. You write "use my vault" once, and the related conversations end up in one place instead of scattered through your history.

A project's detail view separates its chats from its sources, and you add material on the sources side. If the labels on your screen don't match mine, look for the place in the project's sources area where you pick a connected app. This part of the interface changes often.

Write the project instructions while you are there. Two lines were enough for me.

```
Search my vault notes before answering.
Cite the file path of any note you based an answer on.
```

The second line matters more than it looks. Without it you cannot tell whether an answer came out of your vault or out of general knowledge. If no path shows up, assume the vault wasn't touched and ask again.

## The part that actually pays

Start a conversation inside that project and ChatGPT pulls from your notes without being told to. You stop attaching files and stop re-explaining the background at the top of every chat.

The gap shows up on questions that need your own context. General questions were always answered fine. But what you decided six months ago and why, or what you tried and abandoned, exists only in the vault. "If I've written about this before, read that first and then answer" turns into a request that actually works. That answer does not exist without the vault attached.

Know what gets read before you rely on it. The connector reads markdown, text, and code files, and it does not read commit history. A markdown-first vault loses nothing there, but PDFs and scanned images sitting in your attachments folder do not come through this path.

Right after connecting a vault, give it a moment. Indexing takes a while, so if a note you just committed doesn't turn up, wait and ask again.

## Turning conversations back into notes

When a conversation runs long and lands on something worth keeping, ask for it as a note. It has already seen how the rest of your vault is written, so the front matter and title conventions usually come out close to right.

Saving is still your job. The GitHub connection reads; it will not commit to the repository for you from a chat. Paste the note into Obsidian and commit it yourself, which is the reliable option today.
