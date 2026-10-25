---
title: "2015년 CNN, GPT-6 Astra를 피부암 진단에서 이겼습니다"
date: 2026-10-26
summary: "10월 25일 피부과 전문의 Magnus Lynch가 자기 블로그에 실험 하나를 올렸습니다. 조직검사로 확진된 피부 병변 200개를 GPT-6 Astra와 Claude Fable 5.1에 보여주고…"
---

## 20분 다시 학습한 Inception v3 CNN이 GPT-6 Astra와 Claude Fable 5.1을 이겼습니다

10월 25일 피부과 전문의 Magnus Lynch가 자기 블로그에 실험 하나를 올렸습니다. 조직검사로 확진된 피부 병변 200개를 GPT-6 Astra와 Claude Fable 5.1에 보여주고, 같은 200개를 2015년 구글 Inception v3를 다시 학습시킨 CNN에도 보여줬습니다. 첫 번째로 고른 진단이 맞은 비율은 CNN이 200개 중 125개(62%), 두 LLM이 84개와 85개(42%)입니다. 두 번째 선택까지 인정하면 CNN 173개, LLM 134개와 138개. [Lynch Lab](https://lynchlab.net/llm-skin-cancer)

검사에 쓴 병변은 MILK10k 공개 데이터셋에서 무작위로 고른 200개이고 전부 조직검사로 확인된 것입니다. 그냥 두면 안 되는 병변 100개(흑색종 30, 기저세포암 25, 편평세포암 25, 광선각화증 20)와 안심하고 보내도 되는 병변 100개(모반 50, 지루성각화증 50)가 반씩 들어 있습니다. CNN은 일반 사진으로 사전학습된 Inception v3를 ISIC 아카이브 이미지 68,011장으로 H100 한 장에서 다시 학습시킨 모델입니다. 검사에 쓴 200개는 학습에서 뺐고, 학습 시간은 20분 정도. 휴대폰 브라우저에서 WebGPU로 돌아가고 이미지는 밖으로 나가지 않습니다. [CNN 직접 실행](https://lynchlab.net/skin-ai-inception)

두 LLM은 특정 진단으로 답이 몰렸습니다. GPT-6 Astra는 기저세포암이 25개뿐인데 75개를 기저세포암으로 봤고, 그중 14개가 흑색종. Claude Fable 5.1은 광선각화증 20개를 53개로 불렀습니다. CNN이 놓친 흑색종 17개 중 8개는 모반, 6개는 지루성각화증.

한 피부과 의사가 200개로 돌린 실험이고, LLM은 파인튜닝 없이 기본 설정으로 쓴 조건이라 임상 결과로 그대로 옮길 수는 없습니다.

## 라벨이 있는 좁은 문제라면 작은 모델을 먼저 재볼 만합니다

모델을 고르는 순서가 보통 "제일 좋은 LLM부터"인데, 이 실험은 그 순서가 가장 약한 자리를 짚습니다. 답이 정해진 좁은 문제에, 라벨 붙은 예시 몇백 개, 정확도 자체가 제품 가치인 경우. 여기서는 20분 학습한 분류기가 두 프런티어 모델보다 정확했습니다. 호출당 비용도 없고, 브라우저 안에서 돌아가니 이미지가 서버로 나가지도 않지요. 예를 들어 사진에서 불량을 가려내거나, 문의를 정해진 유형으로 나누는 일.

이 실험에서 빌더가 가져갈 숫자는 정확도보다 오답표입니다. 두 LLM에는 각자 좋아하는 답이 있었고, 기저세포암은 200개 중 25개인데 75개를 기저세포암이라고 불렀습니다. 광선각화증은 20개인데 53개를 그렇게 봤습니다. 한쪽으로 쏠리는 오류는 라벨을 더 붙여서 고칠 수 있는 종류. 프런티어 API를 쓴다면 같은 쏠림이 내 데이터에서도 나오는지 확인할 자체 테스트셋 200개가 먼저 필요합니다.

이 실험 하나가 결론을 뒤집지는 않습니다. 좁은 분류기와 대화형 모델은 잘하는 자리가 다르고, 그 경계는 자기 데이터로 재봐야 나옵니다.

## 오늘의 다른 소식 (한 줄)

- **vLLM 0.31.0 미만에서 서비스 거부 결함 5건이 공개됐습니다**: 인증 없이 들어온 요청 하나로 추론 엔진이 모든 사용자에게 멈출 수 있고, 요청 헤더에 주소를 넣어 서버를 공격자 호스트로 접속시키는 SSRF도 포함됩니다. CVSS는 최대 8.8입니다. [GitHub](https://github.com/vllm-project/vllm/security/advisories)
- **OpenAI가 최대 90% 할인으로 Anthropic 고객을 데려오고 있습니다**: The Information 보도를 The Decoder가 정리했습니다. Rippling은 코딩 작업에서 Anthropic 비중이 5월 57%에서 18%로 내려갔고, DataCamp는 비용이 80~90% 줄었다고 밝혔습니다. [The Decoder](https://the-decoder.com/openai-offers-discounts-up-to-90-percent-to-poach-anthropics-biggest-customers/)
- **Kimi K3.1 Pro를 둘러싸고 유료 협찬 미표기 의혹이 제기됐습니다**: 크리에이터에게 유료 파트너십 표기를 빼라고 지시한 스크린샷이 돌았고 진위는 확인되지 않았습니다. Moonshot은 아직 답변하지 않았습니다. [VentureBeat](https://venturebeat.com/technology/moonshots-kimi-k3-1-pro-flirts-with-open-weights-leadership-amid-paid-influencer-scandal-allegations)
- **SpaceX가 GPU 구매용으로 400억 달러를 빌렸습니다**: Musk는 내년 1분기와 2분기에 들어올 GPU를 위한 콜러블 부채라고 밝혔고, 자금줄이 막힌 네오클라우드 200여 곳이 정리 국면에 들어갈 것이라고 말했습니다. [Reuters](https://www.reuters.com/business/media-telecom/musk-says-spacex-raised-40-billion-debt-gpus-2026-10-25/)