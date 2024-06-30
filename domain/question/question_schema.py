'''
pydantic은 fastapi의 입출력 스펙을 정의하고 그 값을 검증하기 위해 사용

'''
import datetime

from pydantic import BaseModel, field_validator
from domain.answer.answer_schema import Answer

# Question schema
class Question(BaseModel):
    id: int
    subject: str | None = None
    content: str
    create_date: datetime.datetime
    # answers: list[Answer] = [] --> list에서는 에러가 발생한다..?

class QuestionCreate(BaseModel):
    subject: str | None = None
    content: str

    @field_validator('subject', 'content')
    def not_empty(cls , v):
        if not v or not v.strip():
            raise ValueError("빈 값은 허용되지 않습니다.")
        return v