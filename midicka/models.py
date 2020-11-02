import rtmidi2

class MidiNote:
    NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    OCTAVES = list(range(11))
    NOTES_IN_OCTAVE = len(NOTES)
    NOTE_ERROR = "Bad Note"

    def __init__(self, note: str, octave: int):
        self._value = MidiNote.note_to_number(note, octave)

    def get(self):
        return self._value

    def get_note(self):
        return MidiNote.number_to_note(self._value)

    def number_to_note(number: int) -> tuple:
        """
        Require a valid MIDI number

        Returns
        -------
        note, octave: If valid
        """
        octave = number // MidiNote.NOTES_IN_OCTAVE
        assert octave in MidiNote.OCTAVES, MidiNote.NOTE_ERROR
        assert 0 <= number <= 127, MidiNote.NOTE_ERROR
        note = MidiNote.NOTES[number % MidiNote.NOTES_IN_OCTAVE]

        return note, octave

    def note_to_number(note: str, octave: int) -> int:
        """
        Require a valid note string and number

        Returns
        -------
        note: If valid
        """
        assert note in MidiNote.NOTES, MidiNote.NOTE_ERROR
        assert octave in MidiNote.OCTAVES, MidiNote.NOTE_ERROR

        note = MidiNote.NOTES.index(note)
        note += (MidiNote.NOTES_IN_OCTAVE * octave)

        assert 0 <= note <= 127, MidiNote.NOTE_ERROR

        return note

class Message():
    def __init__(self, midi_message: list):
        self._empty = False
        if midi_message == None:
            self._empty = True
            return None
        self._msg_type = rtmidi2.msgtype2str(midi_message[0])
        self._number = midi_message[1]
        self._velocity = midi_message[2]

    def get(self):
        if self._empty:
            return None, None, None
        note, octave = MidiNote.number_to_note(self._number)
        return self._msg_type, note, octave