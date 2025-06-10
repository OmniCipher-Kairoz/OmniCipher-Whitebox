"""
Prompt interface for OmniCipher LLM interaction.
Connects to local server and facilitates user input/output.
"""

import requests
import uuid
import json
from sanitize_prompt import sanitize_prompt

SESSION_ID = str(uuid.uuid4())
API_URL = "http://localhost:8000/v1/chat/completions"

print("----------------------------------------")
print(f"[OmniCipher] Signal Engine Online | Session: {SESSION_ID}")
print("[OmniCipher] Type 'exit' to close.")
print("----------------------------------------")

while True:
    user_input = input("Ask: ").strip()
    if user_input.lower() == "exit":
        break

    sanitized = sanitize_prompt(user_input)

    payload = {
        "model": "local-model",
        "messages": [
            {"role": "user", "content": sanitized}
        ]
    }

    try:
        response = requests.post(API_URL, json=payload)
        data = response.json()
        output = data['choices'][0]['message']['content']
        print(f"[OmniCipher] {output}")
    except Exception as e:
        print(f"[ERROR] {e}")
