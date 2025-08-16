from pydantic import BaseModel


class CoachAction(BaseModel):
    action: str  # encourage | remind | explain
    message: str