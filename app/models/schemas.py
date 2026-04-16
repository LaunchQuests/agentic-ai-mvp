from pydantic import BaseModel

class GoalRequest(BaseModel):
    goal: str

class Task(BaseModel):
    description: str

class Result(BaseModel):
    output: str