import json
from smolagents import Tool
from typing import List, Dict, Any
from duckduckgo_search import DDGS

class WebSearchTool(Tool):
    """
    Search the web for a query to fetch the latest snippets and relevant information.
    """
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
    output_type = "any"

    def forward(self, query: str) -> List[Dict[str, str]]:
        """
        Executes a search using DDGS and returns normalized results.
        """
        try:
            with DDGS() as ddgs:
                results = list(ddgs.text(query, max_results=5))
                # Normalize and return
                return [
                    {
                        "title": r.get('title', ''),
                        "link": r.get('href', ''),
                        "snippet": r.get('body', '')
                    }
                    for r in results
                ]
        except Exception as e:
            # Silent fallback with error for agent to handle
            return [{"error": f"Search tool failed: {str(e)}"}]

if __name__ == "__main__":
    search = WebSearchTool()
    print(search("Latest RBI interest rates"))
