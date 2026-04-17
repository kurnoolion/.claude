# GSMA TAC/IMEI database columns

**Date:** 2026-03-30  
**Source:** Claude Web/App  
**ID:** `2129222d-fc13-4a7f-bf3c-13f4ffcd194f`

**Summary:** **Conversation Overview**

The conversation focused on researching and documenting the column/field structure of the GSMA TAC/IMEI Device Database, with the person (referred to as Mohan) asking progressively more specific questions about the database schema. The work is clearly situated in a professional context involving MNO (Mobile Network Operator) certification tracking or device onboarding workflows, with references to internal tools like "DeliverableHub." Mohan demonstrated familiarity with GSMA terminology including TAC (Type Allocation Code), IMEI, TS.30, eUICC, NTN, LPWAN, and related 3GPP standards.

In the first exchange, Claude compiled a comprehensive list of fields and attributes from the GSMA TAC/IMEI Database sourced from the TS.30 v23.0 TAC Application Form, organized into categories covering identification, company details, device identity, OS, radio interfaces, LPWAN, LTE, 5G NR, SIM/UICC/eSIM configuration, IMS emergency call support, and band profile confirmation. Claude also produced a structured Excel spreadsheet (gsma_tac_columns.xlsx) with 75 column entries including mandatory/optional flags, data types, allowed values, and TS.30 source notes. In the second exchange, Mohan provided five specific column names encountered in practice — "eUICC", "Standardized_Name", "GSMA_NONREMOVABLE_eUICC", "Band_Support", and "GSMA_Name" — and asked Claude to trace their origins and map them to TS.30. Claude analyzed each column name, noting that these appear to be from the restricted GSMA Device Database export schema rather than the raw TS.30 input form, and provided detailed mapping rationale for each, including the observation that the "GSMA_" prefix likely distinguishes native TAC allocation fields from DeviceAtlas/Device Map enrichment columns. Claude offered to update the spreadsheet with these mappings as an additional sheet.

---

## User

Get full list of columns/attributes in GSMA TAC/IMEI database.

---

## Assistant

> **Tool:** web_search

<details>
<summary>Tool output</summary>

```
[{'type': 'knowledge', 'title': 'IMEI DATABASE - Industry Services', 'url': 'https://www.gsma.com/solutions-and-impact/industry-services/imei-database/', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'gsma.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=gsma.com', 'site_name': 'GSMA'}, 'is_missing': False, 'text': 'All the services and information previously visible through https:imeidb.gsma.com/imei/index can now be viewed here, www.gsma.com/services. To speed up
```
</details>

> **Tool:** web_search

<details>
<summary>Tool output</summary>

```
[{'type': 'knowledge', 'title': 'IMEI Database Application Form Version 21.0 02 October ...', 'url': 'https://www.gsma.com/newsroom/wp-content/uploads//TS.30-v21.0-IMEI-Database-Application-Form.pdf', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'gsma.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=gsma.com', 'site_name': 'GSMA'}, 'is_missing': False, 'text': '... Names must be between 1 and 50 characters long. ... Details of the device the TAC will be used for. 
```
</details>

> **Tool:** web_fetch

<details>
<summary>Tool output</summary>

```
[{'type': 'knowledge', 'title': '', 'url': 'https://www.gsma.com/newsroom/wp-content/uploads//TS.30-v23.0-GSMA-TAC-Application-Form.pdf', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'gsma.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=gsma.com', 'site_name': 'gsma'}, 'is_missing': False, 'text': 'GSM Association Non-confidential\r\nOfficial Document TS.30 - IMEI Database Application Form:\r\nV23.0 Page 1 of 40\r\nGSMA TAC Application Forms:\r\nVersion 23.0\r\n0
```
</details>

> **Tool:** web_search

<details>
<summary>Tool output</summary>

```
[{'type': 'knowledge', 'title': 'Device attribute data - Device Services', 'url': 'https://www.gsma.com/solutions-and-impact/industry-services/device-services/gsma-device-attribute', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'gsma.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=gsma.com', 'site_name': 'GSMA'}, 'is_missing': False, 'text': 'The TAC (Type Allocation Code) which forms the first 8 digits of a mobile device’s unique 15-digit IMEI (International Mob
```
</details>

> **Tool:** web_search

<details>
<summary>Tool output</summary>

```
[{'type': 'knowledge', 'title': 'Device attribute data - GSMA Services', 'url': 'https://www.gsmaservices.com/device-services/device-attribute-data/', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'gsmaservices.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=gsmaservices.com', 'site_name': 'GSMA Services'}, 'is_missing': False, 'text': 'Information to identify and validate devices, such as the manufacturer, model, hardware information, operating system, IoT type, 
```
</details>

Mohan, here's the comprehensive list of fields/attributes in the GSMA TAC/IMEI Database, compiled from the **TS.30 v23.0 TAC Application Form** (the authoritative source of what manufacturers submit) and recent GSMA Device Database enhancements.

---

**Identification & Company Fields**

- TAC (Type Allocation Code — 8 digits)
- Applicant Name
- Applicant Email Address
- Brand Name
- OEM Status (Yes/No — if No, ODM/IDH details required: Company Name, Address, Contact Name, Contact Email)
- Manufacturer Organization ID (OrgId — 15-character unique identifier)
- TAC Allocation Date
- Last Updated Date (recently added)

**Device Identity Fields**

- Equipment Type (dropdown): Mobile Phone/Feature Phone, Smartphone, Tablet, IoT Device, Wearable, Dongle, Modem, WLAN Router, ADP (Automatic Processing of Data / Point of Sale), UAS/UAV, Vehicle TCU
- Model Name
- Marketing Name (up to 3, comma-separated)
- Quantity of TAC Requested (1–5, each TAC = 1M IMEIs)

**Operating System / Platform**

- Operating System (dropdown): Android, Android Wear, Bada, BlackBerry, CyanogenMod, Firefox, iOS, KaiOS, Linux, MAC OS, Nucleus, Proprietary OS, Phoenix, RTOS, S30, Sailfish, Symbian, ThreadX, TIZEN, UBUNTU, Windows, Windows Phone, YunOS (Aliyun), None, Other

**Certification**

- Device Certification Bodies (optional — e.g., CE, FCC, IC, GCF, PTCRB, CCC, Anatel)

**Radio Interface & Connectivity**

- Other Radio Interfaces Supported: CDMA, 3GPP2, None
- NTN (Non-Terrestrial Network) Support: 3GPP NTN Only / 3GPP NTN & TN / No
  - GSO (Geostationary Orbit) satellite support (Y/N)
  - NGSO (Non-Geostationary Orbit) satellite support (Y/N)
  - NTN Frequency Bands

**LPWAN (Low Power Wide Area Network)**

- EC-GSM-IoT support (Y/N)
- Cat-NB1 support (Y/N)
- Cat-NB2 support (Y/N)
- Cat-NB Multicast support (Y/N)
- Cat-NB E-UTRA FDD Bands (Bands 1–85, selectable)
- Cat-NB E-UTRA TDD Bands (Bands 33–51, selectable)
- Cat-M1 support (Y/N)
- Cat-M2 support (Y/N)
- Cat-M E-UTRA FDD Bands
- Cat-M E-UTRA TDD Bands
- Cat-M Multicast support (Y/N)

**LTE Capabilities**

- LTE Category supported (Y/N)
- LTE UL/DL Category (0–12)
- Explicit LTE DL Category (0, 1bis, 4, 6, 7, 9, 10, 11, etc.)
- LTE MIMO Configuration (default 2×2; "None" for IoT)
- Carrier Aggregation (CA) Band Combinations supported
- VoLTE support

**2G / 3G Band Support (GSM / WCDMA)**

- GSM Bands supported (e.g., 850, 900, 1800, 1900)
- WCDMA/UMTS Bands supported

**4G E-UTRA (LTE) Band Support**

- E-UTRA FDD Bands
- E-UTRA TDD Bands

**5G NR Band Support**

- NR FDD Bands
- NR TDD Bands
- NR SA (Standalone) support
- NR NSA (Non-Standalone) support
- 5G RedCap (Reduced Capability) support

**SIM / UICC / eSIM Configuration**

- Number of SIM Slots
- Removable UICC quantity
- Non-removable UICC quantity
- Removable eUICC quantity
- Non-removable eUICC quantity
- Number of IMEIs supported
- eSIM support (SGP.22 Consumer / SGP.02 M2M)

**IMS Emergency Call Support (newer attributes)**

- Authenticated IMS Emergency Calls
- Unauthenticated IMS Emergency Calls
- IMS Emergency Calls with no UICC or eUICC Profiles

**Band Profile / Performance**

- Supported Frequency Band Confirmation (signed off by RB)
- Band performance data (available via Device Map)

---

**Important distinctions to keep in mind:**

The **GSMA Device Database** contains the core TAC record data listed above — essentially what manufacturers submit through the TS.30 form. The **GSMA Device Map** (partnership with DeviceAtlas/Afilias) enriches each TAC with 100–220+ additional properties like screen size, browser capabilities, multimedia features, Bluetooth version, NFC, GPS, etc. — but those enriched properties are *not* part of the official GSMA TAC allocation dataset.

The Device Database was also recently expanded to include new device classifications for UAV/UAS and Vehicle TCUs, plus a "last updated date" on each TAC record.

If you're building this into your MNO certification tracking or DeliverableHub workflows, the TS.30 fields are the ones you'll encounter directly when dealing with TAC allocations and device onboarding. Want me to put this into a structured spreadsheet or reference doc?

---

## User

Can you list down column names for the fields/attributes you listed down?

---

## Assistant

Let me search for the actual column/header names used in the GSMA Device Database export files.

> **Tool:** web_search

<details>
<summary>Tool output</summary>

```
[{'type': 'knowledge', 'title': 'Data - GSMA Intelligence', 'url': 'https://www.gsmaintelligence.com/data/', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'gsmaintelligence.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=gsmaintelligence.com', 'site_name': 'GSMA Intelligence'}, 'is_missing': False, 'text': 'Export all data as excel, csv or connect directly to our API. We provide data on every mobile operator in every country worldwide, covering 1,250 mobile operat
```
</details>

> **Tool:** web_fetch

<details>
<summary>Tool output</summary>

```
[{'type': 'knowledge', 'title': 'How to download the GSMA file', 'url': 'https://www.scribd.com/document/710808885/How-to-download-the-GSMA-file', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'scribd.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=scribd.com', 'site_name': 'scribd'}, 'is_missing': False, 'text': 'Download GSMA Device Database Guide | PDF\n\nSkip to main content\n\n[Open navigation menu](#sidebar)[![Scribd](data:image/svg+xml;base64,PD94bWwgdmVyc2
```
</details>

> **Tool:** web_search

<details>
<summary>Tool output</summary>

```
[{'type': 'knowledge', 'title': 'Device attribute data - Device Services', 'url': 'https://www.gsma.com/solutions-and-impact/industry-services/device-services/gsma-device-attribute', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'gsma.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=gsma.com', 'site_name': 'GSMA'}, 'is_missing': False, 'text': 'Information to identify and validate devices, such as the manufacturer, model, hardware information, operating system, IoT
```
</details>

Mohan, the GSMA Device Database is a restricted product, so the exact export column headers aren't published publicly. However, I can derive the definitive column names from the **TS.30 v23.0 TAC Application Form** field names (which is what feeds the database) and supplement with what's referenced in documentation. Let me put this into a clean spreadsheet for you.

> **Tool:** view

<details>
<summary>Tool output</summary>

```
[{'type': 'text', 'text': '     1\t---\n     2\tname: xlsx\n     3\tdescription: "Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .xlsx, .xlsm, .csv, or .tsv file (e.g., adding columns, computing formulas, formatting, charting, cleaning messy data); create a new spreadsheet from scratch or from other data sources; or convert between tabular file formats. Trigger especially when the user r
```
</details>

> **Tool:** create_file

<details>
<summary>Tool output</summary>

```
[{'type': 'text', 'text': 'File created successfully: /home/claude/gsma_columns.py', 'uuid': '162ebaca-1476-4f9e-8458-9daaf40c99f8'}]
```
</details>

> **Tool:** bash_tool

<details>
<summary>Tool output</summary>

```
[{'type': 'text', 'text': '{"returncode":0,"stdout":"Saved to /home/claude/gsma_tac_columns.xlsx\\n","stderr":""}', 'uuid': '28b1407d-6a56-4c08-b9c1-2cd14fbd8004'}]
```
</details>

> **Tool:** bash_tool

<details>
<summary>Tool output</summary>

```
[{'type': 'text', 'text': '{"returncode":0,"stdout":"","stderr":""}', 'uuid': 'd4ae91f2-4d78-489f-9276-6e912f9be6d2'}]
```
</details>

> **Tool:** present_files

<details>
<summary>Tool output</summary>

```
[{'type': 'local_resource', 'file_path': '/mnt/user-data/outputs/gsma_tac_columns.xlsx', 'name': 'gsma tac columns', 'mime_type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'uuid': '27618121-4b51-4bfe-93e0-308acebaa7ac'}]
```
</details>

Here's the spreadsheet with 75 column/field names organized by category, each with its Mandatory/Optional flag, data type, allowed values, and notes traced back to **TS.30 v23.0**.

A couple of important caveats: the GSMA Device Database is a restricted product so the exact export header names aren't publicly documented — the column names I've used are derived directly from the TS.30 form field labels and naming conventions seen in documentation references (like `OrgId`, `BrandName`, `ModelName`, `EquipmentType`, `SIMSlotQuantity`, etc.). Your organization's actual download format may use slightly different casing or delimiters, but the field semantics will match. The fields marked with `M*` are conditionally mandatory — required only when a parent field triggers them (e.g., `NR_FDD_Bands` is required only when 5G is selected).

---

## User

I'm told there are columns with names "eUICC", "Standardized_Name", "GSMA_NONREMOVABLE_eUICC", "Band_Support", "GSMA_Name". Can you track them down and see where they might be coming from and how they are mapped to GSMA PRD TS.30?

---

## Assistant

Let me dig into these specific column names — they look like they could be from the actual GSMA Device Database export/API rather than the raw TS.30 form fields.

> **Tool:** web_search

<details>
<summary>Tool output</summary>

```
[{'type': 'knowledge', 'title': 'What is GSMA SGP.32? Diving into the eSIM IoT standard - Onomondo', 'url': 'https://onomondo.com/blog/what-is-gsma-sgp-32-esim-iot-standard/', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'onomondo.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=onomondo.com', 'site_name': 'Onomondo'}, 'is_missing': False, 'text': 'Imagine a zero-touch connectivity management experience for globally-distributed IoT devices of scale. With the GSMA 
```
</details>

> **Tool:** web_search

<details>
<summary>Tool output</summary>

```
[{'type': 'knowledge', 'title': '© GSMA 2023 1 Training Module Four: Completing the TAC Band Profile', 'url': 'https://imeidb.gsma.com/imei/resources/documents/GSMA_TAC_Allocation_Training_Module_4_Band_Profiles.pdf', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'gsma.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=gsma.com', 'site_name': 'Gsma'}, 'is_missing': False, 'text': 'One Band Profile can be applied to multiple TAC. ... Use the SAVE AS DRAFT button when 
```
</details>

> **Tool:** web_search

<details>
<summary>Tool output</summary>

```
[{'type': 'knowledge', 'title': 'IMEI Database - Working Groups', 'url': 'https://www.gsma.com/get-involved/working-groups/terminal-steering-group/imei-database/', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'gsma.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=gsma.com', 'site_name': 'GSMA'}, 'is_missing': False, 'text': 'Each IMEI consists of 3 key parts – Type Allocation Code (TAC), Serial Number and a Check Digit. The GSMA allocates official TAC numbers to m
```
</details>

Mohan, here's what I've found. These specific column names don't appear in any publicly available GSMA documentation — which is expected because the **actual GSMA Device Database export schema** (the CSV/XML file you download as an MNO or partner) is restricted and not published in the PRDs. The TS.30 defines the *input form* fields, but the *output export* format uses its own column naming convention.

That said, based on the naming patterns, TS.30 field semantics, and what we know about the DB structure, here's the most likely mapping:

---

**1. `GSMA_Name`**

This almost certainly maps to the **Marketing Name** field from TS.30 Section 3.4. In TS.30, there are two name fields: `Model Name` (the internal/technical name) and `Marketing Name` (the consumer-facing name). The `GSMA_Name` prefix suggests this is the GSMA-authoritative device name as it appears in their database — likely the Marketing Name or a GSMA-normalized composite of Brand + Marketing Name. It could also be a system-generated display name like "Samsung Galaxy S24 Ultra" assembled from Brand + Marketing Name fields.

**TS.30 mapping:** `Marketing Name` (Section 3.4) — or a derived/composite field combining `Brand Name` + `Marketing Name`.

---

**2. `Standardized_Name`**

This is not a raw TS.30 form field. It's likely a **post-processing / normalization column** added by the GSMA Device Database system (or by GSMA Device Map / DeviceAtlas enrichment) to create a canonical, deduplicated device name. Manufacturers often submit inconsistent naming — "Galaxy S24," "SM-S921B," "Galaxy S24 5G" could all be the same device across different TACs. A `Standardized_Name` would resolve these to one canonical string for analytics and reporting.

**TS.30 mapping:** Derived from `Brand Name` + `Model Name` + `Marketing Name` (Section 3.2, 3.3, 3.4). The **Naming Consistency Check** described in TS.30 Section 3.3 is the input-side mechanism that attempts to catch this at submission time by matching similar names and prompting the applicant.

---

**3. `eUICC`**

This maps to the eUICC-related fields on the TS.30 TAC form. In TS.30 v25.0, the form has separate fields for removable vs. non-removable UICC and eUICC quantities. A single `eUICC` column in the export likely represents a **boolean or aggregate** — i.e., "does this device have any eUICC capability at all?" (Yes/No), or it could be the total eUICC count (Removable eUICC + Non-Removable eUICC).

**TS.30 mapping:** Derived from the combination of `Removable eUICC Quantity` + `Non-Removable eUICC Quantity` fields (TS.30 Section 3.4, under the UICC/eUICC designation block).

---

**4. `GSMA_NONREMOVABLE_eUICC`**

This is a direct match to the **Non-Removable eUICC Quantity** field from TS.30. The naming convention with the `GSMA_` prefix is consistent with how the Device Database export distinguishes its columns from DeviceAtlas/Device Map enriched columns. The export likely uses `GSMA_` prefixed columns for fields sourced directly from the TAC allocation form and unprefixed columns for enriched/derived data.

**TS.30 mapping:** `Non-Removable eUICC Quantity` (TS.30 Section 3.4) — the count of embedded/soldered eUICC chips that support eSIM remote provisioning per SGP.21/SGP.22. Value is typically 0, 1, or 2.

---

**5. `Band_Support`**

This is almost certainly a **flattened/aggregated representation** of the entire Band Profile. In TS.30, band support is captured across many separate fields: GSM bands, WCDMA bands, E-UTRA FDD/TDD bands, NR FDD/TDD bands, Cat-NB bands, Cat-M bands — each as multi-select lists. The GSMA Device Database export likely consolidates all of these into a single `Band_Support` column as a delimited string or coded list (e.g., "GSM850,GSM1900,LTE1,LTE2,LTE3,LTE4,LTE7,NRn71,NRn77").

**TS.30 mapping:** Composite of all band fields from TS.30 Section 3.4 + the Band Profile (Training Module 4). Specifically: `GSM Bands` + `WCDMA Bands` + `E-UTRA FDD/TDD Bands` + `NR FDD/TDD Bands` + `Cat-NB Bands` + `Cat-M Bands` + `NTN Frequency Bands`. This also corresponds to the "Supported Frequency Band Confirmation" signed off by the Reporting Body.

---

**Summary Table**

| Export Column Name | Likely TS.30 Source Field(s) | Type in Export | Notes |
|---|---|---|---|
| `GSMA_Name` | Marketing Name (Sec 3.4) | Text | Possibly Brand + Marketing Name composite |
| `Standardized_Name` | Derived from Brand + Model + Marketing Name (Sec 3.2-3.4) | Text | Post-processing normalization; not a raw form field |
| `eUICC` | Removable eUICC Qty + Non-Removable eUICC Qty | Boolean or Integer | Aggregate eSIM capability flag or total count |
| `GSMA_NONREMOVABLE_eUICC` | Non-Removable eUICC Quantity (Sec 3.4) | Integer | Direct field; `GSMA_` prefix = sourced from TAC form |
| `Band_Support` | All band multi-select fields + Band Profile | Text (delimited) | Flattened aggregate of GSM/WCDMA/LTE/NR/LPWAN/NTN bands |

---

The `GSMA_` prefix convention is a strong clue — it likely distinguishes **native GSMA Device Database columns** (from TAC allocation data) from columns added by the **GSMA Device Map / DeviceAtlas enrichment layer**. If your team has access to the Device Database portal, the column schema documentation should be accessible under the download/export section. You could also reach out to `tac@gsma.com` or your GSMA account contact to get the formal export schema document — it's not governed by a PRD but likely has an internal reference guide.

Want me to update the spreadsheet I made earlier to include these mappings as an additional sheet?

---
