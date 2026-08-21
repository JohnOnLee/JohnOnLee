---
title: "엔비디아, 풀사이드 모델 팩토리를 60억 달러에 라이선스"
date: 2026-08-22
summary: "엔비디아가 풀사이드의 AI 모델 개발 인프라('모델 팩토리')와 직원 109명을 60억 달러 규모로 라이선스하는 계약을 맺고, 풀사이드는 잔여 회사를 120억 달러 평가로…"
---

## 스타트업 / 제품 / 플랫폼 레이더
- **엔비디아, 풀사이드 '모델 팩토리' 및 인력을 60억 달러에 라이선스**: 엔비디아가 풀사이드의 AI 모델 개발 인프라('모델 팩토리')와 직원 109명을 60억 달러 규모로 라이선스하는 계약을 맺고, 풀사이드는 잔여 회사를 120억 달러 평가로 10억 달러를 추가 조달한다. '인수 없이 기술·인력을 빌리는' 딜 구조가 큰 주목을 받고 있다. [Newcomer](https://www.newcomer.co/p/sources-poolside-strikes-6-billion) · [Bloomberg](https://www.bloomberg.com/news/articles/2026-08-21/nvidia-to-pay-poolside-a-6-billion-license-tap-startup-s-staff)
- **Salesforce 파트너, Agentforce에서 유의미한 매출 못 올려**: 파트너 대상 조사에서 에이전트 플랫폼 Agentforce로 실제 수익을 내지 못한다는 보고가 나왔다. 에이전트 상용화 수요가 강조되는 상황에서 파트너 생태계의 실질 수익화가 지연되는 신호다. [The Register](https://www.theregister.com/saas/2026/08/21/salesforce-partners-are-not-seeing-revenue-from-agentforce-ai-platform-report-says/5291167)
- **AI 데이터 스타트업 Micro1, 5억 달러 매출총이익 실행률 진입**: AI 훈련 열풍 속에서 데이터 라벨링·주석 스타트업 Micro1이 5억 달러 연환산 매출총이익(Gross Run Rate)을 달성했다. 훈련 데이터 파이프라인 수요가 여전히 강함을 보여준다. [TechCrunch](https://techcrunch.com/2026/08/20/ai-data-startup-micro1-reaches-500m-gross-run-rate-amid-ai-training-boom/)
- **궤도 데이터센터 스타트업 Starcloud, 2억 5천만 달러 조달**: 발사 옵션이 줄어드는 상황에서도 Starcloud가 우주 데이터센터 확장 자금 2억 5천만 달러를 확보했다. [TechCrunch](https://techcrunch.com/2026/08/21/starcloud-raises-200-million-for-orbital-data-centers-as-launch-options-dry-up/)

## AI가 바꾸는 미래 신호
- **'모델이 아니라 하네스'가 경쟁 우위가 된다**: 엔비디아 시연에서 AI 모델 자체보다 이를 둘러싼 하네스(오케스트레이션·추론 스택)가 핵심 가치라는 점이 강조됐다. 모델이 상품화되면서 그 주변 인프라에 진입장벽이 생기는 흐름이다. [TechCrunch](https://techcrunch.com/2026/08/21/nvidia-just-showed-that-the-harness-not-the-ai-model-is-now-the-real-hero/)
- **프론티어 MoE를 로컬에서 실행하려는 움직임**: GLM-5.2를 NVFP4 양자화로 포스트-트레이닝하는 작업과, 게이밍 PC에서 290B+ Mixture-of-Experts를 구동하는 오픈소스 프로젝트가 함께 등장했다. 추론 비용과 데이터 민감성 문제로 로컬 실행에 대한 실질 수요가 커지고 있다. [Patronus AI](https://patronus.ai/blog/getting-glm-5-2-nvfp4-post-training-off-the-ground) · [GitHub](https://github.com/FlashML-org/FreeToken)
- **에이전트 물결이 CI를 병목으로 만든다**: 에이전트가 쏟아내는 변경으로 CI가 중단되는 상황이 늘면서, 테스트 선택(테스트 셀렉션)이 대기 시간을 몇 시간에서 몇 분으로 줄이는 사례가 보고됐다. 에이전트 붐의 인프라 병목이 코드 리뷰·CI로 이동하고 있다. [human systems](https://humansystems.dudzik.co/p/when-agents-make-ci-the-bottleneck)

## 현실적인 기회 / 실험 아이디어
- **모델 라이선싱·'모델 팩토리' 인프라 스택**: 풀사이드 딜은 모델 개발 인프라가 독립 자산이 될 수 있음을 보여준다. 학습·파인튜닝 파이프라인을 재사용 가능한 제품으로 만드는 도구에 실험 가치가 있다. [Newcomer](https://www.newcomer.co/p/sources-poolside-strikes-6-billion)
- **로컬 추론·양자화 도구**: 프론티어 MoE를 로컬/엣지에서 돌리려는 수요가 커지는 가운데, NVFP4 같은 양자화 파이프라인과 로컬 MoE 런타임, 그리고 이를 감싸는 배포·모니터링 도구가 현실적 틈새다. [Patronus AI](https://patronus.ai/blog/getting-glm-5-2-nvfp4-post-training-off-the-ground) · [GitHub](https://github.com/FlashML-org/FreeToken)
- **에이전트 시대의 테스트 선택·CI 옵저버빌리티**: 에이전트가 생성하는 대규모 변경에 맞춘 지능형 테스트 선택과 CI 대기열 관리 소프트웨어가 명백한 수요다. [human systems](https://humansystems.dudzik.co/p/when-agents-make-ci-the-bottleneck)

## 불확실성 / 계속 볼 것
- **Salesforce Agentforce 파트너 수익화 지연**: 에이전트 플랫폼의 홍보 강도와 실제 파트너 매출 사이의 격차가 확인됐다. 에이전트 시장이 '수요 신호'에서 '수익화'로 넘어가는 속도를 지켜볼 필요가 있다. [The Register](https://www.theregister.com/saas/2026/08/21/salesforce-partners-are-not-seeing-revenue-from-agentforce-ai-platform-report-says/5291167)
- **프론티어 모델 규제·안전 거버넌스 방향**: 엔비디아·스페이스X·MS의 AI 안전 이니셔티브와 브런데이지의 가드레일 주장이 겹치며, 프론티어 모델 검증과 안전 운영이 어떻게 제도화될지가 여전히 미정이다. [The Guardian](https://www.theguardian.com/commentisfree/2026/aug/21/openai-frontier-ai-speed)