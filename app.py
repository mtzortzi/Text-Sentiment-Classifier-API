#!/usr/bin/python3

"""  
    This file launches a simple web interface using Gradio to classify text sentiment 
    (positive/negative) using a pre-trained DistilBERT model. It is designed to run 
    locally or directly on Hugging Face Spaces.
    
    @author mtzortzi
"""

import gradio as gr
from transformers import pipeline

# Load sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis", model = "distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(text):
    result = sentiment_analyzer(text)[0]
    label = result['label'].capitalize()
    score = round(result['score'], 4)
    return f"Sentiment: {label} (Confidence: {score})"

# Gradio interface
iface = gr.Interface(
    fn=analyze_sentiment,
    inputs=gr.Textbox(lines=3, placeholder="Enter a sentence for sentiment analysis..."),
    outputs="text",
    title="Text Sentiment Classifier",
    description="Classifies text as Positive or Negative using a DistilBERT model trained on SST-2."
)

iface.launch()
