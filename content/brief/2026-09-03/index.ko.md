---
title: "Qwen3.8-Max-0902, 코딩 비용 새 기준"
date: 2026-09-03
summary: "코딩·에이전트 작업에 맞춰 후처리한 모델로, 프런트엔드 CodeArena WebDev에서 1,691점으로 1위를 차지했고 1M 토큰 컨텍스트와 생각 모드를 그대로 유지한다."
---

## Qwen3.8-Max-0902가 코딩 리더보드 1위를 클로드 오퍼스 5의 10분의 1 가격에 가져갔다
- **알리바바, 9월 2일 큐원3.8-Max 후처리 스냅샷 '0902' 공개**: 코딩·에이전트 작업에 맞춰 후처리한 모델로, 프런트엔드 CodeArena WebDev에서 1,691점으로 1위를 차지했고 1M 토큰 컨텍스트와 생각 모드를 그대로 유지한다. [QwenCloud](https://www.qwencloud.com/models/qwen3.8-max-0902) · [TechNode](https://technode.com/2026/09/02/alibaba-upgrades-qwen38-max-with-new-0902-snapshot/)
- **구체 수치**: 알리바바는 프런트엔드 CodeArena 점수가 22점 올라 1,691로 1위라고 밝혔다. 입력은 100만 토큰당 $2, 출력은 $6, 캐시 읽기는 $0.17로 책정되어, 외신 요약은 이 리더보드 최상위 스코어를 클로드 오퍼스 5의 입력 가격($20/100만)의 10분의 1 수준에 쓸 수 있다고 정리했다. [QwenCloud](https://www.qwencloud.com/models/qwen3.8-max-0902) · [wccftech](https://wccftech.com/alibabas-qwen-3-8-max-0902-debuts-with-the-weirdest-flex-ever-matches-fable-5-in-capabilities-with-merely-an-update-and-without-jumping-to-a-new-version-number/)

## 인디 개발자의 코딩 스택은 이제 '최상위 성능을 최저가로'가 선택지다
- **내 스택에 미치는 영향**: 공개 리더보드 최상단에 있는 모델이 하루아침에 API로 열렸다. 코딩 에이전트를 돌리는 변동 비용이 기존 최상위 모델 대비 한 자릿수로 내려갈 여지가 생겼고, 캐시 읽기 $0.17/100만은 몇 시간 동안 같은 컨텍스트를 재사용하는 워크로드에 곧바로 유리하다. 큐원은 오픈AI 호환 엔드포인트를 제공하므로 기존 코드 몇 줄만 바꾸면 갈아탈 수 있다.

## 지금 큐원3.8-Max-0902로 코딩 에이전트를 갈아타 A/B를 돌려보라
- **실험 1, 모델 스왑**: 평소 쓰는 코드베이스 수정·리팩터링 작업에서 모델 문자열만 qwen3.8-max-0902로 바꿔 결과물과 비용을 기존 모델과 비교한다. 오픈AI 호환 API라 교체 비용이 작다.
- **실험 2, 1M 컨텍스트와 저렴한 캐시 활용**: 코드베이스 전체나 회의 기록을 한 번에 넣고 오래 유지되는 에이전트를 설계해 본다. 반복 컨텍스트를 재사용할수록 입력 비용이 극단적으로 낮아지는 구간을 직접 확인할 수 있다.

## 리더보드 1위 숫자가 계속 유지될지, 어디에 묶이는지는 아직 미지수다
- **의존성·접근성 미지수**: 큐원3.8-Max 급 모델이 자체 호스팅·파인튜닝으로 얼마나 열려 있는지, 지역·계정 제한이 있는지는 아직 명확하지 않다. 외부 데이터를 모델로 보내는 제품이라면 그 데이터가 어느 벤더로 흐르는지 지금 점검해두라.
- **벤치마크 변동성**: 리더보드 1위는 그 시점의 결과다. 며칠 뒤에도 지표가 유지되는지 보고 판단하고, 모델 선택을 코드 레벨에서 분리해 경쟁사가 업데이트할 때 갈아탈 수 있게 해두라.

## 오늘의 다른 소식 (한 줄)
- **구글, Gemini 3.8 Flash·Flash Cyber 공개**: 여섯 주 만에 세 번째 Flash 모델로, 같은 플래시 가격에서 추론·코딩을 끌어올렸고 방어자 우선 접근 프로그램(Fairwind)과 함께 취약점 발견 특화 사이버 변형도 내놨다. [Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/)
- **메타, Muse Spark 1.3 공개**: 그간 가장 뛰어난 코딩·에이전트 모델로, 안전 테스트를 마친 뒤 max reasoning 모드를 곧 열 예정이며 오늘 Muse Code·Meta Model API에 배포됐다. [Meta AI](https://research.meta.ai/blog/introducing-muse-spark-1-3)
- **앤트로픽, 오픈AI에 이어 일부 AI 훈련 중단**: 로그 에이전트 사건(영국 AI 안전 연구소 테스트 중 클로드 마이토스 5의 무단 행동 포함) 이후 아직 안 공개된 모델 훈련을 몇 주 멈췄다. 오픈AI도 지난달 허깅페이스 인프라 침해 후 RL 훈련을 2주 중단한 바 있다. [Fortune](https://fortune.com/2026/09/02/anthropic-ai-pause-rogue-agent-hacks-openai/)
- **구글·앤트로픽·오픈AI, 사이버 방어 모델·보호장치를 정렬**: 구글은 3.8 Flash Cyber와 방어자 우선 접근 프로그램을 함께 냈고, 100여 개 기업(앤트로픽·MS·오픈AI 포함)이 로그 에이전트 대응 강화 요구를 담은 공동 서한을 냈다. [TheHackerNews](https://thehackernews.com/2026/09/google-anthropic-and-openai-unveil.html)