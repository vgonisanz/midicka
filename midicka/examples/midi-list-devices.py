import mido
import typer

app = typer.Typer()

@app.command()
def list_midi_inputs():
    input_ports = mido.get_input_names()
    typer.echo("Available MIDI Input Ports:")
    for index, port in enumerate(input_ports, start=1):
        typer.echo(f"{index}. {port}")

if __name__ == "__main__":
    app()
