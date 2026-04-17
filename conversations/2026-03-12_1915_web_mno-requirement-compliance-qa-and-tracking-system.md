# MNO requirement compliance Q&A and tracking system

**Date:** 2026-03-12  
**Source:** Claude Web/App  
**ID:** `aedd7575-c203-4909-a011-b72ea612af88`

**Summary:** **Conversation overview**

The person works at a connected device company where their team builds devices that connect via Mobile Network Operator (MNO) cellular networks. Their role involves managing MNO technical approvals, which requires tracking compliance against MNO-published requirement documents across functional areas including VoLTE, VoWiFi, IMS, RCS, and Android platform. They provided detailed context about how MNO requirements are structured: quarterly releases with versioned documents per functional area, requirement IDs, cross-references, glossaries, standard references (3GPP, GSMA), and MNO-specific customizations on top of standards. Devices are locked to specific requirement release versions at launch, and compliance is tracked per-device per-requirement with YES/NO/PARTIAL statuses and comments collected from distributed R&D teams.

The person asked Claude to design a full technical architecture for an AI-powered MNO Requirement and Compliance platform supporting five use cases: requirement Q&A (e.g., IMS registration behavior for a specific MNO), version delta analysis between quarterly releases, per-device compliance lookup, cross-device compliance comparison, and automated compliance sheet generation using a baseline device with chipset-aware change detection. Claude produced a comprehensive Word document covering a six-layer architecture: document ingestion pipeline with MNO-specific parser profiles and a versioning/diffing engine, a hybrid RAG knowledge store (vector DB plus BM25 with cross-encoder reranking), a PostgreSQL compliance data store with a chipset capability matrix, a supervisor-worker agent orchestration layer with five specialized agents, LLM integration patterns with hallucination prevention, and a three-phase implementation roadmap over approximately 26 weeks. An architecture diagram was also rendered inline.

In the follow-up, the person reported that their already-built basic RAG system fails on queries requiring reasoning across multiple requirements spanning multiple documents. Claude proposed a layered multi-hop retrieval solution prioritized by implementation effort: agentic query decomposition (breaking complex queries into atomic sub-questions with functional-area metadata filters), cross-reference graph expansion (one-to-two hop traversal of the explicit requirement cross-reference index built during ingestion), an iterative sufficiency check loop (LLM judge evaluates whether retrieved context covers all sub-questions and triggers targeted re-retrieval for gaps), hierarchical parent-child chunking (section context pulled on demand), and semantic clustering of requirements by functional concept for comprehensive coverage queries. Claude recommended implementing in that order — decomposition first as the highest-impact, lowest-effort change — and offered to draft prompt templates for the decomposition and sufficiency check steps or detail the cross-reference extraction logic.

---

## User

I work for a company that makes connected devices. These connected devices use Mobile Network Operator (MNO) Cellular Networks for connectivity. To be able to launch these devices, we need to obtain technical approvals from MNOs. After we submit devices with specific SW supporting various features (many of which are our own and some features correspond to Network capabilities that MNOs support), MNOs test the devices in the lab and field, and then provide approval.  These MNOs release device requirements that need to be supported by devices to access their Network capabilities. MNOs requirements also specify specific application requirements (functional and UX), device platform (Android) requirements, MNOs own application preload requirements etc.  Each MNO release requirements in their own format. At a high level : 1) Each functional area (e.g., VoLTE, VoWiFi, Android platform etc) usually have a requirement document. 2) Most of the Network and device functionalities are already specified in standards like GSMA, 3GPP, but MNOs have their own customizations on top of standards, which are captured in their requirements. 3) Each requirement document usually has glossary of terms used, usually refers to some standard if applicable, and specification their customization. 4) Each requirement usually has a requirement ID 5) Requirements can cross reference other requirements in the same doc or other docs 6) Each requirement itself is a simple text explaining expected device implementation and behavior of an aspect captured in the requirement.  MNOs release requirements every quarter. Each release usually have some changes from previous version. Some times, new feature requiremnts are added. They also release test plan documents to verify requiement compliance.  Each of our device is locked down to a specific requirement release version at launch. Before we begin development, we lock down the features, fill out compliance lock down document that specifies yes or no or partial to each requirement id for each requirement document. In case of no and partial, we also provide some comments explaining our position.   Now my team wants to develop a requirement & compliance Q&A bot, as well as a bot that collects compliances from all R&D teams for each requirement. We use internal LLM and Agentic APIs. Below are few use-cases. 1) List down requirements pertaining to a specific question (e.g., What is the expected behavior of IMS registration fails for MNO XXX? What are IMS specific customizations that XXX MNO has per latest requirements) 2) List down differences between latest requirements of XXX MNO from previous version 3) What the compliance of device AA for the requirement RR for MNO XXX? 4) What is the compliance difference between device AA and device BB? 5) Create compliance sheet for device BB, using AA's sheet as baseline. BB has chipset C2 while AA had chipset C1. So, high light which compliance items need to be manually updated.  I want you to propose a full detailed technical solution on how to achieve this using our internal LLM, RAG and Agentic AI.

---

## Assistant

This is a substantial enterprise system. Let me put together a comprehensive technical architecture document for you.

> **Tool:** view

<details>
<summary>Tool output</summary>

```
[{'type': 'text', 'text': '     1\t---\n     2\tname: docx\n     3\tdescription: "Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of \'Word doc\', \'word document\', \'.docx\', or requests to produce professional documents with formatting like tables of contents, headings, page numbers, or letterheads. Also use when extracting or reorganizing content from .docx files, inserting or replacing images in document
```
</details>

> **Tool:** bash_tool

<details>
<summary>Tool output</summary>

```
[{'type': 'text', 'text': '{"returncode":0,"stdout":"/home/claude/.npm-global/lib\\n`-- docx@9.5.3\\n\\n","stderr":""}', 'uuid': 'de02643c-1676-4e89-b200-7c566e027e05'}]
```
</details>

> **Tool:** create_file

<details>
<summary>Tool output</summary>

```
[{'type': 'text', 'text': 'File created successfully: /home/claude/generate_doc.js', 'uuid': '2a484b21-4077-4bd3-95f5-30acb98e78dd'}]
```
</details>

> **Tool:** bash_tool

<details>
<summary>Tool output</summary>

```
[{'type': 'text', 'text': '{"returncode":0,"stdout":"Document created successfully.\\n","stderr":""}', 'uuid': 'fa73b998-9c1d-46de-ba55-fbcae7e078c7'}]
```
</details>

> **Tool:** bash_tool

<details>
<summary>Tool output</summary>

```
[{'type': 'text', 'text': '{"returncode":0,"stdout":"\\nParagraphs: 0 → 611 (+611)\\nAll validations PASSED!\\n","stderr":""}', 'uuid': '2598686d-a825-4549-9421-35a664c1068b'}]
```
</details>

Now let me also create a high-level architecture diagram to accompany the document.

> **Tool:** visualize:read_me

<details>
<summary>Tool output</summary>

```
[{'type': 'text', 'text': '# Imagine — Visual Creation Suite\n\n## Modules\nCall read_me again with the modules parameter to load detailed guidance:\n- `diagram` — SVG flowcharts, structural diagrams, illustrative diagrams\n- `mockup` — UI mockups, forms, cards, dashboards\n- `interactive` — interactive explainers with controls\n- `chart` — charts and data analysis (includes Chart.js)\n- `art` — illustration and generative art\nPick the closest fit. The module includes all relevant design guidan
```
</details>

> **Tool:** visualize:show_widget

<details>
<summary>Tool output</summary>

```
[{'type': 'text', 'text': "Content rendered and shown to the user. Please do not duplicate the shown content in text because it's already visually represented.", 'uuid': '28e07064-ace6-4c69-b3cc-ebdd3023fe15'}, {'type': 'text', 'text': '[This tool call rendered an interactive widget in the chat. The user can already see the result — do not repeat it in text or with another visualization tool.]', 'uuid': 'a7c2a3db-6eba-44e6-8d94-f24ce951860a'}]
```
</details>

> **Tool:** present_files

<details>
<summary>Tool output</summary>

```
[{'type': 'local_resource', 'file_path': '/mnt/user-data/outputs/MNO_Requirement_Compliance_AI_Platform_Architecture.docx', 'name': 'MNO Requirement Compliance AI Platform Architecture', 'mime_type': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'uuid': 'd178f653-efa4-445a-a4c3-f2410babeac9'}]
```
</details>

Here's the full technical architecture document along with the system overview diagram above. The solution has six layers:

**Document Ingestion Pipeline** — MNO-specific parser profiles normalize heterogeneous requirement formats (PDF, DOCX, Excel) into a canonical schema with requirement IDs, cross-references, standards mappings, and version lineage. A diffing engine pre-computes changes between quarterly releases so delta queries are instant.

**Knowledge Store (RAG)** — Requirements are chunked at the individual requirement level (the natural compliance boundary), embedded with domain context, and indexed in both a vector DB and a BM25 full-text index. A hybrid retrieval strategy with cross-encoder reranking handles both natural-language questions and exact ID/spec lookups.

**Compliance Data Store** — A relational DB holding per-device, per-requirement compliance records alongside a chipset capability matrix. This is the structured backbone for use cases 3–5.

**Agent Orchestration** — A supervisor-worker pattern where a Planning Agent classifies queries, decomposes them into execution plans, and routes to five specialized worker agents (Requirement Retrieval, Version Delta, Compliance Query, Compliance Comparison, Compliance Generator). The Compliance Generator agent is the most complex — it clones baseline sheets, computes chipset capability deltas, maps impacted requirements, and flags items for manual review.

**LLM Integration** — Structured prompts with citation enforcement, retrieval-only constraints, and post-generation validation to minimize hallucination in this high-stakes compliance domain.

**Implementation Roadmap** — Three phases over ~26 weeks, delivering incremental value starting with Q&A and compliance lookup, then adding delta analysis and comparisons, and finally the automated compliance sheet generation workflow.

The document includes detailed schemas for every data model, the full agent specification for each use case, and a quality/evaluation framework with target metrics. Let me know if you'd like me to dive deeper into any specific area — for example, the prompt engineering templates, the chipset impact mapping logic, or the compliance collection bot workflow.

---

## User

We have already built a basic RAG system and evaluating it. What we are finding is that it is not able to answer queries that need to consider multiple requirements. What kind of technique you propose so that this system can answer complex queries by considering multiple requirements that span across multiple documents?

---

## Assistant

This is one of the most common failure modes in requirement-domain RAG. A query like "What is the expected IMS registration behavior when the device is on Wi-Fi with ePDG fallback?" might need to pull from VoWiFi requirements, IMS registration requirements, ePDG tunnel requirements, and potentially timer/retry requirements — spread across three or four documents. Basic top-K retrieval grabs the closest single-topic chunks and misses the rest.

Let me lay out a layered approach to solve this.

> **Tool:** visualize:show_widget

<details>
<summary>Tool output</summary>

```
[{'type': 'text', 'text': "Content rendered and shown to the user. Please do not duplicate the shown content in text because it's already visually represented.", 'uuid': '56a661ec-20af-47f3-a95b-260e3098baf7'}, {'type': 'text', 'text': '[This tool call rendered an interactive widget in the chat. The user can already see the result — do not repeat it in text or with another visualization tool.]', 'uuid': 'c8568fe6-793a-402a-8103-ee0b0f27c9c9'}]
```
</details>

The diagram above shows the full pipeline. Let me walk through each technique and why it matters for your domain specifically.

## 1. Agentic query decomposition

This is the single biggest improvement you can make. Before any retrieval happens, feed the user's query to your LLM with a decomposition prompt that breaks it into atomic sub-questions, each scoped to a single functional area or document.

For example, a query like *"What happens when IMS registration fails over Wi-Fi with ePDG for MNO XYZ?"* becomes three sub-queries: one targeting IMS registration error handling, one targeting VoWiFi/ePDG tunnel establishment requirements, and one targeting fallback and retry behavior. Each sub-query gets its own retrieval pass with targeted metadata filters (functional area, document type). This is dramatically more effective than a single broad retrieval against the full corpus because the embedding for the original complex query sits in a vague region of vector space that doesn't match any single requirement well — but each decomposed sub-query lands precisely on its target requirements.

The decomposition prompt should be domain-aware. Include the list of your functional areas (VoLTE, VoWiFi, IMS, RCS, Android Platform, etc.) and document types so the LLM can route each sub-query to the right metadata filter. You can also provide it with a few examples of good decompositions from your domain to guide its output.

## 2. Cross-reference graph expansion

This is specific to your domain and extremely high-value. MNO requirements are heavily cross-referenced — a VoWiFi requirement might say "IMS registration shall follow REQ-IMS-042" or "per 3GPP TS 24.229 section 5.1.1.3." Your basic RAG ignores these links entirely.

Build an explicit cross-reference index during ingestion. Every time the parser encounters a reference to another requirement ID, a standard section, or even a shared concept, store that as an edge in a lightweight graph (this can be a simple adjacency table in PostgreSQL — you don't necessarily need Neo4j). Then, after initial retrieval, run a one-to-two hop expansion: for every retrieved requirement, pull its directly cross-referenced requirements and add them to the context set. This is how you bridge across documents without the user needing to know which documents to look in.

The critical nuance here is to limit expansion depth. One hop catches direct references (which covers most cases). Two hops is useful for chains like "REQ-VOWIFI-010 references REQ-IMS-042 which references REQ-TIMER-005." Beyond two hops, you get too much noise. You can also weight the expansion — explicit requirement ID references get full weight, while weaker links (shared 3GPP section reference) get lower priority in the reranking step.

## 3. Iterative retrieval with a sufficiency check

This is the "agentic loop" that makes the system self-correcting. After merging the results from all sub-queries and the cross-reference expansion, run a sufficiency check by asking the LLM: "Given these retrieved requirements, can each of the following sub-questions be fully answered?" Pass it the sub-questions and the retrieved requirement texts.

If the LLM identifies a gap — say the IMS timer values weren't found — it generates a refined follow-up query targeting that specific gap. This follow-up gets another retrieval pass, and the results are merged into the growing context set. You typically cap this at two to three iterations to avoid runaway loops. In practice, most queries resolve in one or two iterations.

This pattern is critical for your domain because MNO requirements often have implicit dependencies that aren't captured by explicit cross-references. A requirement might say "the device shall use the configured T1 timer" without citing the requirement that defines T1's default value. The sufficiency check catches these gaps.

## 4. Hierarchical document context (parent-child chunking)

Your current system likely chunks each requirement in isolation. Add a parent-child relationship: each requirement chunk stores a pointer to its parent section and the document-level metadata (the glossary terms, the document's scope statement, the applicable device categories). When a requirement is retrieved, you can optionally pull its section-level context to give the LLM the framing it needs.

For instance, a requirement saying "the device shall retry" is ambiguous without its section context — retry what? But if you include the section header "5.3.2 IMS PDN Connection Recovery," the LLM can reason about it correctly. You don't embed the parent section — you just store the relationship and pull it into the LLM's context window on demand.

## 5. Semantic clustering for related requirements

During ingestion, cluster requirements by semantic similarity within each MNO's corpus. Requirements about IMS registration retry timers, IMS registration error codes, and IMS registration guard timers will naturally cluster together even if they're in different sections or documents. Store the cluster ID on each requirement record.

At retrieval time, when you find a highly relevant requirement, you can pull its cluster neighbors as candidates. This catches related requirements that aren't linked by explicit cross-references but are about the same functional concept. It's particularly effective for questions like "What are all the IMS-specific customizations for MNO XYZ?" where you need comprehensive coverage rather than a single best match.

## 6. Putting it all together: the retrieval chain

Here's how these techniques compose for a single complex query:

The LLM decomposes the query into two to four sub-questions with metadata filters. Each sub-question gets a parallel hybrid retrieval pass (vector + BM25) scoped to the right functional area. The initial results go through cross-reference expansion (one to two hops) and optional cluster-neighbor expansion. All results are merged, deduplicated, and reranked with a cross-encoder. The sufficiency check evaluates coverage — if gaps remain, refined sub-queries target them for one more retrieval pass. Finally, the full context set (typically fifteen to twenty-five requirements from across multiple documents) goes to the LLM for synthesis with explicit citation of each requirement ID.

## Practical implementation priority

If you want the most impact for the least engineering effort, I'd suggest this order: start with query decomposition (biggest single improvement, purely prompt-engineering — you can prototype it in a day), then add the cross-reference graph expansion (requires a one-time ingestion change to extract and store cross-reference edges), then implement the sufficiency check loop (adds the self-correcting behavior), and finally add semantic clustering as a polish step for comprehensive coverage queries.

Would you like me to draft the actual prompt templates for the decomposition and sufficiency check steps, or dive into the cross-reference extraction logic for your ingestion pipeline?

---
