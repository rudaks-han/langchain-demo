# pip install --upgrade --quiet  langchain-google-genai pillow

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-pro")

result = llm.invoke("자연어처리에 대해서 간략히 설명해 줘")
print(result.content)
