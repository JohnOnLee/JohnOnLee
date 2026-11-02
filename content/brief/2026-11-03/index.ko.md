---
title: "gemini-2.5-pro, 12월 1일 자동 전환"
date: 2026-11-03
summary: "구글이 12월 1일부터 Gemini 2.5 Pro와 2.5 Flash API 요청을 각각 다른 플래시 모델로 넘기고, 넘어간 모델의 요금으로 청구합니다."
---

## gemini-2.5-pro가 gemini-3.8-flash로 바뀌기 전에 모델을 직접 골라야 합니다

구글이 12월 1일부터 Gemini 2.5 Pro와 2.5 Flash API 요청을 각각 다른 플래시 모델로 넘기고, 넘어간 모델의 요금으로 청구합니다.

`gemini-2.5-pro` 요청은 `gemini-3.8-flash`로, `gemini-2.5-flash` 요청은 `gemini-3.5-flash-lite`로 갑니다. 코드를 고치지 않아도 구글이 모델을 바꿉니다. 두 모델은 이미 Google AI Studio 선택 목록에서 빠졌고, API는 예전에 실제로 써 본 계정에만 열려 있습니다. [지원 종료 안내](https://ai.google.dev/gemini-api/docs/deprecations)의 일반 표는 날짜를 '가장 이른 가능 날짜'라고 적지만, 이 두 모델에는 12월 1일 종료와 당일 자동 전환을 명시했고 따로 이전 기간을 두지 않았습니다.

요금은 12월과 1월이 다릅니다. `gemini-3.8-flash`는 100만 토큰당 입력 $0.75, 출력 $3.75이고 이 가격은 12월 31일까지입니다. 2027년 1월 1일부터는 입력 $1.50, 출력 $7.50이 됩니다. 구글은 [3.8 Flash 안내](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.8)에서 연말 가격을 도입 요금이라고 부릅니다. 20만 토큰 이하 프롬프트에 적용되는 2.5 Pro의 $1.25·$10.00과 견주면, 12월에는 입력이 60%, 출력이 37.5% 수준이고 1월에는 입력이 20% 비싸지고 출력이 25% 싸집니다. 공개 요금을 계산한 값입니다. 12월 청구서로 마진을 잡으면 1월에 틀립니다([구글 요금표](https://ai.google.dev/gemini-api/docs/pricing)).

모델 ID를 그대로 두면 12월 1일부터 답하는 모델이 바뀝니다. 지금 제품에 쓸 모델을 정해 ID를 직접 바꾸고 파라미터까지 맞춰야 합니다. 구글이 예고한 호환성 변경에는 함수 호출과 `thought_signature` 검증이 들어 있고, `thinking_budget`은 `thinking_level`로 바뀝니다. 일부 샘플링 파라미터와 미리 채운 모델 응답도 사라집니다([변경 기록](https://ai.google.dev/gemini-api/docs/changelog)). 3.8 Flash의 기본 thinking level은 `medium`이라서, 모델 ID만 갈아 끼우고 예전 설정을 그대로 보내면 이전이 끝나지 않습니다. 구글도 12월 1일 전에 이전 가이드를 보라고 안내하는 이유가 여기 있습니다. 자동 전환을 기다리면, 어떤 모델이 고객에게 답할지와 1월부터 낼 요금을 구글이 정합니다.

## 오늘의 다른 소식 (한 줄)

- **Anthropic 메시지 스레드 공개 베타**: 50만~100만 토큰 요청에서 첫 토큰 지연 중간값이 약 35% 줄지만 토큰 사용량과 요금은 그대로이고, 마지막 요청 뒤 5분이 지나면 스레드가 만료되며 중간에 모델을 바꿀 수 없습니다. [Anthropic](https://claude.com/resources/articles/message-threads)
- **GitHub Actions의 pull_request_target 기본 차단**: 공개 저장소는 12월 2일부터 명시적으로 허용한 워크플로만 실행되므로, 11월 9일과 16일 임시 차단 전에 Insights에서 걸리는 실행을 확인해야 합니다. [GitHub Changelog](https://github.blog/changelog/2026-11-02-pull_request_target-blocked-by-default-december-2/)
- **뉴욕타임스 등, Brave에 저작권 소송**: 기사 수집과 AI 업체 판매, 유료벽 우회를 두고 제소했고 주장은 아직 입증되지 않았습니다. 뉴스 콘텐츠를 쓰는 제품이라면 수집 경로가 라이선스인지 확인할 일입니다. [Reuters](https://www.reuters.com/legal/litigation/new-york-times-sues-maker-brave-web-browser-over-copyrights-2026-11-02/)