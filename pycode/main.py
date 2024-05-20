from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
import argparse
from dotenv import load_dotenv

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("--task", default="Return a list of numbers")
parser.add_argument("--language", default="python")
args = parser.parse_args()

llm = OpenAI()

# code template을 만든다.
code_prompt = PromptTemplate(
    # input_variables로 변수를 나타낸다.
    input_variables=["language", "task"],
    # task, language는 변수로 사용되고 매개변수의 값으로 치환이 된다.
    template="Write a very short {language} function that will {task}",
)

test_prompt = PromptTemplate(
    input_variables=["language", "code"],
    template="Write a test for the following {language} function:\n{code}"
)

# chain을 만드는 데 code_prompt를 사용한다.
code_chain = LLMChain(
    llm=llm,
    prompt=code_prompt,
    output_key="code"
)

test_chain = LLMChain(
    llm=llm,
    prompt=test_prompt,
    output_key="test"
)

# code_chain과 test_chain을 차례로 연결한다.
chain = SequentialChain(
    chains=[code_chain, test_chain],
    input_variables=["task", "language"],
    output_variables=["test", "code"]
)

result = chain.invoke({
    "language": args.language,
    "task": args.task
})
# result = code_chain.invoke({
#     "language": args.language,
#     "task": args.task
# })

#result = llm.invoke("짧은 농담 하나 해줘~")
print("[code]")
print(result["code"])

print("[test]")
print(result["test"])

