from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from schemas.base import Base

class Options(Base):
    __tablename__ = 'options'

    id = Column(String, primary_key=True, nullable=False, unique=True)
    option = Column(String)
    correct = Column(Boolean)

    questionId = Column(String, ForeignKey('questions.id'))


    def get_set(self, stmt):

        return {
            "option": stmt.excluded.option,
            "correct": stmt.excluded.correct,
            "questionId": stmt.excluded.questionId
        }

