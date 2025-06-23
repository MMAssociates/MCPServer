# server.py

from fastmcp import FastMCP, Context

# Create the MCP server
mcp = FastMCP("FlutterMCPServer")

@mcp.tool
def notify_user(user_id: str, message: str, ctx: Context) -> str:
    ctx.info(f"Sending message to user {user_id}: {message}")
    return f"Message sent to {user_id}"

# Expose it as a FastAPI-compatible ASGI app
app = mcp.http_app(path="/mcp")
