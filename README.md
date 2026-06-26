# QueueStorm Investigator

AI-powered customer complaint investigation copilot.

This service receives one customer complaint with a short transaction history and returns a structured JSON response that helps support agents classify, route, and understand the case.

The system is designed as an internal support assistant, not an autonomous financial decision maker.

---

## Features

- Customer complaint classification
- Transaction evidence matching
- Department routing
- Risk severity detection
- Human review escalation
- Safe customer response generation
- Synthetic data testing support

---

## Architecture

```
Customer Complaint
        |
        v
     FastAPI
        |
        v
   Analyzer Pipeline
        |
        |
  -------------------
  |                 |
Rules Engine   Transaction Check
  |                 |
  -------------------
        |
        v
 Local AI Reasoning Layer
        |
        v
 Safety Validation
        |
        v
 Structured JSON Response
```

---

## Project Structure

```
queuestorm-investigator

│
├── app
│   |
│   ├── main.py
│   ├── schemas.py
│   ├── analyzer.py
│   ├── rules.py
│   ├── ai_model.py
│   └── safety.py
│
├── sample_data
│   └── test_cases.json
│
├── test_runner.py
│
└── README.md
```

---

# API Endpoints

## Health Check

### GET

```
/health
```

Response:

```json
{
  "status": "ok"
}
```

---

## Analyze Complaint

### POST

```
/analyze-ticket
```

Example Request:

```json
{
  "ticket_id": "TKT-001",
  "complaint": "I sent 5000 taka to wrong number",
  "transaction_history": [
    {
      "transaction_id": "TXN-1001",
      "timestamp": "2026-06-26T10:00:00Z",
      "type": "transfer",
      "amount": 5000,
      "counterparty": "01700000000",
      "status": "completed"
    }
  ]
}
```

---

Example Response:

```json
{
  "ticket_id": "TKT-001",
  "case_type": "wrong_transfer",
  "severity": "high",
  "department": "dispute_resolution",
  "evidence_verdict": "consistent",
  "human_review_required": true
}
```

---

# Safety Rules

The system:

- Never requests OTP
- Never requests PIN/password
- Never confirms unauthorized refunds
- Never makes final financial decisions
- Escalates risky cases for human review

---

# Case Classification

Supported cases:

- wrong_transfer
- payment_failed
- duplicate_payment
- refund_request
- phishing_or_social_engineering
- other

---

# Running the Project

Install dependencies:

```bash
pip install fastapi uvicorn requests
```

Run server:

```bash
python -m uvicorn app.main:app --reload
```

Open Swagger:

```
http://127.0.0.1:8000/docs
```

---

# Running Tests

Start server first.

Then:

```bash
python test_runner.py
```

---

# Data Policy

All complaints and transaction histories used in this project are synthetic.

No real customer data or production payment integration is used.