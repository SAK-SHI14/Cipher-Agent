from smolagents import Tool
from typing import List, Dict, Any
import requests

class WebSearchTool(Tool):
    name = "web_search"
    description = (
        "Search the web for a given query to fetch the latest and most relevant information. "
        "Returns a list of dictionaries with 'title', 'link', and 'snippet'."
    )
    inputs = {
        "query": {
            "type": "string",
            "description": "The search query to look up on the web."
        }
    }
    output_type = "any" # Usually return a list of dicts

    def forward(self, query: str) -> List[Dict[str, str]]:
        """
        Executes a search using DuckDuckGo.
        In a production system, this could be SerpAPI or Tavily.
        """
        try:
            from duckduckgo_search import DDGS
            with DDGS() as ddgs:
                results = list(ddgs.text(query, max_results=5))
                # Normalize results
                return [
                    {
                        "title": r.get('title', ''),
                        "link": r.get('href', ''),
                        "snippet": r.get('body', '')
                    }
                    for r in results
                ]
        except Exception as e:
            return [{"error": f"Search failed: {str(e)}"}]

if __name__ == "__main__":
    # Internal test
    search = WebSearchTool()
    print(search("Latest RBI repo rates 2024"))
