# QueueStorm Investigator

AI-powered customer complaint investigation copilot.

QueueStorm Investigator is an internal support assistant that receives a customer complaint with recent transaction history and returns a structured JSON response for support agents.

The system classifies complaints, routes them to the correct department, evaluates transaction evidence, explains the case, and decides whether human review is required.

> This system is a support copilot, not an autonomous financial decision maker.

---

# Features

## Complaint Classification

Supports:

- Wrong transfer
- Payment failed
- Duplicate payment
- Refund request
- Phishing / social engineering
- Merchant settlement delay
- Agent cash-in issue
- Other cases


## Transaction Evidence Analysis

The system checks transaction history and returns:

- consistent
- inconsistent
- insufficient_data


## Risk Detection

Automatically identifies:

- High risk cases
- Critical fraud cases
- Cases requiring human review


## Safety Controls

The system:

- Never asks for OTP
- Never asks for PIN/password
- Never confirms unauthorized refunds
- Escalates ambiguous and risky cases


---

# Project Architecture

```
Customer Complaint
        |
        v
     FastAPI API
        |
        v
 Analyzer Pipeline
        |
        |
 -----------------------
 |                     |
Rules Engine     Transaction Check
 |                     |
 -----------------------
        |
        v
 AI Reasoning Layer
        |
        v
 Safety Validation
        |
        v
 Structured JSON Response
```


---

# Project Structure

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
├── requirements.txt
│
└── README.md
```


---

# Installation

Install dependencies:

```bash
pip install -r requirements.txt
```


---

# Running the API

Start server:

```bash
python -m uvicorn app.main:app --reload
```


API will run at:

```
http://127.0.0.1:8000
```


Swagger Documentation:

```
http://127.0.0.1:8000/docs
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
  "status": "ok",
  "service": "QueueStorm Investigator"
}
```


---


## Analyze Customer Complaint

### POST

```
/analyze-ticket
```


Example Request:

```json
{
  "ticket_id": "TKT-001",
  "complaint": "I sent 5000 taka to wrong number",
  "language": "en",
  "channel": "app",
  "user_type": "customer",
  "transaction_history": [
    {
      "transaction_id": "TXN-1001",
      "timestamp": "2026-06-26T10:00:00Z",
      "type": "transfer",
      "amount": 5000,
      "counterparty": "+8801700000000",
      "status": "completed"
    }
  ]
}
```


Response:

```json
{
  "ticket_id": "TKT-001",
  "case_type": "wrong_transfer",
  "severity": "high",
  "department": "dispute_resolution",
  "evidence_verdict": "consistent",
  "human_review_required": true,
  "confidence": 0.90
}
```


---

# Testing

Start the API server first:

```bash
python -m uvicorn app.main:app --reload
```


Run synthetic test cases:

```bash
python test_runner.py
```


The test runner evaluates multiple complaint scenarios using synthetic data.


---

# Sample Cases Covered

Examples:

- Wrong transfer
- Phishing attempt
- Failed payment
- Duplicate payment
- Refund request
- Merchant settlement delay
- Agent cash-in issue
- Ambiguous complaints


---

# Data Policy

All complaints and transaction histories used in this project are synthetic.

No real customer data is used.

No real payment system integration exists.

---

# Technology Stack

- Python
- FastAPI
- Pydantic
- Rule-based NLP
- AI reasoning layer
- JSON based synthetic evaluation


---

# Future Improvements

Possible improvements:

- LLM integration
- Database storage
- Authentication
- Monitoring dashboard
- Advanced fraud detection model