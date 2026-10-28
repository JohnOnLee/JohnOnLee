---
title: "Gemini 4 Carbon, 1등인데 지금은 방어팀만 부릅니다"
date: 2026-10-29
summary: "10월 28일 구글이 Gemini 4 Carbon을 공개했습니다. 내세우는 건 두 가지. 자사 기준 가장 강한 프런티어 모델이고, 보안 취약점을 찾고 고치는 일에 특화됐습니다.…"
---

## Carbon은 종합 1위를 가져갔고, 접근은 사이버 방어팀에서 시작합니다

10월 28일 구글이 Gemini 4 Carbon을 공개했습니다. 내세우는 건 두 가지. 자사 기준 가장 강한 프런티어 모델이고, 보안 취약점을 찾고 고치는 일에 특화됐습니다. Artificial Analysis Intelligence Index v5.0에서 59점으로 1위이고, 취약점 탐지 SEC-bench Pro 88.2%, 실제 공격 가능성 검증 ExploitGym 54.8%, 근본 원인 패치 CWE-bench 71.0%를 기록했습니다. [Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/) [Ars Technica](https://arstechnica.com/ai/2026/10/google-announces-gemini-4-carbon-its-latest-frontier-ai-model-that-you-cant-use/)

지금 부를 수 있는 사람은 거의 없습니다. 이번 주부터 사이버 방어 담당자 일부에게 먼저 열고, 신뢰 파트너 프로그램을 거쳐 개발자와 기업, 소비자에게 "가능한 한 빨리" 공개한다는 계획만 있습니다. 그 '빨리'에 날짜는 없습니다. 직전 모델인 Argon도 같은 단계를 밟았고, Ars Technica는 Carbon이 그 길을 따른다면 넓게 풀리기까지 몇 주가 걸릴 것으로 봤습니다.

가격은 접근권보다 먼저 나왔습니다. 출시 기간에는 Argon과 같은 100만 토큰당 입력 2달러, 출력 10달러이고 캐시 입력은 95% 할인입니다. 기간이 끝나면 두 배로 뜁니다. 입력 4달러, 출력 20달러. Ars Technica가 종료일을 구글에 물었지만 답은 없었습니다. Argon의 할인은 11월 말까지.

성능 주장에는 조건이 붙습니다. 보안 벤치마크는 가드레일 없이 측정했고, 나머지 항목에는 구글 내부 평가가 섞여 있습니다. Gray Swan의 간접 프롬프트 인젝션 평가에서는 0.0%로 Argon의 0.7%, Claude Opus 5.5의 1%, GPT-6 Astra의 8.5%보다 낮았습니다. 다만 Ars Technica는 프런티어 모델들이 모두 비슷한 구간에 몰려 있고 차이는 몇 점이라고 짚었습니다.

## 점수 몇 점 차이로 스택을 바꿀 근거는 아직 없습니다

Carbon이 내세운 개선 가운데 인디 팀이 실제로 겪는 문제와 맞닿은 쪽은 보안 점수가 아니라 행동입니다. 근거 없는 주장은 Argon의 절반 수준으로 줄였고, 정보가 모호하면 추측하는 대신 출처를 찾아 사용자에게 차이를 알린다고 합니다. 지시 범위를 넘는 행동은 26%, 해야 할 일을 빠뜨리는 경우는 29% 줄었습니다. 이 네 가지는 지금 쓰는 모델로도 그대로 시험해볼 수 있죠. 정보를 일부러 빼고 물었을 때 모른다고 말하는지, 범위 밖 파일을 건드리는지 보면 됩니다.

보안 성능은 내 코드에 닿는 시점이 가장 늦습니다. 취약점을 찾아 패치까지 만든다는 건 작은 팀에 매력적이지만, 그 모델이 먼저 가는 곳은 사이버 방어 조직입니다. 그 전까지 코드 리뷰와 취약점 점검 단계를 줄일 근거는 없습니다.

모델을 바꾸는 비용도 있습니다. 프롬프트를 다시 쓰고 회귀 테스트를 다시 돌려야 하고, 두세 명이 만드는 제품에서는 그 작업이 곧 일정입니다.

가격 인상 시점은 아직 모릅니다. 구글이 할인 종료일을 말하지 않았으니, Carbon을 전제로 원가를 계산한 기능은 종료일이 나올 때까지 붙잡아두는 편이 낫습니다. 지금 스택에서 바뀌는 것은 없습니다. 다음에 새 모델을 붙일 때 접근 조건과 가격 종료일을 같이 확인하면 됩니다.

## 오늘의 다른 소식 (한 줄)

- **SK하이닉스 3분기 영업이익률 80%, 메모리 부족은 2030년까지**: 매출 104.6조원과 영업이익 83.3조원으로 분기 최대 실적입니다. 첨단 공정 난이도와 증설 기간 때문에 수요가 공급을 넘는 구조가 2030년까지 이어지고, 2027~2028년 생산능력의 절반 이상은 14개 고객과 장기계약으로 묶여 있습니다. [SK hynix](https://news.skhynix.com/en/q3-2026-business-results/)
- **Reddit이 'For You' 피드를 전 세계에 풉니다**: 홈이 알고리즘 추천 탭과 구독 커뮤니티 탭으로 나뉘고, 앞으로 몇 주에 걸쳐 순차 적용됩니다. [TechCrunch](https://techcrunch.com/2026/10/28/reddit-is-the-latest-platform-to-embrace-the-for-you-feed/)
- **NVIDIA가 Nemotron 3.5 Transcribe를 공개했습니다**: 40개 언어 전사와 13개 언어 화자 구분을 한 모델에서 처리하는 오픈웨이트 모델입니다. 1시간짜리 녹음까지 받고, Granary v2 데이터 파이프라인과 파인튜닝 예제도 함께 나왔습니다. [Hugging Face](https://huggingface.co/blog/nvidia/nemotron-transcribe-granary)
- **ChatGPT dot을 문자로 부를 수 있게 됐습니다**: 미국 Pro 이용자 프리뷰로 iMessage와 RCS에서 문자, 사진, 음성 메모를 보내면 에이전트가 먼저 진행 상황을 알려줍니다. [Engadget](https://www.engadget.com/2300235/openai-now-lets-you-text-your-dot-agent/)