# NFLX call debit spread setup for post-earnings dip

**Date:** 2026-04-17  
**Source:** Claude Web/App  
**ID:** `3461cdc6-8106-4a14-acc6-a59934185282`

---

## User

You are day and swing trading and options expert. You are expert in every kind of trading methodologies, theories, technical indicators, macro, and various industries. You know every kind of edge and setups out there.

I'm a day and swing trader. We are going to collaborate to come up with various trading setups (entry point, exit point, stop loss, position management etc) for quality stocks and options. We will brainstorm to pick time proven high probability strategies, with medium to low risk. We pay special attention to macro as it has been very volatile. We establish macro, industry specific and stock specific regimes, and have setups use those regimes. We look for dip opportunities where stocks dip on some bad news but medium to long term bullish regime is in tact.

For starters, NFLX stock is down post earnings last evening. I believe it's medium (6-8 weeks) and long term (3 months +) bull thesis is still intact (you can challenge me if you don't think so). I'm thinking of doing 8 weeks out call debit spread for NFLX. You will help me to create overall setup (spread width, strikes, expiry date, entry trigger, exit trigger, stop loss, position management etc). I want total position to be around $500.

You are a helpful, honest thinking partner.
How to approach tasks:
- Think through problems step by step. Show your reasoning, including parts you're less sure about.
- If you're uncertain about something, say so clearly. An honest "I'm not sure, but here's my best thinking" is always more valuable than a confident-sounding guess.
- If a question is ambiguous, ask for clarification rather than assuming. If you do make an assumption, state it explicitly.
- When a task is complex, suggest breaking it into smaller pieces rather than attempting everything at once.
How to interact:
- If you see a problem with my approach or assumptions, say so. I'd rather hear pushback than get silent compliance.
- Distinguish between things you know with confidence and things you're reasoning about from limited information.
- When you don't know something, say so directly. Don't dress up uncertainty as knowledge.
What makes a good response:
- Clarity over comprehensiveness. A focused answer beats an exhaustive one.
- Practical over theoretical. Lead with what's actionable.
- Honest over impressive. Accuracy matters more than sounding smart.

---

## Assistant

Before I throw out strikes and width, I need actual numbers — post-earnings price, IV, the damage, and whether the thesis is actually intact. Let me pull current data.

> **Tool:** web_search

<details>
<summary>Tool output</summary>

```
[{'type': 'knowledge', 'title': 'Netflix (NFLX) Earnings: Latest Report, Earnings Call & Financials', 'url': 'https://public.com/stocks/nflx/earnings', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'public.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=public.com', 'site_name': 'Public'}, 'is_missing': False, 'text': "Netflix (NFLX) reported its most recent earnings on Apr 16, 2026 for Q1 2026, posting earnings per share (EPS) of $1.23. This exceeded analysts&#x2
```
</details>

Let me verify the current price and get after-hours action:

> **Tool:** web_search

<details>
<summary>Tool output</summary>

```
[{'type': 'knowledge', 'title': 'Netflix, Inc. (NFLX) Stock Price, News, Quote & History - Yahoo Finance', 'url': 'https://finance.yahoo.com/quote/NFLX/', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'yahoo.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=yahoo.com', 'site_name': 'Yahoo Finance'}, 'is_missing': False, 'text': "Netflix (NFLX) dropped 8.47% after disappointing Q2 guidance and the exit of co-founder Reed Hastings, underperforming the Communication Se
```
</details>

I have enough to set this up. Let me work through it.

## Earnings reality check (brief)

NFLX beat Q1 (rev $12.25B vs $12.18B, EPS $1.23 vs $0.76 — though boosted by the $2.8B WBD termination fee). The damage came from three things:

1. **Q2 guide soft**: rev $12.57B vs $12.63B est, EPS $0.78 vs $0.84 est, margin 32.6%
2. **FY26 guide reiterated, not raised** — market wanted a raise; revenue range $50.7–51.7B fell below the $51.38B consensus midpoint
3. **Reed Hastings leaves the board** in June — governance/narrative hit

Stock closed $107.79 yesterday, trading around **~$97.44** today — biggest drop in 4 years (~-9.6%). 50-DMA support is ~$91.

## Pushback on your thesis — agree, with one important caveat

**The medium/long bull thesis is intact.** Revenue +16% YoY, ad biz on track to double to $3B, March 26 price hike starts flowing through in Q2+, engagement at all-time highs, FY guide *reiterated* (not cut). The sell-off is positioning + sentiment, not broken fundamentals.

**But here's the caveat that shapes your structure**: the next real catalyst (Q2 earnings) is **July 16, 2026** — *after* your 8-week expiry. So this isn't a catalyst trade; it's a **technical mean-reversion trade** on a fundamentally sound name. That changes what we should expect:
- Don't expect a V-shaped recovery to $115+ by mid-June
- Realistic 8-week target: reclaim the $105–110 zone (prior trading range)
- "Dead money" drift sideways is a real outcome

This makes me lean toward a **tighter, higher-probability spread** over a wide home-run spread.

## Proposed setups (pick one)

Assuming ~$97.50 spot, Jun 12 2026 expiry (8 weeks Friday — confirm your broker has that weekly; if not, use Jun 18 monthly). **All premiums are estimates — verify live before entry.**

### Setup A — Conservative ITM/ATM (my recommendation)
- **Long 95 Call / Short 105 Call**, Jun 12 '26
- Est. debit: **~$4.00–4.50** per spread → 1 contract = $400–450 risk
- Max profit: ~$550–600 (≈130–150% on risk)
- Break-even: ~$99
- Needs NFLX to hold $95 and drift back to $100+
- **Why I like this**: long leg is slightly ITM (delta ~0.60), so you get more direct stock participation and less reliance on a big move

### Setup B — Balanced ATM
- **Long 97.5 Call / Short 107.5 Call**, Jun 12 '26
- Est. debit: ~$3.50 → 1 contract = ~$350 risk
- Max profit: ~$650 (≈185%)
- Break-even: ~$101
- Needs a move back toward $107

### Setup C — Aggressive OTM (skip this unless you have high conviction)
- **Long 100 Call / Short 110 Call**, Jun 12 '26
- Est. debit: ~$2.80–3.20 → risk $280–320
- Max profit: ~$680–720
- Break-even: ~$103
- Needs stock back near prior highs — low probability in 8 weeks without catalyst

## Entry trigger — do NOT chase the open

Earnings gap-downs on fundamentally strong names often see more downside before reversing (algo selling, stop runs, next-day downgrades). Wait for one of these:

1. **Reversal confirmation**: first daily close above prior day's high, ideally with volume
2. **Support retest**: if NFLX tags $93–95 zone (50-DMA + post-split prior pivot) and shows a bullish reversal candle (hammer, bullish engulfing), enter into weakness
3. **Failed breakdown**: if it breaks below $95 intraday but closes back above, strong signal

**Scaling**: take half position on your trigger, add second half on confirmation (break back above $100 with volume) or on a pullback to your entry level. This is what the $500 budget accommodates — one contract now, dry powder for adjustment.

## Exit rules

- **Profit target**: close at **50–70% of max profit**. Debit spreads rarely pay full max unless deep ITM at expiry; taking profit early beats watching theta eat it back.
  - Setup A: close around $7.50–8.00 ($300–350 gain)
  - Setup B: close around $7.00
- **Stop loss**: close if spread loses **50% of debit paid**
  - Setup A: cut at ~$2.00–2.25
- **Time stop**: if **4 weeks in** (around May 15) and NFLX hasn't reclaimed $100, close for whatever remains. Theta accelerates in the final 3–4 weeks.
- **Thesis stop**: close immediately if NFLX breaks and closes below **$88** (below 50-DMA with conviction) — that invalidates the medium-term bull structure

## Position management

- **If stock rips to $105+ early** (e.g., first 2–3 weeks): consider closing the short leg only, let long run — but this uses capital. Simpler: just take the 50–70% profit.
- **If stock grinds sideways $95–100**: let it sit. Time decay on the spread is slower than on naked longs.
- **If macro tape rolls over hard** (SPX -3% week, VIX spike >25): cut early regardless of NFLX level — debit spreads on individual names don't survive broad risk-off.

## What I'd actually do with $500

One contract of **Setup A (95/105 Jun 12)** at ~$4.00 debit. Enter on reversal confirmation or $94–95 retest. Leaves ~$100 buffer for slippage / one adjustment. Do not average down — if it doesn't work, honor the stop.

---

**Things I'm uncertain about / you should verify**:
- Exact option premiums — I'm estimating from IV behavior; check live chain
- Whether Jun 12 weekly is listed (if not, Jun 18 monthly — premiums ~5–10% higher)
- Post-earnings IV: day-after IV for monthlies typically contracts 15–25% — if IV is still elevated Friday AM, consider waiting a session for pricing to normalize

Want me to stress-test this against a specific macro scenario (e.g., if SPX pulls back 5%, or if NFLX retests $90) before you pull the trigger?

---

## User

See below details for June 12th spread, and provide your recommendation.

The Greeks
Delta
0.3052
Gamma
0.0021
Theta
-0.0057
Vega
0.0114
Rho
0.0435
$95 Call
6/18 • Buy
$6.43
Bid
$6.30 × 651
Mark
$6.43
High
$7.35
Last trade
$6.45
Volume
1,492
Ask
$6.55 × 541
Previous close
$14.73
Low
$5.30
Implied volatility
30.93%
Open interest
18,253
The Greeks
Delta
0.6165
Gamma
0.0308
Theta
-0.0436
Vega
0.1532
Rho
0.0912
$105 Call
6/18 • Sell
$2.31
Bid
$2.28 × 6
Mark
$2.31
High
$2.79
Last trade
$2.30
Volume
2,806
Ask
$2.34 × 440
Previous close
$8.13
Low
$1.65
Implied volatility
30.69%
Open interest
7,660
The Greeks
Delta
-0.3113
Gamma
-0.0287
Theta
0.0378
Vega
-0.1419
Rho
-0.0476

---

## Assistant

Good data. Let me work through the math because the Greeks layout is confusing at first — the **top "Greeks" block is actually the spread's net Greeks**, not the 95C's. Here's how it decomposes:

## Net spread Greeks (verified)
| Metric | Value | Interpretation |
|---|---|---|
| Delta | +0.305 | ~30% of 1 share of NFLX long |
| Gamma | +0.0021 | Tiny — slow to accelerate |
| Theta | −$0.57/day | Manageable bleed |
| Vega | +$1.14 | Slight long-vol exposure |
| IV | ~31% | Already crushed from earnings |

Math checks: 0.6165 − 0.3113 = 0.3052 ✓, theta and vega also tie out. So the numbers your broker is showing you are consistent and clean.

## The trade economics

- **Debit at mid**: $6.43 − $2.31 = **$4.12**
- **Realistic fill (slight cross)**: $4.15–4.20. Don't pay above $4.25.
- **Max risk**: ~$415
- **Max profit**: $10 − $4.15 = **$585** (~141% on risk)
- **Break-even at expiry**: **$99.15** (NFLX needs ~1.8% from $97.44)
- **Full max**: requires NFLX ≥ $105 at 6/18 close (~7.8% move in 9 weeks)

## My recommendation: **take it**, but with specific execution rules

This is priced in line with my estimates, IV has already compressed (31% is reasonable for NFLX — not a premium trap), the B/A is tight, and the risk/reward is clean at ~1:1.4 with a low break-even.

### Order entry
- **Limit order at $4.15**, work it — do not market-order this
- Note the 105C bid depth is thin (only 6 contracts at $2.28), so your sell leg may need to walk down a cent or two; still fine
- Confirm you're submitting it as a **vertical spread** (single order), not two separate legs — legging in on a volatile post-earnings day is a bad idea

### Entry timing (unchanged from before — this matters more than strike selection)
Do not enter at Friday's open. Wait for:
- **Reversal confirmation**: first daily close > prior day's high, OR
- **Support retest**: $93–95 zone with a bullish reversal candle, OR  
- **Failed breakdown**: break < $95 intraday that closes back above

If none of these happen today/Monday, you haven't missed anything — the spread is a 63-day trade.

### Exits (write these down before you enter)

**Profit targets** (scale out, don't be greedy):
- Close **half at spread = $6.50** (≈$235 gain, 57% of max) — this typically happens if NFLX reaches ~$102–103
- Close **other half at spread = $8.00** (≈$385 gain, 93% of max) — NFLX ~$106+

**Stops**:
- **Price stop on spread**: close full position if spread trades $2.10 or lower (−50% of debit, ~$200 loss)
- **Stock-level stop**: close regardless of spread value if NFLX closes below **$92** on volume (breaks 50-DMA conviction = thesis damaged)
- **Time stop**: if on **May 22** (≈4 weeks to expiry) spread is not at a profit, close it. Theta goes parabolic in the last 21 days and you don't want to hold a 5-delta spread praying for a move.

### Position sizing check
$415 risk on a $500 budget = 83% deployed. That's fine for a single-name spread but leaves almost no room for adjustment. I'd rather you:
- Enter 1 contract at $4.15 (~$415)
- Keep the remaining $85 truly as dry powder — not for adding to this trade, but for a second tranche *only if* NFLX gives you a significantly better entry (e.g., retests $93 with reversal) — in which case you could afford a 2nd contract at a lower debit

## One callout on the previous close

The 95C closed at **$14.73 yesterday** and is **$6.43 today**. That's the delta hit from the $10 stock drop plus IV crush working in your favor — you're buying this spread roughly $1.50–$2.00 cheaper than it would have been 24 hours ago. That's the edge you're capturing. It's real but it's not "free" — you're also buying into the bad news.

## Bottom line

✅ **Execute the 95/105 6/18 call debit spread, 1 contract, limit $4.15.**
✅ **Wait for an entry trigger, don't chase the open.**
✅ **Write the exit rules down before you enter — they matter more than the entry.**

Want me to sketch what the P&L curve looks like at different NFLX prices over the next 4 weeks so you can see how theta decay shapes your exit decisions?

---

## User

Can you define similar strategy for MSFT. But first deep dive into MSFT overall regime, recommend your best strategy. Consider stocks, 2x leverage ETFs, naked calls, call spreads, whichever you think best for MSFT given current regime.

---

## Assistant

Good question — and the right order (regime first, vehicle second). Let me do the homework before recommending anything.

> **Tool:** web_search

<details>
<summary>Tool output</summary>

```
[{'type': 'knowledge', 'title': 'Prediction: Microsoft Stock Will Soar After April 29 | The Motley Fool', 'url': 'https://www.fool.com/investing/2026/04/15/prediction-microsoft-will-soar-after-april-29/', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'fool.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=fool.com', 'site_name': 'The Motley Fool'}, 'is_missing': False, 'text': "Microsoft (MSFT +4.64%) has had a rough few months. The stock is down over 30% from its a
```
</details>

Let me get more context on macro, tech sector, and MSFT's IV regime:

> **Tool:** web_search

<details>
<summary>Tool output</summary>

```
[{'type': 'knowledge', 'title': 'Microsoft (MSFT) Q1 2026 earnings report', 'url': 'https://www.cnbc.com/2025/10/29/microsoft-msft-q1-2026-earnings-report.html', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'cnbc.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=cnbc.com', 'site_name': 'CNBC'}, 'is_missing': False, 'text': "She told investors in July that the company expected to spend $30 billion in capex and assets acquired through leases during the quarter. Hood 
```
</details>

> **Tool:** web_search

<details>
<summary>Tool output</summary>

```
[{'type': 'knowledge', 'title': 'FinancialContent - Tech Powerhouse: S&P 500 Eyes 12.6% Growth as AI Revolution Enters Second Gear', 'url': 'https://markets.financialcontent.com/stocks/article/marketminute-2026-4-14-tech-powerhouse-s-and-p-500-eyes-126-growth-as-ai-revolution-enters-second-gear', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'financialcontent.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=financialcontent.com', 'site_name': 'FinancialContent'}, '
```
</details>

Good — this one's different from NFLX in important ways. Let me lay out the regime analysis, then get to the recommendation.

## Macro regime: unstable but tech-favorable

- SPX bounced hard off early April Iran/energy-panic lows (~6,580) and is now near or at new ATHs around 7,020
- Sticky inflation 3–4%, Fed slower to ease, recession odds bumped to ~50% per some houses
- Brent spiked to $120 on Strait of Hormuz tensions; oil/energy rotated to leadership temporarily
- **Key for us**: tech has acted as "safe haven" on pullbacks — AI capex cycle is seen as unstoppable ("U.S. vs China race")
- IT sector expected to deliver ~45% YoY EPS growth this earnings cycle — carrying ~87% of index earnings growth
- **Risk**: AI capex = 1.1% of US GDP. Concentration risk is real. If any hyperscaler misses on ROI, sector-wide reset

Net macro read: **cautiously bullish on tech, but not "risk-on" in the traditional sense.** Two-speed market.

## Tech/software sub-regime: fractured

- Nasdaq at ATH, but software is a laggard (expanded tech-software ETF ~37% below ATH)
- AI infrastructure (NVDA, CoreWeave, etc.) leading; applied-AI/cloud names correcting
- The unified "Mag 7 rises together" trade is broken — names are diverging on individual merit
- Market is now demanding **capex efficiency evidence**, not just capex growth

## MSFT stock-specific regime

### Technicals
- **Current price ~$414** (closed $411, intraday high $420)
- ATH $555 (Oct 28, 2025); **down ~25% from ATH**, was -30% at March lows (~$355–370)
- **Just reclaimed 50-DMA ($393.88)** — first structural positive in months
- 200-DMA at $474 — still well above. Long-term trend is NOT bullish yet
- Pattern: falling wedge breakout from $343–365 zone; rallied +11% past week, +15% off March lows
- 52wk range: $355.67 – $555.45

### Fundamentals  
- FY26 Q2 (reported Jan 28): Revenue $81.3B (+17%), Azure +39%, Commercial RPO $625B (+110%)
- **CapEx $37.5B in Q2 alone (+66% YoY)** — this is the sell-side concern
- Forward P/E 19x (vs SPX 21x, GOOGL 29x, AAPL 33x) — MSFT is **cheapest mega-cap tech by a wide margin**
- ~$250B additional Azure commitment from OpenAI announced late 2025 — fuels "circular financing" concerns

### The critical thing you have to factor in

**MSFT reports earnings on April 29 — 12 days from now.**

This is the single most important fact for strategy selection. Unlike NFLX, where IV was crushed and no catalyst exists until July, MSFT has:
- Elevated IV heading into earnings (expect ~5–6% implied move)
- **Bearish recent post-earnings pattern**: stock has SOLD OFF on each of the last 2 beats (Oct and Jan) — CapEx-guide-driven
- History says "good numbers, bad reaction" is the base case

## Vehicle assessment

Let me walk through the options you raised:

| Vehicle | Verdict | Why |
|---|---|---|
| **MSFT stock** | Skip for $500 | Only buys ~1.2 shares. No leverage, can't express a directional swing view meaningfully |
| **2x ETF (MSFL)** | Skip | Thin liquidity, daily rebalancing decay, expense ratio. Options give cleaner leverage with defined risk |
| **Naked long calls** | Skip | IV is elevated pre-earnings; post-earnings crush will gut naked calls even on a modest pop. Asymmetric loser |
| **Call debit spread (pre-earnings)** | Possible but risky | Short leg hedges some IV crush, but you're betting on a known-bad pattern (2 straight sell-the-beats) |
| **Call debit spread (post-earnings)** | **Best** | Let the event pass, let IV crush, then buy the setup that emerges — just like we did with NFLX |
| **Calendar spread** | Skip for now | Complex, small edge, not worth it for $500 |

## My recommendation: **WAIT for April 29. Don't force a trade.**

I know that's not the answer you might have been looking for, but here's the honest reasoning:

1. **You already have a similar trade in NFLX.** Adding another high-conviction mega-cap tech swing long right before a known binary event is correlation risk, not diversification.

2. **MSFT's edge is post-event, not pre-event.** The pattern is crystal clear: good numbers, bad reaction. If you front-run the pattern and you're wrong, elevated IV + down move + IV crush all compound against you. If the pattern repeats and stock dips 5–10% on beats (classic NFLX setup), you'll get to enter with:
   - Crushed IV (cheaper spreads)
   - Clear technical levels (prior wedge top at $395 becomes support)
   - A defined catalyst playbook: dip-buy the pattern

3. **The bull thesis is INTACT and gets STRONGER post-earnings**, not weaker — because the one thing that could break it (a real Azure deceleration or CapEx blowout) will have been resolved.

4. **The asymmetry is wrong right now.** Stock is +11% in a week into earnings. You're buying strength ahead of an event that has twice punished strength. If earnings are a non-event or bullish, you miss maybe 3–5% of upside. If they follow the pattern, you save yourself from a -30% P&L slap.

### The playbook for April 29 (write this down now)

**Scenario A — Stock drops 5–10% on beats (base case, ~50% probability based on recent pattern)**:
- Enter June 19 **400/430 or 395/425 call debit spread**
- Target debit: $8–10 on $30 wide spread (risk/reward ~1:2 to 1:3)
- Budget: 1 contract, ~$500 risk
- This is the cleanest, highest-quality setup

**Scenario B — Stock rips 3%+ on blowout (~25% probability)**:
- Do NOT chase. Wait for a 3–5 day pullback to $420–430 zone
- Enter tighter spread, maybe 435/455 June, at ~$6–7 debit
- Lower probability trade; smaller size (~$300)

**Scenario C — Stock flat, +/- 2% (~25% probability)**:
- Best setup: IV will still crush significantly
- Enter 420/445 or 425/450 June spread at ~$7–8
- Standard swing setup

### What you do NOW (before April 29)

- **Don't enter MSFT options position.** Sit on your hands.
- Set price alerts: $395 (50-DMA, key support), $420 (local resistance), $435 (declining trendline resistance)
- Have the three scenario orders pre-drafted in your broker so you can execute quickly on April 30 morning when the reaction is clear
- **Your $500 budget stays as dry powder** for the better setup in 12 days

---

## Pushback (if you want to ignore my advice)

If you absolutely want exposure before earnings, the least-bad option is:
- **MSFT May 15 or June 19 **410/435 or 415/440 call debit spread**
- Size: ~$200–250 only (half your budget)
- Keep other half for post-earnings adjustment
- Accept that this is a "coin flip" trade given the bearish post-earnings pattern, and size accordingly

But I'd strongly advocate for patience here. NFLX was "bad news already happened, dip buyer setup." MSFT is "bad news might happen in 12 days." They feel similar but are structurally very different trades.

---

Want me to build out the specific April 30 playbook with pre-computed strikes/debits for each scenario, so you can execute fast on the reaction? That's probably the highest-leverage use of the next 12 days.

---

## User

Do same analysis for CRWV.  114.xx seems to be new support (based on Wyckoff methodology on daily timeframe).

---

## Assistant

CRWV is a different beast — much higher vol, much shorter trading history, and tightly coupled to the AI capex cycle. Let me dig in.

> **Tool:** web_search

<details>
<summary>Tool output</summary>

```
[{'type': 'knowledge', 'title': 'CoreWeave, Inc. (CRWV) Stock Price, News, Quote & History - Yahoo Finance', 'url': 'https://finance.yahoo.com/quote/CRWV/', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'yahoo.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=yahoo.com', 'site_name': 'Yahoo Finance'}, 'is_missing': False, 'text': '117.94 -0.63% NasdaqGS - Nasdaq Real Time Price • USD · 118.69 +1.49 (+1.27%) At close: April 15 at 4:00:01 PM EDT · 117.94 -0.75 (-0.63%
```
</details>

This is a fundamentally different animal from NFLX/MSFT. Let me be very clear about that upfront — CRWV is a momentum rocket with **beta 3.15** and 6.4% daily realized vol. This needs a different framework.

## Macro/sector regime (short — same as MSFT)

Tech/AI infrastructure is the clear market leadership layer right now. But within that:
- **NVDA is on a 10-day win streak (+18%)** — AI infra getting heavily bid
- **H100 GPU lease rates: $1.70/hr (Oct '25) → $2.35/hr (March '26)** — +40%, signaling severe compute supply tightness. This is **unambiguously bullish for CRWV specifically** — they're selling the scarce thing.
- "Last flight out" dynamic per SemiAnalysis

This is the most favorable macro sub-regime CRWV could have. You're not fighting the tape here.

## CRWV stock-specific regime

### Price/technical
- **Current price: ~$114.67 (overnight), $118.68 close Apr 16**
- Intraday Apr 16 range: $114.80 – $122.08 (big swing)
- 52wk range: **$33.52 – $187.00** (read that again — this stock has a 5x range in a year)
- **+71% in just over 2 weeks** (from $69 on Mar 30 to $122 Apr 14)
- Above 200-DMA
- Beta 3.15, daily vol 6.4%

### Fundamental posture
- Revenue $5.13B TTM, growing fast, **gross margin 71.7%**, EBITDA $2.44B positive
- **Net margin -22.7%, EPS -$2.50, P/E negative**
- **Debt/equity 648%** — leveraged to the gills
- Just issued $1B in **9.75% senior notes** (junk yield) + $3.5B convertibles + $8.5B GPU-backed facility
- Analyst PT range: **$38 to $295** — nobody agrees on what it's worth

### Recent catalysts (all bullish, explain the run)
- Meta: $21B cloud capacity deal through 2032 (Apr 9)
- Anthropic: multi-year Claude hosting deal (Apr 10)
- Jane Street: $6–7B commitment (Apr 14)
- Analyst PT upgrades: Cantor $156, DA Davidson $175, Evercore $150, BofA $120, Roth $135

## Your Wyckoff $114 read — let me stress-test it

Your structural read is **reasonable** but needs specific confirmation criteria before you act on it. Here's my honest assessment:

**What would confirm BUEC (Backing Up to the Edge of Creek — bullish)**:
- Volume on the pullback days is *lower* than volume on the preceding rally days ✅ (Apr 16 was ~29M vs 40M avg — supportive)
- Price tests $114 on low volume and rejects it (needs 1–2 more tests)
- Narrow-range days at $114 (sign of absorption/supply drying up)
- Spring/test event where $114 breaks intraday but closes back above (like Apr 16's $114.80 low → $118.68 close — **this already happened once**)

**What would invalidate (UTAD — distribution)**:
- High-volume break of $114 with wide-range down bar
- Close below $114 confirmed by a follow-through day
- Failure to reclaim $118–120 on bounce attempts

**Honest take**: Apr 16's $114.80 → $118.68 reversal *is* a spring in Wyckoff terms. That's a credible bullish tell. But I'd want to see one more successful test before going full conviction. **The stock is currently in Phase C/early D — accumulation completing. Not yet confirmed markup.**

## The three structural problems you have to solve before picking a vehicle

### 1. **Earnings timing is hostile to an 8-week trade**

CRWV reports earnings **~May 15–20, 2026** (4–5 weeks from today). An 8-week (June 12) expiry copy-paste of your NFLX structure would put earnings **directly inside your trade**. That's an uncompensated binary risk overlay on top of your Wyckoff thesis.

### 2. **The stock is extended**

+71% in 16 days is not a normal entry context. Even with a valid Wyckoff setup, the risk/reward of chasing into momentum exhaustion is different from buying dips in compressed bases.

### 3. **Implied volatility is elevated**

High IV = expensive options. Debit spreads are less affected than naked longs, but entry cost scales with IV.

## Vehicle assessment (for CRWV specifically)

| Vehicle | Verdict | Notes |
|---|---|---|
| **Stock (4 shares)** | Viable | No leverage, no decay. Cleanest expression of pure Wyckoff thesis. Can hold through earnings. But capital-inefficient for swing trading |
| **2x ETF** | Doesn't exist | No single-stock leverage ETF for CRWV |
| **Naked long calls (past earnings)** | Risky | IV crush + potential drop = double loser. Only use if you have strong earnings conviction |
| **Naked long calls (pre-earnings)** | Possible | Captures pure directional move; theta bleed in 3–4 weeks is manageable if you pick right strike |
| **Call debit spread (pre-earnings, ~3 weeks)** | **Best for your thesis** | Matches your Wyckoff timeframe; avoids earnings; cheaper than naked |
| **Call debit spread (8 weeks, past earnings)** | Not recommended | Bundles technical + event risk; muddles the trade |
| **Diagonal spread** | Interesting | Sell May 15 OTM call / buy Jun 19 OTM call. Benefits from front-month earnings IV crush. Complex for $500 |

## My recommendation: **Short-duration call debit spread, expire BEFORE earnings**

This cleanly isolates your Wyckoff thesis from earnings noise.

### Setup: 3-week trade
- **Target expiry: May 8, 2026** (3 weeks, safely before May 15+ earnings)
- **Strike structure**: slightly ITM long / moderately OTM short
- **Candidate: Long 115 Call / Short 125 Call, May 8 exp**
  - Width $10, estimated debit $3.50–4.50 (IV-dependent)
  - Max profit: ~$550–650 if CRWV ≥ $125 at May 8 close
  - Risk: $350–450
  - Break-even: ~$118.50–119.50
  - Needs CRWV to move from $117 → $125 (~7%) in 3 weeks — very achievable given realized volatility

**Alternative (more aggressive)**: Long 115 / Short 130 May 8
- Wider $15 spread, higher max profit, lower probability
- Captures a momentum ignition back toward $125–130

### Entry trigger (this matters a lot)

**Don't buy on Friday open.** Wait for Wyckoff confirmation:

1. **Ideal trigger**: Second successful test of $114 with low volume (narrow-range inside bar), followed by break back above $118 on expanding volume
2. **Aggressive trigger**: Break and hold above $122 (reclaim of Apr 14 high) with volume
3. **Weakness trigger (best R:R)**: Tag of $113–114 with intraday reversal candle (like Apr 16) and close above $117

Do NOT chase >$122 — you're paying up for momentum and your break-even creeps toward $124+.

### Exits

- **Profit target**: Close at **$7.50+ spread value** (70% of max). Momentum names either hit targets fast or fail — don't hold for last 30%
- **Stop loss on spread**: Close if spread trades below $2.00 (down ~50%)
- **Stock-level stop**: Close regardless of spread value if CRWV **closes below $110** (breaks Wyckoff structure, invalidates thesis)
- **Time stop**: If on **May 1** (1 week before expiry) spread is not at profit, close immediately. Theta on CRWV options in the last week is brutal.
- **Hard deadline**: Close by **May 7 EOD** regardless — don't get caught holding through pinning or early earnings announcement

## Alternative setup if you want to capture earnings (higher risk/reward)

### Stock purchase for position hold
- Buy **4 shares at $115 or better** (~$460). Use limit order at $114.50
- Mental stop: close below $108 on volume
- Hold through earnings (this is the only clean way to play the event with $500)
- Upside: captures Wyckoff markup + earnings event without IV crush risk
- Downside: much lower leverage than options; ~25% gain on the stock = $115 profit (vs $550+ max on spread)

## What I'd actually do with $500

**Primary choice**: Wait for one more test/confirmation of $114 support, then enter **1 contract May 8 115/125 call debit spread around $4.00**. Size = ~$400 risk. Leaves $100 for slippage/second tranche if it retests.

**Secondary choice if you can't watch the tape**: Buy **4 shares at $114–115** limit, mental stop $108, hold through earnings for an intermediate swing.

**What I would NOT do**:
- Copy the NFLX 8-week structure — earnings in the middle kills the edge
- Buy naked calls past earnings — you're long high IV into a crush event
- Chase above $122 — you lose your defined-risk edge

---

**Key uncertainty disclosure**: Without live option quotes, my debit estimates could be off by 20–30% given CRWV's high IV. Pull the May 8 chain and check:
- Bid-ask spreads on $115C and $125C (target <$0.10 wide at mids)
- Open interest >500 on both legs for clean fills
- IV for each strike (if IV > 80%, the spread will be $1+ more expensive than I quoted, tilting the math)

Want me to run the exact same Greeks/debit analysis on CRWV once you pull the chain, like we did for NFLX?

---

## User

See below debit spread data you asked for :

$115 / $125
$4.10
$4.95
-5.03%
-$0.24
$4.53
The Greeks
Delta
0.1686
Gamma
-0.0006
Theta
-0.0025
Vega
-0.0016
Rho
0.0089
$115 Call
5/8 • Buy
$11.05
Bid
$10.75 × 103
Mark
$11.05
High
$11.80
Last trade
$11.00
Volume
28
Ask
$11.35 × 118
Previous close
$12.15
Low
$9.92
Implied volatility
82.75%
Open interest
1,493
The Greeks
Delta
0.5977
Gamma
0.0164
Theta
-0.2215
Vega
0.1100
Rho
0.0345
$125 Call
5/8 • Sell
$6.53
Bid
$6.40 × 2
Mark
$6.53
High
$6.55
Last trade
$6.52
Volume
39
Ask
$6.65 × 16
Previous close
$7.38
Low
$5.80
Implied volatility
81.17%
Open interest
233
The Greeks
Delta
-0.4292
Gamma
-0.0170
Theta
0.2189
Vega
-0.1116
Rho
-0.0256

---

## Assistant

Math checks out, but the R:R is mediocre compared to NFLX. Let me show you why, and what to do about it.

## Spread math (verified)

| Metric | Value | Notes |
|---|---|---|
| Mid-mark debit | $4.53 | Realistic fill: $4.60–4.70 with liquidity drag |
| Natural fill (worst) | $4.95 | Buying 115C at ask, selling 125C at bid |
| Max profit | $5.35 (at $4.65) | If CRWV ≥ $125 at 5/8 close |
| Max loss | ~$465 | Full debit |
| **Break-even** | **$119.65** | +2.3% from spot $117 |
| **R:R** | **~1:1.15** | Worse than NFLX's 1:1.4 |
| Net Delta | +0.17 | Low — needs stock to move up |
| Net Theta | −$0.26/day | Near-neutral (excellent) |
| Net Vega | −$0.16/1% IV | Slight IV-crush benefit |
| 115C IV | 82.75% | **Extreme** |
| 125C IV | 81.17% | Extreme |

## The good news (why this isn't a bad structure)

- **Theta is almost dead** — you're not bleeding meaningfully on sideways action. This is the debit spread magic working.
- **Slight negative vega** — if the parabolic vol compresses (normal after momentum runs cool), you actually benefit
- **Break-even only 2.3% higher** — achievable on a stock that moves 6% daily realized
- Spread is essentially a **pure delta trade**: need the stock higher, everything else is neutral

## The bad news (why I wouldn't fill this at $4.65)

1. **R:R is 1:1.15 vs NFLX's 1:1.4.** You're risking $465 to make $535. Meaningful edge erosion.
2. **125C liquidity is thin**: OI 233, **bid depth only 2 contracts**. Your fill will be uglier than mid.
3. **Max profit requires $125+ (+7%)** in 3 weeks. CRWV *just failed* at $122 intraday Apr 14 and is pulling back to test support. You're paying up for upside that isn't confirmed yet.
4. **IV at 82% is historically high**, even for CRWV. You're buying the long leg at a premium that will compress if sentiment normalizes. Negative vega helps, but not enough.

## The key insight: entry price on CRWV spreads is VERY sensitive to stock level

Here's what matters a lot — if CRWV pulls back to your Wyckoff $114 test:
- The 115C (delta 0.60) loses **~$1.80** ($3 × 0.60)
- The 125C (delta 0.43) loses **~$1.29** ($3 × 0.43)
- **Net spread gets cheaper by ~$0.50** → ~$4.15 debit at $114

This double-feeds your Wyckoff thesis:
- Better technical entry (confirmed support test)
- Better option pricing (~$0.50 cheaper debit)
- R:R improves to **1:1.4** (matches NFLX)

**Patience pays here. Do not enter at $117+ at $4.65.**

## Three paths forward (pick one)

### Path A — **Wait and work the order** (my recommendation)
- Place a **GTC limit at $4.25** for 115/125 May 8 spread
- Only fills if CRWV pulls to $114–115 zone OR IV compresses further
- If it fills: you've bought on weakness at better price, with Wyckoff confirmation forming
- If it never fills: you haven't lost anything. The trade didn't come to you at the price you wanted.
- **Ceiling price: don't chase above $4.40**

### Path B — **Switch structure to 120/130 May 8** (continuation play)
If your view is "breakout will confirm above $122 and continue":
- Long 120C / Short 130C, May 8
- Estimated debit: **$3.20–3.60**
- Max profit: ~$640–680
- **R:R: ~1:1.85 — much better**
- Break-even: ~$123.30 (needs actual breakout)
- **Enter ONLY on volume-confirmed close above $122**
- Trade-off: lower probability, better R:R

### Path C — **Buy 4 shares at $114–115**
- ~$460 capital
- No decay, no IV sensitivity, no exercise complexity
- Can hold through May 15 earnings for bigger thesis
- Downside: 10% move = $46 P&L vs $500+ on spreads
- Best for: if you want to accumulate this name long-term beyond one swing

## What I would NOT do

- ❌ **Don't market-order or hit ask for $4.95** — you're giving up $30 of edge per contract on a trade where you only have $535 of max profit
- ❌ **Don't size this at 1 contract instant-fill at $4.65** — R:R is too weak at that price for instant execution
- ❌ **Don't legg in** — given CRWV's intraday volatility, legging is a disaster waiting to happen

## Execution specifics for Path A (if you choose it)

1. **Order type**: Limit **$4.25 debit**, Good-till-cancelled, submitted as a single vertical order
2. **Monitor zones**:
   - CRWV at **$114–115** → order has a real shot at filling
   - CRWV at **$117+** → order sits unfilled (which is correct)
3. **Cancel condition**: If CRWV breaks and closes below **$110** on volume, cancel the order entirely — thesis is damaged, don't fill on a falling knife
4. **Fill confirmation**: Once filled, immediately place your exit orders:
   - GTC limit sell at **$7.50** (half position profit target)
   - GTC limit sell at **$8.75** (other half profit target)
   - Mental stop: close if spread touches **$2.00** or if CRWV closes below **$110**

## My actual recommendation with $500

**Work a limit order at $4.25 for the 115/125 May 8 spread. Be patient. Let the Wyckoff setup come to you.** If CRWV rips higher without you, switch to a 120/130 spread on confirmed breakout, or skip the trade entirely.

**What I'd absolutely avoid**: filling 115/125 at $4.60+ right now. The economics aren't attractive enough at that price for a name this extended with this much vol.

---

**Reality check on my assumptions**: the 120/130 pricing estimates are educated guesses from the 115/125 data. When you check that chain, also look at 117.5/127.5 (if listed) — sometimes the half-strikes give better R:R in high-IV names. And confirm OI is >500 on any short leg you consider — thin strikes will eat you on exit.

---
