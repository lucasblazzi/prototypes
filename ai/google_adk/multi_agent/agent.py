import os
import asyncio
from loguru import logger
from google.adk.agents import LlmAgent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from .sub_agents import (
    create_onboarding_agent,
    create_coach_agent,
    create_task_agent,
    create_manager_agent
)
from google.genai import types
from google.adk.tools.transfer_to_agent_tool import transfer_to_agent


def say_hello(name: str):
    """
    Say hello

    Args:
        name: The name of the user

    Returns:
        str: A greeting message
    """
    return f"Hello, {name}! How can I help you today?"


def say_goodbye(name: str):
    """
    Say goodbye

    Args:
        name: The name of the user

    Returns:
        str: A goodbye message
    """
    return f"Goodbye, {name}! See you next time!"


onboarding_agent = create_onboarding_agent()
coach_agent = create_coach_agent()
task_agent = create_task_agent()
manager_agent = create_manager_agent()


coordinator = LlmAgent(
    name="PWCoordinator",
    model="gemini-2.0-flash",
    description="Roteia qualquer evento para o agente especialista.",
    instruction="""
        Decida para qual sub-agente delegar:
          - onboarding_*  → OnboardingGuide
          - daily_*       → DailyWorkCoach
          - feedback_*    → FeedbackWriter
          - task_*        → TaskBuilder
          - manager_*     → ManagerInsight
        Use transfer_to_agent(agent_name=...) quando necessário.
    """,
    sub_agents=[
        onboarding_agent,
        coach_agent,
        task_agent,
        manager_agent
    ],
    tools=[say_hello, say_goodbye, transfer_to_agent]
)

session_service = InMemorySessionService()
runner = Runner(agent=coordinator, app_name="orbit", session_service=session_service)
initial_state = {
    "user_name": "John Doe",
    "user_email": "john.doe@example.com",
    "user_id": "1234567890",
    "user_role": "manager",
    "user_team": "Team A",
    "user_department": "Department A",
    "user_location": "Location A",
    "user_phone": "1234567890",
    "user_job_title": "Manager",
    "user_job_description": "Manager of Department A",
    "user_job_location": "Location A",
    "user_job_phone": "1234567890",
    "user_job_email": "john.doe@example.com",
    "user_job_id": "1234567890",
    "user_job_role": "manager",
}

root_agent = coordinator