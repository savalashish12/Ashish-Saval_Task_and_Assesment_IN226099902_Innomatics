from langchain_core.prompts import PromptTemplate

score_prompt = PromptTemplate.from_template("""
You are a strict evaluator.

Data:
{data}

Instructions:
- total_required = len(jd.required_skills)
- matched = len(match.matched_skills)

Score formula:
score = (matched / total_required) * 100

Adjustments:
+10 if experience_years >= 3
-10 if experience_years < 1

Return ONLY JSON:
{{
  "score": number
}}

DO NOT add explanation.
DO NOT return text outside JSON.
DO NOT hallucinate.
""")