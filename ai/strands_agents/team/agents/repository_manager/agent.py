from team.common.parser import load_raw_md
from team.agents.base import TeamAgent

from strands_tools import editor, file_read, file_write


system_prompt = load_raw_md("team/agents/repository_manager/instructions.md")

repository_manager_agent = TeamAgent(
    model="amazon.nova-pro-v1:0",
    tools=[editor, file_read, file_write],
    name="Repository Manager",
    system_prompt=system_prompt,
    description="Manages repository files and structures."
)()
