from src.mortgage_ai.ingestion import load_text_document
from src.mortgage_ai.pipeline import process_income_document

if __name__ == "__main__":
    # Load the sample W-2 style document
    doc = load_text_document("data/samples/sample_w2.txt")

    # Run the full pipeline
    result = process_income_document(doc)

    # Print results
    print("=== Extracted Fields ===")
    print(result["fields"])

    print("\n=== Validation Results ===")
    print(result["validation"])

    print("\n=== Underwriter Summary ===")
    print(result["summary"])