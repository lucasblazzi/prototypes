from IPython.display import Image, display
from langgraph.graph import START, StateGraph, END
from app.states import AgentState

workflow = StateGraph(AgentState)

workflow.add_node("classification_node", ClassificationNode())

workflow.add_edge(START, "classification_node")
workflow.add_edge("classification_node", END)

app = workflow.compile()

Image(app.get_graph().draw_mermaid_png())