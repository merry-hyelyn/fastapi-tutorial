from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from databases import Base


class Question(Base):
    __tablename__ = "question"
    
    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=True)
    content = Column(Text, nullable=True)
    create_date = Column(DateTime, nullable=False)


class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True)  # null 허용
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    question_id = Column(Integer, ForeignKey("question.id"))
    question = relationship("Question", backref="answers")
