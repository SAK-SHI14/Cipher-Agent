import os
from dotenv import load_dotenv

load_dotenv()

# --- AXIOM Configuration ---

# Model Configuration
# Primary: Qwen 72B for deep synthesis. Fallback: Coder 32B.
MODEL_ID = os.getenv("MODEL_ID", "Qwen/Qwen2.5-72B-Instruct")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HF_TOKEN = os.getenv("HF_TOKEN")

# Search & Retrieval Parameters
MAX_SEARCH_RESULTS = 5
MAX_STEPS = 10
FACT_VALIDATION_THRESHOLD = 2 # Min sources required for "Verified" status

# UI & Style Configuration
BRAND_COLOR = "magenta"
THOUGHT_COLOR = "cyan"
TOOL_COLOR = "yellow"
SUCCESS_COLOR = "green"
ERROR_COLOR = "red"
