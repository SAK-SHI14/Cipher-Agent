import sys
from agent.agent import create_autonomous_agent

def main():
    print("="*50)
    print(" INDUSTRIAL AUTONOMOUS AGENT (smol-agents) ")
    print("="*50)
    print("Ready to fetch, verify, and reason over web data.")
    
    agent = create_autonomous_agent()
    
    # Pre-defined demo queries
    demos = [
        "Latest interest rate announced by RBI",
        "Current CEO of OpenAI",
        "Recent AI regulation updates in India",
        "Today's tech news related to LLMs"
    ]
    
    print("\nDEMO SCENARIOS:")
    for i, d in enumerate(demos, 1):
        print(f"{i}. {d}")
    print("5. Custom Query")
    
    choice = input("\nSelect a demo (1-4) or enter '5' for custom: ")
    
    if choice in ['1', '2', '3', '4']:
        query = demos[int(choice)-1]
    else:
        query = input("Enter your custom query: ")
    
    print(f"\n[AGENT] Analyzing: '{query}'...")
    print("-" * 30)
    
    try:
        # Running the agent
        # The agent will automatically use tools to find the answer
        result = agent.run(query)
        
        print("\n" + "="*50)
        print(" FINAL ANSWER ")
        print("="*50)
        print(result)
        print("="*50)
        
    except Exception as e:
        print(f"\n[ERROR] An error occurred during agent execution: {e}")

if __name__ == "__main__":
    main()
