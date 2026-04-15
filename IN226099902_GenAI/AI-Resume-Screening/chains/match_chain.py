from langchain_core.output_parsers import StrOutputParser
from prompts.match_prompt import match_prompt
from utils.config import get_llm
llm = get_llm()

match_chain = match_prompt | llm | StrOutputParser()