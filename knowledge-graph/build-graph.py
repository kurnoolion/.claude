#!/usr/bin/env python3
"""Build a knowledge graph from extracted session entities and relationships.

Usage:
    python build-graph.py              # Print summary
    python build-graph.py --json       # Export as JSON graph
    python build-graph.py --dot        # Export as Graphviz DOT
    python build-graph.py --html       # Export as interactive HTML (requires pyvis)
"""

import json
import sys
from collections import defaultdict
from pathlib import Path

KG_DIR = Path(__file__).parent
ENTITIES_FILE = KG_DIR / "entities.jsonl"
RELATIONSHIPS_FILE = KG_DIR / "relationships.jsonl"


def load_jsonl(path):
    items = []
    if not path.exists():
        return items
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    items.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    return items


def dedupe_entities(entities):
    seen = {}
    for e in entities:
        key = (e.get("name", "").lower(), e.get("type", ""))
        if key not in seen or len(e.get("description", "")) > len(seen[key].get("description", "")):
            seen[key] = e
    return list(seen.values())


def build_graph():
    entities = dedupe_entities(load_jsonl(ENTITIES_FILE))
    relationships = load_jsonl(RELATIONSHIPS_FILE)

    entity_index = {(e["name"].lower(), e["type"]): e for e in entities}

    graph = {
        "nodes": entities,
        "edges": relationships,
        "stats": {
            "total_nodes": len(entities),
            "total_edges": len(relationships),
            "node_types": dict(defaultdict(int)),
            "edge_types": dict(defaultdict(int)),
        },
    }

    for e in entities:
        graph["stats"]["node_types"][e.get("type", "unknown")] = (
            graph["stats"]["node_types"].get(e.get("type", "unknown"), 0) + 1
        )
    for r in relationships:
        graph["stats"]["edge_types"][r.get("type", "unknown")] = (
            graph["stats"]["edge_types"].get(r.get("type", "unknown"), 0) + 1
        )

    return graph


def print_summary(graph):
    stats = graph["stats"]
    print(f"Knowledge Graph: {stats['total_nodes']} entities, {stats['total_edges']} relationships\n")

    print("Entity types:")
    for t, count in sorted(stats["node_types"].items(), key=lambda x: -x[1]):
        print(f"  {t}: {count}")

    print("\nRelationship types:")
    for t, count in sorted(stats["edge_types"].items(), key=lambda x: -x[1]):
        print(f"  {t}: {count}")

    print("\nEntities:")
    for e in sorted(graph["nodes"], key=lambda x: x.get("type", "")):
        print(f"  [{e.get('type', '?')}] {e['name']}: {e.get('description', '')}")

    print("\nRelationships:")
    for r in graph["edges"]:
        print(f"  {r.get('source', '?')} --[{r.get('type', '?')}]--> {r.get('target', '?')}")


def export_json(graph):
    print(json.dumps(graph, indent=2))


def export_dot(graph):
    print("digraph KnowledgeGraph {")
    print("  rankdir=LR;")
    print('  node [shape=box, style=filled, fillcolor=lightyellow];')

    type_colors = {
        "person": "lightblue", "project": "lightgreen", "technology": "lightsalmon",
        "concept": "plum", "file": "lightyellow", "decision": "lightcoral",
        "task": "lightcyan", "problem": "mistyrose",
    }

    for e in graph["nodes"]:
        color = type_colors.get(e.get("type", ""), "white")
        label = f"{e['name']}\\n({e.get('type', '')})"
        safe_id = e["name"].replace(" ", "_").replace("-", "_").replace(".", "_")
        print(f'  "{safe_id}" [label="{label}", fillcolor={color}];')

    for r in graph["edges"]:
        src = r.get("source", "").replace(" ", "_").replace("-", "_").replace(".", "_")
        tgt = r.get("target", "").replace(" ", "_").replace("-", "_").replace(".", "_")
        print(f'  "{src}" -> "{tgt}" [label="{r.get("type", "")}"];')

    print("}")


def export_html(graph):
    try:
        from pyvis.network import Network
    except ImportError:
        print("Install pyvis: pip install pyvis", file=sys.stderr)
        sys.exit(1)

    net = Network(height="800px", width="100%", directed=True, notebook=False)
    type_colors = {
        "person": "#6CB4EE", "project": "#77DD77", "technology": "#FA8072",
        "concept": "#DDA0DD", "file": "#FFFACD", "decision": "#F08080",
        "task": "#E0FFFF", "problem": "#FFE4E1",
    }

    for e in graph["nodes"]:
        net.add_node(
            e["name"],
            label=e["name"],
            title=f"{e.get('type','')}: {e.get('description','')}",
            color=type_colors.get(e.get("type", ""), "#FFFFFF"),
        )

    for r in graph["edges"]:
        net.add_edge(r["source"], r["target"], title=r.get("type", ""), label=r.get("type", ""))

    out_path = str(KG_DIR / "knowledge-graph.html")
    net.show(out_path, notebook=False)
    print(f"Saved to {out_path}")


if __name__ == "__main__":
    graph = build_graph()

    if "--json" in sys.argv:
        export_json(graph)
    elif "--dot" in sys.argv:
        export_dot(graph)
    elif "--html" in sys.argv:
        export_html(graph)
    else:
        print_summary(graph)
