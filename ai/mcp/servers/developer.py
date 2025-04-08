import json
import base64

import PyPDF2 as pdf2
from mcp.server.fastmcp import FastMCP


gips_pdf_path = "C:/Users/User/Blazzi/Repositories/prototypes/ai/mcp/servers/files/2020_gips_standards_firms.pdf"
balances_path = "C:/Users/User/Blazzi/Repositories/prototypes/ai/mcp/servers/mocks/balances.json"
trades_path = "C:/Users/User/Blazzi/Repositories/prototypes/ai/mcp/servers/mocks/trades.json"

mcp = FastMCP(
    name="Developer MCP", 
    instructions="Developer MCP for financial data",
    version="0.1",
    debug=True,
    log_level="DEBUG",
    host="localhost",
    port=3001,
    sse_path="/sse",
    message_path="/messages/",
    warn_on_duplicate_resources=True,
    warn_on_duplicate_tools=True,
    warn_on_duplicate_prompts=True,
    dependencies=[]
)

# mcp = FastMCP(
#     name="Developer MCP"
# )


@mcp.tool(name="greetings", description="Returns a greeting message")
def greetings(name: str) -> str:
    """
    Returns a greeting message.
    
    Args:
        name (str): The name to greet.

    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}! Welcome to the Developer MCP."


@mcp.resource(uri="resource://gips", name="get_gips_pdf", description="Get GIPS PDF", mime_type="application/pdf")
def get_gips_pdf():
    """
    Get GIPS PDF.
    
    Returns:
        base64: The base64 encoded PDF file.
    """
    with open(gips_pdf_path, "rb") as file:
        pdf_content = file.read()
        base64_encoded = base64.b64encode(pdf_content)
        base64_string = base64_encoded.decode("utf-8")
    
    return base64_string


@mcp.tool(name="read_gips", description="Read GIPS - Global Investment Performance Standards for Firms")
def read_gips(query: str) -> str:
    """
    Respond TWR questions based on GIPS.

    Args:
        query (str): The query string to search in the PDF.

    Returns:
        str: The content fetched from the PDF based on the query.
    """
    
    return """
"To calculate the Time-Weighted Return (TWR) according to the Global Investment Performance Standards (GIPS), you can follow these steps:\n\n1. **Identify the Periods**: Break down the total investment period into sub-periods based on the timing of external cash flows (deposits and withdrawals).\n\n2. **Calculate Sub-Period Returns**: For each sub-period, calculate the return using the formula:\n   \\[\n   R_i = \\frac{(V_{i} - C_{i})}{C_{i}}\n   \\]\n   where:\n   - \\( R_i \\) is the return for the sub-period.\n   - \\( V_{i} \\) is the ending value of the portfolio at the end of the sub-period.\n   - \\( C_{i} \\) is the beginning value of the portfolio at the start of the sub-period, adjusted for any external cash flows.\n\n3. **Link the Returns**: Once you have the sub-period returns, link them together to calculate the overall TWR using the formula:\n   \\[\n   TWR = (1 + R_1) \\times (1 + R_2) \\times \\ldots \\times (1 + R_n) - 1\n   \\]\n   where \\( R_1, R_2, \\ldots, R_n \\) are the sub-period returns.\n\n4. **Adjust for Cash Flows**: Ensure that the calculation negates the effects of external cash flows by adjusting the beginning and ending values of the portfolio for any cash inflows or outflows during the period.\n\n5. **Report the Results**: Present the TWR as a percentage, and ensure compliance with GIPS by providing all necessary disclosures regarding the calculation methodology, any changes in return types, and the frequency of external cash flows.\n\nBy following these steps, you can accurately calculate the TWR in accordance with GIPS standards."    
    """
    query = query.lower()
    
    with open(gips_pdf_path, "rb") as file:
        reader = pdf2.PdfReader(file)
        content = ""
        for page in reader.pages:
            text = page.extract_text()
            if text:
                content += page.extract_text() + "\n"

    content = content[(len(content) // 2):]

    return (f"Using context from GIPS - Global Investment Performance Standards for Firms {gips_pdf_path}:\n\n"
            f"Content:\n{content}\n\n"
            f"Query: {query}\n\n"
            f"Please answer the question based on the content above.")


@mcp.tool(name="get_balances", description="Get balances for a given account ID and date range")
def get_balances(account_id: str, start_date: str, end_date: str):
    """
    Get the balances for a given account ID and date range.
    
    Args:
        account_id (str): The account ID to get balances for.
        start_date (str): The start date for the balance query (YYYY-MM-DD).
        end_date (str): The end date for the balance query (YYYY-MM-DD).

    Returns:
        array: A list of daily balances for each asset on the given account ID and date range.
    """

    data = json.load(open(balances_path))
    return data


@mcp.tool(name="get_trades", description="Get transactions for a given account ID and date range")
def get_trades(account_id: str, start_date: str, end_date: str):
    """
    Get the trades for a given account ID and date range.

    Args:
        account_id (str): The account ID to get trades for.
        start_date (str): The start date for the trade query (YYYY-MM-DD).
        end_date (str): The end date for the trade query (YYYY-MM-DD).

    Returns:
        array: A list of trades for the given account ID and date range.
    """

    data = json.load(open(trades_path))
    return data


# Transports
# https://modelcontextprotocol.io/docs/concepts/transports
if __name__ == "__main__":
    mcp.run(transport="sse")
    # mcp.run()