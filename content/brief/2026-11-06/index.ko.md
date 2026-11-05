---
title: "OpenSSH 10.6p2, AI 버그 보고가 릴리스 주기를 당겼습니다"
date: 2026-11-06
summary: "OpenSSH가 2026년 11월 5일 10.6p2를 내고 비밀번호 인증 우회를 막았습니다. 공격자는 SSH 포트로 붙어 257~1024바이트짜리 긴 비밀번호를 한 번 보내면 되고, 어떤…"
---

## OpenSSH 10.6p2는 비밀번호 인증 우회를 막았습니다

OpenSSH가 2026년 11월 5일 10.6p2를 내고 비밀번호 인증 우회를 막았습니다. 공격자는 SSH 포트로 붙어 257~1024바이트짜리 긴 비밀번호를 한 번 보내면 되고, 어떤 비밀번호인지 몰라도 재시도 없이 로그인이 됩니다. 비밀번호가 없는 계정이 접속 가능한 상태가 되는데, 같은 서버에 비밀번호를 가진 계정이 하나만 있어도 이런 일이 생깁니다. 공격자가 미리 알아야 하는 건 비밀번호가 없는 쪽의 계정 이름이죠. [Alpine Linux](https://alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/)

musl libc를 쓰고 PAM 없이 sshd를 실행할 때 생기는 버그입니다. Alpine에서는 `PasswordAuthentication yes`가 켜져 있고, 비밀번호 필드가 `*`인 계정과 `$5$` 또는 `$6$` 해시를 가진 다른 계정이 함께 있어야 합니다. `PasswordAuthentication yes`는 OpenSSH 기본값이고, `*`는 키로만 로그인하는 계정에서 정상적으로 쓰는 값입니다. Alpine 기본 이미지의 root도 여기에 해당하고요. 긴 비밀번호를 처리하다 musl의 `crypt()`가 오류 표시로 돌려준 `*`를 sshd가 저장된 비밀번호와 일치한다고 받아들입니다. PAM을 켠 sshd는 영향이 없는 것으로 안내됐고, `PasswordAuthentication no`로 둔 시스템이나 컨테이너 안에서 sshd를 실행하지 않는 경우도 빠집니다.

OpenSSH는 같은 릴리스 노트에서 AI 모델이 찾았거나 AI의 도움으로 작성한 보안 버그 보고를 많이 받고 있는데, 현실적인 공격 조건에서는 보안 영향이 없는 보고도 많다고 밝혔습니다. 그런데 AI 도구가 찾은 버그를 다른 연구자가 독립적으로 다시 발견한 사례도 있었고요. 신고하지 않는 공격자도 같은 버그를 찾을 수 있다고 보고, 수정본을 다음 예정 릴리스까지 모아두지 않고 더 자주 내기로 했습니다([OpenSSH release notes](https://www.openssh.org/releasenotes.html)). 하루 전인 11월 4일에는 [OpenAI](https://openai.com/index/a-thousand-fewer-paths-to-root/)가 자사 파이프라인으로 Linux 커널의 로컬 권한 상승 취약점 948개를 찾아 검증하고 패치를 만들었다고 발표했습니다. 통제된 연구 환경에서 얻은 OpenAI 자체 수치이고, 공격에는 이미 시스템에 접근한 상태가 필요했거든요.

## 혼자 운영하는 제품은 OpenSSH 공지가 뜬 날 패치와 재시작을 끝내야 합니다

혼자 서버를 굴리며 유료 제품을 운영한다면 패치 시점을 분기마다로 잡아둔 계산도 바뀝니다. 분기마다 배포판 업데이트 일정을 확인하는 대신, OpenSSH 릴리스 노트를 보고 그날 처리하는 쪽으로 옮길 이유가 생겼습니다. 개발자가 AI 버그 보고를 받아 수정본을 일찍 내도 운영자가 다음 분기까지 기다리면, 그 서버에서는 여전히 수정 전 코드가 실행되는 거죠.

여기에 드는 일은 두 가지입니다. OpenSSH 릴리스 공지를 확인하고, 운영 중인 서버가 해당 조건이면 그날 업데이트와 재시작까지 끝내는 것입니다. Alpine 안내문은 패키지만 업그레이드해도 실행 중인 데몬은 바뀌지 않는다고 명시했는데, 파일은 새 버전이어도 기존 sshd는 그대로인 겁니다. 재시작해야 새 코드가 실제 접속을 받는 sshd에 올라가죠.

## 오늘의 다른 소식 (한 줄)

- **GPT-6 Cyber**: OpenAI의 첫 'Critical' 등급 사이버 모델은 일부 Daybreak Red 고객에게만 API와 Codex로 제공되므로, 보안 기능 설계에서 일반 API 계정으로 쓸 수 있다고 가정하면 안 됩니다. [OpenAI](https://openai.com/index/introducing-gpt-6-cyber/)
- **Conductor**: Meta에 인수된 뒤 클라우드는 11월 13일 읽기 전용으로 바뀌고 11월 20일 종료와 데이터 삭제가 시작되므로, 사용자는 13일 전에 워크스페이스를 로컬 앱으로 옮기거나 데이터를 내보낼 필요가 있습니다. [InfoWorld](https://www.infoworld.com/article/4245065/meta-acquires-conductor-as-ai-coding-shifts-toward-multi-agent-development.html)
- **Railway**: 위조된 Railway 소스 IP의 스캔으로 생긴 외부 네트워크 차단이 11월 5일 18:51 UTC에도 일부 남아 있어, 접속 장애를 살필 때 앱 코드 밖의 IP 차단도 확인할 필요가 있습니다. [Railway](https://status.railway.com/incident/QBCLHG1V)