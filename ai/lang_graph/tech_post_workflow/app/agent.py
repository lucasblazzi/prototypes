import os
from typing import TypedDict, List
from langgraph.graph import StateGraph, END

from app.state import AgentState
from app.nodes.classification import ClassificationNode
from app.nodes.entity import EntityNode
from app.nodes.summarize import SummarizeNode


workflow = StateGraph(AgentState)

workflow.add_node("classification_node", ClassificationNode())
workflow.add_node("entity_extraction", EntityNode())
workflow.add_node("summarization", SummarizeNode())

workflow.set_entry_point("classification_node")
workflow.add_edge("classification_node", "entity_extraction")
workflow.add_edge("entity_extraction", "summarization")
workflow.add_edge("summarization", END)

app = workflow.compile()