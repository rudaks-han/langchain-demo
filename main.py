from langchain_openai import OpenAI

api_key = "sk-xxx"

llm = OpenAI(
    openai_api_key=api_key,
)

result = llm.invoke("짧은 농담 하나 해줘~")
print(result)
