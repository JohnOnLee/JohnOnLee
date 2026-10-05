---
title: "Reflection 501B 오픈웨이트 Beam 공개, 가중치는 이달 말"
date: 2026-10-06
summary: "엔비디아의 지원을 받는 Reflection이 첫 오픈웨이트 모델 Beam을 10월 5일 공개했습니다. 전체 파라미터 5010억 개에 활성 파라미터 230억 개를 쓰는 전문가 혼합(MoE)…"
---

## 미국 스타트업 Reflection이 501B 오픈웨이트 모델 Beam을 내놨습니다

엔비디아의 지원을 받는 Reflection이 첫 오픈웨이트 모델 Beam을 10월 5일 공개했습니다. 전체 파라미터 5010억 개에 활성 파라미터 230억 개를 쓰는 전문가 혼합(MoE) 모델이고, 텍스트만 다루며 컨텍스트는 100만 토큰입니다. 코딩과 추론, 에이전트 작업에 맞췄습니다. 회사는 23.8조 토큰으로 프리트레이닝했고, 엔비디아 GB300 GPU 1만 500개에서 4주 동안 1억 건이 넘는 롤아웃으로 강화학습을 돌렸다고 밝혔습니다. [Reflection](https://reflection.ai/blog/introducing-beam) · [TechCrunch](https://techcrunch.com/2026/10/05/reflection-debuts-beam-a-open-weight-ai-model-to-rival-chinese-models-at-lower-compute-cost/)

Reflection은 Beam이 Z.ai의 GLM-5.2와 비슷한 점수를 내면서 추론 연산은 3~4배 적게 쓴다고 주장합니다. 이 수치는 회사가 직접 낸 것이고 독립 검증은 아직 없습니다. 비교 대상인 GLM-5.2는 7월 모델이고, 그 뒤 8월에 GLM-5.3이 나왔습니다. 최상위 오픈 모델인 Kimi K3는 여전히 앞서 있습니다. 값싼 오픈웨이트 선택지가 하나 더 생긴 것이 오늘의 내용입니다. [Fortune](https://fortune.com/2026/10/05/reflection-ai-unveils-beam-a-new-us-based-open-source-model-to-compete-with-china/)

내려받을 수는 아직 없습니다. 오늘 나온 건 프리뷰이고 얼리 액세스 대기 명단만 받습니다. 가중치와 기술 보고서, 모델 카드는 이달 말에 Apache 2.0으로 공개됩니다.

## 자체 호스팅 코딩 에이전트의 서구 후보가 하나 생깁니다

Beam의 활성 파라미터는 230억 개입니다. 노트북에 올릴 크기는 아닙니다. 임대한 GPU 한두 장에 올려 돌리는 규모입니다. 그래서 이 모델이 겨냥하는 상대는 개인 개발자의 로컬 실행보다, 에이전트 루프를 돌리느라 API 비용이 커진 팀입니다. Apache 2.0으로 가중치가 풀리면 파인튜닝한 모델과 평가셋이 자기 자산으로 남고, 벤더가 가격을 올릴 때 옮겨갈 자리가 생깁니다. 지금 그 자리를 채우는 건 중국 오픈 모델뿐이었습니다.

"미국이 중국을 따라잡았다"는 프레임은 과합니다. Reflection이 비교한 GLM-5.2는 이미 두 세대 전 모델이고, 최상위 오픈 모델은 여전히 중국 쪽입니다. 오늘 확인된 건 추론 연산을 3~4배 줄여 값싸게 돌리는 쪽의 진전입니다. 능력에서 앞섰다는 뜻은 아닙니다. 에이전트는 같은 요청을 여러 번 반복해서 처리하니 토큰 단가가 곧 제품 원가가 됩니다. 그 숫자가 이 모델의 실제 무기입니다.

가중치가 나오고 독립 평가가 붙기 전에는 결정할 게 없습니다. 성능 주장도, 하드웨어 요구량도, 라이선스 문구도 아직 확인되지 않았습니다. 코딩 에이전트를 폐쇄 API에 묶기 직전이라면, 이달 말 가중치 공개와 검증 결과를 보고 나서 정해도 늦지 않습니다.

## 오늘의 다른 소식 (한 줄)

- **llama.cpp v0.6.0 공개**: ggml 추론 엔진에 Qwen4Exp용 MTP 추측 디코딩과 GLM-5.3-Flash 지원이 들어갔습니다. [GitHub](https://github.com/ggml-org/llama.cpp/releases/tag/v0.6.0)
- **OpenAI, EU에서 ChatGPT 텍스트에 워터마크**: 몇 주에 걸쳐 순차 적용되고, API 개발자는 오늘부터 일부 모델에서 선택적으로 켤 수 있습니다(기본 꺼짐). [TechCrunch](https://techcrunch.com/2026/10/05/openai-will-start-watermarking-chatgpts-text-in-the-eu/)
- **Reka, 19B 옴니 모델 Rho-1 연구 프리뷰**: 텍스트와 이미지, 영상, 행동을 한 네트워크에서 처리합니다. [Reka](https://reka.ai/news/rho-1-collapsing-the-multimodal-stack)
- **Aleph Alpha, 유럽산 오픈웨이트 Kolibri 공개**: 독일어와 영어를 지원하고 가중치는 Hugging Face에 올라갔습니다. [Aleph Alpha](https://aleph-alpha.com/en/news/kolibri-sovereign-ai-made-in-germany/)
- **Cohere, 엔터프라이즈 에이전트 플랫폼 North 2 공개**: 세션 간 메모리와 비용 관리 기능을 붙였습니다. [Unite.AI](https://www.unite.ai/cohere-launches-north-2-with-redesigned-agent-harness-and-memory/)
- **말레이시아, 고위험 AI 규제 법안 예고**: 위험 기반 접근으로 내년 초 의회 제출을 목표로 합니다. [The Star](https://www.thestar.com.my/news/nation/2026/10/05/gobind-high-risk-ai-systems-to-face-stricter-safeguards-under-new-bill)