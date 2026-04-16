from langchain_core.prompts import PromptTemplate

extract_prompt = PromptTemplate.from_template("""
You are an expert resume parser.

Extract the following clearly:

1. Skills (programming, ML, tools)
2. Tools
3. Total experience in YEARS

Return STRICT JSON:
{{
  "skills": [],
  "tools": [],
  "experience_years": number
}}

Rules:
- Extract skills EXACTLY as written (Python, SQL, etc.)
- Do NOT miss obvious skills
- Convert experience to number (e.g., 2.5 years → 2.5)
- If fresher → 0
- Do NOT leave skills empty if present
- Return only JSON. No explanation text.
- DO NOT add explanation text.
- DO NOT add anything outside JSON.

Resume:
{resume}
""")