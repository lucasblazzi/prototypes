from pydantic import BaseModel


class ManagerInsight(BaseModel):
    insight: str
    severity: str  # info | warning | critical