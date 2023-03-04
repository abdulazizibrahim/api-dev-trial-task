from sqlalchemy import create_engine, delete
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import insert

from database.schemas.quiz import Quiz
from database.schemas.options import Options
from database.schemas.questions import Questions
from database.schemas.base import Base


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


    def upsertData(self, table: str, data: dict):
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



    def getData(self, table: str, id: str=None):
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
            stmt = self.session.query(MODEL_MAPPER[table]).filter(MODEL_MAPPER[table].id == id)
        result = (stmt).all()
        res = []
        for data in result:
            data = data.__dict__
            data.pop('_sa_instance_state')
            res.append(data)
        return res


    def deleteData(self, table: str, id: str):
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
        return True


    def getQuestionsFromQuiz(self, quiz_id: str):
        """_summary_
        This function returns questions associated with the
        provided quiz_id.
        Args:
            quiz_id (str): The id of the quiz.
        """
        result = (
            self.session.query(Questions)
            .filter(Questions.quizId == quiz_id)
            ).all()
        res = []
        for data in result:
            data = data.__dict__
            data.pop('_sa_instance_state')
            res.append(data)
        return res
    
    def getOptionsFromQuestion(self, question_id: str, verify=False):
        """_summary_
        This function returns questions associated with the
        provided quiz_id.
        Args:
            quiz_id (str): The id of the quiz.
        """
        stmt = self.session.query(Options).filter(Options.questionId == question_id)
        if verify:
            stmt = self.session.query(Options).filter((Options.questionId == question_id) & (Options.correct == True))

        result = (stmt).all()
        res = []
        for data in result:
            data = data.__dict__
            data.pop('_sa_instance_state')
            res.append(data)
        return res
