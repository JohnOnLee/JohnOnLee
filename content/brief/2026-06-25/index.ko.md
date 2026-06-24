---
title: "AI·스타트업 모닝 브리프 - 2026-06-25"
date: 2026-06-25
summary: "OpenAI, Broadcom과 첫 커스텀 추론 칩 'Jalapeño' 공개: OpenAI가 최초의 자체 추론 프로세서를 공개했다. NVIDIA GPU 의존도를 낮추기 위한 전략적 움직임으로, Google TPU·Amazon Trainium과 같은 길을 걷기 시작했다. LLM 추론에 특화된 설계이며 OpenAI의 자체…"
description: "OpenAI, Broadcom과 첫 커스텀 추론 칩 'Jalapeño' 공개: OpenAI가 최초의 자체 추론 프로세서를 공개했다. NVIDIA GPU 의존도를 낮추기 위한 전략적 움직임으로, Google TPU·Amazon Trainium과 같은 길을 걷기 시작했다. LLM 추론에 특화된 설계이며 OpenAI의 자체…"
---

[브리핑/AI] AI·스타트업 모닝 브리프 - 2026-06-25

## 핵심 변화
- **OpenAI, Broadcom과 첫 커스텀 추론 칩 'Jalapeño' 공개**: OpenAI가 최초의 자체 추론 프로세서를 공개했다. NVIDIA GPU 의존도를 낮추기 위한 전략적 움직임으로, Google TPU·Amazon Trainium과 같은 길을 걷기 시작했다. LLM 추론에 특화된 설계이며 OpenAI의 자체 AI 모델이 칩 설계에 활용되었다. 파운드리·제조는 Broadcom과 협업. [TechCrunch](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/) · [OpenAI](https://openai.com/index/openai-broadcom-jalapeno-inference-chip/)
<!--more-->
- **Qualcomm, AI 인프라 스타트업 Modular 인수 (~$4B)**: Qualcomm이 Chris Lattner(Swift·LLVM 창시자)가 설립한 Modular를 인수한다. Modular는 고성능 AI용 Python 슈퍼셋 Mojo와 MAX 플랫폼을 개발해왔다. 온디바이스 AI 소프트웨어 스택을 확보하려는 퀄컴의 전략적 베팅. AI 인프라 레이어에서의 M&A가 본격화되고 있다는 신호. [Modular](https://www.modular.com/blog/qualcomm-to-acquire-modular) · [Qualcomm](https://www.qualcomm.com/news/releases/2026/06/qualcomm-to-acquire-modular)
- **Google Gemini 3.5 Flash에 'Computer Use' 기본 탑재**: 구글이 Gemini 3.5 Flash에 컴퓨터 제어 기능을 빌트인 툴로 통합했다. 브라우저·모바일·데스크톱 환경 전반에서 클릭·타이핑·UI 탐색이 가능. 이전에는 별도 Gemini 2.5 모델로만 제공되던 기능. Gemini API와 Enterprise Agent Platform으로 제공. [Google Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/)

## 스타트업 / 제품 / 플랫폼 레이더
- **Reid Hoffman, xAI를 "완전한 실패작"으로 평가**: LinkedIn 공동창업자이자 영향력 있는 AI 투자자인 Reid Hoffman이 Fortune 인터뷰에서 xAI를 "complete train wreck"이라 평하고, SpaceX는 AI 기업이 아니라고 선을 그었다. OpenAI와 Anthropic에는 여전히 공간이 있다고 평가. AI 업계 내부자의 솔직한 구도 진단으로서 주목할 만하다. [Fortune](https://fortune.com/2026/06/24/reid-hoffman-spacex-musk-openai-anthropic-gen-z-mistake/)

## AI가 바꾸는 미래 신호
- **Oracle, 21,000명 감원 — 절감 재원을 AI 인프라에 투입**: 오라클이 21,000명 규모의 인력 감축을 단행하면서 동시에 수십억 달러를 AI 인프라에 쏟아붓고 있다. 인건비를 줄여 AI CapEx로 전환하는 패턴이 대기업의 템플릿으로 굳어지고 있다. [Ars Technica](https://arstechnica.com/ai/2026/06/oracles-21000-layoffs-help-drive-its-debt-fueled-ai-investments/)
- **Meta, 사내 AI 직원 모니터링 프로그램 중단**: Meta가 AI 기반 직원 활동 추적 프로그램을 운영하다 내부 데이터 유출 사고로 중단했다. 기업용 AI 감시가 실제 조직 마찰을 일으킨 구체적 사례. 생산성 측정과 프라이버시 사이의 긴장이 본격화되고 있다. [WIRED](https://www.wired.com/story/meta-pauses-employee-tracking-program-following-internal-security-breach/)
- **Qwen-AgentWorld: 범용 에이전트를 위한 언어 세계 모델**: 알리바바 Qwen 팀이 arXiv에 공개한 논문. 7개 도메인, 1,000만 건 이상의 실제 환경 상호작용 궤적으로 학습된 언어 세계 모델. LLM이 환경 시뮬레이터 역할을 하여 에이전트의 계획·추론을 지원하는 접근. 35B-A3B와 397B-A17B 두 가지 사이즈로 공개. [arXiv](https://arxiv.org/abs/2606.24597)

## 현실적인 기회 / 실험 아이디어
- **추론 비용 하락을 전제로 한 프로덕트 재검토**: OpenAI의 커스텀 칩이 양산 단계에 접어들면 LLM 추론 비용은 한 차례 더 꺾일 가능성이 높다. 현재 추론 비용 때문에 경제성이 안 나오던 AI 프로덕트(실시간 대규모 문서 처리, 고빈도 에이전트 루프 등)를 6~12개월 후 기준으로 다시 계산해볼 시점.
- **'Computer Use'가 테이블 스테이크가 된 세상에서의 UX**: Gemini Flash 수준의 모델에도 컴퓨터 제어가 기본 탑재되기 시작했다. 에이전트에게 GUI를 통째로 넘기는 방식이 과연 사용자가 원하는 UX인지, 아니면 API·숏컷 기반의 타이트한 통합이 더 나은지 — 파운더/오퍼레이터는 지금 실험해서 자기 도메인에서 정답을 찾아야 한다.

## 불확실성 / 계속 볼 것
- **커스텀 AI 칩이 NVIDIA의 추론 지배력을 얼마나 빨리 잠식할지**: OpenAI와 Google, Amazon, Microsoft 모두 커스텀 칩 전략을 가속 중이다. 그러나 NVIDIA도 매년 새로운 추론 최적화를 내놓고 있다. 추론 칩 시장의 구도 변화 속도와 폭은 아직 불확실하다. 실제 양산 물량과 성능 벤치마크가 나오기 전까지는 신중한 관찰이 필요하다. [TechCrunch](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/)