from typing import Dict, List
from anthropic import Anthropic
import os

def summarize_mortgage_profile(fields: Dict[str, str], issues: List[str]) -> str:
    """
    Ask Claude for a concise underwriter-style summary.
    """
    client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    prompt = f"""
You are an underwriter assistant. Given extracted W-2 style fields and validation issues,
produce a concise, professional summary of the borrower's income profile.

Extracted fields:
{fields}

Validation issues:
{issues}

Write 1–2 short paragraphs, plain text only.
"""

    resp = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=300,
        messages=[{"role": "user", "content": prompt}],
    )

    return resp.content[0].text