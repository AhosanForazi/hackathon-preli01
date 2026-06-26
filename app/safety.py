# Safety layer for AI generated responses

def validate_response(response):
    # -----------------------------
    # Prevent unsafe refund confirmation
    # -----------------------------
    unsafe_refund_words = [
        "refund approved",
        "refund confirmed",
        "money has been refunded",
        "reversal completed"
    ]

    customer_reply = response.get("customer_reply", "").lower()

    for word in unsafe_refund_words:
        if word in customer_reply:
            response["customer_reply"] = (
                "Your request has been received. "
                "Our support team will review the "
                "transaction details and provide an update."
            )

    # -----------------------------
    # Prevent credential requests
    # -----------------------------
    blocked_words = [
        "send otp",
        "share otp",
        "provide pin",
        "give password",
        "share credential"
    ]

    for word in blocked_words:
        if word in customer_reply:
            response["customer_reply"] = (
                "For your security, "
                "please do not share OTP, PIN, "
                "password, or any sensitive credentials."
            )

    # -----------------------------
    # Force human review for high risk
    # -----------------------------
    if response.get("case_type") == "phishing_or_social_engineering":
        response["human_review_required"] = True
        response["severity"] = "critical"

    return response