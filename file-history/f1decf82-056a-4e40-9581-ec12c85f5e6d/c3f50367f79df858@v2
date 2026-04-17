#!/usr/bin/env python3
"""Batch KG extraction for imported conversations.

Reads import-queue.jsonl and spawns claude processes to extract
entities and relationships from each conversation.

Usage:
    python extract-kg-batch.py [--max-parallel 3] [--dry-run]
"""

import argparse
import json
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

CLAUDE_DIR = Path.home() / ".claude"
KG_DIR = CLAUDE_DIR / "knowledge-graph"
QUEUE_FILE = KG_DIR / "import-queue.jsonl"
PROMPT_FILE = CLAUDE_DIR / "hooks" / "kg-extract-prompt.txt"
LOG_DIR = KG_DIR / "logs"


def load_queue():
    if not QUEUE_FILE.exists():
        return []
    items = []
    with open(QUEUE_FILE) as f:
        for line in f:
            line = line.strip()
            if line:
                items.append(json.loads(line))
    return items


def get_processed():
    """Check which sessions have already been processed."""
    processed = set()
    log_file = KG_DIR / "extraction.log"
    if log_file.exists():
        with open(log_file) as f:
            for line in f:
                if "SUCCESS" in line:
                    for part in line.split():
                        if part.startswith("web-"):
                            processed.add(part)
    return processed


def extract_one(item, prompt_template, dry_run=False):
    """Run KG extraction on a single conversation."""
    session_id = item["session_id"]
    date = item["date"]
    text = item["text"]

    LOG_DIR.mkdir(parents=True, exist_ok=True)

    # Write transcript text to a temp file for the agent to read
    tmp = tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False,
                                      dir=str(KG_DIR))
    tmp.write(text)
    tmp.close()

    entities_file = str(KG_DIR / "entities.jsonl")
    rels_file = str(KG_DIR / "relationships.jsonl")

    # Ensure output files exist
    for f in [entities_file, rels_file]:
        Path(f).touch()

    prompt = f"""You are a knowledge graph extraction agent. Read the conversation transcript below and extract entities and relationships.

## Entity Types
person, project, technology, concept, file, decision, task, problem

## Relationship Types
uses, depends_on, built_with, related_to, part_of, created, modified, solved, caused, blocked_by, decided, worked_on, learned, prefers

## Output
Read existing entities from {entities_file} first to avoid duplicates (match by name+type).
Append new entities to {entities_file} — one JSON per line:
{{"name":"X","type":"technology","description":"...","properties":{{}},"session_id":"{session_id}","date":"{date}"}}

Append new relationships to {rels_file} — one JSON per line:
{{"source":"X","target":"Y","type":"uses","context":"...","session_id":"{session_id}","date":"{date}"}}

## Rules
- Skip trivial/generic entities. Focus on meaningful things.
- Keep descriptions under 100 chars.
- Do NOT modify existing lines — only append.
- If the conversation has no meaningful entities, write nothing.

## Conversation Transcript
Read the file at: {tmp.name}
"""

    if dry_run:
        print(f"  [DRY RUN] Would extract from {session_id} ({len(text)} chars)")
        os.unlink(tmp.name)
        return True

    log_path = LOG_DIR / f"{session_id}.log"

    try:
        result = subprocess.run(
            ["claude", "-p", prompt,
             "--allowedTools", "Read,Write,Glob,Grep",
             "--model", "claude-haiku-4-5-20251001"],
            capture_output=True, text=True, timeout=120
        )

        with open(log_path, "w") as f:
            f.write(result.stdout)
            if result.stderr:
                f.write("\n--- STDERR ---\n")
                f.write(result.stderr)

        success = result.returncode == 0

        with open(KG_DIR / "extraction.log", "a") as f:
            status = "SUCCESS" if success else f"FAILED (exit {result.returncode})"
            f.write(f"[{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}] {status} {session_id}\n")

        return success

    except subprocess.TimeoutExpired:
        with open(KG_DIR / "extraction.log", "a") as f:
            f.write(f"[{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}] TIMEOUT {session_id}\n")
        return False
    finally:
        os.unlink(tmp.name)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-parallel", type=int, default=1, help="Max parallel extractions")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    queue = load_queue()
    if not queue:
        print("No items in extraction queue.")
        return

    processed = get_processed()
    remaining = [item for item in queue if item["session_id"] not in processed]

    print(f"Queue: {len(queue)} total, {len(processed)} already processed, {len(remaining)} remaining")

    if not remaining:
        print("All conversations already processed!")
        return

    success = 0
    failed = 0

    for i, item in enumerate(remaining, 1):
        print(f"[{i}/{len(remaining)}] Extracting from {item['session_id']}...")
        if extract_one(item, None, dry_run=args.dry_run):
            success += 1
        else:
            failed += 1

    print(f"\nDone: {success} succeeded, {failed} failed")

    # Show current KG stats
    for fname in ["entities.jsonl", "relationships.jsonl"]:
        fpath = KG_DIR / fname
        if fpath.exists():
            with open(fpath) as f:
                count = sum(1 for line in f if line.strip())
            print(f"  {fname}: {count} entries")


if __name__ == "__main__":
    main()
