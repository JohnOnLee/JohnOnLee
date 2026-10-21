---
title: "LiteLLM 1.107.0 악성 배포, 빌드가 뚫렸습니다"
date: 2026-10-22
summary: "10월 21일 LiteLLM 1.107.0이 자격증명을 훔치는 코드를 담은 채 PyPI와 도커 레지스트리에 배포됐습니다."
---

## LiteLLM 1.107.0이 자격증명 탈취 코드를 달고 PyPI에 올라갔습니다

10월 21일 LiteLLM 1.107.0이 자격증명을 훔치는 코드를 담은 채 PyPI와 도커 레지스트리에 배포됐습니다. [LiteLLM](https://docs.litellm.ai/blog/security-incident-oct-21-2026)

문제가 된 건 휠 안에 끼어든 파일 세 개입니다. cook.pth, cook.py, sitecustomize.py가 site-packages 최상위에 들어갔고, 이 자리들은 파이썬이 시작될 때마다 자동으로 실행됩니다. 앱이 litellm을 불러오지 않아도 돕니다. 훔치는 범위는 이렇습니다. SSH 키, 브라우저에 저장된 비밀번호, 클라우드 자격증명, 쿠버네티스 토큰, 개발도구 설정, 프로세스 환경변수. LiteLLM 프록시가 데이터베이스에 쌓아둔 제공자 API 키도 직접 조회해 가져갑니다. 모은 데이터가 나간 곳은 실제 도메인 litellm.ai와 비슷하게 생긴 www.litellm.dev입니다. [Wiz](https://www.wiz.io/blog/litellm-compromised-steals-credentials)

공격자가 노린 지점은 소스가 아니라 빌드 단계였습니다. 같은 버전의 깃 태그와 소스 타르볼에는 악성 파일이 없었습니다. 공격자는 LiteLLM과 이름이 비슷한 저장소 Berri-AI/litellm에서 빌드를 돌려 그 산출물을 올렸습니다. 배포 파이프라인에 접근한 건 엔지니어 세 명의 깃허브 계정. 깃허브 CLI OAuth 토큰이 탈취된 정황입니다. [GitHub 이슈](https://github.com/BerriAI/litellm/issues/47826)

PyPI 휠은 UTC 11시 39분부터 13시 23분까지 올라가 있었습니다. 도커 이미지는 11시 46분부터 14시 20분까지입니다. 지금은 PyPI와 도커허브, GHCR 모두에서 내려갔습니다. 안전한 마지막 버전은 1.106.2.

## 오늘 확인할 것은 이미 설치한 서버입니다

먼저 확인할 건 그 사이 버전을 설치한 적이 있는지입니다. LiteLLM은 여러 LLM 제공자를 하나의 API로 묶는 게이트웨이라 널리 쓰입니다. 지난달 PyPI 다운로드가 1억 건을 넘었고, 2천 개가 넘는 패키지가 LiteLLM을 가져다 씁니다. [Chainguard](https://www.chainguard.dev/unchained/litellm-attacked-again-malicious-1-107-0-wheels-on-pypi-and-docker-hub-october-2026)

프록시로 돌리는 구성이면 피해가 한 대에서 끝나지 않죠. 여러 제공자의 키를 한 데이터베이스에 모아두기 때문입니다. 이미 1.107.0을 설치한 적이 있다면 순서를 지켜야 합니다. 그 환경에서 pip을 먼저 돌리면 안 됩니다. 파이썬이 뜨는 순간 같은 코드가 다시 실행됩니다.

- site-packages에서 cook.pth, cook.py, sitecustomize.py와 같은 이름의 __pycache__ 파일을 지웁니다.
- /tmp/remote_code_loader.lock을 잡고 있는 백그라운드 파이썬 프로세스를 찾아 종료합니다.
- 그 호스트가 닿을 수 있었던 자격증명은 전부 교체합니다. 클라우드 역할, LiteLLM 프록시 데이터베이스의 제공자 키, DATABASE_URL, 프로세스 환경변수에 있던 값까지.

컨테이너와 가상환경은 흔적을 지우는 것보다 새로 만드는 편이 빠릅니다.

## 오늘의 다른 소식 (한 줄)

- **오픈AI 모델이 구글 클라우드에 들어갑니다**: Model Garden에서 GPT 계열 모델과 Codex 워크플로를 살 수 있게 되고, Antigravity와 Gemini Agent에도 순차적으로 붙습니다. [CNBC](https://www.cnbc.com/2026/10/21/openai-bring-its-ai-models-to-googles-cloud-expands-beyond-microsoft.html)
- **앤스로픽이 Claude Duet 연구 프리뷰를 열었습니다**: Claude Opus 5.5 기반의 백그라운드 에이전트 앱으로, 아침 브리핑을 보내고 승인을 받은 뒤에만 메시지 발송이나 결제를 합니다. 미국 Pro·Max 구독자 대기 명단입니다. [Anthropic](https://claude.com/resources/articles/claude-duet)
- **Recursive가 노트북용 코딩 모델 Flint를 공개했습니다**: 40B MoE에서 2.5B만 활성화하는 구조로 MacBook Pro에서 초당 131토큰을 냈고, 아파치 2.0으로 Hugging Face에 올랐습니다. 개발 대부분을 자사 자동화 연구 시스템이 맡았다고 밝혔습니다. [TechCrunch](https://techcrunch.com/2026/10/21/recursive-launches-flint-a-laptop-coding-model-it-says-was-largely-built-by-ai/)
- **Flapping Airplanes가 10억 달러 시리즈 A를 유치했습니다**: 기업가치 60억 달러 평가이고 설립 9개월 만입니다. 적은 데이터로 큰 모델을 훈련하는 방법을 연구합니다. [TechCrunch](https://techcrunch.com/2026/10/21/year-old-ai-lab-flapping-airplanes-raises-1b-at-a-6b-valuation/)
- **PHP 코어 원격 코드 실행 취약점 2건이 공개됐습니다**: CVE-2026-109618과 CVE-2026-109619, CVSS 9.2이고 PHP 5.4 이후 버전이 모두 영향을 받습니다. 10월 21일 패치가 나왔습니다. [Wiz](https://www.wiz.io/blog/php2shell-php-rce)
- **앤스로픽이 클라우드 컴퓨팅 확보에 어려움을 겪고 있습니다**: AWS와 구글, 마이크로소프트가 자사 경쟁자가 된 상황에서 원하는 만큼 용량을 주지 않는다고 합니다. [India Today](https://www.indiatoday.in/technology/news/story/anthropic-is-struggling-to-get-compute-from-aws-google-and-microsoft-3021835-2026-10-21)