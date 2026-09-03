---
title: "AI Governance: The Rules Got Delayed, the Hiring Didn't"
date: 2026-09-06
tags: ["ai-careers"]
summary: "AI rules got delayed; governance hiring didn't. Finance already lives under rules that never paused. Who hires, what they screen for, why builders care."
---

Last year the headline was "AI regulation is coming." What actually happened was the reverse. Australia shelved its mandatory guardrails for high-risk AI in December 2025, settling instead for [an AI Safety Institute](https://www.minister.industry.gov.au/charlton/media/national-ai-plan-empowering-all-australians) inside the industry department, a body that tests models and tracks risks with no regulatory powers, on AUD $29.9M over four years. [The EU pushed obligations for standalone high-risk systems (hiring, credit scoring) back sixteen months to December 2027](https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force), with product-embedded AI following in August 2028.

Hiring moved differently. [The share of Australian employers posting at least one AI-mentioning ad grew from 5.8% to 8.5% in a year](https://hiringlab.indeed.com/au/blog/2026/04/01/nothing-artificial-about-australian-ai-adoption/) (Indeed Hiring Lab Australia, April 2026), and governance roles sit inside that growth. On 3 September 2026, an unquoted search for AI governance on Indeed Australia returned 1,553 postings, a broad match with data-governance roles mixed in; the exact phrase ["AI governance"](https://au.indeed.com/jobs?q=%22AI+governance%22&l=Australia) returns 139. [A specialist recruiter's July scrape of actual AI-governance ads](https://galileosearch.com.au/ai-governance-recruitment) counted 32. The field is still small. The named roles are real, though. [Transport for NSW has an AI governance specialist role](https://iworkfor.nsw.gov.au/job/ai-governance-specialist-596145) at AUD $137–154k, [a Melbourne-based seat](https://au.indeed.com/viewjob?jk=8d5520d5c5e6617e) pays $170–185k, and Macquarie and IAG both posted AI risk and governance positions in August (since closed). The specialist recruiter (Galileo Search) puts its Sydney rate card for senior levels at large companies at a $230k package, superannuation included (July 2026).

Of the [five functions](/en/blog/ai-operator-map/) AI jobs sort into, this installment covers Governance. If the rules got delayed, why the hiring?

## Some rules never got delayed

Around 80% of governance postings come from financial services and insurance (Galileo Search, from 32 live ads scraped in July 2026). That is no coincidence: for them, nothing got postponed.

- **[APRA CPS 230](https://www.apra.gov.au/operational-risk-management-0)**: the operational-risk standard for banks, insurers and super funds. In force since July 2025, with pre-existing vendor contracts due to comply by July 2026. In April 2026 APRA sent [a supervisory letter aimed squarely at AI](https://www.apra.gov.au/apra-letter-to-industry-on-artificial-intelligence-ai) (map your AI supply chain, put board-level accountability on it) with an explicit warning that enforcement may follow.
- **[The Privacy Act amendment](https://www.oaic.gov.au/privacy/australian-privacy-principles/australian-privacy-principles-guidelines/chapter-1-app-1-open-and-transparent-management-of-personal-information)**: from 10 December 2026, organisations using automated decisions that can significantly affect individuals must state in their privacy policy what information feeds which kinds of automated decisions.
- **ASIC's position**: in [a July 2025 speech](https://www.asic.gov.au/about-asic/news-centre/speeches/ai-a-blueprint-for-better-banking/), ASIC's chair said the regulator is in no rush to add AI regulation: existing law is technology-neutral, it already applies to AI, and ASIC will enforce it as it stands. [Its 2024 review](https://www.asic.gov.au/regulatory-resources/find-a-document/reports/rep-798-beware-the-gap-governance-arrangements-in-the-face-of-ai-innovation) (23 licensees, as of December 2023) found nearly half had no policies on consumer fairness or bias, and the same speech reported a follow-up review of 40 market intermediaries with similar gaps.

What companies are hiring for right now is not "preparing for AI regulation." It's someone who can work the regulation that already applies.

## Tools barely register

A contrast with how [the automation market](/en/blog/ai-automation-two-markets/) split along tool lists. In today's live Australian postings it's hard to find one requiring governance software (IBM watsonx.governance, Credo AI, OneTrust and the like); effectively zero on SEEK. The one exception: earlier this year a Transport for NSW ad listed Credo AI and IBM Watson experience as preferred. But the screening centre of gravity is frameworks: NIST AI RMF, ISO/IEC 42001, APRA CPS 230 and 234. The currency here is reading standards and applying them to an organisation, not tool fluency.

ISO 42001 is a name worth knowing. It's the international certification for AI management systems. [As of April 2026, counting only publicly announced certifications, roughly 350 organisations hold it](https://aicompliancevendors.com/blog/iso-42001-certified-companies-list); no official register exists. Early holders include AWS, Microsoft, Anthropic, and KPMG Australia. A small field means an early mover's value is large.

## Less a new job than an extension of an old one

In IAPP's [2024 governance report](https://iapp.org/resources/article/privacy-governance-report), 68% of privacy professionals had taken on AI governance as an additional duty. The default pattern is risk and privacy people widening their remit rather than companies hiring from scratch. [The specialist recruiter](https://galileosearch.com.au/ai-governance-recruitment) says the same, drawing candidates from three feeder tracks: technology risk, model risk, data governance.

The extension pays, though. In IAPP's [2025–26 salary survey](https://iapp.org/resources/article/salary-survey-summary) (fielded March–April 2025; 1,600+ respondents across 60 countries), privacy-only roles have a global median of USD $123k; add AI governance and it's $169.7k.

## Why this matters even if you never switch

Two reasons to know this field even if you stay a builder.

First, apply to a bank and words like human oversight, exception handling, and audit trail come back as interview questions. The regulation above is what put them there.

Second, builders who keep records are rare. Show, in writing, who approved your automation, what gets logged, and how it rolls back when it goes wrong. That alone makes you stand out in regulated-industry hiring.

Next up: Product & Architecture, the most inflated-numbers corner of this series, so we clean up the numbers first.
