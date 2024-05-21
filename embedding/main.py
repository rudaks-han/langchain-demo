from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma
# from dotenv import load_dotenv
from create_embeddings import create_embeddings_for_txt

# load_dotenv()

create_embeddings_for_txt("123", "경제상식.txt")

# text_splitter = CharacterTextSplitter(
#     separator="\n",
#     chunk_size=1,
#     chunk_overlap=0
# )
# loader = TextLoader("경제상식.txt")
# docs = loader.load_and_split(
#     text_splitter=text_splitter
# )
#
# # for doc in docs:
# #     print("==========")
# #     print(doc.page_content)
# #     print("\n")
#
# embeddings = OpenAIEmbeddings()
#
# db = Chroma.from_documents(
#     docs,
#     embedding=embeddings,
#     persist_directory="emb"
# )
#
# results = db.similarity_search_with_score(
#     "물가상승률을 고려하지 않은 금리이며 은행에서 제시하는 금리를 뭐라고 하나?"
# )
#
# for result in results:
#     print("\n")
#     print(result[1])
#     print(result[0].page_content)
