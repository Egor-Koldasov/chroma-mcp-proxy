# Bridge local server to HTTP
from fastmcp import FastMCP
from fastmcp.client.transports import StdioTransport
from fastmcp.server.proxy import ProxyClient


local_proxy = FastMCP.as_proxy(
    ProxyClient(
        StdioTransport(
            command="uvx",
            args=[
                "chroma-mcp",
                "--client-type",
                "persistent",
                "--data-dir",
                "/home/egor/data/chroma-data",
            ],
        )
    ),
    name="Local-to-HTTP Bridge",
)

# Run via HTTP for remote clients
if __name__ == "__main__":
    local_proxy.run(transport="http", host="0.0.0.0", port=3030)
