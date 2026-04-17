# Remote access to home trading PC from work laptop

**Date:** 2026-03-23  
**Source:** Claude Web/App  
**ID:** `d74ae97d-5b5c-478a-bfb2-52500e37f51e`

**Summary:** **Conversation Overview**

The person uses a home mini PC for stock trading, running TradingView Premium with multiple Chrome tabs displaying ticker charts, alongside Discord and WhatsApp desktop apps for monitoring messages in trading groups. They work from a separate office location using a work laptop and want to remotely access their home mini PC's screen from work to check charts and Discord, with the key constraint that their workplace has firewalls in place.

Claude provided a tiered set of remote access solutions ordered by likelihood of working through corporate firewalls. The primary recommendation was Chrome Remote Desktop, favored because it tunnels over standard HTTPS through Google's servers on port 443, which corporate firewalls rarely block, and requires no software installation on the work laptop beyond a Chrome browser tab. The setup involves installing the companion app on the home mini PC via remotedesktop.google.com/access and connecting with the same Google account from the work laptop. Secondary options included Tailscale (a mesh VPN with WireGuard and HTTPS relay fallback via DERP servers, used in combination with Windows RDP) and Parsec (best visual quality but more likely to be blocked). Claude also noted that installing software on a work laptop may conflict with corporate IT policy and advised checking before doing so.

Practical configuration advice was provided for the home mini PC regardless of tool chosen: disabling sleep and hibernate entirely, preventing the display from turning off, using a dummy HDMI plug if no monitor is connected, enabling auto-login, and setting Chrome, Discord, and WhatsApp to launch on startup. A fallback suggestion was offered — accessing TradingView directly in a browser on the work laptop using the existing Premium account, since chart layouts sync via the account, reducing reliance on full remote access.

---

## User

I have a mini PC at home which I use for trading. I have tradingview premium subscription. I open multiple ticker charts in multiple tabs in Chrome and monitor charts occasionally. I also run discord and Whatsapp apps on my Mini PC to track all the messages in various trading groups I'm part of.

I have a work laptop that I work from from my office location. I want to leave my personal mini PC at home running, at access the screen remotely from my work laptop so that I can check stock charts in chrome, and also access discord. Help me achieve this goal. Note that my work has firewalls in place.

---

## Assistant

This is a common setup. The main challenge is getting through your work firewall. Here's a practical approach, ordered by likelihood of working behind corporate firewalls.

## Option 1: Chrome Remote Desktop (Recommended — Start Here)

This is your best bet because it tunnels through Google's servers over standard HTTPS (port 443), which almost no corporate firewall blocks since it looks like normal Google traffic.

**On your home mini PC:**
1. Open Chrome, go to `remotedesktop.google.com/access`
2. Sign in with a personal Google account
3. Click "Set up remote access" and install the companion app
4. Give the machine a name and set a PIN
5. Make sure the PC is set to never sleep (Power Settings → set sleep to "Never" on both screen and PC)

**From your work laptop:**
1. Open Chrome, go to `remotedesktop.google.com/access`
2. Sign in with the same Google account
3. Click your home PC, enter your PIN — you're in

**Why this works through firewalls:** It's just HTTPS traffic to Google domains. IT departments almost never block `*.google.com`. No special ports, no VPN software to install on your work machine.

**Downsides:** Moderate latency, image quality is decent but not amazing. For monitoring charts and reading Discord messages, it's perfectly fine.

---

## Option 2: Tailscale (If You Want Something More Robust)

Tailscale creates a private mesh network between your devices. It uses WireGuard under the hood and has an HTTPS relay fallback (called DERP) for restrictive firewalls.

**Setup:**
1. Install Tailscale on both your home mini PC and work laptop (`tailscale.com`)
2. Sign in with the same account on both
3. On your home PC, enable Windows Remote Desktop (Settings → System → Remote Desktop → On)
4. From your work laptop, connect via RDP to your home PC's Tailscale IP (shown in the Tailscale app, something like `100.x.y.z`)

**Why it might work:** DERP relays fall back to port 443. But some aggressive corporate firewalls do deep packet inspection and may block it.

**Risk:** Your IT department might not allow installing Tailscale on your work laptop, or their endpoint management might flag it.

---

## Option 3: Parsec (Best Visual Quality)

Parsec is designed for low-latency remote access and gives the smoothest experience for visual content like charts. It also uses HTTPS relay fallback. Setup is similar — install on both machines, sign in, connect. However, some corporate firewalls specifically block Parsec's relay domains.

---

## Practical Tips Regardless of Tool

**On your home mini PC, make sure to:**
- Disable sleep and hibernate entirely
- Set the display to never turn off (or use a dummy HDMI plug if you don't have a monitor connected — remote desktop tools sometimes need an active display)
- Enable auto-login so it recovers after power outages or Windows updates
- Set Chrome, Discord, and WhatsApp to launch on startup

**On your work laptop:**
- Try Chrome Remote Desktop first since it requires zero software installation — it's just a browser tab
- Avoid installing VPN or remote-access software on a work laptop without checking your company's IT policy, as it could flag endpoint security tools

**If Chrome Remote Desktop is blocked** (unlikely but possible), a fallback is to use your personal phone as a hotspot briefly to check charts, or access TradingView directly in a browser on your work laptop (it syncs layouts via your TV account) and keep Discord open in a browser tab — reducing the need for full remote access.

Want me to walk through the detailed setup for any of these options?

---
