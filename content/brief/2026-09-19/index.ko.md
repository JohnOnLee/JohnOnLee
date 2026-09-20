---
title: "Plugin4Shell: 플러그인 핀은 검증이 아니다"
date: 2026-09-19
summary: "Plugin4Shell은 에이전트 플러그인 핀이 실제 체크아웃 결과를 검증하지 않은 사고다. 인디 개발자에게 플러그인도 공급망이 됐다."
---

## Plugin4Shell은 핀 고정의 빈틈을 찔렀습니다

AI 보안 회사 AIR가 9월 17일 Plugin4Shell을 공개했습니다. 문제는 Claude Code, Codex, GitHub Copilot, Gemini CLI가 플러그인을 특정 커밋에 고정해도 실제로 그 커밋의 코드가 디스크에 놓였는지 확인하지 않았다는 점이다. AIR는 이 결함을 AI 에이전트 생태계의 첫 공급망 취약점이라고 부릅니다. [AIR](https://www.air.security/blog-posts/plugin4shell)

공격 경로는 작지만 곧장 위험합니다. 마켓플레이스가 검토한 커밋을 핀으로 걸면 에이전트는 그 커밋을 체크아웃합니다. 빈틈은 그 다음에 생겼다. 체크아웃 뒤 `HEAD`가 기대한 SHA인지 확인하지 않았고, 플러그인 저장소를 쥔 공격자는 기본 브랜치 이름을 핀된 해시와 똑같은 40자 hex 문자열로 바꾼 뒤 그 브랜치에 악성 코드를 넣을 수 있었습니다. git이 커밋 해시보다 브랜치 이름을 먼저 찾으면서 악성 코드가 설치됩니다. [Help Net Security](https://www.helpnetsecurity.com/2026/09/18/plugin4shell-ai-coding-agents-vulnerability/)

설치 순간만의 구멍도 아니었다. 같은 체크아웃 로직이 플러그인 백그라운드 자동 업데이트에서 다시 실행되고, Claude Code와 Codex에서는 그 자동 업데이트가 기본값으로 켜져 있습니다. 마켓플레이스가 핀을 새 커밋으로 올리면 이미 설치된 플러그인이 사용자 클릭 없이 악성 버전으로 바뀔 수 있다. 다만 모든 git 호스트에서 가능한 공격은 아니다. GitHub는 40자 hex 브랜치 이름을 거부하지만 Bitbucket과 자체 호스팅 git 서버는 허용합니다. [Help Net Security](https://www.helpnetsecurity.com/2026/09/18/plugin4shell-ai-coding-agents-vulnerability/)

AIR는 2026년 5월에 결함을 찾아 네 에이전트 모두에 통하는 개념 증명을 만들었고, 6월에 벤더들에게 알렸습니다. Anthropic은 Claude Code 2.1.179에서, OpenAI는 Codex 0.146.0에서 수정했습니다. Microsoft는 Copilot 패치를 내지 않았고, Google은 Gemini CLI를 고치는 대신 폐기하면서 기존 사용자에게 Antigravity로 옮기라고 안내하는 쪽을 택했다. [Help Net Security](https://www.helpnetsecurity.com/2026/09/18/plugin4shell-ai-coding-agents-vulnerability/)

## 마켓플레이스를 믿어도 실행 코드는 따로 확인해야 합니다

이 사건에서 노출된 사람은 무작위 스크립트를 내려받은 사용자가 아니다. 신뢰하는 마켓플레이스에서 검토된 플러그인을 골랐고, 그 플러그인을 특정 커밋에 정확히 고정한 사용자다. 핀은 "어느 버전을 원한다"는 요청이었지만, 에이전트 안에서는 "그 버전이 도착했다"는 검증까지 이어지지 않았다.

에이전트 플러그인은 일반 라이브러리보다 더 가까운 곳에서 실행되는 코드입니다. 코딩 에이전트가 사용자 권한으로 도는 만큼 플러그인 코드도 파일 전체, 배포 키, 자격증명에 닿을 수 있죠. 지금까지 에이전트 보안 논의가 모델이나 에이전트 본체에 많이 머물렀다면, Plugin4Shell은 그 아래 유통 계층인 마켓플레이스와 설치 흐름을 건드린다.

한 제품의 실수로 끝나지 않는 이유도 여기에 있다. AIR의 개념 증명은 네 랩의 에이전트에서 통했고, 마켓플레이스만 손봐서는 완전히 막히지 않는다. 핀 검증은 에이전트 안에서 실행돼야 합니다. 마켓플레이스가 할 수 있는 강한 조치는 해시처럼 생긴 브랜치 이름을 거부하는 호스트만 받는 정도다. 그렇게 하면 에이전트가 공식 지원하는 Bitbucket이나 사내 git 서버를 잘라내게 됩니다.

인디 개발자 입장에서 플러그인은 작은 편의 기능만이 아닙니다. 남의 저장소를 가리키는 플러그인은 외부 공급자입니다. 저장소 주인이 바뀌거나 기본 브랜치가 바뀌거나 자동 업데이트 경로가 열려 있으면, 내 제품의 사용자에게도 그 변경이 닿는다.

## 지금 확인할 기준

Claude Code에서는 `claude --version`이 2.1.179 이상이면 수정된 버전이다. Codex는 `codex --version`이 0.146.0 이상이어야 합니다. 이 두 제품은 업데이트가 완전한 수정이다.

GitHub Copilot에는 아직 Microsoft 패치가 없다. 그래서 지금의 기준은 자동 업데이트를 끄고 마켓플레이스 플러그인 수를 줄이는 쪽에 가깝다. Gemini CLI에는 패치가 오지 않는다. 기존 설치본은 계속 취약하므로 Google 안내대로 Antigravity나 다른 에이전트로 옮기는 계획이 필요하다.

설치 스크립트나 CI에서 직접 거를 수 있는 부분도 있다. 체크아웃 뒤 `git rev-parse HEAD`가 기대한 SHA와 같은지 비교하면 된다. 다르면 설치를 중단하는 조건을 넣으면 된다. 에이전트 내부에서 이미 실행되는 경로까지 모두 막지는 못하지만, 파이프라인에 들어온 플러그인 바꿔치기는 잡을 수 있다.

플러그인 인벤토리도 필요하다. 어떤 플러그인을 어느 저장소에서 받았고 그 저장소를 누가 통제하는지 목록으로 남기는 일이다. Bitbucket이나 사내 git 서버를 참조하는 팀은 GitHub의 40자 hex 브랜치 이름 차단에 기대기 어렵기 때문에 더 급하다.

## 같은 주에 다른 경로도 열렸습니다

Gemini CLI 사용자는 제품 폐기 결정 때문에 끝까지 노출됩니다. 새 패치가 없으니 남는 선택지는 이동뿐입니다. 영향 범위도 깔끔히 세기 어렵다. AIR는 영향받는 에이전트를 수백만 개로 봅니다. 실제 악용 사례가 공개된 것은 아직 없고, 설치 규모도 정확히 셀 방법이 없습니다. [AIR](https://www.air.security/blog-posts/plugin4shell)

같은 주에는 다른 성격의 공격도 있었다. 보안 스타트업 Hacktron AI의 3인 팀이 Claude Opus 5를 사용해 OpenAI 직원 ChatGPT 계정 여러 개에 들어갔고 회사 소프트웨어에도 접근했다. 시작점은 OpenAI 개발자 커뮤니티 포럼이 쓰는 Discourse의 이미지 업로드 결함이었습니다. 팀은 7월 25일에 찾아 신고했고 6,500달러 포상금을 받았습니다. [TechCrunch](https://techcrunch.com/2026/09/18/researchers-used-anthropics-claude-to-hack-into-openai/)

Gray Swan의 Matt Fredrikson은 TechCrunch에 월 200달러면 누구나 이런 도구로 OpenAI 같은 회사를 공격할 수 있다고 말했습니다. 작은 팀은 표적이 되지 않는다는 가정도 흔들립니다. 유지보수자나 인디 개발자는 오히려 반대쪽 위험을 집니다. 내가 참조하는 저장소 하나가 탈취되면 내 사용자가 공격을 받는다.

## 오늘의 다른 소식 (한 줄)

- **결정값만 내는 모델이 개발자들 사이에서 화제입니다**: 챗GPT 개발과 RLHF 연구에 참여한 OpenAI 출신 연구자가 세운 TypeSafe AI가 이번 주 Jev를 공개했습니다. 문장 대신 확률이 붙은 결정을 내리는 모델이고, 출력 토큰은 무료이며 입력 토큰은 100만 개가 아니라 10억 개 단위로 과금합니다. Vercel은 자체 안전 분류기를 OpenAI Luna에서 Jev로 바꾼 뒤 5배에서 18배 빨라지고 정확도도 올랐다고 밝혔습니다. [TechCrunch](https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/)
- **Meta Muse가 맥에 올라왔습니다**: 파일, 메시지, 캘린더, 메모, 메일을 각 앱 안에서 직접 다룹니다. 접근 범위는 항목별로 켜고 끄며, 민감한 작업은 매번 승인을 받습니다. [TechCrunch](https://techcrunch.com/2026/09/18/metas-muse-hits-mac-letting-the-ai-take-actions-on-your-computer/)
- **앤스로픽의 첫 임베디드 평가자는 액센츄어입니다**: 액센츄어가 1월에 인수한 Faculty 인력이 앤스로픽 안에서 모델 레드팀과 정렬 평가, 안전장치 시험을 맡습니다. 두 회사는 5년간 최소 10억 달러를 함께 투자하고, 발표 뒤 액센츄어 주가가 시간외에서 8% 올랐습니다. [TechCrunch](https://techcrunch.com/2026/09/18/anthropics-first-embedded-evaluator-is-accenture/)
- **구글이 CC를 가족 비서로 돌렸습니다**: CC가 자기 구글 계정과 권한을 따로 갖고 가족 구성원과 일을 맞춥니다. 가족마다 Gmail과 캘린더에서 공유할 항목을 고르고, 특정 발신자의 메일은 자동 공유로 묶을 수 있습니다. [TechCrunch](https://techcrunch.com/2026/09/18/googles-new-cc-is-an-ai-agent-that-helps-families-run-their-households/)
- **Manus가 40억 달러 밸류로 5억 달러 투자를 유치합니다**: 메타와의 20억 달러 인수가 중국 당국에 막힌 뒤 독립 운영으로 돌아왔습니다. IDG캐피탈과 보위캐피탈, CATL이 새 투자자로 검토되고 있고 홍콩 상장을 위한 재편도 논의됩니다. [TechCrunch](https://techcrunch.com/2026/09/18/manus-seeks-4b-valuation-in-new-500m-fundraise-as-it-resumes-independent-ops/)
- **앤스로픽은 Claude가 자사 모델 R&D의 26%를 이끈다고 밝혔습니다**: 나머지를 포함하면 R&D의 약 90%가 Claude와의 협업으로 이뤄집니다. 같은 발표에서 업계가 개발 속도 지표를 공개하자는 제안도 나왔습니다. [The Canberra Times](https://www.canberratimes.com.au/story/9352917/anthropics-ai-helping-to-build-next-version-of-itself/)
- **미 연방항공청이 8억 7,500만 달러 AI 관제 도구를 올립니다**: SMART가 워싱턴 DC 3개 공항에서 항공 교통 흐름과 충돌 가능성을 예측합니다. 이르면 9월 21일 시작이고 이후 미국 전역으로 넓힐 계획입니다. [Ars Technica](https://arstechnica.com/ai/2026/09/faa-tees-up-875m-ai-tool-to-help-manage-air-traffic-congestion/)
- **미 정부 웹사이트가 FBI가 악성이라 부른 중국 모델을 썼습니다**: Federal Register가 알리바바 Qwen 검색을 잠깐 노출했다가 내렸습니다. FBI는 이달 초 알리바바를 산업 규모 증류를 하는 중국 기업 여섯 곳 중 하나로 지목했습니다. [Ars Technica](https://arstechnica.com/tech-policy/2026/09/us-government-website-used-chinese-model-the-fbi-called-malicious/)
- **캘리포니아가 프런티어 모델 킬 스위치를 검토합니다**: 뉴섬 주지사가 행정명령을 내리고 전문가 그룹에서 두 달 안에 권고안을 받기로 했습니다. 독립 검증 인력의 상주 감사, 투명성 보고서의 외부 검증, 통제 상실 사고의 중대 사고 보고가 검토 항목입니다. [The Verge](https://www.theverge.com/policy/997516/california-governor-newsom-ai-kill-switch)
- **버지니아가 데이터센터 승인을 조입니다**: 스팬버거 주지사가 행정명령 22호에 서명해 데이터센터 프로젝트의 비밀유지계약 체결을 막고, 소음 규정을 앞당기고, 비상발전 운영 검토를 요구했습니다. 워크포스 이전과 데이터 프라이버시를 다룰 AI 태스크포스도 함께 만듭니다. [The Verge](https://www.theverge.com/policy/997573/virginia-governor-spanberger-data-center-ai-task-force)
