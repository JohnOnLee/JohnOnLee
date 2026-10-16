---
title: "중국, AI 모델 가중치 수출통제 초안"
date: 2026-10-17
summary: "10월 16일 중국 상무부와 과학기술부가 수출 금지·제한 기술 목록 개정안을 함께 내놨습니다. 40개 가운데 23개가 AI이고, 대형 모델과 에이전트, 칩 설계, 컴퓨팅…"
---

## 중국이 AI 모델 가중치와 소스코드를 수출통제 목록에 올리는 초안을 냈습니다

10월 16일 중국 상무부와 과학기술부가 수출 금지·제한 기술 목록 개정안을 함께 내놨습니다. 40개 가운데 23개가 AI이고, 대형 모델과 에이전트, 칩 설계, 컴퓨팅 클러스터가 들어갔습니다. 목록 전체로는 14개가 금지, 26개가 제한입니다. [AP](https://apnews.com/article/china-export-restrictions-ai-chips-solar-us-5ac381c0c6d6628bbea2e0da7d855a5b) [The Verge](https://www.theverge.com/ai-artificial-intelligence/1012753/china-is-weighing-export-controls-on-ai)

새로 목록에 오른 건 학습이 끝난 모델의 가중치와 소스코드, 체크포인트, 아키텍처, 학습과 추론 방법입니다. 지금까지 중국의 수출통제가 칩과 장비에 머물렀던 것과 달리 소프트웨어를 직접 겨냥했습니다. 발동 조건도 숫자로 정해졌죠. 학습 연산량 10^26 FLOPs, 파라미터 2조 개 이상, 또는 전 세계 상위 10위권 성능이면 통제 대상입니다. 중국의 '중요 데이터'로 학습하고 그 데이터를 근거로 서비스를 파는 모델은 금지 쪽으로 갑니다. 파라미터 2조를 넘는 중국 모델로는 문샷의 Kimi K3와 알리바바의 Qwen 3.8-Max가 꼽힙니다. [the-decoder](https://the-decoder.com/china-tightens-export-controls-on-open-weight-models-and-23-key-ai-technologies/)

예외는 넓게 뒀습니다. API와 웹사이트, 앱, SaaS로 쓰는 경로는 통제 밖이고, 이미 오픈소스로 공개됐거나 논문으로 나온 기술은 아예 빠집니다. 제한 기술을 오픈소스로 공개할 때와 자사 해외 데이터센터에서 돌릴 때는 자동 허가를 주는 절차도 함께 넣었지만, 다른 회사 해외 서버에 얹는 경우에는 정식 수출 허가가 필요합니다. 의견 수렴은 11월 15일까지이고, 최종 규칙이 나오기 전까지는 대상 기술의 수출을 사전 등록해야 합니다.

## 값싼 중국 오픈웨이트 위에 제품을 세웠다면 공급 경로를 다시 봐야 합니다

이미 내려받은 가중치는 이번 초안의 적용을 받지 않습니다. 공개된 오픈소스와 논문은 통제 대상에서 빠진다고 명시했기 때문입니다. API나 SaaS로 Qwen과 DeepSeek을 쓰는 제품도 오늘 당장 달라지는 게 없습니다. 흔들리는 쪽은 앞으로 나올 가중치죠. 임계값이 어디에 걸리느냐에 따라 프런티어급 중국 오픈웨이트의 해외 배포가 허가제로 넘어갈 수 있는데, 그 값은 아직 공개되지 않았죠.

모델을 직접 돌리는 제품은 한 줄을 더 봐야 합니다. 제한 대상 모델을 자사 해외 데이터센터에서 돌리는 건 자동 허가로 처리되지만, 다른 회사 서버에 얹는 건 정식 수출 허가를 받아야 합니다. 학습과 추론을 한 제공사에만 맡기고 그 모델 위에 제품을 얹은 구조라면, 11월 15일 이후 최종 규칙이 그 경로를 건드릴 수 있습니다.

## 오늘의 다른 소식 (한 줄)

- **미국 8개 주, OpenAI 상대 소송**: 아칸소와 애리조나, 아이다호, 아이오와, 캔자스, 몬태나, 네브래스카, 웨스트버지니아 법무장관이 소비자보호법과 제조물책임법으로 각각 소송을 내고 ChatGPT가 아동에게 안전하지 않으며 회사가 그 위험을 숨겼다고 주장했습니다. [Law.com](https://www.law.com/2026/10/16/8-states-sue-openai-over-chatgpts-alleged-risks-to-children/)
- **인도 CERT-In, AI 에이전트가 기업 운영 시스템에 접근했다고 경고**: 여러 모델 제공사가 연구와 평가 과정에서 자국 기업 시스템에 모델이 닿았다고 당국에 알렸고, 인도 사이버보안청이 최고 등급 경고를 냈습니다. [The Hindu](https://www.thehindu.com/sci-tech/technology/after-openais-australia-hack-indias-cyber-agency-says-ai-agents-breachedsystems/article71591537.ece)
- **메타, 10월 30일 상업약관으로 비즈니스 계정 연결 웹사이트 크롤링 허용**: 비즈니스 계정으로 페이스북과 인스타그램, 왓츠앱을 계속 쓰면 연결된 웹사이트를 메타가 긁어 AI 학습에 쓸 수 있게 되고, 법률 전문가들은 뉴스 사이트도 대부분 여기 걸린다고 봅니다. [Editor & Publisher](https://www.editorandpublisher.com/stories/metas-new-commercial-terms-will-allow-the-scraping-of-news-sites-legal-experts-say,264042)
- **텐센트, 기억 전용 모델 Hy-Memory-30B-A3B 공개**: 30B MoE에 활성 3B로 Mem0과 MemOS, 자사 Hy-Memory 프레임워크의 일반 모델 자리를 대신하고, 자체 평가에서 네 개 하네스 평균 55.49로 Claude Opus 5의 54.62를 앞선다고 밝혔습니다. Apache 2.0이고 vLLM으로 돌립니다. [Tencent Hunyuan](https://memory.hunyuan.tencent.com/) [Hugging Face](https://huggingface.co/tencent/Hy-Memory-30B-A3B)
- **이번 주 최대 펀딩 라운드는 규모가 줄었지만 1위는 Modal Labs**: Accel이 주도한 Series D로 7억 5천만 달러를 받고 기업가치 157억 5천만 달러를 인정받았습니다. 에이전트 평가와 학습 도구를 만드는 Labelbox도 1억 달러를 받았습니다. [Crunchbase News](https://news.crunchbase.com/venture/biggest-funding-rounds-investors-scaled-back-ai-biotech-modal/)