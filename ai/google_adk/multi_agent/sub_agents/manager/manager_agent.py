from google.adk.agents import LlmAgent
from ...utils.parser import load_md
from ...models import ManagerInsight
from google.adk.tools.transfer_to_agent_tool import transfer_to_agent


metadata = load_md("orbit/instructions/manager_agent_instruction.md")


def get_team_performance(team_id: str) -> str:
    """
    Gets a team's performance report.

    Args:
        team_id: The ID of the team.

    Returns:
        The team's performance report.
    """
    return f"Team {team_id} is performing well."


def approve_leave_request(request_id: str) -> str:
    """
    Approves a leave request.

    Args:
        request_id: The ID of the leave request.

    Returns:
        A confirmation message.
    """
    return f"Leave request {request_id} approved."


def create_manager_agent():
    return LlmAgent(
        name="manager_agent_v1",
        model="gemini-2.0-flash",
        description=metadata["description"],
        instruction=metadata["instruction"].format(coordinator_name="PWCoordinator"),
        tools=[get_team_performance, approve_leave_request, transfer_to_agent],
        # output_schema=ManagerInsight,
        output_key="manager_insight"
    )

