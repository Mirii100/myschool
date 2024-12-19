# utils.py
import PyPDF2
from docx import Document as DocxDocument

def read_pdf(file_path):
    content = ""
    with open(file_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        for page in reader.pages:
            content += page.extract_text()
    return content

def read_docx(file_path):
    doc = DocxDocument(file_path)
    content = "\n".join([paragraph.text for paragraph in doc.paragraphs])
    return content
