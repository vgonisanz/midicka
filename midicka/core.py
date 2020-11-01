import rtmidi2

import structlog

logger = structlog.get_logger()

class Midicka:
    """
    Class to isolate midi class
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
    
    def send_message_out(self):
        self._midi_out.send_noteon(0, 48, 100)

    def info(self):
        logger.info("midi_in_ports", names=','.join(self.in_ports))
        logger.info("midi_out_ports", names=','.join(self.out_ports))
