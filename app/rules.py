import re


def extract_amount(text):

    numbers = re.findall(r"\d+", text)

    if numbers:
        return float(numbers[0])

    return None



def detect_case_type(text):

    text = text.lower()


    # Fraud / OTP
    if any(word in text for word in [
        "otp",
        "pin",
        "password",
        "credential",
        "called me",
        "চাইছে",
        "দিতে বলছে",
        "ওটিপি",
        "পিন"
    ]):
        return "phishing_or_social_engineering"



    # Wrong transfer
    if any(word in text for word in [
        "wrong",
        "mistake",
        "wrong number",
        "vul number",
        "ভুল নাম্বার",
        "ভুল নম্বরে",
        "ভুল করে",
        "vul kore"
    ]):
        return "wrong_transfer"



    # Payment failed
    if any(word in text for word in [
        "failed",
        "failure",
        "not completed",
        "kaj kore nai",
        "হয়নি",
        "ব্যর্থ",
        "fail"
    ]):
        return "payment_failed"



    # Duplicate payment
    if any(word in text for word in [
        "twice",
        "duplicate",
        "double",
        "two times",
        "দুইবার",
        "ডাবল",
        "duibar"
    ]):
        return "duplicate_payment"



    # Refund
    if any(word in text for word in [
        "refund",
        "return money",
        "ফেরত",
        "refund chai",
        "টাকা ফেরত"
    ]):
        return "refund_request"



    return "other"


def get_department(case_type):

    mapping = {

        "wrong_transfer":
        "dispute_resolution",

        "payment_failed":
        "payments_ops",

        "duplicate_payment":
        "payments_ops",

        "refund_request":
        "customer_support",

        "phishing_or_social_engineering":
        "fraud_risk",

        "other":
        "customer_support"

    }


    return mapping.get(
        case_type,
        "customer_support"
    )