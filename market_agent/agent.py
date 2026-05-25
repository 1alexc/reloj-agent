from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search
"""
Market Agent
==============

This agent provides live market pricing and availability information for watches.
It uses the `google_search` tool to query recent listings and price ranges from
online marketplaces. The agent is designed to avoid speculation: it only returns
price information that can be directly sourced from the search results and offers
concise buying tips when appropriate.
"""

market_agent = Agent(
    model='gemini-2.5-flash',
    name='market_agent',
    description='Provides live market pricing and availability for watches.',
    instruction='When given a watch model, use the google_search tool to fetch current secondary market prices and availability. Return concise price range and any relevant buying tips.',
    tools=[google_search],
)
