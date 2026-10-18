#!/usr/bin/env python3
"""
Jargon Buster builder  (Python 3.8+, no extra packages)

    python build.py          build the HTML + reports
    python build.py --open   ...and open the result in your browser

Reads every  batches/*.md , checks them, merges them, and writes into output/:
    Jargon_Buster.html   the finished, self-contained page (also copied to ./index.html)
    report.txt           errors / warnings / did-you-mean suggestions
    ids.txt              every defined id  (paste into Claude so it reuses ids)
    to_define.txt        undefined terms people keep referencing  (your next-batch to-do list)
    glossary.json        the merged data, in case you want it elsewhere
"""
import difflib, json, re, sys, webbrowser
from collections import defaultdict, Counter
from pathlib import Path

ROOT = Path(__file__).parent
FIELDS = {"term", "category", "eli5", "analogy", "precursors", "enables", "related", "aliases"}
REQUIRED = ("term", "category", "eli5", "analogy")
LISTS = ("precursors", "enables", "related", "aliases")
ID_RE = re.compile(r"^[a-z0-9_]+$")


def parse_batch(path):
    """Entries start with '## some_id'. Then 'key: value' lines. Unindented text continues the previous value."""
    entries, errors, cur, last = [], [], None, None
    for n, raw in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
        line = raw.rstrip()
        if line.strip().startswith("```"):
            continue
        if line.startswith("## "):
            cur = {"id": line[3:].strip(), "_file": path.name, "_line": n}
            entries.append(cur); last = None
        elif cur is None or not line.strip() or line.lstrip().startswith("<!--"):
            continue
        else:
            m = re.match(r"^([a-z0-9_]+):\s*(.*)$", line)
            if m and m.group(1) in FIELDS:
                last = m.group(1); cur[last] = m.group(2).strip()
            elif m and not line.startswith(" "):
                errors.append(f"{path.name}:{n}: unknown field '{m.group(1)}' in '{cur['id']}' (allowed: {', '.join(sorted(FIELDS))})")
            elif last:
                cur[last] += " " + line.strip()
    return entries, errors


def split_list(v):
    return [x.strip() for x in re.split(r"[,;]", v or "") if x.strip()]


def load_categories():
    cats = {}
    f = ROOT / "categories.txt"
    if f.exists():
        for line in f.read_text(encoding="utf-8-sig").splitlines():
            if line.strip() and not line.startswith("#"):
                name, _, colour = line.partition("|")
                cats[name.strip()] = colour.strip() or None
    return cats


def main():
    errors, warnings = [], []
    cats = load_categories()
    entries = []
    for f in sorted((ROOT / "batches").glob("*.md")):
        e, errs = parse_batch(f)
        entries += e; errors += errs

    # ---- per-entry checks, ids and aliases
    by_id, alias_of = {}, {}
    for e in entries:
        where = f"{e['_file']}:{e['_line']}"
        if not ID_RE.match(e["id"]):
            errors.append(f"{where}: id '{e['id']}' must be lowercase letters, digits and underscores only")
        if e["id"] in by_id:
            errors.append(f"{where}: duplicate id '{e['id']}' (first defined in {by_id[e['id']]['_file']}:{by_id[e['id']]['_line']})")
            continue
        by_id[e["id"]] = e
        for k in REQUIRED:
            if not e.get(k):
                errors.append(f"{where}: '{e['id']}' is missing '{k}'")
        for k in LISTS:
            e[k] = split_list(e.get(k))
        if len(e.get("eli5", "").split()) > 40:
            warnings.append(f"{where}: '{e['id']}' eli5 is {len(e['eli5'].split())} words (aim for 25 or fewer)")
        if len(e.get("analogy", "").split()) > 45:
            warnings.append(f"{where}: '{e['id']}' analogy is {len(e['analogy'].split())} words (aim for 30 or fewer)")
        if e.get("category") and cats and e["category"] not in cats:
            close = difflib.get_close_matches(e["category"], cats, 1, 0.6)
            warnings.append(f"{where}: '{e['id']}' has category '{e['category']}' which is not in categories.txt" + (f" - did you mean '{close[0]}'?" if close else ""))
    for e in by_id.values():
        for a in e["aliases"]:
            if a in by_id:
                errors.append(f"{e['_file']}:{e['_line']}: alias '{a}' of '{e['id']}' is also a real id")
            elif a in alias_of:
                errors.append(f"{e['_file']}:{e['_line']}: alias '{a}' used by both '{alias_of[a]}' and '{e['id']}'")
            else:
                alias_of[a] = e["id"]

    def resolve(x):
        return x if x in by_id else alias_of.get(x)

    # ---- resolve references, drop self-links, find undefined
    mentions, near = Counter(), {}
    for e in by_id.values():
        for k in ("precursors", "enables", "related"):
            out = []
            for x in e[k]:
                r = resolve(x)
                if r == e["id"]:
                    continue
                if r is None:
                    mentions[x] += 1
                out.append(r or x)
            e[k] = list(dict.fromkeys(out))
    known = list(by_id) + list(alias_of)
    for x in mentions:
        c = difflib.get_close_matches(x, known, 1, 0.8)
        if c:
            near[x] = c[0]

    # ---- write each relationship once, derive the other direction
    for e in list(by_id.values()):
        for t in e["enables"]:
            if t in by_id and e["id"] not in by_id[t]["precursors"]:
                by_id[t]["precursors"].append(e["id"])
        for p in e["precursors"]:
            if p in by_id and e["id"] not in by_id[p]["enables"]:
                by_id[p]["enables"].append(e["id"])

    # ---- same term under two ids
    seen = defaultdict(list)
    for e in by_id.values():
        seen[re.sub(r"[^a-z0-9]", "", e["term"].lower())].append(e["id"])
    for ids in seen.values():
        if len(ids) > 1:
            warnings.append(f"Same term under several ids: {', '.join(ids)} - merge them and keep the others as aliases")

    # ---- dependency loops (precursor -> enables)
    graph = {i: [t for t in e["enables"] if t in by_id] for i, e in by_id.items()}
    state, loops = {}, []
    sys.setrecursionlimit(20000)

    def dfs(u, path):
        state[u] = 1; path.append(u)
        for v in graph[u]:
            if state.get(v) is None:
                dfs(v, path)
            elif state[v] == 1 and len(loops) < 15:
                loops.append(path[path.index(v):] + [v])
        path.pop(); state[u] = 2

    for n in graph:
        if state.get(n) is None:
            dfs(n, [])
    for l in loops:
        warnings.append("Loop in precursors/enables: " + " -> ".join(l))

    # ---- reports
    out = ROOT / "output"
    out.mkdir(exist_ok=True)
    ghosts, referrers = Counter(), defaultdict(list)
    for e in by_id.values():
        for k in ("precursors", "enables", "related"):
            for x in e[k]:
                if x not in by_id:
                    ghosts[x] += 1
                    referrers[x].append(f"{e['id']}({k})")
    lines = [f"{len(by_id)} terms defined, {len(ghosts)} referenced but not defined yet", ""]
    lines += [f"ERRORS ({len(errors)})"] + [f"  {m}" for m in errors] + [""]
    lines += [f"WARNINGS ({len(warnings)})"] + [f"  {m}" for m in warnings] + [""]
    if near:
        lines += ["DID YOU MEAN? (undefined ids that look like typos or aliases of defined ones)"]
        lines += [f"  {a}  ->  {b}" for a, b in sorted(near.items())] + [""]
    (out / "report.txt").write_text("\n".join(lines), encoding="utf-8")
    (out / "ids.txt").write_text(
        "\n".join(f"{i} | {e['term']} | {e['category']}" for i, e in sorted(by_id.items())), encoding="utf-8")
    (out / "to_define.txt").write_text(
        "\n".join(f"{n:3d}  {x}  <- {', '.join(referrers[x])}" for x, n in ghosts.most_common()), encoding="utf-8")

    print(f"{len(by_id)} terms | {len(ghosts)} undefined | {len(errors)} errors | {len(warnings)} warnings")
    for m in errors[:25]:
        print("  ERROR  ", m)
    if len(errors) > 25:
        print(f"  ... {len(errors) - 25} more errors in output/report.txt")
    for m in warnings[:10]:
        print("  warning", m)
    if len(warnings) > 10:
        print(f"  ... {len(warnings) - 10} more warnings in output/report.txt")
    if near:
        print(f"  {len(near)} undefined ids look like typos/aliases - see 'DID YOU MEAN' in output/report.txt")
    if errors:
        print("Fix the errors above and run again (HTML not updated).")
        return 1

    data = [{"id": i, "term": e["term"], "category": e["category"], "eli5": e["eli5"], "analogy": e["analogy"],
             "precursors": e["precursors"], "enables": e["enables"], "related": e["related"]}
            for i, e in by_id.items()]
    colours = {c: v for c, v in cats.items() if v}
    (out / "glossary.json").write_text(json.dumps(data, indent=1, ensure_ascii=False), encoding="utf-8")
    html = (ROOT / "template.html").read_text(encoding="utf-8")
    # '</' is escaped so entry text can never close the <script> tag
    safe = lambda o: json.dumps(o, ensure_ascii=False).replace("</", "<\\/")
    html = html.replace("/*__DATA__*/[]", safe(data)).replace("/*__COLORS__*/{}", safe(colours))
    target = out / "Jargon_Buster.html"
    target.write_text(html, encoding="utf-8")
    (ROOT / "index.html").write_text(html, encoding="utf-8")  # root copy, ready for GitHub Pages
    print(f"Built {target}")
    if "--open" in sys.argv:
        webbrowser.open(target.resolve().as_uri())
    return 0


if __name__ == "__main__":
    sys.exit(main())