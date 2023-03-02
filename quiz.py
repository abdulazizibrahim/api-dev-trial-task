from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Quiz(Base):
    __tablename__ = 'quiz'

    quizId = Column(String, primary_key=True, nullable=False, unique=True)
    title = Column(String)
    description = Column(String)