"""Wiki 機械性 lint：對應 AGENTS.md 第 5.3 節的第 1、2、3、4、8、9 項，以及第 10 項（概念頁模板，見 4.2 節）。

用法：python tools/lint.py
內容判斷類問題（矛盾、符號不一致、重複概念）仍需人工與 AI 討論。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
LINK = re.compile(r"\[([^\]]*)\]\(([^)#\s]+\.md)(#[^)]*)?\)")
SKIP_FILES = {"log.md"}

pages = [p for p in WIKI.rglob("*.md") if p.name not in SKIP_FILES]
content_pages = [p for p in pages if p.parent.name in ("concepts", "examples", "sources", "questions")]
problems = {k: [] for k in ["1 斷掉的連結", "1 誤用 [[...]]", "2 孤兒頁", "3 index 缺頁",
                            "4 缺少出處的條列", "8 公式後缺符號表", "10 概念頁缺少模板區塊", "9 未處理的 TODO"]}
inbound = {p.resolve(): 0 for p in content_pages}

for p in pages:
    text = p.read_text(encoding="utf-8")
    rel = p.relative_to(ROOT)
    if "[[" in text:
        problems["1 誤用 [[...]]"].append(str(rel))
    for m in LINK.finditer(text):
        target = (p.parent / m.group(2)).resolve()
        if not target.exists():
            problems["1 斷掉的連結"].append(f"{rel} → {m.group(2)}")
        elif p.name != "index.md" and target in inbound and target != p.resolve():
            inbound[target] += 1
    for line in re.findall(r"<!-- TODO:([^>]*)-->", text):
        problems["9 未處理的 TODO"].append(f"{rel}：{line.strip()}")

    if p.parent.name == "concepts":
        for h in ["## 一句話說明", "## 白話解釋", "## 正式內容", "## 和其他概念的關係", "## 出處"]:
            if h not in text:
                problems["10 概念頁缺少模板區塊"].append(f"{rel}：{h}")
        body = text.split("## 正式內容", 1)[-1].split("\n## ", 1)[0]  # 只檢查「正式內容」一節
        group_cited = parent_cited = False  # 條列上方的小標或引言已標出處時，視為整組都有出處
        for line in body.splitlines():
            s = line.strip()
            if not s:
                continue
            is_item = re.match(r"^(- |\d+\. )", s) or line.startswith("  ")
            if not is_item:
                group_cited = "〔" in s
                continue
            nested = line.startswith("  ")
            if not nested:
                parent_cited = "〔" in s
            covered = group_cited or (nested and parent_cited)
            if "〔" not in s and not s.endswith("：") and not covered:
                problems["4 缺少出處的條列"].append(f"{rel}：{s[:40]}")
        lines = text.splitlines()
        for i, line in enumerate(lines):
            if line.strip().startswith("$$") and line.strip().endswith("$$") and len(line.strip()) > 4:
                k = i + 1  # 連續的公式共用同一張符號表：跳過空行與後續公式
                while k < len(lines) and (not lines[k].strip() or lines[k].strip().startswith("$$")):
                    k += 1
                window = "\n".join(lines[k:k + 2])
                if "| 符號 |" not in window and "〔" not in window:
                    problems["8 公式後缺符號表"].append(f"{rel} 第 {i + 1} 行")

index_text = (WIKI / "index.md").read_text(encoding="utf-8")
for p in content_pages:
    rel_to_wiki = p.relative_to(WIKI).as_posix()
    if rel_to_wiki not in index_text:
        problems["3 index 缺頁"].append(rel_to_wiki)
    if p.parent.name in ("concepts", "examples") and inbound[p.resolve()] == 0:
        problems["2 孤兒頁"].append(rel_to_wiki)

total = 0
for k, v in problems.items():
    print(f"[{'OK' if not v else len(v)}] {k}")
    for item in v:
        print(f"    - {item}")
    if not k.startswith("9"):
        total += len(v)
print(f"\n頁面數：{len(pages)}（內容頁 {len(content_pages)}）；需修正：{total}；TODO：{len(problems['9 未處理的 TODO'])}")
sys.exit(1 if total else 0)
