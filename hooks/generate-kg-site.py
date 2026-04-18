#!/usr/bin/env python3
"""Generate the interactive knowledge graph HTML site from entities and relationships."""

import json
from collections import defaultdict
from pathlib import Path

CLAUDE_DIR = Path.home() / ".claude"
KG_DIR = CLAUDE_DIR / "knowledge-graph"
DOCS_DIR = CLAUDE_DIR / "docs"
TEMPLATE = CLAUDE_DIR / "hooks" / "kg-site-template.html"


def load_jsonl(path):
    items = []
    if not path.exists():
        return items
    with open(path) as f:
        for line in f:
            if line.strip():
                try:
                    items.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
    return items


def dedupe(entities):
    seen = {}
    for e in entities:
        key = (e.get("name", "").lower(), e.get("type", ""))
        if key not in seen or len(e.get("description", "")) > len(seen[key].get("description", "")):
            seen[key] = e
    return list(seen.values())


def main():
    entities = dedupe(load_jsonl(KG_DIR / "entities.jsonl"))
    rels = load_jsonl(KG_DIR / "relationships.jsonl")

    # Clean data for JSON embedding
    nodes = []
    entity_names = set()
    for e in entities:
        name = e.get("name", "").strip()
        if not name:
            continue
        entity_names.add(name)
        nodes.append({
            "name": name,
            "type": e.get("type", "unknown"),
            "description": e.get("description", ""),
            "date": e.get("date", ""),
        })

    edges = []
    for r in rels:
        src = r.get("source", "").strip()
        tgt = r.get("target", "").strip()
        if src in entity_names and tgt in entity_names:
            edges.append({
                "source": src,
                "target": tgt,
                "type": r.get("type", ""),
                "context": r.get("context", ""),
            })

    graph_data = json.dumps({"nodes": nodes, "edges": edges}, ensure_ascii=False)

    with open(TEMPLATE) as f:
        html = f.read()

    html = html.replace("__GRAPH_DATA__", graph_data)

    with open(DOCS_DIR / "index.html", "w") as f:
        f.write(html)

    print(f"Generated site: {len(nodes)} nodes, {len(edges)} edges")


if __name__ == "__main__":
    main()
