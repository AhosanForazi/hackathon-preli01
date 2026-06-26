from fastapi import FastAPI

from .schemas import (
    TicketRequest,
    TicketResponse
)

from .analyzer import analyze_ticket



app = FastAPI(

    title="QueueStorm Investigator",

    description=(
        "AI-powered customer complaint "
        "classification and routing copilot"
    ),

    version="1.0.0"

)



# -----------------------------
# Health Check
# -----------------------------

@app.get("/health")
def health():


    return {

        "status": "ok",

        "service":
            "QueueStorm Investigator",

        "version":
            "1.0.0"

    }



# -----------------------------
# Analyze Ticket
# -----------------------------

@app.post(
    "/analyze-ticket",
    response_model=TicketResponse
)
def analyze(

    ticket: TicketRequest

):

    return analyze_ticket(
        ticket
    )