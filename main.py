from textblob import TextBlob

text = "I am excited to learn AI!"
text1 = "I am sad to learn AI!"
blob = TextBlob(text)
blob1 = TextBlob(text1)
print("Sentiment polarity:", blob.sentiment.polarity)
print("Sentiment polarity:", blob1.sentiment.polarity)