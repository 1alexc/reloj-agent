from google.adk.agents.llm_agent import Agent
# Placeholder import for a vector database RAG tool. Replace with the actual ADK tool when available.
# from google.adk.tools import vector_search

"""
Spec Historian Agent
====================

Purpose
-------
Provides precise technical specifications, heritage information, and caliber details for watches. The agent must never guess; if the requested information is not found in the knowledge base it should respond clearly that it cannot answer.

Tools
-----
* **vector_search** – a RAG‑style retrieval over a curated vector store containing official manufacturer catalogs, Wikipedia extracts and other horology datasets. The tool returns a list of relevant passages that the LLM can cite.

Behavior
--------
1. Query the vector store with the user’s watch model.
2. If at least one passage is returned, extract the exact technical data (caliber name, beat rate, water resistance, power reserve, etc.).
3. Respond with a concise, fact‑only answer, e.g.:
   `Caliber MT5402, 28,800 vph, 70 m water resistance, 70 h power reserve.`
4. If no passage is found, reply with a fallback like:
   “I’m sorry, I don’t have verified data for that model.”
"""

spec_hist_agent = Agent(
    model='gemini-2.5-flash',
    name='spec_hist_agent',
    description='Provides exact watch technical specs and heritage facts without speculation.',
    instruction=(
        "When a user asks for specifications, query the vector_search tool with the watch model. "
        "Only return data that appears in the retrieved passages; never fabricate values. "
        "If nothing is found, politely inform the user that the information is unavailable."
    ),
    # Uncomment when the vector search tool is available:
    # tools=[vector_search],
)
