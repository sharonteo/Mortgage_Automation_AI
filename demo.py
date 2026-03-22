import sys
sys.stdout.reconfigure(encoding='utf-8')

from src.mortgage_ai.ingestion import load_text_document
from src.mortgage_ai.extraction import extract_fields
from src.mortgage_ai.validation import validate_fields
from src.mortgage_ai.summarization import generate_summary


def main():
    # Require a file path
    if len(sys.argv) < 2:
        print("Usage: python demo.py <path_to_document>")
        return

    file_path = sys.argv[1]

    print(f"=== PROCESSING DOCUMENT: {file_path} ===\n")

    # Load text
    text = load_text_document(file_path)

    # Extract → Validate
    fields = extract_fields(text)
    issues = validate_fields(fields)

    # Show extracted fields
    print("=== EXTRACTED FIELDS ===")
    print(fields)
    print()

    # Show validation results
    print("=== VALIDATION ===")
    if issues:
        for issue in issues:
            print(f"- {issue}")
    else:
        print("No validation issues found.")
    print()

    # Generate summary  ← THIS WAS MISSING
    summary = generate_summary(fields, issues)

    # Save summary to file
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(summary)

    # Print summary
    print("=== SUMMARY ===")
    print(summary)
    print()


if __name__ == "__main__":
    main()