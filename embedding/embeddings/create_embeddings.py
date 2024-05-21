from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
# from embedding.vector_stores.chromadb import vector_store
from langchain.vectorstores.chroma import Chroma
from embedding.embeddings.openai import embeddings

def create_embeddings_for_pdf(pdf_id: str, pdf_path: str):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    loader = PyPDFLoader(pdf_path)
    docs = loader.load_and_split(text_splitter)

    # print(docs)
    # vector_store.add_documents(docs)
    add_vector_store(docs, embeddings)


def create_embeddings_for_txt(txt_id: str, txt_path: str):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    #
    loader = TextLoader(txt_path)
    docs = loader.load_and_split(text_splitter)
    #
    # vector_store.add_documents(docs)
    add_vector_store(docs, embeddings)

def add_vector_store(docs, embeddings):
    Chroma.from_documents(docs, embedding=embeddings, persist_directory="emb")
