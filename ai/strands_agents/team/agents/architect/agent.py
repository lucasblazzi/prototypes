from team.agents.base import TeamAgent
from team.common.parser import load_raw_md
from strands_tools import diagram


system_prompt = load_raw_md("team/agents/architect/instructions.md")

architect_agent = TeamAgent(
    model="amazon.nova-pro-v1:0",
    tools=[diagram],
    name="Architect",
    system_prompt=system_prompt,
    description="Owns architecture, NFRs, paved roads, and design reviews."
)()
