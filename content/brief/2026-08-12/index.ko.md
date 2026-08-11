---
title: "Nemotron 3.5·Mojo 1.0·LLM 추론 탈취"
date: 2026-08-12
summary: "경량 오픈소스 모델과 라우팅 라이브러리로, 엣지·PC·워크스테이션·데이터센터·클라우드 전반에서 에이전틱 AI 워크플로우를 더 빠르고 효율적으로 실행할 수 있게…"
---

## 스타트업 / 제품 / 플랫폼 레이더
- **NVIDIA, Nemotron 3.5 Lightning과 NeMo Switchyard 공개**: 경량 오픈소스 모델과 라우팅 라이브러리로, 엣지·PC·워크스테이션·데이터센터·클라우드 전반에서 에이전틱 AI 워크플로우를 더 빠르고 효율적으로 실행할 수 있게 설계됐다. [NVIDIA Blog](https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/)
- **Mojo 1.0 정식 출시**: Modular가 2023년 첫 공개 이후 3년 만에 Mojo 언어의 1.0 안정화 버전을 발표했다. Python 스타일 람다 문법, 메모리 안전 진단, VS Code LSP 안정화, GPU 프로그래밍용 AI Skills 1.0 등을 포함하며, 향후 비동기 프로그래밍과 패턴 매칭이 로드맵에 올라 있다. [Modular](https://www.modular.com/blog/modular-26-5-mojo-1-0-is-here)
- **OpenAI, ChatGPT Linux 데스크톱 앱 출시 — 동시에 경영진 이탈**: Linux용 ChatGPT 데스크톱 앱이 정식 출시됐다. 같은 날 COO Brad Lightcap이 "새로운 무언가를 시작하기 위해" 퇴사하며, 윤리 책임자도 입사 1년도 안 되어 퇴사한 것으로 알려졌다. [TechCrunch](https://techcrunch.com/2026/08/11/openai-launches-chatgpt-desktop-app-for-linux/) · [FT](https://www.ft.com/content/e49dfb75-f841-4466-a577-f7aaff8779a0) · [TechCrunch](https://techcrunch.com/2026/08/11/brad-lightcap-openais-longtime-coo-is-leaving-to-start-something-new/)
- **Anthropic 미공개 모델, 수학 난제에 진전**: 아직 출시되지 않은 Anthropic의 신규 모델이 수학계의 주요 미해결 문제 중 하나에서 의미 있는 진전을 보였다고 보도됐다. 구체적 문제명이나 방법론은 공개되지 않았으나, AI의 순수 수학 연구 능력이 한 단계 도약했음을 시사한다. [TechCrunch](https://techcrunch.com/2026/08/11/an-unreleased-anthropic-model-made-progress-on-one-of-maths-biggest-unsolved-problems/)
- **xAI, Grok Bot 출시**: xAI가 Grok을 독립형 봇 서비스로 공개했다. 상세 기능은 아직 확인되지 않았으나, 기존 X 플랫폼 통합을 넘어선 별도 서비스로의 확장으로 보인다. [xAI](https://x.ai/bot)

## AI가 바꾸는 미래 신호
- **LLM 추론 트레이스 탈취 공격 실증**: Anthropic, OpenAI, Google의 API가 반환하는 암호화된 Chain-of-Thought 블록이 세션·사용자·모델 간에 상호 교환 가능하며, 약한 모델을 탈옥시켜 강한 모델의 은닉된 추론 과정을 복원할 수 있다는 연구가 공개됐다. 이는 현재 LLM API의 추론 보안 모델 전체에 근본적 취약점이 있음을 의미한다. [Stolen Thoughts](https://stolen-thoughts.com/)
- **Manus, Meta에서 분리 독립 — AI 에이전트 스타트업의 새 국면**: Manus가 Meta 인수 8개월 만에 다시 독립 기업으로 전환한다. 규제 요건 준수를 위해 일부 사용자의 2025년 12월 29일 이후 데이터가 8월 23~24일 삭제되며, 백업 기간은 8월 11~23일이다. 대규모 AI 에이전트 서비스의 기업 분리와 데이터 규제 대응이 현실화되는 첫 사례다. [Manus](https://manus.im/blog/a-note-to-our-users)
- **NVIDIA, AI 인프라 금융 확대로 위험 영역 진입**: Ben Thompson의 분석에 따르면, NVIDIA가 고객사에 AI 인프라 구축 자금을 지원하는 방식을 확대하며 AI 빌드아웃의 리스크를 자사로 흡수하고 있다. 공급사가 아닌 금융 주체로 변모하는 전략적 전환이다. [Stratechery](https://stratechery.com/2026/nvidias-risky-business/)

## 현실적인 기회 / 실험 아이디어
- **Mojo 1.0 + MAX로 고성능 AI 추론 서빙 구축**: Mojo 1.0 안정화와 MAX의 GLM-5.2·Nemotron-H(Mamba-2 하이브리드) 지원을 활용해, Python 생태계와 호환되면서도 GPU/가속기에서 CPU 수준의 접근성으로 고성능 추론 서빙을 구축할 수 있다. 특히 MAX의 `max["serve"]`로 의존성을 최소화한 경량 서빙이 가능해졌다. [Modular](https://www.modular.com/blog/modular-26-5-mojo-1-0-is-here)
- **Nemotron Lightning 기반 온디바이스 에이전트 실험**: 오픈소스 경량 모델인 Nemotron 3.5 Lightning을 RTX/엣지 환경에 배포해, 고객 데이터를 외부로 전송하지 않는 로컬 에이전틱 워크플로우를 실험해볼 시점이다. NeMo Switchyard로 여러 모델을 라우팅해 작업별 최적 성능을 내는 구조도 가능하다. [NVIDIA Blog](https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/)

## 불확실성 / 계속 볼 것
- **OpenAI 경영진 연쇄 이탈의 의미**: COO Brad Lightcap과 윤리 책임자가 같은 날 퇴사 보도된 점은 OpenAI 내부의 전략적·문화적 변화를 시사한다. 올해 출시 예정인 차세대 모델과의 연관성은 아직 불분명하다. [TechCrunch](https://techcrunch.com/2026/08/11/brad-lightcap-openais-longtime-coo-is-leaving-to-start-something-new/) · [FT](https://www.ft.com/content/e49dfb75-f841-4466-a577-f7aaff8779a0)
- **LLM 추론 암호화는 근본적으로 가능한가**: Stolen Thoughts 연구가 입증한 취약점은 추론 과정을 서버에서 암호화해도 API 블록 수준에서 복원 가능함을 보여준다. 이 문제를 근본적으로 해결하려면 추론 아키텍처 자체를 재설계해야 할 수 있다. [Stolen Thoughts](https://stolen-thoughts.com/)