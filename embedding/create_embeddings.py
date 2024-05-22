from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.chroma import Chroma
from langchain_community.document_loaders import TextLoader

from embeddings.openai import embeddings


def create_embeddings_for_txt(txt_id: str, txt_path: str):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    #
    loader = TextLoader(txt_path)
    docs = loader.load_and_split(text_splitter)
    # print(docs)

    Chroma.from_documents(
        docs,
        embedding=embeddings,
        persist_directory="emb"
    )

