import datetime
from pydantic import BaseModel, field_validator

class AnswerCreate(BaseModel):
    content: str

    @field_validator("content")
    def not_empty(cls, v):
        if not v or not v.stript():
            raise ValueError("빈 값은 허용되지 않습니다.")
        return v
    
class Answer(BaseModel):
    id: int
    content: str
    created_date: datetime.datetime