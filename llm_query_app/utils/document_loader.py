import fitz  # PyMuPDF
import docx
import os
from typing import Union

def extract_text(file: Union[str, bytes], filename: str) -> str:
    """
    Extracts raw text from PDF or DOCX file.
    
    Args:
        file: File object (stream or path)
        filename: File name string to detect extension
    
    Returns:
        Extracted plain text
    """
    text = ""

    if filename.lower().endswith(".pdf"):
        doc = fitz.open(stream=file.read(), filetype="pdf")
        for page in doc:
            text += page.get_text()

    elif filename.lower().endswith(".docx"):
        document = docx.Document(file)
        for para in document.paragraphs:
            text += para.text + "\n"

    else:
        raise ValueError("Unsupported file format: Use PDF or DOCX only.")

    return text.strip()

