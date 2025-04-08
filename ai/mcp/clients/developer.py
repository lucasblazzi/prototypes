import json
import asyncio
from typing import Optional
from contextlib import AsyncExitStack

from mcp import ClientSession
from mcp.client.sse import sse_client

from config import env
from handler.gpt import GPTMessageHandler


class MCPClient:
    def __init__(self):
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()
        self.message_handler = None

    async def connect_to_server(self):
        sse_transport = await self.exit_stack.enter_async_context(sse_client(url="http://localhost:3001/sse"))
        read_stream, write_stream = sse_transport
        self.session = await self.exit_stack.enter_async_context(ClientSession(read_stream, write_stream))
        await self.session.initialize()
        response = await self.session.list_tools()
        tools = response.tools
        print("\nConnected to server with tools:", [tool.name for tool in tools])
        self.message_handler = GPTMessageHandler(session=self.session)
        print("Message handler initialized.")

    async def process_query(self, query: str) -> str:
        message = {"role": "user", "content": query}
        response = await self.message_handler.send_message(message)
        with open("C:/Users/User/Blazzi/Repositories/prototypes/ai/mcp/response.json", "w") as f:
            json.dump(self.message_handler.messages, f, indent=4)
        return response

    async def chat_loop(self):
        while True:
            try:
                query = input("\nQuery: ").strip()
                # query = "How can I calculate TWR based on GIPS?"
                response = await self.process_query(query)
                print("\n" + response)
            except Exception as e:
                print(f"\nError: {str(e)}")
    
    async def cleanup(self):
        """Clean up resources"""
        await self.exit_stack.aclose()


async def main():
    print("Connecting to MCP server...")
    client = MCPClient()
    try:
        await client.connect_to_server()
        print("Connected to MCP server.")
        print("Starting chat loop...")
        await client.chat_loop()
    finally:
        await client.cleanup()


if __name__ == "__main__":
    print("Starting MCP Client...")
    asyncio.run(main())