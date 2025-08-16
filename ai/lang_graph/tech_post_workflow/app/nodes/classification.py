from langchain.schema import HumanMessage
from langchain.prompts import PromptTemplate

from app.nodes import Node
from app.state import AgentState


class ClassificationNode(Node):

    def __call__(self, state: AgentState) -> dict:
        """
        Classify the text into one of predefined categories.

        Parameters:
            state (AgentState): The current state containing the text to classify
            
        Returns:
            dict: A dictionary with the "classification" key containing the category result
            
        Categories:
            - AI: Artificial Intelligence
            - Code: Programming code
            - Architecture: Software architecture
            - SoftSkill: Soft skills
            - Management: Project management
            - Quality: Software quality
            - Other: Content that doesn't fit the above categories
        """
        llm = self.get_llm(model="gpt-4o-mini", temperature=0)
        text_prompt = self.get_text_prompt(name="classification")

        prompt = PromptTemplate(
            input_variables=["text"],
            template=text_prompt
        )

        message = HumanMessage(content=prompt.format(text=state["text"]))
        classification = llm.invoke([message]).content.strip()

        return {"classification": classification}
