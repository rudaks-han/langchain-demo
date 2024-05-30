import langchain
from dotenv import load_dotenv
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.pydantic_v1 import Field
from langchain_openai import ChatOpenAI
from pydantic import BaseModel
from typing import List

langchain.debug = True

load_dotenv()


class MatchResult(BaseModel):
    winner_team: str = Field(description="승자팀")
    winner_team_score: str = Field(description="승자팀 점수")
    loser_team: str = Field(description="패자팀")
    loser_team_score: str = Field(description="패자팀 점수")
    money: str = Field(description="패자팀 벌금")


class MatchSummary(BaseModel):
    date: str = Field(description="date with the format YYYY.MM.DD")
    match_result: List[MatchResult] = Field(description="경기 결과")


llm = ChatOpenAI(temperature=0)
parser = PydanticOutputParser(pydantic_object=MatchSummary)

match_result = """
날짜: 2024.05.13, 패자팀: 한경만, 허동혁, 패자팀 점수: 4점, 패자팀 벌금: ₩1,000원, 승자팀: 김상현, 김지훈, 승자팀 점수: 11점
날짜: 2024.05.13, 패자팀: 김상현, 김지훈, 패자팀 점수: 5점, 패자팀 벌금: ₩1,000원, 승자팀: 박은규, 한경만, 승자팀 점수: 11점
날짜: 2024.05.13, 패자팀: 박은규, 한경만, 패자팀 점수: 5점, 패자팀 벌금: ₩1,000원, 승자팀: 김지훈, 허동혁, 승자팀 점수: 11점
"""

prompt = PromptTemplate.from_template(
    """
You are a helpful assistant. Please answer the following questions in KOREAN.

QUESTION:
{question}

경기 전적 결과:
{match_result}

FORMAT:
{format}
"""
)
prompt = prompt.partial(format=parser.get_format_instructions())

question = "5월 13일 경기 결과 알려줘"

# print(prompt)
chain = prompt | llm
response = chain.invoke(
    {
        "match_result": match_result,
        "question": question,
    }
)
print(response.content)
