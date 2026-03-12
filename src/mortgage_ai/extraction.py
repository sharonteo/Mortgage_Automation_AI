import re
from .ingestion import Document

def extract_income_fields(doc: Document) -> dict:
    """
    Extracts key fields from an income-related document (e.g., W-2, paystub).
    This simulates an AI/LLM extractor using simple regex patterns.
    """
    text = doc.content

    name_match = re.search(r"Name:\s*(.+)", text)
    employer_match = re.search(r"Employer:\s*(.+)", text)
    income_match = re.search(r"Annual Income:\s*([\d,]+)", text)
    debt_match = re.search(r"Monthly Debt:\s*([\d,]+)", text)

    def to_number(match):
        if not match:
            return None
        return float(match.group(1).replace(",", ""))

    return {
        "borrower_name": name_match.group(1).strip() if name_match else None,
        "employer": employer_match.group(1).strip() if employer_match else None,
        "income": to_number(income_match),
        "monthly_debt": to_number(debt_match),
    }