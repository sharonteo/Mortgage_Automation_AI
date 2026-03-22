from src.mortgage_ai.extraction import extract_fields
from src.mortgage_ai.ingestion import load_text_document

def test_extract_bank_statement_transactions():
    text = load_text_document("data/samples/sample_bank_statement.txt")
    fields = extract_fields(text)

    assert "transactions" in fields
    assert len(fields["transactions"]) >= 1
