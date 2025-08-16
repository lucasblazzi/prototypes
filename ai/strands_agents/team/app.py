import logging
from strands.multiagent import Swarm

from team.agents import architect_agent, backend_agent, repository_manager_agent

logging.getLogger("strands.multiagent").setLevel(logging.INFO)
logging.basicConfig(format="%(levelname)s | %(name)s | %(message)s")


team = Swarm(
    nodes=[
        architect_agent, backend_agent, repository_manager_agent
    ],
    max_handoffs=10,
    max_iterations=10,
    execution_timeout=300,
    node_timeout=120,
    repetitive_handoff_detection_window=8,
    repetitive_handoff_min_unique_agents=3,
)

if __name__ == "__main__":
    task = (
        "Design and deliver a minimal vertical slice: "
        "User inputs two numbers on an api and expects their sum"
    )
    result = team(task)
    print("\nStatus:", result.status)
    print("\nAgents invoked:", [n.node_id for n in result.node_history])
    print(f"\nLatency: {result.accumulated_metrics['latencyMs']}ms")
    print(f"\nInput tokens: {result.accumulated_usage['inputTokens']}")
    print(f"\nOutput tokens: {result.accumulated_usage['outputTokens']}")
    print(f"\nTotal tokens: {result.accumulated_usage['totalTokens']}")
    print(f"\nExecution count: {result.execution_count}")
