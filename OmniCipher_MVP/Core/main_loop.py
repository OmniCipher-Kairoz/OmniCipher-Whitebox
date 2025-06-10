# OmniCipher | 1_core/main_loop.py
# Main LLM loop logic — loads model, receives input, processes, and returns response.

import os
import sys
import time
import json
from llama_cpp import Llama
from pathlib import Path

# === CONFIGURATION ===
MODEL_PATH = Path("1_core/models/mistral-7b-instruct-v0.1.Q4_K_M.gguf")
CONTEXT_SIZE = 4096
MAX_TOKENS = 512
TEMP = 0.4

# === LOAD MODEL ===
if not MODEL_PATH.exists():
    print(f"[FATAL] Model not found at: {MODEL_PATH}")
    sys.exit(1)

print("[INFO] Loading model...")
llm = Llama(
    model_path=str(MODEL_PATH),
    n_ctx=CONTEXT_SIZE,
    n_threads=os.cpu_count(),
    verbose=False
)
print("[INFO] Model loaded successfully.")

# === MAIN FUNCTION ===
def query_local_ai(prompt):
    response = llm(
        prompt=prompt,
        max_tokens=MAX_TOKENS,
        temperature=TEMP,
        echo=False
    )

    content = response.get("choices", [{}])[0].get("text", "")
    return content.strip()

# === COMMAND-LINE INTERFACE ===
def main():
    print("[OmniCipher] Local Model Ready. Type 'exit' to quit.")
    while True:
        user_input = input("Ask: ").strip()
        if user_input.lower() == "exit":
            break

        print("[Processing...]")
        answer = query_local_ai(user_input)
        print(f"\n>> {answer}\n")

if __name__ == "__main__":
    main()
