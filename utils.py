import PyPDF2
import pandas as pd
from docx import Document
import glob
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def load_api_keys(env_var="google_api_key"):
    api_keys_str = os.getenv(env_var, "")
    api_keys = [key.strip() for key in api_keys_str.split(",") if key.strip()]
    if not api_keys:
        raise ValueError(f"No valid API keys found in environment variable '{env_var}'.")
    return api_keys

def read_docx(file_path):
    document = Document(file_path)
    return "\n".join([para.text for para in document.paragraphs if para.text.strip()])

def read_xlsx(file_path):
    dfs = pd.read_excel(file_path, sheet_name=None)
    text = ""
    for sheet, df in dfs.items():
        text += df.to_string(index=False) + "\n"
    return text

def read_pdf(file_path):
    text = ""
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def build_transcript(document_dir="document"):
    transcript = ""
    for file_path in glob.glob(f"{document_dir}/**/*", recursive=True):
        if file_path.endswith(".docx"):
            transcript += read_docx(file_path) + "\n"
        elif file_path.endswith(".xlsx") or file_path.endswith(".xls"):
            transcript += read_xlsx(file_path) + "\n"
        elif file_path.endswith(".pdf"):
            transcript += read_pdf(file_path) + "\n"
    return transcript

