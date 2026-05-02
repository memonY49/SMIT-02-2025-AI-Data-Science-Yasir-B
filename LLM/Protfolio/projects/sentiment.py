from textblob import TextBlob

def analyze(text):
    return str(TextBlob(text).sentiment)