1. Types of Agents:
    - ReAct Agents (Reason + Act):
        1. Think about the user input
        2. Decide what tool or action to take (This is where the agent needs to be able to read the docstring to decide which one to use)
        3. Use a tool if needed
        4. Reflect on the result
        5. Repeat if necessary
    - Chain-of-Thought Agents
        1. Do you want interpretable reasoning
        2. You don’t need tool use, just better logic
        3. The task is complex (math, puzzles, planning)
    - Custom Agents
        1. Agents that call APIs directly
        2. Agents with conditional rules
        3. Agents who talk to other agents


References:
- [LangGraph Documentation](https://langgraph.com/docs/)
- [Building Multi-Agent Systems with LangGraph](https://medium.com/@sushmita2310/building-multi-agent-systems-with-langgraph-a-step-by-step-guide-d14088e90f72)