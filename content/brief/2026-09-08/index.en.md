---
title: "Nvidia-Hugging Face openness test"
date: 2026-09-08
summary: "On September 3, Nvidia said it will buy Hugging Face for $12,930,300,000."
---

## Nvidia is taking Hugging Face for $12.9B, and this week the 'stays open' promise moved onto the US-EU antitrust stand

- **A $12.9B deal, closing in H1 2027**: On September 3, Nvidia said it will buy Hugging Face for $12,930,300,000.
- **The hub 18 million developers use moves under one chip vendor**: Hugging Face hosts 3 million models and 500,000 datasets. The deal is set to close in the first half of 2027 after regulatory approval. [Pondero](https://pondero.ai/news/2026-09-07-nvidia-hugging-face-acquisition/) · [NVIDIA](https://blogs.nvidia.com/blog/nvidia-to-acquire-hugging-face/)
- **The openness pledge is now the review's fault line**: Nvidia promised Hugging Face will stay open and hardware neutral, usable without Nvidia compute. Regulators and commentators now ask whether a dominant chip supplier that controls a critical developer platform can extend its reach across the ecosystem. [MLex](https://www.mlexwatch.com/ftcwatch/articles/2521533/nvidia-s-hugging-face-openness-pledge-identifies-us-eu-antitrust-fault-line)

## If your product runs on Hugging Face, neutrality is no longer a default you can take for granted

- **The owner of the neutrality promise changed**: Hugging Face stayed neutral across clouds and hardware vendors, and builders trusted it partly for that reason. Now the company that has to protect that neutrality is the strongest chip vendor in the ecosystem. In the near term, US and EU scrutiny effectively guarantees openness; that is not the same as being safe to lean on Hugging Face alone.
- **Keep one extra inference path**: do not route all inference through a Hugging Face centered stack. Holding a copy of the weights and one provider that does not depend on Nvidia's stack is the practical hedge.

## Audit your stack's vendor neutrality today, and mirror the Hugging Face assets you actually use

- **Mirror the models and datasets you deploy, and test an alternative host**: move the weights you rely on to another store such as Git LFS, and run one Space on self-hosting. Every asset you migrate is dependency you stop carrying.
- **Stand up a second inference provider**: bring up one inference route that does not sit on Nvidia NIM or its dedicated GPUs, then map which parts of your stack would break if Hugging Face tilted.

## The openness pledge is a statement, not a binding condition, so the variables stay open until the deal closes

- **A promise can shift before it hardens into a condition**: the open and hardware neutral commitment is company language. Until it is written into a regulatory remedy, treat it as adjustable.
- **The US and the EU may reach different conclusions**: the EU in particular could frame the deal as handing Europe's open AI infrastructure to one American company. What conditions regulators attach before the H1 2027 close is the variable to watch.

## The rest of today's news

- **Apple's September 9 event is almost here**: a first foldable iPhone and a CEO handoff to John Ternus are the headline expectations. [TechCrunch](https://techcrunch.com/2026/09/07/what-we-expect-from-the-upcoming-apple-launch/)
- **Computer-use agents still stall on long tasks**: on OSWorld 2.0's 108 long-horizon tasks, the best model, GPT-6 Astra, clears only 72.6%. [miraflow](https://miraflow.ai/blog/osworld-2-explained-computer-use-agent-benchmark-2026)
- **Matt Clifford steps down as ARIA chair**: the founding chair of the UK's high-risk research funder quit on September 7, five days after taking a government affairs role at Anthropic. [Unite.AI](https://www.unite.ai/matt-clifford-steps-down-as-aria-chair-after-anthropic-move)
- **Customers may soon whisper complaints into their phones**: a voice based feedback UX is drawing attention. [WIRED](https://www.wired.com/story/whispering-complaints-into-your-phone-may-be-the-future-of-customer-feedback)