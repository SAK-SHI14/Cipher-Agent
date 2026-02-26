import os
from smolagents import CodeAgent, InferenceClientModel, LiteLLMModel
from agent.tools.search import WebSearchTool
from agent.tools.web_fetcher import WebFetcherTool
from agent.tools.fact_verifier import FactVerifierTool
from agent.config import MODEL_ID, MAX_STEPS, HF_TOKEN

def create_autonomous_agent():
    """
    Initializes and configures the industrial-grade autonomous agent.
    """
    
    # 1. Initialize Tools
    search_tool = WebSearchTool()
    fetch_tool = WebFetcherTool()
    verifier_tool = FactVerifierTool()
    
    # 2. Configure Model
    # Using LiteLLMModel which is a common choice for flexibility in smol-agents
    # Alternatively, use HfApiModel for free Hugging Face Inference API
    if os.getenv("OPENAI_API_KEY"):
        model = LiteLLMModel(model_id=MODEL_ID)
    else:
        # Fallback to a free model on Hub using the ID from config
        model = InferenceClientModel(model_id=MODEL_ID, token=HF_TOKEN)
    
    # 3. Create CodeAgent
    # CodeAgent allows writing Python code to perform reasoning, which is more reliable
    # than just predicting tool calls (LLM-as-a-Reasoning-Engine)
    agent = CodeAgent(
        tools=[search_tool, fetch_tool, verifier_tool],
        model=model,
        max_steps=MAX_STEPS,
        add_base_tools=True, # Includes tools like python_interpreter, print, etc.
    )
    
    # 4. Customize System Prompt to enforce the Fact-Synthesis "Distiller" Persona
    agent.prompt_templates["system_prompt"] = """
    You are a Fact-Synthesis Autonomous Agent. 
    Your purpose is to act as a senior research analyst and information compressor.

    🔒 OUTPUT CONTRACT (STRICT)
    - You MUST return a single string containing maximum 5 bullet points.
    - Each bullet ≤ 20 words.
    - Use '•' or '*' for bullets.
    - NO Python lists in final_answer. NO URLs, NO filler phrases.
    - If answer is not confidently synthesized -> say: "No reliable consolidated answer found from current web data."

    🐍 PYTHON RULES (CORE)
    - Use '#' for comments. NEVER use '//'.
    - All logic must be in <code>...</code> blocks.
    - Call 'final_answer(\"your formatted bulleted string\")' to finish.

    🔄 INTERNAL REASONING PIPELINE (MANDATORY)
    1. Decide if live data is needed. If YES, perform 'web_search'.
    2. Extract only factual statements from snippets or page content.
    3. Cross-validate facts.
    4. COMPRESS into a high-signal summary string with bullets.
    """
    
    return agent

if __name__ == "__main__":
    # Test instance
    agent = create_autonomous_agent()
    print("Agent Initialized.")
