"""
memory_recall.py

Handles retrieval and update of semantic memory using vector-based similarity scoring.
Integrates with: codex_logger.py, signal_scoring_refined.py, and memory index files.
"""

import json
import os
from pathlib import Path
from typing import Dict, Any, List
from 6_peers.signal_scoring_refined import score_relevance
from 2_codex.codex_logger import log_event

MEMORY_DIR = Path("3_memory/Memory")
INDEX_PATH = MEMORY_DIR / "codex_memory_index.json"
LOG_PATH = MEMORY_DIR / "codex_memory_log.txt"

def load_memory_index() -> List[Dict[str, Any]]:
    """Load the vector-based memory index."""
    if INDEX_PATH.exists():
        with open(INDEX_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_memory_index(index: List[Dict[str, Any]]) -> None:
    """Save updated memory index."""
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2)

def recall(prompt: str) -> Dict[str, Any]:
    """
    Retrieve the most relevant memory entry based on prompt similarity.

    Args:
        prompt (str): The user's prompt.

    Returns:
        Dict[str, Any]: Best matched memory entry with reasoning metadata.
    """
    index = load_memory_index()
    if not index:
        return {"match": None, "score": 0.0, "reason": "No memory entries available."}

    best_entry = None
    highest_score = 0.0
    for entry in index:
        score = score_relevance(prompt, entry["prompt"])
        if score > highest_score:
            highest_score = score
            best_entry = entry

    result = {
        "match": best_entry,
        "score": round(highest_score, 4),
        "reason": "Highest semantic similarity found."
    }
    log_event("memory_recall", result)
    return result

def store_memory(prompt: str, response: str) -> None:
    """
    Store a new memory entry with prompt, response, and timestamp.

    Args:
        prompt (str): Original user input.
        response (str): AI's generated response.
    """
    from datetime import datetime
    index = load_memory_index()
    entry = {
        "prompt": prompt,
        "response": response,
        "timestamp": datetime.utcnow().isoformat()
    }
    index.append(entry)
    save_memory_index(index)

    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")

    log_event("store_memory", {"status": "success", "entry": entry})