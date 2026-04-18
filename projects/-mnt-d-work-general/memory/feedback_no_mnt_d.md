---
name: Never use /mnt/d/ paths
description: Always use /home/mohan/ paths, never /mnt/d/ WSL mount paths
type: feedback
originSessionId: f1decf82-056a-4e40-9581-ec12c85f5e6d
---
Always use `/home/mohan/` paths, never `/mnt/d/` paths.

**Why:** Mohan has symlinked `/mnt/d/` content to `/home/mohan/` so paths are consistent across all PCs and WSL instances. Using `/mnt/d/` breaks cross-PC session resume and is WSL2-specific.

**How to apply:** When running commands, referencing files, or writing paths in any file, always use `/home/mohan/` as the base. This includes working directory, git operations, and any file I/O.
