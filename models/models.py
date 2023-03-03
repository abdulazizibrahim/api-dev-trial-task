from dataclasses import dataclass
from typing import List, Optional
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
    options : Optional[List[Options]] = []
    
    @root_validator()
    @classmethod
    def populate_segments_exists(cls, values):
        """
        Validate that segment export should only be
        generated for a single message type.
        """

        count = 0
        for option in values["options"]:
            if option["correct"]:
                count +=1
        if count != 1:
            raise HTTPException(success=422,
                                detail="There can only be one correct answer")

        return values


class Quiz(BaseModel):
    id: Optional[str]
    title: str
    description: str
    questions: Optional[List[Questions]] = []


@dataclass
class BaseResponse:
    success: bool
    errors: Optional[str] = None
    data: Optional[dict] = None
