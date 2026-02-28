"""
KurOS Main Application Module
Cherry Computer - KurOS v1.0.4
"""

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Placeholder
from textual.binding import Binding


class KurOS(App):
    """A simple KurOS-inspired terminal interface."""
    
    CSS = """
    #title {
        text-align: center;
        text-style: bold;
        color: #ff6b6b;
        padding: 1;
    }
    
    .status-bar {
        background: $surface;
        color: $text;
        padding: 1;
        text-align: center;
        border: solid $primary;
    }
    
    Placeholder {
        height: 10;
        border: solid $secondary;
        margin: 1;
    }
    """
    
    BINDINGS = [
        Binding("d", "toggle_dark", "Toggle dark mode"),
        Binding("q", "quit", "Shutdown"),
        Binding("ctrl+c", "quit", "Emergency shutdown", priority=True),
    ]
    
    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header(show_clock=True)
        yield Static("CHERRY COMPUTER - KurOS v1.0.4", id="title")
        yield Static("SYSTEM STATUS: OPTIMAL", classes="status-bar")
        yield Placeholder("System Logs")
        yield Placeholder("Network Traffic")
        yield Footer()
    
    def action_toggle_dark(self) -> None:
        """Toggle between dark and light themes."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )
        self.notify(f"Switched to {'dark' if self.theme == 'textual-dark' else 'light'} mode")


def main() -> None:
    """Entry point for the kuros console script."""
    app = KurOS()
    app.run()


if __name__ == "__main__":
    main()
