---
name: Never use /home/mohan/ paths
description: Always use /home/mohan/ paths, never /home/mohan/ WSL mount paths
type: feedback
originSessionId: f1decf82-056a-4e40-9581-ec12c85f5e6d
---
Always use `/home/mohan/` paths, never `/home/mohan/` paths.

**Why:** Mohan has symlinked `/home/mohan/` content to `/home/mohan/` so paths are consistent across all PCs and WSL instances. Using `/home/mohan/` breaks cross-PC session resume and is WSL2-specific.

**How to apply:** When running commands, referencing files, or writing paths in any file, always use `/home/mohan/` as the base. This includes working directory, git operations, and any file I/O.
