#!/usr/bin/env python3
"""Pattern mining for AI-tell candidates (stdlib only).

--en           : fetch HC3 (human vs ChatGPT) via HF datasets-server, mine word n-grams
--ko AI_FILE   : mine char/word n-grams, John's published ko posts vs a local AI-style corpus
Output: ranked log-odds tables to stdout; candidates are CURATED by hand into
prose_lint.py / SKILL.md — never auto-added.

Future ko contrast corpora (found via John's deep research, 2026-08-25):
- KatFish: Korean human-vs-LLM (essays/poems/abstracts), interpretable features (spacing, POS n-grams, commas)
- XDAC: Korean news comments, 1.3M human + ~1M LLM (14 models)
Domain differs from tech-blog prose - re-validate patterns before adopting."""
import sys, re, json, math, pathlib, urllib.request, collections

ROOT = pathlib.Path(__file__).parent.parent

def logodds(counts_a, counts_b, min_a=10):
    tot_a, tot_b = sum(counts_a.values()) or 1, sum(counts_b.values()) or 1
    rows = []
    for g, ca in counts_a.items():
        if ca < min_a: continue
        cb = counts_b.get(g, 0)
        lo = math.log((ca + 0.5) / tot_a) - math.log((cb + 0.5) / tot_b)
        rows.append((round(lo, 2), ca, cb, g))
    return sorted(rows, reverse=True)

def en_tokens(text): return re.findall(r"[a-z']+", text.lower())

def mine_en():
    base = "https://datasets-server.huggingface.co/rows?dataset=Hello-SimpleAI%2FHC3&config=all&split=train&length=100&offset="
    human, ai = [], []
    for off in range(0, 800, 100):
        try:
            with urllib.request.urlopen(base + str(off), timeout=30) as r:
                rows = json.load(r)["rows"]
        except Exception as e:
            print(f"fetch offset {off} failed: {e}"); break
        for row in rows:
            r = row["row"]
            human += r.get("human_answers") or []
            ai += r.get("chatgpt_answers") or []
    print(f"HC3 fetched: human {len(human)} / ai {len(ai)} answers")
    for n in (1, 2, 3):
        ca, cb = collections.Counter(), collections.Counter()
        for t in ai:
            toks = en_tokens(t)
            ca.update(tuple(toks[i:i+n]) for i in range(len(toks)-n+1))
        for t in human:
            toks = en_tokens(t)
            cb.update(tuple(toks[i:i+n]) for i in range(len(toks)-n+1))
        print(f"\n== EN {n}-grams over-represented in AI text (logodds, ai_count, human_count) ==")
        for lo, a, b, g in logodds(ca, cb, min_a=40 if n == 1 else 25)[:35]:
            print(f"  {lo:>5}  {a:>5} {b:>5}  {' '.join(g)}")

def ko_corpus_human():
    texts = []
    for sec in ("blog", "guides"):
        for f in (ROOT/"content"/sec).glob("*/index.ko.md"):
            t = re.sub(r"^---.*?---", "", f.read_text(), flags=re.S)
            t = re.sub(r"```.*?```", "", t, flags=re.S)
            texts.append(t)
    return texts

def mine_ko(ai_file):
    human = ko_corpus_human()
    ai = [p for p in pathlib.Path(ai_file).read_text().split("\n\n") if len(p.strip()) > 50]
    print(f"KO corpora: human {len(human)} posts / ai {len(ai)} passages")
    def char_ngrams(texts, n):
        c = collections.Counter()
        for t in texts:
            for run in re.findall(r"[가-힣][가-힣 .,]*[가-힣]", t):
                c.update(run[i:i+n] for i in range(len(run)-n+1))
        return c
    for n in (3, 4, 5):
        ca, cb = char_ngrams(ai, n), char_ngrams(human, n)
        print(f"\n== KO char {n}-grams over-represented in AI text ==")
        for lo, a, b, g in logodds(ca, cb, min_a=6)[:35]:
            print(f"  {lo:>5}  {a:>4} {b:>4}  「{g}」")

if __name__ == "__main__":
    if "--en" in sys.argv: mine_en()
    elif "--ko" in sys.argv: mine_ko(sys.argv[sys.argv.index("--ko")+1])
    else: print(__doc__)
