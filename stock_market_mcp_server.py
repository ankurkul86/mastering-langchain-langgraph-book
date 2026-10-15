######### stock_market_mcp_server.py #########

import random
from mcp.server.fastmcp import FastMCP

## Initialize MCP Server
mcp = FastMCP("stock_server")

## ------ Add Tools ------

## Note: The output type is str in the book's snippet, which fails now due to strict type checking in the latest MCP SDK
@mcp.tool()
def stock_price(name: str) -> float: 
    """
    Fetches the current market price of a stock.

    Parameters
    ----------
    name : str
        The name of the stock.

    Returns
    -------
    float
        The current stock price (in USD).
    """
    price = round(random.uniform(10, 500), 2)
    return price

@mcp.tool()
def buy_stock(name: str, qty: int) -> str:
    """
    This function buys a specific quantity of a stock.

    Parameters
    ----------
    name : str
        The name of the stock to buy.

    qty : int
        The number of shares to purchase.

    Returns
    -------
    str
        Feedback on stock purchase success or failure.
    """
    return f"Successfully purchased {qty} shares of {name}."

@mcp.tool()
def sell_stock(name: str, qty: int) -> str:
    """
    This function sells a specific quantity of a stock.

    Parameters
    ----------
    name : str
        The name of the stock to sell.

    qty : int
        The number of shares to sell.

    Returns
    -------
    str
        Feedback on the stock sales success or failure.
    """
    return f"Successfully sold {qty} shares of {name}."

## Run MCP Server
if __name__ == "__main__":
    mcp.run(transport="stdio")
