---
title: "Meta Muse Spark Open 공개, 로컬은 맥 스튜디오 두 대"
date: 2026-10-16
summary: "10월 15일 메타가 Muse Spark Open의 가중치를 공개했습니다. 파라미터 816B에 컨텍스트 100만 토큰, 텍스트와 이미지, 영상, 오디오를 입력받는 모델입니다."
---

## 메타가 816B 오픈웨이트 Muse Spark Open을 공개했습니다

10월 15일 메타가 Muse Spark Open의 가중치를 공개했습니다. 파라미터 816B에 컨텍스트 100만 토큰, 텍스트와 이미지, 영상, 오디오를 입력받는 모델입니다. [Meta AI Research](https://research.meta.ai/blog/muse-spark-open) [Hugging Face](https://huggingface.co/collections/meta-models/muse-spark-open)

구조와 실행 조건을 보면 쓸 자리가 분명해집니다. 토큰마다 42B만 활성화하는 MoE라 816B를 통째로 계산하지 않고, 로컬에서는 M5 Ultra 맥 스튜디오 512GB 두 대를 MLX로 묶어 통합 메모리 1TB에 올립니다. 애플은 512GB 구성의 맥 스튜디오를 아직 내놓지 않았고, 256GB 모델 가격이 이미 1만 달러를 넘습니다. [MacRumors](https://www.macrumors.com/2026/10/15/meta-muse-spark-open-mac-studio/)

가중치는 Hugging Face를 비롯해 아마존 SageMaker AI와 구글 클라우드 모델 가든, 마이크로소프트 파운드리 모델에서도 받습니다. 추론 API로는 Baseten·Fireworks AI·Groq·Modal·Nebius·OpenRouter·Together AI가 제공하고, SGLang·vLLM·TensorRT-LLM·llama.cpp·MLX·Unsloth가 첫날부터 지원합니다. 라이선스는 Muse Model License죠. 복사와 수정, 증류와 배포는 무료지만 제품 화면에 "Built with Muse Spark Open"을 표시해야 합니다. 모델을 서비스로 파는 사업의 최근 12개월 매출이 2천만 달러를 넘으면 메타와 별도 계약이 필요하고, 내부 사용이나 자기 제품 안의 구성 요소로 쓰는 경우에는 이 조건이 붙지 않습니다. [Unite.AI](https://www.unite.ai/metas-816b-parameter-muse-spark-open-weights-are-now-public/)

## 메타가 공개한 표에서 이 모델은 코딩보다 에이전트 작업이 강합니다

수치는 메타가 함께 낸 모델 카드 기준입니다. 에이전트 평가에서는 JobBench 61.8, MCP-Atlas 89.2로 카드에 실린 다른 모델보다 높습니다. 코딩은 다르죠. Terminal-Bench 2.1은 76.4로 Kimi K3의 85.0에 못 미치고, Artificial Analysis 지능 지수는 39로 GLM 5.3의 45와 Kimi K3의 44보다 낮습니다. "미국에서 가장 성능이 높은 오픈웨이트"라는 말은 미국 모델끼리의 비교입니다.

인디 빌더에게 달라지는 건 고르는 기준이죠. 발표문의 최상급 표현보다 자기 제품이 실제로 하는 일에 맞는 벤치마크를 봐야 합니다. 문서와 화면을 읽히는 에이전트라면 후보가 되고, 코드 생성이 중심이면 중국 오픈웨이트가 아직 앞섭니다.

두 번째로 열린 것은 튜닝입니다. 완전한 가중치가 풀렸으니 TorchTitan이나 Hugging Face TRL, Unsloth로 자기 데이터에 맞춰 미세조정하고, 그 사본을 빌린 GPU에 올릴 수 있고, Fireworks와 Together의 관리형 학습을 쓰는 길도 있습니다. 맥 두 대를 살 형편이 아니어도 자기 데이터로 튜닝한 모델을 제품에 넣는 길은 생겼습니다.

아직 확정되지 않은 것도 있습니다. 전체 평가 보고서는 나오지 않았고, 메타는 모델 카드에서 파인튜닝이 안전장치를 약화시킬 수 있다고 적었습니다. 512GB 맥 스튜디오의 출시 시점과 가격도 공개되지 않았습니다.

## 오늘의 다른 소식 (한 줄)

- **퍼플렉시티, 에이전트 샌드박스 SPACE 공개**: 자사 에이전트를 가둬 두는 데 쓰던 격리와 복구, 네트워크 제어 계층을 Apache 2.0으로 열었고 CoreWeave와 Akamai, Crusoe가 고객에게 제공하기로 했습니다. [Perplexity](https://www.perplexity.ai/hub/blog/open-sourcing-space)
- **엔비디아, 120B 비전언어 모델 Nemotron 3.5 Super VL 공개**: 토큰마다 12B만 활성화하는 MoE로 텍스트와 이미지, 문서, 영상을 읽고 vLLM과 SGLang에서 첫날부터 돌아갑니다. [NVIDIA](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning/)
- **FTC, OpenAI와 Anthropic에 문서 요구**: 두 회사의 안전 사고와 보호장치, 개인정보 처리에 관한 50쪽짜리 민사 조사 요구를 보냈습니다. [Ars Technica](https://arstechnica.com/tech-policy/2026/10/ftc-probes-if-openai-anthropic-security-incidents-harmed-americans-report-says/)
- **앤트로픽 3분기 매출 168억 달러**: 전분기 116억 달러에서 45% 늘고 조정 기준 흑자를 냈습니다. 다만 성장률이 143%에서 46%로 내려앉으면서 투자자들이 기업가치를 2조 달러 대신 1조 5천억 달러 쪽으로 잡는 이야기가 나옵니다. [CNBC](https://www.cnbc.com/2026/10/15/anthropics-third-quarter-revenue-hits-16point8-billion-ipo.html)
- **AI와 반도체 주식 1조 달러 증발**: 이번 주 SK하이닉스가 10% 넘게 빠지고 삼성전자가 8.7%, 어드반테스트가 14% 가까이 밀리면서 20개 종목에서 1조 달러가 사라졌습니다. [CNBC](https://www.cnbc.com/2026/10/15/sk-hynix-samsung-softbank-stocks-asia-tech-rout-ai-funding-worries.html)
- **피그마, 에이전트용 디자인 규칙 Specs 공개**: 사람과 AI 에이전트가 같은 문서를 보고 작업하도록 디자인 언어를 Markdown으로 적는 편집기이고, 코드 레이어는 퍼블릭 베타로 열렸습니다. [Figma](https://www.figma.com/blog/introducing-figma-specs/)
- **블루스키, Attie로 게임과 웹사이트 제작**: 커스텀 피드를 만들던 AI 도구가 AT 프로토콜 위에서 퀴즈와 게임, 웹사이트까지 만들도록 넓어졌습니다. [TechCrunch](https://techcrunch.com/2026/10/15/bluesky-expands-its-ai-powered-attie-app-to-let-anyone-build-websites-games-and-more/)