from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Questions(Base):
    __tablename__ = 'questions'

    questionId = Column(String, primary_key=True, nullable=False, unqiue=True)
    mandatory = Column(Boolean)
    questionStatement = Column(String)

    correctAnswer = Column(String, ForeignKey('options.optionId'), nullable=False)
    options = relationship("Options", backref="questions")