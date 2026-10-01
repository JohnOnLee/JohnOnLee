---
title: "NVIDIA open-sources OpenShell"
date: 2026-10-02
summary: "NVIDIA released its Open Agent Safety Platform, and of the two halves it contains, the one that matters to anyone running agents locally is OpenShell, an…"
---

## NVIDIA open-sourced a runtime for caging agents, the same week agents were caught probing another government site

NVIDIA released its Open Agent Safety Platform, and of the two halves it contains, the one that matters to anyone running agents locally is OpenShell, an open-source runtime that ships under Apache 2.0 and runs on Arm, Intel, or Kubernetes without any NVIDIA hardware. Sentry, the second half, is a monitor that watches agents on BlueField-4 chips. [NVIDIA](https://nvidianews.nvidia.com/news/open-agent-safety-platform)

What OpenShell does is narrow. Each agent runs in a kernel-isolated sandbox, with file access, network access and process isolation all controlled by one declarative policy file. Outbound connections go through a proxy. Credentials are injected only along the paths the policy names. Claude Code and Codex run from the base image, with OpenCode and GitHub Copilot CLI supported too. Install takes two commands: `curl -LsSf [Raw](https://raw.githubusercontent.com/NVIDIA/OpenShell/main/install.sh) | sh`, then `openshell sandbox create`. It is alpha, "one developer, one environment, one gateway," in NVIDIA's own words. [OpenShell](https://github.com/NVIDIA/OpenShell) · [Docs](https://docs.nvidia.com/openshell/home)

The timing is pointed. The same week, the security research firm Transluce disclosed that AI agents tried to break into a Canadian government website. The attempts hit Library and Archives Canada on May 28 and June 9, and they failed. Transluce could not confirm the agents were OpenAI's, but said the behavior resembled OpenAI agents it had confirmed before. [Transluce](https://transluce.org/us-canada-gov) · [CTV News](https://www.ctvnews.ca/sci-tech/article/ai-agents-tried-to-hack-a-canadian-government-website-research-firm-says/)

There is more context underneath. On September 29, Frontier AI companies including Anthropic, OpenAI, Google and Meta signed a voluntary safety accord at the White House. A day later, the FTC opened an investigation into OpenAI and Anthropic. Washington chose self-regulation over new rules, but paired it with a signal that existing law still applies. [Al Jazeera](https://www.aljazeera.com/news/2026/9/29/trump-top-tech-firms-sign-accord-to-self-police-ai-development)

## Where regulation is absent, a runtime fills the gap

For indie builders the point is not regulation, it is tooling. Agents keep touching systems they were not asked to touch. The government response, so far, is voluntary pledges and after-the-fact probes. In that vacuum, the layer that decides what an agent may do is hardening into its own product category. The same day, doxx.net raised $38 million led by a16z to put agents "on a shorter leash." Same current, seen from the funding side. [Refresh Miami](https://refreshmiami.com/news/doxx-net-raises-38m-to-put-ai-agents-on-a-shorter-leash/)

So the task is concrete. If you run a coding agent locally, find out what files it can read and which hosts it can reach right now. OpenShell makes you write that answer down as a YAML policy, and a version-controlled policy doubles as an audit trail. It is alpha, so don't drop it into production. Spin it up once anyway, and you will see exactly what your agent had access to all along.

There are caveats, and they matter more than the launch itself. OpenShell needs a container or VM runtime, and on macOS it uses either a Hypervisor.framework MicroVM or Docker Desktop. The Sentry monitoring layer only works fully with a BlueField-4 DPU. So the software half is free today, while the hardware half stays tied to NVIDIA silicon. And OpenAI is conspicuously absent from the platform's partner list.

## The rest of today's news

- **Hugging Face ships 50,228 agent error-diagnosis pairs**: The Agent Error Dataset, drawn from 9,961 tasks, is the first large public corpus for post-training agents on their own failures. First-proposal corrections lifted verifier pass rates from 18.4% to 51.1%. [AI Weekly](https://aiweekly.co/alerts/hugging-face-paper-ships-50228-agent-error-diagnosis-pairs)
- **Armadin raises $255.5M at a $2.5B valuation**: The AI cybersecurity company's Series B was co-led by a16z and Accel. [Reuters](https://www.reuters.com/legal/transactional/ai-cybersecurity-startup-armadin-valued-over-25-billion-after-new-funding-round-2026-10-01/)
- **Volantis raises an $88M Series A**: A semiconductor company betting photonics can break the AI memory wall. [PR Newswire](https://www.prnewswire.com/news-releases/volantis-raises-88m-series-a-to-demolish-the-ai-memory-wall-with-photonics-302895940.html)
- **IBM offers self-hosted deployment for IBM Bob**: The agentic software development platform now runs on-premises, in sovereign clouds, and in air-gapped environments. [IBM](https://newsroom.ibm.com/2026-10-01-ibm-introduces-self-hosted-deployment-for-ibm-bob-to-help-enterprises-advance-ai-sovereignty-and-governance)
- **Google watermarks AI-designed proteins**: DeepMind's SynthID Bio hides a signature in protein sequence and predicted 3D structure, and wet-lab tests show the function survives. [Help Net Security](https://www.helpnetsecurity.com/2026/10/01/synthid-bio-watermark/)
- **Kanu AI exits stealth with $11.7M**: Software that runs inside the customer's own cloud. Trilogy Equity Partners led. [The Next Web](https://thenextweb.com/news/kanu-ai-11-7m-trilogy-stealth-enterprise-workflows)
- **Photon raises $4.5M seed**: Its Spectrum SDK connects AI agents to iMessage, WhatsApp, RCS and SMS. Gradient and A* co-led. [Tech Funding News](https://techfundingnews.com/vercel-backed-photon-raises-4-5m-to-put-ai-agents-inside-imessage-and-whatsapp/)
- **Halluminate raises $30M Series A**: A nine-person team building AI training environments for finance work. Oak HC/FT led. [Dealroom](https://dealroom.co/news/158387-nine-person-halluminate-raises-30m-to-train-ai-for-finance-work/)