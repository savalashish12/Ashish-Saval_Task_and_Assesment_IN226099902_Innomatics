from langchain_core.prompts import PromptTemplate

score_prompt = PromptTemplate.from_template("""
You are a strict evaluator.

Rules:
- Base score = (matched / total_required) * 100

Adjustments:
- If experience_years >= 3 → add +10
- If experience_years < 1 → reduce -10

Return STRICT JSON:
{{
  "score": number
}}

Data:
{data}
""")