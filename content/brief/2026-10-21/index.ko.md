---
title: "딥시크 DeepInfer 오픈소스, 추론 비용이 다시 내려갑니다"
date: 2026-10-21
summary: "10월 20일 딥시크가 자사 추론 엔진 DeepInfer를 깃허브에 아파치 2.0 라이선스로 공개했습니다."
---

## 딥시크가 자사 추론 엔진 DeepInfer를 아파치 2.0으로 공개했습니다

10월 20일 딥시크가 자사 추론 엔진 DeepInfer를 깃허브에 아파치 2.0 라이선스로 공개했습니다. [GitHub](https://github.com/deepseek-ai/DeepInfer)

자사 서비스를 돌리는 데 실제로 쓰는 엔진이고 지금 지원하는 모델은 자체 모델인 V4.1-Flash 하나입니다. 도는 칩은 엔비디아 SM100 GPU와 화웨이 어센드 950 NPU. 구성은 대부분 vLLM 위에 세웠고 SGLang과 엔비디아 TensorRT-LLM도 참고했습니다. [The Next Web](https://thenextweb.com/news/deepseek-deepinfer-open-source-inference-engine)

기능은 추론을 여러 칩에 나눠 돌리는 병렬화, 몇 토큰을 미리 뽑아 한 번에 검증하는 speculative decoding, 실행마다 같은 출력을 내는 결정성, 정해진 형식으로 답을 묶는 structured output입니다. 성능 수치는 모두 회사가 직접 낸 값. 프롬프트 처리는 SM100 네 장, 출력 생성은 예순네 장에서 쟀고 독립 검증은 아직 없습니다. [TechTarget](https://www.techtarget.com/ai/news/366652363/DeepSeek-makes-DeepInfer-open-source-to-cut-AI-costs) [Bloomberg](https://www.bloomberg.com/news/articles/2026-10-20/deepseek-unveils-open-source-tool-to-help-cut-ai-operating-costs)

## 같은 주에 미국 정부는 딥시크를 연방 민간기관에서 빼라고 했습니다

미국 국토안보부가 연방 민간기관에 딥시크 기술을 쓰지 말고 이미 들어간 것도 걷어내라고 지시했습니다. 이 주문은 10월 20일 연방관보에 실렸습니다. 문구가 넓죠. 딥시크와 딥시크 계열 제품뿐 아니라 "딥시크 구현을 이용해 만든 제3자 제품과 서비스"까지 포함합니다. [The Register](https://www.theregister.com/security/2026/10/20/deepseek-deep-sixed-at-all-us-federal-civilian-agencies/5304010) [Federal Register](https://www.federalregister.gov/documents/2026/10/20/2026-21447/notice-of-order-regarding-exclusion-and-removal-of-deepseek-products-from-federal-civilian-executive)

어디까지인지가 애매한데, 딥시크 모델을 API로 계속 불러오는 경우만 뜻하는지 딥시크 도움을 받아 만든 앱까지 포함하는지 문서에 답이 없습니다. 게이트웨이가 끼면 더 애매하죠.

OpenRouter나 Vercel AI Gateway는 기본 설정에서 요청에 맞는 제공자를 알아서 고르기 때문에, 제약을 걸어두지 않으면 딥시크 모델이 뒤에서 돌아갈 수 있습니다.

제품을 만드는 쪽이 지금 챙길 건 값과 의존 범위. 게이트웨이를 쓴다면 라우팅에서 제공자를 직접 지정해 두고, 미국 공공이나 규제 시장을 노린다면 어느 모델이 어디서 도는지 설정과 계약 양쪽에서 확인해 두는 편이 낫습니다. 이번 주에 열린 것과 막힌 것이 같이 나왔으니 싸다는 이유만으로 한 제공자에 오래 묶이는 선택은 다시 따져볼 만합니다.

## 오늘의 다른 소식 (한 줄)

- **미니맥스 M3.1 Flash 공개**: 에이전트 작업 기준 사용 비용이 이전 모델보다 70% 낮아졌고, 100만 토큰당 입력 0.15달러에 출력 0.60달러입니다. 익명으로 200조 토큰을 처리한 "Space Bunny"가 이 모델의 초기 버전이었습니다. [MiniMax](https://www.minimax.io/blog/minimax-m31f)
- **앤스로픽 S-1, 상반기 순손실 800억 달러 넘김**: 개정 상장 서류에 컴퓨트 비용으로 최대 7,500억 달러를 쓸 수 있다고 적었습니다. [WSJ](https://www.wsj.com/tech/ai/anthropic-revenue-growth-ipo-accaf0f1) [Channel News Asia](https://www.channelnewsasia.com/business/anthropic-logged-net-loss-over-80-billion-in-first-half-2026-wsj-reports-6476676)
- **오픈AI, COBOL 마이그레이션 평가 97.9%**: GPT-6.1 Sol이 기존 5.4%에서 97.9%로 올랐고, 낮은 추론 노력에서는 86.6%를 기록했습니다. [Dataconomy](https://dataconomy.com/2026/10/20/openai-gpt-6-cobol-coding-migration-gains/) [OpenAI](https://openai.com/index/low-resource-programming-languages/)
- **바이트댄스·알리바바·텐센트, 엔비디아 칩 350억 달러어치 주문**: RTX PRO 5500 300만 장이 넘고 장당 1만 1,400달러 수준입니다. [The Edge Malaysia](https://theedgemalaysia.com/node/822533)
- **스포티파이, 추천에서 AI 슬롭 5천만 곡 제거**: 지난 1년간 걸러낸 규모이고, 사람이 만든 곡을 우선하도록 추천 방식을 바꿨습니다. [The Verge](https://www.theverge.com/entertainment/1014284/spotify-ai-slop-spam-songs-removed)
- **영국 FCA, AI 실패와 니어미스 보고 요구**: 금융사 사고 보고 의무를 중요한 AI 실패와 니어미스까지 넓히겠다고 밝혔습니다. [The Register](https://www.theregister.com/ai-and-ml/2026/10/20/uk-finance-watchdog-wants-firms-to-report-ai-failures-and-close-calls/5304078)