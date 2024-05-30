from dotenv import load_dotenv
from langchain.vectorstores.chroma import Chroma
from langchain_openai import OpenAIEmbeddings
import langchain
langchain.debug = True

load_dotenv()


if __name__ == "__main__":
    embeddings = OpenAIEmbeddings()

    db = Chroma(
        persist_directory="chroma_emb",
        embedding_function=embeddings
    )

    retriever = db.as_retriever()
    docs = retriever.invoke("Python은 무엇인가?")
