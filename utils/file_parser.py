"""
File parser utility for extracting text from uploaded files
Supports: TXT, PDF
"""

import PyPDF2


def extract_text_from_file(file) -> str:
    """
    Extract text from uploaded file

    Args:
        file: Werkzeug FileStorage object

    Returns:
        str: Extracted text
    """

    if file.filename.endswith(".txt"):
        return file.read().decode("utf-8", errors="ignore")

    elif file.filename.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)
        extracted_text = ""

        for page in reader.pages:
            extracted_text += page.extract_text() or ""

        return extracted_text.strip()

    else:
        return ""
