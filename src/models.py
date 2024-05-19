from pydantic import BaseModel


class Question(BaseModel):
    question: str
    answer: str


class Team(BaseModel):
    name: str
    members: list[str]
