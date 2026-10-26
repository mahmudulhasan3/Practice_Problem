# load_dataset.py
import json
from collections import Counter
from dataset_schema import GoldenItem


def load_golden(path: str) -> list[GoldenItem]:
    items, seen_ids = [], set()
    with open(path, encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            if not line.strip():
                continue
            try:
                item = GoldenItem(**json.loads(line))
            except Exception as e:
                # কোন line-এ ভুল সেটা বলে দাও
                raise ValueError(f"Line {line_no}: {e}")
            if item.id in seen_ids:
                raise ValueError(f"Duplicate id: {item.id}")
            seen_ids.add(item.id)
            items.append(item)
    return items


def coverage_report(items: list[GoldenItem]) -> None:
    """Dataset balanced কিনা দেখো"""
    print("Total:", len(items))
    print("By category:", Counter(i.category for i in items))
    print("By difficulty:", Counter(i.difficulty for i in items))
    print("Answerable ratio:", sum(i.answerable for i in items) / len(items))


if __name__ == "__main__":
    data = load_golden("golden_dataset.jsonl")
    coverage_report(data)
