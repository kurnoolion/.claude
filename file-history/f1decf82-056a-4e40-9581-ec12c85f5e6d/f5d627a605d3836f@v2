#!/bin/bash
# Post-session hook: convert session transcript to human-readable Markdown
# Output goes to ~/.claude/conversations/ and gets git-synced automatically

INPUT=$(cat)
TRANSCRIPT_PATH=$(echo "$INPUT" | jq -r '.transcript_path')
SESSION_ID=$(echo "$INPUT" | jq -r '.session_id')
REASON=$(echo "$INPUT" | jq -r '.reason')

# Skip non-meaningful session endings
case "$REASON" in
  clear|resume) exit 0 ;;
esac

# Skip if transcript doesn't exist or is trivially small
[ -f "$TRANSCRIPT_PATH" ] || exit 0
LINES=$(wc -l < "$TRANSCRIPT_PATH")
[ "$LINES" -lt 10 ] && exit 0

CONV_DIR="$HOME/.claude/conversations"
LOG_FILE="$CONV_DIR/.conversion.log"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

mkdir -p "$CONV_DIR"

DATE=$(date +%Y-%m-%d)
TIME=$(date +%H%M)

# Run conversion in background
nohup bash -c "
  python3 \"$SCRIPT_DIR/transcript-to-md.py\" \
    --transcript \"$TRANSCRIPT_PATH\" \
    --session-id \"$SESSION_ID\" \
    --output-dir \"$CONV_DIR\" \
    --date \"$DATE\" \
    --time \"$TIME\" \
    >> \"$LOG_FILE\" 2>&1

  EXIT_CODE=\$?
  if [ \$EXIT_CODE -eq 0 ]; then
    echo \"[\$(date -u +%Y-%m-%dT%H:%M:%SZ)] SUCCESS converted session $SESSION_ID\" >> \"$LOG_FILE\"
  else
    echo \"[\$(date -u +%Y-%m-%dT%H:%M:%SZ)] FAILED session $SESSION_ID (exit \$EXIT_CODE)\" >> \"$LOG_FILE\"
  fi
" > /dev/null 2>&1 &

exit 0
