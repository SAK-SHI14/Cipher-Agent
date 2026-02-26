from smolagents import CodeAgent, InferenceClientModel

agent = CodeAgent(tools=[], model=InferenceClientModel(model_id="Qwen/Qwen2.5-Coder-32B-Instruct"))
try:
    print(agent.run("What is 1+1? Answer only the number."))
except Exception as e:
    print(f"Failed to run: {e}")
