from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from schemas.base import Base

class Questions(Base):
    __tablename__ = 'questions'

    questionId = Column(String, primary_key=True, nullable=False, unique=True)
    mandatory = Column(Boolean)
    questionStatement = Column(String)

    correctAnswer = Column(String, ForeignKey('options.optionId'))
    options = relationship("Options", backref="questions", cascade="all, delete")