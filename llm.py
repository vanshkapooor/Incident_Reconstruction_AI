import requests
import os

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

headers = {
    "Authorization": f"Bearer {os.getenv('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')}"
}

def call_llm(prompt):
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 200,
            "temperature": 0.3
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    result = response.json()

    if isinstance(result, list):
        return result[0]["generated_text"]
    else:
        return str(result)
