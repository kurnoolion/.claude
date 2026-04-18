# WHat is your cwd?

**Date:** 2026-04-17  
**Session:** `cee147ed-85db-4f0c-87b8-d7e831dc465b`

---

## User

WHat is your cwd?

## Assistant

My current working directory is `/home/mohan/work/req-agent`.

---

## User

It should be changed to /home/mohan/work/req-agent

## Assistant

> **Tool:** Run: `cd /home/mohan/work/req-agent && pwd`

---

## Assistant

Done — my working directory is now `/home/mohan/work/req-agent`.

---

## User

I started claude from /home/mohan/work/req-agent. Why did it change to /home/mohan/work/req-agent?

## Assistant

This is likely because `/home/mohan/work/req-agent` is a symlink that resolves to `/home/mohan/work/req-agent`. Claude Code probably resolved the symlink to the canonical path. Let me verify.

---

## Assistant

> **Tool:** Run: `ls -la /home/mohan/work/req-agent && echo "---" && readlink -f /home/mohan/work/req-agent`

---

## Assistant

That confirms it. `readlink -f` shows that `/home/mohan/work/req-agent` resolves to `/home/mohan/work/req-agent` — it's on your Windows D: drive mounted via WSL2. Claude Code resolves symlinks to the canonical path, which is why it set the primary working directory to `/home/mohan/work/req-agent`.

Both paths point to the same directory, so functionally there's no difference. I'll continue using `/home/mohan/work/req-agent` as you prefer.

---

## User

How do I make sure claude doesn't resolve symlinks to canonical names?

## Assistant

> **Tool:** Spawn agent: Symlink resolution in Claude Code

---

## Assistant

There's **no built-in setting** in Claude Code to disable symlink resolution — it always resolves to the canonical path.

**Workarounds:**

1. **Use a bind mount instead of a symlink** — bind mounts don't get resolved:
   ```bash
   sudo mount --bind /home/mohan/work/req-agent /home/mohan/work/req-agent
   ```
   (Add to `/etc/fstab` to persist across reboots.)

2. **Launch from the canonical path** — just `cd /home/mohan/work/req-agent` before starting `claude`.

3. **File a feature request** — run `/feedback` in Claude Code to request a `--no-resolve-symlinks` flag or similar option.

The symlink resolution is cosmetic — both paths access the same files — but if the shorter path matters to you, the bind mount approach is the cleanest fix.

---

## User

The reason I'm insisting on /home/mohan path is that I'm using thie path across WSL and Linux PCs with /home/mohan/.claude sycned through github. So, I will go with bind mount option. Give me what line I need to add in /etc/fstab

## Assistant

Add this line to `/etc/fstab`:

```
/home/mohan/work/req-agent /home/mohan/work/req-agent none bind 0 0
```

After adding it, apply without rebooting:

```bash
sudo mount -a
```

---
