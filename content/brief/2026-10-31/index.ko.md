---
title: "Cursor, Claude Code 확장 백도어"
date: 2026-10-31
summary: "Cursor 마켓플레이스에서 배포된 변조 Claude Code 확장 프로그램이 개발 기계에 SSH 키와 백도어를 심었습니다."
---

## Claude Code 확장 백도어, 공격자가 그 기계에서 본 것은 자격 증명 목록이었습니다

Cursor 마켓플레이스에서 배포된 변조 Claude Code 확장 프로그램이 개발 기계에 SSH 키와 백도어를 심었습니다.

대상은 macOS와 Windows용 `Anthropic.claude-code` 2.1.312와 2.1.313입니다. 10월 29일 02시 27분부터 13시 35분(태평양시)까지 약 11시간 배포됐습니다. 악성 코드는 정상 확장 프로그램 앞에 붙어 모듈을 불러올 때 실행됐습니다. Claude Code를 직접 열지 않아도 그대로 돌아갔습니다. Anthropic은 자사 시스템이나 직원 노트북이 침해된 건 아니고 공식 배포 경로의 버전은 영향이 없다고 밝혔습니다. Cursor 공지에는 영향 규모가 없고, 보도에서는 최대 5,000명으로 나왔습니다. [Cursor](https://cursor.com/blog/claude-code-extension-security-notice), [Phorion](https://phorion.io/blog/offical-claude-code-vsx-compromise/)

악성 코드는 그 기계에 무엇이 있는지도 세어서 보냈습니다. 사용자 이름과 기기 정보, 전역 Git 이메일도 보냈습니다. 환경 변수 이름 가운데 `KEY`, `TOKEN`, `SECRET`, `PASS`, `AWS`, `GCP`가 들어간 것은 최대 40개까지 골라 이름만 보냈습니다. 값은 보내지 않았습니다. 소스 코드나 비밀 값을 가져갔다는 증거로 읽을 수는 없습니다. 다만 다음에 무엇을 노릴지 정하는 목록은 그렇게 만들어집니다. 제품을 만드는 인디 개발자라면 오늘 자기 노트북에 어떤 키가 있는지 답할 수 있어야 합니다. 목록이 없으면 교체할 키도 정할 수 없습니다.

원격 접속은 구현 버그 두 개 때문에 대체로 뚫리지 않았습니다. macOS에서는 관리자 권한 오류를 SSH가 꺼진 상태로 잘못 읽어 SSH 켜기를 건너뛰었고, Windows에서는 PowerShell 설정을 `/bin/sh`로 실행하려 했습니다. SSH가 이미 켜져 있던 기계가 아니면 역방향 터널로 들어올 길이 없었습니다. 그래도 공격자의 SSH 키와 재실행 설정, 비컨은 그대로 남았습니다.

확장 프로그램을 지우는 것만으로는 백도어가 사라지지 않습니다. IDE를 닫아도 터널 재시도 프로세스가 남고, macOS에는 `~/Library/LaunchAgents/com.apple.sysmond.plist`, Windows에는 `SysMon` 예약 작업이나 시작 폴더 항목이 남습니다. 확장 프로그램은 IDE와 사용자 권한으로 돌아갑니다. 그래서 그 기계에서 쓰던 제품 자격 증명은 교체 대상입니다. 터널이 열리지 않았다는 사실만으로 키를 계속 써도 된다고 판단하기는 쉽지 않습니다.

Cursor는 배포를 막고 마켓플레이스를 점검해 다시 세웠고, 공격자 서버도 더는 작동하지 않는다고 밝혔습니다. 변조된 패키지가 어떤 경로로 마켓플레이스에 들어갔는지는 아직 설명이 없습니다. 노출 여부는 macOS에서 `grep -qs svc-telemetry ~/.ssh/authorized_keys`로 확인할 수 있습니다. 키가 나왔다면 확장 프로그램 삭제로 끝나지 않죠. Cursor가 배포한 정리 스크립트로 남은 것을 지우고, 그 기계의 자격 증명을 교체해야 합니다.

## 오늘의 다른 소식 (한 줄)

- **Northflank 자격 증명 교체 공지**: 보안 사고를 선언하고 모든 환경 변수가 복호화됐다고 가정해 비밀 값을 교체하라고 안내했습니다. 여러 사용자가 AI 키 무단 사용을 확인했습니다. [Northflank](https://status.northflank.com)
- **GLM 5.3의 Firefox 공격 체인**: Epoch AI는 공개 패치를 읽은 GLM 5.3이 Firefox 6개 버전의 작동하는 공격 체인을 만들었고, 버전당 API 비용은 약 1,000달러였다고 밝혔습니다. [The Decoder](https://the-decoder.com/open-weight-model-glm-5-3-built-full-firefox-exploit-chains-with-zero-human-input-in-under-48-hours/)
- **OpenAI의 AI 학습 선호 신호**: OpenAI는 여러 참여 업체에 학습 선호를 알리는 robots.txt 공통 신호를 향후 수개월 내 지원할 계획입니다. 기술 문서는 아직 Internet-Draft입니다. [OpenAI](https://openai.com/index/helping-websites-express-ai-training-preferences/)
- **AI 지출 우려에 기술주 하락**: 미국 기술주가 이틀 연속 하락했고 Intel은 28% 떨어졌습니다. Meta·Alphabet·Oracle·Amazon·Microsoft의 2026년 지출 약정은 합계 8,000억 달러입니다. [BBC](https://www.bbc.co.uk/news/articles/cvwy72e0n72yo)