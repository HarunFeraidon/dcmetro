from .commands import process_message
from textual.app import App, ComposeResult
from textual.widgets import Input, Static, Footer
from textual.containers import Container


class InputRow(Static):
    CSS_PATH = "app.css"

    def compose(self) -> ComposeResult:
        self.query_widget = Static(classes="query")
        self.results_widget = Static(classes="results")
        yield self.query_widget
        yield self.results_widget

    def on_mount(self) -> None:
        self.query_widget.styles.border = ("heavy", "#F0EDCC")
        self.query_widget.styles.background = "#02343F"


class DcMetroApp(App):

    @classmethod
    def run_cli(cls):
        app = cls()
        app.run()
    
    BINDINGS = [
        ("-", "clear", "Clear Here"),
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        self.input_widget = Input(placeholder="Enter a command",
                                  classes="input-field")
        yield self.input_widget
        yield Container(InputRow(), id="results-container")
        yield Footer()

    def on_mount(self) -> None:
        """Called when app starts."""
        # Give the input focus, so we can start typing straight away
        self.query_one(Input).focus()

    def on_input_submitted(self, message: Input.Submitted) -> None:
        """A coroutine to handle a text changed message."""
        if message.value:
            result = process_message(message.value)
            self.query(".query").last().update(f"> {message.value}")
            self.query(".results").last().update(str(result))
            message.input.value = ""
            new_input = InputRow()
            self.query_one("#results-container").mount(new_input)
            new_input.scroll_visible()

    def action_clear(self) -> None:
        """Clear the input field and previous output."""
        input = self.query_one(".input-field")
        query = self.query(".query")
        result = self.query(".results")
        input.value = ""
        while result:
            result.last().remove()
            result = self.query(".results")
            query.last().remove()
            query = self.query(".query")
        self.query_one("#results-container").mount(InputRow())
