from typing import Dict, List, Any


def validate_extracted_fields(fields: Dict[str, Any]) -> List[str]:
    """
    Validates extracted mortgage fields from Claude or regex extraction.
    Handles mixed types (string, float, int, None).
    Returns a list of validation issues.
    """

    issues: List[str] = []

    # Required fields for a basic W-2 profile
    required_fields = ["employee_name", "employer", "wages", "tax_year"]

    for key in required_fields:
        if key not in fields or fields[key] in (None, "", []):
            issues.append(f"Missing required field: {key}")

    # Validate wages
    wages_raw = fields.get("wages")
    wages_val = None

    if wages_raw is not None:
        try:
            # If Claude returned a number
            if isinstance(wages_raw, (int, float)):
                wages_val = float(wages_raw)
            else:
                # If Claude returned a string
                wages_str = str(wages_raw).replace(",", "").replace("$", "")
                wages_val = float(wages_str)
        except Exception:
            issues.append("Wages is not a valid number.")

        if wages_val is not None and wages_val <= 0:
            issues.append("Wages must be a positive value.")

    # Validate tax year
    tax_year_raw = fields.get("tax_year")
    if tax_year_raw is not None:
        try:
            tax_year_val = int(str(tax_year_raw).strip())
            if tax_year_val < 1900 or tax_year_val > 2100:
                issues.append("Tax year appears invalid.")
        except Exception:
            issues.append("Tax year is not a valid integer.")

    return issues