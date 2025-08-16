from google.adk.agents import LlmAgent
from ...utils.parser import load_md
from ...models import OnboardingPlan
from google.adk.tools.transfer_to_agent_tool import transfer_to_agent


metadata = load_md("orbit/instructions/onboarding_agent_instruction.md")


def get_company_document(document_name: str) -> str:
    """
    Retrieves a company document.

    Args:
        document_name: The name of the document to retrieve.

    Returns:
        The content of the document.
    """
    if document_name == "employee_handbook":
        return "This is the employee handbook."
    elif document_name == "style_guide":
        return "This is the company style guide."
    else:
        return f"Document '{document_name}' not found."


def schedule_meeting(topic: str, participants: list[str]) -> str:
    """
    Schedules a meeting.

    Args:
        topic: The topic of the meeting.
        participants: A list of participants.

    Returns:
        A confirmation message.
    """
    return f"Meeting '{topic}' scheduled with {', '.join(participants)}."


def create_onboarding_agent():
    return LlmAgent(
        name="onboarding_agent_v1",
        model="gemini-2.0-flash",
        description=metadata["description"],
        instruction=metadata["instruction"].format(coordinator_name="PWCoordinator"),
        tools=[get_company_document, schedule_meeting, transfer_to_agent],
        # output_schema=OnboardingPlan,
        output_key="onboarding_plan"
    )

