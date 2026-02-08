"""
ROUGE score evaluation for text summarization models
Supports: ROUGE-1, ROUGE-2, ROUGE-L
"""

from rouge_score import rouge_scorer


def calculate_rouge(reference_text: str, generated_summary: str) -> dict:
    """
    Calculate ROUGE scores between reference text and generated summary

    Args:
        reference_text (str): Original text
        generated_summary (str): Model-generated summary

    Returns:
        dict: ROUGE-1, ROUGE-2, ROUGE-L scores
    """

    scorer = rouge_scorer.RougeScorer(
        ["rouge1", "rouge2", "rougeL"],
        use_stemmer=True
    )

    scores = scorer.score(reference_text, generated_summary)

    rouge_results = {
        "ROUGE-1": round(scores["rouge1"].fmeasure, 4),
        "ROUGE-2": round(scores["rouge2"].fmeasure, 4),
        "ROUGE-L": round(scores["rougeL"].fmeasure, 4)
    }

    return rouge_results


if __name__ == "__main__":
    # Simple test
    reference = """
    Machine learning is a field of artificial intelligence that allows systems
    to learn and improve from experience without being explicitly programmed.
    """

    summary = "Machine learning allows systems to learn from data."

    print(calculate_rouge(reference, summary))
