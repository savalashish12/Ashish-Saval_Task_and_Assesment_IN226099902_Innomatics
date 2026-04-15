from langchain_core.output_parsers import StrOutputParser
from prompts.jd_extract_prompt import jd_extract_prompt
from utils.config import get_llm

llm = get_llm()

jd_extract_chain = jd_extract_prompt | llm | StrOutputParser()