import requests
import os
import urllib3

from dotenv import load_dotenv
load_dotenv()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


API_KEY = os.getenv("EURI_API_KEY")


def generate_completion(prompt, model="gpt-4.1-mini", temperature=0.3):
    
    url = "https://api.euron.one/api/v1/euri/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature,
        "max_tokens": 500
    }
    res = requests.post(url, headers=headers, json=payload, verify=False, timeout=30)
    return res.json()["choices"][0]["message"]["content"]    