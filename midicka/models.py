from pydantic import BaseModel
from enum import Enum

class KeyState(Enum):
    PRESS = 1
    RELEASE = 0

    def __str__(self):
        return self.name


class MidiMessage(BaseModel):
    """
    note_on Event on Key Press:
        When a key is pressed on a MIDI keyboard, a note_on message is generated and sent to the
        MIDI receiver (e.g., a synthesizer or a computer).
        The note_on message contains several pieces of information:
            channel: Indicates which of the 16 MIDI channels the message belongs to. This allows
                     multiple instruments or voices to be controlled independently.
            note: Specifies which key was pressed, corresponding to a particular pitch.
            velocity: Indicates how hard the key was pressed, often corresponding to the loudness
                      of the note.
            time: In some contexts, indicates the time at which the message was sent or should be
                  processed.
    
    note_on Event on Key Release:
        It's common to use a note_on message with a velocity of 0 to indicate that a key has been
        released, as an alternative to sending a note_off message.
        This practice can simplify the processing of MIDI messages, as the receiver only needs to
        listen for note_on messages and treat a velocity of 0 as a key release.
    
    We are hold the state with an enum to be more easy to parse.
    """
    channel: int
    note: int
    state: KeyState
    velocity: int
    time: int

    class Config:
        json_encoders = {
            KeyState: lambda x: x.value
        }
