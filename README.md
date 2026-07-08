# 🚗 Autonomous Insurance Claims Processing Agent

An AI-powered backend application that automates the processing of **First Notice of Loss (FNOL)** documents for insurance claims.

The application extracts structured information from PDF and TXT FNOL documents using the **Groq LLM**, validates the extracted data, detects missing or inconsistent fields, classifies the claim according to business rules, and returns a structured JSON response.

> **Note:** This repository currently contains the backend implementation. A React frontend will be added in a future update.

---

# Features

- 📄 Extract information from PDF and TXT FNOL documents
- 🤖 AI-powered field extraction using Groq (Llama 3.3)
- ✅ Pydantic schema validation
- 🔍 Detect missing mandatory fields
- ⚠️ Detect basic inconsistent claim data
- 🚦 Rule-based claim routing
- 💬 Human-readable routing explanation
- 🚀 REST API built with FastAPI
- 📚 Interactive Swagger API documentation

---

# Tech Stack

## Backend

- Python 3.12
- FastAPI
- Groq API
- PyMuPDF
- Pydantic
- python-dotenv
- Uvicorn

---

# Project Structure

```text
INSURANCE-CLAIMS-AGENT/
│
├── backend/
│   │
│   ├── app/
│   │   │
│   │   ├── api/
│   │   │     └── routes.py
│   │   │
│   │   ├── core/
│   │   │     └── config.py
│   │   │
│   │   ├── models/
│   │   │     └── schema.py
│   │   │
│   │   ├── prompts/
│   │   │     └── extraction_prompt.txt
│   │   │
│   │   │
│   │   ├── services/
│   │   │     ├── llm/
│   │   │     ├── claim_processor.py
│   │   │     ├── consistency_checker.py
│   │   │     ├── extractor.py
│   │   │     ├── reasoning.py
│   │   │     ├── router.py
│   │   │     └── validator.py
│   │   │
│   │   ├── utils/
│   │   │     ├── file_loader.py
│   │   │     ├── json_parser.py
│   │   │     ├── normalizer.py
│   │   │     ├── pdf_reader.py
│   │   │     └── prompt_loader.py
│   │   │
│   │   └── main.py
|   |
│   ├── sample_documents/
|   |
│   ├── uploads/
│   ├── outputs/
│   │
│   ├── test_extractor.py
│   ├── test_groq.py
│   ├── requirements.txt
│   ├── .env
│   └── .gitignore
│
└── README.md
```

---

# Processing Pipeline

```text
          FNOL Document
                 │
                 ▼
        PDF/TXT File Reader
                 │
                 ▼
         Text Extraction Layer
                 │
                 ▼
            Groq LLM API
                 │
                 ▼
         Structured JSON Output
                 │
                 ▼
        Pydantic Validation
                 │
                 ▼
      Missing Field Detection
                 │
                 ▼
      Consistency Validation
                 │
                 ▼
          Routing Engine
                 │
                 ▼
        Reasoning Generator
                 │
                 ▼
          Final JSON Result
```

---

# Extracted Fields

The application extracts the following information:

## Policy Information

- Policy Number
- Policyholder Name
- Effective Dates

## Incident Information

- Incident Date
- Incident Time
- Location
- Description

## Involved Parties

- Claimant
- Third Parties
- Contact Details

## Asset Details

- Asset Type
- Asset ID
- Estimated Damage

## Other Information

- Claim Type
- Attachments
- Initial Estimate

---

# Routing Rules

| Condition | Route |
|------------|-------|
| Estimated Damage < 25,000 | Fast-track |
| Missing mandatory fields | Manual Review |
| Description contains "fraud", "staged" or "inconsistent" | Investigation Flag |
| Claim Type = Injury | Specialist Queue |
| Otherwise | Standard Processing |

---

# API Endpoint

## Process FNOL Claim

```
POST /process-claim
```

### Request

```
multipart/form-data
```

| Parameter | Type |
|----------|------|
| file | PDF or TXT |

---

# Example Response

```json
{
  "extractedFields": {
    "policyNumber": "POL12345",
    "policyholderName": "John Smith",
    "estimatedDamage": 20000,
    "claimType": "Vehicle"
  },
  "missingFields": [],
  "consistencyIssues": [],
  "recommendedRoute": "Fast-track",
  "reasoning": "Estimated damage is below ₹25,000 and all mandatory fields are present."
}
```

---

# Getting Started

## Clone the Repository

```bash
git clone https://github.com/1-ashish-04/INSURANCE-CLAIMS-AGENT.git
```

---

## Navigate to the Backend

```bash
cd insurance-claims-agent/backend
```

---

## Create a Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file inside the `backend` directory.

```env
GROQ_API_KEY=your_groq_api_key
MODEL_NAME=llama-3.3-70b-versatile
```
Create a free API key from https://console.groq.com/.
---

## Run the Server

```bash
uvicorn app.main:app --reload
```

Server

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# Testing

Run the Groq connection test

```bash
python test_groq.py
```

Run the extraction pipeline test

```bash
python test_extractor.py
```

---

# Sample Documents

Sample FNOL documents can be placed inside

```
backend/app/sample_documents/
```

Supported formats:

- PDF
- TXT

---

# Future Improvements

- React frontend dashboard
- Drag-and-drop file upload
- OCR support for scanned PDFs
- DOCX support
- Docker containerization
- Unit and integration testing
- Database integration
- Authentication and authorization
- Claim history tracking

---

# License
This project is licensed under the MIT License. See the LICENSE file for details.

---

# Author

**Ashish Jayaswal**

Bachelor of Computer Science

AI-Powered Autonomous Insurance Claims Processing Agent