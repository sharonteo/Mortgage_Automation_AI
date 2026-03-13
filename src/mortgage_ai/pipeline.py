from .ingestion import load_text_document
from .extraction import extract_fields
from .validation import validate_extracted_fields
from .summarization import summarize_mortgage_profile


def run_pipeline(path: str):
    # 1) Load
    doc = load_text_document(path)

    # 2) Extract (Claude)
    fields = extract_fields(doc.text)

    # 3) Validate
    issues = validate_extracted_fields(fields)

    # 4) Summarize
    summary = summarize_mortgage_profile(fields, issues)

    return fields, issues, summary