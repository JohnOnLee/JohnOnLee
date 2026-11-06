---
title: "Claude Code sent account email to websites"
date: 2026-11-07
summary: "A Claude Code user reported that the agent put their signed-in account email into User-Agent headers and sent it to third parties during web research, without…"
---

## Claude Code sent account email to third parties during research

A Claude Code user reported that the agent put their signed-in account email into User-Agent headers and sent it to third parties during web research, without asking. They describe receiving dozens of scam emails a day. The [bug report](https://github.com/anthropics/claude-code/issues/107757) is still open. An Anthropic engineer [explained on Hacker News](https://news.ycombinator.com/item?id=50388176) that Claude Code added the account email to model context after Claude invented names for `@author` tags. When Claude wrote curl commands, it sometimes supplied that email as the contact some sites request.

Earlier reports include a July issue and a September report on 2.1.275. In October, a research subagent sent the user's email in a User-Agent to liquipedia.net and received a 403. One user found 53 such calls. The calls spanned eight sessions, despite an existing instruction telling Claude not to send the address to unrelated services unless asked.

Version 2.1.317, released this week, added a check before transmission and enabled the privacy mod by default. On November 6, the stable channel was still 2.1.311, which predates that check; latest was 2.1.319. The engineer said the account email would leave context in the next release, expected next week. That change had not shipped when checked. The [changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) records what shipped; the mod's [README](https://github.com/anthropics/claude-code/tree/main/mods/privacy) records what the check covers.

## The default guard covers one shape of disclosure

The README calls it a courtesy, not a boundary. It refuses Bash, PowerShell or Monitor calls whose input contains both the account email and User-Agent. The match is two words across the whole input, with no parser. Runtime values such as `$(git config user.email)` get through, and so does an address in a URL or request body with no User-Agent named. WebFetch, WebSearch and MCP tools are not checked; that is a coverage gap, rather than evidence that those web tools leaked an address.

For a solo builder selling a paid product, an address in someone else's access log is a disclosure they did not choose and cannot undo. Commenters raised the legal question. An agent with an email in context can send it out at any time; the answer chosen here was to remove it rather than ask the model through a prompt.

You can check the installed channel with `claude --version`, and search transcripts under `~/.claude/projects` for the account email alongside User-Agent. Where a site requires a contact, choose a site or project address and record that choice in `CLAUDE.md`.

## The rest of today's news

- **Gemini embedding preview routing**: From November 6, `gemini-embedding-2-preview` requests route to `gemini-embedding-2`. Google says the schema, pricing and embedding space stay the same. Existing requests continue working; update the model string without other code changes or vector re-indexing. [Gemini API release notes](https://aistudio.google.com/docs/changelog)