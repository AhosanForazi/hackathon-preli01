import json
import requests



API_URL = "http://127.0.0.1:8000/analyze-ticket"



# Load test cases

with open(
    "sample_data/test_cases.json",
    "r",
    encoding="utf-8"
) as file:

    test_cases = json.load(file)



print(
    f"\nRunning {len(test_cases)} test cases...\n"
)



for case in test_cases:


    response = requests.post(
        API_URL,
        json=case
    )


    print("=" * 50)


    print(
        "Ticket:",
        case["ticket_id"]
    )


    if response.status_code == 200:

        result = response.json()


        print(
            "Case Type:",
            result["case_type"]
        )


        print(
            "Severity:",
            result["severity"]
        )


        print(
            "Department:",
            result["department"]
        )


        print(
            "Evidence:",
            result["evidence_verdict"]
        )


        print(
            "Human Review:",
            result["human_review_required"]
        )


    else:

        print(
            "Error:",
            response.text
        )


print("=" * 50)

print(
    "\nTesting completed."
)