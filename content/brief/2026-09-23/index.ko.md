---
title: "OpenAI·Anthropic 동시 인하, GPT-6 Sol·Luna와 Opus 5.5"
date: 2026-09-23
summary: "9월 22일 오후, OpenAI와 Anthropic이 90분 사이에 API 단가를 절반으로 낮췄습니다. GPT-6 Sol은 입력 2달러·출력 10달러, Claude Opus 5.5는 4달러·20달러입니다."
---

## OpenAI GPT-6 Sol·Luna와 Claude Opus 5.5, 같은 날 값을 절반으로 내렸습니다

9월 22일 오후, OpenAI와 Anthropic이 90분 사이에 API 단가를 절반으로 낮췄습니다. GPT-6 Sol은 입력 2달러·출력 10달러, Claude Opus 5.5는 4달러·20달러입니다.

OpenAI가 내놓은 GPT-6 Sol과 GPT-6 Luna는 직전 세대인 GPT-5.6 Sol·Luna의 현재 프로모션 가격에서 절반입니다. Sol은 100만 토큰당 입력 2달러, 출력 10달러이고 Luna는 0.1달러와 0.5달러입니다. Sol은 내부 사실성 평가에서 전작보다 실수를 절반으로 줄였고, Luna는 GPT-5.6 Sol과 맞먹는 성능을 1% 수준의 비용에 낸다고 회사는 밝혔습니다. 캐시된 입력 토큰은 90% 할인되고, 어디까지 캐시할지 개발자가 직접 정할 수 있습니다. 같은 모델이 Copilot에도 들어갔습니다. Sol은 Pro+·Max·Business·Enterprise, Luna는 Pro 이상 요금제에서 모델 선택기에 나타납니다. [OpenAI](https://openai.com/index/introducing-gpt-6-sol-and-luna/) · [TechCrunch](https://techcrunch.com/2026/09/22/openai-launches-gpt-6-sol-and-luna/) · [TNW](https://thenextweb.com/news/openai-gpt-6-sol-luna-api-price-cut) · [GitHub Changelog](https://github.blog/changelog/2026-09-22-openais-gpt-6-sol-and-gpt-6-luna-now-available/)

Anthropic이 90분 먼저 움직였습니다. Opus 5.5는 Fable 5.1에 맞먹는 성능을 내면서 실행 비용은 Opus 5보다 40% 적고, 출력 속도는 30% 이상 빠릅니다. 요금은 100만 토큰당 입력 4달러, 출력 20달러로 Opus 5보다 20% 낮습니다. 에이전트와 코딩 작업 비용의 대부분을 차지하는 캐시 읽기는 100만 토큰당 0.2달러로 60% 내려갔습니다. 출시 전 평가는 Frontier Design과 METR 같은 외부 기관이 맡았고, 한 테스터는 68만 줄 코드 마이그레이션을 하루 안에 끝냈습니다. 프로바이더가 밝힌 대로 이 모델은 프런티어 속도 조절을 공개 요구한 뒤 나온 첫 릴리스이고, Pro·Max·Team 구독의 5시간 사용 한도도 20% 올랐습니다. [Anthropic](https://www.anthropic.com/news/claude-opus-5-5) · [ZDNET](https://www.zdnet.com/innovation/anthropic-claude-opus-5-5-fable-5-1-performance-costs-less/)

오픈웨이트 쪽에서도 같은 날 바닥이 내려갔습니다. Xiaomi가 MIT 라이선스로 공개한 MiMo-V2.6-Pro는 Artificial Analysis 지능 지수 46으로 오픈웨이트 1위이고, 이 회사가 추적하는 모델 가운데 작업 하나당 비용이 0.13달러로 가장 낮습니다. 전체 1조 200억 파라미터 가운데 420억 개만 활성화하는 MoE 구조이고, 100만 토큰당 입력 0.435달러, 출력 0.87달러에 OpenRouter와 자체 API, MiMo 앱에서 돌아갑니다. 학습은 6일이 채 걸리지 않았고 비용은 262만 달러였습니다. 학습 코드와 7,000개 강화학습 환경도 같이 공개됐습니다. [TNW](https://thenextweb.com/news/xiaomi-mimo-v2-6-open-weight-model-anthropic-distillation) · [Hugging Face](https://huggingface.co/XiaomiMiMo)

## 값이 가장 크게 내려간 자리는 에이전트가 실제로 태우는 부분입니다

세 회사가 내놓은 숫자는 토큰 단가가 아니라 작업 하나당 비용입니다. OpenAI는 업무 자동화 벤치마크인 AutomationBench에서 Sol(최대 추론)이 33.2%를 0.27달러에 처리했고 Claude Opus 5는 26.9%를 11.1배 비용에 처리했다고 적었습니다. 자사 벤치마크이니 그대로 받아들이기는 어렵지만, 단가표만 보고 있으면 자기 서비스의 원가를 잘못 잡게 됩니다. 청구서에서 봐야 할 숫자는 요청 하나를 끝내는 데 든 총액입니다.

차이는 캐시에서 갈립니다. Anthropic은 캐시 읽기가 에이전트와 코딩 비용의 대부분을 차지한다고 밝혔고, OpenAI는 캐시 적중 시 90% 할인과 함께 캐시 경계를 직접 지정하는 기능을 넣었습니다. 추론 강도를 바꾸거나 도구를 껐다 켜도 캐시가 유지됩니다. GitHub은 이 변화로 새로 처리해야 하는 프롬프트 토큰 비율이 절반 넘게 줄었다고 전했습니다. 대화 기록과 도구 정의를 매 요청마다 새로 밀어 넣는 파이프라인이라면 이번 인하의 혜택은 거의 없습니다.

싼 모델을 검증에 쓸 여지도 커졌습니다. GPT-6 Luna는 100만 토큰당 0.1달러이고 MiMo-V2.6-Pro는 작업 하나당 0.13달러입니다. 비싼 모델의 출력을 두 번째 모델이 다시 확인하는 구조는 지난달까지 비용이 맞지 않았습니다. 다만 절반 인하는 지금의 프로모션 가격과 비교한 값이고, 오픈웨이트 1위 자리는 올해 Kimi와 Qwen이 번갈아 가져갔습니다. 가격표를 상수로 두면 다음 달에 다시 계산해야 합니다.

- 지난주 로그로 요청 하나당 비용을 다시 계산합니다. 토큰 단가표 대신 실제 트레이스에서 뽑은 값을 기준으로 삼습니다.
- 시스템 프롬프트와 도구 정의처럼 고정된 구간을 앞에 두고, 시각이나 사용자 입력처럼 매번 바뀌는 값을 뒤로 보냅니다. 캐시 적중은 접두사가 같을 때만 일어납니다.

## 오늘의 다른 소식 (한 줄)

- **Meta, Muse가 OpenClaw에서 영감 받았다고 인정**: Meta Superintelligence Labs 제품 책임자 Nat Friedman이 X에 Muse가 제품으로서 OpenClaw에서 "확실히 큰 영감을 받았다"고 적었습니다. Muse 자체는 처음부터 만들었다고 덧붙였습니다. [TechCrunch](https://techcrunch.com/2026/09/22/meta-admits-muses-likeness-to-openclaw-isnt-a-coincidence/)
- **Mirendil, 50억 달러 밸류에 10억 달러 조달 협상**: 전 Anthropic 연구자들이 세운 자가개선 AI 스타트업입니다. Kleiner Perkins가 이번 라운드를 이끄는 협상에 나섰습니다. [Bloomberg Law](https://news.bloomberglaw.com/artificial-intelligence/ex-anthropic-staffers-ai-startup-in-talks-for-5-billion-value)
- **OpenAI, 학습 단계부터 외부 안전 평가 허용**: METR과 Redwood Research 등과 협의 중이지만 파트너와 접근 조건은 아직 정해지지 않았습니다. 샘 알트만은 9월 12일 사무실 출입증과 결과 공개 권한을 약속했습니다. [TNW](https://thenextweb.com/news/openai-evaluators-training-phase)
- **ShinyHunters, FBI 데이터 탈취 주장**: 오라클 피플소프트 제로데이를 이용했다고 주장하며 FBI 관련 서비스에서 직원과 지원자 데이터를 가져갔다고 밝혔습니다. 404 Media가 본 표본 5,000건에는 주소와 전화번호, 배우자 정보가 들어 있었고 FBI 채용 사이트는 변조됐습니다. [404 Media](https://www.404media.co/we-hacked-the-fbi-hackers-say-they-have-data-on-all-fbi-employees/)