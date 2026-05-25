from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

"""
Spec Historian Agent
===================

Purpose
-------
Provides precise technical specifications, heritage information, and caliber details
for watches. The agent must never guess; if the requested information cannot be
found via web search it should respond clearly that it cannot answer.

Tools
-----
* **google_search** – Uses Google Search to retrieve recent, reputable web pages
  (official brand sites, Wikipedia, horology references). The tool returns a list of
  snippets that the LLM can cite.

Behavior
--------
1. Query `google_search` with a concise query that includes the watch brand,
   model, and the phrase “specifications” or “history”.
2. Scan the returned snippets for concrete data (caliber name, beat rate,
   water resistance, power reserve, introduction year, notable milestones).
3. Return a concise, fact‑only answer, e.g.:

   `Caliber MT5402, 28,800 vph, 70 m water resistance, 70 h power reserve; introduced 2018.`

4. If no reliable snippet is found, reply with a polite fallback such as:
   “I’m sorry, I couldn’t locate verified specifications for that model.”
"""

spec_hist_agent = Agent(
    model='gemini-2.5-flash',
    name='spec_hist_agent',
    description='Provides exact watch technical specs and heritage facts using web search.',
    instruction=(
        "When a user asks for watch specifications or history, use the google_search tool "
        "with a focused query (brand, model, and 'specifications'). Only return data "
        "that appears in the retrieved snippets; never fabricate values. If nothing reliable "
        "is found, inform the user that the information is unavailable."
    ),
    tools=[google_search],
)
