import requests
from bs4 import BeautifulSoup
import re
from smolagents import Tool

class PageFetcherTool(Tool):
    """
    Retrieves the full textual content of a specific digital asset for cross-verification.
    """
    name = "fetch_page"
    description = (
        "Fetch the complete raw text from a target URL for detailed evidence extraction. "
        "Use this for deeper analysis when snippets are insufficient."
    )
    inputs = {
        "url": {
            "type": "string",
            "description": "Target asset URL to fetch content from."
        }
    }
    output_type = "string"

    def forward(self, url: str) -> str:
        if not url.startswith("http"):
            return "ERR_INVALID_URL"
        
        try:
            headers = {"User-Agent": "CipherIntelligence/1.0 (Windows NT 10.0; Win64; x64)"}
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'lxml')
            for tag in soup(['script', 'style', 'header', 'footer', 'nav', 'form', 'aside']):
                tag.decompose()
            
            content = " ".join([p.get_text() for p in soup.find_all('p')])
            content = re.sub(r'\s+', ' ', content).strip()
            
            return content[:8000] # Cap for model safety
            
        except Exception as e:
            return f"ERR_EXTRACTION_FAILURE: {str(e)}"
