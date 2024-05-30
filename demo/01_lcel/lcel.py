# API KEY를 환경변수로 관리하기 위한 설정 파일
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser


# API KEY 정보로드
load_dotenv()


def format():
    template = "{country}의 수도는 어디인가요?"

    prompt_template = PromptTemplate.from_template(template)
    prompt = prompt_template.format(country="한국")
    llm = ChatOpenAI()
    result = llm.invoke(prompt)
    print(result)


def lcel_format():
    template = "{country}의 수도는 어디인가요?"

    prompt = PromptTemplate.from_template(template)

    llm = ChatOpenAI()
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser

    result = chain.invoke({"country": "한국"})
    print(result)


if __name__ == "__main__":
    format()
    # lcel_format()
