import json
import structlog
from typing import List
from pydantic import (
    FilePath,
    BaseModel
)
from midicka.models import MidiKeyMapping


logger = structlog.get_logger()


class KeyboardPalette(BaseModel):
    mappings: List[MidiKeyMapping] = []

    def get_key(self, midi_note: int) -> str:
        for mapping in self.mappings:
            if mapping.midi_note == midi_note:
                return mapping.keyboard_key
        return ""

    def save_to_file(self, file_path: FilePath):
        logger.info("save_to_file", path=file_path)
        with open(file_path, "w") as file:
            json.dump(self.dict(), file, indent=4)

    @classmethod
    def load_from_file(cls, file_path: FilePath = FilePath()):         
        logger.info("load_from_file", path=file_path)
        with open(file_path, "r") as file:
            data = json.load(file)
        return cls(**data)

    @classmethod
    def generate_default_palette(cls) -> 'KeyboardPalette':
        default_mappings = [
            MidiKeyMapping(midi_note=60, keyboard_key='a'),
            MidiKeyMapping(midi_note=61, keyboard_key='s')
        ]
        return cls(mapping=default_mappings)

    @classmethod
    def generate_empty_palette(cls) -> 'KeyboardPalette':
        return cls(mapping=[])
