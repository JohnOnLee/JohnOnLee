---
title: "AI PM과 솔루션 아키텍트: 공고에 적힌 숫자로 본 시장"
date: 2026-09-07
tags: ["ai-careers"]
summary: "AI PM과 솔루션 아키텍트 숫자는 떠도는 것부터 근거가 약합니다. 게재 급여로 다시 재고, 만드는 쪽과 판매하는 쪽이 어떻게 갈리는지, 호주 밴드까지 봤습니다."
---

이 직군을 알아보기 시작하면 이런 숫자들을 보게 됩니다. "시니어 AI PM 총보상 32만~52만 달러." "AI PM 공고가 2년 만에 3배." 따로따로 퍼진 숫자인데, 출처를 따라가면 둘 다 근거가 약합니다. 앞의 것은 [한 리크루팅 회사 급여 가이드](https://www.kore1.com/ai-product-manager-salary-guide/)에 있는 숫자인데 표본도 방법도 안 적혀 있고, 뒤의 것은 [콘텐츠 사이트 글](https://www.paraform.com/blog/what-is-ai-product-manager)에 출처 없이 나옵니다.

실제 숫자는 이렇습니다. [미국 공고에 게재된 급여를 12,397건 모은 자료](https://axialsearch.com/insights/ai-product-management-jobs)(Axial Search, 2026년 1~6월)의 중앙값이 19만 4천 달러로, 앞의 32만~52만과는 차이가 큽니다. 다만 단위가 다릅니다. 32만~52만은 지분까지 합친 총보상이고, 19만 4천은 공고에 적힌 급여 밴드의 중앙값입니다. 총보상과 게재 급여를 섞어 비교하면 차이의 상당 부분은 지분을 세느냐 마느냐일 뿐입니다. 게재 급여끼리 비교해도 AI 랩은 확실히 다르긴 합니다. [Anthropic의 PM 공고 하나](https://job-boards.greenhouse.io/anthropic/jobs/5247640008)는 30만 5천~46만 달러를 적어놨습니다. 시장 게재 중앙값의 1.6배인데, 랩 공고 한 건의 밴드일 뿐 "랩의 하한선" 같은 통계는 아닙니다.

이 시리즈가 모든 숫자에 출처와 단위를 붙이는 이유를 이 직군이 제일 잘 보여줍니다. 이제 시장을 봅시다.

## 같은 이름인데 방향이 둘입니다

실제 공고 두 개를 나란히 놓으면 보입니다.

**만드는 쪽(AI PM)**: [Anthropic, PM(Claude Code 모델 성능)](https://job-boards.greenhouse.io/anthropic/jobs/5247640008), 30만 5천~46만 달러. 자기 제품의 평가(eval) 로드맵을 책임지고 모델 출시를 계획합니다. 자격 요건에 "에이전트 평가 스위트(SWE-bench류)를 직접 만들어본 경험"이 적혀 있습니다. [애플리케이션 편](/blog/ai-application-evals/)의 그 eval이 여기서는 채용 조건입니다.

**판매하는 쪽(솔루션 아키텍트)**: [Anthropic, Applied AI Architect](https://job-boards.greenhouse.io/anthropic/jobs/5409008008), 24만~31만 5천 달러. 영업·제품·엔지니어링 팀과 붙어서 고객사의 기술 검토부터 배포까지 자문합니다. 자격 요건은 Field CTO·솔루션 아키텍트·세일즈 엔지니어·PM 같은 역할 8년 이상, 직접 만들어본 경험 포함.

같은 회사 같은 기능인데 방향이 다릅니다. 만드는 쪽은 자기 제품의 지표를 책임지고, 판매하는 쪽은 고객사의 배포를 책임집니다. 다만 둘 사이를 오가기 어렵지는 않습니다. 위 아키텍트 공고가 자격 요건에 PM 경력을 넣어놨듯이, 한쪽 경력으로 다른 쪽에 지원할 수 있는 시장입니다.

## 판매하는 쪽은 덜 알려져 있습니다

구직 콘텐츠는 대부분 PM 쪽만 다룹니다. 보상은 두 갈래로 봐야 합니다. 같은 랩 안에서는 만드는 쪽이 더 받습니다. 위 두 공고만 봐도 PM은 30만 5천 달러부터, 아키텍트는 24만 달러부터 시작합니다. 판매하는 쪽의 몸값이 오른 곳은 랩 밖입니다. AI 벤더가 솔루션 아키텍트에게 주는 돈이 예전 엔터프라이즈 소프트웨어 회사의 SA와는 다른 급이 됐거든요. levels.fyi에서 보면 [OpenAI 솔루션 아키텍트의 중앙값 총보상이 41만 8천 달러](https://www.levels.fyi/companies/openai/salaries/solution-architect/locations/united-states), [Databricks가 35만 3천 달러](https://www.levels.fyi/companies/databricks/salaries/solution-architect/locations/united-states)입니다(2026년 9월 3일 조회). 다만 이 숫자를 볼 때 조심할 건 자기 보고라는 점보다 표본입니다. levels.fyi는 오퍼레터로 검증은 하지만 표본 수를 공개하지 않습니다. 이런 틈새 직무라면 중앙값이 몇 건짜리일 수 있다는 얘기입니다.

급성장 직함 Forward Deployed Engineer도 이쪽입니다. Salesforce는 Agentforce FDE를 미국에서 상시로 뽑고 있고, 호주 공고도 오르내립니다. 다만 FDE의 게재 밴드는 회사와 레벨에 따라 크게 달라서([Salesforce의 미국 전 레벨 공고 하나](https://www.salesforce.com/company/careers/jobs/JR349466/forward-deployed-engineer-all-levels/)가 기본급만 8만 9천~28만 8천 달러, 대도시는 최고 31만 7천), 직함이 아니라 회사와 레벨을 봐야 합니다. 이쪽이 원하는 건 만들 줄 알면서 고객 앞에서 설명도 할 줄 아는 사람입니다. 흔치 않은 조합이라 몸값이 붙습니다.

## 직함 경고

[LinkedIn의 2026년 미국 급성장 직업 25개](https://www.linkedin.com/pulse/linkedin-jobs-rise-2026-25-fastest-growing-roles-us-linkedin-news-dlb1c)에 PM도 솔루션 아키텍트도 없습니다. 1위는 AI 엔지니어, 2위는 AI 컨설턴트입니다. 성장률 순위라 원래 사람이 많은 직군은 순위에 오르기 어렵다는 점은 감안해야 하지만, 새 수요가 어디로 몰리는지는 보여줍니다. 전례도 있습니다. [Airbnb](https://blog.logrocket.com/product-management/airbnb-eliminated-traditional-pm-role-now-what/)는 2023년에 전통적 PM 직함을 없애고 PM과 제품 마케팅을 한 직군으로 합친 적이 있는 회사입니다. 모든 제품이 AI 제품이 되면 "AI PM"이라는 수식어는 사라질 수 있습니다.

[첫 편](/blog/ai-operator-map/)에서 한 얘기가 여기서도 그대로 적용됩니다. 준비할 건 직함이 아니라 그 자리가 하는 일입니다. 제품의 가치를 숫자로 증명하는 능력과 고객사에 배포를 성공시키는 능력은 직함이 뭐로 바뀌든 남습니다.

## 호주 숫자

호주에서 솔루션 아키텍트 정규직은 시드니 기준 16만 5천~22만 호주달러 선입니다([Morgan McKinley](https://www.morganmckinley.com/au/salary-guide/data/solutions-architect/sydney) 16만 5천~22만, [Robert Half](https://www.roberthalf.com/au/en/job-details/solutions-architect/sydney) 18만~21만 3천, 2026년 가이드). 계약직은 주류 집계에서 LLM 아키텍트·에이전트 아키텍트 같은 자리가 하루 1,430~1,490 호주달러입니다([Talent International](https://www.talentinternational.com/blog/top-tech-contractor-day-rates-australia/), 2026년 3월). 하루 2,000~3,500달러나 "AI 프리미엄 20~35%" 같은 숫자는 [전문 리크루터 한 곳](https://www.aitalentondemand.com.au/article/ai-solutions-architect-salary-australia-2026)에서만 나오니 기대치로 잡지 마세요. 주류 가이드에서 AI 프리미엄은 밴드 상단에서나 보이는 정도입니다.

## 근거는 방향마다 다릅니다

- 만드는 쪽: 출시한 것에서 지표가 얼마나 움직였는지입니다. 전환율, 비용, 리텐션. 그리고 eval 로드맵을 굴려본 기록.
- 판매하는 쪽: 고객사에 배포한 것이 프로덕션에 남아 있다는 사실입니다. 데모 말고, 석 달 뒤에도 돌아가는 배포.

위의 Anthropic 공고 두 개는 시니어 자리입니다. 주니어라면 판매하는 쪽부터 들어가게 됩니다. 벤더의 솔루션 엔지니어와 FDE 하단 밴드로 먼저 들어가는 경로고, 사이드 프로젝트는 거기서 통하는 근거입니다. 사이드 프로젝트가 있다면 제품처럼 다루는 게 시작입니다. 쓰는 사람 열 명을 만들고 그들의 사용 지표를 재면 만드는 쪽 근거가 쌓입니다. 그걸 다른 팀이나 다른 회사에 배포해 주고 유지되게 만들면 판매하는 쪽 근거가 됩니다. 직함은 그다음 문제입니다.

이걸로 다섯 기능을 다 돌았습니다. 기능마다 무엇을 측정하고 무엇을 보여줘야 하는지도 다 적었습니다. 다음부터는 그 근거를 실제로 만드는 가이드로 넘어갑니다.
