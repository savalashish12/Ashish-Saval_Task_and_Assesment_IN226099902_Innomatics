from langchain_core.prompts import PromptTemplate

match_prompt = PromptTemplate.from_template("""
Example:
Required Skills: ["Python", "SQL"]
Candidate Skills: ["Python"]

Output:
{{
  "matched_skills": ["Python"],
  "missing_skills": ["SQL"]
}}

Now do for below:

Required Skills:
{jd}

Candidate:
{candidate}


DO NOT assume skills.
ONLY use given data.
""")