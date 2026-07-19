from mcp.server.fastmcp import FastMCP

from tools.namespaces import list_namespaces

mcp = FastMCP("DevOps MCP")


@mcp.tool()
def namespaces():
    """
    Return all Kubernetes namespaces.
    """
    return list_namespaces()


if __name__ == "__main__":
    mcp.run()
