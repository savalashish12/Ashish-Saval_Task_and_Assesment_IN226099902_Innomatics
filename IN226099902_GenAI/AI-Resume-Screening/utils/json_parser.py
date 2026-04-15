import json
import re

def safe_json_parse(text):
    try:
        cleaned = re.sub(r"```json|```", "", text).strip()
        return json.loads(cleaned)
    except:
        return {"error": "Invalid JSON", "raw": text}