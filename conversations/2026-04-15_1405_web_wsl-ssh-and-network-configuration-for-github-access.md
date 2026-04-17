# WSL SSH and network configuration for GitHub access

**Date:** 2026-04-15  
**Source:** Claude Web/App  
**ID:** `b75f279f-4fe4-49ea-b9aa-b6b749c03ea0`

---

## User

I have installed WSL installed on my work laptop. To be able to access girhub via SSH, apparently I have to install a certificate, and IT has to whitelist IP address and MAC address. When I looked at WSL IP address and MAC addresses, they seem to be completely local. How do I the info IT is requesting?

---

## Assistant

You're right that WSL's IP and MAC addresses are virtual — they belong to a virtual network adapter (usually `eth0` inside WSL, backed by a Hyper-V virtual switch on Windows). IT won't be able to whitelist those because they're internal and can change.

What IT actually needs is your **Windows host machine's** network info, not WSL's. Here's how to get it:

**On Windows (not inside WSL), open PowerShell or CMD and run:**

```powershell
ipconfig /all
```

Look for your **physical adapter** — typically labeled something like:
- `Ethernet adapter Ethernet` (wired)
- `Wireless LAN adapter Wi-Fi` (wireless)

From that section, grab:
- **IPv4 Address** → this is the IP IT needs
- **Physical Address** (e.g., `A1-B2-C3-D4-E5-F6`) → this is the MAC address

**Why this works:** WSL routes all outbound traffic through the Windows host's physical network adapter. So when WSL connects to GitHub (or anything external), the traffic appears to originate from the Windows machine's IP and MAC — not from WSL's virtual interface.

---

**One caveat — corporate laptops with dynamic IPs:**

If your work machine gets its IP via DHCP (most corporate environments), the IP can change. In that case, IT may prefer to whitelist by **hostname** or by **MAC address alone** (since MAC is stable). You can get your Windows hostname with:

```powershell
hostname
```

Share that with IT as well, and ask if they can whitelist by MAC + hostname rather than IP, which is more reliable long-term.

---

**For the certificate piece:** That's almost certainly a corporate SSL inspection certificate that needs to be trusted by your Git/SSH client inside WSL. Once IT whitelists your machine, they'll likely give you a `.crt` file to install. If you hit that step and need help installing it in WSL's trust store, just let me know.

---
