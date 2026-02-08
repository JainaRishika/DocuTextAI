"""
Text cleaning utilities
"""

import re


def clean_text(text: str) -> str:
    """
    Clean and normalize input text

    Args:
        text (str): Raw input text

    Returns:
        str: Cleaned text
    """

    if not text:
        return ""

    # Remove extra newlines
    text = re.sub(r"\n+", "\n", text)

    # Remove multiple spaces
    text = re.sub(r"\s+", " ", text)

    # Remove non-printable characters
    text = re.sub(r"[^\x20-\x7E]+", " ", text)

    return text.strip()
