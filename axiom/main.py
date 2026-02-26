import sys
from axiom.agent import create_axiom_agent
from axiom.ui import AxiomUI, console
from rich.live import Live
from rich.spinner import Spinner
from rich.table import Table
from rich.panel import Panel

def run_axiom_demo(query: str, agent):
    """
    Executes a single fact-synthesis run with premium UI progress markers.
    """
    AxiomUI.show_step(f"Analyzing query: '{query}'...", style="cyan")
    
    # Progress indication for the complex reasoning steps
    with console.status("[cyan]AXIOM is distilling signal from web data...[/]") as status:
        try:
            # Execute the Fact-Synthesis loop
            # The agent will write Python code, call web_search, verify_facts, etc.
            result = agent.run(query)
            
            # Post-process result if it's a list (some models might still return it)
            if isinstance(result, list):
                result = "\n".join([f"• {str(item)}" for item in result])
            
            # Render the compressed synthesis
            AxiomUI.show_final_answer(str(result))
            
        except Exception as e:
            AxiomUI.show_error(f"Reasoning process encountered a critical failure: {str(e)}")

def main():
    # Initial branding
    AxiomUI.show_header()
    
    # Agent initialization (Slow step)
    AxiomUI.show_step("Initializing AXIOM engine and loading Qwen 72B model...", style="magenta")
    try:
        agent = create_axiom_agent()
    except Exception as e:
        AxiomUI.show_error(f"Failed to initialize AI engine: {str(e)}")
        sys.exit(1)
        
    demos = [
        "Latest RBI repo rate",
        "Current CEO of OpenAI",
        "Recent AI policy updates in India"
    ]
    
    while True:
        console.print("\n[bold white]SELECT A DEMO OR ENTER CUSTOM QUERY:[/]")
        for i, d in enumerate(demos, 1):
             console.print(f"  [yellow]{i}[/]. {d}")
        console.print(f"  [yellow]4[/]. Custom Query")
        console.print(f"  [yellow]5[/]. Quit AXIOM")
        
        choice = input("\nChoice > ").strip()
        
        if choice == '5':
            console.print("\n[magenta]Terminating AXIOM session. Signal extraction complete.[/]")
            break
        elif choice in ['1', '2', '3']:
            query = demos[int(choice)-1]
        elif choice == '4':
            query = input("Custom Query > ").strip()
        else:
            console.print("[red]Invalid choice. Try again.[/]")
            continue
            
        if not query:
            continue
            
        run_axiom_demo(query, agent)

if __name__ == "__main__":
    main()
