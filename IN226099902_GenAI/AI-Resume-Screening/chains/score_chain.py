from langchain_core.output_parsers import StrOutputParser
from prompts.score_prompt import score_prompt
from utils.config import get_llm
llm = get_llm()

score_chain = score_prompt | llm | StrOutputParser()