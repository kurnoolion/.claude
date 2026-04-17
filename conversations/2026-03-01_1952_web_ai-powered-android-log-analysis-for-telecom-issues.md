# AI-powered Android log analysis for telecom issues

**Date:** 2026-03-01  
**Source:** Claude Web/App  
**ID:** `8bd711b2-c3a8-4e36-8c37-8b3eb4078915`

---

## User

I'm an Android OS/framework and modem protocol Engineer. As part of my job, I analyze device logs provided by QA to root cause various issues related to eSIM, voice/messaging/data (VoLTE/VoNR/VoWiFi/RCS etc), application battery drain, telephony and connectivity framework, as well as all L2/L3/L4 protocols of 4G/5G. Of late, I also have been alayizing logs for Satellite connectivity related issues. I use Android logcat, dumpstate logs, as well as Qualcomm logs for modem issue analysis.  I want to develop a solution to analyze Android logs to to root cause the issues. Guide me on how I go about developing an AI/LLM based solution for log analysis. I want you to be thorough, use GSMA/3GPP specs, Android implementation, Qualcomm modem knowledge etc to come up with outline of a solution.

Assume our internal proprietary LLM was already trained on all Telecom standards. Create me comprehensive list of prompts and how to verify the LLM responses to test knowledge of our proprietary LLM on Telecom standards knowledge.

---

## Assistant

# Comprehensive LLM Telecom Knowledge Evaluation Framework

This framework tests your proprietary LLM across the full stack of telecom standards relevant to Android/Qualcomm log analysis. The prompts are designed to expose gaps, hallucinations, and depth of understanding — not just surface recall.

---

## Evaluation Philosophy

Before the prompts: establish a **grading rubric** for each response:

- **Factual Accuracy** — spec references correct (TS number, section, release)
- **Completeness** — covers all relevant sub-cases (e.g., doesn't describe NR but omit NSA)
- **Causal Reasoning** — can trace symptom → protocol event → root cause
- **Log Correlation** — maps spec behavior to actual log artifacts (cause codes, timers, IEs)
- **Hallucination Detection** — invents spec sections, timer values, or IE names that don't exist

---

## DOMAIN 1: eSIM / eUICC (SGP.02, SGP.22, SGP.32)

### Prompt Set 1.1 — Profile Lifecycle

**P1.1.1**
> "Walk through the complete SGP.22 M2M and Consumer profile download flow. For each ES interface (ES2+, ES8+, ES9+, ES10x), identify: the protocol used, the entities involved, the sequence of APDU commands exchanged, and what a failure at each interface looks like in Android logcat and eUICC HAL logs."

**Verification:**
- Must distinguish SGP.02 (M2M) from SGP.22 (Consumer) architectures
- ES9+ = HTTPS between LPA and SM-DP+; ES10b = LPA↔eUICC; ES10c = profile installation APDUs
- Should mention `EuiccService`, `EuiccConnector`, `IEuiccService` binder interface in Android
- Failure signatures: `HTTP 4xx` on ES9+, APDU SW `6982`/`6A88`, `euicc_error_code` in logcat
- Hallucination check: Verify any cited SGP.22 section numbers (§3.1 entity definitions, §3.6 ES interfaces)

**P1.1.2**
> "A QA device shows 'Profile Installation Failed' with eUICC error code 0x8. Decode this per SGP.22, explain the likely root cause, and describe the log artifacts you'd look for in: (a) Android EuiccService logs, (b) APDU trace, (c) network-side SM-DP+ logs."

**Verification:**
- Error 0x8 = `PPR_NOT_ALLOWED` or similar — LLM must map the hex to the correct SGP.22 Annex error table
- If it maps it incorrectly, flag as factual error
- Should mention `ProfileInstallationResult` in the ES8+ response and the `notificationList` mechanism

**P1.1.3**
> "Explain the eUICC Profile Policy Rules (PPR) defined in SGP.22. How does PPR1 (no disabling) and PPR2 (no deletion) affect profile management operations, and what Android HAL calls will return errors when these policies are enforced?"

---

### Prompt Set 1.2 — RSP Protocols

**P1.2.1**
> "Describe the TLS mutual authentication flow between LPA and SM-DP+ per SGP.22. What certificates are in the chain, what is the role of CI (Certificate Issuer), and what CI OIDs are defined by GSMA? How would a certificate mismatch manifest in Android logs?"

**Verification:**
- GSMA CI OIDs: 2.23.146.1.2.1.0 (test) and 2.23.146.1.2.1.1 (production)
- Must mention GSMA SGP.26 (Root CI public key) and SGP.11
- Android: `EuiccCardController`, TLS errors in `NetworkSecurityConfig` or OkHttp layer

---

## DOMAIN 2: 5G NR — Registration, Mobility, Session Management

### Prompt Set 2.1 — Registration Procedures

**P2.1.1**
> "Trace a 5G SA initial registration procedure per 3GPP TS 24.501. List every NAS message exchanged, the IEs that are mandatory vs optional in each, the 5GMM cause codes for common rejection scenarios, and how each rejection maps to what you'd see in Android telephony logcat and Qualcomm QXDM/QCAT logs."

**Verification:**
- Message sequence: Registration Request → Authentication Request/Response → Security Mode Command/Complete → Registration Accept/Reject
- Key IEs: 5GS registration type, SUCI,

---
