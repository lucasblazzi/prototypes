from typing import Literal
from app.config import logger
from app.states import AgentState


agent_docs = {
    "search_agent": search_agent.__doc__,
    "math_agent": math_agent.__doc__
}


def routing_logic(state: AgentState) -> Literal["math_agent", "search_agent"]:
    """
    Uses the LLM to choose between 'math_agent' and 'search_agent'
    based on the intent of the user query and the agents' docstrings.

    Args:
        state (AgentState): The current state containing the user query.

    Returns:
        str: The name of the next node to route to.
    """
    prompt = f"""
    You are a router agent. Your task is to choose the best agent for the job.
    Here is the user query: {state['user_query']}

    You can choose from the following agents:
    - math_agent: {agent_docs['math_agent']}
    - search_agent: {agent_docs['search_agent']}

    Which agent should handle this query? Respond with just the agent name.
    """
    response = llm.invoke(prompt)
    decision = response.content.strip().lower()
    return "math_agent" if "math" in decision else "search_agent"