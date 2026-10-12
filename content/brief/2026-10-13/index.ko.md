---
title: "메타 Muse Wonder, 윗급은 API에 없다"
date: 2026-10-13
summary: "10월 12일 메타 슈퍼인텔리전스랩이 Muse Wonder와 Muse Wonder Full을 공개했습니다. 메타가 프런티어 모델을 직접 낸 건 이번이 처음입니다. API로 열린 건…"
---

## 메타 첫 프런티어 모델 Muse Wonder, 가장 센 버전은 API 밖에 있습니다

10월 12일 메타 슈퍼인텔리전스랩이 Muse Wonder와 Muse Wonder Full을 공개했습니다. 메타가 프런티어 모델을 직접 낸 건 이번이 처음입니다. API로 열린 건 Wonder입니다. 100만 토큰 컨텍스트에 입력 100만 토큰당 4달러, 출력 20달러. 텍스트와 이미지, 음성, 영상을 함께 받습니다. [Meta](https://about.fb.com/news/2026/10/introducing-muse-wonder-models/) [TechCrunch](https://techcrunch.com/2026/10/12/meta-releases-its-first-frontier-model-muse-wonder/)

윗급은 토큰 단위로 팔지 않습니다. 상위 버전인 Full은 메타 코딩 도구 Muse Code 구독자에게만 열리고 API에는 아예 올라가지 않습니다. 구독료는 Muse Code가 월 50달러와 200달러, 앱이 월 20달러와 100달러. 이름은 같은 계열인데 사는 방식이 다릅니다. [CNBC](https://www.cnbc.com/2026/10/12/meta-muse-wonder-ai-model-agent.html)

점수 차이도 그대로 남습니다. Artificial Analysis 지능 지수로는 Wonder가 52점, Full이 56점입니다. 메타 자체 모델카드는 Fable 5.1이나 GPT-6 Astra와 비슷한 점수를 주장합니다. 그건 메타가 낸 숫자거든요. [Artificial Analysis](https://artificialanalysis.ai/models/muse-wonder)

## 제품에 붙일 수 있는 건 API로 열린 Wonder뿐입니다

인디 빌더에게 달라진 건 결제 경로입니다. "제일 좋은 모델을 붙인다"는 계획에 구멍이 하나 생겼죠. 지능 지수 4위에 오른 Full은 내 제품이 호출할 수 있는 대상이 아니니, 최상위 모델을 결제 한 번으로 쓴다는 전제는 이제 모델마다 따져봐야 합니다. 성능이 요금제를 따라 갈리면, 서비스가 어디까지 좋아질 수 있는지는 내 코드가 아니라 그쪽 요금표가 정하는 셈이죠.

API로 열린 쪽에서 확인할 것은 메모리입니다. 메타는 Active Memory로 대화가 바뀌어도 맥락을 이어간다고 설명합니다. 대화 기록을 직접 저장하고 요약해 다시 넣는 코드를 줄일 수 있다는 얘기죠. 아직은 메타 설명뿐입니다. 이미 쓰는 모델과 같은 과제 몇 개를 붙여서 내 요약 파이프라인이 실제로 짧아지는지 한 번 재보면 확인됩니다.

## 오늘의 다른 소식 (한 줄)

- **Microsoft Maia 300 공개**: 3세대 자체 AI 가속기를 내놓고 2027년부터 멀티기가와트 규모로 배치해 추론의 주력으로 쓰겠다고 밝혔습니다. [Microsoft](https://blogs.microsoft.com/blog/2026/10/12/microsoft-to-expand-azure-maia-system-to-multi-gigawatt-deployments/)
- **NVIDIA, Vera Rubin 랙 설계를 OCP에 기부**: MGX 1.2 사양으로 랙과 컴퓨트 트레이 설계를 열었고 250kW 랙과 액체냉각을 담았습니다. [NVIDIA](https://blogs.nvidia.com/blog/ocp-global-summit-vera-rubin-scale-ai-factories/)
- **Anthropic, IoT 자기복제 경고**: Frontier Red Team은 소형 오픈웨이트 모델이 스마트 오븐이나 안드로이드 TV 박스에서 스스로 복제할 단계에 가까워졌다고 밝혔습니다. [Anthropic](https://www.anthropic.com/research/self-replicating-ai)
- **토르발즈, Claude Code로 만든 커널 브랜치 공개**: 페이지 캐시 패치의 코드와 테스트, 커버레터 초안을 AI가 썼다고 밝혔고 노트북 벤치마크에서 작은 읽기 처리량이 세 배로 늘었습니다. [Hardware Busters](https://hwbusters.com/news/linus-torvalds-uses-claude-code-to-rework-the-linux-page-cache-tripling-small-read-throughput/)
- **Ondas와 Palantir, Regna AI 설립**: 고객이 통제하는 환경에서 돌아가는 파인튜닝 모델을 방산과 엣지 하드웨어부터 공급합니다. [Ondas](https://ir.ondas.com/press-releases/detail/334/ondas-announces-regna-ai-powered-by-palantir-to-advance)
- **HCLTech와 Anthropic, 총판 계약**: Anthropic 전담 조직을 만들고 Claude와 Claude Code를 자사 엔터프라이즈 제품에 넣습니다. [HCLTech](https://www.hcltech.com/press-releases/hcltech-and-anthropic-sign-global-premier-partnership-scale-governed-agentic-ai)
- **르쿤, AI 통제 불능론은 공상과학**: 서울 브리핑에서 LLM 기반 안전 접근의 한계를 짚고 월드모델을 대안으로 제시했습니다. [Digital Today](https://www.digitaltoday.co.kr/en/view/113258/lecun-says-ai-running-out-of-control-is-science-fiction-world-models-could-be-alternative)