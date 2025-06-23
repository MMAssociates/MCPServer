# server.py

from fastmcp import FastMCP, Context

# Create a FastMCP server instance
mcp = FastMCP("FlutterMCPServer")

# Example tool you can call from Flutter or any client
@mcp.tool
def notify_user(user_id: str, message: str, ctx: Context) -> str:
    ctx.info(f"Sending message to user {user_id}: {message}")
    return f"Message sent to {user_id}"

# Expose FastAPI app for deployment
app = mcp.as_fastapi()
