from anthropic import Anthropic
import os

def detect_summary_type(fields):
    if "transactions" in fields:
        return "bank_statement"
    if "gross_pay" in fields or "net_pay" in fields:
        return "paystub"
    if "wages" in fields:
        return "w2"
    return "unknown"


def generate_summary(fields, issues):
    client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    doc_type = detect_summary_type(fields)

    # Shared instruction to prevent dangling sections
    base_instruction = """
Write a clean, professional underwriting summary.

CRITICAL RULES:
- All sentences must be complete.
- The summary must end cleanly with a full concluding sentence.
- Do NOT leave trailing or unfinished thoughts (e.g., “assuming this”, “as the purpose is”).
- Do NOT speculate beyond the provided data.
- Do NOT start a sentence you cannot finish.
- Do NOT include a 'Recommendation' section unless you have a meaningful recommendation.
- Do NOT output empty headers or placeholders.

STRUCTURE:
- Keep the summary concise (6–10 sentences maximum).
- End with a clear, final concluding sentence.

"""

    if doc_type == "w2":
        summary_prompt = f"""
{base_instruction}

Document type: W-2

Extracted fields:
{fields}

Validation issues:
{issues}

Write a concise underwriting summary focusing on:
- employee/employer
- wages
- income stability
- any concerns
"""
    elif doc_type == "paystub":
        summary_prompt = f"""
{base_instruction}

Document type: Paystub

Extracted fields:
{fields}

Validation issues:
{issues}

Write a concise underwriting summary focusing on:
- employer
- gross pay
- net pay
- deductions
- income stability
"""
    elif doc_type == "bank_statement":
        summary_prompt = f"""
{base_instruction}

Document type: Bank Statement

Extracted fields:
{fields}

Validation issues:
{issues}

Write a concise underwriting summary focusing on:
- deposits
- withdrawals
- transaction patterns
- income consistency
"""
    else:
        summary_prompt = f"""
{base_instruction}

Document type: Unknown

Extracted fields:
{fields}

Validation issues:
{issues}

Explain why underwriting cannot proceed.
"""

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=300,
        messages=[{"role": "user", "content": summary_prompt}],
    )

    return response.content[0].text