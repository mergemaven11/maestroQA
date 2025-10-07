# 🎯 MaestroQA Ticket Upload – Technical Assessment

---

## 🧩 Overview

This project demonstrates a full workflow for **loading customer-provided ticket data into MaestroQA via API**.

The process covers:
1. Reading and transforming client CSV data.
2. Authenticating securely using MaestroQA’s API.
3. Uploading tickets programmatically to a test account.
4. Verifying successful ingestion both through API responses and dashboard review.

---

## 🧠 Summary of Actions

| Step | Description |
|------|--------------|
| **1. Data Preparation** | The client provided a CSV file (`CX Ticket Upload Data - Tech Assessment - Tobias Scott - Tickets.csv`) containing 10 support ticket records. The dataset included fields like `Support_Ticket_Id`, `Agent ID`, `Created_Date`, `Closed_Date`, `ticket_category`, `Csat_Score`, and more. |
| **2. Data Cleaning & Transformation** | Each row from the CSV was parsed using Python’s `csv.DictReader` and converted into a JSON-compatible format required by the MaestroQA API. Fields were normalized and mapped to the expected API schema. |
| **3. Authentication** | The MaestroQA API key was stored securely in a `.env` file and accessed using the `dotenv` package. Authentication was handled via a header parameter:<br>`apiToken: <API_KEY>` |
| **4. Upload Process** | Each ticket record was sent via a `POST` request to:<br>`https://app.maestroqa.com/api/v1/tickets`<br> Successful uploads returned **HTTP 201 Created**, confirming that all tickets were loaded successfully. |
| **5. Verification** | API responses confirmed success for tickets `ts-1009` through `ts-1018`. To confirm visibility, dashboard filters (Agent, Group, Date Range) were adjusted to “All Time” and “All Agents.” |
| **6. Result** | ✅ All 10 tickets were successfully uploaded into the MaestroQA test account using the provided API key. |

---

## 🧾 Process Summary (Concise)

> **In short:**  
> The customer’s raw CSV ticket data was transformed into the MaestroQA API format and uploaded using a secure Python script.  
> The process validated input data, authenticated via `apiToken`, and confirmed success via API responses (`201 Created`).  
> The resulting tickets (`ts-1009` → `ts-1018`) now exist in the MaestroQA test account, ready for QA analysis or dashboard viewing.

---

## 🧰 Tools & Technologies

| Tool | Purpose |
|------|----------|
| **Python 3.11** | Scripted the data load process. |
| **Requests** | API communication with MaestroQA. |
| **dotenv** | Secure API key management. |
| **CSV / JSON** | Data input and transformation. |
| **MaestroQA API** | Target endpoint for ticket ingestion. |

---

## ⚙️ How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/maestroQA.git
   cd maestroQA

## ⚙️ How to Run Locally

### 1️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Add Your API Key
Create a `.env` file in the project root:
MAESTRO_API_TOKEN=TOKEN

### 4️⃣ Run the Uploader

```bash
python -m main
```

### 5️⃣ Expected Output

✅ Uploaded ts-1009
✅ Uploaded ts-1010
...
✅ Uploaded ts-1018

---


## 📄 Full Documentation
You can view the detailed write-up here:

👉 [View Google Doc](https://docs.google.com/document/d/1cTV7jIngy0Bt3gEKlmuNb4kNvFfmhQwNEEIjLSSkCV8/edit?usp=sharing)


