from src.mortgage_ai.extraction import extract_fields
from src.mortgage_ai.ingestion import load_text_document

def test_extract_paystub_fields():
    text = load_text_document("data/samples/sample_paystub.txt")
    fields = extract_fields(text)

    assert fields.get("employer") == "Acme Manufacturing Inc."
    assert fields.get("gross_pay") is not None
    assert fields.get("net_pay") is not None
