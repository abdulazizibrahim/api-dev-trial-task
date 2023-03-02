from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from schemas.base import Base

class Options(Base):
    __tablename__ = 'options'

    optionId = Column(String, primary_key=True, nullable=False, unique=True)
    option = Column(String)

    questionId = Column(String, ForeignKey('questions.questionId'))
    questions = relationship("Questions", backref="options", cascade="all, delete")

