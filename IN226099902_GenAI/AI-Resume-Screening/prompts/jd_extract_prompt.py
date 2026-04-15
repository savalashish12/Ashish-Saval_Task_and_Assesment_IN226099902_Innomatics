from langchain_core.prompts import PromptTemplate

jd_extract_prompt = PromptTemplate.from_template("""
Extract REQUIRED skills from job description.

Return STRICT JSON:
{{
  "required_skills": []
}}

DO NOT assume anything.

Job Description:
{jd}
""")