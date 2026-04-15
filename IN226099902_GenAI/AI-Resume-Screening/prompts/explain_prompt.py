from langchain_core.prompts import PromptTemplate

explain_prompt = PromptTemplate.from_template("""
Explain the score clearly.

Include:
- Matched skills count
- Missing important skills
- Experience impact (use experience_years from candidate)

DO NOT say "not available" if data exists.

Data:
{data}
""")