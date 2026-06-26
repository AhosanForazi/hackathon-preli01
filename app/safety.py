def generate_safe_reply(case_type, txn_id):


    if case_type == "phishing_or_social_engineering":

        return (
            "Please do not share OTP, PIN, or password with anyone. "
            "Our security team will review this case."
        )


    if case_type == "payment_failed":

        return (
            f"We have received your concern regarding {txn_id}. "
            "Our team will verify the transaction status."
        )


    if case_type == "duplicate_payment":

        return (
            f"We have received your duplicate payment concern regarding {txn_id}. "
            "Our team will investigate the transaction records."
        )


    if case_type == "wrong_transfer":

        return (
            f"We have received your transfer concern regarding {txn_id}. "
            "Our support team will review the transaction details."
        )


    return (
        f"We have received your request regarding {txn_id}. "
        "Our support team will review the case."
    )



# Safety layer for AI output

def validate_response(data):


    forbidden_words = [
        "otp",
        "pin",
        "password",
        "card number"
    ]


    reply = data.get(
        "customer_reply",
        ""
    ).lower()



    for word in forbidden_words:

        if word in reply:

            data["customer_reply"] = (
                "Please do not share sensitive credentials. "
                "Our support team will assist you through official channels."
            )

            break



    # Never allow fake confirmation

    risky_words = [
        "refund completed",
        "money returned",
        "reversal completed"
    ]


    for word in risky_words:

        if word in reply:

            data["customer_reply"] = (
                "Your request has been received. "
                "Our team will review the case and update you."
            )

            break



    return data