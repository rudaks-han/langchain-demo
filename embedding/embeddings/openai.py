from dotenv import load_dotenv
from langchain_openai.embeddings import OpenAIEmbeddings

load_dotenv()

embeddings = OpenAIEmbeddings()
