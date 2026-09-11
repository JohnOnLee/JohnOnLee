---
title: "OpenAI Agents API 공개 베타"
date: 2026-09-12
summary: "공개 베타인 Agents API는 세션과 오케스트레이션, 컨텍스트 압축, 복구를 맡는다. 개발자는 모델과 도구, 실행 환경을 정하며 자체 인프라도 선택할 수 있다."
---

## OpenAI가 Codex 실행 하네스를 Agents API로 내놨다
- **에이전트 실행부를 관리형 API로 제공한다**: 공개 베타인 Agents API는 세션과 오케스트레이션, 컨텍스트 압축, 복구를 맡는다. 개발자는 모델과 도구, 실행 환경을 정하며 자체 인프라도 선택할 수 있다. [InfoWorld](https://www.infoworld.com/article/4221163/openai-launches-managed-agents-api-to-simplify-enterprise-ai-agent-development.html)

## 인디 개발자는 에이전트 기능에 더 빨리 집중할 수 있다
- **직접 운영할 부분이 줄어든다**: 작업 큐와 상태 DB, 샌드박스, 재시도 정책을 따로 만들 필요가 줄어든다. 대신 모델부터 실행 제어까지 OpenAI에 맡기면 다른 공급자로 옮기기 어려워질 수 있다.

## 장시간 작업 하나로 먼저 검증해볼 만하다
- **중단과 복구를 직접 시험한다**: 실제 작업을 중간에 끊은 뒤 다시 시작해서 상태가 얼마나 남는지 확인하고, 재시도 비용과 완료 시간을 기록해보면 된다. 같은 작업을 다른 공급자로 옮길 때 보존할 수 있는 상태도 함께 확인하는 편이 낫다.

## 공개 베타라서 운영 기준을 확정하기는 이르다
- **자체 실행 환경에서도 세션은 OpenAI 방식에 묶인다**: 코드를 자체 인프라에서 실행해도 세션과 컨텍스트 압축, 복구 방식은 OpenAI API에 묶인다. 실제 장애 처리와 장기 세션 비용을 확인하기 전에는 핵심 작업 전체를 옮기지 않는 편이 안전하다.

## 오늘의 다른 소식 (한 줄)
- **DeepSeek가 V4.1 Flash를 공개했다**: 새 causal encoder-decoder와 네이티브 비전을 넣고 KV 캐시 부담을 줄인 모델이다. [The Register](https://www.theregister.com/ai-and-ml/2026/09/11/deepseeks-new-model-sets-a-template-for-powerful-llms-that-run-lean/5295715)
- **OpenAI가 GPT-Live-1 API를 출시했다**: 양방향 음성과 끼어들기, 백엔드 모델·도구 위임을 지원하며 음성 프런트엔드 요금은 분당 0.05달러다. [GIGAZINE](https://gigazine.net/gsc_news/en/20260911-gpt-live-1/)
- **Anthropic이 Claude 악용 사례를 공개했다**: 회사는 무기 개발과 사이버 작전, 감시, 사기에 Claude를 쓴 활동을 찾아 차단했다고 밝혔다. [Reuters](https://www.reuters.com/world/china/how-anthropic-says-claude-was-used-weapons-spying-cyber-operations-2026-09-11/)