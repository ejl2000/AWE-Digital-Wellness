# AWE-Digital-Wellness

## JSON Message Analyzer

This script processes a list of chat messages stored in a JSON file.  
It counts how many messages came from the user, how many came from the assistant, and checks whether any user message contains specific phrases that should trigger a human review.

It’s a simple, lightweight tool designed to demonstrate working with JSON data, basic logic, and clean code structure.

## Features

The script outputs:

- **Total number of messages**
- **Number of user messages**
- **Number of assistant messages**
- **needs_human_review: true/false**

The `needs_human_review` flag becomes **true** if any user message contains one of the following phrases:

- “suicide”
- “kill myself”
- “end it”
- "ending it"
- “ending it all”
- “take my life”

These phrases are defined in the script and can be modified as needed.

## Requirements

- Python 3.x
- A JSON file containing an array of message objects  
  (each with `"sender"` and `"text"` fields)

## How to Run

1. Save the script as **`analyze_messages.py`**
2. Create a JSON file, for example **`messages.json`**
3. Run the script from the command line:

```
python analyze_messages.py messages.json
```

You will see the output: 

```json
{
  "total_messages": 4,
  "user_messages": 3,
  "assistant_messages": 1,
  "needs_human_review": true
}
```

## Assumptions & Limitations

- Input must be a JSON array of objects with `"sender"` and `"text"`.
- Only **user** messages are scanned for concerning phrases.
- Phrase detection uses simple substring matching.
- This script is a basic demonstration and not a replacement for human judgment.
