from google.adk.agents import LlmAgent
from ...utils.parser import load_md
from ...models import CoachAction
from google.adk.tools.transfer_to_agent_tool import transfer_to_agent


metadata = load_md("orbit/instructions/coach_agent_instruction.md")


import random


def get_motivational_quote() -> str:
    """
    Returns a motivational quote.

    Returns:
        A motivational quote.
    """
    quotes = [
        "The best way to predict the future is to create it.",
        "The only way to do great work is to love what you do.",
        "Success is not final, failure is not fatal: it is the courage to continue that counts."
    ]
    return random.choice(quotes)


def create_coach_agent():
    return LlmAgent(
        name="coach_agent_v1",
        model="gemini-2.0-flash",
        description=metadata["description"],
        instruction=metadata["instruction"].format(coordinator_name="PWCoordinator"),
        tools=[get_motivational_quote, transfer_to_agent],
        # output_schema=CoachAction,
        output_key="coach_action"
    )

