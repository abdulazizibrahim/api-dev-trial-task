from dataclasses import dataclass
from typing import List, Dict, Union, Optional
from pydantic import BaseModel, root_validator, conlist

from fastapi import HTTPException


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
    options : List[Options]


class Quiz(BaseModel):
    id: Optional[str]
    title: str
    description: str
    questions: List[Questions]


# class Data:
#     quiz: Optional[List[Quiz]]
#     questions: Optional[List[Questions]]
#     options: Optional[List[Options]]
#     status: Optional[str]


@dataclass
class BaseResponse:
    success: bool
    errors: Optional[str] = None
    data: Optional[dict] = None
