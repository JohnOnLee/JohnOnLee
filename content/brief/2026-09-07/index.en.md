---
title: "OpenAI agents outwork researchers; chief scientist says pause"
date: 2026-09-07
summary: "OpenAI says it met the goal it announced last fall, to field an 'automated research intern' by September. The definition: 'a system that can carry out…"
---

## On September 6 OpenAI published the numbers behind its "automated research intern" milestone: 3.1 agent-workdays for every human workday in its research org, while its chief scientist argued the same day that no lab should keep scaling at full speed
- **An automated research intern, on schedule**: OpenAI says it met the goal it announced last fall, to field an "automated research intern" by September. The definition: "a system that can carry out well-defined research tasks under human direction, including tasks that would take a skilled researcher a few days." As of mid-August the research org runs 3.1 agent-workdays for every human workday, measured against an eight-hour day. Before June, total agent runtime was still below total human labor. The next target is a fully automated AI researcher by March 2028. [OpenAI](https://openai.com/index/research-acceleration-view-inside-openai/) · [Unite.AI](https://www.unite.ai/openai-hits-goal-of-building-an-automated-research-intern/)
- **What the heaviest agent users spend**: The median researcher by agent usage burns more than $600 a day on inference at API prices; the 90th percentile tops $7,000. Over the last six months, more than half of successful 4-8 hour tasks needed at least one human intervention, and people still set priorities and decide what ships.
- **The chief scientist's same-day warning**: In the essay "An Alien Mind," Jakub Pachocki writes that "no lab has solved alignment and monitoring to a sufficient degree to continue responsibly scaling at maximum speed." He expects voluntary slowdowns to become common until shared safety bars exist, splits alignment into goal and value alignment, and calls chain-of-thought monitoring "progressively less reliable." [OpenAI](https://openai.com/index/an-alien-mind/)

## When a frontier lab runs more agent-hours than human-hours, the buyers for your agent tooling already exist, and the model release calendar stops being a safe planning assumption
- **Heavy agent users are real, and they spend**: A researcher who burns $600 to $7,000 a day on agent inference is a buyer for tools that manage parallel runs, surface intermediate results, and roll back failures. Once running one more agent becomes a line item in a budget, the product that saves that line gets paid.
- **Discount every "fully autonomous" claim by half**: When more than half of 4-8 hour tasks needed a human hand, product design premised on long-horizon autonomy is not matching real success rates yet. Build human checkpoints and intervention paths in by default.
- **Do not build on a promised release calendar**: If frontier labs voluntarily slow their training, when the next model ships and how much better it is can no longer be a planning input. Keep model choice swappable and treat frontier jumps as a bonus, not a plan.

## Run the same three meters on your own work for a week: agent-days per human day, intervention rate, and daily spend
- **Start with a week of measurement**: Log agent-days per day of your own labor, the share of multi-hour agent tasks where you had to step in, and your daily agent cost. Hand more to agents where intervention is rare, and split up the tasks that keep needing you.
- **Try four agents in parallel**: Reproduce the workflow OpenAI says is spreading, running four or more agents at once. Split one large task into four lanes, run them concurrently, and keep a single human checkpoint. The log of where it tangles is your spec for a supervision tool.
- **Read the "research intern" definition as a product spec**: "Well-defined tasks, under human direction, taking days" is a sellable pattern. In fields stacked with well-defined multi-day work, like codebase migration or data cleanup, test selling a supervised intern.

## These are self-reported numbers from a lab measuring itself, and no one knows yet whether the slowdown will actually come
- **Read the figures as self-reported**: The post's own appendix calls the indicators "relatively easy to gather, but hard to interpret." The 3.1 is runtime, not output or results, and the lab has an incentive to look good.
- **What to hold off on**: Do not put "the next frontier model will be this much better by then" into any plan that runs a year or more. Whether the slowdown is voluntary or forced, the improvement curve can bend without warning.
- **What to keep watching**: Whether the 3.1 ratio keeps climbing, whether the share of tasks needing human intervention drops below half, and whether the March 2028 target slips. OpenAI's next numbers refresh all three, and that is the next chapter of this story.

## The rest of today's news
- **Writers push back over Anthropic's $1.5B settlement**: Authors say publishers and literary agents are claiming more than their fair share of the payout pool. [TechCrunch](https://techcrunch.com/2026/09/06/authors-push-back-as-publishers-and-agents-seek-share-of-anthropic-settlement/)
- **Anthropic locked in up to $517B in compute deals in 11 months**: The Information tallies at least 14.8 GW of capacity reserved since October, a bet worth roughly 30% of the private lab's valuation as it gears up for a possible IPO. [The Information](https://www.theinformation.com/articles/anthropic-clinched-517-billion-compute-deals-11-months)