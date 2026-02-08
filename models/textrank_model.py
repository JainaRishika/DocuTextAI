"""
TextRank-based extractive text summarization
"""

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.utils import get_stop_words


class TextRankSummarizerModel:
    def __init__(self, language: str = "english"):
        self.language = language
        self.summarizer = TextRankSummarizer()
        self.summarizer.stop_words = get_stop_words(language)

    def summarize(
        self,
        text: str,
        sentence_count: int = 5
    ) -> str:
        """
        Generate extractive summary using TextRank

        Args:
            text (str): Input text
            sentence_count (int): Number of sentences

        Returns:
            str: Extractive summary
        """

        if not text or len(text.strip()) == 0:
            return "No text provided for summarization."

        parser = PlaintextParser.from_string(
            text,
            Tokenizer(self.language)
        )

        summary_sentences = self.summarizer(
            parser.document,
            sentence_count
        )

        summary = " ".join(str(sentence) for sentence in summary_sentences)

        return summary.strip()
