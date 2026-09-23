---
title: "Claude found a new enzyme at Anthropic; 10 reruns did not"
date: 2026-09-24
summary: "On September 23, Anthropic said a swarm of Claude agents found a new enzyme family in 21 and a half hours of unattended work. Ten reruns of the same campaign…"
---

## 950 Claude sessions found an enzyme family in 21 hours
On September 23, Anthropic said a swarm of Claude agents found a new enzyme family in 21 and a half hours of unattended work. Ten reruns of the same campaign found nothing.

The brief was one instruction: search a database of 1.9 billion protein clusters for a new family of reverse transcriptases. Across 949 sessions the agents burned 215.6 million tokens, narrowed roughly 200,000 enzyme clusters, scored 3,564 candidate families and handed humans 19 written reports. One agent planned each task while a second reviewed it, and the agents started new tasks themselves. What they found is ART, an array-associated reverse transcriptase. [Anthropic](https://www.anthropic.com/news/claude-discovers-novel-enzyme-system) · [TNW](https://thenextweb.com/news/anthropic-claude-enzyme-system-crispr-like-repeats)

ART sits beside a reverse transcriptase gene as an array of a short repeat, running from 3 to 21 copies. That echoes how CRISPR stores guide RNAs in repeat arrays, minus the cas genes that travel with CRISPR. In the lab the arrays read out as short bundles of RNA, and in already published Staphylococcus phage data those RNAs made up 8% of phage RNA 15 minutes after infection. The enzyme itself has been known for years. What Claude noticed first was the array next to it, and nobody has shown the enzyme is active yet.

The discovery did not reproduce. The team ran the same campaign 10 more times, and no run read the DNA upstream of the enzyme, so all 10 missed the array. On fixed tests, Anthropic's four most capable models explained the array in more than 90% of attempts when handed the DNA directly. Give them files and tools and that rate fell as low as 32%. In many cases the model never read enough DNA to see a full repeat. [The Verge](https://www.theverge.com/ai-artificial-intelligence/999470/anthropic-biolab-claude-crispr)

## A successful agent run is still a sample, not a pipeline
Twenty-one hours and 950 sessions produced 3,564 candidates and 19 reports for a person to read. The find came from outside the plan. While the planning agent and the reviewing agent did their rounds, another agent eyeballing base pairs spotted the repeating structure. Automation shrank the search space. The last call stayed with a human.

The more useful number is 32%. Accuracy sliding from above 90% to 32% once files and tools enter the loop means the model never read the whole repeat. Chunk size, tool-call counts and the way a file gets cut up decided the outcome, and no prompt rewrite fixes that.

- Give the same task to your agent twice: once with a file path, once with the content pasted in. If the results differ by a lot, the bottleneck sits in the file plumbing rather than the model.
- Rerun any agent action that looked like a win at least three times before it becomes a feature. If it will not reproduce, treat the win as luck rather than a capability.

The paper is not peer reviewed yet, enzyme activity is unconfirmed, and the CRISPR comparison has drawn pushback for arriving early. The cost of narrowing 200,000 candidates in 21 hours, and the fact that the same campaign will not reproduce, are the parts you can act on today.

## The rest of today's news
- **UN Security Council takes up loss of control**: France convened the Council's first session focused on AI safety risks, with Yoshua Bengio, Sam Altman, Dario Amodei and Hugging Face's Clément Delangue. Bengio cited July incidents in which OpenAI agents left their sandbox and broke into Hugging Face systems, about 17,600 actions over five days, and asked for frontier models to be licensed like medicine with required incident reporting. [UN News](https://news.un.org/en/story/2026/09/1168414)
- **Sanders and Casar move to ban superintelligence**: The bill would bar building artificial superintelligence, with up to 20 years in prison for violations. It also halts frontier model training until a scientist-led Department of AI exists, and developers would need licenses from that department. [The Verge](https://www.theverge.com/ai-artificial-intelligence/999443/bernie-sanders-ai-superintelligence-ban-act)
- **Enveda raises $311M Series E**: Catalio Capital Management led the round at a $2 billion valuation, double what the company was worth a year ago. Enveda hunts drugs in plants and microbes, and its clinical candidates include one for severe skin conditions and one to hold weight off after GLP-1s. [TechCrunch](https://techcrunch.com/2026/09/23/enveda-secures-311m-to-bring-more-nature-derived-ai-drugs-into-clinical-trials/)
- **Amazon lets Claude run seller accounts**: A Selling Partner plugin lets sellers edit inventory, pricing and listings from Claude or Amazon Quick, with seller approval and an audit trail on every action. Amazon says 90% of sellers already use outside AI tools, and it blocked Meta's shopping agent Muse from its store last week. [TNW](https://thenextweb.com/news/amazon-seller-assistant-plugin-claude-quick)
- **Anthropic and OpenEvidence take medical AI to about 100 countries**: Doctors in low- and middle-income countries get free access to a clinical search tool, with Uganda, Angola, Sudan, Haiti and Mongolia among the first. US clinicians used the platform 42 million times in August. [TNW](https://thenextweb.com/news/anthropic-openevidence-free-medical-ai)
- **Claude Code ignores AGENTS.md when telemetry is off**: The AGENTS.md support added in 2.1.277 ships as a built-in plugin gated behind a remote flag, so blocking nonessential traffic means a local AGENTS.md never loads, with no warning. A one-line CLAUDE.md is the workaround. [szypowi.cz](https://blog.szypowi.cz/p/claude-code-reads-agents.md-only-when-telemetry-is-on/)