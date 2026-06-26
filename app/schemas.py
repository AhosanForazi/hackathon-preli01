from pydantic import BaseModel, Field
from typing import List, Optional



# -----------------------------
# Transaction Schema
# -----------------------------

class Transaction(BaseModel):

    transaction_id: str

    timestamp: str

    type: str

    amount: float

    counterparty: str

    status: str



# -----------------------------
# Ticket Request Schema
# -----------------------------

class TicketRequest(BaseModel):

    ticket_id: str

    complaint: str

    language: Optional[str] = "en"

    channel: Optional[str] = "unknown"

    user_type: Optional[str] = "unknown"

    campaign_context: Optional[str] = None

    transaction_history: List[Transaction] = Field(
        default_factory=list
    )



# -----------------------------
# Ticket Response Schema
# -----------------------------

class TicketResponse(BaseModel):

    ticket_id: str

    relevant_transaction_id: Optional[str] = None

    evidence_verdict: str

    case_type: str

    severity: str

    department: str


    agent_summary: str

    recommended_next_action: str


    customer_reply: str


    human_review_required: bool


    confidence: float


    reason_codes: List[str]