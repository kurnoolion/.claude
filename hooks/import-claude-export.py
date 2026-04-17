#!/usr/bin/env python3
"""Import Claude web/app data export into .claude repo.

Converts conversations.json to:
  - conversations/*.md (readable Markdown pages)
  - knowledge-graph/entities.jsonl + relationships.jsonl (via background extraction)
  - conversations/README.md (updated index)

Also imports memories.json into the memory system.

Usage:
    python import-claude-export.py /path/to/export-dir [--extract-kg]
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path


CLAUDE_DIR = Path.home() / ".claude"
CONV_DIR = CLAUDE_DIR / "conversations"
KG_DIR = CLAUDE_DIR / "knowledge-graph"
MEMORY_DIR = CLAUDE_DIR / "projects" / "-mnt-d-work-general" / "memory"


def slugify(text):
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text[:60].strip('-')


def parse_date(iso_str):
    try:
        dt = datetime.fromisoformat(iso_str.replace('Z', '+00:00'))
        return dt.strftime('%Y-%m-%d'), dt.strftime('%H%M')
    except (ValueError, AttributeError):
        return "unknown", "0000"


def render_conversation(conv):
    """Convert a conversation dict to Markdown."""
    name = conv.get("name", "Untitled")
    uuid = conv.get("uuid", "unknown")
    created = conv.get("created_at", "")
    date, time = parse_date(created)
    messages = conv.get("chat_messages", [])

    lines = []
    lines.append(f"# {name}")
    lines.append("")
    lines.append(f"**Date:** {date}  ")
    lines.append(f"**Source:** Claude Web/App  ")
    lines.append(f"**ID:** `{uuid}`")
    lines.append("")

    summary = conv.get("summary", "")
    if summary:
        lines.append(f"**Summary:** {summary}")
        lines.append("")

    lines.append("---")
    lines.append("")

    for msg in messages:
        sender = msg.get("sender", "unknown")
        role_label = "User" if sender == "human" else "Assistant"
        lines.append(f"## {role_label}")
        lines.append("")

        content_blocks = msg.get("content", [])
        if isinstance(content_blocks, list):
            for block in content_blocks:
                if isinstance(block, dict):
                    btype = block.get("type", "")
                    if btype == "text":
                        text = block.get("text", "").strip()
                        if text:
                            lines.append(text)
                            lines.append("")
                    elif btype == "tool_use":
                        tool_name = block.get("name", "unknown")
                        lines.append(f"> **Tool:** {tool_name}")
                        lines.append("")
                    elif btype == "tool_result":
                        result = block.get("text", str(block.get("content", "")))
                        if result and len(str(result)) > 10:
                            lines.append("<details>")
                            lines.append("<summary>Tool output</summary>")
                            lines.append("")
                            lines.append("```")
                            lines.append(str(result)[:500])
                            lines.append("```")
                            lines.append("</details>")
                            lines.append("")
                elif isinstance(block, str) and block.strip():
                    lines.append(block)
                    lines.append("")
        else:
            text = msg.get("text", "")
            if text:
                lines.append(text)
                lines.append("")

        # Attachments
        attachments = msg.get("attachments", [])
        if attachments:
            for att in attachments:
                fname = att.get("file_name", att.get("name", "attachment"))
                lines.append(f"> **Attachment:** {fname}")
                lines.append("")

        files = msg.get("files", [])
        if files:
            for f in files:
                fname = f.get("file_name", f.get("name", "file"))
                lines.append(f"> **File:** {fname}")
                lines.append("")

        lines.append("---")
        lines.append("")

    return "\n".join(lines), name, date, time, uuid


def update_index(conv_dir):
    """Regenerate the conversations README.md index."""
    conv_path = Path(conv_dir)
    md_files = sorted(conv_path.glob("*.md"), reverse=True)
    md_files = [f for f in md_files if f.name != "README.md"]

    lines = []
    lines.append("# Claude Conversations")
    lines.append("")
    lines.append("Readable archive of Claude sessions (Code + Web/App), auto-generated.")
    lines.append("")
    lines.append(f"**Total conversations:** {len(md_files)}")
    lines.append("")
    lines.append("| Date | Source | Conversation |")
    lines.append("|------|--------|-------------|")

    for f in md_files:
        date_prefix = f.name[:10] if len(f.name) > 10 else "?"
        with open(f) as fh:
            title = "Untitled"
            source = "Code"
            for line in fh:
                line = line.strip()
                if line.startswith("# "):
                    title = line[2:]
                if "**Source:** Claude Web/App" in line:
                    source = "Web/App"
                    break
                if "**Session:**" in line:
                    source = "Code"
                    break
        lines.append(f"| {date_prefix} | {source} | [{title}]({f.name}) |")

    lines.append("")
    return "\n".join(lines)


def build_kg_transcript(conv):
    """Build a simplified transcript for KG extraction."""
    lines = []
    for msg in conv.get("chat_messages", []):
        sender = msg.get("sender", "unknown")
        role = "User" if sender == "human" else "Assistant"
        text = msg.get("text", "")
        if text:
            lines.append(f"{role}: {text[:2000]}")
    return "\n".join(lines)


def import_memories(export_dir):
    """Import Claude web/app memories into the memory system."""
    mem_file = Path(export_dir) / "memories.json"
    if not mem_file.exists():
        return

    with open(mem_file) as f:
        data = json.load(f)

    if not data:
        return

    MEMORY_DIR.mkdir(parents=True, exist_ok=True)

    memory_text = data[0].get("conversations_memory", "")
    if not memory_text:
        return

    mem_path = MEMORY_DIR / "imported_web_app_memory.md"
    with open(mem_path, "w") as f:
        f.write("""---
name: Claude Web/App Memory Import
description: Memory context imported from Claude web/app conversations (2026-04-17)
type: user
---

""")
        f.write(memory_text)
        f.write("\n")

    print(f"Imported memories to: {mem_path}")

    # Update MEMORY.md index
    memory_index = MEMORY_DIR / "MEMORY.md"
    existing = ""
    if memory_index.exists():
        with open(memory_index) as f:
            existing = f.read()

    if "imported_web_app_memory.md" not in existing:
        with open(memory_index, "a") as f:
            if not existing:
                f.write("# Memory Index\n\n")
            f.write("- [Claude Web/App Memory Import](imported_web_app_memory.md) — user context imported from Claude web/app\n")
        print(f"Updated memory index: {memory_index}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("export_dir", help="Path to Claude data export directory")
    parser.add_argument("--extract-kg", action="store_true", help="Run KG extraction on each conversation")
    args = parser.parse_args()

    export_dir = Path(args.export_dir)
    conv_file = export_dir / "conversations.json"

    if not conv_file.exists():
        print(f"Error: {conv_file} not found")
        sys.exit(1)

    with open(conv_file) as f:
        conversations = json.load(f)

    print(f"Found {len(conversations)} conversations")

    CONV_DIR.mkdir(parents=True, exist_ok=True)
    KG_DIR.mkdir(parents=True, exist_ok=True)

    # Track what we write for KG extraction
    kg_transcripts = []
    imported = 0
    skipped = 0

    for conv in conversations:
        markdown, name, date, time, uuid = render_conversation(conv)
        slug = slugify(name) if name else slugify(uuid)
        filename = f"{date}_{time}_web_{slug}.md"
        output_path = CONV_DIR / filename

        if output_path.exists():
            skipped += 1
            continue

        with open(output_path, "w") as f:
            f.write(markdown)

        imported += 1

        if args.extract_kg:
            transcript_text = build_kg_transcript(conv)
            if transcript_text:
                kg_transcripts.append({
                    "session_id": f"web-{uuid}",
                    "date": date,
                    "text": transcript_text,
                })

    print(f"Imported: {imported}, Skipped (already exists): {skipped}")

    # Update index
    index = update_index(CONV_DIR)
    with open(CONV_DIR / "README.md", "w") as f:
        f.write(index)
    print("Updated conversations index")

    # Import memories
    import_memories(export_dir)

    # Write KG extraction queue if requested
    if args.extract_kg and kg_transcripts:
        queue_path = KG_DIR / "import-queue.jsonl"
        with open(queue_path, "w") as f:
            for t in kg_transcripts:
                f.write(json.dumps(t) + "\n")
        print(f"Wrote {len(kg_transcripts)} conversations to KG extraction queue: {queue_path}")
        print(f"Run KG extraction with: python {CLAUDE_DIR}/hooks/extract-kg-batch.py")


if __name__ == "__main__":
    main()
