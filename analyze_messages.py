import json
import sys
import re

FLAG_PATTERNS = [
    r"\bsuicide\b",
    r"\bkill myself\b",
    r"\bend(ing)? it(\sall)?\b",
    r"\btake my life\b",
]

def contains_flag(text):
    text = text.lower()
    return any(re.search(pattern, text) for pattern in FLAG_PATTERNS)

def analyze_messages(messages):
    total = len(messages)
    user_count = sum(1 for m in messages if m.get("sender") == "user")
    assistant_count = sum(1 for m in messages if m.get("sender") == "assistant")

    needs_review = any(
        m.get("sender") == "user" and contains_flag(m.get("text", ""))
        for m in messages
    )

    return {
        "total_messages": total,
        "user_messages": user_count,
        "assistant_messages": assistant_count,
        "needs_human_review": needs_review
    }

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyze_messages.py messages.json")
        sys.exit(1)

    try:
        with open(sys.argv[1], "r") as f:
            data = json.load(f)
        if not isinstance(data, list):
            raise ValueError("JSON must be a list of messages.")
    except Exception as e:
        print(f"Error loading JSON: {e}")
        sys.exit(1)

    results = analyze_messages(data)
    print(json.dumps(results, indent=2))
