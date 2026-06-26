import json
import requests



API_URL = "http://127.0.0.1:8000/analyze-ticket"



# Load official test cases

with open(
    "sample_data/test_cases.json",
    "r",
    encoding="utf-8"
) as file:

    data = json.load(file)



cases = data["cases"]



print(
    f"\nRunning {len(cases)} test cases...\n"
)



for case in cases:


    ticket = case["input"]


    response = requests.post(

        API_URL,

        json=ticket

    )


    print("=" * 60)


    print(
        "Ticket ID:",
        ticket["ticket_id"]
    )


    if response.status_code == 200:


        result = response.json()



        print(
            "Case Type:",
            result.get("case_type")
        )


        print(
            "Severity:",
            result.get("severity")
        )


        print(
            "Department:",
            result.get("department")
        )


        print(
            "Evidence:",
            result.get("evidence_verdict")
        )


        print(
            "Human Review:",
            result.get("human_review_required")
        )


        print(
            "Confidence:",
            result.get("confidence")
        )


    else:


        print(
            "ERROR:",
            response.text
        )



print("=" * 60)

print("\nTesting completed.")