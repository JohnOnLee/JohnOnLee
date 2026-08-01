---
title: "이 사이트를 만든 방법: Hugo + PaperMod를 에디토리얼 사이트로"
date: 2026-08-02
summary: "테마를 포크하지 않고 홈 오버라이드, CSS 변수 팔레트, 다크모드 대응, 한글 타이포까지 — 이 사이트에 실제로 적용한 커스텀을 코드 그대로 정리했습니다."
---

기성 테마로 시작한 사이트에는 어딘가 '기성 테마 티'가 납니다. 이 사이트도 얼마 전까지 [PaperMod](https://github.com/adityatelange/hugo-PaperMod) 기본 화면 그대로였습니다. 지금 보시는 에디토리얼 홈과 통일된 본문 스타일은 하루 동안의 커스텀 작업의 결과이고, 이 글은 그 과정을 코드 그대로 정리한 것입니다.

원칙은 하나였습니다. **테마를 포크하지 않는다.** 테마는 서브모듈로 두고 업데이트를 계속 받으면서, 사이트 레벨 파일로만 이깁니다. Hugo가 같은 경로의 사이트 파일을 테마 파일보다 우선하기 때문에 가능한 방식입니다. 덕분에 이 사이트의 커스텀은 파일 몇 개가 전부입니다:

```
layouts/index.html              ← 홈 전체 교체
data/home/ko.yaml, en.yaml      ← 홈 카피 (언어별)
assets/css/extended/home.css    ← 홈 스타일
assets/css/extended/custom.css  ← 나머지 페이지 통일
```

전제는 Hugo 사이트 + PaperMod 서브모듈 + GitHub Pages 배포입니다. 기본 설치는 [PaperMod 위키](https://github.com/adityatelange/hugo-PaperMod/wiki/Installation)가 잘 정리돼 있어 생략합니다.

## 1. 홈은 통째로 교체한다

`layouts/index.html` 파일 하나를 만들면 홈 전체가 내 것이 됩니다. 테마의 홈 템플릿은 건드리지 않습니다.

이때 카피(문구)를 마크업에 박지 말고 데이터 파일로 분리하는 게 핵심입니다. 이중언어 사이트라면 템플릿 하나로 두 언어를 처리할 수 있습니다:

```html
{{- $copy := index .Site.Data.home .Site.Language.Lang -}}
{{- $posts := first 4 (where .Site.RegularPages.ByDate.Reverse "Section" "blog") -}}

<section class="editorial-hero">
  <p class="editorial-eyebrow">{{ $copy.hero.eyebrow }}</p>
  <h1>{{ range $i, $line := $copy.hero.titleLines }}{{ if $i }}<br>{{ end }}{{ $line }}{{ end }}</h1>
  <p class="editorial-intro">{{ $copy.hero.intro }}</p>
</section>
```

`data/home/ko.yaml`에는 문구만 남습니다:

```yaml
hero:
  eyebrow: "아이디어 · 제품 · 기회"
  titleLines:
    - "아이디어가 제품이 되고,"
    - "제품이 새로운 기회가 되도록."
```

문구를 바꿀 때 템플릿을 열지 않게 되고, 언어 추가도 yaml 파일 하나로 끝납니다. 최신 글은 위 코드처럼 섹션에서 동적으로 뽑습니다 — 콘텐츠가 없을 때를 대비해 `{{ else }}` 빈 상태까지 처리해두면 섹션이 비어도 깨지지 않습니다.

## 2. 나머지 페이지는 CSS 변수로 통일한다

글·목록 페이지까지 다시 만들 필요는 없습니다. PaperMod는 모든 색을 CSS 변수로 쓰기 때문에, 변수만 갈아끼우면 사이트 전체의 톤이 바뀝니다. `assets/css/extended/` 아래의 CSS는 테마가 자동으로 번들하니 테마 수정도 필요 없습니다:

```css
:root {
  --theme: #fbfaf7;      /* 종이색 배경 */
  --entry: #f1f3f2;
  --primary: #1b1d1f;
  --secondary: #676b70;
  --border: #dddcd7;
}

:root[data-theme="dark"] {
  --theme: #151617;
  --primary: #f0efeb;
  --secondary: #a9adb2;
  --border: #333638;
}
```

제목만 세리프로 바꾸면 에디토리얼 인상이 절반은 완성됩니다:

```css
.post-title,
.page-header h1,
.entry-header h2 {
  font-family: var(--j-serif);
  font-weight: 400;
}
```

목록의 카드 박스를 플랫한 구분선 행으로 바꿀 때 함정이 하나 있습니다. PaperMod의 `.post-entry`에는 `border: 1px solid`가 **4면에** 걸려 있어서, `border-bottom`만 덮어쓰면 나머지 3면이 남아 유령 외곽선이 생깁니다:

```css
.post-entry {
  background: transparent;
  border: 0;                                /* 먼저 전부 끄고 */
  border-bottom: 1px solid var(--border);   /* 아래만 다시 */
}
```

## 3. 다크모드는 data-theme다 (body.dark가 아니라)

인터넷의 오래된 PaperMod 커스텀 예제들은 `body.dark`에 다크 스타일을 겁니다. **최신 PaperMod에서는 조용히 죽습니다.** 지금 버전은 `<html>`의 `data-theme` 속성을 JS로 세팅하는 방식입니다. 이 사이트도 처음에 이 함정에 걸려서 다크모드가 통째로 안 먹었습니다.

```css
:root[data-theme="dark"] {
  /* 다크 팔레트 */
}

/* JS가 꺼진 방문자는 data-theme="auto"로 남는다 — 시스템 설정을 따라가게 */
@media (prefers-color-scheme: dark) {
  :root[data-theme="auto"] {
    /* 같은 다크 팔레트 */
  }
}
```

라이트/다크/시스템 자동, 세 모드를 전부 확인해야 합니다.

## 4. 한글은 keep-all 한 줄이 절반이다

한글 사이트에서 "1,200포\n인트"처럼 단어 중간이 잘리는 줄바꿈은 CSS 한 줄로 막습니다:

```css
body {
  word-break: keep-all;        /* 한글: 단어 중간에서 줄바꿈 금지 */
  overflow-wrap: break-word;   /* 긴 URL 등의 탈출구 */
}
```

`keep-all`은 CJK에만 작동하므로 영문에는 영향이 없습니다. 본문에만 걸지 말고 `body`에 걸어야 제목·목록·홈까지 전부 적용됩니다.

세리프 폰트의 현실도 알아두면 좋습니다. 한글 세리프는 시스템 폰트 폴백이 기기마다 제각각입니다 — macOS는 붓글씨풍, Windows는 바탕체, Android는 아예 고딕으로 떨어집니다. 기기 간 일관성이 브랜드에 중요하다면 Noto Serif KR을 서브셋 woff2로 셀프호스팅하는 게 답입니다. 이 사이트는 아직 폴백을 수용하고 있습니다.

## 5. 검색엔진이 읽는 두 가지를 미리 챙긴다

**제목.** "모닝 브리프 - 2026-08-01" 같은 날짜만 다른 반복 제목은 목록에서도 검색결과에서도 죽습니다. 이 사이트는 자동 발행 글의 제목을 그날의 첫 헤드라인으로 바꿨습니다. 날짜는 메타와 URL에 이미 있습니다.

**summary.** frontmatter에 `summary`가 없으면 Hugo가 본문 앞부분을 잘라 meta description으로 씁니다. 표로 시작하는 글은 **표 셀 내용이 검색결과 설명에 그대로 들어갑니다** — 이 사이트에서 실제로 벌어진 일입니다. 글마다 한두 문장을 직접 쓰는 게 가장 쌉니다:

```yaml
summary: "입력 토큰이 비슷한 두 요청의 비용이 46배 차이 났습니다. 프롬프트 캐싱의 구조와…"
```

보너스: 서치 콘솔 등록에 필요한 사이트 인증 메타 태그는 PaperMod에 내장돼 있습니다. `hugo.yaml`에 값만 넣으면 됩니다:

```yaml
params:
  analytics:
    google:
      SiteVerificationTag: "…"
    naver:
      SiteVerificationTag: "…"
```

## 배포 전 체크리스트

- 라이트 / 다크 / 시스템 자동 세 모드
- 모바일 (그리드가 1열로 접히는지)
- 두 언어 홈이 모두 렌더링되는지
- `hugo --minify` 빌드 통과

이 사이트의 전체 코드는 공개 리포입니다: [github.com/JohnOnLee/JohnOnLee](https://github.com/JohnOnLee/JohnOnLee). 이 글의 모든 코드가 실제로 돌아가는 모습 그대로 있으니, 뜯어보면서 적용하시면 됩니다. 막히는 부분은 [GitHub 이슈](https://github.com/JohnOnLee/JohnOnLee/issues)로 남겨주세요.
