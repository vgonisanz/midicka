import mido
import typer
from pydantic import BaseModel, confloat, root_validator
from enum import Enum
import structlog

structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.dev.ConsoleRenderer()
    ],
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)

log = structlog.get_logger()

class ChannelEnum(str, Enum):
    ch0 = "0"
    ch1 = "1"
    ch2 = "2"
    ch3 = "3"
    ch4 = "4"
    ch5 = "5"
    ch6 = "6"
    ch7 = "7"
    ch8 = "8"

class MidiMessage(BaseModel):
    channel: ChannelEnum
    note: str
    velocity: confloat(ge=0, le=1)
    time: int

    @root_validator(pre=True)
    def convert_note_number_to_notation(cls, values):
        note_number = values.get("note")
        note_notation = note_number_to_notation(int(note_number))
        note, octave_str = note_notation[:-1], note_notation[-1]
        octave = int(octave_str)
        values["note"] = NoteOctaveStruct(note=note, octave=octave)
        return values

class NoteOctaveStruct(BaseModel):
    note: str
    octave: int

def pretty_print_message(midi_message: MidiMessage):
    log.info(
        "MIDI Message",
        channel=midi_message.channel,
        note=f"{midi_message.note.note}{midi_message.note.octave}",
        velocity=midi_message.velocity,
        time=midi_message.time
    )

def note_number_to_notation(note_number: int) -> str:
    note_names = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    octave = note_number // 12
    note = note_names[note_number % 12]
    return f"{note}{octave}"

app = typer.Typer()

def parse_midi_message(msg: mido.Message) -> MidiMessage:
    return MidiMessage(
        channel=f"ch{msg.channel}",
        note=str(msg.note),
        velocity=msg.velocity / 127,
        time=msg.time
    )

def list_midi_ports():
    typer.echo("Input Ports:")
    for port in mido.get_input_names():
        typer.echo(port)

    typer.echo("\nOutput Ports:")
    for port in mido.get_output_names():
        typer.echo(port)

@app.command()
def list():
    list_midi_ports()

@app.command()
def listen(port_name: str = typer.Option(..., '-i', '--in', help="The name of the MIDI input port")):
    with mido.open_input(port_name) as inport:
        typer.echo(f"Listening {port_name}")
        for msg in inport:
            if msg.type == 'note_on':
                midi_message = parse_midi_message(msg)
                pretty_print_message(midi_message)

if __name__ == '__main__':
    app()
