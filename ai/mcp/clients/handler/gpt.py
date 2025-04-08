import json

from openai import OpenAI

from config import env, logger


class GPTMessageHandler:
    def __init__(self, session):
        self.llm = OpenAI(api_key=env.openai_api_key)
        self.session = session
        self.final_response = list()
        self.messages = list()

    async def get_tools(self):
        response = await self.session.list_tools()
        available_tools = [{ 
            "type": "function",
            "function": {
                "name": tool.name,
                "description": tool.description,
                "parameters": tool.inputSchema
            }
        } for tool in response.tools]
        return available_tools

    @property
    def reason_handlers(self):
        return {
            "text": self.handle_text,
            "stop": self.handle_text,
            "length": self.handle_text,
            "tool_calls": self.handle_function_call,
            "content_filter": self.handle_text,
        }

    async def handle_text(self, choice):
        logger.info(f"Handling text response")
        self.messages.append({"role": "assistant", "content": choice.message.content})
        self.final_response.append(choice.message.content)
    
    async def handle_function_call(self, choice):
        logger.info(f"Handling function call response")
        for tool_call in choice.message.tool_calls:
            tool_name = tool_call.function.name
            tool_args = json.loads(tool_call.function.arguments) if tool_call.function.arguments else {}
            logger.info(f"Calling tool: {tool_name} with args: {tool_args}")
        
            result = await self.session.call_tool(tool_name, tool_args)
            self.final_response.append(f"[Calling tool {tool_name} with args {tool_args}]")

            self.messages.append({
                "role": "assistant",
                "tool_calls": [
                    {
                        "id": tool_call.id,
                        "function": {
                            "name": tool_call.function.name,
                            "arguments": tool_call.function.arguments
                        },
                        "type": "function"
                    }
                ]
            })
            self.messages.append({
                "tool_call_id": tool_call.id,
                "role": "tool",
                "content": result.content[0].text,
            })
            # 
            # self.messages.append({
            #     "role": "user", 
            #     "content": result.content[0].text
            # })
        
        response = await self.send_message()
        return
        
    async def handle_response(self, response):
        logger.info(f"Handling response")
        for i, choice in enumerate(response.choices):
            logger.info(f"Handling choice: {i}")
            handler = self.reason_handlers.get(choice.finish_reason, self.handle_text)
            await handler(choice)
        return

    async def send_message(self, message=None):
        if message:
            self.messages.append(message)
        print("Sending message")
        response = self.llm.chat.completions.create(
            model="gpt-4o-mini",
            temperature=0.2,
            max_tokens=1000,
            messages=self.messages,
            tools=await self.get_tools()
        )
        await self.handle_response(response)
        return "\n".join(self.final_response)
