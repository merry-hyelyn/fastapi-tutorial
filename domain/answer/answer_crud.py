from datetime import datetime

from sqlalchemy.orm import Session

from .answer_schema import AnswerCreate
from models import Question, Answer


def create_answer(db: Session, question: Question, answer_create: AnswerCreate):
    answer = Answer(content=answer_create.content, 
                    question=question,
                    create_date=datetime.now())
    db.add(answer)
    db.commit()