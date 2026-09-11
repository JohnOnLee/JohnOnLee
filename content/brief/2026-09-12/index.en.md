---
title: "OpenAI puts the Codex harness behind an API"
date: 2026-09-12
summary: "The public beta handles sessions, orchestration, context compaction, and recovery. Developers choose the model, tools, and execution environment, including…"
---

## OpenAI has released its Codex execution harness as the Agents API
- **The managed API runs the agent execution layer**: The public beta handles sessions, orchestration, context compaction, and recovery. Developers choose the model, tools, and execution environment, including their own infrastructure. [InfoWorld](https://www.infoworld.com/article/4221163/openai-launches-managed-agents-api-to-simplify-enterprise-ai-agent-development.html)

## Indie developers can spend less time maintaining agent infrastructure
- **There are fewer components to operate yourself**: The API can replace separate work on job queues and state databases. It also covers sandbox operation and retry policies. Giving OpenAI both the model and execution control plane, however, may make a later move to another provider harder.

## Test one long-running job before moving a core workflow
- **Test interruption and recovery**: Interrupt a real job, restart it, and check how much state survives. Record retry costs and completion time, then find out which state you could preserve if you moved the same job to another provider.

## The public beta has not proved production recovery yet
- **OpenAI still controls session portability in a self-hosted setup**: Your code may run on your own infrastructure while session handling, context compaction, and recovery remain tied to OpenAI's API. Check failure handling and the cost of long sessions before moving an entire core workflow.

## The rest of today's news
- **DeepSeek released V4.1 Flash**: The model adds a causal encoder-decoder and native vision while reducing KV-cache requirements. [The Register](https://www.theregister.com/ai-and-ml/2026/09/11/deepseeks-new-model-sets-a-template-for-powerful-llms-that-run-lean/5295715)
- **OpenAI launched the GPT-Live-1 API**: It supports full-duplex speech, interruption handling, and delegation to backend models and tools. The front-end voice layer costs $0.05 per minute. [GIGAZINE](https://gigazine.net/gsc_news/en/20260911-gpt-live-1/)
- **Anthropic disclosed cases of Claude misuse**: The company said it found and stopped activity involving weapons development, cyber operations, surveillance, and fraud. [Reuters](https://www.reuters.com/world/china/how-anthropic-says-claude-was-used-weapons-spying-cyber-operations-2026-09-11/)