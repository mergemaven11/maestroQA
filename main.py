"""
main.py

Uploads tickets from a customer-provided CSV file into MaestroQA via their REST API.

Author: Tobias Scott
Date: 2025-10-07
"""

import csv
import requests
import os
from dotenv import load_dotenv
from typing import List, Dict, Any

load_dotenv()

API_URL = "https://app.maestroqa.com/api/v1/tickets"
API_TOKEN = os.getenv("MAESTRO_API_TOKEN")
# Check to make sure Token is loaded
print("Using API token:", API_TOKEN[:5] + "..." if API_TOKEN else "None")


HEADERS = {
    "apiToken": API_TOKEN,
    "Content-Type": "application/json"
}


def load_tickets_from_csv(file_path: str) -> List[Dict[str, Any]]:
    """Load and parse ticket data from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing ticket data.

    Returns:
        List[Dict[str, Any]]: A list of ticket dictionaries.
    """
    tickets = []
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            tickets.append(row)
    return tickets


def transform_ticket_for_api(raw: Dict[str, Any]) -> Dict[str, Any]:
    """Convert raw CSV data into MaestroQA ticket payload format.

    Args:
        raw (Dict[str, Any]): Raw ticket record from CSV.

    Returns:
        Dict[str, Any]: API-ready payload.
    """
    payload = {
        "ticket_id": raw["Support_Ticket_Id"],
        "type": "support_case",
        "subject": raw.get("ticket_category", "General Inquiry"),
        "agents": [raw["Agent ID"]],
        "status": "closed" if raw.get("Closed_Date") else "open",
        "body": raw.get("Body", ""),
        "attributes": {
            "Created_Date": raw.get("Created_Date"),
            "Closed_Date": raw.get("Closed_Date"),
            "Total_Resolution_Hours": raw.get("total_resolution_time_hours"),
            "First_Response_Hours": raw.get("first_response_time_hours"),
            "Agent_Responses": raw.get("agent_responses"),
            "Customer_Responses": raw.get("customer_responses"),
            "Csat_Score": raw.get("Csat_Score"),
            "Csat_Reason": raw.get("Csat_Reason")
        }
    }
    return payload


def upload_ticket(payload: Dict[str, Any]) -> bool:
    """Upload a single ticket to MaestroQA.

    Args:
        payload (Dict[str, Any]): The formatted ticket payload.

    Returns:
        bool: True if upload succeeded, False otherwise.
    """
    resp = requests.post(API_URL, headers=HEADERS, json=payload)
    if resp.status_code == 201:
        print(f"✅ Uploaded {payload['ticket_id']}")
        return True
    else:
        print(f"❌ Failed {payload['ticket_id']}: {resp.status_code} - {resp.text}")
        return False


def main() -> None:
    """Main entry point for uploading tickets."""
    csv_path = "tickets.csv"

    try:
        tickets = load_tickets_from_csv(csv_path)
        print(f"Loaded {len(tickets)} tickets from {csv_path}")
        for raw in tickets:
            payload = transform_ticket_for_api(raw)
            upload_ticket(payload)
    except FileNotFoundError:
        print(f"❌ File not found: {csv_path}")
    except KeyError as e:
        print(f"❌ Missing expected column: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


if __name__ == "__main__":
    main()
