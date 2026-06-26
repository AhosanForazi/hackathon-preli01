from .rules import (
    extract_amount,
    detect_case_type,
    get_department
)

from .ai_model import ask_ai

from .safety import validate_response



def analyze_ticket(ticket):

    # -----------------------------
    # Step 1: Rule based analysis
    # -----------------------------

    case_type = detect_case_type(
        ticket.complaint
    )


    transaction_id = None

    verdict = "insufficient_data"


    amount = extract_amount(
        ticket.complaint
    )


    # Transaction evidence checking

    if ticket.transaction_history:

        verdict = "inconsistent"


        for txn in ticket.transaction_history:


            if amount and txn.amount == amount:

                transaction_id = txn.transaction_id

                verdict = "consistent"

                break



    # -----------------------------
    # Step 2: Risk calculation
    # -----------------------------

    severity = "medium"

    human_review = False


    if case_type in [
        "wrong_transfer",
        "duplicate_payment"
    ]:

        severity = "high"

        human_review = True



    if case_type == "phishing_or_social_engineering":

        severity = "critical"

        human_review = True



    # -----------------------------
    # Step 3: Prepare AI context
    # -----------------------------

    base_result = {

        "ticket_id": ticket.ticket_id,

        "complaint": ticket.complaint,

        "language": ticket.language,

        "channel": ticket.channel,

        "user_type": ticket.user_type,


        "relevant_transaction_id":
            transaction_id,


        "evidence_verdict":
            verdict,


        "case_type":
            case_type,


        "severity":
            severity,


        "department":
            get_department(case_type),


        "transaction_history":
            [
                txn.model_dump()
                for txn in ticket.transaction_history
            ],


        "human_review_required":
            human_review
    }



    # -----------------------------
    # Step 4: AI reasoning
    # -----------------------------

    ai_result = ask_ai(
        base_result
    )



    # -----------------------------
    # Step 5: Safety validation
    # -----------------------------

    ai_result = validate_response(
        ai_result
    )



    # -----------------------------
    # Step 6: Ensure required field
    # -----------------------------

    ai_result["ticket_id"] = (
        ticket.ticket_id
    )


    return ai_result