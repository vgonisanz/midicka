import mido
import json


from midicka.models import (
    KeyState,
    MidiMessage,
)


class Core:
    def __init__(self, input_port_name: str = None, output_port_name: str = None):
        self.input_port_name = input_port_name
        self.output_port_name = output_port_name

    def list_midi_devices(self):
        print("MIDI Input Devices:")
        for input_name in mido.get_input_names():
            print(f"'{input_name}'")

        print("\nMIDI Output Devices:")
        for output_name in mido.get_output_names():
            print(f"'{output_name}'")

    def read(self):
        with mido.open_input(self.input_port_name) as inport:
            for msg in inport:
                # Windows ñapa, not take signal TERM
                if msg.type == 'note_on' and msg.note == 21:
                    self.stop_recording = True
                    break
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
    
    def write(self, midi_messages, file_path):
        midi_data = [json.loads(msg.json()) for msg in midi_messages]

        with open(file_path, 'w') as file:
            json.dump(midi_data, file, indent=4)

