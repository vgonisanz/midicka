import os
import typer
from midicka.keyboard_palette import KeyboardPalette
from midicka.logger import configure_logs

app = typer.Typer()

@app.command()
def listen(file_path: str = os.path.join("files", "mapping.json"),
           port_name: str = None):
    typer.echo(f"Listening input port {port_name} and writing mapping file {file_path}")
    ...
    typer.echo(f'\nData written to {file_path}')


if __name__ == "__main__":
    configure_logs()
    app()
