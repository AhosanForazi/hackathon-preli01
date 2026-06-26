from pydantic import BaseModel, Field
from typing import List, Optional

class Transaction(BaseModel):
    transaction_id: str
    timestamp: str
    type: str
    amount: float
    counterparty: str
    status: str

class TicketRequest(BaseModel):
    ticket_id: str
    complaint: str
    language: Optional[str] = "en"
    channel: Optional[str] = "unknown"
    user_type: Optional[str] = "unknown"
    campaign_context: Optional[str] = None
    metadata: Optional[dict] = None
    transaction_history: List[Transaction] = Field(default_factory=list)

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
    confidence: Optional[float] = 0.0
    reason_codes: Optional[List[str]] = []