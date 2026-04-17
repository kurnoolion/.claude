#!/bin/bash
# Auto-commit and push .claude changes on session end
CLAUDE_DIR="$HOME/.claude"

cd "$CLAUDE_DIR" || exit 0

# Skip if not a git repo yet
[ -d .git ] || exit 0

git add -A
git diff --cached --quiet && exit 0

git commit -m "auto-sync $(date +%F-%H%M)"
git push 2>/dev/null || true
