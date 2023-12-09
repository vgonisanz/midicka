import time
import mido
import json
import structlog
from pynput.keyboard import (
    Controller,
    Key
)


from midicka.models import (
    KeyState,
    MidiMessage
)
from midicka.keyboard_palette import KeyboardPalette


logger = structlog.get_logger()


class Core:
    def __init__(self, input_port_name: str = None, output_port_name: str = None):
        self.input_port_name = input_port_name
        self.output_port_name = output_port_name
        self.keyboard = Controller()
        self.keyboard_palette = None

    def list_midi_devices(self):
        print("MIDI Input Devices:")
        for input_name in mido.get_input_names():
            print(f"'{input_name}'")

        print("\nMIDI Output Devices:")
        for output_name in mido.get_output_names():
            print(f"'{output_name}'")

    def read(self):
        with mido.open_input(self.input_port_name) as inport:
            start_time = time.time()

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
                        time=msg.time,
                        relative_time = time.time() - start_time 
                    )
                    yield msg_midi
    
    def write(self, midi_messages, file_path):
        midi_data = [json.loads(msg.json()) for msg in midi_messages]

        with open(file_path, 'w') as file:
            json.dump(midi_data, file, indent=4)

    def play(self, file_path: str):
        with open(file_path, 'r') as file:
            midi_data = [MidiMessage(**msg) for msg in json.load(file)]

        with mido.open_output(self.output_port_name) as outport:
            for msg in midi_data:
                logger.info("midi_msg_play", **msg.dict())
                if msg.state == KeyState.PRESS:
                    midi_msg = mido.Message('note_on', note=msg.note, velocity=msg.velocity, time=0)
                    outport.send(midi_msg)
                    time.sleep(msg.relative_time)

    def run(self, mapping_file: str):
        """Run the core to listen midi and traslate keys"""
        logger.info("run", mapping_file=mapping_file)
        self.keyboard_palette = KeyboardPalette.generate_default_palette()
        for msg in self.read():
            logger.debug("midi_msg_run", **msg.model_dump())
            key_str = self.keyboard_palette.get_key(msg.note)
            if key_str == "":
                continue
            try:
                key = getattr(Key, key_str, key_str)
                logger.debug("Mapping", key=key, state=msg.state)
                if msg.state == KeyState.PRESS:
                    self.keyboard.press(key)
                elif msg.state == KeyState.RELEASE:
                    self.keyboard.release(key)
            except AttributeError:
                logger.debug(f"key_press_invalid_key", key=key_str)
