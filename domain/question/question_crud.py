from datetime import datetime
from models import Question
from sqlalchemy.orm import Session
from .question_schema import QuestionCreate

def get_question_list(db: Session):
    question_list = db.query(Question).order_by(
        Question.create_date.desc()
    ).all()
    return question_list


def get_question(db: Session, question_id: int):
    question = db.query(Question).get(question_id)
    return question

def create_question(db: Session, new_question: QuestionCreate):
    question = Question(
        subject=new_question.subject, 
        content=new_question.content, 
        create_date=datetime.now())
    db.add(question)
    db.commit()