from app.chat.embeddings.openai import embeddings
from langchain_community.vectorstores.chroma import Chroma

vector_store = Chroma(
    persist_directory="emb",
    embedding_function=embeddings,

)


def build_retriever(chat_args):
    search_kwargs = {"filter": {"pdf_id": chat_args.pdf_id}}
    return vector_store.as_retriever(
        search_kwargs=search_kwargs
    )
