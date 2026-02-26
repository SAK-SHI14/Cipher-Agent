import sys
from cipher.agent import create_cipher_agent
from cipher.ui import CipherUI, console
from rich.live import Live

def run_mission(query: str, agent):
    """Executes a single intelligence gathering mission."""
    CipherUI.log_action(f"Initiating mission: '{query}'", "agent")
    
    with console.status("[cyan]CIPHER is processing intelligence signals...[/]"):
        try:
            # Autonomous reasoning loop
            intelligence = agent.run(query)
            
            # Formatting check
            if isinstance(intelligence, list):
                intelligence = "\n".join([f"• {str(i)}" for i in intelligence])
            
            CipherUI.present_intelligence(str(intelligence))
            
        except Exception as e:
            CipherUI.show_error(f"Intelligence loop failed: {str(e)}")

def main():
    CipherUI.show_header()
    
    CipherUI.log_action("Booting autonomous intelligence core...", "agent")
    try:
        agent = create_cipher_agent()
    except Exception as e:
        CipherUI.show_error(f"Engine initialization failed: {str(e)}")
        sys.exit(1)

    missions = [
        "Latest RBI repo rate",
        "Current CEO of OpenAI",
        "Recent AI regulations in India"
    ]

    while True:
        console.print("\n[branding]COMMAND INPUT >[/] [white]Select Mission Index or Enter Query[/]")
        for i, m in enumerate(missions, 1):
            console.print(f"  [yellow]{i}[/]. {m}")
        console.print("  [yellow]4[/]. Custom Intel Query")
        console.print("  [yellow]5[/]. Shutdown Core")
        
        choice = input("\nCIPHER > ").strip()
        
        if choice == '5':
            CipherUI.log_action("Core shutdown sequence initiated. Goodbye.", "agent")
            break
        elif choice in ['1', '2', '3']:
            query = missions[int(choice)-1]
        elif choice == '4':
            query = input("Custom Mission > ").strip()
        else:
            query = choice # Treat as custom query
            
        if not query: continue
        
        run_mission(query, agent)

if __name__ == "__main__":
    main()
