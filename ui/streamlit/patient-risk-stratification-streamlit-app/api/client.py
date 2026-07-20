import requests
API_URL="http://localhost:8000/predict-risk"
def predict(payload):
    return requests.post(API_URL,json=payload,timeout=60)
