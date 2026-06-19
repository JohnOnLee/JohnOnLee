---
title: "AI·스타트업 모닝 브리프 - 2026-06-20"
date: 2026-06-20
summary: "트랜스포머 공동 저자 Noam Shazeer, 구글 떠나 OpenAI 합류: 'Attention Is All You Need' 논문의 공동 저자이자 구글 Gemini 공동 리드였던 Shazeer가 OpenAI로 이적했다. OpenAI IPO를 앞두고 전 트럼프 백악관 AI 정책 담당자 Dean Ball도 함께 영입. 최…"
description: "트랜스포머 공동 저자 Noam Shazeer, 구글 떠나 OpenAI 합류: 'Attention Is All You Need' 논문의 공동 저자이자 구글 Gemini 공동 리드였던 Shazeer가 OpenAI로 이적했다. OpenAI IPO를 앞두고 전 트럼프 백악관 AI 정책 담당자 Dean Ball도 함께 영입. 최…"
---

[브리핑/AI] AI·스타트업 모닝 브리프 - 2026-06-20

## 핵심 변화
- **트랜스포머 공동 저자 Noam Shazeer, 구글 떠나 OpenAI 합류**: "Attention Is All You Need" 논문의 공동 저자이자 구글 Gemini 공동 리드였던 Shazeer가 OpenAI로 이적했다. OpenAI IPO를 앞두고 전 트럼프 백악관 AI 정책 담당자 Dean Ball도 함께 영입. 최상위 AI 인재 쟁탈전이 가속화되고 있으며, IPO를 준비 중인 OpenAI에겐 상징적 의미가 큰 영입이다. [Reuters](https://www.reuters.com/technology/googles-gemini-co-lead-noam-shazeer-join-openai-2026-06-18/) · [TechCrunch](https://techcrunch.com/2026/06/18/openai-is-bringing-on-some-big-guns-in-the-lead-up-to-its-ipo/)
<!--more-->
- **구글과 아마존, Nvidia AI 칩 독점에 동시다발적 도전**: WSJ에 따르면 구글은 Nvidia의 플레이북을 활용해 클라우드 중립적인 AI 칩 비즈니스를 구축 중이다. 같은 날 아마존도 자사 Trainium 칩을 서드파티에 직접 판매하는 방안을 추진 중이라고 확인했다. Andy Jassy CEO는 Trainium이 독립 사업이었다면 연간 $500억 런레이트 규모라고 밝혔다. AI 칩 시장이 빠르게 다극화되고 있다. [WSJ](https://www.wsj.com/tech/ai/google-is-using-nvidias-playbook-to-build-a-rival-ai-chip-business-1eac86f9) · [TechCrunch](https://techcrunch.com/2026/06/18/amazon-hopes-to-challenge-nvidia-more-directly-by-selling-its-ai-chips/)
- **AI 모델의 진짜 병목은 '데이터 블랙홀' — 샘플 효율성이 아니라 데이터다**: Dwarkesh Patel의 분석에 따르면, 최근 AI 발전의 대부분은 더 많고 더 나은 데이터에서 비롯됐으며, 근본적인 샘플 효율성(데이터당 학습량)은 크게 개선되지 않았다. RL과 합성 데이터 생성은 결국 인간 전문가의 궤적 데이터(trajectory data)에 의존하며, 이 데이터의 생산 비용과 규모가 실질적인 한계다. 단순한 스케일링 법칙만 믿고 있어선 안 된다는 경고. [Dwarkesh](https://www.dwarkesh.com/p/the-sample-efficiency-black-hole-2)

## 스타트업 / 제품 / 플랫폼 레이더
- **Elastic, AI 버그 탐지 스타트업 Deductive AI를 최대 $85M에 인수**: 2023년 설립되어 작년 11월 $7.5M 시드($33M 밸류)를 받은 지 7개월 만의 엑시트. AI가 작성한 코드가 폭증하면서 AI 기반 SRE(사이트 신뢰성 엔지니어링) 툴에 대한 수요가 급증하고 있다. 기존 기업들이 agentic AI 툴링을 빠르게 흡수하는 패턴. [TechCrunch](https://techcrunch.com/2026/06/18/source-elastic-agrees-to-buy-crv-backed-deductiveai-for-up-to-85m/)
- **AI 추론 스타트업 Baseten, $15억 규모 투자 유치로 $130억 밸류에이션**: 5개월 만에 밸류에이션이 160% 상승. 일부 투자자는 $130억, 다른 투자자는 $110억에 참여하는 분할가격 라운드(split-priced round) 구조. AI 추론 골드러시가 식지 않고 있지만, 구조의 복잡성이 리스크 신호라는 해석도 있다. [TechCrunch](https://techcrunch.com/2026/06/18/ai-inference-startup-baseten-reportedly-raising-1-5b-months-after-its-last-mega-round/)
- **Snap, AI 영상팀을 Dotmo로 분사 — 비용 부담이 직접적 원인**: CTO Bobby Murphy가 개인 자격으로 리드 투자자로 참여하고, Snap은 Dotmo 기술에 대한 라이선스를 확보하는 구조. 빅테크들이 AI R&D 비용을 내부에서 감당하기 어려워져 분사+라이선스백 모델을 선택하는 패턴이 늘고 있다. [TechCrunch](https://techcrunch.com/2026/06/18/snap-spins-off-ai-video-team-into-new-company-dotmo-due-to-costs/)

## AI가 바꾸는 미래 신호
- **에이전트의 자가학습 메모리가 제품 단계로 진입**: Perplexity가 에이전트가 상호작용 이력에서 학습하고 개선되는 '자가 개선 메모리' 아키텍처를 공개했다. 에이전트 메모리가 단순한 RAG를 넘어 진정한 학습 루프로 진화하고 있다. 이는 에이전트가 장기간 사용될수록 더 똑똑해진다는 의미. [Perplexity](https://www.perplexity.ai/hub/blog/self-improving-memory-for-agents)
- **비즈니스 AI 에이전트가 빅테크의 다음 격전지로**: 구글, 마이크로소프트, OpenAI, 아마존이 모두 챗봇을 넘어 다단계 워크플로를 자율 실행하는 비즈니스 에이전트로 전환 중. '묻는 AI'에서 '실행하는 AI'로의 전환이 다음 플랫폼 전쟁이다. [RNZ](https://www.rnz.co.nz/news/science-and-technology/600928/more-than-chatbots-why-business-ai-agents-are-big-tech-s-next-product-battleground)

## 현실적인 기회 / 실험 아이디어
- **전문가 궤적 데이터(Expert Trajectory Data) 시장이 진짜 병목이다**: Dwarkesh의 분석이 명확히 보여주듯, AI 발전의 실질적 제약은 인간 전문가의 작업 데이터를 대규모로 생산하는 파이프라인이다. Mercor, Surge 같은 기업들이 이 공간에서 빠르게 성장 중이며, 특정 버티컬 도메인의 전문가 데이터 마켓플레이스를 구축하는 것은 아직 초기 기회다. [Dwarkesh](https://www.dwarkesh.com/p/the-sample-efficiency-black-hole-2)
- **AI 칩 다각화는 조달 전략상의 기회**: 구글과 아마존이 모두 서드파티 칩 시장에 진입하면서, GPU 의존 인프라를 운영하는 기업들은 비Nvidia 옵션을 적극 평가할 시점이다. 초기 도입자는 시장이 타이트해지기 전에 유리한 가격과 공급 계약을 확보할 수 있다. [WSJ](https://www.wsj.com/tech/ai/google-is-using-nvidias-playbook-to-build-a-rival-ai-chip-business-1eac86f9) · [TechCrunch](https://techcrunch.com/2026/06/18/amazon-hopes-to-challenge-nvidia-more-directly-by-selling-its-ai-chips/)

## 불확실성 / 계속 볼 것
- **AI 추론 스타트업 밸류에이션의 지속가능성**: Baseten의 5개월 만의 160% 밸류에이션 급등과 분할가격 라운드 구조는 시장의 과열을 시사한다. AI 추론이 예상보다 빨리 코모디티화된다면 현재 밸류에이션을 정당화하기 어려울 수 있다. [TechCrunch](https://techcrunch.com/2026/06/18/ai-inference-startup-baseten-reportedly-raising-1-5b-months-after-its-last-mega-round/)
- **아마존·구글의 칩 전략이 Nvidia를 실제로 위협할 수 있을까**: 두 회사 모두 막대한 강점(AWS 에코시스템, 구글 TPU 역사)을 갖고 있지만, Nvidia의 CUDA 해자는 여전히 깊고 넓어지고 있다. 향후 6~12개월 기업 도입 데이터가 판가름할 것이다. [WSJ](https://www.wsj.com/tech/ai/google-is-using-nvidias-playbook-to-build-a-rival-ai-chip-business-1eac86f9) · [TechCrunch](https://techcrunch.com/2026/06/18/amazon-hopes-to-challenge-nvidia-more-directly-by-selling-its-ai-chips/)