---
title: "엔비디아, 허깅페이스 129억 달러 인수"
date: 2026-09-05
summary: "엔비디아가 오픈소스 AI 허브 허깅페이스를 129억 3천만 달러에 인수하기로 했다. 9월 3일 젠슨 황 블로그 글로 공식 확인됐고, 허깅페이스는 모델 300만 개, 앱 100만…"
---

## 엔비디아가 9월 3일 허깅페이스를 129억 3천만 달러에 사기로 했고 개발자의 모델 허브가 칩 제조사 품에 들어왔다
- **계약 규모와 대상**: 엔비디아가 오픈소스 AI 허브 허깅페이스를 129억 3천만 달러에 인수하기로 했다. 9월 3일 젠슨 황 블로그 글로 공식 확인됐고, 허깅페이스는 모델 300만 개, 앱 100만 개, 데이터셋 50만 개를 호스팅하며 개발자 1천 8백만 명이 쓴다. [TechCrunch](https://techcrunch.com/2026/09/03/nvidia-confirms-it-will-buy-hugging-face-for-12-9-billion/) · [NVIDIA](https://blogs.nvidia.com/blog/nvidia-to-acquire-hugging-face/)
- **중립성 약속**: 황은 "허깅페이스는 AI 생태계 전체의 오픈 플랫폼으로 남는다"며 "개발자가 원하는 모델, 프레임워크, 클라우드, 추론 서비스, 컴퓨팅 플랫폼을 고르고, 엔비디아 컴퓨팅은 필수가 아니다"라고 했다. 허깅페이스 CEO 클레망 들랑그가 황을 수 주 앞서 직접 찾아간 것으로 알려졌다. [CNBC](https://www.cnbc.com/2026/09/03/nvidia-agrees-to-buy-hugging-face-for-almost-13-billion-ai-expansion.html) · [The Guardian](https://www.theguardian.com/technology/2026/sep/03/nvidia-to-buy-hugging-face-in-129bn-deal)

## 당신의 기본 모델 허브 주인이 거대 칩 제조사로 바뀌었고 이제 '중립성'이 스택 전체를 좌우한다
- **내 스택에 닿는 곳**: 허깅페이스는 모델 다운로드와 배포, 데이터셋, 추론 API의 기본 창구다. 이 창구의 주인이 GPU를 파는 회사로 바뀌면, 같은 GPU를 안 쓰는 제품도 그 회사의 상품에 끌리는 경로에 놓인다. 지금은 '약속'만 믿어야 하는 시점이다.
- **오픈소스의 선언**: 칩 제조사가 오픈 허브를 지른 것은 개방 모델의 승리처럼 보이지만, 동시에 대형 플랫폼이 오픈 생태계의 요충지를 무력으로 사는 사례다. 인디는 어느 쪽 해석이 맞는지 제품에서 확인하게 된다.

## 오늘 당신의 배포 파이프라인을 하나의 허브에 묶지 말고 이탈 경로를 미리 만들어라
- **실험 1, 허브를 두 곳 쓰기**: 모델과 데이터셋을 허깅페이스에만 두지 말고, 다른 저장소나 자체 저장에 미러를 걸어라. 배포 계층과 모델 리포지토리의 결합을 풀면 허브 정책이 바뀌어도 흔들리지 않는다.
- **실험 2, 추론 벤더를 한 곳으로 몰지 않기**: 엔비디아 불가피성에 대비해 추론 API를 표준 인터페이스 위에 얹고, 벤더 전환을 코드 몇 줄로 되게 설계하라. 칩 유불리가 생겨도 구조는 그대로 남는다.

## 계약이 규제 심사를 지나야 하고 중립성이 실제로 지켜질지는 아직 미지수다
- **보류할 결정**: 인수는 미국과 유럽에서 필수 반독점 심사를 거친다. 승인 전까지 허깅페이스의 소유 구조가 바뀔 수 있으므로, 이제 허브를 사업상 확고한 자산으로 셈하지 말 것.
- **계속 볼 것**: 엔비디아 컴퓨팅이 필수가 아니라 유리한 선택으로 남는지, 다중 가속기 지원 약속이 실제 API와 가격에 반영되는지 지켜봐라. 중립성이 마케팅 문구로 끝나면 이탈 준비가 답이 된다.

## 오늘의 다른 소식 (한 줄)
- **구글 딥마인드, 기상 모델 WeatherNext 3 공개**: 시간 단위로 갱신되는 5km 해상도 예보를 내며 검색, 지도, 제미니에 들어간다. [Google blog](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/introducing-weathernext-3/)
- **퀄컴 벤처스, 울트라휴먼에 7000만 달러 투자**: 스마트링을 자체 AI 계산 기기로 바꾸는 3.65억 달러 밸류 라운드다. [TechCrunch](https://techcrunch.com/2026/09/03/qualcomm-backs-ultrahuman-in-70m-round-on-bet-to-turn-smart-rings-into-computers/)
- **웨이퍼, 추론 최적화로 4000만 달러 시리즈 A**: AI 추론 성능 최적화 플랫폼에 투자가 몰린다. [AI Market Watch](https://www.ai-market-watch.com/news/ai-inference-optimization-startup-wafer-raises-40-million-series-a-iw10en)