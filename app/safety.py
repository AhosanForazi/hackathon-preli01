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


    customer_reply = response.get(
        "customer_reply",
        ""
    ).lower()



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

    if response.get(
        "case_type"
    ) == "phishing_or_social_engineering":


        response["human_review_required"] = True


        response["severity"] = "critical"



    return response





def generate_safe_reply(
        case_type,
        transaction_id
):


    replies = {


        "wrong_transfer":
            (
                "We have received your transfer concern. "
                "Our support team will review the "
                "transaction details."
            ),



        "payment_failed":
            (
                "We received your payment issue. "
                "The transaction status will be reviewed "
                "by our support team."
            ),



        "duplicate_payment":
            (
                "We received your duplicate payment concern. "
                "Our team will investigate the transaction."
            ),



        "phishing_or_social_engineering":
            (
                "For your security, do not share OTP, "
                "PIN, password, or credentials. "
                "Our fraud team will review this case."
            ),



        "refund_request":
            (
                "Your refund request has been received. "
                "Our team will review eligibility "
                "according to policy."
            )

    }



    return replies.get(

        case_type,

        "Your request has been received. "
        "Our support team will review the details."

    )