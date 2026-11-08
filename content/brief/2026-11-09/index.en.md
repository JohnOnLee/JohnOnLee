---
title: "Coding agents finish 26%"
date: 2026-11-09
summary: "A progress score cannot set a release date. In Co-Design Bench, the strongest of ten model endpoints, GPT-6 Astra, passed an average of 69.9% of acceptance…"
---

## Co-Design Bench separates partial credit from finished work

A progress score cannot set a release date. In Co-Design Bench, the strongest of ten model endpoints, GPT-6 Astra, passed an average of 69.9% of acceptance criteria per task. It satisfied every requirement on just 26.4% of tasks, according to [The Decoder's November 8 coverage](https://the-decoder.com/ai-coding-agents-still-need-human-cleanup-on-nearly-three-out-of-four-tasks-in-a-real-world-test/).

The [Co-Design Bench paper](https://arxiv.org/abs/2610.35138), submitted October 26, evaluates 273 tasks drawn from real user coding sessions, each pairing a normalized request with a runnable application before editing. Experts wrote 2,331 hidden acceptance criteria. One AI judge checks them by testing the finished app in a browser; another challenges positive verdicts, looking for mockups or hardcoded results. There is no reference implementation or target screenshot.

GPT-6 Astra fully solved about 41% of multimodal tasks and just under 18% of repository tasks, finishing least often on the track closest to actual product work. For someone building and selling a paid product alone, partial credit still leaves work to finish. Extracting an amount from a receipt and updating every dependent total can remain incomplete after several criteria pass. Passing 70% of requirements does not mean 70% of the development time is saved.

All ten endpoints lost ground once a task combined three or four change types. A single feature change usually moves layout and behaviour together, and a request like that leaves the largest share of the work to the person finishing it.

Task selection was deliberately hard. The researchers favored requests that users repeatedly rephrased or rolled back. Each task gets one fixed request, excluding follow-up questions and corrections during work. AI judges can also make mistakes, so results for ten endpoints under one harness on those tasks do not predict a particular repository's completion rate.

## Coding agents need a model and harness tested together

On larger overhauls, Qwen3.8-27B scored 75% in one harness and 56% in another. Which of two models performed better also depended on the harness. The authors recommend reporting the model and working environment together.

Token use affects the bill. On smaller changes, GLM-5.2 used nearly six times the tokens of GPT-6 Astra and still scored significantly worse, so paying more per task bought no better result here.

A tool buyer needs results from actual repository changes rather than leaderboard position. Test the model with the harness you actually use. Separate partial credit from finished tasks, and record the time you spend checking and fixing the result. The benchmark offers no conversion from missing criteria to repair hours, so weekly capacity has to come from the pair's completion rate and the hours you spend finishing what it leaves. A harness that helped here offers no guarantee of the same improvement elsewhere.

## The rest of today's news

- **DeepSeek Harness usage disclosure**: DeepSeek reported 1.54 million daily active users and about 92 trillion tokens per day, company figures reported by Bloomberg. [Bloomberg](https://www.bloomberg.com/news/articles/2026-11-08/deepseek-s-ai-agent-platform-hits-1-54-million-daily-users)
- **Anthropic account information notice**: Anthropic notified customers of unauthorized access by an outside security research firm; its notice excludes conversation content and passwords. [CellCog](https://cellcog.ai/blog/anthropic-breach-notice-email/)