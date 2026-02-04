import json
import sys

FLAG_PHRASES = [
    "suicide",
    "kill myself",
    "end it",
    "ending it",
    "ending it all",
    "take my life",
]

def analyze_messages(messages):
    total = len(messages)
    user_count = sum(1 for m in messages if m.get("sender") == "user")
    assistant_count = sum(1 for m in messages if m.get("sender") == "assistant")

    needs_review = False
    for m in messages:
        if m.get("sender") == "user":
            text = m.get("text", "").lower()
            if any(phrase in text for phrase in FLAG_PHRASES):
                needs_review = True
                break

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

    with open(sys.argv[1], "r") as f:
        data = json.load(f)

    results = analyze_messages(data)
    print(json.dumps(results, indent=2))
