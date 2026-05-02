from transformers import pipeline

summarizer = pipeline("text-generation")

def summarize(text):
    return summarizer(text)[0]["summary_text"]