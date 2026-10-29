---
title: "Mistral Large 4: cost per task"
date: 2026-10-30
summary: "Mistral released the open weights of its trillion-parameter Mistral Large 4 model on October 29."
---

## Mistral Large 4 should be judged by cost per task in your repository

Mistral released the open weights of its trillion-parameter Mistral Large 4 model on October 29.

The model entered public preview on October 6. Mistral has since given it three more weeks of reinforcement learning and published the weights. For an indie developer choosing a coding agent's model, the tokens and price needed to finish a task matter more than the scale of the release. [Mistral](https://mistral.ai/news/mistral-large-4-oss/)

Mistral reports 48% on the Artificial Analysis Coding Agent Index, effectively tying GLM-5.3 while using 47% fewer tokens per task on average. On Terminal-Bench 4.0, it reports 41%, up 13 percentage points from preview, with 30% fewer output tokens. The announcement cites no independent evaluation.

When choosing a model for your product, you need to know how few tokens it uses to finish work at comparable coding performance, something you cannot judge from parameter count. The definition of finished matters as much. On Cognition's private FrontierCode 2.0 benchmark, which evaluates whether a repository maintainer would merge an agent's change, Mistral Large 4 leads at 19.7%. Use that criterion in your repository too: compare token consumption alongside whether you can accept and merge the result.

The new Mistral API prices are $0.70 per million input tokens, $0.07 per million cached input tokens and $2.10 per million output tokens. Keep input and output separate. To calculate what it costs to complete the change your product needs, apply those rates to actual usage, including the cached rate for cached input. A benchmark's 47% reduction in tokens does not establish a 47% reduction in your development bill.

The same cost test applies if you consider running the open weights yourself. Self-hosting a trillion-parameter model requires a multi-GPU cluster, so a hosted endpoint is the practical route for most small teams. You can compare costs by running your own tasks through the Mistral API or OpenRouter before choosing a model. Being able to download the weights does not establish that self-hosting is cheaper.

Keep the coding agent the same and give your current model and Mistral Large 4 the same tasks in your repository, then compare tokens and cost through to a change you would merge. Failed attempts count too. Include their usage in each task's record so you do not calculate costs from successful runs alone. Mistral Large 4 offers Low for simple tasks, Medium for everyday work and High, the default, for the hardest cases. Record the mode alongside the cost. Choose by what you pay to finish work at the quality your stack requires.

## The rest of today's news

- **Gemini file editing**: All Gemini app users can now generate, preview and edit files in chat; PDF editing works on web and mobile, while other file operations are web only. [Google](https://blog.google/innovation-and-ai/products/gemini-app/edit-files-directly/)
- **OpenAI allowance increase**: OpenAI doubled the Work and Codex allowance in Pro 100, Pro 200, Pro 500 and Business Premium, and cancelled the Pro 200 reduction announced in its September 29 email. [OpenAI](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- **Thrive agrees to acquire ADT**: Thrive Holdings agreed to acquire ADT in a $15.3 billion transaction, with plans to bring AI into home security. [ADT](https://newsroom.adt.com/financial/adt-to-be-acquired-by-thrive-holdings-in-15-3-billion-transaction)