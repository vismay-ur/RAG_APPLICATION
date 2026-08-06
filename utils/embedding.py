import requests
import numpy as np
import os
import urllib3
from dotenv import load_dotenv
load_dotenv()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


API_KEY = os.getenv("EURI_API_KEY")

def get_embedding(text, model="text-embedding-3-small"):
    url = "https://api.euron.one/api/v1/euri/embeddings"   # verify this endpoint

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "input": text,
        "model": model
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload,
        verify=False,
        timeout=30,
    )

    print("Status:", response.status_code)
    print("Response:", response.text)

    response.raise_for_status()

    return np.array(
        response.json()["data"][0]["embedding"],
        dtype=np.float32,
    )