from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from .question_schema import Question, QuestionCreate
from . import question_crud
from databases import SessionLocal, get_db

router = APIRouter(prefix='/api/question',)

@router.get('/', response_model=list[Question])
def question_list(db: Session = Depends(get_db)):
    _question_list = question_crud.get_question_list(db)
    return _question_list

@router.get('/{question_id}', response_model=Question)
def question_detial(question_id: int, db: Session = Depends(get_db)):
    _question = question_crud.get_question(db, question_id)
    return _question


@router.post('/', status_code=status.HTTP_204_NO_CONTENT)
def question_create(new_question: QuestionCreate, db: Session = Depends(get_db)):
    question_crud.create_question(db=db, new_question=new_question)
    