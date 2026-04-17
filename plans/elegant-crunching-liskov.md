# Plan: WebSocket Streaming — Add Dependency + Review/Test

## Context

The hybrid REST + WebSocket + SSE architecture is fully implemented across all files. The only hard gap is `websocket-client` missing from `requirements.txt`. User wants the dependency added plus a thorough code review for bugs or improvements.

## Step 1: Add Missing Dependency

**File: `requirements.txt`**
- Add `websocket-client>=1.8.0`

## Step 2: Code Review — Potential Issues to Investigate

### 2a. SSE heartbeat timeout mismatch
- `app.py` line 380: `q.get(timeout=25)` — heartbeat every 25s
- Browser `EventSource` default timeout varies by browser (typically 45–60s)
- **Check**: Is 25s appropriate or could it cause unnecessary reconnects?

### 2b. StreamingFetcher subscribes to underlyings only
- `_dispatch()` filters out symbols NOT in `self._symbols` (line 678–680)
- `build_occ_symbols()` exists but is never called in the streaming pipeline
- **Check**: Is this intentional? (Yes — we only need spot ticks for recalc, not individual option ticks. OCC symbols were built for potential future use.)

### 2c. Thread safety on `tick_count` / `recalc_count`
- `self.tick_count += 1` (line 694) and `self.recalc_count += 1` (line 715) — not atomic
- **Check**: These are diagnostics only, race conditions here are harmless. No fix needed.

### 2d. SSE generator exception handling
- `app.py` line 380: bare `except Exception` catches `queue.Empty` (timeout) — correct
- But also catches unexpected errors silently
- **Check**: Should we log unexpected errors separately?

### 2e. Chain snapshot staleness
- Chain snapshot stored by `_build_matrix_core()` on REST fetch
- Used by `recompute_matrix_from_spot()` on every WS tick
- BG fetcher refreshes every 55s → snapshot IV stays current
- **Check**: What if BG fetch fails for several cycles? Snapshot IV could drift. Add a staleness warning?

### 2f. CSS for `.cell--flash` animation
- `app.js` adds/removes `cell--flash` class (line 370–371) but...
- **Check**: Does `style.css` define the `.cell--flash` animation? Need to verify.

### 2g. `_skipSSEReconnect` edge case
- Set in `handleSSEUpdate()` around `renderHeatmap()` call
- **Check**: If `renderHeatmap()` throws, the flag stays `true` permanently → SSE never reconnects. Should wrap in try/finally.

## Step 3: Apply Fixes

Based on review findings, apply targeted fixes:
1. Add dependency to `requirements.txt`
2. Add `.cell--flash` CSS if missing
3. Wrap `_skipSSEReconnect` in try/finally in `app.js`
4. Any other issues found during review

## Step 4: Verification

1. `pip install -r requirements.txt` — verify `websocket-client` installs
2. `python app.py` — check logs for `[WS] StreamingFetcher STARTED`
3. Open `http://localhost:5050`, add a widget
4. Check `/api/debug` for `streamer.connected` and `tick_count`
5. Check `gexvex.log` for `[WS]` entries
6. **Note**: WS requires Tradier brokerage account (not sandbox)

## Files to Modify

| File | Change |
|------|--------|
| `requirements.txt` | Add `websocket-client>=1.8.0` |
| `static/style.css` | Add `.cell--flash` animation if missing |
| `static/app.js` | try/finally around `_skipSSEReconnect` |
| Other files | As needed from review findings |
