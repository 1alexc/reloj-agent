# Market Agent Instructions

## Purpose
The **Market Agent** provides live market pricing and availability information for watches. It leverages the `google_search` tool to retrieve recent listings from online marketplaces (e.g., Chrono24, eBay, watch forums) and returns concise price ranges along with brief buying tips.

## How It Works
1. **Input** – The user sends a watch model or reference (e.g., "Omega Speedmaster Professional 2021").
2. **Tool Invocation** – The agent automatically calls `google_search` with a query constructed to surface recent secondary‑market listings.
3. **Result Extraction** – The agent parses the top results, extracts price information, and formats a response like:
   ```
   • Price range: $5,400 – $6,200 (average recent listings)
   • Availability: Mostly available on Chrono24; limited on eBay.
   • Tip: Look for sellers with ≥90% positive feedback and watch for "refurbished" listings that may lack original paperwork.
   ```
4. **Safety** – The agent never fabricates numbers. If no reliable price data is found, it replies with a polite fallback message.

## Customising the Query
- The default query template is:
  ```
  "[watch model] secondary market price 2024"
  ```
- To adjust the query (e.g., target a specific marketplace), modify the `instruction` field in `agent.py` accordingly.

## Limitations
- The agent depends on the freshness of Google search results; occasional stale listings may appear.
- It does not perform real‑time API calls to marketplace services; for higher fidelity data you may replace `google_search` with a dedicated API in the future.

## Development
- The agent is defined in `market_agent/agent.py`.
- To add more tools (e.g., a Chrono24 API client), import the tool and include it in the `tools` list.

---
*Generated on 2026‑05‑25.*
