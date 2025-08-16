from team.common.parser import load_raw_md
from team.agents.base import TeamAgent
from strands_tools import http_request


system_prompt = load_raw_md("team/agents/backend/instructions.md")

backend_agent = TeamAgent(
    model="amazon.nova-pro-v1:0",
    tools=[],
    name="Backend Developer",
    system_prompt=system_prompt,
    description="Implements async Python services and AWS integrations."
)()
