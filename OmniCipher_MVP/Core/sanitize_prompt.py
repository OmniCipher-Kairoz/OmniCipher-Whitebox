import re
import string

def sanitize_prompt(prompt: str) -> str:
    """
    Sanitize and normalize the input prompt.

    Args:
        prompt (str): The raw input prompt from the user.

    Returns:
        str: A cleaned and normalized prompt string.
    """
    if not isinstance(prompt, str):
        raise ValueError("Prompt must be a string.")

    # Normalize whitespace
    prompt = re.sub(r'\s+', ' ', prompt).strip()

    # Remove unsafe control characters
    prompt = ''.join(ch for ch in prompt if ch in string.printable)

    # Convert to lowercase for normalization (can be removed if case-sensitive processing is required)
    prompt = prompt.lower()

    # Remove leading/trailing quotes or brackets
    prompt = prompt.strip('"[]{}()')

    return prompt
