from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import (
    CharacterTextSplitter,
    TokenTextSplitter,
    KonlpyTextSplitter,
    SentenceTransformersTokenTextSplitter,
)


def split_text():
    loader = TextLoader("sample.txt")
    document = loader.load()

    # text_splitter = TokenTextSplitter(chunk_size=8, chunk_overlap=0)
    # text_splitter = KonlpyTextSplitter(separator="\n\n")
    text_splitter = SentenceTransformersTokenTextSplitter(chunk_size=8, chunk_overlap=0)
    texts = text_splitter.split_documents(document)

    for i, text in enumerate(texts):
        print(f"{i} : {text.page_content}")


if __name__ == "__main__":
    split_text()
