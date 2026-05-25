from google.adk.agents.llm_agent import Agent
# Placeholder import for a multimodal image analysis tool. Replace with the actual ADK tool when available.
# from google.adk.tools import image_analyze

"""
Style Concierge Agent
=====================

Purpose
-------
This agent helps users discover watches that match their personal style, attire, wrist size, and occasion. It can handle:

* Textual queries like "What watch goes well with a tuxedo?"
* Optional image inputs (e.g., a picture of the user's wrist or outfit) when the multimodal tool becomes available.

Behaviour
----------
* Generates a short, creative description of suitable watch families (dress, tool, dive, heritage, etc.).
* When an image is supplied, extracts visual cues (color palette, formality level) and tailors the recommendation.
* Returns a concise recommendation with:
  - Suggested watch type(s)
  - A brief styling tip
  - (Optional) a link to a reference image
"""

style_agent = Agent(
    model='gemini-2.5-flash',
    name='style_agent',
    description='Creative concierge that suggests watch styles based on vibe, attire, wrist size, and occasion.',
    instruction=(
        "When a user asks for styling advice, consider the context (formal, casual, sport, etc.). "
        "If an image is provided, use the multimodal tool to extract dominant colors and formality cues, then map those cues to appropriate watch families. "
        "Produce a concise, friendly recommendation with one or two watch style suggestions and a brief styling tip."
    ),
    # Uncomment and add the real tool when it becomes available:
    # tools=[image_analyze],
)
