from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter


def split_text():
    loader = TextLoader("sample.txt")
    document = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=8, chunk_overlap=0)
    texts = text_splitter.split_documents(document)

    for i, text in enumerate(texts):
        print(f"{i} : {text.page_content}")


if __name__ == "__main__":
    split_text()
