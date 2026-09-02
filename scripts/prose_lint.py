#!/usr/bin/env python3
"""Mechanical prose lint for john.onlee.io drafts (ko+en).

Encodes the regex-detectable rules from .claude/skills/prose-polish/SKILL.md.
Judgment-level rules (metaphor, staging, voice) are NOT here - this only
catches the mechanical layer. Usage: python3 scripts/prose_lint.py FILE...
Modes: --test (golden cases), --calibrate [dir], --verbs FILE... (ko 명사+조사+서술어
짝을 나열 — 동사 연어 검수용. 블랙리스트는 아는 짝만 잡으므로, 새 짝은 이 목록을
통독해서 찾고 발견 즉시 블랙리스트+케이스에 추가한다).
Exit code 1 if any hit."""
import re, sys, pathlib

KO_RULES = [
    ("번역투 ~에 대해", re.compile(r"에 대해|에 대한")),
    ("번역투 ~를 통해", re.compile(r"[를을] 통해")),
    ("번역투 당신", re.compile(r"당신의?")),
    ("번역투 ~로부터", re.compile(r"[가-힣]로부터(?<!유로부터)")),
    ("결론 신호어", re.compile(r"결론적으로|요약하자면|정리하자면")),
    ("과장 수식어", re.compile(r"(매우|정말|완벽한|훌륭한|놀라운) ")),
    ("~하게 됩니다체", re.compile(r"하게 됩니다")),
    ("명사절+요 꼬리", re.compile(r"[가-힣]이요\.|(방향|점|얘기)이요")),  # 다고요/니까요 등 구어 인용꼬리는 허용
    ("문어체 의문 종결", re.compile(r"[가-힣]는가\.")),
    ("어색: 한 해 새", re.compile(r"한 해 새")),
    ("피동: 설명이 됩니다", re.compile(r"설명이 됩니다")),
    ("피동: 요구받는", re.compile(r"요구받")),
    ("관용구 오용: 손을 타다", re.compile(r"손을 (덜 |많이 )?(타|탑니|탄다)")),
    ("어휘 톤(검토): 잡종", re.compile(r"잡종")),
    ("용어 눈높이(검토): 조달", re.compile(r"조달")),
    # 동사 연어 블랙리스트 2026-08-31 (John: "전반적으로 한글 동사 사용을 확인해봐야 할 정도")
    # 영어 동사 직역·조사 오류로 확인된 짝. 새 짝이 발견되면 여기 추가하고 cases에 m케이스를 쌍으로 남긴다.
    ("동사 연어(검토): 프로그램·제휴를 열다", re.compile(r"(프로그램|제휴)[을를] (열|엽)")),
    ("동사 연어: 시장이 서다", re.compile(r"시장이 (따로 )?(서고|서는|섭니|선다)")),
    ("동사 연어: ~에 책임지다(조사)", re.compile(r"에 책임지")),
    ("동사 연어: 갈래로 모이다", re.compile(r"갈래로 모")),
    ("동사 연어: 자리를 열다", re.compile(r"자리를 열")),
    ("동사 연어(검토): 자격을 알아보다(인정 의도면 알아주다)", re.compile(r"자격[을증]? 알아(보|봅)")),
    ("동사 연어: 수익화가 일어나다", re.compile(r"수익화[가는은] [^.]{0,12}일어나")),
    ("동사 연어: 규모를 타다", re.compile(r"규모를 (타|탑니|탄다)")),
    # 2026-09-02 John: 자동화 편 제목 "채용 시장은 두 개입니다" — 추상 명사를 개로 세는 단정문. 갈라지다/나뉘다/두 갈래로.
    ("개수 세기(검토): 추상명사+N 개입니다", re.compile(r"(시장|방향|길|경로|답|이유|기준)[이은가는]? (두|세|네|다섯) 개입니다")),
    # mined 2026-08-25 vs John's published ko corpus (scripts/mined_report_ko.txt): counts John=0
    ("채굴(검토): 또한", re.compile(r"(^|[ .])또한[ ,]")),
    ("채굴(검토): 다양한", re.compile(r"다양한 ")),
    ("채굴(검토): 이러한", re.compile(r"이러한 ")),
    ("채굴(검토): ~것이 중요", re.compile(r"것이 중요")),
    ("채굴(검토): 위해서는", re.compile(r"위해서는")),
]
NEGPAR = re.compile(r"가 아니라|이 아니라")
MYEO = re.compile(r"[가-힣]며, ")
KO_FILE_RULES = [
    ("채굴(검토): 며-연결 2회 이상", lambda t: len(MYEO.findall(t)) > 1, lambda t: str(len(MYEO.findall(t))) + "회"),
    ("em-dash 4회 이상", lambda t: len(re.findall("—", t)) > 3, lambda t: f"{len(re.findall('—', t))}회"),
    ("부정 병렬(~가 아니라) 3회 이상", lambda t: len(NEGPAR.findall(t)) > 2,
     lambda t: str(len(NEGPAR.findall(t))) + "회"),
]
KO_ABSTRACT = re.compile(r"(시장|공고|가격|경계|데이터|숫자|산업|시대|기술|툴|직함)(이|가) [가-힣]+(합니다|입니다|줍니다|옵니다|갑니다|납니다|섭니다|낍니다)")
KO_ABSTRACT2 = re.compile(r"(시장|공고|가격|경계|데이터|숫자|표|툴|직함)(이|가|은|는)[^.,]{0,24}?(무너지|보여줍|보여준|말해줍|말해준|허락하|확인하는|확인하는 건|모릅니다|모른다|움직이|기다리|원합니다|치르)")
KO_ENDING_RUN = re.compile(r"(니다\.\s+[^.!?]*니다\.\s+[^.!?]*니다\.\s+[^.!?]*니다\.)")

EN_BANNED = re.compile(r"\b(delve|leverag\w+|seamless\w*|robust|landscape|journey|elevate|unleash|(?<!eval )(?<!test )harness\b|navigat\w+|tapestry|crucial|comprehensive)\b", re.I)
EN_RULES = [
    ("banned word", EN_BANNED),
    ("banned opener", re.compile(r"(?m)^(In today's|It's worth noting|Moreover,|Furthermore,|Let's dive)")),
    ("hedging stack", re.compile(r"\b(can|could|may) potentially\b|\bhelp to\b", re.I)),
    ("overgeneralization (review)", re.compile(r"\b(the entire|every|all) \w+ (job market|market|industry|compan\w+)\b", re.I)),
    # mined 2026-08-25 from HC3 human-vs-ChatGPT (scripts/mined_report_en.txt): e.g. "it's important to" 172:0
    ("mined AI-tell (review)", re.compile(r"\b(it([\u2019']s| is) (also )?important to|important to (note|remember)|a variety of|for a variety|(this |it )?can help to|helps to|also known as|it is generally|a good idea to|(one|another) reason is|few reasons why|overall, the|additionally)\b", re.I)),
]
NOTJUST = re.compile(r"\bnot just\b", re.I)
TRICOLON = re.compile(r", \w+,? and \w+")
EN_FILE_RULES = [
    ("em-dash > 3", lambda t: len(re.findall("—", t)) > 3, lambda t: f"{len(re.findall('—', t))}x"),
    ("'not just' > 1", lambda t: len(NOTJUST.findall(t)) > 1,
     lambda t: str(len(NOTJUST.findall(t))) + "x"),
    ("tricolon > 2", lambda t: len(TRICOLON.findall(t)) > 2,
     lambda t: str(len(TRICOLON.findall(t))) + "x"),
]


# ---------- statistical signals, calibrated on John's published corpus ----------
import statistics, json as _json
BASELINE_PATH = pathlib.Path(__file__).parent / "prose_baseline.json"

def _clean_lines(text):
    out, fence = [], False
    for l in text.splitlines():
        t = l.strip()
        if t.startswith("```"): fence = not fence; continue
        if fence or t.startswith("|") or t.startswith("#") or t.startswith("<!--") or t.startswith("-"):
            continue
        out.append(l)
    return out

def _sentences(text):
    import re as _re
    body = " ".join(_clean_lines(text))
    parts = _re.split(r"(?<=[.!?…])\s+", body)
    out = []
    for x in parts:
        x = x.strip()
        if len(x) <= 1: continue
        if _re.fullmatch(r"[*#\d.\s]+", x): continue  # "**3." 같은 번호 헤더 조각 제외
        out.append(x)
    return out

def _ending_class(sent):
    core = sent.rstrip('."\u201d)\u2019 !?…')
    if core.endswith("니다"): return "nida"
    if core.endswith("죠"): return "jyo"
    if core.endswith("요"): return "yo"
    if core.endswith("까"): return "q"
    if core.endswith("다"): return "da"
    return "other"

def text_metrics(text, korean):
    sents = _sentences(text)
    if len(sents) < 5: return None
    lens = [len(s) if korean else len(s.split()) for s in sents]
    mean_len = statistics.mean(lens)
    cv_len = round(statistics.pstdev(lens) / mean_len, 3) if mean_len else 0
    commas = round(sum(s.count(",") + s.count("、") for s in sents) / len(sents), 2)
    paras = [p for p in "\n".join(_clean_lines(text)).split("\n\n") if len(p.strip()) > 40]
    m = {"sents": len(sents), "mean_len": round(mean_len, 1), "cv_len": cv_len, "commas_per_sent": commas}
    if len(lens) >= 10:  # lag-1 autocorrelation of sentence lengths (KatFish/보고서: 리듬 패턴)
        mu = statistics.mean(lens)
        num = sum((lens[i]-mu)*(lens[i+1]-mu) for i in range(len(lens)-1))
        den = sum((l-mu)**2 for l in lens)
        m["len_autocorr"] = round(num/den, 3) if den else 0.0
    toks = []
    for sent in sents: toks += sent.split()
    if len(toks) >= 60:  # MATTR window 50
        w = 50
        ratios = [len(set(toks[i:i+w]))/w for i in range(0, len(toks)-w+1, 10)]
        m["mattr"] = round(statistics.mean(ratios), 3)
    if korean:
        classes = [_ending_class(s) for s in sents]
        m["nida_share"] = round(classes.count("nida") / len(classes), 3)
        m["ending_classes"] = len(set(classes))
        n_abs = sum(len(KO_ABSTRACT.findall(s)) + len(KO_ABSTRACT2.findall(s)) for s in sents)
        m["abstract_per_1k"] = round(n_abs * 1000 / max(1, len(text)), 2)
    return m

# metric -> (bad direction, meaning)
KO_STAT_FLAGS = {"nida_share": ("high", "니다 어미 편중"), "ending_classes": ("low", "어미 다양성 부족"),
                 "cv_len": ("low", "문장 길이 단조(기계 리듬)"), "commas_per_sent": ("both", "쉼표 리듬 이탈(부족=뚝뚝 끊김/과다=LLM 한국어 신호, KatFish)"),
                 "abstract_per_1k": ("high", "추상 주어 밀도"),
                 "len_autocorr": ("both", "문장 길이 리듬 패턴 이탈"), "mattr": ("low", "어휘 다양성 부족")}
EN_STAT_FLAGS = {"cv_len": ("low", "monotone sentence rhythm"), "mean_len": ("both", "sentence length extreme"),
                 "len_autocorr": ("both", "sentence-rhythm pattern deviation"), "mattr": ("low", "low lexical diversity")}

def stat_hits(text, korean):
    if not BASELINE_PATH.exists(): return []
    base = _json.loads(BASELINE_PATH.read_text()).get("ko" if korean else "en")
    if not base: return []
    m = text_metrics(text, korean)
    if not m: return []
    hits = []
    flags = KO_STAT_FLAGS if korean else EN_STAT_FLAGS
    for k, (direction, label) in flags.items():
        if k not in m or k not in base: continue
        v, (p10, p50, p90) = m[k], base[k]
        if direction in ("high", "both") and v > p90:
            hits.append((0, f"통계(검토): {label}", f"{k}={v}, 발행 글 기준 {p10}~{p90} (중앙값 {p50})"))
        if direction in ("low", "both") and v < p10:
            hits.append((0, f"통계(검토): {label}", f"{k}={v}, 발행 글 기준 {p10}~{p90} (중앙값 {p50})"))
    return hits

def calibrate(root):
    root = pathlib.Path(root)
    data = {}
    for lang, glob_pat in (("ko", "index.ko.md"), ("en", "index.en.md")):
        rows = []
        for sec in ("blog", "guides"):
            for f in sorted((root / "content" / sec).glob(f"*/{glob_pat}")):
                t = f.read_text()
                t = re.sub(r"^---.*?---", "", t, flags=re.S)
                m = text_metrics(t, lang == "ko")
                if m: rows.append(m)
        if not rows: continue
        keys = rows[0].keys()
        data[lang] = {}
        for k in keys:
            vals = sorted(r[k] for r in rows if k in r)
            if len(vals) < 4: continue
            q = statistics.quantiles(vals, n=10)
            data[lang][k] = [round(q[0], 3), round(statistics.median(vals), 3), round(q[8], 3)]
        data[lang]["_n_files"] = len(rows)
    BASELINE_PATH.write_text(_json.dumps(data, ensure_ascii=False, indent=1))
    print("baseline written:", {k: v.get("_n_files") for k, v in data.items()})
# ---------- end statistical signals ----------

def is_korean(text):
    return len(re.findall(r"[가-힣]", text)) > len(text) * 0.15

def lint(path):
    text = pathlib.Path(path).read_text()
    body = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    lines = body.splitlines()
    hits = []
    line_rules = KO_RULES if is_korean(body) else EN_RULES
    file_rules = KO_FILE_RULES if is_korean(body) else EN_FILE_RULES
    for i, line in enumerate(lines, 1):
        if line.startswith("|") or line.startswith("#"):  # tables/headers: looser
            continue
        check = re.sub(r"\u201c[^\u201d]*\u201d|\"[^\"]*\"", "", line)  # quoted spans exempt
        for name, rx in line_rules:
            for m in rx.finditer(check):
                hits.append((i, name, line.strip()[:80]))
    if is_korean(body):
        for i, line in enumerate(lines, 1):
            if line.startswith("|"): continue
            for m in KO_ABSTRACT.finditer(line):
                hits.append((i, "추상 주어(검토)", m.group(0)))
            for m in KO_ABSTRACT2.finditer(line):
                hits.append((i, "추상 주어 동작(검토)", m.group(0)))
        for m in KO_ENDING_RUN.finditer(body):
            ln = body[:m.start()].count("\n") + 1
            hits.append((ln, "니다 4연속(검토)", m.group(0)[:60] + "…"))
    for name, pred, detail in file_rules:
        if pred(body):
            hits.append((0, name, detail(body)))
    hits.extend(stat_hits(body, is_korean(body)))
    return hits

def lint_text(text, korean):
    tmp = pathlib.Path("/tmp/._prose_lint_probe.md")
    pad = "검사용 문장이죠. 기준이 되는 글이에요. 여기까지가 준비 부분. " if korean else "This is filler context for the probe. "
    tmp.write_text(pad + "\n" + text + "\n")
    return lint(str(tmp))

if len(sys.argv) > 1 and sys.argv[1] == "--calibrate":
    calibrate(sys.argv[2] if len(sys.argv) > 2 else pathlib.Path(__file__).parent.parent)
    sys.exit(0)

if len(sys.argv) > 2 and sys.argv[1] == "--spoken":
    # 재발화 게이트 (2026-08-31, John: "'말로 하면 뭐라고 하지'를 체계적으로 강제").
    # 초안을 John에게 보이기 전, 문장별 재발화 기록(drafts/spoken/<이름>.spoken.md,
    # "N| 말한 버전" 줄, 예외 유지는 "N| 문장 §유지: 이유")이 존재하고, 초안보다 새로우며,
    # 본문 문장 수를 덮어야 통과. 게이트가 강제하는 건 수행·최신성·커버리지다 —
    # 각 줄이 진짜 말버전인지는 게이트가 못 재므로 John의 지적 빈도가 그 지표.
    fail = False
    ENTRY = re.compile(r"(?m)^\d+\| ")
    for f in sys.argv[2:]:
        p = pathlib.Path(f)
        text = p.read_text()
        if not is_korean(text):
            print(f"  {p.name}: en — 재발화 게이트 생략")
            continue
        sp = p.parent / "spoken" / (p.stem + ".spoken.md")
        n_sent = len(_sentences(re.sub(r"<!--.*?-->", "", text, flags=re.S)))
        if not sp.exists():
            print(f"FAIL {p.name}: 재발화 기록 없음 ({sp})"); fail = True; continue
        if p.stat().st_mtime > sp.stat().st_mtime:
            print(f"FAIL {p.name}: 초안이 재발화 기록보다 새로움 — 수정분을 재발화하고 기록 갱신"); fail = True; continue
        n_spoken = len(ENTRY.findall(sp.read_text()))
        if n_spoken < n_sent:
            print(f"FAIL {p.name}: 재발화 커버리지 부족 ({n_spoken}/{n_sent})"); fail = True; continue
        # 콜드 재발화 (2026-08-31 John 지시로 표준): 초안을 본 적 없는 새 컨텍스트가
        # 요점만 받고 말한 기록. 없으면 FAIL, 초안이 더 새로우면 WARN(구조적 재작성이면 재실행).
        cold = p.parent / "spoken" / (p.stem + ".cold.md")
        if not cold.exists():
            print(f"FAIL {p.name}: 콜드 재발화 기록 없음 ({cold})"); fail = True; continue
        note = " · WARN: 초안이 콜드 기록보다 새로움 — 구조적 재작성이었다면 콜드 재실행" if p.stat().st_mtime > cold.stat().st_mtime else ""
        print(f"  OK {p.name}: 재발화 {n_spoken}/{n_sent}, 콜드 기록 있음{note}")
    sys.exit(1 if fail else 0)

if len(sys.argv) > 2 and sys.argv[1] == "--verbs":
    # 동사 연어 검수용 짝 추출. 형태소 분석 없는 근사: 명사+조사 뒤 1~2어절을 서술어 후보로 본다.
    PAIR = re.compile(r"([가-힣A-Za-z0-9·]{2,})(을|를|이|가|에|에서|에게|로|으로) ([가-힣]+(?: [가-힣]+)?)(?=[ .,)]|$)")
    for f in sys.argv[2:]:
        body = re.sub(r"<!--.*?-->", "", pathlib.Path(f).read_text(), flags=re.S)
        pairs = {}
        for line in body.splitlines():
            if line.startswith("|"): continue
            line = re.sub(r"“[^”]*”|\"[^\"]*\"", "", line)
            for m in PAIR.finditer(line):
                key = f"{m.group(1)}{m.group(2)} {m.group(3)}"
                pairs[key] = pairs.get(key, 0) + 1
        print(f"\n== {pathlib.Path(f).name}: {len(pairs)}쌍 ==")
        for k in sorted(pairs):
            n = pairs[k]
            print(f"  {k}" + (f" ×{n}" if n > 1 else ""))
    sys.exit(0)

if len(sys.argv) > 1 and sys.argv[1] == "--test":
    import json
    cases = json.loads((pathlib.Path(__file__).parent / "prose_lint_cases.json").read_text())["cases"]
    passed = failed = judged = 0
    for c in cases:
        if c["tier"] == "judgment":
            judged += 1
            continue
        ko = c["lang"] == "ko"
        bad_hits = [h for h in lint_text(c["bad"], ko) if h[0] > 0]
        good_hits = [h for h in lint_text(c.get("good", ""), ko) if h[0] > 0] if c.get("good") else []
        bad_rules = {h[1] for h in bad_hits}
        good_rules = {h[1] for h in good_hits}
        caught = bool(bad_rules)
        clean = not (bad_rules & good_rules)
        if caught and clean:
            passed += 1
        else:
            failed += 1
            why = "미검출" if not caught else "good에서도 같은 규칙 검출: " + str(bad_rules & good_rules)
            print(f"FAIL {c['id']} [{c['rule_hint']}] {why}")
    print(f"\nmechanical: {passed} pass / {failed} fail · judgment(기록만): {judged}")
    sys.exit(1 if failed else 0)

any_hit = False
for f in sys.argv[1:]:
    hits = lint(f)
    if hits:
        any_hit = True
        print(f"\n== {pathlib.Path(f).name} ({len(hits)}) ==")
        for ln, name, ctx in sorted(hits):
            loc = f"L{ln}" if ln else "file"
            print(f"  {loc:>5} [{name}] {ctx}")
sys.exit(1 if any_hit else 0)
