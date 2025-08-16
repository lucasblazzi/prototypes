import asyncio
from fastapi import FastAPI
from pydantic import BaseModel
from google.genai import types

from .agent import runner, session_service

app = FastAPI()

class InvokeRequest(BaseModel):
    user_id: str
    session_id: str
    query: dict


class CreateSessionRequest(BaseModel):
    user_id: str


def parse_response(events):
    return


@app.post("/invoke")
async def invoke(request: InvokeRequest):
    content = types.Content(role="user", parts=[types.Part(text=request.query["content"])])
    
    events = runner.run(
        user_id=request.user_id,
        session_id=request.session_id,
        new_message=content
    )
    for event in events:
        if event.is_final_response():
            final_response = event.content.parts[0].text
    return final_response


@app.post("/create_session")
async def create_session(request: CreateSessionRequest):
    session = await session_service.create_session(app_name="orbit", user_id=request.user_id)
    return session
