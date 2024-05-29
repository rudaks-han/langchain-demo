from langchain.prompts import PromptTemplate
from datetime import datetime


# 방법 1: from_template을 사용하는 방법
def task1():
    template = "{task}을 수행하는 로직을 {language}으로 작성해 줘~"

    prompt_template = PromptTemplate.from_template(template)
    prompt = prompt_template.format(task="0부터 10까지 계산", language="파이썬")
    print(prompt)  # 0부터 10까지 계산을 수행하는 로직을 파이썬으로 작성해 줘~

    # 출력: 0부터 10까지 계산을 수행하는 로직을 파이썬으로 작성해 줘~


# 방법 2: PromptTemplate 객체 생성과 동시에 prompt 생성
def task2():
    template = "{task}을 수행하는 로직을 {language}으로 작성해 줘~"
    prompt_template = PromptTemplate(
        template=template,
        input_variables=["task", "language"],  # input_variables=[] 으로 해도 실행된다.
    )

    prompt = prompt_template.format(task="0부터 10까지 계산", language="파이썬")
    print(prompt)  # 0부터 10까지 계산을 수행하는 로직을 파이썬으로 작성해 줘~


def get_today():
    now = datetime.now()
    return now.strftime("%Y-%m-%d")


def partial_variable():
    prompt_template = PromptTemplate(
        template="오늘의 {today} 입니다. 그리고 {n}을 입력 받았습니다.",
        input_variables=["n"],
        partial_variables={"today": get_today},  # partial_variables에 함수를 전달
    )

    prompt = prompt_template.format(n=10)
    print(prompt)  # 오늘의 2024-05-29 입니다. 그리고 10을 입력 받았습니다.


from langchain_core.runnables import RunnablePassthrough


def runnable_passthorugh():
    prompt_template = PromptTemplate(
        template="오늘의 {today} 입니다. 그리고 {n}을 입력 받았습니다.",
        input_variables=["n"],
        partial_variables={"today": get_today},  # partial_variables에 함수를 전달
    )
    runnable_template = {"n": RunnablePassthrough()} | prompt_template
    prompt = runnable_template.invoke(5)
    print(prompt)

    # 아래 로직과 동일
    # runnable_template = {"n": RunnablePassthrough()}
    # runnable_template.update(prompt_template)
    # prompt = prompt_template.invoke(5)


if __name__ == "__main__":
    # task1()
    # task2()
    # partial_variable()
    runnable_passthorugh()


# 참고: https://wikidocs.net/233351
