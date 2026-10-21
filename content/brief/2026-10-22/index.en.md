---
title: "LiteLLM 1.107.0 malware came from the build, not the tag"
date: 2026-10-22
summary: "On October 21, LiteLLM 1.107.0 went out to PyPI and the Docker registries carrying credential-stealing code."
---

## LiteLLM 1.107.0 reached PyPI with credential-stealing code inside

On October 21, LiteLLM 1.107.0 went out to PyPI and the Docker registries carrying credential-stealing code. [LiteLLM](https://docs.litellm.ai/blog/security-incident-oct-21-2026)

Three extra files inside the wheel did the work. cook.pth, cook.py, sitecustomize.py landed in the root of site-packages, where Python runs them automatically on every start. An application that never imports litellm still triggers them. The stealer takes SSH keys, browser-saved passwords, cloud credentials, Kubernetes tokens, developer tool configs and the environment variables of readable processes. It also queries the LiteLLM proxy database for every upstream provider key stored there. The collected data leaves for www.litellm.dev, a lookalike of the real litellm.ai domain. [Wiz](https://www.wiz.io/blog/litellm-compromised-steals-credentials)

The compromise point was the build, not the source. The v1.107.0 git tag and the source tarball contain none of the malicious files, because the payload was injected into the build tree before the wheels were produced, and the wheel is the artifact pip actually installs. The attacker built from Berri-AI/litellm, a lookalike repository, and published that output. Three engineers' GitHub accounts were used to reach the release pipeline, apparently through stolen GitHub CLI OAuth tokens. [GitHub issue](https://github.com/BerriAI/litellm/issues/47826)

The affected PyPI wheels were live from 11:39 to 13:23 UTC. The Docker images ran until 14:20 UTC. All of it is gone now. The last safe release is 1.106.2.

## The work today is a host check

The first thing to check is whether you ever installed that version. LiteLLM is the gateway that puts many LLM providers behind one API. It passed 100 million PyPI downloads last month, and more than 2,000 packages depend on it. [Chainguard](https://www.chainguard.dev/unchained/litellm-attacked-again-malicious-1-107-0-wheels-on-pypi-and-docker-hub-october-2026)

In a proxy deployment the damage does not stop at one machine, because the proxy keeps provider keys in a single database. If 1.107.0 was ever installed, order matters. Do not start with pip in that environment, since every Python start runs the same code again.

- Delete cook.pth, cook.py, sitecustomize.py and their matching __pycache__ files from site-packages.
- Find and kill the detached Python process holding /tmp/remote_code_loader.lock.
- Rotate every credential the host could reach: instance roles, the provider keys in the LiteLLM proxy database, DATABASE_URL, and anything that sat in a process environment.

Rebuilding containers and virtual environments is faster than proving they are clean.

## The rest of today's news

- **OpenAI models are coming to Google Cloud**: frontier models and Codex workflows will be sold through Model Garden, with availability planned inside Antigravity and the Gemini Agent. [CNBC](https://www.cnbc.com/2026/10/21/openai-bring-its-ai-models-to-googles-cloud-expands-beyond-microsoft.html)
- **Anthropic opened a research preview of Claude Duet**: a background agent app on Opus 5.5 that sends a morning brief and asks before sending messages or paying. Waitlist for US Pro and Max subscribers. [Anthropic](https://claude.com/resources/articles/claude-duet)
- **Recursive released Flint, a laptop coding model**: a 40B mixture-of-experts model that activates 2.5B parameters, hits 131 tokens per second on a MacBook Pro, and ships on Hugging Face under Apache 2.0. The company says its automated research system did most of the work. [TechCrunch](https://techcrunch.com/2026/10/21/recursive-launches-flint-a-laptop-coding-model-it-says-was-largely-built-by-ai/)
- **Flapping Airplanes raised a $1 billion Series A**: nine months after launch, at a reported $6 billion valuation. The lab works on training large models with less data. [TechCrunch](https://techcrunch.com/2026/10/21/year-old-ai-lab-flapping-airplanes-raises-1b-at-a-6b-valuation/)
- **Two PHP core remote code execution flaws went public**: CVE-2026-109618 and CVE-2026-109619, CVSS 9.2, affecting every PHP release since 5.4. Patches shipped on October 21. [Wiz](https://www.wiz.io/blog/php2shell-php-rce)
- **Anthropic is short on compute**: AWS, Google and Microsoft now compete with Anthropic and are not handing over all the capacity it asks for. [India Today](https://www.indiatoday.in/technology/news/story/anthropic-is-struggling-to-get-compute-from-aws-google-and-microsoft-3021835-2026-10-21)