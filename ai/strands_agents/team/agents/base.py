from strands import Agent
from team.common.parser import load_dict_md



class TeamAgent:

    def __init__(self, model: str, name: str, system_prompt: str, description: str, tools: list):
        self.model = model
        self.name = name
        self.system_prompt = system_prompt
        self.description = description
        self.tools = tools

    @property
    def agent_id(self):
        return f"{self.name.lower().replace(' ', '_')}_agent"

    @property
    def team_context(self):
        instructions = load_dict_md("team/agents/instructions.md")
        return instructions.get("Team Context", "No context provided.")
    
    @property
    def team_principles(self):
        instructions = load_dict_md("team/agents/instructions.md")
        return instructions.get("Team Principles", "No principles provided.")

    @property
    def collaboration_rules(self):
        instructions = load_dict_md("team/agents/instructions.md")
        return instructions.get("Collaboration Rules", "No collaboration rules provided.")

    def __call__(self):
        agent = Agent(
            model=self.model,
            tools=self.tools,
                # - String tool names (e.g., "retrieve")
                # - File paths (e.g., "/path/to/tool.py")
                # - Imported Python modules (e.g., from strands_tools import current_time)
                # - Dictionaries with name/path keys (e.g., {"name": "tool_name", "path": "/path/to/tool.py"})
                # - Functions decorated with `@strands.tool` decorator.
            system_prompt=(
                f"You are the {self.name}.\n\n"
                f"Context:\n{self.team_context}\n\n"
                f"Team Principles:\n{self.team_principles}\n\n"
                f"Collaboration Rules:\n{self.collaboration_rules}\n\n"
                f"Role Charter:\n{self.system_prompt}\n"
                "When the task requires another specialty, use the handoff tool with a clear rationale and summary."
            ),
            agent_id=self.agent_id,
            name=self.name,
            description=self.description,
        )
        return agent
