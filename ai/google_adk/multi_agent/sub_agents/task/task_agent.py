from google.adk.agents import LlmAgent
from ...utils.parser import load_md
from ...models import TaskSuggestion
from google.adk.tools.transfer_to_agent_tool import transfer_to_agent


metadata = load_md("orbit/instructions/task_agent_instruction.md")

def get_daily_tasks(user_id: str) -> list[str]:
    """
    Gets the user's tasks for the day.

    Args:
        user_id: The ID of the user.

    Returns:
        A list of tasks.
    """
    return ["Review PR #123", "Finish the design for the new feature", "Prepare for the team meeting"]


def create_task(title: str, description: str) -> str:
    """
    Creates a new task.

    Args:
        title: The title of the task.
        description: The description of the task.

    Returns:
        A confirmation message with the new task's ID.
    """
    return f"Task '{title}' created with ID 42."


def assign_task(task_id: str, user_id: str) -> str:
    """
    Assigns a task to a user.

    Args:
        task_id: The ID of the task.
        user_id: The ID of the user.

    Returns:
        A confirmation message.
    """
    return f"Task {task_id} assigned to user {user_id}."


def create_task_agent():
    return LlmAgent(
        name="task_agent_v1",
        model="gemini-2.0-flash",
        description=metadata["description"],
        instruction=metadata["instruction"].format(coordinator_name="PWCoordinator"),
        tools=[create_task, assign_task, transfer_to_agent],
        # output_schema=TaskSuggestion,
        output_key="task_suggestion"
    )

