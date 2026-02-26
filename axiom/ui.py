from rich.console import Console
from rich.panel import Panel
from rich.progress import SpinnerColumn, Progress, TextColumn
from rich.text import Text
from rich.table import Table
from rich.live import Live
from axiom.config import BRAND_COLOR, THOUGHT_COLOR, SUCCESS_COLOR, ERROR_COLOR

# Initialize global console with UTF-8 force
# On Windows, we sometimes need to force encoding
import sys
import io
if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

console = Console(force_terminal=True)

class AxiomUI:
    @staticmethod
    def show_header():
        """Shows the premium Axiom branding."""
        header_text = Text()
        header_text.append(" 🚀 AXIOM\n", style=f"bold {BRAND_COLOR}")
        header_text.append("  Live Fact-Synthesis Engine", style="italic white")
        
        panel = Panel(
            header_text,
            border_style=BRAND_COLOR,
            expand=False,
            padding=(1, 4)
        )
        console.print(panel)
        console.print("\n")

    @staticmethod
    def show_step(message: str, style=THOUGHT_COLOR):
        """Displays a specific action step with a marker."""
        console.print(f"[{style}]▶ {message}[/]")

    @staticmethod
    def show_error(message: str):
        """Displays a critical error message."""
        console.print(f"[{ERROR_COLOR}]✘ ERROR:[/] {message}")

    @staticmethod
    def show_final_answer(answer_text: str):
        """Displays the compressed high-signal synthesized facts."""
        console.print("\n")
        
        # Format the content into a table for premium feel
        table = Table.grid(padding=(0, 1))
        table.add_column(style=f"bold {SUCCESS_COLOR}") # Validated icon
        table.add_column(style="white") # Each bullet
        
        lines = answer_text.strip().split("\n")
        for line in lines:
            if line.strip():
                # Strip potential existing bullets for consistent styling
                clean_fact = line.lstrip("•-* ").strip()
                table.add_row("✅", clean_fact)

        panel = Panel(
            table,
            title="[bold green]SYNTHESIZED SIGNAL[/]",
            border_style=SUCCESS_COLOR,
            expand=False,
            padding=(1, 2)
        )
        console.print(panel)

    @staticmethod
    def show_thinking(agent_output_stream):
        """
        Placeholder for a streaming-friendly thinking display if needed.
        Currently can be handled via console.print in real-time.
        """
        pass
