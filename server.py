from fastmcp import FastMCP, Context

mcp = FastMCP("FlutterMCPServer")

@mcp.tool
def notify_user(user_id: str, message: str, ctx: Context) -> str:
    ctx.send(f"🔔 {message}")
    return f"Message sent to {user_id}"

app = mcp.http_app(path="/mcp")
