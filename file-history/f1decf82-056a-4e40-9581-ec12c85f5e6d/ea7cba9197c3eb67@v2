#!/usr/bin/env python3
"""Convert a Claude Code session transcript (JSONL) to human-readable Markdown."""

import argparse
import json
import os
import re
import sys
from pathlib import Path


def parse_transcript(path):
    """Parse JSONL transcript into structured messages."""
    messages = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue

            msg_type = entry.get("type")
            if msg_type in ("user", "human"):
                text = extract_user_text(entry)
                if text:
                    messages.append({"role": "user", "content": text})
            elif msg_type == "assistant":
                parts = extract_assistant_parts(entry)
                if parts:
                    messages.append({"role": "assistant", "content": parts})
    return messages


def extract_user_text(entry):
    """Extract text from a user message entry."""
    msg = entry.get("message", entry)
    content = msg.get("content", "")
    if isinstance(content, str):
        return content.strip()
    if isinstance(content, list):
        texts = []
        for block in content:
            if isinstance(block, str):
                texts.append(block)
            elif isinstance(block, dict):
                if block.get("type") == "text":
                    text = block.get("text", "")
                    if not text.startswith("<system-reminder>"):
                        texts.append(text)
        return "\n".join(texts).strip()
    return ""


def extract_assistant_parts(entry):
    """Extract text and tool use from an assistant message entry."""
    msg = entry.get("message", entry)
    content = msg.get("content", "")
    if isinstance(content, str):
        return [{"type": "text", "text": content}] if content.strip() else []

    parts = []
    if isinstance(content, list):
        for block in content:
            if isinstance(block, str):
                if block.strip():
                    parts.append({"type": "text", "text": block})
            elif isinstance(block, dict):
                btype = block.get("type", "")
                if btype == "text":
                    text = block.get("text", "").strip()
                    if text and not text.startswith("<system-reminder>"):
                        parts.append({"type": "text", "text": text})
                elif btype == "tool_use":
                    parts.append({
                        "type": "tool_use",
                        "tool": block.get("name", "unknown"),
                        "input": block.get("input", {}),
                    })
                elif btype == "tool_result":
                    result_content = block.get("content", "")
                    if isinstance(result_content, list):
                        for rc in result_content:
                            if isinstance(rc, dict) and rc.get("type") == "text":
                                result_content = rc.get("text", "")
                                break
                        else:
                            result_content = str(result_content)
                    parts.append({
                        "type": "tool_result",
                        "tool_use_id": block.get("tool_use_id", ""),
                        "content": str(result_content)[:500],
                    })
    return parts


def format_tool_use(tool, input_data):
    """Format a tool use block for Markdown."""
    tool_name = tool
    summary = ""

    if tool in ("Read", "read"):
        summary = f"Read `{input_data.get('file_path', '?')}`"
    elif tool in ("Write", "write"):
        summary = f"Write to `{input_data.get('file_path', '?')}`"
    elif tool in ("Edit", "edit"):
        summary = f"Edit `{input_data.get('file_path', '?')}`"
    elif tool in ("Bash", "bash"):
        cmd = input_data.get("command", "")
        if len(cmd) > 120:
            cmd = cmd[:120] + "..."
        summary = f"Run: `{cmd}`"
    elif tool in ("Glob", "glob"):
        summary = f"Search files: `{input_data.get('pattern', '?')}`"
    elif tool in ("Grep", "grep"):
        summary = f"Search for: `{input_data.get('pattern', '?')}`"
    elif tool in ("Agent", "agent"):
        summary = f"Spawn agent: {input_data.get('description', '?')}"
    elif tool in ("WebSearch", "web_search"):
        summary = f"Web search: {input_data.get('query', '?')}"
    elif tool in ("WebFetch", "web_fetch"):
        summary = f"Fetch: `{input_data.get('url', '?')}`"
    else:
        summary = f"{tool_name}"
        if input_data:
            args = ", ".join(f"{k}={repr(v)[:60]}" for k, v in list(input_data.items())[:3])
            summary += f"({args})"

    return summary


def generate_title(messages):
    """Generate a title from the first user message."""
    for msg in messages:
        if msg["role"] == "user":
            text = msg["content"]
            text = re.sub(r'\s+', ' ', text).strip()
            if len(text) > 80:
                text = text[:77] + "..."
            return text
    return "Untitled Session"


def slugify(text):
    """Convert text to a filename-safe slug."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text[:60].strip('-')


def render_markdown(messages, session_id, date):
    """Render messages as Markdown."""
    title = generate_title(messages)
    lines = []
    lines.append(f"# {title}")
    lines.append("")
    lines.append(f"**Date:** {date}  ")
    lines.append(f"**Session:** `{session_id}`")
    lines.append("")
    lines.append("---")
    lines.append("")

    for msg in messages:
        if msg["role"] == "user":
            lines.append("## User")
            lines.append("")
            lines.append(msg["content"])
            lines.append("")
        elif msg["role"] == "assistant":
            lines.append("## Assistant")
            lines.append("")
            for part in msg["content"]:
                if part["type"] == "text":
                    lines.append(part["text"])
                    lines.append("")
                elif part["type"] == "tool_use":
                    summary = format_tool_use(part["tool"], part.get("input", {}))
                    lines.append(f"> **Tool:** {summary}")
                    lines.append("")
                elif part["type"] == "tool_result":
                    content = part.get("content", "")
                    if content and len(content) > 10:
                        lines.append("<details>")
                        lines.append("<summary>Tool output</summary>")
                        lines.append("")
                        lines.append("```")
                        lines.append(content[:500])
                        lines.append("```")
                        lines.append("</details>")
                        lines.append("")
            lines.append("---")
            lines.append("")

    return "\n".join(lines), title


def update_index(conv_dir):
    """Regenerate the conversations README.md index."""
    conv_path = Path(conv_dir)
    md_files = sorted(conv_path.glob("*.md"), reverse=True)
    md_files = [f for f in md_files if f.name != "README.md"]

    lines = []
    lines.append("# Claude Conversations")
    lines.append("")
    lines.append("Readable archive of Claude Code sessions, auto-generated on session end.")
    lines.append("")
    lines.append(f"**Total conversations:** {len(md_files)}")
    lines.append("")
    lines.append("| Date | Conversation |")
    lines.append("|------|-------------|")

    for f in md_files:
        date_prefix = f.name[:10] if len(f.name) > 10 else "?"
        with open(f) as fh:
            first_line = fh.readline().strip().lstrip("# ")
        lines.append(f"| {date_prefix} | [{first_line}]({f.name}) |")

    lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--transcript", required=True)
    parser.add_argument("--session-id", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--date", required=True)
    parser.add_argument("--time", default="0000")
    args = parser.parse_args()

    messages = parse_transcript(args.transcript)
    if not messages:
        print("No messages found in transcript, skipping.")
        return

    markdown, title = render_markdown(messages, args.session_id, args.date)
    slug = slugify(title)
    filename = f"{args.date}_{args.time}_{slug}.md"
    output_path = os.path.join(args.output_dir, filename)

    with open(output_path, "w") as f:
        f.write(markdown)
    print(f"Wrote: {output_path}")

    index = update_index(args.output_dir)
    with open(os.path.join(args.output_dir, "README.md"), "w") as f:
        f.write(index)
    print("Updated index: README.md")


if __name__ == "__main__":
    main()
