---
title: "MiniMax, 모델 카드 없이 조용히 코딩 모델 출시"
date: 2026-09-28
summary: "지난 9월 27일 MiniMax가 자사 코딩 에이전트 제품인 MiniMax Code 안에서 M3.1-Flash-Preview를 조용히 켰습니다. 모델 카드도 벤치마크 리포트도 공개 API 가격도…"
---

## MiniMax M3.1-Flash-Preview는 가격표도 벤치마크도 없이 자기 제품 안에서만 돌아갑니다

지난 9월 27일 MiniMax가 자사 코딩 에이전트 제품인 MiniMax Code 안에서 M3.1-Flash-Preview를 조용히 켰습니다. 모델 카드도 벤치마크 리포트도 공개 API 가격도 없습니다. MiniMax_Agent 계정의 X 공지는 "debuts today on MiniMax Code"와 "built for everyday development, fast, reliable, and ready for real work, from quick bug fixes to full features"가 전부입니다. OpenRouter에서는 이 모델을 찾을 수 없고 어디에도 값이 붙어 있지 않습니다. 공개된 사양은 컨텍스트 100만 토큰과 다섯 단계 추론 강도뿐입니다. low, medium, high, xhigh, 그리고 max입니다. [Startup Fortune](https://startupfortune.com/minimax-slips-a-new-coding-model-into-its-agent-tool-without-a-price-tag/) · [KuCoin News](https://www.kucoin.com/news/flash/minimax-launches-new-text-model-m3-1-flash-preview-for-code-development)

이보다 며칠 앞서 개발자들은 OpenRouter에 stealth/space-bunny-alpha라는 이름으로 올라온 무료 모델을 같은 백엔드로 지목했습니다. 오늘 같은 날 메이투안도 같은 방식을 썼습니다. LongCat-2.5-Preview를 OpenCode 안에 무료로 풀었고 컨텍스트 100만 토큰과 이미지 입력, 툴 호출을 내걸었습니다. 별도 벤치마크 결과는 아직 없습니다. OpenCode 카탈로그에도 이 모델의 사용량 데이터는 아직 한 줄도 없습니다. [AICrier](https://aicrier.com/post/wivb1rmn7olwac8316ox) · [OpenCode](https://opencode.ai/data/meituan/longcat-2.5-preview)

두 사건을 따로 보면 신모델 공지 두 건입니다. 같이 보면 다른 그림이 나옵니다. 두 중국 랩 모두 모델을 값이 매겨진 API로 파는 대신 자기 에이전트 제품의 기능으로 먼저 풀었습니다.

## MiniMax의 새 모델은 여러분 스택의 부품이 아니라 남의 제품 기능입니다

인디 개발자 입장에서 달라지는 것은 가격표의 유무가 아닙니다. 평가 순서입니다. 가격이 공개된 API라면 토큰당 비용과 지연 시간을 먼저 계산하고 그다음에 품질을 봅니다. 제품 안에만 들어 있는 모델은 그 계산을 할 수 없습니다. 과금 단위가 토큰이 아니라 구독이나 사용량 한도가 되고 실제 비용은 여러분의 워크로드가 그 제품 안에서 도는 동안에만 드러납니다.

M3.1-Flash-Preview에서 다섯 단계 추론 강도를 노출한 것도 이 맥락에서 읽힙니다. 보통 세 단계로 끝나는 노브를 다섯 단계로 늘렸다는 것은 비용과 지연을 작업 난이도에 맞춰 현장에서 조절하라는 요구를 랩이 인정한 셈입니다. 문제는 그 조절의 기준이 될 숫자를 랩이 공개하지 않았다는 점입니다.

그래서 오늘 할 수 있는 판단은 하나로 좁혀집니다. 여러분의 스택에서 코딩 모델이 바뀌었을 때 그 변화가 여러분 코드에 남는지 제품 안에 남는지를 확인하는 것입니다. 추론 호출이 여러분 서버를 떠나 남의 에이전트 제품 안에서만 일어난다면 모델 교체는 여러분의 결정이 아닙니다. 벤더의 릴리스 노트일 뿐입니다.

지금 시도해볼 만한 것은 세 가지입니다. M3.1-Flash-Preview가 매일 쓰는 작업에서 버티는지 여러분이 이미 돌리는 회귀 테스트 세트로 직접 재보는 것입니다. 무료 창이 열려 있는 LongCat-2.5-Preview도 같은 테스트로 나란히 놓고 이미지 입력이 실제로 값을 하는 작업이 있는지 확인해볼 수 있습니다. 어느 쪽이든 채택한다면 그 모델을 갈아끼울 수 있는 어댑터 경계를 먼저 만들어 두는 편이 낫습니다. 오늘 무료인 모델이 내일도 같은 조건이라는 보장이 없기 때문입니다.

## 오늘의 다른 소식

- **호주 상원, 알트만·아모데이 소환 요청**: OpenAI 에이전트의 정부 사이트 침해 이후 그린스 주도 상원 조사가 두 CEO에게 출석을 요청했습니다. [The Guardian](https://www.theguardian.com/australia-news/2026/sep/27/sam-altman-openai-dario-amodei-anthropic-senate-inquiry-medicare-hack-rogue-ai-agent-leak)
- **Stanford HomeBody, VLA 계층을 건너뛰다**: GPT-6 Astra가 Unitree G1을 직접 조종해 처음 보는 주방을 정리하고 애매한 요청에서 기억한 물건을 찾아옵니다. 환경별 학습 데이터는 쓰지 않았습니다. [Stanford TML](https://tml.stanford.edu/homebody/)
- **placeholder 도메인이 349개 에이전트 스킬에서 사기 페이지로**: yoursite.com과 your-domain.com이 GitHub 파일 약 35만 9천 개에 인용돼 있고 그중 일부가 macOS 방문자에게만 가짜 보안 경고를 보여줍니다. 텍스트 fetch로는 보이지 않습니다. [Hackread](https://hackread.com/placeholder-domains-ai-agent-skills-redirect-scams/)
- **"설명할 수 없는 실패"의 일상화**: LLM으로 빨라진 개발이 평가 파이프라인 없이 AI 기능을 내보내고 실패를 "그냥 별로임"으로 넘긴다는 에세이입니다. [i hate the future](https://www.ihatethefuture.com/2026/09/the-normalization-of-inexplicable.html)