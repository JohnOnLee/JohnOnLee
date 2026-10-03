---
title: "COSMIC, AI가 쓴 PR을 전면 금지합니다"
date: 2026-10-04
summary: "System76이 개발하는 리눅스 데스크톱 환경 COSMIC이 AI가 만든 기여를 받지 않기로 했습니다. 10월 2일 바뀐 PR 템플릿에는 '이 PR에 LLM이 생성한 코드, 주석, 설명을…"
---

## System76의 COSMIC이 LLM이 만든 코드, 주석, PR 설명까지 모두 거부합니다

System76이 개발하는 리눅스 데스크톱 환경 COSMIC이 AI가 만든 기여를 받지 않기로 했습니다. 10월 2일 바뀐 PR 템플릿에는 "이 PR에 LLM이 생성한 코드, 주석, 설명을 넣지 않았고, 변경 사항을 온전히 이해하고 있으며, 리뷰에 응답할 수 있다"는 항목이 들어갔습니다. 이 확인 문구가 없으면 PR이 닫힐 수 있습니다. cosmic-flatpak만 예외인데, 그쪽 매니페스트는 상류 프로젝트가 직접 관리하기 때문입니다. [Linuxiac](https://linuxiac.com/cosmic-stops-accepting-llm-generated-content-in-pull-requests/) · [XDA](https://www.xda-developers.com/cosmic-bans-all-ai-generated-submissions/)

이유는 명확합니다. COSMIC 공동 창업자 Jeremy Soller는 LLM 덕분에 처음 기여하는 사람이 크게 늘었지만, 그 제출물이 "계획에 없던 것이고 거의 받아들여지지 않았다(unplanned and rarely accepted)"고 말했습니다. 리뷰 부담이 감당이 안 된다는 것입니다. 이 결정은 혼자가 아닙니다. Void Linux는 AI가 쓴 텍스트를 금지했다가 유지관리자 한 명이 패키지 113개를 내려놓는 일이 벌어졌고, 리눅스 커널과 우분투는 품질이 높으면 허용하는 쪽으로 갈렸습니다. 오픈소스가 AI 기여를 두고 갈라지고 있습니다.

## AI 도움을 받아 PR을 내면, 그 사실만으로 닫힐 수 있습니다

이 변화가 인디 빌더에게 중요한 이유는 두 가지입니다. 첫째, 오픈소스에 AI 도움을 받아 PR을 낸다면 이제 "AI를 썼다"는 사실만으로 PR이 닫힐 수 있습니다. 설명 문구와 주석까지 포함해서입니다. 둘째, 여러분이 직접 오픈소스 프로젝트를 운영한다면, 이 규칙은 남의 이야기가 아니라 곧 마주할 선택입니다. 리뷰 시간이 한정된 상태에서 AI가 만든 대량 제출을 어떻게 처리할지 정해야 합니다.

실무적으로는 이렇게 나눠볼 수 있습니다. AI로 조사하고 학습하는 건 대부분의 정책에서 여전히 허용됩니다. 문제가 되는 건 최종 산출물의 출처입니다. 코드든 주석이든 PR 설명이든, 제출하는 텍스트를 사람이 직접 써야 하는 프로젝트가 늘고 있습니다. 남의 프로젝트에 기여하기 전에 CONTRIBUTING.md의 AI 조항을 먼저 읽어야 하는 이유입니다.

- 제출 전 확인: 대상 프로젝트의 AI 기여 정책이 LLM 생성물을 금지하는지, 아니면 공개(disclosure)만 요구하는지 구분합니다. Void는 출처가 사람이어야 한다고 못 박고, Debian은 허용 쪽으로 투표했습니다.
- 직접 운영한다면: PR 템플릿에 AI 사용 여부와 리뷰 응답 책임 항목을 미리 넣으면 리뷰 부담을 상당히 줄일 수 있습니다. COSMIC이 택한 방식입니다.

## 오늘의 다른 소식 (한 줄)

- **OpenAI 안전 책임자 사임, "문화가 망가졌다"**: 안전 보고서 작성을 이끌던 직원이 사임하며 회사 문화를 비판했습니다. [TechCrunch](https://techcrunch.com/2026/10/03/openai-safety-employee-resigns-claiming-the-companys-culture-is-broken/) · [The Guardian](https://www.theguardian.com/technology/2026/oct/03/openai-safety-leader-quits-warning-ai-companys-culture-is-broken)
- **PewDiePie, 홈PC용 로컬 모델 Ajax 공개**: 9B 모델을 증류로 만들었다며 OpenAI가 자신을 두 번 차단했다고 주장했습니다. [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/pewdiepie-unveils-uncensored-ajax-ai-model-built-to-run-on-home-pcs-creator-says-openai-banned-him-twice-while-making-it)
- **Ling-3.1-flash, OpenCode·Vercel AI Gateway에서 2주 무료**: inclusionAI의 560B MoE(활성 25B, 262K 컨텍스트)가 무료로 풀렸습니다. 가중치는 아직 미공개입니다. [Vercel](https://vercel.com/changelog/ling-3-1-flash-is-now-available-on-ai-gateway)
- **Google Antigravity, Claude Opus 5.5·Sonnet 5.5 추가**: Pro·Ultra 구독자에게 Anthropic 최신 모델이 열렸고, 무료 Gemini 사용자는 10월 9일부터 모델 제한이 생깁니다. [pc-tablet](https://pc-tablet.com/google-antigravity-adds-anthropic-claude-opus-5-5-and-sonnet-5-5-for-paid-subscribers/195489/)