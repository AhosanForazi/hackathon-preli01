

def ask_ai(context):


    case_type = context.get(
        "case_type",
        "other"
    )


    severity = context.get(
        "severity",
        "medium"
    )


    department = context.get(
        "department",
        "customer_support"
    )


    evidence = context.get(
        "evidence_verdict",
        "insufficient_data"
    )


    transaction_id = context.get(
        "relevant_transaction_id"
    )



    # -----------------------------
    # Generate agent summary
    # -----------------------------


    summaries = {


        "wrong_transfer":

            "Customer reported a transfer sent to an unintended recipient.",



        "payment_failed":

            "Customer reported a failed payment transaction.",



        "duplicate_payment":

            "Customer reported a possible duplicate charge.",



        "phishing_or_social_engineering":

            "Customer may have experienced a social engineering attempt.",



        "refund_request":

            "Customer requested a refund review.",



        "merchant_settlement_delay":

            "Merchant reported a settlement related issue.",



        "agent_cash_in_issue":

            "Agent reported a cash-in related issue."

    }



    agent_summary = summaries.get(

        case_type,

        "Customer complaint requires support investigation."

    )




    # -----------------------------
    # Recommended action
    # -----------------------------


    actions = {


        "wrong_transfer":

            "Verify transfer details and review dispute process.",



        "payment_failed":

            "Check payment status and transaction processing logs.",



        "duplicate_payment":

            "Review duplicate transaction records.",



        "phishing_or_social_engineering":

            "Escalate to fraud team and advise customer not to share credentials.",



        "refund_request":

            "Review refund eligibility according to policy.",



        "merchant_settlement_delay":

            "Review merchant settlement status.",



        "agent_cash_in_issue":

            "Verify agent transaction records."

    }



    next_action = actions.get(

        case_type,

        "Review transaction details according to policy."

    )




    # -----------------------------
    # Safe customer response
    # -----------------------------


    replies = {


        "wrong_transfer":

            "We have received your transfer concern. Our support team will review the transaction details.",



        "payment_failed":

            "We received your payment issue. Our team will review the transaction status.",



        "duplicate_payment":

            "We received your duplicate payment concern. Our team will investigate the transaction.",



        "phishing_or_social_engineering":

            "For your security, do not share OTP, PIN, password, or credentials. Our fraud team will review this case.",



        "refund_request":

            "Your refund request has been received. Our team will review it according to policy."

    }



    customer_reply = replies.get(

        case_type,

        "Your request has been received. Our support team will review the details."

    )





    return {


        "relevant_transaction_id":

            transaction_id,


        "evidence_verdict":

            evidence,


        "case_type":

            case_type,


        "severity":

            severity,


        "department":

            department,


        "agent_summary":

            agent_summary,


        "recommended_next_action":

            next_action,


        "customer_reply":

            customer_reply,


        "human_review_required":

            context.get(

                "human_review_required",

                False

            ),


        "confidence":

            0.90,


        "reason_codes":

            [

                case_type,

                evidence

            ]

    }