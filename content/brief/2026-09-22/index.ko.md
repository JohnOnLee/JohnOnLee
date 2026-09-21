---
title: "Zhipu ZCode 오픈소스, 앱은 비공개"
date: 2026-09-22
summary: "9월 21일 중국 Zhipu가 코딩 에이전트 ZCode를 오픈소스로 전환하고, 작업공간 무단 업로드 논란을 다룬 외부 감사 결과를 함께 내놨습니다."
---

## Zhipu가 오픈소스로 공개한 ZCode 코드와 내려받아 실행하는 앱은 서로 다릅니다

9월 21일 중국 Zhipu가 코딩 에이전트 ZCode를 오픈소스로 전환하고, 작업공간 무단 업로드 논란을 다룬 외부 감사 결과를 함께 내놨습니다.

논란은 9월 18일 블로거 ferstar가 올린 분석에서 시작했습니다. ZCode 데스크톱 앱이 쓰던 작업공간에 313MB짜리 업로드 대기 데이터가 남아 있었고, 풀어보니 약 90%가 .git 디렉터리였습니다. 목적지는 Zhipu가 운영하는 알리바바 클라우드 OSS 버킷이었고, 데이터는 암호화됐지만 복호화 키는 서버가 쥐고 있었습니다. 설정 화면에서 작업공간과 저장소 업로드 스위치를 꺼도 전송은 멈추지 않았습니다. [ferstar의 분석](https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/)

Zhipu는 9월 18일 사과하고 9월 19일 v3.14.0을 내면서 업로드 설정과 고지 문구를 추가했습니다. 9월 21일에는 저장소를 Apache 2.0으로 공개하고 첫 감사 결과를 발표했습니다. 중국정보통신연구원(CAICT)은 zcode-prod OSS 버킷에 클라우드에 남은 데이터가 없다고 확인했고, NSFOCUS는 버킷과 객체가 삭제됐고 v3.14.0 클라이언트에서 정리가 끝났다고 전했습니다. 저장소 위키 항목과 생성 링크도 삭제됐고, 로컬 저장소 스냅샷이나 파일 유출을 일으키는 경로는 찾지 못했다는 것이 감사 결론입니다. Zhipu는 매달 감사 같은 정기 보안 운영 체계를 만들겠다고 밝혔습니다. 저장소는 GitHub의 zai-org/ZCode에 올라와 있습니다. [36Kr](https://eu.36kr.com/en/p/3992798380833792) · [GitHub](https://github.com/zai-org/ZCode)

## Zhipu가 연 저장소와 내려받는 앱이 다른데 감사는 저장소만 확인했습니다

저장소가 공개되자마자 [BlockBeats](https://en.theblockbeats.news/flash/368173)는 저장소의 코드와 공식 홈페이지에서 내려받는 클라이언트가 완전히 같지 않다고 보도했습니다. 저장소의 NOTICE.md는 공개 소스와 빌드 산출물이 공식 제품의 모든 기능과 프로모션 정책을 포함한다고 보장하지 않는다고 적고 있고, 코드 주석에는 오픈소스 버전이 크레딧 프로모션 혜택을 받지 않는다는 설명도 있습니다. 감사가 들여다본 대상은 저장소에 올라온 코드지만, 대부분의 사용자는 홈페이지에서 내려받은 앱을 실행합니다. ferstar가 9월 21일 덧붙인 검토에서도 저장소는 커밋 두 개짜리 공개였고 PR과 이슈는 닫혀 있었습니다.

감사를 수행한 것은 외부 기관이지만 감사를 요청한 쪽은 회사입니다. 버킷이 비어 있다는 확인은 오늘의 상태를 말해줄 뿐이고, 다음 버전의 클라이언트가 무엇을 보내는지는 알려주지 않습니다. 남는 것은 내 컴퓨터에서 밖으로 나가는 연결과 저장소에 들어 있는 내용입니다. 압축 파일의 대부분이 .git이었다는 사실은 코딩 에이전트에게 저장소 전체가 곧 전송 대상이라는 뜻이기도 합니다.

- 코딩 에이전트를 홈 디렉터리에서 바로 돌리는 대신 별도 계정이나 컨테이너 안에서 실행하면 노출 범위가 프로젝트 하나로 줄어듭니다.
- 세션 하나를 나가는 연결 기록과 함께 돌려보면 어떤 도구가 어디로 무엇을 보내는지 드러납니다.
- 유출된 용량의 대부분이 .git이었던 만큼, 히스토리에 남은 키와 토큰을 먼저 정리하는 순서가 자연스럽습니다.

## 오늘의 다른 소식 (한 줄)

- **Grok 4.7 공개**: xAI가 100만 토큰당 입력 2달러, 출력 6달러로 Grok 4.7을 내놨습니다. Grok API와 Grok Build, Cursor에서 쓸 수 있습니다. Artificial Analysis 지능 지수는 46으로 중위권이고 Claude Fable 5.1과 GPT-6가 53입니다. 에이전트 코딩 벤치마크 Terminal-Bench 4.0에서는 26%로, GPT-6 Astra(60%)와 Claude Fable 5.1(55%)에 크게 뒤졌습니다. [xAI](https://x.ai/news/grok-4-7) · [The Decoder](https://the-decoder.com/xai-launches-grok-4-7-at-bargain-prices-but-benchmarks-reveal-a-wide-gap-to-claude-and-gpt-6/)
- **유엔 AI 패널의 첫 에이전트 브리프**: 유엔이 뒷받침하는 국제 AI 과학패널이 AI 에이전트를 다룬 첫 주제별 브리프에서 현재의 방어 체계가 풀리고 있다고 경고했습니다. 5월부터 7월까지 OpenAI가 시작한 시험에서 AI 에이전트가 허깅페이스를 해킹한 사건이 근거로 인용됐습니다. [UN News](https://news.un.org/en/story/2026/09/1168380)
- **브리티시컬럼비아주, OpenAI와 알트만 상대 소송**: BC주 법무장관 니키 샤르마가 2월 텀블러리지 총기 사건과 관련해 주 정부가 캘리포니아에서 OpenAI와 샘 알트만을 상대로 소송을 낸다고 발표했습니다. 총기 사건 전에 ChatGPT에 올라온 위협을 수사기관에 알리지 않은 것이 소송 근거입니다. [BC주 정부](https://news.gov.bc.ca/releases/2026AG0067-001105) · [CBC](https://www.cbc.ca/news/canada/british-columbia/bc-government-announce-update-openai-legal-action-9.7352395)
- **Cloudflare, Python Workers 정식 출시**: 베타로 1년 넘게 돌던 Python Workers가 정식 버전이 됐습니다. openai, langchain, mcp 같은 라이브러리가 별도 설정 없이 돌아가고 D1, R2, Workers AI 바인딩을 그대로 쓸 수 있습니다. [Cloudflare](https://blog.cloudflare.com/python-workers-ga/)
- **Codex 샌드박스 탈출 취약점**: 읽기 전용 모드에서도 승인 프롬프트 없이 호스트 명령을 실행할 수 있었던 Heapjack과 Overpatch가 공개됐습니다. Codex CLI 0.149.0 이상, 데스크톱 26.818.21641 이상에서 수정됐습니다. [DevOps.com](https://devops.com/codex-sandbox-escapes-show-why-agent-guardrails-cant-live-inside-the-agent/)