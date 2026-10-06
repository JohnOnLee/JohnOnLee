---
title: "미스트랄 Large 4, 1T 오픈웨이트 예고"
date: 2026-10-07
summary: "프랑스 미스트랄이 10월 6일 Mistral Large 4의 공개 프리뷰를 시작했습니다. 회사가 붙인 별명은 le Chonk입니다. 파라미터 1조 개 중 토큰마다 49B만 활성화하는 MoE…"
---

## 미스트랄이 1조 파라미터 모델 Large 4를 API에 올렸습니다

프랑스 미스트랄이 10월 6일 Mistral Large 4의 공개 프리뷰를 시작했습니다. 회사가 붙인 별명은 le Chonk입니다. 파라미터 1조 개 중 토큰마다 49B만 활성화하는 MoE 구조이고, 이미지 입력과 텍스트 출력을 함께 다룹니다. 유럽에 있는 미스트랄 자체 데이터센터에서 엔비디아 Grace Blackwell GPU 3,800장으로 처음부터 학습했습니다. 가중치는 이달 말 공개되고, 그때까지 사이버보안 기관과 파트너, 정부 기관을 상대로 레드팀 테스트를 함께 돌립니다. [Mistral](https://mistral.ai/news/mistral-large-4)

가격은 정가와 청구가가 다릅니다. 오픈라우터에는 입력 100만 토큰당 0.68달러, 출력 2.09달러로 올라와 있습니다. Artificial Analysis가 측정한 정가는 입력 1.36달러, 출력 4.18달러이고, 같은 기관이 집계한 모델 중간값은 입력 2.00달러, 출력 10.00달러입니다. 캐시를 재사용하면 입력 단가가 90% 깎여 100만 토큰당 0.07달러까지 내려갑니다. [Artificial Analysis](https://artificialanalysis.ai/models/mistral-large-4)

성능은 회사 주장과 독립 측정이 갈립니다. 미스트랄은 미국과 유럽에서 나온 오픈웨이트 모델 중 최고라고 말합니다. Artificial Analysis의 Intelligence Index에서 Large 4 프리뷰는 38점을 받았고 225개 모델 중 64위입니다. 같은 기관의 사이버 지수에서는 상위 5위권이고, 취약점을 재현한 뒤 패치하는 테스트에서 82%를 냈습니다. 미스트랄은 Claude Opus 5.5와 GPT-6 Astra가 그 테스트에서 거의 0점을 받았다고 밝혔습니다. 답을 거부한 결과입니다.

## 에이전트를 돌리는 쪽에서는 원가 계산이 오늘 바뀝니다

에이전트 제품에서 토큰 단가는 제품 원가입니다. 같은 컨텍스트를 호출마다 다시 보내는 구조라면 입력 가격과 캐시 할인이 그대로 마진이 됩니다. Large 4 프리뷰는 오늘부터 API로 호출할 수 있으니, 자기 프롬프트와 평가셋으로 돌려보고 기존 모델과 값을 비교할 수 있습니다. 오픈라우터 가격은 정가의 절반 수준이고, 언제까지 그 가격인지는 공지되지 않았습니다.

가중치를 기다릴 이유도 분명합니다. 이달 말 공개되면 파인튜닝한 모델과 평가 자산이 자기 것으로 남고, 벤더가 값을 올릴 때 옮겨갈 자리가 생깁니다. 지금 그 자리에 있는 건 중국 오픈 모델이 대부분이었고, 유럽에서 1조 파라미터 규모로 나오는 건 이번이 처음입니다.

## 자체 호스팅은 노트북 일이 아닙니다

전체 파라미터가 1조 개입니다. 49B만 활성화한다고 해도 1조 개 분량을 담아야 하니, 노트북이나 개인 GPU 한 장으로는 돌릴 수 없습니다. 임대 GPU 클러스터나 온프레미스 장비가 필요한 규모이고, 어제 나온 Reflection Beam보다 무겁습니다.

라이선스 문구는 아직 없습니다. Apache 2.0인지 상업적 제한이 붙는지는 가중치와 함께 나올 문서를 봐야 압니다. 벤치마크도 대부분 미스트랄이 직접 낸 값이고, 서드파티 수치는 Intelligence Index 38점과 사이버 지수 순위 정도입니다. 컨텍스트 길이도 자료마다 다르게 적혀 있습니다. 결정을 미룰 이유는 충분합니다. 지금 값을 재보는 일과 이달 말에 정하는 일은 따로 해도 됩니다.

## 오늘의 다른 소식 (한 줄)

- **딥시크, 라운드를 두 배로**: 800억 위안(약 120억 달러) 투자 유치가 임박했고 최대 1,000억 위안까지 늘어날 수 있는데, 텐센트와 CATL이 최대 투자자로 2027년 초 상장을 준비합니다. [CNBC](https://www.cnbc.com/2026/10/06/deepseek-funding-round.html)
- **Sierra와 Meta, 개인 에이전트 표준 공개**: 개인 AI 에이전트가 기업과 인증하고 상호작용하는 방식을 정의하는 OAuth 기반 개방 표준이고, 월마트와 쇼피파이, 스트라이프가 창립 파트너로 v0.1 명세를 이달 말에 냅니다. [Sierra](https://sierra.ai/blog/introducing-personal-agent-protocol)
- **구글, 미국 원전 증설의 앵커 고객으로**: 컨스텔레이션과 20년 계약으로 890MW 업레이드를 지원하고 15년짜리 2,700MW 공급 계약도 함께 맺었습니다. [Google](https://blog.google/company-news/why-were-backing-americas-existing-nuclear-plants/)
- **한국, AI 해킹 금융사 침해 조사**: 7개 금융사에서 약 6만 6천 명의 정보가 노출됐고 경찰이 28명 전담팀으로 수사에 들어갔습니다. [Korea JoongAng Daily](https://www.koreajoongangdaily.com/korea/lee-orders-dedication-of-personnel-resources-to-handling-hacking-attacks/12906622)
- **EmbeddingGemma 2 공개**: 텍스트와 코드, 이미지, 영상, 오디오를 한 벡터 공간에 넣는 740M 임베딩 모델로 Apache 2.0이고 온디바이스에서 돕니다. [Google Developers Blog](https://developers.googleblog.com/en/google-ai-edge-with-embeddinggemma-2/)
- **Kandinsky 6.0 Video 오픈소스**: 3B와 29B 확산 모델이 5초 영상과 44kHz 음성을 함께 생성하고 MIT 라이선스로 코드와 가중치가 공개됐습니다. [GitHub](https://github.com/kandinskylab/kandinsky-6)