from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.2:
        return "😊 Positive"
    elif polarity < -0.2:
        return "😔 Negative"
    else:
        return "😐 Neutral"

if __name__ == "__main__":
    print("📝 Write your journal entry below (end with ENTER):")
    entry = input("> ")

    mood = analyze_sentiment(entry)
    print(f"🧠 Sentiment Analysis Result: {mood}")
