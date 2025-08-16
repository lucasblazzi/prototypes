from typing import Dict, TypedDict


class AgentState(TypedDict):
    user_input: str
    header: Dict
    entities: list[str]
    summary: str