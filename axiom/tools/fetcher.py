import requests
from bs4 import BeautifulSoup
import re
from smolagents import Tool
from typing import List, Dict, Any

class WebFetcherTool(Tool):
    """
    Fetches the cleaned text content from a given URL to retrieve detailed information.
    Essential for deep fact verification which cannot be done with just snippets.
    """
    name = "fetch_content"
    description = (
        "Extract the raw text from a webpage URL. "
        "Useful for deep verification of specific links returned by web_search."
    )
    inputs = {
        "url": {
            "type": "string",
            "description": "The URL of the webpage to fetch content from."
        }
    }
    output_type = "string"

    def forward(self, url: str) -> str:
        """
        Fetches the content from the URL, cleans up the text, and returns a string.
        """
        if not url.startswith("http"):
            return "Error: Invalid URL format."
        
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'lxml')
            
            # Remove scripts, styles, etc.
            for tag in soup(['script', 'style', 'header', 'footer', 'nav', 'form', 'aside']):
                tag.decompose()
            
            # Extract content from paragraphs
            paragraphs = [p.get_text() for p in soup.find_all('p')]
            content = "\n\n".join(paragraphs)
            
            # Basic cleaning
            content = re.sub(r'\s+', ' ', content).strip()
            
            # Limit the output to 2000 words to avoid token limits for agent's interpreter
            max_words = 2000
            words = content.split()
            if len(words) > max_words:
                content = " ".join(words[:max_words]) + "... (truncated)"
            
            return content if content else "Error: No readable content found on page."
            
        except requests.exceptions.HTTPError as e:
             return f"HTTP Error {response.status_code} occurred while fetching."
        except Exception as e:
            return f"Unexpected Error: {str(e)}"

if __name__ == "__main__":
    fetcher = WebFetcherTool()
    print(fetcher("https://en.wikipedia.org/wiki/Main_Page"))
