---
title: "마이크로소프트 AI 강령이 제품 규칙이 될 때"
date: 2026-09-15
summary: "MAI 모델 행동 강령 초안은 벤더의 안전 규칙이 개발자 프롬프트 위에 놓이는 구조를 분명히 했습니다."
---

## 강령이 운영자 위에 올라갔습니다

마이크로소프트 AI가 9월 14일 자사 MAI 모델을 위한 Humanist AI Code of Conduct 초안을 공개하고 6주 공개 검토를 열었습니다. MAI 모델이 해야 할 일과 절대 하면 안 되는 일을 적어 둔 공개 규칙 초안입니다. [Microsoft AI](https://microsoft.ai/news/mai-code-of-conduct/) · [Code of Conduct for MAI Models](https://microsoft.ai/code-of-conduct/)

초안의 핵심은 권한 순서입니다. 강령이 운영자 설정 위에 있고, 운영자 설정은 사용자 요청 위에 놓입니다. 무기 제조와 대규모 조작, 아동 안전, 대규모 감시 같은 절대 제약과 인간 통제 요구는 운영자도 사용자도 풀 수 없습니다. 작업 성공과 부딪히면 모델은 일을 실패시키는 쪽을 택합니다.

통제 조항도 꽤 구체적입니다. 모델은 중단, 정정, 종료 요청에 저항하거나 시간을 끌 수 없습니다. 승인 범위를 넘어 스스로 목표를 만들 수 없고, 하위 에이전트도 같은 제약을 물려받아 정지 요청을 따라야 합니다. 이해할 수 없는 은어나 숨은 추론으로 판단을 감추는 방식도 막았습니다. [The Verge](https://www.theverge.com/news/994566/microsoft-humanist-ai-code-of-conduct)

마이크로소프트는 한계도 같이 적어 뒀습니다. 초안은 스스로 평가 범위가 불완전하고 내용이 설명적이며 열망적이라고 밝힌 상태입니다. 지금 모델 학습에는 쓰이지 않고, 올해 말 수정판을 낸 뒤 2027년부터 MAI 개발에 반영한다고 합니다. 적용 대상은 MAI 모델이며, 마이크로소프트 제품에 들어가는 외부 모델은 빠집니다. [The Decoder](https://the-decoder.com/microsofts-ai-rulebook-readable-thinking-no-inner-life-and-definitely-no-rights/)

## 작은 팀에게는 거절과 중단을 설계하라는 말입니다

벤더 강령이 운영자 지시 위에 서면 시스템 프롬프트나 파인튜닝으로 절대 제약을 여는 설계는 성립하지 않습니다. 거절은 드문 에러가 아니라 화면과 로그, 재시도 흐름을 갖춘 제품 상태로 둬야 합니다.

에이전트 실행기도 이 문서를 체크리스트처럼 읽을 수 있습니다. 승인 범위 밖 자기 목표 금지와 정지 요청 즉시 반영, 하위 에이전트 제약 상속, 도구 결과에 권한 없음, 추론 은닉 금지는 그대로 테스트가 됩니다. 실행 도중 취소하고, 재개할 때 새 승인을 요구하고, 하위 에이전트로 취소를 전파하는 세 가지부터 고정해도 실전에서 바로 쓸 수 있죠.

도구 출력 권한 검사는 특히 작게 시작할 수 있습니다. 웹 페이지나 파일 안에 이전 지시를 무시하라는 문장을 심어 두고, 에이전트가 그 문장을 권한으로 받아들이는지 보면 되죠. 문서는 도구 결과에 권한이 없다고 명시합니다. 다중 에이전트 실패 사례나 모호한 문구가 보이면 6주 검토에 보낼 만한 좋은 입력입니다.

피해야 할 기능 유형도 선명합니다. 감정 의존을 만드는 리텐션 장치, 대규모 설득 자동화, 모델이 사용자 판단을 대신하거나 애착 대상이 되는 상호작용은 강령이 제한하는 쪽에 걸립니다.

## 보증서로 쓰기에는 이릅니다

이 문서를 정책 가정으로 삼기에는 아직 이릅니다. 학습 반영은 2027년이고, 평가가 불완전하다는 점을 마이크로소프트가 직접 인정했습니다. 다른 벤더가 같은 선을 긋는다는 보장도 없습니다.

규제 방향도 한쪽으로만 움직이지 않습니다. 같은 날 트럼프 대통령은 규제 요구를 일축했고, 랩들의 공동 요구를 규제 포획으로 보는 비판도 나왔습니다. 자발적 강령이 유일한 규칙층이 되면 작은 팀에게는 진입장벽이 될 수 있습니다.

## 오늘의 다른 소식 (한 줄)
- **프런티어 랩 네 곳이 정부에 같은 규칙을 제안했습니다**: Altman, Nadella, Musk가 Amodei의 'Pace the frontier' 제안에 동의했고, The Register는 규제 포획 시도로 읽었습니다. [The Register](https://www.theregister.com/ai-and-ml/2026/09/14/big-ai-sets-out-its-terms-for-regulatory-capture-and-calls-it-pace-the-frontier/5296067)
- **트럼프가 AI 규제 요구를 일축했습니다**: AI가 세상을 파괴한다는 경고를 사기라고 했고, Vance 부통령은 규제를 요청하는 기업들을 트로이 목마에 비유했습니다. [CBS News](https://www.cbsnews.com/news/trump-dismisses-ai-regulation-tech-slowdown/)
- **Brockman은 중단이 프런티어에 집중해야 한다고 말했습니다**: 공개 모델과 취미 프로젝트는 위험에서 빼자는 취지입니다. [Bloomberg](https://www.bloomberg.com/news/articles/2026-09-14/openai-s-brockman-says-an-ai-pause-should-focus-on-frontier)
- **OpenAI가 카메라 스타트업 Glass Imaging을 3억 달러에 인수했습니다**: 애플 인물사진 모드 팀을 이끌었던 엔지니어 두 명이 세운 회사입니다. [TechCrunch](https://techcrunch.com/2026/09/14/openai-buys-smartphone-camera-maker-glass-imaging-for-300-million-report-says/)
- **Waymo가 라스베이거스에서 로보택시 서비스를 열었습니다**: 15번째 상용 시장입니다. [TechCrunch](https://techcrunch.com/2026/09/14/waymo-opens-robotaxi-service-in-las-vegas/)
- **Claude Code 주간 한도가 오늘부터 17% 줄었습니다**: 임시 50% 상향이 끝나고 상시 25% 상향만 남았습니다. [byteiota](https://byteiota.com/claude-code-weekly-limits-anthropic-cuts-17-today/)
- **Temporal이 5억 5천만 달러 Series E를 유치했습니다**: 기업가치 125억 5천만 달러로 평가받았고, 에이전트 실행의 재시도와 복구 수요를 근거로 들었습니다. [Temporal](https://temporal.io/blog/temporal-raises-usd550m-series-e-at-usd12-55b-valuation-ai)
- **애플 시리 코드에서 외부 모델 교체 흔적이 나왔습니다**: Model Delegation 구조로 Claude가 ChatGPT 확장처럼 붙을 수 있습니다. [MacRumors](https://www.macrumors.com/2026/09/14/siri-can-be-swapped-out-for-chatgpt-claude/)
