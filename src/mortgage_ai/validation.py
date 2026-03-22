def validate_fields(fields):
    issues = []

    # Detect document type
    if "transactions" in fields:
        doc_type = "bank_statement"
    elif "gross_pay" in fields or "net_pay" in fields:
        doc_type = "paystub"
    elif "wages" in fields:
        doc_type = "w2"
    else:
        doc_type = "unknown"

    # Required fields by document type
    required_by_type = {
        "w2": ["employee_name", "employer", "wages", "tax_year"],
        "paystub": ["employee_name", "employer", "gross_pay", "net_pay", "tax_year"],
        "bank_statement": ["transactions"],
        "unknown": []
    }

    required_fields = required_by_type.get(doc_type, [])

    # Check for missing required fields
    for field in required_fields:
        if field not in fields or fields[field] in (None, "", []):
            issues.append(f"Missing required field: {field}")

    # Additional validation rules (optional)
    if doc_type == "bank_statement":
        tx = fields.get("transactions", [])
        if not isinstance(tx, list) or len(tx) == 0:
            issues.append("Bank statement contains no transactions.")
        else:
            # Example: flag negative deposits
            for t in tx:
                if t.get("description", "").lower().startswith("deposit") and t.get("amount", 0) < 0:
                    issues.append("Deposit transaction has negative amount.")

    return issues