from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import insert

from schemas.quiz import Quiz
from schemas.options import Options
from schemas.questions import Questions
from schemas.base import Base


class DatabaseHandler:

    def __init__(self, host: str, user_name: str, password: str, database_name: str):
        """_summary_
        The function creates connection with the database.
        Args:
            host (str): The database host url.
            user_name (str): The database user.
            password (str): The database password
            database_name (str): The database to connect with.
        """
        engine = create_engine(
            "postgresql://"
            + user_name
            + ":"
            + password
            + "@"
            + host
            + ":5432/"
            + database_name
            + ""
        )
        
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)
        self.session = session()


    def upsert_quiz(self, quiz: dict):
        """_summary_
        This function updates and inserts a record into the quiz table.
        Args:
            quiz (dict): A dictionary containing records of quiz
        """

        stmt = insert(Quiz).values(quiz)

        stmt = stmt.on_conflict_do_update(
            constraint = "quiz_pkey",
            set_={
                "quizId": stmt.excluded.quizId,
                "title": stmt.excluded.title,
                "description": stmt.excluded.description
            }
        )

        self.session.execute(stmt)
        self.session.commit()
        return quiz

db = DatabaseHandler("localhost", "postgres", "postgres", "test")
quiz = {
    "quizId": "e962aaff-772b-4964-bb6d-44b572e1d23f",
    "title": "This is Quiz 2 of Computer Science.",
    "description": "This Quiz will comprise of general OOP concepts."
}
print(db.insert_quiz(quiz))