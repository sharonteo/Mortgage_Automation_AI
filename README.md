# Mortgage Automation AI  

[![gitcgr](https://gitcgr.com/badge/sharonteo/Mortgage_Automation_AI.svg)](https://gitcgr.com/sharonteo/Mortgage_Automation_AI)
A modular, end‑to‑end Claude‑powered document intelligence pipeline for mortgage underwriting workflows.

This project uses Anthropic’s Claude LLM alongside traditional extraction and validation logic to automate the repetitive steps of reviewing W‑2s, paystubs, and bank statements. The system ingests documents, detects the document type, extracts structured fields, validates them with document‑specific rules, and generates a clean underwriting‑style summary grounded in structured data.

The architecture is intentionally simple, modular, and production‑friendly — designed to scale to additional document types and integrate into real mortgage workflows

---

## 🚀 Features

- **Document ingestion**  
  Reads raw text from uploaded documents.

- **Document type detection**  
  Lightweight pattern‑based classifier for W‑2s, paystubs, and bank statements.

- **Field extraction**  
  Converts raw text into structured fields (income, employer, pay periods, YTD values, deposits, etc.).

- **Validation engine**  
  Document‑specific rules ensure required fields are present and consistent.

- **LLM‑powered summary**  
  Generates a clean, underwriting‑friendly summary grounded in structured fields.

- **Simple entry script**  
  Run the entire pipeline end‑to‑end with a single command.

---

## 🧠 Architecture Overview

### **Pipeline Flow**
```

┌────────────┐     ┌────────────────────┐     ┌──────────────────┐     ┌────────────────────────┐
│ Ingestion  │ --> │ Claude Extraction  │ --> │ Validation       │ --> │ Underwriter Summary    │
└────────────┘     └────────────────────┘     └──────────────────┘     └────────────────────────┘
```

Each step is isolated, testable, and easy to extend.

---

## 📁 Project Structure

```
Mortgage_Automation_AI/
│
├── data/
│   └── samples/
│       ├── sample_bank_statement.txt
│       ├── sample_paystub.txt
│       └── sample_w2.txt
│
├── src/
│   └── mortgage_ai/
│       ├── extraction.py
│       ├── ingestion.py
│       ├── pipeline.py
│       ├── summarization.py
│       ├── validation.py
│       └── __init__.py
│
├── tests/
│   ├── test_bank_statement_extraction.py
│   └── test_paystub_extraction.py
│
├── demo.py
├── claude_test.py
└── README.md
```
---

## 🏃‍♀️ How to Run

From the project root:

```bash
python demo.py data/samples/sample_paystub.txt
```

Or:

```bash
python demo.py --file data/samples/sample_w2.txt
```

The script will:

1. Ingest the document  
2. Detect the document type  
3. Extract structured fields  
4. Validate required fields  
5. Generate an underwriting‑style summary  
6. Save the output to `output.txt`

---

## 🧩 Extensibility

The system is designed to scale:

- Add new document types by creating a new extractor + validator  
- Add new validation rules without touching extraction logic  
- Swap in different LLMs or prompt templates  
- Integrate into an LOS or workflow engine as a service  

---

## 🛠 Future Improvements

- Add automated tests for extraction + validation  
- Add GitHub Actions for lightweight CI  
- Support multi‑month bank statements  
- Add anomaly detection for irregular deposits or income gaps  
- Add PDF ingestion instead of plain text  

---

## 📬 Contact

Built by Sharon Teo — Senior Data Scientist / ML Engineer.  
Focused on modular, production‑ready AI systems for real workflows.
