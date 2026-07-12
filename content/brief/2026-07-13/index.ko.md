---
title: "AI·스타트업 모닝 브리프 - 2026-07-13"
date: 2026-07-13
summary: "Claude Code, 프롬프트 읽기도 전에 33K 토큰 소비 — OpenCode는 7K: Systima의 실측 벤치마크에 따르면 Claude Code는 사용자 프롬프트를 읽기 전에 이미 33,000 토큰을 소비한다. 같은 조건에서 OpenCode는 7,000 토큰. instruction 파일, MCP 서버, 서브에이전…"
description: "Claude Code, 프롬프트 읽기도 전에 33K 토큰 소비 — OpenCode는 7K: Systima의 실측 벤치마크에 따르면 Claude Code는 사용자 프롬프트를 읽기 전에 이미 33,000 토큰을 소비한다. 같은 조건에서 OpenCode는 7,000 토큰. instruction 파일, MCP 서버, 서브에이전…"
---

[브리핑/AI] AI·스타트업 모닝 브리프 - 2026-07-13

## 핵심 변화
- **Claude Code, 프롬프트 읽기도 전에 33K 토큰 소비 — OpenCode는 7K**: Systima의 실측 벤치마크에 따르면 Claude Code는 사용자 프롬프트를 읽기 전에 이미 33,000 토큰을 소비한다. 같은 조건에서 OpenCode는 7,000 토큰. instruction 파일, MCP 서버, 서브에이전트까지 추가하면 격차는 더 벌어진다. 코딩 에이전트를 프로덕션에 도입 중인 팀이라면 토큰 효율성이 인프라 비용의 핵심 변수가 될 전망. [Systima](https://systima.ai/blog/claude-code-vs-opencode-token-overhead)
<!--more-->
- **George Hotz의 균형 잡힌 AI 시각: "LLM은 사랑하지만 하이프는 싫다"**: 유명 해커이자 AI 창업자인 George Hotz가 LLM, 자율주행, 코딩 에이전트에 대한 진심 어린 기대를 밝히면서도, "기회의 창이 닫힌다"는 FOMO나 "모든 게 끝장난다"는 AI 둠(doom) 담론 양쪽 모두를 거부하는 글을 발표. 실무자 관점에서 과장된 내러티브를 경계하라는 신호. [geohot](https://geohot.github.io/blog/jekyll/update/2026/07/12/i-love-llms.html)
- **Uber, "로보택시 85%는 인간이 운전해야" 로비 — 자율주행 규제 전선 형성 중**: Wired가 입수한 문서에 따르면 Uber는 뉴저지주 의회에 인간 운전자와 로봇이 함께 운영되는 "하이브리드 네트워크" 법제화를 추진 중이다. 이는 자율주행 개발사보다 기존 ride-hailing 플랫폼에 유리한 구조. 모빌리티·자율주행 스타트업은 이 규제 프레임이 다른 주로 확산될지 주목해야 한다. [Wired](https://www.wired.com/story/ubers-autonomous-vehicle-strategy-slow-their-adoption/)

## 스타트업 / 제품 / 플랫폼 레이더
- **LARP — 창업자를 위한 매출 인프라 도구 출시**: 스프레드시트와 파편화된 툴을 대체할 목적으로 설계된 창업자용 매출/영업 인프라 도구. HN에서 97포인트를 기록하며 주목받았다. [LARP](https://www.larp.website/)
- **MCP 보안 현황 2026 — 첫 구조화된 보안 평가 발표**: Canopii가 Model Context Protocol(MCP)에 대한 첫 체계적 보안 평가 보고서를 공개. MCP가 AI-도구 연동의 사실상 표준으로 자리잡는 가운데, 보안 감사가 등장한 것은 생태계 성숙의 신호. [Canopii (HN)](https://news.ycombinator.com/item?id=48884647)
- **Adaptive Recall — MCP 기반 AI 메모리 서비스**: 벡터 검색을 넘어 인지과학 모델을 활용한 AI 메모리 시스템. MCP 프로토콜을 통해 AI 어시스턴트와 연동된다. [Adaptive Recall](https://www.adaptiverecall.com/)
- **Capn-hook — 코딩 에이전트의 중복 검색을 막는 도구**: 코딩 에이전트가 동일한 정보를 반복 검색하는 문제를 해결하기 위한 CLI 도구. 에이전트 작업 효율화에 실질적 도움. [GitHub](https://github.com/cyrusNuevoDia/capn-hook)

## AI가 바꾸는 미래 신호
- **코딩 에이전트 시장, '토큰 효율성'이 새로운 경쟁 축으로**: Claude Code와 OpenCode의 토큰 오버헤드 격차(4.7배)는 코딩 에이전트 시장의 경쟁 구도가 단순한 기능 차별화에서 인프라 비용 효율성으로 이동하고 있음을 보여준다. 1회 세션에 수만 토큰이 낭비된다면, 수백 명의 개발자가 사용하는 조직에선 연간 비용 차이가 수백만 달러 규모로 벌어질 수 있다. [Systima](https://systima.ai/blog/claude-code-vs-opencode-token-overhead)
- **MCP 생태계, 실험에서 프로덕션으로 전환 중**: 같은 날 MCP 보안 평가, MCP 기반 메모리 서비스, MCP 도구(코딩 에이전트 유틸리티)가 동시에 등장한 것은 프로토콜 생태계가 빠르게 성숙하고 있다는 신호. AI 에이전트를 도구·데이터와 연결하는 인프라 레이어가 형성되고 있다. [Canopii (HN)](https://news.ycombinator.com/item?id=48884647) · [Adaptive Recall](https://www.adaptiverecall.com/)

## 현실적인 기회 / 실험 아이디어
- **토큰 오버헤드 최적화 도구 또는 서비스**: Systima의 벤치마크가 보여주듯, 코딩 에이전트의 토큰 소비를 추적·최적화하는 도구는 팀 단위로 채택될 가능성이 높다. 특히 instruction 파일 최적화, 컨텍스트 윈도우 관리, MCP 서버 설정 튜닝을 패키징한 SaaS 제품은 실질적 비용 절감을 제공할 수 있다. [Systima](https://systima.ai/blog/claude-code-vs-opencode-token-overhead)
- **MCP 보안 스캐너/감사 도구**: MCP 서버를 운영하는 조직이 늘어나면서, MCP 연결의 보안 취약점을 자동으로 스캔하고 감사하는 도구는 새로운 틈새 시장이 될 수 있다. Canopii의 첫 보안 평가는 이 카테고리의 수요를 확인해준다. [Canopii (HN)](https://news.ycombinator.com/item?id=48884647)

## 불확실성 / 계속 볼 것
- **로보택시 규제의 주(州) 단위 확산 여부**: Uber의 뉴저지 로비가 성공하면 다른 주에서도 유사한 "하이브리드 네트워크" 법안이 제출될 가능성이 있다. 이는 Waymo, Tesla 등 자율주행 개발사와 기존 ride-hailing 플랫폼 간의 힘겨루기가 본격화되는 신호다. [Wired](https://www.wired.com/story/ubers-autonomous-vehicle-strategy-slow-their-adoption/)
- **코딩 에이전트 토큰 효율성 경쟁의 방향**: Claude Code가 OpenCode보다 4.7배 더 많은 토큰을 쓰는 이유는 설계 철학의 차이인가, 아니면 단순한 최적화 부족인가? 향후 Claude Code가 이 격차를 줄일지, 아니면 "더 많은 컨텍스트 = 더 나은 결과"라는 패러다임이 유지될지가 코딩 에이전트 도입 비용을 좌우할 변수. [Systima](https://systima.ai/blog/claude-code-vs-opencode-token-overhead)