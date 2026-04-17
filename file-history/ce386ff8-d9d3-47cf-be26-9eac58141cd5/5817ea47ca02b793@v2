# Plan: Configurability + Pin Strike + Strike Grid Fix

## Context
CLAUDE.md was updated with three clarifications/requirements:
1. **Pin strike definition** — clarified to "highest |value| in any individual column (for a given strike price), not row total". The current code already implements this correctly (scans individual cells, picks that cell's strike). **No code change needed.**
2. **Configurable strike count** — default 101 strikes (50 above + ATM + 50 below) should be env-var configurable as `STRIKES_PER_SIDE=N` → produces 2N+1 strikes.
3. **Configurable expiry months** — default 6 months should be env-var configurable as `EXP_MONTHS=N`.

There's also a **subtle correctness fix** needed in `build_strike_grid_centered`: the current code puts strikes `<= spot` in `below_list`, so an exact ATM strike can consume one of the 50 "below" slots (giving 50+50=100 instead of 50+1+50=101). The fix ensures ATM is always the center and N strikes exist on each side.

## Files to Modify

### 1. `D:/trading/gex-vex-dashboard/app.py`

**Change 1 — Lines 74–76: Read constants from env vars**

```python
# Before:
DEFAULT_STRIKES_ABOVE = 50
DEFAULT_STRIKES_BELOW = 50
DEFAULT_EXP_MONTHS = 6

# After:
DEFAULT_STRIKES_PER_SIDE = int(os.environ.get("STRIKES_PER_SIDE", "50"))
DEFAULT_STRIKES_ABOVE = DEFAULT_STRIKES_PER_SIDE
DEFAULT_STRIKES_BELOW = DEFAULT_STRIKES_PER_SIDE
DEFAULT_EXP_MONTHS = int(os.environ.get("EXP_MONTHS", "6"))
```

**Change 2 — Lines 96–105: Fix `build_strike_grid_centered` to ATM-centered logic**

```python
# Before:
def build_strike_grid_centered(all_strikes: set[float], spot: float,
                                above: int, below: int) -> list[float]:
    sorted_all = sorted(all_strikes)
    if not sorted_all:
        return []
    below_list = [s for s in sorted_all if s <= spot]
    above_list = [s for s in sorted_all if s > spot]
    selected_below = below_list[-below:] if below_list else []
    selected_above = above_list[:above] if above_list else []
    return sorted(set(selected_below + selected_above))

# After:
def build_strike_grid_centered(all_strikes: set[float], spot: float,
                                above: int, below: int) -> list[float]:
    sorted_all = sorted(all_strikes)
    if not sorted_all:
        return []
    atm = min(sorted_all, key=lambda s: abs(s - spot))
    atm_idx = sorted_all.index(atm)
    selected_below = sorted_all[max(0, atm_idx - below):atm_idx]
    selected_above = sorted_all[atm_idx + 1:atm_idx + 1 + above]
    return selected_below + [atm] + selected_above
```

This guarantees `2N+1` strikes centered on ATM. The rest of the call chain (`_build_matrix_core` → `build_matrix` / `build_matrix_fast`) is unchanged.

### 2. `D:/trading/gex-vex-dashboard/.env.example`

Append two documented, commented-out entries:

```
# Strikes to fetch above and below current price (default: 50 → 101 total)
# STRIKES_PER_SIDE=50

# Months of expirations to fetch for full matrix (default: 6)
# EXP_MONTHS=6
```

## What Does NOT Change
- `FAST_EXP_MONTHS = 1` — performance constant, not user-facing config
- Pin strike loop in `_build_matrix_core` (lines 190–193) — already correct
- `_build_matrix_core` signature — `strikes_above`/`strikes_below` params remain, fed from `DEFAULT_STRIKES_ABOVE`/`DEFAULT_STRIKES_BELOW`
- Frontend, data_store, greeks, tradier_client — no changes

## Verification
1. Set `STRIKES_PER_SIDE=3` in `.env`, restart server, subscribe a ticker → matrix should have 7 strikes (3 below ATM + ATM + 3 above)
2. Set `EXP_MONTHS=1`, restart → matrix expirations should cover ~1 month only
3. Remove both env vars → defaults restore (50 strikes per side, 6 months)
4. Check that ATM strike is always the center row in the matrix (not shifted by ±1)
