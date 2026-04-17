# Finding IMEI lists for Samsung devices

**Date:** 2026-03-04  
**Source:** Claude Web/App  
**ID:** `fbcd39ca-d93a-4437-93fd-e62c49122220`

**Summary:** **Conversation Overview**

The person asked two sequential technical questions about IMEI and TAC (Type Allocation Code) data for Samsung device models. First, they asked how to find a complete list of IMEIs for a given Samsung model, and Claude explained that IMEIs are unique per individual device rather than per model, making a complete list impossible to obtain publicly. Claude clarified that manufacturers like Samsung hold proprietary IMEI range data, and directed the person toward the practical alternative of using TAC codes (the first 8 digits of an IMEI) to identify device models.

The person then refined their question to ask specifically about finding a complete list of TAC codes for a given Samsung model. Claude explained that multiple TAC codes exist per model due to regional, carrier, storage, and manufacturing batch variations. Claude outlined available resources ranging from the authoritative paid GSMA IMEI Database (imeidb.gsma.com) to free community resources including imei.info, tacdb.osmocom.org, and GitHub repositories containing downloadable TAC data in CSV/JSON formats. Claude noted that for programmatic use cases, filtering open-source TAC dumps from GitHub or Osmocom by Samsung model name is the fastest free approach, while commercial or regulatory needs warrant the GSMA licensed database. Claude asked about the person's specific use case at the end of both responses to better tailor guidance, but the person did not share their underlying goal.

---

## User

How do I find compute complete list of IMEIs of any given Samsung device model.

---

## Assistant

There's no way to obtain a complete list of all IMEI numbers for a given Samsung device model, and here's why:

**IMEI numbers are unique per individual device**, not per model. Each physical phone manufactured gets its own unique 15-digit IMEI. A popular model like the Galaxy S24 might have tens of millions of unique IMEIs — one for each unit produced. These are not published or aggregated into any public list.

**Who holds this data?**

Samsung (and other manufacturers) maintain internal records of IMEI ranges assigned during manufacturing, but this information is proprietary and not shared publicly. Mobile carriers also track IMEIs of devices on their networks, but again, this is private data.

**What you *can* do:**

- **Find the IMEI of a specific device you own:** Dial `*#06#` on the phone, or check Settings → About Phone → IMEI.
- **Identify the model from an IMEI:** Use the first 8 digits (the TAC — Type Allocation Code) to look up the device model via the GSMA TAC database or sites like imei.info.
- **Look up the TAC range for a model:** The TAC prefix is shared across all units of a given model/variant. You can find known TAC codes for Samsung models through GSMA's IMEI database or third-party lookup tools. This tells you which IMEI *prefix* belongs to which model, but not every individual IMEI under that prefix.

If your goal is to **verify whether a specific IMEI belongs to a certain Samsung model**, the TAC lookup approach is the practical solution. Could you share more about what you're ultimately trying to accomplish? That might help me point you in a more useful direction.

---

## User

How can I find complete list of TAC codes given a Samsung device model?

---

## Assistant

Finding a complete list of TAC codes for a specific Samsung model can be done through a few routes, depending on your needs and budget:

**Official / Authoritative Source**

The GSMA maintains the global IMEI/TAC database, since they are the organization that allocates TAC codes to manufacturers. Access is available through their IMEI Database service at imeidb.gsma.com, but it's a paid, licensed product primarily intended for carriers, regulators, and device management companies. If you need a fully authoritative and complete list, this is the definitive source.

**Free / Community Resources**

Several free tools and databases have aggregated TAC data over time, though completeness isn't guaranteed:

- **imei.info** — You can look up individual TACs or search by brand/model. It won't necessarily give you every TAC for a model, but it's a good starting point.
- **tacdb.osmocom.org** — An open-source TAC database maintained by the Osmocom (Open Source Mobile Communications) community. You can browse or search by manufacturer.
- **GitHub repositories** — Several community-maintained TAC lists exist on GitHub. Search for "TAC database" or "IMEI TAC list" and you'll find CSV/JSON dumps that can be filtered by manufacturer and model.

**Why there are multiple TACs per model**

A single Samsung model (e.g., Galaxy S24) can have many different TAC codes because TACs vary by region, carrier variant, storage configuration, modem variant, and manufacturing batch. So "complete" can be a moving target.

**Practical approach**

If you're building something programmatic, grabbing an open-source TAC dump from GitHub or Osmocom and filtering by Samsung model name is probably the fastest free path. If accuracy and completeness are critical (e.g., for a commercial product or regulatory use), the GSMA's licensed database is the way to go.

What's your use case? That might help me narrow down the best option for you.

---
