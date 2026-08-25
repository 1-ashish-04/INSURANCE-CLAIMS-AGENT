# 🚗 Autonomous Insurance Claims Processing Agent

An AI-powered full-stack application that automates the processing of **First Notice of Loss (FNOL)** insurance claim documents.

The system extracts structured information from PDF and TXT FNOL documents using the **Groq LLM (Llama 3.3)**, validates the extracted data, identifies missing or inconsistent fields, classifies claims according to predefined business rules, and recommends the appropriate processing workflow.

The application consists of:

- ⚛️ **React Frontend** for uploading FNOL documents and visualizing results.
- 🚀 **FastAPI Backend** for AI-powered extraction, validation, routing, and reasoning.

---

# ✨ Features

## 🤖 AI Claim Processing

- 📄 Extract structured information from PDF and TXT FNOL documents
- 🤖 AI-powered field extraction using Groq (Llama 3.3)
- ✅ Schema validation using Pydantic
- 🔍 Detect missing mandatory fields
- ⚠️ Detect inconsistent claim information
- 🚦 Rule-based claim routing
- 💬 AI-generated routing explanation

---

## 💻 Frontend Dashboard

- ⚛️ Modern React dashboard
- 📤 Upload PDF/TXT FNOL documents
- 📊 Claim summary dashboard
- 🚥 Route status badges
- 📋 Missing fields panel
- 🔍 Consistency issues panel
- 💡 AI reasoning display
- 📱 Responsive UI

---

## 🚀 Backend API

- FastAPI REST API
- Interactive Swagger Documentation
- React ↔ FastAPI Integration
- JSON Response API

---

# 🛠 Tech Stack

## Frontend

- React (Vite)
- JavaScript (ES6+)
- Axios
- React Icons
- CSS3

---

## Backend

- Python 3.12
- FastAPI
- Groq API
- Llama 3.3 70B Versatile
- PyMuPDF
- Pydantic
- python-dotenv
- Uvicorn

---

# 📁 Project Structure

```text
INSURANCE-CLAIMS-AGENT/
│
├── backend/
│   │
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   ├── prompts/
│   │   ├── services/
│   │   ├── utils/
│   │   └── main.py
│   │
│   ├── outputs/
│   ├── sample_documents/
│   ├── uploads/
│   ├── requirements.txt
│   ├── test_extractor.py
│   ├── test_groq.py
│   └── .env
│
├── frontend/
│   │
│   ├── public/
│   │
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── styles/
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   ├── package.json
│   ├── vite.config.js
│   └── .gitignore
│
├── LICENSE
└── README.md
```

---

# 🏗 System Architecture

```text
                    User Uploads FNOL Document
                               │
                               ▼
                    React Frontend Dashboard
                               │
                               ▼
                         FastAPI REST API
                               │
                               ▼
                      PDF / TXT Text Reader
                               │
                               ▼
                         Groq LLM (Llama 3.3)
                               │
                               ▼
                  Structured Information Extraction
                               │
                               ▼
                    Validation & Consistency Checks
                               │
                               ▼
                        Rule-Based Routing Engine
                               │
                               ▼
                     AI Reasoning Generation
                               │
                               ▼
                      JSON Response to Frontend
```

---

# ⚙ Processing Pipeline

```text
          FNOL Document
                 │
                 ▼
         Upload via React UI
                 │
                 ▼
         FastAPI File Upload API
                 │
                 ▼
        PDF/TXT Text Extraction
                 │
                 ▼
            Groq LLM API
                 │
                 ▼
      Structured JSON Extraction
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
      Results Displayed in React
```

---

# 📄 Extracted Fields

## Policy Information

- Policy Number
- Policyholder Name
- Effective Dates

---

## Incident Information

- Incident Date
- Incident Time
- Location
- Description

---

## Involved Parties

- Claimant
- Third Parties
- Contact Details

---

## Asset Details

- Asset Type
- Asset ID
- Estimated Damage

---

## Other Information

- Claim Type
- Attachments
- Initial Estimate

---

# 🚦 Routing Rules

| Condition | Route |
|------------|-------|
| Estimated Damage < ₹25,000 | Fast-track |
| Missing mandatory fields | Manual Review |
| Description contains **fraud**, **staged**, or **inconsistent** | Investigation Flag |
| Claim Type = Injury | Specialist Queue |
| Otherwise | Standard Processing |

---

# 🌐 REST API

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

## Example Response

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

# 🚀 Getting Started

## Clone Repository

```bash
git clone https://github.com/1-ashish-04/INSURANCE-CLAIMS-AGENT.git

cd INSURANCE-CLAIMS-AGENT
```

---

# ⚙ Backend Setup

## Navigate to Backend

```bash
cd backend
```

---

## Create Virtual Environment

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

Create a free API key from:

https://console.groq.com/

---

## Run Backend

```bash
uvicorn app.main:app --reload
```

Backend

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# 💻 Frontend Setup

Navigate to the frontend directory.

```bash
cd frontend
```

Install dependencies.

```bash
npm install
```

Run the React development server.

```bash
npm run dev
```

Frontend

```
http://localhost:5173
```

---

# 🧪 Testing

Run the Groq connection test.

```bash
python test_groq.py
```

Run the extraction pipeline test.

```bash
python test_extractor.py
```

---

# 📂 Sample Documents

Place sample FNOL documents inside:

```
backend/sample_documents/
```

Supported formats:

- PDF
- TXT


# 🚀 Future Improvements

- OCR support for scanned PDFs
- DOCX document support
- Authentication & Authorization
- Database integration (PostgreSQL/MongoDB)
- Claim history dashboard
- Docker & Docker Compose
- Unit & Integration Testing
- CI/CD Pipeline
- Cloud Deployment
- Email Notifications

---

# 📄 License

This project is licensed under the **MIT License**.

See the **LICENSE** file for more information.

---

# 👨‍💻 Author

**Ashish Jayaswal**

Bachelor of Computer Science

**Autonomous Insurance Claims Processing Agent**

Built using **React**, **FastAPI**, and **Groq Llama 3.3**.