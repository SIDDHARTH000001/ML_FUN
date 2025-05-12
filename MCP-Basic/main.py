import asyncio
import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import AzureChatOpenAI
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.client import MultiServerMCPClient
load_dotenv()

llm = AzureChatOpenAI(
    deployment_name=os.getenv("OPENAI_API_DEPLOYMENT"),
    azure_endpoint=os.getenv("OPENAI_API_ENDPOINT"),
    temperature=0,
)

stdio_server_params = StdioServerParameters(
    command="python",
    args=[r"C:\Users\SIVERMA\Documents\Experimenting\DeepSeek\langchain-mcp\servers\weather_server.py"],
)


async def main_single_server():
    async with stdio_client(stdio_server_params) as (read, write):
        async with ClientSession(read_stream=read, write_stream=write) as session:
            await session.initialize()
            print("session initialized")
            tools = await load_mcp_tools(session)

            agent = create_react_agent(llm, tools)

            result = await agent.ainvoke(
                {"messages": [HumanMessage(content="what is 2 + 2?")]}
            )
            print(result["messages"][-1].content)


async def main_multi_server():
    async with MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": [
                    r"C:\Users\SIVERMA\Documents\Experimenting\DeepSeek\langchain-mcp\servers\math_server.py"
                ],
            },
            "weather": {
                "url": "http://localhost:8000/sse",
                "transport": "sse",
            },
        }
    ) as client:
        agent = create_react_agent(llm, client.get_tools())
        # result = await agent.ainvoke({"messages": "What is 2 + 2?"})
        result = await agent.ainvoke(
            {"messages": "What is the weather in San Francisco?"}
        )

        print(result["messages"][-1].content)
        
if __name__ == "__main__":
    asyncio.run(main_multi_server())
