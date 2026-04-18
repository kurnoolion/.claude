---
name: Collaboration Protocol
description: Multi-environment pipeline workflow for team collaboration across dev PC (with Claude) and work laptop (no Claude, 16GB NVIDIA GPU)
type: project
originSessionId: 2dd2cfbc-8085-4803-b413-7f6835b40b88
---
Multi-machine workflow established 2026-04-15:
- Dev PC: co-develop with Claude, push to github.com
- Work laptop: clone repo, pull changes, run pipeline on proprietary docs, push to internal github
- Team members: pull from internal github, contribute corrections/eval via defined environments

**Why:** User cannot send company docs/info outside company premises. Claude has no access to work artifacts.

**How to apply:**
- Pipeline runner (`src/pipeline/run_cli.py`) handles end-to-end orchestration with environment configs
- Compact report format (RPT/HW/MDL/stage lines) is the standard for pasting results in chat
- QC templates (QC env stage) and FIX templates (FIX env artifact) for structured feedback
- Error codes (EXT-E001, PRF-W001, etc.) for remote debugging without full logs
- Model picker auto-selects best Ollama model for detected hardware
- Environment system (`src/env/`) manages per-member scoped workspaces
- Corrections go in `corrections/` dir (profile.json, taxonomy.json) — pipeline auto-detects
- User-supplied eval Q&A pairs in `eval/*.xlsx` — pipeline auto-loads
- Work laptop has 16GB NVIDIA GPU — enables larger/faster models than dev PC
