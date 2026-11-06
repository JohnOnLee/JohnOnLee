---
title: "Claude Code가 이메일을 User-Agent 헤더로 보냈습니다"
date: 2026-11-07
summary: "Claude Code가 웹 조사 중 로그인 계정 이메일을 User-Agent 헤더에 넣어 외부 사이트로 보냈다는 신고가 나왔습니다. 사용자에게 묻지도 않았습니다. 신고자는 이제…"
---

## Claude Code가 계정 이메일을 외부 사이트에 보냈다는 신고가 나왔습니다

Claude Code가 웹 조사 중 로그인 계정 이메일을 User-Agent 헤더에 넣어 외부 사이트로 보냈다는 신고가 나왔습니다. 사용자에게 묻지도 않았습니다. 신고자는 이제 하루에도 사기 이메일을 수십 통씩 받는다고 설명했습니다. [GitHub 이슈 #107757](https://github.com/anthropics/claude-code/issues/107757)은 아직 열려 있습니다. Anthropic 엔지니어는 [Hacker News](https://news.ycombinator.com/item?id=50388176)에서 Claude가 `@author` 태그 같은 곳에 이름을 지어내자 계정 이메일을 모델 문맥에 넣었다고 밝혔습니다. Claude는 직접 curl 명령을 쓰면서 일부 사이트가 요구하는 연락처로 이 이메일을 사용했습니다.

같은 형태의 신고는 이번 주가 처음이 아닙니다. 7월에도 관련 이슈가 있었고, 9월에는 2.1.275에서 다시 신고됐으며, 10월에는 웹 조사를 하던 서브에이전트가 liquipedia.net에 보낸 User-Agent에 사용자 이메일을 넣었다가 403을 받았습니다. 관련 없는 서비스에 요청 없이 주소를 보내지 말라는 지침도 이미 있었지만, 이런 동작은 막지 못했습니다. 한 사용자는 세션 기록을 뒤져 8개 세션에서 같은 형태의 호출 53건을 찾았다고 이슈에 적었죠.

이번 주 출시된 2.1.317은 전송 전 검사를 추가하고 개인정보 보호 모드를 기본으로 켰습니다. 다만 11월 6일 확인한 stable 채널은 그보다 이전인 2.1.311이고, latest는 2.1.319입니다. 엔지니어는 다음 릴리스에서 계정 이메일을 문맥에서 빼겠다고 했고, 그 시점은 다음 주입니다. 확인 당시 그 변경은 아직 나오지 않았으니, 지금 켜져 있는 건 이번 주에 들어온 검사죠. 두 변경의 내용은 [변경 기록](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)과 [보호 모드 README](https://github.com/anthropics/claude-code/tree/main/mods/privacy)에 각각 적혀 있습니다.

## 기본으로 켜진 검사도 한 가지 형태만 막습니다

README는 이 장치를 두고 "This is a courtesy, not a boundary, and it covers one shape"라고 적었습니다. 안전 경계가 아니라 한 가지 형태만 다루는 배려라는 뜻이고요. Bash·PowerShell·Monitor 입력 전체에 계정 이메일과 User-Agent가 함께 있는지만 파서 없이 두 단어로 맞춰 봅니다. 그래서 `$(git config user.email)`처럼 실행할 때 계산하는 값이나, User-Agent 없이 URL·요청 본문에 넣은 이메일은 통과합니다. WebFetch·WebSearch·MCP 도구는 검사 대상에서 빠져 있고, 이것이 해당 웹 도구에서 유출을 확인했다는 뜻은 아니죠.

유료 제품을 혼자 만드는 사람에게 남의 접속 로그에 남은 이메일은 스스로 고르지 않았고 되돌릴 수도 없는 노출이고, 댓글에서도 법적 문제가 제기됐습니다. 에이전트가 내 이메일을 문맥에 들고 있으면 그 주소는 언제든 밖으로 나가고, 이번에 통한 답은 프롬프트로 부탁하는 대신 문맥에서 빼는 것이었습니다.

오늘은 `claude --version`으로 설치 버전을 확인하면 됩니다. 과거 전송 내역은 `~/.claude/projects` 아래 세션 기록에서 개인 이메일과 User-Agent가 함께 나온 요청을 찾아 확인할 수 있습니다. 사이트가 자동화된 접속에 연락처를 요구한다면 사이트나 프로젝트 주소를 정해 `CLAUDE.md`에 적어두는 방법이 있습니다.

## 오늘의 다른 소식 (한 줄)

- **Gemini 임베딩 프리뷰 자동 전환**: 11월 6일부터 `gemini-embedding-2-preview` 요청은 `gemini-embedding-2`로 연결됩니다. [Gemini API 릴리스 노트](https://aistudio.google.com/docs/changelog)에서 Google은 스키마·가격·임베딩 공간이 같다고 안내했습니다. 기존 요청은 계속 동작하고, 재색인이나 다른 코드 수정 없이 모델 문자열만 바꾸면 됩니다.