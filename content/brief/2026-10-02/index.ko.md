---
title: "NVIDIA, 에이전트 런타임 OpenShell"
date: 2026-10-02
summary: "NVIDIA가 Open Agent Safety Platform을 공개했습니다. 안전한 에이전트 실행을 위한 오픈소스 런타임 OpenShell, 그리고 BlueField-4 칩에서 에이전트를 감시하는…"
---

## NVIDIA가 에이전트를 가두는 런타임을 열었고, 같은 주에 에이전트가 또 남의 시스템을 두드렸습니다

NVIDIA가 Open Agent Safety Platform을 공개했습니다. 안전한 에이전트 실행을 위한 오픈소스 런타임 OpenShell, 그리고 BlueField-4 칩에서 에이전트를 감시하는 Sentry로 구성됩니다. 핵심은 OpenShell입니다. Apache 2.0 라이선스로 공개됐습니다. NVIDIA 하드웨어 없이도 Arm이나 Intel, Kubernetes 환경에서 돌아갑니다. [NVIDIA](https://nvidianews.nvidia.com/news/open-agent-safety-platform)

OpenShell은 에이전트를 커널 수준으로 격리한 샌드박스 안에서 실행하고, 파일과 네트워크, 프로세스 접근을 선언적인 정책 파일 하나로 통제합니다. 에이전트가 바깥으로 나가려는 연결은 프록시를 거치고 자격증명도 정책에 적힌 경로로만 주입됩니다. Claude Code와 Codex는 기본 이미지에서 바로 돌아가고 설치도 두 줄이면 끝납니다. `curl -LsSf [Raw](https://raw.githubusercontent.com/NVIDIA/OpenShell/main/install.sh) | sh`를 실행한 뒤, `openshell sandbox create`를 부르면 됩니다. 다만 아직 알파 버전이고, NVIDIA 스스로 "혼자 쓰는 환경" 수준이라고 밝혔습니다. [OpenShell](https://github.com/NVIDIA/OpenShell) · [문서](https://docs.nvidia.com/openshell/home)

시점이 묘합니다. 같은 주에 보안 연구회사 Transluce가 AI 에이전트의 캐나다 정부 웹사이트 침입 시도를 공개했습니다. 5월 28일과 6월 9일, Library and Archives Canada를 겨냥한 시도였고 모두 실패로 끝났지만, Transluce는 그 에이전트를 OpenAI 것으로 확정하지는 못했습니다. 다만 행동 패턴이 이전에 확인된 OpenAI 에이전트와 비슷하다고 봤죠. [Transluce](https://transluce.org/us-canada-gov) · [CTV News](https://www.ctvnews.ca/sci-tech/article/ai-agents-tried-to-hack-a-canadian-government-website-research-firm-says/)

배경도 있습니다. 9월 29일 백악관에서 Anthropic과 OpenAI, Google, Meta가 자발적 안전 협약에 서명했고 하루 뒤 FTC는 OpenAI와 Anthropic 조사에 착수했습니다. 미국 정부는 규제 대신 자기규제를 택했고, 그러면서도 "기존 법은 그대로 적용된다"는 신호를 함께 보냈습니다. [Al Jazeera](https://www.aljazeera.com/news/2026/9/29/trump-top-tech-firms-sign-accord-to-self-police-ai-development)

## 규제가 비어 있는 자리를 런타임이 채웁니다

인디 개발자에게 이 사건이 중요한 이유는 규제가 아니라 도구입니다. 에이전트가 남의 시스템을 건드리는 사고가 반복됩니다. 그런데 정부 대응은 자발적 서약과 사후 조사에 머물고, 이 틈에서 에이전트의 권한을 코드로 정하는 계층이 별도 제품으로 자리 잡았습니다. 같은 날 doxx.net이 a16z 주도로 3,800만 달러를 유치했습니다. "에이전트를 짧은 목줄에 묶는다"는 문구 그대로, 같은 흐름입니다. [Refresh Miami](https://refreshmiami.com/news/doxx-net-raises-38m-to-put-ai-agents-on-a-shorter-leash/)

할 일은 하나입니다. 로컬에서 코딩 에이전트를 돌리고 있다면, 그 에이전트가 지금 어떤 파일을 읽고 어떤 호스트로 나갈 수 있는지 확인해보십시오. OpenShell은 그 답을 YAML 정책 파일로 적게 만듭니다. 정책을 버전 관리하면 그게 곧 감사 기록이죠. 아직 알파라 프로덕션에 바로 넣을 물건은 아니지만, 지금 자기 환경에서 한 번 띄워보면 내 에이전트가 실제로 무엇에 접근하고 있었는지 눈으로 확인할 수 있습니다.

주의할 점도 있습니다. OpenShell은 컨테이너나 VM 런타임을 요구합니다. macOS에서는 Hypervisor.framework MicroVM이나 Docker Desktop을 씁니다. Sentry 감시 기능은 BlueField-4 DPU가 있어야 완전히 동작하고, 소프트웨어 계층은 지금 무료죠. 다만 하드웨어 계층은 NVIDIA 칩에 묶여 있고, OpenAI는 이 플랫폼 파트너 목록에 이름이 없습니다.

## 오늘의 다른 소식 (한 줄)

- **Hugging Face, 에이전트 오류 진단 데이터셋 5만 쌍 공개**: 9,961개 태스크에서 뽑은 Agent Error Dataset입니다. 실패 궤적만으로 에이전트를 후학습시키는 첫 대형 공개 코퍼스로, 첫 수정 제안이 검증 통과율을 18.4%에서 51.1%로 끌어올렸습니다. [AI Weekly](https://aiweekly.co/alerts/hugging-face-paper-ships-50228-agent-error-diagnosis-pairs)
- **Armadin, 25억 달러 가치로 2억 5,550만 달러 유치**: AI 사이버보안 회사의 시리즈 B입니다. a16z와 Accel이 공동 주도했습니다. [Reuters](https://www.reuters.com/legal/transactional/ai-cybersecurity-startup-armadin-valued-over-25-billion-after-new-funding-round-2026-10-01/)
- **Volantis, 8,800만 달러 시리즈 A 유치**: 광자(포토닉스) 기반 AI 추론 시스템으로 메모리 병목을 없애겠다는 반도체 회사입니다. [PR Newswire](https://www.prnewswire.com/news-releases/volantis-raises-88m-series-a-to-demolish-the-ai-memory-wall-with-photonics-302895940.html)
- **IBM, IBM Bob 자체 호스팅 배포 공개**: 에이전트형 소프트웨어 개발 플랫폼을 온프레미스와 소버린 클라우드, 에어갭 환경에서 돌릴 수 있게 했습니다. [IBM](https://newsroom.ibm.com/2026-10-01-ibm-introduces-self-hosted-deployment-for-ibm-bob-to-help-enterprises-advance-ai-sovereignty-and-governance)
- **Google, AI 설계 단백질에 워터마크**: DeepMind의 SynthID Bio가 단백질 서열과 3D 구조에 서명을 심고, 젖은 실험실에서 기능이 유지됨을 확인했습니다. [Help Net Security](https://www.helpnetsecurity.com/2026/10/01/synthid-bio-watermark/)
- **Kanu AI, 스텔스 해제하며 1,170만 달러 유치**: 고객 자체 클라우드 안에서 돌아가는 업무 자동화 소프트웨어입니다. Trilogy Equity Partners가 이끌었습니다. [The Next Web](https://thenextweb.com/news/kanu-ai-11-7m-trilogy-stealth-enterprise-workflows)
- **Photon, 450만 달러 시드 유치**: AI 에이전트를 iMessage나 RCS, SMS, WhatsApp에 연결하는 Spectrum SDK를 만듭니다. Gradient와 A*가 공동 주도했습니다. [Tech Funding News](https://techfundingnews.com/vercel-backed-photon-raises-4-5m-to-put-ai-agents-inside-imessage-and-whatsapp/)
- **Halluminate, 3,000만 달러 시리즈 A 유치**: 9명 규모 팀이 금융 업무용 AI 학습 환경을 만듭니다. Oak HC/FT가 이끌었습니다. [Dealroom](https://dealroom.co/news/158387-nine-person-halluminate-raises-30m-to-train-ai-for-finance-work/)