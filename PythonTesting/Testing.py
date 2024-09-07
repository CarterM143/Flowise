"""
This is the pull from the "Simple Doc Reader" Flowise script
"""

import requests

API_URL = "http://localhost:3050/api/v1/prediction/ef035852-b714-4ec6-b3cc-cccd6029e011"

def query(payload):
    response = requests.post(API_URL, json=payload)
    print(response.json())
    return response.json()
    
output = query({
    "question": "What is the current leverage ratio? I want only the answer, with no other text",
})

if output["text"] == "4.6%":
    print("Correct number found!")
