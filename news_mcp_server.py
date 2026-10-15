######### news_mcp_server.py #########

import random
from mcp.server.fastmcp import FastMCP

## Initialize MCP Server
mcp = FastMCP("news_server")


## ------ Add Tools ------

@mcp.tool()
def get_company_news(company: str) -> str:
    """
    Fetch news updates for a given company.

    Args:
        company (str): Name of the company for which the news is requested.

    Returns:
        str: A two-sentence news update describing the company's current situation.
    """
    positive_news = (
        f"{company} is performing exceptionally well this quarter. "
        "Analysts predict its stock price is likely to rise."
    )

    negative_news = (
        f"{company} is facing challenges in the current market environment. "
        "Experts say its stock price is trending downward."
    )

    return random.choice([positive_news, negative_news])

## Run MCP Server
if __name__ == "__main__":
    mcp.run(transport="streamable-http")
