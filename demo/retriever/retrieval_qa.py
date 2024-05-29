from dotenv import load_dotenv
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_openai.chat_models import ChatOpenAI
from langchain.vectorstores.chroma import Chroma
from langchain_openai import OpenAIEmbeddings
import langchain
langchain.debug = True

load_dotenv()


if __name__ == "__main__":
    print("Retrieving...")
    chat = ChatOpenAI()
    embeddings = OpenAIEmbeddings()

    db = Chroma(
        persist_directory="chroma_emb",
        embedding_function=embeddings
    )

    retriever = db.as_retriever()
    chain = RetrievalQA.from_chain_type(
        llm=chat,
        retriever=retriever,
        chain_type="stuff"
    )

    result = chain.invoke("주식 시장이란 무엇인가?")
    print(result)
