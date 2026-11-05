---
title: "OpenSSH 10.6p2: AI bug reports moved the release schedule"
date: 2026-11-06
summary: "OpenSSH released 10.6p2 on November 5, 2026 to close a password authentication bypass. An attacker who can reach the SSH port sends a password between 257 and…"
---

## OpenSSH 10.6p2 closes a password authentication bypass

OpenSSH released 10.6p2 on November 5, 2026 to close a password authentication bypass. An attacker who can reach the SSH port sends a password between 257 and 1024 bytes long and logs in without knowing it. One connection is enough, and no retry is needed. The account that opens has no password set. A single account with a password elsewhere on the machine is enough to make that happen, and the attacker only needs the name of the unprotected account. [Alpine Linux](https://alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/)

The bug needs musl libc and sshd running without PAM, plus `PasswordAuthentication yes`, the OpenSSH default. On Alpine the machine must also hold an account whose password field is `*`. It needs at least one other account with a `$5$` or `$6$` hash. That `*` field is normal for key-only accounts, including root in the Alpine base image. musl's `crypt()` returns `*` to flag an overlong password, and sshd reads that as a match for the stored field. PAM-enabled sshd, systems with `PasswordAuthentication no`, and containers that do not run sshd inside them are listed as unaffected.

OpenSSH says the release notes brought a large number of security bug reports. Many are findings from AI models or made with AI assistance, and plenty have no security impact under a realistic threat model. It also notes cases where AI tools found a bug that another researcher later rediscovered independently. The team reads that as a sign that adversaries who never report bugs can find them too. So it will ship fixes more often instead of batching them for the next planned release, the [OpenSSH release notes](https://www.openssh.org/releasenotes.html) say. A day earlier, on November 4, [OpenAI](https://openai.com/index/a-thousand-fewer-paths-to-root/) published its own figures. One October run of its pipeline found and validated 948 local privilege-escalation vulnerabilities in the Linux kernel and generated patches. That was controlled research, and the attacks required an existing foothold.

## For a solo product, the patch signal now comes from OpenSSH's release notes

If you run a paid product and its server alone, the calendar you patch against changes. The signal comes from the upstream project's release notes, not the distribution's schedule. OpenSSH is shipping fixes between releases. Wait for the next quarterly window and the server keeps running the old code.

The routine is two things. Watch the release notes, then patch and restart on the day a notice lands. Alpine is explicit about the restart. Upgrading the package leaves the running daemon untouched, so new files sit on disk while the old sshd keeps accepting connections. The restart is what puts the patched code in front of traffic.

## The rest of today's news

- **GPT-6 Cyber**: OpenAI's first cyber model rated 'Critical' is initially available through the API and Codex only to selected Daybreak Red customers, so builders cannot assume ordinary API access when designing a security feature. [OpenAI](https://openai.com/index/introducing-gpt-6-cyber/)
- **Conductor**: Following Meta's acquisition, the cloud service becomes read-only on November 13 and shuts down on November 20 as data deletion begins; users need to move workspaces to the local app or export their data before November 13. [InfoWorld](https://www.infoworld.com/article/4245065/meta-acquires-conductor-as-ai-coding-shifts-toward-multi-agent-development.html)
- **Railway**: External network blocks triggered by scans with forged Railway source IPs still affected some networks on November 5 at 18:51 UTC, so diagnosing access failures also requires checking IP blocks outside the app's code. [Railway](https://status.railway.com/incident/QBCLHG1V)