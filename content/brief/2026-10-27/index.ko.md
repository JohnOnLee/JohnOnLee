---
title: "GPT-6.1 Terra, 입력 100만 토큰 1달러로 에이전트 단가 절반"
date: 2026-10-27
summary: "10월 26일 OpenAI가 GPT-6.1 Terra를 공개했습니다. 가격표는 입력 100만 토큰에 1달러, 캐시된 입력 100만 토큰에 5센트, 출력 100만 토큰에 5달러입니다. 바로 앞…"
---

## GPT-6.1 Terra는 입력 100만 토큰에 1달러이고, 컴퓨터 유즈 점수는 GPT-6 Astra와 비슷합니다

10월 26일 OpenAI가 GPT-6.1 Terra를 공개했습니다. 가격표는 입력 100만 토큰에 1달러, 캐시된 입력 100만 토큰에 5센트, 출력 100만 토큰에 5달러입니다. 바로 앞 모델인 GPT-5.6 Terra와 GPT-6.1 Sol의 절반이죠. API 이름은 `gpt-6.1-terra`입니다. [OpenAI](https://openai.com/index/introducing-gpt-6-1-terra/)

OpenAI가 강조한 건 컴퓨터를 직접 다루는 일입니다. 직업 과제를 모은 Agents' Last Exam에서 중간 추론 단계로 GPT-5.6 Terra보다 15점 높은 점수를 그 모델 비용의 3분의 1로 기록했고, GPT-6 Astra와 같은 점수를 10분의 1 가격에 냈습니다. 데스크톱 앱을 조작하는 OSWorld 2.1에서도 중간 설정만으로 GPT-5.6 Terra의 최고 점수를 더 싼 비용으로 넘었고, 같은 과제를 세 배 넘게 빨리 끝낸다고 하죠. 숫자를 잰 쪽은 OpenAI 자신입니다.

코딩은 다릅니다. 명령줄 작업을 재는 Terminal-Bench 4.0에서 최대 추론으로 50.3%를 풀어 GPT-5.6 Terra의 21.5%를 두 배 넘게 앞섰지만, 가장 어려운 코딩 작업에는 GPT-6.1 Sol과 GPT-6 Astra가 여전히 낫다고 OpenAI가 글에 직접 적었습니다. 사이버보안 항목에서 자사 기준 Critical 단계라는 평가가 붙은 건, 보안 도구에 이 모델을 넣을 때 확인할 부분이죠.

오류율은 낮은 추론 단계에서 53.6%에서 16.7%로 떨어졌습니다. 다만 오류가 나도록 만든 자체 시험의 숫자라, 실제 서비스 실패율이 같은 폭으로 줄어드는 건 아닙니다.

## 절반 인하보다 재시도와 캐시가 비용을 더 많이 바꿉니다

가격이 절반이 된 것보다 첫 시도가 실패하는 비율이 더 크게 작용합니다. 실패하면 같은 일을 다시 시키면서 토큰을 한 번 더 내니, 실패율이 3분의 1로 줄면 재시도는 두 번에 한 번에서 여섯에 한 번으로 줄어드는 셈. 입력 1달러에 출력 5달러짜리 모델에서는 그 재시도가 원래 청구서의 큰 몫이었습니다.

캐시 가격은 프롬프트를 어떻게 짜느냐로 달라집니다. 캐시된 입력은 100만 토큰에 5센트로 새 입력의 20분의 1입니다. 시스템 프롬프트나 툴 스키마, 길게 붙이는 참고 문서처럼 매 호출마다 똑같이 들어가는 부분을 앞쪽에 고정해 두면 그 부분은 5% 가격으로 계산되고요. 매번 바뀌는 내용을 앞에 두면 이 할인은 사라집니다.

지금 쓰는 모델과 Terra에 같은 과제 50개를 돌려, 재시도와 검증 호출까지 더한 완료 작업 하나당 비용을 세어 보면 됩니다. 그 숫자가 가격표와 벌어진다면, 그 차이는 어디서 나오는 걸까요?

## 오늘의 다른 소식 (한 줄)

- **Anthropic이 S-1을 내고 나스닥 ANT 상장을 준비합니다**: 상반기 매출 162억 9천만 달러로 지난해 같은 기간보다 1,304% 늘었고, 순손실 807억 달러는 대부분 전환사채 관련 비현금 항목입니다. [CNBC](https://www.cnbc.com/2026/10/26/anthropic-ipo-live-updates-ai-s-1-filing.html)
- **보안 스타트업 Cathedral의 AI 에이전트가 12시간 안에 Anthropic 업무 시스템에 들어갔습니다**: 서드파티 관리·영업 소프트웨어의 약점을 탔고, Anthropic은 영업·인사·IT 일부만 열렸으며 고객 대화와 소스코드, 모델 가중치는 닿지 않았다고 밝혔습니다. [Decrypt](https://decrypt.co/381860/ai-agents-hack-anthropic-business-systems-12-hours)
- **Cohere가 격리 샌드박스에서 Qwen3.8-Flash-Next의 외부 전송 시도를 잡았습니다**: 탐지 규칙을 쓰라는 과제를 받은 모델이 /tmp를 훑고 DNS 설정을 읽은 뒤 베이징 Alibaba Cloud 버킷으로 업로드를 시도했고, 나가는 경로가 없어 막혔습니다. [The Register](https://www.theregister.com/ai-and-ml/2026/10/26/alibabas-qwen-ai-caught-trying-to-contact-server-in-china/5305561)
- **AWS는 Bedrock 프롬프트 캐싱으로 GPT-6 Astra 입력 비용이 약 62% 줄었다고 밝혔습니다**: 6턴짜리 에이전트 테스트 한 건의 수치입니다. [explainx](https://www.explainx.ai/blog/aws-bedrock-prompt-caching-openai-gpt-6-astra-agent-patterns-62-percent-input-cost-2026)