---
title: "하이쿠 5.5, 소형 모델값 90% 인하"
date: 2026-10-08
summary: "앤스로픽이 10월 7일 Claude Haiku 5.5를 공개했습니다. 입력 100만 토큰당 0.10달러, 출력 0.50달러입니다. Haiku 4.5가 입력 1달러, 출력 5달러였으니 10만 토큰 이하…"
---

## 앤스로픽이 소형 모델 값을 10분의 1로 내렸습니다

앤스로픽이 10월 7일 Claude Haiku 5.5를 공개했습니다. 입력 100만 토큰당 0.10달러, 출력 0.50달러입니다. Haiku 4.5가 입력 1달러, 출력 5달러였으니 10만 토큰 이하 프롬프트에서는 값이 정확히 10분의 1로 줄었습니다. 프롬프트가 10만 토큰을 넘으면 입력 0.50달러, 출력 2.50달러로 올라가고, 캐시 읽기는 0.01달러입니다. 컨텍스트 창은 100만 토큰, 최대 출력은 12만 8천 토큰이고, Claude API와 아마존 베드락, 구글 클라우드, 마이크로소프트 파운드리에서 바로 호출할 수 있습니다. 회사는 평균 운영 비용이 약 75% 줄었다고 밝혔습니다. [Anthropic](https://www.anthropic.com/claude-haiku-5-5) [Claude Platform](https://platform.claude.com/docs/en/models/haiku-5-5/overview)

같은 날 값표도 함께 손봤습니다. Sonnet 5.5의 캐시 읽기 단가를 절반으로 내려 에이전트 작업에서 약 20% 싸졌고, Max와 Team 구독자에게는 매달 API 크레딧이 붙습니다. 오픈AI도 같은 날 GPT-6를 모든 ChatGPT 등급에 풀었고, 무료 등급은 GPT-6 Luna가 맡습니다. 소형 모델 자리에서 두 회사가 값을 맞춘 셈입니다.

## 청구서는 10만 토큰 경계와 토크나이저가 정합니다

에이전트 제품 원가를 정하는 건 정가표 한 줄이 아니라 청구서입니다. 10만 토큰을 넘기면 입력 단가가 5배가 되니, 긴 컨텍스트를 호출마다 다시 보내는 구조라면 인하 폭을 그대로 받지 못합니다. 배치 API를 쓰면 입력과 출력이 50% 더 깎입니다.

토크나이저가 바뀐 것도 변수입니다. 같은 문장이 Haiku 4.5보다 약 30% 많은 토큰으로 세어지므로, 10분의 1 인하가 청구서에서는 그만큼 줄어듭니다. 회사가 말한 평균 75% 절감도 이 계산 위에서 나온 값입니다. 분류와 요약, 라우팅, 서브에이전트처럼 짧은 호출이 많은 자리부터 옮겨 보고, 어려운 한 턴은 상위 모델에 남기는 편이 안전합니다.

## 비교 수치는 아직 회사 값입니다

Haiku 5.5의 성능 수치는 대부분 앤스로픽이 직접 낸 시스템 카드에서 나왔습니다. 서드파티가 다시 재면 순위가 달라질 수 있고, GPT-6 Luna와의 우열도 워크로드에 따라 갈립니다. 10만 토큰 경계와 토크나이저 변화는 문서에 적힌 사실이니, 자기 프롬프트의 토큰 수와 청구액을 재보기 전에는 절감 폭을 확정하기 어렵습니다.

## 오늘의 다른 소식 (한 줄)

- **오픈AI, GPT-6를 전 등급에**: Intelligent UI가 답변을 차트와 버튼, 입력 폼 같은 조작 가능한 화면으로 바꾸고, 유료 등급에 이어 무료와 Go 등급에도 10월 8일부터 적용됩니다. [OpenAI](https://openai.com/index/gpt-6-for-everyone/)
- **윈도우 ML에 llama.cpp 합류**: GGUF 모델을 WinMLServer 하나로 돌려 OpenAI 호환 엔드포인트를 얻고, 윈도우가 GPU와 NPU, CPU를 알아서 고릅니다. [Windows Blog](https://blogs.windows.com/windowsexperience/2026/10/07/building-windows-for-hybrid-intelligence/)
- **구글 플레이그라운드 공개**: 문장만 넣으면 브라우저 게임이 만들어져 바로 플레이하고 공유할 수 있는 실험실 플랫폼이고, 지금은 미국 18세 이상만 씁니다. [TechCrunch](https://techcrunch.com/2026/10/07/google-experiments-with-an-ai-powered-gaming-platform/)
- **구글 SynthID 검증 개방**: 이미지와 영상, 오디오가 생성 모델에서 나왔는지 누구나 확인하는 사이트를 열었고, 하루 100만 건 검증 요청이 들어온다고 밝혔습니다. [TechCrunch](https://techcrunch.com/2026/10/07/googles-new-synthid-website-can-identify-ai-generated-media/)
- **메타 뮤즈, 아이패드로**: 출시 한 달 만에 전용 아이패드 앱을 냈고, 센서타워 추정 설치 수는 660만 건입니다. [TechCrunch](https://techcrunch.com/2026/10/07/metas-muse-launches-on-ipad-just-a-month-after-its-mobile-debut/)
- **개인 비서 Tab, 3억 달러 가치로 등장**: 스텔스에서 나온 개인 AI 비서 스타트업이고, 정확한 투자 내역은 공개하지 않았습니다. [TechCrunch](https://techcrunch.com/2026/10/07/another-personal-ai-assistant-has-launched-meet-tab-which-emerged-from-stealth-with-a-300m-valuation/)