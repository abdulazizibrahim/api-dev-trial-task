import os
import sys
from copy import copy
PROJECT_ROOT = os.path.abspath(
                os.path.join(
                    os.path.dirname(__file__),
                    os.pardir)
)
sys.path.append(PROJECT_ROOT)
from database.database_handler import DatabaseHandler
from config.config import DATABASE, DATABASE_HOST
from config.config import DATABASE_USER, DATABASE_PASSWORD


DB_HANDLER = DatabaseHandler(DATABASE_HOST, DATABASE_USER, DATABASE_PASSWORD, DATABASE)


def getQuiz(id: str):
    """_summary_
    This function returns quizes and its
    associated questions. If id is None it returns all available records,
    else it returns the specific record that macthes the id.
    Args:1
        id (str): The id of quiz to fetch a specific record.
    """
    quizes = DB_HANDLER.getData("quiz", id)
    for quiz in quizes:
        quiz["questions"] = DB_HANDLER.get_questions_from_quiz(quiz["id"])
        for question in quiz["questions"]:
            question["options"] = DB_HANDLER.get_options_from_question(question["id"])
    return quizes


def upsertQuiz(quiz: dict):
    """_summary_
    This function updates and creates a quiz.
    Args:
        quiz (dict): A dict containg quiz information
    """
    temp = copy(quiz)
    temp.pop("questions")
    DB_HANDLER.upsertData("quiz", temp)
    for question in quiz["questions"]:
        question["quizId"] = quiz["id"]
        temp2 = copy(question)
        temp2.pop("options")
        DB_HANDLER.upsertData("questions", temp2)
        for option in question["options"]:
            option["questionId"] = question["id"]
            DB_HANDLER.upsertData("options", option)

    return quiz


def deleteQuiz(id: str):
    """_summary_
    This function deletes the provided quiz
    and all its associated questions.
    Args:
        quiz (dict): A dict containing information of the quiz.
    """
    questions = DB_HANDLER.getQuestionsFromQuiz(id)
    for question in questions:
        options = DB_HANDLER.getOptionsFromQuestion(question["id"])
        for option in options:
            DB_HANDLER.deleteData("options", option["id"])
        DB_HANDLER.deleteData("questions", question["id"])
    quiz = DB_HANDLER.getData("quiz", id)
    DB_HANDLER.deleteData("quiz", id)
    if not quiz:
        quiz = "No record exists for the provided id."
    return quiz 


def checkQuiz(quiz: dict):
    """_summary_
    This function verifies the answers of the quiz
    and returns the score.
    Args:
        quiz (dict): A dict containing information of the quiz.
    """
    res = {}
    res["answers"] = []
    score = 0
    total = len(quiz["answers"])
    for question in quiz["answers"]:
        answer = {}
        answer["questionId"] = question["questionId"]
        answer["questionStatement"] = question["questionStatement"]
        record = DB_HANDLER.getOptionsFromQuestion(question["questionId"], verify=True)[0]
        answer["optionId"] = record["id"]
        answer["option"] = record["option"]
        if question["optionId"] == record["id"]:
            score += 1
        res["answers"].append(answer)
    res["score"] = f"{score}/{total}"
    return res
 
