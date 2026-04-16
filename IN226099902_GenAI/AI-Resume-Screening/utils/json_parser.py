import json
import re

def safe_json_parse(text):
    try:
        cleaned = re.sub(r"```json|```", "", text).strip()
        return json.loads(cleaned)
    except:
        def safe_json_parse(text):
            try:
                cleaned = re.sub(r"```json|```", "", text).strip()
                return json.loads(cleaned)
            except:
                print("⚠️ JSON ERROR:", text)
                return {}