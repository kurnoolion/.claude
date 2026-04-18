#!/bin/bash
# Post-session hook: extract knowledge graph entities from session transcript
# Runs in background so it doesn't block session teardown

INPUT=$(cat)
TRANSCRIPT_PATH=$(echo "$INPUT" | jq -r '.transcript_path')
SESSION_ID=$(echo "$INPUT" | jq -r '.session_id')
REASON=$(echo "$INPUT" | jq -r '.reason')

# Skip non-meaningful session endings
case "$REASON" in
  clear|resume) exit 0 ;;
esac

# Skip if running inside a batch/non-interactive claude -p session
[ "$CLAUDE_KG_BATCH" = "1" ] && exit 0

# Skip if transcript doesn't exist or is trivially small
[ -f "$TRANSCRIPT_PATH" ] || exit 0
LINES=$(wc -l < "$TRANSCRIPT_PATH")
[ "$LINES" -lt 10 ] && exit 0

KG_DIR="$HOME/.claude/knowledge-graph"
LOG_DIR="$KG_DIR/logs"
PROMPT_FILE="$HOME/.claude/hooks/kg-extract-prompt.txt"

mkdir -p "$KG_DIR" "$LOG_DIR"

# Ensure output files exist
touch "$KG_DIR/entities.jsonl" "$KG_DIR/relationships.jsonl"

# Build the full prompt with session-specific details
DATE=$(date +%Y-%m-%d)
PROMPT=$(cat "$PROMPT_FILE")
PROMPT="$PROMPT

## Session Details
- Transcript path: $TRANSCRIPT_PATH
- Session ID: $SESSION_ID
- Date: $DATE
- Entities file: $KG_DIR/entities.jsonl
- Relationships file: $KG_DIR/relationships.jsonl"

# Spawn background claude process for extraction, then notify on completion
nohup bash -c "
  CLAUDE_KG_BATCH=1 claude -p \"$PROMPT\" \
    --allowedTools 'Read,Write,Glob,Grep' \
    --permission-mode bypassPermissions \
    --model claude-haiku-4-5-20251001 \
    > \"$LOG_DIR/$SESSION_ID.log\" 2>&1
  EXIT_CODE=\$?

  ENTITIES=\$(wc -l < \"$KG_DIR/entities.jsonl\" 2>/dev/null || echo 0)
  RELS=\$(wc -l < \"$KG_DIR/relationships.jsonl\" 2>/dev/null || echo 0)

  if [ \$EXIT_CODE -eq 0 ]; then
    MSG=\"Knowledge graph updated: \${ENTITIES} entities, \${RELS} relationships\"
    echo \"[$(date -u +%Y-%m-%dT%H:%M:%SZ)] SUCCESS session $SESSION_ID — \$MSG\" >> \"$KG_DIR/extraction.log\"
    python3 \"$HOME/.claude/hooks/generate-kg-readme.py\" > /dev/null 2>&1
    powershell.exe -Command \"[System.Reflection.Assembly]::LoadWithPartialName('System.Windows.Forms') | Out-Null; [System.Windows.Forms.MessageBox]::Show('\$MSG', 'Claude KG Extraction', 'OK', 'Information')\" > /dev/null 2>&1 &
  else
    echo \"[$(date -u +%Y-%m-%dT%H:%M:%SZ)] FAILED session $SESSION_ID (exit \$EXIT_CODE)\" >> \"$KG_DIR/extraction.log\"
    powershell.exe -Command \"[System.Reflection.Assembly]::LoadWithPartialName('System.Windows.Forms') | Out-Null; [System.Windows.Forms.MessageBox]::Show('KG extraction failed for session. Check logs.', 'Claude KG Extraction', 'OK', 'Error')\" > /dev/null 2>&1 &
  fi
" > /dev/null 2>&1 &

# Log that extraction was triggered
echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] Triggered KG extraction for session $SESSION_ID ($LINES lines)" \
  >> "$KG_DIR/extraction.log"

exit 0
