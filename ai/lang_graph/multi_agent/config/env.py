from pydantic import BaseModel


class Environment(BaseModel):
    openai_api_key: str = ""


env = Environment()
