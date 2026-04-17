# Claude Code powershell integration issue

**Date:** 2026-04-03  
**Source:** Claude Web/App  
**ID:** `c9599d88-2a68-47dd-865e-bf6a533a8647`

**Summary:** **Conversation Overview**

The person sought help setting up and using Claude Code, starting with a troubleshooting issue where the VS Code extension was opening a PowerShell terminal but failing with a "command not found" error. Claude explained that the VS Code extension requires the `claude` CLI to be pre-installed on the system, and walked through the installation process using the native PowerShell installer (`irm https://claude.ai/install.ps1 | iex`), along with the requirement for Git for Windows, PATH configuration, and OAuth authentication steps.

After successful setup, the person asked how conversation history is stored and maintained. Claude explained that Claude Code automatically saves all sessions as `.jsonl` files in `~/.claude/projects/`, with a global history file at `~/.claude/history.jsonl`. Key commands covered included `claude --continue` and `claude --resume` for resuming sessions, and the community tool `claude-conversation-extractor` for exporting readable Markdown or HTML versions of conversations. An important caveat was noted: sessions are directory-specific, so users must `cd` into the correct project folder before resuming.

The person then asked about accessing their PC's Claude Code sessions from a mobile phone. Claude described the built-in Remote Control feature (requiring Claude Code v2.1.51+), activated via `/rc` or `claude --remote-control`, which generates a session URL accessible through `claude.ai/code` or the Claude mobile app. Limitations noted included single concurrent connections per session, session termination if the terminal process closes, roughly 10-minute timeout on network outages, and the QR code shortcut not functioning on Windows.

---

## User

I installed Claude Code in my VS Code. When click on Claude icon in right most corner, a powershell is coming up. It runs Claude and gives error no such command found. How do I use Claude Code from this powershell terminal?

---

## Assistant

> **Tool:** view

<details>
<summary>Tool output</summary>

```
[{'type': 'text', 'text': '     1\t---\n     2\tname: product-self-knowledge\n     3\tdescription: "Stop and consult this skill whenever your response would include specific facts about Anthropic\'s products. Covers: Claude Code (how to install, Node.js requirements, platform/OS support, MCP server integration, configuration), Claude API (function calling/tool use, batch processing, SDK usage, rate limits, pricing, models, streaming), and Claude.ai (Pro vs Team vs Enterprise plans, feature limit
```
</details>

> **Tool:** web_fetch

<details>
<summary>Tool output</summary>

```
[{'type': 'text', 'text': '{"error_type": "PERMISSIONS_ERROR", "error_message": "This URL cannot be fetched because it was not provided by the user nor did it appear in any search/fetch results"}', 'uuid': '909c93f5-8af9-480a-b6b6-d73689129a5d'}]
```
</details>

> **Tool:** web_fetch

<details>
<summary>Tool output</summary>

```
[{'type': 'text', 'text': '{"error_type": "PERMISSIONS_ERROR", "error_message": "This URL cannot be fetched because it was not provided by the user nor did it appear in any search/fetch results"}', 'uuid': 'd60df598-8e39-49a7-88c2-9c8fb8060f1b'}]
```
</details>

> **Tool:** web_search

<details>
<summary>Tool output</summary>

```
[{'type': 'knowledge', 'title': 'Advanced setup - Claude Code Docs', 'url': 'https://code.claude.com/docs/en/setup', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'claude.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=claude.com', 'site_name': 'Claude'}, 'is_missing': False, 'text': 'Do NOT use sudo npm install -g as this can lead to permission issues and security risks. If you encounter permission errors, see troubleshooting permission errors. Each release publi
```
</details>

The problem is that the VS Code extension for Claude Code expects the `claude` CLI to already be installed on your system — it just opens a terminal and runs it. Since it's not installed yet, you get the "command not found" error. Here's how to fix it:

## Step 1: Install Claude Code via PowerShell

The recommended native installer requires no Node.js or npm — just run this in PowerShell (no Administrator needed):

```powershell
irm https://claude.ai/install.ps1 | iex
```

The installer downloads the Claude Code binary and puts it in `%LOCALAPPDATA%\Programs\ClaudeCode`. The whole process takes 10–30 seconds.

## Step 2: Also install Git for Windows (required)

Claude Code on Windows requires Git for Windows — install it from git-scm.com, then run the installer command above. Claude Code uses Git Bash internally to run commands.

## Step 3: Restart PowerShell / VS Code

After installation, **close and reopen PowerShell** — PATH updates only after a terminal restart. Then type `claude --version` to verify it works.

If it still says "not found" after reopening, your PATH may not have updated yet. Run this in PowerShell to add it manually:

```powershell
$npmPath = npm config get prefix
$userPath = [Environment]::GetEnvironmentVariable("Path", "User")
[Environment]::SetEnvironmentVariable("Path", "$userPath;$npmPath", "User")
```

Then close all terminals and reopen.

## Step 4: Authenticate

On first launch, a browser window opens for OAuth login. Sign in with your Claude Pro/Max account. The token is stored locally in `~/.claude/` so you won't need to re-authenticate.

## Step 5: Back in VS Code

Once `claude` works in a standalone PowerShell window, click the Claude icon in VS Code again — it should now find the command and launch properly.

---

**One gotcha to watch for:** if you have Cursor or another editor installed alongside VS Code, it can intercept the `code` command that Claude Code uses internally. If file edits fail, check your PATH order in system environment variables and make sure VS Code appears before Cursor.

---

## User

Setup successfully.  How do I make sure all the prompts and responses from the Claude terminal are maintained/stored?

---

## Assistant

> **Tool:** web_search

<details>
<summary>Tool output</summary>

```
[{'type': 'knowledge', 'title': 'How Claude Code works - Claude Code Docs', 'url': 'https://code.claude.com/docs/en/how-claude-code-works', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'claude.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=claude.com', 'site_name': 'Claude'}, 'is_missing': False, 'text': 'Each Claude Code conversation is a session tied to your current directory. When you resume, you only see sessions from that directory. Claude sees your current
```
</details>

Good news — Claude Code automatically saves everything. Here's what you need to know:

## What's Stored Automatically

Claude Code saves your conversation locally as you work. Each message, tool use, and result is stored, which enables rewinding, resuming, and forking sessions. Before Claude makes code changes, it also snapshots the affected files so you can revert if needed.

All conversation logs live in `~/.claude/projects/`. Each project gets its own folder, and inside each project folder are individual conversation files as `.jsonl` files — one per session. On Windows, that path is `C:\Users\YourName\.claude\projects\`.

---

## Resuming Sessions (Most Important)

Use `claude --continue` (or `claude -c`) to resume your last session, or `claude --resume` (or `claude -r`) to open a picker to browse all recent sessions.

When you resume a session, new messages append to the existing conversation and your full conversation history is restored.

---

## Searching Across All Sessions

Every prompt you've ever sent is logged in `~/.claude/history.jsonl`. If you're trying to find something specific you typed two weeks ago but can't remember which session it was in, this is the file to search.

You can grep through it in PowerShell like:
```powershell
Select-String "your keyword" "$env:USERPROFILE\.claude\history.jsonl"
```

---

## Exporting Conversations as Readable Files

Claude Code doesn't have a built-in export button, but you can use the community tool **claude-conversation-extractor**:

```powershell
pip install claude-conversation-extractor
claude-extract --all          # export everything
claude-extract --recent 5     # last 5 sessions
claude-extract --format html  # pretty HTML output
```

It converts the JSONL files to clean Markdown with user messages prefixed with 👤 and Claude responses with 🤖, including metadata like session ID and timestamps.

---

## One Caveat to Know

Each Claude Code conversation is tied to your **current directory**. When you resume, you only see sessions from that directory. So make sure you `cd` into your project folder before running `claude --resume`, otherwise it won't show those sessions.

The bottom line: your conversations are being saved to disk in real-time automatically — you just need to use `claude --resume` to get back to them, rather than starting a fresh `claude` session each time.

---

## User

How can I access Claude code sessions that I have on my PC from my phone?

---

## Assistant

> **Tool:** web_search

<details>
<summary>Tool output</summary>

```
[{'type': 'knowledge', 'title': 'Continue local sessions from any device with Remote Control - Claude Code Docs', 'url': 'https://code.claude.com/docs/en/remote-control', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'claude.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=claude.com', 'site_name': 'Claude'}, 'is_missing': False, 'text': 'If you’re already in a Claude Code session and want to continue it remotely, use the /remote-control (or /rc) command: ... This 
```
</details>

There's a built-in feature made exactly for this — **Remote Control**, launched by Anthropic in February 2026. Here's everything you need to know:

## How It Works

Remote Control connects a second screen to a Claude Code session running on your machine. Your files, MCP server configurations, project credentials, and `.claude/` settings all stay on your machine. What travels through Anthropic's servers is limited to two things: the messages you type and the tool results Claude generates.

---

## Setup (3 steps)

**1. Update Claude Code first**

Remote Control requires Claude Code v2.1.51 or later. Check your version with `claude --version`.

```powershell
claude --version
```

If needed, update with the native installer: `irm https://claude.ai/install.ps1 | iex`

**2. Start a Remote Control session on your PC**

From an active Claude Code session, type:
```
/rc
```

Or start a new session with it enabled:
```powershell
claude --remote-control
```

This starts a Remote Control session that displays a session URL. You can press spacebar to show a QR code for quick access from your phone.

**3. Connect from your phone**

Open `claude.ai/code` in any browser or the Claude mobile app. Remote Control sessions appear with a computer icon and a green status dot. Tap it to connect to your local session.

Don't have the app yet? Run `/mobile` inside Claude Code to get a download QR code for iOS or Android.

---

## Enable It Automatically for Every Session

To enable Remote Control for every session automatically, run `/config` inside Claude Code and set "Enable Remote Control for all sessions" to true. That way you never need to remember to turn it on before leaving your desk.

---

## Key Limitations to Know

Remote Control is available on all plans. On Team and Enterprise, it is off by default until an admin enables it. API keys are not supported — you need a Pro, Max, Team, or Enterprise subscription.

A few other gotchas:
- Each Claude Code session supports a single remote connection at a time, and if the terminal process is closed or the `claude` command exits, the remote session ends and must be restarted manually.
- Extended network outages of roughly 10 minutes cause the session to time out. For truly unreliable connections, the community SSH + tmux stack handles intermittent connectivity more gracefully.
- The QR code shortcut does not currently work on Windows, so use the session list in the Claude app or `claude.ai/code` to connect instead.

---
