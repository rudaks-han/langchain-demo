from dotenv import load_dotenv
from langchain_google_community import GoogleDriveLoader
from langchain_community.document_loaders import UnstructuredFileIOLoader

load_dotenv()

loader = GoogleDriveLoader(
    folder_id="1v5ghuHtPR5GnD8qV60_JUhDZFMgKVB3nvN1uI9Tia0U",
    file_types=["sheet"],
    # file_loader_cls=UnstructuredFileIOLoader,
    recursive=False,
)

docs = loader.load()
print(docs)

