from langchain_openai import ChatOpenAI

from app.config import env
from app.state import AgentState

class Node:

    @staticmethod
    def get_text_prompt(name) -> str:
        with open(f"app/prompts/{name}.txt", "r") as file:
            prompt = file.read()
        return prompt
    
    @staticmethod
    def get_llm(model, temperature) -> ChatOpenAI:
        return ChatOpenAI(model=model, temperature=temperature, api_key=env.openai_api_key)
    
    def __call__(self, state: AgentState) -> dict:
        raise NotImplementedError