import typer
import structlog
from midicka.core import Core
from midicka.logger import configure_logs

logger = structlog.get_logger()
app = typer.Typer()

@app.command()
def listen_to_midi(port_name: str = typer.Option(None, help="The name of the MIDI input port.")):
    logger.info("Listening", port_name=port_name)
    core = Core(port_name)
    for msg in core.read():
        logger.info("MIDI message received", **msg.model_dump())

if __name__ == "__main__":
    configure_logs()
    app()
