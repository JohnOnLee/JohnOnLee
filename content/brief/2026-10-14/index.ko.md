---
title: "Gemini 4 Argon, 도입가 11월 30일까지"
date: 2026-10-14
summary: "10월 13일 구글이 Gemini 4 Argon을 전면 배포하기 시작했습니다. Gemini 앱과 검색의 AI 모드, 코딩 도구 Antigravity가 대상입니다. 9월 30일 공개한 뒤 사이버 방어…"
---

## Gemini 4 Argon 전면 배포, 값은 12월 1일에 두 배가 됩니다

10월 13일 구글이 Gemini 4 Argon을 전면 배포하기 시작했습니다. Gemini 앱과 검색의 AI 모드, 코딩 도구 Antigravity가 대상입니다. 9월 30일 공개한 뒤 사이버 방어 담당자에게만 열어 둔 Fairwind 프로그램은 이번에 끝났고, Gemini 3 이후 구글이 내놓는 첫 프런티어 모델이기도 하죠. [Ars Technica](https://arstechnica.com/ai/2026/10/gemini-4-argon-begins-rolling-out-in-gemini-app-and-antigravity-but-only-if-you-pay/) [The Verge](https://www.theverge.com/ai-artificial-intelligence/1009862/google-releases-gemini-4-argon)

값은 두 단계로 나뉩니다. 지금은 입력 100만 토큰당 2달러, 출력 100만 토큰당 10달러이고, 캐시된 입력에는 95% 할인이 붙습니다. 여기까지가 11월 30일까지 적용되는 도입 가격. 12월 1일부터는 입력 4달러, 출력 20달러. 두 배가 됩니다. 출력 한도는 64K에서 100만 토큰으로 늘었습니다. 한 번의 호출이 내놓는 결과물의 크기가 파일 몇 개에서 저장소 하나 규모로 바뀐 셈입니다. [구글](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/)

구글이 앞세우는 성적은 DeepSWE v1.1 77.9%, LVBench 91.7%, Zapier의 AutomationBench 1위 51.3%. 전부 구글이 직접 잰 숫자입니다.

## 2달러는 12월 1일에 끝나고, 코딩 도구는 월 99달러 요금제뿐입니다

인디 빌더가 챙길 건 두 가지입니다. 하나는 2달러와 10달러가 정가가 아니라 12월 1일에 끝나는 도입 가격이라는 점입니다. 지금 단가로 원가를 잡아 두면 연말에 계산이 두 배로 어긋나죠. 다만 인상 뒤에도 Argon은 프런티어 모델 중에서는 싼 편입니다. The Verge는 GPT-6 Astra와 Claude Fable 5 대비 대략 5분의 1 수준으로 봤고, 값이 두 배가 된 뒤에도 토큰당 단가로는 경쟁 모델보다 낮다고 정리했습니다.

다른 하나는 요금제입니다. Gemini 앱과 검색에서 Argon을 쓰는 요금제는 AI Pro(월 20달러)와 AI Ultra(월 99달러부터). Antigravity와 AI Studio에서는 AI Ultra만 되죠. 코딩 에이전트 워크플로에서 Argon을 쓰려면 월 99달러 요금제가 필요하다는 얘기입니다. API로 직접 호출하는 길은 따로 있습니다.

아직 정해지지 않은 것도 있습니다. 구글은 Flash 계열보다 강한 모델이 필요한 사용자에게 Gemini 3.1 Pro를 계속 제공하겠다고 했고, Antigravity의 하위 요금제에 Argon이 언제 열릴지는 밝히지 않았습니다.

## 오늘의 다른 소식 (한 줄)

- **JPMorgan, 외부 AI 에이전트의 계좌 접근 차단**: 제이미 다이먼은 3분기 실적 발표에서 Meta의 Muse 같은 외부 에이전트가 고객 계좌 안에서 대신 행동하도록 두지 않겠다고 밝혔습니다. 잔액 조회는 오픈뱅킹으로 가능하지만 자금 이동은 막힙니다. [CNBC](https://www.cnbc.com/2026/10/13/jpmorgan-ai-agents-account-access.html)
- **Anthropic, Git을 사내 시스템 Scion으로 교체**: 모노레포 하루 병합이 5월 2,500건에서 9월 30,000건으로 늘자 7명이 5개월 만에 Scion을 만들어 전면 이전했고, CPU와 메모리 사용량이 기존 Git 미러 구성의 200분의 1이라고 밝혔습니다. [Anthropic](https://www.anthropic.com/engineering/redesigning-source-control)
- **Reuters: OpenAI와 Anthropic, 외부 평가 보고서에 사전 통제 추구**: 10월 5일까지 두 회사가 외부 평가자가 무엇을 공개할지 상당 부분 통제하려 했고, 평가자 상주 감시와 경쟁사와의 협업 금지안이 논의됐습니다. [The Verge](https://www.theverge.com/ai-artificial-intelligence/1010444/openai-and-anthropic-reportedly-wanted-control-over-what-safety-reviewers-can-publish)
- **Character.AI 파산 신청, 디즈니가 2,000만 달러 입찰**: 10월 12일 델라웨어 파산법원에 Chapter 11을 신청하고 자산과 부채를 각각 5,000만에서 1억 달러로 적었습니다. 디즈니가 일부 IP에 2,000만 달러 스토킹 호스 입찰자로 나섰습니다. [NBC News](https://www.nbcnews.com/tech/tech-news/characterai-files-bankruptcy-sell-assets-disney-20-million-rcna603174)
- **Epic Games, 디즈니 게임을 AI 우선 개발로 전환**: 개발자들에게 코드는 Claude 같은 도구로, 아트도 AI 워크플로로 만들라고 지시하고 사람은 감독 역할로 옮겼습니다. [The Verge](https://www.theverge.com/games/1010097/epic-games-disney-project-ai-coding-art)
- **Decagon, ServiceNow와 인수 협상**: 기업용 AI 상담 에이전트 Decagon이 투자은행을 선임하고 ServiceNow 등과 초기 매각 협의에 들어갔습니다. 올초 기업가치는 45억 달러였습니다. [Business Insider](https://www.businessinsider.com/ai-agent-company-decagon-hired-investment-bank-acquisition-interest-2026-10)
- **Pluto Security, 4,200만 달러로 스텔스 탈출**: 사내 AI 에이전트와 직원이 만든 AI 앱을 감시하는 제품으로 시드 850만 달러와 시리즈 A 3,400만 달러를 합쳐 4,200만 달러를 확보했습니다. [TechCrunch](https://techcrunch.com/2026/10/13/pluto-security-raises-42m-as-ai-gives-enterprise-security-teams-a-new-headache/)
- **Meta, 'Your algorithm'을 페이스북으로 확대**: 인스타그램에 있던 자연어 토픽 조절을 페이스북 피드와 릴스로 넓혔습니다. [Meta](https://about.fb.com/news/2026/10/introducing-your-algorithm-facebook/)