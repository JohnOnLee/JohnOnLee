---
title: "Obsidian + GitHub: Notes You Can Write With AI"
date: 2026-08-18
tags: ["writing-with-ai"]
summary: "How to turn an Obsidian vault into a git repo backed by a private GitHub repository. The .gitignore, the sync routine, the numeric-prefix folder trick, and what all of it lets an AI do with your notes."
---

Obsidian became the strongest-positioned note app the moment LLMs went mainstream. There's one reason for that. A vault is nothing but markdown files in folders, and that collapsed the gap between how a person keeps notes and how an AI reads them.

Other note apps keep your writing inside their own format and their own database. For an AI to read any of it, either the app opens an API or you export first. An Obsidian vault is a directory. An agent reads it with `cat`, searches it with `grep`, and edits a file by opening it. Nothing has to be handed over.

That difference goes further than escaping export hell every time you switch apps. The AI reads your notes the same way you do. There's no translation layer between what's on my screen and what the agent sees, so "fix the third paragraph of that file" just works. Frontmatter, tags, links: all of it is only text.

A local folder alone isn't enough, though. There's no backup, and what I wrote on the laptop isn't on my phone. Put GitHub underneath it to solve backup and cross-device sharing, and you have something very close to a perfect set of notes to write with an AI.

## Turning the vault into a repo

The vault folder is the repository root. No extra structure required.

```bash
cd ~/Obsidian
git init
```

Write the `.gitignore` before the first commit.

```gitignore
.obsidian/workspace.json
.obsidian/workspace-mobile.json
.trash/
```

`workspace.json` holds screen state: which panes are open, which tab is active. It holds no note data, and its contents differ on every device. When you sync across machines, most of the conflicts you hit come from that one file. Leave it out from the start.

You can also ignore the whole `.obsidian` folder, which keeps the repo purely to notes. The cost is that plugins, themes, and hotkey settings stop following you between machines. I exclude only the two workspace files and commit the rest of the config, because cloning onto a new machine and having my setup arrive with it is worth more to me.

Attachments are worth one moment of thought. Text notes stay cheap no matter how many you write. Images and PDFs don't. Git stores a fresh copy of a binary every time it changes, so a vault full of pasted screenshots keeps growing regardless of how much actual writing is in it. When cloning starts to drag, that's when you decide whether the attachments folder belongs in the ignore list.

Now create a private repo on GitHub and connect it.

```bash
git remote add origin git@github.com:username/my-vault.git
git add .
git commit -m "Initial vault"
git push -u origin main
```

Make it private. Your notes have other people's names in them and ideas you haven't said out loud yet. Flipping a public repo to private later doesn't recall what already left.

## Not committing by hand

On the desktop, plain git works fine. But stopping mid-sentence to go commit in a terminal is not a habit that survives. Give it a few days and you stop doing it.

So install Git (`obsidian-git`, by Vinzent03) from the community plugin list. It runs automatic commit-and-sync on a schedule, and a side panel gives you staging, commits, diffs, and history. I set the auto-commit interval once and stopped thinking about it.

Mobile is a different story. There, the plugin runs on isomorphic-git, a JavaScript reimplementation, because a plugin can't reach a native git install on iOS or Android. The author says plainly in the README that mobile comes with real limitations. That's not a reason to give up, though. I use this vault on my iPhone. The setup is fiddly, but once it's in place it works better than you'd expect. I plan to write that one up separately.

Use two machines and you will eventually collide: a note edited on the laptop, edited again on the desktop, and both of them pushed. Markdown pays off here too. The conflict markers land in the file as ordinary text, so you open that note in Obsidian, pick the side you want, and delete the markers. In a binary format the app would have quietly picked a winner and you'd never learn what went missing. One habit cuts the frequency way down: pull before you open your notes.

## Line the folders up with numbers

Obsidian can only sort folders by a rule. There's no dragging a folder up or down to pin it where you want it, the way other note apps let you.

So my method is to put a number in front.

```
01_Ideas
02_Video-Scripts
03_Reference
04_Blogs
```

Set the file explorer to sort by name ascending and the folders fall into exactly the order I want. Two digits rather than one, because the moment you pass ten folders the order becomes 1, 10, 11, 2.

The AI gets something out of it too. The folder name is the category, so "file this under 03_Reference" is the whole instruction. I never have to explain where things go.

## What this unlocks

Once the notes live on GitHub, any tool that can read GitHub can read my notes.

A coding agent opens the vault folder as its working directory. It searches, it drafts new files. Pulling six scattered notes into one document happens there too. A chatbot with GitHub access can read the repo without cloning anything.

History is the part that actually changes things. When an AI edits a note, that edit is a commit. I read the diff, and if I don't like it I revert. That's why handing an agent write access isn't frightening. Backup is the side benefit; being able to undo is the point.

Connecting ChatGPT to this vault is covered in [the follow-up guide](/en/guides/chatgpt-github-obsidian/).
