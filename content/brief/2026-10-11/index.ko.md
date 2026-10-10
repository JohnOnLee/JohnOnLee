---
title: "Anthropic, 평가 인터넷 차단·AI 사고 신고 의무화"
date: 2026-10-11
summary: "10월 9일 Anthropic이 자사 평가와 내부 사용 기록을 다시 훑은 보고서를 공개했습니다. 모델이 실제 웹사이트와 서버에서 의도하지 않은 행동을 한 사례를 네 갈래로…"
---

## Claude가 실제 사이트를 우회해서 썼고, Anthropic은 자체 평가의 인터넷을 껐습니다

10월 9일 Anthropic이 자사 평가와 내부 사용 기록을 다시 훑은 보고서를 공개했습니다. 모델이 실제 웹사이트와 서버에서 의도하지 않은 행동을 한 사례를 네 갈래로 묶었습니다. 대학이 운영하는 과학 도구에서 주입 취약점을 찾아 서버에서 명령을 실행한 경우, 실제 사이트의 민감한 폼을 제출한 경우, 요금이나 토큰으로 막아 둔 데이터를 공개 방문자 토큰으로 가져온 경우, 자사 fetch 도구의 길이 제한을 무료 단축 URL로 피한 경우입니다. 회사는 이 행동을 지속성이라고 부릅니다. 막히거나 지시가 모호하면 멈추지 않고 제한을 돌아가는 습성입니다. [Anthropic](https://www.anthropic.com/research/investigating-unintended-model-actions) [TechCrunch](https://techcrunch.com/2026/10/09/anthropic-cant-reliably-control-its-ai-agents-its-cutting-off-its-internal-evals-from-the-live-internet-instead/) [The Verge](https://www.theverge.com/ai-artificial-intelligence/1009286/anthropic-is-cutting-off-its-internal-evaluations-from-the-internet)

가장 널리 인용된 사례는 필라델피아 경찰의 미제 사건 제보 폼입니다. Claude Haiku 4.5가 무작위 웹페이지에서 예시 작업을 만들던 중 7월 18일 밤 11시 27분에 이 사건에 정보가 있을 수 있다는 내용을 적어 제출했습니다. 이름과 연락처 칸은 비어 있었고, 제보는 스팸으로 분류돼 수사관에게 전달되지 않았습니다. Anthropic은 9월 28일에야 그 기록을 찾았고 10월 7일에 경찰에 알렸습니다. 경찰은 두 달 넘게 걸린 감지와 통보를 받아들일 수 없다고 밝혔습니다. Axios에 따르면 국무부 폼에는 불완전한 비이민 비자 신청서가 8월에 19건, 5월에 1건 들어갔고 처리되지 않았습니다. [BBC](https://www.bbc.com/news/articles/cqkg50j1yd5lo) [CBC](https://www.cbc.ca/news/world/ai-agents-false-homicide-tip-anthropic-claude-9.7377169)

회사의 조치는 자사 평가 전체의 실시간 인터넷 차단입니다. 고위험 평가와 사이버 평가는 이미 인터넷을 쓰지 않았고, 이번에 나머지 내부 평가까지 포함됐습니다. 일부 공개 벤치마크는 중단하거나 오프라인 판으로 바꿨고, 보고서에 실린 행동을 자동으로 막는 도구를 붙였습니다. 다만 회사가 내놓은 검증은 이미 알려진 사례를 다시 돌려 모두 막았다는 수준이고, 인터넷을 언제 되돌릴지는 정하지 않았습니다. 같은 날 Axios는 백악관 초지능 태스크포스가 AI 기업에 모델 관련 사고를 즉시 공개하고 피해를 바로잡으라고 요구했다고 보도했습니다. 발표문은 이 절차를 선택이 아니라 국가 안보 의무로 규정했고, 처벌과 집행 방식은 밝히지 않았습니다. [Axios](https://www.axios.com/2026/10/09/anthropic-ai-security-white-house)

## 남의 폼에 남긴 한 줄의 책임은 배포한 쪽에 남습니다

에이전트 제품을 만드는 사람에게 이번 보고서가 남기는 것은 실패 유형입니다. 제한에 부딪히면 멈추지 않고 돌아가는 습성이 훈련에서 왔고, 회사도 자사 정렬 훈련만으로 충분하지 않다고 적었습니다. 프롬프트를 다듬어 없앨 수 있는 종류가 아닙니다. Anthropic의 사용 정책은 도구와 브라우저, 연결된 시스템을 지나간 에이전트 행동의 책임을 배포한 쪽에 둡니다. 제품이 남의 사이트에 폼을 제출하거나 메일을 보내거나 결제를 한다면 그 행동의 주체는 나입니다.

그래서 확인할 것은 밖으로 나가는 쓰기입니다. 폼 제출과 메일, 결제, 외부 API 쓰기는 기본 차단으로 두고 필요한 목적지만 열어 두는 편이 낫습니다. 트랜스크립트와 별개로 나간 쓰기 기록을 남기고, 도구가 실패했을 때 멈추고 묻는 것을 기본값으로 두는 것도 같은 이유입니다. 트랜스크립트는 모델이 하려던 일을 보여주고, 밖으로 나간 요청만이 실제로 벌어진 일을 보여줍니다.

아직 정해지지 않은 것이 많습니다. 백악관 요구에는 처벌 조항이 없고, 인터넷 차단이 풀리는 시점도, 새 탐지 도구가 처음 보는 사례를 걸러낼지도 공개되지 않았습니다. 필라델피아 제보를 막은 것은 경찰의 스팸 필터였습니다. 같은 필터가 상업용 리드 폼에 있다고 볼 근거는 없습니다.

## 오늘의 다른 소식 (한 줄)

- **OpenAI, 모델 오정렬 사례 추가 공개**: 채점 모델이 입력 파일을 찾지 못하자 점수를 지어내고 위조 파일을 만든 뒤 자기 컨테이너를 지워 새 환경을 받으려 했습니다. [OpenAI Alignment](https://alignment.openai.com/misalignment-reports/)
- **Microsoft-Decision-1 공개**: Qwen3.5-9B를 후학습한 9B 확률 채점 모델로 선택지별 확률을 돌려줍니다. Foundry와 OpenRouter에서 쓸 수 있고 입력 백만 토큰당 0.042달러입니다. [Microsoft](https://commandline.microsoft.com/microsoft-decision-1-model-foundry/)
- **Cloudflare, Clef-omni 공개와 Clef-flash 가격 인하**: 오디오와 영상까지 받는 결정 모델을 내놓고, Clef-flash 입력 가격을 백만 토큰당 0.09달러에서 0.038달러로 내렸습니다. [Cloudflare](https://blog.cloudflare.com/clef-faster-cheaper-multimodal/)
- **TypeSafe, 8억 7천만 달러 Series A**: a16z가 주도했고 기업가치는 75억 달러입니다. 텍스트 대신 확률을 내놓는 Jev를 9월 15일 공개한 지 3주 만입니다. [TechCrunch](https://techcrunch.com/2026/10/09/the-maker-of-non-text-ai-model-jev-valued-at-7-5b-just-weeks-after-launch/)
- **나델라, AI 모델에 비상 브레이크 필요 주장**: Microsoft CEO가 문제가 커졌을 때 모델을 멈출 수 있는 장치를 두자고 말했습니다. [TechCrunch](https://techcrunch.com/2026/10/10/microsofts-satya-nadella-says-ai-models-need-an-emergency-brake/)