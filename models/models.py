from dataclasses import dataclass
from typing import List, Optional
from pydantic import BaseModel

class Options(BaseModel):
    id: Optional[str]
    option: str
    correct: bool
    questionId: Optional[str]


class Questions(BaseModel):
    id: Optional[str]
    mandatory: bool
    questionStatement: str
    quizId: Optional[str]
    options : Optional[List[Options]] = []
    
 
class Quiz(BaseModel):
    id: Optional[str]
    title: str
    description: str
    questions: Optional[List[Questions]] = []


class VerifyAnswer(BaseModel):
    questionId: str
    questionStatement: str
    optionId: str
    option: str

class Answers(BaseModel):
    answers: List[VerifyAnswer]

@dataclass
class BaseResponse:
    success: bool
    errors: Optional[str] = None
    data: Optional[dict] = None
