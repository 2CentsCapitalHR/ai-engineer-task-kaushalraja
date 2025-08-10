# main.py

import streamlit as st
import os
import shutil
import json
from checklist import clean_doc_name, check_missing_documents
from comment_inserter import insert_comment
from rag_engine import build_rag_pipeline

# ========== Config ==========
UPLOAD_DIR = "uploaded_docs"
REVIEWED_DIR = "reviewed_docs"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(REVIEWED_DIR, exist_ok=True)

# ========== UI ==========
st.set_page_config(page_title="ADGM Corporate Agent", layout="centered")
st.title("📄 ADGM-Compliant Corporate Agent")
st.markdown("Upload your Company Incorporation documents (.docx) for review and compliance checks.")

uploaded_files = st.file_uploader("Upload .docx files", type=["docx"], accept_multiple_files=True)

if st.button("🔍 Analyze Documents") and uploaded_files:
    st.info("Processing... Please wait ⏳")

    uploaded_names = []
    full_paths = []

    # Save and clean names
    for file in uploaded_files:
        save_path = os.path.join(UPLOAD_DIR, file.name)
        with open(save_path, "wb") as f:
            f.write(file.read())
        cleaned = clean_doc_name(file.name)
        uploaded_names.append(cleaned)
        full_paths.append((cleaned, save_path))

    # Step 1: Checklist Verification
    missing_docs = check_missing_documents(uploaded_names)

    # Step 2: Build RAG
    rag = build_rag_pipeline()

    # Step 3: Review each doc
    issues_found = []
    reviewed_docs = []

    for doc_name, path in full_paths:
        # Run RAG for a standard prompt (can be improved)
        prompt = f"Are there any ADGM compliance issues in the '{doc_name}' document?"
        result = rag.invoke(prompt)

        answer = result.get("result", "No response")
        sources = result.get("source_documents", [])

        if "not ADGM" in answer or "jurisdiction" in answer or "signatory" in answer:
            comment_text = f"⚠️ COMMENT: {answer}"
            reviewed_path = os.path.join(REVIEWED_DIR, f"reviewed_{os.path.basename(path)}")
            insert_comment(path, comment_text, reviewed_path)
            reviewed_docs.append(reviewed_path)

            # Add to summary
            issues_found.append({
                "document": doc_name,
                "issue": answer,
                "sources": [s.metadata['source'] for s in sources]
            })
        else:
            reviewed_docs.append(path)  # No issue, keep original

    # Step 4: Display Summary
    st.success("✅ Review completed!")

    st.subheader("📋 Checklist Summary")
    st.markdown(f"**Uploaded:** {len(uploaded_names)} / **Required:** 5")
    if missing_docs:
        st.warning("Missing Documents:")
        for doc in missing_docs:
            st.markdown(f"- ❌ {doc}")
    else:
        st.success("All required documents uploaded ✅")

    st.subheader("⚠️ Compliance Issues Found")
    if issues_found:
        for issue in issues_found:
            st.markdown(f"**{issue['document']}**: {issue['issue']}")
    else:
        st.success("No major red flags found in uploaded documents.")

    # Step 5: Generate summary JSON
    summary = {
        "process": "Company Incorporation",
        "documents_uploaded": len(uploaded_names),
        "required_documents": 5,
        "missing_documents": missing_docs,
        "issues_found": issues_found
    }

    summary_path = os.path.join(REVIEWED_DIR, "summary.json")
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)

    # Step 6: Download links
    st.subheader("⬇️ Download Files")
    for path in reviewed_docs:
        with open(path, "rb") as f:
            st.download_button(
                label=f"Download {os.path.basename(path)}",
                data=f,
                file_name=os.path.basename(path),
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

    with open(summary_path, "rb") as f:
        st.download_button(
            label="📊 Download Summary JSON",
            data=f,
            file_name="summary.json",
            mime="application/json"
        )

elif not uploaded_files:
    st.info("📎 Please upload your .docx documents to begin.")
