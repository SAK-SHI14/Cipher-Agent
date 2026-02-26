import os
from dotenv import load_dotenv

load_dotenv()

# Model Configuration
# For smolagents, we can use HfApiModel (HuggingFace) or LiterLLMModel (OpenAI, Anthropic, etc.)
MODEL_ID = os.getenv("MODEL_ID", "Qwen/Qwen2.5-72B-Instruct") 
API_KEY = os.getenv("OPENAI_API_KEY") # We'll need this for OpenAI/Anthropic/etc.
HF_TOKEN = os.getenv("HF_TOKEN") # For HuggingFace models

# Search Configuration
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

# Agent Parameters
MAX_STEPS = 10
VERBOSITY_LEVEL = 1
