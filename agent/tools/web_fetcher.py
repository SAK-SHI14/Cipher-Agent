from smolagents import Tool
import requests
from bs4 import BeautifulSoup
import re

class WebFetcherTool(Tool):
    name = "fetch_page_content"
    description = (
        "Fetch the cleaned text content from a given URL to retrieve detailed information "
        "that might not be in the search snippet. This is essential for deep fact verification."
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
        Fetches the content from the URL, extracts paragraphs, and cleans up the text.
        """
        if not url.startswith("http"):
            return "Invalid URL format."
        
        try:
            # Simple User-Agent to avoid blocking
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'lxml')
            
            # Remove scripts, styles, etc.
            for tag in soup(['script', 'style', 'header', 'footer', 'nav', 'form']):
                tag.decompose()
            
            # Extract paragraphs
            paragraphs = [p.get_text() for p in soup.find_all('p')]
            content = "\n\n".join(paragraphs)
            
            # Basic cleaning
            content = re.sub(r'\s+', ' ', content).strip()
            
            # Limit the output to 3000 words to avoid token limits
            max_words = 3000
            words = content.split()
            if len(words) > max_words:
                content = " ".join(words[:max_words]) + "... (truncated)"
            
            return content if content else "No readable content found on the page."
            
        except requests.exceptions.HTTPError as e:
             return f"HTTP error occurred: {e}"
        except Exception as e:
            return f"An unexpected error occurred while fetching content: {str(e)}"

if __name__ == "__main__":
    fetcher = WebFetcherTool()
    print(fetcher("https://en.wikipedia.org/wiki/Main_Page"))
