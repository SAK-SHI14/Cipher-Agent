import os
from smolagents import CodeAgent, InferenceClientModel, LiteLLMModel
from axiom.tools.web_search import WebSearchTool
from axiom.tools.fetcher import WebFetcherTool
from axiom.tools.verifier import FactVerifierTool
from axiom.config import MODEL_ID, MAX_STEPS, HF_TOKEN

def create_axiom_agent():
    """
    Initializes and configures the AXIOM Fact-Synthesis Agent.
    """
    
    # 1. Initialize Tools
    search_tool = WebSearchTool()
    fetch_tool = WebFetcherTool()
    verifier_tool = FactVerifierTool()
    
    # 2. Configure Model
    # Uses LiteLLMModel for OpenAI/Anthropic/etc. OR InferenceClientModel for HF.
    if os.getenv("OPENAI_API_KEY"):
        model = LiteLLMModel(model_id=MODEL_ID)
    else:
        # Fallback to a free model on Hub with the ID from config
        model = InferenceClientModel(model_id=MODEL_ID, token=HF_TOKEN)
    
    # 3. Create CodeAgent (The Reasoning Engine)
    # Code-based agents are superior for complex data processing and self-correction.
    agent = CodeAgent(
        tools=[search_tool, fetch_tool, verifier_tool],
        model=model,
        max_steps=MAX_STEPS,
        add_base_tools=True, # Includes python_interpreter, print, etc.
    )
    
    # 4. Customize System Prompt to enforce the Fact-Synthesis Contract
    agent.prompt_templates["system_prompt"] = """
    You are AXIOM, a Senior Fact-Synthesis Autonomous Agent and a senior research analyst.
    Your mission is to perform signal extraction and fact distillation from live data.
    You are NOT a chatbot. You are an information compressor.

    🔒 OUTPUT CONTRACT (STRICT)
    - EXACTLY 3-5 bullet points in your final answer.
    - Each bullet ≤ 20 words.
    - NO URLs. NO source names ("According to Wikipedia"). NO filler words.
    - NO speculation. NO redundant facts.
    - Format: return a single synthesized string containing the bulleted facts (using '•' or '*').
    - If reliable synthesis is impossible, return exactly: "No reliable consolidated answer found."

    🐍 PYTHON RULES (CORE)
    - Use '#' for comments. NEVER use '//'.
    - Wrap all logic and tool calls inside <code>...</code> blocks.
    - Call 'final_answer(\"your formatted result string\")' once synthesis is complete.

    🔄 REASONING PIPELINE (MANDATORY)
    1. Parse intent and determine if live web data is needed. 
    2. If YES, perform 'web_search' to get raw material snippets.
    3. If necessary, follow up with 'fetch_content' for specific high-value pages.
    4. Extract factual claims and cross-verify them using 'verify_facts'.
    5. Prioritize facts with at least TWO independent matches (VERIFIED). 
    6. Compress verified facts into high-signal final answer. 
    7. Remove noise, opinions, and repetition.

    Don't just talk. Execute code in <code> blocks to find the signal!
    Today is 2026-02-26. Use this as a reference point.
    """
    
    return agent

if __name__ == "__main__":
    agent = create_axiom_agent()
    print("AXIOM Agent Initialized.")
