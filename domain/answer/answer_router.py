from fastapi import Depends, APIRouter, HTTPException
from databases import get_db
from starlette import status
from sqlalchemy.orm import Session

from .answer_schema import AnswerCreate
from . import answer_crud
from domain.question import question_crud

router = APIRouter(prefix="/api/answer")

@router.post('/{question_id}', status_code=status.HTTP_204_NO_CONTENT)
def create_answer(question_id: int, answer_create: AnswerCreate, db: Session = Depends(get_db)):
    question = question_crud.get_question(db=db, question_id=question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return answer_crud.create_answer(question=question, answer_create=answer_create, db=db)