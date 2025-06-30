from textblob import TextBlob

text = input("Enter text: ")
blob = TextBlob(text)
print(f"Sentiment: {blob.sentiment.polarity:.2f} (Positive > 0, Negative < 0)")