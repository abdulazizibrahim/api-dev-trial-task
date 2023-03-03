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


DB_HANDLER = DatabaseHandler("localhost", "postgres", "postgres", "test-db")


def getQuiz(id: str):
    """_summary_
    This function returns quizes and its
    associated questions. If id is None it returns all available records,
    else it returns the specific record that macthes the id.
    Args:1
        id (str): The id of quiz to fetch a specific record.
    """
    quizes = DB_HANDLER.get_data("quiz", id)
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
    DB_HANDLER.upsert_data("quiz", temp)
    for question in quiz["questions"]:
        question["quiz_id"] = quiz["id"]
        DB_HANDLER.upsert_data("question", question)
        for option in question["options"]:
            option["question_id"] = question["id"]
            DB_HANDLER.upsert_data("options", option)

    return quiz


def deleteQuiz(id: str):
    """_summary_
    This function deletes the provided quiz
    and all its associated questions.
    Args:
        quiz (dict): A dict containing information of the quiz.
    """
    questions = DB_HANDLER.get_questions_from_quiz(id)
    for question in questions:
        options = DB_HANDLER.get_options_from_question(question["id"])
        for option in options:
            DB_HANDLER.delete_data("options", option["id"])
        DB_HANDLER.delete_data("questions", question["id"])
    quiz = DB_HANDLER.get_data("quiz", id)
    DB_HANDLER.delete_data("quiz", id)
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
    total = len(quiz["questions"])
    for question in quiz["questions"]:
        answer = {}
        answer["questionId"] = question["id"]
        answer["questionStatement"] = question["questionStatement"]
        record = DB_HANDLER.get_options_from_question(question["id"], verify=True)[0]
        answer["optionId"] = record["id"]
        answer["option"] = record["option"]
        if question["optionId"] == record["id"]:
            score += 1
        res["answers"].append(answer)
    res["score"] = f"{score}/{total}"
    return res
 
    
# getQuiz("e962aaff-772b-4964-bb6d-44b572e1d23g")
# DB_HANDLER.get_questions_from_quiz("e962aaff-772b-4964-bb6d-44b572e1d23g")
# print(DB_HANDLER.get_options_from_question("a8eb9ad4-3b68-4b7e-a000-26f0af8c0a8f", verify=True))
print(checkQuiz({
"questions":[
{
'questionStatement': 'This is question 2.',
 'id': 'a8eb9ad4-3b68-4b7e-a000-26f0af8c0a8f',
'optionId': '6cfa6e51-7200-4738-ba62-6c32444a720b',
'option': 'A'
}    
]
}))