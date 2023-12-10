import os
import typer
from midicka.keyboard_palette import KeyboardPalette, MidiKeyMapping
from midicka.logger import configure_logs
from pynput import keyboard


app = typer.Typer()


def get_key():
    with keyboard.Events() as events:
        event = events.get()
        if isinstance(event, keyboard.Events.Press):
            try:
                return event.key.char
            except AttributeError:
                return event.key.name
        return None


@app.command()
def listen(file_path: str = typer.Option(
                os.path.join("files", "mapping.json"), "--file-path", "-f"),
           port_name: str = typer.Option(
               None, "--port-name", "-p"),
           start_midi_note: int = typer.Option(
               60, "--start-midi-note", "-s"),
           end_midi_note: int = typer.Option(
               73, "--end-midi-note", "-e")):
    typer.echo(f"Listening input port {port_name} and writing mapping file {file_path}")

    palette = KeyboardPalette.generate_empty_palette()
    key_pressed = None
    for midi_number in range(start_midi_note, end_midi_note + 1):
        typer.echo(f"Press key for MIDI note {midi_number} (then press Enter): ", nl=False)
        while True:
            key_pressed = get_key()
            if key_pressed:
                break
        if key_pressed:
            request_key = True
            typer.echo(key_pressed)
            typer.echo(f"Assigning '{key_pressed}' to {midi_number}")
            palette.mappings.append(
                MidiKeyMapping(midi_note=midi_number, keyboard_key=key_pressed)
            )

    palette.save_to_file(file_path)
    typer.echo(f'\nData written to {file_path}')

if __name__ == "__main__":
    configure_logs()
    app()
