import os
import typer
from midicka.core import Core
from midicka.logger import configure_logs

app = typer.Typer()

@app.command()
def listen(file_path: str = os.path.join("files", "record.json"),
           port_name: str = None):
    typer.echo(f"Listening input port {port_name} and writing to file {file_path}")
    core = Core(input_port_name=port_name)
    core.write(core.read(), file_path)
    typer.echo(f'\nData written to {file_path}')


if __name__ == "__main__":
    configure_logs()
    app()
