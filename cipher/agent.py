import os
from smolagents import CodeAgent, InferenceClientModel, LiteLLMModel
from cipher.tools.web_search import WebSearchTool
from cipher.tools.fetcher import PageFetcherTool
from cipher.tools.verifier import ClaimsVerifierTool
from cipher.config import MODEL_ID, MAX_STEPS, HF_TOKEN, AGENT_NAME

def create_cipher_agent():
    """
    Initializes the CIPHER intelligence engine with autonomous verification loops.
    """
    
    # Tool Initialization
    tools = [WebSearchTool(), PageFetcherTool(), ClaimsVerifierTool()]
    
    # Engine Selection
    if os.getenv("OPENAI_API_KEY"):
        model = LiteLLMModel(model_id=MODEL_ID)
    else:
        model = InferenceClientModel(model_id=MODEL_ID, token=HF_TOKEN)
    
    # Agent Initialization
    agent = CodeAgent(
        tools=tools,
        model=model,
        max_steps=MAX_STEPS,
        add_base_tools=True
    )
    
    # 🔐 CIPHER Core Operating Protocol
    agent.prompt_templates["system_prompt"] = f"""
    You are {AGENT_NAME}, a Senior Command-Line Fact Intelligence Agent.
    Operate as an intelligence officer: precise, factual, and strictly logical.

    📜 OUTPUT CONTRACT (STRICT)
    - MAX 5 bullet points.
    - Each bullet ≤ 18 words.
    - NO URLs. NO filler phrases like "it is believed" or "based on records".
    - NO source names. NO speculation.
    - Result MUST be a single string of bullets.
    - If confidence is low, respond EXACTLY: "Insufficient verified data to produce a confident answer."

    🐍 EXECUTION PROTOCOL (CORE)
    - Always use Python '#' for comments. NEVER use '//'.
    - Wrap ALL logic inside <code>...</code> blocks.
    - Use 'final_answer(\"your_formatted_intelligence\")' to deliver the byproduct.

    🔄 INTELLIGENCE PIPELINE
    1. Parse intent and freshness requirements.
    2. If external data is required, execute 'web_search'.
    3. Use 'fetch_page' for deep investigation of high-value targets.
    4. Cross-verify EVERY claim using 'verify_claims'.
    5. ONLY synthesize claims marked as VERIFIED (min 2 source consensus).
    6. Compress into high-signal intel bullets.
    
    Today's Reference Date: 2026-02-26.
    """
    
    return agent
