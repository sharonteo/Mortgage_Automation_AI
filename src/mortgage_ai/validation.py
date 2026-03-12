import yaml
import os

# Path to the underwriting rules file
RULES_PATH = os.path.join(os.path.dirname(__file__), "rules", "underwriting_rules.yaml")

def load_rules(path: str = RULES_PATH) -> dict:
    """
    Loads underwriting rules from a YAML file.
    """
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def validate_income_fields(fields: dict, rules: dict) -> dict:
    """
    Applies underwriting rules to extracted income fields.
    Computes DTI and flags issues like high DTI or low income.
    """
    results = {"flags": [], "computed": {}}

    income = fields.get("income")
    monthly_debt = fields.get("monthly_debt")

    # Compute DTI if both values exist
    if income and monthly_debt:
        annual_debt = monthly_debt * 12
        dti = annual_debt / income
        results["computed"]["dti"] = dti

        if dti > rules["dti_max"]:
            results["flags"].append("high_dti")

    # Check minimum income guideline
    if income and income < rules["min_income"]:
        results["flags"].append("low_income")

    return results