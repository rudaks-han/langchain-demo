from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings


load_dotenv()

# OpenAI의 "text-embedding-3-large" 모델을 사용하여 임베딩을 생성합니다.
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

text = (
    "임베딩 테스트를 하기 위한 샘플 문장입니다."  # 테스트용 문서 텍스트를 정의합니다.
)

query_result = embeddings.embed_query(text)

print(query_result[:5])
