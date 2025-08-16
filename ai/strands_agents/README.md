## Swarm Multi-Agent Pattern


### Overview
A Swarm is a collaborative agent orchestration system where multiple agents work together as a team to solve complex tasks. Unlike traditional sequential or hierarchical multi-agent systems, a Swarm enables autonomous coordination between agents with shared context and working memory.

- Self-organizing agent teams with shared working memory
- Tool-based coordination between agents
- Autonomous agent collaboration without central control
- Dynamic task distribution based on agent capabilities
- Collective intelligence through shared context
- Multi-modal input support for handling text, images, and other content types

Each agent in a Swarm:

- Has access to the full task context
- Can see the history of which agents have worked on the task
- Can access shared knowledge contributed by other agents
- Can decide when to hand off to another agent with different expertise

### Safety Mechanisms
Swarms include several safety mechanisms to prevent infinite loops and ensure reliable execution:

- Maximum handoffs: Limits how many times control can be transferred between agents
- Maximum iterations: Caps the total number of execution iterations
- Execution timeout: Sets a maximum total runtime for the Swarm
- Node timeout: Limits how long any single agent can run
- Repetitive handoff detection: Prevents agents from endlessly passing control back and forth

### Best Practices
- Create specialized agents: Define clear roles for each agent in your Swarm
- Use descriptive agent names: Names should reflect the agent's specialty
- Set appropriate timeouts: Adjust based on task complexity and expected runtime
- Enable repetitive handoff detection: Set appropriate values for repetitive_handoff_detection_window and repetitive_handoff_min_unique_agents to prevent ping-pong behavior
- Include diverse expertise: Ensure your Swarm has agents with complementary skills
- Provide agent descriptions: Add descriptions to your agents to help other agents understand their capabilities
- Leverage multi-modal inputs: Use ContentBlocks for rich inputs including images