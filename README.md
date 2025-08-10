# 🏛️ ADGM-Compliant Corporate Agent

An AI-powered tool that reviews company incorporation documents for **Abu Dhabi Global Market (ADGM)** compliance.  
It checks required documents, detects compliance issues, and provides structured summaries with recommendations.

---

## 📌 Features
- 📂 **Multi-file Upload** – Upload `.docx` incorporation documents
- ✅ **Checklist Verification** – Auto-checks presence of all mandatory documents
- ⚠️ **Compliance Analysis** – Detects red flags & suggests improvements
- 📄 **Annotated Outputs** – Returns annotated `.docx` with comments
- 📊 **Summary Export** – Download compliance report in JSON or PDF format
- 🔍 **Auto Document Type Detection** – Identifies AoA, MoA, UBO forms, etc.

---

## 🚀 Tech Stack
- **Frontend:** Streamlit
- **Backend:** Python + LangChain + OpenAI API
- **Storage:** Local / ChromaDB for RAG
- **Document Processing:** `python-docx`, PDF support
- **Deployment:** Local / Cloud

---

## 📸 Screenshots

## Upload Screen
![Upload Screen](assets/upload_screen.png)

## Checklist Summary
![Checklist Summary](assets/checklist_summary.png)

---

## 📂 Project Structure
corporate_agent_adgm/
│── app.py # Streamlit frontend
│── checklist_verifier.py # Checklist & compliance logic
│── comment_inserter.py # Annotates .docx with comments
│── rag_pipeline.py # RAG-based compliance checker
│── requirements.txt # Dependencies
│── README.md # Project documentation
│── assets/ # Screenshots & static files

---
