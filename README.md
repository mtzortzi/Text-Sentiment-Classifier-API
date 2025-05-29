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

# 📁 File Structure

. </br>
├── main.py               # API implementation </br>
├── requirements.txt      # Python dependencies </br>
└── README.md             # Project documentation </br>


## 🚀 How to Use

1. Enter any English sentence in the input box
2. Click **Submit**
3. View the sentiment label and confidence


## 🚀 How to Deploy on Hugging Face Spaces

1. Create a Hugging Face account <br>
   Sign up at https://huggingface.co/join

2. Create a new Space
   Go to https://huggingface.co/spaces and click Create new Space

3. Fill out the form
   - Space name: text-sentiment-api (or your choice)
   - SDK: Gradio
   - Visibility: Public or Private

4. Upload the files
   - app.py
   - requirements.txt
   - README.md (this file)

5. Wait for the build 
   Hugging Face will automatically install dependencies and launch the app

6. Access your app
