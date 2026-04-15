from langchain_core.output_parsers import StrOutputParser
from prompts.explain_prompt import explain_prompt
from utils.config import get_llm
llm = get_llm()

explain_chain = explain_prompt | llm | StrOutputParser()