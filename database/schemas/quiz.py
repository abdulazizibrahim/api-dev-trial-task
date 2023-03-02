from sqlalchemy import Column, String

from schemas.base import Base

class Quiz(Base):
    __tablename__ = 'quiz'

    id = Column(String, primary_key=True, nullable=False, unique=True)
    title = Column(String)
    description = Column(String)


    def get_set(self, stmt):

        return {
            "title": stmt.excluded.title,
            "description": stmt.excluded.description
        }