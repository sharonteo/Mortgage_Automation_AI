from typing import Dict, Any
from anthropic import Anthropic
import os
import json


def extract_fields(text: str) -> Dict[str, Any]:
    """
    Uses Claude to extract structured fields from a mortgage-related document.
    Returns a dictionary with keys such as:
        - employee_name
        - employer
        - wages
        - tax_year

    Claude is instructed to ALWAYS return valid JSON.
    """

    client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    prompt = f"""
You are an expert mortgage document analyst. Extract key fields from the document
below and return ONLY valid JSON. Do not include explanations or commentary.

Document text:
{text}

Extract the following fields when possible:
- employee_name
- employer
- wages (numeric, no commas, no dollar sign)
- tax_year

Rules:
- If a field is missing, set its value to null.
- Do not infer values that are not explicitly stated.
- Return ONLY a JSON object. No markdown, no code fences.

Return format example:
{{
  "employee_name": "John Doe",
  "employer": "ACME Corp",
  "wages": 85000.00,
  "tax_year": 2024
}}
"""

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=300,
        messages=[{"role": "user", "content": prompt}],
    )

    raw = response.content[0].text.strip()

    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        data = {"error": "Invalid JSON returned by model", "raw_output": raw}

    return data