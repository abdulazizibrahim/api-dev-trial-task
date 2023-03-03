from sqlalchemy import create_engine, delete
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import insert

from schemas.quiz import Quiz
from schemas.options import Options
from schemas.questions import Questions
from schemas.base import Base


MODEL_MAPPER = {
    "quiz": Quiz,
    "questions": Questions,
    "options": Options
}
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
                "id": stmt.excluded.id,
                "title": stmt.excluded.title,
                "description": stmt.excluded.description
            }
        )

        self.session.execute(stmt)
        self.session.commit()
        return quiz


    def upsert_data(self, table: str, data: dict):
        """_summary_
        This function updates and inserts a record into the provided table.
        Args:
            table(str): The name of the table to which we want to upsert data.
            quiz (dict): A dictionary containing records of quiz.
        """

        stmt = insert(MODEL_MAPPER[table]).values(data)

        model = MODEL_MAPPER[table]()
        stmt = stmt.on_conflict_do_update(
            constraint = f"{table}_pkey",
            set_= model.get_set(stmt)
        )

        self.session.execute(stmt)
        self.session.commit()
        return data



    def get_data(self, table: str, id: str=None):
        """_summary_
        This function gets all the data from the provided table
        if the id is not provided. If the id is provided it fetches
        that specific record.
        Args:
            table (str): The name of table for which the data is required.
            id (str, optional): Optional field to fetch any specific record from the table.
        """
        
        stmt = self.session.query(MODEL_MAPPER[table])
        if id:
            stmt.filter(MODEL_MAPPER[table].id == id)
        result = (stmt).all()
        res = []
        for data in result:
            data = data.__dict__
            data.pop('_sa_instance_state')
            res.append(data)
        return res


    def delete_data(self, table: str, id: str):
        """_summary_
        This function deletes a record of the provided
        table based on the provided id.
        Args:
            table (str): _description_
            id (str): _description_
        """
        res = delete(MODEL_MAPPER[table]).where(MODEL_MAPPER[table].id == id)
        self.session.execute(res)
        self.session.commit()
        return res



db = DatabaseHandler("localhost", "postgres", "postgres", "test-db")
quiz = {
    "id": "e962aaff-772b-4964-bb6d-44b572e1d23g",
    "title": "This is Quiz 3 of Computer Science.",
    "description": "This Quiz will comprise of general SAS concepts."
}

question = {
    "id": "a8eb9ad4-3b68-4b7e-a000-26f0af8c0a8f",
    "questionStatement": "This is question 2.",
    "mandatory": True,
    "quizId": "e962aaff-772b-4964-bb6d-44b572e1d23g"
}
options = {
    "id": "6cfa6e51-7200-4738-ba62-6c32444a720d",
    "option": "C",
    "correct": False,
    "questionId": "a8eb9ad4-3b68-4b7e-a000-26f0af8c0a8f"
}
# print(db.upsert_data("options", options))
# print(db.get_data("quiz"))
print(db.delete_data("quiz", "e962aaff-772b-4964-bb6d-44b572e1d23g"))