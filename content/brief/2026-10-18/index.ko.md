---
title: "DeepSeek V4.1 Flash 1017, 새 모델을 같은 API 이름으로"
date: 2026-10-18
summary: "10월 17일 DeepSeek이 DeepSeek-V4.1-Flash-1017을 공개했고, 9월 10일에 나온 V4.1 Flash의 마이너 업데이트라고 설명했습니다. 같은 작업을 더 짧은 실행 시간과 더…"
---

## DeepSeek이 V4.1 Flash 1017을 내고 검색 API까지 열었습니다

10월 17일 DeepSeek이 DeepSeek-V4.1-Flash-1017을 공개했고, 9월 10일에 나온 V4.1 Flash의 마이너 업데이트라고 설명했습니다. 같은 작업을 더 짧은 실행 시간과 더 적은 출력으로 끝내게 됐다는 얘기입니다. API 이름과 가격은 그대로죠. `deepseek-flash`를 호출하면 새 모델이 응답하고, 예전 이름인 `deepseek-v4-flash`와 `deepseek-v4-flash-vision-exp`는 은퇴해서 요청이 같은 새 모델로 넘어갑니다. [DeepSeek 변경 로그](https://api-docs.deepseek.com/updates)

가격은 100만 토큰 기준으로 입력 캐시 적중이 비피크 $0.003, 피크 $0.006이고 캐시 미스가 비피크 $0.15, 피크 $0.3이며 출력은 비피크 $0.6, 피크 $1.2입니다. 컨텍스트는 100만 토큰에 최대 출력 384K, 이미지 입력도 됩니다. 같은 날 사내 검색 엔진을 붙인 Search와 Fetch API를 열었고, 1,000건이 성공했을 때 $0.75이니 검색 벤더를 따로 붙이지 않아도 됩니다. [Search & Fetch 가이드](https://api-docs.deepseek.com/guides/search/)

성능 숫자는 모두 DeepSeek이 직접 잰 값이고, Terminal-Bench는 Claude Code 하네스로, DeepSWE는 Mini-SWE-V2로 쟀습니다. Terminal-Bench 4.0은 31.2에서 42.3, DeepSWE v1.1은 74.2에서 77.0, HLE는 도구 없이 42.6. MIT 라이선스 가중치는 같은 날 Hugging Face에 올라왔고, 저장소 파일은 510GB쯤 되며 해커뉴스에서는 600점을 넘겼습니다. [Hugging Face](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)

## 코드를 그대로 두어도 다음 주에는 다른 모델이 응답합니다

빌더 쪽에서 실제로 달라진 건 점수가 아닙니다. 여러분의 코드가 부르는 이름은 그대로인데 그 이름이 가리키는 모델이 바뀌었습니다. 가격표도 청구서도 그대로. 프롬프트를 손댄 적 없이 출력이 달라졌다면 원인이 여기 있을 수 있습니다.

다시 재야 할 값은 두 가지인데, 먼저 자기 하네스에서 평가를 돌려야 합니다. 공개된 숫자는 DeepSeek이 자기 하네스로 잰 값이고 Terminal-Bench는 Claude Code, DeepSWE는 Mini-SWE-V2로 쟀으니 여러분의 에이전트 루프와는 다릅니다. 다음은 캐시 단가입니다. 입력 캐시 적중이 100만 토큰에 $0.003, 미스가 $0.15로 같은 토큰에 50배 차이가 나는데, 시스템 프롬프트와 도구 스키마를 앞쪽에 고정해 두는 것만으로 청구서가 달라집니다.

모델을 직접 돌릴 생각이라면 라이선스보다 크기를 먼저 봐야 합니다. MIT라서 상업적 사용에는 제약이 없지만, 8비트와 FP8 형식을 받아도 저장소가 510GB라 노트북에서는 돌지 않습니다. 날짜가 붙은 모델 ID를 노출하는 경로로 옮기면 버전을 고정할 수 있습니다.

Search와 Fetch는 기존 검색 벤더를 대체할 만한 값이니, 검색 호출이 많은 에이전트라면 지금 쓰는 비용과 비교해 볼 만합니다. 다만 색인 범위와 한국어 결과 품질은 직접 확인해야 하는데 공개된 평가가 아직 없습니다.

성능 숫자는 모두 벤더 자체 측정이고 제3자 재현은 나오지 않았습니다. 다음 업데이트도 이번처럼 API 이름과 가격을 그대로 둔 채 올 수 있습니다.

## 오늘의 다른 소식 (한 줄)

- **OpenCode 침해, 저장해 둔 API 키 노출**: 레거시 시스템에 무단 접근이 있었고 콘솔 사용자 1.4%가 저장한 OpenAI·Anthropic·Google 키가 노출됐다고 OpenCode가 10월 17일 알렸으며 연결된 계정에서 예상치 못한 과금이 보고됐습니다. [Blockonomi](https://blockonomi.com/opencode-security-breach-exposes-api-keys-of-1-4-of-console-users/)
- **Replit, 기본 모델을 OpenAI로 교체**: 암자드 마사드가 TechCrunch Disrupt에서 Anthropic과 더 이상 일하지 않는다고 말했고, ChatGPT가 Replit Agent의 기본값이 되며 Claude는 선택지로 남습니다. [TechCrunch](https://techcrunch.com/2026/10/17/replit-is-no-longer-working-with-anthropic-ceo-says/)
- **Vercel AI Gateway, V4.1 Flash 1017 추가**: 같은 날 AI Gateway에도 올라왔습니다. [Vercel Changelog](https://vercel.com/changelog/deepseek-v4-1-flash-1017-now-available-on-ai-gateway)