"""
Gemini-based abstractive text summarization
"""

from google import genai
import os


class GeminiSummarizer:
    def __init__(self):
        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

    def summarize(
        self,
        text: str,
        length: str = "medium",
        tone: str = "neutral"
    ) -> str:
        """
        Generate abstractive summary using Gemini

        Args:
            text (str): Input text
            length (str): short | medium | detailed
            tone (str): neutral | simple | academic

        Returns:
            str: Generated summary
        """

        prompt = f"""
You are an expert text summarizer.

Summary length: {length}
Tone: {tone}

Rules:
- Do not add extra information
- Keep meaning accurate
- Use clear sentences

Text:
{text}
"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text.strip()
