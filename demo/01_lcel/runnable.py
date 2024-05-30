from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


def base():
    prompt = PromptTemplate.from_template("{num} x 2는?")
    llm = ChatOpenAI()

    chain = prompt | llm | StrOutputParser()

    response = chain.invoke({"num": 3})
    print(response)


def runnable_passthrough():
    prompt = PromptTemplate.from_template("{num} x 2는?")
    llm = ChatOpenAI()

    chain = {"num": RunnablePassthrough()} | prompt | llm | StrOutputParser()

    response = chain.invoke(3)
    print(response)


def runnable_parallel():
    chain1 = (
        {"num": RunnablePassthrough()}
        | PromptTemplate.from_template("{num} 의 10배는?\n답변(결과만): ")
        | ChatOpenAI()
        | StrOutputParser()
    )
    chain2 = (
        {"num": RunnablePassthrough()}
        | PromptTemplate.from_template("{num} 의 1/10배는?\n답변(결과만): ")
        | ChatOpenAI()
        | StrOutputParser()
    )

    combined_chain = RunnableParallel(a=chain1, b=chain2)
    result = combined_chain.invoke({"num": 10})

    print(result)


def runnable_lambda():
    chain = (
        {"num": lambda x: x * 2}
        | PromptTemplate.from_template("{num} 의 10배는?\n답변(결과만): ")
        | ChatOpenAI()
        | StrOutputParser()
    )

    result = chain.invoke(10)
    print(result)


if __name__ == "__main__":
    # base()
    # runnable_passthrough()
    # runnable_parallel()
    runnable_lambda()
