import random


def ask_ai(data):

    case_type = data.get(
        "case_type",
        "other"
    )

    severity = data.get(
        "severity",
        "medium"
    )

    department = data.get(
        "department",
        "customer_support"
    )

    transaction_id = data.get(
        "relevant_transaction_id"
    )


    summary_map = {

        "wrong_transfer":
            "Customer reported a transfer sent to an unintended recipient.",

        "payment_failed":
            "Customer reported a failed payment attempt.",

        "duplicate_payment":
            "Customer reported a possible duplicate transaction.",

        "refund_request":
            "Customer requested information about a refund.",

        "phishing_or_social_engineering":
            "Customer may be exposed to a potential fraud attempt.",

        "other":
            "Customer complaint requires further investigation."
    }


    action_map = {

        "wrong_transfer":
            "Verify transfer details and review dispute process.",

        "payment_failed":
            "Check transaction status and payment logs.",

        "duplicate_payment":
            "Verify duplicate transaction records.",

        "refund_request":
            "Review refund eligibility according to policy.",

        "phishing_or_social_engineering":
            "Escalate immediately to fraud risk team.",

        "other":
            "Collect additional information from customer."
    }


    reply_map = {

        "wrong_transfer":
            "We have received your transfer concern. Our support team will review the transaction details.",

        "payment_failed":
            "We have received your payment issue. Our team will verify the transaction status.",

        "duplicate_payment":
            "We have noted your duplicate payment concern. Our team will investigate the transaction records.",

        "refund_request":
            "We have received your refund request. Eligibility will be reviewed by our support team.",

        "phishing_or_social_engineering":
            "Please do not share OTP, PIN, or password with anyone. Our security team will review this case.",

        "other":
            "Your request has been received and our support team will review it."
    }


    return {

        "ticket_id":
            data.get("ticket_id"),

        "relevant_transaction_id":
            transaction_id,

        "evidence_verdict":
            data.get("evidence_verdict"),

        "case_type":
            case_type,

        "severity":
            severity,

        "department":
            department,

        "agent_summary":
            summary_map.get(case_type),

        "recommended_next_action":
            action_map.get(case_type),

        "customer_reply":
            reply_map.get(case_type),

        "human_review_required":
            data.get(
                "human_review_required",
                False
            ),

        "confidence":
            round(
                random.uniform(
                    0.75,
                    0.95
                ),
                2
            ),

        "reason_codes":[
            case_type,
            data.get("evidence_verdict")
        ]
    }