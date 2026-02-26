import sys
import io
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.theme import Theme
from cipher.config import PRIMARY_COLOR, THINKING_COLOR, TOOL_COLOR, SUCCESS_COLOR, ERROR_COLOR

# Force UTF-8 for PowerShell encoding stability
if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Define custom command-center theme
theme = Theme({
    "agent": f"bold {THINKING_COLOR}",
    "branding": f"bold {PRIMARY_COLOR}",
    "intelligence": f"bold {SUCCESS_COLOR}",
    "log": "white italic",
    "tool": f"bold {TOOL_COLOR}"
})

console = Console(theme=theme, force_terminal=True)

class CipherUI:
    @staticmethod
    def show_header():
        """Command-center branding for CIPHER."""
        header = Text()
        header.append("==================================================\n", style="branding")
        header.append(" 🔐 CIPHER\n", style="branding")
        header.append(" Autonomous Fact Intelligence Agent\n", style="branding")
        header.append("==================================================", style="branding")
        
        console.print(header)
        console.print("")

    @staticmethod
    def log_action(message: str, category: str = "agent"):
        """Prints a standardized lifecycle log."""
        prefix = f"[{category.upper()}]"
        console.print(f"[{category}]{prefix}[/] {message}")

    @staticmethod
    def show_error(message: str):
        """Displays critical failures in command-center red."""
        console.print(f"[{ERROR_COLOR}]✘ ERROR:[/] {message}")

    @staticmethod
    def present_intelligence(intelligence: str):
        """Presents synthesized fact-bullets in a premium block."""
        console.print("\n>>> INTELLIGENCE OUTPUT", style="intelligence")
        
        # Grid layout for clean bullets
        table = Table.grid(padding=(0, 1))
        table.add_column(style=f"bold {SUCCESS_COLOR}") 
        table.add_column(style="white")
        
        facts = intelligence.strip().split("\n")
        for fact in facts:
            if fact.strip():
                clean_fact = fact.lstrip("•-* ").strip()
                table.add_row("•", clean_fact)

        panel = Panel(
            table,
            border_style=SUCCESS_COLOR,
            expand=False,
            padding=(1, 2)
        )
        console.print(panel)
        console.print("")
