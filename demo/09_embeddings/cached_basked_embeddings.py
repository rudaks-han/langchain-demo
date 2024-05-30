from dotenv import load_dotenv
from langchain.storage import LocalFileStore
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.embeddings import CacheBackedEmbeddings


load_dotenv()

# OpenAI 임베딩을 사용하여 기본 임베딩 설정
embedding = OpenAIEmbeddings()

# 로컬 파일 저장소 설정
store = LocalFileStore("./cache/")

# 캐시를 지원하는 임베딩 생성
cached_embedder = CacheBackedEmbeddings.from_bytes_store(
    embedding,
    store,
    namespace=embedding.model,  # 기본 임베딩과 저장소를 사용하여 캐시 지원 임베딩을 생성
)

# store에서 키들을 순차적으로 가져옵니다.
list(store.yield_keys())

from langchain.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

# 문서 로드
raw_documents = TextLoader("./data/appendix-keywords.txt").load()
# 문자 단위로 텍스트 분할 설정
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
# 문서 분할
documents = text_splitter.split_documents(raw_documents)

# 코드 실행 시간을 측정합니다.
db = FAISS.from_documents(
    documents, cached_embedder
)  # 문서로부터 FAISS 데이터베이스 생성


# 캐싱된 임베딩을 사용하여 FAISS 데이터베이스 생성
db2 = FAISS.from_documents(documents, cached_embedder)

# VectorStore에서 처음 5개의 키를 가져옵니다.
list(store.yield_keys())[:5]
