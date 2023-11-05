import mido
import typer

app = typer.Typer()

@app.command()
def listen_to_midi(port_name: str = typer.Option(None, help="The name of the MIDI input port.")):
    typer.echo(f"Listening {port_name}")
    with mido.open_input(port_name) as inport:
        for msg in inport:
            typer.echo(msg)

if __name__ == "__main__":
    app()
