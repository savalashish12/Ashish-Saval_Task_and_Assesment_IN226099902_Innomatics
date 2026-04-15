from langchain_core.output_parsers import StrOutputParser
from prompts.extract_prompt import extract_prompt
from utils.config import get_llm
llm = get_llm()

extract_chain = extract_prompt | llm | StrOutputParser()