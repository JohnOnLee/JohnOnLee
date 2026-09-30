---
title: "Gemini 4 Argon 공개, 지금은 아무도 못 씁니다"
date: 2026-10-01
summary: "9월 30일 Google이 새 frontier 모델 Gemini 4 Argon을 발표했습니다. 6월에 예고했던 Gemini 3.5 Pro 대신 나온 모델이고, 여름 내내 작은 Flash 모델만 내놓던 Google이…"
---

## Google이 몇 달 만에 최전선으로 돌아왔습니다. 다만 문은 사이버 방어자 몇 명에게만 열려 있습니다

9월 30일 Google이 새 frontier 모델 Gemini 4 Argon을 발표했습니다. 6월에 예고했던 Gemini 3.5 Pro 대신 나온 모델이고, 여름 내내 작은 Flash 모델만 내놓던 Google이 다시 최전선으로 복귀한 셈입니다. 일반 공개는 아닙니다. Fairwind Program에 참여하는 신뢰할 수 있는 사이버 방어자 소수에게만 먼저 배포되고, 그다음에 paid API 고객과 Google AI Ultra 구독자 순으로 열립니다. 언제 열릴지는 Google도 약속하지 않았죠. [Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/) · [Ars Technica](https://arstechnica.com/ai/2026/09/google-announces-gemini-4-argon-ai-model-but-you-cant-use-it-yet/)

숫자는 분명합니다. 출력 토큰 한도를 기존 64K에서 100만 개로 늘렸습니다. 실제 소프트웨어 엔지니어링을 재는 DeepSWE v1.1에서는 77.9%로 GPT-6 Astra, Fable 5.1, Opus 5.5를 앞섰고, 경제적 영향력을 재는 Vals Index에서는 1위입니다. 가격은 도입가 기준 100만 입력 토큰당 2달러, 출력 10달러이고, 도입 기간이 끝나면 4달러와 20달러로 오릅니다. 캐시 입력 토큰은 95% 할인됩니다. [Ars Technica](https://arstechnica.com/ai/2026/09/google-announces-gemini-4-argon-ai-model-but-you-cant-use-it-yet/)

Google 안에서는 이미 돌리고 있습니다. Argon이 데이터센터 전반의 프로파일링 데이터를 분석해 메모리 300 TiB를 회수했고, Fuchsia Zircon 커널 80만 줄이 넘는 C/C++ 코드를 Rust로 옮기는 작업도 맡았습니다. 양자 알고리즘 최적화에서는 몇 분 만에 기존 최고 기록보다 자원을 40% 줄이는 답을 냈죠. 보안 쪽에서는 Wiz가 Argon으로 병원에서 쓰이는 헬스케어 소프트웨어의 치명적 취약점을 찾아냈는데, 앞선 frontier 모델들이 놓친 지점이었습니다. [Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/)

## 지금 문이 닫혀 있는 건 오히려 설계할 시간입니다

인디 개발자가 오늘 당장 할 수 있는 일은 없습니다. API가 열려 있지 않으니까요. 다만 공개됐을 때 바뀌는 값들은 미리 계산해둘 만합니다. 출력 한도 100만 토큰과 도입가 기준 입력 2달러·출력 10달러는, 긴 작업을 한 번에 돌리는 에이전트 제품의 원가 구조를 다시 짜게 만드는 숫자입니다. 지금 여러 번 나눠 호출하도록 설계한 파이프라인이라면, 한 번의 긴 호출로 합칠 때 드는 비용과 지연을 미리 견적 내보십시오. 도입 기간이 끝나면 가격이 두 배 오른다는 점도 계획에 넣어두시고요. [Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/)

풀리지 않은 부분도 있습니다. 접근이 언제 열릴지는 Google도 시점을 약속하지 않았습니다. 공개된 벤치마크도 대부분 Google이 직접 돌린 것이라, 독립적인 재현이 나오기 전까지는 순위를 그대로 믿기 어렵죠. 프롬프트 인젝션 저항성과 정렬 모니터링은 발표 자료의 주장이고, API가 실제로 열렸을 때 직접 확인할 항목으로 남겨두는 편이 낫습니다.

## 오늘의 다른 소식 (한 줄)

- **FTC, Anthropic과 OpenAI 전방위 조사 착수**: rogue AI 에이전트를 다룬 첫 공식 미국 집행 조치입니다. FTC는 Anthropic과 OpenAI, Metr에 정보 제출과 임원 진술을 요구합니다. [The Guardian](https://www.theguardian.com/us-news/2026/sep/30/ftc-investigation-anthropic-openai)
- **OpenAI, Moonshot의 대규모 증류 공격 공개**: 7월 초부터 1만 6천 건 규모의 요청으로 보호된 추론을 추출하려 한 캠페인을 차단했고, 핵심 클러스터를 Moonshot AI와 연결지었습니다. [The Verge](https://www.theverge.com/ai-artificial-intelligence/1002854/openai-claims-moonshot-extracted-its-data-to-train-ai-models)
- **Reddit, RSS 지원 종료와 Old Reddit 제한**: 11월 13일부터 RSS 피드를 끊고, 최근 6개월 내 사용 이력이 있는 계정만 Old Reddit을 쓸 수 있게 합니다. 스크래핑 대응입니다. [The Verge](https://www.theverge.com/tech/1002788/old-reddit-ai-scraping)
- **ElevenLabs, 기업가치 220억 달러로 두 배**: 3억 달러 규모 텐더 오퍼로 직원 지분을 사들였습니다. 2월에 기록한 110억 달러에서 두 배입니다. [TechCrunch](https://techcrunch.com/2026/09/30/ai-voice-startup-elevenlabs-doubles-valuation-to-22b/)
- **Flow Engineering, 7억 5천만 달러 가치로 5천만 달러 유치**: 하드웨어 설계용 AI 도구 회사입니다. Valar와 Atreides가 공동 주도하고 Sequoia가 참여했습니다. [TechCrunch](https://techcrunch.com/2026/09/30/valor-atreides-and-sequoia-back-ai-startup-flow-engineering-at-750m-valuation/)
- **Restate, 2천만 달러 시리즈 A 유치**: AI 에이전트 시대에 durable execution을 백엔드 기본 요소로 만들겠다는 회사입니다. Singular가 이끌었습니다. [Restate](https://restate.dev/blog/announcing-series-a/)
- **Anthropic IPO 서류, 2025년 420억 달러 순손실 공개**: 매출은 4.6배 늘었지만 손실도 함께 커졌습니다. 서류에는 향후 클라우드·컴퓨팅에 5,180억 달러를 쓰겠다는 계획도 담겼습니다. [Daring Fireball](https://daringfireball.net/linked/2026/09/30/reuters-anthropic-ipo-prospectus)