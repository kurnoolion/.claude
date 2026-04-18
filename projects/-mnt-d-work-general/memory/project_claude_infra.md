---
name: Claude Infrastructure Setup
description: SessionEnd hooks for KG extraction, conversation markdown, git sync, and cross-PC resume
type: project
originSessionId: f1decf82-056a-4e40-9581-ec12c85f5e6d
---
**Why:** Mohan wants a knowledge graph of all Claude interactions and browsable conversation history on GitHub.

**What's set up:**
- `.claude` repo synced to `github.com:kurnoolion/.claude.git`
- 3 SessionEnd hooks in `~/.claude/settings.json`:
  1. `sync-claude-to-git.sh` — auto-commit + push .claude changes
  2. `extract-knowledge.sh` — spawns background Haiku agent for KG extraction → entities.jsonl + relationships.jsonl
  3. `session-to-markdown.sh` — converts transcript JSONL to readable Markdown → conversations/
- `CLAUDE_KG_BATCH=1` env var suppresses hooks in batch/non-interactive sessions
- `build-graph.py` for KG visualization (summary, JSON, DOT, HTML)
- `import-claude-export.py` + `extract-kg-batch.py` for importing claude.ai data exports
- Windows toast notification on KG extraction completion
- Session states synced for cross-PC resume
- 14/45 web/app conversations timed out during KG extraction (120s limit) — can retry with higher timeout

**How to apply:** When resuming this work, check `~/.claude/knowledge-graph/` for current state and `conversations/README.md` for the index.
