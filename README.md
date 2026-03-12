# Mortgage_Automation_AI

Intelligent Document Processing, Classification, and Workflow Automation for Mortgage Operations

This project demonstrates how applied AI, LLM-based automation, and multi-agent workflows can streamline key steps in the mortgage process. It simulates a LoanDepot-style system that ingests borrower documents, classifies them, extracts structured information, validates it against underwriting rules, and generates an underwriter-ready summary. The goal is to show how modern AI can reduce manual review, improve accuracy, and accelerate the mortgage experience for both customers and operations teams.

---

## What this project solves

Mortgage operations rely on manual review of income documents — a slow, error-prone process that delays underwriting decisions. This project shows how AI-assisted automation can:

- extract key borrower fields
- apply underwriting rules (DTI, minimum income)
- generate an underwriter-style summary
- produce consistent, auditable results

---

## System architecture

The pipeline mirrors a real mortgage workflow:

Ingestion -> Extraction -> Validation -> Underwriter Summary

### Components

- Ingestion — loads raw text documents into a structured Document object
- Extraction — simulates AI/LLM extraction using regex to pull borrower name, employer, income, and debt
- Validation — applies underwriting rules (DTI, minimum income) from YAML config
- Summarization — generates a concise, human-readable underwriter summary
- Pipeline — orchestrates the full workflow
- Demo script — runs the pipeline on a sample W-2

---

## Folder structure

Mortgage_Automation_AI/ | +-- data/ |   +-- samples/ |       +-- sample_w2.txt | +-- src/ |   +-- mortgage_ai/ |       +-- ingestion.py |       +-- extraction.py |       +-- validation.py |       +-- summarization.py |       +-- pipeline.py |       +-- rules/ |           +-- underwriting_rules.yaml | +-- demo.py


---

## How to run the demo

Install dependencies:

pip install pyyaml


Run the pipeline:

python demo.py


Expected output:

=== Extracted Fields === {'borrower_name': 'John Doe', 'employer': 'Acme Corporation', 'income': 85000.0, 'monthly_debt': 2500.0}
=== Validation Results === {'flags': ['high_dti'], 'computed': {'dti': 0.35}}
=== Underwriter Summary === Borrower: John Doe Employer: Acme Corporation Reported annual income: 85000.0 Estimated DTI: 0.35 Flags:
- DTI exceeds guideline threshold.
