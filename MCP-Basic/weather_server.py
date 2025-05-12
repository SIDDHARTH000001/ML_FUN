from mcp.server.fastmcp import FastMCP

mcp = FastMCP("WeatherServer")

@mcp.tool()
def get_forecast(location: str) -> str:
    """Get the weather forecast for a location (dummy implementation)."""
    return f"The weather forecast for {location} is sunny with a high of 25°C."

@mcp.tool()
def get_alerts(location: str) -> str:
    """Get weather alerts for a location (dummy implementation)."""
    return f"No weather alerts for {location}."

if __name__ == "__main__":
    print("Starting WeatherServer MCP server...")
    mcp.run() 