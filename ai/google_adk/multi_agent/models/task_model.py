from pydantic import BaseModel


class TaskSuggestion(BaseModel):
    title: str
    description: str
    acceptance_criteria: list[str]
    tags: list[str]