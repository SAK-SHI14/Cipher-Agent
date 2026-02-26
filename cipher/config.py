import os
from dotenv import load_dotenv

load_dotenv()

# --- CIPHER Intelligence Configuration ---

# Agent Identity
AGENT_NAME = "CIPHER"
VERSION = "1.0.0-PROTOTYPE"

# Model Selection
# Defaulting to Qwen 72B for precision intelligence extraction.
MODEL_ID = os.getenv("MODEL_ID", "Qwen/Qwen2.5-72B-Instruct")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HF_TOKEN = os.getenv("HF_TOKEN")

# Intelligence Constraints
MAX_STEPS = 12
FACT_VERIFICATION_THRESHOLD = 2
OUTPUT_BULLET_LIMIT = 5
WORD_COUNT_LIMIT = 18

# PowerShell Color Palette
PRIMARY_COLOR = "magenta"   # Branding
THINKING_COLOR = "cyan"     # Reasoning
TOOL_COLOR = "yellow"       # Execution
SUCCESS_COLOR = "green"     # Final Intelligence
ERROR_COLOR = "red"         # Failures/Conflicts
