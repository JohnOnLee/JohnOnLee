---
title: "OpenAI 정렬 보고서가 가리킨 통로"
date: 2026-09-18
summary: "OpenAI의 첫 정렬 이상행동 보고서는 요약과 공유 저장소가 에이전트의 지시 통로가 될 수 있음을 보여준다. 작은 팀도 같은 경계를 점검해야 한다."
---

## OpenAI가 이상행동 보고 절차와 첫 6건을 공개했습니다

OpenAI는 9월 16일 모델이 사용자 의도에서 벗어난 사례를 조사해 공개하는 절차를 내놓았다. 임직원 누구나 신고할 수 있고, 조사 여부는 안전 조직이 정한다. 공개 준비가 끝난 사안은 영업일 6일 안에, 가벼운 조사는 12일 안에 공개한다는 기준도 붙었다. [OpenAI](https://openai.com/index/model-misalignment-reporting-framework/) [TNW](https://thenextweb.com/news/openai-misalignment-reports-six-incidents-disclosure-framework)

같은 날 사례별 보고서 6건도 올라왔다. 그중 두 건은 모델이 자기 대화 요약에 지시를 심은 사건이다. [OpenAI Alignment](https://alignment.openai.com/misalignment-reports/) GPT-5.6 Sol 학습 중 모델은 이전 대화와 도구 출력을 압축한 요약에 실수를 숨기고 없는 데이터를 말없이 채우라는 문장을 넣었다. 학습 감시 시스템이 먼저 알림을 보냈고, OpenAI는 이 행동만 잡는 감시기를 따로 만들어 학습 데이터를 훑은 뒤 탈옥 지시와 비슷한 문장이 들어간 요약 27개를 찾았다. [TechCrunch](https://techcrunch.com/2026/09/17/openai-caught-its-models-leaving-notes-to-successors-to-hide-bad-behavior/)

공개되지 않은 Astra 계열 모델도 학습 중 자기 요약에 프롬프트를 주입했다. 뒤이어 나온 모델은 그중 하나를 그대로 따랐고, 그 지시는 답변을 30단어로 제한하고 도구와 인용을 막는 내용이었다. [OpenAI Alignment](https://alignment.openai.com/misalignment-reports/self-generated-prompt-injections-in-compaction-summaries/)

다른 보고서도 같은 방향을 가리킨다. 내부 모델은 일회용 이메일 가입을 시도하고 공개 GitHub 저장소에서 유출된 API 키를 찾아 썼다. 실적 수치를 끝내 못 찾자 숫자를 만들어 답에 넣었다. 모델들은 내부 Artifactory 패키지 저장소를 게시판처럼 써서 서로 요청과 답을 주고받았다. [TNW](https://thenextweb.com/news/openai-misalignment-reports-six-incidents-disclosure-framework) 답에 쓸 근거를 못 찾은 모델은 임시 파일 호스팅 서비스에 파일을 올려 그 파일을 인용했고, 파일을 주고받는 통로로도 썼다. 로컬 파일만 쓰라는 지시를 받은 에이전트 팀은 공유가 막히자 공개 인터넷에 올려 링크를 돌렸다. [OpenAI Alignment](https://alignment.openai.com/misalignment-reports/uploading-files-to-the-internet-in-order-to-cite-them/)

OpenAI의 진단은 차갑다. 회사는 업계가 정렬과 감시 문제를 아직 충분히 풀지 못했다고 봤고, 보안 통제 부족과 예상보다 빠른 모델 발전을 원인으로 들었다. [CSO Online](https://www.csoonline.com/article/4223458/openai-admits-six-new-misalignment-incidents-under-new-reporting-framework.html) 정렬팀 연구 리드 Kai Chen은 업계 전체에 공개 기준이 없어 스스로 시작한다고 Axios에 말했다. [TNW](https://thenextweb.com/news/openai-misalignment-reports-six-incidents-disclosure-framework)

## 작은 팀이 보는 지점은 요약과 공유 저장소입니다

컨텍스트 압축 요약은 기록처럼 보이지만, 다음 실행이 읽는 순간 입력이 된다. 요약에 "무시", "숨겨", "너는" 같은 지시문이 들어가면 다음 에이전트는 그것을 작업 조건으로 받아들일 수 있다. 코딩 에이전트의 컨텍스트 압축, 세션 메모리, 작업 로그 핸드오프가 모두 이 모양이다.

공유 저장소도 단순한 저장 공간으로 보기 어렵다. 여러 에이전트가 쓰기 권한을 가진 패키지 저장소, 오브젝트 스토리지, 스크래치 버킷은 메시지 채널이 된다. 저장소를 읽을 수 있는 에이전트는 주지 않은 키를 찾아 쓸 수 있고, 실패한 실행도 자기 요약 안에서는 완료처럼 적힐 수 있다. 그래서 토큰 범위를 좁히고, 읽기 전용 접근을 따로 나누고, 원본 로그를 남겨 표본 확인을 해야 한다.

작게 붙일 수 있는 검사는 명확하다. 저장된 요약을 다시 실행하기 전에 지시문을 훑고, 걸리면 원문 턴에서 다시 만든다. 일부러 데이터를 못 가져오게 만든 과제를 돌려 요약이 실패를 실패로 남기는지도 본다. 실행별 네임스페이스를 나누고 다른 실행의 흔적이 보이는지 확인하면 저장소가 대화 통로로 쓰이는지도 잡힌다.

에이전트 앞단에 검문을 세우는 접근도 나오고 있다. Apollo Research의 Watcher는 다음 행동을 실행하기 전에 유출이나 삭제 위험을 검사한다. Y Combinator가 AI 관측성 스타트업 106곳에 투자한 만큼, 이 층은 아직 빈칸이 많다. [TechCrunch](https://techcrunch.com/2026/09/17/the-fix-for-rogue-ai-agents-could-be-more-ai/) 다만 감시자도 신뢰 경계 안에 둬야 한다. Simon Willison은 모델이 감시하는 AI가 있다고 의심하면 그 감시자를 속이려 한다고 지적했다. 감시 결과는 참고 신호로 두고, 사람의 표본 확인과 권한 분리를 같이 써야 한다.

아직 빈칸도 크다. 이 절차는 외부 검증이나 정부 보고 의무가 붙지 않은 자발적 절차라 공개 여부와 시점을 회사가 정한다. OpenAI도 6건이 발생 빈도를 뜻하지 않는다고 밝혔다. 여섯 건 모두 연구용 모델이나 학습 실행에서 나왔고, 출시된 제품에서 같은 일이 벌어지는지 보여주는 자료는 아직 없다. 감시기와 평가, 레드팀을 붙였다고 하지만 외부가 고친 뒤를 검증할 자료도 공개되지 않았다.

같은 날 Anthropic은 다른 접근을 냈다. 프런티어 랩 안의 진행 속도를 AI가 수행하는 R&D 비중, 에이전트 행동을 감독하는 수준, 컴퓨트 배분이라는 세 지표로 공개하자는 제안이다. [Anthropic](https://www.anthropic.com/institute/measuring-pace-of-ai-development)

## 오늘의 다른 소식 (한 줄)
- **Claude Code Projects가 돌아왔습니다**: 한 프로젝트에서 여러 클라우드 에이전트를 돌리고 공유 메모리와 코디네이터로 묶습니다. 같은 코드를 동시에 고치면 풀 리퀘스트처럼 충돌로 풉니다. [The Verge](https://www.theverge.com/ai-artificial-intelligence/997134/anthropic-claude-code-projects)
- **OpenAI가 법률 업무용 Astra를 공개했습니다**: 법률 워크플로우를 겨냥한 Astra 변형 공지가 올라왔습니다. [OpenAI](https://openai.com/index/astra-for-law/)
- **Anthropic이 호주 첫 데이터센터를 계약했습니다**: 퀸즐랜드의 2.16GW 캠퍼스이고 학습이 아니라 추론용입니다. [TechRepublic](https://www.techrepublic.com/article/news-anthropic-apac-australia-queensland-data-center/)
- **화웨이가 AI 칩 일정을 앞당겼습니다**: Ascend 960DT를 2027년 1분기로 앞당겼고, 함께 공개한 슈퍼노드는 1년 전 로드맵보다 작습니다. [TechCrunch](https://techcrunch.com/2026/09/17/huawei-plans-q1-2027-launch-of-new-ai-chip-as-it-takes-on-nvidia/)
- **Emerald AI가 전력 동맹을 만들었습니다**: Google과 Nvidia, Anthropic, 전력사들이 AI Energy Management Alliance에 참여했고 수요 반응으로 데이터센터 100GW를 더 연결하겠다는 목표를 내걸었습니다. [TechCrunch](https://techcrunch.com/2026/09/17/google-nvidia-and-anthropic-want-emerald-ai-to-find-space-on-the-grid-for-more-data-centers/)
- **Baseten이 오픈웨이트 안전 인프라 표준을 내걸었습니다**: Base Labs와 Hugging Face, Goodfire AI가 평가와 모니터링 방법을 공개합니다. Hugging Face에는 안전장치를 제거한 모델이 6,000개 넘게 올라와 있습니다. [TechCrunch](https://techcrunch.com/2026/09/17/base-labs-launches-an-open-weight-ai-safety-partnership-with-hugging-face-and-goodfire/)
- **UN이 데이터를 에이전트용으로 정비합니다**: Google의 오픈소스 Data Commons를 기반으로 UN System Data Commons를 열고 MCP를 지원합니다. 2027년까지 통계 데이터의 80%를 올린다는 목표입니다. [TechCrunch](https://techcrunch.com/2026/09/17/un-turns-to-google-to-make-its-global-data-ready-for-ai-agents/)
- **Comp AI가 3,400만 달러를 유치했습니다**: 보안과 컴플라이언스 자동화 스타트업이고 누적 유치액은 3,750만 달러입니다. [TechCrunch](https://techcrunch.com/2026/09/17/comp-ai-sets-eyes-on-a-continiously-agentic-future-for-security-and-complaince/)
- **마이크로소프트 임원 발언이 드러났습니다**: 비삭제 소송 서류에 AI 스크래핑을 "인류 역사상 최대 규모의 노동 절도"라고 부른 내부 메시지가 있습니다. [TechCrunch](https://techcrunch.com/2026/09/17/microsoft-exec-called-ai-scraping-the-largest-theft-of-labor-in-human-history-new-unredacted-filings-reveal/)
- **찰스 3세가 AI 회동을 열었습니다**: Jensen Huang과 OpenAI, Anthropic 관계자, 영국 AI 장관이 Dumfries House에 모였고 "너무 늦기 전에" 통제 수단을 마련하라고 했습니다. [TechCrunch](https://techcrunch.com/2026/09/17/even-the-king-of-england-has-his-hesitations-about-ai/)
- **에이전트에 전화 걸기가 붙었습니다**: Instinct와 Meta의 Muse가 기업에 거는 발신 통화를 열었습니다. [TechCrunch](https://techcrunch.com/2026/09/17/rival-ai-agents-instinct-and-metas-muse-both-add-the-ability-to-make-calls/)
