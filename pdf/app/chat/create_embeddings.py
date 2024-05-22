from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
# from app.chat.vector_stores.pinecone import vector_store
from app.chat.vector_stores.chroma import vector_store

def create_embeddings_for_pdf(pdf_id: str, pdf_path: str):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    loader = PyPDFLoader(pdf_path)
    docs = loader.load_and_split(text_splitter)

    for doc in docs:
        doc.metadata = {
            "page": doc.metadata["page"],
            "text": doc.page_content,
            "pdf_id": pdf_id,
        }


    # for i, doc in enumerate(docs):
    #     print(f"Document {i+1}:")
    #     print("--------------------")
    #     print(doc.page_content)
    #     print(doc.metadata)
    #     print("\n")

    vector_store.add_documents(docs)
