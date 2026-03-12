def generate_underwriter_summary(fields: dict, validation: dict) -> str:
    """
    Generates a concise underwriter-style summary based on extracted fields
    and validation results.
    """
    name = fields.get("borrower_name", "Unknown borrower")
    income = fields.get("income")
    employer = fields.get("employer")
    dti = validation.get("computed", {}).get("dti")
    flags = validation.get("flags", [])

    lines = []
    lines.append(f"Borrower: {name}")
    lines.append(f"Employer: {employer}")
    lines.append(f"Reported annual income: {income}")

    if dti is not None:
        lines.append(f"Estimated DTI: {dti:.2f}")

    if flags:
        lines.append("Flags:")
        for f in flags:
            if f == "high_dti":
                lines.append("- DTI exceeds guideline threshold.")
            if f == "low_income":
                lines.append("- Income below minimum guideline.")
    else:
        lines.append("No guideline issues detected based on available fields.")

    return "\n".join(lines)