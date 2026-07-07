import os
import pdfplumber
from docx import Document


# ==========================
# Extract Text From PDF
# ==========================

def extract_pdf_text(filepath):

    text = ""

    try:

        with pdfplumber.open(filepath) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

    except Exception as e:

        print("PDF Error :", e)

    return text


# ==========================
# Extract Text From DOCX
# ==========================

def extract_docx_text(filepath):

    text = ""

    try:

        doc = Document(filepath)

        for para in doc.paragraphs:

            text += para.text + "\n"

    except Exception as e:

        print("DOCX Error :", e)

    return text


# ==========================
# Main Function
# ==========================

def extract_resume_text(filepath):

    extension = os.path.splitext(filepath)[1].lower()

    if extension == ".pdf":
        return extract_pdf_text(filepath)

    elif extension == ".docx":
        return extract_docx_text(filepath)

    else:
        return ""