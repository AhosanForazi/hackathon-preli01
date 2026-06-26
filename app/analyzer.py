from .rules import (
    extract_amount,
    detect_case_type,
    get_department
)

from .ai_model import ask_ai

from .safety import validate_response



def analyze_ticket(ticket):


    # -----------------------------
    # Step 1: Classification
    # -----------------------------

    case_type = detect_case_type(
        ticket.complaint
    )



    # -----------------------------
    # Step 2: Transaction Evidence
    # -----------------------------

    transaction_id = None

    verdict = "insufficient_data"


    amount = extract_amount(
        ticket.complaint
    )



    if ticket.transaction_history:


        verdict = "inconsistent"



        for txn in ticket.transaction_history:


            if amount and txn.amount == amount:


                transaction_id = (
                    txn.transaction_id
                )


                verdict = "consistent"

                break




    # -----------------------------
    # Step 3: Risk Assessment
    # -----------------------------

    severity = "medium"

    human_review = False



    if case_type in [

        "wrong_transfer",

        "duplicate_payment",

        "refund_request"

    ]:


        severity = "high"

        human_review = True




    if case_type == "phishing_or_social_engineering":


        severity = "critical"

        human_review = True




    if case_type in [

        "merchant_settlement_delay",

        "agent_cash_in_issue"

    ]:


        severity = "high"

        human_review = True





    # -----------------------------
    # Step 4: Build AI Context
    # -----------------------------


    context = {


        "ticket_id":

            ticket.ticket_id,


        "complaint":

            ticket.complaint,


        "language":

            ticket.language,


        "channel":

            ticket.channel,


        "user_type":

            ticket.user_type,


        "case_type":

            case_type,


        "severity":

            severity,


        "department":

            get_department(case_type),



        "relevant_transaction_id":

            transaction_id,



        "evidence_verdict":

            verdict,



        "transaction_history":

            [

                txn.model_dump()

                for txn

                in ticket.transaction_history

            ],



        "human_review_required":

            human_review

    }




    # -----------------------------
    # Step 5: AI Explanation
    # -----------------------------


    result = ask_ai(
        context
    )




    # -----------------------------
    # Step 6: Safety Layer
    # -----------------------------


    result = validate_response(
        result
    )




    # -----------------------------
    # Step 7: Ensure Fields
    # -----------------------------


    result["ticket_id"] = (

        ticket.ticket_id

    )


    result["case_type"] = (

        result.get(

            "case_type",

            case_type

        )

    )


    result["severity"] = (

        result.get(

            "severity",

            severity

        )

    )


    result["department"] = (

        result.get(

            "department",

            get_department(case_type)

        )

    )


    result["evidence_verdict"] = (

        verdict

    )


    result["human_review_required"] = (

        human_review

    )


    result.setdefault(

        "reason_codes",

        [

            case_type,

            verdict

        ]

    )


    result.setdefault(

        "confidence",

        0.85

    )



    return result