# Wyckoff technical indicator for TradingView

**Date:** 2026-03-04  
**Source:** Claude Web/App  
**ID:** `cbf8c16a-4bf2-44ef-b754-8e4aafbd1944`

---

## User

I'm a swing trader, and occasional day trader. I want you to create Wyckoff technical indicator for tradingview in pine script.

Below are initial set of requirements. I will add lot more later.

1) Should adapt to time frame of the chart intraday, daily and weekly)
2) Should clearly show all labels per Wyckoff methodology
3) Use colored boxes to show various phases of Wyckoff methodology
4) Most common settings

---

## Assistant

> **Tool:** view

<details>
<summary>Tool output</summary>

```
[{'type': 'text', 'text': '3.9M\t/mnt/skills/public\n1.1M\t/mnt/skills/public/docx\n155K\t/mnt/skills/public/docx.skill\n1.5K\t/mnt/skills/public/docx/LICENSE.txt\n20K\t/mnt/skills/public/docx/SKILL.md\n1.1M\t/mnt/skills/public/docx/scripts\n15K\t/mnt/skills/public/frontend-design\n6.0K\t/mnt/skills/public/frontend-design.skill\n10K\t/mnt/skills/public/frontend-design/LICENSE.txt\n4.5K\t/mnt/skills/public/frontend-design/SKILL.md\n60K\t/mnt/skills/public/pdf\n22K\t/mnt/skills/public/pdf.skill\n1
```
</details>

I'll build a comprehensive Wyckoff indicator in Pine Script. This is a substantial piece of work — let me put it together properly.

> **Tool:** create_file

<details>
<summary>Tool output</summary>

```
[{'type': 'text', 'text': 'File created successfully: /home/claude/wyckoff_indicator.pine', 'uuid': 'be1cbd80-b7c0-4d75-a96d-e19dfb5ba53e'}]
```
</details>

> **Tool:** bash_tool

<details>
<summary>Tool output</summary>

```
[{'type': 'text', 'text': '{"returncode":0,"stdout":"","stderr":""}', 'uuid': '89371542-eb91-4bcc-adb0-08d930e2adc5'}]
```
</details>

> **Tool:** present_files

<details>
<summary>Tool output</summary>

```
[{'type': 'local_resource', 'file_path': '/mnt/user-data/outputs/wyckoff_indicator.pine', 'name': 'wyckoff indicator', 'mime_type': None, 'uuid': '3be2e72e-a9c6-456c-a612-4b015850ccac'}]
```
</details>

Here's your Wyckoff Method indicator for TradingView (Pine Script v5). To use it, open the Pine Editor in TradingView, paste the code, and add it to your chart.

Here's what it covers:

**Wyckoff Events Detected (all labeled on chart):**

*Accumulation side:* PS (Preliminary Support), SC (Selling Climax), AR (Automatic Rally), ST (Secondary Test), Spring, Test of Spring, SOS (Sign of Strength), LPS (Last Point of Support), BU (Back Up to Edge)

*Distribution side:* PSY (Preliminary Supply), BC (Buying Climax), AR (Automatic Reaction), ST (Secondary Test), UT (Upthrust), UTAD (Upthrust After Distribution), SOW (Sign of Weakness), LPSY (Last Point of Supply)

**Phase Boxes:** Color-coded overlays for Accumulation Phases A–E, Distribution Phases A–E, Markup, and Markdown — each with a descriptive label in the corner.

**Adaptive Timeframe:** Auto-detects intraday (1m–60m), daily, and weekly charts and adjusts lookback periods, volume averaging windows, and pivot detection lengths accordingly. You can also override with manual settings.

**Other features built in:**
- Dynamic support/resistance lines (dotted)
- Status table (top-right) showing current phase, trend, volume state, relative volume, and range position
- Optional volume spike bar coloring
- Every label has a detailed tooltip explaining the Wyckoff concept
- Alert conditions for all major events (SC, Spring, SOS, LPS, BC, UT, SOW, LPSY)

All colors, sensitivity thresholds, and visual toggles are configurable in the settings panel. Let me know what you'd like to add or refine next.

---
