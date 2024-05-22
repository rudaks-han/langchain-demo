from langchain.embeddings.base import Embeddings
from langchain.vectorstores.chroma import Chroma
from langchain.schema import BaseRetriever


class RedundantFilterRetriever(BaseRetriever):
    embeddings: Embeddings
    chroma: Chroma

    def get_relevant_documents(self, query):
        # 'query'에 대해 embeddings 계산
        emb = self.embeddings.embed_query(query)

        # embedding을 가지고 max_marginal_relevance_search_by_vector에 주입
        return self.chroma.max_marginal_relevance_search_by_vector(
            embedding=emb, lambda_mult=0.8
        )

    async def aget_relevant_documents(self):
        return []
