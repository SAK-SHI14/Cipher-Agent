from smolagents import Tool
from typing import List, Dict, Any
from duckduckgo_search import DDGS

class WebSearchTool(Tool):
    """
    Executes deep web intelligence scans for raw snippet data.
    """
    name = "web_search"
    description = (
        "Conduct a web search to gather raw intelligence snippets. "
        "Returns a dataset of links, titles, and factual summaries."
    )
    inputs = {
        "query": {
            "type": "string",
            "description": "The search query for intelligence gathering."
        }
    }
    output_type = "any"

    def forward(self, query: str) -> List[Dict[str, str]]:
        try:
            with DDGS() as ddgs:
                results = list(ddgs.text(query, max_results=5))
                return [
                    {
                        "title": r.get('title', ''),
                        "link": r.get('href', ''),
                        "snippet": r.get('body', '')
                    }
                    for r in results
                ]
        except Exception as e:
            return [{"error": f"Intelligence scan failed: {str(e)}"}]
