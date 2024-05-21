from langchain.vectorstores.chroma import Chroma
from embedding.embeddings.openai import embeddings
#
# vector_store = Chroma.from_documents(
#     documents=docs,
#     embedding=embeddings,
#     persist_directory="emb"
# )
#
#
def create_vector_store(documents, embeddings):
    # 벡터 저장소의 디렉토리
    persist_directory = "emb"  # 여기에 실제 디렉토리 경로를 입력하세요.

    # Chroma 객체 생성
    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=persist_directory
    )

    return vector_store
