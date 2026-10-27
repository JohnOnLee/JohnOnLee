---
title: "Genie 4, 게임 엔진 앞단에 도착한 실시간 월드 모델"
date: 2026-10-28
summary: "10월 27일 Google DeepMind가 실시간으로 돌아가는 월드 모델 Genie 4를 공개했습니다. 지난해 Genie 3와 다른 점은 소리입니다. 바람 소리와 음악, 사람의 대화를 월드와…"
---

## Genie 4는 말로 장면을 바꾸고 소리까지 같이 만듭니다

10월 27일 Google DeepMind가 실시간으로 돌아가는 월드 모델 Genie 4를 공개했습니다. 지난해 Genie 3와 다른 점은 소리입니다. 바람 소리와 음악, 사람의 대화를 월드와 동시에 생성합니다. 플레이 도중에 문장을 넣으면 장면이 그 자리에서 바뀌고요. [Google](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/introducing-genie-4/) [TechCrunch](https://techcrunch.com/2026/10/27/googles-genie-4-world-model-adds-audio-more-realistic-worlds-and-real-time-steering/)

Gemini 계열 위에서 돌아갑니다. Gemini Omni가 사물의 생김새와 움직임을 실제처럼 붙잡아 두고, 다른 Gemini 모델이 장면이 무너지지 않도록 추론을 맡습니다. "비가 오게 해줘" 같은 문장을 넣으면 주변 장면에 맞춰 반영되고, 입력이 없을 때도 장면은 계속 굴러갑니다. 공기역학과 충돌 같은 물리, 사람의 자연스러운 움직임과 대화도 함께 만들어집니다.

장면을 검증하는 일도 Gemini가 맡습니다. 목표를 단계로 쪼개고 프레임을 확인하는 감독 역할입니다. Gemini Robotics와 묶은 실험에서는 Gemini 4 Argon이 로봇 과제를 단계로 나누고, Genie 4가 그 단계를 실시간으로 시뮬레이션했습니다.

아직 아무나 쓸 수는 없습니다. 신뢰 테스터를 대상으로 한 리서치 프리뷰로 시작하고, 다음 차례는 Google AI Ultra 구독자의 Project Genie와 Gemini API, AI Studio 얼리액세스 파트너입니다. 장면이 일관되게 유지되는 시간은 최대 2분으로 Genie 3의 두 배입니다. 시뮬레이션이 길어질수록 사물과 세부가 흐트러지고, 월드 안 글자를 제대로 그리는 일도 아직 남았습니다.

## 엔진 코드를 쓰기 전에 확인하는 자리를 가져갑니다

DeepMind가 공개한 테스터 사례에서 게임 개발자는 엔진 코드를 한 줄도 쓰기 전에 프롬프트로 스타일과 소재, 조작감을 확인합니다. 아이디어에서 탐색 가능한 프로토타입까지 몇 초면 도달한다는 게 회사 설명입니다. 인디 개발자에게 이 모델은 게임 엔진을 대체하는 도구가 아닙니다. 엔진 코드를 쓰기 전에 아이디어를 버릴지 말지 판단하는 자리에 들어옵니다. 재미없는 안을 기획 단계에서 몇 초 만에 걸러낼 수 있다면, 그 실패의 값이 훨씬 싸집니다.

물체가 사라지거나 모양이 바뀌는 장면 위에 게임 상태를 두면 버그를 고칠 방법이 없습니다. 상태와 규칙, 세이브 파일은 계속 엔진이 갖고 있어야 합니다. 월드 모델은 그럴듯한 장면을 즉석에서 만드는 데 강합니다. 그 장면이 2분을 넘어서도 버티는지는 아직 보장되지 않고요.

지금 접근권이 없어도 준비할 수 있는 게 있습니다. Genie 4가 쓴 방식은 화면을 보고, 목표를 단계로 쪼개고, 각 단계가 실제로 됐는지 다시 확인하는 반복입니다. 이 반복은 스크린샷과 지금 쓰는 모델로도 만들 수 있습니다. 내 제품의 핵심 화면 몇 개를 골라 "이 상태가 되면 성공"이라는 문장을 적어두고, 모델이 그 문장을 확인하게 하는 것부터 시작해볼 만합니다. 생성된 장면을 제품에 넣을 계획이라면 2분을 넘길 때 무엇이 먼저 흐트러지는지부터 재보면 됩니다.

## 오늘의 다른 소식 (한 줄)

- **Stanford Daily: Anthropic이 스탠퍼드 교수들의 책을 복제해 Claude 학습에 썼습니다**: 5월 Bartz 판결로 15억 달러 합의가 끝난 뒤에도 Tobias Wolff, Chang-rae Lee 교수는 합의에서 빠져 Cruz v. Anthropic 소송을 이어가며 작품당 최대 15만 달러 배상을 요구합니다. [Stanford Daily](https://stanforddaily.com/2026/10/27/professors-books-pirated-to-train-claude/)
- **Apple이 M6 14인치 맥북 프로를 발표했습니다**: 12코어 CPU와 12코어 GPU, GPU마다 뉴럴 액셀러레이터가 들어가고 M5보다 AI 작업이 최대 25% 빠릅니다. 10월 28일 선주문, 11월 6일 판매 시작입니다. [Apple](https://www.apple.com/newsroom/2026/10/apple-introduces-the-new-14-inch-macbook-pro-with-m6/)
- **터미널 Ghostty가 1.4.0을 냈습니다**: 7개월, 172명 기여, 2,889개 커밋이고 Kitty 그래픽스 규격을 애니메이션과 상대 배치까지 100% 구현한 첫 비-Kitty 터미널입니다. [Ghostty](https://ghostty.org/docs/install/release-notes/1-4-0)
- **Discord가 공개 서버 대화를 웹 검색에 노출합니다**: 11월 16일부터 모든 Discoverable 서버에 웹 페이지가 생기고, 12월 중순부터 공개 채널 메시지가 검색에 걸릴 수 있습니다. 관리자는 Server Settings > Web Presence에서 채널을 뺄 수 있습니다. [Discord](https://discord.com/blog/making-content-from-discoverable-servers-easier-to-discover)