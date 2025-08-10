from docx import Document
from PyPDF2 import PdfReader
import os

def docx_to_text(path):
    doc = Document(path)
    return "\n".join([p.text.strip() for p in doc.paragraphs if p.text.strip()])

def pdf_to_text(path):
    reader = PdfReader(path)
    return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

def convert_all_docs(raw_folder="data/raw_docs", out_folder="data/converted"):
    os.makedirs(out_folder, exist_ok=True)
    for file in os.listdir(raw_folder):
        input_path = os.path.join(raw_folder, file)
        if file.endswith(".docx"):
            content = docx_to_text(input_path)
        elif file.endswith(".pdf"):
            content = pdf_to_text(input_path)
        else:
            continue  # Skip unsupported files

        output_filename = file.replace(".pdf", ".txt").replace(".docx", ".txt")
        output_path = os.path.join(out_folder, output_filename)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ Converted: {file} → {output_filename}")
