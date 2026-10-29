---
title: "Mistral Large 4, 작업당 비용"
date: 2026-10-30
summary: "Mistral이 10월 29일 1조 파라미터 모델 Mistral Large 4의 오픈 웨이트를 공개했습니다."
---

## Mistral Large 4는 자기 저장소의 작업당 비용으로 골라야 합니다

Mistral이 10월 29일 1조 파라미터 모델 Mistral Large 4의 오픈 웨이트를 공개했습니다.

10월 6일 공개 프리뷰로 나왔던 모델에 강화학습을 3주 더 진행하고 가중치를 공개한 것이고요. 인디 개발자가 모델을 고를 때는 공개 규모보다 코딩 에이전트가 작업 하나를 끝내는 데 쓰는 토큰과 단가를 먼저 봐야 합니다. [Mistral](https://mistral.ai/news/mistral-large-4-oss/)

Mistral에 따르면 Artificial Analysis Coding Agent Index에서 48%를 기록해 GLM-5.3과 사실상 동률이었지만, 작업당 평균 토큰은 47% 적게 썼습니다. Terminal-Bench 4.0에서는 프리뷰보다 13%포인트 오른 41%를 기록했고, 출력 토큰은 30% 줄었습니다. 자기 제품을 만드는 개발자라면 비슷한 코딩 성능에서 작업을 마칠 때까지 얼마나 적은 토큰을 쓰는지 비교해야 하는데, 파라미터 수만 보고서는 알 수 없죠.

다만 모두 Mistral이 보고한 결과로, 발표문에서는 독립 평가를 인용하지 않았습니다. 여기서 기준이 하나 필요합니다. 병합할 수 있는 변경인가입니다. 저장소 관리자가 에이전트의 변경을 병합할지를 평가하는 Cognition의 비공개 벤치마크 FrontierCode 2.0에서는 19.7%로 선두였습니다. 자기 저장소에서도 토큰을 얼마나 적게 썼는지와 함께 받아들여 병합할 수 있는 변경을 만들었는지까지 확인해야 합니다.

Mistral API의 새 단가는 100만 토큰당 입력 0.70달러, 캐시된 입력 0.07달러, 출력 2.10달러입니다. 작업 비용을 비교하려면 입력과 출력을 나눠 기록하고 캐시된 입력에는 해당 단가를 적용해야 하고요. 작업당 토큰을 47% 덜 썼다는 벤치마크만으로 자기 제품 개발비도 47% 줄어든다고 계산할 수는 없습니다. 실제로 쓴 토큰에 단가를 적용해 필요한 변경을 완성하는 데 얼마가 들었는지 재야 합니다.

오픈 웨이트를 직접 운영할 때도 비용을 따져야 하는데, 1조 파라미터 모델을 자체 호스팅하려면 여러 GPU로 구성한 클러스터가 필요해서 작은 팀 대부분에는 호스팅된 엔드포인트가 현실적인 선택입니다. Mistral API나 OpenRouter에서 먼저 자기 작업을 돌려보면 모델 선택에 필요한 비용을 직접 비교할 수 있죠. 가중치를 내려받을 수 있다는 사실만으로 자체 운영이 더 저렴하다고 판단해서는 안 됩니다.

현재 쓰는 모델과 Mistral Large 4에 자기 저장소의 같은 작업을 맡기고 코딩 에이전트는 그대로 두면, 병합 가능한 변경을 만들 때까지 쓴 토큰과 비용을 작업별로 비교할 수 있습니다. 실패한 시도에 쓴 비용도 포함해야 합니다. Mistral Large 4에서는 단순한 작업에 Low, 일상 작업에 Medium, 가장 어려운 작업에 기본값인 High를 쓸 수 있으니, 비교할 때 어떤 추론 모드를 썼는지도 함께 남겨야 하고요. 필요한 품질로 작업을 끝낸 비용으로 고르면 됩니다.

## 오늘의 다른 소식 (한 줄)

- **Gemini 파일 편집**: 모든 Gemini 앱 사용자가 채팅에서 파일을 만들고 미리보거나 편집할 수 있게 됐고, PDF 편집은 웹과 모바일에서, 나머지 파일 작업은 웹에서 지원합니다. [Google](https://blog.google/innovation-and-ai/products/gemini-app/edit-files-directly/)
- **OpenAI 사용량 확대**: Pro 100·200·500과 Business Premium에 포함된 Work·Codex 사용량이 두 배로 늘었고, 9월 29일 이메일로 예고했던 Pro 200 사용량 축소도 취소됐습니다. [OpenAI](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- **Thrive의 ADT 인수 합의**: Thrive Holdings가 ADT를 153억 달러에 인수하기로 합의했으며, 가정용 보안에 AI를 도입할 계획입니다. [ADT](https://newsroom.adt.com/financial/adt-to-be-acquired-by-thrive-holdings-in-15-3-billion-transaction)