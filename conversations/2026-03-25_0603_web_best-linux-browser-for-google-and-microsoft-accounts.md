# Best Linux browser for Google and Microsoft accounts

**Date:** 2026-03-25  
**Source:** Claude Web/App  
**ID:** `235a1fa1-aff0-4bd9-9502-52b50749b237`

**Summary:** **Conversation Overview**

The person is a Fedora Linux user troubleshooting two separate audio issues on their system. The conversation covered browser recommendations as a brief starting topic, then shifted primarily to Linux audio configuration using PipeWire and WirePlumber.

For the browser question, the person asked about the best browser for managing both Google and Microsoft accounts on Linux, and Claude recommended a two-browser setup (Chrome/Chromium for Google, Edge for Microsoft) while also suggesting single-browser alternatives like Vivaldi (with Workspaces), Brave (with profiles), and Firefox with Multi-Account Containers extension.

The main technical work involved two audio problems on Fedora. First, the person's audio output menu was flooded with dozens of other people's AirPlay devices (MacBooks, Apple TVs) from a shared local network. This was resolved by disabling the `monitor.raop` module in WirePlumber via a config file at `~/.config/wireplumber/wireplumber.conf.d/51-disable-raop.conf`. Second, the person could not get audio output from 3.5mm speakers connected via a USB-C hub. Diagnosis revealed the system was running the `pro-audio` profile on the `alsa_card.pci-0000_00_1f.3-platform-skl_hda_dsp_generic` card (a Raptor Lake-P/U/H cAVS device), which bypasses jack detection. Switching to `HiFi (HDMI1, HDMI2, HDMI3, Mic1, Mic2, Speaker)` profile exposed the Speaker sink (node ID 330), which became the active default. The Headphones port showed `not available` because the USB-C hub does not assert the jack detection pin, preventing Linux from detecting insertion. The recommended fix involved setting `api.acp.auto-port = false` in WirePlumber rules and manually forcing the port via `pactl set-sink-port`. The conversation ended with the Speaker sink active and further troubleshooting steps provided including `alsamixer` channel mute checks.

---

## User

best browser for google accounts and microsoft accounts linux reddit\

---

## Assistant

> **Tool:** web_search

<details>
<summary>Tool output</summary>

```
[{'type': 'knowledge', 'title': 'Can I get some browser suggestions? | Linux.org', 'url': 'https://www.linux.org/threads/can-i-get-some-browser-suggestions.56012/', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'linux.org', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=linux.org', 'site_name': 'Linux.org'}, 'is_missing': False, 'text': 'Microsoft Edge or Google-Chrome On the more serious note, Vivaldi. ... If you want something a bit odd but with a wealth of history, 
```
</details>

---

## User

best browser for google accounts and microsoft accounts linux reddi

---

## Assistant

---

## User

best browser for google accounts and microsoft accounts linux

---

## Assistant

Here's the practical consensus from the Linux community:

## For Google Accounts
**Google Chrome** (or **Chromium**) is the obvious best fit — deepest integration with Google Workspace, Drive, Meet, and seamless multi-account switching. Chrome is available as a `.deb`/`.rpm` for most distros.

## For Microsoft Accounts
**Microsoft Edge** is surprisingly the best choice on Linux. It's Chromium-based, has a native Linux build, and handles Microsoft 365, Teams, SharePoint, and Outlook web far better than any other browser. Edge has been rebuilt with Chromium at its heart and has official Linux versions available.

## The Most Common Real-World Setup (from Linux forums)

The popular approach is **two-browser separation**:

- **Edge** for Microsoft accounts / M365 / Outlook
- **Chrome or Chromium** for Google accounts
- **Firefox** as a general-purpose daily driver with uBlock Origin

A common pattern is Firefox for general use, with Chrome and Edge kept specifically for sites or services that work better in those browsers.

Some users deliberately split accounts across browsers — keeping Microsoft accounts in one and Google accounts in another — to avoid cross-contamination of cookies and tracking.

## Quick Recommendation

| Need | Browser |
|---|---|
| Google Workspace / Drive / Gmail | Chrome or Chromium |
| Microsoft 365 / Outlook / Teams | Microsoft Edge |
| Everything else + privacy | Firefox + uBlock Origin |

**Bottom line:** Install Edge for Microsoft and Chrome/Chromium for Google — both have solid native Linux support and are the most compatible with their respective ecosystems.

---

## User

any other browser out there that combines both?

---

## Assistant

> **Tool:** web_search

<details>
<summary>Tool output</summary>

```
[{'type': 'knowledge', 'title': 'The Best Browsers for Multiple Profiles - Shift Blog | Browser Tips, App Integrations, and Productivity | Shift Browser', 'url': 'https://shift.com/guides/multiple-accounts/the-best-browsers-for-multiple-profiles/', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'shift.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=shift.com', 'site_name': 'Shift'}, 'is_missing': False, 'text': 'Microsoft Edge has a feature called &quot;Profiles&qu
```
</details>

Yes, a few good options exist. The key insight is that **any Chromium-based browser with solid profile support** can handle both ecosystems equally well, since neither Google nor Microsoft services require their "own" browser — they just need Chromium compatibility.

---

## Best Single-Browser Options

### 1. **Vivaldi** ⭐ (Top Pick)
The most feature-rich option for power users. Vivaldi has a "Workspaces" feature that lets you organize different accounts and contexts into separate workspaces, similar to having different desktops. It's Chromium-based so M365 and Google Workspace both work flawlessly on Linux.

### 2. **Brave**
Brave supports multiple profiles, each with its own set of bookmarks, extensions, and settings, along with built-in ad/tracker blocking. Good privacy defaults and works well with both Google and Microsoft services.

### 3. **Firefox with Multi-Account Containers**
Firefox has an extension called **Multi-Account Containers** (by Mozilla) that isolates different accounts into color-coded tabs — no separate profiles needed. You can have your Google stuff in one container and Microsoft in another, all in the same window. Works great on Linux.

### 4. **Chrome/Chromium with Profiles** (simplest)
A common misconception is that Chrome profiles require a unique Google account — you can skip that prompt and create profiles freely. So you can have a "Google" profile and a "Microsoft" profile running simultaneously in separate windows, no second Google account needed.

---

## Summary

| Browser | Linux | Multi-account | Google | Microsoft | Notes |
|---|---|---|---|---|---|
| **Vivaldi** | ✅ | Workspaces | ✅ | ✅ | Most powerful |
| **Brave** | ✅ | Profiles | ✅ | ✅ | Best privacy |
| **Firefox + Containers** | ✅ | Containers | ✅ | ✅ | Single window |
| **Chrome** | ✅ | Profiles | ✅ | ✅ | Simplest |

**Vivaldi** is probably the most compelling if you want everything in one place — it's essentially Chrome-level compatibility with much better multi-account and workspace organization built in natively.

---

## User

my fedora installation for some reason shows me a shit ton of devices i can output audio to like other peopels devices, I dont want these options, how to disable

---

## Assistant

This is almost certainly **PipeWire + WirePlumber** discovering audio devices on your local network via **Avahi (mDNS)**. It picks up things like other people's PulseAudio/PipeWire streams, AirPlay devices, Bluetooth of neighbors, etc.

## Fix: Disable Network Audio Discovery in WirePlumber

**Step 1** — Check if the raop/network modules are the culprit:
```bash
wpctl status
```
Look for anything labeled "raop", "network", or "tunnel" in the sinks/sources.

**Step 2** — Disable network device discovery by creating a WirePlumber config override:
```bash
mkdir -p ~/.config/wireplumber/wireplumber.conf.d/
```

```bash
nano ~/.config/wireplumber/wireplumber.conf.d/51-disable-network-audio.conf
```

Paste this:
```
wireplumber.profiles = {
  main = {
    monitor.libcamera = disabled
  }
}

monitor.alsa.rules = [
  {
    matches = [ { node.name = "~raop*" } ]
    actions = { update-props = { node.disabled = true } }
  }
]
```

**Step 3** — Also disable Avahi-based audio discovery more broadly:
```bash
nano ~/.config/wireplumber/wireplumber.conf.d/52-no-zeroconf.conf
```
```
wireplumber.profiles = {
  main = {
    monitor.raop = disabled
    monitor.network = disabled
  }
}
```

**Step 4** — Restart WirePlumber:
```bash
systemctl --user restart wireplumber
```

---

## Alternative: Disable Avahi Entirely (if you don't need network discovery at all)

If you don't use any network printers, file sharing discovery, etc:
```bash
sudo systemctl disable --now avahi-daemon
```
This stops mDNS network discovery system-wide, which is often the root cause of all those phantom devices appearing.

---

The Avahi disable is the nuclear but simple option. The WirePlumber config is cleaner if you want to keep Avahi for other things like network printers.

---

## User

```

```

> **Attachment:** 

> **File:** 

---

## Assistant

Yep, confirmed — those are all **AirPlay (RAOP) devices** being discovered on your local network. You're on a shared network (university/office?) with dozens of people's MacBooks and Apple devices showing up. The fix is straightforward:

## Disable the RAOP/AirPlay Monitor in WirePlumber

```bash
mkdir -p ~/.config/wireplumber/wireplumber.conf.d/
```

```bash
nano ~/.config/wireplumber/wireplumber.conf.d/51-disable-raop.conf
```

Paste this:
```
wireplumber.profiles = {
  main = {
    monitor.raop = disabled
  }
}
```

Then restart WirePlumber:
```bash
systemctl --user restart wireplumber
```

That's it. All those MacBooks, Apple TVs, and "Don't bother me please" devices will disappear immediately.

---

**Why this works:** WirePlumber has a `monitor.raop` module that scans your local network for AirPlay-capable devices via mDNS and adds them as audio output sinks. On a shared/campus network this goes wild. Disabling that one profile module surgically removes all of them without touching anything else.

Also worth noting — I can see **Advait's MacBook Pro** in that list 😄 — so it's definitely your local network.

---

## User

ok, now fedora detects my audio devices like my monitor speakers and usbc eearbuds plugged into dock but I cant output from speakers connected to 3.5 mm jack from the usbc hub

---

## Assistant

Run these to diagnose first:

```bash
wpctl status | grep -i usb
```

```bash
aplay -l
```

This will tell us if the hub's 3.5mm jack is even being detected as a device. What's the output?

Also, the default sink in your `wpctl status` was:
```
alsa_output.usb-Samsung_Samsung_USB_C_Earphones_20160406.1-00.analog-stereo
```

So the Samsung earbuds are detected fine — the question is whether the hub's audio chipset shows up separately. Most USB-C hubs expose their 3.5mm jack as a separate USB audio device, but some cheaper hubs don't advertise it properly.

A few quick things to also check:

**1. See all audio cards:**
```bash
cat /proc/asound/cards
```

**2. Check if it shows up but with wrong profile:**
```bash
wpctl inspect <device-id>
```

**3. Try switching the audio profile on the hub device via PipeWire:**
```bash
pactl list cards | grep -A 20 "usb"
```

Paste the output and we can pinpoint whether it's a detection issue, a profile issue, or needs an ALSA UCM config workaround.

---

## User

 aplay -l **** List of PLAYBACK Hardware Devices **** card 1: sofhdadsp [sof-hda-dsp], device 0: HDA Analog (*) []  Subdevices: 1/1  Subdevice #0: subdevice #0 card 1: sofhdadsp [sof-hda-dsp], device 3: HDMI1 (*) []  Subdevices: 1/1  Subdevice #0: subdevice #0 card 1: sofhdadsp [sof-hda-dsp], device 4: HDMI2 (*) []  Subdevices: 1/1  Subdevice #0: subdevice #0 card 1: sofhdadsp [sof-hda-dsp], device 5: HDMI3 (*) []  Subdevices: 1/1  Subdevice #0: subdevice #0 card 1: sofhdadsp [sof-hda-dsp], device 31: HDA Analog Deep Buffer (*) []  Subdevices: 1/1  Subdevice #0: subdevice #0

---

## Assistant

The hub's 3.5mm jack is **not showing up as a separate USB audio device** — it's routing through your laptop's internal `sof-hda-dsp` (HDA Analog, device 0), which is the same path as your built-in headphone jack. This is common with USB-C hubs that don't have their own audio chipset.

The problem is likely **jack detection** — PipeWire doesn't know something is plugged in. Run:

```bash
pactl list cards | grep -A 40 "sof-hda-dsp"
```

This will show all the available profiles for that card. Paste the output — specifically looking for whether there's an "active profile" and what profiles are listed (things like `output:analog-stereo`, `output:analog-stereo+input:analog-stereo`, `HiFi`, etc.).

Also try this to manually force-switch to the analog output profile:

```bash
pactl set-card-profile alsa_card.platform-sof-hda-dsp output:analog-stereo
```

Then try playing something and see if sound comes out of the 3.5mm speakers.

If that doesn't work, also run:
```bash
dmesg | grep -i "jack\|audio\|hdmi" | tail -20
```

The `sof-hda-dsp` driver on Raptor Lake laptops sometimes has quirks with jack detection on Fedora — knowing the active profile will tell us exactly what's going wrong.

---

## User

> **Attachment:** 

> **File:** 

---

## Assistant

Found it. Your active profile is `pro-audio` which bypasses all the jack detection logic. You need to switch to the HiFi profile that includes Headphones:

```bash
pactl set-card-profile alsa_card.pci-0000_00_1f.3-platform-skl_hda_dsp_generic "HiFi (HDMI1, HDMI2, HDMI3, Headphones, Mic1, Mic2)"
```

Then try playing audio through the 3.5mm speakers.

---

To make it **permanent**, create a WirePlumber rule:

```bash
nano ~/.config/wireplumber/wireplumber.conf.d/50-fix-profile.conf
```

```
monitor.alsa.rules = [
  {
    matches = [ { device.name = "alsa_card.pci-0000_00_1f.3-platform-skl_hda_dsp_generic" } ]
    actions = {
      update-props = {
        device.profile = "HiFi (HDMI1, HDMI2, HDMI3, Headphones, Mic1, Mic2)"
        api.acp.auto-profile = false
      }
    }
  }
]
```

```bash
systemctl --user restart wireplumber
```

---

**Why this happened:** `pro-audio` mode exposes raw ALSA devices directly (which is why you had those "Pro 1", "Pro 3", "Pro 5" sinks in your earlier `wpctl status`). It's meant for DAW/studio use and skips all the intelligent jack switching. The HiFi profile is what normal desktop use should be on.

---

## User

which one to output from

> **File:** 1774420528290_image.png

---

## Assistant

Those are all still the **pro-audio profile** sinks — the profile switch didn't take effect yet. You shouldn't be seeing these at all after switching to HiFi.

Run this to confirm what profile is actually active right now:

```bash
pactl list cards | grep "Active Profile"
```

If it still says `pro-audio`, force the switch again:

```bash
pactl set-card-profile alsa_card.pci-0000_00_1f.3-platform-skl_hda_dsp_generic "HiFi (HDMI1, HDMI2, HDMI3, Headphones, Mic1, Mic2)"
```

Then restart WirePlumber to clear out the stale sinks:

```bash
systemctl --user restart wireplumber
```

After that, your audio settings should show clean named outputs like **"Headphones"**, **"Speaker"**, and **"HDMI1"** instead of these "Pro" numbered ones. The 3.5mm jack will appear as "Headphones" when something is plugged in.

---

## User

only have these options

> **File:** 1774420616277_image.png

---

## Assistant

The Headphones port isn't showing because **jack detection isn't triggering** — the audio controller doesn't see anything plugged into the 3.5mm port (common issue with USB-C hubs since they don't always signal insertion properly).

Try the **other HiFi profile** that includes Speaker instead:

```bash
pactl set-card-profile alsa_card.pci-0000_00_1f.3-platform-skl_hda_dsp_generic "HiFi (HDMI1, HDMI2, HDMI3, Mic1, Mic2, Speaker)"
```

```bash
systemctl --user restart wireplumber
```

This profile exposes the internal speaker + the analog jack as a shared output. Your 3.5mm speakers should appear.

---

Also check what the jack ports report right now:

```bash
pactl list cards | grep -A 5 "\[Out\] Speaker\|Headphone"
```

This will show whether the ports say `not available`, `available`, or `availability unknown`. If the headphones port says `not available` even when plugged in, the hub isn't signaling insertion to the HDA controller — in that case the Speaker profile is your best bet since its availability is `unknown` (meaning it always shows up regardless of jack detection).

---

## User

 pactl list cards | grep -A 5 "\[Out\] Speaker\|Headphone"                HiFi (HDMI1, HDMI2, HDMI3, Headphones, Mic1, Mic2): Play HiFi quality Music (HDMI1, HDMI2, HDMI3, Headphones, Mic1, Mic2) (sinks: 4, sources: 2, priority: 10300, available: yes)                HiFi (HDMI1, HDMI2, HDMI3, Mic1, Mic2, Speaker): Play HiFi quality Music (HDMI1, HDMI2, HDMI3, Mic1, Mic2, Speaker) (sinks: 4, sources: 2, priority: 10200, available: yes)                pro-audio: Pro Audio (sinks: 5, sources: 3, priority: 1, available: yes)        Active Profile: HiFi (HDMI1, HDMI2, HDMI3, Mic1, Mic2, Speaker)        Ports:                [Out] HDMI3: HDMI / DisplayPort 3 Output (type: HDMI, priority: 700, latency offset: 0 usec, availability group: HDMI/DP,pcm=5, not available) --                        Part of profile(s): HiFi (HDMI1, HDMI2, HDMI3, Mic1, Mic2, Speaker), HiFi (HDMI1, HDMI2, HDMI3, Headphones, Mic1, Mic2)                [Out] HDMI2: HDMI / DisplayPort 2 Output (type: HDMI, priority: 600, latency offset: 0 usec, availability group: HDMI/DP,pcm=4, not available)                        Properties:                                port.type = "hdmi"                                port.availability-group = "HDMI/DP,pcm=4"                                device.icon_name = "video-display" --                        Part of profile(s): HiFi (HDMI1, HDMI2, HDMI3, Mic1, Mic2, Speaker), HiFi (HDMI1, HDMI2, HDMI3, Headphones, Mic1, Mic2)                [Out] HDMI1: HDMI / DisplayPort 1 Output (type: HDMI, priority: 500, latency offset: 0 usec, availability group: HDMI/DP,pcm=3, available)                        Properties:                                port.type = "hdmi"                                port.availability-group = "HDMI/DP,pcm=3"                                device.icon_name = "video-display" --                        Part of profile(s): HiFi (HDMI1, HDMI2, HDMI3, Mic1, Mic2, Speaker), HiFi (HDMI1, HDMI2, HDMI3, Headphones, Mic1, Mic2)                [Out] Speaker: Speaker (type: Speaker, priority: 100, latency offset: 0 usec, availability unknown)                        Properties:                                port.type = "speaker"                                device.icon_name = "audio-speakers"                                card.profile.port = "3"                        Part of profile(s): HiFi (HDMI1, HDMI2, HDMI3, Mic1, Mic2, Speaker) --                        Part of profile(s): HiFi (HDMI1, HDMI2, HDMI3, Mic1, Mic2, Speaker), HiFi (HDMI1, HDMI2, HDMI3, Headphones, Mic1, Mic2)                [In] Mic1: Digital Microphone (type: Mic, priority: 100, latency offset: 0 usec, availability unknown)                        Properties:                                port.type = "mic"                                device.icon_name = "audio-input-microphone"                                card.profile.port = "5"                        Part of profile(s): HiFi (HDMI1, HDMI2, HDMI3, Mic1, Mic2, Speaker), HiFi (HDMI1, HDMI2, HDMI3, Headphones, Mic1, Mic2)                [Out] Headphones: Headphones (type: Headphones, priority: 200, latency offset: 0 usec, availability group: Headphone, not available)                        Properties:                                port.type = "headphones"                                port.availability-group = "Headphone"                                device.icon_name = "audio-headphones"                                card.profile.port = "6"                        Part of profile(s): HiFi (HDMI1, HDMI2, HDMI3, Headphones, Mic1, Mic2)

---

## Assistant

The situation is clear:
- **Speaker**: `availability unknown` → should always show, but isn't appearing in KDE
- **Headphones**: `not available` → hub isn't signaling jack insertion, so it won't show

The Speaker port exists but KDE is auto-routing everything to HDMI1 (the only "available" port). Force-set the port directly:

```bash
# First find the sink ID
wpctl status | grep -i "cAVS"
```

Then force the Speaker port:
```bash
pactl set-sink-port alsa_output.pci-0000_00_1f.3-platform-skl_hda_dsp_generic.HiFi__HDMI1__HDMI2__HDMI3__Mic1__Mic2__Speaker__sink analog-output-speaker
```

And to make Headphones work despite the hub not signaling, force it as always available:

```bash
nano ~/.config/wireplumber/wireplumber.conf.d/53-fix-headphone-jack.conf
```

```
monitor.alsa.rules = [
  {
    matches = [ { node.name = "~alsa_output.*skl_hda_dsp*" } ]
    actions = {
      update-props = {
        api.acp.auto-port = false
      }
    }
  }
]
```

```bash
systemctl --user restart wireplumber
```

Then manually set the port:
```bash
pactl set-sink-port alsa_output.pci-0000_00_1f.3-platform-skl_hda_dsp_generic.HiFi__HDMI1__HDMI2__HDMI3__Headphones__Mic1__Mic2__sink analog-output-headphones
```

The root issue is your USB-C hub doesn't assert the jack detection pin, so Linux never gets the "something is plugged in" signal. The `api.acp.auto-port = false` stops WirePlumber from auto-switching ports based on detection, letting you pick manually.

---

## User

 wpctl status | grep -i "cAVS" │     111. Raptor Lake-P/U/H cAVS              [alsa] │     115. Raptor Lake-P/U/H cAVS HDMI / DisplayPort 3 Output [vol: 1.00] │     291. Raptor Lake-P/U/H cAVS HDMI / DisplayPort 2 Output [vol: 1.00] │     294. Raptor Lake-P/U/H cAVS HDMI / DisplayPort 1 Output [vol: 0.35] │  *  330. Raptor Lake-P/U/H cAVS Speaker      [vol: 0.83] │  *  257. Raptor Lake-P/U/H cAVS Digital Microphone [vol: 1.00] │     427. Raptor Lake-P/U/H cAVS Stereo Microphone [vol: 1.00]

---

## Assistant

The **Speaker sink (330) is already active and default** (notice the `*`). Try playing audio right now — does sound come out of the 3.5mm speakers?

If not, the issue is that the hub is physically routing the 3.5mm jack differently. Try switching the active port on that sink explicitly:

```bash
pactl set-sink-port 330 analog-output-speaker
```

Also try setting it as the default output explicitly:
```bash
wpctl set-default 330
```

Then play something and test. If you still get no sound from the 3.5mm, run:
```bash
alsamixer
```

Hit `F6` → select `sof-hda-dsp`, then check if the **Speaker** or **Headphone** channels are muted (press `M` to unmute, arrow keys to raise volume). Sometimes ALSA-level mutes survive PipeWire's volume control.

---
