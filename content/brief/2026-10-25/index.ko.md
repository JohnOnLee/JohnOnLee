---
title: "브로틀리 CVE-2026-111497, 런타임마다 따로 패치했습니다"
date: 2026-10-25
summary: "10월 21일 Node.js 보안 릴리스에서 CVE-2026-111497이 공개됐습니다. Node.js가 함께 싣는 구글 브로틀리 디코더의 경계 밖 쓰기 결함입니다. 앱이 공격자가 만든…"
---

## 브로틀리 CVE-2026-111497, 고치는 코드는 2월에 있었지만 10월에 나왔습니다

10월 21일 Node.js 보안 릴리스에서 CVE-2026-111497이 공개됐습니다. Node.js가 함께 싣는 구글 브로틀리 디코더의 경계 밖 쓰기 결함입니다. 앱이 공격자가 만든 브로틀리 데이터를 풀면 프로세스 메모리가 깨지고, Node.js는 원격 코드 실행까지 가능하다고 적었습니다. 수정 버전은 22.23.4 / 24.22.1 / 26.12.1. 신고자는 OpenAI Codex Security의 두 연구자입니다. [Node.js](https://nodejs.org/en/blog/vulnerability/october-2026-security-releases)

같은 결함은 Node.js 안에만 있지 않습니다. 구글은 10월 21일 브로틀리 1.2.1을 내면서 이 CVE를 보안 수정으로 표기했습니다. GitHub 보안 권고는 파이썬 패키지 brotli 1.2.1 미만과 brotlicffi 1.2.1.0 미만도 같은 문제라고 밝혔습니다. requests와 httpx, aiohttp는 이 패키지가 설치돼 있으면 브로틀리 압축을 알아서 풉니다. [GitHub 보안 권고](https://github.com/advisories/GHSA-9v8h-qqgm-4m35)

10월 23일 보안 업체 Aikido가 이 결함에 HTTP2Shell이라는 이름을 붙이고 영향 범위를 정리했습니다. 브로틀리를 함께 싣는 런타임과 프록시, 게이트웨이가 다 대상입니다. 패치 목록에 Bun 1.4.4·Envoy·Istio·curl이 올랐습니다. 빌더에게 더 중요한 대목은 따로 있습니다. 10월 23일 기준 권고 데이터베이스가 이 CVE를 PyPI 패키지에 연결하지 않아서, pip-audit와 Dependabot, Safety가 취약한 버전을 알려주지 않는다고 적었습니다. [Aikido](https://www.aikido.dev/blog/python-packages-vulnerable-node2shell-brotli-cve-2026-111497)

원인 수정은 2월에 이미 브로틀리 소스에 들어갔습니다(Aikido 분석). 그때는 보안 문제로 인식되지 않아서, 이 수정을 실은 릴리스가 나온 게 10월 21일이 처음입니다. 그사이 8개월 동안 같은 코드가 Node.js와 Bun, 파이썬 패키지 안에서 그대로 돌았습니다. Vercel은 10월 21일 WAF 규칙으로 들어오는 공격을 막았고, 그 규칙이 패치를 대신하지는 않는다고 밝혔습니다. [Vercel](https://vercel.com/kb/bulletin/node-js-security-advisory)

## 스캐너가 알려주지 않으니 런타임 버전을 직접 봐야 합니다

브로틀리를 직접 쓰는 코드에서만 들어오는 문제가 아닙니다. 서버가 요청 본문을 풀 때(Express 5에 body-parser 2.x를 붙인 구성), 내 코드가 fetch()로 받은 응답을 풀 때, node:zlib를 직접 쓸 때가 모두 같은 디코더를 거칩니다. 컨테이너 이미지는 다시 빌드하기 전까지 예전 런타임 그대로. 밖에서 받아오는 브로틀리 응답은 WAF 규칙에도 안 걸립니다. Node.js 20.x와 그 이하는 지원이 끝나 이번 수정을 받지 못하지요.

오늘 볼 것은 세 가지.

- CI 러너·컨테이너 이미지·로컬의 node --version을 확인하고 22.23.4 / 24.22.1 / 26.12.1로 올린 뒤 이미지를 다시 빌드합니다.
- 파이썬 프로젝트는 brotli 1.2.1, brotlicffi 1.2.1.0 이상으로 맞춥니다. 스캐너가 이 항목을 대신 알려주지는 않습니다.
- 지금 올릴 수 없으면 리버스 프록시나 미들웨어에서 Content-Encoding: br 요청을 거부합니다. 다른 서버에서 받아오는 브로틀리 응답은 이 방법으로 막히지 않지요.

## 오늘의 다른 소식 (한 줄)

- **Block이 음성만으로 학습한 실시간 대화 모델 Dessa를 공개했습니다**: 텍스트 없이 사람 대화 녹음만으로 처음부터 학습한 full-duplex speech 모델이고, 맥북 프로 M4 Max에서 로컬로 돌아갑니다. 벤치마크 대신 데모 녹음만 공개했고, 대기 명단을 열었습니다. [TechCrunch](https://techcrunch.com/2026/10/24/blocks-new-voice-model-sounds-eerily-human/)
- **Moonshot이 Kimi K3.1 Pro의 해킹 능력을 미리 낮췄습니다**: 10월 24일 Moonshot은 새 모델의 사이버 공격 능력을 학습 단계에서 줄였다고 밝혔습니다. 가중치 공개를 앞둔 조치입니다. [Reuters](https://www.reuters.com/technology/moonshot-curbs-hacking-ability-new-kimi-model-fears-grow-over-ai-powered-2026-10-24/)
- **Apollo: 기술 업종 밖에서는 AI 성과가 아직 안 보입니다**: 수석 이코노미스트 Torsten Slok은 10월 24일 노트에서 Mag 7의 근로자당 매출과 마진은 오르는데 S&P 493은 제자리라고 적었습니다. [Apollo](https://www.apollo.com/wealth/insights-news/insights/daily-spark/no-signs-of-ai-payoff-outside-the-tech-sector)
- **Replit이 AI 지출 대부분을 Anthropic에서 OpenAI로 옮겼습니다**: The Information 보도입니다. OpenAI가 30% 이상 할인한 연 1억 달러 규모 계약이고, Anthropic은 자체 할인을 중단했습니다. [Techmeme](https://www.techmeme.com/261024/p8)
- **Claude Code v2.1.310이 나왔습니다**: Bedrock과 Vertex, Foundry에서도 Monitor 도구와 플러그인 모니터를 쓸 수 있게 됐습니다. [GitHub](https://github.com/anthropics/claude-code/releases/tag/v2.1.310)