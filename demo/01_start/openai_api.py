from dotenv import load_dotenv
from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# API KEY 정보로드
load_dotenv()


# print(openai.__version__)


# 객체 생성
llm = ChatOpenAI(
    temperature=0.1,  # 창의성 (0.0 ~ 2.0)
    max_tokens=2048,  # 최대 토큰수
    model_name="gpt-3.5-turbo",  # 모델명
)

# 질의내용
question = "대한민국의 수도는 어디인가요?"


def base():
    result = llm.invoke(question)
    print(result.content)


def prompt_template_and_chain():
    # 질문 템플릿 형식 정의
    template = "{country}의 수도는 뭐야?"

    # 템플릿 완성
    prompt = PromptTemplate.from_template(template=template)
    chain = LLMChain(prompt=prompt, llm=llm)
    result = chain.invoke({"country": "대한민국"})
    print(result["text"])


def multiple_input():
    input_list = [{"country": "호주"}, {"country": "중국"}, {"country": "네덜란드"}]
    template = "{country}의 수도는 뭐야?"
    prompt = PromptTemplate.from_template(template=template)
    chain = LLMChain(prompt=prompt, llm=llm)
    result = chain.apply(input_list)

    print(result)


def multiple_input_variable():
    template = "{area1} 와 {area2} 의 시차는 몇시간이야?"

    # 템플릿 완성
    prompt = PromptTemplate.from_template(template)
    # 연결된 체인(Chain)객체 생성
    llm_chain = LLMChain(prompt=prompt, llm=llm)

    input_list = [
        {"area1": "파리", "area2": "뉴욕"},
        {"area1": "서울", "area2": "하와이"},
        {"area1": "켄버라", "area2": "베이징"},
    ]

    result = llm_chain.apply(input_list)
    for res in result:
        print(res["text"].strip())


def streaming():
    from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

    # 객체 생성
    llm = ChatOpenAI(
        temperature=0,  # 창의성 (0.0 ~ 2.0)
        max_tokens=2048,  # 최대 토큰수
        model_name="gpt-3.5-turbo",  # 모델명
        streaming=True,
        callbacks=[StreamingStdOutCallbackHandler()],
    )

    # 질의내용
    question = "대한민국에 대해서 300자 내외로 최대한 상세히 알려줘"

    # 스트리밍으로 답변 출력
    response = llm.invoke(question)
    print(response.content)


if __name__ == "__main__":
    # base()
    # prompt_template_and_chain()
    # multiple_input()
    # multiple_input_variable()
    streaming()
