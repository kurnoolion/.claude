---
name: DocumentProfiler Design Decision
description: Standalone LLM-free profiler derives document structure from representative docs; replaces hard-coded per-MNO parsers with generic profile-driven parser
type: project
originSessionId: 63c6b7f4-a800-49d2-8865-a7c6236450d5
---
DocumentProfiler replaces per-MNO parser registry (old decisions #3 and #10). Key properties:
- Standalone module/executable, independent of LLM APIs
- Heuristic analysis only (font clustering, regex mining, frequency analysis)
- Outputs human-editable JSON profile (document_profile.json)
- One-time offline step, perfected before ingestion pipeline runs
- Updatable by providing more representative docs and/or manual JSON editing
- One profile per MNO document format (e.g., VZW OA requirements, TMO requirements)

**Why:** Scalability — adding new MNO requires zero code changes, just profile representative docs. Format changes between releases require re-profiling, not code modification.
**How to apply:** PoC uses LTEDATARETRY.pdf + LTEB13NAC.pdf as representative docs for VZW OA profile. DocumentProfiler is PoC Step 2 (after content extraction, before structural parsing). Supported formats: PDF, DOC, DOCX, XLS, XLSX.
