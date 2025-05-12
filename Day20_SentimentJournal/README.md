# 🧠 Day 20 - Sentiment Journal Analyzer

A simple CLI tool where you write your journal entry and get an instant emotional feedback using Natural Language Processing.

## 💡 Features:
- Detects if your journal text is Positive, Neutral, or Negative
- Uses TextBlob NLP library
- Great for mental reflection & mood tracking

## 🧪 Example:

**Input:**  
`Today I felt motivated and proud of my efforts.`

**Output:**  
`😊 Positive`

## ⚙️ Setup:

```bash
pip install textblob
python -m textblob.download_corpora
python journal_sentiment.py
