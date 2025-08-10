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

### 1️⃣ Upload Screen
![Upload Screen](./assets/upload_screen.png)

### 2️⃣ Checklist Summary Screen
![Checklist Summary](./assets/checklist_summary.png)

---

## 📂 Project Structure

