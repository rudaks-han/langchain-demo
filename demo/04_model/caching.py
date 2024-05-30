from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.cache import SQLiteCache
from langchain.globals import set_llm_cache
import langchain

langchain.debug = True

load_dotenv()
set_llm_cache(SQLiteCache(database_path="my_llm_cache.db"))

llm = ChatOpenAI()

prompt = PromptTemplate.from_template("{country} 에 대해서 20자 내외로 요약해줘")

chain = prompt | llm

response = chain.invoke({"country": "한국"})
print(response.content)
