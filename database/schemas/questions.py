from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from database.schemas.base import Base

class Questions(Base):
    __tablename__ = 'questions'

    id = Column(String, primary_key=True, nullable=False, unique=True)
    mandatory = Column(Boolean)
    questionStatement = Column(String)

    quizId = Column(String, ForeignKey('quiz.id'))
    options = relationship("Options", cascade="all,delete", backref="questions")

    def get_set(self, stmt):

        return {
            "mandatory": stmt.excluded.mandatory,
            "questionStatement": stmt.excluded.questionStatement,
            "quizId": stmt.excluded.quizId
        }
