from langchain_openai.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_openai.chat_models import ChatOpenAI
from langchain.vectorstores.chroma import Chroma
from dotenv import load_dotenv
import langchain

langchain.debug = True
load_dotenv()

chat = ChatOpenAI()
embeddings = OpenAIEmbeddings()
db = Chroma(
    persist_directory="emb",
    embedding_function=embeddings
)

retriever = db.as_retriever()

chain = RetrievalQA.from_chain_type(
    llm=chat,
    retriever=retriever,
    chain_type="stuff"
)

print('[chain]')
print(chain)

result = chain.invoke("물가상승률을 고려하지 않은 금리이며 은행에서 제시하는 금리를 뭐라고 하나?")

print(result)
