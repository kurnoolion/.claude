# Before and after workflow automation icons

**Date:** 2026-03-24  
**Source:** Claude Web/App  
**ID:** `65c2aeb6-7165-4f50-baa0-2ce14da1868f`

**Summary:** **Conversation Overview**

The person requested help creating a PowerPoint presentation to visually communicate the difference between manual and automated workflows, specifically for illustrating a before-and-after automation implementation story. No personal details, role, company, or team information were shared.

Claude built a complete four-slide PowerPoint deck using PptxGenJS and React Icons. The presentation used a red color theme for the "before" state and a green color theme for the "after" state to create immediate visual contrast. Slide 1 served as a title slide with a dark navy background and an orange lightning bolt icon as a decorative automation motif. Slide 2 depicted the manual workflow in a 3×2 card grid with icons representing clipboard-based data collection, spreadsheet entry, email distribution, manual review, approval chasing, and report generation, along with a pain points strip at the bottom. Slide 3 mirrored the layout with automation-era icons representing automated data ingestion, centralized data storage, smart notifications, AI-assisted review, live dashboards, and instant report generation, paired with a benefits strip. Slide 4 provided a side-by-side comparison table across four metrics: processing time, data accuracy, visibility, and reporting.

During QA, Claude identified that the bolt icon on the title slide was overlapping with the main heading text. This was corrected by repositioning the icon to the right side of the slide as a decorative background element with slight transparency, resolving the overlap without removing the visual element. The final file was delivered as a `.pptx` output.

---

## User

I want before and now icons to be used in PPT to show workflow before automation implementation and work flow after automation.

---

## Assistant

> **Tool:** view

<details>
<summary>Tool output</summary>

```
[{'type': 'text', 'text': '     1\t---\n     2\tname: pptx\n     3\tdescription: "Use this skill any time a .pptx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations; reading, parsing, or extracting text from any .pptx file (even if the extracted content will be used elsewhere, like in an email or summary); editing, modifying, or updating existing presentations; combining or splitting slide files; working with templates, lay
```
</details>

> **Tool:** view

<details>
<summary>Tool output</summary>

```
[{'type': 'text', 'text': '     1\t# PptxGenJS Tutorial\n     2\t\n     3\t## Setup & Basic Structure\n     4\t\n     5\t```javascript\n     6\tconst pptxgen = require("pptxgenjs");\n     7\t\n     8\tlet pres = new pptxgen();\n     9\tpres.layout = \'LAYOUT_16x9\';  // or \'LAYOUT_16x10\', \'LAYOUT_4x3\', \'LAYOUT_WIDE\'\n    10\tpres.author = \'Your Name\';\n    11\tpres.title = \'Presentation Title\';\n    12\t\n    13\tlet slide = pres.addSlide();\n    14\tslide.addText("Hello World!", { x: 
```
</details>

Now I'll build a polished "Before vs. After Automation" PowerPoint with workflow icons on each slide.

> **Tool:** bash_tool

---

## Assistant

> **Tool:** view

<details>
<summary>Tool output</summary>

```
[{'type': 'text', 'text': '     1\t---\n     2\tname: pptx\n     3\tdescription: "Use this skill any time a .pptx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations; reading, parsing, or extracting text from any .pptx file (even if the extracted content will be used elsewhere, like in an email or summary); editing, modifying, or updating existing presentations; combining or splitting slide files; working with templates, lay
```
</details>

> **Tool:** view

<details>
<summary>Tool output</summary>

```
[{'type': 'text', 'text': '     1\t# PptxGenJS Tutorial\n     2\t\n     3\t## Setup & Basic Structure\n     4\t\n     5\t```javascript\n     6\tconst pptxgen = require("pptxgenjs");\n     7\t\n     8\tlet pres = new pptxgen();\n     9\tpres.layout = \'LAYOUT_16x9\';  // or \'LAYOUT_16x10\', \'LAYOUT_4x3\', \'LAYOUT_WIDE\'\n    10\tpres.author = \'Your Name\';\n    11\tpres.title = \'Presentation Title\';\n    12\t\n    13\tlet slide = pres.addSlide();\n    14\tslide.addText("Hello World!", { x: 
```
</details>

Now I have all the info I need. Let me build a polished before/after automation workflow PPT with icons.

> **Tool:** bash_tool

<details>
<summary>Tool output</summary>

```
[{'type': 'text', 'text': '{"returncode":0,"stdout":"\\nchanged 29 packages in 6s\\n\\n3 packages are looking for funding\\n  run `npm fund` for details\\n","stderr":""}', 'uuid': '65400b93-231a-40b1-a404-1ca8b5c3db94'}]
```
</details>

> **Tool:** create_file

<details>
<summary>Tool output</summary>

```
[{'type': 'text', 'text': 'File created successfully: /home/claude/workflow_ppt.js', 'uuid': '852e82e1-d4e2-42cc-8fb2-b5e4097128b8'}]
```
</details>

> **Tool:** bash_tool

<details>
<summary>Tool output</summary>

```
[{'type': 'text', 'text': '{"returncode":0,"stdout":"✅ PPT created successfully!\\n","stderr":""}', 'uuid': 'b613ec41-e530-4be3-9474-14e2de7e5aef'}]
```
</details>

> **Tool:** bash_tool

<details>
<summary>Tool output</summary>

```
[{'type': 'text', 'text': '{"returncode":2,"stdout":"","stderr":"python: can\'t open file \'/home/claude/scripts/office/soffice.py\': [Errno 2] No such file or directory\\n"}', 'uuid': '7c67acbd-d17c-45dc-97d0-cf2006b85b64'}]
```
</details>

> **Tool:** bash_tool

<details>
<summary>Tool output</summary>

```
[{'type': 'text', 'text': '{"returncode":0,"stdout":"/mnt/skills/public/docx/scripts/office/soffice.py\\n/mnt/skills/public/pptx/scripts/office/soffice.py\\n/mnt/skills/public/xlsx/scripts/office/soffice.py\\n","stderr":""}', 'uuid': '7332c02e-78fa-43f0-99cf-fc0602de02d8'}]
```
</details>

> **Tool:** bash_tool

<details>
<summary>Tool output</summary>

```
[{'type': 'text', 'text': '{"returncode":1,"stdout":"convert /mnt/user-data/outputs/Workflow_Before_After_Automation.pptx as a Impress document -> /home/claude/Workflow_Before_After_Automation.pdf using filter : impress_pdf_Export\\n","stderr":"I/O Error: Couldn\'t open file \'/mnt/user-data/outputs/Workflow_Before_After_Automation.pdf\': No such file or directory.\\n"}', 'uuid': 'ffa58af6-15a3-472f-a446-8b43b014aa38'}]
```
</details>

> **Tool:** bash_tool

<details>
<summary>Tool output</summary>

```
[{'type': 'text', 'text': '{"returncode":0,"stdout":"/home/claude/Workflow_Before_After_Automation.pdf\\nconvert /home/claude/Workflow_Before_After_Automation.pptx as a Impress document -> /Workflow_Before_After_Automation.pdf using filter : impress_pdf_Export\\n/home/claude/Workflow_Before_After_Automation.pdf\\n","stderr":""}', 'uuid': '2bcc5ffc-f1a6-4ed0-8d73-b0a4c85350f9'}]
```
</details>

> **Tool:** bash_tool

<details>
<summary>Tool output</summary>

```
[{'type': 'text', 'text': '{"returncode":0,"stdout":"/home/claude/slide-1.jpg\\n/home/claude/slide-2.jpg\\n/home/claude/slide-3.jpg\\n/home/claude/slide-4.jpg\\n","stderr":""}', 'uuid': '7bbb2663-c20d-4860-aa48-fb725f2b552f'}]
```
</details>

> **Tool:** view

<details>
<summary>Tool output</summary>

```
[{'type': 'image', 'file_uuid': '019d205d-26d0-70e6-b9c3-4652fe14830c'}]
```
</details>

> **Tool:** view

<details>
<summary>Tool output</summary>

```
[{'type': 'image', 'file_uuid': '019d205d-5894-73df-9dda-9640cada2403'}]
```
</details>

> **Tool:** view

<details>
<summary>Tool output</summary>

```
[{'type': 'image', 'file_uuid': '019d205d-6baa-75f9-8cfd-4be52d264d8a'}]
```
</details>

> **Tool:** view

<details>
<summary>Tool output</summary>

```
[{'type': 'image', 'file_uuid': '019d205d-83b5-710d-b7c0-f0530e9fcfd9'}]
```
</details>

Slides 2, 3, and 4 look excellent. Just fixing the bolt icon overlap on slide 1:

> **Tool:** str_replace

<details>
<summary>Tool output</summary>

```
[{'type': 'text', 'text': 'Successfully replaced string in /home/claude/workflow_ppt.js', 'uuid': 'c4a5207f-ae07-42cc-89b1-d31ca619487b'}]
```
</details>

> **Tool:** bash_tool

<details>
<summary>Tool output</summary>

```
[{'type': 'text', 'text': '{"returncode":0,"stdout":"✅ PPT created successfully!\\nconvert /mnt/user-data/outputs/Workflow_Before_After_Automation.pptx as a Impress document -> /home/claude/Workflow_Before_After_Automation.pdf using filter : impress_pdf_Export\\nOverwriting: /home/claude/Workflow_Before_After_Automation.pdf\\ndone\\n","stderr":""}', 'uuid': '8eba397b-42f0-4c72-862e-26140c55140e'}]
```
</details>

> **Tool:** view

<details>
<summary>Tool output</summary>

```
[{'type': 'image', 'file_uuid': '019d205d-f581-773a-9012-168ea6d02c29'}]
```
</details>

All 4 slides look clean and polished. Let me present the final file.

> **Tool:** present_files

<details>
<summary>Tool output</summary>

```
[{'type': 'local_resource', 'file_path': '/mnt/user-data/outputs/Workflow_Before_After_Automation.pptx', 'name': 'Workflow Before After Automation', 'mime_type': 'application/vnd.openxmlformats-officedocument.presentationml.presentation', 'uuid': 'cd8178db-db4f-4487-938c-b91a36bef0af'}]
```
</details>

Your 4-slide deck is ready! Here's what's inside:

**Slide 1 — Title:** Dark navy background with a bold orange lightning bolt icon — immediately signals the automation theme.

**Slide 2 — Before Automation (Red):** Six workflow cards in a 3×2 grid, each with a unique icon (Clipboard, Spreadsheet, Email, Search, User Check, File) showing the manual pain points. Pain indicators at the bottom: High Time Consumption, Frequent Errors, Lack of Visibility.

**Slide 3 — After Automation (Green):** Mirror layout with automation-era icons (Robot, Database, Bell, AI Check, Live Chart, Download) showing the transformed workflow. Benefits strip: 10x Faster, Near-Zero Errors, Full Audit Visibility.

**Slide 4 — Impact at a Glance:** A clean side-by-side BEFORE vs AFTER comparison table across 4 metrics — Processing Time, Data Accuracy, Visibility, and Reporting — with matching icons for each row.

> **File:** slide-1.jpg

> **File:** slide-2.jpg

> **File:** slide-3.jpg

> **File:** slide-4.jpg

> **File:** slide-1.jpg

---
