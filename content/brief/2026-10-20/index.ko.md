---
title: "OpenCode 콘솔 API 키 유출, 방어용 모델은 왜 거절했나"
date: 2026-10-20
summary: "10월 17일 OpenCode가 자사 콘솔에서 침해가 있었다고 밝혔습니다. 영향 범위는 콘솔 사용자의 1.4%이고, 외부 AI 제공자 계정을 연결해 둔 사용자들입니다. 콘솔은 API…"
---

## OpenCode 콘솔에서 API 키가 새고, 막는 쪽은 분석을 못 했습니다

10월 17일 OpenCode가 자사 콘솔에서 침해가 있었다고 밝혔습니다. 영향 범위는 콘솔 사용자의 1.4%이고, 외부 AI 제공자 계정을 연결해 둔 사용자들입니다. 콘솔은 API 키를 보관해 두는 호스팅 서비스이고, CLI와 오픈소스 앱은 영향을 받지 않았습니다. 공동창업자 Dax Raad는 "OpenCode Console이지 OpenCode 자체가 아닙니다. 그 키는 저희에게 오지 않습니다"라고 적었습니다. [TechCrunch](https://techcrunch.com/2026/10/19/hackers-hit-ai-coding-tool-opencode-running-up-charges-on-users-ai-accounts/)

그날 밤부터 지출 알림이 돌기 시작했습니다. 한 개발자는 OpenAI, Anthropic, Google에서 알림이 한꺼번에 왔다고 썼고, 계정당 수백 달러, 일부는 1,000달러를 넘긴 사례도 나왔습니다. Anthropic과 Google은 노출된 것으로 보는 키를 차단했고, OpenAI는 OpenCode와 함께 접근을 복구하고 공격에 쓰인 크레딧을 환불했다고 밝혔습니다. OpenCode는 환불을 진행 중이라고 합니다. 피해자에게 간 알림 메일에는 오래된 시스템에 권한 없는 접근이 있었다는 설명과 함께, 워크스페이스에 저장해 둔 제공자 키를 각 제공자 대시보드에서 폐기하고 교체하라는 요청이 담겼습니다. [Cybersecurity News](https://cybersecuritynews.com/opencode-security-breach/)

공격을 막는 일은 더 어려웠습니다. Raad는 48시간 동안 침입 시도가 끊이지 않아 방어용 AI 에이전트를 계속 돌려야 했다고 말했습니다. 그런데 분석에 쓰던 상용 모델들이 악성 코드를 보자 안전 필터에 걸려 작업을 거절하기 시작했습니다. Raad는 그 대목이 답답했다고 적었고, 이후 OpenAI의 Daybreak Blue 프로그램 접근 권한을 받은 뒤 조사가 나아졌다고 합니다. Hugging Face가 7월에 같은 벽을 만나 "대칭성 문제"라고 이름 붙였습니다. 대통령 과학기술자문위원회 공동의장 David Sacks도 가드레일이 역효과를 냈다고 엑스에 썼습니다. [TechCrunch](https://techcrunch.com/2026/10/19/hackers-hit-ai-coding-tool-opencode-running-up-charges-on-users-ai-accounts/)

## 키를 어디에 두는지가 청구서의 크기를 정합니다

이번 침해에서 돈이 나간 경로는 단순합니다. 제공자 계정에 붙어 있던 키가 남의 손에 들어갔고, 그 키로 요청이 돌았고, 청구서는 키 주인에게 왔습니다. 제품을 만드는 쪽이 통제할 수 있는 건 그 앞단입니다. 프로젝트마다 키를 따로 발급하고, 제공자 쪽에 지출 한도를 걸고, 지출 알림을 켜두면 사고가 나도 상한이 생깁니다. 콘솔 같은 제3자 워크스페이스에 키를 두는 경우에는 그 워크스페이스가 내 서비스의 일부가 됩니다.

방어 도구 쪽도 함께 봐야 합니다. 사고가 나면 로그와 악성 코드를 읽어야 하는데, 그 작업을 맡긴 모델이 안전 필터에서 멈추면 손에 남는 게 없습니다. 직접 돌릴 수 있는 오픈 웨이트 모델 하나를 분석용으로 준비해 두면 그때 도움이 됩니다. OpenCode가 GLM-5.3-Flash를 무료로 푼 것과 같은 날 밤에 이 일이 벌어졌습니다.

## "증류 공격"이라는 설명에는 아직 근거가 없습니다

OpenCode는 이번 일을 대규모 증류 공격과 관련된 침해라고 부릅니다. 다만 어떻게 들어왔는지, 얼마나 머물렀는지, 키가 몇 개나 새는지는 밝히지 않았습니다. 단순한 침해를 증류로 부르는 건 과한 해석이라는 지적도 나옵니다. 키가 실제로 모델 출력 수집에 쓰였는지도 확인되지 않았습니다. 회사는 사고가 아직 진행 중이라고 밝혔습니다.

남은 확인 지점은 두 가지입니다. OpenCode가 기술 보고서를 내는지, 그리고 제공자들이 도난당한 키로 발생한 요금을 어떻게 처리하는지입니다. 청구서 부담 주체가 정해지기 전까지는 월 단위 지출 한도를 기준으로 움직이는 편이 낫습니다.

## 오늘의 다른 소식 (한 줄)

- **엔비디아, 에이전트용 오픈 모델 공개**: 1,200억 파라미터 Nemotron 3.5 Super VL과 AI PC·DGX Spark에서 도는 경량 Bolt 모델 두 종을 냈습니다. [TechCrunch](https://techcrunch.com/2026/10/19/nvidia-launches-new-open-models-to-run-agents-in-the-enterprise-and-on-pcs/)
- **AWS, PyTorch 앱을 Trainium으로 옮기는 TorchNeuron 공개**: 설정 한 줄을 바꾸면 아마존 자체 칩에서 돌아간다고 합니다. [TechCrunch](https://techcrunch.com/2026/10/19/amazon-is-taking-its-biggest-shot-at-nvidia-yet-with-new-torchneuron-dev-tool/)
- **애플, 심사 통과 뒤 기능을 켜는 앱 금지**: 숨긴 기능과 AI 생성 유해 콘텐츠 차단 요건을 앱 심사 가이드라인에 넣었습니다. [TechCrunch](https://techcrunch.com/2026/10/19/apple-updates-guidelines-to-ban-nudify-apps-masquerading-as-regular-apps-to-pass-review/)
- **딥시크, 검색·페이지 가져오기 API를 1,000회당 0.75달러에 개방**: 딥시크 모델로 Claude Code와 Codex를 돌릴 때 서버 쪽 검색 호출은 10월 31일까지 무료입니다. [WebProNews](https://www.webpronews.com/deepseek-opens-in-house-search-and-fetch-apis-to-developers/)
- **슈왑과 JP모건, 외부 AI 에이전트의 고객 계좌 접근 차단**: 슈왑은 읽기 전용 MCP 서버를 준비 중이고, 자금 이동은 자사 도구로만 허용합니다. [Agent News Daily](https://agentnewsdaily.com/brief/2026-10-19)
- **텐스토렌트, 15억 달러 투자 유치**: 기업가치 62억 달러로 오픈 웨이트 모델 서빙용 추론 칩을 키웁니다. [TechCrunch](https://techcrunch.com/2026/10/19/tenstorrent-hits-6-2b-valuation-to-scale-open-weight-ai-chips/)
- **AI로 스마트 TV에서 광고와 추적을 걷어내는 흐름**: dumbtv 같은 깃허브 프로젝트와 Claude Code 활용 사례가 퍼졌습니다. [TechCrunch](https://techcrunch.com/2026/10/19/people-are-using-ai-to-make-their-smart-tvs-dumb-again/)