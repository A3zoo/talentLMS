from pydantic import BaseModel
from typing import List, Dict

class Question(BaseModel):
    id: str
    text: str
    type: str
    weight: str
    correct: str
    answers: Dict[str, str]
    correct_answers: Dict[str, str]
    user_answers: Dict[str, str]

class TestAnswer(BaseModel):
    test_id: str
    test_name: str
    user_id: str
    user_name: str
    score: str
    completion_status: str
    completed_on: str
    completed_on_timestamp: str
    total_time: str
    total_time_seconds: int
    questions: List[Question]




