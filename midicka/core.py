import mido
from midicka.models import (
    KeyState,
    MidiMessage,
)

class Core:
    def __init__(self, port_name: str):
        self.port_name = port_name

    def read(self):
        with mido.open_input(self.port_name) as inport:
            for msg in inport:
                if msg.type == 'note_on':
                    state = KeyState.RELEASE if msg.velocity == 0 else KeyState.PRESS
                    msg_midi = MidiMessage(
                        channel=msg.channel,
                        note=msg.note,
                        state=state,
                        velocity=msg.velocity,
                        time=msg.time
                    )
                    yield msg_midi
