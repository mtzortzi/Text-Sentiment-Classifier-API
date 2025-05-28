# Text-Sentiment-Classifier-API
This project is a simple REST API for sentiment analysis built with FastAPI and HuggingFace Transformers. It uses the distilbert-base-uncased-finetuned-sst-2-english model to classify English text as positive,  negative or (rarely) neutral, and it returns a confidence score.

# 🚀 Features

- RESTful API with FastAPI

- Pre-trained BERT-based sentiment model

- JSON input and output

- Interactive Swagger UI at /docs

# 📦 Model

The API uses:

`` distilbert-base-uncased-finetuned-sst-2-english ``

A lightweight version of BERT fine-tuned on the SST-2 dataset for sentiment classification.

# Example

Request:
``
POST /predict
{
  "text": "I absolutely love this product!"
}
``

Response:
``
{
  "sentiment": "positive",
  "confidence": 0.9981
}
``
