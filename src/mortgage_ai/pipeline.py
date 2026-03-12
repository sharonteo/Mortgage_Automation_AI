from .ingestion import Document
from .extraction import extract_income_fields
from .validation import load_rules, validate_income_fields
from .summarization import generate_underwriter_summary

def process_income_document(doc: Document) -> dict:
    """
    Runs the full mortgage income document pipeline:
    extraction -> validation -> summarization.
    """
    rules = load_rules()
    fields = extract_income_fields(doc)
    validation = validate_income_fields(fields, rules)
    summary = generate_underwriter_summary(fields, validation)

    return {
        "fields": fields,
        "validation": validation,
        "summary": summary,
    }