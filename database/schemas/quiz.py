from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from database.schemas.base import Base

class Quiz(Base):
    __tablename__ = 'quiz'

    id = Column(String, primary_key=True, nullable=False, unique=True)
    title = Column(String)
    description = Column(String)

    questions = relationship("Questions",  cascade="all,delete", backref="quiz")

    def get_set(self, stmt):

        return {
            "title": stmt.excluded.title,
            "description": stmt.excluded.description
        }