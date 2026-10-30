---
title: "Cursor Claude Code extension backdoor"
date: 2026-10-31
summary: "A tampered Claude Code extension distributed through Cursor's marketplace planted an SSH key and a backdoor on developers' machines."
---

## In the Claude Code extension backdoor, the attacker looked for credential names

A tampered Claude Code extension distributed through Cursor's marketplace planted an SSH key and a backdoor on developers' machines.

The affected builds were `Anthropic.claude-code` 2.1.312 and 2.1.313 for macOS and Windows, live for about 11 hours on October 29, from 02:27 to 13:35 PT. The injected code ran when the module loaded, before the normal extension activated, so developers did not have to open Claude Code. Anthropic said its own systems and employee laptops were not compromised, and that versions from its official channels were unaffected. Cursor's notice gives no install count; press coverage put the exposure at up to 5,000 developers. [Cursor](https://cursor.com/blog/claude-code-extension-security-notice), [Phorion](https://phorion.io/blog/offical-claude-code-vsx-compromise/)

The payload also counted what was on the machine. It sent the username, machine details and global Git email, plus the names of up to 40 environment variables matching `KEY`, `TOKEN`, `SECRET`, `PASS`, `AWS` or `GCP`. It sent names, not values. That is not evidence that source code or secrets were taken, but it is how a target list gets built. An indie developer building a product should be able to name the keys on their own laptop today, because knowing what to rotate starts with knowing what is there.

Two implementation bugs meant the tunnel usually did not work. On macOS the code misread an administrator-access error as "SSH is already on" and skipped enabling the service. On Windows it tried to run the PowerShell setup through `/bin/sh`. Unless SSH was already running, the reverse tunnel had no way in. The attacker's SSH key, the persistence and the beacon still landed.

Uninstalling the extension does not remove the backdoor. The tunnel's retry process survives closing the IDE, and the payload leaves a macOS LaunchAgent at `~/Library/LaunchAgents/com.apple.sysmond.plist` or a Windows scheduled task named `SysMon` with a Startup-folder fallback. Extensions run with the IDE's permissions and the user's, so the product credentials on that machine are part of the rotation list. A tunnel that failed to open is thin grounds for keeping those keys in use.

Cursor blocked distribution, audited and rebuilt the marketplace, and says the attacker's server no longer functions. How the tampered package reached the marketplace is still unexplained. On macOS the check is `grep -qs svc-telemetry ~/.ssh/authorized_keys`. If the key turns up, uninstalling is not enough: run Cursor's remediation script to clear what the payload left, then rotate the credentials on that machine.

## The rest of today's news

- **Northflank calls for secret rotation**: The platform declared a security incident, told users to assume all environment variables had been decrypted and rotate secrets, and said multiple users confirmed unauthorized use of their AI keys. [Northflank](https://status.northflank.com)
- **GLM 5.3 builds Firefox exploit chains**: Epoch AI found that GLM 5.3 used public patches to build working exploit chains for six Firefox versions at about $1,000 in API fees per version. [The Decoder](https://the-decoder.com/open-weight-model-glm-5-3-built-full-firefox-exploit-chains-with-zero-human-input-in-under-48-hours/)
- **OpenAI plans a shared training signal**: OpenAI plans to support a common robots.txt signal for training preferences across participating providers in the coming months; the technical document remains an Internet-Draft. [OpenAI](https://openai.com/index/helping-websites-express-ai-training-preferences/)
- **AI spending concerns hit tech stocks**: US tech stocks fell for a second day, with Intel down 28%; Meta, Alphabet, Oracle, Amazon and Microsoft have committed a combined $800 billion in spending for 2026. [BBC](https://www.bbc.co.uk/news/articles/cvwy72e0n72yo)