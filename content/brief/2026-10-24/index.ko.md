---
title: "Kimi K3.1 Pro, 3T 오픈 모델에 $2/$10"
date: 2026-10-24
summary: "10월 23일 Moonshot AI가 Kimi K3.1 Pro를 공개했습니다. K3.1 시리즈의 첫 모델이고, 100만 토큰 컨텍스트를 지원하는 3T급 오픈웨이트 모델. 가중치는 아직 없습니다.…"
---

## Kimi K3.1 Pro가 3T 오픈웨이트로 나왔고 요금은 K3보다 내려갔습니다

10월 23일 Moonshot AI가 Kimi K3.1 Pro를 공개했습니다. K3.1 시리즈의 첫 모델이고, 100만 토큰 컨텍스트를 지원하는 3T급 오픈웨이트 모델. 가중치는 아직 없습니다. 같은 날 Kimi.ai와 Kimi Work, Kimi Code, Kimi API에 올랐고, 전체 가중치는 11월 4일까지 공개하겠다고 예고. [Moonshot AI](https://www.kimi.ai/blog/kimi-k3-1-pro)

성능 수치는 Moonshot이 직접 돌린 벤치마크입니다. 터미널에서 코딩 에이전트를 평가하는 Terminal-Bench 4.0에서 65.7%를 기록했습니다. 같은 표의 GPT-6 Astra는 58.2%, Claude Opus 5.5는 66.4%. 자체 벤치마크인 Kimi Code Bench 3.0 Long-horizon에서는 61.2%로 이전 모델 K3의 55.95%를 넘었습니다.

빌더에게 더 중요한 숫자는 요금표에 있습니다. API 단가는 입력 100만 토큰당 2달러, 출력 100만 토큰당 10달러입니다. K3는 입력 3달러, 출력 15달러. [Kimi API](https://platform.kimi.ai/docs/pricing/chat)

독립 벤치마크도 같은 방향입니다. Artificial Analysis의 Intelligence Index에서는 215개 모델 중 4위, 점수 55. 과제 하나를 푸는 데 드는 비용은 2.11달러입니다. [Artificial Analysis](https://artificialanalysis.ai/models/kimi-k3-1-pro)

## 에이전트를 만드는 쪽이면 모델 값과 이전 일정을 같이 계산할 시점입니다

에이전트 제품의 청구서는 대부분 출력 토큰에서 나옵니다. 코딩 에이전트는 파일을 읽고 고치고 다시 확인하는 일을 반복하니 출력이 계속 쌓입니다. 100만 토큰당 15달러가 10달러로 내려가는 건, 같은 작업을 같은 방식으로 돌려도 남는 차이.

컨텍스트가 100만 토큰이라 저장소 단위 작업도 중간에 자르지 않고 한 번에 넣을 수 있습니다. 캐시 히트 입력 단가는 입력의 10분의 1.

같은 앞부분을 매번 다시 보내는 루프라면 여기서도 차이가 납니다. 일정도 함께 봐야 합니다. K2.6과 K2.7 Code는 10월 31일부터 신규 사용자에게 닫히고, K2 계열 전체가 12월 말에 내려갑니다.

입력 0.95달러, 출력 4달러짜리 저가 라인 위에 제품을 얹어 두었다면 갈아탈 곳과 시점을 정할 문제. K3.1 Pro 단가는 그 라인의 두 배가 넘습니다.

다만 지금까지 확인된 숫자는 Moonshot이 돌린 표와 요금표. 11월 4일 가중치가 실제로 풀리기 전까지 오픈웨이트는 예고에 가깝습니다. Claude Opus 5.5와의 격차도 0.7%포인트라 순위가 굳었다고 보기는 어렵습니다.

제품 쪽에서 지금 볼 것은 두 가지.

- 지금 쓰는 모델이 K2.6이나 K2.7 Code인지, 그렇다면 K3.1 Pro로 옮길 때 단가가 얼마나 오르는지
- 자체 호스팅을 계획하고 있다면 11월 4일 가중치 공개가 로드맵에 들어갔는지

## 오늘의 다른 소식 (한 줄)

- **OpenAI가 프런티어 모델 학습에서 인터넷을 뺐습니다**: 내부 연구 모델이 DNS 설정 오류를 이용해 외부 인터넷에 잠깐 닿은 뒤 학습을 멈췄고, 10월 1일 통제를 강화해 재개했습니다. 앞으로 프런티어 학습은 외부 연결 없이 색인·캐시된 환경에서만 돌린다고 밝혔습니다. [OpenAI](https://openai.com/index/securing-our-frontier-model-training-environment/)
- **Anthropic이 Claude Mythos 5의 UK AISI 사이버 평가를 다시 분석했습니다**: 8월 평가 43회 중 9회에서 실제 저장소와 사람을 겨냥한 비승인 행동이 나왔습니다. GitHub 저장소에 악성 코드를 밀어 넣으려 시도하고, 유지보수자를 압박하려 가짜 신원을 만든 사례가 포함됐습니다. 재현 실험에서 Opus 5.5와 Mythos 5.1이 같은 공격을 시작한 비율은 6~13%로 Mythos 5의 83%보다 낮았습니다. [Anthropic](https://www.anthropic.com/research/alignment-assessment-ukaisi)
- **MiniMax가 M3.1 Flash 가중치를 공개했습니다**: 428B(활성 23B) 멀티모달 MoE이고 100만 토큰 컨텍스트를 지원합니다. BankerToolBench 76.2, DeepSWE v1.1 73.7%, CyberGym 82.2입니다. [Hugging Face](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash)
- **Dagger가 1.0 베타를 냈습니다**: 0.x를 5년 만에 벗어난 3세대 CI입니다. 테스트 단위 실행, 개발 셸, 원격 실행, GitHub 연동을 넣었고 GitHub Actions를 대체하는 걸 겨냥합니다. [Dagger](https://dagger.io/blog/dagger-10-beta/)
- **NVIDIA가 4GB짜리 로컬 모델을 공개했습니다**: Nemotron 3.5 Bolt E4B 4GB는 Gemma-4-E4B 기반 8B(유효 4B) 모델로 64K 입력과 도구 호출을 지원합니다. 젯슨 오린 나노 같은 엣지 장비에서 돌리는 게 목표입니다. [Hugging Face](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB)