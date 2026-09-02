# Writing workflow — john.onlee.io

How prose gets written for this site by an agent, so that a different agent
(Hermes for the daily brief, Stig for posts and page copy) can run the same
procedure. This file is the *procedure*. The rule catalog it relies on lives in
one place only, `.claude/skills/prose-polish/SKILL.md`, and is not repeated
here; when a rule changes, it changes there.

## What the workflow is for

Korean prose written by a model comes out as a translation of English thought:
"~에 대해", abstract subjects performing actions, uniform "~습니다" endings,
metaphors doing the work of a plain claim. John's direction for the site is the
opposite — say it to the reader directly (직접·직설·직관), no devices — and the
voice to match is documented in `.claude/skills/prose-polish/VOICE.md`.

The trap is that the model which wrote a calque will approve it on review:
detection and generation share one prior. So the workflow does not ask "is
this sentence okay?". It makes the writer *say* the content first and write
from the spoken version, records that re-utterance sentence by sentence, and
has a second model that never saw the draft say the same content from facts
alone. The scripts enforce that those steps happened; only John's flags
measure whether they were done honestly.

## Files

| Path | Role | In git? |
|---|---|---|
| `.claude/skills/prose-polish/SKILL.md` | Procedure + the Korean/English tell catalog, structure tells, fact discipline, voice anchors | no — `.claude/*` is ignored; copy it to the other agent |
| `.claude/skills/prose-polish/VOICE.md` | John's voice, extracted from an unedited sample. Read *before* drafting Korean | no — copy |
| `.claude/skills/humanizer/SKILL.md` | Second pass: Wikipedia "signs of AI writing", 33 patterns | no — copy |
| `.claude/skills/story-structure/SKILL.md` | Outline stage for narrative posts: addressee (§0.5), angle, ending-first structure | no — copy; not needed for briefs |
| `scripts/prose_lint.py` | Mechanical layer of the catalog + statistics against John's published posts; the re-utterance gate | yes |
| `scripts/prose_baseline.json` | Quantiles (p10/p50/p90) of rhythm and vocabulary metrics over 25 ko and 25 en published posts | yes |
| `scripts/prose_lint_cases.json` | Golden bad/good pairs; `--test` must pass whenever a rule changes | yes |
| `scripts/prose_mine.py` | Mines AI-tell candidates from a human-vs-AI corpus; output is curated by hand, never auto-added | yes |
| `scripts/seo_check.py` | Title width, description ≤ 160 columns, ko/en pair, canonical and links; `--source` mode runs on front matter with no build | yes |
| `drafts/<name>.md`, `drafts/spoken/<name>.spoken.md`, `drafts/spoken/<name>.cold.md` | Draft and its two re-utterance records | no; deleted after publish |

## The steps for one piece

1. **Fix the addressee, then outline.** One person the prose talks to; other
   readers benefit over the shoulder. Narrative posts go through
   `story-structure/SKILL.md` first; briefs and page copy skip the outline
   but still name the addressee (for the brief: the person building products
   with AI).
2. **Draft Korean speak-first.** Per section, write what you would *say* to
   John, then tidy that into 습니다체. Never write English first and
   translate — that is where calques come from. Then write English fresh from
   the same facts. Every post ships as a ko+en pair. Dates are KST and the
   site does not build future dates, so a piece dated tomorrow is invisible
   until tomorrow; never link forward to a later-dated post (the deploy
   treats a broken internal link as a structural fault and blocks).
3. **Pass 1, the catalog.** Read the draft against `prose-polish/SKILL.md`.
   Deletion beats editing: if a sentence trips a rule, try removing it first.
   Then the mechanical layer:

   ```
   python3 scripts/prose_lint.py drafts/<name>-ko.md drafts/<name>-en.md
   python3 scripts/prose_lint.py --verbs drafts/<name>-ko.md
   ```

   Exit 1 on any hit. Line-numbered hits are rule hits: fix them. Hits
   marked `(검토)` are review-level: judge them. `통계(검토)` hits compare the
   piece to the published baseline and are meaningful for post-length text;
   on anything under about 300 words they fire on size alone — read, don't
   obey. `--verbs` prints every noun+particle+verb pair; read the list and
   replace pairs that are English verbs in Korean clothing (프로그램을 열다,
   시장이 서다). A confirmed pair goes into the blacklist *and* the cases file.
4. **Re-utterance record.** For each sentence, in `drafts/spoken/<name>-ko.spoken.md`,
   one line `N| <spoken version>`. Order matters: extract the paragraph's
   point first, speak from the point *before* re-reading the written
   sentence, and replace the written sentence when the two differ. A
   paragraph whose point will not come out in one sentence is the first
   finding — rebuild the paragraph, don't polish it. Quotes, numbers and
   table references stay as written: `N| <sentence> §유지: <reason>`.
5. **Cold re-utterance.** Give a worker that has never seen the draft — a
   different model if possible — only the facts, in telegraphic form, with no
   draft wording and no file or tool access, and have it say the piece. Save
   its output as `drafts/spoken/<name>-ko.cold.md`, then compare. Where the
   cold phrasing diverges from the draft, suspect the draft: it was written
   by the contaminated sense, the worker was not anchored to it. Any draft
   wording that leaks into the facts brief comes back verbatim, and that
   match proves nothing.
6. **Gate.**

   ```
   python3 scripts/prose_lint.py --spoken drafts/<name>-ko.md
   ```

   Passes only if the spoken record exists, is newer than the draft, covers
   every sentence, and the cold record exists (it warns if the draft is newer
   than the cold record — re-run the cold step after a structural rewrite).
   English files are skipped by the gate; the catalog and humanizer still
   apply to them.
7. **Pass 2, humanizer.** `humanizer/SKILL.md` in full on English; the
   language-agnostic patterns on Korean (staccato drama, rule of three,
   significance inflation, negative parallelism, aphorism formulas).
8. **SEO source check.**

   ```
   python3 scripts/seo_check.py --source content/<section>/<slug>/index.ko.md content/<section>/<slug>/index.en.md
   ```

   Title pixel width, description under 160 columns (a Hangul syllable
   counts two), and the ko/en pair. Resolves paths against the repo root, so
   it can be called from any working directory.
9. **John's review** — posts and page copy only, never briefs: one paragraph
   at a time, wait for the verdict, fix in place, move on. A whole draft in
   one batch pushes the reader toward shallow judgment.
10. **Publish.** Commit the ko+en pair; the deploy builds, runs `seo_check`
    on the rendered site (structural faults block, content issues report),
    deploys, then pings IndexNow. English posts and guides are auto-drafted
    to Dev.to with a canonical back to the site; briefs are not cross-posted.
    Then delete the draft and both records — the published post is the
    canonical copy.

## Briefs: what changes for an autonomous writer

- There is no John review. Steps 3–8 are the whole review, so they are not
  optional there.
- The gate looks for records in a `spoken/` folder beside the draft. Inside
  `content/` Hugo would render that folder as pages, so draft under
  `drafts/` (`drafts/brief-YYYY-MM-DD-ko.md`, `-en.md`), pass the gate, and
  only then write `content/brief/YYYY-MM-DD/index.{ko,en}.md`.
- Minimum viable adoption, if the writer cannot run multiple steps or call a
  second model: steps 3 and 8 (the two scripts) with a fix-and-rerun loop.
  Full adoption adds 4, 5 and 6.
- Copy rules that bite briefs: never present agent-written work as human
  work ("hand-picked" → "picked daily"); briefs carry no tags; `summary`
  under 160 columns; `date` is today in KST.

## Maintenance

- When John flags a phrase: add the rule to `prose-polish/SKILL.md`, the
  regex to `prose_lint.py` when it is mechanical, and a bad/good pair to
  `prose_lint_cases.json`. Then `python3 scripts/prose_lint.py --test` must
  pass. Rules are regression armor for known patterns; they do not detect
  the next new one — the re-utterance does.
- When new posts publish: `python3 scripts/prose_lint.py --calibrate`
  rewrites the baseline from `content/`.
- `prose_mine.py` proposes candidate patterns from a human-vs-AI corpus;
  everything it prints is reviewed by hand before it enters the catalog.
