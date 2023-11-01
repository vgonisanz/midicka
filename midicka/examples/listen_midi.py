import mido
from mido import MidiFile, MidiTrack, Message

def listen_to_midi(port_name=None):
    with mido.open_input(port_name) as inport:
        for msg in inport:
            print(msg)

if __name__ == '__main__':
    # The argument to listen_to_midi is the name of your MIDI input port.
    # If it's None, mido will pick the first available port.
    listen_to_midi()