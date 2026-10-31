---
title: "Claude 워터마크, 집필 보증 불가"
date: 2026-11-01
summary: "Anthropic이 Claude 구형 모델에도 고객이 끌 수 없는 텍스트 워터마크를 확대했습니다."
---

## Anthropic의 Claude 워터마크는 제품에서 끌 수 없습니다

Anthropic이 Claude 구형 모델에도 고객이 끌 수 없는 텍스트 워터마크를 확대했습니다.

이 표시는 모델 수준에서 글 자체에 들어갑니다. API로 만든 제품의 출력에도 붙고, 글을 복사해 다른 곳에 붙여 넣어도, 일부 편집을 거쳐도 남을 수 있습니다. Anthropic은 EU AI Act 제50조 2항의 AI 생성 콘텐츠 투명성 실천규약에 서명하고 이 방식을 적용하고 있습니다. 제품에서 따로 표시를 붙이지 않아도 출력에는 이미 들어 있으므로, 이 모델로 글을 만드는 기능이 고객에게 "사람이 쓴 글"이라고 안내할 근거는 없습니다. [Anthropic](https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content)

API 고객에게 보낸 이메일에서 새로 추가한 모델은 Claude Mythos 5, Opus 4.7, Opus 4.6, Sonnet 4.6입니다. 이 가운데 Opus 4.6과 Sonnet 4.6은 temperature, top_p, top_k가 모두 기본값일 때만 워터마크가 붙습니다. Anthropic은 워터마크에 의존해 규정을 준수하는 고객에게 이 기본값을 유지하라고 안내했습니다. 같은 이메일에서 Mythos 5와 Opus 4.7에는 이 조건을 붙이지 않았습니다. 제품에서 검출 결과를 쓰려면 어느 모델과 설정에서 붙은 표시인지도 확인해야 합니다. [The Decoder](https://the-decoder.com/anthropics-watermark-rollout-leaves-a-loophole-on-two-older-claude-models/)

하지만 표시가 검출돼도 Claude가 그 글을 썼다고 단정할 수 없습니다. Anthropic은 사람이 쓴 글을 Claude로 교정하거나 번역해도 결과에 워터마크가 붙는다고 설명합니다. 글의 생각과 초안을 사람이 만들었어도 Claude를 거쳤다는 표시가 남는 셈입니다. 따라서 제품이 검출 결과만 보고 고객의 글을 AI가 썼다고 판정하면, 교정이나 번역을 맡긴 글까지 그렇게 분류합니다.

표시가 없다고 사람이 썼다는 뜻도 아닙니다. Anthropic은 짧은 글에서는 신뢰할 만한 신호를 얻기 어렵고, 글을 많이 고치면 표시가 사라질 수 있다고 밝힙니다. 제품이 내놓은 글에서 워터마크를 찾지 못했다는 결과만으로 고객에게 사람이 쓴 글이라고 보증할 근거는 없습니다. 표시가 있든 없든 누가 썼는지 확정할 수 없으니, 글을 다듬어 주는 기능이 사람 글이라고 말할 근거도 없습니다.

검출 기능도 현재 EU 법에 따라 검증 의무가 있는 적격 기관과 기업을 대상으로 한 비공개 프리뷰입니다. Anthropic은 검출 API 접근을 점차 확대할 계획이라고 밝혔습니다. 제품에 바로 붙일 수 있는 판별 기능이라고 가정하면 안 됩니다. 검출 접근권을 얻어도 교정된 사람 글과 짧은 AI 글을 확실히 구분할 수 없다는 한계는 그대로입니다.

Anthropic은 Claude를 자체 제품에 넣는 개발자가 EU AI Act 제50조에 따른 제품과 서비스의 의무를 독립적으로 판단해야 한다고 명시했습니다. 모델에 워터마크가 있다는 사실만으로 제품의 의무를 다했다고 볼 수는 없습니다. 고객에게 보여 주는 판정 결과와 안내문에도, 워터마크만으로 사람이 썼다고 보증할 수 없다는 한계를 적어야 합니다.

## 오늘의 다른 소식 (한 줄)

- **OpenAI, 투자 유치 목표 미달**: 300억 달러를 목표로 한 투자 라운드에서 약 110억 달러를 확보했고, 기업가치도 목표였던 1조 4,000억 달러보다 낮은 1조 2,500억 달러였습니다. [TechCrunch](https://techcrunch.com/2026/10/31/openai-reportedly-lowers-funding-target-for-new-round/) [The Decoder](https://the-decoder.com/openai-raises-just-11-billion-of-its-30-billion-target-as-big-investors-lose-their-ai-appetite/)
- **Daybreak Blue 학습 정책 변경**: OpenAI는 11월 29일부터 사이버보안 세션 데이터를 모델 학습에 쓰겠다고 안내했다가 반발 뒤 별도 거부 옵션을 약속했지만, 안전 검토에서 표시된 상호작용은 안전 목적으로 계속 사용할 수 있습니다. [The Decoder](https://the-decoder.com/openai-plans-to-train-models-on-daybreak-blue-cybersecurity-session-data-that-was-previously-off-limits/)
- **VOLTA의 AI 피해자 평가**: Cisco Talos는 정보 탈취 악성코드 VOLTA가 훔친 자료를 LLM에 보내 피해자 자산의 수익화 가치를 매기고, 모델이 거부하면 다른 모델로 전환하는 기능을 분석했습니다. [Cisco Talos](https://blog.talosintelligence.com/appraisal-by-ai-model-driven-victim-prioritization-in-the-volta-infostealer/)
- **Prospero 코딩 하네스 공개**: Chris Wellons가 C++과 Dear ImGui로 만든 코딩 하네스를 공개했고, 모델은 기본으로 연결돼 있지 않아 사용자가 API나 llama.cpp를 직접 연결해야 합니다. [nullprogram](https://nullprogram.com/blog/2026/10/31/)