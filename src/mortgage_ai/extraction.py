from typing import Dict, Any
import json
import os
from anthropic import Anthropic


# ---------------------------------------------------------
# Document Type Detection
# ---------------------------------------------------------

def detect_document_type(text: str) -> str:
    """
    Very lightweight heuristic-based document classifier.
    Determines whether the document is a W-2, paystub, or bank statement.
    """
    t = text.lower()

    if "w-2" in t or "wage and tax statement" in t:
        return "w2"

    if "gross pay" in t or "net pay" in t or "ytd" in t or "pay period" in t:
        return "paystub"

    if "beginning balance" in t or "ending balance" in t or "withdrawal" in t or "deposit" in t:
        return "bank_statement"

    return "unknown"


# ---------------------------------------------------------
# JSON Cleaning
# ---------------------------------------------------------

def clean_json(raw: str) -> str:
    """
    Removes markdown code fences (```json ... ```).
    Claude sometimes returns fenced JSON even when instructed not to.
    """
    raw = raw.strip()

    if raw.startswith("```"):
        raw = raw.split("```")[-1].strip()

    if raw.endswith("```"):
        raw = raw.split("```")[0].strip()

    return raw


# ---------------------------------------------------------
# Main Extraction Function
# ---------------------------------------------------------

def extract_fields(text) -> Dict[str, Any]:
    """
    Extract structured fields from a mortgage-related document using Claude.
    Automatically detects document type and applies the correct schema.
    """

    # Allow passing either a Document object or a raw string
    if hasattr(text, "text"):
        text = text.text

    client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    doc_type = detect_document_type(text)

    # -----------------------------
    # Select schema based on type
    # -----------------------------
    if doc_type == "w2":
        schema = """
Extract the following fields:
- employee_name
- employer
- wages (numeric)
- tax_year
"""
    elif doc_type == "paystub":
        schema = """
Extract the following fields:
- employee_name
- employer
- wages (numeric)
- gross_pay (numeric)
- net_pay (numeric)
- tax_year
"""
    elif doc_type == "bank_statement":
        schema = """
Extract the following fields:
- transactions: a list of objects with:
    - date
    - description
    - amount (numeric, positive for deposits, negative for withdrawals)
"""
    else:
        return {"error": "Unknown document type"}

    prompt = f"""
You are an expert mortgage document analyst.
Extract structured fields from the document below.

Document:
{text}

{schema}

Rules:
- Return ONLY valid JSON.
- No markdown.
- No code fences.
- If a field is missing, set it to null.
"""

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}],
    )

    raw = response.content[0].text
    cleaned = clean_json(raw)

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        return {
            "error": "Invalid JSON returned by model",
            "raw_output": raw
        }