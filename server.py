# server.py

from fastmcp import FastMCP, Context

# Create a FastMCP instance with a name
mcp = FastMCP("FlutterMCPServer")

# Define a tool to send message
@mcp.tool
def notify_user(user_id: str, message: str, ctx: Context) -> str:
    ctx.info(f"Sending message to user {user_id}: {message}")
    # Here, you could integrate Firebase or a database
    return f"Message sent to {user_id}"

# Expose FastMCP server as a FastAPI app for Render
app = mcp.from_fastapi()
