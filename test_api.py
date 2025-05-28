#!/usr/bin/python3

"""
   
    
    @author mtzortzi
"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_predict_sentiment():
  response = client.post("/predict", json={"text": "I love this!"})
  assert response.status_code == 200
  data = response.json()
  assert "sentiment" in data
  assert data["sentiment"] in ["positive", "negative", "neutral"]
  assert isinstance(data["confidence"], float)
