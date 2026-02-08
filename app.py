from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os

from models.gemini_model import GeminiSummarizer
from models.textrank_model import TextRankSummarizerModel
from evaluation.rouge_scores import calculate_rouge
from utils.file_parser import extract_text_from_file
from utils.text_cleaner import clean_text

load_dotenv()

app = Flask(__name__)

# Initialize models
gemini_model = GeminiSummarizer()
textrank_model = TextRankSummarizerModel()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/summarize", methods=["POST"])
def summarize():
    text = request.form.get("text", "")
    model_type = request.form.get("model", "gemini")
    length = request.form.get("length", "medium")
    tone = request.form.get("tone", "neutral")
    uploaded_file = request.files.get("file")

    # If file is uploaded, extract text
    if uploaded_file and uploaded_file.filename != "":
        text = extract_text_from_file(uploaded_file)

    if not text or len(text.strip()) == 0:
        return jsonify({"summary": "Please provide text or upload a file."})

    text = clean_text(text)

    # Generate summary
    if model_type == "textrank":
        summary = textrank_model.summarize(text, sentence_count=5)
    else:
        summary = gemini_model.summarize(text, length=length, tone=tone)

    # ROUGE evaluation
    rouge_scores = calculate_rouge(text, summary)

    return jsonify({
        "summary": summary,
        "rouge": rouge_scores
    })


if __name__ == "__main__":
    app.run(debug=True)
