import typer
from midicka.core import Core
from midicka.logger import configure_logs


app = typer.Typer()


@app.command()
def play(file_path: str, port_name: str = None):
    typer.echo(f"Playing from file {file_path} on output port {port_name}")
    core = Core(output_port_name=port_name)
    core.run(file_path)
    typer.echo("Playback finished.")

if __name__ == "__main__":
    configure_logs()
    app()
