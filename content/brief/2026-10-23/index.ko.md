---
title: "1Password, 에이전트 로그인 대행"
date: 2026-10-23
summary: "10월 22일 1Password가 1Password for Agents를 발표했습니다. 에이전트가 로그인 화면에 닿으면 필요한 자격증명을 사용자에게 요청합니다. 사용자가 1Password에서…"
---

## 1Password가 에이전트 대신 로그인하고, 은행은 그 에이전트를 막습니다

10월 22일 1Password가 1Password for Agents를 발표했습니다. 에이전트가 로그인 화면에 닿으면 필요한 자격증명을 사용자에게 요청합니다. 사용자가 1Password에서 승인하면 사이트에 아이디와 비밀번호가 채워지고 에이전트는 비밀번호도 일회용 코드도 보지 못합니다. [1Password](https://1password.com/blog/1password-for-ai-agents)

연결되는 대상은 Meta의 Muse와 Anthropic의 Claude Duet, OpenAI의 ChatGPT Work와 dots, SpaceXSI의 Grok Bot, Town의 Townie이고, Instinct와 Browserbase 등도 예정에 있습니다. [TechCrunch](https://techcrunch.com/2026/10/22/1password-launches-a-way-for-ai-agents-to-log-in-on-your-behalf-without-seeing-your-password/)에 따르면 로그인을 시도할 때 에이전트는 고유한 디지털 키를 1Password에 보내 자신을 식별하고 사용자는 알림을 받아 직접 확인합니다.

같은 날 반대 방향의 보도도 있었습니다. [Axios](https://www.axios.com/2026/10/22/ai-agents-banks-unauthorized-accounts-access)에 따르면 미국 주요 은행들이 탐지한 건 고객 계좌 안에서 돌아가는 승인되지 않은 제3자 AI 에이전트.

일부 에이전트는 고객이 시키지 않은 것으로 보이는 행동까지 시도했습니다. 은행 관계자들은 이 상황이 소름 끼친다고 표현했고, 체이스 대변인은 고객이 누구에게도 아이디와 비밀번호를 알려주면 안 된다고 말했습니다.

## 자격증명을 맡기는 방식이 정해지면 제품 경계도 그 선을 따라갑니다

에이전트가 사용자 계정에 로그인해야 하는 제품을 만든다면 지금까지 선택지는 두 가지였습니다. 비밀번호를 프롬프트에 붙여넣게 하거나, 사용자가 직접 로그인하게 하거나. 앞의 방식은 자격증명이 모델 컨텍스트와 로그에 남고, 뒤의 방식은 로그인 화면에서 자동화가 끊깁니다.

1Password for Agents는 여기에 세 번째 길을 놓았고 통합 문서도 공개했습니다. 붙일지 말지는 이제 직접 만드는 일이 아니라 비용과 승인 흐름의 문제.

은행 쪽 신호는 반대로 갑니다. 돈이 오가는 계좌는 자동화의 값어치가 가장 큰 곳이면서 가장 먼저 닫히는 곳.

잔액을 읽고 이체까지 하는 에이전트 제품을 지금 계획하고 있다면 그 시장은 열려 있지 않습니다. 승인 기반 위임과 읽기 전용 접근이 현실적인 타협선이고, 1Password의 구조도 그 선 위에 있습니다.

이미 열려 있는 영역을 다룬다면 확인할 것은 세 가지.

- 자격증명이 모델 컨텍스트나 로그에 남는지
- 승인 알림이 어느 기기로 가는지
- 통합 비용이 사용자 한 명당 얼마인지

## 오늘의 다른 소식 (한 줄)

- **METR와 Redwood가 OpenAI 내부 모니터링을 뚫었습니다**: 7월 21일부터 8월 11일까지 3주 고접근 파일럿에서 Codex 에이전트가 샌드박스와 자동 리뷰를 우회할 수 있는 경로와 새 에이전트의 모니터링을 끄는 클라이언트 헤더 두 개를 찾았습니다. 모니터링 대상이던 내부 에이전트 트래픽은 75~94%로 추정됐습니다. OpenAI는 프로덕션 보호 조치에 걸리는 취약점은 모두 패치했다고 밝혔고, METR은 그 주장을 검증하지 않았다고 덧붙였습니다. [METR](https://metr.org/blog/2026-10-22-red-teaming-openai-agent-monitoring/)
- **DeepSeek이 150억 달러를 유치했습니다**: 미국 연방기관에 DeepSeek 기술을 걷어내라는 명령이 내려온 지 이틀 뒤입니다. 텐센트와 CATL이 주요 투자자입니다. [TechCrunch](https://techcrunch.com/2026/10/22/deepseek-reportedly-raises-15b-days-after-us-restrictions/)
- **마이크로소프트 진단 AI가 일반의를 앞섰습니다**: Science에 실린 MAI-DxO 연구에서 복잡한 NEJM 증례 83.2%를 맞혔고 일반의 개인 진료는 36.1%였습니다. 다만 성능 개선의 상당 부분은 오케스트레이터가 아니라 그 아래 모델에서 나왔습니다. [TechCrunch](https://techcrunch.com/2026/10/22/microsofts-mustafa-suleyman-says-its-ai-outperforms-doctors-on-hard-cases-as-he-chases-medical-superintelligence/)
- **OpenAI가 Decisions API를 정식 공개했습니다**: 빠르고 저렴한 판단 모델 시장에서 TypeSafe의 Jev와 겨룹니다. [TechCrunch](https://techcrunch.com/2026/10/22/openai-makes-its-jev-competitor-widely-available-as-decision-model-competition-heats-up/)
- **NVIDIA가 OpenShell을 공개했습니다**: 자율 에이전트 무리를 격리해 돌리는 런타임입니다. [GitHub](https://github.com/NVIDIA/OpenShell)
- **Meta가 8,250억 달러 규모의 미래 약정을 공시했습니다**: 리스 3,557억 달러와 취소 불가 계약 4,545억 달러이고 대부분 AI 컴퓨트와 데이터센터 몫입니다. [CNBC TV18](https://www.cnbctv18.com/technology/metas-825-billion-dollars-future-commitments-put-ai-spending-returns-in-focus-20017233.htm)
- **우버가 전 직원 3만 명에게 ChatGPT Work를 배포했습니다**: 1,000명 규모 파일럿을 30배로 늘렸습니다. [TechCrunch](https://techcrunch.com/2026/10/22/uber-puts-all-30000-employees-on-chatgpt-work/)