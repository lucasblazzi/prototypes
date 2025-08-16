from typing import List, TypedDict


class AgentState(TypedDict):
    text: str
    classification: str
    entities: List[str]
    summary: str