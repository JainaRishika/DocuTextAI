# 🧠 Advanced Text Summarizer (NLP + ML)

An advanced **text summarization web application** that combines **Large Language Models (Gemini)** with **classical Machine Learning (TextRank)**.  
The system supports **abstractive and extractive summarization**, file uploads, configurable controls, and quantitative evaluation using **ROUGE metrics**.

---

## 🚀 Features

- ✨ Abstractive summarization using **Gemini LLM**
- 📌 Extractive summarization using **TextRank (classical ML)**
- 🎚️ Summary length control: Short / Medium / Detailed
- 🗣️ Tone control: Neutral / Simple / Academic
- 📂 File upload support (TXT, PDF)
- 📊 Evaluation using **ROUGE-1, ROUGE-2, ROUGE-L**
- 🎨 Modern dark UI with loader animation
- ⚡ Flask-based backend with clean architecture

---

## 🏗️ Tech Stack

**Frontend**
- HTML, CSS (custom UI)
- JavaScript (Fetch API)

**Backend**
- Flask (Python)
- REST-style API

**NLP / ML**
- Gemini 2.5 Flash (Abstractive Summarization)
- TextRank (Extractive Summarization)
- ROUGE metrics for evaluation

**Libraries**
- google-genai
- sumy
- nltk
- rouge-score
- PyPDF2

---

## 📁 Project Structure

advanced-text-summarizer/
│
├── app.py
├── requirements.txt
├── .env
│
├── models/
│ ├── gemini_model.py
│ ├── textrank_model.py
│
├── evaluation/
│ └── rouge_scores.py
│
├── utils/
│ ├── file_parser.py
│ └── text_cleaner.py
│
├── static/
│ ├── style.css
│ └── loader.css
│
├── templates/
│ └── index.html
│
└── README.md


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/JainaRishika/advanced-text-summarizer.git
cd advanced-text-summarizer

2️⃣ Create virtual environment 
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Set environment variables
Create a .env file:
GEMINI_API_KEY=your_api_key_here

▶️ Run the Application
python app.py

Open in browser.

📊 How Evaluation Works

The application evaluates generated summaries using:

ROUGE-1 → Unigram overlap

ROUGE-2 → Bigram overlap

ROUGE-L → Longest common subsequence

These metrics help quantitatively compare different summarization approaches.

🧪 Models Used
🔹 Gemini (Abstractive)

Generates human-like summaries

Supports length and tone control

Best for concise and meaningful summaries

🔹 TextRank (Extractive)

Graph-based ranking algorithm

Selects most important sentences

No external API required

📌 Use Cases

Summarizing articles, blogs, research papers

Condensing long documents (PDF/TXT)

Educational and productivity tools

NLP experimentation and benchmarking

Website link:
https://docutextai.onrender.com/



