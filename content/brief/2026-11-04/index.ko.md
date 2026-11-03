---
title: "LLMJacking, 하루 10만 달러 청구서 (2026-11-04)"
date: 2026-11-04
summary: "공격자가 훔친 클라우드 자격증명으로 남의 LLM을 호출해 피해 조직에 하루 10만 달러가 넘는 청구서를 남겼습니다. Google 위협 인텔리전스 그룹(GTIG)이 2026년 11월…"
---

## LLMJacking 청구서는 쓰지 않던 모델까지 포함합니다

공격자가 훔친 클라우드 자격증명으로 남의 LLM을 호출해 피해 조직에 하루 10만 달러가 넘는 청구서를 남겼습니다. Google 위협 인텔리전스 그룹(GTIG)이 2026년 11월 3일 공개한 분석에 따르면 Mandiant가 대응한 여러 사건에서는 침해 당시 꺼져 있던 Bedrock이나 Gemini API를 공격자가 탈취한 키로 직접 켰고, 청구서는 그렇게 몇 분에서 몇 시간 만에 만들어졌습니다. 혼자 유료 제품을 운영한다면, 제품이 쓰는 모델뿐 아니라 쓰지 않는 모델을 켜고 호출할 권한까지 비용 관리에 넣어야 합니다. [Google Cloud](https://cloud.google.com/blog/topics/threat-intelligence/llmjacking-monetizing-compromised-cloud-models)

공격자들은 훔친 접근권을 되팔기도 하죠. 한 공격자가 Jet Night라는 토큰 중계 서비스에 탈취한 키를 넣었습니다. 8시간도 안 돼 API 호출이 50만 회를 넘었고 피해 조직에 남은 토큰 비용은 거의 100만 달러였습니다.

Jet Night의 무제한 요금제는 최신 모델을 쓸 수 있다고 주장하는 월 약 60달러짜리인데, 정상적인 가격은 월 100~250달러죠. GTIG는 이 서비스가 훔친 키에 기대고 있다고 봅니다. [BleepingComputer](https://www.bleepingcomputer.com/news/security/google-llmjacking-attacks-rack-up-1-million-in-cloud-ai-charges/)

쓰지 않는 API를 꺼 두는 것만으로는 부족하니, GTIG는 지출 상한과 모델별 쿼터를 지금 걸라고 권합니다. 필요하지 않은 LLM 서비스는 접근 권한부터 거부하고 API 키는 모델과 개발·운영 환경별로 나눠야 합니다. 공격자들이 아주 작은 요청으로 키를 시험해 요청량 이상 탐지를 피한 사례가 있으니 그런 호출까지 모니터링에 넣어야 합니다(예: `max_tokens=1`).

## 오늘의 다른 소식 (한 줄)

- **EU 기사 요약 챗봇의 저작권 책임**: EU 사법재판소 법무관은 실시간 기사 수집에서 차단을 우회했는지, 답변이 원문의 표현을 알아볼 수 있게 재현하는지를 침해 판단 기준으로 제시했습니다. 기사 요약 제품의 수집·답변 방식을 점검할 사안으로, 법원을 구속하는 판결은 아닙니다. [Agence Europe](https://agenceurope.eu/en/bulletin/article/13974/18/cjeu-advocate-general-says-chatbots-can-infringe-press-publishers-rights)
- **Claude Sonnet 4.6 워터마크 예외**: Claude 릴리스 노트에 따르면 Sonnet 4.6 요청의 `temperature`, `top_p`, `top_k` 중 하나를 기본값에서 바꾸면 텍스트 워터마크가 없을 수 있으므로, 출력을 발행하는 제품은 AI 생성 표시를 워터마크 존재에만 의존해서는 안 됩니다. [Claude 릴리스 노트](https://platform.claude.com/docs/en/release-notes/overview)