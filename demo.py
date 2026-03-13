from src.mortgage_ai.pipeline import run_pipeline

if __name__ == "__main__":
    fields, validation, summary = run_pipeline("data/samples/sample_w2.txt")

    print("\n=== EXTRACTED FIELDS ===")
    for k, v in fields.items():
        print(f"{k}: {v}")

    print("\n=== VALIDATION ===")
    for issue in validation:
        print(f"- {issue}")

    print("\n=== SUMMARY ===")
    print(summary)