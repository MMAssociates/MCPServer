# server.py
from fastmcp import FastMCP, Context

mcp = FastMCP("FlutterMCPServer")

@mcp.tool
def notify_user(user_id: str, message: str, ctx: Context) -> str:
    # Send live message
    ctx.send(f"🔔 {message}")
    return f"Message sent to {user_id}"

# Create the app using streamable HTTP (default transport)
app = mcp.http_app(path="/mcp")
