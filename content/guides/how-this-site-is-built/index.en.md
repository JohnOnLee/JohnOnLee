---
title: "How This Site Is Built: Turning Hugo + PaperMod Into an Editorial Site"
date: 2026-08-02
summary: "Home override, CSS-variable palette, dark mode done right, and Korean typography — every customization on this site, with the actual code, and no theme fork."
---

Sites that start from a stock theme tend to look like it. This one did too — until recently it was the default [PaperMod](https://github.com/adityatelange/hugo-PaperMod) screen. The editorial homepage and unified article styling you're looking at came out of a single day of customization, and this guide is that work written down, code included.

One principle drove all of it: **never fork the theme.** The theme stays a submodule and keeps receiving updates; you win with site-level files only. Hugo resolves same-path site files ahead of theme files, which makes this possible. The entire customization of this site is a handful of files:

```
layouts/index.html              ← full homepage replacement
data/home/ko.yaml, en.yaml      ← homepage copy (per language)
assets/css/extended/home.css    ← homepage styles
assets/css/extended/custom.css  ← unifying every other page
```

The starting point is a Hugo site with PaperMod as a submodule, deployed to GitHub Pages. Basic installation is well covered by the [PaperMod wiki](https://github.com/adityatelange/hugo-PaperMod/wiki/Installation), so I'll skip it.

## 1. Replace the homepage wholesale

Create a single `layouts/index.html` and the homepage is yours. The theme's home template stays untouched.

The key move: don't hardcode copy into the markup — pull it from data files. On a bilingual site, one template then serves both languages:

```html
{{- $copy := index .Site.Data.home .Site.Language.Lang -}}
{{- $posts := first 4 (where .Site.RegularPages.ByDate.Reverse "Section" "blog") -}}

<section class="editorial-hero">
  <p class="editorial-eyebrow">{{ $copy.hero.eyebrow }}</p>
  <h1>{{ range $i, $line := $copy.hero.titleLines }}{{ if $i }}<br>{{ end }}{{ $line }}{{ end }}</h1>
  <p class="editorial-intro">{{ $copy.hero.intro }}</p>
</section>
```

`data/home/en.yaml` holds nothing but words:

```yaml
hero:
  eyebrow: "IDEAS · PRODUCTS · OPPORTUNITIES"
  titleLines:
    - "Where ideas become products,"
    - "and products become new opportunities."
```

Copy edits stop requiring template changes, and adding a language is one more yaml file. Latest posts are pulled dynamically as above — handle the `{{ else }}` empty state so a section with no content degrades gracefully.

## 2. Unify every other page with CSS variables

You don't need to rebuild article and list pages. PaperMod drives all of its colors through CSS variables, so swapping the variables re-tones the whole site. Anything under `assets/css/extended/` is bundled automatically — no theme edits:

```css
:root {
  --theme: #fbfaf7;      /* paper background */
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

Putting just the display type in a serif gets you half the editorial impression:

```css
.post-title,
.page-header h1,
.entry-header h2 {
  font-family: var(--j-serif);
  font-weight: 400;
}
```

One trap when flattening the card-style list entries into rules-only rows: PaperMod's `.post-entry` carries `border: 1px solid` on **all four sides**, so overriding only `border-bottom` leaves a ghost outline on the other three:

```css
.post-entry {
  background: transparent;
  border: 0;                                /* kill all four first */
  border-bottom: 1px solid var(--border);   /* then bring back the bottom */
}
```

## 3. Dark mode is data-theme (not body.dark)

Older PaperMod customization examples on the internet hang dark styles off `body.dark`. **On current PaperMod they silently do nothing.** The theme now sets a `data-theme` attribute on `<html>` via JS. This site hit exactly that trap at first — dark mode was dead on arrival.

```css
:root[data-theme="dark"] {
  /* dark palette */
}

/* No-JS visitors stay on data-theme="auto" — follow their system setting */
@media (prefers-color-scheme: dark) {
  :root[data-theme="auto"] {
    /* the same dark palette */
  }
}
```

Check all three modes: light, dark, and system-auto.

## 4. For Korean text, keep-all is half the battle

On Korean sites, mid-word line breaks ("1,200포\n인트") are fixed with one line of CSS:

```css
body {
  word-break: keep-all;        /* Korean: never break inside a word */
  overflow-wrap: break-word;   /* escape hatch for long URLs */
}
```

`keep-all` only affects CJK text, so Latin is untouched. Put it on `body`, not just article content — titles, lists, and the homepage need it too.

A note on serif fonts: Korean serif fallbacks differ wildly per device — calligraphic on macOS, Batang on Windows, and plain sans on Android. If cross-device consistency matters to your brand, self-host a subsetted Noto Serif KR woff2. This site currently accepts the fallback.

## 5. Two things search engines read — handle them early

**Titles.** Repetitive titles that differ only by date ("Morning Brief — 2026-08-01") die in lists and in search results. This site retitled its auto-published posts to each day's top headline; the date already lives in the metadata and URL.

**Summaries.** Without a `summary` in frontmatter, Hugo cuts the start of the body into the meta description. If a post opens with a table, **table cells end up verbatim in your search snippet** — that actually happened on this site. Writing one or two sentences per post is the cheapest fix:

```yaml
summary: "Two requests with near-identical input tokens, a 46x cost gap. How prompt caching really works…"
```

Bonus: the site-verification meta tags for search consoles are built into PaperMod — just add the values to `hugo.yaml`:

```yaml
params:
  analytics:
    google:
      SiteVerificationTag: "…"
    naver:
      SiteVerificationTag: "…"
```

## Pre-deploy checklist

- Light / dark / system-auto, all three modes
- Mobile (grids collapse to one column)
- Both language homepages render
- `hugo --minify` builds clean

The full source of this site is public: [github.com/JohnOnLee/JohnOnLee](https://github.com/JohnOnLee/JohnOnLee). Every snippet in this guide is there, running, in context. If you get stuck, open an issue on the [GitHub repository](https://github.com/JohnOnLee/JohnOnLee/issues).
