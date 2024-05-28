from dotenv import load_dotenv
from langchain.storage import InMemoryStore, LocalFileStore, create_kv_docstore
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.retrievers import ParentDocumentRetriever
import langchain
langchain.debug = True

load_dotenv()

loaders = [
    TextLoader("./data/보험약관.txt"),
]
docs = []  # 빈 리스트를 생성합니다.
for loader in loaders:  # loaders 리스트의 각 로더에 대해 반복합니다.
    docs.extend(
        loader.load()
    )  # 로더를 사용하여 문서를 로드하고 docs 리스트에 추가합니다.

parent_splitter = RecursiveCharacterTextSplitter(chunk_size=900)
# 자식 분할기를 생성합니다.
child_splitter = RecursiveCharacterTextSplitter(chunk_size=300)

# DB를 생성합니다.
vectorstore = Chroma(
    collection_name="split_parents", embedding_function=OpenAIEmbeddings()
)

store = InMemoryStore()
fs = LocalFileStore(root_path="./file_store")
store = create_kv_docstore(fs)

# Retriever 를 생성합니다.
retriever = ParentDocumentRetriever(
    vectorstore=vectorstore,
    docstore=store,
    child_splitter=child_splitter,
    parent_splitter=parent_splitter
)

# 문서를 검색기에 추가합니다. docs는 문서 목록이고, ids는 문서의 고유 식별자 목록입니다.
retriever.add_documents(docs)

# 저장소의 모든 키를 리스트로 반환합니다.
list(store.yield_keys())

# 유사도 검색을 수행합니다.
question = "사람이 죽는 경우 보상이 돼?"
sub_docs = vectorstore.similarity_search(question)

# sub_docs 리스트의 첫 번째 요소의 page_content 속성을 출력합니다.
print(f"결과 개수: {len(sub_docs)}")
print(sub_docs)

# for sub_doc in sub_docs:
#     print("______")
#     print(sub_doc.page_content)

retrieved_docs = retriever.invoke(question)
print(f"retrieved_docs 결과 개수: {len(retrieved_docs)}")
print(retrieved_docs)
