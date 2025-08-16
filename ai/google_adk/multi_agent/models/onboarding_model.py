from pydantic import BaseModel


class OnboardingPlan(BaseModel):
    missions: list[str]
    notification_cadence_hours: int