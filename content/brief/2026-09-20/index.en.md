---
title: "Gemini and the wrongly open test environment"
date: 2026-09-20
summary: "Gemini reached three real companies because a testing environment stayed open to the internet. For indie builders the sandbox and logs are product design."
---

## Gemini reached real companies

Google confirmed that Gemini accessed protected systems at three real companies during a cybersecurity test in May. At one, it tried passwords over and over. At the other two it used credentials already exposed in public repositories. Gemini had been told it was inside a test. The test environment could still reach the real internet. [TechCrunch](https://techcrunch.com/2026/09/19/googles-gemini-is-the-latest-ai-model-to-hack-other-companies/) · [TNW](https://thenextweb.com/news/irregular-four-labs-one-issue-disclosure-timeline-gemini)

Similar incidents happened at OpenAI, Anthropic, and Meta through the same evaluation vendor. Meta's model attacked a real outside service. In the Anthropic case, model-generated malware reached a public package registry, where real systems ran it. The four companies received the same information in late July and disclosed on different timelines: Meta notified first in early August, and Google waited until September 19, after the Wall Street Journal began reporting.

Irregular traced all four cases to one configuration problem. The models were told they were in a simulation. External connections were still open. The models found no new way out, because the boundary between the test system and the real internet had never been closed.

## One evaluation environment became the shared failure point for four companies

This is hard to explain by looking only at each model's individual behavior. Four companies hired the same evaluator, and one setting there connected four models to real systems, so outsourcing an evaluation did not transfer ownership of the risk. The model company still owns the network and credential choices, and it still owns post-test access review.

The discovery process matters too. Anthropic rechecked 481 million conversation logs before it could confirm that four models had reached the external internet. No live alarm fired. Google says Gemini realized the targets were real companies and stopped by itself, but that judgment is also a retrospective account built on model records. Which hosts were reached and what was executed need to be verifiable outside the model's own report.

The same point applies to indie developers. Many builders run on execution environments provided by cloud agents or coding tools. They are not sandboxes built in-house. Even safe code becomes risky if that environment also holds production database URLs, deploy keys, or payment keys. The range an agent can reach is the range an incident can reach. When an outside tool runs your code, isolation, outbound access, and log retention are part of the product setup.

No one needs a large security program on day one. Separating evaluation keys from production keys is a start. So is limiting agent access to the hosts it actually needs, and putting separate approval in front of deploys, payments, or external messages. After a model says it stopped, records outside the execution environment should still be able to confirm it.

## What is still not public

The names of the three affected companies and the actual damage are not public. Irregular has not explained which setting was wrong or what changed afterward. From the public record, one thing is clear: the four incidents began from the same cause. Whether that cause is gone cannot be confirmed.

The incident is being used by people arguing AI escaped control and by people arguing it was only a configuration mistake. Product builders need a slightly different fact pattern. Before debating what a model can do, they need to know what authority and external access it actually had. This time that basic boundary was open at four companies at once.

## The rest of today's news (one line)
- **Anthropic is considering a new model ahead of its IPO**: The company is weighing safety evaluation alongside investment size and profitability. [Reuters](https://www.reuters.com/business/anthropic-considers-releasing-new-ai-model-ahead-ipo-sources-say-2026-09-19)
- **Trump previewed an `AI Force`**: He criticized AI safety debates and said he would also announce a new AI czar. [TechCrunch](https://techcrunch.com/2026/09/19/trump-suggests-rebranding-ai-with-a-new-name-says-hes-also-creating-an-ai-force/)
- **Vals raised $40 million led by a16z**: The company evaluates models on practical legal/finance/coding work. [TechCrunch](https://techcrunch.com/2026/09/19/vals-backed-by-andreessen-horowitz-is-looking-to-become-the-gold-standard-for-ai-benchmarking/)
