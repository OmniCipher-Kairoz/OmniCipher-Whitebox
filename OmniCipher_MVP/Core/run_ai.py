"""
Main system controller for OmniCipher.
Launches local LLM server, verifies components, then hands off to prompt interface.
"""

import os
import subprocess
import time
import requests
import platform

MODEL_PATH = "Models/mistral-7b-instruct-v0.1.Q4_K_M.gguf"
PROMPT_SCRIPT = "Core/codex_prompt.py"
SERVER_PORT = 8000

def wait_for_server(url, timeout=30):
    start = time.time()
    while time.time() - start < timeout:
        try:
            response = requests.get(url)
            if response.status_code in [200, 404]:
                return True
        except requests.exceptions.ConnectionError:
            pass
        time.sleep(1)
    return False

if not os.path.exists(MODEL_PATH):
    print(f"[ERROR] Missing model file: {MODEL_PATH}")
    exit(1)

if not os.path.exists(PROMPT_SCRIPT):
    print(f"[ERROR] Missing script: {PROMPT_SCRIPT}")
    exit(1)

subprocess.Popen([
    "python", "-m", "llama_cpp.server",
    "--model", MODEL_PATH,
    "--port", str(SERVER_PORT)
])

print("[INFO] LLM server launched.")
if not wait_for_server(f"http://localhost:{SERVER_PORT}/v1/models"):
    print("[ERROR] Server did not respond in time.")
    exit(1)

print("[INFO] Launching OmniCipher prompt interface...")
os.system(f'python {PROMPT_SCRIPT}')
