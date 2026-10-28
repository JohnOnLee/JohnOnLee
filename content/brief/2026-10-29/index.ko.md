---
title: "Gemini 4 Carbon, 교체는 아직"
date: 2026-10-29
summary: "Google이 2026년 10월 28일 Gemini 4 Carbon을 발표했습니다. 소규모 팀이 API를 쓸 수 있는 날짜는 아직 없습니다."
---

## Carbon은 벤치마크 1위지만 API 이용 날짜는 미정입니다

Google이 2026년 10월 28일 Gemini 4 Carbon을 발표했습니다. 소규모 팀이 API를 쓸 수 있는 날짜는 아직 없습니다.

Google은 Carbon을 자사의 가장 강력한 프런티어 모델이자 보안 취약점을 찾고 고치도록 만든 모델로 소개했습니다. Artificial Analysis Intelligence Index v5.0에서는 59점으로 1위입니다. [Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/)

Carbon은 취약점을 찾는 SEC-bench Pro에서 88.2%, 실제 악용 가능성을 입증하는 ExploitGym에서 54.8%, 근본 원인을 수정하는 CWE-bench에서 71.0%를 기록했습니다. 세 항목은 서로 다른 일을 측정하니 제품에서 맡길 작업에 맞춰 읽어야 합니다. Google은 이 보안 성적을 가드레일 없이 측정했고, 다른 결과 중 일부는 내부 평가입니다.

Gray Swan의 간접 프롬프트 인젝션 평가에서는 공격 성공률이 0.0%였습니다. 공격을 모두 막았다고 해서 환각이나 필수 단계 누락까지 없다고 볼 수는 없습니다. Ars Technica도 프런티어 모델들이 몇 점 차이 안에 모여 있다고 평가했습니다. 점수만으로 지금 쓰는 모델을 교체하기에는 근거가 부족합니다. [Ars Technica](https://arstechnica.com/ai/2026/10/google-announces-gemini-4-carbon-its-latest-frontier-ai-model-that-you-cant-use/)

Google은 이번 주 일부 사이버 방어 담당자에게 Carbon을 제공하고, Fairwind 프로그램의 신뢰 파트너로 대상을 넓힌 뒤 개발자·기업·소비자에게 가능한 한 빨리 제공할 계획입니다. Argon도 같은 순서로 공개됐기 때문에 Ars Technica는 Carbon 역시 널리 공개되기까지 몇 주가 걸릴 것으로 예상했습니다. Google이 약속한 출시일은 아니죠. 작은 팀이 이 예상만으로 제품에 도입할 일정을 잡기는 어렵습니다.

출시 할인가는 입력 100만 토큰당 2달러, 출력 10달러이고 캐시 입력은 95% 할인입니다. 할인 뒤에는 입력 4달러, 출력 20달러로 두 배가 됩니다. 도입 시점에 할인이 남아 있을지는 알 수 없죠. Ars Technica가 Google에 종료일을 물었지만 날짜를 받지 못했습니다. Argon의 할인은 11월 말까지지만 Carbon의 종료일을 뜻하지는 않습니다. 접근 일정과 할인 기간을 함께 알아야 실제 도입 비용을 판단할 수 있습니다.

## Carbon을 기다리는 동안 지금 모델에서 확인할 네 가지

Google에 따르면 Carbon은 Argon보다 근거 없는 주장을 약 절반으로 줄였습니다. 근거가 모호하면 추측하는 대신 출처를 찾아 어느 부분이 맞지 않는지 사용자에게 보여준다고 합니다. 지시 범위를 벗어나는 행동은 26%, 필수 단계를 빠뜨리는 행동은 29% 줄였다는 설명도 있습니다.

지금 쓰는 모델이 근거가 모호할 때 추측을 멈추는지 먼저 확인할 수 있습니다. 서로 맞지 않는 근거를 주고, 출처의 차이를 설명하는지 아니면 빈 부분을 추측하는지 보면 됩니다. 출처를 보여줬다는 이유만으로 답까지 근거가 있다고 판단하지 않고, 출처가 답을 뒷받침하는지 함께 확인해야 합니다.

범위 초과와 누락은 허용한 작업 범위와 반드시 거칠 단계를 명시한 요청으로 시험할 수 있습니다. 요청을 끝냈다고 해도, 시키지 않은 작업을 했는지와 필요한 단계를 빠뜨렸는지는 각각 확인해야 합니다. 현재 모델을 이렇게 시험해두면 Carbon을 쓸 수 있게 됐을 때 같은 요청으로 비교할 수 있습니다.

스택을 바꿀지는 접근 일정과 가격 조건을 확인하고 판단하면 됩니다. 그동안 현재 모델에서 직접 확인한 행동을 비교 기준으로 삼을 수 있습니다.

## 오늘의 다른 소식 (한 줄)

- **SK hynix 2026년 3분기 실적**: 매출 104.6조 원과 영업이익 83.3조 원으로 모두 사상 최대, 영업이익률은 80%이며, 회사는 2030년까지 수요가 공급을 웃돌고 2027~2028년 생산능력의 절반 이상을 14개 고객과 장기 계약했다고 밝혔습니다. [SK hynix](https://news.skhynix.com/en/q3-2026-business-results/)
- **Reddit For You**: 전 세계 홈 화면을 알고리즘 추천 For You와 Following 탭으로 나누는 변경을 앞으로 몇 주에 걸쳐 적용합니다. [TechCrunch](https://techcrunch.com/2026/10/28/reddit-is-the-latest-platform-to-embrace-the-for-you-feed/)
- **NVIDIA Nemotron 3.5 Transcribe**: 가중치를 공개한 전사 모델로 40개 언어, 13개 언어의 화자 구분, 최대 한 시간 녹음을 지원하고 Granary v2 데이터 파이프라인과 파인튜닝 레시피도 함께 공개했습니다. [Hugging Face](https://huggingface.co/blog/nvidia/nemotron-transcribe-granary)
- **ChatGPT Dots 문자 미리보기**: 미국 Pro 사용자는 iMessage와 RCS로 텍스트·사진·음성 메모를 보낼 수 있고, 작업에 진전이 있으면 에이전트가 먼저 메시지를 보냅니다. [Engadget](https://www.engadget.com/2300235/openai-now-lets-you-text-your-dot-agent/)