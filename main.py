from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--task", default="Return a list of numbers")
parser.add_argument("--language", default="python")
args = parser.parse_args()

api_key = "sk-xxx"

llm = OpenAI(
    openai_api_key=api_key,
)

# code template을 만든다.
code_prompt = PromptTemplate(
    # task, language는 변수로 사용되고 매개변수의 값으로 치환이 된다.
    template="Write a very short {language} function that will {task}",
    # input_variables로 변수를 나타낸다.
    input_variables=["language", "task"],
)

# chain을 만드는 데 code_prompt를 사용한다.
code_chain = LLMChain(
    llm=llm,
    prompt=code_prompt
)

result = code_chain.invoke({
    "language": args.language,
    "task": args.task
})

#result = llm.invoke("짧은 농담 하나 해줘~")
print(result['text'])
