#!/usr/bin/env python3
"""Generate the interactive knowledge graph HTML site from entities and relationships."""

import json
import re
from collections import defaultdict
from pathlib import Path

CLAUDE_DIR = Path.home() / ".claude"
KG_DIR = CLAUDE_DIR / "knowledge-graph"
DOCS_DIR = CLAUDE_DIR / "docs"
TEMPLATE = CLAUDE_DIR / "hooks" / "kg-site-template.html"
CONVERSATIONS_DIR = CLAUDE_DIR / "conversations"
GITHUB_BASE = "https://github.com/kurnoolion/.claude/blob/main/conversations/"


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


def parse_conversation_metadata(md_path):
    """Extract title, date, and session/ID from a conversation markdown file header."""
    meta = {"filename": md_path.name}
    try:
        with open(md_path) as f:
            lines = []
            for line in f:
                lines.append(line)
                if len(lines) >= 8:
                    break
    except Exception:
        return None

    for line in lines:
        line = line.strip()
        if line.startswith("# "):
            meta["title"] = line[2:].strip()
        elif line.startswith("**Date:**"):
            meta["date"] = line.replace("**Date:**", "").strip()
        elif line.startswith("**ID:**"):
            raw = line.replace("**ID:**", "").strip().strip("`")
            meta["session_id"] = f"web-{raw}"
        elif line.startswith("**Session:**"):
            meta["session_id"] = line.replace("**Session:**", "").strip().strip("`")

    if "session_id" not in meta or "title" not in meta:
        return None
    return meta


def build_conversations():
    """Scan conversations/ directory and build metadata list."""
    convs = []
    if not CONVERSATIONS_DIR.exists():
        return convs
    for md_file in sorted(CONVERSATIONS_DIR.glob("*.md")):
        if md_file.name == "README.md":
            continue
        meta = parse_conversation_metadata(md_file)
        if meta:
            convs.append({
                "session_id": meta["session_id"],
                "title": meta.get("title", md_file.stem),
                "date": meta.get("date", ""),
                "url": GITHUB_BASE + md_file.name,
            })
    return convs


def build_entity_sessions(entities):
    """Group session_ids by entity (name, type) key."""
    sessions_by_entity = defaultdict(set)
    for e in entities:
        sid = e.get("session_id", "")
        if sid:
            key = (e.get("name", "").lower(), e.get("type", ""))
            sessions_by_entity[key].add(sid)
    return sessions_by_entity


def main():
    raw_entities = load_jsonl(KG_DIR / "entities.jsonl")
    entities = dedupe(raw_entities)
    rels = load_jsonl(KG_DIR / "relationships.jsonl")

    conversations = build_conversations()
    conv_session_ids = {c["session_id"] for c in conversations}

    entity_sessions = build_entity_sessions(raw_entities)

    entity_names = set()
    nodes = []
    for e in entities:
        name = e.get("name", "").strip()
        if not name:
            continue
        entity_names.add(name)
        key = (name.lower(), e.get("type", ""))
        sessions = sorted(entity_sessions.get(key, set()))
        nodes.append({
            "name": name,
            "type": e.get("type", "unknown"),
            "description": e.get("description", ""),
            "date": e.get("date", ""),
            "sessions": sessions,
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
    conv_data = json.dumps(conversations, ensure_ascii=False)

    DOCS_DIR.mkdir(parents=True, exist_ok=True)

    with open(TEMPLATE) as f:
        html = f.read()

    html = html.replace("__GRAPH_DATA__", graph_data)
    html = html.replace("__CONVERSATIONS__", conv_data)

    with open(DOCS_DIR / "index.html", "w") as f:
        f.write(html)

    print(f"Generated site: {len(nodes)} nodes, {len(edges)} edges, {len(conversations)} conversations")


if __name__ == "__main__":
    main()
