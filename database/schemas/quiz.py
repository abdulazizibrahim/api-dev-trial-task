from sqlalchemy import Column, String

from schemas.base import Base

class Quiz(Base):
    __tablename__ = 'quiz'

    quizId = Column(String, primary_key=True, nullable=False, unique=True)
    title = Column(String)
    description = Column(String)