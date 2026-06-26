import re

# -----------------------------
# Extract amount from complaint
# -----------------------------
def extract_amount(text):
    matches = re.findall(r"\d+", text)
    if matches:
        return float(matches[0])
    return None

# -----------------------------
# Detect complaint category
# -----------------------------
def detect_case_type(text):
    text = text.lower()

    # Phishing / Social Engineering
    if any(word in text for word in [
        "otp", "pin", "password", "credential", "called me", 
        "share code", "verify account", "ওটিপি", "পিন", "পাসওয়ার্ড"
    ]):
        return "phishing_or_social_engineering"

    # Wrong Transfer
    if any(word in text for word in [
        "wrong number", "wrong person", "wrong recipient", "mistake",
        "mistakenly", "reverse", "vul number", "ভুল নাম্বার", "ভুল নম্বরে", "ভুল করে"
    ]):
        return "wrong_transfer"

    # Duplicate Payment
    if any(word in text for word in [
        "twice", "double", "duplicate", "charged twice", "দুইবার", "ডাবল"
    ]):
        return "duplicate_payment"

    # Payment Failed
    if any(word in text for word in [
        "failed", "failure", "not completed", "deducted", "balance deducted", 
        "ব্যর্থ", "কেটে নিয়েছে"
    ]):
        return "payment_failed"

    # Refund
    if any(word in text for word in [
        "refund", "money back", "return my money", "টাকা ফেরত", "ফেরত"
    ]):
        return "refund_request"

    # Agent Cash In
    if any(word in text for word in [
        "cash in", "agent", "এজেন্ট", "ক্যাশ ইন", "balance not updated"
    ]):
        return "agent_cash_in_issue"

    # Merchant Settlement
    if any(word in text for word in [
        "merchant", "settlement", "sales", "merchant portal"
    ]):
        return "merchant_settlement_delay"

    return "other"

# -----------------------------
# Department Routing
# -----------------------------
def get_department(case_type):
    mapping = {
        "wrong_transfer": "dispute_resolution",
        "payment_failed": "payments_ops",
        "refund_request": "customer_support",
        "duplicate_payment": "payments_ops",
        "phishing_or_social_engineering": "fraud_risk",
        "merchant_settlement_delay": "merchant_operations",
        "agent_cash_in_issue": "agent_operations",
        "other": "customer_support"
    }
    return mapping.get(case_type, "customer_support")