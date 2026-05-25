from google.adk.agents.llm_agent import Agent
from spec_hist_agent.agent import spec_hist_agent
from market_agent.agent import market_agent
from style_agent.agent import style_agent

"""
Root Orchestrator Agent
=======================
Routes user queries to the appropriate specialist agents:
- **spec_hist_agent** - technical specifications & heritage
- **market_agent** - pricing & availability
- **style_agent** - styling advice
"""

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='Orchestrator for watch queries, routing to specialist agents.',
    instruction='''You are the Horology Concierge orchestrator.
Your job is to understand a user's watch-related query, determine its focus (specifications, market pricing, or style), and route the query to the appropriate specialist agent (spec_hist_agent, market_agent, or style_agent).
If the query is about technical specs or heritage, delegate to spec_hist_agent.
If it concerns price, availability, or market trends, delegate to market_agent.
If it concerns styling, wrist size, outfit matching, or occasion, delegate to style_agent.
Aggregate the response from the specialist and present it clearly to the user, maintaining conversation context.
If the user asks a general, non-watch question, respond directly yourself.''',
    sub_agents=[spec_hist_agent, market_agent, style_agent],
)


