#!/usr/bin/python3

"""
    Uses the HuggingFace model: distilbert-base-uncased-finetuned-sst-2-english.
    Provides a /predict endpoint that accepts text input and returns sentiment
    (positive, negative, or neutral) along with a confidence score.
    
    @author mtzortzi
"""


from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Load a pre-trained sentiment analysis pipeline from HuggingFace
sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

class TextInput(BaseModel):
  text: str

@app.get("/")
def read_root():
  return {"message": "Welcome to the Text Sentiment Classifier API"}

@app.post("/predict")
def predict_sentiment(input: TextInput):
  """
  Predict the sentiment of the input text using a DistilBERT model fine-tuned on SST-2.
  Returns whether the sentiment is positive, negative, or neutral, along with a confidence score.
  """
  result = sentiment_analyzer(input.text)[0]
  label = result['label']
  score = round(result['score'], 4)

  # Map model output to similar sentiment labels
  if label == 'POSITIVE':
    sentiment = 'positive'
  elif label == 'NEGATIVE':
    sentiment = 'negative'
  else:
    sentiment = 'neutral' # Not commonly returned by this binary model
  return {
    "sentiment": sentiment,
    "confidence": score
}
