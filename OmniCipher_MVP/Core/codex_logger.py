from datetime import datetime

def log_codex_entry(prompt: str, response: str, tag: str = "Unclassified", signal: int = 50):
    """
    Appends a prompt/response entry to the codex log file.
    """
    entry = f"""------------------------------
[TIMESTAMP]: {datetime.now().isoformat()}
[PROMPT]: {prompt}
[RESPONSE]: {response}
[TAG]: {tag}
[SIGNAL]: {signal}%
------------------------------\n"""
    
    with open("codex_signal_entries.txt", "a", encoding="utf-8") as f:
        f.write(entry)
