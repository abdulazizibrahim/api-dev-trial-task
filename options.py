from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Options(Base):
    __tablename__ = 'options'

    optionId = Column(String, primary_key=True, nullable=False, unique=True)
    option = Column(String)

    questionId = Column(String, ForeignKey('questions.questionId'), nullable=False)
    questions = relationship("Questions", backref="options")

