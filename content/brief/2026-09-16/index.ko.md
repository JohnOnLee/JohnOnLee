---
title: "Gemini 3.8 Live, 음성 에이전트 공개"
date: 2026-09-16
summary: "두 모델 모두 네이티브 음성-대-음성 모델이고, Gemini Live API와 AI Studio에서 오늘부터 쓸 수 있습니다."
---

## 구글이 Gemini 3.8 Live와 3.8 Live Extended Thinking을 공개하고 캐스케이드 음성 파이프라인을 정면으로 겨냥했습니다
- **9월 15일 공개**: 두 모델 모두 네이티브 음성-대-음성 모델이고, Gemini Live API와 AI Studio에서 오늘부터 쓸 수 있습니다. [Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/)
- **가격은 분당 과금입니다**: 오디오 입력 $0.005/분, 오디오 출력 $0.018/분입니다. 10분 통화면 입력 $0.05에 출력 $0.18을 더해 $0.23, 60분이면 $1.38입니다. [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing)
- **비동기 함수 호출이 이번 릴리스의 중심입니다**: 도구 호출은 백그라운드에서 돌고 오디오 응답은 계속 스트리밍됩니다. 구글은 ASR, LLM, TTS를 이어 붙인 캐스케이드 구조의 대안으로 두 모델을 배치했습니다. [Google for Developers](https://blog.google/innovation-and-ai/technology/developers-tools/build-real-time-voice-applications-gemini-audio/)
- **Live API가 함께 여는 것들**: 실시간 시각 입력, 확인 코드와 청구 번호 같은 영숫자 정밀도, 97개 언어 전환, 구조화 데이터와 실시간 오디오 병합입니다. Extended Thinking은 말하면서 백그라운드로 추론하고 "확인해볼게요" 같은 초기 신호를 먼저 냅니다.
- **벤치마크 숫자**: 3.8 Live Extended Thinking이 Artificial Analysis 음성-대-음성 품질 지수에서 82.6으로 1위, τ-Voice 68.6%, τ-Voice-banking 35.1%, Big Bench Audio 97.7%를 기록했습니다. [MarkTechPost](https://www.marktechpost.com/2026/09/15/google-releases-gemini-3-8-live-and-3-8-live-extended-thinking-for-production-grade-voice-agents/)
- **호스팅 전용입니다**: 오픈 웨이트가 아니어서 직접 띄우는 선택지는 없습니다. LiveKit, Pipecat, Vercel, Agora 같은 스트리밍 파트너를 거쳐 붙일 수 있고, 9to5Google은 같은 모델이 Gemini Live와 Gmail에도 들어간다고 전했습니다. [9to5Google](https://9to5google.com/2026/09/15/gemini-3-8-live-announced/)

## 통화 10분에 0.23달러라는 숫자가 다시 여는 음성 스택 결정
- **3단 파이프라인을 걷어낼 수 있습니다**: ASR, LLM, TTS를 각각 붙이고 그 사이 턴 관리와 끊김 처리를 하던 코드가 세션 하나로 줄어듭니다. 지연 예산을 세 조각으로 나눠 쓰던 구조도 함께 단순해지죠.
- **침묵을 채우는 우회로가 필요 없어집니다**: 도구가 도는 동안에도 모델은 계속 말합니다. "잠시만요" 오디오를 미리 만들어 두고 재생할 이유가 있을까요?
- **분당 과금은 통화 길이를 그대로 원가로 만듭니다**: 10분 통화 $0.23, 60분 $1.38은 어림잡아 선형입니다. 무료 통화를 붙이는 제품이라면 통화 시간 상한과 유휴 세션 종료가 가격표보다 먼저 나옵니다.
- **모델 교체 여지는 추상화 레이어에 남습니다**: Live API를 직접 부르면 구글에 묶이니, LiveKit이나 Pipecat을 사이에 두고 세션 코드는 유지한 채 모델만 갈아끼우는 편이 낫습니다.

## 오늘 해볼 만한 것: 필러 오디오를 지우고 도구 호출을 백그라운드로 넘기면 어떻게 될까?
- **필러 오디오 제거 실험**: 기존 캐스케이드에서 쓰던 "확인 중입니다" 클립을 빼고 도구 호출이 끝날 때까지 모델이 말을 잇게 두면, 사용자가 느끼는 대기 시간이 어떻게 달라지는지 비교해볼 수 있습니다.
- **카메라와 화면 공유를 대화에 붙여보기**: 시각 입력이 실시간으로 들어오니, 사진 속 청구서 번호나 오류 화면을 읽어 주는 지원 흐름을 한 세션 안에서 만들 수 있죠.
- **Extended Thinking을 낭독 패턴으로 쓰기**: 오래 걸리는 작업을 시킬 때 "먼저 확인해볼게요" 식 초기 신호와 단계별 진행 낭독을 붙이면, 대기 시간을 침묵 대신 정보로 바꾸는 설계를 시험할 수 있습니다.
- **10분 통화 원가 비교**: 지금 쓰는 STT, LLM, TTS 단가를 합산해 같은 10분 통화 비용과 나란히 놓으면, 스택 교체 시점을 숫자로 판단할 수 있습니다.

## 벤치마크 82.6점보다 먼저 확인할 것들
- **τ-Voice-banking 35.1%는 낮습니다**: 은행 업무 같은 규제 영역의 에이전트 완주율이 이 수준이면, 완전 자동화를 약속하는 제품 문구는 아직 이릅니다.
- **무료 티어는 데이터를 학습에 씁니다**: 무료 등급으로 개인 음성을 받아도 될까요? 구글 가격표는 무료 티어 트래픽을 "Used to improve our products"로 표시하고, 유료 등급만 이 조항에서 빠집니다.
- **장시간 통화 품질은 아직 검증되지 않았습니다**: 공개된 숫자는 벤치마크와 짧은 시연 중심이니, 30분 이상 통화에서의 맥락 유지와 끼어들기 처리는 직접 재봐야 합니다.
- **비용이 대화 길이에 비례합니다**: 세션을 열어 두는 구조라면 유휴 시간도 과금 대상입니다. 상한 없는 통화를 허용하는 요금제는 손실을 키울 뿐이죠.

## 오늘의 다른 소식 (한 줄)
- **개발자들이 Claude Code를 Anthropic 모델 없이 돌리는 방법을 찾았습니다**: OpenRouter 프록시 같은 우회로가 공유됐습니다. [The Information](https://www.theinformation.com/articles/developers-find-ways-use-claude-code-without-anthropic-models)
- **메타가 WhatsApp Business 설정을 AI 에이전트에 열었습니다**: 새 MCP 서버로 코딩 에이전트가 템플릿, 번호, 테스트, 장애 확인을 처리합니다. [TechCrunch](https://techcrunch.com/2026/09/15/meta-now-lets-ai-agents-handle-the-boring-parts-of-whatsapp-business-setup/)
- **오픈AI가 FRONTIER Act를 지지했습니다**: 제3자 안전 평가를 요구하는 초당파 법안이고, 같은 날 세 랩이 몇 주째 안전 협의를 해왔다는 보도가 나왔습니다. [Politico](https://www.politico.com/news/2026/09/15/openai-backs-bipartisan-house-plan-for-third-party-safety-assessments-01076588) · [TechCrunch](https://techcrunch.com/2026/09/15/openai-anthropic-google-have-been-in-talks-on-ai-safety-for-weeks/)
- **TypeSafe가 Jev를 공개하고 4천만 달러 시드를 받았습니다**: 텍스트 생성 대신 확률이 붙은 구조화 결정을 내리는 모델이고, 입력 100만 토큰당 $0.042를 제시합니다. [TypeSafe](https://typesafe.ai/blog/introducing-system-one-models-and-jev)
- **Factory가 기업가치 50억 달러로 2억 달러를 유치했습니다**: 5개월 만에 세 배가 됐고, 자동 모델 라우팅으로 토큰 비용을 60% 줄였다고 밝혔습니다. [Factory](https://factory.com/news/5-billion-valuation)
- **404 Media: 계정 접근 권한을 가진 에이전트가 인터넷을 망가뜨리는 중**: 권한을 받은 에이전트가 실제 피해를 만들고 있다는 정리입니다. [404 Media](https://www.404media.co/theres-a-100-chance-ai-agents-are-already-ruining-the-internet/)
- **한국 KISA가 자율 AI 에이전트 보안 가이드를 만듭니다**: 에이전트 서비스 배포 때 생기는 보안 이슈와 점검 목록을 담고, 물리 AI 통제 항목도 검토합니다. [The Star](https://www.thestar.com.my/tech/tech-news/2026/09/15/south-korea-to-develop-new-security-guidelines-for-autonomous-ai-agents)
- **F-Droid 하루치 앱 102개 중 74개가 AI 작성으로 보였습니다**: 저장소 겉모습을 눈으로 본 3단 분류이고 코드 분석이 아닙니다. [tintotint](https://tintotint.eu/whacky-corner/f-droid_slop/)
- **오픈AI 재단이 Public Data for Health 1억 2,500만 달러 프로그램을 시작했습니다**: 첫 지원은 UNC 암센터 4천만 달러로, 개인 맞춤 백신 데이터를 만듭니다. [OpenAI Foundation](https://openaifoundation.org/news/public-data-for-health) · [UNC](https://news.unchealthcare.org/2026/09/unc-lineberger-secures-40m-from-openai-foundation-to-make-cancer-vaccines-more-effective/)
- **미 상무부가 Kalshi의 AI 컴퓨트 가격 지수를 내리게 했습니다**: 국가안보를 이유로 걸었고, 신규 컴퓨트 계약 승인도 60일 동결을 요청했습니다. [Semafor](https://www.semafor.com/article/09/15/2026/commerce-dept-ordered-kalshi-to-take-down-ai-compute-futures-product)
- **Profound가 기업가치 18억 달러로 1억 8천만 달러를 받았습니다**: AI 검색 노출을 다루는 AEO 도구이고, 7개월 만에 밸류에이션이 두 배가 됐습니다. [TechCrunch](https://techcrunch.com/2026/09/15/aeo-startup-profound-hits-unicorn-valuation-raises-180m-series-d-7-months-after-last-round/)