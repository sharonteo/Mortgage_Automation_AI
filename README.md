# Mortgage Automation AI  
Lightweight Claude‑powered pipeline for extracting and summarizing mortgage income documents.

This project demonstrates a clean, modular AI workflow for processing mortgage‑related documents. It ingests raw text, extracts key income fields using Claude, validates them, and produces a concise underwriter‑style summary. The design focuses on clarity, maintainability, and real‑world applicability for lending operations.

## Pipeline Overview

┌────────────┐     ┌────────────────────┐     ┌──────────────────┐     ┌──────────────────────┐
│ Ingestion  │ --> │ Claude Extraction  │ --> │ Validation        │ --> │ Underwriter Summary  │
└────────────┘     └────────────────────┘     └──────────────────┘     └──────────────────────┘

- Ingestion loads a text document and normalizes it into a Document object.
- Claude Extraction returns structured JSON fields such as employee name, employer, wages, and tax year.
- Validation checks for missing or invalid values and ensures numeric fields are well‑formed.
- Summary Generation uses Claude to produce a clear, professional narrative suitable for underwriting review.

## Project Structure

Mortgage_Automation_AI/
│
├── demo.py
│
├── data/
│   └── samples/
│       └── sample_w2.txt
│
└── src/
    └── mortgage_ai/
        ├── __init__.py
        ├── ingestion.py
        ├── extraction.py
        ├── validation.py
        ├── summarization.py
        └── pipeline.py

## Installation

Install dependencies:

python -m pip install anthropic

Set your Anthropic API key:

setx ANTHROPIC_API_KEY "sk-ant-xxxxxxxx"

(After setting the key, close and reopen your terminal.)

## Running the Demo

Run the end‑to‑end pipeline:

python demo.py

Expected output includes:

- Extracted fields returned by Claude
- Validation messages
- A generated underwriter summary

## Sample Input File

data/samples/sample_w2.txt

Employee Name: John Doe
Employer: ACME Corp
Wages: $85,000.00
Tax Year: 2024

## How It Works

### Ingestion
Loads a text file and wraps it in a Document object with a `.text` attribute used throughout the pipeline.

### Claude Extraction
Uses the Claude model to extract structured JSON fields. Missing fields are returned as null.

### Validation
Checks for required fields and ensures numeric values (such as wages) are valid and positive.

### Summary Generation
Sends extracted fields and validation issues to Claude to produce a concise, professional summary suitable for underwriting review.

## Why This Project Matters

Mortgage teams spend significant time manually reviewing income documents. This pipeline shows how AI can automate the first pass by:

- Extracting structured data
- Identifying missing or inconsistent values
- Generating a clear summary for underwriting

The architecture demonstrates practical AI engineering skills: modular design, LLM integration, error‑tolerant validation, and clean orchestration.