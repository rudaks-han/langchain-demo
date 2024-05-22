from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings()

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=1,
    chunk_overlap=0
)

loader = TextLoader("경제상식.txt")
docs = loader.load_and_split(text_splitter=text_splitter)

db = Chroma.from_documents(docs, embedding=embeddings, persist_directory="emb")
# for doc in docs:
#     print("==========")
#     print(doc.page_content)
#     print("\n")

results = db.similarity_search_with_score(
    "한 나라의 경제 동향의 현상 분석 및 물가 실업률 고용율을 연구하는 것을 뭐라고 하나?"
)

for result in results:
    print("\n")
    print(result[1])
    print(result[0].page_content)
