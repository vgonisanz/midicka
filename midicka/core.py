import time
import rtmidi2
import structlog

from midicka.models import MidiNote
from midicka.models import Message

logger = structlog.get_logger()

class Midicka:
    """
    Class to isolate midi class

    All notes input are in string format, from A0 (21) to C8 (108)

    Bibliography:
    - Notes midi snippets: https://gist.github.com/devxpy/063968e0a2ef9b6db0bd6af8079dad2a
    - Midi reference: https://newt.phys.unsw.edu.au/jw/notes.html
    """
    def __init__(self):
        self.in_ports = rtmidi2.get_in_ports()
        self.out_ports = rtmidi2.get_out_ports()

        self._midi_in = rtmidi2.MidiIn()
        self._midi_out = rtmidi2.MidiOut()

    def select_in_port(self, index):
        self._midi_in.close_port()
        self._midi_in.open_port(index)

    def select_out_port(self, index):
        self._midi_out.close_port()
        self._midi_out.open_port(index)
    
    def send_message_out(self, note: MidiNote, velocity: int):
        """
        We only support channel 0 of 8 right now
        """
        channel = 0
        self._midi_out.send_noteon(channel, note.get(), 100)
        self._midi_out.send_noteoff(channel, note.get())

    def receive_message_blocking(self):
        """
        Print messages until dead
        """
        # will block until a message is available
        while True:
            message = Message(self._midi_in.get_message())
            msg_type, note, octave = message.get()
            if msg_type:
                logger.info("got_message", note=note, octave=octave, msg_type=msg_type)
            time.sleep(0.01)

    def receive_message(self, callback):
        """
        Print messages until dead
        """
        self._midi_in.callback = callback
    
    def info(self):
        logger.info("midi_in_ports", names=','.join(self.in_ports))
        logger.info("midi_out_ports", names=','.join(self.out_ports))
