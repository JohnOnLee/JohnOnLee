---
title: "Anthropic, IPO 기밀 제출 + Project Glasswing 출범"
date: 2026-06-03
summary: "$65B 투자 유치 후 IPO 추진. 동시에 Apple, AWS, Google, Microsoft, NVIDIA, CrowdStrike 등이 참여하는 Project Glasswing 컨소시엄 출범. Claude Mythos가 27년 된 Op…"
description: "$65B 투자 유치 후 IPO 추진. 동시에 Apple, AWS, Google, Microsoft, NVIDIA, CrowdStrike 등이 참여하는 Project Glasswing 컨소시엄 출범. Claude Mythos가 27년 된 Op…"
---

## 핵심 변화
- **Anthropic, IPO 기밀 제출 + Project Glasswing 출범**: $65B 투자 유치 후 IPO 추진. 동시에 Apple, AWS, Google, Microsoft, NVIDIA, CrowdStrike 등이 참여하는 Project Glasswing 컨소시엄 출범. Claude Mythos가 27년 된 OpenBSD 취약점, 16년 된 FFmpeg 취약점 등 수천 개의 제로데이를 발견. 한국 기업으로는 삼성, SK하이닉스, SK텔레콤이 Mythos 접근 권한 확보
  출처: [TechCrunch](https://techcrunch.com/2026/06/02/anthropic-scales-claude-mythos-to-critical-infrastructure-in-15-countries/) · [Anthropic](https://www.anthropic.com/glasswing)
- **기업 AI ROI 위기 가시화**: Uber, 연간 AI 예산을 4개월 만에 소진하고 직원당 월 $1,500 사용 한도 설정. COO도 "AI 사용과 제품 기능 개선 사이의 인과관계를 찾기 어렵다"고 언급. HN에서 "AI Doesn't Have ROI" 에세이가 56포인트로 확산
  출처: [TechCrunch](https://techcrunch.com/2026/06/02/uber-caps-employee-ai-spending-after-blowing-through-budget-in-four-months/) · [Wheresyoured](https://www.wheresyoured.at/ai-doesnt-have-roi/)
- **에이전트 직장 점령 경쟁 가속**: Microsoft, 상시 가동형 자율 에이전트 Scout 발표 (M365 앱 연동). OpenAI, Codex에 데이터 분석·영업·투자은행 등 6종 직무별 플러그인 출시. Codex 주간 활성 사용자 500만 돌파, 지식 노동자 비중 20%로 3배 빠르게 성장 중
  출처: [Computerworld](https://www.computerworld.com/article/4180103/microsoft-unveils-scout-an-autonomous-ai-agent-built-on-openclaw.html) · [TechCrunch](https://techcrunch.com/2026/06/02/openai-launches-new-codex-tools-for-white-collar-work/)
- **AI 사이버 보안: 공격·방어 군비 경쟁**: Claude Mythos가 Linux 커널 권한 상승 취약점 체이닝까지 자율 수행. OpenAI도 GPT-5.5-Cyber로 대응. 404 Media는 Microsoft 내부 문서를 인용해 "Scout에 중독되게 만들겠다"는 목표 보도
  출처: [404 Media](https://www.404media.co/microsoft-wants-to-make-people-addicted-to-scout-its-new-ai-assistant-internal-documents-reveal/)

## 스타트업 / 제품 / 플랫폼 레이더
- **Anthropic**: Opus 4.8 출시 — 'dynamic workflow' 도구 탑재. Claude Mythos, 15개국 이상 중요 인프라로 확대
- **Microsoft**: Scout(자율 에이전트), MAI-Code-1-Flash·MAI-Thinking-1 신규 모델, AI 에이전트 행동 제어 도구, 텍스트 기반 AI 행동 테스트 도구 출시
- **OpenAI**: Codex 직무별 플러그인 6종 + Sites(호스팅 웹사이트 출력) + Annotations 기능. GPT-5.5-Cyber 보안 특화 모델
- **GitHub Copilot**: 사용량 기반 토큰 과금 체계로 전환, 개발자 커뮤니티 강력 반발 ("What a joke")
  출처: [Ars Technica](https://arstechnica.com/ai/2026/06/ai-costs-how-much-github-copilot-users-react-to-new-usage-based-pricing-system/)
- **DeepSeek-V4-Flash**: AMD MI300X에서 구동 성공 사례 등장
- **Google**: AI 딥페이크 사기 탐지 통화 보호 기능 출시
- **DuckDuckGo**: 'no-AI' 검색 엔진 트래픽 급증, 접근성 강화
  출처: [TechCrunch](https://techcrunch.com/2026/06/01/duckduckgo-makes-its-no-ai-search-engine-easier-to-access-as-its-traffic-booms/)
- **YC P26**: Expanse (유휴 GPU 용량 활용), Rudus (건설 콘크리트 AI)
- **기타**: Skillhound (공개 SKILL.md 접근), vLLM 세션 인식 에이전트 라우팅, RSS 부활(AI 에이전트가 읽기 시작)

## AI가 바꾸는 미래 신호
- **AI 네이티브 보안 감사가 기본 인프라가 된다**: Mythos가 27년 묵은 OpenBSD 취약점을 찾아냈다는 건, 우리가 의존하는 모든 소프트웨어에 아직 발견되지 않은 취약점이 수두룩하다는 뜻. 1~2년 내에 모든 중요 인프라는 AI 기반 상시 보안 감사를 받는 게 당연해질 것
- **'공짜 점심' AI 예산 시대의 종말**: Uber 사례는 빙산의 일각. Copilot의 사용량 과금 전환에 대한 격렬한 반발은 기업/개발자 모두 AI 비용이 예상보다 훨씬 크다는 걸 깨닫기 시작했다는 신호. AI 도입의 진짜 장벽은 기술이 아니라 경제성이 될 것
- **상시 가동 에이전트가 OS의 다음 레이어가 된다**: Scout의 'autopilot' 컨셉은 사용자가 명령하지 않아도 백그라운드에서 일하는 에이전트. Google Spark, OpenAI Codex와 함께 '에이전트 OS' 레이어를 누가 장악하느냐의 싸움. 이긴 쪽이 다음 10년의 플랫폼이 된다
- **AI 냉전 구도 형성**: Project Glasswing(Anthropic+미국 빅테크 연합) vs 중국(DeepSeek). 사이버 보안에서 시작됐지만, AI가 국가 안보 인프라로 편입되면서 기술 표준과 동맹국 라인까지 결정할 수 있는 지정학적 변수가 되고 있음

## 현실적인 기회 / 실험 아이디어
- **AI 비용 최적화 미들웨어**: Uber처럼 기업들이 AI 사용량을 통제할 도구가 절실하다. 사용량 모니터링, 모델 라우팅(비싼 모델 vs 싼 모델), 예산 알림, 팀별 할당량 관리 — 아직 초기 시장. Copilot 과금 반발은 시장 타이밍이 좋다는 신호
- **수직 특화 에이전트 + 명확한 ROI 지표**: 'AI가 생산성을 높인다'는 막연한 주장은 더 이상 통하지 않는다. 건설(Rudus), 콘크리트, 제조 등 ROI를 측정 가능한 협소한 도메인에서 에이전트를 만들고, 비용 절감 또는 매출 증가 수치를 직접 연결하는 접근이 차별화 포인트
- **AI 보안 감사 SaaS**: Mythos 수준은 아니어도, 중견기업이 감당할 수 있는 가격대로 코드베이스 취약점 감사 서비스를 제공하는 모델. Glasswing이 대기업·정부 레이어를 장악한다면, 그 아래 중견·스타트업 레이어가 비어 있음

## 불확실성 / 계속 볼 것
- **Anthropic IPO가 AI 섹터 전체를 리프라이싱할까**: $1T 밸류에이션이 공모 시장에서 유지될지, 아니면 과대평가로 드러날지
- **Uber 사태가 AI 업계 전반의 '지출 조정' 신호탄인가, 아니면 Uber만의 관리 실패인가**: 전자라면 Copilot, Cursor, Codex 같은 도구들의 매출 모델에 직격탄
- **Project Glasswing이 사실상의 AI 안보 동맹으로 진화할 가능성**: 사이버 보안에서 AI 표준·규제로 확장되면, 비참여 기업과 국가는 배제될 위험
- **'no-AI' 백래시의 실체**: DuckDuckGo의 트래픽 급증, 데이터센터 반대 운동, 하버드 졸업연설까지 — 이게 일시적 반작용인지, 지속 가능한 소비자 세그먼트로 정착할지